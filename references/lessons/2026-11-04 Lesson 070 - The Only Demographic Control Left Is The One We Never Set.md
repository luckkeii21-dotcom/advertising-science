---
title: "Lesson 070 - The Only Demographic Control Left Is The One We Never Set"
type: lesson
lesson: 70
date: 2026-11-04
topic: Meta Delivery & Andromeda
claims: [MD-196, MD-197, MD-013, MD-182, MD-150, AU-019, AU-076, MD-014, MD-194]
tags: [advertising-science, lesson, meta-delivery, targeting, value-rules, demographics]
---

# Lesson 070 · The Only Demographic Control Left Is The One We Never Set

Topic: Meta Delivery & Andromeda. Harvest-driven, so the rotation pointer holds at 4. This morning's research pass banked [[Meta Delivery & Andromeda#MD-196|MD-196]] and [[Meta Delivery & Andromeda#MD-197|MD-197]], and it moved the law layer. Video, 3 min 52 s, silent-capable: `video/2026-11-04-lesson-070.mp4`.

## 1. The mechanism

Meta took the gender field out of the hard-control section of the ad set. You can still walk the path: sales campaign, ad set, audiences, "Further limit the reach of your ads", accept Meta's own prompt trying to talk you out of it, "Switch setup". Custom audiences still harden there once you untick "Use as a suggestion". Minimum age is still there. Gender is not.

The operator who demonstrated the field existing is the same one who demonstrated it missing:

> "until very recently, if I get rid of that out of there, there was an option for gender. 'I only want to advertise to men. I only want to advertise to women. Don't use it as a suggestion.' ... But now, look, it's not there. It doesn't exist. We've got all these various options. We've got minimum age, but there's no gender option."

Gender still appears twice in the product. Both are suggestions. The suggested-audience section carries Meta's own sentence printed next to the setting: "We'll also show ads beyond your selected gender when it's likely to improve performance." And the creative-level pairing from October at [[Meta Delivery & Andromeda#MD-182|MD-182]], where you set an age and gender per piece of media, is also a suggestion. The operator is direct about it: "when you select cuz you think, 'Okay, we should select the gender there.' No, that is still going in as a suggestion."

So a field that read as an instruction has been replaced by two fields that read as instructions and behave as hints. That is the part worth slowing down on. The screen did not go blank. It went soft.

The analogy that maps: a restaurant used to take "no coriander" as a note the kitchen was bound by. Now the same box is headed "preferences", and the kitchen reads it, weighs it against what it thinks you will enjoy, and decides. Nothing on the form looks different. The guarantee behind it is gone, and the only person who finds out is the diner.

**The second finding today puts a number under why this keeps happening.** Meta Engineering published that one ads ranking request can require **more than 20,000 features**, against "a few hundred" when the same framework launched publicly in 2020 ([[Meta Delivery & Andromeda#MD-197|MD-197]], T1, Meta's own figure). Set that against what an advertiser can still hard-set after today: location, minimum age, language, exclusions. Four inputs against twenty thousand. The withdrawal is not Meta being stingy with controls. It is Meta removing inputs it now outweighs by four orders of magnitude.

**The only route left for gender is a bid-down value rule.** Three-lines menu, Advertising settings, Value rules, create a rule set, criteria type audience, criteria gender, select the gender you want to suppress, decrease the bid by the 90% maximum, name it, create. Then attach it inside each ad set, where the Value rules field defaults to none. Creating the rule set does nothing on its own.

And be precise about what 90% buys you. It is deep suppression at an unmeasured residual rate, never an off switch. The mechanism is that you undercut your own bid so far that other advertisers win those impressions, and the operator's own words are "very very few of your ads are going to be shown". Not none. Nobody on the roster has published what share of delivery survives a 90% cut.

## 2. The evidence

- **[[Meta Delivery & Andromeda#MD-196|MD-196]], T1 for the surface, active.** The assertion is what a Meta product screen does or does not display, which is why it earns T1 off one source, on the AU-076 and MD-099 precedent. Read the limits in the claim and keep them attached: no Meta announcement, no help-centre page, and the Marketing API changelog was read today and carries nothing for October or November on gender or demographic targeting. **That is weak negative evidence, not corroboration in reverse**, because the changelog is known to under-render and because the August placement withdrawal at [[Meta Delivery & Andromeda#MD-150|MD-150]] also arrived in-product with no announcement. One operator narrating his own screen. This lane did not see the screen and read no screenshot. No rollout fraction, no account count, no date from Meta.
- **[[Meta Delivery & Andromeda#MD-013|MD-013]] is partially falsified, and that is the more interesting event.** MD-013 held that the "further limit the reach" toggle hardens age, gender and detailed targeting into hard constraints. The gender third of that sentence is now false and carries a ⚠. The toggle still works and still switches Advantage+ broad to original broad. It no longer carries gender. MD-013's headline, that the hard boundaries are location, minimum age and language plus exclusions, is unchanged and is now one input closer to literally true. **A claim getting narrower and more accurate at the same time is what a working codex looks like.**
- **[[Auction Mechanics & Bidding#AU-019|AU-019]] was promoted today from preferred alternative to only option for gender, with its evidence explicitly unchanged.** That distinction is the whole lesson in tier discipline. The bid-down did not get better. The alternative got deleted. The 90% figure still has no test behind it, and the claimed delivery advantage over a hard exclusion has never been measured by anyone.
- **[[Auction Mechanics & Bidding#AU-076|AU-076]], T1, is now load-bearing in two places.** The gender criterion, because it is the last place gender can be steered. And the ten-rules-per-set ceiling, because an account replacing several withdrawn ad-set controls with value rules at once can actually reach it. Meta's own tickbox on that surface reads "I understand my overall cost per result may increase when using value rules."
- **[[Meta Delivery & Andromeda#MD-197|MD-197]], T1.** Banked for the 20,000 figure and for the cadence direction only: the release path was rebuilt so each feature ships and rolls back independently, and "comparable extraction features now reach production ~3.6x faster". Meta names the consequence itself, more model iterations in the same period. It discloses no retrain cadence and it is **not** an explanation for any specific account's drop. Reaching for it that way is exactly the error the breakdowns-first ladder exists to stop.
- **[[Meta Delivery & Andromeda#MD-014|MD-014]], T3, is untouched by any of this and still runs first.** It holds that demographic restrictions cut the auction pool and block Meta from finding converters outside the assumption, naming gift buyers and pass-along buyers. It also carries the five-minute check: gender-tag the client's own customer list from first names and read the real split before proposing any gender rule. The instrument changed. The reason to distrust a gender assumption did not.

## 3. Our accounts

**Phoenix Truxx is the account with a standing client instruction that this change touches.** The approved-language rules say it plainly: "Domestic trucks and Spanish-weighted working men, never women as the target." That instruction has never been a hard setting in the ad set. The 15 September account audit recorded targeting running **18 to 65+ unexcluded**, with roughly **1 in 7 opt-ins outside the 25-64 working band**, and set an age floor as an open task. That task is still open, **fifty days later**.

Read those two facts together and the headline of this lesson falls out. The demographic control Meta withdrew is one we never used on that account. The demographic control Meta kept, minimum age, is the one we identified ourselves as worth setting, measured the cost of not setting, wrote down, and never set.

**StayWell is the counterweight, and it argues the field was doing less than anyone assumed.** No gender setting on any ad set. Delivery found the demographic anyway. Week of 23 to 29 October: **women 55-64 were the top band, 7 of 23 opt-ins**, 100% Michigan. Week of 9 to 15 October: **women 45-64 took 20 of 28**. Two consecutive filed weeks where the audience arrived gender-skewed with nobody instructing it. If the creative and the offer are doing the selection, a withdrawn checkbox costs nothing.

**StayWell also carries our only measured evidence that the surviving control works.** The 22 September age fix, vague to 45-60, was verified: **65+ fell from 52% to 22.2% of combined spend and cost per opt-in held**. In the same read 55-64 was the best band at **$15.86** and 45-54 was the weak spot at **$50.42 on 34% of spend**. Minimum age moved real money. That is the one still on the screen.

**RK Consumer Services is the account where today changes nothing, for a reason worth knowing.** Its launch playbook already records that the Special Ad Category "fixes age at 18 to 65+, gender to all, and removes ZIP, lookalikes and detailed targeting. The creative does the targeting." The category took the field away before the product did. An account already operating without a lever cannot lose it.

**SJR Commercial: no gender setting recorded anywhere in the vault, and no client instruction asking for one.** Nothing to check and nothing to unwind.

**ChiroWorks is off-boarded, so its persona split is history rather than exposure.** The targeting brief ran "core 40 to 65, split by persona at the ad-set level", which was an age-and-creative split, never a gender constraint.

**The gap this opens on our own book, and nobody has looked at it.** Meta withdrawing the field says nothing about what happened to a gender setting already saved on a live ad set. We believe we have none. We have never read one to confirm it, and [[Meta Delivery & Andromeda#MD-194|MD-194]] is a standing warning that a Meta audience setting you believe you set can stop being the setting you set. That makes four two-minute reads in a live interface now carried across four consecutive lessons, and none of them has an owner.

## 4. The decision rule

**When a client asks for men-only or women-only, the honest answer is that nobody can do that any more, and the only thing on offer is a 90% bid-down value rule built once and attached to every ad set by hand. Before you build it, run the first-name split on their own customer list, because the field being gone is not a reason to skip the check that said the assumption was probably wrong.**

And the second clause, which is the one with money behind it: **a withdrawn control is not a reason to look away from the controls that remain.** Location, minimum age, language and exclusions still bind. On Phoenix Truxx one of those four has been identified, costed and left unset for fifty days.

## 5. Quiz

Answers go in `_answers-inbox.md`.

**Q1.** MD-196 is T1 off a single operator with no Meta announcement, no help-centre page and no changelog entry. Explain what kind of assertion earns T1 from one source, and say why the missing changelog entry is weak negative evidence rather than a contradiction.

**Q2.** AU-019 was promoted today from preferred alternative to only option for gender, and the claim states its evidence is unchanged. Explain why both halves of that sentence are true at once, and say what would have to happen for the 90% bid-down to actually get stronger as a claim.

**Q3.** Applied. A client tells you their buyer is a woman over 40 and asks you to target women only. Write the two things you say, in order, and name the claim behind each. Then describe what you build, including the step most people miss, and state plainly what the build does and does not do to delivery.

**Q4.** Applied. Someone on the team cites MD-197's 20,000 features and the 3.6x faster release path to explain why StayWell's cost per opt-in moved from $14.35 to $29.87 across two weeks in October. Say what is wrong with that, name what MD-197 may and may not be used for, and say what you would look at instead.

**Q5.** Applied. You are handed Phoenix Truxx and told to act on today's finding. Say which of the account's demographic controls the finding actually implicates, which one the account has an open task on and for how long, and what you check before writing a single value rule. Then say which of our five accounts is unaffected by the withdrawal and why.

> [!note]- Answer key
>
> **A1.** T1 off one source is earned when the assertion is **what a product screen does or does not display**, which is directly observable and is not a performance claim, per the AU-076 and MD-099 precedent. It is T1 **for the surface only**: no rollout fraction, no account count, no date from Meta, and no claim that the change performs any particular way. The missing changelog entry is weak negative evidence for two named reasons: the Marketing API changelog index is **known to under-render**, recorded 2026-08-24, and the August placement withdrawal at MD-150 **also arrived in-product with no announcement** and with the help centre still describing the old behaviour. Silence from Meta is the pattern here, not a denial. Credit for noting this lane never saw the screen and read no screenshot.
>
> **A2.** They are both true because **promotion was by elimination, not by evidence**. The hard-exclusion alternative that AU-019 argued against no longer exists to choose, so the bid-down is the only option by default. Nothing was measured: the 90% figure still has no test behind it and the delivery advantage over a hard exclusion has still never been measured by anyone on the roster. For the claim to actually get stronger, somebody would have to run the isolated test: hold creative, budget, geo and placements still, apply the 90% gender bid-down, and publish **what share of delivery survives it** and what it cost. Full marks for naming that "only option" and "well evidenced" are independent properties, and that confusing them is how a convention becomes a rule.
>
> **A3.** First: **nobody can target women only any more, on any account**, and that is the product rather than a problem with theirs (MD-196). Second: **before any gender rule ships, gender-tag their own customer list from first names and read the real split** (MD-014), because the people a gender restriction removes are gift buyers and pass-along buyers, and the assumption is a hypothesis until the list is read. What you build: a value rule set under Advertising settings, criteria type audience, criteria gender, select **men** to suppress, decrease bid by the **90% maximum** (AU-019, AU-076). **The step most people miss: creating the rule set does nothing. It has to be attached inside each ad set, where the Value rules field defaults to none.** What it does: suppresses delivery deeply and reversibly, backed out with a slider rather than a relaunch. What it does not do: switch delivery off. Residual delivery continues at a rate nobody has published. Credit for mentioning the ten-rules-per-set ceiling and Meta's own tickbox conceding cost per result may rise.
>
> **A4.** It is the wrong altitude. MD-197 is **a platform-wide infrastructure disclosure with no advertiser surface**: no feature, setting or report is exposed by it. It discloses **no retrain cadence**, so it cannot date or size any change in any account. It may be used for exactly two things: the **20,000-feature figure** as the hard number under "the system reads more than you can address", and the **direction** that the substrate is changing faster, which is a general reason to expect an unchanged ad set to drift. It may never explain a specific account's drop. That is the error the breakdowns-first diagnostic ladder exists to prevent, whose stated prior is that the cause is usually local. What to look at instead for that StayWell window: the filed read already names it, **one campaign**, Dr. Schneider's $75 collapsing from 26 opt-ins at $11.97 to 11 at $27.49 with its sciatica ad going $11.95 to $30.77, plus the click-to-form softening. Local, visible, specific.
>
> **A5.** The finding implicates **gender**, which Phoenix Truxx has **never set as a hard control**, so the withdrawal changes nothing it is doing today. The control it has an open task on is the **age floor**: the 15 September audit recorded targeting at **18 to 65+ unexcluded** with about **1 in 7 opt-ins outside the 25-64 working band**, and that task has been open **fifty days**. Age is one of the four controls that still bind, so it is the one with money behind it. Before writing any value rule: read the client instruction as written, confirm no gender setting is saved on a live ad set (MD-194 says a setting you believe you set can stop being it), and run the MD-014 first-name split. The unaffected account is **RK Consumer Services**: its Special Ad Category already fixes gender to all and age to 18 to 65+, so the category removed the lever before the product did. Full marks for noting the correct first move on Phoenix is the age floor, not a gender rule.
