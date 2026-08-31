# -*- coding: utf-8 -*-
"""2026-08-31: write the Harvest Log entry and the run log."""
from pathlib import Path

VAULT = Path(r"E:\claude code marketing skill\Obsidian God-level Marketing Vault\God-level Marketing\wiki\science")
RUNS = Path(r"E:\claude code marketing skill\.claude\skills\advertising-science\runs")

ENTRY = """## 2026-08-31 (research run)

**3 new transcripts, 0 harvest errors, and the single most actionable platform item in a month: Google is REMOVING campaign-level language targeting from Search next month, documented on Google's own help page. 6 transcripts read in full, 9 claims banked, 1 law-layer update.**

\u26a0 **GOOGLE REMOVES LANGUAGE TARGETING, SEPTEMBER 2026 (GA-069, T1).** Google Ads Help, read today: "Starting in September 2026, the way language targeting works is changing for Search campaigns and the Search Network portion of Performance Max campaigns." For Search: **"The campaign-level language targeting setting will be removed. Search ads will automatically match based on the language of your ads."** Existing criteria stay and stop working. PMax keeps the setting for YouTube, Display, Discover and Gmail and loses it for Search only, so one campaign will run split behaviour across its own channels. **This moves law 1a and it is the first time a platform has stated the control-to-suggestion conversion in writing with a date on it.** Any account structured to keep one language's creative in front of that language's speakers is, from September, held there by the ad copy and the landing page and not by the setting.

**The landing-page methodology gap got its denominators and the answer is worse than silence (AT-111, T2).** AT-106 closed that gap on 27 August with a negative finding: nobody on the roster states a sample size, a conversion floor or a confidence level. A CRO operator has now published five sample sizes on camera off live dashboards. **All five are underpowered for the lift they report, by 1.59x to 7.63x.** Best in the set has 63% of the sample its own result needs, worst has 13%. **The useful half is counter-intuitive: a big sample does not rescue a small effect, because required sample scales with the inverse square of the effect.** The 250,000-visitor test reporting +3.3% is the second-worst powered; the 49,000-visitor test reporting +10% is the best. **AT-027 was recomputed against its own arithmetic and HOLDS**: 40,000 sessions per arm at 2.5% detects a 12.5% relative lift, inside its stated 10-to-20% band. So AT-027 is now the load-bearing claim in that section rather than an assertion.

**A flagship claim refuted by its own dashboard, ninety seconds apart (CR-210).** "The higher the shipping price, the higher the conversion rate" is the operator's headline. His readout says conversion rate +3.3%. He then describes the same test as "CVR is down with the two more expensive groups, revenue went up". **Never repeat the headline.** The seven page tests are banked with their numbers, the two that carry no number at all are banked as guards per the CR-183 precedent, and the internal arithmetic on all five measured tests was recomputed and every one holds. **The problem with that set is power, not honesty**, which is why it splits across two claims.

**The Ads Library instrument at CR-190 has degraded (CR-209, T3).** Meta now stamps Library creative with a "protected" watermark, and the reporting operator says Claude and ChatGPT decline to work with the images because of it: "the actual use of Facebook Ad Library has declined a little bit in just the last few weeks." He sells the tool that solves it, so T3 with the commercial interest attached. **Checkable free on our own competitor sets.** The same source also collapses the impressions sort into a longevity ranking, which is exactly the misread CR-190 was banked to prevent.

**A third independent attributed-versus-incremental gap, and the range is now stable enough to plan against (AT-112).** A Spain launch reading an attributed 20 to 30 return on ad spend measured **5.6 incremental**, a 3.6x to 5.4x gap. AT-098 holds 13 reading 5 reading 1.71, and the same family holds 108 purchases reading 29. **Three brands, three measurement routes, gap lands between roughly 3.5x and 5.5x every time.**

**Backlog: 43 items were carried as "off-topic tutorials" by two prior passes. That triage was wrong in at least three cases.** Spot-checking the most plausibly relevant found a full nine-figure performance case study with geo-lift incrementality data (AT-112), a US-launch economics video with a MER argument worth keeping (MM-197), and a four-minute post-ID tutorial containing a structural limit nobody had priced (SC-153). **Do not treat the remaining backlog as cleared.** 40 remain unextracted: 21 Blue Sense, 17 Mark Builds Brands, 2 Matt Shiver. The Mark Builds Brands set is genuinely mindset content; the Blue Sense remainder is genuinely Shopify and Merchant Center tooling by title, but that is what the last two passes said about the three read today.

**SC-153 is the one to check on our own account.** The post-ID pull "doesn't work" reliably on ads carrying multiple headlines and multiple primary texts. **SC-022 and SC-023 build the whole control ad set out of post IDs harvested from 3-2-2 flexible ads, which are by construction exactly that object.** Nobody has checked whether it is the same failure case. If it is, the harvest step in that architecture has a hole in it.

**Source reliability, two entries, and both operators supplied the evidence themselves.** Fraser Cottrell prescribes a testing/scaling/retargeting budget split and then says "I'm not a media buyer by any means" in the next breath (CR-211), so his creative material and his structural material do not carry the same weight. And Blue Sense fails the arithmetic gate twice more: "we doubled year-on-year growth rate from 119% to 362%" is a **tripling** (3.04x) and he says "almost 3xed" one sentence later without noticing; 400% and 250% averaged is **325, not the 327 stated**; and a US launch adding $2M to a $3M business is called a **doubling** when it is +67%. **That channel's MM-176 warning keeps earning its place.**

**Watchlist: 0 new items on every readable source, and one predicted trap fired exactly as recorded.** RSS 0 new across Meta Engineering, Meta Newsroom and Google Ads & Commerce. **The Marketing API changelog index under-rendered to v25.0 again**, which is the artefact the 2026-08-24 note warned about; Graph API confirms **v26.0, 29 July 2026**, unchanged. Google Ads API v25.1 (19 Aug) already banked. TikTok SDK unchanged at 0.1.8; the three geo-blocked TikTok sources were not retried and the Playwright browser was unavailable this session, so **TikTok is unmonitored today and is not logged as clean**. AI at Meta blog carries no ads-ranking posts (newest ads-adjacent: nothing; July posts are generative media and robotics). **New since the last weekly check: Merchant Center reporting definitions changed 24 August 2026 (GP-043), and the Google Ads Developer Blog carries "Migrate Campaign-level Broad Match and Automatically Created Assets to AI Max" (12 Aug), which is GA-047's prediction that Google would push AI Max harder in 2026 arriving on schedule.**

**Two read-quality flags, stated rather than smoothed.** The Google Ads Developer Blog post body did not render to two separate fetches, so GA-069's substance comes from Google's help centre page and trade coverage while the blog supplies only the title and date; the `ContextError.OPERATION_NOT_PERMITTED_FOR_CONTEXT` API detail is recorded as reported and unverified. And the Merchant Center detail page returned HTTP 404, so GP-043 states only what the changelog entry itself says.

**Gap logged against the engine, not against a source.** The arXiv filter returned 1 item today, "HubMixer: Progressive Latent Hub Mixing for Parameter-Efficient Feature Interaction in Recommendation". Its abstract was read in full. **It is a Kuaishou short-video recruitment recommender paper reporting a 5.48% lift in resume submission conversion rate, and it passed the advertising filter on the phrase "recommendation and advertising ranking systems" in its opening framing sentence.** The 2026-08-19 tightening required a bank-list hit and this is a bank-list hit inside boilerplate. **Not banked.** The filter needs a rule that discounts an "advertising" mention appearing only in a paper's first sentence. Also worth stating: today's run read the **Monday 31 August 04:00 UTC build**, not Sunday's, because it fired at 17:20 IST rather than 07:00, so the usual one-day lag did not apply today.

**A second engine finding, cheap and worth keeping.** The Google Ads Announcements diff reported 1 line added and 1 removed. The checker was run twice within two minutes and **the "added" token differed between runs** (3697659702011457550, then 2629469373506859982). **Those are per-request nonces, not content.** A single-line add/remove on that source is noise and should not be reported as a change.

"""

RUNLOG = """# Advertising Science research run: 2026-08-31

Executed `RUNBOOK-RESEARCH.md` top to bottom. Run started 17:20 IST (manual, not the 07:00 task).

## 1. Harvest

`harvest.py daily`: **3 new transcripts, 0 errors**, 6 skipped short, 0 no-subs, 0 out of window.

- Sam Piliero, *Claude + Meta Ads Library = Unlimited Winning Ad Creatives*, 2026-08-31, 3,007 words
- Fraser Cottrell, *FREE Meta Ads Course for Shopify Dropshipping*, 2026-08-30, 3,808 words
- Andrew Faris with Dave Diederen, *7 Real CRO Tests That Drove Big Profit Lifts*, 2026-08-31, 10,736 words

Nine of twelve roster channels returned nothing.

## 2. Watchlist

**0 new items on every readable source.** No errors.

| Source | Result |
|---|---|
| Meta Engineering RSS | 200, 9 in feed, 0 new (build Thu 27 Aug) |
| Meta Newsroom RSS | 200, 10 in feed, 0 new (build Fri 28 Aug) |
| Google Ads & Commerce RSS | 200, 20 in feed, 0 new (build Thu 27 Aug) |
| arXiv cs.IR | 200, 33 in feed, 1 passed the ad filter, **0 banked** (false positive, see below) |
| TikTok SDK changelog | 200, top version 0.1.8, unchanged |
| Google Ads Announcements | 200, 1 line added / 1 removed, **both per-request nonces, not content** |

Weekly (Monday) sources, all fetched:

- **Marketing API changelog index under-rendered to v25.0 again.** This is the artefact recorded 2026-08-24. Graph API confirms **v26.0, 29 July 2026**. No change.
- Google Ads API: **v25.1, 19 August 2026**. Already banked, no change.
- Ads Developer Blog: newest 27 Aug (DV360). **Two items of interest: "Google Ads language targeting changes starting September 2026" (13 Aug) and "Migrate Campaign-level Broad Match and Automatically Created Assets to AI Max" (12 Aug).**
- Merchant Center changelog: **new since last check, 11 August 2026 entry, reporting definitions change effective 24 August 2026.**
- AI at Meta blog: no ads-ranking or delivery posts. Newest are generative media and robotics.
- Meta Advertising Standards: page structure read, **still shows no last-updated or effective date and still has no cached text baseline**, so a silent rewrite would pass undetected. **Not logged as clean.**
- **TikTok: browser check SKIPPED, Playwright MCP failed to connect this session.** The three geo-blocked sources were not retried per the standing rule. TikTok product and policy news is unmonitored today.

## 3. Extraction

**6 transcripts read start to finish** (3 new plus 3 pulled from backlog). **9 claims banked, 0 merged into existing, 0 contested.** Nothing was flagged `extracted` that was not read in full.

| ID | File | Tier |
|---|---|---|
| GA-069 | Google Auction & Smart Bidding | T1 |
| GP-043 | Google PMax & Shopping | T1 |
| CR-209 | Creative Science | T3 |
| CR-210 | Creative Science | T2/T3/T4 |
| CR-211 | Creative Science | T3 |
| AT-111 | Attribution & Incrementality | T2 |
| AT-112 | Attribution & Incrementality | T3 |
| SC-153 | Scaling Models | T3 |
| MM-197 | Marketing Math & Unit Economics | T3 |

**Backlog: 40 unextracted remain** (21 Blue Sense, 17 Mark Builds Brands, 2 Matt Shiver), down from 43. The runbook's 25-most-substantive rule was not run as a flat top-25. Two prior passes classified this backlog as off-topic tutorials; three of the items spot-checked today were substantive and produced AT-112, MM-197 and SC-153, so **that triage is recorded as unreliable rather than accepted.**

**Arithmetic gate: 24 stated figures recomputed. 6 failed.**

- PASS: five CRO tests' conversion x average-order-value against stated revenue per visitor, all coherent
- PASS: AT-027's own threshold (40,000 sessions/arm at 2.5% detects 12.5%, inside its stated band)
- PASS: Piliero's $670,000 at 2.36 return called "like a million and a half" ($1,581,200, 5.4% under)
- PASS: MER of 4 as a 25% marketing allocation
- PASS: Cottrell's budget bands can sum to 100
- **FAIL:** 119% to 362% called "doubled" (it is 3.04x, a tripling)
- **FAIL:** 400% and 250% averaged given as 327% (it is 325%)
- **FAIL:** $3M business plus $2M called a "doubling" (it is +67%)
- **FAIL:** $173k in one month presented as "a $2 million business" (annualised run rate, not realised)
- **FAIL:** headline "over 650%" against a body figure of 645%, and the metric switches from sales to new customers
- **FAIL (quote, not arithmetic):** "making the font 5% bigger" when the source said two to four PIXELS and 5% was the conversion lift

None of the failed figures entered a law.

## 4. Law layer

**Updated.** GA-069 is T1, dated and documented, and it moves law 1a by giving it a Google half stated by the platform in writing. Three paragraphs added to the hot layer: the language-targeting removal, the AT-111 power finding with AT-027's self-check, and the CR-209 Ads Library degradation. Counts recomputed from the topic files: **1,125 claims (90 T1, 116 T2, 770 T3, 149 T4; 1,020 active, 99 contested, 5 superseded, 1 refuted) across 11 topic files.** Reconciles exactly against 1,116 + 9.

## 5. Errors and gaps

- **Playwright MCP failed to connect** (CONNECT_TIMEOUT, all four profiles). TikTok browser check skipped.
- **Google Ads Developer Blog post body did not render** to two separate fetches. GA-069's substance came from Google's help centre; the API `ContextError` detail is recorded as reported and unverified.
- **Merchant Center detail page returned HTTP 404.** GP-043 states only what the changelog entry says.
- **arXiv filter false positive.** "HubMixer" passed on the phrase "recommendation and advertising ranking systems" in its opening sentence. It is a Kuaishou recruitment recommender paper. **The filter needs a rule discounting an advertising mention that appears only in a paper's framing sentence.**
- **Meta Advertising Standards still has no cached baseline.** Unchanged since 2026-08-24. Not logged as clean.
- Today's arXiv read was the Monday 04:00 UTC build rather than Sunday's, because the run fired at 17:20 IST. The usual one-day lag did not apply.
"""

hl = VAULT / "Harvest Log.md"
b = hl.read_text(encoding="utf-8")
anchor = "## 2026-08-30 (research run)"
assert anchor in b, "harvest log anchor missing"
b = b.replace(anchor, ENTRY + anchor, 1)
hl.write_text(b, encoding="utf-8")
print("Harvest Log entry inserted")

rl = RUNS / "2026-08-31-research-log.md"
rl.write_text(RUNLOG, encoding="utf-8")
print(f"run log written: {rl}")
