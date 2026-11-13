# SKILL.md hot-layer update, 2026-11-13. Adds law 11e: Meta's own published
# calibration doctrine, which lands on a contested claim in our codex.
import io

S = r"E:\claude code marketing skill\.claude\skills\advertising-science\SKILL.md"

LAW = """
11e. **Meta now publishes its OWN recipe for correcting attribution, and the recipe is a single scalar multiplier with a residual step that quietly launders the error into organic (AT-135, T1, added 2026-11-13).** A four-part Meta for Business series, May 2025 to 12 November 2026, read in full at source. The method: run a Conversion Lift test, divide lift conversions by attributed conversions, apply that scalar to the channel "going forward". Meta's worked example is `150 / 100 = 1.5x`. **Then the step to watch.** If the multiplied total exceeds real total conversions, Meta says test the other platforms too, and "Any remaining conversions can be attributed to organic." Organic never gets an experiment in Meta's procedure, so it absorbs every error in every paid multiplier plus every untested channel. **Three things this changes for us.** One, the contested static-discount-factor argument at AT-023 now has a T1 on the pro-multiplier side, so a client or an agency proposing a fixed discount is quoting platform doctrine rather than freelancing; the staleness objection survives untouched, because Meta's only cadence guidance is "periodically", with no interval and no refresh trigger. Two, our measurement hierarchy at AT-022 is no longer ours to defend alone: Meta publishes the same ordering (experiment above model above attribution, AT-138) and so does Google (AT-115), and the tier stays T3 because two interested platforms agreeing is agreement rather than evidence. Three, **the three-tier MMM calibration taxonomy at AT-136 gives us a question worth asking out loud**: when anyone says a model is "calibrated", ask which tier, because Meta's own tier one is a check that both methods point the same direction and tier three is the only one that touches carryover and saturation. **Guards, and they are heavy.** Zero confidence intervals anywhere across a series about experiments, no holdout size, no test duration, no minimum detectable effect, and the one worked example is a company Meta labels fictional. Use the series for Meta's doctrine, vocabulary and mechanics. Never as proof the mechanics work, and never as a reason to put a multiplied number in a client report.
"""

t = io.open(S, encoding="utf-8").read()
assert "11e. **Meta now publishes its OWN recipe" not in t, "law 11e already present"
anchor = "\n11d. **Warm-audience leakage now has three shown accounts"
assert t.count(anchor) == 1, "anchor for law 11d not unique"
t = t.replace(anchor, "\n" + LAW.strip() + "\n" + anchor, 1)
io.open(S, "w", encoding="utf-8").write(t)
print("added law 11e to SKILL.md hot layer")
