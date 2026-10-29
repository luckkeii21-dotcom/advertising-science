# -*- coding: utf-8 -*-
# Research run 2026-10-29: append the Harvest Log entry at the bottom (research lane).
import io

P = (r"E:\claude code marketing skill\Obsidian God-level Marketing Vault\God-level Marketing"
     r"\wiki\science\Harvest Log.md")

ENTRY = u"""

---

## 2026-10-29 (research run)

**1 transcript in, 8 claims added, 9 merged, 1 contested. Count 1,396 to 1,404. The law layer moved on five new claims, four of them T1 Meta.** The heaviest Meta architecture day since Andromeda's own launch: three Meta pages dated 28 October, all read in full, plus one Google announcement and one Jon Loomer episode. Nothing was banked that was not read.

**Nothing urgent to act on.** No policy change, no deprecation, no new dated deadline. The nearest carried deadline is still Google landing-page image extraction on 4 December 2026 (GP-051).

**Harvest.** `lib/harvest.py daily`, 17:02:04 to 17:04:02. 1 new transcript, 12 of 12 channels listed, zero errors, **RSS fallback used on 0 of 12**. 7 skipped under the 150-second floor, 4 with no subtitles, 0 out of window. Per channel: jon-loomer 1, every other channel 0. Backlog verified empty after the merge: 501 markdown files in the transcripts folder, 0 carrying `extracted: false`.

**Watchlist, daily lane.** All sources HTTP 200, zero checker errors. Meta Engineering **1 new** (feed built Wed 28 Oct 17:35:01 UTC). Meta Newsroom 2 new, both set aside. Google Ads & Commerce **2 new** (feed built Wed 28 Oct 21:30 UTC). **arXiv cs.IR returned an EMPTY feed, 0 items in it**, build stamp Thu 29 Oct 04:00:02 UTC, which is a different condition from the usual "items present, none passed the filter" and is logged as such. TikTok SDK changelog unchanged at 0.1.8. Google Ads announcements 396 ids, 396 cached, 0 added, 0 removed. **Meta for Business News: two new, ending a seven-day flat streak.**

**⚠ The seven-day flat streak on Meta for Business News broke with the two most consequential advertiser-facing posts of the month**, both dated 28 October: *How Meta's Ads System Matches Your Ad to the Right Person at the Right Time* and *Inside the Three New AI Innovations in Ads Ranking*. Both read in full. Two slugs dropped off the bottom of the twelve-item shelf, both already in `slugs_seen_cumulative`.

**Added 8.**
- **[[Meta Delivery & Andromeda#MD-188|MD-188]], T1.** The 2026 Andromeda scores **every eligible ad** at over one billion ads per second per GPU server, 100x the 2024 system, which Meta now dates at tens of millions per second per card. Advertiser figure 2.4% more conversions on Facebook since 2025; Q3 2026 alone 1.37% Facebook and 0.24% Instagram Reels, stated as 1.4% on the sister page, a clean cross-check. No setting, no readout, never quotable to a client.
- **[[Meta Delivery & Andromeda#MD-189|MD-189]], T1.** Retrieval Mixture-of-Experts brings "near ranking-level" quality at ~300x fewer inference-time FLOPs. The cost asymmetry that justified a shallow-then-deep funnel is the thing Meta says it broke.
- **[[Meta Delivery & Andromeda#MD-190|MD-190]], T1.** Advertiser targeting rules are a named GPU stage, "index matching", over 100 billion ads per second, with real-time index updates "as ads are created, modified, or expired throughout the day". Confirms index freshness and says nothing about learning or performance resetting.
- **[[Meta Delivery & Andromeda#MD-191|MD-191]], T1.** Generative retrieval shipped on Facebook Feed in Q3 2026: the system "generates the semantic ID for the ideal ad for a person, then matches that to the ads available in our system". Nearly +2% conversions across targeted segments, +0.35% across surfaces paired with GEM and adaptive ranking.
- **[[Meta Delivery & Andromeda#MD-192|MD-192]], T1.** Q2 2026 alone: 8.3% more ad clicks and 15.7% more conversions on Facebook from user-understanding models plus GEM plus sequence learning, footnoted to Meta's Q2 and Q3 2026 earnings. Platform aggregate, never a client number.
- **[[Auction Mechanics & Bidding#AU-102|AU-102]], T1.** The ad quality term carries "more than 200 million customer survey responses a year covering satisfaction with purchases, shipping delays, unexpected charges, and whether people felt misled". Post-purchase experience is an auction input.
- **[[Google Auction & Smart Bidding#GA-099|GA-099]], T1.** Ads in AI Mode scaled to ten more countries on 28 October, Brazil/Mexico/UK named for Q4, **multiturn ads launched in the US**. Both Google numbers read with their footnotes: 3x longer queries is US, May 2026; sponsored-versus-organic click-through parity is US internal data over a 15-day window, 20 Aug to 3 Sep 2026.
- **[[Scaling Models#SC-182|SC-182]], T3 surface / T1 recommendation.** Meta's scheduled-budget-increase control ramps a daily budget for a set window and reverts on its own, and Meta's own peak-season guidance now tells advertisers to use budget scheduling. Closes a gap SC-117 named itself.

**Contested 1. [[Meta Delivery & Andromeda#MD-186|MD-186]], on its retrieval limb only, by Meta's own later page.** It ruled on 20 October that "generative recommenders" does not mean Meta retrieves or writes ads generatively. **The writing limb stands: no ad is generated by a model.** The retrieving limb is contested, because Meta shipped a product it calls generative retrieval in which a semantic ID genuinely is generated inside the retrieval path. The entry's reading rule was right and now reads narrower: what is generated is a target representation, and retrieval is still matching against it.

**Merged 9.** MD-024 (2024 generation superseded, its baseline throughput now stated by Meta, its +6%/+8% figures fenced to that generation), MD-026 (the hierarchical-index and model-elasticity machinery is now historical; Meta names the multi-kernel HBM bottleneck that replaced it), MD-089 (second first-party statement of the same cause, now sized at "hundreds of millions of new ads"), MD-022 (cascade and millisecond budget re-confirmed verbatim across two Meta pages, "within the same latency budget"), MD-177 (same GEM figures on a second page, scoped "since 2025", and the footnote complaint is answered for the sister page's numbers only), MD-120 (creative representation is now the matching key, not only an input feature), MD-093 ("A lead isn't a sale, and an install isn't a subscriber" is this law in Meta's own sentence, plus the three named attribution settings), SC-086 (Loomer's time-boxed complexity exception: trade structural purity for spend certainty only where the complexity has an end date), SC-117 (cross-linked from SC-182).

**Read and deliberately not banked.** Meta Newsroom *Meta Partners With Five US Universities*, 28 Oct, read at source, $2M research grants, zero advertising content. Meta Newsroom *Muse Singapore*, already read and set aside on the 28th. Google Ads & Commerce *Adapt your ad strategy to meet the way people search today*, 28 Oct, read in full: a two-paragraph pointer to an Ads Decoded podcast episode with Shivani Mohan on long-form query trends. **The post itself carries no number, no finding and no claim; the substance is inside audio this lane cannot read, so it is logged as a pointer and a gap rather than as a finding.**

**Law layer touched.** Five paragraphs added to the "Current laws" hot layer in `SKILL.md`, inserted after the 2026-10-28 block: the end of the cheap first gate, index matching and what its freshness does and does not prove, generative retrieval as the strongest form of creative-is-the-targeting, fulfilment entering the auction's quality term, and Google widening the AI surface again without widening the reporting. Backup at `SKILL.md.bak-20261029`.

**Gaps.** One new, six carried, none closed. NEW: the Ads Decoded podcast lane is unreadable to us, and Google is now publishing search-behaviour research in audio only. Carried: the arXiv new-ID re-submission defect in `lib/watchlist_check.py` and its stale `last_build`; the live ad set count on every client account still unverified against the LS-089 formula, now nine days old; `occ-2025`, `occ-2024`, `occ-2023` unread; "promotion mode" still undocumented by Google; TikTok product and policy news geo-blocked and genuinely unmonitored, re-confirmed live today at HTTP 503 and HTTP 451; and the Harvest Log's two write ends, flagged 21 October, ninth day, still unfixed.

**Errors.** Harvest none. Watchlist checker none. Plain curl on Meta for Business News returned HTTP 200 today rather than yesterday's 400, but served a 1,542-byte JavaScript stub with zero slugs, so the 200 is not a usable read and the shelf was read via WebFetch; recorded because a status-code-only check would now report this source as healthy and extract nothing. TikTok Newsroom HTTP 503 and the for-Business blog HTTP 451, both the known permanent geo-block, not errors. `rizzdial` MCP ENDPOINT_NOT_FOUND, not a research source. No source went unread.
"""

t = io.open(P, encoding='utf-8').read()
if "## 2026-10-29 (research run)" in t:
    raise SystemExit("already appended")
io.open(P, 'w', encoding='utf-8', newline='\n').write(t.rstrip() + ENTRY)
print("Harvest Log appended at the bottom")
