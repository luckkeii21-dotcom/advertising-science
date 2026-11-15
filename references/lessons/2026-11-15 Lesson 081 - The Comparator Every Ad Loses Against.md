---
title: "Lesson 081 - The Comparator Every Ad Loses Against"
type: lesson
created: 2026-11-15
tags: [advertising-science, lesson, meta-delivery, frequency]
lesson: 81
topic: Meta Delivery & Andromeda
---

# Lesson 081 - The Comparator Every Ad Loses Against

## The mechanism

There is a popular read going around that says "mid-funnel" is not a real thing. What you have instead is your
campaign's own daily frequency, and you judge each ad against it. An ad below the campaign number sits higher in
the funnel. An ad above it is working the warm audience. Then you pair it with CPM to get a diagnosis.

The read is good. The comparator is broken, and it breaks the same direction every time.

Here is why. Impressions add up across ads. Reach does not. If the same contractor sees three of your ads, each
ad's Reach cell counts him once, so the three ad rows sum to three while the campaign counts one person. Divide
impressions by reach at each level and an identity falls out:

`campaign frequency = (impression-weighted average ad frequency) x (distinct ads seen per reached person)`

That second factor is creative breadth. It is not repetition and it is not fatigue. It is the thing we spend all
week trying to build. But it sits inside the campaign frequency number as a multiplier, so the campaign number is
always larger than any single ad's number, by roughly the number of distinct ads a person sees.

Think of a shop with four staff. Each one serves the same regular twice. Ask a staff member how often he saw that
regular and he says twice. Ask the shop and the shop says eight visits. Nothing about the regular changed. The
shop count carries how many staff he walked past. Judging one staff member's "twice" against the shop's "eight"
to decide whether he is crowding the regular is a category error.

So when you rank ads against campaign frequency, every ad loses. Every single one. You have not measured funnel
position. You have measured how many ads are running.

## The evidence

- **MD-200, T3.** The read itself, banked 12 November: reject mid-funnel, use the campaign's own daily frequency as
  the baseline, pair it with CPM. It is asserted with no data shown, which is what a T3 means and exactly why the
  arithmetic underneath it was worth checking.
- **MD-155, T2 for the sizes and plain arithmetic for the identity.** The two-factor decomposition above, already
  verified to four decimals on three of our own accounts in September. This is the claim that kills MD-200's
  comparator, and it was already in the codex when MD-200 was banked.
- **MD-047, T3.** The four-metric read (spend, frequency, CPM, cost per result) that MD-200 is supplying a
  comparator for. Its own wording only says frequency "tells you who the ad is being shown to", with no number
  attached, which is the gap MD-200 was trying to close.
- **MD-080, T3.** Never compare two ad sets at different spend levels, because the lower-spend one reads better on
  CPM and enters lower in the funnel. MD-200 is that discipline applied between ads instead of between ad sets, so
  it inherits the same requirement: the two things you compare have to be the same kind of thing.

Notice what the tiers bought. A T3 gave a usable shape. A T2 plus arithmetic showed the shape was pointed at the
wrong number. Neither was wasted, and the T3 does not get thrown away.

## Our accounts

Pulled live from Phoenix Truxx this morning. Window 9 to 15 November, all three campaigns that spent.

| Campaign | Spend | Campaign frequency | Avg ad frequency | Breadth | Ads above the campaign number |
|---|---:|---:|---:|---:|---:|
| Approved statics test | $928.38 | 2.0053 | 1.5477 | 1.2957 | 0 of 27 |
| Dump Truck leads | $375.44 | 2.8196 | 1.6106 | 1.7506 | 0 of 21 |
| Box Truck leads | $112.95 | 2.1033 | 1.6759 | 1.2550 | 0 of 7 |

Zero of 55 ads. Not a close call either. The highest ad-level frequency in the statics campaign is 1.8966 against
a campaign number of 2.0053, so the single most repeated ad we own still reads as top-of-funnel.

The identity reproduces exactly. 1.547661 x 1.295697 = 2.005300, against a campaign figure of 2.005300. Same on
the other two campaigns, to six decimals. **One correction to how we have been stating it: the weighting has to be
by impressions, not by spend.** Spend weighting returns 1.9775 on the statics campaign, close enough to look right
and wrong by 1.4%.

Read the dump campaign with the right eyes and it changes meaning. Campaign frequency 2.82 is the highest number on
the account and looks like a fatigue problem. Decompose it: 1.61 repetition times 1.75 distinct ads per person. The
repetition is the **lowest** per-ad figure across all three campaigns. That campaign is not tired. It is broad,
because it is carrying 21 live ads.

Now run MD-200's pairing against the comparator that works, 1.5477 frequency and $32.29 CPM on the statics
campaign, where the campaign averages $12.72 per lead.

- **Dream_Truck.** Frequency 1.768, CPM $19.63, $7.13 per lead. High frequency, low CPM, and it closes better than
  the campaign average. This is what a working warm ad looks like.
- **Box Truck Ad version-2.** Frequency 1.717, CPM $30.87, $11.05 per lead on $198.83. Same corner, same verdict.
- **One Truck - Multiple Bodies.** Frequency 1.739, CPM $15.20, $17.74 per lead. Above-average frequency and
  below-average CPM, so it is talking to warm people, and it closes 39% worse than the campaign average. By the
  rule that is a bad warm-audience ad.
- **Service truck, Black Hino rollback.** Frequency 1.897, the highest in the campaign, CPM $14.04, zero leads on
  $28.06. The worst failure of the test on the account.
- **Phoenix Experience – Copy.** Frequency 1.334, CPM $42.61, $14.03 per lead on $350.87, which is 38% of campaign
  spend. Low frequency, high CPM, worse than average cost per lead. That is the funnel-filling corner, and worse
  than average is the **expected** result there. Nothing to fix.

Two honest limits. Those lead counts are Ads Manager's, so the trim call on the two failing ads gets confirmed
against real CRM people before anything is paused. And Meta prints frequency over whatever window you ask for, so
both sides of the comparison have to use the same window or the read is noise.

## The decision rule

Compare an ad's frequency against the impression-weighted average ad frequency inside its own campaign, never
against the campaign's own frequency, because the campaign number carries creative breadth as a multiplier and
every ad will lose to it.

## Quiz

Drop your answers in `_answers-inbox.md`.

1. State the two-factor identity for campaign frequency, and say which of the two factors can burn out.
2. A campaign shows frequency 3.4. Its ads all sit between 1.3 and 1.9. Nothing is wrong. Explain in one sentence
   why not.
3. Why does ranking ads against campaign frequency always produce the same verdict, whichever ads you run?
4. An ad in a campaign averaging $20 per lead has frequency 1.9 against a weighted ad average of 1.5, a CPM of $11
   against a campaign $26, and costs $31 per lead. What is your call, and what is the reasoning chain?
5. Same campaign. A second ad has frequency 1.2, CPM $44, and costs $27 per lead. Your client asks you to pause it
   for being the worst performer in the account. What do you say?

> [!note]- Answer key
> 1. `campaign frequency = (impression-weighted average ad frequency) x (distinct ads seen per reached person)`.
>    Only the first factor is fatigue. The second is creative breadth, which is what we are trying to build, so a
>    rising campaign frequency can mean the account got broader rather than more tired. MD-155.
> 2. Because 3.4 decomposes into per-ad repetition times how many distinct ads each person saw, so a campaign with
>    many live ads reads high on frequency while no individual ad repeats much. At 1.9 the worst-repeating ad is
>    still low, and the breadth factor is carrying most of the 3.4.
> 3. Because the campaign number is the weighted ad average multiplied by a breadth factor that is always at or
>    above 1, the campaign number is always at or above every ad's number. So every ad reads below it and every ad
>    gets classified top-of-funnel. The test has no power to separate anything.
> 4. Trim it or rewrite it. Above-average frequency plus below-average CPM puts it in the warm corner, which is
>    where cost per lead is supposed to be **better** than the campaign average, and $31 against $20 is 55% worse.
>    An ad that cannot close warm people better than the campaign closes strangers is a bad warm ad. Confirm
>    against CRM people before pausing, since the lead count is Ads Manager's.
> 5. Push back. Low frequency plus high CPM is the funnel-filling corner, where a worse-than-average cost per lead
>    is the expected outcome and not a fault, so $27 against $20 is this ad doing its job. Pausing it removes the
>    ad that feeds the audience the cheap warm ads are closing. The ad to look at is the one in question 4, which
>    looks better on cost per lead and is failing the test that applies to it.
