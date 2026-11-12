"""Claim merge for the 2026-11-12 research pass.

Sources actually read in full this pass:
  - Meta Engineering, "Intelligent Delivery: Making Every Unit of Compute Serve
    Better Ads", 2026-11-11 (T1)
  - Google Ads & Commerce blog, "We're introducing a new transparency tool for
    invalid traffic in Google Ads", 2026-11-12 (T1)
  - Professor Charley T, "Copy this 3-Part Meta Ads Strategy, It'll Blow Up your
    Business", 2026-11-11, 58 min, 9,606 words (T3)
  - Ben Heath, "The REAL Secret to Winning with Meta Ads", 2026-11-11, 23 min,
    4,944 words (T3)
"""
import io
import os

SCI = os.path.join(
    "E:\\claude code marketing skill",
    "Obsidian God-level Marketing Vault", "God-level Marketing", "wiki", "science")


def rd(name):
    return io.open(os.path.join(SCI, name), encoding="utf-8").read()


def wr(name, text):
    io.open(os.path.join(SCI, name), "w", encoding="utf-8", newline="\n").write(text)


def amend(text, header, addition):
    """Append a paragraph to the claim block starting at `header`."""
    i = text.index(header)
    j = text.index("\n### ", i + 10)
    block = text[i:j].rstrip()
    return text[:i] + block + "\n\n" + addition.strip() + "\n" + text[j:]


# ---------------------------------------------------------------- Meta Delivery
MD = "Meta Delivery & Andromeda.md"
t = rd(MD)

MD199 = """
### MD-199 - T1: Meta allocates a DIFFERENT amount of compute to every individual ad request, decided by a 6B-parameter model that runs before retrieval, and the allocation layer alone is credited with ~10% of ranking performance
Tier: T1 . Status: active
Meta engineering, 11 November 2026, "Intelligent Delivery: Making Every Unit of Compute Serve Better Ads". The system is an ML layer that decides, per request, how much of the serving stack to spend on it. Meta credits it with "an additional ~10% improvement in ads ranking performance on top of model and system advancements across major surfaces, from 2017 through the first half of 2026". The premise is stated outright: "The same additional unit of compute can generate very different returns depending on the product surface, user intent, candidate quality, and system state."

**The three layers, as published.** One, a *Resource Core Model*, **6B sparse and 20M dense parameters**, runs ONCE before candidate retrieval and is shared across the whole delivery funnel; it predicts each request's outcome, compute consumption and latency impact, and specialised fine-tunes read off it. It replaced hand-written segment rules that grouped requests by surface, context and creative representation, and is reported as "about a 20% improvement in identifying the highest-impact ad requests in offline benchmarks on major surfaces, relative to our previous production model". Two, a hierarchy of decision engines: which REGION serves the request, re-balanced "in a cycle of minutes" toward equal marginal efficiency across regions; which HARDWARE it lands on, across Intel, AMD and Arm CPUs and NVIDIA, AMD and MTIA accelerators, assigned by measured efficiency per workload-SKU pair because "retrieval [is bound] by memory capacity, ranking by compute, and model inference by accelerator throughput"; and how much of the HOST it gets, a constrained optimisation under a hard tail-latency SLO reaching from the kernel scheduler up to application thread pools. Beyond those three it also sets "the number of ads to rank for each request in each ranking stage, what ad candidates enter the pool, and much more". Three, an agentic optimisation loop: agents read mechanism source code, design documents and "a decade of experiment logs" to narrow millions of tunable dimensions to a handful of changes worth testing, with an engineer approving every change. **"In the first half of 2026, agents contributed to about 20% of Intelligent Delivery optimizations. On our most automated mechanism, they now contribute to about 80% of the engineering effort."**

**Why it matters to an operator.** This is the first T1 statement that the DEPTH of the ranking funnel is a per-request variable rather than a constant. How many of your candidates get ranked, and how hard, depends on the marginal return Meta's own model predicts for that request, on how loaded the host is ("as the host load increases, the performance trade-off rises and resource-intensive low-impact work is trimmed first"), and on which region and chip generation the request landed in. Two consequences for how we read accounts. Identical ad sets can receive genuinely different serving treatment request to request, which is a named mechanism underneath the volatility [[Scaling Models#SC-102|SC-102]] tells low-volume accounts to accept as an operating condition. And a request predicted to be low-value is explicitly served more cheaply, which is a mechanism for cheap impressions being structurally thinner rather than merely colder.

**The honest limit, state it every time.** Nothing here is a lever. The post names no advertiser-visible control, no reporting surface, and no way to influence the allocation. The ~10% is Meta's own cumulative figure across nine years with no methodology, no holdout and no breakdown published, and the ~20% identification gain is an offline benchmark against their own previous model. Do not quote either number as something an advertiser can capture. Reads onto [[Meta Delivery & Andromeda#MD-022|MD-022]] and [[Meta Delivery & Andromeda#MD-023|MD-023]] on the multi-stage funnel, [[Meta Delivery & Andromeda#MD-189|MD-189]] on retrieval quality per FLOP, and [[Meta Delivery & Andromeda#MD-198|MD-198]] on serving budgets rising 1.2x to 10x: MD-198 says the budget per model went up, MD-199 says that who receives it is itself a prediction.
Sources: Meta Engineering blog, Intelligent Delivery: Making Every Unit of Compute Serve Better Ads, 2026-11-11 (read in full 2026-11-12)
Last touched: 2026-11-12
"""

MD200 = """
### MD-200 - "Mid-funnel" is not a readable state: an ad's funnel position is its daily frequency against the CAMPAIGN'S OWN daily frequency, and no external number applies
Tier: T3 . Status: active
Charley T, 11 November 2026, stated as a rejection rather than a refinement: "I want you to reject the idea that mid-funnel exists. What you have is a baseline, the campaign's own daily frequency." Procedure: read the campaign's daily frequency, say 1.23; any ad below 1.23 sits higher in the funnel than the account's own centre of gravity, any ad above it sits lower. "You're reading each ad against the account it lives in, not against some number you saw on somebody's random out-of-context screenshot."

**The pairing he attaches is the operative half, because it converts the read into a diagnosis.** Below-average frequency with a below-average CPM means the ad is filling the funnel, so its cost per result is EXPECTED to be worse than the account average and that is not a fault. Above-average frequency with an above-average CPM means it is working the warm audience, so its cost per result has to be BETTER than average: "If it can't close the deal better than your prospecting ads do to complete strangers, it's a bad retargeting ad." That is what tells you whether the account has an upper-funnel or a lower-funnel problem, which then decides which concept gets tested next.

Sharpens [[Meta Delivery & Andromeda#MD-047|MD-047]], where frequency only "tells you who the ad is being shown to", by supplying the missing comparator, and it is the discipline of [[Meta Delivery & Andromeda#MD-080|MD-080]] (never compare two ad sets at different spend levels) applied between ads inside one campaign. It is also compatible with [[Meta Delivery & Andromeda#MD-155|MD-155]]: the campaign figure here is used only as an internal yardstick between ads in the same campaign and is never read as fatigue, which is exactly what MD-155 forbids. Asserted, no data shown, and the absolute numbers are account-specific by construction, so there is nothing here to benchmark against anyone else's account.
Sources: Professor Charley T, Copy this 3-Part Meta Ads Strategy, It'll Blow Up your Business, 2026-11-11
Last touched: 2026-11-12
"""

t = t.rstrip() + "\n" + MD199 + MD200

t = amend(
    t,
    "### MD-008 - Early-life frequency reveals learning"
    if "### MD-008 - Early-life" in t else
    "### MD-008 \u00b7 Early-life frequency reveals learning",
    """**Restated verbatim 2026-11-11 by the same operator, with the misread now named as the cause of an entire behaviour pattern.** "A frequency of 1.6 means 60% of people saw that ad twice in a single day. A frequency of 1.2 means only 20% of people did... Then as learning ends, spend goes up and frequency comes down. That's not the ad dying. It's the ad moving up the funnel." He attributes the whole launch-panic-kill cycle to operators reading that decline as fatigue and switching off the upper-funnel ads that were building the audience everything else converts. No new evidence, so the tier does not move; what is new is that the claim is now the stated foundation of his entire operating system rather than an isolated observation. Source added 2026-11-12.""")

t = amend(
    t,
    "### MD-047 \u00b7 The 4PI read" if "### MD-047 \u00b7 The 4PI read" in t
    else "### MD-047 - The 4PI read",
    """**The read is now published as "4PI plus two", 2026-11-11, and the two additions are the money columns.** The four stay as banked: spend, frequency, CPM, and cost per result, which he now calls efficiency. Added are **gross profit per transaction, built as a custom metric because Meta carries no default for it, defined as AOV minus CPA**, and **AOV, read as customer quality**. His argument for AOV as its own column: "Let's say one ad has an AOV of 65 and another has an AOV of 100. Those ads are selling different things to different people, even if they're in the same ad set, even if they're going to the same landing page." He also states the exclusions explicitly for the first time, and they are aggressive: the dashboard carries **no ROAS, no CTR, no CPC and no hook rate**, all named as vanity metrics. The GPT half is the same build and the same unstated-COGS problem already banked at [[Marketing Math & Unit Economics#MM-080|MM-080]] and guarded at [[Scaling Models#SC-049|SC-049]]; here he states the limit himself, that GPT "isn't a profit and loss statement" and is only good for comparing one ad against another "because the same costs sit behind all of them". The comparator for the frequency column is banked separately at [[Meta Delivery & Andromeda#MD-200|MD-200]]. Source added 2026-11-12.""")

wr(MD, t)
print("MD ok:", t.count("### MD-199"), t.count("### MD-200"))

# --------------------------------------------------------------- Scaling Models
SC = "Scaling Models.md"
t = rd(SC)

SC183 = """
### SC-183 - A creative test is judged ONLY on whether the account can absorb more money afterwards, so a test with a good CPA that does not restore headroom is recorded as a loss
Tier: T3 . Status: active
Charley T, 11 November 2026. Every test resolves into exactly three outcomes, and the pass mark is never the test's own efficiency.

1. **Win.** The test earns spend and the volume of profit in the business rises, which he reads as GPT holding roughly flat while the budget goes up. Action: change nothing, do not harvest the post ID, do not touch it, and let the automated budget rule take over. His suggested custom metric for the judgement is "profit volume", total revenue minus total ad spend.
2. **Loss.** The test takes spend but the budget still cannot be raised. "It's a failure because it didn't get you back to a yes on move number one." Stated against the obvious objection: "I know that feels harsh when the CPA looks decent or the ROAS is great, but a test that earns money and doesn't allow you to scale the budget isn't a win." Action: turn it off and launch the next test.
3. **No spend.** Delivery looked at it and declined, which he treats as a verdict rather than a fault, on the mechanism that the first few hundred impressions against the warm audience were enough to model expected behaviour against everything else competing. **One exception only:** a LOWER-funnel test launched into a new ad set and starved because the upper-funnel ad is already satisfying the shared objective gets a 20% minimum budget "so you can get a fair read", and the same move is allowed for an upper-funnel test when a single ad is soaking the campaign and nothing else delivers.

**Why this is worth banking separately from the kill rules.** It makes the unit of judgement the ACCOUNT's capacity to take budget, not the ad's row in Ads Manager, which is the only criterion in the codex that cannot be gamed by an ad that converts cheaply on a small warm pocket. It is the test-side counterpart of the headroom gate in [[Scaling Models#SC-001|SC-001]]. Outcome 3 agrees with Piliero, who accepts that a newly launched ad may take no spend across a full 7-day window and treats that as a verdict rather than a delivery fault, with the counting consequence banked at [[Scaling Models#SC-121|SC-121]]; the 20% minimum remedy is the same instrument Piliero uses for the opposite purpose, forcing test spend onto produced ads so none sits at zero delivery. Entirely asserted. No account shown, no before-and-after, and the "profit volume" metric is proposed rather than demonstrated.
Sources: Professor Charley T, Copy this 3-Part Meta Ads Strategy, It'll Blow Up your Business, 2026-11-11
Last touched: 2026-11-12
"""

t = t.rstrip() + "\n" + SC183

t = amend(
    t,
    "### SC-049 \u00b7 Two-axis kill rule" if "### SC-049 \u00b7 Two-axis kill rule" in t
    else "### SC-049 - Two-axis kill rule",
    """**The spend band this rule has always lacked arrived 2026-11-11, and it answers the AOV-collapse failure mode account three demonstrated above.** Sort ads by amount spent, then act only on an ad **taking at least 10% and no more than 40% of the budget** whose CPA is above the campaign average and whose GPT is below it. **Above 40% of spend the ad is explicitly left alone**, for a structural reason rather than a performance one: "Removing it changes how the whole campaign works. And that's a bigger decision than this move." The cadence is stated too: wait **at least 48 hours** after the switch-off, re-read on a **trailing 7-day** view rather than the last three days (three to seven days on a low-volume account), and make **at most two or three such moves a week**, "because if you stack move on top of move, you'll never know what worked". He notes the rule usually bites when **four to eight ads are live**, and that on a heavily over-launched account it is fine to switch off several small ads together to clear the 10% floor.

**This is the first stated version of "prune in steps" that names the steps**, and the 40% ceiling is the useful half, because it protects exactly the ad whose removal collapsed GPT from $206 to $131 in account three. It sits inside the 20%-of-account-spend-per-day brake at [[Scaling Models#SC-132|SC-132]], so the two are compatible rather than competing. Still asserted: no account was shown for the 10%, the 40% or the 48 hours. Source added 2026-11-12.""")

t = amend(
    t,
    "### SC-001 \u00b7 How big a budget step is safe is contested"
    if "### SC-001 \u00b7 How big a budget step is safe is contested" in t
    else "### SC-001 - How big a budget step is safe is contested",
    """**The half-the-headroom rule was restated and fully operationalised 2026-11-11, and this pass adds the two parts that were missing: where the target comes from, and the firing schedule.** The target CPA "comes from your unit economics, not from yesterday's ROAS", the current figure is the trailing 7-day CPA read off the campaign row, and the gap between them is the headroom. His framing is worth keeping because it kills a common misread: "headroom is a gap. It's leverage. It's not a score. A CPA on its own tells you nothing until you set it against the target." Worked both ways in the same breath: a $50 target against a $45 trailing CPA is 10% headroom and licenses a 5% raise, while a $46 target against the same $45 is the identical CPA with almost no headroom and licenses nothing. He also names the consequence of waiting: "if you only decide to scale once you've hit your target, you're already at your ceiling."

**The mechanism he gives for why only half the gap is spent is new here and is testable.** New budget does not buy more of the people who would have converted anyway, it buys colder impressions at the top of the funnel first, so cost per result rises for a period after every increase: at a $50 CPA and a $20 CPM the account needs about 2,500 impressions per sale (arithmetic checks: 50/20 x 1,000 = 2,500) and the marginal money buys those from colder people. That makes the half-step a buffer against a temporary post-increase CPA rise rather than a profit-margin rule, which is a different justification from the one this claim recorded on 2026-05-17.

**The automated-rule build, and it CONTRADICTS a banked configuration.** Applied at campaign level because the budget lives there, action "increase daily budget by 5%", condition "cost per purchase, last 7 days, at or below 90% of target", and schedule **Monday, Wednesday and Friday only**, with the reason stated: "A daily rule keeps pushing the budget before the account has had time to absorb and react to the last move, and you end up with runaway compounding interest." [[Scaling Models#SC-101|SC-101]] carries Ben Heath prescribing exactly the opposite, **one firing daily** between midnight and 1am so each move gets a full day of data. Both are asserted from large managed books with no data behind either schedule. The disagreement is narrow and cheap to settle on our own accounts: same rule, same step, same dead band, one campaign fired daily against a comparable one fired three times a week, read account cost per result at 30 days. Source added 2026-11-12.""")

wr(SC, t)
print("SC ok:", t.count("### SC-183"))

# ------------------------------------------------------- Google Auction/Bidding
GA = "Google Auction & Smart Bidding.md"
t = rd(GA)

GA101 = """
### GA-101 - Google now shows invalid-traffic savings and credits in the Ads UI, and states it cut advertiser exposure to invalid LEADS by an average of 30% so far in 2026
Tier: T1 . Status: active
Google Ads & Commerce blog, 12 November 2026, by Keerat Sharma, VP and General Manager, Ads Privacy and Safety. Three things are stated, and only the first is a product change.

**One, a new surface.** An **Invalid Traffic Overview Card** is rolling out in Google Ads so advertisers can see, "for the first time", both the amount saved by invalid traffic being blocked before billing and the credits Google issues automatically when it is detected after the fact.

**Two, the billing position restated.** "We don't charge for invalid traffic, and our multi-layered defenses have always worked in the background to catch it before an advertiser is billed. We issue a credit when it's detected later, **where appropriate and possible**." Carry that qualifier verbatim; it is the whole difference between a guarantee and a best effort.

**Three, the only number in the post.** "So far in 2026, we've reduced advertiser exposure to invalid **leads** by an average of 30% through continuous system upgrades." Note the word is leads, not clicks, which makes it the more relevant figure for the lead-gen accounts we actually run, and note what is absent: no baseline, no denominator, no definition of an invalid lead, no methodology, and no per-account or per-vertical breakdown. It is a platform-wide average asserted in a marketing post.

**What to do with it, and what not to.** When a client's Google spend or lead count looks lower than expected, this card is now a place to look before building a theory, and the credit line is worth reading on any account where we have previously eaten a spike of junk form-fills. It is **not** a reason to tell a client their junk-lead problem is solved, and the 30% must never be quoted to a client as something their account received. Same reporting discipline as our own rule on never calling last-click-zero spend "wasted": a platform-reported saving is the platform's own measurement of its own work. Adjacent to the financial-scam-ads enforcement work in the same author's earlier post.
Sources: Google Ads & Commerce blog, We're introducing a new transparency tool for invalid traffic in Google Ads, 2026-11-12 (read in full 2026-11-12)
Last touched: 2026-11-12
"""

t = t.rstrip() + "\n" + GA101
wr(GA, t)
print("GA ok:", t.count("### GA-101"))

# ------------------------------------------------- Marketing Math & Unit Econ
MM = "Marketing Math & Unit Economics.md"
t = rd(MM)

t = amend(
    t,
    "### MM-002 \u00b7 The LTGP:CAC bands are real but the ratio is not portable"
    if "### MM-002 \u00b7 The LTGP:CAC bands" in t
    else "### MM-002 - The LTGP:CAC bands are real but the ratio is not portable",
    """**A FOURTH stated numerator, banked 2026-11-12, and it widens the band dispute rather than the numerator dispute.** Ben Heath builds the ratio live in a sheet and uses **gross profit explicitly**, with the gross-versus-net distinction spelled out and defended: deduct cost of goods sold and direct labour only, and deliberately exclude overheads, office costs and professional fees "because those are relatively fixed. They're not marginal as you scale." That puts him with Andrew Faris and Blue Sense on the numerator, so three of five now use gross profit, one uses revenue, and one moves between them.

**The problem is the bands, and the gap is enormous.** On the gross-profit numerator Blue Sense puts the ramp zone at 2 to 3 and reads anything above 3 as leaving money on the table. Heath's worked example lands at **10** and he calls it "fantastic... likely a very profitable business", then improves it to **28.8** and treats that as the goal rather than as a symptom of chronic underspend. Same numerator, same metric, and a band roughly an order of magnitude apart. Neither side shows comparative data, and the likely reconciliation is the business mix behind each book: Blue Sense's figures come from e-commerce audits where media is nearly the only acquisition cost, while Heath's examples are services and local businesses carrying heavy delivery labour and overhead, where a 10 on gross profit can still leave little net. **The operating rule this claim already states therefore needs a second half.** State which numerator a ratio uses before acting on it, AND state the business model behind the band, because a 10 is a scaling signal in one book and evidence of underspend in another. Nothing here resolves it, and the ratio stays contested.
Sources added: Ben Heath, The REAL Secret to Winning with Meta Ads, 2026-11-11""")

t = amend(
    t,
    "### MM-068 \u00b7 Derive the CAC target from new-customer AOV and new-customer gross profit"
    if "### MM-068 \u00b7 Derive the CAC target" in t
    else "### MM-068 - Derive the CAC target from new-customer AOV and new-customer gross profit",
    """**The lead-gen port of this derivation, with the arithmetic checked, 2026-11-12.** Ben Heath states both forms as a break-even ceiling rather than a target. For e-commerce, **maximum acceptable cost per purchase = AOV x gross profit margin**, which is break-even on the first transaction and which he frames as the cash-flow-safe starting point rather than the aggressive one. For lead gen, **maximum acceptable cost per lead = AOV x gross profit margin x lead-to-client conversion rate**, because "we can't pay that per lead, because obviously there's a conversion rate from lead to client".

**His sensitivity run is the part worth carrying, because it prices the sales process as a media lever.** On a $1,000 first transaction, at a 75% gross margin the gross profit is $750, and the acceptable CPL moves **$75 at a 10% close rate, $150 at 20%, $225 at 30%** (all three recompute exactly). Identical offer, identical delivery cost, identical margin, and a **threefold** difference in what the account is allowed to pay for a lead, decided entirely downstream of the ad. That makes the close rate a budget input, and it is the cleanest argument in this file for why post-lead experience outranks creative work on a lead-gen account. He closes the loop to scaling: you need headroom between the current CPL and the ceiling, because "as we scale, our cost per lead is likely to increase", which is the unit-economics source of the target in the headroom rule at [[Scaling Models#SC-001|SC-001]].

A third operator therefore now lands on the same derivation from a third direction, which strengthens the claim's core point: the acceptable cost is an OUTPUT of the business and a benchmark is never an input. Worked in a spreadsheet on screen with round illustrative numbers; no client account named and no realised figures shown.
Sources added: Ben Heath, The REAL Secret to Winning with Meta Ads, 2026-11-11""")

t = amend(
    t,
    "### MM-121 \u00b7 Profit equals (blended AOV minus blended CPA) times transaction volume"
    if "### MM-121 \u00b7 Profit equals" in t
    else "### MM-121 - Profit equals (blended AOV minus blended CPA) times transaction volume",
    """**The lever ranking in this claim now has arithmetic behind it from a second operator, and every figure recomputes exactly, 2026-11-12.** This entry has sat at T4 because the "AOV beats CPA" argument was asserted. Ben Heath runs it as a worked comparison on one baseline: AOV $200, five purchases, 50% gross margin, so $500 lifetime gross profit; $10,000 spend acquiring 200 customers, so a $50 CAC and a ratio of **10**.

- Work the CAC side hard, 200 customers becomes 250, a 25% improvement: ratio **12.5** (500/40).
- Work the value side, AOV $200 to $300, purchases 5 to 8, margin 50% to 60%: LTGP $1,440, ratio **28.8** (1,440/50).

All three check to the stated figures. The conclusion he draws is the ranking: "it would be impossible to reduce your cost to acquire a customer enough to go from a 10 to 28.8", so limited time goes into customer value, not into cost per acquisition. Within the value side he ranks **repeat purchases first**, on a feasibility argument rather than a magnitude one: tripling the number of purchases is usually achievable given time, tripling AOV is sometimes achievable, and tripling gross margin is "almost never, unless it's really bad to begin with". His subscription case makes the same point against the hardest condition, **halving AOV to $100 while taking purchases from 5 to 23** still lifts LTGP from $500 to $1,150 and the ratio from 10 to 23, which is his explanation for why unrelated categories keep converting to recurring billing.

**What this does and does not settle.** It is still arithmetic rather than evidence, a demonstration that the equation is more sensitive to the value terms than to the CPA term, which is true by construction of the equation. It does not show that any business actually moved those numbers, and the CAC-side scenario is deliberately modest (25%) against a value-side scenario that moves three terms at once. Keep the tier at T4 as a model, and note that it converges with the independent lever rankings at [[Marketing Math & Unit Economics#MM-159|MM-159]] and [[Marketing Math & Unit Economics#MM-094|MM-094]], both of which also put the value terms above media efficiency.
Sources added: Ben Heath, The REAL Secret to Winning with Meta Ads, 2026-11-11""")

wr(MM, t)
print("MM ok")

# ------------------------------------------------------------ Learning & Signal
LS = "Learning & Signal.md"
t = rd(LS)
t = amend(
    t,
    "### LS-045 \u00b7 Send the qualified lead back to Meta as a PURCHASE event"
    if "### LS-045 \u00b7 Send the qualified lead back" in t
    else "### LS-045 - Send the qualified lead back to Meta as a PURCHASE event",
    """**The missing prerequisite finally gets a formula, 2026-11-11, and the same sentence states it two incompatible ways.** This claim's first prerequisite has been that you must know average lead value before you can assign it. Charley T now supplies the derivation: create a custom conversion called qualified lead and set its value from the stage of the funnel where the close rate is actually known. **The correct form is sale price x close rate** ("that value is simply sales price times close rate"), which is the same quantity Ben Heath derives independently as the acceptable cost per lead on the same day ([[Marketing Math & Unit Economics#MM-068|MM-068]]), and two operators arriving at one formula from opposite directions, one pricing the event and one pricing the bid ceiling, is the reason to trust the form.

**Carry the error with it, because it is a factor of twenty-five on a 20% close rate.** In the next breath he says "divide the sale price by that close rate", which inverts it and would value a $1,000 sale at a 20% close rate at $5,000 instead of $200. A sale price divided by a close rate is a revenue-per-lead-cohort figure, not a per-lead value, and feeding it to Meta would overstate every conversion value in the account. **Use sale price x close rate. Anyone quoting the divide version from this transcript is quoting a slip.** It is one more instance of the pattern recorded at [[Scaling Models#SC-148|SC-148]], where this operator's stated figures fail internal arithmetic about half the time, so check the arithmetic on anything numeric from this source before acting.
Sources added: Professor Charley T, Copy this 3-Part Meta Ads Strategy, It'll Blow Up your Business, 2026-11-11""")
wr(LS, t)
print("LS ok")

# ------------------------------------------------------------- Creative Science
CR = "Creative Science.md"
t = rd(CR)
t = amend(
    t,
    "### CR-162 \u00b7 Per-creative spend inside a flexible ad IS now visible under Breakdown"
    if "### CR-162 \u00b7 Per-creative spend inside a flexible ad" in t
    else "### CR-162 - Per-creative spend inside a flexible ad IS now visible under Breakdown",
    """**The operator whose objection this claim corrected restated the obsolete version on 2026-11-11, after the correction, and defended it as intentional:** "You'll never see an itemized breakdown for each permutation. And that's not a bug. It's a feature." Read precisely, half of that is still true and half is not. There is still no readout crossing a primary text with a headline, so the COPY half of a 3-2-2 remains unmeasurable and his paired-322 workaround is still the only route to it. Per-MEDIA spend is visible, so the blanket "never" is wrong as stated. The distinction matters whenever this claim is quoted to decide whether a flexible ad can be read: ask which half of the unit is in question before answering. Source added 2026-11-12, as a dated restatement rather than new evidence.""")
wr(CR, t)
print("CR ok")
