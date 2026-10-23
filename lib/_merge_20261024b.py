# -*- coding: utf-8 -*-
"""2026-10-24 research merge, pass 2: MD-187, the MD-171 pattern note, AT-132."""
from pathlib import Path

W = Path(r"E:\claude code marketing skill\Obsidian God-level Marketing Vault\God-level Marketing\wiki\science")
SRC = ('Meta for Business News, "you-dont-beat-the-auction-you-brief-it", Best Practice, '
       'dated 21 October 2026, read in full 2026-10-24 in the Playwright browser')


def edit(fname, anchor, insert, before=True):
    p = W / fname
    t = p.read_text(encoding="utf-8")
    if t.count(anchor) != 1:
        raise SystemExit("ANCHOR count=%d in %s: %r" % (t.count(anchor), fname, anchor[:80]))
    p.write_text(t.replace(anchor, (insert + anchor) if before else (anchor + insert)),
                 encoding="utf-8")
    print("OK  %s  (+%d chars)" % (fname, len(insert)))


def append(fname, block):
    p = W / fname
    t = p.read_text(encoding="utf-8")
    head = block.split("\n", 1)[0].split(" \u00b7 ")[0]
    if head in t:
        raise SystemExit("%s already present" % head)
    p.write_text(t.rstrip("\n") + "\n\n" + block.rstrip("\n") + "\n", encoding="utf-8")
    print("OK  %s  %s appended" % (fname, head))


# ------------------------------------------- MD-171, the sixth instance
md171 = """
**2026-10-24, the sixth instance, and it carries a new failure mode: a footnote MARKER with no footnote.** The Peak Season 2026 best-practice post opens on "Last peak season, 42% of shoppers said they planned to spend less. They spent 4.2% more." A superscript **1** sits on that sentence. The page was checked in the browser for a footnote block, a sources line, a "Meta internal data" line and the whole rendered tail: **there is none.** The marker promises a provenance that does not exist on the page, which is worse than MD-171's original case, where no marker was offered in the first place. The same post's other figure, about 28% more expensive per purchase below fifty conversions a week, is footnoted only by the words "in our analysis" (see [[Learning & Signal#LS-001|LS-001]], 2026-10-24).
**The running tally, because the pattern is now the finding.** [[Meta Delivery & Andromeda#MD-171|MD-171]], [[Meta Delivery & Andromeda#MD-177|MD-177]], [[Marketing Math & Unit Economics#MM-230|MM-230]], [[Meta Delivery & Andromeda#MD-181|MD-181]], [[Attribution & Incrementality#AT-131|AT-131]] and this one. Six Meta pages in seven weeks carrying numbers with no population and no counterfactual. **Treat an unfootnoted Meta figure as the default expectation rather than as an exception worth noting each time.**
**The 42% against 4.2% is worth keeping as a DIRECTION and never as a pair of digits**, because what it describes is real and matters for peak season: stated spending intent runs below actual spending, so a survey-led budget plan under-provisions. Carry that sentence. Do not carry either number, and never put them in a client plan.
Added source: {src}
""".format(src=SRC)
edit("Meta Delivery & Andromeda.md",
     "Sources: Meta for Business, Advertising Week New York 2026, 2026-10-06, footnote presence verified absent",
     md171)

# ------------------------------------------- MD-187 (new)
md187 = """### MD-187 \u00b7 Meta states the optimisation event decides WHICH CREATIVE WINS, not only who gets reached: same ads, same budget, different winner
Tier: T1 for the sentence \u00b7 Status: active
**The sentences, verbatim:** "None of this replaces the creative. It decides which creative wins. Brief the auction for volume and it finds the ad that brings cheap orders. Brief it for value and it finds the ad that brings big ones. Same ads, same budget, different winner, because you changed what winning meant." And earlier, on the same mechanism: "Volume tells the auction to find you more cautious planners. Value tells it to find you more confident buyers. Same budget, same audience, different people at the checkout."

**This codex has held the audience half of that for months and never the creative half from Meta.** The pool-swap mechanism is Nick Theriot's at [[Meta Delivery & Andromeda#MD-093|MD-093]]'s neighbour claim, that Meta holds users in event buckets and the optimisation event decides which bucket you are shown, asserted with no documentation. The amplification law is Charley T's at [[Meta Delivery & Andromeda#MD-093|MD-093]], that Andromeda executes the objective more literally each quarter so a shallow event degrades harder than it used to, also asserted. **Meta now states the first-party version of both, and adds the step neither operator took: the event choice re-ranks your existing creative against each other.** Its closing line is MD-093's law in Meta's own words: "The auction will do exactly what you asked. That's the good news and the bad news, and it's the same news."

**The precondition our own guard already names, and Meta skips it.** [[Creative Science]] records that writing creative to a high-value archetype only bites if the optimisation event carries VALUE, because on a volume objective the optimiser has no value signal to act on. Meta's sentence assumes the operator can choose value, which on a lead-gen account optimising for form fills they cannot. **So on our book the claim reads narrower: the event choice re-ranks creative wherever the event differs, and the volume-versus-value version of it is unavailable until a value signal exists in the account.**

**The measurement consequence, and it is the one that costs us money if ignored.** Our own creative read-outs are only comparable inside a single optimisation event, which is already the operating rule at [[Creative Science]]'s quality-grade findings. Meta has now supplied the mechanism for why: changing the event changes which ad the system picks, so a creative ranking carried across an event change is reading two different auctions. Any before-and-after on a batch that spans an event change is void.

**Evidence state.** No number, no test, no sample. Meta describing its own selection behaviour in a best-practice post.
Sources: {src}
Last touched: 2026-10-24
""".format(src=SRC)
append("Meta Delivery & Andromeda.md", md187)

# ------------------------------------------- AT-132 (new)
at132 = """### AT-132 \u00b7 Meta names its three attribution settings side by side and defines each in one line: standard counts what the ads TOUCHED, incremental counts what the ads ADDED, custom counts it the way the business already counts it
Tier: T1 \u00b7 Status: active
**The definitions, verbatim:** "Standard attribution counts what the ads touched. Incremental attribution counts what the ads added. Custom attribution counts it the way your business already counts it. Those are three different numbers. If the one you optimise against isn't the one your finance team uses, you're reading a different campaign from the one you're running."

**Why this is banked when [[Attribution & Incrementality#AT-001|AT-001]] through AT-006 already cover incremental attribution.** Everything on file about the incremental setting arrived through operators, mostly Andrew Faris and Blue Sense Digital, arguing about whether to switch and what the switch buys. **None of it is Meta stating the choice as a three-way selection with the third option named.** Custom attribution does not appear anywhere else in this file. The one-line definitions are also the cleanest statement of the distinction this codex holds, and they are quotable to a client, which almost nothing else in this topic is.

**The two sentences that do the operating work.** First, "The attribution setting is how you agree to be judged", from the same post's brief framing, which puts attribution inside the campaign setup rather than inside reporting. Second, "It's the decision most likely to be inherited rather than chosen." **That is the auditable one.** On any account we take over, the attribution setting was chosen by whoever built it and almost certainly never revisited, and it is now the setting Meta itself flags as the most likely to be stale.

**The circularity warning at [[Attribution & Incrementality#AT-003|AT-003]] still governs, and Meta's post does not mention it.** You cannot judge a change of attribution model from the column that model produces. The read-out for an attribution switch is store-level or CRM-level revenue over the switch window, not Ads Manager. Meta tells the operator the three numbers differ and does not tell them that comparing the three in-platform is reading the instrument against itself.

**Our book, plainly.** We run lead-gen accounts where the finance number is a closed sale weeks downstream and the Meta number is an opt-in. Meta's finance-team sentence is the right instinct and the mapping is not available to us in-platform at all, which is why the CRM count is the one we report. That is already the standing rule and this post is first-party support for it.

**Evidence state.** Definitions only. No number, no test, no statement of how the incremental model is fitted, and no eligibility floor named for any of the three.
Sources: {src}
Last touched: 2026-10-24
""".format(src=SRC)
append("Attribution & Incrementality.md", at132)
