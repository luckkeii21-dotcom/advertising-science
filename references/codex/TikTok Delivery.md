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

### TT-017 · TikTok incrementality is category-dependent: 4 of 5 fashion lift experiments came back strongly positive, 4 of 4 inverse holdouts outside fashion showed none.
Tier: T3 · Status: active
Nine tests across one agency's book. The four non-fashion clients were pulled off the platform on the result. He names creative supply as the real decider rather than the vertical alone: an account needs a genuine native organic TikTok operation producing volume, because TikTok creative fatigues very fast, and without that pipeline he says the channel will not work. Test counts and directions are stated. No lift percentages, no holdout dashboards, no confidence intervals, so ASSERTED. Read alongside the cross-channel attribution asymmetry filed in [[Attribution & Incrementality]], where raising TikTok spend on large retail accounts lifted Meta and Google ROAS while TikTok's own stayed flat. Both point the same way: judge TikTok on lift tests rather than on in-platform ROAS. The fast-fatigue element sits against TT-004's platform-stated refresh trigger and against TT-014's slow organic warm-up on TikTok Shop.
Sources: Blue Sense Digital, Why Most Fashion Brands Are Running Paid Media Wrong, 2026-05-25
Last touched: 2026-08-18
