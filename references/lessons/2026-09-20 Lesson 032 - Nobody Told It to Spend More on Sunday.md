---
title: "Lesson 032 - Nobody Told It to Spend More on Sunday"
type: lesson
lesson: 32
date: 2026-09-20
topic: Scaling Models
claims: [SC-117, SC-118, AT-100, SC-102, SC-001]
video: none
tags: [advertising-science, lesson, scaling, pacing, day-of-week]
---

# Lesson 032 · Nobody Told It to Spend More on Sunday

There is a claim in our codex that says Meta cannot help itself. Give it a $100 daily budget and it spends $100 every day of the week, Monday the same as Sunday, because it has no choice. Everything that follows from that claim is a manual correction. Find the days that convert better, move money into them by hand.

We had never checked it on our own book. It took twenty minutes.

Meta moved the money on its own. And the days it moved money toward were not better.

## 1. The mechanism

Two ways to hand out a budget.

Give a kid ₹100 every morning for seven mornings. That is flat. Every day gets the same, whatever is happening that day.

Or hand over ₹700 on Monday and say make it last the week. Now Friday night gets more, because that is when their friends are out. Nobody instructed that. It fell out of the money being pooled and the week being uneven.

Sam Piliero says Meta is the first kind. Meta's own breakdown-effect documentation describes the second kind. The words in it are that the system is **pacing the budget across the delivery schedule** while choosing where to serve, and that it equalises **marginal** cost rather than average cost. Read plainly: it pushes money into a slot until the next dollar there would do less good than the same dollar somewhere else, then it moves.

A delivery schedule is days. So the documentation and the practitioner claim disagree, and one of them is checkable against a CSV we already have.

## 2. The evidence

- **[[Scaling Models#SC-117|SC-117]], T4, active.** "If you give Facebook a $100 daily budget, it's going to spend the same $100 every single day of the week. Right? It has no choice." One operator, no account shown, no data. The claim already carries its own instruction: pull your own day-of-week breakdown before acting on it.
- **[[Scaling Models#SC-118|SC-118]], T4, active.** The move that follows. Cut the weak days about 20%, push the money into the strong days at roughly +33%, aim for an equal conversion rate across all seven. **The 20% and the 33% are invented.** He says on the recording that the 1% weekday and 1.5% weekend conversion rates are hypothetical, then works the percentages out loud from those two made-up numbers. No account, no before, no after.
- **[[Attribution & Incrementality#AT-100|AT-100]], T1 for the mechanism.** Meta's own documentation on the breakdown effect. Pacing across the delivery schedule, equalising marginal cost. This is the strongest source in the lesson and it points the other way from SC-117.
- **[[Scaling Models#SC-102|SC-102]], T3.** Delivery volatility falls as spend and conversion volume rise. A low-volume account swinging day to day is behaving as designed, so day-level reactions there are reactions to noise.
- **[[Scaling Models#SC-001|SC-001]], T3, contested.** The step-size file. Worth holding beside SC-118, because a 33% move on a subset of days is bigger than almost every daily step any operator in that claim will defend.

## 3. Our accounts

**Phoenix Truxx, daily export, 1 July to 3 August 2026.** The final row is 3 August at $53.75 against a file averaging near $190, so it is a part-day pull and it is dropped. The clean read is **13 July to 2 August, three complete Monday-to-Sunday weeks, 21 days, $4,259.23, 469 opt-ins, $9.0815 each.**

Share of each week's spend, where flat would be 14.286%:

| Day | Wk 29 | Wk 30 | Wk 31 | Mean |
|---|---|---|---|---|
| Mon | 13.72% | 13.68% | 15.30% | **14.24%** |
| Tue | 15.17% | 15.50% | 14.24% | **14.97%** |
| Wed | 14.92% | 14.24% | 14.43% | **14.53%** |
| Thu | 13.75% | 13.56% | 12.95% | **13.42%** |
| Fri | 13.76% | 14.18% | 13.18% | **13.71%** |
| Sat | 12.42% | 13.26% | 12.66% | **12.78%** |
| Sun | 16.25% | 15.59% | 17.24% | **16.36%** |

**Sunday is the highest day in all three weeks. Saturday is the lowest in all three.** Sunday takes 28% more than Saturday. Nobody set that. There is no day-parting on the account and no weekend schedule. Add the fourth week in the file and Sunday is highest in four of four, which a coin flip produces about once in 343 tries.

So SC-117 is wrong on this account. Meta did have a choice and it took it.

**Now the half that matters more.** If Sunday is getting extra money, the next question is whether Sunday deserved it. Line the opt-ins up against the dollars and ask whether any weekday bought them at a different rate: chi-square **2.414 on 6 degrees of freedom, p = 0.88.** The opt-ins land almost exactly proportional to the spend. There is no day-of-week effect left to find.

The raw numbers still look like there is one. Saturday reads **$7.7751** per opt-in and Monday reads **$9.7821**, a 25.8% spread, and that spread is what makes an operator reach for SC-118. It is noise. Here is the same file asked the cheap way, which day was cheapest each week:

| Week | Cheapest | Dearest |
|---|---|---|
| 28 | Wed $6.50 | Sat $13.25 |
| 29 | Sat $8.42 | Sun $13.61 |
| 30 | Sun $6.65 | Thu $10.60 |
| 31 | Fri $7.24 | Tue $11.96 |

**Four weeks, four different winners, four different losers.** Saturday is the dearest day in week 28 and the cheapest in week 29. Sunday is the dearest in week 29 and the cheapest in week 30. Take the three cheapest days from one week and look them up in the next week: their average rank comes out 5.33, then 4.00, then 5.00, against 4.00 for picking at random. Last week's good day tells you nothing about next week's.

**SJR Commercial, a second truck dealership, a different five months.** 5,536 Meta-sourced opt-ins from the CRM export, 1 January to 31 May 2026, timestamps converted to Eastern so the weekday is the buyer's weekday. Sunday **40.18** opt-ins a day, Saturday **33.64**, a 19.5% spread, chi-square 18.74 on 6 df, **p = 0.0046**. Same shape as Phoenix's spend, on a sample thirty times larger, and this one is real.

**The limit on that second number, stated plainly.** The SJR file has no daily spend in it. So those arrivals cannot separate "more people opt in on Sunday" from "more money ran on Sunday". Phoenix can answer it because Phoenix has both columns. SJR cannot, and the fix is one export away.

Both accounts sell trucks to tradesmen in New Jersey. Saturday is a working day for that buyer and Sunday is not. That reading is comfortable and it is still only a reading.

## 4. The decision rule

**Before you correct a platform by hand, check whether last period's answer is still this period's answer. If the winning day changes every week, there is no day, there is only variance, and the correction spends real money on it.**

## 5. Quiz

1. SC-117 says Meta "has no choice" about how it spreads a daily budget across the week. Give the one number from the Phoenix table that contradicts it, and say what the table would have looked like if the claim were true.
2. SC-117 and SC-118 are both T4. Say what T4 means in one sentence, and say where the 20% and the 33% in SC-118 actually came from.
3. You open ChiroWorks and the last 7 days show Tuesday at $41 per opt-in and Thursday at $67. Name the two checks you run before moving any budget, and say which result would make you leave the account alone.
4. Phoenix's Sunday takes 16.36% of the week and Saturday takes 12.78%, and the opt-ins still come out proportional to the dollars at p = 0.88. The client asks why you are not fixing Sunday. Answer in three sentences, and do not use the word "algorithm".
5. SJR's opt-in arrivals lean to Sunday, 40.18 a day against Saturday's 33.64, p = 0.0046 on 5,536 records. Explain why that number on its own cannot justify moving SJR's budget, and name the single export that would settle it.

Answers go in `_answers-inbox.md`. Partial answers get graded.

> [!note]- Answer key
> **1.** Sunday's 16.36% mean share against a flat 14.286%, highest in all three weeks, four of four with week 28 included. If the claim were true every row in that table would sit near 14.286%, the week-to-week wobble would be small, and the day means would be indistinguishable from each other. Saturday's 12.78% is the same evidence from the other end, and Sunday takes 28% more than Saturday.
>
> **2.** T4 is theory. An idea with no platform documentation, no shown test and no operator data behind it. The 20% and 33% are arithmetic Sam Piliero did on the recording off two conversion rates, 1% weekday and 1.5% weekend, that he states are hypothetical. They are calculations on invented inputs, so they carry no evidence at all and must be labelled that way every time they are quoted.
>
> **3.** Check one, volume: how many opt-ins sit behind each figure. At ChiroWorks volumes a single Tuesday holds a handful, and SC-102 says a low-volume account swings by design. Check two, persistence: pull the previous three or four weeks and ask whether Tuesday was cheap in those weeks too. **Leave the account alone if the cheap day moves around**, which is exactly what Phoenix did across four consecutive weeks. Moving budget onto a day chosen from one lucky week is paying for the regression back to the mean.
>
> **4.** Something like: "Sunday is already getting the biggest share of the week, about a quarter more than Saturday, and we did not set that. When we check what the money bought, every day of the week produced opt-ins at the same price, so there is no cheap day sitting there unfunded. If we shifted budget onto whichever day looked best last week, we would be paying for luck, and last week's best day has been a different day four weeks running."
>
> **5.** Because the arrival count has no denominator. More opt-ins on Sunday is equally consistent with more buyers being free on Sunday and with more money having run on Sunday, and the CRM export contains no spend. Phoenix answers it only because Phoenix has spend and opt-ins in the same file. **The export that settles it is SJR's day-level Meta spend for the same window**, which turns the count into a cost per opt-in and lets the same chi-square run. It is a five-minute pull and it is the cheapest open item this lesson creates.
>
> **Carry forward.** We have now measured the pacing claim on one account and refuted it there. What we have not measured is whether Meta's Sunday lean is deliberate scheduling or a weekly budget-balancing window that starts on Sunday. Nothing in our files separates those, and neither one changes the operating rule.
