---
title: "Lesson 062 - The Switch Stays On Screen And Stops Governing"
type: lesson
lesson: 62
date: 2026-10-27
topic: Google PMax & Shopping
tags: [advertising-science, lesson, google-pmax]
---

# Lesson 062 - The Switch Stays On Screen And Stops Governing

No video today. Tuesday.

Topic: Google PMax & Shopping. Harvest-driven. Yesterday's research pass banked one claim, [[Google PMax & Shopping#GP-051|GP-051]], T1, dated and carrying a deadline 38 days out. Today's research pass banked nothing, so this is the claim on the table.

## 1. The mechanism

A setting can stop applying without changing.

That sentence sounds like a trick. It is the whole lesson, and Google published a working example of it on 21 October 2026.

Performance Max has a feature called image extraction. You give the campaign your landing pages. Google scans those pages for high-resolution images and uses what it finds as ad creative across Search, YouTube, Display, Discover, Gmail and Maps. You did not upload those images. You did not approve them as ads. They were on a web page, and the automation lifted them.

Until now there was a switch that held it off. At account level, Dynamic Image Extensions could be set to Off, and a PMax campaign that was never explicitly set either way inherited that Off. One switch, set once, governing everything new.

**From 4 December 2026 that inheritance ends.** Google's words: "Starting December 4, 2026, image extraction (`GENERATE_IMAGE_EXTRACTION`) will be enabled by default (`OPTED_IN`) for newly created Performance Max campaigns across Google Ads interfaces, including the the Google Ads API, Google Ads UI, and Google Ads Editor." And the sentence that matters more than the default: "Crucially, this new campaign-level default applies even if Dynamic Image Extensions are disabled at the account level (`isImageExtractionAdExtensionEnabled`). Previously, campaigns left unset inherited their status from this account-level setting."

Read the two halves separately, because they fail differently.

The first half is an automation turning on. We have seen that before and the codex is full of it.

The second half is new and it is worse. **The account switch does not move. It does not grey out. It does not warn you. It keeps reading Off, truthfully, about a scope that no longer includes your new campaigns.** Nobody gets a prompt, because from the campaign's point of view nothing was overridden. It simply stopped asking.

Existing campaigns keep whatever they have now. Only new ones are captured. So the way this reaches you is through ordinary work: you build a new campaign in January, or you rebuild one, and it ships with image extraction on while the account page still says Off.

The analogy. You put a sign on the front door of a building: no deliveries. For years every new tenant read the sign on their way in and followed it. Then the landlord quietly stops handing the sign to new tenants. The sign is still on the door. It is still accurate about the tenants who read it. Every tenant who moves in after that date takes deliveries, and you will not learn this by looking at the sign. You learn it by looking at who is carrying boxes.

Checking a control is not the same as checking that it still reaches anything. **The second question is "what inherits this", and almost nobody asks it.**

## 2. The evidence

[[Google PMax & Shopping#GP-051|GP-051]], **T1**. Google Ads Developer Blog, "Upcoming changes to image extraction in Performance Max campaigns starting December 4, 2026", 21 October 2026, read in full at source. This is the top tier: the platform stating its own future behaviour in its own words, with the field names and the date. A T1 like this can decide on its own.

Notice what GP-051 does **not** contain, because the tier covers the change and not its value. **No lift figure. No sample. No comparison of campaigns with extraction against campaigns without it.** Google published a default change and published no performance evidence for the default. So there is no evidence basis for leaving it on, and none for turning it off either. The decision gets made on creative control and image rights. Anyone who argues it on expected performance is arguing past the end of the evidence.

Two older claims make this a pattern rather than an incident.

[[Google Auction & Smart Bidding#GA-066|GA-066]], **T1 for the setting and its stated function, T3 for what it costs you**. Optimized Targeting is on by default and expands delivery past the audience you selected. The audience you chose is a starting point the system is licensed to leave.

[[Meta Delivery & Andromeda#MD-128|MD-128]], **T1 for the surface and the default state only**. Flex Media is an enhancement inside an ordinary image, video, carousel or collection ad, on by default since April 2026, licensing Meta to recrop and change your creative. Note the tier wording there too: the default state is documented, the performance effect is not, and no operator has shown data with it on against off.

Three platforms-worth of the same move. An automation ships on, and the control that used to hold it off quietly stops reaching it. GP-051 is the first one in the codex where the control is **orphaned** rather than withdrawn: on Meta in September 2026 four ad-set controls were taken away, which is visible because the fields vanish. Google's version leaves the field on screen.

Tier practice for today: **cite the tier of the half you are using.** GP-051's change is T1 and you can build on it. GP-051's performance consequence does not exist at any tier, so it cannot enter a recommendation at all.

## 3. Our accounts

Be straight about the exposure, because overstating it would be the easy move.

**We run zero live Performance Max campaigns today.** The only PMax in our history belongs to Mattia Spinal Care, Orlando FL, built to spec by us and pasted in by the client on 8 July 2026, running a roughly 12-mile presence-only ring around 32835. That account offboarded on 24 July 2026. Our own strategy document for it put PMax at priority 3 and listed it under "do not run" until 30 or more offline conversions a month fed back, on the grounds that health policy weakens its audience signals and junk leads arrive first. So the honest statement is that **4 December 2026 changes nothing on our book on the day it lands.** It is a rule for the next PMax campaign we build, whenever that is.

That rule is worth having early, for one reason: when we do build one, our landing pages are exactly the wrong pages to hand a scraper.

The pages we hand clients are pages we composite. StayWell's Binder landing page, the Mattia decompression funnel pages, the GoHighLevel relay pages: they carry client-supplied photography, licensed stock, and in places our own finished ad creative sitting as a page image. Google puts the legal burden on the advertiser in the same post: "confirm that you own all legal rights or permissions to the images published on your landing pages and allow Google to utilize them for commercial and advertising purposes."

For the clinics the sharper problem is not rights. **A photograph can be legitimate on a page and a policy violation in an ad.** We have the case on file. On 12 October 2026 five live ChiroWorks invisa-RED ads in ad set `52534730848975` were checked at the pixel level and found to be side-by-side before-and-after weight-loss composites, a named Meta ban. The copy on all five was clean. The images were the violation, and two of them carried partial nudity. An image-extraction automation does not know the difference between a page asset and an approved ad asset, and the account that pays for the distinction is the client's.

One more fact from the Mattia file, because it bears on any audit we run: that account had **a second unrelated Google Ads account contaminating its landing-page traffic data, IDs 24031060460 and 24031057880.** Check for shadow accounts before you trust any reading of a client's Google setup, including a reading of this setting.

Finally, the write trap, because it is the part that breaks accounts quietly. The field is `campaign.asset_automation_settings`. **It is a repeated field and an update replaces the whole array instead of merging into it.** Write an opt-out onto a live campaign naively and you silently clear every other entry in it, `TEXT_ASSET_AUTOMATION` included. Read the current array, add your opt-out to it, write the whole thing back. Google's own audit query reads the state:

```
SELECT campaign.id, campaign.name, campaign.asset_automation_settings
FROM campaign
WHERE campaign.advertising_channel_type = 'PERFORMANCE_MAX'
```

A campaign with no `GENERATE_IMAGE_EXTRACTION` entry in that array is inheriting from the account right now. That is the population the new default captures if those campaigns are ever recreated.

## 4. The decision rule

**Reading a setting is not proof it applies, so every automation control gets two questions: what is it set to, and what still inherits it. From 4 December 2026, any Performance Max campaign we create states its image-extraction status explicitly in the campaign, never by relying on the account switch.**

The general form is the one to carry: a control you set in the past is evidence about the past. Scope changes without touching the value.

## 5. Quiz

Drop your answers in `_answers-inbox.md` with the lesson number.

**Q1.** Dynamic Image Extensions is set to Off at the account level. On 15 December 2026 you create a new Performance Max campaign and touch nothing else. What is image extraction doing in that campaign, and what does the account-level switch read when you go and look at it?

**Q2.** GP-051 is T1. Name the specific thing the T1 covers, and name one thing in the same subject that GP-051 provides no evidence for at any tier.

**Q3.** A client asks you to turn image extraction off on their five live PMax campaigns. You write `asset_automation_settings` with `GENERATE_IMAGE_EXTRACTION` set to `OPTED_OUT` on each one. What have you just broken, and why?

**Q4.** Applied. A chiropractic client's landing page carries a patient photograph that has a signed release and has never been disapproved as a page image. Someone proposes that this makes the page safe for image extraction. Give the one-sentence reason that argument fails, and name the account and date in our own files that proves it.

**Q5.** Applied. You are asked for a recommendation: should we leave image extraction on or turn it off for a future PMax build, and what is the performance justification? Answer in two parts, and the second part is the point.

> [!note]- Answer key
> **A1.** Image extraction is **on** (`OPTED_IN`), because from 4 December 2026 that is the campaign-level default for newly created PMax campaigns and the campaign no longer inherits from the account. The account-level switch still reads **Off**, unchanged and un-greyed. Both facts are true at once, which is why this is a trap: the switch is accurate about a scope that no longer contains your new campaign. Full credit needs both halves. Saying "off, because the account says off" is the error the lesson exists to prevent.
>
> **A2.** T1 covers **the change itself**: the date, the new campaign-level default, the field names (`GENERATE_IMAGE_EXTRACTION`, `OPTED_IN`), and the fact that the campaign default applies even when the account-level `isImageExtractionAdExtensionEnabled` is disabled. All of it is Google stating its own behaviour in its own post. **No evidence at any tier**: the performance effect. No lift, no sample, no comparison of campaigns with extraction against campaigns without it. Also acceptable: there is no stated evidence on image quality, on which surfaces benefit, or on how extraction interacts with uploaded assets. Deduct if the answer treats T1 as blessing a recommendation to leave it on, because T1 on a default is not T1 on an outcome.
>
> **A3.** You have cleared every other entry in each campaign's automation settings, `TEXT_ASSET_AUTOMATION` first among them. `asset_automation_settings` is a **repeated field**, and an update replaces the entire array rather than merging into it. The correct sequence is read the current array, append the opt-out, write the whole array back. Five campaigns means five reads, not one blind write. Note that nothing errors and nothing warns, which is why this belongs in an answer key rather than in a post-mortem.
>
> **A4.** A release settles the rights question and does nothing about the platform-policy question: an image can be legitimate on a web page and a banned ad asset the moment it is served as an ad. The proof in our files is **ChiroWorks, 12 October 2026**: five live invisa-RED ads in ad set `52534730848975` were read at the pixel level and found to be before-and-after weight-loss composites, a named Meta ban, with fully compliant copy on every one. The copy was clean and the images were the violation. Two also carried partial nudity. Credit for naming the account and the date. Half credit for the right reasoning with no case attached, because an argument like this one needs an account behind it.
>
> **A5.** Part one, the recommendation: **turn it off, or rather state it explicitly as off in the campaign**, and the grounds are creative control and image rights, not performance. Google's own post puts the legal burden on the advertiser, our pages carry client photography, licensed stock and composited ad creative, and the clinic accounts have a live case where page-legitimate images are ad violations. Part two, and this is what is being graded: **there is no performance justification available in either direction.** Google published no lift figure, no sample and no comparison, so any number offered for or against would be invented. The correct answer says out loud that the performance question is unanswered and declines to fill it. An answer that invents a plausible-sounding performance rationale scores zero on part two no matter how good part one was.

Related: [[Google PMax & Shopping#GP-051|GP-051]], [[Google PMax & Shopping#GP-012|GP-012]], [[Google Auction & Smart Bidding#GA-066|GA-066]], [[Meta Delivery & Andromeda#MD-128|MD-128]].
