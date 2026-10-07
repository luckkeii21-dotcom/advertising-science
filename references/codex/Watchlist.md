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

So a link-set diff produces a 5-item false positive on this source. Read the date on each candidate before treating it as new, and remember the page uses UK date format ("13th October 2025") on some posts, which a `Month D, YYYY` regex silently misses. **CEILING BROKEN 2026-09-10. The newest post is now 3 September 2026, "Businesses driving results with Meta AI ads", and it is the first new item on this source since 11 June.** It carries five named advertiser case studies across five products and is banked at MD-153. The 11 June ceiling had held across eleven consecutive daily checks, which is long enough that a future run should treat a long flat period on this source as normal rather than as a fault.

**Transport note, 2026-09-10.** Earlier runs recorded HTTP 400 on a plain curl and moved this source to the browser. A plain HTTPS fetch answered fine today, so the 400 was not permanent. The page geo-renders in Hindi from our New Delhi egress; append `?locale=en_US` to read it in English, and never transcribe a number out of the machine-translated Hindi.

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

### The SATURDAY run reads an empty feed too, for a different reason (found 2026-09-05)

Same empty file, different cause, and worth separating so neither is mistaken for a fault. The Monday case above is the lag: Monday reads Sunday's build and arXiv announces nothing on Sunday. **A Saturday run that lands AFTER 04:00 UTC reads Saturday's own build, and arXiv does not announce on Saturday either.** The feed carries `<skipDays>` naming Saturday and Sunday explicitly.

Observed 2026-09-05 at 06:31 UTC: **892 bytes, zero `<item>` elements, `lastBuildDate` Sat, 05 Sep 2026 04:00:04 +0000**, byte-signature identical to the 2026-08-24 Monday observation. **No build was skipped and no paper was lost**; Friday's build was read by Friday's run. Log it as "feed empty, weekend build" and move on.

Practical consequence for the whole weekend: **a Friday-evening-through-Sunday window announces nothing**, so Saturday, Sunday and Monday runs all have an empty or stale arXiv lane by construction. Only Tuesday through Friday runs can return papers.

## Source-quality gaps recorded 2026-08-24

Two watchlist sources are weaker than the table above implies, and both were found by checking rather than by failing.

- **Meta Advertising Standards has no cached baseline.** Plain fetch returns HTTP 400, the page displays no last-updated or effective date, and no text snapshot has ever been saved. So the lane can report the page's structure and genuinely cannot detect a silent rewrite. This matters because our chiropractic accounts, ChiroWorks and Chiropraise, depend on the health and personal-attributes sections. *(Count corrected 2026-08-27 from "four": Mattia was offboarded 2026-07-24.)* **Do not log this source as clean.** Fix: add a WebFetch-based snapshot step so future runs have something to diff.
- **The Marketing API changelog index under-renders.** On 2026-08-24 it showed only through v25.0; v26.0 (29 July 2026) had to be confirmed from the Graph API changelog and the v26.0 detail page. A future run reporting "newest is v25.0" from the index alone is seeing a rendering artefact, not a rollback.

### The "Monday is always empty" rule is about RUN TIME, not about Monday (corrected 2026-09-07)

The note above says a Monday run always reads Sunday's empty build. That is true only for a run
that fires **before 04:00 UTC**, which the scheduled 07:00 IST task does.

Observed 2026-09-07 (a Monday) at **05:25 UTC**, after that morning's rebuild: the feed carried
**27 items**, `lastBuildDate` **Mon, 07 Sep 2026 04:00:12 +0000**, 23 of them not previously seen.
So arXiv **does** announce on Monday, and Monday's 04:00 UTC build carries it.

Corrected statement of the whole lag: **a run before 04:00 UTC reads yesterday's build; a run after
04:00 UTC reads today's.** Combined with `<skipDays>` Saturday and Sunday, the empty results are:
a Saturday or Sunday run at any hour, and a Monday run before 04:00 UTC. **A Monday run after
04:00 UTC is a normal, full read.** Do not log it as "feed empty, weekend build" without checking
`lastBuildDate` against the clock.

### arXiv filter: "sponsored" is the second false-positive term (found 2026-09-07)

`sponsored` sits on the bank list and fired on arXiv 2609.05063, *Beyond Co-purchase Relation:
Evolution of Complementary Recommendations at Allegro*. The paper is a complementary-product
retrieval system for organic discovery at an e-commerce marketplace. It has no auction, no bidding,
no ad ranking and no advertising mechanism. The single trigger is the last clause of the abstract,
where sponsored placements appear as a **downstream revenue beneficiary**: "delivers significant
uplifts in attributed GMV for organic discovery and drives substantial revenue growth in sponsored
placements."

This is the same shape as the two failures already recorded: `CTR prediction` firing on a pure
recsys paper (2026-08-26) and `HubMixer` passing on an advertising mention inside a framing
sentence (2026-08-31). **The pattern across all three is that the advertising term appears once, in
framing or in an outcome clause, never in the method.** The filter needs a rule that discounts a
single bank-list hit confined to the first or last sentence of an abstract, or a co-occurrence
requirement of two distinct bank terms. Until that ships, expect roughly one false positive a week
and read the abstract before banking.

### Google Ads Developer Blog: WebFetch returns the chrome without the article body

Second occurrence, after 2026-08-31. WebFetch on a post permalink returns the blog header, sharing
buttons, labels, archive nav and footer, and **no post body**. On 2026-08-31 that cost GA-069 its
primary source and the substance had to come from the help centre.

**The working route is a plain urllib fetch plus a `post-body` div regex**, which returned both
2026-09-07 posts in full on the first attempt. Use it whenever a post's substance is needed. The
index and archive pages render fine through WebFetch, so use WebFetch for titles and dates and
urllib for bodies.

### Meta for Business News: the card DATES drift by one day, so a date diff is not safe either (found 2026-09-14)

The rule at the top of this note says diff on dates, never on the link set, because a link-set diff
produced five false positives on 2026-08-20. That rule is still right about links and it is now
known to be incomplete.

**Observed 2026-09-14 against 2026-09-13, same 12 cards, same order, nothing new.** Five of the
twelve card dates rendered exactly ONE DAY EARLIER than they had the day before:

| 2026-09-13 | 2026-09-14 | Post |
|---|---|---|
| 11 Sep | **10 Sep** | Performance Spotlight: How Instant Hydration Built a System for AI to Scale |
| 26 Aug | **25 Aug** | Small to Scale: How Sydney Sock Project Scaled a Cause |
| 12 Aug | **11 Aug** | Win over shoppers with ad formats they're engaging with |
| 7 Aug | **6 Aug** | Performance Spotlight: What Your CFO Actually Wants to Hear About Marketing |
| 28 Jul | **27 Jul** | Getting Your Small Business Holiday-Ready |

The other seven (3 Sep, two 19 Aug, three 11 Aug, 15 Jul) were identical. So the drift is not applied
uniformly, it is a timezone boundary catching whichever posts sit near midnight in the rendering
locale. **This also explains the 2026-09-13 entry that read the card "catching up" from 10 Sep to
11 Sep. It was not catching up. It drifted, and it drifted back.**

**Consequence for the method.** Neither key is stable on its own: the link set rotates, and the dates
move by a day. **Diff on the post TITLE, and read the date only to decide whether a genuinely new
title is worth opening.** A whole-list shift of one day with the titles unchanged is a rendering
artefact and must never be logged as twelve new items or as twelve disappearances.

**Transport, sixth consecutive daily observation.** The browser opened the listing on the first
attempt again. The plain-fetch routes have now returned 200, 400, 200 and 400 across six days. The
honest instruction for this source is "use the browser", not "try fetch first".

### Meta Advertising Standards: the source-quality gap recorded 2026-08-24 is CLOSED (2026-09-14)

That note said the lane could report the page's structure and genuinely could not detect a silent
rewrite, and it sat directly under our two chiropractic accounts. Two things changed today.

1. **The heading baseline caught a real change on its 20th day**, its first ever: section 7 renamed
   from "Fraud, Scams, and Deceptive Practices" to "Prohibited Commercial Practices", with two
   policies collapsed into one. Banked as MD-156.
2. **A per-section SHA-256 map of the rendered body now exists**, so a rewrite under an unchanged
   title is detectable from the next run onward. Method and the 16 baseline hashes are in
   `.claude/skills/advertising-science/cache/meta-ad-standards-baseline.md`.

**New standing instruction for this source: read BOTH `/policies/ad-standards/` and
`/en-gb/policies/ad-standards/`.** They disagreed on 2026-09-14, in the same browser session, on the
name and count of a policy section. Meta stages these rewrites by locale. A single-locale read will
show a change a week late or not at all, depending on which locale you happen to check.

### Google Ads Announcements: the script's own diff key is UNSTABLE, and the stable key is the answer href (found 2026-09-18)

`lib/watchlist_check.py` diffs this page on a line comparison and reports an added and removed id
count from it. **That output is not reliable.** Two fetches taken seconds apart on 2026-09-18, both
against the same cache, reported a DIFFERENT "added" id: `11355155681876453040` on the first run and
`7690260504386057358` on the second. A long-digit regex over the page body returns 30 ids, and 3 of
those 30 change on every render. They are per-render session values, the same class of artefact as
the `nonce` recorded on 2026-09-16. The "removed" list is worse noise still: it contains nav labels
("Start advertising", "Campaigns", "Explore features"), which drop out whenever the page renders in
a different locale.

**The stable key is the answer permalink id:** `/google-ads/answer/(\d+)`. On 2026-09-18 it returned
**396 ids, byte-identical across two consecutive fetches**, and 396 against the cached copy with zero
added and zero removed.

Method for any future run: extract the answer-href id SET from a fresh fetch and from the cache, and
diff the sets. Never report the script's `added`/`removed` line counts as news. Note the count has
drifted by one against the 2026-09-17 log, which reported 395 from the same cached file; that is a
regex difference between runs and not a page change, which is exactly why the SET diff is the thing
to read and the count is not.

### Meta for Business News: the ceiling moved to 15 September 2026 (checked 2026-09-18)

Previous ceiling was the Instant Hydration performance spotlight at 10 or 11 September, held since
the 2026-09-14 check. **Two genuinely new cards, both dated 15 September 2026, both read in full:**
"Introducing Meta One plans for businesses" and "IAB Global Creator Week: Making it Easier for
Businesses to Partner with Creators and Turn Discovery into Purchase". Banked at MD-159 and as an
amendment to MD-157.

Title diff is working as the 2026-09-14 rule intends. Same 12-card module, two in, and "Getting Your
Small Business Holiday-Ready" (late July) rotated out, which is the rotation the link-set rule
already warns about. All five drift-prone cards rendered their EARLIER date today (10 Sep, 25 Aug,
11 Aug, 11 Aug, 6 Aug), consistent with the one-day timezone artefact and not a change.

**Transport, 2026-09-18.** Plain HTTPS returned HTTP 400 on both `?locale=en_US` and the bare URL.
The browser opened it first try. The instruction stays "use the browser".

**Browser availability note.** `playwright` and `playwright-arcads` both failed to connect at session
start, and `playwright-metatech` was already locked by another process. `playwright-higgsfield`
connected and did the work. When this source needs a browser, try every configured Playwright profile
before logging it unchecked.

### Meta for Business News is LOCALE-PARTITIONED, and reading one locale misses a whole catalogue (found 2026-09-20)

Every note above this one treats the source as a single 12-card module that rotates. It is not. **The bare URL and `?locale=en_US` serve two DIFFERENT catalogues from the same browser, in the same session, seconds apart.**

Observed 2026-09-20, `playwright` profile, both reads inside one minute:

| Read | Newest card | What it carried |
|---|---|---|
| `facebook.com/business/news` (renders en_GB from our New Delhi egress) | **11 September 2026** | Instant Hydration spotlight, Meta AI ads, and **four posts no US render has ever shown** |
| `facebook.com/business/news?locale=en_US` | **15 September 2026** | Meta One plans, IAB Global Creator Week, Sydney Sock Project, Laura Geller, the three holiday posts |

Only two cards appear in both. **The UK ceiling is FOUR DAYS OLDER than the US ceiling, so a run that reads only the bare URL will report the source as gone quiet while the US catalogue has moved.** That is the exact failure the 2026-09-18 entry would have produced if the bare URL had answered that day.

**The four UK-only posts, all read in full on 2026-09-20 and all previously unbanked:**

- *Why social search and traditional search aren't competing*, 13 May 2026
- *How to optimise content for social search on Meta technologies*, 14 May 2026, source of the caption-indexing statement banked at [[Meta Delivery & Andromeda#MD-161|MD-161]]
- *The trends reshaping search and the ROI that justifies moving now*, 15 May 2026, source of [[Attribution & Incrementality#AT-120|AT-120]] and [[Marketing Math & Unit Economics#MM-221|MM-221]]
- *Closing the creator measurement gap: How L'Oreal...*, 11 June 2026, source of [[Creative Science#CR-254|CR-254]]

A three-part series with a platform statement about how Meta search indexes captions sat unread for **four months** because the daily check only ever saw one locale's shelf. Five claims came out of one day's reading of it.

**New standing instruction: read BOTH the bare URL and `?locale=en_US` every day, and diff the TITLE sets separately.** This is the same rule the 2026-09-14 entry already imposed on Meta Advertising Standards, arriving independently on a second source. Assume by default that any Meta property stages content by locale.

**Two smaller observations from the same check.** The bare URL rendered in ENGLISH (UK), not the Hindi the 2026-09-10 note records, so the geo-render language is not stable either. And a post's own page can date itself in a different format from its card: *Closing the creator measurement gap* shows "11 June 2026" on the UK listing and "June 11, 2026" in its own header.

**Transport and browser, 2026-09-20.** The `playwright` profile connected and opened the listing on the first attempt, after three consecutive days of CONNECT_TIMEOUT at session start. Plain fetch was not attempted; the standing instruction is still "use the browser".

### Google Ads Announcements: the answer-href set diff is now IN THE SCRIPT (2026-09-20)

The 2026-09-18 entry above diagnosed the unstable key and left the fix as an instruction to future runs. It is now code. `lib/watchlist_check.py` diffs `/google-ads/answer/(\d+)` as a SET against the cached copy and reports `answer_ids_now`, `answer_ids_cached`, `added` and `removed`, replacing the visible-line diff that printed a phantom added id on 2026-09-16, 09-17, 09-18, 09-19 and again on the first run of 09-20.

Verified the same day: the old code reported `added 1, removed 1` with a DIFFERENT added id on two consecutive runs (`4881972142780550782`, then `5979057098169415478`). The new code reports **396 answer ids, 0 added, 0 removed**, matching a hand check of two fresh fetches that were byte-identical to each other and to the cache. The phantom-id class of finding does not need to be re-diagnosed by another run.

### Zero-browser day: the whole Meta lane is unreadable when no Playwright profile connects (2026-09-22)

Every note above assumes a browser can be found if enough profiles are tried. On 2026-09-22 none could, and the consequence is larger than a single missed source because **Meta serves HTTP 400 to plain fetch on every property this watchlist tracks.**

Observed, all in one run, plain HTTPS with a normal desktop user agent:

| Source | Result |
|---|---|
| Meta for Business News, bare URL | HTTP 400, 1,542-byte error body |
| Meta for Business News, `?locale=en_US` | HTTP 400, identical 1,542 bytes |
| Marketing API changelog | HTTP 400 |
| Graph API changelog | HTTP 400 |
| Advertising Standards, `/policies/ad-standards/` | HTTP 400 |
| Advertising Standards, `/en-gb/policies/ad-standards/` | HTTP 400 |
| AI at Meta blog | HTTP 400 |

All four configured Playwright MCP profiles failed at session start: `playwright`, `playwright-arcads`, `playwright-higgsfield` and `playwright-metatech`, all CONNECT_TIMEOUT at 30s. The 2026-09-18 instruction to try every profile before logging a source unchecked was followed and there was nothing left to try.

**The honest phrasing for a run log on a day like this is "the Meta lane was not checked", never "no Meta changes".** The distinction matters because the locale-partition finding of 2026-09-20 exists precisely because a source can look quiet while a catalogue behind it has moved.

**Non-Meta sources are unaffected.** Every Google source, the arXiv feed and the TikTok SDK changelog all answered a plain fetch normally in the same run, so a zero-browser day is a Meta-lane outage and not a network fault.

### Google weekly lane: a Monday failure silently costs a whole week (2026-09-22)

The 2026-09-21 research run exited on `API Error: Can't reach the API server (ENOTFOUND)` and the watchdog relaunched once, then stood down for the rest of the day. Monday is the only day the weekly sources are read, so the failure took the whole weekly lane with it and nothing recorded that it had.

Caught and run as catch-up on the Tuesday. **Add to the runbook's reading of "Weekly (Mon) sources: only on Mondays": if the previous Monday's run did not complete, run them on the next day that does.** The cheapest check is `runs/<yesterday>/research-claude.log` and the presence of a `<date>-research-log.md`.

**Merchant Center renders differently by transport, and the difference looks like a rollback.** A plain fetch on 2026-09-22 showed a newest dated entry of 15 July 2026; the 2026-09-07 WebFetch check recorded 11 August 2026. Same page, two transports, and the older-looking result is the artefact. This is the same class as the Marketing API changelog index under-rendering to v25.0. **Never report a newest-entry date going backwards as news; re-read on the other transport first.**

**The Developer Blog post-body regex is not universal.** The urllib plus `post-body` div route recorded on 2026-09-07 returned nothing on the 2026-09-10 permalink `new-onboarding-experience-for-google-ads-api.html`, so that post's body has not been read. The index and the Atom feed both render its title and date fine.


### Meta for Business News: the TITLE BASELINE now exists, and it found four unread posts sitting in plain sight (2026-09-23)

Every note above prescribes a title diff and none of them could run one, because no title set had ever
been stored. `cache/watchlist-seen.json` carried `meta-business-news` with the result string
"NOT CHECKED" and a `last_checked` of 2026-09-17. **Both locales' 12-card title sets are now saved
under `pages.meta-business-news.titles_us` and `titles_uk`.** From tomorrow the diff the 2026-09-14 rule
asks for is mechanical.

**Ceilings on the first browser read since 2026-09-20.** US moved, UK did not:

| Locale | Ceiling | Change since 2026-09-20 |
|---|---|---|
| `?locale=en_US` | **21 September 2026**, "Meet the 2026 Meta Agency Award Winners" | **New.** Previous ceiling 15 September |
| bare URL (renders en_GB) | 10 September 2026, Instant Hydration spotlight | Unchanged, eleven days behind the US shelf |

**The locale-partition rule of 2026-09-20 held again and the gap WIDENED to eleven days.** It was four
days on 20 September. A run reading only the bare URL today would have reported the source quiet while
the US catalogue had moved twice.

**Four posts were on the shelf, unread and unbanked, and reading them produced most of today's haul.**
Three were US-only and one UK-only, and none was new:

- *How do advertisers increase holiday ad budgets?* (card 11 Aug, post header **13 Aug 2026**), source of AT-125 and AT-126
- *Cyber 5 2025: What worked, what changed and how to win Q5* (15 December 2025, UK-only), source of AU-094, CR-261 and the CR-058 amendment
- *New Meta AI Features for Small Businesses* (19 August 2026), merged into MD-159
- *Game Changers: Why the fastest-growing audience in sports* (19 August 2026), read in full and **deliberately not banked**

**This is the same failure the 2026-09-20 entry diagnosed, arriving a second time.** There, a three-part
series sat unread for four months because only one locale was ever read. Here, four posts sat unread
because a title baseline that every note asked for had never been written. **The pattern in both: the
ceiling check answers "has the newest thing changed" and says nothing about what is already on the shelf.
A source can be checked daily for a month and still have unread posts in view.** The fix in both cases is
a stored SET rather than a remembered maximum.

**A new date artefact, and it is the third distinct one on this source.** *How do advertisers increase
holiday ad budgets?* shows **11 August** on its card and **August 13, 2026** in its own post header. That
is a two-day gap between card and post, which is larger than the one-day timezone drift recorded on
2026-09-14 and different in kind from the format difference recorded on 2026-09-20. **Cite the date from
the POST, never from the card**, and treat a card date as an approximate sort key only.

**Meta publishes fictional case studies on this channel and discloses it only in the footnote.** Banked at
AT-126 because it is a reading rule for this source, and repeated here because this is where a future run
will look. Before banking any figure from a Meta for Business post, check whether the advertiser is NAMED.

**Transport and browser, 2026-09-23.** `playwright` and `playwright-arcads` both failed CONNECT_TIMEOUT at
session start again, a fourth consecutive day. **`playwright-higgsfield` connected and did every read**,
after failing yesterday. The 2026-09-18 instruction to try every profile is doing real work: on two of the
last four days exactly one profile answered, and it was a different one each time. Plain fetch was not
attempted for this source; the standing instruction is still "use the browser". Plain fetch DID answer
normally on `engineering.fb.com` and `about.fb.com`, so the Meta HTTP 400 wall recorded on 2026-09-22 is
specific to `facebook.com` and `transparency.meta.com` properties.

### The watchlist cache had not been committed since 2026-09-19 (found 2026-09-23)

`cache/watchlist-seen.json` carried `last_run: 2026-09-19T14:37 IST` and every feed's `last_checked` read
2026-09-19. The 09-20 and 09-22 runs ran `watchlist_check.py` without `--commit`, so their diffs were
taken against a baseline up to four days stale and their "new links" counts were cumulative rather than
daily. **Nothing was missed**, because a stale baseline over-reports rather than under-reports, and both
days' logs record having read what surfaced. The cost is that neither day's count means what it says.

Today's run committed. **Add to the runbook reading of step 2: the watchlist check is not finished until
the cache is committed, and the cheapest verification is that `last_run` in `watchlist-seen.json` carries
today's date.** Today's committed figures: Meta Engineering 2 items (both already read on 09-22, neither
about ads), Meta Newsroom 2 (one the same subsea cable, one the Singapore enforcement post banked into
MD-160), Google Ads & Commerce 0, arXiv 20 new with **0 passing the ad filter**, TikTok SDK unchanged at
v0.1.8, Google Ads Announcements 396 answer ids with 0 added and 0 removed.

### blog.google footnotes live at `#footnote-N` anchors and a naive tag-strip DROPS them (found 2026-09-25)

The September Demand Gen drop prints "a 40% increase in conversions at the same ROI". A tag-strip plus
line-dedup extraction of the `<article>` element returned the whole post and **no footnote**, and this
run came within one step of logging the figure as having no provenance at all. It has provenance:
**"Google Internal Data, Global, Gmail Ads, February 2026"**, sitting outside the paragraph flow behind
a `1` that links to `#footnote-1`.

Method for any blog.google post: after stripping tags, search the text for `Internal Data`, `Google Data`
and `Based on`, and pull every `#footnote-N` anchor from the article's link list. **The footnote is
usually the most important sentence in a Google announcement**, because it is where the data window and
the population appear. Three of the five vendor figures now catalogued (GA-081, GA-083, GA-084) are
weakened mainly by what their own footnote says.

### The Google Ads Announcements page does NOT carry Demand Gen drops (found 2026-09-25)

The three help-article ids linked from the September Demand Gen drop (`16040527`, `16024357`,
`16388390`) are **not** among the 396 answer ids on `support.google.com/google-ads/announcements/9048695`.
That page's 396-id set has been stable at 0 added and 0 removed for days while Google shipped a monthly
product drop. **The announcements page is not a superset of Google ads product news.** The Ads &
Commerce RSS feed is the only lane in this watchlist that caught it, and it caught it one day late
because the post is dated 24 September and surfaced in the 25 September feed read.

### Demand Gen Drops Hub: a MONTHLY Google series with a year of unread instalments (found 2026-09-25)

`https://business.google.com/us/accelerate/demand-gen-drops/` answers a **plain fetch, HTTP 200**, no
browser needed. It lists every Demand Gen Drop back to the "Introducing Demand Gen Drops" post, twelve
entries, monthly cadence. This codex held exactly one of them (GA-068, August).

**The hub LAGS the blog.** On 2026-09-25 its newest listed drop was August, a day after the September
drop published on blog.google. So the hub is the back catalogue, not the alarm. Watch the Ads & Commerce
RSS for new drops and use the hub to work the backlog.

**This is the third instance of the same failure shape**, after Meta for Business News on 2026-09-20
(a three-part series unread for four months behind a locale partition) and again on 2026-09-23 (four
posts unread in plain sight because no title baseline existed). **A source can be watched daily and
still have a year of instalments behind it, because a ceiling check answers "has the newest thing
changed" and says nothing about the shelf.** Reading two of the ten unread drops on 2026-09-25 produced
GA-083 and GA-084 and re-dated two things the September post appeared to introduce.

**BACKLOG CLOSED 2026-09-26.** The nine remaining instalments were read in full at source in one
pass: the introduction post of 1 September 2025, then October, November and December 2025 and January,
February, March, April and June 2026. With the two read on 2026-09-25 and the August and September 2026
drops already banked, the series is complete at **thirteen instalments, monthly with no month missing,
1 September 2025 through 24 September 2026**.

Body extraction, confirmed working on all nine: strip tags, then anchor on `Social Module` and read to
`Return to top of page`. Anchoring on the post title fails on some of them because the chrome repeats
it. **Footnotes are reachable only through the `#footnote-1` anchor**, and a tag-strip plus line-dedup
drops them, which is where both of today's provenance findings were hiding.

**What closing the shelf produced:** GA-085, GA-086, GA-087 and GA-088 in
[[Google Auction & Smart Bidding]] and CR-266 in [[Creative Science]], plus amendments to GA-068,
GA-081 and GA-083. Two of those are provenance defects invisible in the body text of the posts.

**Maintenance from here:** the hub is the back catalogue and the Ads & Commerce RSS is the alarm. One
new instalment is expected per month. Read its footnote before its body.

### arXiv filter: TWO outcome-clause false positives in a single day (2026-09-25)

The 2026-09-07 entry predicted "roughly one false positive a week" and proposed two candidate fixes.
On 2026-09-25 the filter passed 3 items and **2 were false positives of exactly the documented shape**,
with 1 genuine:

| Paper | Verdict | The single trigger |
|---|---|---|
| 2609.28972 *Cross-Country Code-Mixing for Generative Recommendation* | **False positive** | "+1.77% advertising revenue" in the final clause of the abstract. Method is cross-market recsys token substitution, no auction, no bidding |
| 2609.30001 *Advancing Model Research in AgentX* | **False positive** | "15-20% in target-segment advertising spend" in an outcome list. Method is agentic automation of recsys model research |
| 2609.29182 *ScalarLens: Numerical Embeddings ... for CTR Prediction* | **Genuine** | CTR prediction throughout the method, evaluated on Criteo, an advertising dataset |

**Both false positives would be killed by the first proposed fix**, which discounts a single bank-list
hit confined to the first or last sentence of an abstract. That fix now has three supporting
observations (2026-09-07, plus two today) and zero counter-examples. **It is worth shipping into
`lib/watchlist_check.py` rather than leaving as an instruction**, the same way the answer-href set diff
was shipped on 2026-09-20 after being diagnosed on 2026-09-18.

ScalarLens was read and **deliberately not banked**: it is a benchmark method paper about numerical
feature embeddings, not a deployed ad system, and it changes no operating decision. Logged so a future
run does not re-read it.

### Merchant Center: the 2026-09-22 "transport artefact" was an ORDINAL-DATE BUG, and the fix belongs in every date regex in this file (corrected 2026-09-28)

The 2026-09-22 note above records a plain fetch showing a newest entry of 15 July 2026 against a 2026-09-07 WebFetch showing 11 August 2026, concludes the two transports render the page differently, and rules that the older-looking result is the artefact.

**That conclusion is wrong and it is retired.** Both transports render the same page. Today a plain urllib fetch and a real Playwright browser BOTH reported 15 July as newest, which should have been impossible under the transport theory. The actual cause is in our own pattern: the page renders that entry as **"August 11th, 2026"**, with an ordinal suffix, and a `Month D, YYYY` regex cannot match it, so the scraper skipped the entry entirely and reported the next one down. Widening the pattern to `(st|nd|rd|th)?` and an optional comma surfaced it immediately, along with "August 24th 2026" in the body, which also has no comma at all.

**This is the SECOND occurrence of the same bug in this file.** The Meta for Business News section already warns that the page "uses UK date format ('13th October 2025') on some posts, which a `Month D, YYYY` regex silently misses". The lesson did not travel to the Google lane.

**Two standing rules.**
- Every date regex used against any source in this watchlist must accept an optional ordinal suffix and an optional comma: `(January|...|December)\s+\d{1,2}(st|nd|rd|th)?,?\s+20\d{2}`.
- **Never explain a newest-entry date moving backwards as a transport artefact or a rollback before re-reading with an ordinal-aware pattern.** The failure looks identical to a page change and it is a bug on our side. Merchant Center's true newest entry has been 11 August 2026 throughout, and GP-043 already covers it.

### Meta Advertising Standards: the baseline's offset-150 anchor is brittle, and it failed on a 106-character header change (found 2026-09-28)

The per-section SHA-256 method added 2026-09-14 says to search for the 16 section names in order, starting the first search at offset 150. That offset is load-bearing and undocumented as such, and it broke today.

The page's leading chrome shrank by 106 characters, so `1. Overview` now sits at offset **102**. Starting at 150 skips it and locks onto the page's FOOTER "On this page" navigation list, where all 16 names appear again in order. Every section then hashes 12 to 74 characters of nav text and section 16 comes back not-found. **The output looks exactly like a full-page rewrite and the page had not changed at all.** Re-anchoring on the first occurrence of `Overview` reproduced all 16 baseline lengths and hashes byte-for-byte.

**Two fixes to the baseline, both in `cache/meta-ad-standards-baseline.md`.**
- Anchor on the **first** occurrence of `Overview`, or start at offset 0. Do not use a magic offset that assumes a fixed amount of page chrome.
- Section 16's stored name is `Transparency requirements under the EU DSA`. The page renders **`Transparency requirements under the EU Digital Services Act`**. Match on the rendered string, or on the prefix `Transparency requirements under the EU`.

**The result once anchored correctly: UNCHANGED.** All 16 slices byte-identical to 2026-09-14, including *Restricted goods and services* at 6,531 chars / `75a81517aee32a45`, which is the section carrying Health and Wellness that ChiroWorks and StayWell depend on. Whole-page text is 32,505 chars against a baseline 32,611, and the 106-character difference is entirely header chrome above section 1.

### The Marketing API changelog MOVED, and the index under-rendering artefact did not reproduce (2026-09-28)

`https://developers.facebook.com/docs/marketing-api/marketing-api-changelog` now redirects to **`https://developers.facebook.com/documentation/ads-commerce/marketing-api/marketing-api-changelog`**. The old URL still resolves through the redirect, so nothing is broken, but the table at the top of this file should carry the new path.

Separately, the index under-rendering artefact recorded three times (2026-08-24, 2026-09-07 and once before, where the index showed only through v25.0) **did not reproduce**. The index rendered v26.0, v25.0 and v24.0 in a dated table on the first read. Treat it as fixed and re-open it if it returns. Newest Marketing API version is unchanged at v26.0, 29 July 2026, and **v24.0 carries an Available Until of 6 October 2026**, which is eight days out.

### arXiv filter: the pending first-or-last-sentence rule would have been WRONG today (2026-09-28)

One paper passed the bank-list filter, arXiv 2609.31045, *KuaFu: Compressing Long User Behavior into Understanding at Billion Scale*. It carries exactly two bank-list hits, both the term `advertis`, one in the first sentence ("conversational agents, generative recommenders, and personalized advertising all rest on one capability") and one in the last ("has run on the Tencent advertising and recommendation platform for ten months, lifting overall GMV by 1.37%").

**That is the precise shape of the three recorded false positives, and this one is a TRUE positive.** The paper describes the production user-understanding layer of a real advertising platform at billion-user scale, with deployment numbers, and it was banked as LS-083.

So the rule proposed on 2026-09-07 and carried as a gap ever since, discount a bank-list hit confined to the first or last sentence of an abstract, **would have suppressed a genuine finding today.** The co-occurrence variant (require two distinct bank terms) would also have suppressed it, because both hits are the same term. This is the first counter-example against a rule that previously had three supporting observations and none against. **The gap stays open and the rule stays unshipped, and the reason has changed: it is no longer only that enforcing a judgement in code is Lucky's call, it is that the rule as specified is now known to produce false negatives.** Reading the abstract remains the only method that has never been wrong.

### The US shelf IS readable on a zero-browser day, through WebFetch with `?locale=en_US` (found 2026-09-30)

The 2026-09-22 entry above rules that "the whole Meta lane is unreadable when no Playwright profile connects", on the
evidence that every Meta property this watchlist tracks serves HTTP 400 to a plain fetch. **That ruling is about PLAIN
FETCH and it over-reaches to the lane.** Today all four Playwright profiles failed CONNECT_TIMEOUT at session start, a
plain fetch returned HTTP 400 on both Business News URLs, and **WebFetch rendered `?locale=en_US` in English (US) with
all 12 card titles and dates**. Diffed against `pages.meta-business-news.titles_us`: **0 added, 0 removed, set identical
to the 2026-09-28 baseline.** Ceiling holds at 21 September 2026, "Meet the 2026 Meta Agency Award Winners".

That is the first clean title-set diff ever run on the US lane without a browser, and it makes the most important source
on this watchlist browser-optional rather than browser-only.

**The `?locale=en_US` parameter is load-bearing and yesterday's run is the control.** On 2026-09-29 WebFetch was pointed
at the bare URL and rendered the India catalogue, which that run correctly refused to commit. Today the bare URL did the
same thing again, in Hindi, while the parameterised URL rendered US English in the same session. **The parameter
controls the render. The absence of it does not fall back to UK or to US, it falls back to our egress.**

### The bare URL does NOT give us the UK shelf, so `titles_uk` cannot be diffed from here without a browser (2026-09-30)

The 2026-09-20 standing instruction says to read BOTH the bare URL and `?locale=en_US` every day and diff the two title
sets separately, on the finding that the bare URL "renders en_GB from our New Delhi egress". **That was true on
2026-09-20 and it is not a property of the URL.** The bare URL rendered Hindi/India on 2026-09-29 and again on
2026-09-30, and the India catalogue is a third shelf, not the UK one.

Today's India set against the cached UK set: **8 of 12 titles overlap** (Instant Hydration, Meta AI ads, winning hearts
before peak season, Conversations 2026, optimise content for social search, trends reshaping search, why social search
and traditional search coexist, Cyber 5 2025). The four that do not are all back catalogue: 15 September 2025,
17 June 2024, 28 February 2023, 29 July 2022. **Byte-for-byte the same 8-and-4 split as 2026-09-29**, so the India shelf
is stable day over day and is not quietly rotating past us.

**Standing instruction, amended.** Read `?locale=en_US` and diff it against `titles_us`; that lane works with or without
a browser. **A bare-URL read from our egress is an INDIA read and must never be committed against `titles_uk`.** The UK
shelf needs a browser with an explicit `en-gb` path, or a UK egress. Until one of those runs, log the UK lane as not
checked and say how stale the baseline is, rather than logging the source as clean.

### Meta's HTTP 400 pages can be 267 KB and still contain nothing (2026-09-30)

Recorded so no future run chases the byte count. `transparency.meta.com/policies/ad-standards/` returned **HTTP 400 with
a 266,875-byte body** on a plain fetch, against the 1,542-byte error body the 2026-09-22 entry records for
`facebook.com/business/news`. The large body looks like a successful render and is not one: strip scripts and tags and
**the visible text is 7 characters and reads "Error"**. None of the 16 section names appears. Both localess behaved the
same way. **Judge a Meta 400 on its rendered text, never on its content length.**


### The UK shelf IS readable without a browser, and the key is `?locale=en_GB` (found 2026-10-01)

The 2026-09-30 entry above rules that "the UK shelf needs a browser with an explicit `en-gb` path, or a UK
egress", and instructs future runs to log the UK lane as not checked until one of those exists. **That
ruling is retired. WebFetch on `?locale=en_GB` rendered the UK shelf in English (UK) today, with all 12
card titles, all 12 dates and all 12 slugs, on the first attempt.** All four Playwright profiles failed
CONNECT_TIMEOUT at session start, so no browser was involved at any point.

**Both shelves therefore diffed clean in one pass with no browser, for the first time:**

| Locale | Ceiling | Slugs | Against the 2026-09-28 baseline |
|---|---|---|---|
| `?locale=en_US` | 21 September 2026, "Meet the 2026 Meta Agency Award Winners" | 12 | **0 added, 0 removed** |
| `?locale=en_GB` | 10 September 2026, Instant Hydration spotlight | 12 | **0 added, 0 removed** |

**What the 2026-09-30 entry got right and what it got wrong.** It was right that the bare URL is an India
read from our egress and must never be committed against the UK baseline. It was wrong to generalise from
"the bare URL does not give us the UK shelf" to "the UK shelf needs a browser". The missing step was to try
the parameter that already worked for the US lane with the other locale code in it. **The parameter is the
key on every locale, and it was never only a US fix.**

**Standing instruction, now simple enough to state in one line: read `?locale=en_US` and `?locale=en_GB`
through WebFetch, diff the SLUG sets, and never read the bare URL at all.** The whole source is
browser-optional. The US-to-UK ceiling gap is 11 days, unchanged from 2026-09-23, so the gap is a property
of Meta's publishing and not of our reading.

**Ask WebFetch for the hrefs, not the titles.** The 2026-09-27 note established that a slug diff is stable
where a title diff is not. WebFetch returns titles by default and three of today's twelve UK titles differ
from the stored baseline on punctuation alone: `L'Oreal` against `L'Oréal`, a hyphen against an en dash in
the social-search title, and double against single quotes in "Auto-Pilot". **A title diff would have had
three adjudications to make and a slug diff had none.** One extra WebFetch call per locale buys the stable
key.

### arXiv filter: `ad-hoc` is a FOURTH false-positive mechanism, and this one survives the whole-word rule (fixed in code 2026-10-01)

The filter notes above record three false-positive shapes, all of them about WHERE a genuine advertising
term sits in an abstract. This one is different: it is a term that is not about advertising at all.

**`\bads?\b` matches the "ad" in "ad-hoc", because a hyphen is a word boundary.** It fired on the GEAR
abstract at "stabilizing gradient dynamics without ad-hoc heuristics". GEAR is a true positive on two other
hits, "Ad Retrieval" in the title and "Douyin Ads" in the deployment sentence, so nothing was mis-banked
today. **The exposure is a pure recommender-systems paper that says "ad-hoc" once and nothing else**, which
would pass the filter on that alone. "ad-hoc" is ordinary machine-learning prose and appears constantly.

**The whole-word rule already in this file does not catch it.** That rule was written against substring
matches, naming "adaptive", "advanced" and "gradient", and `\bads?\b` correctly excludes all three. It was
never tested against a hyphenated compound whose first element is literally "ad".

**Shipped, because it is a literal exclusion with no judgement in it:** `lib/watchlist_check.py` now uses
`r"\bads?\b(?![- ]hoc)"`. Five regression cases are in `lib/_wl_20261001.py` and all five pass. A blanket
`(?!-)` was deliberately NOT used, because "ad-level" and "ad-set" are genuine advertising terms and would
have become false negatives.

**This stays separate from the first-or-last-sentence rule, which is still unshipped and should stay that
way.** That rule asks for a judgement about where meaning sits in a paragraph and it now has two known false
negatives (LS-083 on 2026-09-28, LS-084 on 2026-09-30). This one asks whether four characters are the word
"ad", which code can answer.

### An Ads & Commerce post that recaps a podcast is a POINTER, not a source: pull the episode (found 2026-10-02)

The 2026-10-01 feed carried *Turn your existing social assets into high-impact YouTube ads*. On its own it is **three
bullets and no numbers**: one product mention already banked at GA-068 and two pieces of generic creative advice. A run
that read it and moved on would have logged a quiet day.

It ends "Catch the full episode here" against an embedded player. **Pulling the video id and running the transcript
returned 3,049 words of a Google product manager for Demand Gen talking about creative**, and produced GA-091, GA-092 and
CR-283, including the only finding of the day that changes how we would brief a Demand Gen account. **Three of the four
claims banked on 2026-10-02 would have been missed by reading the post and stopping.**

**Method, verified today.** The embed is a `uni-youtube-player-article` element in the page HTML carrying
`video-id="..."`. `<article>`-scoped link extraction does NOT find it, because it is a sibling block outside the article
element; grep the whole page body for `video-id=`. Then:

```
".venv-research/Scripts/python.exe" ".claude/skills/advertising-science/lib/ytresearch.py" pull <video-id> --out "<run-dir>"
```

**Standing instruction: when an Ads & Commerce post embeds or links an episode, pull the episode transcript before
deciding the day is quiet.**

**This is the fourth instance of one failure shape on this watchlist**, after the locale partition (2026-09-20), the
missing title baseline (2026-09-23), the unread Demand Gen Drops back catalogue (2026-09-25) and the dropped
`#footnote-N` anchors (2026-09-25). **In every one, the thing being read was an index of the thing worth reading.** The
general rule this source family keeps teaching: on a Google or Meta publishing surface, assume the published page is a
summary of something else until you have checked what it points at.

### Merchant Center: the changelog is NOT in date order, its newest entry sits LAST, and "newest is 11 August" has been wrong since 24 September (found 2026-10-07)

The 2026-09-28 entry above corrects a date-regex bug on this source and closes with "Merchant Center's true newest entry has been 11 August 2026 throughout". **That closing sentence is wrong and it is retired.** The regex fix was right. The assumption underneath it, that the first dated entry in the page is the newest, was never checked.

**What the page actually is.** The announcement list is an `<ol>` of **78 `announcement__post` items, and it is not sorted by date.** Index 1 is 11 August 2026 near the top. **Index 77, the LAST item in the list, is 24 September 2026.** The four items before it are dated October 2025, October 2025, undated, and 1 July 2026. Several items carry no date at all.

| Read | Result |
|---|---|
| First date in page order | 11 August 2026, "Merchant Center performance reporting updates" |
| **Max over entry dates** | **24 September 2026, "Loyalty program updates: Loyalty Customer Match via Merchant API"** |
| Max over ALL dates in the visible text | 30 September 2026, which is a FUTURE REQUIREMENT inside the 28 April entry body, not an entry date |

**The method, and all three parts are load-bearing.** Extract `announcement__post-title` paired with its own `announcement__post-sub-head` date, accept an optional ordinal suffix and an optional comma per the 2026-09-28 rule, and take the **MAX over entry dates**. Never take the first date in page order, because the list is unsorted. Never take the max over all dates in the body text, because entry bodies announce future effective dates that are later than any entry.

**The entry itself is banked at [[Google PMax & Shopping#GP-049|GP-049]].** Low relevance to our book, no client on Shopping, and it is the finding about the reading that matters.

**This is the fifth instance of one failure shape on this watchlist** after the locale partition (2026-09-20), the missing title baseline (2026-09-23), the unread Demand Gen Drops back catalogue (2026-09-25) and the dropped `#footnote-N` anchors (2026-09-25). Previous four were all "the page is an index of the thing worth reading". **This one is narrower and sharper: the page IS the thing, and we read only the top of it.** A sixth-week restatement of the general rule: on any Google or Meta publishing surface, never assume the order on the page is the order of publication.

### The Developer Blog weekly check reads dates out of post BODIES, so the fetch script's `dates_first5` is not a post date (found 2026-10-07)

`lib/_weekly_20260928.py` prints `dates_first5` from a date regex over the whole fetched body. On this source that output is meaningless as a recency signal. Today it returned "October 7, 2026", "October 7, 2026", "October 1, 2026", "October 12, 2026", which reads like four fresh posts. **All four are dates INSIDE post text:** 7 October 2026 is the Google Ads API v22 sunset date, 1 October and 12 October 2026 are Display & Video 360 deprecation milestones.

**The correct read is the Atom feed's own `published` element, and it says the source is quiet.** 25 entries, newest **2026-09-23, "Announcing v25.2 of the Google Ads API"**, which predates the last completed weekly read on 2026-09-28. **Nothing new on this source.** Same correction applies to `changed: true`, which was reported for all three Google sources and only means the bytes differ between fetches.

**One live date came out of it and it is worth knowing: Google Ads API v22 sunsets 7 October 2026, which is today.** All v22 requests begin to fail from this date. We do not call the Google Ads API directly for client work, so there is no action, and a tool that does would break today.

### arXiv: the RSS lane IS backfillable through the API, so a missed build is not a lost build (found 2026-10-07)

Every arXiv note above treats the RSS feed as the lane and reasons about which build a run happens to read. The feed carries one build, so four consecutive failed runs (3 to 6 October, OAuth) looked like three unreadable builds and a permanent hole.

**It is not a hole. `export.arxiv.org/api/query` with `cat:cs.IR`, `sortBy=submittedDate`, `sortOrder=descending` and `max_results=250` returns the full submission history with titles and abstracts**, which covers any missed window. Run today across 2026-10-02 to 2026-10-07: **63 cs.IR submissions, and 0 passed the bank-list filter.** Date histogram: 6 Oct 16, 5 Oct 22, 4 Oct 12, 3 Oct 3, 2 Oct 10.

So the outage cost this lane nothing, and that is now verified rather than assumed. **Standing instruction: after any missed run, backfill arXiv through the API rather than recording the window as unchecked.** Note the API's `published` is the SUBMISSION date while the RSS announces on a separate schedule, so query a window one day wider than the gap on each side.

Today's own RSS read for the record: 35 items in the `Wed, 07 Oct 2026 04:00:03 +0000` build, 33 not previously seen (the count is cumulative over the outage, not a daily figure), **0 passing the filter**. The run fired at 07:03 UTC, after the 04:00 UTC rebuild, so this is today's build and the 2026-09-07 correction applies.

### Meta for Business News: the US shelf moved for the first time since the slug baseline existed, and the locale gap more than doubled (2026-10-07)

| Locale | Ceiling | Slugs | Against the 2026-10-02 baseline |
|---|---|---|---|
| `?locale=en_US` | **6 October 2026** | 12 | **2 added, 2 removed** |
| `?locale=en_GB` | 10 September 2026, Instant Hydration spotlight | 12 | 0 added, 0 removed |

**Added, both dated 6 October 2026 and both read in full at source:** `advertising-week-new-york-2026` (banked at [[Meta Delivery & Andromeda#MD-170|MD-170]] and [[Meta Delivery & Andromeda#MD-171|MD-171]]) and `a-new-way-for-businesses-and-personal-agents-to-work-together` (the Personal Agent Protocol with Sierra; **read in full and deliberately NOT banked**, no advertising, ad delivery, measurement or lead-capture content, logged here so a future run does not re-read it).

**Rotated out:** `holiday-advantage-is-creative-advantage` and `skip-the-single-surface-holiday-strategy`, both August back catalogue, which is the known 12-card rotation.

**The US-to-UK ceiling gap went from 11 days to 26.** It had been pinned at 11 days from 2026-09-23 through 2026-10-02, and the 2026-10-01 entry concluded the gap was a property of Meta's publishing rather than of our reading. That still holds and the gap is not a constant. **A run that read only one locale today would have reported this source either quiet or moved, depending purely on which one.**

**Transport.** WebFetch rendered `?locale=en_US` in English (US) and `?locale=en_GB` in English (UK), both on the first attempt, no Playwright profile used or needed. Fourth consecutive browser-free read of both shelves. The slug diff needed zero punctuation adjudication again.

### The weekly (Monday) lane was run on a WEDNESDAY, under the 2026-09-22 catch-up rule (2026-10-07)

Recorded because the rule has now fired twice. The 2026-09-22 entry says: if the previous Monday's run did not complete, run the weekly sources on the next day that does. **The research runs of 3, 4, 5 and 6 October all exited on `Failed to authenticate: OAuth session expired and could not be refreshed`**, which took Monday 5 October's weekly lane with it. Weekly sources were run today.

**All seven were read. Four of the seven are Meta properties and all four returned HTTP 400 to plain fetch**, consistent with every prior observation, and **WebFetch then read all four.** The 2026-09-22 ruling that "the whole Meta lane is unreadable when no Playwright profile connects" is now retired for the WEEKLY sources as well as for Business News, and on the same evidence: the 400 is about plain fetch, not about the lane.

| Weekly source | Transport that worked | Result |
|---|---|---|
| Marketing API changelog | WebFetch | **Index under-rendered to v25.0 again, see below** |
| Graph API changelog | WebFetch | **Unchanged. Newest v26.0, 29 July 2026** |
| Advertising Standards | WebFetch | **16 section headings, order and names IDENTICAL to baseline** |
| AI at Meta blog | WebFetch | Newest post 27 July 2026, nothing on advertising, ranking or measurement |
| Google Ads API release notes | plain fetch | 200, no new dated release surfaced by an ordinal-aware pattern |
| Google Ads Developer Blog | plain fetch | Newest post 23 September 2026, predates the last weekly read |
| Merchant Center changelog | plain fetch | **Newest entry is 24 September 2026, not 11 August, see above** |

**The Advertising Standards read is a partial close and the split matters.** The heading-level check is clean: 16 sections, in order, including section 7 as "Prohibited Commercial Practices" (the 2026-09-14 rename banked at MD-156) and section 16 rendering "Transparency requirements under the EU Digital Services Act" (the 2026-09-28 correction). **The per-section SHA-256 map CANNOT be diffed through WebFetch**, because WebFetch returns a rendered summary rather than the raw body the hashes were taken from. So a silent rewrite under an unchanged heading is still undetected, and the honest statement is that the hash map has not been diffed since 2026-09-28, nine days, and *Restricted goods and services* is the section ChiroWorks and StayWell depend on. **Method note for a future run: the heading check is browser-optional, the hash check is not.**

**The Marketing API index under-rendering artefact HAS reproduced, and the 2026-09-28 "treat it as fixed" is withdrawn.** That entry recorded the index rendering v26.0, v25.0 and v24.0 on a plain urllib fetch and declared the artefact fixed. Today WebFetch on the same URL lists only v25.0 (18 February 2026), v24.0 and v23.0, with v25.0 presented as newest. **The true newest is v26.0, 29 July 2026, confirmed on the Graph API changelog in the same session.** So the artefact is transport-dependent, it was never fixed, and the standing rule stands: a run reporting "newest is v25.0" from this index alone is seeing a rendering artefact, never a rollback.

**One live date out of the same read: Marketing API v24.0's Available Until was 6 October 2026, which was yesterday.** The 2026-09-28 entry flagged it as eight days out. It has now passed.

**A third page on this watchlist renders out of date order.** The AI at Meta blog listing presents 9 July 2026 first and 27 July 2026 third. With Merchant Center above and the known Business News card drift, that is three sources where position on the page does not imply recency. **Take the max over parsed dates on every listing source, never the first item.**
