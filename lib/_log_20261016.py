# -*- coding: utf-8 -*-
"""2026-10-16: Watchlist.md notes + Harvest Log entry."""
from pathlib import Path

SCI = Path(r"E:\claude code marketing skill\Obsidian God-level Marketing Vault\God-level Marketing\wiki\science")

WATCH_NOTE = """

### Read and NOT banked: Google's Universal Cart, because the announcement has no advertiser in it (2026-10-16)

Google launched Universal Cart on 15 October 2026, US only, across Search and the Gemini app. Named participating merchants include Nike, Sephora, Target, Ulta Beauty, Walmart, Wayfair and Shopify merchants. It is built on the Shopping Graph, stated at 60 billion-plus product listings, and on something called the Universal Commerce Protocol. Checkout runs through Google Pay or passes through to the merchant.

**Read in full and deliberately not banked.** The post contains zero advertising content: no Shopping ads, no Performance Max, no Merchant Center requirement, no attribution or conversion-tracking change, no advertiser opt-in and no advertiser action. Same handling as *Launching Structured Data Files v11* on 2026-10-07: a real platform change with nothing in it for how an account is run. Recorded here so a future run does not re-read it.

**Why it is worth a note rather than silence.** A cart that lives on Google's surface and completes with Google Pay moves the purchase event off the merchant's site, and that is the sort of change that eventually arrives at Shopping attribution. **Nothing in the published post says it does, and this engine does not bank an inference.** The trigger to look again is an ads-side announcement that names Universal Cart, not another consumer post.

### Read and NOT banked: the Meta/YouGov APAC small-business AI survey (2026-10-16)

Meta Newsroom, 15 October 2026. YouGov on Meta's commission, 3,983 small business owners across nine APAC markets, fieldwork 6 August to 2 September 2026. Headline figures: 84% use AI, 76% report a positive productivity effect, 71% a positive revenue effect over twelve months, 86% say small businesses need more guidance.

**One advertising datum in it**, and it is self-reported usage rather than a mechanism: among owners whose business used AI in the past year, "51% have used it to create or edit content, 43% for local advertising and marketing, 38% for translation, and 37% for customer support."

**Not banked.** Stated behaviour from a vendor-commissioned attitude survey, no mechanism, no outcome measurement, and the piece then promotes Advantage+, click-to-WhatsApp ads and Meta Business Agent. The case study inside it (Zayya, Indonesia, 8x return on roughly $1.68 a day) is a named-advertiser showcase on Meta's own channel with no method, which is exactly what the AT-126 reading rule exists for. Logged so a future run does not re-read it.
"""

HARVEST_ENTRY = """## 2026-10-16 (research run)

**0 transcripts in, 4 claims added, 2 merges, 0 contested, 0 refuted, 0 errors. No law changed.** The YouTube roster published nothing, and the day's whole haul came off the watchlist: one Meta post that had gone unread for a day, and two arXiv papers.

**4 new claims.** [[Meta Delivery & Andromeda#MD-181|MD-181]] (T1), [[Attribution & Incrementality#AT-127|AT-127]] (T1), [[Auction Mechanics & Bidding#AU-099|AU-099]] (T2), [[Scaling Models#SC-177|SC-177]] (T4). **2 merges**, into [[Meta Delivery & Andromeda#MD-162|MD-162]] and [[Auction Mechanics & Bidding#AU-032|AU-032]].

**Meta opened a brand-reservation lane, and every number it published for it is a brand metric** ([[Meta Delivery & Andromeda#MD-181|MD-181]], T1). Three US products on one page. **Ads Super Burst** moves to general availability this month in phases: a bookable 3-to-24-hour window with category exclusivity, booked in Reach Planner with "guaranteed delivery tied to those estimates", reporting a median 2.9-point ad recall lift, a median 0.6-point intent lift and a median 34 million people per flight. **First Impression Ads**, the first ad in Feed on app open, one brand per day, in test in the United States only. **Reels Trending Ads** expanded to 15 always-on topics including Home & Garden and Spanish-language content, with custom audience exclusions "coming later in 2026", which means the product has been generally available with no way to exclude an existing-customer list. **Not one cost-per-result or conversion figure appears anywhere in the post**, and that absence is the finding: it is the exact shape [[Auction Mechanics & Bidding#AU-032|AU-032]] predicts for a reservation buy, so the 2026 product neither confirms nor refutes that T3 argument and the merge says so. **Guaranteed delivery is not guaranteed performance.** Nothing here is buyable at our budgets; banked as platform direction.

**A week-level attention objective, and a finding that cuts against how frequency gets argued** ([[Attribution & Incrementality#AT-127|AT-127]], T1). Meta is testing **Aggregated View Time** in alpha, which measures and optimises total time with a brand across a week instead of per impression, and it cites this: **"five seconds of attention added up over a week drove 32% more offline sales than one continuous five second view."** Same total exposure, spread, 32% more. If it holds, two accounts with identical total view time are not equivalent. Guards are heavy and the product is alpha: Meta measuring Meta, no sample, no vertical, no geography, no window, no control definition, and "offline sales" undefined. **No client on our book has an offline sales instrument, so this is not testable here as published.**

**The set is the unit a sponsored-search auction values, measured rather than argued** ([[Auction Mechanics & Bidding#AU-099|AU-099]], T2, arXiv 2610.20293). Exhaustive auction replay over 1,200 real requests with five ads returned each "reveals substantial coalition dependence": the contribution of any one ad depends materially on which others came back beside it, and for sets of four or more the per-ad attribution cannot be recovered from singleton, leave-one-out and full-set cases. Training on that dependence produced **"an observed 3.51% lift in the primary advertiser-value metric"** in a randomised seven-day production A/B test on 10% of traffic. Platform unnamed, so this is never documentation of Meta or Google, and the paper publishes its own failure case. **What it changes for us is a habit rather than a lever**: it gives an independent mechanism to the read-one-level-up rule already at [[Attribution & Incrementality#AT-087|AT-087]] and [[Attribution & Incrementality#AT-107|AT-107]].

**The first published automated media-buying loop, and its numbers come from a simulator** ([[Scaling Models#SC-177|SC-177]], T4, arXiv 2610.19454). Planner on account budget once per period, Optimizer on delivery every remaining timestep, Inspector diagnosing after settlement and feeding the next period's plan. Reported at "14.02%" more advertiser value and 7.07% lower cost per acquisition. **The evidence is the AuctionNet simulator, 3 controlled accounts, 12 ad units, 500,000 simulated opportunities per period, and the baseline it beats is a rule inside the same simulator.** Banked at T4 for exactly that reason, and banked at all because it is the first paper on this lane describing OUR side of the glass rather than the platform's. It also names a real gap of ours: the weekly report's diagnosis does not feed the next budget decision in any written form.

**Meta now quotes a second, different figure set for Reels trending ads** ([[Meta Delivery & Andromeda#MD-162|MD-162]] merge). Today: more than 5 percentage points of action intent versus control, and an incremental 5-point lift in unaided brand awareness. Banked in June: +20% total unaided awareness and +5.5 points of incremental ad recall. **Different measures, so not a contradiction and not contested**, but it is the second figure set for one product in four months and the newer one carries no method at all.

**Harvest: 0 new transcripts across 12 channels, 0 errors.** 3 uploads skipped as too short, 1 had no subtitles, 0 out of window. **8 of 12 channels needed the /videos-tab fallback** because YouTube's RSS endpoint returned 404 or 500, which is the known outage since 2026-09-05 and not a listing failure: every channel was listed. No extraction backlog. Summary at `runs/2026-10-16-0634-harvest.json`.

**Watchlist: 10 new items surfaced, 1 banked from, 9 read and discarded, zero errors.** Every discard was read, not assumed.

- **Meta for Business News read by hand on both locales**, which is the 2026-10-15 method fix working as intended. **US shelf 1 added 1 removed**: `meta-brand-building-summit-2026` in at slot 1, `laura-geller-creative-volume` out of slot 12, ceiling moves from 8 to 15 October. That one post is the whole of today's Meta haul. **UK shelf 0 added 0 removed and identical in order to yesterday.**
- **The UK alternation falsifier now has its first flat day and it survives at n=5.** Two consecutive daily reads exist for the first time since the gap opened, and the UK shelf did not move, so the head-of-list alternation seen on 10-08, 10-10, 10-12 and 10-15 is not a daily metronome. Still do not report it as holding.
- **Meta Engineering 3 new, all read, all 0 advertising content.** Forum built with AI-native engineering, 2026 World Cup traffic reliability, and the Sapienz ISSTA impact award. Zero occurrences of advertising, ads, campaign or auction in any of the three.
- **Meta Newsroom 2 new, both read, neither banked.** The AI-glasses art partnership with Milan's Pinacoteca di Brera, and the Meta/YouGov APAC small-business AI survey. The survey carries one advertising datum, 43% of AI-using owners used it for local advertising and marketing, on 3,983 owners across nine APAC markets, fieldwork 6 August to 2 September 2026. Stated behaviour from a vendor-commissioned attitude survey with no mechanism and no outcome, so not banked. Written up in [[Watchlist]].
- **Google Ads & Commerce 2 new, both read, neither banked, and one is a bigger launch than it looks.** Universal Cart went live 15 October, US, across Search and the Gemini app, with Nike, Sephora, Target, Ulta Beauty, Walmart, Wayfair and Shopify merchants, on a Shopping Graph of 60 billion-plus listings. **The post contains no advertising content at all**: no Shopping ads, no Performance Max, no Merchant Center requirement, no attribution change, no advertiser action. Same handling as SDF v11 on 7 October. The holiday when-to-buy guide is consumer guidance with no numbers in it. Both written up in [[Watchlist]] so a future run does not re-read them.
- **arXiv cs.IR 21 new in window, 2 passed the advertising filter, both read, both banked.** That is the first day in this lane's history with a 2-for-2 conversion.
- **Google Ads Announcements 396 answer IDs, identical to cache, 0 added 0 removed.** TikTok SDK changelog unchanged at 0.1.8.
- **Friday, so the 9 Monday-only weekly sources were not due** (last read 2026-10-12). The Demand Gen Drops Hub is not due either: read 2026-10-12 at 13 instalments, next expected around 24 October.
- **TikTok Newsroom and the TikTok for Business blog: not retried, permanent India geo-block.** Not an outage and not logged as one, per the 2026-10-15 correction.

**Law layer: untouched, and the one candidate was considered and declined.** [[Auction Mechanics & Bidding#AU-099|AU-099]] is a new T2 and it supports the standing law that judgement belongs at ad-set level rather than on the ad's own row. It does not change what that law tells anyone to do, and it carries no operating consequence for our accounts, so it stays in the codex and out of the hot layer. Nothing today refuted or contested anything.

**Gaps.**

1. **Oldest and still cheapest, now carried four days.** [[Scaling Models#SC-176|SC-176]] wants a new-audience and one-day-click read on Phoenix Truxx and SJR Commercial, and [[Meta Delivery & Andromeda#MD-180|MD-180]] has wanted a 30-day hour-of-day and day-of-week cost-per-result breakdown on the same two accounts since 14 October. Three claims, two accounts, mostly one column change. It has not moved.
2. **Dated, carried from 15 October.** Nobody has checked which client Google accounts have the Display Network or Search partners switched on inside a Search campaign, ahead of the February 2027 change at [[Google Auction & Smart Bidding#GA-094|GA-094]].
3. **New today, and it is ours rather than the codex's.** [[Scaling Models#SC-177|SC-177]] describes a diagnosis step that feeds the next period's budget plan. Our weekly report diagnoses and our budget calls decide, and nothing written connects the two. No claim fixes that; a habit would.
4. **New today, and probably worth ten minutes.** Spanish-language content is now an always-on Reels trending topic. Two clients sell to Spanish-speaking buyers. Nobody has checked whether the topic is reachable at a lead-gen objective or whether it is brand-reach only.
5. Still open from 14 October: nothing on file measures whether our results differ by buyer platform-activity, and no instrument has been named.
6. Codex hygiene unchanged and still deliberate. MD-103 and MD-141 stay near-duplicates, because collapsing them changes an ID other claims link to.

**Errors: none.** 12 channels listed clean, all six script lanes answered, both Meta Business News shelves read, 0 failures anywhere.

"""


def main():
    w = SCI / "Watchlist.md"
    s = w.read_text(encoding="utf-8")
    assert "Universal Cart" not in s, "watchlist note already present"
    w.write_text(s.rstrip("\n") + "\n" + WATCH_NOTE, encoding="utf-8")
    print("Watchlist.md +", len(WATCH_NOTE), "chars")

    h = SCI / "Harvest Log.md"
    s = h.read_text(encoding="utf-8")
    assert "## 2026-10-16" not in s, "harvest log entry already present"
    # newest-first log: find the first dated entry heading and insert above it
    i = s.find("## 2026-10-15")
    assert i > 0, "could not locate 2026-10-15 entry"
    s = s[:i] + HARVEST_ENTRY.lstrip("\n") + "\n" + s[i:]
    h.write_text(s, encoding="utf-8")
    print("Harvest Log.md +", len(HARVEST_ENTRY), "chars")


main()
