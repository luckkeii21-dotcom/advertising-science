# -*- coding: utf-8 -*-
"""Harvest Log + Watchlist entries for the 2026-09-22 research pass."""
import io
import os

SCI = os.path.join(
    r"E:\claude code marketing skill",
    "Obsidian God-level Marketing Vault", "God-level Marketing", "wiki", "science")

ENTRY = u"""## 2026-09-22 (research run)

- **4 transcripts in, 0 harvest errors, 22 new claims and 9 merges.** The biggest single-source day in a while: a 55-minute, 11,953-word agency strategy deck with portfolio data pulled from the Meta MCP, plus three practitioner videos. Backlog after the run is 0.
- **The finding: Pareto does not hold in a peak-spend window, and the codex had the opposite banked as settled.** [[Scaling Models#SC-163|SC-163]], from an estimated $50 to $100 million of Black Friday spend: top single ad 7% of spend, top 20 ads 46%, **bottom 80% of ads 54%**, and concentration FALLS as accounts get bigger (53% held by the top 20% of ads under $250k November spend, then 44%, then 33%). Banked as a boundary on [[Scaling Models#SC-058|SC-058]] rather than a refutation, because the reconciliation is probably arithmetic: an ad has a daily spend ceiling, so overflow goes to the tail. **The test that would settle it is one account measured across both windows and nobody has run it.**
- **New claims (22).** Scaling: SC-163 Pareto break, SC-164 elasticity is a cut instrument only, SC-165 fund the pre-season at 31 to 43% of the Sep-Dec budget, SC-166 cost caps as a measurement instrument, SC-167 dead weight priced at 52 of 60 ad sets spending with zero sales. Creative: CR-255 volume from peak daily spend over per-ad capacity, CR-256 offer creative buys spend capacity not conversion, CR-257 creative as a CPM lever, CR-258 the offer corrupts the creative feedback loop, CR-259 concepts not visuals, CR-260 never turn evergreen off. Auction: AU-092 the cheap 2025 auction was bought with inventory expansion, AU-093 peak saturation is mild at 1.96 frequency. Attribution: AT-122 the 1-day to 30-day gap doubles in November, AT-123 incremental attribution as a scaling instrument, AT-124 the hourly pacing lag. Marketing math: MM-222 the marginal-CAC worked example, MM-223 revenue floor and profit volume, MM-224 the Wilson lower bound on repeat rate. Meta delivery: MD-163 the cost of daily on-off churn, MD-164 sales-mix homeostasis (T4). Google: GA-079 Google is a preparation platform in the peak.
- **Merges (9), no new IDs:** MM-204 (a third instance, and the first with a NULL result: 2 of 10 brands showed no November cohort penalty at all), AU-034 (Q5 confirmed, plus the claim that CPMs track expected action rate so succeeding in the cheap window raises its price), AT-039, LS-051 (the hero-product custom conversion mechanics plus subscription and high-ticket extensions), MM-214 (a second operator's target ladder and a 20 to 30% first-order take ceiling), SC-154 (a second full-year one-CBO instance: 193 ad sets, $5M in sales), CR-185, MD-008, SC-058.
- **Tier discipline exercised twice, both worth recording.** The Haus incrementality figures in AT-122 (105% post-treatment lift for experiments ending 3+ weeks out, 41% of incremental value after the treatment window, fashion 93% against CPG 30%) are real geo-holdout experiments and **would be T2 if read at source. They are banked at T3 because the primary was not read.** And MD-164 was banked at **T4 rather than T3** because its 13%, 25% and 50% thresholds have no source; the line beside it that CPMs fall because Meta recognises a quality signal provider has no support of any kind and is flagged not to be repeated.
- **A live disagreement inside one day's harvest, recorded and not resolved.** MD-163 says continuous ad turn-off destroys the sequencing signal and manufactures the volatility operators blame on Meta. SC-167 prices the opposite policy on a real takeover at about $6,000 a month of spend with zero sales. The distinction is probably which ads get cut. Neither operator has tested the other's policy.
- **Watchlist: the entire Meta lane went unchecked today and it should not be logged as clean.** Plain fetch returned HTTP 400 on Meta for Business News (both locales), the Marketing API changelog, the Graph API changelog, Advertising Standards (both locales) and the AI at Meta blog, and **all four Playwright MCP profiles failed to connect at session start** (`playwright`, `playwright-arcads`, `playwright-higgsfield`, `playwright-metatech`). There was no browser available at any point in the run.
- **Watchlist, what did answer.** Meta Engineering 2 new posts, both read, neither about ads (Rebalancer assignment-problem library, Petal subsea cable). Meta Newsroom 1 new, the same subsea cable. Google Ads & Commerce 0 new. Google Ads Announcements 396 answer ids, 0 added, 0 removed, the set-diff method working as intended for the third consecutive run. TikTok SDK changelog unchanged at v0.1.8; TikTok product and policy news remains genuinely unmonitored behind the India geo-block, and the browser outage meant no alternative route was even available. arXiv cs.IR read Tuesday's own 04:00 UTC build, 55 items, 50 new, 2 passed the ad filter and **both were read and neither was banked**: the Netflix counterfactual observability paper (2609.22747) is organic recsys and fired on `incrementality`, and IDProxy (2603.01590v2) is a real advertising-adjacent system that is logged as a gap below rather than banked from an abstract.
- **arXiv filter: `incrementality` is the third false-positive term**, after `CTR prediction` (2026-08-26) and `sponsored` (2026-09-07). The Netflix paper uses it as a genuine method word for a recommender, not as framing, so the existing "discount a single hit confined to the first or last sentence" proposal would NOT have caught it. Any tightening needs a second rule: a bank-list hit applied to an organic recommender is not an advertising hit.
- **Monday weekly lane caught up, because yesterday's run never happened.** The 2026-09-21 research run died with `API Error: Can't reach the API server (ENOTFOUND)` and the watchdog stood down after one relaunch, so Monday's weekly sources were never read. Checked today: Google Ads API release notes newest still **v25.1 (2026-08-19)**, no change since 2026-09-07. Google Ads Developer Blog, **one new post since 2026-09-02**, "A new onboarding experience for Google Ads API developers" (2026-09-10); the post-body regex recorded in Watchlist.md did not match on this permalink and **the body was not read**, so it is neither banked nor dismissed. Merchant Center announcements rendered a newest dated entry of **15 July 2026** against the **11 August 2026** recorded from the 2026-09-07 WebFetch check; that is a transport render difference of the same class as the Marketing API index artefact, **not a rollback**, and nothing dated after 11 August appeared by either route. Its one forward-looking line, "Changes beginning September 30, 2026", sits inside the 28 April 2026 pickup-cost post for the UK, Switzerland and EEA and is not new. The Meta half of the weekly lane is still unread, now going on two weeks.
- **Gaps noticed.** (1) **Read the Haus Black Friday report at source** and upgrade AT-122's post-treatment figures to T2; it is the single highest-value open item today. (2) **Read arXiv 2603.01590v2 (IDProxy, Xiaohongshu) in full**: it is a production CTR-prediction system using multimodal LLM embeddings to solve item cold start, deployed in Content Feed **and Display Ads**, and it is directly on-topic for [[Creative Science#CR-003|CR-003]] and the Andromeda cold-start thesis. It was not banked today because an abstract is not a read. (3) The Motion offer-creative figure behind CR-256 is quoted from a report not read here. (4) Meta for Business News has now gone unread for two consecutive daily runs and the locale-partition rule found on 2026-09-20 has never been exercised.
"""

WATCH = u"""
### Zero-browser day: the whole Meta lane is unreadable when no Playwright profile connects (2026-09-22)

Every note above assumes a browser can be found if enough profiles are tried. On 2026-09-22 none could, and the consequence is larger than a single missed source because **Meta serves HTTP 400 to plain fetch on every property this watchlist tracks.**

Observed, all in one run, plain HTTPS with a normal desktop user agent:

| Source | Result |
|---|---|
| Meta for Business News, bare URL | HTTP 400, 1,542-byte error body |
| Meta for Business News, `?locale=en_US` | HTTP 400, identical 1,542 bytes |
| Marketing API changelog | HTTP 400 |
| Graph API changelog | HTTP 400 |
| Advertising Standards, `/policies/ad-standards/` | HTTP 400 |
| Advertising Standards, `/en-gb/policies/ad-standards/` | HTTP 400 |
| AI at Meta blog | HTTP 400 |

All four configured Playwright MCP profiles failed at session start: `playwright`, `playwright-arcads`, `playwright-higgsfield` and `playwright-metatech`, all CONNECT_TIMEOUT at 30s. The 2026-09-18 instruction to try every profile before logging a source unchecked was followed and there was nothing left to try.

**The honest phrasing for a run log on a day like this is "the Meta lane was not checked", never "no Meta changes".** The distinction matters because the locale-partition finding of 2026-09-20 exists precisely because a source can look quiet while a catalogue behind it has moved.

**Non-Meta sources are unaffected.** Every Google source, the arXiv feed and the TikTok SDK changelog all answered a plain fetch normally in the same run, so a zero-browser day is a Meta-lane outage and not a network fault.

### Google weekly lane: a Monday failure silently costs a whole week (2026-09-22)

The 2026-09-21 research run exited on `API Error: Can't reach the API server (ENOTFOUND)` and the watchdog relaunched once, then stood down for the rest of the day. Monday is the only day the weekly sources are read, so the failure took the whole weekly lane with it and nothing recorded that it had.

Caught and run as catch-up on the Tuesday. **Add to the runbook's reading of "Weekly (Mon) sources: only on Mondays": if the previous Monday's run did not complete, run them on the next day that does.** The cheapest check is `runs/<yesterday>/research-claude.log` and the presence of a `<date>-research-log.md`.

**Merchant Center renders differently by transport, and the difference looks like a rollback.** A plain fetch on 2026-09-22 showed a newest dated entry of 15 July 2026; the 2026-09-07 WebFetch check recorded 11 August 2026. Same page, two transports, and the older-looking result is the artefact. This is the same class as the Marketing API changelog index under-rendering to v25.0. **Never report a newest-entry date going backwards as news; re-read on the other transport first.**

**The Developer Blog post-body regex is not universal.** The urllib plus `post-body` div route recorded on 2026-09-07 returned nothing on the 2026-09-10 permalink `new-onboarding-experience-for-google-ads-api.html`, so that post's body has not been read. The index and the Atom feed both render its title and date fine.
"""


def main():
    p = os.path.join(SCI, "Harvest Log.md")
    t = io.open(p, encoding="utf-8").read()
    anchor = "## 2026-09-22 (teacher run;"
    i = t.index(anchor)
    t = t[:i] + ENTRY.strip() + "\n\n" + t[i:]
    io.open(p, "w", encoding="utf-8").write(t)
    print("Harvest Log entry inserted above the teacher entry")

    p = os.path.join(SCI, "Watchlist.md")
    t = io.open(p, encoding="utf-8").read().rstrip() + "\n\n" + WATCH.strip() + "\n"
    io.open(p, "w", encoding="utf-8").write(t)
    print("Watchlist notes appended")


if __name__ == "__main__":
    main()
