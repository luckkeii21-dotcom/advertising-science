---
title: "Lesson 015 - A Question Is Not a Gate"
type: lesson
lesson: 15
topic: Learning & Signal
source: harvest 2026-09-02 (LS-074, T3). Explicitly queued by the 2026-09-02 teacher pass as the item landing hardest on our own book. Paired with an audit of all eight Instant Form builds on file across four accounts, and four consecutive StayWell weekly reports.
created: 2026-09-03
updated: 2026-09-03
tags: [advertising-science, lesson, meta, lead-forms, optimisation-event]
---

# Lesson 015 · A Question Is Not a Gate

🎬 **Lesson video (2m 30s, silent, watch anywhere):** [[video/2026-09-03-lesson-015.mp4]]

> Lesson 010 asked what delivery learns from when it cannot learn from opt-ins. This one is the other end of the same wire: what delivery learns from when we hand it a population we already know is wrong.

**If you only answer two questions, answer Q3 and Q5.** Q3 is the one where our own account gives an answer that looks like proof and is not. Q5 is the guard that stops this lesson turning into a round of switch-flipping.

## 1. The mechanism

Meta optimises toward an event. On a Leads campaign that event is the form submit. Whoever submits is what Meta counts, and what Meta counts is the description of the person it goes looking for next.

Conditional logic changes who gets counted. Inside the Instant Form builder there is a setting called Conditional logic, and one of its actions is **Close form**. Meta's own definition: *"Considers the person as a non-lead and directs them to a custom end page. You won't receive the information for anyone who responds with an answer that closes the form."* A person routed there never appears in the Leads column, never lands in the CSV, never fires the webhook.

So the target silently narrows. Ben Heath's line, demonstrating it live in Ads Manager: *"None of these people that say they have less than 1K actually register as leads. Only the people that say they have 1K and above register as leads. So, in that instance, Meta is still just trying to get you leads, but who qualifies makes all the difference in the world."*

Picture a shop with a counter clicker at the door and a manager who buys advertising aimed at whoever the clicker counted. Someone wanders in, looks around, leaves. Click. The manager buys more of him. Now put a person at the door asking every visitor "are you here to buy something?" Nothing changes. The clicker still clicks. The question only matters when the answer decides whether the clicker clicks.

That is the whole idea. **Asking is free and does nothing. Routing is the lever.**

Two costs come attached, and both are real.

**You still pay for the people you screen out.** Meta bills the Leads objective on impressions. Someone who opens the form, answers wrong and gets closed out has already cost you the delivery. Meta says so on its own conditional-logic page: *"The use of conditional logic may increase your cost per lead."*

**You cannot see what you cut.** There is no Meta column, breakdown or export that reports how many people the form closed on. The number simply does not exist anywhere in Ads Manager.

## 2. The evidence

**LS-074, T3, active.** Heath building it in Ads Manager, dated 2026-09-01. The dateable part is not the build, it is the reversal: *"Previously, I have recommended go with more volume, don't have any conditional logic, reduce friction, get as many leads as possible. But I think we're now at a place where we're seeing so many poor quality leads come through with that setup... that we're by default switching more and more accounts to this setup."* Thirteen years and a stated $300 million of Meta spend, moving his default from low-friction to qualified.

**CR-096, T3, active, last touched 2026-08-21.** The same build was already in the codex three weeks before the reversal. LS-074 adds no new mechanism. What it adds is a named operator changing what he does by default, which is a different kind of evidence and a weaker one than a test.

**LS-008 is the spine underneath both.** Every lead event looks identical to the platform because none carries a financial commitment, so the raw lead event defines a population selected on willingness to type a name.

**LS-043 is the guard on reading the result.** The cheaper cost-per-opt-in side looks like the winner precisely when it is not.

Hold the tier honestly. T3 means a practitioner claim from real spend with no shown test. Heath publishes no before-and-after on opt-in volume, cost per opt-in, show rate or close rate, for either lever he recommends. The whole trade, fewer opt-ins for better ones, has no figure attached from anyone.

One tier note worth carrying. Meta's own statements here (the Close form definition, the cost-per-lead warning, and the builder's validation rule that a form will not save unless at least one path submits and one path closes) are platform documentation, so T1. They sit quoted in our own build notes and are not yet banked as a codex claim.

## 3. Our accounts

Eight Instant Form builds sit on file across four clients. **Seven of them contain zero mentions of conditional logic.** The one that specifies it in full is the Mattia build dated 2026-07-29, and Mattia was offboarded on 2026-07-24. It was written five days after the engagement ended, so it has never run.

Four of the seven ask a disqualifying question anyway.

**ChiroWorks invisa-RED** asks three: timeline, willingness to pay out of pocket, and geography with "No, that's too far for me" as an option. The routing lives in a reading key for the front desk. Priority A, Priority B, Deprioritize. Every one of those people is a lead in Ads Manager before anyone reads anything. The desk deprioritises after delivery has already learned.

**StayWell Form 06** asks "Our clinic is in Novi, Michigan. Can you travel to Novi, MI for your appointment?" with "No, I am too far away" sitting right there. It routes on none of it.

**SJR's dump and cargo-van forms** run More Volume and disqualify nobody, deliberately, and the dump form carries an explicit instruction never to drop the down-payment band.

Now the number that carries the lesson, and it is the opposite of the one you would expect.

**StayWell's geo question has come back yes 39 times out of 39.** Four consecutive reported weeks: 15 of 15 for Jul 31 to Aug 6, 10 of 10 for Aug 7 to 13, 6 of 6 for Aug 14 to 20, 8 of 8 for Aug 21 to 27. A perfect record.

And the same account has a documented geo leak. The June lead-data snapshot records a large share of "Not Interested" arriving from Pennsylvania, Georgia, North Carolina and far-Michigan, with our own note reading: *"The form's 'Can you visit Novi?' auto-answers yes, masking it."*

So a geo question with a 100% yes rate across 39 answers is not a gate, and it is not even a measurement. Wire Close form to it and it closes on nobody. The out-of-state people are answering yes.

The Mattia build had already solved that exact failure in writing, by putting the drive time inside the answer instead of leaving it abstract: "Yes, I'm about 20 minutes away", "Yes, I'd drive 30-45 min for it", "No, that's too far for me". A vague yes is free. A number makes the reader do the arithmetic on their own commute.

**And the wiring gets checked before the routing.** StayWell carries a second geo field, "How close are you to Novi, MI?", which has returned pain-duration answers for four consecutive weeks. Flagged 2026-08-06, again 08-13, again 08-20, again 08-27, unfixed in all four. Seven of the most recent respondents "answered" that distance question with "more than 3 years". Had Close form been wired to that field, we would have been blocking people from the clinic based on how long their knee had hurt.

*(Correction to our own filed reporting. `report-2026-08-27` calls it "a third week". Counting the flags in our own files it is the fourth, and both `_TIMELINE` and `_HOT` say fourth. The report body is the line that is wrong.)*

One more guard from our own rules. Our funnel says the form qualifies and captures contact, and the voice agent books. A Close form on a soft answer costs us a call the agent would otherwise have made. SJR's standing rule is to never disqualify on credit, and the down-payment question exists to inform the callback rather than to block it. Geography is permanent. Timing and budget are not.

## 4. The decision rule

**Close the form only on the one answer that makes a person unservable no matter what we do, and only after two weeks of routing that same answer to a submit-and-tag page, because Meta reports nothing about who you screened out.**

Two weeks of paying for leads you already know are wrong is a cheap price for knowing whether the answer you are about to block is 8% of your volume or 40%.

## 5. Quiz

Drop your answers in `_answers-inbox.md`. Partial answers get graded.

**Q1.** A form asks a qualifying question and a human reads the answers afterwards. Explain, in terms of what Meta counts, why that changes nothing about who the ads reach.

**Q2.** LS-074 is T3. Name the specific thing missing that would move it up a tier, and name two numbers Heath never published for the levers he recommends.

**Q3.** *(Application.)* StayWell's "Can you travel to Novi?" question has returned 39 yes answers out of 39 across four weeks, and the same account has out-of-state opt-ins on record from Pennsylvania, Georgia and North Carolina. You are told to switch on Close form for that question tomorrow. Say what would actually happen, and name the change that has to come first.

**Q4.** *(Application.)* ChiroWorks asks whether someone would be open to paying for a plan out of pocket, with answers Yes / Possibly, depending on the recommendation / No. Decide which of those three, if any, gets Close form. Justify it against our own funnel rule about what a form is for.

**Q5.** We turn on Close form for a geo answer on one ad set. Two weeks later cost per opt-in is up 34% and booked appointments are flat. Name the two readings that both fit those numbers, and name the one number that separates them.

> [!note]- Answer key
> **Q1.** Meta optimises toward the event, and on a Leads campaign the event fires on submit. A disqualified person who still submits is still counted as a conversion, so delivery keeps hill-climbing toward people who look like him. The human reading the answers is downstream of the count and cannot undo it. Only Close form changes the count, because it makes that person a non-lead who never enters the Leads column at all. Full marks name the event as the thing that defines the population, per LS-008.
>
> **Q2.** What is missing is a test: the same offer run with and without the gate in one account, read on cost per booked-and-showed rather than cost per opt-in. Two numbers he never published, any two of: opt-in volume before and after, cost per opt-in before and after, show rate before and after, close rate before and after. Naming the phone one-time-passcode lever as separately unmeasured earns credit too. T3 is a practitioner claim from real spend with no shown test, and a reversal by a credible operator is still a reversal rather than a result.
>
> **Q3.** **Almost nothing happens, because the question closes on nobody.** 39 of 39 said yes, including people who were in other states. Turning on Close form there buys no filtering and costs the Meta warning about a higher cost per lead for no return. **The change that has to come first is the wording of the answers.** Put the drive time inside the option, the way the Mattia build did: "about 20 minutes away", "I'd drive 30-45 min", "that's too far for me". An abstract yes is free to give. A number makes an out-of-state reader stop and do the arithmetic. Full marks also name the second problem: the account's other geo field has been crossed and returning pain-duration answers for four straight weeks, so the wiring gets fixed before any routing is switched on at all.
>
> **Q4.** **None of the three, and "No" is the trap.** Geography is permanent, so it can be blocked. Willingness to self-pay is a stated intention before anyone has heard a price, a recommendation, or a payment plan, which makes it exactly the kind of soft answer the call exists to move. Our funnel rule is that the form qualifies and captures contact while the voice agent does the persuading and the booking, so closing on "No" throws away a call we were going to make anyway and pays for the delivery regardless. It also mirrors SJR's standing rule about never disqualifying on credit. Accept a well-argued "Close form on No" only if it prices the trade explicitly and proposes measuring it first. It is the wrong default.
>
> **Q5.** Reading one: the gate is working, we are paying more per opt-in for better ones, and the booking flatness is a lag or a back-end problem. Reading two: the gate is cutting people who would have booked, and we have bought a more expensive version of the same result. **The number that separates them is booked-and-showed appointments per dollar spent**, compared against the same window before the change. Cost per opt-in cannot separate them and never could, which is LS-043 exactly: the cheaper side looks like the winner precisely when it is not. Naming show rate or cost per showed appointment gets full marks. Naming lead volume or cost per opt-in gets none.
