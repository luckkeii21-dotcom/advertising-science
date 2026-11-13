# New claims for the 2026-11-13 research run: AT-135 through AT-138.
# Append-only. Amendments to existing claims live in _amend_20261113.py.
import io

AT = (r"E:\claude code marketing skill\Obsidian God-level Marketing Vault"
      r"\God-level Marketing\wiki\science\Attribution & Incrementality.md")

NEW_CLAIMS = """
### AT-135 \u00b7 Meta's own attribution-calibration recipe is a single scalar multiplier from a lift test, and its overshoot rule dumps the leftover conversions on organic
Tier: T1 \u00b7 Status: active
Meta for Business, "Calibrating Attribution with Incrementality Experiments for Optimal Budget Allocation", read in full at source 2026-11-13. The page prints "October 22" with **no year anywhere next to it**; the sequel at [[Attribution & Incrementality#AT-136|AT-136]] is dated 29 October 2025 and calls this one "a previous piece", which places it in October 2025. Date it that way and state the inference when quoting it.

**Meta's four steps, verbatim.** "Run incrementality experiments on all platforms (e.g., Conversion Lift for Meta)." "Compare experimental results to your attribution model to see how they align." "Test different attribution models (last-click, even credit, data-driven) and see which best matches incremental impact." "Adjust your attribution outputs using multipliers based on experiment results."

**The multiplier, worked on a company Meta itself labels fictional.** "Coats & More" measures with a click-based multi-touch attribution model reading Meta 100 conversions, Platform X 200, Platform Y 80, Organic 120. Meta then states that "a Conversion Lift test reveals Meta actually drove 150 incremental conversions". The arithmetic as Meta prints it: **"150 (Conversion Lift) / 100 (Attribution) = 1.5x"**, followed by "This multiplier is then applied to Meta's results from the attribution model going forward."

**The overshoot rule, and it is the part to read twice.** "However, if the total conversions after applying the multiplier exceed actual total conversions, it's best to repeat this process for other platforms." Then: "Run an experiment on Platform X and Y to get their multipliers and adjust accordingly. **Any remaining conversions can be attributed to organic.**"

**Why that last sentence is an accounting convenience and not a measurement.** The procedure scales every paid channel up by its own measured lift and assigns whatever is left of the real total to organic as a residual. Organic never gets an experiment in Meta's recipe, so it absorbs every error in every paid multiplier plus every untested channel. A brand that tests Meta and nothing else, applies 1.5x and books the remainder as organic has not measured organic at all. It has measured Meta and relabelled the difference.

**What Meta does not supply, and the absences are uniform.** No holdout size, no test duration, no minimum conversion volume, no minimum detectable effect, and **zero confidence intervals or significance statements anywhere on a page about experiments**. On refresh cadence the entire guidance is that multipliers "should be updated periodically to stay accurate", plus "Calibration isn't a one-time fix", with **no interval and no refresh trigger**. On harder methods: "There are also more advanced techniques available beyond multipliers", unspecified. And no caveat at all about applying one scalar across campaigns, objectives, placements or audiences inside a single channel.

**Operating rule for us.** Usable as Meta's stated doctrine, and as a cheap first calibration on an account that can afford exactly one lift test. Not usable as evidence that a scalar is correct. If we ever run it: run it per objective rather than per platform, never let organic take the residual, and write the test's window and holdout size next to the multiplier so the next reader knows when it expired.

**The figures in this post, and not one of the three is quotable.** "Businesses using these types of experiments see ROI increases of 20% or more", footnoted to a Bain and Company title and the date February 2023, with **no sample, no baseline, no denominator, no window and no link**. A Meta-commissioned Kantar figure, "businesses use nearly four different measurement solutions on average", n=1,935 decision makers, May 2025, which is survey colour rather than a mechanism. And the Gen Z click claim, whose scope limits are set out at [[Attribution & Incrementality#AT-138|AT-138]].
Sources: Meta for Business, Calibrating Attribution with Incrementality Experiments for Optimal Budget Allocation, page date "October 22" with no year, placed October 2025 from the sequel's back-reference, read in full 2026-11-13
Last touched: 2026-11-13

### AT-136 \u00b7 Meta publishes a three-tier MMM calibration taxonomy, and only the top tier touches carryover and saturation
Tier: T1 \u00b7 Status: active
Meta for Business, "Calibrating Marketing Mix Modeling with Incrementality Experiments for Cross-Channel Understanding", **29 October 2025**, category "Best Practices", no byline, read in full at source 2026-11-13. The sequel to [[Attribution & Incrementality#AT-135|AT-135]]. A conceptual explainer: no formula, no code, no worked example, no fitting procedure.

**The failure mode Meta names for an uncalibrated model.** "If used alone, MMM can misattribute results, systematically over- or under-estimating the effectiveness of specific channels." Meta's ordering rule comes from its own Chief Data Officer, Alex Schultz: "you should only use them when you have run the experiment first", and "then you must periodically back-test to make sure the result is still valid". **The experiment is the input and the model is the output**, which is the same direction Google states for Meridian GeoX at [[Attribution & Incrementality#AT-115|AT-115]]. Two platforms, same doctrine, independently stated.

**Tier 1, Basic, which Meta names "qualitative model selection".** The test is "Are the results pointing in the same direction?" Pass condition: "If both methods show similar trends (for example, both show a positive impact from advertising), the MMM is considered reliable." Meta's own verdict on it: "This is easy to do, but not very precise." **A direction check is not a calibration. An MMM that agrees on the sign can still be wrong by a multiple.**

**Tier 2, Intermediate, "Injecting average effect size estimate from experiments".** The clearest statement of what actually moves: "the parameters of the MMM", specifically "the mean and spread of the estimate", are "directly informed by the results of experiments", and this "allows the prior knowledge from lift experiments to guide the optimization process of MMM", "without the need to rebuild the model from scratch."

**Tier 3, Advanced, "comprehensive parameter calibration".** It "uses lift experiments to adjust not just the main impact of advertising", but also "how long ads keep working after they run (ad stock)" and "how returns decrease as you spend more (media saturation)", so that the model "captures both immediate and carryover effects". **This is the only tier that touches the two parameters deciding what an MMM says about scaling**, which is exactly why the tier label matters: a brand told its MMM is "calibrated" may only have passed the sign check.

**What Meta leaves out, and it is everything an implementer needs.** The word "prior" appears once and Bayesian methods are never named, so there is **no distribution family, no variance mapping and no shrinkage or weighting rule** for turning a point estimate into a prior. No cadence beyond "periodically". **No minimum number of experiments, no minimum history length, no data-volume requirement, and no guidance for the normal case where experiments exist for only some channels.** Nothing on experiment power, on geo-test design, or on whether a null result should move a prior at all. Neither Robyn nor Meridian is named, and no Meta MMM tooling is named either.

**The numbers, and the only one carrying a footnote is the weakest.** "a study conducted by Analytic Edge found that when MMM was calibrated with experiments, measured ROI varied by 29%", footnoted to "Contextual Calibration: Accounting for immediate vs. carry-over effect in MMM calibration", Analytic Edge, December 2023, **not linked**. "Varied by 29%" states **no direction**, no baseline ROI, no number of models or brands, no category and no window, so it cannot be carried in either direction. The two Kantar figures carry **no footnote at all**: "51% of marketers using MMM alongside other tools" and "55% of respondents said they frequently encounter conflicting results". The Kantar work is disclosed in the body as commissioned by Meta.

**Where it leaves us.** Our accounts are nowhere near MMM scale, so the usable output is the vocabulary and the ranking, not the method. The durable line: **when anyone says an MMM is calibrated, ask which of Meta's three tiers they mean**, because tier one is a sign check and tier three is a different object.
Sources: Meta for Business, Calibrating Marketing Mix Modeling with Incrementality Experiments for Cross-Channel Understanding, 2025-10-29, read in full 2026-11-13
Last touched: 2026-11-13

### AT-137 \u00b7 Meta now frames incrementality as a finance control rather than a marketing metric, recommends branded search as the first test, and says a credible range beats a single number
Tier: T1 \u00b7 Status: active
Meta for Business, "From measurement to capital allocation: How leaders are putting incrementality to work", **12 November 2026**, category "Best practices", no byline, read in full at source 2026-11-13. The capstone of the series at [[Attribution & Incrementality#AT-135|AT-135]], [[Attribution & Incrementality#AT-136|AT-136]] and [[Attribution & Incrementality#AT-138|AT-138]].

**Tier the evidence before using any of it.** The entire basis is "two closed-door sessions in North America and the United Kingdom": no attendee count, no session dates, no company named, no report published, plus one internal Meta executive. **There are zero percentages, zero lift figures, zero sample sizes, zero currency figures and zero windows in the post, and no footnote apparatus at all.** So it is T1 on what Meta recommends, and it carries no evidential weight whatsoever on effect sizes.

**The distinction Meta draws, verbatim, and it is the cleanest one-line version we hold.** "Attribution can show where conversions were recorded." Incrementality "goes further by estimating whether advertising caused them". Note the verb Meta chose: **estimating**, not proving.

**The reframe, which is the point of the post.** "This is where incrementality stops being a measurement preference and becomes a financial control", and the argument for urgency is AI: "If AI multiplies output and makes decisions hands-off, causal measurement is the only way to know whether that output produced value or just activity."

**The four practices Meta prescribes.** Agree the outcome metric before budget season and before anyone sees a test result, because "Every business in both rooms optimised for a different primary metric". Walk finance through "how incrementality is measured, how the results are checked and where the method has limits" **before a budget request exists**, so finance can "pressure-test the method before it is used to support an investment". Evaluate the budget as a whole rather than channel by channel, because "Marketing teams organized by channel often optimize around boundaries that customers never experience", and "Otherwise, better tools may simply reinforce existing misalignment". And test brand over the horizon on which brand actually pays back rather than the quarterly funding cycle.

**The first-test recommendation, specific enough to act on.** Start with "one high-spend channel where last-touch attribution and incremental impact are likely to tell different stories", and "Branded search can be a useful place to start because it may capture demand that already exists." That is the same mechanism [[Attribution & Incrementality#AT-113|AT-113]] banks from the other side, where a promotional peak multiplies reported return on demand the brand already had.

**The two sentences worth borrowing for our own reporting.** "Different measurement methods may still produce different answers." And: "In many cases, a credible range will be more useful than a single precise number." Meta is arguing against the point estimate, which is the posture our own client reporting already takes on labelling an estimate as an estimate. **Useful cover the next time a client asks why we gave a band instead of a number.**

**Conversion Lift, and one genuine refinement on the design.** Meta's wording: Conversion Lift "is designed to measure incremental conversions" by comparing outcomes "between people who were eligible to see ads and a randomized holdout group". **Eligibility, not exposure, defines the treated arm.** That is an intention-to-treat design and it is a sharper statement than the wording banked at [[Attribution & Incrementality#AT-125|AT-125]]. Meta also states calibration as a loop: "periodic experiments keep day-to-day reporting honest".

**No advertiser action in it.** No setting, no rollout, no deprecation, no deadline, no API change, no default change. **Geo testing is never mentioned anywhere in the post**, despite sitting above Conversion Lift in our own hierarchy at [[Attribution & Incrementality#AT-022|AT-022]], and no measurement vendor or external study is named at all.
Sources: Meta for Business, From measurement to capital allocation, 2026-11-12, read in full 2026-11-13
Last touched: 2026-11-13

### AT-138 \u00b7 The root of Meta's calibration series ranks the tools explicitly, and the one number it carries is retail-only, North-America-only and measured over a holiday window by Meta itself
Tier: T1 \u00b7 Status: active
Meta for Business, "Measurement 360: Building a 'suite of truth' to capture the incremental impact of advertising", **28 May 2025**, category "Best Practices", no byline, read in full at source 2026-11-13. The earliest post in the series and the one that defines the phrase the other three lean on.

**The definition, verbatim.** Businesses "are moving beyond a single source of truth", which "in many cases, is an attribution model", "to a suite of trusted tools and methods" that "often includes attribution, marketing mix modeling (MMM), and experiments".

**Meta ranks the members, and this is the load-bearing part.** "Randomized control experiments, such as those implemented through Meta Conversion Lift, provide the most accurate measure of incrementality." Models are the thing being corrected rather than the authority: the job named for MTA and MMM is "Calibrating measurement models" "with the results of experiments to accurately reflect real world outcomes". **So Meta's own published ranking puts the experiment above the model and the model above attribution**, which is the same ordering as our own hierarchy at [[Attribution & Incrementality#AT-022|AT-022]] and was arrived at independently.

**The scope limit Meta puts on experiments, and it is one we should keep.** "Experiments are particularly effective for single channel evaluations and in-channel optimization." Read plainly, that concedes an experiment is not the instrument for cross-channel allocation, which is the job Meta hands to the calibrated model. Meta's prescription on frequency is maximalist and unquantified: "Conducting regular experiments, as frequently as possible across as many channels as possible."

**The one number, and every scope limit on it.** "Gen Z is twice as likely to make a purchase without clicking than other generations", footnoted to "91 advertisers across the 'Retail' vertical between 11/26/2023 - 02/27/2024 (Meta, North America)", "Based on Meta in-platform metrics, including 1-day-click and 1-day-view attribution rules", "including web, app, and offline conversions". **The footnote is the right footnote for the claim, and it is thin.** 91 advertisers, retail only, North America only, a 94-day window spanning the holiday peak, and Meta measuring its own platform with no third-party verification. **No base rate is given for either group**, so "twice as likely" has no denominator, and neither the Gen Z age band nor "other generations" is defined. Meta attaches no caveat to any of this. **Never quote it as a general fact about Gen Z purchase behaviour**; it is a retail holiday window read off Meta's own view-through reporting.

**Two further items on the page.** Meta names a prior "Measurement 360 framework" in prose and does not link it. And the actual methodology sits in a report, "Building a Suite of Truth: A Hybrid Approach to Measuring Incrementality", at `facebook.com/business/f/1094917955782254`. **That report was NOT read and nothing here rests on it.** It is carried as a named gap in the Harvest Log.

**The interested-party point, stated once because it applies to all four posts.** Meta publishes the ranking that puts Meta Conversion Lift at the top of it, and the only survey behind the series is Meta-commissioned. That does not make the ranking wrong, and it does mean none of these four posts is independent evidence about effect sizes. Use the series for Meta's doctrine, its vocabulary and its mechanics, and never as proof that the mechanics work.
Sources: Meta for Business, Measurement 360: Building a "suite of truth" to capture the incremental impact of advertising, 2025-05-28, read in full 2026-11-13
Last touched: 2026-11-13
"""

t = io.open(AT, encoding="utf-8").read()
assert "### AT-135" not in t, "AT-135 already present, nothing to do"
t = t.rstrip("\n") + "\n" + NEW_CLAIMS
io.open(AT, "w", encoding="utf-8").write(t)
print("appended AT-135 through AT-138")
