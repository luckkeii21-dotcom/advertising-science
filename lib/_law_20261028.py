import io, shutil, os

SK = r"E:\claude code marketing skill\.claude\skills\advertising-science\SKILL.md"
shutil.copyfile(SK, SK + ".bak-20261028")

t = io.open(SK, encoding="utf-8").read()
anchor = "a naive opt-out clears `TEXT_ASSET_AUTOMATION` and anything else already in there."
assert t.count(anchor) == 1

para = """

**The 2026-10-28 pass names the FAST LOOP inside an auto-bidder for the first time, and it is a classical feedback controller rather than a learned bidder (AU-101, T1).** Pinterest published its deployed auto-bidding system, RLBP. Two layers, stated plainly: "PID controllers are widely used in production for their stability and interpretability", they stay in place for the **high-frequency bid adjustments**, and the reinforcement-learning part sits above as a meta-controller that picks each campaign's PID parameters **once a day**. So the learned component acts on the controller's tuning, not on the bid. **Two operating readings fall out, both directional.** A daily parameter update is a mechanism for why a bid change settles over about a day rather than in minutes. And a controller tuned per campaign explains two campaigns with identical settings behaving differently, with no appeal to audience quality. **The same paper states that the objective WEIGHTING MOVES OVER A CAMPAIGN'S LIFE**, cost efficiency dominating early "when budgets roll over" and delivery urgency taking over near the deadline, which makes a first-week-against-last-week cost comparison a comparison of two different objectives. **The result half publishes no magnitude at all**, only "a statistically significant reduction in effective cost-per-click" with a two-month holdout, so there is nothing to quote and nothing to forecast from. Pinterest is not Meta and not Google, and we do not buy it; this is read as how auto-bidding is built.

**The same pass got the first measurement of what happens between a Google impression and a Google click, and it says the top of the page is a near-certain impression and a scarce click (GA-098, T2).** Eye-gaze, cursor and click telemetry on **2,776 real Google result pages**: **99.7% of top-ads carousels are fixated and only 10% of clicks land on them**, ad placements take about **16%** of main-axis clicks, and the same page's People Also Ask boxes are fixated 44% of the time for two clicks in the whole corpus. **The dissociation is a property of the element, not of ads.** The diagnostic consequence is the usable one: on a Search campaign holding high impression share with a weak click-through rate, "nobody saw it" is close to ruled out for the top block, which puts the whole burden on the ad text and the query match. Lab-recorded tasks, no vertical, no device mix, no date range published, so the percentages never travel to an account or to a client, and the 10% is a share of clicks rather than a click-through rate.

**One existing claim went contested the same day, and it cuts at a structure question we answer weekly (CR-196).** It held, from one operator, that images and video in the same ad set starve each other, so separate them. A second operator with a $300M book runs the opposite deliberately and reports the starvation too, with the winner reversed: **Meta is now allocating his mixed ad sets' budget toward STATICS** (CR-289, T3). **So "one format cannibalises the other" has two independent sightings and which format wins is not fixed.** Meta's own measurement at CR-261 sits on the mix-them side of the structure question. **The only instruction to carry: check spend by format before judging a format, and from today read that in both directions, because the video is now the one that can go unfunded.** The reversal itself stays a T3 direction and never a number. Its one quantified limb is a self-selected YouTube audience poll with no respondent count on any of its four readings, which measures what advertisers believe their accounts returned, and a wave of newer advertisers making cheap AI statics would move it with no change in the auction at all.
"""

t = t.replace(anchor, anchor + para.rstrip("\n"), 1)
io.open(SK, "w", encoding="utf-8").write(t)
print("law layer updated:", "AU-101, T1" in t, "GA-098, T2" in t)
print("backup:", os.path.basename(SK + ".bak-20261028"))
