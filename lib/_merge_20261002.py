# -*- coding: utf-8 -*-
"""Codex merge, research run 2026-10-02.

New:    GA-091, GA-092 (Google Auction & Smart Bidding), CR-283 (Creative Science),
        MM-225 (Marketing Math & Unit Economics)
Amend:  GA-066, GA-068, MM-011, MM-074

Sources read in full today:
  - Google Ads, "Demand Gen campaign creative, explained: asset variety, testing,
    and fatigue", Ads Decoded S2E5, 2026-10-01, yz-ui2LSMtQ, 19:47, 3,049 words
  - blog.google/products/ads-commerce/creating-assets-youtube-ads/, 2026-10-01
  - Andrew Faris, "Their Business Doubled But Their Supply Chain Wasn't Ready.",
    2026-10-02, DlIbUPnfF9s, 36 min, 6,928 words (DISCLOSED SPONSORED EPISODE)
"""
from pathlib import Path

SCI = Path(r"E:\claude code marketing skill\Obsidian God-level Marketing Vault\God-level Marketing\wiki\science")
GA = SCI / "Google Auction & Smart Bidding.md"
CR = SCI / "Creative Science.md"
MM = SCI / "Marketing Math & Unit Economics.md"


def read(p):
    return p.read_text(encoding="utf-8")


def write(p, s):
    p.write_text(s, encoding="utf-8")


def replace_once(text, old, new, label):
    n = text.count(old)
    assert n == 1, "%s: expected 1 anchor, found %d" % (label, n)
    return text.replace(old, new)


GA_NEW = """
### GA-091 \u00b7 Demand Gen explores your creative only as far as the budget stretches, so Google's own PM prescribes asset QUALITY over volume and names budget-per-asset as the governing quantity
Tier: T1 \u00b7 Status: active
Alejandro Osio, a Google product manager for Demand Gen and YouTube performance ads, on Google's own Ads Decoded podcast. This is the first statement in the codex from the platform side on why a large creative pool can fail to get tested, and it runs the opposite direction to the Meta-side volume doctrine.

**The mechanism, in his words.** "The more assets you have in your campaign, the more time and budget you likely need to reach a clear conclusion." The constraint is not a cap on how many assets you may upload, it is that exploration competes with delivery: with a large pool "the system's not feasibly gonna be able to explore all of those assets quickly, **since its primary objective is to deliver performance against your set goals**." The governing quantity he names is budget per asset: "the larger your budget per asset, the better positioned your campaign is to more quickly and completely test all the creatives you've provided."

**His worked case, and the budget floor inside it.** He sets up a Demand Gen campaign at **$100 a day, which he calls "bare minimum best practice"**, then adds "tens of thousands of non-feeded images and videos" and says the system cannot work through them. He flags it himself as a deliberately extreme illustration. The $100/day figure is the first dollar floor for Demand Gen on file here; the conversion-count eligibility floor of roughly 50 in 35 days is already recorded in this note under target ROAS.

**The retail-feed carve-out, which is the part most likely to be misapplied.** He says "non-feeded" twice and explains why: "if you have a retail feed, we're dealing with much larger volumes and our systems are built for that." **So the volume ceiling described here applies to manually uploaded images and videos, not to feed-driven assets.** A retail advertiser reading this claim as a cap on catalogue size would be reading it wrong.

**His prescription for refreshing a live campaign**, which follows from the same mechanism: make creative changes gradually, and keep the top-performing highest-traffic assets running while new ones are added, "because this helps keep performance stable while the system ramps up on any new inputs you've added."

**Google's own host flags the divergence from Search, unprompted.** Ginny Marvin: "that's very helpful and a little bit different than where things are in terms of recommendations on the search side." Worth holding onto, because it means Google is not claiming one creative-volume doctrine across its own surfaces.

**Read it against the Meta side, where it cuts the other way.** [[Creative Science#CR-001|CR-001]] holds that Meta built Andromeda explicitly to absorb rapidly growing creative volume, and [[Creative Science#CR-026|CR-026]] holds the raw-volume-versus-multiplying-winners question. **Nothing here refutes those: they are statements about a different auction, and Osio is describing a budget-rationed exploration problem rather than a modelling limit.** The transferable operating line is that creative volume has to be funded per asset on Demand Gen, and an operator porting a Meta-style upload of 50 assets onto a $100/day Demand Gen campaign has bought a test the budget cannot finish.

**Tier discipline.** T1 for what Google says its own system prioritises and prescribes. **No data of any kind is shown**: no exploration curve, no time-to-conclusion by pool size, no definition of "clear conclusion", and no number attached to "budget per asset". The extreme example is explicitly hypothetical. Treat the mechanism as platform-stated and the sizing as unquantified.
Sources: Google Ads, Demand Gen campaign creative, explained: asset variety, testing, and fatigue, Ads Decoded S2E5, 2026-10-01, youtube.com/watch?v=yz-ui2LSMtQ, 19:47, 3,049 words, transcript read in full; Google Ads & Commerce Blog, Turn your existing social assets into high-impact YouTube ads, 2026-10-01
Last touched: 2026-10-02

### GA-092 \u00b7 Ad Strength on Demand Gen measures INVENTORY COVERAGE, not ad quality, and Google's stated floor is good with excellent preferred
Tier: T1 \u00b7 Status: active
The codex has carried no entry on Ad Strength at all. Osio defines it for Demand Gen and the definition is narrower than the name suggests: "**think of it as just your indicator to understand if your ad is covering the breadth of inventory that Demand Gen offers.**" Ginny Marvin presses the point deliberately, saying advertisers ask what it actually indicates, and he confirms it reads asset variety and that it works the same way as on Search.

**The stated target, twice in one episode:** "aim to achieve at least good if not excellent ad strength across all of your Demand Gen ads", and again in his closing checklist.

**What covering the breadth means in practice, as he lists it:** images and videos across horizontal, vertical and square aspect ratios, for both image and video assets.

**Why the distinction is worth banking rather than the score.** A diagnostic that reports whether you have supplied enough shapes to serve every placement is not a diagnostic that reports whether the creative is any good. An account can hold excellent Ad Strength on assets nobody responds to, and a strong single-format creative set will score poorly for a reason that has nothing to do with the work. **Report it to a client as placement coverage, never as a quality grade.** This is the same reading discipline [[Google Auction & Smart Bidding#GA-009|GA-009]] applies to expected asset impact in Ad Rank.

**Unevidenced, and stated as such.** No correlation between Ad Strength and outcome is offered anywhere in the episode. The instruction to reach excellent is a Google recommendation with nothing shown behind it.
Sources: Google Ads, Demand Gen campaign creative, explained: asset variety, testing, and fatigue, Ads Decoded S2E5, 2026-10-01, youtube.com/watch?v=yz-ui2LSMtQ, transcript read in full
Last touched: 2026-10-02
"""

CR_NEW = """
### CR-283 \u00b7 Google looked at its own data and refuses to publish an asset-refresh cadence for Demand Gen, recommending AGAINST any blanket rule; the replacement is add-do-not-remove until the ad is at capacity
Tier: T1 \u00b7 Status: active
A platform declining to answer the question operators ask most, with the reason given, which makes it more useful than most answers would have been.

**The refusal, in Osio's words.** "As much as I'd love to be able to give a definitive number, **when we look at the data, we find that the answer is really that it depends**." The named dependencies: the type of asset, the inventory it is serving on, and the particular behaviours of the audience. His instruction follows directly: "**I would actually recommend against setting a blanket rule for your business on how frequently to replace assets.**"

**What he gives instead is a per-asset read, not a calendar.** Open asset reporting and compare an asset against **its own start**, not against the other assets: "is there a declining trend relative to when you first added that asset... if you see that it is markedly declining relative to how it was performing when it was fresh, that's a good indication that it is a stronger candidate to consider swapping out."

**The decision rule, and it is the operationally new part.** Decline alone does not justify removal. "It's generally better to keep it in if it is still showing strong serving in traffic", and "**the only time where it makes sense to actively remove or replace assets is if you're already at capacity within your Demand Gen ad AND a specific asset has shown a significant decline in performance relative to its start.**" Both conditions, together. Where there is room in the ad, the prescribed move is to add the new asset and leave the old one running.

**Why this belongs next to the fatigue claims rather than in a settings note.** [[Creative Science#CR-028|CR-028]] carries fatigue as embedding-cluster saturation and [[Creative Science#CR-029|CR-029]] carries the open question of whether iterating around the fatigue point extends or ends a winner. **Google is saying, from inside the system, that the fatigue point is not a property of the asset or of elapsed time, it is a joint property of the asset, the inventory and the audience, so no cadence can be right in general.** That is consistent with CR-028's mechanism and it kills the "refresh every N days" rule for this channel specifically.

**Carries directly into our own retainers.** Any creative calendar built on a fixed replacement cadence for Demand Gen is unsupported by the platform that runs it. The replacement is a weekly read of asset reporting against each asset's own baseline, plus an add-first default.

**The guard.** Nothing is shown. No distribution of asset lifespans, no definition of "markedly declining", no capacity number for a Demand Gen ad, and no evidence that add-first beats replace-first. This is Google's stated recommendation, not a measured result, and it is also the answer that keeps the most assets in the auction.
Sources: Google Ads, Demand Gen campaign creative, explained: asset variety, testing, and fatigue, Ads Decoded S2E5, 2026-10-01, youtube.com/watch?v=yz-ui2LSMtQ, transcript read in full
Last touched: 2026-10-02
"""

MM_NEW = """
### MM-225 \u00b7 Set the sales-velocity window by how fast the SKU moves, short for fast movers and long for slow ones, because one averaging window across the catalogue stocks you out of exactly the products the ads are working on
Tier: T3 \u00b7 Status: active
**Read the sourcing note at the bottom before quoting any number here. This is a disclosed sponsored episode and the guest is a client of the sponsor.**

[[Marketing Math & Unit Economics#MM-076|MM-076]] says to allocate budget by days of inventory rather than by ROAS, and assumes days of inventory is a number you have. This is the layer underneath it: how the number gets computed, and the finding is that the averaging window itself has to vary by tier.

**The operator's statement of the problem:** "averages will kill you." Joel Taylor, director of supply chain at Reformation Heritage Books, after the business went out of stock on its top sellers.

**The spec they run, stated in full.**

| Tier | Safety stock | Sales-velocity window |
|---|---|---|
| A and hero | 180 days | **30 days** |
| B | 90 days | longer, up to a year on some |
| C | 60 days | ~365 days |

**The reasoning, which is the transferable part.** A fast mover is volatile and can clear in days off one promotion, so it needs a short window that catches the acceleration while there is still time to reorder: "you could do a sale and it could sell out super quick." A slow mover carries the opposite risk, so a long window smooths the noise and stops a single good week triggering an order that ties up cash. The stated goal is "profitable in stock": deliberately overstocked on fast movers, deliberately not on slow ones.

**The tiering key is two-dimensional, and the reason matters for any wide-AOV catalogue.** A and B and C are assigned on revenue contribution **and** sales velocity together, Pareto-ranked, because a $300 set and a $10 book with the same order velocity are not the same product to the business. A catalogue with a wide price range will mis-tier on either axis alone.

**Why this sits in the advertising codex.** The products a short window protects are precisely the ones paid media is currently working, so the window length decides whether a winning ad runs into a stockout. It is the inventory-side twin of [[Creative Science#CR-133|CR-133]], which briefs multi-product assets so a stockout does not kill the ad.

**Tier discipline, and it is the whole caveat.** This is one operator describing a system a vendor built for him, on a **disclosed sponsored episode** for that vendor, with the host stating the sponsorship at the top. The day counts are his current policy and he describes them as still being revised ("we're even learning this past couple weeks"). **No before-and-after on stockout rate, no inventory-turn figure, and no control.** Bank the mechanism, which is checkable on any account, and do not repeat 180/90/60 as a benchmark.
Sources: Andrew Faris, Their Business Doubled But Their Supply Chain Wasn't Ready. So They Did This., 2026-10-02, youtube.com/watch?v=DlIbUPnfF9s, 36 min, 6,928 words, transcript read in full. DISCLOSED SPONSORED EPISODE for Move Supply Chain; the guest, Joel Taylor of Reformation Heritage Books, is a client of the sponsor
Last touched: 2026-10-02
"""

GA068_AMEND = """**Amended 2026-10-02: the multimodal video feature is named, and it is Gemini Omni's first appearance in Google Ads.** The Demand Gen PM, on Google's own podcast: "this is actually the **first time Gemini Omni has made it into Google Ads**", in Asset Studio's multimodal video creation, taking existing creatives plus a URL as inputs. The flow is prompt-based and the storyboard is editable scene by scene, so the operator keeps per-scene control rather than accepting a single generated output. His own usage advice is "quality in, quality out", and to prompt it the way you would brief a creative production team. Two further items from the same episode: **shareable preview links** now exist, so Demand Gen ads can be sent to a client or a brand team for approval before they run, which is the missing piece for any account with a real brand-approval step; and the full asset-optimisation list is video generation, video shortening, video resizing, adaptive layout for images (square extruded to vertical), landing-page previews, animated images in beta, and generated text. **Every one of those writes creative after our review**, which is the same compliance exposure recorded against Meta's creative enhancements and against Google's auto-generated Display assets at [[Google Auction & Smart Bidding#GA-066|GA-066]]. He confirms the generated variants can be reviewed in asset reporting and paused individually. No performance figure is attached to any of it.
"""

GA066_AMEND = """**Amended 2026-10-02 with the platform-side confirmation, and with where to READ the expansion.** GA-066 was banked off a practitioner reading the UI panel. Google's own Demand Gen product manager now states the same thing on Google's podcast, with three details the original entry could not supply. **One, the default is confirmed from the platform side: optimised targeting "is on by default in Demand Gen campaigns and can be managed at the ad group level."** Two, the inputs are named: it uses the campaign's conversion data plus the audience segments, custom segments and customer-data segments you provided, "to find additional people who are predicted to convert", and audience exclusions can be set against it. **Three, and this is what makes the five-minute check above actionable: the expansion traffic is reported in the "total expansion and optimised targeting" row of the account.** So the leak this claim warns about is measurable rather than inferred, and any of our Google campaigns built to hit one uploaded list can be read for it directly instead of being argued about. Note the PM presents it as a recommended launch step for new Demand Gen advertisers, which is the opposite of the practitioner's "turn that off" above; both positions stay recorded and the row named here is how an account settles it.
"""

MM074_AMEND = """**Amended 2026-10-02 with a worked case where the same scaling failure happened WITHOUT the cash mechanism, which narrows what MM-074 is actually about.** Reformation Heritage Books, a legacy Christian publisher running the Faris playbook (manual bids on Meta, high creative volume, message-first), grew **two to three times year over year through the 2025 holiday depending on the month**, and **went out of stock on its top sellers at the start of 2026**. That is this claim's failure arriving on schedule. **The cash lever was not the binding one**: the business runs 60 to 70 points of gross margin on direct sales (stated from memory, not read off a document), and carries donation income alongside the trade. Their director of supply chain names the actual constraint as visibility: "our biggest problem was we didn't have any visibility into our inventory from a stockout perspective, our sales velocity perspective." **So the mechanism generalises past the cash conversion cycle: scaling paid media relocates the bottleneck downstream, and the new bottleneck is whichever supply capability was never built, which may be cash, lead time, or simply knowing what is selling.** His own framing of the pattern is the cleanest line in the episode: "whenever you expand a bottleneck, give it more capacity, that creates bottlenecks down the road." The remedies they ran are at [[Marketing Math & Unit Economics#MM-225|MM-225]] (tier-segmented velocity windows and safety stock). **The recovery number must not be read as an effect size.** They report a **75% year-over-year growth rate** after the work, and the same speaker immediately attributes it to both halves at once: "that's the full picture of both the improvement in the marketing and then being able to catch those big sales moments by having supply at the ready." Self-reported, on a disclosed sponsored episode for the vendor that did the supply-chain work, with no control.
"""

MM011_AMEND = """**Amended 2026-10-02, a second named instance on the same channel.** Reformation Heritage Books moved printing of its larger works to an international printer, R.R. Donnelley, sourced for them by an outside supply-chain team, and their director of supply chain calls international sourcing "probably going to be our biggest profit lever in the coming year", ahead of anything in the ad account. The saving is described only as "a small percentage of what it used to be", **with no landed-margin figure on either side**, so it corroborates the direction of MM-011 and adds nothing to its sizing. Two mechanics worth carrying: higher order quantities buy a better unit cost, so better inventory visibility feeds the margin lever as well as the stockout one, and the second-source discipline here is to hold **approved print samples with backup manufacturers you have never ordered from**, because a disruption upstream of your vendor (they lost a paper mill to a tornado) stops production at a supplier who is otherwise fine. Disclosed sponsored episode for the supply-chain vendor; the guest is that vendor's client.
"""


def main():
    t = read(GA)
    t = t.rstrip("\n") + "\n" + GA_NEW
    t = replace_once(
        t,
        "Sources: Google Ads & Commerce Blog, Reach your audience in new ways with August\u2019s Demand Gen Drop, 2026-08-27\nLast touched: 2026-09-25",
        GA068_AMEND
        + "Sources: Google Ads & Commerce Blog, Reach your audience in new ways with August\u2019s Demand Gen Drop, 2026-08-27; Google Ads, Demand Gen campaign creative, explained, Ads Decoded S2E5, 2026-10-01\nLast touched: 2026-10-02",
        "GA-068")
    t = replace_once(
        t,
        "Sources: Blue Sense Digital, 2025-03-22 (Display Retargeting Strategy in Google Ads)\nLast touched: 2026-08-27",
        GA066_AMEND
        + "Sources: Blue Sense Digital, 2025-03-22 (Display Retargeting Strategy in Google Ads); Google Ads, Demand Gen campaign creative, explained, Ads Decoded S2E5, 2026-10-01\nLast touched: 2026-10-02",
        "GA-066")
    write(GA, t)

    t = read(CR)
    write(CR, t.rstrip("\n") + "\n" + CR_NEW)

    t = read(MM)
    t = t.rstrip("\n") + "\n" + MM_NEW
    t = replace_once(
        t,
        "Sources: Blue Sense Digital, How to Scale an eCommerce Brand Profitably in 2026: The Full System, 2026-06-15; Blue Sense Digital, Everything You Need to Know About Finance in eCommerce, 2026-05-04; Blue Sense Digital, Why eCommerce Is So Difficult (Deep Dive), 2025-01-23\nLast touched: 2026-09-05",
        MM074_AMEND
        + "Sources: Blue Sense Digital, How to Scale an eCommerce Brand Profitably in 2026: The Full System, 2026-06-15; Blue Sense Digital, Everything You Need to Know About Finance in eCommerce, 2026-05-04; Blue Sense Digital, Why eCommerce Is So Difficult (Deep Dive), 2025-01-23; Andrew Faris, Their Business Doubled But Their Supply Chain Wasn't Ready., 2026-10-02 (sponsored)\nLast touched: 2026-10-02",
        "MM-074")
    t = replace_once(
        t,
        "Sources: Andrew Faris, You're Working Hard On The Wrong Problem. Here's How To Tell., 2026-07-27\nLast touched: 2026-08-18",
        MM011_AMEND
        + "Sources: Andrew Faris, You're Working Hard On The Wrong Problem. Here's How To Tell., 2026-07-27; Andrew Faris, Their Business Doubled But Their Supply Chain Wasn't Ready., 2026-10-02 (sponsored)\nLast touched: 2026-10-02",
        "MM-011")
    write(MM, t)

    for p in (GA, CR, MM):
        print("ok", p.name, len(read(p)), "chars")


if __name__ == "__main__":
    main()
