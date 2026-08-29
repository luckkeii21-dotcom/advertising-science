# -*- coding: utf-8 -*-
"""Codex amendments for the 2026-08-28 research pass."""
import pathlib, re

S = pathlib.Path(r'Obsidian God-level Marketing Vault/God-level Marketing/wiki/science')
TODAY = '2026-08-28'


def read(fn):
    return (S / fn).read_text(encoding='utf-8')


def write(fn, t):
    (S / fn).write_text(t, encoding='utf-8')


def amend(fn, cid, add_body=None, add_source=None, new_status=None):
    """Insert a paragraph into an existing claim, extend Sources, bump Last touched."""
    lines = read(fn).split('\n')
    start = None
    for i, l in enumerate(lines):
        if re.match(r'^### ' + re.escape(cid) + r'[ ·\-]', l):
            start = i
            break
    if start is None:
        raise SystemExit('claim not found: ' + cid + ' in ' + fn)
    end = len(lines)
    for j in range(start + 1, len(lines)):
        if lines[j].startswith('### '):
            end = j
            break
    blk = lines[start:end]
    si = li = None
    for k, l in enumerate(blk):
        if l.startswith('Sources:'):
            si = k
        if l.startswith('Last touched:'):
            li = k
    if si is None or li is None:
        raise SystemExit('no Sources/Last touched in ' + cid)
    if new_status is not None:
        blk[1] = re.sub(r'Status: \w+', 'Status: ' + new_status, blk[1])
    if add_body:
        blk[si:si] = [add_body.strip()]
        si += 1
        li += 1
    if add_source:
        blk[si] = blk[si].rstrip() + '; ' + add_source
    blk[li] = 'Last touched: ' + TODAY
    lines[start:end] = blk
    write(fn, '\n'.join(lines))
    print('amended', cid)


amend('Creative Science.md', 'CR-097', add_body=(
    "**Restated 2026-08-27 with the mechanism attached and one exception, which is the part that is new.** "
    "The spend floor is now stated as a signal-volume argument rather than a preference: below 1x cost per call "
    "\"it's going to be really hard for you to optimize the ads for qualified calls because you're not getting any. "
    "So, Facebook has a harder time optimizing\", which is why the $50 to $100/day tier routes to DM ads instead. "
    "**The exception he names goes the other way and is worth carrying:** on the application or VSL funnel he will "
    "sometimes optimise for leads or applications rather than scheduled calls specifically to push more events through "
    "the pixel, and reports that this \"will generally give us better quality than the DM ads\". So the funnel choice "
    "and the optimisation event are two decisions, not one, and running the cheaper event on the more expensive funnel "
    "is a live option. He also fixes the B2B boundary at six figures of client revenue, \"anything under six figures is "
    "B2C\", because a sub-six-figure buyer \"still ha[s] to run it by their spouse\". The 1x-cost-per-call floor and the "
    "$200 to $500 B2B call cost now appear on two dates, so treat the floor as his standing rule rather than one "
    "video's framing."),
    add_source='Dr. Matt Shiver, The Right Funnel for Every B2B Ad Budget, 2026-08-27')

amend('Creative Science.md', 'CR-186', add_body=(
    "**A THIRD figure from the same operator, found 2026-08-28, and it sits between the other two: \"a regular hit rate "
    "for an e-commerce brand sits at about 15%\", which he immediately restates as \"you have to go and launch seven "
    "ads ... and only one of these will work and actually be able to scale.\"** *Arithmetic check: 1 in 7 is 14.3%, so "
    "for once the sentence is internally consistent.* He caps it in the same breath, \"there's an argument that you are "
    "really capped at maybe 20% as your highest hit rate.\"\n"
    "**A FOURTH, implied rather than stated, and it is an order of magnitude lower.** Planning a US launch he describes "
    "testing 130 to 160 ads a month through Q1 and coming out of three months with \"like seven really high performing "
    "winners\", which is roughly 1.5% of about 480 ads. He never reconciles it with 15%.\n"
    "**The reconciliation is the finding, and it is definitional: the bar moves.** 15% is ads that work. 5 to 10% is ads "
    "that hold spend. 1.5% is ads that scale in a market with no brand presence behind them. **Four numbers from one "
    "operator spanning 1.5% to 15%, and the spread is mostly the definition of \"winner\" rather than a disagreement "
    "about accounts.** Before quoting any hit rate, state which of the three bars it is measured at. The instruction "
    "not to average now covers four figures instead of two."),
    add_source=('Blue Sense Digital, The Two Highest ROI Activities for an eCommerce Founder, 2025-01-29; '
                'Blue Sense Digital, Why eCommerce Brands Fail To Launch Into The USA, 2025-11-21'))

amend('Attribution & Incrementality.md', 'AT-038', add_body=(
    "**Stated as a standing audit step on 2025-09-18, which makes it his default rather than a finding from two audits, "
    "and it supplies the platform boundary that was missing.** The procedure in his words: take MER or acquisition MER "
    "off the P&L, say a 3, then \"we can go to an attribution setting breakdown and then we can start looking at well "
    "what attribution setting correlates to the three\", and if Meta's headline reads 9 against a business 3, \"it's "
    "wrong\". Once a setting reconciles, that setting becomes the one the account is read on.\n"
    "**The boundary: this does not work on Google.** \"On Google, it's a little bit tougher ... it's not as simple as "
    "hey, you can just do an attribution setting change and you get clarity. It becomes a little bit more important in "
    "terms of how you structure the account. You need to go a little bit more into campaign by campaign to get more "
    "confidence that the numbers are actually linking up.\" **So the cheap one-column fix is Meta-only, and the Google "
    "equivalent is a structural separation of cold from warm, which is expensive.**\n"
    "**The second use of the same reconciliation is a validation loop rather than a calibration, and it is the more "
    "useful half for us.** After any account change, read both surfaces: \"when we went and increased creative volume in "
    "the account from 50 ads to 100 ads ... the platform looks better ... but can we actually go over to the P&L and see "
    "an improvement as well?\" The case worth knowing is the disagreement, where platform ROAS falls, the P&L improves, "
    "and nothing else changed. He reads that as colder reach converting elsewhere later, which is the signature proposed "
    "at [[Attribution & Incrementality#AT-049|AT-049]]. **He also names the three numbers a client should hold an agency "
    "to: MER or aMER, contribution margin 3 (gross profit minus ad spend), and new-customer CAC.** Third-party "
    "attribution tools \"add more confusion than help\"; third-party P&L aggregators he rates as useful."),
    add_source="Blue Sense Digital, An Agency Doesn't Create Business Growth, 2025-09-18")

amend('Attribution & Incrementality.md', 'AT-009', add_body=(
    "**Second named instance, added 2026-08-28, and it is the cleanest gap on file because both numbers describe the "
    "same campaign over the same 30 days.** Blue Sense launched a 9-figure Australian fashion brand into Spain for the "
    "first time. Reported ROAS \"was a 20. It was a 30 even\". The incremental read on the same launch was **5.6**. His "
    "stated cause is the one that generalises: the brand already had retail stores, organic revenue and awareness in "
    "Spain, \"so when you launch onto the platforms, you're immediately going to have a ton of over-attribution just due "
    "to the fact of the existing brand presence.\"\n"
    "**The rule this yields is sharper than \"a 20 ROAS is not real\": the size of the attribution error tracks how much "
    "brand presence already exists in the market being measured.** A new geography with no presence over-attributes "
    "least, and the home market over-attributes most. That is the same mechanism the same operator uses to explain why "
    "home-market winners do not travel, banked at [[Creative Science#CR-200|CR-200]], so one cause is now doing two "
    "jobs.\n"
    "**Guards.** No incrementality output shown, no holdout design described for Spain beyond the words \"incremental "
    "ROI\", and 20 against 30 is quoted loosely inside one sentence. The 5.6 is stated once, in a case-study video that "
    "closes on a free-audit call to action."),
    add_source="Blue Sense Digital, How We Accelerated KOOKAI Australia's Growth Rate By 100%, 2025-04-22")

amend('Scaling Models.md', 'SC-058', add_body=(
    "**The largest single allocation figure on this question, added 2026-08-28, and it refuses the seasonal framing "
    "above.** Nick Theriot, agency spending \"over $5 million a month\" across ecommerce and lead gen: **\"based off "
    "last 30 days ... 97% of our accounts use a CBO campaign.\"** He restates it as \"95, 98% of the time\" later in the "
    "same video, so read it as roughly 95 to 98 rather than as a precise 97.\n"
    "**His two triggers for reaching for ABO are the same symptom, and it is our symptom.** New ads receiving literally "
    "zero spend, not merely low spend: \"when they're earning purely zero spend, this is when I'm inclined to want to go "
    "and set up that ABO campaign.\" Low-but-nonzero delivery he explicitly accepts, \"50, 75, 90, $48, like they're "
    "still getting some spend ... I'm okay with that. That's enough for me.\" Second trigger: accounts spending tens of "
    "thousands a day where nothing new is funded inside the main CBO. **He gives three incompatible frequencies for the "
    "exception inside one 20-minute video, 2 to 5%, 10%, and 20%. Quote the exception, never the rate.**\n"
    "**What he uses ABO for is diagnosis, not performance.** The stated purpose is confidence that a creative was "
    "genuinely bad rather than merely unfunded, and he reports the answer usually comes back against him: \"nine times "
    "out of ten we're wrong and Facebook still is correct with its choice.\" He also prices the ABO route: forced "
    "testing consumes a fixed 10 to 20% of daily budget, and a winner found in ABO takes an extra 3 to 4 days to reach "
    "the scaling campaign, against a CBO winner that took $6,300 of spend in 4 days and moved that campaign's cost per "
    "purchase from $57 to $46.\n"
    "**Read this against [[Meta Delivery & Andromeda#MD-137|MD-137]] before importing it.** His accounts run $5,000 a "
    "day through a single CBO. Every client on our book is under $30,000 a MONTH, where the same claim says roughly one "
    "ad gets funded. **The 97% is an argument for CBO at his spend, and the zero-spend trigger he names as the rare "
    "exception is the everyday condition at ours.**"),
    add_source='Nick Theriot, ABO vs CBO in 2026: Which One Should You Actually Use?, 2026-08-28')

amend('Scaling Models.md', 'SC-049', add_body=(
    "**The quadrant tool named above is now shipped and walked through on screen, 2026-02-14, across three real "
    "accounts. The rule survives. The confidence numbers do not.** The axes are CPA and gross profit per transaction, "
    "each against the account average, giving scalers (low CPA, high GPT), keepers (high CPA, high GPT), **\"fake "
    "wins\" (low CPA, low GPT)** and liabilities (high CPA, low GPT). **His asymmetry argument for protecting the GPT "
    "axis is the part worth keeping:** you can almost always work a CPA down through the environment, but you cannot "
    "make one ad produce higher-AOV customers than the ads beside it in the same ad set pointing at the same landing "
    "page, so AOV is the harder-won axis.\n"
    "**Account one, shown: 75 ads, $144,000 spend in a month, 1,394 purchases, $190,000 conversion value, CPA $103, AOV "
    "$135, gross profit per transaction $31.69.** *Arithmetic check, and it passes to the cent: 144,000/1,394 = $103.30, "
    "190,000/1,394 = $136.30, and $31.69 is consistent with CPA $103.31 against AOV $135.00.* At the 10% setting the "
    "tool cuts 41 of 75 ads, 18% of spend, for a projected CPA improvement of about 40 cents. **He calls that \"not "
    "needle-moving\" himself and argues the real return is a simpler account.**\n"
    "**⚠ Account three is the counter-example and it is the most valuable thing in the video.** 46 ads, CPA $314, "
    "GPT $206. Pruning hard to 8 ads cut CPA from $314 to $263 **and cut gross profit per transaction from $206 to "
    "$131.** His diagnosis is that the cull removed the high-AOV ads along with the inefficient ones. He then walks the "
    "setting back down and finds the break point at 30%. **So the two-axis rule is directionally right and the "
    "aggression is account-specific, with AOV collapse as the failure mode. Prune in steps and watch GPT, not CPA.**\n"
    "**The supporting observation is the strongest internal evidence for the whole thesis: after pruning, ROAS barely "
    "moves (1.94 to 2.21 becomes 2.08 to 2.20) while profit per sale nearly doubles.** That is what \"optimising to "
    "ROAS optimises for the ad closest to converting, not the ad that makes the most money\" looks like inside one "
    "account.\n"
    "**Guards, and they are real.** The confidence percentages, 90% at the 10% setting falling to 70% at 30%, sit behind "
    "\"very advanced mathematics that we don't need to get into today\", with no methodology, no backtest and no "
    "holdout. **Treat the confidence figures as interface decoration.** The tool is his own $39 product. And his "
    "\"profit per transaction\" is AOV minus CPA, which excludes cost of goods and is never flagged as such; on a "
    "physical product at 40% COGS his $200-AOV example leaves $20, not $100. **The RANKING between ads survives that "
    "omission because COGS is roughly common across them. The absolute profit figures do not.**"),
    add_source='Professor Charley T, Academy News #9, 2026-02-14')

amend('Meta Delivery & Andromeda.md', 'MD-137', add_body=(
    "**The same structure stated from the operator side rather than the platform side, added 2026-08-28, and it turns "
    "the claim into a planning model.** Blue Sense: **\"each individual ad unit has a maximum spend threshold that it "
    "can hold profitably\"**, illustrated at $1,000/day for a broad-message ad, $100/day for a narrow one and $40/day "
    "for a weak one, and \"it's the summation of the ad spends that all of these ads can currently hold that gives you "
    "the total ad spend that that ad account should hold whilst maintaining efficiency targets.\"\n"
    "**He then applies the identical ceiling one level up, to products, and that is the part that transfers to a service "
    "business.** A niched product has a spend ceiling no amount of creative volume can break: \"no matter what you do, "
    "whether it's you go on ramp creative testing up to thousands of ads a month, you go and test a bunch of different "
    "angles, you're using five different agencies ... there will be a limit on how much you can spend profitably within "
    "this particular product.\" The only move past it is a second product. He also puts the shape of the underlying "
    "curve on record: efficiency against spend declines logarithmically, and the job is to find the spend that maximises "
    "profit contribution and then try to shift the curve right.\n"
    "**Worked illustration with the arithmetic intact:** Australian fashion brands reach high spend by carrying 100-plus "
    "products that turn over every two to three weeks, so a brand at $100,000 a month spends about $3,300 a day, which "
    "across 100 products is about $33 a day each. *He first says $300 per product, corrects himself to $30 on camera, "
    "and the corrected figure is the right one.* He attaches Pareto anyway, 20% of products taking 80% of spend.\n"
    "**Why this matters for our book: the same ceiling is banked one level lower again, at offers, in "
    "[[Scaling Models#SC-151|SC-151]].** Per-ad, per-product and per-offer ceilings are one claim stated three times by "
    "one operator. On a local service client there is no second product to launch, so the horizontal axis is a second "
    "offer."),
    add_source='Blue Sense Digital, The Two Highest ROI Activities for an eCommerce Founder, 2025-01-29')

print('amendments done')
