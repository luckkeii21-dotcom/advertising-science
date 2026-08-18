---
name: advertising-science
description: The living science of modern advertising, backed by a tiered claims codex in the God-level vault. Consult BEFORE and DURING any media buying decision on Meta, Google, or TikTok - planning a campaign or test, choosing structure (CBO/ABO, consolidation), scaling or cutting budget, diagnosing performance drops, setting bids or cost caps, choosing optimization events, judging creative volume needs, reading attribution, or forecasting. Also owns the daily research engine (YouTube harvest + platform watchlist) and the daily lessons for Lucky. Trigger on - advertising science, ad science, what does the science say, how does the algorithm work, Andromeda, GEM, auction mechanics, learning phase, why did performance drop, should I scale this, CBO vs ABO decision science, smart bidding internals, PMax mechanics, incrementality, MER, marketing math, run the science research, science lesson, quiz me.
---

# Advertising Science

The codex is the source of truth. On Lucky's machine it lives in the vault: `Obsidian God-level Marketing Vault/God-level Marketing/wiki/science/00-Codex.md` and its topic notes. In the team package (repo `EverythingAI-Pro/advertising-science`) the same codex ships as `references/codex/`, refreshed by the daily research run; if the vault path does not exist on this machine, read `references/codex/` instead. This skill is the protocol for using and growing it.

## Evidence tiers (the spine of everything)

- **T1**: platform docs or engineering publications. How the machine is built.
- **T2**: a real test with shown data. Ours beat everyone else's.
- **T3**: practitioner claim from real spend, no shown test. Strong hypothesis, never a law.
- **T4**: theory. An idea, nothing more.

Statuses: `active`, `contested` (disagreeing credible sources, both recorded), `superseded`, `refuted` (kept forever so we never relearn it).

## Using the science (every ad decision)

1. Name the decision (scale, cut, structure, bid, creative volume, diagnosis, forecast).
2. Read the relevant topic note(s) from the codex. Meta delivery, Auction, Learning & Signal, Creative, Scaling, Attribution, Google Auction, PMax, TikTok, Marketing Math.
3. Apply claims by tier: T1/T2 can decide. T3 informs but a T3-only decision must be named as a bet, not a law. T4 never decides.
4. If codex claims conflict with a client's own account data, the account wins and the conflict gets recorded in the codex as a contested claim.
5. If the decision would make a good test, say so: every T3 we test on our own accounts becomes a T2 with our numbers. That upgrade path is the whole point.
6. If the codex is silent on the question, say "the codex is silent here", decide on judgment, and log the gap in the Harvest Log so research targets it.

## Growing the science (claim merge protocol)

New information (transcript, doc, update) is decomposed into claims. For each claim:

- **Matches an existing claim**: add the source and date to it. Never create a duplicate.
- **Contradicts an existing claim**: set status `contested`, record both sides with sources. A T1/T2 contradiction of a T3 claim supersedes it instead.
- **New**: next free ID in its topic (`MD-`, `AU-`, `LS-`, `CR-`, `SC-`, `AT-`, `GA-`, `GP-`, `TT-`, `MM-`), tier it honestly, date it.
- **Fluff** (motivation, repetition of banked claims, pure promotion): discard silently. We bank claims, not videos.

A claim entry looks like:

```
### MD-001 · Creative is the primary targeting input post-Andromeda
Tier: T1 · Status: active
Meta's multi-stage retrieval system selects candidate ads by predicted
per-user relevance of the creative itself; audience settings mostly bound
the candidate pool.
Sources: Meta engineering blog (Andromeda post); BlueSense 2026-07-28; Charley T.
Last touched: 2026-08-18
```

## The engine (automation this skill owns)

- **Daily Research run, 07:00 IST** (Windows task `EvAI-AdScience-Research`): executes `RUNBOOK-RESEARCH.md`. Harvests roster uploads (`lib/harvest.py`), checks the watchlist, extracts and merges claims, updates this skill if a law changed, one line in the Harvest Log. Quiet day = one line, stop.
- **Daily Teacher run, 08:00 IST** (`EvAI-AdScience-Teacher`): executes `RUNBOOK-TEACHER.md`. Daily lesson + 5-question quiz for Lucky in `wiki/science/lessons/`; lesson video Mon/Wed/Fri; grades pending quiz answers.
- Roster: `channels.json` (mirror table: vault `wiki/science/Channel Roster.md`). Watchlist: vault `wiki/science/Watchlist.md`.
- Manual runs: "run the science research" / "run the science teacher", or `bin/Run-ScienceResearch.ps1` / `bin/Run-ScienceTeacher.ps1`.

## Current laws (hot layer)

Updated only when the codex changes at law level. Each law cites its claims; depth lives in the codex. Last rebuilt: 2026-08-19 from 747 claims (49 T1, 59 T2, 542 T3, 97 T4, 54 contested, 5 superseded).

**Meta delivery and creative**

1. **Creative is the targeting.** Meta reads the creative content itself at the retrieval stage (T1 architecture, MD-022/MD-025); the avatar or scenario named in the ad decides who sees it (MD-001, T3). Verified case: niching one product's creative to one avatar halved cost per purchase, $73 to $35 at equal spend (CR-005, T2). Settings only set boundaries: location, minimum age, language, exclusions.
2. **Near-duplicate ads collapse into one entity ID** with zero unique reach; diversity must live at the concept level (angle x offer x persona), and a format change (static to video) escapes the collapse (MD-003, T3).
3. **Do not run the doom cycle. The top-spender half of this law is now openly contested and must be spoken as a bet.** The original position: the top-spending "worst CPA" ad is usually the TOF engine, killing it can crater the ad set, and churn-killing ads into replacements is the most-cited reason accounts stop scaling (MD-010 T3, SC-012 T2). Against it, Charley T says kill the budget hog so the others can spend. Faris, across 100+ accounts, says leave high spenders on in 99%+ of cases and reports roughly 30% more spend at the same target just by switching a previous buyer's paused high spenders back on (SC-085, contested, neither side shows data; SC-008 flipped to contested). What survives on both sides: killing LOW spenders is always safe, and judge at ad-set level. Settle it on our own accounts, the test is cheap and reversible: kill the top spender for 2 to 3 days and read ACCOUNT-level cost per result, not the ad's own row. Counterweight still on file: CTC's back-test found manual on/off decisions had no measurable impact at all (both T2).
4. **Relevance is a bid.** A more relevant ad wins auctions against higher bidders (AU-002, T1). Creative quality is the cheapest CPM lever we have.

4a. **How many ads to run live has no agreed answer. Never quote a number as settled.** Charley T's own figure moves across four months (4-6 in Dec, 3-4 in Jan, 3-5 in Feb, 5-8 in Apr), against Ben Heath at 20 per ad set, Jeremy Haynes at 75-90, and a Blue Sense account that went 15 to 60 live ads and cut CAC 20-30% (CR-154, contested). Related and also contested: whether replicating proven winners is the top allocation bucket at 50-60% of output, or the most common cause of new ads getting zero delivery because they read as knockoffs of the incumbents (CR-033). Both are settleable in one week on our own accounts.

4b. **The hook is not a substitute for a new argument.** The hook-is-80%-of-performance rule now has a named ceiling: hook swaps are near-free and should be exhausted before an asset is retired, and they stop working where the message itself is the limit (CR-124, contested). Haynes films 25-30 separate arguments rather than hook variants. Nobody has run the comparison.

**Learning and signal**

5. **Never significant-edit a working ad set.** Targeting, creative, optimization event, bid strategy, adding an ad, or a 7-day pause always reset learning; budget moves reset it only when large, Meta's own example being $100 to $1,000 (LS-002/LS-003, T1). An ad set needs ~50 optimization events in the week after its last significant edit to exit learning (LS-001, T1).
6. **The results column IS the targeting.** Meta finds more people like whoever fired the optimization event, so feed it only qualified conversions (LS-008, T3). The live trade-off between event volume and signal quality is contested; say which side you are betting on.

**Scaling**

7. **Budget step size is folklore territory.** Prescriptions run from 5% to 20%/day to "raise freely"; nobody has controlled data (SC-001, T3, contested). A ROAS dip after a raise is upper-funnel time lag, wait before rebuilding (SC-002, T3).
8. **Minimum viable daily budget is 1x target cost per result** per day; three roster operators converged on this independently (MM-019, T3).

8a. **A cost cap has no AOV term, so never mix price bands inside one capped ad set.** At a $50 cap a $50 AOV product returns 1.0 ROAS and a $100 AOV product returns 2.0 ($80 gives 1.6, $90 gives 1.8), and Meta drains the budget onto the cheapest SKU because a 1.0 ROAS conversion is the easiest to buy (AU-040, T3). Shown on a live account: a sitewide markdown pulled capped spend onto a $46 AOV product, and the fix was off-platform, raise the price and re-merchandise the collection page (AU-045, T2). **Operating consequence for us: a client price change or promo calendar IS a delivery change. We have to see it before it ships.**

8b. **Accumulated learning lives in the ad account, not the pixel.** A fresh ad account starts from zero even on the same pixel (SC-094, T3). So client ad accounts get created under the CLIENT's Business Manager with partner access to us, never the reverse. Getting this backwards throws away the asset when the relationship changes.

**Attribution**

9. **Turn view-through attribution off and audit for it**; rebuild any ad set where view-through exceeds ~10% of conversions (AT-012, T2). Click-based platform reporting underreports true contribution only 10-20% in lift tests (AT-008, **downgraded T2 to T3 on 2026-08-19**: both sources are the same speaker citing Haus and CTC meta-analyses from memory, studies never shown). House rule stands: never call spend "wasted" from a last-click zero. Contested scale: one auditor finds 1-day view running 30-50% of reported ROAS as the norm, which would make the 10% threshold a healthy exception rather than a typical account (AT-037, T3). AT-037 also now carries the delivery half: the 7-day-click plus 1-day-view setting biases DELIVERY toward view-through, not only the report, so roughly 90% of accounts overspend on existing customers and the fix is two-sided.

9a. **The incrementality benchmarks expired.** True incremental sits near 28-day click, or roughly 7-day click times 110-115% (AT-008, T3). That multiplier was derived on the OLD wider 7-day-click column, so applying it after the March 2026 outbound-click-only redefinition understates true incremental by whatever share the engagement clicks carried (AT-008 cross-referenced to AT-036). Never quote it against post-March-2026 data as current.
10. **Meta redefined 7-day click around March-April 2026** to require an outbound click, moving likes, comments, shares and page clicks into a new 1-day engaged view bucket, so 7-day-click ROAS fell overnight with no change in real performance (AT-036, T3; delivery-side half at AU-017). **Reporting consequence, and it is a client-facing one:** a step-down in 7-day-click ROAS dated to that window is a definitional artefact and must never be written up as a performance decline.
11. **Incremental attribution is not a holdout on your account.** It applies a factor derived from conversion-lift experiments run by other advertisers in your niche (AT-035, T3, and MD-034). Treat it as directional evidence about your category, never quote it to a client as a measured lift. It still beats standard attribution on the T2 evidence (AT-001 to AT-004).
11a. **Period-end reports read the most incomplete days as final.** Conversions keep landing after a window closes, so the newest days in any report are still filling in. Every week-over-week and month-over-month comparison therefore structurally flatters the EARLIER window. Cut the same tail off both windows or state the uncertainty (AT-068, T3). At low conversion counts a zero-conversion day is baseline variance, not a finding (AT-031). And never write "Meta broke" or "platform issue" without the spend-spike-at-strange-CPM signature; it is the least likely explanation and the only one with no plan attached (AT-066).

12. **Prune before you launch.** In a shown 89-ad campaign the winning ads and the losing ads consumed the same budget, $48,594 against $48,800, while the losers ran a $230 CPA and a negative $0.98 gross profit per transaction (MD-046, T2). Cutting that campaign from 89 ads to 4 and launching nothing new for six weeks 10x'd spend in 90 days, with weekly gross profit per transaction holding at 136/133/137/124 even as platform ROAS fell below 2 (SC-050, T2). This does not license killing top spenders, which law 3 still forbids; it licenses removing the long tail that is losing money per transaction.

**Google**

13. **Quality Score is a diagnostic, not an auction input**; auction-time quality is computed fresh per auction (GA-010, T1).
14. **Under tCPA, bid adjustments move the CPA target itself**: +40% mobile on a $10 tCPA means a $14 mobile target; -100% excludes the device (GA-004, T1).
15. **Exact match beats PMax for a matching query; search themes only tie with phrase/broad** (GP-001, T1). PMax audience signals are suggestions, never constraints for the whole campaign life, and after ~30 days of conversion data Google bypasses them entirely so tweaking them on a mature account is a non-intervention (GP-004, T1 core with a T3 practitioner boundary).
16. **PMax over-reports and standard shopping under-reports.** 50%+ of PMax conversions are repeat or warm customers it did not acquire, so a PMax ramp can hold reported ROAS flat while adding no backend revenue, and the standard shopping campaign doing the cold acquisition loses the credit (GP-005/GP-006, T3). Run brand exclusions or PMax is a retargeting campaign (GP-009, T3). The reading signal: a WIDENING gap between Google-reported and backend revenue is the ceiling indicator and triggers a structural audit, not a bidding tweak (AT-062). **Now contested where the ceiling sits:** GP-006 puts it near $15-20k/month, GP-028 puts it anywhere from $3k to $100k/month depending on the business, neither with data. Stop planning against $15-20k as a fixed number.

16a. **A share of Google spend is now unmeasurable.** As of Dec 2025, broad match, shopping feeds, PMax and AI Max can already serve inside AI Overviews and AI Mode with no off switch and no reporting breakout (GA-043, T3). Every "where the Google budget went" statement we make to a client inherits that unknown, so say so rather than implying full visibility.
17. **Raising target ROAS is an audience-temperature dial, not an efficiency dial.** Each increase shrinks the bid pool and cuts cold audiences first, so reported efficiency rises while new-customer acquisition falls (GA-019, T3). Missing target then starts a self-reinforcing spiral that requires an aggressive cut to escape, not an incremental one (GA-020, T3).

**TikTok**

18. **3-5 ad groups per account, 3-5 genuinely different creatives per ad group; learning settles after ~25 results or 7 days; refresh into the EXISTING ad group** (TT-002/TT-003/TT-004, T1).
19. **TikTok incrementality is category-dependent and creative-supply-gated.** 4 of 5 fashion lift tests came back strongly positive while 4 of 4 inverse holdouts outside fashion showed none, and those clients were pulled off the platform. The real decider is whether the brand runs a genuine native organic TikTok operation, because TikTok creative fatigues very fast (TT-017, T3).

**Economics**

20. **Gross margin sets the ROAS breakeven** (87 points of margin is profitable at 1.3x; 50-60 points needs ~2.0x); fix margin before blaming ads (MM-010, T3). LTGP:CAC of 2-3 is the scale zone (MM-002, T3, now contested on whether the ratio uses gross profit or revenue in the numerator, so state which before acting).
21. **Discounting raises required ROAS exponentially while breakeven rises only linearly**, so the gap between a 15% and a 25% discount can be the gap between an achievable target and an impossible one; model it before publishing the offer (MM-085 to MM-092, T4 worked models).

**Meta-rule**

22. **Decide on tiers.** No decision gets justified with a T3/T4 claim spoken as a law. Say the tier out loud. When our own account data contradicts the codex, the account wins and the codex gets a contested entry.

## Current watch items (timely, expire when resolved)

- **Aug 2026 in-place budget-raise bug (Meta):** raising budget in place on a winning campaign dropped results to zero or -90% across many of Ben Heath's 1,400+ managed accounts; workaround is duplicate-at-new-budget then kill the original. Contradicts the normal in-place-beats-duplicate rule, verify per account. (T3, banked 2026-08-18)
- **Meta instant forms now embed calendar booking** (Calendly/GHL live, HubSpot early Aug, global Oct). Our delivery stack law says the VOICE AGENT owns booking, never the form. Flag to Lucky before any client adopts this; it changes the qualification funnel, and contact info is captured even on abandoned bookings.
- **RESOLVABLE BY DOCS, so resolve it:** does defining new/engaged/existing audience segments actually let Meta allocate budget across them, or is it a reporting lens only? Ben Heath says the former, Charley T says the definitions never reach the delivery model (MD-019, contested, neither shows evidence). Meta's help documentation settles this outright. Until then treat the reported split as reliable and the allocation benefit as unverified. Watchlist target.
- **Meta has announced a ROAS guardrail on cost-cap campaigns.** If it ships it retires most of the manual AU-040/041/043/045 cap work above. Review when it lands (AU-042).
- **AI Max returned no benefit** across a large agency's ongoing testing, with testing referenced and zero numbers shown (GA-047). It is an unquantified read on a product under active development, so never quote it to anyone as a null result.

## Writing rules for everything this skill produces

No em dashes. No contrast negating. Short sentences, numbers over adjectives, honesty rules from the client-reporting law apply to lessons and logs too.
