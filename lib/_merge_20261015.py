# -*- coding: utf-8 -*-
"""2026-10-15 research merge: 3 new claims, 4 merges."""
from pathlib import Path

SCI = Path(r"E:\claude code marketing skill\Obsidian God-level Marketing Vault\God-level Marketing\wiki\science")


def rd(p):
    return (SCI / p).read_text(encoding="utf-8")


def wr(p, t):
    (SCI / p).write_text(t, encoding="utf-8")


def after_block(text, anchor_heading, insert):
    """Insert `insert` just before the Sources: line of the claim beginning at anchor_heading."""
    i = text.index(anchor_heading)
    j = text.index("\nSources:", i)
    return text[:j] + "\n" + insert.rstrip() + text[j:]


def bump(text, anchor_heading, newdate="2026-10-15"):
    i = text.index(anchor_heading)
    j = text.index("\nLast touched:", i)
    k = text.index("\n", j + 1)
    return text[:j] + "\nLast touched: " + newdate + text[k:]


# ---------------------------------------------------------------- SC-001 merge
f = "Scaling Models.md"
t = rd(f)
t = after_block(t, "### SC-001 \u00b7", """
**A sixth independent step size, 2026-10-14, and it arrives with the clearest argument yet that the percentage is the least important part of the decision.** Jon Loomer: "A safe increase that will hopefully result in minimal volatility will be around 15%. Again, it's just a number, and don't feel like you need to stick to it." That lands inside the converging 15 to 30% band and he refuses to defend the figure, which is the honest version of what every operator in this claim is doing. **What he adds is the reason to be cautious, and it is not the one this claim has been arguing about.** "It's not about restarting learning, it's about finding that sweet spot", where the sweet spot is the highest spend that still clears the profit bar. The step size exists to locate a profitability ceiling by bisection, so a smaller step buys resolution on where the ceiling sits and costs time, and the governing variable is the account's RUNWAY rather than any delivery mechanic: "If you have all the time in the world to find your sweet spot, you can take your time. But if you need to scale quickly, you may not have that flexibility." The mechanism behind the dip he attributes to audience expansion rather than to a learning reset, banked separately at [[Learning & Signal#LS-088|LS-088]].
**One move at the ceiling that no other prescription in this claim contains.** When results stop holding, do not drop the budget first. "It could be a perceived ceiling. This is also an opportunity to create more ads and try something different and see if that improves your results before dropping your budget." Lower the budget only after new creative fails to lift it. That orders two levers this codex has carried separately, and it is consistent with [[Scaling Models#SC-161|SC-161]], where new creative inside an existing CBO cannot out-compete incumbent winners for funding. Prescriptive, 8-minute video, 1,284 words, no account, no spend figure and no before-and-after on any step.
""")
t = bump(t, "### SC-001 \u00b7")
t = t.rstrip() + """

### SC-176 \u00b7 Before deciding an ad set is scalable, strip the algorithmic remarketing out of its result: breakdown by audience segment and read the one-day-click or incremental column
Tier: T3 \u00b7 Status: active
The first claim in this topic about qualifying an ad set for scaling rather than about how fast to raise its budget, and it names the failure it exists to prevent: "The reason so many advertisers fail to scale is because they falsely believe that an ad set was worth scaling in the first place."
**The mechanism.** A $10 cost per conversion or a 4x return can be mostly warm traffic, because remarketing now happens inside delivery whether or not anyone built a retargeting ad set. Warm pools exhaust, so any result carried by them is unscalable by construction, and the surface number hides which kind you have.
**The two tests, either of which is one breakdown.** First, break the ad set down by audience segment, ignore engaged audiences and existing customers, and ask whether cost per result on NEW audiences alone clears the bar, "because prospecting scales since you have close to an endless supply of potential new customers." Second, and offered because he does not trust that most accounts have defined their segments properly, isolate one-day click or the incremental attribution column: "Ignore one-day view, one-day engage through, and even seven-day click because they all tend to require other marketing channels. In other words, likely remarketing, which isn't scalable. One-day click is scalable and predictable."
**Why it is worth banking at T3 rather than being obvious.** It converts a measurement setting into a go/no-go gate on a spending decision, which nothing else in this topic does. It also predicts the size of the dip in [[Learning & Signal#LS-088|LS-088]]: an ad set whose result was remarketing-heavy should fall further on a budget raise than one that was already prospecting, "if your original results came primarily from remarketing audiences, the drop in performance is likely to be even more pronounced."
**For us, this is cheap and we have not run it.** Both breakdowns are a column change on an account we already have open. Neither Phoenix Truxx nor SJR Commercial has ever had an audience-segment or one-day-click read pulled before a budget move, and both run in markets where warm pools are small enough that the answer could go either way.
**Guards.** Prescriptive video, nothing shown. No account, no worked breakdown, no case where the test changed a decision, and no evidence offered that a new-audience-clean ad set actually scales better than a contaminated one. The second test rests on the assumption that one-day click equals prospecting, which is a proxy and not a definition. Loomer's own "most surface level conversion results lie" is an assertion about a population he does not quantify. Read as a diagnostic worth running, not as a validated filter. Directly related: [[Attribution & Incrementality#AT-087|AT-087]] states the same rule one level down, at the creative rather than the ad set, and is T4 for the same reason.
Sources: Jon Loomer, How Do You Scale Your Meta Ads Budget?, 2026-10-14
Last touched: 2026-10-15
"""
wr(f, t)
print("SC: merged SC-001, added SC-176")

# ---------------------------------------------------------------- LS-003 merge + LS-088
f = "Learning & Signal.md"
t = rd(f)
t = after_block(t, "### LS-003 \u00b7", """
**Added 2026-10-15, and it closes part of the question this claim has carried open since August while opening a smaller one.** Jon Loomer states the absence outright: "there isn't an established threshold dollar amount or percentage increase that will restart learning." That agrees with the T1 core, which documents a magnitude-dependent threshold and never locates it, and it means the 3% and 100% figures above stay practitioner assumptions rather than approximations of a known number. **Stop treating the threshold as discoverable from the outside.**
**The new part, and it is a product-level exemption nobody has banked: "if your ad set is labeled high performing, your increase won't restart learning."** If that is right, the reset risk on a budget raise is not a function of the percentage alone, it is gated on a status Meta assigns to the ad set, and an operator can read that status before deciding the step. **Unverified and worth one minute to check.** He shows no screenshot, names no documentation, and Meta's own significant-edits page lists no such exemption. Before this is quoted to anyone, open a scaled ad set, confirm the label exists in the current interface, and raise the budget on it while watching delivery status. That is a T2 we could own for free.
**And the reason he gives for not caring much either way is banked separately at [[Learning & Signal#LS-088|LS-088]]:** on his account of it, the performance dip after a budget raise is caused by the audience expansion, not by the learning reset, which makes the reset question less load-bearing than this claim's history assumes.
""")
t = bump(t, "### LS-003 \u00b7")
t = t.rstrip() + """

### LS-088 \u00b7 The performance dip after a budget raise is audience expansion to first-time viewers, not the learning reset, and that makes it partly temporary and partly permanent
Tier: T4 \u00b7 Status: active
A competing explanation for the second most-cited phenomenon in media buying, and it belongs beside [[Learning & Signal#LS-072|LS-072]], which does the same job for the launch ramp.
**The mechanism as stated.** "It's not restarting learning that's the problem. It's the increase itself, regardless of how much, that leads to temporary instability." The chain: a budget raise forces Meta to widen the pool, so the incremental impressions land on people being reached for the first time, and "if you're selling anything of value, you should know that most purchases will not happen from that first view of your ad." Two separate penalties arrive at once, a less-likely-to-convert group AND a group that has not been through a full exposure cycle yet.
**Two predictions that make it useful rather than merely plausible.** The dip is expected, so a raise that looks bad on day two is not evidence the raise was wrong: "Expect your results to get worse, at least initially. That's normal." And recovery is partial, never full: "you're unlikely to get the same cost per conversion and return on ad spend at $200 per day as at $5,000 per day." The second half is the part operators skip, and it is why the ceiling in [[Scaling Models#SC-001|SC-001]] is a real economic boundary rather than a settling artefact.
**Why this is T4 and what would move it.** No cohort read, no first-impression-versus-repeat-impression breakdown, no account, no numbers anywhere in the source. The mechanism and a learning reset predict the same curve for the first few days, which is the identical evidence problem LS-072 names: if two mechanisms predict the same curve, the curve is not evidence for either. **Separating them is cheap and nobody has done it.** Raise a budget on an ad set that is NOT in learning (see the unverified high-performing exemption at [[Learning & Signal#LS-003|LS-003]]) and read whether the dip still appears. If it does, the reset was never the cause.
**The operating consequence, which holds whichever mechanism is right.** Hold a step "at least a few days" before reading it, and judge the raise on whether results stabilise and stay profitable rather than on the first day. Related: [[Scaling Models#SC-176|SC-176]] predicts the dip is deeper when the pre-raise result was remarketing-carried.
Sources: Jon Loomer, How Do You Scale Your Meta Ads Budget?, 2026-10-14
Last touched: 2026-10-15
"""
wr(f, t)
print("LS: merged LS-003, added LS-088")

# ---------------------------------------------------------------- GA-032 merge + GA-094
f = "Google Auction & Smart Bidding.md"
t = rd(f)
t = after_block(t, "### GA-032 \u00b7", """
**\u26a0 The first of the three settings is being rebuilt, and there is a dated deadline on it, added 2026-10-15.** Google is replacing the all-or-nothing Display opt-out inside Search campaigns with a priority tier plus a percentage cap, and **"starting in February 2027, for Search campaigns with the Google Display Network turned on, the current spend allocation setup will go away, and advertisers may see a shift in channel spending."** The preservation setting is published: Google Display Network on "Low priority" with a 50% budget allocation. Full claim, including what the new controls do and do not do, at [[Google Auction & Smart Bidding#GA-094|GA-094]]. **The audit step in this claim does not change: on a cold Search campaign the right Display allocation is still usually zero.** What changes is that leaving it alone is no longer a stable state.
""")
t = bump(t, "### GA-032 \u00b7")
t = t.rstrip() + """

### GA-094 \u00b7 Google is replacing all-or-nothing network opt-outs with priority tiers plus a percentage cap, and a Search campaign left on the Google Display Network loses its current spend split in February 2027
Tier: T1 \u00b7 Status: active
**The two new controls, in Google's own words.** Channel prioritization "lets marketers decide where their budgets go first by categorizing inventory as 'High priority' or 'Low priority' for specific channels or channel groupings. When configured, campaigns will fully fund high-priority channels (within their target when using Target CPA or Target ROAS) before allocating the remaining budget to lower-priority channels." Budget allocation sits underneath it: a channel set to Low priority can carry "a maximum percentage of their daily budget", held "on a best-effort basis". Both are optional, both land at account and campaign level, both apply to shared budgets, and they roll out to Search, Shopping, Performance Max and Demand Gen "over the next months". On Search the addressable channels are Google Search, Search partners and the Google Display Network separately. On Performance Max and Demand Gen the Google surfaces (Search, YouTube, Maps, Gmail, Discover) are one undivided group called "Google channels", so the new control cannot split YouTube out of a PMax campaign.
**\u26a0 The dated change, and it is the only part that acts on an account by itself.** "Starting in February 2027, for Search campaigns with the Google Display Network turned on, the current spend allocation setup will go away, and advertisers may see a shift in channel spending. To keep their current configuration, they can set the Google Display Network to 'Low priority' with a 50% budget allocation." **So today's implicit Display split inside a Search campaign is being retired, and the replacement default is not stated anywhere in the post.** Any Search campaign with Display still on is exposed to an unquantified shift in where its money goes. The named preservation setting is the only mitigation Google publishes.
**The limit Google states on its own feature, and it is the most useful sentence in the announcement.** Channel prioritization alone does nothing on a tCPA or tROAS campaign that is not budget-limited: "This is particularly helpful for campaigns with Target CPA or Target ROAS bidding that are not limited by budget since channel prioritization alone will generally not have an impact there." A priority order only bites when there is not enough budget to fund everything. **On most of our Search accounts, which run target-based bidding and are not budget-capped, the percentage allocation is the real control and the priority tier is decoration.**
**What this is not.** It is not a guarantee. "Best-effort basis" is Google's own hedge on whether the cap holds, no tolerance is published, and no figure of any kind appears in the post, so there is nothing here to quote to a client and nothing to put in a forecast. It is also framed as added control while the underlying direction is the opposite of an opt-out: the pitch is that advertisers who historically turned Search partners and Display off "can use this new lever to test these networks with more confidence and clearer limits, rather than turning them off entirely."
**Operating position, held until the controls appear in our accounts.** Check every client Search campaign for Google Display Network and Search partners state now, before February 2027, because the deadline falls on the setting rather than on the announcement. Where Display is on without a reason, the answer is still off. Where it is on deliberately, set Low priority with an allocation and treat the percentage as a ceiling that may leak. Related: [[Google Auction & Smart Bidding#GA-032|GA-032]] records Display-inside-Search as one of three default settings that silently leak budget; [[Google Auction & Smart Bidding#GA-085|GA-085]] records the thirteen-month pattern of Google shipping controls that make its automated channels comparable on other platforms' terms.
Sources: Google Ads & Commerce Blog, "Guide your campaign spending with new priority and allocation features", Tal Akabas, Director of Product Management, Google Ads, 2026-10-14, read in full; page cached at .claude/skills/advertising-science/cache/google-channel-priority-20261015.html
Last touched: 2026-10-15
"""
wr(f, t)
print("GA: merged GA-032, added GA-094")

# ---------------------------------------------------------------- AT-087 merge
f = "Attribution & Incrementality.md"
t = rd(f)
t = after_block(t, "### AT-087 \u00b7", """
**A second independent operator states the same rule one level up, 2026-10-15, which raises the claim's standing without supplying the test it needs.** Jon Loomer applies it to the AD SET as a gate on scaling rather than to creative as a gate on selection: isolate one-day click or the incremental column, and treat that number rather than the default read as the one that says whether the thing can take more budget. His reason is the same one, that the longer windows are carrying warm traffic, and his guards are the same, nothing shown. Full claim at [[Scaling Models#SC-176|SC-176]]. **Two operators asserting it is still two assertions. The load-bearing word is still "scalable" and neither has tracked a scaled ad afterwards.** What the second source does change: the proposed read is now the gate for two different decisions, which makes the test in the paragraph above worth more than it was, because one column read answers both.
""")
t = bump(t, "### AT-087 \u00b7")
wr(f, t)
print("AT: merged AT-087")
