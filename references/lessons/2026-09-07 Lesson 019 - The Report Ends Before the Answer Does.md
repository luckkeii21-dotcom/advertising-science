---
title: "Lesson 019 - The Report Ends Before the Answer Does"
type: lesson
lesson: 19
topic: Google Auction & Smart Bidding
source: rotation index 6. The 2026-09-07 harvest was a genuine quiet day (0 new transcripts, 12 of 12 channels read clean, 0 errors) and the 2026-09-06 harvest banked nothing either, so there was no harvest material two days running. Anchored on GA-030, transferred to the back end using our own filed reports.
created: 2026-09-07
updated: 2026-09-07
tags: [advertising-science, lesson, google-ads, attribution, reporting]
---

# Lesson 019 · The Report Ends Before the Answer Does

🎬 **Lesson video (2m 32s, silent, watch anywhere):** [[video/2026-09-07-lesson-019.mp4]]

> Lesson 013 said cost per opt-in means nothing without the column next to it. This one is about the clock on that column. A number can be arithmetically correct and still be unreadable, because the thing it counts has not finished happening.

**If you only answer two questions, answer Q2 and Q4.** Q2 is the arithmetic you will do on Friday. Q4 is about two of our own reports, filed in the same run, that treated the same shape of data two different ways.

## 1. The mechanism

Every number in a report is filed under a date. That date is a choice, and the platform usually makes it for you without saying so.

Google files a conversion under the day of the **click**, not the day of the purchase. Somebody clicks on Monday and buys on Friday, and Google writes that sale back onto Monday. The consequence is structural: the newest days in any Google report are always understated, because the sales that belong to them have not happened yet. They fill in over the following week.

Our CRM does the same thing one step further down the funnel. An appointment is filed under the day it was **booked**. Whether that person actually turned up is decided on a completely different day, the day of the visit, and that day is often outside the reporting window altogether.

Think about exam results. A school files a student under the day they sat the paper. Ask for the pass rate the morning after the exam and you get 0%. Nobody failed. The papers are not marked yet.

A show rate is an exam result. A booking is sitting the paper.

So there are two clocks running through every report. The **event clock** records when the thing happened. The **outcome clock** records when the thing resolved. A reporting window closes on the event clock. The outcome clock keeps running after everyone has gone home.

## 2. The evidence

**GA-030, T3.** Google backdates conversions to the click date, so any trailing three to seven day window shows depressed performance that fills in later. The fix he names is a custom column, "conversions by conversion time". Read the tier before you lean on it: this is one practitioner asserting a mechanism, with no platform doc cited anywhere in the source.

**GA-034, T3.** The diagnostic gate. You are not allowed to touch the account until you can finish the sentence "this is underperforming because X dropped, driven by Y, caused by Z". Correcting for click-date latency is a step you take *before* you start that sentence, alongside checking change history and widening the window.

**AT-068, T3.** The general form of the problem. A period-end report reads its most incomplete days as final, so every week-over-week comparison structurally flatters the earlier week. Either cut the same tail off both windows, or say in the report which numbers are still filling in.

**AT-095, T3.** The limit case, and the one that applies to us. Some funnels have a cycle longer than the whole reporting window. Trimming a tail fixes nothing there, because the window cannot contain the outcome at all.

Law 11a already carries AT-068 in the hot layer. It stops at the ad platform. **Nothing in the law layer covers the back end**, which is exactly where our reports break.

Notice that all four claims are T3. Practitioner assertion, no shown test behind any of them. Which makes the next section carry more weight than this one.

## 3. Our accounts

No client of ours runs Google today. Mattia's Performance Max was the last one and it shut down on 2026-08-16. GA-030 is a mechanism we hold and currently do not use. The transfer to the back end is the part that is live on four accounts.

**ChiroWorks, filed report for 2026-08-08 to 2026-08-16.** Three appointments are on file. All three sit in a different relationship to that one window.

| Person | Booked | Visit | Booking inside window | Visit inside window |
|---|---|---|---|---|
| Ivorie | prior window | Aug 10 | no | yes |
| Leondra | Aug 10 | Aug 12 | yes | yes |
| Courtney | Aug 14 | Aug 21 | yes | no, 5 days after it closed |

On the booking clock the window holds Leondra and Courtney. On the visit clock it holds Leondra and Ivorie. Two each way, and only one person appears on both.

The report headline says "2 appointments booked in-window". That is the booking clock and it is correct on that clock. There is no version of that window in which Courtney could show up.

The booking-to-visit gap on the only two records that carry both dates is **2 days and 7 days**. Two data points, and that is all we have. The window was 9 days long. A 7-day gap starting on day 7 of the window lands outside it.

Then a second failure, which is a different animal. None of the three is marked showed or no-show. The report's own line: **"No ChiroWorks appointment has ever been marked showed/no-show."** So even Leondra, whose visit sat fully inside the window with four days to spare, produces nothing.

Two reasons a cell is blank. Only one of them gets better if you wait.

**One run, 2026-08-27, three accounts, two different treatments:**

- SJR Commercial: "4 appointments booked, 0 marked shown, show rate not yet measurable."
- Phoenix Truxx: "0 appointments logged... Show rate not computable."
- StayWell: a KPI row reading "Show rate | 0% | 0% | flat, the standing wall."

StayWell's 0% is arithmetically true. One appointment, cancelled, zero shows. It is published as a **trend** on a denominator of one, in the same table as "Reached appointment stage | 3", whose outcomes had not happened yet. The other two accounts refused to publish a rate on the same shape of data. Same run, same script, opposite calls.

The reason the script allows both is in the script. `weekly-client-reports/RUNBOOK.md` names the clock for one query and not for the next one:

- Line 83: "**Opportunities created in window** by stage"
- Line 84: "**Appointments in window** grouped by status... Show rate = showed ÷ booked × 100"

"Created in window" is a clock. "In window" is not one. The rate that decides whether a client renews is computed off the one line in our SOP that never says which date it means.

## 4. The decision rule

**An outcome rate is readable only when the window closed at least one full event-to-outcome lag ago. Until then publish the two counts and the two dates, never the percentage.**

Three things that follow:

1. Name the clock in the query. Booked-on, or visited-on. Never "in window".
2. Report bookings on the booking clock and shows on the visit clock, as two separate rows, and say which is which.
3. Where the lag is not measured on that account, write that the rate is not yet measurable. SJR and Phoenix already do this. It is the right call and it should be the only call.

## 5. Quiz

**Q1.** Google files a conversion under which date, and what does that do to the last three days of a trailing report? Name the column that corrects it.

**Q2.** ChiroWorks, window 1 to 7 September, pulled on the 8th. Three people book: A books the 2nd for the 4th, B books the 5th for the 9th, C books the 6th for the 15th. All three eventually show up. What show rate does a booking-clock query return on the 8th? What does a visit-clock query return? Which number goes in the client report, and what sentence goes next to it?

**Q3.** Every claim behind this lesson is T3, and GA-030 has no platform documentation behind it. What is the cheapest thing you could do on one of our live accounts this week that would move the back-end version of this claim to T2, and what exactly would you have to write down for it to count as T2?

**Q4.** StayWell published "Show rate 0%, flat, the standing wall" on one cancelled appointment. SJR published "show rate not yet measurable" on four bookings with zero marked outcomes. The arithmetic in both is correct. One is the worse mistake. Which one, and why?

**Q5.** Someone proposes fixing all of this by moving the report window from 7 days to 30, so every booking has time to resolve. Give the strongest argument for it, then name the two things it breaks. Which of AT-068 and AT-095 applies to each half of your answer?

Drop your answers in `_answers-inbox.md`. Partial answers get graded.

> [!note]- Answer key
>
> **A1.** The click date, not the purchase date. Google backdates the sale onto the day the click happened. So the most recent three to four days of any trailing report are understated and fill in over the following week, which beginners read as a performance collapse and act on. The correction is the "conversions by conversion time" column, added as a custom column (GA-030, T3). Full marks also for noting the tier: no platform doc was cited, so verify it against your own account before you build a rule on it.
>
> **A2.** Booking-clock query on the 8th: three bookings created inside the window (2nd, 5th, 6th), zero marked shown, so it returns **0%**. Visit-clock query on the 8th: only A's visit (the 4th) has happened, so the denominator is **1** and, once marked, the rate is **100%**. Neither number belongs in a client report as a show rate. B's visit is on the 9th and C's is on the 15th, both after the pull. The honest line is the counts and the dates: three appointments booked in the window, one visit has happened, two are scheduled for the 9th and the 15th, show rate not measurable until the 15th has passed and all three are marked. The trap is the 0%, because it is the number the query hands you and it reads like a finding.
>
> **A3.** Measure the account's own booking-to-visit lag and its marking rate, then publish both. Concretely: pull every ChiroWorks appointment on record with its booking date and its appointment date, compute the distribution of the gap, and count how many carry a showed or no-show marking. For T2 it has to be a shown result, not an assertion, so what gets written down is the sample size, the actual gap values or the median with the spread, the date range the pull covers, and the marking rate as a fraction with both numbers visible. Today we have exactly two gap values, 2 days and 7 days, which is an anecdote. The same pull answers whether the marking problem is universal or specific to one desk. Credit for noticing that this pull is nearly free: the appointment dates are already in the CRM, nobody has to change anything, and the reason it has never been done is that no report asked for it.
>
> **A4.** StayWell is the worse mistake, and the reason is not the arithmetic. It publishes a **trend**. "0%, 0%, flat, the standing wall" tells the client that a stable thing has been measured twice and has not moved, when the underlying denominator is one cancelled appointment. SJR's line makes a weaker claim than its data and is therefore safe; StayWell's makes a stronger claim than its data and is therefore not. Worse, it sits directly below "Reached appointment stage: 3", so the reader is invited to divide 0 by 3. The second-order damage is that a manufactured zero becomes a standing narrative, and next quarter somebody argues about lead quality when the actual finding is that nobody marks the calendar. Half marks for saying "n=1 is too small", because sample size is the symptom rather than the cause.
>
> **A5.** The argument for it: a 30-day window is longer than any booking-to-visit gap we have on record (2 and 7 days), so every appointment inside it resolves, and the show rate becomes a real number instead of an artefact. That is AT-095's own logic, that the window has to be able to contain the outcome. Two things it breaks. First, the tail problem does not go away, it just moves: the last few days of a 30-day window are still immature, so week-over-week comparison still flatters the earlier window unless you cut the same tail off both. That half is AT-068, and it applies to any window length. Second, a 30-day cadence is not a weekly report. The whole point of reporting weekly is to change something this week, and a decision made on a 30-day average is a decision made partly on ads that were switched off three weeks ago. The real answer is not one window: report spend and opt-ins on a 7-day window and outcome rates on a lagged window that closed long enough ago to have resolved, and say plainly in the report that the two cover different periods. Full marks for spotting that changing the window is a reporting change and not a measurement fix, because the marking problem survives every window length.
