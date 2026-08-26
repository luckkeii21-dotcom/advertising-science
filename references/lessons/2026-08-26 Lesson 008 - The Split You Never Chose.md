---
title: "Lesson 008 - The Split You Never Chose"
type: lesson
lesson: 8
topic: Meta Delivery & Andromeda
source: harvest 2026-08-26 second pass (MD-019 thresholds, MD-133 new T2, MD-019b, MD-123)
created: 2026-08-26
updated: 2026-08-26
tags: [advertising-science, lesson, meta-delivery, attribution]
---

# Lesson 008 · The Split You Never Chose

🎬 **Lesson video (2m 40s, silent, watch anywhere):** [[video/2026-08-26-lesson-008.mp4]]

**If you only answer two questions, answer Q4 and Q5.** Seven lessons have gone out. The inbox has come back empty seven times. Two answers is a real submission.

This lesson has a twist in it. The codex has spent six research passes telling us to open one specific report. Today I went to write the instructions and found a reason it may not work on a single account we run. Both halves are in here, because the second half is the more useful lesson.

## 1. The mechanism

Every ad account spends money on three kinds of people.

**New:** never heard of the business. **Engaged:** visited the site, watched a video, filled something in, did not buy. **Existing:** already a customer.

You never chose that split. You chose a budget, a location and a creative. Meta chose the split, one auction at a time, and it does not ask.

Think about a shop that pays for flyers. The flyers are meant for strangers. But the person handing them out works the same street corner every day, and the regulars walk past that corner on the way in. Month after month, most of the flyers land in the hands of people who were already coming. Takings look fine. The shop is paying to be introduced to people it already knows.

There is a free report that shows you which hand the flyer landed in. Ads Manager, Breakdown, then Audience segments, sitting under By demographics next to age and region. Spend by segment. Add the frequency column and you also get how many times each group saw the ad.

Two things make this worth a lesson rather than a note. Most operators never open it. And until this week, nobody had published a number to compare the reading against, so opening it gave you a figure and no verdict.

## 2. The evidence

- **MD-019, T1, active.** Audience segments are a **reporting breakdown, not a delivery control**. This is settled on Meta's own documentation: "You can use audience segments to enable breakdown reporting." In the API it is `user_segment_key`, a breakdowns parameter on the insights endpoint. There is no matching field on the campaign object. Defining the segments costs nothing and buys a clean split. It buys **no** budget allocation.
- **MD-019b, T1, active.** There *was* a real control and Meta killed it. `existing_customer_budget_percentage` capped the share of budget that could reach existing customers. Meta's help centre now says it "is no longer available", and campaigns using it "will be paused" at Marketing API v26.0, which shipped **29 July 2026**. Any playbook that says "define your segments and Meta splits the budget for you" is describing a dead product.
- **The threshold, new on 2026-08-26, T3.** A rule of thumb from auditing, not a shown dataset. **Fashion: no more than 25 to 30% of spend to existing customers. Not fashion and not CPG: under 10%.** CPG is excluded and given no number, so do not assume it inherits the fashion band. The logic is repeat rate: a category people buy from monthly can afford existing-customer spend, one they buy from once cannot.
- **MD-133, T2, banked today.** Sam Piliero, breakdown open on screen: "Our engaged audience has spent **$161,000 out of the $317,000** in ad spend." New took $120,000, existing $34,000. Then the frequency column over 30 days: **new 2.9x, engaged 9.5x, existing 36x.** A tiny group of people saw the ads three dozen times each.
- **MD-123, T3, contested.** Exclusions bind, inclusions suggest. If you want to keep a group out, exclude them; adding an audience as targeting is a suggestion Meta routinely goes past. Match quality sets the leak: a pixel-event audience picks up roughly 60 to 70% of the people who did the event, so an exclusion built on one is porous by construction.

**Now the part that matters more than any of the above.**

I checked MD-133's fix figure against its own components and it does not survive. The codex banked "98% of the spend going to new customers" as the shown result of splitting prospecting from retargeting. His numbers, from the raw transcript: **$26,000 new, $7,000 engaged, $211 existing, $33.9k total.**

$26,000 of $33,900 is **77%**, not 98%. His 98% is new **plus** engaged, which is 97.3%. He says it himself one sentence earlier: "all of our spend is going to new and engaged."

So the fix eliminated the existing-customer leak, $211 out of $33,900, and left **engaged at 21% of prospecting spend**. Engaged was the headline problem. It was $161,000 of $317,000 on the first account. The celebrated fix barely touched it.

The claim is corrected in the codex today. Two smaller corrections went with it: the ROAS figures (10.37 blended, 8 new, 12 engaged, 14.69 existing) belong to his **second** account, not the leaking one, and that second account, the one he holds up as doing it right, runs **$8,000 of $46,000 on existing customers**. That is **17%**, and he calls it "very efficient". It fails the under-10% line from the paragraph above. Two operators on our own roster, no reconciliation.

## 3. Our accounts

**We have never opened this report on any account. Six research passes have named it as the highest-value unactioned item in the codex.** That is the honest state.

Here is why it has not happened, and it is not laziness.

**Blocker one: the instrument is documented for the wrong campaign type.** Read MD-019's own source text again. The help article says breakdown reporting "for your **sales campaign** reporting". The API parameter is described as "User segment (ex: new, existing) of **Advantage+ Shopping Campaigns (ASC)**."

Every account we run is **lead generation**. ChiroWorks, Chiropraise, Phoenix Truxx and SJR Commercial all run Instant Forms into a CRM. ChiroWorks has only ever sent Meta one signal, "a form was submitted". Nobody has checked whether the audience-segment breakdown populates on a lead campaign at all. It may return "all unknown". Six passes said "go open it" and the scope line saying it might be empty was sitting inside the claim the whole time.

**Blocker two: "existing customer" has no definition on our accounts.** The segment reads from custom audiences you attach under Advertising Settings. Existing customers means purchasers. Our clients have patients and buyers in a CRM, not a pixel purchase event. Until a customer list is uploaded and attached, the existing bucket is empty by construction and the report will read clean because it cannot see anything.

Related, and it is in the vault as an unshipped task: **no client of ours has a customer-list exclusion live.** ChiroWorks carries it as an open item with a warning attached, exclude CRM contacts from cold sets only and ship the warm reactivation layer in the same edit, or bookings go to zero.

**What we can read today, without any of that.** Frequency, which we already export.

SJR Commercial, 19 July to 17 August, from the last filed numbers: the **dump CBO at frequency 2.58** across 106 leads and $957.81, and **Box & Wreckers at 2.02** across 197 leads and $832.98.

Set those against Piliero's segment column. His new audiences ran **2.9x**. Ours are blended across every segment and still come in **below** his new-audience figure.

Be careful with what that buys. Frequency is impressions divided by reach, so a small existing-customer group getting hammered 36 times contributes very few impressions and barely moves a blended number. **A blended 2.58 bounds our reach mix, not our spend mix.** It says most of the people we reach are seeing ads about twice. It does not prove a small warm pool is not quietly absorbing real money. It is genuine evidence and it is weaker than it looks, which is the correct way to hold it.

One housekeeping fact worth knowing, because the codex has it wrong. **The codex names our accounts as "ChiroWorks, Chiropraise, Phoenix Truxx, SJR Commercial and Mattia".** Mattia was offboarded on 2026-07-24 and no creative ever ran under our management, and MetaTechAI came on 2026-08-22 and is not in the list. The roster sentence is stale in both directions.

## 4. The decision rule

**Before acting on a number from the codex, read the scope line of the source that produced it. Then open the audience-segment breakdown with the frequency column, confirm it is not reading "all unknown", and hold existing-customer spend under 10%.**

The order matters. Scope first, reading second, threshold third. Six passes did the third without the first.

## 5. Quiz

Drop answers in `lessons/_answers-inbox.md`. Lesson number plus your answers. Partial is fine and still gets graded.

1. Name the three audience segments, and say in one sentence what the audience-segment breakdown does and does not control.
2. Meta removed a real segment-level delivery control. Name it, say what it did, and give the date it stopped working.
3. Piliero's fix is quoted as "98% of the spend going to new customers." Show the arithmetic that breaks it, and say what the true new-customer share was.
4. **Applied.** You open the breakdown on ChiroWorks tomorrow and it reads 100% new audience, 0% engaged, 0% existing. Give two different explanations for that reading, and say which one you would check first and how.
5. **Applied.** SJR's dump CBO shows frequency 2.58 over 30 days. Piliero's existing-customer segment showed 36x. Someone concludes SJR therefore has no existing-customer spend problem. Say why that inference does not hold, and name the one report that would actually settle it.

> [!note]- Answer key
> **1.** New (never engaged with the business), engaged (interacted, did not buy), existing (already a customer). It controls nothing. It is a reporting breakdown only, settled at T1 on Meta's own documentation, and it reports spend and frequency by segment.
> **2.** `existing_customer_budget_percentage`, the existing customer budget cap. It set the maximum share of an ad set's budget that could be spent on existing customers. It stopped working at Marketing API **v26.0, 29 July 2026**, when Meta began pausing campaigns that used it. Full marks for adding that the only replacement is structural: two ad sets, include in one and exclude in the other.
> **3.** $26,000 new out of $33,900 total is **77%**. The 98% is new plus engaged ($26,000 + $7,000 = $33,000, so 97.3%), which is really "not existing". The engaged segment still took **21%** of prospecting spend after the fix, and engaged was the original problem at $161,000 of $317,000. Credit anyone who notes he says "all of our spend is going to new and engaged" one sentence before calling it new.
> **4.** Explanation A: the split is genuinely clean. Explanation B, far more likely: the segments were never defined under Advertising Settings, or the account has no purchase-based custom audience to define "existing" with, so the buckets are empty by construction and the report is reading nothing rather than reading zero. Also accept: it is a lead-gen campaign and the breakdown is documented for sales/ASC campaigns, so it may not populate at all. **Check B first**, by opening All Tools, Advertising Settings, Audience Segments and confirming an audience is actually attached to each bucket. A report that cannot see anything always looks perfect.
> **5.** Frequency is impressions divided by reach. A small existing-customer group seen 36 times contributes very few impressions, so it barely moves a blended average. A low blended frequency bounds the **reach** mix, not the **spend** mix, so it cannot rule out a small warm pool absorbing real budget. The report that settles it is the audience-segment breakdown showing **spend** by segment, with the caveat from Q4 that the segments must be defined first or it will read unknown. Extra credit for pointing out that 2.58 is a campaign-level blend and 2.9 was a single-segment figure, so the two were never directly comparable.

---

Related: [[2026-08-20 Lesson 004 - Controls Bind, Suggestions Don't]], which is the same asymmetry from the targeting side and explains why exclusions are the lever here. [[2026-08-18 Lesson 002 - The Attribution Column Is an Instrument]] on reading a number as the output of a model rather than as the truth. Laws 1b, 11d and 11e in the skill file.
