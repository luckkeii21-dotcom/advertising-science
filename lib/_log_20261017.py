# -*- coding: utf-8 -*-
"""2026-10-17 research run: watchlist note, harvest log entry, transcript flag, run log."""
import io
import json
import re
from pathlib import Path

ROOT = Path(".")
SCI = ROOT / "Obsidian God-level Marketing Vault/God-level Marketing/wiki/science"
SKILL = ROOT / ".claude/skills/advertising-science"
TRANSCRIPT = (ROOT / "Obsidian God-level Marketing Vault/God-level Marketing/wiki/sources/"
              "transcripts/nick-theriot/"
              "2026-10-16--nick-theriot--30kday Facebook Ads Campaign Structure.md")


def read(p):
    return io.open(p, encoding="utf-8").read()


def write(p, s):
    io.open(p, "w", encoding="utf-8", newline="\n").write(s)


# ------------------------------------------------------- 1. transcript extracted
t = read(TRANSCRIPT)
t2 = t.replace("extracted: false", "extracted: true", 1)
assert t2 != t, "extracted flag not found"
write(TRANSCRIPT, t2)
print("transcript flagged extracted")

# ------------------------------------------------------- 2. Watchlist note
wl = SCI / "Watchlist.md"
note = """

### Meta for Business News: a post can be dated in the FUTURE, which is a fourth distinct date artefact on this source (found 2026-10-17)

The US shelf moved by one head-of-list event today: `meta-nest-ai-creative-diversification` in at slot 1,
`game-changers-series-1` out of slot 12, the other eleven shifting down one. That is the 12-slot window
behaviour recorded on 2026-10-10, so it is ONE event and not two rotations. The post was read in full and
banked at [[Creative Science#CR-286|CR-286]].

**The new card is dated 19 October 2026, two days after the read, and its own post header carries the same
future date.** Every other date finding on this source is about a disagreement between two renderings of a
past date: the one-day timezone drift across cards (2026-09-14), the two-day card-against-post gap
(2026-09-23), and the format difference between a card and a post header (2026-09-20). **This one is not a
disagreement. Both surfaces agree and both are ahead of the clock.**

**Two consequences for the method.**

- **Never treat a future-dated card as a render fault, a parse failure or a cache artefact. Read the post.**
  A ceiling check that asks "is the newest card date later than the last read" passes this correctly by
  accident; a check that sanity-tests a parsed date against today would reject the only new item on the
  shelf.
- **The 2026-09-23 rule, cite the date from the post and never from the card, does not help here**, because
  the post agrees with the card. The honest citation is the published date as Meta states it, with the read
  date beside it, which is how CR-286 records it. Do not silently correct it to the read date and do not
  treat the post as unpublished because the date has not arrived.

**The likely cause is a scheduled publication whose timestamp is set in a locale or an editorial calendar
ahead of ours, and it does not matter, because the post is live and readable now.** What matters is that a
date on this source is not evidence about when anything happened, which is the fourth independent reason to
stop using these dates as anything but an approximate sort key.

**UK shelf: 0 added, 0 removed, identical in content and order to the 2026-10-16 read.** Ceiling holds at
10 September 2026 and `creator-marketing-whitepaper` is absent from slot 1 for a second consecutive day.
The head-of-list alternation diagnosed on 2026-10-10 now has two flat days in it (10-16 and 10-17) on top of
the falsifier recorded on 2026-10-16, so **it is not a daily metronome and should not be reported as a
pattern at all.** Observed presence: absent 10-07, present 10-08, absent 10-09, present 10-10, present
10-12, absent 10-15, absent 10-16, absent 10-17.

**Transport, 2026-10-17.** WebFetch on both `?locale=en_US` and `?locale=en_GB`, hrefs requested rather than
titles, first attempt each. **Eleventh consecutive browser-free read of both shelves.** `playwright`,
`playwright-arcads` and `hostinger-hosting` all failed CONNECT_TIMEOUT at session start and
`playwright-higgsfield` and `playwright-metatech` connected, so a browser was available today and was not
needed. The bare URL was not read, per the standing instruction.
"""
write(wl, read(wl).rstrip("\n") + note)
print("Watchlist: future-dated-post note appended")

# ------------------------------------------------------- 3. Harvest Log entry
hl = SCI / "Harvest Log.md"
hl_text = read(hl)
entry = """## 2026-10-17 (research run)

**1 transcript in, 1 platform post in, 4 claims banked, 5 merges. Both of the day's real findings are the same shape: an operator and a platform each publishing a number that cannot support the sentence around it.**

- **Harvest: 1 new transcript, read in full.** Nick Theriot, *$30k/day Facebook Ads Campaign Structure*, 2026-10-16, 3,615 words. 6 skipped short, 1 no subtitles, 0 errors across all 12 channels. The other 11 channels returned nothing.
- **New claims: [[Scaling Models#SC-178|SC-178]], [[Scaling Models#SC-179|SC-179]], [[Scaling Models#SC-180|SC-180]], [[Creative Science#CR-286|CR-286]].** All four T3. **Merges into SC-001, SC-009, SC-095, CR-035 and CR-154.** No law-level change, so the skill's hot layer takes one operating line and nothing more.
- **The finding worth acting on: the budget-decision lookback window is picked by the account's variance, and that picks the LONGER window on every client we have (SC-178).** Theriot reads yesterday by default and switches to a trailing 7 days when the account swings day to day: "instead of looking at yesterday every day, I'll look at last 7 days every every day." In the shown account the two windows disagreed and he followed yesterday, "last 7 days is saying don't scale". **This is the first selector anybody on the roster has given instead of a number**, and it agrees with SC-102 from the other side, where delivery volatility falls as conversion volume rises. ChiroWorks, StayWell, Phoenix Truxx and SJR Commercial all sit far below the volume where one day carries a readable signal, so **a yesterday-based scaling decision on any of them is a reaction to noise.**
- **The same operator has now published THREE different windows and the inconsistency is the honest headline.** Yesterday and trailing-7 today, against a 30-day average on 2026-08-31 stated as his standing rule and stated explicitly against reading day to day. **The 20% step held across all three dates**, so read his protocol as a stable step with an unstable window and never quote the window without its date. The cheapest upgrade on the board: log what each window would have decided on one account for 30 days and count the disagreements. Pure paper, no spend at risk, turns a T3 into a T2 with our numbers.
- **A hard platform ceiling nobody had banked: 200 ad sets per campaign (SC-179).** "This campaign is 191 ad sets. At 200 ad sets, you can't make any more ad sets." **This is the first stated limit on a structure this codex recommends in several places**, the add-an-ad-set-per-idea-inside-one-campaign pattern that SC-012 prescribes against the doom cycle. At his own five-ad-sets-a-week launch rate, 200 slots is about 40 weeks, so a campaign run this way hits the wall inside a year and the pruning is not optional. His campaign has taken $4.5M lifetime over two years and holds about 600 creatives. **Open item worth one search: this is either in Meta's published limits or it is not, and confirming it promotes the claim from T3 to T1.** Not binding on our book, where the longest-lived client campaigns hold single-digit to low-double-digit ad sets.
- **The CBO kill test moves up a level (SC-180).** The test for switching off an ad set is whether its spend damages the CAMPAIGN-level cost per result, and both halves are required: heavy spend AND campaign-level damage. A bad cost per result on small spend is left alone. **With SC-011 that completes a ladder: in ABO read the ad set, in CBO read the campaign, and in both the ad level is diagnostic only**, which matches the documentation-side statement that a CBO optimises the whole budget distribution against a campaign-level target. His evidence is the timing only, that the campaign improved when the expensive ad set started spending, and it is observational. Nobody has run the test that settles it.
- **The frequency number that must not travel.** He left an ad set running at **5x frequency**, $20,000 of spend over 30 days, $19 cost per purchase against a $22 target, bottom-funnel statics for a sales event. **That is the same operator breaching his own 1.46-to-1.5 early warning by a factor of three, and it refutes nothing**, because his thresholds are AD-level over 7 DAYS and this is AD-SET level over 30 DAYS. Merged into SC-095 as a documented exception rather than a contradiction: a converting bottom-funnel ad set is allowed to run hot, and the test he applied was cost per purchase, never frequency.
- **One assertion in the codex became a reported action.** His "if I go to 20, it's not going to break anything" had never been observed above three. He launched **twelve statics in one ad set** for a Labor Day sale, and that ad set is the heaviest-spending one of the month. Still not a concurrency test, with a sale offer confounding it, and merged into CR-154.
- **Watchlist: one new platform post, everything else clean.** Meta for Business News US shelf 1 in 1 out, a single head-of-list event in the 12-slot window. **The new post is dated 19 October 2026, two days in the future, on both the card and its own post header**, which is a fourth distinct date artefact on this source and the first that is not a disagreement between two renderings. Logged in [[Watchlist]]: never treat a future-dated card as a render fault, read the post. UK shelf 0 added 0 removed. Meta Engineering 0 new of 9, Meta Newsroom 0 of 10, Google Ads & Commerce 0 of 20, Google Ads Announcements 396 answer ids with 0 added and 0 removed, TikTok SDK unchanged at v0.1.8.
- **Meta published a partner case study and it fails both provenance tests this codex already applies (CR-286).** Nest Commerce, a UK agency, marketing its own AI-creative tool on Meta's channel: brands scaling it to "an average of 40% of spend" saw "revenue grow 70%, with 20% higher CVR", plus 56% higher ROAS at one brand and 5% lower cost per result at another. **No footnote anywhere on the page, no data window, no definition of the benchmark, and not one of the seven brands is named.** The counterfactual is worse than absent: seven brands that chose to onboard a new creative platform in one quarter are selected on budget, appetite and creative headroom before any variant is generated, and the share of spend is itself an outcome of the account doing well enough to keep feeding it. **Never quote 70%, 20%, 56%, 17% or 5% to a client or put any of them in a forecast.** The direction corroborates diversification claims that already stand on better evidence, and the one sentence carrying a mechanism is the agency CEO restating what the codex holds at law level.
- **The one cheap idea inside it is the share-of-spend framing.** Reporting newly-generated creative as a PERCENTAGE OF SPEND rather than as a count of ads prices it by what delivery actually bought. **We track that number on zero client accounts and it is one breakdown away.**
- **arXiv: feed empty, weekend build.** `lastBuildDate` Sat 17 Oct 2026 04:00:02 UTC, zero items, `skipDays` naming Saturday and Sunday. The run fired at 15:29 IST, which is 09:59 UTC and therefore after the rebuild, so this is **Saturday's own build and the 2026-09-05 Saturday case applies, not the lag case**. Not an error and not a filter result.
- **TikTok: geo-block, not an outage.** Per the 2026-10-15 rule, the Newsroom and for-Business blog are a permanent India geo-block and are not retried or logged as a fault. The SDK changelog answered HTTP 200 and is unchanged at v0.1.8, which detects endpoints and misses policy and creative news. **TikTok product news remains genuinely unmonitored and is stated as such rather than implied covered.**
- **Weekly lane: nothing due.** Saturday. The 2026-10-12 Monday run completed and wrote its log, so no catch-up is owed under the 2026-09-22 rule. Next weekly read is Monday 2026-10-19.
- **Gaps noticed.** The 200-ad-set ceiling needs one documentation check to promote. The yesterday-against-trailing-7 paper test is unrun and is the cheapest T2 upgrade currently available. AI-creative share of spend is untracked on every client account. And the evidentiary hole in CR-035 is now four videos old: nobody has shown a per-variant comparison for a three-ad visual-hook batch at any date, on an account at $328,000 of monthly spend or any other.

"""
hl_text = hl_text.replace(
    "One line per Research run: what came in, what changed. Quiet days get one line and nothing else.\n",
    "One line per Research run: what came in, what changed. Quiet days get one line and nothing else.\n\n"
    + entry.rstrip("\n") + "\n",
    1,
)
write(hl, hl_text)
print("Harvest Log: 2026-10-17 research entry prepended")

# ------------------------------------------------------- 4. run log
runlog = SKILL / "runs/2026-10-17-research-log.md"
write(runlog, """---
title: "Research run 2026-10-17"
date: 2026-10-17
type: run-log
---

# Advertising Science research run, 2026-10-17

Started 15:27 IST. Saturday, so the weekly (Monday) sources were not due; the 2026-10-12 Monday run
completed and wrote its log, so no catch-up was owed.

## 1. Harvest

`lib/harvest.py daily` across all 12 roster channels. **1 new transcript, 0 errors.**

- Nick Theriot, *$30k/day Facebook Ads Campaign Structure*, published 2026-10-16, 18 minutes,
  3,615 words. Read in full and extracted.
- 6 skipped short, 1 no subtitles, 0 out of window, 0 listing failures, 0 RSS fallbacks.
- The other 11 channels returned nothing.

## 2. Watchlist

| Source | Result |
|---|---|
| Meta Engineering (RSS) | HTTP 200, 9 in feed, **0 new** |
| Meta Newsroom (RSS) | HTTP 200, 10 in feed, **0 new** |
| Google Ads & Commerce (RSS) | HTTP 200, 20 in feed, **0 new** |
| Google Ads Announcements | HTTP 200, **396 answer ids, 0 added, 0 removed** |
| arXiv cs.IR | HTTP 200, **0 items, feed empty, weekend build** |
| TikTok SDK changelog | HTTP 200, **unchanged at v0.1.8** |
| Meta for Business News, `?locale=en_US` | **1 added, 1 removed** (one head-of-list event) |
| Meta for Business News, `?locale=en_GB` | **0 added, 0 removed**, identical in order to 2026-10-16 |
| TikTok Newsroom and for-Business blog | **Geo-block, not retried and not an outage** |

**arXiv is Saturday's own build, not the lag case.** `lastBuildDate` Sat 17 Oct 2026 04:00:02 UTC,
zero `<item>` elements, `skipDays` naming Saturday and Sunday. The run fired at 09:59 UTC, after the
04:00 rebuild. Per the 2026-09-05 rule this is "feed empty, weekend build" and is not an error.

**Meta for Business News, US shelf.** `meta-nest-ai-creative-diversification` in at slot 1,
`game-changers-series-1` out of slot 12, the other eleven shifting down one. One event in a 12-slot
window, not two rotations. The post was read in full and banked.

**New Watchlist finding: a post on this source can be dated in the FUTURE.** The new card and its own
post header both read 19 October 2026, two days after the read. The three date artefacts already on
file are all disagreements between two renderings of a past date; this one is an agreement that is
ahead of the clock. Logged in `wiki/science/Watchlist.md`: never treat a future-dated card as a render
fault, read the post, and cite the published date with the read date beside it.

**UK shelf.** `creator-marketing-whitepaper` absent from slot 1 for a second consecutive day. The
head-of-list alternation diagnosed on 2026-10-10 now has three flat days against it and should not be
reported as a pattern.

**Transport.** WebFetch on both locales, hrefs requested rather than titles, first attempt each.
Eleventh consecutive browser-free read of both shelves. The bare URL was not read.

## 3. Claims

**4 new, all T3. 5 merges. No duplicate IDs.**

| ID | Topic | Claim |
|---|---|---|
| SC-178 | Scaling Models | The budget-decision lookback window is set by the account's day-to-day variance, and the same operator has now published three different windows |
| SC-179 | Scaling Models | A campaign holds at most 200 ad sets, so the one-ad-set-per-idea structure has a hard end and has to be pruned |
| SC-180 | Scaling Models | Inside a CBO the kill test for an ad set is damage to the CAMPAIGN-level cost per result, not its own |
| CR-286 | Creative Science | Meta's Nest partner case study fails both provenance tests: no named advertiser and no counterfactual |

Merged: **SC-001** (third lookback window, plus the anti-collapse reason that cutting a budget spends
the account's recovery runway), **SC-009** (a third reason to delete low-spend ad sets, and it is
housekeeping against the 200 ceiling rather than a performance kill), **SC-095** (an ad set left
running at 5x frequency, which is a different window and a different unit from his own thresholds and
refutes nothing), **CR-035** (restated at a fourth date on the largest account yet), **CR-154** (twelve
statics actually launched in one ad set, which converts his assertion into a reported action).

## 4. Skill update

**No law-level change.** Everything banked today is T3, nothing was refuted, and no core claim became
contested. The hot layer took one operating line, because SC-178 changes what we should do on every
client account today and that is what the hot layer is for.

## 5. Errors and environment

- `playwright`, `playwright-arcads`, `hostinger-hosting` and `plugin:pdf-viewer:pdf` all failed
  CONNECT_TIMEOUT at session start. `playwright-higgsfield` and `playwright-metatech` connected.
  **No browser was needed at any point.**
- `rizzdial` failed ENDPOINT_NOT_FOUND. Not used by this run.
- No harvester errors, no watchlist fetch errors.

## 6. Open items this run surfaced

1. **The 200-ad-set ceiling needs one documentation check.** Confirming it against Meta's published
   limits promotes SC-179 from T3 to T1.
2. **The yesterday-against-trailing-7 paper test is unrun and is the cheapest T2 upgrade available.**
   Log what each window would have decided on one account for 30 days and count the disagreements.
   No spend at risk.
3. **AI or newly-generated creative as a share of spend is tracked on zero client accounts.** One
   breakdown away, and a better instrument than an ad count.
4. **CR-035's evidentiary hole is four videos old.** Nobody has shown a per-variant comparison for a
   three-ad visual-hook batch at any date.
""")
print("run log written")
