# -*- coding: utf-8 -*-
"""Merge the 2026-11-19 research haul into the codex."""
import shutil, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import merge_helper as mh

mh.TODAY = "2026-11-19"
SCI = mh.BASE
MD = "Meta Delivery & Andromeda.md"
AU = "Auction Mechanics & Bidding.md"
GA = "Google Auction & Smart Bidding.md"
LS = "Learning & Signal.md"
SC = "Scaling Models.md"

for fn in {MD, AU, GA, LS, SC}:
    p = SCI / fn
    b = p.with_suffix(p.suffix + ".bak-20261119")
    if not b.exists():
        shutil.copy2(p, b)
        print("backup", b.name)

SRC_SMT = ("Meta Engineering, Design Once, Deploy at Scale: Building a Template-Driven ML Ecosystem, "
           "2026-11-18, engineering.fb.com/2026/11/18/ml-applications/design-once-deploy-at-scale-template-driven-ml-ecosystem/, "
           "read in full 2026-11-19")
SRC_AGENTS = ("Meta Engineering, How Meta Uses AI Agents to Scale ML Innovations Across Ads Ranking Models, "
              "2026-11-18, engineering.fb.com/2026/11/18/ml-applications/ai-agents-to-scale-ml-innovations-across-ads-ranking-models/, "
              "read in full 2026-11-19")
SRC_LOOMER = ("Jon Loomer, Do Not Listen to People Like Me, 2026-11-18, "
              "youtube.com/watch?v=_W0eSJ4TgK0, 9 min, 1,445 words, read in full 2026-11-19")

MD202 = u"""Two Meta Engineering posts published the same day, 18 November 2026, both on ads ranking models, read in full. They are parts of one series and they are banked as one claim because they describe one system: Standard Model Templates (SMT) and the agent layer that drives technique propagation across it. [[Meta Delivery & Andromeda#MD-198|MD-198]] already holds the fleet's shape from Meta's own arXiv paper. This claim holds the thing MD-198 explicitly said was not disclosed anywhere: **how long an improvement takes to spread.**

**The number, in Meta's words.** "Today it can take over a year for every proven technique to reach every applicable model. We are aiming to reduce that time down to three months." Hitting three months requires pushing the agent workflows to "5x higher end-to-end throughput", which is stated as a target and not an achieved result.

**So the fleet is heterogeneous in TIME as well as in architecture, and that is the operating consequence.** MD-198 established that there is no single ads model, that each one is bound to a surface, an objective, a feature set and a serving budget, and that this is a better first explanation than audience quality for a creative behaving differently by placement. Add this claim and the explanation gets sharper: at any given moment the model ranking an ad on Reels and the model ranking it on Feed may be a year apart in which improvements they carry. **A tactic that genuinely works on one surface or one optimisation event, and genuinely does not work on another at the same time, can be a propagation gap rather than a difference in audience or creative.** It is an explanation to hold, never a diagnosis to offer a client, because Meta names no model, no surface and no technique, and nothing here is readable from an ad account.

**How the propagation works, and why a technique does not simply copy across.** A "technique" is anything that makes a ranking model better: architectural work (Meta names Wukong factorization layers and Interformer interaction networks), richer data representations, training optimisations, inference efficiency. "Because each model has its own architecture, data, and training and serving constraints, a technique proven on one model almost never copy-pastes onto the next." SMT answers that by standardising models onto a small set of opinionated templates built from shared components (feature selection, feature interaction, model parallelism, training configuration, hardware-aware serving), so a technique validated once at template level reaches every model built from that template. Models outside template coverage still get hand adaptation, and Meta says bespoke adaptation "is still the process for our highest-revenue models".

**Meta also publishes a shelf life on its own improvements.** "ML techniques have a shelf life. An innovation that delivers gains today may be superseded within a couple of model development cycles." That is the first first-party statement in this codex that platform-side gains decay on their own, and it is the mechanism behind why propagation speed is the thing Meta is optimising rather than invention speed.

**The two-year scoreboard, and it belongs beside MD-198's.** Over the last two years SMT reduced per-model engineering time by **92%**, shipped **5,000+ technique-model combinations**, shipped **80 new ML techniques** through its multi-model optimisation workflow, improved offline model quality by **0.63% on average at neutral serving capacity**, and delivered **0.86% cumulative online lift covering 70% of models by count**. MD-198's figures from the arXiv paper were 0.66% offline and summed online lifts of 0.07% and 0.29%. **Two independent Meta publications, two different measurement frames, same order of magnitude: a generation of Meta's ranking work moves a platform aggregate by well under one percent.** That is the second first-party confirmation of the rule MD-198 states, so "Meta changed their model" still cannot explain a client account moving by tens of percent in a week.

**The agent layer, banked for the gate it describes rather than for its productivity numbers.** Since agents began driving execution in March 2026, Meta estimates agents handle "over 60% of all technique propagation", with claimed 3x engineering productivity, a median 4x reduction in training compute "across select technique-model combinations", and "an estimated $45M+ in compute savings by the end of the year". **The useful part is the ship gate, which is published explicitly:** a technique must improve an offline predictive metric (normalized entropy), must not regress guardrails on training or inference cost, and must then "show a statistically significant win in online A/B testing before it can be shipped". Multi-model optimisation additionally weighs **regression rate** alongside average gain, because "a technique with a strong average gain but frequent regressions is difficult to ship across a large fleet. Consistency is as important as peak improvement." Humans approve what ships.

**One assumption Meta says it overturned, and it cuts against a thing practitioners assume too.** SMT "challenged a common assumption that diverse optimization goals require highly diversified model designs. In many cases, a well-designed shared template can generalize much further than expected." Read narrowly, that is about model architecture. It is not evidence about whether an advertiser should separate objectives into separate campaigns, and it must not be quoted that way.

**Limits, stated plainly.** Both posts are engineering blog posts, not documentation and not peer-reviewed papers; the SMT paper is linked but was not read for this entry. Every percentage is Meta's own, with no population, no holdout and no counterfactual published, and the 3x, 4x, 60% and $45M figures are all prefixed in Meta's own text by "we estimate", "early results", or "across select combinations". "Online lift" names no metric, and 70% of models by count is not 70% of spend or of impressions. **Nothing here is a lever:** no setting, no report, no opt-in and no advertiser-visible surface is exposed, and the propagation latency cannot be checked from any account. It reads onto [[Meta Delivery & Andromeda#MD-198|MD-198]] on the fleet's shape and serving budgets, [[Meta Delivery & Andromeda#MD-199|MD-199]] on per-request compute allocation, and [[Meta Delivery & Andromeda#MD-189|MD-189]] on retrieval quality per FLOP."""

MD203 = u"""Jon Loomer, 18 November 2026, nine minutes, no account data, no test, no numbers, no settings. Banked because this engine reads twelve practitioner channels every day and tiers what they say, and nothing in this codex holds a test for source staleness. Tiered **T4: it is reasoning, not evidence.**

**The five tells, verbatim in substance, of a Meta source that stopped adapting.** Run from a source who (1) constantly talks about remarketing strategies, (2) argues broad targeting can never match remarketing and does not understand the remarketing that happens naturally inside broad, (3) builds deliberately complicated campaigns and ad sets to exert control, (4) switches off setting after setting in the ad set while optimising for a conversion, (5) stops, starts and refines obsessively on small sample sizes.

**Every one of the five is already a law in this codex, arrived at independently, which is why the convergence is worth recording.** Natural remarketing inside broad is [[Meta Delivery & Andromeda#MD-052|MD-052]]. The collapse of cold-warm-hot separation is [[Meta Delivery & Andromeda#MD-075|MD-075]]. Hyper-segmentation fragmenting conversion data is [[Scaling Models#SC-014|SC-014]]. Restricting delivery under a conversion goal is [[Meta Delivery & Andromeda#MD-015|MD-015]] and [[Meta Delivery & Andromeda#MD-014|MD-014]]. Editing on small samples is [[Learning & Signal#LS-006|LS-006]] and [[Learning & Signal#LS-055|LS-055]]. **So the checklist adds no mechanism. What it adds is a cheap pre-read on a source before its claims are tiered, assembled by someone who was on the wrong side of it.**

**The stated mechanism, and it is the honest part.** Loomer describes resisting algorithmic targeting because his own business was built on targeting, microtargeting and remarketing: "deep down I also knew that this evolution was an attack on my brand as a targeting guy." He generalises it as "frustration with how things work today is actually overwhelm and uncertainty disguised as authority". **Read as a conflict-of-interest model: a practitioner whose commercial position depends on a control the platform has removed has a reason to keep teaching the control.** That is a reason to check a claim, never a reason to dismiss one.

**How to use it here, narrowly.** It is a prior on the SOURCE, and it never overrides what a source actually shows. A stale-looking operator showing real account data still outranks a current-sounding one showing none, because the evidence tiers decide and this claim is T4. Its practical use is in deciding what to read closely and what to treat as a strong hypothesis, which is the same judgment the no-shown-data findings on the Google roster already force.

**Limits, and one of them is in the video itself.** No evidence of any kind is offered: no example source, no named claim, no before-and-after, and no definition of "small sample". The argument is symmetric and unfalsifiable as stated, since any disagreement with a change can be relabelled as insecurity, and Loomer says so himself ("Not every change Meta makes is an improvement"). **And the closing line, "avoid making anyone your go-to source on anything", sits immediately before a pitch to subscribe to his own weekly tips for a year.** Carry the five tells. Do not carry the framing as though it were a finding."""

AU103 = u"""arXiv 2611.24283v1, announced 19 November 2026, cs.IR. "X-split Argus: Learning Reusable History Tokens for Efficient CTR Prediction". Read at abstract level only; the full paper was not opened. Banked because it is a rare outside-the-wall statement of what a ranking-model improvement is worth AND what it costs, with both halves published.

**What the system does.** Processing a user's full behavioural history for every ranking request is too expensive under production compute and latency budgets. So a history compressor encodes past interactions into a small set of tokens that are **computed offline and reused across every candidate ad**, while the online ranker scores ads by cross-attention to those tokens plus representations of recent events. The compressor and the ranker are trained end to end, with distillation from a larger teacher that scores each candidate against the uncompressed history. The number of compressed tokens and the length of recent history are tunable to fit the serving budget.

**The three numbers, all from the paper's own abstract.** Offline: a **0.81% relative reduction in normalized entropy** against the production baseline. Cost: deployment "increases online inference cost by **15%** relative to the production baseline". Online A/B against that baseline: **+4.65% on a business metric reflecting the monetary value of conversions generated for advertisers**, and **+2.96% in clicks**.

**Why this one matters to us, and it is the pairing.** [[Meta Delivery & Andromeda#MD-198|MD-198]] and [[Meta Delivery & Andromeda#MD-202|MD-202]] establish that a generation of Meta ranking work moves a platform aggregate by a fraction of one percent, measured in normalized entropy with no advertiser-facing equivalent. This paper runs the same metric on a different company's deployed system and then **translates it into advertiser money**: 0.81% NE offline came out as 4.65% more conversion value. That is the first figure in this codex connecting an internal model-quality metric to an advertiser-facing outcome, and the ratio is roughly 6 to 1 in the advertiser's favour. **Treat it as one data point from one unnamed system, never as a conversion factor.** It does not license multiplying Meta's 0.63% or 0.66% NE figures by anything.

**The second useful thing is the cost side, because nobody publishes it.** 15% more inference cost for a shipped win is the counterweight to [[Meta Delivery & Andromeda#MD-199|MD-199]], where Meta trims "resource-intensive low-impact work" first as host load rises. A ranking improvement that costs 15% more per request is exactly the kind of work an allocation layer would decline to run on a low-predicted-return request. The two claims together say the sophistication an ad request receives is a spend decision on the platform's side.

**Limits.** The company, the ad product and the placements are not named in the abstract, so this is "a large-scale real-time bidding system" and nothing more specific. Preprint, announce type new, not peer reviewed, and read at abstract level only, so the experiment design, traffic split, duration and the definition of the business metric are all unverified. The business metric is described rather than defined. Nothing here is an advertiser lever."""

GA103 = u"""Google Ads & Commerce blog, 18 November 2026, "Win the holiday shopping season with November's Demand Gen Drop". Read in full. One item in it is a new control, the rest is case-study marketing.

**The control.** Smart Bidding on Target CPA or Target ROAS in **Demand Gen** campaigns now accepts **Seasonality Adjustments**, described as factoring in "expected conversion rate increases during short promotions. This allows campaigns to bid competitively from day one and smoothly return to baseline afterward." Google's word is "newly available", so this existed in other campaign types and did not exist here. No effective date, no eligibility list and no rollout detail is published, and no lift figure is attached to it.

**Why it is worth an ID even though we run no Demand Gen.** It is the first dated instrument for the problem a short promotion creates in any Smart Bidding campaign: the bidder has learned a baseline conversion rate and a two-day offer invalidates it exactly when the money is being spent. [[Google Auction & Smart Bidding#GA-066|GA-066]] and the Demand Gen channel changes already on file mean the ad group is where Demand Gen reach is bounded; this adds the bid side. If a Demand Gen or promotional lane is ever built, the operating note is that the adjustment has to be entered **before** the promotion, since its stated purpose is bidding competitively from day one.

**The rest of the post is three advertiser case studies and none of them is evidence.** Petco with product feeds: "a 6% lift in purchase intent, a 71% surge in store visits, and a 30% boost in overall Omni ROAS". Javvy Coffee with Creator partnerships boost: "50% higher conversion rates". Shopee with affiliate partnerships boost: "a 9x average ROI". **No baseline, no window, no spend, no control group and no method is published for any of the six figures.** Same standing as every other vendor case study in this file. Do not quote them, and do not let a client quote them at us.

**Also announced, recorded without a claim of its own:** product feeds showing catalogue items directly on YouTube, checkout links and **Universal Commerce Protocol**-enabled checkout as a path to purchase, and the two creator-content boost products. All of it is catalogue and e-commerce machinery. **Our whole Google-side book is lead generation with no catalogue, so none of it applies, and the honest read is that the November Demand Gen drop is a retail-holiday release with one control in it that generalises.**"""

AM198 = u"""**The propagation latency MD-198's limits said was undisclosed is now published, 2026-11-19.** This entry closes with "'two development cycles' is not a calendar, so this discloses no retrain or refresh cadence". Meta Engineering, 18 November 2026: "Today it can take over a year for every proven technique to reach every applicable model", with a stated target of three months. The template system this paper refers to as "a common template" is also now named and described as Standard Model Templates, with its own two-year scoreboard that lands in the same order of magnitude as the figures above: 0.63% offline at neutral serving capacity and 0.86% cumulative online lift over 70% of models by count, against 0.66% and a summed 0.36% here. **So the fleet is heterogeneous in time, not only in architecture, and the under-one-percent rule now has two independent first-party sources.** Full entry at [[Meta Delivery & Andromeda#MD-202|MD-202]]."""

AM199 = u"""**The cost side of a ranking improvement now has an outside number, 2026-11-19, and it sharpens what this claim implies.** A deployed real-time-bidding system published a shipped ranking win that raises online inference cost by 15% per request ([[Auction Mechanics & Bidding#AU-103|AU-103]]). Set against the line quoted above, that "resource-intensive low-impact work is trimmed first" as host load rises, it names the kind of work that gets trimmed and prices it. The two together say the sophistication an individual ad request receives is a spend decision made on the platform's side, with no advertiser input and no readout."""

AM076 = u"""**Re-check number five, 2026-11-19, and this one moves the boundary a step closer.** Muse added Loblaw on 18 November as its first Canadian retail partner connector, the fifth Muse post this claim has read. Again **no advertising content**: one occurrence of the word ads anywhere on the page, in site furniture. The launch-day sentence is not repeated, so this is again an absence of contradiction rather than a renewal. **What is new is that a purchase now completes inside the agent.** Loblaw brings its catalogue in, and "Canadian shoppers can now ask Muse to help with meal planning, build their basket and check-out, all in Muse", with Muse remembering brand preferences and food allergies between sessions. Payment methods and credentials sit in Muse Secure VM and out of the agent's view, and the agent asks before a purchase. **Two things follow and neither is a contradiction yet.** First, a transaction completed inside Muse touches no website, so it fires no pixel and has no landing page, which is a conversion an advertiser could not measure even if an ad surface existed. Second, remembered brand preferences are exactly the standing intent data the banked sentence says does not reach the ad systems, and they now accumulate against a named retailer's catalogue. There is still no ad inventory, no lead capture and no advertiser-facing surface of any kind. Voice rolled out in Canada and user-built "spaces" shipped in the same post; neither carries advertising content. Re-check again on the next Muse post."""

LOOM_NOTE = (u"**Independent source add, 2026-11-19.** Jon Loomer names this as one of five tells that a "
             u"Meta practitioner has stopped adapting, with no new evidence and no new detail on the mechanism. "
             u"Recorded as a source rather than as support, because the full checklist and its limits are at "
             u"[[Meta Delivery & Andromeda#MD-203|MD-203]], tiered T4.")

mh.mint(MD, "MD-202",
        "A proven ranking improvement takes OVER A YEAR to reach every model it applies to, so Meta's ads "
        "model fleet is never uniform at any moment in time",
        "T1", "active", MD202, [SRC_SMT, SRC_AGENTS])

mh.mint(MD, "MD-203",
        "A long-standing Meta practitioner publishes a five-item test for whether a source has stopped "
        "keeping up, and names the conflict of interest that produces it",
        "T4", "active", MD203, [SRC_LOOMER])

mh.mint(AU, "AU-103",
        "A deployed real-time-bidding system publishes the whole trade: compressing user history for ad "
        "ranking bought +4.65% advertiser conversion value and +2.96% clicks for 15% more inference cost",
        "T1", "active", AU103,
        ["arXiv 2611.24283v1 [cs.IR], X-split Argus: Learning Reusable History Tokens for Efficient CTR "
         "Prediction, announced 2026-11-19, abstract read 2026-11-19 (full paper not opened)"])

mh.mint(GA, "GA-103",
        "Seasonality Adjustments are now available in Demand Gen, which is the first bid control in that "
        "campaign type for a short promotion",
        "T1", "active", GA103,
        ["Google Ads & Commerce blog, Win the holiday shopping season with November's Demand Gen Drop., "
         "2026-11-18, blog.google/products/ads-commerce/demand-gen-drop-november-2026/, read in full 2026-11-19"])

mh.amend(MD, "MD-198", AM198, [SRC_SMT])
mh.amend(MD, "MD-199", AM199, [])
mh.amend(LS, "LS-076", AM076,
         ["Meta Newsroom, Meta Welcomes Loblaw as First Canadian Retail Partner to Muse, 2026-11-18, "
          "about.fb.com/news/2026/11/meta-welcomes-loblaw-as-first-canadian-retail-partner-to-muse/, "
          "read in full 2026-11-19 (no advertising content)"])

for fn, cid in [(MD, "MD-052"), (MD, "MD-075"), (MD, "MD-015"), (SC, "SC-014"), (LS, "LS-006")]:
    mh.amend(fn, cid, LOOM_NOTE, [SRC_LOOMER])

total, tiers, stat, per = mh.audit()
print("TOTAL CLAIMS", total)
print("TIERS", tiers)
print("STATUS", stat)
