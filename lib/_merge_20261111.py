# -*- coding: utf-8 -*-
"""2026-11-11 research merge. Source: Jon Loomer, "How I'm Using AI to Create
Meta Ads", 2026-11-11, read in full.
  - CR-291 new: the AI-creative control architecture.
  - CR-169 amended: first outright "better results" assertion, still no number.
  - MD-124: source added for the 10-asset capacity restatement.
  - transcript frontmatter extracted: false -> true
"""
import shutil
from pathlib import Path

SCI = Path(r"E:\claude code marketing skill\Obsidian God-level Marketing Vault\God-level Marketing\wiki\science")
CR = SCI / "Creative Science.md"
MD = SCI / "Meta Delivery & Andromeda.md"
TR = Path(r"E:\claude code marketing skill\Obsidian God-level Marketing Vault\God-level Marketing\wiki\sources\transcripts\jon-loomer\2026-11-11--jon-loomer--How Im Using AI to Create Meta Ads.md")

for p in (CR, MD):
    shutil.copy2(p, p.with_name(p.name + ".bak-20261111"))

CR291 = """
### CR-291 \u00b7 The only AI-creative control architecture on file that an operator says changed his own output: a written rule book updated on every correction, adversarial review roles including one reviewer whose sole job is catching AI-looking visuals, and the operator's own published corpus as the voice reference
Tier: T3 \u00b7 Status: active
**The problem he states first is a production problem, not a performance one**, and it is the one [[Meta Delivery & Andromeda#MD-124|MD-124]] creates: "the most painful part of meta ads for me is the ad creation itself. Specifically, the images and videos." Ten assets per ad object, multiplied again by aspect ratios, is more creative than a one-or-two-ads-at-a-time operator produces by hand.

**Seven controls, as he names them.**
1. **A written rule book** for how ads are planned and created, updated every time he corrects something or says what he likes. His own consequence, and it is the right way round: "the ads I'm creating early are bound to be the worst ads that I create."
2. **Named adversarial roles**: copywriters, creative directors, designers and an auditor, each with a defined job and each "told to push back when judging the work."
3. **Voice fitted from his own corpus**, "hundreds and hundreds of pages of blog posts", rather than from a described tone.
4. **A maintained list of AI-tell words and phrases**, his own, supplied as a block list.
5. **A voice-editor role** that audits every piece of copy against that corpus.
6. **One reviewer whose single job is catching AI-looking visuals**, run twice: on the design plan before a single image exists, and again on the finished images and videos.
7. **Three human approval gates after two automated rounds**: messaging, visual direction, mock-ups. Results of previous batches are read in before the next batch starts.

**The mechanism claim under all seven, and it is the part worth keeping.** Without operator-specific input the output is "generic and based on the average of advertising advice found on the internet." That names why an unconstrained AI creative pipeline converges on the category median, which is the same failure a batch slop gate catches in copy from the other direction, and it is an argument for the rule book rather than for the tool.

**Guards, and they are heavy.** One operator, zero numbers, no control, no window, no spend, no sample. The pipeline is his own and the episode closes on a paid-membership promotion. The only quantity anywhere in the transcript is cycle time, "a couple of hours start to finish", which is a production-cost figure. **Build a pipeline from this list. Do not quote it as evidence that the pipeline works.** His performance assertion and why it changes nothing are at [[Creative Science#CR-169|CR-169]].
Sources: Jon Loomer, How I'm Using AI to Create Meta Ads, 2026-11-11
Last touched: 2026-11-11
"""

t = CR.read_text(encoding="utf-8")

# 1. amend CR-169
anchor = "Sources: Mark Builds Brands, i tried running only AI ads for 30 days, 2026-04-29; Fraser Cottrell, The New Way to Make Ai UGC in 2026, 2026-03-15; Fraser Cottrell, Watch Me Create 3 Static Ads With AI From Scratch, 2026-04-05\nLast touched: 2026-09-18"
assert t.count(anchor) == 1, "CR-169 source anchor not unique"
amend = """**Amended 2026-11-11, and this is the cleanest confirmation the claim has had.** Jon Loomer, 11 November 2026, asserts a performance improvement outright: "the ads I've created so far aren't perfect, but I'm actually getting better results than I was with the ads I created myself." **No number of any kind accompanies it.** No cost per result, no spend, no window, no sample, no control arm, and the comparison is against his own remembered prior output. The only quantity in the transcript is production time, "a couple of hours start to finish", which is a production-cost figure, which is the exact category this claim says every AI-creative advantage falls into.

**So the first outright "better results" sentence from a high-credibility Meta operator arrives with the same evidence shape as all the rest, and the rule is unchanged.** We do not write that AI creative performs better. The control architecture he credits for the improvement is worth having on its own terms and is banked separately at [[Creative Science#CR-291|CR-291]].

""" + anchor.replace(
    "2026-04-05\nLast touched: 2026-09-18",
    "2026-04-05; Jon Loomer, How I'm Using AI to Create Meta Ads, 2026-11-11\nLast touched: 2026-11-11")
t = t.replace(anchor, amend)

# 2. append CR-291
t = t.rstrip("\n") + "\n" + CR291
CR.write_text(t, encoding="utf-8")

# 3. MD-124 source
m = MD.read_text(encoding="utf-8")
md_anchor = "Sources: Charley T, Facebooks New Update Just KILLED Flexible Ads, 2026-04-26\nLast touched: 2026-08-24"
assert m.count(md_anchor) == 1, "MD-124 anchor not unique"
m = m.replace(md_anchor,
    "Sources: Charley T, Facebooks New Update Just KILLED Flexible Ads, 2026-04-26; Jon Loomer, How I'm Using AI to Create Meta Ads, 2026-11-11 (restates the 10-asset capacity from the operator side and notes that aspect-ratio variants of one concept push the asset count past 10 inside a single ad object)\nLast touched: 2026-11-11")
MD.write_text(m, encoding="utf-8")

# 4. transcript extracted flag
s = TR.read_text(encoding="utf-8")
assert "extracted: false" in s
TR.write_text(s.replace("extracted: false", "extracted: true", 1), encoding="utf-8")

print("CR-291 appended, CR-169 amended, MD-124 source added, transcript marked extracted")
