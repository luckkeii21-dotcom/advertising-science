# -*- coding: utf-8 -*-
import shutil
from pathlib import Path
H = Path(r"E:\claude code marketing skill\Obsidian God-level Marketing Vault\God-level Marketing\wiki\science\Harvest Log.md")
shutil.copy2(H, H.with_name(H.name + ".bak-20261111-research"))
entry = """## 2026-11-11 (research run)

**1 transcript in, 1 new claim, 1 claim amended, 1 source added, 0 contested, 0 new watchlist items, no law change.**

**YouTube harvest.** `harvest.py daily`, exit 0, 17:25:01 to 17:25:49 IST. 12 channels listed, 0 errors, 0 RSS
fallbacks, 4 rejected as too short, 1 for having no subtitles. **1 new transcript**, Jon Loomer, "How I'm Using AI to
Create Meta Ads", 9 minutes, 1,494 words, published today. Extraction backlog **0**, verified across all 505
transcript files.

**Claims merged, all in the AI-creative lane.**
- **CR-291 new, T3.** The control architecture Loomer credits for his AI-produced ads: a written rule book updated on
  every correction, named adversarial review roles including one whose only job is catching AI-looking visuals and
  which runs twice, voice fitted from his own published corpus rather than a described tone, a maintained AI-tell
  block list, and three human approval gates after two automated rounds. The mechanism sentence under all of it is the
  keeper: without operator-specific input the output is "generic and based on the average of advertising advice found
  on the internet."
- **CR-169 amended.** He states a performance improvement outright, "I'm actually getting better results than I was
  with the ads I created myself", and supplies **no number at all**. No cost per result, no spend, no window, no
  sample, no control arm. The only quantity in 1,494 words is cycle time, "a couple of hours start to finish", which
  is a production-cost figure. So the first outright "better results" sentence from a high-credibility Meta operator
  has the same evidence shape as every other AI-creative claim on file, and CR-169's rule stands untouched: we never
  write that AI creative performs better.
- **MD-124 source added.** He restates the 10-asset capacity from the operator side and notes that aspect-ratio
  variants of one concept push the asset count past 10 inside a single ad object.
- Discarded: the campaign-simplification restatement, already law, and the tooling specifics.

**Watchlist.** Six automated sources, all HTTP 200, all 0 new. Meta Engineering 9 in feed, Meta Newsroom 10, Google
Ads & Commerce 20, all three built Mon 09 Nov. **arXiv cs.IR served the 11 November 05:00 UTC build, 29 items, 0 past
the ad filter**, which closes the two-day read-the-stale-build lag the 9 and 10 November runs both logged. TikTok
Business API SDK changelog top version 0.1.8, unchanged. Google Ads Announcements 396 answer ids, 0 added, 0 removed.
Monday weekly lane not due. Demand Gen Drops Hub not read, its trigger is a stale Ads & Commerce feed and the feed is
two days old. TikTok Newsroom and the for-Business blog stay blocked, India geo-block, not retried.

**Meta for Business News.** Plain fetch HTTP 400 on both pinned URLs, the ordinary intermittent state, read through
WebFetch. **US 12 slugs, identical in set and in order to every US read since 29 October, 13 consecutive reads, one
state, ceiling 28 October 2026. UK 12 slugs, exactly the ordered state of 30 October and 9 November, ceiling 22
October 2026.** 0 of today's 24 slugs is absent from the 36-slug cumulative set, so 0 new and nothing to read.

**The one source finding: 31 saved UK reads, still exactly 5 distinct ordered states, no sixth in 46 days.** Today was
a third sighting of state 4, served 2 days after its last appearance and 12 days after its first. A closed set of
variants recurring out of date order is what request-level variance looks like, and a genuine publishing event would
introduce a state nobody has seen. Written into `Watchlist.md`: the only valid test for a UK move is a slug absent
from `slugs_seen_cumulative`, never an added-or-removed diff against yesterday.

**Gap carried, 7th day.** The per-channel count of what the length and subtitle filters reject, asked for on
5 November, is still not built. Today 4 uploads were rejected as too short and 1 for no subtitles, and there is still
no record of which channels they came from, so a channel that has switched to clips cannot be told from one that has
gone quiet.

**Errors: none.** 0 harvest errors, 0 watchlist fetch errors. The two HTTP 400s fell through to the documented
WebFetch route.

"""
t = H.read_text(encoding="utf-8")
m = "## 2026-11-10 (research run)"
assert t.count(m) == 1
i = t.index(m)
H.write_text(t[:i] + entry + t[i:], encoding="utf-8")
print("Harvest Log entry prepended")
