---
title: "Lesson 050 - The Lag Is Not the Same Size Every Month"
type: lesson
lesson: 50
date: 2026-10-14
topic: Attribution & Incrementality
claims: [AT-122, AT-124, AT-113, AT-068, AT-081, AT-125, AT-095, AT-079, AT-123]
video: none (Tuesday)
tags: [advertising-science, lesson, attribution, incrementality, seasonality, reporting-windows, maturation-lag]
---

# Lesson 050 · The Lag Is Not the Same Size Every Month

You already know a conversion can land after the window closes. Lesson 019 covered it on the back end and lesson 022 covered the empty row.

This one is the part nobody says out loud. **The lag has a length, the length changes with the calendar, and the error it creates always points the same way.** That last bit is what makes it dangerous. A random error averages out. A one-directional error that gets bigger exactly when the budget gets bigger moves real money to the worst place available.

Mid-October is the right week to learn it, because the decision it governs is in front of us now.

## 1. The mechanism

You write cheques and you read your bank balance. Most weeks a couple of cheques are in flight, so the balance you read is a little low. You know this, you ignore it, nothing breaks.

Then comes the week everyone pays at once. Now a lot of cheques are in flight. The balance is wrong by much more, and it is wrong in the same direction it is always wrong, which is low. If you made a spending decision off that screen you would decide you were poorer than you are, on the one week you were richest.

Attributed performance works exactly like that balance. A purchase gets credited back to the click that caused it. If the purchase has not happened yet, the click sits in your report with no revenue beside it. So today's reported return is today's spend divided by the revenue that has finished arriving, and nothing else.

Two things follow, and the second one is the lesson.

**First, every report is understated at its young end.** The newest days have had the least time to mature. That is [[Attribution & Incrementality#AT-068|AT-068]] and it holds in every window length.

**Second, the size of the understatement is not a constant.** It grows when more purchases are in flight, which is when conversion volume is high and when the delay between click and purchase stretches. A season does both at once. So the gap between a narrow window and a wide one widens in the run-up to a peak, then slams shut during the sale as the backlog books all at once.

Your dashboard is therefore at its most pessimistic before the peak and at its most flattering during it. Operators read that and move money into the peak weekend. **That is the exact wrong direction**, because the pre-peak dollar is the one whose revenue is still clearing.

## 2. The evidence

The load-bearing claim is [[Attribution & Incrementality#AT-122|AT-122]], **T3**. Year round the gap in credited revenue between a 1-day-click and a 30-day-click read sits near **40%**. In November it goes to about **80%**. One named account, X Cloud, read about **1.0** return in real time on 12 and 13 November and about **4.0** once the value finished booking to the original clicks, a 300% lift on the same two days.

The strongest support inside it is not the case study, it is geo-holdout work from Haus: experiments ending **three or more weeks before** Black Friday showed a **105%** post-treatment lift, experiments closer showed **+75%**, and **41% of incremental value appeared after the treatment window**. Split by category, fashion and apparel **93%** against health, wellness, food and beverage **30%**.

**Now the tier discipline, because this is the whole point of learning tiers.** Those Haus numbers are real randomised geo experiments. Read at source they would be T2. They are banked at **T3 because the primary was never read**; what was read is a presentation citing them. Same numbers, weaker claim, and the weakness is in our handling, not in their study. Reading the Haus report upgrades the claim and costs an afternoon.

[[Attribution & Incrementality#AT-124|AT-124]], **T3**, is the same mechanism at a different time scale. Spend peaks **5am to 7am** while revenue peaks **7am to 11am**, so a 5am return is measuring spend whose revenue has not landed. Judged against a daily target it looks like a disaster and triggers a cut. It is described rather than shown, and no multiplier table was published, which is why it is T3 and not better.

[[Attribution & Incrementality#AT-113|AT-113]], **T3**, is the cross-channel version. Google's attributed return multiplies overnight at a peak, and for roughly **70% of brands** the operator says it is not incremental. Two ordinary causes, neither of them Google finding demand: site-wide conversion rate is up because it is a peak, and the other platform drove the person across to finish on a branded click. **Hold this one loosely.** The 70% is his own audit figure with nothing published behind it and he flags the exception himself.

Then the pair that disagree, and you should be able to resolve them.

[[Attribution & Incrementality#AT-081|AT-081]], **T4**: never run an incrementality test in a high-seasonality month, because seasonal noise swamps the effect. Three design rules from one operator, none tested.

[[Attribution & Incrementality#AT-125|AT-125]], **T1**: Meta states a Conversion Lift study reaches a reliable read in **2 to 3 weeks at holiday conversion volume against 6 or more weeks in a quiet quarter**, because a holdout resolves when enough events land on both arms.

Note what the tiers do and do not tell you. **T1 is a direct quote from the platform, read in full, and it is self-interested**; Meta sells the ads whose value the study measures. **T4 is an untested design argument from an operator with no stake in your booking it.** Tier ranks how well sourced a claim is. It does not rank who is right.

And they are both right, because they answer different questions. A holdout run at peak measures peak. If you want a number to generalise to the rest of the year, November contaminates it, so run in a flat month. If you want a number to fund next year's peak, November is the population you actually care about. Scope split, not contradiction.

## 3. Our accounts

We sell trucks and chiropractic visits, not Black Friday sweaters. The mechanism still lands, it just lands on a different outcome.

**Phoenix Truxx is the only account on the book with an attributed-sale series, and it is already proof.** Thirteen of nineteen sales matched to our own opt-in records give a **median of 12 days from opt-in to sale, range 3 to 37**. Every weekly report we file is seven days long. **A seven-day report is structurally incapable of seeing a sale.** Opt-in to sale runs **0.88%** on that account, against **13.5%** to Appointment Booked, which is why the appointment is the eligible optimisation stage and the sale is a measurement stage.

**ChiroWorks has the same shape on a shorter clock and almost no data.** The measured booking-to-visit lag is **2 days and 7 days**, from the only two records that carry both dates. Two values is an order of magnitude, not a distribution. A 7-day lag starting on day 7 of a 7-day window cannot resolve inside it.

**And here is the honest hole, which is the thing worth taking away.** Phoenix has real seasonality on file: NJ dump search is **flat February to May**, **holds in November**, **September is the low**; plow moves on storm days **November to February**; box leads run **January to March**. So we know the demand curve. **We do not know whether the 12-day median moves along it.** Nobody has split that lag by month. If a storm week in January compresses a dump buyer from 12 days to 3, or stretches him to 30, every January report we write is biased and we cannot say by how much or which way.

That is one pull. The nineteen-sale ledger and the opt-in dates are already on disk.

## 4. The decision rule

**Never compare a reported number across two periods without first asking whether the maturation lag was the same length in both. If you cannot name the lag, you are reading a calendar, not performance.**

Three things that follow immediately. Cut the same immature tail off both ends of any period comparison, per AT-068. Judge against target on your normal window and read a wider or incremental window only to price the next dollar, per [[Attribution & Incrementality#AT-123|AT-123]]. And when you propose a lift study, say which question it answers before you say which month it runs in.

## 5. Quiz

Drop your answers in `lessons/_answers-inbox.md` with the lesson number.

**1.** Why does the 1-day-click to 30-day-click gap widen before a peak and narrow during it? Name both inputs to the lag that a season changes.

**2.** AT-125 is T1 and AT-081 is T4. AT-081 is the one we follow for most tests anyway. Explain why that is not inconsistent, and say in one sentence what a tier actually ranks.

**3.** A client's Google account read a 10 return all year. First week of November it reads a 40. The client wants to triple the Google budget. What do you tell them, which claim is it, and what is the single weakest thing about that claim that you should say out loud in the same breath?

**4.** Application. Phoenix Truxx: median 12 days opt-in to sale, range 3 to 37, 0.88% opt-in to sale, 13.5% to Appointment Booked. Phoenix asks on 1 December whether November beat October on cost per truck sold. You have both months' spend, opt-ins and the sales ledger. State exactly what you would and would not put in that answer, and name the one pull that would let you give a real one.

**5.** Application. ChiroWorks, booking-to-visit lag known only as 2 days and 7 days. Someone proposes fixing the immature-tail problem by reporting show rate on a trailing 30-day window instead of 7. Does that fix it? Say what it fixes, what it does not, and what you would do instead.

> [!note]- Answer key
>
> **1.** The lag is the time between the click and the purchase, and the understatement at any moment is the volume of purchases still in flight. **A season raises conversion volume**, so more purchases are mid-flight at once, and **it stretches the click-to-purchase delay**, because people browse and save in the run-up and buy on the sale day. Both inputs push the same way, so the gap widens from about 40% to about 80% in November per AT-122. It narrows during the sale because the backlog books all at once and gets backdated onto the earlier clicks, which is the X Cloud 1.0 reading that resolved to 4.0. Full credit for naming the direction: the report is most pessimistic before the peak and most flattering during it, so the bias pushes budget toward the weekend, which is where the marginal dollar is worst.
>
> **2.** **A tier ranks how well a claim is sourced, not whether it is true.** AT-125 is T1 because it is a direct platform statement read in full; it is also self-interested, since Meta sells the ads whose value the study measures. AT-081 is T4 because it is three untested design arguments from one operator. They are not in conflict at all, because they answer different questions: **AT-081 is about a test whose result you want to generalise to the whole year**, where November contaminates the estimate, and **AT-125 is about a test whose result you want to use for next peak**, where November is the population you care about. A holdout measured at peak measures peak. Credit for noting the file records this as a scope split and sets neither claim to contested. Extra credit for spotting that AT-125's duration figure is falsifiable against our own next study, which is what makes it useful despite the self-interest.
>
> **3.** **Tell them the rise is the expected artefact of a peak and not headroom. Let Google run, let the attributed return sit high, do not treat it as room to scale.** That is AT-113, and the mechanism has two ordinary causes with no new demand in either: site-wide conversion rate is up because it is a peak, and the other platform is driving the person across to complete on a branded or shopping click, where the last click harvests credit created upstream. **The weakest thing, said out loud: the "roughly 70% of brands" figure is the operator's own number from audit practice with nothing published behind it, and he names the exception himself.** So the direction of the advice is well supported by the last-click mechanism this topic documents everywhere; the 70% is not a measured rate and should never be quoted to a client as one. Full credit for adding that in a client report this belongs in writing before anyone proposes the budget move, not after. Credit for noting we cannot run the clean version of this check on our own accounts anyway.
>
> **4.** **What you put in: both months' spend, both months' opt-in counts, and the sales that have closed, each labelled with the date it closed.** What you refuse to put in is **a cost per truck sold for November**, because on 1 December a November opt-in has had at most 30 days and the range runs to 37, so November's sales are not finished arriving and October's are much closer to complete. Dividing both months by spend compares a finished month against an unfinished one and will always flatter October. **That is AT-068's immature tail, except the lag here is 12 days median rather than a couple of days, so the immature tail is most of the month.** Say that in the report in one sentence rather than filling the gap with a number. **What you can compare honestly: spend and opt-ins, which mature in seconds, and appointments, at 13.5% and a short clock.** **The pull that fixes it: split the nineteen-sale ledger's days-to-sale by month of opt-in.** Both the ledger and the opt-in dates are already on disk. That tells you how long to wait before a month is readable, and whether the 12-day median moves with dump and plow seasonality. Credit for proposing a lagged window instead: report spend and opt-ins on the month, report cost per sale only for months that closed at least 37 days ago, and say plainly that the two cover different periods.
>
> **5.** **It does not fix it, and it is a reporting change dressed as a measurement fix.** What it genuinely does fix: a 30-day window is longer than both lag values we have, 2 and 7 days, so appointments booked early in it resolve inside it, which is the AT-095 condition that the window must be able to contain the outcome. **What it does not fix, two things.** First, **the immature tail does not disappear, it moves**: the last days of a 30-day window are still unresolved, so any week-over-week or month-over-month comparison still flatters the older period unless you cut the same tail off both. That is AT-068 and it applies at every window length. Second, **the real blocker on this account is not the window at all, it is that the lag is two data points and appointments go unmarked**, so a longer window still computes a rate on a denominator nobody filled in. **What you do instead: pull the full booking-to-visit distribution**, which is nearly free because the dates are already in the CRM, **publish the marking rate as a fraction with both numbers visible**, and until then report spend and opt-ins weekly while reporting show rate only on a sub-window that closed at least one full lag before the pull, saying in the report that the two cover different periods. Full credit for refusing to publish a rate that looks like a measurement and is actually an artefact of an unfilled field.
