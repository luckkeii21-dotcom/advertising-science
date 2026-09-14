# -*- coding: utf-8 -*-
"""2026-09-14 research merge, part 2: the two amendments.
Part 1 aborted at the SC-024 edit because the short source-line anchor matched
four times in Scaling Models.md. Both amendments below use unambiguous anchors.
"""
import re
from pathlib import Path

SCI = Path(r"E:\claude code marketing skill\Obsidian God-level Marketing Vault\God-level Marketing\wiki\science")

SAM = "Sam Piliero, The Most Valuable Ecommerce Ads Training You'll Ever Watch, 2026-09-14"
FRA = "Fraser Cottrell, The Ultimate Guide to Static Image Ads (copy & scale), 2026-09-13"


def edit(fname, old, new, count=1):
    p = SCI / fname
    t = p.read_text(encoding="utf-8")
    assert t.count(old) == count, f"{fname}: anchor count {t.count(old)} != {count}"
    p.write_text(t.replace(old, new, count), encoding="utf-8")
    print("edited  ", fname)


# ==================================================== SC-024, amendment
SC024_SRC = ("Sources: Sam Piliero, The Only Facebook Ads Video You Need in 2026, 2026-07-26; "
             "Sam Piliero, Do THIS and the Meta Andromeda Algorithm Will LOVE You!, 2026-08-14; "
             "Sam Piliero, The BEST Facebook Ads Campaign Structure for 2026, 2026-07-05; "
             "Sam Piliero, 21 Facebook Ad Tricks to Improve Your ROAS INSTANTLY, 2026-05-15")

SC024_ADD = """**A FIFTH video adds the enforcement mechanism and, for the first time, the reason, 2026-09-14.** Every restatement above describes WHERE new ads go. This one describes what is done to make them deliver, and names the failure it exists to prevent: **a 7-day minimum budget is forced onto each new pack.** "The reason we set this 7-day minimum budget is because it forces for just 7 days budget against a new adset to give it a fair shot to see if it's actually scalable."

**The stated diagnosis is the part worth carrying.** "One of the biggest problems in the Andromeda algorithm that we have experienced is that when we launch new ads in existing campaigns, they get no spend and then we never know if the creative that we've spent so much time producing actually works. Occasionally, it ramps to the top on its own, but we always want to give it a little bit of a booster pad." So the pack rule is not only about protecting incumbents from tests. It is about a CBO refusing to fund anything unproven, with the minimum budget as the workaround. That converges with [[Scaling Models#SC-086|SC-086]] on consolidation starving committed spend, and it is the same problem [[Meta Delivery & Andromeda#MD-094|MD-094]] says Meta's own creative-testing tool solves by forcing minimum spend through chosen ads.

Also newly specified: each pack holds **one avatar and between two and eight creatives**, and packs are trimmed rather than paused wholesale, "you're pausing the bad, you're keeping the good". Still no performance data attached to any of it after five videos.
Added source: """ + SAM + """
"""

edit("Scaling Models.md", SC024_SRC, SC024_ADD + SC024_SRC)

# ==================================================== CR-031, amendment
# Append to the END of the CR-031 block, immediately before the next claim heading.
CR031_BODY = """
**The static-to-static threshold, added 2026-09-14.** This claim covers turning a static into a video. Fraser Cottrell states the rule for staying INSIDE the static format, and it is stricter than most variation practice: a headline swap on one design does not clear the bar. "Instead of just having that static and switching out the headline, we're building different designed ads, essentially different statics, but based around the same messaging... You want to make these assets as different as you can do, so Meta sees them as different assets."

So the unit being varied is the DESIGN and the thing held constant is the MESSAGE, which is the inverse of how most variation batches get built. His worked example is one message, a perfume line about claiming a scent before the group chat does, rendered as several visually unrelated statics including a call-out ad. He frames it as harder than it was: "with Meta's Andromeda changes, it can be a little bit harder. It's a bit more of a dance." Asserted from agency practice, no test shown, and it is the same threshold question left open at [[Creative Science#CR-172|CR-172]].
Added source: """ + FRA + """
"""

p = SCI / "Creative Science.md"
t = p.read_text(encoding="utf-8")
m = re.search(r"^### CR-031 ·.*?(?=^### )", t, re.S | re.M)
assert m, "CR-031 block not found"
block = m.group(0)
assert t.count(block) == 1, "CR-031 block is not unique"
t = t.replace(block, block.rstrip("\n") + "\n" + CR031_BODY, 1)
p.write_text(t, encoding="utf-8")
print("edited   Creative Science.md (CR-031 body)")

print("\nAMENDMENTS COMPLETE")
