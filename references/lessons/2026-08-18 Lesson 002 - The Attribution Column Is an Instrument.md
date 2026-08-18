---
title: "Lesson 002: The Attribution Column Is an Instrument, and the Instrument Changed"
lesson: 2
topic: "Attribution & Incrementality"
date: 2026-08-18
video: none (Tuesday. Next video day is Wed 19 Aug)
tags: [advertising-science, lesson]
---

# Lesson 002: The Attribution Column Is an Instrument, and the Instrument Changed

Today's topic comes from the research run, not the rotation. Yesterday's harvest banked two attribution claims that change how we write reports, so we teach those.

## The mechanism

Meta does not know which ad caused a conversion. It records touches, then applies a rule that decides which touch gets the credit. That rule is the attribution setting. It has two parts: the window (how long after the touch a conversion still counts) and the touch type (a click, or a view).

The default is 7-day click, 1-day view. Every lead number you have ever put in front of a client is the output of that rule, not a measurement of reality.

Around March or April 2026, Meta rewrote what the word "click" means inside the 7-day-click column. Before the change, any click on the ad unit counted: the like button, a comment, a share, a click through to the Page. Almost nobody knew that. Meta narrowed the definition to outbound clicks only and moved the engagement clicks into a new bucket called 1-day engaged view. Same ads, same buyers, same spend. The 7-day-click column stepped down overnight (AT-036, T3).

The analogy that maps: your bathroom scale gets a firmware update that stops counting your clothes. Monday you weigh 74kg. Tuesday you weigh 72kg. Plot the line across the update date and it looks like you lost 2kg in a night. The firmware moved. You did not.

Two operator consequences, and the first one is client-facing:

1. A step-down in 7-day-click performance dated to that window is a definitional artefact. Never report it as a decline. Any year-over-year or before-and-after comparison on that column that spans roughly March 2026 is broken. This is now house law 10.
2. 7-day click alone counts less than it used to, which is why Blue Sense reads it paired with 1-day engaged view instead of bare.

The same harvest banked a second one. Incremental attribution.

Most advertisers believe the setting holds out 10% of their own users in real time and reads the difference. Here is what the source describes instead: Meta takes conversion-lift experiments run by other advertisers in your niche, reads how incremental those campaign types were, and applies that factor into your account (AT-035, T3; mechanism at MD-034, T3). No holdout group runs inside your ad account. The arithmetic he gives for what the factor represents: a 2% purchase rate in the exposed cell against 1% in the holdout turns a reported 5 ROAS into a real 2.5.

The analogy: a doctor tells you your ten-year heart-attack risk is 12%, from a study of ten thousand men your age. Real information. Useful for deciding what to do. You would not tell your insurer that 12% was measured in your blood.

Hold the contested part honestly. The same speaker, in a different video, describes incremental attribution as a live 10% user holdout with a difference-in-differences calculation. That contradicts his own quote above. Both sides are banked in the codex. Neither is T1. When a source disagrees with itself, you say the tier out loud and you do not build a client promise on it.

## The evidence, in tiers

- **AT-036 (T3)**: the click redefinition. One credible operator, no platform changelog on file. Strong enough to change our reporting language, not strong enough to call a law of the machine. If we ever find Meta's own note on it, this becomes T1.
- **AT-035 (T3) + MD-034 (T3)**: incremental attribution provenance. Contested inside the source itself.
- **AT-008 (T2)**: compiled meta-analyses of Meta lift tests put 7-day-click underreporting of true contribution at roughly 10-20%. Click-based reporting is broadly honest and slightly conservative. This is the claim that keeps us calm.
- **AT-012 (T2)**: shown case, 427 message conversions, 390 from 7-day click, 37 (about 10%) from view-through, left running. Second shown case with Ads Manager screenshots: switching the column to 7-day click alone dropped ROAS from 2.14 to 1.68 and attributed revenue from about $79k to about $62k in one month. Roughly $17k of over-attribution.
- **AT-037 (T3)**: across a stated 1,000-plus audits, 30-50% of reported ROAS comes from 1-day view alone. This contests AT-012's 10% tolerance. Both stay on file. Worth noticing that the one case with screenshots landed at a 21% cut, below the recited band.
- **AT-001 to AT-004 (T2)**: Haus geo-holdout tests of incremental attribution against standard. Ratio of 0.8x in the 2024 to July 2025 sample, 1.26x in the July 2025 to July 2026 refresh. DTC-only brands up to 38% better.

Read that list again and notice the shape. The claims about how the number is built are T2. The claims about what Meta secretly did are T3. Confidence should follow.

## Our accounts

Start with the honest part. Every account we run is lead-gen. Phoenix Truxx on CPL, SJR Commercial on CPL per engine, Chiropraise on CPL for the free consult, ChiroWorks on CPL for the $0 consult, MG Fit Bod on cost per booked call. Zero accounts optimise to purchase. Zero accounts report a measured ROAS. So the ROAS inflation numbers above are other people's numbers, and view-through inflation is a smaller problem for us than for a DTC brand.

What is actually ours:

- **We have never run the comparison.** Compare attribution settings has not been opened on a single one of the five accounts. Nothing in the vault records a 7-day-click versus 1-day-view split for any client. We do not know our own view-through share anywhere. That is a gap, not a finding, and it is the cheapest thing on this list to close.
- **ChiroWorks, the client-side audit** (ad spend 24 Jun to 23 Jul 2026, CRM outcomes 10 to 24 Jul): $818 spend, 23 leads, $35.57 CPL, 3 booked, $272.72 per booking, 0 attended. Conversions API not connected. Meta Opportunity Score 60 out of 100.
- **The bigger ChiroWorks problem is upstream of attribution.** Meta has only ever received one signal from that account: a form was submitted. No booking event, no attendance event, ever sent back. The algorithm has been optimising to the cheapest form fill for the entire history of the account. Attribution windows decide what the report says. The results column decides who Meta goes and finds (law 6). Fixing the second one is worth more than tuning the first.
- **9 of 24 ChiroWorks leads, 37.5%, were already in the CRM**, aged 169 to 1,979 days. That is the lead-gen cousin of view-through inflation. We paid to re-capture people already in the building, and the report counted them as new.
- **Incremental attribution has never been enabled on any client.** At ChiroWorks' $50/day it is unreadable, and we govern on cost per booked and cost per show instead. That decision is already on file and this lesson supports it.
- The SJR performance thesis already carries the right instinct in writing: switching attribution settings mid-flight breaks comparability.

One number to treat carefully: Meta's own audit estimates CAPI would cut cost per quality lead by 24% on ChiroWorks. That is Meta's estimate of its own product, so it belongs in an internal note. It does not belong in a client report as a forecast.

## The decision rule

**State the window and the event beside every number you report, never compare a 7-day-click figure across March 2026, and never quote incremental attribution to a client as a measured lift.** When you do change an attribution column, change it once, write down the date, and report both readings for one overlapping period so the client can see the seam.

## Quiz

Drop your answers in `lessons/_answers-inbox.md` (just "L002: 1) ... 2) ...").

1. What changed inside Meta's 7-day-click column around March to April 2026, and where did the removed clicks go?
2. Incremental attribution: what do most advertisers assume it does, what does our banked source say it actually does, and what tier is that claim? Say why the tier matters here.
3. A client's 7-day-click cost per lead looks 30% worse in May 2026 than in February 2026. Name the first thing you check, the claim ID you are leaning on, and the sentence you will not write in the report.
4. You open Compare attribution settings on Phoenix Truxx for the first time and 40% of leads are coming from view. Walk through what you do, in order, before anything reaches Ruddy. Two of our banked claims disagree about whether 40% is alarming. Name both and say how you handle the disagreement.
5. ChiroWorks: 23 leads at $35.57, 3 booked, 0 attended, CAPI not connected, and Meta has only ever received "form submitted". Rank these three fixes and justify the top one with a law: (a) tighten the attribution window for reporting, (b) connect CAPI and send booking plus attendance events back, (c) ask Meta for a longer attribution window to catch more credit.

> [!note]- Answer key
> 1. "Click" was narrowed to outbound clicks only. Likes, comments, shares and clicks through to the Page were removed from 7-day click and re-housed under a new 1-day engaged view bucket. The column stepped down with no change in real performance (AT-036).
> 2. Assumption: Meta holds out about 10% of your own users live and reads the difference. Banked source: Meta applies a factor derived from conversion-lift experiments run by other advertisers in your niche, so it is directional evidence about your category (AT-035, T3, with MD-034). Tier matters because T3 cannot decide anything on its own, and this particular T3 is contested by the same speaker elsewhere, so it can inform a bet and can never be quoted to a client as measured.
> 3. Check whether the comparison spans the March to April 2026 click redefinition, since a step-down dated there is a definitional artefact (AT-036, house law 10). The sentence not to write: any version of "performance declined" or "the ads got worse" based on that column across that seam. Report the window change first, then compare like-for-like on a window that did not move.
> 4. Order: confirm the split in Compare attribution settings rather than guessing, check how much of the view-through sits on people already in the CRM, then re-read the account on 7-day click alone and see what survives. Only then decide, and if we act, duplicate the ad set without view attribution rather than editing the live one, because a significant edit resets learning (LS-002/LS-003, T1). The disagreement is AT-012 (T2, about 10% view-through is tolerable, more is a rebuild trigger) against AT-037 (T3, 30-50% is typical across audits). Handle it by tier: the T2 shown case outranks the T3 recited band, so 40% is worth investigating, and we report it as a finding with both claims named rather than as an emergency. Nothing goes to Ruddy until we have the actual split in front of us.
> 5. (b) first, by a distance. Meta has been optimising to the cheapest form fill for the account's whole history because that is the only event it has ever received, and the results column IS the targeting (law 6, LS-008). Sending booking and attendance back changes who Meta looks for, which moves the 0 attended number. (a) second: it improves the honesty of the report and costs nothing, and it changes no delivery. (c) last, and really never. A longer window collects more credit without creating a single additional patient, and on an account with 0 attended appointments, more credit is the opposite of the problem.
