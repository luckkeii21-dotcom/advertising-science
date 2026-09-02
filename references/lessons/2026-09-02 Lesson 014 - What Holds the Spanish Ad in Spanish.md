---
title: "Lesson 014 - What Holds the Spanish Ad in Spanish"
type: lesson
lesson: 14
topic: Google Auction & Smart Bidding
source: harvest 2026-08-31 (GA-069, T1). Queued for teaching by the 2026-08-31 teacher pass, which locked its own topic minutes before this claim was banked. The 2026-09-01 teacher run did not execute, so this is the first pass since. Paired with an audit of every language-split campaign on our own book.
created: 2026-09-02
updated: 2026-09-02
tags: [advertising-science, lesson, google, targeting, language]
---

# Lesson 014 · What Holds the Spanish Ad in Spanish

🎬 **Lesson video (silent, watch anywhere):** [[video/2026-09-02-lesson-014.mp4]]

> Lesson 004 said controls bind and suggestions don't. This one is a control becoming a suggestion, stated by the platform, in writing, with a date on it. That has never happened before in this codex.

**If you only answer two questions, answer Q3 and Q5.** Q3 is the arithmetic that decides where a language control is worth anything. Q5 is the guard that stops this lesson turning into a panic in September.

## 1. The mechanism

Google's help page, read 31 August: "Starting in September 2026, the way language targeting works is changing for Search campaigns and the Search Network portion of Performance Max campaigns." Then the operative sentence: "The campaign-level language targeting setting will be removed. **Search ads will automatically match based on the language of your ads.**"

Two separate things happen. The setting disappears on Search. And language criteria already sitting on a campaign are not deleted, they stay there and stop working. A campaign can therefore look correctly configured and be doing nothing.

Performance Max splits down the middle. It keeps the campaign-level language setting for YouTube, Display, Discover and Gmail. It loses it for the Search Network portion only. One campaign, two behaviours, divided by its own channel list.

Think of a doorman and a doorplate. Today there is a doorman on the Spanish room checking everyone who walks up. From September the doorman leaves and a plate on the door says SPANISH. Nearly everyone reads the plate and walks past.

The question is not whether the plate works. It mostly does. The question is what the doorman was catching that the plate will not.

Under a doorman the wrong-language share is zero by construction. Under a plate it is whatever the plate leaves. That leftover has a name worth learning, because everything in this lesson turns on it: the **residual**.

## 2. The evidence

**GA-069, T1**, off Google's own help documentation, banked 31 August. It is T1 because the platform states the change about itself and dates it. Two read-quality notes travel with it, and say them out loud when you quote it: the Google Ads Developer Blog post body failed to render on two separate fetches, so the substance comes from the help centre page plus trade coverage, and one API detail (that adding language criteria to a Search campaign will throw `ContextError.OPERATION_NOT_PERMITTED_FOR_CONTEXT`) is recorded as reported and unverified.

**Law 1a, MD-001 family, T3.** Meta's ad set has a controls section and a suggestions section. Location, minimum age, language and exclusions bind. Interests, lookalikes and custom audiences suggest by default, and bind on request through a documented toggle (MD-013). That whole law is read off the interface by operators. Nobody at Meta has published it.

**GA-066, T1.** Google runs the same architecture under a different name. Optimized Targeting is on by default and, in Google's own panel text, "expands your reach outside of the specific audience that you've selected."

**GP-042, T3.** PMax's new-customer setting loses to the conversion action, so the campaign skews warm regardless of the toggle.

Four claims, one architecture. Here is what the tiers buy you. GA-069 is the only one where a platform states the change about itself with a date, so it is the only one you can put on a calendar. MD-001 is T3, so it tells you what experienced operators see on screen, and it can be wrong in a way GA-069 cannot. Neither of them tells you what your own account does. T1 says what the platform says. Only the account says what the account does.

## 3. Our accounts

The honest part first. **No client of ours has a live Google campaign today.** Mattia Spinal Care was the only Google account we ever ran, and it was offboarded on 24 July. The campaigns were left running untouched with a shutdown set for 16 August. Nothing in the vault records that shutdown happening, so the correct status is unverified rather than closed. MetaTechAI carries "scope Google Search" as a queued item, not a live one. The 31 August log says Mattia "runs Performance Max English-only" in the present tense. That is a spec on a shelf, not a running campaign.

The spec is still worth reading, because it is exactly the shape GA-069 acts on. The 8 July PMax build sets **Languages: English only**, with the note "Spanish copy built + held for Phase 2." The Spanish asset groups are written, character-verified and switched off. **The setting is the only thing holding them out.** From September, on the Search half of that campaign, it would stop being the thing holding them out while still holding them out on YouTube, Display, Discover and Gmail.

That same file contradicts itself. The settings table says English only. Pre-flight checklist item 9 says "Languages = English + Spanish." Both in one document. It survived review because the campaign never ran under our management.

And on the same account we had already reached the September position two months early, for a different reason. The Spanish Search campaign, G2, was specified as **"Language targeting: ALL languages (Spanish-dominant users often run English interfaces); Spanish keywords do the selection."** We decided the setting was the wrong instrument and handed the job to the words.

Now the number that actually teaches this, and it is on Meta.

**SJR Commercial, 7 to 21 June.** Two programs, two languages, CBO, open and broad. No language control anywhere in the structure. The creative did all the sorting:

- **Dump trucks: 237 of 238 profiled leads were Spanish.** 99.58%. Residual: 1 lead, 0.42%.
- **Cargo vans: 138 of 147 profiled leads were English.** 93.88%. Residual: 9 leads, 6.12%.

Meta pushed 86% of van budget into English by itself, because English ran $2.88 per lead against $8.70 Spanish, a 3.02x gap.

So the September regime is not a forecast. We have already run it. Creative sorted language at 99.58% on one program and 93.88% on the other, with no setting doing any work at all. **What a control buys is not the average. It is the residual. And the residual was fourteen times larger on the program where the sort was harder.**

⚠ **One correction, caught while reading those rows.** `report-2026-06-21.md` and the June Performance Thesis both state the van split as "163 English vs 9 Spanish (95% English)". 163 plus 9 is 172, which is every van form lead, but only 147 van leads were profiled. The internally consistent pair is **138 and 9**, which is what `_TIMELINE.md` already carries, and it checks three ways: 237 plus 9 is the 246 Spanish leads as filed, 385 minus 246 leaves 139 English, and taking out the single English dump lead leaves 138. The conclusion survives. The English share falls from 94.77% to 93.88%. The number in two filed documents does not survive.

## 4. The decision rule

**When a platform converts a control into an inference, the average barely moves and the guarantee disappears, so price the residual and not the average.**

On our book that cashes out as one question. Before putting a second language inside a campaign, ask what in the ad itself keeps the wrong reader out, and accept that the honest answer is a percentage rather than a zero.

## 5. Quiz

Drop your answers in `_answers-inbox.md`. Partial answers get graded.

**Q1.** From September 2026, Google removes campaign-level language targeting. Name the two campaign types affected, and name the part of Performance Max where the setting survives.

**Q2.** A campaign has Spanish language criteria set on it today. In October, what is the state of those criteria, and why is that worse than Google deleting them outright?

**Q3.** *(Application.)* SJR's dump program sorted 237 of 238 leads into Spanish with no language setting. The van program sorted 138 of 147 into English. You are handed a language control and you can apply it to exactly one of the two programs. Which one, and what is the number you use to argue it?

**Q4.** *(Application.)* Suppose Mattia's PMax had stayed live and you were told to switch on the held Spanish asset groups in October. The build spec's settings table says English only and its pre-flight checklist says English plus Spanish. Explain what each of those two lines would actually do to that campaign in October, channel by channel.

**Q5.** Name the wrong action someone takes in September because they read this lesson, and say what number would have stopped them.

> [!note]- Answer key
> **Q1.** Search campaigns and the Search Network portion of Performance Max. AI Max for Search loses it outright alongside Search. The setting survives inside PMax for **YouTube, Display, Discover and Gmail**, so one PMax campaign runs split behaviour across its own channels.
>
> **Q2.** The criteria stay on the campaign and stop affecting targeting. That is worse than deletion because the campaign still reads as correctly configured. A deleted field makes somebody ask what replaced it. A dead field that looks alive does not, so the account can be audited, passed, and be doing nothing.
>
> **Q3.** **Cargo vans.** The argument is the residual, not the sort rate. Dump already sorts itself at 99.58%, so a control there buys back **1 lead in 238, 0.42%**. Vans sort at 93.88%, so a control buys back **9 leads in 147, 6.12%**, roughly fourteen times as much. A second and stronger argument sits on the same rows: Spanish van leads ran **$8.70 against $2.88** English, so those 9 are not merely off-language, they are the expensive ones, and Meta was already routing 86% of van budget away from them without being told to. Answering "dump, because Spanish is the dump engine" reads the average instead of the residual, and that is the mistake this lesson exists to prevent.
>
> **Q4.** Neither line does one clean thing any more. **"English only"** would still hold the Spanish asset groups out of YouTube, Display, Discover and Gmail, and would stop holding them out of Search. **"English + Spanish"** would open every channel, and on Search it would be redundant, because Search is already matching on the language of the ad itself. So the two contradictory lines converge on Search and stay opposite everywhere else, and the real decision moves to whether the Spanish creative and the Spanish landing page are strong enough to do the sorting on Search alone. Full marks also require naming that the campaign is offboarded and its shutdown is unverified, so the first move is checking whether it is running at all.
>
> **Q5.** The wrong action is tearing language-split campaigns apart in a panic, or refusing to run two languages in one account at all. The number that stops it is **99.58% and 93.88%**: our own account already ran with no language control and the creative sorted almost perfectly. The change costs a guarantee, not a program. The equal and opposite error is assuming the residual is zero because the average is high. It was 6.12% on vans, and 6.12% of a real budget is real money going to leads that cost 3.02x more.
