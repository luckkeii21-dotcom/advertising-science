import json, pathlib
C = pathlib.Path(r"E:\claude code marketing skill\.claude\skills\advertising-science\cache\watchlist-seen.json")
d = json.loads(C.read_text(encoding="utf-8-sig"))
p = d["pages"].setdefault("meta-business-news", {})

# Second pass of 2026-10-09, read 14:50 IST. Both shelves identical to the
# 04:35 IST read of the same day, same slugs in the same order.
us = ['muse-smb-bennett-orchards','a-new-way-for-businesses-and-personal-agents-to-work-together',
      'advertising-week-new-york-2026','agency-awards-2026','introducing-meta-one-plans-for-businesses',
      'iab-global-creator-week-making-it-easier-for-businesses-to-partner-with-creators',
      'performance-spotlight-how-instant-hydration-built-a-system-for-ai-to-scale',
      'businesses-driving-results-with-meta-ai-ads','sydney-sock-project-scaled-cause',
      'meta-ai-for-small-businesses','game-changers-series-1','laura-geller-creative-volume']
uk = ['performance-spotlight-how-instant-hydration-built-a-system-for-ai-to-scale',
      'businesses-driving-results-with-meta-ai-ads','closing-the-creator-measurement-gap',
      '2026-winning-hearts-boosting-carts','conversations-2026-introducing-meta-business-agent',
      'social-search-series-2','social-search-series-3','social-search-series-1',
      '2026-trends-from-around-the-world',
      'meta-growth-drivers-putting-your-digital-marketing-strategy-on-auto-pilot',
      'cyber-5-2025-what-worked','unlocking-the-value-of-q5marketing-for-mobile-game-developers']

assert us == p["slugs_us_2026_10_09"], "US shelf moved since the morning read"
assert uk == p["slugs_uk_2026_10_09"], "UK shelf moved since the morning read"

p["slugs_us_2026_10_09_pass2"] = us
p["slugs_uk_2026_10_09_pass2"] = uk
p["last_checked"] = "2026-10-09 (pass 2, 14:50 IST)"
p["note_2026_10_09_pass2"] = (
    "Second read of both shelves 10 hours after the first, same calendar day. Both locales returned "
    "the identical 12 slugs in the identical order, so 0 added and 0 removed on each. US ceiling still "
    "8 October 2026, UK ceiling still 10 September 2026. The rotation that moved a UK slug out and back "
    "inside 24 hours is therefore NOT per-render and not sub-daily: it moves at most once a day. "
    "A same-day second pass buys nothing on this source and one read per day is sufficient.")

# Cumulative slug seen-set, the fix the morning entry asked for.
cum = set(p.get("slugs_seen_cumulative", []))
cum |= set(us) | set(uk)
for k, v in p.items():
    if k.startswith("slugs_us_") or k.startswith("slugs_uk_"):
        cum |= set(v)
p["slugs_seen_cumulative"] = sorted(cum)

C.write_text(json.dumps(d, indent=2), encoding="utf-8")
print(f"pass-2 baselines recorded, both shelves unchanged")
print(f"cumulative slug seen-set now {len(cum)} slugs")
