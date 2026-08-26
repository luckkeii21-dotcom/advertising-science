"""2026-08-27: fix the stale client roster the 2026-08-26 teacher log flagged for this run,
and correct the chiropractic account count introduced in MD-139 earlier in this same pass."""
import io
from pathlib import Path

SCI = Path(r"E:\claude code marketing skill\Obsidian God-level Marketing Vault\God-level Marketing\wiki\science")

# (file, old, new) - each must appear exactly once
EDITS = [
    ("Meta Delivery & Andromeda.md",
     '**COMPLIANCE, and this is why it lands harder on our book than on an ecommerce book. Four of our five accounts are chiropractic and sit under Meta\'s health rules.**',
     '**COMPLIANCE, and this is why it lands harder on our book than on an ecommerce book. TWO of our five accounts, ChiroWorks and Chiropraise, are chiropractic and sit under Meta\'s health rules.** *(Corrected in-pass 2026-08-27: this entry first read "four of our five", the same stale roster count the 2026-08-26 teacher log flagged. Mattia was offboarded 2026-07-24, so the health-rule exposure is two accounts.)*'),

    ("Meta Delivery & Andromeda.md",
     "ine is the one that applies to ChiroWorks, Chiropraise, Phoenix Truxx, SJR Commercial and Mattia.**",
     "ine is the one that applies to ChiroWorks, Chiropraise, Phoenix Truxx, SJR Commercial and MetaTechAI.** *(Roster corrected 2026-08-27: Mattia offboarded 2026-07-24, MetaTechAI onboarded 2026-08-22.)*"),

    ("Meta Delivery & Andromeda.md",
     "es without once being opened on ChiroWorks, Chiropraise, Phoenix Truxx, SJR Commercial or Mattia.**",
     "es without once being opened on ChiroWorks, Chiropraise, Phoenix Truxx, SJR Commercial or MetaTechAI.** *(Roster corrected 2026-08-27.)*"),

    ("Watchlist.md",
     "This matters because four chiropractic accounts depend on the health and personal-attributes sections.",
     "This matters because our chiropractic accounts, ChiroWorks and Chiropraise, depend on the health and personal-attributes sections. *(Count corrected 2026-08-27 from \"four\": Mattia was offboarded 2026-07-24.)*"),
]

for fname, old, new in EDITS:
    p = SCI / fname
    txt = p.read_text(encoding="utf-8")
    n = txt.count(old)
    if n != 1:
        print(f"SKIP ({n} matches): {fname} :: {old[:60]}")
        continue
    with io.open(p, "w", encoding="utf-8", newline="") as f:
        f.write(txt.replace(old, new, 1))
    print(f"fixed: {fname} :: {old[:60]}")

# report any surviving "Mattia" roster mentions across the science wing
print("\n-- surviving 'Mattia' mentions in science wing --")
for p in sorted(SCI.glob("*.md")):
    t = p.read_text(encoding="utf-8", errors="replace")
    if "Mattia" in t:
        print(f"  {p.name}: {t.count('Mattia')}")
