---
title: "Lesson 023 - Nothing Got Worse and the Number Did"
type: lesson
lesson: 23
date: 2026-09-11
topic: TikTok Delivery
claims: [AT-115, AT-100, TT-022, TT-021, TT-025, TT-026, MD-154]
tags: [advertising-science, lesson]
---

# Lesson 023 · Nothing Got Worse and the Number Did

🎬 **Lesson video (2m 34s, silent, watch anywhere):** [[video/2026-09-11-lesson-023.mp4]]

Every Friday you open an account and read one number off the top of the screen. Cost per opt-in. It went up. Somebody asks what broke. This lesson is about the weeks when the honest answer is that nothing broke, and about how to tell those weeks apart from the ones where something did.

## 1. The mechanism

Cost per opt-in at account level is total spend divided by total opt-ins. That is not an average of your ad sets. It is a weighted average, and the weights are how the budget happened to split that week.

Think about your drive across Delhi. Thirty kilometres of open road at 80 km/h, five kilometres of Ring Road traffic at 15 km/h. Your average speed for the trip is not 47.5 km/h, because the slow bit eats far more of your clock than it does of your distance. Now drive the same two roads next week, both exactly as fast as before, and take ten kilometres of Ring Road instead of five. Your average speed drops. Nothing on either road changed. You changed the mix.

An ad account does the same thing, and it does it every single week, because budget moves between ad sets constantly. In a CBO you are not even the one moving it. Meta is, and Meta is doing it on purpose: it equalises the marginal cost of the next result across everything the campaign can buy, which means the split you see on Friday is an output of the algorithm rather than a choice anybody made.

So when the headline number moves, it has two causes. A component actually changed, or the weights changed. They look identical in the column. That is the same shape as yesterday's lesson, where an absent placement row had two causes and the export could not separate them ([[Meta Delivery & Andromeda#MD-154|MD-154]], T1 on the format fact). Reports are full of numbers that are true and that answer a question you did not ask.

**There is a second and nastier version, where the mix moves, the component is genuinely fine, and everything downstream reads as broken.** That is [[TikTok Delivery#TT-022|TT-022]], T2 and shown on screen: a Shopify brand turned TikTok on, sessions rose 63%, and the absolute count of sessions with a cart addition **fell**. Site conversion rate dropped 54%. Every funnel metric in the business was blended across sources, so a channel holding 33% of media budget contaminated all of them. The brand read its own site as broken. Its site was fine. Turning TikTok off took conversion rate from 1.5% back to roughly 6% with no revenue drop ([[TikTok Delivery#TT-023|TT-023]], T2).

Two smaller claims from the same account are worth carrying. The top line hid the damage completely: media up 50%, net sales up 6%, and the read on the surface was merely disappointing ([[TikTok Delivery#TT-021|TT-021]], T2). And the thing that got the brand in was a cheap CPM, which predicts nothing about cost per customer because the discount gets arbitraged away at the click ([[TikTok Delivery#TT-025|TT-025]], T3).

## 2. The evidence

- **[[Attribution & Incrementality#AT-100|AT-100]]**, T1 for the mechanism, T3 for the verdict. The readable unit of analysis is whichever level holds the budget, and this comes from Meta's own breakdown-effect documentation. Meta solves pacing and placement together, and it equalises marginal cost rather than average cost. The claim carries a warning we can now do something about: the worked example in the source does not survive arithmetic, so the codex has held this mechanism for months **with no verified numeric proof of it**.
- **[[TikTok Delivery#TT-022|TT-022]]**, T2, shown. The blended rate falls when you add a source whose people do not convert, and the tell is the absolute count rather than the rate.
- **[[TikTok Delivery#TT-026|TT-026]]**, T2, shown. A related trap on the same account: a campaign optimised for view-content reported 449 clicks and 206 conversions, so cost per conversion was a cost per page view. Choosing the wrong event makes the column unreadable in a different way, and the two errors compound.
- **[[Attribution & Incrementality#AT-115|AT-115]]**, T2, banked by this lesson from our own raw exports. The numeric proof AT-100 was missing.

Read the tiers. TT-022 is a single brand, walked through on screen, and it is the strongest TikTok evidence we hold. AT-100's mechanism half is documentation. The verdict half is an operator's judgment. Our own tables below are T2 because they are computed, checkable and from raw files, and they are still three accounts.

## 3. Our accounts

**SJR Commercial, 10 to 20 July 2026, the whole account.** Four funded ad sets, recomputed from the raw campaign and ad-set exports. The placement rows sum to the account total to the cent, so this is not a slice.

| Lane | Spend | Opt-ins | Cost per opt-in | Share of spend |
|---|---|---|---|---|
| Cargo Vans program | $719.42 | 220 | **$3.27** | 70.3% |
| Dump Trucks test | $304.60 | 36 | **$8.46** | 29.7% |
| **Account** | **$1,024.02** | **256** | **$4.00** | 100% |

The account's headline number is $4.00. **No ad in the account cost $4.00.** The ad carrying 61% of spend cost $3.34. The cheapest cost $2.09. The dearest funded one cost $10.24. The $4.00 describes a budget split.

Hold both lanes at exactly the rates above and move only the money. At a 10% dump-truck share the account reads **$3.48**. At 50% it reads **$4.72**. That is a 35% swing in the number the client sees, with no ad, audience, bid or creative touched. Sanity check on the model: put the share back to its real 29.75% and it returns $4.0002 against the exported $4.0001.

**ChiropracticWorks, three consecutive reported weeks, ad-set level from the weekly-report raw exports.**

| Week | Account cost per opt-in | invisa-RED cost per opt-in | invisa-RED share of spend | Spend that returned nothing |
|---|---|---|---|---|
| 8 to 16 Aug | $41.93 | $36.25 | 80.7% | $54.08 (8.6%) |
| 17 to 23 Aug | $54.41 | $40.07 | 73.6% | $98.77 (22.7%) |
| 24 to 30 Aug | $47.97 | $45.05 | 65.7% | $62.47 (13.0%) |

Week one to week two, the ad set holding four fifths of the budget got **10.5% dearer** and the account got **29.8% dearer**. Two thirds of what the client saw came from the mix.

The middle week is the cleanest demonstration in the table. **All 8 opt-ins came from invisa-RED.** So the account bought 8 opt-ins at $40.07 each, and it also bought 8 opt-ins at $54.41 each. Both are true. The gap is $98.77 that went to two Advantage+ ad sets and returned nothing.

Week two to week three is the one to remember, because the two numbers move in **opposite directions in the same week on the same account**. invisa-RED got 12.4% dearer. The account got 11.8% cheaper. Two new Advantage+ ad sets produced 3 opt-ins on 20.4% of the budget, one of them at $25.55, which is the cheapest thing in the account.

Anyone reading only the headline saw a good week. Anyone reading only invisa-RED saw a bad week. Both were reading real numbers.

**The honest limits.** ChiroWorks is 15, 8 and 10 opt-ins. That is small enough that a single opt-in moves the account number by several dollars, and nothing here should be read as a performance verdict on any ad set. SJR's 256 is the only volume in this lesson. And a zero-result ad set is real money genuinely spent, so stripping it out gives you a diagnostic and never a truer number.

## 4. The decision rule

**A blended number moving has two causes, a component changed or the weights changed, so before you explain the move, split the spend by lane and check whether the shares moved. Explain the move only after that.**

The mechanics take about four minutes. Pull spend and results by ad set for both windows. Compute each lane's own cost per opt-in and its share of spend. If a lane's share moved more than a few points, the mix owns part of the story and you say how much. State the absolute counts alongside every rate, because the rate is what the mix contaminates and the count is not.

When a genuinely new ad set turns on, the rate you watch is not its own row. Watch whether the **absolute count** of the money event holds. That is TT-022's rule and it needs no attribution model to run.

## 5. Quiz

Five questions. Put answers in `_answers-inbox.md`, any format, partial is fine.

**Q1.** In one paragraph, explain why the SJR account's $4.00 is not a number any ad in that account produced, and name the claim that says which level is the readable one.

**Q2.** *(Applied.)* Next Friday ChiroWorks reads: account cost per opt-in $39.10, down from $47.97. invisa-RED sits at $52.00 on 58% of spend. Work out roughly what must be true about the rest of the account for both numbers to hold, then say what you write in the client report and what you do on Monday.

**Q3.** *(Applied.)* SJR's dump-truck lane costs $8.46 against the van lane's $3.27. Kartik asks whether to switch the dump-truck test off to protect the account number. Give your answer, name the two things that decision does to the headline figure, and name the one number you would need before the decision is anything more than a guess.

**Q4.** Argue the opposite. Build the strongest case that the ChiroWorks week two rise to $54.41 really was a performance problem rather than a mix effect. Then name the exact column that settles it and say which way it has to read for your own argument to survive.

**Q5.** AT-100's mechanism is T1 and the codex has carried it for months with no verified arithmetic behind it. Explain what our two tables add and what they do not, and say what would have to be true for AT-115 to deserve better than T2.

> [!note]- Answer key
>
> **Q1.** Cost per opt-in at account level is total spend over total opt-ins, so it is a weighted average of the lanes with the spend shares as weights. It lands between the lanes and matches neither. In this window the lanes were $3.27 and $8.46, so $4.00 is just the point 70.3/29.7 of the way between them in money terms. **AT-100** (T1 mechanism, T3 verdict) is the claim: the readable unit is whichever level holds the budget, and in a CBO that is the campaign. Full marks for adding that Meta is actively moving the weights, so the split is an output of delivery rather than a decision anyone made.
>
> **Q2.** If invisa-RED is at $52.00 on 58% of spend and the account is at $39.10, the rest of the account has to be much cheaper and carrying real volume. Work it with any plausible spend, say $480 total: invisa takes $278.40 and buys 5.4 opt-ins, the account buys 12.3, so the other $201.60 bought about 6.9 opt-ins at roughly $29. **So the honest reading is that the account improved because a cheaper lane grew, while the ad set carrying most of the money got worse for the third week running.** The report says both, in that order, with the absolute opt-in counts beside both rates, because a client who is told only the headline will be surprised later. Monday: find out what the cheap lane actually is, and check whether it is selling the same offer, because a cheaper opt-in on a different offer is not a like-for-like win. Half marks for spotting the divergence without the arithmetic. Zero for reporting $39.10 as an improvement and stopping.
>
> **Q3.** Switching it off does two things to the headline. It removes the drag, so the number falls toward $3.27 immediately, and it removes a test, so you learn nothing further about dump trucks. Both are real and only the first shows up in the report. The answer is that the headline figure is the wrong reason to do it either way: the test is either worth running on its own merits or it is not, and the account average is not evidence about that. **The number you need is what a dump-truck opt-in is worth relative to a cargo-van opt-in**, at booking, at show, or at sale. A dump truck is a far larger ticket, so $8.46 against $3.27 may be the better buy and the cost column cannot tell you. Credit for noting this is the column we do not have: across five accounts exactly one filed table pairs a cost per opt-in with a booking count, and there is no ad-level version anywhere. Extra credit for saying so out loud to Kartik rather than picking a side.
>
> **Q4.** The strongest opposing case: invisa-RED's own cost per opt-in rose in every one of the three weeks, $36.25 to $40.07 to $45.05, a 24.3% climb with no mix effect in it at all, because that is one ad set measured against itself. Lesson 021 decomposed exactly that rise and found CTR falling, which is creative wear and a genuine performance problem. Volume also halved, 15 opt-ins to 8. So there was a real problem in week two and the mix merely amplified it. **The column that settles the split is the share of spend by ad set.** For the opposing case to survive, invisa-RED's share has to have held roughly flat while its cost rose. It did not: it fell 80.7% to 73.6%, and the spend that moved bought nothing, which is where $14.34 of the $54.41 came from. Full marks require naming the direction and conceding that both effects were live at once, because they were.
>
> **Q5.** The tables add checkable arithmetic on real accounts for a mechanism the codex previously held only as documentation plus an operator's unverifiable example. SJR shows the weighted-average behaviour with volume, 256 opt-ins, and shows the range the headline can be pushed across without touching anything. ChiroWorks shows the two numbers diverging in opposite directions in one week. What they do not add: any evidence about what Meta's allocator is optimising, because they are consistent with the mechanism rather than a test of it, and no counterfactual was run on a live account. **For AT-115 to beat T2 you would need the shares deliberately moved on a live account with the ad sets held constant, and the predicted headline computed in advance and then compared to the exported one.** That is a cheap test and nobody has run it. Credit for noticing that the $4.0002 against $4.0001 check is a consistency check on our own arithmetic and not a prediction, because the shares were read off the same file.

---

**Related:** [[TikTok Delivery]] · [[Attribution & Incrementality]] · [[2026-09-10 Lesson 022 - An Empty Row Has Two Causes]] · [[2026-08-19 Lesson 003 - The Ad's Own Row Is Not the Verdict]] · [[2026-08-27 Lesson 009 - The CPM Does Not Say Why]] · [[2026-09-05 Lesson 017 - A Spend Floor Is a Share, Not a Dollar]] · [[SJR Commercial]] · [[ChiroWorks]]
