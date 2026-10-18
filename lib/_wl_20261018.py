# -*- coding: utf-8 -*-
"""Commit the 2026-10-18 Meta for Business News slug sets, which watchlist_check.py does not handle."""
import io
import json
from pathlib import Path

CACHE = Path(".claude/skills/advertising-science/cache/watchlist-seen.json")

US = [
    "meta-nest-ai-creative-diversification",
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

NOTE = (
    "Both shelves 0 added 0 removed, identical in content AND order to the 2026-10-17 read. US ceiling "
    "still 19 October 2026, UK ceiling still 10 September 2026. ONE REFINEMENT to the 2026-10-17 "
    "future-date finding: the card read 19 October on 17 Oct (two days ahead) and reads 19 October "
    "again today (one day ahead), so the future date is a FIXED published date that the clock is "
    "catching up to, not a rolling render offset. A future-dated card should therefore be read once and "
    "then left alone; it does not need re-reading each day until the date passes. UK: "
    "creator-marketing-whitepaper absent from slot 1 for a THIRD consecutive day, so the 2026-10-10 "
    "head-of-list alternation now has four flat days against it and is retired as a pattern. Transport: "
    "WebFetch on both locales, hrefs not titles, first attempt each, TWELFTH consecutive browser-free "
    "read. Every playwright server failed CONNECT_TIMEOUT at session start and no browser was needed. "
    "The bare URL was not read."
)

d = json.load(io.open(CACHE, encoding="utf-8"))
p = d["pages"]["meta-business-news"]
p["last_checked"] = "2026-10-18"
p["result"] = NOTE
p["slugs_us_2026_10_18"] = US
p["slugs_uk_2026_10_18"] = UK
cum = set(p.get("slugs_seen_cumulative", [])) | set(US) | set(UK)
p["slugs_seen_cumulative"] = sorted(cum)
p["note_2026_10_18"] = NOTE
io.open(CACHE, "w", encoding="utf-8", newline="\n").write(
    json.dumps(d, indent=2, ensure_ascii=False)
)
print("meta-business-news committed; cumulative slugs now", len(cum))
