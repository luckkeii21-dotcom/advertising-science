# -*- coding: utf-8 -*-
import io, shutil

P = (r"E:\claude code marketing skill\Obsidian God-level Marketing Vault"
     r"\God-level Marketing\wiki\science\Harvest Log.md")
shutil.copyfile(P, P + ".bak-20261115-research")
t = io.open(P, encoding="utf-8").read()

ANCHOR = u"## 2026-11-13 (research run)"
assert t.count(ANCHOR) == 1

ENTRY = u"""## 2026-11-15 (research run, Sunday) \u00b7 0 transcripts in \u00b7 7 claims added, 5 amended, 0 contested

**One line: every automated feed was empty or irrelevant and both Meta shelves were flat, and the day still
banked seven claims, because the methodology report this lane has carried as its top gap since 13 November turned
out to be an ungated 20-page PDF.** It supplies the magnitude the four-part calibration series omitted, a median
31% undervaluation of Meta and a 1.45X minimum multiplier off 307 studies, and it does not supply the test-design
parameters the gap predicted it would.

### 1. YouTube harvest

`harvest.py daily`, exit 0, 12:33:57 to 12:35:08 IST. **0 new transcripts.** 12 channels listed, 0 listing
failures, 0 errors. 3 videos skipped for having no subtitles, 0 too short, 0 out of window.

**12 of 12 RSS fallbacks, and that is not an outage in disguise.** YouTube's `feeds/videos.xml` answered HTTP 404
on all twelve channels, so `harvest.py` listed each from the yt-dlp `/videos` tab instead. The code raises only
when the fallback returns nothing, and `errors` came back empty, so all twelve were listed. This is the outage
first recorded 2026-09-05. 13 November logged 12 fallbacks and 12 November logged 0, so the endpoint stays
intermittent.

### 2. Daily watchlist

`lib/watchlist_check.py --commit`. Cache backed up to `cache/watchlist-seen.json.bak-20261115` first.

| Source | Result |
|---|---|
| Meta Engineering (RSS) | HTTP 200, 9 in feed, **1 new**, build Fri 13 Nov 00:19 UTC. Read and discarded, see below |
| Meta Newsroom (RSS) | HTTP 200, 10 in feed, **0 new**, build Thu 12 Nov 14:12 UTC |
| Google Ads & Commerce (RSS) | HTTP 200, 20 in feed, **0 new**, build Thu 12 Nov 13:00 UTC |
| arXiv cs.IR (RSS) | HTTP 200, **0 items**, build Sun 15 Nov 05:00 UTC. API backfill below |
| TikTok Business API SDK changelog | HTTP 200, top version **0.1.8**, unchanged |
| Google Ads Announcements | HTTP 200, **396 answer ids, 0 added, 0 removed** |
| Meta for Business News | Read on both pinned URLs. **Both shelves flat**, see below |
| Monday weekly lane (8 sources) | **Not due.** Sunday |
| TikTok Newsroom / TikTok for Business blog | **Blocked, not skipped.** India geo-block, verified 2026-08-20 |

Cache committed. **File mtime 12:48:11 proves the write**, per the standing rule from 2026-10-24 and 2026-10-28
that a run log claiming a commit is not evidence of one.

**The one new feed item was read in full and deliberately not banked.** `cuttlefish-on-mac`, Meta Engineering,
13 November: Reality Labs porting Android's Cuttlefish virtual device framework to macOS on Apple silicon. Zero
advertising content, no ranking, no delivery, no auction, no measurement. Same handling as the Google Structured
Data Files post on 2026-10-07, and recorded in the cache so a future run does not re-read it.

**arXiv: the empty build is arXiv publishing nothing, for the third time this month.** RSS served an empty cs.IR
build, the documented weekend state from 2026-09-05. Backfilled through `export.arxiv.org/api/query` for
`cat:cs.IR`, `sortBy=submittedDate`, 250 most recent, per the standing instruction from 2026-10-07.
**The newest submission in the whole index is dated 2026-11-12**, so arXiv published no cs.IR submissions on 13,
14 or 15 November. 29 submissions landed on 11 and 12 November and **0 passed the bank-list filter.** Histogram:
12 Nov 16, 11 Nov 13, 10 Nov 14, 9 Nov 15, 8 Nov 8, 7 Nov 16, 6 Nov 13, 5 Nov 20. No window lost. Cached at
`cache/arxiv-api-csir-20261115.xml`.

**Meta for Business News: both shelves flat, and this read covers two days** because no run fired on 14 November.

| Locale | Slugs | Ceiling | Against 2026-11-13 |
|---|---|---|---|
| `?locale=en_US` | 12 | 12 November 2026 | **0 added, 0 removed, order-identical** |
| `en-gb` host | 12 | 27 October 2026 | **0 added, 0 removed, order-identical** |

Cumulative seen set stays at **41**. The UK shelf is now order-identical to nine saved reads, so across 33 saved
UK reads there are still exactly **5 distinct ordered states and no sixth**, and the 2026-11-10 finding that UK
movement is request-level variance rather than publishing holds. The link-extraction method added on 13 November
had nothing to act on, because no new post entered either shelf.

### 3. The day's real finding: the methodology report is ungated, and it was read

The gap logged 13 November named "Building a Suite of Truth: A Hybrid Approach to Measuring Incrementality" at
`facebook.com/business/f/1094917955782254` as the cheapest high-value item on the board, because it was the only
plausible home for the holdout sizes, durations and precision figures missing from all four blog posts.

**It is ungated.** A plain GET on the business URL answers 302 straight to a `scontent` PDF: no form, no login,
no email wall. 6,416,093 bytes, 20 pages. Downloaded to `cache/meta-suite-of-truth-20261115.pdf`, text extracted
to `cache/meta-suite-of-truth-20261115.txt`, read in full. **Seven claims out of one document, the largest single
source in this lane since the Andromeda posts.**

**The headline, and it is the number the series was missing.** "at the median advertisers undervalue Meta by 31%
(meaning 31% of total incremental conversions caused by Meta are misattributed to other channels) when using
rules-based attribution models", and "**a multiplier of at least 1.45X was required to calibrate the results of
the models to the true value driven by Meta**", footnoted to **307 studies run by 54 advertisers between March
2022 and November 2024 across North America, EMEA, APAC and LATAM**.

**Two observations that only come from holding the report against the blog post.** First, the 31% and the 1.45X
are one measurement from two ends, `45 / 145 = 31.0%`, so they are not two findings and never corroborate each
other. Second, the October 2025 blog post teaches the multiplier method with a worked `150 / 100 = 1.5x` on a
company Meta labels fictional, and **1.5x sits within 3% of Meta's own measured median of 1.45X**, with no
indication anywhere on the page that the teaching example rests on a measurement.

**And the gap closes negatively on the half it was actually opened for.** Across all 20 pages: no holdout size,
no minimum detectable effect, no statistical power figure, no confidence interval on any number, no minimum
conversion volume, no geo-test design and no model specification. The only precision-adjacent figure in the
document is one case study's "99.6% winning score", which the report never defines. **So across the four-part
series and this report, Meta publishes exactly one test-design parameter, the duration heuristic already banked
at AT-125, and nothing else.** A practitioner cannot size a Conversion Lift test from Meta's public material.

### 4. Claims

**New, 7, all from the report, all read at source.**

- **AT-139, T1.** The 31% median undervaluation and the 1.45X minimum multiplier, with the 307-study footnote, the
  arithmetic identity between the two figures, and the eight things the footnote still does not give: no spread,
  no distribution, no per-vertical or per-spend-tier breakdown, no count of how many of the 307 found no lift, and
  5.7 studies per advertiser so the median is not over independent businesses.
- **AT-140, T1.** Meta's which-tool-when ladder tied to cadence: single-cell Conversion Lift for cross-publisher
  budgets "typically quarterly", multi-cell for strategy validation, incremental attribution in real time. Closes
  the "periodically" absence at AT-135. Carries the guard that matters most, Meta's own "run multiple tests to
  allow a pattern to emerge, as opposed to taking action on a single study", which cautions against the move its
  own worked example demonstrates. Plus Product Madness's 10 single-cell studies per quarter, and the HBR 2020
  "15 or more experiments annually, 30% higher ad performance" figure with the reasons never to quote it.
- **AT-141, T1 for the sentence, T3 for the effect.** The 46% average performance lift for incremental attribution,
  and **the footnote is the finding**: the 37 studies are restricted to those "where statistically significant
  incrementality was detected in at least one cell", so the denominator excludes every null. Includes an explicit
  warning not to collide it with the unrelated 46% at AT-085, and the Laura Geller three-cell design, 3.3X higher
  incremental ROAS and 71% lower incremental CPA against the business-as-usual cell.
- **AT-142, T1.** Calibration via bid strategy, Meta's third named calibration route and the only one that needs
  no lift test and no MMM: tailor bids to a cohort's expected incremental lifetime value, branded against
  non-branded search, prospecting against retargeting. It is the platform's own description of what AT-040 argues
  from the account side.
- **AT-143, T1.** Conversion Lift now runs off the Conversions API, which Meta names as **recommended** over the
  pixel, and is self-serve in Experiments for "all qualified advertisers" with qualified left undefined. Both
  halves matter for us: our accounts already send server-side CRM events, and a self-serve lift test would be a
  look rather than a spend.
- **AT-144, T1.** The negative, recorded so nobody re-reads the document: what is absent from all 20 pages, scoped
  correctly against AT-125's real duration figure, and the operational consequence that any client lift-test
  proposal has to be sized from our own event volume.
- **AT-145, T1.** A method claim. Meta's MMM blog post prints the same Kantar 51% as "marketers using MMM
  alongside other tools"; the report prints it as advertisers who "default to the solution that holds the most
  credibility within their organisation" when results conflict. Same survey, same number, two different
  propositions, and only the report carries the footnote. **The rule: find the primary document before carrying a
  figure a Meta blog post recites.**

**Amended, 5.**

- **AT-138.** The gap it opened is closed on both halves. Plus a correction it would be wrong to bury: this claim
  records the Gen Z footnote as 91 retail advertisers in North America, read off the blog on 13 November, and
  **the report footnotes the identical sentence to GlobalWebIndex, 2024, n=955,000 global excluding China**. Two
  Meta documents, one sentence, two unrelated sources. The 13 November conclusion that the retail footnote was the
  correct one should now be read as unsettled. The operating rule is unchanged: never quote the Gen Z figure.
- **AT-131.** The contrast case. All four case studies in the report **are** footnoted, which is the opposite of
  the no-footnote state AT-131 records, and three of the four footnotes point at another Meta page rather than at
  a method. So the rule sharpens: check whether the footnote points at a method or only at Meta. Also records that
  "3X improvement in reporting accuracy" is an uninterpretable unit, and keeps H&M's one structural detail, a
  weekly agile digital MMM that replaced the legacy last-click model.
- **AT-132.** Custom attribution finally has a mechanism: the advertiser shares **click-level** attribution data
  and the values it assigns per touchpoint, and Meta optimises to the advertiser's own analytics model, Meta's
  example being first-click credit. Status is "can now test a new feature", so not general availability, and the
  click-level prerequisite puts it out of reach on every account we run.
- **AT-022.** Meta now prints our ordering as a drawn, named "ladder of incrementality" with three rungs and a
  job per rung. **Tier deliberately stays T3**, because this is the third interested platform statement. What it
  adds is Meta's concession list, and the observation that **Meta leaves geo testing off the ladder entirely**, so
  the rung we put above Conversion Lift is one Meta does not rank.
- **AT-002.** Meta's own comparable figure is larger than Haus's up-to-38% and comes off a sample conditioned on
  the outcome. Haus's figure stays the one to quote.

**Discarded.** H&M's "incremental ROAS tripled in key markets" and "attributed ROAS grew 21% year over year", no
market, no spend, no baseline. Huel's 6X marginal return, 11.8M more incremental people and 10% brand favorability,
no window and no starting point. Product Madness's 3X and 5X "improvement in reporting accuracy", a unit that does
not exist. All four are footnoted to Meta's own case-study pages, which is why they are noted at AT-131 rather
than banked as effects. Colour discarded: store counts, founding dates, brand mission copy.

### 5. Skill law layer

**Law 11g amended, no new law added.** The 13 November paragraph already carried Meta's calibration doctrine; what
it lacked was the magnitude, so the amendment goes inside it rather than into a new sub-letter, which also avoids
worsening the duplicate-numbering gap logged on 13 November. The addition carries the 31% and 1.45X with the
307-study footnote, the arithmetic identity, the 1.5x-versus-1.45X observation, the cadence ladder, the 46% with
its selection condition and the collision warning against AT-085, and the standing absence of test-design
parameters. `SKILL.md.bak-20261115` written first.

### 6. Gaps

- **Nobody has opened the Experiments tab on any of our accounts.** AT-143 says Conversion Lift is self-serve for
  "qualified advertisers" and defines nothing. This is the cheapest open item on the board now: it is a look, not
  a test, and it answers whether a lift study is reachable for us at all.
- **The Gen Z footnote conflict is unresolved.** Two Meta documents cite different sources for one sentence. It
  costs one re-read of the May 2025 blog post to see whether both footnotes sit on the same page or whether the
  blog's footnote was attached to a different sentence. Not done today.
- **The link-extraction method change is still only a cache note.** `lib/watchlist_check.py` does not touch
  Meta for Business News at all, so the method added 13 November depends on whoever runs the pass. Second day open,
  and today it had nothing to act on so it cost nothing.
- **The size of the Meta back catalogue is still unmeasured.** Both shelves render "Show More" as `href="#"`, so a
  bound needs a browser. Unchanged from 13 November.
- **`SKILL.md` has duplicate law numbering**, two paragraphs numbered 11a and out-of-order sub-letters. Deliberately
  not fixed in a research pass for the second time. Worth half an hour on a maintenance day.
- **Per-channel rejection count, eleventh day open.** Asked for 5 November. Today the subtitle filter rejected 3
  videos and nobody knows which channels they came from.

### Errors

- **0 harvest errors, 0 watchlist fetch errors.**
- **YouTube `feeds/videos.xml` answered HTTP 404 on all 12 channels.** Handled by the documented yt-dlp `/videos`
  fallback, all 12 listed, no transcripts lost.
- **3 roster videos had no subtitles** and were skipped. The channels they belong to were not recorded, which is
  the standing gap above.
- **No run of any kind fired on 14 November**, so both the watchlist and the business-news read cover two days.
- **The Meta business-news plain fetch was not attempted today**; both shelves were read through WebFetch directly,
  which worked on the first attempt on both pinned URLs.

"""

t = t.replace(ANCHOR, ENTRY + ANCHOR, 1)
io.open(P, "w", encoding="utf-8").write(t)
print("harvest log entry written; new length", len(t))
print("em dashes:", t.count(u"\u2014"))
