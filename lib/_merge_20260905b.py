# -*- coding: utf-8 -*-
"""Merge pass 2 for 2026-09-05: Google, Attribution and Creative amendments."""
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


GP = "Google PMax & Shopping.md"
GA = "Google Auction & Smart Bidding.md"
AT = "Attribution & Incrementality.md"
CR = "Creative Science.md"

amend(GP, "GP-014", """**The variant instruction above has a counter-case from the same channel, and the two are not talking about the same kind of variant.** The rule here is built on a 50g/100g/500g product, where each size is a genuinely different search and three listings open three keyword pools. A separate episode argues the opposite for **colour**: a product carried in 30 to 40 colours submits 30 to 40 near-identical listings and "your spend within Google ads is too finely split across hundreds of different product variants", so only the first variant should reach Merchant Center.

**Reconciliation, and it is ours rather than either operator's: the variant TYPE decides.** A size, weight or format variant expands the query surface because shoppers search the size. A colour variant of the same garment does not create thirty distinct query pools, it fragments the spend and the conversion data across thirty copies of one listing. **Neither operator addresses the other's case**, so this is a boundary we are drawing, not a position either of them stated. The practical test before submitting every variant: would a shopper type this attribute into the search bar? If yes, separate listings. If no, one listing.

Two ways to execute the restriction. The Simprosys feed app carries a variant submission preference under sync settings, first variant only against all variants, which is a one-click change and resync. Without that app it is the excluded_destination attribute applied through a supplemental feed, one row per variant to suppress, which becomes unmanageable above a few thousand products.""",
      add_source="Blue Sense Digital, How to Submit ONLY 1 Product Variant into Google Merchant Center NEXT, 2025-02-21")

amend(GP, "GP-031", """**Two implementation notes for the pull-and-remove half of this claim, both added 2026-09-05.**

**Removing a product from Shopping without delisting it: the excluded_destination attribute.** Applied through a supplemental feed keyed on item ID, it takes a product out of Shopping ads and Display ads while leaving it live in free listings, and multiple channels are comma-separated in the one cell. That is the mechanism for the removal this claim prescribes, and for the ordinary case of a gift card that should never enter a Shopping auction at all.

**Getting the per-product funnel data this claim depends on.** Shopify does not expose add-to-carts per product natively; its reports carry add-to-cart rates and ratios but no product-level count. The route is a GA4 Explore free-form report with **item ID and item name as rows and "items added to cart" as the metric**. That gives the layer between spend by product and purchase by product, which is what tells you whether a high-spending product is failing at the page or at the checkout. Useful against the site-level checkout funnel benchmark at [[Marketing Math & Unit Economics#MM-192|MM-192]], which cannot localise where the drop happens.""",
      add_source="Blue Sense Digital, [excluded_destination] Attribute in Google Merchant Center NEXT Explained, 2025-02-12; Blue Sense Digital, ADD TO CART Report in Google Analytics, 2025-02-03")

amend(GA, "GA-036", """**A third position, added 2026-09-05 and more specific than either above.** Blue Sense opens a new standard Shopping campaign on a brand-new account with **Maximize Clicks and no maximum bid set**, explicitly accepting early wasted spend on the argument that a capped bid stops the campaign ramping at all: "you have some wasted spend or the campaign never ramps and spends in itself". Where the account is established enough for target ROAS to be available, he sets it at **50%**, and says anything above that prevents the campaign from spending. The observable he uses to tell whether the choice is working is the impression-doubling ramp at [[Google PMax & Shopping#GP-044|GP-044]].

That puts three positions on this contested claim: manual CPC or Maximize Clicks, straight into maximize conversion value, and Maximize Clicks uncapped or a deliberately slack 50% target. **All three are practitioner defaults with no shown test**, and the 50% figure is the same number the same operator uses for the feeder campaign at [[Google PMax & Shopping#GP-008|GP-008]], so it is one number reused rather than independent corroboration.""",
      add_source="Blue Sense Digital, Why Your New Google Shopping Campaign Isn't Spending, 2025-03-19")

amend(AT, "AT-046", """**The customer-list accuracy question has three rungs, not two, and the third one was missing until 2026-09-05.** Three separate episodes from this channel state that manually uploaded customer lists, whether exported from Shopify or synced from Klaviyo, are materially more accurate than the platforms' own auto-created audiences: Facebook pixel audiences on Meta, and Google Analytics auto-created audiences on Google. He says the comparison came from running "audience comparison tests" on the back end of both platforms, and that the auto-generated audiences "were quite off in terms of actually including all of those relevant people".

**Combined with the paragraph above, the ladder reads: manual Shopify upload, then the Klaviyo sync, then the platform's own auto-created audience.** The paragraph above supplies the discriminator between the top two, which these episodes miss. These episodes supply the bottom rung, which the paragraph above did not have.

**The warning that falls out of putting them side by side.** The same channel documents the Klaviyo suppressed-profile defect in February 2025 and then, in May 2025, recommends the Klaviyo sync as the preferred option because it auto-refreshes and saves re-uploading. It never reconciles the two. **Anyone who follows the May tutorial inherits an exclusion list that is short by however many profiles the email platform has suppressed**, which is the exact error the February episode says changes every new-versus-existing number.

**Evidence quality is the weak point: he names a test three times and publishes nothing from it.** No match rate, no audience size on either side, no count of accounts, no numbers at all. T3 on the ranking, and the ranking is plausible on mechanism alone, since a hashed identifier list beats a behavioural audience assembled from a pixel that misses browsers and blocked sessions.

**Google customer-list mechanics worth having on file, since the upload is where it usually breaks.** The match fields are first name, last name, email, phone, country and postal code; every other column in the Shopify export has to be unmapped or the upload errors out. The audience shows a size of zero on completion and populates over the following days as Google matches identifiers to real users, so an empty audience on day one is expected. **It cannot be used in a campaign, for inclusion or exclusion, until it holds more than 1,000 members**, which is the practical floor on how small an account can run list-based exclusion at all.""",
      add_source="Blue Sense Digital, How to Upload a Shopify Customer List into Google Ads, 2025-05-01; Blue Sense Digital, Meta Ads / Klaviyo Integration & Audience Sync Setup, 2025-05-01; Blue Sense Digital, Google Ads / Klaviyo Integration & Audience Sync Setup, 2025-05-04")

amend(CR, "CR-048", """**Second independent operator on the cheap-traffic half of the format above, added 2026-09-05.** Mark Builds Brands reaches the same trade from the production side rather than the creative side: native image ads that read as ordinary social posts are chosen because "you can make hundreds of them just in under an hour", and they buy "extremely low cost of traffic, which means they're probably not going to be as qualified as normal compared to like, you know, a 3-minute-long video ad". **His conclusion is the same one: the funnel has to absorb the deficit, so the ad runs to an advertorial rather than to the product page, and the advertorial exists to compensate for traffic the format bought cheaply.**

That is two operators, on different channels and different formats, stating the same relationship: **cheap traffic and qualified traffic trade against each other, and the creative format therefore sets how long the funnel has to be.** Both assert it and neither shows a cost-per-acquisition comparison between the short and long funnel behind the same ad. It also carries the same judging rule, that this format is never scored on click-through rate.""",
      add_source="Mark Builds Brands, how to print money with AI (before NPCs ruin it), 2026-04-24; Mark Builds Brands, how to print money online (easier than scrolling youtube), 2025-12-26")

amend(CR, "CR-138", """**Restated by the same speaker 2026-04-17, so this is one operator saying it twice rather than corroboration.** The addition worth keeping is the instrument, since the claim above prescribes a readability check without naming one: he runs the copy through **hemingwayapp.com** to read the grade level back. He pairs it with reading the copy aloud five to seven times, which is craft rather than a testable claim and belongs with the copy skills, not here.""",
      add_source="Mark Builds Brands, i asked claude to build me a $5k/day website (it worked lol), 2026-04-17")

print("pass 2 done")
