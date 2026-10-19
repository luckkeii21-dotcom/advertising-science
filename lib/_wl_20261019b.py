# -*- coding: utf-8 -*-
"""Second pass 2026-10-19: commit the Meta for Business News slug sets and the arXiv Monday build."""
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
    "creator-marketing-whitepaper",
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
]

NOTE = (
    "SECOND PASS 13:50 IST, and it overturns a finding the 03:38 pass made this morning. US shelf "
    "unchanged, 12 slugs, 0 added 0 removed, ceiling still 19 October 2026. UK shelf CHANGED between "
    "03:38 and 13:50 on the same day: creator-marketing-whitepaper (6 October 2026) is back at slot 1 "
    "and unlocking-the-value-of-q5marketing-for-mobile-game-developers dropped off the bottom. The "
    "03:38 pass read both shelves as identical in order to 2026-10-18 and retired the slot-1 "
    "alternation as a dead pattern after four flat days. IT IS NOT DEAD, it rotated later the same "
    "day. METHOD CONSEQUENCE: a single early-morning read does not see the whole day on the UK shelf, "
    "and a flat-day streak counted from one daily read understates rotation. No new content either "
    "way; the returning card is a fortnight old, so this is a rotation under the standing "
    "rotating-module rule and banks nothing. Also closed: meta-nest-ai-creative-diversification "
    "reached its own date, was opened in full, and is the post already banked as CR-286 on "
    "2026-10-17, so the read-once rule for a future-dated card holds. Transport: WebFetch on both "
    "locales, hrefs and dates, first attempt each, thirteenth consecutive browser-free read."
)

ARXIV_NOTE = (
    "Monday build read on the second pass: lastBuildDate Mon 19 Oct 2026 04:00:07 UTC, 18 items, 12 "
    "new against the cache, 0 passing the advertising filter. All 12 titles checked by hand and the "
    "filter is correct: semantic-ID reranking, Portuguese IR judging, quality-diversity recsys, "
    "sparse news recsys, generative engine optimisation, astronomy VQA, LLM benchmarking, OCR, code "
    "search, tool recommendation, CoT supervision, novelty assessment. No auction, no bidding, no "
    "advertising paper in the batch. This closes the deferral the 03:38 pass logged when it read "
    "Sunday's empty build at 22:08 UTC."
)

d = json.load(io.open(CACHE, encoding="utf-8-sig"))

p = d["pages"]["meta-business-news"]
p["last_checked"] = "2026-10-19"
p["result"] = NOTE
p["slugs_us_2026_10_19_pass2"] = US
p["slugs_uk_2026_10_19_pass2"] = UK
cum = set(p.get("slugs_seen_cumulative", [])) | set(US) | set(UK)
p["slugs_seen_cumulative"] = sorted(cum)
p["note_2026_10_19_pass2"] = NOTE

d["feeds"]["arxiv-cs-ir"]["note_2026_10_19_pass2"] = ARXIV_NOTE
d["last_run"] = "2026-10-19T13:55 IST (second pass)"

io.open(CACHE, "w", encoding="utf-8", newline="\n").write(
    json.dumps(d, indent=2, ensure_ascii=False)
)
print("committed; cumulative slugs now", len(cum))
