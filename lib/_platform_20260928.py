# -*- coding: utf-8 -*-
"""Platform claims banked by the 2026-09-28 research run (Monday weekly lane)."""
import io, os

SCI = r"E:\claude code marketing skill\Obsidian God-level Marketing Vault\God-level Marketing\wiki\science"


def append(p, block):
    fp = os.path.join(SCI, p)
    with io.open(fp, encoding="utf-8") as f:
        s = f.read()
    if not s.endswith("\n"):
        s += "\n"
    with io.open(fp, "w", encoding="utf-8", newline="") as f:
        f.write(s + block)
    print("appended to", p, "->", block.split("\n", 1)[0][:70])


append("Google Auction & Smart Bidding.md", u"""### GA-089 \u00b7 Google now ships a recommendation that names a tCPA or tROAS target as too low for a Search campaign TO ENTER AUCTIONS, and hands you the multiplier
Tier: T1 \u00b7 Status: active
Google Ads API v25.2, released 2026-09-23, adds two recommendation types and their apply operations. Release notes read in full at source 2026-09-28.

- `Recommendation.raise_target_cpa_performance_bid_too_low_recommendation` (enum `RAISE_TARGET_CPA_PERFORMANCE_BID_TOO_LOW`), applied through `RaiseTargetCpaPerformanceBidTooLowParameters.target_cpa_multiplier`.
- `Recommendation.lower_target_roas_performance_bid_too_low_recommendation` (enum `LOWER_TARGET_ROAS_PERFORMANCE_BID_TOO_LOW`), applied through `LowerTargetRoasPerformanceBidTooLowParameters.target_roas_multiplier`.

**Google's own words for what the two are for, and this is the load-bearing sentence:** "to support raising Target CPA or lowering Target ROAS when bids are too low for Search campaigns to **enter auctions**."

**Why this is worth banking rather than filing as an API note.** The failure it describes is not underdelivery, it is non-participation. A target set too aggressively does not buy fewer, cheaper conversions, it keeps the campaign out of the auction, which surfaces to an operator as a Search campaign that simply will not spend. That mechanic has been operator folklore for years. This is Google building a first-party detector for it, naming it in its own schema, and quantifying the gap.

**The quantification is the genuinely new part.** Each recommendation returns `recommended_target_multiplier`, greater than 1.0 for tCPA and less than 1.0 for tROAS, alongside `current_average_target_cpa_micros` or `current_average_target_roas`. So the system will state how far off the target is, as a factor, rather than only that it is off.

**Two limits, stated plainly.** Google does not publish the threshold, the lookback or the confidence behind the multiplier, so the number is a platform opinion and not a measurement we can audit. And it is a recommendation surface, which historically optimises toward spend; the direction of both recommendations is loosen the target. Read the multiplier as a useful diagnostic that a Search campaign is target-blocked rather than demand-blocked, and decide the size of the move yourself.
Sources: Google Ads API v25.2 release notes, developers.google.com/google-ads/api/docs/release-notes, read at source 2026-09-28; Google Ads Developer Blog, Announcing v25.2 of the Google Ads API, 2026-09-23, read in full 2026-09-28
Last touched: 2026-09-28
### GA-090 \u00b7 BenchmarksService now returns your PERCENTILE standing against all advertisers in a category, not only category averages
Tier: T1 \u00b7 Status: active
Google Ads API v25.2, 2026-09-23. `BenchmarksService.GenerateBenchmarksMetrics` gains `CustomerMetrics.percentile_metrics`, carrying `PercentileMetrics` and a `BenchmarksCustomerPercentileTier`, on both `GenerateBenchmarksMetricsResponse.customer_metrics` and `BreakdownMetrics.customer_metrics`.

**It is gated and the gate is easy to miss.** The field populates only when BOTH conditions hold in the request: `PERCENTILE_DATA` is in `supplemental_data`, AND `benchmarks_source` is set to `all_advertisers`, which itself requires a `category_filter`. Ask for it any other way and the field comes back empty with no error explaining why.

**Date coverage differs by metric family, and this is the part that will bite a reporting build.** Customer aggregate metrics, customer rate metrics and the new customer percentile metrics are supported across every date in `ListBenchmarksAvailableDatesResponse.supported_dates`, **including open quarters**. Customer share metrics and the benchmark source's own rate metrics (for example the average CPM of `/Apparel/Clothing` ads) are **not** supported for open quarters and are silently omitted from the response unless the requested range falls inside the narrower `supported_dates_for_all_metrics`. So a dashboard mixing percentile and share metrics over a current quarter will render half a table.

**Also added:** a dedicated `BenchmarksError.NO_METRICS_FOUND`, so an empty result is now distinguishable from a malformed request.

**What it is worth to us.** Competitive standing moves from an estimate we derive off the Ads Transparency Center to a first-party number Google will state. The caveat is the one that applies to every Google-supplied benchmark: the peer set is Google's category taxonomy, not our client's actual competitive set, so a percentile against `/Apparel/Clothing` is not a percentile against the four dealerships in the same county. Useful as a direction check, never as a client-facing scoreboard without saying whose peer group it is.
Sources: Google Ads API v25.2 release notes, developers.google.com/google-ads/api/docs/release-notes, read at source 2026-09-28
Last touched: 2026-09-28
""")

append("Google PMax & Shopping.md", u"""### GP-048 \u00b7 Google now converts a Smart campaign into a PAUSED PMax draft through the API, and PMax asset groups get their own URL options
Tier: T1 \u00b7 Status: active
Three PMax-relevant additions in Google Ads API v25.2, 2026-09-23, read at source 2026-09-28.

**1. Smart campaign to PMax, programmatically.** `SmartCampaignSettingService.GeneratePMaxDraftCampaign` generates a Performance Max draft from an existing Smart campaign. The draft arrives at `CampaignStatus.PAUSED` with `CampaignCreationStatus.INCOMPLETE`, so nothing goes live by accident. Setting `validate_only` to true returns validation warnings and conversion issues in `validated_info` without creating anything, which makes a dry run free. The response returns resource names for the generated `pmax_campaign`, `campaign_budget`, `asset_group` and assets. **Two options are not yet supported and error rather than degrade:** `gbp_enabled` and `image_enabled` must be left unset or false, or the call returns `SmartCampaignError.GBP_ENABLED_GENERATE_PMAX_NOT_SUPPORTED` or `IMAGE_ENABLED_GENERATE_PMAX_NOT_SUPPORTED`. For a local-service advertiser that is the significant gap, because Business Profile assets are usually the whole point of the Smart campaign being converted.

**2. URL options at the ASSET GROUP level.** `AssetGroup` gains `tracking_url_template`, `url_custom_parameters` and `final_url_suffix`. Until now those lived at campaign or account level for PMax, so every asset group in a campaign shared one tracking configuration. Per-asset-group tracking makes it possible to separate asset groups in downstream analytics without splitting them into separate campaigns, which is the usual workaround and the one that fragments the budget.

**3. Automated video crawl becomes a controllable setting.** `Campaign.AssetAutomationSetting` gains `AutomatedVideoCrawlSetting` with `AssetAutomationType.AUTOMATED_VIDEO_CRAWL`. Each `AutomatedVideoCrawlInfo` entry configures a crawl url, a `source_platform` (`LANDING_PAGE`, `SOCIAL` or `YOUTUBE`) and an `enabled` opt-in flag. So Google will pull video from a client's landing page, social profiles or YouTube channel to build PMax video assets, and the opt-in is now explicit and per-source. **Worth a deliberate decision on every PMax build rather than a default**, because `SOCIAL` points Google at content nobody briefed, approved or compliance-checked for use as an ad.
Sources: Google Ads API v25.2 release notes, developers.google.com/google-ads/api/docs/release-notes, read at source 2026-09-28; Google Ads Developer Blog, Announcing v25.2 of the Google Ads API, 2026-09-23, read in full 2026-09-28
Last touched: 2026-09-28
""")

append("Emerging Channels.md", u"""### EC-007 \u00b7 Ads in WhatsApp Status is live and it is a RIDER on Instagram Stories, with an exclusion list that rules out several of our verticals outright
Tier: T1 \u00b7 Status: active
Found on the Meta Marketing API changelog and read in full on the Ads in WhatsApp Status documentation, both at source 2026-09-28. The placement was not previously in this codex.

**What it is.** Ads inside WhatsApp Status, which is the 24-hour vertical feed separate from chats and calls. Single vertical image or video, 9:16, statuses run up to 60 minutes.

**It cannot be bought on its own.** The ad set must target both platforms and both positions together:
```
"publisher_platforms": ["instagram", "whatsapp"],
"instagram_positions": ["story"],
"whatsapp_positions": ["status"]
```
Meta states plainly that "standalone Status campaigns are not supported at this time." So this is incremental inventory attached to an Instagram Stories buy, not a channel you can isolate, and you cannot read its performance apart from Stories without Meta shipping a breakdown.

**The exclusions, and this is the part that decides whether it is relevant to a given client.**
- **Special ad categories are not eligible**: Finance, Employment, Housing, and Social Issues, Elections or Politics.
- **Sensitive verticals are excluded from delivery**: Pharma, Healthcare and GSI (gambling, state lotteries, alcohol and similar restricted categories).
- A/B testing, Dynamic Creative Optimization and Reach and Frequency buying are not compatible.
- Advantage+ Creative tools are not available on this placement.
- Collection and flexible format ads are not supported. Single image, single video and carousel up to 10 cards are.
- Available globally **except** the EU, UK, Iran, Cuba, Syria, Russia and North Korea.
- `wamo_whatsapp_identity_spec` cannot be updated on an existing creative; changing the identity means a new creative.

**Read against our book of business: this is not a lane for the chiropractic clients**, which sit inside Healthcare, and vehicle finance offers sit inside the Finance special ad category. It is available to the truck dealerships only where the ad does not carry a credit or financing offer.

**Objectives and optimisation goals Meta lists.** Awareness (reach, impressions, thruplay); Traffic, Leads and Sales (link clicks, reach, impressions, conversations, landing page views); Engagement, which is the only objective carrying **offsite conversions** in addition to the rest. Note the asymmetry: **`OUTCOME_LEADS` does not list offsite conversions**, so a conversion-optimised lead campaign cannot pick up this inventory under the Leads objective. Destinations are WhatsApp chat and website, and a WhatsApp Business Account is not required for the website destination.

**One targeting switch to make deliberately.** Because Meta does not hold an age for every WhatsApp user, ad sets carry a `user_age_unknown` flag. Opting in reaches those users and obliges the ad to be suitable for all ages. It is optional and reversible with `user_age_unknown: false`.
Sources: Meta, Ads in WhatsApp Status, developers.facebook.com/documentation/ads-commerce/marketing-api/ads-in-whatsapp-status, read in full 2026-09-28; Meta Marketing API changelog, read at source 2026-09-28
Last touched: 2026-09-28
""")

append("Learning & Signal.md", u"""### LS-083 \u00b7 A billion-user production ad platform refreshes user profiles WEEKLY and runs ONE shared compressed behaviour representation across tasks, because throughput forces it
Tier: T2 \u00b7 Status: active
arXiv 2609.31045, *KuaFu: Compressing Long User Behavior into Understanding at Billion Scale*, announced 2026-09-28. Abstract read in full. Tencent advertising and recommendation platform, ten months in production. T2 rather than T1: it is a deployment paper with reported production numbers rather than a platform doc, and none of the numbers is independently auditable.

**Three facts about how a large ad platform's user-understanding layer actually runs, and none of them is how an operator usually pictures it.**

1. **Profiles refresh on a schedule, not per impression.** The paper states the production load as a billion users weekly at roughly 100K queries per minute in aggregate. The user-understanding representation feeding downstream tasks is rebuilt on that cadence under a fixed GPU budget, which the authors call a hard throughput floor.
2. **The industry default they are replacing is one model per task**, where each task extracts its own subsequence from the full behaviour history and trains a dedicated model on it. Even after filtering, a single-task sequence stays at several hundred items per user, tens of thousands of tokens once serialised.
3. **Compression is not an optimisation, it is a precondition.** And crude compression corrupts the profile in four named ways: fabrication, omission, date misattribution and broken logic. Because there was no way to evaluate the compressed representation on its own, those errors previously surfaced only as diffuse degradation in downstream metrics.

**The reported results.** Matches or beats uncompressed single-task production models on all five headline metrics across four production profiling tasks, raises per-GPU throughput 37% to 350%, saves 190 GPUs, and over ten months in production lifted overall GMV by 1.37%.

**Why it belongs in this topic.** It is a direct observation about the resolution and latency of the user-side signal a modern ad system actually holds. A behavioural profile driving candidate selection is a weekly-refreshed compressed artefact, not a live read of what the user did an hour ago. That sets a floor on how fast a change in a person's behaviour can propagate into which ads they are shown, and it is the same architectural direction as Meta's move to unified representations.

**Two honest limits.** This is Tencent, not Meta or Google, so the cadence is evidence about what a platform at that scale finds economical rather than about our platforms specifically. And the paper is an infrastructure paper: it says nothing about auction mechanics, bidding or creative selection, and should not be stretched to.

**Filter note for the watchlist, recorded because it cuts against the pending rule.** This passed the arXiv bank-list filter on two `advertis` hits, both in framing sentences, the first and the last. That is the exact shape of the three recorded false positives, and it is a true positive. It is direct evidence against shipping the "discount a lone bank-list hit in the first or last sentence" rule as code.
Sources: arXiv 2609.31045, KuaFu: Compressing Long User Behavior into Understanding at Billion Scale, arxiv.org/abs/2609.31045, abstract read in full 2026-09-28
Last touched: 2026-09-28
""")

print("platform claims done")
