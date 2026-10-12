"""Watchlist cache writeback for the 2026-10-12 research run."""
import json
from pathlib import Path

SKILL = Path(r"E:\claude code marketing skill\.claude\skills\advertising-science")
P = SKILL / "cache" / "watchlist-seen.json"
d = json.loads(P.read_text(encoding="utf-8-sig"))
pages = d["pages"]

us = [
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
    "game-changers-series-1",
    "laura-geller-creative-volume",
]
uk = [
    "creator-marketing-whitepaper",
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
]

mb = pages["meta-business-news"]
mb["last_checked"] = "2026-10-12"
mb["slugs_us_2026_10_12"] = us
mb["slugs_uk_2026_10_12"] = uk
mb["result"] = (
    "US ceiling 8 Oct 2026, UK ceiling 6 Oct 2026. Both shelves 0 added 0 removed and "
    "IDENTICAL IN ORDER to the 2026-10-10 baseline, across a two-day gap (11 Oct not read)."
)
mb["note_2026_10_12"] = (
    "Both locales identical IN ORDER to slugs_us_2026_10_10 / slugs_uk_2026_10_10, over a TWO-day gap, because the "
    "2026-10-11 run did not complete. creator-marketing-whitepaper is still at UK slot 1. CONSEQUENCE: the one-day "
    "alternation falsifier named in the 2026-10-10 entry CANNOT be evaluated. It required an 11 October read. Today is "
    "consistent with BOTH live hypotheses (alternation with absent-11 then present-12, and no rotation at all since "
    "10 Oct) and distinguishes neither. Do not report the alternation as holding at five points. Transport: WebFetch on "
    "both locales, first attempt, EIGHTH consecutive browser-free read of both shelves, and a browser was available "
    "today and was not needed here."
)
mb["slugs_seen_cumulative"] = sorted(set(mb["slugs_seen_cumulative"]) | set(us) | set(uk))

secs = json.loads((SKILL / "cache" / "adstd-sections-2026-10-12.json").read_text(encoding="utf-8"))
ads = pages["meta-ad-standards"]
ads["last_checked"] = "2026-10-12"
ads["method"] = (
    "browser (playwright) browser_evaluate returning document.body.innerText, per-section SHA-256 on the offset-0 anchor"
)
ads["result"] = (
    "UNCHANGED, and this CLOSES the hash-lane gap the 2026-10-07 entry opened. Whole-page innerText 32,505 chars, "
    "exactly the 2026-09-28 figure. All 16 sections located, none not-found. Restricted goods and services 6,531 chars "
    "and sha256 75a81517aee32a45, byte-identical to the 2026-09-14 baseline and the 2026-09-28 reconfirmation. "
    "Health and Wellness and Privacy Violations and Personal Attributes both PRESENT. The hash lane had been undiffed "
    "for 14 days."
)
ads["section_map_2026_10_12"] = secs
ads["note_2026_10_12"] = (
    "METHOD. The 2026-09-28 offset-0 anchor fix works and is now confirmed on a second run: all 16 headings resolve in "
    "order with zero not-found. NEW FINDING, WebFetch and the browser DISAGREE on this page's heading list and the "
    "browser is right. WebFetch returned Introduction to the Advertising Standards as item 1 and omitted Overview "
    "entirely, which reads exactly like a rename of section 1 and is not one. The browser innerText carries both, with "
    "Overview as section 1 at 958 chars and the Introduction string as the H1, which confirms the 2026-09-07 amendment. "
    "So the heading check is browser-optional only if you accept a 1-off list; a correct heading list and the hash check "
    "both need the browser."
)

pages["google-ads-api-release-notes"].update({
    "last_checked": "2026-10-12",
    "method": "plain fetch; version-heading set. DO NOT trust a raw byte diff on this host.",
    "result": (
        "UNCHANGED. Top version still v25.2, the same as the 2026-09-28 read. The weekly script reported changed=true; "
        "that is nonce noise, see note."
    ),
    "note_2026_10_12": (
        "PER-RENDER NONCE CONFIRMED ON THIS PAGE. Two fetches taken seconds apart differ in exactly two places: the "
        "script nonce attribute value, and the key order inside the inline analytics JSON blob. Byte counts went 366,207 "
        "then 366,203. So the weekly script changed=true flag is MEANINGLESS on developers.google.com and has probably "
        "been firing falsely since it was written. Same defect already documented on the Google Ads Announcements page, "
        "where added=1/removed=1 fired on a response nonce. FIX, same shape as the announcements lane: diff a stable key, "
        "here the version-heading set, never the raw body."
    ),
})

pages["merchant-center-changelog"].update({
    "last_checked": "2026-10-12",
    "method": "plain fetch; entry dates are BARE date lines only, never a date embedded in prose",
    "result": (
        "UNCHANGED. Newest entry is still Loyalty program updates: Loyalty Customer Match via Merchant API, "
        "24 September 2026, the same as the 2026-10-07 read. 72 dated entries parsed."
    ),
    "note_2026_10_12": (
        "QUALIFIES THE 2026-10-07 take-the-max-over-parsed-dates RULE FOR THIS SOURCE. A max over ALL parsed dates returns "
        "September 30, 2026, which is NOT an entry date. It is a sub-heading, Changes beginning September 30, 2026, INSIDE "
        "the 28 April 2026 entry about pickup cost and minimum order values in the UK, Switzerland and the EEA. A "
        "forward-looking compliance deadline, not a publication. QUALIFIER: on this source only count dates that stand "
        "ALONE on their own line. The max-over-dates instinct is still right; the eligibility of the dates was wrong. "
        "Page order is not date order at EITHER end: 11 August 2026 renders first and the two genuinely newest entries, "
        "1 July 2026 and 24 September 2026, render LAST."
    ),
})

pages["google-ads-developer-blog"].update({
    "last_checked": "2026-10-12",
    "method": "feedburner Atom for titles and dates, raw urllib plus post-body regex for the body",
    "result": (
        "ONE new post since the 2026-09-28 weekly read: Launching Structured Data Files v11, 8 October 2026. Read IN FULL "
        "via the urllib route. DELIBERATELY NOT BANKED, Display and Video 360 only."
    ),
    "note_2026_10_12": (
        "WebFetch returned the post chrome with no article body AGAIN, the documented failure on this host; the raw urllib "
        "plus post-body regex route worked first try, fourth clean run of that route. CONTENT, recorded so a future run "
        "does not re-read it: SDF v11 general availability for download and upload in the DV360 interface. Lookalike "
        "audience inclusion and exclusion targeting extended to all ad groups except those under YouTube Ad Sequence line "
        "items; Business Chain proximity targeting added to the line item file format; four YouTube third-party vendor "
        "columns reformatted to carry reporting IDs and multiple vendor assignments, with the now-redundant reporting-ID "
        "columns removed; new columns, column options and restrictions for YouTube Instant Deal line items, beta and "
        "allowlisted partners only, excluded from all downloads. Versions earlier than v10 sunset January 2027. ZERO "
        "Google Ads Search, Shopping or Performance Max content, and no delivery, auction or measurement mechanism. "
        "No client on our book runs DV360."
    ),
})

pages["meta-graph-api-changelog"].update({
    "last_checked": "2026-10-12",
    "method": "WebFetch",
    "result": "UNCHANGED. Newest v26.0, released 29 July 2026. 14 versions listed.",
})

mapi = pages["meta-marketing-api-changelog"]
mapi["last_checked"] = "2026-10-12"
mapi["result"] = (
    "Index UNDER-RENDERED to v25.0 AGAIN, third observation. Lists only v25.0 (18 Feb 2026, presented as newest), v24.0 "
    "and v23.0, and states that the latest Graph API version is v25.0. True newest is v26.0, 29 July 2026, confirmed on "
    "the Graph API changelog in the same session. The 2026-09-28 treat-it-as-fixed stays withdrawn."
)
mapi["note_2026_10_12"] = (
    "v24.0 Available Until is rendered as 6 October 2026 and that date has now passed. The 2026-09-28 entry flagged it "
    "eight days out and the 2026-10-07 entry recorded it as one day past. No action for us: no client integration pins a "
    "Marketing API version."
)

pages["ai-at-meta-blog"].update({
    "last_checked": "2026-10-12",
    "method": "WebFetch",
    "result": (
        "UNCHANGED and nothing in lane. Newest post 27 July 2026, now 77 days flat. Same five visible posts as the "
        "2026-09-07, 2026-09-28 and 2026-10-07 checks. Zero advertising, ranking or measurement content. The listing "
        "still renders OUT of date order, 9 July first and 27 July third."
    ),
})

pages["demand-gen-drops-hub"].update({
    "last_checked": "2026-10-12",
    "method": (
        "plain fetch HTTP 200; count the Demand Gen Drop card lines. The 2026-09-26 Social Module to Return to top of "
        "page anchors NO LONGER RENDER."
    ),
    "result": (
        "UNCHANGED. 13 instalment cards, newest September 2026, identical to the 2026-10-10 read. No October drop yet; "
        "expected around 24 October."
    ),
    "note_2026_10_12": (
        "Read directly again because the Ads and Commerce RSS alarm is now 11 days stale, feed build 1 October. Neither "
        "cached text anchor appears in today's render and the page carries ZERO parseable dates, so the card count is the "
        "only stable key. The 13 cards are Sep, Aug, Jul, Jun, May (rendered as Fuel your next wave of growth on YouTube "
        "with Demand Gen), Apr, Mar, Feb, Jan, Dec, Nov, Oct and the intro."
    ),
})

pages["tiktok-newsroom"]["note_2026_10_12"] = (
    "NOT retried. A Playwright browser WAS available today and was deliberately not spent here: the India geo-block was "
    "verified 2026-08-19 across the browser and curl on four paths each, and a browser does not move an egress. "
    "Not an outage."
)
pages["tiktok-business-blog"]["note_2026_10_12"] = (
    "NOT retried, same reason as tiktok-newsroom. Known permanent blind spot."
)

d["last_run"] = "2026-10-12T13:05 IST"
P.write_text(json.dumps(d, indent=2), encoding="utf-8")
print("watchlist-seen.json updated")
print("cumulative slug set now:", len(mb["slugs_seen_cumulative"]))
print("ad-standards sections recorded:", len(secs))
