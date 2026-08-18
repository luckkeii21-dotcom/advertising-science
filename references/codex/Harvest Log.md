---
title: "Harvest Log"
type: log
created: 2026-08-18
tags: [advertising-science, log]
---

# Harvest Log

One line per Research run: what came in, what changed. Quiet days get one line and nothing else.

## 2026-08-19 (research run)

- Ran 00:39 IST, about 4.3 hours after yesterday's 20:21 run, which is why every feed came back empty. Not a quiet internet, a short interval.
- Daily harvest: **0 new transcripts** across all 12 channels. Zero harvester errors. One video skipped as too short.
- Watchlist: **nothing new.** Wednesday, so the 9 Monday-only sources were not due. All 4 RSS feeds identical to yesterday's baseline (Meta engineering 9 items, Meta newsroom 10, Google Ads & Commerce 20, arXiv cs.IR 63). Google Ads Announcements diffed clean against cached HTML, the only delta was a session token. Meta for Business News checked through the Playwright browser because a plain fetch now returns HTTP 400, newest item still 11 June 2026. **TikTok Newsroom FAILED again: HTTP 503 to the browser on two attempts, so it was not checked for the second day running.**
- **Backlog batch: 25 transcripts read in full** by 9 parallel readers, per the 25/day rule. 226,535 words. **450 candidate claims**, every one carrying a verbatim quote. 10 merge agents then wrote them in, one agent per topic file so there were no write conflicts.
- **Codex 610 to 747 claims** (49 T1, 59 T2, 542 T3, 97 T4). Contested 27 to 54. Superseded 1 to 5. 283 claims touched. No duplicate IDs. Dedup was heavy and correct: CR alone folded 131 of its 135 candidates into 60 existing claims and minted only 4 new IDs.
- Per topic: CR 152 to 156, MM 118 to 145, MD 66 to 88, SC 77 to 98, AT 57 to 68, GA 34 to 52, AU 32 to 48, LS 34 to 42, GP 23 to 33, TT 17 unchanged.
- ⚠ **Law 3 is now contested and the skill says so.** Charley T says kill the budget-hogging ad. Faris, across 100+ accounts, says leave high spenders on in 99%+ of cases and reports roughly 30% more spend at the same target just from switching a previous buyer's paused high spenders back on. Neither shows data (SC-085; SC-008 flipped to contested). What survives both sides: killing LOW spenders is always safe. Resolving test written into the claim, kill the top spender 2-3 days and read ACCOUNT-level cost per result.
- ⚠ **AT-008 downgraded T2 to T3.** Both sources are the same speaker citing Haus and CTC meta-analyses from memory with the studies never shown. That is T3 by our own rule. Yesterday's tiering was too generous and this run corrected it.
- ⚠ **The incrementality benchmarks expired.** The 28-day-click and 7-day-click x 110-115% approximations were derived on the OLD wider 7-day-click column, so they no longer hold after the March 2026 outbound-click-only redefinition (AT-008 cross-referenced to AT-036). Never quote them against post-March-2026 data.
- New law 8a, **a cost cap has no AOV term**: at a $50 cap a $50 AOV product returns 1.0 ROAS and a $100 AOV product 2.0, and Meta drains budget onto the cheapest SKU (AU-040 T3). Shown live: a sitewide markdown pulled capped spend onto a $46 AOV product and the fix was off-platform (AU-045 T2). Client promo calendars and price changes are delivery changes now.
- New law 8b, **learning lives in the ad account and not the pixel** (SC-094), so client ad accounts must sit in the CLIENT's Business Manager with partner access to us.
- New law 16a, **a share of Google spend is unmeasurable**: broad match, feeds, PMax and AI Max already serve inside AI Overviews and AI Mode with no off switch and no reporting breakout (GA-043).
- New law 11a for client reports: period-end windows read the most incomplete days as final, so every WoW and MoM comparison structurally flatters the earlier window (AT-068).
- Skill hot layer: 22 laws to 29 (7 added: 4a, 4b, 8a, 8b, 9a, 11a, 16a). Four new watch items, including one that Meta's own docs can settle (MD-019, do new/engaged/existing definitions reach the delivery model or are they a reporting lens).
- **Source-reliability signal worth carrying.** Three independent merge agents caught the same speaker contradicting himself: the live ad count moved 4-6 to 3-4 to 3-5 to 5-8 across four months (CR-154), the Made by Mary gift-card case was told two incompatible ways ten weeks apart (MM-128), and one outcome (310 Nutrition, Under Outfit) is used to prove three different mechanisms (MM-125/131/079). Charley T is the densest source on the roster and the least self-consistent. Weight accordingly.
- Backlog remaining: **314 of 418** transcripts unextracted. At 25/day that is about 13 more days.
- Gaps noticed. The **no-shown-Google-test-data gap is still open**: all three Blue Sense Google episodes shipped zero numbers, so all 20 new Google claims are T3 assertion. TikTok is starving, 2 candidates in 450 and the roster has no TikTok operator. An **Axon channel claim had no topic file to live in** and was correctly refused by the TT agent rather than misfiled, so the codex has no home for emerging-channel claims. The arXiv keyword filter is still too loose and was not touched today.

## 2026-08-18 (research run, second pass same day)

- Daily harvest: 3 new transcripts, all read in full (Ben Heath 6,658w, Dr. Matt Shiver 6,017w, Sam Piliero 563w). Zero harvester errors.
- Watchlist: nothing new. Tuesday, so the 9 Monday-only sources were not due. Two sources FAILED rather than came back empty: TikTok Newsroom returned HTTP 503 to the Playwright browser twice, and Meta for Business News geo-redirected to `lang="hi"` and served a listing whose newest item is 11 June. Google Ads Announcements verified clean directly against cached HTML (zero August 2026 dates). arXiv: 63 items, 5 genuinely ads-adjacent abstracts read, nothing bankable.
- Cache directory did not exist, so step 2 had no diff baseline on its first real run. Created and seeded (102 item links across 4 feeds, plus HTML snapshots of both daily scrape pages).
- **Backlog batch: 25 transcripts read in full** by 10 parallel readers, per the 25/day backlog rule. 486 candidate claims extracted, every one carrying a verbatim quote. 10 merge agents then wrote them in, one agent per topic file so there were no write conflicts.
- **Codex 363 to 610 claims** (49 T1, 54 T2, 456 T3, 51 T4). Contested entries 11 to 27. No duplicate IDs, every claim carries tier, sources and touch date.
- Two known gaps CLOSED: Google PMax & Shopping went 4 to 23 claims and now has its first practitioner layer; TikTok Delivery went 5 to 17 and now has mechanism-level TikTok Shop material. Both were flagged as T1-docs-only at engine build.
- ⚠ **Meta redefined 7-day click around March-April 2026** to require an outbound click, moving engagement clicks into a new 1-day engaged view bucket. 7-day-click ROAS fell overnight with no real performance change. Client-reporting consequence: a step-down dated to that window is a definitional artefact, never write it up as a decline. Banked AT-036, promoted to skill law 10.
- ⚠ **Incremental attribution is not a holdout on your own account.** It applies a factor derived from competitors' lift studies in your niche. Never quote it to a client as a measured lift. Banked AT-035, promoted to skill law 11.
- Skill hot layer rebuilt: 15 laws to 22. New laws cover the 7-day-click redefinition, IA provenance, prune-before-you-launch (two T2 cases), PMax over-attribution, the tROAS trap, TikTok incrementality, and discount math.
- Backlog remaining: 339 of 418 transcripts unextracted. At 25/day that is about 14 more days.
- Gaps noticed: no channel on the roster still covers Google Ads with SHOWN test data, so all 16 new GA claims are T3/T4 assertion. The arXiv keyword filter is too loose (`ad` matches "adaptive"); 45 of 63 items matched today and only 5 were relevant.
- Lesson 002 shipped: The Attribution Column Is an Instrument, and the Instrument Changed. No video (Tuesday). Taught from the harvest instead of the rotation, because AT-035 and AT-036 both change how we write client reports. Lesson 001 still ungraded, inbox was empty.
- Account gap surfaced while writing the lesson: **Compare attribution settings has never been opened on any of the five accounts.** No 7-day-click versus view split exists in the vault for ChiroWorks, Chiropraise, Phoenix Truxx, SJR Commercial or Mattia. We cannot state our own view-through share on a single account. Cheapest open item on the board.

## 2026-08-18 (engine built + first mass harvest)

- Engine went live: harvester built and tested, both daily Windows tasks registered (research 07:00, teacher 08:00 IST).
- Harvested 52 transcripts from the 12-channel roster (30-day window) plus 22 official platform sources (Meta engineering Andromeda/GEM/multi-stage ranking, Google Ads docs, Meta Business Help, TikTok docs).
- First extraction: 14 agents extracted 423 raw claims; 10 merge agents wrote **363 deduplicated claims into the codex** (49 T1, 42 T2, 261 T3, 11 T4, 11 contested disputes recorded with both sides).
- Skill hot layer rebuilt: 15 laws + 2 watch items.
- ⚠ Watch: Aug 2026 in-place budget-raise bug (Ben Heath, 1,400 accounts); instant forms embedded calendar booking rolling out (conflicts with our voice-agent-owns-booking law).
- Deep backfill (top-30 per channel for 12 months + full BlueSense catalog) running; unextracted backlog will be worked at 25/day by the daily research runs.
- Gaps noticed: Google PMax topic has T1 docs only, zero practitioner claims so far (Solutions 8 deep catalog + Mike Rhodes backfill should fill it); TikTok topic is T1-only; no channel currently covers Google Ads with shown test data.
- Lesson 001 shipped: Creative Is the Targeting (no video today; first video day is Wed 20 Aug).
