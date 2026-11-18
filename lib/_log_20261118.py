# -*- coding: utf-8 -*-
"""Harvest Log entry for 2026-11-18."""
from pathlib import Path
import shutil

LOG = Path(r"E:\claude code marketing skill\Obsidian God-level Marketing Vault\God-level Marketing"
           r"\wiki\science\Harvest Log.md")

ENTRY = u"""## 2026-11-18 (Wednesday) - 1 transcript in - 1 claim added, 3 amended, 0 contested, 0 laws amended

**A new Meta ad product was read off the live screen for the first time, and it is a pair of products rather than the one we had banked. 1 claim added, [[Meta Delivery & Andromeda#MD-201|MD-201]], T1. 3 amended: [[Auction Mechanics & Bidding#AU-032|AU-032]], where the author of the claim now argues against his own mechanism, [[Meta Delivery & Andromeda#MD-181|MD-181]], and [[Learning & Signal#LS-076|LS-076]] on its fourth Muse re-check. No law changed.**

**Harvest: 1 new transcript, 1 error.** 11 of 12 roster channels listed clean. `nick-theriot` listing failed with HTTP 404, first failure on that channel in this run series, worth one more day before treating it as a dead handle. 8 uploads skipped as too short, 2 with no subtitles, 0 out of window. The one that came through: Ben Heath, *Facebook Ads Super Burst Just Launched!*, 2026-11-17, 19 min, 4,383 words, a screen walkthrough of the live product inside his own UK ad account. Read in full. Unextracted backlog is now 0.

**Banked [[Meta Delivery & Andromeda#MD-201|MD-201]], T1: the Ads Super Burst configuration surface.** [[Meta Delivery & Andromeda#MD-181|MD-181]] already held the October announcement, which was United States only and published nothing but brand lift. This is the product itself, and five things in it are new to the codex.

1. **It is two products, not one.** The picker inside Reach Planner offers Ads Burst, "sustained reach over two to five days", alongside Ads Super Burst, "concentrated reach in three to 24 hours". Ads Burst appears nowhere else in this codex.
2. **Choosing it locks four delivery controls at once**, all greyed out: buying type reservation, performance goal reach, placements fixed to Facebook and Instagram Feed, Stories and Reels, and frequency fixed at one impression per person. Broad targeting in one country or region only, no detailed targeting and no custom audiences, sub-region exclusions allowed, age bands and gender still editable, duration a menu of 3, 6, 12 or 24 hours defaulting to 6.
3. **Gender still works here while it is being withdrawn from auction ad sets** ([[Meta Delivery & Andromeda#MD-196|MD-196]]). Two surfaces, two rules, same account.
4. **The forecast prices by hour and by day, and the swing is large.** Same UK geography and same 6-hour length: addressable audience 14.9 million for midnight to 06:00 against 33.3 million for 07:00 to 13:00, and the tool defaults to the worse of the two by a factor of 2.2. Day tiers are labelled standard, elevated and peak, measured at GBP 6.00 CPM on a peak day against GBP 4.50 on the Friday nine days earlier. **So a reservation price is a forecast, not a rate card, and the saving sits in the date.**
5. **Meta's own suggested budget for one 6-hour UK flight was GBP 33,010.67**, and the planning method can be flipped from a budget input to a share-of-audience input.

**Also first sighting outside the United States**, which is the rollout marker worth keeping. MD-181 said US general availability in October; this is a UK account on 17 November.

**Amended [[Auction Mechanics & Bidding#AU-032|AU-032]], and it is the day's most interesting line, because Heath argues against his own claim.** AU-032 is his: Meta's reservation buying type can only guarantee a cheap CPM by serving worse prospects in worse placements, so auction is the correct default. Walking Super Burst he supplies the limit himself. The mechanism needs Meta to be able to choose who sees the ad, and at a high share of a named demographic it cannot: "meta would not be able to cherry pick the lower quality prospects... Your ads will be put in front of everyone." **This is reasoning and not evidence.** He reports "very limited experimentation" and no results, and no conversion figure, cost per result or lift number appears anywhere in the walkthrough. Status stays active, the default stays auction, and what changes is a scope line: the degraded-prospect argument applies to reservation buys that leave Meta room to choose, and stops applying to a flight that buys nearly everyone. The one-impression cap is the second reason the operator rule holds, since a flight capped at one impression per person cannot carry a prospect the way a frequency of three can.

**The cheap-reach number, and it is arithmetic.** [[Meta Delivery & Andromeda#MD-053|MD-053]] already holds that cost per thousand people reached equals CPM times frequency. A conversion campaign at a GBP 20 CPM and frequency 3 costs GBP 60 per thousand people reached against GBP 4.50 here at frequency 1. That is the roughly 10x gap Heath claims, and **the frequency term is where nearly all of it comes from, not the CPM term.** No new claim, because the identity was already banked.

**Watchlist: automated lane clean, 0 errors, cache committed.** Meta Engineering 0 new, feed build 13 Nov and now 5 days stale. Meta Newsroom 1 new. Google Ads & Commerce 0 new. Google Ads announcements flat at 396 answer IDs. TikTok SDK changelog unchanged at v0.1.8. arXiv cs.IR 63 items in the build served, 0 passed the advertising filter. Weekly Monday sources not due.

**The one Newsroom item was opened and read in full, and it is not banked.** "Muse Is Now Available in Australia", 17 November. No advertising content: the only occurrences of the word ads on the page are the cookie banner and a footer link. It is recorded as the fourth re-check on [[Learning & Signal#LS-076|LS-076]], the claim that banks Meta's launch-day statement that Muse conversations do not reach the ad systems and that instructs exactly this re-check. **The finding is the direction of the connectors.** Nine named Australian partners including Kogan, MECCA, Officeworks, Ticketek and ShopBack can be transacted with inside the agent, in every case the person's own agent reaching out to an app they already use, with no business onboarding, no lead capture, no directory and no advertiser-facing surface. A surface now carrying purchase intent for nine named retailers that no advertiser can buy into is the state most worth watching.

**Meta for Business News, the one Daily scrape the script does not handle: both shelves flat, 0 new.** Plain fetch returned HTTP 400 on both pinned URLs, so route step 2 carried it and WebFetch read both. US 12 slugs, newest 12 November 2026, identical in set and order to 16 November. UK 12 slugs, newest 27 October 2026, the recurring 2026-10-31 through 11-08 ordered state. **0 new against `slugs_seen_cumulative`, which stays at 41.** Honest limit on today's coverage: the Playwright MCP server failed to connect in this session on every profile, and the UK shelf was read once rather than twice, so today is one sample of a five-state set and not full UK coverage under the 2026-11-10 pass-2 rule.

**TikTok Newsroom, the for-Business blog and the Marketing API what's-new page were not retried.** Permanent India geo-block, standing ruling, not an outage.

### Skill law layer

**Not updated.** MD-201 is platform mechanics on a product our book cannot buy: one country or region is the targeting floor and a month of budget in six hours is the price. MD-181 already ruled the brand-reservation lane out for lead generation at our budgets and that ruling is unchanged. The AU-032 amendment narrows a scope line inside a T3 claim and does not move a law.

### Gaps noticed

- **We have never once opened Reach Planner on a client account.** MD-201 is read entirely off somebody else's UK screen, and the cheapest thing that would make it ours is five minutes per account checking whether Reach Planner and the two burst products are even present on Phoenix Truxx, SJR Commercial and StayWell. That is a presence check, not a spend decision, and it would also date the rollout on US accounts, which is the one thing MD-181 and MD-201 together still cannot say.
- **The forecast tool is a free read on auction demand and we are not using it.** The day tiers and the hour-of-day addressable-audience numbers in MD-201 come out of Reach Planner without spending anything. If it is present on a client account it prices peak against standard days for that geography, which is the same demand signal our CPM claims argue about with no instrument. Unverified for a lead-gen geography, worth the five minutes above before it is believed.
- **`nick-theriot` returned HTTP 404 on listing.** First failure on that handle in this run series. One error does not retire a channel; two consecutive ones should trigger a handle check against the Channel Roster.

"""

txt = LOG.read_text(encoding="utf-8")
anchor = "## 2026-11-17 (Tuesday)"
i = txt.index(anchor)
assert "## 2026-11-18" not in txt
shutil.copy(LOG, str(LOG) + ".bak-20261118")
LOG.write_text(txt[:i] + ENTRY + txt[i:], encoding="utf-8")
print("Harvest Log entry inserted")
