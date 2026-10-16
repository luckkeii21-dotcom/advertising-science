# -*- coding: utf-8 -*-
"""2026-10-16 merge, part b: the AU-032 merge the first pass missed.

Part a assumed AU-033 follows AU-032. It does not: AU-033 sits at line 224
and AU-034 follows AU-032. Match on the next AU heading instead.
"""
import re
from pathlib import Path

SCI = Path(r"E:\claude code marketing skill\Obsidian God-level Marketing Vault\God-level Marketing\wiki\science")
P = SCI / "Auction Mechanics & Bidding.md"

au = P.read_text(encoding="utf-8")
assert "Ads Super Burst" not in au, "AU-032 merge already applied"

m = re.search(r"(### AU-032 ·.*?)(?=\n### AU-)", au, re.S)
assert m, "AU-032 block not found"
blk = m.group(1).rstrip("\n")
assert blk.count("Last touched:") == 1, blk.count("Last touched:")

ADD = (
    '**A 2026 reservation product arrived and it does not settle this, added 2026-10-16.** Meta moved Ads '
    'Super Burst to general availability in the United States in October 2026: a bookable 3-to-24-hour '
    'window with category exclusivity and "guaranteed delivery tied to those estimates", booked through '
    'Reach Planner. **Every outcome Meta publishes for it is a brand metric**, a median 2.9-point ad recall '
    'lift and a median 0.6-point intent lift, and there is no cost-per-result or conversion figure anywhere '
    'in the announcement. That is the shape this claim predicts: the guarantee is on delivery, never on '
    'performance. It does not verify the degraded-prospect mechanism above, which stays asserted and '
    'untested. Full product detail at [[Meta Delivery & Andromeda#MD-181|MD-181]].\n'
    'Last touched: 2026-10-16'
)

newblk = re.sub(r"Last touched: [0-9-]+", ADD, blk, count=1)
assert newblk != blk
au = au.replace(blk, newblk, 1)
P.write_text(au, encoding="utf-8")
print("wrote", P.name, len(au), "chars")
