---
title: "Lesson 039 - The Same End State Has Two Prices"
type: lesson
lesson: 39
date: 2026-09-28
topic: Google PMax & Shopping
claims: [GP-033, GP-035, GP-044, GP-014, GP-036, SC-006, LS-004, LS-025, AT-109, AT-107]
video: video/2026-09-28-lesson-039.mp4
tags: [advertising-science, lesson, google-pmax-shopping, structure, learning-phase, step-size]
---

# Lesson 039 · The Same End State Has Two Prices

🎬 **Lesson video (3m 22s, silent, watch anywhere):** [[video/2026-09-28-lesson-039.mp4]]

A jewellery brand with about 20,000 products tagged every one of them: top, mid, low, zombie.

Then it excluded the low performers and the zombies. About 18,000 products out in one edit. About 2,000 left.

The campaign died.

They turned the 18,000 back on and it came back to life. Then they removed the same products again, this time about 5,000 at a time. The campaign survived and landed on the exact same 2,000 products the single edit had killed it with.

Same end state. Same account. Same products in and the same products out. One route worked and one route did not.

**If you only answer two questions, answer Q3 and Q4.** Q3 is the situation you will actually be in, and the right answer is to do nothing yet. Q4 asks you to argue against this lesson using a claim that outranks every claim in it.

## 1. The mechanism

You run a shop and you want more customers in it.

Route one: make the shop bigger. Same licence, same address, same regulars, same staff who know what people buy.

Route two: open a second identical shop across the road. That shop needs a fresh licence, and the licence gets judged against this year's rules rather than the rules you were approved under. It has no regulars. And every customer it takes on that street is one your first shop was going to get.

Both routes end with more floor space on the same street. They do not cost the same.

Ad platforms work this way too, and the reason is that a platform does not store your intentions. It stores objects. A campaign, an ad set, an asset group, a listing, an ad. Each object carries three things that took time and money to accumulate:

1. **Its record.** What the system has learned about who responds to it.
2. **Its position in the auction.** What it is currently winning, and against whom.
3. **Its approval.** The fact that somebody, at some point, judged it allowed.

Edit an object and it keeps all three. Create a new object and it has none of them. It starts with an empty record, it enters an auction it was not in yesterday, and it goes back through review under whatever the rules are today.

So the question is never only "what do I want the account to look like." It is "what do I want the account to look like, and which route gets there." Those are two separate decisions, and the second one is where the money goes.

## 2. The evidence

This is a Google-heavy lesson because Google is where the cost of the route has been written down most plainly. Every claim below is T3, which matters. Read section 4 before you treat any duration in here as a number.

**GP-033, T3.** The jewellery case above. The evidence caveat is the reason it is not T2: "died" and "came back to life" are the operator's words. No spend, no revenue, no conversion counts, no dates, no chart. What survives the caveat is the structure of the story, because the two routes are their own control. Same operator, same account, same end state, two outcomes. The rule he draws: never remove more than about a quarter of a large catalogue in one edit, and treat a dead campaign after a bulk feed change as recoverable by putting the excluded products back before rebuilding anything. He also reports accounts where even the slow route failed and the weak products had to stay in permanently.

**GP-035, T3.** Structural edits at the asset-group level "destroy campaign performance for like a month". This is the only place in the codex that puts a duration on a Google restructure. The second consequence is the expensive one and it is the one worth memorising: **a performance dip is the worst possible trigger for a restructure.** The restructure costs about a month on top of the dip you are already in, and afterwards the two are impossible to separate in the reporting. You cannot tell whether you fixed the problem, because you added a second problem with the same shape.

**GP-036, T3.** One asset group per $50 of daily spend, and below $50 a day run standard Shopping instead of PMax. Read it beside GP-035 and you get the real instruction: set the container count for the budget you expect to reach, not the budget you have today. Every correction to that count pays the route price again.

**GP-044, T3.** A new Shopping campaign on a new account starts at 2 to 4 impressions a day and then doubles from about day three: 4, 8, 16, 32, 64. Spend sits near a dollar a day for two to three weeks and then ramps. The campaign is not broken. The only thing to watch is whether the doubling is still happening. Touch the titles, the descriptions or the landing pages inside that window and the process restarts. The operator reports his own brands taking 8 to 10 weeks because he kept tweaking titles to speed it up.

**GP-014, T3.** The same warning at a different moment in the account's life. Retitling products is usually right, and a bulk rollover resets learning across every campaign, so roll it out slowly.

**SC-006, T3.** The Meta-side version, stated as a rule: scale an entity in place rather than duplicating it. Duplicating at a higher budget is a workaround for a platform bug, not a scaling method. The specific failure he describes is worth holding: an ad set where 80% of spend went to 2 of 20 ads can, after duplication, give those two proven winners no spend at all.

**LS-025, T4, contested.** The mechanism everything above leans on, that learning accrues at the ad, ad set, campaign and account level at once, so a new object starts all of them at zero. It is T4 because it is asserted architecture with no documentation and no test. Never quote it as the reason. Quote it as the reason the pattern might be true.

**LS-004, T1.** The claim that outranks all of them and cuts this lesson down to size. Read section 4.

**AT-109, T2, ours.** The only measured numbers in this lesson are in section 3.

## 3. Our accounts

Three instances, three different prices, and the prices are not the same size.

### The learning price. SJR Commercial, 2 July 2026.

The client moved the van/dump budget mix toward 70/30 across two shared-budget campaigns. Here is that week, day by day, from the filed report.

| Day (Jun 29 to Jul 5) | Spend | Opt-ins |
|---|---|---|
| Mon | $101.79 | 19 |
| Tue | $107.65 | 19 |
| Wed | $83.17 | 21 |
| **Thu 2 Jul, the edit day** | **$26.62** | **3** |
| Fri | $109.16 | 25 |
| Sat | $85.04 | 20 |
| Sun | $107.71 | 24 |
| **Week** | **$621.14** | **131** |

The six other days averaged $99.09 and 21.3 opt-ins. The edit day delivered 3. That is about 18 opt-ins below the account's own rate for that week, and the money was not spent either, so $72.47 of budget simply did not deliver.

Then read the next line. Friday came back at $109.16 and 25 opt-ins, the highest day of the week.

**So the price was one day.** Not a month. That is the honest read and it is the most useful thing in this lesson.

Two limits on it, and state both every time you quote it. Our own filed report says "likely the restructure day", so the cause is inferred from timing and nothing was held back as a control. And it is one day on one account, which a shared budget can produce on its own without anybody touching anything.

### The auction price. ChiroWorks, 21 July 2026 onward. AT-109, T2.

Somebody wanted more money on a working ad set. They made a copy of it instead of raising its budget. Same creative, same geography, same open targeting, same campaign.

| `All invisa ads \| Open targeting \| Collinsville, IL` | Spend | Opt-ins | Cost | CTR | Click to opt-in | CPM |
|---|---|---|---|---|---|---|
| Up to 26 Jul | $216.12 | 11 | **$19.65** | 0.99% | 16.4% | $32.06 |
| From 27 Jul | $135.66 | **0** | none | 0.97% | **0.0%** | $48.75 |

Then it went dark on its own. $0.00 across both the 8 to 16 August and the 17 to 23 August weeks, status `not_delivering`. The copy went the other way, $58.38 for one and then $203.48 for five.

$19.65 was the cheapest cost per opt-in in that account. It is gone and nothing has replaced it.

Lesson 012 took the statistics rule out of this case, that you judge an ad against its own history and never against its twin. **The part that belongs to today is the route.** The end state that was wanted, more budget behind a winner, was available by editing one field on the original. The route that was taken created a second bidder in the same pool, and the campaign budget settled on the newer object.

The signature tells you which price you are paying, so memorise it. **CTR flat, click-to-opt-in collapsed, CPM up.** The hook kept working at an identical rate. That is not fatigue. That is the ad being pushed onto whoever is left.

### The review price. SJR Commercial, 26 to 27 September 2026. Two days old.

Lucky took over the 26-foot box truck campaign on 26 September. A duplicate of the `26ft-BoxTruck-Program` ad set was rejected on fresh review, while the original kept running on the approval it already had. Same video in both.

The video says "wholesale to the public", quotes "$7,000, $8,000 a week" and says "72 hours" to making money. The original was approved when it was approved. The copy is a new object, so it was read against the standard in force this week.

Two live consequences, and they are decisions rather than observations. The quickest way to put more money behind that campaign is raising the existing budget. And any new ad set built from that video carries a real risk of pulling the original into a re-review it is currently not in.

**This one is not in the codex and not in the client folder.** It is an observation from one account, recorded during the box-truck pass on 27 September. Treat it as a reason to be careful, not as a law, until somebody sees it twice.

## 4. The decision rule

**Change the object you have. A new object pays for its record, its position in the auction and its approval all over again.**

Three guards on it, because a rule with no limits is folklore.

**The durations do not transfer.** GP-035's month is an operator's approximation on PMax asset groups with no recovery curve behind it. Our own only measured instance on Meta cost one day and recovered completely. Carry the direction, never the number. If somebody quotes you a month on a Meta edit, they are quoting a Google claim wearing the wrong badge.

**Meta's own documentation says the learning price is local, and it is T1.** LS-004: normal budget redistribution inside an Advantage+ campaign does not reset learning, a significant edit at the ad-set level does not reset the sibling ad sets, and adding a new ad set to such a campaign does not reset the existing ones. That is the highest-tier claim anywhere in this lesson and it outranks everything in section 2. It means adding a container on Meta does not bill the whole campaign for learning. It also says nothing about the auction, which is where ChiroWorks actually lost the $19.65, and nothing about review.

**Sometimes the new object is the right answer.** LS-004 is also why launching a creative batch into its own ad set is cheaper than injecting it into a working one. AT-107, T3, is blunter: a duplicated ad set never performs like its twin, so an ad-set A/B is not a test. The rule is not "never create". The rule is that creating has a bill, that you should know which of the three prices you are being charged, and that you should not pay it by accident on a Thursday because raising a budget felt too simple.

## 5. Quiz

Drop your answers in `lessons/_answers-inbox.md` with the lesson number. No need to write much.

1. The jewellery account reached the same 2,000-product end state twice, once by a single edit and once in chunks of about 5,000. Given that both routes ended in the same place, what does the case tell you about whether excluding the weak products was the right idea at all?

2. GP-035 says a restructure destroys about a month of PMax performance, and that a dip is the worst possible trigger for one. Explain why the second half follows from the first, in terms of what you can and cannot read in the reporting afterwards.

3. **Applied.** A PMax campaign is on $150 a day with three asset groups. Last week it dipped about 30% and you are fairly sure the asset groups are wrong. What do you do this week, what do you specifically not do, and what would have to be true before you would do the thing you are not doing?

4. **Applied, and argue against the lesson.** Name the claim in the codex that says the learning price of adding a container on Meta is smaller than this lesson makes it sound. Give its tier. Then say what it does not cover, and why ChiroWorks still happened.

5. **Applied.** SJR on 2 July: $26.62 and 3 opt-ins, against about $99 and 21 on the week's other six days, and $109.16 and 25 the very next day. Write the one-sentence version you would be willing to put in front of a client, then name what stops you calling it a measured cost of the restructure.

> [!note]- Answer key
> **1.** It tells you almost nothing about whether the exclusion was right, and that is the point. Both routes ended at the same 2,000 products, so the end state is not what killed the campaign. The route is. The case isolates rate from direction. Worth noting the operator does not resolve this himself: elsewhere in the same conversation he argues weak products actively drag winners down, because the bidder hits its target off the strong ones and spends the surplus testing the weak ones, which is the whole reason to exclude them. He flags the tension and leaves it open. Full credit for saying the case is evidence about step size and silent about direction. Bonus for noticing that some of his accounts never survived the exclusion at any step size, which is direction evidence pointing the other way.
>
> **2.** Because the two costs have the same shape and arrive in the same column. You are already down 30% for a reason you have not found. A restructure adds a second decline, roughly a month long, starting now. Afterwards the campaign is down and you can attribute none of it: not to the original cause, not to the restructure, not to a recovery the restructure is masking. You have destroyed your own ability to read the outcome of your own decision. The corollary is the useful part: a restructure belongs in the roadmap and gets executed in a window where you can afford a month of noise, which by definition is not the week you are panicking.
>
> **3.** Do not restructure. At $150 a day GP-036 puts you at about three asset groups, so the count is not obviously wrong in the first place, and correcting it costs about a month. This week, diagnose in the order the codex ranks the levers: feed first, then brand exclusions, then assets, then the bid, then the signals. Also check whether something definitional moved under you rather than something real. Before a restructure becomes the right call you need two things: a diagnosis that survives the cheaper checks and points at the structure specifically, and a month of tolerance you have said out loud to whoever reads the numbers. Full credit for refusing to act. Extra credit for asking whether the 30% is even real before treating it as a dip.
>
> **4.** LS-004, and it is T1, straight off Meta's own FAQ. It states that budget redistribution inside an Advantage+ campaign does not reset learning, that a significant edit at the ad-set level does not reset sibling ad sets, and that adding a new ad set to such a campaign does not reset the existing ones. That is a higher tier than every other claim in this lesson, and it genuinely narrows the learning price on Meta to the object you touched. What it does not cover is the auction and review. ChiroWorks still happened because nothing in LS-004 stops two ad sets with identical creative, identical geography and identical open targeting from bidding into one pool, with the campaign budget settling on the newer one. The original was never edited. It was outcompeted by its own copy and then stopped delivering. Full credit for separating "learning was not reset" from "the ad set still died".
>
> **5.** Client-facing sentence, something like: on 2 July the account delivered 3 opt-ins against its usual 21 while the budget change went in, and it was back to 25 the next day. What stops it being a measured cost: our own report says "likely the restructure day", so the cause is inferred from timing alone. There is no control, it is one day on one account, and a shared-budget campaign produces quiet days on its own. Full credit for the recovery being inside the sentence, because a one-day stall that recovered is a very different thing to report than a stall, and for not converting the 18 missing opt-ins into a dollar loss. The $72.47 was not spent, so nothing was wasted. What was lost is a day of output.
