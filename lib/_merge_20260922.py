# -*- coding: utf-8 -*-
"""Claim merge for the 2026-09-22 research pass.

Sources read in full today:
  BS  Blue Sense Digital, Black Friday 2026 Strategy (55 min, 11,953 words)
  CT  Professor Charley T, This Facebook Ads Lie is Killing Your Business (32 min, 5,694 words)
  NT  Nick Theriot, How We Helped This Brand Scale To $5M a Year (10 min, 2,118 words)
  SP  Sam Piliero, This is how real businesses scale Facebook Ads FAST (12 min, 2,487 words)
"""
import io
import os
import re

SCI = os.path.join(
    r"E:\claude code marketing skill",
    "Obsidian God-level Marketing Vault", "God-level Marketing", "wiki", "science")

BS = "Blue Sense Digital, Black Friday 2026 Strategy: Spend, Creative, Offers, Pacing, 2026-09-21"
CT = "Professor Charley T, This Facebook Ads Lie is Killing Your Business!, 2026-09-21"
NT = "Nick Theriot, How We Helped This Brand Scale To $5M a Year (It's Boring But It Works), 2026-09-21"
SP = "Sam Piliero, This is how real businesses scale Facebook Ads FAST, 2026-09-20"

NEW = {}
MERGE = []


def add(topic, text):
    NEW.setdefault(topic, []).append(text.strip())


def merge(topic, cid, text, source=None):
    MERGE.append((topic, cid, text.strip(), source))


# ---------------------------------------------------------------- Scaling ----
add("Scaling Models.md", u"""
### SC-163 \u00b7 Pareto BREAKS in the Black Friday window: the bottom 80% of ads hold 54% of spend, and concentration falls as the account gets bigger
Tier: T3 \u00b7 Status: active
The first dataset in this file that disagrees with [[Scaling Models#SC-058|SC-058]]'s compounding-Pareto claim, and it comes from the same operator's own portfolio rather than from an opponent. Pulled from the Meta MCP across what he estimates as **$50 to $100 million of ad spend** over the 2025 Black Friday period.

**Spend held by the top ads, averaged across accounts.** Top single ad **7%**. Top 3 **17%**. Top 5 **23%**. Top 10 **33%**. Top 20 **46%**. So **54% of spend sits in the bottom 80% of ads**, against the 80/20 shape this codex has banked as the normal CBO end state.

**Concentration FALLS as accounts get bigger, which is the half nobody predicts.** Share of spend held by the top 20% of ads, by November spend bracket: under $250k spent, **53%**; the next bracket, **44%**; the largest, **33%**. His mechanism is a ceiling rather than a preference: an individual ad has a maximum daily spend it can absorb (see [[Creative Science#CR-255|CR-255]]), so once an account is pushing past what its winners can carry, the overflow necessarily distributes into the tail.

**The operating consequence, and it is why the slide exists.** It is not only winners that hold up an account in the peak. A plan that funds 12 winners and nothing else leaves roughly half the required spend with nowhere to go. Volume is load-bearing here for a structural reason, not as insurance.

**How to read this against [[Scaling Models#SC-058|SC-058]].** SC-058 says CBO compounds Pareto until about 4% of ads hold about 64% of spend, asserted across two videos with no dataset shown. This is a dataset and it disagrees, but it is measured in a window where spend per account sits several times above its evergreen level. **Treat it as a boundary on SC-058 rather than a refutation: concentration looks like a function of how much spend the account is pushing relative to its winners' ceilings, so it compounds at normal spend and decompresses under a peak ramp.** Neither has been tested against the other on one account across both windows, which is the test that would settle it.
Sources: @SRC@
Last touched: 2026-09-22
""".replace("@SRC@", BS))

add("Scaling Models.md", u"""
### SC-164 \u00b7 Revenue-spend elasticity is a CUT instrument only, and scaling on it overspends by construction
Tier: T3 \u00b7 Status: active
A rare case of an operator publishing a metric and then naming which direction you are allowed to use it in.

**The calculation.** The log of revenue on day two over revenue on day one, divided by the log of spend on day two over spend on day one. The output normalises roughly between 0 and 2 and reads as underspending, spending about right, or room to push. It works retrospectively and on a three to four day rolling delay.

**Why it may only be used to cut.** It is observational, not causal. **You raise spend on the days demand was already going to be high.** Black Friday spend goes up because Black Friday is expected to be a good day, so the metric returns a high elasticity and says spend more, when the revenue was arriving regardless. "It's not that the spend is causing revenue, it's that you might just be spending more because the revenue is going to be high anyway." Used as a scaling trigger it produces severe overspend. Used as a cut trigger the same correlation does no harm, because a low reading is a low reading whichever way causation runs.

**The scaling rule he uses instead.** Scale on **three-day rolling marginal averages**, not day to day. If contribution margin three is marginally improving on the three-day rolling, increase. If it is not, do nothing. **Two consecutive poor reads, decrease.** Day to day is used only when total spend is high enough that the pacing sheet is already moving money fast.

**Where the ceiling sits.** Scale toward the point where **marginal ROAS equals break-even ROAS**, which is one over gross margin ([[Marketing Math & Unit Economics#MM-214|MM-214]]). Contribution margin three is the floor, not the ROAS number. Keep pushing until CM3 flattens; past that point revenue still rises while marginal contribution profit goes negative.
Sources: @SRC@
Last touched: 2026-09-22
""".replace("@SRC@", BS))

add("Scaling Models.md", u"""
### SC-165 \u00b7 Fund the pre-season: 31 to 43% of the September-to-December budget belongs in September and October
Tier: T3 \u00b7 Status: active
The spend-shape recommendation that falls out of [[Attribution & Incrementality#AT-122|AT-122]]'s attribution finding. The default failure is going all in on November with very little September and October spend, which shrinks the funnel the sale is supposed to collapse.

**The prescription.** Roughly **double November spend against October**, on top of a genuinely funded pre-season, with **31 to 43% of the September-to-December budget sitting in September and October**. A "light warm-up" is named and explicitly not recommended.

**Portfolio benchmarks from his best-performing clients last year, by November spend bracket.** Clients spending **$500k to $2 million in November** spent **1.76x** their October figure; November was **13.8%** of their entire yearly spend; the revenue multiple was close enough that the ratio came out at **0.95**, so spend moved almost exactly proportional to the incremental revenue. Clients over **$2 million** spent a little less than that and their returns were better, which he reads as that bracket having **underspent**. Averaged across the whole book including sub-$500k clients, about a **1.8x** spend multiple at a ratio near **1.0**.

**Two operating rules attached.** Model a **base case and a stretch case**, with the efficiency and spend unlocks agreed in advance, so the team can push into an opportunity at 8am on the Saturday without waiting on the client. And **the budget is a ceiling to be deployed against incremental returns, not a target to be spent**: a retail client with a $1.5 million mandate does not get $1.5 million spent into diminishing contribution margin.

Agency portfolio figures described off slides, not published.
Sources: @SRC@
Last touched: 2026-09-22
""".replace("@SRC@", BS))

add("Scaling Models.md", u"""
### SC-166 \u00b7 Cost caps as a MEASUREMENT instrument: run them in the peak to find where the marginal frontier actually is
Tier: T3 \u00b7 Status: active
A use for cost caps this codex has not recorded, and it comes from an operator who is on record against them as a delivery strategy.

**His standing position is anti-cost-cap**, publicly stated: they create too much account volatility and they demand very high volumes of creative. Most of the portfolio does not run them.

**The exception, and the reason for it.** During Black Friday he runs some cost cap campaigns specifically to **see what they will spend to**. A cost cap deploys budget only while it can find conversions at the stated price, so the spend it actually reaches is a read on how much volume exists at that efficiency. That number then calibrates how hard the maximize-volume campaigns can be pushed.

**Why this is worth banking separately from the cost-cap performance debate.** Every other cost-cap claim in this codex argues whether caps deliver better or worse than maximize volume. This one does not care: the campaign is an instrument and its output is a headroom estimate for the campaigns carrying the real money. It sits directly against [[Scaling Models#SC-164|SC-164]], where the elasticity calculation is disqualified for exactly the causality a cap partly supplies.

Asserted as portfolio practice, with no comparison shown between the cap's spend ceiling and the volume campaign's realised headroom.
Sources: @SRC@
Last touched: 2026-09-22
""".replace("@SRC@", BS))

add("Scaling Models.md", u"""
### SC-167 \u00b7 Dead weight inside a CBO is real money and it is measurable: 52 of 60 ad sets spending with zero sales, about $6,000 a month
Tier: T3 \u00b7 Status: active
The first figure in this file that prices the tail of an unmanaged CBO, and it arrives from a takeover audit rather than from a theory about delivery.

**The account.** A newly onboarded client running **north of $150 to $200 cost per acquisition**, with **over 70 ad sets live in one main CBO campaign**. Theriot turned off **around 60 of them**. Of those 60, **52 were receiving spend and had produced zero sales**, collectively about **$200 a day**. That is roughly **$6,000 a month**, which he annualises at about **$72,000**.

**Why the number is the useful part.** It converts "clean up the account" into a quantity, and it lands on the opposite side of the argument from [[Scaling Models#SC-163|SC-163]], where the tail of a Black Friday account carries 54% of spend productively. The two are compatible and the distinction is the whole point: **a tail that spends and converts is capacity, a tail that spends and does not convert is leakage, and only the results column separates them.**

**His reading routine, which is the transferable half.** He does not open ad sets. He goes to the **ad level for the whole campaign with no ad set selected**, sorts by amount spent, and turns off individual ads from that view. He also reports having tested leaving all ads on permanently and abandoned it: it worked on some accounts and not others, and his constraint is a standard set of decisions that must be profitable on the majority of accounts before he adopts it across the book.

**Live tension with the same day's harvest, recorded rather than resolved.** [[Meta Delivery & Andromeda#MD-163|MD-163]] argues that turning ads off at this rate destroys the sequencing signal and manufactures the volatility operators blame on Meta. Theriot's figure says the spend is real and recoverable. Nobody has run both policies on one account.
Sources: @SRC@
Last touched: 2026-09-22
""".replace("@SRC@", NT))

# ---------------------------------------------------------------- Creative ---
add("Creative Science.md", u"""
### CR-255 \u00b7 Forecast creative volume from peak daily spend divided by per-ad spend capacity, and the answer is a count of WINNERS, not a count of ads
Tier: T3 \u00b7 Status: active
A third spend-keyed volume method, and it keys off a different quantity from the two already contested at [[Creative Science#CR-185|CR-185]]. Those two divide MONTHLY spend by a rate. This one divides PEAK DAILY spend by how much a single ad can actually absorb in a day.

**The method.** Look at last November. Find the peak daily spend reached by a single ad in the account, and what type of ad it was. Divide the daily spend you intend to reach by that figure.

**His numbers, pulled from the Meta MCP.** Highest single ad in an AUD account, **$12,500 a day**. Most evergreen ads spending between **$4,000 and $8,500 a day**. Realistic working ceiling **$8,000 to $13,000 a day**. Defaults he offers to anyone who will not pull their own: assume the **average evergreen ad spends about $5,000 a day** and a **winner's realistic working ceiling is $10,000 to $12,000 a day**.

**The worked case, and the sentence that makes the claim.** To spend **$150,000 on a peak day you need 12 to 18 ads that can carry real spend**, and "there's a difference between 12 to 18 ads and 12 to 18 ads that can hold $10,000 a day in ad spend. Very big difference. This is like 12 to 18 winners."

**Why this method is worth having alongside the monthly rules.** It answers a question the monthly rules cannot: whether the account has enough spend CAPACITY to deploy a given budget on a given day, which is the constraint that actually binds in a peak. Pair it with [[Scaling Models#SC-163|SC-163]], which says the winners will not carry all of it anyway and roughly half the spend lands in the tail. Read together, the two say: size the winner count off peak-day spend, then ship the tail volume as well, because the tail is where the other half of the budget goes.

Portfolio figures described off slides, no dataset published, and the per-ad ceilings are AUD accounts in his own book.
Sources: @SRC@
Last touched: 2026-09-22
""".replace("@SRC@", BS))

add("Creative Science.md", u"""
### CR-256 \u00b7 Offer creative buys SPEND CAPACITY, not conversion rate: the same one-day ROAS as evergreen while absorbing 4 to 5x the spend
Tier: T3 \u00b7 Status: active
The most useful creative finding in the 2026 Black Friday read, and it inverts the reason most operators give for making offer creative.

**The finding.** Motion, the creative analysis platform, published that **offer creative delivered the same one-day ROAS as evergreen creative but was able to absorb four to five times more spend.** Blue Sense's own portfolio agrees independently: pure offer statics hold far more spend than any of the evergreen ads in the same accounts.

**So the reason to make offer creative is not that it converts bottom-funnel traffic better.** On the evidence it does not convert better at all. It is that it raises the account's spend ceiling, which is the binding constraint in a peak per [[Creative Science#CR-255|CR-255]] and [[Scaling Models#SC-163|SC-163]].

**The share of spend he recommends by archetype**, which is his portfolio's own 2025 shape and which he explicitly endorses repeating: offer statics about **19%**, offer-overlaid evergreen and catalog about **18%**, creator and founder ads a large share, product and VSL about **14%** (top of funnel, deliberately not pushed harder), catalog about **12%**, plus early access and VIP.

**A diagnostic that travels beyond the season.** Catalog evergreen showed an **8 ROAS** in this data, which looks like the thing to double down on until you read its frequency, which is very high. **Frequency is a good indicator of where an ad sits in the stages of awareness**, so a high-ROAS high-frequency line is bottom-funnel retargeting harvesting demand, not a better ad. High ROAS and high frequency move together in his table.

Motion's figure is quoted from their report, which was not read here. Blue Sense's corroboration is portfolio data described off slides.
Sources: @SRC@
Last touched: 2026-09-22
""".replace("@SRC@", BS))

add("Creative Science.md", u"""
### CR-257 \u00b7 Creative is a CPM lever, not only a conversion lever: in a 72% more expensive auction, better and more diverse creative pushed CPMs DOWN
Tier: T3 \u00b7 Status: active
Reviewing last year's Black Friday data, Blue Sense found a relationship between creative quality, diversity and volume on one side and CPM inflation on the other. **In a window where the auction ran 72% more expensive, accounts with better creative, measured as how diverse it was and how much of it there was, ended up with lower CPMs.**

**His own hedge is part of the claim and must travel with it.** He calls the relationship **qualitative**, not measured, and offers the mechanism as a likelihood rather than a finding: there were a lot more impressions available last year, and you win more auctions with more diverse creative and more of it, so the effect is probably an auction-win-rate effect.

**Why it still matters.** It reframes the creative budget. If creative only moved conversion rate, its return is bounded by the lift it produces on the traffic you were already buying. If it also moves CPM, it changes the price of every impression in the account, and in a peak window that price is moving 25 to 50% against you anyway ([[Auction Mechanics & Bidding#AU-092|AU-092]]).

Qualitative by the source's own description, no regression and no dataset shown. This is the weakest-evidenced claim banked today and should not carry a decision on its own.
Sources: @SRC@
Last touched: 2026-09-22
""".replace("@SRC@", BS))

add("Creative Science.md", u"""
### CR-258 \u00b7 The offer corrupts the creative feedback loop exactly when the account is generating the most data, which makes CTR and CPC the least-bad read in this one window and noise in every other
Tier: T3 \u00b7 Status: active
The sharpest methodological point in the 2026 Black Friday read, and it is unusual because the same operator argues both halves against himself.

**The problem.** During a sale, ad one can post a strong ROAS because its product was a best seller at 50% off, and ad two can post a poor ROAS while being the better ad, because its product was neither discounted nor a best seller. The offer and the product dominate the result. **So the window that produces the year's largest volume of creative data is also the window where that data says least about the creative.** You cannot take the top-ROAS ads out of Black Friday and call them your good ads.

**What to read instead, and the concession it costs him.** Lean on creative metrics, click-through rate and cost per click, during this window because ROAS is unreliable here. He then states the opposite for every other week of the year in the strongest terms: if someone told you to judge ads on CTR and CPC, "I would say that is crazy, and there is no meaningful causal data to showcase that CPCs have any correlation to return on ad spend over large data sets." His test is to plot CPC against ROAS over a large set and look at the R squared, which he reports as very low and the data as very muddy.

**The banked position is therefore conditional, and the condition is load-bearing: CTR and CPC are diagnostic only when the result metric is known to be corrupted by offer and product mix, and are noise the rest of the year.**

**Second half, which generalises further.** Judge creative at the **ad set level rather than the ad level** during the period, because you have multi-touch optimisation reporting into last-click attribution, and Meta's breakdown effect makes ad-level ROAS less reliable still. That is the same direction as [[Attribution & Incrementality#AT-039|AT-039]], which already banks ad-level ROAS as corrupted by last-click sequencing and ad-set level as usable, arriving here from the creative side.
Sources: @SRC@
Last touched: 2026-09-22
""".replace("@SRC@", BS))

add("Creative Science.md", u"""
### CR-259 \u00b7 Diversity means diversity of CONCEPTS, not of visuals: Skims shipped 429 unique visuals built on three core ideas
Tier: T3 \u00b7 Status: active
From a scrape of large fashion brands' November 2025 ad libraries, and it puts a number on a distinction this codex has stated qualitatively.

**Distinct creative concepts run by each brand:** True Classic **11**, Ridge **10**, Threadheads **9**, Alo Yoga **7**, Gymshark **6**. His reading of the ordering is that concept volume decreases as performance-marketing capability decreases.

**The case that makes the point.** **Skims shipped 429 unique visuals, all built on three core ideas.** He is careful not to call that a mistake at the scale Skims was operating, and says it becomes a problem as you push to higher spend, which is the same ceiling logic as [[Creative Science#CR-255|CR-255]]: 429 executions of three ideas is still three ideas competing for the same clusters.

**The static rules that go with it, for the volume half.** There is no correct Black Friday aesthetic. There are two tests: **is the offer legible in under a second**, and **does the brand still look like itself**. Practical version: can you read the discount at thumbnail size. Three axes to spin volume off one offer static, which is how 50 of them get made quickly: **change the person using the product, change the product, or change the offer.** Two placement traps he names: do not let a 9:16 design push the offer into the region feed placements crop, and **put the offer or the deadline in the FIRST line of copy**, because copy truncates on story and several other placements.

**One nearly unexploited surface.** In their scrape of cold brands, catalog ads with no written messaging were **74%** and catalog with sale messaging was **3%**. Writing the offer into catalog copy is close to free and almost nobody does it.

**One constraint that will bite accounts ramping volume.** The Meta **page limit** on ads. Brands that have never hit it roll into November with high creative volume and hit it; the fix is cloned or additional pages, arranged in advance.
Sources: @SRC@
Last touched: 2026-09-22
""".replace("@SRC@", BS))

add("Creative Science.md", u"""
### CR-260 \u00b7 Never turn evergreen off for the sale: it held 50 to 60% of portfolio budget and performs BETTER in the window, because the campaign carries its conversion history
Tier: T3 \u00b7 Status: active
Named outright as **the single biggest mistake people make during Black Friday**, and stated as a rule he has repeated every year for seven years.

**The numbers.** In the 2025 portfolio, **evergreen campaigns held 50 to 60% of budget** through the sale period, and they perform better during Black Friday than outside it. The mechanism he gives is structural rather than creative: **evergreen campaigns carry campaign-level conversion history**, which is why they keep delivering, and turning them off and on "really messes with the learnings of the account".

**The one genuine decision inside the rule, stated with both sides.** Whether to re-badge evergreen copy with Black Friday messaging. Downside, **it resets learning phases**. Upside, more bottom-funnel messaging on ads that are already winning. He declines to prescribe and calls it account specific.

**The practical kit that follows.** Take the best-performing evergreen ads, **including fatigued winners from a year ago**, duplicate them, and badge the offer onto them. **Do not turn the originals off** when you run the badged duplicate. Run the same overlay treatment on creator videos and VSLs. For VSLs and other far-top-of-funnel assets, the Black Friday message usually cannot open the video and has to be pushed back into it, which is a re-edit; he tells fashion brands to skip this entirely and CPG brands to consider it, while warning it should not be a large share of spend.

**Creative phasing across the window:** build and teaser and early access, then launch, then a mid-sale refresh, then final 24 to 48 hour scarcity and deadline messaging.

**Volume multiples against October from the same brand scrape, offered as context and explicitly NOT as a target:** Represent Clo **12.6x**, Skims **4x**, Aesop **3x**, then 2.6x and 2.1x. **Alo Yoga did not increase creative volume at all**, which he flags as questionable. His instruction is to derive volume from expected spend over expected spend per ad ([[Creative Science#CR-255|CR-255]]), never from another brand's multiple.
Sources: @SRC@
Last touched: 2026-09-22
""".replace("@SRC@", BS))

# ----------------------------------------------------------------- Auction ---
add("Auction Mechanics & Bidding.md", u"""
### AU-092 \u00b7 The cheap 2025 Black Friday auction was bought with INVENTORY EXPANSION, and that lever is now spent
Tier: T3 \u00b7 Status: active
The best-evidenced piece of the 2026 Black Friday read, and the part with the longest shelf life, because it explains a year that every operator mis-remembers.

**Meta's own published quarterly numbers for the period.** Price per ad **up 6%**, impressions **up 18%**. Meta publishes total impressions and ad revenue, so CPM falls out of the division. Blue Sense's reading: **Meta opened a large amount of additional ad inventory over Black Friday**, so where a user previously saw 100 ads they saw 118, at the cost of organic posts and content. That extra supply is what held CPMs down against the normal year-on-year trend. "Year-on-year CPMs on Meta are much higher than 6% but we didn't see a spike during the Black Friday period."

**Third-party reads of the same window disagree in magnitude and agree in direction.** Triple Whale measured **7.8% CPM inflation**. Two other sources he pulled showed an outright **decline** in CPMs. He notes these reports all measure differently, which is why the percentages do not line up.

**Why 2025 is a misleading baseline for 2026.** In **Q1 2026 and Q2 2026 impressions have begun compressing year on year**, so the inventory growth is not repeating, and **year-on-year CPM growth is now worse than it was during Black Friday last year.** His forecast: no repeat of 18% impression growth, price per ad up considerably, total impression volume somewhat lower.

**What the peak curve looked like in his own portfolio**, pulled from the Meta MCP across an estimated $50 to $100 million of spend: October is the baseline, **from 12 November CPMs run 25 to 30% above that baseline** and climb through the period. Efficiency also peaks: ROAS outperforms the baseline by about **1.12x**, which he frames as barely enough, because gross margin is compressed by discounting at the same time.

**Triple Whale's 2025 period-on-period comparison, which splits the platforms.** Meta CPMs **+50%** over the Black Friday weekend, Google **+10%**. On Meta, CPA falls and ROAS improves. On Google, CPA worsens, ROAS worsens and impression-to-purchase falls (see [[Google Auction & Smart Bidding#GA-079|GA-079]]).

The 6% and 18% figures are Meta's own published reporting and are the T1 element here; the inventory-expansion interpretation, the portfolio curve and the 2026 forecast are the operator's and are T3.
Sources: @SRC@
Last touched: 2026-09-22
""".replace("@SRC@", BS))

add("Auction Mechanics & Bidding.md", u"""
### AU-093 \u00b7 Peak saturation is mild: portfolio frequency went 1.75 to 1.96 and back to 1.82, so the Black Friday wall is offer response, not audience exhaustion
Tier: T3 \u00b7 Status: active
Directly against the common belief that frequency spikes during Black Friday. Across the Blue Sense portfolio last year, **baseline frequency 1.75, peak 1.96 during Black Friday, 1.82 in Q5.** "Nobody really ran out of people."

**The diagnostic consequence.** When an account stops responding at its peak, it is usually **not a reach problem**. It is that the existing buyers have stopped responding: you have moved along the response curve to where the next dollar buys much less. The cause is offer fatigue or creative or audience fatigue on whatever is being pushed, not an exhausted pool.

**Two honest boundaries he attaches.** It can be a reach problem if you underspent going into the period and never built the funnel ([[Scaling Models#SC-165|SC-165]]). And **the dataset is large brands**: a small brand without a big pull will run much higher frequency on the same spend shape, so the 1.96 ceiling does not transfer down-market.

**Read against [[Creative Science#CR-177|CR-177]]**, where the fatigue metric operators actually use is ad-level frequency above 2.0 over 14 days on cold. A whole portfolio peaking at 1.96 at the busiest moment of the year suggests that threshold is rarely crossed at account level even under maximum pressure, which makes it a much less common trigger than its usage implies.
Sources: @SRC@
Last touched: 2026-09-22
""".replace("@SRC@", BS))

# ------------------------------------------------------------- Attribution ---
add("Attribution & Incrementality.md", u"""
### AT-122 \u00b7 The 1-day-click to 30-day-click gap DOUBLES in November, from about 40% to about 80%, so pre-season spend is systematically under-credited and the marginal dollar is best BEFORE the weekend
Tier: T3 \u00b7 Status: active
The load-bearing attribution finding of the 2026 Black Friday read, and it reverses the instinct every reporting dashboard produces.

**The gap.** Year round, the difference in credited revenue between a 1-day-click window and a 30-day-click window sits at about **40%**. **In November it goes to about 80%.** Reading 30-day click in the month before Black Friday makes the numbers look terrible; reading 1-day click during the sale makes them look outstanding. The same clicks are behind both readings. The purchases are backdated to clicks that happened weeks earlier, and the 30-day-click model loses a lot of them.

**Two conclusions he draws.** First, **spend far away from Black Friday is causal to Black Friday revenue.** Second, the size of the gap is knowable from your own account history, so it can be converted into a real-time correction: measure last year's pre-Black-Friday ROAS in 1-day-click terms and in 7-day-click terms, take the lift between them, and carry that as a premium on this year's pre-season ROAS reads.

**The single named case.** X Cloud, described as a very large multi-nine-figure US D2C brand, measured a **300% ROAS lift on 12 and 13 November** once the value finished booking through the sale. In real time on those two days their ROAS read about **1.0**. Backdated to the original clicks on a wide click-through model it was about **4.0**.

**Incrementality data pointing the same way, and this is the strongest evidence cited.** From Haus, a geo-holdout incrementality platform: experiments ending **3 or more weeks before Black Friday** showed a **105% post-treatment lift**; experiments closer to Black Friday showed **+75%**; **41% of incremental value appeared after the treatment window**; delayed effects during Black Friday ran **nearly triple** those of evergreen periods. Split by category, **fashion and apparel 93%** post-treatment lift against **health, wellness, food and beverage at 30%**, so the backfill case is much stronger in fashion than in CPG. The report is quoted as saying that holding back budget ahead of Black Friday means "you aren't saving dry powder, you're actually digging a deeper hole."

**Evidence-handling note, and it decides the tier.** The Haus figures are real geo-holdout experiments and would be T2 if read at source. **They are banked here at T3 because the primary was not read; what was read is a presentation citing them.** Reading the Haus report is logged as a research gap and would upgrade this claim.

**The bias, stated plainly.** Your reporting is most flattering on the weekend and least flattering on the run-up, so operators move money into the weekend, **which is exactly where the marginal dollar is worst.** Practical response: run 7-day click or 7-day click plus 1-day engaged through the period, compare several attribution settings rather than trusting one, build a post-treatment window into any pre-season measurement, and reconcile to the P&L. His attribution ladder for the sale period is Meta default, then 7-day click, then incremental attribution, then acquisition MER, each step closer to the business number, and he notes that **during the pre-season the ladder runs in reverse**: whatever ROAS shows is understated, because the sales book 7 to 14 days later.
Sources: @SRC@
Last touched: 2026-09-22
""".replace("@SRC@", BS))

add("Attribution & Incrementality.md", u"""
### AT-123 \u00b7 Use the incremental attribution column as a SCALING instrument rather than a scorecard: judge against target on your normal window, read incremental to price the NEXT dollar
Tier: T3 \u00b7 Status: active
A distinct operating use for a column this file already covers extensively, and it is narrower and more defensible than [[Attribution & Incrementality#AT-087|AT-087]]'s proposal to judge prospecting creative on the incremental column alone.

**The rule.** "I don't exclusively use incremental attribution as a guide if under or above my target, but I do use it to understand what's going to happen when I scale next." Pass or fail against target stays on the standard window. Incremental answers a different question: what the marginal dollar is likely to return, because it strips the conversions that were going to happen anyway.

**The shown example.** An account at a **2.28 ROAS on standard attribution and 1.87 on incremental**, on a business spending **$500,000 in the last 30 days across four campaigns**. What he takes from it is that the next dollar is more likely to arrive at 1.87 net incremental than at 2.28.

**The gate he puts in front of a scaling move.** Two conditions, both required: the target ROAS or CPA is set, and **you are comfortable spending at the incremental value, not at the reported value.** Only then does the scaling move happen.

**Why this is worth banking as its own claim.** It converts the incremental column from a number that makes reporting look worse into a decision input with a specific job. It also sits usefully beside [[Attribution & Incrementality#AT-085|AT-085]] and [[Attribution & Incrementality#AT-098|AT-098]], where the same column cut credited conversions by 46% and 75%: those claims establish the size of the haircut, this one says what to do with it.

Single account shown on screen, no test, and the 2.28 against 1.87 is one read on one book of spend.
Sources: @SRC@
Last touched: 2026-09-22
""".replace("@SRC@", SP))

add("Attribution & Incrementality.md", u"""
### AT-124 \u00b7 Hourly pacing has a built-in lag: spend peaks 5am to 7am while revenue peaks 7am to 11am, so early-hour ROAS is not comparable to a daily target
Tier: T3 \u00b7 Status: active
The intraday version of [[Attribution & Incrementality#AT-122|AT-122]], and the reason hourly pacing goes wrong for people who try it for the first time in a peak.

**The observation.** Across a lot of accounts through Black Friday weekend, **spend peaks between 5am and 7am and revenue peaks between 7am and 11am.** So a ROAS read at 5am is measuring spend whose revenue has not landed yet. Judged against the daily target it looks like a disaster and triggers a cut.

**The fix he prescribes.** Build **per-hour delayed attribution multipliers**: at 5am a reported 1.0 might really be a 2.0 once the day's revenue backfills onto that hour. This is the same correction as the pre-season multiplier, applied at a different time scale.

**The instrument that avoids the problem entirely.** **Pull conversion rates by hour.** He calls this a major unlock from two years ago that they have used ever since, because it gives a real-time read on whether to push spend without depending on platform-attributed revenue, which is always lagged.

**Two honest limits on the whole practice.** Hourly pacing only earns its cost at high spend with multiple offers rotating and a lot of creative to move; for most accounts it is overkill for almost no marginal gain. And **for brands that are not dependent on paid**, where a large share of revenue arrives regardless, hourly pacing is running on correlation rather than causation: you are moving spend around in response to how organic is performing.

Portfolio observation, described rather than shown, and no multiplier table published.
Sources: @SRC@
Last touched: 2026-09-22
""".replace("@SRC@", BS))

# -------------------------------------------------------- Marketing Math ----
add("Marketing Math & Unit Economics.md", u"""
### MM-222 \u00b7 Averages hide the marginal dollar: an $80,000 increase that kept average CAC inside a $400 tolerance had a marginal CAC of $1,000
Tier: T3 \u00b7 Status: active
The cleanest worked example of the average-versus-marginal trap in this file, and the numbers are the claim.

**The scenario.** Baseline new-customer cost per acquisition **$337**. Add **25% more spend, which is $80,000**. Average CAC degrades to **$392**. Against a **$400 CAC tolerance** that reads as fine, and most reporting stops there.

**What the increment actually bought.** That $80,000 produced **76 more customers**, which is a **marginal CAC of about $1,000**, two and a half times the tolerance. *Arithmetic check: 80,000 / 76 = $1,052, consistent with his stated $1,000.* The average absorbed it because the baseline volume was large enough to dilute it.

**The rule.** Scale on marginal returns, never on blended averages, both when planning against last year and when pushing intraday. "Averages will always mask the top incremental return."

**The second half, which moves the target rather than the reading.** Discount depth raises the required break-even ROAS **exponentially**, because gross profit per order is compressed. His worked point: a business breaking even at a **2.0** ROAS is breaking even at **4.5** once it discounts **40%**. This extends [[Marketing Math & Unit Economics#MM-214|MM-214]]'s one-over-gross-margin rule into the sale period, where the margin in the denominator is not the margin on the price list. Two things have to be known before any peak efficiency target can be set: the discount, and what it does to gross margin.
Sources: @SRC@
Last touched: 2026-09-22
""".replace("@SRC@", BS))

add("Marketing Math & Unit Economics.md", u"""
### MM-223 \u00b7 Two account-level health metrics that are not ratios: the revenue floor, and profit volume
Tier: T3 \u00b7 Status: active
From an operator claiming over a billion dollars of Facebook spend across more than a decade, and the argument is that both of the numbers most accounts are run on are ratios that can rise while the business shrinks.

**The revenue floor.** Defined as **how much of your revenue comes from people who are not buying from you for the first time**, read month over month. If it rises every month the business is healthy; if it does not, it is not. He proposes it as the single definition of success, above ROAS, CPA, AOV and creative hit rate.

**Profit volume.** Defined as **total revenue minus total ad spend**, absolute, not a ratio of anything, built as a custom metric in a dashboard. It does two jobs. If profit volume rises and the bank account does not, whatever you are doing is not working regardless of what the attribution report says. If it rises and the bank account does too, you know what moved it.

**The observation that motivates both, and it is checkable on any account in about five minutes.** Pull the account with every line item removed, broken down by week, across the whole year, sorted chronologically, with ROAS added alongside. **The weeks with the highest ROAS are not the weeks with the highest profit volume**, and the best-ROAS weeks are often the weeks where revenue suffered most, because ad spend was not driving much incremental revenue in them.

**The mechanism he attaches to why ROAS-chasing degrades the business.** The traits that win on ROAS, low price, low friction, broad appeal, discount responsiveness and direct response, are the same traits that select for the customer least likely to return. So **optimising for ROAS is not neutral toward retention, it selects against it.** That half is a mechanism assertion with nothing shown, and should be carried as reasoning rather than as a finding. The two metric definitions stand on their own and cost nothing to build.
Sources: @SRC@
Last touched: 2026-09-22
""".replace("@SRC@", CT))

add("Marketing Math & Unit Economics.md", u"""
### MM-224 \u00b7 Pick the acquisition offer by the Wilson lower bound on repeat purchase rate, not by raw repeat rate and not by best-seller volume
Tier: T3 \u00b7 Status: active
A statistical method for a decision this codex has so far treated as judgement: which product should the ad account be built around.

**The question it answers.** Not the best seller by volume and not the highest margin product. **Which product, when bought first, most reliably produces a repeat buyer, ranked by how much confidence the sample actually supports.** The input is one receipts export with four columns: customer ID, order date, product, revenue.

**Why the confidence bound rather than the raw rate.** In the shown case, Rose Hip Repair had the **highest raw repeat purchase rate at 67.5%**, on **40 first-time customers**, which is not significant. Vitamin C had the highest raw volume of returning customers. **The Barrier Repair ceramide cream won on the Wilson lower bound: a repeat rate of nearly 55% on almost 500 customers, with a confidence floor above 50%**, making its buyers more than twice as likely to buy again as the number one selling product's. **His thresholds: a confidence floor over 35 is solid, over 50 is strong.** Plotted, everything left of the confidence line does not have enough data to be trusted.

**The case, with the numbers that make it worth banking and the caveat that caps the tier.** Skincare brand, 44 products. Starting state: over **16,000 first-time customers**, **22% storewide repeat rate**; Vitamin C took **58% of Facebook spend ($41,760/month) at a 1.5 ROAS and $78 CPA**; Barrier Repair took **6% ($4,300/month) at a 0.98 ROAS and $130 CPA**; total **$1.8 million spent at a 1.27 ROAS and $90 CPA, about $72,000 a month**. They rebuilt the account around Barrier Repair. End state, August 2026: **44,000 first-time customers, 33.7% storewide repeat rate, $340,000 a month in spend**, Barrier Repair moved from **6% to 80% of spend**, and it now generates **over $2 million in returning revenue** against the roughly **$200,000** Vitamin C produced when it was the hero.

**The headline result is that the account metrics got worse on purpose.** Blended ROAS fell from **1.27 to 1.02** and CPA rose from **$90 to $138**, while the business became dramatically more profitable and spend went up **4.7x**. That is the concrete version of the argument in [[Marketing Math & Unit Economics#MM-223|MM-223]].

**Tier discipline.** This is a two-year before-and-after on a single account with no control and no holdout, so everything else that changed in two years is inside the result. It is banked as T3 with shown numbers, not as T2, and it should be quoted as a case rather than as an effect size.

**One honest finding inside the data that cuts the other way.** **Scaling an offer almost always makes its repeat rate a little worse**, because the spend reaches further up the funnel. They saw it and the business still improved.
Sources: @SRC@
Last touched: 2026-09-22
""".replace("@SRC@", CT))

# ------------------------------------------------------- Meta Delivery ------
add("Meta Delivery & Andromeda.md", u"""
### MD-163 \u00b7 The cost of daily on-off churn: if half the ads the model was learning from yesterday are gone today, it has no basis for tomorrow
Tier: T3 \u00b7 Status: active
The mechanism half of the case against high-churn account management, from an operator claiming over a billion dollars of Facebook spend.

**The claim.** An account running dozens of campaigns, hundreds of ad sets and thousands of creatives is asking the ranking system to choose between a very large number of options that each carry almost no data, while the operator turns ads off continuously. "If half the ads it was learning from yesterday are gone today, it has no confidence on what to do tomorrow." **His conclusion is that the day-to-day unpredictability operators blame on Meta is produced by the operator.**

**The early-life reading rule that follows, and it is the practically useful part.** New ads are tested against the people most likely to act on them, which is the bottom of the funnel, so they show **higher CPMs, higher frequency and strong performance for a few days and then drop off.** That drop is not fatigue. It is the ad graduating into colder traffic, and nothing performs as well against cold as against warm. **"How an ad performs in the first few days tells you almost nothing about how it's going to perform over the first few weeks or months, unless it was no good anyway. Bad ads don't get better."** This is the same delivery behaviour already banked at [[Meta Delivery & Andromeda#MD-006|MD-006]] and [[Meta Delivery & Andromeda#MD-008|MD-008]]; what is new here is the explicit instruction that a three-day read is not a kill signal.

**The at-bats argument he rejects.** More at-bats is true, but "more at-bats doesn't mean giving more batters just a few swings. It means giving the batters who are good more practice." He puts the choice as a thousand ads getting $10 each against ten ads getting $1,000 each, and says a machine-learning system is never better off with less data per option.

**LIVE TENSION with the same day's harvest, recorded rather than resolved.** [[Scaling Models#SC-167|SC-167]] has Nick Theriot turning off around 60 ad sets on one account, 52 of which were spending with zero sales at about $6,000 a month, and treating that cleanup as recovered money. Both operators are describing real accounts. The distinction that probably reconciles them is WHICH ads get cut: Theriot is removing ads that spend and do not convert, this claim is against removing ads the model is still learning from. Neither has tested the other's policy, and no shown data supports either.
Sources: @SRC@
Last touched: 2026-09-22
""".replace("@SRC@", CT))

add("Meta Delivery & Andromeda.md", u"""
### MD-164 \u00b7 Proposed: the account's own sales MIX steers delivery, so pushing one offer past 50% of sales points the whole system at that offer's buyer
Tier: T4 \u00b7 Status: active
Banked at T4 deliberately. The idea is coherent and the specific numbers in it have no source.

**The claim.** Andromeda is described as maintaining homeostasis: whatever is happening most often is what it will do more of. If the hero offer moves from **13% of sales to 25%**, the machine becomes "dramatically more likely" to make the next sale a hero-offer sale. **Once the hero offer crosses 50% of all sales**, every signal and optimisation decision in the account is said to point at finding more of that ideal customer, cheaper and at higher volume.

**Why it is only T4.** The 13%, 25% and 50% are illustrative, not measured. No mechanism inside Meta's published architecture is named to support a threshold effect at 50%, and a monotonic relationship between sales mix and delivery mix, which is plausible, would not produce a threshold at all. The neighbouring assertion that **"your CPMs drop because Meta recognises you as a quality signal provider"** has no support of any kind and should not be repeated.

**What survives if the threshold is discarded.** The directional part is consistent with claims this codex already holds at higher tiers: delivery reinforces on whatever the conversion event actually captures ([[Learning & Signal#LS-008|LS-008]]), and a mixed bag of outcomes inside one optimisation target teaches the system to sell anything ([[Learning & Signal#LS-079|LS-079]]). **So the operating advice, concentrate the account on one offer so the signal is coherent, is supported. The specific 50% tipping point is not.**

Testable on our own accounts cheaply, which is the reason to keep it: track the hero-offer share of total conversions against blended CPA over the same window, on an account we are already concentrating.
Sources: @SRC@
Last touched: 2026-09-22
""".replace("@SRC@", CT))

# ------------------------------------------------------------- Google -------
add("Google Auction & Smart Bidding.md", u"""
### GA-079 \u00b7 Google is a PREPARATION platform in the peak, and its Black Friday ROAS spike is largely Meta's demand arriving as branded search
Tier: T3 \u00b7 Status: active
The clearest statement in this codex of why the two platforms should not be scaled the same way in a sale period.

**The performance split, from the Triple Whale 2025 Black Friday report, period on period.** Meta CPMs **+50%**, Google CPMs **+10%**. On Meta, **CPA falls and ROAS improves** over the weekend, which offsets the gross margin compression from discounting. On Google, **CPA gets worse, ROAS gets worse, and impression-to-purchase falls.** Read across Triple Whale's dataset, **Google performed worse overall for everyone while Meta performed better.**

**The attribution trap that hides it.** Google ROAS looks excellent during Black Friday in most accounts, and for many of them it has little to do with Google. Meta traffic drives demand, that demand arrives as branded search, and branded traffic converts better because the brand is on sale. **Google is a demand capture platform, so it looks better when demand rises without having caused it.** He is explicit that some of the lift is real for some accounts and that the general pattern is a lot of wasted Google spend from operators cranking budget on the strength of the ratio.

**What the work on Google actually is.** Preparation, done in advance, not budget ramping: titles, descriptions and assets rewritten to be relevant to the sale; Merchant Center rolled over and optimised; promotion feeds in place; promotional titles rolled into Search and PMax; discounted price lines feeding correctly. That prep is what produces the CTR and conversion rate advantage over competitors who skip it.

**The operating rule.** Ramp Google on a schedule with the prep done, and never scale it the way Meta is scaled.
Sources: @SRC@
Last touched: 2026-09-22
""".replace("@SRC@", BS))

# ================================================================ MERGES =====
merge("Marketing Math & Unit Economics.md", "MM-204", u"""
**Third instance, 2026-09-22, and it is the first one that reports a NULL result alongside the effect.** The same operator brings a wider sample to the same question: **10 clients, cohort data pulled manually and averaged.** A **November cohort delivered an average 38.5% six-month repeat lift against a February cohort's 63%**, which are the same two figures already on this claim from brand one above, now stated as a book-wide average rather than one report.

**The new and load-bearing part: 2 of the 10 brands showed NO difference at all**, November repeat rate lift identical to February. So the effect is real on average and is not universal, and the honest instruction that comes with it is to measure it per brand rather than apply it as a rule. His own process is to pull the last two years of November repeat-rate cohort lift for every client; where there is no difference, the CAC tolerance is unchanged.

**He also names the double error this produces in a peak CAC allowance**, which is worth carrying: most operators do not put the discount into the allowance, so gross profit per order is modelled as business as usual when it is not, AND the customer acquired is worth less over annual LTV. Both corrections push the same way, which is why a peak CAC tolerance set off list-price margin is wrong twice.

*He again summarises the gap as "50% worse". The arithmetic on his own numbers is 38.5/63 = 0.61, so 39% worse, matching the correction already recorded above. Use 39%.*
""", BS)

merge("Auction Mechanics & Bidding.md", "AU-034", u"""
**Confirmed again 2026-09-22 from portfolio data, with the window stated slightly wider.** Blue Sense calls **16 to 31 December the cheapest media of the quarter** and says CPMs drop massively, which matches this claim's direction on a window that starts a few days earlier than Boxing Day. Portfolio frequency also relaxes across it, from a 1.96 Black Friday peak back to 1.82 ([[Auction Mechanics & Bidding#AU-093|AU-093]]).

**One mechanism he adds, which cuts against the obvious read of a cheap window.** He states that CPMs correlate with auction pressure and more specifically with **expected action rate on the landing page**: when conversion rates are strong and returns are good, Meta charges more, because it can. When an advertiser is unprofitable, CPMs sometimes come down. He flags the statement as a generalisation with a lot of nuance. The practical consequence for Q5 is that arriving with a genuinely good offer will itself inflate the CPM somewhat, so the cheap window is cheaper before you succeed in it than after. Asserted, nothing shown, and it should not be quoted as a mechanism Meta has described.
""", BS)

merge("Attribution & Incrementality.md", "AT-039", u"""
**Independent arrival at the same rule from the creative side, 2026-09-22.** Blue Sense reaches ad-set-level reading as the default for a sale period, for the same stated reason: you have multi-touch optimisation reporting into last-click attribution, and **Meta's breakdown effect** degrades ad-level ROAS further. He notes his book does this evergreen anyway and that the peak makes it more important. Banked in full at [[Creative Science#CR-258|CR-258]], where the surrounding argument is about the offer corrupting the creative feedback loop.
""", BS)

merge("Learning & Signal.md", "LS-051", u"""
**The mechanics, 2026-09-22, from the same operator, plus two vertical extensions this claim did not carry.**

**How to build it.** Create a **custom conversion for the hero product**, named after the product, defined as a purchase event where the event parameter **contains the unique identifier of that specific product** in the store. Which parameter carries it varies by platform, product ID or content ID depending on Shopify, WooCommerce or ThriveCart, and the name does not matter as long as it uniquely identifies the product.

**Why, in one image.** "If I have a Lamborghini dealership with a coffee shop inside of it, and we just track transaction count, it might look like we're clearing the lot on a daily basis, but we're just pulling a ton of shots." **Purchase count tells you a card was run, not what sold.**

**The decision it changes.** Two ads each make 100 sales. One has a 5% better CPA but only 5% of its sales are the hero offer; the other has a worse ROAS with 95% hero-offer sales. **The second is dramatically better**, and no purchase-count column will say so. He adds a ratio metric for this directly: **hero-offer conversions divided by total purchases**, which ranks ads by how cleanly they buy the right customer rather than by how cheaply they buy any customer.

**Two extensions beyond ecommerce, both relevant to lead-gen accounts.** For a **subscription** offer, the repeat measure is not a second purchase, it is **renewal**: promote the initial offer whose customer is least likely to churn before the first renewal, even where two billing intervals are available. For **high ticket or coaching**, where there may only ever be one transaction, use a high-confidence leading indicator further down the funnel: on a webinar to booking-link to sales-call path, **do not optimise for webinar show-ups, optimise for the call being booked**, because different ads win each and only one of them is the business outcome.
""", CT)

merge("Marketing Math & Unit Economics.md", "MM-214", u"""
**Second operator, same construction, 2026-09-20, with a ceiling on the profit take that this claim did not carry.** Sam Piliero builds the target the same way: start at the break-even ROAS or CAC for **new customers only**, then add whatever take you want. His worked version, 50% margins on a $100 average order value, gives $50 of take, so break-even is a $50 CAC or a 2x ROAS; wanting 10% of the order as first-purchase profit adds $10 and raises the target accordingly.

**The ceiling is the new part.** "If you're going beyond 20 or 30%, understand that you are not in the e-commerce game to scale. Any e-commerce business that is actually trying to scale tries to work as close to break even as possible and makes their money on the lifetime value of the customer." He immediately qualifies it as a business decision rather than a rule, and does not tell anyone to sacrifice years of profit. **Carry it as a stated position on the trade between first-order take and growth rate, not as a threshold with evidence behind it.** Nothing is shown.
""", SP)

merge("Scaling Models.md", "SC-154", u"""
**Second full-year instance of this exact structure, different operator, 2026-09-21, and the shape holds.** Nick Theriot walks a $5 million e-commerce account run from **one USA-and-Canada broad CBO**, same ads in both countries, no separate stores and no separate campaigns, which he says arrived that way from the previous team and has never caused a problem.

**The numbers, read off the account for 1 August 2025 to 16 September 2026.** About **$5 million in sales**, **67% revenue growth**, 66% growth in ad spend, a slight ROAS improvement, a slight fall in new-customer CPA, and about a **50% increase in net profit**, which he puts at $200,000 to $300,000 of additional profit. Roughly **$1.6 million spent in this ad account** against **$2.4 million** across the business, the gap being an earlier ad account and some Google. **Well over two thirds of all spend ran through the single campaign.** Last 7 days about **$114,000** in revenue, so about $460,000 a month.

**The cadence inside the campaign, which is the part that matches SC-154 most closely.** **193 ad sets created in roughly 11 months, about $1.4 million spent across them, one ad IDEA per ad set and usually three creatives around it.** That is three to four new ad sets a week, every week, each one preceded by research (reviewing old creative data, Reddit, TikTok). Exceptions are named rather than hidden: a hot period such as Black Friday might get 8, 20 or 30 image ads in one ad set, which he puts at 10 to 15% of cases, and he would not go to 30 or 40. A bid cap campaign was launched, never took off, and was left running because its cost per purchase was fine.

**Two things he attaches that are not structural.** The account went through a profit DECLINE for the first one to three months before the winning ads were found, and he credits the client's patience as a precondition. And the current ceiling is not delivery, it is **LTV**: the brand is front-order profitable only, so further scaling waits on new products to raise lifetime value, at which point they will accept a higher front-end CPA.
""", NT)

merge("Creative Science.md", "CR-185", u"""
**A THIRD spend-keyed method arrived 2026-09-22, and it keys off a different quantity, so it does not extend this disagreement so much as sidestep it.** Both rules above divide MONTHLY spend by a rate to get a launch count. The new one divides **PEAK DAILY spend by how much a single ad can absorb in a day**, which answers a capacity question rather than a cadence question, and returns a count of winners rather than a count of launches. Banked in full at [[Creative Science#CR-255|CR-255]]. It comes from the same operator as the one-ad-per-$1,000 rule on this claim, in the same month, with no attempt made to reconcile the two, which is worth knowing before either is quoted as his position.
""", BS)

merge("Meta Delivery & Andromeda.md", "MD-008", u"""
**Restated independently 2026-09-21 with an explicit kill-rule consequence.** Charley T describes the same early-life shape, new ads carrying higher CPMs, higher frequency and strong performance for a few days before dropping off, and names the drop as the ad graduating into colder traffic rather than fatiguing. The instruction he draws from it is the addition: **a three to five day read is not a kill signal.** "How an ad performs in the first few days tells you almost nothing about how it's going to perform over the first few weeks or months, unless it was no good anyway. Bad ads don't get better." Full entry, including the churn-cost argument attached to it, at [[Meta Delivery & Andromeda#MD-163|MD-163]].
""", CT)

merge("Scaling Models.md", "SC-058", u"""
**A dataset landed against this claim on 2026-09-22 and it is banked as a boundary rather than a refutation.** Blue Sense portfolio data across an estimated $50 to $100 million of Black Friday spend puts the top 20 ads at 46% of spend and the bottom 80% of ads at 54%, with concentration FALLING as accounts get bigger. That is the opposite shape from the compounding described here. The likely reconciliation is spend level relative to the winners' per-ad daily ceiling, not a disagreement about CBO. See [[Scaling Models#SC-163|SC-163]].
""", BS)


# ------------------------------------------------------------- apply --------
def apply_merges():
    done = []
    for topic, cid, text, src in MERGE:
        p = os.path.join(SCI, topic)
        t = io.open(p, encoding="utf-8").read()
        m = re.search(r"(?m)^### " + re.escape(cid) + r"\b.*?(?=^### |\Z)", t, re.S)
        if not m:
            print("MISS", topic, cid)
            continue
        block = m.group(0)
        nb = block.rstrip("\n")
        # insert before the Sources: line
        sm = re.search(r"(?m)^Sources: (.*)$", nb)
        if not sm:
            print("NO SOURCES LINE", cid)
            continue
        srcline = sm.group(1)
        if src and src not in srcline:
            srcline = srcline + "; " + src
        head = nb[:sm.start()].rstrip("\n")
        tail = nb[sm.end():]
        tail = re.sub(r"(?m)^Last touched: .*$", "Last touched: 2026-09-22", tail)
        nb = head + "\n\n" + text.strip() + "\nSources: " + srcline + tail + "\n\n"
        t = t[:m.start()] + nb + t[m.end():]
        io.open(p, "w", encoding="utf-8").write(t)
        done.append(cid)
    return done


def apply_new():
    counts = {}
    for topic, blocks in NEW.items():
        p = os.path.join(SCI, topic)
        t = io.open(p, encoding="utf-8").read().rstrip() + "\n\n"
        t += "\n\n".join(b.strip() for b in blocks) + "\n"
        io.open(p, "w", encoding="utf-8").write(t)
        counts[topic] = len(blocks)
    return counts


if __name__ == "__main__":
    n = apply_new()
    m = apply_merges()
    print("NEW CLAIMS:")
    for k, v in sorted(n.items()):
        print("  %-42s %d" % (k, v))
    print("TOTAL NEW:", sum(n.values()))
    print("MERGED INTO:", ", ".join(m), "(%d)" % len(m))
