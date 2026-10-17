# -*- coding: utf-8 -*-
"""Commit the 2026-10-17 Meta for Business News slug sets, which watchlist_check.py does not handle."""
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
    "US shelf 1 added 1 removed: meta-nest-ai-creative-diversification IN at slot 1, "
    "game-changers-series-1 OUT of slot 12, the other eleven shift down one. One head-of-list event "
    "in a 12-slot window, not two rotations. US ceiling moves 15 Oct to 19 OCTOBER 2026, which is TWO "
    "DAYS IN THE FUTURE on both the card and the post's own header. That is a fourth distinct date "
    "artefact on this source and the first that is not a disagreement between two renderings; see "
    "Watchlist.md 2026-10-17. Never treat a future-dated card as a render fault, read the post. The new "
    "post was READ IN FULL and banked as CR-286 (Nest Commerce partner case study, no named advertiser "
    "and no counterfactual, figures not quotable). UK shelf 0 added 0 removed and identical in content "
    "and order to the 2026-10-16 read, ceiling still 10 Sep 2026, creator-marketing-whitepaper absent "
    "from slot 1 for a SECOND consecutive day so the 2026-10-10 alternation now has three flat days "
    "against it and must not be reported as a pattern. Transport: WebFetch on both locales, hrefs not "
    "titles, first attempt each, ELEVENTH consecutive browser-free read; playwright and "
    "playwright-arcads failed CONNECT_TIMEOUT at session start, playwright-higgsfield and "
    "playwright-metatech connected and were not needed."
)

d = json.load(io.open(CACHE, encoding="utf-8"))
p = d["pages"]["meta-business-news"]
p["last_checked"] = "2026-10-17"
p["result"] = NOTE
p["slugs_us_2026_10_17"] = US
p["slugs_uk_2026_10_17"] = UK
cum = set(p.get("slugs_seen_cumulative", [])) | set(US) | set(UK)
p["slugs_seen_cumulative"] = sorted(cum)
p["note_2026_10_17"] = NOTE
io.open(CACHE, "w", encoding="utf-8", newline="\n").write(
    json.dumps(d, indent=2, ensure_ascii=False)
)
print("meta-business-news committed; cumulative slugs now", len(cum))
