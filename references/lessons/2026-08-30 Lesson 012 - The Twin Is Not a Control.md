---
title: "Lesson 012: The Twin Is Not a Control"
lesson: 12
topic: "Attribution & Incrementality"
date: 2026-08-30
source: "harvest 2026-08-29 (AT-107 new at T3, promoted to law 23; AT-108 new). The 2026-08-29 research run finished after lesson 011 shipped, so nothing from it had been taught. Paired with our own ChiroWorks duplication audit and the StayWell July diagnosis."
video: none
tags: [advertising-science, lesson]
---

# Lesson 012: The Twin Is Not a Control

> Lesson 003 said an ad's own row is not the verdict. Lesson 011 said a starved row means nothing because it never bought a chance. This one is about the row that did buy its chances, sitting next to an identical row, and why the gap between them still tells you nothing.

## 1. The mechanism

Launch two ad sets. Identical ads, identical audience, identical placements, identical budget. Change nothing at all.

They still come apart. Not by a little. Duplicate one ad set many times and "some will perform terrible, some will perform incredible. It's just random."

The reason is that delivery is a search rather than a formula. Each ad set runs its own auctions, finds its own sample of people, at its own moments, and each one optimises separately from the moment it starts. Two searches beginning from the same place do not land in the same place.

Two checkout lanes at a supermarket have the same shape. Same till, same trained cashier, same queue rule. Open both at five o'clock and one clears forty shoppers in the hour while the other clears twenty five. Nothing about the lanes differed. One got three trolley shops and a price check. Read that hour as a test of the lanes and you retrain a cashier who did nothing wrong.

That is a duplicated ad set. The two rows differ before you touch anything, so a difference between them cannot be credited to the variable you changed.

Now the part that makes this a law rather than a caution. **The size of a normal gap has never been measured.** Nobody has duplicated one ad set fifty times and published the spread. So every single-pair ad set test sits on a noise floor of unknown height, including ours, including the ones already written into our reports.

What follows is narrower than "testing is hard." When a row differs from the row beside it, the work has not started yet.

## 2. The evidence

**AT-107, T3, active, banked 2026-08-29, promoted to law 23.** The operator states it while killing his own finding, which is why it is worth more than most T3. He ran 7-day click against 7-day click plus 1-day view as the optimisation setting, on a consistent attribution model, and measured the second one winning by a wide margin. He then refuses to bank his own result: "how do we know that that natural random noise that exists within duplications of identical ad sets isn't just presenting itself here and giving us a biased read? We don't. Therefore, it's not helpful." Do not go looking for his multiple. It is recorded in the codex only so nobody re-extracts it later as a finding.

**The ladder he gives instead.** Meta's own A/B experiment tool first, whose single real value is that it guarantees the two cells do not target the same people. Then repetition, at least ten to twenty runs pooled across accounts. Then a geo holdout for anything you intend to call causal. That is [[Attribution & Incrementality#AT-022|AT-022]]'s measurement hierarchy stated from the failure end.

**The half of AT-107 you will use most often is the reversion method.** A client made three changes in one week: checkout cross-sells, new site offers, an account restructure. Average order value rose 2% and conversion rate halved, from 4% to 2%. The team guessed the offers, killed them, nothing moved. Guessed the restructure, reverted it, nothing moved. Removed the checkout cross-sells and conversion rate returned to 4% immediately. The cross-sells, the change credited with the order-value win, were the thing destroying conversion rate. Serial reversion found it. Analysis did not.

**[[Scaling Models#SC-006|SC-006]], T3, Ben Heath, dated 2026-05-19.** A second reason a twin lies, and AT-107 never names it: "you have competing campaigns running alongside each other, you run into serious auction overlap issues." Two duplicates on the same geo bid into one pool.

**MD-148, T2, banked from our own filed reports on 2026-08-29.** Phoenix `Video02 English` took $0.63, produced nothing, was read as a loser, then returned 14 opt-ins on $23 once it was funded in its own campaign. Same family of error, different cause: a zero read as a verdict from a row that had bought no chances.

**Now the tier discipline, because law 23 is unusual.** It is T3. One operator, no distribution shown, and he is an agency owner describing his own client work, which is precisely the evidence class AT-107 itself warns about. It sits in the law layer anyway, and the reason is worth holding on to: **it does not add a fact to the codex, it sets a ceiling on how much weight every other claim in the codex can carry.** A T3 claim about measurement governs T2 claims about the world.

## 3. Our accounts

**ChiroWorks, and it cost us the cheapest ad in the account.**

Two ad sets, `All invisa ads | Open targeting | Collinsville, IL` and the same name with ` - Copy`, the copy created 21 July. Same creative in both. Same geo. Same open targeting.

| The ORIGINAL ad set | Spend | Opt-ins | Cost per opt-in | CTR | Click to opt-in | CPM |
|---|---|---|---|---|---|---|
| up to 26 Jul | $216.12 | 11 | **$19.65** | 0.99% | 16.4% | $32.06 |
| 27 Jul to about 7 Aug | $135.66 | 0 | none | 0.97% | 0.0% | $48.75 |

Then it went dark on its own, $0.00 across both the 8 to 16 Aug and 17 to 23 Aug weeks, status `not_delivering`. The copy went the other way, $58.38 for one opt-in, then $203.48 for five.

The reflex read is that the original died and should be killed. The original was the account's cheapest ad and the duplication killed it.

**Read the signature, because it is the tell.** CTR flat, 0.99% to 0.97%. Click to opt-in collapsed, 16.4% to zero. CPM up about 50%. Hook fatigue would have moved the CTR, and the hook kept working at an identical rate. What changed is who saw it, the original pushed onto the residual audience while its twin took the pool. Meta's own conversion-rate ranking agreed, moving from Average to Below average while quality ranking held at Average.

**And here is the arithmetic that settles which comparison to trust.** Both recomputed today as one-tailed Fisher exact tests.

- The ad's zero, 0 opt-ins on 27 clicks, against the ad beside it, 5 on 38: **p = 0.06**. That gap is inside normal variation. It proves nothing.
- The same zero against **its own earlier record**, 11 on 67: **p = 0.019**. That is real.

Identical data. The twin comparison could not see the thing the self comparison found immediately.

**The same account, one level up.** The client's July audit found all three bookings coming from contacts already in their CRM and none from the fifteen genuinely new opt-ins, at Fisher one-sided p = 0.042. We recomputed it and it is correct, 84/2024 = 0.0415. It also rests on three events. Move one booking to the other group and the same test returns p = 0.31. A p-value can be arithmetically perfect and still be a coin.

**StayWell, where reverting one thing at a time did the work.** July appointments fell from 10 to 2 while opt-ins fell 51 to 31. The reflex diagnosis was ad fatigue. So we plotted frequency against cost on the same timeline instead of assuming, and frequency **fell** from 2.23 to 1.74, a 22% drop, while cost per opt-in rose $8.16 to $26.97. In June the most fatigued ad in the account, at 2.10x, was also the cheapest at $4.71. Media was healthy on its own terms, $860.16 spent, 33 opt-ins, $26.07 each, inside band. The cause was the phone layer, where the agent booked 11 real appointments in June and 1 in July, quoted the wrong price on 24 of 70 calls, and hit a machine on 67% of dials.

**One number on our own book that nobody on the research roster publishes.** At StayWell's $26 cost per opt-in, an ad performing exactly at the account average still shows zero opt-ins at $50 of spend about 15% of the time, at $75 about 6%, and at $100 about 2%. That is a measured noise floor for a single ad, which is the one-ad version of the question AT-107 says is unanswered for two ad sets. It is why $50 triggers a review on that account and $75 is an automatic off.

## 4. The decision rule

**Judge an entity against its own history, never against the row beside it, and when several changes shipped together, find the cause by reverting them one at a time.**

## 5. Quiz

Drop answers in `lessons/_answers-inbox.md`. Lesson number plus your answers. Partial is fine and still gets graded.

**If you only answer two, answer Q2 and Q5.** Q2 is live on SJR and decides how the Phase 5 bench gets launched. Q5 is the guard that stops this lesson turning into an excuse to never test anything.

1. Law 23 is T3 and it sits in the law layer anyway. Explain why that is defensible, and state the one thing a T3 measurement claim is allowed to do to a T2 claim about the world. Then name the guard that applies to AT-107 itself.

2. **SJR, live.** The dump campaign runs $40 a day. `Caesar Dump Truck Ad` holds 63% of spend and its cost per opt-in has walked $3.20, $6.49, $8.70, $9.18 over four weeks. The Phase 5 bench is built and unlaunched. A teammate proposes duplicating the dump ad set, putting Caesar in one copy and the Phase 5 statics in the other, running a week, and reading the two rows. Give the two separate reasons that design cannot answer the question. One of them is AT-107. The other one we have already measured on our own book, so cite the evidence. Then say what you would do instead.

3. An ad shows 0 opt-ins on 27 clicks. The ad next to it shows 5 on 38. Its own record over the previous three weeks is 11 on 67. One comparison returns p = 0.06 and the other returns p = 0.019. Say which is which without looking it up, explain why the two answers differ so much on the same zero, and state what you would check in the account before accepting the significant result as a real change in the ad.

4. **StayWell, applied.** Appointments fell from 10 to 2 in a month. Frequency fell 22% over the same window. Write the order in which you would rule things out, and say why frequency gets read on its own timeline rather than assumed. Then say what serial reversion looks like on a funnel where the suspect changes sit in a phone system rather than in the ad account, and name the one thing that makes it harder there than in the checkout-cross-sells case.

5. AT-107 says a single-pair ad-set test cannot attribute a difference to the variable you changed, and its ladder starts at ten to twenty pooled runs and ends at a geo holdout. Every one of our accounts spends under $30,000 a month. Explain where that leaves us, and describe what we should actually do given that the correct method is out of reach. Name the failure mode of over-applying this lesson.

> [!note]- Answer key
> 1. **Why it is defensible.** A measurement claim does not add a fact to the model, it prices the confidence of every fact already in it. AT-107 says our commonest test design has an unmeasured error bar, which lowers the weight any conclusion drawn from that design can carry, whatever tier the conclusion was banked at. **What a T3 measurement claim is allowed to do to a T2 claim: discount it, never overturn it.** If a T2 claim was established on a duplicated-ad-set pair, law 23 says read it as directional. It does not say the finding is false. **The guard on AT-107 itself:** one operator, no distribution published, and it is an agency owner describing his own client work with no counterfactual, which is the exact evidence class AT-107 warns about. Full credit needs the discount-not-overturn distinction. Bonus for naming the honesty premium, that he states it while refusing to bank his own favourable result, which is the strongest thing about a T3 source.
> 2. **Reason one, AT-107.** Two duplicated ad sets diverge with no variable changed, the spread has never been published, and one week on one pair cannot separate the creative from the noise. **Reason two, and we have shown it, so cite it.** Same geo plus open targeting means the two cells bid into one auction pool. On ChiroWorks that did more than add noise, it degraded the original: CTR flat at 0.99% to 0.97%, click to opt-in from 16.4% to zero, CPM up about 50% to $48.75, then `not_delivering`. SC-006 is the claim and Heath's auction-overlap reasoning is dated 2026-05-19. **The cost of the proposed design is the whole $40 a day plus the destruction of the only asset currently producing opt-ins.** **What to do instead:** launch the bench in its own campaign, leave Caesar running in place, and read each asset against its own history rather than against Caesar's row. That is lesson 011's answer and MD-148's shown result on Phoenix. Full credit requires naming both reasons and refusing the duplication. Bonus for noting that at $40 a day split in two, each cell is $20 a day, so even a design without these two faults would be reading a cell that has bought roughly two chances at $9.18.
> 3. **p = 0.06 is the twin comparison** (0 of 27 against 5 of 38). **p = 0.019 is the self comparison** (0 of 27 against its own 11 of 67). **Why they differ:** the twin's rate is itself an estimate from 38 clicks, so the comparison carries the uncertainty of both rows and 5 successes is a thin baseline. The ad's own history carries 67 clicks and 11 successes, a rate it established over three weeks, so a zero on 27 clicks is being tested against something far better measured. Neither test knows anything about causes. **What to check before accepting the change as real:** whether anything launched or changed in the account on the boundary date, which on ChiroWorks was the ` - Copy` created 21 July. Also confirm the lead form and primary text are identical across the two ad sets before accepting any audience explanation, check delivery status because a `not_delivering` ad frees no budget when you pause it, and split the ad's spend at the change date rather than reading the whole window as one row. Bonus for saying the significant result tells you only that *something* changed, and that the audience explanation was earned by the CTR-flat, click-to-opt-in-collapsed, CPM-up signature rather than by the p-value.
> 4. **The order.** Confirm the number first, on tags rather than pipeline stage, because the desk re-stages people out of appointment stages and a stage snapshot undercounts older months. Then check media on its own terms, spend, opt-ins and cost per opt-in, which at $860.16, 33 and $26.07 came back healthy. Then plot frequency against cost on one timeline. Then walk the funnel stage by stage. **Why frequency gets plotted rather than assumed:** the fatigue story predicts frequency rising alongside cost, and it fell 22% while cost rose, so the timeline refutes the story rather than merely failing to support it. The June counter-example seals it, the most fatigued ad in the account at 2.10x was also the cheapest at $4.71. **Serial reversion on a phone system:** take the layers one at a time against a period when the number was good, agent prompt, pricing knowledge, name merge, dial timing, answer rate, changing one and watching one week. **What makes it harder:** you cannot revert a conversation. Ad-account changes restore to a known prior state, and a month of calls has already happened, so you are re-running a layer forward rather than restoring it, and the population is different every week. Bonus for naming a specific measurable per layer, for example real bookings, which ran 11 in June and 1 in July.
> 5. **Where it leaves us, and the honest position is to say so out loud.** Ten to twenty pooled runs and a geo holdout need spend we do not have on any account, and AT-022 puts incrementality at roughly the $10M a month tier. **What to do instead, in order.** Compare every entity against its own history, which is free, needs no cell structure, and found the real ChiroWorks answer at p = 0.019 when the twin comparison could not. Change one thing at a time so that when a number moves you already have the candidate list. Use Meta's own A/B tool when you genuinely need two cells, because audience separation is the one thing it does buy. Pool across accounts where the same question exists on more than one client, since five accounts gets closer to ten runs than one account ever will. And state directional reads as directional in every report. **The failure mode of over-applying this:** paralysis, refusing to act because nothing reaches proof. Law 23 governs what you may *claim*, not whether you may *decide*. We will keep making moves on weak evidence because the alternative is making them on none, and the discipline is labelling the evidence honestly and writing down in advance what would show the move was wrong. Bonus for noting we already own one number the roster does not, StayWell's zero-opt-in probabilities at $50, $75 and $100 against a $26 cost per opt-in, which is a measured noise floor for one ad and the model for what we could build for two ad sets if we ever pooled duplicates across clients.
