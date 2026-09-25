"""Claim merge for the 2026-09-25 research pass.

New: GA-081, GA-082, GA-083, GA-084.
Amend: GA-068.

Sources actually read today, in full, at source:
 - Google Ads & Commerce Blog, "Turn discovery into action with September's
   Demand Gen Drop", 2026-09-24, body and the #footnote-1 anchor
 - Google Ads Help /google-ads/answer/16024357, "About Gmail ads clicks and
   reporting on Display", verbatim via urllib
 - Google Ads Help /google-ads/answer/16388390, "How to advertise in Google
   Maps", verbatim via urllib
 - Demand Gen Drops Hub, business.google.com/us/accelerate/demand-gen-drops/
 - Demand Gen Drop May 2026, business.google.com .../demand-gen-drop-may-2026/
 - Demand Gen Drop July 2026, business.google.com .../demand-gen-drop-july-2026/
 - Meta Newsroom, "The Biggest News From Connect 2026", read, no ad content,
   deliberately not banked
 - arXiv 2609.29182 ScalarLens, 2609.28972 CMRec, 2609.30001 AgentX abstracts
"""
import re
from pathlib import Path

VAULT = Path(r"E:\claude code marketing skill\Obsidian God-level Marketing Vault"
             r"\God-level Marketing\wiki\science")

GA = VAULT / "Google Auction & Smart Bidding.md"
TODAY = "2026-09-25"


def read(p):
    return p.read_text(encoding="utf-8")


def write(p, s):
    p.write_text(s, encoding="utf-8")


def block_span(text, claim_id):
    m = re.search(r"^### %s[ \u00b7\-]" % re.escape(claim_id), text, re.M)
    if not m:
        raise SystemExit("NOT FOUND: %s" % claim_id)
    start = m.start()
    nxt = re.search(r"^### [A-Z]{2}-\d+[ \u00b7\-]", text[m.end():], re.M)
    end = m.end() + nxt.start() if nxt else len(text)
    return start, end


def amend(text, claim_id, extra):
    """Insert extra text just before the Sources: line of a claim block."""
    start, end = block_span(text, claim_id)
    block = text[start:end]
    m = re.search(r"^Sources:", block, re.M)
    if not m:
        raise SystemExit("no Sources line in %s" % claim_id)
    block = block[:m.start()] + extra.strip() + "\n" + block[m.start():]
    # refresh Last touched
    if re.search(r"^Last touched:.*$", block, re.M):
        block = re.sub(r"^Last touched:.*$", "Last touched: %s" % TODAY, block,
                       count=1, flags=re.M)
    else:
        block = block.rstrip("\n") + "\nLast touched: %s\n" % TODAY
    return text[:start] + block + text[end:]


GA_081 = """
### GA-081 · Google's September 2026 Demand Gen drop ships one-click on Shorts and Gmail, a Business Agent waitlist and affiliate-location Promoted pins, and its one printed number measures a different thing from the feature it sits under
Tier: T1 · Status: active
Google Ads & Commerce Blog, "Turn discovery into action with September's Demand Gen Drop", 24 September 2026, body and footnote read in full at source. T1 for existence and product copy only. Same tier guard as [[Google Auction & Smart Bidding#GA-068|GA-068]]: nothing here states that Demand Gen performs.

**Three items, and only one carries a hard spec.**

1. **Business Agent for YouTube Ads.** Viewers "engage with conversational AI alongside video ads with product feeds, getting immediate answers about products or brands without leaving their viewing context." Access is a Google Form sign-up, so this is a waitlist and not a launch. The post's own "conversational AI" link points at a Shopping holiday post rather than any Demand Gen documentation.
2. **One-click experiences on YouTube Shorts and Gmail.** The Shorts half is the only hard requirement in the post: you get one-click "when you upload **9:16 full-bleed image ads**". The Gmail half changes what a tap does, and what it does to the metric is at [[Google Auction & Smart Bidding#GA-082|GA-082]].
3. **Affiliate Location Extensions in Google Maps.** "Retail networks and dealerships can capture local demand through Promoted pins across Google Maps, which are displayed as people browse, search, and navigate."

**The number, and the three things wrong with reading it as evidence for the announcement.** Google prints "Advertisers adding Gmail to their Demand Gen campaigns on average see their image creatives achieve a 40% increase in conversions at the same ROI", footnoted **"Google Internal Data, Global, Gmail Ads, February 2026"**.

- **It is about ADDING GMAIL as a channel, not about the one-click change it is printed under.** Google's own sentence in the same paragraph calls Gmail "a channel already delivering strong performance", so the figure describes the channel and predates the update.
- **The data window is February 2026 and the post shipped 24 September 2026.** The number was measured seven months before the feature it accompanies.
- **"At the same ROI" makes it a VOLUME statement at constant efficiency**, which is the arithmetic of adding inventory and spend. It is not an efficiency claim and must never be repeated to a client as one. A client hearing "40% more conversions" hears efficiency.

**Third consecutive vendor aggregate over self-selected adopters with no control group and no holdout**, after the 30% at [[Google Auction & Smart Bidding#GA-068|GA-068]] and the four Data Manager figures at [[Google Auction & Smart Bidding#GA-073|GA-073]]. The pattern is now stable enough to expect: every Google ads release carries one average-uplift figure over adopters, and none of them is a lift measurement.

**The affiliate-location half has no published eligibility rule, checked at source.** The help article Google links for it, `/google-ads/answer/16388390` "How to advertise in Google Maps", contains the word "affiliate" **zero times**. What that page does establish, and it is T1: Promoted pins are supported in **Demand Gen**, Travel for Things to do, Performance Max for store goals and Smart; Promoted pins require a linked **Google Business Profile**; and "currently, you can't serve ads exclusively in Google Maps."

**Operating call for our two truck dealerships, stated so nobody proposes it off the headline.** The announcement says "dealerships" and that will read as an SJR Commercial and Phoenix Truxx opportunity. Affiliate location assets are historically the manufacturer-through-retail-chain instrument, for an advertiser promoting locations it does not own. An independent single-location dealership selling its own inventory at its own address is the ordinary location-asset case, which needs no new feature. **Google has documented no eligibility rule for this, so treat a dealership fit as unverified rather than available.** The Maps inventory itself is not new to Demand Gen either; it landed in May 2026, see [[Google Auction & Smart Bidding#GA-083|GA-083]].

**Source-lane note worth keeping.** The three help-article ids this post links (16040527, 16024357, 16388390) are **not** among the 396 answer ids on the Google Ads Announcements page. That page does not carry Demand Gen drops. The Ads & Commerce RSS feed is the only watchlist lane that catches them.
Sources: Google Ads & Commerce Blog, "Turn discovery into action with September's Demand Gen Drop", 2026-09-24, read in full 2026-09-25; Google Ads Help, "How to advertise in Google Maps", /google-ads/answer/16388390, read 2026-09-25
Last touched: 2026-09-25
"""

GA_082 = """
### GA-082 · A Gmail click counts the same whether it opened the ad or opened your site, so the one-click switch changes what the metric means while the metric keeps its name
Tier: T1 · Status: active
Google Ads Help, "About Gmail ads clicks and reporting on Display", /google-ads/answer/16024357, read verbatim at source 2026-09-25. Banked because [[Google Auction & Smart Bidding#GA-081|GA-081]] just moved Gmail image ads from the two-click format to the one-click format, and this is the rule that decides how to read the result.

**The two formats, in Google's words.** The most common conversion path is two-click: a teaser ad is viewed, and clicking it expands the teaser into the full-sized ad. "Some Gmail ads follow a one-click format where you are taken directly to the advertiser's website when you click on the ad teaser, or certain elements within the ad teaser."

**The reporting rule, quoted because the whole claim rests on it:** "Clicks are reported from the teaser ad click for Display campaign reporting, whether the click expands the ad body or navigates directly to the advertiser's site."

**So one label covers two different actions.** Under two-click a Gmail click means the ad opened. Under one-click the same counter means a person reached the landing page. **A before-and-after read of Gmail clicks or CTR across the September switch is comparing an expand against a site visit.** Expect the ratio of clicks to landing-page sessions to move with no change in demand, and expect cost per click to move with no change in the auction.

**The operating rule.** Judge the Gmail one-click switch on conversions and cost per conversion. Never on clicks, CTR or cost per click. Two supporting details from the same page: the metric that survives the switch is the separate count of **expanded ad clicks that lead to a website, visible in Display reporting under the Gmail asset type**; and a repeat click on the same ad, or interaction inside the expanded ad, is not counted, so the counter is one per person per ad either way.

**The honest limit on this claim, and it matters.** The article is titled "on Display", sits under Display campaigns in Google's own help tree, and the September change lands in **Demand Gen**. The page links "About Demand Gen campaign metrics and reporting" as a related article without restating the rule there. **Whether the identical click-counting rule carries into Demand Gen reporting is not stated anywhere we have read.** Treat the mechanism as established and the Demand Gen application as the reasonable assumption to verify in an account before quoting it to a client.
Sources: Google Ads Help, "About Gmail ads clicks and reporting on Display", /google-ads/answer/16024357, read verbatim 2026-09-25
Last touched: 2026-09-25
"""

GA_083 = """
### GA-083 · The May 2026 Demand Gen drop is where Maps inventory and automotive product feeds actually landed, and it shipped two counterfactual instruments for the channel our own holdout found no lift on
Tier: T1 · Status: active
Demand Gen Drop, May 2026, business.google.com/us/accelerate/announcements/demand-gen-drop-may-2026/, read in full at source 2026-09-25. Read four months late, off the Drops Hub that [[Google Auction & Smart Bidding#GA-081|GA-081]] surfaced. T1 for existence and product copy only.

**Why it matters more than a four-month-old release normally would: it re-dates two things the September drop would otherwise appear to introduce.**

- **"New Google Maps inventory connects your brand with people exploring their local areas."** Maps inventory reached Demand Gen in May. September added an affiliate-location route to it, not the surface itself.
- **Product feeds expanded "to more surfaces and verticals, including automotive".** That is the line that matters for our two truck dealerships, and it is four months old.

**The rest of what shipped.** Multimodal video creation in Asset Studio from a few prompts, later generally available per [[Google Auction & Smart Bidding#GA-068|GA-068]]. Creator partnership videos boostable from the asset picker during campaign setup. Merchant Center video upload for dynamic product videos, stated as coming. Checkout links to nine new markets. **AI-assisted Demand Gen campaign creation**, which clones settings from an existing campaign such as Performance Max in one click, with all settings visible and editable before publishing.

**Two measurement instruments, and this is the part that touches our own evidence.** Google shipped **Campaign Type Attribution**, to isolate all conversions from Demand Gen for comparison against channels like paid social, and **Uplift Experiments**, to measure how Demand Gen complements Performance Max. [[Google Auction & Smart Bidding#GA-068|GA-068]] closes on the line that Google's 30% and our null result can both be true at once "and only the null one was measured against a counterfactual". **Google now ships a counterfactual instrument for this channel.** That does not settle [[Google Auction & Smart Bidding#GA-055|GA-055]] or [[Attribution & Incrementality#AT-072|AT-072]], both of which are a 21-day geo holdout on one e-commerce advertiser, and it is a first-party instrument measuring its own product. It does mean the next Demand Gen argument with a rep can be answered with an experiment rather than with a position.

**The number and its footnote.** "Advertisers with large product selections typically see a 33% increase in conversions when adopting product feeds in their Demand Gen campaigns", sourced "Google data, Global, May to June 2025, based on performance data for campaigns active since Q1 2024 with over 50 products in merchant feed". **That footnote states a survivorship filter out loud:** the cohort is campaigns still running more than a year after launch, with more than 50 products. Campaigns that adopted feeds and were switched off cannot be in it. Fourth vendor aggregate in the same pattern, and the only one so far that publishes the filter that biases it.
Sources: Google, Demand Gen Drop May 2026, read in full 2026-09-25
Last touched: 2026-09-25
"""

GA_084 = """
### GA-084 · Google's July 2026 Demand Gen drop says in its own product copy that tROAS was being overly cautious early, and the fix is an upgrade rather than a setting
Tier: T1 · Status: active
Demand Gen Drop, July 2026, business.google.com/us/accelerate/announcements/demand-gen-drop-july-2026/, read in full at source 2026-09-25, four months late off the Drops Hub.

**The line worth banking, quoted:** use "upgraded Target ROAS (tROAS) bidding to prevent the system from being overly cautious early on so your campaigns hit their targets faster."

**Read it as an admission about the prior behaviour, because that is what it is.** Google is describing its own tROAS on Demand Gen as having been too cautious in the early period of a campaign, and shipping a change to it. **There is no toggle named here and no before-and-after figure.** So an account cannot be checked for it, an operator cannot switch it on or off, and any Demand Gen tROAS result from before July 2026 was produced by a different bidder than the one running now. That is the operating consequence: **do not compare Demand Gen tROAS performance across the July 2026 boundary**, and treat pre-July tROAS ramp behaviour in this codex as describing a superseded system.

**The rest of the drop.** Checkout Links now in nine new markets, named in the footnote as Switzerland, Australia, South Korea, Indonesia, Mexico, France, Poland, Israel and Argentina, which restates the May expansion at [[Google Auction & Smart Bidding#GA-083|GA-083]]. Product feeds, affiliate partnerships boost, and purchases direct from YouTube ads through checkout links or the **Universal Commerce Protocol, US only**.

**Two numbers, both weaker than they look, with their own footnotes.** "On average, advertisers who provided Checkout URLs boosted conversions by 6% on Demand Gen", sourced "Google data, US, 09/01/25 to 09/30/25", a single US month read ten months before publication. And "94% of holiday shoppers who used YouTube reported taking further steps toward their purchase after watching a related video", sourced to a commissioned Ipsos online survey, n=4391, of "US consumers 18+ who conducted Holiday shopping activities in the past two days **and watched videos on YouTube for shopping**". **The sampling frame is people who already used YouTube to shop, asked whether YouTube moved them along.** The answer is built into who was asked. Fifth vendor figure in the running pattern at [[Google Auction & Smart Bidding#GA-081|GA-081]], and the first that is a survey rather than an adopter aggregate.
Sources: Google, Demand Gen Drop July 2026, read in full 2026-09-25
Last touched: 2026-09-25
"""

GA_068_AMEND = """
**Forward note, 2026-09-25.** This is one instalment of a **monthly** series, which this codex did not know until the September drop linked Google's Demand Gen Drops Hub. The September 2026 drop is at [[Google Auction & Smart Bidding#GA-081|GA-081]], and two earlier ones read the same day are at [[Google Auction & Smart Bidding#GA-083|GA-083]] (May, where Maps inventory and automotive product feeds actually landed) and [[Google Auction & Smart Bidding#GA-084|GA-084]] (July, where Google says tROAS had been overly cautious early). **Eight further drops back to October 2025 remain unread.** The 30% figure recorded here is the second of five vendor aggregates now catalogued across the series, and the running note on how to read them is at GA-081.
"""


def main():
    t = read(GA)
    before = len(t)

    for cid in ("GA-081", "GA-082", "GA-083", "GA-084"):
        if re.search(r"^### %s[ \u00b7\-]" % cid, t, re.M):
            raise SystemExit("ALREADY EXISTS: %s" % cid)

    t = amend(t, "GA-068", GA_068_AMEND)

    t = t.rstrip("\n") + "\n" + GA_081 + GA_082 + GA_083 + GA_084
    write(GA, t)

    check = read(GA)
    for cid in ("GA-081", "GA-082", "GA-083", "GA-084"):
        assert re.search(r"^### %s \u00b7" % cid, check, re.M), cid
    assert "Forward note, 2026-09-25" in check
    print("GA file %d -> %d chars" % (before, len(check)))
    print("banked: GA-081, GA-082, GA-083, GA-084")
    print("amended: GA-068")


if __name__ == "__main__":
    main()
