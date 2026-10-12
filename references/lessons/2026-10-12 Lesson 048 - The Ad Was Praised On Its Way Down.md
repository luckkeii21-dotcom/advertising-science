---
title: "Lesson 048 - The Ad Was Praised On Its Way Down"
type: lesson
lesson: 48
date: 2026-10-12
topic: Creative Science
claims: [CR-283, CR-177, CR-232, CR-028, CR-025, MD-051, MD-155, MD-137, SC-168, CR-251]
video: video/2026-10-12-lesson-048.mp4
tags: [advertising-science, lesson, creative-science, creative-fatigue, refresh-cadence, baselines]
---

# Lesson 048 · The Ad Was Praised On Its Way Down

🎬 **Lesson video (3m 57s, silent, watch anywhere):** [[video/2026-10-12-lesson-048.mp4]]

The rotation brought up Creative Science, and the oldest unanswered question in it is the one every client asks. How often do we need new ads.

A platform finally answered it ten days ago. The answer was no.

That refusal is more useful than a number would have been, and it points at a free column we have never added to a report. On our own book that column would have caught a collapsing ad two weeks before anyone noticed. The week before anyone noticed, we put that ad in the "What worked" section of a client report.

## 1. The mechanism

Two runners finish a race. One comes second, the other comes fourth. Run it again next month and they finish second and fourth again. From the placings you know one is faster than the other, and you know nothing at all about whether either of them is getting worse. Both could be twelve seconds slower. The placings cannot see it, because the only thing a placing compares you to is the other runners on the day.

The stopwatch can see it. It compares you to yourself.

Almost everything in an ad report is a placing. Cost per opt-in next to the other ads. Cost per opt-in next to the account average. Frequency next to a threshold. All three are cross-sectional: they tell you where an ad sits today relative to something else today. None of them can see a trend, because a trend needs the same unit measured twice.

So an ad can be the second-cheapest unit in the account, get written up as the workhorse, and already be twice as expensive as it was when it was new. Nobody has to be wrong for that to happen. Both readings are correct. They answer different questions, and only one of them answers "is this ad dying".

## 2. The evidence

**[[Creative Science#CR-283|CR-283]], tier 1, and the tier is the point.** This is Google's own Demand Gen product manager, on Google's podcast, asked how often to replace assets. He looked at the platform's data and declined to answer: "As much as I'd love to be able to give a definitive number, when we look at the data, we find that the answer is really that it depends." The dependencies he names are the type of asset, the inventory it serves on, and the behaviour of the audience. Then the instruction: "I would actually recommend against setting a blanket rule for your business on how frequently to replace assets."

What he gives instead is the stopwatch. Open asset reporting and read each asset **against its own start**: "is there a declining trend relative to when you first added that asset... if you see that it is markedly declining relative to how it was performing when it was fresh, that's a good indication that it is a stronger candidate to consider swapping out."

Then the part that changes what you do with the answer. Decline alone does not earn a removal. **Both conditions have to hold**: "the only time where it makes sense to actively remove or replace assets is if you're already at capacity within your Demand Gen ad AND a specific asset has shown a significant decline in performance relative to its start." Where the container still has room, the prescribed move is to add the new asset and leave the old one running.

**What CR-283 does not establish, and this matters because T1 tempts you.** No distribution of asset lifespans. No definition of "markedly declining". No capacity number. No evidence anywhere that add-first beats replace-first. It is a platform's stated recommendation, not a measured result, and it is also the recommendation that keeps the most assets in Google's auction. Treat the reading method as free and the removal rule as a reasonable bet.

**Scope, stated plainly: this is a Demand Gen claim and we run no Demand Gen campaign on any account.** The own-start read transfers for nothing, because it is arithmetic on two numbers we already pull. The capacity half does not transfer cleanly, because Demand Gen asset slots are a published count and Meta publishes no equivalent per-ad capacity.

**[[Creative Science#CR-177|CR-177]], tier 3, contested, and it is the instrument our own reports actually use.** Frequency above 2.0 at ad level over 14 days on cold. The source supplies his own objection: reported frequency is a mean over a right-skewed distribution Meta stopped exposing six years ago, so "10% of users are actually getting targeted like 11 plus times" can hide behind an average of 2.4. He also tells you most ads pass it, "90% of the time when you do this exercise, frequency is probably going to be under a two and you're fine". Zero data is shown anywhere in the transcript. Four unit disciplines travel with it and they are the valuable part, including the one that does real work below: **frequency always rises as you go up the account structure, because it encapsulates more audience.**

**[[Meta Delivery & Andromeda#MD-051|MD-051]], tier 3, and [[Meta Delivery & Andromeda#MD-155|MD-155]], tier 2.** The claim is that cold ad-level frequency almost never exceeds 2 over a 30 to 60 day pull. We measured it on our own book on 14 September: across ChiroWorks and SJR Commercial, **56 of 60 live ads sat at or below frequency 2**, highest 2.857. So the threshold holds on our accounts. Read that the other way round and it is a problem. **An instrument that fires on about 4 of 60 ads is not a fatigue detector. It is a rarity detector.**

**[[Creative Science#CR-232|CR-232]], tier 3, is why a decline is a trigger rather than a verdict.** A decayed ad has at least three causes that produce an identical Ads Manager row. The audience has genuinely stopped responding, and only new creative fixes that. The delivery system stopped selecting the asset against the objective it is scored on, which a different optimisation setting can reverse, and the test costs one duplicate. Or an operator changed something, in which case the change log holds the answer. **The own-start read tells you which ad to investigate. It never tells you why.**

**[[Creative Science#CR-025|CR-025]], tier 3, is what we are actually doing instead**, along with most of the industry: a fixed-cadence pipeline, 12 to 15 new creatives a week, the pipeline rather than any ad being the fatigue defence. CR-283 is the first source on file to say, from inside a platform, that no cadence can be right in general, because the fatigue point is a joint property of the asset, the inventory and the audience. [[Creative Science#CR-028|CR-028]] already carried that mechanism at T3 as embedding-cluster saturation. [[Creative Science#CR-251|CR-251]] is the same mechanism read across channels and the spread is roughly 13x, quarterly on YouTube against weekly on Meta, which is itself an argument that no single number travels.

## 3. Our accounts

ChiroWorks, Collinsville IL. **Before/After Ad_05** went live on 23 September and became the account's local winner. Every figure below comes out of a filed report.

| Window | Days | Spend | Opt-ins | Cost each | Against its own start |
|---|---|---|---|---|---|
| Sep 23-27 | 5 | $161.56 | 14 | **$11.54** | baseline |
| Sep 28 to month end | 2-3 | $98.43 | 6 | $16.41 | 1.42x |
| Sep 30 - Oct 6 | 7 | $166.34 | 6 | **$27.72** | 2.40x |
| Oct 2-8 | 7 | $149.28 | 3 | **$49.76** | **4.31x** |

Three of those rows are direct pulls. The $11.54 and $49.76 rows were filed as opt-ins and cost per opt-in, so their spend is multiplied back out. The Sep 28 row is derived by subtracting the Sep 21-27 week from the September month figure of $259.99 and 20 opt-ins, which ties to the dollar, and 30 September sits on both sides of that boundary, so call it two days or three. The last two windows overlap on 2 to 6 October. **None of that touches the shape. $11.54, then $27.72, then $49.76, on near-identical weekly spend of $166.34 and $149.28.**

**Now the two readings of the middle row, which is where the lesson lives.** In the week of 30 September to 6 October, Ad_05 at $27.72 was the second-cheapest real unit in an account averaging $27.25. The filed report called it the "new local workhorse" and put it in **What worked**. That is correct as a placing. Against its own start it had already lost 58% of its efficiency. One week later it was at $49.76.

**Its sibling makes the point unarguable, because it ran in the same campaign in the same weeks.** Before/After Ad_06 read $14.90 in the 30 September week and $12.35 in the 2 October week. It got 17% cheaper while Ad_05 doubled. Two ads from the same family, same account, same audience, same fortnight, opposite directions. **No account-level number and no threshold can separate those two. A per-ad baseline separates them instantly.**

**Put the size of the blind spot in one line.** In the 2 October week Ad_05 at $49.76 sat 1.57x above the account's $31.74. Against its own start it sat 4.31x. **The cross-sectional read understates the collapse by about 2.7x.**

**What our own fatigue instrument said while that happened.** Frequency 1.60x in the 30 September week, filed with the note "below the 2.7 refresh trigger". Frequency 1.70x in the 2 October week. CR-177's threshold is 2.0 at ad level. Frequency rises up the account structure, so Ad_05's own ad-level frequency cannot have exceeded the 1.70x reported for the window. **The instrument was not unlucky. It was silent by construction, and it would have stayed silent through a 10x.**

**The second condition, capacity, and our answer is not close.** ChiroWorks spent $2,033.06 in September. [[Meta Delivery & Andromeda#MD-137|MD-137]] puts the funded-ad count at roughly one below $30,000 a month, and its own geography caveat says US thresholds need a 1.5x to 2x lift, which pushes that line further above us. [[Scaling Models#SC-168|SC-168]] measured the container directly: in the 11 to 20 September window, **22 ads spent $624.10, the top ad took $24.76 a day, and 16 of the 22 produced zero opt-ins on $35.55 between them.** Nothing here is at capacity. Under CR-283 the prescribed move on this account is always add, never replace.

**We have been replacing.** The 21 to 27 September report records the weak Before/After line at $46.67 being "replaced by a numbered variant family". The 30 September to 6 October report describes Ad_05 itself as having "replaced a weaker line". The 2 to 8 October plan, written after Ad_05 tired, says launch the three built patient-story videos to refresh the roster. **That last one is an add, and it is the first one that matches the rule.**

**The counter-case sits on the same account, and it is why a decline is a trigger and not a verdict.** The Sciatica video reads $10.32 per opt-in in the 11 to 20 September window, then $33.71, then $37.51, then $33.74. On the own-start read that is a 3.63x decline and the top swap candidate in the account. It is also wrong twice over. The cause is dated and it is ours: the 21 September targeting correction moved delivery to about 98% inside the Collinsville and St. Louis catchment, and the filed note says 24 of the 25 opt-ins behind that $10.32 were out of area. **So the baseline was an artefact, and the decline was us fixing the account.** The monthly report also records that every chiropractic opt-in since 21 September came from that video, so swapping it would have zeroed a lane. Change log first, every time.

## 4. The decision rule

**Write down an ad's cost per result from its own first full window on the day it goes live, and judge that ad against that number, never against the other ads and never against a frequency threshold.**

Two lines on what it costs and what it licenses. The column is free: one number per ad, stored once, and the comparison is division. And a decline buys an investigation, not a swap. Check the change log, then check whether the container has room. On every account we run it has room, so add the new ad and leave the old one running.

## 5. Quiz

Drop your answers in `_answers-inbox.md`.

**1.** CR-283 is T1 and most of this codex is T3. Name the two separate things CR-283 establishes at T1, and the four things it does not establish at all.

**2.** Explain in two sentences why an account-level cost per opt-in and an ad-level frequency threshold are the same kind of instrument, and what defect they therefore share.

**3.** Ad_05 sat 1.57x above its account and 4.31x above its own start in the same week. Both numbers are correct. Say what question each one answers, and which of the two belongs in a client report's "areas to improve" section.

**4. Scenario.** StayWell. In a 10-day window the account ran 12 ads on $337.49 and produced 12 opt-ins, the top ad held 63.6% of spend at $21.48 a day, and 10 of the 12 ads produced zero opt-ins on $98.05 between them. A new ad launched three weeks ago read $19 per opt-in in its first week and reads $44 this week on similar spend. Account frequency is 1.5x. Walk the rule: what do you check, in what order, and what do you actually do. Name the one check that could make the $44 not a fatigue finding at all.

**5. Scenario.** A client asks you to put a creative refresh cadence in the retainer, in writing, because their last agency promised eight new ads a month and they want the same commitment. You have CR-283 at T1 saying a blanket cadence is not supportable, and CR-025 at T3 saying a fixed pipeline is the fatigue defence. Give the answer you would actually send, say which claim you are leaning on for which half of it, and name the number you would put in the retainer instead of a cadence.

> [!note]- Answer key
>
> **1.** T1 establishes two things, both statements rather than results. **One: Google looked at its own data and the data did not support a cadence**, with the three named dependencies, asset type, inventory, audience behaviour. **Two: Google's stated recommendation**, which is the per-asset own-start read plus the two-condition removal rule and the add-first default. It establishes none of the following: a distribution of asset lifespans, a definition of "markedly declining", a capacity number for an ad, or any evidence that add-first beats replace-first. Full credit for adding that the recommendation is also the one that keeps the most assets in Google's own auction, so the incentive runs with the advice.
>
> **2.** Both are **cross-sectional**: each compares an ad to something outside itself at one point in time, the other ads or a fixed number. So both share the same defect, which is that **they cannot see a trend**, because a trend needs the same unit measured twice and neither of them measures the ad twice. Credit for naming the consequence on our book, that an ad can pass both while its own cost per result quadruples.
>
> **3.** **1.57x answers "is this ad worse than the alternatives I am running right now", which is an allocation question.** **4.31x answers "is this ad dying", which is a lifecycle question.** The 4.31x belongs in areas to improve, because it is the one that names a problem and dates it. Credit for noting that the 1.57x is still the right number for deciding where next week's budget goes, so this is not a case of one figure being wrong.
>
> **4.** Order matters. **First the change log**, because an operator cause is the cheapest explanation and it was the real one on our Sciatica video: ask what changed in those three weeks, targeting, geography, budget, offer, form, landing page. Second, **check the baseline was real**, because $19 in week one is only a baseline if that week's delivery was the same kind of delivery as this week's, and on our book a cheap first week turned out to be out-of-area traffic. Third, **check capacity**, and this account is nowhere near it: 12 ads on $337.49 over 10 days is about $33.75 a day, the top ad took $21.48 of that, and 10 of 12 ads returned nothing on $98.05, so the container has room. Therefore **do not remove the ad. Add.** Launch the next ad and leave the $44 one running. **The one check that could make the $44 not a fatigue finding is CR-232's deselection test**: run the asset in an ad set on a different optimisation setting and watch whether it takes spend, because spend returning says it was deselected rather than exhausted, and it costs one duplicate. Credit for refusing to read the 1.5x frequency as evidence of anything, since frequency rises up the structure, so the ad-level figure is at most 1.5 against a 2.0 threshold and the instrument is silent whatever is happening. Credit also for naming that 12 opt-ins across 12 ads is too thin to rank an ad at all.
>
> **5.** Lean on **CR-025 for the commitment and CR-283 for the trigger**. The honest answer: commit to the **production** number, because that is the thing we control and the thing the pipeline evidence actually supports, and refuse to commit to a **replacement** number, because the platform that runs the auction looked at its own data and recommends against a blanket replacement rule. So the retainer carries new ads built and launched per month, and it carries the review mechanism rather than a swap schedule: every ad gets its first-window cost per opt-in recorded on launch, every ad is read against that number weekly, and an ad is retired only when it is both declining against its own start and the container is full. **The number in the retainer is the monthly count of new ads built and launched, not a refresh or replacement cadence.** Credit for adding that on an account this size nothing is ever at capacity, so in practice we add and almost never remove, and for telling the client that plainly up front so an old ad still running is not read as neglect. Credit for noting that the last agency's eight a month was also a production number being sold as a performance promise.
