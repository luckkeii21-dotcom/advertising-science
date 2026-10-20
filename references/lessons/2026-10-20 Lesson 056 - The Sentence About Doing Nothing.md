---
title: "Lesson 056 - The Sentence About Doing Nothing"
type: lesson
lesson: 56
date: 2026-10-20
topic: Meta Delivery & Andromeda
claims: [MD-182, MD-183, MD-128, MD-139, MD-001, MD-171, AT-128, SC-179]
video: none
tags: [advertising-science, lesson, meta, creative-enhancements, defaults]
---

# Lesson 056 · The Sentence About Doing Nothing

Yesterday's harvest banked eight tier 1 claims and lesson 055 spent itself on one of them. Six are still untaught. Two of those six are the same change seen from opposite sides, and read together they teach something neither teaches alone.

Both arrived in the same Meta changelog. One tells you exactly what happens if you ignore it. The other does not.

## 1. The mechanism

Every new platform capability has two halves.

The first half is what it does. That half gets the product copy, the screenshot, the blog post. It is the half everyone reads.

The second half is one sentence long: **what happens if you do nothing.** Nobody writes a blog post about that sentence. It decides whether the capability is an opportunity sitting in a drawer or a change already running on your account.

The analogy. You pick up a rental car. The brochure in the glovebox explains lane-keep assist in four paragraphs. The paragraph you actually need is the one that says whether it is on right now, because that decides whether the wheel will fight you on the first bend. There is a second question the brochure never answers: if the valet moves the car, does it come back on by itself.

Those are three different facts. What it does. Whether it starts on. Whether it stays off. A platform can publish the first and stay silent on the other two, and silence is not the same as off.

Yesterday's two claims sit on opposite ends of that.

**[[Meta Delivery & Andromeda#MD-182|MD-182]] states its sentence.** Creative audience pairing moves age and gender off the ad set and onto the ad creative. You switch it on by setting `creative_audience_pairing` to 1 inside `targeting_automation` in the ad set targeting spec. The field takes 0 or 1, and Meta says plainly that omitting it leaves the feature off. Nothing changes on any account until a person turns it on. The granularity is real and it is new: a persona can hang on the whole ad or on one image or video inside `media_sourcing_spec`, and Meta publishes the precedence rule itself, where the asset's persona beats the ad's. So one ad can aim four assets at four age bands. That collapses the old split where the ad set declared the audience and the ad declared the message, and it runs the same direction as [[Meta Delivery & Andromeda#MD-001|MD-001]], where the creative is already the primary targeting input.

**[[Meta Delivery & Andromeda#MD-183|MD-183]] does not state its sentence.** Three Advantage+ enhancements shipped on 28 June 2026 and all three change the footage rather than the targeting:

- **Image Animation.** A static image "is automatically transformed into a short, subtly animated video". Field `image_animation`.
- **Video Filter.** A visual enhancement "is automatically applied", including converting standard dynamic range video to HDR. Field `video_filtering`.
- **Video Uncrop.** Your video "is automatically expanded (uncropped) to better fit the aspect ratio of additional placements", filling vertical full-screen surfaces instead of cropping or letterboxing. Field `video_uncrop`.

All three live in `degrees_of_freedom_spec.creative_features_spec`, per creative. The change notes say you opt in or out per creative. They never say which state you start in.

## 2. The evidence

Four claims, three tiers, and the tiers are the point.

- [[Meta Delivery & Andromeda#MD-182|MD-182]], **T1**. Meta's own changelog, read at source. The default is stated, so the default is settled.
- [[Meta Delivery & Andromeda#MD-183|MD-183]], **T1**. Same source, same credibility, and still silent on the default. Tier 1 certifies what is written. It cannot certify what was left out.
- [[Meta Delivery & Andromeda#MD-128|MD-128]], **T1 for the surface and the default state only**. The previous member of this family, Flex Media, ships **on by default** and licenses Meta to recrop the creative "in any way that Meta wants". That is why the gap in MD-183 is not a neutral gap. The nearest precedent in the same family starts switched on.
- [[Meta Delivery & Andromeda#MD-139|MD-139]], **T3**. Enhancements re-arm themselves. Duplicating an ad does it, editing the primary text does it, and previewing an ad has been seen to do it. Thin evidence, one operator, no state capture. Treat it as a reason to re-check rather than as an established behaviour.

Hold the shape of that. T1 says the three enhancements exist and alter pixels. T1 says nothing about their default. T1 elsewhere says the family's older sibling starts on. T3 says state does not hold still. **The decision you need is not covered by any of them, and the honest move is to read the account rather than pick a side.** Same discipline as [[Attribution & Incrementality#AT-128|AT-128]] yesterday, where tier 1 settled the behaviour and left the scope open.

None of the three carries a number either. "More engaging" and "more visually appealing" are product copy. [[Meta Delivery & Andromeda#MD-171|MD-171]]'s rule applies: find the population and the counterfactual before carrying a figure. Here there is no figure to carry.

## 3. Our accounts

Phoenix Truxx is where this lands hardest, because the surface Uncrop exists to fill is the surface the money is already arriving on.

Week of 9 to 15 October, instant-form basis: **$1,336.39, 95 opt-ins, $14.07 each**. Of those 95, **51 came from Facebook Reels**. Vertical, full-screen. Uncrop's stated job is "filling vertical, full-screen surfaces", so a majority of that week's opt-ins arrived on exactly the placement it reframes for.

What is running there is not disposable. The dump engine is a Spanish video, Chriss Spanish ad 1, **18 opt-ins at $12.13** in the campaign launched 9 October, and in its earlier run the same creative drove **57 leads and 37 of the month's 79 dump requests at $19.65**. On the static side, the 26 ft box image took **48 leads at $8.30 in September** against **9 at $15.63 in August**, and Box Truck static was last week's volume leader at **25 at $11.49**. Image Animation's job is to convert a static into a short video. Those statics won head to head against busy compositions, fear hooks and no-hero layouts. Animating a tested winner is a change to the thing that was tested.

Then there is the number that makes Uncrop concrete, and it is ours. On 12 August Eric rejected two thumbnails on a Phoenix trades card. Cause: a 452x330 photo slot against 1.99-wide source photos, so **31% of every truck was cropped away**. The client caught it in one look and said "show more of the bottom trucks". That is what a ratio change does to a composition built for a different ratio. Uncrop is a ratio change we do not perform and do not see.

Two more exposures, both specific.

**Compliance.** Phoenix already lost two ads to Meta's financial products policy on 8 October, the Hino tow and rollback after **$98.83 and 6 leads**, plus Box Truck Ad v1. Our two chiropractic accounts sit under Meta's health rules. An enhancement that alters an asset does so after our compliance gate ran, which means the ad that served is not the ad that passed. MD-139's trigger list makes that a habit problem rather than an audit problem, because anyone with access can re-arm it by opening a preview.

**The clean window.** SJR has **seven Telluride hook ads at 9:16, client-approved 13 October**, and **seven more built today, five Portuguese and two Spanish**, sitting in Drive for Eric. None of the fourteen is live. Reading `degrees_of_freedom_spec` before launch costs nothing, and pre-launch is the only point where no buyer has seen the altered version yet.

## 4. The decision rule

**A capability's default is a separate fact from what it does, so read the default off a live ad before you treat a platform feature as dormant, and re-read it after any touch.**

## 5. Quiz

**1.** MD-182 and MD-183 are both tier 1 from the same Meta changelog. One is safe to leave alone and one is not. Why, in one sentence each?

**2.** Someone argues the three June enhancements are probably off by default, because Meta described them as opt-in. Name the two things on file that make that a bet rather than a conclusion.

**3.** You have fourteen SJR hook ads built and not yet live, all 9:16. Write the pre-launch check you would run, name the field you read, and say what you do with the answer in each of the two cases.

**4.** A media buyer unticks every enhancement on Phoenix's Spanish dump video on Monday. On Thursday the ad looks different in Reels. Nothing was edited. Give the most likely explanation, its tier, and what you would capture to move it off that tier.

**5.** Creative audience pairing is on, and one ad carries four assets with a persona on each plus a fifth persona on the ad itself. Which persona governs each asset, and what would make this structure attractive on our truck book against the ad-set split we run today?

Answers into `_answers-inbox.md`.

> [!note]- Answer key
>
> **1.** MD-182 is safe to leave alone because Meta states the default: `creative_audience_pairing` accepts 0 or 1 and omitting it leaves the feature off, so nothing changes until a person sets it. MD-183 is not safe to leave alone because the change notes never state a default at all, so leaving it alone is a decision made without knowing what it decides.
>
> **2.** First, MD-128: the nearest sibling in the same family, Flex Media, is tier 1 confirmed **on by default** and licenses Meta to recrop the creative, so the family precedent runs the other way. Second, MD-139: enhancement state is reported to re-arm after a duplicate, a text edit or even a preview, so "off by default" and "off right now on this ad" are different claims regardless. Being opt-in describes the control, not the starting position.
>
> **3.** Read `degrees_of_freedom_spec.creative_features_spec` on each ad and check `image_animation`, `video_filtering` and `video_uncrop`. If they are off, record the state with the date and the person who read it, so there is a baseline to compare against later. If any is on, switch it off before launch and say so in the build note, because a 9:16 hook has already been composed for 9:16 and the only thing Uncrop can do to it is undo that. Either way the check happens pre-launch, which is the one point where no buyer has seen the altered version yet.
>
> **4.** Most likely explanation is MD-139, enhancements re-arming on a touch that was not an edit, with a preview being the trigger nobody expects. That claim is **T3**: one operator, no screenshot of a toggle flipping, no before and after state capture, no count of affected ads. To move it up, capture the state rather than the symptom. Read the enhancement fields on Monday after unticking, record them, read them again Thursday, and keep both reads with timestamps plus the account activity log showing who opened the ad in between. Two matching captures across two accounts would make it T2.
>
> **5.** Each asset is governed by its own persona, because Meta publishes the precedence rule and the media asset's persona overrides the one set on the ad. The ad-level persona governs only the assets that carry none. It is attractive on the truck book because both the dealership work and the clinic work already run separate creative for separate buyer types split across ad sets, and pairing would let that split live inside one ad set, which matters against the 200 ad sets per campaign bound at [[Scaling Models#SC-179|SC-179]]. The honest caveat belongs in the same answer: Meta publishes no performance figure, no test and no rollout scope for pairing, so it is a capability and not yet an advantage.
