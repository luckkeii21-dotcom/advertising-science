# -*- coding: utf-8 -*-
"""2026-08-31: update the SKILL.md hot layer for the Google language-targeting removal."""
from pathlib import Path

P = Path(r"E:\claude code marketing skill\.claude\skills\advertising-science\SKILL.md")
b = P.read_text(encoding="utf-8")

OLD_REBUILT = "Updated only when the codex changes at law level. Each law cites its claims; depth lives in the codex. Last rebuilt: 2026-08-30 research pass (new law 24, and an arithmetic error corrected inside law 20's source claim), from **1,116 claims** (88 T1, 114 T2, 765 T3, 149 T4; 1,011 active, 99 contested, 5 superseded, 1 refuted) across 11 topic files. Counts recomputed from the topic files, not carried forward from the log."

NEW_REBUILT = "Updated only when the codex changes at law level. Each law cites its claims; depth lives in the codex. Last rebuilt: 2026-08-31 research pass (law 1a gains a documented Google half; no law retired), from **1,125 claims** (90 T1, 116 T2, 770 T3, 149 T4; 1,020 active, 99 contested, 5 superseded, 1 refuted) across 11 topic files. Counts recomputed from the topic files, not carried forward from the log."

assert OLD_REBUILT in b, "rebuilt line not found"
b = b.replace(OLD_REBUILT, NEW_REBUILT, 1)

ANCHOR = "**The 2026-08-27 TEACHER pass produced the first law in this file built on our own accounts rather than on a roster operator, and it says a number we quote every week is a coin flip.**"

NEW = """**The 2026-08-31 pass produced the first DOCUMENTED, DATED platform change that moves law 1a, and it is on Google rather than Meta.** Google is removing campaign-level language targeting from Search and from the Search Network portion of Performance Max in **September 2026**, next month. Google's own help page: "The campaign-level language targeting setting will be removed. **Search ads will automatically match based on the language of your ads.**" Existing language criteria stay on the campaign and stop working. Performance Max keeps the setting for YouTube, Display, Discover and Gmail, so one PMax campaign will run one channel on the ad's language and the rest on the old control. **Law 1a's control-versus-suggestion split has until now been read off Meta's screen by operators and inferred on Google. This is a platform stating it in writing with a date on it, and the direction is the one law 1a predicts: a hard control becomes an inference drawn from the creative.** It is the second Google instance in a month after Optimized Targeting (GA-066) and the PMax new-customer toggle (GP-042), and it is the strongest of the three because it is documented rather than observed. **Operating consequence: from September, an account built to keep Spanish creative in front of Spanish speakers is held there by the ad copy and the landing page, not by the setting** (GA-069, T1).
**The pass also got the thing this codex has asked five sources for, a page test that publishes its denominator, and the answer is worse than silence.** AT-106 closed the landing-page methodology gap in August with a negative: nobody on the roster states a sample size, a conversion floor or a confidence level. A CRO operator has now published five, on camera, off live dashboards. **All five are underpowered for the lift they report, by 1.59x to 7.63x** (AT-111). The best has 63% of the sample its own result needs; the worst has 13%. **The counter-intuitive half is the part to carry: a big sample does not rescue a small effect, because required sample scales with the inverse square of the effect.** The 250,000-visitor test reporting a 3.3% lift is the second-worst powered in the set; the 49,000-visitor test reporting 10% is the best. **Reading a results list and trusting the ones with big traffic numbers gets it exactly backwards.** AT-027 was recomputed against its own arithmetic in the same pass and **holds**: 40,000 sessions per arm at a 2.5% conversion rate detects a 12.5% relative lift, inside its stated 10-to-20% band. **Every one of those seven page changes is cheap and sensible and should probably be shipped. None of the percentages may be forecast from or quoted to a client as an expected lift.**
**A flagship claim that arrived pre-refuted by its own dashboard.** The same operator's headline is "the higher the shipping price, the higher the conversion rate". His readout says conversion rate +3.3%; ninety seconds later he describes the same test as "CVR is down with the two more expensive groups, revenue went up". **Those cannot all be true. Never repeat the headline.** The defensible version is that raising shipping price on a brand already charging for it did not cost revenue and probably raised margin (CR-210).
**The competitor-research instrument at CR-190 degraded and nobody had noticed.** The Ads Library now stamps creative with a "protected" watermark, and the operator reporting it says Claude and ChatGPT decline to work with the images because of it. T3, he sells the tool that fixes it, and it is checkable for free on our own competitor sets in five minutes (CR-209).

"""

assert ANCHOR in b, "anchor paragraph not found"
b = b.replace(ANCHOR, NEW + ANCHOR, 1)

P.write_text(b, encoding="utf-8")
print("SKILL.md hot layer updated")
