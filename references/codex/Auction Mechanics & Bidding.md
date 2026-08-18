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
Sources: Blue Sense Digital, How The Meta Ads Algorithm Works in 2026, 2026-07-28; Blue Sense Digital, eCommerce CRO Masterclass 2026: The Full System, 2026-08-10; Professor Charley T, The NEW BEST Meta Ads Andromeda Course to Scale in 2026, 2026-01-24
Last touched: 2026-08-18

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
Sources: Andrew Faris, Do Cost Caps Work? Taylor Holiday Brings $200M Of Data, 2026-08-06
Last touched: 2026-08-18

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
Sources: Professor Charley T, Record Profits: the Meta Ads Andromeda Playbook, 2026-01-03; Professor Charley T, Meta advertisers... We've got a big problem, 2026-01-17
Last touched: 2026-08-18

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
Sources: Andrew Faris, From A 65% Decline To All-Time Revenue and Profit Highs With Richie Mashiko From She's Birdie, 2026-04-27
Last touched: 2026-08-18

### AU-030 · At high spend, a second ad account on the same pixel and page running different bid logic enters auctions the primary account is not bidding on
Tier: T3 · Status: active
Configuration described: primary account on maximize conversions, secondary account on maximize conversion value or on cost caps or bid caps, with the same creative, the same pixel and the same page. The mechanism claimed is that different bid strategies enter the auction with different bids, so the second account reaches volume the first cannot. He states plainly that the self-competition objection, that cross-bidding raises your own CPMs, is unproven either way, and argues that same-page and same-pixel should limit it. The de-risking half of the argument is unconditional: an account ban or a billing failure otherwise zeroes new-customer acquisition for a week. He warns the tactical detail changes every six months. Only relevant above the bid-strategy attention threshold recorded in AU-012. ASSERTED, no data shown.
Sources: Blue Sense Digital, How To Structure A Meta Ads Account At Every Spend Tier In 2026, 2026-06-01
Last touched: 2026-08-18

## Value rules

### AU-018 · Value rules adjust bids up or down by age, gender, device platform, mobile OS, location, audiences, conversion location, or placement, without hard restrictions
Tier: T3 · Status: active
Value rules (introduced 2025) tell the auction to bid more or less for specific criteria, for example bid more for ages 35-54 or less for certain countries. As of Aug 2026 the supported criteria are age, gender, device platform, mobile operating system, location, audiences, conversion location, and placement. They shift delivery probabilistically instead of excluding anyone.
Sources: Jon Loomer, Ask These Questions Before Using Value Rules, 2026-08-12
Last touched: 2026-08-18

### AU-019 · Never hard-exclude an underperforming demographic segment; apply a bid-decrease value rule instead (10-20% for tuning, up to the 90% maximum for effective exclusion)
Tier: T3 · Status: active
Multiple independent sources converge on the same move. Piliero: removing e.g. 65+ or 18-24 from delivery loses money and scale potential; decrease the segment's bid 10-20% in a NEW ad set containing proven best ads so the rule's effect is isolated like an A/B test, and Meta then only buys that segment when it returns ~10% better than current. Shiver: a 90% bid decrease (the platform maximum) on age brackets outside the real buyer band (e.g. keeping 25-45, downweighting 45-54, 55-64, 65+) effectively excludes them while Advantage+ expansion stays intact, configured at ad set level under value rules > audience > age. Loomer: exclusions remove all chance of conversion from a segment and shrink the pool (raising CPM), while a bid-down rule keeps the segment eligible at reduced spend; he applies it to non-purchase optimization problems and LTV differences by demographic. Multiple independent sources; none showed isolated A/B data.
Sources: Sam Piliero, The Only Facebook Ads Video You Need in 2026, 2026-07-26; Dr. Matt Shiver, How to Run Facebook Ads for Coaches & Agency Owners (FREE COURSE), 2026-08-04; Dr. Matt Shiver, The 'Right Way' to Run Facebook Retargeting Ads in 2026, 2026-07-28; Jon Loomer, Ask These Questions Before Using Value Rules, 2026-08-12; Jon Loomer, You May Be Surprised Who Converts, 2026-07-22
Last touched: 2026-08-18

### AU-020 · When to apply value rules: only with a proven, data-backed delivery problem, or as always-on standard practice
Tier: T3 · Status: contested
Loomer's position: value rules intentionally increase costs by construction, so they are only justified when you have information Meta lacks (offline lead quality, LTV by segment) AND Meta is actually misallocating meaningful budget against that information; applying one without a demonstrated problem raises costs for nothing, and raising bids on groups Meta already prioritizes is pure cost inflation with no delivery gain. Shiver's position: he applies the 90% age bid-down on nearly every ad set as always-on standard practice, treating ICP age steering as a default rather than a diagnosed exception. Neither side showed test data isolating the cost effect.
Sources: Jon Loomer, Ask These Questions Before Using Value Rules, 2026-08-12; Dr. Matt Shiver, How to Run Facebook Ads for Coaches & Agency Owners (FREE COURSE), 2026-08-04
Last touched: 2026-08-18

### AU-021 · Value rules raise bids on first-party-known high-value segments (e.g. +60% bid for a segment worth 60% more) without restricting targeting
Tier: T3 · Status: active
Meta already sees who converts from tracked conversion actions, but not off-platform value data like repeat purchase rate or phone-call-to-client close rate by segment. Value rules feed that in: "these people are worth 60% more, increase my bid by 60%", by age, location, or device. Improves overall ROAS and lead quality at budgets where the customer data exists; $100k/month has the data. The 60% figure is illustrative, no before/after account data shown. Note the tension with AU-020: Loomer would require proof Meta is misallocating before paying more.

Restated 2026-08-18 with the anti-pattern named explicitly, which is the operationally important half. The big mistake Heath sees is building a value rule out of where the account's purchases or leads already come from: if Meta can already see that over-35s convert better, Meta is already delivering mostly to over-35s, so paying a premium for them buys nothing. Value rules are only for information the system is structurally blind to, and he gives two: conversion rate from lead to customer (offline, never reported back), and repeat purchase rate beyond the attribution window. He also states the required posture, that the multiplier must come from measured segment value rather than a guess, and the sophistication claim that advanced advertisers now leave ad-set targeting alone entirely and steer through value rules instead. Build path shown live: All tools, Advertising settings, Value rules, Create a rule set, select audience, select criteria (e.g. age 35+), set the bid increase, name and create; then apply it at ad set level in the Value rule section by choosing the rule set. Different rule sets can apply to different offers, campaigns, and ad sets. This lands Heath on Loomer's side of the AU-020 split for the bid-UP case, narrowing that contest: both now agree raising bids on what Meta already prioritizes is pure cost inflation. AU-020 stays contested because it also covers Shiver's always-on bid-DOWN practice, which neither addresses here.
Sources: Ben Heath, $100 vs $100,000 Facebook Ads Strategy, 2026-08-12; Ben Heath, Learn 97% of Meta Ads in Under 29 Minutes, 2026-08-18
Last touched: 2026-08-18

### AU-022 · A 90% bid-decrease value rule on Android devices reduces foreign leads in US-targeted campaigns
Tier: T3 · Status: active
Meta's location setting targets people who live in OR recently visited the country, so US campaigns leak to visitors. When lead quality complaints include foreign leads, Shiver adds a value rule decreasing bids 90% on Android devices, since foreign visitors skew Android and iOS skews to US residents with higher socioeconomic status. Flagged as an occasional fix, not a default.
Sources: Dr. Matt Shiver, How to Run Facebook Ads for Coaches & Agency Owners (FREE COURSE), 2026-08-04
Last touched: 2026-08-18

## CPM economics

### AU-023 · Meta CPMs are a demand-supply price; supply is still growing, and digital advertising has grown from 1% to roughly 1.3-1.4% of the global economy
Tier: T3 · Status: active
Meta CMO Alex Schultz frames CPM as a pure demand-supply function and rejects the idea that inventory is capped: TikTok created large new time-spent supply (mostly pulled from TV), and digital platforms grew total advertising from a long-stable 1% of the global economy to about 1.3-1.4%. Rising CPMs therefore reflect both more advertiser demand and more efficient placements, not a fixed pie being bid up. Macro figures cited verbally with no chart or source shown, and Heath voices skepticism about the supply-growth part.
Sources: Ben Heath, Meta's CMO on AI Ads and Rising Meta Ad Costs, 2026-07-20
Last touched: 2026-08-18

### AU-024 · Rising CPMs are acceptable, and expected, when ranking improvements raise ROAS; judge accounts on ROAS and cost per conversion, not CPM
Tier: T4 · Status: active
Schultz's argument: better ad ranking (right ad, right person, right time) plus AI-personalized creative extracts more value from existing inventory, which drives ROAS up, which is "the only reason our CPMs go up." Heath's operator translation: a higher CPM with a higher ROAS beats a lower CPM; CPM alone is mostly noise for decision-making. Directionally logical but no account evidence shown, and Meta has an obvious interest in this narrative.
Sources: Ben Heath, Meta's CMO on AI Ads and Rising Meta Ad Costs, 2026-07-20
Last touched: 2026-08-18

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

