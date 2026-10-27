import io, os

SCI = r"E:\claude code marketing skill\Obsidian God-level Marketing Vault\God-level Marketing\wiki\science"
AU = os.path.join(SCI, "Auction Mechanics & Bidding.md")
GA = os.path.join(SCI, "Google Auction & Smart Bidding.md")

# ---------------- AU-101 ----------------
au = io.open(AU, encoding="utf-8").read()
assert "### AU-101" not in au
new_au = """
### AU-101 \u00b7 A deployed auto-bidding system is a PID CONTROLLER, and the production fix was not to replace it but to retune its parameters daily with reinforcement learning
Tier: T1 \u00b7 Status: active
arXiv 2610.33248v1, *Reinforcement Learning for Controller Parameters in the Auto-Bidding System at Pinterest*, announced in the cs.IR feed and read as the abstract at source on 2026-10-28. The full paper was not opened and this claim says nothing the abstract does not. Pinterest authors describing a system they state is deployed at Pinterest.

**The architecture statement is the value here, and it is the first one in this codex that names the control loop out loud.** "While PID controllers are widely used in production for their stability and interpretability, fixed tunings cannot adapt to diverse campaigns and shifting traffic patterns." Their system, RLBP, is explicitly hybrid: reinforcement learning sits above as a meta-controller that picks campaign-specific PID parameters **once a day**, and the PID controller is kept underneath for the **high-frequency bid adjustments**. The RL layer is a multi-head Q-network trained on a relative-lift reward normalised against the production baseline, with inference-time fusion so the cost-versus-delivery trade-off adapts to campaign state without retraining.

**Why that matters to an operator who will never see Pinterest's code.** This codex argues constantly about what an auto-bid is doing and how fast it responds, from [[Auction Mechanics & Bidding#AU-039|AU-039]] through the manual-bid position at [[Auction Mechanics & Bidding#AU-014|AU-014]]. **A platform has now stated that the fast loop is a classical feedback controller with a setpoint, and that the learned part operates on the controller's parameters at a daily cadence rather than on the bid itself.** Two consequences fall out, and both are directional rather than quantified. A daily parameter update is a reason a bid change takes about a day to settle rather than minutes. And a controller tuned per campaign is a mechanism for why two campaigns with identical settings behave differently, without any appeal to audience quality.

**The campaign-lifecycle claim, stated as the thing the controller has to track.** "This trade-off evolves over campaign lifespans: early on, cost optimization dominates when budgets roll over; near deadlines, budget delivery becomes urgent." So the same system deliberately weights cost efficiency differently depending on where a campaign sits relative to its end date. **Anyone comparing the first week of a campaign against its last week on cost per result is comparing two different objective weightings**, which is the same class of void comparison as reading across an optimisation-event change.

**The result half publishes no magnitude, so it decides nothing.** "RLBP achieves a statistically significant reduction in effective cost-per-click (eCPC) with no revenue degradation, and two months of post-rollout measurements against a holdout also show consistent cost reductions." A sustained holdout is a stronger design than most of what this codex reads, and **the abstract states no percentage, no spend level, no campaign count and no confidence interval.** There is nothing here to quote and nothing to forecast from.

**The guards, and they are the usual ones for this lane.** This is Pinterest, not Meta and not Google. [[Emerging Channels#EC-001|EC-001]] and [[Emerging Channels#EC-002|EC-002]] both hold that Pinterest is a thin, structurally over-attributing surface we do not buy, so the value is as a rare published description of a production bidding system, exactly as at [[Creative Science#CR-234|CR-234]]. The optimised metric is eCPC, a platform cost metric, not an advertiser's cost per lead. **Read it as how auto-bidding is built, never as evidence about what our bids will do.**
Sources: arXiv 2610.33248v1, Reinforcement Learning for Controller Parameters in the Auto-Bidding System at Pinterest, abstract read at source 2026-10-28 via the cs.IR feed
Last touched: 2026-10-28
"""
au = au.rstrip("\n") + "\n\n" + new_au.strip("\n") + "\n"
io.open(AU, "w", encoding="utf-8").write(au)
print("AU-101 written:", "### AU-101" in au)

# ---------------- GA-098 ----------------
ga = io.open(GA, encoding="utf-8").read()
assert "### GA-098" not in ga
new_ga = """
### GA-098 \u00b7 On real Google result pages the top-ads carousel is LOOKED AT almost every time and clicked one time in ten, and ads take about 16% of main-axis clicks
Tier: T2 \u00b7 Status: active
arXiv 2605.04949v4, *AllSERP: Exhaustive Per-Element Enrichment of the Versatile AdSERP Dataset*, abstract read at source on 2026-10-28 via the cs.IR feed. Announced as a **replace**, so this is the fourth version of a paper the codex has never held; nothing was superseded here, it is new to us. The full paper was not opened.

**The instrument, which is the reason this is T2 and not T3.** AdSERP is a public corpus of **2,776 search trials** recorded on **real Google result pages**, carrying eye gaze, cursor, scroll, pupil and click telemetry together with the page screenshots and the captured HTML. AllSERP is the layer that labels everything on the page that is not an ad: organic results, People Also Ask, image packs, local packs and other widgets. Three measured numbers are published and they are what gets carried.

**One, the share of clicks ads get.** The shipped ad boxes cover placements "which receive about **16%** of main-axis clicks".

**Two, and this is the finding.** "**99.7% of top-ads carousels are fixated but only 10% of clicks land on them.**" Almost every user looks at the top ads. One in ten clicks goes there.

**Three, the control case on the same page.** "**44% of People-Also-Ask boxes are fixated but only two clicks in the corpus land on one.**" So the dissociation is not a property of ads, it is a property of element type, and it runs much harder against PAA than against ads.

**Why it earns a place in this file.** Every Search decision we make reads impressions and clicks out of Ads Manager and has no instrument for what happened in between. **This measures the middle, and it says the top of a Google results page is a near-certain impression and a scarce click.** The operating consequence is about diagnosis, not about bidding: on a Search campaign holding high impression share with a weak click-through rate, the hypothesis "nobody saw it" is close to ruled out for the top-ads block, which moves the whole burden onto the ad text and the query match. It also means impression share on that block is close to a ceiling measurement rather than a growth lever, which sits beside the budget-floor reading at [[Google Auction & Smart Bidding#GA-096|GA-096]].

**The guards, all load-bearing.** This is a lab-recorded corpus, not our accounts and not Google's data: the trials are tasks performed under eye-tracking, which is a context known to change scanning behaviour, and the paper states no date range, no geography, no device mix and no query mix in its abstract. **No vertical is named, so none of these percentages transfers to a specific account and none may be quoted to a client.** The 10% click figure is a share of clicks in the corpus, not a click-through rate, and reading it as one would be a plain error. The box-fidelity numbers (**95.7%** of final clicks landing in a typed area of interest under the gap-filled flavour, and the ad partition agreeing with the shipped ad rectangles on all **38,250** comparisons) are quality checks on the dataset, not findings about advertising.
Sources: arXiv 2605.04949v4, AllSERP: Exhaustive Per-Element Enrichment of the Versatile AdSERP Dataset, abstract read at source 2026-10-28 via the cs.IR feed
Last touched: 2026-10-28
"""
ga = ga.rstrip("\n") + "\n\n" + new_ga.strip("\n") + "\n"
io.open(GA, "w", encoding="utf-8").write(ga)
print("GA-098 written:", "### GA-098" in ga)
