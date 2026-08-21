---
title: "Google Auction & Smart Bidding"
type: codex-topic
claim_prefix: GA
created: 2026-08-18
tags: [advertising-science, codex]
---

# Google Auction & Smart Bidding

Ad Rank, Quality Score, and the real behavior of tCPA/tROAS smart bidding.

Part of the [[00-Codex|Advertising Science Codex]]. Claims follow the tier system (T1 docs, T2 shown test, T3 practitioner, T4 theory).

## Claims

## Smart Bidding Mechanics

### GA-001 · Smart Bidding is exactly four strategies (tCPA, tROAS, Maximize conversions, Maximize conversion value) that set a unique bid per auction using Google AI
Tier: T1 · Status: active
Google defines Smart Bidding as bid strategies that use Google AI to optimize for conversions or conversion value in each and every auction, a capability it calls auction-time bidding. The bid is set individually per auction rather than per keyword or per ad group.
Sources: Google Ads Help: About Smart Bidding, https://support.google.com/google-ads/answer/7065882
Last touched: 2026-08-18

### GA-002 · Smart Bidding's auction-time signals include device, physical location and location intent, day/time, remarketing list, browser, OS, interface language, and the actual query text beyond the matched keyword
Tier: T1 · Status: active
Google's published signal list spans: device type; physical location down to city and location intent; weekday and time of day in the user's timezone; remarketing list membership and site behavior; ad creative version and format; browser, operating system, and interface language; the actual search query (not just the keyword it matched) and whether it came from a search partner; web placement for Display; and product attributes, price competitiveness, and seasonality for Shopping. Many of these signals are not available to manual bidding at all.
Sources: Google Ads Help: About Smart Bidding, https://support.google.com/google-ads/answer/7065882
Last touched: 2026-08-18

### GA-003 · Target CPA holds the AVERAGE cost per conversion at target; individual conversions are allowed to cost more or less
Tier: T1 · Status: active
Google: some conversions may cost more than your target and some may cost less, but altogether Google Ads will try to keep your cost per conversion equal to the target CPA you set. Bids are set from the predicted likelihood the ad converts, using real-time signals like device, browser, location, time of day, and remarketing list. Performance should be judged over at least 30 days with at least 30 conversions.
Sources: Google Ads Help: About Target CPA bidding, https://support.google.com/google-ads/answer/6268632
Last touched: 2026-08-18

### GA-004 · Under Target CPA, device bid adjustments modify the CPA target itself, not the bids
Tier: T1 · Status: active
A +40% mobile bid adjustment on a $10 tCPA does not raise bids 40%; it raises the mobile CPA target to $14. This inverts the intuition from manual bidding: a negative device adjustment under tCPA tells the system to demand cheaper conversions on that device, and -100% excludes it.
Sources: Google Ads Help: About Target CPA bidding, https://support.google.com/google-ads/answer/6268632
Last touched: 2026-08-18

### GA-005 · Target ROAS predicts the value of a potential conversion at every search and bids high or low on that prediction, holding average conversion-value-per-cost at the target
Tier: T1 · Status: active
Google's AI predicts conversion value each time a user searches and raises bids where high-value conversions are likely, lowering them otherwise. As with tCPA, individual conversions vary; the system aims to keep aggregate conversion value per cost equal to the target ROAS. Stated eligibility floors: at least 15 conversions in the past 30 days for Search/Shopping, roughly 50 in 35 days for Demand Gen, and app-campaign floors of 10 daily or 300 monthly.
Sources: Google Ads Help: About Target ROAS bidding, https://support.google.com/google-ads/answer/6268637
Last touched: 2026-08-18

### GA-006 · The Smart Bidding learning period lasts up to 3 weeks or 1-2 conversion cycles and is re-triggered by strategy, setting, or composition changes
Tier: T1 · Status: active
Learning status appears when a strategy is new or reactivated, a bid-strategy setting changes, or campaigns/ad groups/keywords are added or removed from the strategy. Duration is driven by conversion volume, conversion-cycle length (click-to-conversion lag), and strategy type; Manual CPC has no learning period. Google also notes the algorithms continue to learn after the Learning label disappears, and historical conversion data shortens ramp-up.
Sources: Google Ads Help: Duration of the learning period, https://support.google.com/google-ads/answer/13020501
Last touched: 2026-08-18

### GA-019 · Raising target ROAS shrinks the pool of users the campaign will bid on, and cold audiences are cut first
Tier: T3 · Status: active
Every increase in tROAS restricts who the campaign bids on. Cold users are cut first because they carry the lowest predicted value. The described pattern is a quarter of stepwise increases, 400% to 425% to 450% to 500%, at a flat $1,000/day. Reported ROAS moves from roughly 4 to roughly 6 and reads as excellent media buying. The 500% campaign is by then bidding almost entirely on people who already visited the site, already bought, or already saw the brand on Facebook. Lowering the target reopens the circle to colder users at worse measured efficiency. Verification method given: pull new-customer ROAS in a third-party tool. NC ROAS on a high-tROAS PMax campaign is typically poor, and the same campaign at a low target shows better NC ROAS. Operator rule: tROAS is an audience-temperature dial. Never read a tROAS-driven efficiency gain as a performance improvement until new-customer volume has been checked. A third statement of the same mechanism arrived on 2026-02-25, attributed second-hand to John Moran: squeezing target ROAS up does not produce a better return, it prioritises higher-intent bottom-of-funnel traffic. That version adds an inverted tactic this claim did not carry, setting target ROAS as low as 50% to deliberately force the campaign into top-of-funnel acquisition that then feeds retargeting. The 50% figure is second-hand, no account data sits behind it, and nobody has published a result from running it. The auction-level price of the same dial is recorded at GA-053: smart bidding bids up on high-intent users, so a cold campaign left eligible on the brand term pays $2 to $4 a click for traffic a dedicated brand campaign buys at roughly 2 cents. ASSERTED from agency practice. No account data shown on screen. Three source videos state it independently and the third is second-hand.
Sources: Blue Sense Digital, How to Scale an eCommerce Brand Profitably in 2026: The Full System, 2026-06-15; Blue Sense Digital, The Only Google Ads Strategy You Need for 2026, 2026-06-22; Blue Sense Digital, Why We Turned OFF Flexible Ads & Cost Caps in 2026, 2026-02-25
Last touched: 2026-08-19

### GA-020 · The tROAS death spiral is a closed loop: missing target cuts spend, thinner conversion data degrades the model, targeting worsens, volume falls again
Tier: T3 · Status: active
tROAS models primarily on the last 30 to 90 days of conversion data. An external volume shock starts the loop: a hero product goes out of stock, or a season turns, and 100 conversions become 80. Small-sample bias degrades targeting quality. The campaign misses target, spend contracts, volume falls further. The signature in the account is spend trailing off toward nothing over weeks while campaigns quietly die. The named operator error is under-correcting. A small target reduction does not break the loop and the account keeps declining. Escape requires cutting the target aggressively in one move. Catch it early on the spend curve. Same class of feedback loop as MM-004 (the CAC death spiral), running on the bidding system instead of the P&L. He reports onboarding accounts already mid-spiral and calling it in the audit. ASSERTED. No account data shown on screen. The two source videos state this independently.
Sources: Blue Sense Digital, How to Scale an eCommerce Brand Profitably in 2026: The Full System, 2026-06-15; Blue Sense Digital, The Only Google Ads Strategy You Need for 2026, 2026-06-22
Last touched: 2026-08-18

### GA-021 · Switching from maximize conversion value to target ROAS flattens day-to-day variance while the period average lands in roughly the same place
Tier: T3 · Status: active
Under maximize conversion value the campaign makes larger bets, so weeks alternate between strong efficiency and losses. tROAS flattens that curve. Total performance over the period averages out to roughly the same number. The honest reason to switch is predictability: weekly agency reporting and board-set budgets need a number that does not swing. The endorsed sequence stays launch on maximize conversion value to accumulate data, then roll into tROAS. That closing leg is contested. Grow My Ads opens cold Shopping builds on manual CPC or Maximize Clicks and moves to smart bidding only once conversion volume exists, recorded at GA-036 with both sides. The variance-flattening mechanism itself is uncontested. ASSERTED. Illustrated with hand-drawn performance curves on screen, no exported account data, so this is a practitioner assertion rather than a shown test.
Sources: Blue Sense Digital, The Only Google Ads Strategy You Need for 2026, 2026-06-22
Last touched: 2026-08-19

### GA-022 · Expansive bidding carries an implicit exploration budget of roughly 30% and restrictive bidding close to 0%, with the real exploration share set by the gap between target and achieved ROAS
Tier: T4 · Status: active
The speaker explicitly flags the 30% as a conceptual model he is theorising, not a measured figure, so the number is a teaching device and only the mechanism is the claim. Exploration means bidding on keywords, audiences, placements, regions and psychographic segments that historical conversion data does not yet favour but that sit adjacent to it. That is what unlocks new scale. Restrictive strategies route everything into hitting the number. The operationally testable part is the gap rule: a campaign achieving 4x against a 4.5x target explores close to zero, while a campaign achieving 5x against a 2x target behaves like an expansive strategy. Risk of permanent tROAS is data siloing and the GA-020 loop. Risk of permanent expansive bidding is unnecessary inefficiency. Prescription is to rotate between the two over long periods. Related feature named: smart bidding exploration on Search campaigns permits 10-30% excursions outside the tROAS band, and is not available on PMax or Shopping. ASSERTED, and self-flagged as illustrative.
Sources: Blue Sense Digital, How to Scale an eCommerce Brand Profitably in 2026: The Full System, 2026-06-15; Blue Sense Digital, The Only Google Ads Strategy You Need for 2026, 2026-06-22
Last touched: 2026-08-18

### GA-023 · In e-commerce use value-based bidding about 90% of the time, because maximize conversions optimises for lowest CPA and pushes spend into the cheapest SKU
Tier: T4 · Status: active
Maximize conversions optimises order count and cheapest acquisition. The worked example: a $40 t-shirt at roughly $20 CPA is a 2x return, a $200 jumper at roughly $60 CPA is a 3.5x return. A conversion-count objective funds the t-shirt, which inverts what the business wants. The same defect shows up on Meta at product level, where a hoodie drives $24 contribution margin per sale against a t-shirt's $12 but the t-shirt has the lower CPA. Caveat he adds there: switching to conversion-value optimisation does not always fix it, because the lower-margin product can also carry the better ROAS, and the real fix is campaign segmentation by product-level economics. This also sets which target strategy you graduate into, since tCPA is the restrictive form of maximize conversions and tROAS is the restrictive form of maximize conversion value. Audit check: on any account running maximize conversions, look at whether spend has collected on the lowest-priced products. Numbers are illustrative arithmetic, not an account result, so T4. ASSERTED.
Sources: Blue Sense Digital, How to Scale an eCommerce Brand Profitably in 2026: The Full System, 2026-06-15; Blue Sense Digital, The Only Google Ads Strategy You Need for 2026, 2026-06-22
Last touched: 2026-08-18

### GA-024 · Portfolio bidding strategies pool learnings across segmented campaigns and allow a max and min CPC on top of tROAS
Tier: T3 · Status: active
This is the escape hatch for accounts that had to segment for commercial reasons: grade C inventory that must move, new arrivals that need surfacing for seasonality, brand versus non-brand, per-margin categories. A portfolio strategy set at account level and applied across those campaigns houses their learnings together instead of leaving each to model on its own thin conversion slice. The second benefit is a hard CPC ceiling inside a smart strategy. His example is high-end furniture, where the platform will bid $20 to $30 on a single click that is never profitable regardless of intent. The enterprise equivalent sits in SA360 and is out of reach for most advertisers. Operator step: any account that failed the consolidation test for legitimate commercial reasons should be running a portfolio strategy across those campaigns. The mechanism underneath the pooling benefit is recorded at GA-037: bid signal is inherited from ad group, campaign, and account level, so a split account divides the pool that feeds the bid. ASSERTED. No test data shown. The two source videos state this independently.
Sources: Blue Sense Digital, How to Scale an eCommerce Brand Profitably in 2026: The Full System, 2026-06-15; Blue Sense Digital, The Only Google Ads Strategy You Need for 2026, 2026-06-22
Last touched: 2026-08-19

### GA-035 · For the first three months on a new Google account, buy conversion volume and ignore profitability, because there is nothing to optimise against until volume exists
Tier: T3 · Status: active
Austin's rule is that he does not care about profitability in the first three months on a new account. The goal is conversion volume, which he calls "finding the heat," because volume is what makes any analysis of what is working possible. Smart bidding and segmentation come after that window. The three months is a rule of thumb from portfolio experience, not a measured threshold, and no account data was shown. Read it with GA-036, the bid strategy he runs during that window, and GA-042, the budget floor that makes the window affordable. February 2025 claim, and Google has changed cold-start behaviour repeatedly since, so verify before applying to a 2026 build.
Sources: Blue Sense Digital, The Best Google Ad Structure in eCommerce (ft Austin from Grow My Ads), 2025-02-27
Last touched: 2026-08-19

### GA-036 · Cold-start bid strategy is contested: one agency opens new Shopping on manual CPC or Maximize Clicks, the other launches straight into maximize conversion value
Tier: T3 · Status: contested
Side one, Grow My Ads: open new Shopping builds on manual CPC or Maximize Clicks, and move to smart bidding only once the campaign has produced conversion volume. Manual CPC is the conservative option and Maximize Clicks the aggressive one, chosen by how much he trusts the client's backend data. He flags this as the point where most people argue with him, because Google pushes smart bidding from day one. Side two, recorded at GA-021: launch on maximize conversion value to accumulate data, then roll into tROAS. Both are T3 practitioner assertions, both from the same channel, and neither showed any data, so nothing in the material resolves it. Named failure mode on the aggressive option: running Maximize Clicks with an "everything else" catch-all product ad group in the same campaign lets the catch-all consume the budget before top sellers get spend, so either segment the catch-all further or take the conservative bid. What would resolve it: one account split at launch, manual CPC or Maximize Clicks against maximize conversion value, judged on cost per conversion at day 30 and day 90. February 2025 material on side one, and Google's smart bidding cold start has moved since.
Sources: Blue Sense Digital, The Best Google Ad Structure in eCommerce (ft Austin from Grow My Ads), 2025-02-27; Blue Sense Digital, The Only Google Ads Strategy You Need for 2026, 2026-06-22
Last touched: 2026-08-19

### GA-037 · Google inherits bid signal from ad group, campaign, and account level, so heavy campaign segmentation splits the conversion pool that feeds the bid
Tier: T4 · Status: active
Nathan's model of why over-segmentation degrades performance. Data sits in silos at ad group level, campaign level, and account level, and the auction bid draws on all three. Split an account into many campaigns and that pool divides, so no single campaign accumulates enough conversion volume to bid well. He frames the operating question as avoiding both 200 campaigns and a single campaign. This is his understanding of the system rather than documentation, and both speakers concede repeatedly that nobody outside Google knows the real mechanism, which holds it at T4. It is the mechanism underneath GA-024, where a portfolio bid strategy pools learnings back across campaigns that had to be split for commercial reasons.
Sources: Blue Sense Digital, The Best Google Ad Structure in eCommerce (ft Austin from Grow My Ads), 2025-02-27
Last touched: 2026-08-19

### GA-038 · Mixing low performers with high performers taxes the winners, because the system hits its target on the winners and spends the surplus testing the losers
Tier: T4 · Status: active
Austin's stated reason for segmenting at all. The bidding system knows it can reach the target ROAS from the high performers, so it keeps allocating budget to test the low performers on that headroom. Pulling the low performers out is meant to leave only high-converting inventory for the algorithm to work with. He offers this as a mental model with no test data. He also names the tension himself: the same episode carries a case where excluding roughly 18,000 SKUs at once killed the campaign, and the exclusions had to be reintroduced and then removed in chunks of about 5,000 to reach the same end state. So the direction may be right while the execution speed decides whether the campaign survives it. February 2025, T4, mechanism asserted with nothing shown.
Sources: Blue Sense Digital, The Best Google Ad Structure in eCommerce (ft Austin from Grow My Ads), 2025-02-27
Last touched: 2026-08-19

### GA-039 · Bidding-strategy edges still exist, target impression share is a named one, and Google closes each edge shortly after it is found
Tier: T3 · Status: active
The speaker says exploitable in-platform edges are still real and names target impression share targeting as one that was yielding a delta at the time. His claim about platform behaviour is that Google and Meta actively stamp these out, because neither wants an uneven field where one operator has found a bidding trick. The operating implication is that a micro-optimisation edge has a short half-life and cannot carry a service model. No test data was shown for the target impression share delta and no size was given for it. June 2025 claim, so assume the specific edge is already closed. The half-life rule is the durable part and the named tactic needs a fresh test before use.
Sources: Blue Sense Digital, The Future of Google Ads, AI & Agencies (with Caden), 2025-06-19
Last touched: 2026-08-19

### GA-060 · Set the ad schedule in hour increments at launch, then negate the day-parts that spend budget and return nothing
Tier: T3 · Status: active
The routine: at campaign launch set the ad schedule in one-hour increments, so the account reports traffic volume and traffic quality by hour of day rather than as a daily blur. Read it for a while, then cut the hours that consume clicks and return no purchases. The worked case is a B2C e-commerce account spending on clicks between 12am and 7am with no purchases coming through, which he negates out.
Named tension, unresolved anywhere in the material. Weekday and time of day in the user's timezone is a documented Smart Bidding signal at GA-002, so a campaign on a smart strategy already prices hour of day using more data than the operator can see. Hand-negating a day-part overrides that. The argument for doing it anyway is that a bid adjustment prices an hour while a schedule exclusion removes it, and those are different actions with different outcomes when the bidder's own model is wrong. Nobody has published the test either way, so treat this as a diagnostic worth reading before it is a change worth making.
ASSERTED. A standing operating routine across accounts. No day-part performance table, no before and after, no account shown.
Sources: Solutions 8 / The Google Ads Podcast, Google Ads Essentials: Tips & Strategies, 2025-12-11
Last touched: 2026-08-19

## Ad Rank and Quality

### GA-007 · Ad Rank is recalculated in every auction from bid, auction-time ad quality, thresholds, competitiveness, search context, and expected asset impact
Tier: T1 · Status: active
Google lists the Ad Rank factors as: your bid amount, the quality of your ads and landing page, the Ad Rank thresholds, the competitiveness of the auction, the context of the person's search (location, device, time of search, nature of search terms, other ads and results on the page, other user signals and attributes), and the expected impact of assets and other ad formats. Because it is recalculated each auction, ad position can fluctuate every time depending on competition, context, and quality at that moment.
Sources: Google Ads Help: About Ad Rank, https://support.google.com/google-ads/answer/1752122
Last touched: 2026-08-18

### GA-008 · Higher-quality ads can win a higher position at a lower price than higher-bidding competitors
Tier: T1 · Status: active
Google states that even if your competition bids higher, you can still win a higher position at a lower price by using highly relevant keywords and ads. Quality (via expected CTR, relevance, landing page) is a lever that substitutes for bid, so improving relevance is a direct cost-control mechanism, not just a hygiene metric.
Sources: Google Ads Help: About Ad Rank, https://support.google.com/google-ads/answer/1752122
Last touched: 2026-08-18

### GA-009 · When judging asset/format impact for Ad Rank, Google weighs the relevance, clickthrough rates, and prominence of the assets on the results page
Tier: T1 · Status: active
The expected impact of sitelinks, callouts, and other assets is an explicit Ad Rank input. Google assesses their relevance, expected CTR, and how prominently they would appear. Adding strong assets therefore raises Ad Rank without raising the bid.
Sources: Google Ads Help: About Ad Rank, https://support.google.com/google-ads/answer/1752122
Last touched: 2026-08-18

### GA-010 · Quality Score is a 1-10 keyword-level diagnostic and is NOT an input in the ad auction
Tier: T1 · Status: active
The visible Quality Score has three components: expected clickthrough rate, ad relevance, and landing page experience, each rated Above average / Average / Below average by comparison with advertisers whose ads showed for the same searches over the past 90 days. Google states explicitly that Quality Score is not an input in the ad auction; auction-time quality is calculated separately per auction. A dash shows when there are not enough exact-match searches to score the keyword.
Sources: Google Ads Help: About Quality Score, https://support.google.com/google-ads/answer/6167118
Last touched: 2026-08-18

## What a Click Actually Costs

### GA-011 · Actual CPC is the minimum needed to clear the Ad Rank thresholds and beat the Ad Rank of the competitor immediately below you
Tier: T1 · Status: active
You typically pay less than your max CPC because Google charges only what is minimally required to clear the thresholds and beat the next competitor's Ad Rank. Actual CPC is also influenced by competitors further down the stack, not just the one immediately below. With no eligible competitor below, you pay the reserve price.
Sources: Google Ads Help: Actual cost-per-click (CPC), https://support.google.com/google-ads/answer/6297
Last touched: 2026-08-18

### GA-012 · Actual CPC can exceed your max CPC when Enhanced CPC or bid adjustments are enabled
Tier: T1 · Status: active
The max-CPC cap on the charged click price has stated exceptions: Enhanced CPC and applied bid adjustments can push the actual charge above the entered maximum. Advertisers auditing CPCs above bid should check these settings before assuming a billing error.
Sources: Google Ads Help: Actual cost-per-click (CPC), https://support.google.com/google-ads/answer/6297
Last touched: 2026-08-18

### GA-013 · Ads above the search results carry higher Ad Rank thresholds and typically higher actual CPCs than ads below the results
Tier: T1 · Status: active
Google states that top-of-page positions have greater thresholds to maintain a high-quality experience, so an identical ad in top position typically pays a higher actual CPC than it would below the results even against the same competition. Position itself has a price premium built into the threshold system.
Sources: Google Ads Help: Actual cost-per-click (CPC), https://support.google.com/google-ads/answer/6297
Last touched: 2026-08-18

### GA-014 · Ad Rank thresholds are reserve prices set by ad quality, position, user signals, and the topic of the search; lower-quality ads face higher thresholds
Tier: T1 · Status: active
Thresholds determine auction eligibility and are determined by: ad quality (lower quality means higher thresholds), intended position (higher on page is stricter), user signals and attributes (location, device), and the topic and nature of the search (different query categories carry different thresholds). If your ad is the only eligible one, you pay the reserve price, the threshold rounded up to the minimum billable unit, which is why solo-auction CPCs can still be high.
Sources: Google Ads Help: About Ad Rank thresholds, https://support.google.com/google-ads/answer/7634668
Last touched: 2026-08-18

### GA-025 · CPC is a vanity metric: it correlates with return only at the extremes, because click quality varies with the auctions the bidding entered
Tier: T3 · Status: active
He reports accounts with high CPCs and high ROAS, and accounts with the reverse, at both campaign and product level. The identity that matters is CPA = CPC / conversion rate. Rising CPCs are fine as long as conversion rate rises with them, because CPA holds. The failure state is CPCs rising while conversion rate stays flat, which points to quality score, a new competitor, or entering premium auctions that do not pay off. The extremes carry real information: at $100 CPCs you will never be profitable, and at 10c CPCs the traffic is junk and you will also never be profitable. In between the metric says almost nothing. A lower CPC frequently means worse users, because the bidding model bought a cheaper pool. Diagnostic columns when CPCs move: expected CTR, ad relevance, landing page experience. Landing page experience is the hardest to shift because Google's rescan cadence is unpublished and can take weeks or months. He states the same holds on Meta and TikTok. Baseline to subtract before diagnosing any CPC move: a December 2025 episode reports small CPC increases year over year across client accounts as a standing annual trend, with no numbers attached, so a small yearly drift should be treated as background cost inflation and not opened as an investigation. ASSERTED from "any large data set and analysis". No dataset shown on screen. The three source videos state this independently.
Sources: Blue Sense Digital, How to Scale an eCommerce Brand Profitably in 2026: The Full System, 2026-06-15; Blue Sense Digital, The Only Google Ads Strategy You Need for 2026, 2026-06-22; Blue Sense Digital, Google Ads in 2026 (w/ Austin from Grow My Ads), 2025-12-15
Last touched: 2026-08-19

### GA-053 · A cold campaign left eligible on the brand term pays $2 to $4 a click for traffic a dedicated brand campaign buys at roughly 2 cents
Tier: T3 · Status: active
The mechanism is Smart Bidding doing exactly what it is built to do. It raises bids on high-intent users, and nobody on Google is higher intent than a person typing the brand name. Leave a cold prospecting campaign eligible on that query and the bidding system pays a premium for a user who was going to click the organic listing anyway. Segment the same query into its own campaign with its own bid strategy and the click costs roughly 2 cents. The stated spread is 100x to 200x on the same user.
Prevalence: the same agency reports brand overspend inside supposedly cold campaigns in roughly 90% of the Google accounts it audits, at $2,000 a month and at $100,000 a month alike, and calls it the single most common defect it finds. Brand terms surface across multiple campaigns regardless of the exclusions already in place, which is why the check has to be run on search terms rather than on the settings.
Fix stack given: PMax brand exclusions, dedicated brand Search and brand Shopping campaigns, brand negatives on everything cold. Claimed result across the majority of onboarded accounts is a 10x to 20x cut in cost allocated to brand, released back into acquisition or efficiency.
This is the auction-level price of the dial in GA-019. Target ROAS sorts users by predicted value and brand searchers sit at the top of that sort, so the same lever that looks like an efficiency gain is buying the cheapest possible demand at the highest possible price. Before applying the fix stack read GA-054, which questions whether the brand campaign needs to exist at all, and note that hard brand exclusions carry a stated cost in branded Shopping recorded in the PMax and Shopping file.
ASSERTED. The $2 to $4, the 2 cents, the 90% and the 10x to 20x are all stated from memory across an audit book. No account, no screenshot, no before and after was shown.
Weak corroboration added 2026-08-20, and it is recorded as weak on purpose. A second agency says in passing that a brand whose volume sits on high-intent branded search sees "better pricing" on a blended basis than a comparable brand "dealing with expensive non-branded clicks in a brutal category with a weaker offer." It is one clause inside a budgeting answer, it carries no branded or non-branded CPC, and it was not the point being made. It moves the direction of this claim not at all. Logged so the next reader knows it was found and weighed rather than missed.
Sources: Blue Sense Digital, 6 Step Checklist to Increase Google Ad Performance, 2025-03-06; Solutions 8, 2026-05-19, "How Much Should You Spend on Google Ads? (And When to Stop)" (passing corroboration, no figures)
Last touched: 2026-08-20

### GA-054 · Almost no e-commerce brand has a competitor bidding on its brand keyword, including every nine-figure brand this agency has audited
Tier: T3 · Status: active
The claim runs against the standard defensive argument for brand campaigns. Across seven-, eight- and nine-figure brands the reported finding is that nobody is bidding on the brand term. Named cases: every nine-figure brand audited, plus multiple $50m to $60m brands either worked with or audited. The cost of defending against nobody scales with brand size. A brand pulling 100,000 to 200,000 brand searches a month is described as spending $30,000 to $50,000 a period defending a slot no competitor contests, and the stated recommendation is to cut it.
This sits alongside GA-053 rather than against it. Nobody bidding is precisely why the segmented brand click costs 2 cents, and 2 cents is also why the line item never gets questioned. GA-053 stops the cold campaign paying $2 to $4. This claim asks the next question, whether the cheap brand campaign should run at all.
Two checks before cutting. Auction Insights on the brand term answers the competitor question directly for any specific account, and the speaker never opened it on camera. And hard brand exclusions have a named cost in branded Shopping, where vacating the slot lets competitors place shopping ads above the brand's own organic listing, which is recorded in the PMax and Shopping file. A brand with genuinely zero competitors on Search may still lose money by vacating Shopping.
ASSERTED. Every figure is recalled across an audit book. No auction insights screen, no account, no spend table was shown.
Sources: Blue Sense Digital, Best Google Ad Account Structure for eCommerce in 2025, 2025-09-02
Last touched: 2026-08-19

## Keyword Intent and Landing Page Fit

### GA-015 · Keyword modifiers map to positions on the intent spectrum: 'best' = commercial interest, 'review'/'versus' = active narrowing, 'pricing' = budget-fit check, 'buy' = transactional
Tier: T3 · Status: active
Buyer intent lives on a spectrum rather than binary ready/not-ready. 'Best' signals commercial interest, 'review' and 'versus' signal option-narrowing, 'pricing' signals someone testing whether the offer fits their budget (closer to purchase), and 'buy' is the most transactional. These modifiers separate searchers still learning from searchers actively choosing.
Sources: Solutions 8 / The Google Ads Podcast, Buyer Intent Keywords: How to Find the Ones That Actually Drive Sales, 2026-07-21
Last touched: 2026-08-18

### GA-016 · Validate keyword intent by reading the SERP: top results full of product/category/comparison/pricing pages indicate buyer intent; beginner guides and definitional content indicate an awareness-stage keyword
Tier: T3 · Status: active
Google's ranking of a query reveals what it thinks the searcher wants. If the SERP for a candidate keyword shows product pages, category pages, comparison articles, review pages, pricing pages, and best-of lists, it is high buyer intent. If it shows beginner guides, definitions, and educational explainers about the problem rather than solutions, the keyword is earlier-funnel even if it contains intent-looking words, which is also why high-volume keywords with 'buy'/'comparison' in them can still deliver mixed, low-value traffic when the underlying search intent is broad.
Sources: Solutions 8 / The Google Ads Podcast, Buyer Intent Keywords: How to Find the Ones That Actually Drive Sales, 2026-07-21
Last touched: 2026-08-18

### GA-017 · Mid-intent comparison/review/best keywords catch buyers during the decision stage, letting the advertiser control the comparison before competitors do, and are often more profitable than obvious bottom-funnel 'buy now' terms
Tier: T4 · Status: active
Teams over-focus on bottom-funnel keywords because they are the lowest-hanging fruit. But consideration-stage keywords (review, comparison, best-of) reach people while they are still deciding, which is framed as an often more profitable point in the journey because you shape the comparison narrative before a competitor does. Plausible funnel logic asserted without supporting campaign data.
Sources: Solutions 8 / The Google Ads Podcast, Buyer Intent Keywords: How to Find the Ones That Actually Drive Sales, 2026-07-21
Last touched: 2026-08-18

### GA-018 · No buyer-intent keyword can overcome a landing page that mismatches the search intent; the mismatch shows up as high bounce rate, which feeds back into Google's evaluation
Tier: T4 · Status: active
Even a perfectly chosen transactional keyword fails if the landing page lacks matching messaging, does not satisfy the searcher's intent, or leaves the next action unclear. The stated mechanism is that bounce rate climbs and "Google never forgets," meaning poor page experience compounds into worse outcomes for the keyword over time. The bounce-rate-memory mechanism is asserted without evidence; Google's use of bounce signals in Ads is not demonstrated, which is why this stays T4 even though the landing-page-fit half echoes the T1 landing page experience component in GA-010.
Sources: Solutions 8 / The Google Ads Podcast, Buyer Intent Keywords: How to Find the Ones That Actually Drive Sales, 2026-07-21
Last touched: 2026-08-18

### GA-026 · Landing page split testing is the largest lever in Search, because auction power is a function of conversion rate and AOV
Tier: T3 · Status: active
Everything done inside the platform, segmentation, asset groups, audience signals, feed work, exists to enter better auctions. A competitor converting at twice your rate can outbid you with worse ads and worse structure and still win. Doubling site conversion rate lets you pay double per click at identical economics. That makes conversion rate and AOV the only durable way to outbid someone whose numbers beat yours. Implementation given: duplicate the ad inside one ad group pointing at two different landing pages, judge on conversion rate over 30 to 60 days, retire the loser, rotate the next challenger in, compound. He states almost nobody does this. Extends AU-004 (your bid is your unit economics) from Meta onto Google Search with a concrete test method. ASSERTED. No test results shown. The two source videos state this independently.
Sources: Blue Sense Digital, How to Scale an eCommerce Brand Profitably in 2026: The Full System, 2026-06-15; Blue Sense Digital, The Only Google Ads Strategy You Need for 2026, 2026-06-22
Last touched: 2026-08-18

### GA-059 · Changing the CTA from "Get started" to "Schedule your free consultation" raised conversion rate over a 30-day single-variable test, and the magnitude was never stated
Tier: T3 · Status: active
A real single-variable test with a clean control and an unusable magnitude. One account, 30 days, the CTA text changed on both the ad and the landing page with nothing else moved. The reported outcome is a much higher conversion rate on "Schedule your free consultation" and what the speaker calls a clear-cut winner. No conversion rate was given for either arm, no traffic volume, no account. The size of the win cannot be checked and cannot be planned against, which holds this at T3. A test whose magnitude nobody states gives a direction and nothing to forecast with.
The diagnostic behind it is weaker still. Qualified traffic was hovering on the CTA without clicking, read as the CTA demanding more commitment than the visitor's stage in the journey supports. Naming the specific next action is the stated fix. No hover data or heatmap was shown, so that half is interpretation rather than observation.
Test-design rule stated alongside: give a Google Ads A/B test about a month so it clears learning, and move exactly one variable inside the window. The documented version of the learning period sits at GA-006 and is the harder number to work from.
Transferable form: the winning CTA named what happens next and the losing one described a state. Test it against your own front-end offer rather than adopting the wording. Read with GA-026, which puts landing page split testing as the largest lever in Search and gives the duplicate-ad-two-pages method for running it, and with GA-018 on intent-to-page fit.
Sources: Solutions 8 / The Google Ads Podcast, Google Ads Essentials: Tips & Strategies, 2025-12-11
Last touched: 2026-08-19

## Search Campaign Structure

### GA-027 · Single-keyword ad groups are obsolete: an RSA has about 2,700 combinations and needs roughly 250,000 to 270,000 impressions to resolve, which an exact-match SKAG cannot generate
Tier: T3 · Status: active
An RSA takes 15 headlines and 4 descriptions and assembles them dynamically, producing about 2,700 servable combinations. At an assumed 100 impressions per combination the ad group needs roughly 270,000 impressions to exit learning. He flags 100 impressions per combination as generously low, so the real requirement is higher. A single exact-match keyword cannot deliver that volume, so most SKAG ad groups sit in learning indefinitely. SKAGs worked before 2020 because ads were static: 3 headlines, 1 or 2 descriptions, fixed order, so the advertiser chose the exact pairing. The replacement is single-TOPIC ad groups: 10 to 20 themed keywords per ad group, with ads tuned to the theme. His example split is general plumbing, emergency plumbing, affordable plumbing. He reports migrating onboarded SKAG accounts to single-topic ad groups and "always" seeing better performance. ASSERTED. The permutation arithmetic is sound, the impression threshold is his own assumption, and no before/after data was shown. The two source videos state this independently.
Sources: Blue Sense Digital, How to Scale an eCommerce Brand Profitably in 2026: The Full System, 2026-06-15; Blue Sense Digital, The Only Google Ads Strategy You Need for 2026, 2026-06-22
Last touched: 2026-08-18

### GA-028 · Exact match no longer means exact: it now matches on same meaning, phrase match has broadened, and broad match is unchanged
Tier: T3 · Status: active
This is the second leg of the SKAG argument in GA-027 and it independently invalidates keyword-level control strategies. A pure exact-match ad group now receives semantic variants, so the operator assumption that one keyword equals one query is false. Practical consequences: search term reports must be reviewed even on exact-match ad groups, negative keywords are still required at exact match, and any legacy architecture premised on exact-match precision should be rebuilt. ASSERTED from practice with no Google documentation cited in the transcript, so it sits at T3. This is publicly documented platform behaviour and should be verified against Google's own help docs and promoted to T1 on confirmation.
Sources: Blue Sense Digital, The Only Google Ads Strategy You Need for 2026, 2026-06-22
Last touched: 2026-08-18

### GA-029 · The first 30 days of a Search campaign is the highest-leverage window for negative keywords; after that, cadence should drop because every change resets learning
Tier: T3 · Status: active
New campaigns go out deliberately broad, so the early search term report carries the most irrelevant placements and the most recoverable waste. Review weekly in that window, daily at high budgets. After the first month the trade reverses: each negative keyword edit costs some learning stability, so continuous tinkering turns net negative. Drop to weekly or fortnightly. Pair this with an account-level universal negative list that every new campaign inherits automatically, holding employment-intent terms (jobs, careers, interns, hiring, salary) and similar universal junk. That list can be sourced publicly or generated with an LLM. Two-part operator rule: front-load the negative work, then leave it mostly alone. ASSERTED. No test data on the learning-reset cost.
Sources: Blue Sense Digital, The Only Google Ads Strategy You Need for 2026, 2026-06-22
Last touched: 2026-08-18

### GA-040 · Judge products and brands against the account's own trailing average, not against the target ROAS, when deciding what to consolidate
Tier: T3 · Status: active
Austin's diagnostic on an over-segmented account that is struggling. Pull a year of data, compute the account-wide blended average, for example a 2x ROAS and a 1% conversion rate, and treat that as the bar. Brands and products beating the account average on both volume and conversion rate are the keep candidates. The target ROAS is the wrong bar for this decision because it describes what the business wants rather than what the account has ever produced. Before acting he requires answers on seasonality, price changes, and promos that could explain the gap. The 2x and 1% are illustrative, no client data was shown. This is the account-level form of the same discipline as GA-034: complete the causal sentence before touching anything.
Sources: Blue Sense Digital, The Best Google Ad Structure in eCommerce (ft Austin from Grow My Ads), 2025-02-27
Last touched: 2026-08-19

### GA-041 · Win consolidated first, then segment, because a working consolidated campaign can be split later and a fractured account cannot be repaired quickly
Tier: T3 · Status: active
Austin's sequencing rule after the loss of SKAG and Alpha/Beta control. Lean consolidated at the start, get the campaign converting, then segment for business reasons once volume exists. He applies it to both the new-account roadmap and the rescue of an already over-segmented account. The asymmetry is the whole argument: splitting a working campaign is reversible, and restarting a broken one is slow. He also gates segmentation on being able to name the business reason, margin differences between categories or removing proven low performers, and on the segment having enough conversion volume to survive alone. Portfolio-wide practitioner claim, no data shown. February 2025, before later Google structure changes.
Sources: Blue Sense Digital, The Best Google Ad Structure in eCommerce (ft Austin from Grow My Ads), 2025-02-27
Last touched: 2026-08-19

### GA-042 · Grow My Ads' working minimum for a new ecommerce Google account is $5,000 to $10,000 a month, and below it everything stays in one campaign
Tier: T3 · Status: active
Austin states his agency mostly works with clients who have at least $5,000 to $10,000 a month to start. The number is tied directly to the segmentation advice in GA-041: below it he keeps everything in one campaign rather than splitting top sellers out, because the split campaigns would each be too thin to accumulate conversion data. It is stated as a client filter and no evidence was given that performance breaks at that threshold, so treat it as an agency intake rule rather than a measured floor. February 2025 figure, so inflate it for 2026 CPCs before quoting it to anyone.
Sources: Blue Sense Digital, The Best Google Ad Structure in eCommerce (ft Austin from Grow My Ads), 2025-02-27
Last touched: 2026-08-19

## Reading the Account: Reporting Artefacts and Diagnosis

### GA-030 · Google attributes conversions to the CLICK date, not the purchase date, so the last 3-4 days of any Google report always look bad
Tier: T3 · Status: active
Timeline given: a click on the 1st, another click on the 3rd, a purchase on the 7th. Most platforms record the conversion on the 7th. Google backdates it to the click. The result is a structural, universal artefact: any trailing 3 to 7 day window shows depressed ROAS that fills in later. Beginners misread it as a real performance collapse and act on it. The remedy is the "conversions by conversion time" column, added as a custom column. This is the first of three checks he requires before any diagnostic work, alongside checking change history and extending the time horizon. Direct consequence for any weekly reporting cadence that pulls a trailing window on Google: the most recent days are always understated and must be labelled as incomplete. ASSERTED, and consistent with documented Google attribution behaviour, though no platform doc was cited in the transcript.
Sources: Blue Sense Digital, How to Scale an eCommerce Brand Profitably in 2026: The Full System, 2026-06-15
Last touched: 2026-08-18

### GA-031 · Using GA4 events as the primary conversion action loses roughly 10-15% of conversions versus a direct Google Ads snippet
Tier: T3 · Status: active
He says the gap is "sometimes even higher" than 15%, so treat 10-15% as a floor. This is a signal-starvation problem before it is a reporting problem: smart bidding models on the conversions it actually receives, so the missing tenth degrades bidding accuracy as well as understating performance. His 90-day rollout puts this first, ahead of any structural work, alongside enhanced conversions and auto-tagging switched on. Audit step: check whether the primary conversion action is a GA4 import or a direct Google Ads tag. If it is GA4, install the snippet and re-designate primary before touching structure or bidding. ASSERTED. No measurement of the gap was shown, and the figure is a practitioner range rather than a tested delta.
Sources: Blue Sense Digital, The Only Google Ads Strategy You Need for 2026, 2026-06-22
Last touched: 2026-08-18

### GA-032 · Three default settings silently leak Google budget: display enabled inside Search campaigns, broad match paired with a non-smart bidding strategy, and auto-apply recommendations left on
Tier: T3 · Status: active
All three are on-by-default or easy-to-miss states rather than strategy errors, which is why they survive in accounts for years. Display expansion inside a Search campaign pushes cold spend onto the Display network. Broad match requires a smart bidding strategy to function, so broad plus maximize clicks is structurally broken rather than merely suboptimal. Auto-apply recommendations lets Google make unattended account changes he says are almost never in the advertiser's interest. Add to the same sweep: missing branded negatives on cold campaigns, and missing negatives generally. These are the first checks in any Google audit. That last item is the biggest of them and it is now quantified separately at GA-053: the same agency reports brand overspend inside supposedly cold campaigns in roughly 90% of the accounts it audits, at $2,000 a month and at $100,000 a month alike. ASSERTED. No quantification of the leak was given for any of the three named settings.
Sources: Blue Sense Digital, The Only Google Ads Strategy You Need for 2026, 2026-06-22
Last touched: 2026-08-19

### GA-033 · "Limited by budget" shows on nearly every campaign at any spend level, so it is a weak indicator and never evidence that profitable incremental spend exists
Tier: T3 · Status: active
Google surfaces the status whenever the campaign could theoretically enter more auctions, which is nearly always true. He reports seeing it on essentially every account regardless of spend level, including PMax campaigns spending $5,000 to $10,000 a day into a small total addressable market in Australia. Practical use: treat it as one weak input alongside actual incremental back-end revenue and impression share, and never let it drive a budget increase on its own. This matters because it is the most common in-platform prompt pushing advertisers into overspend. ASSERTED from agency observation. No data shown.
Sources: Blue Sense Digital, The Only Google Ads Strategy You Need for 2026, 2026-06-22
Last touched: 2026-08-18

### GA-034 · Diagnose declines top-down and complete the causal sentence before touching the account; rebuilds are the last resort
Tier: T3 · Status: active
The sequence is business KPI, then cross-channel, then campaign type, then campaign, then metric, then submetric, using CPA = CPC / conversion rate and clicks = impressions x CTR, with revenue = conversion rate x AOV x sessions at business level. The gate he imposes: you may not touch the account until you can complete "this campaign is underperforming because this metric dropped, driven by this submetric, caused by this trigger, which is the root cause." Prior steps before any of it: check change history, extend the time horizon, correct for Google's click-date conversion latency (GA-030), and check whether the channel even carries enough spend share to explain a business-level move. A campaign holding 10% of Google spend inside a 40% Google mix cannot explain a business decline. Rebuilds come last because they trigger a learning reset that deepens the decline, producing a change-decline-change spiral. ASSERTED as an agency process. No case data shown.
Sources: Blue Sense Digital, How to Scale an eCommerce Brand Profitably in 2026: The Full System, 2026-06-15
Last touched: 2026-08-18

### GA-043 · Broad match, shopping feeds, PMax, and AI Max can already serve inside AI Overviews and AI Mode, with no advertiser control and no reporting segmentation
Tier: T3 · Status: active
As of December 2025, an account running broad match keywords, shopping ads with a feed, Performance Max, or AI Max had the potential to serve inside AI Overviews and AI Mode. There is no setting to turn it off and no report that breaks those clicks out, so no advertiser can state what share of spend landed there. His words: "I have no reporting either. So I don't even know if I'm getting clicks there or not and how many." He hoped Google would ship the reporting during 2026, which is worth re-checking now. This is a live measurement blind spot rather than a tactic, and it is the most consequential Google claim in this batch. Two consequences for us. Any account of ours running any of those four surfaces contains an unmeasured spend allocation, and any statement we make about where Google budget went inherits that unknown. Practitioner claim with no platform documentation cited, so verify against Google's current help docs and promote to T1 on confirmation.
Sources: Blue Sense Digital, Google Ads in 2026 (w/ Austin from Grow My Ads), 2025-12-15
Last touched: 2026-08-19

### GA-044 · One agency's whole book shows no paid-side decline from zero-click AI results, with the traffic collapse landing on informational and publisher pages instead
Tier: T3 · Status: active
Austin accepts that the traffic declines are real for media sites built on blog posts and articles, which sit on the informational side of the journey. On the advertising side he reports seeing no decline anywhere across his client accounts, in either ad clicks or revenue. His structural argument is that Google will not cannibalise the ad revenue that makes up the majority of its business. This is a portfolio-level assertion across a book of accounts and zero numbers were given: no account count, no spend, no click or revenue deltas, no before-and-after window, no control. The one movement he does report is small yearly CPC increases, which he treats as a normal annual trend rather than an AI effect, also with no figure attached. December 2025 claim, AI Mode has expanded since, so re-check rather than assume it still holds. Pair it with GA-043: an absence of a visible decline is weaker evidence when the surface in question has no reporting at all.
Sources: Blue Sense Digital, Google Ads in 2026 (w/ Austin from Grow My Ads), 2025-12-15
Last touched: 2026-08-19

### GA-061 · Never commit a Google Ads click count, because click volume is buyable and click quality is not
Tier: T4 · Status: active
A promised number of clicks inside a stated window is a red flag on whoever promised it. Volume can be bought at any time by bidding for it, and nothing in that purchase makes the clicks qualified or capable of producing customers. The honest form of the same conversation is a projection against industry benchmarks, labelled as a projection. Small claim, and it is the entry-level form of a discipline the codex already runs elsewhere: GA-033 says the equivalent about "limited by budget" as evidence that profitable incremental spend exists, and GA-025 says it about CPC as a performance metric.
ASSERTED with no data. A stated position on forecastability rather than a finding.
Sources: Solutions 8 / The Google Ads Podcast, Google Ads Essentials: Tips & Strategies, 2025-12-11
Last touched: 2026-08-19

## Google's Product Cycle and Platform Roadmap

### GA-045 · Google ships ad products before they work, pushes them through reps, and some become genuinely good later, so put a re-test date on every product you rejected
Tier: T4 · Status: active
Austin's pattern claim across three product cycles. Smart bidding was "hot garbage" at launch and he was a manual CPC loyalist. Broad match was likewise rejected and later became what he calls a Nitro boost when layered in correctly. He expects PMax to follow the same arc, which is why he keeps testing it against his own instinct. He also names the distribution mechanism: Google reps hound accounts telling them they are behind unless they adopt the new product, and that pressure is how the tech gets trained. Operating rule: schedule a re-test of any Google product you have dismissed instead of holding a permanent position on it. This is also why GA-047 on AI Max reads as a snapshot rather than a verdict. Pattern reasoning with no data, and the three examples are selected after the fact, so survivorship is uncontrolled.
Sources: Blue Sense Digital, The Best Google Ad Structure in eCommerce (ft Austin from Grow My Ads), 2025-02-27
Last touched: 2026-08-19

### GA-046 · Cap novel structural tests at 10 to 20 percent of the account portfolio, and never promote a single account's result to a rule
Tier: T4 · Status: active
Nathan's rule for handling novel tactics, with John Moran's feeder strategy and Target Impression Share on Search as the named examples. Cap exposure at 10 to 20 percent of accounts. He states the failure mode directly: one tiny data set gets read as a rule and rolled out everywhere when it was probably an edge case. Austin runs the same discipline in reverse and refuses to publish a tactic until it works for the majority, restricting risky tests to clients with high risk tolerance. This is the evidence standard the codex runs on, applied to account management. Reasoning only, no data, and the 10 to 20 percent is a stated preference rather than a derived number.
Sources: Blue Sense Digital, The Best Google Ad Structure in eCommerce (ft Austin from Grow My Ads), 2025-02-27
Last touched: 2026-08-19

### GA-047 · AI Max showed no measurable benefit across a large agency's ongoing testing as of December 2025, and Google is expected to push it harder regardless
Tier: T3 · Status: active
Austin's words are that he has not really seen too much benefit from it from their testing, run across a large number of accounts. Testing is referenced and zero numbers were given: no account count, no spend, no CPA or ROAS comparison, no control, no window. Treat this as an unquantified practitioner read and never quote it as a null result. He expects Google to push AI Max heavier through 2026 on the reasoning that Google does not build and resource a product for fun, and he allows that it may become good during the year. Surrounding structural point: Google now ships four products that solve substantially the same problem, PMax, dynamic search ads, broad match, and AI Max, and advertisers commonly run all four at once with no model of what each one is doing. His speculation, flagged as speculation by him, is that DSA is the retirement candidate because AI Max covers the same capability. December 2025 snapshot of a product under active development, so assume it is stale and run a fresh test before taking any position.
Sources: Blue Sense Digital, Google Ads in 2026 (w/ Austin from Grow My Ads), 2025-12-15
Last touched: 2026-08-19

### GA-048 · Expect Google to keep forcing YouTube inventory into automated campaign types, because YouTube revenue growth is a standing item in every quarterly earnings call
Tier: T4 · Status: active
Austin's method for predicting Google product behaviour is to read the quarterly earnings calls, where YouTube advertising growth is a recurring priority. The precedent he cites is factual: Performance Max's launch pushed advertisers into YouTube inventory unless they ran feed-only. His forecast of more of the same through 2026 is a prediction, which holds this at T4 even though the precedent behind it is solid. He cites no specific report and no figure. The transferable part is the method: platform roadmap is legible from public earnings priorities, so read those before assuming a product push is about advertiser performance.
Sources: Blue Sense Digital, Google Ads in 2026 (w/ Austin from Grow My Ads), 2025-12-15
Last touched: 2026-08-19

### GA-049 · A one-click world bids acquisition cost up to the product's remaining margin, while the LLM query shift expands ad inventory first and fills it later
Tier: T4 · Status: active
Two halves of the same auction argument. First, when the platform compresses the funnel to a single click from query to purchase, competition bids costs up until the margin left on the product is exhausted, which is the structural ceiling on pure demand capture. The speaker extends it to shopping-intent queries inside LLMs and asks why anyone would place on a query that returns $1 of contribution. Second, he estimates his own behaviour moved from about 3 Google searches a day to about 20 questions a day, generalises that to a 2x to 5x increase in total query volume, and concludes costs should stay flat in the short term because inventory expands faster than budgets. Then the inventory fills, budgets follow, and it becomes expensive demand capture again. He says outright that he does not know the real number, so 2x to 5x is a guess. The same conversation notes Alphabet reported its first quarter of declining Google search volume. June 2025 reasoning, no measured result, and the query-volume half is now testable against public data.
Sources: Blue Sense Digital, The Future of Google Ads, AI & Agencies (with Caden), 2025-06-19
Last touched: 2026-08-19

## Channel Fit: Where Google Belongs and When YouTube Pays

### GA-050 · Google Ads is a middle and mostly bottom funnel channel, with bottom of funnel defined as non-brand product or service intent
Tier: T3 · Status: active
Michael Nadalin, who is publicly known for Google Ads work, says he does not recommend Google Ads for top of funnel to any client. He places it middle and mostly bottom funnel and defines bottom of funnel as someone proactively searching for the product or service. A search for the brand name does not count. That exclusion matters in reporting, because a Google account carried by brand search is being credited for demand another channel created. His paired position is that Meta owns middle and top funnel capture. Asserted from client experience, no data shown, December 2025.
Sources: Blue Sense Digital, Two Years Later: What Still Works (And What Doesn't) ft. Michael Nadalin, 2025-12-27
Last touched: 2026-08-19

### GA-051 · YouTube stays off the plan for most accounts on four grounds, with a stated threshold of roughly $200,000 a month on Meta before it is worth considering
Tier: T3 · Status: active
The four reasons given: YouTube needs a lot of spend, its placement algorithm is worse than Meta's at learning where to put ads, attribution is poor because viewers rarely click and buy so the effect runs as a halo, and reading the channel at all requires MMM and incrementality tooling that smaller businesses do not have. The stated rule of thumb is that a business spending $50,000 a month on Meta should probably get to $200,000 a month there before considering YouTube. Austin agrees and says he steers clients to Meta first. A creative constraint sits alongside it: pasting a working Meta ad straight into YouTube fails most of the time and the asset has to be rebuilt for the platform. A second agency puts a number on the spend requirement: YouTube campaigns have never performed for him below $400 a day, because under that the campaign cannot gather enough signal to work out who to prioritise. Those are two different gates and both should be read. $400 a day is where the campaign can function at all. $200,000 a month on Meta is where it is worth the attention. Practitioner claim, no test data shown, and the $50,000, $200,000 and $400 figures are all thresholds stated from experience rather than measured breakpoints. December 2025 on the first source, September 2025 on the second.
Sources: Blue Sense Digital, Google Ads in 2026 (w/ Austin from Grow My Ads), 2025-12-15; Blue Sense Digital, Best Google Ad Account Structure for eCommerce in 2025, 2025-09-02
Last touched: 2026-08-19

### GA-052 · YouTube pays reliably in three cases: high-ticket info with a VSL funnel, a brand with a large existing YouTube channel to remarket against, and budgets big enough for it to be a line item
Tier: T3 · Status: active
Austin's segmentation of where YouTube ads work. High-ticket info products running a VSL funnel work well. A brand with a substantial existing YouTube presence can target and remarket to viewers of its own channel and videos, which is the second reliable case. The third is very large budgets, where YouTube is a line item next to something like $250,000 on Meta, search, and shopping. Ecommerce brands are harder in his experience. This is the positive counterpart to GA-051, so read the pair together before ruling YouTube in or out for a client. Practitioner observation from client and prospect conversations, no data shown. December 2025, and YouTube campaign types change often, so re-check the mechanics before building.
Sources: Blue Sense Digital, Google Ads in 2026 (w/ Austin from Grow My Ads), 2025-12-15
Last touched: 2026-08-19

### GA-055 · A 21-day Demand Gen geo holdout produced no statistically relevant new-customer lift and an implied incremental CAC of $140
Tier: T2 · Status: active
The first Google claim in this codex carrying a real test with real numbers. Every other Google claim we hold is practitioner assertion or platform documentation.
Design. Single geo holdout, Australia, 21 days. Test geo was Victoria plus Queensland, selected by correlating monthly order volume state to state, screening p-values, then cross-correlating to find the states that best predict the rest. Control was the rest of Australia. Baseline was 12 months of daily orders. New-customer and returning-customer orders were measured separately. Confidence set at 90%.
New customers, the acquisition question: expected 2,771 orders, actual 2,857, a lift of 85 against the 166 needed for 90% confidence. No statistical relevance. Implied incremental CAC on new customers was $140, unprofitable on first purchase, and the speaker says plainly the figure is not even statistically supportable before it is unprofitable. New-customer orders fell in both arms over the window: down 4.5% in the rest of Australia, down 1.41% in the test states.
Returning customers, where the campaign did move: a 6.8% period-on-period lift in the test states while the rest of Australia dipped. Expected 1,211 returning-customer orders, achieved 1,521, at $39 per returning-customer order.
Operating decision taken directly off the result: Demand Gen kept running at significantly reduced budget and reclassified as a returning-customer retargeting campaign rather than an acquisition campaign.
Data integrity note, and it belongs on the claim. The transcript's baseline figures are internally inconsistent. A roughly 2,500-order baseline and a 254-order lift threshold are stated early, then 2,771 expected and a 166 threshold at 90% appear later. The reconciliation that fits is that the 2,500 and 254 pair is the 95% confidence scenario used to size the budget before the test, and the 2,771 and 166 pair is the 90% read used to call the result. Nobody restated it on camera, so carry the ambiguity forward with the numbers.
SHOWN. Real spend, counts and the significance threshold stated explicitly, analysis narrated on screen. The interpretation of why it came out this way is a separate and weaker thing, held at GA-056.
Cross-file note, 2026-08-19. The same test is filed twice more. AT-072 in the Attribution file holds it as the geo-holdout method and the new-versus-returning split rule, and the PMax and Shopping file references it as GP-040 from the incrementality side. One test, three entries by design, because it answers a different question in each file. This entry is the Google channel verdict on Demand Gen. Never count it as more than one experiment when weighing evidence.
Sources: Blue Sense Digital, We Tested Google Demand Gen - Here's What Happened, 2025-07-24
Last touched: 2026-08-19

### GA-056 · Demand Gen harvests users already inside the funnel, so any lift is instantaneous, exhausts, and then converts into returning-customer spend
Tier: T3 · Status: active
This is the speaker's reading of his own measured result at GA-055, laid over the measurement rather than drawn from a second test. The mechanism claimed: whatever lift Demand Gen produces comes from going quickly after people already warm and already in the funnel, capitalising on top-of-funnel traffic that other channels created. Once that pool is exhausted the campaign either does nothing or moves onto returning customers and burns budget. The measured pattern is consistent with it: no new-customer lift, a 6.8% returning-customer lift at $39 an order.
Portfolio-level generalisations from the same agency, both without numbers. March 2025: Demand Gen had not delivered consistent, provable cold customer acquisition across four to five larger accounts under active test, and rep pressure to adopt it is a sales motion rather than a performance recommendation. August 2025: Demand Gen significantly over-attributes and has no positive impact on new customer acquisition for 90%+ of ad accounts. The speaker time-stamps the August version himself and tells the viewer to check the publication date, because Google keeps tweaking the product.
Operating rule that falls out: never read a Demand Gen lift blended. Split returning-customer order lift from new-customer order lift, or a retargeting result reads as acquisition.
ASSERTED. The mechanism is interpretation, and the four-to-five-account and 90%+ figures are recalled with nothing shown. Read GA-045 before treating this as permanent: Google ships ad products before they work and some become good later, so this needs a re-test date rather than a standing position.
Sources: Blue Sense Digital, We Tested Google Demand Gen - Here's What Happened, 2025-07-24; Blue Sense Digital, 6 Step Checklist to Increase Google Ad Performance, 2025-03-06; Blue Sense Digital, Best Google Ad Account Structure for eCommerce in 2025, 2025-09-02
Last touched: 2026-08-19

### GA-057 · Cold Search is a post-$50,000-a-month channel in e-commerce and stops scaling around $100 a day, while lead generation search scales to $500,000 a month
Tier: T3 · Status: active
Two claims from the same agency about how far Google's non-Shopping channels actually go. First, the sequencing gate: cold Search, YouTube and Demand Gen do not outperform a PMax plus standard Shopping pair until the account is spending at least $50,000 a month, at which point cold Search becomes the next step. Second, the ceiling: plenty of e-commerce accounts under management run cold Search profitably at roughly $100 a day, and cold Search does not carry from there to thousands or tens of thousands a day on an e-commerce brand. Lead generation behaves differently, with managed accounts spending $500,000 a month on Search alone.
The asymmetry is the useful part. On e-commerce, Search is a small profitable line rather than a scaling engine. On lead generation, Search carries the whole account. Any Google threshold quoted at us should be checked against which of those two businesses it came from before it is applied, because most published Google structure advice is written from e-commerce.
ASSERTED. The $50,000 gate is a stated threshold rather than a measured breakpoint, the same standing as GA-042. The $100 a day and the $500,000 a month describe real managed spend recalled from memory. No account, no CPA, no dates were shown. September 2025.
Sources: Blue Sense Digital, Best Google Ad Account Structure for eCommerce in 2025, 2025-09-02
Last touched: 2026-08-19

### GA-058 · Search out-returns Shopping for the 2% to 4% of e-commerce accounts carrying a B2B component
Tier: T3 · Status: active
The default for e-commerce is Shopping first, and that default was filed to the PMax and Shopping file from this same episode. This is the named exception to it. Where the business has a B2B component, Search campaigns sometimes return better than Shopping, because B2B buyers click Search ads over Shopping ads and arrive at a higher average order value, and that AOV gap outweighs Shopping's conversion-rate advantage. The speaker sizes the exception at 2% to 4% of e-commerce advertisers and states outright that he does not know why B2B buying prefers Search.
Operator use: run this check when an e-commerce account has a trade, wholesale or business-buyer segment and Shopping is underperforming the default expectation. A consumer-only account gets no benefit from the test.
ASSERTED. Observed across a client book. No ROAS comparison, no AOV figures, no account shown, and the causal explanation is explicitly unknown to the speaker.
Sources: Blue Sense Digital, 6 Step Checklist to Increase Google Ad Performance, 2025-03-06
Last touched: 2026-08-19

## Test Instruments Google Ships

### GA-062 · AI Max experiments are a documented within-campaign A/B, and brand inclusions and exclusions apply to BOTH arms, so the guardrail stops confounding the test
Tier: T1 · Status: active
Read off Google's own help article, "About AI Max experiments". The split is inside one existing Search campaign: a percentage of it runs with the AI Max toggle off as the control, the remaining percentage runs with the toggle on as the treatment. Because both arms are the same campaign, the campaign's own bidding history, budget and conversion history are held constant across the comparison.
The clause that matters most is verbatim: "If you add brand inclusions or brand exclusions during setup, these settings will automatically apply to both your control and treatment arms for the duration of the experiment." Until now, testing AI Max meant choosing between the test and the brand guardrail. Holding the guardrail identical on both sides removes it as a confound.
Settings that can be enabled inside the experiment: text customization and final URL expansion under Asset optimization, search term matching with an ad-group-level disable, brand inclusions and exclusions, URL exclusions at campaign level, URL inclusions at ad group level. Reporting lands in three places, the Experiments platform, the Keywords page and the Ads page. One documented blocker: you cannot create an AI Max experiment through this flow if the campaign already has text customization, formerly automatically created assets, enabled. The article states no minimum duration and no minimum budget.
The 2026-08-20 product blog is the announcement half: "New capabilities in AI Max experiments now let you run tests with these settings enabled, so you can confidently test the impact of AI Max without compromising those guardrails."
**Why this is the most useful Google item banked in weeks.** [[Google Auction & Smart Bidding#GA-047|GA-047]] is the codex's only AI Max performance claim and it is an unquantified practitioner read from December 2025 with zero numbers behind it, which the codex already forbids quoting as a null result. This is the instrument that replaces it with our own number. [[Google Auction & Smart Bidding#GA-045|GA-045]] says to put a re-test date on every Google product we dismissed, and this supplies the mechanism for that re-test.
TIER GUARD, on the TT-029 and MD-099 precedent: T1 for existence, documented surface and product copy ONLY. Nothing here states that AI Max performs. Google shipping a measurement tool is not a performance result, and the tool being first-party means the arms are defined by the party selling the product.
Sources: Google Ads Help, About AI Max experiments, support.google.com/google-ads/answer/16450159, read 2026-08-21; Google Ads & Commerce Blog, Make AI Max work for your business with new testing and planning tools, 2026-08-20
Last touched: 2026-08-21

### GA-063 · Google announced a multi-campaign A/B for budgets and ROI targets for September 2026, which is the first instrument that could settle the budget step-size question with data
Tier: T1 · Status: active
Announcement only, dated 2026-08-20, verbatim: "we're now introducing a way for you to test different budgets and ROI targets across multiple Search campaigns in a single A/B test. Rolling out in September, this will help you see exactly how scaling up your campaigns impacts your bottom line." Zero numbers appear in the post. No case study, no aggregate, no named advertiser.
Why it is worth banking before it ships. [[Scaling Models#SC-001|SC-001]] holds budget step size at 3% to 100% per day, contested, across three transcripts with no controlled step-size test anywhere in the codex. [[Google Auction & Smart Bidding#GA-019|GA-019]] holds target ROAS as an audience-temperature dial at T3 on three sources and no experiment. Both sit at folklore tier for the same reason, which is that nobody runs the controlled test. This is that test, on the Google half of the book, built by the platform.
It is not live. September 2026 is the stated window and the post gives no eligibility, no minimum spend and no campaign-count requirement. Do not plan a Q3 test calendar against it until it appears in an account.
Same post, third item, and it carries a guard rather than an opportunity. Performance Planner "now allows you to see how changes, like bidding or budget targets, may impact your existing campaign performance. In one click, you can apply those suggested changes directly to your campaigns." A Performance Planner output is a Google forecast. It is not a measurement of anything that happened. This is the same standing as [[Meta Delivery & Andromeda#MD-099|MD-099]] on Opportunity Score, and the one-click apply raises the stakes, because accepting an unvalidated vendor forecast becomes a single click with no experiment attached. Never report a Performance Planner projection to a client as a result, and never let a one-click apply substitute for GA-062's experiment.
Sources: Google Ads & Commerce Blog, Make AI Max work for your business with new testing and planning tools, 2026-08-20
Last touched: 2026-08-21

