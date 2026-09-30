"""Hot-layer edit for the 2026-09-30 research run: law 4b plus one watch item."""
from pathlib import Path

P = Path(r"E:\claude code marketing skill\.claude\skills\advertising-science\SKILL.md")

b = P.read_bytes()
nl = "\r\n" if b"\r\n" in b else "\n"
lines = b.decode("utf-8").replace("\r\n", "\n").split("\n")

LAW4B = (
    "**\u26a0 2026-09-30: META NOW SHIPS THE HOOK SWAP AS A BUTTON, which kills the delivery-penalty half of this law "
    "and leaves the empirical half exactly where it was (MD-168, T2; CR-124 amended).** Ads Creative Studio, in "
    "pre-release on a small number of accounts and heading for a broad rollout, offers \"try new video hooks\" as a named "
    "lever on a proven asset, describes it in Meta's own interface copy as **\"swap out the first 3 to 5 seconds of a "
    "video with a different approach\"**, gives a hook-type menu (satisfying intro, emotional storytelling, skit, fear of "
    "missing out, auto), and then generates the variants. **Read that against the Fraser Cottrell line quoted above, "
    "\"Simple hook changes or headline swaps simply don't count as creative testing in Meta's eyes anymore.\" Meta built a "
    "generator for it.** The penalty story is folklore with the platform standing on the other side of it. **Nothing "
    "empirical moves.** A platform recommending a move is not a measured result, Meta sells inventory when advertisers "
    "ship assets, and the studio publishes no outcome data for anything it generates. The surviving question is "
    "unchanged: does re-cutting the first 3 to 5 seconds of an EXISTING shoot revive a fatigued winner? Nobody has run it."
)

anchor = next(i for i, l in enumerate(lines)
              if l.startswith("**The same pass banked the body-side craft that the retraction points at"))
lines.insert(anchor + 1, LAW4B)

WATCH = (
    "- **\u26a0 Ads Creative Studio is arriving in Ads Manager and it changes two things we do by hand (MD-168, CR-281, "
    "2026-09-30).** All tools, then under Advertise, \"Ads creative studio\". Pre-release on a small number of accounts, "
    "broad rollout expected soon. **Check every client account for it.** Two reasons it matters before any of its "
    "generated creative does. It reports **hook rate, hold rate and thruplay natively**, which retires the custom-metric "
    "build we use in the weekly reports (CR-176). And it publishes a **numeric minimum performance threshold per account "
    "and per format**, 2.92% click-through for image ads and $20.13 cost per result on the one account seen, where Ads "
    "Manager previously gave only Above average / Average / Below average. **The threshold carries a slider, so the "
    "advertiser sets it: it is a reporting filter, never a market benchmark, and it must never reach a client report as "
    "one.** When it lands on our accounts, read each default threshold BEFORE touching the slider and compare it to that "
    "account's own trailing click-through rate; if the default is just the account's history, Meta's competitor-data "
    "story is decoration."
)

wi = next(i for i, l in enumerate(lines) if l.startswith("## Current watch items"))
ins = next(i for i in range(wi, len(lines)) if lines[i].startswith("- "))
lines.insert(ins, WATCH)

P.write_bytes(nl.join(lines).encode("utf-8"))
print("SKILL.md: law 4b block added at line %d, watch item added at line %d" % (anchor + 2, ins + 1))
