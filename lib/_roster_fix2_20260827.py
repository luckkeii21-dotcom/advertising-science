"""2026-08-27 roster sweep, part 2: remaining offboarded-client references in the codex topic files.
The Harvest Log is append-only and is deliberately NOT touched."""
import io
import re
from pathlib import Path

SCI = Path(r"E:\claude code marketing skill\Obsidian God-level Marketing Vault\God-level Marketing\wiki\science")

EDITS = [
    ("Attribution & Incrementality.md",
     "ChiroWorks, Chiropraise, Phoenix Truxx, SJR Commercial or Mattia",
     "ChiroWorks, Chiropraise, Phoenix Truxx, SJR Commercial or MetaTechAI"),
    ("Meta Delivery & Andromeda.md",
     "A matched pair on ChiroWorks or Mattia,",
     "A matched pair on ChiroWorks or Chiropraise,"),
]

for fname, old, new in EDITS:
    p = SCI / fname
    txt = p.read_text(encoding="utf-8")
    n = txt.count(old)
    if n == 0:
        print(f"SKIP (0 matches): {fname} :: {old[:55]}")
        continue
    with io.open(p, "w", encoding="utf-8", newline="") as f:
        f.write(txt.replace(old, new))
    print(f"fixed {n}x: {fname} :: {old[:55]}")

print("\n-- final sweep: any surviving 'Mattia' outside the append-only Harvest Log --")
for p in sorted(SCI.glob("*.md")):
    if p.name == "Harvest Log.md":
        continue
    t = p.read_text(encoding="utf-8", errors="replace")
    for m in re.finditer(r"Mattia", t):
        s = max(0, m.start() - 90)
        print(f"  {p.name}: ...{t[s:m.end()+90]}...".replace("\n", " "))
