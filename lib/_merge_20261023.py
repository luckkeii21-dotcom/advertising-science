# -*- coding: utf-8 -*-
"""2026-10-23 research merge. One transcript (Jon Loomer, frequency/fatigue) and
one duplicate arXiv re-submission. CR-116 -> contested, CR-027 source + block,
new CR-288, LS-084 source note, Watchlist dedup note."""
import sys
from pathlib import Path

SCI = Path(r"E:\claude code marketing skill\Obsidian God-level Marketing Vault\God-level Marketing\wiki\science")
LOOMER = "Jon Loomer, When Does Frequency Lead to Creative Fatigue, 2026-10-21"


def rd(p):
    return p.read_text(encoding="utf-8")


def wr(p, s):
    p.write_text(s, encoding="utf-8")


def must(cond, msg):
    if not cond:
        print("ABORT: " + msg)
        sys.exit(1)


# ---------------- Creative Science ----------------
cs = SCI / "Creative Science.md"
t = rd(cs)
orig = t

# --- CR-116: active -> contested, add counter-case block, add source ---
cr116_head = ("### CR-116 \u00b7 Purchase probability collapses after two impressions of the SAME "
              "creative, but holds if impressions three and four are novel creatives\n"
              "Tier: T3 \u00b7 Status: active\n")
must(cr116_head in t, "CR-116 header/status not found")
t = t.replace(cr116_head, cr116_head.replace("Status: active", "Status: contested"), 1)

anchor116 = ("Run the diagnostic before accepting any of this: open the account, compare ad-level "
             "frequency with account-level frequency over 30 days on cold campaigns. If ad-level "
             "frequency is already above 2, the account is short of live creative regardless of what "
             "the fatigue debate in [[Creative Science#CR-027|CR-027]] concludes.\n")
must(anchor116 in t, "CR-116 diagnostic anchor not found")

block116 = anchor116 + """
**A COUNTER-CASE TO THE "ABOVE 2" THRESHOLD, 2026-10-21, and it is the first one with spend attached.** Jon Loomer reports a campaign on a broad US audience that has spent more than $450,000 at a total frequency of 4.5, containing two ads that have each spent about $150,000 at an ad-level frequency of about 3.0. Both ad-level figures sit above the 2.0 threshold this claim converts into an audit, and above the 2.2 generous buffer. His reported outcome is the opposite of what the threshold predicts: "frequency isn't a problem. Creative fatigue hasn't happened and in fact, results are only getting better month after month." He also names the account as a deliberate violation of creative diversity practice, "a higher budget going to a small number of ads over a long period of time", which closes the obvious escape that frequency stayed survivable because many assets shared the load.

**What this overturns and what it leaves standing.** It does not touch the curve, because nobody has measured per-impression purchase probability on either side. What it contradicts is the OPERATING THRESHOLD, the instruction to read ad-level frequency above 2 as a creative shortage. One account held 3.0 at the ad level across $150,000 per ad while improving month over month, so the threshold is not a general rule and must not be quoted as one. Status moves to contested on that basis.

**The condition Loomer puts in its place, which is where both sides can still be right.** He attributes harmful frequency to audience size rather than impression count, so the threshold only bites where the pool was deliberately shrunk: "If you intentionally shrink your audience, frequency is more likely to be a problem. This is especially the case for local businesses with a reasonable budget. But it's also true for remarketing. These audiences exhaust quickly." Under that reading Blue Sense's sub-2 observation and Loomer's 3.0 are both real and describe different pool sizes, which is the cluster-versus-population split left unresolved at [[Creative Science#CR-027|CR-027]]. **The read that survives both: frequency is a symptom of pool size, not a standalone creative-health metric, so check the audience definition before accepting the creative-shortage diagnosis.** That bites directly on our own local-service accounts, where the pool genuinely is small and the threshold may well hold.

**One mechanism claim attached, unmeasured.** "Meta does dynamically cycle your ads to avoid high frequencies that would lead to creative fatigue if you let them." That is the same behaviour Blue Sense infers from the gap between ad-level and account-level frequency above, asserted from the other direction, and it carries an operator warning: refreshing on a fixed weekly or monthly cadence overrides the cycling. Neither source measured it.

**Guards on the counter-case.** No dashboard shown, no CPA, ROAS or date range, and the figures are stated from memory on camera. Loomer also says he has "very little control over the refreshing of ads" on that account and calls that "obviously not ideal", so the low creative diversity was a constraint he inherited rather than a designed test. T3 against T3, which is why this contests the threshold rather than superseding it.
"""
t = t.replace(anchor116, block116, 1)

src116 = ("Sources: Blue Sense Digital, How to Scale an eCommerce Brand Profitably in 2026: The Full "
          "System, 2026-06-15; Blue Sense Digital, Meta Ads Creative Strategy in 2026: The Full "
          "System, 2026-05-11; Andrew Faris, Your Meta Ads Account Has Too Many Campaigns, "
          "2026-05-12; Blue Sense Digital, How Machine Learning Works in Meta Ads (2025), "
          "2025-03-25\nLast touched: 2026-08-19\n")
must(src116 in t, "CR-116 sources line not found")
t = t.replace(src116,
              src116.replace("2025-03-25\nLast touched: 2026-08-19",
                             "2025-03-25; " + LOOMER + "\nLast touched: 2026-10-23"), 1)

# --- CR-027: add Loomer position + source ---
src027 = ("Sources: Ben Heath, $100 vs $100,000 Facebook Ads Strategy, 2026-08-12; Professor "
          "Charley T, The NEW BEST Meta Ads Andromeda Course to Scale in 2026, 2026-01-24;")
must(src027 in t, "CR-027 sources line not found")
block027 = """
**A FOURTH POSITION, 2026-10-21, and it sits in Charley's camp with a more specific mechanism.** Jon Loomer agrees the usual fatigue diagnosis is wrong but does not route it through launch cannibalisation. His mechanism is warm-pool exhaustion: "your ads were good enough to succeed with people who know you, but they fail when your performance relies on new eyeballs. That's why your ads die after a week or two. Cuz you've exhausted your built-in remarketing audiences, the lowest hanging fruit." The verdict he draws is about creative quality rather than delivery: "your problem isn't frequency or creative fatigue. Your problem is that your ads aren't good enough to get the results you want from new audiences. Otherwise, your performance wouldn't tank after initially starting strong."

**Why this is worth more than another voice on the pile.** It accounts for the one-to-two-week death clock that both existing camps cite without either explaining its length, and it predicts something neither Ben's market dynamics nor Charley's cannibalisation does: decay should track the size of the account's warm pool, so a brand with a large existing customer and engager base should hold a strong opening longer than a cold brand at identical spend. **That is testable on our own accounts without spending anything extra, by comparing the first-fortnight decay of a new winner against the size of the account's warm custom audiences.** It also rejects population exhaustion at broad targeting, agreeing with Charley, while putting the real exhaustion in a pool smaller than a cluster, which narrows the unresolved question above rather than restating it.

**Guard.** Loomer attaches no account, no numbers and no date range to this half of his argument, and the word he uses is a bet: "What I bet is happening". Hypothesis with a clean test, not a finding.
"""
t = t.replace(src027, block027 + src027, 1)
t = t.replace(
    "Professor Charley T, Copy This Facebook Ads Strategy (Post-Andromeda), 2026-02-07\n"
    "Last touched: 2026-08-20\n\n### CR-028",
    "Professor Charley T, Copy This Facebook Ads Strategy (Post-Andromeda), 2026-02-07; "
    + LOOMER + "\nLast touched: 2026-10-23\n\n### CR-028", 1)

# --- CR-288: new claim appended ---
must("### CR-288" not in t, "CR-288 already exists")
cr288 = """
### CR-288 \u00b7 Meta labels an ad with creative fatigue, so treat the ABSENCE of that label as evidence against the fatigue diagnosis
Tier: T3 \u00b7 Status: active
The rule, from Jon Loomer on 2026-10-21: "Meta will tell you if frequency is a problem. Your ads will get a label of creative fatigue. And that's a sign that, yes, people have seen your ad or ads too many times, and you need to create something different. But don't assume that will happen. And achieving creative fatigue is likely way more difficult than you think." Used as a gate rather than as advice: before diagnosing fatigue off a performance drop, check whether Meta has applied the label, and if it has not, go looking for a different cause.

**Why one sentence from one operator earns an ID.** Every fatigue claim in this codex is argued from inferred evidence, a frequency number, a spend curve, a CPA rise, and the debate at [[Creative Science#CR-027|CR-027]] has run for months without either side producing a first-party readout. This points at one that either appears in the interface or does not, which makes it the cheapest check available and the only one that needs no theory. When the label IS present, his prescription matches the rest of the corpus: "the solution is always to create more ads."

**The guards, and they decide how far to trust it.** He describes what the label means without showing it, names no location in Ads Manager, and gives no case where its presence or absence was checked against an outcome. Meta's own diagnostic surfaces have a recorded history of recommending a setting that was already enabled, see [[Meta Delivery & Andromeda#MD-105|MD-105]], so a label is a signal and not a verdict. **Verify the label exists and where it reads before leaning on this on a client account.** It is the check both [[Creative Science#CR-027|CR-027]] and [[Creative Science#CR-116|CR-116]] lack.
Sources: """ + LOOMER + """
Last touched: 2026-10-23
"""
t = t.rstrip("\n") + "\n" + cr288
must(t != orig, "Creative Science unchanged")
wr(cs, t)
print("Creative Science.md: CR-116 contested, CR-027 extended, CR-288 added")

# ---------------- Learning & Signal ----------------
ls = SCI / "Learning & Signal.md"
t = rd(ls)
src084 = ("Sources: arXiv 2607.26621v3, OneLatent: Latent Reasoning for Efficient Foundation "
          "Recommendation Models, arxiv.org/abs/2607.26621, abstract read in full 2026-09-30\n"
          "Last touched: 2026-09-30\n")
must(src084 in t, "LS-084 sources line not found")
add084 = """
**THE SAME PAPER HAS NOW ARRIVED A THIRD TIME, UNDER A SECOND arXiv ID, 2026-10-23.** Today's cs.IR feed carried *OneLatent: Latent Reasoning for Efficient Foundation Recommendation Models* as arXiv 2610.30675, submitted 2026-10-22. The abstract was read in full and it is the same work reporting the same numbers: 17.44% on SID@64 against the Think variant, over 17x online inference throughput, and the identical single sentence on "an estimated 9.6% revenue lift" in Kuaishou's local-services advertising scenario against OneRec and OneReason. **No claim changes and nothing new was banked.**

**Recorded because the lineage is now a dedup problem.** This work has reached the watchlist as 2607.26621 v1 in July 2026 under the title *WhisperRec*, as 2607.26621v3 announced 2026-09-30 retitled *OneLatent*, and now as a fresh submission under a new ID. The watchlist diffs on item links, so **a re-submission under a new arXiv ID reads as a brand-new paper and will keep doing so**. Filter note added to Watchlist.md.
Sources: arXiv 2607.26621v3, OneLatent: Latent Reasoning for Efficient Foundation Recommendation Models, arxiv.org/abs/2607.26621, abstract read in full 2026-09-30; arXiv 2610.30675, OneLatent (same work, new submission), arxiv.org/abs/2610.30675, abstract read in full 2026-10-23
Last touched: 2026-10-23
"""
t = t.replace(src084, add084, 1)
wr(ls, t)
print("Learning & Signal.md: LS-084 duplicate submission recorded")

# ---------------- Watchlist ----------------
wl = SCI / "Watchlist.md"
t = rd(wl)
note = """

### arXiv dedup: the same paper can return under a NEW ID, not just a new version (2026-10-23)

The filter passed 1 item today, *OneLatent: Latent Reasoning for Efficient Foundation Recommendation
Models*, arXiv **2610.30675**, submitted 2026-10-22. It is the third arrival of one piece of work:

| Arrival | ID | Title | Outcome |
|---|---|---|---|
| July 2026 | 2607.26621 v1 | *WhisperRec* | not seen by the engine |
| 2026-09-30 | 2607.26621v3 | *OneLatent* (retitled) | banked as LS-084, T2 |
| 2026-10-23 | **2610.30675** | *OneLatent* | duplicate, nothing banked |

Same abstract, same numbers: 17.44% on SID@64, over 17x inference throughput, "an estimated 9.6%
revenue lift" in Kuaishou's local-services advertising scenario.

**Why the engine could not catch it.** The arXiv check diffs item LINKS against the seen cache. A
version replace keeps the base ID and so is catchable; a re-submission under a new ID shares no link
with anything cached and is indistinguishable from a new paper. **A title-level check would have caught
this one** and costs nothing, since titles are already parsed for the keyword filter. Worth shipping
into `lib/watchlist_check.py` as a normalised-title set alongside the link set, the same way the
answer-href set diff was shipped on 2026-09-20.

**Reading the abstract is still the only step that decided it**, which is now the third consecutive
entry to reach that conclusion.

### Google Ads & Commerce blog: a teaser named a feature with no documentation behind it (2026-10-23)

The feed's one new item, *New bidding and budgeting tools can transform your upcoming holiday ad
strategy*, published 2026-10-21, is a podcast announcement rather than a product post. It names
**"demand-led budgeting"**, already banked as [[Google Auction & Smart Bidding#GA-077|GA-077]], and
**"promotion mode"**, which the codex has never heard of. A support-doc search returned **no Google
documentation for "promotion mode" at all**. Nothing banked, because the page states no mechanics and
no primary source exists to read.

**This is the second time an Ads & Commerce podcast teaser has been the thing that surfaced an
undocumented Google feature name**, after the 2026-10-12 entry that produced GA-076, GA-077 and
GA-078. The pattern is worth naming: the teasers name features earlier than the docs publish them, so
a named feature with no doc is a GAP TO CARRY, never a claim to bank.
"""
t = t.rstrip("\n") + "\n" + note
wr(wl, t)
print("Watchlist.md: arXiv dedup + Google teaser notes added")
