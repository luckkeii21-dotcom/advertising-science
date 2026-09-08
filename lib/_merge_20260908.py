# -*- coding: utf-8 -*-
"""Advertising Science research merge, 2026-09-08.

Two transcripts read in full:
  Nick Theriot,  2026-09-07, UGC vs Native vs Static Ads: Which One Scales Best in 2026?
  Andrew Faris,  2026-09-08, Your Cost Caps Will Break During Your Next Sale. Here's The Fix.

No em dashes, no contrast negating.
"""
from pathlib import Path

S = Path(r"E:\claude code marketing skill\Obsidian God-level Marketing Vault"
         r"\God-level Marketing\wiki\science")
AUC = S / "Auction Mechanics & Bidding.md"
CRE = S / "Creative Science.md"

FARIS = "Andrew Faris, Your Cost Caps Will Break During Your Next Sale. Here's The Fix., 2026-09-08"
THERIOT = "Nick Theriot, UGC vs Native vs Static Ads: Which One Scales Best in 2026?, 2026-09-07"


def sub(path, old, new, label):
    t = path.read_text(encoding="utf-8")
    n = t.count(old)
    if n != 1:
        raise SystemExit("ANCHOR count=%d for %s" % (n, label))
    path.write_text(t.replace(old, new), encoding="utf-8")
    print("ok   " + label)


def append(path, block, label):
    t = path.read_text(encoding="utf-8")
    path.write_text(t.rstrip("\n") + "\n\n" + block.strip("\n") + "\n", encoding="utf-8")
    print("ok   " + label)


# ============================================================ AMEND AU-028
sub(AUC,
"""Sources: Andrew Faris, Your Meta Ads Account Has Too Many Campaigns, Here's Why And What To Do About It (With Phil Kiel), 2026-05-12
Last touched: 2026-08-18""",
"""**Scope limit added 2026-09-08, from the same speaker, and read it before quoting this claim into a promotion.** The account behind this claim is a seasonal gift brand whose demand rises over roughly 30 days with no price change, and the headline conclusion, that no reach intervention is needed, was reached inside that window. Four months later Faris describes the opposite operating problem for a PROMOTION: a discount lifts conversion rate as a step change, Meta's prediction lags it, and the bid underdelivers for as long as the lag lasts, which costs real volume when the sale runs a weekend rather than a month ([[Auction Mechanics & Bidding#AU-086|AU-086]]). The two are compatible on their facts, because the mechanism is the same catch-up and only the window length and the price discontinuity differ. The catch-up arriving on its own is worth nothing inside a four-day sale. **Faris never reconciles them himself and never cites the earlier case in the later episode**, so the honest reading is that this claim is scoped to slow seasonal demand rises and says nothing about a discounted promotion. Do not carry "Meta widens reach on its own" into a Black Friday or flash-sale decision.
Sources: Andrew Faris, Your Meta Ads Account Has Too Many Campaigns, Here's Why And What To Do About It (With Phil Kiel), 2026-05-12; """ + FARIS + """
Last touched: 2026-09-08""", "AU-028 scope limit")

# ============================================================ AMEND AU-029
sub(AUC,
"""Sources: Andrew Faris, From A 65% Decline To All-Time Revenue and Profit Highs With Richie Mashiko From She's Birdie, 2026-04-27; Andrew Faris, How To Fix The Most Common Bid Cap & Cost Cap Mistake I See, 2026-06-25
Last touched: 2026-08-19""",
"""**The MARGIN term, added 2026-09-08 from the same speaker, and this claim was carrying only half the calculation.** Re-deriving the cap against the sale's new AOV is necessary and it is not sufficient, because a promotion moves the margin underneath the AOV at the same time. His arithmetic: a $100 cap against a $150 AOV is a 1.5 return and the same $100 cap against a $250 AOV is a 2.5 return, so the cap has to track AOV; then the target itself has to track margin, because "almost certainly for most brands when you're on sale, you're going to have some amount less margin than usual." **The exception he names is worth keeping, because it is a real mechanism rather than a hedge.** Shipping and pick-and-pack are close to fixed per ORDER, so a second unit adds roughly $1 to $2 of shipping against $10 for the first, and an offer that lifts units per order recovers part of the discount. He then closes the general case with a number: at 40% off, fulfilment savings do not come close to covering it. **So a promotion needs two adjustments, the cap against the new AOV and the target against the new margin, and both get walked back when the sale ends.** Asserted with the arithmetic shown, no account ledger.
Sources: Andrew Faris, From A 65% Decline To All-Time Revenue and Profit Highs With Richie Mashiko From She's Birdie, 2026-04-27; Andrew Faris, How To Fix The Most Common Bid Cap & Cost Cap Mistake I See, 2026-06-25; """ + FARIS + """
Last touched: 2026-09-08""", "AU-029 margin term")

# ============================================================ NEW AU-086/087/088
append(AUC, """
### AU-086 · A manual bid is deliberately slow to update, so it breaks in BOTH directions whenever the future stops resembling the past
Tier: T3 · Status: active
The mechanism in Faris's own framing: a manual bid is a prediction, Meta builds it from spend, predicted clicks and predicted purchases, and it refuses to reprice off a small sample. Five clicks that all convert do not make Meta forecast a 100% conversion rate; it regresses them against a larger data set. **That refusal to overreact is the entire value of a manual bid in an ordinary week, and it is exactly what fails at a promotion**, because a discount lifts conversion rate as a step change while the prediction is still built on full-price behaviour.

**Two symmetrical failures, one cause, and most operators only plan for the first.** At the START of a sale Meta has not updated, so it underdelivers and hands you an efficiency you did not ask for. His worked case: a Friday-to-Monday sale where Friday produced 20 purchases at a $50 cost per acquisition against 8 the previous day at $100, on an ad set aimed at a 2:1 return, so the result lands near 3:1 with the volume you cut price to buy left unbought. At the END of a sale the prediction has finally learned the sale-era conversion rate, so Meta keeps spending against it into full-price traffic and delivers something like $150 against a $100 target.

**The instrument problem underneath it, and it is why this cannot be solved by watching harder.** Meta never exposes how far through the update it is or what conversion rate it currently expects, and Faris says the reported return column itself lags because the system dumps conversions into the ad set late. So the operator is "sort of kind of guessing by reading the tea leaves" and is missing the one variable that would make the decision arithmetic.

**The remedy he commits to is on the back end, and he states it as the expensive mistake rather than as an idea.** On the day a sale ends, drop the budget AND the bid together, pre-committed, on the assumption that the day after is bad: a $100 cost-per-acquisition target becomes a $50 cap, $10,000 of expected good spend becomes $7,000. Because the flip lands at midnight, automate it with a rule instead of intending to catch it. He reports losing sale profits this way repeatedly, "ask me how I know."

This supplies the mechanism behind [[Auction Mechanics & Bidding#AU-010|AU-010]]'s roughly 50-purchase floor before moving a manual bid, and it scopes [[Auction Mechanics & Bidding#AU-028|AU-028]]. Faris's own hedge on the prediction internals is "as far as anybody knows", and no account data is shown for any of it.
Sources: """ + FARIS + """
Last touched: 2026-09-08

### AU-087 · Budget and bid are both pacing mechanisms, and at a promotion you deliberately swap which one is doing the pacing
Tier: T3 · Status: active
The standing configuration first. Normal manual-bid practice sets the budget far above real spend so the bid does all the pacing, and his figures are $5,000/day of actual spend sitting behind a $50,000 or $100,000 budget. **At the opening of a sale that configuration is at its most dangerous, because the bid is being loosened at precisely the moment delivery is least predictable.** His move reverses the roles: raise the cost cap (or lower the target return) AND pull the budget down to a number he is confident he can spend well, so the budget becomes the safety pacer while the bid pushes. Worked shape: an account spending $10,000/day behind a $100,000 to $200,000 budget goes to a $40,000 budget with a more aggressive cap. Once delivery lands at target he flips it back, raising budget and tightening the cap toward the true number, in his example by 50% and 20% respectively.

**The retraction is the part to record, because the cap-raise is the tactic everyone repeats.** Faris describes pushing a $100 cap to $150 to force spend and teach Meta faster, then walks it back on camera: "I generally am at a point now where I think it's not the best idea to do this." The failure he names is that Meta catches up faster than the operator notices, then spends past the true target before anyone reacts, so you have to cut back "quickly and proactively" or spend a lot of bad money fast. His current preference is to push early spend through an auto-bid campaign instead. **So the cap-raise is his described tactic and not his recommendation, and the budget floor underneath it is the half he keeps.**

**This is the general fix for a risk the codex already holds from the opposite direction.** [[Auction Mechanics & Bidding#AU-026|AU-026]] records Charley T naming a high budget ceiling sitting behind a low bid as the configuration that leaks thousands when a cap breaks. Faris reaches the same danger from the promotional calendar rather than the seasonal one, and his standing rule generalises past sales entirely: in all manual-bid buying, know which of the two is currently pacing your spend, because pacing is the only thing either control does.

**His own gap, stated plainly, and it is the honest ceiling on this whole claim:** "There is probably a mathy way to do this. I just haven't really found it yet." Asserted from agency practice, no account data, and he says on camera that the figures are invented for illustration.
Sources: """ + FARIS + """
Last touched: 2026-09-08

### AU-088 · A short sale, or a low purchase count per ad set, is a reason to AUTO-bid the promotion rather than cap it
Tier: T3 · Status: active
The rule falls straight out of [[Auction Mechanics & Bidding#AU-086|AU-086]]. A manual bid is worth having because it does not adjust quickly, so inside a two-to-four-day window it cannot adjust at all and you are holding a stale full-price prediction through the entire promotion. Faris's thresholds in each direction: run the sale campaign on manual bids when purchase density is high, "if you're getting hundreds of purchases per day, even at a low spend"; run it on auto bids when the sale is short or total conversions are low, with a pre-committed budget he adjusts by hand day to day. His live case is a client running repeated two-day sales, always on an auto-bid campaign with a predetermined budget.

**Note the axis, because it differs from everything else in this topic.** Every threshold at [[Auction Mechanics & Bidding#AU-012|AU-012]] is monthly account spend. This one is conversion DENSITY and window LENGTH, and he decouples it from spend explicitly with "even at a low spend". For our own client sizes both readings point the same way, so the practical answer for a short promotion on any account we run is auto bid.

**The build that ships with it.** Pre-schedule a separate sale campaign rather than editing the evergreen ones: ads uploaded, processed and approved before the sale opens, with scheduled start and end dates, on their own budget and bid controls, added as a third campaign alongside the evergreen pair. His standard evergreen base, which he says is the entire Meta account for one live client, is two campaigns carrying the same ads and the same product, one cost cap on highest volume and one target return on highest value, both on incremental attribution. For the sale campaign's optimisation he is openly undecided between one-day click and incremental and says he would "probably start incremental", so do not read that half as settled.
Sources: """ + FARIS + """
Last touched: 2026-09-08
""", "AU-086 / AU-087 / AU-088")


# ============================================================ AMEND CR-047
sub(CRE,
"""Sources: Nick Theriot, I Spend $100k/Day On Facebook Ads, 2026-08-03; Blue Sense Digital, How To Structure A Meta Ads Account At Every Spend Tier In 2026, 2026-06-01; Blue Sense Digital, Reviewing 7 Ads: The One Change I'd Make To 6 Of Them, 2026-01-22; Nick Theriot, Sh*t I care about when scaling Facebook Ads, 2026-07-10; Mark Builds Brands, i tried running only AI ads for 30 days, 2026-04-29
Last touched: 2026-08-21""",
"""**The COST of the third-party page, added 2026-09-08, and until now this claim listed only its benefits.** Theriot runs the format under an invented person's name and photo so the post reads as something a mom put on her feed, and then names what that buys you and what it takes away: "you don't build any brand value because again, you're using like just this random person's name. You're not using your actual branded Facebook page name. And because of that, if you ever decide to do like a sales promo or like a new product drop, it doesn't do as hot because you haven't been building brand value with that particular page." **So the credibility and page-cap gains recorded above are paid for in accumulated page equity, and the bill arrives at exactly the moment a brand needs its own audience, which is a launch or a promotion.** An account running natives as its main format is buying cheap acquisition now against a weaker promotional peak later. He also names the skill floor honestly: the format needs real long-form sales-letter writing, and AI drafts "still requires a little bit of massaging and finesse."

His demographic read, consistent with the 60-plus numbers above and slightly wider: the case studies he sees cluster at 35 or 40 and up, he has seen operators win with 21 and 22 year olds, and he has personally seen few wins in the 18-to-30 band. He states it as where the case studies are rather than as a property of the format. His own character count for the primary text is roughly 2,500, which sits at the top of this claim's range. Awareness scope: he says natives work best for unaware markets and adds that he has also seen product-aware and solution-aware natives work well, so unaware is the centre of the format rather than its boundary.
Sources: Nick Theriot, I Spend $100k/Day On Facebook Ads, 2026-08-03; Blue Sense Digital, How To Structure A Meta Ads Account At Every Spend Tier In 2026, 2026-06-01; Blue Sense Digital, Reviewing 7 Ads: The One Change I'd Make To 6 Of Them, 2026-01-22; Nick Theriot, Sh*t I care about when scaling Facebook Ads, 2026-07-10; Mark Builds Brands, i tried running only AI ads for 30 days, 2026-04-29; """ + THERIOT + """
Last touched: 2026-09-08""", "CR-047 brand-equity cost")

# ============================================================ AMEND CR-048
sub(CRE,
"""Sources: Nick Theriot, I Spend $100k/Day On Facebook Ads, 2026-08-03; Professor Charley T, Copy This Simple Meta Ads Strategy, 2026-08-10; Blue Sense Digital, Meta Ads Creative Strategy in 2026: The Full System, 2026-05-11; Blue Sense Digital, How to Write Ad Hooks That Scale, 2026-01-29; Mark Builds Brands, how to print money with AI (before NPCs ruin it), 2026-04-24; Mark Builds Brands, how to print money online (easier than scrolling youtube), 2025-12-26
Last touched: 2026-09-05""",
"""**A shown before-and-after where the format change is real and the attribution is not clean, added 2026-09-08.** Theriot takes over an account running exclusively statics at a $491 cost per purchase in the prior 30 days, moves it to UGC video because the product needed visual proof, and reports the first 30 days landing at roughly $119, which he states as a 75% drop and is still short of his own $50 target. **Record the number carefully: he says "$107 cost per purchase" earlier in the same passage and "$491 cost per purchase to $119" later, and only the $119 figure is consistent with the 75% he states, so quote $119 and note the discrepancy.** **The bigger caution is the design.** This is an agency TAKEOVER, so structure, bidding, targeting, budget and copy all changed alongside the format, and none of them is held constant. It is a real account with real numbers and it is not evidence that format alone moved the cost, which is the same class of confound this codex flags elsewhere in someone else's case study. What it does support is the softer version already in this claim: on a product whose proof has to be seen, an all-static account is leaving money on the table.

**A second longevity outlier from the same pass, and it belongs beside the $500,000 static above.** Theriot names a static he built on 2025-07-19 that had spent $260,000 by 2026-09-03, roughly 13.5 months, headline "Viral new laser treatment finishes acne in 30 minutes". Three operators now report single statics carrying six figures of lifetime spend, which is the tail discussed at [[Creative Science#CR-117|CR-117]]. He also names the entry-barrier failure mode of the format: statics are so cheap to produce that operators test hundreds over weeks, get nowhere, and conclude Meta does not work for them, which is the volume version of the skill-gap diagnosis at [[Creative Science#CR-125|CR-125]].
Sources: Nick Theriot, I Spend $100k/Day On Facebook Ads, 2026-08-03; Professor Charley T, Copy This Simple Meta Ads Strategy, 2026-08-10; Blue Sense Digital, Meta Ads Creative Strategy in 2026: The Full System, 2026-05-11; Blue Sense Digital, How to Write Ad Hooks That Scale, 2026-01-29; Mark Builds Brands, how to print money with AI (before NPCs ruin it), 2026-04-24; Mark Builds Brands, how to print money online (easier than scrolling youtube), 2025-12-26; """ + THERIOT + """
Last touched: 2026-09-08""", "CR-048 takeover case + static longevity")

# ============================================================ AMEND CR-117
sub(CRE,
"""Sources: Blue Sense Digital, How to Scale an eCommerce Brand Profitably in 2026: The Full System, 2026-06-15; Blue Sense Digital, Meta Ads Creative Strategy in 2026: The Full System, 2026-05-11; Professor Charley T, Copy This Facebook Ads Strategy (Post-Andromeda), 2026-02-07; Blue Sense Digital, Stop Sending Cold Traffic on Meta to PDPs, 2025-10-30
Last touched: 2026-08-20""",
"""Third operator into the right tail, added 2026-09-08, and this one carries dates on both ends. Nick Theriot names a single static created 2025-07-19 that had spent $260,000 by 2026-09-03, about 13.5 months on one asset. That is roughly 170 to 370 times the $700 to $1,500 mean this claim opens with. **Three operators, three formats, all reporting six-figure single-ad lifetimes, and still nobody has shown a distribution.** The planning consequence hardens: a creative-volume forecast built on a $1,000 mean per ad is modelling the body of a distribution whose tail carries the account, so state the mean as a mean and never as a capacity.
Sources: Blue Sense Digital, How to Scale an eCommerce Brand Profitably in 2026: The Full System, 2026-06-15; Blue Sense Digital, Meta Ads Creative Strategy in 2026: The Full System, 2026-05-11; Professor Charley T, Copy This Facebook Ads Strategy (Post-Andromeda), 2026-02-07; Blue Sense Digital, Stop Sending Cold Traffic on Meta to PDPs, 2025-10-30; """ + THERIOT + """
Last touched: 2026-09-08""", "CR-117 third tail observation")

# ============================================================ AMEND CR-125
sub(CRE,
"""Sources: Blue Sense Digital, How to Scale an eCommerce Brand Profitably in 2026: The Full System, 2026-06-15; Blue Sense Digital, How To Structure Your Meta Ads for Profit (Free Live Webinar), 2025-02-19; Professor Charley T, If you run Facebook Ads... everything just changed., 2025-12-06; Ben Heath, Copy This Meta Ads Testing Strategy for Better Results, 2026-03-03; Ben Heath, Why Most Meta Ads Fail Before Anyone Sees Them, 2026-02-27
Last touched: 2026-08-21""",
"""**A fifth operator on the format-last half, added 2026-09-08, and he is the first to attach an account observation to it.** Theriot states it as "format does not create the winner, messaging does", with messaging as the engine and format as the body of the car, and shows a group of ads that between them carry over $100,000 of spend, all built on the SAME core messaging across several different UGC videos plus an animated version. That is the closest thing on file to the natural experiment this claim needs, since the message is held constant and only the format varies, and it is still a screenshot of spend with no cost per acquisition attached and no failed formats shown. **Everyone now agrees format goes last and nobody has run the controlled test.** What decides format once the message is settled is banked separately at [[Creative Science#CR-230|CR-230]].
Sources: Blue Sense Digital, How to Scale an eCommerce Brand Profitably in 2026: The Full System, 2026-06-15; Blue Sense Digital, How To Structure Your Meta Ads for Profit (Free Live Webinar), 2025-02-19; Professor Charley T, If you run Facebook Ads... everything just changed., 2025-12-06; Ben Heath, Copy This Meta Ads Testing Strategy for Better Results, 2026-03-03; Ben Heath, Why Most Meta Ads Fail Before Anyone Sees Them, 2026-02-27; """ + THERIOT + """
Last touched: 2026-09-08""", "CR-125 fifth operator")

# ============================================================ NEW CR-230
append(CRE, """
### CR-230 · Format is chosen from two questions, what has to be COMMUNICATED and what carries the PROOF, and the ad's destination moves the answer
Tier: T3 · Status: active
[[Creative Science#CR-125|CR-125]] settles that format is tested last. This is the rule Theriot uses to pick it once the message is decided, and he states it as two questions he asks himself: "What do I need to communicate to people?" and "what is going to create the most proof?" Format falls out of the answers rather than entering as an option to test.

**The three answers, with the trade he names against each.**
- **UGC when the product has to be SEEN.** "People believe what they see, not what they hear." Its three jobs: demonstrate a product in action, stack testimonials from several different people so the viewer sees multiple approvals at once, and carry a product too complex to simply state. The cost is production: $200 to $300 per creator, shipping the product to them, a turnaround measured in weeks, and creator management including scripts that come back wrong on the first pass. AI UGC removes the creator dependency and shortens the turnaround, and his two limits on it are that it is "still not 100% perfect with some products" and that generation credits burn fast at volume.
- **Static when there is ONE quick message.** Cheap, and he produces several a day with intention behind each.
- **Native when the job is storytelling**, mostly for unaware markets, detailed at [[Creative Science#CR-047|CR-047]].

**The DESTINATION is the boundary condition, and it is the part that makes the rule usable.** His acne client's static only has to name a new mechanism, because the ad drives to a booked call and the call does the selling. He says the same offer pointed at a sales page instead "would need a longer sales letter". **So the same product, the same market and the same message change format when the destination changes**, which means a format decision copied between two accounts with different funnels is copied wrong. His contrast case, an ad he did not make, is a testosterone offer that has to diagnose a reader into a problem they do not know they have and therefore runs long and native.

The failure this rule is built to prevent is the same one at [[Creative Science#CR-125|CR-125]]: teams pick a format first, run it badly for the job, and conclude the format does not work. Asserted from agency practice across the examples he shows, with no comparison of two formats carrying the same message at matched spend.
Sources: """ + THERIOT + """
Last touched: 2026-09-08
""", "CR-230")

print("MERGE COMPLETE")
