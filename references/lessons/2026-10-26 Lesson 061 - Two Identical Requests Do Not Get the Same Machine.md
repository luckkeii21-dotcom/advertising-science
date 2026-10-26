---
title: "Lesson 061 - Two Identical Requests Do Not Get the Same Machine"
type: lesson
lesson: 61
date: 2026-10-26
topic: Meta Delivery & Andromeda
tags: [advertising-science, lesson, meta-delivery]
---

# Lesson 061 - Two Identical Requests Do Not Get the Same Machine

Video: `video/2026-10-26-lesson-061.mp4`

Topic: Meta Delivery & Andromeda. Taken from the rotation at index 0. This morning's research pass had written nothing at topic-lock, so there was no harvest to teach.

## 1. The mechanism

You have been taught that your ad is scored against a person. That is roughly true and it hides the part that matters. The scoring is not one act. It is split in time, split across machines, and the amount of work spent on it changes minute by minute.

Here is the shape Meta published for itself in August and October 2026.

**The person is written up first, and your ad is not in the room.** An offline model reads thousands of events of someone's history, asynchronously, with no latency pressure, and saves a compressed description of who they are. Meta's own sentence: the upstream model "strictly separates user features from ad and context features to ensure user embeddings remain independent of any particular ad candidate." That description is finished and cached before your ad exists.

**The pairing is also precomputed, in the background.** Once live ranking narrows a request to its top few candidates, a second system scores those exact user-and-ad pairs with the big model in background jobs that carry no deadline, then hands the answer to the serving path just in time. Meta says running the big model inside the live request "is not affordable", so it moved the work in time rather than cutting it.

**When the pairing is missing, nothing fails. It degrades.** Quoted in full, because this is the part operators get wrong: "When an exact user-ad embedding is unavailable, the system degrades rather than drops. It substitutes an aggregate of the user's own recent embeddings across the same ad groups, or borrows from behaviorally similar users."

**And the depth of the whole process is not a constant.** Meta runs part of ads ranking on spare capacity it can take back at any moment. Two levers spend that surplus: one ranks more candidates, one sends a higher share of requests to a more powerful model. Both are governed by controllers watching tail latency, and when capacity contracts the optional work is dropped within milliseconds. Meta states the reason the better model is not always on: "it's not efficient to use them for every request with dedicated capacity."

The analogy that actually maps is a hospital at night.

The patient's notes were written up in advance by a different team, before anybody knew what today's complaint would be. A result for this exact patient and this exact test is usually pre-ordered and waiting. When it is missing, nobody sends the patient home: the doctor uses that patient's recent similar results, or what patients like them normally show. And how much attention the case gets depends on how busy the ward is in that minute. The same patient, with the same complaint, gets a consultant at 3am and a junior at 9am. Nothing about the patient changed.

Your ad is the complaint. The ward's workload is not yours to set.

## 2. The evidence

All five of today's claims are T1, meaning Meta's own engineering publications, read in full and quoted rather than summarised. That is unusually clean ground for this codex, which is 69% T3.

- [[Meta Delivery & Andromeda#MD-119|MD-119]], T1. The offline-user-model and online-ranking-model split, and the sentence that the cached user embedding is ad-agnostic. Meta's 5 August 2026 post.
- [[Meta Delivery & Andromeda#MD-179|MD-179]], T1. Solaris precomputes the user-ad score before the request needs it, and the degradation rule quoted above. 13 October 2026.
- [[Meta Delivery & Andromeda#MD-174|MD-174]], T1. Ranking runs partly on reclaimable idle capacity, so ranking depth varies. 12 October 2026.
- [[Meta Delivery & Andromeda#MD-175|MD-175]], T1. The better model is routed by predicted likelihood of engagement, and exploratory traffic is preserved in every segment permanently.
- [[Meta Delivery & Andromeda#MD-180|MD-180]], T1. Prediction quality follows a power law in how much engagement history the model reads, and larger models gain disproportionately from longer histories.

Two guards come attached to these claims, and they are the reason the codex is worth reading rather than skimming.

**MD-179 forbids one translation.** Meta's phrase "the same ad groups" is not an Ads Manager object. Nobody may map it onto ad sets or campaigns. The honest read is that a pair with no history inherits an aggregate at some grouping level Meta did not define. If you hear anyone turn that into "launch new ads inside an old ad set so they inherit its score", that is an invented mechanism and the claim says so.

**MD-175 forbids the other one.** "Predicted likelihood of user engagement" is an internal signal with no event, no window and no account-visible field, and Meta does not say whether your optimisation event enters it. There is nothing here that tells you how to get your requests into a better-served segment. It is evidence about the machine, not a dial.

A third claim sits one tier down and is worth holding beside these. [[Meta Delivery & Andromeda#MD-090|MD-090]], T3, a Meta employee on stage with no data shown, says compute is allocated heavily to people with long interaction histories and thinly to people the system barely knows. T1 and T3 pointing the same direction is still only T1 plus a hint, so treat the direction as supported and the magnitude as unknown.

## 3. Our accounts

Here is where this gets uncomfortable, and the discomfort is the lesson.

Our book is small enough that ranking-depth volatility is invisible on it. Lesson 059's filed table: SJR Commercial took 95 opt-ins on $779.67 for 16 to 22 October, $8.21 each. Phoenix Truxx took 95 on $1,336.39 for 9 to 15 October, $14.07 each. StayWell took 18 on $537.61, $29.87 each. ChiroWorks took 17 on $463.28 in its last live week before it went dark on 14 October, $27.25 each.

Meta's serving fleet handles over 400 billion requests a day ([[Meta Delivery & Andromeda#MD-129|MD-129]], T1). SJR at about $111 a day is a rounding error inside that. We are not large enough for the capacity question to show up as a line we can read. We are exactly large enough to be moved by it and never know.

That has one immediate consequence for how we talk about short windows. No ad on our book has ever exceeded about $66 in a day. A two-day read on one ad on one of our accounts sits inside a system where the same request can receive materially different amounts of ranking work depending on fleet load that minute. The creative may be the cause of the difference. So may the ward being busy. At our volumes nothing in the export separates them.

MD-180 also leaves us a gap that is genuinely ours. Our clinics and our truck dealers sell to tradesmen and to people with back pain, which is to say light platform users rather than heavy brand-engagers. If the published platform gains concentrate where engagement history is deep, our book inherits the least of them. Nothing on file measures whether our own results differ by how platform-active the buyer is. We have never checked, on any account, ever.

What has not changed is what we can touch. The creative ([[Meta Delivery & Andromeda#MD-001|MD-001]], [[Meta Delivery & Andromeda#MD-120|MD-120]]) and the quality of the signal the account returns. That is still the whole list.

## 4. The decision rule

**A difference between two short windows on the same creative, same audience and same budget is not evidence about the creative, because the amount of ranking work spent on those windows was not the same.**

Practically: when an ad reads better this week than last with nothing changed, the first sentence out of your mouth is not a creative explanation. It is "how many events is this built on". Then size the window until the number can carry a verdict. The machine's own variance is now a documented reason to widen the window, not a vibe.

## 5. Quiz

Drop your answers in `_answers-inbox.md`, lesson number at the top.

**1.** Meta says the cached user embedding is built with no knowledge of any particular ad candidate. Which claim is that, what tier, and what does it mean for the order in which the two halves of a match get computed?

**2.** State MD-179's degradation rule in your own words, then name the one translation of it the claim explicitly forbids and say why the ban is correct.

**3.** Why does Meta not simply route every request to its more powerful ranking model? Quote or paraphrase its stated reason.

**4.** Applied. An SJR Commercial ad ran 9 to 11 October and read $6.90 per opt-in on 7 opt-ins. The same ad, untouched, ran 16 to 18 October and read $11.40 per opt-in on 5 opt-ins. A teammate writes in the weekly that the creative is fatiguing. Give two reasons from today's claims why that sentence is not yet supported, and name the one thing you would do before anybody writes a fatigue line.

**5.** Applied. A client asks you to promise their account will get Meta's published 18.9% conversion improvement. Their buyers are tradesmen who use Facebook twice a week. Answer them in three sentences, naming the claim and tier that governs your answer, and say what you would measure to replace the promise.

> [!note]- Answer key
> **1.** [[Meta Delivery & Andromeda#MD-119|MD-119]], T1. It means the description of the person is computed and cached FIRST, independently, and the ad-specific work happens later in the online stage through target-aware attention over that cached representation. The person's half of the match is finished before your ad is considered at all. Credit for quoting the separation sentence.
>
> **2.** The rule: when the exact user-ad score is unavailable, the system substitutes an aggregate of that user's own recent embeddings across the same ad groups, or borrows from behaviourally similar users, rather than dropping the candidate. The forbidden translation: mapping "ad groups" onto Ads Manager ad sets or campaigns, and therefore recommending that new ads be launched inside established ad sets to inherit a score. The ban is correct because "ad groups" is Meta's internal taxonomy, the post does not define it, and no Ads Manager object carries that name. Acting on the mapping would be acting on a mechanism Meta did not describe. Full credit also notes MD-179 quantifies nothing, so even the real effect has no published size.
>
> **3.** Because it is not efficient to use the powerful models for every request with dedicated capacity ([[Meta Delivery & Andromeda#MD-174|MD-174]], T1). The powerful model runs on surplus capacity that is preemptible and volatile, and coverage is set by a controller watching tail latency. Credit for adding from [[Meta Delivery & Andromeda#MD-175|MD-175]] that routing is by predicted engagement and that the allocation is re-measured continuously rather than fixed.
>
> **4.** Two reasons, either pair accepted. First, 7 opt-ins against 5 opt-ins is not a sample that can carry a verdict on anything, so the difference is inside noise before any mechanism is invoked. Second, MD-174 (T1) says the depth of ranking applied to a request is not a constant, so two identical windows can receive materially different amounts of ranking work from fleet load alone, and no export we hold separates that from a creative effect. The thing to do first: widen the window until the event count can support a verdict, and read the ad's own frequency rather than the account's, per [[Meta Delivery & Andromeda#MD-138|MD-138]]. Deduct for answering only "small sample" with no claim cited. The point of the lesson is that the machine's own variance is now documented.
>
> **5.** Refuse the promise, and say why in the client's own terms. The published figure is a platform-wide average, and [[Meta Delivery & Andromeda#MD-090|MD-090]] (T3) plus [[Meta Delivery & Andromeda#MD-180|MD-180]] (T1) both say the gains land heaviest on people with long engagement histories, which is not this client's buyer. So the honest position is that this account should expect to inherit less than the average implies, with no published number for how much less. What to measure instead: this account's own cost per opt-in over a window long enough to carry it, against its own history, which is the only benchmark that was ever about them. Full credit for naming T3 as the weaker half and refusing to put a number on the shortfall.

Sources for every claim cited: Engineering at Meta posts of 2026-08-05, 2026-10-12 and 2026-10-13, read in full and banked in [[Meta Delivery & Andromeda]].
