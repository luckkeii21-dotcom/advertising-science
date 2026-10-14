# -*- coding: utf-8 -*-
"""Hot-layer (SKILL.md) update for the 2026-10-14 research run.

Three edits:
  1. Law 1 gets the second T1 sentence placing the creative in GEM's feature set,
     and the boundary MD-180 puts on the whole law.
  2. Law 3 gets Meta's own cold-start description and the push-delivery /
     creative-test mutual exclusion, which is an order-of-operations constraint.
  3. The dated preamble is rewritten for today's pass.
"""
import io
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
P = Path(r"E:\claude code marketing skill\.claude\skills\advertising-science\SKILL.md")
s = P.read_text(encoding="utf-8-sig")


def sub(hay, needle, repl, label):
    n = hay.count(needle)
    if n != 1:
        raise SystemExit("ANCHOR %s matched %d times, aborting" % (label, n))
    return hay.replace(needle, repl)


# ---- Law 1 -----------------------------------------------------------------
a = ("That is the architecture our \"creative is the targeting\" shorthand has been "
     "gesturing at.")
s = sub(s, a, a + (
    "\n**2026-10-14 restates the MD-120 sentence inside the CURRENT architecture, and "
    "the restatement is worth more than a second citation (MD-178, T1).** Meta's GEM "
    "post of 13 October defines the feature taxonomy of the new Kunlun architecture the "
    "same way: \"non-sequence features (such as user demographics, ad content "
    "representations), and sequence features with a sequence of events\". MD-120 proved "
    "the creative was a named input to the model as it stood in August 2026. This proves "
    "it is a named input to the model Meta shipped after that, inside a standing "
    "definition rather than as a passing example, and beside demographics in the same "
    "breath. **The limits are identical and do not move: it documents that the creative "
    "is an input, it does not rank the features, and it says nothing about avatars. The "
    "avatar half stays T3.**"
    "\n**The same post puts a hard boundary on this law, and the boundary belongs here "
    "rather than buried in the codex (MD-180, T1).** Meta reports that prediction quality "
    "follows a POWER LAW in the length of the user's engagement history, that it has "
    "doubled that context in production, and that \"larger models benefit "
    "disproportionately from longer sequences\". Put beside MD-090 (compute allocated by "
    "how much history a person carries), MD-174 (ranking depth varies with spare "
    "capacity) and MD-175 (the better model routed by predicted engagement), four "
    "independent T1 statements now say that a large share of match quality is a function "
    "of what Meta already knows about the PERSON. **Nothing in an account touches that "
    "input.** So the law is still the right instruction, because the creative remains the "
    "biggest thing we control, and the honest version of it carries the ceiling: an "
    "account selling to people who barely use the platform inherits the least of Meta's "
    "published gains, and we have never measured whether ours do. Never argue the law as "
    "though creative were the only input the machine reads."
), "law 1 tail")

# ---- Law 3 -----------------------------------------------------------------
a = ("**Low spenders, flipped to contested 2026-08-19.**")
s = sub(s, a, (
    "**2026-10-14: Meta published how it scores an ad it has never served, which is the "
    "one fact this whole argument has been missing (MD-179, T1).** Solaris precomputes "
    "the user-ad score in asynchronous background jobs before the live request needs it, "
    "and the fallback rule is quoted exactly: \"When an exact user-ad embedding is "
    "unavailable, the system degrades rather than drops. It substitutes an aggregate of "
    "the user's own recent embeddings across the same ad groups, or borrows from "
    "behaviorally similar users.\" **A new ad is therefore scored on borrowed "
    "intelligence rather than from zero.** Be strict about what that does and does not "
    "settle. It is about SCORING, not about spend allocation, so it does not decide "
    "whether killing a hog frees budget or craters the ad set, and both halves of this "
    "law stay contested. What it does kill is the folklore that a fresh ad enters "
    "delivery blind. It also means \"ad groups\", which is not an Ads Manager object, is "
    "Meta's own internal grouping and nobody may map it onto ad sets or campaigns.\n"
    "**And one hard constraint that changes the order of operations, read off the live "
    "product (MD-141, CR-113).** Push delivery and Meta's creative testing tool cannot "
    "both run in one campaign in one window. With push delivery on, the creative-test "
    "flow greys out with Meta's own copy: \"you're pushing delivery to one or more ads in "
    "this campaign. You can only set up a creative test after these push delivery periods "
    "have ended.\" The lock is at CAMPAIGN scope, so one ad under push delivery blocks "
    "creative testing across every ad set in it. Defaults are now on file too, 20% of "
    "daily budget and 7 days, and the control was present in about half of one large "
    "agency's accounts on 13 October 2026. **Pick the tool by conversion volume: push "
    "delivery moves one ad and reads out faster in a thin account, the creative testing "
    "tool fills 2 to 7 ads and needs several times the conversions.**\n"
    "**Low spenders, flipped to contested 2026-08-19.**"
), "law 3 low spenders")

# ---- dated preamble --------------------------------------------------------
a = ("Updated only when the codex changes at law level. Each law cites its claims; depth "
     "lives in the codex. **The 2026-10-08 research pass corrected one law-level statement "
     "written the day before,")
s = sub(s, a, (
    "Updated only when the codex changes at law level. Each law cites its claims; depth "
    "lives in the codex. **The 2026-10-14 research pass banked the biggest single T1 "
    "source of the month and amended two laws with it** (5 new claims: MD-176 to MD-180, "
    "plus GA-093; merges into MD-004, MD-029, MD-030, MD-031, MD-032, MD-141, CR-113, "
    "GA-073, GA-088 and LS-023). Meta published the 2026 generation of GEM on 13 October. "
    "**Three things in it matter at law level.** One, the creative's representation is "
    "named as a first-class feature of the CURRENT architecture, not just the August one, "
    "which is the second T1 sentence law 1 has ever had (MD-178). Two, prediction quality "
    "follows a power law in the length of the user's engagement history, which is the "
    "fourth independent T1 statement that match quality is largely a function of what "
    "Meta knows about the person, and that is the ceiling law 1 now carries (MD-180). "
    "Three, Meta described its cold-start path for the first time: an unseen user-ad pair "
    "inherits an aggregate of the user's own recent embeddings, or a behavioural "
    "neighbour's, rather than being scored from nothing (MD-179). **The headline numbers "
    "in the same post, 18.9% more conversions and 12% higher CTR, carry no footnote, no "
    "window on the first pair and an undefined population on the second, so they are not "
    "quotable to a client and not usable in a forecast (MD-177).** On the operating side, "
    "push delivery and the creative testing tool are now known to be mutually exclusive "
    "inside a campaign, and push delivery's defaults are 20% of daily budget over 7 days "
    "(MD-141). **The earlier 2026-10-08 research pass corrected one law-level statement "
    "written the day before,"
), "preamble")

P.write_text(s, encoding="utf-8")
print("SKILL.md: law 1 and law 3 amended, preamble updated")
