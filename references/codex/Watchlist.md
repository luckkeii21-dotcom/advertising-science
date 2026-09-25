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

**Backlog, eight posts, queued:** June 2026, April 2026, March 2026, February 2026, January 2026,
December 2025, November 2025, October 2025, plus the introduction post. Body extraction: strip tags,
then anchor on `Social Module` and read to `Return to top of page`. Anchoring on the post title fails
on some of them because the chrome repeats it.

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
