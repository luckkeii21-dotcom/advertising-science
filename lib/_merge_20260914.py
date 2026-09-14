# -*- coding: utf-8 -*-
"""2026-09-14 research merge. Five sources read in full:
   1. Meta Advertising Standards, transparency.meta.com/policies/ad-standards/ and /en-gb/,
      both read through the Playwright browser (plain fetch returns HTTP 400 on every route).
   2. arXiv 2609.11943, PinDCO (Pinterest), abstract.
   3. arXiv 2609.12375, ChronicleRec, abstract.
   4. Blue Sense Digital, Alo Yoga Teardown, 2026-09-14, 10,571-word transcript.
   5. Sam Piliero, The Most Valuable Ecommerce Ads Training You'll Ever Watch, 2026-09-14.
   6. Fraser Cottrell, The Ultimate Guide to Static Image Ads, 2026-09-13.
"""
from pathlib import Path

SCI = Path(r"E:\claude code marketing skill\Obsidian God-level Marketing Vault\God-level Marketing\wiki\science")


def edit(fname, old, new, count=1):
    p = SCI / fname
    t = p.read_text(encoding="utf-8")
    assert t.count(old) == count, f"{fname}: anchor count {t.count(old)} != {count}\n{old[:160]}"
    p.write_text(t.replace(old, new, count), encoding="utf-8")
    print("edited  ", fname)


def append(fname, block):
    p = SCI / fname
    t = p.read_text(encoding="utf-8").rstrip("\n")
    p.write_text(t + "\n\n" + block.strip("\n") + "\n", encoding="utf-8")
    print("appended", fname)


BSD = "Blue Sense Digital, Alo Yoga Teardown: Creative, Offers, Landers & Acquisition, 2026-09-14"
SAM = "Sam Piliero, The Most Valuable Ecommerce Ads Training You'll Ever Watch, 2026-09-14"
FRA = "Fraser Cottrell, The Ultimate Guide to Static Image Ads (copy & scale), 2026-09-13"

# ============================================================== MD-156, new, T1
append("Meta Delivery & Andromeda.md", """
### MD-156 · Meta collapsed the Advertising Standards fraud section into "Prohibited Commercial Practices", and the rollout is staged by locale, so two people reading the same policy page on the same day see different rules
Tier: T1 · Status: active
**The first change this baseline has ever caught.** The structural baseline for `transparency.meta.com/policies/ad-standards/` was created 2026-08-25 because the lane had been running with nothing to diff against, a gap first recorded 2026-08-24. Read 2026-09-14 through the Playwright browser, because a plain fetch returns HTTP 400 on every route and locale tried.

**What changed.** Baseline section 7 read "Fraud, Scams, and Deceptive Practices" and carried two policies beneath it: "Fraud, Scams and Deceptive Practices" and "Unacceptable Business Practices". On the default locale that section is now titled **"Prohibited Commercial Practices"** and carries ONE policy of the same name, whose entire body is "Ads Must Comply with the Community Standard on Prohibited Commercial Practices." The strings "Fraud, Scams" and "Unacceptable Business Practices" appear nowhere on the default-locale page. The other 15 sections are present in the same order, and both sections our clinics run against are unchanged: "Health and Wellness" under Restricted goods and services, and "Privacy Violations and Personal Attributes" under Objectionable content, the latter word for word against the baseline.

**The locale split is the operationally important half, and it was verified on both pages in the same browser session rather than inferred.** `/policies/ad-standards/` renders 32,611 characters, contains "Prohibited Commercial Practices" and contains no "Fraud, Scams". `/en-gb/policies/ad-standards/` renders 33,672 characters, contains "Fraud, Scams and Deceptive Practices" at offset 11,151 and "Unacceptable Business Practices" at offset 11,365, and contains no "Prohibited Commercial Practices". The 1,061-character difference is consistent with one page carrying two policy entries where the other carries one.

**What it means for us.** Never quote a Meta policy section name without stating which locale it was read on. An appeal that cites a section name the reviewer's locale does not carry is arguing from a page that does not exist for them. And note the direction of the consolidation: two named prohibitions became one pointer at a Community Standard, which moves the binding rule text off the advertising page and onto the Community Standards page, which this lane does not watch.

**A method gap closed on the same read.** The baseline could only detect a section being added, removed or renamed, which is exactly why it caught this and would have missed a silent rewrite inside an unchanged title. A per-section SHA-256 map of the rendered body was captured today, so the next run can detect a body rewrite as well as a heading change.
Sources: Meta Advertising Standards, https://transparency.meta.com/policies/ad-standards/ and https://transparency.meta.com/en-gb/policies/ad-standards/, both read 2026-09-14 through the Playwright browser; structural baseline of 2026-08-25 at .claude/skills/advertising-science/cache/meta-ad-standards-baseline.md
Last touched: 2026-09-14
""")

# ============================================================== CR-234, new, T1
append("Creative Science.md", """
### CR-234 · Pinterest's production creative-selection system gives each creative COMPONENT its own tower and then adjusts the score for how much screen the ad will occupy, for +3.09% CTR
Tier: T1 · Status: active
PinDCO, arXiv 2609.11943v1, announced 2026-09-14. A Pinterest engineering paper describing a system the authors state is launched in the Pinterest Ads platform. Read as the abstract; the full paper was not opened, and this claim says nothing the abstract does not.

**The architecture, and why it is not just another ranker.** A Creative Component Fusion Network models each component of the creative, the paper names image, title and layout, with **its own dedicated tower and its own hyperparameters**, on the stated reasoning that components differ in modelling complexity. The component representations are then fused into a creative-level score that is **conditioned on the ad-level prediction**. Creative score and ad score are separate quantities, and the creative one is computed on top of the other.

**The part with no analogue anywhere else in this codex.** A Pixel-aware Adjustment Module changes a creative's score **according to the size it will render at**, because Pinterest's waterfall grid means one creative's rendered size displaces neighbouring content and moves session-level engagement. Creative selection is being optimised for the whole page, not for the ad's own click.

**Scale plumbing, stated and worth noting because it is the same problem every platform now has.** A lightweight pre-selection model prunes candidates early, with caching and dynamic batching behind it. The paper's reason for needing any of this is that generative AI has multiplied candidate variants per campaign, which is the platform-side statement of the creative-volume argument this codex has so far only heard from operators.

**Result.** +3.09% ad click-through rate online with positive whole-page metrics, from offline analysis plus online A/B.

**Read it as direction of travel, not as Meta.** This is Pinterest, and [[Emerging Channels#EC-001|EC-001]] and [[Emerging Channels#EC-002|EC-002]] both hold that Pinterest is a thin, structurally over-attributing surface we do not buy. Its value is as a rare published description of a production creative-selection system, and it converges with the content-based retrieval architecture at [[Meta Delivery & Andromeda#MD-022|MD-022]] and [[Meta Delivery & Andromeda#MD-025|MD-025]].
Sources: PinDCO: Whole-Page Aware Dynamic Creative Optimization at Scale, arXiv 2609.11943v1, announced 2026-09-14 (abstract read)
Last touched: 2026-09-14
""")

# ============================================================== LS-078, new, T1
append("Learning & Signal.md", """
### LS-078 · Ad ranking is moving to a cached, target-independent summary of the user's whole history, which decouples long-history modelling from the scoring of each candidate ad
Tier: T1 · Status: active
ChronicleRec, arXiv 2609.12375v1, announced 2026-09-14. Evaluated on KuaiRand and **Tencent AdLive**, with a seven-day online A/B test the authors say produced significant production gains. Read as the abstract; the full paper was not opened.

**The problem it names.** Feeding thousands of historical user actions into a ranking model is computationally prohibitive, and truncating the history discards long-range signal. Existing lifelong-interest methods retrieve target-relevant behaviours **per candidate**, which couples long-sequence modelling to candidate scoring and pays the cost again on every request.

**The move.** Compress the entire behaviour sequence ONCE into a chronologically ordered set of tokens, with recent behaviour preserved at fine grain and distant history coarsened. Query tokens are interleaved with the merged sequence under a causal encoder, so each summary covers only the history before its own point in time. Because the tokens are target-independent, they can be **cached per user**, which is the whole point: ultra-long sequence modelling stops being part of the per-request cost.

**Why it belongs here.** It is a direct statement from people shipping it that the expensive object in modern ad ranking is the user's history rather than the ad, and that the industry answer is a durable per-user representation computed ahead of time. That is the same shape as the latent user and interest representations at [[Meta Delivery & Andromeda#MD-025|MD-025]], and it is a mechanism underneath why a pixel's accumulated history behaves like an asset rather than a setting. Compare [[Learning & Signal#LS-039|LS-039]], which holds that the reinforcement signal is wider than the optimization event.

**Filter note, and read it before treating this as an advertising paper.** The word "advertising" appears in this abstract exactly once, in the first sentence, which is the shape of all three arXiv false positives recorded in Watchlist.md. It was banked on a different ground: the EVALUATION runs on Tencent AdLive, an advertising dataset, with a seven-day online A/B test. The method itself is not advertising-specific and the paper is not about auctions, bidding or creative.
Sources: ChronicleRec: Pre-training Temporally Anchored Tokens for Lifelong User Modeling, arXiv 2609.12375v1, announced 2026-09-14 (abstract read)
Last touched: 2026-09-14
""")

# ============================================================== SC-157, new, T3
append("Scaling Models.md", """
### SC-157 · An ad account can be a harvesting layer rather than a demand engine, and when it is, the in-account levers are close to powerless: 96% of Alo Yoga's ads sit in the bottom two awareness stages
Tier: T3 · Status: active
Blue Sense Digital teardown of Alo Yoga, 2026-09-14, built from a scrape of the public ad library plus the landing pages. The agency states 15 to 20 nine-figure fashion brands as its own book. **No account access and no spend distribution**, and the presenter says so twice unprompted: "ad account honestly means nothing because it doesn't tell us spend distribution."

**The measured shape of the account.** 96% of ads sit in the product-aware and most-aware stages. 21% are dynamic catalogue. 99.6% use "Shop now". **15% of ads carry a celebrity or creator name in the copy.** 0% mention price, 0% mention a discount, 0% carry the risk reversal the brand actually offers, 0% mention the loyalty programme, the app, or the 150-plus retail stores. Three quarters of paid traffic lands on a category page.

**The claim.** Demand is created outside the account by celebrity and creator seeding, and the account's only job is capture. His one-line summary: "Alo Yoga runs ads for people that already know about Alo Yoga."

**The consequence he draws, and this is the part to carry past fashion.** In an account shaped this way the commercial impact of in-account work is small and systematically overstated. "Does launching a new ad set in a meta campaign with the same ads on a different bidding strategy, is that going to grow this 100-200 million business? Probably not. At best, it's probably going to add 1% to the existing performance out of that campaign." He then names the failure mode precisely: revenue dips on a natural fluctuation, the agency bumps budgets 5%, changes a bid and kills a creative, revenue recovers on its own, and both sides now hold a false belief about what those three changes are worth.

**The named dependency, which is the honest cost of the strategy.** There is no true cold-prospecting creative in the account, so if cultural attention softens there is nothing in the account to find new customers with. He is explicit both that this is working and that roughly 95% of brands cannot run it, because they use Meta as the new-customer engine with nothing outside it doing the top-of-funnel work.
Sources: """ + BSD + """
Last touched: 2026-09-14
""")

# ============================================================== CR-235, new, T3
append("Creative Science.md", """
### CR-235 · Alo Yoga's live ads have a 5-day median age and a 24-day oldest, and the operator's verdict is that a turnover clock this tight is an unforced error that stops winners being milked
Tier: T3 · Status: active
Same teardown, from a public ad-library scrape. 190 distinct copy lines across the account, new assets entering roughly every 7 days on what he reads as the merchandising drop calendar, **median age of a live ad 5 days, oldest live ad 24 days**. Nothing in the account is older than a month. The unique-asset count is garbled in the auto-transcript and is deliberately not reported here.

**The tension he names is specific to fashion and generalises past it.** "You are constantly balancing newness whilst trying to maximize winners, and most people will overoptimize towards newness rather than maximizing winners."

**His recommendation runs against his own explanation of why Alo does it.** He accepts that a distribution-shaped account wants grade-A inventory only and wants last season's assets gone. He still calls the 24-day ceiling "wild" and argues for holding winners: "If you have a winning product, you should triple down on the thing. You should just be ordering and ordering for years on end until the market stops wanting that product." The binding constraint he concedes is stock, and his answer is replenishment inside 3 to 4 weeks rather than letting the ad die with the size run.

**Read this against the turnover claims, because it points the other way.** Most of this codex's fatigue material argues for volume and replacement. This one says a 24-day ceiling discards proven assets on a calendar rather than on performance. Both hold: what he is attacking is turnover ON A CLOCK, not turnover. The single caveat he offers himself is that the verdict flips if Alo is flexing budgets hard enough to exhaust an asset inside 20 days, which the ad library cannot show.
Sources: """ + BSD + """
Last touched: 2026-09-14
""")

# ============================================================== CR-236, new, T3
append("Creative Science.md", """
### CR-236 · Premium positioning is asserted through photography and association and never defended in words: 0% of Alo Yoga's ads mention price, discount, risk reversal, loyalty or stores
Tier: T3 · Status: active
Same teardown. Median product $118, leggings $98 to $148, pants to $338. The cheapest entry point is a $48 bra and **nothing in the account promotes it**, which he reads as deliberate and correct: do not advertise your lowest average unit retail.

**The claim.** "Their premium pricing is asserted through photography, positioning, associations. It's not defended through words." The brand holds real incentives (10% off for an email, a gift-with-purchase programme, free express for members, Afterpay, instant refunds) and keeps every one of them out of the ad, letting them work post-click. He classes the risk reversals as table stakes that hold conversion rate rather than as an offer: "if they didn't have this stuff it would impact conversion rate."

**The stated mechanism.** Making a price or discount association destroys the aspirational frame that holds the pricing power. This is the reason he gives for the absence of problem-agitating creative too, and he treats the two as one decision: choosing to repel the problem-aware buyer is the cost of the price point.

**His one dissent, and it is a geography argument rather than a brand argument.** Zero ads mention the 150-plus stores. He argues that in a market with no store a store mention is pure credibility with no downside, because the viewer cannot walk in. "I had no idea that Alo Yoga had stores until last week... immediately conversion rates will go up a little bit, brand trust will go up a little bit, which will help the entire funnel." The executable version is store hauls, try-ons or collection walkthroughs shot in a flagship and run into countries with no stores.

**The limit he puts on the whole aspirational play, offered as a challenge to his own audience.** He has never seen a $100M women's fashion brand that problem-agitates, can name roughly six on the men's side, and guesses that problem-agitating brands do not price this high. Treat that as an observation from one agency's book, not as a rule.
Sources: """ + BSD + """
Last touched: 2026-09-14
""")

# ============================================================== CR-237, new, T3
append("Creative Science.md", """
### CR-237 · Sending paid traffic to a fashion collection page makes the top six products the real landing page, and a size-curve stock-out tanks conversion rate with no account change to explain it
Tier: T3 · Status: active
Same teardown. Three quarters of Alo Yoga's paid traffic lands on a category page: 220 ads to New Arrivals, 79 to Best Sellers, the remainder across homepage, men's equivalents and product pages.

**The first-order claim.** "The performance of a collection page in fashion is going to be heavily dependent on whatever the top six products are... if this is grade C inventory, if people don't want these products for whatever reason, this landing page performance will tank." The grid order is a conversion-rate lever that sits outside the ad account entirely.

**The second-order version, which is the one that gets missed.** Traffic concentrates on the winning products and then on the winning variants inside them. When the best-selling colour and the middle sizes go out of stock, he estimates roughly 30% of arriving traffic lands on an unbuyable variant. "Size curves breaking in fashion ends up being a very large contributor to decreasing conversion rates." Nothing in the ad account changed, so every in-account diagnosis of that decline will be wrong.

**This is independent convergence on [[Google PMax & Shopping#GP-017|GP-017]], from a different channel and a different operator.** GP-017 holds that a fashion size curve breaking costs roughly 50% of efficiency and prescribes a feed rule that pulls the whole product when its highest-sell-through size hits zero. That claim is about the Shopping feed. This one is about a Meta-driven collection page. Same failure, two surfaces, and the two operators reached it separately, which raises confidence in the mechanism well above either claim's own tier.

**The operational consequence he assigns.** A named person owns the grid order and watches that lander's conversion rate daily. He will not extend the practice outside the vertical: "if you're not in fashion, questionable, I'd be careful, I'd probably do custom landers."
Sources: """ + BSD + """
Last touched: 2026-09-14
""")

# ============================================================== CR-238, new, T3
append("Creative Science.md", """
### CR-238 · A landing page built from one creator's own shoot gives an ad-to-page congruence a collection page cannot, and the blocker is usually the talent contract rather than the build
Tier: T3 · Status: active
Same teardown. Alo Yoga runs a custom collaboration page for one celebrity, filled with that person's own photo shoot, and the ads featuring her land on it. "This performs incredibly well because it has congruency from the front end messaging." He calls it the most interesting page in the account and a recent learning of his own.

**His criticism is of the execution, not the idea.** The page as scraped is a stack of images with no product carousel and no story about how the collaboration came about, both of which he would add. He recommends the pattern for any fashion brand running a large performing creator, and his guess for why it is not done for the brand's other recent signings is that the talent negotiation forbade it. That is a guess and is labelled as one.

**Where it sits.** [[Creative Science#CR-086|CR-086]] already holds that the landing page must mirror the ad's persona, angle and offer, and that congruence rather than page format is what wins. This is that rule with a PERSON as the matched variable, which is the version that applies to every creator-led and testimonial-led account, not only to fashion.
Sources: """ + BSD + """
Last touched: 2026-09-14
""")

# ============================================================== MM-213, new, T3
append("Marketing Math & Unit Economics.md", """
### MM-213 · Opening retail stores in a market lifts that market's online revenue, observed as roughly 20% overnight on a Canada entry, so a store opening is an unmodelled confounder in any paid-channel read
Tier: T3 · Status: active
Blue Sense Digital, 2026-09-14, from their own client work entering new markets rather than from the Alo Yoga scrape: "we might enter into as an example Canada and then the client begins opening stores in Canada and online revenue overnight will just go up 20%." No client named, no data shown, stated as a repeated pattern.

**Two mechanisms are offered and they are different in kind.** One is trust: physical distribution raises willingness to buy online from the same brand, which he frames as brand impact. The other is mechanical and specific to apparel: customers try garments in store, buy one item, return it and rebuy online; or the size or colour they want is not in stock in store so they buy it online on the spot; or the decision window simply runs past the visit. He calls the relationship "very one for one" between stores opening and online revenue.

**Why this belongs in the marketing math rather than in a retail note.** A 20% overnight lift in online revenue with no change in ad spend lands in the blended numbers and gets attributed to whatever was running. **Any MER, blended-ROAS or incrementality read taken across a store-opening window is confounded, and the confounder is large enough to swamp the effect being measured.** Ask every client with physical retail for the store-opening calendar before reading a trend line.

**The opinion attached to it, kept separate because it carries no evidence.** He argues retail plus DTC beats DTC alone at scale, on the reasoning that scaling pure DTC through paid drives CAC up with no arbitrage available to suppress it. That is a position, not a finding.
Sources: """ + BSD + """
Last touched: 2026-09-14
""")

# ============================================================== MM-214, new, T3
append("Marketing Math & Unit Economics.md", """
### MM-214 · Break-even ROAS is one over the gross margin and the profit take comes out of the margin before the division: 33% COGS gives 1.49, taking 10% gives 1.75
Tier: T3 for the practice, arithmetic verified independently · Status: active
Sam Piliero, 2026-09-14, worked on screen: 300 orders at $100 each = $30,000 revenue, cost of goods at 33% = $9,900, fixed costs set to zero for the illustration. He reports break-even at **1.49**, then sets a 10% profit take and reports **1.75**.

**The arithmetic checks out, and it is worth stating as a formula because he never does.** Break-even ROAS = 1 / gross margin = 1 / 0.67 = 1.49. With a take of t expressed as a share of revenue, required ROAS = 1 / (margin - t) = 1 / (0.67 - 0.10) = 1.75. Fixed costs enter by reducing the margin before the division, which is why he says the number "goes up and up and up" once a warehouse, a supplier or a salary is included.

**One wording trap, and repeating his sentence produces a 2x error.** He says "if you have a 33% margin business, that means your break even return on investment for the business is 1.49." **1.49 is the answer for 33% COGS, which is a 67% MARGIN business.** A genuine 33%-margin business needs 1 / 0.33 = **3.03**. Decide whether the 33% is cost or margin before touching the formula, and never carry his sentence across.

**The rule he attaches.** The figure with the take included is the account's target, and the only hard floor is never falling under the no-take break-even. He runs the whole scaling decision against this one number, which is how it connects to [[Attribution & Incrementality#AT-119|AT-119]].

**Where it sits.** [[Marketing Math & Unit Economics#MM-068|MM-068]] already requires the CAC target to come from new-customer AOV and new-customer gross profit rather than sitewide figures, and this model does use blended sitewide numbers, which is its main weakness. [[Marketing Math & Unit Economics#MM-088|MM-088]] and [[Marketing Math & Unit Economics#MM-085|MM-085]] carry the discount-depth versions of the same arithmetic.
Sources: """ + SAM + """
Last touched: 2026-09-14
""")

# ============================================================== MM-215, new, T3
append("Marketing Math & Unit Economics.md", """
### MM-215 · An evergreen offer adds value rather than subtracting price, runs two to four weeks at a time, and the named cost of discounting instead is a degraded pixel
Tier: T3 · Status: active
Sam Piliero, 2026-09-14. He separates an offer from a sale and pulls six live examples on screen: AG1 (20% off a first subscription with a code), Talentless (a six-pack tee at 44% off, not sitewide), IM8 (a 90-day reset with a free welcome kit, five sachets and a 90-day money-back guarantee), Manscaped (a bundle at 24% off), Caraway (free baking sheet duo over $675, free shipping over $90), Magic Spoon (subscribe and save 26% plus a free bowl set). The common property he points at in each is that the discount is attached to a specific construction, never applied sitewide.

**The construction menu, verbatim from the list he shares.** Bundle-and-save, dollar off, percent off, buy X get X free, buy X get a percentage off, free gift with purchase, **upgrades** (ship the larger or pro version free), tiered spend-X-save-X, starter or trial kits ("7-day discovery kit", "90-day starting plan", "discovery set"), and a sample gift with purchase. Then stack them: "you create outsized value for the customer, they feel like they're getting a striking deal, but it's only costing you a few extra bucks."

**Evergreen means weeks, not days, and he calls out the common error directly.** Three to six offers in rotation, each running two to four weeks, wrapped in a seasonal name. "Do not get this too confused that you need to run this for three or 4 days and have the next one ready to go and ready to go."

**The mechanism he claims for why straight discounting is worse, and it is a SIGNAL claim rather than a margin claim, which is what makes it new here.** Discounting acquires customers who never return: "their LTV metrics tank, their pixel gets completely killed, you have to recondition the pixel with good customers. Good customers want more. They don't want cheap." No test is shown and no account is named, so the pixel half of this is assertion.

**Where it sits.** Same direction as the discount-depth curve at [[Marketing Math & Unit Economics#MM-085|MM-085]] and [[Marketing Math & Unit Economics#MM-086|MM-086]] and the stacked-offer result at [[Marketing Math & Unit Economics#MM-087|MM-087]], reached by a different argument: those three are margin arithmetic, this one is about who the offer recruits. See also the always-on evergreen offer at [[Creative Science#CR-075|CR-075]].
Sources: """ + SAM + """
Last touched: 2026-09-14
""")

# ============================================================== SC-158, new, T3, contested
append("Scaling Models.md", """
### SC-158 · Interest ad sets are run to WIDEN the pixel rather than to scale, and the interests are chosen to be deliberately unlike the brand
Tier: T3 · Status: contested
Sam Piliero, 2026-09-14. He keeps interest ad sets inside a broad CBO prospecting campaign and states a purpose that is explicitly not performance: "The reason we use interest targeting is not because it's going to significantly scale our whole account or not because it's going to drive massive amounts of return on ad spend. Ideally, all interest targeting does is it just finds something semi-similar and then eventually it allows the pixel to expand its reach to more customers."

**The selection rule is the specific part, and it inverts normal practice.** The interest must be far from the category. "If I was Nike, the interest group I would choose here is not Adidas. It is not Reebok. It is not running shoes. It's something totally different. Maybe it's something just high quality like Sony cameras... maybe it's something like Range Rover because that indicates someone who's aspirational." **The selection criterion is a proxy for customer VALUE, not for category affinity.**

**The diagnosis behind it.** A pixel narrows onto one pocket and stops exploring: "your pixel seems to narrow to like this little grouping right here, and it forgets to try to go over here." The claimed effect of the dissimilar interest set is lower CPM, more reach and a larger available pool.

**Contested, and against two claims rather than one.** [[Scaling Models#SC-070|SC-070]] lists interest targeting among the dead media-buying levers. [[Attribution & Incrementality#AT-061|AT-061]] proposes that interest and lookalike ad sets running beside broad add no conversions and take last-touch credit from broad, so broad reads worse than it is.

**Read the shape of the disagreement carefully, because Piliero does not actually contradict AT-061.** He concedes the conversions, twice and unprompted. His claim is about CPM and reach, which AT-061 says nothing about. So the live proposition is new rather than a rerun: **an ad set can be worth running while contributing no incremental conversions, if what it changes is what the delivery system learns.** Nothing in this codex supports that mechanism from the platform side, no test is shown, and the cheapest way to settle it is the CPM and reach trend on an account before and after the interest sets come out. [[Scaling Models#SC-088|SC-088]] describes a live $1M/month account running broad plus an interest stack plus a lookalike stack with identical ads in all three, which is the structure this claim would justify.
Sources: """ + SAM + """
Last touched: 2026-09-14
""")

# ============================================================== AT-119, new, T3
append("Attribution & Incrementality.md", """
### AT-119 · Read the incremental-attribution column before a budget increase and treat that number as the expectation for the next dollar: one account shows 16.04 against 8.53, a 47% gap
Tier: T3 · Status: active
Sam Piliero, 2026-09-14, shown on screen from a live account. One campaign, last 30 days, **$4,500 spent, 145 purchases, 16.04 ROAS** on the account's default attribution. He then opens Columns, Compare Attribution Settings, ticks **incremental attribution** and applies. Revenue falls from $71,000 to $37,000 and **ROAS falls to 8.53**. He calls the drop "around 50%"; it is 47%.

**The interpretation is the claim.** "This 8.53, this is what you could expect generally for the next dollar that you put into this system. You should not anticipate that you're going to hit this 16 with your next dollar." He then hedges downward from there, on the reasoning that the next dollar reaches higher into the funnel and converts worse.

**The scaling rules he attaches to the gap between that number and the break-even target from [[Marketing Math & Unit Economics#MM-214|MM-214]].** At roughly 21% over target (8.5 against a target of 7) increase budget 20 to 30%. At 3x over target, double, and keep doubling until the figure approaches target. The stated objective is total profit dollars rather than the ratio: "I would much rather have a thousand purchases and make $5 on each of those purchases... as opposed to making one purchase worth $500 worth of profit", which is the same position as [[Marketing Math & Unit Economics#MM-014|MM-014]].

**Why this is worth banking separately from the rest of this file.** Every claim here from [[Attribution & Incrementality#AT-002|AT-002]] through [[Attribution & Incrementality#AT-117|AT-117]] argues about whether to OPTIMIZE to incremental attribution. This is the first use of it purely as a **read-out**, with the optimization setting left alone: the column as a marginal-return estimate for a scaling decision. That reframing is free to adopt and carries none of the delivery risk of switching the optimization event.

**The limits, and they are large.** One account, one campaign, one screenshot, and no before-and-after on an actual budget increase, so the central assertion that the incremental figure predicts the next dollar is asserted rather than demonstrated. Worse, Meta's own description of the setting, quoted at [[Attribution & Incrementality#AT-035|AT-035]], is that it "shifts delivery toward users the platform predicts wouldn't have visited otherwise", which is a model scoring users rather than a holdout. **So 8.53 is itself a model output, and using it as the marginal-return estimate means trusting Meta's prediction to grade Meta's delivery.** The honest version of this practice is that it is a more conservative number than 16.04, not that it is a measured one.
Sources: """ + SAM + """
Last touched: 2026-09-14
""")

# ============================================================== CR-239, new, T3
append("Creative Science.md", """
### CR-239 · A static gets a glance where a video gets seconds, so it carries three parts and no more, and its audience is people who already know the brand
Tier: T3 · Status: active
Fraser Cottrell, 2026-09-13, walking through four statics from his agency's client accounts, two of which he states spent six figures on Meta.

**The anatomy, stated as fixed.** "We have the three pieces that go into every single static ad. A headline, an image, a CTA. You want to catch people's eye with the image. You want to give them more information with the headline and you want to tell them what to do with the CTA."

**The reason for the three-part limit is a timing argument, and it is the useful half.** "Unlike a video, we don't have a couple of seconds where we can hook people in. We have a glance." Everything a static does has to survive being looked at once, briefly, which is why he pushes colour and contrast against the feed rather than composition.

**Where he places statics in the funnel, and it is lower than most of this codex assumes.** "Statics usually sit at the bottom of the funnel, meaning that the people who are consuming them are product aware and problem aware. They know of you. They might have even purchased you in the past. These ads are just all about scooping up those final remaining sales." His illustration is his own behaviour: he ran out of a hair product, forgot to reorder, and a static from that brand triggered the purchase.

**Read against [[Creative Science#CR-048|CR-048]], which holds that statics work across the awareness spectrum but produce fewer winners than b-roll video.** These are compatible: CR-048 is about where statics CAN work, this is about where this operator believes their yield is. The disagreement worth noting is that CR-048 treats statics as spectrum-wide and this treats them as a harvesting instrument, which changes what you measure them against.
Sources: """ + FRA + """
Last touched: 2026-09-14
""")

# ============================================================== CR-240, new, T3
append("Creative Science.md", """
### CR-240 · Frame a real on-site review as a social comment, with a face and a like heart, so a designed ad reads as organic: six figures of spend, ranked 3rd of 435 ads
Tier: T3 · Status: active
Fraser Cottrell, 2026-09-13, on a static built for a UK meal-replacement protein brand. He states it "has spent over six figures on Meta" and shows it ranked in the top 1% of the account's ads, **third out of 435**, read from Trend Track.

**The build.** Product image, a review, a CTA, and nothing else. The review is pulled from the brand's own website and then **reformatted as a social comment**: speech-bubble frame, a photo of a woman inside the target demographic as the commenter, and a small love-heart to imply it has already been liked. "This makes the ad feel more organic even though it's highly designed."

**Where the format came from, which is the part that generalises.** He says they saw competitors using social proof screenshotted directly from social platforms, and reverse-engineered the visual grammar onto a source they actually controlled. The on-site review is real; only its presentation is borrowed.

**Two copy decisions he calls out.** The review chosen is results-driven for the specific product ("Absolutely love these shakes. The weight is dropping off") because the buyer of a meal replacement is after weight loss, not protein. And the opener is deliberately conversational: "starting with something that sounds like someone you know, something someone has said, will do wonders for an ad."

**The SKU decision was data-led and is easy to skip.** The ad names a single flavour, pineapple coconut, because the brand told them it was becoming a top seller. Other SKUs were tested in the same frame and this one won. "The more data that you can arm yourself with, whether it's what SKU sells the best or how your customer sounds, all of this can come together."

Related: [[Creative Science#CR-131|CR-131]] holds the Twitter-style static as another operator's most profitable and longest-lived format. Both are the same move, a designed ad wearing a social-native costume.
Sources: """ + FRA + """
Last touched: 2026-09-14
""")

# ============================================================== CR-241, new, T3
append("Creative Science.md", """
### CR-241 · The native storytelling static puts the whole argument in the CAPTION and uses a shocking recognisable image plus the above-the-fold first line as the headline
Tier: T3 · Status: active
Fraser Cottrell, 2026-09-13, on a format he says he has not covered before and that is "fast becoming an incredibly popular format across our clients". The example is for an eczema brand.

**The inversion.** The image is an extreme close-up of broken eczema skin and does almost no selling: "the actual image isn't really doing anything" on its own. The caption carries the entire story and runs long enough to need a "see more". "It's telling a story which the image then supports."

**The two-part mechanism he names.** First, the image is recognisable enough to stop the exact person who has the problem: "if you have eczema you will automatically recognize that." Second, the first line of the caption, the only line above the fold, functions as the headline. His example line is "a customer shared this with us the other day", and the reaction he is engineering is "oh, well that's what my hands look like. Oh, a customer. Hm, okay, click."

**The production order is backwards from a normal static and he says so.** "Spend time on that copy and then go and find yourself an image that supports it." His method for the image is to search Google Images for the shape he wants, then use that as a reference in an image model and change it enough to be a different image while keeping the shock.

**His own honesty about durability, which is worth keeping attached.** "This might be a trend. This might be something that drops off in a couple of months time. I'm not sure." He notes drop shippers used the same format heavily years ago. The brand launched a batch of these off the back of the first one, and he reports they "spend like crazy" with no figure attached.
Sources: """ + FRA + """
Last touched: 2026-09-14
""")

# ============================================================== CR-242, new, T3
append("Creative Science.md", """
### CR-242 · The native story image is a phone photo dressed as an Instagram story, and the underlined @handle harvests mis-taps into clicks: reported 3.5% CTR, built in 10 to 15 minutes
Tier: T3 · Status: active
Fraser Cottrell, 2026-09-13, on a static for an electrolyte brand. Build: pull the product off the store-room shelf, have someone hold it in a kitchen, take one photo on a phone, drop it into Figma, and add text styled to imitate Instagram's own story UI. He reports six figures of spend, **a click-through rate of "like 3.5% or something"**, and a build time of 10 to 15 minutes.

**The effect he is buying.** "If you're scrolling through your stories, you are going to stop at something where you don't recognize it, but it kind of interests you. It piques your interest enough to stop, you consume the content, and then you realize it's an ad." He cites watching his wife do exactly that.

**The specific trick, and this one is mechanical rather than creative.** The brand name and the @handle are underlined in the story-UI style, so viewers try to TAP them the way they would tap a real handle. "They'll try to click on it and of course that will up the click-through rate and send them to the landing page." The tap goes to the landing page because every tap on an ad does. Note that this inflates CTR by capturing intent to view a profile rather than intent to buy, so the 3.5% should not be read as 3.5% of people wanting the product.

**His production warning, which applies to every AI-assisted static.** Do not generate the image and the text together in one pass, because changing one word forces a full regeneration. Shoot or generate a few POV product images, write the copy separately, assemble in a Figma frame, and test the combinations. "Set up a little Figma framework in there and just fire them out."

**The stacking note.** He recommends pairing this format with whitelisting or a partnership ad, so the organic-looking creative also carries a real handle behind it.
Sources: """ + FRA + """
Last touched: 2026-09-14
""")

# ============================================================== CR-243, new, T3
append("Creative Science.md", """
### CR-243 · Reviews are the concept source and the voice at once, and a winning static is an idea to port into other formats rather than an asset to iterate
Tier: T3 · Status: active
Fraser Cottrell, 2026-09-13, demonstrated live rather than described. He opens a fragrance client's product page, scrolls to reviews, and reads one aloud: "I put this on after my shower and my husband went crazy... He's super sensitive to fragrances and usually hates everything I put on. This was different... Please don't make it limited edition. I've been looking for my scent forever."

**Three concepts out of one review in about two minutes, which is the claim.** The first sentence becomes a video hook. "Totally 10 out of five stars" becomes a quoted headline over a product image. The sensitive-husband line becomes a whole podcast-ad narrative about a woman who could not wear perfume because the smell gave her partner a headache. "If you just read that and scroll by, then you might need to readdress your career, because that is absolute gold."

**The voice rule, and it is the reason he insists on doing this manually first.** For the caption-led formats, copy the review nearly verbatim. "That is your story static, because it sounds like the customer, because it's written by the customer... if it sounds like someone that's not them, they aren't going to relate to it. They're just going to scroll by." He is explicit that AI should only enter after the operator can do it by hand: "I really don't want us to become AI-brained here."

**The second half of the claim, on what to do with a winner.** A static is cheap enough to be an idea-testing instrument, and the idea is the asset. His example is a perfume headline, "Claim it before the group chat does", built on the reader's expectation that friends will copy her purchase. That one line spawned UGC videos and podcast ads built on the same tension. "Don't let just one idea be one idea. It can become so many different formats."

**And the loss case is also information.** "When you test the static, even if that static doesn't work, what about it didn't work? Was it the messaging? Was it the imagery?" Decompose before discarding.

Related: [[Creative Science#CR-102|CR-102]] already mines incumbent reviews to pick the launch AVATAR. This mines your own reviews for ANGLE and VOICE, which is the later-stage use of the same corpus.
Sources: """ + FRA + """
Last touched: 2026-09-14
""")

# ==================================================== SC-024, amendment
SC024_SRC = "Sources: Sam Piliero, The Only Facebook Ads Video You Need in 2026, 2026-07-26;"
SC024_ADD = """**A FIFTH video adds the enforcement mechanism and, for the first time, the reason, 2026-09-14.** Every restatement above describes WHERE new ads go. This one describes what is done to make them deliver, and names the failure it exists to prevent: **a 7-day minimum budget is forced onto each new pack.** "The reason we set this 7-day minimum budget is because it forces for just 7 days budget against a new adset to give it a fair shot to see if it's actually scalable."

**The stated diagnosis is the part worth carrying.** "One of the biggest problems in the Andromeda algorithm that we have experienced is that when we launch new ads in existing campaigns, they get no spend and then we never know if the creative that we've spent so much time producing actually works. Occasionally, it ramps to the top on its own, but we always want to give it a little bit of a booster pad." So the pack rule is not only about protecting incumbents from tests, it is about a CBO refusing to fund anything unproven, and the minimum budget is the workaround. That converges with [[Scaling Models#SC-086|SC-086]] on consolidation starving committed spend, and it is the same problem [[Meta Delivery & Andromeda#MD-094|MD-094]] says Meta's own creative-testing tool solves by forcing minimum spend through chosen ads.

Also newly specified: each pack holds **one avatar and between two and eight creatives**, and packs are trimmed rather than paused wholesale, "you're pausing the bad, you're keeping the good". Still no performance data attached to any of it after five videos.
Added source: """ + SAM + """
"""
edit("Scaling Models.md", SC024_SRC, SC024_ADD + SC024_SRC)

# ==================================================== CR-031, amendment
CR031_SRC = "### CR-031 · Animating a winning static counts as a genuinely different entity post-Andromeda; the format is resurging and AI collapses production to 5-10 minutes"
CR031_ADD = """**AMENDED 2026-09-14 with the static-to-static version of the same threshold.** CR-031 covers turning a static into a video. Fraser Cottrell states the rule for staying inside the static format, and it is stricter than most variation practice: a headline swap on one design does not clear the bar. "Instead of just having that static and switching out the headline, we're building different designed ads, essentially different statics, but based around the same messaging... You want to make these assets as different as you can do, so Meta sees them as different assets."

So the unit being varied is the DESIGN, and the thing held constant is the message. His worked example is one message, the perfume group-chat line, rendered as several visually unrelated statics including a call-out ad. He frames it as harder than it used to be: "with Meta's Andromeda changes, it can be a little bit harder. It's a bit more of a dance." Asserted from agency practice, no test shown, and it is the same threshold question as [[Creative Science#CR-172|CR-172]].
Added source: """ + FRA + """

"""
edit("Creative Science.md", CR031_SRC, CR031_ADD + CR031_SRC)

print("\nMERGE COMPLETE")
