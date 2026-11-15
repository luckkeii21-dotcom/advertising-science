# -*- coding: utf-8 -*-
import io, json, os, time

P = r"E:\claude code marketing skill\.claude\skills\advertising-science\cache\watchlist-seen.json"
d = json.load(io.open(P, encoding="utf-8"))
p = d["pages"]["meta-business-news"]

us = ["from-measurement-to-capital-allocation",
      "finding-his-squad-again-in-a-facebook-group",
      "how-metas-ads-system-matches-your-ad-to-the-right-person",
      "three-new-ai-innovations-in-ads-ranking",
      "you-dont-beat-the-auction-you-brief-it",
      "muse-smb-jaeluxe-shoetique",
      "agencies-testing-incrementality",
      "meta-nest-ai-creative-diversification",
      "meta-brand-building-summit-2026",
      "muse-smb-bennett-orchards",
      "a-new-way-for-businesses-and-personal-agents-to-work-together",
      "advertising-week-new-york-2026"]
uk = ["meta-ai-now-available-in-hongkong",
      "meta-agency-first-awards-winners-hongkong-2026",
      "meta-marketing-summit-hongkong-2026",
      "you-dont-beat-the-auction-you-brief-it",
      "performance-spotlight-how-instant-hydration-built-a-system-for-ai-to-scale",
      "businesses-driving-results-with-meta-ai-ads",
      "closing-the-creator-measurement-gap",
      "2026-winning-hearts-boosting-carts",
      "conversations-2026-introducing-meta-business-agent",
      "social-search-series-2",
      "social-search-series-3",
      "social-search-series-1"]

p["slugs_us_2026_11_15"] = us
p["slugs_uk_2026_11_15"] = uk
p["last_checked"] = "2026-11-15"
p["method"] = ("Plain fetch not attempted; read through WebFetch on ?locale=en_US and the "
               "en-gb host, the two pinned URLs. SLUG set diff against "
               "slugs_seen_cumulative (41, unchanged today).")
p["result_2026_11_15"] = (
    "2026-11-15 (Sunday): BOTH shelves FLAT. US 12 slugs, identical in SET AND ORDER to "
    "slugs_us_2026_11_13, ceiling 12 November 2026. UK 12 slugs, identical in SET AND ORDER to "
    "slugs_uk_2026_11_13 and to 8 earlier saved reads, ceiling 27 October 2026. 0 added, 0 removed "
    "on each. 0 of the 24 slugs absent from slugs_seen_cumulative, which stays at 41. No 2026-11-14 "
    "read exists (no run fired), so this read covers two days. UK remains 5 distinct ordered states "
    "across 33 saved reads, so the 2026-11-10 finding that UK movement is request-level variance "
    "still holds.")
p["note_2026_11_15_link_extraction"] = (
    "The 2026-11-13 method change (extract every outbound /business/news/ link from any post read "
    "and diff it against slugs_seen_cumulative) had NOTHING TO ACT ON today, because zero new posts "
    "entered either shelf. The method is still only in this cache note and not in "
    "lib/watchlist_check.py, so it remains dependent on whoever runs the pass. Standing gap.")
p["note_2026_11_15_gap_closed"] = (
    "THE SUITE OF TRUTH REPORT IS READ AND THE GAP IS CLOSED. The report named at AT-138 and carried "
    "as the top Harvest Log gap since 2026-11-13, facebook.com/business/f/1094917955782254, is "
    "UNGATED: a plain GET 302s to a scontent PDF, 20 pages, 6,416,093 bytes, no form and no login. "
    "Downloaded to cache/meta-suite-of-truth-20261115.pdf, text at "
    "cache/meta-suite-of-truth-20261115.txt, read in full. Banked AT-139 to AT-145. It DOES carry "
    "the missing magnitude (31% median undervaluation, 1.45X minimum multiplier, 307 studies by 54 "
    "advertisers) and it does NOT carry the missing test-design parameters (no holdout size, no "
    "minimum detectable effect, no confidence interval). Do not re-read it.")

fe = d.setdefault("feeds", {})
me = fe.get("meta-engineering", {})
if isinstance(me, dict):
    me["note_2026_11_15_discard"] = (
        "cuttlefish-on-mac (engineering.fb.com, 2026-11-13) was the one new feed item of the day. "
        "READ IN FULL AND DELIBERATELY NOT BANKED: Reality Labs porting Android's Cuttlefish virtual "
        "device framework to macOS on Apple silicon. Zero advertising content, no ranking, no "
        "delivery, no auction, no measurement. Same handling as the Google Structured Data Files "
        "post on 2026-10-07. Recorded so a future run does not re-read it.")
    fe["meta-engineering"] = me

ax = fe.get("arxiv-cs-ir", {})
if isinstance(ax, dict):
    ax["note_2026_11_15_api_backfill"] = (
        "RSS served an EMPTY cs.IR build (lastBuildDate Sun 15 Nov 05:00 UTC), the documented "
        "weekend state. Backfilled through export.arxiv.org/api/query, cat:cs.IR, "
        "sortBy=submittedDate, 250 most recent, cached at cache/arxiv-api-csir-20261115.xml. "
        "NEWEST SUBMISSION IN THE WHOLE INDEX IS 2026-11-12, so arXiv has published no cs.IR "
        "submissions on 13, 14 or 15 November. 29 submissions dated 11 and 12 November, 0 passed "
        "the bank-list filter. Histogram: 12 Nov 16, 11 Nov 13, 10 Nov 14, 9 Nov 15, 8 Nov 8, "
        "7 Nov 16, 6 Nov 13, 5 Nov 20. No window lost.")
    fe["arxiv-cs-ir"] = ax

d["last_run"] = "2026-11-15"
io.open(P, "w", encoding="utf-8").write(json.dumps(d, indent=1, ensure_ascii=False))
print("cache written, bytes:", os.path.getsize(P))
print("mtime:", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(os.path.getmtime(P))))
print("cumulative:", len(p["slugs_seen_cumulative"]))
