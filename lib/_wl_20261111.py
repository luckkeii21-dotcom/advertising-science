# -*- coding: utf-8 -*-
"""2026-11-11: save today's Business News shelves, append the Watchlist note."""
import json, shutil
from pathlib import Path

CACHE = Path(r"E:\claude code marketing skill\.claude\skills\advertising-science\cache")
SEEN = CACHE / "watchlist-seen.json"
WL = Path(r"E:\claude code marketing skill\Obsidian God-level Marketing Vault\God-level Marketing\wiki\science\Watchlist.md")

us = ["how-metas-ads-system-matches-your-ad-to-the-right-person","three-new-ai-innovations-in-ads-ranking","you-dont-beat-the-auction-you-brief-it","muse-smb-jaeluxe-shoetique","agencies-testing-incrementality","meta-nest-ai-creative-diversification","meta-brand-building-summit-2026","muse-smb-bennett-orchards","a-new-way-for-businesses-and-personal-agents-to-work-together","advertising-week-new-york-2026","agency-awards-2026","introducing-meta-one-plans-for-businesses"]
uk = ["you-dont-beat-the-auction-you-brief-it","creator-marketing-whitepaper","performance-spotlight-how-instant-hydration-built-a-system-for-ai-to-scale","businesses-driving-results-with-meta-ai-ads","closing-the-creator-measurement-gap","2026-winning-hearts-boosting-carts","conversations-2026-introducing-meta-business-agent","social-search-series-2","social-search-series-3","social-search-series-1","2026-trends-from-around-the-world","meta-growth-drivers-putting-your-digital-marketing-strategy-on-auto-pilot"]

shutil.copy2(SEEN, SEEN.with_name(SEEN.name + ".bak-20261111"))
d = json.loads(SEEN.read_text(encoding="utf-8"))
bn = d["pages"]["meta-business-news"]
bn["slugs_us_2026_11_11"] = us
bn["slugs_uk_2026_11_11"] = uk
bn["last_checked"] = "2026-11-11"
bn["result"] = ("2026-11-11: plain fetch HTTP 400 on both pinned URLs, read through WebFetch. "
                "US 12 slugs, identical in set and order to every US read since 2026-10-29, ceiling 28 October 2026. "
                "UK 12 slugs, exactly the ordered state of 2026-10-30 and 2026-11-09, ceiling 22 October 2026. "
                "0 of 24 slugs absent from slugs_seen_cumulative, so 0 new and nothing to read.")
bn["note_2026_11_11"] = ("Third read of UK state 4. Across 31 saved UK reads there are still exactly 5 distinct "
                         "ordered states and no sixth. Variant variance, not publishing.")
assert set(us) <= set(bn["slugs_seen_cumulative"]) and set(uk) <= set(bn["slugs_seen_cumulative"])
SEEN.write_text(json.dumps(d, indent=1, ensure_ascii=False), encoding="utf-8")

shutil.copy2(WL, WL.with_name(WL.name + ".bak-20261111"))
note = """
### The UK shelf serves 5 recurring states and today was a third sighting of one of them (2026-11-11)

The 2026-11-10 pass-2 note established that the UK shelf varies by request rather than by publishing date, on the
evidence that two reads 3 hours 47 minutes apart served different ordered lists. Today's single read landed on the
**2026-10-30 / 2026-11-09 state exactly, in order**, 2 days after it was last served and 12 days after the first
sighting.

**The count that matters: 31 saved UK reads, still exactly 5 distinct ordered states, no sixth state in 46 days.** A
small closed set of variants recurring out of date order is what request-level variance looks like. A publishing event
would introduce a state nobody has seen. **So the test for a real UK move is a slug absent from
`slugs_seen_cumulative`, which has held at 36 members since 9 October, and never an added-or-removed list against
yesterday.**

What today does NOT settle is how many variants exist, because one read per day samples one variant. The two-read rule
from yesterday stays; a single read is one sample of a set whose size is unknown.
"""
w = WL.read_text(encoding="utf-8")
marker = "### A UK shelf move can REVERSE, so a move is not a publishing event (2026-11-10)"
assert w.count(marker) == 1
i = w.index(marker)
j = w.index("\n### ", i + 10)
WL.write_text(w[:j] + "\n" + note.strip("\n") + "\n" + w[j:], encoding="utf-8")
print("cache saved, Watchlist note inserted")
