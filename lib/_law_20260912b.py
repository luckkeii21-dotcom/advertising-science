# -*- coding: utf-8 -*-
"""2026-09-12 research pass: hot-layer header entry and claim counts."""
from pathlib import Path

SKILL = Path(r"E:\claude code marketing skill\.claude\skills\advertising-science\SKILL.md")
t = SKILL.read_text(encoding="utf-8")

# ------------------------------------------------------------ header entry
OLD = "Updated only when the codex changes at law level. Each law cites its claims; depth lives in the codex. "

ADD = ("**The 2026-09-12 research pass AMENDED TWO laws, both off a single Meta case study** (AT-117, T1 for "
       "what Meta published; CR-232, CR-233 and LS-077 new; AT-035, CR-124, CR-068, CR-115 and MD-013 "
       "amended). **Law 11a** gains a third step, because the find-the-word test can be passed by a NAMED "
       "VALIDATOR that is structurally incapable of validating: Meta prints a 35% net-new-visits gain from "
       "incremental attribution and says a third-party multi-touch attribution tool confirmed it, and MTA "
       "observes only exposed users, so it has no unexposed cell and cannot answer the question. **Law 4b** "
       "gains a free test that sits OUTSIDE the asset: the longest-open question in the codex had been asked "
       "entirely as a question about recutting footage, and an advertiser reports a burned-out asset taking "
       "spend again when moved to a different optimization setting with the creative untouched, which splits "
       "fatigue into an audience diagnosis and a delivery-selection diagnosis that look identical in Ads "
       "Manager. No law was added and none retired. ")

assert t.count(OLD) == 1, "header anchor"
t = t.replace(OLD, OLD + ADD, 1)

# ------------------------------------------------------------ counts
OLDC = ("Built from **1,185 claims** (100 T1, 118 T2, 810 T3, 157 T4; 1,079 active, 100 contested, "
        "5 superseded, 1 refuted) across 11 topic files. Counts recomputed line by line from the topic files "
        "on 2026-09-11, matching each claim heading to the Tier line directly beneath it; every one of the "
        "1,185 headings carries one. **Yesterday's figure of 1,179 was four low** (2 T1, 1 T3, 1 T4) because "
        "the previous recount used a regex that could skip a heading whose Tier line it had already consumed. "
        "Today's two additions are both T1 and both active, so 1,183 pre-existing plus 2 reconciles exactly.")

NEWC = ("Built from **1,191 claims** (101 T1, 121 T2, 811 T3, 158 T4; 1,085 active, 100 contested, "
        "5 superseded, 1 refuted) across 11 topic files, counted at 10:30 IST on 2026-09-12. Both columns sum "
        "to 1,191 and every heading carries a Tier line directly beneath it. The counter pairs each heading "
        "with the next line and reads only the 11 topic files, which is the fix for both of the failures the "
        "2026-09-11 log recorded. **The reconciliation from yesterday's 1,185 is exact and it runs through "
        "two passes, not one**: the 2026-09-11 teaching pass banked AT-116 after that day's count was taken, "
        "the 2026-09-12 teaching pass banked AT-118, and this research pass banked four. 1,185 plus 2 plus 4 "
        "is 1,191. **A figure published by either daily pass is a snapshot taken mid-day, because the "
        "research and teacher runs both write claims into the same files**, and on 2026-09-12 they ran "
        "concurrently from 09:45.")

assert t.count(OLDC) == 1, "counts anchor"
t = t.replace(OLDC, NEWC, 1)

SKILL.write_text(t, encoding="utf-8")
print("header and counts updated")
