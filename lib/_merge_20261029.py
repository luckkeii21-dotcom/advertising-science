# -*- coding: utf-8 -*-
# Research run 2026-10-29: bank new claims into the codex.
import io, os, re, sys

SCI = r"E:\claude code marketing skill\Obsidian God-level Marketing Vault\God-level Marketing\wiki\science"

def read(f):
    return io.open(os.path.join(SCI, f), encoding='utf-8').read()

def write(f, t):
    io.open(os.path.join(SCI, f), 'w', encoding='utf-8', newline='\n').write(t)

MD_NEW = u"""

### MD-188 \u00b7 The 2026 Andromeda scores EVERY eligible ad at over one billion ads per second on a single GPU server, 100x the 2024 system, and Meta's stated advertiser payoff is 2.4% more conversions on Facebook since 2025
Tier: T1 \u00b7 Status: active
Meta published the next generation of its retrieval engine on 2026-10-28, two years after the generation banked at [[Meta Delivery & Andromeda#MD-024|MD-024]]. Read in full at source.

**The throughput numbers, verbatim.** The production pipeline "processes over one billion ads per second on a single GPU server while scoring every eligible ad in the candidate pool", which Meta calls "a new throughput benchmark for ads retrieval-stage models (i.e., a 100x lift compared to the 2024 Meta Andromeda system)". The 2024 baseline is stated here for the first time: that system "evaluates at tens of millions of ads per second per GPU card".

**The phrase that matters more than the throughput is "scoring every eligible ad".** [[Meta Delivery & Andromeda#MD-026|MD-026]] holds the 2024 design, where a hierarchical multi-layer index cut inference steps to reach sub-linear cost, so the engine evaluated an enormous number of ads rather than all of them. The 2026 system states it scores the whole eligible pool. **For an advertiser this removes one excuse that was always available: an ad that did not get shown was not pruned before scoring.** It was scored and it lost.

**The advertiser-facing figures, and they come from three Meta pages published the same day.** The engineering post states "Since 2025, Meta Andromeda has delivered a 2.4% increase in conversions on Facebook." The two business-news posts of 2026-10-28 add the quarterly split: Andromeda improvements in Q3 2026 "increased conversions by 1.4% on Facebook", stated more precisely on the sister page as "1.37% on Facebook and 0.24% on Instagram Reels", and the Q3 work raised "the complexity of Andromeda by 10X without increasing computing costs". The 1.4% and the 1.37% are the same number rounded, which is a clean internal cross-check across two Meta pages published the same day.

**Why Meta says it had to do this, and it is the second first-party statement of the same cause.** "Since then, generative AI creative tools have helped advertisers rapidly create hundreds of millions of new ads, growing Meta's ads candidate pool to an unprecedented scale." That is [[Meta Delivery & Andromeda#MD-089|MD-089]] restated with a magnitude attached.

**What this is worth on our book, stated honestly. Nothing to do.** Meta's own framing is "better performance automatically from the retrieval system matching ads across a larger candidate pool, within the same latency budget". There is no setting, no opt-in and no account-level readout. A 2.4% conversion lift measured across Facebook is a platform aggregate and is not detectable on a single client account at our spend levels, so it is never quotable to a client as something that happened to them.

**Guards.** Every number is Meta's own, unaudited, with no confidence interval, no spend level, no advertiser count and no vertical breakdown. The post's own stated motive includes "increased business from advertisers and lower costs, as each GPU now evaluates more ads per second", so the publication is not disinterested. The business-news page carrying the quarterly figures footnotes them to Meta's Q2 and Q3 2026 earnings, which makes them investor-reported platform aggregates rather than advertiser-measured results.
Sources: Engineering at Meta, "Meta Andromeda: Powering the Next Generation of Ads Retrieval Through Model-System Co-Design", 2026-10-28, read in full 2026-10-29; Meta for Business News, "three-new-ai-innovations-in-ads-ranking", 2026-10-28, read 2026-10-29; Meta for Business News, "how-metas-ads-system-matches-your-ad-to-the-right-person", 2026-10-28, read 2026-10-29
Last touched: 2026-10-29

### MD-189 \u00b7 Retrieval now carries NEAR RANKING-LEVEL model quality at roughly 300x fewer FLOPs, so the quality gap that justified a two-stage funnel is closing
Tier: T1 \u00b7 Status: active
The sharpest architectural finding of 2026-10-29, and it is a change in kind rather than in degree.

**The problem Meta states, verbatim.** "Historically, the deep modeling quality of the ranking stage has been too costly to apply at retrieval's scale." That cost asymmetry is the entire reason the funnel at [[Meta Delivery & Andromeda#MD-022|MD-022]] and [[Meta Delivery & Andromeda#MD-023|MD-023]] has stages at all: a cheap, shallow model reads everything, then an expensive, deep model reads the survivors.

**What shipped.** A Mixture-of-Experts retrieval architecture in three parts. On the user side, "we transitioned from a single user tower to an ensemble of specialized user towers as experts", fed by "sequential ad engagement events, user-cohort representations, LLM-derived semantic features, and cross-surface co-engagement signals". In the candidate ads tower, "a joint encoding strategy that incorporates real-time serving context". In the interaction layer, the model "evolved from dense neural networks into an MoE attention-based gating network that dynamically routes candidates across the most relevant user experts". Only the top-K most relevant experts activate per ad.

**The result claim.** "Model performance approaches ranking-level in a typical retrieval-then-ranking system, at approximately 300x fewer inference-time FLOPs than the 2024 Meta Andromeda retrieval model." Throughput for that model alone is "over 10 billion ads per second on a single GH200 GPU".

**Two operating consequences, and the first one reverses an instinct.** One: the first gate an ad passes is no longer a crude one. The practitioner model of retrieval as a blunt eligibility filter, banked T3 at [[Meta Delivery & Andromeda#MD-130|MD-130]], described a stage that filters cheaply and leaves the judgement to ranking. Meta now says the filter judges almost as well as the ranker, so **if the shallow model and the deep model agree, there is no longer a stage to be lucky at.** Two: cross-surface co-engagement and user-cohort signals are named as inputs at the RETRIEVAL stage, which is earlier than this codex has previously placed them.

**The honest limit on what we can do with it.** None of it is controllable, measurable or visible from an ad account. It supports [[Meta Delivery & Andromeda#MD-120|MD-120]]'s creative-is-the-targeting direction by showing richer ad-content and context representation entering the earliest stage, and it supplies no number any client should ever hear.

**Guards.** FLOPs are a compute measure, not a quality measure, so "300x fewer FLOPs" and "approaches ranking-level" are two separate claims and only the first is quantified. "Approaches" carries no figure at all: no recall delta, no AUC, no gap size against the ranking stage. Meta publishes no accuracy metric versus ranking anywhere in the post.
Sources: Engineering at Meta, "Meta Andromeda: Powering the Next Generation of Ads Retrieval Through Model-System Co-Design", 2026-10-28, read in full 2026-10-29
Last touched: 2026-10-29

### MD-190 \u00b7 Advertiser targeting rules are enforced by a GPU stage called index matching, running at over 100 billion ads per second and absorbing ad creations, edits and expiries throughout the day
Tier: T1 \u00b7 Status: active
The first time this codex has held a named, measured engineering stage for the thing an advertiser actually sets in Ads Manager.

**What index matching is, in Meta's words.** It is the step "enforcing advertisers' targeting rules". Mechanically: "Ads index matching evaluates complex advertiser-defined targeting logic across tens of feature categories, and must support real-time index updates as ads are created, modified, or expired throughout the day."

**Where it now runs, and why that moved.** It used to run on separate local CPU hosts and talk to the scoring GPUs over the network, which at billions of ads per second "saturates the network link, making the network bandwidth become the bottleneck rather than GPU compute". Meta's fix was to "co-locate index matching, scoring, and top-K selection on the same GPU", sending only "a compact request payload, user features and a targeting query" and returning only the final top-K. Stated effect: "reduces network traffic by ~100x".

**The number.** After GPU kernel optimisation with NVIDIA, "index matching throughput improved over 2x, reaching over 100 billion ads per second, an order of magnitude higher than the scoring network. This headroom means index matching can be re-run across multiple retrieval pathways without becoming a bottleneck."

**Three things this settles or sharpens for us.** First, targeting is confirmed as a filter applied before and alongside scoring rather than as a bid-time input, which is the documented version of what [[Meta Delivery & Andromeda#MD-130|MD-130]] relays at T3. Second, "real-time index updates as ads are created, modified, or expired throughout the day" is first-party confirmation that an edit enters the eligible pool within the day rather than on a batch cycle. **It confirms the index update is fast and says nothing whatsoever about learning, delivery history or performance resetting, so it must never be cited as evidence on that question.** Third, "re-run across multiple retrieval pathways" means one request can retrieve down several routes, which is consistent with the generative-retrieval pathway at [[Meta Delivery & Andromeda#MD-191|MD-191]] running beside the conventional one rather than replacing it.

**Guards.** "Tens of feature categories" is the only sizing Meta gives for targeting logic and it is not a list. Nothing here says which advertiser-set fields are cheap or expensive to evaluate, and nothing licenses any claim that a narrower or a broader audience is easier on the system. The 100 billion figure is a benchmarked kernel throughput from the NVIDIA collaboration, not a production figure.
Sources: Engineering at Meta, "Meta Andromeda: Powering the Next Generation of Ads Retrieval Through Model-System Co-Design", 2026-10-28, read in full 2026-10-29
Last touched: 2026-10-29

### MD-191 \u00b7 Generative retrieval shipped on Facebook Feed in Q3 2026: the system GENERATES the semantic ID of the ideal ad for a person, then matches that to the ads it actually has
Tier: T1 \u00b7 Status: active
This is the strongest statement the creative-is-the-targeting law has ever had, and it also puts [[Meta Delivery & Andromeda#MD-186|MD-186]] partly in contest.

**The mechanism, verbatim.** Under GenRecs Tokenization, models "read each ad's text and images and describe the ad in semantic tokens that capture its key attributes". Then: GenRecs "generates the semantic ID for the ideal ad for a person, then matches that to the ads available in our system."

**Read that in order, because the order is the finding.** The system does not start from the ad inventory and score it. It starts from the person, writes a description of the ad that person should see, and then goes looking for the closest real ad. **An ad's job is to be the nearest available answer to a description the system wrote without reference to it.** [[Meta Delivery & Andromeda#MD-120|MD-120]] holds that ad creative representation is a named GEM input feature, which was the previous high-water mark for this law. This is further: the creative representation is the matching key.

**The shipped figures.** "In Q3, we launched generative retrieval on Facebook Feed, driving a nearly 2% increase in conversions across targeted segments." Separately, paired with GEM and the Adaptive Ranking Model, "+0.35% lift in conversions across surfaces".

**What it does to MD-186, and the split is clean.** MD-186 (T1, banked 2026-10-20) ruled that "generative recommenders" does NOT mean Meta retrieves or writes ads generatively, resting on Meta's own cited paper, "The Case Against Generation for Retrieval". **The limb that survives intact: Meta still does not generate the ad.** It generates an identifier and then matches a real ad to it, so no ad is written by a model. **The limb now in contest: Meta has shipped a thing it calls generative retrieval, in which something genuinely is generated inside the retrieval path.** MD-186's reading rule, that the generative word describes the representation rather than the output, was the right call and it needs the narrower wording from today: what is generated is a TARGET representation, and retrieval is then still a matching operation against it.

**Operating consequence, and it is the only one available.** A new ad, a refreshed creative or a new product can be understood through its semantic neighbours before it has any performance data of its own. Meta states this directly: new and refreshed creative "get on a faster track to performing, because the system can understand them through what it already knows about similar ads and products, whether the signals are plentiful or more limited". **This is a mechanism for why a new ad in an established account is not cold, it is Meta asserting it, and no number is attached to the speed claim.**

**Guards.** "Across targeted segments" is undefined and is not an account-wide figure. "Nearly 2%" and "+0.35%" are platform aggregates on Meta's own measurement. Facebook Feed only, with no statement about Instagram, Reels or any other surface. Nothing here is visible or controllable from an ad account.
Sources: Meta for Business News, "three-new-ai-innovations-in-ads-ranking", 2026-10-28, read 2026-10-29; Meta for Business News, "how-metas-ads-system-matches-your-ad-to-the-right-person", 2026-10-28, read 2026-10-29
Last touched: 2026-10-29

### MD-192 \u00b7 Meta's own quarterly platform lift, footnoted to earnings: 8.3% more ad clicks and 15.7% more conversions on Facebook in Q2 2026 alone
Tier: T1 \u00b7 Status: active
The first time this codex has held a combined, dated, cited quarterly figure for what the platform's AI work did to advertiser outcomes.

**The sentence, verbatim.** "In Q2 2026 alone, advances in our user-understanding models, combined with our Generative Ads Recommendation Model (GEM) and sequence learning, delivered an 8.3% increase in ad clicks and a 15.7% uplift in conversions on Facebook."

**Why it is banked separately from the component claims.** [[Meta Delivery & Andromeda#MD-177|MD-177]] holds GEM's published numbers and records that the post carrying them had no footnote of any kind. [[Meta Delivery & Andromeda#MD-028|MD-028]] holds the sequence architecture's cumulative figures. **This figure is the three systems together, scoped to one quarter and one surface, on a page that does carry footnotes, pointing at Meta's Q2 and Q3 2026 earnings and at Engineering at Meta.** The footnoting is the upgrade, and it is answered for this number only, not retrospectively for MD-177's own.

**The reading that stops this being misused, and it is the whole point of the entry.** A 15.7% platform-wide conversion uplift is what Meta's models did across Facebook. **It is not a lift any advertiser can look for in their own account, and an account that got worse over Q2 2026 is not contradicting it.** Platform aggregates and account results are different measurements, and the gap between them is exactly what makes these numbers dangerous in a client conversation. Never put this figure in a client report. Its only legitimate internal use is to answer "is the platform still changing fast", and the answer is yes.

**The scale context from the same page.** "This happens hundreds of billions of times a day, across Facebook, Instagram, Threads, Messenger, WhatsApp, and Audience Network, drawing on what the 3.64 billion people using at least one of our apps each day show us they care about." Compare the fleet figure at [[Meta Delivery & Andromeda#MD-129|MD-129]], over 5 million requests per second and over 400 billion a day.

**Guards.** Meta's own measurement, with no methodology, no control, no confidence interval, no advertiser count and no vertical split. "Advances in our user-understanding models" is not defined, so the attribution across the three named systems cannot be apportioned. Facebook only. An earnings footnote establishes that Meta told investors the number, not that the number was independently verified.
Sources: Meta for Business News, "how-metas-ads-system-matches-your-ad-to-the-right-person", 2026-10-28, read 2026-10-29, footnoted by Meta to Q2 2026 Earnings, Q3 2026 Earnings and Engineering at Meta
Last touched: 2026-10-29
"""

AU_NEW = u"""

### AU-102 \u00b7 The ad quality term in the auction carries a measured survey instrument of more than 200 million customer responses a year, covering shipping delays, unexpected charges and whether people felt misled
Tier: T1 \u00b7 Status: active
[[Auction Mechanics & Bidding#AU-001|AU-001]] has held since August that ad quality is one of the three auction factors and that it is "drawn from many sources including viewer feedback (hiding the ad) and detection of low-quality attributes". Meta has now put an instrument and a volume behind it, and extended it past the ad into what happens after the sale.

**The sentence, verbatim.** "It reflects feedback from people who view, click or hide ads, detection of low-quality traits such as engagement bait or withheld information, and more than 200 million customer survey responses a year covering satisfaction with purchases, shipping delays, unexpected charges, and whether people felt misled."

**What is new here, and it is not the number.** The ad-side inputs restate AU-001. The new limb is **post-purchase**: shipping delays, unexpected charges and feeling misled are events that happen days or weeks after the click, and Meta states they feed the quality term that prices the auction. Meta draws the consequence itself: "The highest bid or the biggest budget doesn't automatically win, quality of ad experience, purchase experience, and product satisfaction matter too... A more relevant ad, backed by a better customer experience, can beat a higher bid." That is [[Auction Mechanics & Bidding#AU-002|AU-002]]'s relevance claim with fulfilment added to the definition of relevance.

**The operating consequence, and it is real for our book even though we cannot measure it.** For an e-commerce or a service client, delivery problems, surprise fees and an over-promising offer are now a media-cost problem and not only a retention problem. **The honest form of the advice: a client with a fulfilment or an expectation-setting problem may be paying more per impression for it, Meta says so, and nobody can show them the line item.** Never quantify this for a client. There is no quality-score readout, no survey-response count per advertiser and no way to attribute a CPM change to it.

**Guards.** 200 million a year is a global response count across all of Meta's advertising, not a per-advertiser sample, and Meta gives no per-advertiser threshold, no weighting, no decay and no indication of how a small advertiser accumulates enough responses to be measured at all. The post does not say the survey limb applies to lead-generation advertisers, where there is no purchase and no shipping. Meta's own page is the only source and it is a best-practice post, not documentation of the auction formula.
Sources: Meta for Business News, "how-metas-ads-system-matches-your-ad-to-the-right-person", 2026-10-28, read 2026-10-29
Last touched: 2026-10-29
"""

GA_NEW = u"""

### GA-099 \u00b7 Ads in AI Mode scaled to ten more countries on 2026-10-28, with Brazil, Mexico and the UK named for Q4, and multiturn ads launched in the US
Tier: T1 \u00b7 Status: active
A dated platform expansion, read at source. It matters to us mainly because of what it does to the measurement gap at [[Google Auction & Smart Bidding#GA-043|GA-043]].

**The rollout, verbatim.** "Now we're scaling ads in AI Mode in Australia, Canada, India, Kenya, Malaysia, New Zealand, Nigeria, Pakistan, the Philippines, and Singapore. In Q4 2026, we plan to expand to additional locales, including Brazil, Mexico, and the United Kingdom." Separately: "To allow ads in follow-up queries in AI Mode, we are launching multiturn ads in the U.S." Ads "will be clearly labeled as 'Sponsored'" and Google says it will "continue testing new formats".

**Multiturn ads are the genuinely new product here.** Until now an AI Mode ad was attached to the opening query. Google now serves ads inside follow-up turns of the same conversation, in the US. **Google publishes no number for it, no format description, no campaign-type eligibility and no reporting.**

**The two numbers Google does publish, with their footnotes, because the footnotes are the story.** "In AI Mode, queries are, on average, three times longer than traditional searches", footnoted to **"Google AI Mode Report, US, May 2026"**. And "click-through rates are already similar between sponsored and organic product list items within AI Mode", footnoted to **"Google Internal Data, US, August 20, 2026 - September 3, 2026"**. So the query-length figure is five months old and US-only, and the click-through parity claim rests on a **15-day US internal window** with no volume, no vertical and no absolute rate. Neither number is from any of the ten countries being switched on.

**What it does to GA-043, and the answer is that it widens it.** GA-043 records that broad match, Shopping feeds, PMax and AI Max can all serve inside AI Overviews and AI Mode with no setting to disable it and no report that segments those clicks or that spend, and that gap has now been checked and found open three times. **This post says nothing about opt-out, nothing about which campaign types serve into AI Mode, and nothing about reporting.** More surface, more countries, more turns per conversation, and the same blind spot. For any client on those four surfaces, the unmeasured share of spend just got a larger place to land.

**For our own book.** Our ad accounts are US, so the ten countries do not change what our clients buy. Multiturn ads in the US do. Nothing to action, because there is no control.

**Guards.** No launch date per country, no campaign-type list, no opt-in or opt-out mechanism, no reporting commitment and no measurement detail of any kind. "Similar" click-through rates is Google's word, not a figure. Nothing states that ads in AI Mode perform better or worse than ads on a conventional result page.
Sources: Google Ads & Commerce blog, "Ads in AI Mode expand to new markets", Shashi Thakur, VP and GM Google Search Ads, 2026-10-28, read in full 2026-10-29 including both footnotes
Last touched: 2026-10-29
"""

SC_NEW = u"""

### SC-182 \u00b7 Meta has a native scheduled-budget-increase control that ramps a daily budget for a set window and reverts on its own, and Meta's own peak-season guidance now tells advertisers to use it
Tier: T3 for the surface, T1 for Meta's recommendation \u00b7 Status: active
This closes a gap this file named itself. [[Scaling Models#SC-021|SC-021]]'s neighbour claim records Sam Piliero's premise that a $100 daily budget spends the same $100 every day of the week, and the entry's own caveat says it "does not address lifetime budgets or scheduled budgets, which are the platform features that would make the manual correction unnecessary". The feature has a name.

**The control, as described.** Jon Loomer: "you can plan increased spending of existing ad sets by using the schedule budget increases option. So, if you're spending $100 per day, you can say to increase that to $200 per day for week one and $300 per day for week two. When that scheduled increase ends, your budget returns to normal." Two stacked windows and an automatic revert, set in advance.

**Meta's own side of it, from a page published the same week.** In the list of things Meta tells advertisers to do for a seasonal peak: use budget scheduling. **So the operator prescription and the platform prescription agree, which is rare enough on budgeting to be worth recording.**

**Why the automatic revert is the useful half.** Every scaling claim in this file that depends on a human remembering to take a budget back down, and every post-promotion overspend, is a process failure rather than a delivery failure. A control that schedules the ramp AND the return removes the failure mode without touching delivery. Compare the manual-step cadences at [[Scaling Models#SC-100|SC-100]] and [[Scaling Models#SC-044|SC-044]], all of which assume an operator is watching.

**Evidence state, and it is thin on the thing that matters.** Loomer describes the control and does not show it on screen, shows no account, and publishes no result from using it. **Zero evidence that a scheduled increase performs differently from the same increase made by hand, and zero evidence on what it does to the learning phase.** Loomer's own position in the same recording is that the budgeting decision is not what decides a promotion: "whether or not you have a good Black Friday, Cyber Monday is unlikely to be because of your budgeting decisions", and he explicitly tells operators not to obsess over the increase percentage and learning-phase resets. That is an assertion from a high-credibility operator with no data attached, and it runs against the careful-step orthodoxy at SC-044 and [[Scaling Models#SC-001|SC-001]] without refuting it.

**Before using it on a client account:** confirm the control exists in that account, because this codex has already recorded one Meta control ([[Meta Delivery & Andromeda#MD-141|MD-141]], push delivery) present in only about half of an agency's accounts.
Sources: Jon Loomer, "How to Plan Your Ads for BFCM", 2026-10-28, transcript read in full 2026-10-29; Meta for Business News, "how-metas-ads-system-matches-your-ad-to-the-right-person", 2026-10-28, read 2026-10-29
Last touched: 2026-10-29
"""

def append(f, block, marker):
    t = read(f)
    if marker in t:
        print("SKIP, already present: " + marker)
        return
    write(f, t.rstrip() + block)
    print("appended " + marker + " to " + f)

append("Meta Delivery & Andromeda.md", MD_NEW, "### MD-188")
append("Auction Mechanics & Bidding.md", AU_NEW, "### AU-102")
append("Google Auction & Smart Bidding.md", GA_NEW, "### GA-099")
append("Scaling Models.md", SC_NEW, "### SC-182")
