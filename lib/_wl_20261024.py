# -*- coding: utf-8 -*-
"""2026-10-24: Watchlist.md and Harvest Log.md entries."""
from pathlib import Path

W = Path(r"E:\claude code marketing skill\Obsidian God-level Marketing Vault\God-level Marketing\wiki\science")

wl = """
### A run log claiming the cache was committed is not evidence that it was (2026-10-24)

The 2026-10-23 pass recorded "Cache committed by `watchlist_check.py`" under its watchlist table. It was not. `cache/watchlist-seen.json` still carried an mtime of 21 October 15:13 when today's run opened it, so three items the 23 October log had already read and dispositioned came back as new today: the Google Ads & Commerce holiday bidding teaser, the arXiv OneLatent re-submission, and a Meta Newsroom post on Forum group-admin tools.

**No harm done, because all three were checked against the 23 October log before anything was banked and none of them was re-banked.** The cost was three lookups. The risk if it had gone unnoticed is worse than the cost: a re-surfaced item read fresh gets banked twice under two IDs, which is exactly the duplicate the merge protocol exists to prevent.

**Standing check, and it is one line.** Before trusting the diff, compare the mtime of `cache/watchlist-seen.json` against the previous run's date. If the cache is older than the last completed run, treat every "new" item as unverified and check it against the previous run log before reading it as news. Run `watchlist_check.py --commit`, never the bare form, on a real pass.

### The TikTok lanes are a geo-block and the 2026-10-23 log repeated the banned framing (2026-10-24)

The 2026-10-23 run log recorded "TikTok Newsroom / blog: **Skipped: browser unavailable.**" That is the exact framing the 2026-10-15 pass-2 note rules out. The block is an India geo-block, verified 2026-08-19 across both the browser and curl on four paths each, and a browser does not move an egress. **A session with a working browser cannot check these sources either, so browser availability is not the reason and must not be named as one.** The honest line is the one already written into this file: TikTok policy and creative announcements are genuinely unmonitored until a non-India egress exists. Today's run had four working Playwright profiles and the TikTok lanes were still unreadable.

### Both locale shelves carried the same new post on 2026-10-24, which the partition finding does not predict

The 2026-09-20 locale-partition finding is that the US and UK shelves hold different catalogues, so a source can look quiet on one while the other has moved. On 2026-10-24 the new post, "you-dont-beat-the-auction-you-brief-it", dated 21 October 2026, arrived at **slot 1 on BOTH shelves**, and the UK shelf's only departure was `unlocking-the-value-of-q5marketing-for-mobile-game-developers`, the known slot-1 toggle. So a simultaneous arrival happens too, and reading one shelf would have found this post. **The partition rule still stands as a floor rather than a prediction: read both, because a one-shelf arrival is possible and a two-shelf arrival costs nothing extra to confirm.** A plain HTTPS fetch returned HTTP 400 again today, bare and with `?locale=en_US`, so the browser remains required for this source.
"""

p = W / "Watchlist.md"
t = p.read_text(encoding="utf-8")
assert "A run log claiming the cache was committed" not in t
p.write_text(t.rstrip("\n") + "\n" + wl, encoding="utf-8")
print("OK  Watchlist.md (+%d chars)" % len(wl))

log = """
## 2026-10-24

**Zero transcripts, one source, four new claims. The whole day came from one Meta for Business best-practice post.**

**YouTube harvest.** Ran 03:03:37 to 03:04:18. Errors none, 0 of 12 channels failed, **0 new transcripts**. skipped_short 3, no_subs 1, out_of_window 0, rss_fallback none. Every channel returned 0. No unextracted backlog.

**Watchlist.** Meta Engineering 0 new (feed built 2026-10-20). Meta Newsroom 1 item, read, Forum group-admin tools, no advertising content anywhere in it, discarded. Google Ads & Commerce 1 item and arXiv 1 item passing the ad filter, **both already read and dispositioned on 2026-10-23** and resurfaced only because that run did not actually commit the cache (see Watchlist.md). TikTok SDK changelog unchanged at 0.1.8. Google Ads announcements 396 answer IDs, 0 added, 0 removed. Weekly Monday sources not due, today is Saturday, and the 2026-10-19 Monday run completed. TikTok Newsroom and for-Business blog unreadable, India geo-block, four working browser profiles in session and none of them helps.

**Meta for Business News, the find.** US shelf read in the browser at `?locale=en_US`, plain fetch HTTP 400 again. One genuinely new slug at slot 1 on both the US and UK shelves: **"Peak Season 2026: You Don't Beat The Auction. You brief it.", Best Practice, dated 21 October 2026.** Read in full. Ceiling moves from 19 to 21 October 2026.

**Claims banked, 4 new.**
- **LS-089**, T1 for the sentence. Meta publishes the ad-set count formula, weekly budget / (cost per result x 50), and says most accounts exceed it. **It is the exact back-propagation Blue Sense Digital calls a mistake, so the LS-001 contest is now practitioner-versus-Meta.** Reconciled: forwards it caps ad set count, backwards it is LS-060.
- **LS-090**, T1 for the sentences, T4 for the diagnosis. Every edit costs twice, the restarted learning phase plus the old instruction spending at full price the whole time it was wrong, and only the first appears on screen. This codex had never priced the cost of NOT changing. Prescription: batch the changes, one learning phase instead of five.
- **MD-187**, T1 for the sentence. The optimisation event decides which creative wins, not only who is reached. "Same ads, same budget, different winner, because you changed what winning meant." **Measurement consequence: any creative before-and-after spanning an event change is void.**
- **AT-132**, T1. Meta's three attribution settings defined side by side, standard counts what the ads touched, incremental what they added, custom the way the business counts it. Custom attribution appears nowhere else in the file. The auditable sentence is Meta's own: it is "the decision most likely to be inherited rather than chosen".

**Merges, 2.**
- **LS-001.** The first first-party performance number ever attached to the 50-conversion threshold, about 28% more expensive per purchase below it. Its whole footnote is "in our analysis". Carry the direction, never the digits.
- **MD-171.** Sixth instance of the unfootnoted-Meta-figure pattern in seven weeks, and a new failure mode: **a superscript footnote marker with no footnote text anywhere on the page.** The 42% planned-to-spend-less against 4.2% actually-spent-more pair is kept as a direction only.

**Discarded as fluff:** the Meta Newsroom Forum admin post, the post's closing product link.

**Law layer:** updated. SKILL.md hot layer carries a 2026-10-24 lead paragraph.

**Gaps noticed.**
1. The 23 October run log claimed a cache commit that did not happen. Standing mtime check added to Watchlist.md.
2. The 23 October log framed the TikTok lanes as "browser unavailable", which the 2026-10-15 ruling forbids. Corrected in Watchlist.md.
3. The arXiv new-ID re-submission defect diagnosed on 2026-10-23 is still unfixed in `lib/watchlist_check.py`.
4. "Promotion mode" still has no Google documentation.
5. **Free check available on our own book:** run LS-089's formula on every client account, weekly budget over cost per opt-in times fifty, against the live ad set count. Turns a T1 sentence into an audit instrument.
6. Zero YouTube uploads in the window. Not a fault, the roster simply did not publish.

**Errors.** Harvest none. Watchlist none from the checker.
"""

p = W / "Harvest Log.md"
t = p.read_text(encoding="utf-8")
assert "## 2026-10-24" not in t
p.write_text(t.rstrip("\n") + "\n" + log, encoding="utf-8")
print("OK  Harvest Log.md (+%d chars)" % len(log))
