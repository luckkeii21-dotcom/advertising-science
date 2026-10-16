# -*- coding: utf-8 -*-
"""2026-10-16 research merge. Four new claims, two merges."""
import re
from pathlib import Path

SCI = Path(r"E:\claude code marketing skill\Obsidian God-level Marketing Vault\God-level Marketing\wiki\science")


def read(p):
    return (SCI / p).read_text(encoding="utf-8")


def write(p, s):
    (SCI / p).write_text(s, encoding="utf-8")
    print("wrote", p, len(s), "chars")


MD_181 = """
### MD-181 · Meta opened a BRAND-RESERVATION lane in October 2026: a bookable burst with guaranteed delivery, a first-ad-in-Feed placement in test, and a trending-Reels adjacency, and every outcome published for all three is a brand metric
Tier: T1 · Status: active
Three inventory products announced on one page, all United States, all measured on recall, awareness or intent. Not one cost-per-result or conversion figure appears anywhere in the post.

**Ads Super Burst, the one that is shipping.** "Ads Super Burst is moving to general availability this month, rolling out in phases." It books a concentrated window of 3 to 24 hours with category exclusivity, and the booking runs through the forecasting tool rather than the auction: "You can plan your Ads Super Burst campaigns in Reach Planner to secure inventory during your desired dates and get an estimate of reach and price, with guaranteed delivery tied to those estimates." Reported from testing: a median 2.9-point lift in ad recall, a median 0.6-point lift in intent, and a median 34 million people reached per flight, which Meta frames as 14% of the US adult online audience in a single day. **Those four test figures were read off the page but not captured sentence-verbatim, and no experiment design, sample or window is published for any of them.** A 0.6-point intent lift is the smallest effect Meta has published to this engine in fourteen months.

**First Impression Ads, in test only.** The first ad in Feed when a person opens the app, currently one brand per day, "we are now testing it in the United States." Rationale given, and it is the whole of the mechanism offered: "The first ad someone sees when they open their Feed comes with a kind of prominence no other placement offers." No pricing, no eligibility, no availability date.

**Reels Trending Ads, expanded.** Ads placed immediately after high-watch, culturally relevant Reels on both Facebook and Instagram. "There are now 15 always-on standard topics an advertiser can choose from", newly including Home & Garden and Spanish-language content, plus seasonal lineups. **Custom audience exclusions are stated as coming later in 2026**, which means the product has been generally available without the ability to exclude an existing-customer list, and any always-on brand spend on it until then has been buying some share of people the advertiser already owns.

**What this does to the auction-versus-reservation fork.** [[Auction Mechanics & Bidding#AU-032|AU-032]] holds the T3 argument that Meta's reservation buying type can only guarantee its price by serving worse prospects in worse placements, so auction is the correct default for conversion work. Ads Super Burst is a 2026 reservation product and it does not settle that argument either way: Meta publishes reach, recall and intent for it and publishes no conversion outcome at all, which is exactly the shape AU-032 predicts. **The absence is the finding.** Do not read guaranteed delivery as guaranteed performance.

**Standing against our own book, and it is a clean no.** Every one of these is a United States brand-reach product sold on recall and awareness. Our book is lead generation for local businesses in New Jersey, Illinois and Michigan buying cost per lead, with no brand-lift instrument on any account. Category exclusivity and 34 million reach in a day are not purchasable or useful at our budgets. **Banked as platform direction, not as anything to buy.** The one piece with a plausible route to our work is the trending-Reels topic list, because Spanish-language content is now an always-on topic and two of our clients sell to Spanish-speaking buyers; that is a lead to check, not a claim.
Sources: Meta for Business News, "Meta Brand Building Summit: New Ways to Help Marketers Build Unforgettable Brands on Meta", published 2026-10-15, read in full 2026-10-16 (two passes)
Last touched: 2026-10-16
"""

AT_127 = """
### AT-127 · Meta is building a WEEK-LEVEL attention objective, and the research it cites says distributed attention beats the same seconds delivered in one block
Tier: T1 · Status: active
A product in alpha and one finding under it. The finding is the part worth keeping, because it cuts against how every frequency conversation on our accounts is actually run.

**The product.** "We are in the early stages of testing a product called Aggregated View Time", described as a way to measure and optimise the total time someone spends with your brand across a week rather than each impression on its own. Meta's own hedge is on the page: "While it's early and this product is in alpha."

**The finding, quoted.** "Five seconds of attention added up over a week drove 32% more offline sales than one continuous five second view." Same total exposure, split across a week, 32% more offline sales.

**Why this earns a claim.** It makes the UNIT of attention the week instead of the impression, and it puts a number on distribution rather than on volume. If it holds, two accounts with identical total view time and identical frequency are not equivalent, and the one that spread its seconds wins. Nothing else in this codex measures exposure that way: [[Auction Mechanics & Bidding#AU-097|AU-097]] reads the cost of attention, not its shape, and the frequency material we hold is about saturation rather than spacing.

**Guards, and they are heavy.** Meta measuring its own product. No sample size, no vertical, no geography, no window, no lift-study design and no control definition published for the 32%. "Offline sales" is not defined and offline conversion measurement is the weakest instrument Meta sells. Vendor-commissioned brand research sits at law 4c standing, which is a prior for a test and never a result to report. **The product is alpha, so there is nothing to opt into and nothing to configure.**

**What we cannot do with it, said plainly.** No client on our book has an offline sales instrument, so this cannot be tested on our accounts as published. The testable residue is cheaper: whether cost per lead differs between a week where one person saw the same total video seconds in one sitting versus spread across days. We have no column that reports it, so this stays unfalsifiable here until an instrument is named.
Sources: Meta for Business News, "Meta Brand Building Summit: New Ways to Help Marketers Build Unforgettable Brands on Meta", published 2026-10-15, read in full 2026-10-16 (two passes)
Last touched: 2026-10-16
"""

AU_099 = """
### AU-099 · In sponsored search, the value of one returned ad DEPENDS on which other ads came back with it, measured by exhaustive auction replay, and training on that dependence lifted advertiser value 3.51% in a live production test
Tier: T2 · Status: active
Picked up on the arXiv cs.IR lane on 2026-10-16. Same handling rules as [[Auction Mechanics & Bidding#AU-079|AU-079]], [[Auction Mechanics & Bidding#AU-084|AU-084]] and [[Auction Mechanics & Bidding#AU-096|AU-096]]: **the platform is not named and this must never be quoted as documentation of Meta or Google.** It earns a place because of what it measured, not what it built.

**The measurement, which is the durable part.** "In a five-action sponsored-search setting, exhaustive auction replay over 1,200 requests reveals substantial coalition dependence." So on 1,200 real requests, with five ads returned per request, every subset was replayed through the auction and the contribution of any single ad was found to depend materially on which other ads sat beside it. **No ad in a returned set has a standalone value.** The authors also prove the arithmetic consequence: for sets of four or more, the per-ad attribution cannot be recovered from the singleton, leave-one-out and full-set cases alone.

**The live result.** "In a randomized seven-day production A/B test on 10% of traffic, the CASI-trained policy yields an observed 3.51% lift in the primary advertiser-value metric over production control." Seven days, 10% of traffic, randomised, on a production sponsored-search system. That is a real online test with a shown number, which is what puts this at T2 rather than beside the simulator work at [[Scaling Models#SC-177|SC-177]].

**Where it lands on our side of the glass.** It is a within-platform credit-assignment result, so nothing here is a lever an advertiser can pull. What it changes is a habit: we read an ad's performance as a property of that ad. On the retrieval side of a sponsored-search system that is measurably false, because the set is the unit the auction values. It gives an independent mechanism to the breakdown-effect problem already recorded at [[Attribution & Incrementality#AT-107|AT-107]] and to the ad-set-level reading rule at [[Attribution & Incrementality#AT-087|AT-087]]: both say read one level up, and this says the level up is where the value actually sits.

**Guards.** Different platform, unnamed, authors reporting on their own system, and the optimised metric is the platform's "primary advertiser-value metric", which is not defined and is not our cost per lead. The 3.51% is a lift on someone else's baseline and must never be quoted as an expectable gain. The paper itself reports a failure case: "under a sensitivity backend, CASI does not outperform Singleton." Abstract read in full at source; the full paper was not opened, and this claim says nothing the abstract does not.
Sources: arXiv 2610.20293v1, CASI: Credit Assignment via Set Intervention for Agentic Retrieval, submitted 2026-10-14, https://arxiv.org/abs/2610.20293, abstract read in full at source 2026-10-16
Last touched: 2026-10-16
"""

SC_177 = """
### SC-177 · The first published attempt at a fully automated media-buying loop closes planning, adjustment and diagnosis into one feedback cycle, and its numbers come from a SIMULATOR with three accounts
Tier: T4 · Status: active
Banked at T4 deliberately, and the tier is the whole point of the entry. The architecture is the first of its kind this engine has read; the evidence behind it is a simulation.

**What it proposes.** Three specialised roles on different clocks, which is the structure worth noting because it is the first formal description of the job we do by hand. A **Planner** sets account-level budget allocation once per period. An **Optimizer** adjusts delivery strategy at every remaining timestep inside the period. An **Inspector** diagnoses at end of period after settlement, aggregating delivery performance, budget utilisation and action records. "Diagnostic results guide account planning and strategy adjustment in the next period", and one role is updated per period in rotation on settled feedback, which is what the authors call co-evolution.

**What it reports.** "AdCoEvo increases advertiser value by 14.02% while reducing cost per acquisition by 7.07%" against a rule-based operational baseline, and 3.96% and 1.24% against a fixed-parameter multi-agent version. **Those figures are the reason this is T4 and not T2.**

**The evidence, stated so nobody quotes the 14% as a result.** "Experiments use the AuctionNet simulator with its official period length and traffic volume. The environment contains 48 ad units that can purchase traffic." Three controlled accounts, twelve controlled ad units, 500,000 simulated opportunities per period, 48 timesteps per period. **No live platform, no real traffic, no real spend, no advertiser count, and no platform named.** The baseline being beaten by 14.02% is a rule-based policy inside the same simulator, which is not a human media buyer. Authors are from JD Opensource; code is published.

**Why bank it at all.** Every other paper on this lane describes the platform's side of the glass. This one describes ours: the loop from diagnosis to budget decision to adjustment that an operator runs weekly. Having it on file, dated and tiered, means that when a vendor sells autonomous media buying the question is already written down. **The question is what the 14.02% is measured against, and in the first published case the answer is a rule in a simulator.**

**Standing against our own book.** Nothing to adopt and nothing to test. It does supply a usable frame: our own cycle is Planner on a weekly budget call, Optimizer on mid-week changes, Inspector in the weekly report, and the Inspector's output does not currently feed the next Planner decision in any written form. That gap is real and it is ours, not the paper's.
Sources: arXiv 2610.19454, AdCoEvo: A Co-Evolving Multi-Agent Advertising Delivery System, submitted 2026-10-14, https://arxiv.org/abs/2610.19454, abstract and HTML body read 2026-10-16
Last touched: 2026-10-16
"""

for path, block, cid in [
    ("Meta Delivery & Andromeda.md", MD_181, "MD-181"),
    ("Attribution & Incrementality.md", AT_127, "AT-127"),
    ("Auction Mechanics & Bidding.md", AU_099, "AU-099"),
    ("Scaling Models.md", SC_177, "SC-177"),
]:
    s = read(path)
    assert "### " + cid not in s, cid + " already present"
    write(path, s.rstrip("\n") + "\n" + block)

# merge 1: MD-162 gets today's differing Reels-trending figure set
md = read("Meta Delivery & Andromeda.md")
anchor = ('Sources: Meta for Business News, "How winning hearts before peak season boosts baskets '
          'when it matters most", 11 June 2026, read in full 2026-09-20 including all eight footnotes\n'
          'Last touched: 2026-09-20')
assert anchor in md, "MD-162 anchor not found"
add = ('**Meta now quotes a DIFFERENT number set for the same product, added 2026-10-16.** The Brand '
       'Building Summit post gives Reels trending ads at "action intent increased more than 5 percentage '
       'points versus control groups" and "an incremental 5 percentage point lift in unaided brand '
       'awareness", against the +20% total unaided awareness and +5.5 point incremental ad recall banked '
       'above. **These are not the same measures**, one is a relative total and the others are incremental '
       'percentage points, so this is not a contradiction and the claim is not contested. What it is: the '
       'second published figure set for one product in four months, with no method stated on the newer one '
       'at all. The reading rule above applies to it harder, not less. The expansion detail belongs to '
       '[[Meta Delivery & Andromeda#MD-181|MD-181]].\n'
       + anchor.replace("Last touched: 2026-09-20", "Last touched: 2026-10-16"))
md = md.replace(anchor, add)
write("Meta Delivery & Andromeda.md", md)

# merge 2: AU-032 gets the 2026 reservation instance
au = read("Auction Mechanics & Bidding.md")
m = re.search(r"(### AU-032 ·.*?)(?=\n### AU-033)", au, re.S)
assert m, "AU-032 block not found"
blk = m.group(1).rstrip("\n")
assert "Last touched:" in blk
newblk = re.sub(
    r"Last touched: [0-9-]+",
    ('**A 2026 reservation product arrived and it does not settle this, added 2026-10-16.** Meta moved Ads '
     'Super Burst to general availability in the United States in October 2026: a bookable 3-to-24-hour '
     'window with category exclusivity and "guaranteed delivery tied to those estimates", booked through '
     'Reach Planner. **Every outcome Meta publishes for it is a brand metric**, a median 2.9-point ad recall '
     'lift and a median 0.6-point intent lift, and there is no cost-per-result or conversion figure anywhere '
     'in the announcement. That is the shape this claim predicts: the guarantee is on delivery, never on '
     'performance. It does not verify the degraded-prospect mechanism above, which stays asserted and '
     'untested. Full product detail at [[Meta Delivery & Andromeda#MD-181|MD-181]].\n'
     'Last touched: 2026-10-16'),
    blk,
    count=1,
)
au = au.replace(blk, newblk)
write("Auction Mechanics & Bidding.md", au)
print("OK")
