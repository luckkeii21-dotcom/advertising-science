# -*- coding: utf-8 -*-
"""2026-09-12 research pass: hot-layer amendments to laws 11a and 4b."""
from pathlib import Path

SKILL = Path(r"E:\claude code marketing skill\.claude\skills\advertising-science\SKILL.md")
t = SKILL.read_text(encoding="utf-8")

# --------------------------------------------------------------- law 11a
OLD11 = ("The other three figures in the same post fail the original test cleanly, "
         "all labelled as internal Google aggregates over 14-day or half-year windows with no control.")

ADD11 = (" **AMENDED AGAIN 2026-09-12, and this time the trap is a NAMED VALIDATOR (AT-117, T1 for what "
         "Meta published).** Meta's 10 September case study prints an advertiser saying incremental "
         "attribution produced \"about 35% higher net-new visits\", and Meta adds that this is \"a lift "
         "validated by their third-party MTA tool\". That sentence looks like the answer to the first two "
         "steps: the word is there, a third party checked it. **Multi-touch attribution cannot validate "
         "incrementality, because it only ever observes people who were exposed.** It splits credit across "
         "touchpoints a converter actually had and has no unexposed cell, so it cannot say whether the visit "
         "would have happened anyway. Two models built on the same exposed population agreeing is not a "
         "control group. So the test has a third step: find the word, ask whether it names the method or the "
         "metric, then ask what the validator actually measures. **A named third party raises the bar for "
         "nothing unless that party ran an unexposed cell.** Note also that the outcome here is site VISITS, "
         "and the design is a before-and-after on the same ads with a setting changed.")

assert t.count(OLD11) == 1, "law 11a anchor"
t = t.replace(OLD11, OLD11 + ADD11, 1)

# --------------------------------------------------------------- law 4b
OLD4B = ("**The surviving empirical question is much narrower than the debate: does re-cutting the first "
         "3 to 5 seconds of an existing shoot revive a fatigued winner?**")

ADD4B = ("\n**2026-09-12: the question had been asked entirely INSIDE the asset, and there is a free test "
         "outside it that nobody had run (CR-232, T3; CR-124 amended).** An advertiser in a Meta case study "
         "says creative the team thought had burned out \"can come back to life\" when moved into an ad set "
         "optimizing on a different setting, with the asset untouched. Nothing is shown and the source sells "
         "the setting, so it is weak evidence for that lever. **It is strong as a reframe, because it splits "
         "fatigue into two diagnoses that produce the identical Ads Manager row.** Either the audience has "
         "seen the asset and stopped responding, which only new creative fixes, or delivery stopped selecting "
         "it against the objective it is scored on, which a different objective can reverse. **Before funding "
         "a reshoot on a dead winner, duplicate it into an ad set optimizing on something else and watch "
         "whether it takes spend.** Spend returning says it was deselected, not exhausted. The same revival "
         "shape is already on file from outside the asset at CR-147, where a matching landing page revived "
         "ads that took no spend.")

assert t.count(OLD4B) == 1, "law 4b anchor"
t = t.replace(OLD4B, OLD4B + ADD4B, 1)

SKILL.write_text(t, encoding="utf-8")
print("laws 11a and 4b amended")
