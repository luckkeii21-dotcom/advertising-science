---
title: "TikTok Delivery"
type: codex-topic
claim_prefix: TT
created: 2026-08-18
tags: [advertising-science, codex]
---

# TikTok Delivery

TikTok ads auction and delivery system, plus TikTok Shop commerce ranking and GMV Max.

Part of the [[00-Codex|Advertising Science Codex]]. Claims follow the tier system (T1 docs, T2 shown test, T3 practitioner, T4 theory).

## Claims

## Auction and Bidding

### TT-001 · TikTok's auction ranks ads on two dimensions: bid price and the relevance the ad might have to people.
Tier: T1 · Status: active
From TikTok's Available bidding methods doc: "TikTok's auction ranks ads based on bid price and the relevance an ad might have to people." Four bidding methods exist: CPM, oCPM (default for conversions and app installs, pays per 1,000 impressions selected toward people likely to act), CPV (charged at 6-second view or interaction within first 6 seconds), and CPC.
Sources: TikTok Ads Manager Help, Available bidding methods (https://ads.tiktok.com/help/article/bidding-methods?lang=en), last updated August 2025
Last touched: 2026-08-18

## Learning Phase

### TT-002 · TikTok's learning phase volatility typically starts to decline after about 25 campaign results or 7 days from entering learning.
Tier: T1 · Status: active
TikTok defines the learning phase as the period when its ad system identifies the best users for a campaign target, with fluctuating performance while it explores. Current guidance (June 2026 revision) says volatility declines "after about 25 campaign results or 7 days." To complete learning, TikTok warns against pausing campaigns or ad groups, edits that retrigger learning-phase status, and unreasonable budget settings or creative volumes.
Sources: TikTok Ads Manager Help, Learning Phase (https://ads.tiktok.com/help/article/learning-phase?lang=en), last updated June 2026
Last touched: 2026-08-18

## Account Structure and Testing

### TT-003 · TikTok's official structure recommendation is 3-5 active ad groups per ad account and 3-5 creatives/ad versions per ad group, with big differences between creatives when testing.
Tier: T1 · Status: active
Auction best practices: create ads from one ad account (conversion data is not shared between accounts), recommend 3-5 active ad groups per account and 3-5 ad versions per ad group, start with a broad audience, and share Pixel + API signals simultaneously. Creative best practices repeat 3-5 different creatives per ad group and 3-5 diversified ad groups per campaign, adding "it is always better to use creatives with big differences, especially when testing," which helps during the ad group's exploration stage.
Sources: TikTok Ads Manager Help, Best practices for Auction Ads / Creative best practices for performance ads (https://ads.tiktok.com/help/article/auction-ads-best-practices?lang=en), last updated March 2025
Last touched: 2026-08-18

## Creative Refresh and Fatigue

### TT-004 · TikTok's official creative-refresh trigger is a consistently declining delivery trend or low daily new users, and new creatives should be added to the EXISTING ad group rather than a new one.
Tier: T1 · Status: active
TikTok recommends checking ad performance regularly and refreshing ad group creatives "when delivery results exhibit a consistently declining trend, or when daily new users are low." When refreshing, add new creatives to the existing ad group instead of creating a new ad group "to extend its lifetime." TikTok also suggests maintaining a standing library of creative assets and offers Smart Creative for automated fatigue management. Note: the current doc gives a trigger condition, not a fixed every-N-days cadence. Practitioner counterpoint on fatigue speed sits in TT-017.
Sources: TikTok Ads Manager Help, Creative best practices for performance ads (https://ads.tiktok.com/help/article/creative-best-practices?lang=en), last updated June 2025
Last touched: 2026-08-18

## Creative Quality Signals

### TT-005 · TikTok's ad quality/engagement signals for performance creative: hook within the first 6 seconds, content proposition in the first 3 seconds, native UGC-style vertical 9:16 video, and 5-10 words per second of on-screen text.
Tier: T1 · Status: active
TikTok's creative best practices say ads perform best when "made for TikTok": vertical 9:16, at least 720p, sound on, within the UI safe zone, featuring people, and in a DIY, not overly polished style that blends with user-generated content. Structure guidance: prioritize the hook in the first 6 seconds to boost engagement and watch time, introduce the content proposition in the first 3 seconds for recall, display 5-10 words per second when using text overlays, and end with a strong CTA.
Sources: TikTok Ads Manager Help, Creative best practices for performance ads (https://ads.tiktok.com/help/article/creative-best-practices?lang=en), last updated June 2025
Last touched: 2026-08-18

### TT-006 · A TikTok meta-analysis, reported second-hand, is said to show 30-40% better performance for ads carrying trending audio.
Tier: T3 · Status: active
The figure comes from a practitioner citing a TikTok study with no link and no document. Treat it as a practitioner's report of a platform study, so T3, not T1 platform documentation. His stated mechanism is that trending audio makes a paid ad read as organic content in feed, which lines up with TT-005's native-content signals. Rights caveat he adds: only use audio the advertiser is licensed for, since a commercial ad on a trending track can draw a claim. ASSERTED. No study, no account data shown. Operator action: run trending audio as a cheap variant axis on TikTok creative and measure your own before/after rather than banking the 30-40%.
Sources: Blue Sense Digital, Why Most Fashion Brands Are Running Paid Media Wrong, 2026-05-25
Last touched: 2026-08-18

## TikTok Shop Ranking

### TT-007 · TikTok ranks shoppable videos on link clicks, add-to-carts and purchases rather than watch time, because TikTok takes 6% of every order placed through the video.
Tier: T3 · Status: active
A normal TikTok video is ranked on watch time and engagement, because TikTok monetizes attention. A video carrying the orange cart link is ranked on commerce events, because TikTok monetizes the order at a 6% take rate. That inverts the creative brief. A shoppable video that holds attention and produces no cart events does not get distributed, which is why a steep intro discount mechanically buys distribution as well as orders. Operator action: judge shoppable brand videos on conversion events, and do not assume organic TikTok best practice transfers to TikTok Shop content. ASSERTED by the agency operator, no dashboard or ranking documentation shown.
Sources: Andrew Faris, He Sold $700,000 Worth Of Pretzels On TikTok Shop In One Month. Here's How You Can Too., 2026-06-30
Last touched: 2026-08-18

## TikTok Shop Offer and Launch

### TT-008 · Nearly every TikTok Shop buyer is a first-time trier, so the winning offer is the lowest-barrier version of the product rather than the highest-AOV one.
Tier: T3 · Status: active
Pop Daddy's Amazon offer, three large bags of one flavor, got no traction on TikTok Shop. A nine-pack of smaller bags across all flavors did. The mechanism is trial risk: give a first-time buyer more ways to like you for the same money. Brands with no variety-pack option get the same effect from a steep intro discount, free shipping or bonuses. Second constraint is listing clarity. Multi-size, multi-SKU listings kill the impulse, clothing excepted, because a confusing listing stops the purchase. Adding a brand-new flavor as a free bonus to the variety pack produced a sales spike across his client base. ASSERTED with named client examples, no revenue numbers shown. Pairs with TT-009 on launch pricing and TT-010 on the price ceiling.
Sources: Andrew Faris, He Sold $700,000 Worth Of Pretzels On TikTok Shop In One Month. Here's How You Can Too., 2026-06-30
Last touched: 2026-08-18

### TT-009 · Launch TikTok Shop at break-even or a steep discount to bank the first 100-1,000 orders, then step price back toward baseline.
Tier: T3 · Status: active
The discount is a launch tactic with a defined exit. Two assets accrue from those first orders: listing-level reviews and a publicly visible sales count that affiliates read before deciding to promote (see TT-011). The low-quality buyers acquired inside the first 100-1,000 orders do not matter, because that is not the end state. He calls getting the snowball moving the hardest part of TikTok Shop and says everything after it is downhill. Hard constraint from later in the same interview: GMV Max ads will not run against the deep launch discount, so plan the price step-up before the ads phase (TT-015). ASSERTED, no P&L or order curve shown.
Sources: Andrew Faris, He Sold $700,000 Worth Of Pretzels On TikTok Shop In One Month. Here's How You Can Too., 2026-06-30
Last touched: 2026-08-18

### TT-010 · The TikTok Shop price ceiling lifted after 2023: $50-70 AOV clients perform well and $100-200+ brands exist.
Tier: T3 · Status: active
In 2023 buyers assumed anything on TikTok Shop shipped from China, which capped what they would spend. That perception eroded over two years. Consequence for TT-008: low barrier to entry still wins, and low barrier now means a strong first-purchase discount at a real price point rather than a forced move into cheap SKUs. Any pre-2025 TikTok Shop price guidance is stale. ASSERTED from his agency client mix, no AOV distribution shown.
Sources: Andrew Faris, He Sold $700,000 Worth Of Pretzels On TikTok Shop In One Month. Here's How You Can Too., 2026-06-30
Last touched: 2026-08-18

## TikTok Shop Affiliates

### TT-011 · Affiliates select brands on visible sales volume rather than commission rate: raising commission from 15% to 30-35% changed affiliate quality and quantity very little.
Tier: T3 · Status: active
15% is his default recommendation. His agency tested up to 35% with negligible effect on the quality or quantity of affiliates reaching out. The mechanism is information asymmetry removal: on TikTok Shop an affiliate can see the brand's GMV before committing, so commission-only work stops being a blind bet. A high-sales week or month spikes affiliate inbound on its own. Corollary that inverts the standard lever: money spent buying affiliates is better spent buying sales velocity, which then buys affiliates for free. Tested across his book, no side-by-side numbers shown, so ASSERTED.
Sources: Andrew Faris, He Sold $700,000 Worth Of Pretzels On TikTok Shop In One Month. Here's How You Can Too., 2026-06-30
Last touched: 2026-08-18

### TT-012 · Affiliate outreach throughput at launch: 2,000+ messages per week per brand yield 100-400 sample requests, of which 10-40 are worth sending product to.
Tier: T3 · Status: active
Response rate is 5-20% and rises materially once the listing has sales velocity behind it. Sourcing is three-way: lists from the TikTok rep, filtered pulls from Cruva (example filter: food and beverage creators, 20k+ followers, 1k+ GMV in the last 30 days), and third-party pulls of the top affiliates on competitor and adjacent brands. The 2,000 are unvetted. Vetting happens only on responders, and the criterion is content quality rather than the creator's GMV, because a creator with sales may have had one lucky video. He acknowledges a viable opposite strategy, sending samples to every responder on venture math, and runs the efficient version instead. ASSERTED as ranges from agency practice, no CRM export shown.
Sources: Andrew Faris, He Sold $700,000 Worth Of Pretzels On TikTok Shop In One Month. Here's How You Can Too., 2026-06-30
Last touched: 2026-08-18

## TikTok Shop Content Supply

### TT-013 · Brand-owned shoppable video, built as a direct-response ad, creates the initial break for about 70% of his TikTok Shop clients.
Tier: T3 · Status: active
He frames this as his main difference from agencies that lead with affiliates. Early affiliate content is low-volume, low-quality and unsteerable. Brand content can be aimed at the exact listing being pushed. Run affiliate outreach from day one anyway and do not depend on it for the break. Build spec: strong hook, full body, and a CTA specific to the TikTok Shop listing and its discount, because the orange cart link is the conversion path and that CTA is the part that differs from a Meta ad. Production is deliberately low-fi iPhone footage with no heavy editing, at roughly 4-8 videos per month from the agency, layered on top of the brand's own content operation. Two recurring formats: founder story and order packing. Pop Daddy's break was an order-packing video shot in the facility. Fishwife's was a founder-story video now past 6 million views. He states 100 high-quality videos beat 10 and warns against trading quality for volume. ASSERTED, the 70% is his own estimate across his book, no client list or view data shown.
Sources: Andrew Faris, He Sold $700,000 Worth Of Pretzels On TikTok Shop In One Month. Here's How You Can Too., 2026-06-30
Last touched: 2026-08-18

### TT-014 · TikTok Shop's feedback loop runs far slower than Meta's: a posted video can start performing one to two months after it goes up.
Tier: T3 · Status: active
On Meta a content-and-offer combination reads within days. On TikTok Shop the algorithm "takes a long time to warm up," so a flat video is not dead, and a kill decision made on Meta timescales destroys assets that were about to work. Operator action: stop pruning the shoppable video library aggressively, and stop reading early GMV Max allocation as a verdict on a video. This also explains the 100-video threshold in TT-015. The library is a slow-maturing asset pool rather than a test queue. Note the tension with TT-017, where the same platform's paid creative is reported to fatigue very fast. Organic shoppable video and paid TikTok creative are being described on different clocks by different operators, and neither showed data. ASSERTED, no cohort curve shown.
Sources: Andrew Faris, He Sold $700,000 Worth Of Pretzels On TikTok Shop In One Month. Here's How You Can Too., 2026-06-30
Last touched: 2026-08-18

## GMV Max Ads

### TT-015 · GMV Max barely spends until the shop has 100+ shoppable videos; launch at $100-200/day with a low ROI target once past that threshold.
Tier: T3 · Status: active
A hard prerequisite that reorders the whole launch sequence: content and affiliate volume first, ads last. GMV Max automatically ingests every video carrying a shopping link for that product and then allocates spend across them, so a thin video pool leaves it nothing to allocate. No manual creative upload is required and campaign-level customization is close to zero by design, because TikTok wants the surface trivially easy so more people spend. Scale by raising budget or the ROI target once the initial read looks acceptable. Sequencing constraint from TT-009: GMV Max will not run against the deep launch discount, so step price up first. ASSERTED as a recommendation, no spend curve or threshold test shown.
Sources: Andrew Faris, He Sold $700,000 Worth Of Pretzels On TikTok Shop In One Month. Here's How You Can Too., 2026-06-30
Last touched: 2026-08-18

### TT-016 · Split hero SKUs into their own GMV Max campaigns, because one combined campaign lets the algorithm concentrate spend on a single hero SKU and starve the rest.
Tier: T3 · Status: active
Most TikTok Shop brands have 2-3 hero SKUs driving about 90% of sales. Inside one campaign, GMV Max picks whichever SKU it predicts will maximize GMV and neglects the others. Recommended shape is one campaign per hero SKU plus one catch-all campaign for the remaining SKUs. This is a deliberate exception to the consolidation logic in SC-014 and SC-015: the data-fragmentation cost is accepted to force budget onto SKUs the algorithm would otherwise abandon. Same structural logic as SC-028, where a campaign exists only to force spend onto specific assets. ASSERTED, no split test shown.
Sources: Andrew Faris, He Sold $700,000 Worth Of Pretzels On TikTok Shop In One Month. Here's How You Can Too., 2026-06-30
Last touched: 2026-08-18

## Incrementality and Channel Fit

### TT-017 · TikTok incrementality splits into a minority of accounts where lift proves out and a majority where a holdout shows nothing. Two credible operators name DIFFERENT deciders for the same split.
Tier: T3 · Status: contested
Both sides observe the same pattern. Neither ran the comparison that would separate the two explanations, and neither showed the data.

**Decider A: category, gated on creative supply.** Nine tests across one agency's book. 4 of 5 fashion lift experiments came back strongly positive. 4 of 4 inverse holdouts outside fashion showed none, and those four clients were pulled off the platform on the result. He names creative supply as the real decider rather than the vertical alone: an account needs a genuine native organic TikTok operation producing volume, because TikTok creative fatigues very fast, and without that pipeline he says the channel will not work. Test counts and directions are stated. No lift percentages, no holdout dashboards, no confidence intervals, so ASSERTED. The fast-fatigue element sits against TT-004's platform-stated refresh trigger and against TT-014's slow organic warm-up on TikTok Shop.

**Decider B: market size and brand scale.** A second Blue Sense operator reports the same split and never mentions organic TikTok operation, native content, or an organic account once across two full transcripts. Not once. His decider is geography and revenue. The US is where TikTok lift has been proven, because a brand selling across enough states can cut TikTok out of selected states and read the dip against the rest of the country. He has run that cut repeatedly on US accounts spending $20,000 to $40,000 a month and it came back null every time (TT-018), and he has one third-party geo-lift on a very large US brand that came back clean (TT-019). He has seen no proven TikTok geo-incrementality test in Australia at all. His floor is a revenue floor rather than a category floor: $5-6M in revenue and already profitable (TT-020). ASSERTED. No lift figures shown on this side either.

**How to hold it.** Category and market size are confounded in both books, because a fashion brand at 8 figures in the US differs from a non-fashion brand at 7 figures in Australia on every dimension at once. Both operators sit under the same agency banner, and the market-size decider is stated in the 2025 episodes while the category-and-creative-supply decider is stated in the 2025-12 and 2026-05 episodes. That may be one position evolving or two operators disagreeing. The transcripts do not say which. Operator action: quote neither decider as settled. Both sides agree on the instrument, a geo holdout or an inverse holdout, so run the test rather than predicting the answer from vertical or from headcount.

Read alongside the cross-channel attribution asymmetry filed in [[Attribution & Incrementality]], where raising TikTok spend on large retail accounts lifted Meta and Google ROAS while TikTok's own stayed flat. That points the same way as everything above: judge TikTok on lift tests rather than on in-platform ROAS.

Corroboration for decider A from December 2025, scoped explicitly to large retail fashion at meaningful spend: "We've run a lot of incrementality studies and it's actually very very good. It it drives a very strong incremental ROI um at a lot of spend. The issue is the attributed rorowes in platform on those accounts is terrible." The operating trap he names is a large retailer reading only the attributed number and killing the channel. He also said in that interview that TikTok is a bad platform for most advertisers and that most businesses should not be on it, which matches the non-fashion holdouts above and matches decider B's revenue floor.

The magnitude of that attribution gap is UNVERIFIED and must not be quoted. The auto-transcript of the number is mangled: "It's like 7 maybe even a one uh seven click." Probable reading is an attributed ROAS of 0.7, possibly 1.0, measured on a 7-day click window, since he calls the number terrible in the same breath and a 7.0 ROAS would not be terrible. That is inference from a garbled line, not a heard number. Use the direction only: platform-attributed ROAS on those accounts sat far below the incremental result. Resolution would need the raw audio at that timestamp or the study itself.
Sources: Blue Sense Digital, Why Most Fashion Brands Are Running Paid Media Wrong, 2026-05-25; Blue Sense Digital, Two Years Later: What Still Works (And What Doesn't) ft. Michael Nadalin, 2025-12-27; Blue Sense Digital, Should You Should Run TikTok Ads In 2025?, 2025-08-18; Blue Sense Digital, Be Careful: TikTok Ads Nearly Bankrupted This Business, 2025-03-24
Last touched: 2026-08-19

### TT-018 · Repeated TikTok holdouts on US accounts spending $20,000-$40,000 a month showed no sales dip, every time, including an 8-figure account that cut roughly $40,000 a month with no revenue drop.
Tier: T3 · Status: active
Two forms of the same test across one agency's US book. Form one is state-level: pick core states, cut those states out of the TikTok spend, and measure sales in them against the rest of the US. His result: "the answer was always no sales never did it was always fine." Form two is whole-account: one 8-figure client had their TikTok rep visit the office, it set off alarm bells, the client cut about $40,000 a month of TikTok spend, and revenue did not drop. He read that as zero incrementality. The accounts carrying these tests were spending $20,000 to $40,000 a month on TikTok, so these are not thin budgets. No per-state numbers, no windows, no dashboards, and the $40,000 is recalled in conversation, so ASSERTED. The one account that went the other way is TT-019, and the operator holds both results at once rather than picking one. Operator action: the state-level cut is the cheapest TikTok incrementality instrument available to a multi-state US advertiser and it needs no third-party platform. The test-design constraint on running it, never in a high-seasonality month, is filed in [[Attribution & Incrementality]].
Sources: Blue Sense Digital, Should You Should Run TikTok Ads In 2025?, 2025-08-18
Last touched: 2026-08-19

### TT-019 · One TikTok geo-lift experiment on a very large US brand, run through a third-party incrementality platform, came back successful with statistical relevancy and blended CAC inside the brand's constraint.
Tier: T3 · Status: active
The counterweight the same operator volunteers against his own null results in TT-018. He names a genuine third-party incrementality platform, statistical relevancy, and blended CAC within what the brand needed. He gives no CAC figure, no lift figure, no platform name, no dates, and shows nothing, so ASSERTED. What it establishes is only that TikTok lift is provable somewhere, which is exactly why the competing deciders in TT-017 matter. Operator action: the brand was "very big" and US-based, so read a positive TikTok lift result as evidence about accounts of that shape rather than about TikTok as a channel.
Sources: Blue Sense Digital, Should You Should Run TikTok Ads In 2025?, 2025-08-18
Last touched: 2026-08-19

### TT-020 · The stated entry threshold for testing TikTok is $5-6M in revenue and already profitable, revised down on camera from an earlier $10-30M position.
Tier: T3 · Status: active
His words: "If you're doing at least 5 to 6 million in revenue minimum, then okay, you can try. Also, you want to be profitable at the same time, don't think that Tik Tok is suddenly going to fix your profitability issues." The reasoning is that TikTok is a volume add, so it cannot repair unit economics that are already broken. Neither the old $10-30M number nor the new $5-6M number has data behind it, and he revises it live on camera, which is itself a signal the threshold is judgment. ASSERTED.
The same agency's case account gives the floor a concrete shape from below. A $2M/year brand had 33% of media budget, $20,000 of $60,000, in TikTok on a top-of-funnel thesis. The 33% and the budget split are shown on screen. The operator's position is that a brand that size has no direct-response case for that allocation, because the top-of-funnel argument only holds for a brand big enough to run a controlled incrementality test in the first place. The threshold behind that judgment is asserted, not tested.
Related ceiling from the same episode, filed in [[Marketing Math & Unit Economics]]: most brands can reach $200,000-$250,000 a month on Meta in Australia and New Zealand alone, so a brand below that ceiling should push Meta budget before opening a second platform. That is the practical form of this claim for most of our accounts.
Sources: Blue Sense Digital, Should You Should Run TikTok Ads In 2025?, 2025-08-18; Blue Sense Digital, Be Careful: TikTok Ads Nearly Bankrupted This Business, 2025-03-24
Last touched: 2026-08-19

## Traffic Quality and Blended Funnel Effects

The strongest TikTok evidence on the roster. One ~$2M/year Shopify brand, walked through live on screen across the account, the Shopify reports and the cohort charts. Claims TT-021 to TT-023 are the same account.

### TT-021 · A ~$2M/year Shopify brand scaled TikTok from $600 to $10,500 a month as purely additive budget: total media went $40,000 to $60,000, up 50%, and net sales rose 6%.
Tier: T2 · Status: active
Shopify period-over-period report shown on screen. Media across Meta and Google was $40,000 before. It was $60,000 after, a 50% increase, with the extra $20,000 going to TikTok. Net sales rose 6%. The operator's read on that trade: "not very convincing." Orders rose substantially in the same comparison while average order value fell, so TikTok was buying low-AOV orders and an order-count-only read would have hidden it.
The top line hides the real damage, which is in TT-022 and TT-023. Ending state, computed on screen from stated figures: blended CAC inflated to $118 in March against a run rate of $210, first-purchase gross profit was $60 to $70, LTGP:CAC came out at 0.48, and the operator put the business 60 to 90 days from bankruptcy if it held course. The ratio claim itself is filed in [[Marketing Math & Unit Economics]]. The apparent LTGP:CAC of 7 to 8 that convinced the previous agency to ramp is filed there too, and it was an artefact of counting add-to-carts as conversions (TT-026).
SHOWN. Spend figures, the 6%, the CAC figures and the ratio are all read off screen.
Sources: Blue Sense Digital, Be Careful: TikTok Ads Nearly Bankrupted This Business, 2025-03-24
Last touched: 2026-08-19

### TT-022 · A channel can add traffic and subtract profit at the same time, and blended site conversion rate falling is the tell: TikTok added 63% more sessions while cart additions fell in absolute terms and site conversion rate dropped 54%.
Tier: T2 · Status: active
This is the mechanism claim. All figures read off the Shopify behaviour reports on screen.
Sessions rose 63%, from about 18,000 to nearly 30,000, roughly 11,000 extra sessions, against 9,800 TikTok clicks, which ties the extra sessions to TikTok. Sessions with cart additions fell in ABSOLUTE terms despite sessions nearly doubling. Sessions that reached checkout fell further. Sessions that completed checkout fell from 969 to 721. Site conversion rate fell 54%.
The mechanism: TikTok delivered volume that was not in market, and because site conversion rate is blended across all sources, the new traffic dragged the denominator and the whole site read as broken. Every downstream metric the brand looked at was contaminated by a channel that occupied 33% of media budget.
Operator action: when a new channel turns on, watch blended site conversion rate and the ABSOLUTE count of cart additions, never the channel's own row. If cart additions fall in absolute terms while sessions rise, the channel is buying traffic that will not convert and no attribution model is needed to make the call. This is the shown instance behind the rule filed in [[Scaling Models]]: never raise spend on a channel while backend metrics fall.
SHOWN.
Sources: Blue Sense Digital, Be Careful: TikTok Ads Nearly Bankrupted This Business, 2025-03-24
Last touched: 2026-08-19

### TT-023 · Turning TikTok off produced no revenue drop, and site conversion rate went 1.5% to 8% overnight before settling near 6%.
Tier: T2 · Status: active
Shown on the Shopify conversion rate chart. The speaker flags the confound himself: a sale launched at the same moment, so the 8% spike is contaminated and the stable read is about 6%. Discount the spike and 1.5% to 6% is still the conversion rate recovering once the non-converting traffic stopped arriving. Revenue did not fall when the channel went off, which is the same null result the state-level holdouts in TT-018 reached by a different route.
Operator action: the off-switch read costs nothing, and on a single-market brand too small for a geo holdout it is the only incrementality instrument available. Give it a stable month with no promo calendar in it, because this account's own read was confounded by a sale on day one.
SHOWN, with the confound stated by the source rather than by us.
Sources: Blue Sense Digital, Be Careful: TikTok Ads Nearly Bankrupted This Business, 2025-03-24
Last touched: 2026-08-19

### TT-024 · TikTok traffic degrades on-site funnel quality in a specific pattern: pop-up form submission rate holds flat or improves while conversion off the back of those submissions collapses.
Tier: T3 · Status: active
Repeated observation across brands that turned TikTok on. Submission rate is not the tell, because a discount pop-up converts a curious scroller as readily as a buyer. What breaks is what happens after: the submitted emails do not buy, and they sit dormant on the list as discount-claiming non-buyers. Two costs follow. List quality falls, and any funnel metric measured at the submission stops meaning anything. No rates, no account and no dashboards shown, so ASSERTED. This is the leading-indicator version of the shown collapse in TT-022. The generic diagnostic behind it, splitting average session duration, add-to-cart rate and pop-up fill rate by traffic source, is filed in [[Attribution & Incrementality]].
Sources: Blue Sense Digital, Should You Should Run TikTok Ads In 2025?, 2025-08-18
Last touched: 2026-08-19

### TT-025 · Cheap TikTok CPMs carry no signal about channel value: in the case account CPMs were strong while CPCs sat about level with Facebook.
Tier: T3 · Status: active
His words: "cpcs are okay they're not great they're about the same as Facebook cpms are great because it's Tik Tok." The metric columns are on screen but no CPC or CPM value is stated, so the comparison is his assertion. T3, not T2, on that basis. Mechanism: a low CPM reflects lower advertiser demand for TikTok inventory, and the advantage is arbitraged away at the click because click-through rate is lower too. Operator action: a cheap CPM is the most common reason a brand opens TikTok and it predicts nothing about CAC. Judge on cost per purchase or on lift.
Sources: Blue Sense Digital, Be Careful: TikTok Ads Nearly Bankrupted This Business, 2025-03-24
Last touched: 2026-08-19

## Reading a TikTok Account

### TT-026 · Optimizing TikTok campaigns for add-to-cart or view-content makes the account's own conversion and CPA columns unreadable: one campaign showed 449 clicks and 206 conversions.
Tier: T2 · Status: active
Campaign row shown on screen with both numbers. Roughly half the people who clicked fired the view-content pixel on page load, and the campaign counted each of those page loads as a conversion, so cost per conversion at campaign level was a cost per page view. The delivery consequence matters more than the reporting one: TikTok optimizes toward whatever event is selected, so a view-content campaign is being told to buy page loads and it buys them. That is how the previous agency on this account arrived at an apparent LTGP:CAC of 7 to 8 and ramped spend into a business that was losing money on every order.
Operator action: on any TikTok test that has to answer a business question, set the optimization event to purchase, and read the account through TT-027's attribution report rather than through the campaign conversion column. The account-wide version of the same disparity, platform-reported conversions against backend purchases, belongs to [[Attribution & Incrementality]] and is filed there.
SHOWN.
Sources: Blue Sense Digital, Be Careful: TikTok Ads Nearly Bankrupted This Business, 2025-03-24
Last touched: 2026-08-19

### TT-027 · TikTok exposes an Attribution Analytics report under Tools that breaks attributed events out by click window from 1 to 90 days and separately by view window.
Tier: T2 · Status: active
The product screen is opened and walked through on camera. The operator calls it more robust than the equivalent on other platforms and says he wishes Meta and Google had it. It lets an operator rebuild a click-only read that the campaign view will not give them, which is the prerequisite for any honest TikTok read.
Tiered T2 rather than T1 deliberately. The UI is shown on camera, no TikTok documentation is quoted or shown, and our rule is that T1 requires the document itself. A product surface seen on screen is a shown observation, not a specification.
Operator action: on any TikTok account, pull the click-only column at 7 days before believing the campaign view. The view-through counts this report exposed on the case account are filed in [[Attribution & Incrementality]].
Sources: Blue Sense Digital, Be Careful: TikTok Ads Nearly Bankrupted This Business, 2025-03-24
Last touched: 2026-08-19

### TT-028 · TikTok reps actively push advertisers off click-only attribution and onto 7-day click plus 1-day view, telling them performance will be better on that model.
Tier: T3 · Status: active
Reported rep behaviour from real account relationships across an agency book. The rep's stated claim, quoted: "No, no, no. You'll always get better performance in the business when you run 7 click one day views." The operator says outright that he has no data on whether that is true. Separately, one 8-figure client cut $40,000 a month of TikTok spend after a rep office visit set off alarm bells (TT-018), so rep contact is not a neutral event on an account.
The incentive explanation offered alongside it is T4 reasoning with no compensation document behind it: reps are salespeople, their KPIs are presumed tied to how much their book of clients spends, so a ROAS-based upsell from a rep is not an independent read on the channel.
Operator action: treat a rep's attribution-setting recommendation as a sales action. The delivery-side reason to resist it is already banked on the Meta side, where the 7-day-click plus 1-day-view setting biases DELIVERY toward view-through rather than only the report. ASSERTED on both halves, nothing shown.
Sources: Blue Sense Digital, Should You Should Run TikTok Ads In 2025?, 2025-08-18
Last touched: 2026-08-19

## Smart Plus (Automated Campaigns)

### TT-029 · TikTok shipped a full Smart Plus API surface in Business API SDK v0.1.8: 18 endpoints covering smart_plus campaign, adgroup and ad create/update/get/status, plus material reporting, review info and appeal.
Tier: T1 · Status: active
Read directly from TikTok's official SDK changelog on 2026-08-19. The v0.1.8 entry adds, all under `/open_api/v1.3/smart_plus/`:
- `campaign/` create, update, get, status/update
- `adgroup/` create, update, get, status/update
- `ad/` create, update, get, status/update, material_status/update, review_info, appeal
- `material_report/` overview, breakdown
- `material/review_info`

Smart Plus is TikTok's automated campaign type, the structural equivalent of Meta's Advantage+. This claim covers the EXISTENCE of the product and the size of its API surface, and nothing more. The changelog documents endpoint names. It documents no performance, no allocation logic and no delivery behaviour, so infer none. What the surface itself states: material-level reporting exists with both an overview and a breakdown, and a dedicated appeal endpoint sits alongside ad-level and material-level review info.
The changelog header also states that "In Q4, 2025, TikTok Business API SDK plans to support more gmv max and ads management endpoints," which puts GMV Max (TT-015, TT-016) and Smart Plus on the same automation roadmap.
The codex held zero claims mentioning Smart Plus before today. Every Meta-side Advantage+ law we hold is a candidate hypothesis for this surface and none of them are evidence for it. Testing Smart Plus against a manual TikTok campaign is an open T2 opportunity on any account we run.
Sources: TikTok Business API SDK Changelog.md v0.1.8 (https://raw.githubusercontent.com/tiktok/tiktok-business-api-sdk/main/Changelog.md), read 2026-08-19
Last touched: 2026-08-19
