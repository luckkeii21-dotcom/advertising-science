---
title: "Google PMax & Shopping"
type: codex-topic
claim_prefix: GP
created: 2026-08-18
tags: [advertising-science, codex]
---

# Google PMax & Shopping

Performance Max internals, feed mechanics, brand cannibalization, channel decomposition.

Part of the [[00-Codex|Advertising Science Codex]]. Claims follow the tier system (T1 docs, T2 shown test, T3 practitioner, T4 theory).

## Claims

## PMax vs Search Priority

### GP-001 · An exact match keyword in a Search campaign that matches the query beats Performance Max; search themes rank only equal to phrase/broad keywords.
Tier: T1 · Status: active
Google's stated priority rule: when a search query matches an exact match keyword in your Search campaign, the Search campaign is prioritized over Performance Max. Search themes in PMax get the same prioritization as phrase and broad match keywords in Search campaigns, so exact-match coverage is the advertiser's lever for keeping queries in the controllable campaign. Brand exclusions in PMax prevent branded-query overlap.
Sources: Google Ads Help: About Performance Max / Use search themes, https://support.google.com/google-ads/answer/14767319
Last touched: 2026-08-18

### GP-002 · Search themes are optional, additive, capped at 50 per asset group, and do not override exclusions or negative keywords.
Tier: T1 · Status: active
Search themes add the words and phrases customers use, on top of the queries and placements PMax already predicts from your assets, feeds, and landing pages. Up to 50 unique themes per asset group. Google states exclusions and negative keywords still apply, so themes expand reach without disabling the account's negative controls.
Sources: Google Ads Help: Use search themes with your Performance Max campaign, https://support.google.com/google-ads/answer/14767319
Last touched: 2026-08-18

## How PMax Buys

### GP-003 · Performance Max serves one campaign across YouTube, Display, Search, Discover, Gmail, and Maps, bidding with Smart Bidding plus attribution technology in real time.
Tier: T1 · Status: active
A single PMax campaign buys across all six Google surfaces against the advertiser's stated goal (sales, leads, store visits), using Smart Bidding combined with attribution technology to set bids across that inventory in real time, maximizing conversions or conversion value. Asset groups are themed creative collections from which the system assembles ads, and Google may combine advertiser-provided assets with AI-generated ones.
Sources: Google Ads Help: About Performance Max campaigns, https://support.google.com/google-ads/answer/10724817
Last touched: 2026-08-18

### GP-004 · PMax audience signals are suggestions that guide and accelerate Google AI; they are not targeting constraints.
Tier: T1 · Status: active
Google frames audience signals (remarketing lists, Customer Match, custom segments) as inputs that enhance the AI's optimization toward your goals, and best-practice guidance says they guide the AI and accelerate ramp-up. The campaign can and will serve beyond the supplied audiences; the signal shapes where learning starts, not where delivery ends.

Practitioner extension added 2026-08-18 (T3, ASSERTED). The guidance window is roughly 30 days. Once about 30 days of conversion data has accumulated inside the campaign, Google bypasses the signal, and removing the audience signal produces no measurable performance change. On a mature account spending $30-100k/month on PMax, tweaking audience signals or search themes is "a one percenter at best", so an agency audit whose headline recommendation is signal tuning is proposing a non-intervention. Signals and search themes earn their keep in the cold-start window only: new account, new campaign, new asset group, new category, where they stop Google wasting budget on random exploration. When search themes are used, populate them from converting terms in the account's own historical search-term report rather than inventing them. Evidence base stated as PMax on 250+ accounts plus roughly 400 consulted e-commerce accounts from 7 to 10 figures. No test output shown. Consistent with the ranking in GP-010, where signals and search themes rank last of five variables.
Sources: Google Ads Help: About Performance Max campaigns, https://support.google.com/google-ads/answer/10724817; Blue Sense Digital, How to Scale an eCommerce Brand Profitably in 2026: The Full System, 2026-06-15; Blue Sense Digital, The Only Google Ads Strategy You Need for 2026, 2026-06-22
Last touched: 2026-08-18

## PMax attribution and incrementality

### GP-005 · PMax over-attributes: 50% or more of PMax conversions are repeat or warm customers it did not acquire, and standard shopping running beside it is structurally under-credited.
Tier: T3 · Status: active
The mechanism is last-click credit theft inside one account. Standard shopping does the cold acquisition, PMax retargets and takes the final click before conversion, so the account reads as PMax scaling while shopping carries the acquisition. Presented as the consensus among large Google agencies "behind closed doors" three years after PMax replaced smart shopping. Evidence base stated as running PMax on 250+ accounts plus consulting on roughly 400 more e-commerce accounts from 7 to 10 figures. ASSERTED. No screenshots or exports described. Operator consequences: never judge the PMax-versus-shopping budget split on in-platform ROAS, and never kill standard shopping because PMax shows a better return next to it. The recommended reframe is to treat it as a split question, with roughly 20-40% PMax and the balance in standard shopping for most mid-to-upper-market ecom. See GP-006 for the test that produced this claim and GP-008 for the strategy built on it.
Sources: Blue Sense Digital, How to Scale an eCommerce Brand Profitably in 2026: The Full System, 2026-06-15; Blue Sense Digital, The Only Google Ads Strategy You Need for 2026, 2026-06-22
Last touched: 2026-08-18

### GP-006 · Ramping PMax 2x over 30 days held reported ROAS flat at 5x with no backend revenue lift; the same ramp on standard shopping dropped reported ROAS to 3-4x and produced materially better backend revenue.
Tier: T3 · Status: active
Run as parallel ramps on separate accounts, described as repeating "every single time we ran the test". The reading: a PMax ROAS that refuses to move while spend doubles means retargeting is absorbing the extra budget instead of the campaign finding new customers. Standard shopping's falling ROAS under the same ramp is the honest signal of reaching colder users. Two extra observations from the same source: PMax campaigns pushed to $100-300k/month stopped showing up in backend revenue at all, and PMax performs well on smaller accounts (roughly $15-20k/month and below) then hits a ceiling above that. This is a direct trap for anyone treating in-platform ROAS stability as evidence that a campaign is scaling. Numbers stated verbally, no dashboards or exports described, so ASSERTED rather than shown. Scope: e-commerce retail accounts.
Sources: Blue Sense Digital, How to Scale an eCommerce Brand Profitably in 2026: The Full System, 2026-06-15; Blue Sense Digital, The Only Google Ads Strategy You Need for 2026, 2026-06-22
Last touched: 2026-08-18

### GP-007 · Google and PMax ROAS stays halo-inflated even with brand excluded; the cheap falsification is to add $1,000 to the campaign and check whether $20,000 of top line appears.
Tier: T3 · Status: active
A separate mechanism from the intra-account credit theft in GP-005. Here the claim is that Google takes credit for demand generated on other platforms and by organic presence, so brand exclusions alone do not clean the number. He is explicit that Google can acquire genuinely incremental new customers at $100-200k/month, which makes this a measurement claim about the reported figure. The test is the operator's fastest and cheapest falsification: a campaign reporting 20x should return roughly proportional top line on a marginal budget increase, and it usually does not. ASSERTED. No test output shown. Pairs with GP-020 on uncontested brand search, which is where ROAS-as-north-star produces the largest waste at 8 and 9 figure retailers.
Sources: Blue Sense Digital, The 1 Bottleneck I See in 80% of eCommerce Audits, 2026-05-18
Last touched: 2026-08-18

## PMax and standard shopping as a pair

### GP-008 · Feeder strategy: standard shopping at a deliberately low target ROAS (as low as 50%) buys the cold query pool, and a high-target-ROAS PMax (~600%) closes on the second or third click.
Tier: T3 · Status: active
The arbitrage is auction-side. Most advertisers set high efficiency targets, so they all crowd into the same high-intent half of the query pool, while the low-intent half (first-time searchers, no site history) attracts almost no bidders and is cheap to reach. The low-tROAS campaign buys that whole pool at low cost, then the high-tROAS campaign converts the survivors on a later click. Standard shopping is the cold vehicle because it reaches cold audiences better than PMax does. This is the strategic answer to GP-005: assign PMax the closing role deliberately instead of fighting it for credit. Expect the cold campaign's own reported ROAS to look bad by design. Judge the pair together on backend revenue, never campaign by campaign. Lead-gen equivalent: substitute search for shopping. ASSERTED, no paired-account numbers shown.
Sources: Blue Sense Digital, How to Scale an eCommerce Brand Profitably in 2026: The Full System, 2026-06-15; Blue Sense Digital, The Only Google Ads Strategy You Need for 2026, 2026-06-22
Last touched: 2026-08-18

## PMax configuration

### GP-009 · A PMax campaign without brand exclusions is a retargeting campaign; run the campaign-level brand list and PMax negative keywords together.
Tier: T3 · Status: active
The brand list is built in campaign settings under brand exclusions, where Google indexes the brand and captures branded variants. PMax negative keywords are a newer addition and did not previously exist, so many accounts carry only one of the two. He runs both deliberately as redundant failsafes: a missed keyword variation is caught by the brand list, and a broken or incomplete negative list is caught by the brand list, and vice versa. Without exclusions, PMax retargets existing brand traffic and returns no incremental value. Same rule applies to Search, where brand should also be excluded from non-brand campaigns. This ranks second in the GP-010 importance ordering, which makes it the highest-leverage single fix in most accounts. ASSERTED across three separate videos, no data shown.
Sources: Blue Sense Digital, How To Structure Your Meta Ads for Profit (Free Live Webinar), 2025-02-19; Blue Sense Digital, How to Scale an eCommerce Brand Profitably in 2026: The Full System, 2026-06-15; Blue Sense Digital, The Only Google Ads Strategy You Need for 2026, 2026-06-22
Last touched: 2026-08-18

### GP-010 · PMax variable importance, in order: 1) GMC feed, 2) brand exclusions, 3) asset and listing group structure plus asset quality, 4) bidding strategy, 5) audience signals and search themes.
Tier: T3 · Status: active
Directly usable as an audit sequence, and it inverts where most operators spend their time, since signal tuning and bid tinkering sit last. The feed ranks first conditional on the campaign actually prioritising Shopping placements in an e-commerce account. Brand exclusions rank second on the blunt justification in GP-009. Assets rank third on a plain creative argument: bad headlines, images and descriptions produce bad ads regardless of structure. The practical read is that a PMax account with a clean feed and brand exclusions and nothing else configured beats an account with perfect signals and a raw default feed. Asserted as an agency heuristic. No ranked test data shown.
Sources: Blue Sense Digital, How to Scale an eCommerce Brand Profitably in 2026: The Full System, 2026-06-15; Blue Sense Digital, The Only Google Ads Strategy You Need for 2026, 2026-06-22
Last touched: 2026-08-18

### GP-011 · PMax asset groups: one per product type with the listing group customised to match, at least 15 products each, 3 minimum and roughly 20 maximum per account.
Tier: T3 · Status: active
Default cut is one asset group per product type (chairs/tables/lighting/decor, or hand tools/power tools/fasteners/accessories). The step most accounts skip is customising the listing group to match, so every asset group ends up holding every product anyway. A single-product asset group is a red flag because it will not attract meaningful spend. Segmentation at this level buys four things that consolidation would otherwise cost: creative relevance in retargeting and cold display, more granular audience signals, more specific search themes, and per-product-type performance visibility. Running a single default asset group is named as the biggest single PMax mistake. Testing basis: roughly 200 to 400 asset groups launched on test accounts when PMax rolled out, with simpler structures winning every time. Product-count thresholds are SKU-count dependent and stated with flexibility. ASSERTED, no comparative numbers shown.
Sources: Blue Sense Digital, How to Scale an eCommerce Brand Profitably in 2026: The Full System, 2026-06-15; Blue Sense Digital, The Only Google Ads Strategy You Need for 2026, 2026-06-22
Last touched: 2026-08-18

### GP-012 · Feed-only PMax: delete every asset group, leave only the listing group, and PMax is confined to Shopping plus display remarketing. Requires URL expansion OFF and automatically created assets OFF.
Tier: T3 · Status: active
Deleting asset groups removes the headlines, descriptions and images PMax needs to assemble ads for Search, YouTube, Discover and Gmail, so the only inventory left is the GMC product tile. This reproduces the old smart shopping behaviour. Two settings silently undo it: URL expansion scrapes site URLs and rebuilds asset groups automatically, and automatically created assets regenerates the missing headlines and descriptions. Both must be off. Use cases: forcing spend into the Shopping placement, and rescuing a campaign that has drifted into unwanted placements (see GP-013). Can be applied per category, so some PMax campaigns in an account run feed-only while others keep full asset groups. ASSERTED, no before/after data shown.
Sources: Blue Sense Digital, How to Scale an eCommerce Brand Profitably in 2026: The Full System, 2026-06-15; Blue Sense Digital, The Only Google Ads Strategy You Need for 2026, 2026-06-22
Last touched: 2026-08-18

### GP-013 · PMax Gmail placements count the user opening the generated email as the click rather than an outbound visit, so click volume inflates while site traffic does not.
Tier: T3 · Status: active
Named diagnostic signature: click volume rises sharply, CPC drops to around 10 cents, ROAS falls, and the clicks never appear as site sessions. Case described on an account spending a few hundred thousand per month: PMax drifted from roughly 2% to roughly 10% of spend on YouTube plus roughly 10% into cold Gmail, clicks spiked at about 10c CPC, ROAS fell about 20%. The team's first hypothesis was bot traffic. The real cause was placement drift inside PMax. Secondary damage is reputational: recipients see what looks like an email, believe the brand emailed them after they unsubscribed, and do not accept the explanation that it was an ad. The fix applied was converting the campaign to feed-only (GP-012) so it could not physically place on Gmail or over-allocate to YouTube, after which the account resumed scaling. Client case, numbers stated verbally, ASSERTED.
Sources: Blue Sense Digital, How to Scale an eCommerce Brand Profitably in 2026: The Full System, 2026-06-15; Blue Sense Digital, The Only Google Ads Strategy You Need for 2026, 2026-06-22
Last touched: 2026-08-18

## The Merchant Center feed

### GP-014 · GMC titles: brand name last, front-load keywords proven in the search terms report, pack in every relevant attribute, and treat variants as separate listings.
Tier: T3 · Status: active
The default Shopify-style title (brand + internal product name + size + colour) spends the highest-value positions on tokens nobody searches. The brand is redundant when brand terms are excluded and already displays at the bottom of the listing, and a proprietary product name means nothing to a shopper who is not product-aware. Google weights keyword match by position in the title, so the rebuild is proven query first, then product type, then attributes, then brand ("formal dress [product name] size 12"; for CPG, "dissolvable creatine powder clear flavored portable [brand]"). Attribute density expands the query surface the listing can place on, since a title carrying "blue" can rank for "blue dress". Keywords must come from the account's own search-term conversion data, never invented. Variant hack: a 50g/100g/500g product generates three separate shopping listings, so each can carry a different title, image and description targeting a different keyword pool while sharing one landing page. Roll title changes out slowly, because a bulk rollover resets learning across every campaign. ASSERTED, no lift numbers shown.
Sources: Blue Sense Digital, Why Most Fashion Brands Are Running Paid Media Wrong, 2026-05-25; Blue Sense Digital, How to Scale an eCommerce Brand Profitably in 2026: The Full System, 2026-06-15; Blue Sense Digital, The Only Google Ads Strategy You Need for 2026, 2026-06-22
Last touched: 2026-08-18

### GP-015 · Supply shopping images at 4:5 through a supplementary feed and optimise for contrast against neighbouring listings; the image is roughly 70% of the listing's real estate.
Tier: T3 · Status: active
Common fashion defect: source imagery is 9:16 and Google auto-crops it badly on ingestion. Override with a supplementary feed carrying 4:5 assets, Google's current preferred ratio (1:1 also acceptable). The selection logic is the Meta hook logic applied to Shopping: the goal is a click from the right person, so maximising raw CTR on the wrong audience is a loss. Within brand constraints the practical lever is differentiating from the five or six competitor listings sitting beside you, for example shooting on a coloured background when everyone else shoots on white, or running a lifestyle image with a model in a row of white-background product shots. He reports running the contrast test repeatedly with CTR going up; the conversion-rate effect is unproven and no numbers were shown. Price and title move the click at the margins, the image is the primary click driver.
Sources: Blue Sense Digital, Why Most Fashion Brands Are Running Paid Media Wrong, 2026-05-25; Blue Sense Digital, How to Scale an eCommerce Brand Profitably in 2026: The Full System, 2026-06-15; Blue Sense Digital, The Only Google Ads Strategy You Need for 2026, 2026-06-22
Last touched: 2026-08-18

### GP-016 · Run one GMC feed per currency; a single multi-currency feed shows a live-converted price label that kills CTR and conversion rate.
Tier: T3 · Status: active
Running all regions through one feed makes the listing display a live conversion, labelled "converted from AUD" or "converted from USD plus tax". The damage is trust rather than arithmetic: the label tells the shopper they are buying from an international store, so they price in customs risk, shipping delay and returns friction before clicking. Reported as a frequent audit finding on multi-region accounts where every region has been bolted onto one feed. The fix is a one-time setup per currency, in the same "clean it once" category as descriptions and the remaining feed attributes. ASSERTED, no CTR or CVR deltas shown.
Sources: Blue Sense Digital, How to Scale an eCommerce Brand Profitably in 2026: The Full System, 2026-06-15; Blue Sense Digital, The Only Google Ads Strategy You Need for 2026, 2026-06-22
Last touched: 2026-08-18

### GP-017 · Fashion size curves: set a dynamic feed rule that pulls the whole product out of the feed the moment its highest-sell-through size goes out of stock, because efficiency drops roughly 50% otherwise.
Tier: T3 · Status: active
The size curve is the silent performance killer in fashion. When the core size (often medium) sells out, the remaining sizes keep serving, click quality collapses, and both Shopping and Meta performance fall overnight with no account change to explain it. Rather than absorbing the decline, pull all sizes of that product from the feed at the moment the core size hits zero. He names size-curve management as the single biggest Google lever at the $75-200k/month tier. The 50% figure is stated as an approximation, ASSERTED, no data shown.
Sources: Blue Sense Digital, Why Most Fashion Brands Are Running Paid Media Wrong, 2026-05-25
Last touched: 2026-08-18

## Shopping versus Search allocation

### GP-018 · E-commerce retail should run 80-90% of Google spend through Shopping rather than Search, because the listing delivers pre-click information that pre-qualifies the click.
Tier: T3 · Status: active
The mechanism is information asymmetry at click time. A search ad gives a headline, a description almost nobody reads, and some extensions, so the user spends $1-2 of your money discovering whether the product matches, which is fatal in visual categories. A shopping listing shows image, price, title, reviews, promos and brand against five competitors simultaneously, so the user has already run the comparison and self-selected before clicking. Post-click conversion rates run high as a result. Conclusion: saturate the shopping network first in essentially any e-commerce business, then add search for incremental volume. Fashion-specific thresholds from the same source: Shopping takes 80%+ of Google budget under $75k/month and 60-70% above it, because text ads in fashion only work off pre-existing brand recognition and therefore do not transfer to an unknown brand in a new market. Scope: e-commerce retail. For lead gen, substitute search everywhere he says shopping. See GP-019 for the exception. ASSERTED, no comparative account data shown.
Sources: Blue Sense Digital, Why Most Fashion Brands Are Running Paid Media Wrong, 2026-05-25; Blue Sense Digital, The Only Google Ads Strategy You Need for 2026, 2026-06-22
Last touched: 2026-08-18

### GP-019 · Exception to shopping-first: e-commerce with a B2B component performs better on Search, because business buyers skip retail-priced shopping listings when they need bulk or supplier pricing.
Tier: T3 · Status: active
The buyer-side mechanism is a price-expectation mismatch. A purchaser sourcing bulk tea or bulk eyelash supplies sees $5-10 shopping tiles, reads them as consumer retail, and jumps to text listings to find someone who does trade pricing. Described as intuitive to the buyer, who has already learned that B2B does not happen on the shopping network. Operator step: for any account with a wholesale, trade or bulk revenue line, do not apply the 80-90% shopping split from GP-018. Run search campaigns against supplier and bulk-intent queries and let shopping handle the consumer side. Single-agency observation, ASSERTED, no comparative numbers given.
Sources: Blue Sense Digital, The Only Google Ads Strategy You Need for 2026, 2026-06-22
Last touched: 2026-08-18

### GP-020 · Large retail fashion brands systematically overspend on branded search even when no competitor is bidding on the term.
Tier: T3 · Status: active
Stated from roughly 20+ large retail fashion audits: brand search consistently absorbs a large share of Google spend with no auction pressure justifying it. The operating instruction is to cut brand spend rather than defend an uncontested term. Pairs with GP-007 and the incrementality frame generally: brand search is the most bottom-of-funnel surface available, so it is where platform ROAS looks best and incremental contribution is lowest. Thin evidence, one sentence in the transcript, ASSERTED with no per-account numbers.
Sources: Blue Sense Digital, Why Most Fashion Brands Are Running Paid Media Wrong, 2026-05-25
Last touched: 2026-08-18

## Standard shopping and Google account structure

### GP-021 · Two standard shopping structures are worth running, both gated on catalogue size: a top-sellers versus everything-else Pareto split, and automated performance-tier labelizer scripts above roughly a thousand SKUs.
Tier: T3 · Status: active
The Pareto split puts top sellers in one standard shopping campaign and everything else in a second, forcing 80% of spend into the top 20% of products while preserving a testing lane that new winners can be promoted out of. Explicit exclusions: do not run it in fashion, and do not run it on a 5-10 product business, because neither has the SKU spread to justify the segmentation cost. The labelizer approach tiers products into over-index / index / near-index / under-index / no-index on 30-day rolling performance, either manually via custom labels or via a script that reshuffles products between ad groups or campaigns in real time with tier-appropriate budgets and bidding. He recommends against the labelizer for most businesses on the same consolidation-beats-segmentation grounds in GP-022, and says it only earns its complexity at thousands of SKUs. ASSERTED, no test data shown.
Sources: Blue Sense Digital, The Only Google Ads Strategy You Need for 2026, 2026-06-22
Last touched: 2026-08-18

### GP-022 · Google campaigns learn in isolation, so campaign count should follow spend: 2 campaigns at $10k/month, 3-5 maximum under $50k/month, and fewer is usually better even at $1M/month.
Tier: T3 · Status: active
Google-specific extension of the cross-platform consolidation principle at [[Scaling Models|SC-014]]. The mechanism with numbers: a campaign holding 10 conversions per 30 days is modelling real-time bids off the psychographic data of 10 users. Merging three siloed campaigns holding 50, 20 and 10 conversions into one 90-conversion campaign raises ROAS purely through data density. The observable pattern in a segmented account is a monotonic relationship between conversion volume and ROAS down the campaign list, which he reads as causal. He acknowledges minor platform-level data sharing exists and says to ignore it when modelling the decision. The default target is one campaign, with every additional campaign carrying heavy justification (GP-023). Escape hatch: portfolio bidding strategies let segmented campaigns pool learnings. ASSERTED, no shown test.
Sources: Blue Sense Digital, Why Most Fashion Brands Are Running Paid Media Wrong, 2026-05-25; Blue Sense Digital, The Only Google Ads Strategy You Need for 2026, 2026-06-22
Last touched: 2026-08-18

### GP-023 · Only four justifications override the consolidation rule in a Google account: brand versus non-brand, geography, different margin or efficiency goals, and genuinely distinct product categories.
Tier: T3 · Status: active
The margin justification is the one most accounts get wrong, and it has a hard mechanism: Google cannot see your margin profile in a standard setup, so a shared 300% tROAS across a 70% gross margin collection and a 35% gross margin collection sends spend wherever revenue is highest, which can be the barely-profitable line. The category justification is about learning contamination, with office chairs versus plants as the extreme case: they share a buyer context and train toward different personas. Geography should always split at campaign level for multi-country selling. Commercial realities also justify campaigns that will knowingly underperform: grade C inventory you need to move, new arrivals you need surfaced for seasonality, dynamic best-seller versus zombie-product campaigns. That is why an agency needs inventory-level business knowledge before restructuring. The test he applies is whether you can steelman the reason a campaign exists. ASSERTED, no data shown.
Sources: Blue Sense Digital, The Only Google Ads Strategy You Need for 2026, 2026-06-22
Last touched: 2026-08-18

