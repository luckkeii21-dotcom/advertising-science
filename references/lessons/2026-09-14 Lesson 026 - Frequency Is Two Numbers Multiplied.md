---
title: "Lesson 026 - Frequency Is Two Numbers Multiplied"
type: lesson
lesson: 26
date: 2026-09-14
topic: Meta Delivery & Andromeda
claims: [MD-155, MD-138, MD-051, MD-107, MD-053, MD-133, MD-147, MD-079, MD-008, AT-059, AT-100]
tags: [advertising-science, lesson]
---

# Lesson 026 · Frequency Is Two Numbers Multiplied

🎬 **Lesson video (2m 32s, silent, watch anywhere):** [[video/2026-09-14-lesson-026.mp4]]

A client looks at the top of Ads Manager and sees frequency 3.2. He says you are hammering the same people. Somebody on the call agrees and asks for new creative. This lesson is about why 3.2 almost never means what everyone in that room thinks it means, and about the four-minute check that tells you what it does mean.

## 1. The mechanism

Say you eat at the same place near Karol Bagh. Over a month the owner says his regulars came 3.2 times each. Nobody concludes that the regulars ate the biryani 3.2 times. They came twice for the biryani and once for the rolls. Two dishes, roughly 1.6 helpings each. If the owner reads 3.2 as "people are sick of my biryani" and changes the recipe, he has fixed a thing that was working and has learned nothing about why people come.

Meta prints the owner's number at every level of the account, and it prints the dish-level number one row down. They are connected by arithmetic that nobody states out loud.

Impressions add up. Reach does not. If one person sees three of your ads, each of those three ads counts her once in its own Reach cell, so summing the ad rows gives you three, while the account counted her once. That gap is information rather than an error to be cleaned up. The codex already holds the same shape for audience segments, where segment reach sums to more than the account actually reached because one person crosses buckets ([[Attribution & Incrementality#AT-059|AT-059]]).

Write it out and the whole thing falls open:

`account frequency  =  average frequency of the ads  ×  how many different ads one person saw`

Both factors are yours. Only the first one can burn out. The second one is creative breadth, which is the thing you are supposed to be building. A high account frequency sitting on top of a wide portfolio is the system working.

This is the multiplicative twin of the weighted-average law from lesson 023. There, a blended cost per opt-in moved because the money sat somewhere else. Here, a blended frequency reads high because the person saw more of your ads. Same disease. A true number answering a question nobody asked.

We already had one instance of this on file and never saw it as general. [[Meta Delivery & Andromeda#MD-107|MD-107]] (T2, shown on screen) records a flexible-media ad whose parent read 5.31 while every asset inside it sat near 2, and the honest resolution there is already written down: the parent is a real per-person exposure count across the whole unit, the child is a per-creative count, and which one you want depends on the question. That is the identity above, observed at one level and never generalised.

## 2. The evidence

[[Meta Delivery & Andromeda#MD-138|MD-138]] (T3) is where this pass started, and it ships with its own protocol: pull the last 90 days at ad level, exclude retargeting, and most ads will not have a frequency above two, while the account or campaign number will read three to six. His stated cause is that Meta rarely serves the same creative to one person more than twice, because purchase probability drops after two impressions.

Guard that sourcing hard. He attributes the two-impression rule to Meta with "Meta has said, I believe a few years ago" and no link, in the same video where he does link a Meta article. So the ceiling is T3 testimony about a platform claim. It is not a platform document and it must never acquire a number.

[[Meta Delivery & Andromeda#MD-051|MD-051]] (T3) is the same observation from a second operator, at 30 to 60 days on cold campaigns, treating any cold ad above 2 as fix-now. It carries a warning that matters for the audit: a flexible-media ad throws a false positive here, because of MD-107. A third operator puts the cold line at 1.5 and attaches no window, which makes it unusable, because a frequency means nothing until you say per day, per week or per month ([[Meta Delivery & Andromeda#MD-008|MD-008]]).

[[Meta Delivery & Andromeda#MD-053|MD-053]] (T3) supplies the money version. Cost per 1,000 people reached equals CPM times frequency, and it ships as a selectable column. CPM is a price you mostly cannot move, so every lever on the cost of reach is a frequency lever.

[[Meta Delivery & Andromeda#MD-133|MD-133]] (T2) is the other frequency cut, by audience segment over 30 days: new 2.9, engaged 9.5, existing 36. Different window and different level, so it does not compare directly with MD-138.

What was missing was anybody doing the arithmetic on a real account. That is [[Meta Delivery & Andromeda#MD-155|MD-155]], banked today at T2 on our own exports.

## 3. Our accounts

Three accounts, three windows, every figure recomputed from the raw ad-level exports on disk.

**ChiropracticWorks, 10 to 27 July 2026, 18 days, $890.84.**

| | |
|---|---|
| Impressions | 28,341 |
| Unique people reached | 8,869 |
| **Account frequency** | **3.1955** |
| Live ads | 52 |
| Sum of the ads' own reach cells | 15,215 |
| Average frequency of the ads | 1.8627 |
| Different ads one person saw | 1.7155 |

1.8627 × 1.7155 = 3.1955. Meta printed 3.19551246.

**The account read 3.2 and not one ad reached it.** The highest single ad was `Before / After IMG - 3` at 2.857 and the next was `Want to lose weight without surgery?` at 2.277. Forty-eight of the 52 ads sat at or below 2, which is 92.3%. So MD-138's prediction held on our book, and the leftover 1.7155 was the average person in Collinsville seeing about two different ads from this clinic.

The cost version, since CPM was $31.43: cost per 1,000 people reached was $100.44, which is exactly $31.43 × 3.1955.

**SJR Commercial, 10 to 20 July 2026, 11 days, $1,024.02, 256 opt-ins.** The two campaigns we run, the same export lesson 023 used.

| | |
|---|---|
| Impressions | 50,128 |
| Unique people reached | 29,944 |
| **Account frequency** | **1.6741** |
| Live ads | 8 |
| Average frequency of the ads | 1.5312 |
| Different ads one person saw | **1.0933** |

1.5312 × 1.0933 = 1.6741. Meta printed 1.67405824. Zero of the eight ads cleared 2, and the top one stopped at 1.999, which is `DUMP_05_Brand Authority`.

**StayWell Spine & Joint, 17 to 23 August 2026, 7 days.** One campaign delivered that week.

| | |
|---|---|
| Impressions | 5,674 |
| Unique people reached | 2,887 |
| **Campaign frequency** | **1.9654** |
| Live ads | 12 |
| Average frequency of the ads | 1.3869 |
| Different ads one person saw | 1.4170 |

1.3869 × 1.4170 = 1.9654. Meta printed 1.965362.

**Put the second factor beside itself and you get a portfolio reading nobody on this book has ever taken.** ChiroWorks 1.72, StayWell 1.42, SJR 1.09. Same platform, same summer, three very different accounts. On SJR the average person we reached saw almost exactly one of our ads, so eight live creatives behaved as one creative per person. Whatever creative diversity buys, SJR was not buying it in that window at that budget.

**And the pool is nowhere near empty.** ChiroWorks reached 8,869 people in 18 days. Metro East holds about 700,000 and the vault puts a tight radius at 300,000 to 500,000. So we touched 1.3% of the catchment, and under 3% of the tightest version of it. For 8,869 to be a tenth of the addressable pool, that pool would have to be about 88,700 people. That is the number that turns a frequency argument into an arithmetic one, and it is why [[Meta Delivery & Andromeda#MD-147|MD-147]]'s rolling-reach instrument is worth building for a city-radius client: the ceiling on new people is the catchment, and we have never once measured how close we are to it.

### The limits, and they are real

The identity is arithmetic. It holds on every account always, and finding that it held on ours proves nothing about Meta. **What is empirical here is the size of the two factors**, and that is what we did not know yesterday.

Our windows are 7, 11 and 18 days. MD-138 specifies 90. A shorter window mechanically lowers every frequency in it, so none of this tests his 90-day claim, and the account figures below 3 on SJR and StayWell are what an 11-day and a 7-day window should look like. The decomposition itself does not care about the window.

None of the three windows had a retargeting campaign in it to exclude, so the protocol's exclusion was satisfied by accident rather than by design. And we did not check whether any of these ads is a flexible-media ad. If `Before / After IMG - 3` is one, its 2.857 is a parent aggregate and carries no fatigue signal at all, per MD-107. That check is one click and nobody has done it.

## 4. The decision rule

**Never read a frequency above ad level as fatigue. Pull the ad-level frequencies underneath it first. Fatigue can only live in those, and whatever is left over after you divide is the number of your own ads one person saw.**

The four-minute version, for any account, any Friday:

1. Ads Manager, ad level, your window, columns for Impressions, Reach and Frequency.
2. Read the account or campaign frequency at the top.
3. Divide it by the spend-weighted average of the ad-level frequencies.
4. The quotient is how many different ads the average person saw. The divisor is the only part new creative can fix.

Two things follow that are worth saying to a client. A cold ad above 2 is a real signal and it is a signal about one ad ([[Meta Delivery & Andromeda#MD-051|MD-051]]). An account above 3 with every ad below 2 is a signal about breadth, and the honest sentence is that they are seeing more of your work rather than more of the same thing.

If you want to know whether you are buying pressure or buying people, the cheapest test in this whole cluster is [[Meta Delivery & Andromeda#MD-079|MD-079]] (T2, shown): cut the budget materially, hold everything else, and watch frequency. Flat frequency means you were buying pressure. Falling frequency means you were buying reach.

## 5. Quiz

Five questions. Put answers in `_answers-inbox.md`, any format, partial is fine.

**Q1.** Explain in one paragraph why summing the Reach column across twelve ads does not give you the campaign's reach, and say what that sum is actually a count of.

**Q2.** *(Applied.)* ★ A client's account reads frequency 4.6 over 30 days. You pull ad level and the spend-weighted average ad frequency is 1.9. Work out the second factor. Then say what you would recommend, and what you would recommend if the ad-level average had come back at 4.4 instead.

**Q3.** *(Applied.)* ★ SJR's 1.09 is the finding in section 3 that costs money. Eight live ads, and the average reached person saw one of them. Give two mechanisms that could produce that number, say which of our own codex claims predicts each, and name the one export or column you would open first to tell them apart.

**Q4.** Argue the opposite. Build the strongest case that ChiroWorks' 3.1955 really was a fatigue problem in July. Then name the single check that would settle it, and say which way it has to read for your case to survive.

**Q5.** MD-155 is banked at T2 on our own exports. Say precisely what it establishes and what it does not, and name what a T1 version of it would require.

> [!note]- Answer key
>
> **Q1.** Each ad's Reach cell counts a person once if she saw that ad at least once in the window. A person who saw three ads is counted once in each of those three cells and once at campaign level. So the sum across ads counts person-and-ad pairs rather than people, and it is always greater than or equal to the true unique reach. Full marks for naming it as person-ad pairs and for connecting it to **AT-059**, which records the same non-additivity for audience segments. Credit also for noting that impressions do add, which is the reason the decomposition works at all.
>
> **Q2.** 4.6 / 1.9 = 2.42, so the average reached person saw about two and a half different ads. That is a wide portfolio doing its job and there is no fatigue signal in it. The recommendation is to leave the creative alone and go look at reach against the catchment instead, because a frequency of 4.6 over 30 days with a small pool is a pool problem. **If the ad-level average had come back at 4.4, the second factor is 1.05 and the diagnosis inverts completely**: one creative is reaching the same person more than four times in a month, which is above every threshold in the codex, and new creative is exactly the answer. Same headline number, opposite decision, and the only thing separating them is the row underneath. Half marks for the arithmetic without both recommendations.
>
> **Q3.** Mechanism one: the eight ads are not really eight, because near-duplicates collapse into one delivery entity, which is **MD-003** and also the reason the creative-diversity law has an evidentiary hole. Mechanism two: budget concentration, where Meta funds about one ad at our spend level and the other seven never bought a real chance, which is **MD-137** with **MD-136** supplying the marginal-CPA reason and **MD-148** showing we already recovered a 363-opt-in anchor from exactly that pattern on Phoenix Truxx. The export that separates them is the ad-level spend column already in the file: if seven ads are starved, the spend split shows it immediately and it is concentration. If all eight were funded and one person still saw only one, collapse is the live hypothesis. **In this window it is concentration and the file says so**: `UGC Inspirational` took $625.12 of $1,024.02. Full marks require naming the column and reading it rather than choosing a side.
>
> **Q4.** The strongest opposing case: 3.1955 over 18 days is high for a clinic whose catchment is one side of a river, the top ad hit 2.857 which is above both MD-051's line and MD-138's, cost per 1,000 people reached was $100.44 against SJR's $34.20 in an overlapping window, and CPM times frequency says the frequency is the half of that we can move. **The check that settles it is the ad-level frequency distribution against the spend split.** For the fatigue case to survive, the ads carrying the spend have to be the ads with the high frequencies. They are not: the two biggest spenders sat at 2.277 and 1.925, 48 of 52 ads were at or below 2, and the leftover factor was 1.72, so the account number was built out of breadth. Credit for adding the second check, which is whether `Before / After IMG - 3` is a flexible-media ad, because if it is, its 2.857 is a parent aggregate and the fatigue case loses its only piece of evidence.
>
> **Q5.** It establishes that the decomposition is exact on real Meta exports, to four decimal places, on three separate accounts, and it establishes the observed size of both factors at our spend and our window lengths: ads-per-person of 1.09, 1.42 and 1.72, and ad-level frequency averages between 1.39 and 1.86. It does not establish anything about why Meta's delivery produces those sizes, it does not test MD-138's two-impression ceiling because arithmetic cannot test a behavioural claim, and it does not test his 90-day protocol because none of our windows is 90 days. **A T1 version does not exist**, because T1 means platform documentation and Meta does not document this decomposition. The honest ceiling for the sizes is T2, and the right next move is running the same pull at 90 days and at a matched window on all four accounts, so the second factor becomes a tracked series instead of three readings. Credit for spotting that the identity half of the claim needs no tier at all, since it is arithmetic.

---

**Related:** [[Meta Delivery & Andromeda]] · [[Attribution & Incrementality]] · [[2026-09-11 Lesson 023 - Nothing Got Worse and the Number Did]] · [[2026-08-26 Lesson 008 - The Split You Never Chose]] · [[2026-08-29 Lesson 011 - Every Ad Has a Ceiling]] · [[2026-09-10 Lesson 022 - An Empty Row Has Two Causes]] · [[ChiroWorks]] · [[SJR Commercial]] · [[Chiropraise]]
