# -*- coding: utf-8 -*-
"""Claim counter. Pairs each claim heading with the Tier line directly beneath it,
scoped to the 11 topic files only (never the Harvest Log, which contains
claim-shaped headings). Method fixed 2026-09-11.
"""
import re
from pathlib import Path

SCI = Path(r"E:\claude code marketing skill\Obsidian God-level Marketing Vault\God-level Marketing\wiki\science")

TOPICS = [
    "Meta Delivery & Andromeda.md", "Auction Mechanics & Bidding.md",
    "Learning & Signal.md", "Creative Science.md", "Scaling Models.md",
    "Attribution & Incrementality.md", "Google Auction & Smart Bidding.md",
    "Google PMax & Shopping.md", "TikTok Delivery.md", "Emerging Channels.md",
    "Marketing Math & Unit Economics.md",
]

HEAD = re.compile(r"^### ((?:MD|AU|LS|CR|SC|AT|GA|GP|TT|EC|MM)-\d+[a-z]?)\b")
tiers = {"T1": 0, "T2": 0, "T3": 0, "T4": 0}
stat = {"active": 0, "contested": 0, "superseded": 0, "refuted": 0}
total = 0
missing = []

for f in TOPICS:
    lines = (SCI / f).read_text(encoding="utf-8").splitlines()
    n = 0
    for i, ln in enumerate(lines):
        m = HEAD.match(ln)
        if not m:
            continue
        total += 1
        n += 1
        nxt = lines[i + 1] if i + 1 < len(lines) else ""
        if not nxt.startswith("Tier:"):
            missing.append(f"{f}:{i+1} {m.group(1)}")
            continue
        t = re.search(r"\bT([1-4])\b", nxt)
        tiers["T" + t.group(1)] += 1 if t else 0
        s = re.search(r"Status:\s*(\w+)", nxt)
        if s and s.group(1) in stat:
            stat[s.group(1)] += 1
    print(f"{n:5d}  {f}")

print()
print("TOTAL", total)
print("tiers", tiers, "sum", sum(tiers.values()))
print("status", stat, "sum", sum(stat.values()))
if missing:
    print("HEADINGS WITH NO TIER LINE BENEATH:")
    for x in missing:
        print("  ", x)
