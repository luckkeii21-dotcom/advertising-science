---
title: "Lesson 028 - Counting Ad Sets Does Not Count the Overlap"
type: lesson
lesson: 28
date: 2026-09-16
topic: Auction Mechanics & Bidding
claims: [AU-090, AU-056, AU-057, AU-058, AU-070, MD-013, MD-002, MD-155, MD-053, AT-059, SC-006]
tags: [advertising-science, lesson]
---

# Lesson 028 · Counting Ad Sets Does Not Count the Overlap

🎬 **Lesson video (2m 37s, silent, watch anywhere):** [[video/2026-09-16-lesson-028.mp4]]

Someone on a call says the ad sets are competing with each other. Someone else says that is nonsense, there are thousands of advertisers in that auction already. Both of them are certain. Neither of them has ever counted the thing they are arguing about, and it takes four minutes to count.

## 1. The mechanism

Picture a canteen with four counters. At the end of the day the manager adds up the counters and gets 400 people served. The door counter says 320 people came in. The two numbers are both correct. The average person queued at 1.25 counters.

That 1.25 is the whole lesson. It tells the manager how much coordinating he actually has to do. At 1.25, three quarters of his customers walked in, picked one counter, and left. The counters are doing separate jobs and they barely touch. If the number had come back at 3.6, the same 320 people were wandering across nearly every counter, and any plan he makes for one counter is really a plan for all four at once.

Now change one thing. Keep four counters, but make all four serve chai under different signboards. The door count stays at 320 and the counter total climbs toward 1,280. Same four counters. Completely different amount of coordination. **The number of counters never moved. What moved was whether the thing separating them separates people.**

Ad sets work exactly like this, and Meta prints both halves already.

Impressions add up across ad sets. Reach does not. If one woman in Collinsville is served by three of your ad sets, each of those three counts her once in its own Reach cell, so the ad set rows sum to three while the account counted her once. Lesson 026 used this at the ad level. One level up it gives you a number nobody here had ever taken:

`sum of the ad set Reach cells  ÷  account Reach  =  how many ad sets the average reached person was inside`

Floor is 1.00, which means no person was ever in two ad sets. Ceiling is the number of ad sets you run, which means everyone was in all of them. And the account frequency decomposes the same way lesson 026 decomposed it, just at the higher level:

`account frequency  =  reach-weighted average ad set frequency  ×  ad sets per reached person`

The identity is arithmetic, so it is always true and it proves nothing about Meta. Only the **sizes** are evidence. But the size is the argument, and until this pass nobody had measured it on a single account we run.

## 2. The evidence

The trade has two loud positions on this and they contradict each other in the open.

[[Auction Mechanics & Bidding#AU-056|AU-056]] (T3, contested) is Ben Heath dismissing the price story: two ad sets chasing the same people is "not ideal", but the idea that it raises your cost because you are bidding against yourself is "a bit silly", because thousands of advertisers are already bidding for those people and your one extra ad set barely moves the clearing price.

[[Auction Mechanics & Bidding#AU-058|AU-058]] (T3, contested) is Solutions 8 arguing the other way, that your own ad sets cannibalise each other in the auction, with audience expansion named as the specific cause: you build two disjoint ad sets, expansion widens each one into the other, and the separation you designed does not survive delivery. Dated 2025-09-08, which is before the Andromeda retrieval change, on exactly the surface that change would move.

Neither side shows a single number. No CPM comparison, no reach comparison, nothing.

[[Auction Mechanics & Bidding#AU-057|AU-057]] (T3, active) is the more interesting claim and it comes from the same speaker as AU-056, in the same breath. His mechanism is about **pacing, not price**. Meta forms a per-person delivery plan with a shape to it, and he offers four or five impressions inside 24 to 48 hours as an illustration of the kind of plan Meta might form. Fragment one buyer across several ad sets and Meta loses the ability to execute that plan. This is also the stated reason underneath [[Scaling Models#SC-006|SC-006]], the rule that you raise a budget in place instead of duplicating, so anyone leaning on SC-006 is leaning on AU-057 whether they know it or not.

Hold the four-to-five figure loosely. He offers it as an example of what Meta might decide, not as a measured setting, and it must never be carried as a number.

The thing that settles this sits in a different file and neither operator mentions it. [[Meta Delivery & Andromeda#MD-013|MD-013]] (T2) says Meta's only hard targeting boundaries are **location, minimum age, language and exclusions**. Everything else is a suggestion delivery is free to ignore. That is the same claim lesson 004 was built on, and it makes a flat prediction here that nobody had tested: an ad set split along a hard boundary produces almost no overlap, and an ad set split along a suggestion produces whatever overlap delivery feels like producing. [[Meta Delivery & Andromeda#MD-002|MD-002]] (T2) says what delivery feels like producing, which is convergence onto the clusters that convert.

Two supporting pieces. [[Attribution & Incrementality#AT-059|AT-059]] (T3) already records the same sum-exceeds-the-account shape for Meta's audience segment breakdown, where it is treated as a defect. It is the same arithmetic and it is not a defect. And [[Auction Mechanics & Bidding#AU-070|AU-070]] (T3) supplies the cost that a split does carry: an audience cut too small runs into a CPM floor.

What was missing was anybody doing this on a real account. That is [[Auction Mechanics & Bidding#AU-090|AU-090]], banked today at T2 from our own raw exports.

## 3. Our accounts

Two accounts, the same eleven days, 10 to 20 July 2026, both recomputed line by line from the ad set exports on disk. On both, the ad set rows reconcile to the account total exactly on impressions and on spend, which is how we know no ad set is missing.

**ChiropracticWorks, seven ad sets, all of them in Collinsville, Illinois.**

| | |
|---|---|
| Spend | $553.26 |
| Impressions | 19,408 |
| People reached | 6,920 |
| Sum of the seven Reach cells | 8,743 |
| **Ad sets per reached person** | **1.2634** |
| Account frequency | 2.80462428 |
| Reach-weighted ad set frequency | 2.2198 |
| Check: 2.2198 × 1.2634 | 2.80462428 |

The account frequency matches Meta's own printed decimals exactly, to all eight of them.

Read the second line of that table properly. The excess is 1,823 people. Even in the worst case where nobody saw three ad sets, **at least 73.7% of everyone ChiroWorks reached in those eleven days was served by exactly one ad set.** For three quarters of the account, Meta had nothing to coordinate, so AU-057's pacing problem cannot apply to them at all.

**SJR Commercial, four ad sets, two campaigns.**

| | |
|---|---|
| Spend | $1,024.02 |
| Impressions | 50,128 |
| People reached | 29,944 |
| Sum of the four Reach cells | 31,725 |
| **Ad sets per reached person** | **1.0595** |
| Account frequency | 1.67405824 |
| Reach-weighted ad set frequency | 1.5801 |
| Check: 1.5801 × 1.0595 | 1.67405824 |

**At least 94.1% of the 29,944 people SJR reached saw exactly one ad set.** Four ad sets, and for nineteen people in twenty the account behaved as if it ran one.

Now put the two side by side, because the comparison is the finding. ChiroWorks runs 1.75 times as many ad sets as SJR. Its overlap is 4.4 times larger. **The count of ad sets does not predict the overlap, and it is not close.**

What does predict it is MD-013, sitting right there in the ad set names. SJR's four ad sets are split on **language and vehicle programme**: English vans, Spanish vans, English dump trucks, Spanish dump trucks. Language is one of Meta's four hard boundaries, so the Spanish ad sets and the English ad sets are drawing from populations that genuinely do not overlap. Six of ChiroWorks' seven ad sets are Advantage+ in the same town, separated by nothing but the creative concept in the name: DOCTOR, Chiropractic, PAIN, Upkeep, GET A CHECKUP, All Ads. Under Advantage+ Meta picks the audience. **Those are not six audiences. They are six draws from one audience, and the reach column says so.**

**One more reading, and it kills the easy excuse.** The obvious objection to 1.2634 is that ChiroWorks is tiny against its catchment, so of course the ad sets rarely collide. Test it. Metro East is roughly 700,000 people and a tight radius is roughly 300,000 to 500,000 before filters. If those seven ad sets had each drawn their people independently at random from that pool, the expected overlap factor is **1.0047 at 700,000 and 1.0110 at 300,000**. The observed excess is **24 to 56 times what chance produces**. The ad sets are not colliding by accident. Delivery is walking back to the same people, which is precisely what MD-002 says it does.

**An internal check that had to pass and did.** Lesson 026 measured SJR's ad-level factor on this identical window from a completely separate export: 1.0933 distinct ads per reached person. Ad sets must be less fragmented than ads, always. Account reach 29,944, sum of ad set reach 31,725, sum of ad reach 32,738. The ordering holds, across two files pulled at different times, which is the strongest evidence we have that both readings are real.

**Limits, stated plainly.** Eleven days is not a delivery lifetime, and an ad set launched mid-window under-reads. This measures overlap among **people actually reached**, which is not the same as overlap between the audiences you targeted, so it tells you what delivery did rather than what the settings said. And the chance baseline leans on the vault's Metro East population figure, not on anything Meta published.

**What it does not say, and this matters.** Nothing here says ChiroWorks' 1.2634 is costing money. It says the fragmentation is real, structural and 24 to 56 times chance. Whether it costs anything is AU-056 against AU-058, and that is still untested on our book. The test AU-056 itself names is cheap: same creative, same budget, one consolidated ad set against several overlapping ones, compare delivered CPM.

## 4. The decision rule

**Split an ad set only along a line that actually separates people, which means location, age floor, language or an exclusion, and after two weeks divide the sum of the ad set Reach cells by the account Reach to check whether the split you designed is the split you got.**

## 5. Quiz

Answers go in `_answers-inbox.md`. Lesson number plus your answers. Partial answers get graded.

**Q1.** An account runs nine ad sets. Sum of the nine Reach cells is 44,000. Account Reach is 40,000. How many ad sets was the average reached person inside, and what is the largest possible share of reached people who saw more than one ad set?

**Q2.** Two ad sets, same city, same budget, one targeting women 25 to 44 and one targeting women 45 to 64. A colleague says these cannot overlap because the age bands are disjoint. Using MD-013, say whether he is right, and name the one thing about how the ad sets were built that decides the answer.

**Q3.** ⭐ ChiroWorks reads 1.2634 and SJR reads 1.0595. Your client asks whether the ChiroWorks number is a problem worth fixing. Give the honest answer in two sentences, then design the cheapest test that would turn your answer into evidence. Name the metric the test reads and the one thing you must hold fixed while it runs.

**Q4.** The 1.2634 was compared against a chance baseline of 1.0047. Explain in one sentence why that comparison was necessary, and name the alternative explanation it rules out.

**Q5.** ⭐ You are handed a campaign running one broad ad set at $80 a day in Orlando, and asked to split it into four so each service gets its own budget. Using this lesson and AU-070, say what you would do and why, and name the number you would pull two weeks later to find out whether you were right.

> [!note]- Answer key
> **Q1.** 44,000 ÷ 40,000 = **1.10 ad sets per reached person**. The excess is 4,000 people. In the worst case nobody saw three or more, so **at most 4,000 of 40,000, which is 10%**, saw more than one ad set, and at least 90% saw exactly one. Full marks need the word "at most", because if some people sat in three ad sets, fewer people account for the same excess.
>
> **Q2.** He is **wrong in general and right only under one condition**. MD-013 lists Meta's hard boundaries as location, **minimum** age, language and exclusions. An age band is a suggestion at the top end, not a fence, so 25 to 44 does not stop delivery serving a 50-year-old. The deciding factor is **whether audience expansion is on**, which is AU-058's specific: with expansion on, Meta widens each ad set into the other and the disjointness you designed does not survive delivery. Credit also for naming Advantage+, which takes the choice away entirely.
>
> **Q3.** Honest answer: **we do not know, and the number alone cannot tell us.** 1.2634 proves the seven ad sets are drawing from one pool at 24 to 56 times chance, which is a fact about delivery, and it says nothing about whether that costs a rupee, because AU-056 and AU-058 disagree and neither has shown data. The test is the one AU-056 names: **run the same creative and the same total budget through one consolidated ad set for a fortnight, then through the seven split ones for a fortnight, and compare delivered CPM** and cost per opt-in. Hold **total budget fixed** across both halves, and do not touch the creative, or the comparison is worthless. Full marks for refusing to answer yes or no.
>
> **Q4.** Because a low overlap number has **two completely different causes** and the raw figure cannot separate them. Either the ad sets genuinely target different people, or they target identical people but the account is so small against the pool that random draws rarely land on the same person. The baseline rules out the second one: chance predicts 1.0047 and we observed 1.2634, so **smallness does not explain it** and the convergence is real.
>
> **Q5.** **Do not split it**, and say why in the client's words. The four services are not one of Meta's four hard boundaries, so under MD-013 you would be splitting on a suggestion and the reach column would show one audience wearing four labels, exactly as it does on ChiroWorks. AU-070 adds the cost: four cuts of one pool are four small audiences, and a small audience is bought at a higher CPM, so you pay more to reach the same people. $80 a day split four ways also lands each ad set near the learning-phase floor. **What to do instead: leave the one ad set and put the four services in as four ads**, which gives you per-service reporting without cutting the pool. **Pull at two weeks: sum of the ad set Reach cells divided by account Reach.** Credit for naming cost per opt-in as the deciding metric, and extra credit for noticing this is the same in-place-versus-duplicate rule as SC-006.

---

**Previously on this topic:** lesson 009, [[2026-08-27 Lesson 009 - The CPM Does Not Say Why]]. Directly upstream: lesson 004, [[2026-08-20 Lesson 004 - Controls Bind, Suggestions Don't]], and lesson 026, [[2026-09-14 Lesson 026 - Frequency Is Two Numbers Multiplied]], whose identity this one borrows and moves up a level.
