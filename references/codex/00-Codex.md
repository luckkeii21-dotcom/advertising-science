---
title: "Advertising Science Codex"
type: moc
created: 2026-08-18
tags: [advertising-science, codex, moc]
---

# Advertising Science Codex

The permanent, growing record of how modern advertising actually works. Every entry is a **claim** with an evidence tier, sources, and a status. We bank claims, not videos: new sources merge into existing claims, contradictions are stored, nothing is silently overwritten.

## Evidence tiers

| Tier | Meaning | Trust level |
|---|---|---|
| **T1** | Platform documentation or engineering publication (Meta engineering blog, Google docs) | How the machine is built |
| **T2** | A real test with shown data (ours or a practitioner's) | Verified behavior |
| **T3** | Practitioner claim from real spend, no shown test | Experience, treat as strong hypothesis |
| **T4** | Theory or reasoning, untested | Idea only |

Our own client accounts are the T2 upgrade path: when we test a T3 claim on SJR, Phoenix, ChiroWorks, StayWell/Chiropraise, or MetaTechAI and it holds, it becomes T2 with our numbers.

## Claim statuses

`active` (current best knowledge) · `contested` (credible sources disagree, both sides recorded) · `superseded` (replaced by a newer claim, kept for history) · `refuted` (shown false, kept so we never relearn it).

## Topics

- [[Meta Delivery & Andromeda]]: retrieval, ranking stages, GEM, why creative is targeting now
- [[Auction Mechanics & Bidding]]: total value equation, bids, cost caps, pacing
- [[Learning & Signal]]: learning phase, optimization events, signal quality, EMQ
- [[Creative Science]]: creative as the main lever, fatigue, volume, testing
- [[Scaling Models]]: budget scaling, consolidation, structure
- [[Attribution & Incrementality]]: what platform numbers lie about, holdouts, MER
- [[Google Auction & Smart Bidding]]: ad rank, quality score, tCPA/tROAS internals
- [[Google PMax & Shopping]]: PMax behavior, feeds, cannibalization
- [[TikTok Delivery]]: TikTok's auction and delivery system
- [[Emerging Channels]]: Pinterest, Snapchat, Reddit, Amazon, X, Applovin/Axon. Opened 2026-08-19. Everything in it is T3 or below, from operators whose main book is elsewhere
- [[Marketing Math & Unit Economics]]: LTGP:CAC, contribution margin, payback, forecasting

## Operations

- [[Channel Roster]]: who we harvest and why
- [[Watchlist]]: official platform pages we monitor
- [[Harvest Log]]: what came in, day by day
- Lessons live in `wiki/science/lessons/`
- Raw transcripts live in `wiki/sources/transcripts/<channel>/`

## Claim ID scheme

`<TOPIC>-<NNN>`: MD (Meta delivery), AU (auction), LS (learning/signal), CR (creative), SC (scaling), AT (attribution), GA (Google auction), GP (PMax/Shopping), TT (TikTok), EC (emerging channels), MM (math/economics). IDs are permanent; never reuse one.
