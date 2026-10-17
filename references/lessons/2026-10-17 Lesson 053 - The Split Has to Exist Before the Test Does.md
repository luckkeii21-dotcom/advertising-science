---
title: "Lesson 053 - The Split Has to Exist Before the Test Does"
type: lesson
lesson: 53
date: 2026-10-17
topic: Google PMax & Shopping
claims: [GP-040, GP-042, GP-041, GP-005, GP-007, GP-004, GP-039, AT-072, AT-061, MD-019, MD-170]
video: none (Saturday)
tags: [advertising-science, lesson, pmax, incrementality, new-versus-returning]
---

# Lesson 053 · The Split Has to Exist Before the Test Does

Rotation day, and the topic is Google PMax and Shopping. It has been next in line for six lessons running. You do not buy PMax and you may never buy it. Teach it anyway, because the best-measured experiment in that whole file is about a mistake that is live on every account you run right now. Google is just where somebody finally wrote the numbers down.

## 1. The mechanism

A campaign type gets sold as prospecting. It has a setting called new customer acquisition. You turn the setting on, you run the campaign, and the reported numbers come back good.

Two separate things then go wrong, and they compound.

The first is that the setting does not decide who gets reached. The optimisation event does. If your conversion action is "purchase" and your existing customers are the people most likely to purchase, the system walks into the warm pool, because that is where the event lives. The audience instruction loses to the event instruction ([[Google PMax & Shopping#GP-042|GP-042]], T3). The quoted frequency is "greater than 50% of the time performance max goes after repeat".

The second is that the reported number cannot tell you this happened. A conversion is a conversion in the column. Warm and cold land in the same cell. So the campaign reads as acquisition working, and the more budget it spends on people you already had, the better it reads, because those people were always going to convert.

The analogy that actually maps. You pay a scout to find you new players. The scout spends the season in your own clubhouse, signs four of your existing squad to fresh contracts, and sends an invoice listing four signings. Every line on the invoice is true. The scout found nobody. The invoice has no column for that, and no instruction you wrote on the contract changes what the invoice can show. The only way to catch it is to count your squad before and after.

## 2. The evidence

[[Google PMax & Shopping#GP-040|GP-040]] is **T2** and it is the only shown-data incrementality test in that entire topic file. A 21-day geo holdout on an Australian ecommerce account. Test states Victoria and Queensland, control the rest of Australia, states chosen by correlating monthly order patterns, baseline built from 12 months of daily orders, confidence set at 90%.

The result on the outcome the campaign was bought for. Expected 2,771 new-customer orders, actual 2,857. A lift of 85 against the 166 needed for relevance at 90%. **Not statistically relevant.** New-customer orders fell in both arms over the window, down 4.5% in the control and down 1.41% in the test, which is a market-wide decline the holdout separates out and an in-platform read would have swallowed whole.

The result on the other outcome. Returning-customer orders up 6.8% in the test states while the rest of the country dipped. Expected 1,211, achieved 1,521, at $39 each, which the operator calls very profitable.

Now the part worth the whole lesson. **A blended read of that test reports a clean win.** Add the two outcomes together and the campaign looks like it worked. The only reason the null result is visible at all is that new and returning were specified as separate outcomes *before the test started*. That is the design decision, and the same experiment is banked again at [[Attribution & Incrementality#AT-072|AT-072]] precisely because the rule generalises past Google.

The surrounding claims are weaker and hold them as weaker. [[Google PMax & Shopping#GP-005|GP-005]] (T3) puts the warm share of PMax conversions at 50% and up, with 70 to 80% as the modal audit finding, asserted from a 250-plus account portfolio with nothing shown. [[Google PMax & Shopping#GP-007|GP-007]] (T3) says discount the reported figure 30 to 40% even with brand excluded, and it is honest that this is a prior rather than a measured coefficient, to be replaced by the account's own holdout the moment one exists. [[Google PMax & Shopping#GP-041|GP-041]] (T3) is the decision the operator took off his own T2: he kept the campaign at much reduced budget and reclassified it from acquisition to retargeting.

One more, and it is the fix rather than the complaint. [[Google PMax & Shopping#GP-039|GP-039]] (T3) says if you need a campaign you can *prove* is cold, build it where you can apply a negative bid adjustment to existing customers, not where you can only hand over an audience signal, because a signal does not restrict delivery at all ([[Google PMax & Shopping#GP-004|GP-004]]).

## 3. Our accounts

Here is the Meta twin, same shape, same axis. [[Meta Delivery & Andromeda#MD-019|MD-019]] is **T1**: audience segments in Meta account settings are a reporting breakdown and nothing else. Meta's own help page opens by saying so. The thing that sounds like allocation is a column. And [[Meta Delivery & Andromeda#MD-170|MD-170]] (T1) has Meta now recommending every advertiser exclude existing customers. On both platforms the event beats the audience setting, and on both platforms the thing named like a lever is a label.

Now the honest state of our own book, which is worse than not knowing the answer. We cannot ask the question.

- **StayWell.** 142 of 144 CRM contacts are not patients. Upload that file as an exclusion and you suppress the prospects we already paid to find.
- **ChiroWorks.** 103 of 143 have never booked, so 72% of the only list we hold.
- **SJR Commercial.** 99.94% net-new across 14,515 Meta contacts, and that figure is net-new *by construction*, because GoHighLevel merges on the email address and the file cannot count the same person twice.
- **Phoenix Truxx.** Zero duplicates across 906 phone numbers. Same construction, same non-answer.

Read those four lines together. Every account shows a high new-customer share, and not one of those shares is a measurement. The real patient records sit in the clinics' own practice software and have never been handed over. So if you ran GP-040's holdout on ChiroWorks tomorrow, perfectly, you would get a blended booking lift and no way to split it, which is the exact read GP-040 tells you never to take.

The ad-set case is already on file and it rhymes. `NJ/SI - 3s VV Retarget` is the only non-broad ad set in our entire book. $142.05, 30 opt-ins, **$4.74 each against $8.19** in its lane, our cheapest row. On CPM it is our most expensive at **$40.94 against $13.38 and $16.55**. Its pool is our own three-second video viewers, so every person in it was found and paid for by another ad set first, and [[Attribution & Incrementality#AT-061|AT-061]] (T4) predicts that cheap row whether the ad set added thirty opt-ins or zero. Lesson 027 named the test. It has not been run.

## 4. The decision rule

**A campaign is only measurable as acquisition if new and returning are separate outcomes before the test starts. No setting, no audience signal and no reporting breakdown substitutes for that split, so the first job on every account is a new-customer event that fires on its own.**

The cheap version on our book is one workflow step: fire a distinct event the first time a phone number or email appears, and nothing after. One step, four accounts, and the holdouts we have been queueing for two months become readable.

## 5. Quiz

1. GP-040 is T2 and the three claims around it are T3. Say in one sentence what the T2 bought that the three T3s cannot buy. Then name the one number in GP-040 that must never be quoted, and why.
2. GP-042 says the conversion action beats the audience setting. Name the Meta claim that is the same statement on the Meta side, give its tier, and say why the tier difference matters when you repeat this to a client.
3. ChiroWorks has 143 CRM contacts, 103 of whom have never booked. The client asks you to upload the list as an exclusion because Meta now recommends excluding existing customers. Give your answer, the claim IDs, and say exactly what you would need before the answer changes.
4. You are handed a 21-day geo holdout on StayWell, run correctly, and it reports a 7% lift in total bookings in the test region. Write what you can conclude. Then write what the client will conclude. Name the one thing that closes the gap and roughly what it costs.
5. GP-007 tells you to discount a reported figure by 30 to 40%. Say why applying that to Phoenix Truxx's $4.00 all-time cost per opt-in would be wrong, and name the only thing that would make a discount legitimate on that account.

> [!note]- Answer key
> **1.** The T2 bought a counterfactual: a control arm, so the market-wide decline in new-customer orders shows up as a decline instead of being read as the campaign working or failing. The three T3s describe the same shape from inside accounts and cannot separate the campaign from the market at all. The number never to quote is the $140 implied new-customer iCAC. The lift it is computed from is not statistically relevant, so $140 is arithmetic on a null result, and the source says so itself.
> **2.** MD-019, and it is **T1** against GP-042's T3, because Meta's own help centre and Marketing API documentation both state that audience segments are a reporting breakdown. The tier difference matters because the Meta version is something you can show a client on Meta's own page, and the Google version is one specialist's recalled frequency with no denominator behind it. Say the first as documentation. Say the second as a practitioner claim, out loud.
> **3.** No. MD-170 (T1) is real and the recommendation is genuine, but the file we would upload is 72% people who have never booked, so excluding it suppresses prospects we already paid to reach. What changes the answer is the clinic's practice-management patient file, which is a request rather than a calculation and has never been made. With that file the exclusion becomes exactly what Meta is describing.
> **4.** You can conclude total bookings rose in the test region. You cannot say whether any of it was new patients, because 142 of 144 CRM contacts are non-patients and nothing on that account fires a distinct new-customer event, so the two outcomes are inseparable. The client will conclude the ads acquired patients. GP-040 and AT-072 say a blended read is exactly the read that reports a win on a null acquisition result. What closes it is a first-touch event written into the automation, one workflow step, and it has to exist before the next holdout rather than after it.
> **5.** Because the 30 to 40% band is a working prior from somebody else's ecommerce book on a different platform, and GP-007 states on its own face that it is a prior to be replaced by the account's own holdout. Applying it to $4.00 invents a number. That $4.00 also straddles the March 2026 click redefinition, so part of the average was measured under different definitions. The only thing that legitimises a discount on Phoenix Truxx is a holdout on Phoenix Truxx, read on separated new and returning outcomes.

Answers into `_answers-inbox.md`.
