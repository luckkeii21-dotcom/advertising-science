---
title: "Lesson 021 - The Offer Changed, the Prediction Did Not"
type: lesson
lesson: 21
date: 2026-09-09
topic: Auction Mechanics & Bidding
claims: [AU-089, AU-086, AU-087, AU-088, AU-083, AU-071, AU-001, AT-109]
tags: [advertising-science, lesson]
---

# Lesson 021 · The Offer Changed, the Prediction Did Not

🎬 Video: [[video/2026-09-09-lesson-021.mp4]]

Three days ago ChiropracticWorks changed the invisa-RED offer from a free consultation to a $49 introductory session. Meta has not been told. Meta cannot be told. This lesson is about what happens in the gap.

## 1. The mechanism

Meta decides who sees your ad by predicting two things about each person: how likely they are to click, and how likely they are to convert once they click. That is not folklore. It is [[Auction Mechanics & Bidding#AU-001|AU-001]], Meta's own help centre, and [[Auction Mechanics & Bidding#AU-071|AU-071]], a Meta document that spells the second half out as estimated click-through rate times estimated click-to-conversion rate.

Both predictions are built from what already happened. That is the entire point of them. A prediction that lurched every time five clicks converted would be useless, so Meta deliberately regresses small samples against a much larger set and refuses to reprice off a handful of results.

**That refusal is worth having in an ordinary week and it is exactly what fails when the offer changes.** A price change moves the real conversion rate as a step, on one day, at one hour. The prediction moves as a slow drift over the days that follow. In between, Meta is buying impressions at a price justified by an offer that no longer exists.

The analogy that actually maps: a thermostat working off a reading it took before you opened the window. The thermostat is not broken. It is doing precisely what it was built to do, using a number that stopped being true. And it will not tell you how stale the number is, because that is not a field it exposes.

Two failures come out of one cause, and they point in opposite directions.

- **The offer gets easier** (a discount, a free version). Meta underdelivers. It still thinks clicks are expensive to convert, so it buys cautiously and hands you an efficiency you did not ask for, with the volume you cut price to buy left unbought.
- **The offer gets harder** (a price appears, a qualifier appears). Meta overdelivers. It still thinks the click converts at the old rate, so it keeps paying old-offer prices for traffic that now converts worse.

ChiroWorks is in the second one, starting 6 September.

## 2. The evidence

The mechanism was banked yesterday from Andrew Faris, in [[Auction Mechanics & Bidding#AU-086|AU-086]] (T3), with [[Auction Mechanics & Bidding#AU-087|AU-087]] and [[Auction Mechanics & Bidding#AU-088|AU-088]] beside it. Read the tier honestly: one operator, no account data shown, and he says on camera that his figures are invented for illustration.

**Read the scope even more honestly, because it is the interesting part.** All three claims are about manual bids. Faris is describing a cost cap breaking during a sale. We hold no cost caps and no bid caps. Across every filed export that carries the column, 344 ad rows over five windows on ChiroWorks and SJR, every single row reads `Bid 0` and `Bid type ABSOLUTE_OCPM`. That is lowest cost with no manual bid, everywhere, on every ad. Phoenix Truxx and StayWell exports do not carry the column, so their bid configuration is unread rather than confirmed.

So a literal reading says the claim does not touch our book at all.

**It touches our book through a different door.** The prediction is not a property of the bid. AU-071 puts it inside the estimated action rate, which is a term in the auction whether or not you ever set a bid. A cost cap does not create the stale prediction. It just gives the stale prediction something to bump into, and something you can see. Take the cap away and nothing is fixed. The ad set now spends its full share of the budget no matter what the prediction believes, and the entire cost of being wrong lands in one column: cost per opt-in.

That is worse for us. A cap fails loudly. Lowest cost fails quietly, in a column we already stare at every week and already have three other explanations for.

Banked today as [[Auction Mechanics & Bidding#AU-089|AU-089]].

## 3. Our accounts

ChiroWorks runs one CBO recorded at $66/day since 21 July. invisa-RED is the ad set inside it that spends. Here is what it did across the three consecutive windows on file, rebuilt from the raw weekly-report exports rather than from any summary:

| Window | Spend | Impressions | Clicks | Opt-ins | CPM | CTR | Click to opt-in | Cost per opt-in |
|---|---|---|---|---|---|---|---|---|
| 8-16 Aug | $507.52 | 17,811 | 171 | 14 | $28.49 | 0.96% | **8.19%** | **$36.25** |
| 17-23 Aug | $320.54 | 10,088 | 91 | 8 | $31.77 | 0.90% | **8.79%** | **$40.07** |
| 24-30 Aug | $315.33 | 11,156 | 93 | 7 | $28.27 | 0.83% | **7.53%** | **$45.05** |

Cost per opt-in rose 24.3% across those two ends. [[Auction Mechanics & Bidding#AU-083|AU-083]] gives the identity that splits it: cost per opt-in equals CPM divided by (1000 × CTR × conversion rate). Run it and the three terms come apart cleanly.

- CPM did **nothing**. $28.49 to $28.27, a 0.8% fall.
- CTR carried most of it. 0.96% to 0.83% multiplies cost per opt-in by **1.152**.
- Click to opt-in carried the rest. 8.19% to 7.53% multiplies it by **1.088**.

0.992 × 1.152 × 1.088 = **1.2426**, and the measured ratio is 1.2426. The decomposition is exact, not approximate.

Frequency rules out the fourth explanation: every invisa-RED ad with real spend in the last window sat between 1.19 and 1.55, and the top ad reached 5,207 people against 5,280 in the first window. The pool is not narrowing. This is creative wear on the click side plus a smaller drift on the conversion side, and it is the signature AU-083 already names.

**Now the part that has no data behind it yet, which is why this lesson is today rather than next week.**

The last filed ChiroWorks export ends **30 August**. The 4 September weekly run pulled Phoenix, SJR and StayWell and produced no ChiroWorks folder at all. The offer changed on **6 September**. So there is a clean pre-change week, 31 August to 5 September, that nobody has pulled and that is still sitting in Ads Manager. It is the last honest reading of the free offer that will ever exist.

Pull it this week and the account owns a before-and-after on a dated, single-variable change, which is the cheapest T2 available to us anywhere right now. Leave it and the two states blur into one trend line and the change becomes unmeasurable forever.

**The second thing, and it is a risk rather than a measurement point.** The offer change is half shipped. Twenty-five files on disk mention invisa-RED and still carry free-consultation language, and the newest of them is dated 14 August. That set includes the live lead-form document, the final image-ad copy, the v2 launch copy and the winning-video copy deck. What is actually live in the ad account cannot be read from here, because the Meta connectors are unauthorised in this session, so treat the live state as unverified rather than as broken.

If any live ad still promises free while the form charges $49, click-to-opt-in does not drop by the price. It drops by the contradiction, and it drops harder. That failure already has a name in this account: on the 8-16 August window we lost a confirmed opt-in, Lisa, to exactly this mismatch running the other way, when the ads said free and the voice agent quoted $49.

**And the confound nobody has scheduled around.** The 25 August decision to split invisa-RED into its own campaign is still unshipped, fifteen days on, and [[2026-09-08 Lesson 020 - Which Side of the Split Do You Move|yesterday's lesson]] flagged its direction as backwards. If that split ships in the same fortnight as the price change, two large changes land on one ad set inside one window and neither can be read. That is the Phoenix Truxx Video02 problem repeating: two causes, four days, nothing settled.

Ship them in an order. The price change is already live and cannot be un-shipped, so it goes first and gets a clean two weeks. The split waits.

## 4. The decision rule

**An offer change is a dated event, so write the date down and capture click-to-opt-in on both sides of it. Delivery keeps buying against the old offer for days afterwards, and the bill arrives in the cost-per-opt-in column disguised as creative fatigue.**

The tell that separates them works on columns we already export: creative wear moves **CTR**, an offer change moves **click-to-opt-in** and leaves CTR alone, because the price is invisible until the form opens. One caveat, and it is the one that bites: this only holds if the ad copy itself did not change. Rewrite the primary text on the same day you change the price and you have broken your own instrument.

## 5. Quiz

Five questions. Put answers in `_answers-inbox.md`, any format, partial is fine.

**Q1.** AU-086, AU-087 and AU-088 are all about manual bids, and 344 of 344 filed ad rows on our book run `Bid 0 / ABSOLUTE_OCPM`. Explain in two sentences why the mechanism still reaches us, and name the claim that says the prediction exists independently of the bid.

**Q2.** *(Applied.)* Two weeks from now the invisa-RED ad set files this window: CPM $29.10, CTR 0.84%, click to opt-in 4.10%, cost per opt-in $84.60, frequency 1.4, reach flat. Using the AU-083 identity, name which term moved and by how much, say what caused it, and say what you would do about the budget on Monday morning.

**Q3.** *(Applied.)* Kartik wants the invisa-RED split shipped this week because it has been open since 25 August. The price changed 6 September. Make the case for the order you would ship them in, say what specific measurement each order destroys or preserves, and name the one date you would put in the vault either way.

**Q4.** Argue the opposite. Build the strongest case that the cost-per-opt-in rise after 6 September has nothing to do with the price, using claims already in the codex. Then name the single exported column that would kill your own argument, and say which way it would have to move.

**Q5.** Our transfer of AU-086 to lowest-cost lead gen is banked at AU-089. What tier does it deserve today, and what exactly would have to be captured for it to become a T2 with our own numbers? Be specific about the windows and the columns.

> [!note]- Answer key
>
> **Q1.** The prediction sits in the estimated action rate, which is a term in the auction for every ad regardless of bid strategy. **AU-071** (T1, carrying the withdrawn-mirror provenance warning) decomposes it into estimated CTR times estimated click-to-conversion rate, and **AU-001** (T1, live help centre) confirms estimated action rate is one of the three auction factors. A cost cap does not create the stale prediction, it only gives it a visible edge to break against. Full marks for adding that removing the cap makes it worse rather than better, because the ad set then spends its full share regardless and the whole error lands in cost per opt-in.
>
> **Q2.** CPM moved +2.9% ($28.27 to $29.10), CTR moved +1.2% (0.83% to 0.84%, effectively flat), click to opt-in **collapsed 45.6%** (7.53% to 4.10%). Multipliers: 1.029 × 0.988 × 1.837 = **1.868**, and $45.05 × 1.868 = $84.16 against the stated $84.60, so the identity accounts for essentially all of it. CTR flat and frequency flat rules out creative wear and pool narrowing. **This is the offer, and it is the signature from section 4.** Monday morning: do not cut the budget as a reflex, because the number is doing what a price change does and $84 may still be cheap for a buyer who has already paid $49 and is far more likely to show. Check the show rate and the closed value on the post-6-September cohort before touching spend. Half marks for a correct decomposition with a budget cut attached and no cohort check, because that is the trap this whole lesson is about. Zero marks for calling it fatigue.
>
> **Q3.** Price first, split second, and the price change already shipped, so the real decision is only whether to hold the split. **Holding the split preserves** a single-variable read on the price, which is the cheapest T2 available on this account and the only shown evidence for AU-089 anywhere. **Shipping the split now destroys it**, because on Meta an ad set cannot be moved between campaigns, only duplicated, so the moved side re-enters learning and the resulting cost-per-opt-in change has two causes in one window. **GP-032** also says this particular split is pointed the wrong way, and at roughly $34/day per half neither campaign clears learning, so the split is questionable on its own merits before the confound is counted. The date for the vault is **6 September 2026**, recorded against the invisa-RED ad set, with delivery status and daily budget captured on that date. Credit for anyone who also says to pull the 31 August to 5 September window before it gets harder to isolate.
>
> **Q4.** The strongest opposing case is built on what the three filed windows already show. Cost per opt-in was rising **before** the price changed, $36.25 to $40.07 to $45.05, and the decomposition puts most of that on CTR, which is creative wear under **AU-083**. The same ads have been live since mid-August. **AT-109** shows this account has already lost its cheapest ad set to displacement rather than to fatigue, so a structural cause is live here too. AU-083 itself proves CPM and cost per lead move in opposite directions on our own book, so no single column reads cleanly. A rise after 6 September could be the same trend continuing, and the date could be a coincidence. **The column that kills it is click-to-opt-in.** If it holds near 7.5% to 8.8% while CTR keeps falling, the opposing case wins and it is creative. If it steps down hard while CTR sits still, the opposing case is dead. Full marks require naming the direction, not just the column.
>
> **Q5.** **T3 today.** The mechanism is transferred from a single-operator T3 with nothing shown, and the lowest-cost half is our own reasoning rather than anyone's measurement. To reach T2 it needs, on one ad set, across a change date nobody else touched: spend, impressions, link clicks, results, CPM, CTR, click to opt-in and frequency, for at least two full windows before 6 September and two full windows after, with the ad copy held constant across all four and delivery status and daily budget recorded on the change date. The 31 August to 5 September window is one of the two "before" windows and it has not been pulled yet. Credit for noting that if the copy changed on 6 September as well, the test is already contaminated and the honest move is to say so rather than to publish the number.

---

**Related:** [[Auction Mechanics & Bidding]] · [[2026-09-08 Lesson 020 - Which Side of the Split Do You Move]] · [[2026-08-27 Lesson 009 - The CPM Does Not Say Why]] · [[2026-08-24 Lesson 007 - Hook Rate Ranks the Wrong Ad]] · [[ChiroWorks]]
