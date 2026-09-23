---
title: "Lesson 034 - A Ceiling and a Budget Look the Same in the Spend Column"
type: lesson
lesson: 34
date: 2026-09-23
topic: Scaling Models
claims: [SC-163, SC-058, SC-167, SC-168, CR-255, MD-137, MD-163]
video: video/2026-09-23-lesson-034.mp4
tags: [advertising-science, lesson, scaling-models, concentration, creative-volume]
---

# Lesson 034 · A Ceiling and a Budget Look the Same in the Spend Column

For a year this codex has carried concentration as a law. Twenty percent of ads take eighty percent of spend, and a CBO compounds it until about 4% of ads hold about 64% of the account. That is [[Scaling Models#SC-058|SC-058]].

On Monday a dataset landed that disagrees, and it came from the same operator who taught us the law.

Across an estimated $50 to $100 million of Black Friday spend, the top single ad held **7%**. The top 20 ads held **46%**. So the bottom 80% of ads held **54%** of the money. And concentration **fell** as accounts got bigger: the top 20% of ads held 53% of spend on accounts under $250k of November spend, then 44%, then 33% on the largest. That is [[Scaling Models#SC-163|SC-163]].

I went to check it against our own five accounts. Two things came back. One is a measurement trap that I expected to dissolve the finding and instead strengthened it. The other is the reason none of our accounts can be read this way at all.

## 1. The mechanism

Think about a four-lane motorway.

At two in the morning, everybody is in the fast lane. Count the cars and you would conclude that drivers overwhelmingly prefer lane one. At eight in the morning the same road carries traffic spread across all four lanes, and if you only had the counts you would conclude that drivers changed their minds overnight.

Nobody changed their mind. Lane one moves a fixed number of cars per hour. Under light traffic it swallows all of them. Under heavy traffic it fills, and the overflow has nowhere to go except the other three lanes.

Concentration in an ad account works the same way, and [[Creative Science#CR-255|CR-255]] is the claim that supplies the lane capacity. A single ad can absorb only so much money in a day before each extra dollar buys a worse conversion. In the portfolio behind these numbers the largest single ad ever recorded peaked at **$12,500 a day**, most evergreen winners ran **$4,000 to $8,500 a day**, and the working ceiling is called at **$10,000 to $12,000**.

So push $150,000 through an account on one day and the winners physically cannot carry it. The tail is not insurance and it is not sloppiness. It is the other three lanes.

That is why concentration decompresses under a peak ramp and compounds at ordinary spend. It is a reading of traffic density, not a reading of preference. Which means the number is only interpretable if you know how hard the road is being pushed.

## 2. The evidence

**[[Scaling Models#SC-163|SC-163]], T3.** The concentration curve and the falling-with-size bracket table. It is a real pull from the Meta MCP across a large portfolio, which is more than SC-058 has ever shown, and it is still T3 because the figures were described off slides rather than published.

**[[Scaling Models#SC-058|SC-058]], T3.** The compounding-Pareto law. Asserted across two videos, no dataset shown, and it now carries SC-163 as a boundary rather than a refutation. Both are T3. Neither can decide anything on its own, and when two T3 claims disagree the honest position is to name the window each was measured in.

**[[Creative Science#CR-255|CR-255]], T3.** The per-ad daily ceiling and the method that divides peak daily spend by it.

**[[Meta Delivery & Andromeda#MD-137|MD-137]], T3.** How many ads the platform actually funds scales with spend, and at $20,000 to $30,000 a month it is about one.

**[[Scaling Models#SC-167|SC-167]], T3.** The tail priced from the other direction: 52 of 60 ad sets spending with zero sales, about $200 a day, roughly $6,000 a month.

**[[Scaling Models#SC-168|SC-168]], T2.** Banked today off our own five export windows. The measurement half of this lesson.

Note what the tier column is doing here. Every claim above is T3 except the one built from our own files. A T3 majority is not a consensus, it is five operators with no shown test. Our own exports are the only T2 in the list, and they are T2 because the arithmetic is reproducible from a file on this machine.

## 3. Our accounts

### The trap I went looking for

There are two ways to state concentration and they are not the same instrument.

**Absolute:** the share of spend held by the top 1, 3, 5, 10, 20 ads.
**Relative:** the share held by the top 20% of ads.

The relative one moves when you launch an ad, with no change in delivery whatsoever. Here is what happens when I add twelve ads spending fifty cents each to our real files:

| Account, window | Ads | Top 20% share | Same, plus 12 dead ads | Top 5 share | Same, plus 12 dead ads |
|---|---|---|---|---|---|
| ChiroWorks, 11 to 20 Sep | 22 | 87.7% | **96.4%** | 92.9% | 92.0% |
| StayWell, 11 to 20 Sep | 12 | 73.4% | **93.3%** | 95.0% | 93.3% |
| SJR Commercial, 9 to 16 Jun | 52 | 61.1% | **71.3%** | 36.5% | 36.4% |

The top-20% column moves nine to twenty points on ads that spent six dollars between them. The absolute column does not move at all. The relative metric is partly a measurement of how many ads you launched, so it cannot be compared across two accounts with different ad counts and it cannot be tracked over time in an account that is launching.

**Then the direction saved the finding.** Adding dead ads pushes the relative number **up**. Bigger accounts run more ads. SC-163 reports concentration going **down** as accounts get bigger, from 53% to 33%. So the artefact runs against the headline, and for that table to come out the way it did, real spend has to be moving into the tail hard enough to beat an artefact pushing the other way. I went to break the claim and made it stronger.

### The arithmetic nobody flagged

[[Creative Science#CR-255|CR-255]] forecasts winners by dividing peak daily spend by per-ad capacity: $150,000 a day at $10,000 to $12,000 per ad gives **12 to 18 winners**. [[Scaling Models#SC-163|SC-163]] separately reports the top ad at **7%** of spend. One divided by 0.07 is **14.3**.

Those are not two findings. Total spend divided by the top ad's spend **is** one over the top ad's share, always. I checked it on all five of our windows and it holds to nine decimal places on every one. So CR-255's "12 to 18" is not independent corroboration of SC-163's 7%. It is the same measurement restated, and quoting both as if they agree double-counts one slide.

The identity is trivial. What it means is not, and this is the part worth carrying.

### Why our accounts cannot be read this way

| Account | Window | Ads spending | Spend | Per day | Top ad per day | Top ad share | 1 / share |
|---|---|---|---|---|---|---|---|
| SJR Commercial | 9 to 16 Jun | 52 | $4,897.15 | $612.14 | $66.39 | 10.8% | 9.2 |
| SJR Commercial | 10 to 20 Jul | 8 | $1,024.02 | $93.09 | $56.83 | 61.0% | 1.6 |
| ChiroWorks | 11 to 20 Sep | 22 | $624.10 | $62.41 | $24.76 | 39.7% | 2.5 |
| StayWell | 11 to 20 Sep | 12 | $337.49 | $33.75 | $21.48 | 63.6% | 1.6 |
| Phoenix Truxx | 17 to 24 Apr | 5 | $581.86 | $72.73 | $34.03 | 46.8% | 2.1 |

Put SJR's June row beside Blue Sense's. Their top ad holds 7% of the account. Ours holds 10.8%. The two percentages are close enough to look like the same reading.

They are opposites. Their top ad is sitting at roughly $10,000 a day because that is all it can take. Ours is sitting at **$66.39 a day** because that is all it was offered.

StayWell is the cleanest case. Its best ad in that window absorbed **$21.48 a day** out of a **$33.75** daily account budget. One over 63.6% is 1.6, and it does not mean StayWell needs 1.6 winners. It means the budget only funded 1.6 ads' worth of spend. There is no ceiling in that file anywhere.

This is [[Meta Delivery & Andromeda#MD-137|MD-137]] showing up as arithmetic. Every client on our book is under $30,000 a month, so the platform funds roughly one ad, and the tail on our accounts is not overflow. Nothing overflowed. A ceiling and a budget produce the same number in the spend column, and the column cannot tell you which one you are looking at.

### The leakage half, priced

[[Scaling Models#SC-167|SC-167]] draws the distinction that decides what to do: **a tail that spends and converts is capacity, a tail that spends and does not convert is leakage, and only the results column separates them.** Run on opt-ins rather than sales:

| Account | Window | Zero-opt-in ads that spent | Spend on them | Share of spend | Per day |
|---|---|---|---|---|---|
| SJR Commercial | 9 to 16 Jun | 19 of 52 | $106.89 | 2.2% | $13.36 |
| ChiroWorks | 11 to 20 Sep | 16 of 22 | $35.55 | 5.7% | $3.56 |
| StayWell | 11 to 20 Sep | 10 of 12 | $98.05 | 29.1% | $9.81 |
| Phoenix Truxx | 17 to 24 Apr | 2 of 5 | $0.93 | 0.2% | $0.12 |

SJR's 19 dead ads have a median spend of **$3.68** and a maximum of **$29.01** across eight days. StayWell's 29.1% is the worst share on the book and it is **$9.81 a day**, against SC-167's $200 a day.

So the cleanup is worth about ten dollars a day at our worst account. That is a tidiness decision, not a money decision, and it is worth saying out loud so nobody spends an afternoon on it expecting $6,000. [[Meta Delivery & Andromeda#MD-163|MD-163]] argues the other way anyway, that cutting ads the model is still learning from manufactures the volatility we then blame on Meta, and that tension is live in the codex with no test on either side.

One caution on the StayWell row. Twelve ads produced twelve opt-ins in ten days, and ten of the twelve ads produced none. A window that thin cannot separate a bad ad from an unfunded one, so read it as a spend figure and not as a ranking.

### The row that is still in the file

The SJR export ships an unnamed total row. In the June file it carries **$4,897.15**, which is exactly half of the file's $9,794.30, with 783 opt-ins split 560 Meta and 223 website. Sort by spend and it lands at the top and reads as the account's biggest ad holding 50.0% of spend.

That is lesson 031's sum, still sitting there, and it would have doubled every concentration figure above. Dividing it out gives **$6.2543**, the exact cost per opt-in lesson 031 printed, which is how it is confirmed as the account total rather than an ad. Every number in this lesson excludes it.

## 4. The decision rule

**Before you read a concentration number as a fact about your ads, check whether the top ad was ever offered more budget than it absorbed. If it was not, the number is measuring your budget. And state concentration as a count of ads, never as a share of them, because a share moves when you launch.**

## 5. Quiz

Drop your answers in `_answers-inbox.md`. Lesson number plus answers is enough. Partial is fine.

**1.** SC-058 says a CBO compounds until about 4% of ads hold about 64% of spend. SC-163 measured the top 20 ads at 46%. Say why SC-163 was banked as a boundary on SC-058 rather than as a refutation, and name the one test that would settle it.

**2.** An account reports that its top 20% of ads hold 91% of spend. You then launch ten ads and eight of them spend under a dollar. Without touching delivery, which way does the 91% move, and why does that disqualify the metric for tracking an account over time?

**3.** Kartik looks at ChiroWorks for 11 to 20 September: 22 ads, $624.10, top ad $247.61, so 39.7% in one ad. He says we are dangerously concentrated against Blue Sense's 7% and need more winners. Write the two sentences you say back.

**4.** StayWell, 11 to 20 September: $337.49 across 12 ads, and 10 of them produced zero opt-ins on $98.05, which is 29.1% of spend. A buyer proposes switching those 10 off to recover the money, citing SC-167's $6,000 a month. Say whether you do it and name the two numbers that decide.

**5.** You want to know whether SJR's top ad is at a ceiling or at a budget. Name the one test that answers it and say what result would mean "ceiling".

> [!note]- Answer key
>
> **1.** SC-163 was measured in a Black Friday window where spend per account runs several times its evergreen level, and SC-058 describes behaviour at ordinary spend, so the two are not measuring the same road. The reconciling mechanism is CR-255's per-ad daily ceiling: concentration compounds while the winners still have headroom and decompresses once account spend exceeds what they can carry. Worth adding that both claims are T3, and that SC-058 has never shown a dataset while SC-163 has, so they are not equally supported even at the same tier. **The settling test is one account measured on both windows, peak and evergreen, on the same concentration metric.** Nobody has run it.
>
> **2.** It goes **up**. The 20% cut widens as the ad count grows, so it captures more ads and therefore more spend, while delivery is unchanged. On our own files twelve fifty-cent ads take ChiroWorks from 87.7% to 96.4% and StayWell from 73.4% to 93.3%, and the top-5 share over the same change moves 92.9% to 92.0% and 95.0% to 93.3%. It is disqualified for tracking because any account that is launching ads will show rising concentration from the launches alone, so the metric cannot separate a delivery change from a publishing schedule. Use an absolute top-N count. **Bonus if you spotted it: the artefact pushes up and SC-163 reports concentration falling as accounts grow, so the artefact works against that headline rather than explaining it away.**
>
> **3.** Something like: "The two percentages are not the same measurement. Their top ad holds 7% of an account spending millions a day and it is pinned at about $10,000 a day because that is its ceiling; our top ad holds 39.7% of $62.41 a day and it is sitting at $24.76 a day because that is what the budget offered it. Second, MD-137 says that under $30,000 a month Meta funds roughly one ad anyway, so 39.7% is the expected reading on an account our size and it is not a risk signal. More winners is not what that number is asking for."
>
> **4.** **No, or at least not for the money.** The two numbers that decide are **the dollar amount per day and the opt-in count in the window.** $98.05 over ten days is $9.81 a day against SC-167's $200 a day, so the recoverable sum is about one four-hundredth of the figure being cited. And the account produced twelve opt-ins in ten days, so a ten-day window cannot tell a bad ad from an unfunded one, which is exactly the confusion SC-058's ABO-for-diagnosis note and MD-163 both warn about. Switch them off for tidiness if you like. Do not book it as savings and do not present it as a performance action.
>
> **5.** **Raise that one ad's budget and see whether it takes the money at a stable cost per opt-in.** Ceiling means the extra spend arrives at a worse cost per opt-in, or the ad declines to absorb it and delivery spreads to other ads instead. Budget means it absorbs the increase at roughly the cost it was already running. The spend column can never answer this on its own, which is the whole point of the lesson: both states print the same number. Also accept CR-255's own cheaper first read, pull the highest daily spend any single ad in the account has ever reached, because if no ad has ever exceeded $70 in a day then nothing on the account has met a ceiling.
>
> **Carry forward.** SC-168 is banked at T2 on five windows across four accounts, and every one of them is a different date range, so the table above compares accounts and not periods. The cheap upgrade is one common window pulled on all five, which turns five readings into a comparison. The expensive and more valuable one is the SC-163 settling test, and we cannot run it, because no account on our book has ever pushed a peak ramp.
