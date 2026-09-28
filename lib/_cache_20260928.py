# -*- coding: utf-8 -*-
"""Write the 2026-09-28 page baselines into the watchlist cache (browser lane + Monday weekly lane)."""
import io, json

P = r"E:\claude code marketing skill\.claude\skills\advertising-science\cache\watchlist-seen.json"

SLUGS_US = ["agency-awards-2026", "introducing-meta-one-plans-for-businesses",
            "iab-global-creator-week-making-it-easier-for-businesses-to-partner-with-creators",
            "performance-spotlight-how-instant-hydration-built-a-system-for-ai-to-scale",
            "businesses-driving-results-with-meta-ai-ads", "sydney-sock-project-scaled-cause",
            "meta-ai-for-small-businesses", "game-changers-series-1", "laura-geller-creative-volume",
            "holiday-measurement-strategies", "holiday-advantage-is-creative-advantage",
            "skip-the-single-surface-holiday-strategy"]

SLUGS_UK = ["performance-spotlight-how-instant-hydration-built-a-system-for-ai-to-scale",
            "businesses-driving-results-with-meta-ai-ads", "closing-the-creator-measurement-gap",
            "2026-winning-hearts-boosting-carts", "conversations-2026-introducing-meta-business-agent",
            "social-search-series-2", "social-search-series-3", "social-search-series-1",
            "2026-trends-from-around-the-world",
            "meta-growth-drivers-putting-your-digital-marketing-strategy-on-auto-pilot",
            "cyber-5-2025-what-worked", "unlocking-the-value-of-q5marketing-for-mobile-game-developers"]

with io.open(P, encoding="utf-8") as f:
    d = json.load(f)

pages = d.setdefault("pages", {})


def setp(name, **kw):
    rec = pages.setdefault(name, {})
    rec.update(kw)


setp("meta-business-news",
     last_checked="2026-09-28",
     method="browser (playwright), BOTH locales, SLUG-set diff (title diff retired 2026-09-27)",
     result=("US 12 slugs, 0 new, 0 removed. UK 12 slugs, 0 new, 0 removed. "
             "Both slug sets identical to 2026-09-27. UK top card 11 September 2026, unchanged. "
             "US-to-UK ceiling gap unchanged."),
     slugs_us_2026_09_28=SLUGS_US,
     slugs_uk_2026_09_28=SLUGS_UK,
     note_2026_09_28=("FIRST RUN OF THE SLUG DIFF AND IT WORKED. Both shelves compared clean in one pass with "
                      "no capitalisation adjudication and no date-drift artefact to explain away. The method "
                      "change proposed on 2026-09-27 is confirmed; keep diffing slugs, not titles."))

setp("meta-ad-standards",
     last_checked="2026-09-28",
     method="browser (playwright), per-section SHA-256 body diff against the 2026-09-14 baseline",
     result=("UNCHANGED. All 16 section slices byte-identical to the 2026-09-14 baseline, "
             "including Restricted goods and services (6531 chars, 75a81517aee32a45) which carries "
             "Health and Wellness. Whole-page text 32,505 chars against a baseline 32,611."),
     note_2026_09_28=("TWO METHOD BUGS FOUND AND BOTH ARE IN THE BASELINE, NOT THE PAGE. (1) The baseline says "
                      "start the first search at offset 150. The page's leading chrome shrank by 106 characters, "
                      "so '1. Overview' now sits at offset 102 and the offset-150 start skips it, anchoring the "
                      "whole sequence on the FOOTER 'On this page' nav instead. Every section then hashed 12 to "
                      "74 chars of nav text and section 16 came back not-found, which looks exactly like a page "
                      "rewrite and is not one. FIX: anchor on the FIRST occurrence of 'Overview', or start at "
                      "offset 0. (2) Section 16 is rendered 'Transparency requirements under the EU Digital "
                      "Services Act'; the baseline stores the abbreviated 'EU DSA' and will never match. Its "
                      "slice to end-of-text is 2,983 chars, identical to baseline. The 106-char delta is entirely "
                      "header chrome."))

setp("meta-marketing-api-changelog",
     last_checked="2026-09-28",
     method="browser (playwright)",
     result=("No version change. Newest is still v26.0, 29 July 2026. v25.0 18 Feb 2026, "
             "v24.0 8 Oct 2025 with an Available Until of 6 October 2026."),
     note_2026_09_28=("TWO CHANGES TO THE SOURCE ITSELF. (1) THE URL MOVED. /docs/marketing-api/"
                      "marketing-api-changelog now redirects to /documentation/ads-commerce/marketing-api/"
                      "marketing-api-changelog. The watchlist URL still resolves through the redirect; update it. "
                      "(2) THE INDEX UNDER-RENDERING ARTEFACT DID NOT REPRODUCE. Recorded three times previously "
                      "(index showing only through v25.0), today the index renders v26.0, v25.0 and v24.0 with "
                      "dates in a table. Treat the artefact as fixed rather than latent, and re-open it if it "
                      "returns. Also newly visible: an out-of-cycle 05/04/2026 entry renaming Ads Management "
                      "Standard Access to Marketing API Access Tier, auto-approval threshold 1,500 down to 500 "
                      "calls per 15 days. Developer-access change, no effect on how we run accounts, not banked. "
                      "The page also now states ads in WhatsApp Status are available via the Marketing API, "
                      "which was followed to the doc and banked as EC-007."))

setp("meta-graph-api-changelog",
     last_checked="2026-09-28",
     method="browser (playwright)",
     result="No change. Newest is v26.0, consistent with the Marketing API changelog.")

setp("google-ads-api-release-notes",
     last_checked="2026-09-28",
     method="plain urllib plus browser (playwright) confirmation",
     result=("CHANGED. v25.2 (2026-09-23) is new since the 2026-09-07 check, which recorded v25.1 as newest. "
             "Read in full. Banked as GA-089 (tCPA/tROAS bid-too-low-to-enter-auctions recommendations), "
             "GA-090 (BenchmarksService percentile tiers) and GP-048 (GeneratePMaxDraftCampaign, asset-group "
             "URL options, automated video crawl setting)."))

setp("google-ads-developer-blog",
     last_checked="2026-09-28",
     method="feedburner Atom for titles and dates, plain urllib plus post-body div regex for the body",
     result=("ONE new post since the 2026-09-22 weekly check: 'Announcing v25.2 of the Google Ads API', "
             "2026-09-23. Body read in full on the first attempt through the urllib route. Banked."),
     note_2026_09_28="The urllib post-body route worked first try again. Third clean run of that route.")

setp("merchant-center-changelog",
     last_checked="2026-09-28",
     method="plain urllib plus browser (playwright), ORDINAL-AWARE date regex",
     result=("No change. Newest dated entry is 11 August 2026, 'Merchant Center performance reporting updates', "
             "already banked as GP-043."),
     note_2026_09_28=("THE 2026-09-22 'TRANSPORT ARTEFACT' CONCLUSION IS WRONG AND IS CORRECTED HERE. That note "
                      "recorded a plain fetch showing 15 July 2026 against a WebFetch showing 11 August 2026, "
                      "and called the older-looking result the artefact. It was never a transport difference. "
                      "The page renders that entry as 'August 11th, 2026' WITH AN ORDINAL SUFFIX, and the "
                      "Month D, YYYY regex cannot see it, so the scraper skipped straight to the next entry, "
                      "15 July. A real browser read produced the identical miss until the regex was widened. "
                      "This is the same ordinal-date bug the Watchlist already documents for Meta for Business "
                      "News ('13th October 2025'). FIX: every date regex in this lane must accept "
                      "(st|nd|rd|th)? and an optional comma. Never call a newest-entry date a rollback or a "
                      "transport artefact before re-reading with an ordinal-aware pattern."))

setp("ai-at-meta-blog",
     last_checked="2026-09-28",
     method="browser (playwright)",
     result=("No change and nothing in lane. Newest post 27 July 2026, 63 days flat. Same five visible posts "
             "as the 2026-09-07 check: assistive robotics, Genesis Mission, Muse Spark 1.1, Muse Image and "
             "Muse Video, Brain2Qwerty. Zero ads-ranking content."))

setp("demand-gen-drops-hub",
     last_checked="2026-09-28",
     note_2026_09_28=("Not fetched. Backlog closed 2026-09-26 and the Ads & Commerce RSS is the alarm; "
                      "RSS returned 0 new links today, so no new instalment exists to work."))

d["last_run"] = "2026-09-28T13:45 IST"

with io.open(P, "w", encoding="utf-8", newline="") as f:
    json.dump(d, f, indent=1, ensure_ascii=False)

print("cache written, pages:", len(pages))
