# -*- coding: utf-8 -*-
"""2026-09-16 research merge. 6 new claims, 5 amendments."""
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

SCI = Path(r"E:\claude code marketing skill\Obsidian God-level Marketing Vault"
           r"\God-level Marketing\wiki\science")
TODAY = "2026-09-16"

META1 = ("Meta Newsroom, Introducing Meta One: A Subscription Service With More "
         "Features and AI to Create, Connect, and Stand Out, 2026-09-15, "
         "https://about.fb.com/news/2026/09/introducing-meta-one-subscription-service-more-features-ai/")
BH = "Ben Heath, Breaking Meta Ads News! Meta One is here..., 2026-09-15"
MS_ANG = "Dr. Matt Shiver, How I use Ad Angles to Scale Call Funnels to $100k/mo, 2026-09-15"
MS_YT = "Dr. Matt Shiver, YouTube Ads vs Facebook Ads: Who Each One Is Actually For, 2026-09-15"
AF = ("Andrew Faris, The Death Of Supplements & What Taylor Holiday What Do Instead, "
      "2026-09-15 (Taylor Holiday speaking)")


def amend(fname, cid, body, source=None):
    p = SCI / fname
    txt = p.read_text(encoding="utf-8")
    m = re.search(r"^### " + re.escape(cid) + r" .*?(?=^### |\Z)", txt, re.S | re.M)
    if not m:
        print("MISS", cid)
        return False
    block = m.group(0)
    if body.strip()[:70] in block:
        print("SKIP (already present)", cid)
        return False
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


def add(fname, title_line, tier_line, body, sources):
    p = SCI / fname
    txt = p.read_text(encoding="utf-8")
    cid = title_line.split()[1]
    if re.search(r"^### " + re.escape(cid) + r"(?![0-9A-Za-z-])", txt, re.M):
        print("SKIP (exists)", cid)
        return False
    claim = (title_line.strip() + "\n" + tier_line.strip() + "\n"
             + body.strip() + "\nSources: " + "; ".join(sources)
             + "\nLast touched: " + TODAY)
    p.write_text(txt.rstrip("\n") + "\n\n" + claim + "\n", encoding="utf-8")
    print("ADDED", cid)
    return True


# ---------------- NEW CLAIMS ----------------

add("Meta Delivery & Andromeda.md",
    "### MD-157 \u00b7 Meta One went live globally on 2026-09-15 with four paid business tiers at $14.99, $49.99, $149 and $499 a month, and the brand is older than the launch",
    "Tier: T1 \u00b7 Status: active",
    """
Meta's own newsroom post is the source for every number here. Meta One is a subscription over Instagram, Facebook, WhatsApp and Meta AI, launching with "more than 50 features" and expanding to Edits and AI glasses later. The business and creator ladder is four tiers, each priced "starting at": **Essential $14.99/mo, Advanced $49.99/mo, Expert $149/mo, Max $499/mo.** A separate individual ladder runs Instagram Plus $3.99, WhatsApp Plus $2.99, Facebook Plus $3.99, Core $7.99 and Premium $19.99. **Plans are available globally from launch day**, which covers both our US client accounts and our own New Delhi egress.

**The brand is older than the launch, and the practitioner account of the same day gets this wrong.** Meta writes: "Earlier this year, we launched Meta One single product plans, Instagram Plus, Facebook Plus, and WhatsApp Plus". What shipped on 2026-09-15 is the bundle structure on top of those, including the business and creator tiers. Anyone describing Meta One as a product that did not exist before that date is describing the bundles rather than the brand.

**The features Meta itself names for the business tiers**, in Meta's words: an enhanced profile showing website, locations and what people say about you; a bold follow button on reels; follow invitations sent automatically to people who engage with your content; more access to Meta Business Agent for 24/7 customer replies; a verified badge, verified WhatsApp channel and impersonation protection "pending successful verification". At Advanced it adds scheduling stories up to 30 days ahead, **links in organic posts and reels**, exportable analytics, deeper audience insights, team access without password sharing, more linked devices and more WhatsApp business broadcast credits.

**Two limits on the pricing, both from Meta's own wording, and both easy to misquote.** Every business figure is "starting at", and Meta states that "plans, benefits, pricing, and availability may vary by region, by app, and by account". So no single price can be given to a client as their price without them opening the subscription flow on their own account. **A per-platform total circulating from the practitioner account, $45 a month for a verified badge across Instagram, Facebook and WhatsApp, is that operator's own arithmetic and appears nowhere in Meta's post.** Do not repeat it.

**Nothing Meta announced is a claim about ad delivery, ad cost or ad performance.** This is an organic, profile and support product sold to advertisers. The half with real advertiser consequence is at [[Meta Delivery & Andromeda#MD-158|MD-158]], and that half is T3 because Meta did not publish it.
""",
    [META1, BH])

add("Meta Delivery & Andromeda.md",
    "### MD-158 \u00b7 Human support and organic distribution are now things a business buys from Meta by subscription, and neither is in Meta's own Meta One announcement",
    "Tier: T3 \u00b7 Status: active",
    """
Everything here comes from one operator who spent two weeks on the Meta One Max beta and interviewed the Meta VP running the programme. **None of it appears in Meta's newsroom post at [[Meta Delivery & Andromeda#MD-157|MD-157]]**, so it is read off in-product plan pages by one person and carries no platform confirmation. That gap is itself the finding: the two features that change how an advertiser operates are the two Meta chose not to put in writing.

**Human support is metered and sold.** One support case per month at Advanced, five at Expert, unlimited at Max, on Instagram, Facebook or WhatsApp. His phrasing for what it is worth: "I think for most people that would be really really valuable. I think that alone may well be worth getting this if meta is important for your business." **The consequence for our own book is the wrongly disabled account.** Every client page or ad account taken down by an automated flag currently has no route to a person, and that is the exact situation this line item sells. Read it against [[Meta Delivery & Andromeda#MD-156|MD-156]], where two locales of the same policy page carried different section names on the same day: an appeal argued from the wrong locale is precisely the case a human support ticket exists to fix.

**Organic distribution is now purchasable, in four named forms.** Featured in feed on Facebook, described as "a dedicated carousel of meta one profiles that appears in people's feeds who may be interested in your business". Optimized search on Instagram and Facebook, ranking the profile higher in on-platform search results. Follow invitations sent automatically to anyone who engages with your content, Facebook only. A bolded follow button on reels, Facebook only.

**Two metering rules on the organic links decide whether the feature is usable at all.** They are not retroactive: a link cannot be added to a post or reel that is already published, however well it is still performing. They are not refundable: archiving a post that flopped does not return the credit. At Advanced the monthly allowance is 4 links in Instagram posts and 8 in Facebook posts, with the same again for reels; at Expert 8 and 20; at Max 12 and unlimited on Facebook.

**His recommendation is the Advanced tier for most advertisers**, on the grounds that the higher tiers mostly raise quantities rather than add features. He separates the two questions explicitly: "do I think this is a good idea and it should have introduced? Probably not... Am I willing to pay because I think it will give me a competitive advantage? Absolutely."

**The honest limit, and it is large.** Nobody has measured any of this. He says the feed carousel has not been seen in the wild because adoption is still too low to judge how often it serves, gives no figure for the follow-button lift and flags his own 50% example as imagined. There is no performance claim here, and a subscription is not a delivery lever.
""",
    [BH])

add("Learning & Signal.md",
    "### LS-080 \u00b7 A longer video ad qualifies the viewer before the call to action is heard, so script length is set by lead volume rather than by a best practice",
    "Tier: T3 \u00b7 Status: active",
    """
Stated as a flat rule: "Anytime the video ad is longer, you will have better quality with leads because they have to get through that before they hear your call to action." The mechanism is friction placed in the ASSET rather than in the form or the funnel, which is what makes it new here. Everyone who reaches the call to action has already spent the runtime, so runtime is a self-selection filter that costs nothing to build and needs no conditional logic.

**The operating rule is conditional on the account's current volume, which inverts the usual instinct to shorten everything.** Low lead volume, keep the script short: his worked case is the mistake angle cut down to a single mistake before the call to action. High lead volume, lengthen it: "If you're getting a ton of leads, we can add more friction by adding a longer script, aka more mistakes, in this example here, before we give the call to action." So an account drowning in unqualified opt-ins has a creative lever available before it touches the form, the offer or the optimisation event.

**Where it sits in the friction contest at [[Learning & Signal#LS-009|LS-009]].** That claim is entirely about qualification friction inside the FUNNEL, an application step or a pixel-conditioning question, and both poles of it argue over the form. This is a third surface neither pole names, and it is compatible with both: Heath can run zero form friction and still lengthen a script, Shiver can run a gated form and lengthen a script on top of it. It is also the cheapest of the three to reverse, because a shorter cut is an edit rather than a funnel change.

**Asserted, no data, and the obvious cost is not priced.** A longer script reaches fewer people and almost certainly costs more per opt-in, and he gives no figure for that trade at any runtime. Treat the direction as the claim and the size as unknown. The opposite-direction warning already on file, that a falling cost per lead is a quality warning, is at [[Learning & Signal#LS-043|LS-043]].
""",
    [MS_ANG])

add("Creative Science.md",
    "### CR-245 \u00b7 A creator's identity is irrelevant to the asset and an influencer's identity IS the asset, so the two are bought, briefed and measured differently",
    "Tier: T3 \u00b7 Status: active",
    """
Taylor Holiday's definition, and it is sharper than the one this codex has been carrying. "He's a creator because he makes videos, but when we say this, what we really mean is that the human's identity is irrelevant. Their identity in the asset creation is irrelevant. That's what you mean by creator." An influencer is the inverse: the reason the asset works is who is in it. His summary of what a creator actually sells is the useful half: "they distinguish themselves on their ability to make engaging content. It's not influence... they're algo wizards."

**This contradicts the definition sitting as a sub-point inside [[Creative Science#CR-054|CR-054]]**, where the stated difference between UGC and influencer is that the influencer carries a following, therefore costs more, and therefore buys more scroll-stopping power. That is a size-and-performance account. This is a mechanism account: you are buying identity transfer, and follower count is a proxy for it rather than the thing itself. Both operators are describing real purchases and neither has shown data, so carry both and name which one you are using.

**The worked example is the test.** A 391-mile ultra runner wearing a hat from a brand called Rapid, and the listener went to buy the hat and found it sold out. Holiday's reading: "his identity made me want to be a part of it". He then corrects himself on what was actually bought, which is the sharpest line in the segment: the desire was not to join the Rapid community, it was to join the runner community that Rapid signals membership of. **So the brand is buying a badge inside a community that already exists, and the influencer is the person who can confer it.**

**The deal-design rule, and it rejects the standard framing.** Asked whether an influencer buy should come out of a brand budget rather than a direct-response budget, he refuses the premise: "I would do everything I could to design the deal structure to offset the cost via direct response." Named mechanisms: build ad and email usage rights into the same shoot, use the person as a route into retail, and then take the halo on top. The failure mode he names is the pure asset buy, "all the creator wants is your money, all you want from them is the asset to make money, and none of you actually give a damn about each other", which he argues decays by construction because one side tires of being extracted from.

**Three more operating rules from the same segment.** First, on community: "go find a place where you can trade... I would try to become endemic to that community", stated against brands trying to build their own, which he calls a terrible idea at zero revenue. Second, on equity: give it at zero revenue only if the person supplies force to the business on an ongoing basis, and the named risk is that a slow-growing brand becomes uninteresting to them by year two; at $10M revenue and 10 to 20% profit, "I would give nobody equity in that business", pay cash instead. Third, on persistence: embed the person across every customer-facing surface rather than in a campaign, his examples being product photography and a named person on the customer service message, so the presence is continuous and no single ad has to carry the whole investment.

**Category dependence, stated as a limit on the whole claim.** It matters most in apparel and accessories, "where the thing you're wearing is essentially a commodity and the brand is the whole value", and least where the product's function is the purchase. Asserted throughout, across two operators in conversation, with no spend figures, no lift and no named brand outcome. This is a way of deciding what to buy, not evidence that it pays.
""",
    [AF])

add("Emerging Channels.md",
    "### EC-006 \u00b7 YouTube is a second channel rather than a first one: start on Meta, and add YouTube at roughly $30k to $50k a month of spend",
    "Tier: T3 \u00b7 Status: active",
    """
A named threshold, which this file has been short of: "most people should just start with Facebook and until you're spending, you know, 30, 40, maybe even 50k a month, I don't think it makes a ton of sense to get onto YouTube." He extends it into a business-stage rule, that YouTube earns its place for an advertiser aiming at $1M a month and not for one aiming at $100k to $200k a month, where the time is better spent getting better at the channel already running.

**His three reasons for Meta first are all operational rather than about reach.** The pixel is better, the data comes back faster so learning is quicker, and the interface is more usable, which he concedes is a low bar: "Meta is not the most user-friendly but I still think it's even more user-friendly than YouTube ads."

**The one asymmetry that favours YouTube is asset life, and it is the part worth carrying.** "You can set them and forget them and they last a lot longer." He ties it to the organic behaviour of each platform, where an Instagram or Facebook post dies within two days and a Meta ad lasts weeks to a couple of months, against YouTube organic and YouTube ads both lasting far longer. That makes creative fatigue a channel property rather than a universal, and it predicts that the creative-refresh cadence our Meta claims assume does not transfer. No retention curve is shown for either platform.

**Fit rule: YouTube suits mass-market B2C** (his examples are online weight loss and investing) and works for B2B only when the addressable market is large enough, "it's just a lot harder". **His own account is the honest footnote on the whole claim**: he spends $3,000 to $5,000 a month on YouTube, most of it retargeting people already watching his organic videos, at roughly $30 to $50 a day. So the operator giving the threshold is not himself running YouTube as an acquisition channel, and every figure here is asserted with no cost comparison shown.
""",
    [MS_YT])

add("Marketing Math & Unit Economics.md",
    "### MM-216 \u00b7 Where anyone can make the same claim there is no defensible cost of acquisition, and an LTV-to-CAC model built on the earliest cohorts overstates both halves at once",
    "Tier: T3 \u00b7 Status: active",
    """
Taylor Holiday on why supplement businesses are hard to make durable, and the argument generalises past supplements to any category with a low barrier to entry. "It is not about science creating a defensible CAC. There is no defensible CAC because there is no barrier to making claims." Research spend does not fix it, because the buyer cannot tell the difference: "Even if you spent $10 million researching your line to be true, if I can write the same line, the customer doesn't know the difference."

**That is a usable test for any positioning, including our own agency's.** If a competitor can put your sentence on their site tomorrow at zero cost, the sentence is not a position. He applies it to agencies by name: a service value proposition that is "a thing that somebody else can just write on their website too" is unprovable and indefensible however true it is.

**The modelling error is the operating half, and it is two errors compounding.** A lifetime-value-to-acquisition-cost model built at month 20 of a business is fitted to its earliest cohorts, which are its highest-value customers. The model then assumes next month's cohort behaves like the first month's. His objection is that **acquisition cost and retention degrade at the same time**, as competition enters and a form-factor shift moves demand elsewhere, so both sides of the ratio move against the forecast at once rather than one of them. His worked case is a competitor changing the form factor from powder to gummies and depressing every existing cohort six months out. "Anytime you're modeling anything far out to the future, the unknown unknown risk becomes larger."

**The live example, and it is the thing to watch rather than repeat.** He describes a named brand taking a billion-dollar debt facility from a venture fund that exists specifically to fund customer acquisition, where the interest rate moves with how far out the payback period is pushed. He calls the lender's position rational, because the lender is exposed to how much gets lent rather than to the acquisition cost, and locates the risk on the borrower's cohort assumption.

**The auction half of the argument, which the interviewer supplies and Holiday only half accepts.** Venture-funded entrants are fronting acquisition cost, and in an auction a bidder willing to pay more for the customer sets the price everyone else pays, so the high-gross-margin high-retention business model gets eaten from the cost side while the balance sheet holds. Holiday's reply is that this describes every market with a low barrier to entry rather than anything specific to supplements. Read beside [[Marketing Math & Unit Economics#MM-182|MM-182]] on efficiency decay inside a fixed pool, [[Marketing Math & Unit Economics#MM-187|MM-187]] on the halo that makes two accounts' in-platform returns uncomparable, and [[Auction Mechanics & Bidding#AU-031|AU-031]] on brand equity inverting diminishing returns in the auction.

**Two limits before quoting any of it.** This is one operator reasoning out loud in a conversation, with no cohort data, no acquisition-cost series and no named failure. The counter-position sits in the same exchange: a low barrier to entry is also why the category has been an unusually good opportunity, and a business sold for $30M to $50M is a good outcome that needs none of this to hold.
""",
    [AF])


# ---------------- AMENDMENTS ----------------

amend("Creative Science.md", "CR-036", """
**Restated 2026-09-15 with the one instruction this entry was missing: which angle to HOLD during the offer round.** The entry already says the offer round locks avatar, awareness, pain point, angle and format and varies only the offer. It never said what to lock the angle AT. He now names it, and calls it a hidden step: "Often times I will lock the angle of a guarantee and I will lock the pain point and then I will test five different offers to figure out which offer works." The reason follows from the round's job. A guarantee or risk-reversal angle states the offer as plainly as an ad can, so the offer is the only thing the reader is reacting to, and any angle with a story or a curiosity gap in it confounds the read it was built to produce. "Very bold, and often times when I'm testing out offers, I'll do like literally just these ads. I'll do like five or 10 of these ads with different offers."

**And the order after the offer resolves, which he states as a loop rather than a finish line**: find the offer, then move pain points, then move angles. Same three phases this entry already carries, now with a return path.
""", MS_ANG)

amend("Creative Science.md", "CR-114", """
**The angle taxonomy expanded to seven on 2026-09-15, from the four this entry carries, each with a written worked line.** His framing of what an angle is stays identical, "the wrapper around your pain point... how do you articulate it, how do you say it, to appeal to different types of people", and the seven are: **mistake** (call out what they are doing wrong, "people hate making mistakes"), **new method** (throw stones at the old way, name a new one), **proof** (lead with a named client's result, which he says converts hardest in B2B), **story** (the speaker's own vulnerability, not the client's), **benefit or how-to**, **contrarian** (break a belief they hold, paired with a stop hook), and **offer or guarantee** (lead with the risk reversal, which he reserves for direct-offer ads). Note the deliberate split between proof and story: proof is a client, story is you, and he assigns them to different jobs rather than treating them as one testimonial bucket.

**A definitional boundary that matters more than the list, because it decides what goes in which variable for a local health business.** The persona is the CONDITION and the pain point is the LIFE IMPACT. His worked case: knee pain is the persona, and "going upstairs", "it hurts really bad to squat" and "not able to run" are three pain points under it. He corrects himself out loud to make the point: "I realized I just said knee pain, right? You might actually categorize that as a pain point, but I wouldn't. I would go a level deeper." The same split on a business offer puts the offer's buyer in the persona slot and puts lead quality, show rate or feeling stuck below a revenue line in the pain point slot. **This is directly load-bearing for the chiropractic and physical-therapy accounts**, where the body part has always been the right hook and the reason to build three ad sets, and it names the layer underneath it that the creative is actually supposed to vary.

**Structure note attached, and he deliberately declines to rule on it.** Angles can run as one ad set with five angle ads, or as one campaign per angle with an ad set each, decided by budget alone: "There's not a right or wrong here." His reason for not caring is worth keeping next to the structure claims in this codex: "the biggest thing that converts and moves the needle nowadays is the actual ad itself, not the campaign structure. I get obsessed over campaign structure more than most people, but I want to emphasize to you the angles, the ads, the messaging matters more."
""", MS_ANG)

amend("Creative Science.md", "CR-037", """
**Restated 2026-09-15 with the threshold attached, which turns the stage rule into something checkable.** One offer and one pain point, wrapped in multiple angles and formats, is explicitly scoped to accounts under $100k a month: "If you're under 100k, you really just need one offer, one pain point, multiple different creative formats, multiple different angles, and scale what works." The trigger for adding a second pain point is reaching that number, not fatigue: "if I could have one pain point, one offer, and scale that to 100k a month, then add another pain point and do the same thing with that." His stated reason for the consolidation is budget rather than message quality, since a limited spend split across several messages starves all of them.

**One caveat he adds for brick-and-mortar that cuts against the single-persona rule.** A local business may legitimately carry several personas at once, his example being a physical therapy or chiropractic clinic running shoulder pain, low back pain and knee pain as three separate avatars, and it may carry several offers with them. Under $100k a month he still tells an online business to pick one of each. So the one-offer rule is a rule about online offers, and the local case is the named exception.
""", MS_ANG)

amend("Creative Science.md", "CR-058", """
**The counterweight to this claim arrived 2026-09-15, and it is about what you are buying rather than whether it works.** Taylor Holiday's position, banked in full at [[Creative Science#CR-245|CR-245]], is that an influencer buy whose only output is an ad asset is the weakest form of the trade and decays, because the relationship is pure extraction on both sides. His prescription does not reduce the buy, it widens it: design the deal so the shoot also produces ad and email usage rights and a route into retail, then embed the person across customer-facing surfaces (product photography, customer service) so the presence is continuous rather than campaign-shaped. He is blunt that the ads alone may not carry it, citing a named athlete partnership where "I don't think we were ever running a lot of ads with him that worked well, but I still think it was important that he was part of the brand."

**Read that against the ranking in this entry rather than as a refutation of it.** Heath ranks hiring influencers to produce video ads as the single highest-return intervention he knows, measured in hook rate, view-to-click and click-to-conversion. Holiday is not disputing those numbers, he is saying that an influencer scored only on them is being bought as a creator. Both are asserted from large books with no data shown.
""", AF)

amend("Creative Science.md", "CR-054", """
**The UGC-versus-influencer definition carried in this entry is now contested, 2026-09-15.** The line above distinguishes them by following size, cost and scroll-stopping power. Taylor Holiday distinguishes them by whether the person's identity is the asset at all, which makes follower count a proxy rather than the mechanism. Full claim and the operating rules that follow from it at [[Creative Science#CR-245|CR-245]]. Nothing else in this entry is affected: the style-diversity claim itself is untouched.
""", AF)
