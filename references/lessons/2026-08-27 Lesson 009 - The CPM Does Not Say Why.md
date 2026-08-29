---
title: "Lesson 009 - The CPM Does Not Say Why"
type: lesson
lesson: 9
topic: Auction Mechanics & Bidding
source: harvest 2026-08-27 second pass (AU-082 new T4; AU-080, AU-024, AU-003, AU-071, MM-176)
created: 2026-08-27
updated: 2026-08-27
tags: [advertising-science, lesson, auction, bidding, cpm]
---

# Lesson 009 · The CPM Does Not Say Why

**If you only answer two questions, answer Q4 and Q5.** Eight lessons have gone out. The inbox has come back empty eight times. Two answers is a real submission.

This morning's research pass banked a claim that inverts something we do most weeks: it says a rising CPM on a winning ad set is the machine repricing you upward because you are winning. It is T4, from a source that earned a reliability warning in the same pass. So instead of teaching it, I went and checked it against our own filed numbers. **We have six weeks of CPM and cost per lead sitting side by side on one account, and the answer is better than the claim.**

## 1. The mechanism

Under a conversion or lead objective, the thing you are buying is conversions. Meta decides what each impression is worth to you before it charges you for it.

Meta's auction equation has three factors: your bid, the estimated action rate, and ad quality. The estimated action rate is the probability that showing this ad to this person produces the outcome you asked for. So the price of putting your ad in front of one person is set by how likely Meta thinks that person is to do the thing.

Two consequences follow, and they point opposite ways.

Someone more likely to convert costs more. So a CPM going up can mean Meta started showing your ad to better people.

Someone less likely to convert costs less. So a CPM going down can mean Meta started showing your ad to worse people.

Think about a corner shop whose electricity bill jumps 40% in a month. Three explanations fit. The tariff went up. Somebody left the storeroom light on all month. Or the owner bought a freezer, and the shop is now selling cold drinks all summer. The bill alone cannot tell you which. You divide the bill by what the shop sold.

The CPM is the bill. Cost per lead is the bill divided by what it produced.

## 2. The evidence

**The documented part is small, and it is worth knowing exactly how small.**

- **AU-001, T1, active.** Meta's own help centre: the auction winner is the ad with the highest total value, built from bid, estimated action rate and ad quality. This is a live page and it is citable.
- **AU-002, T1, active.** "An ad that's more relevant to a person could win an auction against ads with higher bids." Relevance is a bid. Better creative is the cheapest way to lower what you pay.
- **AU-071, T1, with a permanent warning attached.** For a conversion-optimised ad, estimated action rate breaks down into estimated click-through rate times estimated click-to-conversion rate. **Meta withdrew that document.** What we have is a third-party mirror somebody saved. Say that every time you cite it, because it can never be re-verified against Meta.

That is all the documentation there is. Everything below is an operator talking.

**Four people read a rising CPM four different ways. None of them tested it.**

- **AU-082, T4, banked this morning.** The repricing story. "The expected conversion rate on the campaign now goes up and now Meta might expect from you a 5% conversion rate because that's what you've been hitting. So it reweights all of its bidding models and it now starts to come into auctions more aggressively. And what happens? Your CPMs go up."
- **AU-024, T3, contested.** Andrew Faris, from 100+ managed accounts, and Meta's own CMO: the auction moved onto more valuable people, and the price is the pricing working correctly. Faris: "the problem's not the CPM, the problem is your performance."
- **AU-003, T3.** Charley T, in the opposite direction: a rising prospecting CPM means the creative stopped earning cold attention, so the ad has quietly become a warm-audience ad no matter what the targeting says.
- **AU-019 and AU-070, T3.** A narrower pool costs more. Exclusions and tight segments raise CPM by shrinking who is eligible, with no verdict on the creative at all.
- **AU-075, T4, filed as folklore.** That Meta charges you a penalty for repetition past frequency 3 or 4. It is recorded so nobody re-derives it. Meta does not watch for repetition and fine you. Delivery narrows onto a smaller pool and a smaller pool clears at a higher price.

Five readings, one number. AU-024's own entry says it plainly: neither side ran that test.

**Three guards on the new claim, and they are the reason it is teaching material rather than a rule.**

It is **T4**. He cites one unnamed on-screen paper he himself calls a "theoretical analysis". No platform documentation, no test, no account.

**His own worked example breaks his own formula.** He prices a 10%-probability person at a $90 CPM and a 0.5%-probability person at $7. The probability ratio is 20x. The CPM ratio is 90 / 7 = 12.86x. Back-solve the outcome value from each and you get $900 from one and $1,400 from the other, 55.6% apart. Under his own equation the 10% person should price at $140. Never quote the $90 / $7 pair.

And **MM-176 went into the codex this morning about this exact channel.** Twelve of his transcripts were read, 28 headline figures recomputed, and a large share failed, including a sign error narrated on camera with a calculator open: "280 - 104 - 80 - 108 and we are officially at $12,000 in profit" computes to minus $12,000.

**Now the one thing in this whole family that is arithmetic instead of opinion.**

AU-080 banks two identities and both recompute cleanly. Cost per click is CPM divided by 1,000, divided by click-through rate. Cost per acquisition is cost per click divided by conversion rate. Chain them:

> **cost per lead = CPM ÷ (1,000 × CTR × conversion rate)**

Check it on round numbers. A $10 CPM, 2% click-through, 10% form conversion. A thousand impressions cost $10, produce 20 clicks, and 20 clicks at 10% produce 2 leads. Five dollars a lead. The formula gives 10 ÷ (1,000 × 0.02 × 0.10) = $5.

**That identity is the lesson.** The CPM is one of three terms. A CPM rise costs you nothing if the other two absorb it. And the competing stories each predict a different absorber:

| If the story is | CTR does | Conversion rate does | Reach does | Cost per lead does |
|---|---|---|---|---|
| Repricing onto better people | little | rises | holds or shifts | holds or falls |
| Creative stopped earning attention | falls | little | holds | rises |
| Delivery narrowed onto a small pool | can rise | little | falls, frequency climbs | rises |

One caution on the middle column. AU-066 says a click-through rate can climb simply because delivery narrowed onto a smaller, keener pocket. So read reach beside CTR, always. A CTR jump on falling reach is a contraction wearing a performance costume.

## 3. Our accounts

**We already ran this test. Nobody noticed, because the two numbers sit in different rows of the same table.**

StayWell in Novi is the only account with a long run of CPM and cost per lead filed for the same window. Six weekly reports carry both. Every one of the twelve percentage changes below was recomputed against its own two figures before it went in this lesson, and **all twelve hold.**

| Window | CPM | Cost per lead | Same direction? |
|---|---|---|---|
| Jun 6 to 13 | $26.62 → $34.07, **+28%** | $9.58 → $13.32, **+39%** | yes |
| Jun 21 to 27 | $40.16 → $38.40, **-4.4%** | $20.56 → $8.16, **-60.3%** | yes |
| Jun 29 to Jul 5 | $36.95 → $29.69, **-19.7%** | $9.40 → $20.35, **+116.5%** | **no** |
| Jul 3 to 9 | $29.69 → $29.11, **-2%** | $20.35 → $15.46, **-24%** | yes |
| Jul 10 to 16 | $29.11 → $32.93, **+13%** | $30.91 → $20.73, **-33%** | **no** |
| Jul 17 to 23 | $32.93 → $32.17, **-2.3%** | $20.73 → $26.97, **+30.1%** | **no** |

Two of those windows overlap each other by three days, so take the five that do not: Jun 6 to 13, Jun 21 to 27, Jun 29 to Jul 5, Jul 10 to 16, Jul 17 to 23.

**The CPM and the cost per lead moved in opposite directions in three of those five weeks.**

Read the two that matter most.

**Jul 10 to 16 is AU-082's story happening on our own account.** The CPM rose 13% and the cost of a lead fell 33%. Impressions got dearer and leads got cheaper in the same week. Anyone watching the CPM alone would have called that fatigue and pulled the creative. It was the best week in the arc.

**Jun 29 to Jul 5 is the exact inverse, and it happened on two accounts at once.** StayWell's CPM fell 19.7% while its cost per lead more than doubled, and the report read it correctly at the time: "delivery got cheaper and wider, attention held, conversion broke." The same week on SJR Commercial, the van engine's CPM fell while its cost per lead rose 107%, $1.69 to $3.50. Phoenix Truxx did it the following week: CPM down 13.9% to $25.48, cost per lead up 22.8% to $9.11, and that report also called it right, "friendly auction, which makes leaving statics off more expensive."

So on our own book, **AU-082's companion rule is the half that keeps firing.** Cheap impressions turned out to be cheap because the people behind them were worth less, three times, on three accounts. Its headline half has exactly one instance, StayWell in mid-July.

**One more thing worth more than either, from the same SJR week.** SJR's blended CPM rose 20.6% that week, $16.18 to $19.51. Neither engine's price moved much. Dump ran $13.58 and van ran $29.19, and the van costs 2.15x the dump. What actually happened is that the budget split moved from 40% van to 57% van. **The blended CPM rose because the money moved to the expensive engine. The price of each engine barely moved.** A blended CPM is an average over engines that were never priced alike, which is the reading habit AU-082 states plainly and the reason law 11e says to read at the level that holds the budget.

**Two corrections that came out of checking, and both belong to us.**

That same SJR report describes the dump CPM as "flat" and the van CPM as "down 10%", against a baseline it names itself, Jun 21 to 27. Against that baseline the dump CPM rose **7.95%** and the van CPM fell **7.10%**. The report's conclusion, creative wear, survives both, because the van's cost per lead rose 107% against a CPM that fell. The adjectives do not survive. Nobody should re-quote "the auction is fine" from that week without those two numbers attached.

**And the gap. ChiroWorks has no CPM recorded anywhere.** Not in `_HOT.md`, not in the timeline, not in any report. Its refresh trigger is frequency, at 2.7. StayWell's own hot file already warns that trigger is unreliable: "DON'T wait for frequency 2.5 to refresh creative; the Jun 29 to Jul 5 week proved conversion can halve at frequency 2.1 on a stale roster." That is the same week in the table above. **On the account where we do log the number this lesson is about, the CPM was pointing the wrong way. On ChiroWorks we do not log it at all.**

## 4. The decision rule

**Never act on a CPM by itself. Pull CPM, click-through rate, form conversion rate, reach and cost per lead for the same window at the level that holds the budget, and act on whichever one actually moved.**

If cost per lead is flat or falling, a rising CPM is not a problem you have. If cost per lead is rising while CPM falls, the creative or the form broke and no amount of bidding work will fix it.

## 5. Quiz

Drop answers in `lessons/_answers-inbox.md`. Lesson number plus your answers. Partial is fine and still gets graded.

1. Name the three factors in Meta's auction equation, and say which one your creative moves.
2. AU-082 is tiered T4. Say what T4 means in this codex, and give two specific reasons this claim cannot decide anything on its own.
3. **Applied.** An ad set runs an $18 CPM, a 1.2% click-through rate and a 25% form conversion rate. Work out the cost per lead. The next week the CPM is $24 and the form conversion rate is 34%, with click-through unchanged. Work out the cost per lead again. Say what you do on Monday.
4. **Applied.** A Spanish dump ad set on SJR shows its CPM up 30% week over week. Give three different explanations that all fit that number, and for each one name the column you would pull and what it would have to show for that explanation to be the right one.
5. **Applied.** Somebody proposes an automated rule: pause any ad whose CPM rises more than 30% week over week. Using the StayWell table in section 3, say what that rule would have done to the account, and name the one number the rule is missing.

> [!note]- Answer key
> **1.** Bid, estimated action rate, and ad quality (AU-001, T1). Creative moves the estimated action rate, and it also moves ad quality. Full marks for adding AU-002's consequence, that a more relevant ad can beat a higher bidder, which is why creative is the cheapest lever on what you pay.
> **2.** T4 is theory. An idea, nothing more. It never decides. Two reasons out of three: the source cites one unnamed paper he calls a "theoretical analysis" with no platform documentation and no test; his own worked example breaks his own formula (a 20x probability ratio against a 12.86x CPM ratio, back-solving to $900 and $1,400 for the same outcome value); and MM-176 put a source-reliability warning on that channel the same morning, after 28 recomputed figures with a large share failing, including a sign error on camera.
> **3.** First week: 1,000 impressions cost $18 and give 12 clicks, and 12 clicks at 25% give 3 leads. **$6.00 a lead.** Formula: 18 ÷ (1,000 × 0.012 × 0.25) = $6.00. Second week: 12 clicks at 34% give 4.08 leads, so 24 ÷ 4.08 = **$5.88 a lead.** **The CPM rose 33.3% and the cost of a lead fell 2%.** On Monday you leave it alone and you do not refresh the creative. Extra credit for saying you would check reach before celebrating, because a conversion-rate jump on collapsing reach is a different story.
> **4.** Any three of: **repricing onto better people**, check form conversion rate, which has to be rising, and cost per lead, which has to be flat or falling. **Creative stopped earning cold attention**, check click-through rate, which has to be falling, with cost per lead rising. **Delivery narrowed onto a smaller pool**, check reach, which has to be falling, with frequency climbing. **A mix shift**, check the budget split across ad sets, because a blended CPM rises on its own when money moves from a cheap engine to an expensive one, exactly as SJR's did in the Jun 29 to Jul 5 week. Also accept an audience or exclusion change, per AU-019 and AU-070. Full marks needs the column named, not just the story.
> **5.** **It would have done nothing at all.** No week in the table clears +30%. The three rises are +28%, +19% and +13%. So on six weeks of real money the rule never fires once, and a rule that never fires is not a safeguard. Now drop the threshold to catch the rises and it gets worse: at +25% it fires on Jun 6 to 13 and gets that one right by luck, at +10% it also fires on Jul 10 to 16 and Jul 10 to 12, and **both of those are weeks where the cost of a lead fell 33% and 44%.** The missing number is **cost per lead**. Full marks for the last step: the three weeks the account genuinely got worse are Jun 6 to 13, Jun 29 to Jul 5 and Jul 17 to 23, and in two of the three the **CPM fell**. A rule watching for CPM rises sits silent through the damage and pulls the trigger on the wins.

---

Related: [[2026-08-24 Lesson 007 - Hook Rate Ranks the Wrong Ad]], which is the same mistake one metric earlier in the chain. [[2026-08-18 Lesson 002 - The Attribution Column Is an Instrument]] on reading a number as the output of a model. Laws 4, 4f and 11e in the skill file. Law 4f is new today and it was written from the table in section 3, so the account series above is now the law rather than an illustration of one. The full claim, with its limits, is AU-083 in the codex.
