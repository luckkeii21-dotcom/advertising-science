# -*- coding: utf-8 -*-
"""Merge pass for the 2026-09-05 research run: amendments to existing claims."""
import io, os

SCI = os.path.join(
    "E:\\claude code marketing skill",
    "Obsidian God-level Marketing Vault", "God-level Marketing", "wiki", "science")


def amend(fn, tag, body, add_source=None, touched="2026-09-05"):
    path = os.path.join(SCI, fn)
    lines = io.open(path, encoding="utf-8").read().split("\n")
    s = None
    for i, l in enumerate(lines):
        if l.startswith("### " + tag + " "):
            s = i
            break
    assert s is not None, (fn, tag)
    e = len(lines)
    for j in range(s + 1, len(lines)):
        if lines[j].startswith("### "):
            e = j
            break
    blk = lines[s:e]
    si = max(k for k, l in enumerate(blk) if l.startswith("Sources:"))
    ti = max(k for k, l in enumerate(blk) if l.startswith("Last touched:"))
    if add_source:
        blk[si] = blk[si].rstrip() + "; " + add_source
    blk[ti] = "Last touched: " + touched
    blk = blk[:si] + body.split("\n") + [""] + blk[si:]
    io.open(path, "w", encoding="utf-8", newline="\n").write(
        "\n".join(lines[:s] + blk + lines[e:]))
    print("amended", fn, tag)


MM = "Marketing Math & Unit Economics.md"

amend(MM, "MM-074", """**The earliest statement of this thesis on the roster, and it adds the timing mechanism the entries above do not carry.** Recorded 2025-01-23, fourteen months before the two sources previously on this claim. His model: $10,000 of stock plus $5,000 of ads returns $20,000 at a 2x price-to-cost multiple and a 4x efficiency ratio, on a $15,000 founding injection and a roughly 60-day cycle. Cycle two buys $14,000 of stock, spends $7,000 on ads and ends at $27,000 of cash. All of that looks healthy.

**Then he moves the purchase order to when it actually has to be placed, which is roughly 30 days BEFORE the current cycle's revenue lands, because otherwise you stock out while the factory runs.** The same point in the cycle now holds $20,000 less $14,000 = **$6,000**, and the next $7,000 of advertising has to come out of that $6,000. **The business is short before a single operating expense is counted, and the steady-state bank balance is $6,000 against the $15,000 that was put in.** Push the efficiency ratio down to the 2x a new brand without product-market fit actually achieves and the ad spend needed to move the same stock becomes $14,000, at which point there is no money left at all. Every figure recomputes exactly as stated.

**The financing ladder, which explains why the debt in the paragraph above is so expensive.** A company loan requires a full financial year of statements to satisfy a lender, which a first-year brand does not have, so the realistic instrument is a merchant cash advance at a stated **35% to 350%**. (The company-loan range is garbled in the auto-transcript as "17 to 16%" and is not usable; the merchant cash advance figure is clean.) His established-client case: a target of **$750,000 over the 60-day November-December window at a 3x price-to-cost multiple requires about $250,000 of stock**, financed at roughly 20%, which is **about $4,200 a month** and **$8,000 to $12,000** over the 60 to 90 days it takes to pay down. At a 20% to 25% net margin that is a good trade, **and only if the revenue target is near-certain.** He names both failure branches himself: land at $400,000 instead and roughly $100,000 of the loan cannot be paid down, or hit the $750,000 but at a 2.1x efficiency ratio instead of 4x, so the free cash flow that was meant to clear the loan went back into the next purchase order.

**The consequence he draws is aimed at agencies, and it is why this sits in our codex rather than in a finance note: an aggressive growth projection is a request that the client take on debt.** The client rarely says so out loud. Our own version of the same failure is already recorded above from his 2026 material, where an agency ramps spend and the client quietly finances the inventory behind it.

His closing line is the cleanest statement of the mechanism anywhere in this claim: **the cash conversion cycle does not start at the first dollar of ad spend, it starts at the first dollar of inventory purchase.** Read alongside [[Marketing Math & Unit Economics#MM-189|MM-189]], which says advertising sits outside the accounting formula and lengthens the real cycle. Those are the two ends of the same clock. Illustrative model plus one asserted client case, no documents shown.""",
      add_source="Blue Sense Digital, Why eCommerce Is So Difficult (Deep Dive), 2025-01-23")

amend(MM, "MM-065", """**The account-level consequence, from the dedicated episode on this, and it is the number that makes the claim worth enforcing.** Baseline month: $100,000 of revenue, cost of goods assumed at 30% = $30,000, shipping and fulfilment at order level = $10,000, transaction fees at 3% = $3,000, so gross profit is $57,000 and, after $20,000 of ad spend, contribution is **$37,000**. Now discount 30%: the $100 product at $30 cost was making $70 a unit and now makes $40, and holding revenue flat at $100,000 means moving far more units to get there.

With cost of goods actually tagged, Shopify returns **$55,000** rather than the assumed $30,000, fulfilment rises with the order count to $15,000, transaction fees stay at $3,000 because revenue did not move, gross profit falls to $27,000 and contribution lands at **$7,000**. **With the static 30% assumption the model returns $37,000 for that same month. The true figure is $7,000, so the model overstates contribution by 81%.** That is exactly the "80% or 90% lower" he describes, and it is the gap that appears when the accountant's profit and loss statement arrives two months later and contradicts the agency's November report. Every figure in the chain recomputes.

Two more things ship with it. **Accuracy band:** tagged cost of goods will still not be dollar-for-dollar with the eventual statement, but he puts it within **5% to 10%**, against being wrong by 80% to 90% on the assumption. **The alternative is not practical:** recomputing a fresh cost-of-goods percentage for a promotional month requires forecasting sell-through at individual product and bundle level, which he says almost nobody can do and which introduces its own error.

**The operating payoff is a live KPI, not a reporting improvement.** With cost of goods tagged you can pull gross margin for yesterday, see it compressed by 20%, and move the efficiency target from 4 to 6 or 7 the same day, so the marketing goal tracks the profit the discount actually leaves behind. That converts this from a bookkeeping chore into the input that sets the number the media team is held to.""",
      add_source="Blue Sense Digital, Why You Need To Have COGS Tagged Up In Shopify, 2025-09-03")

amend(MM, "MM-192", """**The dedicated episode behind trap one, recorded eight days before the source above, and it adds the reason the shipping line has to be added back.** Shopify treats shipping collected the way it treats tax, as a flow-through that cancels against shipping paid. **It does not cancel: "shipping collected never equals shipping paid, I've never seen it before."** There is always a differential, and that differential is either profit or loss on fulfilment. Netting it out of the revenue figure hides which one it is. So the figure to use is net sales **plus** shipping charges, and the shipping line is then read on its own to see whether the store makes or loses money moving product.

**The diagnostic he attaches is the practical use of the whole claim.** When contribution margin, the efficiency ratio and return on ad spend refuse to reconcile with each other, the cause is almost always that each was computed on a different revenue figure. Standardise the numerator across all three and they triangulate. Worth running before anyone investigates a performance question that is actually an arithmetic question.""",
      add_source="Blue Sense Digital, Why Tax In Shopify Is Ruining Your Reporting & Measurement, 2025-01-30")

amend(MM, "MM-018", """**Two problems with the numbers in this claim, both found 2026-09-05, and neither changes the rule's direction.**

**One, the "3x" is written in the keystone convention and the body mislabels it.** The heading says selling price of at least 3x cost of goods, which is unambiguous. The worked example then calls $10 landed cost sold at $50 a "5x markup". Five is the price-to-cost ratio; by the actual markup formula, (price less cost) over cost, that product is 4x. **Anyone applying the formal definition to the "3x" would impose a floor of price = 4x cost, which is a materially stricter rule than intended.** Read every multiple in this claim as price divided by cost. The two competing definitions and the conversion formulas are at [[Marketing Math & Unit Economics#MM-210|MM-210]].

**Two, the operator behind the floor states it at two different numbers three months apart.** On 2026-04-24 he gives it as at least **$30** of gross margin per unit and 3x cost of goods, with the same shoe-box and passionate-market conditions attached. On 2026-07-30, the source already on this claim, it is **$25**. Same speaker, same rule, same structure, different absolute threshold, and he never acknowledges the change. Treat the floor as "roughly $25 to $30 of gross margin per unit" rather than as a precise number, because it is a rule of thumb that moves.""",
      add_source="Mark Builds Brands, how to print money with AI (before NPCs ruin it), 2026-04-24")

print("MM amendments done")
