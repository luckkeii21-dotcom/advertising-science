# -*- coding: utf-8 -*-
"""2026-09-19: finish the count correction in the Harvest Log and run log."""
import pathlib, re

HL = pathlib.Path(r"E:\claude code marketing skill\Obsidian God-level Marketing Vault\God-level Marketing\wiki\science\Harvest Log.md")
RUN = pathlib.Path(r"E:\claude code marketing skill\.claude\skills\advertising-science\runs\2026-09-19-research-log.md")

HL_NEW = """**The claim count, and a correction to this entry's own first draft.** The codex now holds **1,246 claims** across the 11 topic files: 112 T1, 126 T2, 850 T3, 158 T4, and 1,139 active, 101 contested, 5 superseded, 1 refuted. Both columns sum to 1,246, all 1,246 ids are distinct, and every heading carries a Tier line. **2026-09-18's published 1,240 was right, and 1,240 plus this run's six is 1,246.**

**This pass first published 1,245 and said the 2026-09-18 figure had been corrected in the wrong direction. That was this pass's error**, caught half an hour later by the sync script's own counter printing a third number.

**Counting this codex has exactly two traps and they pull in opposite directions.**

- **`MD-019b` is a sub-lettered id, the only one in the codex.** A regex of the form `^### XX-000 ` that requires a space straight after the digits drops it and returns **1,245**. That is the one this pass hit.
- **`Harvest Log.md` carries a log entry whose own heading reads `### CR-231, new: after the teardown...`.** That is a log entry quoting a claim header, not a claim. A counter that scans every `.md` in this folder rather than the 11 topic files counts it and returns **1,247**. `bin/Sync-TeamRepo.ps1` does exactly that, so every sync commit message it has written overstates the codex by one.

**The method that is right: the 11 topic files only, matching the id on a word boundary so a letter suffix still counts.** Worth fixing the sync script's regex and scope so the two counters agree."""

t = HL.read_text(encoding="utf-8")
start = t.index("**The claim count, and the 2026-09-18 correction went the wrong way.**")
end = t.index("both the tier and status columns summing to 1,245.") + len("both the tier and status columns summing to 1,245.")
t = t[:start] + HL_NEW + t[end:]

t = t.replace(
    "Backlog 0. Codex now holds 1,245 claim entries, 6 of them from this run. No law changed. One reading rule added, and one number this engine published twice is corrected.**",
    "Backlog 0. Codex 1,240 to 1,246, 6 of them from this run. No law changed, one reading rule added.**",
    1)
HL.write_text(t, encoding="utf-8")
print("Harvest Log corrected; stale 1,245 remaining:", t.count("1,245") - 1)

RUN_NEW = """## The count, and a correction to this run's own first draft

**The codex holds 1,246 claims across the 11 topic files.** 112 T1, 126 T2, 850 T3, 158 T4. 1,139 active, 101 contested, 5 superseded, 1 refuted. Both columns sum to 1,246, all 1,246 ids distinct, every heading carrying a Tier line. **2026-09-18 published 1,240 and 1,240 was right. 1,240 + 6 = 1,246.**

**This run first published 1,245 and wrote into three files that commit `7146475` had corrected 1,239 up to 1,240 in the wrong direction. That was this run's error.** It was caught by `bin/Sync-TeamRepo.ps1` printing 1,247 at the end of the run, which forced a third count.

Two traps, pulling opposite ways:

| Trap | Effect | Who hits it |
|---|---|---|
| `MD-019b`, the codex's only sub-lettered id | A regex requiring a space straight after the digits drops a real claim | This run's counter, returning 1,245 |
| `Harvest Log.md` line 669, `### CR-231, new: after the teardown...`, a log entry quoting a claim header | A counter scanning every `.md` in the science folder counts a non-claim | `bin/Sync-TeamRepo.ps1`, returning 1,247 |

**Correct method: the 11 topic files only, matching the id on a word boundary so a letter suffix still counts.**

**Action for tomorrow: fix `bin/Sync-TeamRepo.ps1` line 85.** It scans `Get-ChildItem $codexDst -Filter '*.md'` with `^### [A-Z]{2}-\\d`, so it counts the Harvest Log heading. Every sync commit message it has written overstates the codex by one."""

t = RUN.read_text(encoding="utf-8")
start = t.index("## The count correction, and yesterday's correction went the wrong way")
end = t.index("1,239 + 6 = 1,245.") + len("1,239 + 6 = 1,245.")
t = t[:start] + RUN_NEW + t[end:]
t = t.replace("Codex 1,239 to 1,245. No law changed.** Yesterday's published count of 1,240 is corrected below.",
              "Codex 1,240 to 1,246. No law changed.**", 1)
RUN.write_text(t, encoding="utf-8")
print("run log corrected; stale 1,245 remaining:", t.count("1,245") - 1)
