"""Merge pass for the 2026-10-20 research run.

Sources actually read today:
  1. Engineering at Meta, "GenRecs Tokenization: Transforming Ads Recommendation at
     Meta with Stable Model Vocabulary", 2026-10-19, read in full.
  2. arXiv 2607.25346 "The Case Against Generation for Retrieval" (abstract).
  3. arXiv 2602.07774 "GR2: Generative Reasoning Re-ranker" (abstract).
  4. arXiv 2607.10016 "Tokenizing Numerical and Embedding Features for LLM RecSys" (abstract).
  5. arXiv 2610.25748 "MAPS" (abstract), 2603.02137v2 "NextAds" (abstract).
  6. Meta for Business News, "agencies-testing-incrementality", dated 2026-10-19, read in full.

6 new claims, 12 merges.
"""
import re
from pathlib import Path

SCI = Path(r"E:\claude code marketing skill\Obsidian God-level Marketing Vault"
           r"\God-level Marketing\wiki\science")
TODAY = "2026-10-20"

MD = SCI / "Meta Delivery & Andromeda.md"
CR = SCI / "Creative Science.md"
AT = SCI / "Attribution & Incrementality.md"
AU = SCI / "Auction Mechanics & Bidding.md"

GENRECS_SRC = ("Engineering at Meta, GenRecs Tokenization: Transforming Ads Recommendation "
               "at Meta with Stable Model Vocabulary, 2026-10-19, read in full 2026-10-20")

NEW = {}

NEW[MD] = [r"""
### MD-184 · Meta replaced the per-item ID with a stable semantic vocabulary built from the ad's own text and images, and the only published outcome is +0.35% conversions
Tier: T1 · Status: active
Published 2026-10-19 and read in full. GenRecs Tokenization is the data layer under the generative
ads stack: "Rather than maintaining a dedicated ID for every item, GenRecs Tokenization represents
each item with a set of tokens from a stable semantic vocabulary." Scope is stated as every item
type in the system, "including ads, products, pages, and pixels", across both retrieval and ranking.

**How an ad becomes tokens, in Meta's own order.** "Pre-trained multimodal models read each ad,
product, and page, including its text and images, and encode the items into an embedding that
carries world knowledge. The tokenizer combines that content signal with representations learned
from how people engage with the items, then quantizes the result into a short sequence of discrete
tokens." The pipeline is three stages: **encode** the item into a semantic embedding space,
**decompose** that embedding into independent subspaces, **quantize** by mapping each subspace to a
codebook entry. For many ad representations Meta says it uses prefix n-grams combining a learned
encoder, residual decomposition, learned vector codebooks and token parametrization.

**The sentence that matters for law 1.** The model's representation of an ad is built from that ad's
text and its images. This is the third T1 statement placing the creative's own content inside the
first-class feature set, after [[Meta Delivery & Andromeda#MD-120|MD-120]] and
[[Meta Delivery & Andromeda#MD-178|MD-178]], and it is the first that describes the pixels being
read as an input rather than naming "ad content representations" in a taxonomy.

**The number, and read it slowly.** "Paired with Meta's GEM and Adaptive Ranking Model, GenRecs
Tokenization delivered a +0.35% lift in conversions." The footnote reads, in full: "Meta Internal
Data, measured in February 2026." **Four defects, three of which the footnote creates rather than
cures.** The attribution is joint across three systems, so no part of the 0.35% is separable to
tokenization. The measurement is dated February 2026 and published in October 2026, an eight-month
lag, with nothing said about whether it still holds. No population, no window, no control group and
no sample appear anywhere. And a footnote exists this time, which is the first on a Meta ads figure
this engine has recorded since [[Meta Delivery & Andromeda#MD-162|MD-162]], yet it names only the
data owner and a month. **So the rule at [[Meta Delivery & Andromeda#MD-171|MD-171]] gets a sharper
edge: the presence of a footnote is not the test, the presence of a population and a counterfactual
is.** A footnote that says "internal data, February" satisfies nothing.

**The magnitude is the other finding, and nobody at Meta draws attention to it.**
[[Meta Delivery & Andromeda#MD-177|MD-177]] carries GEM's published 18.9% conversion improvement.
This post attributes +0.35% to the trio including GEM. The two figures are not reconcilable, are not
stated to be measuring the same thing, and sit two orders of magnitude apart. **Never put either in
front of a client, and never put the pair in a forecast.**

**One mechanism claim with no lever attached, banked because it is testable from outside.** Meta says
tokenizer quality can be read without training a ranking model, on three intrinsic measures: cluster
purity, distribution balance and codebook utilization. "Across the eight tokenizer versions we
tested, we see a strong correlation between these intrinsic quality metrics and downstream ranking
prediction accuracy." No correlation coefficient, no scatter and no sample size is published, so
"strong" is unquantified. There is nothing here an advertiser touches.

**What is NOT here.** No statement that an advertiser should change anything. No eligibility, no
rollout scope, no surface list, no date on which tokenization reached any account. Treat it as a
description of the machine, not a lever.
Sources: """ + GENRECS_SRC + r"""
Last touched: """ + TODAY + "\n",

r"""
### MD-185 · A new ad inherits the model's representation of semantically similar items BEFORE anyone sees it, and Meta now states cross-campaign transfer in its own words
Tier: T1 · Status: active
The item-side half of a mechanism this codex has only ever held from the user side. The 2026-10-19
GenRecs Tokenization post, read in full.

**The cold-start sentence, quoted.** "Because tokens describe what an item (e.g., ads, products,
services, etc.) is, the model can relate an item it has never seen engagement for, to items it knows
well. A newly launched 'trail shoe' inherits what the model has already learned about that category,
rather than starting a new representation with no signal." And the timing, stated outright: "When a
sportswear brand launches next season's trail shoe, tokenization lets the new product and its ads
build on what the model learned from last season's shoe, **even before anyone sees the new ad.**"

**Where it lands.** [[Meta Delivery & Andromeda#MD-179|MD-179]] holds Meta's only published cold-start
path and it is user-side: a missing user-ad pair inherits an aggregate of that user's own recent
embeddings, or a behavioural neighbour's. This is the item-side counterpart, and the two together
mean neither side of the pair starts from zero. It also upgrades the evidence under
[[Creative Science#CR-003|CR-003]], which has carried content-feature cold start since August on a
single sentence from a different post; this one names the mechanism.

**Cross-campaign transfer is now a T1 sentence.** "Enabling cross-campaign transfer: Semantic
tokenization creates a stable vocabulary that allows the models to carry insights across campaigns
for advertisers." [[Meta Delivery & Andromeda#MD-070|MD-070]] has carried that as a T3 practitioner
assertion since August, that a proven asset keeps what it has learned when moved to another campaign.
**The direction is now confirmed by Meta. The claim is not, and the difference is load-bearining.**
Meta is describing the MODEL's representation of an item transferring across campaigns. MD-070 is
about an ad object's delivery performance transferring. Those are different things, and a run that
reads the first as proof of the second has mis-banked it. What is established is that the system does
not treat the same product in a new campaign as a stranger. What is not established is that an ad
object carries its own history, or that re-uploading a winner skips anything.

**Where the benefit is claimed to concentrate, and it is not our book.** Meta names two beneficiaries.
"Tokenization maximizes the efficiency of high-volume campaigns by uncovering deeper semantic patterns
across their vast product catalogs", which is a large-catalogue e-commerce advertiser. And "For tail
ads that accumulate fewer impressions, tokenization enables ads recommendation models to generalize
across them via shared content structure, recovering cold-start performance". Its own forward-looking
section says "Tail ad inventory is where semantic tokens contribute most and where advertiser impact
is largest." **Our clients are local service businesses with a handful of services and no catalogue,
so they sit in neither named group squarely.** The tail-ad argument is the closer of the two, since a
four-figure monthly budget accumulates few impressions per ad. Nothing is quantified for either group.

**The flywheel, asserted and unmeasured.** "By improving tail ad prediction quality, tokenization not
only lets tail ads be ranked accurately, but also improves the training data, which then improves
prediction quality for all ads." No figure, no window, no measurement of either leg.

**Announced and not shipped, so nobody may plan on it.** Fully verbalized tokenization is stated to
need "context windows that are impractical at ads scale", and Meta is "combining compacted verbalized
tokens with semantic IDs". A single token space spanning text, image, audio and video across surfaces
is described as exploration, in the conditional: "we are exploring whether".
Sources: """ + GENRECS_SRC + r"""
Last touched: """ + TODAY + "\n",

r"""
### MD-186 · "Generative recommenders" does NOT mean Meta retrieves or writes ads generatively, and Meta's own cited retrieval paper is titled "The Case Against Generation for Retrieval"
Tier: T1 · Status: active
A reading rule, and the sharpest thing found on 2026-10-20. Same shape as the scaling-axis rule at
[[Auction Mechanics & Bidding#AU-085|AU-085]]: one word in a Meta post means something narrower than
it reads.

**The framing in the post.** "Generative Recommenders (GenRecs) represent a paradigm shift from
scoring every ad to reasoning about ad content and user preferences together", and GenRecs "shifts
our approach from scoring every individual ad candidate to leveraging LLM architecture".

**The paper the post cites for that, in the same paragraph.** Under the words "Our work on LLM-native
retrieval shows how far this can go", the post links arXiv 2607.25346. Its title is **"The Case
Against Generation for Retrieval: Discriminative Language Models as Effective Retrievers"**, and two
of its six authors, Carl Hu and Justin Johnson, are the first two authors of the blog post itself.
Its abstract states that deploying LLMs "as generative recommenders or zero-shot rankers at web-scale
remains bottlenecked by prohibitive computational overhead and grounding challenges", that it
"revitalize[s] the classic, highly efficient two-tower retrieval architecture by adapting LLMs as
semantic representation backbones **rather than generative engines**", and concludes that "the
traditional two-tower paradigm remains an exceptionally competitive and practical solution for
industrial retrieval systems". It reports internal production results as "substantial topline
retrieval improvements along with high resilience to model staleness and superior data scaling",
with no figure attached to any of the three.

**So the resolution, and it is not a contradiction.** What is generative is the **representation**:
items are described by composed semantic tokens instead of opaque IDs. The retrieval mechanism stays
discriminative two-tower scoring. **Nothing in either source says Meta generates an ad, writes copy,
or produces creative.** A run that carries "Meta is generative now" into a client conversation has
invented a capability, and the clearest refutation is Meta's own citation.

**Two further details from the cited stack, both abstracts read at source.** GR2 (arXiv 2602.07774,
Meta authors) names **reranking** as a third stage distinct from retrieval and ranking, which this
codex's cascade claims at [[Meta Delivery & Andromeda#MD-022|MD-022]] do not separate, and reports a
failure mode worth knowing: "LLMs tend to exploit reward hacking by preserving item order" when
rewarded on reranking. Its reported gains, +2.4% Recall@5 and +1.3% NDCG@5 over OneRec-Think, are
offline benchmark metrics on two public datasets, not a deployed outcome, and must never be quoted as
a performance figure. And the tokenizer is not text-only: arXiv 2607.10016 maps continuous numerical
features and dense embeddings into the LLM embedding space as soft tokens, on three Amazon
benchmarks, which is consistent with the post's "combines that content signal with representations
learned from how people engage".

**Guards.** The two arXiv papers document Meta-authored research, not necessarily shipped Meta
production, and only the abstracts were read today. Benchmark deltas on public datasets say nothing
about any ad account.
Sources: """ + GENRECS_SRC + r"""; arXiv 2607.25346, The Case Against Generation for Retrieval, abstract read at source 2026-10-20; arXiv 2602.07774, GR2: Generative Reasoning Re-ranker, abstract read at source 2026-10-20; arXiv 2607.10016, Tokenizing Numerical and Embedding Features for LLM RecSys, abstract read at source 2026-10-20
Last touched: """ + TODAY + "\n"]

NEW[CR] = [r"""
### CR-287 · A deployed video-ad system published an online A/B for per-user GENERATED creative, and the honest read of its numbers is narrower than the headline
Tier: T2 · Status: active
Two arXiv papers on the same day, 2026-10-20, both arguing that a fixed set of pre-produced creatives
is now the binding constraint on personalisation. Abstracts read at source. **Neither documents Meta
and neither may ever be quoted as documentation of Meta.**

**MAPS (arXiv 2610.25748), the one with a production number.** Four collaborating agents form a
closed loop: user profile modelling, script generation, video synthesis, and feedback-driven
refinement, with the script-writing agent trained by reinforcement learning against a
multi-dimensional reward. Reported: "Online A/B experiments in a specific scenario in the Kuaishou
advertising system show that MAPS improves CTR by 2.87%, CVR by 2.74%, and ARPU by 9.85% **over the
generative baseline**."

**The three words that change what those numbers mean.** The comparison is against a *generative*
baseline, not against retrieval from a pre-produced set. So the paper's motivation is
generation-versus-retrieval and its measurement is not. **Nothing here quantifies what generated
creative buys over a human-made creative library, and a run that reports it that way has
over-claimed.** What the A/B measures is one generation method against another.

**What is still worth keeping.** ARPU moved 9.85% against CTR 2.87%, so roughly three quarters of the
value landed downstream of the click rather than at the click. That is the same place our own
arguments live: [[Auction Mechanics & Bidding#AU-097|AU-097]] puts a CPM-down, CPA-up account's loss
in conversion rate and offer, not in targeting. A creative system that moves ARPU three times as hard
as it moves CTR is being paid for match quality, not for attention.

**NextAds (arXiv 2603.02137v2), the vision half, and it is T4.** A position paper proposing a
generation-based paradigm with an agentic planning, generation, verification and reflection loop, plus
creatives that "evolve across impressions through feedback-driven refinement and progressive
storytelling". Its own stated result is mixed: exploratory experiments on "lightweight benchmarks,
revealing both the promise and limitations of existing GenAI". **It is a research agenda, it decides
nothing, and the T4 tier is the whole of its weight here.**

**Guards, all load-bearing.** Kuaishou, a Chinese short-video platform, with its own auction, its own
users and its own creative norms. Authors reporting on their own system. "A specific scenario" is
undefined, and no sample size, test duration, spend level or vertical is published. The optimised
metrics are platform CTR, CVR and ARPU, not an advertiser's cost per lead. **The percentages sit on
someone else's baseline and must never be quoted to a client or used in a forecast.**

**Why bank it at all.** Nothing to do this week. It dates the direction: two independent 2026 papers
say the pre-produced creative set is the ceiling, and on the same day Meta published
[[Meta Delivery & Andromeda#MD-184|MD-184]], which makes the creative's own content the model's
representation of it. Three sources, one week, same direction, and
[[Meta Delivery & Andromeda#MD-186|MD-186]] is the guard that stops it being read as Meta writing ads.
Sources: arXiv 2610.25748, MAPS: A Multi-Agent Personalized Script-Driven Video Advertising System Enhanced by Reinforcement Learning, abstract read at source 2026-10-20 via cs.IR feed; arXiv 2603.02137v2, NextAds: Towards Next-generation Personalized Video Advertising, abstract read at source 2026-10-20 via cs.IR feed
Last touched: """ + TODAY + "\n"]

NEW[AT] = [r"""
### AT-131 · Meta published four agency lift studies with eleven numbers and NO footnote, no sample, no window and no spend on any of them, and one is a car-dealership cross-channel read
Tier: T1 for the sentences · Status: active
Meta for Business News, "agencies-testing-incrementality", dated 2026-10-19, read in full 2026-10-20.
Four agency cases, each a Meta lift study. Every number below was quoted verbatim from the page.

**Tinuiti and DSW.** Campaign structure rebuilt to feed in-store sales alongside online tracking.
"The new setup drove 23% more total purchases, 45% more purchases in stores, and a 15% better return
on ad spend."

**WPP Media and Parfums Christian Dior, Taipei.** Meta layered onto existing out-of-home. "Ad recall
increased 10.2 points, the share of people who said they wanted to own the fragrance rose 7.7 points,
and 3.9X lift in incremental sales."

**C-4 Analytics and car dealerships, and this is the one on our book.** The question was whether Meta
ads move search behaviour. "People who saw Meta ads looked at 7.67 times as many vehicle listing
pages. They also generated 14% more paid search traffic."

**AdYogi and Borosil.** "For the group that saw Meta ads, searches for Borosil by name more than
doubled, up 2.2X. Unpaid search traffic rose 24%. Across all types of search combined, the lift was
17%."

**The evidence state, checked and stated plainly: no footnote present.** No asterisk note, no source
note, no "Meta internal data" line, no study date, no sample size and no test duration appears
anywhere on the page. No spend level is given for any of the four. The cases are agency-supplied, and
agencies submit the tests that worked. **So this is the fifth Meta page in six weeks carrying
numbers without a population or a window**, after [[Meta Delivery & Andromeda#MD-171|MD-171]],
[[Meta Delivery & Andromeda#MD-177|MD-177]], [[Marketing Math & Unit Economics#MM-230|MM-230]] and
[[Meta Delivery & Andromeda#MD-181|MD-181]]. Carry the direction, never the digits.

**The one thing it does better than most Meta pages, and the limit of it.** The counterfactual is at
least named: the method is described as comparing an exposed group against "a randomly selected
control group", and the page states the principle as "when you look at the results of your ads, you
should consider how much of this would have happened anyway". Randomised holdout is the right
instrument and it is Meta's own tooling, so the design is better than an adopter-versus-non-adopter
comparison. **What is still missing is every parameter of it**: holdout share, duration, power, and
whether each quoted figure is the study's primary metric or one read off a panel of many. A lift
number with no sample and no window cannot be checked and cannot be forecast from.

**Why the dealership case is worth more to us than the other three.** We run two commercial truck
dealerships on Meta, both reported on last-click. This is Meta's own published claim that its ads move
downstream search behaviour, 7.67x vehicle listing page views and 14% more paid search traffic, for
exactly our vertical. It is direction-only and the digits are unusable, but it is T1-adjacent support
for the standing rule that a zero-lead last-click column is **no last-click leads attributed** and
never evidence of waste. It also pairs with [[Attribution & Incrementality#AT-120|AT-120]], where a
geo-tested vendor put 64% of Meta's incremental conversions on new-to-brand customers.

**Where it sits against the rest of the lift record.** [[Attribution & Incrementality#AT-125|AT-125]]
holds Meta's own statement that a Conversion Lift study reaches a reliable read in 2 to 3 weeks at
holiday volume against 6+ weeks in a quiet quarter, and
[[Attribution & Incrementality#AT-070|AT-070]] holds the ~$100,000-a-month gate on Meta's geo lift
product. **This page names no eligibility floor at all, and four-figure monthly budgets are the whole
of our book, so the realistic expectation is still that none of our clients can run one of these.**
The page's closing line, "None of this required extra budget or new technology", is about the test
rather than the account and should not be read as a statement that lift studies are available at any
spend. **Worth one check in a client account before it is mentioned to anyone.** The Google
counterpart banked the day before is [[Attribution & Incrementality#AT-130|AT-130]].
Sources: Meta for Business News, "agencies-testing-incrementality", dated 2026-10-19, read in full 2026-10-20 at facebook.com/business/news/agencies-testing-incrementality
Last touched: """ + TODAY + "\n"]

NEW[AU] = [r"""
### AU-100 · Meta names THREE scaling axes for the tokenized stack and parameter count is not one of them, which is the first Meta-side support for the axis distinction
Tier: T1 · Status: active
One sentence from the 2026-10-19 GenRecs Tokenization post, banked because it advances an open
reading rule rather than because it changes a decision.

**The sentence.** "A new way to scale: Across production ranking and retrieval, tokens bend the
scaling curve along **sequence length, training data, and model architecture**."

**Why it matters.** [[Auction Mechanics & Bidding#AU-085|AU-085]] opened the rule that this codex must
stop treating "scaling" as one word, after a deployed search-ads system published 90% of its total
gain at its smallest model and found parameter count nearly flat. That distinction was drawn from
non-Meta evidence. **Meta has now published its own list of the axes it is pushing, and parameter
count is absent from it.** Sequence length is the axis already carried at
[[Meta Delivery & Andromeda#MD-180|MD-180]] with a power law attached. Training data and model
architecture are new to the list. Nothing here refutes anything; it means the two sides of the
distinction now both have T1 statements, and the rule stands: **when a source says scaling, ask which
axis before carrying the claim.**

**What is NOT established.** "Bend the scaling curve" is unquantified for all three axes. No curve, no
exponent, no figure and no comparison between the three is published. Meta does not say parameter
scaling is exhausted, only that it is not in this list, and absence from a product post is weak
evidence about an engineering roadmap. No operating consequence this week.
Sources: """ + GENRECS_SRC + r"""
Last touched: """ + TODAY + "\n"]

# ---------------------------------------------------------------- merges
MERGES = [
    (MD, "MD-001",
     "**2026-10-20, the strongest T1 sentence this claim has.** Meta now states that the "
     "representation of an ad is built by reading that ad: \"Pre-trained multimodal models read each "
     "ad, product, and page, including its text and images.\" See "
     "[[Meta Delivery & Andromeda#MD-184|MD-184]]. The practitioner claims in this entry stay T3; "
     "what moved is that the mechanism they assert is now described by the platform in its own words. "
     "Read [[Meta Delivery & Andromeda#MD-186|MD-186]] before carrying the word generative anywhere "
     "near it.",
     GENRECS_SRC),
    (MD, "MD-070",
     "**2026-10-20, the direction is confirmed and the claim is not.** Meta published \"Semantic "
     "tokenization creates a stable vocabulary that allows the models to carry insights across "
     "campaigns for advertisers\" (see [[Meta Delivery & Andromeda#MD-185|MD-185]]). That is the "
     "MODEL's representation of an item transferring, not an ad object's delivery performance "
     "transferring, and the two must not be conflated. **Tier stays T3.** What is now T1 is that the "
     "system does not treat the same product in a new campaign as a stranger. Still unevidenced: that "
     "a re-uploaded winner skips anything, and that a headline or primary-text swap changes the "
     "asset's performance.",
     GENRECS_SRC),
    (MD, "MD-120",
     "**2026-10-20.** Third T1 statement in the series, and the first to describe the pixels being "
     "read rather than naming ad content in a taxonomy. See "
     "[[Meta Delivery & Andromeda#MD-184|MD-184]].",
     GENRECS_SRC),
    (MD, "MD-171",
     "**2026-10-20, the rule gets a sharper edge.** A Meta ads figure finally arrived with a footnote, "
     "and the footnote reads in full \"Meta Internal Data, measured in February 2026\" (see "
     "[[Meta Delivery & Andromeda#MD-184|MD-184]]). It names a data owner and a month, and no "
     "population, window, control or sample. **So the presence of a footnote is not the test. The "
     "presence of a population and a counterfactual is.** Fired again the same day on a page with no "
     "footnote at all: [[Attribution & Incrementality#AT-131|AT-131]], eleven numbers across four "
     "agency lift studies.",
     GENRECS_SRC),
    (MD, "MD-177",
     "**2026-10-20, and the pair is now unreconcilable in public.** Meta attributes +0.35% in "
     "conversions to GEM paired with the Adaptive Ranking Model and GenRecs Tokenization "
     "([[Meta Delivery & Andromeda#MD-184|MD-184]]). This claim carries GEM's 18.9%. Two Meta posts, "
     "seven days apart, with GEM in both, two orders of magnitude apart, and neither states what the "
     "other is measuring. **Neither figure may go in front of a client and the pair may not go in a "
     "forecast.**",
     GENRECS_SRC),
    (MD, "MD-178",
     "**2026-10-20.** The taxonomy sentence banked here is now backed by a description of how the ad "
     "content representation is actually produced, from the ad's text and images. See "
     "[[Meta Delivery & Andromeda#MD-184|MD-184]].",
     GENRECS_SRC),
    (MD, "MD-179",
     "**2026-10-20, the other half of the pair arrived.** This claim is the USER side of cold start. "
     "[[Meta Delivery & Andromeda#MD-185|MD-185]] is the ITEM side: an ad with no engagement inherits "
     "the representation of semantically similar items, stated to apply \"even before anyone sees the "
     "new ad\". Together they mean neither side of a user-ad pair is scored from zero. Still "
     "unquantified on both sides: no share of requests served by any fallback and no accuracy cost.",
     GENRECS_SRC),
    (MD, "MD-022",
     "**2026-10-20, one stage is missing from this cascade.** GR2 (arXiv 2602.07774, Meta authors) "
     "treats **reranking** as a fourth stage distinct from retrieval and ranking, and says it is "
     "\"largely overlooked\". See [[Meta Delivery & Andromeda#MD-186|MD-186]]. Abstract only, "
     "research rather than confirmed production, so this is a flag on the cascade description and not "
     "a correction to it.",
     "arXiv 2602.07774, GR2: Generative Reasoning Re-ranker, abstract read at source 2026-10-20"),
    (CR, "CR-003",
     "**2026-10-20, the mechanism behind this claim is now published.** GenRecs Tokenization describes "
     "how the content feature is built and why it transfers: tokens describe what an item is, so \"the "
     "model can relate an item it has never seen engagement for, to items it knows well\". See "
     "[[Meta Delivery & Andromeda#MD-185|MD-185]] and "
     "[[Meta Delivery & Andromeda#MD-184|MD-184]]. Meta also now names where the benefit concentrates, "
     "and it is tail inventory and large catalogues rather than any account: \"Tail ad inventory is "
     "where semantic tokens contribute most and where advertiser impact is largest.\" Nothing is "
     "quantified.",
     GENRECS_SRC),
    (AU, "AU-084",
     "**2026-10-20.** Meta has now published its own axis list, \"sequence length, training data, and "
     "model architecture\", which includes the sequence axis this claim is about and omits parameter "
     "count. See [[Auction Mechanics & Bidding#AU-100|AU-100]].",
     GENRECS_SRC),
    (AU, "AU-085",
     "**2026-10-20, the axis distinction now has Meta on both sides of it.** This claim drew the "
     "distinction from Meituan's data. Meta's own 2026-10-19 post names three axes it is pushing and "
     "parameter count is not among them. See [[Auction Mechanics & Bidding#AU-100|AU-100]]. Absence "
     "from a product post is weak evidence about a roadmap, so this is corroboration of the reading "
     "rule and not of the flat-parameter finding.",
     GENRECS_SRC),
    (AT, "AT-130",
     "**2026-10-20, the Meta counterpart is a marketing page rather than an API resource.** Meta "
     "published four agency lift studies the day before, with eleven numbers and no footnote, no "
     "sample, no window and no spend: [[Attribution & Incrementality#AT-131|AT-131]]. The contrast is "
     "the finding. Google shipped lift as 15 queryable metrics on a campaign resource; Meta shipped "
     "four case studies. Both carry an unstated eligibility floor and both need one check in a client "
     "account before anyone mentions them.",
     "Meta for Business News, \"agencies-testing-incrementality\", dated 2026-10-19, read in full 2026-10-20"),
]


def append_claims(path, blocks):
    text = path.read_text(encoding="utf-8")
    if not text.endswith("\n"):
        text += "\n"
    for b in blocks:
        cid = re.search(r"### ([A-Z]{2}-\d+)", b).group(1)
        if f"### {cid} " in text:
            raise SystemExit(f"REFUSING: {cid} already exists in {path.name}")
        text += b
    path.write_text(text, encoding="utf-8")
    return len(blocks)


def merge_into(path, cid, note, source):
    text = path.read_text(encoding="utf-8")
    m = re.search(r"(^### " + re.escape(cid) + r" .*?)(^Sources: )(.*?)(\n^Last touched: )(.*?)$",
                  text, re.S | re.M)
    if not m:
        raise SystemExit(f"REFUSING: could not locate {cid} in {path.name}")
    body, src_lbl, src, lt_lbl, lt = m.groups()
    if TODAY in lt:
        print(f"  skip {cid}: already touched {TODAY}")
        return 0
    newsrc = src if source in src else src + "; " + source
    rep = (body.rstrip("\n") + "\n\n" + note + "\n" + src_lbl + newsrc + lt_lbl + TODAY)
    text = text[:m.start()] + rep + text[m.end():]
    path.write_text(text, encoding="utf-8")
    return 1


if __name__ == "__main__":
    n_new = 0
    for path, blocks in NEW.items():
        n_new += append_claims(path, blocks)
        print(f"appended {len(blocks)} to {path.name}")
    n_mrg = 0
    for path, cid, note, source in MERGES:
        n_mrg += merge_into(path, cid, note, source)
        print(f"merged {cid} in {path.name}")
    print(f"\nDONE: {n_new} new claims, {n_mrg} merges")
