# -*- coding: utf-8 -*-
"""Claim merge for the 2026-09-03 research pass.

One new transcript from the daily harvest (Professor Charley T, hero-product
selection plus the 322 ad builder) and eight pulled from the backlog: three
Mark Builds Brands business videos, four Blue Sense Digital Black Friday
videos, and one Dr. Matt Shiver funnel breakdown. All read in full.
"""
import sys
sys.stdout.reconfigure(encoding="utf-8")
import merge_helper
merge_helper.TODAY = "2026-09-03"
from merge_helper import amend, mint, audit

CR = "Creative Science.md"
SC = "Scaling Models.md"
MM = "Marketing Math & Unit Economics.md"
LS = "Learning & Signal.md"
AT = "Attribution & Incrementality.md"

CT = "Professor Charley T, Claude Has Officially Changed Facebook Ads Forever! (Tutorial), 2026-09-02"
MB_AI = "Mark Builds Brands, how i create AI ads w/ higgsfield that print, 2026-04-11"
MB_10 = "Mark Builds Brands, 10 brutal lessons after making $9,867,257 in 2025 w/ branded dropshipping, 2026-01-02"
MB_PR = "Mark Builds Brands, i asked claude to find me a $1k/day product, 2026-06-11"
BS_BF = "Blue Sense Digital, Avoid These Mistakes This Black Friday (eCommerce), 2025-08-27"
BS_KPI = "Blue Sense Digital, Don't Make This Black Friday Mistake, 2025-11-06"
BS_SLUMP = "Blue Sense Digital, Beat the Post-BFCM Slump: The 3 Moves That Prevent It, 2025-10-03"
BS_ASSET = "Blue Sense Digital, No Assets for BFCM? Here's the Workflow That Saves You, 2025-11-19"
MS = "Dr. Matt Shiver, How I Used Skool to Build a 7-Figure Coaching Business (Full Breakdown), 2026-04-28"

print("== Marketing Math ==")

mint(MM, "MM-200",
     "The hero product is the entry SKU with the highest CONFIDENCE-ADJUSTED repurchase rate, which is usually neither the best seller nor the highest raw repurchase rate",
     "T3", "active",
     """Worked on screen against one coffee brand's own order export, stated as "a couple million a year out of Washington", 13 entry products.

**The three numbers that make the point.** The **discovery sampler** is the best seller at nearly 16,000 first-time customers, has always carried the best return on ad spend and the most ad spend, and repurchases at **just over 8%**, which he calls third worst in the business. **Panama Geisha** repurchases at **over 70%**, the best rate in the catalogue, on a small base. **Single origin Ethiopia**, a product nobody was looking at, has **nearly 8,000 customers at a 35% repurchase rate**, and it wins. Two consequences he states: a customer who starts on Ethiopia is **4.3 times more likely to buy again** than one who starts on the sampler, and Ethiopia **already earns more returning revenue than any other product in the business from half the first-time customers the sampler brings in**.

**The statistic that resolves the tie, and it is the transferable part.** Ranking on the raw percentage hands the crown to the 70% product on a tiny base. He ranks on the **Wilson score interval** (Edwin Wilson, 1927), which applies a confidence correction to a percentage measured on a small sample, and is the same statistic behind social-platform ranking. On the confidence chart the highest point is Ethiopia, not the 70% product and not the best seller. Operator rule: **never pick a hero product off a repurchase percentage without a sample-size correction**, because the highest raw rate in any catalogue is almost always the lowest-volume SKU.

**The caveat he states himself, and it must travel with the claim.** "This report describes a pattern in your receipts, but it does not explain that pattern... Maybe the product is genuinely excellent. Maybe the people who buy it are just the kind of buyer who repurchases from anyone. The data can't separate those two, and I'm not going to pretend that it can." So this is a selection heuristic, not a causal finding. It tells you where to point spend next; it does not tell you the product caused the repeat.

**Why it matters for spend.** He frames the entire read as the answer to one question, "can we spend more money tomorrow", with growth in revenue from non-first-time buyers as the only success definition. That is the same allowable-acquisition-cost logic as [[Marketing Math & Unit Economics#MM-199|MM-199]] approached from the product side rather than the P&L side, and it sits directly beside the hero-product exclusion-window logic in [[Auction Mechanics & Bidding#AU-060|AU-060]].

**Evidence class.** One account, shown on screen, no control, no test. Every number is his narration of his own report.""",
     [CT])

mint(MM, "MM-201",
     "Two funnel ratios and two margin floors that decide whether a failed product test is an ads problem or a funnel problem",
     "T3", "active",
     """Stated for US direct-to-consumer e-commerce by an operator claiming tens of millions in Meta spend. All benchmarks, none of them measured on screen.

**Funnel ratios.**
- **Add to cart rate: at least 10%** of everyone who lands on the first page, whether that page is an advertorial, a pre-sell or the product page. He allows 8 to 9% on a higher-priced product. Below that, either the funnel is not good enough or the ads are sending unqualified traffic.
- **Add to cart through to purchase: at least 30%.** Ten carts should produce at least three orders. Below that the fault sits between cart and payment, and his named suspects are payment-processor approval rates and an over-complicated checkout. His fix direction is subtraction: "you'll be much better removing things than you are trying to add all these various things".
- **Average order value: 20 to 40% above the main product's price** on a straight Shopify build, with lifetime value substantially higher again if there is a subscription or a retention motion. *Note an internal inconsistency: having given the 20 to 40% band he immediately says push it to "even like 50% above that number". Use the band, not the aside.*

**Margin floors, and he dates the change.**
- **At least 3x cost of goods sold at the price point.** Sourced and shipped at $15 means selling at $45 minimum.
- **At least $30 gross margin per order.** He raised this from $20, and gives the reason as Meta costs rising: "$30 margins is a good place to be".

**Where this sits.** It is a set of pass conditions to apply before blaming a product, and he is explicit that the product is rarely the fault: the failure is either ad-related or funnel-related, and "90% of the issues that I see is ad-related". The ad half of the same diagnostic is at [[Creative Science#CR-226|CR-226]]. These are e-commerce numbers with a physical product and a cart, so **none of them transfer to a lead-generation account** without being restated as opt-in rate and opt-in to booked call.""",
     [MB_PR])

mint(MM, "MM-202",
     "The public-traffic revenue estimate for a competitor is four stacked assumptions, and the operator who teaches it says outright he cannot calculate the real number",
     "T4", "active",
     """The method, because it is what almost every competitor-research workflow actually runs on, and the honest accounting of what it is worth.

**The formula.** Monthly visits from a SimilarWeb reading, times an assumed conversion rate, times an assumed average order value. His assumed conversion band is **1.5% to 3.5%, lower for a more expensive product**. His worked example on a barefoot-shoe brand: the extension read close to 2 million visits a month, he deliberately marked it down to **1.5 million**, applied **2%** to get **30,000 orders**, and applied a **$90** average order value to reach **roughly $2.7 million a month**. *Arithmetic checks: 1,500,000 x 0.02 = 30,000 exactly, and 30,000 x $90 = $2,700,000 exactly.* His bar for treating a competitor as validated is **$200,000 to $300,000 a month minimum**.

**What is actually known and what is guessed.** One input is observed and it is itself a model: SimilarWeb's traffic figure is an estimate, not a counter. The conversion rate is assumed. The average order value is assumed from browsing the offer stack. The cost of goods is assumed. He says it plainly: "how the hell are you able to calculate exactly how much money? Well, I can't." So the output is an order-of-magnitude sort, useful for ranking candidates and worthless as a number.

**How to use it without lying.** Treat the result as a bucket, not a figure. Never put a competitor revenue estimate produced this way in a client document as a number, and never let it anchor a budget. The one thing it does well is separate a brand doing something real from a brand running ads into nothing, which is all he claims for it.

**A structural caution he adds and it is the better half of the video.** A competitor has usually been buying longer and has better supplier pricing than a new entrant, so their unit economics are not available to you on day one. Copying their price point without their cost base is the trap.""",
     [MB_PR])

mint(MM, "MM-203",
     "Plan a promotional peak against a contribution-profit target, never a revenue target, because the last slice of peak spend buys revenue at a loss",
     "T3", "active",
     """From an operator stating 250+ e-commerce brands worked through the Black Friday period and over a thousand accounts audited.

**The failure mode.** Everyone sets a revenue target for the peak, and the reason is legitimate, because inventory has to be planned against revenue. The damage is that nobody sets a contribution-profit target underneath it, so spend keeps going in past the point where it pays. His worked example, reconstructed from a garbled auto-transcript: **spend $250,000 and make $1,000,000, or spend $200,000 and make $980,000. The extra $50,000 of spend bought $20,000 of incremental revenue.** *Arithmetic: $250,000 - $200,000 = $50,000, and $1,000,000 - $980,000 = $20,000. Both reconcile exactly, which is what identifies the "$4 million" in the raw transcript as a mis-transcription of $250,000.* The verdict he draws: you turned over inventory for nothing and made the profit and loss worse, and "you may as well have just pulled back and been more efficient."

**The replacement planning question.** Not "what revenue do we want in November", but "what contribution profit do we need, and at what efficiency does efficiency start to erode". Set the spend at that point and accept a smaller headline number than the brand down the road. "Ultimately, who won the period?"

**Two named consequences.**
- Peak revenue is the metric most often used to sell a case study and it is the one that says least. This is the planning-side twin of [[Attribution & Incrementality#AT-084|AT-084]], where a Shopify chart rising through October and November is confounded with the season and shows topline rather than profit.
- The efficiency target itself has to move for the peak. Two independent reasons now sit in this codex: discounting compresses gross margin, so the same efficiency target yields less profit ([[Marketing Math & Unit Economics#MM-085|MM-085]]), and the customers acquired in the peak repeat worse, so a target grounded in a retention assumption is wrong ([[Marketing Math & Unit Economics#MM-204|MM-204]]).

Asserted from audit practice. No account data shown.""",
     [BS_BF])

mint(MM, "MM-204",
     "November cohorts repeat substantially worse than off-peak cohorts, so the peak efficiency target must be set HIGHER, and January and February can be set lower",
     "T2", "active",
     """The sharpest thing in today's read, because it inverts the intuitive move and it is shown against real cohort reports rather than asserted.

**The mechanism, in consumer terms.** A November buyer is someone a large discount pushed over the edge. A January or February buyer walked past every sale of the previous two months, which means both high disposable income and genuine conviction about the product. So the November cohort is structurally the year's worst and the January cohort is structurally among the best. "November customers are the worst customers in the entire year."

**Brand one, Shopify customer cohort analysis on screen.** November 2024 cohort: average spend per customer **$114**, rising to **$158 by month six**, an increase of **$44** which he reads as **38.5%**. A February or March cohort on the same report: an increase of **$79**, which he reads as **63%**. *Arithmetic: 44/114 = 38.6%, matching his 38.5%. His summary that the November cohort is "50% worse" overstates it; 38.5/63 = 0.61, so it is 39% worse on the numbers on his own screen. Use 39%, not 50%.*

**Brand two, a different industry, both brands stated as over $10 million online.** November **$116** to **$170** by month six, **+46%**. *Arithmetic: 54/116 = 46.6%, matching.* February on the same report, **+55%**. He calls this the less extreme case, and it is: 46/55 = 0.84, so 16% worse rather than 39%.

**The blind spot he then names, and it is why the gap is understated.** The Shopify cohort report is built on REVENUE. Peak revenue carries a much worse gross-profit percentage because of the discounting, so $54 of six-month growth from a November cohort is worth less gross profit than $54 from a February cohort, and the report cannot show that. His illustrative pair is $27 of gross profit against $18. **Those two numbers are made up on the spot to keep the arithmetic easy and he says so.** The real instruction is to rebuild the cohort analysis at gross-profit level, which his agency does and the native Shopify report does not.

**The operating consequence, stated in both directions.** An efficiency target justified by a retention assumption does not hold in November. His illustrative calendar: a target of MER 5 through November and December, coming down to about 4.0 or 4.1 in January, because the January cohort will prop up returning revenue through the following six months. He attaches the cash-flow condition explicitly: you can only get more aggressive in January if the working capital is there.

**Evidence class.** Two brands, two industries, cohort reports read on screen with figures visible. Not a controlled test, so it does not establish the causal story, but it is real measured cohort data rather than recollection, which is why this is banked as T2 while [[Marketing Math & Unit Economics#MM-203|MM-203]] from the same operator is T3.""",
     [BS_KPI])

mint(MM, "MM-205",
     "Returning-customer revenue is a function of cohorts you have already acquired, so it cannot be forecast by applying a growth multiple",
     "T3", "active",
     """A forecasting rule that kills the most common peak-planning error among brands sophisticated enough to split revenue into new and returning.

The error: take last year's returning-customer revenue for November and multiply by the growth ambition, 40% up on last year. "You can't just simply generate 40% more returning customer revenue out of thin air." Most of November's returning revenue comes from cohorts acquired **earlier in the same year**, so by the time you are building the November forecast the input is already fixed and unchangeable.

**The diagnostic is one line.** Look at this year's new-customer acquisition against last year's. If it is flat, slightly up or slightly down, returning-customer revenue in November will be **5 to 10% better at most**, not 40%. If you want a materially better returning number for a peak, the lever was new-customer acquisition six to twelve months earlier, and it is gone.

Direct consequence for anyone building a forecast: returning revenue is a cohort roll-forward, never a growth multiple applied to a total. It is the same object [[Marketing Math & Unit Economics#MM-006|MM-006]] insists on measuring by cohort rather than by Klaviyo-attributed revenue or a returning-customer percentage, pointed forward instead of backward. Asserted from audit practice, no forecast model shown.""",
     [BS_BF])

mint(MM, "MM-206",
     "Never benchmark your peak growth rate against Shopify's published GMV, because that number is inflated by enterprise onboarding",
     "T3", "active",
     """Shopify publishes a gross merchandise value figure each Black Friday and its growth rate reliably looks strong. The reason given is that Shopify onboards large enterprise retailers each year, and those accounts land inside the total, so the published growth rate mixes new platform accounts with same-store growth. A brand comparing its own same-store November against that number will always look bad and the comparison is meaningless.

He supports it with a concentration figure and flags his own uncertainty in the same breath: "I don't have the numbers on me off the top of my head, but it is something like 70% of total Shopify GMV comes from 5% of Shopify stores." **Record that as his recollection, unverified, and do not quote the 70/5 split to a client.** The structural argument stands without it: a platform total that gains accounts each year is not a same-store index.

Operating rule: benchmark a peak against your own prior-year same-store performance, and against your own contribution profit, never against a platform-wide total. Same class of reading error as [[Attribution & Incrementality#AT-084|AT-084]].""",
     [BS_BF])

mint(MM, "MM-207",
     "A long promotional window needs an offer ROTATION and a permanent sale page, and launching on the actual peak weekend loses revenue to competitors who launched two weeks earlier",
     "T3", "active",
     """Four operational rules for a five-week sale, from the same audit practice.

**Launch timing.** The average consumer knows the sale is somewhere in late November and does not know the date. Because every competitor launches early, a brand that launches on or just before the weekend finds its customers have already spent their November budget elsewhere. His example: an eight-figure activewear brand launching on the 26th against competitors launching two weeks earlier, and the customer thinking "I've already spent $400 so far this month, I already kind of got this from a competitor". **The counter is a VIP list**, an offer nobody else gets, which locks loyal buyers in place while competitors are live. He judges the risk asymmetric: "There really isn't much damage of launching early."

**Then the cost of launching early, which is the offer running too long.** Five weeks on one flat percentage discount erodes brand equity and fatigues. **Do not run one offer for five weeks.** His rotation, in order: enter on a **bundle** offer, move to **flat percentage discounting** across the peak weekend because it is the fastest thing to communicate under a time squeeze ("You do not want complicated messaging during the tight squeeze"), then move out into **single core SKU discounting** for December gifting.

**A consolidated sale page in the site navigation.** Most brands discount across the whole site and never build a destination. With a sale page you can keep every offer in the rotation live at once and simply push retired ones down the page, which keeps the ads pointing at them alive even as spend comes off. Without it the rotation forces a hard cut each time.

**Bundle contingency.** Bundles share SKUs, so one component selling through kills several bundles at once. Keep **plan B and plan C bundles in draft**, with their ads and landing pages built, so a merchandising failure is a switch rather than a scramble.

Prescriptive, drawn from agency practice across a stated 250+ brands. Nothing measured.""",
     [BS_BF, BS_SLUMP])

mint(MM, "MM-208",
     "A free-course funnel to a high-ticket offer books under 5% of opt-ins on the front end and closes 3 to 9 months later, and that is the design rather than a fault",
     "T3", "active",
     """The economics of the free-community funnel, with the numbers its operator put on screen.

**The shown P&L.** March 2026: gross revenue **$222,000**, net income **$96,384**, against a standing target of $100,000 net a month. *That is a 43.4% net margin, which is worth holding against the same operator's coaching cost model at [[Marketing Math & Unit Economics#MM-198|MM-198]], where 20/15/20/15 leaves 30% net. His own month beat his own model by 13 points, so read the 30% as a planning floor rather than a ceiling.*

**The funnel's shape.** A free community, 8,300+ members, positioned as a free ads course. Paid traffic and YouTube organic feed an opt-in page, not the community. **1,353 organic joins year to date as of 7 April 2026**, attributed by UTM in Hyros down to the individual video. Opt-in page converting **around 20%** against a 25%+ target.

**The two numbers that define the model.** Front-end call bookings are **under 5%, "closer to like two or three percent"**. The average buyer purchases **three, six, even nine months** after entering, read out of Hyros. He accepts both, because the common objection is that people want to work through the course first, and the nurture layer is built for that window: weekly YouTube, weekly email, and informal in-community video.

**What the free thing has to be.** Step one only, and genuinely complete. "Can someone go through this and launch ads within 7 days, 14 days" so they get a quick win, at which point the next problem appears on its own: how do I scale this. He gives away a 30-minute campaign build others charge for, on the argument that a person who gets a result names you as the person to call. The gap is made visible rather than hidden: locked classroom modules and members-only calendar entries stay on screen with an apply button.

**Direct read for our own book.** Any funnel with a free destination has to be underwritten on a three-to-nine-month payback, not on front-end booked calls, and the nurture layer is the product. Sits against the free-destination quality problem: a free entry point selects for people who cannot yet pay, which is why the qualification step at [[Learning & Signal#LS-075|LS-075]] carries the whole model.

One operator, one account, figures shown on screen. No cohort table behind the 3-to-9-month claim.""",
     [MS])

print()
print("== Creative Science ==")

mint(CR, "CR-220",
     "An ad can do exactly three jobs (earn attention, clarify value, convert trust), the job is chosen before the format, and there is no mid-funnel",
     "T4", "active",
     """A decision order rather than a finding, banked because it removes the most common ambiguity in a creative brief.

**The three jobs.** Earn attention. Clarify value. Convert trust. "Finding the right customer doesn't fix the account if you ask the ad to do the wrong job."

**The refusal that gives it teeth.** He will not accept a mid-funnel diagnosis: "Mid-funnel is a myth. Either you're trying to scale, or you're trying to get more efficient." Upper funnel is the scale lever, lower funnel is the efficiency lever, and the operator picks by naming which of those two problems the account has right now. He notes the question is deliberately about your ad account rather than about theory, which is why he says you cannot answer it wrong.

**The ordering rule.** The job is decided first, and the format follows from the job. In the worked example the evidence pointed to an attention problem, the job was set to earn attention, and only then did the tool choose video over static and a testimonial treatment over the alternatives, stating what a static could have done that this ad could not.

**The non-duplication rule that follows.** Material collected during research and not used by this ad is marked and held rather than spent. In the example, a price rebuttal, brew versatility and bag mechanics were all on the evidence map, all deliberately left out of an attention ad, and reserved for the next ring, whose job is clarifying value. "Nothing gets gathered twice. This is how you complete a conversation in a funnel."

Fits directly on top of the Olympic Rings structure at [[Scaling Models#SC-021|SC-021]], which assigns five concepts distinct jobs; this is the rule for deciding which job a given ad gets. Framework only. No comparison between the three jobs, no data.""",
     [CT])

mint(CR, "CR-221",
     "Performance data is deliberately excluded from creative research inputs, and a contradiction BETWEEN evidence sources is the finding rather than a defect",
     "T3", "active",
     """Two method rules from a research process run on screen against one brand's real files.

**Rule one: no performance data goes in.** The research intake accepts reviews, surveys, support tickets and ad comments, the brand's own ads and landing page, competitor material and customer interviews. It refuses ad performance figures outright. His reason: "attribution based vanity metrics don't tell you anything about why something happened. Rank your ads by results and all you get back is make more of last month's winner. That's the loop we're trying to get out of." The sharper half of the argument is about quality of customer rather than quality of ad: "A high-performing ad built on an unsupported claim might have a great ROAS, but it's buying the customers who never buy again."

**Weighting.** Reviews carry the most weight, and he notes what reviews structurally cannot give you: 340 reviews told him why people stay and almost nothing about what nearly stopped them buying, so objections had to come from the survey and the support layer instead. Three of the six sources use the customer's words; the brand's own ads and landing page are added last, specifically to measure the gap between what the brand claims and what customers say.

**Rule two, and it is the one operators get wrong: sources are allowed to disagree, and the disagreement is data.** In the shown case, a survey of churned buyers had **49 of 62 mentioning price or suitability**, and he separates those immediately: "Those are not the same objection, and they don't get solved by the same ad." Then **18 support tickets mentioned neither taste nor price**, which fails to corroborate the "too fancy for me" hesitation the survey produced. He records the non-corroboration rather than discarding either source. Operating rule: **an objection that appears in exactly one source is a hypothesis, not a finding**, and the ad built on it should be labelled as testing that hypothesis.

**The gap the method is built to find.** In this account the brand's core vocabulary appeared **zero times across more than 400 pieces of customer evidence**, and **5 of the 9 live ads claimed something customers never say**. That is the output the process exists to produce.

One account, shown on screen, no test. Corroborated the same week and independently by [[Creative Science#CR-227|CR-227]].""",
     [CT])

mint(CR, "CR-222",
     "Write the test specification BEFORE launch: a hypothesis containing a because, what the test does not cover, what a loss puts in doubt, and what a win breaks next",
     "T3", "active",
     """The strongest testing-discipline artefact on file, because it is the only version that specifies what to write down about the OUTCOME before the outcome exists.

**Four required parts, quoted from the shown specification.**
1. **A hypothesis with a because in it.** "If cold buyers are excluding themselves because they think they're not serious enough about coffee, and 23 of 62 told us they nearly did, then a video that disqualifies expertise brings in first purchases at or below what I'm running now because it removes the barrier before price is considered." The because is the mechanism, and it names a business result rather than a platform metric. "A test without a hypothesis is just spending... most people that run 322s don't learn anything."
2. **What this does not test.** Written down explicitly, so a loss cannot later be blamed on something the test never touched.
3. **What a loss puts in doubt, listed in advance.** In the shown case the list has exactly one item: the concept. Not the hero product, because that came from receipts and a creative test cannot overturn it. Not the evidence, because "people did say those things and a losing ad can't unsay them". What is in doubt is one assumption, that a connoisseurship barrier is capping cold reach. It also states, in priority order, which parts of the ad to revisit first.
4. **What a win breaks.** "If this works, the landing page becomes the bottleneck", because the page still opens on a specialty enthusiast while the ad disqualifies expertise. A win that creates a continuity break is a planned next job, not a surprise.

**Why part three is the load-bearing one.** Without it, every losing test drags the whole chain of prior decisions back into the argument, and the account relitigates its product and its research every time an ad fails. Writing the blast radius down in advance is what stops that.

This is the pre-registration half of [[Creative Science#CR-041|CR-041]], which already requires a written hypothesis before launch and a review seven days after. CR-041 supplies the cadence, this supplies the contents. Shown once, on one account, with no comparison against teams that do not do it.""",
     [CT])

mint(CR, "CR-223",
     "Image ads exist to find the winning SALES MESSAGE, and the hook carries 90% of a video ad's outcome with copy inside the hook carrying 70 to 80%",
     "T4", "active",
     """Two stated weightings from an operator running branded direct-to-consumer at eight figures. Both are asserted with no data behind them, and both are useful because they are specific enough to argue with.

**The asset is the message, not the ad.** "Everybody kind of talks about winning ad this, winning ad that, but the best thing that you're really looking for is your winning sales message, because as soon as you have that message, that can be transmuted into videos, into different formats of images, into UGC, into a VSL, into short form, into founder UGC." Image ads are the cheapest and fastest instrument for finding it, so the sequence is find the message on statics, then invest production money in video. That is a different justification for statics than cost alone, and it is the reason a static test is not wasted when the winner ends up being a video.

**The hook weighting.** "90% of your success in video ads is going to come down to having a really really good hook", defined as the first three to five seconds. Inside the hook he splits it again: **copy at 70 to 80%**, then the scroll-stopping clip, then the audio, which he calls the least of your worries. His definition of a scroll stopper is behavioural rather than aesthetic: "something you look at and you literally have to be like, what did I just look at."

**Then the counterweight he supplies himself, five months earlier.** He warns against maximising hook metrics for their own sake: operators running high-curiosity native creative report a high click-through rate and no conversions, "cuz you forgot to sell them". So the hook weighting governs whether the ad gets watched, and it says nothing about whether it sells. Read the 90% strictly as attention, never as outcome.

Both weightings are stated as experience with nothing shown. They are compatible with the hook-variation economics at [[Creative Science#CR-124|CR-124]] and add no evidence to it.""",
     [MB_AI, MB_PR])

mint(CR, "CR-224",
     "The current AI ad pipeline is text-to-image for the start frame then image-to-video per line, and both failure modes are prompt depth rather than model limits",
     "T3", "active",
     """The production method, stated by an operator who builds ads this way daily, and two claims about where it breaks that we can test cheaply on our own accounts.

**The five steps.** Find a swipe as a starting point. Rewrite the script against the brand's own research documents. Storyboard, which is one script line mapped to one or two clips. Build the prompts. Assemble, caption and cut. The prompting step is two-part and that is the part people skip: **a text-to-image prompt generates the START FRAME, then a separate image-to-video prompt animates it.** "Just getting the image as a starting frame is only half of it. You have to make sure you have a really good prompt with it as well."

**The named stack, dated April 2026.** Nano Banana Pro for the start frame, Kling for image to video, both inside Higgsfield, with clip length taken from the script line, 6 to 8 seconds in his worked example. For a swiped static he uploads the competitor's image plus a transparent PNG of his own product on white, and the model returns the layout with his brand's details.

**Failure-mode claim, and it is the checkable one.** Misspelled or malformed text in a generated image or video is a prompt-depth failure, not a model limit: "if you ever struggle with having text being off on an image or a video, it's because you didn't go into enough depth on the prompt. These LLMs can't extract everything from an image. They can get pretty close, but if you add in the details where it's missing, it can create flawless images and videos." Asserted, no comparison run, and directly testable by re-prompting a failed generation with the missing details supplied.

**Independent corroboration on model choice from a different operator seven months earlier.** Blue Sense Digital, refreshing existing statics for a promotion, reaches the same model for the same reason: Nano Banana "is particularly good at keeping things like people's faces and likeliness looking consistent", where the alternative "may make the image look a little bit softer, could literally change the people that are in the ads". **And a named weakness: it will not reframe.** After repeated prompting it refused to convert a 9:16 asset to 1:1, and the workaround was a different tool that did the resize while visibly altering the image. Operating rule that follows: **download every source asset in the ratios you need rather than generating one and converting it.**

Two operators, no measurement from either. Read as a working recipe, not a benchmark.""",
     [MB_AI, BS_ASSET])

mint(CR, "CR-225",
     "The post-Andromeda test order is inverted: validate the CONCEPT first, then spam variations of what survived, and variations are demonstrably not dead",
     "T3", "active",
     """A direct correction of a widely repeated reading of the Andromeda change, from an operator with variations of his own winners among the top spenders in a live account.

**The claim.** "I have variations that are running in my account that are spending a large sum of money daily that are 100% variations of my winning ads. It's nothing new. It's what was already working... One of them is the top spender in my account right now."

**What actually changed is the ORDER, not the tool.** The old procedure, which he dates to 2017 and 2018, launched one net-new concept accompanied by three to five variations of it. The problem he names is that this spends variation budget on a concept nobody has validated yet. The new procedure is the reverse: **launch broad new concepts first, and only once a concept is validated do you build variations of it.** "Instead of going and testing like an ad on day one, you test five variations. You don't even know if this ad concept is validated yet. First, you want to validate the concept and then you go and test all these variations."

**Why this matters to us.** It reconciles two camps that read as contradictory. The volume camp is right that net-new concepts are the scaling input, and the iteration camp is right that variations carry spend, and the two are simply different stages of the same ladder. It also lines up with the one-concept-per-322 rule at [[Creative Science#CR-042|CR-042]], where all three creatives share a concept precisely so the variable under test is execution rather than idea. A concept that has not been validated has no business inside a variation unit.

**Guards.** One account, no screen, no numbers, no CPA and no dates on the ads he describes. It is an assertion against another assertion, and the useful part is the mechanism rather than the verdict.""",
     [MB_10])

mint(CR, "CR-226",
     "The creative diagnostic ladder is cost per click first as the warning light, then click-through rate, then cost per thousand, and the three are causally linked",
     "T3", "active",
     """The ad half of the failed-test diagnostic. US direct-to-consumer e-commerce benchmarks, practitioner numbers with nothing shown.

**The ladder.**
1. **Link cost per click** is the check-engine light. His target is **about $1.50** in the US. "It doesn't tell you what's wrong, but it tells you something is wrong." At two, three or four dollars, go to step two.
2. **Click-through rate.** Floor **3%, preferably closer to 4%**. Below 3% with an elevated cost per click, "you have a serious creative issue" and the diagnosis stops there.
3. **Cost per thousand impressions**, only if click-through rate is healthy and cost per click is still high. He refuses to give a hard target and says it is heavily niche and geography dependent, then offers **over about $80 in the US** as where he would draw a line.

**The loop that connects them, and it is why the ladder terminates at creative most of the time.** "Facebook likes to reward people that have really good creatives, really engaging creatives without pissing off all their users with low CPMs. So it's kind of a self-consuming issue. Your creatives aren't good enough, your CPMs will be higher and your CTR will be lower. So it's a perfect shitstorm for a really high CPC." His summary: **90% of what he sees is an ad problem**, and specifically operators who believe their ads are good.

**The mandatory counterweight.** He immediately warns against optimising these three for their own sake: high-curiosity native creative posts an excellent click-through rate and does not convert, "cuz you forgot to sell them". The ladder diagnoses a delivery problem. It never certifies an ad.

**Transfer warning.** These are e-commerce numbers on a link-click funnel. A lead-generation account on Instant Forms has no link cost per click of this kind and no comparable click-through band, so **do not carry $1.50 or 3% into a local-service account**. The funnel half of the same diagnostic is at [[Marketing Math & Unit Economics#MM-201|MM-201]].""",
     [MB_PR])

mint(CR, "CR-227",
     "Two operators independently reach the same research instruction in the same week: call your own customers and ask what ALMOST STOPPED them buying",
     "T3", "active",
     """Banked because the corroboration is what raises it above opinion. Two operators, different businesses, no shared source, arriving at the same question.

**The instruction.** Stop reading competitor ad libraries and speak to the people who already bought. "How many of you that have generated at least one customer in e-commerce have actually called one of your customers? How many of you have spoken to them on the phone? It's almost nobody. Yet here you go looking on the Facebook ad library... when you have the best source of data right in front of you." And the question that matters is not why they bought: **"a better question to ask is what was something that almost kept you from buying?"**

**The independent second instance.** Charley T's research process, on a real brand, surveys churned buyers with exactly that question and gets 49 of 62 naming price or suitability, then builds the winning concept on the 23 of 62 who "nearly did" not buy because they thought they were not serious enough about the category. See [[Creative Science#CR-221|CR-221]]. Two operators, one week apart, same question, same use.

**The named wrong source.** Comment sections. "It's like Facebook comments where all the lowest of the low people hang out", and the objection is structural rather than snobbery: comment threads select for people who did not buy and who are performing for an audience, so the signal is rage rather than hesitation.

**Two logical fallacies he names as the failure mode of swipe-led strategy**, and they are worth carrying because they are the honest limit of every competitor-research workflow in this codex. **Hasty generalisation**, it works for them so it must work for me, when the product, market, angle, page, funnel and ads all differ. **Survivorship bias**, reasoning from the visible winners while the identical strategies that failed are invisible.

Both instances are practitioner assertion. Neither shows a test comparing interview-led creative against library-led creative, which is the missing measurement.""",
     [MB_10, CT])

mint(CR, "CR-228",
     "The zero-asset peak workflow: three templates that need no brand files, plus a re-skin of the account's own top performers, inside an hour",
     "T3", "active",
     """A production fallback for a peak you are not ready for, from an agency running it on live client accounts. Its honest framing first: "AI isn't magic. It is a multiplier... Video generators particularly are just not there yet."

**Three templates that require no access to a brand's raw files.**
1. **A bare offer static.** Black background, the promotion in large type, brand logo. No imagery at all. He says it does particularly well in retargeting and warm audiences. Caution attached: if you let Advantage+ pull a product carousel underneath it, check the products pulled are relevant to the promotion.
2. **A transparent-centre PNG frame** in brand colours, carrying the promotion, uploaded manually into a dynamic product ad or catalogue carousel. For fashion or any account with a large SKU count already performing on catalogue.
3. **A fast-cut montage** assembled from images and video pulled off the brand's own website, to get many products in front of the viewer quickly, with the offer stated clearly and the logo on top.

**Then re-skin what already works.** Pull top performers two ways: the top 10 to 20 from previous peak periods, plus the top performers of the trailing 365 days. Volume scales with spend, and his worked example is a brand at **$60,000 a month, from which he pulled the top 20 to 30 assets**. Selection metrics: return on ad spend, low cost per result, low cost per click, high click-through rate, high hook rate, and amount spent as the confidence weight, "the more amount that you've spent on a certain ad, the more usable that data is".

**The access workaround worth knowing.** If the raw files are unreachable, search the winning ad's NAME inside the ad account's own media library and download the video, static or GIF directly from there. Any account you have access to carries its media library with it.

**The re-skin prompt, and the model constraint.** One static at a time, "turn this exact ad into a Black Friday version with the headline X, the discount Y, keep everything else in the ad exactly the same". Model behaviour and its aspect-ratio failure are recorded at [[Creative Science#CR-224|CR-224]].

**What it is worth.** He is explicit that this is for brands out of time or budget, not a replacement for new production, and the output is "at least having some base with a hypothesis" because it is built on assets that already won. Nothing was measured.""",
     [BS_ASSET])

print()
print("== Scaling Models ==")

mint(SC, "SC-155",
     "A promotional peak is the worst testing window of the year, because everything wins and none of the conclusions survive into January",
     "T3", "active",
     """The reasoning is seductive and wrong, and he names himself as having made the mistake: spend goes up fourfold in the peak, so it looks like the moment to put four times as much creative through. Two independent reasons not to.

**Reason one: the reads are worthless.** Everything posts a high attributed return in a peak. Buyers are cross-pollinating across every ad they see so attribution is scattered, and a heavy discount converts anyone already in the funnel regardless of what the ad looks like. "If you're doing a 60% off offer, it doesn't matter what you put in front of people... Whether it's a piece of UGC with an overlay or whether it's just a blank static image with an overlay, it doesn't matter." A conclusion drawn inside that window does not hold in a normal January or February.

**Reason two: the tests cost you the peak.** Testing fails at its normal rate, and that failure rate is now applied to the highest-spend weeks of the year. "Not only do you make the time period worse in terms of efficiency because you do a bunch of testing with the budget, but number two, all that testing is for nothing because you can't even use the insights moving forward."

**Where this sits in the codex.** [[Attribution & Incrementality#AT-081|AT-081]] already says never RUN an incrementality test in a high-seasonality month because seasonal noise swamps the effect, and [[Attribution & Incrementality#AT-084|AT-084]] says never READ a case study whose lift sits inside a promotional window. This is the same rule applied to ordinary creative testing, which is the case operators actually face every year. All three point one direction: **a peak is for harvesting, and the creative that harvests it should have been validated before it started.**

Asserted from agency practice plus his own stated error. No comparison run.""",
     [BS_BF])

mint(SC, "SC-156",
     "The post-peak slump is a funnel-emptying artefact you created, and the only real fix is paying for top-of-funnel through the peak at a loss",
     "T3", "active",
     """"Your Black Friday slump isn't the market, it's a planning problem."

**The mechanism.** A sale pulls forward everyone in the funnel who was going to buy at some point in the future. They all buy at once, the funnel empties, and Q1 declines because there is nobody left in it. The corollary is the one operators feel and rarely name: **the deeper the discount, the bigger the hangover**, because a deeper discount pulls more of the future forward.

**Three counters, in his order of preference.**
1. **Extend the sale** through rolling messaging: Christmas gifting, a January self-gift, Valentine's, back to school. Works, and it just moves the fatigue later.
2. **Discount less deeply.** A smaller peak, a smaller collapse, and the deferred sales are recouped later at full price, which he notes is arguably the better position.
3. **Keep buying top of funnel through November and December.** This is the one he calls best, and it is the one that costs you in-period profit.

**What counter three looks like in the account.** Spend naturally migrates to middle and bottom of funnel during a peak because that is where the immediate return is, and he agrees that is the correct read in the moment. The deliberate exception is a fixed allocation: **80% of spend on two creative types, 20% on top-of-funnel education.** The 80% is (a) a bare offer image with nothing else on it and (b) the account's existing best creatives with an offer overlay. The 20% will not return in period and will suppress contribution profit, and it is what keeps a funnel to convert in January and February. "This isn't going to realize into a good return immediately... but what it is going to do is prevent a lot of fatigue post sale."

**The structural reason the offer creative wins in a peak**, and it is worth stating because it explains why peak creative looks cheap: those ads are not appealing to a cold viewer. Almost nobody buys from a brand they first met on the Black Friday weekend. The offer static works because the viewer already knows the brand from September and October.

**The account-structure requirement, which is the operational core.** Do not put the top-of-funnel 20% in the same campaign as the offer ads. Meta can usually tell a top-funnel asset from a bottom-funnel one and route it, but **in a peak everything converts**, so the educational assets will be served to warm users, post a good attributed return, and never reach the new audience they were bought for. Separate campaign, with exclusions. His calibration: **30-day website visitors and existing customers, yes; 180-day website visitors is too aggressive** and starves the campaign of the signal it needs to optimise.

**The rule underneath all of it, stated twice.** To make November good you have to spend in September and October when the attributed return reads low. To stop Q1 collapsing you have to spend on top of funnel in November and December when the attributed return reads low. Both are the same act: prefilling a funnel that converts later. Consistent with the demand-harvest logic at [[Auction Mechanics & Bidding#AU-026|AU-026]] and with the exclusion-leak caution at [[Auction Mechanics & Bidding#AU-063|AU-063]].

Prescriptive, drawn from agency practice. No before-and-after account shown for any of the three counters.""",
     [BS_SLUMP])

print()
print("== Attribution & Incrementality ==")

mint(AT, "AT-113",
     "Google's return on ad spend multiplies overnight at a promotional peak and for most brands it is not incremental, so scaling into it buys revenue you already had",
     "T3", "active",
     """"Literally everyone does this."

**The trap.** Google's attributed return quadruples as November starts. The target is a 10, the account is reading a 40, and the arithmetic says pour budget in. **For roughly 70% of brands, he says, that return is not incremental.** The rise has two ordinary causes and neither is Google finding new demand: site-wide conversion rate is up because it is a peak, and Meta is driving people across platform who then complete on a branded or shopping click. Scaling into it buys more of the revenue you were getting anyway.

**The instruction.** Let Google run. Let the attributed return sit high. Do not treat it as headroom.

**How to hold this honestly.** The 70% is his own figure from audit practice with nothing published behind it, and he flags the exception himself, "this doesn't apply for everyone". The mechanism is the same last-click harvesting pattern this topic already documents, applied to the one moment in the year when the illusion is strongest and the budget is largest. It is also the reason [[Attribution & Incrementality#AT-081|AT-081]] refuses to run an incrementality test in November: the very window where you most want to know the answer is the window where the measurement is least trustworthy.

**Client-reporting consequence for us.** In a peak, a channel's attributed return rising sharply is the expected artefact, not evidence the channel improved. Say so in the report before anyone proposes moving budget onto it.

Asserted from audit practice across a stated 1,000+ accounts. No lift study shown.""",
     [BS_BF])

print()
print("== Learning & Signal ==")

mint(LS, "LS-075",
     "The DESTINATION decides what the pixel learns, so never run paid traffic to a page whose only available event is the one you do not want to optimise for",
     "T3", "active",
     """The cleanest statement of optimisation-event control on file, because the operator explains the choice as a media buyer rather than as a funnel preference.

**The refusal.** He will not run ads straight to his free community's join page, and he has never done it. "If I just run ads to the Skool group, pretty much the only thing you can optimize for is like a purchase or a complete registration, which is a join. I don't want to train the pixel for anyone to join the group. I only want qualified people to join the group." Owning the landing page is what buys the ability to choose which event fires.

**The build, and this is the part to copy.** A two-step opt-in. Step one takes name and email. Step two asks a single qualifying question, "which best describes you", with an answer such as a coach doing $10,000 a month or more, plus the phone number. Qualified respondents move to a video sales letter page which carries the **Complete Registration** pixel. Unqualified respondents go straight to the free community and **fire nothing**. So in that account Complete Registration means "qualified", and the campaign can also be optimised for a booked call or a completed application.

**The trade he accepts, stated plainly.** "I might get more joins in the Skool community if I ran it to the about us page, but I might not get as good a quality."

**The half that keeps it consistent with our own funnel law: unqualified people are still CAPTURED, never blocked.** They enter the community, they receive SMS and email and direct messages, they get retargeted, and calls still get booked from them, "cuz not everybody is truthful on the forms". Only the pixel event is withheld. That is the distinction our own rule turns on, capture never block, and it is what separates this from disqualifying a person on the form.

**Direct corroboration of the mechanism at [[Learning & Signal#LS-074|LS-074]].** Ben Heath reached the same mechanism four months later using conditional logic inside a Meta Instant Form: a respondent routed to a non-lead end page never registers as a lead, so the optimisation target silently narrows. Two operators, two different tools, one mechanism. **Neither of them measured the trade.** Nobody has published what happens to opt-in volume, cost per opt-in, show rate or close rate on either side of the change, and that number is available on our own accounts.

One operator, his own funnel, shown on screen. No comparison against the same funnel without the gate.""",
     [MS])

print()
print("== Amendments ==")

amend(CR, "CR-041",
      """**The specification half arrived 2026-09-03 and it belongs with this claim.** CR-041 gives the cadence, a written hypothesis before launch and a review seven days after. What it never specified is what the written thing has to contain. Professor Charley T's pre-launch specification supplies four parts: a hypothesis with a BECAUSE in it that names a business result, an explicit statement of what the test does NOT cover, a list written in advance of what a loss would put in doubt, and a statement of what a win breaks next. The third part is the one that changes behaviour, because without it a losing ad drags the product decision and the research back into the argument every time. Full contents and the worked example at [[Creative Science#CR-222|CR-222]].""",
      [CT])

amend(CR, "CR-185",
      """**A third spend-independent number joined the disagreement on 2026-09-03, and it is stated as a floor rather than a ratio.** Mark Builds Brands: "an absolute minimum of 25 net new concepts a week. That's completely new creative material. This is no variations, no iterations, new creative concepts." His diversity axis is FORMAT as much as idea, and he lists the formats he counts: distinct image concepts, short-form UGC, long-form UGC, full VSL and mini VSL. He attaches the number to no spend level at all, which is what makes it incompatible with both rules already in this claim: Blue Sense's one net-new ad per $1,000 of monthly spend would put 25 a week at roughly $100,000 a month, while Nick Theriot's concept ladder puts 20 concepts a week at a $40,000-a-month client. So the three cannot be reconciled by arithmetic, because one is a ratio to spend, one is a ratio to retainer, and this one is a fixed personal floor. Nothing is measured behind any of the three. Also note his own qualifier, "if you're just kind of starting out it'll be less", which he does not quantify.""",
      [MB_10])

amend(MM, "MM-085",
      """**The same trap stated as an operating error rather than a curve, 2026-09-03.** Blue Sense Digital gives the version an operator actually commits: keeping the business-as-usual efficiency target while running a discounted offer. His worked chain: a 50% gross margin brand with a 25% contribution-profit target sets a MER of 4, because MER 4 means 25% of revenue goes to marketing, leaving 25% contribution. Apply a discount, gross margin falls to 35%, hold MER at 4, and **contribution profit lands at 10%**, which is below most brands' operating expenses. "Meaning you lost money in November." *Arithmetic: 50 - 25 = 25, and 35 - 25 = 10. Both exact.* The instruction is the same as this claim's, reached without the UPT curve: **if the offer changes the unit economics, the efficiency target has to move with it**, whether that offer is a flat discount or a bundle. Read alongside [[Marketing Math & Unit Economics#MM-204|MM-204]], which supplies a second and independent reason the peak target must be tighter.""",
      [BS_BF])

amend(LS, "LS-074",
      """**Independently corroborated on a different tool, and the source predates this one.** Dr. Matt Shiver was running the same mechanism deliberately in April 2026, four months before Heath's reversal, using an owned two-step landing page instead of Instant Form conditional logic: qualified respondents reach a page carrying the Complete Registration pixel, unqualified respondents are routed away and fire nothing. Same mechanism, opposite tool, and he states the trade in the same terms Heath does, fewer registrations for better ones. Full build at [[Learning & Signal#LS-075|LS-075]]. **What neither operator supplies is still the number**: no before-and-after on opt-in volume, cost per opt-in, show rate or close rate exists from either of them.""",
      [MS])

print()
print("== Audit ==")
total, tiers, stat, per = audit()
print("TOTAL", total)
print("TIERS", tiers)
print("STATUS", stat)
for k, v in per.items():
    print("  ", k, v)
