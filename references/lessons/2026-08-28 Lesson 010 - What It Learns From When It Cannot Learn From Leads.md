---
title: "Lesson 010: What It Learns From When It Cannot Learn From Leads"
lesson: 10
topic: "Learning & Signal"
date: 2026-08-28
source: "rotation index 2 (Learning & Signal). No harvest banked today: the 20:00 research run died on an expired OAuth session."
video: pending
tags: [advertising-science, lesson]
---

# Lesson 010: What It Learns From When It Cannot Learn From Leads

> Lesson 005 proved the learning floor is out of reach on every account we run, and told you to stop managing toward the label. It left the real question open. If the ad set never gets its 50 conversions, what is training delivery right now? Something is. This is that lesson.

## The mechanism

A new manager is told to hire people who will still be at the company in five years. Nobody on the team has been there five years yet, so there is no five-year record to study. The manager does not stop forming judgements. They judge on what they can see this week: who replies fastest, who talks most in meetings. Six months later the team is full of fast repliers. Retention was the stated goal. Reply speed became the actual hiring criterion, because reply speed was the only thing with enough data behind it.

That is your ad set below the floor.

The mistake almost everyone makes is picturing a starved ad set as idle, waiting politely for its 50th lead before it starts working. It is not waiting. It is a system that has to allocate every impression right now, and it will find something abundant to allocate on. Leads are the scarcest thing in the account. Video holds, clicks and impressions are everywhere.

So the question stops being "are we in learning" and becomes "what is it learning from instead". You do not get to switch that substitution off. You only get to control what is available to be substituted in.

Two claims describe the substitution and they disagree about the details. One says that below 50 the ad set samples a pool of roughly 1,000 to 4,000 people and reinforces toward whoever performs soft actions, specifically who holds through the first half of a video. The other says delivery walks up the funnel looking for the nearest event it has enough of: purchases, then clicks, then impressions, and once it lands on impressions, ad-level CPM becomes the thing that decides where the money goes.

Both point the same direction. Neither is documentation. Hold that thought, because the tier work here is the whole lesson.

## The evidence

**LS-001 is the floor and it is T1.** Roughly 50 optimization events in the 7 days after the last significant edit. Meta's own help centre. That number is not in dispute and it is the only part of this lesson that is settled.

**LS-036 is T4.** This is the soft-engagement account: the 1,000 to 4,000 sample, the reinforcement on 50% video hold. It is one operator's model of the cold start. The sample size is his own estimate with no source, the substitution is asserted, and he hedges it himself. Nothing was shown.

**LS-063 is T3, and its tier guard is load-bearing.** This is the upstream cascade, purchases to clicks to impressions. The claim opens by declaring the common understanding wrong and then substitutes the speaker's own model. No Meta page is shown. No delivery column is opened. The 13-purchases and 45-clicks figures are whiteboard illustrations, and extending the same "50" to the click and impression tiers is his invention with nothing behind it. Do not let this claim borrow authority from the T1 threshold it sits underneath.

**Now the part that makes both worth taking seriously anyway, and it is genuinely T1.** LS-017 records that inside billions of daily interactions, clicks and conversions are "very sparse". LS-066 has Meta saying it in its own words: "deep funnel user feedback is scarce", produced by "a small fraction of users", and the research programme exists to extend supervision beyond them. LS-018 and LS-065 add the finding that matters most here. Meta tested this and published it: "sequence diversity beats sequence homogeneity. A balanced mix of action types (e.g., views, clicks, conversions) yields better results than sequences composed of a single action type."

Read the scope carefully, because it is easy to over-claim. Those T1 lines describe how Meta models a **user** from that person's behaviour across the platform. They do not describe what your sub-threshold ad set does, and Meta never discusses advertiser event choice in either post.

So here is the honest position, and I want you to be able to state it exactly this way. The T1 material does not prove the cascade at LS-063 or the video-hold substitution at LS-036. What it does is remove the alternative. A system that tells you conversion signal is scarce, and that it deliberately trains on a mixed ladder of views and clicks because pure high-signal streams model people worse, is not a system that sits idle when your leads run short. The specific mechanism is unproven. The idea that nothing is happening is off the table.

**Two more claims turn this into moves.** CR-196 (T3) says images and video in one ad set means one format takes the spend and the other gets nothing. SC-133 (T3) says an under-volume CBO allocates on click-through rate rather than revenue, which is the same failure one level up.

## Our accounts

**Phoenix Truxx confirms the CPM ordering LS-063 depends on, in our own numbers.** Week to 23 July: the statics engine ran a $20.89 CPM, the video engine $32.48. That is 1.55x, and it is the exact spread that makes the mixing rule dangerous. Statics returned 88 leads on $441.55 ($5.02) while video returned 55 on $963.24 ($17.51), so leads were 3.5x cheaper on the format with the cheaper impressions.

**Then notice what did not happen, because this is the good news and you should take the credit for it.** Those two engines sit in separate campaigns. Delivery never got the opportunity to eat one format with the other. CR-196's trap did not fire on us.

**What went wrong instead was human, and it cost more.** Video held 69% of the budget ($963.24 of $1,404.79) to produce 38% of the leads. Separating the formats stopped the algorithm from making that decision. It did not stop us from making it by hand.

**Phoenix also holds the closest thing on our book to a live floor test, and it needs a caution.** That English statics ad set logged 88 leads in seven days, comfortably past 50. Before anyone celebrates: the account's form-only cost per lead of $13.91 against $1,404.79 of spend implies about 101 form leads of the 143 total, leaving 42 on the pixel and web path, and the report states 42 web leads from that same statics campaign. So the statics ad set's form leads are about 46. Which of those Meta counted as its optimization event is not readable from the file. Lesson 005 taught you to check where a number is measured before celebrating it. Same discipline, our best-looking ad set.

**StayWell is where attention and outcome came apart in writing.** Week to 27 June, four ad sets: Static $81.88 for 10 leads ($8.19), UGC Video $96.48 for 8 ($12.06), Dr. Binder $41.22 for 8 ($5.15), X-ray2 $25.33 for 4 ($6.33). The video ad set took 39% of the spend and returned 27% of the leads. The Real Patient Testimonial video carried the best hook rate in the account at 32.9% and the highest cost per lead of anything running. That is LS-036's warning printed in our own table. *(Carry the caveat: Meta's leads column double-fires on this account, so 30 logged is 15 real people and every cost per lead here is half the true one. The ratios between ad sets hold, because the inflation is constant.)*

**ChiroWorks is the clearest case in the book, and it fails on both axes at once.** The chiropractic ad set was starved to **$1.28/day** ($8.95 and 156 impressions across seven days) inside the consolidated CBO while other ad sets sat budget-limited. That is SC-133's under-volume allocation running on our money.

**The second failure is worse and nobody has been treating it as a delivery problem.** Meta has only ever received one action type from this account: a form was submitted. No conversions API, no booking event, no attendance event, ever. Set that against Meta's own published finding that a sequence of a single action type builds a worse representation than a mixed one. The account with the thinnest event stream on our book is also the account running $38.32 to $54.41 per lead with **zero** attended appointments recorded. Do not read that as proved causation. Read it as the one account where the cheapest available fix, sending more than one kind of event back, has never been tried.

## The decision rule

**An ad set below 50 events a week is still training, on the cheapest abundant action it can see, so control what it can see: one creative format per ad set, more than one event type flowing back, and never a hook approved on hook rate alone.**

## Quiz

Drop your answers in `lessons/_answers-inbox.md` (just "L010: 1) ... 2) ...").

1. LS-001 and LS-036 both contain the number 50. State what each one is actually a claim about, give the tier of each, and explain why treating them as one fact restated would be an error.
2. LS-063 says delivery walks up the funnel to clicks and then impressions. Give its tier, name the specific part of it that the speaker invented, and then name the T1 claims that point the same direction. Finish by saying what those T1 claims do **not** establish.
3. Scenario: an SJR ad set holds one dump-truck video and three statics, and is producing about 12 leads a week. A teammate reports that the three statics failed and wants them cut. Give the first number you pull, the claim you are leaning on, and what result would make you cut them anyway.
4. Scenario: you have one edit's worth of client goodwill on ChiroWorks and $2,000/month that is not moving. Using this lesson, choose between raising the chiropractic ad set's budget floor and wiring booking and attendance events back to Meta. Justify it with claim IDs, and state the honest limit of the evidence behind your choice.
5. Phoenix put statics and video in separate campaigns, which is what CR-196 tells you to do, and the account still sent 69% of its budget to the format costing 3.5x per lead. Explain what separating the formats did buy, what it could never have fixed, and what that tells you about the difference between a delivery problem and an allocation problem.

> [!note]- Answer key
> 1. **LS-001 is about WHEN the learning phase ends**: roughly 50 optimization events in the 7 days after the last significant edit, plus stable delivery. **T1**, Meta's own help centre. **LS-036 is about WHAT delivery reinforces on while it is under that threshold**: a sample of roughly 1,000 to 4,000 people, with reinforcement leaning on soft engagement such as holding through 50% of a video. **T4**, one operator's model, sample size unsourced, substitution asserted and hedged by the speaker himself, nothing shown. The error in fusing them is that it launders a T4 mechanism into a T1 fact by way of a shared number. The 50 in LS-036 is borrowed from LS-001 by the speaker, it is not independent evidence for his model.
> 2. **T3.** The invented part is the extension of the same "50" threshold up to the click and impression tiers, and the 13-purchases / 45-clicks figures, which are whiteboard illustrations. No Meta page shown, no delivery column opened, and he opens by declaring the common understanding wrong before substituting his own model. The T1 claims pointing the same way: **LS-017** (clicks and conversions "very sparse" among billions of daily interactions), **LS-066** (Meta's own "deep funnel user feedback is scarce", from "a small fraction of users"), and **LS-018 / LS-065** (tested and published: sequence diversity beats homogeneity, a balanced mix of views, clicks and conversions beats a single action type). What they do **not** establish: any of them describing what a specific sub-threshold ad set substitutes in. They are about how Meta models a user across the platform, and neither post mentions advertiser event choice. Full credit needs that scope limit stated. They kill "the model idles below the floor" and they do not confirm LS-063.
> 3. **Pull the spend column first**, per **CR-196**. At 12 leads a week that ad set is far under the floor, and the video and the statics are in the same ad set, which is the exact configuration where one format takes the budget and the other gets none. Video CPMs run above image CPMs, which on our own Phoenix read is **1.55x** ($32.48 against $20.89), so the plausible outcome here is the reverse of the teammate's reading. Check whether the three statics were funded at all before calling them failures. What would make you cut them anyway: each static having had a fair, comparable spend window against the video and still returning no leads. A static sitting at a few dollars has not failed, it has not been tested. Bonus for citing the general starvation shape in CR-196, $99 into one ad and 50 cents into the others, and for noting that splitting them into separate ad sets is itself a significant edit under **LS-002** and resets learning on what you touch.
> 4. **Wire the events.** Reasoning: the budget floor addresses **SC-133** and moves money inside an account whose whole signal stream is one action type, so it buys a better-funded ad set that is still training on the single thinnest input available. The event work addresses **LS-018 / LS-065**, which is the only **T1** material in this lesson bearing on the choice, and Meta's tested finding is that a homogeneous single-action stream builds a worse representation than a mixed one. It is also the cheaper thing to be wrong about, and it is required by **LS-015** regardless. **The honest limit, and this is where the marks are:** LS-018 and LS-065 describe how Meta models a user across the platform, not advertiser event selection, so this is a direction-of-travel argument and not a documented prescription for this decision. The zero-attended-appointments figure is a correlation on one account with a known broken follow-up desk, so it cannot be used as evidence that the thin event stream caused the cost per lead. Full credit requires choosing the events **and** conceding that the T1 does not directly cover the choice. Half credit for the right answer with the scope overclaimed.
> 5. Separating the formats bought exactly one thing: it removed the decision from delivery. Inside one ad set, the cheaper-CPM format absorbs the budget and the expensive one is never read, so the statics-versus-video question would have been answered by impression price before anyone saw a cost per lead. Separated, both engines got a genuine read, and that read was unambiguous: $5.02 against $17.51. **What it could never have fixed is a human leaving 69% of the budget on the losing engine after the read came back.** The distinction: a delivery problem is the machine allocating on a proxy because the real signal is too scarce to allocate on, and the fix is structural. An allocation problem is a person looking at a correct answer and not acting on it, and no structure protects against that. Bonus for spotting that video's better hook rate is the likely reason the split felt defensible, which is the same trap **LS-036** describes and the same one that made StayWell's 32.9%-hook testimonial its most expensive lead source.
