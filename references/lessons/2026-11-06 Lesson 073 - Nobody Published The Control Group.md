---
title: "Lesson 073 - Nobody Published The Control Group"
type: lesson
lesson: 73
date: 2026-11-06
topic: Attribution & Incrementality
claims: [AT-130, AT-131, AT-133, AT-125, AT-120, AT-121, AT-070, AT-003, GA-055, GA-088, MD-187]
tags: [advertising-science, lesson, attribution, incrementality, lift-studies, evidence-tiers]
---

# Lesson 073 · Nobody Published The Control Group

🎬 Video: [[video/2026-11-06-lesson-073.mp4]]

Topic: Attribution & Incrementality, rotation index 5, taken in the ordinary way. The research lane has opened no entry for today, so the newest banked work is yesterday's MD-198 and there is no harvest to teach. Three claims on this topic have sat untaught since the back half of October: [[Attribution & Incrementality#AT-130|AT-130]] and [[Attribution & Incrementality#AT-131|AT-131]] from 20 October, [[Attribution & Incrementality#AT-133|AT-133]] from 31 October. The first two arrived one day apart, from two platforms, about the same thing, and they only make sense read together. Friday, so video day.

## 1. The mechanism

A lift study is one idea and it is not complicated. Split the audience at random. One group is allowed to see your ads. The other group is not. Count what happened in both. The difference is what the advertising added.

Everything expensive about incrementality lives in the second group. The exposed half is just your campaign running. The holdout is the part somebody has to build, hold, and keep clean for the length of the test. **So a lift number is worth exactly what you know about the group that did not see the ads.**

The analogy that maps: a weighing scale. A dial reading 4.1 kilograms only means something if you know where the needle sat before the thing went on. Lose the zero and the dial is decoration. The control group is the zero.

There are three ways a lift number can reach you, and they are not close in value.

**One, you build the holdout.** You own the split, so you can see every flaw in it, including the ones that embarrass you. Slow and expensive, and the sample often fails.

**Two, the platform builds it and hands you a column.** Fast, free, and you cannot inspect the split.

**Three, somebody hands you the finished figure.** A case study, a keynote slide, a headline. Free, instant, and you cannot inspect anything.

In one week in October both big platforms shipped at the second and third levels, and they chose differently. Google shipped lift as something you can query. Meta shipped it as four stories.

## 2. The evidence

**[[Attribution & Incrementality#AT-130|AT-130]], T1.** Google Ads API v26, released 14 October 2026, from Google's own release notes and announcement post. A Search Lift study became an addressable resource: a read-only `SearchLiftKeywordBundle`, two new segments, three new enums, and **15 new Search Lift metrics**, of which Google names `relative_search_lift`, `normalized_incremental_searches`, `search_lift_cost_micros` and `search_lift_impressions`. The study attaches to a campaign through `Campaign.lift_measurement_config`.

That is a real change in kind. Every incrementality instrument this codex holds is a project you run. This one is a column you select. The counterfactual is maintained by Google and the output arrives in reporting.

Two guards sit on it. The design, the control construction, the exposure definition and the significance treatment are all Google's, **and none of them appears in the release notes.** And read what it measures: `normalized_incremental_searches` and `search_lift_impressions` are search behaviour. A Search Lift study answers "did the advertising make more people search". It is not an incremental cost per lead. Eligibility is stated nowhere.

**[[Attribution & Incrementality#AT-131|AT-131]], T1 for the sentences.** Meta, 19 October 2026, one day before Google's release. Four agency lift studies, eleven numbers, quoted verbatim in the claim. Tinuiti and DSW: 23% more total purchases, 45% more in stores, 15% better return on ad spend. WPP Media and Dior in Taipei: ad recall up 10.2 points, want-to-own up 7.7 points, 3.9x lift in incremental sales. AdYogi and Borosil: brand searches up 2.2x, unpaid search traffic up 24%, all search combined up 17%. And **C-4 Analytics and car dealerships: people who saw Meta ads looked at 7.67 times as many vehicle listing pages, and generated 14% more paid search traffic.**

Now the part that was checked rather than assumed. **No footnote. No asterisk, no source note, no "Meta internal data" line, no study date, no sample size, no test duration, no spend level on any of the four.** The cases are agency-supplied, and agencies submit the tests that worked.

Meta does one thing better than most of its pages: it names the method as a comparison against "a randomly selected control group", which is the right instrument. What is missing is every parameter of it. Holdout share, duration, power, and whether each quoted figure was the study's primary metric or one read off a panel of many.

**Learn the tier correctly here, because this pair is the clearest example in the codex.** T1 is a statement about provenance, not about quality. T1 means we read it at the source and the source is the platform itself. It does not mean the number is good. AT-131 is T1 and not one of its eleven numbers can be carried. Our own 21-day holdout at [[Google Auction & Smart Bidding#GA-055|GA-055]] is T2 and it decided a channel. **Tier tells you who said it and how directly. Only the method tells you what it is worth.**

**[[Attribution & Incrementality#AT-133|AT-133]] is the same reading problem with the opposite outcome.** Meta's "every US dollar spent with Meta generated US$4.13 in revenue, up 25% from 2022" carries a real footnote: a study run **13 to 20 April 2026**, over **one million ad campaigns**, following the framework from Tadelis et al., 2023, published with the NBER. That disclosure is better than Meta's house average. The figure is still unusable, for three reasons in order of severity. The window is **eight days** in mid-April, compared against a 2022 figure whose window is not stated. It is a blended mean across a million campaigns with no median and no spread. And it is revenue, not profit, on an ecommerce shape, while our revenue event sits weeks downstream in a CRM.

**The reading rule that falls out of AT-131 and AT-133 together: a footnote turns a figure from unverifiable into checkable, and the checking is the work, not a formality.**

Three more to hold. [[Attribution & Incrementality#AT-125|AT-125]], T1: Meta states a Conversion Lift study reaches a reliable read in 2 to 3 weeks at holiday conversion volume against 6 or more weeks in a quiet quarter, and the mechanism is only event volume. [[Attribution & Incrementality#AT-070|AT-070]], T3: Meta's geo lift product is gated at roughly $100,000 a month, asserted from practice with nothing shown and flagged for re-checking before anyone quotes it. [[Attribution & Incrementality#AT-120|AT-120]], T2: an independent vendor, Measured, ran geo test-versus-control across more than 10,000 campaigns and 200+ North American advertisers and put **64% of Meta's incremental conversions on new-to-brand customers**, with 2.3x higher incremental ROAS than search on new-customer acquisition. We read Meta's summary of that study, not the study.

## 3. Our accounts

**One of Meta's four cases is our vertical, and it is the one worth something to us.** We run two commercial truck dealerships on Meta, SJR Commercial and Phoenix Truxx, and both are reported on last click. AT-131 is Meta's own published claim that its ads moved dealership search behaviour: 7.67x vehicle listing page views and 14% more paid search traffic. The digits are unusable with no sample and no window. The direction is first-party support for a rule we already hold: **a zero in the last-click lead column is "no last-click leads attributed", and it is never evidence of waste.** It pairs with AT-120, where a geo-tested vendor put most of Meta's incremental value on buyers a keyword bid was never going to catch.

**Neither new instrument is open to us, and the reason is budget.** AT-070 puts Meta geo lift near $100,000 a month. AT-130 and AT-131 name no floor, which is not the same thing as having none. Our book, as of this week: SJR Commercial ran $767.78 for 136 opt-ins at $5.65 in the week of 23 to 29 October, roughly $110 a day. StayWell ran $562.63 for 23 at $24.46 in the same week. Phoenix sits at $160 a day on statics and $40 on dump since 3 November. RK Consumer Services was built paused on 5 November at $50 a day. **Nothing on that list is within two orders of magnitude of a geo lift gate.**

**The one real holdout on our book is also the honest picture of what we can do.** GA-055: a 21-day Demand Gen geo holdout produced **85 orders against the 166 required** for a statistically relevant read on new customers, while returning-customer orders rose 6.8%. That test did not find no lift. It found **not enough events to say**, which is exactly the failure AT-125's volume mechanism predicts, and it is the failure our budgets will produce every time.

**What we use instead, and it works.** The CRM count. Phoenix September read 706 leads at $8.18 in Ads Manager against **417 real CRM people at $13.86**. SJR the same month read 809 at $4.07 against **358 real at $9.19**. That is not incrementality and nobody should call it incrementality. It is the counting layer, and on our book it finds more money than any lift study we are eligible for.

**Two open items, and both are free.** [[Attribution & Incrementality#AT-121|AT-121]]: the new-to-brand share AT-120 turns on cannot be produced on any account we hold, because SJR's CRM returns 99.94% net-new when GoHighLevel merges a repeat opt-in on the email address. The instrument has to be built before the test can exist. And **Compare attribution settings has still never been opened on any account we hold, on any book, ever.** Named in lesson 071, carried unrun for the seventh day. One click, no spend.

## 4. The decision rule

**A lift figure is worth exactly what you know about its control group.** Built it yourself, report it with its sample and its power, including when the sample failed. Platform built it, call it the platform's estimate of its own effect and say so out loud. Arrived with no sample and no window, carry the direction and never the digits, and never put it in a proposal, a forecast or a client report.

## 5. Quiz

Drop your answers in `_answers-inbox.md`. Lesson number plus answers is enough.

1. AT-131 is T1 and none of its eleven numbers can be used. GA-055 is T2 and it settled a channel decision. Explain what tier is actually telling you, and what it is not.

2. AT-133's $4.13 figure carries a real footnote naming a date window, a campaign count and an academic framework. Give the three reasons the figure still cannot be carried, in order of severity, and say what the footnote did buy.

3. Applied. A Meta rep offers SJR Commercial a Conversion Lift study ahead of the year-end truck buying window. Name three things you do before you answer, the number from our own book that decides whether the test can produce a read at all, and the one claim that tells you when to run it if you do.

4. Applied. A prospect in the dealership space says a competitor's agency showed them Meta's 7.67x vehicle listing page figure. Write the two sentences you say back. Be exact about what you concede and what you will not repeat.

5. Applied. You are asked for an incrementality number on Phoenix Truxx next week, with no new budget. Say what you can produce, what you cannot, what you would have to build first, and name the free check on that account that has now been carried unrun for seven days.

> [!note]- Answer key
>
> **1.** Tier records provenance and directness: T1 means read at the source and the source is the platform or the official doc. It says nothing about method quality. AT-131 is T1 because Meta published those sentences, and it is unusable because the page carries no footnote, no sample, no window, no duration and no spend on any of the four cases. GA-055 is T2 because it is a real test with shown data, and it decided something because the design is inspectable, including the part that failed. Full marks require saying tier is about who said it and how directly, and method is what decides what it is worth. Deduct for any answer that treats T1 as automatically better than T2.
>
> **2.** Severity order: the eight-day window, 13 to 20 April 2026, with no holiday and no seasonal spread, compared against a 2022 figure whose window is not stated at all; then the blended mean across more than a million campaigns with no median, no spread and no breakdown; then revenue rather than profit, on an ecommerce shape, where our own revenue event sits weeks downstream in a CRM. What the footnote bought: it turned the figure from unverifiable into checkable, and the three objections above only exist because the footnote was readable. Half marks for the three reasons without that last point.
>
> **3.** Before answering: check whether a Conversion Lift study is actually available at SJR's spend, because AT-070's $100k-a-month figure is T3, unverified, and sits on Meta's geo lift product rather than on Conversion Lift; ask Meta in writing for the holdout share, the duration and the significance treatment, because none of that is published anywhere; and decide which question the test is for, since AT-125 and AT-081 split on exactly that. The number from our book: SJR ran $767.78 for 136 opt-ins at $5.65 in the week of 23 to 29 October, roughly $110 a day, and GA-055 shows a 21-day holdout at our scale returned 85 events where 166 were required, so the realistic expectation is a null for want of volume rather than a result. AT-125 is the timing claim: event volume is the whole mechanism, so if the question is what Meta does for us at the year-end window, run it in that window and accept the answer is only about that window.
>
> **4.** Something close to: "That number is real in the sense that Meta published it, and it carries no sample size, no test window and no spend level, so nobody can check it or forecast from it. What I will stand behind is the direction, which is that our ads move search and walk-in behaviour a last-click lead column never shows, and the number I will actually put in front of you is your own." Concede the direction and that Meta published it. Refuse the digits. Deduct for repeating 7.67x as a projection. Deduct for dismissing the case outright, because the direction supports a rule we rely on.
>
> **5.** Producible: the CRM-counted cost per real person and per qualified buyer, which on Phoenix September was 417 real people at $13.86 against Ads Manager's 706 at $8.18. Not producible: any incremental figure, because there is no holdout, no geo split, and no eligibility for a platform lift study at $160 plus $40 a day. Would have to be built first: a repeat-versus-new instrument in the CRM, since AT-121 records that GoHighLevel merges a repeat opt-in on the email address and SJR therefore reads 99.94% net-new, so the new-to-brand question cannot even be asked yet. The free check: **Compare attribution settings**, never opened on any account we hold, named in lesson 071 and carried unrun for seven days. Full marks require saying plainly that the CRM count is a counting instrument and not incrementality.
