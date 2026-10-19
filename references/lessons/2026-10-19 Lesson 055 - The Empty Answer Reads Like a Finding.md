---
title: "Lesson 055 - The Empty Answer Reads Like a Finding"
type: lesson
lesson: 55
date: 2026-10-19
topic: Attribution & Incrementality
claims: [AT-128, AT-129, CR-177, AU-093, MD-155, MD-051, MD-138]
video: video/2026-10-19-lesson-055.mp4
tags: [advertising-science, lesson, attribution, api, breakdowns, provenance]
---

# Lesson 055 · The Empty Answer Reads Like a Finding

![[video/2026-10-19-lesson-055.mp4]]

Harvest day, and a big one. Eight claims banked, all tier 1, five of them off a Meta source this engine had never read. One of the eight is a silent failure sitting inside our own reporting, and it has been sitting there since 6 August.

It does not break a number. It replaces a number with a blank that looks like a number.

## 1. The mechanism

There are two kinds of zero and only one of them is a fact.

The first is a measured zero. You asked the question, the system looked, nobody did the thing. That is information and you can act on it.

The second is a withheld zero. You asked the question, the system declined to answer, and it handed you back an empty box. The box is the same shape as the first box.

The analogy. You text a supplier asking whether the part shipped. Nothing comes back. Two completely different worlds produce that silence: he read it and the part has not shipped, or the message never left your phone. Your screen looks identical in both. One of them means you need a new supplier. The other means you need to tap send again. The thread does not tell you which, and if you act on the blank you are acting on a coin flip.

Meta built that exact ambiguity into the Ads Insights API this August. From 6 August 2026 three breakdowns require per-account enablement:

- `breakdowns=impression_device`, and any combination containing it
- `breakdowns=hourly_stats_aggregated_by_audience_time_zone`
- `breakdowns=frequency_value`

Meta's own sentence is the whole problem. Requests using these breakdowns "may return no results for Ad Accounts that have not enabled them, whether synchronous or asynchronous."

No results. Not an error. Not a warning field. Not a permission code. A clean, well-formed, empty response, which is the same response a genuinely quiet account produces.

Now walk it downstream, because this is where it stops being a technical footnote. A report pipeline asks for the device split and gets nothing back. What it prints is "no desktop impressions". A dashboard asks for hour of day and gets nothing back. What it prints is "no impressions before 9am". Something asks for the frequency distribution and gets nothing back. What it prints is "frequency unavailable, no fatigue signal".

All three of those are statements about the account. All three are false. And nothing anywhere in the response said the data was withheld rather than absent.

The getting-back-in path matters too, because it is slower than it sounds. An account admin requests the breakdown inside Ads Manager. From that day forward, ordinary calls work. **History only comes back through asynchronous report jobs, and Meta throttles those at ten per 24 hours or the account's ad-group count, whichever is smaller.** So a small account is capped by its own smallness. Three ad groups means three backfill jobs a day.

## 2. The evidence

**[[Attribution & Incrementality#AT-128|AT-128]], T1, banked this morning.** A Marketing API out-of-cycle change dated 8 May 2026, effective 6 August 2026, read in full at source. Tier 1 because it is the platform describing its own behaviour in its own words.

Notice what tier 1 does not buy you here. Meta writes "certain Ad Accounts" and publishes no list, no criterion, and no way to ask which accounts are affected. So the claim is solid and its scope is unknown. **The exposure has to be tested account by account, never assumed either way.** A tier-1 claim can still leave you with homework.

The test is cheap. Request the breakdown over a window you already know was busy. If rows come back, you are enabled. If nothing comes back on a window that definitely had impressions, you are gated.

**[[Attribution & Incrementality#AT-129|AT-129]], T1, same shelf, same morning.** Meta retired Nielsen DMAs for Comscore Markets on 22 June 2026, `breakdowns=dma` stopped being supported, and no crosswalk was published. Different mechanism, same family: the ruler changed and the number moved without the account moving. Both of these are reasons to distrust a series that crosses a date, rather than reasons to distrust the account.

## 3. Our accounts

Our standing rule is that Meta data comes through the API, and the browser is for looking at one page at human speed. So the gated road is our main road. That is the bad news.

Here is the good news, stated precisely, because precision is the only thing that makes this useful.

**The frequency arithmetic is safe, and it is safe for a boring reason.** [[Meta Delivery & Andromeda#MD-155|MD-155]] was recomputed on 14 September from raw ad-level Ads Manager exports sitting on disk. ChiropracticWorks, 10 to 27 July, $890.84: 28,341 impressions, 8,869 people reached, account frequency 3.1955, 52 live ads, the highest single ad `Before / After IMG - 3` at 2.857, and 48 of the 52 ads at or below 2. Average frequency is a reported column. It is not `breakdowns=frequency_value`. The gate does not touch a single figure in that table.

**What the gate does touch is the exact thing we have been missing for two months.** [[Creative Science#CR-177|CR-177]] is contested, and the objection comes from the man selling the threshold: a reported frequency of 2.4 is a mean over a right-skewed distribution in which 10% of people may be seeing the ad eleven or more times, and the distribution is not visible. `breakdowns=frequency_value` **is** that distribution. The one instrument that could promote or kill a contested claim is now behind a request form that nobody has filled in.

**Hour of day is not a corrupted number here. It is a trap that has not been stepped in yet.** Our speed-to-lead and opening-hours work reads arrival time out of the CRM, and the rule is that no response-time figure ships without the business's real open hours and the share of leads that arrive while the doors are shut. Meta's hour-of-day breakdown is the impression side of the same question, and we have never opened it on any account. Device split, the same. So the first person who pulls either one is the person at risk, and that person will be one of us, soon, because both sit on the never-opened-instruments list.

**And the real finding is a gap in our own bookkeeping.** Look at the frequency figures we quote in client work: SJR's dump CBO at 2.58 and Box & Wreckers at 2.02 across 19 July to 17 August, Caesar at 2.33, ChiroWorks at 2.80 on the 10 to 20 July pull, Phoenix Truxx New Jersey at 2.10 in June and 2.24 in July, Spanish creative at 2.52 on 5 July. Not one of those carries a note saying where it came from. Export, UI, or API.

So the honest position is this. **None of our published numbers is confirmed corrupted, and none is confirmed clean, because we never wrote down the route.** The gate did not create that problem. It made it expensive.

## 4. The decision rule

**An empty result from a gated breakdown is not a zero, so prove the breakdown returns rows on a window you know was busy before publishing any device, hour-of-day or frequency-distribution figure. And from today, every number we quote carries its route.**

Two jobs follow, both small. Test the three breakdowns on all five accounts over a known-busy week. Add a source field to any figure that goes into a report.

## 5. Quiz

**1.** Meta gated three Ads Insights breakdowns in August. Why is the failure mode worse than a permission error would have been?

**2.** AT-128 is tier 1. Name the thing it still does not tell you, and what that forces you to do.

**3.** A dashboard pulls hour of day for ChiroWorks and reports that no impressions were delivered between midnight and 7am. The media buyer proposes narrowing the ad schedule to daytime only. What do you check first, and what is the cheapest way to check it?

**4.** Someone wants to settle CR-177 once and for all by pulling the frequency distribution on SJR Commercial and showing what share of people saw an ad more than five times. Walk through what has to happen before that number exists, including the part that is slow.

**5.** A client asks for market-level performance this year against last year, by metro. Two separate claims from today's harvest make that answer dishonest if you just pull it. Name both, and say what the honest version of the answer sounds like.

Answers into `_answers-inbox.md`.

> [!note]- Answer key
>
> **1.** Because an error stops the pipeline and an empty result set does not. A permission code would have been caught, logged and fixed. Meta returns a clean, well-formed response with no rows and no field saying why, which is identical to the response from an account that genuinely had no impressions on that cut. The pipeline then publishes a false statement about the account with full confidence. Silence is more dangerous than failure, because silence is indistinguishable from a fact.
>
> **2.** It says "certain Ad Accounts" and names no list and no criterion for which ones. So the claim is certain and its scope is unknown, and the exposure has to be tested per account rather than assumed in either direction. The test is one call: request the breakdown over a window you know was busy and see whether rows come back. Tier 1 settles what the behaviour is, never who it lands on.
>
> **3.** Check whether ChiroWorks is enabled for `hourly_stats_aggregated_by_audience_time_zone` at all, because a gated account returns exactly that result. Cheapest check: pull the same breakdown over a window with known heavy delivery, for instance the 10 to 27 July period that carried 28,341 impressions. If that window also comes back empty, the account is gated and the overnight figure is a withheld blank rather than a measurement. Narrowing the schedule off a withheld blank would cut real delivery on the strength of no evidence.
>
> **4.** An account admin has to request `breakdowns=frequency_value` inside Ads Manager. From the day enablement lands, ordinary synchronous calls work, so a forward-looking distribution starts accumulating immediately. The slow part is history: past data only arrives through asynchronous report jobs throttled at ten per 24 hours or the account's ad-group count, whichever is smaller. SJR's structure decides the pace, and a small account is capped by its own smallness. So the sequence is request, wait for enablement, then backfill across several days. One more thing worth saying out loud: this settles the measurement half of CR-177, which is whether the mean hides a tail. It does not settle whether a tail of eleven-plus exposures actually damages performance. That still needs an outcome comparison.
>
> **5.** [[Attribution & Incrementality#AT-129|AT-129]] first: Meta retired Nielsen DMAs for Comscore Markets on 22 June 2026 and published no crosswalk, so a year-over-year metro view is two different partitions of the map stitched together, and `breakdowns=dma` no longer returns anything. [[Attribution & Incrementality#AT-128|AT-128]] second, if the view includes device or hour cuts, because those can come back empty and read as real zeros. The honest answer names the break: performance by market can be shown inside each period, the two periods cannot be compared market to market because the market definitions changed in June, and any apparent growth or decline across that date may be a boundary change rather than a performance change.
