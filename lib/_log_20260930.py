"""Prepend the 2026-09-30 entry to the Harvest Log (file is newest-first)."""
from pathlib import Path

HL = Path(r"E:\claude code marketing skill\Obsidian God-level Marketing Vault\God-level Marketing\wiki\science\Harvest Log.md")

ENTRY = """## 2026-09-30 (research run)

**1 transcript, 4 claims added, 4 amended, 0 contested, 0 refuted. Codex 1,322 to 1,326. One law-level change. 0 harvest errors, 0 watchlist errors.** New: MD-168, MD-169, CR-281, LS-084. Amended: CR-124, CR-176, MD-105, LS-076. The zero-transcript streak ended at four days.

**The day's finding: Meta is shipping a second AI surface into Ads Manager, and one button on it settles an argument this codex has carried for four passes (MD-168, T2).** Ads Creative Studio, demonstrated live by Ben Heath on 2026-09-29 after a private briefing from the Meta team building it. Pre-release on a small number of accounts, broad rollout expected. It sits on top of the AI business assistant (MD-105) and does at the asset level what the assistant does at the account level: grade the creative, compare it to top performers in your category rather than only to your own account, then generate replacements.

**The button. Meta's own interface copy offers "try new video hooks" on a proven asset and describes it as "swap out the first 3 to 5 seconds of a video with a different approach"**, with a hook-type menu of satisfying intro, emotional storytelling, skit, fear of missing out, or auto. It then generates the variants. **Law 4b has carried Fraser Cottrell's "Simple hook changes or headline swaps simply don't count as creative testing in Meta's eyes anymore" since 2026-08-25 as the strongest statement on file.** Meta built a generator for it. The delivery-penalty story is folklore with the platform standing on the other side of it, and law 4b now says so.

**Nothing empirical moved, and the log should be honest about the size of that.** A platform recommending a move is not a measured result, Meta sells inventory when advertisers ship assets, and the studio publishes no outcome data for anything it generates. **The longest-open question in this codex is unchanged: does re-cutting the first 3 to 5 seconds of an EXISTING shoot revive a fatigued winner? Nobody has run it, Meta included.**

**The second thing on that surface is the one our own reporting has to answer to (CR-281, T2).** Meta now publishes a **number** for minimum acceptable creative performance, split by format: **2.92% click-through for image ads and $20.13 cost per result** on the one account shown, where Ads Manager previously gave only Above average / Average / Below average. CR-248 already measured what that three-band grade is worth on our accounts, 22 of 24 ads graded Above average in one week. **The catch is a slider.** Each threshold is advertiser-editable with a reset button, so it cannot be an auction input and it is not a statement about what the market achieves. It decides which of your own ads get flagged. **Moving it changes what you get told, not what you get charged. It must never reach a client report as a category benchmark.**

**A smaller change with a direct cost to us: the studio reports hook rate, hold rate and thruplay as NATIVE columns.** CR-176 records that Meta does not provide hook rate and that Heath builds it as a custom metric, 3-second plays over impressions. That build is being retired by the platform. **The finding in CR-176 survives intact**: a native column makes the metric cheaper to read, and does not make it predict cost per result.

**Meta Newsroom carried 4 new posts. All 4 were read in full, 1 was banked (MD-169, T1).** Muse for Small Business, 2026-09-29: "Muse can connect your Instagram professional account analytics, Facebook Pages, and Meta ad accounts in a few clicks", and one of the five use cases Meta publishes is "analyze what's working or not, and draft a campaign for next week". MD-159 recorded the first agent-reachable Meta buying surface, the Ads MCP connector, which is a developer route. **This is the same capability arriving in a consumer app pointed at the business owner directly**, which is the population our clients sit in. Meta names no write scope and no permission model, so what "draft a campaign" creates is unknown.

**It also moves LS-076 from a watch note to a live question, and the tier stays put.** LS-076 banks Meta's launch-day sentence that Muse conversations and VM data do not reach the ad systems. Three weeks later Muse reads ad accounts. **Reading an ad account is the opposite direction from feeding the ad systems, so nothing is contested.** The two surfaces now sit inside one agent, which is exactly the condition under which a launch-day commitment gets quietly revised.

**The other 3 Newsroom posts were read and deliberately not banked**, so a future run does not re-read them. *Forum, a dedicated app for Facebook Groups* (new app, new member role, AI "Ask" over group posts, topic labels): no ad product, no placement, no advertiser-facing feature. *Expanding Instagram's School Partnership Program* (school hub, verified students, clubs and teams): teen safety, makes no ad-targeting statement. *One Step Ahead anti-scam campaign* (APAC, 303M people reached across 18 countries, 1.3 billion impressions, 1.2M link clicks since May 2026): these are Meta's numbers for Meta's own public-service campaign, with no cost, no objective and no benchmark attached, and a 0.09% link-click rate on a PSA sets no bar for anything we run.

**A MD-105 correction that nobody would find without reading two sources against each other.** MD-105 quotes Meta's published "20% increased resolution rates of common account issues". Heath restates the same figure from a Meta briefing as the assistant being "able to resolve about 20% of account issues". **A 20% relative improvement and a 20% absolute rate are different claims and one reading is wrong.** Neither carries a methodology. The figure is now unusable in either form and is flagged as such in the claim.

**arXiv passed 1 through the filter and it was a partial true positive (LS-084, T2).** 2607.26621v3, *OneLatent*, and **it is a replace rather than a new paper**, v1 dates to July 2026. Latent-reasoning compression for a foundation recommendation model, deployed with a purpose-built serving system, reporting over 17x online inference throughput and, in one sentence, "an estimated 9.6% revenue lift" from an online A/B test in Kuaishou's local-services advertising scenario.

**It is banked for what it is next to, not for what it says.** Alone it changes nothing we do. Beside LS-083, which recorded Tencent running a compressed shared user-behaviour representation in production for ten months, it makes **two large ad platforms reporting the same architectural move inside one month**: put a large-model reasoning layer into the ranking stack, then compress it until it is cheap enough to serve. One observation is a company, two is a direction, and the binding constraint in both papers is serving throughput rather than accuracy. **A platform revenue lift is not an advertiser's cost per result and must never be quoted as one.**

**Filter note, and it is the second counter-example in three days.** The only bank-list term in the OneLatent abstract is `advertis`, once, in the second-to-last sentence. That is the exact outcome-clause shape recorded as a false-positive signature on 2026-09-07 and twice on 2026-09-25. It is a partial true positive: the deployment is genuinely inside an ad system, the method is not about advertising. **After LS-083 on 2026-09-28, the pending first-or-last-sentence rule now has two known false negatives and it should stay unshipped.**

### Watchlist

| Source | Result |
|---|---|
| Meta Engineering (RSS) | 200, build 29 Sep 16:24 UTC. 9 in feed, **0 new**. Build moved after 5 days flat, contents did not |
| Meta Newsroom (RSS) | 200, build 29 Sep 16:00 UTC. 10 in feed, **4 new**, all 4 read in full, **1 banked** |
| Google Ads & Commerce (RSS) | 200, build 24 Sep 16:00 UTC. 20 in feed, **0 new**. Build 6 days flat |
| Google Ads Announcements | 200. **396 answer ids, 0 added, 0 removed.** Seventh consecutive unchanged day |
| arXiv cs.IR | 200, build **Wed 30 Sep 04:00 UTC**, run landed after 04:00 UTC so this is today's build. 41 items, 39 new, **1 passed the filter, 1 banked** |
| TikTok SDK changelog | 200, **unchanged at v0.1.8** |
| TikTok blog / Newsroom | India geo-block, permanent, not retried. **Policy and creative still unmonitored** |
| Meta for Business News, US | **READ, and without a browser.** 12 titles, 0 added, 0 removed against the 2026-09-28 baseline. Ceiling holds at 21 Sep 2026 |
| Meta for Business News, UK | **NOT CHECKED.** The bare URL serves the India shelf from our egress. Baseline now 2 days stale |
| Weekly (Mon) lane | Not due, today is Wednesday. The 2026-09-28 Monday run completed, so no catch-up is owed |

Cache committed, `last_run: 2026-09-30`.

**The zero-browser day is no longer a Meta blackout, and the 2026-09-22 ruling over-reached (3 notes added to Watchlist.md).** All four Playwright profiles failed CONNECT_TIMEOUT at session start, and a plain fetch returned HTTP 400 on both Business News URLs, on both Ad Standards locales and on the AI at Meta blog, exactly as that entry predicts. **WebFetch on `?locale=en_US` then rendered the page in English (US) with all 12 titles and dates.** That is the first clean title-set diff ever run on the US lane without a browser, and it makes the most important source on this watchlist browser-optional. The 2026-09-22 finding is true of plain fetch and was generalised to the lane.

**`?locale=en_US` is load-bearing, and yesterday's run is the control.** On 2026-09-29 WebFetch was pointed at the bare URL and rendered India, which that run correctly refused to commit. Today the bare URL did it again, in Hindi, while the parameterised URL rendered US English in the same session. **The parameter controls the render; without it the page falls back to our egress, not to UK and not to US.**

**So the bare URL does not give us the UK shelf, and the 2026-09-20 standing instruction needs the correction.** That instruction says to read both URLs and diff the sets separately, on the finding that the bare URL renders en_GB from New Delhi. It rendered Hindi/India on both of the last two days. Today's India set overlaps the cached UK set on 8 of 12 titles, with the other four all back catalogue (15 Sep 2025, 17 Jun 2024, 28 Feb 2023, 29 Jul 2022), **the same 8-and-4 split as 2026-09-29**, so the India shelf is stable and is not rotating past us. **A bare-URL read from here is an India read and must never be committed against `titles_uk`.** The UK lane is logged as not checked, with its baseline 2 days stale.

**One byte-count trap recorded so nobody chases it.** `transparency.meta.com/policies/ad-standards/` returned **HTTP 400 with a 266,875-byte body**, against the 1,542-byte error body the 2026-09-22 entry records for `facebook.com/business/news`. The large body looks like a successful render and is not one: strip scripts and tags and **the visible text is 7 characters and reads "Error"**. Judge a Meta 400 on its rendered text, never on its length.

### Gaps carried forward

- The UK shelf on Meta for Business News needs a browser with an explicit `en-gb` path, or a UK egress. Nothing we ran today can reach it.
- TikTok policy and creative stay unmonitored behind the India geo-block.
- The arXiv first-or-last-sentence rule now has two known false negatives, LS-083 and LS-084. It should stay unshipped and the gap should be restated as a decision rather than as pending work.
- No en-gb hash set for Meta Ad Standards, open since 2026-09-14.
- **Marketing API v24.0 sunsets 6 October 2026, 6 days out.** Nothing of ours is pinned to it, still worth one check.
- Ads Creative Studio is not on any of our accounts yet. When it lands, read each default threshold BEFORE touching the slider and compare it to that account's own trailing click-through rate.
- The 14 craft claims banked 2026-09-28 are still untested on our accounts. CR-268 is the cheapest T3-to-T2 upgrade on the board.

"""

body = HL.read_bytes()
nl = "\r\n" if b"\r\n" in body else "\n"
text = body.decode("utf-8").replace("\r\n", "\n")

marker = "One line per Research run: what came in, what changed. Quiet days get one line and nothing else."
i = text.index(marker) + len(marker)
text = text[:i] + "\n\n" + ENTRY.rstrip("\n") + "\n" + text[i:].lstrip("\n")
HL.write_bytes(text.replace("\n", nl).encode("utf-8"))
print("Harvest Log.md: 2026-09-30 entry prepended above 2026-09-29")
