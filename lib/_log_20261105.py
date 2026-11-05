# Harvest Log entry for the 2026-11-05 research run.
import io

P = (r"E:\claude code marketing skill\Obsidian God-level Marketing Vault"
     r"\God-level Marketing\wiki\science\Harvest Log.md")

ENTRY = """
## 2026-11-05 (Thursday) \u00b7 0 transcripts in \u00b7 1 claim added, 1 amended, 0 contested

**One real finding, from arXiv, and it is Meta's own paper.** 0 transcripts in, **1 claim added, MD-198**, 1 amended (MD-197), 0 contested, 1 defect found in our own tooling. The law layer moved.

**The finding in one line.** Meta published that its ads ranking and retrieval fleet is hundreds of separately tuned models, that each one's serving budget is being raised 1.2x to 10x, and that a whole generation of model work across 34 production models is worth 0.66% offline and summed online lifts of 0.07% and 0.29%, which is the first-party number that disqualifies "Meta changed their model" as an explanation for a client's drop.

### 1. YouTube harvest

`lib/harvest.py daily`, started 19:27:33, finished 19:29:42 IST. `errors: []`.

- All 12 roster channels listed, every one returning 0. **0 new transcripts.** 5 uploads skipped as too short, 2 had no subtitles, 0 fell out of the window. No RSS fallback needed.
- 11-03 and 11-04 each brought one transcript, so this is the first dry roster day since 2026-11-02.

### 2. Watchlist

Thursday, so the daily lane only. `lib/watchlist_check.py`, all six automated sources HTTP 200, `errors: []`, committed.

| Source | Result |
|---|---|
| Meta Engineering (RSS) | 0 new links, 9 in feed, feed built 2026-11-03. The F3 Lightning post banked yesterday at MD-197 is still the newest |
| Meta Newsroom (RSS) | 0 new links, 10 in feed, feed built 2026-10-29 |
| Google Ads & Commerce (RSS) | 0 new links, 20 in feed, feed built 2026-10-28 |
| arXiv cs.IR (RSS) | 31 in feed, 28 new links, **2 passed the ad filter, 1 genuine.** See below |
| TikTok Business API SDK changelog | HTTP 200, top version 0.1.8, unchanged against baseline |
| Google Ads Announcements | 396 answer ids, 0 added, 0 removed |
| Meta for Business News | **0 new slugs on either shelf, second static day.** See below |

**Meta for Business News: plain fetch 400s again, one day after answering 200.** Both pinned URLs returned HTTP 400 to the plain-fetch script, which is the ordinary state of this source and makes yesterday's pair of 200s the anomaly rather than a recovery. Read instead through WebFetch on `?locale=en_US` and `?locale=en_GB`, the fallback established 2026-09-30 and 2026-10-01. US shelf 12 slugs, ceiling 28 October, **0 new against the 36-slug cumulative set**. UK shelf 12 slugs, ceiling 27 October, **0 new**. Both shelves carry the same slug sets as 2026-11-04, so the three Hong Kong posts that arrived yesterday have not rotated off and nothing has arrived behind them.

**Defect in our own tooling, found today, and it is the kind that reports a false haul rather than a false quiet.** `lib/_bizmeta_20261104b.py` reads `slugs_seen_cumulative` from the TOP LEVEL of `watchlist-seen.json`. The key does not live there. It lives at `pages/meta-business-news/slugs_seen_cumulative`. The script prints "cumulative seen: 0" and, had the fetch succeeded, would have declared **every slug on both shelves new**. It escaped notice because the fetch 400s before the diff runs, and because on the one day the fetch did work a human read the result. Recorded in the cache under `defect_2026_11_05`. Fix the key path before that script's new-slug count is trusted again.

**arXiv, and the filter did its job in both directions.** Build dated 2026-11-05, read today, so no scheduling lag to correct for. 2 of 31 passed the keyword filter.

| Paper | Verdict | Reason |
|---|---|---|
| 2611.06777 *WISE: An Agentic Framework for Whole-page Multimodal Search Experience Attribution* | **False positive** | "advertising" appears once, in the opening list "search, recommendation, and advertising". The method is quality diagnosis for industrial search, benchmarked on search pages. No auction, no bidding, no ads ranking |
| 2611.05643 *Data-Efficient Scaling-Law Discovery for Recommendation Systems via Coupled Hyperparameter Scaling* | **Genuine, and the day's whole haul** | Affiliation printed as Meta, deployed on "Meta's ads ranking and retrieval fleet", 34 production model iterations. PDF pulled and read in full |

The WISE false positive is the same mechanism recorded 2026-09-25: advertising named in a context list, never in the method. No filter change proposed, because the filter is meant to surface it and a human is meant to reject it, and the cost of reading one abstract is lower than the cost of a missed Meta paper.

### 3. Claims

**MD-198 added (T1).** Meta, arXiv 2611.05643v1, submitted 3 November 2026, 12 pages, read in full from the PDF. Thirteen authors, affiliation line reads Meta, and the system is stated as deployed on "Meta's ads ranking and retrieval fleet". A method paper on choosing model architectures; banked for four facts about the fleet it ran on and nothing about the method.

1. **The fleet is hundreds of models, tuned individually.** Quoted: "hundreds of unique models that often share a common template" but differ "in signals, objectives, and serving capacity \u2014 and therefore in optimal configuration", with the operating point chosen "per model rather than once for the fleet" because each serves a surface with its own latency ceiling. This is the architectural reason a creative behaves differently by placement with nothing changed in the ad set, and it is a better first explanation than audience quality. Meta names no model and no surface.
2. **Serving compute per model is rising 1.2x to 10x.** Quoted: "infrastructure investments provide each model with a serving budget between 1.2x and 10x that of its production predecessor". Meta frames its own problem as distributing finite serving compute across the fleet rather than building bigger models, and says that allocation was previously "made by hand, one model at a time, at a cost of days to weeks of training per decision".
3. **What a model generation is worth, which is the number worth carrying.** 34 production model iterations, two development cycles: mean offline normalized-entropy improvement 0.66% (cycle 1, 11 models, 0.66%; cycle 2, 23 models, 0.67%; SD 0.59 percentage points), online lifts 0.07% across the 11 and 0.29% across the 23. Meta attaches "business impact on the order of hundreds of millions of dollars in annual revenue".
4. **Meta wrote its own guard, so quote it.** The table footnote on the headline 0.36%: "The online value is the sum of the shipped cycle-level lifts over disjoint model sets, not a separately measured aggregate effect." It is an addition of two numbers from two different model sets. Never present it as a measured total; the honest form is 0.07% and 0.29%, each on its own set.

**Why it is banked, in one sentence.** Put these magnitudes beside [[Meta Delivery & Andromeda#MD-188|MD-188]], where Meta's Andromeda figures are 2.4% conversions since 2025 and 1.37% on Facebook in Q3 2026: both lanes agree that a generation of Meta's model work moves a platform aggregate by a fraction of a percent to low single digits, which is far less than a single account's week moves from creative, budget, seasonality and sample size. So **"Meta changed their model" is now disqualified as an explanation for an account's drop by a first-party number instead of by our judgment**, and the breakdowns-first ladder in `Attribution & Incrementality.md` keeps its prior that the cause is local.

**Limits recorded inside the claim.** Preprint, under review, not peer reviewed. Normalized entropy is an internal model-quality metric with no advertiser-facing equivalent, so 0.66% translates into nothing a client would ever see in a report. The 34 iterations are undated, no surface or model is identified, and "two development cycles" is not a calendar, so **this discloses no retrain or refresh cadence and [[Meta Delivery & Andromeda#MD-033|MD-033]] stands unchanged.** Nothing in it is a lever: no setting, no report, no opt-in.

**MD-197 amended.** A pointer added to MD-198, because the two are the same story from opposite ends and were published within a day of each other: F3 Lightning says feature iteration got about 3.6x faster, and this paper says what an iteration is worth. `Last touched` moved to 2026-11-05.

### 4. Skill law layer

**Updated.** One paragraph added to the Current laws hot layer for the 2026-11-05 pass, carrying the fleet shape, the 1.2x to 10x serving-budget range, the 0.66% and the two online lifts with Meta's own footnote attached, and the disqualification of the platform-side explanation. It sits under law 1 beside the 2026-11-04 MD-197 paragraph.

### 5. Gaps noticed

- **Which Meta model serves which placement is unknown and probably unknowable from outside.** MD-198 establishes that they are separate models with separate budgets, which makes a placement-level performance gap an architecture fact rather than an audience fact. Nothing in the paper, and nothing in this codex, names a model or maps one to a placement. Our own placement breakdowns are the only instrument we have on this, which is an argument for reading them more often, not for explaining them.
- **Normalized entropy has no bridge to anything we report.** Meta publishes model quality in NE, we publish cost per opt-in and bookings. There is no stated conversion between them anywhere in this codex, so every NE figure Meta publishes is directional only. Worth watching for a Meta source that connects the two; until then every NE number gets the same guard.
- **The roster's dry days are not random and nobody has looked at the pattern.** Five uploads were skipped as too short today and two had no subtitles. A standing count of what the length and subtitle filters reject, per channel, would tell us whether a channel has changed format rather than gone quiet. Not built.
"""

t = io.open(P, encoding="utf-8", newline="").read()
t = t.rstrip("\r\n") + "\r\n" + ENTRY.replace("\n", "\r\n")
io.open(P, "w", encoding="utf-8", newline="").write(t)
print("harvest log appended")
