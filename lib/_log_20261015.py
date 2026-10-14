# -*- coding: utf-8 -*-
"""2026-10-15: Harvest Log entry + run log."""
from pathlib import Path

SCI = Path(r"E:\claude code marketing skill\Obsidian God-level Marketing Vault\God-level Marketing\wiki\science")
RUNS = Path(r"E:\claude code marketing skill\.claude\skills\advertising-science\runs")

ENTRY = """## 2026-10-15 (research run)

**1 transcript in, 3 claims added, 4 merges, 0 contested, 0 refuted, 0 errors. One law amended.** A thin day on volume with one dated platform change in it that acts on client accounts without anyone touching them.

**One claim from Google, and it is the day's only item with a deadline.** [[Google Auction & Smart Bidding#GA-094|GA-094]], T1, from "Guide your campaign spending with new priority and allocation features" (Google Ads & Commerce Blog, Tal Akabas, Director of Product Management, 2026-10-14), read in full; page cached at `cache/google-channel-priority-20261015.html`. Google is replacing the all-or-nothing network opt-out with two optional controls across Search, Shopping, Performance Max and Demand Gen: channel prioritization, which funds High-priority channels fully before anything reaches Low priority, and budget allocation, which caps a Low-priority channel at a percentage of daily budget. Account and campaign level, shared budgets included. On Search the three channels are addressable separately. On PMax and Demand Gen the Google surfaces are one undivided group, so the control cannot split YouTube out of a PMax campaign.

- **\u26a0 The dated part.** "Starting in February 2027, for Search campaigns with the Google Display Network turned on, the current spend allocation setup will go away, and advertisers may see a shift in channel spending." The replacement default appears nowhere in the post. The published preservation setting is Google Display Network on "Low priority" with a 50% budget allocation. Merged as a warning into [[Google Auction & Smart Bidding#GA-032|GA-032]], which already records Display-inside-Search as one of three defaults that silently leak budget, because that claim's audit step is the one that now has a clock on it.
- **The limit Google states on its own feature**, and it is the most useful sentence in the announcement: channel prioritization alone "will generally not have an impact" on a tCPA or tROAS campaign that is not limited by budget. A priority order only bites when there is not enough budget to fund everything. On most of our Search work the percentage allocation is the real control and the tier is decoration.
- **Nothing here is quotable.** The cap holds "on a best-effort basis" with no tolerance published, and the post contains no figure of any kind. First Google announcement in the thirteen-month series this engine has read that carries no headline number to check a footnote against.

**Two claims from Jon Loomer, "How Do You Scale Your Meta Ads Budget?" (2026-10-14, 8 minutes, 1,284 words), read in full and marked extracted.**

- **[[Scaling Models#SC-176|SC-176]], T3, and it is the one worth acting on.** The first claim in the Scaling topic about qualifying an ad set for scaling rather than about how fast to raise its budget. A $10 cost per conversion can be mostly warm traffic, because remarketing happens inside delivery whether or not anyone built a retargeting ad set, and warm pools exhaust. Two tests, either of which is one breakdown: read cost per result on NEW audiences alone with engaged and existing customers excluded from the read, or isolate the one-day-click or incremental column, on the reasoning that "one-day click is scalable and predictable" while seven-day click and the view windows are carrying other channels' work. Guards are total: prescriptive video, no account, no worked breakdown, no case where the test changed a decision, and no evidence that a new-audience-clean ad set actually scales better. The one-day-click-equals-prospecting step is a proxy, not a definition.
- **[[Learning & Signal#LS-088|LS-088]], T4.** A competing explanation for the dip after a budget raise, and it sits beside [[Learning & Signal#LS-072|LS-072]], which does the same job for the launch ramp. "It's not restarting learning that's the problem. It's the increase itself, regardless of how much, that leads to temporary instability." The chain: the raise widens the pool, the incremental impressions land on first-time viewers, and most purchases do not happen on a first view. Two predictions make it useful. The dip is expected rather than diagnostic. And recovery is partial: "you're unlikely to get the same cost per conversion and return on ad spend at $200 per day as at $5,000 per day", which makes the ceiling in SC-001 an economic boundary rather than a settling artefact. T4 because a learning reset predicts the same curve for the first few days and nobody has separated them. The clean separation is cheap: raise a budget on an ad set that is not in learning and see whether the dip still appears.

**Four merges.** **[[Scaling Models#SC-001|SC-001]]** takes a sixth independent step size, 15%, disowned by the operator offering it in the same sentence, inside the 15 to 30% band already converging there, plus the better reason for going gradually: the step is a bisection search for the highest spend that still clears the profit bar, so the governing variable is the account's runway and not any delivery mechanic. It also takes one move no other prescription in that claim contains: at the apparent ceiling, add creative before cutting the budget, because the ceiling may be perceived. **[[Learning & Signal#LS-003|LS-003]]** takes Loomer's flat statement that "there isn't an established threshold dollar amount or percentage increase that will restart learning", which agrees with the T1 core and means the banked 3% and 100% figures stay practitioner assumptions rather than estimates of a known number, plus one unverified product detail worth a minute: an ad set labelled high performing is claimed to be exempt from a restart on a budget raise, and Meta's significant-edits page lists no such exemption. **[[Attribution & Incrementality#AT-087|AT-087]]** gains a second independent operator stating the same rule one level up, at the ad set rather than the creative, which makes the open column-read test there answer two decisions instead of one. **[[Google Auction & Smart Bidding#GA-032|GA-032]]** gains the February 2027 warning.

**One law amended.** The hot layer now opens with the February 2027 Google Display deadline and the instruction that falls out of it: check every client Search campaign's Display and Search-partners state now, because the deadline falls on the setting rather than on the announcement. The Meta scaling material went in beside it with the gate ahead of the step size, since the pre-raise breakdown is the part we can run this week and the percentage is the part the field has argued about for three months without a test.

**Harvest: 1 new transcript from 12 channels, zero errors.** 4 uploads skipped as too short, 2 had no subtitles, 0 out of window. No extraction backlog, so the 25-a-day rule did not apply. Summary at `runs/2026-10-15-0315-harvest.json`.

**Watchlist: 3 new items, 1 banked, 2 discarded, zero errors.** Discarded, both from Meta Newsroom and both with the advertising content checked rather than assumed: "Now You Can Invite Anyone to a WhatsApp Call" is a consumer calling feature, and the Farah Khan Edits Film Festival interview is organic creator craft, the second item from that festival discarded in two days. Both pages render their bodies client-side, so the fetched shell carries only the headline and chrome; zero occurrences of advertis, campaign, ad set, Ads Manager, ROAS or Advantage+ in what was returned, and the discard rests on that plus the headline. Meta Engineering quiet at 9 items, nothing new. arXiv cs.IR carried 0 new items in window. TikTok SDK changelog unchanged at 0.1.8. Google Ads Announcements: 396 answer IDs, identical to cache, zero added and zero removed. Thursday, so the 9 Monday-only weekly sources were not due.

**Gaps noticed.**

1. **The oldest open gap is now the cheapest it has ever been to close, because today added a second reason to pull the same export.** SC-176 says read new audiences alone, or one-day click, before raising a budget. We still have not pulled an audience-segment or one-day-click read on Phoenix Truxx or SJR Commercial, and we still have not pulled the 30-day hour-of-day or day-of-week cost-per-result breakdown that MD-180 has been pointing at since 14 October. Three different claims now want data from the same two accounts and one column change supplies most of it.
2. **New, and it has a date on it.** Nobody has checked which client Google accounts have the Display Network or Search partners switched on inside a Search campaign. February 2027 is far enough away to forget and close enough that forgetting costs real money, and the check takes minutes per account.
3. **Still open from 14 October.** Nothing on file measures whether our results differ by buyer platform-activity, and no instrument for it has been named. Our book sells to light platform users while Meta's published gains concentrate where engagement history is deep.
4. **Codex hygiene, unchanged and still deliberate.** MD-103 and MD-141 remain near-duplicate claims about the same control. Not collapsed, because collapsing changes an ID other claims link to.

**Errors: none.** Harvester clean on 12 channels, watchlist clean on all six lanes. TikTok Newsroom and the TikTok for Business blog were **skipped: browser unavailable** (every Playwright MCP server failed to connect at session start), third day running. Both are India geo-blocked to a plain fetch, so they are skipped rather than reported clean.

"""

f = SCI / "Harvest Log.md"
t = f.read_text(encoding="utf-8")
anchor = "## 2026-10-14 (research run)"
i = t.index(anchor)
t = t[:i] + ENTRY + t[i:]
f.write_text(t, encoding="utf-8")
print("harvest log prepended")

RUN = """# Research run 2026-10-15 (Thursday)

**1 transcript in, 3 claims added, 4 merges, 0 contested, 0 refuted, 0 errors. One law amended.** A thin day on volume with one dated platform change in it that acts on client accounts without anyone touching them.

## What was banked

**[[Google Auction & Smart Bidding#GA-094|GA-094]], T1.** Google is replacing the all-or-nothing network opt-out with channel prioritization (High or Low priority, high funded first) plus budget allocation (a percentage cap on a Low-priority channel), across Search, Shopping, Performance Max and Demand Gen, at account and campaign level, shared budgets included. Rolling out "over the next months". On Search the three channels are addressable separately; on PMax and Demand Gen the Google surfaces are one undivided group, so the control cannot split YouTube out of a PMax campaign.

- **\u26a0 Dated.** "Starting in February 2027, for Search campaigns with the Google Display Network turned on, the current spend allocation setup will go away, and advertisers may see a shift in channel spending." The replacement default appears nowhere in the post. Published preservation setting: Google Display Network on "Low priority" with a 50% budget allocation.
- **Google's own stated limit:** channel prioritization alone "will generally not have an impact" on a tCPA or tROAS campaign that is not limited by budget, which is most of our Search work. There, the percentage allocation is the real control and the priority tier is decoration.
- **Nothing quotable.** "Best-effort basis" on the cap, no tolerance published, and no figure of any kind in the post. First Google announcement in the thirteen-month series read by this engine with no headline number at all.
- Source read in full. Page cached at `cache/google-channel-priority-20261015.html`.

**[[Scaling Models#SC-176|SC-176]], T3.** Before deciding an ad set is scalable, strip the algorithmic remarketing out of the result that made it look good: read cost per result on NEW audiences alone, or isolate the one-day-click or incremental column. Warm pools exhaust, so anything they carry is unscalable by construction. Guards are total: no account, no worked breakdown, no case where the test changed a decision, and the one-day-click-equals-prospecting step is a proxy rather than a definition.

**[[Learning & Signal#LS-088|LS-088]], T4.** The dip after a budget raise is the audience widening onto first-time viewers, not the learning reset, which makes it partly permanent: the same ad set will not hold its $200-a-day cost per result at $5,000 a day. T4 because a learning reset predicts the same curve for the first few days and nobody has separated them.

## Merges

- **[[Scaling Models#SC-001|SC-001]]**: a sixth step size, 15%, disowned in the same sentence by the operator offering it; the step reframed as a bisection search for the profitability ceiling with runway as the governing variable; and add creative before cutting budget at an apparent ceiling.
- **[[Learning & Signal#LS-003|LS-003]]**: no established threshold exists for a budget-change learning restart, so the banked 3% and 100% figures stay assumptions. Plus one unverified product detail worth a minute to check: an ad set labelled high performing is claimed exempt from a restart on a raise, and Meta's significant-edits page lists no such exemption.
- **[[Attribution & Incrementality#AT-087|AT-087]]**: a second independent operator states the same rule at the ad set rather than the creative, so the open column-read test there now answers two decisions.
- **[[Google Auction & Smart Bidding#GA-032|GA-032]]**: the February 2027 warning, because that claim's audit step is the one with a clock on it now.

## Law layer

Amended. Opens with the February 2027 Google Display deadline and the instruction that falls out of it: check every client Search campaign's Display and Search-partners state now, because the deadline falls on the setting and not on the announcement. The Meta scaling material went in beside it with the gate ahead of the step size.

## Harvest

1 new transcript from 12 channels, zero errors. 4 uploads skipped as too short, 2 had no subtitles, 0 out of window. No extraction backlog. Summary at `runs/2026-10-15-0315-harvest.json`.

## Watchlist

3 new items, 1 banked, 2 discarded, zero errors.

- **Discarded with the advertising content checked, not assumed.** Meta Newsroom, "Now You Can Invite Anyone to a WhatsApp Call" (consumer calling feature) and the Farah Khan Edits Film Festival interview (organic creator craft, second festival item discarded in two days). Both pages render their bodies client-side, so the fetched shell carries only the headline and chrome; zero occurrences of advertis, campaign, ad set, Ads Manager, ROAS or Advantage+ in what was returned. The discard rests on that plus the headline.
- Meta Engineering quiet at 9 items, 0 new. arXiv cs.IR 0 new items in window. TikTok SDK changelog unchanged at 0.1.8. Google Ads Announcements 396 answer IDs, identical to cache, 0 added and 0 removed.
- Thursday, so the 9 Monday-only weekly sources were not due.
- **Skipped: browser unavailable.** TikTok Newsroom and the TikTok for Business blog, third day running, every Playwright MCP server failed to connect at session start. Both are India geo-blocked to a plain fetch, so they are skipped rather than reported clean.

## Gaps

1. The oldest open gap is now the cheapest it has been to close, because today added a second reason to pull the same export. SC-176 wants new-audience and one-day-click reads on Phoenix Truxx and SJR Commercial; MD-180 has wanted a 30-day hour-of-day and day-of-week cost-per-result breakdown on the same two accounts since 14 October. Three claims, two accounts, mostly one column change.
2. New, with a date on it. Nobody has checked which client Google accounts have the Display Network or Search partners switched on inside a Search campaign. Minutes per account, and February 2027 is far enough away to forget.
3. Still open from 14 October. Nothing on file measures whether our results differ by buyer platform-activity, and no instrument has been named.
4. Codex hygiene, unchanged and still deliberate. MD-103 and MD-141 remain near-duplicate claims about the same control, not collapsed because collapsing changes an ID other claims link to.

## Errors

None. Harvester clean on 12 channels, watchlist clean on all six lanes. The two TikTok lanes were skipped for the reason above.
"""

(RUNS / "2026-10-15-research-log.md").write_text(RUN, encoding="utf-8")
print("run log written")
