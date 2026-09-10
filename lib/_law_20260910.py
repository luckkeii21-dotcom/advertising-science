# Hot-layer (SKILL.md) amendments, 2026-09-10
import io

P = r"E:\claude code marketing skill\.claude\skills\advertising-science\SKILL.md"
s = io.open(P, encoding="utf-8").read()
before = len(s)

# --- 1. Amend the placement law with today's two additions -------------------
a = ("**Read MD-150's scope guards before repeating any of this to a client:** Meta has announced nothing, coverage "
     "on 2026-08-25 found the Business Help Centre still describing manual placement selection as available, the "
     "unofficial scope is Sales and Leads objectives only with sensitive verticals excluded, and our own 2026-09-09 "
     "account read found all four controls still present.")
assert s.count(a) == 1, ("anchor a", s.count(a))
s = s.replace(
    a,
    a + " **Two additions on 2026-09-10.** The account-wide lever is smaller than it sounds: it covers exactly three "
        "things, Audience Network, Facebook Marketplace and Facebook right column, so no feed, Reels or Stories "
        "placement can be switched off by any surviving control (MD-151). And the reason this may cost us nothing is "
        "an empirical claim we have never checked: under conversion optimisation Meta reportedly does not meaningfully "
        "spend on Audience Network in the first place, so the pruning being withdrawn was protecting against a risk "
        "that was not there (MD-152, T3, asserted for purchases and explicitly HEDGED for leads, which is our entire "
        "book). **The instrument is a placement breakdown in Ads Manager on a live client account and we have never "
        "run one. Read it as share of spend, never as conversion rate by placement.**",
    1,
)

# --- 2. Amend the competitor-research paragraph -----------------------------
b = ("**The competitor-research instrument at CR-190 degraded and nobody had noticed.**")
assert s.count(b) == 1, ("anchor b", s.count(b))
add = (
    "**Duplicate count is not a winner signal on its own, corrected 2026-09-10 (CR-206), and this one cuts at our own "
    "practice.** We treat an ad kept active AND duplicated as a confirmed winner. Kept active survives untouched. "
    "Duplication does not, because an advertiser also duplicates an ad that was disapproved or switched off and needs "
    "relaunching, and duplicates one sideways into another country or campaign where it proves nothing about this one. "
    "From outside an account the three causes look identical. **Read duplication with a companion signal, spend rank or "
    "growth direction, or do not read it.** Same pass: runtime alone was already broken and now has a second operator "
    "saying so from a different instrument (CR-190). **And every operator on this roster teaching competitor research "
    "is now demonstrating a paid tool, two of them disclosing sponsorship or a paid link on camera. Bank their methods, "
    "never their estimated spend, rank or revenue figures, none of which anyone has ever validated against an account "
    "whose real numbers are known.**\n\n"
)
s = s.replace(b, add + b, 1)

# --- 3. New attribution law: find the word ----------------------------------
c = ("11. **Never quote Meta's Incremental Attribution to a client as a measured lift.")
assert s.count(c) == 1, ("anchor c", s.count(c))
law = (
    "11a. **Before repeating any platform-published case-study number, find the word (MD-153, added 2026-09-10).** "
    "*Incremental* or *lift* means somebody at least claims a holdout. *Increase*, *more*, *lower cost* or *compared to "
    "the same period last year* means a before-and-after, which is not evidence that the product caused anything. "
    "Meta's own 2026-09-03 post prints both kinds side by side with no visual distinction: three of its five advertiser "
    "results use incrementality language, and two do not, including a straight year-over-year booking comparison. **No "
    "methodology, no test window, no holdout size and no absolute figures are published for any of the five.** The rule "
    "generalises past Meta, and it is the same discipline our client-reporting law already demands of us.\n\n"
)
s = s.replace(c, law + c, 1)

io.open(P, "w", encoding="utf-8").write(s)
print("SKILL ok", before, "->", len(s))
