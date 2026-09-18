---
title: "Lesson 030 - Above Average Against Whom"
type: lesson
lesson: 30
date: 2026-09-18
topic: Creative Science
tags: [advertising-science, lesson, creative-science]
---

# Lesson 030 · Above Average Against Whom

Meta puts three free grades on every ad you run. Quality ranking, Engagement rate ranking, Conversion rate ranking. They sit in Ads Manager, they cost nothing, and almost nobody reads them. Today they got read across three of our accounts for the first time, and they do something different from what the name suggests.

## 1. The mechanism

Each of the three is a **percentile against other ads competing for the same audience**. The grade is a position in a queue. Meta picks the queue.

Think about a school rank. First in a class of twelve and fortieth in a class of six hundred are not the same achievement, and neither number says how good the student is at the subject. Move that same student between the two schools and the rank changes while the student does not. **The rank measures the room.**

Three things follow, and all three show up in our data.

- Two ads in one account chasing different audiences get graded against different rooms. Putting their letters side by side is comparing school ranks across schools.
- An account whose whole book outruns its category gets the same letter for nearly everything. The column stops separating anything.
- The grade moves when your competitors change their ads. Yours can sit untouched and still slide.

The documented floor is 500 impressions before any grade appears, and the bands are percentiles: Below average is the bottom 35%, Average sits around the 35th to 55th, Above average is the top 55%.

**One honesty note before the numbers.** Meta's own help pages would not open to an automated read today. They return a title and no body, so the spec above comes from secondary summaries rather than from the source. Everything below this line is measured off our own export files and does not depend on it.

## 2. The evidence

- **[[Creative Science#CR-176|CR-176]], T2.** Hook rate does not reliably predict cost per result, shown on screen: a 15.55% hook rate delivered £11.02 per booked call while a 27% hook rate cost over £30 in the same account.
- **[[Creative Science#CR-018|CR-018]], T2.** A low hook rate does not mean a losing ad. An ad can filter hard at the top and still buy customers cheaply.
- **[[Creative Science#CR-122|CR-122]], T3.** The ordering of proxies for creative quality: amount spent first, CPA second, CPC and CTR third, hook and hold rate as diagnostics only.
- **[[Learning & Signal#LS-081|LS-081]], T2, banked yesterday.** Meta's Results column is not a unit. It prints whatever each ad set optimises for.
- **[[Creative Science#CR-248|CR-248]], T2, banked today.** The claim this lesson is built on.

Notice the shape CR-176 and CR-018 share. A platform-supplied number that looks like a verdict on creative turns out not to predict cost per result. Today's finding is that same shape on a different column, measured on our own book instead of somebody else's screen.

**Two claims already in the codex set up the whole thing, and they are both T1.**

**[[Auction Mechanics & Bidding#AU-002|AU-002]], T1,** is Meta's own sentence: "Together, estimated action rates and ad quality measure ad relevance. Because these are components of the auction, an ad that's more relevant to a person could win an auction against ads with higher bids." So an ad-quality estimate really is inside the auction. Hold that thought.

**[[Google Auction & Smart Bidding#GA-010|GA-010]], T1,** is the same story told on Google, and it is the one to reason from. Quality Score's three components are rated **Above average / Average / Below average by comparison with advertisers whose ads showed for the same searches over the past 90 days**, and Google states outright that Quality Score is not an input in the auction. Identical scale, identical comparison-pool logic, and a platform saying in writing that the displayed grade is a diagnostic rather than the machinery.

Put the two together and the shape is clear. The auction consumes an internal estimate of ad quality. The column hands you a percentile of that estimate against a pool the platform chose. **Two different objects with one name.**

**What the codex had on this before today: almost nothing.** The phrases "quality ranking" and "conversion-rate ranking" appear five times in the whole science folder, and every one of them traces to a single finding, the twin-ad divergence in AT-107 and its lesson 012, where one sentence used the rankings as corroboration. Creative Science, the topic that owns creative, had zero. Nobody had ever asked what the columns measure, and no claim had ever been built on them. A free, always-on, per-ad diagnostic sat unopened for a month of daily research.

## 3. Our accounts

Week of 24 to 30 August 2026. Three accounts, 136 ads, $6,307.80 spent.

### The column is nearly blank

| Account | Ads | Spend | Quality graded | Conversion graded | Share of spend under a conversion grade |
|---|---|---|---|---|---|
| SJR Commercial | 53 | $4,440.35 | 27 | 20 | 70.8% |
| Phoenix Truxx | 33 | $1,387.77 | 9 | 3 | 52.4% |
| ChiroWorks | 50 | $479.68 | 1 | 1 | 40.3% |

Three ads carry the conversion grade on Phoenix Truxx. One carries it on ChiroWorks. Anything you would do with that column on those two accounts, you would be doing on a tenth of the book.

### The grade is a property of the account, not the ad

Twenty-four conversion grades exist across the three accounts. Here is every one of them.

- **SJR Commercial: 19 Above average, 1 Below average.**
- **Phoenix Truxx: 3 Above average, 0 anything else.**
- **ChiroWorks: 0 Above average, 1 Below average.** The prior week, 17 to 23 August, ChiroWorks carried two conversion grades and **both were Below average**.

Twenty-two of twenty-four are Above average, and both exceptions live in the one account selling something different in a different auction. **The column is close to constant inside an account and it flips between accounts.** A grade that gives the same answer for 19 of 20 ads is not ranking those ads. It is telling you about the room.

### Inside one door, the grade runs backwards

SJR's website-opt-in ad sets, 18 ads, one optimisation event throughout, so the unit is fixed and LS-081 cannot contaminate it.

| Quality ranking | Ads | Opt-ins | Spend | Cost per opt-in |
|---|---|---|---|---|
| Above average | 2 | 76 | $346.51 | **$4.5593** |
| Average | 7 | 221 | $874.73 | **$3.9581** |
| Below average | 1 | 72 | $254.08 | **$3.5289** |

Monotone, and pointing the wrong way. The one Below-average ad, `JFF Its back`, produced **72 opt-ins at $3.53**, more opt-ins than any other website ad in the account and the cheapest of the three tiers.

**Do not oversell this.** The Below tier is a single ad. The Above tier is two ads sitting in one ad set. This is a suggestive table on 18 ads in one week, and it is nowhere near enough to say the ranking is inverted in general. What it is enough for: the grade did not pick the winner here, so it cannot be trusted to pick the winner on its own.

### The one time it was right, it was righter than the column you actually read

Yesterday's lesson found `Hal w hook` in the `NJ/SI - Halal - SOKAL wesbite` ad set showing **$0.36 per result**, the cheapest number in SJR, and the results turned out to be **page views**. 659 of them.

That ad's grades: **Quality Below average. Conversion rate Below average.** It is the **only** Below-average conversion grade in a 53-ad account.

The column everyone reads crowned it. The free column nobody reads flagged it. Both were on the same screen.

### The 500-impression floor does not describe our file

- 35 SJR ads cleared 500 impressions in the week. **27** got a quality grade.
- **8 ads cleared 500 and got nothing.** The largest took **5,613 impressions**.
- **15 ads cleared 500 with no conversion grade.** The largest took **12,941 impressions**, the second-biggest ad in the account.
- Inside one ad set, `EN-> open targeting`, same optimisation event, same last-edit date: **`Dump Testimonial 02` at 970 impressions is graded Average, and `DUMP_05_Brand Authority` at 5,613 impressions is graded nothing.** Five point eight times the impressions, same room, no grade.

That last pair rules out the obvious explanations. Same ad set, so the audience is shared. Same event, so the objective is shared. Same edit date, so the reset history is shared. **Our export file cannot explain it, and I am not going to invent a reason.** What it does establish is that you cannot predict which of your ads will carry a grade, which is a second reason the column cannot be a ranking tool.

## 4. The decision rule

**Read the three rankings as a description of the auction you are buying in, and never let one move budget until you have checked cost per opt-in inside a single optimisation event.**

The practical version, two lines long. A whole account sitting Above average tells you your category pool is soft and says nothing about which of your ads is best. A single Below-average conversion grade in an account full of Above ones is worth four minutes of your attention, because that is the column doing the one thing it can do: pointing at an outlier.

## 5. Quiz

Five questions. Answers go in `_answers-inbox.md`. Partial answers get graded.

**Q1.** A quality ranking is a percentile against what pool? Say why that makes two ads in the same account, running to different audiences, not comparable on their letters.

**Q2.** Phoenix Truxx showed 3 of 3 conversion grades Above average. ChiroWorks showed 2 of 2 Below average the week before and 1 of 1 Below average that week. A client reads both dashboards and asks which account has the better creative. Answer him in two sentences.

**Q3.** You inherit an account. One ad is graded **Below average** on quality and is the cheapest opt-in in the book. Another is graded **Above average** and is the most expensive. The previous manager has left a note saying to pause the Below-average one. What do you check before touching either, and in what order?

**Q4.** In SJR's website-opt-in door, quality ranking ran a specific direction against cost per opt-in. Name the direction, quote the three cost figures, and then say in one sentence why you would refuse to call it a finding.

**Q5.** `DUMP_05_Brand Authority` took 5,613 impressions and got no grade. `Dump Testimonial 02` took 970 impressions in the same ad set on the same optimisation event and got one. Give **two** explanations our export files could test and **one** that they could not. Say what pull you would run for the two.

> [!note]- Answer key
>
> **A1.** Other ads competing for the same audience. Two ads in one account pointed at different audiences are being percentile-ranked inside two different competitor pools, so the letters are ranks from two different schools. The same creative can be Above average against one pool and Below average against another with nothing about the ad having changed. A letter is only comparable to another letter drawn from the same pool.
>
> **A2.** Neither dashboard answers that, because the grade is a percentile against the other advertisers bidding for the same people, so it reads the strength of the competitor pool rather than the strength of our work. The comparison that answers him is cost per opt-in, held to one optimisation event per account, next to what an opt-in is worth in each business.
>
> **A3.** Check three things in this order. **First, the Result indicator on both ads**, because a Results column can hold several units at once (LS-081) and the cheapest ad in SJR turned out to be buying page views at $0.36. **Second, whether the two ads sit in the same ad set and event**, because if they do not, neither their letters nor their cost per result are comparable. **Third, the grades themselves, last**, and only as a flag worth investigating rather than as a reason. Touch nothing until the first check comes back. On our own book the Below-average ad delivered 72 opt-ins at $3.53, more than any other ad in its door, so the note in the account is exactly the mistake this lesson exists to stop.
>
> **A4.** Backwards. Above average $4.5593, Average $3.9581, Below average $3.5289 per opt-in, monotone in the wrong direction. It is not a finding because the Below tier is one ad and the Above tier is two ads sitting in a single ad set, so the table describes three or four creatives over one week rather than a relationship. Extra credit for naming what would make it one: the same decomposition across several weeks and both accounts that carry the column.
>
> **A5.** **Testable from the files:** whether the graded ad had accumulated impressions in earlier weeks that the ungraded one had not, by summing impressions per ad name across the run folders from June onward; and whether the grade tracks the ad's own lifetime impressions rather than impressions inside the report window, by comparing the same two ads across the 21 to 27 August and 24 to 30 August exports, which overlap by four days. **Not testable from the files:** whether Meta withheld the grade because the ad's creative type is excluded from diagnostics, or because the ad was inside some internal measurement window, since neither fact appears in any column we export. The pull for the two: the same ad-level export with impressions and the three ranking columns, run for every week we hold, keyed on ad name.

---

**Where this sits.** Third lesson on Creative Science after 007 (hook rate ranks the wrong ad) and 016 (what a losing ad is allowed to disprove). It is the direct sequel to 029, which found the Results column carrying four units at once. Same account, same week, same screen, and the two columns disagreed about which ad was best.
