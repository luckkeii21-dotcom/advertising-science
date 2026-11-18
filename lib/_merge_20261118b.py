# -*- coding: utf-8 -*-
"""LS-076 re-check amendment from the Muse Australia launch post, 2026-11-18."""
from pathlib import Path
import shutil

LS = Path(r"E:\claude code marketing skill\Obsidian God-level Marketing Vault\God-level Marketing"
          r"\wiki\science\Learning & Signal.md")

AMEND = (
    u"**Re-check number four, 2026-11-18, and the boundary still holds on the page.** Muse launched in "
    u"Australia on 17 November, the fourth Muse post this claim has read. It carries **no advertising "
    u"content at all**: the only occurrences of the word ads anywhere on the page are the site cookie "
    u"banner and a footer link. It also does not repeat the launch-day sentence banked above, so this is "
    u"an absence of contradiction rather than a renewal of the commitment. **What it does add is the "
    u"direction of the connectors, and the direction is the reassuring part.** Named Australian partners "
    u"include Canva, Domain, Kogan, MECCA, Officeworks, realestate.com.au, SWEAT, ShopBack and Ticketek, "
    u"and in every case a person's own agent reaches out to an app the person already uses. There is no "
    u"business onboarding, no lead capture, no business directory and no advertiser-facing surface. Nine "
    u"commerce and property brands can now be transacted with inside the agent while no advertiser can buy "
    u"placement in it, which is the state this claim predicts and the state most worth watching, because a "
    u"surface carrying purchase intent for nine named retailers is the one an ad system would eventually "
    u"want. Re-check again on the next Muse post."
)
SRC_ADD = (u"; Meta Newsroom, Muse Is Now Available in Australia: The World's First Personal AI Agent Built "
           u"for Everyone, 2026-11-17, about.fb.com/news/2026/11/muse-is-now-available-in-australia/, "
           u"read in full 2026-11-18 (no advertising content)")

txt = LS.read_text(encoding="utf-8")
i = txt.index("### LS-076 ")
j = txt.index("\nSources: Meta Newsroom, Introducing Muse", i)
eol = txt.index("\n", j + 1)
k = txt.index("\nLast touched: 2026-09-30", eol)
k_eol = txt.index("\n", k + 1)
assert "2026-11-18" not in txt[i:k]
new = (txt[:j] + "\n" + AMEND
       + txt[j:eol] + SRC_ADD
       + "\nLast touched: 2026-11-18" + txt[k_eol:])
shutil.copy(LS, str(LS) + ".bak-20261118")
LS.write_text(new, encoding="utf-8")
print("LS-076 amended")
