# -*- coding: utf-8 -*-
"""2026-10-23 correction to the CR-116 merge made earlier the same run.

Loomer states 4.5 and 3.0 as TOTAL/lifetime frequency with no window. MD-008 and
CR-177's unit discipline forbid comparing a window-free figure against a 14-day or
30-60 day threshold, so the numeric refutation does not stand. What survives is his
denial that a universal window-free threshold exists. Rewrite the block to say so,
and add the same caution to MD-051.
"""
import sys
from pathlib import Path

SCI = Path(r"E:\claude code marketing skill\Obsidian God-level Marketing Vault\God-level Marketing\wiki\science")


def must(cond, msg):
    if not cond:
        print("ABORT: " + msg)
        sys.exit(1)


cs = SCI / "Creative Science.md"
t = cs.read_text(encoding="utf-8")

old = """**What this overturns and what it leaves standing.** It does not touch the curve, because nobody has measured per-impression purchase probability on either side. What it contradicts is the OPERATING THRESHOLD, the instruction to read ad-level frequency above 2 as a creative shortage. One account held 3.0 at the ad level across $150,000 per ad while improving month over month, so the threshold is not a general rule and must not be quoted as one. Status moves to contested on that basis.
"""
must(old in t, "CR-116 overturn paragraph not found")

new = """**\u26a0 THE NUMBERS CARRY NO WINDOW, SO READ THE REFUTATION NARROWLY.** Loomer says "total frequency of 4.5" on a campaign he describes as running "over a long period of time", and about 3.0 on two ads that took $150,000 each across that same span. **Those are lifetime figures, not a 14-day or 30-day pull.** This claim's threshold is a 30-to-60-day read, [[Creative Science#CR-177|CR-177]]'s is 14 days, and [[Meta Delivery & Andromeda#MD-008|MD-008]] states that a frequency number means nothing until the window is named. A lifetime 3.0 across many months is not the same quantity as a 14-day 2.0 and may well be consistent with it. **So his figures do NOT numerically refute either threshold, and nobody may quote them as if they do.** The irony is worth recording because it is instructive: his own argument opens by insisting the window is everything, "seeing the same ad four times in a week is not the same thing as four times in a year", and he then reports his counter-example without one.

**What does survive, and it is why the status moves.** Two things. First, the qualitative outcome: a $450,000 broad-US campaign deliberately concentrated into a few ads, which he calls "a complete opposite of the popular approach" and against "Meta's own best practices of creative diversity", reports no fatigue and results "only getting better month after month". The threshold's operating instruction is to treat a breach as a fix-now creative shortage; this account looks like the structure the instruction warns about and did not need the fix. Second, the explicit denial of universality: "no one knows what high or low, good or bad frequency actually is. There isn't a universal threshold." **Status moves to contested on the claim that the number is a general rule, not on the arithmetic.** The windowed versions at CR-177 and MD-051 stand untouched and still want a real test.
"""
t = t.replace(old, new, 1)

# Tighten the guard paragraph to name the window gap as the first defect.
oldg = """**Guards on the counter-case.** No dashboard shown, no CPA, ROAS or date range, and the figures are stated from memory on camera."""
must(oldg in t, "CR-116 guard paragraph not found")
newg = """**Guards on the counter-case.** The missing window above is the largest of them. Beyond it: no dashboard shown, no CPA and no ROAS, and the figures are stated from memory on camera."""
t = t.replace(oldg, newg, 1)
cs.write_text(t, encoding="utf-8")
print("Creative Science.md: CR-116 counter-case narrowed to the window-free reading")

# --- MD-051: record that the one counter-case offered carries no window ---
md = SCI / "Meta Delivery & Andromeda.md"
t = md.read_text(encoding="utf-8")
anchor = """A tighter threshold from a second operator, and it is unusable as stated. Mark Builds Brands puts the cold top-of-funnel line at 1.5 rather than 2,"""
must(anchor in t, "MD-051 second-operator paragraph not found")
add = """The first counter-case arrived 2026-10-21 and it fails on this claim's own unit rule. Jon Loomer reports a broad-US campaign at a "total frequency of 4.5" and two ads at about 3.0 each on roughly $150,000 apiece, with no fatigue and improving results, as his argument that no universal frequency threshold exists. **He states no window, and describes the span only as "a long period of time", so these are lifetime figures and they do not touch a 30-to-60-day pull.** Under MD-008 the comparison cannot be made. What his case does press on is the INSTRUCTION rather than the number: that account is concentrated into few ads, which is the shape this audit is built to catch, and it reports no problem. Treat the audit as still correct on its own window and no longer safe to describe as universal. Detail and the surviving dispute at [[Creative Science#CR-116|CR-116]].

"""
t = t.replace(anchor, add + anchor, 1)
md.write_text(t, encoding="utf-8")
print("Meta Delivery & Andromeda.md: MD-051 counter-case + window caution added")
