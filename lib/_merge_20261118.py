# -*- coding: utf-8 -*-
"""Merge the 2026-11-18 research haul into the codex."""
from pathlib import Path
import shutil

SCI = Path(r"E:\claude code marketing skill\Obsidian God-level Marketing Vault\God-level Marketing\wiki\science")
MD = SCI / "Meta Delivery & Andromeda.md"
AU = SCI / "Auction Mechanics & Bidding.md"

SRC = ("Ben Heath, Facebook Ads Super Burst Just Launched!, 2026-11-17, "
       "youtube.com/watch?v=yrVkUnVxcDE, 19 min, read in full (screen walkthrough of the live "
       "product in his own UK ad account)")

NEW_MD = u"""
### MD-201 \u00b7 Ads Super Burst, read off the live product: it is one of TWO burst durations, every delivery control is locked the moment you pick it, and it is capped at ONE impression per person
Tier: T1 \u00b7 Status: active
First sighting of the product in a working ad account, 17 November 2026, and the first sighting outside the United States. [[Meta Delivery & Andromeda#MD-181|MD-181]] banked the October announcement, which was US-only and published nothing but brand-lift outcomes. This claim is the configuration surface, read on screen from Meta's own in-product strings. Route note, and it bounds the tier: this is the platform's own product copy and its own forecasting output, seen through a practitioner screencast rather than through documentation, in one UK account.

**It is a pair of products, not one, and MD-181 only has the second.** The picker inside Reach Planner offers **Ads Burst, "sustained reach over two to five days"**, and **Ads Super Burst, "concentrated reach in three to 24 hours"**. Ads Burst has not appeared anywhere else in this codex.

**Where it lives.** Ads Manager, All tools, Reach Planner, then create a plan and choose the product. It is not in the campaign objective list. Reach Planner itself is not on every account and the burst products are on fewer still; Heath describes the usual Meta pattern of announce, test on a small group, then widen.

**What gets locked the moment the product is selected, all four greyed out in the UI.** Buying type **reservation**. Performance goal **reach**. Placements fixed to **Facebook and Instagram Feed, Stories and Reels**, with no Audience Network and no Messenger, which is the premium-surface set. Frequency fixed at **one time per person**, stated in-product as "average frequency, one time per Meta account".

**What stays editable, and what does not.** Meta's own string: "Ads Super Burst uses broad targeting in only one country or region. Detailed targeting custom audiences aren't available." So no interest or behaviour layers and no custom or lookalike audiences. One country or region at a time, with sub-region **exclusions** permitted. **Age bands are editable**, individually removable from the default full range. **Gender is editable**, women or men, which is worth noting against [[Meta Delivery & Andromeda#MD-196|MD-196]]: the ad-set gender control is being withdrawn from auction campaigns while it still works here. Duration is a fixed menu, **3, 6, 12 or 24 hours, defaulting to 6**. Special ad category must be declared as on a normal campaign, and the plan setup carries an opt-in checkbox for using the flight in a brand lift test.

**It prices by the hour of the day, and the swing is large.** Same UK geography, same 6-hour length, addressable audience **14.9 million for a midnight to 06:00 window against 33.3 million for 07:00 to 13:00**. The default window the tool offers is midnight to 06:00, which is the worse of those two by a factor of 2.2. Read the window before accepting the default.

**It prices by the day as well, with named demand tiers.** The planner labels candidate dates standard, elevated and peak. Measured on screen, UK, same 6-hour window: **\u00a36.00 CPM on a peak day against \u00a34.50 on the Friday nine days earlier.** Same budget, lower reach and lower audience share on the peak day. So the reservation price is not one fixed rate card. It is a forecast that moves with the same demand the auction moves with, and the saving sits in choosing the date.

**The budget it asks for.** Meta's own suggested budget for a single 6-hour UK flight was **\u00a333,010.67**. It can be lowered freely, with audience share and reach falling accordingly, and the in-product framing is that the product is for high-impact campaigns. The planning method can be flipped from a budget input to a **share-of-audience input**, so the question becomes what it costs to reach 10% or 50% of the named demographic rather than what a budget buys.

**The cheap-reach arithmetic, and it is arithmetic rather than a test.** [[Meta Delivery & Andromeda#MD-053|MD-053]] holds the identity that cost per thousand people reached equals CPM times frequency. Apply it here: a conversion campaign at a \u00a320 CPM running an average frequency of 3 costs \u00a360 per thousand people reached, against \u00a34.50 here at a frequency of 1. That is the roughly 10x-plus gap Heath claims, and the frequency term is where almost all of it comes from, not the CPM term. **Nothing in this is a measured outcome.** No conversion figure, no cost per result and no lift number appears in the walkthrough, and Heath states his own testing to date as "very limited experimentation" with no results to report.

**Operating read, and it is unchanged from MD-181 for our book.** Lead generation for local businesses in New Jersey, Illinois and Michigan cannot buy a country-level broad-reach flight at a month of budget in six hours, and the one-country-or-region floor removes the local targeting every account in the book depends on. Heath expects the location floor to loosen over time and still expects it never to reach small-area targeting. **Banked as platform mechanics and as a rollout marker, not as anything to buy.** The one thing to carry forward: if a client ever has a dated, newsworthy event and the budget to blanket a geography in a day, this is the only Meta product that does it, and the first question is what the forecast says on an adjacent cheaper date.
Sources: __SRC__
Last touched: 2026-11-18
"""

AU_AMEND = u"""**The author of this claim now argues it DOES NOT HOLD at high audience share, 2026-11-18.** Heath walked the live Ads Super Burst product and raised the objection against himself. The degraded-prospect mechanism above requires Meta to be able to select who sees the ad. At a high share of a named demographic it cannot: "it's basically like meta would not be able to cherry pick the lower quality prospects and put your ads in front of these people because it's cheaper. Your ads will be put in front of everyone." So the reservation flight buys the good prospects and the bad ones in their true proportion, and the quality objection shrinks as audience share rises. **This is reasoning, not evidence.** No conversion figure, cost per result or test accompanies it, and he states his own experimentation as very limited with no results yet. Two further things keep this claim's operator rule intact rather than overturned. The mechanism is only neutralised at high share, which on his own screen costs a month of budget in six hours unless the geography and demographic are narrow. And the one-impression-per-person cap means a flight of this kind cannot carry a prospect to a conversion the way a frequency of three can. **Status stays active and the default stays auction.** What changes is the scope line: the degraded-prospect argument applies to reservation buys that leave Meta room to choose, and stops applying to a flight that buys nearly everyone. Product mechanics at [[Meta Delivery & Andromeda#MD-201|MD-201]]."""

MD181_PTR = (u"**The live product was read on 2026-11-18 and it is a PAIR of products with a locked control set, "
             u"now visible outside the United States.** Full configuration surface, the Ads Burst sibling, the "
             u"one-impression cap and the day-and-hour pricing at [[Meta Delivery & Andromeda#MD-201|MD-201]].")

# ---- AU-032: append amendment, bump Last touched ----
txt = AU.read_text(encoding="utf-8")
i = txt.index("### AU-032 ")
j = txt.index("\nLast touched:", i)
eol = txt.index("\n", j + 1)
assert txt[j + 1:eol] == "Last touched: 2026-10-16", txt[j + 1:eol]
shutil.copy(AU, str(AU) + ".bak-20261118")
AU.write_text(txt[:j] + "\n" + AU_AMEND + "\nLast touched: 2026-11-18" + txt[eol:], encoding="utf-8")
print("AU-032 amended")

# ---- MD-181 pointer + MD-201 appended ----
txt = MD.read_text(encoding="utf-8")
assert "### MD-201 " not in txt
i = txt.index("### MD-181 ")
j = txt.index("\nLast touched: 2026-10-16", i)
shutil.copy(MD, str(MD) + ".bak-20261118")
txt = txt[:j] + "\n" + MD181_PTR + txt[j:]
txt = txt.rstrip("\n") + "\n" + NEW_MD.replace("__SRC__", SRC)
MD.write_text(txt, encoding="utf-8")
print("MD-181 pointer added, MD-201 appended")
