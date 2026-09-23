"""Merge pass for the 2026-09-23 research run.

Everything here comes from pages read IN FULL today in the Playwright browser
(Meta for Business News, both locales) or by plain fetch (Meta Newsroom).
No claim is banked from a headline, a card, or an abstract.
"""
import io
import re
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

SCI = Path(r"E:\claude code marketing skill\Obsidian God-level Marketing Vault"
           r"\God-level Marketing\wiki\science")

# The provenance warning every Agency Awards case has to carry. Written once,
# referenced by each claim that leans on that post.
AWARDS_CAVEAT = (
    "**Provenance, and it applies to every number in this claim.** The source is Meta's own "
    "2026 Agency Awards post. The entrants are agencies competing for an award, the results are "
    "agency-submitted, the judging panel is drawn from Meta and its award partners, and the "
    "winners were selected partly ON these numbers. That is survivorship selection at its maximum: "
    "the population is the winners of a contest, so nothing here says what the same tactic does on "
    "an average account. None of these campaigns ran a holdout except where the text names one. "
    "Meta publishing the post makes it T1 for *what Meta says happened*; it does not make the "
    "mechanism a law. Tiered T3 for that reason."
)


def append(topic, block):
    p = SCI / f"{topic}.md"
    t = p.read_text(encoding="utf-8")
    if not t.endswith("\n"):
        t += "\n"
    p.write_text(t + "\n" + block.strip() + "\n", encoding="utf-8")
    print(f"  + appended to {topic}")


def amend(topic, claim_id, addition, touched="2026-09-23", add_source=None):
    """Insert `addition` immediately before the claim's Sources: line."""
    p = SCI / f"{topic}.md"
    t = p.read_text(encoding="utf-8")
    start = t.index(f"### {claim_id} ")
    nxt = t.find("\n### ", start + 5)
    end = len(t) if nxt == -1 else nxt
    body = t[start:end]

    m = list(re.finditer(r"^Sources: .*$", body, re.M))
    if not m:
        raise SystemExit(f"{claim_id}: no Sources line")
    s = m[-1]
    new_body = body[:s.start()] + addition.strip() + "\n" + body[s.start():]
    if add_source:
        new_body = re.sub(r"^(Sources: .*)$", lambda mm: mm.group(1) + "; " + add_source,
                          new_body, count=1, flags=re.M)
    new_body = re.sub(r"^Last touched: .*$", f"Last touched: {touched}",
                      new_body, count=1, flags=re.M)
    p.write_text(t[:start] + new_body + t[end:], encoding="utf-8")
    print(f"  ~ amended {claim_id} in {topic}")


# ---------------------------------------------------------------- AUCTION ---

append("Auction Mechanics & Bidding", f"""
### AU-094 · Meta's own median advertiser rates show CPA FALLING through Cyber 5 even as CPMs rise, because conversion rate rises faster than price
Tier: T1 · Status: active
The first figures Meta has published for what the peak window does to an advertiser's costs, and they point the opposite way to the instinct that a crowded auction is an expensive one.

**What Meta measured.** Daily median advertiser rates, across all purchase-optimised ads and all verticals, 1 October to 30 November 2025. Against early October:

| Day | Conversion rate | Cost per acquisition |
|---|---|---|
| Black Friday | **+74%** | **-14%** |
| Cyber Monday | **+43%** | **-15%** |

Meta states the CPM half in words rather than numbers: CPMs rose through November as auction pressure intensified, and conversion rates rose faster, so the cost per acquisition came down anyway. Meta's own phrasing for the conclusion: "auction dynamics reward preparation and conversion excellence, not just budget size."

**Why this matters to the codex specifically.** [[Auction Mechanics & Bidding#AU-034|AU-034]] has carried the line that Meta shows no figures for the seasonal windows, only direction, so nothing there was checkable. For Cyber 5 that limit is now closed. It also lands on the same side as the peak-window finding of 2026-09-22 and as the single-advertiser case at [[Scaling Models#SC-168|SC-168]], where one brand nearly doubled spend across the same nine days and cost per purchase still fell 9.8%. Population-level median and one named account now agree on direction.

**The limit, and it is not small.** This is observational, not a test. The advertisers buying on Black Friday are not the same population, at the same budgets, with the same offers and creative, as the advertisers buying in early October. A median CPA that falls is partly a real efficiency effect and partly a mix shift toward brands that prepared, discounted, and ramped. Meta publishes no decomposition and has a direct commercial interest in the reader concluding that peak spend is cheap. Read the direction as trustworthy and the magnitude as an upper bound.

**One thing in the footnote does not parse and is recorded rather than resolved.** Meta's method note says the window is 1 October to 30 November 2025 with "rates normalised to 1 October 2024 = 1", a base a full year before the window. Either the year is a typo for 2025 or the index is rebased to a prior-year anchor. Nothing about the direction changes either way, and the number should not be quoted to a client without that sentence attached.
Sources: Meta for Business News, "Cyber 5 2025: What worked, what changed and how to win Q5", 15 December 2025, read in full 2026-09-23 on the en_GB locale
Last touched: 2026-09-23
""")

amend("Auction Mechanics & Bidding", "AU-034", """
**The "Meta shows no figures" limit above is now PARTLY closed (2026-09-23).** A second Meta post, the Cyber 5 2025 review, publishes measured median advertiser rates for the peak window itself: conversion rate +74% and CPA -14% on Black Friday, +43% and -15% on Cyber Monday, both against early October, from all purchase-optimised ads across all verticals between 1 October and 30 November 2025. Banked in full at [[Auction Mechanics & Bidding#AU-094|AU-094]]. **Read the scope carefully before treating this as support for Q5.** The figures cover CYBER 5, the five days from Thanksgiving to Cyber Monday. The same post restates the Q5 claim, that CPMs fall to their lowest levels of the season while purchase intent holds, in words with no number attached, exactly as the 2025 mobile-games post did. So Meta has now measured the window BEFORE Q5 and still not measured Q5. The tier stays T3 and the lead-gen scope warning below is untouched.
""", add_source='Meta for Business News, "Cyber 5 2025: What worked, what changed and how to win Q5", 15 December 2025, read in full 2026-09-23')

# --------------------------------------------------------------- CREATIVE ---

append("Creative Science", f"""
### CR-261 · Meta measures format diversity INSIDE a single ad set: carrying at least an image, a video and a vertical video with audio delivered 7.3% lower CPA
Tier: T1 · Status: active
The codex is full of claims that creative diversity matters ([[Creative Science#CR-058|CR-058]], the two-axis format-and-style test, [[Scaling Models#SC-015|SC-015]]). Almost all of them are practitioner assertions with no number. This is Meta's own measurement, and it is scoped tighter than any of them: the unit is the AD SET, and the requirement is three specific asset types present together.

**The number.** Ad sets featuring at least an image, a video, and a vertical video with audio delivered **7.3% lower cost per acquisition**. Same dataset as [[Auction Mechanics & Bidding#AU-094|AU-094]]: daily median advertiser rates, all purchase-optimised ads, all verticals, 1 October to 30 November 2025.

**What is actually actionable here, and it is cheap.** The named third asset is not "more video". It is **vertical video with audio**, as a distinct thing from video. An account running a 4:5 feed video and a static is missing the asset Meta names, and adding it is a re-cut rather than a new shoot. Every client we run already has footage that can produce one.

**Two honest limits.** The comparison group is unstated: 7.3% lower than what, an ad set with two of the three, or with one? Meta does not say, so the size is unquotable even though the direction is usable. And it is observational, so an ad set carrying all three formats is also, on average, an ad set belonging to a better-resourced advertiser. The confound runs the same way as in AU-094 and is not decomposed.
Sources: Meta for Business News, "Cyber 5 2025: What worked, what changed and how to win Q5", 15 December 2025, read in full 2026-09-23
Last touched: 2026-09-23
""")

amend("Creative Science", "CR-058", """
**Meta's OWN figures for partnership ads, and the footnote is the story (added 2026-09-23).** In its Cyber 5 2025 review Meta states that partnership ads with creators generated **19% lower acquisition costs and 71% higher brand intent**. Two things in the method note change how that should be used.

**First, the comparison is BAU versus BAU plus AT LEAST 20% OF CELL SPEND on partnership ads.** That threshold is the most useful number in the whole footnote and it is not in the headline. Ben Heath's advice above is roughly 10% of budget, and Blue Sense reports up to 40% on some accounts. Meta's own evidence was generated at 20% or more, so **the 10% allocation sits below the level at which Meta measured the effect.** If we brief a partnership-ads test, 20% is the floor that has evidence under it.

**Second, the data is old and the two halves cover different periods.** The footnote combines a meta-analysis of 15 advertiser tests across e-commerce, retail, CPG, scaled-tech and travel in NA and APAC from **June 2021 to January 2022**, with **14 global brand lift studies run 1 June 2023 to 30 June 2024** at 98% confidence. Neither window is recent, neither is post-Andromeda, and the acquisition-cost half and the brand-intent half are not necessarily from the same studies. A 2026 deck quoting "19% lower CPA from partnership ads" is quoting data up to five years old without saying so.

**Net effect on this claim.** It stays T3. Meta agreeing with four practitioners is corroboration from an interested party, not measurement, and the interested party's own evidence predates the ranking system everyone is now buying on.
""", add_source='Meta for Business News, "Cyber 5 2025: What worked, what changed and how to win Q5", 15 December 2025, read in full 2026-09-23')

append("Creative Science", f"""
### CR-262 · Let a creator post run ORGANICALLY on the creator's own handle first, amplify only the posts that earned an audience unaided, and run the winner as a Partnership Ad from that same handle
Tier: T3 · Status: active
A selection mechanism rather than a creative style, and it is the cheapest creative test in the codex because the test itself costs nothing.

**The method, as run by Ovative Group for American Eagle.** Creators were chosen for being Gen Z themselves and for having **smaller followings rather than celebrity ones**. They were briefed around real moments, spring break and first-week-of-class outfits, so the output read as campus life. Every post went up **on the creator's own account first and had to earn an audience on its own.** Only the posts that worked got money behind them, run as Partnership Ads from the creator's handle rather than the brand's. Ovative secured usage rights to every piece of content up front, which is what made the second step legal and fast.

**Reported results.** 18% of people who saw the paid creator posts interacted with them, stated as more than three times the usual rate. 16% kept watching past the opening seconds, again stated as more than three times the norm. A **22-point lift in brand favourability**, stated as nearly four times the typical retailer result.

**Why this is worth carrying into our own book.** Every creative test we run costs spend to resolve, and spend spent on a loser is the largest line in a testing budget. Organic reach on the creator's handle is a free pre-filter that produces a real audience response before a single dollar of paid delivery. It also sidesteps the thing that breaks most creator ads, which is that a brand cannot tell in advance which creator's voice will land. The rights-up-front point is the operational catch: without it the winner cannot be amplified quickly, and the whole advantage is speed.

**Where it does NOT obviously transfer.** Every account we run is local lead generation, and a chiropractor's or a truck dealership's creator pool has no comparable organic reach to filter on. The mechanism needs an audience the creator already owns. Treat it as proven for consumer retail with a real creator bench and untested for local service.

{AWARDS_CAVEAT}
Sources: Meta for Business News, "Meet the 2026 Meta Agency Award Winners", 21 September 2026, read in full 2026-09-23
Last touched: 2026-09-23
""")

append("Creative Science", f"""
### CR-263 · Test ONE messaging element per round rather than one creative per round, because the winning angle is routinely the one nobody predicted
Tier: T3 · Status: active
Code3 launched Feastables into grocery-buying households with no advertising history to draw on, so there was no prior about which selling point would carry. Rather than shipping mixed creative and reading the winner, **each round of ads made a single case for the brand**: clean-label ingredients, ethical sourcing, nutrition, comparison against older brands, and real families eating it. One variable per round, held constant across the creative in that round.

**The result that makes the method worth banking.** Clean-label ingredients won, and Meta's write-up says it beat the angles **everyone had expected**. Budget moved behind it immediately. Reported outcomes: a 23.9-point lift in ad recall, 45.5% more click-throughs at 20.6% lower cost per click, more than a million shoppers engaged and re-reachable, and the brand tripled its budget within three months.

**The quote that names the actual payoff**, from Code3 CEO Craig Atkinson: "We learned as much from the creatives that didn't perform as we did from the winners. Meta's creative testing tools helped us understand why creative resonated, not just which ads performed." A mixed-creative test tells you which ad won. A one-variable-per-round test tells you which ARGUMENT won, and an argument transfers to the next twenty ads while a winning ad does not.

**How this sits against what the codex already says.** It pulls against the volume-and-let-the-system-sort-it default that runs through the post-Andromeda claims, and it does not contradict it. Volume is how you find a winning ad. Single-variable rounds are how you find a winning angle. The second is what a brief needs and the first is what a launch needs. Both can be true in the same account in different months.

{AWARDS_CAVEAT}
Sources: Meta for Business News, "Meet the 2026 Meta Agency Award Winners", 21 September 2026, read in full 2026-09-23
Last touched: 2026-09-23
""")

append("Creative Science", f"""
### CR-264 · Spanish and English creative run SIDE BY SIDE on the same offer reached people at roughly half the cost and started more than four times as many conversations
Tier: T3 · Status: active
The first figure in this codex that puts a number on the Spanish-language advantage, and it comes from a US telecom rather than from us.

**The setup.** Boost Mobile sells budget wireless plans to a mobile-first, price-conscious, substantially Spanish-speaking audience. Ovative Group built the campaign on **Click-to-WhatsApp ads**, which drop the responder straight into a WhatsApp conversation with the business, and ran **Spanish and English side by side, each with its own creative**, specifically so the two could be read against each other.

**Reported results.** 11,428 conversations started at **$16.72 each**. 447,000 people reached whom no other Boost campaign on Meta had touched, **248,000 of them Spanish-speaking**. A 17.6-point lift in ad recall, stated as three times the telecom norm. And the finding that matters: **the Spanish-language ads reached people at roughly half the cost of the English ones and started more than four times as many conversations.**

**Why this is directly ours.** We run Spanish and English creative on two truck dealerships out of New Jersey, and the whole question of whether the Spanish lane deserves its own budget has been argued from our own account data alone. This is an independent, named, large-N case pointing the same way, on a different vertical, in a different state, with an explicitly parallel structure. It also supports the structural choice we already make, which is separate creative per language rather than a translated twin.

**Two limits before anybody quotes the halving.** Cheaper reach against a Spanish-speaking audience is partly an auction-competition effect: fewer advertisers bid in Spanish, so the impressions cost less. That is a property of the auction in 2026 and it decays as more advertisers arrive. And "four times as many conversations" is a Click-to-WhatsApp metric on a product where the buyer genuinely has questions, which is not the same funnel as an instant form for a chiropractic appointment. The direction transfers. The multiple does not.

**One part of this campaign was measured properly and is worth noting**, because almost nothing else in the source was. Ovative ran incrementality tests to establish how much of the audience no other Boost campaign had reached, and used Meta's modelling to separate created purchases from credited ones. That is the reason the 447,000 incremental-reach figure is the most trustworthy number in the case.

{AWARDS_CAVEAT}
Sources: Meta for Business News, "Meet the 2026 Meta Agency Award Winners", 21 September 2026, read in full 2026-09-23
Last touched: 2026-09-23
""")

# ---------------------------------------------------------------- SCALING ---

append("Scaling Models", f"""
### SC-168 · A named account nearly doubled peak-window spend year over year and cost per purchase still FELL, on 10 to 20% increments gated on returns holding
Tier: T3 · Status: active
The single-account companion to [[Auction Mechanics & Bidding#AU-094|AU-094]], and it is the clearest worked example in the codex of scaling into the most expensive auction of the year without paying for it.

**The brand and the window.** Compartés, a Los Angeles chocolate maker, run by elk Marketing. The goal going into Black Friday and Cyber Monday was to **nearly double ad spend against the same nine days a year earlier while holding a 4x return**.

**What they actually did**, in the order it matters:
- Handed **about 87% of the budget** to Meta's Advantage suite and let the ads run anywhere across Facebook and Instagram.
- Fed that system genuine variety, because it only works if there is something to choose between: creator videos, holiday photography, animated graphics, and catalogue-built ads.
- **Launched in rounds**, so they could see which idea was carrying the season and build the next round from it.
- Raised budget **10 to 20% at a time, and only while returns held**.

**Reported results.** Over the nine days around Black Friday and Cyber Monday, spend **+99%** year over year, revenue **+105%**, cost per purchase **-9.8%**. Across the eight-week season, **$2.8M in sales and 21,000+ orders, up 33.1% and 32.1%**. And the composition change that is easy to miss: **42.1% more orders from first-time buyers, shifting the campaign from mostly repeat customers to mostly new ones.**

**The operator's own account of why it held**, from James Dupre, VP of Paid Media at elk: "Firm budget and efficiency guardrails gave us the confidence to scale when the account was ready." The guardrail is the mechanism, not the increment size. A 10 to 20% step with no efficiency gate is just a faster way to lose money.

**Read this next to [[Scaling Models#SC-058|SC-058]] and the 2026-09-22 peak-window finding.** Those establish that the concentration behaviour the codex treats as settled does not behave the same way inside a peak-spend window. This case is consistent with that: the account got MORE efficient while doubling into the busiest auction of the year, on a wide creative base and an automated budget.

{AWARDS_CAVEAT} The nine-day and eight-week figures are also year-over-year against a base the post does not disclose, so a 99% spend rise says nothing about the absolute size of the account.
Sources: Meta for Business News, "Meet the 2026 Meta Agency Award Winners", 21 September 2026, read in full 2026-09-23
Last touched: 2026-09-23
""")

append("Scaling Models", f"""
### SC-169 · Several holiday campaigns split by audience and goal were found COMPETING for the same shoppers; merging them into one Advantage+ Shopping campaign with CRM-fed value signals returned 59% more per dollar at 41% lower cost per sale
Tier: T3 · Status: active
The consolidation claims in this topic ([[Scaling Models#SC-052|SC-052]], [[Scaling Models#SC-053|SC-053]], [[Scaling Models#SC-086|SC-086]]) are mostly arguments about reach, frequency and starvation. This is a named case where the stated fault was **internal auction competition**, and it is the largest brand attached to that diagnosis anywhere in the codex.

**The diagnosis.** Christian Dior Couture's holiday campaign, its largest commercial moment of the year, had over several years been split across many separate campaigns, each with its own audience and its own goal. Code3's finding was that **they had started competing with one another for the same shoppers**, and that the fix was structural rather than budgetary. Code3's own framing: the way to sell more without spending more "didn't actually involve budget or the ads themselves. It was all about account structure."

**What was changed, over eight weeks.** Several campaigns were combined into one using **Advantage+ Shopping**. The ad account was set up to favour shoppers likely to spend more. **Dior's CRM data was connected** so the system could learn from real purchases rather than from inferred value.

**Reported results.** Return per dollar **+59%** year over year, cost per sale **-41%**, and nearly **four times** as many people watching Dior's videos to completion. Dior has adopted the structure for future campaigns, which is a stronger signal than any single number here: the advertiser kept it.

**The honest reading, and it is a caution.** Three changes shipped together, consolidation, value optimisation, and a CRM connection. The post attributes the outcome to structure. Nothing in it separates the three, and connecting first-party purchase data to a value-optimised campaign is on its own a well-evidenced lift. **Do not quote this as proof that consolidation alone produced 59%.** Quote it as a named case where a large advertiser found its own campaigns bidding against each other and fixed it by merging them.

**Scope.** Luxury e-commerce at Dior's scale, eight-week rebuild, agency-run. [[Scaling Models#SC-053|SC-053]] already says full consolidation is wrong for about 90% of advertisers. This case does not touch that: it is consolidation of campaigns chasing ONE audience for ONE seasonal goal, which is the situation SC-053's exceptions were written for.

{AWARDS_CAVEAT}
Sources: Meta for Business News, "Meet the 2026 Meta Agency Award Winners", 21 September 2026, read in full 2026-09-23
Last touched: 2026-09-23
""")

# ------------------------------------------------------------ ATTRIBUTION ---

append("Attribution & Incrementality", """
### AT-125 · Meta says a Conversion Lift study reaches a reliable read in 2 to 3 weeks at holiday conversion volume against 6+ weeks in a quiet quarter, which makes peak the cheapest time to buy proof
Tier: T1 · Status: active
A duration figure, which is the number that actually decides whether a lift study is worth proposing to a client.

**What Meta states.** "The holiday season's massive conversion volume means results are reliable in 2 to 3 weeks rather than the 6+ weeks it might take in a quieter quarter." The mechanism is only conversion volume: a randomised holdout resolves when enough events land on both arms, so the calendar cost of the test falls as the event rate rises.

**This cuts directly against [[Attribution & Incrementality#AT-081|AT-081]], and the conflict is real.** AT-081 says never to run an incrementality test in a high-seasonality month, because seasonal noise swamps the effect and a Black Friday holdout is the textbook mistake. Meta says peak is the best time to run one. **Both are defensible and they are answering different questions.** AT-081 is about a test whose result you want to GENERALISE to the rest of the year, where November contaminates the estimate. Meta is arguing for a test whose result you want to use for NEXT YEAR'S PEAK, where November is the population you actually care about. A holdout measured at peak measures peak. Recorded as a scope split rather than as a contradiction, and neither claim is set to contested.

**The operating rule that falls out.** If the question is "what does Meta do for us in general", run the holdout in a flat month, per AT-081. If the question is "what did Meta do for us at peak, so the CFO funds next peak", run it at peak and accept that the answer is only about peak.

**What Meta says you get out of it**, quoted because the third item is the one clients never ask for and should: incremental conversions, cost per incremental result, and a stated confidence level. Meta also names the design plainly as the same randomised controlled method used in medical trials, one group sees the ads and one holdout group does not, and the difference is the lift.

**The self-interest is obvious and does not make it wrong.** Meta sells the ads whose incremental value the study measures, and the post exists to get advertisers to book a study through their Meta rep before peak. The duration claim is still the most useful thing in it, and it is falsifiable against our own next study.
Sources: Meta for Business News, "Holiday measurement strategies", 13 August 2026, read in full 2026-09-23
Last touched: 2026-09-23
""")

append("Attribution & Incrementality", """
### AT-126 · Meta publishes FICTIONAL case studies on its business news channel, disclosed only in a footnote under the article
Tier: T1 · Status: active
A reading rule about the source, banked because the codex now draws heavily on Meta's own business posts and this changes how the narrative parts of them must be read.

**What was published.** "Holiday measurement strategies" opens with two brands. Brand A had a good season, could not answer the CFO asking how they knew the sales would not have happened anyway, and had its budget frozen. Brand B ran a Conversion Lift study and walked into January with **"14,200 incremental conversions attributed to their Meta ads, at $7.40 per incremental result"**, and **"the budget would grow by 20% for next year."** It reads exactly like every advertiser case study on the same channel, down to the specificity of the two figures.

**At the foot of the page:** "*Disclaimer: This is a fictional example and does not represent a real brand example."

**Why this is worth a claim rather than a shrug.** Nothing on the page marks the numbers as invented at the point where a reader meets them. There is no "hypothetically", no "imagine a brand". The disclosure sits below the sources, after the call to action, in the same run of small print as the Ipsos citation. Anyone skim-reading, screenshotting the opening, or quoting "$7.40 per incremental result" into a deck carries an invented number forward as a Meta benchmark. **We have banked genuine advertiser figures from this exact channel**, including everything in the 2026 Agency Awards post read the same day. The lesson is that the channel mixes real named case studies and invented unnamed ones in the same format, and only the footnote separates them.

**The standing rule for this source.** On any Meta for Business post, before banking a performance figure: check whether the advertiser is NAMED. Named brands with a quoted executive are real cases. An unnamed "Brand A" or "a leading retailer" is a narrative device, and the disclaimer for it is at the bottom of the page. Read the small print before the number.

**The same post's survey figures are real and separately weak.** 88% of shoppers use various formats on social media for holiday inspiration, and 68% of those who discover products on Facebook are likely to purchase, both from a Meta-commissioned Ipsos online survey of 14,473 holiday shoppers across 18 countries, November 2025. Vendor-commissioned survey material at law 4c standing, and the numbers are about stated behaviour, not measured behaviour.
Sources: Meta for Business News, "Holiday measurement strategies", 13 August 2026, read in full 2026-09-23
Last touched: 2026-09-23
""")

# ------------------------------------------------------- LEARNING & SIGNAL ---

append("Learning & Signal", f"""
### LS-082 · Feeding server-verified IN-STORE conversions back through the Conversions API and optimising to store trips instead of web clicks cut the cost of driving a high-value shopper into a store by 44%
Tier: T3 · Status: active
A clean worked example of the thing this topic keeps asserting, which is that the optimisation event decides everything downstream.

**The setup.** The Winn-Dixie Company, fresh off a January 2026 rebrand, wanted store visits rather than site traffic. Net Conversion implemented **Meta's Conversions API as a direct server-to-server connection**, feeding reliable real-time **in-store** conversion data back into Ads Manager, and **moved the campaign's optimisation target from web clicks to server-verified store trips**.

**Reported result.** A **44% reduction in the cost of driving a high-value shopper to a Winn-Dixie store.**

**Why the mechanism is the interesting half.** The change was not a bid, an audience or a creative. It was giving the ranking system a truthful signal about the outcome the business actually sells, and then asking it to optimise for that outcome. Web clicks were a proxy that correlated loosely with store visits; server-verified store trips are the thing itself. Everything the codex records about signal quality predicts exactly this shape of result.

**Where it touches our own accounts.** Every client we run has an outcome that happens off the website: an appointment attended, a truck sold, a call booked and held. We optimise to a form submission because that is the event that is easy to fire. This case is the argument for pushing the real downstream event back through CAPI, and the 44% is the size of prize somebody else measured for doing it.

**The limit.** A national grocery chain has point-of-sale infrastructure that can verify a store trip at scale. A single-location chiropractic clinic does not, and the equivalent for us is CRM-side appointment-attended data, which is only as good as whoever updates the CRM. The mechanism transfers. The data quality does not transfer automatically and is the actual work.

{AWARDS_CAVEAT}
Sources: Meta for Business News, "Meet the 2026 Meta Agency Award Winners", 21 September 2026, read in full 2026-09-23
Last touched: 2026-09-23
""")

# ---------------------------------------------------------- META DELIVERY ---

append("Meta Delivery & Andromeda", f"""
### MD-165 · Advantage+ Audience was run head to head against an advertiser's own traditional audience strategy with an independent measurement firm on the brand half, and beat it on cost and on consideration
Tier: T3 · Status: active
Most Advantage+ Audience evidence in this codex is either Meta marketing with no comparison or a practitioner's before-and-after. This one names the control, the comparison and a third-party measurement firm, which makes it the best-designed case on the automated-audience question currently on file.

**The design.** The National Association of REALTORS and Havas Media Network ran an **Advantage+ Audience** campaign to find people likely to be considering a home purchase, and **tested it against NAR's traditional audience strategy** on website visits and advertising cost. The brand-side outcome, whether the campaign moved consideration of and intent to work with a REALTOR, was measured by **DISQO**, named in the post as an independent research firm.

**Reported results.** More people visited NAR's website while the campaign **spent 25% less**. Cost per website visit **-29%**, cost of reach **-18%**. Consideration of working with a REALTOR **+8 points**, intent to use one **+9 points**, with consumer consideration stated as four times higher than the previous year.

**What is genuinely better about this than the usual Advantage+ case.** There is a named control arm, the metric set includes cost and not only volume, and the brand half went to an outside measurer rather than to Meta's own brand lift product. The agency's own framing is about signal recency rather than automation for its own sake, from Holly Dunn of Havas Media Network North America: the opportunity is "moving beyond predefined audience assumptions and using live signals to make smarter decisions throughout the campaign."

**What is still missing, and it is the usual thing.** The two arms were not necessarily concurrent, budget-matched or randomised; the post says "tested this approach against" and nothing more. "Four times higher than the previous year" is a year-over-year comparison with a different market, and does not belong in the same list as the head-to-head numbers. And a lead-gen advertiser reading this should note the outcome is website visits, not booked business.

{AWARDS_CAVEAT}
Sources: Meta for Business News, "Meet the 2026 Meta Agency Award Winners", 21 September 2026, read in full 2026-09-23
Last touched: 2026-09-23
""")

amend("Meta Delivery & Andromeda", "MD-160", """
**Meta's GLOBAL enforcement figures, published 22 September 2026, and they are an order of magnitude above the Poland numbers above (added 2026-09-23).** In a Newsroom post about its information-sharing partnership with the Singapore Police Force, Meta states: **"So far this year we've removed 65 million scam ads from Facebook and Instagram, with 94% of those ads removed before anyone reported them to us."** Set against the Poland figures already recorded here, 137,000 fraudulent ads over twelve months at over 88% proactive, the global proactive rate is 6 points higher and the volume is roughly 475 times larger.

**Read the population the way this claim already tells you to.** Meta calls these "scam ads", which is narrower than the "removed ads" population MD-160 is about, so the two are not the same denominator and cannot be divided into each other. Nothing in the post says how an ad is classified as a scam ad, and the classification is Meta's own with no external audit.

**The same post carries two enforcement actions that are NOT about ads and matter to any advertiser anyway.** Meta actioned **over 3.6 million "shell pages" in July 2026** on Singapore Police signals. Meta's own description of a shell page is the part to notice: these Pages "look empty and harmless, no ads or violating content", and were actioned as pre-built infrastructure before use. **So a Page with no content and no ad history sits inside a population Meta is now bulk-actioning on external signal.** We spin up new Pages for new clients, and they look exactly like that on day one. Nothing here says a legitimate new Page is at risk, and nothing here says it is not. Worth knowing before the next new-client build. Separately, a US Department of Justice Scam Center Strike Force operation across two weeks in May and June 2026, with Meta, Microsoft, Coinbase and Starlink alongside the FBI and five countries' police, disrupted **1.4 million accounts, Pages and Groups across Facebook and Instagram**.
""", add_source='Meta Newsroom, "Meta Takes Action on 3.7 Million Accounts, Pages and Content In Partnership With Singapore Police Force", 22 September 2026, read in full 2026-09-23')

amend("Meta Delivery & Andromeda", "MD-159", """
**What Meta One is FOR became clearer on 2026-09-23, from an August post read late.** Meta is shipping a set of Meta AI business features across meta.ai, the Meta AI mobile app and a new desktop app, which can be connected to a business's **Instagram and Facebook accounts, its Meta ad campaigns, and Google Workspace (Gmail, Docs, Sheets, Slides)** in one conversation. Stated capabilities: read organic engagement (reach, saves, shares, comments, profile visits) and say what is working; benchmark the business against publicly available data on comparable brands; review ad performance and name which audiences are delivering, what the best-performing content has in common, which creative has stopped resonating and where budget could work harder; produce decks, docs and spreadsheets from the result; and run recurring tasks and reminders on a schedule.

**The line that connects it to Meta One:** "It's free to get started with these features today. As we expand, businesses that want to use them even more will be able to subscribe to Meta One." So the subscription recorded in this claim is the paywall these AI features are heading toward, and the free tier is an acquisition window.

**Nothing in the post is measured.** No performance figure, no accuracy figure, no limit stated on what the ad-account analysis can see or get wrong. The only evidence offered is three quotes from named small-business testers. Banked as existence-and-capability only, on the [[Meta Delivery & Andromeda#MD-099|MD-099]] precedent, exactly as the rest of this claim is.
""", add_source='Meta for Business News, "New Meta AI Features for Small Businesses", 19 August 2026, read in full 2026-09-23')

print("merge complete")
