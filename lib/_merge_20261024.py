# -*- coding: utf-8 -*-
"""2026-10-24 research merge. One source: Meta for Business News best-practice
post "Peak Season 2026: You Don't Beat The Auction. You brief it.", dated
21 October 2026, read in full in the browser (plain fetch returns HTTP 400)."""
from pathlib import Path

W = Path(r"E:\claude code marketing skill\Obsidian God-level Marketing Vault\God-level Marketing\wiki\science")
SRC = ('Meta for Business News, "you-dont-beat-the-auction-you-brief-it", Best Practice, '
       'dated 21 October 2026, read in full 2026-10-24 in the Playwright browser')


def edit(fname, anchor, insert, before=True):
    p = W / fname
    t = p.read_text(encoding="utf-8")
    if t.count(anchor) != 1:
        raise SystemExit("ANCHOR count=%d in %s: %r" % (t.count(anchor), fname, anchor[:80]))
    t = t.replace(anchor, (insert + anchor) if before else (anchor + insert))
    p.write_text(t, encoding="utf-8")
    print("OK  %s  (+%d chars)" % (fname, len(insert)))


# ---------------------------------------------------------------- LS-001 merge
ls001 = """
**2026-10-24: Meta publishes the FIRST first-party performance number attached to this threshold, and it is a cost penalty rather than a definition.**
Every figure on this claim until today was either Meta documenting the exit CONDITION or an operator disputing the number from their own book. The post states: "Give each ad set enough volume to learn from. Roughly fifty conversions a week. Below that the system is guessing. In our analysis, ad sets under that threshold ran about **28% more expensive per purchase**."
**Three things that number does, in order of how much they matter.**
**One, it moves the threshold from a status gate to a price.** Theriot's position at [[Learning & Signal#LS-005|LS-005]] is that clearing the label changes nothing, and Meta has now put a number on the other side of that argument for the first time. It does not settle it, because a cost difference between sub-50 and over-50 ad sets is also a difference between small accounts and large ones, which is the identical selection defect catalogued at [[Meta Delivery & Andromeda#MD-171|MD-171]].
**Two, the evidence state is the weakest on this page.** "In our analysis" is the whole footnote. No population, no window, no sample, no spend band and no control. The page also carries a superscript footnote marker on a different figure with no footnote text anywhere on it, recorded at MD-171. **So carry the direction and never the 28%.** It does not go in a client deck and it does not go in a forecast.
**Three, our own book is the population it least describes.** Every lead-gen account we run sits permanently below fifty, per [[Learning & Signal#LS-060|LS-060]] and the 90% figure above. If the 28% were real and causal on our accounts it would be a permanent tax none of them can spend their way out of, which is the reading [[Learning & Signal#LS-063|LS-063]] exists to replace. **The operating line does not change: four operators say stop editing an ad set to chase the number, and today's post agrees with them on the prescription even while it prices the threshold.** Its own instruction is "Then do the hard part. Leave it alone."
Added source: {src}
Last touched: 2026-10-24

""".format(src=SRC)
edit("Learning & Signal.md",
     "### LS-002 \u00b7 Six edits always reset the learning phase", ls001)

# ---------------------------------------------------------------- LS-089, LS-090 (new)
ls089 = """### LS-089 \u00b7 Meta publishes an ad-set COUNT formula off the 50-conversion threshold, weekly budget / (cost per result x 50), and says most accounts exceed it
Tier: T1 for the sentence \u00b7 Status: active
**The formula, verbatim:** "Total weekly budget \u00f7 (cost per result \u00d7 50) = the most ad sets your budget can support". Then: "Most accounts are running more than that. Which means most accounts have written a brief with more objectives than they have money to pursue."

**Why this is its own claim and not a restatement of [[Learning & Signal#LS-001|LS-001]].** LS-001 is the exit condition. This is a STRUCTURE constraint derived from it, and it is the first time Meta has published the derivation rather than leaving operators to do it. It lands where the practitioner gate at [[Learning & Signal#LS-035|LS-035]] already sits, where Charley T caps a CBO at three ad sets conditional on the budget clearing learning for all three, and where Ben Heath's arithmetic says one campaign at 50 conversions a week beats two at 25 each. **Meta and our two most structure-focused operators now arrive at the same rule from opposite directions.**

**The awkward part, and it is the reason to read this claim before quoting either side.** This is the exact back-propagation Blue Sense Digital names as one of four common mistakes below $50k a month, inside LS-001's "CONTESTED ON USE, NOT ON FACT" paragraph: "setting budgets at the adset level based on the 50 conversions in a 7-day window rule". His worked objection is that 50 conversions in 7 days at a $100 expected CPA implies $714 a day for one concept ad set, so five to ten concurrent tests demand $3,500 to $7,000 a day of test budget alone, and his replacement is (target conversions x expected CPA) / test duration in days. **So the contest at LS-001 is no longer practitioner-versus-documentation. It is practitioner-versus-Meta's-published-arithmetic, and Meta has taken the side he calls a mistake.**

**The reconciliation that holds, because the two are answering different questions.** Meta runs the arithmetic FORWARDS from a budget you already have and returns a ceiling on ad set count. Blue Sense runs it BACKWARDS from the threshold to a budget you must go and find, and rejects that direction. Forwards it is a structure constraint and it is useful on every account we run. Backwards it is a spend requirement in disguise, which is [[Learning & Signal#LS-060|LS-060]]. **Use it to decide how many ad sets to run. Never use it to decide what to spend.**

**Evidence state.** The formula is arithmetic and proves nothing by itself. "Most accounts are running more than that" is a population claim with no number, no sample and no source. The 28% cost figure the threshold half rests on is unfootnoted, see LS-001, 2026-10-24.

**Free check on our own book, and it costs one spreadsheet column.** Run the formula on every client account we manage: weekly budget, current cost per opt-in, times fifty, compared against the live ad set count. [[Learning & Signal#LS-060|LS-060]] predicts the answer will be close to one ad set on most of them. Confirming that with our own numbers turns a T1 sentence into an audit instrument.
Sources: {src}
Last touched: 2026-10-24

""".format(src=SRC)

ls090 = """### LS-090 \u00b7 Meta states every edit costs TWICE, the restarted learning phase plus the old instruction spending at full price the whole time it was wrong, and only the first cost appears on screen
Tier: T1 for the sentences, T4 for the behavioural diagnosis \u00b7 Status: active
**The sentences, verbatim:** "Change a campaign and you pay twice. Once for the learning phase you restarted, while the system works out what the new instruction means. And once for the old instruction, which was live and spending at full price the whole time you had it wrong." And: "Only one of those costs appears on screen. The learning phase comes with a warning on it. The other one appears nowhere. Your account has no idea what the other version would have banked."

**What is new is the SECOND cost, and this codex has never stated it.** [[Learning & Signal#LS-002|LS-002]] holds the six edits that reset learning and [[Learning & Signal#LS-006|LS-006]] holds Meta's avoid-unnecessary-edits guidance. Both price the cost of changing. Nothing on file prices the cost of NOT changing. Meta names it and names why it stays invisible: the learning phase carries a label and the counterfactual carries nothing.

**The behavioural consequence Meta draws, and it is the useful half.** "So people fear the visible cost and ignore the invisible one. They leave a bad brief running because changing it feels risky. Then they tinker with a good one because tinkering feels like work." Read against the editing-discipline claims this cuts both ways. The 10-day interval and the 3-to-5-day freeze at [[Learning & Signal#LS-006|LS-006]] protect against tinkering with a good setup, and they are not a reason to leave a wrong optimisation event running. **The rule out of the pair: a freeze protects a brief you chose, never a brief you inherited.**

**The prescription, and it is cheap and new.** "Group your changes. If you're going to rebrief, do it all at once. Take one learning phase instead of five. Then hold it still." One learning phase priced against five, from the platform, and directly actionable on an account where several things are wrong at once. It also sharpens the LS-001 finding that what damages a sub-threshold ad set is the editing done in pursuit of the threshold: batching cuts the number of resets without cutting the number of changes made.

**And the framing the whole post rests on, banked because it generalises past this post.** "Every campaign you set up is a brief. The optimisation event is the ask. The budget is the constraint. The bid strategy is the definition of success. The attribution setting is how you agree to be judged." Then the asymmetry that makes it more than an analogy: "Brief a person and they ask questions... The auction never asks. It accepts everything. It reads what you wrote, decides you meant it, and goes and buys it." And: "A bad brief to a person starts an argument. A bad brief to the auction produces a perfectly executed wrong answer, delivered on time and inside budget."

**Evidence state.** No number anywhere in this claim. Every sentence is Meta describing its own system and its own advertisers' behaviour, with no study, no sample and no measurement attached.
Sources: {src}
Last touched: 2026-10-24
""".format(src=SRC)

p = W / "Learning & Signal.md"
t = p.read_text(encoding="utf-8")
if "### LS-089" in t or "### LS-090" in t:
    raise SystemExit("LS-089/090 already present")
p.write_text(t.rstrip("\n") + "\n\n" + ls089 + ls090 + "\n", encoding="utf-8")
print("OK  Learning & Signal.md  LS-089 + LS-090 appended")
