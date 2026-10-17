---
title: "Lesson 052 - The Ad Has No Number of Its Own"
type: lesson
lesson: 52
date: 2026-10-16
topic: Auction Mechanics & Bidding
claims: [AU-099, AT-127, AT-107, AT-087, SC-172, SC-168, AU-090, SC-044]
video: video/2026-10-16-lesson-052.mp4
tags: [advertising-science, lesson, auction-mechanics, attribution, decision-unit]
---

# Lesson 052 · The Ad Has No Number of Its Own

🎬 **Lesson video (3m 13s, silent, watch anywhere):** [[video/2026-10-16-lesson-052.mp4]]

This morning's research banked a measurement nobody on this roster has produced before. Somebody took a real ad auction, took 1,200 real requests, and replayed every possible combination of the ads that came back. Then they published what they found about the value of a single ad.

The finding is that it does not have one.

You already act on the conclusion. Lesson 003 told you the ad's own row is not the verdict, and lesson 036 told you to move the decision up a level because the spend gate at [[Scaling Models#SC-044|SC-044]] prices a verdict and most rows cannot afford one. Both of those are arguments about noise and money. Today is different and it is stronger. Even with unlimited spend and zero noise, the number on that row still would not be a property of that ad.

## 1. The mechanism

Five-a-side football. One striker. Across a season he scores 15 goals when a particular midfielder is on the pitch with him and 4 when a different one is. Nothing about the striker changed. The pitch, the opposition and the minutes are the same. What changed is who came out with him.

Now try to settle how good the striker is. You have three kinds of evidence available, and they are the natural ones. You can watch him play alone. You can watch the full five play. You can watch the five minus him. Those feel like enough, and for a pair or a trio they nearly are.

At four and above they stop being enough, and the reason is counting. Every pair of players has a way of helping or hurting each other. So does every trio. So does every foursome. The number of those interactions grows faster than the number of lineups you measured, so you are solving for more unknowns than you have equations. There is no arithmetic that gets the striker's own contribution back out. Not because the measurement was sloppy. Because the quantity you are asking for is not in the data.

That is the shape of an ad set. The ads in it are not five independent experiments running side by side. They are a lineup, and the auction values the lineup.

## 2. The evidence

**[[Auction Mechanics & Bidding#AU-099|AU-099]], tier 2, banked this morning.** Exhaustive auction replay over 1,200 real requests in a five-action sponsored-search setting "reveals substantial coalition dependence". The contribution of any one ad depends materially on which others came back beside it. The authors then prove the counting problem above: for sets of four or more, the per-ad attribution cannot be recovered from the singleton, leave-one-out and full-set cases alone. A policy trained on that dependence returned "an observed 3.51% lift in the primary advertiser-value metric" in a randomised seven-day production test on 10% of traffic. Real auction, real traffic, shown number, which is why it is T2.

**The guards, and read them before you quote it.** The platform is not named, so this is never documentation of Meta or Google. It is a retrieval and credit-assignment result inside a sponsored-search system, and sponsored search is not Meta's feed. The optimised metric is the platform's own "primary advertiser-value metric", which is undefined and is not your cost per lead. What transfers is not a proof about our accounts. It is an existence proof: in at least one real ad auction, measured rather than argued, set composition moves per-ad value enough that per-ad value cannot be recovered.

**[[Attribution & Incrementality#AT-127|AT-127]], tier 1, also banked this morning, and it is the same mistake on a different axis.** Meta is testing Aggregated View Time in alpha, which measures total time with a brand across a week instead of each impression on its own. The finding it cites: "five seconds of attention added up over a week drove 32% more offline sales than one continuous five second view." Same seconds, spread out, 32% more. Guards are heavy and they are not optional. Meta measuring Meta, no sample size, no vertical, no geography, no control definition, and offline sales undefined. No client on our book has an offline sales instrument, so this is not testable here as published. Keep the shape, not the number: the unit was the impression because the reporting offered that unit, never because anyone checked it was the right one.

**Already on file, from our side of the glass.** [[Attribution & Incrementality#AT-107|AT-107]], T3, says a duplicated ad set never performs like its twin, so a single-pair ad-set test has an unmeasured noise floor. [[Attribution & Incrementality#AT-087|AT-087]] is T4 and proposes reading prospecting creative on the incremental column alone, which is a proposal and not a rule. And [[Scaling Models#SC-172|SC-172]], T2, is the receipt: an operator ran about 51 test ad sets, kept finding one ad on nearly all the spend with a sibling converting better on a fraction of it, turned the top one off, and reported "99% of the time it did not hold performance at all." He stopped making decisions at the ad level. Today's claim is the mechanism that would explain why the ad he switched off was carrying the ones he kept.

## 3. Our accounts

The lineups are not small. From [[Scaling Models#SC-168|SC-168]], computed on our own ad-level exports:

| Account | Window | Ads that spent | Spend | Top ad share |
|---|---|---|---|---|
| SJR Commercial | 9 to 16 Jun | 52 | $4,897.15 | 10.8% |
| ChiroWorks | 11 to 20 Sep | 22 | $624.10 | 39.7% |
| StayWell | 11 to 20 Sep | 12 | $337.49 | 63.6% |
| Phoenix Truxx | 17 to 24 Apr | 5 | $581.86 | 46.8% |

Every one of those is a set of four or more. The threshold in AU-099 is four.

Then the rows we have been reading as verdicts. Ads that spent money and returned zero opt-ins: **SJR 19 of 52, $106.89. ChiroWorks 16 of 22, $35.55. StayWell 10 of 12, $98.05. Phoenix Truxx 2 of 5, $0.93.** Those 47 zero rows have been treated as 47 small failures. On today's mechanism they are not 47 of anything. They are the parts of four lineups whose individual contributions were never separable, and at least some of them were holding up the ad beside them.

One number keeps that honest. [[Auction Mechanics & Bidding#AU-090|AU-090]] measured the overlap on our book over 10 to 20 July: at least 73.7% of everyone ChiroWorks reached was served by exactly one ad set, and at least 94.1% on SJR Commercial. So the people are not being fought over across ad sets. The lineup effect, if it is here at all, lives inside the ad set, which is exactly where AU-099 puts it.

And the honest limit, said plainly. We have not measured coalition dependence on any account we run, and we cannot, because the instrument is auction replay and we do not have access to the auction. This changes how we read a row. It does not give us a number.

## 4. The decision rule

**Judge at the level that stays whole when you act on it. The ad set gets the verdict, the ad set gets switched off, and any time you do act on a single ad, write down what else was running in that set that week, because the number you acted on belonged to all of them.**

That last clause is the new work. We have never recorded set composition beside an ad decision, so every ad we have ever killed was killed on a number whose other owners are now unrecoverable.

## 5. Quiz

1. AU-099 is tier 2. Name the two things that stop it being tier 1, and say which single sentence of it is the part that transfers to our accounts.
2. Why does the recovery problem start at four and not at two? Answer in terms of counting, not statistics.
3. StayWell's 11 to 20 September window ran 12 ads, spent $337.49, and 10 of those 12 ads returned zero opt-ins. Write the sentence you would put in the weekly report about those 10 ads. Then write the sentence you would have written last week, and name what changed.
4. You are in ChiroWorks. One ad in a six-ad set has the cheapest cost per opt-in in the account by a wide margin, and the client asks you to put the whole budget behind it and pause the other five. Give your answer, the claim IDs it rests on, and the one thing you would record before you touch anything.
5. AT-127 says the same five seconds spread across a week beat five seconds in one sitting by 32%. Name the cheapest thing on our book that this makes worth measuring, and name the reason we still cannot measure it as Meta published it.

> [!note]- Answer key
> **1.** The platform is unnamed, so it is not documentation of any platform we buy on, and the optimised metric is the platform's own undefined "advertiser-value metric" rather than a cost per result. The authors are also reporting on their own system. The transferring sentence is that exhaustive replay found the contribution of one ad depends materially on which others came back beside it, so no ad in a returned set has a standalone value. That is an existence proof about real ad auctions, and nothing more.
> **2.** Because the unknowns grow faster than the measurements. Singletons, leave-one-out and the full set give you a fixed small number of readings. Every pair, trio and foursome inside the set has its own way of helping or hurting, and from four members up there are more of those interactions than you have readings. The system is short of information, so the per-ad figure is not in the data at any sample size.
> **3.** This week: those 10 ads account for $98.05 of $337.49, which is 29.1% of the window, and the window produced 12 opt-ins in total, so nothing in it can rank an ad at all. Last week it would have read as 10 failed ads to cut. What changed is that a zero row is now a statement about a lineup rather than a verdict on a member of it, and on 12 opt-ins across 12 ads there was never enough to grade one anyway.
> **4.** No, and not because the ad is bad. Pausing the other five changes the set, and AU-099 says the cheap ad's number was produced by the set it sat in. SC-172 is the closest thing to a receipt we have: an operator did exactly this across about 51 test ad sets and reported it did not hold performance 99% of the time. SC-044 adds that at ChiroWorks' $33.52 achieved cost per opt-in a single unit needs about $100.57 before it earns any verdict at all, and most of those six ads will not have reached it. Record the set composition and each ad's spend for the window before changing anything, because after the change that information stops existing.
> **5.** Worth measuring: whether cost per opt-in differs between a week where one person saw the same total video seconds in one sitting and a week where they were spread across days. We cannot run it as Meta published it because the outcome in their figure is offline sales, no client on our book has an offline sales instrument, and we hold no column that reports how a person's view time was distributed across a week.

Answers into `_answers-inbox.md`.
