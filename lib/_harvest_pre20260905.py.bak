#!/usr/bin/env python
"""Advertising Science Engine: YouTube transcript harvester.

Modes:
  python harvest.py daily
      RSS scan of every roster channel (latest ~15 uploads each), fetch
      transcripts for videos not yet in state.json. Cheap; run every morning.

  python harvest.py backfill --days 30 [--channel SLUG] [--max 40]
      Walk each channel's /videos tab (long-form only; Shorts live on a
      separate tab and are excluded by construction) back N days.

Output: transcript markdown files in the vault at
  wiki/sources/transcripts/<channel-slug>/YYYY-MM-DD--<slug>--<title>.md
with `extracted: false` frontmatter so the extraction pass can find them.

State: state.json in the skill root records every video id ever handled so
nothing is fetched twice. A JSON run summary is printed as the LAST stdout
line and written to runs/<timestamp>-harvest.json.

Free: yt-dlp + RSS, no API keys. Uses whatever python runs it; launch with
the E-drive research venv python.
"""
import argparse
import glob
import html
import json
import os
import re
import subprocess
import sys
import tempfile
import time
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta

LIB_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_ROOT = os.path.dirname(LIB_DIR)
ROOT = os.path.abspath(os.path.join(SKILL_ROOT, "..", "..", ".."))
CHANNELS_FILE = os.path.join(SKILL_ROOT, "channels.json")
STATE_FILE = os.path.join(SKILL_ROOT, "state.json")
RUNS_DIR = os.path.join(SKILL_ROOT, "runs")
VAULT_TRANSCRIPTS = os.path.join(
    ROOT, "Obsidian God-level Marketing Vault", "God-level Marketing",
    "wiki", "sources", "transcripts")

MIN_SECONDS = 150          # below this it's a short/clip; record it, skip transcript
SLEEP_BETWEEN = 1.5        # be polite to YouTube
OLDER_STREAK_STOP = 3      # tolerate pinned old videos before stopping a channel walk


def load_json(path, default):
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    return default


def save_state(state):
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=1)


def rss_ids(channel_id):
    """Latest ~15 video ids from the channel's RSS feed, newest first."""
    url = f"https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        tree = ET.fromstring(r.read())
    ns = {"yt": "http://www.youtube.com/xml/schemas/2015"}
    return [e.text for e in tree.iter("{http://www.youtube.com/xml/schemas/2015}videoId")]


def tab_ids(ch, limit, tab="videos"):
    """Newest-first video ids from a channel tab (videos = long-form, no Shorts;
    streams = live VODs). Uses the channel-id URL, which never breaks the way
    handles can."""
    url = f"https://www.youtube.com/channel/{ch['channel_id']}/{tab}"
    cmd = [sys.executable, "-m", "yt_dlp", "--flat-playlist",
           "--playlist-end", str(limit), "--print", "%(id)s", url]
    out = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
    return [l.strip() for l in out.stdout.splitlines() if l.strip()]


def clean_vtt(path):
    lines = []
    with open(path, encoding="utf-8") as f:
        for raw in f:
            line = raw.strip()
            if not line or "-->" in line or line.startswith(
                    ("WEBVTT", "Kind:", "Language:", "NOTE")):
                continue
            line = re.sub(r"<[^>]+>", "", line)
            line = html.unescape(line)
            if lines and (line == lines[-1] or line in lines[-1]):
                continue
            lines.append(line)
    text = re.sub(r"\s+", " ", " ".join(lines)).strip()
    return text


def safe_title(title, maxlen=70):
    t = re.sub(r"[^\w\s-]", "", title, flags=re.UNICODE)
    t = re.sub(r"\s+", " ", t).strip()[:maxlen].strip()
    return t or "untitled"


def fetch_one(video_id, ch, tmpdir):
    """Fetch metadata + auto-subs for one video. Returns a record dict."""
    url = f"https://www.youtube.com/watch?v={video_id}"
    cmd = [sys.executable, "-m", "yt_dlp", "--no-simulate", "--skip-download",
           "--write-auto-sub", "--write-sub", "--sub-lang", "en,en-US,en-GB,en-orig",
           "--sub-format", "vtt", "-o", os.path.join(tmpdir, "%(id)s"),
           "--print", "%(upload_date)s|%(duration)s|%(channel)s|%(title)s", url]
    try:
        out = subprocess.run(cmd, capture_output=True, text=True, timeout=300,
                             encoding="utf-8", errors="replace")
    except subprocess.TimeoutExpired:
        return {"id": video_id, "status": "error", "error": "timeout"}
    line = (out.stdout or "").strip().splitlines()
    if not line:
        return {"id": video_id, "status": "error",
                "error": (out.stderr or "no output")[-300:]}
    try:
        upload_date, duration, channel_name, title = line[-1].split("|", 3)
        duration = int(float(duration)) if duration not in ("NA", "") else 0
    except ValueError:
        return {"id": video_id, "status": "error", "error": f"bad meta: {line[-1][:200]}"}
    pub = "unknown"
    if re.fullmatch(r"\d{8}", upload_date):
        pub = f"{upload_date[:4]}-{upload_date[4:6]}-{upload_date[6:]}"
    rec = {"id": video_id, "title": title, "published": pub,
           "duration": duration, "channel": ch["slug"]}
    if duration and duration < MIN_SECONDS:
        rec["status"] = "skipped_short"
        return rec
    vtts = glob.glob(os.path.join(tmpdir, f"{video_id}*.vtt"))
    if not vtts:
        rec["status"] = "no_subs"
        return rec
    text = clean_vtt(vtts[0])
    for v in vtts:
        os.remove(v)
    if len(text.split()) < 200:
        rec["status"] = "no_subs"
        return rec
    outdir = os.path.join(VAULT_TRANSCRIPTS, ch["slug"])
    os.makedirs(outdir, exist_ok=True)
    fname = f"{pub}--{ch['slug']}--{safe_title(title)}.md"
    fpath = os.path.join(outdir, fname)
    words = len(text.split())
    fm_title = title.replace('"', "'")
    md = (
        "---\n"
        f'title: "{fm_title}"\n'
        f"channel: {ch['name']}\n"
        f"channel_slug: {ch['slug']}\n"
        f"video_id: {video_id}\n"
        f"url: {url}\n"
        f"published: {pub}\n"
        f"duration_min: {round(duration / 60) if duration else 'unknown'}\n"
        f"words: {words}\n"
        f"harvested: {datetime.now().strftime('%Y-%m-%d')}\n"
        "extracted: false\n"
        "tags: [transcript, advertising-science]\n"
        "---\n\n"
        f"# {title}\n\n"
        f"Auto-transcript ({words} words). Source: {url}\n\n"
        f"{text}\n")
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(md)
    rec["status"] = "transcribed"
    rec["path"] = fpath
    rec["words"] = words
    return rec


def run(mode, days, only_channel, max_per_channel):
    channels = load_json(CHANNELS_FILE, {})["roster"]
    if only_channel:
        channels = [c for c in channels if c["slug"] == only_channel]
        if not channels:
            print(json.dumps({"error": f"unknown channel {only_channel}"}))
            sys.exit(1)
    state = load_json(STATE_FILE, {"seen": {}})
    cutoff = datetime.now() - timedelta(days=days)
    summary = {"mode": mode, "started": datetime.now().isoformat(timespec="seconds"),
               "new_transcripts": [], "skipped_short": 0, "no_subs": 0,
               "out_of_window": 0, "errors": [], "per_channel": {}}
    tmpdir = tempfile.mkdtemp(prefix="adsci-")
    for ch in channels:
        got = 0
        try:
            if mode == "daily":
                id_lists = [rss_ids(ch["channel_id"])]
            else:
                id_lists = [tab_ids(ch, max_per_channel)]
                if ch.get("include_streams"):
                    id_lists.append(tab_ids(ch, max_per_channel, tab="streams"))
        except Exception as e:
            summary["errors"].append(f"{ch['slug']}: listing failed: {e}")
            continue
        for ids in id_lists:
            older_streak = 0
            for vid in ids:
                if vid in state["seen"]:
                    continue
                rec = fetch_one(vid, ch, tmpdir)
                status = rec["status"]
                pub = rec.get("published", "unknown")
                in_window = True
                if pub != "unknown":
                    in_window = datetime.strptime(pub, "%Y-%m-%d") >= cutoff
                if not in_window:
                    older_streak += 1
                    if status == "transcribed" and os.path.exists(rec.get("path", "")):
                        os.remove(rec["path"])
                    state["seen"][vid] = {"status": "out_of_window", "channel": ch["slug"]}
                    summary["out_of_window"] += 1
                    save_state(state)
                    if mode == "backfill" and older_streak >= OLDER_STREAK_STOP:
                        break
                    continue
                older_streak = 0
                state["seen"][vid] = {"status": status, "channel": ch["slug"],
                                      "published": pub}
                save_state(state)
                if status == "transcribed":
                    summary["new_transcripts"].append(rec["path"])
                    got += 1
                elif status == "skipped_short":
                    summary["skipped_short"] += 1
                elif status == "no_subs":
                    summary["no_subs"] += 1
                else:
                    summary["errors"].append(f"{ch['slug']}/{vid}: {rec.get('error', '?')}")
                time.sleep(SLEEP_BETWEEN)
        summary["per_channel"][ch["slug"]] = got
        print(f"[{ch['slug']}] {got} new transcripts", file=sys.stderr)
    summary["finished"] = datetime.now().isoformat(timespec="seconds")
    os.makedirs(RUNS_DIR, exist_ok=True)
    stamp = datetime.now().strftime("%Y-%m-%d-%H%M")
    with open(os.path.join(RUNS_DIR, f"{stamp}-harvest.json"), "w",
              encoding="utf-8") as f:
        json.dump(summary, f, indent=1)
    print(json.dumps(summary))


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("mode", choices=["daily", "backfill"])
    p.add_argument("--days", type=int, default=None,
                   help="window in days (daily default 3, backfill default 30)")
    p.add_argument("--channel", default=None, help="limit to one roster slug")
    p.add_argument("--max", type=int, default=40,
                   help="backfill: max videos to inspect per channel")
    a = p.parse_args()
    days = a.days if a.days is not None else (3 if a.mode == "daily" else 30)
    run(a.mode, days, a.channel, a.max)
