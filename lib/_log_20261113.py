# Harvest Log entry for the 2026-11-13 research run.
import io

H = (r"E:\claude code marketing skill\Obsidian God-level Marketing Vault"
     r"\God-level Marketing\wiki\science\Harvest Log.md")

ENTRY = """## 2026-11-13 (research run)

**0 transcripts in, 4 new claims, 4 claims amended, 0 contested, 5 posts read in full, one law added. The whole
day came off ONE link.** The roster was silent and the automated feeds were empty. The Meta for Business shelf
moved for the first time in fourteen reads, and the new post pointed at three older posts that this lane had never
seen, because the shelf is a 12-slot window and cannot surface a back catalogue.

**YouTube harvest.** `harvest.py daily`, exit 0, 07:01:36 to 07:02:10 IST. 12 channels listed, **0 errors**, 0
rejected as too short, 0 without subtitles, 0 out of window, **0 new transcripts**. Every id returned was already
in `state.json`. **12 of 12 channels fell back from RSS to the yt-dlp `/videos` tab**, YouTube's
`feeds/videos.xml` answering HTTP 404 on eleven channels and HTTP 500 on one. That is the outage first recorded
2026-09-05 and it is handled in code: the fallback listed every channel successfully, so a quiet day here is a
real quiet day and not a hidden outage. Worth stating because yesterday logged 0 RSS fallbacks, so the endpoint
is intermittent rather than dead. Extraction backlog **0**, verified by scanning all 507 transcript files for
`extracted: false`.

**Daily watchlist.** Meta Engineering RSS, HTTP 200, 9 in feed, **0 new**, build still Tue 10 Nov 23:55 UTC. Meta
Newsroom, HTTP 200, 10 in feed, **0 new**. Google Ads & Commerce, HTTP 200, 20 in feed, **0 new**. TikTok
Business API SDK changelog, HTTP 200, top version 0.1.8, unchanged. Google Ads Announcements, HTTP 200, **396
answer ids, 0 added, 0 removed**. Friday, so the 8 Monday-only weekly sources were not due. TikTok Newsroom and
the TikTok for Business blog stay logged as blocked rather than skipped: India geo-block, verified 2026-08-20,
deliberately not retried. Cache backed up to `watchlist-seen.json.bak-20261113` and committed; **file mtime
07:14:13 proves the write**, per the standing rule that a run log claiming a commit is not evidence of one.

**arXiv: yesterday's open question is answered, and it was arXiv's own gap rather than our fetch.** The RSS lane
served the identical empty build again, `lastBuildDate` Thu 12 Nov 05:00 UTC, content-identical to the copy
cached yesterday. The run fired at 01:32 UTC, before arXiv's 13 Nov rebuild, so that re-read is the documented
lag and on its own proves nothing. The standing instruction from 2026-10-07 settles it: backfilled through
`export.arxiv.org/api/query` for `cat:cs.IR`, 200 most recent submissions, and **the newest submission in the
whole index is dated 2026-11-10**. So there were no cs.IR submissions on 11 or 12 November, the empty build is
arXiv publishing nothing, and the feed is not broken. Date histogram: 10 Nov 14, 9 Nov 15, 8 Nov 8, 7 Nov 16, 6
Nov 13, 5 Nov 20, 4 Nov 16, 3 Nov 26. **0 of the 14 papers since 10 November passed the bank-list filter.** Raw
XML cached at `cache/arxiv-csir-20261113.xml` and the API response at `cache/arxiv-api-csir-20261113.xml`.

**Meta for Business News: the US shelf MOVED after fourteen flat reads, and it covers two days.** No 2026-11-12
read exists. Plain fetch returned HTTP 400 on both pinned URLs, the ordinary state, so both shelves were read
through WebFetch. US: 12 slugs, **2 in at slots 1 and 2, 2 out from the bottom**, and the ceiling moves 28
October to **12 November 2026**. In: `from-measurement-to-capital-allocation` (12 Nov) and
`finding-his-squad-again-in-a-facebook-group` (11 Nov). Out: `agency-awards-2026` and
`introducing-meta-one-plans-for-businesses`, both already in the cumulative set, the ordinary 12-slot rotation.
UK: 12 slugs, **0 new**, order-identical to eight saved reads, so still exactly 5 distinct UK states and no sixth.
Cumulative seen set 36 to **41**.

**⚠ METHOD FINDING, and it is the most valuable thing this run produced. The 12-slot shelf is structurally blind
to the back catalogue, and link-following is the only route in.** The new 12 November post links two companion
posts; the second links a third. All three were read in full today and **all three were absent from the 36-slug
cumulative set built over seven weeks of daily reads of BOTH locales.** Their own page dates are 22 October (no
year printed, placed 2025 by the sequel's back-reference), 29 October 2025 and 28 May 2025. **A four-part Meta
methods series spanning eighteen months was invisible to this lane by construction.** The sharpest instance: the
shelf carried a 22 October post at slot 5 while a different 22 October post sat unseen. The cumulative-slug
method can only ever detect a post that enters one of the twelve visible slots, and the shelf is a curated slice,
not a feed. **Method change, now in the cache note: every post read on this source gets its outbound
`/business/news/` links extracted and diffed against the cumulative set, and any miss is read before the run
closes.** Both shelves render their "Show More" control as `href="#"`, so pagination still needs a browser and was
not attempted today.

### New claims, 4

- **AT-135, T1.** Meta's own attribution-calibration recipe, and it is a single scalar multiplier: run a
  Conversion Lift test, divide lift conversions by attributed conversions, apply the result to that channel "going
  forward". Meta's worked example is `150 / 100 = 1.5x` on a company it labels fictional. **The step that
  matters is the overshoot rule:** if the multiplied total exceeds real total conversions, test the other
  platforms, and "Any remaining conversions can be attributed to organic." Organic never gets an experiment, so
  it absorbs every error in every paid multiplier plus every untested channel. Zero confidence intervals, no
  holdout size, no duration, no minimum detectable effect, and the only cadence guidance is "periodically".
- **AT-136, T1.** Meta's three-tier MMM calibration taxonomy. Tier one is "qualitative model selection", a check
  that both methods point the same direction, which Meta itself calls "not very precise". Tier two injects the
  experiment's "mean and spread" into the model parameters as a prior. Tier three, "comprehensive parameter
  calibration", is **the only tier that touches ad stock and media saturation**, the two parameters that decide
  what an MMM says about scaling. The durable question falls straight out: when anyone says a model is
  calibrated, ask which tier.
- **AT-137, T1.** The 12 November capstone. Meta reframes incrementality as a finance control, prescribes a
  methodology review with finance **before a budget request exists**, and recommends branded search as the first
  test "because it may capture demand that already exists". Two sentences worth borrowing for our own reporting:
  "Different measurement methods may still produce different answers", and "a credible range will be more useful
  than a single precise number". **Tier the evidence honestly: the entire basis is two unnamed, undated
  closed-door roundtables plus one internal Meta executive, with zero numbers of any kind in the post.** T1 on
  what Meta recommends, no evidential weight at all on effect sizes.
- **AT-138, T1.** The May 2025 root post, which defines the "suite of truth" the other three lean on and
  **ranks the tools explicitly**: randomized control experiments "provide the most accurate measure of
  incrementality", and the job it gives MTA and MMM is to be calibrated by those experiments. Also the scope
  limit worth keeping: experiments are "particularly effective for single channel evaluations and in-channel
  optimization", which concedes cross-channel allocation to the model.

### Amended, 4

- **AT-023, the contested static discount factor, and this is the significant one.** Position B now has a **T1
  endorser**: Meta publishes exactly the fixed per-channel multiplier that one practitioner had been arguing for
  against Haus. **Status stays contested**, because Haus's objection is that a factor decays and Meta's own hedge
  concedes the same problem without quantifying it. The T1 lands on the method and says nothing about the
  frequency, which is the half the disagreement is actually about. Meta also has no equivalent of Haus's pooling,
  and its residual step is the opposite of conservative.
- **AT-022, the measurement hierarchy.** Both major platforms now publish our ordering themselves and agree with
  it: Meta at AT-138, Google at AT-115, and Meta's Chief Data Officer states the sequencing flatly at AT-136, run
  the experiment first then the model. **Tier deliberately stays T3.** Two interested platforms agreeing is
  agreement, not evidence, and both sell the experiment at the top of it. What changed is that the hierarchy is
  no longer ours alone to defend to a client.
- **AT-125, Conversion Lift design.** The wording sharpens to intention-to-treat: Meta compares "people who were
  eligible to see ads" against "a randomized holdout group". **Eligibility defines the treated arm, not
  exposure**, so the measured lift is diluted by everyone eligible who never saw an ad and is a floor on the
  effect among the exposed rather than an estimate of it.
- **MD-169, Muse for Small Business.** The third published customer story and the **first to exercise the ads
  path** the claim opened on 2026-09-29. What it exercises is the read side only: a daily 08:00 brief covering
  revenue, spend, return on ad spend and **new-customer cost across 7, 30 and 90 days**. So across three customer
  stories, the number exercising the "draft a campaign" write path Meta advertised at launch is **zero**. Sits
  pointedly against AT-121: Meta's agent emails the owner a new-customer cost line every morning while our CRM
  cannot compute one on any account.

### Read and NOT banked

- **A correction to our own first reading, made before anything was written.** The attribution post's Gen Z
  figure looked at first pass like a second instance of the footnote misattribution recorded at AT-120. Reading
  the May 2025 root post settled it: the 91-advertiser retail study **is** the right footnote for a
  click-versus-view claim. **No misattribution, so nothing was banked against AT-120.** The figure is thin rather
  than mis-sourced, and its scope limits are written into AT-138 instead: 91 advertisers, retail only, North
  America only, a 94-day window spanning the holiday peak, Meta measuring its own platform, and no base rate for
  either group, so "twice as likely" has no denominator.
- **Three figures from the calibration series, all unusable.** "ROI increases of 20% or more", footnoted to a Bain
  and Company title and a date with no sample, baseline, denominator, window or link. "Measured ROI varied by 29%"
  (Analytic Edge, December 2023), unlinked and with **no stated direction**, no baseline and no n. And two Kantar
  figures, 51% and 55%, carrying **no footnote at all** on a Meta-commissioned survey.
- **The human-interest half of the Muse story.** 87,000 customer reviews, nearly 400 ambassador videos, five
  terabytes of unsearchable files, forty community members at a football game. Colour, not mechanism.

### Skill law layer

**One added, 11g.** Meta's published calibration doctrine is law-level because it is the first time the platform
has told us how to correct our own reporting, and because it lands on a contested claim. The paragraph carries the
multiplier, the residual-to-organic step, the three consequences for AT-023, AT-022 and AT-136, and the heavy
guards. `SKILL.md.bak-20261113` written first.

### Gaps noticed

- **The series' actual methodology was NOT read.** It sits in a report, "Building a Suite of Truth: A Hybrid
  Approach to Measuring Incrementality", at `facebook.com/business/f/1094917955782254`. Everything banked today
  comes from the four blog posts. That report is the cheapest high-value item on the board tomorrow, because it is
  the only place the holdout sizes, durations and precision figures absent from all four posts could plausibly
  live.
- **The link-extraction method change is written into the cache note and is not yet in code.** Until it is, it
  depends on whoever runs the pass remembering to do it. `lib/watchlist_check.py` does not touch this source at
  all, so the natural home is the business-news step.
- **How many more posts sit behind "Show More" is unknown and unmeasured.** Both shelves render the control as
  `href="#"`, so the back catalogue's size is not even bounded. Seven weeks of reads established a 36-slug
  cumulative set and today proved that set incomplete by at least three. Nobody knows by how much.
- **`SKILL.md` has two paragraphs numbered 11a and the law-11 sub-letters are out of order.** Pre-existing, found
  while placing today's paragraph, and deliberately not fixed in a research pass. It makes a law citation
  ambiguous, which is worth half an hour on a maintenance day.
- **Per-channel rejection count, ninth day open.** Asked for on 5 November. Today the filters rejected nothing, so
  the gap cost nothing, and a zero-rejection day is also the day the counter would have been cheapest to add.

"""

t = io.open(H, encoding="utf-8").read()
assert "## 2026-11-13 (research run)" not in t, "entry already present"
anchor = "## 2026-11-12 (research run)"
assert t.count(anchor) == 1, "anchor not unique"
t = t.replace(anchor, ENTRY + anchor, 1)
io.open(H, "w", encoding="utf-8").write(t)
print("Harvest Log entry written for 2026-11-13")
