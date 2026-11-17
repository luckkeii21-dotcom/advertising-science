---
title: "Lesson 083 - The Footnote Was The Finding"
type: lesson
created: 2026-11-17
tags: [advertising-science, lesson, attribution, incrementality, meta]
lesson: 83
topic: Attribution & Incrementality
---

# Lesson 083 - The Footnote Was The Finding

Video: `video/2026-11-17-lesson-083.mp4`

## The mechanism

On 15 November this engine read a 20-page Meta report in full and banked seven claims out of it, the biggest
single haul since the Andromeda posts. Every headline number in it is true. Not one of them transfers to our
accounts. The reason is the same in all three cases, and it is the thing worth learning today.

A number has a headline and it has a condition. The headline travels. The condition stays in the footnote.

A gym advertises that members lose 11 kilos on average. True number, measured honestly. The average is taken
over members who finished the twelve-week program. Everyone who quit in week three is outside the denominator.
You walk in off the street and you are not in that denominator yet, you are in the full population, and the full
population average is nothing like 11 kilos. The gym did not lie. It printed a number whose condition it did not
print beside it.

Three shapes of this showed up in one document.

**Shape one: two numbers that are one number.** Meta reports that advertisers undervalue Meta by 31% at the
median under rules-based attribution, and separately that a multiplier of at least 1.45X was needed to calibrate
models to Meta's true contribution. Those read like a finding and a confirmation. Do the arithmetic: 45 divided
by 145 is 31.0%. It is one measurement stated from both ends. Quote them together in a client deck and you have
said one thing twice and implied two independent sources.

**Shape two: the denominator with the failures removed.** The report prints a 46% average performance lift for
incremental attribution across 37 studies. The footnote restricts those 37 to studies "where statistically
significant incrementality was detected in at least one cell". Every test that found nothing is outside the
count. The honest reading of that number is not "this works 46% better". It is "when it works, it works 46%
better", and nobody published how often it works.

**Shape three: the recital.** A Kantar figure of 51% appears on Meta's own MMM blog post as "marketers using MMM
alongside other tools". The same 51% appears in this report as advertisers who default to whichever solution
holds the most credibility inside their organisation when results conflict. Same survey, same number, two
different propositions. Only the report carries the footnote. The blog recites.

## The evidence

New from 15 November, all read at source in the primary document:

- **AT-139, T1.** The 31% median and the 1.45X minimum multiplier, with the 307-study footnote and the
  arithmetic identity between the two figures.
- **AT-141, T1 for the sentence and T3 for the effect.** The 46% and the conditioned denominator.
- **AT-145, T1.** The method claim. Find the primary document before carrying a figure a blog post recites.
- **AT-140, T1.** Meta's which-tool-when ladder, and its own guard: run several tests and let a pattern emerge
  rather than acting on one study.
- **AT-143, T1.** Conversion Lift now runs off the Conversions API, which Meta names as recommended over the
  pixel, and it is self-serve in Experiments for "all qualified advertisers" with qualified left undefined.
- **AT-144, T1.** The negative, banked so nobody reads the document again: no holdout size, no minimum
  detectable effect, no power figure, no confidence interval, no geo design across all 20 pages.
- **AT-142, T1.** Calibration through bid strategy, the one route needing neither a lift test nor a model.

The tier lesson is in AT-139 and it is the sharpest one this file has produced. **T1 is the top tier and the 31%
is still unusable.** The tier scores where a sentence came from, never whether the effect carries to you. A T1
claim read off a 307-study footnote can be more dangerous than a T4 practitioner guess, because the tier buys it
authority it has not earned on your account. Read the tier, then read the condition.

And read the footnote's own arithmetic. 307 studies came from 54 advertisers. That is 5.7 studies each, so the
median is not a median over independent businesses.

## Our accounts

Three reasons the 1.45X does not come near our numbers, in rising order of how badly it fails.

**It is the wrong outcome.** The statics campaign on Phoenix Truxx ran at $12.72 per Ads Manager lead over 9 to
15 November at a $32.29 CPM. Divide by 1.45 and you get $8.77, which looks like a finding and is not one. The
307 studies measure purchases for conversion-optimised advertisers. We measure instant-form opt-ins, several
steps upstream of money.

**It is the wrong population.** 54 advertisers across North America, EMEA, APAC and LATAM, no spread published,
no distribution, no per-vertical or per-spend-tier split, and no count of how many of the 307 found no lift at
all. A median with no spread cannot tell a truck dealership in New Jersey anything about itself.

**We could not run the test that produces it.** Across five accounts exactly one attributed-sale series exists:
Phoenix Truxx, 19 sold records, 13 marked ours, 18 March to 21 August 2026. That is 157 days for 13 sales, so
about 1.7 in a 21-day window. A lift test needs outcomes, and ours barely exist.

What is actually free sits in AT-143. Conversion Lift now runs off the Conversions API, our accounts already send
server-side CRM events, and the test is self-serve inside Experiments. **Nobody has opened the Experiments tab on
any of our five accounts, and today is the third day that gap has been open.** Opening a tab is a look, not a
spend. It would tell us what "qualified" means for us, which is the only unknown standing between us and a free
read.

## The decision rule

Before any platform number leaves your mouth, find its denominator and find its primary document. If the
denominator excludes the cases that failed, or the figure only exists as a recital on a blog post, it is a
brochure and not evidence.

## Quiz

Drop your answers in `_answers-inbox.md`.

1. Meta prints a 31% median undervaluation and a 1.45X minimum multiplier. Why is it wrong to present them as
   two findings that agree?
2. The 46% lift figure rests on 37 studies. What does the footnote remove from that count, and what does the
   number mean once you put it back?
3. AT-139 is T1, the top tier, and the lesson says it is still unusable on our accounts. What does the tier
   actually measure?
4. A client sends you a competitor's case study: "switching to incremental attribution lifted ROAS 3.3X across
   our top cell." You have the one-page PDF and nothing else. Write the two questions you ask before the number
   is allowed into your own report, and say what each answer would have to be for you to use it.
5. Phoenix Truxx statics ran at $12.72 per Ads Manager lead last week. A junior buyer applies Meta's 1.45X and
   reports a true cost per lead of $8.77 to the client. Name the three separate things wrong with that sentence,
   and name the one thing we could do this week that would produce a real number instead.

> [!note]- Answer key
> 1. They are one measurement read from both ends. 45 / 145 = 31.0%, so the second figure is the first
>    rearranged. Presenting them together implies two independent sources where there is one.
> 2. It removes every study that found no statistically significant incrementality. The 37 are restricted to
>    studies where lift was detected in at least one cell. Put the nulls back and the honest sentence is "when
>    it works it averages 46%", with the frequency unpublished.
> 3. The tier scores the provenance of the sentence, meaning how directly we read it and from whom. It says
>    nothing about whether the effect transfers to our accounts. Provenance and applicability are two different
>    axes, and only one of them is in the tier.
> 4. Ask what the denominator is, meaning how many cells or tests ran and how many are inside that 3.3X, and ask
>    for the primary document rather than the recital. Usable only if the denominator includes the cells that
>    failed and the figure appears in a source that publishes its method. If either answer is missing, it is
>    colour, not evidence.
> 5. Wrong outcome: the multiplier was measured on purchases, we measure form opt-ins several steps upstream of
>    money. Wrong population: a median over 54 advertisers with no spread, no vertical split and no count of
>    nulls says nothing about one dealership. Wrong direction of certainty: the multiplier is Meta's own floor
>    from its own data, published with no confidence interval and no refresh interval, which AT-022 already
>    records as the unsettled half of that argument. The real move: open the Experiments tab and find out
>    whether our Conversions API accounts qualify for a self-serve Conversion Lift test.
