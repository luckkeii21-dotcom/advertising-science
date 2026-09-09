# -*- coding: utf-8 -*-
"""2026-09-09: law 1a gains the withdrawal of four ad-set hard controls; counts refreshed."""
from pathlib import Path

P = Path(r"E:\claude code marketing skill\.claude\skills\advertising-science\SKILL.md")
raw = P.read_bytes()
bom = raw.startswith(b"\xef\xbb\xbf")
t = raw.decode("utf-8-sig")

# 1. Preamble: lead with today's law-level change.
OLD_LEAD = ("Updated only when the codex changes at law level. Each law cites its claims; depth lives in the codex. "
            "**The 2026-09-07 pass EXTENDED law 11a past the ad platform**")
NEW_LEAD = ("Updated only when the codex changes at law level. Each law cites its claims; depth lives in the codex. "
            "**The 2026-09-09 pass AMENDED law 1a, and it is the first law-level change on this page driven by a "
            "platform withdrawing a control rather than by anyone learning anything** (MD-150 and MD-151, both T1, new; "
            "MD-016, SC-149, AU-076 and AU-019 amended). Law 1a's list of ad-set settings that genuinely bind is losing "
            "four members: placement, platform, device and operating-system EXCLUSION. Meta's in-product notice is live "
            "and quoted verbatim in MD-150, Meta has published no announcement, and the controls were still fully present "
            "in the one account we could read on 2026-09-09, so **nothing here licenses telling a client this has already "
            "happened to them.** No law was added and none retired. The previous law-level change was "
            "**the 2026-09-07 pass, which EXTENDED law 11a past the ad platform**")
assert t.count(OLD_LEAD) == 1, "lead anchor not unique"
t = t.replace(OLD_LEAD, NEW_LEAD)

# 2. Law 1a: add the withdrawal clause.
OLD_1A_TAIL = ("Operating consequence for our local clients: geo is the one targeting lever that still does what it says.")
NEW_1A_TAIL = (OLD_1A_TAIL +
               "\n**⚠ The CONTROLS side of this law is shrinking, added 2026-09-09 (MD-150, T1).** Meta's in-product "
               "notice reads: \"Excluding placements, platforms, devices and operating systems will no longer be "
               "available for your ad sets.\" Four hard controls, withdrawn at ad-set level. The replacement levers are "
               "a placement value rule, capped at a 90% bid decrease that suppresses delivery without ever switching a "
               "placement off and covering only seven placements, and an account-wide Placement Controls setting that "
               "cannot vary between two clients sharing an account (MD-151). **Location, minimum age and language are "
               "untouched, so the sentence above about geo still holds and gets stronger:** geo is now not merely the "
               "targeting lever that does what it says, it is close to the last ad-set setting that does. "
               "**Read MD-150's scope guards before repeating any of this to a client:** Meta has announced nothing, "
               "coverage on 2026-08-25 found the Business Help Centre still describing manual placement selection as "
               "available, the unofficial scope is Sales and Leads objectives only with sensitive verticals excluded, "
               "and our own 2026-09-09 account read found all four controls still present.")
assert t.count(OLD_1A_TAIL) == 1, "law 1a anchor not unique"
t = t.replace(OLD_1A_TAIL, NEW_1A_TAIL)

# 3. Counts.
OLD_COUNT = ("Built from **1,175 claims** (93 T1, 118 T2, 808 T3, 156 T4; 1,069 active, 100 contested, 5 superseded, "
             "1 refuted) across 11 topic files.")
NEW_COUNT = ("Built from **1,179 claims** (96 T1, 118 T2, 809 T3, 156 T4; 1,073 active, 100 contested, 5 superseded, "
             "1 refuted) across 11 topic files.")
assert t.count(OLD_COUNT) == 1, "count anchor not unique"
t = t.replace(OLD_COUNT, NEW_COUNT)

data = t.encode("utf-8")
if bom:
    data = b"\xef\xbb\xbf" + data
P.write_bytes(data)
print("SKILL.md updated: preamble, law 1a clause, counts 1,175 -> 1,179")
