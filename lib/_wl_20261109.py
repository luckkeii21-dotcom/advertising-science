# Watchlist cache commit for the 2026-11-09 research run. Writes every key by hand on the IST date.
import io, json

P = r"E:\claude code marketing skill\.claude\skills\advertising-science\cache\watchlist-seen.json"
c = json.load(io.open(P, encoding="utf-8"))
pg = c["pages"]

us = ['how-metas-ads-system-matches-your-ad-to-the-right-person', 'three-new-ai-innovations-in-ads-ranking',
      'you-dont-beat-the-auction-you-brief-it', 'muse-smb-jaeluxe-shoetique', 'agencies-testing-incrementality',
      'meta-nest-ai-creative-diversification', 'meta-brand-building-summit-2026', 'muse-smb-bennett-orchards',
      'a-new-way-for-businesses-and-personal-agents-to-work-together', 'advertising-week-new-york-2026',
      'agency-awards-2026', 'introducing-meta-one-plans-for-businesses']
uk = ['you-dont-beat-the-auction-you-brief-it', 'creator-marketing-whitepaper',
      'performance-spotlight-how-instant-hydration-built-a-system-for-ai-to-scale',
      'businesses-driving-results-with-meta-ai-ads', 'closing-the-creator-measurement-gap',
      '2026-winning-hearts-boosting-carts', 'conversations-2026-introducing-meta-business-agent',
      'social-search-series-2', 'social-search-series-3', 'social-search-series-1',
      '2026-trends-from-around-the-world',
      'meta-growth-drivers-putting-your-digital-marketing-strategy-on-auto-pilot']

m = pg["meta-business-news"]
m["last_checked"] = "2026-11-09"
m["slugs_us_2026_11_09"] = us
m["slugs_uk_2026_11_09"] = uk
m["result_2026_11_09"] = (
    "Plain fetch HTTP 400 on both pinned URLs, the ordinary state. The local script now reads the cumulative key at "
    "pages/meta-business-news/slugs_seen_cumulative (36) and carries BOTH date patterns, so defect_2026_11_05 and "
    "note_2026_11_04_pass2_uk_date_format are fixed in lib/_bizmeta_20261109.py. Read through WebFetch on ?locale=en_US "
    "and ?locale=en_GB. US 12 slugs, identical in SET and ORDER to 2026-11-08, ceiling 28 Oct 2026, fifth consecutive "
    "flat day. UK shelf MOVED: 3 out (meta-ai-now-available-in-hongkong, meta-agency-first-awards-winners-hongkong-2026, "
    "meta-marketing-summit-hongkong-2026), 3 in (creator-marketing-whitepaper 6 Oct 2026, 2026-trends-from-around-the-world "
    "31 Mar 2026, meta-growth-drivers 27 Jan 2026). All 6 already in slugs_seen_cumulative, so 0 NEW. UK ceiling moved "
    "BACKWARDS 27 Oct to 22 Oct, the documented non-monotonic rotation at note_2026_10_09, NOT a retraction: the three "
    "Hong Kong posts are still live at their own URLs.")

mb = pg["meta-ad-standards"]
mb["last_checked"] = "2026-11-09"
mb["result_2026_11_09"] = (
    "UNCHANGED on both locales. US: all 16 sections located, zero not-found, every one of the 16 hashes byte-identical to "
    "the post-change state recorded on 2026-11-02 (Restricted goods and services 6528 chars / dac6ec80d7bc8131). UK: all 16 "
    "sections located, zero not-found, Restricted goods and services 6533 chars matching 2026-11-02, and the 266-line body "
    "vector is IDENTICAL index by index to adstd-linelens-uk-2026-11-02.json, sum 30371, total innerText 33583 on both days. "
    "So the UK page is confirmed unchanged line by line, which the 2026-11-02 run could not do.")
mb["section_map_uk_2026_11_09"] = {
    "note": "FULL UK per-section hash baseline, the first one that exists. Closes the gap named at note_2026_11_02: "
            "before today only one UK section had a recorded value.",
    "Overview": {"chars": 969, "sha": "645d4907aa95f6d2"},
    "Meta advertising policy principles": {"chars": 3613, "sha": "c448fb4223c53aa9"},
    "The ad review process": {"chars": 1912, "sha": "7684d7a75f715a3e"},
    "What to do if your ad is rejected or if your business asset is restricted": {"chars": 488, "sha": "80241eca7c262b04"},
    "Community Standards": {"chars": 175, "sha": "9343a2c3441eaf6b"},
    "Unacceptable content": {"chars": 3786, "sha": "5feccddda1041534"},
    "Prohibited Commercial Practices": {"chars": 199, "sha": "8a32e4398761032b"},
    "Restricted goods and services": {"chars": 6533, "sha": "88185e238558badf"},
    "Objectionable content": {"chars": 2464, "sha": "2658162ac50a5729"},
    "Intellectual property infringement": {"chars": 866, "sha": "cc4e906134567839"},
    "Social issue, electoral or political advertising": {"chars": 556, "sha": "375cd36a44373eb9"},
    "Product and format-specific policies": {"chars": 2089, "sha": "62a2b167f0c68ca4"},
    "Advertising policies affecting business assets": {"chars": 1401, "sha": "4306348e70b03aa5"},
    "Data use restrictions": {"chars": 1246, "sha": "74731ffb86e6e1a5"},
    "Things you should know": {"chars": 3181, "sha": "054db5e85f954f48"},
    "Transparency requirements under the EU Digital Services Act": {"chars": 4003, "sha": "6eb8afbfab743a03"},
}
mb["note_2026_11_09_separator_defect"] = (
    "DEFECT IN THE ANCHOR REGEX, FOUND AND FIXED IN THE SAME RUN, and it produced a false policy-removal finding on the "
    "first UK pass. Collapsing each separator CHARACTER with [- ]? cannot match the UK rendering "
    "'Product- and format-specific policies', which carries a hyphen AND a space between 'Product' and 'and'. The first UK "
    "pass reported that section NOT-FOUND and ballooned 'Social issue, electoral or political advertising' from 550 to "
    "12,476 chars by absorbing everything to the end of the page. Use [- ]+ as the separator class, never [- ]?. This is "
    "the SAME section the 2026-10-19 note already flagged for sentence case: the case fix was applied and the hyphenation "
    "fix was not.")
mb["note_2026_11_09_total_is_not_a_key"] = (
    "US total innerText is 32,502 today against 32,611 recorded for a pre-change read, a 106-char drop, while all 16 "
    "section hashes are byte-identical. The delta therefore sits OUTSIDE the hashed span, in nav or footer chrome (335 total "
    "lines, 267 body lines). Total innerText is not a usable key on this page; the section hashes are. A US body vector is "
    "stored today so the US side gets the same line-level localisation the UK side already has.")
mb["linelens_us_2026_11_09"] = {
    "body_lines": 267, "body_sum": 30321, "total_chars": 32502,
    "note": "Body prefix cut at the 'On this page' marker, the same convention as the UK file."}

weekly = {
    "meta-marketing-api-changelog":
        "CHANGED, AND IT IS REAL. Marketing API v27.0 is now in the Available Marketing API versions table, Date Introduced "
        "November 4, 2026, Available Until TBD. The 2026-11-02 baseline topped at v26.0. Full table today: v27.0 4 Nov 2026 "
        "TBD, v26.0 29 Jul 2026 TBD, v25.0 18 Feb 2026 until 23 Feb 2027, v24.0 8 Oct 2025 until 10 NOVEMBER 2026, which is "
        "tomorrow. The page header still reads 'Updated: May 21, 2026' and the newest dated body entry is still 05/04/2026, "
        "so the body did not move; only the version table did. Read in the Playwright browser.",
    "meta-graph-api-changelog":
        "TABLE UNCHANGED, HEADLINE MOVED. The availability table still carries 14 Graph versions, newest v26.0 (29 Jul 2026, "
        "TBD), identical to 2026-11-02. But the page's own headline sentence now reads 'The latest Graph API version is: "
        "v27.0', and so does docs/graph-api/guides/versioning. docs/graph-api/changelog/version27.0 returns HTTP 404, so "
        "v27.0 has no published changelog yet and what it changes is unknown and must not be guessed at. The Marketing API "
        "table on this same page also still ends at v26.0 and gives v24.0 Available Until October 6, 2026, which DISAGREES "
        "with the Marketing API changelog page's November 10, 2026 for the same version. Two Meta pages, two end-of-life "
        "dates for v24.0. Read in the Playwright browser.",
    "google-ads-api-release-notes":
        "UNCHANGED on the version-heading key. h2 set: Page Summary, Release summary and quick links, v26 / v25 / v24 / v23 "
        "major and minor versions, Archived release notes. Same as 2026-11-02 and 2026-10-26. Raw bytes 389,455, not used as "
        "a key because of the per-render nonce.",
    "google-ads-developer-blog":
        "THREE NEW POSTS since the 2026-11-02 weekly read, all three read in full from the Feedburner Atom content body on "
        "the first attempt. (1) 2026-11-04 'Data Manager API now supports Google Ads call conversions and row-level "
        "diagnostics': BANKED as GA-100 for the lead_id attribution gap, MERGED into GA-073 for the call_info field and the "
        "record_indices diagnostics. (2) 2026-11-04 'Upcoming changes to multi-party approvals in the Google Ads API': read "
        "and DELIBERATELY NOT BANKED, access-invitation plumbing (deferred resource creation, a new "
        "STALE_MULTI_PARTY_AUTH_REQUEST error in v26.2, review batch limit 1 to 100) effective the week of 7 December 2026, "
        "with nothing in it that changes how an account is bought or measured. (3) 2026-11-06 'Prepare for CocoaPods "
        "read-only mode': read and NOT BANKED, Google Mobile Ads SDK distribution for iOS app publishers, and no client of "
        "ours ships an app.",
    "merchant-center-changelog":
        "UNCHANGED. 80 /merchants/answer/ ids, 0 added and 0 removed against the 2026-11-02 snapshot. Id set stored at "
        "cache/_wk_mc_20261109.txt.",
    "ai-at-meta-blog":
        "UNCHANGED and nothing in lane. Newest post still 27 July 2026, now 105 days flat. Same five visible posts as every "
        "check since 2026-09-07. Zero advertising, ranking or measurement content. Read in the Playwright browser; plain "
        "fetch returns HTTP 400 on this host.",
}
for k, res in weekly.items():
    d = pg.setdefault(k, {})
    d["last_checked"] = "2026-11-09"
    d["result_2026_11_09"] = res

occ = pg["meta-occ-shelf"]
occ["last_checked"] = "2026-11-09"
occ["result_2026_11_09"] = (
    "MOVED. occ-2026 now declares 'Updated: Nov 5, 2026', up from 'Oct 22, 2026' on 2026-11-02, and carries 17 distinct "
    "entry dates against 16. ONE new entry, dated 5 November 2026: 'Ads Insights API -- Partnership ads creator breakdown', "
    "a new pa_creator_ig_handle breakdown grouping partnership-ads results by the creator's Instagram handle, applying to "
    "all versions on the account, campaign, ad-set and ad insights endpoints. Read in full and BANKED as AT-134. The 2023, "
    "2024 and 2025 shelves remain unread backlog.")

dg = pg["demand-gen-drops-hub"]
dg["last_checked"] = "2026-11-09"
dg["result_2026_11_09"] = (
    "NO NEW INSTALMENT. Read directly again because the Ads & Commerce RSS alarm is now 12 days stale (feed build 28 "
    "October). The newest instalment slug is still demand-gen-drop-october-2026, whose content is already banked at GA-093, "
    "and there is no demand-gen-drop-november-2026. METHOD NOTE, stated so a later run does not read a false drop: today's "
    "count is 10 ANNOUNCEMENT SLUGS linked from the hub, a DIFFERENT key from the 14 CARD HEADINGS the 2026-11-08 run "
    "counted. The two numbers are not comparable and 10 against 14 is not a removal. The slug set is the better key because "
    "it names what moved; the card count includes the intro card and the 2025 instalments that do not link to "
    "/announcements/.")

c["last_run"] = "2026-11-09T17:00 IST"
io.open(P, "w", encoding="utf-8", newline="").write(json.dumps(c, indent=1, ensure_ascii=False))
print("committed keys for 2026-11-09")
