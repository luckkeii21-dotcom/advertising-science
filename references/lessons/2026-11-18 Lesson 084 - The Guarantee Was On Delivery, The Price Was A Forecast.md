---
title: "Lesson 084 - The Guarantee Was On Delivery, The Price Was A Forecast"
type: lesson
created: 2026-11-18
tags: [advertising-science, lesson, auction, bidding, reservation, meta]
lesson: 84
topic: Auction Mechanics & Bidding
---

# Lesson 084 - The Guarantee Was On Delivery, The Price Was A Forecast

Video: `video/2026-11-18-lesson-084.mp4`

## The mechanism

This morning's research run read a Meta ad product off a live screen for the first time. Ads Super Burst, in a
UK account, 17 November. Three separate things in it are worth your time, and none of them is the product
itself. We cannot buy it and we will not try.

Start with what a guarantee actually covers.

You book a flight. The airline guarantees you a seat on that plane on that date. It guarantees nothing about
the fare. The same seat on the same route costs what the date costs, and the date is priced off demand the
airline can see and you cannot. Once you pay, the price stops moving. That is the whole of the guarantee. It
locks a number. It never promises the number is low.

Meta's reservation buying type is that. Pick Ads Super Burst inside Reach Planner and four controls grey out at
once: buying type reservation, performance goal reach, placements fixed to Facebook and Instagram Feed, Stories
and Reels, and frequency fixed at one impression per person. Targeting drops to broad in one country or region,
with no detailed interests and no custom audiences. You keep age bands, gender and sub-region exclusions.
Duration is a menu, 3, 6, 12 or 24 hours, defaulting to 6.

Then look at what the forecast does with the same flight.

Same UK geography, same six-hour length. Midnight to 06:00 reaches an addressable 14.9 million. 07:00 to 13:00
reaches 33.3 million. The tool defaults to the first one, which is worse by a factor of 2.2. On the date axis
the planner labels candidate days standard, elevated and peak, and the same six-hour window priced GBP 6.00 CPM
on a peak day against GBP 4.50 on the Friday nine days earlier. That is 33% more money for the same delivery
because of where the date sat.

So a reservation price is not a rate card. It is a forecast that moves with the same demand the auction moves
with. The saving sits in choosing the date, and the default window the tool hands you is the expensive mistake.

Meta's own suggested budget for one of those six-hour UK flights was GBP 33,010.67.

## The evidence

**[[Meta Delivery & Andromeda#MD-201|MD-201]], T1.** The configuration surface, read off Meta's own in-product
strings and its own forecasting output. Tiered T1 because the assertion is what a Meta product screen displays.
Honest bound on it: one UK account, seen through a practitioner screencast, not through documentation.

**[[Meta Delivery & Andromeda#MD-181|MD-181]], T1.** The October announcement, United States only. It published
a median 2.9-point ad recall lift, a median 0.6-point intent lift, and 34 million reached per flight. Not one
cost per result anywhere. MD-201 is the product. MD-181 is the press release. Notice the gap between them.

**[[Auction Mechanics & Bidding#AU-032|AU-032]], T3, and this is the real lesson.** The claim says Meta can only
guarantee a cheap CPM by serving worse prospects in worse placements, so auction is the correct default. Its
author raised the objection against himself on this screencast. The mechanism needs Meta to be able to choose
who sees the ad. Buy a high share of a named demographic and it cannot choose: "Your ads will be put in front of
everyone." Good prospects and bad ones arrive in their true proportion, and the quality argument shrinks as
audience share rises.

That is reasoning, not evidence. No conversion figure, no cost per result, and he states his own testing as very
limited with nothing to report. The claim stays active and the default stays auction, for two reasons he supplies
himself. The mechanism only dies at high share, and high share costs a month of budget in six hours. And a flight
capped at one impression per person cannot carry anybody to a conversion the way a frequency of three can.

**Learn the move, not the claim.** He did not add another example inside his own mechanism. He found the edge of
it and said where it stops. A mechanism claim has a domain. Finding the boundary is worth more than the tenth
confirmation from inside it.

**And check the arithmetic, including ours.** MD-201 and today's Harvest Log both say the roughly 10x cheap-reach
gap comes almost entirely from the frequency term. That sentence is wrong and the sum is two lines.
[[Meta Delivery & Andromeda#MD-053|MD-053]] holds the identity: cost per thousand people reached equals CPM times
frequency. A conversion campaign at GBP 20 CPM and frequency 3 costs GBP 60 per thousand reached, against GBP
4.50 at frequency 1. The gap is 13.3x. Decompose it. The CPM falls 20 to 4.50, a factor of 4.44. The frequency
falls 3 to 1, a factor of 3. Frequency is the smaller of the two terms, not almost all of it. The conclusion does
not change and the stated cause does. Flagged for correction.

## Our accounts

Phoenix Truxx statics, 9 to 15 November, Ads Manager figures throughout. CPM $32.29, campaign frequency 2.0053,
$12.72 per Ads Manager lead.

Run MD-053 on it. $32.29 times 2.0053 is $64.75 per thousand people reached. That is the number we never look at.
Hold the CPM exactly where it is and take frequency to 1 and it halves to $32.29. We pay for each person roughly
twice, and on the statics campaign that is mostly a breadth effect rather than fatigue. Lesson 081 decomposed the
same 2.0053 into 1.5477 repetition times 1.2957 distinct ads per person.

SJR Commercial sits at 1.70x account average frequency, 2.19x on the dump campaign.

Neither account can buy Super Burst and the reason is the targeting floor, not the price. One country or region
is the smallest geography on offer. Phoenix sells trucks to buyers around New Jersey. A UK-sized or US-sized
broad flight is not a narrower version of that. It is a different business.

The piece that does transfer is free. The forecast is a read on auction demand for a geography and it costs
nothing to open. Standard, elevated and peak day tiers and hour-of-day addressable audience come out of Reach
Planner without spending anything. Nobody has opened Reach Planner on any of our five accounts. Five minutes per
account answers whether it is even present, and that would also date the US rollout, which MD-181 and MD-201
together still cannot say.

## The decision rule

**A reservation guarantee covers delivery and nothing else. Before accepting any guaranteed-price product, price
the adjacent dates and read the hour window, because the default is the expensive one. Keep auction as the
default for anything measured in cost per lead.**

## Quiz

Drop your answers in `_answers-inbox.md`.

1. Ads Super Burst locks four delivery controls the moment you select it. Name them, and say which single one
   makes the product unusable for lead generation even if the geography were solved.
2. The same six-hour UK window priced GBP 6.00 CPM on one day and GBP 4.50 nine days earlier. What does that tell
   you about the word "guaranteed" in Meta's description of the product?
3. AU-032's own author argued his mechanism stops applying at high audience share. Why does the claim stay active
   and the operator rule stay unchanged?
4. Phoenix Truxx statics ran a $32.29 CPM at 2.0053 frequency last week. A client reads about a GBP 4.50
   reservation CPM and asks why we are paying seven times more. Write the answer in three sentences, with the
   arithmetic in it, and name the one thing in that comparison that is not a like-for-like number.
5. You are handed a reservation product in a geography we can actually buy, and the forecast says the Thursday is
   standard and the Saturday is peak. The client wants the Saturday for a dated event. Say what you check before
   quoting a price, and what you tell the client the guarantee does and does not cover.

> [!note]- Answer key
> 1. Buying type reservation, performance goal reach, placements fixed to Facebook and Instagram Feed, Stories and
>    Reels, and frequency fixed at one impression per person. The frequency cap is the killer. One impression per
>    person cannot carry a buyer through consideration, which is the whole job on a truck or a clinic offer.
> 2. The guarantee is on delivery, not on price. Meta commits to deliver the reach it forecast and to stop the
>    price moving after you book. The price itself is a forecast off the same demand the auction prices, so a
>    third more money for the identical flight is normal, and the saving lives in the date.
> 3. Because the objection is reasoning with no measurement behind it, and because the escape only opens at high
>    audience share, which costs a month of budget in six hours. The one-impression cap independently blocks
>    conversion work. What changed is a scope line, not the ruling: the degraded-prospect argument applies where
>    Meta has room to choose and stops where the flight buys nearly everyone.
> 4. Cost per thousand people reached is CPM times frequency, so we sit at $32.29 times 2.0053, which is $64.75,
>    and the GBP 4.50 figure is 4.50 times 1. Most of that gap is two different jobs: we buy repeated contact with
>    buyers near one dealership, that number buys one impression each across a whole country. The thing that is
>    not like-for-like is the currency, dollars against pounds, and nobody should quote the ratio until both sides
>    are in one currency.
> 5. Check the adjacent cheaper dates and the hour window inside the day, since the tool defaults to the worse
>    window, and check the forecast for the same flight on the standard day so the client sees what the Saturday
>    premium costs. Tell them the booking guarantees the reach estimate and freezes the price, and guarantees
>    nothing about leads, calls or sales. If the event is the point the premium may be worth it, and it is a
>    priced decision rather than a free one.
