"""Prepend the 2026-09-25 research entry to the Harvest Log."""
from pathlib import Path

LOG = Path(r"E:\claude code marketing skill\Obsidian God-level Marketing Vault"
           r"\God-level Marketing\wiki\science\Harvest Log.md")

ANCHOR = ("One line per Research run: what came in, what changed. Quiet days get one line "
          "and nothing else.")

ENTRY = """
## 2026-09-25 (research run)

**0 transcripts in, 4 new claims, 1 merge, 0 contested, 0 refuted, 0 harvest errors, 0 watchlist errors.** The YouTube roster returned **zero** new videos across all 12 channels, the first all-zero harvest this engine has recorded. The entire day came out of one Google blog post, and that post turned out to be an instalment of a monthly series this codex did not know existed.

### 1. YouTube harvest

`harvest.py daily` ran clean and returned nothing. **0 new transcripts, 6 skipped short, 0 missing subtitles, 0 out of window, 0 errors, 0 RSS fallbacks.** Every one of the 12 roster channels returned 0.

This is not a fault. Twelve channels each publishing a few times a week will land an empty day eventually, and the run completed normally on every one. The RSS fallback count stayed at 0 for the second consecutive day after 19 days at 12, so YouTube's `feeds/videos.xml` endpoint is still behaving. Still recorded as an observation and not a fix: nothing in our code changed.

Unextracted backlog after the run: **0**.

### 2. Watchlist

**Browser: `playwright` and `playwright-arcads` both failed CONNECT_TIMEOUT at session start for a sixth consecutive day. `playwright-higgsfield` connected and did both Meta reads.** The 2026-09-18 instruction to try every profile is still the thing that keeps this lane alive.

**Meta for Business News, both locales, mechanical title diff, second clean run since the baseline was written.**

| Locale | Ceiling | Result |
|---|---|---|
| `?locale=en_US` | 21 September 2026, Meta Agency Awards | **12 titles, same set as cache. 0 new, 0 removed** |
| bare URL (renders en_GB) | 10 September 2026, Instant Hydration | **12 titles, same set as cache. 0 new, 0 removed.** Now **fifteen** days behind the US shelf |

The UK-to-US gap has gone 4 days (09-20), 11 days (09-23), 12 days (09-24), 15 days today. It is widening monotonically because the UK shelf has not moved since 10 September while the US shelf has moved twice. A run reading only the bare URL would have called this source quiet for five days running.

One minor date observation, logged and not chased: the UK card for *Cyber 5 2025* renders **17 December 2025** today, where the 2026-09-23 entry recorded 15 December. The post was not re-opened to resolve which is which. This source has three documented date artefacts already and the standing rule is to cite the date from the post, never the card.

| Source | Result |
|---|---|
| Meta Engineering (RSS) | 200, build 24 Sep 00:02 UTC. **0 new** |
| Meta Newsroom (RSS) | 200, build 24 Sep 21:16 UTC. **1 new: "The Biggest News From Connect 2026".** Read in full for ad content. **None.** Muse, VR glasses, Ray-Ban Gen 3, hearing enhancement. Deliberately not banked |
| Meta for Business News | Both locales read via browser. 0 new |
| Google Ads & Commerce (RSS) | 200, build 24 Sep 16:00 UTC. **1 new, and it carried the whole day.** See below |
| Google Ads Announcements | 200. **396 answer ids, 0 added, 0 removed.** Set diff, per the 2026-09-20 method |
| arXiv cs.IR | 200, build **Fri 25 Sep 04:00 UTC**, today's own build. 37 in feed, 35 new, **3 passed the ad filter, 1 genuine** |
| TikTok SDK changelog | 200, **unchanged at v0.1.8**. TikTok blog and Newsroom remain India geo-blocked and genuinely unmonitored |

Weekly (Mon) sources not due: today is Friday. The 2026-09-22 catch-up rule did not need to fire; the most recent Monday lane ran as catch-up on Tuesday 2026-09-22 as recorded.

**Cache committed.** `watchlist-seen.json` carries `last_run: 2026-09-25T16:50 IST`, per the verification the 2026-09-23 entry added to step 2.

**One thing from the Connect post, read and not banked, noted so it is not re-read.** Hearing enhancement is priced at $149.99 or is included "via Meta One subscription". Meta One therefore also exists as a CONSUMER subscription bundling a paid hardware feature, which is a different product from the business plans at MD-157 and the link caps at MD-166. It changes no ad decision.

### 3. The Google lane, and what it cost to read properly

**One post in the feed. Reading it at source, following its footnote, and following its links produced four claims and three watchlist findings.**

| Claim | What it is |
|---|---|
| **GA-081** | September 2026 Demand Gen drop: one-click on Shorts and Gmail, a Business Agent waitlist, affiliate-location Promoted pins, and the anatomy of its 40% figure |
| **GA-082** | A Gmail click counts the same whether it opened the ad or opened your site, so the one-click switch changes what the metric means while the metric keeps its name |
| **GA-083** | The May 2026 drop is where Maps inventory and automotive product feeds actually landed, and it shipped two counterfactual instruments for Demand Gen |
| **GA-084** | The July 2026 drop says in Google's own copy that Demand Gen tROAS had been "overly cautious early on" |

Merge: **GA-068** gains a forward note establishing that it is one instalment of a monthly series.

**The most actionable finding, GA-082.** Google's help centre states that a Gmail click is counted from the teaser tap "whether the click expands the ad body or navigates directly to the advertiser's site". The September drop moves Gmail image ads from two-click to one-click. **One counter, two different actions.** Before, a Gmail click meant the ad opened. After, it means a person reached the landing page. Any before-and-after read of Gmail clicks, CTR or cost per click across this boundary compares an expand against a site visit. Judge it on conversions and cost per conversion. Stated limit: the help article is written for Display, the change lands in Demand Gen, and Google does not restate the rule on the Demand Gen page.

**The vendor-figure pattern is now at five instances and the footnote is where each one breaks.** Today's 40% is footnoted "Google Internal Data, Global, Gmail Ads, February 2026". It measures adding Gmail as a channel, not the one-click update it sits under; the window is seven months before the feature shipped; and "at the same ROI" makes it a volume statement at constant efficiency. May's 33% product-feed figure publishes its own survivorship filter: campaigns active since Q1 2024 with over 50 products. July's 94% is an Ipsos survey whose sampling frame is people who already used YouTube to shop.

**Checked at source and left open.** The affiliate-location half of the September drop names "dealerships", which will read as an SJR Commercial and Phoenix Truxx opportunity. The help article Google links for it contains the word "affiliate" **zero times**. No eligibility rule is published, so the fit is unverified rather than available. What that page does establish as T1: Promoted pins are supported in Demand Gen, require a linked Google Business Profile, and you cannot serve ads exclusively in Maps.

### 4. Gaps noticed

- **Eight Demand Gen Drops remain unread**, October 2025 through June 2026, plus the introduction post. Reading two of the ten today re-dated two things the September announcement appeared to introduce, so the backlog is load-bearing rather than archival. Queued with the extraction method in Watchlist.md.
- **This is the third instance of the same failure shape**, after Meta for Business News on 2026-09-20 and 2026-09-23. A source can be watched daily and still have a year of instalments behind it, because a ceiling check answers "has the newest thing changed" and says nothing about the shelf.
- **The Google Ads Announcements page is not a superset of Google ads product news.** Its 396-id set was stable at 0 added and 0 removed on the same day Google shipped a monthly product drop.
- **The arXiv filter fix has three supporting observations and zero counter-examples** and is still only an instruction. Both of today's false positives would be killed by discounting a single bank-list hit confined to the first or last sentence.
- **TikTok remains unmonitored** for policy and creative. Only the SDK changelog answers, and it ships endpoint names.
"""


def main():
    text = LOG.read_text(encoding="utf-8")
    if "## 2026-09-25 (research run)" in text:
        raise SystemExit("2026-09-25 entry already present")
    i = text.index(ANCHOR) + len(ANCHOR)
    out = text[:i] + "\n" + ENTRY + text[i:]
    LOG.write_text(out, encoding="utf-8")
    print("Harvest Log %d -> %d chars" % (len(text), len(out)))


if __name__ == "__main__":
    main()
