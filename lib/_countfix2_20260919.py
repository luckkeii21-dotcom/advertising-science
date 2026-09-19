# -*- coding: utf-8 -*-
"""2026-09-19: my own count was wrong. MD-019b is a real claim my regex dropped.
Yesterday's 1,240 was right. True count today is 1,246."""
import pathlib, re

SKILL = pathlib.Path(r"E:\claude code marketing skill\.claude\skills\advertising-science\SKILL.md")
HL = pathlib.Path(r"E:\claude code marketing skill\Obsidian God-level Marketing Vault\God-level Marketing\wiki\science\Harvest Log.md")
RUN = pathlib.Path(r"E:\claude code marketing skill\.claude\skills\advertising-science\runs\2026-09-19-research-log.md")

TRUE = (
    "Built from **1,246 claims** (112 T1, 126 T2, 850 T3, 158 T4; 1,139 active, 101 contested, 5 superseded, 1 refuted) "
    "across 11 topic files, recounted at 15:10 IST on 2026-09-19 after this pass banked six. Both columns sum to 1,246, "
    "every heading carries a Tier line directly beneath it, all 1,246 ids are distinct. "
    "**The reconciliation from 2026-09-18's 1,240 is exact: 1,240 plus six is 1,246.** "
    "**Counting this codex has exactly two traps and this pass fell into one of them before the sync script caught it.** "
    "Trap one: **`MD-019b` is a sub-lettered id**, the only one in the codex, so a regex of the form `^### XX-\\d+ ` that "
    "requires a space after the digits silently drops a real claim and returns 1,245. Trap two: **`Harvest Log.md` carries a "
    "log entry whose own heading reads `### CR-231, new: after the teardown...`**, which is a log entry quoting a claim header "
    "rather than a claim, so a counter that scans every `.md` in the science folder counts it and returns 1,247. "
    "`bin/Sync-TeamRepo.ps1` does exactly that and prints 1,247 in its commit messages. "
    "**The correct method, and it is the one to use: the 11 topic files only, matching `^### XX-\\d+[a-z]? ` on a word boundary.** "
    "A figure published by either daily pass is still a snapshot taken mid-day, because the research and teacher runs both write "
    "claims into the same files."
)

t = SKILL.read_text(encoding="utf-8")
m = re.search(r"Built from \*\*1,245 claims\*\*.*?so there was nothing missing to find\.", t, re.S)
assert m, "SKILL.md count block not found"
SKILL.write_text(t[:m.start()] + TRUE + t[m.end():], encoding="utf-8")
print("SKILL.md count corrected")

HL_NEW = """**The claim count, and a correction to this entry's own first draft.** The codex now holds **1,246 claims** across the 11 topic files: 112 T1, 126 T2, 850 T3, 158 T4, and 1,139 active, 101 contested, 5 superseded, 1 refuted. Both columns sum to 1,246, all 1,246 ids are distinct, and every heading carries a Tier line. **2026-09-18's published 1,240 was right, and 1,240 plus this run's six is 1,246.**

**This pass first published 1,245 and said the 2026-09-18 figure had been corrected in the wrong direction. That was this pass's error, caught by the sync script's own counter thirty minutes later.** Counting this codex has exactly two traps and they pull in opposite directions.

- **`MD-019b` is a sub-lettered id, the only one in the codex.** A regex of the form `^### XX-\\d+ ` that requires a space after the digits drops it and returns **1,245**. That is what happened here.
- **`Harvest Log.md` carries a log entry whose own heading reads `### CR-231, new: after the teardown...`.** That is a log entry quoting a claim header, not a claim. A counter that scans every `.md` in this folder rather than the 11 topic files counts it and returns **1,247**. `bin/Sync-TeamRepo.ps1` does exactly that, so every one of its commit messages overstates the codex by one.

**The method that is right: the 11 topic files only, matching `^### XX-\\d+[a-z]? ` on a word boundary.** Worth fixing the sync script's regex and scope so the two counters agree."""

t = HL.read_text(encoding="utf-8")
m = re.search(r"\*\*The claim count, and the 2026-09-18 correction went the wrong way\.\*\*.*?both the tier and status columns summing to \*\*1,245\*\*\.", t, re.S)
assert m, "Harvest Log count block not found"
HL.write_text(t[:m.start()] + HL_NEW + t[m.end():], encoding="utf-8")
print("Harvest Log count corrected")

RUN_NEW = """## The count, and a correction to this run's own first draft

**The codex holds 1,246 claims across the 11 topic files.** 112 T1, 126 T2, 850 T3, 158 T4. 1,139 active, 101 contested, 5 superseded, 1 refuted. Both columns sum to 1,246, all 1,246 ids distinct, every heading carrying a Tier line. **2026-09-18 published 1,240 and 1,240 was right. 1,240 + 6 = 1,246.**

**This run first published 1,245 and wrote into three files that commit `7146475` had corrected 1,239 up to 1,240 in the wrong direction. That was this run's error.** It was caught by `bin/Sync-TeamRepo.ps1` printing 1,247 at the end of the run, which forced a third count.

Two traps, pulling opposite ways:

| Trap | Effect | Who hits it |
|---|---|---|
| `MD-019b`, the codex's only sub-lettered id | A regex requiring `^### XX-\\d+ ` with a space after the digits drops a real claim | This run's counter, returning 1,245 |
| `Harvest Log.md` line 669, `### CR-231, new: after the teardown...`, a log entry quoting a claim header | A counter scanning every `.md` in the science folder counts a non-claim | `bin/Sync-TeamRepo.ps1`, returning 1,247 |

**Correct method: the 11 topic files only, matching `^### XX-\\d+[a-z]? ` on a word boundary.**

**Action for tomorrow: fix `bin/Sync-TeamRepo.ps1` line 85.** It scans `Get-ChildItem $codexDst -Filter '*.md'` with `^### [A-Z]{2}-\\d`, so it counts the Harvest Log heading. Every sync commit message it has written overstates the codex by one."""

t = RUN.read_text(encoding="utf-8")
m = re.search(r"## The count correction, and yesterday's correction went the wrong way.*?1,239 \+ 6 = 1,245\.", t, re.S)
assert m, "run log count block not found"
t = t[:m.start()] + RUN_NEW + t[m.end():]
t = t.replace("Codex 1,239 to 1,245. No law changed.** Yesterday's published count of 1,240 is corrected below.",
              "Codex 1,240 to 1,246. No law changed.**")
RUN.write_text(t, encoding="utf-8")
print("run log count corrected")
