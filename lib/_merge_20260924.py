"""Claim merge for the 2026-09-24 research pass.

New: MD-166, MD-167, AU-095, SC-171, SC-172, CR-265, GA-080.
Amend: MD-157, MD-125, SC-044, SC-008, SC-161, AU-051, LS-074, GA-043.

Sources actually read today:
 - Facebook Help Centre, "About links in organic Facebook Page posts and
   comments", /help/1929252614431792, read in full via browser 2026-09-24
 - Meta for Business News, "Introducing Meta One plans for businesses",
   15 September 2026, re-read in full 2026-09-24 for the pricing table
 - Google Ads & Commerce Blog, "We're bringing AI Brief to more languages and
   adding a new AI Max reporting feature", 23 September 2026, read in full
 - Nick Theriot, "I tested ABO & Cost Caps (here's the results)", 2026-09-23
 - Ben Heath, "I paid Alex Hormozi $235,000 for his Facebook Ads Strategy",
   2026-09-23
 - Jon Loomer, "Meta Wants Businesses to Pay to Share Links", 2026-09-23
"""
import re
import sys
from pathlib import Path

VAULT = Path(r"E:\claude code marketing skill\Obsidian God-level Marketing Vault"
             r"\God-level Marketing\wiki\science")

FILES = {
    "AU": VAULT / "Auction Mechanics & Bidding.md",
    "CR": VAULT / "Creative Science.md",
    "SC": VAULT / "Scaling Models.md",
    "MD": VAULT / "Meta Delivery & Andromeda.md",
    "LS": VAULT / "Learning & Signal.md",
    "GA": VAULT / "Google Auction & Smart Bidding.md",
}

TODAY = "2026-09-24"


def read(p):
    return p.read_text(encoding="utf-8")


def write(p, s):
    p.write_text(s, encoding="utf-8")


def block_span(text, claim_id):
    """Return (start, end) character offsets of a claim block."""
    m = re.search(r"^### %s[ \u00b7\-]" % re.escape(claim_id), text, re.M)
    if not m:
        raise SystemExit("NOT FOUND: %s" % claim_id)
    start = m.start()
    nxt = re.search(r"^### ", text[m.end():], re.M)
    end = m.end() + nxt.start() if nxt else len(text)
    return start, end


def amend(prefix, claim_id, addition):
    """Insert addition before the block's Sources line and bump Last touched."""
    p = FILES[prefix]
    text = read(p)
    start, end = block_span(text, claim_id)
    block = text[start:end]

    src = list(re.finditer(r"^Sources?:", block, re.M))
    if src:
        at = src[-1].start()
        block = block[:at] + addition.strip() + "\n" + block[at:]
    else:
        block = block.rstrip("\n") + "\n" + addition.strip() + "\n"

    if re.search(r"^Last touched:.*$", block, re.M):
        block = re.sub(r"^Last touched:.*$", "Last touched: " + TODAY,
                       block, count=1, flags=re.M)
    else:
        block = block.rstrip("\n") + "\nLast touched: %s\n" % TODAY

    write(p, text[:start] + block + text[end:])
    print("amended %s" % claim_id)


def append_claim(prefix, body):
    p = FILES[prefix]
    text = read(p).rstrip("\n")
    write(p, text + "\n\n" + body.strip() + "\n")
    print("added   %s" % body.strip().split("\n")[0][4:24])


# ---------------------------------------------------------------- NEW CLAIMS

append_claim("MD", """
### MD-166 \u00b7 Meta caps organic Facebook Page link posts at 2 a month on the free tier and sells the increase through Meta One, and links in ads are explicitly exempt
Tier: T1 \u00b7 Status: active
Read off Meta's own help article today, "About links in organic Facebook Page posts and comments". This is the half of Meta One that [[Meta Delivery & Andromeda#MD-157|MD-157]] recorded as an added feature, stated from the other direction as a restriction on something that was previously free.

**The table, verbatim from Meta, in USD per month:**

| Meta One plan | Posts or comments with links per month |
|---|---|
| Free, no subscription | 2 |
| Essential, $14.99 | 2 |
| Advanced, $49.99 | 8 |
| Expert, $149.99 | 20 |
| Max, $499.99 | Unlimited |

**The reset rule.** The default limit resets on the 1st of the month. A subscriber's limit resets on the subscription renewal date. Unused link posts do not carry forward.

**What does NOT count against the limit, and the fourth exemption is the one that matters to a media buyer.** Additional links in the comments of a post that already carries a link; links to Meta properties (Facebook, Instagram, WhatsApp, Threads); affiliate-partnership links connected through Facebook; and **links in ads**. So paid delivery is untouched. Nothing in this changes what a client can run, what it costs, or how it delivers. It changes what a client's Page can post for free.

**The scope caveat is Meta's own first sentence and it should be quoted before this is repeated to anyone:** "Limits on posts and comments with links may not apply to all Pages." Meta does not say which Pages, so no one can state from this article whether a given client Page is subject to it. Check the Page.

**Two things a widely-shared practitioner reading of this gets wrong, and both were checked against the source today.** Jon Loomer states per-tier splits of 8 Facebook plus 4 Instagram at Advanced and 20 Facebook plus 8 Instagram at Expert. **This article is Facebook Pages only and publishes a single number per tier with no Instagram split**, so the Instagram figures are unverified and should not be repeated. He also states that putting the link in the comments will not get around the restriction. That is right for a standalone comment and wrong for the case Meta exempts: extra links inside the comments of a post that already carries one are free.

**Meta's own two pages disagree on the price.** The help article says Expert $149.99 and Max $499.99. The Meta for Business announcement, re-read in full on the same day, says Expert $149.00 and Max $499.00. A dollar either way changes no decision, and it is the third documented case on this source of two Meta surfaces disagreeing about the same fact, after the card-date drift of 2026-09-14 and the locale partition of 2026-09-20. Never quote a Meta price from a single page.

**Why this is banked as a restriction rather than as a product note.** The 2026-09-15 harvest entry deliberately withheld a warning line from MD-157 on the reasoning that "Meta One removes nothing, bans nothing and breaks nothing." That reasoning was written from the announcement, which frames links in posts as a new capability. The help article is the same change written as a cap, and it does remove something that was free.
Sources: Facebook Help Centre, "About links in organic Facebook Page posts and comments", https://www.facebook.com/help/1929252614431792, read in full 2026-09-24; Meta for Business News, "Introducing Meta One plans for businesses", 15 September 2026, re-read 2026-09-24; Jon Loomer, "Meta Wants Businesses to Pay to Share Links", 2026-09-23
Last touched: 2026-09-24
""")

append_claim("MD", """
### MD-167 \u00b7 The same post ID running in two live campaigns appears to self-compete at the AD level: $3,600 in the testing campaign, $26 in the cost cap campaign it was copied into
Tier: T4 \u00b7 Status: active
Nick Theriot, from a 7-day test on a client store, and he flags it as a belief with the control named and not run.

**The observation.** A winning ad was found in an ABO testing campaign and scaled there from $100 a day to $800 a day before it collapsed. The same ad, carried into a separate cost cap campaign by post ID, **took $26 of spend** over the same window against **$3,600** in the testing campaign.

**His read:** "this ad right here did work in the ABO campaign before we moved it to a CBO campaign... the CBO for that particular ad is getting bullied out by the ABO campaign", on the reasoning that the testing campaign had already taken the cold audience the second campaign needed.

**What is missing, stated by him.** The ad was never run in the second campaign alone. He says so directly: "would this ad have worked well if we just tossed them in a CBO campaign, non cost cap, no nothing, and just start scaling it? Who knows. Honestly, couldn't tell you the answer because we didn't do that here." So a plain starvation explanation is not excluded, and neither is the cost cap simply refusing to bid at the price.

**Why it is worth an ID despite being T4.** Duplicating a proven post ID into a second campaign is standard practice across this roster, and no claim in this codex prices what the first campaign costs the second one. It is the ad-level version of the entity-level cannibalisation already recorded at [[Meta Delivery & Andromeda#MD-045|MD-045]], and it is the counterweight to [[Scaling Models#SC-161|SC-161]], where the same operator reports a second campaign rescuing new creative that could not win inside the incumbent CBO. Both cannot be freely true at the same spend, and nobody has tested which regime applies when.

**The cheap test, if anyone wants to close it:** pause the ad in the first campaign for 72 hours and read the second campaign's spend on the same post ID.
Sources: Nick Theriot, "I tested ABO & Cost Caps (here's the results)", 2026-09-23
Last touched: 2026-09-24
""")

append_claim("AU", """
### AU-095 \u00b7 The cost-cap ratchet: open the cap far below the account average, raise it $5 every 2 to 3 days, and raise the BUDGET freely, because a cap cannot force spend
Tier: T2 \u00b7 Status: active
The first shown-account cost-cap operating procedure in this topic. Every other cost-cap claim here argues whether caps work. This one states how one was actually run, with the numbers on screen.

**The account.** A client store at roughly $40,000 revenue over 7 days, target new-customer cost per acquisition $65, account-average cost per acquisition running $50 to $60, about $22,000 total ad spend in the window and about $15,000 of it across the two campaigns being tested.

**The ratchet.** The cost cap opened at **$30**, well under the account average, and was raised **$5 at a time, every two to three days**. Theriot's stated purpose is spend rather than efficiency: "I intentionally set it really low and I just kept bumping it up by $5 to get Facebook to spend more and more on it every single day." Early on it delivered around a $25 cost per acquisition at a spend level too small to matter, and he let efficiency drift up on purpose because everything under $65 cleared target. **Result at the end of the window: $55 new-customer cost per acquisition on Triple Whale, against the $65 target.**

**The budget half, and it is the part that generalises.** The campaign carried a **$3,000 a day budget that it was never expected to spend**, and spent the full amount on only two or three days. His reasoning: "I can be more aggressive with raising the budget in a cost cap campaign because the budget is not like a highest value campaign where you'll force spend on all those ads. I'm just giving more room now for those ads to spend if they can, but the cost cap's going to protect me." So under a cap, budget stops being a spend instruction and becomes a ceiling on opportunity. **That inverts the standard 20% budget-step discipline for capped campaigns only.** The days that spent $100 instead of $3,000 are the cap working, not the campaign failing.

**Two configuration choices stated with reasons.** One ad set only, holding proven post IDs stacked together. And **one-day-click attribution**, on the reasoning that a cost cap is solving a same-day problem: "it's trying to figure out what auctions it can answer you in that day to get you that particular cost cap." He explicitly invites correction on that one.

**The entry gate he applies, and it is stricter than the codex has recorded anywhere.** Nothing enters the cap campaign on a single cheap sale. Ads arrive only after spending $200 to $400 a day in the testing campaign at acceptable cost: "they were proven to do volume in like numbers before being brought here."

**Read it against what this topic already holds.** It does not settle [[Auction Mechanics & Bidding#AU-051|AU-051]], because there is still no capped-versus-uncapped comparison on the same account. It is consistent with [[Auction Mechanics & Bidding#AU-033|AU-033]]'s open-low-then-abandon move, extended into a standing configuration rather than a seeding trick. It sits against [[Auction Mechanics & Bidding#AU-049|AU-049]]'s prediction that a cap turns prospecting into bottom-funnel harvesting: he was measuring NEW-customer cost per acquisition in Triple Whale precisely because the account has heavy repeat purchase, and the cap still cleared target on the new-customer number. That is the closest thing on file to a rebuttal of AU-049, and it is one account over 7 days.

**His own verdict on where the cap belongs.** Good for scaling already-proven ads and for making a large spend jump on a smaller account. Not worth the extra campaign to optimise on an account already spending $2,000 to $3,000 a day, where he would rather put new winners into the main CBO. And explicitly bad for testing: "if you're testing new ads on cost caps, you can be quite too restrictive with some of those ads."

One account, 7 days, no holdout, and the same window also changed campaign structure and creative, so nothing here isolates the cap.
Sources: Nick Theriot, "I tested ABO & Cost Caps (here's the results)", 2026-09-23
Last touched: 2026-09-24
""")

append_claim("SC", """
### SC-171 \u00b7 A dedicated ABO testing campaign cost about $10,000 to learn what the same operator estimates a CBO would have learned for about $2,000, at a $106 new-customer CPA against a $65 target
Tier: T2 \u00b7 Status: active
The first priced answer in this file to the question [[Scaling Models#SC-058|SC-058]] frames as risk versus efficiency. Theriot, who teaches CBO-only, ran a separate ABO creative-testing campaign for 7 days specifically to test the structure he argues against.

**The numbers, from the account.** About **51 tests** inside the campaign. Each ad set launched at **$100 a day** and cut at 2 to 3 days, three creatives per ad set, one ad idea per ad set. Total spend about **$10,000**, at a **$106 new-customer cost per acquisition** against a $65 target. The best single ad inside it reached $3,600 of spend at a $69 cost per purchase with an acceptable new-customer number.

**The counterfactual, and it is his estimate rather than a measurement:** "if we had launched this in a CBO campaign, we would probably have spent 2k right there. So we spent like an extra 8k." No control ran, so the $8,000 is an unverified delta from the operator who already holds the position it supports.

**What he says it buys.** Decision confidence and speed, stated plainly and against his own interest: "I love the confidence knowing what actually works versus what actually doesn't", plus a clean lane for testing a new landing page or a new country by adding one ad set. **What he says it does not buy** is a different answer: the ads that won in the ABO were ads he believes would have won in the CBO anyway.

**The rule he ends on, and it is a budget rule rather than a performance rule.** "If you're more budget-conscious, then I would not recommend doing an ABO campaign. If you have a little bit more ad spend, definitely go more of the ABO route." That is [[Scaling Models#SC-058|SC-058]] restated with a price tag: on this account, the tuition for structural certainty was roughly 45% of the window's spend.

**Scope before anyone applies the $8,000.** One e-commerce account at about $3,000 a day, 7 days, aggressive $100-a-day tests cut at 2 to 3 days. An operator running $10-a-day tests over two weeks is buying a different thing at a different price, and he names that as the contrast.
Sources: Nick Theriot, "I tested ABO & Cost Caps (here's the results)", 2026-09-23
Last touched: 2026-09-24
""")

append_claim("SC", """
### SC-172 \u00b7 Across 51 ad-set tests, killing the top-spending ad to push spend toward a cheaper-CPA sibling failed to hold performance 99% of the time, and the operator stopped making ad-level decisions inside a test campaign
Tier: T2 \u00b7 Status: active
The largest stated n anyone on this roster has put behind the kill-the-hog question, and it lands on the leave-it-on side. It is the within-ad-set twin of [[Scaling Models#SC-008|SC-008]], which is `contested` and has never had a count attached to either side.

**The pattern he describes.** Inside a three-creative ad set, one ad takes nearly all the spend while a sibling converts better on a much smaller base. His worked example from the account: one creative at **$3,600**, one at **33 cents**, one at **zero**. A second shape: one at about $1,000 with no sales, one at about $200 with five purchases. He calls the reflex "no brainer, turn off the top one."

**The result, verbatim:** "99% of the time that we tested, in all of these different 51 tests, every time that scenario happened, us turning off the top spending ad and putting spend towards the lower spending ad that was converting way better, 99% of the time it did not hold performance at all."

**What he changed as a result, and it is the operating half.** He stopped reading the ad level inside a testing campaign: "I'm not looking at ads for one campaign. I'm actually breaking down each individual ad set. And I'm turning just the whole ad set off. I'm not going to turn off one ad inside of the ad set and go that deep into the tweaking." So the decision unit moves up one level, from ad to ad set.

**Where this sits against SC-008.** SC-008 is a CBO claim about the two highest-spending ADS in a campaign, and the count there stands at four operators asserting and none showing. This is an ABO claim about the single highest-spending ad inside an AD SET, and it supplies what SC-008 has never had: a stated number of occasions and a stated failure rate. **It does not resolve SC-008**, because the structures differ and because "99% of 51" is recalled on camera with no log shown, no definition of "did not hold performance" and no before-and-after CPA on any of the 51. Treat the direction as the strongest evidence on file and the 99% as a round number a person said out loud.

**Why it matters more than the usual corroboration.** [[Scaling Models#SC-085|SC-085]]'s whole disagreement is about whether an expensive-looking top spender is doing top-of-funnel work for its siblings. This is 51 chances for that hypothesis to be wrong in a structure where the reallocation is forced and immediate, and it was reported wrong roughly once.
Sources: Nick Theriot, "I tested ABO & Cost Caps (here's the results)", 2026-09-23
Last touched: 2026-09-24
""")

append_claim("CR", """
### CR-265 \u00b7 A portfolio operator reports results BETTER than ever post-Andromeda, at 50-plus new ads a week per business, against the roster-wide narrative that Andromeda made things worse
Tier: T3 \u00b7 Status: active
Second-hand, no data shown, and banked because it is the only voice on this roster pushing the other way on a question the codex has been hearing one-sidedly.

**The claim.** Ben Heath, reporting a paid day with Alex Hormozi: Hormozi's Meta results are better than ever after Andromeda, and explicitly **not only on the personal brand**. Heath raises and dismisses that objection himself, saying it holds "across the board" on the portfolio companies. Heath's framing of why it is interesting is the right one: "that goes against the narrative of what you hear from most advertisers online."

**The stated price of it.** More creative than ever, at a cadence of **50-plus ads recorded every single week** per business, by whoever records for that portfolio company. Heath relays that Hormozi finds the work boring and does it anyway.

**Evidence status, stated bluntly.** This is one person relaying a second person's verbal summary of unshown accounts. No spend, no account count, no before-and-after, no window, no definition of "better". It cannot be quoted as a result. What it is good for is as a counterweight: every "Andromeda broke my account" claim in this file is also an unshown assertion, and this is the same class of statement pointing the other way from an operator with a portfolio rather than one account.

**Where it connects.** [[Creative Science#CR-001|CR-001]] has Meta building Andromeda explicitly to absorb rising creative volume, which is the T1 mechanism this anecdote is consistent with. [[Creative Science#CR-255|CR-255]] already warns that a creative-volume target is a count of WINNERS rather than a count of ads, and 50 a week is a production number with no win rate attached. [[Meta Delivery & Andromeda#MD-125|MD-125]] holds the per-ad-set ceiling.

**The honest reading for a client conversation.** Two things could produce "better post-Andromeda" here and they have different costs: the system genuinely rewarding creative diversity, or an operator who can afford 50 ads a week outcompeting operators who cannot. Nothing in the account distinguishes them, and the second one is the reading a smaller client should price first.
Sources: Ben Heath, "I paid Alex Hormozi $235,000 for his Facebook Ads Strategy", 2026-09-23
Last touched: 2026-09-24
""")

append_claim("GA", """
### GA-080 \u00b7 Google is shipping a unified Search-ads-journey report for AI Max and AI Brief in seven more languages, and neither closes the AI-surface spend blind spot
Tier: T1 \u00b7 Status: active
Google Ads & Commerce Blog, 23 September 2026, read in full. T1 for existence and product copy only. Nothing here states that AI Max performs, and the same tier guard applies as at [[Google Auction & Smart Bidding#GA-062|GA-062]].

**What was announced, two things.**

1. **AI Brief closed beta widens to seven more languages:** Dutch, French, German, Italian, Japanese, Portuguese and Spanish. Google's description of the feature: it "lets you guide AI Max in your own words with detailed context on your business, audience, and key messaging." Still a closed beta, so availability is by invitation.

2. **A new report in Google Ads**, described as "a single, unified view of the Search ads journey", showing "what search terms triggered your ads, which creative assets the user saw, and exactly where they landed on your website." Google's stated purpose includes validating "the strategic value AI Max brings to your campaigns."

**Availability, quoted because it is the whole limit:** "We'll share additional details and availability later this year." So there is no ship date, no eligibility list and nothing an account can be checked against today.

**Checked against the open blind spot, and it stays open.** [[Google Auction & Smart Bidding#GA-043|GA-043]] records that broad match, Shopping feeds, PMax and AI Max can all serve inside AI Overviews and AI Mode with no setting to disable it and no report that segments those clicks or that spend. **A search-term-to-asset-to-landing-page report is a within-Search attribution view. It does not break out what an ad account spent on an AI surface**, so the thing GA-043 is waiting for has not shipped. This is the second time in eight days that a Google reporting release has been checked against GA-043 and found adjacent rather than sufficient, after the Merchant Center AI performance insights release at [[Google PMax & Shopping#GP-047|GP-047]] on 2026-09-17.

**One line worth keeping for an account review.** Google is describing a first-party report whose stated job includes validating its own product's value. Read the journey data, do not read the framing. The instrument that actually measures AI Max on our accounts is still the within-campaign experiment documented at [[Google Auction & Smart Bidding#GA-062|GA-062]].
Sources: Google Ads & Commerce Blog, "We're bringing AI Brief to more languages and adding a new AI Max reporting feature", 23 September 2026, read in full 2026-09-24
Last touched: 2026-09-24
""")

# ------------------------------------------------------------------- AMENDS

amend("MD", "MD-157", """
**The link feature is also a CAP, found 2026-09-24 and banked in full at [[Meta Delivery & Andromeda#MD-166|MD-166]].** This claim lists "links in organic posts and reels" among the Meta One features and closes by saying every feature in the bundle is organic, profile or support tooling. Both statements survive. What this claim did not carry is the other side of the same change: Meta's help centre states a **default limit of 2 organic Facebook Page posts or comments with links per month** on the free and Essential tiers, rising to 8 on Advanced, 20 on Expert and unlimited on Max. So Meta One is not only adding a capability, it is charging for one that was previously unmetered. **Links in ads are explicitly exempt**, which is why the closing line about ad delivery, ad cost and ad ranking still holds exactly as written.

**A price correction against this claim's own numbers.** This claim records Expert at $149/mo and Max at $499/mo from the newsroom and business posts. The help centre, read 2026-09-24, prints **$149.99 and $499.99**. Both are Meta's own surfaces on the same day. Quote neither figure without naming which page it came from.
""")

amend("MD", "MD-125", """
**Third statement of the same position from this source, 2026-09-23.** Ben Heath, relaying a paid session with Alex Hormozi: "They used to say no more than six ad creative in any one ad set. Totally throw that out. You can have 20, 30, 50 or more running at any one time." His stated constraint is supply rather than the platform: "the limiting factor is not what the platform can handle anymore... the constraining factor is always how much good stuff can you actually produce." That raises his own live-concurrent number from the 20 recorded here in April 2026 to an open range topping out at the 50 ceiling, from the same speaker, and still with nothing shown. The portfolio-scale version of the same argument is at [[Creative Science#CR-265|CR-265]].
""")

amend("SC", "SC-044", """
**A substitution rule for accounts running far off target, added 2026-09-24, and it is the first time anyone has said what to do when the 3x multiple is anchored to a broken number.** Nick Theriot applies the gate as three times the ACCOUNT AVERAGE cost per result at zero results, worked on screen as $210 against a $67 average. He then names the failure case: an account whose current cost per purchase is $300 against a $100 target would, on that rule, burn $900 per ad set to learn nothing. **His fix is to swap the anchor to 3x AOV instead of 3x current CPA** in that situation, which on his example takes the gate from $900 to $300.

Why this matters more than a tweak. The gate on this claim has always been stated against TARGET cost per result by Charley T and Matt Shiver, and against ACCOUNT AVERAGE by Theriot, and nobody had noticed those are different numbers in a failing account. In a healthy account they converge. In a rescue, the account-average version quietly triples the tuition. **Read the rule as: 3x the smaller of target CPA and AOV, over at least 3 days.** Asserted from account practice, no comparison of the three anchors shown.
""")

amend("SC", "SC-008", """
**The first stated COUNT on the leave-it-on side, added 2026-09-24, and it is at the ad-set level rather than the campaign level.** Nick Theriot reports 51 ad-set tests in which killing the top-spending ad to push spend toward a better-converting sibling "did not hold performance at all" 99% of the time, and responded by refusing to make ad-level decisions inside a testing campaign at all. Full record, including why it does not resolve this claim, at [[Scaling Models#SC-172|SC-172]]. It is ABO-within-ad-set rather than CBO-within-campaign, so it does not close [[Scaling Models#SC-085|SC-085]], and the 99% is recalled on camera with no log shown. It is still the only number either side of this argument has ever produced.
""")

amend("SC", "SC-161", """
**The same operator restated the inverse a week later, 2026-09-23, and it tightens the scope of this claim rather than supporting it.** On ads that are already failing inside a CBO, he puts the rescue rate at effectively zero: "if things weren't working in a CBO campaign and we broke out those particular ads to an ABO campaign, our success with getting them to work is like maybe 0.1%. So I'm just going to burn way more money trying to get them to work versus just let the CBO decide." **So the separate-campaign fix recorded here applies to creative that was never funded, not to creative that was funded and lost.** A starved ad and a tested-and-beaten ad are different objects, and only the first one is what this claim rescued.

He also reports the opposite direction of the same competition, at [[Meta Delivery & Andromeda#MD-167|MD-167]]: an ad spending $3,600 in a testing campaign took $26 in the second campaign it was copied into. Read the two together, a second campaign buys spend for new creative and can lose it for creative the first campaign is already funding.
""")

amend("AU", "AU-051", """
**A fourth operator lands in the same place from the pro-cap side, added 2026-09-24, which is worth more than another anti-cap voice.** Nick Theriot ran a cost cap campaign for 7 days on a client account and clears it on target at a $55 new-customer cost per acquisition (full procedure at [[Auction Mechanics & Bidding#AU-095|AU-095]]). His verdict is still not a performance claim: the cap is "a cool tool to have in the bucket", worth it on smaller accounts making a large spend jump, and **not worth the extra campaign on an account already at $2,000 to $3,000 a day**, where he would rather put new winners into the main CBO. So an operator who got a cap to work on target declines to claim it beat the alternative, because he never ran the alternative. **The count of controlled capped-versus-uncapped comparisons on the same account across this entire roster remains zero.**
""")

amend("LS", "LS-074", """
**A second independent operator on the same two levers, added 2026-09-24, and still nothing measured.** Ben Heath describes the identical conditional-logic structure, on the website side as two thank-you pages firing two different conversion events, and on the Instant Form side as routing a disqualified answer to a non-lead end page. His framing of the mechanism matches this claim exactly: "anyone that comes through that form and says they have less than $5,000, Meta goes, we haven't achieved our objective, that's not what we're optimizing for." He names budget, timeline, industry, education and life stage as the qualifier axes.

He independently reaches the **same OTP position** recorded here, and has moved to it as his default: form type "higher intent" plus required phone-number verification by one-time passcode, on the reasoning that it forces a real number and filters out people who are not serious. **Two operators, same two levers, same direction, and between them zero figures on lead volume, cost per opt-in, show rate or close rate.** The trade this claim already flags, fewer opt-ins for better ones, is still unpriced by anyone.

He adds one axis this claim did not carry, for sales rather than lead campaigns: switch the ad set from maximise number of conversions to **maximise value of conversions** once the account has conversion history, on the same logic that equal-valued conversions push delivery toward the cheapest buyers. That is the middle rung of the ladder already banked at [[Auction Mechanics & Bidding#AU-052|AU-052]], arriving from a second source and applied to the same signal-quality argument rather than to scaling.
""")

amend("GA", "GA-043", """
**Re-checked 2026-09-24 against Google's newest reporting release, and the gap is still open.** Google announced a "single, unified view of the Search ads journey" for AI Max, showing the triggering search term, the creative assets the user saw and the landing page they reached, with availability stated only as "later this year". **That is a within-Search attribution view and not a surface-level spend breakout**, so an account running broad match, PMax or AI Max still cannot state what share of its spend landed inside AI Overviews or AI Mode. Full record at [[Google Auction & Smart Bidding#GA-080|GA-080]]. Second adjacent-but-insufficient release in eight days, after [[Google PMax & Shopping#GP-047|GP-047]] on 2026-09-17.
""")

print("done")
