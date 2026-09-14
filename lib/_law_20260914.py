# -*- coding: utf-8 -*-
"""2026-09-14 law-layer update.

No law added, none retired. Three T1 claims arrived; two of them (PinDCO, ChronicleRec)
are other platforms' internal architecture with no operating consequence for our book
this week, so they stay in the topic files. The third (MD-156) changes how a policy
page may be quoted, which is a reading rule rather than a law.

Also refreshes the stale claim count, and updates the CBO-starvation watch item, which
today's merge speaks to directly.
"""
from pathlib import Path

SKILL = Path(r"E:\claude code marketing skill\.claude\skills\advertising-science\SKILL.md")


def edit(old, new, count=1):
    t = SKILL.read_text(encoding="utf-8")
    assert t.count(old) == count, f"anchor count {t.count(old)} != {count}"
    SKILL.write_text(t.replace(old, new, count), encoding="utf-8")
    print("edited SKILL.md")


# ------------------------------------------------ 1. today's entry at the head of the layer
HEAD_SRC = "Updated only when the codex changes at law level. Each law cites its claims; depth lives in the codex. **The 2026-09-13 teaching pass AMENDED law 21c**"

HEAD_NEW = """Updated only when the codex changes at law level. Each law cites its claims; depth lives in the codex. **The 2026-09-14 research pass changed NO law, and added a reading rule instead** (MD-156, CR-234 and LS-078 new at T1, fifteen more at T3; SC-024 and CR-031 amended). Three T1 claims arrived and only one of them touches how we work. PinDCO and ChronicleRec are Pinterest's and Tencent's own ranking architecture, published and credible, with no consequence for an account we run this week. **MD-156 is the one with a consequence, and the rule it produces is: never quote a Meta policy section name without saying which locale you read it on.** Meta renamed the Advertising Standards section "Fraud, Scams, and Deceptive Practices" to "Prohibited Commercial Practices" and collapsed two policies into one, and on the same day, in the same browser session, the default locale carries the new name and `/en-gb/` still carries the old one. **A rejection appeal that cites a section name the reviewer's locale does not have is arguing from a page that does not exist for them.** Note the direction too: two named prohibitions became one pointer at a Community Standard, which moves the binding text onto a page this lane does not watch. **The 2026-09-13 teaching pass AMENDED law 21c**"""

edit(HEAD_SRC, HEAD_NEW)

# ------------------------------------------------ 2. refresh the stale claim count
COUNT_SRC = """Built from **1,191 claims** (101 T1, 121 T2, 811 T3, 158 T4; 1,085 active, 100 contested, 5 superseded, 1 refuted) across 11 topic files, counted at 10:30 IST on 2026-09-12. Both columns sum to 1,191 and every heading carries a Tier line directly beneath it. The counter pairs each heading with the next line and reads only the 11 topic files, which is the fix for both of the failures the 2026-09-11 log recorded. **The reconciliation from yesterday's 1,185 is exact and it runs through two passes, not one**: the 2026-09-11 teaching pass banked AT-116 after that day's count was taken, the 2026-09-12 teaching pass banked AT-118, and this research pass banked four. 1,185 plus 2 plus 4 is 1,191. **A figure published by either daily pass is a snapshot taken mid-day, because the research and teacher runs both write claims into the same files**, and on 2026-09-12 they ran concurrently from 09:45."""

COUNT_NEW = """Built from **1,211 claims** (104 T1, 122 T2, 827 T3, 158 T4; 1,104 active, 101 contested, 5 superseded, 1 refuted) across 11 topic files, counted at 11:00 IST on 2026-09-14. Both columns sum to 1,211 and every heading carries a Tier line directly beneath it. The counter pairs each heading with the next line and reads only the 11 topic files. **The reconciliation from 2026-09-12's 1,191 runs through three passes and it is exact**: the 2026-09-13 teaching pass banked MM-212, the 2026-09-14 teaching pass banked MD-155, and the 2026-09-14 research pass banked eighteen. 1,191 plus 1 plus 1 plus 18 is 1,211. **A figure published by either daily pass is a snapshot taken mid-day, because the research and teacher runs both write claims into the same files.** On 2026-09-14 they launched in the same second and the research pass read the highest existing ID three minutes AFTER the teacher pass had written MD-155, which is the only reason the two did not both claim that number. **That is luck, not design**, and it is the concrete instance of the concurrency hazard the run logs have carried since 2026-09-10."""

edit(COUNT_SRC, COUNT_NEW)

# ------------------------------------------------ 3. CBO starvation watch item
WATCH_SRC = """- **Push delivery to an ad exists and it is the direct answer to a problem we have.** An ad-level control under "show more options" guarantees a named ad a set percentage of ad set budget for a window of 1 to 30 days (MD-103). Shiver calls it hidden and is not using it, so we hold zero performance evidence. Worth knowing because our CBO on SJR has starved new creative for weeks at a time, and this is the first surface that would force delivery to a refresh without a new ad set."""

WATCH_NEW = """- **Push delivery to an ad exists and it is the direct answer to a problem we have.** An ad-level control under "show more options" guarantees a named ad a set percentage of ad set budget for a window of 1 to 30 days (MD-103). Shiver calls it hidden and is not using it, so we hold zero performance evidence. Worth knowing because our CBO on SJR has starved new creative for weeks at a time, and this is the first surface that would force delivery to a refresh without a new ad set. **A second operator named the same starvation as a general Andromeda-era behaviour on 2026-09-14 and published his workaround** (SC-024, amended): "when we launch new ads in existing campaigns, they get no spend and then we never know if the creative that we've spent so much time producing actually works." His fix needs no hidden control and is the one we could copy this week: a **7-day minimum budget forced onto each new ad set** at launch. So there are now two routes to the same outcome, the ad-level push and the ad-set minimum, and we have run neither. Still zero performance data behind either."""

edit(WATCH_SRC, WATCH_NEW)

print("\nLAW LAYER UPDATED")
