---
title: "Lesson 011: Every Ad Has a Ceiling, and Your Account Is Their Sum"
lesson: 11
topic: "Scaling Models"
date: 2026-08-29
source: "harvest 2026-08-28 (MD-137 gained the per-ad spend ceiling and the account-capacity model; SC-058 gained Theriot's zero-spend ABO trigger and his 95-98% CBO figure). Paired with MD-136, which has never been taught."
video: none
tags: [advertising-science, lesson]
---

# Lesson 011: Every Ad Has a Ceiling, and Your Account Is Their Sum

> Lesson 003 told you what to do with the ad hogging the budget: leave it on, judge at ad-set level. It left the other end of the table alone. This lesson is about the ads sitting at forty cents, why they are there, and the one number that tells you whether their row means anything at all.

## 1. The mechanism

Meta does not ask which ad performed best. It asks what the **next dollar** returns.

That single word changes everything. An ad with a worse average cost per opt-in can correctly receive more spend than an ad with a better one, because the average dollar is history and the next dollar is the actual question.

Here is the part nobody tells you. Each ad has a pocket of people it converts cheaply. Work that pocket and the cost per opt-in stays low. Keep pushing money through the same ad and you reach further out, to people who are harder to convince. The ad did not get worse. The cheap people ran out.

A takeaway shop with one delivery driver has the same shape. The first twenty orders a night are all within a mile. Order forty means driving across town. The driver has not become worse at driving, the nearby customers are used up. Eighty orders a night takes a second driver on a second neighbourhood, so the shop's capacity is the sum of two rounds and it was never double the first.

Every ad has a daily spend it can hold before its next dollar goes bad. **Your account's real capacity is the sum of those ceilings, one ad at a time.**

Now put the two halves together and the starved bench explains itself. When your budget is smaller than what the incumbent ad can comfortably hold, the incumbent wins every next-dollar comparison, all day, every day. The new ads lose that comparison and go dark. They are failing against the incumbent. Their own cost per opt-in never entered the argument.

Which is why the instinct to fix it with more creative does not work. Launch five more ads and they take a few dollars each and fall to zero for exactly the same reason.

## 2. The evidence

Everything below is **T3**. One operator each, no dataset shown, nothing from Meta's own documentation. Hold it as a strong working model and say so out loud when you use it.

- **MD-136, T3, active.** Delivery optimises on "the best CPA at the entire campaign or adset level, which is based on incremental returns as you continue to drive spend into an ad." The only hard time constant in the file: for the first 48 hours all new ads get roughly equal spend, then Meta starts choosing. His reframe is the one to memorise: starved ads "aren't necessarily performing poorly ... They're simply underperforming against the highest performing ads within the account." His two remedies are raising the campaign budget past the point where the incumbent's marginal cost degrades, or breaking the starved ads into dedicated campaigns and accepting a worse but readable number.
- **MD-137, T3, active, gained new material 2026-08-28.** "Each individual ad unit has a maximum spend threshold that it can hold profitably," illustrated at $1,000/day for a broad-message ad, $100/day for a narrow one and $40/day for a weak one. Then the model: "it's the summation of the ad spends that all of these ads can currently hold that gives you the total ad spend that that ad account should hold whilst maintaining efficiency targets." Efficiency against spend declines logarithmically.
- **MD-137's geography caveat, and it applies to every number above.** His figures are Australian, and he says a US equivalent needs scaling up, hedged with "maybe," at roughly 1.5x to 2x. So read the ceilings as roughly $1,500 to $2,000, $150 to $200, and $60 to $80 a day here. Quote them unadjusted and you are quoting them up to twice too low.
- **SC-058, T3, active, gained new material 2026-08-28.** Nick Theriot, agency spending over $5 million a month: "based off last 30 days ... 97% of our accounts use a CBO campaign," restated later as "95, 98%," so read it as a band. **His trigger for reaching for ABO is literally zero spend**, and he names what he is content to leave alone: "50, 75, 90, $48, like they're still getting some spend ... I'm okay with that." He prices the ABO route at 10 to 20% of daily budget plus 3 to 4 extra days, and reports the diagnosis usually goes against him: "nine times out of ten we're wrong and Facebook still is correct with its choice."
- **SC-011, T2, active.** Judge at ad-set level. The only T2 claim here, and it constrains all of the above.

**The guards, because they matter more than the claims.** MD-136 is a whiteboard explanation with no account open, every cost figure prefixed "let's say," and one of its own illustrations fails its own arithmetic (two numbers described as "about 30% lower" compute to 25%). MD-137 gives no account list and no denominator, so its 20-funded-ads figure can never be turned into a percentage. Theriot gives three incompatible frequencies for his own ABO exception inside one video, 2 to 5%, 10%, and 20%. Quote the exception, never the rate.

## 3. Our accounts

**Start with the arithmetic that reframes the whole problem. The SJR dump campaign runs at $40 a day.** In MD-137's model, adjusted for the US, that is at or below what a single *weak* ad can hold profitably.

So there is no mechanical reason for that campaign to fund a second ad. One asset can absorb the entire budget without ever reaching the point where its next dollar goes bad. The starvation we have been writing up as an execution failure for seven weeks is arithmetic.

The account agrees, in detail.

- **`Caesar Dump Truck Ad` took 63% of dump spend**, about $603 of the campaign's $957.81 over 30 days. Its cost per opt-in walked **$3.20, then $6.49, then $8.70, then $9.18** across four weeks. That is an ad crossing its ceiling in public. Same creative, same audience, progressively more expensive people.
- **The three newer dump statics took $4.03 between them over the same 30 days.** That is about **4.5 cents per ad per day**. In the earlier Jun 29 to Jul 5 window they took **$0.58 combined** against a dump campaign that spent roughly $268, which is **0.22%**.
- **ChiroWorks ran a chiropractic ad set at $1.28 a day**, $8.95 and 156 impressions across a week, inside a consolidated campaign where two other ad sets were budget-limited. The chiropractic offer was close to untested at a chiropractic clinic.
- **StayWell's testimonial collage sat at $0.83** and returned one opt-in anyway. Third window running, converts whenever it is fed, starved every time.

**Now hold those against Theriot's floor.** He is comfortable leaving an ad alone at **$48**. Our starved ads sit at **$0.58**, about **83 times** below the number he considers "still getting some spend." The condition he treats as a rare exception is the everyday condition on our book.

**And Phoenix Truxx already ran the experiment for us.** In the week to 2026-04-24, `Video02 English` received **$0.63** and produced nothing. Read as a row in a table, it was a dead ad. It was moved into Campaign 3 with its own budget and returned **14 opt-ins on $23 at $1.64 each**, with a 4.72% click-through rate. It became the account's second anchor creative: **363 opt-ins all-time at $2.66**. The filed report's own line still stands: a proven asset starved of budget looks dead, fund it and it wins.

**The instrument that would have caught it, and you can do it in your head.** Divide the ad's spend by the account's cost per opt-in. Call it chances bought.

| Ad | Spend | Account cost per opt-in | Chances bought |
|---|---|---|---|
| Phoenix `Video02`, week to Apr 24 | $0.63 | $3.99 | **0.16** |
| SJR three dump statics, Jun 29 to Jul 5 | $0.58 | $8.94 | **0.06** |
| SJR three dump statics, 30 days | $4.03 | $9.04 | **0.45** |
| ChiroWorks chiro ad set, one week | $8.95 | $35.57 | **0.25** |
| StayWell collage | $0.83 | $26.52 | **0.03** |

Every one of them is under one. Not one of those ads ever bought a single fair chance at a single opt-in. A zero in that row is a purchase nobody made.

**Be honest about what this instrument is.** It is arithmetic, not a law. **AT-106** closed the question of whether anyone on our source roster publishes a threshold for calling a test, and the answer was that nobody does. Under one chance bought is the only part that is certain, because you cannot read a zero out of an ad that never bought one chance. Above that, you are making a judgement, and you should say so.

## 4. The decision rule

**Before you kill an ad, divide its spend by the account's cost per opt-in. Under one chance bought the row is silent, and the only things that make it speak are a bigger budget or its own campaign, never more ads.**

The second half follows from the first. When the incumbent holds most of the budget and its cost per opt-in is walking upward week after week, that is its ceiling, and the answer is a second funded asset rather than more money into the same one.

## 5. Quiz

Drop answers in `lessons/_answers-inbox.md`. Lesson number plus your answers. Partial is fine and still gets graded.

**If you only answer two, answer Q3 and Q5.** Q3 is live on SJR right now and the answer changes what ships Monday. Q5 is the one that stops you from misapplying this whole lesson.

1. MD-136 and MD-137 are both T3 and both rest on a single operator. State what each one claims in your own words, and give the strongest guard against each. One of the two contains a figure that fails its own arithmetic. Name it.

2. A teammate reads SC-058 and proposes moving all five of our accounts to ABO, because Theriot names zero-spend ads as his ABO trigger and we have zero-spend ads everywhere. Give the argument for the move and the argument against it, using the spend levels involved.

3. **SJR, live.** The dump campaign runs $40/day. `Caesar Dump Truck Ad` holds 63% of spend and its cost per opt-in has walked $3.20 to $6.49 to $8.70 to $9.18 over four weeks. Three newer statics have taken $4.03 between them in 30 days. You have the Phase 5 bench built and unlaunched. Write what you do, what it costs, and what you expect to be able to read in two weeks that you cannot read today. Name the one thing that would tell you your move was wrong.

4. ChiroWorks has roughly $2,000 a month that is not moving and an account cost per opt-in of $35.57. Using chances bought, work out the minimum weekly spend an ad needs before a zero in its row is worth anything to you. Show the arithmetic. Then say what you would actually set, and why your number is above or below the arithmetic minimum.

5. MD-136 says the fix for a starved bench is raising the campaign budget, because that pushes the incumbent past the point where its next dollar goes bad. MD-137 says efficiency against spend declines logarithmically and the account has a total capacity that is the sum of its ads' ceilings. Those two claims bound each other. Explain where the boundary sits, and describe the account condition in which raising the budget stops being the fix and becomes the problem.

> [!note]- Answer key
> 1. **MD-136** claims delivery allocates on *marginal* cost per opt-in, what the next dollar returns, so a starved ad is losing to the incumbent rather than failing its own target, and launching more ads cannot fix that because the newcomers lose the same comparison. **MD-137** claims each ad has a maximum spend it can hold profitably, and the account's healthy total is the sum of those per-ad ceilings. **Guards:** MD-136 is a whiteboard with no account shown and every cost figure prefixed "let's say"; MD-137 gives no account list and no denominator, so its funded-ad figures cannot be converted into a percentage, and all its thresholds are Australian and need a 1.5x to 2x adjustment for US accounts. **The arithmetic failure is in MD-136**: a hypothetical comparison stated as "about 30% lower" whose components give 25%. Full credit needs the failure attributed to MD-136 specifically. Bonus for noting the 48-hour equal-allocation window is MD-136's only hard time constant, and that every other number in it is scaffolding.
> 2. **For:** his stated trigger is literally zero spend, and our ads sit at $0.58 against the $48 he is content to leave alone, so on his own criterion our accounts are 83x past the line where he would act. Our starved assets are also not hypothetical losers, since Phoenix `Video02` and StayWell's collage both converted the moment they were funded. **Against:** he runs $5,000 a day through a single campaign and every client we have is under $30,000 a **month**, so his 97% CBO figure is an argument for CBO *at his spend*, and importing his exception without his scale is importing half a claim. He prices ABO at a fixed 10 to 20% of daily budget plus 3 to 4 days of delay, which on a $40/day campaign is real money for a slower read. And his own reported hit rate goes against the move: "nine times out of ten we're wrong and Facebook still is correct." **The strongest answer refuses the all-five framing entirely.** This is a per-campaign decision driven by whether there is a specific asset we have a commercial reason to fund, and the SJR dump campaign is a yes while the accounts with a working incumbent and nothing waiting are a no. Bonus for spotting that his three stated exception rates (2 to 5%, 10%, 20%) contradict each other, so the rate is unusable and only the trigger transfers.
> 3. **The move: launch the Phase 5 bench in its own ABO lane split by language, and leave Caesar alone.** Reasoning: at $40/day the campaign cannot fund a second ad, so nothing launched into it will ever be read, which is what the last seven weeks demonstrated twice at $0.58 and $4.03. Leaving Caesar on is required by **SC-011** and by lesson 003, and killing it would also remove the only thing currently producing opt-ins. **The cost:** either new budget, or a share of the existing $40/day that goes to a worse cost per opt-in while the bench is read. Say which, out loud, and put a number on it. **What becomes readable in two weeks:** whether any bench asset can produce opt-ins at all, which is a question that currently has no evidence either way, plus a fair Spanish-versus-English read that the blended campaign has never given us. **What would tell you the move was wrong:** the bench ads getting a fair, comparable spend window and still returning nothing, or the dump campaign's total opt-ins falling by more than the bench lane produces. Full credit requires naming the falsifier. Bonus for noting Caesar's walk from $3.20 to $9.18 means a replacement is needed regardless of what the bench proves, so the lane is buying succession and not only information.
> 4. **The arithmetic:** one chance bought at $35.57 means an ad needs $35.57 before a zero in its row carries any information at all. That is roughly **$5.08 a day**, or about **$36 a week**, for a single fair chance. **What you would actually set is higher, and the reasoning is the marks.** One chance produces a zero about a third of the time even for an ad performing exactly at the account average, so a single zero at one chance bought is close to meaningless. Three to five chances, so roughly $107 to $178 over the test window, gets you to where a zero is weak evidence. On roughly $2,000 a month, about $66 a day, funding two bench ads at 3 chances each is a genuine and affordable commitment. **Full credit requires stating that the 3-to-5 figure is your judgement and not a sourced threshold**, per **AT-106**, which found nobody on the roster publishes one. Half credit for correct arithmetic with the threshold presented as if it were a law.
> 5. **The boundary is the sum of the ceilings.** MD-136's remedy works while the campaign budget is below what its current ads can collectively hold: extra money pushes the incumbent past its own efficient range and the allocation genuinely frees up for the bench. Once the budget exceeds the summed ceilings of every ad in the account, there is nowhere efficient left for the next dollar, and raising the budget buys worse marginal cost per opt-in across every asset at once rather than a better distribution. **The account condition:** costs rising on *all* ads together, including newly funded ones, with no asset holding its number as spend increases. That is a capacity problem and more budget makes it worse. **The fix at that point is horizontal**, adding assets or an offer that opens a new pocket of people, rather than vertical. Bonus for connecting this to MD-137's logarithmic curve, since the job is to find the spend that maximises profit contribution and then try to move the curve right. Bonus for noting our accounts sit at the opposite end of this problem, well under capacity, which is exactly why one ad takes everything and why the ceiling argument should not be used to justify holding budget back on our book.
