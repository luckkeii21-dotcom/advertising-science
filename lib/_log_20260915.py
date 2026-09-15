# -*- coding: utf-8 -*-
"""2026-09-15: write the Harvest Log entry and the run log."""
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

SCI = Path(r"E:\claude code marketing skill\Obsidian God-level Marketing Vault"
           r"\God-level Marketing\wiki\science")
RUNS = Path(r"E:\claude code marketing skill\.claude\skills\advertising-science\runs")

ENTRY = """## 2026-09-15 (research run)

**2 transcripts in, both read in full. 3 claims banked, 7 amended, 0 contested. Backlog 0. Codex 1,211 to 1,214.**

**The day's substance is one 29-minute Charley T video, and most of it was already here.** Nine of the eleven propositions in it restate banked claims, which is what the merge protocol is for. Three things were genuinely new: the **10% and 40% spend thresholds** that bound which ad you are allowed to remove (SC-159), the **leverage-only definition of a passing creative test**, where an ad with a good cost per result is killed anyway because the campaign still cannot take a budget increase (CR-244), and **average-order-value spread inside one ad set** as a signal-quality problem rather than a reporting one (LS-079). Four amendments sharpened numbers the codex already held: headroom is a gap and not a score, the 5% step is really "half your headroom", read frequency daily against the campaign's own baseline, and launch two 322s per concept because one test is binary.

**The Nick Theriot video was 80% tool workflow and was mostly discarded.** One thing in it is bankable and it is a number, not a mechanism: his agency now spends over $12,000 a month on human UGC creators and over $20,000 a month on AI video, across almost 30 clients, and he says the ratio has flipped. Banked as an amendment to CR-060 with the limit stated, because it is a production-budget fact and he makes no performance claim behind it.

- **YouTube harvest:** 2 new transcripts from 12 channels (Charley T 5,139 words, Nick Theriot 2,704). 11 skipped under the 150-second floor, 11 out of window, 0 missing subtitles, 0 errors. **All 12 channels listed on RSS with zero fallbacks**, which reverses the three-day decay to 12-of-12 fallback recorded on 2026-09-13.
- **Watchlist:** nothing new. Tuesday, so the Monday-only sources were not due. Meta Engineering 0 new but its feed rebuilt Mon 14 Sep 23:01 UTC after six days flat at 8 Sep. Meta Newsroom and Google Ads & Commerce feeds both still on their old builds, 0 new. arXiv: 48 items on Tuesday's own 04:00 UTC build, 45 unseen, **0 passed the advertising filter**. TikTok SDK unchanged at v0.1.8, and TikTok is not logged as clean because only the changelog answers from this egress.
- **Meta for Business News: 12 cards, titles identical to 2026-09-13 and 2026-09-14, zero new.** All five dates that had drifted one day earlier on 2026-09-14 drifted back today, which confirms the 2026-09-14 finding that the drift is a rendering artefact and the title is the stable key.
- **A title baseline for that source now exists.** The cache record still held the 2026-09-07 slug set, eight days stale, because every run since 09-10 read the page in the browser and never wrote back. Seeded with today's 12 titles and dates, so tomorrow's run has something to diff the rule against.
- **The Google Ads Announcements render nonce was caught twice inside one run**, 3 minutes apart, on the same 2,350-line page: added `13386450140634841372`, then `12489988829632794507`, same token removed both times. Fourth consecutive day. Not news.
- **No law changed.** Everything banked today is T3 from one operator with no shown data.
- Gaps: the concurrency hazard is unacted for a sixth day, the watchdog still guards only the research lane, the arXiv framing-sentence filter is still open, GeoX is still not installed, and Qualified Future Conversions still has no codex entry.

"""

p = SCI / "Harvest Log.md"
txt = p.read_text(encoding="utf-8")
anchor = "## 2026-09-14 (teacher run)"
assert txt.count(anchor) == 1
p.write_text(txt.replace(anchor, ENTRY + anchor, 1), encoding="utf-8")
print("Harvest Log entry written")
