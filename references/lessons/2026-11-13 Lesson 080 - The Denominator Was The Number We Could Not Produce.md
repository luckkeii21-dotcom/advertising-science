---
title: "Lesson 080 - The Denominator Was The Number We Could Not Produce"
type: lesson
lesson: 80
date: 2026-11-13
topic: Attribution & Incrementality
claims: [AT-135, AT-136, AT-137, AT-138, AT-023, AT-022, AT-125, AT-121, AT-115]
tags: [advertising-science, lesson, attribution-incrementality, calibration, incrementality, conversion-lift, data-quality]
---

# Lesson 080 · The Denominator Was The Number We Could Not Produce

🎬 Video: [[video/2026-11-13-lesson-080.mp4]]

Topic: Attribution & Incrementality, harvest-driven, so the pointer holds at 0. Friday, so video day.

This morning's research run found something the engine had been structurally unable to see for seven weeks. One outbound link on a new Meta post opened a four-part Meta for Business methods series spanning eighteen months, and none of the four had ever entered the twelve-slot shelf this lane reads daily. Four new claims, AT-135 through AT-138. All T1.

What they contain is Meta telling us, for the first time, how to correct our own reporting. That is worth a lesson on its own. The reason it is worth today's lesson is narrower: the recipe has a prerequisite Meta never mentions, and it is the exact thing our own accounts have been getting wrong since June.

## 1. The mechanism

Meta's calibration recipe is four steps and the third and fourth are the ones that do work. Run a Conversion Lift test. Compare the result to what your attribution model said. Try other attribution models and see which one matches the experiment best. Then adjust your attribution outputs using a multiplier from the experiment.

The multiplier is one scalar, and Meta works it on a company it labels fictional. "Coats & More" reads 100 Meta conversions out of a click-based model. A Conversion Lift test says Meta actually drove 150. Meta prints the arithmetic:

> 150 (Conversion Lift) / 100 (Attribution) = 1.5x

That number then gets applied to Meta's attributed results "going forward".

Look at what each half of that fraction is. The numerator comes from Meta: a randomised holdout, Meta's own machinery, Meta's own report. **The denominator is yours.** It is whatever your attribution model currently says, pulled from your own reporting. Meta supplies the measurement and leaves the thing being measured entirely unexamined.

The analogy is a kitchen scale and a calibration weight. You buy a 10kg reference weight, set it on the scale, read 12kg, and work out the scale reads 1.2x high. From then on you divide every reading by 1.2 and call the scale calibrated. The procedure is sound and it is the right procedure. It has one unstated requirement: the weight has to actually be 10kg. Hand someone an unverified weight and the calibration step does not fail loudly. It produces a confident correction in the wrong direction, and the operator now trusts the scale more than before they started.

Meta's recipe is that calibration. The Conversion Lift test is the reference weight. Your attributed count is the scale reading. And the whole value of the exercise sits in a number Meta does not ask you to check.

Then there is the fourth step, which deserves reading twice. If the multiplied total comes out higher than your real total conversions, Meta says to run experiments on the other platforms too, get their multipliers, and then: "Any remaining conversions can be attributed to organic."

Organic never gets an experiment anywhere in the procedure. So organic is the residual. It absorbs every error in every paid multiplier, plus every channel you did not test. A brand that tests Meta, applies 1.5x and books the leftover as organic has not measured organic at all. It measured Meta and relabelled the difference.

## 2. The evidence

All four new claims are **T1**, and the tier means one specific thing here: this is reliably what Meta recommends. It is not evidence that the recommendation works.

- [[Attribution & Incrementality#AT-135|AT-135]], T1. The multiplier recipe and the residual-to-organic step. The absences are uniform and they matter: no holdout size, no test duration, no minimum conversion volume, no minimum detectable effect, and **zero confidence intervals anywhere on a page about experiments**. The entire refresh guidance is that multipliers "should be updated periodically", with no interval and no trigger. The one worked example is fictional.
- [[Attribution & Incrementality#AT-136|AT-136]], T1. The three-tier MMM calibration taxonomy. Tier one is "qualitative model selection" and the whole test is whether both methods point the same direction; Meta's own verdict on it is "not very precise". Tier two injects the experiment's mean and spread into the model's parameters. Tier three is the only tier that touches ad stock and media saturation, which are the two parameters that decide what a model says about scaling. **This gives you a question to ask out loud: when anyone tells you a model is calibrated, ask which tier.** An agency can pass tier one and use the word.
- [[Attribution & Incrementality#AT-137|AT-137]], T1, published yesterday. Incrementality reframed as a finance control. Two sentences worth stealing for our own reporting: "Different measurement methods may still produce different answers", and "a credible range will be more useful than a single precise number". Tier the evidence honestly before quoting any of it: the basis is two unnamed, undated closed-door roundtables plus one internal Meta executive, and the post contains zero numbers of any kind.
- [[Attribution & Incrementality#AT-138|AT-138]], T1, the root post from May 2025. Meta ranks its own tools: randomised control experiments "provide the most accurate measure of incrementality", and attribution models and MMM exist to be corrected by them. Keep the scope limit Meta attaches, because it is a concession: experiments are "particularly effective for single channel evaluations and in-channel optimization". Cross-channel allocation goes to the model.

Two older claims moved, and both movements are about who we are arguing with.

[[Attribution & Incrementality#AT-023|AT-023]] is the contested one on whether to log a static discount factor per campaign type. Position B, for fixed multipliers, now has a **T1 endorser**, because Meta publishes exactly the method one practitioner was arguing for against Haus. The status stays contested, and the reason is precise: Haus's objection is decay over time, and Meta's only cadence word is "periodically". The T1 lands on the method and is silent on the frequency, which is the half the disagreement is actually about.

[[Attribution & Incrementality#AT-022|AT-022]], our measurement hierarchy, now has both platforms publishing our ordering. Meta states it at AT-138, Google states it for Meridian GeoX at [[Attribution & Incrementality#AT-115|AT-115]]. **The tier deliberately stays T3.** Two interested platforms agreeing is agreement, not evidence, and both of them sell the experiment that sits at the top. What changed is that we no longer defend the ordering alone in front of a client.

## 3. Our accounts

We have never run a Conversion Lift test on any account. So the numerator in Meta's fraction does not exist on our book, and this lesson is not an instruction to go calibrate anything. The useful half is the other half.

**Phoenix Truxx, September 2026.** Ads Manager said 706 leads at $8.18. Real people from the ads, counted in the CRM by first-touch ad id: **417 at $13.86**. The cause is on file as a published GoHighLevel workflow sending a Lead event back to Meta on every instant-form submission, so the same person landed in the column twice. The ratio between those two counts is 1.69.

Now run Meta's recipe against both denominators. Suppose a lift test had come back at 500 incremental conversions for that month.

| Denominator | Multiplier | What we would have written |
|---|---|---|
| 706, Ads Manager | 500 / 706 = **0.71** | Meta over-reports by 29%, discount it |
| 417, real people | 500 / 417 = **1.20** | Meta under-reports by 20%, uplift it |

Same test, same month, same account, opposite verdicts on direction. And this is not a knife edge. The inflated denominator reads "over-reporting" for any lift figure below 706 and the real one reads "under-reporting" for anything above 417, so **every possible true lift in a 289-wide band flips sign between the two counts**. That band is 69% of the real conversion count. The calibration step does not detect the problem. It converts it into a number with a decimal point in it and hands it to a client.

**SJR Commercial, September 2026.** The same shape, larger. The cargo van campaign reported 390 website leads against 237 landing page views of its own, which is impossible on its face. The draft monthly said 809 opt-ins at $4.07 across vans and dump; those two lanes held **358 real people at $9.19**. Ratio 2.26.

Here is the part to sit with. Phoenix's echo has been **off since 21 October**, so that lead column has been clean for twenty-three days. **SJR's source has never been found.** The task to go look for it was opened on 8 October and is thirty-six days old today. So on one of our two largest accounts we still cannot produce the denominator Meta's recipe divides by, and the first step of the recipe is the only step Meta spends no words on.

There is a second denominator problem underneath the first, and it does not go away when a workflow gets fixed. [[Attribution & Incrementality#AT-121|AT-121]], T2 on our own exports: GoHighLevel merges a repeat opt-in into the existing contact on the email address, so SJR's 20,751-contact file returns 99.94% net-new **by construction**. A contact-record count is a count of first appearances. Our clean denominator counts people. A Conversion Lift numerator counts conversions. Those are different units and the fraction does not care.

One more honest limit, from [[Attribution & Incrementality#AT-125|AT-125]]: Meta puts a reliable Conversion Lift read at 2 to 3 weeks at holiday conversion volume and 6 or more weeks in a quiet quarter. Phoenix produces around 80 opt-ins a week. Meta publishes no minimum conversion volume anywhere in the series, so we cannot size the test from Meta's own documentation even if we wanted to book one.

## 4. The decision rule

**Before applying any multiplier to a channel, prove the denominator. A calibration factor is a ratio of two counts, and the one you own is the one that is wrong.**

Three practical consequences. When a client or an agency proposes a fixed discount on a channel's reported numbers, they are quoting platform doctrine now, so argue the cadence and the denominator rather than the method. When anyone says a model is calibrated, ask which of Meta's three tiers. And never put a multiplied number in a client report, because the series that supplies the method supplies no confidence interval to put next to it.

## 5. Quiz

Drop your answers in `lessons/_answers-inbox.md` with the lesson number. The next teacher run grades them.

**Q1.** Meta's recipe divides a lift figure by an attributed figure. State which side of that fraction Meta supplies and which side you supply, and say in one sentence why that asymmetry is the whole risk.

**Q2.** Meta's overshoot step ends with "Any remaining conversions can be attributed to organic." Explain what is wrong with that sentence as a measurement. Your answer must name what organic absorbs.

**Q3.** An agency sends SJR a slide saying their media mix model is calibrated against incrementality experiments. You get one question before the call ends. What do you ask, and what are the three possible answers you might get back?

**Q4.** Phoenix Truxx ran a Conversion Lift test in September 2026 and it returned 600 incremental conversions. Compute the multiplier on both the Ads Manager count and the real-people count. Say which one you would have reported that month and why, and name the date after which that question stops arising for this account.

**Q5.** A teammate writes in the client channel: "Meta's own documentation says to apply a 1.5x multiplier to Meta's reported conversions." Correct the sentence. Your answer should fix two separate errors in it.

> [!note]- Answer key
> **A1.** Meta supplies the **numerator**, the lift figure from a Conversion Lift test run on Meta's own machinery. You supply the **denominator**, your attributed conversion count out of your own reporting. The asymmetry is the risk because Meta's recipe treats the denominator as a given and spends no words on validating it, so the entire correction inherits whatever is wrong with your own count, and it comes out the far end as a confident decimal rather than as an error. Credit for naming the calibration-weight idea: the procedure is sound and silently assumes the reference is true.
>
> **A2.** Organic is never experimented on anywhere in Meta's procedure, so it is a **residual** rather than a measurement. It absorbs every error in every paid multiplier, plus the entire contribution of every channel that was not tested. A brand that tests Meta only, applies its multiplier and books the leftover as organic has measured Meta and relabelled the difference. Full credit requires naming both things organic absorbs: paid multiplier error and untested channels.
>
> **A3.** Ask **which of the three tiers** the calibration used (AT-136). The three answers: **tier one**, qualitative model selection, which only checks that both methods point the same direction and which Meta itself calls "not very precise"; **tier two**, injecting the experiment's mean and spread into the model's parameters; **tier three**, comprehensive parameter calibration, the only tier that touches ad stock and media saturation. Credit for knowing why the question matters: tier one lets someone use the word "calibrated" truthfully while the model can still be wrong by a multiple, and tier three is the only one that changes what the model says about scaling.
>
> **A4.** On Ads Manager's 706: 600 / 706 = **0.85**, read as Meta over-reporting by 15%, so discount it. On the real 417: 600 / 417 = **1.44**, read as Meta under-reporting by 44%, so uplift it. Report **neither**. The honest answer is that in September 2026 this account could not produce a trustworthy denominator, so no multiplier should have been computed at all, and a range with the limitation stated beats a single number (AT-137). The date is **21 October 2026**, when the Conversions API echo was switched off and the lead column started matching form submissions. Accepting "1.44, because real people are the right basis" earns partial credit only: the basis is right and publishing a multiplier off a single unsized test is still not something we do.
>
> **A5.** Error one: **1.5x is not a recommendation, it is a worked example on a company Meta labels fictional.** The method is the recipe; the number belongs to "Coats & More" and to nothing else. Error two: **the multiplier is not applied to Meta's reported conversions, it is derived from them.** You divide your own lift result by your own attributed count to produce your own factor, and ours does not exist because we have never run a lift test. Credit for adding either guard: the series carries zero confidence intervals, or Meta's only refresh guidance is "periodically" with no interval and no trigger.
