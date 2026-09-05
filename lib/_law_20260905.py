# -*- coding: utf-8 -*-
"""2026-09-05: refresh the SKILL.md hot-layer counts and add one reading rule.
No law changed. Nothing banked today was T1 or T2."""
import io

P = "E:\\claude code marketing skill\\.claude\\skills\\advertising-science\\SKILL.md"
t = io.open(P, encoding="utf-8").read()

OLD_TAIL = ("**The 2026-09-04 pass changed no law**; it banked one claim and amended one, "
            "and only the counts below moved. Built from **1,162 claims** "
            "(92 T1, 117 T2, 798 T3, 155 T4; 1,056 active, 100 contested, 5 superseded, 1 refuted) "
            "across 11 topic files. Counts recomputed from the topic files, not carried forward from the log.")

NEW_TAIL = ("**The 2026-09-05 pass changed no law either**; it cleared the entire 31-file transcript backlog "
            "to zero, banked seven claims and amended eleven, and nothing it banked reached T1 or T2. "
            "Built from **1,169 claims** "
            "(92 T1, 117 T2, 804 T3, 156 T4; 1,063 active, 100 contested, 5 superseded, 1 refuted) "
            "across 11 topic files. Counts recomputed from the topic files, not carried forward from the log.")

assert t.count(OLD_TAIL) == 1, t.count(OLD_TAIL)
t = t.replace(OLD_TAIL, NEW_TAIL)

RULE = """

**A second reading rule, found 2026-09-05, and this one corrects arithmetic already sitting in the codex.** "Markup" is spoken in two incompatible conventions and nobody announces which. By formula it is (price less cost) over cost; in ordinary keystone use it is price divided by cost. **The same product is 4x under one and 5x under the other, so "3x markup" means price is 3x cost to one speaker and 4x cost to another** (MM-210, T3, new). MM-018's product floor is written in the keystone convention and its own worked example mislabels the ratio as markup, which is now flagged on the claim. Margin converts as markup / (1 + markup), and back as margin / (1 - margin). **The rule: before carrying any multiple from a source or a client, ask whether it divides by price or by cost.** No law moves, and the direction of every affected claim is unchanged."""

anchor = "It is a reading rule: when a source says scaling, ask which axis before carrying the claim."
assert t.count(anchor) == 1
t = t.replace(anchor, anchor + RULE)

io.open(P, "w", encoding="utf-8", newline="\n").write(t)
print("SKILL.md hot layer updated")
