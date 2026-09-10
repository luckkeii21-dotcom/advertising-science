---
title: "Lesson 022 - An Empty Row Has Two Causes"
type: lesson
lesson: 22
date: 2026-09-10
topic: Meta Delivery & Andromeda
claims: [MD-150, MD-151, MD-152, MD-016, SC-149, AU-076, AU-019]
tags: [advertising-science, lesson]
---

# Lesson 022 · An Empty Row Has Two Causes

Meta is taking away four ad-set controls. Yesterday's research run found the notice sitting inside Ads Manager. Before you decide how much to care, you have to answer one question about your own account, and today's lesson is that the question is harder than it looks.

## 1. The mechanism

Meta's notice, word for word, live inside the Placements section of an ad set:

> "Excluding placements, platforms, devices and operating systems will no longer be available for your ad sets."

Read the sentence slowly. It names four controls, and everyone is going to hear one.

1. **Placements.** Switch off Audience Network, Marketplace, Search results, Reels.
2. **Platforms.** Run Instagram only. Run Facebook only.
3. **Devices.** Mobile only. Desktop only.
4. **Operating systems.** iOS only. Android only.

All four go at ad-set level. Two things are offered in their place, and neither one does the same job.

**A placement value rule bids down instead of switching off.** The platform maximum is a 90% bid decrease. Ben Heath, demonstrating it on screen, describes the mechanism honestly: you undercut your own bid so other advertisers win the impression. His own words for the result are "very very few of your ads are going to be shown". Very few is a number above zero, and nobody publishes it.

Here is the analogy that maps. A hard exclusion is closing your account at a shop. A 90% bid decrease is keeping the account open and deciding you will only ever pay a tenth of the asking price. On a busy day you never buy anything. On a slow day, when nobody else turns up, you walk out holding something. The shop does not send you a report of the days you nearly bought.

That distinction is why one line in our own codex had to be corrected yesterday. AU-019 has been titled "up to the 90% maximum for effective exclusion" since it was banked. A 90% decrease is deep suppression at an unmeasured residual rate. Calling it exclusion was tolerable while a real exclusion sat next to it in the same panel. It stops being tolerable when the bid-down becomes the only ad-set lever, because a client told Audience Network is "excluded" by a value rule has been told something false.

**Now the part that matters more than the change itself.** Suppose you want to know what these controls were doing for you. You open the placement breakdown, and Audience Network is not in it. Zero spend. No row at all.

An empty row has two causes, and the breakdown records neither one.

- Someone excluded the placement, so delivery was never allowed to buy it.
- Nobody excluded anything, and delivery simply did not buy it.

Those are opposite facts about your account and they produce an identical export. Case one means you are about to lose a control that was doing real work. Case two means you are about to lose a control you were never using. The report cannot tell you which, because a spend breakdown is a record of what was bought and it has no field for what was forbidden.

## 2. The evidence

**[[Meta Delivery & Andromeda#MD-150|MD-150]], T1 for the notice and the surfaces only.** We hold Meta product copy read off the screen as documentation, on the AU-076 precedent. Everything about the rollout inside that claim is **T3** and is marked as such.

**Read the scope guards before you repeat any of this to a client.** Meta has published no announcement. Trade coverage on 2026-08-25 found the Business Help Centre still describing manual placement selection as available. Jon Loomer, who carries the verbatim notice, labels his own scope information unofficial in his own words: "Nothing is official until it's documented in an announcement or found on Meta's official pages." His unofficial read is a test, sensitive verticals excluded, **Sales and Leads objectives only**. Ben Heath states it as done and going "across the board", with no scope and no test framing anywhere in eighteen minutes. Loomer and the trade reporting agree with each other and disagree with him. Nobody should tell a client this has happened to their account.

**[[Meta Delivery & Andromeda#MD-151|MD-151]], T1 for the replacement surfaces and their limits.** Three holes in the value rule, all checkable in the UI. Only seven placements are eligible against 17 to 21 selectable in an ad set. **There is no value-rule criterion for PLATFORM at all.** And a rule set does nothing until it is attached, ad set by ad set. The account-level Placement Controls setting is the only true off switch left, and it is account-wide, so it cannot differ between two clients sharing an account.

**[[Scaling Models#SC-149|SC-149]], T3, and it is the claim that decides how much of this should worry you.** Loomer's governing sentence: "The performance goal matters a whole lot when assessing whether there's a problem to be solved." Under conversion optimisation, delivery self-corrects, and his position is that "there aren't placements that are known to be sources for low quality conversions". Under upper-funnel goals the logic inverts, because a cheap junk impression satisfies a link click or a ThruPlay perfectly well. He names the exposures precisely: **Audience Network** for link clicks and landing-page views, **Audience Network Rewarded Video** for ThruPlay.

**[[Meta Delivery & Andromeda#MD-016|MD-016]] was amended and deliberately not refuted.** It holds a three-way argument about whether to prune junk placements, between Shiver's exclusion recipe, Charley T's rebuttal that the placements in question take under 0.1% of budget, and Piliero's trim-on-your-own-data policy. That argument was never settled by evidence. What changed is that one side's execution route is being withdrawn.

**Law 1a moved.** Its list of ad-set settings that genuinely bind is losing four members. Location, minimum age and language are untouched, so the sentence you already know gets stronger. Geo is now close to the last ad-set setting that does what it says.

## 3. Our accounts

Nobody on our book has ever opened a placement breakdown to answer this question. Three were sitting in the client folders. Here is what they say.

**SJR Commercial, roughly 90 days to 2026-05-18, $33,532.56 of placement-attributed spend.** This is the only window on our book where any of the four withdrawn controls had something to switch off.

| Control being withdrawn | What it would have removed | Spend | Share |
|---|---|---|---|
| Placement exclusion | Audience Network, both positions | $563.02 | **1.68%** |
| Device limiting | desktop, iPad, Android tablet | $664.77 | 1.98% |
| Platform exclusion | Instagram, all three positions | $9,922.00 | 29.59% |
| OS limiting | Android smartphone | **$12,313.98** | **36.70%** |

Four numbers, and the interesting one is the bottom row.

**Audience Network took 1.68%.** Charley T's rebuttal in MD-016 sets the "too small to matter" bar at under 0.1% of budget. Our own number is nearly seventeen times that, so on this account his rebuttal is wrong on the arithmetic. Note also that AN Rewarded Video ran at a **$68.23 CPM**, the most expensive impression in the account against a blended $24.05. The folklore says junk inventory is cheap. Ours was the dearest thing we bought. Both facts fit together: a viewer paid in virtual currency to watch will finish the video, so the CPM is high and the ThruPlay is cheap, which is exactly why an upper-funnel goal walks into it. **The window contains one LINK_CLICKS campaign, VIN IQ Used Unique Units, $1,086.14 at a $5.53 CPM, the cheapest campaign CPM in the account.** Nothing filed lets me crosstab campaign against placement, so read that as consistent with SC-149 rather than as shown.

**The OS row is the one to remember.** Android smartphone cost a **$29.91 CPM against iPhone's $21.36**, forty percent more per thousand impressions. An operator with the OS control and an eye on CPM has an obvious move available, and taking it would have removed **36.7% of the account's delivery**. There is no opt-in column in that breakdown. There never was. The whole case for switching Android off is built on a cost number with no result number beside it. The withdrawn control that could have hurt us most is the one nobody is mourning.

**Now the platform question, on three accounts, in the same summer.**

| Account | Window | Opt-ins | Instagram share of spend | Cost per opt-in, Facebook | Cost per opt-in, Instagram |
|---|---|---|---|---|---|
| SJR Commercial | 10-20 Jul 2026 | **256** | 28.91% | **$4.00** | **$4.00** |
| ChiroWorks | 10-27 Jul 2026 | 28 | 6.70% | $34.62 | $14.93 |
| Mattia Spinal Care | 26 Jul - 3 Aug 2026 | 19 | 29.90% | $23.95 | $54.49 |

SJR is the account with volume, and its two platforms are priced identically to the cent. $728.14 and 182 opt-ins on Facebook. $296.09 and 74 on Instagram. That is what an auction under conversion optimisation is supposed to do, and it is the cleanest demonstration of SC-149 on our own book.

The two small accounts disagree with each other by a factor of 2.3, in opposite directions, on 19 and 28 opt-ins. Mattia's Instagram number rests on **three opt-ins**. Nobody should touch a platform on the strength of three.

**Audience Network appears in none of the three exports.** Not one dollar across $2,461.70. And I cannot tell you why, which is the whole point of section 1. Five positions that were live in SJR's spring window are absent from its July window, including Instream Video at 5.8% and Reels Overlay at 1.2%. Nobody excludes Reels Overlay and leaves Marketplace running. The likelier reading is that the campaigns and the creative changed and delivery bought a different mix. The reading I cannot rule out is that somebody acted on the May audit, which recommended in writing that "Audience Network across the board should be off for lead campaigns". **One instrument settles it and it expires when the change lands: open a live SJR or Phoenix Truxx Sales or Leads ad set and write down what the four controls are actually set to.** After the withdrawal that record cannot be reconstructed from any export.

One more thing worth seeing. ChiroWorks' breakdown contains a row labelled `unknown / Unknown`, $0.36, two impressions, a $180 CPM. The instrument you are reading has a bucket for impressions it cannot classify. It is tiny here. It is not always tiny.

## 4. The decision rule

**A placement breakdown records what delivery bought and has no field for what it was forbidden to buy, so a missing row proves nothing until you have read the ad-set setting. Read the settings on every live client ad set now, write them down, and only then decide whether losing the control costs you anything.**

## 5. Quiz

Answers go in `_answers-inbox.md`. Partial answers get graded.

1. Meta's notice names four controls. Name all four, and say which one has no replacement at all under the new architecture.
2. A client asks you to switch Audience Network off after the change lands. You build a placement value rule at the 90% maximum. Write the one sentence you send the client describing what you have actually done, and say why the word "excluded" cannot appear in it.
3. **Application.** You open Phoenix Truxx's placement breakdown for last month. Audience Network has no row. Write down the two things that could be true, say which piece of evidence separates them, and say what you would do this week given that the evidence expires.
4. **Application.** Someone shows you the SJR device table: Android CPM $29.91 against iPhone $21.36, Android taking 36.7% of spend. They propose limiting delivery to iOS while the control still exists. Give the strongest version of their argument, then kill it, using two specific weaknesses. Say what single column would settle it and where you would get it.
5. Mattia's Instagram cost per opt-in is $54.49 against Facebook's $23.95, and Instagram takes 29.9% of that budget. SJR's two platforms are level at $4.00. Explain both results with one mechanism, and state what would have to be true of the Mattia numbers before you acted on them.

> [!note]- Answer key
>
> **Q1.** Placements, platforms, devices, operating systems, all at ad-set level. **Platform has no replacement.** MD-151: there is no value-rule criterion for platform, so an Instagram-only build can only be approximated by bidding down each of that platform's placements one at a time, and only seven placements are eligible for a value rule at all. Credit for also naming the account-level Placement Controls setting as the surviving off switch and for saying it is account-wide, so it cannot differ between two clients sharing an account.
>
> **Q2.** Something close to: "Audience Network is now bid down by 90%, which makes it expensive enough that we expect almost no delivery there. It cannot be switched off at ad-set level any more, so a small residual is possible and I will report what it costs." The word excluded cannot appear because a 90% bid decrease suppresses delivery at a rate nobody measures and never eliminates it. This is the AU-019 wording correction. Full marks require the residual being owned out loud rather than buried.
>
> **Q3.** Either the placement was excluded in the ad set, or delivery was free to buy it and did not. The export is identical under both. **The evidence that separates them is the ad-set setting itself**, which you can still read today and cannot reconstruct after the withdrawal. This week: open every live Sales or Leads ad set on SJR and Phoenix Truxx, record placements, platforms, devices and operating systems as they are currently set, and file it with the date. Extra credit for pulling the placement breakdown at the same time, since MD-016 notes the breakdown survives the control, and for noting the chiropractic accounts are the wrong instrument because health and wellness sits among the verticals Loomer says are excluded from the test.
>
> **The half-mark trap:** answering only "it means nobody excluded it" is the natural reading and it is one of the two cases, asserted without evidence.
>
> **Q4.** Strongest version: Android is 40% more expensive per thousand impressions, its frequency is higher at 4.19 against 3.75 which suggests a smaller pool being hit harder, and 36.7% of spend is a large enough share that a real CPM gap is worth money. **Two weaknesses.** First, the device breakdown has no result column, so the entire case is a cost number with no opt-in number beside it, and a dearer impression that converts better is a bargain. Second, this removes over a third of delivery in one move, which SC-149's own qualifying test forbids unless "this finding is based on meaningful data" of a kind Meta does not already have, and a CPM gap Meta can see perfectly well is not that. **The settling column is cost per opt-in by device**, available from an Ads Manager export with the device breakdown and the results column selected. Credit for noting the CPM gap may be a creative artefact rather than an audience one, and full marks require refusing the move until the column exists.
>
> **Q5.** One mechanism: under conversion optimisation the auction equalises marginal cost per result across surfaces, so at real volume the platforms converge, which is what SJR's 256 opt-ins show at $4.00 against $4.00. Divergence at small n is sampling noise, and it points in whichever direction the last few opt-ins happened to land, which is why ChiroWorks and Mattia disagree by the same factor in opposite directions. Before acting on Mattia you would need the gap to survive many times the current sample, since three opt-ins carry it now, and you would need it to persist across a creative refresh, because a vertical-video ad underperforming in an Instagram surface is a creative fact rather than a platform fact. Credit for pointing out that after the change nobody can act on it at ad-set level anyway, since platform has no value-rule criterion.

---

**Related:** [[Meta Delivery & Andromeda]] · [[Scaling Models]] · [[2026-09-09 Lesson 021 - The Offer Changed, the Prediction Did Not]] · [[2026-08-20 Lesson 004 - Controls Bind, Suggestions Don't]] · [[2026-08-27 Lesson 009 - The CPM Does Not Say Why]] · [[SJR Commercial]]
