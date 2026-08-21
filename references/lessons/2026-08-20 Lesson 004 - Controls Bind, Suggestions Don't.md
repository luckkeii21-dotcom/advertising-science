---
title: "Lesson 004: Controls Bind, Suggestions Don't"
lesson: 4
topic: "Meta Delivery & Andromeda"
date: 2026-08-20
source: "harvest (MD-019 resolved to T1, MD-019b new; MD-013, MD-062, MD-100)"
video: none (Thursday, not a video day)
tags: [advertising-science, lesson]
---

# Lesson 004: Controls Bind, Suggestions Don't

> This morning's research run closed MD-019, a question that had sat open for three runs. It was closed by reading Meta's documentation, not by watching another 25 hours of podcasts. Hold onto that.

## The mechanism

Open any Meta ad set. You see a stack of targeting boxes and they all look equal. Location, age, gender, language, detailed targeting, custom audiences, lookalikes. Same panel, same styling, same apparent authority.

They are not equal. The panel has two halves and only one of them is enforced.

**Controls bind.** Location, minimum age, language, and exclusions. Meta will not cross these. Type a boundary and delivery stays inside it.

**Suggestions do not bind.** Interests, lookalikes, custom audiences. These are model inputs. Meta reads them as a hint about who might work, then goes wherever it thinks the conversion is. Ben Heath demonstrates it in the UI: select a 180-day website-visitor custom audience and Meta "will reach people within this audience... but they will also go beyond that to reach other people that Meta believes are going to generate a sale." Select only a lookalike and Meta prints its own label on the screen: *lookalike audiences are always suggestions*.

The analogy that maps: you hire a courier, give them a delivery zone, and pay them per delivery. They will never leave the zone. Inside the zone they will do whatever deliveries are quickest and cheapest for them. Hand them a note saying "I'd prefer the north side" and it changes nothing, because they are paid per delivery and the note is not.

Two consequences follow, and the second one is the expensive one.

1. An ad set labelled "retargeting" is not a retargeting ad set. It is a broad ad set with a warm hint attached.
2. **The boundary you draw is the whole instruction.** Inside it, the machine optimises on its own cost gradient. If you draw the box too wide, all your spend lands in the cheap corner, and cheap is not the same as good.

## The evidence, in tiers

**[[Meta Delivery & Andromeda|MD-013]], T2, active.** The controls-versus-suggestions split. This is T2 because it is shown in the product, not merely asserted: Meta prints the "always suggestions" label itself. Four independent operators agree on the same list of hard boundaries. Read it per input, not as a blanket. Ticking "further limit the reach of your ads" does harden age, gender and detailed targeting into real constraints, and Meta warns you in-product that results will get worse.

**[[Meta Delivery & Andromeda|MD-019]], upgraded to T1 today.** Audience segments (new / engaged / existing) are a **reporting breakdown**, not a delivery control. Meta's help article opens with it: "You can use audience segments to enable breakdown reporting." In the API it is `user_segment_key`, a breakdowns parameter on the insights endpoint. There is no matching field on the campaign object.

**[[Meta Delivery & Andromeda|MD-019b]], T1, new today.** There *was* a real delivery control and Meta killed it. `existing_customer_budget_percentage` was an ad set parameter capping the share of budget spendable on existing customers. Meta's help centre now reads "no longer available," and the API docs say campaigns using it "will be paused" at Marketing API v26.0, which shipped **29 July 2026**, 22 days ago.

Sit with what that pair means. Two credible operators argued about this in April. Heath said the segments inform delivery. Charley T said reporting only. **Both were describing something real.** Heath was describing a product that Meta has since removed. Charley T is right about the product as it stands today. Neither was lying and neither had checked.

**[[Meta Delivery & Andromeda|MD-062]], T3, and the codex marks it ASSERTED, no data.** "Set geo to the full area you can actually serve and let Meta find the pockets inside it." One source, one sentence, no numbers. Remember that tier. We are about to put a price on it.

**[[Meta Delivery & Andromeda|MD-100]], T1 for surface existence only.** Meta's value rules now expose an "audiences" criterion that applies a **bid multiplier** by audience label. A bid multiplier is delivery. This is the one live candidate for a segment-level delivery lever after MD-019b killed the old one. Nobody on the roster has run it and it has not been checked against documentation. Do not build on it yet.

## Our accounts

**SJR is the cleanest demonstration of the second consequence that we own, and I recomputed it from the raw Meta exports this morning rather than trusting the note.**

The SJR ad sets ran a location setting of New Jersey plus Northeast US. That is a control, so Meta obeyed it exactly. Meta never left the Northeast. It simply found the cheap corner.

| Window | Total spend | Blended cost per result | Blended CPM | Non-lot states, share of spend |
|---|---|---|---|---|
| Jun 9-16 | $4,897.15 | $6.25 | $25.36 | **9.0%** ($439.98) |
| Jul 10-20 | $1,024.23 | $4.00 | $20.43 | **19.8%** ($202.64) |

Why it drifted, from the same exports. June CPM by state:

- Where the lots are: New Jersey **$26.02**, Pennsylvania **$33.14**, New York **$35.77**
- Where there are no lots: North Carolina **$11.54**, Virginia **$11.71**, Maryland **$12.00**, Connecticut **$12.68**, Massachusetts **$13.83**

Impressions in the no-lot bloc cost roughly a third to a half of impressions in New Jersey. Meta is optimising for cost per result, so it walked toward the cheap impressions. In five weeks the no-lot share of spend roughly doubled.

**Now the part that should bother you.** Blended cost per result fell from $6.25 to $4.00, a 36% improvement, while blended CPM fell 19.4%. On a dashboard that is a great month. SJR is a walk-in dealership whose entire trust mechanic is "real address, come meet us." A cheap lead in North Carolina is not a cheap lead. It is a non-lead that flatters the average.

Two honesty limits, and both matter:

- **Meta withheld per-region lead counts in both exports.** Every regional lead cell is zero. I can show you where the spend went and what the impressions cost. I cannot show you the cost per lead by state from these files, so I am not going to quote one.
- The cost-per-result drop has other candidate causes in that window: creative changed and budget changed. The geo drift is a **candidate** contributor, not a proven one. Naming it as proof would be exactly the error Lesson 003 was about.

**What SJR contributes back to the codex.** MD-062 says set geo wide and let Meta find the pockets. It is T3 and carries no data at all. SJR gives it its first shown numbers and also gives it a boundary condition it was missing: **Meta finds the CHEAPEST pocket, which equals the best pocket only when you can serve every pocket equally.** For a national ecommerce brand, cheapest is best. For a dealership with two lots, cheapest is worthless. That is a claim-merge candidate for tomorrow's research run, not a law today.

**ChiroWorks got this right, partly by accident.** The targeting brief says to keep detailed targeting deliberately light and to exclude current patients with a custom audience. Under MD-013 that is well built: the exclusion is a control and binds, the light detailed targeting was never going to bind anyway. Note the tier split though. That the exclusion *works* is MD-013, T2. Whether you *should* run exclusions at all is [[Meta Delivery & Andromeda|MD-068]], T3 and **contested**, with a credible operator arguing they are near-useless on small lists and small budgets. Mechanism and recommendation are separate questions.

**Phoenix Truxx has a live task that needs its expectation reset.** "Upload the buyer list as offline conversions and build a buyer-based lookalike" has been open on `_HOT` since 5 August, due 8 August, still unchecked. Do it. Just know what you are buying: a lookalike sits in the suggestion half, so it seeds the model and does not restrict anyone. [[Meta Delivery & Andromeda|MD-076]] adds the scale, a 1% US lookalike is roughly 2.1 million people. If anyone on that account expects the lookalike to make Meta "target buyers," correct them before it ships.

One curiosity from the SJR June export, flagged as trivial: Baja California, Mexico, **$0.01** of spend. Negligible in money and worth one second of thought, because Meta's default location setting is "living in **or recently in** this location." The stricter option, "People living in this location," is the actual control.

## The decision rule

**Before changing any targeting setting, name which half it lives in. If it is a control, the setting IS the outcome, so draw it at the edge of what the business can genuinely serve and no wider. If it is a suggestion, it is a hint, so never promise anyone it will restrict delivery and never read an ad set's label as its audience.**

## Quiz

Drop your answers in `lessons/_answers-inbox.md` (just "L004: 1) ... 2) ...").

1. List the four hard controls and three of the suggestions. Name the claim ID and its tier.
2. In April, Ben Heath said audience segments inform delivery and Charley T said they are reporting only. This morning the codex ruled that both were describing something real. Explain how both can be true, and name the date and version number that makes it true.
3. SJR's blended cost per result fell from $6.25 to $4.00 between those two windows. Why is that not automatically good news for this client, and what is the one number in the tables above that explains the drift?
4. Scenario: a client asks you to build a "warm audience only" ad set that shows ads exclusively to people who visited the site in the last 30 days. What do you tell them, what do you actually build, and which claim are you leaning on?
5. Scenario: you are handed a new local clinic, one location, patients travel about 20 minutes. A teammate cites MD-062 and says set the geo statewide and let Meta find the pockets. Give your answer, cite the tier of what they quoted, and say what SJR adds to it.

> [!note]- Answer key
> 1. Controls: location, minimum age, language, exclusions. Suggestions: interests / detailed targeting, lookalikes, custom audiences. MD-013, T2. Bonus if you caught the exception: ticking "further limit the reach of your ads" hardens age, gender and detailed targeting into real constraints, and Meta warns results will get worse.
> 2. There are two different surfaces wearing similar names. Audience *segments* defined in account settings were always reporting only (MD-019, T1, `user_segment_key` is a breakdowns parameter on the insights endpoint). Separately, a genuine ad set level delivery control existed, `existing_customer_budget_percentage`, which capped the budget share spendable on existing customers. Meta removed it: campaigns using it are paused as of **Marketing API v26.0, shipped 29 July 2026** (MD-019b, T1). Heath was describing the removed control, Charley T is describing the product as it stands. Neither had checked the documentation, which is why it took three runs to close.
> 3. Because a lead in a state with no lot is close to worthless to a walk-in dealership, so a falling blended cost per result can mean the mix got worse rather than the buying got better. The explaining number is the CPM gradient: New Jersey $26.02 and New York $35.77 against North Carolina $11.54 and Virginia $11.71. Meta optimises on cost per result, cheap impressions sit outside the serviceable area, and the non-lot share of spend went 9.0% to 19.8%. Full credit only if you also said the drop is a candidate cause and not proven, because creative and budget changed in the same window, and that per-region lead counts were withheld so per-state CPL cannot be quoted at all.
> 4. Tell them it cannot be built as described. A custom audience entered in the suggested-audience field is a model input, so Meta reaches those people and then goes beyond them (MD-013, T2). What you build instead: put the 30-day visitor audience in as a suggestion for the seed, and get the actual boundary from the control half by using an **exclusion** on the ad set that should stay cold. Then read the split in reporting rather than assuming it. Also worth saying out loud: whether the exclusion is worth running at all is MD-068, T3 contested, so you are making a bet, not applying a law.
> 5. Do not set it statewide. MD-062 is **T3 and explicitly carries no data**, so it cannot decide anything on its own, and its own text says the only correct input is service capability, which here is a 20-minute drive rather than a state. SJR adds the missing mechanism with real numbers: inside a control boundary Meta walks toward the cheapest impressions, and the cheap pockets in a wide boundary are cheap precisely because nobody valuable is competing for them there. Set the geo to the real catchment, use "People living in this location" rather than the default "living in or recently in," and let the creative do the rest of the targeting.
