---
title: "Lesson 066 - The Event Picks The Winner, Not The Ads"
type: lesson
lesson: 66
date: 2026-10-31
topic: Learning & Signal
claims: [MD-187, LS-008, LS-026, LS-022, LS-081, MD-093, LS-007]
tags: [advertising-science, lesson, learning-signal, optimisation-event, creative-ranking]
---

# Lesson 066 · The Event Picks The Winner, Not The Ads

Topic: Learning & Signal, taken from the rotation. This morning's research pass had nothing banked, so this lesson goes to the oldest sharp claim in the queue: [[Meta Delivery & Andromeda#MD-187|MD-187]], banked 24 October, waiting seven days. It belongs here rather than in Meta Delivery, because what it is really about is the optimisation event. No video, Saturday.

## 1. The mechanism

You already believe the optimisation event decides who sees your ads. Pick purchase, Meta goes looking for buyers. Pick form fill, Meta goes looking for form fillers. That half has been in this codex for months.

Here is the half Meta added on 21 October, in its own words:

> "None of this replaces the creative. It decides which creative wins. Brief the auction for volume and it finds the ad that brings cheap orders. Brief it for value and it finds the ad that brings big ones. Same ads, same budget, different winner, because you changed what winning meant."

Read the fourth sentence again. Same ads. Same budget. Different winner.

So the leaderboard you pull every Monday, the one that says Box Truck v2 is your best unit and the 26 ft box is your worst, is not a property of those ads. It is a property of the ads **and** the event. Change the event and the order changes, and nothing about the ads moved.

The normal-life version. Hand five chefs the same kitchen and say "feed the most people". You get a rice guy. Say "charge the most per plate" and the same five chefs, same kitchen, same ingredients, hand you a different winner. Nobody got better at cooking. You changed the brief, and the brief is what ranks them.

Meta's closing line is the whole posture: "The auction will do exactly what you asked. That's the good news and the bad news, and it's the same news."

## 2. The evidence

This is **T1 for the sentence** and nothing more. Meta describing its own selection behaviour in a best-practice post. No number, no sample, no test, no before-and-after. Learn to say that out loud when you cite it, because the tier is doing real work here.

What makes it worth banking anyway is that it is the first-party version of two things we only had as assertions. [[Meta Delivery & Andromeda#MD-093|MD-093]] carries Nick Theriot's pool-swap claim, that Meta holds users in event buckets and your event decides which bucket you are shown to, and Charley T's amplification law, that Andromeda executes the objective more literally each quarter so a shallow event degrades harder than it used to. Both practitioner, both asserted, nothing shown. Meta now states the same mechanism and adds the step neither operator took: the event re-ranks your existing creative against each other.

Three claims around it you should hold at the same time:

- [[Learning & Signal#LS-008|LS-008]], whatever hits the results column IS the targeting. Today's lesson is its creative twin.
- [[Learning & Signal#LS-026|LS-026]], optimise on the event that clears learning and judge creative quality at a separate layer. That rule now has a mechanism underneath it instead of just good manners.
- [[Learning & Signal#LS-081|LS-081]], the Results column is not a unit. One account printed four different events in it in a single week.

And the precondition Meta skips. Its volume-versus-value framing assumes you can choose value. On a lead-gen book optimising for form fills, you cannot. **So on our accounts the claim reads narrower: the event re-ranks creative wherever the event differs, and the volume-against-value version is unavailable until a value signal exists in the account.** We have no value signal on any live account today.

## 3. Our accounts

We did not just run into this. We already lost a decision to it, and the numbers are filed.

**Phoenix Truxx, September 2026.** Two campaigns ran side by side. The image lane's ad sets counted a lead as an instant-form submission **plus** any pixel or Conversions API Lead event, and a GoHighLevel workflow was echoing every form submission back as a website Lead. The dump lane counted instant-form submissions only. Two lanes, two definitions of the word lead.

What that did to the leaderboard:

| Read | Image against video gap |
|---|---|
| Ads Manager, echoed count | images about **2x cheaper** |
| Real people in the CRM | **16%** |
| Per qualified buyer | **the same** |

Ads Manager said 706 leads at $8.18 for the month. Real people first-touched by our ads: **417 at $13.86**. The image lane reported **230 website leads against 222 landing page views**, which is more sign-ups than page loads. **The video campaign was paused on the 2x read.** On real people there was almost no gap at all.

SJR Commercial sat in the same trap the same month: a draft monthly at 809 at $4.07 for the van and dump lanes, against **358 real people at $9.19**, with the cargo van campaign showing 390 website leads against 237 landing page views.

Separate the two limbs honestly, because they are not the same thing. The **counting** limb is a measurement defect, and it is why the number was wrong. The **optimisation** limb is MD-187, and it is why the ranking was wrong: the two lanes were briefed on different events, the image lane's optimiser chasing an event that contained an echo of itself, so the two lanes found different winners. It got the ranking wrong, and the ranking is what paused the video campaign. The echo is still live. The 23 to 29 October pull still matched 66 lead actions against 16 real ones on that lane.

The same account states the consequence in buyer quality. September 1 to 20: the image campaign's opt-ins were **53% people starting or with no business** against **35%** on the video campaign. Same offer, same dealership, different brief, different people.

ChiroWorks wrote the sentence three months before Meta did, in our own 24 July attribution audit: the algorithm is optimising for the cheapest form, and **the cheapest form is not the cheapest patient**.

**Where the claim cannot be tested on our book, and this is the finding.** We have never changed an optimisation event on a live account while holding the creative still. The nearest thing is StayWell's 20 October form swap, Schneider Form 03 and Binder form 10, and that changed the form's questions rather than the event, with **no cliff in volume** at the swap. So MD-187's central prediction is untested here and the test is cheap.

Also worth knowing: MetaTechAI's documented event is a server-side Lead on application submit, deliberately chosen and written down with its price attached. That is the one account where we briefed the auction on purpose.

## 4. The decision rule

**A creative leaderboard is only valid inside one optimisation event, and the event includes what counts as a conversion. Before comparing two ads, two ad sets or two lanes, confirm they are optimising on the same event with the same definition. If they are not, there is no leaderboard and the comparison does not get made.**

The corollary, and it is the expensive one: any before-and-after on a creative batch that spans an event change is void. Not weak. Void.

## 5. Quiz

Answers go in `_answers-inbox.md`.

**Q1.** State MD-187 in one sentence, then state its tier and exactly what evidence sits behind it. Say what the codex held before Meta published this, and who held it.

**Q2.** Meta's volume-versus-value framing does not apply to our accounts as written. Say why, and give the narrower version of MD-187 that does apply.

**Q3.** Applied. Phoenix Truxx, September. The echoed count made images look 2x cheaper than video and the video campaign was paused. Split the failure into its counting limb and its optimisation limb, say which limb MD-187 is, and say what each limb got wrong. Then name the number that proves the count was impossible.

**Q4.** Applied. A teammate pulls last week's Phoenix leaderboard, sees Box Truck v2 at $13.36 beating the 26 ft box at $18.40, and proposes building four more Box Truck statics. Both ads live in the statics lane. Name the one thing you check before agreeing, say why MD-187 makes it a gate rather than a nicety, and say what you do if the check fails.

**Q5.** Applied. Design the cheapest possible test of MD-187 on our own book. Name the account, what you change, what you hold still, what you read, and how long you hold it. Then name the reason we cannot run the volume-against-value version of the test at all.

> [!note]- Answer key
>
> **A1.** One sentence close to: the optimisation event decides which of your existing creatives wins, not only who gets reached, so the same ads on the same budget produce a different winner when the event changes. Tier: T1 for the sentence only. Evidence behind it: nothing. Meta describing its own selection behaviour in a best-practice post dated 21 October 2026, with no number, no sample, no test and no comparison. Before this the codex held the audience half only, at MD-093: Theriot's event-bucket pool swap and Charley T's amplification law, both practitioner, both asserted with nothing shown. Credit for noting that Meta added the step neither operator took, which is the re-ranking of creative against each other.
>
> **A2.** Meta's framing assumes the operator can choose a value objective. Every live account we run optimises for a form fill and has no value signal in it, so the volume-against-value comparison is not available to us. The narrower version: the event re-ranks creative wherever the event differs, whatever those events are, and the value limb stays parked until a value signal exists in an account. Deduct for any answer that treats this as a reason to go and switch an account to value optimisation, because nothing in MD-187 is evidence that value performs better.
>
> **A3.** Counting limb: the image lane's Leads column counted instant-form submissions plus a CRM echo of those same submissions arriving back as website Lead events, so the number was roughly doubled. It got the cost wrong, 706 at $8.18 against 417 real people at $13.86. Optimisation limb, which is MD-187: the two lanes were briefed on different events, the image lane's optimiser chasing an event that contained an echo of itself, so the two lanes found different winners and were never on one leaderboard. It got the ranking wrong, and the ranking is what paused the video campaign. The impossible number: 230 website leads against 222 landing page views. A page cannot sign up more people than load it. Full credit also for the SJR pair, 390 against 237.
>
> **A4.** Check that both ads sit in ad sets optimising on the same event with the same definition, which on the statics lane means checking whether the CAPI echo is still inflating one side. It is a gate rather than a nicety because under MD-187 a different event produces a different ranking, so if the definitions differ the $13.36-against-$18.40 ordering is not a fact about those two ads and cannot support a creative decision. If the check fails: do not make the comparison, do not build on it, fix the event definition first, and say in the report that the lane's ranking is unreadable until then. Credit for naming that this lane already carries filed confounds on language, format and campaign age, so the event is the third.
>
> **A5.** A reasonable design: Phoenix Truxx, one lane, change only the conversion event or its definition, for example removing the Conversions API echo step so the statics lane counts instant-form submissions only, exactly as the filed fix prescribes. Hold still the creative set, budget, geo, placements and audience. Read which ads take the spend and in what order, before and after, not the blended cost. Hold it long enough to clear a resettle and accumulate a readable number of events, which on our volumes is a week minimum and the filed editing floor is 10 days. Why the value version is impossible for us: no account has a value signal, so there is no value objective to switch to. Credit for naming that removing the echo roughly doubles the reported cost per lead overnight and the client has to be told first, and extra credit for noting the pre-change ranking must be captured before the change, because afterwards it cannot be reconstructed.
