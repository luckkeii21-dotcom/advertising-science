---
title: "Lesson 049 - Nothing in the Account Says Which Ceiling It Is"
type: lesson
lesson: 49
date: 2026-10-13
topic: Scaling Models
claims: [SC-080, SC-081, SC-082, SC-124, SC-002, SC-112, SC-091, MD-155, MD-051, SC-114]
video: none (Tuesday)
tags: [advertising-science, lesson, scaling-models, spend-ceiling, frequency, diagnostics]
---

# Lesson 049 · Nothing in the Account Says Which Ceiling It Is

The rotation brought up Scaling Models. The topic's biggest open question is why an account stops absorbing budget, and the file holds three competing answers to it.

All three are testable. All three are tested the same way, by reading frequency. So the first real job was to find out whether frequency says anything at all on our book.

It does not. On a real ad-level export it moves across a band narrower than one point, it never crosses the threshold anyone set, and it tracks the spend column more closely than it tracks anything about saturation. Every ceiling diagnostic in the topic is therefore silent on our accounts, and the honest consequence is that when one of our accounts stalls we cannot name which ceiling we hit.

## 1. The mechanism

A clinical thermometer with a range of 36.0 to 37.0 degrees is a perfectly accurate instrument. You can calibrate it, trust it, read it to one decimal. It will never detect a fever. The fault is not accuracy. The fault is that the thing it measures and the thing you want to know do not overlap inside the range it can see.

Frequency is impressions divided by reach. It rises for two unrelated reasons, and the arithmetic cannot separate them inside one number.

It rises when the pool is exhausted: the system has run out of new people worth showing the ad to, so the next dollar buys a second and third impression against someone already reached. That is the fever. It is what every ceiling claim is listening for.

It also rises when the ad simply got more money in the same window. More spend buys more impressions, and reach grows more slowly than impressions do once an ad has been running a while, so the heavier-funded ad shows a higher frequency than the lighter-funded one for no reason except its budget. That is not a fever. That is the thermometer reading the room.

Across one short window on one small account, the second effect is the larger one. The number still moves. It moves for the wrong reason, and nothing in the column tells you which reason you are looking at.

## 2. The evidence

**Three ceiling mechanisms, and they disagree about what the extra dollar buys.**

**[[Scaling Models#SC-080|SC-080]], tier 3, is the behavioural definition.** Push budget up until every incremental dollar both raises cost per result and lowers result volume. Both conditions, not one, and the two-condition test is the load-bearing part: cost per result rising on its own can be auction pressure or seasonality, while a simultaneous volume drop says the pool itself is exhausted. Then pull back to that level and freeze the ad set. Asserted from roughly $1M a month of agency spend with nothing shown. The same claim carries a second, economic definition: the ceiling is the daily spend at which efficiency crosses the business's own profit floor, found by stepping up and recording the decay. The two definitions do not have to agree, and an account with a low profit floor can buy well past the economic ceiling and still be nowhere near the exhaustion one.

**[[Scaling Models#SC-081|SC-081]], tier 4, says the ceiling is a credit limit.** A bottom-funnel account harvests demand created elsewhere by organic, email, search and word of mouth, and it saturates when there is no more credit left to take. The exits are both outside the ad account: add genuinely upper-funnel creative so the account manufactures demand, or raise what you can afford to pay by fixing the back end. Reasoning, no data.

**[[Scaling Models#SC-124|SC-124]], tier 4, says the ceiling is a delivery decision.** Raising budget does not push the same product-aware creative outward to cold people. The system re-serves the warm pool harder and frequency climbs. The claim's own entry in the file flags the gap in plain terms: this is a claim about frequency and CPM and it presents neither.

**They are not a menu. Two of them are a live contradiction.** [[Scaling Models#SC-002|SC-002]] is contested on exactly this point. The lag position says a post-raise dip is new, colder, slower-converting people maturing, so wait. The ceiling position says the wait is wasted because the money never reached anyone new. One says hold, the other says the holding is the mistake, and patience cannot settle it. The file names the test that would: pull the frequency trend and the audience-segment breakdown before and after a raise on the same account.

**[[Scaling Models#SC-082|SC-082]], tier 4, is the instrument built on top of all this, and it is the one worth knowing because it inverts the normal instinct.** It reads three signals together. An ad with lower frequency, lower CPM and a worse reported result is opening the funnel rather than harvesting it, and adding that ad on purpose is what lets the efficient ads take more budget. The rule inverts for pruning: the ad with the highest CPM, the highest frequency and a merely good-enough result is the least incremental thing in the account, and killing it frees budget for everything else.

Notice what SC-082 assumes. The three signals have to co-move. "Low, low, worse" has to describe one ad and "high, high, fine" has to describe another. If frequency and CPM are unrelated in your account, or move opposite ways, the triple read returns nothing: every ad has one half of each profile and the diagnostic cannot point at anything.

**And our own book already said the threshold would never fire.** [[Meta Delivery & Andromeda#MD-051|MD-051]], tier 3, puts cold ad-level frequency almost never above 2. [[Meta Delivery & Andromeda#MD-155|MD-155]], tier 2, measured it here on 14 September: across ChiroWorks and SJR Commercial, 56 of 60 live ads sat at or below 2, the highest 2.857. Lesson 048 drew the right conclusion from that and it is worth repeating. An instrument that fires on 4 of 60 ads is a rarity detector, not a fatigue detector.

## 3. Our accounts

**The measurement.** StayWell, ad-level export `Cpraise---StayWell-Chiropractic-Ads-22-Sep-2026-1-Oct-2026.csv`, 22 September to 1 October 2026, 10 days, 25 ad rows. Account spend $689.56, 39 opt-ins at $17.68 each, 16,494 impressions, blended CPM $41.81. Twelve rows carry $10 or more and hold $672.28, which is 97.5% of the spend, so that funded set is the account.

**Frequency has almost no range, and it never approaches the threshold.** The twelve funded rows run from **1.152 to 1.769**. The span is **0.617**, the median is 1.475, and the spend-weighted average is **1.531**. **Twelve of twelve sit at or below 2.0.** CR-177's 2.0 line and MD-051's audit both read this account as clean, and they would read it as clean through any raise a $69-a-day account could survive.

**The two signals SC-082 needs to move together move opposite ways here.** Pearson correlation of frequency against CPM across the funded twelve is **-0.384**. Against spend it is **+0.413**, and against log spend **+0.560**. So on this account frequency is better explained by how much money an ad got than by anything about its audience, and the ad with the higher frequency tends to have the lower CPM, which is the reverse of the profile.

**The named rows make it concrete.** The highest-frequency ad in the account is `Neck pain Ad_01` at **1.769**. By SC-082's pruning rule it is the bottom-funnel candidate, the one to kill. Its CPM is **$31.41**, the second lowest in the funded set, and its cost per opt-in is **$7.51 on 5 opt-ins**, the best figure on the account. The highest-CPM ad is `Old UGC Winning | Copy` at **$78.91**, and its frequency is **1.152**, the lowest in the set. **No ad in this account carries the prune profile. No ad carries the ceiling-breaker profile either.** The triple read does not resolve, in either direction, across 97.5% of the spend.

**One row pair kills the idea that the profile belongs to the creative.** `Cortisone wears off faster than ever | Ad 03` appears twice under the same name in the same ad set, one copy paused and one live. The funded copy: **$154.92, frequency 1.610, CPM $52.93, 8 opt-ins.** The other: **$35.81, frequency 1.218, CPM $34.30, 1 opt-in.** Same creative, same ad set, same ten days. The frequency gap is 0.392, which is 64% of the entire account's frequency range, and the visible difference between the two rows is how much money each took. `PRP and Stem Cell Therapy | Ad 02` does the same thing: 1.587 on $24.97 against 1.195 on $10.84. **An ad's frequency in a short window is partly a restatement of its spend, so reading it as a property of the creative is reading the budget column twice.**

**The same account, five weeks earlier, through MD-155.** 17 to 23 August, 7 days, 12 live ads: parent frequency **1.965362**, spend-weighted ad-level frequency **1.3869**, and 1.4170 distinct ads seen per reached person. Set beside today's 1.531, that is two points on a series and the windows differ, 7 days against 10, so it is directional and nothing more. What it does establish is that this account has now been read twice, five weeks apart, and has never produced an ad-level frequency near 2.

**And the one account where an ad genuinely did collapse says the same thing.** ChiroWorks `Before/After Ad_05` went $11.54 to $27.72 to $49.76 per opt-in on near-flat spend, a 4.31x decline against its own start. Account frequency through that collapse: **1.60x in the 30 September week, 1.70x in the 2 October week.** Frequency rises as you move up the account structure, so the ad's own figure cannot have been higher than the account's. The fatigue instrument sat silent through a 4.31x collapse, and SC-124's signature, frequency climbing as the ceiling arrives, was absent from the one real decline on our book.

**So here is the finding, and it is a negative one.** We cannot tell which ceiling our accounts hit, because the three mechanisms are distinguished only by frequency and audience-segment behaviour, and frequency on our book has no usable range. What we can rule out is SC-124's warm-pool mechanism: it predicts frequency climbing, and ours does not climb, not in two StayWell windows and not through a real ChiroWorks collapse. That leaves the economic ceiling in SC-080, the creative chain in [[Scaling Models#SC-112|SC-112]] where each successive winner lifts the level, and [[Scaling Models#SC-091|SC-091]]'s harder answer, that in-account changes are worth 2% to 20% and a bigger gap than that lives in the offer and the creative.

**The limits, stated plainly, because this is twelve rows.** Twelve data points produce weak correlations; -0.384 and +0.560 are suggestive and neither is decisive. It is one account, one ten-day window, and a small one at $68.96 a day. No raise happened inside the window, so this is not the before-and-after test SC-002 asks for. And the audience-segment breakdown, the other half of that test, has never been pulled on any account we run. **That pull is still the cheapest unanswered question in this topic, and the file has been asking for it since 21 August.**

## 4. The decision rule

**Before using a ceiling diagnostic, measure the range of the signal it reads in your own account. If frequency sits in a band under one point and never crosses 2, no frequency-based ceiling claim can fire there, so stop looking for a budget answer and go to the next creative or to the business economics.**

Two consequences worth holding. A frequency figure in a short window is partly a spend figure, so never compare the frequency of a heavily funded ad to a lightly funded one and call the gap fatigue. And a stall on an account at this size is almost never a ceiling in the SC-080 sense, because a $69-a-day account has not exhausted a catchment in the hundreds of thousands. It is the next winning ad that has not been built yet.

## 5. Quiz

Drop your answers in `_answers-inbox.md`.

**1.** Name the three ceiling mechanisms in this lesson, in one sentence each, and say which two of them are a live contradiction rather than two options. Then name the single measurement that would separate them.

**2.** Frequency is impressions divided by reach. Give the two separate reasons it can rise, say which one every ceiling claim is listening for, and explain why the number cannot tell you which one you are looking at.

**3.** `Cortisone wears off faster than ever | Ad 03` ran as two copies in the same ad set over the same ten days and read frequency 1.610 on $154.92 and 1.218 on $35.81. Say what that pair proves and what it does not prove.

**4. Scenario.** A ChiroWorks client call. The clinic wants to go from about $69 a day to $200 a day and asks whether the account can absorb it. You pull the last ten days: spend-weighted ad-level frequency 1.53, no ad above 1.77, blended CPM $41.81, cost per opt-in $17.68, and the top ad holds 28% of spend. Say what you can and cannot conclude about a ceiling from those numbers, what you would actually do about the raise, and what you would put in writing to the client about the risk. Name the one thing you would pull before the raise so the account can answer this question next time.

**5. Scenario.** SJR Commercial stalls. Spend has been flat for three weeks, cost per opt-in is drifting up, and someone proposes SC-082's pruning move: find the highest-CPM, highest-frequency ad with a merely acceptable result and kill it to free budget. From MD-155 the account read 8 live ads, parent frequency 1.674, spend-weighted ad frequency 1.5312, 1.09 distinct ads per reached person, and one ad holding $625.12 of $1,024.02. Say whether the pruning move is available on this account and why, say what the 1.09 figure tells you that the frequency figure does not, and name the move you would make instead.

> [!note]- Answer key
>
> **1.** **SC-080, exhaustion:** the pool runs out, so the next dollar raises cost per result and lowers volume at the same time. **SC-081, credit limit:** the account is harvesting demand created elsewhere and saturates when there is no more credit to take. **SC-124, delivery decision:** added budget never reaches cold people at all, it re-serves the warm pool harder and frequency climbs. **The live contradiction is SC-124 against SC-002's lag position**, recorded as contested in the file: one says the post-raise dip is new colder people maturing so wait, the other says the money never left the warm pool so the wait is wasted. **The separating measurement is the audience-segment breakdown, new against engaged against existing, plus the frequency trend, taken before and after a raise on the same account.** Credit for noting SC-081 and SC-124 share the same exit, upper-funnel creative, so they do not have to be separated before you can act.
>
> **2.** It rises when **the reachable pool is exhausted**, so extra impressions land on people already reached. It also rises when **the ad simply got more budget in the same window**, because impressions grow faster than reach does. **Every ceiling claim is listening for the first one.** The number cannot separate them because it is a single ratio with no term in it for why the denominator stopped growing, and on our own book the second effect is the larger one: frequency correlates +0.560 with log spend and -0.384 with CPM across the funded twelve. Credit for adding MD-155's second factor, that above ad level the parent figure also contains distinct ads seen per person, which is creative breadth rather than fatigue.
>
> **3.** It proves that **a short-window frequency figure is partly a restatement of spend**, because the creative, the ad set, the audience and the ten days were all identical and the money differed, yet the frequency gap was 0.392, which is 64% of the whole account's frequency range. So frequency is not a stable property of a creative and the SC-082 profile cannot be attributed to the ad. **It does not prove anything about the saturation mechanism**, because no raise happened and there is no cold-versus-warm breakdown behind either row. It also does not prove the two copies had identical delivery conditions beyond name and ad set; they are two separate ad objects, and the export shows neither start date nor bid setting. Credit for flagging that `PRP and Stem Cell Therapy | Ad 02` repeats the pattern at 1.587 on $24.97 against 1.195 on $10.84, so it is two instances and not one coincidence.
>
> **4.** **You can conclude that SC-124's warm-pool ceiling is not present**, because its signature is frequency climbing and nothing on this account is near 2, and you can conclude the account is nowhere near SC-080's exhaustion ceiling, because $69 a day against a catchment in the hundreds of thousands has not run out of people. **You cannot conclude the raise will hold**, because the exhaustion ceiling is not the only one: SC-080's economic definition fires when efficiency crosses the clinic's own profit floor, and none of those five numbers is the profit floor. **What you do: step it, do not jump it.** A 3x jump in one move breaks delivery and, worse, destroys the information, because the level at which efficiency crosses the floor never gets located. Step up and record cost per opt-in at each level. **What you put in writing: the cost per opt-in you expect at $200 a day and the number at which you would stop**, stated before the raise, so a rise afterwards is a measurement rather than an argument. **What you pull first is the audience-segment breakdown**, new against engaged against existing, because without a before reading the after reading answers nothing. Credit for naming SC-091, that if the account is off by 3x the fix is not in the ad account at all.
>
> **5.** **The pruning move is not available.** It needs one ad carrying the highest CPM and the highest frequency together, and on this account 0 of 8 ads sat above frequency 2 and the spend-weighted figure was 1.5312, so there is no high-frequency candidate to find. Nothing is being over-served. **The 1.09 figure is the one that names the real problem.** It says each reached person saw essentially one of our eight creatives, so eight ads behaved as one, and the cause recorded in MD-155 is concentration: `UGC Inspirational` took $625.12 of $1,024.02, which is 61%. **Frequency says nobody is seeing an ad too often. The 1.09 says almost nobody is seeing more than one of them.** Those are different failures and only the second one is happening. **The move: spread the money, not cut an ad.** Put spend floors under the other creatives so distinct ads per person can rise above 1, and build the next winner, since SC-112 says the ceiling is lifted by the next ad and not by reallocating around the current one. Credit for refusing to kill the $625.12 ad: SC-085 is contested on exactly that question, and the file's own caution is that the cycle of killing the top ad and launching a replacement is the most common reason accounts stop scaling.
