---
title: "Lesson 046 - The Budget Stops Being an Instruction"
type: lesson
lesson: 46
date: 2026-10-09
topic: Auction Mechanics & Bidding
claims: [AU-095, AU-091, AU-005, AU-051, AU-012, AU-048, AU-049, AU-026, AU-033]
video: video/2026-10-09-lesson-046.mp4
tags: [advertising-science, lesson, auction-mechanics, cost-caps, bidding, budget-pacing]
---

# Lesson 046 · The Budget Stops Being an Instruction

🎬 **[Watch the 4-minute version](video/2026-10-09-lesson-046.mp4)** (silent, built to read without sound)

The rotation brought the auction topic up today, and it turns out the entire cost-cap cluster has never been taught. Nine claims, two of them T2, arguing with each other since February.

Most of that argument is unsettled and will stay unsettled. One piece of it is an identity, true whether or not caps work, and it changes how you read a spend column for the rest of your career. Start there.

## 1. The mechanism

You tell a broker: buy up to 100 shares of something, never above $40. You put $4,000 in the account.

The price sits at $47 all week. You buy nothing. The $4,000 sits there untouched, and nothing has gone wrong. That money was never an instruction to buy. It was permission to buy, if the price showed up.

A cost cap is that order, placed into the Meta auction. You set a cost per result goal and Meta may only enter auctions it forecasts it can win at that average price or under. On a day when nobody is available at your price, it spends almost nothing.

Now look at what that does to the budget. Everywhere else on Meta a daily budget is an instruction. Meta spends it, near enough, every day, which is why the step-size discipline exists: raise the budget too fast and you force spend into auctions you did not want, and the price climbs. Put a cap on and the budget becomes a ceiling on opportunity. You can raise it freely, because the price is now being held by something else.

AU-095 says this out loud, from the operator's own mouth: *"I can be more aggressive with raising the budget in a cost cap campaign because the budget is not like a highest value campaign where you'll force spend on all those ads. I'm just giving more room now for those ads to spend if they can, but the cost cap's going to protect me."*

His campaign carried $3,000 a day and spent the full amount on two or three days out of seven. **A day that spends $100 out of $3,000 is the cap doing its job.** Read that row as underdelivery and you will raise the cap to fix a campaign that was working.

## 2. The evidence

| Claim | Tier | What it actually carries |
|---|---|---|
| [[Auction Mechanics & Bidding#AU-095\|AU-095]] | T2 | The only shown-account cap procedure on file. Opened at $30 against a $50 to $60 account average, raised $5 every 2 to 3 days, finished at $55 against a $65 target. One account, 7 days, no holdout. |
| [[Auction Mechanics & Bidding#AU-091\|AU-091]] | T3 | The same operator's build one week earlier. Cap set at the trailing 30-day cost, $40. One ad set, 1-day click. No capped-campaign results shown at all. |
| [[Auction Mechanics & Bidding#AU-005\|AU-005]] | T2 | $200M of cost-controlled spend, 253 accounts. Min ROAS on 7-day click delivered 96.5% of target. 7-day click plus 1-day view delivered 101%. 1-day click missed target more often. |
| [[Auction Mechanics & Bidding#AU-051\|AU-051]] | T3 | A practitioner on eight- and nine-figure accounts concedes there is not enough conclusive data that caps outperform maximize conversions. |
| [[Auction Mechanics & Bidding#AU-012\|AU-012]] | T3 | Three spend floors, all above six figures: $100k total, $250k a month for bid work generally, $300k a month for caps specifically. None has data behind it. |
| [[Auction Mechanics & Bidding#AU-048\|AU-048]] | T3 | The binding prerequisite is creative velocity rather than spend. Two independent operators, no account data. |
| [[Auction Mechanics & Bidding#AU-049\|AU-049]] | T4 | A cap drains onto the conversions nearest to purchase, so a capped prospecting campaign stops being measurably prospecting. |
| [[Auction Mechanics & Bidding#AU-026\|AU-026]] | T4 | Harvest, then crash, because the cap empties the funnel that was already there. |
| [[Auction Mechanics & Bidding#AU-033\|AU-033]] | T4 | The one temporary use: seed a brand-new pixel by taking conversions off other bidders, then exit on purpose. |

Three things to learn from the shape of that table. They are worth more than any single row.

**The two T2s do not answer the question anyone is asking.** AU-005 measures whether a control delivers to its own target, across a genuinely large dataset. That is a different question from whether running a control beats not running one. AU-095 is one account for one week, and the same window also changed campaign structure and creative, so nothing in it isolates the cap. Across the whole roster, the number of controlled capped-versus-uncapped comparisons on the same account is **zero**.

**The same operator gave two different opening prices seven days apart.** On 16 September, set the cap at what the account already achieved. On 23 September, open far below the account average and ratchet up $5 at a time. He never ran one against the other. When a single source disagrees with himself inside a week, you are looking at taste.

**The budget half is the only part that generalises.** It falls straight out of the bid rule, so it holds in every account at every spend level, including the accounts where the cap itself is a bad idea.

## 3. Our accounts

The build does not fit our book, and our own exports say so twice over. Daily spend, measured from the weekly-report raw exports at [[Scaling Models#SC-168|SC-168]]:

| Account | Window | Spend per day | Monthly equivalent | Biggest single ad per day |
|---|---|---|---|---|
| SJR Commercial | 9 to 16 June | $612.14 | about $18,400 | $66.39 |
| Phoenix Truxx | 17 to 24 April | $72.73 | about $2,180 | $34.03 |
| ChiroWorks | 11 to 20 Sept | $62.41 | about $1,870 | $24.76 |
| StayWell | 11 to 20 Sept | $33.75 | about $1,010 | $21.48 |

**Test one, the account floor.** The lowest figure anyone names is $100,000 of total spend. The highest, attached specifically to caps, is $300,000 a month. Our largest account at its largest window ran about $18,400 a month equivalent, roughly 6% of that. Every version of the threshold says no.

**Test two is sharper, because it is per ad.** AU-095 admits an ad into the capped campaign only after it has spent **$200 to $400 a day in the testing campaign at an acceptable cost**. The biggest day any single ad on our entire book has ever had is **$66.39**, and it took that much because the budget offered it, never because it hit a ceiling. The per-ad entry gate is three to six times what our largest account spends in total in a day. Not one ad we have ever run would be admitted.

**Test three is the one that would still bite at scale.** AU-048 puts the binding constraint on creative velocity. That constraint does not loosen when the budget grows.

Then the measurement problem, which is the part that would actually cost us. AU-049 says a cap drains onto the conversions nearest to purchase. Every account we run is a prospecting account. ChiroWorks and StayWell have no funnel sitting behind them, and neither has appointment outcomes marked at the desk, so we could not see the harvest-then-crash shape AU-026 predicts even if it happened. A capped ChiroWorks campaign would look excellent for a fortnight and we would hold no instrument that could tell us why.

One part of this is already live on our book without a cap anywhere. AU-012 names zero-spend days as a real operational risk. On 21 July the consolidated ChiroWorks CBO starved its chiropractic ad set to **$1.28 a day, 1.94% of a $66 campaign**, and that ad set held the best cost per opt-in in the account at **$32.73**. At $1.28 a day it needs 26 days to buy one. We manufacture starvation already. A cap would give the starvation a switch.

## 4. The decision rule

**A cap converts the budget from an instruction into a permission, so it belongs only on an account that agreed its target price in advance, produces enough creative to keep clearing that price, and can read a near-zero spend day as the control working.**

Our accounts fail the first clause before the money ever becomes the issue. ChiroWorks $33.52, StayWell $25.72, SJR Commercial $2.78 blended and Phoenix Truxx $4.00 all-time are each an average over whatever we happened to run. Not one is a target anybody agreed. AU-091 anchors a cap to demonstrated recent cost and AU-012 says set the goal exactly at break-even or target. We can do neither today, because nobody has written down what a chiropractic patient or a truck sale is worth to the business.

That is the cheap job this lesson exposes. Write a target cost per opt-in for each account. It takes an afternoon and it unblocks more than caps.

## 5. Quiz

Drop your answers in `_answers-inbox.md`.

**1.** A capped campaign carries a $3,000 daily budget and spends $140 on Tuesday. Explain in two sentences why that row is not evidence of a problem, and name the setting you would be wrong to change.

**2.** AU-005 is T2 across $200M and 253 accounts. State the question it answers, then state the question operators quote it for, and say why those are two different questions.

**3.** AU-012 names three spend floors and AU-048 names a creative-velocity prerequisite. Which of the two is the binding constraint on our book today, and which one would still bind if a client handed us $300,000 a month tomorrow?

**4. Scenario.** Phoenix Truxx is running at $72.73 a day with an all-time blended cost per opt-in of $4.00. Someone proposes a cost cap set at $4.00 to protect efficiency through Q4. Give three separate reasons to refuse, each with a number from this lesson, and name the one thing you would need before a cap on that account could even be configured honestly.

**5. Scenario.** A new e-commerce client arrives spending $340,000 a month, 60 new ads a month, 90-day repeat purchase rate 41%, target new-customer cost per acquisition $70, trailing 30-day actual $62. They want the AU-095 build, and they clear every floor in this lesson. Name the two risks that survive clearing the floors, say which claim and tier each comes from, and state the one reporting change you would make before launch so each risk would be visible if it happened.

> [!note]- Answer key
>
> **1.** Under a cap the budget is permission rather than an instruction, so Meta may only buy auctions it forecasts it can win at or under your cost per result goal, and a quiet day means those auctions were not available at that price. The setting you would be wrong to change is the **cap**: raising it to unlock spend removes the only thing holding the price. Full credit also for naming the budget as the thing you may raise freely under a cap, which inverts the usual step-size discipline, and for noting that one Tuesday is not a window, so the read is week over week per AU-026.
>
> **2.** AU-005 answers **whether a cost control delivers to the target you set it**, and on min ROAS 7-day click it delivered 96.5%. It gets quoted as evidence that **running a control beats not running one**. Those are two different questions because the study has no uncapped arm: every account in it was already cost-controlled, so it measures the instrument's accuracy and is silent on the counterfactual. AU-051 is the honest summary of that gap, and the count of controlled capped-versus-uncapped comparisons on one account across the roster is zero.
>
> **3.** On our book **both bind, and the spend floor binds first and by the larger margin**: our largest account runs about $18,400 a month equivalent against floors of $100k total to $300k a month, and the per-ad entry gate of $200 to $400 a day is three to six times our largest account's whole daily spend. At $300,000 a month the spend floor is cleared and **AU-048's creative-velocity prerequisite still binds**, because creative supply does not scale with the budget. Credit for adding that AU-048 is the reason AU-012's zero-spend-day risk actually fires: a capped ad set starves when the creative cannot find enough people who clear the cap.
>
> **4.** Any three of these, with the number attached. The account runs **$72.73 a day**, about $2,180 a month, against a floor of $100,000 total or $300,000 a month, so it fails AU-012 by more than an order of magnitude. Its biggest measured single-ad day is **$34.03** against AU-095's **$200 to $400 a day** entry gate, so no ad on the account qualifies to enter a capped campaign. The **$4.00** is an all-time blended average of whatever we ran and was never an agreed target, while AU-012 says set the goal at break-even or target, so the proposed cap value has no basis. It is a prospecting account, so AU-049 predicts the cap drains onto the warmest conversions and its cost per opt-in stops describing cold acquisition. And the $4.00 straddles the March 2026 click redefinition, so it is not a clean reading of our own history either. What you need first: **an agreed target cost per opt-in derived from what a truck sale is worth**, on a post-March window. Credit for adding that Q4 repricing is the worst moment to introduce a control nobody can read yet.
>
> **5.** Risk one, **AU-049, T4**: a 41% repeat rate means a large warm pool, so the cap drains onto near-purchase buyers and the campaign stops prospecting while its own cost per acquisition column looks excellent. Risk two, **AU-048, T3**: 60 ads a month is the whole question, and if that velocity cannot keep feeding people who clear the cap, AU-012's zero-spend days arrive. Credit also for **AU-026, T4**, harvest then crash, and for **AU-091's** attribution tension, where his 1-day-click preference sits against AU-005's T2 finding that 1-day click missed target more often. The reporting change: **report new-customer cost per acquisition separately from blended**, which is exactly what made AU-095's own result readable, because a blended number hides the AU-049 drift completely. Full credit also for a week-over-week view rather than a to-date one, so the harvest shape stays visible, and for holding out an uncapped arm, which would make this the first controlled comparison on file anywhere.
