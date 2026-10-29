# -*- coding: utf-8 -*-
# Research run 2026-10-29: merges into existing claims + MD-186 contest.
import io, os, re

SCI = r"E:\claude code marketing skill\Obsidian God-level Marketing Vault\God-level Marketing\wiki\science"

def read(f):
    return io.open(os.path.join(SCI, f), encoding='utf-8').read()

def write(f, t):
    io.open(os.path.join(SCI, f), 'w', encoding='utf-8', newline='\n').write(t)

def splice(fname, claim_id, addition, touched="2026-10-29"):
    """Insert addition before the Sources: line of the given claim, and bump Last touched."""
    t = read(fname)
    m = re.search(r'(?m)^### ' + re.escape(claim_id) + r'(?: |\u00b7|\s)', t)
    if m is None:
        raise SystemExit("claim not found: " + claim_id)
    start = m.start()
    nxt = re.search(r'(?m)^### [A-Z][A-Z]-\d+', t[start + 5:])
    end = (start + 5 + nxt.start()) if nxt else len(t)
    body = t[start:end]
    if addition.strip()[:60] in body:
        print("SKIP already merged: " + claim_id)
        return
    sm = list(re.finditer(r'(?m)^Sources: ', body))
    if not sm:
        raise SystemExit("no Sources line in " + claim_id)
    si = sm[-1].start()
    body = body[:si] + addition.strip() + "\n" + body[si:]
    body = re.sub(r'(?m)^Last touched: .*$', 'Last touched: ' + touched, body)
    t = t[:start] + body + t[end:]
    write(fname, t)
    print("merged into " + claim_id)

MD = "Meta Delivery & Andromeda.md"

splice(MD, "MD-024", u"""
**SUPERSEDED AS THE CURRENT GENERATION, 2026-10-29, and the 2024 baseline is now stated by Meta.** The engineering post of 2026-10-28 publishes the next Andromeda generation at [[Meta Delivery & Andromeda#MD-188|MD-188]], and in doing so gives this entry's system a throughput figure it never had: the 2024 deployment "evaluates at tens of millions of ads per second per GPU card", against over one billion ads per second per GPU server now. Meta's own description of the 2024 work in the new post matches this entry exactly, "growing model capacity by four orders of magnitude", so the 10,000x holds. **The +6% recall and +8% ads quality figures belong to the 2024 generation and must not be carried forward to the 2026 one, which publishes no recall or quality figure at all.** The "another 1,000x increase in model complexity" Meta expected in 2024 has not been claimed as delivered; what the 2026 post claims instead is 300x FEWER FLOPs at near ranking-level quality ([[Meta Delivery & Andromeda#MD-189|MD-189]]), which is a different axis. Status stays active as the record of the 2024 generation.
""")

splice(MD, "MD-026", u"""
**AMENDED BY THE 2026 GENERATION, 2026-10-29.** This entry's machinery is the 2024 design and it has been rebuilt. Meta now states the pipeline "scores every eligible ad in the candidate pool" rather than reaching a huge number through hierarchical pruning, and that the multi-kernel structure this entry describes became the bottleneck: "At billions of ads per second, even a small intermediate tensor per ad multiplies into terabytes per second of high bandwidth memory (HBM) traffic. The memory workload of these intermediate tensors, not arithmetic, becomes the dominant bottleneck in multi-kernel retrieval pipelines." The replacement is a single fused kernel keeping intermediates in registers and shared memory, plus co-location of index matching, scoring and top-K on one GPU. **So the 10x model elasticity, 3x end-to-end QPS and 100x feature-extraction figures here are historical 2024 numbers describing a superseded architecture.** Keep them as the record of that generation, cite [[Meta Delivery & Andromeda#MD-188|MD-188]] and [[Meta Delivery & Andromeda#MD-190|MD-190]] for how retrieval runs now.
""")

splice(MD, "MD-089", u"""
**SECOND FIRST-PARTY STATEMENT OF THE SAME CAUSE, WITH A MAGNITUDE, 2026-10-29.** Meta's 2026-10-28 Andromeda post repeats this entry's causal story and sizes it: "Since then, generative AI creative tools have helped advertisers rapidly create hundreds of millions of new ads, growing Meta's ads candidate pool to an unprecedented scale." **Hundreds of millions of new ads is the first number Meta has put on the creative-volume explosion its own tools caused.** Two years, two posts, the same explanation, which makes this one of the better-supported causal claims in this file. It also tightens the loop worth keeping in view: Meta ships generative creative tools, advertisers flood the pool, Meta rebuilds retrieval to cope, and the rebuild is then published as an advertiser benefit.
""")

splice(MD, "MD-022", u"""
**RE-CONFIRMED VERBATIM BY META, 2026-10-29, and the latency budget is explicitly unchanged.** Two Meta pages dated 2026-10-28 restate this cascade in this entry's own terms. The business-news page: Andromeda "narrows tens of millions of ads to the few thousand worth ranking for each person". The engineering post: "Retrieval narrows a vast pool of eligible ads down to a small set of strong candidates in milliseconds; a later, more computationally expensive ranking stage then scores those survivors in fine detail", and the 100x throughput gain arrives "within the same latency budget". **So the tens-of-millions-to-a-few-thousand funnel and the millisecond budget both survive two years and a full architectural rebuild.** What has changed sits inside the first stage rather than in the shape of the cascade: every eligible ad is now scored ([[Meta Delivery & Andromeda#MD-188|MD-188]]) and the retrieval model's quality now approaches the ranker's ([[Meta Delivery & Andromeda#MD-189|MD-189]]), which weakens the premise that the early stage is the crude one.
""")

splice(MD, "MD-177", u"""
**THE SAME FIGURES APPEAR ON A SECOND META PAGE, DATED, 2026-10-29, and the footnote complaint is answered only in part.** Meta's business-news post of 2026-10-28 carries this entry's numbers again and scopes them in time: GEM has delivered "up to a 18.9% conversion improvement and a 12% ad click-through rate improvement" **since 2025**, alongside the same "5.8%, 4.1%, and 1.6% conversion uplift on Facebook, Instagram, and offsite conversions". So the two sets are one claim restated, not two achievements, and the period is since 2025 rather than a quarter. The same page restates the architecture figures as "2x longer engagement history through a 2.5x more complex model", consistent with [[Meta Delivery & Andromeda#MD-178|MD-178]] and [[Meta Delivery & Andromeda#MD-180|MD-180]]. **On footnotes: the sister page published the same day DOES footnote its numbers to Meta's Q2 and Q3 2026 earnings ([[Meta Delivery & Andromeda#MD-192|MD-192]]), which proves Meta footnotes these pages when it chooses to. This entry's figures still carry none, on either page.** Treat the "up to" in "up to a 18.9%" as the load-bearing word it is.
""")

splice(MD, "MD-120", u"""
**STRENGTHENED, 2026-10-29, and this is now the second-strongest support rather than the strongest.** Meta's 2026-10-28 business-news post states that the system "generates the semantic ID for the ideal ad for a person, then matches that to the ads available in our system", and that models "read each ad's text and images and describe the ad in semantic tokens that capture its key attributes". Full record at [[Meta Delivery & Andromeda#MD-191|MD-191]]. **An input feature is one thing; a matching key the system generates before it ever looks at your ad is a stronger thing.** This entry's claim, that ad creative representation is a named GEM input, is unchanged and now sits inside a larger documented role for creative representation across retrieval as well as ranking.
""")

splice(MD, "MD-093", u"""
**META STATES THE SHALLOW-EVENT WARNING IN ITS OWN WORDS, 2026-10-29.** The business-news post of 2026-10-28 instructs advertisers: "Choose the outcome you actually want, not the closest proxy you can measure. A lead isn't a sale, and an install isn't a subscriber." And on values: "Send back the value of each conversion, not just the fact that a conversion happened, so delivery weights toward your most valuable outcomes." **"A lead isn't a sale" is this entry's law in Meta's own sentence, from the platform whose literalism the entry is about.** It arrives with no number and no test, which is the same evidence state as the practitioner version it confirms. The same page names the three measurement settings an advertiser can optimise to: "Meta's measurement using standard attribution, your own attribution framework using custom attribution, or incrementality experiments with incremental attribution, conversions that would not have happened without the ad." Relevant to us because our lead-gen accounts optimise to form fills by necessity, so the instruction is one we cannot fully follow, which is exactly the precondition recorded at [[Meta Delivery & Andromeda#MD-187|MD-187]].
""")

# MD-186: contest the retrieval limb
t = read(MD)
m = re.search(r'(?m)^### MD-186 .*$', t)
line = m.group(0)
newline = line.replace(
    u"Tier: T1 \u00b7 Status: active", u"Tier: T1 \u00b7 Status: active")
# status line sits on the line after the heading
start = m.start()
nxt = re.search(r'(?m)^### [A-Z][A-Z]-\d+', t[start + 5:])
end = start + 5 + nxt.start() if nxt else len(t)
body = t[start:end]
if "CONTESTED ON ITS RETRIEVAL LIMB" not in body:
    body = re.sub(r'(?m)^Tier: (.*?) \u00b7 Status: active$',
                  u'Tier: \\1 \u00b7 Status: CONTESTED on the retrieval limb, active on the rest',
                  body, count=1)
    add = u"""
**CONTESTED ON ITS RETRIEVAL LIMB, 2026-10-29, by Meta's own later page.** On 2026-10-28 Meta published that it "launched generative retrieval on Facebook Feed" in Q3 2026, and that GenRecs "generates the semantic ID for the ideal ad for a person, then matches that to the ads available in our system". Full record at [[Meta Delivery & Andromeda#MD-191|MD-191]].

**The split, and it is clean.** This entry's headline says Meta does not retrieve OR write ads generatively. **The writing limb stands and is not in question: no ad is generated by a model.** The retrieving limb is now contested by Meta itself, which ships a product called generative retrieval in which a semantic ID genuinely is generated inside the retrieval path before any real ad is consulted.

**The reading rule this entry exists for was still the right call, and it needs narrower wording.** What is generated is a TARGET REPRESENTATION, not an ad and not a retrieval result; retrieval remains a matching operation against that target. The cited paper's case against generation for retrieval is a case against generating the RESULT, which is compatible with generating the query. **So use this entry as: generative means the representation, and from today also means the system can generate the description of the ad it wants before matching. It still never means Meta writes your ad.**
"""
    sm = list(re.finditer(r'(?m)^Sources: ', body))
    si = sm[-1].start()
    body = body[:si] + add.strip() + "\n" + body[si:]
    body = re.sub(r'(?m)^Last touched: .*$', 'Last touched: 2026-10-29', body)
    t = t[:start] + body + t[end:]
    write(MD, t)
    print("contested MD-186")
else:
    print("SKIP MD-186 already contested")

# SC-086: Loomer's time-boxed complexity exception
splice("Scaling Models.md", "SC-086", u"""
**A TIME-BOXED EXCEPTION FROM A CONSOLIDATION ADVOCATE, 2026-10-29, and it is the cleanest statement of the exception this file holds.** Jon Loomer, whose standing position is maximum consolidation, draws the line at duration rather than at structure. His words: "you know that I prefer a simple campaign construction where you consolidate your budget as much as possible. But, at the same time, I'm not going to fight you on some short-term complexity to make room for Black Friday and Cyber Monday... And since it's short-term, I don't see it as being nearly as problematic as creating permanent unnecessary complexity."

**Why it belongs on this entry specifically.** This entry's finding is that consolidation starves anything the business has already committed money to. **A seasonal promotion is the textbook case of committed money: the offer is built, the stock or the capacity is reserved, and the dates cannot move.** Loomer's own ordering agrees, because he reaches for a separate ad set or campaign only when ongoing ads must keep running, and consolidates onto the promotion when budget is tight: "if you're strapped on budget, I consolidate to focus my money on the Black Friday Cyber Monday promotion."

**His stated reason for accepting the split is certainty, not performance.** "While it's not ideal, it adds some certainty and predictability regarding ad spend." He names the two in-ad-set alternatives first, push delivery to force spend onto the promo ads inside an existing sales ad set ([[Meta Delivery & Andromeda#MD-141|MD-141]]), or a CBO ad set spending minimum. **No account, no numbers, no test. T4 operator judgement, banked for the decision rule: trade structural purity for spend certainty only where the complexity has an end date.**
""")
