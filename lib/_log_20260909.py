# -*- coding: utf-8 -*-
"""2026-09-09: write the Harvest Log entry for the research run."""
from pathlib import Path

ENTRY = """## 2026-09-09 (research run)

**⚠ PLATFORM CHANGE AFFECTING OUR CLIENTS. Meta is withdrawing ad-set exclusion of placements, platforms, devices and operating systems.** The notice is live inside Ads Manager and is quoted verbatim at MD-150: *"Excluding placements, platforms, devices and operating systems will no longer be available for your ad sets."* **Meta has published no announcement**, trade coverage on 2026-08-25 found the Business Help Centre still describing manual placement selection as available, and the unofficial scope is a test on Sales and Leads objectives only with sensitive verticals excluded. **Nobody should tell a client this has happened to their account.** Our own read today found all four controls still present.

**1 new transcript, read in full. 3 claims added, 4 amended, law 1a amended, 0 errors on every readable source.** Harvest listed all 12 channels clean, 6 videos skipped under the length floor, 2 with no subtitles. Backlog was 0 going in, 1 going in on today's file, and is **0 going out**; 450 transcripts on file, all flagged extracted.

### The change, and what it actually removes

**Four controls, not one, and three of them will be missed because the headline reads as being about placements (MD-150, T1 for the notice and the surfaces, new).** Individual placements can no longer be switched off. Whole platforms can no longer be excluded, so an Instagram-only build stops existing at ad-set level. Delivery can no longer be limited to mobile or desktop. Delivery can no longer be limited by mobile operating system.

**The two sources disagree about the rollout and only one of them is careful.** Jon Loomer, dated 2026-08-24, carries the verbatim notice and labels his own scope information unofficial: *"Nothing is official until it's documented in an announcement or found on Meta's official pages."* His unofficial read is a test with plans to expand, sensitive verticals excluded (special ad categories and possibly health and wellness), eligibility tied to the new multimedia workflow, **and Sales and Leads objectives only**. **Ben Heath, 2026-09-08, states it as done**: going "across the board in ad accounts very soon" and "may have already happened in your ad account", with no scope, no objective limit and no test framing anywhere in eighteen minutes, and no mention that Meta has announced nothing. Loomer and the trade reporting agree with each other and disagree with him. Read Heath for the mechanics he demonstrates on screen and not for the rollout status.

### We checked our own account, and the honest answer is that it has not arrived where we could look

Ad account 645682541775849, ad set editor opened on a **Leads** objective (Advantage+ leads) and on an **Awareness** objective as a control, because Loomer's scope note predicts the change spares Awareness. **Both still carry a full Placements section.** Expanded, the Leads ad set shows every control the notice says is going: **Devices and operating systems: All. Platforms: Facebook, Instagram and Audience Network. Placement controls: Included 17, Allowed with limited spend 0, Excluded 0. Skippable ads: Included.**

**⚠ This settles nothing about our clients and the scope limits are why.** One account, INR-billed, campaigns in draft rather than live, and it is the least representative account we hold. **Absence in one account is exactly what a partial rollout predicts**, so the observation can date our own exposure and cannot argue against the change. **The instrument that would answer it is queued: open a live US client ad set on a manual Sales or Leads campaign, which means SJR Commercial or Phoenix Truxx.** The chiropractic accounts are the wrong instrument, because health and wellness sits among the verticals Loomer says are excluded.

**Method note worth keeping, because it nearly produced a false finding.** The Ads Manager ad-set form mounts progressively, so the accessibility snapshot reported **no Placements section at all** on both objectives. That was wrong twice. A raw DOM text scan after the form settled found Placements present in both. **An absent section in an Ads Manager a11y snapshot means nothing until the form has finished mounting; scan `document.body` text, not the snapshot.**

**Two UI details new to this codex.** Placement state is **not binary**: the UI counts Included, **Allowed with limited spend**, and Excluded as three buckets, which is where the up-to-5%-of-budget-to-excluded-placements setting actually lives. And **Skippable ads is its own included/excluded control**, which no claim here had ever named. The account shows **17 placements against the 21 options Heath counts**, so the inventory count is account-dependent and neither number is the platform total.

### What replaces it, and it cannot do the same job (MD-151, T1, new)

**Lever one, placement value rules, is a bid multiplier and not a switch.** The maximum is a 90% bid decrease, which suppresses delivery and never eliminates it. Heath is straight about the mechanism, that undercutting the bid lets other advertisers win the impression, and his own words are "very very few of your ads are going to be shown", not none. **Three holes, all checkable in the UI: only seven placements are eligible against 17 to 21 in the ad set; there is no value-rule criterion for PLATFORM at all; and a rule set does nothing until it is attached, ad set by ad set.**

**Lever two, account-level Placement Controls, is the only true off switch left and it is account-wide**, so it cannot differ between two clients or two offers sharing an account. Heath's own read of its durability is a guess and is carried as one: "I think there's a decent chance that Meta takes away the ability for you to do this as well."

**The operating rule this leaves is the one SC-149 already had.** Under conversion optimisation Loomer says you should rarely need a placement value rule at all. The real exposure is upper-funnel goals, and he names it precisely for the first time: **Audience Network** for link clicks and landing-page views, **Audience Network Rewarded Video** for ThruPlay, where third-party apps pay users in virtual currency to watch. His remedy is to abandon the goal rather than prune the placement. Heath reaches the same place from the other side, that a traffic or engagement campaign should be rebuilt as Sales or Leads. **Neither states the irony: on Loomer's own scope note the change spares exactly the objectives that need placement control most.**

### Codex changes

- **MD-150 and MD-151 banked, both T1** for the notice wording, the surfaces and their limits, on the AU-076 precedent that Meta product copy read off the screen is documentation. **Everything about the rollout inside them is marked T3.**
- **MD-016 amended, and deliberately NOT refuted.** It is the recipe for excluding junk placements at ad-set level, and its execution route is what is being withdrawn. The three-way argument inside it, Shiver's recipe against Charley T's under-0.1%-of-budget rebuttal against Piliero's trim-on-your-own-data policy, is untouched on the merits and was never settled by evidence. **The resolving read it has always asked for is now time-sensitive**: the placement breakdown survives the control, so anyone wanting a record of what excluded placements were costing should pull it before the change lands.
- **SC-149 amended.** Its ordering rule, bid down before excluding, was operator judgement when banked and is about to become compulsory. Gained Loomer's named upper-funnel exposures and his stronger conversion-side line, "You should rarely need to use value rules to adjust bids by placement when using a performance goal that maximizes the number or value of conversions."
- **AU-076 amended** with the seven-placement cap, the missing platform criterion, and the per-ad-set attachment cost now that this is the main lever.
- **⚠ AU-019 amended, and this one is a correction to our own wording.** Its title says "up to the 90% maximum for effective exclusion". **A 90% decrease is deep suppression at an unmeasured residual rate, never an exclusion.** That was pedantic while the hard exclusion existed beside it. It stops being pedantic when the bid-down rule becomes the only ad-set lever, because a client told Audience Network is "excluded" by a 90% rule has been told something false. The honest sentence is that it can be made expensive and cannot be made impossible.
- **LS-076 banked, T1, and it is a negative worth an ID.** Meta launched Muse on 2026-09-08 and the launch post states: "Muse doesn't share a person's conversations or the data in their VM with Meta's ad systems." Every signal-supply claim in that file assumes new Meta surfaces eventually become both inventory and input; this is Meta drawing the boundary explicitly at launch on the surface that would hold the richest intent data it has ever collected. **Banked with its date attached so a future revision reads as a change rather than as news.** A stated policy at launch is not an architecture, and it is not a privacy guarantee to quote to a client.
- **Law 1a amended in SKILL.md**, its first law-level change driven by a platform withdrawing a control rather than by anyone learning anything. Law 1a lists the ad-set settings that genuinely bind, and it is losing four members. **Location, minimum age and language are untouched, so its geo sentence gets stronger: geo is now close to the last ad-set setting that does what it says.**
- **Counts recomputed from the topic files: 1,179 claims (96 T1, 118 T2, 809 T3, 156 T4; 1,073 active, 100 contested, 5 superseded, 1 refuted).** Reconciles exactly: 1,175 carried, plus **AU-089 from today's teacher run** (T3, banked before this pass started), plus this pass's three, all T1.

### Watchlist, 0 errors

| Source | Result |
|---|---|
| Meta Engineering RSS | 200, 9 in feed, 0 new (build Tue 08 Sep) |
| Meta Newsroom RSS | 200, 10 in feed, **1 new**, read in full and banked as LS-076 |
| Google Ads & Commerce RSS | 200, 20 in feed, 0 new (build Wed 02 Sep) |
| arXiv cs.IR | 200, 72 in feed, 69 new links, **0 passed the ad filter** |
| TikTok SDK changelog | 200, top version 0.1.8, unchanged |
| Google Ads Announcements | 200, 2350 lines both sides, 1 added / 1 removed, **a 20-digit per-response nonce, not content** |
| Meta for Business News | 12 cards, card set unchanged, **newest still 11 June 2026** |

**arXiv is a trustworthy zero today.** `lastBuildDate` Wed, 09 Sep 2026 04:25:11 UTC read at roughly 07:55 UTC, so this is today's own build after the 04:00 rebuild and not a stale one. 69 unseen links, none matching the advertising bank list. Weekly Monday sources not due on a Wednesday.

**Meta for Business News served in Hindi from our India egress**, which is new in the record and changes nothing: the card set and every date match the previous checks, and the newest post is still 11 June 2026 as it has been since 2026-08-20.

### Gaps

- **TikTok stays a genuine blind spot and is not logged as clean.** Only the SDK changelog answers, and it ships endpoint names rather than policy or creative news. The India geo-block is permanent without a non-India egress.
- **Meta Advertising Standards still has no cached baseline**, open since 2026-08-24. The lane cannot detect a silent rewrite, and ChiroWorks and Chiropraise depend on its health and personal-attributes sections.
- **The client-account placement check is the queued instrument and it is time-limited.** Open a live SJR Commercial or Phoenix Truxx Sales or Leads ad set and record whether the four controls are still present. It has to be done before the change lands to be worth anything, and it is the only way to date our own exposure rather than repeat a rumour.
- **Nobody has measured what share of delivery survives a 90% bid decrease.** That number now sits under the only ad-set placement lever we will have left, and it is unmeasured by every source on the roster. Any of our own accounts could produce it with a placement breakdown before and after a rule.

"""

P = Path(r"E:\claude code marketing skill\Obsidian God-level Marketing Vault\God-level Marketing\wiki\science\Harvest Log.md")
raw = P.read_bytes()
bom = raw.startswith(b"\xef\xbb\xbf")
t = raw.decode("utf-8-sig")
anchor = "## 2026-09-08 (teacher run)"
assert t.count(anchor) == 1, "anchor not unique"
t = t.replace(anchor, ENTRY + anchor, 1)
data = t.encode("utf-8")
if bom:
    data = b"\xef\xbb\xbf" + data
P.write_bytes(data)
print("Harvest Log entry written for 2026-09-09")
