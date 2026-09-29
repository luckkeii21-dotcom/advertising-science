"""2026-09-29 research run: write the Harvest Log entry and re-file the
2026-09-28 research block, which was appended to the bottom of a
newest-first file."""
from pathlib import Path

SCI = Path(r"E:\claude code marketing skill\Obsidian God-level Marketing Vault"
           r"\God-level Marketing\wiki\science")
p = SCI / "Harvest Log.md"
lines = p.read_text(encoding="utf-8").split("\n")

start = next(i for i, l in enumerate(lines) if l.startswith("## 2026-09-28 (Monday)"))
misfiled = lines[start:]
while misfiled and misfiled[-1].strip() == "":
    misfiled.pop()
rest = lines[:start]
while rest and rest[-1].strip() == "":
    rest.pop()

anchor = next(i for i, l in enumerate(rest) if l.startswith("## 2026-09-28 (teacher run"))

today = """## 2026-09-29 (research run)

**0 transcripts, 0 claims added, 0 merged, 0 contested, 0 refuted. Codex unchanged at 1,322. 0 harvest errors, 0 watchlist errors.** Fourth consecutive zero-transcript day and the seventh on record. One maintenance edit and no new ID: LS-076 now carries a dated watch note.

**Meta Newsroom had the day's only new item. It was read in full and deliberately not banked.** "Launching Meta Enterprise Platform", 2026-09-28: Meta is starting an enterprise business line selling its own AI stack (Muse agent, Muse API, Muse Code, Meta Business Agent) to businesses and developers, and Chirantan "CJ" Desai joins from MongoDB as Chief Enterprise Platform Officer reporting to Zuckerberg. **No ad product, no placement, no mechanism and no performance figure**, so there is nothing to tier.

**It earned a watch note on LS-076 instead of an ID.** LS-076 banks Meta's launch-day sentence that Muse conversations and VM data do not reach the ad systems, and the claim's own text instructs a future re-check. Twenty days later Meta put a business line and a direct report to the CEO on top of that same stack. **The post says nothing about the ad-system boundary**, so nothing is contested, the tier is unchanged, and the note is filed as context. The commercial weight now sitting on Muse is the reason the re-check matters.

**arXiv passed 3 through the ad filter and all 3 are false positives.** All three abstracts were read before the call.

| Paper | Term that fired | Why it fails |
|---|---|---|
| EvoSkillRec, 2609.34552, new | `CTR prediction` | LLM-driven architecture search for recommenders. CTR prediction is one of three benchmark tasks. No auction, no bidding, no ad ranking |
| FARE, 2609.31890, cross | `CTR prediction` | Share-of-Voice-constrained re-ranking of financial product content. Fairness of organic exposure, no advertising |
| SAGA, 2608.15429v2, replace-cross | `conversion lift` | Multi-surface user action embeddings at a financial services firm. "Click and conversion lift" is a downstream recsys metric |

**Two things about the filter are worth recording, and neither is visible from the pass count.**

**One, the failure rate is running well above what this file predicts.** The 2026-09-07 note estimated "roughly one false positive a week". Today produced **three in a single build**, and the open fix is still an instruction rather than code. **SAGA is also the first recorded instance of `conversion lift` firing on a non-advertising paper**; the three failures already on file fired on `CTR prediction`, on `sponsored`, and on an advertising mention inside a framing sentence. That is a fourth bank term now known to be leaky.

**Two, the documented bank list and the shipped bank list disagree.** Watchlist.md still lists `click-through rate` as a bank term. It was removed from the regex in `lib/watchlist_check.py` on 2026-09-03, after it was the only hit on a job-matching recommender. **The doc overstates what the filter actually matches.** Left as found and flagged rather than edited, because which terms bank is Lucky's call.

### Watchlist

| Source | Result |
|---|---|
| Meta Engineering (RSS) | 200, build 24 Sep 00:02 UTC. 9 in feed, **0 new**. Build now 5 days flat |
| Meta Newsroom (RSS) | 200, build 28 Sep 12:37 UTC. 10 in feed, **1 new**, read in full, not banked |
| Google Ads & Commerce (RSS) | 200, build 24 Sep 16:00 UTC. 20 in feed, **0 new** |
| Google Ads Announcements | 200. **396 answer ids, 0 added, 0 removed.** Sixth consecutive unchanged day |
| arXiv cs.IR | 200, build **Tue 29 Sep 05:12 UTC**, run landed after 04:00 UTC so this is today's build. 85 items, 80 new, **3 passed the filter, 0 banked** |
| TikTok SDK changelog | 200, **unchanged at v0.1.8** |
| TikTok blog / Newsroom | India geo-block, permanent, not retried. **Policy and creative still unmonitored** |
| Meta for Business News | **Local browser unavailable.** Partial answer from a third locale, see below |
| Weekly (Mon) lane | **Not due.** Today is Tuesday |

### Meta for Business News: the browser lane was down and the fallback answered in the wrong locale

**All four local Playwright servers timed out at 30 seconds this session**, so the usual US and UK browser reads could not run. Plain fetch was tried anyway to confirm the documented behaviour and returned **HTTP 400 on both `www` and `en-gb`**, exactly as Watchlist.md records.

**WebFetch did render the page, in the India locale.** That is neither baseline, so **it was not committed as the daily slug diff** and the US and UK slug sets stay dated 2026-09-28. The observation still answers the operating question. The shelf carried **12 slugs, newest dated 10 September 2026**, the Instant Hydration Performance Spotlight, which is the **same top card as the UK baseline**. Eight of the twelve are in the cached UK set. **The four that are not are all back catalogue**, dated 15 September 2025, 17 June 2024, 28 February 2023 and 29 July 2022, which is the rotating-module behaviour this file has warned about since 2026-08-20. **Zero genuinely new items.**

Two method points fall out of it. **The US-to-UK ceiling gap now has a third locale**: India shows the UK top card and none of the US-only recent posts (Agency Awards, Meta One plans, IAB Creator Week). And **the same slug renders 10 September in India against 11 September in the UK**, which is the one-day date drift already recorded on 2026-09-27 and the reason the diff runs on slugs rather than on dates.

### One filing error in this file, found and fixed

**The 2026-09-28 research entry had been appended to the BOTTOM of a newest-first file**, landing below the 2026-08-18 entry where nothing would ever read it. Moved to its correct position above the 2026-09-28 teacher entry. The runbook says "append", the file is ordered newest-first, and the two disagree. **Worth one line so the next run writes to the top.**

### Gaps carried forward

- **TikTok policy and creative stay unmonitored** behind the India geo-block. The SDK changelog reports API surface and never policy.
- **The arXiv single-hit fix is still an instruction rather than code**, and today raised its cost from one false positive a week to three in one build.
- **No en-gb hash set for Meta Ad Standards**, open since 2026-09-14.
- **Marketing API v24.0 sunsets 6 October 2026**, 7 days out. Nothing of ours is pinned to it, still worth one check.
- **The 14 craft claims banked 2026-09-28 are untested on our own accounts.** CR-268, agitate the accommodation rather than the symptom, is still the cheapest T3-to-T2 upgrade on the board.
- **The Playwright browser lane needs to come back** before the next daily Meta for Business News diff is trustworthy."""

out = rest[:anchor] + today.split("\n") + [""] + misfiled + [""] + rest[anchor:]
p.write_text("\n".join(out), encoding="utf-8")
print("Harvest Log written.")
