# -*- coding: utf-8 -*-
"""Claim merge for the 2026-10-19 research run.

Sources: Google Ads API v26 release notes and the Ads Developer Blog posts of
12 and 14 October 2026, plus Meta's 2026 Out-Of-Cycle Changes shelf, found this
run at a NEW URL after the Marketing API changelog moved and stopped
under-rendering.
"""
from pathlib import Path

V = Path(r"E:\claude code marketing skill\Obsidian God-level Marketing Vault\God-level Marketing\wiki\science")


def append(fn, text):
    p = V / fn
    cur = p.read_text(encoding="utf-8")
    if not cur.endswith("\n"):
        cur += "\n"
    p.write_text(cur + "\n" + text.strip() + "\n", encoding="utf-8")
    print("appended to", fn, len(text), "chars")


MD182 = """
### MD-182 · Meta moved AGE AND GENDER off the ad set and onto the CREATIVE in October 2026, and a persona can now be attached to a single image or video inside one ad
Tier: T1 · Status: active
Meta Marketing API out-of-cycle change dated 14 October 2026, read in full at source. "Creative audience pairing lets you set age and gender on the ad creative instead of the ad set."

**How it is switched on, exactly.** It is opt-in per ad set, by setting `creative_audience_pairing` to 1 inside `targeting_automation` in the ad set targeting spec. The parameter accepts only 0 or 1, and Meta states that omitting it leaves the feature off. So nothing changes in an existing account until somebody turns it on, which is the opposite of the Advantage+ enhancements recorded at [[Meta Delivery & Andromeda#MD-183|MD-183]].

**The granularity is the finding.** A persona is attached through `creative_audience_pairing_persona`, and it can sit at two levels: on the ad, which pairs the whole ad, or on an individual image or video inside `media_sourcing_spec`, which pairs a single media asset. Meta states the precedence rule itself: **a media asset's own persona overrides the persona set on the ad.** One ad can therefore carry several assets each aimed at a different age and gender band, resolved per asset rather than per ad set.

**Why this matters more than it looks.** Every structural claim in this file treats the ad set as the unit where audience is declared and the ad as the unit where the message is declared. This collapses that split: demographic intent becomes a property of the asset. It runs in the same direction as [[Meta Delivery & Andromeda#MD-001|MD-001]], where the creative is the primary targeting input, and it is the first time Meta has given the advertiser a field to say which person a specific piece of footage is for.

**What is NOT established, and no run should imply it.** Meta publishes no performance figure, no test, no rollout scope and no statement that paired creative delivers better than unpaired. There is nothing here about whether a declared persona narrows the candidate pool, biases retrieval, or is treated as a hint the system can ignore. It is a capability, not an effect.

**The operating read for our book.** Both our chiropractic work and our truck-dealership work already run separate ads for separate buyer types, split across ad sets. If pairing holds up, the same split could live inside one ad set, which is the structure [[Scaling Models#SC-179|SC-179]] says is bounded at 200 ad sets per campaign. Nothing to act on until the field appears in an account and somebody measures it. Worth one look in Ads Manager on a client account to see whether the control exists outside the API at all.
Sources: Meta for Developers, 2026 Out-Of-Cycle Changes to Marketing API, entry dated 2026-10-14, read in full 2026-10-19 at developers.facebook.com/documentation/ads-commerce/marketing-api/out-of-cycle-changes/occ-2026
Last touched: 2026-10-19
"""

MD183 = """
### MD-183 · Meta shipped three Advantage+ enhancements in June 2026 that ALTER the footage itself, animating a static image, converting video to HDR and uncropping video to fill vertical placements, each controlled per creative
Tier: T1 · Status: active
Three Marketing API out-of-cycle changes all dated 28 June 2026, read in full at source, plus a fourth from 1 June 2026. All four change the asset Meta serves rather than the targeting or the budget.

**Image Animation.** "A static image in your ad is automatically transformed into a short, subtly animated video to make your creative more engaging." Controlled per creative through the `image_animation` field in `degrees_of_freedom_spec.creative_features_spec`.

**Video Filter.** "A visual enhancement is automatically applied to your video creative, for example, improving color or converting standard dynamic range (SDR) video to high dynamic range (HDR)." Field `video_filtering`, same spec.

**Video Uncrop.** "Your video is automatically expanded (uncropped) to better fit the aspect ratio of additional placements, for example, filling vertical, full-screen surfaces instead of cropping or letterboxing your video." Field `video_uncrop`, same spec.

**IG Audio Swap, 1 June 2026, and this one is advertiser-initiated.** New parameters on `POST /act_{id}/advideos` replace copyrighted music on Instagram Reels with royalty-free audio from Meta's Sound Collection: pass `source_instagram_media_id` with `selected_audio_spec`. It is asynchronous, and Meta's instruction is to poll `replace_audio_status` on `GET /{ad-video-id}` until it returns `SUCCESSFUL` before building creative on the swapped video.

**The consequence for a graded edit, and it is the reason to bank this.** We grade our own video work on deliberate choices: one font family, a specific colour treatment, framing that keeps the whole subject in shot, levels set per track. Image Animation, Video Filter and Video Uncrop each override one of those after delivery, and Meta's phrasing is "automatically applied". **Uncrop is the sharpest risk on our book, because it reframes a composition to fill a taller surface, and a reframe is exactly what a subject-in-frame rule exists to prevent.** Nothing in the change notes states whether the enhancements are on by default; Meta says only that you opt in to or out of them per creative. **So the honest instruction is to open `degrees_of_freedom_spec` on a live client ad and read its actual state, not to assume either way.**

**Unevidenced.** No performance figure, no test and no sample appears beside any of the three. "To make your creative more engaging" and "more visually appealing" are product copy. Same reading rule as [[Meta Delivery & Andromeda#MD-171|MD-171]]: find the population and the counterfactual before carrying a number, and here there is no number at all.

**Where this sits in the existing record.** This file already holds Advantage+ creative enhancements as a category. These three are new members of it, and they are the first that modify the pixels and the audio of a supplied asset rather than arranging it, cropping it to a known ratio, or adding an overlay.
Sources: Meta for Developers, 2026 Out-Of-Cycle Changes to Marketing API, entries dated 2026-06-28 (Image Animation, Video Filter, Video Uncrop) and 2026-06-01 (IG Audio Swap), read in full 2026-10-19
Last touched: 2026-10-19
"""

AT128 = """
### AT-128 · Meta gated three Ads Insights breakdowns behind per-account enablement in August 2026, and an unenabled account returns NO RESULTS rather than an error
Tier: T1 · Status: active
Marketing API out-of-cycle change dated 8 May 2026, effective 6 August 2026, read in full at source. Three breakdowns now require enablement for certain ad accounts:

- `breakdowns=impression_device`, including any combination containing it
- `breakdowns=hourly_stats_aggregated_by_audience_time_zone`
- `breakdowns=frequency_value`

**The failure mode is silence, and that is the whole reason to bank this.** Meta's own sentence: "API requests using these breakdowns may return no results for Ad Accounts that have not enabled them, whether synchronous or asynchronous." An empty result set is not an error. **A report pipeline that reads device split, hour of day or frequency distribution from the API on an unenabled account produces a clean, well-formed, empty answer, and nothing in the response says the data was withheld rather than absent.** Downstream that reads as "no impressions on desktop" or "frequency unavailable", which is a false statement about the account.

**How access is restored.** An account administrator requests the breakdown in Ads Manager. After enablement, synchronous calls work from that day onward, and **historical data comes back only through asynchronous report jobs**, which Meta throttles at `min(10, number_of_ad_groups)` per 24 hours. So a backfill on a small account is capped by its own ad-group count: an account with three ad groups gets three async jobs a day.

**What we have to do about it.** Three of our own instruments touch these breakdowns. Frequency is quoted directly in our portfolio record at [[Auction Mechanics & Bidding#AU-093|AU-093]] and in the fatigue thresholds at [[Creative Science#CR-177|CR-177]]. Hour of day sits behind every speed-to-lead and business-hours argument we make. **Any frequency or hour-of-day figure pulled through the API since 6 August 2026 needs its account checked for enablement before it is quoted again**, because an empty pull and a genuine zero are indistinguishable in the output. The cheapest check is to request the breakdown over a known-busy window and see whether rows come back at all.

**Limit on the claim, stated.** Meta says "certain Ad Accounts", not all, and publishes no list and no criterion for which accounts are affected. So the exposure is unknown per account and has to be tested rather than assumed.
Sources: Meta for Developers, 2026 Out-Of-Cycle Changes to Marketing API, entry dated 2026-05-08 effective 2026-08-06, read in full 2026-10-19
Last touched: 2026-10-19
"""

AT129 = """
### AT-129 · Meta retired Nielsen DMAs for Comscore Markets on 22 June 2026, and `breakdowns=dma` stopped being supported in the Ads Insights API
Tier: T1 · Status: active
Marketing API out-of-cycle change dated 22 June 2026, read in full at source. Meta's wording: "Effective June 22, 2026, we are transitioning from Nielsen Designated Market Areas (DMAs) to Comscore Markets across ads targeting and reporting solutions. When requesting market-level data via the Ads Insights API, `breakdowns=dma` will no longer be supported; to retrieve market-level data, please instead use `breakdowns=comscore_market`."

**It is a change in both lanes, not just reporting.** The sentence says "across ads targeting and reporting solutions", so the market definitions available to target by changed on the same date as the ones available to report on.

**Why it earns a claim rather than a footnote.** Market-level reads are how a local advertiser answers "where is the money going", and our whole book is local: clinics in Collinsville and Novi, truck dealerships in New Jersey. **A market boundary is a measurement instrument, and the instrument was swapped mid-year.** Any geography series that spans 22 June 2026 is two different partitions of the map stitched together, and a market that appears to have grown or shrunk across that date may have changed definition rather than performance. Same class of error as comparing unequal windows: the number moved because the ruler moved.

**No crosswalk is published in the change note.** Meta links its help centre for what Comscore Markets are, and offers no mapping from DMA to Comscore Market, no count of markets under either scheme, and no guidance on comparing across the cut. So a pre-June against post-June market comparison cannot be reconciled from the platform's own documentation.

**Operating instruction.** Never compare a market-level Meta figure from before 22 June 2026 against one from after it without saying the market definition changed. If a client asks for a year-over-year view by market, the honest answer names the break.
Sources: Meta for Developers, 2026 Out-Of-Cycle Changes to Marketing API, entry dated 2026-06-22, read in full 2026-10-19
Last touched: 2026-10-19
"""

AT130 = """
### AT-130 · Google made a Search Lift study a QUERYABLE resource in Google Ads API v26, with 15 incrementality metrics and a lift config attached to the campaign
Tier: T1 · Status: active
Google Ads API v26, released 14 October 2026. Release notes and announcement post both read in full at source.

**What shipped.** A new read-only resource `SearchLiftKeywordBundle` representing a keyword bundle in a Search Lift study; two new selectable segments, `segments.search_lift_keyword_bundle` and `segments.search_property`; three new enums, `SearchLiftKeywordBundleStatus`, `SearchLiftMatchingInfoSource` and `SearchLiftSearchProperty`; and **15 new Search Lift metrics**, of which Google names `relative_search_lift`, `normalized_incremental_searches`, `search_lift_cost_micros` and `search_lift_impressions`. The study itself links to a campaign through the new field `Campaign.lift_measurement_config`.

**Why this is the most useful Google item of the month for us.** Everything this codex holds on incrementality has the same shape: the platform reports attributed conversions, and a real incremental read has to be built by hand as a holdout. Our own Demand Gen holdout at [[Google Auction & Smart Bidding#GA-068|GA-068]] found no lift, and building it was the work. **A lift study addressable from the reporting API is a different kind of instrument, because the counterfactual is maintained by the platform and the output is a column rather than a project.**

**The guard, and it is the one that applies to every platform-run lift study.** The experiment design, the control construction, the exposure definition and the significance treatment are all Google's, none of them appears in the release notes, and an advertiser querying `relative_search_lift` is reading a number whose construction it cannot inspect. That is strictly weaker than a holdout we run ourselves, where we own the split. **Treat a platform lift figure as the platform's estimate of its own effect until the methodology is published**, which is the caution this file already applies to every adopter-versus-non-adopter figure at [[Google Auction & Smart Bidding#GA-088|GA-088]].

**Note what it measures.** `normalized_incremental_searches` and `search_lift_impressions` are search-behaviour outcomes, not purchases or leads. A Search Lift study answers "did the advertising make more people search", which is an upper-funnel question. It is not a substitute for an incremental cost per lead.

**Eligibility is unstated.** Nothing in the release notes says which accounts or spend levels can run a Search Lift study, and lift studies on every other platform carry a spend floor. Our clients run four-figure monthly budgets, so the realistic expectation is that this is not available to them. **Worth one check before it is mentioned to anyone.**
Sources: Google Ads API release notes, v26 (2026-10-14), read in full; Google Ads Developer Blog, Announcing v26 of the Google Ads API, 2026-10-14, read in full via the Feedburner Atom content element
Last touched: 2026-10-19
"""

GA095 = """
### GA-095 · The Google Ads API moved to TWO releases a month from v26, while the support window and the four-majors-a-year rhythm stayed exactly as they were
Tier: T1 · Status: active
Google Ads Developer Blog, "Google Ads API Release and Sunset Schedules for 2026-2027", 12 October 2026, read in full at source including the whole 2026-2027 release table.

**What actually changed, and it is only the frequency.** "We are thrilled to accelerate our launch timelines even further, moving to two Google Ads API releases per month starting from version v26." Everything structural is explicitly unchanged: "We will still ship four major releases per year. All other releases will be minor releases that add only new, non-breaking features. Each major release will still be available for one year after the release. Sunset schedules are also unchanged, so you will not need to migrate more often. Each minor release sunsets together with its parent major version."

**The published schedule, for reference.** v26 major October 2026 sunsetting November 2027; v27 major January 2027; v28 major April 2027; v29 major July 2027; v30 major October 2027. Minors sit between them, roughly two a month, and Google marks the December instalments as ones it may skip because they fall in the holiday season. Sunsets for 2027: v23 February, v24 May, v25 August, v26 November. Google labels every date "estimated and subject to change" and says it may add or remove releases, or switch a release between major and minor.

**The stated reason, quoted because the framing is the news.** "As we enter a new agentic era where speed and agility are paramount", and "this faster cadence gives your automated agents and workflows near-instant access to cutting-edge features." Google is pacing its own API releases to how fast automated clients can consume them.

**The consequence that touches a human, and it is a monitoring consequence.** "Our release blog posts and YouTube live events will move to twice a quarter, covering key updates across several releases at once." **So the announcement channel gets SPARSER while the release channel gets denser, and the blog stops being a per-release alarm.** Google's own instruction is to watch the release notes page directly. This watchlist already reads that page weekly, which is now the right lane, and the blog is no longer sufficient on its own. That is the same failure shape already recorded for the Google Ads Announcements page, which does not carry Demand Gen drops: a source that looks like a superset of product news is not one.

**No performance content of any kind.** Nothing here says anything about delivery, bidding or auction behaviour. Banked as a monitoring and migration fact.
Sources: Google Ads Developer Blog, Google Ads API Release and Sunset Schedules for 2026-2027, 2026-10-12, read in full; confirmed against the v26 announcement post of 2026-10-14 and the release notes page
Last touched: 2026-10-19
"""

GA096 = """
### GA-096 · Google now names a BUDGET FLOOR in two places at once: a Search recommendation that says the daily budget is too low for performance, and a per-currency minimum daily budget for Demand Gen exposed in the API
Tier: T1 · Status: active
Both arrived in Google Ads API v26, 14 October 2026, release notes read in full at source.

**The Search recommendation.** New `RecommendationType.RAISE_BUDGET_PERFORMANCE_TOO_LOW`, with `Recommendation.raise_budget_performance_too_low_recommendation` and `ApplyRecommendationOperation.raise_budget_performance_too_low`, added "to support raising budgets when daily budgets are too low for Search campaigns."

**The Demand Gen floor.** New field `demand_gen_info.minimum_budget_per_day_micros` on `CurrencyConstant`, which "specifies the minimum required budget per day for Demand Gen campaigns in that currency. This field's value updates when the minimum budget enforced by the API changes."

**Why the pair is worth one claim.** This file already holds, from Google's own product manager, that Demand Gen explores creative only as far as the budget stretches and that budget per asset is the governing quantity ([[Google Auction & Smart Bidding#GA-091|GA-091]]). **These two fields are the first time Google has put a readable number behind that idea rather than leaving it to be inferred.** A minimum enforced daily budget is the cleanest possible statement that below some spend the channel does not function, which is an argument our own forecasting has had to make from first principles.

**The honest limits, both of them sharp.**

1. **Neither field publishes its threshold in the release note.** `minimum_budget_per_day_micros` is a field to query, not a figure Google states, so the actual floor for USD is unknown until somebody reads it off an account. **That read is one API call and it is the cheapest open item this run produced.**
2. **A raise-the-budget recommendation from the company selling the inventory is not evidence the raise pays.** It is the same class of object as every other Google recommendation, and [[Meta Delivery & Andromeda#MD-171|MD-171]] and [[Google Auction & Smart Bidding#GA-088|GA-088]] both record how adopter-versus-non-adopter recommendation figures are built. The recommendation tells us Google has a model of "too low". It tells us nothing about where profit sits.

**What it does not change.** Our scaling rules are unaffected. The step size and the gate at [[Scaling Models#SC-001|SC-001]] and [[Scaling Models#SC-176|SC-176]] govern raising a budget that is already working. A floor governs whether the channel is usable at all, which is a different question, asked before the first dollar.
Sources: Google Ads API release notes, v26 (2026-10-14), read in full; Google Ads Developer Blog, Announcing v26 of the Google Ads API, 2026-10-14, read in full
Last touched: 2026-10-19
"""

GP050 = """
### GP-050 · Local Services Performance Max became an externally creatable campaign type in October 2026, capped at ONE per account and welded to a single Google Business Profile listing
Tier: T1 · Status: active
Google Ads API v26, 14 October 2026, release notes read in full at source. This is a local-business campaign type and our entire book is local businesses, so it gets read closely.

**What changed mechanically.** `PmaxCampaignSettings.local_services_enabled` moved from `OUTPUT_ONLY` to `IMMUTABLE`, which means an external client can now set it to true when creating a campaign and can never change it afterwards. Two fields are required at creation: `LocalServicesPmaxCampaignSettings.country_code`, which v26 turned from optional into a hard requirement, and `LocalServicesPmaxCampaignSettings.listing_id`, which exposes "the Google Business Profile listing ID linked to the Local Services Performance Max campaign" and is marked REQUIRED at creation.

**The constraints, read off the new error codes, because the error list is where the real rules are.**

- `CampaignError.LOCAL_SERVICES_MULTIPLE_PERFORMANCE_MAX_CAMPAIGNS_NOT_ALLOWED`. **One Local Services PMax campaign per account.** That is a hard structural ceiling and it rules out the campaign-per-service or campaign-per-location structure a multi-service local business would otherwise want.
- `CampaignError.LOCAL_SERVICES_AGREEMENT_REQUIRED`. An agreement has to be accepted before the campaign can exist.
- `AssetSetLinkError.LOCATION_ASSET_DOES_NOT_MATCH_CAMPAIGN_LISTING_ID`. The location assets attached to the campaign must match the listing it was created against, so the campaign is tied to one Google Business Profile.
- `AssetGroupError.UNSUPPORTED_LOCAL_SERVICES_CATEGORY`. The category named in `AssetGroup.google_local_services_info` has to be on a supported list, and the list is not published in the release note.
- A family of goal errors: `CANNOT_UNLINK_LOCAL_SERVICES_GOAL_FROM_LOCAL_SERVICES_CAMPAIGN`, `GOAL_NOT_ALLOWED_FOR_LOCAL_SERVICES_CAMPAIGN`, `LOCAL_SERVICES_GOAL_NOT_ALLOWED_FOR_NON_LOCAL_SERVICES_CAMPAIGN` and `CANNOT_DISABLE_CAMPAIGN_OVERRIDE_GOALS_FOR_LOCAL_SERVICES_CAMPAIGN`. **The conversion goal is fixed to the Local Services goal and cannot be unlinked or overridden**, so the usual Performance Max freedom to choose and weight conversion goals is not available here.

**Lead plumbing arrived with it.** `LocalServicesLead.campaign` now links a lead to the campaign that produced it, which is the attribution join that was previously missing, and `COUPON` was added to `LocalServicesLeadType`.

**The operating read, stated honestly.** This is a plausible fit for a single-location service business with one Google Business Profile and one primary service, which describes a chiropractic clinic better than it describes a truck dealership selling several body types. **It is also a tightly bounded campaign type: one per account, one listing, a locked goal and an unpublished category list.** Nothing in the release notes says it performs, and no cost, lead-volume or comparison figure appears anywhere, so there is no basis here for recommending it over a standard Search campaign. The next step is a category-list check against the verticals we actually serve, not a build.
Sources: Google Ads API release notes, v26 (2026-10-14), read in full; Google Ads Developer Blog, Announcing v26 of the Google Ads API, 2026-10-14, read in full
Last touched: 2026-10-19
"""

append("Meta Delivery & Andromeda.md", MD182)
append("Meta Delivery & Andromeda.md", MD183)
append("Attribution & Incrementality.md", AT128)
append("Attribution & Incrementality.md", AT129)
append("Attribution & Incrementality.md", AT130)
append("Google Auction & Smart Bidding.md", GA095)
append("Google Auction & Smart Bidding.md", GA096)
append("Google PMax & Shopping.md", GP050)
print("done")
