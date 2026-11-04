---
title: "Lesson 071 - The Setting That Decides Our Numbers Has Never Been Read"
type: lesson
lesson: 71
date: 2026-11-04
topic: Attribution & Incrementality
claims: [AT-132, AT-082, AT-085, AT-012, AT-003, AT-006, AT-038, AT-037, MD-187]
tags: [advertising-science, lesson, attribution, incrementality, reporting, lead-gen]
---

# Lesson 071 · The Setting That Decides Our Numbers Has Never Been Read

Topic: Attribution & Incrementality. Second teacher pass today. Lesson 070 shipped this morning on the two claims the research lane banked at 04:47, and nothing has been banked since, so this slot goes to the backlog. It goes to [[Attribution & Incrementality#AT-132|AT-132]], untaught for eleven days, which the 1 November scoreboard already reserved for the next quiet harvest. No video on this one, and section 5 says why.

## 1. The mechanism

Meta prints three definitions of its own attribution settings, side by side, one line each.

> "Standard attribution counts what the ads touched. Incremental attribution counts what the ads added. Custom attribution counts it the way your business already counts it. Those are three different numbers. If the one you optimise against isn't the one your finance team uses, you're reading a different campaign from the one you're running."

Three numbers off one campaign. Three different numbers, not three opinions about one number. The setting picks which of the three lands in the column you screenshot into a client report, and it also feeds delivery, so it changes which ads get the money ([[Attribution & Incrementality#AT-006|AT-006]]).

Then Meta writes the sentence that should make you open a tab.

> "The attribution setting is how you agree to be judged."
> "It's the decision most likely to be inherited rather than chosen."

Think about the electricity meter in a rented flat. The landlord installed it years ago and picked a tariff. You pay the bill every month. You argue about the air conditioner. You have never once read which plan the meter is on, and the plan decides the bill more than the air conditioner does.

That is our position on every account we have taken over. Somebody set the attribution window when they built the ad set. Nobody re-read it. Every number we have reported came out the other side of it.

## 2. The evidence

[[Attribution & Incrementality#AT-132|AT-132]], **T1**. Meta's own words, best-practice post dated 21 October 2026, read in full. Definitions only. No number, no test, no statement of how the incremental model is fitted, no eligibility floor for any of the three. T1 buys the definitions and the framing. It buys nothing about effect size.

[[Attribution & Incrementality#AT-082|AT-082]], **T1**. The instrument exists and it is free. Columns, then Compare attribution settings. It splits one conversion total four ways: 1-day click, 7-day click, 1-day view, 1-day engaged view. Shown live on a campaign with 15 booked calls. The same claim records that **this view has never been opened on a single one of our accounts.**

[[Attribution & Incrementality#AT-085|AT-085]], **T2**. Somebody else opened it and narrated his screen. 379 credited conversions fell to 206. CPA went from $14 to $26. That is 173 conversions removed, a 46% cut, an 86% rise in cost. One account, window not stated, vertical not stated, no backend reconciliation. Never quote 46% as a benchmark. It is a price tag on the gap, not a rate.

[[Attribution & Incrementality#AT-012|AT-012]], **T2**. Two shown splits. 427 conversions, 390 from 7-day click, 37 from view-through, about 10%, which the operator leaves alone. And an audited ecommerce account where switching the read to 7-day click alone cut ROAS from 2.14 to 1.68 and attributed revenue from about $79k to about $62k in one month. He says roughly 95% of audited accounts never touch the column.

[[Attribution & Incrementality#AT-003|AT-003]], **T2**, and this is the one that stops you doing something stupid with all of the above. You cannot judge a change of attribution model from the column that model produces. Reading an attribution switch off the switched column is reading the instrument against itself. The read-out lives in the CRM or at store level, over a window long enough for a business number to move.

Notice what the tiers do here. The definitions are T1. The instrument is T1. Every number about how big the difference is runs T2 and comes from other people's accounts. We hold zero T2 of our own on this entire question, and converting that costs one click and no spend.

## 3. Our accounts

**We never chose the setting on our instant-form ad sets. The API chose it.** The build note is explicit: for `optimization_goal=LEAD_GENERATION` with `destination_type=ON_AD`, attribution must be 1-day click, and 7-day click plus 1-day view is rejected outright. Every instant-form ad set we have created through the API sits on 1-day click because Meta would not accept anything else. Inherited is generous. It was assigned.

**The two written specs on the book disagree with that, and with each other.** MetaTechAI's 25 August strategy says 7-day click, 1-day engaged view, view-through off. The v7 locked version a day later says 7-day click only, view-through and engage-through off, audited monthly. Neither matches what an instant-form ad set is permitted to run.

**We already know what happens when the counted number and the business number drift, because it cost a campaign.** Phoenix Truxx, September 2026: Ads Manager showed 706 at $8.18 against **417 real CRM people at $13.86**. SJR Commercial the same month: 809 at $4.07 drafted against **358 real people at $9.19**. The impossible number that proves the Phoenix count was wrong is 230 website leads against 222 landing page views. On the inflated read, images looked 2x cheaper than video. On real people the gap was 16%. Per qualified buyer the two campaigns cost **the same**, and the video campaign had already been paused on the 2x read. That is [[Meta Delivery & Andromeda#MD-187|MD-187]] and AT-132 arriving as the same failure from two directions: what counts as a conversion decides which creative wins.

**ChiroWorks gave us the purest example of inheritance in the vault, and the client found it, not us.** Their 24 July attribution review recorded that the campaign we call "Functional Tonal Neurology | Free consultations Offer" is stored in their CRM as **"test"**, because that was its name when those leads arrived. Renames break attribution for leads already captured. Same audit: `{{ad.name}}`, `{{campaign.name}}` and `{{ad.id}}` sitting in their CRM as literal unresolved tokens. We flagged that on 20 July, four days before their audit. It was found and not fixed.

**And the honest limit on where the incremental setting is usable at all.** Native instant-form leads are a direct in-app click, so the gap between the blended and incremental reads is small and nobody should expect an ecommerce-sized drop. The model is fitted from lift data and needs real volume, so it is unreadable on a $50/day account. ChiroWorks at $50/day could never have produced a number from it. At that size the incrementality leak is downstream anyway, in the lead that never shows, and cost per booked already catches it.

**Current state of the gap, restated for the book we have today.** AT-082 names five accounts and that list is stale: ChiroWorks off-boarded on 14 October, StayWell and RK Consumer Services came in. The gap did not change. No file in this vault records a Compare attribution settings read for StayWell or RK Consumer Services either. We still cannot state a view-through share or an incremental drop-off for a single live client.

## 4. The decision rule

**The attribution setting is a decision somebody made on your behalf, so read it on every account you hold, write it down, and never judge a change to it from inside Ads Manager.**

Three parts, because each one fails on its own.

- **Read it.** Every account, at takeover and then monthly. One screen.
- **Record it.** Next to the campaign, with the date. SJR's own performance thesis already bans switching settings mid-flight because it breaks comparability, and that ban only means something if the setting is written down somewhere.
- **Judge it outside.** Any read-out on an attribution change comes from the CRM count of real people, over a window long enough to move.

## 5. Why there is no video on this one

Wednesday is a video day and today's video already shipped with lesson 070, rendered and checked against a contact sheet. Building a second one for a second same-day lesson buys nothing this note does not already carry. One video per video day, and it is met.

Worth saying plainly: the answers inbox has been empty for twelve consecutive runs, and two lessons landed today. If the pile is the reason nothing comes back, say so and the cadence changes.

## 6. Quiz

Answers into `_answers-inbox.md`, lesson number plus your answers.

**Q1.** Meta names three attribution settings and defines each in one line. Name all three and what each one counts.

**Q2.** AT-085 shows an account going from 379 conversions at $14 to 206 at $26 when the incremental column is read. Why is it wrong to tell a client to expect a 46% cut?

**Q3.** You take over a chiropractic account at $120/day running instant-form ads built through the API. You want to know whether its reported cost per lead is inflated by view-through credit. State what you open, what four numbers you expect, and what you can conclude from them about incrementality.

**Q4.** A teammate switches a client's ad sets to incremental attribution on Monday. On Friday he sends you a screenshot of the incremental column showing cost per lead down 11% and says the switch worked. Name the error and state the read-out you would accept instead.

**Q5.** Phoenix Truxx September: Ads Manager 706 at $8.18, CRM 417 real people at $13.86, and per qualified buyer the image and video campaigns cost the same. One campaign was paused on the inflated read. Split that failure into its counting half and its attribution-setting half, and say which half the pause belongs to.

> [!note]- Answer key
> **Q1.** Standard counts what the ads touched. Incremental counts what the ads added. Custom counts it the way the business already counts it. Full marks need all three, including custom, which appears nowhere else in the codex.
>
> **Q2.** It is one account, one unstated window, one unstated vertical, one operator, with no backend reconciliation. [[Attribution & Incrementality#AT-074|AT-074]] is the standing reason to expect the size of the drop to be a property of the account rather than of the platform. Quote the direction, never the rate. Deduct for any answer that treats 46% as a benchmark. Credit for adding the operator's own caveat: at $26 he still calls the account very efficient, so the honest client framing is that the ads still work and the number we were quoting was the wrong number.
>
> **Q3.** Columns, then Compare attribution settings. The four columns are 1-day click, 7-day click, 1-day view and 1-day engaged view (AT-082). About 10% or less sitting in the view columns is the level you want to find; [[Attribution & Incrementality#AT-037|AT-037]] puts the typical share at 30 to 50%, so treat 10% as a healthy exception rather than an expectation (AT-012). **The trap is the last part.** The split runs entirely inside Meta's attribution layer, so it answers click versus view and says nothing about incrementality. Reconcile against the business number before concluding anything ([[Attribution & Incrementality#AT-038|AT-038]]). Half marks for the correct path with the wrong conclusion. Extra credit for noticing that an API-built instant-form ad set is forced onto 1-day click, so the 7-day and view columns may be near empty and the exercise is thinner than it looks on that lane.
>
> **Q4.** Circularity (AT-003). He is judging a change to the attribution model from the column that model produces, which is reading the instrument against itself. Five days is also far too short for a business number to move. Accept: the CRM count of real people first-touched by those ads, over a window long enough to move, against the same count before the switch. Deduct for any answer that fixes this by switching the column back and comparing the two columns to each other.
>
> **Q5.** Counting half: the CRM Conversions API echo counted one person twice, so 706 was never 706, and 230 website leads against 222 landing page views is the arithmetic proof. Attribution-setting half: MD-187 and AT-132, where what counts as a conversion re-ranks existing creative against each other. **The pause belongs to the ranking, not the count.** The wrong count made images look 2x cheaper; the decision that acted on it was a creative ranking read off a number two lanes did not share. Full marks require naming cost per qualified buyer as the number that showed the two campaigns were equal, and noting the echo was still live on the statics lane as of the 23 to 29 October pull, 66 lead actions against 16 real ones.
