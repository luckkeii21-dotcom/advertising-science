---
title: "Lesson 054 - Yesterday Holds Two People"
type: lesson
lesson: 54
date: 2026-10-18
topic: Scaling Models
claims: [SC-178, SC-180, SC-179, SC-102, SC-001, SC-011, SC-012]
video: none (Sunday)
tags: [advertising-science, lesson, scaling, budget-steps, variance, lookback-window]
---

# Lesson 054 · Yesterday Holds Two People

Harvest day. Yesterday's research pass banked four claims off one Nick Theriot transcript, and one of them is the first thing anybody on the roster has said about budget decisions that is not a number. It is a selector. It tells you which number to use.

It also answers a question you have been making up on the fly across five accounts.

## 1. The mechanism

Every scaling rule you have ever read has two halves and only one of them gets printed. The printed half is the step: raise 20%, cut 20%. The hidden half is the window: 20% based on *what*. Yesterday? The last week? The last month?

The window is where the decision actually lives, because the window decides how much of what you are looking at is real.

The analogy that maps. You weigh yourself every morning to see if the diet is working. Daily weight swings two kilos on water alone. So a daily reading cannot see a 300-gram real loss, however carefully you read the scale, and anyone adjusting their food every morning off that number is chasing yesterday's salt. Weigh weekly and the water averages out and the 300 grams becomes visible. The scale was never broken. The window was too short for the signal.

Advertising has the same structure, with one extra fact that makes it computable. Opt-ins arrive as countable events. When events land independently at some average rate, the spread around that average is the square root of the count. That is not a rule of thumb. It falls out of the arithmetic.

So the noise in a day's reading, as a percentage, is one over the square root of the day's events.

Ten a day is 32% noise. A hundred a day is 10% noise. Two a day is 71% noise.

Read that last one again. A 20% scaling step taken off a number carrying 71% noise is not a decision. It is a reaction to the dice.

## 2. The evidence

**[[Scaling Models#SC-178|SC-178]], T3, banked yesterday.** Theriot, screen-sharing a campaign at $6,000 a day: read yesterday by default, switch to a trailing 7 days "where like every day it's crazy, like huge swings up and down." On the account he was showing, the two windows disagreed and he followed yesterday. "Last 7 days is saying don't scale." He scaled.

Two things about this claim, and both matter.

It is the first **selector** on the roster. Everyone else hands you a window. He hands you the test for picking one, and the test is the account's own variance.

And his own testimony is inconsistent. He has now published three windows across three dates: yesterday and trailing-7 on 2026-10-16, and a 30-day average on 2026-08-31, which he stated as his standing rule and stated explicitly against reading day to day. The **20% step held across all three dates**. So read his protocol as a stable step with an unstable window, and never quote the window without its date.

**[[Scaling Models#SC-102|SC-102]], T3.** Delivery volatility falls as spend and conversion volume rise. The same argument from the other end: a low-volume account swinging day to day is behaving exactly as designed, and a day-level reaction there is a reaction to noise.

**[[Scaling Models#SC-001|SC-001]], T3, contested.** Charley T carries the matching precondition from a third direction. An account whose day-to-day performance is hyperbolic cannot run a trailing-7-day rule at all and should sit on a flat linear step. Three operators agree that account variance governs the window. They disagree on what to do about it.

**[[Scaling Models#SC-180|SC-180]], T3, banked yesterday.** A second window question hiding as a level question. Inside a CBO, the kill test for an ad set is whether its spend damages the **campaign-level** cost per result, and both halves are required: heavy spend *and* campaign-level damage. A bad cost per result on small spend gets left alone. With [[Scaling Models#SC-011|SC-011]], which moved the kill decision from ad up to ad set, that completes a ladder. In ABO read the ad set. In CBO read the campaign. In both, the ad level is diagnostic only. His evidence is timing and nothing else, so it is observational: the campaign improved when the expensive ad set started spending.

**[[Scaling Models#SC-179|SC-179]], T3, banked yesterday.** A campaign holds at most 200 ad sets, so the one-ad-set-per-idea structure that [[Scaling Models#SC-012|SC-012]] prescribes against the doom cycle has a hard end. His campaign sits at 191. Not binding on us, our client campaigns hold single-digit to low-double-digit ad sets, and it is here so you know the ceiling exists long before it bites.

## 3. Our accounts

Take the filed week of 30 September to 6 October, using the real-people opt-in counts, never the Results column.

| Account | Opt-ins in the week | Per day | Noise in one day | Noise in a trailing 7 |
|---|---|---|---|---|
| ChiroWorks | 17 | 2.4 | **64%** | 24% |
| StayWell | 34 | 4.9 | **45%** | 17% |
| Phoenix Truxx | 68 | 9.7 | **32%** | 12% |
| SJR Commercial | about 100 | 14.3 | **27%** | 10% |

Theriot's shown account runs $6,000 a day against a $22 target, so his yesterday holds about 273 conversions. **Noise in his one day: 6%.**

That is the finding, and it is uncomfortable.

**Not one of our four accounts reaches in a full week what his account reaches in a day.** ChiroWorks' trailing seven days carries 24% noise. His yesterday carries 6%. His default window is four times more precise than our best available one.

Run it the other way and it gets sharper. To read cost per opt-in as precisely as Theriot reads yesterday, ChiroWorks needs **111 days**. StayWell needs 55. Phoenix Truxx needs 28. SJR Commercial needs 19.

Three honest limits on those numbers. Say them out loud whenever you quote them.

They are **floors**, not estimates. They assume the only thing moving is the count. Spend moves too, and the denominator carries its own variance, so the true noise on cost per opt-in is higher than every figure in that table.

They assume the underlying rate is **stable**. If the offer or the creative changed mid-window, the longer window buys precision on a number that no longer describes the account. That is the real price of the long window, and it is why 111 days reads as a verdict on ChiroWorks rather than an instruction to it.

And those opt-in counts are one filed week, not a tracked series. ChiroWorks has since gone to zero: every ad on it was paused 14 October.

**What this says about our own practice.** Every time anybody opened a client account and formed a view about an ad set from today or yesterday, that view rested on a number carrying between 27% and 64% noise. None of those reads was careless. All of them were unreadable.

**The cheapest upgrade on the board is paper and risks no spend.** Take one account, log what yesterday would have decided and what trailing-7 would have decided, every day for 30 days, and count the disagreements. That turns SC-178 from a practitioner claim into a T2 measured on our own numbers. SJR Commercial is the account to run it on: highest volume, longest history, and the day-level export is already pulled for the Sunday test.

## 4. The decision rule

**Pick the budget window by counting the events it will hold, not by preference. Take the shortest window that holds about 100 conversions, because that is where a 20% step stops being smaller than the noise. On our book that is weekly at best, and on ChiroWorks and StayWell it is monthly.**

Four riders.

The step and the window are separate decisions. The 20% step survived three of Theriot's dates. The window did not. Keep them apart.

A longer window is not free. It buys precision and spends freshness, so it is the wrong trade on an account that just changed its offer.

Inside a CBO the question is not only how long, it is how high. Read the campaign, not the ad set.

And when an account is genuinely too thin for any window, the answer is not a cleverer reading. It is more conversion volume per optimisation unit, which is a structure decision rather than a budget one.

## 5. Quiz

Drop your answers in `_answers-inbox.md`. Lesson number plus answers is enough.

**1.** An operator publishes "scale 20% off yesterday." Which half of that instruction do you have to check against your own account before using it, and why is the other half safer to borrow?

**2.** Why does the noise in a daily reading go as one over the square root of the count, rather than as one over the count?

**3.** StayWell runs 34 opt-ins in a week. You open a single day, see cost per opt-in up 30% against the day before, and want to cut the budget 20%. Work out whether that 30% move is readable, state the number you used, and say what you would do instead.

**4.** Phoenix Truxx and ChiroWorks both get called "volatile accounts" in a team message. Using SC-178's selector, explain why that word is doing no work, and name the one number that replaces it for each account.

**5.** An ad set inside a CBO is top of the campaign in spend and reads a cost per opt-in 60% worse than the campaign average. Someone wants it off. What two things do you check before agreeing, which claim governs it, and what is the weakest part of the evidence behind that claim?

> [!note]- Answer key
>
> **1.** The window. "Yesterday" is readable only on an account whose yesterday holds enough events, and the same operator has published three different windows across three dates while his 20% step held across all of them. The step is the stable half and travels. The window is a property of your account's variance and has to be re-derived per account.
>
> **2.** Because independent events accumulate variance in proportion to the count, so the spread around the mean grows as the square root of the count while the mean grows as the count. The ratio of the two is one over the square root. Practically: quadrupling daily volume halves your percentage noise, it does not quarter it.
>
> **3.** 34 a week is 4.9 a day, so one day carries about 45% noise on the count alone, and more once spend variance is added. A 30% move sits well inside that, so it is unreadable and no action follows from it. Read the trailing seven days instead, where noise is about 17%, and accept that even that window needs roughly 55 days to reach the precision a high-volume account gets from one.
>
> **4.** "Volatile" labels a property both accounts have by construction, so it separates nothing. The number that replaces it is events per candidate window: ChiroWorks 2.4 a day and 17 a week, Phoenix Truxx 9.7 a day and 68 a week. Phoenix can be read weekly. ChiroWorks cannot be read usefully at either and needs a month.
>
> **5.** Check whether it is actually taking heavy spend, and check whether the **campaign-level** cost per result is damaged. Both halves are required by [[Scaling Models#SC-180|SC-180]], and a bad cost per result on small spend is left alone. The weak part: the evidence is timing only, observational, that the campaign improved when the expensive ad set started spending. Nobody has isolated it. It is T3, so acting on it is a named bet.
