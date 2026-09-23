"""Harvest Log entry + run log for the 2026-09-23 research run."""
import io
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

ROOT = Path(r"E:\claude code marketing skill")
SCI = ROOT / "Obsidian God-level Marketing Vault" / "God-level Marketing" / "wiki" / "science"
RUNS = ROOT / ".claude" / "skills" / "advertising-science" / "runs"

ENTRY = """## 2026-09-23 (research run)

- **0 transcripts in, 11 new claims and 4 merges, all of it from the Meta watchlist.** The YouTube roster was genuinely quiet and the browser lane carried the whole day. First browser read of Meta for Business News since 2026-09-20, after two days with no browser at all.
- **YouTube: 0 new transcripts across 12 channels, and this is a real quiet day rather than an outage.** RSS returned 404 or 500 for all 12 channels, which has been true since 2026-09-05, and the `/videos` tab fallback listed every channel fine. One video was skipped for having no subtitles: matt-shiver, published 2026-09-22, `r8unHVbiZg4`. Unextracted backlog stays 0, so the 25-a-day rule never engaged.
- **The finding: Meta's own numbers now sit behind yesterday's peak-window item.** [[Auction Mechanics & Bidding#AU-094|AU-094]], from Meta's daily median advertiser rates across all purchase-optimised ads in all verticals, 1 Oct to 30 Nov 2025: CPMs rose through November and **CPA fell anyway, 14% on Black Friday and 15% on Cyber Monday against early October, because conversion rate rose faster than price** (+74% and +43%). [[Scaling Models#SC-170|SC-170]] is the single-account twin: Compartes ran spend +99% year over year across the same nine days, revenue +105%, **cost per purchase down 9.8%**, on 10 to 20% increments gated on returns holding. Three independent sources now point the same way.
- **The reading rule, and it is about a source this codex has been leaning on hard.** [[Attribution & Incrementality#AT-126|AT-126]]: Meta for Business News publishes real named case studies and INVENTED unnamed ones in the same format. "Holiday measurement strategies" opens with a brand walking into January with "14,200 incremental conversions at $7.40 per incremental result" and a 20% budget rise, and the footnote under the article says the example is fictional. **The test before banking any figure from this channel: is the advertiser NAMED?**
- **New claims (11).** AU-094 Cyber 5 efficiency paradox. CR-261 format diversity inside one ad set (image plus video plus vertical video with audio, 7.3% lower CPA). CR-262 let creator content prove itself organically before any paid spend. CR-263 test one messaging element per round rather than one creative. CR-264 Spanish creative reached people at roughly half the cost of English and started four times the conversations, run side by side on the same offer. SC-169 Dior's holiday campaigns were competing with each other and merging them returned 59% more per dollar at 41% lower cost per sale. SC-170 Compartes peak scaling. AT-125 a Conversion Lift study resolves in 2 to 3 weeks at holiday volume against 6+ weeks in a quiet quarter. AT-126 the fictional case study. LS-082 server-verified in-store conversions through the Conversions API cut cost per store visit 44%. MD-165 Advantage+ Audience run head to head against the advertiser's own audience strategy with DISQO measuring the brand half.
- **Merges (4), no new IDs.** AU-034 (the "Meta shows no figures" limit is now closed for Cyber 5 and still open for Q5). CR-058 (**Meta's own 19% partnership-ads figure was generated at 20% or more of cell spend, above the roughly 10% allocation this codex has been recommending**, and the underlying data runs June 2021 to January 2022 and June 2023 to June 2024, none of it post-Andromeda). MD-159 (Meta AI business features read your ad account, your organic analytics and Google Workspace; free now, heading behind the Meta One paywall). MD-160 (**65 million scam ads removed globally so far in 2026, 94% before any user report**, against the 137,000 and 88% Poland figures already banked; plus 3.6 million "shell pages" actioned in July on Singapore Police signals, Pages Meta itself describes as carrying no ads and no violating content).
- **Tier discipline, exercised once, and it cost most of the day's headline numbers their tier.** Six of the eleven claims come from Meta's 2026 Agency Awards post. Those entrants are agencies competing for an award, the results are agency-submitted, the panel is drawn from Meta and its award partners, and the winners were selected partly ON those numbers. **All six are tiered T3 with the survivorship caveat written onto each**, rather than T1, even though Meta published them. The Cyber 5 aggregates are T1 because Meta states a window and a method, with the observational limit attached: the November advertiser population is not the October one.
- **AT-125 pulls against AT-081 and both stay active.** AT-081 says never run an incrementality test in a high-seasonality month. Meta says peak is the best time. Recorded as a scope split rather than a contradiction: a test whose result you want to generalise runs in a flat month, a test whose result has to justify next year's peak runs at peak and only measures peak.
- **Watchlist: the title baseline for Meta for Business News finally exists, and writing it found four unread posts on the shelf.** Every note in Watchlist.md since 2026-09-14 has prescribed a title diff and none could run one, because no title set had ever been stored. Both locales' 12 titles are now in `watchlist-seen.json`. The four previously unread posts produced AU-094, CR-261, AT-125, AT-126 and the MD-159 merge. **Same failure shape as 2026-09-20: a ceiling check answers "has the newest thing changed" and says nothing about what is already in view.**
- **The locale gap widened to eleven days.** US ceiling moved to 21 September (Agency Awards); the UK render is still at 10 September. It was a four-day gap on 20 September. A bare-URL-only read today would have called the source quiet.
- **Watchlist, the rest.** Meta Engineering 2 items, both already read on 09-22, neither about ads. Meta Newsroom 2, one the same subsea cable and one the Singapore enforcement post now merged into MD-160. Google Ads & Commerce 0 new. Google Ads Announcements **396 answer ids, 0 added, 0 removed**, fourth consecutive clean run on the set diff shipped 09-20. TikTok SDK unchanged at v0.1.8. arXiv: today's own 04:00 UTC build, 22 items, 20 new, **0 passed the ad filter**, which is the normal result. Weekly (Mon) sources not due; they were caught up on 09-22.
- **TikTok is still genuinely unmonitored** for product and policy news behind the permanent India geo-block. Not logged as clean.
- **A process defect found and fixed: the watchlist cache had not been committed since 2026-09-19.** The 09-20 and 09-22 runs ran the checker without `--commit`, so both diffed against a baseline up to four days stale and both reported cumulative "new link" counts as daily ones. Nothing was missed, because a stale baseline over-reports rather than under-reports. Today's run committed. **The check is not finished until `last_run` in `watchlist-seen.json` carries today's date.**
- **Read in full and deliberately NOT banked.** *Game Changers: Why the fastest-growing audience in sports lives across Meta technologies* (19 Aug 2026): a category and audience post with two unmethoded survey numbers, no auction, no delivery, no creative mechanic, and no client of ours in the vertical. *Open-Sourcing Rebalancer* and *Petal* on Meta Engineering: datacenter allocation and a subsea cable.
- **Gaps noticed.** (1) **Yesterday's two open items are still open**: read the Haus Black Friday report at source to upgrade AT-122 to T2, and read arXiv 2603.01590v2 (IDProxy, Xiaohongshu) in full. (2) The Cyber 5 method footnote says the window is Oct to Nov 2025 with "rates normalised to 1 October 2024 = 1", a base a year before the window; unresolved, flagged on AU-094. (3) CR-261's 7.3% has no stated comparison group, so the direction is usable and the magnitude is not. (4) The generative-AI shopping numbers in the same post (AI traffic +670% year over year, AI involved in 20% of all online orders, AI-referred shoppers 38% more likely to convert) are cited only as "Forbes, December 2025" with no study named, so they were read and not banked; worth chasing to source, because nothing else in this codex measures AI-referred commerce traffic.

"""

p = SCI / "Harvest Log.md"
t = p.read_text(encoding="utf-8")
anchor = "## 2026-09-22 (research run)"
i = t.index(anchor)
p.write_text(t[:i] + ENTRY + t[i:], encoding="utf-8")
print("Harvest Log entry prepended. em dashes:", ENTRY.count("\u2014"))

RUNLOG = """# Research run, 2026-09-23

Result: **0 transcripts in, 11 new claims, 4 merges, 0 harvest errors.** The YouTube roster was genuinely quiet. The whole day came from the Meta watchlist, on the first browser read of Meta for Business News since 2026-09-20.

## 1. YouTube harvest

`harvest.py daily` ran clean. **0 new transcripts, 0 skipped short, 1 missing subtitles, 0 errors, 12 RSS fallbacks.**

All 12 roster channels returned nothing new in window. **The 12 RSS fallbacks are not a failure and this day is not an outage.** YouTube's `feeds/videos.xml` endpoint has returned 404 or 500 for every channel since 2026-09-05; `harvest.py` falls through to the `/videos` tab via yt-dlp, which listed every channel fine and only raises if the tab returns empty. It did not.

One video could not be transcribed: **matt-shiver `r8unHVbiZg4`, published 2026-09-22, no subtitles available.** That is the only thing the roster lost today.

Unextracted backlog after the run is **0**, so the 25-a-day rule never engaged.

## 2. Watchlist

### The browser lane

`playwright` and `playwright-arcads` failed CONNECT_TIMEOUT at session start for a fourth consecutive day. **`playwright-higgsfield` connected and did every read.** It had failed yesterday, and `playwright` had been the working profile on 09-20, so the 2026-09-18 instruction to try every profile is doing real work.

**Meta for Business News, both locales, title sets read and stored:**

| Locale | Ceiling | Change since the 2026-09-20 read |
|---|---|---|
| `?locale=en_US` | **21 September 2026**, Meet the 2026 Meta Agency Award Winners | **New.** Previous ceiling 15 September |
| bare URL (renders en_GB) | 10 September 2026, Instant Hydration spotlight | Unchanged. Now **eleven days** behind the US shelf, up from four on 09-20 |

**The title baseline now exists for the first time.** Every Watchlist note since 2026-09-14 has prescribed a title diff on this source and none could run one, because no title set had ever been stored (`pages.meta-business-news` read "NOT CHECKED", `last_checked` 2026-09-17). Both locales' 12 titles are written to `cache/watchlist-seen.json` under `titles_us` and `titles_uk`. From tomorrow the diff is mechanical.

**Writing that baseline surfaced four posts sitting unread in plain view**, none of them new, and they produced most of today's haul:

| Post | Date | Outcome |
|---|---|---|
| How do advertisers increase holiday ad budgets? | card 11 Aug, **post header 13 Aug 2026** | AT-125, AT-126 |
| Cyber 5 2025: What worked, what changed and how to win Q5 | 15 Dec 2025, UK-only | AU-094, CR-261, AU-034 and CR-058 amendments |
| New Meta AI Features for Small Businesses | 19 Aug 2026 | merged into MD-159 |
| Game Changers: the fastest-growing audience in sports | 19 Aug 2026 | read in full, **deliberately not banked** |

Plus the newest card, Meet the 2026 Meta Agency Award Winners (21 Sep 2026), read in full: CR-262, CR-263, CR-264, SC-169, SC-170, LS-082, MD-165.

**This is the 2026-09-20 failure arriving a second time in a different shape.** There, a three-part series sat unread for four months because only one locale was ever read. Here, four posts sat unread because the baseline every note asked for had never been written. The common cause: **a ceiling check answers "has the newest thing changed" and says nothing about what is already on the shelf.**

**A third date artefact on this source.** "How do advertisers increase holiday ad budgets?" shows 11 August on its card and August 13, 2026 in its own post header. Two days, larger than the one-day timezone drift recorded 2026-09-14 and different in kind from the format mismatch recorded 2026-09-20. Cite the date from the post, never from the card.

### What answered without a browser

| Source | Result |
|---|---|
| Meta Engineering (RSS) | 200, 2 items. **Both already read on 09-22**, neither about ads (Rebalancer, an assignment-problem solver for datacenter and service placement; Petal, a subsea cable). Not banked. |
| Meta Newsroom (RSS) | 200, 2 items. One the same subsea cable. One the **Singapore Police Force enforcement post, 22 Sep, read in full and merged into MD-160.** |
| Google Ads & Commerce (RSS) | 200, 0 new. Feed build Fri 18 Sep. |
| Google Ads Announcements | 200. **396 answer ids, 0 added, 0 removed.** Fourth consecutive clean run on the set diff shipped 09-20. |
| TikTok SDK changelog | 200, unchanged at v0.1.8. |
| arXiv cs.IR (RSS) | 200. **Today's own 04:00 UTC build**, 22 items, 20 new, **0 passed the ad filter.** Normal result. |

Weekly (Mon) sources were not due today and were caught up on 2026-09-22.

**TikTok product and policy news remains genuinely unmonitored** behind the permanent India geo-block. Only the SDK changelog was read, so this lane is not logged as clean.

**Plain fetch answered normally on `engineering.fb.com` and `about.fb.com`**, so the Meta HTTP 400 wall recorded on 2026-09-22 is specific to `facebook.com` and `transparency.meta.com` properties rather than to Meta as a whole.

### A process defect, found and fixed

`cache/watchlist-seen.json` carried `last_run: 2026-09-19T14:37 IST`. **The 09-20 and 09-22 runs ran the checker without `--commit`**, so both diffed against a baseline up to four days stale and both reported cumulative "new link" counts as if they were daily. **Nothing was missed**, because a stale baseline over-reports rather than under-reports, and both days' logs record reading what surfaced. The cost is that neither day's counts mean what they say.

Today's run committed. Added to the Watchlist note: the check is not finished until `last_run` carries today's date.

## 3. Claims merged

**11 new, 4 merges into existing claims, 0 contested, 0 refuted.**

| ID | Topic | Tier | Claim |
|---|---|---|---|
| AU-094 | Auction | T1 | CPA falls through Cyber 5 despite rising CPMs, because conversion rate rises faster than price |
| CR-261 | Creative | T1 | An ad set carrying image + video + vertical video with audio delivered 7.3% lower CPA |
| CR-262 | Creative | T3 | Let a creator post earn an audience organically first, then amplify only the winners as Partnership Ads |
| CR-263 | Creative | T3 | Test one messaging element per round, because the winning angle is routinely the unpredicted one |
| CR-264 | Creative | T3 | Spanish creative run beside English on the same offer reached at roughly half the cost, 4x the conversations |
| SC-169 | Scaling | T3 | Dior's holiday campaigns were competing with each other; merging them returned +59% per dollar, -41% cost per sale |
| SC-170 | Scaling | T3 | Spend +99% year over year in a peak window with cost per purchase still down 9.8%, on gated 10-20% increments |
| AT-125 | Attribution | T1 | A Conversion Lift study resolves in 2-3 weeks at holiday volume against 6+ weeks in a quiet quarter |
| AT-126 | Attribution | T1 | Meta publishes fictional case studies on its business channel, disclosed only in a footnote |
| LS-082 | Learning & Signal | T3 | Server-verified in-store conversions through CAPI cut cost per high-value store visit 44% |
| MD-165 | Meta Delivery | T3 | Advantage+ Audience beat the advertiser's own audience strategy on cost, with DISQO measuring the brand half |

**Merges:** AU-034, CR-058, MD-159, MD-160.

### Tier discipline, exercised once

**Six of the eleven claims come from one source: Meta's 2026 Agency Awards post.** The entrants are agencies competing for an award, the results are agency-submitted, the judging panel is drawn from Meta and its award partners, and the winners were selected partly ON these numbers. That is survivorship selection at its maximum.

**All six are tiered T3 with the survivorship caveat written onto each claim**, rather than T1, even though Meta published them. Meta publishing a case makes it T1 for *what Meta says happened*. It does not make the mechanism a law.

The Cyber 5 aggregates are tiered **T1**, because Meta states a window and a method, with the observational limit attached on the claim: the November advertiser population is not the October population, so the median CPA fall is partly real efficiency and partly a mix shift toward brands that prepared and ramped.

### A scope split recorded rather than a contradiction

**AT-125 pulls against AT-081.** AT-081 says never run an incrementality test in a high-seasonality month, because seasonal noise swamps the effect. Meta says peak is the best time because volume resolves the test faster. Both stay `active` and neither is set to `contested`: a test whose result you want to generalise to the rest of the year runs in a flat month, and a test whose result has to justify next year's peak budget runs at peak and only measures peak.

### Two things read in full and deliberately not banked

- **Game Changers: Why the fastest-growing audience in sports lives across Meta technologies** (19 Aug 2026). A category and audience post. Two survey figures (61% of fans more drawn to individual athletes than to team loyalty, 73% of Gen Z built their fandom through social content alone) attributed only to "our consumer sports research" with no n, no method and no date. No auction, no delivery mechanic, no creative mechanic, and no client of ours in the vertical.
- **Open-Sourcing Rebalancer** and **Petal** on Meta Engineering. Datacenter resource allocation and a subsea cable. Already read and discarded on 09-22.

## 4. Skill update

**No law moved.** The hot layer in `SKILL.md` was rewritten at its opening paragraph for three things that reach it:

1. **The peak-window item flagged yesterday is now carried by three independent sources**, one of them Meta's own median advertiser rates.
2. **The AT-126 reading rule**, because this codex has banked eleven claims off Meta for Business News in three weeks and that channel mixes real and invented case studies in one format.
3. **One operating number moved**: the codex's partnership-ads advice sits at roughly 10% of budget, and Meta's own evidence for the format was generated at 20% or more of cell spend.

## 5. Errors and gaps

**Errors: 0 in the harvest, 0 in the watchlist checker.**

**One ID collision caught and corrected during the merge.** The new peak-scaling claim was first written as SC-168, which already existed. Renumbered to **SC-170** and the cross-reference in AU-094 repointed. A full duplicate scan across all 11 topic files after the fix returns zero duplicate IDs. (`MD-019` and `MD-019b` are a deliberate sub-ID pair, not a collision.)

**Gaps, carried forward:**

1. **Still open from 09-22:** read the Haus Black Friday report at source to upgrade AT-122's post-treatment figures to T2, and read arXiv 2603.01590v2 (IDProxy, Xiaohongshu) in full rather than from its abstract.
2. **The Cyber 5 method footnote does not parse.** Meta states the window as 1 Oct to 30 Nov 2025 with "rates normalised to 1 October 2024 = 1", a base a full year before the window. Flagged on AU-094, unresolved.
3. **CR-261's 7.3% has no stated comparison group.** Lower than an ad set with two of the three formats, or one? Meta does not say, so the direction is usable and the magnitude is not quotable.
4. **The generative-AI shopping figures in the Cyber 5 post were read and not banked.** AI-referred traffic +670% year over year, AI involved in 20% of all online orders, AI-referred shoppers 38% more likely to convert. Cited only as "Forbes, December 2025" with no study named. Worth chasing to source, because nothing else in this codex measures AI-referred commerce traffic at all.
"""

RUNS.mkdir(parents=True, exist_ok=True)
(RUNS / "2026-09-23-research-log.md").write_text(RUNLOG, encoding="utf-8")
print("run log written. em dashes:", RUNLOG.count("\u2014"))
