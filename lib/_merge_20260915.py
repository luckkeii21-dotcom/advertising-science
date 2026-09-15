# -*- coding: utf-8 -*-
"""2026-09-15 research merge. 3 new claims, 7 amendments."""
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

SCI = Path(r"E:\claude code marketing skill\Obsidian God-level Marketing Vault"
           r"\God-level Marketing\wiki\science")
CT = "Professor Charley T, The NEW BEST Way To Scale Facebook Ads, 2026-09-14"
NT = ("Nick Theriot, GPT-6 Astra Is Overhyped for Facebook Ads Except for "
      "These 3 Things, 2026-09-14")
TODAY = "2026-09-15"


def amend(fname, cid, body, source=None):
    p = SCI / fname
    txt = p.read_text(encoding="utf-8")
    m = re.search(r"^### " + re.escape(cid) + r" .*?(?=^### |\Z)", txt, re.S | re.M)
    if not m:
        print("MISS", cid)
        return False
    block = m.group(0)
    lines = block.rstrip("\n").splitlines()
    si = next(i for i, l in enumerate(lines) if l.startswith("Sources:"))
    if source and source not in lines[si]:
        lines[si] = lines[si].rstrip() + "; " + source
    for i, l in enumerate(lines):
        if l.startswith("Last touched:"):
            lines[i] = "Last touched: " + TODAY
    new = lines[:si] + [body.strip(), ""] + lines[si:]
    tail = "\n" * (len(block) - len(block.rstrip("\n")))
    p.write_text(txt[:m.start()] + "\n".join(new) + tail + txt[m.end():],
                 encoding="utf-8")
    print("AMENDED", cid)
    return True


def add(fname, claim):
    p = SCI / fname
    txt = p.read_text(encoding="utf-8").rstrip("\n")
    p.write_text(txt + "\n\n" + claim.strip() + "\n", encoding="utf-8")
    print("ADDED", claim.strip().splitlines()[0][:90])


# ---------------- AMENDMENTS ----------------

amend("Scaling Models.md", "SC-078", """
**Restated 2026-09-14 with the distinction that makes it operable: headroom is a GAP, not a score.** Same speaker, same arithmetic, one sharper point. "$45 is not good news by itself. It's not an inherently good CPA. $45 against a $46 target has almost no headroom at all. Same CPA, still profitable, completely different decision." No cost-per-acquisition figure can be judged without the target beside it, so a dashboard showing cost per result with no target column is unreadable for this decision.

**The corollary is the part that changes when you act.** "If you decide to scale when you hit your target, you're already at the ceiling." An account run that way meets the normal, expected efficiency cost of added volume with nothing to absorb it, reads that cost as proof that scaling does not work in its category, and concludes the business has a hard limit. He names the belief directly: the ceiling "isn't a limit on the business. It's a limit created by the way the moves in the ad account are being made." Worth flagging that as stated this is close to unfalsifiable, because any ceiling an operator actually hits can be re-attributed to a missing move. Reasoning with worked arithmetic, no data.
""", CT)

amend("Scaling Models.md", "SC-001", """
**Two additions from the same operator 2026-09-14, and the first turns his 5% figure into a rule.** "My best practice is to never increase by more than half of your headroom." The 5% step this claim already credits to him is that rule applied to a $50 target running at $45: a 10% beat allows a 5% raise. Stated that way the step is a function of the gap rather than a constant, so the same account is allowed a different step in different weeks, and an account running close to its target is allowed almost nothing.

**Second, the conditional rule must not fire daily.** "We do not let it fire every day. We run it two or three times a week. I like Monday, Wednesday, Friday." The stated reason is that a daily conditional collapses into the compounding case, which he prices out loud: 1% a day doubles the budget in 70 days by the rule of 70 and reaches 37.8x in a year, 2% a day doubles every 35 days and takes a $100 daily budget past $137,000 inside a year. That is arithmetic, not evidence, and he calls anything above 1% a day unsustainable for most accounts in the same breath. One equivalence is worth carrying because it collapses the linear-versus-fractional argument at small budgets: starting at $100 a day, adding a flat $10 a day for a year lands at $3,750 and compounding 1% a day lands at $3,780, so at that scale the choice of method barely matters and only the discipline does.

**He also names a volume precondition the earlier entry does not.** The conditional rule reads a trailing 7-day average, so it needs enough transactions to smooth the daily swings. An account whose day-to-day performance is hyperbolic cannot run it and should sit on the flat linear rule instead.
""", CT)

amend("Scaling Models.md", "SC-002", """
**A cheap in-account check for the dip, added 2026-09-14.** Charley T offers a procedure rather than a mechanism, and it costs one report: take the last 30 days, break them down by week, and find the week immediately after a budget increase. "Almost every time you're going to see a drop in performance followed by a recovery if you gave it the time to recover." He says CPM and frequency move in that week too, and reads both as the machine taking on load rather than as damage.

**Read it against the contest above before using it, because it settles half the question and not the other half.** Recovery or no recovery separates the lag position from the ceiling position, which is exactly what is in dispute. Frequency climbing does not separate them, because both positions predict it: the lag position expects wider and colder reach, the ceiling position expects the same warm pool served harder. So run the weekly breakdown to answer "did it come back", and still pull the audience-segment breakdown to answer "where did the money go". Asserted, no curve shown.
""", CT)

amend("Creative Science.md", "CR-042", """
**Restated 2026-09-14 with the reason for launching TWO 322s rather than one, which this entry previously carried as a rule with no logic attached.** "If you only test one ad, you're essentially asking, is this ad good? Yes or no. You learn nothing from that. It's a binary outcome. If you test two, you can understand whether the concept works, and if so, which version works better." The pair are two attempts at the same concept against the same diagnosed problem, differing slightly. The kill rule that follows is the operative half: "if neither works, don't test the concept again. It's not worth pounding into a loss."

**Two construction constraints, one tighter than this entry records.** All three creatives share format AND aspect ratio AND media type, all video or all images. All three sit on one marketing angle, "three images about features and benefits, or three videos that are UGC testimonials", and that holds across both 322s in the pair rather than just inside one. The two headlines must carry substantially different reasons to care and must not be rewordings of one point, and the primary text has to stay in line with the angles the headlines push.

**And the unit of analysis, stated plainly enough to quote.** "The 322 is the ad. It has 12 permutations in it, but you're not testing 12 different ads. You're not trying to find the winning post ID." The question under test is whether the concept solves the diagnosed problem. If one permutation does run away with the budget and the comments he says it will be obvious in the inbox, and only then is it worth taking that post ID and running it as a standalone ad later.
""", CT)

amend("Creative Science.md", "CR-158", """
**Sharpened 2026-09-14 by the same operator, and three of the four additions change how the number is read.**

**Read frequency DAILY, and against the campaign's own baseline.** "I don't care about frequency over weeks or months. We need to look at the day breakdown." There is no absolute number to hold: the campaign's own daily frequency is the axis. "If your campaign is sitting at 1.23 on a daily basis, any ad with a daily frequency lower than 1.23 is higher in the funnel. Any ad with a daily frequency higher than 1.23 is lower in the funnel relative to your baseline." That confirms the caution already on this entry, that the 1.3 to 1.4 figures are one account's axis rather than a benchmark.

**Middle of funnel is rejected as a category.** "I want you to reject the idea that middlefunnel exists. That's old thinking and honestly, it doesn't make any sense." Two positions only, above the line and below it.

**The daily frequency number converts into a share of people, which is what makes a decimal like 1.23 usable.** A frequency of 1.05 means roughly 5% of the people reached saw the ad twice; 1.95 means roughly 95% did.

**The expectation matrix, which is the enforceable form of this claim.** Below-average frequency plus below-average CPM is allowed a worse-than-average cost per result, because that ad is filling the funnel. Above-average frequency plus above-average CPM must return a better-than-average cost per result, "otherwise, it's a bad retargeting ad", on the argument that hammering warm traffic trades reach for closing power and has to be paid for in efficiency. His mechanism for the CPM half: an ad that appeals to strangers buys a cheaper impression because the experience is positive, while "if somebody ignores an ad three times a week, that is objectively a worse experience than complete strangers liking, commenting, and watching." Asserted from account reviews, with no distribution shown behind any cell of the matrix.
""", CT)

amend("Creative Science.md", "CR-130", """
**One structural addition 2026-09-14, same speaker.** Where this entry records the first 125 characters as the hello and everything below as the close, he now specifies what sits at the boundary itself: a complete thought above the fold that earns the click on "see more", then an immediate call to action directly below the fold, then the rest of the argument under that. "You tease, ask for the sale, and then give other reasons to click if somebody doesn't say yes right away." The call to action is placed there for the reader already convinced by the teaser, and the copy under it exists only for the reader who was not. Asserted, never tested.
""", CT)

amend("Creative Science.md", "CR-060", """
**A spend inversion reported 2026-09-14 by one of this claim's own sources, and it complicates the claim without touching its performance argument.** Nick Theriot now states his agency spends "over 12 grand a month paying UGC creators" and "over $20,000 a month on Higgsfield", across almost 30 clients and close to a dozen editors, and says the ratio has flipped: "before it was primarily UGC we're spending money on, less money on AI UGC. Now that table's starting to turn, and I'm okay with that."

**Read it for what it is, because the number is easy to misquote.** This is a PRODUCTION-VOLUME statement, not a performance one. He gives the reason himself, creative volume across a large book, and he is still paying human creators five figures a month in the same sentence. He makes no claim anywhere in this video that AI UGC now outperforms real-creator UGC. The honest amendment is narrower than the dollar figures suggest: at agency scale the cost of producing a unit of AI UGC has fallen far enough that an account will carry more of it than its performance ranking alone would justify, so a high AI share in a live account is evidence about the production budget and not about what works. Numbers recalled on camera with nothing shown.
""", NT)

# ---------------- NEW CLAIMS ----------------

add("Scaling Models.md", """
### SC-159 · The scaling loop is three moves in a fixed order, and the removal move has a spend window: take out the biggest ad under 40% of the budget, never one over it
Tier: T3 · Status: active
Professor Charley T, 2026-09-14, against a claimed lifetime figure of more than a billion dollars across his own brands, his clients and his students. The whole system answers one question every day, and he is explicit that nothing else in the account earns its keep: "Everything you do in your account is getting you to one question. Can I spend more money tomorrow?" Then: "Everything else you do in the ad account is a liability and a complete waste of your time."

**Move one, budget.** If there is headroom, raise the budget and change nothing else. "The worst thing you can do when you've built a system that can handle more load is change the system." Sizing and cadence for this move sit at [[Scaling Models#SC-001|SC-001]] and [[Scaling Models#SC-078|SC-078]].

**Move two, addition by subtraction, and this is the new material.** When there is no headroom the instinct is to launch more ads, and he calls that exactly backwards: first find what is consuming the headroom and remove it. The spend window is the part worth banking, because it is a concrete pair of thresholds nothing else in this file carries. An ad spending **10% or more** of the budget will shift how the campaign allocates across the remaining ads when it is removed. An ad spending **more than 40%** will "completely change how everything works" when it is removed, which is a rebuild rather than a trim. So the target is the **highest-spending ad at or above 10% and below 40%** whose cost per acquisition is above the campaign average and whose gross profit per transaction is below it. That kill criterion is the one already at [[Creative Science#CR-122|CR-122]] and [[Marketing Math & Unit Economics#MM-080|MM-080]]; the contribution here is the spend band it is allowed to operate in.

**Note the asymmetry, because it inverts the usual instinct.** He wants the BIGGEST removable ad, not the smallest. The reasoning is opportunity cost rather than waste: "That ad is soaking up a ton of money so that you can pay more money to buy a worst customer. Every time money goes into that ad, you lose."

**Move three, creative test.** Only when there is nothing left to remove. Direction comes from the funnel read rather than from a creative wishlist, and he allows exactly two diagnoses: either scaling destroys efficiency, which is an upper-funnel problem needing an upper-funnel ad, or there was no efficiency to begin with, which is a lower-funnel problem needing a lower-funnel ad. Grading of that test is at [[Creative Science#CR-244|CR-244]].

**Cadence, and it governs moves two and three as well as the automated budget rule.** Two or three times a week, never daily. "You cannot compound choice on top of choice on top of choice. That leaves us somewhere we cannot possibly plan for." After a removal he waits three days before re-reading whether move one has become available.

Relation to what is already here: [[Scaling Models#SC-004|SC-004]] holds that if you can spend more you do not launch a test, which is moves one and three with nothing between them. The middle move and the 10-to-40 window are new. Asserted from agency and program practice. No account shown, and neither threshold carries a distribution behind it, so treat 10% and 40% as one operator's working rule rather than as measured breakpoints.
Sources: """ + CT + """
Last touched: """ + TODAY + """
""")

add("Creative Science.md", """
### CR-244 · A creative test passes only if the campaign can now take a budget increase, so a test with a good cost per result can still be a failure and an unspent test is still a verdict
Tier: T3 · Status: active
Professor Charley T, 2026-09-14. "Creative testing is not about finding winners, it's about making the team better... Facebook ads is a team sport." The test is graded on what the campaign can now do, never on the test's own row in the dashboard.

**Three outcomes, and the second is the one that changes practice.**
1. The new ads earn spend and the campaign improves enough to allow a budget increase. Raise it and touch nothing else. "You don't turn the test off. You don't move post IDs. You don't mess with it. You already won the game."
2. The new ads earn spend and the campaign still cannot take an increase. "Regardless of what any CPA or ROAS metric says, it's a failure." Turn it off, launch another.
3. The new ads earn no spend. "That is itself a signal", not a null result.

**The caveat on outcome three is specific to lower-funnel tests, and it is what prevents a wrong kill.** A lower-funnel ad can go unspent because the incumbents are good enough that the delivery system never needs it, and the system has no way to know that the result it is currently producing is not good enough for the business. In that case he accepts an ad-set spending minimum, "generally starting around 20%", and re-asks the same question once the ad has actually spent. Compare the 7-day minimum sized at one target cost per acquisition recorded at [[Scaling Models#SC-058|SC-058]], and this vault's own build rule that a floor props up a loser.

**This cuts against reading spend as the quality proxy, and both positions belong to the same author.** [[Creative Science#CR-122|CR-122]] ranks amount spent as the most reliable signal of creative quality; outcome two here is an ad that earned plenty of spend and is killed anyway. The reconciliation available: spend tells you what the delivery system values, and the budget gate tells you whether the business can use what it values. When the two disagree, this claim says the business wins.

**Where the test comes from is not optional either.** The concept is chosen to answer the diagnosis from the funnel read at [[Creative Science#CR-158|CR-158]], and the test is launched only after the removal move at [[Scaling Models#SC-159|SC-159]] has nothing left to take. On placement, the decision rule is one question: can the account afford a second ad set going through learning? If yes, the new ads get their own ad set. If no, they go into the existing ad set beside the incumbents.

Asserted from agency and program practice, no test data shown, and note the definition is circular by construction: a test succeeds when the budget can rise, and the budget rises when the test succeeds. It is useful as a decision rule and it is not a measurement.
Sources: """ + CT + """
Last touched: """ + TODAY + """
""")

add("Learning & Signal.md", """
### LS-079 · A wide average-order-value spread inside one ad set teaches the optimiser to "sell anything", so value homogeneity is part of signal quality
Tier: T3 · Status: active
Professor Charley T, 2026-09-14, reading average order value per ad as a measure of customer quality rather than as revenue. "If we're in an ad set where the AOVs are dramatically different, say one is 65 and another is 100, we're selling dramatically different products to dramatically different people. That means we're not teaching the machine what success actually looks like. We're just saying sell anything."

**The second-order version is the practical trap, and it runs through the dashboard rather than through the delivery system.** An ad can post an excellent cost per acquisition because its average order value is low and the product is an easy sale of no real value to the business. "Maybe an ad has a great CPA because the AOV is really low and it's just a easy sale product that has no real value to us." Rank ads on cost per result alone and that ad wins every week, so the account trains toward the cheapest customer rather than the best one.

**What it implies if it holds.** A purchase event is not one thing when the value behind it varies widely, so an ad set is a value bucket as well as an audience bucket, and a mixed-value ad set degrades the optimisation target without anything in the interface reporting a problem. The instrument is average order value carried as a column beside cost per acquisition and gross profit per transaction, which is the dashboard built at [[Marketing Math & Unit Economics#MM-080|MM-080]], and the profit algebra behind it is [[Marketing Math & Unit Economics#MM-121|MM-121]].

Asserted with illustrative numbers, no account shown and no before-and-after on splitting a mixed-value ad set. The cheap check on any live account: pull average order value at the ad level inside one ad set and look at the spread before trusting that ad set's cost-per-result ranking.
Sources: """ + CT + """
Last touched: """ + TODAY + """
""")
