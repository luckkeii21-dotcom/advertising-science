---
title: "Lesson 069 - The Rule Was Written Before The Campaign Existed"
type: lesson
lesson: 69
date: 2026-11-03
topic: Learning & Signal
claims: [LS-091, MD-063, LS-048, LS-055, SC-001]
tags: [advertising-science, lesson, learning-signal, automated-rules, shared-account, measurement]
---

# Lesson 069 · The Rule Was Written Before The Campaign Existed

Topic: Learning & Signal. Harvest-driven, so the rotation pointer holds at 4. This morning's research pass banked [[Learning & Signal#LS-091|LS-091]] off a rule collision shown on screen. It is a T3 claim from one operator on one account, and it still reaches the SJR ad account harder than almost anything we have banked this month, because of a fact about that account we verified ourselves in September. No video today, Tuesday.

## 1. The mechanism

An operator built a new engagement campaign and set it a cap of 1,000,000 impressions. Sensible. He then opened his automated rules list and found one he had written earlier:

> turns off ads when campaign names contain **IG** and impressions exceed **250,000**

His new campaign had IG in its name. So the old rule owned it from the moment it was created. His words:

> "My old rule hits any campaign with IG in the name. The campaign has IG in the name, so my million impressions cap would have never fired. No ad would have ever reached that threshold."

Here is the part worth slowing down on. A rule scoped to a name fragment is not a rule about a campaign. It is a **standing order about a string**. You wrote it once, against the campaigns that existed that day, and then it sat there waiting. Every campaign you build afterwards gets read by it on creation and gets governed by it without ever being named in it.

The analogy that maps: a building manager puts a sign on the third floor saying *all doors on this corridor lock at 6pm*. Two years later someone builds four new offices on that corridor. Nobody told the sign. The sign was never about those offices and it governs them anyway, and the people inside them keep discovering at 6pm that a decision was made for them before they moved in.

**Now the expensive half, and it is not the delivery failure.** If the rule had killed the campaign outright, you would notice in a day. It does not. It lets the campaign run and quietly moves where it stops. Every post in that campaign halts at 250,000 impressions. Every post's cost per outcome is therefore computed over an impression volume nobody chose. And critically, **the comparison stays internally consistent**: all your posts got the same unchosen amount, so the ranking between them still looks clean, the chart still has a winner, and nothing on screen is wrong.

> "Most people would find that out a month later, wondering why every post dies at the same number and why Facebook never spends on full on anything."

A measurement failure that preserves internal consistency is the worst kind we have. It does not produce a bad number. It produces a confident one.

**Second detail from the same sequence, and it bounds every cap you will ever set.** Rules are evaluated on a schedule, roughly every 30 to 60 minutes. The claim is explicit that this is asserted rather than documented:

> "It's never going to stop it immediately. It checks it periodically and anytime something passes it, it gets cut."

So an impression cap is an approximate ceiling plus whatever the ad delivers between two checks. Two ads under the same cap did not receive the same impressions, and the gap between them is set by delivery speed, which is the thing you were trying to measure.

## 2. The evidence

- **[[Learning & Signal#LS-091|LS-091]], T3, active.** One operator, one account, no test. The rule text and the collision are **shown on screen**, so the collision itself is not in question. The 30-to-60-minute evaluation cadence is **asserted only** and was not checked against Meta documentation. Whether that interval varies by account is unknown.
- **The mechanism is stronger than its tier.** This is the rare case where a T3 behaves like a T1 for one half of the claim. A condition that reads "campaign name contains X" *must* match any campaign satisfying it, now or later. That is what a name-matching rule is. You do not need a test to believe it, and that half can decide. The cadence figure cannot; treat it as a named bet.
- **[[Meta Delivery & Andromeda#MD-063|MD-063]], T3.** The same shape, found two months earlier in a different corner: account-level automated rules switch Advantage+ creative enhancements back on over time, so turning them off ad by ad is "both tedious and insufficient". Two independent observations of one principle. **A rule set once keeps acting on things created after it.**
- **[[Learning & Signal#LS-048|LS-048]], T3.** The sibling failure, and keep them apart. LS-048 governs the **window** a rule reads over, where the failure is a stale average scaling a decayed campaign. LS-091 governs the **scope** a rule applies to. An account can get both wrong independently, and the same rule can be correctly windowed and promiscuously scoped at once.
- **[[Learning & Signal#LS-055|LS-055]], T3.** The only method on file for calling a winner, a significance calculator at 90%. LS-091 is upstream of it. If both ads were truncated at a number nobody chose, the calculator is being fed a sample that was decided for you, and it will return a clean verdict on it.
- **[[Scaling Models#SC-001|SC-001]]** holds the step size and cadence of a rule, which is where cadence belongs. LS-091 only bounds what a cap can promise.

Tiers, said plainly: the scope behaviour decides. The cadence number is a bet. Nothing here is T1 and nothing here needed to be.

## 3. Our accounts

**SJR Commercial is the exposed one, and the reason is a fact we verified ourselves on 23 September.**

The account `act_1066566104034369` ("Sansone NEW") is not our account. It is a **shared ad account carrying 166 campaigns across multiple dealership brands**, run by different MetaTechAI pods at the same time. We confirmed that live in Ads Manager while building the September report.

Two things follow, and the second has no precedent anywhere else on our book.

**One.** The bare `MetaTechAI` prefix sits on campaigns that are not ours. Confirmed live: `MetaTechAI | (NEW) 26ft Box & International Wreckers | CBO | 29th August 2026 | Windsor Nissan | Relaunch - 22nd Sep 2026` carries it and belongs to Windsor Nissan. That is why our reporting filter is `contains Sjr-commercial` **or** `contains EvrythingAI`, never bare `MetaTechAI`. We already learned that a name fragment in this account over-matches. We learned it in the reporting lane and fixed it there.

**Two, and this is the new part.** Automated rules in that account are account-scoped. If any pod on those 166 campaigns ever wrote a rule against a name fragment, it governs our two campaigns. Our live names are:

- `MetaTechAI | Dump Trucks | Testing | CBO | 12-06-2026 | Sjr-commercial Dealership`
- `MetaTechAI Winning CARGO Vans Campaign | CBO | 21-05-2026 | EvrythingAI`

Both contain `MetaTechAI`. Both contain `CBO`. Both carry a date string. Any of those is a plausible fragment for somebody else's rule. The symmetry is real too: a rule **we** wrote on `MetaTechAI` would govern Windsor Nissan's box truck campaign and a separate team's `ADV - 66 Mitsu New Car`.

**Phoenix Truxx is the clean contrast, and it is clean for a structural reason rather than a lucky one.** It runs its own account with a small campaign count, four at the ceiling per the 9 October structure audit, each needing roughly three leads a day to function. Same naming discipline, no shared surface, so a name-scoped rule there can only capture campaigns we built. That is the whole difference, and it means exposure to LS-091 is a property of **account tenancy**, not of naming discipline. Our naming is good on both accounts. Only one of them is ours alone.

**The honest state of what we know, and it is the real finding of this lesson.** I searched every client note and every concept note in the vault for "automated rule". **Zero hits.** We have no record of a single automated rule on any account we manage. That is not a record that there are none. It is the absence of a record either way, on a shared account where other people can write them. Nobody has opened the rules list on `act_1066566104034369` and read it.

StayWell, Mattia and the clinic lane: nothing to report, and that is a real nothing rather than an unchecked one, since none of them shares an ad account.

## 4. The decision rule

**Read the account's rule list before you create a campaign, and scope every rule you write to the entity rather than to a name fragment wherever the UI allows it. On a shared ad account, read the rule list before you trust any number the account produces.**

The second clause is the one that is new today. On an account you own alone, a bad rule is your bad rule and you can find it by remembering. On a shared account, a cap you never set can be truncating your sample while your comparison stays internally consistent.

And treat every cap as approximate. Never compare two ads on the assumption they received the same impressions.

## 5. Quiz

Answers go in `_answers-inbox.md`.

**Q1.** State LS-091's tier. Then split the claim into the part that can decide on its own and the part that is a named bet, and say what makes the first part strong despite the tier.

**Q2.** LS-091 is called a measurement failure before it is a delivery failure. Explain why that ordering makes it more expensive, and name the specific property of the truncated data that keeps anything from looking wrong.

**Q3.** Applied. You are about to build a fifth campaign in the SJR shared account and you name it `MetaTechAI | Rollbacks | Testing | CBO | 03-11-2026 | Sjr-commercial Dealership`. List every fragment in that name another pod could plausibly have written a rule against, say what you do before you hit publish, and say what you do if the rules list turns out to be empty.

**Q4.** Applied. A teammate says our naming convention is the problem and we should drop the shared tags. Say what you send back. Name the one account property that actually creates the exposure, and say what we would lose in the reporting lane if we dropped the tags.

**Q5.** Applied. Two ads in one ad set, same cap, and the significance calculator from LS-055 says Ad A beat Ad B at 94%. Name the two separate things in this lesson that could make that verdict meaningless, say which of them LS-048 would NOT catch, and say what you check first.

> [!note]- Answer key
>
> **A1.** **T3**, one operator, one account, no test. **The part that decides on its own: the scope behaviour.** A condition reading "campaign name contains X" must match any campaign satisfying it, including ones created after the rule. That is definitional rather than empirical, and the rule text plus the collision were shown on screen. **The named bet: the 30-to-60-minute evaluation cadence.** It is asserted, never verified against Meta documentation, and whether the interval varies by account is unknown. Full marks for noting that a T3 is normally a named bet in full, and that this one splits because half of it is what a name-matching rule logically must do.
>
> **A2.** A delivery failure announces itself. The campaign stops, or spend collapses, and you look. A measurement failure leaves the campaign running and moves **where it stops**. Every post halts at the same unchosen impression count, so every cost per outcome is computed over a volume nobody selected. The specific property is **internal consistency**: because all the posts received the same truncated amount, the comparison between them is still fair, the ranking still resolves, and the chart still produces a winner. Nothing looks broken because nothing is inconsistent. The operator's own estimate is that this surfaces about a month later. Credit for the general form: a wrong number that is self-consistent is worse than one that is obviously wrong, because it gets acted on.
>
> **A3.** Plausible fragments another pod could have scoped a rule to: **`MetaTechAI`** (on all 166 campaigns, including Windsor Nissan's and the `ADV -` team's), **`CBO`**, **`Testing`**, **`Sjr-commercial`**, **`Dealership`**, **`Rollbacks`**, and the **date string** `03-11-2026` or any partial of it. Before publishing: open the account's automated rules list and read every rule, checking which conditions this name satisfies. If the list is empty, **record that it is empty, with the date, in the SJR client note**. That is the point: the absence of rules is a finding worth writing down exactly once, because today we cannot tell an empty list from an unread one. Full marks for noting the symmetry, that any rule we write on `MetaTechAI` governs Windsor Nissan and 66 Mitsu campaigns we have no business touching.
>
> **A4.** Send back: the convention is not the problem, and dropping it makes things worse. **The exposure comes from account tenancy**, a shared ad account where other pods can write account-scoped rules, not from our names. Phoenix Truxx uses the same discipline in its own account and has zero exposure, which isolates the variable. What we would lose by dropping the tags: the reporting filter. `contains Sjr-commercial` or `contains EvrythingAI` is the only thing keeping Windsor Nissan's box-truck spend and leads out of SJR's client-facing numbers, and it exists precisely because the bare `MetaTechAI` prefix over-matches. Dropping the tags trades a hypothetical rule collision for a certain reporting contamination. Credit for naming that the fix is scoping rules to entities, not renaming campaigns.
>
> **A5.** The two things: **(1)** a name-scoped rule truncated both ads at a cap nobody set, so the calculator is fed a sample size that was decided for you (LS-091); and **(2)** the periodic evaluation means the two ads did not receive equal impressions even under the same cap, and the gap is set by delivery speed, which is the variable under test. **LS-048 catches neither.** LS-048 is about the evaluation **window**, a stale average, and both failures here are **scope** and **cadence**. A rule can be perfectly windowed at 14 days and still be promiscuously scoped. **Check first: open the rules list** and find out whether any rule's condition matches this campaign's name. Everything downstream, including the 94%, is conditional on that answer. Credit for noting that 94% clears the LS-055 threshold of 90% and the verdict is still worthless, because significance tests the difference between two samples and says nothing about whether the samples were the ones you meant to collect.
