# -*- coding: utf-8 -*-
"""Claim merge, research run 2026-10-14.

Sources read in full today:
  1. Engineering at Meta, "Meta's Generative Ads Model (GEM): Scaling the Central
     Model and Compute Engine for Frontier Ads AI", 2026-10-13.
     cache/fb-eng-gem-20261014.html
  2. Google Ads & Commerce Blog, "Build your data strength with October's Demand
     Gen drop.", 2026-10-13, body AND footnote.
     cache/google-dg-drop-oct2026.html
  3. Ben Heath, "NEW Way To Test Facebook Ads!", 2026-10-13, 4172-word transcript.
"""
import io
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
V = Path(r"E:\claude code marketing skill\Obsidian God-level Marketing Vault\God-level Marketing\wiki\science")
MD = V / "Meta Delivery & Andromeda.md"
CR = V / "Creative Science.md"
GA = V / "Google Auction & Smart Bidding.md"
LS = V / "Learning & Signal.md"


def read(p):
    return p.read_text(encoding="utf-8")


def write(p, s):
    p.write_text(s, encoding="utf-8")


def sub(hay, needle, repl, label):
    n = hay.count(needle)
    if n != 1:
        raise SystemExit("ANCHOR %s matched %d times, aborting" % (label, n))
    return hay.replace(needle, repl)


# ---------------------------------------------------------------- Meta Delivery
md = read(MD)

a = "Named, dated updates cited from Meta engineering posts."
md = sub(md, a, a + (
    "\nADDED 2026-10-14: the timeline now has a 2026 generation of GEM, published "
    "2026-10-13, which consolidates the per-surface and per-objective prediction "
    "systems into one central model. Entry at [[Meta Delivery & Andromeda#MD-176|MD-176]], "
    "its published numbers at [[Meta Delivery & Andromeda#MD-177|MD-177]], its new "
    "architecture at [[Meta Delivery & Andromeda#MD-178|MD-178]]."
), "MD-004 tail")

a = ("Sources: Engineering at Meta, Meta's Generative Ads Model (GEM), 2025-11-10; "
     "Sam Piliero, Meta Ads Insider Exposes How The Algorithm ACTUALLY Works "
     "(with Matt Steiner of Meta), 2026-06-04\nLast touched: 2026-08-19")
md = sub(md, a, (
    "THE 2x NOW HAS A NAMED MECHANISM, 2026-10-14. The 2026-10-13 post calls it "
    "LoopFM, a precomputed structure representation that carries GEM's compressed "
    "internal layers plus the representations the model previously generated for "
    "the same user. Full entry, with the speculative-precomputation path that "
    "delivers it, at [[Meta Delivery & Andromeda#MD-179|MD-179]].\n"
    "Sources: Engineering at Meta, Meta's Generative Ads Model (GEM), 2025-11-10; "
    "Sam Piliero, Meta Ads Insider Exposes How The Algorithm ACTUALLY Works "
    "(with Matt Steiner of Meta), 2026-06-04; Engineering at Meta, GEM: Scaling the "
    "Central Model and Compute Engine for Frontier Ads AI, 2026-10-13\n"
    "Last touched: 2026-10-14"
), "MD-029 sources")

a = ("Sources: Engineering at Meta, Meta's Generative Ads Model (GEM), 2025-11-10\n"
     "Last touched: 2026-08-18\n\n### MD-031")
md = sub(md, a, (
    "ARCHITECTURE SUPERSEDED 2026-10-14. The InterFormer design named here is the "
    "previous version. Meta's 2026-10-13 post replaces it with Kunlun and states "
    "\"Compared to the previous version (Interformer), Kunlun delivers 2x "
    "performance gains with the same computation scaling.\" This claim stays active "
    "as the dated record of what GEM was built from through August 2026; read "
    "[[Meta Delivery & Andromeda#MD-178|MD-178]] for what it is built from now.\n"
    "Sources: Engineering at Meta, Meta's Generative Ads Model (GEM), 2025-11-10\n"
    "Last touched: 2026-10-14\n\n### MD-031"
), "MD-030 sources")

a = ("These are platform-wide model gains an advertiser inherits without changing "
     "anything.")
md = sub(md, a, a + (
    "\nSUPERSEDED AS THE CURRENT FIGURES, 2026-10-14, AND NOT COMPARABLE TO THE NEW "
    "ONES. Meta's 2026-10-13 post publishes 18.9% conversion and 12% CTR "
    "improvement for the 2026 generation, plus a separate 5.8% / 4.1% / 1.6% set "
    "for Facebook, Instagram and off-site conversion. Different periods, different "
    "populations, no shared baseline, so the two generations' numbers cannot be "
    "lined up or subtracted. Entry and the reasons not to quote either at "
    "[[Meta Delivery & Andromeda#MD-177|MD-177]]."
), "MD-031 body")

a = ("Sources: Engineering at Meta, Training GEM at LLM Scale, 2026-08-03\n"
     "Last touched: 2026-08-18")
md = sub(md, a, (
    "RESTATED UNCHANGED BY A SECOND POST, 2026-10-14. The 2026-10-13 post repeats "
    "the same two figures in substance, \"doubled GEM's E2E training efficiency to "
    "20-25% MFU over the past 12 months while scaling total training FLOPs by 4x\", "
    "and adds the decomposition Meta optimises against: E2E MFU = Local MFU x "
    "Scaling Ratio, compute efficiency times how much single-GPU performance "
    "survives distribution across thousands of GPUs. Two posts ten weeks apart "
    "carrying identical numbers means the 4x and the 20-25% describe one "
    "achievement, not two rounds of it.\n"
    "Sources: Engineering at Meta, Training GEM at LLM Scale, 2026-08-03; "
    "Engineering at Meta, GEM: Scaling the Central Model and Compute Engine for "
    "Frontier Ads AI, 2026-10-13\n"
    "Last touched: 2026-10-14"
), "MD-032 sources")

a = ("**Guards.** Staged rollout, so absence in an account says nothing. No "
     "percentage default is stated, no duration range is stated, and nobody has "
     "shown performance data with it on. Availability across our five accounts is "
     "unchecked.\nSources: Jon Loomer, Dont Get Attached to Your Ad Process, "
     "2026-05-04; Jon Loomer, Every Change You Make Should Solve a Problem, "
     "2026-06-08\nLast touched: 2026-08-27")
md = sub(md, a, (
    "**Guards.** Staged rollout, so absence in an account says nothing. Nobody has "
    "shown performance data with it on. Availability across our five accounts is "
    "unchecked.\n"
    "**TWO OF THOSE GUARDS CLOSED 2026-10-14, read off the live product.** Ben "
    "Heath, 2026-10-13, demonstrating it in a client account: the defaults are "
    "**20% of daily budget and 7 days**, and the field reads \"what percent of "
    "budget spent per day should go to test ads\". Meta's own in-product copy, "
    "quoted: \"help ensure your ad gets delivery by dedicating budget to it\", and "
    "after the window \"your ad will use your existing budget after its end\". Path, "
    "matching MD-103 exactly: ad level, ad setup, beneath multi-advertiser ads, Show "
    "more settings. Spend is averaged rather than fixed daily, demonstrated on a "
    "$150 campaign budget at 20%: Meta says it aims to spend an average of $30 a day "
    "and will fluctuate day to day. The 1-to-30-day range stays with MD-103; Heath "
    "says he runs it as long as a month on low-volume accounts and that the window "
    "can be re-run when the first one returned too little data.\n"
    "**ROLLOUT, FIRST REAL FRACTION ON FILE.** \"It's available in about half of our "
    "ad accounts at this point across the board.\" One agency's book, no account "
    "count given, but it is the first time anyone has put a fraction on it, and it "
    "means an account without the control in October 2026 is ordinary rather than "
    "unusual.\n"
    "**IT IS MUTUALLY EXCLUSIVE WITH META'S CREATIVE TESTING TOOL, AND THE PRODUCT "
    "ENFORCES IT.** With push delivery on, the Creative testing section greys out "
    "and reads: \"you're pushing delivery to one or more ads in this campaign. You "
    "can only set up a creative test after these push delivery periods have ended.\" "
    "The block is at CAMPAIGN scope, not ad set, so one ad under push delivery locks "
    "creative testing out of the whole campaign. Switching push delivery off restores "
    "the creative-test flow immediately. This is the first hard constraint on file "
    "between the two controls and it fixes the order of operations: you cannot run "
    "both in one campaign in one window. The tool on the other side of the lock is "
    "[[Creative Science#CR-113|CR-113]].\n"
    "**His selection rule between the two, T3, and it is indexed to conversion "
    "volume rather than to budget.** Push delivery moves one ad at a time, so it "
    "reaches a verdict faster in a thin account; the creative testing tool takes 2 to "
    "7 ads at once and therefore needs several times the conversions to fill. \"In a "
    "lot of ad accounts where they're generating a conversion or two a day. If you "
    "set up a creative test with 5 [ads], you're going to have to run that test for a "
    "month or longer to get enough data, maybe more.\" His stated testing budget band "
    "is 10 to 50 or 60% of spend, falling toward 10 to 20% when current results are "
    "good and rising to 100% when the account is not converting at all, and he says 30 "
    "to 40% of his agency's annual Meta spend is testing new ads. Two further T3 rules "
    "from the same session: use it for a format, hook, avatar or angle change rather "
    "than for a background colour, and do not run either tool through a one-off peak "
    "event such as Black Friday, where the long-run payoff window does not exist and "
    "consolidation onto the proven ads is the point. Honesty note on the spend figure: "
    "the auto-transcript mangled the dollar amount (\"more than $und00 million a "
    "year\"), so the 30 to 40% share is usable and the absolute is not.\n"
    "Sources: Jon Loomer, Dont Get Attached to Your Ad Process, 2026-05-04; Jon "
    "Loomer, Every Change You Make Should Solve a Problem, 2026-06-08; Ben Heath, NEW "
    "Way To Test Facebook Ads!, 2026-10-13 (UI shown)\n"
    "Last touched: 2026-10-14"
), "MD-141 guards")

NEW_MD = """
### MD-176 \u00b7 The 2026 generation of GEM replaces the per-surface, per-objective prediction systems with ONE central model that predicts clicks across every surface and conversions across every objective, and Meta says the click-rich data carries the conversion-sparse data
Tier: T1 \u00b7 Status: active
Engineering at Meta, 2026-10-13, read in full. Page cached at `cache/fb-eng-gem-20261014.html`.
The structural sentence: "The 2026 generation of GEM shifts from isolated per-domain optimizations - such as Facebook, Instagram, Reels - to a single central foundation model." And the one that says what the model now outputs: "GEM powers the first optimized model that jointly predicts both CTR across all the surfaces and conversion rate (CVR) across the major optimization goals. Previously, each surface and each prediction objective had its own system."
**The claim inside it that matters to a thin account**, quoted: "The generalizable representations learned on data-rich click tasks transfer into data-sparse conversion tasks." Meta is stating that the abundant signal, clicks, now pays for the scarce signal, conversions, inside one model.
**Two mechanisms Meta names for making heterogeneous training tractable.** A cost-free data mixing strategy: virtual data loading from different combinations of data pipelines without physically merging them, with a mixture controller that holds offline and online mixture proportions "close to the real datastream order received in real time, mitigating instability for domain switch and overmemorization for the recent domain data". And a domain expert framework: one shared expert learning the unified representation across all domains plus domain-specific experts for surface-specific patterns, both built on the Kunlun framework at [[Meta Delivery & Andromeda#MD-178|MD-178]].
**Read the transfer claim for exactly what it is.** It describes transfer inside Meta's own foundation model. It does not change the account-level exit condition at [[Learning & Signal#LS-002|LS-002]], roughly 50 optimisation events in 7 days, and it gives no account a way to borrow conversion volume it does not have. The honest operator version is narrower and still worth having: a low-volume conversion objective is being predicted by a model that learned from click behaviour at platform scale, which is an argument against the folklore that a small account's model starts from nothing.
**What is not said.** No share of traffic, no statement of how much of a sparse objective's prediction quality comes from transfer, and no number of any kind in this section. Meta also confirms the downstream vertical models "still train with the specific surface or traffic data", which is exactly why the data mixing had to be virtual rather than a real merge.
Sources: Engineering at Meta, GEM: Scaling the Central Model and Compute Engine for Frontier Ads AI, 2026-10-13, read in full
Last touched: 2026-10-14

### MD-177 \u00b7 Meta's published numbers for the 2026 GEM generation are 18.9% more conversions and 12% higher CTR, plus a separate 5.8% / 4.1% / 1.6% set, and the post carries no footnote of any kind
Tier: T1 for the statement \u00b7 Status: active
The sentence in full: "GEM has delivered 18.9% conversion improvement and 12% ad click-through rate (CTR) improvement across Meta's ad surfaces and objectives, and additionally contributed 5.8%, 4.1%, and 1.6% conversion uplift on Facebook, Instagram, and off-site conversion for targeted users over the past year."
**Five things wrong with it as evidence, all visible in the sentence itself.** The first pair carries no window. The second set carries "over the past year" and is restricted to "targeted users", a term the post never defines. Nothing states whether the second set is a subset of the first, a component of it, or a different measurement, so the two cannot be reconciled, added or subtracted. There is no baseline and no control group. And there is no footnote anywhere in the post, on this figure or any other.
**This is a house construction, not an oversight.** [[Meta Delivery & Andromeda#MD-171|MD-171]] catalogues the unfootnoted platform-improvement figure as a Meta habit, and [[Meta Delivery & Andromeda#MD-162|MD-162]] records that Meta does publish experiment design in a footnote when it chooses to. The absence is a choice.
**Against the previous generation.** [[Meta Delivery & Andromeda#MD-031|MD-031]] holds +5% conversions on Instagram and +3% on Facebook Feed for Q2 2025. The directions agree and the magnitudes are not comparable across the two posts.
**The rule for us, unchanged by a bigger number.** An account inherits whatever share of a platform-wide average its own audience earns, and [[Meta Delivery & Andromeda#MD-090|MD-090]] carries Meta's own statement that the gains concentrate on heavy-engagement users. Never put 18.9% in front of a client as something their account will see, and never put it in a forecast.
Sources: Engineering at Meta, GEM: Scaling the Central Model and Compute Engine for Frontier Ads AI, 2026-10-13, read in full
Last touched: 2026-10-14

### MD-178 \u00b7 GEM's new Kunlun architecture doubles performance at the same compute and carries 2.5x the model complexity, and Meta names the cuts that paid for it
Tier: T1 \u00b7 Status: active
Kunlun replaces the InterFormer design banked at [[Meta Delivery & Andromeda#MD-030|MD-030]]: "Compared to the previous version (Interformer), Kunlun delivers 2x performance gains with the same computation scaling." Meta reports 2.5x model complexity growth from earlier GEM versions and says it observed "an LLM-like scaling law at our largest pre-training scale".
**Each layer has three components:** attention customised to the long dependency pattern in user behaviour, a summarisation component that bridges sequence and non-sequence structure, and a cross-interaction component expanded to a mixture-of-experts design for modelling interactions between the two.
**The efficiency moves, with Meta's own numbers where it gives them.** Block-aligned sparse attention replaces full self-attention and takes complexity from quadratic to linear in window size. Generalized Dot-Product Attention reformulates per-example feed-forward networks into attention operations so they share one GPU kernel, "delivering up to 2x forward speedup". Expert parallelism shards the cross-interaction experts so each GPU processes a subset. CompSkip selectively deactivates sequence modules per layer and routes only the residual: "we reduce FLOPS by 43% with negligible quality loss". OneSeq unifies heterogeneous user sequences chronologically after event-feature aggregation, because a purchase event is described by ad ID and account ID while a post event is described by actors and object ID, and the two cannot be merged at the data-source level.
**The sentence to keep for law 1.** Meta defines its feature taxonomy as "non-sequence features (such as user demographics, ad content representations), and sequence features with a sequence of events". That is the second T1 statement placing the ad creative's representation in the model's first-class feature set, after [[Meta Delivery & Andromeda#MD-120|MD-120]], and the first to put it beside demographics inside a standing architecture definition rather than as a passing example.
No operator lever here. Bank it because it dates the architecture and because the taxonomy is evidence.
Sources: Engineering at Meta, GEM: Scaling the Central Model and Compute Engine for Frontier Ads AI, 2026-10-13, read in full
Last touched: 2026-10-14

### MD-179 \u00b7 Meta precomputes the user-ad score BEFORE the request needs it, and when the exact pair is missing it substitutes the user's own recent embeddings for the same ad group or borrows from behaviourally similar users
Tier: T1 \u00b7 Status: active
Two post-training systems in the 2026-10-13 post, and the second carries the only cold-start description Meta has ever published.
**LoopFM, the transfer mechanism.** A precomputed structure representation: Meta compresses GEM's intelligence into compact representations "summarized from the important layers", then structures each one together with the representations the model previously generated for the same user into a sequential context window, "capturing user intent dynamics across all surfaces and traffic through GEM's memory". Downstream models read that long historical context during both training and inference. Meta states it achieves "2x of transfer effectiveness beyond knowledge distillation", at no additional foundation-model cost, because the representation generation shares computation with the soft-label generation knowledge distillation already needed. This names the mechanism behind the bare 2x figure carried at [[Meta Delivery & Andromeda#MD-029|MD-029]].
**Solaris, the timing mechanism.** "Evaluating the large-scale model inside a live ad request is not affordable", so Meta moves the work in time instead of cutting it. As multi-stage ranking narrows a live request to its top ad candidates, Solaris evaluates those user-ad pairs with the foundation model in asynchronous background jobs carrying no latency budget, then delivers the embeddings just-in-time on the serving hot path. Meta says the idea is borrowed from speculative decoding in LLM serving. The output is per-pair, not per-user: "giving vertical models real-time, point-to-point knowledge of how a specific user is likely to act on the exact ad candidate".
**The degradation rule, quoted in full, because this is the operator-relevant part.** "When an exact user-ad embedding is unavailable, the system degrades rather than drops. It substitutes an aggregate of the user's own recent embeddings across the same ad groups, or borrows from behaviorally similar users."
**What that settles and what it does not.** It settles that a user-ad pair with no history is not scored from zero: it inherits an aggregate at the ad-group level, and failing that, a behavioural neighbour's. It does not define "ad groups" in Meta's internal taxonomy, and that phrase is not an Ads Manager object, so nobody may map it onto ad sets or campaigns. It quantifies nothing: no share of requests served by either fallback and no accuracy cost for either. Do not build a structural rule on it.
**Where it lands on an argument this codex has been running.** The fight at [[Meta Delivery & Andromeda#MD-067|MD-067]] and [[Scaling Models#SC-009|SC-009]] over new ads taking no spend has been argued with nothing on file about how Meta scores an ad it has never served. This is that missing middle, from Meta, and it describes borrowed intelligence rather than a cold start. It also pairs with [[Meta Delivery & Andromeda#MD-174|MD-174]]: both systems move foundation-model work off the live request, one into idle capacity and one into asynchronous background jobs, so they are two halves of the same budget.
Sources: Engineering at Meta, GEM: Scaling the Central Model and Compute Engine for Frontier Ads AI, 2026-10-13, read in full
Last touched: 2026-10-14

### MD-180 \u00b7 Sequence length is its own scaling law: prediction quality follows a POWER LAW in how much engagement history the model reads, and larger models gain disproportionately from longer history
Tier: T1 \u00b7 Status: active
"GEM scaled the long engagement context length by 2x in production, and further enabled the capability of scaling long context to 25x, demonstrating infrastructure capability at frontier scale." So 2x is shipped and 25x is demonstrated, and the post is explicit about which is which.
**Three findings, quoted.** "Prediction quality follows a power law with sequence length. The relationship is predictable and consistent across sequence lengths." "Larger models benefit disproportionately from longer sequences." And the compounding statement: "The two scaling laws reinforce each other", because scaling compute makes the model bigger which makes longer sequences more valuable, and scaling sequence length makes the model more accurate which justifies more compute.
**The uncomfortable operator read, and it is the reason to bank this.** The input Meta is scaling hardest is the user's own engagement history. No advertiser controls it and no setting in Ads Manager touches it. Three separate T1 statements now say the same thing from three directions: compute is allocated by how much history a person carries ([[Meta Delivery & Andromeda#MD-090|MD-090]]), ranking depth varies with available capacity ([[Meta Delivery & Andromeda#MD-174|MD-174]]), and the better model is routed by predicted engagement ([[Meta Delivery & Andromeda#MD-175|MD-175]]). Quality of match is substantially a function of what the platform already knows about the person. The account's levers stay what they were: the creative ([[Meta Delivery & Andromeda#MD-001|MD-001]], [[Meta Delivery & Andromeda#MD-120|MD-120]]) and the quality of the signal it returns.
**The gap this opens, and it is cheap to close.** Nothing on file measures whether our own accounts' results differ by how platform-active the buyer is. Our clinics and our truck dealers sell to light platform users. If the published gains concentrate where engagement history is deep, our book inherits the least of them, and we have never checked.
Sources: Engineering at Meta, GEM: Scaling the Central Model and Compute Engine for Frontier Ads AI, 2026-10-13, read in full
Last touched: 2026-10-14
"""
md = md.rstrip("\n") + "\n" + NEW_MD
write(MD, md)
print("Meta Delivery: MD-176..MD-180 added; MD-004, MD-029, MD-030, MD-031, MD-032, MD-141 amended")

# -------------------------------------------------------------- Creative Science
cr = read(CR)
a = ("This is the platform-native answer to the problem in [[Creative Science#CR-040|CR-040]] "
     "and [[Scaling Models#SC-020|SC-020]] where new ads dropped into a consolidated ad set "
     "never take spend.")
cr = sub(cr, a, a + (
    "\n**IT CANNOT RUN ALONGSIDE PUSH DELIVERY, CONFIRMED OFF THE PRODUCT 2026-10-14.** "
    "Ben Heath, 2026-10-13: with \"push delivery to this ad\" switched on, this whole "
    "Creative testing section greys out and reads \"you're pushing delivery to one or more "
    "ads in this campaign. You can only set up a creative test after these push delivery "
    "periods have ended.\" The lock is at CAMPAIGN scope, so one ad under push delivery "
    "blocks creative testing across every ad set in that campaign, and switching push "
    "delivery off restores the flow at once. The variant cap still reads 2 to 7. His "
    "selection rule between the two tools, T3, indexes on conversion volume and not on "
    "budget: this tool fills 2 to 7 ads at once and so needs several times the conversions, "
    "which in an account producing one or two conversions a day means \"a month or longer "
    "to get enough data, maybe more\", while push delivery reads out faster because it moves "
    "one ad. Full detail of the other control at "
    "[[Meta Delivery & Andromeda#MD-141|MD-141]]."
), "CR-113 tail")

a = ("Sources: Ben Heath, How To Test Facebook Ads in 2026")
if cr.count(a) == 1:
    pass
write(CR, cr)
print("Creative Science: CR-113 amended")

# --------------------------------------------------- Google Auction & Smart Bidding
ga = read(GA)

a = ("**Standing rule for this series and for Google announcements generally: read the "
     "footnote before you read the sentence.** Most of what is wrong with these figures is "
     "invisible in the body and visible in the footnote, and one whole class of it is "
     "visible only in the absence of a footnote.")
ga = sub(ga, a, a + (
    "\n**CENSUS EXTENDED 2026-10-14. Fifteen instalments, nineteen figures.** The cadence "
    "has now held for fifteen straight months. The October 2026 drop, published 2026-10-13, "
    "adds two figures and both land in constructions already named here. **Figure 18, "
    "Oct 2026:** \"over 20% conversion uplift in Demand Gen campaigns\" for advertisers who "
    "build data strength with Google Tag Gateway. Footnote 1 in full: \"Google Data, Global, "
    "Performance, June 3, 2026 - June 17, 2026.\" A **14-day window**, the shortest behind "
    "any figure in the series, with no advertiser count, no control group and no stated "
    "threshold for what counts as having built data strength. Construction 3, an adoption "
    "comparison printed as a result. **Figure 19, Oct 2026:** The Zebra, 16% more conversion "
    "volume and 19% more conversion value. **No footnote**, which makes it the fourth "
    "footnote-silent figure of nineteen alongside LG Electronics, Cropp and the June 2026 "
    "72%. **The counterfactual count does not move: still three footnotes out of nineteen "
    "name an experiment or an A/B test.** Entry for the drop at "
    "[[Google Auction & Smart Bidding#GA-093|GA-093]]."
), "GA-088 standing rule")

a = ("**Five, a new Data Strength Uplift metric in Google Ads**, which \"calculates the "
     "additional conversions recovered by your first-party data setup.\"")
ga = sub(ga, a, a + (
    "\nSTILL NOT SHIPPED AS OF 2026-10-13, 33 DAYS LATER. Google's October 2026 Demand Gen "
    "drop announces the same three items a second time and in the same forward tense: the "
    "Data Strength Uplift metric \"is launching\", Data Manager \"is expanding\" to DV360 and "
    "Analytics, and enhanced conversions \"will soon be available\" in DV360 and Analytics. "
    "Do not promise a client the column or the DV360 integration off either announcement. "
    "Check the account. See [[Google Auction & Smart Bidding#GA-093|GA-093]]."
), "GA-073 item five")

NEW_GA = """
### GA-093 \u00b7 Google's October 2026 Demand Gen drop re-announces the same three measurement items as September's, still in future tense, and its 20% figure rests on a 14-day window
Tier: T1 for existence and product copy \u00b7 Status: active
Google Ads & Commerce Blog, "Build your data strength with October's Demand Gen drop.", 2026-10-13, body and footnote read in full at source. Page cached at `cache/google-dg-drop-oct2026.html`. Same tier guard as [[Google Auction & Smart Bidding#GA-068|GA-068]]: nothing in it states that Demand Gen performs.
**The three product items, quoted.** The Data Strength Uplift metric "is launching in Google Ads, helping you understand the conversion gains driven by your data setup within the Google Ads UI." Data Manager "is expanding to Display & Video 360 (DV360) and Google Analytics (GA)". Enhanced conversions "will soon be available in Display & Video 360 (DV360) and Google Analytics (GA) to improve measurement accuracy and unlock more powerful bidding."
**All three were already announced 33 days earlier**, in the 2026-09-10 measurement drop at [[Google Auction & Smart Bidding#GA-073|GA-073]]. A month on, one is launching and two are still coming. The operator consequence is small and concrete: a client cannot be promised the Data Strength Uplift column or DV360 enhanced conversions on the strength of an announcement that has now been made twice. Open the account and look.
**The headline figure and what holds it up.** "Based on an internal analysis, advertisers who build their data strength with Google Tag Gateway see, on average, over 20% conversion uplift in Demand Gen campaigns." Footnote 1, in full: "Google Data, Global, Performance, June 3, 2026 - June 17, 2026." Fourteen days. No advertiser count, no control group, and no definition of the threshold that makes an advertiser one who has built data strength. It is an average over self-selected adopters, construction 3 in the census at [[Google Auction & Smart Bidding#GA-088|GA-088]], and the shortest measurement window behind any figure in the series.
**The case study carries no footnote at all.** "Insurance platform The Zebra implemented data strength to achieve a 16% increase in conversion volume and a 19% increase in overall conversion value." No window, no absolute numbers, no comparison basis. Fourth footnote-silent figure in fifteen instalments.
**What the drop does not say, which is the first thing a client asks.** Nothing about whether any of the uplift is incremental. Our own Demand Gen holdout, recorded at [[Google Auction & Smart Bidding#GA-068|GA-068]], found no lift, and a 20% adoption average is not evidence against a holdout. The useful half of this drop is the product news, not the number.
Sources: Google Ads & Commerce Blog, Build your data strength with October's Demand Gen drop., 2026-10-13, body and footnote read in full
Last touched: 2026-10-14
"""
ga = ga.rstrip("\n") + "\n" + NEW_GA
write(GA, ga)
print("Google Auction: GA-093 added; GA-073 and GA-088 amended")

# ------------------------------------------------------------- Learning & Signal
ls = read(LS)
a = ("Three operators, three indexes (spend multiple, conversion volume, fixed clock), and "
     "not one of them ran a test.")
ls = sub(ls, a, a + (
    "\nHEATH RESTATED THE VOLUME INDEX 2026-10-13 AND ADDED THE REFUSAL THAT GOES WITH IT. "
    "His sharpest formulation of it yet: \"a campaign that has generated 20 conversions in "
    "an hour is just as old... as a campaign that has generated 20 conversions in 2 months. "
    "Time is irrelevant. It's all conversion volume.\" The new part is what he says an "
    "operator may do about a thin account, which is nothing: \"I often get the question of "
    "like, if I've got lower conversion volume, how do I assess performance earlier? You "
    "don't. You can't. You can't cheat the system. You can't use a different metric to try "
    "and work out if this ad's performing well or not. You have to do it based on return on "
    "ad spend, cost per conversion, your northstar metric.\" That is a direct refusal of the "
    "upper-funnel proxy read, hook rate or CTR standing in for a verdict, and it is the "
    "position to quote the next time a client with six conversions a week asks for a weekly "
    "creative call. Asserted, no test, same as everything else in this claim."
), "LS-023 three indexes")
write(LS, ls)
print("Learning & Signal: LS-023 amended")

# ------------------------------------------------------- transcript extracted flag
T = Path(r"E:\claude code marketing skill\Obsidian God-level Marketing Vault\God-level Marketing\wiki\sources\transcripts\ben-heath\2026-10-13--ben-heath--NEW Way To Test Facebook Ads.md")
t = read(T)
t = sub(t, "extracted: false", "extracted: true", "transcript flag")
write(T, t)
print("Transcript marked extracted: true")
