# -*- coding: utf-8 -*-
"""Watch-item amendment for the 2026-10-19 research run.

The enhancement-audit watch item is the right home for the three June 2026
Advantage+ enhancements banked today at MD-183, so the account audit stays on
one list instead of two.
"""
from pathlib import Path

SKILL = Path(r"E:\claude code marketing skill\.claude\skills\advertising-science\SKILL.md")
ANCHOR = "Do not flip it on a high-spend healthy account."

ADD = (
    " **Three more enhancements joined the audit list on 2026-10-19 and they are a different kind: "
    "they change the asset itself** (MD-183, T1, Meta's own out-of-cycle change notes of 28 June "
    "2026). Image Animation turns a static image into a short animated video, Video Filter applies "
    "colour changes including standard-to-high-dynamic-range conversion, and Video Uncrop expands a "
    "video to fill taller placements instead of cropping or letterboxing it. Each is controlled per "
    "creative through `image_animation`, `video_filtering` and `video_uncrop` inside "
    "`degrees_of_freedom_spec.creative_features_spec`. **Unlike Flex Media, the change notes do NOT "
    "say whether any of them starts on, so the default state is genuinely unknown and has to be read "
    "off a live ad rather than guessed.** Add all three fields to the same account audit that reads "
    "Flex Media, Related details and Related media. Uncrop is the one to read first: reframing a "
    "composition to fill a vertical surface is the exact failure our whole-subject-in-frame rule "
    "exists to stop, and a dealership ad that loses the back of the truck is a worse ad whatever it "
    "does to delivery. No performance evidence exists either way on any of the three."
)

s = SKILL.read_text(encoding="utf-8")
assert s.count(ANCHOR) == 1, s.count(ANCHOR)
s = s.replace(ANCHOR, ANCHOR + ADD, 1)
SKILL.write_text(s, encoding="utf-8")
print("watch item amended, +", len(ADD), "chars")
