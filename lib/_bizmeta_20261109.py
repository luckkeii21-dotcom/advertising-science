# Meta for Business News shelf read, 2026-11-09. Read-only, no cache write.
# Fixes the two defects on record: cumulative key path (defect_2026_11_05) and
# the UK day-first date pattern (note_2026_11_04_pass2_uk_date_format).
import io, json, re, urllib.request

CACHE = r"E:\claude code marketing skill\.claude\skills\advertising-science\cache\watchlist-seen.json"
OUT = r"E:\claude code marketing skill\.claude\skills\advertising-science\cache"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36")
URLS = {
    "us": "https://www.facebook.com/business/news?locale=en_US",
    "uk": "https://en-gb.facebook.com/business/news",
}
M = "January|February|March|April|May|June|July|August|September|October|November|December"
MONTHS = {m: i + 1 for i, m in enumerate(M.split("|"))}
US_RE = re.compile(r"(%s)\s+(\d{1,2})(?:st|nd|rd|th)?,\s+(20\d\d)" % M)
UK_RE = re.compile(r"(\d{1,2})(?:st|nd|rd|th)?\s+(%s)\s+(20\d\d)" % M)

cache = json.load(io.open(CACHE, encoding="utf-8"))
mbn = cache["pages"]["meta-business-news"]
cum = set(mbn.get("slugs_seen_cumulative", []))
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
    io.open("%s\bn-%s-20261109.html" % (OUT, loc), "w", encoding="utf-8").write(body)
    slugs = sorted(set(re.findall(r"/business/news/([A-Za-z0-9][A-Za-z0-9\-]{4,})", body)))
    d1 = [(MONTHS[a], int(b), int(c)) for a, b, c in US_RE.findall(body)]
    d2 = [(MONTHS[b], int(a), int(c)) for a, b, c in UK_RE.findall(body)]
    dates = d1 + d2
    prev = mbn.get("slugs_%s_2026_11_08" % loc) or []
    new = [s for s in slugs if s not in cum]
    print("\n--", loc.upper(), "HTTP", status, len(body), "bytes")
    print("   slugs:", len(slugs), "| new vs cumulative:", len(new), new)
    print("   vs 2026-11-08 set: added", [s for s in slugs if s not in prev],
          "removed", [s for s in prev if s not in slugs])
    print("   same order as 11-08:", slugs == sorted(prev) if prev else "n/a")
    print("   dates parsed:", len(dates), "US-form", len(d1), "UK-form", len(d2),
          "distinct", len(set(dates)))
    if dates:
        n = max(dates, key=lambda t: (t[2], t[0], t[1]))
        print("   newest card date: %04d-%02d-%02d" % (n[2], n[0], n[1]))
