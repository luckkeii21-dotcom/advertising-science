---
title: "Lesson 029 - The Results Column Has No Unit"
type: lesson
lesson: 29
date: 2026-09-17
topic: Learning & Signal
claims: [LS-081, LS-008, LS-001, LS-021, LS-022, LS-051, LS-075, LS-018, LS-065, AT-015]
tags: [advertising-science, lesson]
---

# Lesson 029 · The Results Column Has No Unit

Sort SJR Commercial by cost per result, cheapest first. Scroll past two rows that spent four cents. The best performing ad in the account costs **$0.36** and it has never produced an opt-in in its life.

## 1. The mechanism

A school prints one column on the report card and calls it Score. Some children were marked out of 10 on a maths paper. Some sat an 800-question general knowledge quiz and got 640. One was marked on how many mornings he turned up, and that is 180. The column prints 9, 640 and 180. Sort it and the quiz kid is top of the school.

Nobody lied. The column just never carried the unit. The unit lives in a second column, and you have to add it on purpose.

Meta's Results column is that column. Every ad set carries its own optimisation event, and Results prints **that ad set's own event**, whatever it happens to be. A form opt-in, a website opt-in, a page view, a message, a video view, raw reach. Ads Manager does keep the unit. It is a separate field called **Result indicator**, and it is not in the default view.

So far this is a reporting annoyance. The reason it belongs in Learning and Signal is that the column is doing two jobs at once, and only one of them is reporting.

The other job is instruction. Meta looks at whoever fired that ad set's event and goes and finds more people like them. The column is the scoreboard you read **and** the order the delivery system is following. When one account's column carries four different units, four different orders are running at the same time, and the scoreboard has no way to compare them.

The direction of the error is predictable, which is the useful part. The deeper the event sits in the funnel, the fewer people perform it and the more each one costs. Shallow events are abundant and cheap. So **sorting a mixed column by cost per result sorts by how shallow the event is**, and calls the shallowest one the winner.

## 2. The evidence

[[Learning & Signal#LS-008|LS-008]] (T3, active) is law 6 on this page: whatever hits the results column IS the targeting. Meta seeds its expansion from whoever registered for the optimised event, so unqualified people in that column mean more unqualified people delivered.

[[Attribution & Incrementality#AT-015|AT-015]] adds the reporting half: the column counts any qualifying standard event inside the attribution window, not the specific thing the ad was selling.

[[Learning & Signal#LS-021|LS-021]] (T3) states the cost direction. Under a top-of-funnel goal like clicks or video views, Meta delivers to whoever performs that cheap action, and whether those people ever buy is not part of the instruction.

[[Learning & Signal#LS-022|LS-022]] (T3) is the selection rule: take the deepest event that clears roughly 20 to 25 conversions a week, and step one event back up the funnel below that. [[Learning & Signal#LS-001|LS-001]] (T1, contested) puts the learning-phase floor at about 50 results in the week after the last significant edit.

[[Learning & Signal#LS-051|LS-051]] (T3) says define the event as the actual business outcome, because the ad does not necessarily sell what it shows. [[Learning & Signal#LS-075|LS-075]] (T3) says the destination decides what the pixel can learn, so never run paid traffic to a page whose only available event is the one you do not want.

[[Learning & Signal#LS-018|LS-018]] and [[Learning & Signal#LS-065|LS-065]] are the T1 material, and they need their scope guard read out loud. Meta documents that a diverse mix of action types builds better representations of a **user**. Meta never mentions advertiser event choice anywhere in that post, so it does not license mixing your own optimisation events.

Here is the gap. Every one of those claims assumes the column holds one thing. Not one of them describes what happens when it holds four at once. Nobody had checked whether ours does.

## 3. Our accounts

**SJR Commercial, 24 to 30 August 2026, $4,440.35 across 53 ads.** Recomputed line by line from the weekly export, grouped on Result indicator.

| What the number actually counts | Ads | Results | Spend | Per result |
|---|---|---|---|---|
| Opt-in through a Meta form | 18 | 276 | $2,157.43 | $7.8168 |
| Opt-in through the website | 18 | 440 | $1,531.07 | $3.4797 |
| Opt-in through either door | 4 | 238 | $479.84 | $2.0161 |
| A page view on the website | 1 | 659 | $239.89 | $0.3640 |
| No result at all | 12 | 0 | $32.12 | n/a |

**Four units in one column.** The column printed 1,613 numbers that week. **659 of them, 40.9%, are page views produced by a single ad.** At least 954 are opt-ins, and that floor costs $4,168.34, so **$4.3693 per counted opt-in** across the account.

Read the per-result column top to bottom: $7.82, $3.48, $2.02, $0.36. It is monotone in shallowness. That is LS-021 arriving as a table on our own book.

**The same creative under two different events, in the same week, in the same account.** An ad called `Hal w hook` ran twice:

- In ad set `NJ/SI - Halal`, optimising for the Meta form: **$11.75, 3 opt-ins**.
- In ad set `NJ/SI - Halal - SOKAL wesbite`, optimising for a website content view: **$239.89, 659 content views**. Twenty times the budget.

June carries the same pair with an opt-in count attached to it, **9 to 16 June 2026**:

- `Hal w hook` on content-view optimisation: $275.32, 669 content views, **2 opt-ins. $137.66 each.**
- `Hal w hook` on form optimisation: $69.94, **20 opt-ins. $3.497 each.**

**A factor of 39, with the ad name held constant.** State the limit every time you quote this. The same name is strong evidence of the same creative and it is not proof, and the two rows sit in different ad sets with different destinations and a four-fold budget gap, so the event and the destination move together. It is a natural pairing, not an experiment.

**The second finding is a door nobody has counted.** SJR, 9 to 16 June, $4,897.15, **783 opt-ins: 560 through Meta forms and 223 through the website.** So **28.48% of the account's opt-ins arrive through a door that a form ad set's own Results column cannot count.**

Inside that window, the `Truck buyer leads | NJ` campaign, two ad sets, $910.26:

| Ad set | Results | Real opt-ins | Website | Counted/wk | Real/wk |
|---|---|---|---|---|---|
| English Video Ads, broad | 60 | 91 | 31 | 52.50 | 79.63 |
| Spanish Video Ads, broad | 26 | 41 | 15 | 22.75 | 35.88 |
| Both | 86 | 132 | 46 | 75.25 | 115.50 |

**34.85% of that campaign's opt-ins sit outside its own Results column.** The campaign reads **$10.5844 per result** and the business bought those people at **$6.8959**. Every efficiency number in a report built off the Results column on this account is high by half.

**It does not rescue the learning position, and that distinction is the whole point.** The Spanish ad set counts 22.75 a week, which is on the floor of LS-022 and less than half of LS-001's 50. Its real rate of 35.88 is still under 50, and it does not matter anyway, because the event that clears learning is the one the ad set is optimising on. **The uncounted door changes the price you report. It does not change what the ad set is learning from.**

**ChiroWorks is the control, and it is clean.** Same week, 24 to 30 August: one indicator only, the Meta form. $479.68 total, 10 opt-ins off $391.67 across 5 ads at $39.17 each, and 45 ads holding $88.01 with no result. ChiroWorks does not have this problem. It has the other one.

**StayWell and Phoenix Truxx cannot answer the question at all.** Their weekly exports carry no Result indicator column, because the preset was built around the Opt-ins custom metric. The column is one click away in the preset, and until somebody adds it, nobody on those two accounts can tell what their own Results column is counting.

## 4. The decision rule

**Put Result indicator next to Results before you rank anything, and never compare two rows whose indicators differ. When one account's column holds more than one unit, report each unit on its own line, and price the opt-in on the count of opt-ins, never on the count of results.**

## 5. Quiz

Drop your answers in `lessons/_answers-inbox.md` (just "L029: 1) ... 2) ...").

**Q1.** SJR's 24 to 30 August Results column printed 1,613 numbers. Say how many of them are opt-ins and how many are not, give the cost per counted opt-in for the account on that basis, and say why that figure is a floor rather than an exact number.

**Q2.** ⭐ A client sends you the SJR ad list sorted by cost per result and asks why you are not moving the whole budget behind the $0.36 ad. Answer him in two sentences, name the one column you would add to his screenshot, and quote the number from this lesson that settles it.

**Q3.** The two `Hal w hook` rows in June read $3.50 and $137.66 per opt-in. Name the one thing that pair does establish, the one thing it cannot establish, and describe the cheapest change that would turn it into a real test on SJR.

**Q4.** 28.48% of SJR's June opt-ins came through the website while the form ad sets counted only the form. Say what that changes and what it leaves untouched, and use the Spanish ad set's two weekly rates to show it.

**Q5.** ⭐ You inherit an account on Monday. Three ad sets, the Results column says Leads on all three, cost per result $4, $11 and $26. The client wants the $26 one killed. Name what you check before you touch anything, what would make you kill it, and what would make you keep it and say so to his face.

> [!note]- Answer key
> **Q1.** Opt-ins are the three lead indicators: 276 + 440 + 238 = **954**. Not opt-ins: **659 page views**, 40.9% of the column. Spend behind the 954 is $2,157.43 + $1,531.07 + $479.84 = $4,168.34, so **$4.3693 per counted opt-in**. It is a floor because an ad optimising on the Meta form prints only its form opt-ins, so any website opt-ins the same ad also produced are missing from its own row. June measured exactly that gap at 28.48% of the account.
>
> **Q2.** The $0.36 buys a **page view on the website**, not an opt-in, so it is not in the same unit as the rows it is being ranked against. Add **Result indicator** beside Results and the ranking dissolves. The number that settles it is June's reading of the same ad under the same optimisation event: **$275.32 bought 669 content views and 2 opt-ins, which is $137.66 per opt-in**, making it the most expensive opt-in in the account rather than the cheapest result.
>
> **Q3.** It **does** establish that on our own book, with the ad name held constant, changing the optimisation event moved cost per opt-in by a factor of 39. It **cannot** establish that the creative was identical, and it cannot separate the optimisation event from the destination, because one ran to a Meta form and the other to a website at four times the budget. The cheapest real test: **hold the destination fixed on the SOKAL website and run two ad sets that differ only in the optimisation event**, content view against website lead, same creative, same total budget, same window, and read both on opt-ins. That is runnable on SJR this week with no new tooling. Credit for noticing you cannot optimise for a Meta form on a website destination, which is why the destination has to be the thing held constant.
>
> **Q4.** It changes **the price we report**. The campaign reads $10.5844 per result and the business actually bought those people at $6.8959, so any efficiency figure taken off the Results column on this account is roughly half again too high. It leaves **the learning position untouched**, because the ad set trains on its own optimisation event and not on the sum of both doors. The Spanish ad set shows it: **22.75 counted a week against 35.88 real**, and both sit under LS-001's 50, so correcting the count does not move it out of permanent learning. Full marks need that separation stated, not just the two numbers.
>
> **Q5.** **Check Result indicator on all three first**, before anything else. "Leads" in the Results header is the objective, and the indicator is the unit. If the $4 ad set is running on a page view or a landing-page view while the $26 one is running on a Meta form, the ranking is comparing three different exams and the $26 row may be the only one selling anything. If all three genuinely carry the same indicator, then check the counted-versus-actual door split before killing, because a form ad set with website opt-ins is priced high by exactly the SJR error. **Kill it** if the indicators match, the door split is accounted for, and it is still six times the account's own cost per opt-in with a real downstream rate behind the comparison. **Keep it** if it is the only ad set clearing the learning floor at LS-001, or if it is the only one whose event is the actual business outcome under LS-051. Credit for refusing to act on Monday, and extra credit for naming the pruning entry trigger in law 12a: below 10 ads in one campaign, cleanup is not the best move available.

---

**Previously on this topic:** lesson 005, [[2026-08-22 Lesson 005 - The Learning Phase Is a Price Tag]], lesson 010, [[2026-08-28 Lesson 010 - What It Learns From When It Cannot Learn From Leads]], and lesson 015, [[2026-09-03 Lesson 015 - A Question Is Not a Gate]]. Directly upstream: lesson 003, [[2026-08-19 Lesson 003 - The Ad's Own Row Is Not the Verdict]], and lesson 022, [[2026-09-10 Lesson 022 - An Empty Row Has Two Causes]], which asked what an empty Results cell means. This one asks what a full one means.
