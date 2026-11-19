# -*- coding: utf-8 -*-
"""Insert the 2026-11-19 law paragraph into the SKILL.md hot layer."""
from pathlib import Path

P = Path(r"E:\claude code marketing skill\.claude\skills\advertising-science\SKILL.md")
ANCHOR = "**The 2026-11-12 pass establishes that the DEPTH of Meta's ranking funnel"

NEW = (
 "**The 2026-11-19 pass puts a CLOCK on Meta's own ranking changes, and the clock is the law (MD-202, T1).** "
 "Two Meta Engineering posts, both 18 November, both on ads ranking models, read in full. Meta's own sentence: "
 "\"Today it can take over a year for every proven technique to reach every applicable model\", with a stated "
 "target of three months that needs 5x more throughput to reach. MD-198 already held that there is no single "
 "ads model, that each one is bound to a surface, an objective, a feature set and a serving budget, and MD-198's "
 "own limits said no refresh cadence was disclosed anywhere. It is disclosed now. **So the fleet is heterogeneous "
 "in TIME as well as in architecture: the model ranking an ad in Reels and the model ranking it in Feed can be a "
 "year apart in which improvements they carry.** The operating use is narrow and it is a better first explanation "
 "than the ones usually reached for: a tactic that genuinely works on one placement or one optimisation event and "
 "genuinely does not work on another, at the same time, in the same account, can be a propagation gap rather than "
 "audience quality or creative. Hold it as an explanation, never offer it as a diagnosis, because Meta names no "
 "model, no surface and no technique, and nothing in it is readable from an ad account. **Three more things land "
 "with it.** Meta publishes a shelf life on its own work, \"an innovation that delivers gains today may be "
 "superseded within a couple of model development cycles\", which is the first first-party statement that "
 "platform-side gains decay on their own. The two-year scoreboard for the template system is 0.63% offline and "
 "0.86% cumulative online lift over 70% of models by count, which is the same order of magnitude as MD-198's "
 "0.66% and summed 0.36% from a separate publication, so **the under-one-percent rule now has two independent "
 "first-party sources and \"Meta changed their model\" still cannot explain an account moving by tens of percent "
 "in a week.** And the ship gate is published: an offline normalized-entropy gain, no regression on training or "
 "inference cost, then a statistically significant online A/B win, with regression RATE weighed alongside average "
 "gain because \"consistency is as important as peak improvement\". Every percentage is Meta's own with no "
 "population, no holdout and no counterfactual, and the 60%, 3x, 4x and $45M agent figures are all hedged in "
 "Meta's own text. **One outside number pairs with it and it is worth carrying (AU-103, T1):** a deployed "
 "real-time-bidding system published both halves of a shipped ranking win, 0.81% offline normalized-entropy "
 "improvement and +4.65% on advertiser conversion value, bought for 15% more online inference cost per request. "
 "That is the first figure connecting an internal model-quality metric to advertiser money, it is one unnamed "
 "system, and it is not a conversion factor for Meta's numbers."
)


def main():
    t = P.read_text(encoding="utf-8")
    if "2026-11-19 pass puts a CLOCK" in t:
        print("SKIP: already present")
        return
    i = t.index(ANCHOR)
    t = t[:i] + NEW + "\n\n" + t[i:]
    P.write_text(t, encoding="utf-8")
    print("inserted law paragraph, %d chars" % len(NEW))


main()
