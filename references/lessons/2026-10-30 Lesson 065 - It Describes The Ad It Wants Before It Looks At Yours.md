---
title: "Lesson 065 - It Describes The Ad It Wants Before It Looks At Yours"
type: lesson
lesson: 65
date: 2026-10-30
topic: Meta Delivery & Andromeda
tags: [advertising-science, lesson, meta-delivery-andromeda]
---

# Lesson 065 - It Describes The Ad It Wants Before It Looks At Yours

Topic: Meta Delivery & Andromeda. Harvest-driven. Yesterday's research pass was the heaviest Meta architecture day since Andromeda first launched: eight claims banked, four of them T1 Meta. The sharpest is [[Meta Delivery & Andromeda#MD-191|MD-191]], and it changes the order of operations you have been picturing. Video: `video/2026-10-30-lesson-065.mp4`.

## 1. The mechanism

Here is how everyone pictures ad delivery, including us until yesterday. There is a pile of ads. A person opens Facebook. The system walks the pile, scores each ad against that person, and serves the winner. Your ad competes inside the pile.

Meta published something on 28 October that runs the other way round.

Step one, which Meta calls GenRecs Tokenization. Models "read each ad's text and images and describe the ad in semantic tokens that capture its key attributes". Every ad gets converted into a short machine description of what it actually is.

Step two is the part to slow down on. The system "generates the semantic ID for the ideal ad for a person, then matches that to the ads available in our system."

Read those in order, because the order is the whole finding. The system does not start at the pile. It starts at the person, writes the description of the ad that person should see, and then goes looking for the closest real ad it happens to have.

The normal-life version. There are two ways to do a grocery run. You can walk every aisle and rate everything you pass. Or you can write "something quick for dinner, spicy, under three hundred rupees" before you leave the house, then find the nearest thing on the shelf to what you already wrote down. The list got written without looking at the shelf. If your product is not close to anything anyone writes down, the aisle it sits in does not save it.

Your ad's job, in that second picture, is to be the nearest available answer to a brief the system wrote without reference to your account.

Two more claims from the same day change the shape around it.

[[Meta Delivery & Andromeda#MD-188|MD-188]]: the current Andromeda scores **every eligible ad**, at over a billion ads per second on one GPU server. The 2024 design reached an enormous number of ads rather than all of them. One excuse is now gone. An ad that did not get shown was not pruned before anyone looked at it. It was looked at and it lost.

[[Meta Delivery & Andromeda#MD-189|MD-189]]: the retrieval model's quality now "approaches ranking-level" at roughly 300x fewer inference-time FLOPs. The reason the funnel at [[Meta Delivery & Andromeda#MD-022|MD-022]] has stages at all is that deep judgement was too expensive to run early. If the cheap early stage now judges nearly as well as the expensive late one, there is no crude gate left to get lucky at.

And [[Meta Delivery & Andromeda#MD-190|MD-190]] names the stage that enforces your targeting: index matching, moved onto the GPU, benchmarked at over 100 billion ads per second, absorbing ad creations, edits and expiries throughout the day. Your targeting is a filter running before and beside scoring, which is the documented version of what we previously held at T3.

Put together: the targeting you set is a filter, the description of your creative is the matching key, and the matching key gets generated before your ad is consulted.

## 2. The evidence, and where it stops

[[Meta Delivery & Andromeda#MD-191|MD-191]] is **T1**. Meta describing a product on its own business-news pages, dated 28 October, two pages cross-read. MD-188, MD-189 and MD-190 are also T1, same source day.

T1 is the ceiling in this codex and it earns the mechanism. It earns nothing else, and here is where it stops.

**The figures are platform aggregates.** Generative retrieval drove "a nearly 2% increase in conversions across targeted segments" on Facebook Feed, and "+0.35% lift in conversions across surfaces" when paired with GEM and the Adaptive Ranking Model. "Across targeted segments" is undefined and is not an account-wide number. Nobody can look for 2% in their own account.

**It is Facebook Feed only.** Meta says nothing about Instagram, Reels or any other surface. Remember that one, it matters in section 3.

**The speed claim carries no number at all.** Meta states that new and refreshed creative "get on a faster track to performing, because the system can understand them through what it already knows about similar ads and products, whether the signals are plentiful or more limited". That is a mechanism for why a new ad in an established account is not starting from nothing. It is Meta asserting it, with no figure on the speed, no comparison and no test.

**Nothing here is visible or controllable from an ad account.** There is no setting, no readout, no opt-in.

Now the tier work worth learning from, because a claim moved yesterday.

[[Creative Science#MD-186|MD-186]] was banked on 20 October at T1. It ruled that "generative recommenders" does **not** mean Meta retrieves or writes ads generatively, resting on Meta's own cited paper, "The Case Against Generation for Retrieval". Yesterday Meta published a product it calls generative retrieval. So MD-186 is now **contested on its retrieval limb**, and the split is clean.

The limb that survives untouched: **Meta still does not generate the ad.** No ad is written by a model. If a client asks you that question, the answer is still no.

The limb in contest: something genuinely is generated inside the retrieval path. MD-186's reading rule was the right call and it needed narrower wording. What is generated is a **target representation**, not an ad and not a retrieval result. Retrieval is still a matching operation against that target. The cited paper argues against generating the result, which is perfectly compatible with generating the query.

That is what a contest looks like when it is done properly. The claim does not get deleted and it does not get quietly rewritten. One limb holds, one limb is marked, and the wording gets tighter.

One more. [[Meta Delivery & Andromeda#MD-120|MD-120]] held that ad creative representation is a named GEM input feature. That was the strongest support the creative-is-the-targeting law had. It was strengthened yesterday and **demoted to second strongest**, because a matching key the system generates before it ever looks at your ad outranks an input feature.

Last guard, and it is a rule rather than a note. [[Meta Delivery & Andromeda#MD-192|MD-192]] has Meta's Q2 2026 platform lift, 8.3% more ad clicks and 15.7% more conversions on Facebook, footnoted to earnings. **It never goes in a client report.** A platform-wide uplift is not a lift any advertiser can look for in their own account, and an account that got worse over that quarter is not contradicting it.

## 3. Our accounts

The useful test of MD-191's speed claim is already on our book, and it points two ways in the same lane in the same month.

SJR Commercial, dump truck lane. Filed week of 9 to 15 October: the **new** Caesar Dump English AI dub came in at **$4.64**, the cheapest dump unit in the account on arrival. A brand new creative landed straight at the front.

Filed week of 16 to 22 October, same lane, same account: the **new** English AI dub v2 came in at **$26.62 for 3 opt-ins**, against the original dub at **$6.39**. Our own filed call was to cut v2 and keep the original.

Hold those two side by side. Same speaker, same truck, same offer, same language, same account, one week apart. Whatever semantic neighbourhood the first dub sat in, the second one sat in it too. One arrived cheapest in the account and one arrived four times worse than the ad it was meant to replace.

So the honest reading of the speed claim is narrow. "Understood through similar ads" is a statement about not being cold. It says nothing about being good, and it predicts nothing about which of two near-identical ads wins. Our own numbers are the counterweight to the only operating consequence the claim offers.

The same week gives the other half. The Spanish Caesar dump ad went from $13.12 to **$7.00 on 20 opt-ins** and became the dump engine. That is an existing ad improving, which no claim here speaks to.

Phoenix Truxx, 16 to 22 October: the established statics engine ran 74 opt-ins at **$13.29** while the new dump lane ran 19 at **$18.71**, with only the Spanish Chriss video working. That lane still carries both confounds we filed: Spanish and video moved together, and the campaign launched 9 October so week one is being read against week two. It cannot answer a creative question yet and MD-191 does not rescue it.

Now the limit that applies to all of it, from our own filed data. MD-191 is Facebook Feed only. The SJR weekly for 16 to 22 October records **Facebook Reels delivering 34 of the 95 opt-ins**. More than a third of that week's results came from a surface this claim says nothing about. Before we reason from a Feed mechanism on our accounts, we have to know how much of the account is even on Feed, and the filed answer is that a large slice is not.

## 4. The decision rule

**Write every ad so a machine reading only its own text and images can say what it is, who it is for and what the offer is, because the system describes your creative in its own words before it ranks it and matches that description to a brief written without you. A new ad is not cold, and being understood early is a long way from being good.**

## 5. Quiz

Answers go in `_answers-inbox.md`.

**Q1.** State MD-191's two steps in Meta's own order. Then say which step is the finding and why the order is the thing that matters.

**Q2.** MD-186 was T1 and is now contested on one limb only. Name the limb that survives, the limb in contest, and the narrower wording that fixes it.

**Q3.** A client reads a headline and asks whether Meta's AI is writing their ads now. Answer in two sentences, with a claim ID behind each. Then name the Meta figure from yesterday's bank that may never appear in their report, and the reason.

**Q4.** Applied. SJR dump lane. The new English dub arrived at $4.64 and the new English dub v2 arrived at $26.62 against the original's $6.39. A teammate says MD-191 shows new creative gets on a faster track, so v2 just needs more time. Rebut it using those numbers, and state exactly what the faster-track claim does and does not promise.

**Q5.** Applied. You are briefing the next Phoenix Truxx dump creative. List three concrete things you change in the ad itself because of MD-191. Then name the one fact from our own filed weeklies that limits how far you can push this reasoning on our accounts, with the number.

> [!note]- Answer key
>
> **A1.** Step one, GenRecs Tokenization: models read each ad's text and images and describe the ad in semantic tokens. Step two: the system generates the semantic ID of the ideal ad for the person, then matches that to the ads available. Step two is the finding. The order matters because the system starts at the person rather than at the ad pile, so the matching key exists before your ad is consulted, and your ad's job is to be the nearest available answer to a brief written without reference to it. An answer that says Meta scores the pile against the person has given the old picture and gets nothing.
>
> **A2.** Surviving limb: Meta does not generate the ad. No ad is written by a model, and that answer to a client is unchanged. Contested limb: Meta has shipped a product it calls generative retrieval in which something genuinely is generated inside the retrieval path. The narrower wording: what is generated is a target representation, not an ad and not a retrieval result, and retrieval remains a matching operation against that target. Credit for noting the cited paper argues against generating the result, which permits generating the query.
>
> **A3.** Two sentences close to: no, Meta does not write or generate your ads, and MD-186's writing limb holds on Meta's own published position. What it does do is read your ad's text and images, describe it in its own machine tokens, and use a generated description of the ideal ad for each person as the matching key, which is MD-191. The figure that may never appear: MD-192, the 8.3% more clicks and 15.7% more conversions on Facebook in Q2 2026. Reason: it is a platform-wide aggregate on Meta's own measurement, no advertiser can look for it in their own account, and quoting it sets an expectation we cannot deliver or defend. Deduct for any answer that puts the "nearly 2%" generative-retrieval figure in a client sentence either, since "across targeted segments" is undefined.
>
> **A4.** The two ads sat in the same semantic neighbourhood by construction: same speaker, same truck, same offer, same language, same account. If being understood through similar ads decided the outcome, those two could not land at $4.64 and $26.62. So the faster-track claim promises only that a new ad is not starting cold, and it promises nothing about whether the ad is any good or which of two near-identical ads wins. Add the evidence state: the speed claim carries no number, no comparison and no test, it is Meta asserting it, and three opt-ins is not a window that supports any verdict in either direction. Our filed call, cut v2 and keep the original, stands.
>
> **A5.** Any three of: say the vehicle type and body in the ad's own words rather than only showing it, because the tokenizer reads text and images and is the only thing describing your ad. Name the buyer and the qualifying condition in the copy. State the offer explicitly instead of implying it. Keep one idea per ad so the machine description is not an average of three. Avoid carrying the whole meaning in a visual gag or in audio, since the stated inputs are text and images. The limiting fact: MD-191 is Facebook Feed only, and the filed SJR week of 16 to 22 October records Facebook Reels delivering 34 of the 95 opt-ins, so more than a third of that week's results came from a surface the claim does not cover. Credit also for naming that nothing here is visible or controllable in the account, so this changes the brief and never the settings.
