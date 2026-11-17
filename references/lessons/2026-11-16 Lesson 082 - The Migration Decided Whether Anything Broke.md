---
title: "Lesson 082 - The Migration Decided Whether Anything Broke"
type: lesson
created: 2026-11-16
tags: [advertising-science, lesson, google-ads, demand-gen, controls]
lesson: 82
topic: Google Auction & Smart Bidding
---

# Lesson 082 - The Migration Decided Whether Anything Broke

Video: `video/2026-11-16-lesson-082.mp4`

## The mechanism

Google published two control withdrawals on the same blog five weeks apart. Both read the same in a headline.
A setting the advertiser used to hold is being taken off the campaign. One of them changes what serves without
telling anybody. The other changes nothing at all. The difference is not in the size of the change or in how
loudly it was announced. It is in one step of the migration.

Think of a building where the thermostat sits in the hallway and every room obeys it. Management decides each
room should have its own dial.

Version one: before they move anything, somebody walks over, reads the hallway dial at 18 degrees, and sets all
forty rooms to 18. The building feels identical the next morning. The only thing that changed is where you stand
to adjust it.

Version two: they leave the hallway dial on the wall. It still turns. It still reads 18. New rooms simply stop
listening to it, and nobody sends an email. Walk past the dial in March and it tells you the building is at 18.
It is not.

Same headline, opposite outcomes, and one question separates them. Did anyone read the old setting before moving
the control?

That is the whole lesson, and it has a second half that matters more to us this week, because the same shape
shows up on instruments rather than settings. A thing that still responds when you poke it is not a thing that
still works. This morning our own research engine found one.

## The evidence

- **[[Google Auction & Smart Bidding#GA-102|GA-102]], T1.** Banked today. From the week of 1 December 2026 the
  campaign-level Display opt-out disappears from Demand Gen. `network_settings.target_content_network` defaults
  to `true` on new campaigns, and setting it to `false` returns `OPERATION_NOT_PERMITTED_FOR_CONTEXT`. Display is
  managed only at the ad group from then on. **This is version one of the thermostat.** Google backfills every
  existing campaign so that "None of the existing campaigns being backfilled will change their serving behavior",
  and ad group channel controls default to Display off, so the overall default is unchanged. The control was
  relocated with the operator's intent carried across.
- **[[Google PMax & Shopping#GP-051|GP-051]], T1.** Banked 26 October, taught in lesson 062. From 4 December 2026
  a new Performance Max campaign defaults to landing-page image extraction ON **even when the account-level
  switch is off**, because campaigns stop inheriting that switch. **This is version two.** The dial still
  renders, still reads Off, and governs nothing created after that date.
- **[[Google Auction & Smart Bidding#GA-066|GA-066]], T1.** Optimised targeting in Demand Gen is on by default and
  managed at the ad group. GA-102 sharpens it: after 1 December the ad group is the only level where Demand Gen
  reach is bounded at all.
- **[[Google Auction & Smart Bidding#GA-100|GA-100]], T1.** The handling precedent. A Google claim we cannot act
  on yet still gets banked, because the cost of learning it late is higher than the cost of writing it down
  early.

Notice what both T1 claims lack. No lift figure, no sample, no comparison appears anywhere in either post.
A T1 tier here buys you certainty about **what the platform will do**, and buys you nothing about whether it
helps. Both decisions are made on control and on rights, never on expected performance.

## Our accounts

Honestly: GA-102 costs us nothing today. We hold zero live Google lanes, so there is no Demand Gen campaign of
ours to be backfilled on 1 December. Writing it down now is the whole action.

The shape, though, is already live on our own stack twice, and one instance cost us something this morning.

**The frozen feed.** Google moved the Ads Developer Blog off Blogger on 11 November. The old Feedburner feed we
monitor answered HTTP 200 today with 25 entries, newest dated 10 November. The new feed answered HTTP 200 with
25 entries, newest dated 12 November, carrying a post the old feed does not have at all. Status code identical.
Entry count identical. **One post was already missed on the first weekly check after the cutover.** Nothing about
a healthy-looking response told us the source had stopped carrying anything. The watchlist now points at the new
feed and keeps no fallback.

**The pinned API version.** `real-numbers/scripts/real_numbers.py` runs on Graph API v21.0. That version ends
21 January 2027, nine weeks from today. It answers every request we send it right now, which is exactly the
problem: a working response is the only signal we have, and it will keep arriving until the day it does not. The
same page shows Marketing API v24.0's end date of 10 November 2026 has already passed. This is the lane that
produces every daily and weekly number for every client.

One more worth seeing, because it is the one branch of GA-102 that does change state. An ad group that targeted
**only** Display gets set to `PAUSED` by the backfill, since a Demand Gen ad group must target at least one
channel. No delivery is lost; that ad group was not serving anyway. But a status audit after 1 December shows a
paused ad group nobody paused. If we ever run Demand Gen, the December status check is the one that will look
alarming and mean nothing.

## The decision rule

Before you trust any surface you still read, name the one thing a working version would show that a dead or
orphaned one cannot, then go check for that specific thing.

A status code is not that thing. An entry count is not that thing. A setting rendering on screen is not that
thing. For a feed it is a dated item the old route does not carry. For a setting it is the behaviour downstream
of it. For an API version it is the published end date. If nobody on the team can name the thing, treat the
surface as already dead and find out why you were wrong.

## Quiz

Drop your answers in `lessons/_answers-inbox.md` with the lesson number.

1. Google removes a campaign-level control in both GP-051 and GA-102. One is a silent erosion and one is not.
   State the single question that separates them, in one sentence.

2. GA-102 is T1. Name one thing that tier entitles you to assert, and one thing it does not, using this claim
   as the example.

3. A client's account has a Performance Max campaign created on 1 December 2026 and an account-level Dynamic
   Image Extensions switch reading Off. You open the account on 10 December. What is actually true about image
   extraction on that campaign, and what would you have to look at to confirm it?

4. A teammate reports that a monitored source is healthy: HTTP 200, 25 entries, no errors in the log, same byte
   count as last week. Give the one check you would run before accepting that, and say what result would prove
   the source is dead.

5. On 2 December 2026 someone audits a Demand Gen account and reports "an ad group was paused overnight and
   nobody knows who did it." What is the most likely explanation, and what is the correct response?

> [!note]- Answer key
> **1.** Does the migration read and carry the operator's old setting across? If it does, the change is
> architecture and the account behaves as asked. If it does not, the behaviour changes with nobody prompted,
> and only that version is a silent erosion.
>
> **2.** T1 entitles you to assert what the platform will do: the campaign-level field will error with
> `OPERATION_NOT_PERMITTED_FOR_CONTEXT`, existing campaigns are backfilled without serving changes, Display-only
> ad groups go to `PAUSED`. It entitles you to assert nothing about performance. Google publishes no lift figure,
> no sample and no comparison anywhere in the post, so a sentence like "moving Display to the ad group improves
> results" has no evidence behind it at any tier.
>
> **3.** Image extraction is almost certainly ON, because from 4 December a new Performance Max campaign no
> longer inherits the account-level switch (GP-051). The account switch reading Off proves nothing about that
> campaign. You confirm it at campaign level, on `asset_automation_settings` for that specific campaign, not on
> the account screen. Credit for also flagging the API trap: `asset_automation_settings` is a repeated field and
> a write replaces the whole array, so a naive opt-out clears `TEXT_ASSET_AUTOMATION` too.
>
> **4.** Compare the source against an independent route that should carry the same content, and look at the
> newest dated item rather than the count. The source is dead when the other route carries a dated item the
> monitored one does not have at all, as happened to us today: both feeds returned 200 with 25 entries, and only
> one of them had the 12 November post. Any answer resting on status code, byte count or entry count is the
> failure this question is testing for.
>
> **5.** The GA-102 backfill. An ad group that targeted only Display, in a campaign with Display off, is set to
> `PAUSED` because a Demand Gen ad group must target at least one channel. Nobody paused it and no delivery was
> lost, because it was not serving before either. The correct response is to confirm the ad group's channel
> selection, set channels deliberately at ad group level, and not go looking for an account breach or reverse the
> status without reading the channel controls first.
