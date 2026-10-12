---
title: "Lesson 047 - The Gate Is Priced in Events"
type: lesson
lesson: 47
date: 2026-10-10
topic: Learning & Signal
claims: [LS-050, LS-049, LS-011, LS-012, LS-013, LS-044, LS-045, LS-029, LS-020, LS-064]
video: none
tags: [advertising-science, lesson, learning-signal, optimisation-event, lead-quality, conversions-api]
---

# Lesson 047 · The Gate Is Priced in Events

The rotation brought up Learning & Signal, and the biggest untaught block in it is the lead-quality cluster. Ten claims, every one of them about the same complaint: Meta keeps sending cheap leads who do not buy.

Every operator in the codex agrees on the cause. They disagree on the fix, they have argued about it for a year, and none of them has run a test. That argument can be settled today, and not by picking a side. It gets settled by arithmetic, because three of the numbers involved are published by Meta and the rest are in our own exports.

## 1. The mechanism

You hire a recruiter. The arrangement is strict: you may send exactly one piece of feedback a week, and it has to be a list of names. "These are the people I liked." The recruiter reads the list and goes out to find more people like those names. That list is the entire channel. Nothing else you think reaches them.

Four weeks in you notice half the names were time-wasters. Two fixes suggest themselves.

Put only the good names on the list. Honest, and it cuts the list from forty names to three. Three names a week is not a pattern, and the recruiter starts guessing.

Or keep sending all forty, and separately hand over a marked-up copy: these ones in green, pay more for people like them, these ones in red, pay less. The list stays long. The feedback gets richer. It costs nothing.

That is the whole subject. The list is your optimisation event. The names are whoever fires it. The markup is a labelled audience with a bid rule attached. **Signal purity and event volume are bought with the same currency, and the only question worth asking is how much of that currency you have.**

## 2. The evidence

Six routes exist in the codex. Here is what each one actually costs.

| Route | Claim | Tier | Price in events |
|---|---|---|---|
| Two-step form, pixel fires only on the qualified answer | [[Learning & Signal#LS-011\|LS-011]] | T3 | Never quantified by anyone. A second build routes to two pages instead, so the disqualified branch fires its own event rather than silence |
| Human review of each booking, event fired by hand | [[Learning & Signal#LS-012\|LS-012]] | T3 | Cuts to the booking rate. Its own stated floor is roughly $1,000/day because of that |
| Fire on the follow-up email click instead of the form | [[Learning & Signal#LS-044\|LS-044]] | T3 | Cuts to the email-click rate. Unmeasured, and the 0% figure behind it is definitional |
| Register the qualified lead as a Purchase valued at average lead value | [[Learning & Signal#LS-045\|LS-045]] | T3 | Cuts to the qualification rate, and requires knowing average lead value first |
| Add the deep stage as a second event, keep the shallow one firing | [[Learning & Signal#LS-029\|LS-029]] | T3 | Nothing, by design |
| Leave the event alone and bid on labelled audiences | [[Learning & Signal#LS-050\|LS-050]] | T3 | Nothing |

The failure mode driving the whole argument is worth stating once with its number. [[Learning & Signal#LS-013|LS-013]] (T3): an ungated booking event trained on people who book and rebook, so delivery went and found more reschedulers, and roughly $10,000 of spend produced nothing. [[Learning & Signal#LS-020|LS-020]] (T3) is the same mechanism in a calmer account: Meta put about 40% of a lead-gen budget into people over 65 because their leads were cheapest, and the back end showed they almost never paid.

Now notice what every claim in that table has in common. **T3, all of them.** Not one carries a before-and-after. Six routes, one failure anecdote with a dollar figure, zero comparisons. Stacking six assertions on one side of a scale is consensus, and consensus is not evidence. The argument itself is on file as [[Learning & Signal#LS-009|LS-009]], T3 and contested since August, with three named operators on the quality side and one on the volume side, and nobody has run a test in the year it has been open.

**So look for the constraint instead of the argument.** Three numbers decide this and all three are platform-published:

- About **50 results** in the week after the last significant edit, which is when an ad set stops being in learning. [[Learning & Signal#LS-001|LS-001]], T1.
- Meta's Conversion Leads integration will not finish setting up until **at least 2 stages carry events** and events total **at least 50 over 7 days**, with **lead coverage of at least 60%**.
- The stage you optimise toward has to be reached by **between 1% and 40%** of leads, **within 28 days**, on an account doing at least **200 leads a month** (Meta's figure, GoHighLevel's article says 250).

Those last two sets are T1 and they live in the vault at [[Meta Conversions API via GoHighLevel]] rather than in the codex with an ID. They should be claims. For now, read them as the strongest evidence in this lesson, because they are the only numbers here that nobody is guessing.

And read the coverage bar carefully, because it ends the argument outright. **Meta names sending the raw event for every single opt-in as the fix for low coverage.** A workflow that fires only on the good leads can never reach 60% coverage, so it never validates, so it never optimises anything. The choice was never gate or do not gate. The shallow event has to keep firing either way. The only real decision is whether a second, deeper event gets added beside it, and that is a volume question.

## 3. Our accounts

Run the arithmetic on the filed week of 30 September to 6 October. Opt-ins are the real-people counts where an echo has been corrected, never the Results column.

| Account | Opt-ins, filed week | Deep stage written somewhere we can read | Rate | Events in 7 days, both stages | Clears 50 in 7 days | Clears 200 a month |
|---|---|---|---|---|---|---|
| ChiroWorks | 17 | appointment booked | 28.0% (40 of 143) | about 22 | no | no, about 95 |
| StayWell | 34 | appointment row | about 15% (5 of 34) | about 39 | no | no, about 119 |
| Phoenix Truxx | 68 | Appointment Booked | 13.5% | about 77 | **yes** | **yes, 417 in September** |
| SJR Commercial | about 100 | nothing exists | n/a | one stage only | n/a | yes, 429 in September |

Four accounts, four different verdicts, and not one of them is a matter of taste.

**ChiroWorks and StayWell fail on volume, before any gate is built.** 17 and 34 opt-ins in the week, against a learning threshold of about 50. Add the booking stage and the totals reach about 22 and about 39. Both are still short of the bar that merely lets the integration finish installing. The booking rates themselves are fine: ChiroWorks at 28.0% and StayWell at about 15% both sit comfortably inside Meta's 1% to 40% band. The stage is eligible. The account is not.

**Phoenix Truxx clears every bar on the list, and it is the only account that does.** 68 real people plus about 9 appointments is about 77 events across two stages in seven days. 417 real people in September clears both the 200 and the 250 figure. Appointment Booked at 13.5% is inside the band. Opt-in to sale at 0.88% is below the 1% floor, so the sale is not an eligible optimisation stage and belongs there as a measurement stage only.

**SJR Commercial has the volume and nothing to send.** About 100 real people a week, and no voice agent on the account. Follow-up is the human team plus DriveCentric, invisible to us past the opt-in. One stage, and the integration needs two.

Three more findings came out of running this, and all three are corrections.

**The pipe LS-029 asks us to build is already running on Phoenix, pointed at the wrong event.** The GoHighLevel workflow "Meta Conversions API Setup" triggers on Facebook Lead Form Submitted and sends a Funnel Event named Lead. It fires on the thing Meta already counted. Its only measurable effect so far has been to double our own opt-in count: Ads Manager read 706 at $8.18 for September against 417 real people at $13.86. The hardest-to-build part of route five exists on that account, and it has spent five months teaching Meta a fact Meta already knew.

**LS-045 is not buildable on this book, and the reason is documented rather than arguable.** It needs average lead value. The only value in any of our CRMs is a flat $40,000 pipeline default on Phoenix, where 1 of 3,998 opportunities has ever reached a sold stage against 19 real sales. Separately, GoHighLevel drops the value field unless the stage is literally named Purchase, and Meta's CRM payload specification has no value field at all. Two independent blocks, neither of which is about strategy.

**LS-050's own in-house paragraph is wrong and this lesson corrects it.** It says every account we run already has the CRM half built because the voice agent writes the qualification outcome. Checked today: a booking is written on three of four accounts, and a qualification outcome past the booking is written on none of them. ChiroWorks has 40 bookings with 1 marked showed, 2 no-show, and 26 sitting past their date still marked confirmed. StayWell's outcomes are unmarked and some of its appointment rows are internal test contacts. SJR and Phoenix have no voice agent at all. The cheapest route in the cluster is cheap because the hard half was supposed to be done already, and it is not.

## 4. The decision rule

**Count the opt-ins per week before you touch the optimisation event. Under about 50 a week you do not get to choose a deeper event at all, so leave the event alone and push quality back as a labelled audience with a bid rule. Over 50 a week, add the deep stage as a second event and keep the shallow one firing, because Meta's own integration requires it.**

Four riders.

Pick the stage on its conversion rate, not on which outcome feels real. The sale usually fails the 1% floor. The appointment usually passes.

Events per week is the right denominator for more than this one decision. [[Learning & Signal#LS-064|LS-064]] (T3) keys the whole ABO or CBO choice to the daily event rate rather than to the budget, and hands allocation to Meta only between 2 and 10 events a day. That is 14 to 70 a week, so the operator's own practical floor straddles the 50 figure without him ever naming it. Carry his caveat with the number: he says in the same breath that he has changed his mind on it many times.

Before calling route five free, check that the outcome is written down. The automations are an afternoon. Marking the outcome is a habit at somebody else's desk, and that is the actual blocker on two of our accounts.

Do not present route five as proven. One operator, one video, the plumbing shown on screen, the bid layer never run by anyone, no comparison of any kind. [[Learning & Signal#LS-049|LS-049]] adds its own limit: most label-eligible audiences have to be pixel-sourced, and that restriction was read off one Ads Manager UI on one day in June 2026. Re-check the field exists before building on it.

## 5. Quiz

Drop your answers in `_answers-inbox.md`.

**1.** Six routes in this lesson are T3 and three numbers are T1. Explain in two sentences why the T1 numbers settle the question when six T3 claims could not.

**2.** Why can a workflow that fires only on qualified leads never finish installing? Name the bar it fails and the fix Meta itself prescribes.

**3.** ChiroWorks' booking rate is 28.0% and Phoenix's opt-in-to-sale rate is 0.88%. One is an eligible optimisation stage and one is not. Say which, and why the ineligible one is still worth sending.

**4. Scenario.** A new client runs a roofing company. Meta Instant Forms, 260 opt-ins a month and about 60 a week, $400 a day. The CRM records "inspection booked" for 22% of opt-ins, usually 4 to 9 days after the form, and "contract signed" for 3%, usually 6 weeks after. They want to stop paying for tyre-kickers. Work each bar in this lesson and say exactly what you would build, including which stage carries the optimisation and which is measurement only.

**5. Scenario.** Someone proposes switching ChiroWorks' optimisation event to the booked appointment this week, on the grounds that the booking is what the clinic actually wants. Give the three strongest objections, each with a number, then say what you would do on that account instead.

> [!note]- Answer key
>
> **1.** The six T3 claims are assertions about what works, and six of them pointing the same way is consensus rather than measurement, because not one carries a before-and-after. The three T1 numbers are not claims about what works at all, they are constraints on what can be built, and a constraint turns a question of taste into arithmetic: you either have 50 events in seven days or you do not. Full credit for adding that LS-001's status is contested even at T1, so treat 50 as an approximate floor rather than a switch.
>
> **2.** It fails **lead coverage of at least 60%**, the percentage of leads with a matching event uploaded to Meta. Firing only on the good ones puts coverage near zero, so setup never validates and nothing gets optimised. **Meta's own prescribed fix is to send the raw event for every opt-in** and carry the qualification as a second stage. Credit also for the companion bars it fails: at least 2 stages carrying events, and at least 50 events over 7 days.
>
> **3.** **The 28.0% booking rate is eligible**, because it sits inside Meta's 1% to 40% band. **The 0.88% sale rate is not**, because it is below the 1% floor. The sale is still worth sending as a second, measurement-only stage: it is the number the business is actually judged on, it satisfies the two-stage requirement, and sending it costs nothing in optimisation. Credit for naming the 28-day rule, which a truck sale would also fail, and for naming the 7-day backfill cap, which means no stage can be seeded with history.
>
> **4.** Work the bars in order. Volume: 60 a week clears about 50, and 260 a month clears Meta's 200 but sits only just above GoHighLevel's 250, so flag that the two published floors disagree and this account is close to one of them. Stages: inspection booked at 22% is inside the 1% to 40% band and lands in 4 to 9 days, well inside 28. Contract signed at 3% is inside the band on rate and **lands at about 6 weeks, outside the 28-day window**, so it fails on timing rather than on rate. Build: send the raw opt-in for all 60 a week as stage one so coverage reaches 100% and the two-stage bar is met, **optimise on inspection booked**, and send contract signed as a third, measurement-only stage. Leave the form alone, because a gate would cut the optimisation event to about 13 a week and the client already clears the bar without paying that. Credit for adding any of: expect a learning reset when the optimisation event changes, so budget two quiet weeks; confirm the CRM actually writes the inspection outcome before promising the build; and 3% at 6 weeks means last-click will never show the contracts, so agree how they get counted before launch.
>
> **5.** Objection one: **the account does not have the events.** 17 opt-ins in the filed week, and the booking stage would fire about 5 times, against a learning threshold of about 50. Objection two: **the integration will not even install.** It needs 2 stages and 50 events in 7 days, and ChiroWorks reaches about 22 with both stages sent, so there is nothing to switch to. Objection three: **changing the optimisation event is a significant edit**, so the switch resets learning on an account already producing roughly a third of the threshold, and it buys that reset for a stage firing less than once a day. Credit for a fourth: the booking is written but the outcome is not, so even after the switch nobody could tell whether it worked, with 1 of 40 bookings ever marked showed. **Instead: leave the optimisation event alone and run route five.** Fire a GoHighLevel automation at each qualification point into a named Meta custom audience, bid the disqualified audience down and the booked one up with a value rule, and in the same week ask the front desk to start marking appointment outcomes, because that habit is what every other route on this account is waiting for.
