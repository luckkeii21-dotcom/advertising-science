# -*- coding: utf-8 -*-
"""2026-10-17 research merge. Sources actually read this run:
   - Nick Theriot, "$30k/day Facebook Ads Campaign Structure", 2026-10-16 (transcript, 3,615 words)
   - Meta for Business News, "Creative diversification at scale: how Nest builds for the way
     Meta technologies work now", slug meta-nest-ai-creative-diversification (read in full, US shelf)
"""
import io
import re
from pathlib import Path

SCI = Path("Obsidian God-level Marketing Vault/God-level Marketing/wiki/science")


def read(p):
    return io.open(SCI / p, encoding="utf-8").read()


def write(p, s):
    io.open(SCI / p, "w", encoding="utf-8", newline="\n").write(s)


def merge_into(text, claim_id, paragraph, source_add=None, touched="2026-10-17"):
    """Insert a paragraph before the Sources: line of claim_id, optionally append a source."""
    m = re.search(r"^### " + re.escape(claim_id) + r"\b.*?(?=^### |\Z)", text, re.S | re.M)
    if not m:
        raise SystemExit("claim block not found: " + claim_id)
    block = m.group(0)
    sm = re.search(r"^Sources: (.*)$", block, re.M)
    if not sm:
        raise SystemExit("no Sources line in " + claim_id)
    new = block
    if paragraph:
        new = new[:sm.start()] + paragraph.strip() + "\n\n" + new[sm.start():]
    if source_add:
        sm2 = re.search(r"^Sources: (.*)$", new, re.M)
        new = new.replace(sm2.group(0), sm2.group(0).rstrip() + "; " + source_add, 1)
    new = re.sub(r"^Last touched: .*$", "Last touched: " + touched, new, count=1, flags=re.M)
    return text[:m.start()] + new + text[m.end():]


def append_claim(text, claim_md):
    return text.rstrip("\n") + "\n\n" + claim_md.strip("\n") + "\n"


THERIOT = "Nick Theriot, $30k/day Facebook Ads Campaign Structure, 2026-10-16"

# ---------------------------------------------------------------- Scaling Models
sm = read("Scaling Models.md")

sm = merge_into(sm, "SC-001", """
**Theriot's lookback window moved for a THIRD time, 2026-10-16, and the new entry supplies the rule
that picks the window.** The 2026-08-31 restatement above records him reading the cost-per-purchase
gate on a 30-day average and arguing explicitly against operators "who literally look at a day to
day". Today he reads YESTERDAY by default: "all we do is look at yesterday, and then if this CPA is
below, I think it's like $22 for this account... as long as it's below that, then we scale", on a
campaign at $6,000/day. The selector is account variance, not preference, and the full rule is
banked at [[Scaling Models#SC-178|SC-178]]. **The 20% step itself is unchanged at a fifth date**, and
he still names the rejected alternative, so the step size is the stable part of his protocol and the
window is not.

**He also states the anti-collapse reason the scale-DOWN prescriptions in this claim do not carry.**
Charley T's half-speed-then-hold and Heath's 3% taper with a neutral band both describe HOW to come
down. Theriot argues against coming down at all unless the account is losing badly, and his reason is
recovery time rather than delivery: "if I go from $6,000 a day, scale all the way down to $600 a day,
I find a new winner, it's like, great, it picked up performance, but it's going to be such a hard
climb to get all the way back to $6,000 a day. So, I'd rather try to hold that." Under his own 20%
ceiling per qualifying day, a 10x climb needs about 13 qualifying days, and the realised cadence
measured elsewhere in this claim is one green light every 17 days, so the climb back from a 90% cut is
a multi-month project. **That prices the cut: cutting a budget spends the account's recovery runway,
and the asymmetry is arithmetic rather than a claim about Meta.** His decrease trigger is explicitly
severity-gated and he gives it in blood: a scrape gets left alone, "a full-on gash where we're just
pouring out blood" gets 20% a day for a few days. This is the same ordering as the ceiling move
recorded above, add creative before dropping the budget, arriving at a second date with a different
reason. Screen-shared account, no before-and-after on any hold decision.
""", source_add=THERIOT)

sm = merge_into(sm, "SC-095", """
**Theriot left an ad set running at 5x frequency on 2026-10-16, which is the same operator breaching
his own thresholds above by a factor of three, and the window and the unit are both different.** The
figures, read off the screen: an ad set at $20,000 of spend over 30 days, a $19 cost per purchase
against a $22 target, 5x frequency, carrying bottom-of-funnel statics launched for a sales event. His
verdict: "I'd be brain dead if I decided to turn off all the ads... because that's such a high
frequency here is because it's just converting a lower funnel traffic. That's still good because
those people are still new customers that we're acquiring." **Before anyone reads this as a
contradiction, check the axes.** The thresholds above are AD-level over 7 DAYS and this is AD-SET
level over 30 DAYS, which is the exact window-and-unit confusion this claim already warns about, now
produced inside one operator's own corpus. The honest reading is that his 1.46-to-1.5 early warning
says nothing about this number and this number refutes nothing. **What it does add is a documented
exception to reading frequency as a problem at all: a converting bottom-funnel ad set is allowed to
run hot, and the test applied was cost per purchase against target, never frequency.** Consistent
with his standing position, already recorded above, that he does not make decisions off frequency.
One ad set, numbers shown on screen, no comparison against the same ad set at a lower frequency.
""", source_add=THERIOT)

sm = merge_into(sm, "SC-009", """
**A third reason to delete low-spend ad sets appeared on 2026-10-16 and it is not a performance reason
at all, which matters because it looks identical to one in a change log.** Theriot prunes a campaign by
switching the window to lifetime, sorting by schedule to surface the oldest ad sets, and deleting the
ones that "barely spent anything like $2, $3". The purpose is to free slots against the
200-ad-set-per-campaign ceiling banked at [[Scaling Models#SC-179|SC-179]], not to stop a leak. **The
kill-side argument in this claim fires on cumulative spend at zero purchases, and the reserve-role
objection fires on ads that might pick up slack. Neither applies to a $2 ad set from two years ago
being cleared to make room.** Operating consequence for reading somebody else's account: a bulk ad-set
deletion on a long-lived campaign near 200 ad sets is housekeeping and should not be read as a
performance judgement.
""", source_add=THERIOT)

sm = append_claim(sm, """
### SC-178 - The budget-decision lookback window is set by the account's day-to-day variance, not by preference, and the same operator has now published three different windows
Tier: T3 · Status: active
**The rule, stated 2026-10-16 while screen-sharing a campaign at $6,000/day.** Read yesterday by
default and switch to a trailing 7 days when the account swings: "some accounts are a lot more, what I
would say, volatile, where like every day it's crazy, like huge swings up and down. And all I'll do
is, instead of looking at yesterday every day, I'll look at last 7 days every every day... but because
this account is pretty like straightforward, then I'll still look at yesterday." In the shown account
the two windows disagreed on the day and he followed yesterday: "last 7 days is saying don't scale".
So the window is a property of the account's variance and the operator picks it once, which is the
first time anyone on the roster has given a selector rather than a number.

**The same operator's own window has now been recorded at three values across three dates, and that
should lower confidence in any single one of them.** Yesterday (2026-10-16, default), trailing 7 days
(2026-10-16, volatile accounts), and a 30-day average (2026-08-31, stated as the standing rule and
stated explicitly AGAINST reading day to day). The 20% step size held across all three dates. **Read
his protocol as a stable step with an unstable window**, and never quote the window without its date.

**Why the selector is probably right even though the testimony is inconsistent.** It is the same
argument [[Scaling Models#SC-102|SC-102]] makes from the other side, where delivery volatility falls as
conversion volume rises, so a low-volume account swinging day to day is behaving as expected and a
day-level read there is a read of noise. Charley T's conditional rule carries the matching precondition
in [[Scaling Models#SC-001|SC-001]]: an account whose day-to-day performance is hyperbolic cannot run a
trailing-7-day rule at all and should sit on a flat linear step. Three operators therefore agree that
account variance governs the reading window and disagree on what to do about it.

**For our book this picks the window today, and it picks the longer one.** ChiroWorks, StayWell and the
two truck accounts all sit far below the volume where a single day carries a readable signal, so the
trailing window is the correct instrument on every one of them, and a yesterday-based scaling decision
on any of them is a reaction to noise. **The cheap test, and nobody has run it: take one account, log
what the yesterday rule and the trailing-7 rule each would have decided for 30 days, and count how
often they disagree and which one was right.** That is a paper test with no spend at risk and it would
turn this T3 into a T2 with our own numbers.
Sources: Nick Theriot, $30k/day Facebook Ads Campaign Structure, 2026-10-16; Nick Theriot (30-day window), 2026-08-31
Last touched: 2026-10-17

### SC-179 - A campaign holds at most 200 ad sets, so the "one new ad set per ad idea, never switch anything off" structure has a hard end and has to be pruned to continue
Tier: T3 · Status: active
**The ceiling, reported from hitting it 2026-10-16: "this campaign is 191 ad sets. At 200 ad sets, you
can't make any more ad sets."** The remedy he uses is to switch the window to lifetime, sort by schedule
to bring up the oldest entries, and delete the ad sets that spent $2 or $3, which frees slots without
touching anything carrying money. The campaign in question has taken $4.5 million lifetime over roughly
two years and holds about 600 creatives at his standard three per ad set.

**This is the first stated limit on a structure this codex recommends in several places.** The
add-an-ad-set-per-idea-inside-one-campaign pattern is the fix [[Scaling Models#SC-012|SC-012]]
prescribes against the doom cycle, it is the topology recorded for this operator in
[[Creative Science#CR-154|CR-154]], and no entry anywhere said it terminates. At his own launch rate of
roughly five ad sets a week, 200 slots is about 40 weeks from an empty campaign, so **a campaign run
this way reaches the ceiling inside a year and the maintenance is not optional.**

**Tiering, and what to check.** The 200 figure is a practitioner report of a platform limit rather than a
measured effect, so it sits at T3 by this codex's rules, and it is the kind of claim that is cheap to
promote: it is either in Meta's own published limits or it is not. **Nobody has checked it against Meta
documentation and that check is worth one search.** If it confirms, this becomes T1 and belongs with the
structural constraints alongside the 50-ads-per-ad-set ceiling at
[[Meta Delivery & Andromeda#MD-125|MD-125]]. Note the two limits multiply: 200 ad sets at 50 ads each is
a 10,000-ad campaign ceiling, far above anything our book will reach, so **the binding constraint on a
long-lived campaign is the ad-set count and not the ad count.**

**Not relevant to our accounts yet, and worth saying so.** Our longest-running client campaigns hold
single-digit to low-double-digit ad sets. This matters for reading somebody else's two-year-old account,
and for any client campaign we intend to keep alive for years rather than rebuild.
Sources: Nick Theriot, $30k/day Facebook Ads Campaign Structure, 2026-10-16
Last touched: 2026-10-17

### SC-180 - Inside a CBO the kill test for an AD SET is whether its spend damages the CAMPAIGN-level cost per result, not whether its own cost per result looks bad
Tier: T3 · Status: active
**The test, stated 2026-10-16: "I'm looking for ad sets that take a lot of spend and negatively impact
overall... overall meaning the overall CPA at the campaign level."** Both halves are required. A bad cost
per result on small spend fails the test and is left alone; the one ad set he named for switching off was
a $37 cost per purchase against a $22 target. And a frightening-looking ad set that is actually
converting gets defended rather than cut, which is the 5x-frequency case recorded in
[[Scaling Models#SC-095|SC-095]].

**The argument he answers is the one every operator gets asked, and his answer is about the direction of
causation.** The question he receives: an ad set is top of the account in spend with a bad cost per
result, the campaign overall is doing well, and the operator is sure killing it will help. His reply:
"Did campaigns start doing good when that one took a lot of spend? Well, yeah, coincidentally. That
particular ad set took a lot of spend. It's bringing in a ton of top of funnel traffic and it's allowing
your other ads to convert." **The timing is the evidence and it is observational: the campaign improved
when the expensive ad set started spending.** He has not isolated it and neither has anybody else in this
codex.

**Where this sits against the rest of the file.** [[Scaling Models#SC-011|SC-011]] moves the kill
decision from ad level up to ad-set level, because ads inside an ad set sequence together. This moves it
one level further up, from ad set to campaign, and the mechanism is the same mechanism one level out: ad
sets inside a CBO are also not independent, because the budget is allocated at campaign level. That is
consistent with the documentation-side statement in [[Attribution & Incrementality]] that in CBO or
Advantage+ the whole budget distribution optimises against a campaign-level target, so no valid inference
is available at ad-set level. **The three levels now line up: in ABO read the ad set, in CBO read the
campaign, and in both cases the ad level is diagnostic only.**

**The operating form, which is what to actually do.** Before switching off any ad set in a CBO, read the
campaign-level cost per result with and without the period that ad set has been spending, and require the
campaign number to be the thing that got worse. The assist and reserve mechanisms in
[[Scaling Models#SC-009|SC-009]] are the same argument at ad level and are equally untested, so this is a
strong hypothesis and a bet, never a law. **Nobody has run the only test that would settle it: switch the
suspect ad set off and read the campaign for a week.**
Sources: Nick Theriot, $30k/day Facebook Ads Campaign Structure, 2026-10-16
Last touched: 2026-10-17
""")

write("Scaling Models.md", sm)
print("Scaling Models: SC-178, SC-179, SC-180 added; SC-001, SC-095, SC-009 merged")

# -------------------------------------------------------------- Creative Science
cs = read("Creative Science.md")

cs = merge_into(cs, "CR-154", """
**Theriot's "more would not break anything" became a reported action on 2026-10-16: he launched TWELVE
statics in one ad set.** Every earlier entry for him in this claim is an assertion about what would
happen ("if I go over four, if I go to 20, it's not going to break anything"). The event: a Labor Day
sale in early September, where his designer produced twelve statics instead of the standard three, "we
just created the ad set, we loaded in the 12 ads and we launched it. I didn't think anything of it."
That ad set is the $20,000-of-spend, $19-cost-per-purchase one recorded in
[[Scaling Models#SC-095|SC-095]], so it is the account's heaviest-spending ad set of the month and also
the one carrying four times his standard ad count. He names six as another observed count when the
design team has extra ideas. **This is still not a concurrency test: it is one ad set at twelve against
a book of ad sets at three, with no matched comparison and a sale offer confounding the performance.**
What it removes is the gap between his stated indifference to ad count and his observed behaviour,
which previously only ever ran at three.

**He also puts the argument at its bluntest, and it is worth quoting because it is the position this
whole claim is contested over:** "Some of you guys literally think that your success is dependent on how
many ads you put in an ad set or how many ad sets you have running in the campaign. I can tell you what,
it doesn't matter." He lists the structural superstitions he personally held and discarded over eleven
years, including raising budget only at certain hours, only to odd numbers, manipulating the values sent
to the pixel, and duplicating campaigns to reach a fresh audience pocket. **None of that is evidence
against any specific number in this claim, and it is the clearest statement on the roster of the prior
that structure is not the lever: "just create great creative, have a good offer, have a good product,
have a good product page, you'll be set."**
""", source_add=THERIOT)

cs = merge_into(cs, "CR-035", """
**Restated unchanged 2026-10-16, a fourth date, and the account behind it is the largest yet recorded
for this batch design.** "On average, we do three ads per ad idea, and that's going to be three videos
or three photos. The three videos are going to be exactly the same. The only difference is the visual
hook of each particular video is going to be different. Not a text hook, not what the person says in
the video as the hook, the visual hook, what people see for the first three to four seconds." For
photos, "three of the exact same photos, just a different background on each photo." The window is given
as three to four seconds here against three to five seconds on 2026-08-19, which is the same answer at
the resolution anyone can act on. **The account: $328,000 of spend over 30 days returning $1.03 million,
a stated 3.08 blended ROAS and a stated $112,000 of profit, with 13 new ad sets launched in September
inside one of its three campaigns.** Still no per-variant comparison shown for any batch, at any date,
which is the whole evidentiary hole in this claim and it is now four videos old.
""", source_add=THERIOT)

cs = append_claim(cs, """
### CR-286 - Meta published a partner case study tying AI-creative share of spend to revenue growth, and it fails both provenance tests this codex already applies: no named advertiser and no counterfactual
Tier: T3 · Status: active
**What the post is.** "Creative diversification at scale: how Nest builds for the way Meta technologies
work now", on Meta for Business News, dating itself 19 October 2026. Nest Commerce is described in the
post as "a UK performance agency specialising in scaling digital-first brands on Meta technologies", and
the subject is the agency's own product, "its AI performance and creative solution, Nest AI Creative",
which "turns a single brief into multiple platform-native variants". **This is an agency marketing its
own tool on the platform's channel, so the publisher is Meta and the measurer is the vendor.**

**The figures, quoted exactly.** Brands that "scaled to an average of 40% of spend" on the tool saw
"revenue grow 70%, with 20% higher CVR" against non-AI creative. One health brand at 57% of spend saw "5%
lower cost per result and 17% higher CVR". Another at 20% of spend saw "56% higher ROAS". The composition
figures are "68% of spend on video against 38% across the benchmark" and "93% vertical-first video
adoption". The cohort: "In Q1 2026, Nest onboarded seven brands onto its Nest AI Creative platform",
across health and wellness, food and beverage, and home and lifestyle.

**The defects, and they are the ones the standing rule names.** This codex's rule since 2026-10-07 is to
find the population and the counterfactual before carrying any platform figure, and that when there is no
footnote the number is an illustration rather than a measurement. Here: **no footnote anywhere on the
page, no data window for the results, no definition of the benchmark the 38% video share is measured
against, and not one of the seven brands is named**, which is exactly the check
[[Attribution & Incrementality#AT-126|AT-126]] exists to force on this source. **The counterfactual is
worse than absent, it is structurally impossible as stated.** Seven brands that chose to onboard a new
creative platform in one quarter are selected on budget, on appetite and on having creative headroom
before any variant is generated, and "40% of spend on the tool" is itself an outcome of the account doing
well enough to keep feeding it. **Revenue growing 70% alongside a rising AI-creative share is a
correlation in seven self-selected accounts with no holdout.** The one sentence in the post that carries a
mechanism is the agency CEO's, and it is a restatement of what this codex already holds at law level:
"The Meta ad delivery system rewards creative diversity, and we've built our approach around that
insight."

**What is usable.** The direction only, and only as corroboration of claims that already stand on better
evidence: variant volume from one brief, video-heavy composition and vertical-first framing are what a
delivery-led account looks like, which is the format-and-style diversification argument already banked in
[[Creative Science#CR-154|CR-154]] and in the diversification material above. **Never quote 70%, 20%,
56%, 17% or 5% to a client or put any of them in a forecast.** The honest sentence for a client
conversation is that agencies running high AI-variant volume report better outcomes and nobody has
published a controlled comparison.

**One thing in it is cheap and worth copying: the share-of-spend framing.** Reporting AI or
newly-generated creative as a PERCENTAGE OF SPEND rather than as a count of ads is a better instrument
than an ad count, because it prices the creative by what delivery actually bought, which is the same
correction [[Scaling Models#SC-009|SC-009]] reaches on the kill side. We do not currently track that
number on any client account and it is one breakdown away.
Sources: Meta for Business News, Creative diversification at scale: how Nest builds for the way Meta technologies work now, dated 19 October 2026, read 2026-10-17
Last touched: 2026-10-17
""")

write("Creative Science.md", cs)
print("Creative Science: CR-286 added; CR-154, CR-035 merged")
