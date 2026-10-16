# -*- coding: utf-8 -*-
"""2026-10-16: record the Meta for Business News read.

This source is NOT in watchlist_check.py (it returns HTTP 400 to a plain fetch
and needs WebFetch against two explicit locales), so --commit never touches it.
Per the 2026-10-15 second-pass finding, it has to be written by hand or it
silently goes unread behind a log that looks complete.
"""
import json
from pathlib import Path

CACHE = Path(r"E:\claude code marketing skill\.claude\skills\advertising-science\cache\watchlist-seen.json")

US = [
    "meta-brand-building-summit-2026",
    "muse-smb-bennett-orchards",
    "a-new-way-for-businesses-and-personal-agents-to-work-together",
    "advertising-week-new-york-2026",
    "agency-awards-2026",
    "introducing-meta-one-plans-for-businesses",
    "iab-global-creator-week-making-it-easier-for-businesses-to-partner-with-creators",
    "performance-spotlight-how-instant-hydration-built-a-system-for-ai-to-scale",
    "businesses-driving-results-with-meta-ai-ads",
    "sydney-sock-project-scaled-cause",
    "meta-ai-for-small-businesses",
    "game-changers-series-1",
]
UK = [
    "performance-spotlight-how-instant-hydration-built-a-system-for-ai-to-scale",
    "businesses-driving-results-with-meta-ai-ads",
    "closing-the-creator-measurement-gap",
    "2026-winning-hearts-boosting-carts",
    "conversations-2026-introducing-meta-business-agent",
    "social-search-series-2",
    "social-search-series-3",
    "social-search-series-1",
    "2026-trends-from-around-the-world",
    "meta-growth-drivers-putting-your-digital-marketing-strategy-on-auto-pilot",
    "cyber-5-2025-what-worked",
    "unlocking-the-value-of-q5marketing-for-mobile-game-developers",
]

d = json.loads(CACHE.read_text(encoding="utf-8-sig"))
rec = d["pages"]["meta-business-news"]
prev_us = rec["slugs_us_2026_10_15"]
prev_uk = rec["slugs_uk_2026_10_15"]

added_us = [s for s in US if s not in prev_us]
removed_us = [s for s in prev_us if s not in US]
added_uk = [s for s in UK if s not in prev_uk]
removed_uk = [s for s in prev_uk if s not in UK]

rec["slugs_us_2026_10_16"] = US
rec["slugs_uk_2026_10_16"] = UK
rec["last_checked"] = "2026-10-16"
rec["result"] = (
    "US shelf 1 added 1 removed: meta-brand-building-summit-2026 IN at slot 1, "
    "laura-geller-creative-volume OUT of slot 12, the other eleven shift down one. "
    "Single head-of-list event in a 12-slot window. US ceiling moves 8 Oct to 15 Oct 2026. "
    "The new post was READ IN FULL and banked as MD-181, AT-127, plus merges into MD-162 and AU-032. "
    "UK shelf 0 added 0 removed and identical in order to the 2026-10-15 read, ceiling still 10 Sep 2026."
)
rec["note_2026_10_16"] = (
    "ALTERNATION FALSIFIER, n now 5 and it SURVIVES. The UK shelf did not move today, so the "
    "head-of-list alternation seen on 2026-10-08, 10-10, 10-12 and 10-15 is not a daily metronome. "
    "Two consecutive daily reads (10-15, 10-16) exist for the first time since the gap opened. "
    "Do not report the pattern as holding; it now has one flat day in it. "
    "Transport: WebFetch on both ?locale=en_US and ?locale=en_GB, first attempt each, hrefs requested "
    "rather than titles, tenth consecutive browser-free read of both shelves."
)
cum = set(rec.get("slugs_seen_cumulative", []))
cum |= set(US) | set(UK)
rec["slugs_seen_cumulative"] = sorted(cum)

CACHE.write_text(json.dumps(d, indent=2), encoding="utf-8")
print("US added", added_us, "removed", removed_us)
print("UK added", added_uk, "removed", removed_uk)
print("cumulative slugs", len(cum))
