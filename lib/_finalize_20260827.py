"""Mark the 2026-08-27 pass's transcripts as extracted."""
import io
from pathlib import Path

T = Path(r"E:\claude code marketing skill\Obsidian God-level Marketing Vault\God-level Marketing\wiki\sources\transcripts")

FILES = [
    # today's harvest
    "ben-heath/2026-08-26--ben-heath--We have a new Facebook Ads problem.md",
    "nick-theriot/2026-08-26--nick-theriot--How To Lower Facebook Ads CPA in 2026 4 Things I Fix First.md",
    "jon-loomer/2026-08-26--jon-loomer--A Reflection on 15 Years.md",
    # bluesense batch A
    "bluesense-digital/2025-11-26--bluesense-digital--Why Youre Overspending on Retargeting How To Fix It.md",
    "bluesense-digital/2025-05-22--bluesense-digital--Heres Why You Need To Spend on Existing Customers.md",
    "bluesense-digital/2025-10-14--bluesense-digital--Heres How Much You Should Be Spending On Creative.md",
    "bluesense-digital/2025-03-03--bluesense-digital--How We Lowered A Brands CPCs by 10x on Meta in 30 Days.md",
    "bluesense-digital/2025-03-18--bluesense-digital--How To Fix High CPCs on Meta Ads.md",
    "bluesense-digital/2025-04-02--bluesense-digital--Meta Traffic Campaigns Destroys This Business.md",
    # bluesense batch B
    "bluesense-digital/2025-05-02--bluesense-digital--New Strategy To Scale Meta Ads Faster.md",
    "bluesense-digital/2025-09-10--bluesense-digital--Cold vs Warm Tactics on Meta Google Ads with Caden.md",
    "bluesense-digital/2025-04-16--bluesense-digital--Why Rolling Reach Doesnt Matter in eCommerce And What Actually Does.md",
    "bluesense-digital/2025-05-09--bluesense-digital--MER Is A Terrible KPI for Marketing.md",
    "bluesense-digital/2025-06-17--bluesense-digital--How to Trust Meta ROAS and Tie It Directly to Your PL.md",
    "bluesense-digital/2025-09-16--bluesense-digital--Why You Shouldnt Measure Results Daily or Even Monthly in eCommerce.md",
    "bluesense-digital/2025-04-14--bluesense-digital--Heres Why Your Should Turn Brand Search Off.md",
    # charley t + piliero
    "charley-t/2026-01-26--charley-t--Academy News 6 Q1 Reality Check VIP Loom Audits Roast My Ad Account Le.md",
    "charley-t/2025-12-28--charley-t--Meta MBA Just Opened Q5 Goldmine 1000 Templates Academy News 2.md",
    "charley-t/2026-01-06--charley-t--Q1 Strategy Blueprint Meta MBA Bonus New Masterclass Live Academy News.md",
    "sam-piliero/2026-05-18--sam-piliero--Claude Has Officially Changed Facebook Ads Forever Tutorial.md",
    # heath / loomer / solutions8 / shiver
    "ben-heath/2026-04-14--ben-heath--How To Spy On Your Competitors Meta Ads for FREE.md",
    "ben-heath/2026-04-21--ben-heath--How To Set Up A Meta Business Account in 2026.md",
    "jon-loomer/2026-05-04--jon-loomer--Dont Get Attached to Your Ad Process.md",
    "jon-loomer/2026-06-08--jon-loomer--Every Change You Make Should Solve a Problem.md",
    "solutions8/2025-09-15--solutions8--eCommerce Success with Demographic-Focused Creatives.md",
    "matt-shiver/2026-05-05--matt-shiver--I Trained Claude to Write My Facebook Ads My Exact Prompts.md",
]

ok = missing = already = 0
for rel in FILES:
    p = T / rel
    if not p.exists():
        print("MISSING:", rel)
        missing += 1
        continue
    txt = p.read_text(encoding="utf-8")
    if "extracted: true" in txt:
        already += 1
        continue
    if "extracted: false" in txt:
        txt = txt.replace("extracted: false", "extracted: true", 1)
    else:
        print("NO extracted FIELD:", rel)
        missing += 1
        continue
    with io.open(p, "w", encoding="utf-8", newline="") as f:
        f.write(txt)
    ok += 1

print(f"marked={ok} already={already} missing={missing} of {len(FILES)}")

# recount backlog
rows = [p for p in T.rglob("*.md") if "extracted: true" not in p.read_text(encoding="utf-8", errors="replace")]
print("remaining unextracted:", len(rows), "of", len(list(T.rglob('*.md'))))
