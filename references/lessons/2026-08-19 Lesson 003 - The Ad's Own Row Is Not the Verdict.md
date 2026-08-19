---
title: "Lesson 003: The Ad's Own Row Is Not the Verdict"
lesson: 3
topic: "Scaling Models"
date: 2026-08-19
source: "harvest (SC-085, SC-008 flipped contested; SC-007, MD-010)"
video: "video/2026-08-19-lesson-003.mp4"
tags: [advertising-science, lesson]
---

# Lesson 003: The Ad's Own Row Is Not the Verdict

> Today the science got *less* certain, not more. Law 3 flipped to contested this morning. That is worth a lesson on its own, because most of your career will be spent acting inside contested claims.

## The mechanism

Open any CBO and you see a table. One ad has most of the spend and a mediocre cost per result. A few ads have almost no spend and beautiful cost per result. Every instinct says: kill the expensive one, feed the cheap ones.

Those rows are not independent measurements. Meta distributes spend inside an ad set as a **sequence**, not a contest ([[Scaling Models|MD-010]], T3). One ad takes 75-90% of spend running top-of-funnel at a modest return. The small-spend ads show cheap cost per result because they are closing people the big ad already warmed up. The cheap ads' numbers are borrowed.

The analogy that actually maps: a restaurant with a guy outside handing out flyers and a waiter inside taking orders. Per interaction, the flyer guy converts almost nobody and the waiter converts nearly everybody. Fire the flyer guy for bad numbers and the waiter's numbers collapse too, because the waiter was never generating anything. He was finishing.

That is the whole idea. **The unit of judgment is the account, not the row.**

## The evidence, in tiers

Here is where it gets interesting, and where you learn to read tiers properly.

**The T3 contest, opened today ([[Scaling Models|SC-085]]).** Two credible operators, flat contradiction, neither shows data.

- *Kill it.* Professor Charley T, 2026-02-14: turn off the thing that hogs budget so the others get a chance. His argument underneath is worth respecting: a genuine winner lets you raise budget, so an account that cannot scale does not have winners worth protecting.
- *Leave it on.* Andrew Faris, 2026-05-27, across 100+ managed accounts: turning off a HIGH spender is close to never correct, 99%+ of cases leave it on. His first move on every account takeover is switching the previous buyer's paused high spenders back on, and he reports roughly 30% more spend at the same target from that alone.

**The T2 contest underneath it ([[Scaling Models|SC-007]]).** Both sides here *do* show data, which makes it the more serious disagreement.

- CTC, via Faris and Taylor Holiday, on billions in managed spend: manual on/off decisions made things neither better nor worse. They back-tested their own auto-kill rule (5x CPA, zero purchases) and found it non-beneficial.
- Nick Theriot, on a real account: $80k in 7-day sales, $4,000/day CBO, $50 target, campaign averaging $65. The top two spenders sat at ~$69 and he killed the ads at $76, $80 and $88.

They have never been tested against each other.

So: a T2 contest about whether the lever does anything at all, sitting underneath a T3 contest about which way to pull it. Read that honestly and you get humility, not paralysis.

**What survives on every side:**

1. **Judge at ad-set level, never on the ad's own row** ([[Scaling Models|SC-011]], T2, active). This is the strongest thing standing in the whole argument.
2. The resolving test is cheap and reversible: turn the top spender off for 2-3 days, read **account-level** cost per result, turn it back on if the account gets worse.

> [!warning] This section was rewritten six hours after it was drafted
> The first draft carried a third survivor: *killing LOW spenders is always safe*, conceded by both sides. **That clause broke tonight.** The second research pass of 2026-08-19 flipped [[Scaling Models|SC-009]] to contested. Blue Sense Digital calls killing the starved ads the category's biggest mistake and gives two mechanisms, both untested: the **assist** role, where a low-spend ad sits inside a conversion sequence another ad closes, and the **reserve** role, where Meta rotates delivery back into starved ads once the winner fatigues.
>
> The likely reconciling boundary, and nobody has tested it: Theriot only kills once cumulative spend has actually accrued against zero purchases, so a genuinely zero-spend ad costs nothing to keep. A true $0 ad is free optionality. An ad that has quietly eaten a few hundred dollars at zero conversions is a measured loss.
>
> Read this as the lesson demonstrating itself. A claim you were taught as settled at 4pm was contested by 11pm, and neither side has ever shown controlled data. That is the actual working condition of this job.

## Our accounts

**Phoenix Truxx is the cleanest evidence we own.** On 30 June the Box and Pickup statics campaign was paused and the legacy February video campaign reactivated. Statics were running $4.16 cost per lead. Account blended cost per lead, from the filed reports:

| Window | Account CPL | State |
|---|---|---|
| Jun 21-27 | **$6.42** | statics live |
| Jun 29 - Jul 5 | **$7.42** | statics paused Jun 30 |
| Jul 3-9 | **$9.11** | statics off, week 2 |
| Jul 10-16 | **$9.06** | statics back (relaunched Jul 12) |

Relaunch day one: $61.03 spent, 19 leads, $3.21.

Now the part that makes it evidence instead of a story. In the Jul 3-9 week our **CPM fell 13.9% to $25.48** and hook rate rose 3.1 points, while cost per lead rose 22.8%. The auction got *cheaper* while we got *worse*. That rules out the auction as the cause. Without that check, "the pause did it" is just a guess with a table next to it.

Be precise about what this does and does not prove. Nobody killed a bad-looking top spender here; the paused engine was the cheap one. So it is not a test of the contested claim. It is proof of the **method**: read the account, and find a control before naming a cause.

**The closest thing we have to the real case is confounded, so we will not use it.** On 14 May we retired two Phoenix anchors that were still healthy: Faceless Spanish (488 lifetime leads at $2.86) and Video02 English (401 at $2.83). Account CPL went $5.14 to $7.61. In that same window targeting opened from 2 markets to 9 states. Two causes, one window, no verdict. Naming it as proof would be exactly the mistake this lesson is about.

**SJR shows the opposite failure.** The dump CBO has starved the same handful of ads for about seven weeks. In the 29 Jun - 5 Jul week, three new English dump statics took **$0.58 combined**, zero leads, zero learning, while Caesar took $156.66 and DUMP_05 took $110.60. Across 19 Jul - 17 Aug, Caesar holds 63% of dump spend ($605.83) at $9.18. Those starved ads were never tested and rejected. They were never funded enough to be tested. Caesar's own walk: $3.20 → $6.49 → $8.70 → $9.18 at frequency 2.33. Standing instruction is cap Caesar, not kill it, because at 63% of spend he is the feeder.

**ChiroWorks shows CBO starving the wrong thing.** After the 21 July consolidation to one CBO at $66/day, budget routed to the cheapest form fills (invisa-RED, ~$21) and starved the chiro ad set to **$8.95 over 7 days, $1.28/day, 156 impressions**. Inside its own campaign that ad set had been the *best* performer at $32.73 against the campaign's $86.17 average. CBO does not know it starved your best concept. It only knows one number was cheaper.

## The finding that matters most today

The resolving test needs account-level cost per result at 2-3 day resolution. Check what we can actually read:

- **Phoenix Truxx:** best baseline in the vault, 13 period rows plus daily CPL arrays. Meta blind since 25 July.
- **SJR Commercial:** 5 period rows, then Meta blocked 7 straight weeks. Daily arrays for one week only.
- **ChiroWorks:** 4 period rows on overlapping, unequal windows. No daily series exists at all.
- **Chiropraise / StayWell:** 12 weekly rows, but 6-15 leads a week. A 3-day read is 1 to 3 leads. Noise.
- **Mattia:** no reports folder. Offboarded 24 July.

On zero of five accounts can we run the resolving test cleanly today. The honest conclusion is not "Charley T is right" or "Faris is right". It is **we cannot currently arbitrate**, and the cheapest thing on the board is fixing the measurement, not picking a side.

## The decision rule

**Judge at ad-set level, never on the ad's own row. Leave high spenders on unless you can read account-level cost per result at daily resolution with a CPM control, and if you cannot read it, leaving it on is the default.**

On low spenders, as of tonight there is no safe default either way. A genuinely $0 ad costs nothing to keep, so keep it. An ad that has accumulated real spend at zero results is a measured loss and killing it is defensible. Anywhere in between, say out loud that you are making a bet.

## Quiz

Drop your answers in `lessons/_answers-inbox.md` (just "L003: 1) ... 2) ...").

1. Inside a CBO, why do the low-spend ads usually show a cheaper cost per result than the top spender? Name the claim ID and its tier.
2. SC-007 and SC-085 are both contested. One is T2 and one is T3. What is the difference in what each side brought, and why does that change how much weight you give each?
3. In the Phoenix Jul 3-9 week, cost per lead rose 22.8% while CPM fell 13.9%. Why does the CPM number matter to the conclusion, and what would you have been forced to conclude instead if CPM had risen 30% that week?
4. Scenario: SJR. Caesar is at $9.18, holds 63% of dump spend, and his CPL has walked $3.20 → $6.49 → $8.70 → $9.18. The client asks you to kill him this week. What do you do, what do you need in place first, and what do you say to the client?
5. Scenario: a teammate wants to settle the top-spender question by running the 2-3 day kill test on ChiroWorks next week. Give your answer and your reasoning from what we can actually measure there.

> [!note]- Answer key
> 1. Because spend inside an ad set distributes as a funnel sequence, not a contest: the top spender runs top-of-funnel and the low-spend ads close people it already warmed, so their cheap numbers are borrowed from its work. MD-010, T3.
> 2. SC-085 is T3 both ways: Charley T and Faris both assert from experience and neither shows a dataset, so it is two strong hypotheses in conflict and nothing more. SC-007 is T2 both ways: CTC back-tested on billions in managed spend and Theriot shows a live account with real figures. The T2 contest deserves more weight, and it is the more unsettling one, because it questions whether manual on/off does anything measurable at all. Neither can be quoted as law.
> 3. A rising cost per lead has two candidate causes: our change, or the auction getting more expensive. CPM falling 13.9% removes the auction, which is what lets us attribute the rise to the pause. If CPM had risen 30%, the auction would be a live competing explanation, the pause would be unproven, and the honest write-up would name both causes rather than pick one.
> 4. Do not kill him. He is the feeder at 63% of spend, and MD-010 plus the one surviving clause of law 3 (judge at ad-set level, SC-011, T2) both say his own row does not decide. Before touching him you need a readable account-level cost-per-result baseline at daily resolution, which SJR does not currently have (Meta blocked 7 weeks, one week of daily arrays). The correct move is cap him and fund a separate ABO lane for the starved creative, not kill him. To the client: his CPL walk from $3.20 to $9.18 at frequency 2.33 is real fatigue and we are acting on it, and the way we act on it is capping and refreshing, because pausing the ad carrying 63% of delivery risks the whole campaign and we cannot currently measure the fallout.
> **Bonus, ungraded.** The "killing low spenders is safe" clause broke between this lesson being drafted and being published. Argue the SJR case both ways: the three dump statics that took $0.58 in a week are either dead weight worth clearing, or the ad set's assist and reserve layer worth keeping for free. Which do you actually believe, and what would you need to see to change your mind? There is no answer key for this one, because the codex does not have one either.
>
> 5. You cannot run it there. ChiroWorks has no daily series at all, only 4 overlapping period rows on unequal windows, and volume is roughly 15 leads per 9 days, so a 3-day read is 3 to 5 leads. That is inside normal variance and would produce a confident answer from noise. Fix the measurement first, or run the test on the account with a real daily baseline once Meta reporting is restored.
