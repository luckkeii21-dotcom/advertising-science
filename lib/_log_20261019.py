# -*- coding: utf-8 -*-
"""Harvest Log and Watchlist writes for the 2026-10-19 research run."""
from pathlib import Path

V = Path(r"E:\claude code marketing skill\Obsidian God-level Marketing Vault\God-level Marketing\wiki\science")

HL = V / "Harvest Log.md"
HL_ANCHOR = "One line per Research run: what came in, what changed. Quiet days get one line and nothing else.\n"

HL_ENTRY = """
## 2026-10-19 (research run)

**The biggest Meta haul in a month, and it came from a source this engine had never read.** 0 transcripts, 8 claims banked, all T1, law layer and one watch item amended. Monday, so the weekly lane ran.

- **Harvest:** `lib/harvest.py daily`, all 12 roster channels, **0 new transcripts, 0 errors**, 3 skipped short, 1 no subtitles. Unextracted backlog is 0.
- **The find.** The Marketing API changelog has MOVED to `developers.facebook.com/documentation/ads-commerce/marketing-api/marketing-api-changelog`, the old URL redirects, and **the under-rendering defect this watchlist has recorded since 2026-08-24 is CLOSED**: the page now correctly names v26.0 as newest instead of stopping at v25.0. The new page exposes a per-year **Out-Of-Cycle Changes** shelf going back to 2023 that nothing on the watchlist had ever pointed at. The 2026 shelf is 20 entries, 17 February through 22 October 2026, and it was read in full in one pass.
- **8 new claims: MD-182, MD-183, AT-128, AT-129, AT-130, GA-095, GA-096, GP-050.** Codex 1,371 to **1,379**.
- **⚠ The one with teeth is AT-128, and it is a silent failure in our own reporting.** Three Ads Insights breakdowns require per-account enablement from 6 August 2026 (`impression_device`, `hourly_stats_aggregated_by_audience_time_zone`, `frequency_value`), and Meta's own sentence is that a gated account "may return no results", not an error. An empty pull and a genuine zero look identical. **Any frequency or hour-of-day number we have pulled through the API since 6 August needs its account checked for enablement before it is quoted again.**
- **AT-129, a measurement instrument swapped mid-year.** Nielsen DMAs retired for Comscore Markets on 22 June 2026 across targeting AND reporting; `breakdowns=dma` unsupported; no crosswalk published. Our book is entirely local, so any market-level series that spans that date is two different partitions of the map.
- **MD-182, demographics moved onto the creative.** Creative audience pairing sets age and gender on the ad creative instead of the ad set, opt-in per ad set, with a persona attachable per media asset and the asset's persona overriding the ad's. Capability only, zero published effect.
- **MD-183, three Advantage+ enhancements that alter the footage**, all 28 June 2026: Image Animation, Video Filter (including SDR to HDR) and Video Uncrop. Added to the existing enhancement-audit watch item. Default state is NOT stated in the change notes, which is a real difference from Flex Media, so it has to be read off a live ad.
- **Google v26, released 14 October.** GA-095 two API releases a month from v26 with the support window unchanged and the release blog dropping to twice a quarter. GA-096 a budget floor named twice, a Search "budget too low" recommendation and a per-currency Demand Gen minimum daily budget. AT-130 Search Lift studies became a queryable API resource with 15 metrics. GP-050 Local Services Performance Max is externally creatable, one per account, welded to one Google Business Profile listing with a locked goal.
- **Watchlist, all lanes:** Meta Engineering 0 new, Meta Newsroom 0 new, Google Ads & Commerce 0 new, Google Ads Announcements 396 answer ids 0 added 0 removed, arXiv empty (Monday run before 04:00 UTC, so Sunday's build, the documented case), TikTok SDK unchanged at v0.1.8, both Meta for Business News shelves 0 added 0 removed and identical in order to 2026-10-18. Weekly lane: Graph API changelog unchanged at v26.0, Merchant Center 79 answer ids 0 added 0 removed, AI at Meta blog unchanged and 84 days flat, Demand Gen Drops hub unchanged at 13 cards, Advertising Standards unchanged on both locales.
- **Two method findings filed in [[Watchlist]].** The Advertising Standards heading list must be matched case-insensitively, because the UK locale renders every section in sentence case with different hyphenation and a case-sensitive US list produces a false "section missing" on the two sections our clinic accounts depend on. And the Google Ads Developer Blog Feedburner feed carries each post's FULL body in its `content` element, which retires the post-body regex route and the WebFetch-returns-chrome problem recorded on 2026-09-07 and 2026-09-22.
- **Gaps noticed.** The 2023, 2024 and 2025 out-of-cycle shelves are unread, three years of T1 Meta platform documentation. Same failure shape as the Demand Gen Drops backlog of 2026-09-25 and the locale partition of 2026-09-20: a source can be watched daily and still have years of material behind it. The Demand Gen minimum daily budget for USD is one API call away and nobody has read it. Four entries on the 2026 shelf were read and deliberately not banked (Threads ads x3, Creator Marketplace, partnership ad codes, WhatsApp marketing messages, `audience_labels`) because no client on our book runs them.
"""

s = HL.read_text(encoding="utf-8")
assert s.count(HL_ANCHOR) == 1
s = s.replace(HL_ANCHOR, HL_ANCHOR + HL_ENTRY, 1)
HL.write_text(s, encoding="utf-8")
print("Harvest Log updated")

WL = V / "Watchlist.md"
WL_ADD = """

### The Marketing API changelog MOVED, and the under-rendering defect is CLOSED (2026-10-19)

Every note on this source since 2026-08-24 records the same defect: the changelog index rendered only
through v25.0 and stated that the latest version was v25.0, while the true newest was v26.0 of 29 July
2026, confirmable only from the Graph API changelog. It was re-observed on 2026-09-28, 2026-10-07 and
2026-10-12, and the 2026-09-28 "treat it as fixed" was withdrawn.

**It is fixed, and the page moved.** `developers.facebook.com/docs/marketing-api/marketing-api-changelog`
now redirects to **`developers.facebook.com/documentation/ads-commerce/marketing-api/marketing-api-changelog`**,
which renders correctly: "The latest Graph API version is: v26.0", with v26.0 (29 July 2026), v25.0
(18 February 2026) and v24.0 (8 October 2025) listed. Update the watchlist URL to the new path; the old
one works through the redirect but the browser lands on the new address.

**Two "Available Until" dates MOVED BACKWARDS INTO THE FUTURE, and this retires an open worry.** The
2026-09-28, 10-07 and 10-12 entries tracked Marketing API v24.0 as "Available Until 6 October 2026", a
date that passed with no action. It now reads **10 November 2026**, and v25.0 moved from TBD to
**23 February 2027**. **So a Marketing API "Available Until" date can be EXTENDED after it has passed.**
Never report a passed sunset date on this source as a shutdown, and never raise it as a risk without
re-reading the page.

**The real find: a per-year OUT-OF-CYCLE CHANGES shelf that nothing on this watchlist pointed at.** The
new page's nav carries `out-of-cycle-changes/occ-2023`, `occ-2024`, `occ-2025` and `occ-2026`. The 2026
shelf is **20 entries, 17 February through 22 October 2026**, auto-generated every two weeks from the API
spec, and it is T1 Meta platform documentation on delivery, creative, targeting and reporting mechanics.
It was read in full on 2026-10-19 and produced five of the day's eight claims. **The 2023, 2024 and 2025
shelves are unread.**

This is the fourth instance of the same failure shape, after Meta for Business News on 2026-09-20 (a
three-part series unread for four months behind a locale partition), 2026-09-23 (four posts unread
because no title baseline existed) and the Demand Gen Drops hub on 2026-09-25 (a year of instalments
behind a source watched daily). **The pattern, now four for four: a ceiling check answers "has the
newest thing changed" and says nothing about the shelf behind it. A source can be read every morning
for two months and still have years of unread material in view.** Add `occ-2026` to the weekly lane and
work the 2025 shelf as a backlog.

**One date artefact, and it is the same one recorded on Meta for Business News on 2026-10-17.** The 2026
shelf declares itself "Updated: Oct 22, 2026" and its newest entry is dated 22 October 2026, three days
ahead of the clock on the day it was read. Per the 2026-10-18 refinement, a future date on a Meta
property is a fixed publication date the clock catches up to, not a render offset. Read it once; do not
re-read daily waiting for the date to arrive.

### Meta Advertising Standards: the UK locale renders every heading in SENTENCE CASE, and a case-sensitive US list reports the two sections our clinics depend on as MISSING (found 2026-10-19)

The 2026-09-14 entry made it a standing instruction to read both `/policies/ad-standards/` and
`/en-gb/policies/ad-standards/`, because Meta stages policy rewrites by locale. That instruction is
right. **What it does not say is that the two locales disagree on the ORTHOGRAPHY of almost every
heading, so the US heading list cannot be reused against the UK page as-is.**

Observed 2026-10-19, same browser session, both pages read minutes apart:

| US render | UK render |
|---|---|
| Prohibited Commercial Practices | Prohibited commercial practices |
| Product and format-specific policies | Product- and format-specific policies |
| Privacy Violations and Personal Attributes | Privacy violations and personal attributes |

**The consequence is a false alarm on the highest-consequence section on this whole watchlist.** A
case-sensitive run of the US list against the UK page returned `Product and format-specific policies`
as NOT-FOUND and `Privacy Violations and Personal Attributes` as absent. **Neither is absent. Both are
present in sentence case, and the hyphen in "Product-" is an additional difference that no case fold
fixes.** The baseline note in `cache/meta-ad-standards-baseline.md` says a heading that "moved, added or
disappeared" means read the section in full and open a claim, so this artefact would have produced a
policy-removal finding on the personal-attributes rules that ChiroWorks and Chiropraise run against.

**Method, for every future run: match the heading list CASE-INSENSITIVELY and treat hyphens as optional,
or keep a separate UK heading list. Never report a section as missing from one locale until it has been
searched for in that locale's own casing.**

**What the corrected UK read actually found: unchanged, and it closes a 2026-09-14 question.** All 16
sections located with zero not-found, 33,587 chars of `innerText`, and both `Health and Wellness` and
`Privacy violations and personal attributes` present. **`Prohibited commercial practices` is 199 chars
in the UK locale and `Prohibited Commercial Practices` is 199 chars in the US locale**, so the section
rename banked at MD-156 on 2026-09-14 has now propagated to both locales at identical length. The
locale-staging concern that entry raised for this section is resolved.

**First UK section-hash map ever recorded**, saved in `cache/watchlist-seen.json` under
`pages.meta-ad-standards.section_map_uk_2026_10_19`. Before today only the US page had one, so a silent
UK-only rewrite was undetectable. From the next run it is diffable.

**The US page is unchanged.** 32,505 chars, exactly the 2026-09-28 and 2026-10-12 figure, all 16 sections
byte-identical to the 2026-10-12 hashes.

**Anchor method, stated precisely because it was nearly got wrong today.** The 2026-10-12 note calls it
"the offset-0 anchor". That phrasing is ambiguous and a literal `indexOf(name)` from position 0 is WRONG:
`Community Standards` occurs 20 times on the US page, and a from-zero search put section 4 at 25,944
chars instead of 483. **The working method is a SEQUENTIAL scan: search for each heading starting from
the end of the previous heading's match.** That reproduces the 2026-10-12 figures exactly.

### Google Ads Developer Blog: the Feedburner feed carries the FULL post body, which retires the post-body regex (found 2026-10-19)

Two notes above this one are about failing to extract a Developer Blog post body. On 2026-08-31 WebFetch
returned the chrome without the article and cost GA-069 its primary source. On 2026-09-07 the fix was
recorded as "plain urllib plus a `post-body` div regex", and on 2026-09-22 that route itself returned
nothing on the `new-onboarding-experience-for-google-ads-api.html` permalink, leaving that post unread.

**Neither is necessary. The Atom feed at `feeds.feedburner.com/GoogleAdsDeveloperBlog` carries each
post's entire body inside its `<content>` element.** Both new posts of 2026-10-12 and 2026-10-14 were
read in full from the feed on the first attempt, including the complete 2026-2027 release and sunset
tables, with no permalink fetch and no browser. 25 entries are in the feed, which is roughly a two-month
window.

**Method for this source from now on: read titles, dates AND bodies from the Feedburner feed. Only fetch
a permalink when a post has aged out of the 25-entry window.** The 2026-09-22 unread post is recoverable
this way if it is still in range.

### Google Ads API release notes: the VERSION HEADING set is the stable key, confirmed by a real change (2026-10-19)

The 2026-10-12 entry established that a raw byte diff on `developers.google.com` is meaningless because
the page carries a per-render script nonce, and prescribed diffing the version-heading set instead.
**That method has now caught its first real change.** Cached headings on 2026-10-12: v25, v24, v23, v22.
Today: **"Release summary and quick links", "v26 major version", v25, v24, v23**. So v26 appeared and v22
dropped to the archive, and a new summary section was added. The raw byte count also changed, from
371,961 to 376,334, but it changes on every render anyway and says nothing.

**Merchant Center, same weekly check, same stable-key approach: 79 `/merchants/answer/(\\d+)` ids, 0 added
and 0 removed against the 2026-10-12 cache.** The answer-id set is a better key on this source than the
bare-line entry dates the 2026-10-12 note had to qualify twice.
"""

s = WL.read_text(encoding="utf-8-sig")
if not s.endswith("\n"):
    s += "\n"
WL.write_text(s + WL_ADD, encoding="utf-8")
print("Watchlist updated, +", len(WL_ADD), "chars")
