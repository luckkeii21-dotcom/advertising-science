# -*- coding: utf-8 -*-
"""Claim merge for the 2026-09-04 research pass.

Two new transcripts from the daily harvest, both read start to finish:
Jon Loomer's 15-year reflection episode (one line banked as an amendment)
and Dr. Matt Shiver's mindset interview with Chase Tolleson (read in full,
nothing banked). One arXiv paper past the ad filter, full HTML read:
UniCon, deployed on Meituan search advertising.
"""
import sys
sys.stdout.reconfigure(encoding="utf-8")
import merge_helper
merge_helper.TODAY = "2026-09-04"
from merge_helper import amend, mint, audit

AU = "Auction Mechanics & Bidding.md"
MD = "Meta Delivery & Andromeda.md"

LOOMER = "Jon Loomer, 15 Years of Lessons Learned, 2026-09-02"
UNICON = ("UniCon: A Unified Context-Centric Modeling Paradigm for CTR Prediction, "
          "arXiv 2609.03290v1, full HTML read 2026-09-04 via cs.IR feed")

print("== Meta Delivery ==")

amend(MD, "MD-075",
      """**A fourth operator, added 2026-09-04, and this one is reporting a retreat rather than recommending a tactic.** Jon Loomer, in the episode marking 15 years of jonloomer.com: "during the past several years, I was confronted with the reality that my focus on remarketing and microtargeting was no longer relevant. And that may have been the most difficult pivot of all because those targeting strategies were a big part of why my business exists today." He built a 15-year business teaching the thing and then stopped teaching it, at a cost he names. That is a harder kind of evidence than a tactical recommendation, because nobody talks themselves out of their own franchise for fun.
**What it does NOT repair, and this matters more than what it adds.** The two dates in the first paragraph, interest targeting worthless since 2018 and cold/warm/hot dead the same year, come from one speaker who carries a standing arithmetic warning at [[Scaling Models#SC-148|SC-148]]. **Loomer gives no date, no mechanism and no data, so the 2018 dating stays single-sourced and unverified.** What he supplies is a second long-record operator arriving at the same destination independently, and the word he reaches for is "no longer relevant" rather than "never worked", which is a claim about a change over time and not about the whole history. Practitioner statement inside a reflective episode, no delivery data shown.""",
      [LOOMER])

print("== Auction Mechanics ==")

mint(AU, "AU-085",
     "A deployed search-ads ranking model reports 90% of its gain from reorganising the INPUT and almost none from parameter count, and throws away 75.4% of its computation for a difference inside its own noise floor",
     "T1", "active",
     """Picked up on the arXiv cs.IR lane on 2026-09-04, full HTML read rather than the abstract alone. Same handling rules as [[Auction Mechanics & Bidding#AU-079|AU-079]] and [[Auction Mechanics & Bidding#AU-084|AU-084]]: this documents Meituan, a Chinese local-services search advertising platform, and must never be quoted as documentation of Meta or Google. It earns its place because it publishes an internal comparison the other papers in this lane do not.

**The production result.** Seven-day online A/B at 20% traffic on Meituan search advertising: **RPM +3.09%, CTR +2.07%, revenue +2.95%**, all "significant under two-sided tests (p<=0.01)". Offline AUC moved from a production base model at **0.8558 to 0.8697**, the stated **+0.0139**. The paper states its own noise floor: "AUC differences within 0.0003 are treated as normal run-to-run variation."

**The finding that makes this worth banking, and the authors do not headline it.** Their three model sizes are UniCon-Small at 0.09B parameters (0.8683), Mid at 0.17B (0.8693) and Large at 0.33B (0.8697). **The smallest model already carries 0.0125 of the 0.0139 total gain, which is 90% of it. Nearly quadrupling the parameter count buys the remaining 0.0014.** Split further, the first near-doubling (0.09B to 0.17B) buys 0.0010 and the second (0.17B to 0.33B) buys **0.0004, which is 1.3x their own stated noise floor.** So on this system the gain came from how the input was organised, and parameter scaling was close to exhausted by the smallest model tested.

**The second number in the same direction.** Context compression at the production retention ratio of 0.5 changes AUC from 0.8698 to 0.8697, a 0.0001 move **inside their own 0.0003 noise band**, while "reducing profiled computation by 75.4%". Three quarters of the ranking computation was redundant and its removal cost nothing measurable.

**The architectural argument, which is the transferable idea.** A context unit is "the set of items jointly displayed in one exposure event, together with the associated user intent and environmental signals", and their case is that a user's history and the request being scored right now are the same kind of object: they "differ only in whether their outcomes are observed or remain to be predicted". Splitting them into sequential and non-sequential branches "introduces artificial heterogeneity before model interaction begins". Scale of what is modelled: "each input history can contain hundreds of context units, with fewer than ten items per unit", against up to 300 candidates per production shard.

**Where this sits against AU-084, stated as a distinction and not as a contradiction.** ReST concluded that "behavior-sequence scaling remains a promising, under-exploited axis for production ranking" and Meta says its sequence model scaling law "shows no signs of saturation". Those are claims about scaling the SEQUENCE. UniCon scales PARAMETERS and finds that axis nearly flat above 0.09B. **Two different axes, so neither refutes the other, and the codex should stop treating "scaling" as one word.** Nothing here contests AU-084; it narrows what AU-084's word "scaling" is allowed to mean.

**A consistency check the paper does not run, and it passes.** Revenue is RPM times impressions, so +3.09% RPM against +2.95% revenue implies impressions fell about 0.14%, which is flat. And +3.09% RPM against +2.07% CTR implies revenue per click rose about 1.0%. **So roughly two thirds of the revenue-per-impression gain came from more clicks and one third from better-paying clicks.** All three published numbers are mutually consistent.

**Guards, all load-bearing.** Different platform, different market, authors reporting on their own system, and the optimised metrics are platform RPM and revenue rather than advertiser outcome. **The percentage lifts sit on someone else's baseline and must never be quoted to a client or forecast as an expectable gain.** Nothing here changes an operating decision this week. What it changes is one word in how we read this lane.""",
     [UNICON])

print("\n== audit ==")
total, tiers, stat, per = audit()
print(f"total claims: {total}")
print(f"tiers: {tiers}  (sum {sum(tiers.values())})")
print(f"status: {stat}  (sum {sum(stat.values())})")
for k, v in per.items():
    print(f"  {v:>5}  {k}")
