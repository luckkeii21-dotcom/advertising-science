#!/usr/bin/env python
"""Ad-hoc YouTube research instrument for new-client market research.

harvest.py walks a fixed roster of advertising channels every morning.
This is the other half: point it at ANY vertical, any query, any video, and
pull back the three things market research actually needs.

  search   discover what the market watches, with triage data
  pull     transcript + metadata for one or many video URLs or ids
  comments the unfiltered voice of the customer, sorted by top

Everything here is verified working on this machine (2026-08-22).

Visuals are handled outside this file. Three verified routes, cheapest first:
  1. storyboards, no video download:
       yt_dlp -f sb0 -o "sb_%(id)s.%(ext)s" <url>
       then sb_frames.py and contact_sheet.py in this same lib
  2. full download, when you need real resolution or frame-accurate beats:
       yt_dlp --extractor-args "youtube:player_client=android" -f "bv*[height<=720]+ba/b"
       then ffmpeg -vf "fps=1/15,scale=480:-1,tile=3x2"
     The android player client is the flag that clears the 403. The default
     android_vr client, web_safari, tv and ios all fail.
  3. Playwright element screenshot, when you must READ small on-screen text.

Usage
  P="E:\\claude code marketing skill\\.venv-research\\Scripts\\python.exe"
  $P .claude\\skills\\advertising-science\\lib\\ytresearch.py search "what does sciatica feel like" --n 25
  $P .claude\\skills\\advertising-science\\lib\\ytresearch.py pull <url-or-id> [...] --out "<dir>"
  $P .claude\\skills\\advertising-science\\lib\\ytresearch.py comments <url-or-id> --max 300 --out "<dir>"

Writes markdown into --out (default: a client research folder you pass in).
Prints a JSON summary as the last stdout line so an agent can parse it.
"""
import argparse
import html
import io
import json
import os
import re
import subprocess
import sys
import tempfile

# Windows consoles default to cp1252 and YouTube text is full of emoji.
if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

SUB_LANGS = "en,en-US,en-GB,en-orig"


def ydl(args, timeout=600):
    """Run yt-dlp as a module using whatever python is running this file."""
    cmd = [sys.executable, "-m", "yt_dlp"] + args
    return subprocess.run(cmd, capture_output=True, text=True,
                          encoding="utf-8", errors="replace", timeout=timeout)


def vid_id(s):
    s = s.strip()
    m = re.search(r"(?:v=|youtu\.be/|/shorts/|/embed/)([A-Za-z0-9_-]{11})", s)
    if m:
        return m.group(1)
    return s if re.fullmatch(r"[A-Za-z0-9_-]{11}", s) else None


def slug(t, n=70):
    t = re.sub(r"[^\w\s-]", "", (t or "untitled")).strip()
    return re.sub(r"[-\s]+", "-", t)[:n].strip("-").lower() or "untitled"


def clean_vtt(path):
    """VTT to clean prose. Drops cue timings, tags, and the rolling duplicate
    lines that auto-captions emit."""
    out, seen = [], None
    with open(path, encoding="utf-8", errors="replace") as f:
        for line in f:
            line = line.strip()
            if (not line or line.startswith(("WEBVTT", "Kind:", "Language:", "NOTE"))
                    or "-->" in line or line.isdigit()):
                continue
            line = re.sub(r"<[^>]+>", "", line)
            line = html.unescape(line).strip()
            if line and line != seen:
                out.append(line)
                seen = line
    text = " ".join(out)
    return re.sub(r"\s+", " ", text).strip()


def cmd_search(a):
    """Discovery with triage data. Sorted by views so you transcribe the
    videos the market actually watched."""
    rows = []
    for q in a.query:
        r = ydl(["--flat-playlist", "--dump-json", f"ytsearch{a.n}:{q}"])
        for line in r.stdout.splitlines():
            try:
                d = json.loads(line)
            except Exception:
                continue
            rows.append({
                "query": q,
                "id": d.get("id"),
                "title": d.get("title"),
                "channel": d.get("channel") or d.get("uploader"),
                "views": d.get("view_count") or 0,
                "duration_s": d.get("duration") or 0,
                "url": d.get("url") or f"https://www.youtube.com/watch?v={d.get('id')}",
            })
    rows.sort(key=lambda x: x["views"], reverse=True)

    if a.out:
        os.makedirs(a.out, exist_ok=True)
        p = os.path.join(a.out, "youtube-discovery.md")
        with open(p, "w", encoding="utf-8") as f:
            f.write("# YouTube discovery\n\n")
            f.write(f"Queries: {'; '.join(a.query)}\n\n")
            f.write("| Views | Min | Channel | Title | URL |\n|--:|--:|---|---|---|\n")
            for x in rows:
                f.write(f"| {x['views']:,} | {round((x['duration_s'] or 0)/60)} | "
                        f"{x['channel']} | {x['title']} | {x['url']} |\n")
        print(f"wrote {p}", file=sys.stderr)

    for x in rows[:40]:
        print(f"{x['views']:>9,} | {round((x['duration_s'] or 0)/60):>3}m | "
              f"{x['channel']} | {x['title']} | {x['url']}")
    print(json.dumps({"mode": "search", "results": len(rows),
                      "out": a.out, "rows": rows}))


def cmd_pull(a):
    """Transcript + metadata for each video. Captions only; if a video has
    none, it is reported so you can decide whether whisper is worth the time."""
    os.makedirs(a.out, exist_ok=True)
    done, missing = [], []
    for raw in a.videos:
        v = vid_id(raw)
        if not v:
            missing.append({"input": raw, "why": "unparseable id"})
            continue
        with tempfile.TemporaryDirectory() as td:
            r = ydl(["--skip-download", "--write-auto-sub", "--write-sub",
                     "--sub-lang", SUB_LANGS, "--sub-format", "vtt",
                     "--write-info-json", "-o", os.path.join(td, "%(id)s.%(ext)s"),
                     f"https://www.youtube.com/watch?v={v}"])
            info, meta = None, {}
            for fn in os.listdir(td):
                if fn.endswith(".info.json"):
                    info = os.path.join(td, fn)
            if info:
                with open(info, encoding="utf-8", errors="replace") as f:
                    meta = json.load(f)
            vtts = sorted(fn for fn in os.listdir(td) if fn.endswith(".vtt"))
            if not vtts:
                missing.append({"input": raw, "id": v,
                                "title": meta.get("title"),
                                "why": "no captions available",
                                "stderr": (r.stderr or "")[-300:]})
                continue
            # prefer a manual track over the auto one when both exist
            pick = next((x for x in vtts if ".en.vtt" in x and "orig" not in x), vtts[0])
            text = clean_vtt(os.path.join(td, pick))

        title = meta.get("title") or v
        name = f"{(meta.get('upload_date') or '00000000')}--{v}--{slug(title)}.md"
        p = os.path.join(a.out, name)
        with open(p, "w", encoding="utf-8") as f:
            f.write("---\n")
            f.write(f'video_id: "{v}"\n')
            f.write(f'title: "{(title or "").replace(chr(34), chr(39))}"\n')
            f.write(f'channel: "{(meta.get("channel") or "").replace(chr(34), chr(39))}"\n')
            f.write(f"upload_date: {meta.get('upload_date')}\n")
            f.write(f"views: {meta.get('view_count')}\n")
            f.write(f"duration_s: {meta.get('duration')}\n")
            f.write(f"url: https://www.youtube.com/watch?v={v}\n")
            f.write(f"words: {len(text.split())}\n")
            f.write("extracted: false\n")
            f.write("---\n\n")
            f.write(f"# {title}\n\n{text}\n")
        done.append({"id": v, "title": title, "words": len(text.split()), "path": p})
        print(f"ok  {len(text.split()):>6} words  {title}", file=sys.stderr)

    for m in missing:
        print(f"MISS  {m.get('title') or m['input']}  ({m['why']})", file=sys.stderr)
    print(json.dumps({"mode": "pull", "transcripts": done, "missing": missing,
                      "out": a.out}))


def cmd_comments(a):
    """Top comments. On a customer-problem video this is the least filtered
    voice-of-customer source that exists, and like counts give you a rough
    frequency signal on which complaint is the loudest."""
    os.makedirs(a.out, exist_ok=True)
    v = vid_id(a.video)
    if not v:
        print(json.dumps({"mode": "comments", "error": "unparseable id"}))
        return
    with tempfile.TemporaryDirectory() as td:
        ydl(["--skip-download", "--write-comments", "--write-info-json",
             "--extractor-args",
             f"youtube:max_comments={a.max},all,{a.replies};comment_sort=top",
             "-o", os.path.join(td, "%(id)s.%(ext)s"),
             f"https://www.youtube.com/watch?v={v}"], timeout=900)
        info = next((os.path.join(td, fn) for fn in os.listdir(td)
                     if fn.endswith(".info.json")), None)
        if not info:
            print(json.dumps({"mode": "comments", "error": "no info.json"}))
            return
        with open(info, encoding="utf-8", errors="replace") as f:
            meta = json.load(f)

    cs = meta.get("comments") or []
    cs.sort(key=lambda c: c.get("like_count") or 0, reverse=True)
    title = meta.get("title") or v
    p = os.path.join(a.out, f"comments--{v}--{slug(title)}.md")
    with open(p, "w", encoding="utf-8") as f:
        f.write("---\n")
        f.write(f'video_id: "{v}"\n')
        f.write(f'title: "{(title or "").replace(chr(34), chr(39))}"\n')
        f.write(f"url: https://www.youtube.com/watch?v={v}\n")
        f.write(f"comments_pulled: {len(cs)}\n")
        f.write(f"comments_total: {meta.get('comment_count')}\n")
        f.write("extracted: false\n")
        f.write("---\n\n")
        f.write(f"# Comments: {title}\n\n")
        f.write("Sorted by likes. Treat every line as a verbatim quote from a real\n")
        f.write("person in this market. Do not paraphrase them into your own words.\n\n")
        for c in cs:
            t = re.sub(r"\s+", " ", (c.get("text") or "")).strip()
            if t:
                f.write(f"- **[{c.get('like_count') or 0}]** {t}\n")
    print(f"wrote {p}  ({len(cs)} comments)", file=sys.stderr)
    print(json.dumps({"mode": "comments", "video_id": v, "pulled": len(cs),
                      "total": meta.get("comment_count"), "path": p}))


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("search", help="discover videos for a vertical")
    s.add_argument("query", nargs="+")
    s.add_argument("--n", type=int, default=20, help="results per query")
    s.add_argument("--out", default=None)
    s.set_defaults(fn=cmd_search)

    p = sub.add_parser("pull", help="transcripts for one or more videos")
    p.add_argument("videos", nargs="+", help="urls or 11-char ids")
    p.add_argument("--out", required=True)
    p.set_defaults(fn=cmd_pull)

    c = sub.add_parser("comments", help="top comments for one video")
    c.add_argument("video")
    c.add_argument("--max", type=int, default=300)
    c.add_argument("--replies", type=int, default=10)
    c.add_argument("--out", required=True)
    c.set_defaults(fn=cmd_comments)

    a = ap.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
