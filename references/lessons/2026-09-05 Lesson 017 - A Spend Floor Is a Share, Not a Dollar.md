---
title: "Lesson 017 - A Spend Floor Is a Share, Not a Dollar"
type: lesson
lesson: 17
date: 2026-09-05
topic: Scaling Models
claims: [SC-154, SC-133, SC-058, SC-059, MD-137]
tags: [advertising-science, lesson, scaling, cbo]
---

# Lesson 017 - A Spend Floor Is a Share, Not a Dollar

🎬 **Video:** [[video/2026-09-05-lesson-017.mp4|Watch the 2-minute version]]

## 1. The mechanism

A CBO hands one budget to the campaign and lets Meta decide which ad sets get it. Meta routes to whatever it predicts will hit the optimisation event cheapest. New creative has no history, so it loses that prediction and gets close to nothing. You have watched this happen on SJR twice.

The fix everyone reaches for is a minimum spend floor on the ad set. Set $5 a day and the ad set cannot be starved below $5 a day. Simple.

Here is the part nobody states. **A floor is written in dollars and it spends as a share.** The number that decides what happens to your campaign is not the floor. It is the floor multiplied by the number of live ad sets, divided by the campaign budget. Call it the **pinned share**: the fraction of the budget Meta is no longer allowed to move.

Think about reserving a table in a restaurant. Holding one table for a regular costs the owner nothing in a 60-table room. Hold one table in a 4-table room and you have given away a quarter of the restaurant. The reservation is the same size both times. The room is not.

At 0.5% pinned you nudged. At 40% pinned you are running an ABO with worse tooling, and you are still carrying CBO's concentration risk while you do it.

## 2. The evidence

Three positions on this, and they disagree.

- **Our own build rule**, the vault note `CBO Ad Set Spend Limits Throttle Optimization`, written 10 June. Never set a floor or a cap inside a CBO. Its stated reason: a minimum props up a loser. No data behind it.
- **SC-133, T3, contested.** Blue Sense reports CBO-with-floors losing to plain ABO and says outright he cannot explain the mechanism. No account named, no figures shown.
- **SC-154, T3, active.** Nick Theriot runs that exact construction for 365 days. One CBO, 180 ad sets, a $25/day floor on each, scaled from about $100/day to $5,000/day. $1.3 million spent, roughly 26,000 purchases, $50 average cost per purchase. Every figure he states recomputes.

Read the tiers before you read the content. Nothing here is T1 or T2. One flat rule with nothing under it, and two operators asserting opposite things, neither of whom ran the comparison. That is a question you are allowed to test, not a law you have to obey.

**Two arithmetic problems sit inside the strongest claim, and both are in our own wording.**

Our codex says Theriot scales the floor "proportionally" with budget. His own two numbers are $25 on $5,000 and $5 on $100. That is **0.5% and 5%. Ten times apart.** He raises the share by a factor of ten at small budgets and never mentions it. SC-133 and SC-154 both record it as proportional. Both are wrong.

Second, 180 ad sets at $25 each is **$4,500 against a $5,000 budget, which is 90% pinned**. That would leave Meta $500 to spread across 180 ad sets. For the floor to stay under 20% of budget, at most **40** of those 180 can be live. The claim's own guards admit the live count is unknown. So the 0.5% describes one ad set and never the campaign, and the headline "180 ad sets" and the "$25 floor" only hold together if most of the 180 are paused.

## 3. Our accounts

**SJR, dump CBO, 19 July to 17 August.** Budget $40/day, actual spend $31.93/day, 106 opt-ins at $9.04 each. Three new English dump statics were starved to **$4.03 combined across the whole 30 days**. That is 13 cents a day between the three of them, 0.34% of the campaign budget. At the campaign's own cost those three ads bought **0.45 of one opt-in in a month**. At that rate they need 67 days to buy a single one. They had been starved once already, to $0.58 combined in the week of 29 June.

**ChiroWorks, 21 July.** We consolidated two testing campaigns into one CBO at $66/day. CBO routed the money to the cheapest form fill and starved the chiropractic ad set to **$1.28/day, which is 1.94% of the campaign**. That ad set held the best cost per opt-in in the account at $32.73. At $1.28 a day it needs 26 days to buy one.

**Now price the fix honestly, because this is where the science stops being borrowed.** Theriot's $25 floor against his $50 cost per purchase buys half a purchase per day. To buy half an opt-in a day at SJR's $9.04, the floor has to be **$4.52. On a $40/day campaign that is 11.3% of the budget, 22 times his 0.5%.** Protect all three new ads that way and you have pinned **34%** of the campaign. At ChiroWorks, funding the chiro ad set to one opt-in a week costs $4.68/day, **7.1%** of the campaign, 3.7 times what it actually received.

That is the finding. The floor is not more expensive at our budgets in dollars. It is roughly **twenty times more expensive as a share**, because a floor has to clear the price of one opt-in before it produces anything readable, and that price does not shrink when the budget does. Theriot's 0.5% is affordable because his campaign is 125 times bigger than ours, not because 0.5% is the right number.

Lesson 016 established that a row funded below the price of one opt-in is not a result. This is the structure that does the underfunding, and the only control anyone has published for it does not scale down to a $40/day campaign.

## 4. The decision rule

**Before you set any ad-set floor, compute floor times live ad sets divided by campaign budget. Under 5% it is a nudge and you keep the CBO. Over 20% you are running an ABO badly, so run the ABO on purpose. And never set a floor below the price of one opt-in inside your test window, because a floor that cannot buy a result only buys a slower zero.**

For SJR that settles a standing instruction with arithmetic instead of a hunch. Never launch a refresh into the dump CBO. A $40/day campaign cannot carry three protected test ad sets and still be a CBO.

## 5. Quiz

Drop your answers in `_answers-inbox.md`. Partial answers are fine and still get graded.

**Q1.** Our codex records Theriot as scaling his floor proportionally with budget. Give his two stated floor-and-budget pairs, convert both to a percentage of campaign budget, and say by what factor the description is wrong.

**Q2 (application).** Phoenix Truxx runs a CBO at $60/day and the account buys an opt-in for $12. You want to protect two new ad sets so each can buy one opt-in a week. Compute the floor per ad set, compute the pinned share, and decide whether you set the floors or move to ABO. Show the arithmetic.

**Q3.** SC-154 states 180 ad sets, a $25/day floor and a $5,000/day budget. Explain why those three numbers cannot all describe a live campaign, and name the one figure the claim would need in order to become checkable.

**Q4 (application, and this is the guard).** A buyer proposes a $2/day floor on every ad set in the SJR dump CBO to stop the starvation. The campaign is $40/day, an opt-in costs $9.04, and there are 8 live ad sets. Compute the pinned share. Then say what $2/day actually buys one ad set over a 14-day test, and say whether the proposal fixes the problem it is aimed at.

**Q5 (judgement).** Our own build rule bans floors inside a CBO. SC-133 agrees, at T3, and is contested. SC-154 disagrees, at T3, with $1.3 million behind it. Nothing in this lesson is T1 or T2. What are we allowed to conclude today, and what is the single number we must record if we run the test on our own book?

> [!note]- Answer key
>
> **Q1.** $25 on a $5,000/day campaign is 0.5%. $5 on a $100/day campaign is 5%. The share is **ten times larger at the small budget**, so the floor is not proportional. He raises the share as the budget falls and never says he is doing it. Both SC-133 and SC-154 describe this wrongly and need correcting.
>
> **Q2.** One opt-in a week at $12 is $12 / 7 = **$1.71/day per ad set**. Two ad sets is $3.43/day. Pinned share = $3.43 / $60 = **5.7%**. That sits just over the 5% nudge line, so it is defensible and it is close to the boundary. Second check, does the floor buy anything: $1.71 x 14 days = $24, which is **2 opt-ins per ad set** in a two-week window. Thin but readable. Set the floors, read at 14 days, and do not draw a conclusion off one opt-in either way. Full credit also for arguing ABO instead on the grounds that 2 opt-ins is too thin to read, as long as the arithmetic is shown.
>
> **Q3.** 180 x $25 = **$4,500 of a $5,000 budget, 90% pinned**, which leaves $500 for Meta to allocate across 180 ad sets. A campaign in that state is not making allocation decisions at all. The three numbers only reconcile if most of the 180 ad sets are paused, and the claim's own guards say the live count is unknown. **The missing figure is the number of LIVE ad sets.** Without it, 0.5% is a fact about one ad set and tells you nothing about the campaign.
>
> **Q4.** Pinned share = 8 x $2 = **$16 of $40, which is 40%**. That is double the 20% line, so the campaign is functionally an ABO with $24/day left free. What the floor buys: $2 x 14 = $28 per ad set, which at $9.04 is **3.1 expected opt-ins** in the window. So the floor does clear the price of an opt-in and it genuinely would stop the starvation. The honest verdict is that it fixes the problem **by converting the campaign into an ABO without admitting it**. If that is the structure you want, build the ABO deliberately and split it by language, which is the standing SJR instruction. Full marks need both halves: it works, and it works by ceasing to be a CBO.
>
> **Q5.** We are allowed to conclude that **the question is unsettled and our own build note overstates its confidence.** A flat prohibition written with no data does not outrank a shown $1.3M account, and the shown account does not outrank it either, because neither operator ran the comparison. What we are not allowed to do is keep quoting our build rule as settled. The number to record if we test it is **the floor as a percentage of campaign budget**, and to do better than SC-154, the live ad set count beside it so the pinned share is recoverable. Recording the floor in dollars alone makes the result unusable by anyone at a different budget, which is exactly why the two sources cannot be compared today.

---

**Sources in the codex:** [[Scaling Models#SC-154|SC-154]] (T3), [[Scaling Models#SC-133|SC-133]] (T3, contested), [[Scaling Models#SC-058|SC-058]] (T3), [[Scaling Models#SC-059|SC-059]] (T3), [[Meta Delivery & Andromeda#MD-137|MD-137]]. Our own build rule: [[CBO Ad Set Spend Limits Throttle Optimization]].

**Account numbers from:** SJR Commercial `_HOT.md` 2026-08-19 browser read and `reports/_TIMELINE.md`; ChiroWorks `report-2026-07-24-client-attribution-audit` and `ChiroWorks Journey.md`.

**Previous lesson:** [[2026-09-04 Lesson 016 - What a Losing Ad Is Allowed to Disprove]]
