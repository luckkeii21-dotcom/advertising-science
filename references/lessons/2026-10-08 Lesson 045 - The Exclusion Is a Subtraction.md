---
title: "Lesson 045 - The Exclusion Is a Subtraction"
type: lesson
lesson: 45
date: 2026-10-08
topic: Meta Delivery & Andromeda
claims: [MD-170, AU-059, AU-061, AU-060, AU-063, LS-037, MD-171]
video: none
tags: [advertising-science, lesson, meta-delivery, exclusions, customer-lists, learning-signal]
---

# Lesson 045 · The Exclusion Is a Subtraction

On 6 October at Advertising Week New York, Meta made **Customer Lifecycle Strategy available to all advertisers**. It builds acquisition campaigns and it carries an automatic recommendation: exclude your existing customers.

That recommendation is going to appear in ChiroWorks, StayWell, SJR Commercial and Phoenix Truxx. It is a checkbox with a reason printed beside it, and it will look like free money.

Our own codex argues both sides of it and has for a year.

| Claim | Tier | Status | Position |
|---|---|---|---|
| [[Auction Mechanics & Bidding#AU-059\|AU-059]] | T4 | contested | The leak is $40 out of a $500 day. Turn off the bad ad instead. |
| [[Auction Mechanics & Bidding#AU-061\|AU-061]] | T3 | contested | Without heavy exclusions Meta prioritises warm audiences and cold scale stalls. |

A product default is about to settle a question the evidence has not. So the job today is to know what you would say when it appears, before it appears.

## 1. The mechanism

Picture a recruiter working a phone list for you.

You hand over a sheet of names and say do not call any of these. That sheet works. The recruiter stops calling them. It saves you the calls.

What the sheet never does is tell the recruiter who to call **more**. And every name you crossed off is also a name whose outcome the recruiter can no longer learn anything from.

A Meta exclusion is that sheet. It is enforced at delivery and it teaches the model nothing. [[Learning & Signal#LS-037|LS-037]] states the consequence in one line worth memorising: **you are not feeding it nearly as much as you are taking out.** Subtracting signal is a different act from steering it.

That gives an exclusion two separate prices, and almost everyone argues about only the first.

**Price one, impressions.** Money spent showing ads to people who were already yours. Visible, computable, usually small.

**Price two, events.** Conversions removed from the pool the optimiser learns from. Invisible, and it arrives late. LS-037 carries the only timeline anyone has published for it: a stacked exclusion gives a short improvement in acquisition cost because the easy new customers come first, **then tanks after two to three months.** Long enough that whoever built the exclusion credits the early win to the exclusion and blames the collapse on creative.

There is a third thing nobody can price, which is whether the exclusion works at all. [[Auction Mechanics & Bidding#AU-063|AU-063]] records exclusion leakage from four separate operators, including clients watching their own ads arrive while sitting on the suppression list. The mechanism is boring and real: an exclusion binds against the people Meta can match to your list and leaks against everyone it cannot. On one pixel-event audience the measured coverage was 60 to 70%.

## 2. The evidence, and the tier order is upside down

Read the stack in tier order and watch what the strong claim can and cannot decide.

**[[Meta Delivery & Andromeda#MD-170|MD-170]], T1.** Meta's own announcement, read in full at source. This is as strong as evidence gets in this codex, and all it establishes is that **the button exists**. T1 on a product announcement tells you what shipped. It says nothing about whether pressing it helps you. That gap is the most useful thing in today's lesson.

**[[Auction Mechanics & Bidding#AU-061|AU-061]], T3, contested.** The case for exclusions, and the useful part is the conditioning rather than the rule. It applies to accounts with a **high returning-customer share** and accounts that have **existed a long time**. A young account with almost no warm pool has nothing for delivery to drift onto. An old account with a big one is where the cold campaign quietly becomes a retargeting campaign. Note the date too, 2025-02-26, which is before the Andromeda retrieval change, so the strength of the drift may have moved since.

**[[Auction Mechanics & Bidding#AU-059|AU-059]], T4, contested.** The case against, and it is reasoning on invented round numbers. 1,000 customers, a $20 CPM, a $500 daily budget, every customer seeing the ad twice a day for a year. That is $40 of $500, 8%, in the worst case the arithmetic allows. The claim is honest about its own limits and says the answer **scales entirely with list size against budget**. Hold on to that sentence. It does more work in section 3 than anything else here.

**[[Auction Mechanics & Bidding#AU-060|AU-060]], T3.** The one exclusion anybody on file actually derived. The operator found the repeat-purchase interval first, about 25 days, then set the window just past it at 30 days. The logic inverts the usual reason for excluding: those customers were going to buy again on their own, so paying to reach them inside that window buys a purchase you were getting free. **The method transfers, the number does not.** Nothing says a chiropractic practice or a truck dealership has an equivalent interval to find.

AU-060 also got amended yesterday, and the amendment is a lesson in itself. The hero account attached to it, $50k a month to $1M a week, is now credited by the same operator to a completely different mechanism, a buy-three-get-one-free offer built because the average customer bought 2.5 times. **One case is now the headline example for two mechanisms from one speaker, so it cannot carry weight for either.** Cite the exclusion setting on its own merits. Drop the growth figure.

So the two claims that would actually decide this are T3 and T4, both contested, and they are not even arguing with each other. AU-059 prices the impressions. AU-061 prices the delivery skew. **A leak can be cheap in dollars and expensive in what it does to delivery.** They can both be right.

**One last thing from the same announcement, and the rule is do nothing with it.** The post says advertisers who adopt Meta's recommendations are "typically seeing 5% more conversions at the same cost per conversion than those who don't." There is no footnote anywhere on the page. No window, no population, no geography. "Than those who don't" compares adopters against non-adopters, and advertisers who adopt a platform's recommendations are already selected on budget, attention and account health before any recommendation is applied. [[Meta Delivery & Andromeda#MD-171|MD-171]] is T1 for the sentence existing and T4 for the effect. Keep the 5% out of every deck, and do not use it to argue either side of this decision.

## 3. Our accounts

Two findings. The first says the recommendation cannot do anything on our book yet. The second says the fix that would make it work is the dangerous part.

### The list we would upload is not a customer list

Every account we run is lead generation into an Instant Form. The existing-customer bucket reads from an attached custom audience, and our clients hold their customers in a CRM with no purchase event wired to the pixel. **So the bucket is empty by construction until somebody uploads a list.** Nobody has. The recommendation arrives inert, and the real work it creates is an upload rather than a toggle.

Now look at what we would upload.

| Account | Window | Opt-ins | Booked | Came in | Confirmed customers |
|---|---|---|---|---|---|
| ChiroWorks | 6 Jul to 22 Sep | 143 | 40 | outcomes unmarked at the desk | 1 recorded as showed |
| StayWell | 15 Jun to 23 Sep | 144 | 21 | 9 | **2 became patients** |

Both sets of figures are cent-matched to Ads Manager on the live dashboards.

Upload StayWell's CRM as the existing-customer list and you suppress 144 people in order to suppress **2 actual patients**. That is **98.6% of the list who are not customers**, and 93.8% who never walked in the door. ChiroWorks is less extreme and still wrong: **103 of 143 never booked anything, 72%.**

An exclusion built from either file does not remove existing customers. It removes the prospects we already paid to find and have not yet converted. On two accounts whose stated bottleneck is the booking back end rather than opt-in volume, that is the exact population we most want to keep reachable.

The one number AU-061's conditioning actually asks for, returning-customer share, we cannot produce on any account. That is [[Attribution & Incrementality#AT-121|AT-121]] and lesson 033 taught the mechanism, so one line is enough here: GoHighLevel merges a repeat opt-in into the existing contact on the email address, so the file cannot record a repeat. We are not measuring a low returning share. We are unable to measure it.

### Run AU-059's arithmetic on real numbers and watch where it breaks

ChiroWorks, the filed week of 30 September to 6 October. Spend $463.28, which is $66.18 a day. CPM $20.66. Both from the same window.

Take AU-059's ceiling case exactly as written: every person on the list sees the ad **twice a day, every day**.

| List | Impressions in the week | Cost at $20.66 CPM | Share of the week's spend |
|---|---|---|---|
| Our 143 CRM contacts | 2,002 | **$41.36** | **8.93%** |

AU-059's invented example gave $40 and 8%. Ours gives $41.36 and 8.93%, on a different vertical at a seventh of the budget. That is not a coincidence and it is not a confirmation either. The share is **2 × CPM × (people ÷ budget)**, and his ratio was 2.00 people per budget dollar while ours is 2.17. Same ratio, same answer. The arithmetic was never about customers. It was about list size per dollar.

Which is why it flips:

| If the list were | People | Weekly leak | Share of the week |
|---|---|---|---|
| 5x our CRM | 715 | $206.81 | 44.6% |
| 10x our CRM | 1,430 | $413.61 | 89.3% |
| 1,602 | 1,602 | $463.28 | **100%** |

At 1,602 names the ceiling case eats the entire budget. A chiropractic practice with years of patient records clears 1,602 without trying, and that file lives in their practice management software, never in ours.

Read the two findings together, because separately each one is harmless.

**The exclusion recommendation is inert on our accounts because no customer list is attached. Attaching the list is the only way to make the recommendation work. And the list we have access to is 72% to 98.6% prospects, while the list that would be correct is large enough to move AU-059's arithmetic out of the regime where it says the leak is trivial.**

### And we cannot afford the events

[[Learning & Signal#LS-001|LS-001]] puts the learning-phase exit at roughly 50 optimisation events in seven days. September: ChiroWorks produced 94 opt-ins, about **21.9 a week, 44% of the threshold.** StayWell produced 59, about **13.8 a week, 28%.** Both accounts already sit permanently below it.

LS-037's price-two comes out of that. We cannot even size the subtraction, because sizing it needs the repeat share, and AT-121 says the instrument cannot produce it. **An unmeasurable cost taken out of a signal budget already running at under half the threshold is not a trade anyone here can price.**

## 4. The decision rule

**Never accept an exclusion you cannot price twice, once in wasted impressions at your own CPM and your own list size, and once in lost optimisation events. And never build one from a file whose rows you cannot prove are customers.**

On our four Meta accounts, today, that resolves to a specific answer and a specific next step.

- **Decline the recommendation when it appears.** Write down the date it appeared, per the standing scoreboard item on recording platform change dates ourselves.
- **The exclusion worth having is the clinic's own patient file, not our CRM.** Ask ChiroWorks and StayWell for it. That is a request, not a calculation.
- **Before uploading anything, run the week's arithmetic with the real row count.** If the file is 1,600 rows at ChiroWorks' current budget, the ceiling case is the whole budget and the conversation changes completely.
- **If the goal is new customers rather than suppression, the alternative is an event and not an audience.** LS-037's own argument is to fire a first-time event and optimise on it, because an audience definition can report and cannot steer. On our volumes that is a hypothesis, not a plan.

## 5. Quiz

Drop your answers in `_answers-inbox.md`.

**1.** MD-170 is T1 and the two claims that decide whether to act on it are T3 and T4. Explain in two sentences why the T1 cannot settle the decision.

**2.** AU-059 concludes the leak is trivial at 8% of budget. Name the single quantity that conclusion depends on, and state what happens to the conclusion when that quantity goes up 10x.

**3.** What are the two separate prices of an exclusion, and which one does LS-037 say arrives two to three months late?

**4. Scenario.** A new client runs a cash-pay med spa, opened 2019, 4,100 patient records in their practice software, 38% of monthly revenue from repeat visits, $150 a day Meta budget, measured CPM $31. They ask whether to exclude existing patients from the acquisition campaign. Work the impression leak on the ceiling case. Then say which of AU-059 and AU-061 the account's own facts support, and what you would actually recommend.

**5. Scenario.** Someone proposes uploading ChiroWorks' 143 CRM contacts as the existing-customer exclusion this week, arguing it is free, reversible and takes ten minutes. Give the two strongest objections from this lesson, each with a number, then name the one thing you would ask the clinic for instead.

> [!note]- Answer key
> **1.** T1 on a platform announcement establishes that the feature exists and what it does mechanically. It carries no evidence about outcome, because Meta published no population, no counterfactual and no footnote (MD-171). Whether excluding helps rests entirely on AU-061 and AU-059, which are T3 and T4 and both contested, and a T3-only or T4-only decision has to be named as a bet rather than applied as a law.
>
> **2.** **List size per budget dollar.** The share is 2 × CPM × (people ÷ budget), so it is linear in list size. At 10x the list the leak goes from about 8% of budget to about 89%, and at roughly 16x it consumes the whole budget. AU-059's own text says the answer scales entirely with customer-list size against budget, so "the leak is trivial" is a statement about one account's ratio and never a general finding. Full credit also for naming CPM as a second scaling input, since the formula is linear in both.
>
> **3.** **Impressions** (money spent reaching people who are already customers) and **events** (conversions removed from what the optimiser learns on). **The event price arrives two to three months late.** LS-037's named failure mode is that the early acquisition-cost improvement gets credited to the exclusion and the later collapse gets blamed on creative.
>
> **4.** Arithmetic: 4,100 × 2 = 8,200 impressions a day, at a $31 CPM that is **$254.20 a day against a $150 budget, about 169%**. The ceiling case exceeds the entire budget, so AU-059's "the leak is trivial, turn off the bad ad instead" does not hold on this account. The account's own facts also satisfy AU-061's conditioning on both counts: it has existed since 2019 and 38% of revenue is repeat, so there is a large warm pool for delivery to drift onto. **Both claims point the same way for the first time in this lesson**, which makes it the cleanest case for an exclusion anywhere in it. Recommendation: build it, and say out loud that it is still a bet on T3 and T4 evidence. Credit for adding any of these: the ceiling case assumes twice-daily exposure for every record, which overstates it, so get the real frequency before quoting 169%; AU-063 says it will leak against every record Meta cannot match, so the effect will be smaller than the arithmetic; LS-037's two to three month decay still applies and the account's event volume should be checked against LS-001 before subtracting from it; and AU-060's method says to find the repeat-visit interval and set the window just past it rather than excluding forever.
>
> **5.** Objection one: **the file is not a customer list.** 103 of the 143 never booked anything, 72%, so the exclusion removes prospects we already paid to find, on an account whose bottleneck is the booking back end. Objection two: **the account cannot afford the events.** ChiroWorks produced about 21.9 opt-ins a week in September against LS-001's roughly 50, which is 44% of the learning threshold, and LS-037's event price is subtracted from that. Credit also for: the suppression is not reversible in the way the proposal claims, because LS-037's damage shows up two to three months later, by which time it will be attributed to creative. **Ask the clinic for their practice management patient file.** Then re-run the leak arithmetic on the real row count before uploading, because at 1,602 rows the ceiling case is the whole week's budget.
