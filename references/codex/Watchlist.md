---
title: "Watchlist"
type: reference
created: 2026-08-18
tags: [advertising-science, sources]
---

# Watchlist: official platform sources

The pages the daily Research run monitors for platform updates. All URLs verified 2026-08-15.

## Meta

| Source | URL | Method | Check |
|---|---|---|---|
| Meta Engineering Blog (Andromeda/GEM posts land here first) | https://engineering.fb.com/ | RSS: https://engineering.fb.com/feed/ | Daily |
| Meta Newsroom | https://about.fb.com/news/ | RSS: https://about.fb.com/news/feed/ | Daily |
| Meta for Business News | https://www.facebook.com/business/news | Scrape listing, **compare DATES not links**, see below | Daily |
| Marketing API changelog | https://developers.facebook.com/docs/marketing-api/marketing-api-changelog | Page diff | Weekly (Mon) |
| Graph API version hub | https://developers.facebook.com/docs/graph-api/changelog | Page diff | Weekly (Mon) |
| Advertising Standards (silent policy rewrites) | https://transparency.meta.com/policies/ad-standards/ | Page diff | Weekly (Mon) |

### Meta for Business News: diff on dates, never on the link set (added 2026-08-20)

The listing is a **rotating module, not a chronological feed.** On 2026-08-20 a link-set diff against the cache showed 5 links absent from the cache and 5 present in the cache but gone from the page. All 5 "new" ones were opened and dated: 13 October 2025, 28 January 2026, 9 April 2026 and 11 June 2026. **Zero were new.** The page had simply rotated a different slice of the same back catalogue into view.

So a link-set diff produces a 5-item false positive on this source. Read the date on each candidate before treating it as new, and remember the page uses UK date format ("13th October 2025") on some posts, which a `Month D, YYYY` regex silently misses. The newest post seen to date is still **11 June 2026**.

## Google

| Source | URL | Method | Check |
|---|---|---|---|
| Google Ads Announcements | https://support.google.com/google-ads/announcements/9048695 | Scrape dated entries | Daily |
| Ads & Commerce Blog | https://blog.google/products/ads-commerce/ | RSS: https://blog.google/products/ads-commerce/rss/ | Daily |
| Google Ads API release notes | https://developers.google.com/google-ads/api/docs/release-notes | Page diff | Weekly (Mon) |
| Ads Developer Blog | https://ads-developers.googleblog.com/ | RSS: http://feeds.feedburner.com/GoogleAdsDeveloperBlog | Weekly (Mon) |
| Merchant Center changelog | https://support.google.com/merchants/announcements/6192467 | Scrape dated entries | Weekly (Mon) |

## TikTok

**ROOT CAUSE FOUND 2026-08-20: this is an India geo-block and it is permanent.** Following the for-Business blog redirect to its end returns HTTP 200 on `https://ads.tiktok.com/business/notfound`, and the body is TikTok's June 2020 open letter to Indian partners about the Government of India blocking 59 apps including TikTok, signed by Sam Singh, TikTok India. TikTok has been banned in India since 29 June 2020, we egress from New Delhi, and TikTok's edge serves that notice in place of the blog. The Newsroom 503s are the same block at a different layer.

**Consequences: stop retrying these daily, and never log them as an outage or a transient fault.** No user agent, browser profile or path fixes a geo-block. The only real fix is a non-India egress (VPN or a proxy in a country where TikTok operates). Until that exists, TikTok policy and creative announcements are genuinely unmonitored and should be stated as such rather than implied covered.

Previously verified 2026-08-19 across the Playwright browser and curl on four paths each, after three consecutive failed daily runs (17, 18 and 19 August), where the cause was recorded as unknown.

| Source | URL | Check | Status 2026-08-19 |
|---|---|---|---|
| **Business API SDK changelog (PRIMARY)** | https://raw.githubusercontent.com/tiktok/tiktok-business-api-sdk/main/Changelog.md | Daily | **Working, HTTP 200.** Baseline seeded at v0.1.8. Version-string diff, no browser needed |
| TikTok Newsroom | https://newsroom.tiktok.com/en-us | Suspended | **HTTP 503 on every path**, including /rss, /feed, /sitemap.xml and the en-gb locale, in both the browser and curl. Host-level block, not a page fault |
| TikTok for Business blog | https://ads.tiktok.com/business/en-US/blog | Suspended | **302 to /business/notfound, which serves the 2020 India ban notice.** Geo-block, confirmed 2026-08-20 |
| Marketing API what's new | https://business-api.tiktok.com/portal/docs/whats-new/v1.3 | Suspended | HTTP 403 |

The SDK changelog is now the primary TikTok source because it is the only one that answers. It ships endpoint names rather than prose, so it detects new ad products and campaign types and misses policy and creative announcements. Treat TikTok product news as a known blind spot until a working route is found. Do not log a TikTok check as clean when only the changelog was read.

## Research

| Source | URL | Method | Check |
|---|---|---|---|
| arXiv cs.IR (ranking/recsys papers, Andromeda's home category) | https://arxiv.org/list/cs.IR/recent | RSS: https://rss.arxiv.org/rss/cs.IR, see filter below | Daily |
| AI at Meta Blog | https://ai.meta.com/blog/ | Scrape | Weekly (Mon) |

### arXiv keyword filter (tightened 2026-08-19)

The original filter was `ads, advertising, CTR, ranking, auction` matched loosely. It fired on every recommender-systems paper in the category and returned 8 false positives on 2026-08-19, 0 of them about advertising. cs.IR is mostly recsys, so a loose filter returns the whole category.

Require a hit on the **advertising** list, not the ranking list:

- Bank list: `advertis`, `\bads?\b` as a whole word, `ad auction`, `sponsored`, `click-through rate`, `CTR prediction`, `bid landscape`, `bidding`, `conversion lift`, `incrementality`, `budget pacing`, `creative selection`, `GSP`, `second-price`.
- Do NOT trigger on `recommend*`, `ranking`, `retrieval` or `CTR` alone. Those match recsys papers with no advertising content. They only count alongside a bank-list hit.
- `\bads?\b` must be a whole word. Substring matching pulls in "adaptive", "advanced" and "gradient".

A day with 0 arXiv items is the normal result. Report it as 0 rather than padding with recsys papers.

### arXiv scheduling lag: the daily run always reads YESTERDAY's build (found 2026-08-20)

arXiv rebuilds the cs.IR feed at **04:00 UTC**. The daily research task fires at **07:00 IST, which is 01:30 UTC**, so it lands **2.5 hours before that day's rebuild**. The feed served at run time is always the previous day's.

Two runs in a row (02:07 IST and 07:00 IST on 20 August) both read the Wed 19 Aug 04:00 UTC build and both correctly reported 0 new. Neither says anything about Thursday's papers.

**No papers are lost.** They are picked up by the next morning's run, one day late. So the honest phrasing in a run log is "0 new in the build served, which is yesterday's", never "no advertising papers today". Fix if the lag ever matters: move the task past **09:30 IST**. Until then, state the lag.

### The MONDAY run always reads an EMPTY feed (found 2026-08-24)

Second consequence of the same lag, and it is worth stating separately because it looks like a broken fetch. A Monday run reads **Sunday's** build, and arXiv announces nothing on Sunday. On 2026-08-24 the feed body was **892 bytes containing zero `<item>` elements**, with `lastBuildDate` of Sun, 23 Aug 2026 04:00:00 +0000.

That is not a fetch failure, not a parse failure, and not a filter result. There was nothing in the file. Log it as "feed empty, weekend build", never as "0 advertising papers today" and never as an error. The same will be true of every future Monday run until the task moves past 09:30 IST.

## Source-quality gaps recorded 2026-08-24

Two watchlist sources are weaker than the table above implies, and both were found by checking rather than by failing.

- **Meta Advertising Standards has no cached baseline.** Plain fetch returns HTTP 400, the page displays no last-updated or effective date, and no text snapshot has ever been saved. So the lane can report the page's structure and genuinely cannot detect a silent rewrite. This matters because four chiropractic accounts depend on the health and personal-attributes sections. **Do not log this source as clean.** Fix: add a WebFetch-based snapshot step so future runs have something to diff.
- **The Marketing API changelog index under-renders.** On 2026-08-24 it showed only through v25.0; v26.0 (29 July 2026) had to be confirmed from the Graph API changelog and the v26.0 detail page. A future run reporting "newest is v25.0" from the index alone is seeing a rendering artefact, not a rollback.
