---
title: "Lesson 042 - The Benchmark Has a Reset Button"
type: lesson
lesson: 42
date: 2026-10-01
topic: Creative Science
claims: [CR-281, MD-168, CR-248, CR-176, MD-099, CR-124, LS-081]
tags: [advertising-science, lesson, creative-science, benchmarks, client-reporting, meta-ai-surfaces]
---

# Lesson 042 · The Benchmark Has a Reset Button

Meta is rolling out a second AI surface inside Ads Manager. It is called Ads Creative Studio, it is in pre-release on a small number of accounts, and it does at the asset level what the account-level assistant already does: grade the work, compare it to top performers in your category, then generate replacements.

On it, for the first time, Meta prints a **number** for minimum acceptable creative performance. Click-through rate for image ads, **2.92%**. Cost per result, **$20.13**.

For a month this engine has complained that Meta's only published creative grade was Above average, Average or Below average, which tells you almost nothing. A number is better than a letter. So the first instinct is to go and see where our accounts sit against it.

Then look one pixel to the right of the number. Each threshold carries **a slider and a reset button**.

## 1. The mechanism

You set that number. Not Meta, not your category, not the market. You.

Which means the only thing it controls is **which of your own ads get flagged**, and therefore which advice the studio shows you. Drag it up and more of your book turns red. Drag it down and the red goes away. Nothing about the auction has changed in either direction.

Think about the low-balance alert on your banking app. Set it to warn you under $500 and you get pinged most weeks. Set it to $5 and you never hear from it again. Your actual balance does not care where you put the line. The alert was never a measurement of your money. It was a setting about how often you wanted to be bothered.

Two consequences follow, and they are not the same consequence.

**First, an editable number cannot be a market fact.** If every advertiser sets their own 2.92%, then 2.92% is not what anybody achieves. It is what one account's slider happens to be resting on. That rules it out as a benchmark permanently, not until better data arrives.

**Second, an editable number cannot be an auction input.** Meta does not let you type in the thing it charges you. A slider on your screen is downstream of delivery, so it is a reporting filter sitting on top of results that were already decided.

Three things ship on that one surface and all three are the same kind of thing. The thresholds. Native hook rate, hold rate and thruplay columns, which we currently build by hand. A generator that makes new assets from your winners. Every one of them changes what you are **told**. Not one of them changes what you are **charged**, and the studio publishes no outcome data for anything it produces.

There is exactly one place on that surface where something real moved, and it is worth more than the rest of the feature list combined. That is in section 2.

## 2. The evidence

- **[[Creative Science#CR-281|CR-281]], T2.** The spine. 2.92% and $20.13 read off one live account on 2026-09-29, with the slider and the reset button on screen. T2 covers the interface and the figures as read. It covers no outcome, because there is none.
- **[[Meta Delivery & Andromeda#MD-168|MD-168]], T2.** The surface itself: one account, one operator, one session, preceded by a private Meta briefing. No generated asset was shown and no hit rate exists.
- **[[Creative Science#CR-248|CR-248]], T2, ours.** What the old three-band grade was worth on our own book: **22 of 24 conversion-rate grades came back Above average** across three accounts in one week. A column that gives the same answer 19 times out of 20 is not separating those ads.
- **[[Creative Science#CR-176|CR-176]], T2.** Hook rate does not reliably predict cost per result. On screen, one account: a **15.55% hook rate delivered £11.02 per booked call** while a **27% hook rate cost over £30**. The studio now prints hook rate as a native column. That makes the metric cheaper to read. It does not make it predict anything.
- **[[Meta Delivery & Andromeda#MD-099|MD-099]], T1 for existence and surface only.** Opportunity Score, the 0 to 100 account health number, which law 4c already says never to report to a client as a grade. **We have made this exact mistake once.** Lesson 002 records ChiroWorks sitting at 60 out of 100, a number put beside a client's account that nobody in this building could define.

**Tier discipline on the unsourced half.** The claim that the thresholds come from "our data and also data from our competitors" is one operator's reading of an interface. The screen carried no methodology, no window and no pool definition. Treat the cross-account story as unestablished.

**Now the thing that genuinely changed.** [[Creative Science#CR-124|CR-124]] and law 4b have carried this sentence since 25 August as the strongest statement on file about hook swaps: *"Simple hook changes or headline swaps simply don't count as creative testing in Meta's eyes anymore."* Ads Creative Studio offers a lever called **try new video hooks**, describes it in Meta's own interface copy as *"swap out the first 3 to 5 seconds of a video with a different approach"*, gives you a hook-type menu, and generates the variants.

Meta built a generator for the move we were told Meta punishes. **The delivery-penalty story is finished.** What is completely untouched is the question underneath it: does re-cutting the first 3 to 5 seconds of an existing shoot revive a fatigued winner? Nobody has run that. Meta included. A platform recommending a move is not a measured result, and Meta sells inventory every time an advertiser ships an asset.

## 3. Our accounts

Week of **21 to 27 September 2026**, all four live Meta accounts, computed from the raw ad-level exports behind the filed client reports. Click-through rate here is Meta's link click-through rate, link clicks over impressions.

| Account | Spend | Link CTR | Opt-ins | Cost per opt-in |
|---|---|---|---|---|
| SJR Commercial | $769.98 | 2.87% | 151 | $5.10 |
| Phoenix Truxx | $1,391.30 | 1.70% | 150 | $9.28 |
| ChiroWorks | $527.33 | 0.99% | 25 | $21.09 |
| StayWell | $441.44 | 1.63% | 21 | $21.02 |
| **All four** | **$3,130.05** | **1.83%** | **347** | **$9.02** |

**Four accounts. Four for four below 2.92%.** 110,218 impressions, $3,130.05 spent, 347 opt-ins bought. Our best account misses Meta's "minimum acceptable" by 0.05 of a percentage point while buying opt-ins at $5.10. Our worst sits at about a third of it.

One honesty note that belongs with the table: Phoenix Truxx's result count is known to combine Meta's own instant-form count with CAPI website-lead events, which the vault records as running high. Correcting it pushes that $9.28 up, not down.

### Phoenix Truxx, where the default flags the entire book

Twelve ads cleared 500 impressions. **A 2.92% default flags all twelve.** The best in the table is 2.71%.

Narrow it to statics, which is the format the 2.92% is actually for. Six image ads over 500 impressions, **none clear it**, and between them they spent $462.56 and bought **67 opt-ins at $6.90 each**.

### The inversion, inside one optimisation event

[[Learning & Signal#LS-081|LS-081]] says Meta's Results column prints whatever each ad set optimises for, so a comparison that crosses events is worthless. These nine ads all sit on the same website-lead event.

| Link CTR | Ad | Spend | Opt-ins | Cost per opt-in |
|---|---|---|---|---|
| 2.71% | IMG-2 RAM Van | $56.17 | 6 | $9.36 |
| 2.10% | IMG-5 26 ft box | $155.57 | 25 | $6.22 |
| 1.98% | IMG-8 Red F-550 dump | $13.65 | 3 | $4.55 |
| 1.87% | Black Hino rollback | $39.81 | 7 | $5.69 |
| 1.74% | F-550 dump, rent-vs-own | $46.93 | 10 | $4.69 |
| 1.65% | Box Truck Ad version-2 | $122.24 | 21 | $5.82 |
| 1.60% | Plow ready Trucks | $52.01 | 8 | $6.50 |
| 1.55% | IMG-1 Ford Van | $164.22 | 16 | $10.26 |
| 1.10% | IMG-3 Ford-350 | $26.02 | 7 | **$3.72** |

The **lowest** click-through rate in that table is the **cheapest opt-in in the account**, and the filed client report named it the cheapest ad of the week and the strongest debut of the month. The highest click-through rate is the second most expensive. Rank the nine on both columns and the correlation is **+0.13**, which is nothing, and what little there is points the wrong way for a threshold that treats low click-through as underperformance. Nine ads, one week, one account. That is a reading of this file, not a law.

SJR does the same thing on four ads inside its own website-lead event. The threshold passes three at $3.41, $4.00 and $4.79, and flags the one at **$2.67**.

### ChiroWorks, where the flag is right by accident

Two ads, same event, click-through rates of **0.93%** and **0.91%**. Two hundredths of a percentage point apart. Cost per opt-in: **$11.54** and **$122.12**. A factor of **10.6**.

The threshold flags both, for the same reason, with the same wording. The $122.12 ad deserved it. Being right about one of those two while blind to a 10.6x gap is not a diagnostic.

### The two sliders disagree about us

Against $20.13 cost per result, the picture inverts. SJR at $5.10 and Phoenix at $9.28 clear it comfortably. ChiroWorks at $21.09 and StayWell at $21.02 sit just over.

Same four accounts, same seven days, same screen. **One default flags every ad we run. The other flags half the accounts and misses the rest.** Both are editable. Neither is a fact about anything outside our own dashboard.

## 4. The decision rule

**Before a platform number goes anywhere near a client, find out whether you can edit it. If you can, it is a setting on your own dashboard, and it never appears in a report as a benchmark.**

Two things to actually do.

When Ads Creative Studio lands on one of our accounts, **read every default threshold before touching a single slider**, and write each one down beside that account's own trailing click-through rate. If the defaults turn out to be the account's own history, the competitor story is decoration and we will know in four minutes.

And when any of us reaches for a benchmark in a client deck, the question is not whether the number is current. It is who owns the number.

## 5. Quiz

Drop your answers in `lessons/_answers-inbox.md` with the lesson number. No need to write much.

1. The 2.92% has a slider and a reset button next to it. Say in one sentence what that rules out, and why it rules it out permanently rather than until better data arrives.

2. CR-281 records 2.92% as a figure and the video threshold as a description of a screen. Explain the difference and what each one is allowed to be used for.

3. **Applied.** Ads Creative Studio appears on ChiroWorks tomorrow morning. Write the first four minutes: what you read, in what order, what you write down, and what you deliberately do not touch. Then name the single result that would kill the competitor story.

4. **Applied.** Kartik sends you a draft client slide: "Meta's benchmark for this industry is 2.92% click-through. We're at 0.99%. Creative is the problem." Answer him in three sentences. Then name one number from our own accounts, this week, that argues against his conclusion.

5. **Applied, and argue against the lesson.** Make the strongest case that the 2.92% default is useful to us anyway. Then state exactly what would have to be true for it to be a benchmark.

> [!note]- Answer key
> **1.** It rules out the number being a statement about the market, and it rules it out permanently because the value is set per advertiser. If each account sets its own, there is no shared quantity for it to be a statement about. Full credit for naming the market-fact claim as the thing killed. Extra credit for the second kill, that Meta does not let an advertiser type in an auction input, so an editable threshold is downstream of delivery and can only be a reporting filter.
>
> **2.** 2.92% and $20.13 were on screen and are recorded as read, so they can be quoted as what one account's sliders sat on, with the slider caveat attached. The video threshold was described in speech as "a whole percent higher", so about 3.92% is somebody's paraphrase of a screen nobody showed, and it can be used to say the video bar is set higher than the image bar and for nothing numeric. Full credit for distinguishing read from described. Extra credit for noticing this matters on our own book, because most of SJR's funded ads are video and judging them against an image threshold is the wrong comparison before you even get to the slider.
>
> **3.** Open the studio, screenshot the panel before clicking anything, write down both default thresholds and the format split, and do not move a slider or accept a generated asset. Then pull the account's own trailing link click-through rate for the same window and put the two side by side. ChiroWorks ran 0.99% over 21 to 27 September, so if the default lands near 1% rather than near 2.92%, the threshold is the account's own history wearing a competitor label, and the cross-account story is decoration. Full credit for reading before touching, and for naming the account's own rate as the control. Extra credit for also capturing the written diagnosis text, since MD-168 shows the studio explaining its verdicts in prose, and prose that repeats across our four accounts is boilerplate rather than analysis.
>
> **4.** Something close to: 2.92% is a threshold each advertiser sets with a slider, so it is not this industry's benchmark and it is not any industry's benchmark. Our cost per opt-in is the number that decides whether the creative is working, and the slide quotes the one metric on the screen that does not. The number that argues against him is Phoenix Truxx's IMG-3 Ford-350, 1.10% click-through and $3.72 per opt-in, the cheapest ad in that account for the week; or ChiroWorks' own pair at 0.93% and 0.91% costing $11.54 and $122.12, where click-through is identical and cost is 10.6x apart. Full credit for refusing the word benchmark and for moving the argument to cost per opt-in. Extra credit for flagging that the slide would also breach our own reporting rule, since it hands the client a vendor setting as an industry fact, which is the Opportunity Score error from lesson 002 repeated with a better-looking number.
>
> **5.** The honest case: a number beats a letter. CR-248 showed the three-band grade returning Above average for 22 of 24 of our ads, which separates nothing, and a per-format numeric threshold at least varies across our book. It is also a free prompt to go and look at an ad, and ChiroWorks' $122.12 ad was correctly flagged. Treated as a to-do list rather than a verdict, it costs four minutes and occasionally saves money. What it would take to be a benchmark: a fixed value we cannot edit, a published pool definition, a stated window, and a methodology, with the value computed from delivered results across that pool rather than set per account. None of those four exists. Full credit for separating a prompt-to-look from a verdict. Extra credit for noticing that the flag on the $122.12 ad was not earned, because its 0.93% near-twin at $11.54 got the identical flag.
