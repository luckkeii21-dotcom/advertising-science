---
title: "Meta Delivery & Andromeda"
type: codex-topic
claim_prefix: MD
created: 2026-08-18
tags: [advertising-science, codex]
---

# Meta Delivery & Andromeda

How Meta decides who sees an ad: the multi-stage retrieval and ranking machine (Andromeda), the GEM foundation model, and why creative became the targeting input.

Part of the [[00-Codex|Advertising Science Codex]]. Claims follow the tier system (T1 docs, T2 shown test, T3 practitioner, T4 theory).

## Claims

## Creative Is the Targeting (Andromeda Era)

### MD-001 · Meta now targets by reading the creative itself, so the avatar callout in the ad decides who sees it
Tier: T3 · Status: active
Multiple independent sources converge on the same mechanism: Meta scans the video transcript, visuals, and text of each creative and routes delivery to the matching people, so the creative maker, not the media buyer, controls who sees the ad. Fraser Cottrell reports that mentioning a specific scenario or objection in the script routes delivery to the matching audience. Sam Piliero cites a supplement brand that sold for $1B running distinct avatar angles ("Lose weight, not your metabolism", "2025 with better poops") in one broad account, and says without avatar callouts "Andromeda does not know how to deliver your ads appropriately". Matt Shiver operationalizes it: the avatar callout must appear in the image, the primary text, and the landing page, and the results column completes the loop. Consistent with Meta's documented content-based retrieval (MD-022, MD-025).
Andrew Faris supplies a candidate mechanism: when an ad is served, Meta watches who engages, then finds more users like those engagers and serves them the same ad, which amounts to a lookalike audience built in real time per creative. His read of Meta's own statements plus what he can observe, no test. Faris also reports the scaling consequence in live client accounts, that narrowing the creative message no longer costs reach efficiency the way it used to, so his agency now writes deliberately narrow ads. His illustration is a feed serving Little League drills specific to four, five and six year olds rather than nine and ten year olds, a materially different coaching problem.
Jeremy Haynes states the same principle harder, that ad-set-level targeting is an "archaic, outdated belief" because messaging controls targeting, then uses it to justify dumping every interest, behaviour and demographic trait into one giant ad set. Charley T flags the internal contradiction on camera: if messaging does the targeting, the interest and lookalike ad sets have no job to do.
Sources: Fraser Cottrell, How to Make Meta Ads So Good People Can't Stop Watching, 2026-08-16; Sam Piliero, The Only Facebook Ads Video You Need in 2026, 2026-07-26; Dr. Matt Shiver, How the Facebook Ads Algorithm Actually Works, 2026-07-21; Andrew Faris, The 3-Part Creative Diversity Framework I Use To Scale Past $10M On Meta Ads, 2026-05-01 and Ezra Firestone: Nothing Has Changed In Ecom In 20 Years, 2026-05-15; Professor Charley T, Meta Ads expert reacts to $1M/month Strategy, 2026-02-14
Last touched: 2026-08-19

### MD-002 · Meta targeting is vector-embedding based: broad delivery sprinkles spend across the space, then hones into converting clusters
Tier: T2 · Status: active
Interactions no longer apply interest labels; each one nudges the user's position in a tens-of-thousands-dimension embedding space where similar users cluster. Broad targeting seeds small spend across the space, observes who interacts and buys, and concentrates delivery on those clusters, which is why broad beats interest targeting on large datasets over long periods. Interest and lookalike targeting were deprecated in July 2025. Presenter states every mechanic is sourced to Meta's own engineering posts and help documentation. Two supporting points from the same speaker's earlier session, both weaker evidence: roughly 30% of the people inside any Meta interest group were assigned wrongly, because a label records interaction and not intent (comment "I hate dogs" and every dog advertiser targets you), which he sources in his own words as "Meta put out a report or someone put out a report", so treat it as argument rather than evidence. Second, the scaling consequence: spending more expands the targeted region outward from the converting hotspot into colder people who are not convinced, which is why campaigns degrade as budget rises.
Earliest statement of the same mechanism, from the same speaker in March 2025: each interaction bundle gets numeric values and pushes the user's coordinates, users who interact similarly cluster together, and that clustering is offered as the reason two friends see near-identical Reels feeds. He sizes the space at "hundreds if not thousands of axes"; the July 2026 statement says tens of thousands. The dimension count is unsettled inside one speaker's own material, so quote the mechanism and not the number.
The interest-group critique gains a date from a second speaker. Charley T states the Facebook engineering team that maintained interest-group technology was disbanded in 2018, so the classifier is frozen, and repeats the one-third-by-mistake figure in two separate sessions with "I hate cats" as the example that puts you in the cat interest group. The disbandment date carries no cited source. Layer the share who feel positive, then the share who would ever buy, then the share not already loyal to a competitor, and the usable fraction of any interest audience is small.
Signal set, per Andrew Faris quoting a public post: likes, comments, shares, saves, video watch time, in-app search on Facebook and Instagram, and web browsing on pixel sites, with the framing that Meta stopped building a social profile from age, gender, location and interest. The auto-transcript garbles the post author's name ("Alex Skryfeld" in one place, "Alex Gryffindor" in another), so verify the attribution before citing it. Faris says openly the system stays a black box.
Sources: Blue Sense Digital, How The Meta Ads Algorithm Works in 2026, 2026-07-28 and How To Structure A Meta Ads Account At Every Spend Tier In 2026, 2026-06-01 and How Machine Learning Works in Meta Ads (2025), 2025-03-25; Professor Charley T, Meta Ads expert reacts to $1M/month Strategy, 2026-02-14 and Do these 5 things each day to scale Facebook Ads, 2026-02-21; Andrew Faris, The 3-Part Creative Diversity Framework I Use To Scale Past $10M On Meta Ads, 2026-05-01
Last touched: 2026-08-19

### MD-003 · Post-Andromeda, near-duplicate ads collapse into one entity ID and share identical delivery with zero unique reach
Tier: T3 · Status: contested
Two independent sources agree on the core. Fraser Cottrell: brands posting 100 copies of the same ad with minor headline tweaks get those ads flagged as one entity and their results collapse; he flags this especially at $70-100k/month spend, while accounts already launching net-new diverse assets saw essentially no change. Blue Sense: ads judged the same are grouped under one entity ID and all serve to the same audience pool, so 200 similar ads can register as 20; diversity must be at the concept level (angle x offer x persona), and a sufficiently different format can register as a distinct ad even with the same concept. Fraser adds that animating a static into video is very unlikely to be tagged as the same entity because the media type differs.
Two extensions from Blue Sense. First, the metric exists: Meta will give you a creative similarity score, obtainable only by asking a dedicated Meta rep, where a higher number means more similar and therefore worse. Second, the bundling trigger is broader than visual duplication. The same campaign shoot with a different model pose, a UGC script with a mid-video variation, and even formally different videos that speak to the same audience all get bundled into one delivery pool, at which point frequency rises, reach falls and ROAS decays. The remedy is three creatives that address different people, which reach separate pools with little audience overlap.
CONTESTED, scoped to hook swaps. In an earlier transcript the same Blue Sense speaker states the opposite for hook variations: "Meta will still recognize a different hook as a different creative. It will get its own creative ID. It will not get pulled together with this asset. It will go and reach a novel unique audience." Evidence offered: rotating 50 new hooks onto a fatigued ad that had already spent $50-100k bought another $100k of spend at the same efficiency. He concedes partial overlap, since 87 of 90 seconds are unchanged and the concept is identical, and frames hook rotation as worth doing mainly because it is nearly free. Note the chronology: the hook-swap position is from 2026-05-11 and the near-duplicate-collapse position from 2026-07-28, so this may be the same speaker updating rather than a two-party disagreement. MD-043 offers a candidate reconciliation: differences the system can actually parse (media type, landing-page URL, a new 3-second opener) register as distinct, metadata tweaks like a headline swap do not.
Sources: Fraser Cottrell, How to Make Meta Ads So Good People Can't Stop Watching, 2026-08-16 and Creative Volume, 2026-08-02; Blue Sense Digital, How The Meta Ads Algorithm Works in 2026, 2026-07-28 and How to Scale an eCommerce Brand Profitably in 2026: The Full System, 2026-06-15 and Meta Ads Creative Strategy in 2026: The Full System, 2026-05-11
Last touched: 2026-08-18

### MD-004 · Update timeline: Lattice 2023, sequence learning Nov 2024, Andromeda Dec 2024, GEM multimodal grouping, adaptive ranking 2026
Tier: T2 · Status: active
Sequence learning (Nov 2024) optimizes which sequence of your ads a user sees across the purchase journey, which killed single-ad-per-ad-set structures. Andromeda (Dec 2024) is a retrieval-stage change that reads creative content itself. GEM, commonly conflated with Andromeda, gave the system multimodal ability (watch video, listen to audio) to group creatives by format and representation, making creative diversity mandatory. The 2026 adaptive ranking model allocates compute per impression and sped up time-to-relevancy; Meta claims a 3% platform-wide conversion lift and 5% CTR lift from it. Named, dated updates cited from Meta engineering posts.
Sources: Blue Sense Digital, How The Meta Ads Algorithm Works in 2026, 2026-07-28
Last touched: 2026-08-18

### MD-005 · Andromeda scores every ad on two dimensions: efficiency versus account peers AND scalability, not efficiency alone
Tier: T3 · Status: active
Meta evaluates (1) can this ad hit the account's efficiency target better than its peers and (2) can this ad actually absorb spend. This explains why some ads post very high ROAS but only get a few dollars of delivery, and why forcing spend onto them tanks results. It also explains the scaling wall: an account can sustain $100, $500, $1,000 or $5,000/day, but a jump from 100 to 200 or 1,000 to 1,200 can degrade ROAS below the lower-budget level. Speaker claims $500M lifetime and $100M managed in the Andromeda era.
Sources: Sam Piliero, Do THIS and the Meta Andromeda Algorithm Will LOVE You!, 2026-08-14
Last touched: 2026-08-18

### MD-041 · iOS 14 removed roughly 30% of Meta's targeting signal, which forced delivery off interest labels and onto creative-based broad
Tier: T3 · Status: contested
Interest grouping was built substantially on off-site pixel data from third-party browsing. ATT removed that data, and Meta had to compensate by rebuilding both retrieval and user ranking around on-platform behaviour plus the content of the creative itself. The speaker places this before Meta repurposed its metaverse Nvidia GPUs into ads inference, which produced Andromeda. This is the prequel to MD-004's update timeline and the historical reason consolidation became the preferred account structure. The 30% figure is ASSERTED with no source shown.
CONTESTED on what iOS 14 actually damaged. Charley T's flat counter: "Targeting has been obsolete since 2018. iOS 14 didn't impact targeting at all. iOS 14 was a bad week." His reading is that ATT destroyed businesses whose accounts were built in fragmented structures and left targeting untouched, because manual targeting had already stopped mattering three years earlier. He also compresses the platform's whole history to two substantial changes since 2018: the iOS 14 response, which he says removed delayed attribution and with it the 28-day window agencies used to claim credit for other channels' work, and Andromeda. Everything else he treats as surface.
Both sides are practitioner assertion with nothing shown, and Charley T's version is self-serving toward his own single-campaign method. Note also the shared ground: both agree the post-ATT correction was structural consolidation. What would resolve it is a pre-versus-post ATT comparison of interest-audience delivery quality on the same account, which neither speaker offers.
Sources: Blue Sense Digital, How To Structure A Meta Ads Account At Every Spend Tier In 2026, 2026-06-01; Professor Charley T, Mastering Andromeda: Creative Testing and Scaling, 2025-12-13 and How to Scale Facebook Ads in 2026, 2026-02-28
Last touched: 2026-08-19

### MD-042 · Audience memory lives in the Page, Instagram account, ad account and website; the pixel is a conduit that does not learn
Tier: T3 · Status: active
Refutes the "season your pixel" folklore. The pixel is "the paper a vote is written on", and the systems counting the votes are what learn: the Page learns who interacts with it, the Instagram account learns what content people engage with, the ad account learns who buys, the website holds its own history. Cited payoff: an operator pushing $4-6M/month has built multiple Facebook Pages, each with its own personality and audience profile, and runs ads from each so Meta can match distinct personas to distinct buyers. Also offered as the explanation for why two brands running near-identical creative get different outcomes. ASSERTED only, and weakly: a third-party account, spend level asserted, nothing shown. Two risks the source does not address. The multi-Page play carries the ban-wave and Business Manager exposure of MD-038, and it stacks against the per-Page live-ad cap in MD-066.
Sources: Professor Charley T, The NEW BEST Meta Ads Andromeda Course to Scale in 2026, 2026-01-24
Last touched: 2026-08-18

### MD-043 · Meta crawls the ad's landing page URL, and per one Meta rep that crawl alone differentiates delivery between two ads identical except for the URL
Tier: T3 · Status: contested
Brad Plock relays his Meta rep: the crawl exists for policy enforcement (the health-and-wellness tag), and delivery differentiation is a side effect. If true, this is the mechanism that makes duplicate-the-ad-and-swap-the-URL testing legitimate rather than a hack, and it gives MD-003 a reconciliation line: a URL change is a content difference the crawler can parse, a headline tweak is not. Account evidence offered: demographic delivery reallocated toward women 45-54, and an ad that had been getting zero spend became the second top spender. This is a relayed rep statement, not Meta documentation, so T3 and not T1. Brad concedes he cannot fully verify it, because a duplicate that does not spend is indistinguishable from an ad that was not good enough.
Counter-hypothesis from Andrew Faris in the same conversation: Meta forecasts delivery off upper-funnel engagement signals (video view length, clicks, shares) which are identical across two ads sharing one creative, and landing-page conversion data arrives too slowly to inform delivery, so the two ads should deliver near-identically. Reasoning only, no test run. This is the reason most media buyers reach for a split test instead. Resolving test: run a URL-swap duplicate and check whether the demographic delivery breakdown diverges from the original inside the first week.
Sources: Andrew Faris (with Brad Plock), The Right Way To Test Landing Pages On Meta Ads In 2026, 2026-06-22
Last touched: 2026-08-18

### MD-070 · A creative asset carries its learned performance across campaigns, and changing the headline or primary text changes it
Tier: T3 · Status: active
Charley T says a video or static keeps the performance it has learned no matter which campaign it is placed into, so re-uploading a proven asset elsewhere does not restart it from zero. Changing the headline or the primary text attached to it does change the performance. Two operator consequences follow. A winner that fails in a new ad set is more likely losing to the ad next to it than decaying on its own, so check the neighbours before killing it. And a copy-only refresh on a proven asset is a change to that asset's delivery, not a free test. Sits in tension with MD-003, which reports that metadata tweaks like a headline swap do not register as a distinct entity. Both can hold only if a headline swap changes how an existing asset is scored without making it a new entity. Asserted, no data shown.
Sources: Professor Charley T, Q5: the 2nd Black Friday: Meta Ads for Profit, 2025-12-20
Last touched: 2026-08-19

### MD-071 · Andromeda did not change the rules, it raised the price of a messy account
Tier: T3 · Status: contested
Charley T's one-line version: "Andromeda at a very simple level, Andromeda meant that doing a bad job hurt you more." The named patterns that got more expensive are five different offers inside one account, twenty new ads launched per week, and multiple landing pages and angles running at once. His framing is that before Andromeda you could brute-force outcomes with more ads, more audiences and more effort and outrun bad habits, and that the update amplifies those same mistakes instead of introducing new rules.
CONTESTED, with thin evidence on both sides. His supporting case is a single counter-anecdote: an interviewee whose cost per lead fell $2 while Andromeda arrived unnoticed and Reddit filled with $100k-a-month stores reporting collapse. Against it stands the larger set of practitioners reporting Andromeda-era collapses on accounts with unchanged creative, budget, offer and structure, which is the premise of MD-003 and the July 2025 cliff in MD-072. No controlled comparison exists either way, and the position is self-serving toward his own single-campaign method. Resolving test: an account-level before-and-after on structure complexity held against a matched control, which nobody has run.
Sources: Professor Charley T, Q5: the 2nd Black Friday: Meta Ads for Profit, 2025-12-20 and How to Scale Facebook Ads in 2026, 2026-02-28 and If you run Facebook Ads... everything just changed., 2025-12-06
Last touched: 2026-08-19

### MD-072 · Andromeda rollout chronology: isolated testing Nov-Dec 2024, a handful of accounts April 2025, roughly half by July 2025, with performance sliding March to June and breaking in July
Tier: T3 · Status: active
Two speakers give a compatible chronology and neither cites Meta documentation. Jeremy Haynes: isolated testing in November and December 2024, rollout to a handful of accounts in April 2025, "ripping across about half the accounts" by July 2025, and effectively universal by February 2026. Charley T describes the matching curve from the advertiser's side: gradual weekly decay from March through May, then a cliff in July where costs jumped and lead volume slowed with no change to creative, budget or offer. The dates line up with MD-004's Andromeda ship date of December 2024 and with the July 2025 interest and lookalike deprecation in MD-002. Use it as a calendar marker when reading 2025 account history. A step change in July 2025 has at least three candidate causes stacked on it, so do not attribute it to your own changes without checking.
Sources: Professor Charley T, Meta Ads expert reacts to $1M/month Strategy, 2026-02-14 and If you run Facebook Ads... everything just changed., 2025-12-06
Last touched: 2026-08-19

## Delivery Dynamics: Sequencing, Displacement, Funnel Position

### MD-006 · New ads launch with zero data, so Meta serves them to the warmest audience first, temporarily degrading existing ads
Tier: T3 · Status: active
A new ad has zero history, so Meta gives it the best possible audience (warm, engaged users) to build signal fast. While that happens, existing ads lose access to that warm audience and their performance immediately looks worse. What operators read as ad fatigue is usually this displacement effect, and killing the "dying" ads then concentrating spend lower in the funnel is the doom cycle that stops accounts scaling. Claimed from over $1B in managed spend.
Two consequences the same speaker draws elsewhere. A launch-constantly habit manufactures great ROAS on an account whose budget can never be raised: the first-days spike is delivery into the least incremental pocket, and because no up-funnel learning gets banked, every budget increase then breaks performance. Practical test: if raising budget reliably tanks results in an account that launches ads weekly, check this first. Second, test-campaign winners fail on graduation, because the winner was measured under a load and audience mix that no longer exists once it moves into the scaling campaign and has to do a different job. His analogy is hiring someone to make one shoe a day perfectly and being surprised they cannot make 30. This is also the mechanism behind the common "ad dies after three days" complaint. Reasoning only, nothing shown.
Generalised: every piece of content, paid or organic, is first validated against users the model already predicts well, and their response decides how widely it gets served. The same speaker says this is how every organic and paid platform operates. The reporting consequence is the one operators miss: heavy launch volume systematically over-represents engaged audiences and existing customers in the breakdown data, which then gets misread as a targeting problem rather than a launch-cadence problem. MD-081 records the contested version of what this does to fatigue.
Sources: Professor Charley T, Copy This Simple Meta Ads Strategy, 2026-08-10 and The BEST Facebook Ads Strategy for 2026 Post Andromeda, 2025-12-27 and Meta advertisers: We've got a big problem, 2026-01-17 and Facebook Ads in 2026: NEW Secrets, Tips & Strategies, 2026-04-15
Last touched: 2026-08-19

### MD-007 · Every post, paid or organic, carries an estimated action rate score; higher score means cheaper impressions, and every new ad starts at zero
Tier: T3 · Status: active
Meta scores every piece of content on how likely each person is to engage, click, and take the actions the advertiser cares about. Higher score means more reach and lower cost per impression; lower score means more expensive impressions. Because a new ad starts at zero, the system routes it to the best data source (warm bottom-funnel users) first, which is the root mechanism behind MD-006.
Sources: Professor Charley T, Copy This Simple Meta Ads Strategy, 2026-08-10
Last touched: 2026-08-18

### MD-008 · Early-life frequency reveals learning: frequency 1.6 in the first days means 60% saw it twice in one day; frequency falling as spend rises means the ad is moving up-funnel, not dying
Tier: T3 · Status: active
During learning, Meta reaches the same warm people repeatedly (frequency 1.6 = 60% saw it twice in a single day, 1.2 = 20%). As learning ends, spend goes up and frequency goes down because the ad starts reaching genuinely new people for the first time. The apparent performance drop after a few days is the ad graduating to colder audiences.
Read frequency broken down BY DAY and it becomes a permanent funnel-position diagnostic with thresholds at both ends: 1.05 means 5% saw the ad twice today, so 95% of that ad's spend is prospecting; 1.95 means 95% saw it twice today, so the ad is almost entirely retargeting. The consequential half is the decoupling of audience setting from delivery reality. A retargeting ad set can read 1.05 while a worldwide no-exclusion audience reads 1.9, because the creative does the targeting. Two operator corrections follow. Stop treating a frequency above 3 as a fatigue alarm without naming the window ("three over what? Three per day, three per week, three per month"). And stop assuming a retargeting ad set is doing retargeting work. He grounds high frequency as desirable through the frequency-illusion sequence: frequency bias at 3-5 impressions, selection bias at 5-10, confirmation bias well past 12, making 12+ exposures the familiarity target rather than a warning.
One more pairing seen repeatedly in post-Andromeda reads: frequency climbing while CPM does NOT climb to match means the machine found a small pocket of people who love the ad. That is a high-quality experience delivered to a tiny audience, fine as a bottom-of-funnel closer and useless as a scaling asset. Fix which part of the funnel the ad is used for rather than band-aiding the number.
Sources: Professor Charley T, Copy This Simple Meta Ads Strategy, 2026-08-10 and The NEW BEST Meta Ads Andromeda Course to Scale in 2026, 2026-01-24 and Record Profits: the Meta Ads Andromeda Playbook, 2026-01-03
Last touched: 2026-08-18

### MD-009 · Personalization on Meta is a delivery-sequence problem: the system needs a small number of distinct ads with clear jobs, not more ads
Tier: T3 · Status: active
Citing Meta CMO Alex Schultz, personalization means the sequence of messaging a user experiences across the feed, not a different ad per person. Meta needs to know which message works for which person in what order; account complexity makes that matching harder and every impression more expensive. A small set of distinct ads each doing a specific job lets Andromeda sequence messages with confidence instead of guessing across dozens of variables.
The combinatorial argument underneath it, and the arithmetic checks out: 20 ads have 20! possible delivery orderings, which is 2.43e18. At one combination per second the machine would need about 77 billion years to try each once. So 20 ads do not create 20 chances to win, they remove the system's ability to learn any journey, at which point Meta collapses spend into the single ad it has most confidence in and the operator blames Meta. Adding ads multiplies the sequence space factorially, not linearly. Pure reasoning, nothing shown.
Same speaker on the launch-volume consensus, and it is a direct inversion of the "feed the beast" advice: he argues Andromeda was built to contain the damage from creative spam, and that a system better at routing the right ad to the right person needs fewer ads, not more. He still wants creative diversity, delivered as distinct formats reinforcing one message, and pushed into organic and engagement campaigns rather than into the conversion campaign. This sits directly against MD-003's remedy of concept-level creative diversity at volume, and against Faris's volume argument in MD-081. Asserted, no documentation cited.
The pricing symptom, diagnosed on a new brand with clean compliance and high CPMs: many ads launched at once across multiple angles and multiple landing pages leave delivery with no consistent signal about who responds or why, and the system prices the account as a liability. His fix is to test two options on one variable, pick the winner, route 90% of traffic there, then add the next thing. Asserted, no data shown.
Sources: Professor Charley T, Copy This Simple Meta Ads Strategy, 2026-08-10 and Meta advertisers: We've got a big problem, 2026-01-17 and Facebook Ads in 2026: NEW Secrets, Tips & Strategies, 2026-04-15 and How to Scale Facebook Ads in 2026, 2026-02-28
Last touched: 2026-08-19

### MD-010 · Inside a CBO, spend distributes as an inverted funnel: high-spend ads run higher CPA (top-of-funnel), low-spend ads show cheap CPA (bottom-of-funnel closers)
Tier: T3 · Status: active
Two independent sources describe the same distribution. Matt Shiver: one ad takes 75-90% of ad-set spend at a modest 1-2x ROAS while the 5-10%-spend ads show 2-4x, because Meta sequences them as TOF then MOF/BOF to the same people; killing the 90%-spend "underperformer" can drop the whole ad set from ~3x to ~1x, and the former 2-4x ads to 0.5-1x because they cannot source cold traffic alone. Nick Theriot: the ads taking the most spend typically carry the highest CPA as demand drivers, which is why the top spenders' CPA becomes the benchmark ceiling and cheap-CPA low-spend ads should never be read as "better" ads.
A third-party account of making the mistake, given as his single largest error: Meta had learned a working sequence with one ad prospecting and another closing, the prospecting ad looked like a loser on the per-ad conversion metrics he had been taught, so he turned it off. That cut the inflow, forced the closers to prospect, and restarted the algorithm's search. Mechanism claim from practice, no data shown.
Sources: Dr. Matt Shiver, How the Facebook Ads Algorithm Actually Works, 2026-07-21; Nick Theriot, When to Turn Facebook Ads Off in 2026, 2026-08-07; Professor Charley T, How to Scale Facebook Ads in 2026, 2026-02-28
Last touched: 2026-08-19

### MD-011 · Once the structure works and targets are beaten, stop tweaking; mid-scale strategy changes are the biggest self-inflicted wound
Tier: T3 · Status: active
Operators who reach a working creative engine above target then add bid caps, cost caps, new campaigns and structures from an "itching sensation", which resets what the algorithm has learned. The correct inputs to keep feeding: highest-quality creative at scale, offers, landing pages, and product quality, with permanent levers (spend minimums/maximums, value rules) held ready for break events like stockouts.
Sources: Sam Piliero, Do THIS and the Meta Andromeda Algorithm Will LOVE You!, 2026-08-14
Last touched: 2026-08-18

### MD-012 · The last 7 days of every quarter dip because large brands surge spend to exhaust quarterly budgets, and mid-January dips after Black Friday and Q5
Tier: T3 · Status: active
End-of-quarter auction pressure from big advertisers finishing quarterly budgets predictably degrades performance in the final 7 days of each quarter, stacking with calendar events (Father's Day, July 4th, Prime Week) that shift buyer attention. Response: lower spend slightly, keep testing, scale back up after; no structural changes. He publishes this forecast to students months ahead.
Mid-January is the second predictable trough, arriving after Black Friday, Cyber Monday and Q5. Charley T's point is the misattribution: operators read the calendar-driven drop as fatigue, a platform bug, or the result of their own changes, and then make destructive changes on top of it. In January 2026 a real Meta bug landed inside the expected trough and made the misattribution worse. He claims simple accounts bounce back between the Wednesday and Thursday of that week. Operating rule: hold structure, judge January against last January and never against December. Asserted, no data.
Early February is the third named trough. Charley T told a viewer whose results deteriorated in February that the dip was flagged to his community nine months in advance, and several viewers in the live chat confirmed the same February decline. He never explains the mechanism behind it. The operating point is the same as the other two: a share of month-to-month swing is calendar, so a planned response beats a reactive account change. Asserted, no data.
Sources: Nick Theriot, Simple Creative Testing Framework I Use To Scale Facebook Ads In 2026, 2026-08-12; Professor Charley T, Meta advertisers: We've got a big problem, 2026-01-17 and Do these 5 things each day to scale Facebook Ads, 2026-02-21
Last touched: 2026-08-19

### MD-044 · Meta allocates on incremental return at the margin, so the placement or ad with the lower reported ROAS usually deserves the budget it is getting
Tier: T3 · Status: active
The breakdown report shows average return; Meta buys on the next dollar. Worked example: Stories reports 4x and Feed reports 3x while Feed holds 80% of spend, because another $20/day into Stories returns nothing incremental while the same dollars into Feed still return about 2x at the margin. The same logic explains an ad at 1.7x taking more budget than a 2.2x sibling. Operator action: do not restructure or launch dedicated campaigns to force spend into the higher-ROAS breakdown segment unless you are a genuinely expert buyer, because the segmentation that breakdown data invites is usually commercially misaligned and loses performance. He states the principle does not weaken at high spend. He attributes the breakdown effect to Meta's own public documentation but does not show it, so treat the attribution as unverified.
Sources: Blue Sense Digital, How to Scale an eCommerce Brand Profitably in 2026: The Full System, 2026-06-15 and How To Structure A Meta Ads Account At Every Spend Tier In 2026, 2026-06-01
Last touched: 2026-08-18

### MD-045 · ROAS reliability rises up the account hierarchy: ad-level is close to meaningless, ad-set is trustworthy, campaign-level 7-day-click with existing customers excluded is congruent with the P&L
Tier: T3 · Status: active
The cause is sequencing plus last-click reporting. Meta optimises across multi-click and view chains but credits only the final click, so a top-of-funnel opener can show 1.4x while the closer shows 6x inside the same ad set. Some cross-ad-set serving also happens, since the algorithm prioritises adjacent ads within an ad set without confining itself to them, which is why one ad set can absorb credit generated by another. Operating rule: make kill and scale decisions at ad-set and campaign level, and read the ad level for diagnostics only. MD-010 describes the same phenomenon inside a CBO at ad level; this states it as a reliability gradient with a specific settings condition (7-day click, existing customers excluded). Asserted from agency experience, nothing shown.
Charley T names the same phenomenon as the real cost of fragmented structures and separates it from the thing operators usually worry about. He states flatly that "audience overlap doesn't matter", meaning duplicate impressions across ad sets are not the problem, then attacks isolated one-ad-set campaigns for exactly this: they compete for last-touch credit without sharing data. His position is internally in tension, since he warns against a structure that guarantees the overlap he says is harmless, and it is a bare assertion with nothing shown. The usable part is the distinction: overlap is a delivery non-event, credit cannibalisation between isolated entities is a measurement failure that then drives wrong kill decisions.
Sources: Blue Sense Digital, How to Scale an eCommerce Brand Profitably in 2026: The Full System, 2026-06-15; Professor Charley T, Meta Ads expert reacts to $1M/month Strategy, 2026-02-14
Last touched: 2026-08-19

### MD-046 · Live audit of an 89-ad campaign: 14 winners and the losing 75% of ads consumed the same 34% of budget, at $138 CPA and +$69 gross profit per transaction versus $230 CPA and -$0.98
Tier: T2 · Status: active
SHOWN: filtered and sorted live in Ads Manager, with column totals read out loud because Meta does not display them. Winners were 14 ads, 16% of the ad count: $48,594 spend (about 34% of budget), CPA $138 (17% below the campaign average), gross profit per transaction $69 (nearly 2x the $36.17 campaign average), over 40% of purchases and over 40% of revenue. Losers were 75% of the ad count: $48,800 spend, just $300 more than the winners, CPA over $230 (39% worse), GPT negative $0.98, under 25% of sales and under 22% of revenue. The symmetry is the finding. The account spent half its money losing money on every transaction it bought. He is explicit that the goal of the audit is not to switch everything bad off, it is to see where spend should go. GPT is a custom Ads Manager metric, average purchase conversion value minus cost per purchase.
Sources: Professor Charley T, The NEW BEST Meta Ads Andromeda Course to Scale in 2026, 2026-01-24 (account audit shown)
Last touched: 2026-08-18

### MD-047 · The 4PI read (spend, frequency, CPM, cost per result) classifies an ad's funnel position: high spend, low frequency, low CPM and a bad CPR is top-of-funnel; the inverse is bottom-of-funnel
Tier: T3 · Status: active
All four metrics are outputs, not controls. Spend is a KPI: where Meta chooses to spend is the machine naming the ad it wants to invest in, so a spend drop is feedback and not punishment. Frequency tells you who the ad is being shown to. CPM tells you how much strangers like it, with one corrective, a high CPM can mean many advertisers are bidding for that specific person rather than that the creative is weak. Cost per result measures only how much last-touch credit that ad should take, because "not every ad is supposed to make a sale". The named failure mode it diagnoses is pushing as much spend as possible at the bottom of the funnel. MD-008 and MD-010 hold pieces of this; the composite read is the contribution. Asserted, nothing shown.
Worked case for the top-of-funnel corner of the read: a new ad set takes all the budget away from a converting one, at very cheap CPMs, and returns nothing. The cheap CPM is the tell that delivery placed it high in the funnel, which is exactly where results should be poor. His prescription is blunt, since nothing obliges you to fund an ad set that loses money, so turn it off. The general principle is that CPM level reads as funnel position and not as efficiency.
Sources: Professor Charley T, The NEW BEST Meta Ads Andromeda Course to Scale in 2026, 2026-01-24 and Record Profits: the Meta Ads Andromeda Playbook, 2026-01-03 and Mastering Andromeda: Creative Testing and Scaling, 2025-12-13
Last touched: 2026-08-19

### MD-048 · High-AOV, low-conversion-volume accounts should not run CBO, because with too few purchases the algorithm allocates on CTR, CPC and hold rate, which correlate weakly with return
Tier: T3 · Status: active
The illustrative account has a $10,000 AOV and does about $50k/day on roughly five orders, nowhere near enough purchase signal for CBO to allocate on purchases, so allocation moves upstream to pre-intent proxies. He states the underlying finding directly: across very large datasets CPC has almost no relationship to return except at the extremity of the bounds. Operator action: at low daily purchase counts, set budgets at ad-set level instead of handing allocation to CBO. A specific, testable boundary condition on CBO usage. Asserted from agency datasets, nothing shown.
The general form of the warning, from Charley T: Meta buys and optimises impressions, so it is an optimised CPM environment and per-click heuristics imported from search auctions mislead. Use it as the reason to distrust CPC-shaped reasoning on Meta rather than as a finding in itself.
Sources: Blue Sense Digital, How to Scale an eCommerce Brand Profitably in 2026: The Full System, 2026-06-15; Professor Charley T, Do these 5 things each day to scale Facebook Ads, 2026-02-21
Last touched: 2026-08-19

### MD-049 · On the New Balance account, a large majority of prospecting first impressions went to people who had abandoned cart at a competitor in the previous seven days
Tier: T3 · Status: active
Competitors named: Nike, Reebok, Converse, Puma, Adidas. Measured while scaling the account toward younger buyers. The transcript renders the share as "23 of our first impressions", almost certainly a mangling of "two thirds", so the exact figure is unverified and only the direction is the claim. If broadly true, prospecting delivery for a large brand is functionally competitor-retargeting, which changes what cold traffic means and supports a warm-first approach at small budget. No screenshot and no measurement method given, and Meta does not natively report competitor cart abandonment, so the data source is unexplained. Bank with the uncertainty attached.
Sources: Professor Charley T (joint session with Ben Heath), How to CRUSH Facebook Ads with a Low Budget, 2026-02-28
Last touched: 2026-08-18

### MD-050 · Advantage+ reportedly serves on product-level purchase intent, so every reseller stocking the same product gets served to the same in-market shopper
Tier: T3 · Status: active
ASSERTED mechanism, no data. The observation given: browse a Nike product and every reseller carrying it retargets you. If accurate, this is MD-002's embedding-space delivery operating at SKU level, and it means a reseller's ad performance is partly inherited from the parent brand's advertising rather than earned. Two cautions. The source is a February 2025 webinar whose account-structure sections the speaker himself time-boxed, so treat it as a hypothesis to validate rather than a current documented mechanism.
Sources: Blue Sense Digital, How To Structure Your Meta Ads for Profit (live webinar), 2025-02-19
Last touched: 2026-08-18

### MD-067 · Spend concentrating onto one to three ads out of 25-30 is expected delivery behaviour, and it reads early-impression user-experience confidence rather than business value
Tier: T3 · Status: active
Jeremy Haynes reports the distribution as reliable: launch 25 to 30 ads in one ad set and expect 27 to 29 to get little or no reach, spending pennies or at best dollars, while one to three take essentially all the distribution. He calls those one to three the winners, and names "every creative deserves distribution" as the belief that most damages accounts under Andromeda, because holding it drives operators to duplicate an ad set 25 to 30 times with one ad in each to force delivery.
Charley T accepts the delivery observation and rejects the label. His account of what concentration means: the ad got early spend because something in its first few impressions signalled that end users wanted to see it, weighted against metadata from the site, landing page, customer journey and social accounts. That is a user-experience judgement, not a verdict on business impact, and the delivery system is not answering the second question. "It's not saying that's the good ad. It's not saying that's the bad ad. It's the ad that gave the most highest quality with highest confidence end user experience."
Operator instruction from the same speaker: concentration is not a sign the ad set is broken and does not warrant forcing even distribution or restarting it. The job splits in two, support the consolidation and remove anything in the ad set that is a liability to it. All three positions are asserted with no spend or CPA figures shown. MD-010 gives the funnel-position reading of the same distribution and MD-047 gives the rule that a spend allocation is feedback rather than punishment.
Sources: Professor Charley T, Meta Ads expert reacts to $1M/month Strategy, 2026-02-14 and Mastering Andromeda: Creative Testing and Scaling, 2025-12-13
Last touched: 2026-08-19

### MD-074 · Andromeda is claimed to optimise for incremental lift rather than last click, so chasing reported ROAS trains delivery to re-serve existing buyers
Tier: T4 · Status: active
Charley T's framing hypothesis for the 2025 decline: Meta did not change what it wants, it changed how hard it penalises the wrong inputs, moving from optimising the last touch to optimising for the person who would not have bought without the ads. The corollary is the part with teeth. Optimising to attributed return signals that the cheapest converters are the goal, delivery concentrates on people already primed to buy, total transaction volume stops rising while spend does, and cost climbs. He uses it to explain why agency habits built around ROAS stall accounts.
Asserted, no data shown, and no Meta documentation supports an objective-function change of this kind. Treat it as a framing hypothesis until a lift test confirms it. Note the size difference against MD-034, which describes a reporting column trained on competitor lift studies. This claim describes a change to the delivery objective itself, which is a far larger claim with far less behind it. MD-020 holds the shipped product surface, new-customers versus all-customers delivery, which is the closest documented thing to it.
Sources: Professor Charley T, If you run Facebook Ads... everything just changed., 2025-12-06
Last touched: 2026-08-19

### MD-075 · Cold, warm and hot ad set separation stopped producing funnel-stage delivery, and the model it comes from predates CBO and broad
Tier: T3 · Status: active
Charley T dates the obsolescence twice and states it flatly both times: interest targeting has had no value since 2018, and cold/warm/hot campaign separation stopped working the same year. His historical argument is that funnel-stage segmentation dates to the EdgeRank era, before CBO, broad targeting and the Power 5, that the case studies behind it were disproven in 2017, and that he helped write the Power 5. Asserted, no data shown, and the self-citation is unverifiable.
The mechanism is banked elsewhere and it is the stronger half. Warm audiences entered in the suggested-audience field are inputs and not constraints (MD-013), any cold user who engages becomes warm inside the same campaign (MD-052), and Ben Heath reports the new/engaged/existing spend split coming out identical across a retargeting ad set and a cold ad set (MD-052). Operator consequence: build ad sets around what you can actually constrain, which is location, minimum age, language and exclusions, and let the creative carry the funnel-stage work, because the ad set label does not survive contact with delivery. MD-018 is the surviving exception, since conversion-optimised retargeting with warm audiences as suggestions is a delivery-order preference rather than a funnel-stage wall.
Sources: Professor Charley T, If you run Facebook Ads... everything just changed., 2025-12-06 and Facebook Ads in 2026: NEW Secrets, Tips & Strategies, 2026-04-15
Last touched: 2026-08-19

### MD-077 · Your own feed is the worst possible sample of your own ads, so stop diagnosing delivery from it
Tier: T4 · Status: active
The advertiser is the single most engaged non-converter in their own account. They have clicked every ad and visited the site repeatedly without firing the conversion event, so delivery is scraping the bottom of its option set to find anything they might respond to, and they see ads 99.9% of people never see. Charley T's check when someone complains their flexible ads render as ugly carousels: ask how often you see carousels from other brands running the same widely used format. The operating rule is that a personal-feed observation is not evidence about delivery, creative quality, or format rendering, and every diagnosis has to come from account data. Reasoning only, no data shown. Pairs with MD-064 on flexible-ad carousel rendering and MD-016 on placement complaints.
Sources: Professor Charley T, Do these 5 things each day to scale Facebook Ads, 2026-02-21
Last touched: 2026-08-19

### MD-080 · Never compare two ad sets at different spend levels, because the lower-spend one reads better on CPM and enters lower in the funnel
Tier: T3 · Status: active
Live audit case. A clothing client ran two broad catalog ad sets that differed only in primary text, and the newer one looked like the winner. Charley T attributes the whole gap to spend level rather than copy: less spend buys a lower CPM, and a new ad initially serves lower in the funnel where conversions are cheapest, so its cost per purchase arrives flattered. AOVs were $269 and $298, which he does not treat as a material difference. His resolution converts a confounded comparison into a real one, duplicate the newer primary text into the ad set that has already spent $24,000 and check whether the $300 AOV holds there. Numbers were on screen in the audit; the causal attribution is his reading and not a test. This is the read-the-report form of MD-006's displacement mechanism and the same trap MD-047 names when spend level is treated as a verdict.
Sources: Professor Charley T, Copy this Meta Ad strategy to BLOW UP your business. (After Andromeda, Clothing Niche), 2026-01-31
Last touched: 2026-08-19

### MD-081 · Ad fatigue cause is contested: operator-manufactured versus Andromeda burning the reachable pool faster
Tier: T3 · Status: contested
Side one, Charley T: "99% of ad fatigue that isn't built around just you raised the budget too much too fast is because you launch a new ad." His mechanism is MD-006's displacement. New ads enter at the bottom of the user funnel because that is the machine's testing environment where it already knows how those people behave, they take last-touch credit at the eleventh hour from the ads already carrying spend without adding conversions, and the incumbents then look like they are decaying. He goes further and says that without constant ad set duplication and constant new-ad injection you would not see fatigue at all. The 99% is rhetorical and nothing is shown.
Side two, Andrew Faris: Meta has got materially better at putting the right ad in front of the right person faster, so an ad reaches its best audience sooner and exhausts it sooner. He calls this a feature with a cost attached, states explicitly it is not a media buying error and not a ghost in the machine, and uses it as the direct reason creative diversity and creative volume matter more now. The shape he reports: an ad going from $5,000/day to $15,000/day a day or two later, then $50,000/day, then back to $5,000, inside days. In apparel he saw ads rip for three or four weeks then fade, which he attributes to fast fashion demand cycles. Numbers given, no account, date range or performance metric attached.
The two make opposite prescriptions from the same symptom. Charley T says launch fewer ads and stop manufacturing the problem, which is MD-009's position. Faris says launch more, because the pool burns faster and volume is now mandatory, which is MD-003's position. A clean resolving test exists and neither has run it: hold launch cadence at zero on a mature account for four to six weeks and measure whether the incumbent winners still decay. If they do, displacement is not the whole story.
Sources: Professor Charley T, Meta Ads expert reacts to $1M/month Strategy, 2026-02-14 and Facebook Ads in 2026: NEW Secrets, Tips & Strategies, 2026-04-15; Andrew Faris, I've Managed Over 100 Meta Ads Accounts. Here's Why Yours Is Broken., 2026-05-27 and The 3-Part Creative Diversity Framework I Use To Scale Past $10M On Meta Ads, 2026-05-01
Last touched: 2026-08-19

## Reach, Frequency, and CPMR

### MD-051 · On cold campaigns, ad-level frequency almost never exceeds 2 over a 30-60 day pull; anything above that is a creative diversity and volume red flag
Tier: T3 · Status: active
The audit is concrete: pull the last 30 or 60 days at ad level, filter to cold campaigns, read frequency. He states that across every account his agency runs, no cold ad sits above a 2, and an exception is treated as a fix-now signal. Mechanism is MD-003: Andromeda bundles similar creatives into one delivery pool, which drives frequency up, reach down and ROAS down over time. The value is timing, this fires before ROAS decays. Always state the window alongside the number (MD-008), because a frequency of 3 means nothing until you say 3 per day, per week or per month. Asserted across the agency's book, nothing shown.
Sources: Blue Sense Digital, Meta Ads Creative Strategy in 2026: The Full System, 2026-05-11
Last touched: 2026-08-18

### MD-052 · Frequency on any ad is never 1.0, so every ad retargets somebody every day and the new/engaged/existing breakdown describes a moment rather than an addressable population
Tier: T4 · Status: active
Users cross the boundaries constantly: a new person engages, becomes an engaged audience, buys, becomes an existing customer, keeps engaging. So the reported segmentation cannot carry the weight of separate retargeting structures built on top of it. He still uses the audience definitions, for the opposite purpose: in a one-campaign setup the defined segments make Meta throttle delivery to already-converted users in the name of incrementality. Reasoning only, nothing shown. Sits in tension with MD-019, which treats the same breakdown as an allocation and budgeting tool, and takes the opposite operational turn from MD-057, which builds a retargeting ad set precisely because delivery ignores the segmentation. File as the counter-reading.
The strongest evidence for it comes from the other side of that dispute. Ben Heath reports from agency accounts that if you set up one ad set as retargeting and one as cold and then read the breakdown, the spend split across new, engaged and existing audiences "is exactly the same". That is a practitioner observation with no numbers shown, but it is offered by the speaker who argues the definitions do inform delivery, which makes it harder to dismiss. Charley T uses it as the reason the M3 funnel-stage method breaks, since M3 assumes the split differs by ad set. MD-075 carries the funnel-stage consequence.
Sources: Professor Charley T, The BEST Facebook Ads Strategy for 2026 Post Andromeda, 2025-12-27; Ben Heath (with Professor Charley T), Facebook Ads in 2026: NEW Secrets, Tips & Strategies, 2026-04-15
Last touched: 2026-08-19

### MD-053 · CPMR (cost per 1,000 unique accounts reached) equals CPM times frequency and ships as a default Ads Manager column; since CPM is market-set, frequency is the only lever
Tier: T3 · Status: active
It is a selectable column, not a custom metric. Because CPMR decomposes into CPM times frequency and CPM is largely a price the operator cannot move, every practical remedy is a frequency intervention: campaign consolidation, exclusions, placement expansion, creative diversity, and partnership ads. Partnership (whitelisted) ads get called out for a consistent CPM discount across a long period in Kiel's accounts, from a large volume of partners posting regularly, which flows straight into lower CPMR and wider reach; his explanation, which he flags as his own theory, is that Meta shifted platform favour from the shopping feed toward partnership ads and partnership content. CR-058 covers the creative-quality case for partnership ads, this is the delivery-cost case. Read CPMR as a leading signal alongside ROAS and CAC. Asserted, no dashboard shown.
Second independent source on the metric, and a stronger framing of what it is for. Charley T calls cost per 1,000 Accounts Center accounts the practical proxy for the cost of incrementality, because it prices reaching new individuals rather than impressions, and notes the platform does the CPM-times-frequency arithmetic for you. He splits the two inputs by what each reads: frequency reads how warm the audience is, CPM reads how premium or contested that audience is.
Mechanism for the partnership-ad discount, from Blue Sense, and it comes with an operating rule: a partnership ad lets Meta optimise using the creator page's data alongside the advertiser's, which is what makes it effective at reaching the right cold users. So the fee earns out on cold traffic and is wasted on retargeting, where the viewer already knows the product and the company page would do the same job. He graded one Hyro ad down specifically for running a warm-intent script as a partnership ad.
Sources: Andrew Faris (with Phil Kiel), Your Meta Ads Account Has Too Many Campaigns, 2026-05-12; Professor Charley T, Copy this Meta Ad strategy to BLOW UP your business. (After Andromeda, Clothing Niche), 2026-01-31; Blue Sense Digital, Reviewing 7 Ads: The One Change I'd Make To 6 Of Them, 2026-01-22
Last touched: 2026-08-19

### MD-054 · Diagnose CPMR only year over year; the absolute level does not matter, the change does
Tier: T3 · Status: active
Two windows: year-to-date versus the same period last year, and the last 7 or 30 days versus the same window last year. Short recent windows only work against the same window last year, because seasonality dominates everything else. A permanently high CPMR is fine if the business was built around it, the same way a permanently $50 CPM is fine when CTR and conversion rate put CPC at $1. The failure case is a $10 CPM becoming $40, because something else in the funnel then has to absorb the increase and usually nothing can. Pair CPMR with spend and reach: flat reach on rising spend is the diagnostic pattern. Kiel's summary: "high CPMR isn't bad. Where it's important is when it changes over time."
Sources: Andrew Faris (with Phil Kiel), Your Meta Ads Account Has Too Many Campaigns, 2026-05-12
Last touched: 2026-08-18

### MD-055 · When consolidation, creative diversity, exclusions, placements and partnership ads are all already in place and reach is still falling, rising CPMR is a product and market problem
Tier: T3 · Status: active
The original case: a UK brand (60M population), single-purchase product, over-indexed on Facebook, six or seven years of accumulated spend, negligible new product development. Multi-year data showed CPMR as the metric that moved most, spending more and reaching fewer, because the account had already reached most of the reachable population. With no reason to reach different people and no follow-up product giving a reason to reach the same people again, account structure and creative work were "fairly futile". The terminal move is diagnostic, not tactical: ask what the brand does outside the Meta ad account, require that it at minimum holds level and ideally increases, and measure its impact inside Meta. Named off-platform levers: new product development, product seeding with tracked post dates, blog and SEO. Symmetric with creative volume, if you can go from 10 creatives a week to 20, do the same outside the ad account. Case described, no data shown.
Sources: Andrew Faris (with Phil Kiel), Your Meta Ads Account Has Too Many Campaigns, 2026-05-12
Last touched: 2026-08-18

### MD-056 · Exclusion sets go stale: most accounts collapsed to purchasers plus email list after iOS 14 and never revisited, and rising spend against a shrinking TAM usually means website visitors need to come back in
Tier: T3 · Status: active
Pre-iOS-14 practice used every available exclusion: social engagers, page followers, website visitors. Post-iOS-14 practice collapsed to purchasers plus email list, and most accounts have sat there ever since. The correct exclusion set is a function of current spend, current TAM and current product velocity, so what was right two years ago is not right now. Adding website visitors back is the standard next step when frequency is climbing. This is a manual intervention against a delivery system that will otherwise keep spending prospecting budget on warm people, which MD-013 already names as the single most important remaining control.
Sources: Andrew Faris (with Phil Kiel), Your Meta Ads Account Has Too Many Campaigns, 2026-05-12
Last touched: 2026-08-18

### MD-057 · Running a retargeting ad set purely as a decoy, to absorb warm audiences so Meta does not serve them inside top-of-funnel ad sets, is in testing across five or six accounts
Tier: T3 · Status: active
The logic: if you do not give Meta a designated place to spend on warm audiences, it will find them inside your prospecting ad sets anyway, inflating frequency and CPMR while the report still says prospecting. The decoy ad set exists as a sink, and its own ROAS is not the point. Explicitly in-flight rather than settled: no numbers reported, described as collecting data across five or six accounts. It inverts SC-027's rationale from cost control to prospecting protection, and it takes the opposite operational turn from MD-052 off the same premise.
Sources: Andrew Faris (with Phil Kiel), Your Meta Ads Account Has Too Many Campaigns, 2026-05-12
Last touched: 2026-08-18

### MD-058 · Falling reach at equal spend may be Meta matching better rather than your account degrading
Tier: T4 · Status: active
Faris's theory, offered as a caveat on reading declining reach as automatically bad: Meta has saturated daily active users, so revenue growth has to come from higher value per impression, which means better ad-to-person matching, which mechanically reduces the number of people needed to hit the same result. Kiel concedes it is possible and notes the relevance of ads in his own feed is very strong. Practical consequence: never act on a reach decline in isolation, check whether business outcomes moved with it. Explicitly framed as a theory by the speaker, untested. Consistent with the pricing logic in MD-035.
Sources: Andrew Faris (with Phil Kiel), Your Meta Ads Account Has Too Many Campaigns, 2026-05-12
Last touched: 2026-08-18

### MD-079 · Cutting a clothing brand's daily budget from about $1,100 to about $500 left frequency flat, which proves a saturated finite pool and means the cut cost nothing incremental
Tier: T2 · Status: active
SHOWN in a live audit of a US catalog campaign broken down by day. Daily budget fell from roughly $1,100 to roughly $500 while frequency stayed flat. Charley T's read: the same pocket of people is being hit the same number of times, and CPM fell only because the advertiser is buying less pressure, not because delivery reached anyone new. Cost per purchase improved, gross profit per transaction improved with it, and AOV stayed consistent. His conclusion is that the pool is finite and already saturated, so cutting spend by more than half bought no loss in incremental volume, and that every cost in the account is pegged to how much you spend while user behaviour and audience stay unchanged.
This is the single cleanest diagnostic pattern in the CPMR cluster and it is cheap to run: cut budget materially, hold everything else, and watch frequency. Frequency flat means you were buying pressure. Frequency falling means you were buying reach. It is an observation on one account over one date range, not a holdout test, so the direction is the claim and the magnitude is not. MD-055 gives the terminal version of the same problem, where reach keeps falling with everything already in place.
Sources: Professor Charley T, Copy this Meta Ad strategy to BLOW UP your business. (After Andromeda, Clothing Niche), 2026-01-31 (account audit shown)
Last touched: 2026-08-19

## What Advertisers Can Still Control

### MD-013 · Meta's only hard targeting boundaries are location, minimum age, and language (plus exclusions); everything else is a suggestion
Tier: T2 · Status: active
Matt Shiver demonstrates in the Ads Manager UI that even after clicking "further limit the reach of ads" and selecting only a lookalike, Meta displays "lookalike audiences are always suggestions"; same for detailed targeting, and minimum age is settable up to 25. Blue Sense independently lists the remaining real controls as exclusions, minimum age, location, and language, with age bands, gender and interests treated as suggestions, and calls customer-list exclusions the single most important control because broad delivery will happily concentrate on the warm cluster and charge cold-acquisition CPMs for warm conversions.
Per-input nuance on the same toggle, shown in the UI by Ben Heath: ticking "further limit the reach of your ads" does harden the suggested-audience age, gender and detailed targeting into hard constraints, and Meta prints its own in-product warning that you are likely to get worse results. Both demos can be true if the toggle hardens demographic and interest inputs while lookalike seeds stay labelled suggestions. Read the claim per input, not as a blanket.
The consequence for funnel-stage account builds, from Ben Heath: custom audiences entered in the suggested-audience field are model inputs and not constraints, which is why a warm ad set leaks cold and a cold ad set leaks warm. Charley T adds the reverse case, that any cold user who engages becomes warm, so a genuinely warm-free cold audience would require conversion on first touch, which does not happen. Practitioner claim, no documentation cited. MD-075 records what this does to cold/warm/hot ad set separation.
Sources: Dr. Matt Shiver, How the Facebook Ads Algorithm Actually Works, 2026-07-21 (UI shown); Blue Sense Digital, How The Meta Ads Algorithm Works in 2026, 2026-07-28; Ben Heath, The BEST Instagram Ads Tutorial for Beginners in 2026, 2026-04-28 (UI shown); Professor Charley T (with Ben Heath), Facebook Ads in 2026: NEW Secrets, Tips & Strategies, 2026-04-15
Last touched: 2026-08-19

### MD-014 · Restricting age/gender from breakdown data raises costs and almost never improves performance durably
Tier: T3 · Status: active
Demographic restrictions cut the auction pool (higher CPM) and block Meta from finding converters outside the assumed demographic: gift buyers, near-boundary ages (33-34 vs a 35-54 target), and pass-along buyers. The common pattern of restricting to the best-ROAS segments in the breakdown almost never optimizes performance, and when it does the gain does not last; it is especially dangerous when conversion volume is too small for segment differences to be signal rather than noise. The advertiser's demographic assumption is an untested hypothesis enforced as a hard constraint.
Andrew Faris names the same edits as the standard panic response and extends the list beyond demographics: going male-only or female-only, cutting 18-24 because its ROAS looks bad, removing Audience Network because it is over-delivering. His rule is that these edits usually make things worse, and that the clean move when a placement genuinely looks broken is to kill the ad and relaunch it in a new ad set instead of editing the live one. If exclusions genuinely need to change for targeting reasons, expect volatility and plan for it, for example by giving existing customers their own ad set with its own budget rather than deleting them, since delivering to existing customers when they are the most likely buyers is a feature. Asserted from over 100 managed accounts, nothing shown.
Sources: Jon Loomer, You May Be Surprised Who Converts, 2026-07-22; Andrew Faris, I've Managed Over 100 Meta Ads Accounts. Here's Why Yours Is Broken., 2026-05-27
Last touched: 2026-08-19

### MD-015 · Under a purchase goal, delivery automatically skews toward converting demographics, so broad age/gender is safe; demographic waste appears under top-of-funnel goals
Tier: T3 · Status: active
With a purchase performance goal, Meta's objective aligns with the advertiser's: it delivers unevenly across demographics on its own and is unlikely to waste high budget share on non-converting groups, especially at spend levels that generate learning data. The exception is legally age-restricted products. With click, engagement, or video-view goals, Meta serves whoever performs that cheap action regardless of purchase likelihood, which is where real demographic misallocation occurs; even then, confirm the problem exists in the data before intervening, and intervene with a bid-down value rule, never a restriction.
Sources: Jon Loomer, You May Be Surprised Who Converts, 2026-07-22
Last touched: 2026-08-18

### MD-016 · Manually exclude the junk placements: Messenger, Threads, search results, in-stream, Facebook Reels, notifications feed, and Explore
Tier: T3 · Status: contested
Shiver used to recommend full Advantage+ placements but reversed after seeing too much spend go to placements that produced no results, naming Facebook Reels specifically for wasted spend. Current lead-gen recipe: Messenger and Threads off, "allow spend to excluded placements" off, then turn off search results, in-stream ads for reels, Facebook Reels, the notifications feed, Explore and business explore, keeping Facebook feed, profile feed, Instagram feed, Instagram profile, and right column. Advantage+ audience expansion stays on.
CONTESTED. Charley T says placement customisation is not worth managing at all, because delivery already withholds meaningful budget from placements where the creative performs poorly. He puts the exposure at under 0.1% of budget and treats the "my 1:1 renders as an ugly carousel" complaint as a rounding error, adding that placement customisation was not built for e-commerce. Neither side shows a spend-by-placement breakdown. Note the scope difference that may reconcile them: Shiver's case is lead generation, where a cheap shallow action is easy to buy on a junk placement, and Charley T's case is e-commerce purchase optimisation, where MD-015's alignment argument does more of the work. Resolving read: pull placement breakdown at ad-set level on your own account and check what share of spend the excluded placements actually take.
Sources: Dr. Matt Shiver, How to Run Facebook Ads for Coaches & Agency Owners, 2026-08-04; The 'Right Way' to Run Facebook Retargeting Ads in 2026, 2026-07-28; Professor Charley T, How to Scale Profits with Meta Ads, 2026-01-24
Last touched: 2026-08-19

### MD-017 · Go fully broad only above ~100 pixel fires on the optimization event; below that, seed with a 2-3 lookalike stack as suggestions
Tier: T3 · Status: active
Broad Advantage+ works by finding people similar to those who already hit the results column, so a new pixel with under 100 fires for the optimized event gives Meta nothing to pattern-match. Below the threshold he stacks 2-3 lookalikes (booked calls, qualified calls, paying clients), each seed needing at least 100 people, left as Advantage+ suggestions rather than hard limits, then drops them once the pixel has data. His demo account had 68 schedule fires as the seed pool.
Seed quality ranking, from Charley T, and it runs inverse to seed size: followers are the highest quality and the smallest pool and sit furthest down the trust funnel, website visitors sit one tier below, engagers are the lowest quality and the largest pool. Despite ranking last on quality he starts with a 30-day engager audience, because the 30-day window gives the machine the most data at a usable size. Drop to 7 days if 30 fails; 90, 180 and 365-day windows exist if more volume is needed. Practitioner claim, no comparative test shown.
Sources: Dr. Matt Shiver, How to Run Facebook Ads for Coaches & Agency Owners, 2026-08-04; How the Facebook Ads Algorithm Actually Works, 2026-07-21; Professor Charley T, How to CRUSH Facebook Ads with a Small Budget in 2026 (Full Course Post-Andromeda), 2026-04-09
Last touched: 2026-08-19

### MD-018 · For conversion-optimized retargeting, leave Advantage+ ON with warm audiences as suggestions; hard-limit reach only for shallow-event DM/engagement campaigns
Tier: T2 · Status: active
With schedule optimization, suggested (not limited) warm audiences let delivery start at the hottest pool and spill slightly wider, which he credits for his retargeting ad set's 5x cash collected ($14K spend to $60-70K revenue), attributed to this exact setting change. For DM ads optimizing a shallow engagement event, click "further limit the reach of ads" instead, and expect a much lower sustainable budget because the capped pool exhausts fast.
Prerequisite test before any of this, from Charley T: broad retargeting (warm engagers and site traffic used as a suggestion layer) is only worth running when the brand occupies some mental space. With no brand there is nobody to retarget, and the retargeting ad set then recycles a tiny pool and reports flattering CPAs that are pure last-touch credit theft. Rule: if nobody knows who you are, put 100% of budget in prospecting. Asserted, no numbers.
Charley T goes further and rejects event-based retargeting outright: "NO EVENT BASED RETARGETING. BROAD ALL THE WAY." A student reported switching from event-based to broad retargeting and called it their biggest win of the year, with no numbers attached. This is consistent with his anti-exclusion position in MD-068; both refuse to hand delivery a hand-built audience definition. He also argues the broad retargeting pool regenerates itself: running ads on organic content adds engagers and followers every day, follower growth adds earned organic reach, which adds more engagers, so the pool grows without a budget increase and never exhausts its supply of ready buyers. Reasoning only, no growth-curve data shown.
Window ladder for retargeting and engagement ad sets, covering site traffic and Instagram engagers: start at 30 days, widen to 90 if it performs and you cannot spend more, tighten to 7 if it fails, and stop testing the audience entirely if 7 also fails. His stated reason for starting at 30 rather than 7 or 90 is that 30 is the only starting point with a defined move in both directions, which bakes the next decision into the setup instead of requiring the first guess to be right.
Sources: Dr. Matt Shiver, The 'Right Way' to Run Facebook Retargeting Ads in 2026, 2026-07-28 (account result shown); Professor Charley T, Record Profits: the Meta Ads Andromeda Playbook, 2026-01-03 and Mastering Andromeda: Creative Testing and Scaling, 2025-12-13 and How to CRUSH Facebook Ads with a Small Budget in 2026 (Full Course Post-Andromeda), 2026-04-09 and Copy this Meta Ad strategy to BLOW UP your business. (After Andromeda, Clothing Niche), 2026-01-31
Last touched: 2026-08-19

### MD-019 · Defining existing-customer and engaged audiences in ad account settings lets Meta apportion budget across new/engaged/existing and report the split
Tier: T3 · Status: contested
Upload the customer list and define it as existing customers, and define external engaged audiences (email list, site visitors) that Meta cannot see on-platform. Meta then allocates budget between the three segments better and you can read how much spend went to warm vs existing vs new. Recommended at high budgets; it is a settings-level definition, not an ad-set targeting restriction.
Known failure mode: the upstream sync feeding that definition breaks periodically. Blue Sense monitors the Klaviyo-to-Meta audience segment sync continuously because when it breaks, existing customers stop flowing through correctly, exclusions stop working, cold campaigns start buying existing customers while reporting them as new, and every attribution read built on the segment split becomes wrong. Operator action: put a recurring check on the sync rather than treating audience setup as configure-once. MD-052 files the counter-reading, which argues the same breakdown cannot support separate retargeting structures at all.
CONTESTED, head-on, on camera, in one 2026-04-15 session. Ben Heath states the definitions do reach delivery: uploading the customer list and defining the segments "allows Meta to better allocate budget across cold, warm, and hot audience." Charley T cuts in and says the definitions never touch the delivery model and exist only so the advertiser can read a spend breakdown: "It's a reporting lens. It's not informing delivery. It's not direction for the machine." He adds a supporting observation, that the three segment totals sum to more than the account's total reach because users sit in more than one bucket at once.
Neither speaker shows evidence. Both are practitioner assertion, so tier does not break the tie and neither position supersedes the other. This is a resolvable factual question about a documented product surface, so it belongs on the watchlist: Meta's own help documentation or an engineering post on audience segment definitions would settle it outright. Until then, treat the reported split as reliable reporting and the budget-allocation benefit as unverified, and note the practical asymmetry, that defining the audiences costs nothing either way. Charley T's own separate use of the same setting (MD-052) is to throttle delivery to already-converted users, which is itself a delivery effect and sits awkwardly with his reporting-lens-only position.
Sources: Ben Heath, $100 vs $100,000 Facebook Ads Strategy, 2026-08-12; Blue Sense Digital, How To Structure A Meta Ads Account At Every Spend Tier In 2026, 2026-06-01; Professor Charley T (with Ben Heath), Facebook Ads in 2026: NEW Secrets, Tips & Strategies, 2026-04-15
Last touched: 2026-08-19

### MD-020 · With Meta's 2026 new-customers vs all-customers delivery option, choose new customers and accept the higher CPA
Tier: T3 · Status: active
Meta is rolling out (not to everyone yet) an option to deliver only to people who have not bought versus a mix of new and returning. Theriot picks new-customers-only: ad spend should buy new eyeballs while email/SMS re-converts existing customers at near-zero cost. New-customer CPA is higher, but the spend is known-incremental.
Launch mechanics, from Charley T: a campaign on a new objective runs roughly 4x the CPM at first because the machine has to relearn. Fund it with a small budget share and require only that it beat your worst existing entity, not your best. Once it clears second-worst, move budget off the worst entity into it and keep throttling toward volume of new customers to control CAC and cash flow. The 4x figure came from a viewer's account and he confirmed it rather than measuring it himself; nothing shown.
Sources: Nick Theriot, NEW Customers or ALL Customers with Meta Ads In 2026?, 2026-08-05; Professor Charley T, The NEW SIMPLE EASY WAY to Scale BIG with Meta Ads, 2026-02-07
Last touched: 2026-08-18

### MD-021 · Meta instant forms now support embedded calendar booking, and the flow captures contact info even when the lead abandons the booking step
Tier: T3 · Status: active
A "Book time" additional action on the instant-form end screen lets the lead book a slot on-platform after submitting contact info. Launch partners are Calendly and HighLevel, HubSpot announced for early August 2026, global availability expected October; only new instant forms get the option. Because the form submits name/email before the calendar step, an abandoning lead is still captured for outreach, unlike most website booking funnels, and contact info auto-prefills into the booking. Heath's general rule: less friction equals more leads and lower cost per lead.
Sources: Ben Heath, Facebook Ads Just Changed Forever!, 2026-07-23
Last touched: 2026-08-18

### MD-059 · Advantage+ is a compliance state that switches on when the campaign score is high enough, so treat every score deduction as a priced trade
Tier: T2 · Status: active
SHOWN in Ads Manager: a 98/100 campaign score with the only deduction coming from deselecting Facebook, Threads and Messenger placements, falling further when he disabled personalized destinations and skipped the sitelink, product and promotion extensions. Meta presents Advantage+ as a campaign type; the score behaves like a conformity measure that flips the label on when you do things the way Meta prefers. The operator reading follows: a high-but-not-100 score is the correct outcome when you deviate deliberately, and each deduction is a trade you priced rather than an error to fix. MD-016 covers manual placement exclusion; this is the scoring mechanic that makes the cost of those exclusions visible.
Sources: Ben Heath, The BEST Instagram Ads Tutorial for Beginners in 2026, 2026-04-28 (UI shown)
Last touched: 2026-08-18

### MD-060 · Meta's personalized-destination defaults can reroute traffic off your chosen landing page and inject a WhatsApp button onto your site, so check both per ad
Tier: T2 · Status: active
SHOWN in the ad-level UI. "Optimize website destination" sends each person to whichever page Meta judges most relevant (homepage, product page, collection page) and was OFF by default in his account. Shop was off. The WhatsApp browser add-on was ON by default. For any funnel with a designed VSL or single-page sequence the reroute is destructive, and the add-on hands the visitor an alternate contact path that bypasses the intended conversion. Turning both off costs campaign-score points (MD-059), which is the trade to accept.
Sources: Ben Heath, The BEST Instagram Ads Tutorial for Beginners in 2026, 2026-04-28 (UI shown)
Last touched: 2026-08-18

### MD-061 · Declare the special ad category even though declaring strips ad-set targeting, because failing to declare risks ad rejection and full account disablement
Tier: T3 · Status: active
Categories shown on screen: financial products and services, employment, housing, social issues, elections, politics. More than one can apply. The trade is explicit. Declaring removes targeting options at ad-set level. Not declaring and running the ads anyway risks rejection and, per the speaker, the entire ad account being disabled. His posture: if in doubt, select one. ASSERTED, no disablement case shown. MD-038 covers ban waves hitting clean accounts; this is the one ban risk the operator creates for himself.
Sources: Ben Heath, The BEST Instagram Ads Tutorial for Beginners in 2026, 2026-04-28
Last touched: 2026-08-18

### MD-062 · Set geo to the full area you can actually serve and let Meta find the pockets inside it
Tier: T3 · Status: active
Location is one of Meta's three genuine hard boundaries (MD-013), which makes narrowing it one of the few irreversible constraints an advertiser can still impose. The only correct input is service capability. Two symmetric failure modes: an audience larger than you can serve, and an artificially constrained one when you could serve wider. Do not pre-narrow to the city you believe converts best, because Meta will work out the best places inside the country on its own. For local service businesses the sizing question is travel distance in whichever direction the trade runs. Same logic as MD-014 and MD-015, applied to location. ASSERTED, no data.
Sources: Ben Heath, The BEST Instagram Ads Tutorial for Beginners in 2026, 2026-04-28
Last touched: 2026-08-18

### MD-063 · Turn Advantage+ creative optimizations off at the ad-account advertiser-settings level, because account-level automated rules switch them back on over time
Tier: T3 · Status: active
Path: advertiser settings, then the creative sub-dropdown, where a set of automated rules is on by default. Turning enhancements off ad by ad is both tedious and insufficient, because those account-level rules re-enable them later. This is standing hygiene rather than a one-time setup step, and it matters because enhancements alter creative you have already graded and approved. UI path given, not shown on screen.
Sources: Blue Sense Digital, How To Structure A Meta Ads Account At Every Spend Tier In 2026, 2026-06-01
Last touched: 2026-08-18

### MD-064 · Flexible ads are unavailable if catalog was selected at campaign level, and were unavailable in lead campaigns as of January 2026, where dynamic creative is the substitute
Tier: T3 · Status: active
The most common build blocker he fields, answered at least five times in one stream. Fix for catalog: rebuild the campaign with catalog unchecked. For lead objectives, dynamic creative is the fallback, which he describes as functionally the same thing one level up ("flexible ads is essentially just dynamic creative at the ad level") but limited to one ad per ad set. He also confirms Meta will sometimes render flexible creatives as a carousel, and says this stops at meaningful spend. Date-sensitive: verify current availability in Ads Manager before relying on it.
Sources: Professor Charley T, The BEST AD ON META after Andromeda, 2026-01-10
Last touched: 2026-08-18

### MD-065 · Paid engagement campaigns on organic content are claimed to pre-train delivery and lower conversion-campaign CPMs; the opposing position in the same session says skip them
Tier: T3 · Status: contested
Charley T's case: engagement inventory buys at roughly one tenth the CPM of conversion inventory, so an engagement campaign is a cheap qualification filter that populates the warm pool the conversion campaign then spends against, and Meta rewards content people want to see with lower CPMs. He recommends running it on every piece of organic content, including for new brands with no following, and cites a creator holding $4-5 CPMs in Western English-speaking markets as "an artifact of running engagement stuff for years". Numbers cited: a health and wellness account cut CPA from $200+ to under $80 and CPMs from $100-300 to under $30 in six weeks, while scaling $800/day to $3,500/day with 10-15% of budget in engagement plus broad retargeting.
Against: Ben Heath, in the same joint session, says run no awareness or engagement campaigns on a small budget and go straight to leads or sales. LS-021 records the same hazard, that optimizing for a top-of-funnel event delivers to whoever performs that cheap action regardless of purchase likelihood.
Evidence quality decides this one. Every number is asserted verbally with no dashboard, over a period with several simultaneous changes, so engagement spend is never isolated as the cause. Test it in one account before adopting, never blanket-apply.
Build constraint if you run it. Organic posts are ineligible to promote as existing posts when they carry copyrighted music, third-party filters, an attached extra such as a poll, or the carousel format. So a content calendar meant to feed paid seeding has to avoid those four things at creation time, not at promotion time. Platform behaviour asserted by a practitioner, no documentation cited, so verify in Ads Manager.
Sources: Professor Charley T (joint session with Ben Heath), How to CRUSH Facebook Ads with a Low Budget, 2026-02-28 and The NEW SIMPLE EASY WAY to Scale BIG with Meta Ads, 2026-02-07 and How to CRUSH Facebook Ads with a Small Budget in 2026 (Full Course Post-Andromeda), 2026-04-09
Last touched: 2026-08-19

### MD-068 · Exclusions are contested: one practitioner runs them on roughly 1% of ads and shows the arithmetic, while the codex's standing position calls customer-list exclusions the single most important remaining control
Tier: T3 · Status: contested
Against exclusions, Charley T. He uses exclusions on roughly 1% of the ads he runs, and add-to-cart exclusions 0.1% of the time. His historical argument is that holdout audiences and exclusion lists came out of email marketing, moved into search and especially branded search, and that Meta is a different technology solving a different problem. He extends it to customers: if you optimise for new customers at the conversion event, the exclusion is redundant. He tells a viewer excluding purchasers from broad to stop, and says a rise in purchase frequency caused by the ads is a win rather than a leak. He allows there are edge reasons and declines to name them.
The arithmetic he offers, on a viewer's real question about excluding 180-day buyers and a 4,000-person Klaviyo list on a $200/day budget: at a $10 CPM, $10 reaches 1,000 people, $40 reaches all 4,000, and $80 reaches each of them twice a day. On $200/day that worst case is under 50% of spend, and it requires every past customer to see every ad twice every single day, which delivery will not do because it is a poor end-user experience. He adds that excluding also raises CPMs, so you pay twice, and that if disinterested past customers are consuming impressions the real fault is content that appeals to non-buyers.
Benchmark from the same source. A viewer reporting about 9% of spend landing on engaged audiences and existing customers was told that is fine and is evidence the machine is already throttling the other 91%. To move it, optimise toward new customers at the conversion event, and expect the number to stay near 9% with the composition shifting from existing toward engaged. If those people buy, expect spend on engaged customers to rise.
For exclusions: MD-013 calls customer-list exclusions the single most important remaining control, because broad delivery will happily concentrate on the warm cluster and charge cold-acquisition CPMs for warm conversions. MD-056 says most accounts' exclusion sets went stale after iOS 14 and need website visitors added back. MD-057 goes further and builds a decoy retargeting ad set purely to absorb warm traffic. Neither side shows a controlled test. Note the scope difference that may reconcile them: the arithmetic case is scoped to a small list on a small budget, and MD-013's case is scoped to accounts where the warm pool is large relative to spend. Resolving test: run MD-008's frequency-by-day read on one prospecting ad set with and without the exclusion, and compare what share of spend lands on existing customers.
Sources: Professor Charley T, Mastering Andromeda: Creative Testing and Scaling, 2025-12-13 and Do these 5 things each day to scale Facebook Ads, 2026-02-21 and How to Scale Profits with Meta Ads, 2026-01-24
Last touched: 2026-08-19

### MD-076 · A 1% US lookalike is about 2.1 million people, so selecting it excludes roughly 198 million on a few thousand records, and lookalike size tiers are built mutually exclusive rather than nested
Tier: T4 · Status: active
Charley T's reframe is that a lookalike is an exclusion decision wearing an inclusion label. A 1,000-record seed produces a US 1% lookalike of roughly 2.1 million people, about 2,000 times the seed size, while discarding roughly 198 million people you could otherwise reach. His question is what customer-file size buys enough confidence to make that exclusion reliably, and his answer is that 100, 1,000 or even 5,000 customers is nowhere near the required order of magnitude, especially when the creative is doing the targeting anyway.
Second, a platform mechanic worth knowing if you still build them: when multiple lookalike sizes are created together, the larger ones are built to exclude the smaller ones. A 1%, 2% and 5% set is incremental rather than compounding, so a 5% is not a superset of the 1% and behaves as a distinctly lower-similarity pool. He says going past 1% is not necessary at all because a 1% is already large enough. Asserted by a practitioner, no documentation cited. Meta deprecated lookalike targeting in July 2025 (MD-002), so this now applies mainly to legacy audiences and to the sub-100-conversion seeding case in MD-017. Population figures stated, no test shown.
Sources: Professor Charley T, Meta Ads expert reacts to $1M/month Strategy, 2026-02-14 and Do these 5 things each day to scale Facebook Ads, 2026-02-21 and How to CRUSH Facebook Ads with a Small Budget in 2026 (Full Course Post-Andromeda), 2026-04-09
Last touched: 2026-08-19

### MD-078 · The small-budget broad retargeting build: sales objective, manual setup, pixel dataset, purchase or lead event, original audience with the stage-one seeds attached
Tier: T3 · Status: active
Charley T explicitly declines the advantage audience option in favour of original audience, then adds the same seed audiences used to build the lookalikes at stage one. The loop it closes: the seed audience produces the lookalikes, the lookalikes receive the content promotion, the content promotion grows the seed audience, and the sales campaign sells to the grown seed. That structure is the reason MD-018's self-regenerating retargeting pool is supposed to hold. Operating instruction from a course, with no comparison run against advantage audience and no performance data attached, so treat these settings as one working recipe rather than a tested optimum. Pairs with MD-017 for seed selection and MD-065 for the contested engagement-campaign half of the same system.
Sources: Professor Charley T, How to CRUSH Facebook Ads with a Small Budget in 2026 (Full Course Post-Andromeda), 2026-04-09
Last touched: 2026-08-19

## The Official Delivery Architecture (Meta Engineering)

### MD-022 · Meta's ads delivery is a multi-stage funnel: retrieval narrows tens of millions of candidates to a few thousand before ranking picks the final ads, all in ~200ms
Tier: T1 · Status: active
Retrieval is the first step of the multi-stage ads recommendation system, "selecting ads from tens of millions of ad candidates into a few thousand relevant ad candidates", processing three orders of magnitude more ads than subsequent stages. Larger ranking models then predict people and advertiser value to determine the final set shown. Blue Sense, citing Meta documentation, adds that the whole retrieval-ranking-auction pass runs in about 200 milliseconds and that Andromeda is a retrieval-stage change, which is why the creative content itself decides which auctions an ad even enters.
Sources: Engineering at Meta, Meta Andromeda post, 2024-12-02; Blue Sense Digital, How The Meta Ads Algorithm Works in 2026, 2026-07-28
Last touched: 2026-08-18

### MD-023 · Within a surface, the ranking funnel has three layers: sourcing (retrieval), early-stage ranking, and late-stage ranking, each on fewer candidates as operations get costlier
Tier: T1 · Status: active
Meta describes the layers explicitly: sourcing/retrieval, ESR, then LSR, with progressively fewer candidates as model cost per candidate rises. The system must retrieve and rank thousands of ads within milliseconds while processing millions of candidates per second.
Sources: Engineering at Meta, Journey to 1000 Models, 2025-05-21
Last touched: 2026-08-18

### MD-024 · Andromeda increased retrieval model capacity roughly 10,000x, delivering +6% recall and +8% ads quality on selected segments
Tier: T1 · Status: active
Andromeda is Meta's ML redesign of the retrieval stage, run on NVIDIA Grace Hopper Superchips and Meta's MTIA accelerators. Model capacity grew 10,000x versus the prior system, producing a +6% recall improvement and +8% ads quality improvement on selected segments. Meta expects another 1,000x increase in model complexity.
Sources: Engineering at Meta, Meta Andromeda post, 2024-12-02
Last touched: 2026-08-18

### MD-025 · Andromeda's retrieval models learn complex latent relationships between people's interests, products, and services rather than simple matching
Tier: T1 · Status: active
Meta states the upgraded retrieval system uses advanced interaction features and new algorithms to capture "complex latent relationships between people's interests, products, and services". Personalization at the retrieval stage means which ads even enter the auction for a given person is model-decided, not audience-setting decided.
Sources: Engineering at Meta, Meta Andromeda post, 2024-12-02
Last touched: 2026-08-18

### MD-026 · Andromeda uses a hierarchical multi-layer index and model elasticity to evaluate an enormous number of ads per request within milliseconds
Tier: T1 · Status: active
The retrieval engine's hierarchical index reduces inference steps and achieves sub-linear inference costs. Model elasticity boosted inference efficiency 10x, end-to-end queries per second improved over 3x, and feature extraction latency/throughput improved over 100x. This machinery is what lets a per-person candidate pool stay huge.
Sources: Engineering at Meta, Meta Andromeda post, 2024-12-02
Last touched: 2026-08-18

### MD-027 · Meta's ads ranking splits into an offline user model producing cached user embeddings and an online model scoring ad candidates in real time
Tier: T1 · Status: active
The offline model processes long user histories asynchronously (thousands of events: clicks, views, purchases) and caches embeddings; the online model combines those cached representations with fresh user signals and ad candidate information under strict latency budgets. Target-aware attention weighs a user's past behaviors against the specific ad being scored, the direct personalization mechanic per impression.
Sources: Engineering at Meta, From User Sequences to Scaling Laws, 2026-08-05
Last touched: 2026-08-18

### MD-028 · Ranking improvements follow a log-linear scaling law with compute; the sequence architecture delivered +6% Instagram conversions, +3% Facebook conversions, +3.5% Facebook ad clicks cumulatively
Tier: T1 · Status: active
Performance scales log-linearly with compute via four levers: balanced model shape (depth/width/sequence length), multi-stage tunability, sequence composition diversity, and semantic feature representation. Cumulative business impact stated: 6% in conversions on Instagram, 3% in conversions on Facebook, 3.5% in ad clicks on Facebook.
Sources: Engineering at Meta, From User Sequences to Scaling Laws, 2026-08-05
Last touched: 2026-08-18

## GEM: The Ads Foundation Model

### MD-029 · GEM is Meta's LLM-scale ads foundation model, the "central brain" that improves hundreds of production ads models rather than serving ads directly
Tier: T1 · Status: active
GEM is described as the largest recommendation-system foundation model in the industry, trained across thousands of GPUs. It transfers knowledge to hundreds of user-facing vertical models via knowledge distillation, representation learning, and parameter sharing, achieving 2x the effectiveness of standard knowledge distillation. A "Student Adapter" refines the teacher's outputs using the most recent ground-truth data.
Sources: Engineering at Meta, Meta's Generative Ads Model (GEM), 2025-11-10
Last touched: 2026-08-18

### MD-030 · GEM's architecture is 4x more efficient at driving ad performance gains per unit of data and compute than Meta's original ads ranking models
Tier: T1 · Status: active
GEM uses stackable factorization machines with cross-layer attention, a pyramid-parallel structure for sequences up to thousands of events, an InterFormer design alternating sequence and cross-feature layers, and multi-domain learning optimized separately for Facebook, Instagram, and Business Messaging. Q3 improvements "doubled the performance benefit" from added data and compute.
Sources: Engineering at Meta, Meta's Generative Ads Model (GEM), 2025-11-10
Last touched: 2026-08-18

### MD-031 · GEM lifted ad conversions +5% on Instagram and +3% on Facebook Feed in a single quarter (Q2 2025)
Tier: T1 · Status: active
Meta states GEM produced a 5% increase in ad conversions on Instagram and 3% on Facebook Feed in Q2, with Q3 doubling the performance benefit from scaling data and compute. These are platform-wide model gains an advertiser inherits without changing anything.
Sources: Engineering at Meta, Meta's Generative Ads Model (GEM), 2025-11-10
Last touched: 2026-08-18

### MD-032 · GEM trains on several thousand latest-generation GPUs with trillions of sparse embedding parameters; Meta scaled its training FLOPs 4x in 12 months
Tier: T1 · Status: active
The training post states GEM trains at LLM scale on several thousand of the latest-generation GPUs, uses a hybrid architecture with trillions of sparse embedding parameters and billions of dense parameters, and that Meta doubled end-to-end training efficiency to 20-25% Model FLOPs Utilization while scaling training FLOPs 4x in 12 months. The Nov 2025 post adds a 23x increase in effective training FLOPs with a 1.43x increase in MFU and 16x more GPUs.
Sources: Engineering at Meta, Training GEM at LLM Scale, 2026-08-03
Last touched: 2026-08-18

### MD-033 · Meta keeps its ads foundation models fresh with continuous online training rather than fixed periodic retrains
Tier: T1 · Status: active
The GEM post references continuous online training to refresh the foundation models, alongside the Student Adapter that corrects outputs with the most recent ground-truth data before knowledge reaches production vertical models. Neither GEM post discloses a fixed retrain cadence.
Sources: Engineering at Meta, Meta's Generative Ads Model (GEM), 2025-11-10
Last touched: 2026-08-18

### MD-034 · Meta's incremental attribution is a machine-learning model trained on the mass of free conversion lift studies, giving Meta a 3-5 year moat
Tier: T3 · Status: active
Meta made conversion lift free for all advertisers with no minimum spend after rebuilding it on CAPI post-iOS 14.5, sacrificing short-term revenue to accumulate a huge training corpus, potentially millions of lift studies. IA replaces the click-as-proxy-for-incrementality heuristic with a model trained on user-level lift outcomes. A competitor would have to build self-serve free conversion lift, accumulate years of data, then train a model, hence the 3-5 year lead estimate. An earlier version tested by Netflix around 2017-2018 failed because almost no lift data existed to train on.
The operator-facing consequence most people get wrong: no live holdout group runs inside your ad account. Blue Sense states Meta takes conversion lift experiments from competitors in your niche, reads how incremental those were, and applies a factor into your account. The IA column is therefore an industry-level estimate applied to you, not measured lift on your own campaigns. Still useful directionally, because the training data is real lift experiments. Use IA as a second validation layer and never as a substitute for your own geo test.
Sources: Andrew Faris (with Olivia of Haus), DTC Brands See 38% Better Meta Ads Performance When They Switch To Incremental Attribution, 2026-08-10; Blue Sense Digital, The 1 Bottleneck I See in 80% of eCommerce Audits, 2026-05-18
Last touched: 2026-08-18

## Platform Economics, Bugs, and Ops

### MD-035 · Meta's algorithm updates raise platform-wide efficiency and Meta captures the gain via CPMs: expect ROAS to stay flat while CPMs rise every year
Tier: T3 · Status: active
Meta grows revenue by increasing ad load or increasing price; ad load has a ceiling, CPMs do not, so CPMs will be higher next year. Algorithm updates that lift advertiser CTR/CVR let Meta reprice upward and keep the surplus. Operator implication: annual CTR or CVR improvement is required just to hold profitability flat; those who improve faster than the majority gain share as the rest pull back under CPM pressure.
Magnitude: an aggregated ad report across $150M+ of spend connected to their own business manager shows roughly 20-30% annual CPM inflation over three years, cyclical with Black Friday and faster than currency inflation. The report was described, not shown, so this stays T3. He frames Meta's objective function as revenue per user per minute with exactly two levers, more ad inventory (triple-ad sequences in feed today versus one ad per 5-6 posts six years ago) or higher CPMs. The structural constraint explains why the updates keep arriving: Meta cannot raise CPMs without also raising expected conversion rates, or every advertiser goes unprofitable and stops spending, so each release improves ad-serving efficiency first and licences the price increase second.
Sources: Blue Sense Digital, The Death Spiral That Kills Most eCommerce Brands, 2026-07-22; How The Meta Ads Algorithm Works in 2026, 2026-07-28; How To Structure A Meta Ads Account At Every Spend Tier In 2026, 2026-06-01; How to Scale an eCommerce Brand Profitably in 2026: The Full System, 2026-06-15
Last touched: 2026-08-18

### MD-036 · Boosting from an Instagram profile costs ~30% more than running the same ads through a Meta Business Portfolio, with no extra results
Tier: T3 · Status: active
Advertising directly from a profile feels quick but carries roughly a 30% cost premium and far more limited options versus a proper Business Portfolio and Ads Manager. Framed as a day-one setup step that is cheap to do early and expensive to fix after spend has started.
Sources: Ben Heath, What You NEED To Know To Get Started With Facebook Ads, 2026-08-06
Last touched: 2026-08-18

### MD-037 · Bug (Aug 2026): raising the budget inside an existing well-performing campaign or ad set caused results to drop to zero or by 90%+ in many accounts
Tier: T3 · Status: active
Observed across many client ad accounts (his business manager holds 1,400+), affecting only in-place budget increases on winners, distinct from the normal mild CPA/ROAS degradation of scaling. It did not hit every account but hit enough to establish a pattern; no official Meta acknowledgment, fix expected within roughly a week to a month. Workaround: duplicate the winning campaign/ad set at the higher budget and turn the original OFF, never run replicas simultaneously. He stresses this is a temporary fix; in-place scaling is normally superior because duplication discards accrued learning (MD-011).
Sources: Ben Heath, Urgent Message For Facebook Advertisers!, 2026-08-03
Last touched: 2026-08-18

### MD-038 · Ad account shutdowns hit even clean accounts during Meta ban waves; backup accounts and recovery contacts are standing infrastructure
Tier: T2 · Status: active
A properly warmed account with zero rejected ads was shut down on day 2 of spend and restored the morning of its first $1k day, the gap visible in the shown revenue timeline. The operator treats bans as part of the game and pre-provisions backup ad accounts, agency accounts, and recovery channels because any single recovery route sometimes works and sometimes does not.
Sources: Mark Builds Brands, ZERO to $1k/day in 3 days with ai dropshipping, 2026-07-30
Last touched: 2026-08-18

### MD-066 · Meta caps live ads per Facebook Page at roughly 300-500, so high-volume accounts need a Page strategy rather than turning winners off
Tier: T3 · Status: active
Once creative throughput passes the cap the advertiser has two options: pause ads that are working, or add Pages. Four named workarounds. Duplicate brand Pages, with Gruns cited as running about 15 Pages that differ only by logo colour. Third-party whitelisting Pages, a publisher-looking handle such as "fiber health magazine" running advertorial-framed versions of the same ads. Partnership ads. And per-country Pages, because a multi-region account carrying roughly 100 ads per country campaign burns through one Page's cap fastest, so Brand UK, Brand AU and Brand US each get their own cap. He would run all of them simultaneously at scale, and calls flexible ads the wrong solution when they are used purely as a cap workaround.
Two caveats the operator has to carry. The "about 3 to 500" figure is ASSERTED and not sourced to Meta documentation, so read your own Page's ad limit in Ads Manager before building a Page strategy on the number. And the source does not address the ban-wave exposure of running many near-identical Pages and Business Manager assets (MD-038), which compounds with the multi-Page play in MD-042.
Sources: Blue Sense Digital, How to Scale an eCommerce Brand Profitably in 2026: The Full System, 2026-06-15 and How To Structure A Meta Ads Account At Every Spend Tier In 2026, 2026-06-01
Last touched: 2026-08-18

### MD-039 · AI agents will become an ad audience (sponsored listings in agent-queried databases), but human-facing brand ads remain necessary
Tier: T4 · Status: active
Meta CMO Alex Schultz predicts agent-targeted ads within 10 years: today an LLM recommends vendors from training-data preferences, later it will query databases containing sponsored plus free listings. But when an agent buys on your behalf it buys your preferred brand, and those preferences are built by ads shown to humans over years, so human brand advertising and agent-facing listings will coexist. Pure forecast; no data possible yet.
Sources: Ben Heath, Meta's CMO on AI Ads and Rising Meta Ad Costs, 2026-07-20
Last touched: 2026-08-18

### MD-040 · Google/YouTube holds deeper personal data than Meta and its recommender seeds expansion from rich viewer profiles the way Meta seeds from pixel events
Tier: T4 · Status: active
YouTube sees identity, email, location, and watch-time by topic ("35-year-old guy, lives here, watched 20 minutes of a 30-minute video") and finds more viewers like that seed, but the seed viewer usually arrived from ads, email, or short-form rather than YouTube discovery. This is the organic mirror of the results-column mechanism: whoever you send into the channel defines who the algorithm brings next. Plausible platform-mechanics reasoning without cited documentation.
Sources: Dr. Matt Shiver, How He Made $15M From YouTube, 2026-07-23
Last touched: 2026-08-18

### MD-069 · Meta is claimed to hold the strongest middle and top-funnel audience capture and to be the best lead-generation channel for high-ticket B2B
Tier: T3 · Status: active
Worth banking mainly for who says it. Michael Nadalin is publicly known for Google Ads content, has 11 years full-time in paid and more than $115 million in tracked ad spend, and states Meta has the strongest middle and top funnel audience capture he has seen. He extends it to B2B: for his high-ticket B2B lead generation clients Meta is the best lead generation channel, and he calls the performance "wild". He adds that he runs Meta accounts himself and gets the same or better results than on Google. Practitioner assertion with no CPL, close rate, or account figures given, from a source with no obvious incentive to favour Meta. Read it as a prior on channel selection for high-ticket B2B rather than as evidence, and note it says nothing about which structure or creative makes it work.
Sources: Blue Sense Digital, Two Years Later: What Still Works (And What Doesn't) ft. Michael Nadalin, 2025-12-27
Last touched: 2026-08-19

### MD-073 · Meta engineering guidance describes how a tool was built, which is a weaker claim than how the tool behaves in a live account
Tier: T4 · Status: active
Challenged on why he disagrees with Meta's own published recommendation to increase ad volume, Charley T draws the distinction directly: "the engineering team is not a marketing department. What the engineer has built the tool to use versus how it's used in the real world aren't always the same thing." He notes that practitioners who spent years distrusting Meta communications now treat one engineering document as authoritative, and his epistemic rule is that neither side can prove the mechanism without writing the code, so account evidence still has to be weighed.
This is a direct challenge to the codex's own tier ordering, where T1 documentation outranks T3 practitioner claims, so it is worth stating the reconciliation the codex should hold. A T1 engineering post is authoritative about what Meta built and what Meta measured. It is not authoritative about what a given account should do. MD-024's +6% recall and MD-031's +5% Instagram conversion lift are platform-wide averages, not account predictions. Keep documentation above assertion on questions of mechanism, and keep account evidence above documentation on questions of operator action. Reasoning only, and self-serving toward a position that contradicts Meta's published guidance.
Sources: Professor Charley T, Q5: the 2nd Black Friday: Meta Ads for Profit, 2025-12-20
Last touched: 2026-08-19

## Pre-Andromeda Mechanism (March 2025 Baseline)

One source, a 25 March 2025 whiteboard episode, recorded before Meta's July 2025 deprecation of detailed interest and lookalike targeting and before all the Andromeda-era material above. No screenshots, no spend, no before-and-after, so everything here is T3 or T4. Claims a later platform change has overtaken carry `Status: superseded` and name the claim that replaced them. They stay in the codex because they record what the mechanism looked like before the change.

### MD-082 · Meta ingests off-platform behaviour through third-party "sign in with Facebook" logins and folds it into ad targeting
Tier: T4 · Status: active
The speaker's account of the data pipeline starts with on-platform signals (likes, shares, comments) and then claims Meta deliberately extends it off-platform, with the social-login button on third-party websites as the stated mechanism. His framing is that the login convenience exists to license the data flow rather than as a user-experience feature. Asserted, no data shown, no platform documentation cited, and no distinction drawn between what a social login actually exposes and what Meta is permitted to use. The operating implication is indirect: the targetable signal set is wider than in-app behaviour, which is consistent with MD-002's pixel and browsing signals and with MD-041's account of what ATT removed. Bank as a hypothesis about signal breadth.
Sources: Blue Sense Digital, How Machine Learning Works in Meta Ads (2025), 2025-03-25
Last touched: 2026-08-19

### MD-083 · A single interest is a weak buying signal; the productive unit is roughly ten psychographic traits intersecting on a pocket of about 20,000 people
Tier: T4 · Status: active
The argument that survives the interest-targeting deprecation intact, because it explains why broad works rather than why interests failed. "Likes pets" on its own carries little intent. What predicts action is the intersection: likes pets, engages with a particular post type, has two kids, lives in a given area, about ten traits deep, converging on a pocket he sizes at roughly 20,000 people. Only broad targeting can reach that intersection, because manual interest selection cannot express a ten-way conjunction. The 20,000 figure is illustrative with no source or measurement behind it, so use the structure of the argument and not the number. This is the cluster in MD-002's embedding space stated in plain language, and it is the clearest available intuition for why the creative has to name a specific situation (MD-001) rather than a demographic.
Sources: Blue Sense Digital, How Machine Learning Works in Meta Ads (2025), 2025-03-25
Last touched: 2026-08-19

### MD-084 · Vector-based targeting made sensitive-audience restrictions unenforceable at the targeting layer, so Meta policed the optimisation layer instead
Tier: T4 · Status: active
The causal story for why health advertisers lost purchase optimisation. Meta removed sensitive interests roughly one to two years before March 2025. But once audiences live in an embedding space rather than in named segments, an advertiser can still reach a sensitive audience by writing copy that resonates only with that audience, which drives the model straight to that region of the space. Since the targeting layer cannot be policed, Meta policed the optimisation layer and blocked purchase optimisation for health advertisers, who still get some machine-learning benefit with vaguer and less precise targeting. Asserted, no documentation cited.
The durable part is the mechanism, and it generalises: when targeting inputs stop being explicit, platform enforcement moves to the layers that remain explicit, which are the optimisation event, the creative and the landing page. The specifics are stale. Meta rewrote its health advertising rules onto a claims-based footing in July 2026, so any checklist derived from the March 2025 state is out of date and the current rules have to be read fresh.
Sources: Blue Sense Digital, How Machine Learning Works in Meta Ads (2025), 2025-03-25
Last touched: 2026-08-19

### MD-085 · Meta is said to borrow data from other campaigns running similar creative to speed up a new campaign's learning
Tier: T3 · Status: active
The speaker says he has seen Meta state this more than once and flags it as the point not to skip: when a new campaign or ad set launches, Meta looks at other similar campaigns with similar creatives and pulls their data across to accelerate learning. He treats it as the underlying engine of Advantage+. He names no document, so T3 rather than T1. If true it cuts two ways. A new ad set carrying creative similar to an existing winner should stabilise faster than a genuinely novel one, which is an argument for iterating on a proven concept when speed matters. And it is the benign face of the same similarity detection MD-003 describes as entity collapse, where near-duplicate creatives get bundled into one delivery pool with zero unique reach. Worth resolving against Meta documentation, because the two readings point to opposite creative strategies.
Sources: Blue Sense Digital, How Machine Learning Works in Meta Ads (2025), 2025-03-25
Last touched: 2026-08-19

### MD-086 · March 2025 position: interest targeting was dying and optional, because the interest label no longer existed as a retrievable segment
Tier: T4 · Status: superseded
SUPERSEDED by MD-002, which records Meta's July 2025 deprecation of interest and lookalike targeting. The operating advice survived, the "dying and optional" framing did not.
What the March 2025 version said: once users sit in an embedding space instead of carrying named tags, selecting an interest reverts you to the crude old method and buys everyone who carries that trait, while broad lets the model locate the productive region of the space and serve only that cluster. He cited this as one reason Meta was moving toward broad-only targeting. Kept because it dates the mechanism argument roughly four months ahead of the product change, which is the useful part: the delivery architecture made interest targeting obsolete before the product removed it. Asserted, no test data shown.
Sources: Blue Sense Digital, How Machine Learning Works in Meta Ads (2025), 2025-03-25
Last touched: 2026-08-19

### MD-087 · March 2025 position: Advantage+ skipped the learning phase by generating instantaneous lookalikes from account history, and carried less in-campaign reinforcement than a CBO
Tier: T3 · Status: superseded
SUPERSEDED on the mechanism by MD-002, since lookalike targeting was deprecated in July 2025, and on the structure by MD-004, since Meta consolidated Advantage+ and Advantage+ Shopping into a single campaign flow through 2025, which dissolves the ABO versus CBO versus Advantage+ comparison he draws.
What the March 2025 version said: Advantage+ never enters the learning phase because it uses all historical account data to build instantaneous lookalike audiences and opens against people it already believes are warm. His offered check is observational, that you have never seen an Advantage+ campaign sitting in learning. He also said the campaign type carries less data reinforcement than a CBO. Asserted, no data shown.
The part likely to survive is account-history-as-warm-start: a campaign type that opens against people the account's own history already predicts, rather than sampling cold and reinforcing off the response. MD-006 and MD-025 describe the Andromeda-era version of that behaviour with more precision.
Sources: Blue Sense Digital, How Machine Learning Works in Meta Ads (2025), 2025-03-25
Last touched: 2026-08-19

### MD-088 · March 2025 belief: ABO and CBO had also stopped doing true broad cold-start and were opening against high-intent users from account-level data
Tier: T4 · Status: superseded
SUPERSEDED by MD-006 and MD-025, which describe the same behaviour with a mechanism attached: retrieval decides per person which ads enter the auction, and a new ad with no history gets routed to the warmest audience first to build signal fast.
What the March 2025 version said, explicitly hedged as belief and not a finding: the old pattern of sampling a cold broad audience and reinforcing off the response was fading from ABO and CBO too, with both campaign types going straight at high-intent users using account-level data. He framed the whole direction as one large push toward Advantage+, on the grounds that vector-based user labelling outperforms sample-then-reinforce. No data shown. Kept because it is the pre-Andromeda formulation of a trend the Andromeda-era claims now state precisely, so it shows a practitioner reading the direction correctly before the vocabulary existed.
Sources: Blue Sense Digital, How Machine Learning Works in Meta Ads (2025), 2025-03-25
Last touched: 2026-08-19

