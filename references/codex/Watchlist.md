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
| Meta for Business News | https://www.facebook.com/business/news | Scrape listing | Daily |
| Marketing API changelog | https://developers.facebook.com/docs/marketing-api/marketing-api-changelog | Page diff | Weekly (Mon) |
| Graph API version hub | https://developers.facebook.com/docs/graph-api/changelog | Page diff | Weekly (Mon) |
| Advertising Standards (silent policy rewrites) | https://transparency.meta.com/policies/ad-standards/ | Page diff | Weekly (Mon) |

## Google

| Source | URL | Method | Check |
|---|---|---|---|
| Google Ads Announcements | https://support.google.com/google-ads/announcements/9048695 | Scrape dated entries | Daily |
| Ads & Commerce Blog | https://blog.google/products/ads-commerce/ | RSS: https://blog.google/products/ads-commerce/rss/ | Daily |
| Google Ads API release notes | https://developers.google.com/google-ads/api/docs/release-notes | Page diff | Weekly (Mon) |
| Ads Developer Blog | https://ads-developers.googleblog.com/ | RSS: http://feeds.feedburner.com/GoogleAdsDeveloperBlog | Weekly (Mon) |
| Merchant Center changelog | https://support.google.com/merchants/announcements/6192467 | Scrape dated entries | Weekly (Mon) |

## TikTok

**Two of the three original sources are unreachable from our IP and the browser does not fix it.** Verified 2026-08-19 across the Playwright browser and curl, on four paths each, after three consecutive failed daily runs (17, 18 and 19 August).

| Source | URL | Check | Status 2026-08-19 |
|---|---|---|---|
| **Business API SDK changelog (PRIMARY)** | https://raw.githubusercontent.com/tiktok/tiktok-business-api-sdk/main/Changelog.md | Daily | **Working, HTTP 200.** Baseline seeded at v0.1.8. Version-string diff, no browser needed |
| TikTok Newsroom | https://newsroom.tiktok.com/en-us | Suspended | **HTTP 503 on every path**, including /rss, /feed, /sitemap.xml and the en-gb locale, in both the browser and curl. Host-level block, not a page fault |
| TikTok for Business blog | https://ads.tiktok.com/business/en-US/blog | Suspended | **HTTP 302 to /business/notfound** from our IP |
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
