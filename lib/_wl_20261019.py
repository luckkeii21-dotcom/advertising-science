# -*- coding: utf-8 -*-
"""Watchlist cache writeback for the 2026-10-19 research run (Monday, weekly lane ran)."""
import json
from pathlib import Path

SKILL = Path(r"E:\claude code marketing skill\.claude\skills\advertising-science")
P = SKILL / "cache" / "watchlist-seen.json"
d = json.loads(P.read_text(encoding="utf-8-sig"))
pages = d["pages"]

us = [
    "meta-nest-ai-creative-diversification",
    "meta-brand-building-summit-2026",
    "muse-smb-bennett-orchards",
    "a-new-way-for-businesses-and-personal-agents-to-work-together",
    "advertising-week-new-york-2026",
    "agency-awards-2026",
    "introducing-meta-one-plans-for-businesses",
    "iab-global-creator-week-making-it-easier-for-businesses-to-partner-with-creators",
    "performance-spotlight-how-instant-hydration-built-a-system-for-ai-to-scale",
    "businesses-driving-results-with-meta-ai-ads",
    "sydney-sock-project-scaled-cause",
    "meta-ai-for-small-businesses",
]
uk = [
    "performance-spotlight-how-instant-hydration-built-a-system-for-ai-to-scale",
    "businesses-driving-results-with-meta-ai-ads",
    "closing-the-creator-measurement-gap",
    "2026-winning-hearts-boosting-carts",
    "conversations-2026-introducing-meta-business-agent",
    "social-search-series-2",
    "social-search-series-3",
    "social-search-series-1",
    "2026-trends-from-around-the-world",
    "meta-growth-drivers-putting-your-digital-marketing-strategy-on-auto-pilot",
    "cyber-5-2025-what-worked",
    "unlocking-the-value-of-q5marketing-for-mobile-game-developers",
]

mb = pages["meta-business-news"]
mb["last_checked"] = "2026-10-19"
mb["slugs_us_2026_10_19"] = us
mb["slugs_uk_2026_10_19"] = uk
mb["result"] = (
    "Both shelves 0 added 0 removed, identical in content AND order to the 2026-10-18 read. US ceiling "
    "19 October 2026, UK ceiling 10 September 2026."
)
mb["note_2026_10_19"] = (
    "The 2026-10-18 future-date refinement is CONFIRMED and now closed. meta-nest-ai-creative-diversification "
    "read 19 October on 17 Oct (two days ahead), 19 October on 18 Oct (one day ahead) and 19 October today "
    "(the date itself). The card date never moved while the clock closed on it, so it is a FIXED published "
    "date, not a render offset, and a future-dated card is read once and left alone. Third consecutive flat "
    "day on both shelves. Transport: WebFetch on ?locale=en_US and ?locale=en_GB, hrefs requested rather than "
    "titles, first attempt each, THIRTEENTH consecutive browser-free read of both shelves. A browser WAS "
    "available today and was used for the Meta weekly lane, not here. The bare URL was not read."
)
mb["slugs_seen_cumulative"] = sorted(set(mb["slugs_seen_cumulative"]) | set(us) | set(uk))

ads = pages["meta-ad-standards"]
ads["last_checked"] = "2026-10-19"
ads["method"] = (
    "browser (playwright) browser_evaluate on document.body.innerText, per-section SHA-256. The anchor scan "
    "is SEQUENTIAL, each heading searched from the end of the previous match; a literal indexOf from position "
    "0 is WRONG because Community Standards occurs 20 times. Read BOTH locales, and match headings "
    "CASE-INSENSITIVELY with hyphens optional: the UK page is sentence case."
)
ads["result"] = (
    "UNCHANGED on both locales. US: 32,505 chars, exactly the 2026-09-28 and 2026-10-12 figure, all 16 "
    "sections byte-identical to the 2026-10-12 hashes. UK: 33,587 chars, all 16 sections located, zero "
    "not-found, Health and Wellness and Privacy violations and personal attributes both present. First UK "
    "section map ever recorded."
)
ads["section_map_uk_2026_10_19"] = {
    "Overview": "969|645d4907aa95f6d2",
    "Meta advertising policy principles": "3613|c448fb4223c53aa9",
    "The ad review process": "1912|7684d7a75f715a3e",
    "What to do if your ad is rejected or if your business asset is restricted": "488|80241eca7c262b04",
    "Community Standards": "175|9343a2c3441eaf6b",
    "Unacceptable content": "3786|5feccddda1041534",
    "Prohibited commercial practices": "199|8a32e4398761032b",
    "Restricted goods and services": "6537|d7bd566f08db2a23",
    "Objectionable content": "2464|2658162ac50a5729",
    "Intellectual property infringement": "866|cc4e906134567839",
    "Social issue, electoral or political advertising": "556|375cd36a44373eb9",
    "Product- and format-specific policies": "2089|62a2b167f0c68ca4",
    "Advertising policies affecting business assets": "1401|4306348e70b03aa5",
    "Data use restrictions": "1246|74731ffb86e6e1a5",
    "Things you should know": "3181|054db5e85f954f48",
    "Transparency requirements under the EU Digital Services Act": "4003|6eb8afbfab743a03",
}
ads["note_2026_10_19"] = (
    "FALSE-ALARM CLASS FOUND AND CLOSED. The UK locale renders section titles in SENTENCE CASE with different "
    "hyphenation: Prohibited commercial practices, Product- and format-specific policies, Privacy violations "
    "and personal attributes. A case-sensitive run of the US heading list against the UK page reported "
    "Product and format-specific policies NOT-FOUND and the personal-attributes section ABSENT. Neither is "
    "absent. That would have produced a policy-removal finding on the exact section ChiroWorks and Chiropraise "
    "run against. Match case-insensitively, hyphens optional. Also: Prohibited commercial practices is 199 "
    "chars in BOTH locales, so the MD-156 rename of 2026-09-14 has propagated to both and the locale-staging "
    "concern for that section is resolved."
)

pages["meta-marketing-api-changelog"].update({
    "last_checked": "2026-10-19",
    "url": "https://developers.facebook.com/documentation/ads-commerce/marketing-api/marketing-api-changelog",
    "method": "browser; the old /docs/marketing-api/ URL redirects to the new /documentation/ads-commerce/ path",
    "result": (
        "DEFECT CLOSED. The page MOVED and now renders correctly: latest version stated as v26.0, with v26.0 "
        "(29 Jul 2026), v25.0 (18 Feb 2026) and v24.0 (8 Oct 2025) listed. The index-under-renders-to-v25.0 "
        "defect recorded since 2026-08-24 and re-observed 09-28, 10-07 and 10-12 is gone."
    ),
    "note_2026_10_19": (
        "TWO THINGS BEYOND THE FIX. (1) Available Until dates MOVED FORWARD after passing: v24.0 was 6 October "
        "2026, a date tracked as passed across three runs, and now reads 10 November 2026; v25.0 went from TBD "
        "to 23 February 2027. So a passed Marketing API sunset date can be EXTENDED and must never be reported "
        "as a shutdown. (2) The new page exposes a per-year OUT-OF-CYCLE CHANGES shelf (occ-2023, occ-2024, "
        "occ-2025, occ-2026) that nothing on this watchlist pointed at. occ-2026 is 20 entries, 17 Feb to 22 Oct "
        "2026, read IN FULL today and the source of 5 of the day's 8 claims. occ-2023/24/25 are UNREAD."
    ),
})

pages.setdefault("meta-occ-shelf", {}).update({
    "url": "https://developers.facebook.com/documentation/ads-commerce/marketing-api/out-of-cycle-changes/occ-2026",
    "added": "2026-10-19",
    "check": "Weekly (Mon)",
    "method": "browser; document.body.innerText, entries are date-headed, newest first",
    "last_checked": "2026-10-19",
    "result": (
        "FIRST READ. 20 entries, 17 February to 22 October 2026, all read in full. Banked: MD-182 (creative "
        "audience pairing, 14 Oct), MD-183 (Image Animation, Video Filter, Video Uncrop 28 Jun, IG Audio Swap "
        "1 Jun), AT-128 (Insights breakdown gating, 8 May effective 6 Aug), AT-129 (DMA to Comscore Markets, "
        "22 Jun). Read and DELIBERATELY NOT BANKED, no client on our book runs them: Threads ads (17 Feb, "
        "25 Mar, 21 Apr), partnership ads account-level permissioning and ad codes (30 Mar), audience_labels on "
        "custom audiences (30 Apr), Creator Marketplace filter expansion (11 Jun), WhatsApp marketing messages "
        "(13 Aug), video ads in Instagram search results via the ig_search placement (6 Oct), is_pca_unified on "
        "campaign groups (22 Oct). Also noted and not banked: the Marketing API Access Tier rename of 4 May 2026 "
        "lowered the auto-approval threshold from 1,500 to 500 calls in 15 days, moved the error-rate test to a "
        "rolling 500-request window under 15%, and dropped the screen-recording requirement; that governs our "
        "own tooling rather than advertising mechanics. And the lift_estimate field in the recommendation object "
        "changed data source on 4 May 2026 for a subset of campaigns, which is one more reason a platform "
        "recommendation's own lift number is not comparable across campaigns (see MD-171)."
    ),
    "note_2026_10_19": (
        "The shelf declares itself Updated: Oct 22, 2026, three days ahead of the clock, and its newest entry "
        "carries the same date. Per the 2026-10-18 rule a future date on a Meta property is a fixed publication "
        "date, so read once and do not re-read daily. BACKLOG: occ-2025, occ-2024 and occ-2023 are unread, "
        "three years of T1 Meta platform documentation. Fourth instance of the ceiling-check-misses-the-shelf "
        "failure shape after Meta business news 09-20 and 09-23 and the Demand Gen hub 09-25."
    ),
})

pages["meta-graph-api-changelog"].update({
    "last_checked": "2026-10-19",
    "method": "browser",
    "result": "UNCHANGED. Newest v26.0, 29 July 2026. 14 Graph API versions listed, identical to 2026-10-12.",
})

pages["google-ads-api-release-notes"].update({
    "last_checked": "2026-10-19",
    "method": "plain fetch; VERSION-HEADING set. Never trust a raw byte diff on this host.",
    "result": (
        "CHANGED, and it is real. Headings went from [v25, v24, v23, v22] on 2026-10-12 to [Release summary and "
        "quick links, v26 major version, v25, v24, v23] today. v26 released 2026-10-14, v22 moved to archive. "
        "The v26 section was read in full and produced AT-130, GA-096 and GP-050."
    ),
    "note_2026_10_19": (
        "FIRST REAL CHANGE CAUGHT BY THE VERSION-HEADING KEY, which validates the 2026-10-12 fix. The raw byte "
        "count also moved, 371,961 to 376,334, but it moves on every render because of the script nonce and "
        "means nothing on its own."
    ),
})

pages["google-ads-developer-blog"].update({
    "last_checked": "2026-10-19",
    "method": (
        "Feedburner Atom for titles, dates AND BODIES. The <content> element carries each post in full; the "
        "urllib plus post-body regex route of 2026-09-07 is no longer needed."
    ),
    "result": (
        "TWO new posts since the 2026-10-12 weekly read, both read in full from the feed on the first attempt: "
        "Google Ads API Release and Sunset Schedules for 2026-2027 (2026-10-12, banked GA-095 including the "
        "whole release and sunset table) and Announcing v26 of the Google Ads API (2026-10-14, corroborates "
        "AT-130, GA-096 and GP-050)."
    ),
    "note_2026_10_19": (
        "METHOD RETIRED AND REPLACED. Two notes in Watchlist.md are about failing to extract a Developer Blog "
        "post body: WebFetch returns the chrome without the article (2026-08-31, cost GA-069 its source) and "
        "the urllib post-body regex returned nothing on one 2026-09-10 permalink (2026-09-22, that post still "
        "unread). Neither route is necessary. The Feedburner feed carries the FULL body inside <content>, "
        "including complete tables. 25 entries in the feed, roughly a two-month window; only fetch a permalink "
        "for a post older than that. The 2026-09-22 unread post may be recoverable this way."
    ),
})

pages["merchant-center-changelog"].update({
    "last_checked": "2026-10-19",
    "method": "plain fetch; /merchants/answer/(\\d+) id SET diff, a better key than the bare entry dates",
    "result": "UNCHANGED. 79 answer ids, 0 added, 0 removed against the 2026-10-12 cache.",
})

pages["ai-at-meta-blog"].update({
    "last_checked": "2026-10-19",
    "method": "browser",
    "result": (
        "UNCHANGED and nothing in lane. Newest post 27 July 2026, now 84 days flat. Same five visible posts as "
        "the 2026-09-07, 09-28, 10-07 and 10-12 checks. Zero advertising, ranking or measurement content. "
        "Listing still renders out of date order."
    ),
})

pages["demand-gen-drops-hub"].update({
    "last_checked": "2026-10-19",
    "method": "plain fetch HTTP 200; count the Demand Gen Drop card headings",
    "result": (
        "UNCHANGED. 13 instalment cards, newest September 2026, identical to the 2026-10-12 read. No October "
        "drop yet; expected around 24 October."
    ),
})

pages["tiktok-newsroom"]["note_2026_10_19"] = (
    "NOT retried. A Playwright browser was available and was deliberately not spent here. The India geo-block "
    "was verified 2026-08-19 across the browser and curl on four paths each, and a browser does not move an "
    "egress. Not an outage."
)
pages["tiktok-business-blog"]["note_2026_10_19"] = (
    "NOT retried, same reason as tiktok-newsroom. Known permanent blind spot."
)

d["last_run"] = "2026-10-19T04:05 IST"
P.write_text(json.dumps(d, indent=2), encoding="utf-8")
print("watchlist-seen.json updated")
print("cumulative slug set now:", len(mb["slugs_seen_cumulative"]))
print("last_run:", d["last_run"])
