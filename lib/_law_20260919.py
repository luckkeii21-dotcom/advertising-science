# -*- coding: utf-8 -*-
"""2026-09-19: hot-layer update for SKILL.md. No law changed."""
import pathlib, re

SKILL = pathlib.Path(r"E:\claude code marketing skill\.claude\skills\advertising-science\SKILL.md")
txt = SKILL.read_text(encoding="utf-8")

ANCHOR = "Updated only when the codex changes at law level. Each law cites its claims; depth lives in the codex. "
assert ANCHOR in txt, "anchor missing"

NEW = (
    "**The 2026-09-19 research pass changed NO law and produced a reading rule that corrects a number "
    "this file already leaned on** (CR-252 and MM-220 new at T3; MD-160, GA-076, GA-077 and GA-078 new at T1; "
    "CR-117, CR-048, CR-021 and CR-023 amended, CR-023 lifted T4 to T3). "
    "**The rule: a headline single-ad spend figure is a SUM until the operator says it is not.** "
    "On 2026-09-07 Nick Theriot showed a static built 2025-07-19 and said it had spent $260,000, in the words "
    "\u201cthis particular static ad right here\u201d. On 2026-09-18 he walked the same asset, same client, same headline, "
    "gave $234,853 over the last 12 months at a $27 cost per lead, and then added the half the first telling left out: "
    "it runs in three different cities as three ads and the figure is all three added together. "
    "**Per ad that is roughly $78,300, so CR-117's right tail loses one of its three six-figure single-ad points, "
    "and the two that remain, the Charley T $2 million ad and the Blue Sense quarter-million-a-month VSL, "
    "have never been re-told and carry exactly the same exposure.** Nothing in the claim is refuted. The mean is still a mean "
    "and the tail still carries accounts. What moved is the confidence in the tail, which is measured entirely in figures "
    "nobody publishes a denominator for. "
    "**The four new T1s are all product-existence with no mechanism and no figures, and three of them are a GAP rather than news**: "
    "journey-aware bidding, demand-led pacing and lead intent scores were announced at Google Marketing Live 2026 in May and this "
    "codex had zero coverage of any of the three until today. The one with an operating consequence is GA-076, because it makes a "
    "third state available for a conversion action, **feeding the prediction without entering the bid target**, which is the exact "
    "reason a lead-gen account refuses to track its own back end. MD-160 is Meta stating that its own ad removals fire across "
    "restricted goods, third-party intellectual property, ad quality and format as well as fraud, so **a removal on a client account "
    "says nothing about which policy fired until the notice itself is read**, and any outside estimate of scam-ad revenue built on "
    "removal counts is inflated by an unpublished factor. "
)

txt = txt.replace(ANCHOR, ANCHOR + NEW, 1)

OLD_COUNT = re.search(r"Built from \*\*1,222 claims\*\*.*?the concrete instance of the concurrency hazard the run logs have carried since 2026-09-10\.", txt, re.S)
assert OLD_COUNT, "count sentence block not found"

NEW_COUNT = (
    "Built from **1,245 claims** (111 T1, 126 T2, 850 T3, 158 T4; 1,138 active, 101 contested, 5 superseded, 1 refuted) "
    "across 11 topic files, recounted at 14:55 IST on 2026-09-19 after this pass banked six. "
    "Both columns sum to 1,245, every heading carries a Tier line directly beneath it, all 1,245 ids are distinct, "
    "and every prefix runs unbroken from 1 to its maximum with no gaps. "
    "**The reconciliation is exact and it corrects a number this engine published twice: the committed vault at the end of "
    "2026-09-18 holds 1,239 claims, not the 1,240 that both of that day's run logs printed.** 1,239 plus six is 1,245. "
    "The likely cause is that day's cross-lane CR-248 collision, where both lanes wrote the same id into the same file and the "
    "fix removed one header after the count had already been taken. **A figure published by either daily pass is a snapshot taken "
    "mid-day, because the research and teacher runs both write claims into the same files**, and this is the first time that hazard "
    "has been shown to have moved a published total rather than merely threatened to. Count against the committed file, never "
    "against yesterday's printed number."
)

txt = txt[:OLD_COUNT.start()] + NEW_COUNT + txt[OLD_COUNT.end():]
SKILL.write_text(txt, encoding="utf-8")
print("hot layer updated; SKILL.md now", len(txt.split("\n")), "lines")
