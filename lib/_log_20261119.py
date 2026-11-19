# -*- coding: utf-8 -*-
"""Write the 2026-11-19 Harvest Log entry and the run log."""
import shutil
from pathlib import Path

SCI = Path(r"E:\claude code marketing skill\Obsidian God-level Marketing Vault"
           r"\God-level Marketing\wiki\science")
HL = SCI / "Harvest Log.md"
RUNS = Path(r"E:\claude code marketing skill\.claude\skills\advertising-science\runs")

ENTRY = """## 2026-11-19 (Thursday) - 1 transcript in - 4 claims added, 8 amended, 0 contested, 1 law amended

**Meta published a clock on its own ranking changes, and the clock is the finding.** Two Meta Engineering posts, both dated 18 November, both about ads ranking models, read in full. Meta's sentence: "Today it can take over a year for every proven technique to reach every applicable model", target three months. [[Meta Delivery & Andromeda#MD-198|MD-198]] established that there is no single ads model and said in its own limits that no refresh cadence was disclosed anywhere. It is disclosed now, so the fleet is heterogeneous in time as well as in architecture. 4 claims added, 1 law paragraph.

**Harvest: 1 new transcript, 0 errors.** 12 of 12 roster channels listed clean, 0 RSS fallbacks, which is the first fully clean listing in this run series after yesterday's `nick-theriot` 404. That channel listed fine today, so the 404 was transient and no handle check is owed. 5 uploads skipped as too short, 2 with no subtitles, 0 out of window. Unextracted backlog after this run: 0.

**Banked [[Meta Delivery & Andromeda#MD-202|MD-202]], T1: a proven ranking improvement takes over a year to reach every model it applies to.** Both posts are one series about one system, Standard Model Templates plus the agent layer that propagates techniques across it, so they are one claim. What is new against MD-198: the propagation latency, a published shelf life on Meta's own work ("an innovation that delivers gains today may be superseded within a couple of model development cycles"), the template system named and described, and a second two-year scoreboard. The scoreboard: per-model engineering time down 92%, 5,000+ technique-model combinations, 80 new techniques, 0.63% average offline gain at neutral serving capacity, 0.86% cumulative online lift over 70% of models by count. Against MD-198's 0.66% offline and summed 0.36% online from a separate publication, that is **two independent first-party sources landing in the same order of magnitude, so the under-one-percent rule holds and "Meta changed their model" still cannot explain an account moving by tens of percent in a week.** The ship gate is published too: offline normalized-entropy gain, no regression on training or inference cost guardrails, then a statistically significant online A/B win, with regression rate weighed alongside average gain. The agent figures (60% of propagation since March 2026, 3x productivity, median 4x compute reduction, $45M+ savings) are all hedged in Meta's own text and are banked as context, not as evidence.

**The operating use of MD-202 is narrow and it is worth stating plainly.** A tactic that genuinely works on one placement or one optimisation event and genuinely does not work on another, at the same time, in the same account, can be a propagation gap rather than audience quality or creative. Hold it as an explanation. Never offer it as a diagnosis, because Meta names no model, no surface and no technique, and nothing in it is readable from an ad account.

**Banked [[Auction Mechanics & Bidding#AU-103|AU-103]], T1: the first outside figure that connects a model-quality metric to advertiser money, with the cost attached.** arXiv 2611.24283v1, announced today, abstract read, full paper not opened. A deployed real-time-bidding system compresses user history into tokens computed offline and reused across candidates. Published both halves: 0.81% relative offline normalized-entropy reduction and +4.65% on a business metric reflecting advertiser conversion value plus +2.96% clicks, bought for **15% more online inference cost per request**. The company is not named. Treat the 0.81%-to-4.65% ratio as one data point from one unnamed system and never as a conversion factor for Meta's own NE figures. The cost side is the counterweight to [[Meta Delivery & Andromeda#MD-199|MD-199]]: a win that costs 15% more per request is exactly the work an allocation layer declines to run when predicted return is low.

**Banked [[Google Auction & Smart Bidding#GA-103|GA-103]], T1: Seasonality Adjustments are now available in Demand Gen.** Google's November Demand Gen drop, 18 November, read in full. One control in it generalises, and it is the first dated instrument for the problem a short promotion creates in any Smart Bidding campaign. It has to be entered before the promotion, since its stated purpose is bidding competitively from day one. Everything else in the post is catalogue and e-commerce machinery that our lead-generation book cannot use: product feeds on YouTube, checkout links, Universal Commerce Protocol checkout, two creator-boost products. **Its six case-study figures are not evidence.** Petco 6% purchase intent, 71% store visits, 30% Omni ROAS; Javvy 50% conversion rate; Shopee 9x ROI. No baseline, no window, no spend, no control group and no method for any of them.

**Banked [[Meta Delivery & Andromeda#MD-203|MD-203]], T4: a five-item test for whether a practitioner source has stopped keeping up.** Jon Loomer, 18 November, 9 minutes, 1,445 words, read in full. Zero numbers, zero account data, zero settings, so the tier is T4 and the claim is reasoning. Banked anyway because this engine reads twelve practitioner channels every day and nothing in the codex held a source-staleness test. The five tells: constant remarketing strategies; arguing broad can never match remarketing while not understanding the remarketing that happens naturally inside broad; building complicated structures to exert control; switching off setting after setting in the ad set while optimising for a conversion; stopping and starting on small samples. **Every one of the five is already a law here, reached independently**, which is the reason to record the convergence: MD-052, MD-075, SC-014, MD-015 and MD-014, LS-006 and LS-055. He also states the conflict of interest that produces the pattern, from his own case: "deep down I also knew that this evolution was an attack on my brand as a targeting guy." The limit is in the video, and it is recorded in the claim: the closing line "avoid making anyone your go-to source on anything" sits immediately before a pitch to subscribe to his own weekly tips for a year.

**Watchlist: 0 errors, 5 new items across 3 feeds, 3 of the 5 banked or recorded.** Meta Engineering 2 new, both read in full and both inside MD-202, feed build 18 November. Meta Newsroom 2 new, both opened and read in full. Google Ads & Commerce 1 new, read in full, banked at GA-103. Google Ads announcements flat at 396 answer IDs, 0 added, 0 removed. TikTok SDK changelog unchanged at v0.1.8. arXiv cs.IR: 21 items in the Thursday 05:00 UTC build, 2 passed the advertising filter, 1 banked.

**The second Newsroom item is a fifth re-check on [[Learning & Signal#LS-076|LS-076]] and it moves the boundary a step closer.** Muse added Loblaw on 18 November as its first Canadian retail partner. Still no advertising content, one occurrence of the word ads anywhere on the page and that is site furniture, and the launch-day sentence about ad systems is not repeated. **What is new is that a purchase now completes inside the agent:** catalogue in, basket built, checkout done in Muse, with brand preferences and food allergies remembered between sessions. A transaction that completes inside Muse touches no website, so it fires no pixel and has no landing page, which would be an unmeasurable conversion even if an ad surface existed. Still no ad inventory, no lead capture and no advertiser-facing surface. Amendment recorded, tier unchanged, re-check again on the next Muse post.

**The first Newsroom item was read and not banked.** "Our Approach to Updating Our Commercial Terms of Service", 18 November. Meta has put the proposed commercial-terms updates on hold after objections from news publishers about how the terms apply to its web crawlers, and has defined a three-phase consultation. It is a crawler and publisher-rights matter with no advertising content, so no claim.

**The second arXiv hit was read and not banked.** "UniRank: Benchmarking Ranking Models for Unified Sequential Modeling and Feature Interaction", a v3 replacement. It is a genuine advertising-adjacent paper rather than a filter false positive, benchmarking 15 unified ranking models on five public datasets with an open PyTorch toolkit. It carries no operational claim and no deployed result, so it is recorded here and not given an ID.

**Meta for Business News, the one Daily scrape source the script does not handle: not read today, and that is a coverage gap rather than a clean check.** The Playwright MCP server failed to connect in this session on every profile, and the two shelves were not fetched. Under the 2026-11-10 pass-2 rule the UK shelf needs two reads several hours apart to count as covered, so a session with no read at all is a blind day on this source. `slugs_seen_cumulative` is untouched.

**TikTok Newsroom, the for-Business blog and the Marketing API what's-new page were not retried.** Permanent India geo-block per the standing ruling, not an outage.

**Weekly (Monday) sources not due today.**

### Skill law layer

**Updated.** One paragraph added to the Current laws hot layer for the 2026-11-19 pass, carrying the over-a-year propagation latency and the three-month target, the shelf-life sentence, the second under-one-percent scoreboard, the published ship gate, and AU-103's paired win-and-cost figures with the guard that the ratio is not a conversion factor. It sits above the 2026-11-12 MD-199 paragraph.

### Gaps noticed

- **We still cannot name which Meta model serves which placement, and MD-202 raises the price of not knowing.** MD-198 made a placement-level gap an architecture fact. MD-202 makes it a dated architecture fact: two placements can be a year apart in which improvements they carry. Our own placement breakdowns remain the only instrument, and now there is a second reason to read them more often. Nothing in either post maps a model to a surface.
- **Normalized entropy now has one bridge to advertiser money and one is not enough.** AU-103 is the first figure anywhere in this codex translating an NE gain into advertiser conversion value, at roughly 6 to 1. It is one unnamed system, one experiment, read at abstract level. A second independent sighting would make it usable; until then every NE figure stays directional and the ratio stays unquotable.
- **No browser in this session, and today it cost the whole Meta for Business News lane.** Yesterday the plain fetch returned HTTP 400 and WebFetch carried the source. Today the lane was not read at all. The honest statement is a blind day on one Daily source, and the cheap fix is to attempt the plain fetch for that source from inside `watchlist_check.py` so it never depends on a browser or on a session tool being available.
- **The skipped-upload counters are still not tracked over time.** Five too-short and two no-subtitle skips today, the same shape as yesterday's eight and two. A per-channel standing count of what the length and subtitle filters reject would show a channel changing format rather than going quiet. Logged for the fourth time, not built.

"""

RUNLOG = """# Advertising Science: Research run 2026-11-19 (Thursday)

Result: 1 transcript in, 4 claims added, 8 amended, 0 contested, 1 law paragraph added, 0 errors, 1 coverage gap.

## 1. Harvest

`lib/harvest.py daily`, 12 of 12 roster channels listed clean, 0 errors, 0 RSS fallbacks. First fully clean listing in this run series.

- 1 new transcript: Jon Loomer, *Do Not Listen to People Like Me*, 2026-11-18, 9 min, 1,445 words. Read in full.
- 5 uploads skipped as too short, 2 with no subtitles, 0 out of window.
- `nick-theriot` listed clean today after yesterday's HTTP 404, so that failure was transient and the handle check flagged yesterday is not owed.
- Unextracted backlog after this run: 0.

## 2. Watchlist

Automated lane, `lib/watchlist_check.py`, 0 errors.

| Source | Result |
|---|---|
| Meta Engineering | **2 new**, both read in full, both banked at MD-202. Feed build 18 Nov. |
| Meta Newsroom | 2 new, both opened and read in full. 1 amends LS-076, 1 not banked. |
| Google Ads & Commerce | 1 new, read in full, banked at GA-103. Feed build 18 Nov. |
| Google Ads announcements | Flat at 396 answer IDs, 0 added, 0 removed. |
| TikTok SDK changelog | Unchanged at v0.1.8. |
| arXiv cs.IR | 21 items in the Thu 19 Nov 05:00 UTC build, 2 passed the advertising filter, 1 banked. |

The two Meta Engineering posts are one series: "How Meta Uses AI Agents to Scale ML Innovations Across Ads Ranking Models" and "Design Once, Deploy at Scale: Building a Template-Driven ML Ecosystem", both dated 18 November, both `/ml-applications/`. Banked as one claim because they describe one system.

Newsroom item 1, "Meta Welcomes Loblaw as First Canadian Retail Partner to Muse", 18 November: opened because LS-076 instructs a re-check on every Muse post. Fifth re-check. No advertising content, one occurrence of the word ads on the page and it is site furniture. New fact: a purchase now completes inside the agent.

Newsroom item 2, "Our Approach to Updating Our Commercial Terms of Service", 18 November: read in full, no claim. Proposed commercial-terms updates put on hold after news-publisher objections about how the terms apply to Meta's web crawlers, three-phase consultation defined. Crawler and publisher rights, no advertising content.

arXiv hit 2, "UniRank", v3 replacement: read at abstract level, no claim. A real advertising-adjacent paper and not a filter false positive, but it is a benchmark and toolkit release with no deployed result and no operational claim.

**Coverage gap, stated rather than implied: Meta for Business News was not read today.** It is the one Daily scrape source `watchlist_check.py` does not handle, the Playwright MCP server failed to connect on every profile in this session, and no fetch was attempted through another route. Under the 2026-11-10 pass-2 rule the UK shelf needs two reads several hours apart to count as covered, so zero reads is a blind day on this source. `slugs_seen_cumulative` is untouched.

TikTok Newsroom, the for-Business blog and the Marketing API what's-new page were not retried. Permanent India geo-block per the standing ruling, not an outage.

Weekly (Monday) sources not due today.

## 3. Claims merged

New:

- `MD-202`, T1. A proven ranking improvement takes over a year to reach every model it applies to; Meta's target is three months, needing 5x more end-to-end throughput. So the ads model fleet is heterogeneous in time as well as in architecture, and two placements can be a year apart in which improvements they carry. Also in the claim: Standard Model Templates named and described, a published shelf life on Meta's own techniques, a second two-year scoreboard (92% less per-model engineering time, 5,000+ technique-model combinations, 80 new techniques, 0.63% average offline gain at neutral serving capacity, 0.86% cumulative online lift over 70% of models by count), and the published ship gate (offline NE gain, no training or inference cost regression, then a statistically significant online A/B win, with regression rate weighed alongside average gain). The agent-layer figures are hedged in Meta's own text and are banked as context. Operating read: an explanation to hold, never a diagnosis to offer, and no lever anywhere in it.
- `AU-103`, T1. arXiv 2611.24283v1, abstract read, full paper not opened. A deployed real-time-bidding system compresses user history into tokens computed offline and reused across candidates, and publishes both halves of the trade: 0.81% relative offline normalized-entropy reduction and +4.65% on advertiser conversion value plus +2.96% clicks, for 15% more online inference cost per request. First figure in this codex connecting a model-quality metric to advertiser money. One unnamed system, not a conversion factor.
- `GA-103`, T1. Seasonality Adjustments now available in Demand Gen on Target CPA and Target ROAS, the first bid control in that campaign type for a short promotion, with no effective date and no lift figure published. Must be entered before the promotion. The rest of the November Demand Gen drop is catalogue and e-commerce machinery our lead-generation book cannot use, and its six case-study figures carry no baseline, window, spend, control group or method.
- `MD-203`, T4. A five-item test for whether a Meta practitioner source has stopped keeping up, plus the conflict of interest that produces the pattern, stated from the author's own case. Every one of the five tells is already a law here, reached independently, so the claim adds no mechanism and is banked as a source-reading prior. Its own limits are recorded, including that the closing line against go-to sources precedes a pitch for a year of his weekly tips.

Amended:

- `MD-198`. Its limits said no retrain or refresh cadence was disclosed anywhere. It is disclosed now, and the template system it calls "a common template" is named. Pointer to MD-202 with the second scoreboard beside the first.
- `MD-199`. The cost side of a ranking improvement now has an outside number, 15% more inference cost per request for a shipped win (AU-103), which prices the "resource-intensive low-impact work is trimmed first" line this claim quotes.
- `LS-076`. Fifth re-check, 2026-11-19. Tier and status unchanged. The addition is that a purchase now completes inside Muse, which means a conversion that fires no pixel and has no landing page, and that remembered brand preferences now accumulate against a named retailer's catalogue. Still no ad inventory and no advertiser-facing surface.
- `MD-052`, `MD-075`, `MD-015`, `SC-014`, `LS-006`. Source adds only. Loomer names each as one of five tells of a stale source, with no new evidence and no new detail on the mechanism, so each gets the source and a pointer to MD-203 rather than support.

Not banked, deliberately:

- The Meta commercial terms-of-service consultation. Crawlers and publisher rights, no advertising content.
- The UniRank benchmark paper. Advertising-adjacent and real, no deployed result, no operational claim.
- The six Demand Gen case-study percentages. Recorded inside GA-103 as unusable rather than given standing.

Discarded as fluff: Loomer's podcast framing and the closing subscription pitch, except where the pitch is recorded in MD-203 as a limit on the claim itself.

## 4. Skill update

**Updated.** One paragraph added to the Current laws hot layer, above the 2026-11-12 MD-199 paragraph. It carries the over-a-year propagation latency and the three-month target, the shelf-life sentence, the second under-one-percent scoreboard with both publications side by side, the published ship gate, and AU-103's paired win and cost figures with the guard that the ratio is not a conversion factor. Nothing in it changes what we do on an account tomorrow, and the paragraph says so.

## 5. Gaps noticed

- **Which Meta model serves which placement is still unknown, and MD-202 raises the price of not knowing.** Two placements can now be a year apart in which improvements they carry. Our own placement breakdowns remain the only instrument on this, and neither post maps a model to a surface.
- **Normalized entropy now has exactly one bridge to advertiser money.** AU-103's roughly 6-to-1 ratio is one unnamed system, one experiment, read at abstract level. A second independent sighting would make it usable; until then every NE figure stays directional and the ratio stays unquotable.
- **No browser in this session, and today it cost the whole Meta for Business News lane.** Yesterday WebFetch carried it after a plain-fetch HTTP 400. Today it was not read. The cheap fix is to attempt the plain fetch for that source from inside `watchlist_check.py`, so the lane stops depending on a browser or on which tools a session happens to have.
- **The skipped-upload counters are still not tracked over time.** Five too-short and two no-subtitle skips today. A per-channel standing count would show a channel changing format rather than going quiet. Logged for the fourth time, not built.

## 6. Publish

See the end of this log for the commit and sync results.

## Errors

None from the harvest or the watchlist script.

- Coverage gap, not an error: Meta for Business News not read, Playwright MCP server failed to connect on all profiles.

## Files touched

- `wiki/science/Meta Delivery & Andromeda.md` (backup `.bak-20261119`)
- `wiki/science/Auction Mechanics & Bidding.md` (backup `.bak-20261119`)
- `wiki/science/Google Auction & Smart Bidding.md` (backup `.bak-20261119`)
- `wiki/science/Learning & Signal.md` (backup `.bak-20261119`)
- `wiki/science/Scaling Models.md` (backup `.bak-20261119`)
- `wiki/science/Harvest Log.md` (backup `.bak-20261119`)
- `wiki/sources/transcripts/jon-loomer/2026-11-18--jon-loomer--Do Not Listen to People Like Me.md` (`extracted: true`)
- `.claude/skills/advertising-science/SKILL.md` (backup `.bak-20261119`)

Codex audit after the merge: 1,442 claims. Tiers T1 209, T2 140, T3 928, T4 164. Status active 1,330, contested 104, superseded 5, refuted 2.
"""


def main():
    t = HL.read_text(encoding="utf-8")
    if "## 2026-11-19 (Thursday)" in t:
        print("SKIP harvest log: already present")
    else:
        bak = HL.with_suffix(HL.suffix + ".bak-20261119")
        if not bak.exists():
            shutil.copy2(HL, bak)
        anchor = "## 2026-11-18 (Wednesday)"
        i = t.index(anchor)
        HL.write_text(t[:i] + ENTRY + t[i:], encoding="utf-8")
        print("harvest log entry inserted")

    p = RUNS / "2026-11-19-research-log.md"
    p.write_text(RUNLOG, encoding="utf-8")
    print("run log written", p)


main()
