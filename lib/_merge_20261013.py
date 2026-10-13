import pathlib
p = pathlib.Path(r"E:/claude code marketing skill/Obsidian God-level Marketing Vault/God-level Marketing/wiki/science/Meta Delivery & Andromeda.md")
t = p.read_text(encoding="utf-8")
assert "MD-174" not in t and "MD-175" not in t, "already merged"

new = """

### MD-174 · Part of Meta's ads ranking runs on idle, reclaimable inference capacity, so the DEPTH of ranking applied to a request is not a constant
Tier: T1 · Status: active
Meta published the system on 2026-10-12. Its own one-line summary: "we've built a system that enhances ads recommendations by leveraging idle inference capacity in our fleet." The fleet can be globally constrained while pockets sit locally idle (peak provisioning against time-of-day traffic, capacity arriving before models are ready for it, CPU-to-accelerator ratios that do not match in a region, and accelerator types a workload cannot run on). Meta aggregates those pockets into one shared **opportunistic capacity pool**, which it describes as "preemptible (can be reclaimed at any time), highly volatile in its availability, and carries no long-term guarantees."

**Two levers spend that pool, and they are the part that touches us.**
- **Rank More Ads (RMA)** raises the number of candidates the ranking stages evaluate when surplus exists. "Evaluating more candidates increases the chance of finding ads that are relevant to the user." It needs both CPU and accelerator surplus, because the extra candidates also pass through retrieval and feature processing.
- **Serve Better Models (SBM)** raises the share of requests scored by a more powerful model. It holds candidate count constant, so it can spend accelerator-only surplus that RMA cannot. Meta states plainly why the better model is not simply always on: "it's not efficient to use them for every request with dedicated capacity."

**The control loops run on minutes and the shedding runs on milliseconds.** RMA is governed by a central PID controller reading observed **tail latency**: latency under target, rank more candidates; latency rising, rank fewer. SBM has a matching controller setting target coverage for the powerful model. Because "opportunistic capacity can be reclaimed faster than the control loops," both servers and clients also shed the lowest-value optional work directly, "within a few milliseconds," to bridge the gap. When capacity contracts, optional work is removed rather than allowed to spill onto baseline capacity, which Meta protects physically for SBM (separate routing targets, requests fall back to the baseline model) and logically for RMA (a global budget capped at what the opportunistic replicas can carry).

**What this changes for an operator, and it is a reading rule rather than a lever.** Two identical requests for the same ad, same audience, same budget can receive materially different amounts of ranking work depending on how much of Meta's fleet happened to be idle at that moment, in that region, on compatible hardware. The variance has an infrastructure source that no account setting can see or influence, it is not auction competition, and it moves on a cadence between milliseconds and minutes. It is one more reason a two-day swing in cost per result on an unchanged ad set is not evidence of anything, and the standing instruction at [[Learning & Signal#LS-055|LS-055]], run the numbers through a significance calculator before calling a winner, is the correct response. There is nothing to optimise against here.

**Scope, stated honestly.** Meta gives no magnitude anywhere in the post: no share of requests served by RMA or SBM, no size of the opportunistic pool, no conversion or CPM effect, and no statement of how far the candidate count or model coverage actually swings. "Drives significant advertiser value and capacity efficiency" is the entire claim of effect, and it carries no number and no footnote, which is the same construction [[Meta Delivery & Andromeda#MD-171|MD-171]] catalogues. The mechanism is T1 because Meta's own engineers describe their own production system. The size of its effect on any one account is unmeasured and unmeasurable from outside.

**Where it sits against what we already hold.** [[Meta Delivery & Andromeda#MD-022|MD-022]] and [[Meta Delivery & Andromeda#MD-023|MD-023]] describe the funnel this elasticity moves inside: retrieval, early-stage ranking, late-stage ranking, each on fewer candidates. [[Meta Delivery & Andromeda#MD-026|MD-026]] records "model elasticity" on the Andromeda retrieval side, which is a different mechanism with the same word on it: that one is an efficiency property of the index, this one is a scheduling decision about spare hardware. [[Meta Delivery & Andromeda#MD-028|MD-028]] is the reason any of it pays, ranking quality scaling log-linearly with compute. [[Meta Delivery & Andromeda#MD-090|MD-090]] records compute allocated unevenly across USERS by history length; this records it allocated unevenly across TIME by hardware availability.
Sources: Engineering at Meta, Turning Opportunistic AI Inference Capacity Into Better Ads Recommendations, 2026-10-12, read in full
Last touched: 2026-10-13

### MD-175 · Meta routes the better ranking model to requests by PREDICTED LIKELIHOOD OF ENGAGEMENT, measures the incremental benefit per segment, and deliberately keeps exploratory traffic in every segment
Tier: T1 · Status: active
From the same 2026-10-12 post, and it is banked separately because it is a statement about who gets the good model rather than about capacity. The SBM model router "uses a request-value signal to group requests into segments based on predicted likelihood of user engagement with the ad." An **explore-and-exploit process** then "periodically measures the incremental outcome of using the more powerful model in each segment and updates the allocation between the two models."

**Meta names the non-obvious finding itself:** "the incremental benefit of the more powerful model does not always align with the absolute value of a request." The requests worth the most are not automatically the requests the better model helps most, so the allocation has to be measured per segment rather than reasoned from value. That is a first-party statement that a platform's own best-guess ordering of its traffic was wrong often enough to need continuous measurement.

**The second half is the one to carry.** The process "preserves exploratory traffic across segments so the system continues to collect the observations needed to adapt, rather than reinforcing an outdated routing decision." Meta spends its own scarce capacity on exploration permanently, inside a system whose stated purpose is efficiency, specifically to avoid locking in a stale allocation. We argue the same shape to clients every week about ad testing and budget, usually against the instinct to put everything behind the current winner. This is the platform's own infrastructure making that argument with its own money, and it is quotable as such.

**A calibration loop** keeps realised traffic share near the target as the traffic mix shifts across regions and over time, and on contraction the controller lowers target coverage while removed requests continue through the baseline model.

**The limit, and it matters before anyone tries to act on this.** "Predicted likelihood of user engagement" is Meta's internal request-value signal and the post defines it no further: no event, no window, no account-visible field, and no statement of whether an advertiser's optimisation event enters it. Nothing here tells an operator how to make their requests land in a better-served segment, and treating it as a lever would be inventing a mechanism Meta did not describe. Read it as evidence about how the machine allocates quality, not as something to target.
Sources: Engineering at Meta, Turning Opportunistic AI Inference Capacity Into Better Ads Recommendations, 2026-10-12, read in full
Last touched: 2026-10-13
"""

p.write_text(t.rstrip() + new + "\n", encoding="utf-8")
print("appended MD-174, MD-175")
