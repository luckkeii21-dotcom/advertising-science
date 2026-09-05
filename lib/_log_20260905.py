# -*- coding: utf-8 -*-
"""2026-09-05: prepend the Harvest Log entry and add the Watchlist method notes."""
import io, os

SCI = os.path.join(
    "E:\\claude code marketing skill",
    "Obsidian God-level Marketing Vault", "God-level Marketing", "wiki", "science")

ENTRY = """## 2026-09-05 (research run)

**0 new transcripts and 0 new watchlist items, and the day was not quiet. The whole 31-file transcript backlog was read and cleared to zero. 7 claims banked, 11 amended, 0 contested. No law changed. Codex 1,162 to 1,169. The most important finding is an arithmetic error inside a claim we already hold.**

**Harvest: 0 new files, 12 channels, 0 errors after a fix**, 12:00 to 12:04 IST. **The first run was a FALSE quiet and it is worth recording as such.** YouTube's `feeds/videos.xml` endpoint returned 404 or 500 for **11 of 12 channels**, the run reported "0 new transcripts" in 12 seconds, and that would have been logged as a quiet day. The endpoint is broken for us globally, not for our channel IDs: **YouTube's own channel feed 404s from this machine on retry, and all 12 of ours failed on a second pass including the one that had succeeded 60 seconds earlier.** Channel HTML pages return 200 and yt-dlp lists the `/videos` tab fine. `harvest.py` now falls back to the tab listing when RSS fails and records every fallback in the run summary, so an outage can never again be reported as an empty inbox. Re-run: **12 of 12 channels listed, 0 errors, 0 new videos, 1 with no subtitles. That is a real quiet inbox.**

**Watchlist: 0 new items anywhere. 0 fetch errors.** Meta Engineering 200, 9 in feed, 0 new (build Wed 2 Sep). Meta Newsroom 200, 10 in feed, 0 new (build Fri 4 Sep). Google Ads and Commerce 200, 20 in feed, 0 new (build Wed 2 Sep). TikTok SDK changelog 200, top version 0.1.8, unchanged. Google Ads Announcements 200, 2,350 lines both sides, 1 added and 1 removed and **both are numeric page nonces**, the same artefact as yesterday.

- **arXiv served an EMPTY feed and it is the weekend build, not a fault.** 892 bytes, **zero `<item>` elements**, `lastBuildDate` Sat 5 Sep 04:00 UTC, `skipDays` listing Saturday and Sunday. Byte-identical in signature to the empty Monday build documented on 2026-08-24. **New detail: this run landed at 06:31 UTC, past the 04:00 rebuild, so it read SATURDAY'S OWN build rather than yesterday's.** No build was skipped and no paper was lost. Watchlist.md updated so a future Saturday run does not log this as an error.
- **Meta for Business News: 12 slugs, IDENTICAL set and identical order to the cached list. Zero new, and the rotation trap did not fire because nothing rotated.** All 12 dates read straight off the listing cards in one pass, which is faster and safer than opening each candidate. Newest is still 11 June 2026, unchanged since 26 August. The `playwright` profile connected today after failing on 30 August and 4 September. Plain fetch returned HTTP 400 for the seventh consecutive run.
- **⚠ Our own cache write from yesterday did not land.** The 2026-09-04 log states the cache union was extended with five slugs and their dates. The `meta-business-news` entry in `watchlist-seen.json` still read `last_checked: 2026-08-30` today, with no 4 September key of any kind. The top-level `last_run` was written, because `watchlist_check.py --commit` ran; the browser source is checked by hand and outside that script, so the manual write was simply never made. Today's was written properly. **Method note: anything checked outside `watchlist_check.py` has to be committed by hand, and the log should not claim a cache write without reading the file back.**

**Extraction: the backlog was the whole day. 31 files, roughly 70,000 words, every one read start to finish. Backlog 31 to 0, the first time it has been empty since the engine was built.**

- **7 banked.** MM-209 (multi-country tax mix distorts the efficiency ratio; a $20k lift in a 10%-tax market is worth $18k and the same lift in a 0%-tax market is worth $20k, so a drifting geographic mix moves the ratio with no advertising change). MM-210 (markup versus margin, both formulas, both conversions, and the two incompatible conventions the word "markup" carries). GP-044 (a new Shopping campaign on a new account does not spend for weeks and the only diagnostic is whether daily impressions are DOUBLING, 4 to 8 to 16 to 32 to 64; do not touch the feed during the ramp). GP-045 (Google matches submitted product reviews to products by **GTIN**, so a missing barcode silently disapproves the entire review feed). GA-071 (not seeing your own ads is never an account diagnosis; the usual cause is that the person searched repeatedly and never clicked). AT-114 (a custom-coded form replacing a platform-native one breaks the tracked submission and the attribution unless the native form is kept hidden and fired; the source's own live test FAILED on camera). CR-229 (T4, proposed: write to the highest-value customer archetype because creative selects who the optimiser fetches, with our own guard that it needs a value-carrying optimisation event to mean anything).

- **⚠ The finding of the day is against our own codex.** MM-018's product floor says "selling price of at least 3x cost of goods" and its worked example calls $10 landed cost sold at $50 a **"5x markup"**. Five is price divided by cost; by the actual markup formula that product is **4x**. **So MM-018 is written in the keystone convention, and anyone applying the formal definition to its "3x" would impose a floor of price = 4x cost, a whole multiple stricter than intended.** Flagged on the claim and carried into the skill as a reading rule: before using any multiple, ask whether it divides by price or by cost. **Second problem on the same claim: the operator behind it states the gross-margin floor as $30 on 2026-04-24 and $25 on 2026-07-30, three months apart, and never acknowledges the change.** Recorded as a rule of thumb that moves rather than a number.

- **11 amended.** MM-074 gained the earliest source on the roster and the mechanism it was missing: the next purchase order is paid roughly 30 days BEFORE the current cycle's revenue lands, so the steady-state bank balance is $6,000 rather than the $20,000 the cycle appears to earn, against a $15,000 founding injection; plus the financing ladder (merchant cash advance at 35% to 350%, because a company loan needs a full year of statements) and a client case at $750,000, $250,000 of stock, ~$4,200 a month of interest. MM-065 gained the account-level number it lacked: a static 30% cost-of-goods assumption models a discount month at **$37,000 of contribution when the true figure is $7,000, an 81% overstatement**, and tagged cost of goods lands within 5 to 10%. MM-192 gained the dedicated episode behind its first trap and the reason shipping must be added back (shipping collected never equals shipping paid). MM-018 as above. GP-014 gained the variant counter-case and our own reconciliation, that the variant TYPE decides: a size variant opens new searches, a colour variant fragments spend across near-identical listings. GP-031 gained two instruments, the `excluded_destination` attribute and the GA4 route to per-product add-to-carts, which Shopify does not expose. GA-036 gained a third cold-start position. AT-046 gained the third rung of the customer-list ladder. CR-048 and CR-138 and CR-086 gained sources and one observation.

- **AT-046's third rung comes with a warning about the same channel contradicting itself.** Three May 2025 episodes rank manually uploaded and Klaviyo-synced customer lists above the platforms' own pixel and analytics auto-created audiences, citing "audience comparison tests" and publishing **no numbers at all**. The codex already holds, from the same channel in February 2025, that the Klaviyo sync drops suppressed profiles and leaves the exclusion list short. **The channel never reconciles the two, so anyone following the May tutorial inherits the February defect.** Full ladder now on file: manual Shopify upload, then Klaviyo sync, then platform auto-created audience.

- **20 of the 31 files produced nothing, and that is the honest yield.** Six Mark Builds Brands mindset videos (tier lists, focus protocols, dopamine, "stop trying to save your friends") contain **zero advertising mechanism and zero testable claim**. A book tier list is a reading list. Five Blue Sense files are pure setup walkthroughs (UTM placement, Klaviyo integration steps, Shopify Markets versus separate stores) and one, *Paid eCommerce Course*, is a straight promotion for their paid product. All were read start to finish before being discarded.

- **Channel routing rule, from today's evidence rather than from a guess.** On Mark Builds Brands the split is clean: **3 business-mechanic titles produced claims, 6 mindset titles produced nothing.** That does not overturn the 2026-09-04 note that title alone predicts neither way, which was drawn across channels. Within this one channel the title is a usable filter, and the backlog should have been ordered by it rather than by word count, since the four longest files in the queue were all mindset.

- **Gaps.** The launcher still cannot distinguish an auth failure from a quiet day, carried a fourth time, and today produced the adjacent failure in the harvester instead: a source outage that reads as an empty inbox. The harvester is now fixed; the launcher is not. LS-074 and LS-075, the cost of a qualification gate in opt-in volume and show rate, remains unmeasured by anyone and remains the cheapest thing we could produce. Meta's own wording on Close form and conditional logic is still quoted only in our build notes and still not banked. Meridian and Qualified Future Conversions still have no codex entry. The SC-133 CBO-with-floors comparison is still unrun. The arXiv framing-sentence filter gap is still open and did not fire today only because the feed was empty. **New: with the backlog at zero the engine's claim volume is now capped by the daily inbox, which is running at roughly 0 to 2 files a day.**

"""

# Harvest Log: newest entries go directly under the intro line.
p = os.path.join(SCI, "Harvest Log.md")
t = io.open(p, encoding="utf-8").read()
anchor = "One line per Research run: what came in, what changed. Quiet days get one line and nothing else.\n\n"
assert t.count(anchor) == 1
t = t.replace(anchor, anchor + ENTRY)
io.open(p, "w", encoding="utf-8", newline="\n").write(t)
print("Harvest Log entry prepended")

# Watchlist: record the Saturday empty-build variant beside the Monday one.
p = os.path.join(SCI, "Watchlist.md")
t = io.open(p, encoding="utf-8").read()
anchor2 = ("That is not a fetch failure, not a parse failure, and not a filter result. There was nothing in the file. "
           "Log it as \"feed empty, weekend build\", never as \"0 advertising papers today\" and never as an error. "
           "The same will be true of every future Monday run until the task moves past 09:30 IST.")
assert t.count(anchor2) == 1, t.count(anchor2)
add = """

### The SATURDAY run reads an empty feed too, for a different reason (found 2026-09-05)

Same empty file, different cause, and worth separating so neither is mistaken for a fault. The Monday case above is the lag: Monday reads Sunday's build and arXiv announces nothing on Sunday. **A Saturday run that lands AFTER 04:00 UTC reads Saturday's own build, and arXiv does not announce on Saturday either.** The feed carries `<skipDays>` naming Saturday and Sunday explicitly.

Observed 2026-09-05 at 06:31 UTC: **892 bytes, zero `<item>` elements, `lastBuildDate` Sat, 05 Sep 2026 04:00:04 +0000**, byte-signature identical to the 2026-08-24 Monday observation. **No build was skipped and no paper was lost**; Friday's build was read by Friday's run. Log it as "feed empty, weekend build" and move on.

Practical consequence for the whole weekend: **a Friday-evening-through-Sunday window announces nothing**, so Saturday, Sunday and Monday runs all have an empty or stale arXiv lane by construction. Only Tuesday through Friday runs can return papers."""
t = t.replace(anchor2, anchor2 + add)
io.open(p, "w", encoding="utf-8", newline="\n").write(t)
print("Watchlist.md updated")
