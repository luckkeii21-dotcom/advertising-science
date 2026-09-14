---
title: "Lesson 025 - The Price of the Front Door Picks Who Walks In"
type: lesson
lesson: 25
topic: Marketing Math & Unit Economics
source: Rotation index 9, taken in the ordinary way. The 2026-09-13 research run banked 0 claims from 0 transcripts, so there was no harvest material. Closes the standing queue item MM-204 with law 21c, held since 2026-09-09 for want of an honest local-service translation. Second lesson on this topic; lesson 013 covered the missing downstream column.
created: 2026-09-13
updated: 2026-09-13
tags: [advertising-science, lesson, marketing-math, offers]
---

# Lesson 025 · The Price of the Front Door Picks Who Walks In

> Lesson 013 said cost per opt-in cannot rank two ads on its own, because the downstream column is missing. This one is harder. Even with that column built, the number breaks the moment you change the price of the offer, because you are no longer measuring the same population.

**If you only answer two questions, answer Q3 and Q4.** Q3 is live on ChiroWorks right now and nobody has pulled the data. Q4 is the arithmetic you will need the first time a client asks whether adding a price was worth it.

## 1. The mechanism

A price is a filter before it is a fee.

Run a free concert and 400 people take a ticket. Charge $20 and 60 people buy. On the night, a large share of the free crowd finds something better to do, and almost everyone who paid turns up, because they already spent the money and walking away costs them something. Cost per ticket handed out says the free show won by a mile. Cost per person actually in a seat says something else entirely.

Nothing about the two crowds is the same except the name of the event. The $20 did not make people more committed. It selected for people who were already committed enough to pay.

That is the whole idea, and it has a sharp consequence for how we read our own reports. **When the front-door price changes, the cost per opt-in before the change and the cost per opt-in after the change are measuring two different populations.** They sit in the same column, in the same currency, in the same account. They are not comparable. Every instinct says to put them side by side and read the difference as performance. The difference is mostly composition.

The same thing runs in reverse. A discount does not only buy volume. It buys a different kind of customer, and that customer behaves worse afterwards.

## 2. The evidence

**MM-204, T2, active.** Two brands, two industries, both stated as over $10 million online, Shopify cohort reports read on screen. Brand one: a November cohort's average spend per customer grew from $114 to $158 by month six, up 38.5%, against 63% for a February or March cohort. Brand two: November $116 to $170, up 46%, against 55% for February. The operator's mechanism is plain consumer reasoning. A November buyer is someone a large discount pushed over the edge. A February buyer walked past every sale of the previous two months, which means both money and conviction. *He summarises brand one's gap as "50% worse". His own numbers give 38.5/63 = 0.61, so it is 39% worse. Quote 39%.* Both gaps are understated, because the native Shopify report is built on revenue and peak revenue carries a worse gross-profit percentage.

**Law 21c** in our hot layer already carries this, and it now has two reasons under it. The margin reason from MM-085: a brand at 50 points of gross margin holding a MER of 4 keeps 25% contribution at full price and 10% once a discount takes margin to 35 points, which is below most brands' operating expenses. And the selection reason from MM-204 above.

**Why this sat unteachable for four days.** Both of those are e-commerce. All five of our clients are local service businesses. Nobody repurchases a chiropractic intro session in November. The translation had to be found rather than assumed, and it turns out one of our own clients made it four months before the codex banked the claim.

**MM-002 is the guard rail.** Three operators state the numerator of their LTGP:CAC out loud and they do not agree. A 2.5 on revenue and a 2.5 on gross profit are different businesses, a factor of two apart at 50 points of margin. Same failure as this lesson, one level up: a number is meaningless until you know what population or quantity is inside it.

## 3. Our accounts

**StayWell made this exact move in May 2026, and gave MM-204's reason back before we had MM-204.** The knee offer went from a free consultation to a paid roughly $39 evaluation. The stated reason, in the brief: too many booked appointments were no-showing, so the price adds friction and only serious patients book and show. Kartik's instruction was to put the price in the ad itself so it filters before the form fill. That is selection by price, described by a chiropractor in Novi, Michigan, four months before two Shopify cohort reports put a number on the same mechanism.

**Two of our chiropractic accounts ran opposite front doors in the same week, and the free one was dearer.** Week of 24 to 30 August 2026, recomputed line by line from the raw ad-level exports:

| Account | Front door | Spend | Opt-ins | Cost per opt-in |
|---|---|---|---|---|
| StayWell Spine & Joint | paid, $39 evaluation | $249.59 | 10 | **$24.96** |
| ChiropracticWorks | free consultation | $479.68 | 10 | **$47.97** |

StayWell's single biggest ad that week is named `StayWell | BestPerformer Remake | $39+FREE Xray`, $98.57 and 4 opt-ins, so the price is in the creative exactly as instructed. ChiroWorks' invisa-RED ad set took $315.33 for 7 opt-ins at $45.05, which is 65.7% of the account.

**Label this honestly before you repeat it.** Different cities, different body parts, different creative, different budgets, one week, ten opt-ins each. It is not a controlled comparison and it proves nothing about price. What it does is kill the lazy assumption, which is that the free door is obviously the cheap door. On our own book, in the same week, in the same vertical, it was not.

**The only measured selection effect we own is not about price, and it is the clearest thing in this file.** ChiroWorks, 10 to 24 July 2026, 24 traced opt-ins. Nine of them were already contacts in the CRM, aged 169 to 1,979 days. All three bookings came from those nine. Zero of the fifteen genuinely new opt-ins booked. Ads Manager charged the same for both groups and printed one number over the top of them.

**Our own counter-analysis on that, and keep it attached.** Three events is a thin base. The client's one-sided Fisher gave p = 0.042; move one booking to the new group and it goes to p = 0.31, and across the wider 10 to 27 July window it is 3-of-9 against 1-of-19, p = 0.084. The bigger problem is a confound we found ourselves: all three bookings arrived through SMS automation, and only 2 of 22 called opt-ins ever reached a live human, median call length 5 seconds. So the test that actually ran was "text a familiar name" against "text a stranger". Treat it as the shape of a selection effect rather than its size.

**Now the live one, and this is the part that matters this week.** ChiropracticWorks changed the invisa-RED front door from a free consultation to a **$49 introductory session on 6 September 2026**. Seven days ago. Three things are true today:

- **The ad, the form and the project file still say free.** The live Instant Form is still named `invisa-RED Free Consultation Form EvrythingAI`, form ID `1759974908344299`. Its third question still reads "How soon would you like to come in for your free consultation?" and the thank-you headline still reads `Free invisa-RED Consultation`. The project file still carries "Active offer (advertise this ONLY): the $0 Free Consultation". Nothing on disk records a change to any of them.
- **No ChiroWorks data has been pulled since 30 August.** The weekly runs on 4 September and 11 September produced no ChiroWorks folder at all. There is no before-and-after series for a change that is a week old.
- **Nobody could read the outcome even with the data.** No ChiroWorks appointment has ever been marked showed or no-show. We established that on 7 September. The show rate is the only number that can say whether a $49 gate worked, and the field has never been written to.

**So the account is in the worst available position.** The ad promises free, the clinic charges $49, and the person finds out at the desk. That collects the free door's acquisition cost and the paid door's arrival risk at the same time, which is the one combination that has no upside.

**How much does a price have to buy?** Take the invisa-RED free-door figure of $45.05 per opt-in as the baseline. Let the $49 gate raise cost per opt-in by some multiple, and let the $49 come back as revenue from everyone who arrives. Net cost per patient in the chair matches the free door when the paid show rate reaches `P_paid / (P_free / s_free + 49)`.

| If cost per opt-in rises | Paid door costs | Free show rate 10% | 20% | 30% |
|---|---|---|---|---|
| 1.5x | $67.57 | 13.5% (1.35x) | 24.6% (1.23x) | 33.9% (1.13x) |
| 2.0x | $90.10 | 18.0% (1.80x) | 32.9% (1.64x) | 45.2% (1.51x) |
| 3.0x | $135.15 | 27.1% (2.71x) | 49.3% (2.46x) | 67.9% (2.26x) |

Read the middle row. If the $49 gate halves the opt-in count, it has to lift show rate by 64% in relative terms just to break even. That is a demanding number, and it is a floor, because the table credits the paid door with the full $49 and charges it no extra cost of delivery.

**The table is a decision aid and not a result.** The show-rate column does not exist on either account. StayWell's only recorded appointment in the 8 to 16 August week was booked and then cancelled, a show rate of 0% on one record. That is an absence, not a measurement.

## 4. The decision rule

**When the price of the offer changes, start a new series. Never read across the change.** Report the two periods as two populations, say in one line that the offer changed and on what date, and treat the front door's price as a lever on show rate that has to be measured downstream before anyone claims it worked.

## 5. Quiz

Drop answers in `lessons/_answers-inbox.md`. Lesson number plus your answers. Partial is fine and still gets graded.

1. MM-204 is two Shopify cohort reports from brands over $10 million online. All five of our clients are local service businesses with no repeat purchase to measure. State what actually transfers from that claim to a chiropractic clinic and what does not, and name the one thing our own book supplied that the e-commerce evidence could not.

2. The codex holds a number that should be quoted as 39% and is stated by its own source as 50%. Give both figures, show the arithmetic that decides between them, and explain in one sentence why the codex keeps the source's wrong version on the record instead of deleting it.

3. **ChiroWorks, live.** The invisa-RED offer became a $49 introductory session on 6 September. The ad, the Instant Form and the project file still say free consultation. The last data pull ends 30 August. No appointment has ever been marked showed or no-show. Kartik asks on Monday whether the $49 change is working. Answer him. Say what you can measure today, what you cannot, what you would fix first and in what order, and what you would refuse to put in the client report.

4. **Applied arithmetic.** ChiroWorks' invisa-RED ad set ran $45.05 per opt-in before the change. Suppose the $49 gate cuts opt-in volume so that cost per opt-in reaches $90.10, and suppose the free door was showing 20% of the people who opted in. Work out the show rate the paid door needs to break even on cost per patient in the chair, show your working, and then name two ways this arithmetic flatters the paid door.

5. In the week of 24 to 30 August, StayWell's paid $39 front door produced opt-ins at $24.96 and ChiroWorks' free front door produced them at $47.97. A teammate wants to write "charging for the first visit halves cost per opt-in" in a deck. Say what is wrong with that sentence, list every reason the two numbers are not comparable, and give the version of the claim you would actually defend.

> [!note]- Answer key
> 1. **What transfers is the mechanism, which is selection.** A price or a discount changes WHO says yes, not only how many, and the acquisition column cannot see the difference because it charges the same for both populations. **What does not transfer is the measurement.** MM-204's evidence is cohort spend over six months, which requires repeat purchase and a customer-level revenue record. A chiropractic clinic has no November cohort to follow, and the local-service equivalent of "repeats worse" is "does not show up", which lives in a CRM field rather than in Shopify. **What our own book supplied:** a named business decision made for exactly MM-204's reason before the claim existed. StayWell moved from a free consultation to a paid roughly $39 knee evaluation in May 2026 because booked appointments were no-showing, with the instruction to put the price in the ad so it filters before the form fill. Full credit needs both halves, mechanism transfers and measurement does not. Bonus for noting that this makes the local-service version cheaper to test than the e-commerce version, because show rate resolves in days and a six-month cohort does not.
> 2. **38.5% against 63%.** The November cohort grew $114 to $158 by month six, and 44/114 = 38.6%, which matches his stated 38.5%. The February cohort grew 63%. **38.5/63 = 0.61, so November is 39% worse, not 50%.** His "50% worse" is a summary he says out loud over numbers that are on his own screen. **Why the wrong version stays:** the codex records contradictions rather than overwriting them, so anyone who later reads the source and sees "50%" finds the correction already sitting beside it instead of re-litigating it. Bonus for the second brand, 46% against 55%, which is 16% worse and shows the gap size is not stable across brands. Bonus for noting both gaps are understated because the Shopify report is revenue-based and peak revenue carries worse gross profit.
> 3. **What you can measure today: nothing about the change.** No ChiroWorks pull exists after 30 August and the change landed 6 September, so there is no post-change row of any kind. Even with the pull you would only get cost per opt-in, which is the number this lesson says cannot be read across a price change. The number that decides it, show rate, has never been recorded on this account at all. **Order of fixes, and the first one is not the data.** First, make the ad and the form say $49, because right now we pay the free door's acquisition price and hand the client the paid door's arrival risk, which is the one combination with no upside. Second, turn on the appointment and show write-back, because without it the question is unanswerable in any future week too. Third, pull the account from 31 August so there is at least a clean pre-change week on file. **What you refuse to put in the report:** any before-and-after comparison of cost per opt-in across 6 September, and any statement that the $49 improved or hurt lead quality. Say the offer changed, give the date, and say the measurement starts now. Bonus for noting the pre-change baseline is $479.68 / 10 / $47.97 at account level and $315.33 / 7 / $45.05 on the invisa-RED ad set for 24 to 30 August, so the clean comparison window is available if somebody pulls it. Bonus for spotting that a rising cost per opt-in after 6 September is the EXPECTED result of a working gate, so reporting it as a decline would be exactly backwards.
> 4. **Working.** Net cost per patient in the chair on the free door is $45.05 / 0.20 = **$225.25**. On the paid door it is $90.10 / s − $49, because the $49 is collected from everyone who arrives. Set them equal: $90.10 / s = $274.25, so **s = 32.9%**. Against a 20% free-door show rate that is a **1.64x** relative improvement. **Two ways it flatters the paid door.** It credits the full $49 as if it were pure contribution, with no cost of delivering the session, so the real requirement is higher. And it assumes the price change costs nothing except opt-in volume, when the same change also alters which ads work, resets what delivery has learned, and takes the ad set back through a period where the prediction is stale. Bonus for a third: it compares against a free-door show rate we have never measured, so the entire baseline is assumed. Bonus for noticing that the $49 is collected per ARRIVAL rather than per booking, so no-shows contribute nothing and the offset is smaller than a per-booking reading would suggest.
> 5. **What is wrong with the sentence:** it reads a difference between two accounts as an effect of a variable that was never controlled. It also states a causal claim, "charging halves cost", from a single week of parallel observation. **Why the numbers are not comparable:** different cities and catchments, Novi Michigan against Collinsville Illinois; different services, knee and spine against body contouring and chiropractic; different creative, different budgets, different ad counts and different campaign structures; one week each; and ten opt-ins on each side, which is a base too small to separate a real effect from an ordinary week. Add that StayWell's opt-in count has a known pixel double-fire history, so even the ten is uncertain. **The defensible version:** in the week of 24 to 30 August our account with a paid front door produced opt-ins more cheaply than our account with a free front door, which is enough to retire the assumption that a free offer is always the cheaper way to acquire, and not enough to attribute the gap to price. Bonus for naming what would make it a real comparison: the same account, the same city, the same creative, before and after its own price change, with show rate on both sides. Bonus for noting that ChiroWorks is about to generate exactly that data and currently cannot capture it.
