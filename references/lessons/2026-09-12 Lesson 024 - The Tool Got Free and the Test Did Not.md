---
title: "Lesson 024 - The Tool Got Free and the Test Did Not"
type: lesson
lesson: 24
date: 2026-09-12
topic: Attribution & Incrementality
claims: [AT-115, AT-118, AT-071, AT-072, AT-022, AT-050, AT-052]
tags: [advertising-science, lesson]
---

# Lesson 024 · The Tool Got Free and the Test Did Not

On 10 September Google made Meridian GeoX generally available worldwide. It is a free, open-source library for running causal geo-experiments across any ad platform, Meta included. The top rung of our measurement ladder just stopped costing money.

This lesson is about what that does and does not change on our five accounts. The short version is that it removes one of the two things standing in the way, and the one it leaves behind is the one that was actually stopping us.

## 1. The mechanism

A geo holdout is simple in concept. Split your map into a test region and a control region that historically move together. Change something in the test region only. Predict what the test region would have done from what the control region did. Read the gap.

The part nobody explains is that the design is sized **backwards**. You do not pick a budget and see what happens. You state, before any money moves, the percentage lift the test would need to produce for the result to clear significance. That number falls out of your baseline volume. Then you work out whether you can plausibly produce a lift that big. If you cannot, the test is already decided, and running it just buys you a wrong answer with a confidence interval attached.

Here is the everyday version. You want to know whether a new gym routine is building muscle. You have a scale. The scale is free, it is accurate to the gram, and it will not answer your question, because your weight swings 1.5 kg across a normal day on water and food alone, and the routine adds maybe 400 g a month. A better scale changes nothing. The effect you are hunting is smaller than the noise in the thing you are measuring. You either need to measure for much longer, or hunt a much bigger effect.

That is exactly the position a geo holdout is in. The noise is how much your weekly opt-in count bounces around on its own. The effect is the lift the campaign produced. A free library builds the experiment. It does not shrink the noise.

**The number that makes this concrete is in our own codex and it is the strongest incrementality evidence we hold.** Blue Sense ran a 21-day Google Demand Gen geo holdout in Australia. Test cell Victoria plus Queensland, control the rest of the country. Baseline in the test cell: 2,771 expected new-customer orders over the window. Threshold declared in advance: a lift of **166 orders at 90% confidence**, which is 5.99%. They measured a lift of 85, which is 3.07%. No statistical relevance. Nothing detectable.

Sit with that. Nearly 2,800 orders in three weeks, thresholds written down in advance, money genuinely spent, and the test could not resolve a 3% effect. That is the volume at which a geo holdout starts being readable.

## 2. The evidence

- **[[Attribution & Incrementality#AT-115|AT-115]]**, T1, banked yesterday. GeoX is generally available worldwide as of 2026-09-10. T1 covers existence, name, availability and Google's own description. Google publishes no accuracy figure, no minimum spend, no minimum order volume and no worked example. Nobody in this workspace has installed it.
- **[[Attribution & Incrementality#AT-071|AT-071]]**, T2. Size the test backwards from the lift it must detect. The thresholds were declared before the read and real money was spent, which is what makes it T2 rather than a worked model. The claim carries an honesty note: the source's own baseline figures are internally inconsistent, so read 2,500 with a 254 threshold as the 95% scenario and 2,771 with 166 as the 90% one.
- **[[Attribution & Incrementality#AT-072|AT-072]]**, T2. The result of that test. Also the rule that generalises furthest: new-customer lift and returning-customer lift must be read separately. A blended read on this test would have shown a win and been reported as acquisition, when the lift was retargeting at $39 per returning-customer order.
- **[[Attribution & Incrementality#AT-050|AT-050]]**, T3. Design rules. Cluster regions on three historical daily series: ad spend, new-customer revenue, new-customer orders. Use combinations of states, because single-state matches usually do not exist.
- **[[Attribution & Incrementality#AT-022|AT-022]]**, the measurement ladder. Geo holdout sits at the top, above MMM and above every platform report, and it puts incrementality at roughly the top 20% of operators. That claim was amended yesterday to say the tooling half of the gate is now free.

Read the tiers honestly. The instrument is T1. The method is T2 from one agency, one advertiser, one market, 21 days. The ladder itself is a practitioner's ranking. Nothing here is a law.

## 3. Our accounts

The first step of AT-050 is to build a per-region series of spend and outcomes. So I opened every regional breakdown on disk across all five accounts. This had not been done before.

**Four of the five cannot produce a test cell at all, and it has nothing to do with statistics.**

| Account | Window | Regions in the export | Outcomes by region |
|---|---|---|---|
| Mattia Spinal Care | 26 Jul to 3 Aug | 1 (Florida) | 19 of 19 in one region |
| StayWell | 8 to 16 Aug | 1 (Michigan) | 12 of 12 in one region |
| Phoenix Truxx | none on file | no regional export exists | none |
| SJR Commercial | 10 to 20 Jul | 10 states, $1,024.14 of spend | **blank in all 10 rows** |
| ChiroWorks | 8 to 16 Aug | 2 (Illinois, Missouri) | 8 and 7 |

SJR's file is the one worth staring at. It carries `Leads` and `Cost per lead` columns. They are populated on the total row, 256 and $4.0009, and every single one of the ten state rows is empty. So the export tells you Pennsylvania took $282.23 and returned a 6.29% click-through rate, and it does not tell you whether Pennsylvania produced one opt-in or forty. **That is the same defect lesson 022 found in the device breakdown, which carried a CPM by operating system and no result column.** Two of our richest breakdowns measure the cost side only.

**ChiroWorks is the single account with a usable two-region split, and it is a real one.** Collinsville sits in the Metro East, so the clinic draws from Illinois and from across the river in Missouri. Three windows, recomputed from the raw CSVs:

| Window | Days | Illinois | Missouri | Account |
|---|---|---|---|---|
| 10 to 20 Jul | 11 | $392.08 / 9 / $43.56 | $161.36 / 5 / $32.27 | $553.44 / 14 |
| 10 to 27 Jul | 18 | $629.81 / 19 | $261.03 / 9 | $890.84 / 28 |
| 8 to 16 Aug | 9 | $429.33 / 8 / $53.67 | $199.56 / 7 / $28.51 | $628.89 / 15 / $41.93 |

Two notes travel with that table. The 10 to 27 July window contains the 10 to 20 July window, so those two rows are not independent observations. And in the July file the two state rows sum to $553.44 against a total row of $553.26, an 18-cent gap I have not chased.

Missouri is 31.7% of spend and 46.7% of opt-ins in August, at $28.51 against Illinois' $53.67. That is interesting on its own and it is not what this lesson is about.

**Now the sizing.** Hold Blue Sense's design, confidence level and split constant, and scale only the count noise, which for counts goes as the square root of the baseline. Their threshold of 166 on a baseline of 2,771 sets the constant at 3.15. Apply it to our own 21-day volumes:

| Cell | Opt-ins per day | 21-day baseline | Lift needed to read |
|---|---|---|---|
| SJR Commercial, whole account | 23.3 | 489 | **~14%** |
| Mattia, whole account | 2.1 | 44 | ~47% |
| ChiroWorks, whole account | 1.4 | 30 | ~57% |
| StayWell, whole account | 1.3 | 28 | ~60% |
| ChiroWorks Missouri cell | 0.5 to 0.8 | 10 to 16 | **~78% to ~97%** |

**State the method's limits out loud, because this is a gate and not a power calculation.** It assumes count noise scales as the square root of volume, it holds someone else's design and confidence level fixed, and it says nothing about how well our regions actually track each other. It is good for one decision: whether the test is obviously out of reach. For ChiroWorks it is. The only cell we could build would have to produce somewhere near a doubling of Missouri opt-ins, sustained three weeks, and even SJR at 489 opt-ins needs an effect more than twice the size of the one Blue Sense failed to detect.

**There is a third gate, and it is the cheapest of the three to fix.** AT-050 says read new-customer **orders**, never blended, because statistical relevance drops hard once returning customers enter the metric. We would be feeding GeoX opt-ins, which are form fills sitting several steps upstream of money. Across five accounts, exactly one holds an attributed sale series: Phoenix Truxx, 19 sold records, 13 marked as ours, spanning 18 March to 21 August. **157 days, 13 sales, which is 1.7 in a 21-day window against Blue Sense's 2,771.** And lesson 019 established that no ChiroWorks appointment has ever been marked showed or no-show, so on our biggest-volume health account the outcome series does not exist at any stage past the form.

So the honest position on GeoX is this. It is free, it is real, and on today's book it is unrunnable. Two of the three blockers are volume, which we do not control. The third is that we have never built the outcome series, which we do.

## 4. The decision rule

**Before anyone builds an incrementality test, compute the lift it would have to detect from the baseline you already have. If that number is larger than a lift you could plausibly cause, the test is decided before it runs, and the decision is not to run it.**

The check takes ten minutes and needs no library. Count the outcomes your test cell produced in a window the length of the test. Take the square root, multiply by roughly three, and divide by the baseline. That is the rough percentage lift you need. Compare it to what the change could honestly produce. A budget doubling does not double results.

Second rule, from AT-072 and it costs nothing: whenever you do run a lift test on any platform, split new customers from returning customers before you read it. A blended read turned a null acquisition result into an apparent win on the one test in our codex where the numbers were fully shown.

## 5. Quiz

Five questions. Put answers in `_answers-inbox.md`, any format, partial is fine.

**Q1.** Explain in your own words why a free, accurate measurement tool can still be unable to answer a question, and name the specific quantity that decides it.

**Q2.** *(Applied.)* Kartik reads about GeoX and asks you to run a geo holdout on ChiroWorks to prove to Dr Kris that Meta is actually working. Give him your answer in five sentences, with the number that settles it, and then say what you would propose instead.

**Q3.** *(Applied.)* SJR's regional export shows Pennsylvania at $282.23 of spend and a 6.29% click-through rate, with the opt-in column blank. A teammate suggests cutting Pennsylvania because the CPM is $30.00 against New Jersey's $22.96. Say what is wrong with that reasoning, name the earlier lesson it repeats, and say what you would pull before deciding.

**Q4.** Argue the opposite. Build the strongest case that we should install GeoX and run something on SJR anyway, at 489 opt-ins and a ~14% detection threshold. Then name the condition that would have to hold for your case to survive.

**Q5.** Blue Sense's test found 85 orders of new-customer lift against 166 required, and a 6.8% returning-customer lift at $39 each. They kept the campaign running at reduced budget and reclassified it. Explain why that is the right response to a null result, and say what the two wrong responses are.

> [!note]- Answer key
>
> **Q1.** Because the limit is not the instrument's precision, it is the ratio between the effect you are looking for and the natural variation in what you are measuring. The scale is accurate to the gram and your weight swings 1.5 kg a day on water alone, so a 400 g monthly gain is invisible no matter how good the scale is. The deciding quantity is **statistical power**, which comes from baseline volume, and in practice the usable form is the percentage lift your baseline lets you detect. Full marks for saying a better tool does not shrink the noise. Extra credit for noting the two ways out: measure longer, or go after a bigger effect.
>
> **Q2.** The answer is no, and the number is the detection threshold. ChiroWorks runs about 30 opt-ins in a 21-day window across the whole account, and the only test cell available is Missouri at 10 to 16, which would need roughly a 78% to 97% lift to register. Blue Sense needed 5.99% on a baseline of 2,771 and missed it. So the test would almost certainly return "not incremental" regardless of whether Meta is working, which is worse than no answer because it looks like one. **Propose instead:** a Meta conversion lift study in the Experiments tab, free and built in ([[Attribution & Incrementality#AT-052|AT-052]], T3), while being straight that it reads platform-attributed conversions and runs through the same attribution layer we are questioning, so it is not a geo holdout and must never be described to Dr Kris as one. Credit for also saying we should first check eligibility by opening Experiments on that account, since nobody in the corpus states the spend gate for CLS. Extra credit for naming the cheaper honest win: build the booking and show series, because the argument with Dr Kris is about whether opt-ins turn into patients and no lift test answers that.
>
> **Q3.** The reasoning compares a cost metric with no outcome metric beside it. A $30.00 CPM buys impressions, and whether that is expensive depends entirely on what those impressions produced, which is the column that is blank in all ten rows. The state could be the cheapest opt-ins in the account or it could be zero, and the file cannot tell you. It repeats **lesson 022**, where SJR's device breakdown showed Android at a $29.91 CPM against iPhone's $21.36 with no result column, and acting on it would have cut over a third of delivery on a cost number alone. Before deciding, re-pull the regional breakdown with the results column populated, or fall back to the opt-in records themselves and count by state from the form data. Full marks require saying that Pennsylvania's 6.29% click-through rate is the second-highest in the file, which is evidence pointing the other way and still is not an outcome.
>
> **Q4.** The strongest case: SJR is the only account with real volume, 256 opt-ins in 11 days; the library is free so the build cost is time only; SJR already delivers across ten states, so combinations of states are genuinely available in a way they are not for a single clinic; and a 14% detection threshold is not absurd for a test that switches a whole lane on or off rather than nudging a budget. Running it would also build the skill before we have an account that needs it. **The condition that has to hold:** SJR's state-level outcome series must exist, and today it does not, because the results column is blank in every region row. Everything else in the case is downstream of that one file. Credit for adding the second condition, that the states have to be shown to track each other on historical daily series first per AT-050, which is work nobody has done. Credit for honesty about the real reason to do it, which is learning rather than a client answer.
>
> **Q5.** Because a null result on the question you asked is not the same as the campaign doing nothing, and the data said what it actually did: it drove returning-customer orders at $39, profitably. Reclassifying it as a retargeting campaign at lower budget matches the spend to what was measured, and it keeps the finding. **The two wrong responses are switching it off**, which throws away a profitable returning-customer channel because it failed a test it was never measured against, **and defending it**, which means reading the blended lift as acquisition and repeating the claim to a client. Full marks for naming the rule underneath: never read a blended lift number, because this exact test would have shown a positive result and been reported as acquisition when the lift was retargeting.

---

**Related:** [[Attribution & Incrementality]] · [[2026-09-11 Lesson 023 - Nothing Got Worse and the Number Did]] · [[2026-09-10 Lesson 022 - An Empty Row Has Two Causes]] · [[2026-09-07 Lesson 019 - The Report Ends Before the Answer Does]] · [[2026-08-30 Lesson 012 - The Twin Is Not a Control]] · [[2026-08-18 Lesson 002 - The Attribution Column Is an Instrument]] · [[ChiroWorks]] · [[SJR Commercial]] · [[Phoenix Truxx]]
