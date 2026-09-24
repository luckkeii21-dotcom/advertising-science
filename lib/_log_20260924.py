"""Prepend the 2026-09-24 research entry to the Harvest Log."""
from pathlib import Path

LOG = Path(r"E:\claude code marketing skill\Obsidian God-level Marketing Vault"
           r"\God-level Marketing\wiki\science\Harvest Log.md")

ANCHOR = "One line per Research run: what came in, what changed. Quiet days get one line and nothing else."

ENTRY = """
## 2026-09-24 (research run)

\u26a0 **Meta now caps organic Facebook Page link posts at 2 a month on the free tier, and sells the increase through Meta One. Links in ads are exempt, so no client campaign is affected. Client ORGANIC posting is.** Read at source on Meta's own help centre today. This entry also corrects a call this engine made on 2026-09-15.

**3 transcripts in, 7 new claims, 8 merges, 0 contested, 0 refuted, 0 harvest errors, 0 watchlist errors.** The YouTube roster carried the day. The Meta lane was fully readable for the second consecutive day and returned nothing new.

### 1. YouTube harvest

`harvest.py daily` ran clean. **3 new transcripts, 11 skipped short, 1 missing subtitles, 0 errors, 0 RSS fallbacks.**

| Channel | Video | Outcome |
|---|---|---|
| nick-theriot | I tested ABO & Cost Caps (here's the results), 20 min | AU-095, SC-171, SC-172, MD-167, merges into SC-044, SC-008, SC-161, AU-051 |
| ben-heath | I paid Alex Hormozi $235,000 for his Facebook Ads Strategy, 17 min | CR-265, merges into MD-125, LS-074 |
| jon-loomer | Meta Wants Businesses to Pay to Share Links, 10 min | Triggered the MD-166 source read. Banked on Meta's page, not on his |

**The RSS fallback count went to zero for the first time since 2026-09-05.** Every run since then has logged 12 fallbacks because YouTube's `feeds/videos.xml` endpoint was returning 404 or 500 for every channel and `harvest.py` was falling through to the `/videos` tab via yt-dlp. Today it did not need to. Recorded as an observation, not as a fix: nothing in our code changed, so this is YouTube's endpoint behaving, and it may not hold tomorrow.

Unextracted backlog after the run: **0**. The 25-a-day rule never engaged.

### 2. Watchlist

**Browser: the `playwright` profile connected on the first attempt and did every Meta read.** Second consecutive day with a working browser after the 2026-09-22 zero-browser outage.

**Meta for Business News, both locales, and the title diff the 2026-09-23 entry set up ran mechanically for the first time.**

| Locale | Ceiling | Result |
|---|---|---|
| `?locale=en_US` | 21 September 2026, Meta Agency Awards | **12 titles, byte-identical to the cached set, same order. 0 new** |
| bare URL (renders en_GB) | 10 September 2026, Instant Hydration | **12 titles, identical to cache. 0 new.** Now twelve days behind the US shelf |

**This is what the diff is supposed to look like on a quiet day**, and it took nine days of notes to get here. The baseline written yesterday did its job: two locale reads, two clean comparisons, zero judgement calls about rotation or date drift.

| Source | Result |
|---|---|
| Meta Engineering (RSS) | 200, build 24 Sep 00:02 UTC. **1 new: Private Processing on Meta AI Glasses.** Read for ad content, none, not banked |
| Meta Newsroom (RSS) | 200, build 24 Sep 06:15 UTC. **3 new, all 23 Sep, all Connect hardware:** Ray-Ban Display features, Meta VR Glasses, Ray-Ban Meta Audio. All three scanned in full for advertising content. **The only match in any of them is the cookie banner.** Not banked |
| Google Ads & Commerce (RSS) | 200, build 23 Sep 08:30 UTC. **1 new, and it is real platform news:** AI Brief in seven more languages plus a new AI Max reporting feature. Read in full, banked at GA-080 |
| Google Ads Announcements | 200. **396 answer ids, 0 added, 0 removed.** Fifth consecutive clean run on the set diff shipped 09-20 |
| TikTok SDK changelog | 200, unchanged at v0.1.8 |
| arXiv cs.IR (RSS) | 200, **today's own 04:00 UTC build**, 32 items, 28 new, **0 passed the ad filter.** Normal |

Weekly (Mon) sources were not due. Monday 09-22 ran them as catch-up, so the lane recorded on 2026-09-22 is current.

**TikTok product and policy news remains unmonitored** behind the permanent India geo-block. Only the SDK changelog answered, so this lane is not logged as clean.

**The checker committed.** `last_run` carries today's date, per the rule added 2026-09-23.

### 3. Claims merged

**7 new, 8 merges, 0 contested, 0 refuted.** A full duplicate scan across all eleven topic files after the merge returns **1,294 claims and zero duplicate IDs**.

| ID | Topic | Tier | Claim |
|---|---|---|---|
| MD-166 | Meta Delivery | **T1** | Facebook Pages capped at 2 organic link posts a month free, 8/20/unlimited by Meta One tier; **links in ads exempt** |
| MD-167 | Meta Delivery | T4 | The same post ID in two live campaigns appears to self-compete: $3,600 in one, $26 in the other |
| AU-095 | Auction | T2 | The cost-cap ratchet: open at $30 under a $50-60 average, +$5 every 2-3 days, and raise the BUDGET freely |
| SC-171 | Scaling | T2 | An ABO testing campaign cost ~$10k for what the operator estimates a CBO would learn for ~$2k |
| SC-172 | Scaling | T2 | Across 51 ad-set tests, killing the top-spending ad to feed a cheaper sibling failed 99% of the time |
| CR-265 | Creative | T3 | A portfolio operator reports BETTER results post-Andromeda, at 50+ new ads a week per business |
| GA-080 | Google Auction | T1 | Google's unified Search-ads-journey report for AI Max, plus AI Brief in 7 more languages, no ship date |

**Merges:** MD-157, MD-125, SC-044, SC-008, SC-161, AU-051, LS-074, GA-043.

### The correction, and it is ours

**On 2026-09-15 this log banked Meta One at MD-157 and deliberately withheld a \u26a0, writing: "Meta One removes nothing, bans nothing and breaks nothing. It is a new optional product, so it gets a headline and not an alarm."** That was written off Meta's announcement, which lists "links in organic posts and Reels" as a feature the subscription unlocks.

Meta's help centre states the same change as a cap. Free and Essential tiers: **2 organic Facebook Page posts or comments carrying links per month.** Advanced $49.99: 8. Expert $149.99: 20. Max $499.99: unlimited. Resets on the 1st, or on the renewal date for subscribers, no rollover.

**The failure mode is worth naming because it will recur.** A feature list and a limit table describe the same product from two ends, and only one of them reads as a restriction. Reading the announcement alone is how a paywall gets logged as a product launch. The rule that follows: when a platform announces that a subscription "unlocks" something users already do, go find the page that states the free-tier number.

**What does NOT change, and it is most of it.** Links in ads are exempt. So are links to Meta properties, affiliate-partnership links, and additional links inside the comments of a post that already carries one. Nothing in this touches delivery, cost or ranking on any client campaign. MD-157's closing line, that nothing in Meta One touches ad delivery, survives intact.

**Meta's own hedge, quoted because it has to travel with the claim:** "Limits on posts and comments with links may not apply to all Pages." Meta does not say which. Nobody can state from this article whether a given client Page is subject to it.

### Source discipline, exercised twice

**Once against a practitioner.** Jon Loomer's video is what surfaced this, and two of his specifics did not survive the source read. He states per-tier Instagram splits (8 Facebook plus 4 Instagram at Advanced, 20 plus 8 at Expert); **the article is Facebook Pages only and publishes one number per tier with no Instagram split**, so those figures are unverified and are not in the claim. He states that a link in the comments does not get around the limit; **Meta exempts extra links in the comments of a post that already carries one.** MD-166 is banked on Meta's page. Loomer is credited as the pointer, not as the source of a number.

**Once against Meta.** The help centre prints Expert **$149.99** and Max **$499.99**. The Meta for Business announcement, re-read in full on the same day, prints **$149.00** and **$499.00**. Two Meta surfaces, one day, a dollar apart. Third documented self-contradiction on this source after the card-date drift (2026-09-14) and the locale partition (2026-09-20).

### The count nobody has ever produced

**SC-008 has been `contested` since 2026-08-19** on whether to kill an ad eating an entity's budget: four operators asserting leave-it-on, one asserting kill-the-worst-profit, **zero numbers from anyone on either side**.

Theriot ran 51 ad-set tests and reports the reflex failing: "99% of the time that we tested, in all of these different 51 tests... turning off the top spending ad and putting spend towards the lower spending ad that was converting way better, 99% of the time it did not hold performance at all." His response was structural rather than tactical: he stopped reading the ad level inside a testing campaign and now kills whole ad sets.

**It does not close SC-008 and SC-172 says so on its face.** Different structure (ABO within an ad set, not CBO within a campaign), and "99% of 51" is recalled on camera with no log, no definition of "did not hold performance" and no before-and-after CPA on any of the 51. It is still the only number either side has produced in five weeks.

### An operating rule that changed shape

**SC-044's 3x kill gate has been carrying two different anchors and nobody had noticed.** Charley T and Matt Shiver state it against TARGET cost per result. Theriot states it against ACCOUNT AVERAGE. In a healthy account those converge. In a rescue they do not: an account at a $300 cost per purchase against a $100 target burns **$900 an ad set** on the account-average version to learn nothing.

Theriot's own fix is to swap the anchor to 3x AOV in that case, taking his example from $900 to $300. Merged into SC-044 as: **3x the smaller of target CPA and AOV, over at least 3 days.** This matters for us specifically, because takeover accounts arrive running far off target by definition.

### Read in full and deliberately not banked

- **Three Meta Connect hardware posts** (Ray-Ban Display features, Meta VR Glasses, Ray-Ban Meta Audio, all 23 Sep) and **Private Processing on Meta AI Glasses** on Meta Engineering. All four scanned end to end for advertising, monetisation or campaign content. **The only match in any of the four is the cookie consent banner.** No new ad surface is announced in any of them.
- **Most of the Ben Heath video.** A sponsor read, a Skool pitch, and the qualified-lead-event walkthrough, which is a clean restatement of material already banked at LS-008, LS-011, LS-074, AT-030 and CR-096 and added no mechanism. Only the creative-volume claim and the OTP corroboration were taken.

### 4. Skill update

**No law moved.** The hot layer in `SKILL.md` was rewritten at its opening paragraph for four things: the MD-166 correction of this engine's own 2026-09-15 call, the SC-172 count on SC-008, the SC-044 anchor split, and the two things that did NOT move (zero controlled cost-cap comparisons still, GA-043 still open).

### 5. Errors and gaps

**Errors: 0 in the harvest, 0 in the watchlist checker, 0 browser failures.**

**Gaps, carried forward:**

1. **Still open from 09-22:** read the Haus Black Friday report at source to upgrade AT-122 to T2, and read arXiv 2603.01590v2 (IDProxy, Xiaohongshu) in full rather than from its abstract.
2. **Still open from 09-23:** the Cyber 5 method footnote does not parse (AU-094); CR-261's 7.3% has no stated comparison group; the generative-AI shopping figures cited only to "Forbes, December 2025" are unchased.
3. **New: MD-166's scope is unknown for our own clients.** Meta says the limit "may not apply to all Pages" and names no criterion. **Nobody has checked whether the ChiroWorks, StayWell, SJR Commercial or Phoenix Truxx Pages are subject to it.** That is a five-minute check inside each Page and it has not been done.
4. **New: MD-167 has a cheap test nobody ran.** Pause the ad in the first campaign for 72 hours and read the second campaign's spend on the same post ID. Until someone does, the self-competition read and a plain starvation read are indistinguishable.
5. **New: GA-080 has no ship date.** "Later this year" is all Google states. Re-check the Google Ads release notes on the next weekly Monday lane rather than waiting for the blog to repeat itself.
"""

text = LOG.read_text(encoding="utf-8")
assert ANCHOR in text
text = text.replace(ANCHOR, ANCHOR + "\n" + ENTRY.rstrip() + "\n", 1)
LOG.write_text(text, encoding="utf-8")
print("harvest log entry prepended, %d chars" % len(ENTRY))
