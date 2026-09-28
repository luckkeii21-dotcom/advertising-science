"""Monday weekly-lane fetch for the 2026-09-28 research run."""
import json, re, sys, urllib.request, urllib.error
from pathlib import Path

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/127.0 Safari/537.36")
CACHE = Path(r"E:\claude code marketing skill\.claude\skills\advertising-science\cache")

SRC = {
  "meta-marketing-api-changelog": "https://developers.facebook.com/docs/marketing-api/marketing-api-changelog",
  "meta-graph-api-changelog": "https://developers.facebook.com/docs/graph-api/changelog",
  "meta-ad-standards": "https://transparency.meta.com/policies/ad-standards/",
  "google-ads-api-release-notes": "https://developers.google.com/google-ads/api/docs/release-notes",
  "google-ads-dev-blog": "http://feeds.feedburner.com/GoogleAdsDeveloperBlog",
  "merchant-center-changelog": "https://support.google.com/merchants/announcements/6192467",
  "ai-meta-blog": "https://ai.meta.com/blog/",
}

def fetch(url, timeout=60):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*",
                                               "Accept-Language": "en-US,en;q=0.9"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.status, r.read().decode("utf-8", "replace")

out = {}
for name, url in SRC.items():
    rec = {"url": url}
    try:
        st, body = fetch(url)
        rec["status"] = st
        rec["bytes"] = len(body)
        p = CACHE / f"wk-{name}.html"
        prev = p.read_text("utf-8", "replace") if p.exists() else None
        rec["had_cache"] = prev is not None
        rec["changed"] = (prev != body) if prev is not None else None
        p.write_text(body, "utf-8")
        # version strings
        vers = sorted(set(re.findall(r"\bv(\d{2}\.0)\b", body)), key=lambda s: float(s), reverse=True)
        if vers:
            rec["versions_top5"] = vers[:5]
        # dates
        dates = re.findall(r"\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+20\d{2}", body)
        if dates:
            rec["dates_first5"] = dates[:5]
        # rss titles
        if "feedburner" in url or "<rss" in body[:400] or "<feed" in body[:400]:
            titles = re.findall(r"<title[^>]*>(.*?)</title>", body, re.S)
            rec["titles"] = [re.sub(r"<[^>]+>", "", t).strip()[:140] for t in titles[:12]]
    except Exception as e:
        rec["error"] = f"{type(e).__name__}: {e}"
    out[name] = rec

print(json.dumps(out, indent=2)[:12000])
