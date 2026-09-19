# -*- coding: utf-8 -*-
"""2026-09-19: replace the speculative count explanation with the verified cause."""
import pathlib

SKILL = pathlib.Path(r"E:\claude code marketing skill\.claude\skills\advertising-science\SKILL.md")
HL = pathlib.Path(r"E:\claude code marketing skill\Obsidian God-level Marketing Vault\God-level Marketing\wiki\science\Harvest Log.md")
RUN = pathlib.Path(r"E:\claude code marketing skill\.claude\skills\advertising-science\runs\2026-09-19-research-log.md")

# ---------------------------------------------------------------- SKILL.md
old = (
    "The likely cause is that day's cross-lane CR-248 collision, where both lanes wrote the same id into the same file and the "
    "fix removed one header after the count had already been taken. **A figure published by either daily pass is a snapshot taken "
    "mid-day, because the research and teacher runs both write claims into the same files**, and this is the first time that hazard "
    "has been shown to have moved a published total rather than merely threatened to. Count against the committed file, never "
    "against yesterday's printed number."
)
new = (
    "**The cause is found and it is not the concurrency hazard.** `Harvest Log.md` line 665 carries a log entry whose own heading "
    "reads `### CR-231, new: after the teardown there are three places to differentiate`. That is a log entry quoting a claim header, "
    "not a claim, and it sits outside the 11 topic files. A counter that scans every `.md` in the science folder, or that matches "
    "`^### XX-000` without requiring the space that separates an id from its title, picks it up and returns one too many. "
    "**1,239 topic-file claims plus that one stray log heading is exactly the 1,240 published on 2026-09-18.** This file's own stated "
    "method already says the counter \u201creads only the 11 topic files\u201d, so the method was right and the run that corrected 1,239 up to "
    "1,240 corrected in the wrong direction. **Count the 11 topic files, require the space after the id, and check that every prefix "
    "runs unbroken from 1 to its maximum**, which is the test that would have caught this on the day: 1,239 had no gaps and no "
    "duplicates, so there was nothing missing to find."
)
t = SKILL.read_text(encoding="utf-8")
assert old in t, "SKILL.md passage not found"
SKILL.write_text(t.replace(old, new, 1), encoding="utf-8")
print("SKILL.md corrected")

# ---------------------------------------------------------------- Harvest Log
old_hl = """**The claim count correction.** Both 2026-09-18 run logs printed 1,240. **The committed vault at the end of that day holds 1,239, checked by counting headers at the commit itself: 1,239 headers, 1,239 distinct ids, no duplicates, no gaps in any prefix.** 1,239 plus this run's six is 1,245, which is what today's file holds. The likely cause is that day's cross-lane CR-248 collision, where both lanes wrote the same id and the fix removed one header after the count had been taken. **This is the first time the concurrency hazard has been shown to have moved a published total rather than merely threatened to.** Count against the committed file, never against yesterday's printed number."""
new_hl = """**The claim count, and the 2026-09-18 correction went the wrong way.** That day's log first said 1,239 unique ids, then a later commit changed it to 1,240 headers and 1,240 distinct ids. **1,239 was right.** Counting at the committed revision returns 1,239 headers across the 11 topic files, 1,239 distinct ids, no duplicates, and no gaps in any prefix.

**The extra one is a log entry, not a claim.** `Harvest Log.md` line 665 opens an entry with `### CR-231, new: after the teardown there are three places to differentiate`. A counter that scans every `.md` in this folder, or that matches `### XX-000` without requiring the space that separates an id from its title, counts that heading as a claim. **1,239 plus that stray heading is 1,240.** The method this engine documents already says the counter reads only the 11 topic files, so the method was right and the recount was not.

**The test that catches it costs nothing: check that every prefix runs unbroken from 1 to its maximum.** At 1,239 there were no gaps and no duplicates, so nothing was missing and the higher number had nowhere to come from. Today: 1,239 plus this run's six is **1,245**, verified the same way, 1,245 headers, 1,245 distinct ids, every prefix contiguous, both the tier and status columns summing to 1,245."""
t = HL.read_text(encoding="utf-8")
assert old_hl in t, "Harvest Log passage not found"
HL.write_text(t.replace(old_hl, new_hl, 1), encoding="utf-8")
print("Harvest Log corrected")

# ---------------------------------------------------------------- run log
old_run = """## The count correction

Both 2026-09-18 run logs printed 1,240 claims. Counting headers at the committed vault revision returns **1,239 headers, 1,239 distinct ids, no duplicates, no gaps in any prefix**. 1,239 + 6 = 1,245, which is today's file. Today's file verified the same way: 1,245 headers, 1,245 distinct, no duplicates, every prefix contiguous from 1 to max, every heading carrying a Tier line. Tier split 111 T1, 126 T2, 850 T3, 158 T4; status split 1,138 active, 101 contested, 5 superseded, 1 refuted; both columns sum to 1,245."""
new_run = """## The count correction, and yesterday's correction went the wrong way

The 2026-09-18 Harvest Log entry first said **1,239 unique ids**. Commit `7146475`, titled "correct the codex claim count in the log entry", changed it to **1,240 claim headers and 1,240 distinct ids**. **1,239 was right and the correction introduced the error.**

Counting at the committed revision returns 1,239 headers across the 11 topic files, 1,239 distinct ids, no duplicates, no gaps in any prefix.

**The extra one is a log entry.** `wiki/science/Harvest Log.md` line 665 opens an entry with `### CR-231, new: after the teardown there are three places to differentiate and they are checked in order`. Note the comma: a regex requiring `^### XX-000 ` with a trailing space skips it, a regex without that space matches it. A counter scanning every `.md` in the science folder rather than the 11 topic files picks it up either way. **1,239 + 1 stray log heading = 1,240.**

`SKILL.md` already documents the right method, "the counter pairs each heading with the next line and reads only the 11 topic files". The recount did not follow it.

**The free test: every prefix must run unbroken from 1 to its maximum.** At 1,239 there were no gaps and no duplicates, so there was no room for a 1,240th claim anywhere. Today's file passes the same test: **1,245 headers, 1,245 distinct ids, every prefix contiguous from 1 to max, every heading carrying a Tier line directly beneath it.** Tier split 111 T1, 126 T2, 850 T3, 158 T4. Status split 1,138 active, 101 contested, 5 superseded, 1 refuted. Both columns sum to 1,245. 1,239 + 6 = 1,245."""
t = RUN.read_text(encoding="utf-8")
assert old_run in t, "run log passage not found"
t = t.replace(old_run, new_run, 1)
t = t.replace("Codex 1,239 to 1,245. No law changed.**", "Codex 1,239 to 1,245. No law changed.** Yesterday's published count of 1,240 is corrected below.")
RUN.write_text(t, encoding="utf-8")
print("run log corrected")
