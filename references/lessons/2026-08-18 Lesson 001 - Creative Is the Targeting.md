---
title: "Lesson 001: Creative Is the Targeting"
lesson: 1
topic: "Meta Delivery & Andromeda"
date: 2026-08-18
video: none (first video day is Wed 19 Aug. Corrected 2026-08-18: 20 Aug is a Thursday)
tags: [advertising-science, lesson]
---

# Lesson 001: Creative Is the Targeting

## The mechanism

For years, media buyers picked the audience: interests, lookalikes, age sliders. That machine is gone. Since Andromeda (December 2024), Meta's delivery system reads the ad itself, the words in the script, the person in the frame, the objection you answer, and decides from that content who should see it.

Here is the machine in three stages, and this comes from Meta's own engineering posts, not a guru ([[Meta Delivery & Andromeda|MD-022, MD-025, T1]]):

1. **Retrieval.** For every single impression opportunity, the system narrows tens of millions of candidate ads down to a few thousand. Andromeda made this stage 10,000x bigger in model capacity. It selects candidates by matching ad content to the person.
2. **Ranking.** Bigger models score those few thousand and pick the handful worth auctioning.
3. **Auction.** Bid times estimated action rate plus ad quality decides the winner ([[Auction Mechanics & Bidding|AU-001, T1]]). A more relevant ad beats a higher bid ([[Auction Mechanics & Bidding|AU-002, T1]]).

The analogy: Meta stopped being a postal service where you write the address on the envelope. It became a matchmaker who reads your letter first. You do not tell it who to deliver to. The letter itself does. Write "for dump truck owners tired of rented iron" and the matchmaker walks it straight to those men. Leave it generic and the matchmaker guesses, badly, with your money.

Three practical consequences:

- **The avatar callout is the targeting input.** Name the person, their situation, or their objection in the creative, and delivery routes to them (MD-001, T3, three independent operators agree). One verified case: the same product, re-shot for one specific avatar, cut cost per purchase from $73 to $35 at the same $1,000/day spend ([[Creative Science|CR-005, T2]]).
- **Near-duplicates are worthless.** Ads that look the same collapse into one entity ID and share identical delivery, zero extra reach. 200 lookalike variations can count as 20 real ads (MD-003, T3). Diversity has to live at concept level: different angle, different persona, different offer. Changing format (a static animated into video) does escape the collapse.
- **Your settings still matter at the edges only.** Location, minimum age, language, exclusions. That is the fence. Everything inside the fence, the creative decides.

## The evidence, in tiers

- T1: Meta's engineering posts describe content-based retrieval and semantic scoring of brand-new ads with no history (MD-022, MD-025).
- T2: the $73 to $35 avatar-niching case with ads-manager screenshots (CR-005); embedding-based delivery walkthrough sourced to Meta docs (MD-002).
- T3: the avatar-callout mechanism itself, agreed by Fraser Cottrell, Sam Piliero, and Matt Shiver from real spend, but nobody has published a controlled test. Strong hypothesis, not yet a proven law. This is exactly what our own accounts can upgrade.

## Our accounts

We have been obeying this law without naming it:

- **ChiroWorks / chiro statics:** our rule that the hook is the BODY PART (one condition noun, 6x size) is an avatar callout. "SCIATICA" is not decoration; it is the targeting input that tells Meta which sufferers to find.
- **SJR dump truck ads:** the Spanish volteo scripts speak to Beto, an owner-operator with a specific situation. That specificity is why ES dump delivers volume. A generic "trucks for sale" ad would enter far fewer of the right auctions.
- **Phoenix Truxx:** the $3.19 ES business-starter winner names the exact person (first-truck buyer starting a business). The creative did the targeting; the ad set was broad.

The upgrade path: when we next test creative, we treat avatar-niched versus generic as a real experiment and bank the numbers. That turns a T3 claim into OUR T2.

## The decision rule

Before any ad ships, ask: **which avatar does this creative name, in its first line and its imagery?** If the answer is "nobody in particular", the ad has no targeting. And never ship near-duplicate variations as if they were volume; they collapse into one entity.

## Quiz

Drop your answers in `lessons/_answers-inbox.md` (just "L001: 1) ... 2) ...").

1. Name the three stages an impression passes through and what each one does.
2. Why can an ad with a LOWER bid beat an ad with a higher bid, and which claim tier backs this?
3. A client wants to "scale" by duplicating their winning static 15 times with different headlines. What happens in the delivery system, and what should we do instead?
4. Scenario: ChiroWorks wants one ad that works for sciatica, knee pain, and neuropathy at once, to "reach more people." Using this lesson's mechanism, what happens to delivery, and what is the science-correct structure?
5. Our SJR cargo van EN ads slow down. A teammate proposes narrowing the ad set to "contractors, 30-55, interest: construction." What does post-Andromeda science say about that lever versus the creative lever, and what would you change first?

> [!note]- Answer key
> 1. Retrieval (tens of millions of candidates narrowed to a few thousand by matching ad content to the person), ranking (bigger models score those candidates), auction (bid x estimated action rate + ad quality picks the winner).
> 2. Because relevance is part of auction value: estimated action rate and ad quality are auction inputs alongside bid, so a more relevant ad can win at lower cost. T1, Meta's own auction documentation (AU-001, AU-002).
> 3. The 15 near-duplicates collapse into one entity ID and share the same delivery, so there is no extra reach, and the account looks diverse while the system sees one ad. Instead: build genuinely different concepts (new angle, persona, or offer), or change format, for example animate the winning static into video, which registers as a new entity.
> 4. One ad naming three conditions names nobody; retrieval has no clear avatar signal, so it matches weakly everywhere. Correct structure: three separate creatives, each with ONE condition as the dominant callout (our body-part hook rule), running broad, letting each creative find its own sufferers.
> 5. Interest narrowing is a fence adjustment on a system that mostly ignores fences, and it shrinks the auction pool without adding signal. The creative lever is the targeting lever. Change the creative first: name the contractor avatar and his situation explicitly in the hook, then let delivery stay broad. Settings-only fixes to a creative problem are pre-Andromeda thinking.
