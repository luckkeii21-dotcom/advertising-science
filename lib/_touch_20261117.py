# -*- coding: utf-8 -*-
"""Bump Sources + Last touched on the three amended claims."""
from pathlib import Path

SCI = Path(r"E:\claude code marketing skill\Obsidian God-level Marketing Vault\God-level Marketing\wiki\science")
CR = SCI / "Creative Science.md"
AU = SCI / "Auction Mechanics & Bidding.md"

ADD = "; Andrew Faris, Breaking Down The Ad That Spent $3M Last Month, 2026-11-16 (Harry Dohmgeest speaking)"
ADD_AU = "; arXiv 2611.19074v1 TokenFormer V2, abstract read 2026-11-17"


def touch(path, claim_id, src_suffix):
    t = path.read_text(encoding="utf-8")
    i = t.find("### %s " % claim_id)
    assert i >= 0, claim_id
    j = t.find("\nLast touched:", i)
    assert j >= 0, claim_id
    k = t.find("\n", j + 1)
    s = t.rfind("\nSources:", i, j)
    assert s >= 0, claim_id
    s_end = t.find("\n", s + 1)
    sources_line = t[s + 1:s_end]
    if src_suffix.strip("; ") not in sources_line:
        sources_line = sources_line + src_suffix
    new = t[:s + 1] + sources_line + "\nLast touched: 2026-11-17" + t[k:]
    path.write_text(new, encoding="utf-8")
    print("touched", claim_id)


for cid in ("CR-245", "CR-273", "CR-277"):
    touch(CR, cid, ADD)
touch(AU, "AU-084", ADD_AU)
