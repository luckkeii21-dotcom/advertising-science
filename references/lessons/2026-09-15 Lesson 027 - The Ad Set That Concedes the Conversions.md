---
title: "Lesson 027 - The Ad Set That Concedes the Conversions"
type: lesson
lesson: 27
topic: Scaling Models
source: Harvest-driven from the 2026-09-14 research run, which banked SC-158 at T3 contested and flagged the proposition inside it as new rather than a rerun. Lesson 026 shipped before that harvest was written, so all eighteen claims from it were untaught. Topic is rotation index 4, not the pointer's own topic at index 1, so the pointer holds. Third lesson on this topic; lesson 011 covered per-ad spend ceilings and lesson 017 covered ad-set spend floors.
created: 2026-09-15
updated: 2026-09-15
tags: [advertising-science, lesson, scaling, audiences, evidence-reading]
---

# Lesson 027 · The Ad Set That Concedes the Conversions

> Lesson 003 taught you that an ad's own row is not the verdict, so judge one level up. This one goes a step further. Sometimes the ad set's own row is not even the right **column**, and two people who look like they are arguing turn out to be grading different exams.

**If you only answer two questions, answer Q2 and Q4.** Q2 is a live ad set in NJ Auto Lending that currently looks like the best thing in the account. Q4 is the decision you will actually be asked to make the next time somebody says "let's test an interest."

## 1. The mechanism

Two operators, same subject, opposite conclusions on the surface.

Charley T says interest, lookalike and retargeting ad sets running beside broad add no conversions. They arrive late in the journey and take last-touch credit for work broad already did. Remove them and total sales do not move.

Sam Piliero runs interest ad sets inside a broad prospecting campaign and defends them. So far this reads like a fight.

It is not one. Read what Piliero actually says: "The reason we use interest targeting is not because it's going to significantly scale our whole account or not because it's going to drive massive amounts of return on ad spend." He concedes the conversions. Twice, unprompted, without being pushed.

**So both men agree the narrow ad set adds no conversions. The disagreement is about a different outcome entirely.** Piliero's claim is CPM, reach, and the size of the pool the system is willing to explore. Charley T's claim says nothing about any of those.

Strip it down and a genuinely new proposition falls out, and this is the thing to carry:

> **An ad set can be worth running while contributing no conversions of its own, if what it changes is what the delivery system learns.**

A football club runs a scout. The scout never scores. Grade him on goals and he is worth nothing, forever, no matter how good he is. His job is to widen the set of players the club ever looks at. If the shortlist has quietly narrowed to two schools in the same town, the scout's value is the schools nobody visited. You can only grade him on the shortlist. Put him on the scoreline and you have guaranteed the answer before you started.

Piliero's selection rule follows from that and it inverts what most people do. The interest must be **far** from the category. "If I was Nike, the interest group I would choose here is not Adidas. It is not Reebok. It is not running shoes. It's something totally different. Maybe it's something just high quality like Sony cameras... maybe it's something like Range Rover because that indicates someone who's aspirational." The criterion is a proxy for customer **value**, not category affinity. Picking Adidas sends the scout to the school next door.

## 2. The evidence

Read the tiers before the content, because the tiers here are the lesson.

- **SC-158, T3, contested.** One operator, one video, one screen. No test shown.
- **SC-070, T3, active.** Interest targeting and lookalikes are dead levers, judged on return on the operator's time rather than on whether they still function.
- **AT-061, T4.** Theory. Reasoning only, no incrementality test anywhere in it.
- **SC-088, T3.** A live account at $1M a month runs exactly the structure SC-158 would justify: one cold campaign holding broad, an interest stack and a lookalike stack, identical ads in all three.
- **SC-022** cuts the other way and says identical creatives in parallel ad sets are separate auctions competing against each other.

Nothing on this question is T1 or T2. Meta documents none of it.

**Now the part worth learning.** AT-061 is the weakest tier in the room, and it is the claim that predicts our own numbers best. You are about to see it do that in section 3. **A T4 that predicts correctly is still T4.** It has earned a test, not obedience. If you take one habit from this lesson, take that one.

**Two T2 claims from a different topic file decide more of this than any of the T3s do, and nobody had put them next to SC-158 before.**

**MD-002, T2.** Meta's targeting is an embedding space. Broad sprinkles small spend across it, watches who converts, then concentrates on those clusters. That is the codex saying, at T2 and months earlier, exactly what Piliero describes as a fault: "your pixel seems to narrow to like this little grouping right here, and it forgets to try to go over here." **His diagnosis is supported at T2. His remedy is not.** Delivery narrowing is the design working, not a bug it developed.

**MD-013, T2.** On a Meta ad set, location, minimum age, language and exclusions bind. Interests and lookalikes sit in the suggestion section and delivery routinely leaves them. Which means a dissimilar interest is not a fence around a weird audience. **It is a seed direction, and delivery walks away from it.** That is the only shape in which Piliero's widening argument can work at all, and it produces a concrete instruction he never gives: if you run the dissimilar-interest ad set, leave the "further limit the reach of your ads" toggle **off**. Turn it on and you have converted the seed into a cage and thrown away the entire point.

The same T2 claim supplies the counter. If delivery leaves every seed, two differently seeded ad sets in one campaign converge on the same people, which is SC-022's competing-auctions problem arriving by a different road.

## 3. Our accounts

I checked every ad-set-level export we hold for the week of 24 to 30 August, across NJ Auto Lending, ChiroWorks and StayWell.

**We run zero interest ad sets and zero lookalike audiences.** ChiroWorks is open targeting and Advantage+ only. NJ Auto Lending's twenty-seven ad sets are named by geography, language and creative. The only strings in the files that look like "lal" are the word "Halal."

We run exactly one non-broad ad set, and it is the kind SC-158's argument does not cover.

**NJ Auto Lending, 24 to 30 August, from the raw ad-level export. $4,440.35 across 27 ad sets and four different result types.** Compare inside one result type only. The Instant Form lane holds fifteen ad sets, $2,157.43 and 276 opt-ins at $7.82.

| Ad set | Spend | Opt-ins | Cost per opt-in | CPM | Cost per 1,000 people reached |
|---|---|---|---|---|---|
| NJ/SI - 3s VV Retarget | $142.05 | 30 | **$4.74** | **$40.94** | **$52.89** |
| ES - > open targeting | $173.20 | 27 | $6.41 | $13.38 | $24.07 |
| EN-> open targeting | $108.96 | 14 | $7.78 | $16.55 | $25.86 |
| Rest of the lane, retarget removed | $2,015.38 | 246 | $8.19 | $29.83 | $45.82 |

**The retargeting ad set is the cheapest thing in its lane, 42% under everything else in it.** On cost per opt-in it looks like the best decision in the account.

Its audience is people who watched three seconds of our video. Every one of them was found and paid for by another ad set first. **AT-061 predicts this exact row, and it predicts it whether the ad set added thirty opt-ins or zero.** A number a claim tells you to expect either way is not evidence that the thing works.

Now grade it on the columns Piliero says a non-broad ad set should be graded on, which is the whole of his defence:

- **$40.94 CPM against $16.55 and $13.38** for the two broad ad sets. 2.5 and 3.1 times. Against the lane average of $30.37 it is 1.35 times, which is the more conservative reading and still the wrong direction.
- **$52.89 to reach a thousand people against $25.86 and $24.07.** Twice the price for people we had already reached.

Some of that is ordinary. A retargeting pool is small, the auction inside it is thin, and thin auctions cost more. That is expected and it is not a scandal.

**The finding is not that the ad set is bad. It is that the column you pick decides the answer, and its own cost-per-opt-in row is the one column that cannot settle it.** On one column it is our best ad set. On two others it is our most expensive. Nobody here had opened the other two.

And the two claims separate cleanly on our book. SC-158's value is **widening**. A retargeting pool built from our own video viewers is the narrowest audience in the account and can widen nothing. **On Piliero's own reasoning, the one non-broad ad set we run is the wrong kind.**

**Where his argument would have to land instead, and it fails there too.** ChiroWorks reached 8,869 people in eighteen days against a radius pool the vault puts at 300,000 to 500,000. That is under 3% of the tightest version of the catchment, measured yesterday in lesson 026. His diagnosis is a pixel that has narrowed inside a large pool and stopped exploring. Ours has not run out of room to explore. It has barely started.

**One is on a plan.** The Phoenix Truxx report of 21 August says: "get the names behind the 18 marketing-sourced sales, upload as offline conversions, and seed a buyer lookalike audience." **LS-019 puts the floor for a lookalike seed at 100 people. We have 18.** That task cannot be scheduled as written, and the fix is upstream of Meta: the seed list has to reach 100 before the audience can exist at all.

## 4. The decision rule

**An ad set defended on what it teaches has to be graded on what it teaches. Write down the column it is supposed to move before you launch it, run the account with it off for a window and on for a window, and read account-level CPM, reach and total opt-ins. Its own cost-per-result row is the one number that cannot answer the question, because a later touch reads cheap whether or not it added anything.**

Applied to us this week, that is three sentences long. We have no interest ad set, so SC-158 is untested here and stays that way until somebody wants to spend a week on it. Our one retargeting ad set is not what SC-158 is about, and its $4.74 should stop being quoted as a result until the account has been read with it switched off. And the Phoenix lookalike is blocked on arithmetic, not on strategy.

## 5. Quiz

Drop answers in `lessons/_answers-inbox.md`. Lesson number plus your answers. Partial is fine and still gets graded.

1. AT-061 and SC-158 are both in the codex. One is T4 and one is T3. Say which is which, then explain why AT-061 predicting our NJ Auto Lending numbers correctly does not raise its tier, and what would.

2. **Live in the account.** NJ/SI - 3s VV Retarget reads $4.74 per opt-in against $8.19 for the rest of its lane. Name the one thing that number cannot tell you. Then design the cheapest test that could, say exactly which numbers you would read at the end of it, and say what result would make you keep the ad set.

3. **Applied.** You are asked to add one dissimilar-interest ad set to ChiroWorks. Collinsville, Illinois, a radius pool of roughly 300,000 to 500,000, 8,869 people reached in the last eighteen-day window we measured. Use Piliero's own stated mechanism to decide whether his argument applies to this account, and give the number that decides it.

4. **Applied.** Using Piliero's selection criterion, pick an interest for NJ Auto Lending. It finances used vehicles for credit-challenged buyers across New Jersey and Staten Island. Name the interest you would pick, name the obvious one you would reject, and say in one sentence what the criterion is actually selecting for. Then say which toggle you would leave alone in the ad set and why.

5. Phoenix Truxx's plan says to seed a buyer lookalike from the marketing-sourced sales. Give the arithmetic reason that task cannot be scheduled as written, name what has to happen first, and say what you would put in the weekly report about it in the meantime.

> [!note]- Answer key
> 1. **AT-061 is T4, SC-158 is T3.** AT-061 is reasoning with no test shown anywhere, which is theory. SC-158 is a practitioner claim from real spend, which is a rung higher even though it is contested. **Why correct prediction does not raise the tier:** tier records the strength of the evidence behind a claim, not the claim's track record on any one dataset. Our NJ Auto Lending numbers are consistent with AT-061 and also consistent with the retargeting ad set genuinely producing thirty opt-ins, because the export has no unexposed cell in it. A claim that explains an observation without ruling out the alternative has not been tested by it. **What would raise it:** turning the narrow ad sets off for a defined window and reading total account opt-ins rather than the ad-set columns, which is the falsification AT-061 names itself. Bonus for spotting that a confirmed prediction from a T4 is a reason to prioritise the test, not a substitute for it.
> 2. **What it cannot tell you: whether any of those thirty opt-ins would have happened anyway.** The pool is our own three-second video viewers, so every person in it had already been reached and paid for by another ad set. The row measures who converted last, not who was caused to convert. **Cheapest test:** switch the retargeting ad set off for a fortnight, leave everything else alone, and hold the campaign budget fixed so the money moves to the remaining ad sets instead of leaving the account. **What you read:** total account opt-ins and account-level cost per opt-in for the off window against the on window, never the ad-set rows. **What makes you keep it:** total account opt-ins fall, or account cost per opt-in rises. If total volume holds while the retarget row disappears, those thirty were being harvested rather than created. Bonus for naming the confounds: a fortnight is one sample, the account has seasonality nobody has measured, and the budget-fixed condition is what stops the test answering a different question. Bonus for noting this costs nothing except the risk of two worse weeks.
> 3. **His argument does not apply here.** The mechanism is a pixel that has narrowed inside a large pool and stopped exploring the rest of it. **The number that decides it is the share of the catchment we have actually reached: 8,869 against 300,000 to 500,000, which is under 3%.** You cannot have exhausted or over-narrowed inside a pool you have touched 3% of. Delivery on ChiroWorks is concentrating because that is what MD-002 says it does, and there is no evidence it has run out of room. Bonus for adding that geography is a hard control under MD-013 while the interest is only a suggestion, so on a radius-limited local account the binding constraint is the radius and an interest cannot widen past it. Bonus for saying what you would do instead, which is fund the account to reach more of the pool it already has.
> 4. **Reject the obvious one: car dealerships, auto financing, used cars, or any competitor.** That is the Adidas answer. It sends delivery to the people already closest to the category, which is where it goes on its own. **A defensible pick** is something that indexes on the customer's real situation rather than the product: rent-to-own or furniture financing, tax-refund services, gig-platform apps, or check-cashing and prepaid-card brands. Any of those is fine with the reasoning attached. **What the criterion selects for is a proxy for the customer's financial position and buying mode, not for interest in vehicles.** Note the honest difference from Piliero's own example: his Nike case picks upmarket proxies because his customer is aspirational, and ours points the other way, so you have to copy the method rather than his interests. **The toggle:** leave "further limit the reach of your ads" off. Under MD-013 the interest is a seed direction delivery is meant to leave, and turning the toggle on hardens it into a constraint, which destroys the widening the ad set exists to do. Bonus for saying you would grade it on account CPM and reach, never on its own cost per opt-in.
> 5. **The arithmetic reason: LS-019 puts the minimum seed at 100 people and the plan names 18.** A lookalike cannot be built from a source that small, so the task is blocked before any judgement about whether lookalikes are worth running. **What has to happen first** is upstream of Meta: get to at least 100 identified buyers, which means either more attributed sales or a wider source than marketing-sourced sales alone, for example the dealership's full customer list uploaded as offline conversions. **What goes in the report:** say the lookalike is blocked, say it is blocked on seed size with both numbers, say what the seed has to reach, and do not carry it forward as "in progress." Bonus for noting we hold exactly one attributed-sale series across five accounts, so this is the constraint on far more than one audience. Bonus for refusing to pad the seed with unqualified contacts, because a lookalike is only as good as what it is modelled on.
