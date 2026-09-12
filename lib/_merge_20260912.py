# -*- coding: utf-8 -*-
"""2026-09-12 research merge. Two sources read in full:
   1. Meta for Business News, "Performance Spotlight: How Instant Hydration Built
      a System for AI to Scale", 10-11 Sep 2026 (read through the Playwright browser).
   2. Nick Theriot, "We Cut This Brand's Facebook Ads CPA by 75% (Here's How)", 2026-09-11.
"""
from pathlib import Path

SCI = Path(r"E:\claude code marketing skill\Obsidian God-level Marketing Vault\God-level Marketing\wiki\science")


def edit(fname, old, new, count=1):
    p = SCI / fname
    t = p.read_text(encoding="utf-8")
    assert t.count(old) == count, f"{fname}: anchor count {t.count(old)} != {count}\n{old[:120]}"
    p.write_text(t.replace(old, new, count), encoding="utf-8")
    print("edited", fname)


def append(fname, block):
    p = SCI / fname
    t = p.read_text(encoding="utf-8").rstrip("\n")
    p.write_text(t + "\n\n" + block.strip("\n") + "\n", encoding="utf-8")
    print("appended", fname)


# ---------------------------------------------------------------- AT-035 amend
AT035_SRC = "Sources: Andrew Faris, 2026 Meta Performance Marketing Summit Recap, 2026-05-20; Blue Sense Digital, How to Scale an eCommerce Brand Profitably in 2026 The Full System, 2026-06-15;"

AT035_ADD = """**A FOURTH ACCOUNT ARRIVED 2026-09-12, and this one is from Meta.** Every position above is a practitioner reading Meta's product back to itself, and this claim has recorded since 2026-08-20 that no Meta text is quoted anywhere in it. Meta's own prose now exists, in a business-news case study rather than in documentation: incremental attribution optimization **"shifts delivery toward users the platform predicts wouldn't have visited otherwise."**

**What that one sentence settles and what it does not.** It settles the verb. Meta says *predicts*, which is a model scoring users, and a model scoring users is not a holdout running on your account. That is direct evidence against Position B, the permanent 10% holdout, and it sits comfortably with Position A, a factor derived from lift experiments run elsewhere. It settles nothing about what trained the prediction, over whose data, or how often it is refit, and a marketing case study is not documentation, so the mechanism stays undocumented and this claim stays contested. **Note also the outcome the sentence names: a VISIT, not a purchase.** Every practitioner account above discusses the setting as a conversion instrument. Meta's own sentence describes it steering toward site visits.
"""

edit("Attribution & Incrementality.md", AT035_SRC, AT035_ADD + AT035_SRC)

# ---------------------------------------------------------------- AT-117 new
append("Attribution & Incrementality.md", """
### AT-117 · Meta published a 35% net-new-visits gain from switching to incremental attribution, and the validator it names is a multi-touch attribution tool, which cannot validate incrementality
Tier: T1 for what Meta published, T3 for the figure · Status: active
Meta for Business News, 10-11 September 2026, Instant Hydration, an electrolyte brand that launched mid-2024 and reached what Meta calls "significant monthly Meta spend" inside 18 months. The advertiser is Kevin Cooper, Founding Partner and VP of Paid Acquisition, quoted by name.

**The claim, verbatim.** "We could have the exact same ads in a conversion campaign with 7-day click, 1-day view. We can have the exact same ads in incremental attribution. And we'll see about 35% higher net-new visits." Meta's own framing adds "a lift validated by their third-party MTA tool."

**Run the find-the-word test from [[Meta Delivery & Andromeda#MD-153|MD-153]] and this fails it in a way that page did not.** There the split was between numbers that said *incremental* and numbers that said *increase*. Here the word *incremental* is present and it is the NAME OF THE META SETTING, not a description of a method. The design behind the number is a before-and-after on the same ads with the optimization option changed. No control group appears anywhere in the post.

**The validator makes it weaker rather than stronger, and this is the part to carry.** Multi-touch attribution assigns credit across touchpoints a converter actually had. It observes only exposed users, it has no unexposed cell, and it therefore cannot answer whether the visit would have happened anyway. **An MTA tool agreeing with a platform column is two models built on the same exposed population agreeing, which is not validation.** Anyone handed this figure by a Meta rep should ask for the holdout, and there is not one.

**Three further limits.** The outcome is SITE VISITS, not purchases, revenue or new customers, and the whole argument for the setting at [[Attribution & Incrementality#AT-003|AT-003]] is that the read-out has to be store-level new-customer revenue. No absolute spend, no window length and no test dates are published. And the account runs Advantage+ audience and placements everywhere with only a lifecycle exclusion of existing customers, so "net-new" here is bounded by that exclusion rather than by any measurement.

**Why bank it at all.** It is the first advertiser-side effect size Meta itself has printed for incremental attribution since the roughly 27% new-customer-revenue figure recalled at [[Attribution & Incrementality#AT-006|AT-006]], and it is directionally consistent with the 38% at [[Attribution & Incrementality#AT-002|AT-002]] from an independent operator on DTC-only brands. Instant Hydration is DTC pushing into retail, which is exactly the boundary AT-002 says the gain shrinks at. Treat the convergence as a reason to run our own switch test, never as two confirmations of one number.
Sources: Meta for Business News, Performance Spotlight: How Instant Hydration Built a System for AI to Scale, 2026-09-10 (listing card dates it 10 September, the post byline reads 11 Sep 2026; read 2026-09-12 through the browser after a plain fetch returned HTTP 400 on six routes)
Last touched: 2026-09-12
""")

# ---------------------------------------------------------------- CR-124 amend
CR124_SRC = "Added sources: Fraser Cottrell, Copy This NEW Meta Ads Strategy Post Andromeda, 2026-02-01;"

CR124_ADD = """**A REVIVAL LEVER THAT TOUCHES NO CREATIVE, 2026-09-12, and it changes the shape of the open question.** Every candidate above moves something inside the asset: a recut, a fresh hook, a new person on camera. Instant Hydration's operator claims a fatigued asset came back by changing the OPTIMIZATION SETTING and nothing else: "We found that by repurposing that content into incremental attribution campaigns, they can come back to life." Full detail, and the reasons to distrust it, at [[Creative Science#CR-232|CR-232]].

**The consequence here is diagnostic.** If an asset that took no spend under standard attribution takes spend under a different optimization option, the asset was never fatigued in the creative sense. The delivery system stopped selecting it. That is the same distinction [[Creative Science#CR-147|CR-147]] reaches from the landing-page side, where a matching lander revived ads that took no spend. **Before paying for a reshoot on a dead winner, change what the ad set optimizes toward and see whether the asset moves.** It is a free test and nobody in this corpus had proposed it.
"""

edit("Creative Science.md", CR124_SRC, CR124_ADD + CR124_SRC)

# ---------------------------------------------------------------- CR-068 amend
CR068_SRC = "Two operating facts that decide whether any of the above holds, both from Matt Shiver on 2026-06-30, both shown on screen."

CR068_ADD = """**A sixth position, 2026-09-12, and it is the first one scoped by AD TYPE rather than by enhancement type.** Every position above sorts the enhancement menu. Instant Hydration sorts the ad book instead: enhancements run on brand-owned ads and are held off on whitelisted creator ads specifically. The stated reason is not performance. "That's the only manual way we intervene. We just want to make sure things stay on brand", and the concrete risk named is a creator's handle appearing on an asset the creator did not make.

**That is a different argument from the other five, and it is the one most likely to survive a test showing enhancements help.** A brand can accept a small delivery cost on the slice of the account where a third party's name is attached, because the downside there is a creator relationship rather than a CPA. Our own book runs partnership and whitelisted ads, so the rule transfers directly: **audit the enhancement toggles on creator-handle ads separately from the rest of the account.** Asserted by the advertiser in a Meta-published case study, nothing shown.

"""

edit("Creative Science.md", CR068_SRC, CR068_ADD + CR068_SRC)

# ---------------------------------------------------------------- CR-115 amend
CR115_SRC = "Sources: Ben Heath, Learn 97% of Meta Ads in Under 29 Minutes, 2026-08-18;"

CR115_ADD = """**Where the brief's content comes from, 2026-09-12, and it is a method rather than a rule.** The bullet-points-not-a-script rule above says what a brief must not be and leaves open where its subject comes from. Instant Hydration derives it from the creator's own back catalogue: analyse the creator's organic posts with AI, surface the themes their audience responds to most, then build the brief on the overlap between those themes and the product. **The named case is the whole argument.** The analysis surfaced a health condition the creator posted about often, one that electrolytes can directly help; the partnership content was reframed around it and the advertiser says it unlocked significant scale.

**Why this is worth copying even with no number attached.** It resolves the tension the rule above creates. A loose brief protects authenticity and gives up control of the message; this method keeps the brief loose on delivery while choosing the SUBJECT from evidence about that specific audience. It is also cheap, because the input is public organic content. **What it does not give you is a hit rate**, and one anecdote inside a vendor case study is the entire evidence base. Run it as a briefing default across several creators before treating it as better than picking the angle yourself.
"""

edit("Creative Science.md", CR115_SRC, CR115_ADD + CR115_SRC)

print("phase 1 done")
