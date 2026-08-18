---
title: "Auction Mechanics & Bidding"
type: codex-topic
claim_prefix: AU
created: 2026-08-18
tags: [advertising-science, codex]
---

# Auction Mechanics & Bidding

The Meta auction: total value equation, bid strategies, cost caps, pacing, and what actually sets your CPM.

Part of the [[00-Codex|Advertising Science Codex]]. Claims follow the tier system (T1 docs, T2 shown test, T3 practitioner, T4 theory).

## Claims

## How the auction decides winners

### AU-001 · Meta's auction winner is the ad with the highest total value, combining exactly three factors: advertiser bid, estimated action rate, and ad quality
Tier: T1 · Status: active
Bid is what the advertiser will pay for the outcome. Estimated action rate is the probability that showing this ad to this person produces the desired outcome. Ad quality is drawn from many sources including viewer feedback (hiding the ad) and detection of low-quality attributes such as withholding information, sensationalized language, and engagement bait. An auction runs every time there is an opportunity to show someone an ad; billions run daily across Meta technologies, subject to a price floor.
Sources: Meta Business Help Center, About ad auctions (https://www.facebook.com/business/help/430291176997542)
Last touched: 2026-08-18

### AU-002 · Estimated action rate plus ad quality constitute ad relevance, and a more relevant ad can beat competitors with higher bids
Tier: T1 · Status: active
Meta states: "Together, estimated action rates and ad quality measure ad relevance. Because these are components of the auction, an ad that's more relevant to a person could win an auction against ads with higher bids." This is the official basis for the claim that better creative lowers effective media cost; Blue Sense independently restates it as a $0.50 bidder beating a $1 bidder on relevance, so the cheapest cost reduction is relevance, not bid. Blue Sense adds that EAR and ad quality are diagnostic rearview mirrors built from historical performance, not live levers, since relevance is per-user; the actionable lever is wider creative diversity so more ads are relevant to more people. Meta also notes clickbait and engagement bait do not improve performance, and auction adjustments never cause a charge above the advertiser's bid. Multiple independent sources.
Sources: Meta Business Help Center, About ad auctions (https://www.facebook.com/business/help/430291176997542); Blue Sense Digital, How The Meta Ads Algorithm Works in 2026, 2026-07-28
Last touched: 2026-08-18

### AU-003 · Expected action rate appears strongly causal to CPMs: lead-magnet funnels see ~$25 CPMs vs ~$100 for book-a-call funnels on the identical lead event
Tier: T3 · Status: active
Lead-magnet landing pages convert at 30-70% vs 3-6% for book-a-call pages. Both fire the same lead event, yet book-a-call CPMs run ~4x higher, which Blue Sense attributes to expected action rate feeding the bid equation: Meta reads high on-page action rates as "people love this" and cheapens delivery. Implication: funnels engineered for high on-page action rates buy structurally cheaper impressions, an exploitable arbitrage. Their CRO video restates it second-order: raising conversion rate lowers CPMs slightly via EAR, but the effect is small enough not to chase for its own sake. The causal path between EAR and Meta inferring value is admitted speculation and no account data was shown.

Restated 2026-08-18 from the creative side, which adds the interpretive rule. Charley T frames CPM as a tax on attention, on the argument that the ad competes for attention against organic content in the same feed: "If people enjoy seeing your ad, it earns cheaper traffic. If they hate it, the platform taxes you with the higher CPM." A low CPM means the ad is interesting to strangers. A high CPM means it only works on people who already care about you. The operator rule that follows: a rising CPM on a prospecting ad means the creative stopped earning cold attention and the ad has quietly become a warm-audience ad regardless of targeting, so read prospecting CPM as a creative-quality readout and not only as a cost input. Reasoning only, no data shown, and it points the same direction as the expected-action-rate mechanism above.

The same speaker generalizes the mechanism one level up, added 2026-08-19. His model is that the platform optimizes for stickiness of the customer journey on its own surfaces, and prices advertising against that objective: advertising that supports the journey gets cheap impressions, advertising that degrades it gets priced out. "Remember, you're in a business partnership with a platform that is optimizing for the stickiness of the customer journey. If you don't help them do that, they'll just price you out of being able to work with them." The three inputs he says he manages are simplicity, value and identification. He endorses a viewer's observation that CPMs differ sharply between brands with strong organic engagement and brands without, which is the same argument arriving from outside the ad account. Theory, no data shown. Note the CPM-as-diagnostic reading here is contested by AU-024, where Faris and Meta's CMO read a rising CPM as the auction moving onto more valuable people rather than as a creative verdict.
Sources: Blue Sense Digital, How The Meta Ads Algorithm Works in 2026, 2026-07-28; Blue Sense Digital, eCommerce CRO Masterclass 2026: The Full System, 2026-08-10; Professor Charley T, The NEW BEST Meta Ads Andromeda Course to Scale in 2026, 2026-01-24; Professor Charley T, How to Scale Facebook Ads in 2026, 2026-02-28
Last touched: 2026-08-19

### AU-004 · Your bid is your unit economics: the competitor with better margin, AOV and LTV wins more auctions and can outscale you with worse creative
Tier: T3 · Status: active
The higher your sustainable bid, the more auctions you win and the more scale you achieve, so business strategy collapses into pricing strategy: maximize price, minimize COGS, and allocate the opened margin to acquisition. You cannot out-tactic bad economics, which is why Blue Sense audits start at the economics level. The same dynamic applies on Google. Structural argument from auditing 1,000+ brands; no dataset shown.

Worked example added 2026-08-18 from a second source. Two competitors sell the same product and both currently pay a $50 CAC; one extracts $80 per customer, the other $100. The $20 AOV delta is auction headroom, so the higher-AOV advertiser can bid up to $70 while the competitor stays capped at $50. It compounds, because acquisition is the expensive step and everything after it (email, phone, resell) is close to free. Cited to Dan Kennedy: the business that can spend the most to acquire a customer wins. Operator implication for AOV work: an AOV lift is worth more than the margin it adds, because it also buys auction position and scaling speed. Illustrative numbers, ASSERTED, no account data.
Sources: Blue Sense Digital, How The Meta Ads Algorithm Works in 2026, 2026-07-28; Mark Builds Brands, 8 years of marketing advice in 70 minutes, 2026-03-21
Last touched: 2026-08-18

### AU-025 · Maximize-conversions bidding routes spend to the lowest-CPA product, which is frequently the lowest-contribution-margin product
Tier: T3 · Status: active
Worked example: a $90 hoodie with $21 COGS and a $45 CAC contributes $24 per sale, while a tee with $27 gross margin and a $15 CAC contributes $12. Every platform's default bidding pours spend into the tee because its CPA is lower, so the account optimises itself to half the contribution margin per sale. Switching to maximize conversion value does not correct it when the low-margin product also carries the better ROAS: "So maximize conversion value won't fix this issue either. So segmentation is the way that you actually need to fix this." The only fix given is segmenting products into their own campaigns or ad sets by product-level unit economics, so the bid strategy is asked to optimise inside a margin band instead of across one. Second-order move: a product with an unusually cheap CAC may be selling on its own product-market fit, so pulling paid off it raises contribution per order and frees the budget for products that need paid to sell through. The parallel Google-side version of this failure is banked in the Google Auction & Smart Bidding topic. Numbers are an illustrative worked example, ASSERTED, no account data shown.
Sources: Blue Sense Digital, Everything You Need to Know About Finance in eCommerce, 2026-05-04
Last touched: 2026-08-18

### AU-047 · Pre-Andromeda practitioner model of the auction: predicted CTR times predicted CVR gives an expected CPA, and the bid is set at the level that still lands that CPA
Tier: T4 · Status: active
Two predictions per user, probability of click and probability of conversion. Meta reads the user's position in the vector space, reads the average CTR and average CVR of that region, multiplies them, and derives an expected CPA. In the worked example the expected CPA comes out at $30 and is on target, so the bid is set at whatever level still delivers that outcome. The stated constraint is that bidding too high on a user raises CPMs and the $30 CPA no longer holds. The $30 is a teaching number, not a measured result. The same speaker names logistic regression and tree-based models as the statistical methods he believes sit underneath, and says openly that Meta keeps the architecture private and this is inference from what practitioners can tell. Useful as a decomposition of the estimated action rate term Meta names officially in AU-001. STALENESS FLAG: recorded 25 March 2025, pre-Andromeda. Andromeda (announced December 2024, rolled through 2025) moved the retrieval stage onto deep neural ranking with a large jump in model capacity, so a regression-and-trees account of the stack is a historical snapshot. Bank it as the "before" picture.
Sources: Blue Sense Digital, How Machine Learning Works in Meta Ads (2025), 2025-03-25
Last touched: 2026-08-19

## Cost controls and manual bidding

### AU-005 · Across $200M of CTC cost-controlled spend, minimum ROAS bidding delivered 96.5-97% of the set target on average
Tier: T2 · Status: active
CTC reviewed $1.5B and analyzed $200M of cost-controlled spend across 253 accounts. On min ROAS 7-day click (the majority of their spend), a weighted average target of 236 delivered 228, which is 96.5% of target. The 7-day-click-plus-1-day-view setting delivered 101% of target; 1-day click missed target more often, consistent with a noisier window. Taylor Holiday's conclusion: Meta's capacity to deliver a set value outcome across a broad dataset is unbelievable, and "Meta is out to get you" is the dumbest counter-argument.
Sources: Andrew Faris, Do Cost Caps Work? Taylor Holiday Brings $200M Of Data, 2026-08-06
Last touched: 2026-08-18

### AU-006 · Cost-per-result bidding delivered 140% of target on average (a $78 bid produced a $108 CPA); bid cap was more accurate at 123%
Tier: T2 · Status: active
In the same $200M CTC dataset, cost-per-result goal on 7-day click delivered 140% of the set target (average bid $78, delivered $108). Bid cap came in at 123% of target but on only a ~$3M sample. In practice teams manage cost caps by repeatedly lowering the bid to drag actual performance to goal. The result drove CTC to change its default manual-bid type from cost-per-result to bid cap.
Sources: Andrew Faris, Do Cost Caps Work? Taylor Holiday Brings $200M Of Data, 2026-08-06
Last touched: 2026-08-18

### AU-007 · The average masks the distribution: 67% of min-ROAS accounts delivered more than 5% below their own target, and 75% on CPA goals delivered more than 5% above target
Tier: T2 · Status: active
While min ROAS averaged 97% of target in aggregate, most individual accounts miss on the bad side: 67% of min-ROAS accounts came in more than 5% below their ROAS target, and 75% of cost-per-result accounts came in more than 5% above their CPA target. Individual outcomes scatter widely around the aggregate line, the coin-flip small-sample effect. Operators should choose per client whether erring toward overspend or underspend hurts less: high-LTV brands tolerate CAC overshoot, first-purchase-margin brands should constrain.
Sources: Andrew Faris, Do Cost Caps Work? Taylor Holiday Brings $200M Of Data, 2026-08-06
Last touched: 2026-08-18

### AU-008 · CTC sets manual bids with a correction factor: multiply the true goal by 0.959 for min ROAS and 1.54 for cost-per-result
Tier: T2 · Status: active
From the delivery-vs-target distributions, CTC derived bid-setting factors analogous to incrementality factors: set min ROAS bids at 95.9% of goal and cost-per-result bids at 154% of goal. The 95%-confidence bounds are 90-101% for min ROAS and 145-164% for cost-per-result. Consistency matters more than accuracy: a control that reliably misses by a known percentage is fully usable because you offset the bid. These factors are also the foundation for automating bid-setting.
Sources: Andrew Faris, Do Cost Caps Work? Taylor Holiday Brings $200M Of Data, 2026-08-06
Last touched: 2026-08-18

### AU-009 · Accounts that persistently deviate from bid targets should keep cost controls and offset the bid, not abandon controls
Tier: T2 · Status: active
CTC's study table shows individual brands (e.g. "brand 14", a ~$6.9M-spend account) that consistently deliver far off target with no diagnosed cause even after checking Events Manager and EMQ scores. The response is an account-specific adjustment factor on the bid, the same logic as the global 0.959/1.54 factors. Persistent per-account deviation is a measurable offset, not proof the control is broken.
Sources: Andrew Faris, Do Cost Caps Work? Taylor Holiday Brings $200M Of Data, 2026-08-06
Last touched: 2026-08-18

### AU-010 · Rule of thumb: accumulate ~50 purchases before changing a manual bid
Tier: T3 · Status: active
Small samples are dominated by noise: three coin flips can all be heads without changing the 3,000-flip expectation. When forced to give media buyers an operational threshold, Taylor Holiday's answer is about 50 purchases, explicitly a reasonable-decision placeholder rather than a derived constant. It exists to stop buyers reacting to noise like one 5-item order doubling an ad set's apparent AOV.

A second practitioner lands on converging numbers for the adjacent decision, added 2026-08-19. Faris sets the minimum sample for trusting an ad set's AOV before restructuring a cap at 30 purchases for semi-reliable confidence, says plainly that 30 is honestly not enough, and puts real confidence at 50 to 100. Ten purchases showing $80 AOV against a $50 historical AOV is not a reason to blow up an ad set. The distortion he names is outlier orders: one $1,000 purchase sitting in a pile of $100 purchases moves the average a lot and is partly real, which makes it hard to discount. His judgement test is a sanity check on the store: two products priced the same on-site should not be producing $100 versus $50 AOV, so make the outlier prove itself. This is a different decision from Holiday's (how reliable is the AOV reading, not when to move the bid), the same order of magnitude, and neither number is derived. AU-044 shows him applying the 30-purchase floor live to reject a $108 AOV on 12 purchases.
Sources: Andrew Faris, Do Cost Caps Work? Taylor Holiday Brings $200M Of Data, 2026-08-06; Andrew Faris, How To Fix The Most Common Bid Cap & Cost Cap Mistake I See, 2026-06-25
Last touched: 2026-08-19

### AU-011 · Cost controls bid dynamically far above and below target early (up to ~9-10x) and condense as conversion data accrues, so accuracy improves with volume
Tier: T4 · Status: active
Min ROAS and cost caps both explore by bidding widely around the target at first, then converge; the first ~$10k of ad-set spend should show a wider outcome range than each subsequent $10k. This predicts that fewer ad sets with more conversions each land closer to target, and may explain why CTC's huge tROAS spend delivers near-target while smaller accounts see tROAS as unreliable. Bid caps do NOT bid dynamically, so at low conversion volume they can over-constrain delivery as Meta loses confidence. Mechanism reasoning consistent with but not yet isolated in the study, flagged as a follow-up research question.
Sources: Andrew Faris, Do Cost Caps Work? Taylor Holiday Brings $200M Of Data, 2026-08-06
Last touched: 2026-08-18

### AU-012 · Only enable cost controls at roughly $100k+ spend; they are stability tools that limit spend and can produce zero-spend days
Tier: T3 · Status: active
Cost controls only let Meta spend when it believes it can hit the set target, so under-threshold accounts starve; Piliero's agency enables them at ~$100,000+ spend and treats zero-spend days as a real operational risk. Set the cost per result goal exactly at break-even or target ($50, not $53 or $55): the goal is maximum profitable spend, not squeezing extra dollars. Bid caps are the most advanced but most stable, and "the biggest accounts in the world run on bid caps." Consistent with AU-011's prediction that control accuracy improves with conversion volume.

A second source sets a higher threshold on a narrower question, added 2026-08-18. Diversifying bidding strategies is only worth attention above roughly $200-250k/month, and 60% of Blue Sense's own client portfolio spends above $250k/month, which is why they almost never cover bidding publicly: "99.9% of people are not spending over 250k a month and so should not be concerned whatsoever with bidding strategies." He separates two things that get confused. Running a cost cap at any spend level is fine if you know what you are doing. Spending your management time testing and rotating bid strategies at low spend is the wrong bottleneck, and his test question is whether the business would double if you focused on bidding, which below the threshold answers no. He also kills daily bid tweaking and daily budget pacing outright as 2019-2020 tactics worth maybe 5% upside for an hour a day. ASSERTED, no data shown.
Sources: Sam Piliero, The Only Facebook Ads Video You Need in 2026, 2026-07-26; Blue Sense Digital, How To Structure A Meta Ads Account At Every Spend Tier In 2026, 2026-06-01
Last touched: 2026-08-18

### AU-013 · Do not run cost-capped and highest-volume campaigns simultaneously: the cap cherry-picks the cheapest conversions and distorts both readings
Tier: T3 · Status: active
The bid cap / cost cap / tROAS campaign takes the best-of-the-best purchases while the highest-volume campaign is left feeding top-of-funnel for the whole account. Result: the capped campaign looks artificially good and the highest-volume campaign artificially poor, corrupting the comparison and the budget decisions built on it. Only mix them in rare circumstances.
Sources: Sam Piliero, The Only Facebook Ads Video You Need in 2026, 2026-07-26
Last touched: 2026-08-18

### AU-014 · In a manual-bid incremental-attribution setup, a lander that performs to bid gets rapid day-over-day spend increases without auto-bid guesswork
Tier: T2 · Status: active
Once the new lander performed according to their bids in the She's Birdie account, Meta increased delivery day over day rapidly; the scaling procedure was raise the budget, keep the cost cap in a good spot, and let it run. Faris frames this as the payoff of manual bidding: performance-to-bid is the scaling signal. Meta also matched the new lander's persona to the right audience at scale within about a day.
Sources: Andrew Faris, The Secret To Great Landing Pages Is Simpler (And Harder To Execute) Than You Think, 2026-07-20
Last touched: 2026-08-18

### AU-015 · Switching campaign bid strategy from highest volume to a cost control silently changes the attribution setting to 7-day click only
Tier: T2 · Status: active
Demonstrated live in Ads Manager: with highest volume the ad set runs 7-day click, 1-day view, 1-day engaged; select ROAS goal and the ad set attribution model collapses to 7-day click. Any bid-strategy change must be re-checked at the ad set level because it alters what the campaign optimizes against.
Sources: Sam Piliero, The Only Facebook Ads Video You Need in 2026, 2026-07-26
Last touched: 2026-08-18

### AU-016 · To set a bid under incremental attribution you must first measure IA's own incrementality factor with lift studies, because the target embeds the factor
Tier: T3 · Status: active
CTC is running conversion-lift studies on individual holdouts specifically to learn IA's incrementality factor before rolling IA out broadly, since manual-bid targets are set with the incrementality factor baked in. Early results (CTC's and Haus's) showed IA has a HIGHER incrementality factor than standard attribution, meaning Meta under-reports more under IA, so raw IA numbers must be adjusted up more. You cannot port your standard-attribution bid target to IA unchanged. No factor values published yet.
Sources: Andrew Faris, Do Cost Caps Work? Taylor Holiday Brings $200M Of Data, 2026-08-06
Last touched: 2026-08-18

### AU-017 · Meta's March click-definition change hurt delivery on manual-bid, click-optimized accounts, which pushed the retest of incremental attribution
Tier: T3 · Status: active
When Meta changed its definition of a click (March, pre-Aug 2026), early-to-mid 8-figure ecommerce accounts optimized on click attribution with manual bids got noticeably less volume than expected even after adjusting attribution settings. Accounts were not on fire but persistently under-delivered. Switching those accounts' bidding to incremental attribution restored and improved performance on every measurable outcome. Pattern observed across Faris's client book; no numbers shown.
Sources: Andrew Faris, DTC Brands See 38% Better Meta Ads Performance When They Switch To Incremental Attribution - Olivia, 2026-08-10
Last touched: 2026-08-18

### AU-026 · Cost caps produce a burst of exceptional results and then tank, because the cap harvests the conversions already sitting in the funnel
Tier: T4 · Status: active
Mechanism claimed: a cost cap cherry-picks the cheapest bottom-of-funnel conversions that are already in the funnel, so the account harvests and then falls off a cliff with nothing behind it. Highest volume, maximum conversions, or old auto-bid builds slower and compounds, so every day trends as good as or better than the last. This supplies the mechanism for why an early cost-cap result flatters, and it complements AU-012 (only enable cost controls at roughly $100k+) and AU-013 (never run capped and highest-volume campaigns simultaneously). Operator instruction: judge any bidding change on week-over-week data sets so the harvest-and-crash shape is visible, and do not read the post-harvest slump as the account breaking. The same speaker separately predicted in January 2026 that cost-capped campaigns would all tank about three weeks into January, and repeated the forecast in February ("all the cost caps in the world are going to fail in a week"), naming the configuration risk of a high budget ceiling sitting behind a low bid, which leaks thousands of dollars when the crash lands. He does not explain the January mechanism in either stream and published no follow-up data, so treat the seasonal timing as unverified and the config risk as the usable half. Reasoning only, no data shown.

Two further statements from the same speaker sharpen the seasonal forecast into something falsifiable, added 2026-08-19. In December 2025 he moved the failure point from January to February and pinned it to a specific calendar cluster, the Super Bowl and Valentine's Day weekend, claiming a six-year post-COVID streak of ecommerce cost caps breaking there: "it always breaks at the same time it's clockwork it's Valentine's Day weekend it's the Super Bowl it's Valentine's Day." In January 2026 he named the configuration that breaks, low bid plus high budget, and forecast failure within a couple of weeks: "for all of you low bid, high budget folks, your cost caps are going to break in the next couple of weeks. They do every February for so many reasons." That confirms the config risk already recorded above. The mechanism he implies is that consumers have already made their large seasonal purchases, so the cap can no longer clear the auction at the required volume. Across all four statements the timing has moved (three weeks into January, a week in February, every February, the Valentine's and Super Bowl cluster) and none carries account data, so the date is still unverified. It is directly testable on any of our accounts running caps through a February.
Sources: Professor Charley T, Record Profits: the Meta Ads Andromeda Playbook, 2026-01-03; Professor Charley T, Meta advertisers... We've got a big problem, 2026-01-17; Professor Charley T, Q5: the 2nd Black Friday: Meta Ads for Profit, 2025-12-20; Professor Charley T, How to Scale Profits with Meta Ads, 2026-01-24
Last touched: 2026-08-19

### AU-027 · Bid caps and cost caps deserve at most 5-10% of budget, except roughly two months a year when they act as a cheat code
Tier: T3 · Status: active
The two named windows are the month leading up to Black Friday and sometime in late spring. He gives no reason for late spring. The implied mechanism is that auction dynamics in those windows make a capped bid unusually efficient, presumably because competitor budgets and inventory prices move sharply, but that is inference and not stated. This is a when-to-use rule, not an accuracy rule, so it sits alongside AU-005 through AU-011 (how close controls land to target) and AU-012 (the spend threshold) rather than replacing them, and it is consistent with AU-026's harvest mechanism if the funnel is fullest in those windows. Asserted with no account data.
Sources: Professor Charley T, The BEST AD ON META after Andromeda, 2026-01-10
Last touched: 2026-08-18

### AU-028 · Under a bid cap, Meta widens reach on its own when demand rises, so a seasonal account does not need a separate reach intervention
Tier: T3 · Status: active
On a heavily seasonal gift brand doing about 40% of revenue in 30 days, Faris left the manual bid untouched going into peak. Meta saw conversions landing under the cap and extended delivery to a broader group by itself. His conclusion: an account that reaches few people for most of the year did not have a prospecting problem, because Meta found those people once demand made them findable. Recorded here as a counterweight to the cost-per-thousand-reached thesis Phil Kiel argues in the same conversation, that falling reach is itself the problem to manage. Kiel did not dispute the bid-cap case and reframed CPMR for it as a post-hoc diagnostic: was this year better or worse, and was the cause creative, product, or cheaper reach. The practical split both sides land on is that auto-bid accounts must manage reach structurally while bid-cap accounts get reach expansion priced in automatically. Account observation, ASSERTED, no numbers shown.
Sources: Andrew Faris, Your Meta Ads Account Has Too Many Campaigns, Here's Why And What To Do About It (With Phil Kiel), 2026-05-12
Last touched: 2026-08-18

### AU-029 · A bid cap is only correct relative to the AOV the ads are currently producing, so it must be re-derived whenever product mix, bundles or promos move AOV
Tier: T3 · Status: active
On a three-SKU brand running rotating bundles and promos, a static bid cap either loses money or underspends the moment AOV shifts. The bid is tied to the average order value the ads are actually driving, not the sitewide historical figure. This is the operating-cadence version of AU-004 (your bid is your unit economics) and of MM-017 (sitewide AOV is the wrong divisor for wide-catalog brands): the calculation is recurring, not one-time. Faris's consequence for the role is that the media buyer has to sit inside the forecast rather than downstream of it, and he names this linkage as the buyer's remaining job in the "media buying is dead" argument. Asserted on a podcast, no worked example shown.

The same speaker supplied the worked mechanism two months later, added 2026-08-19. The full cross-sectional version, one cap sitting across products of different AOV at the same moment, is banked at AU-039 through AU-045. He also names the analysis-window trap that this claim's promo case implies. Discounts and gift-with-purchase offers move AOV sharply, so never pull an AOV reading across a window that straddles a promo boundary, because you are averaging two different price regimes. His rule: "if your promo ended two days ago, don't go looking at what the AOV was three days ago when you do your AOV analysis, uh because it's no longer relevant because you were charging a different price then." Combined with AU-010's 30-purchase floor this is a real operating bind: you need 30 to 100 purchases to trust an AOV, and you must not cross a promo boundary to collect them, so promo-heavy accounts may never have a clean window.
Sources: Andrew Faris, From A 65% Decline To All-Time Revenue and Profit Highs With Richie Mashiko From She's Birdie, 2026-04-27; Andrew Faris, How To Fix The Most Common Bid Cap & Cost Cap Mistake I See, 2026-06-25
Last touched: 2026-08-19

### AU-030 · At high spend, a second ad account on the same pixel and page running different bid logic enters auctions the primary account is not bidding on
Tier: T3 · Status: active
Configuration described: primary account on maximize conversions, secondary account on maximize conversion value or on cost caps or bid caps, with the same creative, the same pixel and the same page. The mechanism claimed is that different bid strategies enter the auction with different bids, so the second account reaches volume the first cannot. He states plainly that the self-competition objection, that cross-bidding raises your own CPMs, is unproven either way, and argues that same-page and same-pixel should limit it. The de-risking half of the argument is unconditional: an account ban or a billing failure otherwise zeroes new-customer acquisition for a week. He warns the tactical detail changes every six months. Only relevant above the bid-strategy attention threshold recorded in AU-012. ASSERTED, no data shown.
Sources: Blue Sense Digital, How To Structure A Meta Ads Account At Every Spend Tier In 2026, 2026-06-01
Last touched: 2026-08-18

### AU-033 · On a brand-new pixel, launch on cost caps to buy conversions off other bidders and seed the model, then abandon them
Tier: T4 · Status: active
For a pixel with no purchase history, Charley T's launch move is cost caps, explicitly to take sales from other bidders in a high-demand window such as Christmas: "I might launch with cost caps just to start to steal sales from other people. It's not sustainable, but it's a great way to teach your machine what to get." He is direct that the tactic is not sustainable and frames it as teaching the model what to fetch. Provenance he gives for the whole cost-cap method now circulating in the market: a 70-page manual he wrote with Meta in 2018, of which the popular version uses roughly pages 13 to 15 without the surrounding context. A new pixel sits below every threshold in AU-012, which sets a roughly $100k spend floor for cost controls, so read this as a deliberate temporary seeding move with a planned exit rather than a standing configuration. AU-012's own second source already allows that a cap at any spend level is fine if you know what you are doing, which is where these two land compatibly. Reasoning, no test shown.
Sources: Professor Charley T, Mastering Andromeda: Creative Testing and Scaling, 2025-12-13
Last touched: 2026-08-19

### AU-039 · A cap is a permission to spend tied to the optimization event, and cap logic exists only inside highest volume bidding, never inside highest value / target ROAS
Tier: T3 · Status: active
Faris's definition: a cap controls how much money Meta may spend relative to the optimization event you selected. "Do not spend unless your forecast says you will get the conversions in this ad set at the price that I've selected for this bid cap or below it. In the case of cost cap, at the average price that you did." A bid cap enforces the price per auction; a cost cap enforces it at the average. Nothing in the cap logic applies to highest value bidding with a target ROAS, which is a separate control with its own accuracy profile (AU-005). He treats bid cap and cost cap as interchangeable for the AOV problem in AU-040 and states his own preference for bid caps. Terminology trap worth flagging before anyone reads these claims side by side: "highest volume" here means the conversion-count optimization that caps sit inside, while AU-013's "highest volume campaign" means an uncapped auto-bid campaign. The two claims use the same phrase for different things and do not conflict.
Sources: Andrew Faris, How To Fix The Most Common Bid Cap & Cost Cap Mistake I See, 2026-06-25
Last touched: 2026-08-19

### AU-040 · A cap is a cost target with no AOV term, so one cap across mixed-AOV products produces a different ROAS per product and Meta drains the budget onto the cheapest one
Tier: T3 · Status: active
This is the core mechanism and it has direct operating consequences. A cap is a CPA control and it never reads average order value: "Cost caps and bid caps have no consideration for the average order value and therefore, when you set your cost cap or your bid cap, you don't actually know what average order value you're going to get and therefore conversions have really different values to you." At a $50 cap, a $50 AOV product returns 1.0 ROAS, an $80 AOV product returns 1.6, a $90 AOV product returns 1.8, and a $100 AOV product returns 2.0. The gap bites far below the extreme spread. Meta then shifts spend disproportionately onto the low-AOV SKU, because a 1.0 ROAS conversion is easier to buy at the capped price than a 2.0 ROAS conversion, and Faris says all of the money goes there. Account example: he took over an account where the previous buyers ran a roughly $250 AOV SKU and a $400 AOV SKU inside the same highest volume campaign, and spend had concentrated on the $250 SKU. The fix was to split the top two SKUs into their own ad sets inside the same CBO campaign with a manual bid on each; the client was then surprised at how much of the $400 product moved, which had looked like a slow mover only because nobody was watching this. He flags that $10 AOV gaps are almost invisible in the Meta UI because most advertisers do not carry AOV in their column set. Number provenance: the auto-transcript dropped the figure at first mention ("a SKU that produced like a uh AOV"), and Faris names it as the "$250 AOV SKU" later in the same episode, so read $250 as approximately right and the $400 as stated. Operating rule for our accounts: any capped ad set carrying more than one price band is running an uninterpretable cap. Asserted from operating experience with the arithmetic shown, no split test.
Sources: Andrew Faris, How To Fix The Most Common Bid Cap & Cost Cap Mistake I See, 2026-06-25
Last touched: 2026-08-19

### AU-041 · Judge a cap by the AOV-to-cap ratio, which is just ROAS, never by the raw CPA number, and stop carrying one CAC target across a multi-product brand
Tier: T4 · Status: active
The reading rule that follows from AU-040. "Judge the cap, or really any highest volume bidding, the CPA target against the AOV to cap ratio. It's really just the ROAS. You have to judge it against the AOV, not just a raw cap number, not just a raw CPA number." Faris says it bothers him when operators quote a single CAC or CPA target, because the correct question is on what products, and most brands run multiple offers, so one CAC target carries almost no information. The two failure modes of a single cap across mixed AOV are symmetric and both cost money. Set too low and it is an opportunity cost problem, the higher-AOV products you actually want to buy never clear the forecast and never get spend. Set too high and it is a negative-ROAS problem, the ad set overspends on the cheap products and ad set ROAS collapses: "a cap set too low ends up starving the higher AOV products that you'd actually want to spend on. A cap set too high drives down the ROAS of an ad set because it overspends on low AOV products." Reasoning, no test attached. AU-044 is this rule confirmed on screen, where a 89% CPA gap between two ads turned out to sit on roughly equal ROAS.
Sources: Andrew Faris, How To Fix The Most Common Bid Cap & Cost Cap Mistake I See, 2026-06-25
Last touched: 2026-08-19

### AU-042 · Meta announced at its 2026 Performance Marketing Summit that it is building a ROAS guardrail on top of a CPA target, which would retire most manual AOV-coherence work
Tier: T3 · Status: active
Faris reports Meta announced a product letting an advertiser layer a ROAS adjustment onto a cost cap or CPA target, so you could ask for the lowest-cost conversion available subject to a floor such as a 2.0 ROAS. Announced, not shipped, at the time of recording on 25 June 2026, and he says he does not know the final shape of the tool. He expects it to date his whole episode, and calls the current manual state a constant pain and very error-prone. Tiered T3 rather than T1 because this is a secondhand verbal report of an unshipped announcement with no Meta documentation attached; upgrade to T1 and re-tier the surrounding claims once the feature appears in Meta's bid-strategy docs. Review trigger: check those docs before leaning on AU-040, AU-041, AU-043 or AU-045, because a shipped ROAS guardrail changes what a capped ad set needs to look like and removes the reason for splitting SKUs by price band.
Sources: Andrew Faris, How To Fix The Most Common Bid Cap & Cost Cap Mistake I See, 2026-06-25
Last touched: 2026-08-19

### AU-043 · Live account: five ad sets carrying caps of $70, $75, $75, $70 and $77, with the $77 reserved for the single-product ad set producing $97 AOV
Tier: T2 · Status: active
Screen-shared client campaign covering 22 to 23 June 2026, a window he picked because a sale ended and a new offer went live on those dates. Ad set 1 is a product mix at $65 AOV. Ad set 2 is a single isolated product, the reliable spender, at $97 AOV across 23 purchases in two days. Ad sets 4 and 5 are mixes. He pushed the cost control on the isolated $97 AOV ad set to $77 while the rest sit at $70 to $75: "I've pushed the cost control up to $77 in this case above 70, 75, 75, and 70 for the rest of these. And it's actually getting a lower CPA than that right now for a bunch of different reasons, but that's because it's relative to this $97 AOV, which I basically trust." The cap was raised on non-sale historical AOV he trusts, not on the two-day sample, and he said he would keep watching as the sample builds. This is AU-040 and AU-041 executed: the spread of caps across ad sets tracks the spread of AOV across ad sets, and the isolated single-product ad set is the one that earns a differentiated cap. In-account numbers shown, observational, not a controlled test.
Sources: Andrew Faris, How To Fix The Most Common Bid Cap & Cost Cap Mistake I See, 2026-06-25
Last touched: 2026-08-19

### AU-044 · Inside one mixed ad set, two ads produced $108 AOV at $85 CPA and $46 AOV at $45 CPA at similar ROAS, and sample size decided which number to act on
Tier: T2 · Status: active
The two top-spending ads in a mixed ad set showed $108 AOV on 12 purchases and $46 AOV on 25 purchases, at CPAs of $85 and $45. "The ROAS is actually relatively similar on both, even though the CPA is very different on the two of them, 45 and 85." That is AU-041 in one screenshot: two CPAs 89% apart sitting on roughly equal returns, so the raw CPA carried no decision information without the AOV beside it. Faris refused to act on the $108 figure because 12 purchases is too small and too noisy, consistent with the 30-purchase floor in AU-010. He acted on the $46 figure because the sample was building and because checking the website confirmed the product was heavily marked down. The trap he names: a $70 cost cap running against a $46 AOV is a recipe for overspending, and the high-AOV product will eventually be underspent inside the same ad set. Numbers shown on screen, single account.
Sources: Andrew Faris, How To Fix The Most Common Bid Cap & Cost Cap Mistake I See, 2026-06-25
Last touched: 2026-08-19

### AU-045 · A heavy sitewide markdown on one SKU pulls cost-capped spend onto it, so a price change on the website is a delivery change in the ad account
Tier: T2 · Status: active
Faris confirmed the AU-040 mechanism live. The ad soaking up spend at $46 AOV pointed to a product dramatically discounted on the website: "the product is dramatically marked down in its price. So it's not surprising exactly what I was saying earlier, which is that Meta is shifting spend toward a product that is a really low AOV for precisely the reason I said earlier. It's on a cost cap. It's going for highest volume." His prescribed fix was not in the ad account. First, ask the client to raise the price on that product now that new creative is performing, on the theory that the markdown was originally applied because old creative made the inventory look slow-moving. Second, re-merchandise the collection page the ad points at: move the bundles up the page, remove the sold-out product, then watch for a couple of days. The operating consequence for us is a process one. On any capped account, ecommerce promo calendars, markdowns and free-shipping-threshold changes must reach the media buyer before they ship, because they are delivery changes. Live diagnosis with numbers shown, single case.
Sources: Andrew Faris, How To Fix The Most Common Bid Cap & Cost Cap Mistake I See, 2026-06-25
Last touched: 2026-08-19

### AU-046 · The default for conversion-optimized ads is broad targeting plus a manual bid: set the price at which Meta may spend, then get out of the way
Tier: T4 · Status: active
Two episodes, one position. The Andromeda-era argument: improved ad ranking makes the machine better at matching, so operator interference costs more now than it used to, which makes broad plus manual bids more correct after Andromeda than before it. "Run broad targeting, run your manual bids, set a price at which Meta can spend, get out of the way, let the machine learning do the work." The second episode names the failure mode it prevents. Auto-bidding is one of the standard justifications for structural below-target spend, where operators accept losing days as the price of finding the upper spend limit, and a manual bid removes the excuse: "Mostly for conversion optimized ads you should just be running them in a manual bid and let Meta sort out the return that you're going to get." He accepts genuine exceptions for new accounts and new channels, and acknowledges nuance around predictive forecasting and sample size that can make a poor-looking ad worth leaving on. This is the stance underneath AU-039 through AU-045 and it presumes the AOV coherence those claims require, so adopting it without fixing ad set AOV coherence first reproduces the AU-040 failure. Asserted, no test data in either episode.
Sources: Andrew Faris, The 3-Part Creative Diversity Framework I Use To Scale Past $10M On Meta Ads, 2026-05-01; Andrew Faris, The One Part Of Your Business Where You Should Be Wasting More Money, 2026-06-15
Last touched: 2026-08-19

### AU-048 · Cost caps work by forbidding the model from overbidding on an expensive user, and the hard prerequisite is creative velocity most seven- and eight-figure brands do not have
Tier: T3 · Status: active
The mechanism given: a cap fixes the bid ceiling inside the auction, so when a competitor bids up a user, Meta walks away rather than winning at an unprofitable price. The speaker rates the structure highly on efficiency and calls it desirable if you can get it to work. He then attaches a constraint nobody else in this topic names, the creative volume needed to sustain it: "most people just aren't doing enough creative to even sustain cost caps at the spend levels that they want. And so they're kind of better off just bleeding in efficiencies in over bidding on particular users than constraining their spend and constraining volume." His judgement is that most seven-, eight- and possibly nine-figure brands do not produce enough creative, and he explicitly rejects blanket "run cost caps" advice as unconstructive for the majority. This is a creative-supply threshold sitting alongside the spend thresholds in AU-012 (roughly $100k) and AU-012's second source (roughly $250k/month), and for our client sizes it is likely the more binding one. It also supplies the missing prerequisite for the zero-spend-day risk AU-012 names: a capped ad set starves when the creative cannot find enough people who clear the cap. Practitioner opinion from agency work, no account data shown.
Sources: Blue Sense Digital, How Machine Learning Works in Meta Ads (2025), 2025-03-25
Last touched: 2026-08-19

## Value rules

### AU-018 · Value rules adjust bids up or down by age, gender, device platform, mobile OS, location, audiences, conversion location, or placement, without hard restrictions
Tier: T3 · Status: active
Value rules (introduced 2025) tell the auction to bid more or less for specific criteria, for example bid more for ages 35-54 or less for certain countries. As of Aug 2026 the supported criteria are age, gender, device platform, mobile operating system, location, audiences, conversion location, and placement. They shift delivery probabilistically instead of excluding anyone.
Sources: Jon Loomer, Ask These Questions Before Using Value Rules, 2026-08-12
Last touched: 2026-08-18

### AU-019 · Never hard-exclude an underperforming demographic segment; apply a bid-decrease value rule instead (10-20% for tuning, up to the 90% maximum for effective exclusion)
Tier: T3 · Status: active
Multiple independent sources converge on the same move. Piliero: removing e.g. 65+ or 18-24 from delivery loses money and scale potential; decrease the segment's bid 10-20% in a NEW ad set containing proven best ads so the rule's effect is isolated like an A/B test, and Meta then only buys that segment when it returns ~10% better than current. Shiver: a 90% bid decrease (the platform maximum) on age brackets outside the real buyer band (e.g. keeping 25-45, downweighting 45-54, 55-64, 65+) effectively excludes them while Advantage+ expansion stays intact, configured at ad set level under value rules > audience > age. Loomer: exclusions remove all chance of conversion from a segment and shrink the pool (raising CPM), while a bid-down rule keeps the segment eligible at reduced spend; he applies it to non-purchase optimization problems and LTV differences by demographic. Multiple independent sources; none showed isolated A/B data.

A fourth practitioner adds the ordering rule and names the anti-pattern, 2026-08-19. Charley T's version is to bid DOWN on the segments you do not want and never bid UP on the segment you do. If the ideal customer is a woman over 35, cut the bid on men by 75% (so you are willing to pay 25% as much to reach them) and cut it on under-35s, rather than adding a bid increase on women over 35. His argument: "Where people get this wrong is they say, 'I want women over the age of 35, so I'm willing to increase my bid against that audience.' That is where things go horribly wrong cuz you're basically saying, 'This is my ideal customer. I'm willing to make less money on them.'" He notes the bid-down configuration is close to hard targeting plus expansion, with more control. This converges with the Loomer and Heath positions recorded in AU-020 and AU-021 on the bid-up case. The single exception he allows is banked at AU-036. Practitioner rule, no test shown.
Sources: Sam Piliero, The Only Facebook Ads Video You Need in 2026, 2026-07-26; Dr. Matt Shiver, How to Run Facebook Ads for Coaches & Agency Owners (FREE COURSE), 2026-08-04; Dr. Matt Shiver, The 'Right Way' to Run Facebook Retargeting Ads in 2026, 2026-07-28; Jon Loomer, Ask These Questions Before Using Value Rules, 2026-08-12; Jon Loomer, You May Be Surprised Who Converts, 2026-07-22; Professor Charley T, Facebook Ads in 2026: NEW Secrets, Tips & Strategies, 2026-04-15
Last touched: 2026-08-19

### AU-020 · When to apply value rules: only with a proven, data-backed delivery problem, or as always-on standard practice
Tier: T3 · Status: contested
Loomer's position: value rules intentionally increase costs by construction, so they are only justified when you have information Meta lacks (offline lead quality, LTV by segment) AND Meta is actually misallocating meaningful budget against that information; applying one without a demonstrated problem raises costs for nothing, and raising bids on groups Meta already prioritizes is pure cost inflation with no delivery gain. Shiver's position: he applies the 90% age bid-down on nearly every ad set as always-on standard practice, treating ICP age steering as a default rather than a diagnosed exception. Neither side showed test data isolating the cost effect.
Sources: Jon Loomer, Ask These Questions Before Using Value Rules, 2026-08-12; Dr. Matt Shiver, How to Run Facebook Ads for Coaches & Agency Owners (FREE COURSE), 2026-08-04
Last touched: 2026-08-18

### AU-021 · Value rules raise bids on first-party-known high-value segments (e.g. +60% bid for a segment worth 60% more) without restricting targeting
Tier: T3 · Status: active
Meta already sees who converts from tracked conversion actions, but not off-platform value data like repeat purchase rate or phone-call-to-client close rate by segment. Value rules feed that in: "these people are worth 60% more, increase my bid by 60%", by age, location, or device. Improves overall ROAS and lead quality at budgets where the customer data exists; $100k/month has the data. The 60% figure is illustrative, no before/after account data shown. Note the tension with AU-020: Loomer would require proof Meta is misallocating before paying more.

Restated 2026-08-18 with the anti-pattern named explicitly, which is the operationally important half. The big mistake Heath sees is building a value rule out of where the account's purchases or leads already come from: if Meta can already see that over-35s convert better, Meta is already delivering mostly to over-35s, so paying a premium for them buys nothing. Value rules are only for information the system is structurally blind to, and he gives two: conversion rate from lead to customer (offline, never reported back), and repeat purchase rate beyond the attribution window. He also states the required posture, that the multiplier must come from measured segment value rather than a guess, and the sophistication claim that advanced advertisers now leave ad-set targeting alone entirely and steer through value rules instead. Build path shown live: All tools, Advertising settings, Value rules, Create a rule set, select audience, select criteria (e.g. age 35+), set the bid increase, name and create; then apply it at ad set level in the Value rule section by choosing the rule set. Different rule sets can apply to different offers, campaigns, and ad sets. This lands Heath on Loomer's side of the AU-020 split for the bid-UP case, narrowing that contest: both now agree raising bids on what Meta already prioritizes is pure cost inflation. AU-020 stays contested because it also covers Shiver's always-on bid-DOWN practice, which neither addresses here.

A third source pushes the caution past Heath's, added 2026-08-19. Charley T treats any bid increase on the ICP as self-harm regardless of what the off-platform data says, and inverts the whole move into bid-downs on everyone else (banked at AU-019). He allows exactly one bid-UP case, and it is triggered by on-platform economics rather than off-platform value: a segment already beating target CPA while starved of spend share (AU-036). So the operating split now reads as two different triggers for the same lever. Heath bids up on segments worth more in data Meta cannot see. Charley T bids up only on segments Meta is under-delivering against your own CPA target. Neither ran an isolated test.
Sources: Ben Heath, $100 vs $100,000 Facebook Ads Strategy, 2026-08-12; Ben Heath, Learn 97% of Meta Ads in Under 29 Minutes, 2026-08-18; Professor Charley T, Facebook Ads in 2026: NEW Secrets, Tips & Strategies, 2026-04-15
Last touched: 2026-08-19

### AU-022 · A 90% bid-decrease value rule on Android devices reduces foreign leads in US-targeted campaigns
Tier: T3 · Status: active
Meta's location setting targets people who live in OR recently visited the country, so US campaigns leak to visitors. When lead quality complaints include foreign leads, Shiver adds a value rule decreasing bids 90% on Android devices, since foreign visitors skew Android and iOS skews to US residents with higher socioeconomic status. Flagged as an occasional fix, not a default.
Sources: Dr. Matt Shiver, How to Run Facebook Ads for Coaches & Agency Owners (FREE COURSE), 2026-08-04
Last touched: 2026-08-18

### AU-036 · The one case for raising a value-rule bid is a segment already beating target CPA while starved of spend, and the second-order gain is that the dominant segment stops buying its expensive marginal conversions
Tier: T3 · Status: active
Charley T's stated exception to his own bid-down-only rule in AU-019, with worked numbers. Target CPA is $50. Women over 54 convert below $20 but take only 15% of spend: "Let's say my target cost is $50, and women over the age of 54 are coming in at below 20, but they're only getting 15% of my spend. Well, the machine's not showing my ads there because of user experience and a bunch of other things, but I could say, 'I'm willing to increase my bid against that audience by 50%.'" A 50% bid increase accepts a $20 to $30 CPA there, still well inside the $50 target, and pulls spend share toward them. He expects the dominant segment, women 35 to 44 at 80% of spend and a $49 CPA, to fall to around 60% of spend and get more efficient, because at 80% share it is buying its expensive marginal conversions and at 60% the remaining spend sits on lower-hanging fruit inside the same segment. He frames value rules as rounding the edges of delivery rather than steering it. The diagnostic that identifies the case: a segment beating target CPA while holding a small share of spend, which is Meta declining to deliver there. Note this is the opposite trigger to AU-021. Heath raises bids on segments worth more in off-platform data Meta cannot see; Charley T raises them only on segments Meta already prices cheaply on-platform but under-delivers. The two are compatible and both are narrower than a general bid-up habit. Worked numbers, no account screenshots.
Sources: Professor Charley T, Facebook Ads in 2026: NEW Secrets, Tips & Strategies, 2026-04-15
Last touched: 2026-08-19

## CPM economics

### AU-023 · Meta CPMs are a demand-supply price; supply is still growing, and digital advertising has grown from 1% to roughly 1.3-1.4% of the global economy
Tier: T3 · Status: active
Meta CMO Alex Schultz frames CPM as a pure demand-supply function and rejects the idea that inventory is capped: TikTok created large new time-spent supply (mostly pulled from TV), and digital platforms grew total advertising from a long-stable 1% of the global economy to about 1.3-1.4%. Rising CPMs therefore reflect both more advertiser demand and more efficient placements, not a fixed pie being bid up. Macro figures cited verbally with no chart or source shown, and Heath voices skepticism about the supply-growth part.
Sources: Ben Heath, Meta's CMO on AI Ads and Rising Meta Ad Costs, 2026-07-20
Last touched: 2026-08-18

### AU-024 · Rising CPMs are acceptable, and expected, when ranking improvements raise ROAS; judge accounts on ROAS and cost per conversion, not CPM
Tier: T3 · Status: contested
Schultz's argument: better ad ranking (right ad, right person, right time) plus AI-personalized creative extracts more value from existing inventory, which drives ROAS up, which is "the only reason our CPMs go up." Heath's operator translation: a higher CPM with a higher ROAS beats a lower CPM; CPM alone is mostly noise for decision-making. Directionally logical but no account evidence shown, and Meta has an obvious interest in this narrative.

A buy-side source independent of Meta was added 2026-08-19, which is why the tier moved from T4 to T3. Faris, from 100+ managed Meta accounts, argues CPM is an output of an auction that prices access to the customers most likely to convert for your objective, so reaching older, wealthier women costs more and that cost is the pricing working correctly: "CPM looks like this thing that Meta gives you that's a problem, but in fact, it's a reflection of Meta probably reaching the right customer next. And if you're still not performing well enough at a high CPM, the problem's not the CPM, the problem is your performance." He gives a self-critical example: he blamed high CPMs on a new ad account launch, the CPMs stayed high for the whole run, and he now attributes it to not selling the product well enough. Operating consequence: stop fighting CPM, fix the offer and the creative.

Marked contested 2026-08-19 because AU-003 reads the same number in the opposite direction. Charley T's rule there is that a rising prospecting CPM means the creative stopped earning cold attention, which makes CPM a live creative-quality readout. Faris and Schultz say a rising CPM usually means the auction moved onto more valuable and more expensive people, which makes CPM close to uninformative on its own. Both camps end at the same instruction, fix creative and offer rather than chase CPM, and they disagree on what the number tells you, which matters because one side would kill a high-CPM prospecting ad and the other would leave it running. Resolution: hold creative constant and segment CPM by delivered audience value, or hold audience constant and rotate creative, and see which variable moves the CPM. Neither side ran that test.
Sources: Ben Heath, Meta's CMO on AI Ads and Rising Meta Ad Costs, 2026-07-20; Andrew Faris, I've Managed Over 100 Meta Ads Accounts. Here's Why Yours Is Broken., 2026-05-27
Last touched: 2026-08-19

### AU-031 · Brand equity inverts diminishing returns in the auction: a $300M/yr fashion account beat an $8M/yr account in the same category on CPM, CTR, CPC and ROAS at roughly 20x the spend
Tier: T3 · Status: active
He opens both account types routinely and reports that every core metric is better in the larger account, which contradicts the expectation that scale degrades efficiency: "And the crazy thing is that the ad account over here has better metrics on everything." Mechanism offered: market saturation and brand associations built entirely outside the ad account raise click-through, which lowers delivered CPMs. Stated boundary: performance marketing alone can brute-force a brand from roughly $1M to $20M, and past roughly $30-40k/day of spend further scale requires brand investment (influencer presence, events, showing up where the customer already is) that will not show profitable last-click ROI. This is the auction-side mechanism behind CR-100 (brand-led campaign-shoot assets only show good ROAS on pre-existing brand equity) and a counterweight to SC-040 (a practical spend ceiling from frequency saturating the TAM), since equity moves where that ceiling sits. ASSERTED from account audits, no numbers shown on screen.
Sources: Blue Sense Digital, Everything You Need to Know About Finance in eCommerce, 2026-05-04
Last touched: 2026-08-18

### AU-032 · Meta's reservation buying type buys a locked, often lower CPM by serving lower-quality prospects and lower-quality placements, so auction is the correct default for conversion campaigns
Tier: T3 · Status: active
Mechanism given: reservation can only guarantee a fixed cost per thousand impressions by degrading who it serves and where it serves, which lowers conversion probability, so the cheaper CPM buys worse impressions. Heath's words: "the only way that Meta can guarantee that is because they typically put your ad in front of lower quality prospects or use lower quality placements." Operator rule: take auction and accept CPM fluctuation, including the predictable Q4 and Black Friday demand spike, rather than buying a cheap guaranteed CPM. AU-023 treats CPM as a demand-supply price; this is the buying-type choice sitting underneath it, and it is the only claim in this topic covering the auction-versus-reservation fork. ASSERTED, no data shown.
Sources: Ben Heath, The BEST Instagram Ads Tutorial for Beginners in 2026, 2026-04-28
Last touched: 2026-08-18

### AU-034 · Q5, the week from Boxing Day to New Year, is the fastest CPM decline of the year and pairs near-Black-Friday buying intent with roughly half the CPM
Tier: T3 · Status: active
Charley T's seasonal calendar, stated across two videos. Impression supply spikes in that week because more people are on more devices for longer than in any other week of the year, producing the single fastest CPM drop of the calendar year: "CPMs begin to fall fast. It's one of the it is the fastest decline in CPMs for the whole year." Buying intent stays close to Black Friday levels while CPMs "could be half as much," which is the arbitrage. He puts the official run at seven days and says it stays workable for three to four weeks. January and February are the annual CPM floor in absolute terms, but Q5 is the better window because the floor months do not carry the intent: "what we're going to see in January and February is the lowest CPMs that we'll see all year long. But this is where you get buying intent that is very similar to Black Friday, but at CPMs that could be half as much." The end of the window is dated. The Q5 rush ends between 10 and 15 January with a hard drop around the 12th or 13th, every year, and comparing January performance to November and December is a category error. The cause he gives for the drop is consumer behaviour, almost nobody makes an unplanned purchase in mid-January after a full quarter of gift buying. This is a third seasonal window alongside the two named in AU-027 (the month before Black Friday, and late spring). See AU-035 for a same-speaker claim that pulls against the January CPM floor. Asserted from practitioner spend, no data shown.
Sources: Professor Charley T, Q5: the 2nd Black Friday: Meta Ads for Profit, 2025-12-20; Professor Charley T, How to Scale Profits with Meta Ads, 2026-01-24
Last touched: 2026-08-19

### AU-035 · Holding-company agencies return in the first weeks of January and their budget-insensitive spend lifts CPMs and takes the best impressions
Tier: T3 · Status: contested
The auction-side explanation for January cost rises. Charley T names Omnicom-scale buyers spending a million dollars a day, says teams like his did not work the first week of January, and that when they come back they buy the most attractive impressions with no revenue target attached: "there are now businesses willing to spend more in a day than you will a year with no revenue goals at all, spiking your CPMs and taking the impressions of the people who are most likely to be interested in what you have to say." He says he personally ran a million a day. The claimed cost is twofold, a higher CPM and reduced access to your best prospects, which would also degrade quality at constant CPM. Marked contested because the same speaker states in AU-034 that January and February carry the lowest CPMs of the year. Both can hold if the January rise is measured against the late-December Q5 trough while the month still sits far below Q4 in absolute terms, but he never reconciles them, so the expected direction of January CPM on a given account is unresolved. Resolution: pull weekly CPM for December through February on any account with two years of history and check whether weeks 1 to 3 of January rise off the late-December floor and by how much. Practitioner testimony, no CPM data shown.
Sources: Professor Charley T, How to Scale Profits with Meta Ads, 2026-01-24
Last touched: 2026-08-19

### AU-037 · On auto bids, day-level performance tracks the number of daily active users in market, so a bad day can be a supply effect rather than an account effect
Tier: T4 · Status: active
Faris notes daily active user counts on Meta change day to day, and on auto bids that flows straight through to both price and quality: "if you're running auto bids, there's actually changing numbers of daily active users on Meta and with changing numbers of daily active users means changing amounts of changing performance." Fewer daily actives in market means you pay more for worse customers. More daily actives, or higher buying intent that day, means you pay less and perform better. He offers this as a mechanism distinct from plain statistical noise, so it survives the usual "small sample" objection. Two consequences: do not diagnose a single bad day on an auto-bid ad set as an account problem, and note that a manual bid neutralises the price half of this effect by refusing to clear above your number, which is one more argument for the manual-bid default in AU-046. Asserted, no data shown.
Sources: Andrew Faris, I've Managed Over 100 Meta Ads Accounts. Here's Why Yours Is Broken., 2026-05-27
Last touched: 2026-08-19

### AU-038 · Pixel-event retargeting pays an auction premium because cart abandoners are contested by every competitor at once; broad retargeting reaches the same people outside that pocket
Tier: T4 · Status: active
Charley T's auction argument: add-to-cart and checkout abandoners are the most contested pool on the platform. "This keeps CPMs lower because we aren't competing in high bid auctions for checkout abandoners. Remember, if somebody's abandoning cart on your site, they're probably abandoning cart on a couple of your competitors' sites, too." Every advertiser bids for the same person, that person gets hit by all of them, and the bid pressure shows up as a CPM premium. Broad retargeting reaches the same interested population without entering the high-bid pocket. He adds a second reason the pool is poor value: most cart abandoners already decided against buying, so the audience is largely spent. This is the auction-price half of the broad-versus-event retargeting argument; the arithmetic half, that concentrating budget on 100 abandoners buys 90 people who will never convert, is banked in the Attribution topic. Reasoning only, no auction or CPM data shown.
Sources: Professor Charley T, How to CRUSH Facebook Ads with a Small Budget in 2026 (Full Course Post-Andromeda), 2026-04-09
Last touched: 2026-08-19

