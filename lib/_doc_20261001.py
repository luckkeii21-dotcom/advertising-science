# -*- coding: utf-8 -*-
"""2026-10-01: Watchlist.md method notes + Harvest Log entry."""
from pathlib import Path

V = Path("E:/claude code marketing skill/Obsidian God-level Marketing Vault/God-level Marketing/wiki/science")

WATCHLIST_NOTE = """

### The UK shelf IS readable without a browser, and the key is `?locale=en_GB` (found 2026-10-01)

The 2026-09-30 entry above rules that "the UK shelf needs a browser with an explicit `en-gb` path, or a UK
egress", and instructs future runs to log the UK lane as not checked until one of those exists. **That
ruling is retired. WebFetch on `?locale=en_GB` rendered the UK shelf in English (UK) today, with all 12
card titles, all 12 dates and all 12 slugs, on the first attempt.** All four Playwright profiles failed
CONNECT_TIMEOUT at session start, so no browser was involved at any point.

**Both shelves therefore diffed clean in one pass with no browser, for the first time:**

| Locale | Ceiling | Slugs | Against the 2026-09-28 baseline |
|---|---|---|---|
| `?locale=en_US` | 21 September 2026, "Meet the 2026 Meta Agency Award Winners" | 12 | **0 added, 0 removed** |
| `?locale=en_GB` | 10 September 2026, Instant Hydration spotlight | 12 | **0 added, 0 removed** |

**What the 2026-09-30 entry got right and what it got wrong.** It was right that the bare URL is an India
read from our egress and must never be committed against the UK baseline. It was wrong to generalise from
"the bare URL does not give us the UK shelf" to "the UK shelf needs a browser". The missing step was to try
the parameter that already worked for the US lane with the other locale code in it. **The parameter is the
key on every locale, and it was never only a US fix.**

**Standing instruction, now simple enough to state in one line: read `?locale=en_US` and `?locale=en_GB`
through WebFetch, diff the SLUG sets, and never read the bare URL at all.** The whole source is
browser-optional. The US-to-UK ceiling gap is 11 days, unchanged from 2026-09-23, so the gap is a property
of Meta's publishing and not of our reading.

**Ask WebFetch for the hrefs, not the titles.** The 2026-09-27 note established that a slug diff is stable
where a title diff is not. WebFetch returns titles by default and three of today's twelve UK titles differ
from the stored baseline on punctuation alone: `L'Oreal` against `L'Or\u00e9al`, a hyphen against an en dash in
the social-search title, and double against single quotes in "Auto-Pilot". **A title diff would have had
three adjudications to make and a slug diff had none.** One extra WebFetch call per locale buys the stable
key.

### arXiv filter: `ad-hoc` is a FOURTH false-positive mechanism, and this one survives the whole-word rule (fixed in code 2026-10-01)

The filter notes above record three false-positive shapes, all of them about WHERE a genuine advertising
term sits in an abstract. This one is different: it is a term that is not about advertising at all.

**`\\bads?\\b` matches the "ad" in "ad-hoc", because a hyphen is a word boundary.** It fired on the GEAR
abstract at "stabilizing gradient dynamics without ad-hoc heuristics". GEAR is a true positive on two other
hits, "Ad Retrieval" in the title and "Douyin Ads" in the deployment sentence, so nothing was mis-banked
today. **The exposure is a pure recommender-systems paper that says "ad-hoc" once and nothing else**, which
would pass the filter on that alone. "ad-hoc" is ordinary machine-learning prose and appears constantly.

**The whole-word rule already in this file does not catch it.** That rule was written against substring
matches, naming "adaptive", "advanced" and "gradient", and `\\bads?\\b` correctly excludes all three. It was
never tested against a hyphenated compound whose first element is literally "ad".

**Shipped, because it is a literal exclusion with no judgement in it:** `lib/watchlist_check.py` now uses
`r"\\bads?\\b(?![- ]hoc)"`. Five regression cases are in `lib/_wl_20261001.py` and all five pass. A blanket
`(?!-)` was deliberately NOT used, because "ad-level" and "ad-set" are genuine advertising terms and would
have become false negatives.

**This stays separate from the first-or-last-sentence rule, which is still unshipped and should stay that
way.** That rule asks for a judgement about where meaning sits in a paragraph and it now has two known false
negatives (LS-083 on 2026-09-28, LS-084 on 2026-09-30). This one asks whether four characters are the word
"ad", which code can answer.
"""

HARVEST_ENTRY = """## 2026-10-01 (research run)

**1 transcript, 3 claims added, 2 amended, 0 contested, 0 refuted. Codex 1,326 to 1,329. No law-level change. 1 harvest error, 0 watchlist errors.** New: SC-173, AU-096, CR-282. Amended: SC-149, MD-166. Both shelves of Meta for Business News read clean with no browser for the first time, and the arXiv filter got a fourth false-positive mechanism found and fixed in code.

**The day's finding: the same operator reversed his own remedy five weeks apart, and both halves survive (SC-173, T3).** [[Scaling Models#SC-149|SC-149]] records Jon Loomer on 2026-08-24 naming the two upper-funnel placement exposures precisely, Audience Network for link clicks and landing-page views and ads-on-Facebook-Reels for reach, then arguing the fix is to **abandon the goal** rather than prune the placement, "because you're still bound to get cheap, low-quality optimized actions from other placements". On 2026-09-30 he prescribes those goals and prunes exactly those two placements.

**What he is solving for is [[Meta Delivery & Andromeda#MD-166|MD-166]], the 2-organic-link-posts-a-month cap, and the design is fully specified.** One permanent ad set replacing the organic publishing routine, a high-funnel performance goal, targeting restricted to the Page's own followers through custom audiences, placements pruned by goal, up to 50 ads one per post, a frequency cap, **$5 a day set to match the $149 Meta One Expert tier**. His own framing, four times in ten minutes, is that this is an exception to everything else he recommends.

**The boundary is what makes it a claim rather than a contradiction.** SC-149's remedy assumes a bottom-funnel action to fall back to. A campaign driving traffic to a blog post or a podcast episode has none, so abandoning the goal is not an available move and guard rails are the only one left. The mechanism is unchanged and he restates it in the same words: with no conversion to optimise for, "Meta will exploit weaknesses to find the cheapest and likely lowest quality optimized actions".

**Nothing here has been run and he says so: "Will $150 of ads be better than the $149 paid for Meta 1? We'll see. But my hunch is that it would be."** No spend, no account, no before-and-after. The reasoning for preferring ads over the subscription is the one durable sentence: "Meta has devalued link sharing over the years by throttling reach for businesses. With ads, I can guarantee a certain amount of delivery." The design is [[Scaling Models#SC-130|SC-130]] doing a different job, so if we ever want to test it the structure is already on file.

**The same transcript produced a third unverified Instagram figure, and our own correction has not reached him (MD-166 amended).** MD-166 records that Loomer's per-tier Instagram splits cannot be verified, because Meta's help article covers Facebook Pages only and publishes one number per tier with no Instagram split. He now adds Max at unlimited Facebook and **12** Instagram link posts. He also repeats, unchanged, that a link in a comment does not get around the cap, which MD-166 corrected on 2026-09-24: right for a standalone comment, wrong for extra links inside the comments of a post that already carries one, which Meta exempts by name.

**arXiv passed 2 and BOTH were true positives, which has not happened before on this filter.** Every prior multi-pass day on this source produced at least one outcome-clause false positive.

**2609.39327, GEAR, generative end-to-end ad retrieval at Douyin (AU-096, T1).** Serving "hundreds of millions of daily active users on Douyin Ads". The keeper is a coupled constraint rather than a result: representation collapse (the item tokenizer degenerates under continuous distribution shift) against item collisions (distinct items get identical token sequences in a large pool), and **"expanding codebook capacity to mitigate collisions inevitably exacerbates collapse"**, so the obvious fix for one causes the other. **No percentage, no revenue figure and no baseline anywhere on the arXiv page**, only "substantial empirical improvements". Banked for what it sits beside: the TAGR half of [[Auction Mechanics & Bidding#AU-081|AU-081]] makes two large platforms running semantic-ID retrieval in production, and [[Meta Delivery & Andromeda#MD-001|MD-001]] is the same mechanism at Meta. The candidate set is generated from a learned representation of the item, so what the ad IS decides which pool it can be drawn from. It changes no decision this week.

**2606.15911v2, Interactor, ad description generation in sponsored search (CR-282, T1).** EMNLP 2026 Industry Track, v1 14 June, v2 30 September, and **a replace rather than a new paper**. Deployed since late May 2026 in an unnamed "leading search ads system", serving **over 140k advertisers**. The finding for our lane is what the platform's own reward models score: **knowledge capacity and landing page consistency**, returned as a binary signal plus written feedback that the policy rewrites against over multiple turns. [[Google Auction & Smart Bidding#GA-010|GA-010]] already carries landing page experience as a T1 Quality Score component; this is a second instance on a different surface and further upstream, grading the copy against the page while the copy is being written. The paper also separates the two slots by job: titles are optimised for clicks, descriptions carry "world knowledge" and "the fine-grained selling points". **No numbers on either side**, only "contributing to both ad revenue and user experience", and a platform optimising for its own revenue is not an advertiser optimising for cost per opt-in.

**The Meta lane: both shelves clean, no browser, and a 2026-09-30 ruling retired.** Yesterday's entry concluded the UK shelf "needs a browser with an explicit `en-gb` path, or a UK egress", and told future runs to log the lane as unchecked until then. **`?locale=en_GB` through WebFetch rendered it in English (UK) on the first attempt, all 12 cards and all 12 slugs.** The parameter was never a US-only fix. US 12 slugs 0 added 0 removed, ceiling 21 September; UK 12 slugs 0 added 0 removed, ceiling 10 September; gap 11 days, unchanged since 2026-09-23. All four Playwright profiles failed CONNECT_TIMEOUT again, a tenth consecutive day of browser trouble, and it cost nothing today.

**The filter gap found today is the cheapest one this engine has had, and it is already fixed.** `\\bads?\\b` matches the "ad" in **"ad-hoc"**, because a hyphen is a word boundary. It fired on GEAR's "without ad-hoc heuristics". GEAR had two genuine hits so nothing was mis-banked, but a pure recsys paper saying "ad-hoc" once would pass on that alone, and "ad-hoc" is ordinary ML prose. **The whole-word rule in Watchlist.md does not catch it**: that rule was written against substring matches (adaptive, advanced, gradient) and never tested against a hyphenated compound whose first element is literally "ad". Shipped as `r"\\bads?\\b(?![- ]hoc)"` with five passing regression cases, because it is a literal exclusion with no judgement in it. A blanket `(?!-)` was rejected: "ad-level" and "ad-set" are genuine.

**Meta Newsroom carried 1 new post. Read and deliberately not banked**, so a future run does not re-read it: *Meta Names Dhruv Vohra to Lead Southeast Asia Business*, a leadership appointment with no ad product, no placement, no delivery statement and no advertiser-facing change.

**1 harvest error.** `ben-heath/8EqC6qf7zcw` timed out during transcript fetch. One video from one channel, and the other eleven channels listed normally. It will be retried by tomorrow's run.

**Gap for research to target: nobody has run SC-173, and we are the population.** Any client Page subject to the MD-166 cap that posts links more than twice a month can answer it for $5 a day. The single question is whether follower-targeted reach buys more clicks than the subscription buys link slots.

### Watchlist

| Source | Result |
|---|---|
| Meta Engineering (RSS) | 200, build 29 Sep 16:24 UTC. 9 in feed, **0 new**. Build unchanged from yesterday |
| Meta Newsroom (RSS) | 200, build 30 Sep 14:13 UTC. 10 in feed, **1 new**, read in full, not banked (leadership appointment) |
| Meta for Business News, `?locale=en_US` | WebFetch, English (US). 12 slugs, **0 added, 0 removed**. Ceiling 21 September 2026 |
| Meta for Business News, `?locale=en_GB` | WebFetch, English (UK). 12 slugs, **0 added, 0 removed**. Ceiling 10 September 2026. **First browser-free UK read** |
| Google Ads & Commerce (RSS) | 200, build 24 Sep 16:00 UTC. 20 in feed, **0 new**. Build flat for 7 days |
| Google Ads Announcements | 200. **396 answer ids, 0 added, 0 removed.** Stable since 2026-09-20 |
| arXiv cs.IR | 200, build **Thu 01 Oct 04:00 UTC**, today's own build. 41 in feed, 35 new, **2 passed the ad filter, both true positives**, both banked |
| TikTok SDK changelog | 200, **unchanged at v0.1.8**. Newsroom, for-Business blog and Marketing API what's-new still India geo-blocked and not retried. **TikTok policy and creative news is not monitored and is not logged as clean** |
| Weekly (Mon) sources | Not due. Thursday. The 2026-09-28 Monday run completed and read them, so no catch-up is owed |
| Playwright browser | All four profiles CONNECT_TIMEOUT at session start. **Cost nothing today**, both Meta shelves read through WebFetch |

**Cache committed.** `watchlist-seen.json` `last_run` carries 2026-10-01T14:01 IST, and both locales' slug baselines are stored at `slugs_us_2026_10_01` and `slugs_uk_2026_10_01`. Transcript backlog is **0 unextracted**.

"""

# --- Watchlist.md: append method notes
wl = V / "Watchlist.md"
wl.write_text(wl.read_text(encoding="utf-8").rstrip("\n") + "\n" + WATCHLIST_NOTE, encoding="utf-8")
print("Watchlist.md: 2 method notes appended")

# --- Harvest Log.md: insert today's entry above the newest existing entry
hl = V / "Harvest Log.md"
t = hl.read_text(encoding="utf-8")
anchor = "## 2026-09-30 (teacher run;"
assert t.count(anchor) == 1, "harvest log anchor not unique"
i = t.index(anchor)
hl.write_text(t[:i] + HARVEST_ENTRY + t[i:], encoding="utf-8")
print("Harvest Log.md: 2026-10-01 entry inserted at the top of the log")
