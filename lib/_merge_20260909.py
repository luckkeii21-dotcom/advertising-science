# -*- coding: utf-8 -*-
"""2026-09-09 research merge: Meta ad-set placement/platform/device/OS exclusion withdrawal."""
from pathlib import Path

SCI = Path(r"E:\claude code marketing skill\Obsidian God-level Marketing Vault\God-level Marketing\wiki\science")


def load(name):
    raw = (SCI / name).read_bytes()
    bom = raw.startswith(b"\xef\xbb\xbf")
    return raw.decode("utf-8-sig"), bom


def save(name, text, bom):
    data = text.encode("utf-8")
    if bom:
        data = b"\xef\xbb\xbf" + data
    (SCI / name).write_bytes(data)


def amend(text, claim_id, addition, newdate):
    """Insert `addition` just before the Sources: line of the claim, and bump Last touched."""
    start = text.index("\n### " + claim_id + " ")
    nxt = text.find("\n### ", start + 1)
    if nxt == -1:
        nxt = len(text)
    block = text[start:nxt]
    src = block.rindex("\nSources:")
    block2 = block[:src] + "\n" + addition.rstrip() + block[src:]
    lt = block2.rindex("\nLast touched: ")
    end = block2.index("\n", lt + 1)
    block2 = block2[:lt] + "\nLast touched: " + newdate + block2[end:]
    return text[:start] + block2 + text[nxt:]


# ---------------------------------------------------------------- Meta Delivery
md, md_bom = load("Meta Delivery & Andromeda.md")

MD_NEW = """
### MD-150 - Meta is withdrawing ad-set exclusions for placements, platforms, devices and operating systems. The notice is live in the product, Meta has announced nothing, and the controls were still fully present in the account we read on 2026-09-09
Tier: T1 · Status: active
T1 covers the notice wording and the surfaces only, on the [[Auction Mechanics & Bidding#AU-076|AU-076]] precedent that Meta product copy read off the screen counts as documentation. **Every statement about the rollout is T3 and is marked below.**

**Meta's notice, verbatim, as it appears inside the Placements section of an ad set:** "Excluding placements, platforms, devices and operating systems will no longer be available for your ad sets."

**Four controls go, and three of them are easy to miss because the headline reads as being about placements alone.**
1. Individual placements can no longer be switched off. This is the one advertisers have used for years and it will take all the attention.
2. Whole platforms can no longer be excluded, so an Instagram-only or Facebook-only build stops existing at ad-set level.
3. Delivery can no longer be limited to mobile or to desktop.
4. Delivery can no longer be limited by mobile operating system.

**⚠ Do not quote a date and do not tell a client this has happened to their account. Meta has published nothing.** As of the trade coverage on 2026-08-25 there was no Meta announcement and the Business Help Centre still described manual placement selection as available. Jon Loomer, whose post carries the verbatim notice and is dated 2026-08-24, says the same in his own words: "Nothing is official until it's documented in an announcement or found on Meta's official pages." Advertisers began reporting the in-product notice around 2026-08-19.

**Loomer's unofficial scope, T3, and he labels it unofficial himself.** It is a test with plans to expand. Sensitive verticals are excluded, which he reads as special ad categories and possibly health and wellness. Eligible accounts must have the new multimedia workflow in ad creation, which is his explanation for why most advertisers are not seeing it. **It applies only to Sales and Leads objectives, with full placement control retained on every other objective.** More placement options are being added to placement value rules, which currently expose only seven.

**Ben Heath states it far harder than the evidence supports, and the gap is worth recording.** On 2026-09-08 he says it is going "across the board in ad accounts very soon" and "may have already happened in your ad account", with no scope, no objective limit and no test framing anywhere in an 18-minute video. He never mentions that Meta has announced nothing. **Loomer's hedged version and the trade reporting agree with each other and disagree with him.** Read Heath for the mechanics, which he demonstrates on screen, and not for the rollout status.

**OUR OWN READ, 2026-09-09, and the honest answer is that it has not arrived where we could look.** Ad account 645682541775849, ad set editor opened on a Leads objective (an Advantage+ leads campaign) and on an Awareness objective as a control. **Both still carry a full Placements section.** Expanded, the Leads ad set shows every control the notice says is going: **Devices and operating systems: All. Platforms: Facebook, Instagram and Audience Network. Placement controls: Included 17, Allowed with limited spend 0, Excluded 0. Skippable ads: Included.**
**⚠ Scope limits, and they are large enough that this settles nothing about our clients.** One account, INR-billed, campaigns in draft rather than live, and it is the least representative account we have. The informative test is a live US client account running a manual Sales or Leads campaign, which is SJR Commercial or Phoenix Truxx; the chiropractic accounts are the wrong instrument because Loomer's scope note puts health and wellness among the excluded verticals. **Absence in one account is exactly what a partial rollout predicts, so this observation cannot argue against the change, only date our own exposure.**

**Two details from that read that are new to this codex.** Placement state is not binary: the UI counts **Included, Allowed with limited spend, and Excluded** as three separate buckets, which is where the up-to-5%-of-budget-to-excluded-placements setting Loomer describes actually lives. And **Skippable ads is its own included/excluded control**, which no claim here has ever named. The account shows **17 placements**, against the 21 options Heath counts, so the inventory count is account-dependent and neither number should be quoted as the platform total.

**What this does to advice already banked.** [[Meta Delivery & Andromeda#MD-016|MD-016]] is a recipe for excluding junk placements at ad-set level and its execution route is the thing being withdrawn. [[Scaling Models#SC-149|SC-149]] already held that bidding down should come before excluding; the platform is now enforcing that ordering rather than leaving it to judgement, which is the rare case of a contested operating argument being settled by the surface disappearing underneath one side of it.
Sources: Jon Loomer, Meta Is Removing Placement Controls From Ad Sets, last updated 2026-08-24 (carries Meta's in-product notice verbatim); Ben Heath, HUGE Facebook Ads Option Just Disappeared!, 2026-09-08; PPC Land, Some Meta advertisers lose placement controls, with bid cuts capped at 90%, 2026-08 (reports no Meta announcement and Help Centre unchanged as of 2026-08-25); our own read of ad account 645682541775849, 2026-09-09
Last touched: 2026-09-09

### MD-151 - The replacement for placement exclusion is value rules plus an account-wide control, and between them they cannot do what the ad-set exclusion did
Tier: T1 · Status: active
T1 for the surfaces, their capacity and their limits, all of which are read off Ads Manager by two operators independently and confirmed on our own account. Nothing here measures performance.

**Lever one, placement value rules, and it is a bid multiplier rather than a switch.** Set a bid decrease on a placement, up to the platform maximum of 90%. **A 90% cut suppresses delivery and never eliminates it.** Heath is straight about the mechanism, that undercutting the bid means other advertisers win the impression instead, and his own words are "very very few of your ads are going to be shown", not none. The trade reporting states the same limit flatly: no placement can be switched off completely. **This is the sentence to give a client who asks for Audience Network off after the change: it can be made expensive, it cannot be made impossible.**

**Three holes in that lever, all of them Loomer's, all of them checkable in the UI.**
1. **Only seven placements are eligible for a value rule**, against 17 to 21 selectable in the ad set. More are said to be coming.
2. **There is no value rule for PLATFORM at all.** The nearest build is bidding down the placements belonging to a platform one at a time, which is an approximation and not the control.
3. **Rule sets do not apply themselves.** Creating one changes nothing until it is attached to an ad set, and it must be attached ad set by ad set. Already banked as the trap at [[Auction Mechanics & Bidding#AU-076|AU-076]] and it matters more now that this is the main lever.

**Lever two, account-level Placement Controls, and it is the only true off switch left.** Path is Advertising Settings, Account Controls, Placement Controls, then declare that the business can only advertise on specific placements and uncheck the rest. **It is account-wide**, so it cannot differ between two clients or two offers sharing an account, and the selectable set is narrower than what the ad set used to offer. Heath's own read of its durability is a guess and is worth carrying as one: "I think there's a decent chance that Meta takes away the ability for you to do this as well."

**Where the ad set now points.** On our 2026-09-09 read the Placements section leads with **Placement value rules** and **Account controls: Excluded placements: None** before the manual controls, which sit behind a Show more settings disclosure. The replacement architecture is already the front of the panel in an account that has not received the change.

**The operating rule this leaves, and [[Scaling Models#SC-149|SC-149]] already had it right.** Under conversion optimisation Loomer's position is that you should rarely need a placement value rule at all, because a placement is not a plausible source of cheap low-quality purchases. The real exposure is upper-funnel goals, where cheap junk inventory satisfies the goal: link clicks and landing-page views on Audience Network, and ThruPlay on **Audience Network Rewarded Video**, where third-party apps pay users in virtual currency to watch. His stated remedy for those is to stop using the goal rather than to fix the placement, since "you're still bound to get cheap, low-quality optimized actions from other placements". **Heath arrives at the same place from the other side:** if a traffic, engagement or awareness campaign can be rebuilt as Sales or Leads, do that first, because it removes the need for the control that is going away. Note the objective irony, which neither of them states: on Loomer's own scope note the change spares exactly the objectives that need placement control most and removes it from the two that need it least.
Sources: Jon Loomer, Meta Is Removing Placement Controls From Ad Sets, last updated 2026-08-24; Ben Heath, HUGE Facebook Ads Option Just Disappeared!, 2026-09-08; PPC Land, Some Meta advertisers lose placement controls, with bid cuts capped at 90%, 2026-08; our own read of ad account 645682541775849, 2026-09-09
Last touched: 2026-09-09
"""

md = md.rstrip("\n") + "\n" + MD_NEW

MD016_ADD = """**⚠ 2026-09-09: the ad-set execution route for this entire claim is being withdrawn by Meta.** [[Meta Delivery & Andromeda#MD-150|MD-150]] carries Meta's in-product notice that excluding placements, platforms, devices and operating systems will no longer be available at ad-set level. **Nothing here is refuted.** The argument between Shiver's exclusion recipe, Charley T's under-0.1%-of-budget rebuttal and Piliero's trim-on-your-own-data policy is untouched on the merits, and it was never settled by evidence anyway. What changes is that on an affected ad set the recipe becomes unbuildable, and the surviving forms are a bid-down value rule, which suppresses without eliminating, or an account-wide exclusion that applies to every campaign in the account. **The resolving read this claim has always asked for, pulling the placement breakdown on our own accounts, is now time-sensitive: the breakdown stays available after the control goes, so anyone who wants a record of what the excluded placements were actually costing should take it before the change lands.**"""

md = amend(md, "MD-016", MD016_ADD, "2026-09-09")
save("Meta Delivery & Andromeda.md", md, md_bom)
print("MD written: MD-150, MD-151; MD-016 amended")

# ---------------------------------------------------------------- Scaling Models
sc, sc_bom = load("Scaling Models.md")
SC149_ADD = """**2026-09-09: the platform is about to enforce the ordering rule this claim recommends, and the same source supplied the enforcement.** Loomer's "prioritize using value rules first before removing a placement entirely" was operator judgement when it was banked. Meta's in-product notice at [[Meta Delivery & Andromeda#MD-150|MD-150]] withdraws ad-set placement, platform, device and operating-system exclusion, which leaves the value rule as the only ad-set-level lever and makes the ordering compulsory rather than advised.
**Two additions to the substance, both from his 2026-08-24 post on the change.** The upper-funnel exposure gets named precisely: link clicks and landing-page views should watch **Audience Network**, and ThruPlay should watch **Audience Network Rewarded Video**, where third-party apps pay users in virtual currency to watch video. And he now argues the fix is to abandon the goal rather than prune the placement, because "you're still bound to get cheap, low-quality optimized actions from other placements". **On the conversion side he goes further than this claim recorded:** "You should rarely need to use value rules to adjust bids by placement when using a performance goal that maximizes the number or value of conversions", with "do not apply value rules universally" attached. So under conversion optimisation the correct action after the change is still nothing.
**The limit that stops this being a clean substitution, from [[Meta Delivery & Andromeda#MD-151|MD-151]]:** the 90% maximum bid decrease suppresses delivery and cannot switch a placement off, and only seven placements are eligible for a value rule at all. The soft version of the hard exclusion is genuinely softer."""
sc = amend(sc, "SC-149", SC149_ADD, "2026-09-09")
save("Scaling Models.md", sc, sc_bom)
print("SC-149 amended")

# ---------------------------------------------------------------- Auction
au, au_bom = load("Auction Mechanics & Bidding.md")
AU076_ADD = """**Three limits on the placement criterion, added 2026-09-09, and they matter far more now that placement value rules are becoming the main ad-set lever ([[Meta Delivery & Andromeda#MD-150|MD-150]]).** First, **only seven placements are eligible for a value rule**, against 17 to 21 selectable in the ad set itself, with more said to be coming. Both Loomer and Heath count seven independently. Second, **there is no value-rule criterion for PLATFORM**, so an Instagram-only or Facebook-only intent has to be approximated by bidding down that platform's placements one at a time. Third, the trap already recorded here, that a rule set does nothing until it is attached, now bites harder: attachment is per ad set, so a placement policy that used to be one ad-set setting becomes a rule set plus one attachment per ad set.
**And the 90% maximum is a suppression floor, not an off switch.** Heath's own description of the mechanism is that undercutting the bid lets other advertisers win the impression, and his words are "very very few of your ads are going to be shown". Trade reporting states it flatly: no placement can be switched off completely."""
au = amend(au, "AU-076", AU076_ADD, "2026-09-09")

AU019_ADD = """**⚠ The phrase "up to the 90% maximum for effective exclusion" in this claim's own title overstates what a 90% bid decrease does, and the correction now matters. Added 2026-09-09.** A 90% decrease suppresses delivery; it never eliminates it. Heath states the mechanism plainly, that the bid is undercut so far that other advertisers win the impression instead, and his own words are "very very few of your ads are going to be shown", not none. Shiver's "essentially saying, don't serve these people any ads" is the same overstatement in the other direction. **Read "effective exclusion" as "deep suppression at an unmeasured residual rate", because nobody on the roster has published what share of delivery survives a 90% cut.**
**Why this stopped being pedantic.** With ad-set placement, platform, device and operating-system exclusion being withdrawn ([[Meta Delivery & Andromeda#MD-150|MD-150]]), the bid-down rule is becoming the only ad-set lever rather than the preferred one, so a client told that Audience Network is "excluded" by a 90% rule has been told something false. The honest sentence is that it can be made expensive and cannot be made impossible. The reversibility argument in this claim is unaffected and is still the reason to prefer the rule on demographics."""
au = amend(au, "AU-019", AU019_ADD, "2026-09-09")
save("Auction Mechanics & Bidding.md", au, au_bom)
print("AU-076, AU-019 amended")

# ---------------------------------------------------------------- Learning & Signal
ls, ls_bom = load("Learning & Signal.md")
LS076 = """
### LS-076 - Meta shipped a personal AI agent and stated in the launch post that its conversations and data do not reach the ad systems, so the largest new Meta surface of 2026 supplies no targeting signal
Tier: T1 · Status: active
Meta Newsroom, 2026-09-08, launching Muse. The whole claim is one sentence in the post: **"Muse doesn't share a person's conversations or the data in their VM with Meta's ad systems."** The post carries no other advertising content, no ad product, no placement and no advertiser-facing feature.
**Why a negative is worth an ID.** Every claim in this file about signal supply assumes new Meta surfaces eventually become both inventory and input. This is Meta drawing that boundary explicitly at launch on a surface designed to hold long personal conversations, which would be the richest intent data the company has ever collected. It is the counterexample to the assumption, and it is the kind of statement that gets quietly revised, so it is banked with its date attached so a future change is visible as a change rather than read as new information.
**What it does not say, and the limits are the useful part.** It says nothing about whether Muse becomes an ad placement later, nothing about aggregate or derived signals, and nothing about any other Meta AI surface. **A stated policy at launch is not an architecture.** Treat this as a dated commitment to check again, never as a permanent property of the system, and never quote it to a client as a privacy guarantee.
Sources: Meta Newsroom, Introducing Muse: The World's First Personal AI Agent Built for Everyone, 2026-09-08
Last touched: 2026-09-09
"""
ls = ls.rstrip("\n") + "\n" + LS076
save("Learning & Signal.md", ls, ls_bom)
print("LS-076 written")
