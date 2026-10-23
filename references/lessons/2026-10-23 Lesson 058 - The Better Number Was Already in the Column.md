---
title: "Lesson 058 - The Better Number Was Already in the Column"
type: lesson
lesson: 58
date: 2026-10-23
topic: TikTok Delivery
claims: [TT-027, TT-028, TT-026, AT-082, AT-037, AT-012, AT-076, AT-036]
video: "video/2026-10-23-lesson-058.mp4"
tags: [advertising-science, lesson, tiktok, attribution, windows, rep-pressure]
---

# Lesson 058 · The Better Number Was Already in the Column

![[video/2026-10-23-lesson-058.mp4]]

TikTok Delivery has been next in the rotation for five lessons running. Today it gets taken, and the claim it gets taken on is one sentence a TikTok rep says out loud to real advertisers.

We run no TikTok spend. That is not a reason to skip this. The same sentence arrives on our accounts too. It just arrives as a default setting instead of a phone call.

## 1. The mechanism

A TikTok rep tells an advertiser to move off click-only attribution and onto 7-day click plus 1-day view. The pitch, quoted: "No, no, no. You'll always get better performance in the business when you run 7 click one day views."

Read the sentence again. It says performance **in the business**.

Here is a shop. The owner counts customers at the door, one tally mark per person who comes in and buys. A consultant suggests a better counting rule: count anyone who walks in, and also count anyone who walks past the window and glances at the display. Monday's tally goes from 40 to 180.

Nothing happened on Monday. The till is the same. The number is bigger because the rule got wider.

Now the second half, which is the half that actually costs money. The shop pays its promoter a bonus per person counted. Under the new rule the promoter stops bringing people in and starts standing at the window waving at passers-by, because that is what gets counted. The counting rule did not only change the report. It changed where the effort went.

That is what an attribution window does on a paid platform. It is two different changes wearing one sentence.

**Change one, the report.** A wider window credits conversions the narrower one did not credit. The number improves. The business does not.

**Change two, the delivery.** The optimiser is fed whatever the window counts. Feed it view-through conversions and it learns that showing an ad to someone who already visited your site is cheap and effective, because for those people it is. A prospecting ad set drifts into being a retargeting ad set with nobody touching the targeting. A view-through can only fire for someone who already hit your pixel, so the drift is structural rather than accidental.

And the person making the recommendation is a salesperson whose book is your spend.

## 2. The evidence, and the tiers are the point today

**[[TikTok Delivery#TT-028|TT-028]], T3.** The rep behaviour and the quote, reported from real account relationships across an agency book. The operator reporting it says plainly that he has no data on whether the claim is true. The incentive explanation that travels with it, that rep KPIs are tied to client spend, is **T4**. There is no compensation document behind it. So the most quotable part of this claim is the weakest part of it. Say the quote, not the motive.

**[[TikTok Delivery#TT-027|TT-027]], T2.** TikTok exposes an Attribution Analytics report under Tools that breaks attributed events out by click window from 1 to 90 days, and separately by view window. The operator calls it more robust than the Meta or Google equivalent. **Tiered T2 deliberately, and notice why:** the product screen was walked through on camera and no TikTok documentation was quoted. A surface seen on screen is a shown observation. T1 needs the document. That distinction is worth more to you than the claim itself.

**[[Attribution & Incrementality#AT-037|AT-037]], T3.** Across a stated 1,000-plus audits of 7 to 9-figure brands, 30 to 50% of reported ROAS comes from 1-day view alone. Strip the window and that share disappears. T3 because the audits are recited rather than shown.

**[[Attribution & Incrementality#AT-012|AT-012]], T2.** The shown version, and it is smaller: 427 conversions, 390 from 7-day click, 37 from view-through, about 10%, left running. On a second shown account, switching the column to 7-day click alone moved ROAS from 2.14 to 1.68 and attributed revenue from about $79,000 to about $62,000 in one month. Treat 10% as the level you want to find, not the level to expect.

**[[Attribution & Incrementality#AT-076|AT-076]], T4.** The only defensible case for keeping 1-day view is an AND: Meta is the sole traffic driver AND the purchase cycle is long. Reasoning from the mechanism, no test attached. The delivery-drift half of today's lesson lives mostly at this tier, and hold that honestly. The consequence is large and the evidence is thin.

**[[Attribution & Incrementality#AT-082|AT-082]], T1.** Meta's own instrument. Columns, then Compare attribution settings, and one conversion total splits four ways: 1-day click, 7-day click, 1-day view, 1-day engaged view.

**[[Attribution & Incrementality#AT-036|AT-036]], T1.** And the column does not mean what it meant last year. In March 2026 Meta made 7-day click require an outbound click and moved likes, shares and saves into 1-day engaged view. Any 7-day-click series crossing March 2026 is two different measurements.

## 3. Our own accounts

We have measured this once, and the measurement is better than the claims above because it is ours.

**ChiroWorks, `act_548394595331610`, read 26 August 2026.** One view, 1 June to 25 August, all four windows applied, a within-account control so both event types rendered in the same pull.

One website-pixel campaign, since retired, $643.85 of spend:

| Window | Leads | Cost per lead |
|---|---|---|
| 1-day click | 42 | $15.33 |
| 7-day click | 46 | $14.00 |

Same ads, same spend, same dates. The window moved the reported cost per lead by $1.33, about 8.7% cheaper, and not one extra person walked into that clinic because of it.

**Then the direction nobody expects.** That campaign ran a 1-day click or 1-day view default, and 1-day click alone read 42 against a default total of 42. **View-through contributed zero.** On this campaign the rep's promise would have delivered nothing at all. The real under-count was the narrow click window, not a missing view window.

Scope it hard before you repeat it. One retired campaign, one clinic, a lead event, $643.85 of spend. AT-037's 30 to 50% was measured on purchase events at 7 to 9-figure ecommerce. Different event, different population. Our reading neither confirms nor refutes it.

**The finding that changes a standing task.** In the same view, four Instant Form campaigns at 46, 20, 6 and 4 leads returned `—` on every window column. StayWell repeated it, including 216 leads at $6.82 across 1 May to 15 June with the Results column fully populated. Two rival explanations were tested and refuted: it is not an empty Results column, and it is not slow loading. **Event type is the variable.** So AT-082's open item, the one that says Compare attribution settings has never been opened on any of our five accounts, is mis-scoped. On Instant Form it is not an unopened task. It is unachievable, and no fix to an optimisation event unlocks it. Phoenix Truxx, SJR Commercial, StayWell and the ChiroWorks form campaigns all sit on that side of the line.

**And we already own TT-026's defect without ever touching TikTok.** [[TikTok Delivery#TT-026|TT-026]] says an optimisation event chosen for the wrong thing makes the account's own CPA column unreadable: 449 clicks and 206 conversions on one campaign, because a page load was being counted as a conversion. Our version is SJR's `Truck buyer leads | NJ`, which reads $10.5844 per result against $6.8959 per actual opt-in, because 28.48% of that account's opt-ins arrive through the website and a form ad set's own column cannot count them. Different cause, same consequence: the column in front of you is not counting the thing you are judging.

## 4. The decision rule

**Any attribution-setting recommendation is two proposals in one sentence, one about the report and one about where the money goes. Separate them before you answer, and take neither from someone who is paid on your spend.**

Two habits follow. Read the same window before and after any change, so the comparison survives. And never let a window change reach a client as performance, in either direction.

## 5. Quiz

**1.** A rep's recommendation to widen the attribution window makes two separate changes. Name both, and say which one the rep's own quote is claiming.

**2.** TT-027 describes a product screen walked through on camera and it was tiered T2, not T1. Say why, in one sentence, and say what would upgrade it.

**3.** AT-037 says 30 to 50% of reported ROAS is 1-day view. Our ChiroWorks campaign read view-through at zero. Explain in two sentences why that is not a contradiction, and say what our reading does entitle us to claim.

**4.** A client's previous agency hands over a deck showing cost per lead improving from $15.33 to $14.00 month over month, and you discover the attribution window changed between the two months. Write the two sentences you would put in the report, and name the one pull you would run before writing them.

**5.** Someone proposes putting "open Compare attribution settings" on the Phoenix Truxx weekly list so we can finally state our own view-through share. Say what you would tell them, name the evidence, and then say what we would actually have to build to answer the question for that account.

Answers into `_answers-inbox.md`.

> [!note]- Answer key
>
> **1.** First, the report: a wider window credits conversions the narrower one did not credit, so the number improves with no change to the business. Second, the delivery: the optimiser is fed whatever the window counts, so feeding it view-through conversions pushes a prospecting ad set toward people who already visited the site, because a view-through can only fire for someone who already triggered the pixel. The rep's quote claims performance "in the business", which is the one thing neither change produces, and the operator reporting the quote says he has no data on it. Credit for naming that the delivery half sits at T4 ([[Attribution & Incrementality#AT-076|AT-076]]) while the reporting half is shown at T2 ([[Attribution & Incrementality#AT-012|AT-012]]).
>
> **2.** Because the surface was shown on camera and no TikTok documentation was quoted or shown, and our rule is that T1 requires the document itself. The upgrade is TikTok's own documentation of the Attribution Analytics report, which would move the existence of the report and its window ranges to T1. Nothing about performance moves with it, because TT-027 describes an instrument and not a result.
>
> **3.** The two readings measure different events on different populations: AT-037 is purchase events on 7 to 9-figure ecommerce brands, and ours is a single lead event on a local clinic at $643.85 of spend. A view-through can only fire for a prior site visitor, and a small local clinic campaign has almost no prior-visitor pool to harvest, so a near-zero share is what the mechanism predicts there. What we are entitled to claim is narrow and real: on that one campaign the 1-day setting under-counted by about 10% against 7-day click, so the window choice rather than the view window was the thing moving the number.
>
> **4.** Something close to: "Cost per lead reads $14.00 against $15.33, and the attribution window changed between the two months, so the two figures are not the same measurement and the movement cannot be read as performance. We are re-pulling both months on one window before we state a direction." The pull is both months on a single consistent window, ideally 7-day click, at the same level. If the account is Instant Form the window columns will dash, in which case say that plainly and compare raw lead counts and spend instead of inventing a window read. Credit for also checking whether the comparison crosses March 2026 ([[Attribution & Incrementality#AT-036|AT-036]]), which breaks the column's definition independently of anyone's settings.
>
> **5.** Tell them to retire the task rather than reschedule it. Evidence: on 26 August 2026 a within-account control on ChiroWorks rendered all four window columns as `—` on four Instant Form campaigns while a website-pixel campaign in the same view, same date range, same render, populated at 1-day click 42 and 7-day click 46. StayWell reproduced it on 216 populated leads, and the two obvious alternative explanations, an empty Results column and slow loading, were both tested and refuted. Event type is the variable, so fixing an optimisation event does not unlock it. To answer the question on Phoenix Truxx we would have to run a website-form campaign with real volume on that account and read the split there, which is a new build and a spend decision rather than a reporting click. Honest limit to state alongside it: this is T2 on our own data with no Meta documentation either way, so it should not harden into a law.
