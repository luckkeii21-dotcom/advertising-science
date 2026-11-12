import io
import os

SCI = os.path.join(
    "E:\\claude code marketing skill",
    "Obsidian God-level Marketing Vault", "God-level Marketing", "wiki", "science")
P = os.path.join(SCI, "Harvest Log.md")

ENTRY = """## 2026-11-12 (research run)

**2 transcripts in, 4 new claims, 6 claims amended, 0 contested, 2 new watchlist items, one law added.** The two
platform items are both T1 and both came from the daily feeds. The two transcripts were the opposite: a combined 95
minutes from the two most-harvested channels on the roster produced almost nothing new, because nearly everything in
them is already banked.

**YouTube harvest.** `harvest.py daily`, exit 0, 19:10:33 to 19:13:06 IST. 12 channels listed, **0 errors, 0 RSS
fallbacks**, 5 rejected as too short, 2 for having no subtitles, 0 out of window. **2 new transcripts**, both
published 11 November: Professor Charley T, "Copy this 3-Part Meta Ads Strategy, It'll Blow Up your Business", 58
minutes, 9,606 words; Ben Heath, "The REAL Secret to Winning with Meta Ads", 23 minutes, 4,944 words. Both read in
full before extraction. Extraction backlog **0**, verified by scanning every transcript file for `extracted: false`.

**Daily watchlist.** Meta Engineering RSS, HTTP 200, 9 in feed, **1 new**. Meta Newsroom, HTTP 200, 10 in feed, 1 new
and irrelevant (a data-centre manufacturing agreement). Google Ads & Commerce, HTTP 200, 20 in feed, **1 new**. TikTok
Business API SDK changelog, HTTP 200, top version 0.1.8, unchanged. Google Ads Announcements, HTTP 200, **396 answer
ids, 0 added, 0 removed**. Monday weekly lane not due, Thursday. Meta for Business News not read this pass, see the
gap below. TikTok Newsroom and the TikTok for Business blog stay logged as blocked, not skipped: India geo-block,
verified 2026-08-20, deliberately not retried.

**⚠ arXiv cs.IR served an EMPTY build.** HTTP 200, `lastBuildDate` Thu 12 Nov 05:00 UTC, 892 bytes, **0 items in the
feed**, so 0 could pass the ad filter. This is a different state from the familiar one of items arriving and none
qualifying, and it is the first empty build on file. The raw XML is cached at `cache/arxiv-csir-20261112.xml` so
tomorrow's run can tell a one-day publishing gap apart from a feed that has broken.

### The two platform items

**MD-199, T1, and it is the most consequential thing in the day.** Meta Engineering, 11 November, "Intelligent
Delivery: Making Every Unit of Compute Serve Better Ads", read in full. The depth of the ranking funnel is a
**per-request prediction, not a constant**. A Resource Core Model, 6B sparse and 20M dense parameters, runs once
before candidate retrieval and predicts that single request's outcome, compute consumption and latency impact.
Downstream engines then choose the serving region (rebalanced "in a cycle of minutes"), the CPU or accelerator
generation, the host share under a hard tail-latency SLO, and "the number of ads to rank for each request in each
ranking stage, what ad candidates enter the pool, and much more". Meta credits the allocation layer alone with
"an additional ~10% improvement in ads ranking performance" from 2017 through H1 2026, and the request-identification
model as about 20% better than its predecessor offline. Also published: AI agents "contributed to about 20% of
Intelligent Delivery optimizations" in H1 2026 and about 80% of the engineering effort on the most automated
mechanism, with an engineer approving every change. **What it buys us is a mechanism, not a lever.** Two identical
requests to two identical ad sets can get different serving treatment, and low-predicted-value work is explicitly
trimmed first as host load rises, which is a named cause under the volatility [[Scaling Models#SC-102|SC-102]] tells
low-volume accounts to accept. No advertiser control, no reporting surface, no methodology behind either percentage,
so neither figure is ours to quote.

**GA-101, T1.** Google Ads & Commerce, 12 November, Keerat Sharma, read in full. An **Invalid Traffic Overview Card**
is rolling out in Google Ads showing both the spend saved by pre-billing blocks and the credits Google issues when
invalid activity is caught later, "where appropriate and possible". The one number in the post: "So far in 2026,
we've reduced advertiser exposure to invalid **leads** by an average of 30%." Leads, not clicks, which makes it the
more relevant figure for the lead-gen accounts we run, and it ships with no baseline, no denominator, no definition
of an invalid lead and no breakdown. Useful as a place to look before theorising about a soft Google week. Never
quotable to a client as a saving their account received.

### The two transcripts

**Charley T, 9,606 words, and the honest summary is that the system is already in the codex.** The 322 definition, the
Olympic rings, the one-concept rule, the hypothesis rule, the harvest signal, the conversion-volume gating of account
complexity, the launch-displacement reframe of fatigue and the 4PI read were all banked before today. Four things were
genuinely new or sharper:

- **MD-200 new, T3. "Mid-funnel" is rejected outright as a readable state.** An ad's funnel position is its daily
  frequency against **the campaign's own daily frequency**, so a campaign sitting at 1.23 makes every ad below 1.23
  upper-funnel and every ad above it lower-funnel, and no external number applies. The diagnostic half is the pairing:
  low frequency with low CPM is funnel-filling and its cost per result is *supposed* to be worse than average, while
  high frequency with high CPM must beat the average or "it's a bad retargeting ad". That supplies the comparator
  [[Meta Delivery & Andromeda#MD-047|MD-047]] never had.
- **SC-183 new, T3. A test is judged only on whether the account can absorb more money afterwards.** Three outcomes:
  earns spend and lifts profit volume (win, change nothing, let the rule scale it); takes spend but the budget still
  cannot rise (**loss, even with a good CPA or ROAS**, "a test that earns money and doesn't allow you to scale the
  budget isn't a win"); or takes no spend at all (delivery's verdict, with a 20% ad-set minimum as the single
  exception for a starved lower-funnel test). The pass mark being the account's capacity rather than the ad's own row
  is the part worth having.
- **SC-049 amended, and this is the fix for its own worst counter-example.** The liability rule finally has a spend
  band: act only on an ad **taking at least 10% and no more than 40%** of budget with CPA above and GPT below the
  campaign average, and **leave anything above 40% alone** because "removing it changes how the whole campaign works".
  Wait 48 hours, re-read on a trailing 7-day view, two or three moves a week at most. The 40% ceiling protects exactly
  the ad whose removal cut GPT from $206 to $131 in SC-049's account three.
- **SC-001 amended, with a contradiction logged.** The half-the-headroom rule is restated with the target CPA sourced
  from unit economics and the current figure as trailing 7-day, plus a new and testable mechanism for why only half
  the gap is spent: new budget buys colder impressions first, about 2,500 of them per sale at a $50 CPA and a $20 CPM
  (checks: 50/20 x 1,000), so cost per result rises for a while after every increase. His automated rule fires
  **Monday, Wednesday and Friday only**, on the reasoning that a daily rule compounds before the account absorbs the
  last move. [[Scaling Models#SC-101|SC-101]] has Ben Heath prescribing **one firing daily**. Both asserted from large
  books with no data. Cheap to settle on our own accounts: same rule, same step, one campaign daily against a
  comparable one three times a week, read account cost per result at 30 days.

Two smaller merges from the same transcript. **LS-045 finally has the formula for its own prerequisite**, the
qualified-lead conversion value, and the same sentence states it two incompatible ways: "sales price times close rate"
(correct) and "divide the sale price by that close rate" (wrong by a factor of 25 at a 20% close rate). Use the
multiply form. It is another instance of the arithmetic-reliability pattern at [[Scaling Models#SC-148|SC-148]]. And
**CR-162 records that this operator restated the obsolete no-breakdown position after the correction**, calling it
"not a bug, it's a feature"; half of that is still true, because per-media spend is visible while the copy
cross-tabulation still is not. Discarded as fluff: the day-trade framing (already banked), the five-rings worked
example (already banked), the Messi and great-white analogies, and every program plug.

**Ben Heath, 4,944 words, one subject, and all of it lands in Marketing Math.** Nothing new on delivery or structure.

- **MM-002 amended with a FOURTH stated numerator, and it widens the band dispute instead of the numerator dispute.**
  He uses gross profit explicitly and defends excluding overheads "because those are relatively fixed. They're not
  marginal as you scale", which puts three of five operators on the gross-profit numerator. The problem is the band:
  Blue Sense ramps at 2 to 3 on the same numerator and reads above 3 as leaving money on the table, while Heath calls
  **10** "fantastic" and treats **28.8** as the goal. An order of magnitude apart on the same metric. The likely
  reconciliation is the book behind each: e-commerce audits where media is nearly the whole acquisition cost against
  services and local businesses carrying heavy delivery labour. The operating rule gains a second half: state the
  numerator AND the business model before comparing any ratio.
- **MM-068 amended with the lead-gen port, arithmetic verified.** Maximum acceptable cost per purchase is AOV x gross
  margin; maximum acceptable cost per lead is **AOV x gross margin x lead-to-client close rate**. His sensitivity run
  is the keeper because it prices the sales process as a media lever: on $750 of gross profit the ceiling is **$75 at
  a 10% close rate, $150 at 20%, $225 at 30%**, a threefold swing in what the account may pay per lead with the ad,
  the offer and the margin all unchanged. Third operator to derive the ceiling from the business rather than from a
  benchmark.
- **MM-121 amended, and every figure recomputes exactly.** One baseline, AOV $200, five purchases, 50% margin, $50
  CAC, ratio 10. Working the CAC side 25% harder gives **12.5**. Moving AOV to $300, purchases to 8 and margin to 60%
  gives **28.8**. The subscription version halves AOV to $100 while taking purchases from 5 to 23 and still reaches
  **23**. All three check. It is still arithmetic rather than evidence, and the CAC scenario is deliberately modest
  against a value scenario that moves three terms at once, so the tier stays at T4. It converges with the independent
  lever rankings at [[Marketing Math & Unit Economics#MM-159|MM-159]] and
  [[Marketing Math & Unit Economics#MM-094|MM-094]].

Discarded from this transcript: the $300M-spend and $1.2B-revenue credential, the mother's interior-design and hair-
salon anecdotes (illustration, no figures that test anything), the private-jet-brokerage aside, the Demand Gen plug,
and the school-community promotion.

### Gaps

- **The per-channel rejection count is still not built, eighth day.** Asked for on 5 November. Today 5 uploads were
  rejected as too short and 2 for having no subtitles, and there is still no record of which channels they came from,
  so a channel that has switched to clips cannot be told apart from a channel that has gone quiet.
- **Meta for Business News was not read this pass.** The pinned-URL route needs a WebFetch fallback when the plain
  fetch returns HTTP 400, and this session had no browser: Playwright MCP failed to connect (CONNECT_TIMEOUT). The
  source has held one US state for 14 consecutive reads with a 28 October 2026 ceiling, and the only valid test for
  movement is a slug absent from the 36-member cumulative set, so a single missed day carries low risk. Read it
  tomorrow.
- **The arXiv empty build needs one confirming read.** If 13 November also returns 0 items, the feed is broken rather
  than quiet and the source needs a replacement route.
- **Nothing in MD-199 is testable by us,** which is the gap worth naming rather than hiding: the codex now holds a T1
  mechanism for per-request serving variance with no advertiser-visible correlate at all, so it can explain a
  volatility reading after the fact but can never predict one.

"""

t = io.open(P, encoding="utf-8").read()
anchor = "## 2026-11-11 (research run)"
assert t.count(anchor) == 1
t = t.replace(anchor, ENTRY + anchor, 1)
io.open(P, "w", encoding="utf-8", newline="\n").write(t)
print("harvest log ok")
