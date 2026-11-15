# -*- coding: utf-8 -*-
import io, shutil

P = r"E:\claude code marketing skill\.claude\skills\advertising-science\SKILL.md"
shutil.copyfile(P, P + ".bak-20261115")
t = io.open(P, encoding="utf-8").read()

ANCHOR = u"Never as proof the mechanics work, and never as a reason to put a multiplied number in a client report."
assert t.count(ANCHOR) == 1
ADD = u""" **AMENDED 2026-11-15, and the amendment is the magnitude.** The methodology report behind the series, "Building a suite of truth", is **ungated** at `facebook.com/business/f/1094917955782254` and was read in full: 20 pages. It supplies the number the four blog posts omitted. **At the median, advertisers undervalue Meta by 31%, and "a multiplier of at least 1.45X was required to calibrate the results of the models to the true value driven by Meta", off 307 studies run by 54 advertisers between March 2022 and November 2024 across four regions (AT-139, T1).** The 31% and the 1.45X are one measurement from two ends, `45 / 145 = 31%`, so they never corroborate each other. Note what that does to the worked example above: Meta teaches the method with an invented `1.5x` that sits within 3% of its own measured median and never says so. **Three operating consequences.** One, Meta's own report tells you not to do what its blog demonstrates: "run multiple tests to allow a pattern to emerge, as opposed to taking action on a single study", and it finally gives a cadence, "typically quarterly" for the cross-publisher calibration test, with single-cell Conversion Lift for allocation, multi-cell for strategy validation and incremental attribution for real time (AT-140). Two, incremental attribution now has one Meta-published effect size, **a 46% average performance lift, and the footnote restricts the sample to the 37 studies where significant incrementality was already detected in at least one cell** (AT-141), so it is the gain among campaigns already known to have an effect and not the expected gain from flipping the setting. Do not collide it with the unrelated 46% at AT-085, a reporting haircut in the opposite direction. Three, the test-design parameters are **still not published anywhere**: no holdout size, no minimum detectable effect, no confidence interval, in the report that was the only plausible home for them (AT-144). The one duration figure Meta has ever published remains AT-125's 2 to 3 weeks at holiday volume against 6 or more weeks in a quiet quarter. **So the guards above stand unchanged, with one addition: 1.45 is Meta's median across its own studies of its own undervaluation, and it is not a coefficient to apply to a client's lead count.**"""

t = t.replace(ANCHOR, ANCHOR + ADD, 1)
io.open(P, "w", encoding="utf-8").write(t)
print("law 11g amended; new length", len(t))
