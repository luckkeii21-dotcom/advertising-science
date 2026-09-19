# -*- coding: utf-8 -*-
"""2026-09-19: Harvest Log entry + run log."""
import pathlib

SCI = pathlib.Path(r"E:\claude code marketing skill\Obsidian God-level Marketing Vault\God-level Marketing\wiki\science")
RUNS = pathlib.Path(r"E:\claude code marketing skill\.claude\skills\advertising-science\runs")

ENTRY = """## 2026-09-19 (research run)

**1 transcript in, read in full. 6 claims added, 4 amended, 0 contested, 0 refuted. Backlog 0. Codex now holds 1,245 claim entries, 6 of them from this run. No law changed. One reading rule added, and one number this engine published twice is corrected.**

**The finding of the day is a correction to our own codex and it arrived for free.** CR-117 and CR-048 both carried a static that Nick Theriot said on 2026-09-07 had spent **$260,000** since 2025-07-19, in the words "this particular static ad right here". On 2026-09-18 he walked the same asset, same client, same headline, and gave it as **$234,853 over the last 12 months at a $27 cost per lead**, then added the half the first telling left out: "we do have it in three different cities. So that's why it's three different times right there. But if you put them all together, over $234,000 all was spent on this." **It is three ads, not one. Per ad that is roughly $78,300 across 12 months, so the tail point sits 52 to 112 times the $700 to $1,500 per-ad mean rather than the 170 to 370 times the codex recorded.** The two figures do not contradict, they differ on window: the asset was built 2025-07-19, so a trailing-12-month read drops its first seven weeks.

**The transferable rule: a headline single-ad spend figure is a SUM until the operator says otherwise.** CR-117's right tail is built on three such figures. This one shrinks by 3x. The other two, Charley T's $2 million ad and Blue Sense's quarter-million-a-month VSL, have never been re-told and carry exactly the same exposure. Nothing in CR-117 is refuted; the mean is still a mean and the tail still carries accounts. What moved is how much weight the tail can hold.

**Three Google products the codex had never heard of, all announced four months ago.** The Ads & Commerce feed's one new item was a podcast teaser that named three features in passing. All three were read on Google's own pages and all three were absent from this codex. **Journey-aware bidding (GA-076)** is the one with a consequence: Search campaigns on Target CPA and Maximize conversions "learn from both biddable and non-biddable conversion goals", which makes a third state available for a conversion action, feeding the prediction without entering the bid target. That is the exact reason a lead-gen account refuses to track its own back end, so it is worth a test once an account has a CRM uploading fast enough to matter. **Demand-led pacing (GA-077)** moves Search and Shopping spend between days inside a monthly budget, not live yet. **Lead intent scores (GA-078)** grade every form submission High, Medium or Low and do not feed bidding. All three are T1 for existence and surface only, with no figure, no eligibility and no method published for any of them. **The honest read is that this is a four-month hole in the Google lane rather than a news day**, and it was found by a podcast teaser rather than by the watchlist.

**Meta says an ad removal is not a fraud finding, and it said so in Polish (MD-160, T1).** Rebutting a third-party report that used removals as its fraud proxy, Meta names the taxonomy: enforcement fires across restricted goods and services, third-party intellectual property, ad quality and format, "oraz wielu innych", and many others, "a nie wylacznie oszustw", and not exclusively fraud. **Outward, any outside estimate of scam-ad revenue built on removal counts is inflated by an unpublished factor. Inward, and this is the half that touches our own accounts: a takedown on a client account says nothing about which policy fired until the notice itself is read.** Our chiropractic accounts sit under the health and personal-attributes sections and our dealership accounts under vehicle and finance rules, and guessing the category from the fact of a removal is the same error at account scale. Self-reported enforcement figures in the same post: 137,000 fraudulent ads removed in Poland July 2025 to June 2026, over 88% actioned before anyone reported them, and a scam-ad report rate per impression down 83% July 2024 to June 2026. **A report rate falling is equally consistent with fewer scam ads and with fewer people bothering to report, and Meta publishes no way to separate the two.**

**MD-149 restated, and one number did not survive the restatement.** The same post repeats the 100%-verification rule for financial-services advertisers targeting Poland and the target that by end-2026 90% of Meta's worldwide ad revenue comes from verified advertisers. **It drops the 70%-in-2025 baseline the 2026-08-28 post carried, so the 20-point move rests on the earlier post alone and has to keep being quoted from it.** New in this telling: Poland is in the first group of European countries on a new anti-impersonation AI system, which Meta says removed 50% more ads impersonating public figures than the system it replaced.

**A reading instrument for published ad-market estimates (MM-220, T3).** Meta's rebuttal itemises how the report's number was built, and the defects are generic to the whole class: reach for 27 EU countries applied to one country, frequency assumed at 3 from a US vendor's 2,800-customer sample, a CPM the authors admit they could not estimate empirically, 108 ads observed on one deliberately conditioned iOS profile, and a full-year figure extrapolated from three single days that differed from each other by up to 80%. **When a published figure about ad spend or ad exposure is reach times frequency times price, ask which of the three was measured.** Banked at T3 with the conflict of interest stated in the claim: Meta is a defendant in litigation brought by the party whose law firm prepared the report, and the report itself was not read here, so the five checks are adopted and the verdict on this report is not.

**Two creative claims from the transcript beyond the correction.** **CR-252 (new, T3):** a new mechanism has to compete on speed, price, simplicity or without-what-they-hate, and Theriot refuses accounts whose mechanism competes on none of the four, "they're just not going to do great when it comes onto Facebook ads". It is the cheapest pre-flight check in the creative file because it needs no account, no spend and no creative. **CR-023 lifted T4 to T3:** the five-stage sophistication ladder had been sitting on a book citation since August and now has an operator walking it against a live asset that has taken six figures of spend.

**The claim count correction.** Both 2026-09-18 run logs printed 1,240. **The committed vault at the end of that day holds 1,239, checked by counting headers at the commit itself: 1,239 headers, 1,239 distinct ids, no duplicates, no gaps in any prefix.** 1,239 plus this run's six is 1,245, which is what today's file holds. The likely cause is that day's cross-lane CR-248 collision, where both lanes wrote the same id and the fix removed one header after the count had been taken. **This is the first time the concurrency hazard has been shown to have moved a published total rather than merely threatened to.** Count against the committed file, never against yesterday's printed number.

**Watchlist, Saturday 19 September.**

| Source | Result |
|---|---|
| Meta Engineering (RSS) | HTTP 200, 9 items, **0 new** |
| Meta Newsroom (RSS) | HTTP 200, 10 items, **1 new**, the Polish scam-ads rebuttal, read in full, banked at MD-160 and as an MD-149 amendment |
| Meta for Business News | Browser, 12 cards, **0 new titles**, ceiling holds at 15 September 2026 |
| Google Ads & Commerce (RSS) | HTTP 200, 20 items, **1 new**, the Ads Decoded podcast teaser, read in full, three Google pages read behind it, banked at GA-076, GA-077, GA-078 |
| Google Ads Announcements | HTTP 200, **396 answer-href ids, 0 added, 0 removed** against yesterday's cache, byte-identical across two consecutive fetches |
| arXiv cs.IR (RSS) | HTTP 200, **feed empty, weekend build**, `lastBuildDate` Sat 19 Sep 04:00:03 UTC, 0 items, `skipDays` Saturday and Sunday |
| TikTok SDK changelog | HTTP 200, v0.1.8, unchanged |
| TikTok Newsroom, for-Business blog, Marketing API | Not checked. India geo-block, permanent, per Watchlist.md. **TikTok policy and creative news remains unmonitored** |
| Weekly (Mon) sources | Not due. Today is Saturday |

**Method notes worth keeping.** The Google Ads Announcements answer-href key held for a second consecutive day: 396 ids, identical across two fetches taken seconds apart, against the 3-of-30 per-render ids that made the script's own line diff useless on 2026-09-18. The script still printed 8 added and 1 removed today, all of it nav labels and session ids, which is the artefact the 2026-09-18 note describes. **Meta for Business News returned HTTP 400 on both the bare URL and `?locale=en_US`, and the browser opened it first try.** That is the seventh consecutive day the instruction "use the browser" has been right for this source.

**Gaps noticed.**

- **The Google lane missed the whole of Google Marketing Live 2026.** Three named products from May 2026 were absent from a codex that has run a daily Google check since August. The watchlist covers announcements, the blog and the release notes, and GML lands as a keynote none of the three fully enumerate. Worth a one-off backfill pass over the GML 2026 announcement hub rather than waiting for another podcast to mention something.
- **Two arXiv papers flagged unread on 2026-09-17 are still unread.** `2609.18296` (sponsored-search ads retrieval, ANGLE) and `2510.04816` (post-click conversion-rate counterfactual, ESCIM). Queued for a weekday run with room. They are unbanked, not discarded.
- **MD-160's operating consequence is untested on our own book.** Nobody has checked whether our clients' historical ad rejections carry a readable policy category in the notice. That is a 20-minute check across ChiroWorks, SJR Commercial and Phoenix Truxx and it would turn a T1 platform statement into something we can act on.

"""

hl = SCI / "Harvest Log.md"
txt = hl.read_text(encoding="utf-8")
MARK = "One line per Research run: what came in, what changed. Quiet days get one line and nothing else.\n\n"
assert MARK in txt
txt = txt.replace(MARK, MARK + ENTRY, 1)
hl.write_text(txt, encoding="utf-8")
print("Harvest Log updated")

RUNLOG = """# Advertising Science research run, 2026-09-19 (Saturday)

**1 transcript in, read in full. 6 claims added, 4 amended, 0 contested, 0 refuted. Backlog 0. Codex 1,239 to 1,245. No law changed.** Run started 14:29 IST, merge written 14:50 IST.

## What was banked

| Claim | Tier | What |
|---|---|---|
| CR-252 | T3 | A new mechanism has to compete on speed, price, simplicity or without-what-they-hate; the operator refuses accounts that answer none of the four |
| MM-220 | T3 | Reading instrument for a published ad-spend estimate built as reach times frequency times CPM, with the five checks |
| MD-160 | T1 | Meta says an ad removal is not a fraud finding; enforcement fires across restricted goods, third-party IP, ad quality and format too |
| GA-076 | T1 | Journey-aware bidding: Search, Target CPA and Maximize conversions, learns from non-biddable goals, beta |
| GA-077 | T1 | Demand-led pacing: Search and Shopping spend follows demand inside a monthly budget, not live |
| GA-078 | T1 | Lead intent scores: High, Medium, Low on every form submission, prioritisation only, not a bidding input |

Amended: **CR-117** and **CR-048** (the $260,000 static is a three-ad sum), **CR-021** (the winning line decomposed, mechanism naming), **CR-023** (five-stage ladder, lifted T4 to T3), **MD-149** (restated, 70% baseline absent from the new telling, anti-impersonation system added).

## The correction, stated plainly

The codex held a static at $260,000 lifetime spend from a 2026-09-07 telling that said "this particular static ad right here". The 2026-09-18 telling of the same asset gives $234,853 over the last 12 months at a $27 cost per lead and discloses that it runs as three ads in three cities, summed. **Roughly $78,300 per ad.** CR-117's right tail loses one of three six-figure single-ad points. The rule: a headline single-ad spend figure is a sum until the operator says otherwise. The other two tail points in that claim have never been re-told.

## The count correction

Both 2026-09-18 run logs printed 1,240 claims. Counting headers at the committed vault revision returns **1,239 headers, 1,239 distinct ids, no duplicates, no gaps in any prefix**. 1,239 + 6 = 1,245, which is today's file. Today's file verified the same way: 1,245 headers, 1,245 distinct, no duplicates, every prefix contiguous from 1 to max, every heading carrying a Tier line. Tier split 111 T1, 126 T2, 850 T3, 158 T4; status split 1,138 active, 101 contested, 5 superseded, 1 refuted; both columns sum to 1,245.

## Harvest

`harvest.py daily`: 12 channels, **1 new transcript**, 13 skipped short, 0 without subtitles, 0 out of window, **0 errors, 0 RSS fallbacks**. New: Nick Theriot, "This Static Ad Spent $234,853 (Here's How)", 2026-09-18, 1,808 words, 8 minutes. Marked `extracted: true` after reading.

Note against yesterday: the 2026-09-18 run logged 12 RSS fallbacks, all HTTP 404. Today's run had zero. Nothing was changed in the script, so treat the fallback list as a transient upstream condition rather than a fault to chase.

## Watchlist

| Source | Result |
|---|---|
| Meta Engineering (RSS) | 200, 9 items, 0 new |
| Meta Newsroom (RSS) | 200, 10 items, **1 new**, read in full, banked |
| Meta for Business News | Browser, 12 cards, **0 new titles**, ceiling holds at 15 Sep 2026 |
| Google Ads & Commerce (RSS) | 200, 20 items, **1 new**, read in full, three Google pages read behind it, banked |
| Google Ads Announcements | 200, **396 answer ids, 0 added, 0 removed**, identical across two fetches |
| arXiv cs.IR (RSS) | 200, **empty, weekend build**, lastBuildDate Sat 19 Sep 04:00:03 UTC, skipDays Sat and Sun |
| TikTok SDK changelog | 200, v0.1.8, unchanged |
| TikTok Newsroom / blog / Marketing API | Not checked, India geo-block, permanent. TikTok policy and creative news unmonitored |
| Weekly (Mon) sources | Not due, Saturday |

## Errors and environment

- **`playwright` and `playwright-arcads` MCP servers both failed to connect** (CONNECT_TIMEOUT, 30s). `playwright-higgsfield` connected and did the Meta for Business News read. Third consecutive day the primary Playwright profile has been unavailable at session start. Try every configured profile before logging a browser source unchecked.
- **`rizzdial` MCP failed to connect** (ENDPOINT_NOT_FOUND). Not used by this lane.
- **Meta for Business News returned HTTP 400** on both the bare URL and `?locale=en_US`. Browser opened it first try. Seventh consecutive day.
- **`watchlist_check.py` reported 8 added and 1 removed on Google Ads Announcements.** All artefact: 7 nav labels and 1 per-render session id. The answer-href set diff is the key that works, per the 2026-09-18 Watchlist note. The script's own line diff should not be quoted as news and should be fixed to use the answer-href set.
- Watchlist cache committed. Harvest json written to `runs/2026-09-19-1431-harvest.json`.

## Gaps for tomorrow

1. **Backfill Google Marketing Live 2026.** Three named products from May were missing from a codex running a daily Google check. GML is a keynote the three watchlist Google sources do not fully enumerate. One pass over the GML 2026 announcement hub would close it.
2. **Two arXiv advertising papers still unread**, flagged 2026-09-17: `2609.18296` (ANGLE, sponsored-search retrieval) and `2510.04816` (ESCIM, post-click CVR counterfactual). Unbanked, not discarded.
3. **MD-160 is untested against our own accounts.** Check whether historical ad rejections on ChiroWorks, SJR Commercial and Phoenix Truxx carry a readable policy category in the notice. Roughly 20 minutes, and it converts a platform statement into something operable.
4. **Fix the Google Ads Announcements diff in `lib/watchlist_check.py`** to use `/google-ads/answer/(\\d+)` set membership instead of a line diff. It has printed noise on two consecutive days.
"""

(RUNS / "2026-09-19-research-log.md").write_text(RUNLOG, encoding="utf-8")
print("run log written")
