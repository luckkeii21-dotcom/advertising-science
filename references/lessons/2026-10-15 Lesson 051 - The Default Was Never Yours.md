---
title: "Lesson 051 - The Default Was Never Yours"
type: lesson
lesson: 51
date: 2026-10-15
topic: Google Auction & Smart Bidding
claims: [GA-094, GA-032, GA-053, GA-091]
video: none (Thursday)
tags: [advertising-science, lesson, google-ads, display-network, search-partners, defaults, channel-prioritization, tier-discipline]
---

# Lesson 051 · The Default Was Never Yours

**If you only answer two questions, answer Q4 and Q5.** Those are the two that are actually a client conversation.

Google announced two new budget controls yesterday. Most of the post is a feature announcement you could skim. One sentence inside it has a date on it, and that sentence changes a setting in a live account without anyone logging in.

This lesson is about that class of event. A default you never chose is not a setting you get to keep.

Lesson 008 covered a Meta setting nobody chose and what it did to the attribution column. This is the same species on a different platform, with one thing added that lesson 008 did not have: a date.

## 1. The mechanism

Think about how you ended up on your current electricity tariff. You did not choose it. You moved in, the supply was already connected, and a tariff got applied because something had to be applied. It worked, so you never looked. Years later the utility retires that tariff and moves everyone on it to a new one. You do not get a vote. You get a date.

Your bill changes, and the reason has nothing to do with any decision you made. It traces back to a decision you never made.

That is what is happening inside Google Search campaigns.

Today a Search campaign has one switch for the Google Display Network: on or off. If it is on, Google decides how much of your daily budget goes to Display. You never set that split. There is no field for it. The split is an implicit behaviour of the product, and it has been sitting quietly in accounts for years.

Google is replacing that switch with two controls:

- **Channel prioritization.** You mark each channel High priority or Low priority. High-priority channels get funded fully first. Whatever is left flows down to Low priority.
- **Budget allocation.** A Low-priority channel can carry a cap, written as a maximum percentage of the daily budget.

On Search the three channels are addressable separately: Google Search, Search partners, Google Display Network. On Performance Max and Demand Gen they are not. There, all the Google surfaces (Search, YouTube, Maps, Gmail, Discover) sit in one undivided group. So this control cannot pull YouTube out of a PMax campaign. Worth knowing before someone promises a client that it can.

**Now the part with the date.** Google's own words: "Starting in February 2027, for Search campaigns with the Google Display Network turned on, the current spend allocation setup will go away, and advertisers may see a shift in channel spending."

Read what that does and does not say. The old split is being retired. The new split appears nowhere in the post. So every Search campaign with Display still on is exposed to a change in where its money goes, of unpublished size, in an unpublished direction.

Google publishes one mitigation. Set the Google Display Network to "Low priority" with a 50% budget allocation and you keep roughly what you have now.

**One piece of auction logic here is worth carrying well past this feature.** Google states that channel prioritization "will generally not have an impact" on a tCPA or tROAS campaign that is not limited by budget. That is arithmetic rather than a hedge. A priority order is a rationing device. It only decides anything when there is not enough money to fund everyone in the queue. If the budget covers everything the targets will buy, nothing gets rationed and the order never fires.

So on a target-bid campaign that is not budget-capped, the percentage cap is the real control and the priority tier is decoration.

## 2. The evidence

[[Google Auction & Smart Bidding#GA-094|GA-094]], **T1**, read in full from Google's own announcement rather than from a summary of it.

[[Google Auction & Smart Bidding#GA-032|GA-032]], **T3**. Display enabled inside a Search campaign is the first of three on-by-default states that leak Google budget quietly for years. The other two are broad match paired with a non-smart bidding strategy, and auto-apply recommendations left on. GA-032 never quantified the leak on any of the three, which is exactly why it sits at T3. Its sibling [[Google Auction & Smart Bidding#GA-053|GA-053]] does carry a number from the same agency: brand overspend inside supposedly cold campaigns in roughly 90% of audited accounts, at $2,000 a month and at $100,000 a month alike.

**Now a new tier lesson.** You already know T1 can decide. Here is the limit of that. GA-094 is T1 and it contains no number at all. Not one. It is the first Google announcement in thirteen months of this engine's reading with no headline figure anywhere in it. The cap is held "on a best-effort basis", which is Google's own hedge on its own feature, and no tolerance is published.

So GA-094 is strong enough to order an audit and too thin to build a forecast on. **A tier tells you how well sourced a claim is. It does not tell you the claim is quantified.** T1 with no numbers decides what you check. It cannot decide what you promise a client.

## 3. Our accounts

The honest position first. **Nobody on our book runs a Google Search campaign today.** All five live accounts are Meta.

The one Google account we have ever run was Mattia Spinal Care in Orlando. We inherited two live Google campaigns and audited them, and we built a Performance Max campaign to spec that the client pasted in on 8 July 2026. On 4 July the decision on record was to put 100% of a $4,000 a month budget onto Google, alongside a $997 Google package. The client offboarded on 24 July 2026 and all billing stopped, so that budget never ran.

Two things follow and both are useful.

**The campaign we built was PMax, so the February 2027 line would not have touched it.** That deadline is written for Search campaigns with Display on. PMax is also the campaign type where the new control gives us the least, because the Google surfaces are one group there.

**The two campaigns we inherited: we do not know what their network switches were set to.** Nobody wrote it down. That is not a criticism of the audit. It is the whole shape of the problem. A network switch is the kind of thing you look at once, find acceptable, and never record, and that is precisely the state a retirement notice punishes.

So the audit this claim demands costs us nothing this week, because there is nothing to audit. It costs real money the day we sell the next Google engagement and inherit an account whose Display state nobody captured. **Pre-pay it. The Google intake checklist gets three lines: Display state, Search-partners state, and the date the state was read.** Minutes per account, and the window is sixteen months wide.

One nearby claim is worth holding beside this. [[Google Auction & Smart Bidding#GA-091|GA-091]], **T1**, is a Google product manager saying Demand Gen exploration is rationed by budget per asset, so a large creative pool on a small budget never finishes its own test. Same underlying machine as the new priority tier: when money is short, Google's delivery objective wins and the thing you wanted tested waits. Rationing is the theme, not the feature.

## 4. The decision rule

**When a platform retires a default, the deadline lands on the setting and not on the announcement, so record the state of every inherited switch with the date you read it, then set the state you actually want. Leaving it alone stops being the same as keeping it.**

## 5. Quiz

Drop your answers in `lessons/_answers-inbox.md` with the lesson number.

**1.** A Search campaign has the Google Display Network turned on. What specifically goes away in February 2027, and what does Google publish as the replacement?

**2.** Why does channel prioritization do nothing on a tROAS campaign that is not limited by budget? Answer with the mechanism, not the quote.

**3.** GA-094 is T1. Name one decision it is strong enough to make and one it is not, and say why the tier is not the thing that settles that.

**4.** A client calls in November 2026. They run one Search campaign at $300 a day on target CPA, Display is on, and the campaign has never been budget-limited. They ask whether this announcement will cost them money. What do you tell them, and what do you do in the account? Be specific about what you set and what you refuse to predict.

**5.** Someone on the team says the new controls let us keep PMax running on Search and Maps and cut YouTube out. Is that true? If not, what is the actual boundary, and what would you have to do instead to get that split?

> [!note]- Answer key
>
> **1.** The current implicit spend allocation between Search and Display inside the campaign goes away, and Google says advertisers "may see a shift in channel spending". The replacement default is not published anywhere in the announcement. The one published preservation setting is Google Display Network on "Low priority" with a 50% budget allocation. Credit for naming that the new default is unstated, because that is the exposure.
>
> **2.** A priority order is a rationing rule. It decides who gets funded when there is not enough budget for everyone. On a target-bid campaign that is not budget-limited there is no shortage to ration, so the order never binds and spend lands wherever the targets justify it. The percentage cap is a different kind of control: it binds whether or not there is a shortage, which is why it is the one with teeth there.
>
> **3.** Strong enough to order an audit of every client Search campaign's Display and Search-partners state, because it is Google stating a change to its own product. Not strong enough to put a number in a forecast, a report or a client promise, because the claim contains no figure of any kind and the cap holds only on a best-effort basis with no published tolerance. The tier ranks how well sourced a claim is, not whether it is quantified. T1 and unquantified is a normal combination.
>
> **4.** Tell them a change is coming, it has a date in February 2027, and Google has not published how big the shift is, so you will not guess at a number. Then act. Read and record the current Display and Search-partners state with today's date on it. Decide what you actually want on a cold Search campaign, which is usually zero Display, and set it rather than inherit it. If they want today's behaviour preserved, set Display to Low priority with a 50% allocation, which is Google's own published preservation setting. Note that on an uncapped target-CPA campaign the priority tier alone will do nothing, so the allocation percentage is the setting that matters. Full marks need both halves: set the switch, refuse the forecast.
>
> **5.** Not true. On Performance Max and Demand Gen all the Google surfaces (Search, YouTube, Maps, Gmail, Discover) are one undivided group called "Google channels", so the control cannot address YouTube on its own. Separate addressing of Google Search, Search partners and the Google Display Network is a Search-campaign capability. To get a Search-and-Maps-without-YouTube split you would have to stop asking PMax for it and run the campaign types that expose those channels separately.
