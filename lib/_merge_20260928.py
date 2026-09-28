# -*- coding: utf-8 -*-
"""Claim merge for the 2026-09-28 research run.

Sources actually read in full by this run:
  * Blue Sense Digital, "How To Write Meta Ads That Scale: Copywriting Masterclass",
    2026-09-28, 181 min, 37,218 words. Whole transcript read.
  * Google Ads API v25.2 release notes plus the v25.2 announcement post. Both read at source.
  * Meta Marketing API changelog and the Ads in WhatsApp Status doc. Both read at source.
  * arXiv 2609.31045 (KuaFu), abstract read in full.
"""
import io, os, re

SCI = r"E:\claude code marketing skill\Obsidian God-level Marketing Vault\God-level Marketing\wiki\science"
TODAY = "2026-09-28"
BS = ("Blue Sense Digital, How To Write Meta Ads That Scale: Copywriting Masterclass, "
      "2026-09-28, youtube.com/watch?v=LoL1w-k9Mgg, 181 min, read in full")


def read(p):
    with io.open(os.path.join(SCI, p), encoding="utf-8") as f:
        return f.read()


def write(p, s):
    with io.open(os.path.join(SCI, p), "w", encoding="utf-8", newline="") as f:
        f.write(s)


def append(p, block):
    s = read(p)
    if not s.endswith("\n"):
        s += "\n"
    write(p, s + block)


def insert_before_sources(p, claim_id, para):
    """Insert a paragraph into an existing claim, just above its Sources: line."""
    s = read(p)
    h = "### %s " % claim_id
    i = s.find(h)
    if i < 0:
        print("MISS header", claim_id)
        return False
    j = s.find("\n### ", i + 1)
    if j < 0:
        j = len(s)
    body = s[i:j]
    m = list(re.finditer(r"\nSources: ", body))
    if not m:
        print("MISS Sources", claim_id)
        return False
    k = m[-1].start()
    body = body[:k] + "\n" + para.rstrip("\n") + body[k:]
    body = re.sub(r"\nLast touched: \d{4}-\d{2}-\d{2}", "\nLast touched: " + TODAY, body)
    write(p, s[:i] + body + s[j:])
    print("merged", claim_id)
    return True


def append_source(p, claim_id, src):
    s = read(p)
    h = "### %s " % claim_id
    i = s.find(h)
    if i < 0:
        print("MISS header", claim_id)
        return False
    j = s.find("\n### ", i + 1)
    if j < 0:
        j = len(s)
    body = s[i:j]

    def repl(mo):
        return mo.group(0).rstrip() + "; " + src

    body2, n = re.subn(r"(?m)^Sources: .*$", repl, body, count=1)
    if not n:
        print("MISS Sources line", claim_id)
        return False
    write(p, s[:i] + body2 + s[j:])
    return True


CS = "Creative Science.md"

CR124 = u"""
**THE SOURCE OF THE 80% RETRACTED IT, 2026-09-28, and this codex called it folklore first.** The FOLKLORE block above traced "the hook is 80% of performance" to Blue Sense (90% on 2026-01-08, 80% on 2026-01-29) and to Nick Theriot, graded all of it T4 on 2026-08-19, and named Ogilvy's print-headline observation as the likely origin. Blue Sense opened his 181-minute scripting masterclass by withdrawing it in his own words: "I have said quite often that the hook is 80% of performance. I said this in my creative strategy video as well... This is not true. This wording is actually bad by me. The hook is not driving 80% of performance."

**The replacement he offers is narrower and it survives.** "The hook is 80% of the AUDIENCE. Roughly none of it is persuasion. And so the hook is selling no one. No one gets sold by the hook. There's nowhere near enough scripting within the first 3 seconds to actually be able to sell someone." One exception he allows: a category where a genuinely prevalent unique mechanism can be stated inside the opening line.

**The operating consequence he draws, which is the reason the retraction matters.** "If the objective is to sell... you need to actually focus on the other 57 seconds of the 60-second script." He reports scraping 360 YouTube transcripts on how to write ads while preparing this video and finding that 70 to 75% of their total runtime went to hooks, which he reads as the market optimising the beat that selects the audience and ignoring the beats that do the selling.

**What moves and what does not.** The audience-selection half of this claim is unchanged and still carries the production arithmetic and the fatigue-revival cases above. The persuasion half is now withdrawn by its own source. Nothing here touches the open empirical question, which is still whether re-cutting the first 3 to 5 seconds of an EXISTING shoot revives a fatigued winner. Status stays contested, because the 80%-of-audience figure is itself still a rule of thumb with no retention curve behind it."""

CR136 = u"""
Restated from the primary text and turned into a gate, 2026-09-28. Blue Sense quotes the Schwartz passage directly ("copy cannot create desire for a product, it can only take the hopes, dreams, fears and desires that already existed in the hearts of millions of people and focus those already existing desires onto a particular product") and converts it into a test a brief either passes or fails: **if you cannot find evidence for the underlying desire somewhere outside your own marketing, in a review, a support ticket, a Reddit thread or a call recording, you do not have a concept.** What you have is a product description with a hook stapled to the front. His diagnosis of the common failure is that almost every brief starts at the product and reverse-engineers a reason to care, which he names as the specific thing that produces flat copy the audience has already seen from every competitor. Worked example: a shampoo client's messaging was "gentle shampoo for sensitive scalps" until the review and support corpus turned up a recurring fragrance-without-histamine-reaction theme, which rewrote the line to "every fragrance-free shampoo I tried still sets my histamines off, this one didn't". Single account, no numbers, so T3 for the example and no tier change to the law."""

CR230 = u"""
**A six-property scoring version of the same decision, 2026-09-28, plus the diagnosis that makes it worth running.** Blue Sense arrives at the identical rule from the other end and adds a scorecard. Sequence: write the script first, then find the **load-bearing beat**, the one doing most of the persuading, then score candidate surfaces on six properties and pick the surface that can hold that beat.

The six properties: can it carry a believable human face; can it show what a camera cannot; do you control the order in which it is received; can you assume sound; will it hold attention long enough to develop something; does it read as a person rather than as an advertisement.

Which beat each property serves: the face serves problem and proof; showing the unshowable serves mechanism and sometimes proof; controlling the order serves promise onward; sound serves nearly all of them; holding attention serves problem, mechanism and offer; reading as a person serves hook and problem.

Where the load-bearing beat sits by product type: an invisible edge (supplement, multivitamin) puts it on the mechanism; a visibly demonstrable edge puts it on proof; a differentiated terms structure puts it on the offer. His framing of why this is not a format question: "the beat that's important is a property of the proposition, not the format."

**The diagnosis, and it is the useful part.** "Every format failure that I've seen is typically part of the script that's placed on a format that can't hold it. So it's not actually a production failure. It's typically a writing failure that ends up looking like a production failure, which is exactly why it keeps getting sent back to the editor on multiple revisions." Two named mismatches: a proposition resting on proof should not go on a surface with no believable face, and a proposition resting on an invisible mechanism should not be a talking head.

Three surfaces scored as worked examples. Live action, one person to camera: face yes, unshowable no, order yes, sound yes, sustains attention weakly, reads as a person only if the talent is not obviously acting. Drawn or AI animation: face no, unshowable yes, order yes, sound yes, sustains attention well, reads as a person yes. Long-form native static: face no, order no because the eye path is out of your control, sound no, sustains attention yes, reads as a person better than either of the others. His closing constraint is that none of the three outperforms the others in general, and there are long-form statics, rendered ads and live-action ads that have each spent millions. T3, asserted from managed spend he puts at about $1M a day, no per-format numbers shown."""

CR114 = u"""
**The same lock-and-vary machine expressed as a concept grid, 2026-09-28, and it answers the "we need 50 ads a week" objection without re-running research each time.** Blue Sense defines a concept as **persona x angle x offer** and treats research as a batched input to the grid rather than a per-ad cost. His arithmetic, which he calls deliberately conservative: two personas crossed with three angles that fit them gives six concepts, and ten ads per concept gives sixty ads off one research pass. Volume at constant concept comes from three moves he names in order: entirely different scripts against the same persona and angle, hook swaps (justified by the audience-share half of [[Creative Science#CR-124|CR-124]]), and format variation, where the same persona, angle and research ship as a VSL, an animation, UGC, EGC and a founder story. He counts the format layer as delivery-visible diversity in the account. No hit rate attached, so T3, and the grid is a planning device rather than a measured result."""

CR127 = u"""
Corroborated and given its failure mechanic, 2026-09-28, by the same operator. Blue Sense states the rule as a hard sequencing constraint rather than a preference: **do not name the product before the mechanism has been introduced and understood.** His worked case is electrolytes, where naming the category early drops you into the undifferentiated pool and hands the decision to price, and where the fix is to spend the mechanism beat on something in the formulation, the supply chain or the manufacturing process before the category word is said at all. The mechanic he attaches is a retention discontinuity rather than a slow decay: "nothing will make you scroll past an ad faster than watching a storytime video... and then 5 seconds in suddenly obviously becomes an ad. What you don't want is product awareness to go from zero to 100 immediately." His prescribed shape is the one organic content already uses, random thought, small complaint, personal story, then the product, and he allows the product to appear visually one or more lines before it is named. The bridge machinery this sits inside is [[Creative Science#CR-272|CR-272]]."""

CR206 = u"""
**Why a long-running competitor ad does not transfer, stated as a mechanism rather than as a caution, 2026-09-28.** Blue Sense takes the common shortcut head on, which is to sort a competitor's Ad Library by longevity and run the longest-running ad on the assumption it carries the most spend. His objection is that longevity is a fact about a system and not about a script: "that ad works for that brand at that spend level against that audience that they're talking to with that level of existing belief in that brand's name." He points at the observable consequence, which is that nine-figure accounts visibly hold large spend on mediocre ads. **The transfer failure named:** "when you steal someone's ad... you don't inherit their entire belief chain that they've built in their consumers and target demographic, their brand recognition, their proof assets, and they're all the things that do most of the hard work." This sharpens the rule already in this claim rather than replacing it. Diagnosing WHICH variable won is necessary and still not sufficient, because some of the winning variables are account properties that cannot be copied at all. T3, reasoning from managed spend, no test shown."""

for cid, para in (("CR-124", CR124), ("CR-136", CR136), ("CR-230", CR230),
                  ("CR-114", CR114), ("CR-127", CR127), ("CR-206", CR206)):
    insert_before_sources(CS, cid, para)
    append_source(CS, cid, BS)

print("merges done")
