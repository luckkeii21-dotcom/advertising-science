# -*- coding: utf-8 -*-
"""2026-10-01 research merge. 3 new claims (SC-173, AU-096, CR-282), 2 amendments (SC-149, MD-166)."""
from pathlib import Path

V = Path("E:/claude code marketing skill/Obsidian God-level Marketing Vault/God-level Marketing/wiki/science")


def rd(n):
    return (V / n).read_text(encoding="utf-8")


def wr(n, t):
    (V / n).write_text(t, encoding="utf-8")


SRC_LOOMER = (
    "Jon Loomer, \"An Ad Solution for Meta's Restriction on Organic Link Sharing\", Pubcast, "
    "2026-09-30, youtube.com/watch?v=vjNRpNSASOQ, 10 min, 1,535 words, read in full"
)

SC173 = """

### SC-173 \u00b7 Loomer prescribes the upper-funnel goal and the placement pruning he told advertisers to abandon five weeks earlier, as a $5-a-day paid replacement for capped organic link posts
Tier: T3 \u00b7 Status: active
Jon Loomer, 2026-09-30, who flags it as an exception to his own standing advice four times in a ten-minute episode: "these are all things I would normally not recommend", "this is one of those situations that is an exception to my typical recommendations", "I have to keep reminding you that this is a rare exception", and "in most cases, I'd give you a side eye for talking about doing this in the first place".

**The problem he is solving is [[Meta Delivery & Andromeda#MD-166|MD-166]].** Meta caps a Facebook Page at 2 organic link posts a month on the free tier and sells the increase through Meta One. His frame: do not buy the subscription, spend the same money on ads. The budget is set to match, $5 a day against the $149 Expert tier.

**The structure, every parameter he states:**

- One permanent ad set that replaces the organic publishing routine. "Instead of publishing today's blog post to your page, publish an ad that promotes it."
- Performance goal high in the funnel: maximise reach, link clicks, landing page views or interactions. He names no single choice and says to experiment. Video views and ThruPlay are ruled out because the goal is traffic.
- Targeting restricted to the Page's own Facebook and Instagram followers through custom audiences, with the country count limited as well.
- Placements pruned by goal: remove Audience Network on link clicks or landing page views, remove ads on Facebook Reels on reach.
- Up to 50 ads in the one ad set, one per blog post or podcast episode, added as they publish.
- A frequency cap or frequency target, because the audience is a fixed follower pool.

**Why this is banked rather than discarded as a repeat: it reverses the remedy in [[Scaling Models#SC-149|SC-149]], and the same operator supplied both sides.** SC-149 records him on 2026-08-24 naming exactly these two pairings as the upper-funnel exposure, then arguing the fix is to abandon the goal rather than prune the placement, "because you're still bound to get cheap, low-quality optimized actions from other placements". Today he keeps the goal and prunes the placement. The mechanism underneath is unchanged and he restates it in the same words: with no conversion to optimise for, "Meta will exploit weaknesses to find the cheapest and likely lowest quality optimized actions".

**The boundary that lets both statements survive.** SC-149's remedy answers "the campaign's job is conversions and the goal is wrong". This answers "the campaign's job is traffic to content that has no conversion". Where there is no bottom-funnel action to fall back to, abandoning the goal is not an available move, so guard rails are the only one left. He also restates the piece of placement-control scope that makes this possible at all: Meta's withdrawal of placement exclusion is bottom-of-funnel only, so the control still exists on the goals this design uses.

**Nothing here has been run, and he says so.** "Will $150 of ads be better than the $149 paid for Meta 1? We'll see. But my hunch is that it would be." No spend, no account, no before-and-after. The reasoning for preferring ads is one sentence and it is the strongest part of the episode: "Meta has devalued link sharing over the years by throttling reach for businesses. With ads, I can guarantee a certain amount of delivery."

**The cheap test, and our own book is the population for it.** This design is [[Scaling Models#SC-130|SC-130]] doing a different job: same small fixed budget, same upper-funnel goal, same frequency cap, same large creative pool against one fixed audience. SC-130 is a retargeting presence layer; this is an organic-distribution replacement. Any client Page subject to the MD-166 cap that posts links more than twice a month can run it, and the only new question is whether follower-targeted reach buys more clicks than the subscription buys link slots.
Sources: %s
Last touched: 2026-10-01
""" % SRC_LOOMER

AU096 = """

### AU-096 \u00b7 Generative retrieval is in production on a second major ad platform's candidate-generation stage, and its two named bottlenecks are coupled against each other
Tier: T1 \u00b7 Status: active
arXiv 2609.39327, *GEAR: Generative End-to-end Ad Retrieval at Douyin*, submitted 30 September 2026, eleven authors, no affiliations printed on the arXiv page. **"It currently serves hundreds of millions of daily active users on Douyin Ads."**

**The mechanism worth keeping is a scaling constraint rather than a result.** Generative retrieval reformulates candidate selection as the generation of discrete item tokens. The paper names two bottlenecks that appear only at real-system scale:

1. **Representation collapse.** The item tokenizer converges to degenerate results under continuous distribution shift, which blocks stable end-to-end adaptation.
2. **Item collisions.** The candidate pool is large enough that distinct items receive identical token sequences, which costs retrieval precision.

**The coupling is the claim: "expanding codebook capacity to mitigate collisions inevitably exacerbates collapse."** The obvious fix for one failure causes the other. GEAR's answer is an orthogonal-basis re-parameterisation of the codebook (BasisVQ, extended to prefix-aware BasisRQ) plus a context-conditioned reranking head placed inside the generative process.

**What it does not say, and the abstract is the whole of what we have.** "Substantial empirical improvements in extensive online A/B tests", with **no percentage, no revenue figure and no baseline anywhere on the arXiv page.** The deployment is established and the magnitude is unpublished. Do not carry this as a measured gain.

**Why it is banked when it changes no decision we make this week.** Beside the TAGR half of [[Auction Mechanics & Bidding#AU-081|AU-081]], which refreshes an ad's semantic ID as its live-stream content changes and does publish its lifts, it makes two large ad platforms running semantic-ID retrieval in production. And beside [[Meta Delivery & Andromeda#MD-001|MD-001]], where Meta's multi-stage retrieval selects candidates on predicted per-user relevance of the creative, it says the industry is arriving at the same place by a different route: **the candidate set is generated from a learned representation of the item, so what the ad IS decides which pool it can be drawn from at all.** That is the mechanism under our creative-volume position, reported from a third codebase.
Sources: arXiv 2609.39327v1, GEAR: Generative End-to-end Ad Retrieval at Douyin, 2026-09-30, https://arxiv.org/abs/2609.39327, abstract read in full at source
Last touched: 2026-10-01
"""

CR282 = """

### CR-282 \u00b7 A search-ads platform writes advertisers' ad descriptions with a reward model that scores LANDING PAGE CONSISTENCY, live since late May 2026 across more than 140,000 advertisers
Tier: T1 \u00b7 Status: active
arXiv 2606.15911v2, *Interactor: Agentic RL oriented Iterative Creation for Ad Description Generation in Sponsored Search*, EMNLP 2026 Industry Track, v1 14 June 2026, v2 30 September 2026, six authors. **The platform is not named**; the paper says only "a leading search ads system". **"Since late May 2026, it has been deployed online in a leading search ads system, where the framework serves over 140k advertisers."**

**The finding for our lane is what the platform's own reward model grades.** The generator is a policy. The environment is several generative reward models that score each draft on **knowledge capacity** and **landing page consistency**, return a binary signal plus written feedback, and the policy rewrites against that feedback over multiple turns.

**Two operating consequences, and the first is the one that costs money.**

1. **Description-to-landing-page agreement is a scored quantity inside a live ad system.** [[Google Auction & Smart Bidding#GA-010|GA-010]] already carries landing page experience as one of Quality Score's three T1 components. This is a second, independent instance on a different surface, and it sits further upstream: the platform grades the copy against the page while the copy is being written. A description that promises something the page does not say is failing a model trained to catch exactly that.
2. **The platform separates titles from descriptions by job.** The paper's own framing is that titles are optimised to attract clicks, while a description has "a longer text span and possesses the potential of incorporating world knowledge to address user search intents while presenting the fine-grained selling points of the ads". The description is the slot where the specifics belong, which is the opposite of treating it as padding.

**The guard.** No numbers are published on either side. The deployment line reads "contributing to both ad revenue and user experience", with no lift, no window and no control group. And a platform optimising descriptions against its own revenue and its own quality definition is not an advertiser optimising for cost per opt-in. **Carry this as evidence about what the machine scores, never as evidence that machine-written descriptions beat ours.**
Sources: arXiv 2606.15911v2, Interactor: Agentic RL oriented Iterative Creation for Ad Description Generation in Sponsored Search, v1 2026-06-14, v2 2026-09-30, EMNLP 2026 Industry Track, https://arxiv.org/abs/2606.15911, abstract read in full at source
Last touched: 2026-10-01
"""

SC149_AMEND = """**2026-09-30: the same operator reversed the remedy, and the reversal is banked at [[Scaling Models#SC-173|SC-173]] rather than contested here.** The paragraph above records him on 2026-08-24 naming Audience Network for link clicks and landing-page views, and ads-on-Facebook-Reels for reach, then arguing the fix is to abandon the goal rather than prune the placement. Five weeks later he prescribes both of those goals and prunes exactly those two placements, as a paid replacement for the organic link posts Meta capped at [[Meta Delivery & Andromeda#MD-166|MD-166]]. **Nothing in this claim is refuted.** The condition that decides the argument, the performance goal, is unchanged, and so is the mechanism. What changed is the availability of his remedy: abandoning the goal assumes a bottom-funnel action to fall back to, and a campaign driving traffic to a blog post or a podcast episode has none. SC-173 carries the full structure and the fact that he has not run it.
"""

MD166_AMEND = """**A third unverified Instagram figure, and this claim's correction has not reached him (2026-09-30).** The paragraph above records that Loomer's per-tier Instagram splits are unverified, because Meta's help article covers Facebook Pages only and publishes one number per tier with no Instagram split. He now states a third: **Max gives unlimited Facebook link posts but 12 Instagram link posts**, alongside Expert at 20 Facebook and 8 Instagram, which matches what he said on 2026-09-23. **Still unverified against any Meta surface, still not repeatable to a client.** He also repeats, unchanged, that putting the link in a comment does not get around the limit. The correction above stands: that is right for a standalone comment and wrong for extra links inside the comments of a post that already carries one, which Meta exempts by name. **The paid-replacement design he builds on top of this cap is at [[Scaling Models#SC-173|SC-173]].**
"""


def amend_before_sources(name, hdr, next_hdr, amend_text, src_add=None, touched="2026-10-01"):
    """Insert amend_text just before the final 'Sources:' line inside one claim block."""
    t = rd(name)
    i = t.index(hdr)
    j = t.index(next_hdr, i)
    block = t[i:j]
    k = block.rindex("\nSources: ")
    m = block.rindex("\nLast touched: ")
    end = block.index("\n", m + 1)
    src_line = block[k + 1:m].rstrip()
    if src_add:
        src_line = src_line + "; " + src_add
    newblock = block[:k + 1] + amend_text + "\n" + src_line + "\n" + "Last touched: " + touched + block[end:]
    wr(name, t[:i] + newblock + t[j:])
    print("amended", hdr.strip(), "in", name)


for fn, body in (("Scaling Models.md", SC173),
                 ("Auction Mechanics & Bidding.md", AU096),
                 ("Creative Science.md", CR282)):
    wr(fn, rd(fn).rstrip("\n") + "\n" + body)
    print("appended new claim to", fn)

amend_before_sources("Scaling Models.md", "### SC-149 \u00b7", "### SC-150 \u00b7", SC149_AMEND, SRC_LOOMER)
amend_before_sources("Meta Delivery & Andromeda.md", "### MD-166 \u00b7", "### MD-167 \u00b7", MD166_AMEND, SRC_LOOMER)
print("DONE")
