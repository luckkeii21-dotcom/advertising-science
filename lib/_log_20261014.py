# -*- coding: utf-8 -*-
"""Harvest Log entry + run log for the 2026-10-14 research run."""
import io
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
VAULT = Path(r"E:\claude code marketing skill\Obsidian God-level Marketing Vault\God-level Marketing\wiki\science")
LOG = VAULT / "Harvest Log.md"
RUNS = Path(r"E:\claude code marketing skill\.claude\skills\advertising-science\runs")

ENTRY = """## 2026-10-14 (research run)

**1 transcript in, 6 claims added, 10 merges, 0 contested, 0 refuted, 0 errors. Two laws amended.** Meta published the 2026 generation of GEM and it is the largest single T1 source this engine has read in weeks. Read in full from the saved page, not summarised.

**Five claims from "Meta's Generative Ads Model (GEM): Scaling the Central Model and Compute Engine for Frontier Ads AI" (Engineering at Meta, 2026-10-13).** Page cached at `cache/fb-eng-gem-20261014.html`.

- **[[Meta Delivery & Andromeda#MD-176|MD-176]], T1.** The 2026 generation replaces the per-surface and per-objective prediction systems with one central model that jointly predicts CTR across every surface and CVR across every major optimisation goal. Meta's own sentence on why that matters to a thin account: "The generalizable representations learned on data-rich click tasks transfer into data-sparse conversion tasks." Made tractable by cost-free virtual data mixing and a shared-expert-plus-domain-expert framework. The claim records the limit: it changes nothing about the account's own 50-events-in-7-days exit condition and lets no account borrow conversion volume it does not have.
- **[[Meta Delivery & Andromeda#MD-177|MD-177]], T1 for the statement only.** The published numbers: 18.9% conversion improvement and 12% CTR improvement across surfaces and objectives, plus a separate 5.8% / 4.1% / 1.6% conversion uplift on Facebook, Instagram and off-site "for targeted users over the past year". **No footnote anywhere in the post**, no window on the first pair, no definition of "targeted users", and no statement of how the two sets relate, so they cannot be reconciled or added. Not quotable to a client and not usable in a forecast.
- **[[Meta Delivery & Andromeda#MD-178|MD-178]], T1.** Kunlun replaces InterFormer: 2x performance at the same compute scaling, 2.5x model complexity, LLM-like scaling law observed at largest pre-training scale. The paid-for cuts, with Meta's numbers: block-sparse attention (quadratic to linear in window size), Generalized Dot-Product Attention (up to 2x forward speedup), expert parallelism, CompSkip (43% fewer FLOPS, "negligible quality loss"), OneSeq.
- **[[Meta Delivery & Andromeda#MD-179|MD-179]], T1.** LoopFM and Solaris. The line worth the whole post: "When an exact user-ad embedding is unavailable, the system degrades rather than drops. It substitutes an aggregate of the user's own recent embeddings across the same ad groups, or borrows from behaviorally similar users." **This is the first cold-start description Meta has ever published.** A new ad is scored on borrowed intelligence, not from zero.
- **[[Meta Delivery & Andromeda#MD-180|MD-180]], T1.** Sequence length is its own scaling law. "Prediction quality follows a power law with sequence length", 2x long context shipped in production and 25x demonstrated, and "larger models benefit disproportionately from longer sequences."

**One claim from Google.** [[Google Auction & Smart Bidding#GA-093|GA-093]], T1 for product copy. The October 2026 Demand Gen drop re-announces the same three measurement items as the 2026-09-10 drop, 33 days later, still in forward tense: the Data Strength Uplift metric "is launching", Data Manager "is expanding" to DV360 and Analytics, enhanced conversions "will soon be available" there. Its 20% conversion-uplift figure rests on footnote 1 in full: "Google Data, Global, Performance, June 3, 2026 - June 17, 2026." **Fourteen days**, the shortest window behind any figure in the thirteen-month series, no advertiser count and no control group. The Zebra case study (16% conversion volume, 19% conversion value) carries no footnote at all.

**Ten merges.** MD-004 (timeline now carries the 2026 GEM generation), MD-029 (the bare 2x finally has a named mechanism, LoopFM), MD-030 (InterFormer dated as the previous architecture), MD-031 (old figures explicitly not comparable to the new ones), MD-032 (second post restates 4x FLOPs and 20-25% MFU verbatim, so it is one achievement and not two), MD-141 and CR-113 (push delivery, see below), GA-073 (the three measurement items still unshipped a month on), GA-088 (census extended to fifteen instalments and nineteen figures; four now footnote-silent, counterfactual count unchanged at three), LS-023 (Heath's conversion-volume index restated with an explicit refusal of proxy metrics).

**Two laws amended.** **Law 1** gains the second T1 sentence it has ever had placing the creative's representation in Meta's feature set, this time inside the current architecture's standing definition and beside demographics (MD-178), and gains a ceiling it did not carry: four independent T1 statements now say a large share of match quality is a function of what Meta knows about the PERSON, an input no account touches (MD-180, with MD-090, MD-174, MD-175). The instruction does not change. The claim that creative is the only input the machine reads does. **Law 3** gains Meta's own cold-start description (MD-179) and one hard constraint on the control it recommends.

**The operating find of the day, read off the live product.** Ben Heath, 2026-10-13, demonstrating in a client account: push delivery's defaults are **20% of daily budget over 7 days**; the control was present in **about half** of his agency's accounts, the first fraction anyone has put on the rollout; and **push delivery and Meta's creative testing tool are mutually exclusive, enforced by the product at CAMPAIGN scope.** With push delivery on, the creative-test flow greys out and reads "you're pushing delivery to one or more ads in this campaign. You can only set up a creative test after these push delivery periods have ended." So one ad under push delivery locks creative testing out of every ad set in that campaign. His selection rule is indexed to conversion volume: push delivery moves one ad and reads out faster in a thin account, the creative testing tool fills 2 to 7 ads and needs several times the conversions. Both of MD-141's open guards are now closed.

**Harvest: 1 new transcript from 12 channels, zero errors.** Ben Heath, "NEW Way To Test Facebook Ads!", 18 minutes, 4,172 words, read in full and marked extracted. 6 uploads skipped as too short, 2 had no subtitles, 0 out of window. No extraction backlog, so the 25/day rule did not apply. Summary at `runs/2026-10-14-1402-harvest.json`.

**Watchlist: 5 new items, 2 banked, 3 discarded, zero errors.** Discarded with reasons: Meta Newsroom's "Your Algorithm, Your Words" (natural-language control over Facebook Feed and Reels **organic** recommendations; ads are never mentioned anywhere in it), the Edits Film Festival selection, and the West African scam-network enforcement announcement. arXiv cs.IR carried 83 new items and 1 passed the ad filter, "LLM-based User-Product Relevance Evaluation for Dynamic Product Advertising" (2610.14550): **read and not banked**, because it proposes an offline evaluation metric rather than describing a delivery mechanism, names no platform, and reports no correlation number behind its "strongly correlates with offline and online business metrics". TikTok SDK changelog unchanged at 0.1.8. Google Ads Announcements: 396 answer IDs, identical to cache, zero added and zero removed. Wednesday, so the 9 Monday-only weekly sources were not due.

**Gaps noticed.**

1. **Yesterday's gap got bigger and is still open.** MD-180 is the fourth T1 statement that ranking quality tracks what the platform knows about the person. We have still never pulled a 30-day hour-of-day or day-of-week cost-per-result breakdown on Phoenix Truxx or SJR Commercial. It costs one export.
2. **New, and it is the sharper version of the same gap.** If Meta's published gains concentrate where engagement history is deep, our book inherits the least of them, because clinics and truck dealers sell to light platform users. Nothing on file measures whether our results differ by buyer platform-activity, and no instrument for it has been named yet.
3. **Codex hygiene: MD-103 and MD-141 are near-duplicate claims about the same control**, banked three months apart from two different operators. Today's merge went into MD-141 and cross-references MD-103 rather than collapsing them, because collapsing changes an ID other claims link to. Worth a deliberate pass, not a drive-by.

**Errors: none.** Harvester clean, watchlist checker clean on all six lanes. TikTok Newsroom and the TikTok blog were **skipped: browser unavailable** (every Playwright MCP server in the session failed to connect, 30s timeout), same as 2026-10-13. Both are India geo-blocked to a plain fetch, so they are skipped rather than reported clean.

"""

log = LOG.read_text(encoding="utf-8")
anchor = "## 2026-10-14 (teacher run; the research lane had written no entry at topic-lock)"
if log.count(anchor) != 1:
    raise SystemExit("teacher anchor matched %d times, aborting" % log.count(anchor))
log = log.replace(anchor, ENTRY + anchor)
LOG.write_text(log, encoding="utf-8")
print("Harvest Log: 2026-10-14 research entry inserted above the teacher entry")

RUN = RUNS / "2026-10-14-research-log.md"
RUN.write_text("# Research run 2026-10-14 (Wednesday)\n\n" + ENTRY.split("\n", 1)[1].lstrip("\n"), encoding="utf-8")
print("Run log written:", RUN)
