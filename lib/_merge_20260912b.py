# -*- coding: utf-8 -*-
"""2026-09-12 research merge, phase 2: CR-115 amend (unique anchor) + new claims."""
from pathlib import Path

SCI = Path(r"E:\claude code marketing skill\Obsidian God-level Marketing Vault\God-level Marketing\wiki\science")


def edit(fname, old, new, count=1):
    p = SCI / fname
    t = p.read_text(encoding="utf-8")
    assert t.count(old) == count, f"{fname}: anchor count {t.count(old)} != {count}"
    p.write_text(t.replace(old, new, count), encoding="utf-8")
    print("edited", fname)


def append(fname, block):
    p = SCI / fname
    t = p.read_text(encoding="utf-8").rstrip("\n")
    p.write_text(t + "\n\n" + block.strip("\n") + "\n", encoding="utf-8")
    print("appended", fname)


# ---------------------------------------------------------------- CR-115 amend
CR115_SRC = ("Sources: Ben Heath, Learn 97% of Meta Ads in Under 29 Minutes, 2026-08-18; "
             "Ben Heath, Copy This Meta Ads Testing Strategy for Better Results, 2026-03-03; "
             "Professor Charley T, The BEST NEW Way to Run Facebook Ads in 2026 (Andromeda 2.0), 2026-06-13")

CR115_ADD = """**Where the brief's content comes from, 2026-09-12, and it is a method rather than a rule.** The bullet-points-not-a-script rule above says what a brief must not be and leaves open where its subject comes from. Instant Hydration derives it from the creator's own back catalogue: analyse the creator's organic posts with AI, surface the themes their audience responds to most, then build the brief on the overlap between those themes and the product. **The named case is the whole argument.** The analysis surfaced a health condition the creator posted about often, one that electrolytes can directly help; the partnership content was reframed around it and the advertiser says it unlocked significant scale.

**Why this is worth copying even with no number attached.** It resolves the tension the rule above creates. A loose brief protects authenticity and gives up control of the message; this method keeps the brief loose on delivery while choosing the SUBJECT from evidence about that specific audience. It is also cheap, because the input is public organic content. **What it does not give you is a hit rate**, and one anecdote inside a vendor case study is the entire evidence base. Run it as a briefing default across several creators before treating it as better than picking the angle yourself.
"""

edit("Creative Science.md", CR115_SRC,
     CR115_ADD + CR115_SRC + "; Meta for Business News, Performance Spotlight: How Instant Hydration Built a System for AI to Scale, 2026-09-10")

# ---------------------------------------------------------------- CR-232, CR-233 new
append("Creative Science.md", """
### CR-232 · A fatigued asset was claimed back to life by changing the optimization setting and nothing else, which makes "fatigue" two different diagnoses that look identical in Ads Manager
Tier: T3 · Status: active
Instant Hydration, in a Meta-published case study, 10-11 September 2026. The advertiser's words: "We found that by repurposing that content into incremental attribution campaigns, they can come back to life", about creative the team "thought had burned out."

**Nothing is shown.** No asset, no spend curve, no before and after, no count of how many assets this was tried on, and the source is a vendor page selling the setting that supposedly did it. As evidence for the setting it is worth very little. **As a hypothesis about what fatigue IS, it is the most useful thing this codex has banked on the question in a month**, because it separates two states that produce the same Ads Manager row.

**The two states.** Either the audience has genuinely seen the asset and stopped responding, which is creative fatigue and only new creative fixes it. Or the delivery system stopped selecting the asset against the objective it is being scored on, which is a selection effect and a different objective can reverse it. Both look like an ad whose spend decayed to nothing. Only the second one is free to test.

**The test, and it costs one duplicate.** Take an asset the account has written off, run it in an ad set optimizing on a different setting, and watch whether it takes spend. Spend returning says the asset was deselected rather than exhausted. Spend not returning says the audience is done with it. **Run this before funding a reshoot**, which is where [[Creative Science#CR-124|CR-124]] has been stuck for four passes, and note that [[Creative Science#CR-147|CR-147]] already reports the same revival shape from a landing-page change, which is also outside the asset.

**The honest caveat on this specific lever.** The setting named is incremental attribution, whose own mechanism is contested at [[Attribution & Incrementality#AT-035|AT-035]] and whose published effect size fails the holdout test at [[Attribution & Incrementality#AT-117|AT-117]]. If incremental attribution optimizes toward a partly different user pool, an asset taking spend there is a statement about pool composition, not about the creative. So the diagnostic is sound and the causal story behind it is not established.
Sources: Meta for Business News, Performance Spotlight: How Instant Hydration Built a System for AI to Scale, 2026-09-10
Last touched: 2026-09-12

### CR-233 · A format swap from statics to video cut a fragrance account's cost per purchase from $491 to $107 in 30 days, and the stated mechanism is that a non-demonstrable benefit needs several people reacting rather than one
Tier: T2 for the account numbers, T3 for attributing them to the format · Status: active
Nick Theriot, 2026-09-11, a new agency client selling a fragrance. Both windows read off Ads Manager on screen.

| Window | Spend | Cost per purchase | Creative |
|---|---|---|---|
| 30 days before onboarding | about $2,000 | $491 | statics only |
| First 30 days after onboarding | about $3,400 | $107 | video only |

**The arithmetic he states is 75% and the figures give 78%.** Use the figures.

**What is NOT isolated, and the list is long.** The agency changed at the same time as the format, so structure, budget, bids and targeting all moved with it. Spend rose about 73%, which changes the auction position and the delivery pool. No attribution window is stated, no account named, no product price, no conversion volume, and a $107 cost per purchase on $3,400 is roughly 32 purchases, small enough that the figure carries real noise. He flags the size himself: "is this a massive case study where it's just like, oh my god, like we're scaling, we're crushing it? No."

**The mechanism is the part worth carrying, and it is narrower than "video beats statics."** A fragrance cannot show its benefit. The claim is that a single person saying it smells good reads as bought, and that stacking several different people reacting to one creator inside a single video is what makes the claim believable. "If we just showed one person reacting to it, then it's like, oh, well, it's obviously fake cuz it's just one person. But if I show multiple different people, it helps create more belief." His general form: the job of the creative is to install a belief, and the number of beliefs you have to install follows the awareness stage.

**Read it as a proof-device claim, not a format claim.** The codex already rejects "statics don't work for our brand" as a skill gap rather than a property of the format at [[Creative Science#CR-032|CR-032]], and [[Creative Science#CR-054|CR-054]] has statics and video competing inside a concept rather than being siloed. Nothing here overturns that. What it adds is a selection rule: **when the product's benefit cannot be seen on screen, the creative has to carry witnesses, and one witness is worse than none because it reads as paid.** That is testable on our own book, and it applies well outside fragrance.

**The counterweight in the same session, recorded because it cuts against the research-heavy default elsewhere in this file.** He did no research on this account: "some products just are simple products and you need a very simple thing... research is just a tool", matched to the job. That is a defensible position and it is also the position of someone describing a win after the fact.
Sources: Nick Theriot, We Cut This Brand's Facebook Ads CPA by 75% (Here's How), 2026-09-11
Last touched: 2026-09-12
""")

# ---------------------------------------------------------------- LS-077 new
append("Learning & Signal.md", """
### LS-077 · An advertiser claims that running more channels improves Meta performance by feeding Meta more signal, and the claim has an ordinary confound it never addresses
Tier: T4 · Status: active
Instant Hydration, in a Meta-published case study, 10-11 September 2026: "Where we really see the signal get better is the fact that we're running on so many channels now. It actually improves our Meta performance because there's more signals from these different channels coming in."

**Why it is banked at T4 and not higher.** No mechanism is described, no measurement is offered, and the sentence conflates two things. Site and purchase events fired by traffic from other channels do reach the pixel and the conversions API, so a busier site genuinely sends more events. That is not the same as those events improving Meta's ranking of Meta impressions, which is what the advertiser is claiming. **The ordinary explanation is that spending on more channels raises total demand, and Meta's last-click column captures some of it.** That produces exactly the reported pattern with no signal story at all.

**Why it is banked at all.** It is a clean, checkable statement of a belief that is widespread and almost never written down, and it points at a real question this file has no entry for: does off-Meta-sourced conversion volume improve Meta's delivery on the same account. **A test exists and it is not cheap**, because it needs a channel turned off or on with Meta spend held flat, which is the natural experiment shape already recorded at [[Attribution & Incrementality#AT-050|AT-050]]. Until someone runs it, do not repeat this to a client as a reason to add a channel.

**From the same account, and it belongs beside this one because it is the same person describing their operating model.** They run an agent against a third-party tool that reads business-level CAC and reallocates budget across ad sets in real time: "Right now your CAC is very low, the business is performing well, and it just allocates budget to the best ad sets." No tool named, no rules shown, no result attached. Record it as a dated example of external-signal budget control existing in a large account, never as a recommendation.
Sources: Meta for Business News, Performance Spotlight: How Instant Hydration Built a System for AI to Scale, 2026-09-10
Last touched: 2026-09-12
""")

print("phase 2 done")
