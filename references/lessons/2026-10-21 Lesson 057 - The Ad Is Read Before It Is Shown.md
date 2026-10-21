---
title: "Lesson 057 - The Ad Is Read Before It Is Shown"
type: lesson
lesson: 57
date: 2026-10-21
topic: Meta Delivery & Andromeda
claims: [MD-184, MD-185, MD-186, MD-120, MD-178, MD-001, MD-070, MD-171, MD-177, CR-287]
video: "video/2026-10-21-lesson-057.mp4"
tags: [advertising-science, lesson, meta, genrecs, tokenization, cold-start, law-1]
---

# Lesson 057 · The Ad Is Read Before It Is Shown

![[video/2026-10-21-lesson-057.mp4]]

Yesterday's research run banked six claims off one Meta engineering post. Three of them describe the same change, and together they move law 1 from something we argue to something Meta documents.

The post also carries one word that will get misquoted inside a month. Both halves are in here.

## 1. The mechanism

Picture the old system first, because the change only makes sense against it.

Every ad used to get its own private ID. A number. The number said nothing about the ad. The only way the model could learn anything about ad number 48219 was to serve it, watch what happened, and write the result against that number. A brand-new ad was a blank row. It bought its way out of the blank row with your money.

Here is what Meta says it does now, quoted: "Rather than maintaining a dedicated ID for every item, GenRecs Tokenization represents each item with a set of tokens from a stable semantic vocabulary."

So instead of a private number, each ad gets a short sequence of tokens pulled from one shared vocabulary that every item in the system draws on. Ads, products, pages and pixels, all described in the same language.

Where do the tokens come from? Meta's own sentence, and read it twice: "Pre-trained multimodal models read each ad, product, and page, **including its text and images**, and encode the items into an embedding that carries world knowledge."

The ad's words. The ad's pictures. That is the input.

**The analogy.** A library with a barcode on every book. The barcode is unique and it is meaningless. To find out whether a reader will finish book 48219 you hand it to readers and watch. Now the library throws out the barcodes and writes each book a short description taken from its own pages: crime, Scottish, 1970s, first person, bleak. A reader who finished three other books carrying that description is a sensible first guess for this one. On day one. Before anybody has opened it.

Two things follow, and Meta states both.

**A new ad is not a blank row.** "Because tokens describe what an item is, the model can relate an item it has never seen engagement for, to items it knows well." Meta's own example is a sportswear brand launching next season's trail shoe, and the clause worth memorising is the last one: tokenization lets the new product build on what the model learned from last season's shoe, "even before anyone sees the new ad."

**The description travels.** "Semantic tokenization creates a stable vocabulary that allows the models to carry insights across campaigns for advertisers."

Then the trap. The post frames all of this as "Generative Recommenders", a shift "from scoring every individual ad candidate to leveraging LLM architecture". Someone will read that as Meta writing ads.

The hardest refutation is Meta's own citation. Under the words "Our work on LLM-native retrieval shows how far this can go", the post links a paper titled **"The Case Against Generation for Retrieval: Discriminative Language Models as Effective Retrievers"**. Two of its six authors wrote the blog post. Its abstract says it adapts LLMs as semantic representation backbones "rather than generative engines", and concludes that "the traditional two-tower paradigm remains an exceptionally competitive and practical solution for industrial retrieval systems".

What is generative is the **description**. The scoring stays the same discriminative two-tower machinery it was. Nothing in either source says Meta writes your copy or makes your creative.

## 2. The evidence

Nine claims, four tiers, and the tier movement is the real lesson.

- [[Meta Delivery & Andromeda#MD-184|MD-184]], **T1**. The tokenization mechanism, read in full at source. Meta's own words that the model reads the ad's text and images.
- [[Meta Delivery & Andromeda#MD-185|MD-185]], **T1**. Item-side cold start and cross-campaign transfer, both quoted.
- [[Meta Delivery & Andromeda#MD-186|MD-186]], **T1**. The reading rule on the word "generative", resting on Meta's own cited paper.
- [[Meta Delivery & Andromeda#MD-120|MD-120]] and [[Meta Delivery & Andromeda#MD-178|MD-178]], both **T1**. The two earlier statements that put ad creative representation in the model's first-class feature set, beside user location and demographics. MD-184 is the third, and the first that describes the pixels being read rather than naming "ad content representations" in a taxonomy.
- [[Meta Delivery & Andromeda#MD-001|MD-001]], **T3**. The avatar half of law 1: that the callout in the ad decides who sees it. Practitioner convergence, no test. **It did not move yesterday and it should not have.** Meta documents that the creative is read. Meta does not say the creative decides the audience.

Now the tier move that matters most, because it is a refusal.

- [[Meta Delivery & Andromeda#MD-070|MD-070]], **T3, deliberately left at T3.** It claims a proven ad keeps what it has learned when you move it to another campaign. Meta just said cross-campaign transfer out loud. It looks like an upgrade and it is not one. Meta is describing the **model's representation of an item** carrying across campaigns. MD-070 is about an **ad object's delivery performance** carrying across campaigns. Those are different objects. Reading the first as proof of the second is a mis-bank, and the direction being confirmed is not the claim being confirmed.

And the numbers, which are the weakest part of the whole post.

- The only published outcome is **+0.35% in conversions**, and it is attributed jointly to GenRecs Tokenization, GEM and the Adaptive Ranking Model together. No part of it is separable.
- The footnote reads, in full: "Meta Internal Data, measured in February 2026." A data owner and a month, published eight months later. No population. No window. No control. No sample.
- [[Meta Delivery & Andromeda#MD-177|MD-177]] carries GEM's published **18.9%** conversion improvement. This post attributes **0.35%** to a trio including GEM. Two orders of magnitude apart, never stated to be measuring the same thing. Neither figure goes in front of a client and the pair never goes in a forecast.
- So [[Meta Delivery & Andromeda#MD-171|MD-171]]'s rule gets a sharper edge. The old test was "read the footnote". The test is now **find the population and the counterfactual**. A footnote that says "internal data, February" satisfies neither.
- [[Creative Science#CR-287|CR-287]], **T2**, is the same failure from the other direction. A Kuaishou production A/B reports CTR +2.87%, CVR +2.74%, ARPU +9.85% for per-user generated creative. Those are measured **over a generative baseline**, not against a human-made creative library. The paper's argument is generation versus retrieval and its measurement is not.

## 3. Our accounts

Start with the honest part. Nothing here is a lever. Meta publishes no rollout scope, no eligibility, no surface list and no date on which tokenization reached any account. There is no setting to find. The right response is a change in how we write and how we read, and no change in the ad manager.

**Phoenix Truxx, and the trap is ours before it is anyone else's.** The 26 ft box image took 48 leads at $8.30 in September against 9 at $15.63 in August. Same creative, two prices, one account. Chriss Spanish ad 1 is the sharper case. It was the dump engine in its earlier run, 57 leads and 37 of the month's 79 dump requests at $19.65. It was rebuilt from its original post and put into the new "Core NJ + NY ring" campaign on 9 October, where it took 18 opt-ins at $12.13 in the first week.

That pair looks like cross-campaign transfer proving itself. It is not, and MD-070 is exactly why. The creative was **rebuilt**, so it is a new object. The campaign is new. The audience excludes 30-day form fillers. And $19.65 was a cost per dump request while $12.13 is a cost per opt-in, which are different denominators. Four confounds and a unit mismatch. Anyone who quotes that pair as evidence of transfer has done the thing the research run refused to do.

**SJR Keyport Kia is the cleanest cold-start case on the book, and it is sitting unlaunched right now.** Seven Telluride hook ads at 9:16, client-approved 13 October. Seven more built 20 October, five Portuguese and two Spanish. Fourteen ads, none live, in a lane that has never run a Kia ad in this account.

Under MD-185 the account's own history is not what those ads inherit from. They inherit from whatever the model already holds about semantically similar items across the whole system, because the vocabulary is shared rather than account-scoped. What they carry in is their own text and their own frames. That is the entire first-day input, and it stays fully under our control for another few days.

**ChiroWorks is off the board.** All ads paused since 14 October and nothing restarts without Lucky. Nothing to test there.

The useful consequence across all of it is small and real. When the words and the pictures are the input, a vague ad is not a neutral ad. It is a bad description. "Work trucks, all credit considered, South Amboy" describes something. A hero shot with a slogan over it describes very little, and we now have Meta's own sentence for why that costs something on day one.

## 4. The decision rule

**Put the buyer, the problem and the offer into the ad's own words and pictures, because that text and those images are literally the input the model is handed.**

## 5. Quiz

**1.** What replaced the per-item ID, where do the replacements come from, and why does the change mean a brand-new ad is not a blank row?

**2.** Meta now states cross-campaign transfer in its own words, and MD-070 was still left at T3. Explain the distinction in one sentence, and say what a correct upgrade would have to show.

**3.** Someone on the team says Meta is generative now and writes the ads. Name the single strongest thing that refutes it, say why it is the strongest, and give the one-line version of what is actually generative.

**4.** A deck has "+0.35% conversions, GenRecs Tokenization" and "18.9% conversion improvement, GEM" on the same slide as evidence that the Meta machine is getting better. Name three separate defects before that slide leaves the building.

**5.** Fourteen Kia hook ads are built and none is live, in an account that has never run a Kia ad. Under MD-185, say what the model already has to go on, what it does not, and name one thing you would change about the ads themselves before launch because of it. Then say honestly what you would and would not be able to measure afterwards.

Answers into `_answers-inbox.md`.

> [!note]- Answer key
>
> **1.** A short sequence of tokens from a stable semantic vocabulary shared across every item type in the system, including ads, products, pages and pixels. The tokens are produced by pre-trained multimodal models reading the item's own text and images into an embedding, which is then decomposed into independent subspaces and quantized against codebooks. A new ad is not a blank row because the tokens describe what the item **is**, so the model can relate an item it has never served to items it knows well, which Meta states happens "even before anyone sees the new ad".
>
> **2.** Meta is saying the **model's representation** of an item carries across campaigns; MD-070 says an **ad object's delivery performance** carries across campaigns, and those are different objects. A correct upgrade would need a measurement of the ad's own outcome, same creative, moved between campaigns, with budget, audience, optimisation event and window held constant, on a creative that was not rebuilt. The direction being confirmed by the platform is not the claim being confirmed.
>
> **3.** Meta's own citation. In the same paragraph that frames the work as generative, the post links arXiv 2607.25346, titled "The Case Against Generation for Retrieval: Discriminative Language Models as Effective Retrievers", and two of that paper's six authors are the first two authors of the post. It is the strongest refutation because it is first-party and self-inflicted, so nobody can argue it is an outside critic misreading Meta. What is generative is the **representation** of the item, composed semantic tokens instead of an opaque ID. The retrieval mechanism stays two-tower and discriminative, and nothing in either source says Meta writes copy or produces creative.
>
> **4.** Three from this list. The 0.35% is **jointly attributed** across three systems including GEM, so no part of it belongs to tokenization. Its footnote names only a data owner and a month, so there is **no population and no counterfactual**, which is the MD-171 test. The two figures sit **two orders of magnitude apart** and are nowhere stated to measure the same thing, so putting them on one slide manufactures a comparison the source does not make. A fourth is available: the measurement is dated February 2026 and published in October 2026, with nothing said about whether it still holds.
>
> **5.** The model has the tokens it can build from each ad's own text and frames, plus whatever it already holds about semantically similar items across the system, because the vocabulary is shared rather than account-scoped. It does not have anything from this account's Kia history, because there is none, and it does not have engagement on these specific ads. The change worth making is to put the actual buyer, the vehicle and the service promise into the visible copy and the frame rather than leaning on a hook alone, since that text and those images are the whole of the first-day input. The honest measurement answer is the important half: we will see cost per opt-in on the new lane, and we will not be able to attribute any part of it to tokenization, because there is no control, no toggle, no rollout date and no comparable prior Kia ad in the account. It is a reason to write the ads better, not a result we can claim.
