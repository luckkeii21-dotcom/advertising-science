---
title: "Lesson 033 - The File Cannot Count You Twice"
type: lesson
lesson: 33
date: 2026-09-22
topic: Attribution & Incrementality
claims: [AT-120, AT-121, AT-002, MD-162, MM-211, LS-019]
video: none
tags: [advertising-science, lesson, attribution, incrementality, new-to-brand, crm]
---

# Lesson 033 · The File Cannot Count You Twice

An independent measurement vendor ran geo test-versus-control across 10,000+ campaigns and 200+ North American advertisers last year and found that 64% of Meta's incremental conversions come from buyers who were new to the brand. It landed in our codex on 2026-09-20 as [[Attribution & Incrementality#AT-120|AT-120]].

The obvious next question is what our number is.

So I went and got it. Our file says 99.94%. That answer is false, and how it got to be false is worth more than the number.

## 1. The mechanism

Two ways to keep a list of the people who come through the door.

First way, a visitor's book. Everyone signs on the way in. Come back in March, sign again. By December the book has your name three times, and counting names tells you how many visits happened.

Second way, a membership file. First visit, you get a card. Come back in March and nothing is added. The clerk pulls your card, updates your address, puts it back. By December the file has your name once. Counting names tells you how many people exist. It tells you nothing about how many times they came.

Every account we run keeps the second kind. Form submissions land in GoHighLevel, and GoHighLevel matches an incoming submission against the contacts it already holds. Same email, same card. The created date on that card never moves.

So the created date answers "when did this person first appear". It does not answer "when did this person opt in". A person who fills the form twice shows up once, dated the first time. The second opt-in happened, we paid for it, and the file has no row for it.

That is the whole mechanism. Now watch what it does to a rate.

## 2. The evidence

**[[Attribution & Incrementality#AT-120|AT-120]], T2.** Measured, an incrementality vendor, on 200+ North American advertisers and 10,000+ campaigns in 2025, geo-based test versus control. Three published figures: 64% of Meta's incremental conversions are new-to-brand, 2.3x higher incremental ROAS than search on new-customer acquisition, 46% better efficiency for brands at $50M+ in media.

Read the caveats before you like it. We read Meta's summary, not the study. Meta chose which three numbers to publish and Meta is the party the study flatters. The comparison arm is "search", undefined. The 46% is scoped to $50M+ advertisers, which is nobody in our book.

One more, and it is the habit this claim is worth teaching for. **Meta's own part 1 attaches the 64% figure to footnote 3, the Kantar consumer survey. Footnote 4 is the Measured study, defined in the same list and then never cited in the body.** Part 3 attributes it correctly. So the platform cites the wrong study for its own headline incrementality number on one of three pages. Read which footnote the sentence actually points at. Do not trust the numbering.

**[[Attribution & Incrementality#AT-002|AT-002]], T2.** The Haus work, and the reason a geo test counts for anything here. It is the only method this file treats as settling a causal question.

**[[Meta Delivery & Andromeda#MD-162|MD-162]], T2.** From the same harvest. Four Meta-published product deltas, four different experiment designs, ranging from a 10,107-campaign global test to a 12-study meta-analysis three years stale. A deck that lists all four as "Meta data" flattens a real range.

**[[Marketing Math & Unit Economics#MM-211|MM-211]], T2.** Precedent from our own book. A field that exists and never gets written turns an outcome rate into a guess.

Tier discipline. T2 is the strongest tier we hold outside our own tests, and AT-120 is a well-designed prior. It is not a result about us. It cannot go in a client report as our number.

## 3. Our accounts

**SJR Commercial.** The CRM export `Clients/SJRC/_ghl_contacts_slim.csv`. 20,751 contacts, 7 January 2025 to 7 June 2026, 516 days. Meta 14,515 of them, 69.95% of the file. TikTok 2,128, SWA 2,517, Renters Remorse 1,126.

The test: for every Meta contact, was that phone number or email address already in the file on an earlier date?

- All 14,515 Meta contacts: **8 were already known. 0.06%.**
- 2026 only, 1 January to 7 June, 5,725 Meta contacts: **4 were already known. 0.07%.**

Read as a new-to-brand rate, that is 99.94%, against AT-120's 64% across 200 advertisers, on a dealership that has run paid ads into the same New Jersey trades catchment for seventeen months. It is not a finding. It is the dedup key.

**Here is the proof, and it is the best part.** The file holds 20,689 distinct phone numbers. Exactly ten phone numbers appear twice. **All ten differ on the email address.** Three of the ten differ by a typo:

- `mt3546@drexel.edu` and `mt3546@drxel.edu`
- `kennethuni1165@hotmail.com` and `kennethuni1165@hotmail.conm`
- `davidschwartz09121955@gmail.com` and `davidschwartz091210955@gmail.com`

Those people came back and got counted twice only because they mistyped. Everyone who typed their address the same way the second time was merged into the record they already had. The instrument does not have a repeat rate near zero. It has a repeat rate it cannot see.

One of the ten is an internal test record and is excluded. The nine real pairs sit **1, 62, 65, 101, 107, 123, 125, 202 and 248 days apart, median 107 days.** Repeats happen, and they happen three to four months later, which is exactly the window where a dealership is paying to reach the same person again.

**Phoenix Truxx.** Same test on `Clients/Phoenix Truxx/Leads Data/`, 935 contacts created 19 February to 24 April 2026. **906 phone numbers across 906 rows that carry one. Zero repeats. 901 email addresses across 901 rows. Zero repeats.** Not one duplicate anywhere in the file. Same mechanism, and cleaner, because a 65-day window gives almost nothing time to come back.

The counter-signal is in the same file. **36.83% of Phoenix contacts carry a last-activity timestamp at least a day after they were created, 18.52% at least a week, 9.21% at least thirty days.** That is the record being touched long after it was made. It is not evidence the person came back, because our own outbound SMS and the voice agent write to that field too. It is evidence that these rows get updated in place, which is the behaviour that eats the second opt-in.

**So across five accounts we can produce the new-to-brand split on none of them,** and the one file that looks like it answers returns 99.94% by construction. Banked as [[Attribution & Incrementality#AT-121|AT-121]], T2, measured on our own exports.

Three fixes, cheapest first.

1. **Free, today.** Stop reading a created date as an opt-in date anywhere. It is a first-seen date. Every rate built on it counts people and gets called events.
2. **Cheap.** Put Meta's own reported opt-in count for a window beside the count of CRM rows created in that window. Meta counts form submissions and does not merge them. **The gap is the collapsed repeats.** SJR's day-level Meta results for 1 January to 31 May 2026 is already a carried open item from lesson 032. This is the second thing that one pull unlocks.
3. **The real fix.** Have the automation write a timestamped note or increment a counter on every submission, so the second opt-in lands somewhere even when the contact is merged.

Worth knowing what else this blocks. [[Learning & Signal#LS-019|LS-019]] puts the floor for a lookalike seed at 100 people. A file that cannot identify a repeat buyer cannot build a repeat-buyer seed, and it cannot build the exclusion audience either.

## 4. The decision rule

**Before you quote or chase any rate about repeat behaviour, check whether the instrument can record a repeat at all. A file that merges on the email address counts people and never events, so a 99% new rate off that file is a setting, not a measurement.**

## 5. Quiz

Drop your answers in `_answers-inbox.md`. Lesson number plus answers is enough. Partial is fine.

**1.** AT-120 sits at T2. Name the two things about how it was produced that earn it T2, and the one thing about how we got hold of it that stops it being T1.

**2.** SJR's file returns 99.94% net-new across 14,515 Meta contacts. Exactly ten phone numbers appear twice and all ten differ on the email address. In two sentences, say what those ten records are and why they are the proof rather than the exception.

**3.** Kartik wants "96% of our opt-ins are brand new customers" in the SJR monthly report, sourced from this export. Write the two sentences you say back to him.

**4.** You now hold Meta's reported opt-in count for SJR for March 2026 and a count of CRM rows created in March 2026, and Meta's number is higher. Name three things that could cause that gap. Say which one you rule out first and how.

**5.** ChiroWorks asks for a lookalike audience built off past patients, and LS-019 sets the seed floor at 100 people. Say what this lesson changes about that request, and name the one thing you check before you quote a seed size.

> [!note]- Answer key
> **1.** It earns T2 on the design and the scale: geo-based test versus control, which is the only method [[Attribution & Incrementality#AT-002|AT-002]] and this file treat as causal, run across 10,000+ campaigns and 200+ advertisers rather than one account. What stops it being T1 is that we read **Meta's summary of the study and not the study**, and Meta selected which three of its findings to print. Meta's own part 1 then hangs the 64% on the wrong footnote, which is the tell that the summary was assembled loosely.
>
> **2.** They are nine people who opted in a second time plus one internal test record, and the nine survived only because the email address on the second submission did not match the first, three of them purely from a typo. They are the proof because if the file genuinely held almost no repeats you would not expect typo-pairs at all; their existence shows repeats are happening and the merge is eating every one where the address matched.
>
> **3.** Something like: "That number is 99.94% and it comes out of the dedup rule, not out of the market. GoHighLevel merges a second opt-in into the existing contact when the email matches, so the file counts people once and cannot see a repeat at all, and the only ten repeats in seventeen months got through on typos. If we want a real figure it is one pull: Meta's reported opt-ins for the month against CRM rows created in the month, and the gap is the answer."
>
> **4.** Three causes. **One, collapsed repeats**, which is the one this lesson is about. **Two, opt-ins that never reached the CRM**, a webhook or automation failure between the form and GoHighLevel. **Three, a counting mismatch in Meta's own column**, which lesson 029 already found on this exact account: the Results column was printing four different units, so "opt-ins" may not all be opt-ins. **Rule out three first**, because it is free and it is a known defect on SJR: pull Result indicator grouped against Results for the same window and confirm every row counts the same event before you interpret a single unit of the gap.
>
> **5.** It changes the seed, not the floor. The request assumes we can identify past patients as a group, and the CRM cannot separate a person who came once from a person who came back, so "past patients" is not a field we hold. The thing to check before quoting any seed size is **whether the source list is built from an event or from a contact record**: a list of contacts will silently be a list of first appearances, and on ChiroWorks nothing has ever been marked showed or no-show ([[Marketing Math & Unit Economics#MM-211|MM-211]]), so the patient half of the seed does not exist yet either.
>
> **Carry forward.** We have measured that the instrument is blind. We have not measured how big the blindness is, and that costs one pull: Meta's reported opt-ins for a month beside CRM rows created in that month, on SJR first because it has the longest history. Until that runs, treat every "new customer" share on our book as unmeasured rather than as high.
