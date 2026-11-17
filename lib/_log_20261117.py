# -*- coding: utf-8 -*-
"""Prepend the 2026-11-17 Harvest Log entry."""
from pathlib import Path

LOG = Path(r"E:\claude code marketing skill\Obsidian God-level Marketing Vault\God-level Marketing\wiki\science\Harvest Log.md")

ENTRY = u"""## 2026-11-17 (Tuesday) - 1 transcript in - 2 claims added, 4 amended, 0 contested, 0 laws amended

**One 61-minute episode carried the whole day and it was worth reading in full. 2 claims banked, [[Creative Science#CR-292|CR-292]] and [[Creative Science#CR-293|CR-293]], both T3. 3 existing creative claims amended with a second independent operator. 1 arXiv paper amended [[Auction Mechanics & Bidding#AU-084|AU-084]]. No law changed.**

**Harvest: 1 new transcript, 0 errors.** All 12 roster channels listed clean. 15 uploads skipped as too short, 2 with no subtitles, 11 out of window. The one that came through: Andrew Faris, *Breaking Down The Ad That Spent $3M Last Month*, 2026-11-16, 61 min, 13,799 words, guest Harry Dohmgeest of Rolly Polley Digital. Read in full. Unextracted backlog is now 0.

**Banked [[Creative Science#CR-292|CR-292]], T3: the long-form creator-read script, four to five minutes, fully scripted, teleprompter, five-act story spine.** The reported spend is the reason it is banked rather than discarded as agency positioning: around $3M on his ads inside one client account in one month at roughly 50% of that account's spend with three of his ads in the top five, around $1M at a second client at 30 to 40% of spend, and a single February 2026 ad past $3M lifetime. **The one device in it the codex did not already hold is the Oracle:** a named third party inside the story introduces the product, which lets a claim be made that the speaker cannot make without sounding like a seller, and the failure mode is an oracle nobody can picture. The qualifier has to be aspirational and physical. One causal anecdote attached, a reported two to three times CPA drop within a fortnight of adding that qualifier to an existing script, single case, no account, no baseline. Also inside: the four hook openings against one body script, the three beats he says are in basically all his winners (results timeline, third-party compliment, oracle callback), and how hard direct-response CTAs survive a friend-to-friend tone by being rephrased as something the speaker personally observed.

**Banked [[Creative Science#CR-293|CR-293]], T3: casting as a lever with its own budget.** The transferable finding is the non-transferability one. Performers who win in other accounts died in the beauty niche, so casting gets re-run per category rather than inherited. Prices stated plainly, $700 to $900 per video against a $100 to $150 market expectation, retainers, no revenue share, and his newer client deals absorb talent cost into the agency minimum. Operating details worth copying: shortlist of five against a stated energy brief rather than a list of 50 to 100, a standing prop budget performers draw on without asking, and two takes every time with the second one giving explicit permission to inject personality while the mechanism and claims stay fixed.

**Amended, 3 creative claims, all with a second operator and none changed in substance.** [[Creative Science#CR-273|CR-273]] (no optimal ad length) gains a second operator reporting seven-figure spend at four to five minutes, reached by a different route: he buys length with narrative rather than with the problem and mechanism beats. [[Creative Science#CR-277|CR-277]] (AI script writing, selection is the human job) gains independent agreement on the same division of labour, with his stated target for model output being "a six or seven out of 10 draft". [[Creative Science#CR-245|CR-245]] (creator identity versus influencer identity) gains a fourth category, ACTOR, which is the one this format actually hires.

**Daily watchlist: every automated source either flat or irrelevant.** Meta Engineering 0 new (feed build 13 Nov, 4 days stale). Meta Newsroom 3 new, 0 ad-relevant: an Instagram recommendations update for India, a new standalone messaging app, and a Singapore small-business AI survey. The India one was opened and read because Instagram is a surface we buy on, and it is organic recommendations only, with no ad delivery, ranking or policy content. Google Ads & Commerce 1 new, a consumer Black Friday shopping-tips post, title read, not opened. Google Ads announcements flat at 396 answer IDs, 0 added, 0 removed. TikTok SDK changelog unchanged at v0.1.8.

**Meta for Business News flat on both shelves, confirmed through the browser after the documented HTTP 400.** Plain fetch returned 400 on both pinned URLs as it has every day this month, so the check ran through the Playwright profile. US shelf 12 slugs, UK shelf 12 slugs, **0 new against the 41-slug cumulative set on either.** One observation worth a line and not worth a rule change: the `en-gb` host redirected to the bare `www.facebook.com/business/news` URL today, and the page served was the same UK catalogue, not the stale third catalogue the Watchlist warns the bare URL renders. One day is not enough to amend that warning. Watch whether the redirect repeats.

**TikTok browser lanes not retried, and that is the standing ruling rather than an outage.** Newsroom, the for-Business blog and the Marketing API what's-new page are a permanent India geo-block. The SDK changelog is the live source and it answered.

**arXiv cs.IR: 56 new, 1 passed the ad filter, and it was a genuine hit.** TokenFormer V2 (2611.19074v1, 14 Nov), Tencent, evaluated on **WeChat Channels advertising** with **GMV +2.33%** in live online A/B against the production model, off **+0.07 pp** offline AUC and 5.1x fewer FLOPs. Appended to [[Auction Mechanics & Bidding#AU-084|AU-084]] as a fourth deployed non-Meta system, same surface as OneRanker. **It adds confirmation on the sequence axis rather than a new mechanism, and the number worth carrying is the ratio:** a 0.07 percentage point offline AUC move, close to the run-to-run noise floors papers in this lane publish, lands as a 2.33% production GMV change. That is why platform teams spend engineering budget on gains an advertiser would read as a rounding error. Abstract read, full paper not read.

**No law amended.** Everything banked today is T3 practitioner experience or a third-platform corroboration that explicitly changes no mechanism. The hot layer in SKILL.md is untouched.

**Gap noticed.** The codex now holds two independent operators reporting seven-figure spend on four to five minute scripts and zero of our own accounts have ever run one. Every client in the book runs 30 to 60 seconds. Phoenix Truxx and SJR Commercial both have the ingredient this format needs, a buyer with a long consideration window, and the cheapest version of the test is one four-minute script against the current best short ad in a single ad set. Until then the length claim stays T3 for us no matter how many operators report it.

"""

t = LOG.read_text(encoding="utf-8")
anchor = u"Quiet days get one line and nothing else.\n"
i = t.find(anchor)
assert i >= 0
i += len(anchor)
LOG.write_text(t[:i] + u"\n" + ENTRY + t[i:].lstrip("\n"), encoding="utf-8")
print("Harvest Log entry prepended")
