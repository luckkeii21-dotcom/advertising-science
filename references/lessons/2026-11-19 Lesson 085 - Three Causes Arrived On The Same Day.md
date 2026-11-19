---
title: "Lesson 085 - Three Causes Arrived On The Same Day"
type: lesson
created: 2026-11-19
tags: [advertising-science, lesson, learning-phase, signal, scaling, meta]
lesson: 85
topic: Learning & Signal
---

# Lesson 085 - Three Causes Arrived On The Same Day

Video: `video/2026-11-19-lesson-085.mp4`

## The mechanism

You raise a budget. Results get worse for a day or two, then come back. Every media buyer alive has seen that
curve and every one of them has a reason for it. The reasons do not agree.

On Monday you change three things at once. New diet, first run in a year, eight hours of sleep instead of five.
Tuesday you feel terrible. Friday you feel great. Which one did it? Nothing in how you feel can answer that.
The curve has one shape and three authors, and no amount of staring at it separates them.

Three published explanations for the post-raise dip. They predict the same first few days.

**One, the learning reset.** Meta documents a list of edits that always reset learning, and budget sits in a
second group that resets only if the change is large. Its own illustration is $100 to $101 for no reset and
$100 to $1,000 for a likely one. Where the line sits between those is not published and not discoverable from
outside.

**Two, audience expansion.** A raise forces Meta to widen the pool, so the extra impressions land on people
seeing you for the first time. Two penalties arrive together: a group less likely to buy, and a group that has
not been through a full exposure cycle yet. On this account the dip is expected and healthy, so a bad day two
is not evidence the raise was wrong.

**Three, funnel fill.** The ramp operators call learning may be people moving through a normal consideration
window. Nothing is learning. The pipeline is just filling.

Here is the part worth keeping. **If two mechanisms predict the same curve, the curve is not evidence for
either one.** You could watch that dip every month for a year and know nothing more about its cause than you do
today.

What does separate them is what happens after the recovery. The reset story predicts you get back to the old
cost per lead, because the ad set only has to relearn something it already knew. The audience story predicts
you never fully get back, because the audience is genuinely worse now, and $200 a day does not come back to the
cost it had at $50. One says the dip is a fee. The other says the dip is a down payment on a permanent new
floor. That difference is the entire scaling question, and nobody on our side has measured it.

## The evidence

- [[Learning & Signal#LS-002|LS-002]], **T1**. The six always-significant edits. Adding a new ad to an ad set
  is on that list, with no size condition attached.
- [[Learning & Signal#LS-003|LS-003]], **T1** for the core, **T3** for everything useful. Meta documents that
  a budget threshold exists and never locates it. The 3% a day and the 100% step figures come from one
  operator's managed book, not a test.
- [[Learning & Signal#LS-088|LS-088]], **T4**. The audience-expansion mechanism. Read why it is T4: no cohort
  read, no first-impression versus repeat-impression split, no account, no numbers anywhere in the source. It
  is a good story told by a credible person.
- [[Learning & Signal#LS-072|LS-072]], **T4**. Funnel fill plus time to purchase as the real ramp.
- [[Scaling Models#SC-001|SC-001]], **T3, contested**. Safe step size, prescriptions from 5% to 20% a day to
  "the 20% rule is folklore."
- [[Scaling Models#SC-176|SC-176]], **T3**. Strip algorithmic remarketing out of a result before calling an
  ad set scalable, because a remarketing-carried result dips hardest when you widen it.

Notice the shape of the board. **The trigger list is T1 and the causes are T4.** We know with documentation
what resets learning. We do not know, at any decent tier, why performance falls when it does. So a T4 mechanism
never carries a client decision on its own, and it never goes in a report as the reason.

## Our accounts

Phoenix Truxx, 11 November. Real numbers from Marketing OS, data through 17 November.

We split the budget by truck type. The dump campaign started a six-day ladder from $48 to $140 a day, a **2.92x
raise** in steps of about 20%. The statics campaign stepped down from $120 to $30. Then on 12 November, eight
Spanish image ads went live **into ad sets that were already running**.

The curve:

| Date | Spend | Form leads | Cost per form lead |
|---|---|---|---|
| 11 Nov | $236.78 | 14 | $16.91 |
| 12 Nov | $206.06 | 8 | $25.76 |
| 13 Nov | $213.06 | 20 | $10.65 |

Day two was **52% more expensive per form lead** than day one. Now count the candidate causes sitting on that
same day. A budget step on the dump campaign. New ads dropped into live ad sets, which is a documented reset
trigger at any size. A widened audience from the step itself. Three authors, one curve, and our account cannot
tell you which one wrote it.

What the fuller window says, and it is good news. Five days before, 7 to 11 November: $992.38, 72 form leads,
**$13.78 each**. Six days after, 12 to 17 November: $1,278.99, 103 form leads, **$12.42 each**. We recovered and
went past the old number.

The honest limit on that comparison. **The mix changed inside the window.** Dump went from $48 to $140 a day
while statics went from $120 to $30, so a cheaper average after the raise may be a different campaign carrying
more of the spend rather than the same campaign recovering. Composition first, then rates. The one thing the
numbers do settle is the panic reading: nobody should have paused anything on 12 November.

Also worth saying plainly. The Ads Manager change log returned **nothing** for this account across twelve days,
so every change date above comes from our own launch record. Our record is the only audit trail we have.

**The free move nobody has run.** Pick an ad set that is not in learning, raise only its budget, add no ads, and
read whether the dip still appears. If it does, the reset was never the cause. That test costs one budget edit
and it would move LS-088 off T4 using our own book. It joins the unowned-check list.

## The decision rule

Write down what you changed and on which day **before** you read the curve, because a dip with three authors is
not evidence about any one of them, and the only way to get evidence is to change one thing at a time.

## Quiz

Drop your answers in `_answers-inbox.md`.

1. Name the three published explanations for the dip after a budget raise, and say which tier each one sits at.
2. "If two mechanisms predict the same curve, the curve is not evidence for either." Explain what that rules out
   in practice.
3. The reset story and the audience-expansion story make different predictions about the recovery. State both,
   and say why the difference matters more than the dip does.
4. Phoenix went from $13.78 per form lead in the five days before 11 November to $12.42 in the six days after.
   Lucky wants to put that in the client report as proof the budget split worked. Say what you check first, and
   what you would actually write.
5. SJR's dump campaign is at $60 a day and holding a cost per lead the client is happy with. You have four new
   Spanish ads approved and a mandate to take the campaign to $120 a day this week. Lay out the order you do it
   in, and say what you give up by choosing that order.

> [!note]- Answer key
> 1. Learning reset, LS-002 at T1 for the trigger list and LS-003 at T1 for the documented-but-unlocated budget
>    threshold. Audience expansion to first-time viewers, LS-088 at T4. Funnel fill plus time to purchase,
>    LS-072 at T4. The trigger list is documented and both causal stories are the weakest tier on the board.
> 2. It rules out learning anything about cause by watching the dip. Shape of curve, depth of dip, length of
>    recovery: none of it discriminates, because all three mechanisms produce the same first few days. The only
>    route to evidence is changing one input at a time, or finding a case where the predictions diverge.
> 3. The reset predicts full recovery to the old cost per lead, since the ad set relearns something it already
>    knew. Audience expansion predicts partial recovery and a permanent new, worse floor, since the pool itself
>    is worse. It matters more because the dip is a few days of money and the floor is the ceiling on the whole
>    account. If the audience story is right, SC-001's ceiling is real economics and not a settling artefact.
> 4. Check composition before rates. The dump campaign nearly tripled its daily budget in that window and
>    statics dropped from $120 to $30, so the blended cost per lead moved partly because a different campaign is
>    carrying the spend. Pull cost per lead per campaign on both sides of 11 November before claiming anything.
>    Also note that eight new Spanish ads launched on 12 November, so the split is not the only change. Write
>    the result honestly: leads went from 72 in five days to 103 in six at a lower blended cost, the direction is
>    good, and a per-campaign read is needed before crediting the split.
> 5. Add the four ads first, in their own new ad set, and let the budget sit still. New ads in a live ad set is a
>    documented reset at any size, so pairing it with a step guarantees you cannot read either one. Hold a few
>    days, read it, then ladder the budget in steps with no creative changes. What you give up is speed: you will
>    not be at $120 by the end of the week, and a new ad set does not inherit the old one's accumulated
>    learning. You buy a readable result with calendar time.
