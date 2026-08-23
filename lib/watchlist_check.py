"""Daily watchlist checker for the Advertising Science research run.

Fetches the RSS/scrape sources listed in wiki/science/Watchlist.md, diffs them
against cache/watchlist-seen.json (schema: {"feeds": {name: {"links": [...]}},
"pages": {name: {...}}}), and prints a JSON summary on the last line.

Writes nothing unless --commit is passed, so a dry run is safe.

Sources that need a real browser (Meta for Business News returns HTTP 400 to a
plain fetch; TikTok Newsroom and blog are India geo-blocked) are NOT handled
here. See Watchlist.md.
"""
import json
import re
import sys
import urllib.request
import urllib.error
from pathlib import Path
from datetime import datetime, timezone

SKILL = Path(__file__).resolve().parent.parent
CACHE = SKILL / "cache"
SEEN = CACHE / "watchlist-seen.json"

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/127.0 Safari/537.36")

RSS = {
    "meta-engineering": "https://engineering.fb.com/feed/",
    "meta-newsroom": "https://about.fb.com/news/feed/",
    "google-ads-commerce": "https://blog.google/products/ads-commerce/rss/",
    "arxiv-cs-ir": "https://rss.arxiv.org/rss/cs.IR",
}

TIKTOK_SDK = "https://raw.githubusercontent.com/tiktok/tiktok-business-api-sdk/main/Changelog.md"
GOOGLE_ANN = "https://support.google.com/google-ads/announcements/9048695"
GOOGLE_ANN_CACHE = CACHE / "google-ads-announcements-today.html"

# arXiv filter, per Watchlist.md (tightened 2026-08-19). A bank-list hit is
# required; recommend/ranking/retrieval alone never qualify.
BANK_RE = re.compile("|".join([
    r"advertis", r"\bads?\b", r"ad auction", r"sponsored", r"click-through rate",
    r"CTR prediction", r"bid landscape", r"bidding", r"conversion lift",
    r"incrementality", r"budget pacing", r"creative selection", r"\bGSP\b",
    r"second-price",
]), re.I)


def fetch(url, timeout=45):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.status, r.read().decode("utf-8", "replace")


def strip_tags(s):
    return re.sub(r"<[^>]+>", " ", s.replace("<![CDATA[", "").replace("]]>", "")).strip()


def parse_items(xml):
    out = []
    blocks = re.findall(r"<item[\s>].*?</item>", xml, re.S) or \
             re.findall(r"<entry[\s>].*?</entry>", xml, re.S)
    for b in blocks:
        m = re.search(r"<link[^>]*>(.*?)</link>", b, re.S)
        link = strip_tags(m.group(1)) if m else ""
        if not link:
            href = re.search(r'<link[^>]*href="([^"]+)"', b)
            link = href.group(1) if href else ""
        t = re.search(r"<title[^>]*>(.*?)</title>", b, re.S)
        d = re.search(r"<(?:description|summary)[^>]*>(.*?)</(?:description|summary)>", b, re.S)
        out.append({
            "link": link,
            "title": strip_tags(t.group(1)) if t else "",
            "desc": strip_tags(d.group(1)) if d else "",
        })
    return out


def visible_text(html):
    """Strip script/style then tags, per the 2026-08-20 google-announcements method."""
    html = re.sub(r"<(script|style)[\s>].*?</\1>", " ", html, flags=re.S | re.I)
    text = re.sub(r"<[^>]+>", "\n", html)
    return [ln.strip() for ln in text.splitlines() if ln.strip()]


def main():
    commit = "--commit" in sys.argv
    seen = json.loads(SEEN.read_text(encoding="utf-8-sig")) if SEEN.exists() else {}
    feeds = seen.setdefault("feeds", {})
    pages = seen.setdefault("pages", {})
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    report = {"date": today, "sources": {}, "errors": []}

    for name, url in RSS.items():
        entry = feeds.setdefault(name, {"url": url, "links": []})
        prev = set(entry.get("links", []))
        try:
            status, body = fetch(url)
        except Exception as e:
            report["sources"][name] = {"status": "ERROR"}
            report["errors"].append(f"{name}: {type(e).__name__}: {e}")
            continue
        items = parse_items(body)
        fresh = [i for i in items if i["link"] and i["link"] not in prev]
        build = re.search(r"<lastBuildDate>(.*?)</lastBuildDate>", body)

        rec = {"status": status, "in_feed": len(items), "new_links": len(fresh)}
        if build:
            rec["feed_build"] = build.group(1)
        if name == "arxiv-cs-ir":
            kept = [i for i in fresh if BANK_RE.search(i["title"] + " " + i["desc"])]
            rec["passed_ad_filter"] = len(kept)
            rec["items"] = [i["title"][:180] for i in kept]
            if "<skipDays>" in body:
                rec["skip_days"] = re.findall(r"<day>(\w+)</day>", body)
        else:
            rec["items"] = [{"title": i["title"][:180], "link": i["link"]} for i in fresh[:25]]
        report["sources"][name] = rec

        if commit:
            entry["url"] = url
            entry["last_checked"] = today
            entry["item_count"] = len(items)
            entry["links"] = sorted(prev | {i["link"] for i in items if i["link"]})

    # TikTok SDK changelog: version-string diff, the only TikTok route that answers.
    try:
        status, body = fetch(TIKTOK_SDK)
        vers = re.findall(r"^##\s+v?(\d+\.\d+\.\d+)", body, re.M)
        base = pages.get("tiktok-sdk-changelog", {}).get("baseline_version")
        report["sources"]["tiktok-sdk-changelog"] = {
            "status": status, "top_version": vers[0] if vers else None,
            "baseline_version": base, "changed": bool(vers) and vers[0] != base,
        }
        if commit and vers:
            pages.setdefault("tiktok-sdk-changelog", {}).update(
                {"last_checked": today, "baseline_version": vers[0],
                 "method": "raw.githubusercontent.com", "result": f"HTTP {status}, top version {vers[0]}"})
    except Exception as e:
        report["sources"]["tiktok-sdk-changelog"] = {"status": "ERROR"}
        report["errors"].append(f"tiktok-sdk-changelog: {type(e).__name__}: {e}")

    # Google Ads announcements: visible-text diff against yesterday's cached copy.
    try:
        status, body = fetch(GOOGLE_ANN)
        new_lines = visible_text(body)
        old_lines = visible_text(GOOGLE_ANN_CACHE.read_text(encoding="utf-8", errors="replace")) \
            if GOOGLE_ANN_CACHE.exists() else []
        added = [ln for ln in new_lines if ln not in set(old_lines)]
        removed = [ln for ln in old_lines if ln not in set(new_lines)]
        report["sources"]["google-ads-announcements"] = {
            "status": status, "lines_now": len(new_lines), "lines_cached": len(old_lines),
            "added": len(added), "removed": len(removed),
            "added_sample": added[:20], "removed_sample": removed[:20],
        }
        if commit:
            GOOGLE_ANN_CACHE.write_text(body, encoding="utf-8")
            pages.setdefault("google-ads-announcements", {}).update(
                {"last_checked": today, "method": "plain fetch; visible-text diff after stripping script/style",
                 "result": f"{len(new_lines)} visible lines, {len(added)} added, {len(removed)} removed"})
    except Exception as e:
        report["sources"]["google-ads-announcements"] = {"status": "ERROR"}
        report["errors"].append(f"google-ads-announcements: {type(e).__name__}: {e}")

    if commit:
        seen["last_run"] = datetime.now().strftime("%Y-%m-%dT%H:%M IST")
        SEEN.write_text(json.dumps(seen, indent=2), encoding="utf-8")
        report["committed"] = True

    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
