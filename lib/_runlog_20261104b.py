import io

P = r"E:\claude code marketing skill\.claude\skills\advertising-science\runs\2026-11-04-research-log.md"

ENTRY = """

---

# Research run 2026-11-04, pass 2 (18:38 IST)

**Result: no new claims, four amendments, one defect in our own parser closed a gap pass 1 left open.** 1 transcript in, **0 claims added**, 4 amended (LS-035, LS-089, LS-060, MD-191), 0 contested, 1 arXiv paper banked as an amendment and 1 read and refused. **`SKILL.md` was deliberately NOT updated.** Pass 1 ran at 04:46 and banked MD-196 and MD-197; nothing from that pass was touched or duplicated.

**The findings in one line each.** Jon Loomer read the same Meta post this codex banked on 2026-10-24 and added a consolidation line stricter than Meta's own arithmetic, 100 conversions a week before a second ad set may even be considered, plus the condition that clearing the arithmetic is necessary and not sufficient. And the Meta for Business UK shelf has always carried card dates in a day-first format our parser never tries, so yesterday's unverified UK ceiling is now confirmed from today's own body and the UK-needs-WebFetch instruction is retired.

## 1. YouTube harvest

`lib/harvest.py daily`, 18:38:15 to 18:38:55 IST. `errors: []`, `rss_fallback: []`.

- All 12 roster channels listed on the primary route. **1 new transcript**, Jon Loomer, "Your Extra Ad Sets Are Costing You 28% More", published 2026-11-04, 7 minutes, 1,046 words.
- 3 skipped as too short, 0 missing subtitles, 0 out of window.
- **First fully clean primary-route run on this roster in four days**, after 12/12, 0/12 and 6/12 secondary-route fallbacks on the three preceding runs. Recorded because the swing itself is the only reason the route was being watched.

Read in full, decomposed, `extracted` flipped to `true`. No unextracted transcripts remain on this roster.

## 2. Watchlist

`lib/watchlist_check.py`, dry run then `--commit`. `errors: []` on both.

| Source | Result |
|---|---|
| Meta Engineering (RSS) | HTTP 200, 9 in feed, 0 new. Build Tue 3 Nov 19:02 UTC |
| Meta Newsroom (RSS) | HTTP 200, 10 in feed, 0 new. Build Thu 29 Oct 20:14 UTC |
| Google Ads & Commerce (RSS) | HTTP 200, 20 in feed, 0 new. Build Wed 28 Oct 21:30 UTC |
| Google Ads Announcements | HTTP 200, 396 answer ids, 0 added, 0 removed |
| TikTok SDK changelog | HTTP 200, top version 0.1.8, baseline 0.1.8, unchanged |
| **arXiv cs.IR (RSS)** | HTTP 200, **35 items, 32 new links, 2 passed the ad filter**. Build Wed 4 Nov 05:11 UTC |
| Meta for Business News US | Read once at 04:49 (HTTP 200). **Plain fetch HTTP 400 at 18:42.** No second read owed |
| Meta for Business News UK | Read once at 04:49 (HTTP 200). **Plain fetch HTTP 400 at 18:42.** No second read owed |

**The arXiv lane produced its first in-lane items since the link-shape defect was hand-patched.** 32 new links in a rebuilt 35-item feed, 2 through the keyword filter. Both abstracts were read in full. The arXiv API returned nothing for either title, so both were read from the cs.IR RSS `<description>`, which carries the complete abstract; that is a route note rather than an error, and it is worth keeping because the API is the obvious first reach and it was the wrong one. **The two code fixes are still absent from `lib/watchlist_check.py`:** normalise to the bare arXiv id before comparing, and read `arxiv:announce_type`.

**Meta for Business News: no new read, and that is the correct outcome.** The shelves were read once today at 04:49, HTTP 200 on both pinned URLs, 12 slugs each, 0 new, fourth consecutive flat day. The one-read-per-day rule of 2026-10-09 has now had three pass-2 re-reads demonstrate that a second read buys no coverage. **Plain fetch returned HTTP 400 on both pinned URLs at 18:42 IST, about 14 hours after both answered HTTP 200.** Fourth separate confirmation that the 400 is intermittent rather than a wall, and the first measurement of how fast a working window closes. Route order unchanged: plain fetch, then WebFetch, then the browser.

**TikTok product and policy news remains unmonitored.** India geo-block, permanent, confirmed 2026-08-20. Only the SDK changelog was read. Not logged as a clean TikTok read. **The weekly (Monday) lane is not due and was not re-read**; Monday 2026-11-02 read all eight, so nothing is owed. Not re-reading them is not logged as a clean read.

## 3. Extract and merge

**Zero new claim IDs, and that is the merge protocol working rather than a thin day.** The transcript is Loomer reading the Meta post banked on 2026-10-24 as LS-089, LS-090 and MD-187. Most of it restates banked claims and was discarded as such.

**Amended: LS-035**, fourth operator onto the consolidation side. His line is stricter than Meta's arithmetic: "One campaign and one ad set. Only consider a second ad set if you're generating at least 100 conversions per week", where the published formula permits two at exactly 100. **The part no other operator on file states is that the arithmetic is necessary and not sufficient:** "even then, only do it because you have a really good reason for it. Typically, that means there's a problem you're solving with that second adset." He names unnecessary targeting segmentation and standalone creative-testing ad sets as the two insufficient reasons, and limits his objection to creative-testing ad sets to budget rather than principle. Evidence is the same class as the three operators already there, audits and one-on-one sessions, nothing on screen, no comparison. **The count on that side goes to four and the evidence quality does not change. Theriot's contesting account at 10 to 20 live ad sets still stands unanswered by any of them.**

**Amended: LS-089**, on two counts. He uses the formula forwards, which is the direction the claim argues for, working it on screen at $2,000 a week and a $20 cost per result to a two-ad-set ceiling. He also judges the formula unnecessary, which is a useful check on treating a published formula as a finding. **And he propagates the 28% with Meta's hedge stripped off**, sharpening "in our analysis" into "on average" and closing on it as a decision input, without remarking on the missing population, sample, window or control, and without noticing that sub-50 versus over-50 is also small accounts versus large ones, which is the MD-171 selection defect. **This is evidence about the figure's circulation, not evidence for the figure. The standing instruction is unchanged: carry the direction, never the 28%. What is new is that we should expect to meet it second-hand from credible operators and from clients.** He is also the first source anywhere to challenge the post's provenance on its face, twice.

**Amended: LS-060**, second independent operator declining to manage toward the threshold, and he holds both halves at once. Having just endorsed the 28% as real, he tells the single-ad-set sub-threshold account to carry on: doubling the budget to reach 50 is "incredibly risky", and "as long as you're getting results that are good enough to make it worthwhile... keep doing what you're doing." On his own reading those accounts are paying the 28% and he still rules out chasing it, so his decision rule is unit economics rather than the label. He gives Meta its say and declines to act on it. **The first operator on this side was high-ticket lead gen; this one is ecommerce-weighted, which is the stronger pairing.** His distinction is which account is actually at fault: not the one that cannot reach 50 on its whole budget, but the one that has the budget and splits it anyway.

**Amended: MD-191**, external corroboration plus one mechanism detail Meta did not state. **ReuseGR (arXiv:2611.04259)** builds the same semantic-ID generative retrieval pipeline on an industrial search-advertising system and treats it as the established baseline rather than the novelty. Its contribution is a split into a **query-level plan shared and cached across people** and a **request-level completion that cannot be shared**, because "when different users submit the same query, generating complete Semantic IDs (SIDs) for every request repeats computation, while their interaction histories call for different results". A 7B offline planner produces the shared prefixes; a 0.5B online model uses the individual's history to choose one and finish the tokens. **Read against MD-191 that says the person-specific half of the ideal-ad description is the expensive half, and the platform-side incentive is to cache everything that is not person-specific.** Independent support for the hardest part of the claim, that two people issuing an identical query should be matched to different ads by design. **Guards written into the claim and they are heavy:** not Meta, not Google, platform never named, we do not buy it, same treatment as AU-101 (Pinterest). Its figures are infrastructure results on an unnamed platform, 3.83pp query-level HR@100, 38.9% lower latency, a 14-day A/B at +0.93% CTR and +1.05% revenue per thousand requests, 3.38M-item catalogue. **None travels near a client and nothing in the paper is a lever.** The catalogue is also four orders of magnitude below the pool at MD-188.

**Read and NOT banked, with the reason. OneTrans-GSR (arXiv:2611.04720).** It describes a learned slate-assembly stage in which advertising cards compete against product cards, short videos and livestreams for the final exposure slate, replacing hand-crafted mix-ranking rules with one autoregressive policy trained against a slate-level reward, with business constraints enforced at decoding, reporting +2.63% GMV per user, +2.06% advertiser value and +2.03% repurchase rate. **It is a genuine gap in how this codex describes the pipeline, which ends at ranking and top-K selection.** Refused anyway: unnamed industrial recommender platform, neither Meta nor Google has named such a stage, it is a content feed rather than an ad auction, and there is no setting, report or advertiser surface anywhere in it. Logged here so a future run does not re-read it, and flagged as the shape of claim to bank if Meta or Google ever names an equivalent stage.

**Also read and not banked from the transcript**, each with its reason: the "for years" and audit-volume credentials, biography; the AI-authorship complaint, carried inside LS-089 as provenance rather than banked, since it is not an argument against the content; the podcast subscribe-rate-and-review appeal.

**ID safety.** No new IDs were taken, so the concurrency hazard carried since 2026-09-10 had no surface today. The teacher lane runs at 08:00 and this pass ran at 18:38.

## 4. Law layer

**NOT CHANGED, deliberately, and `SKILL.md` was not touched.** The runbook's bar for step 4 is a new T1 or T2, a refutation, or a contested core claim. Today produced zero new claims and zero contests. **The 28% propagation sharpens a reading rule the law layer already carries verbatim**, "Carry the direction and never the 28%", so there is nothing to rewrite: an operator circulating a figure is a change in the information environment around a law, not a change in the law. Same bar that kept MD-194 out on 2026-11-03 and that MD-196 cleared this morning. The four amendments all deepen claims the law layer already cites and none of them changes what it instructs.

## 5. Cache and gaps

`cache/watchlist-seen.json` backed up to `watchlist-seen.json.bak-20261104-pass2` before the write, then committed. `Learning & Signal.md`, `Meta Delivery & Andromeda.md` and `Harvest Log.md` were backed up to `.bak-20261104-pass2` before writing. `Watchlist.md` carries the new parsing note.

**FOURTH DEFECT IN OUR OWN RESEARCH LANE IN FOUR DAYS, FOUND AND RECORDED, FIX NOT YET IN CODE. This one retires a standing instruction.** Pass 1 recorded the Meta for Business UK body as carrying **zero** parseable card dates, left the UK ceiling carried over from 2026-11-03 unverified, and concluded that a UK read needing a ceiling still has to go through WebFetch. **Re-parsing the body pass 1 itself saved (`cache/bn-uk-20261104.html`, 231,511 bytes) finds 24 parseable dates, 8 distinct, newest 27 October 2026.** The two shelves render dates in different formats and our parser only tries one:

| Shelf | Rendered format | Example |
|---|---|---|
| `?locale=en_US` | month first, with a comma | `October 28, 2026` |
| `en-gb` host | **day first, no comma, no ordinal suffix** | `27 October 2026` |

**The fix is a second pattern, not a different transport**, and it must sit alongside the ordinal-optional form the Merchant Center lane needs; the ordinal form matched zero times on both bodies today, so that is a separate defect on a separate source. **Both ceilings are now confirmed from today's own bodies with no WebFetch and no browser: US 28 October 2026, UK 27 October 2026.** The UK-needs-WebFetch instruction is retired in `Watchlist.md`. **One more observation falls out: the UK shelf reaches back to 14 May 2026 while the US shelf stops at 15 September 2026, so the two rotate at different speeds and a slug ageing off the UK shelf is weak evidence of a publishing event.**

**The checker's UTC date defect masked itself again, on the same day it was identified.** Pass 1 stamped `2026-11-03` onto a run that happened on 2026-11-04 IST; this pass committed at 18:42 IST and overwrote it with `2026-11-04`. **That is the masking mechanism demonstrated rather than inferred.** `lib/watchlist_check.py` line 100 still uses `datetime.now(timezone.utc)` and is still unfixed. A day with one early pass and no second pass remains the case that shows it.

**Gaps opened today, one new and cheap.** Loomer's 100-per-week line and Meta's formula both bear on our live ad set count, which has been unverified against LS-089 for **seventeen days** and is one spreadsheet column across the book. **Both gender gaps from pass 1 are unchanged and both are ours to answer on our own accounts:** whether a hard gender setting already saved on a live ad set survived the withdrawal, and whether the withdrawal is universal or partial.

**Gaps carried.** The business-verification status on SJR Commercial and Phoenix Truxx still unread, **sixth consecutive day**, still the one errand in the file with money behind it. The three business-news date patterns absent from the parser, added today. The arXiv version-suffix normalisation and `announce_type` read. The arXiv new-ID re-submission defect of 2026-10-23. The destination controls on a live account, which MD-146 asked for in August and MD-195 made answerable. The four unread Hindi-catalogue slugs. The Ads Decoded podcast lane unreadable. `occ-2025`, `occ-2024` and `occ-2023` unread. Google's promotion mode undocumented. TikTok product and policy news geo-blocked. The Community Standards page MD-156 flagged. The UK Advertising Standards fourth character unlocalised. The Nielsen Catalina 2026 edition unobtainable. The Harvest Log's two write ends, **sixteenth day**.

## Errors

Harvest `errors: []`, **0 of 12 channels on the secondary route**, the first fully clean primary-route run on this roster after 12/12, 0/12 and 6/12 on the three preceding runs. Watchlist checker `errors: []` on both the dry run and the committed pass. Plain fetch HTTP 400 on both business-news pinned URLs at 18:42, handled under the recorded route order, no read owed, not an outage. The arXiv API returned nothing for either paper title and both abstracts were read from the cs.IR RSS `<description>`; recorded as a route note, not an error. The `rizzdial` MCP server failed to connect, `claude.ai Figma` returned HTTP 503 earlier in the session, and several other MCP servers needed authorization or were still connecting; none is a research source and none affected this run. **No source in today's due set went unread.**
"""

t = io.open(P, encoding="utf-8").read()
io.open(P, "w", encoding="utf-8").write(t.rstrip() + "\n" + ENTRY)
print("run log appended, %d -> %d chars" % (len(t), len(t.rstrip()) + len(ENTRY) + 1))
