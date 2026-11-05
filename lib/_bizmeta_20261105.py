# Meta for Business News shelf read, pass 2 on 2026-11-04. Read-only, no cache write.
import io, json, re, urllib.request

CACHE = r"E:\claude code marketing skill\.claude\skills\advertising-science\cache\watchlist-seen.json"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36")
URLS = {
    "us": "https://www.facebook.com/business/news?locale=en_US",
    "uk": "https://en-gb.facebook.com/business/news",
}

cache = json.load(io.open(CACHE, encoding="utf-8"))
cum = set(cache.get("slugs_seen_cumulative", []))
print("cumulative seen:", len(cum))

for loc, url in URLS.items():
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA,
                                                   "Accept-Language": "en-US,en;q=0.9"})
        with urllib.request.urlopen(req, timeout=60) as r:
            body = r.read().decode("utf-8", "replace")
            status = r.status
    except Exception as e:
        print(loc, "FETCH FAILED:", type(e).__name__, e)
        continue
    slugs = sorted(set(re.findall(r"/business/news/([A-Za-z0-9][A-Za-z0-9\-]{4,})", body)))
    dates = re.findall(r"(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{1,2}),\s+(20\d\d)", body)
    prev = cache.get("slugs_%s_2026_11_05" % loc) or cache.get("slugs_%s_2026_11_04" % loc) or []
    new = [s for s in slugs if s not in cum]
    print("\n--", loc.upper(), "HTTP", status, len(body), "bytes")
    print("   slugs:", len(slugs), "| new vs cumulative:", len(new), new)
    print("   vs prev pinned set: added", [s for s in slugs if s not in prev],
          "removed", [s for s in prev if s not in slugs])
    print("   parseable card dates:", len(dates),
          "newest:", max(dates, key=lambda d: (int(d[2]), d[0])) if dates else "NONE")
