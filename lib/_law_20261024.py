# -*- coding: utf-8 -*-
"""2026-10-24: replace the hot-layer lead paragraph in SKILL.md."""
from pathlib import Path

P = Path(r"E:\claude code marketing skill\.claude\skills\advertising-science\SKILL.md")
lines = P.read_text(encoding="utf-8").split("\n")

i = next(n for n, l in enumerate(lines) if l.startswith("Updated only when the codex changes at law level."))
assert "2026-10-23 pass" in lines[i], lines[i][:120]

lines[i] = (
    "Updated only when the codex changes at law level. Each law cites its claims; depth lives in the codex. "
    "**The 2026-10-24 pass put a PRICE on the 50-conversion threshold for the first time, and the price comes from Meta** "
    "(3 new claims: LS-089, LS-090, MD-187, plus AT-132; merges into LS-001 and MD-171). "
    "Zero transcripts came in. The whole day's haul is one Meta for Business best-practice post, "
    "\"Peak Season 2026: You Don't Beat The Auction. You brief it.\", dated 21 October 2026. "
    "**Three things in it change how we read settings we already manage.** "
    "**One, the threshold now has a cost attached: \"ad sets under that threshold ran about 28% more expensive per purchase\", "
    "and its entire footnote is the words \"in our analysis\".** No population, no window, no sample, no control. "
    "Carry the direction and never the 28%, because the comparison between sub-50 and over-50 ad sets is also a comparison "
    "between small accounts and large ones, which is the selection defect MD-171 exists to catch. "
    "It does not move the operating line: four operators say stop editing an ad set to chase the number, and this post agrees, "
    "\"Then do the hard part. Leave it alone.\" "
    "**Two, Meta published the ad-set COUNT formula, `weekly budget / (cost per result x 50)` = the most ad sets the budget supports, "
    "and says most accounts exceed it (LS-089).** That is the exact back-propagation Blue Sense Digital calls one of four common "
    "mistakes below $50k a month, so the contest at LS-001 is now practitioner-versus-Meta rather than practitioner-versus-documentation. "
    "**The reconciliation: run it forwards to cap ad set count, never backwards to set spend.** Forwards it is a structure constraint "
    "useful on every account we have; backwards it is LS-060, a spend requirement in disguise. "
    "**Three, Meta states that the optimisation event decides WHICH CREATIVE WINS, not only who gets reached: "
    "\"Same ads, same budget, different winner, because you changed what winning meant\" (MD-187).** "
    "We held the audience half of that from practitioners and never the creative half from Meta. "
    "The measurement consequence is the expensive one: a creative ranking carried across an optimisation-event change is reading two "
    "different auctions, so any before-and-after spanning an event change is void. "
    "**Also banked: every edit costs twice, the restarted learning phase plus the old instruction spending at full price the whole time "
    "it was wrong, and only the first cost appears on screen (LS-090).** The prescription is to batch the changes, "
    "\"Take one learning phase instead of five\", and the rule that falls out of it is that a freeze protects a brief you chose, "
    "never a brief you inherited. "
    "**And the reading rule hardens again.** This is the sixth Meta page in seven weeks carrying numbers with no population and no "
    "counterfactual, and it adds a new failure mode: a superscript footnote marker with no footnote text anywhere on the page. "
    "**An unfootnoted Meta figure is now the default expectation, not an exception worth remarking on.**"
)

P.write_text("\n".join(lines), encoding="utf-8")
print("OK  SKILL.md hot layer lead paragraph replaced (line %d)" % (i + 1))
