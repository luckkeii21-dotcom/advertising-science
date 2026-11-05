---
title: "Lesson 072 - Nobody Has To Remember To Put It Back"
type: lesson
lesson: 72
date: 2026-11-05
topic: Scaling Models
claims: [SC-182, SC-117, SC-101, SC-100, SC-134, SC-044, SC-001, MD-141]
tags: [advertising-science, lesson, scaling, budgets, automated-rules, seasonal]
---

# Lesson 072 · Nobody Has To Remember To Put It Back

Topic: Scaling Models. The research lane launched in the same second as this one and has written no entry, so the newest banked work is yesterday's second pass, which added zero claims. Quiet harvest. The pointer has sat on Scaling Models for five straight lessons, and [[Scaling Models#SC-182|SC-182]] has been untaught for seven days on that same topic. Pointer and backlog land together, so this one comes off the rotation in the ordinary way and the pointer finally moves. No video: Thursday.

## 1. The mechanism

Meta has a control that raises a daily budget for a window you set in advance and then puts it back by itself.

Jon Loomer describes it plainly: "you can plan increased spending of existing ad sets by using the schedule budget increases option. So, if you're spending $100 per day, you can say to increase that to $200 per day for week one and $300 per day for week two. When that scheduled increase ends, your budget returns to normal."

Two stacked windows, set once, and an automatic return.

Read the second half, because the second half is the finding. Every scaling model in our codex assumes a person is watching. [[Scaling Models#SC-100|SC-100]] holds each step 5 to 10 days before the next one. [[Scaling Models#SC-044|SC-044]] waits for 3x the target cost per result over at least 3 days. [[Scaling Models#SC-001|SC-001]] argues about whether the step is 5% or 20% or folklore. Every one of those prescriptions has the same soft spot: somebody has to come back and act. A promotion ends and the budget is still high. A test wins and the budget never moves. Those are process failures, not delivery failures, and they do not show up in any column.

The analogy that actually maps: a push-button tap in a public bathroom against a tap you turn. The push-button tap does not run better. It runs for a fixed number of seconds and then stops, so it cannot be left running. Scheduled budget increases do not make the raise work better. They make it impossible to forget the return.

## 2. The evidence

[[Scaling Models#SC-182|SC-182]] carries **two tiers for two different assertions**, and that split is worth learning on its own.

**T3 for the control.** Loomer describes it. He does not show it on screen, shows no account, and publishes no result from using it. One credible operator narrating a feature.

**T1 for the recommendation.** Meta's own peak-season page, published the same week, lists budget scheduling among the things it tells advertisers to do. So the operator and the platform agree, which on budgeting is rare enough to record.

Now the part that decides how far you can push this: **there is zero evidence that a scheduled increase performs differently from the same increase made by hand, and zero evidence on what it does to the learning phase.** Nobody has measured either. So the claim buys process safety and nothing else. If you tell a client a scheduled ramp will deliver better than a manual one, you have invented the only half they care about.

Loomer's own position in the same recording cuts against treating any of this as the lever: "whether or not you have a good Black Friday, Cyber Monday is unlikely to be because of your budgeting decisions." He tells operators not to obsess over the increase percentage or learning-phase resets. That is an assertion from a high-credibility operator with no data attached, and it runs against the careful-step orthodoxy at SC-044 and SC-001 without refuting it.

Two more to hold beside it. [[Scaling Models#SC-134|SC-134]] is the correction to how all of this gets read: the account quoting "20% a day" went from $100/day to $5,000/day in about 365 days, which is a realised average step of about 1.08% a day, roughly one green light every 17 days. A ceiling is not a schedule. And [[Meta Delivery & Andromeda#MD-141|MD-141]] is the reason to check before promising anything: this codex already holds one Meta control that existed in only about half of one agency's accounts.

## 3. Our accounts

**SC-182 closes a gap this topic opened itself.** [[Scaling Models#SC-117|SC-117]] records the claim that a $100 daily budget spends the same $100 every day, and its own caveat says it "does not address lifetime budgets or scheduled budgets, which are the platform features that would make the manual correction unnecessary." The feature has a name now. Do not reach for it as a day-of-week fix on our book, because we measured that. Phoenix Truxx, 13 July to 2 August 2026, 21 days, $4,259.23, 469 opt-ins at $9.08. Spend leaned to Sunday in all three weeks. **Opt-ins came back proportional to the dollars: chi-square 2.414 on 6 degrees of freedom, p = 0.88.** No weekday bought leads at a different rate. Saturday was the dearest day one week and the cheapest the next.

**The one piece of budget automation we ever ran failed in the opposite direction, and that is the sharpest thing on this account.** Phoenix Truxx carried an automated rule, "Daily budget de-scaling 01", cutting 5% a day whenever Meta's cost per lead read over $9, with a floor of $140. It **dragged every raise back to $140.** The scale-up rule is still on and capped at $100, so it never fires at all. Lucky disabled the de-scaling rule on 3 November and set budgets to $160 on the statics campaign and $40 on dump, up from $140 and $50.

Read that against [[Scaling Models#SC-101|SC-101]], which says a budget rule needs a dead band so the budget can simply hold. This rule had no usable band, and its threshold was worse than that: **the $9 trigger was set on a count we now know was wrong.** Phoenix September read 706 leads at $8.18 in Ads Manager against **417 real CRM people at $13.86**, because the GoHighLevel Conversions API step echoed every instant-form submission back as a website Lead. A rule aimed at $9 on a number that was really $13.86 fires more or less permanently. **So our budget automation ran the ramp in reverse, and no human forgot anything.** SC-182 removes the forgetting failure. It does nothing about this one.

**Where a scheduled ramp has an actual date to attach to.** The 9 October structure audit found one Phoenix CBO at $180.50 a day holding about seven ad sets mixed together, including a winter English lane and a winter Spanish lane. Plow and winter work are a named "why now" in that account's own ICP file. As of today there is an open item to split it into up to four campaigns by division, roughly $50 on Phoenix Experience, $60 on box, $50 on dump plus plow and $40 on the rest, once Ruddy's picks come back. **That is the first dated seasonal ramp on our book in months, and the return date is the thing nobody has written down.**

**The rest of the book, honestly.** SJR Commercial ran $767.78 for 136 opt-ins at $5.65 in the week of 23 to 29 October, the best clean instant-form week on record, at roughly $110 a day. SC-100 permits a 50% step at that level. Nobody has scheduled one. StayWell ran $562.63 for 23 at $24.46 in the same week, a recovery after two down weeks, and a scheduled ramp onto a recovering account is not what this claim argues for. RK Consumer Services was built paused yesterday at $50 a day CBO, and its own launch playbook says $50 flat for 7 to 14 days, so SC-182 is not for it yet.

**And the limit that matters most.** SC-182 arrives inside Black Friday guidance. **We have no Black Friday.** Commercial trucks in New Jersey, a spine clinic in Michigan, a final expense agency in California. Our seasonal events are plow season and the year-end truck buying window, and neither has ever had a dated budget plan written for it.

**Nobody has confirmed this control exists on any account we hold.** On the MD-141 precedent that is a real question, not a formality. It is the sixth two-minute read in a live interface named across six consecutive lessons, and none of the six has an owner.

## 4. The decision rule

**A budget raise is not planned until its return date is set in the same action.** Use Meta's scheduled budget increase so the ramp and the revert ship together. If the control is not in the account, the raise does not go in until a dated return and an owner are written down.

## 5. Quiz

Drop your answers in `_answers-inbox.md`. Lesson number plus answers is enough.

1. SC-182 carries two tiers. Name both, say which assertion each one covers, and say what the claim has no evidence for at all.

2. A client asks whether scheduling the increase will perform better than you raising the budget by hand. Answer in two sentences, and be precise about what you are and are not claiming.

3. Applied. Ruddy's picks come back and Phoenix splits into four campaigns, with dump plus plow at about $50 a day. You want to push the plow lane for a six-week winter window. Write the plan: what you set, what you set it to, and the single thing that makes this plan different from the budget work already on that account. Then name the one check you run before any of it, and why.

4. Applied. Someone proposes scheduling higher budgets on Sundays across Phoenix and SJR, because our own data shows Meta already leans spend to Sunday. Kill or approve, with the number that settles it, and say what the Sunday finding does and does not establish.

5. Applied. Phoenix's de-scaling rule had a $9 trigger, a $140 floor and a scale-up rule capped at $100. Name the two separate defects in that setup, say which claim describes each, and say which of the two SC-182 would have prevented.

> [!note]- Answer key
> **1.** T3 for the control itself: Loomer describes it, no screen, no account, no published result. T1 for Meta's recommendation: Meta's own peak-season page lists budget scheduling among its instructions to advertisers. **No evidence at all** on two things: whether a scheduled increase performs differently from the same increase made by hand, and what it does to the learning phase. Full marks need the "no evidence" half, because that is where a client conversation goes wrong.
>
> **2.** No, there is no reason to expect it to perform better and nobody has measured it. What it does is guarantee the budget returns on a date you chose, which removes the overspend that happens when a promotion ends and nobody lowers it. Deduct for any answer that implies a delivery or learning-phase benefit. Deduct for an answer that dismisses the control as pointless: the process failure it removes is real and has cost money on our own accounts.
>
> **3.** Set a scheduled budget increase on the plow lane with the window and the step both defined in advance, for example $50 to $100 for the first stretch and $150 for the peak, with the automatic return landing at the end of the window. **The thing that makes it different: the return is in the same action as the raise, so the budget comes back without anyone remembering.** Step size should respect SC-100 at that budget level, and SC-134 says the ceiling is not a schedule. The check first: confirm the control actually exists in that ad account, on the MD-141 precedent where a Meta control was present in only about half of one agency's accounts. A strong answer also notes the Conversions API echo was removed from that account on 21 October, so any cost threshold is now readable against real numbers.
>
> **4.** Kill it. **Chi-square 2.414 on 6 degrees of freedom, p = 0.88**, measured on Phoenix's own 21-day export: opt-ins landed proportional to spend and no weekday bought them at a different rate. Saturday was the dearest day one week and the cheapest the next, so the spread is noise. What the Sunday finding establishes is only that Meta chose where the money went, which refutes "it has no choice" on that account. It does not establish that Sunday converts better, and the second half of the same measurement removes any reason to act. Zero marks for approving on the spend lean alone. Half marks for killing it without the p-value.
>
> **5.** Defect one: **no dead band.** The scale-down trigger and the scale-up cap left no range where the budget could hold, so the rule pulled every raise back to the $140 floor. That is SC-101, which says set the scale-down threshold worse than the scale-up threshold on purpose. Defect two: **the trigger was anchored to a false number.** $9 was read off a count inflated by the CRM lead echo, where September's 706 at $8.18 was really 417 real people at $13.86, so a $9 rule was always going to fire. **SC-182 would have prevented neither.** It removes the forgetting failure, and this rule failed while running exactly as configured. Full marks require naming that SC-182 is not the fix here.
