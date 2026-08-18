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
Every increase in tROAS restricts who the campaign bids on. Cold users are cut first because they carry the lowest predicted value. The described pattern is a quarter of stepwise increases, 400% to 425% to 450% to 500%, at a flat $1,000/day. Reported ROAS moves from roughly 4 to roughly 6 and reads as excellent media buying. The 500% campaign is by then bidding almost entirely on people who already visited the site, already bought, or already saw the brand on Facebook. Lowering the target reopens the circle to colder users at worse measured efficiency. Verification method given: pull new-customer ROAS in a third-party tool. NC ROAS on a high-tROAS PMax campaign is typically poor, and the same campaign at a low target shows better NC ROAS. Operator rule: tROAS is an audience-temperature dial. Never read a tROAS-driven efficiency gain as a performance improvement until new-customer volume has been checked. ASSERTED from agency practice. No account data shown on screen. The two source videos state this independently.
Sources: Blue Sense Digital, How to Scale an eCommerce Brand Profitably in 2026: The Full System, 2026-06-15; Blue Sense Digital, The Only Google Ads Strategy You Need for 2026, 2026-06-22
Last touched: 2026-08-18

### GA-020 · The tROAS death spiral is a closed loop: missing target cuts spend, thinner conversion data degrades the model, targeting worsens, volume falls again
Tier: T3 · Status: active
tROAS models primarily on the last 30 to 90 days of conversion data. An external volume shock starts the loop: a hero product goes out of stock, or a season turns, and 100 conversions become 80. Small-sample bias degrades targeting quality. The campaign misses target, spend contracts, volume falls further. The signature in the account is spend trailing off toward nothing over weeks while campaigns quietly die. The named operator error is under-correcting. A small target reduction does not break the loop and the account keeps declining. Escape requires cutting the target aggressively in one move. Catch it early on the spend curve. Same class of feedback loop as MM-004 (the CAC death spiral), running on the bidding system instead of the P&L. He reports onboarding accounts already mid-spiral and calling it in the audit. ASSERTED. No account data shown on screen. The two source videos state this independently.
Sources: Blue Sense Digital, How to Scale an eCommerce Brand Profitably in 2026: The Full System, 2026-06-15; Blue Sense Digital, The Only Google Ads Strategy You Need for 2026, 2026-06-22
Last touched: 2026-08-18

### GA-021 · Switching from maximize conversion value to target ROAS flattens day-to-day variance while the period average lands in roughly the same place
Tier: T3 · Status: active
Under maximize conversion value the campaign makes larger bets, so weeks alternate between strong efficiency and losses. tROAS flattens that curve. Total performance over the period averages out to roughly the same number. The honest reason to switch is predictability: weekly agency reporting and board-set budgets need a number that does not swing. The endorsed sequence stays launch on maximize conversion value to accumulate data, then roll into tROAS. ASSERTED. Illustrated with hand-drawn performance curves on screen, no exported account data, so this is a practitioner assertion rather than a shown test.
Sources: Blue Sense Digital, The Only Google Ads Strategy You Need for 2026, 2026-06-22
Last touched: 2026-08-18

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
This is the escape hatch for accounts that had to segment for commercial reasons: grade C inventory that must move, new arrivals that need surfacing for seasonality, brand versus non-brand, per-margin categories. A portfolio strategy set at account level and applied across those campaigns houses their learnings together instead of leaving each to model on its own thin conversion slice. The second benefit is a hard CPC ceiling inside a smart strategy. His example is high-end furniture, where the platform will bid $20 to $30 on a single click that is never profitable regardless of intent. The enterprise equivalent sits in SA360 and is out of reach for most advertisers. Operator step: any account that failed the consolidation test for legitimate commercial reasons should be running a portfolio strategy across those campaigns. ASSERTED. No test data shown. The two source videos state this independently.
Sources: Blue Sense Digital, How to Scale an eCommerce Brand Profitably in 2026: The Full System, 2026-06-15; Blue Sense Digital, The Only Google Ads Strategy You Need for 2026, 2026-06-22
Last touched: 2026-08-18

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
He reports accounts with high CPCs and high ROAS, and accounts with the reverse, at both campaign and product level. The identity that matters is CPA = CPC / conversion rate. Rising CPCs are fine as long as conversion rate rises with them, because CPA holds. The failure state is CPCs rising while conversion rate stays flat, which points to quality score, a new competitor, or entering premium auctions that do not pay off. The extremes carry real information: at $100 CPCs you will never be profitable, and at 10c CPCs the traffic is junk and you will also never be profitable. In between the metric says almost nothing. A lower CPC frequently means worse users, because the bidding model bought a cheaper pool. Diagnostic columns when CPCs move: expected CTR, ad relevance, landing page experience. Landing page experience is the hardest to shift because Google's rescan cadence is unpublished and can take weeks or months. He states the same holds on Meta and TikTok. ASSERTED from "any large data set and analysis". No dataset shown on screen. The two source videos state this independently.
Sources: Blue Sense Digital, How to Scale an eCommerce Brand Profitably in 2026: The Full System, 2026-06-15; Blue Sense Digital, The Only Google Ads Strategy You Need for 2026, 2026-06-22
Last touched: 2026-08-18

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
All three are on-by-default or easy-to-miss states rather than strategy errors, which is why they survive in accounts for years. Display expansion inside a Search campaign pushes cold spend onto the Display network. Broad match requires a smart bidding strategy to function, so broad plus maximize clicks is structurally broken rather than merely suboptimal. Auto-apply recommendations lets Google make unattended account changes he says are almost never in the advertiser's interest. Add to the same sweep: missing branded negatives on cold campaigns, and missing negatives generally. These are the first checks in any Google audit. ASSERTED. No quantification of the leak was given for any of the three.
Sources: Blue Sense Digital, The Only Google Ads Strategy You Need for 2026, 2026-06-22
Last touched: 2026-08-18

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

