---
title: "Harvest Log"
type: log
created: 2026-08-18
tags: [advertising-science, log]
---

# Harvest Log

One line per Research run: what came in, what changed. Quiet days get one line and nothing else.

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
