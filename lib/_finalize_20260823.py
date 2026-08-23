# -*- coding: utf-8 -*-
"""Mark the 25 read transcripts extracted and prepend today's Harvest Log entry."""
import glob
import os
import re

TR = (r"E:\claude code marketing skill\Obsidian God-level Marketing Vault"
      r"\God-level Marketing\wiki\sources\transcripts")
SCI = (r"E:\claude code marketing skill\Obsidian God-level Marketing Vault"
       r"\God-level Marketing\wiki\science")

PATS = [
    ("nick-theriot", "2026-08-21*Campaign Structure*"),
    ("nick-theriot", "2026-07-08*Most Successful Products*"),
    ("ben-heath", "2026-03-17*Retargeting Has Completely*"),
    ("ben-heath", "2026-05-05*BETTER Way To Do Meta Ads Targeting*"),
    ("ben-heath", "2026-03-27*Targeting Just Changed*"),
    ("ben-heath", "2026-03-31*Learning Limited*"),
    ("sam-piliero", "2026-03-09*Test Facebook Ad Creatives*"),
    ("sam-piliero", "2026-03-12*Everything You Need*"),
    ("sam-piliero", "2026-03-22*Fastest Growing Brands*"),
    ("sam-piliero", "2026-06-15*Algorithm Explained*"),
    ("fraser-cottrell", "2026-05-30*Winning Meta Ad Creatives*"),
    ("fraser-cottrell", "2026-05-10*Creative Diversity Post Andromeda*"),
    ("fraser-cottrell", "2026-02-08*500 Static Ads*"),
    ("fraser-cottrell", "2026-03-01*Hook Strategy*"),
    ("fraser-cottrell", "2026-04-28*300M in Ad Spend*"),
    ("charley-t", "2026-02-04*NEW BEST Way to Scale*"),
    ("charley-t", "2026-02-17*Creative Strategy*"),
    ("charley-t", "2026-03-24*15kDay*"),
    ("charley-t", "2026-05-17*BEST NEW Way to Scale*"),
    ("matt-shiver", "2026-05-26*ABO vs CBO*"),
    ("matt-shiver", "2026-05-19*Qualified Leads*"),
    ("matt-shiver", "2026-03-31*Double Your Leads*"),
    ("bluesense-digital", "2026-01-26*ABO vs CBO*"),
    ("bluesense-digital", "2026-03-12*8 Static Creatives*"),
    ("bluesense-digital", "2025-12-17*Learning Phase*"),
]

done = 0
words = 0
for ch, p in PATS:
    g = glob.glob(os.path.join(TR, ch, p))
    assert len(g) == 1, (ch, p, len(g))
    f = g[0]
    t = open(f, encoding="utf-8", errors="replace").read()
    words += len(t.split())
    t2 = re.sub(r"^extracted:\s*false\s*$", "extracted: true", t, count=1, flags=re.M)
    if t2 != t:
        open(f, "w", encoding="utf-8").write(t2)
        done += 1
print(f"marked extracted: {done}/25   words read: {words:,}")

# remaining backlog
rem = 0
for f in glob.glob(os.path.join(TR, "**", "*.md"), recursive=True):
    t = open(f, encoding="utf-8", errors="replace").read(3000)
    m = re.search(r"^extracted:\s*(\S+)", t, re.M)
    if m and m.group(1).lower() not in ("true", "yes"):
        rem += 1
print("backlog remaining:", rem)

ENTRY = """## 2026-08-23 (research run, 07:23 IST)

- Harvest: **0 new transcripts.** All 12 channels returned nothing, 0 harvester errors, 5 videos skipped under the length floor. A genuinely quiet harvest.
- Watchlist: **0 new items across every source that answers.** Meta Engineering 9 items and Meta Newsroom 10, both identical to cache. Google Ads & Commerce 20, identical. Meta for Business News 12 slugs live, all 12 already in the 17-slug union, newest date on page still 11 June 2026. Google Ads Announcements diffed 2,349 visible lines against yesterday's cache: **1 line added, 1 removed, both 19-digit session tokens.** Confirmed by running the fetch twice and watching the token change again, so the 2026-08-20 "it is a session token" reading is now verified rather than assumed. TikTok SDK changelog still v0.1.8. Sunday, so the 9 Monday-only sources were not due.
- **arXiv returned 0 items and the reason is structural, not a miss.** The feed served carried `<skipDays>Saturday, Sunday</skipDays>` and a Sat 22 Aug 04:00 UTC build with zero items. **arXiv does not publish on weekends.** So today's 0 is real and is not the 2.5-hour scheduling lag recorded on 2026-08-20. Both causes produce "0 new" and they need distinguishing in the log, which is why this line exists.
- TikTok Newsroom and the for-Business blog **deliberately not retried**, per the permanent India geo-block. Only the SDK changelog was read, so **TikTok is not logged as clean today.**

### The day's work was the backlog, and it was a VOCABULARY pass

Zero new material arrived, so the run went at the 242-transcript backlog under the runbook's 25-a-day rule. **25 transcripts, 79,000+ words, read in full by 7 extraction agents, one per channel.** Selection weighted to 2026 and aimed deliberately at the laws currently contested. **This also closes the gap left by the 2026-08-22 run that died mid-flight:** the Nick Theriot campaign-structure transcript it harvested but never read is in this batch.

**Codex 962 to 972 claims** (68 T1, 93 T2, 681 T3, 130 T4; 882 active, 85 contested, 5 superseded). 6 amendments, 10 new IDs, no duplicate IDs, counts recomputed from the topic files. Backlog 242 to 217.

**The headline is that three of the widest fights in the codex turned out to be operators answering different questions.** Today dissolved more disagreement than it created, which is a different and rarer result than the last three passes, all of which converted false confidence into recorded contest.

### ⚠ Law 3: the single voice on the kill side is not saying what we recorded

- We had Charley T as the lone operator saying "kill the budget hog so the others can spend", against three operators plus a Meta statement. Read in full, **he never says that.** He says kill the worst-PROFIT ad among the top spenders: "Look at the ads spending the most money, and identify the ones making you the least profit per sale."
- He also supplies a brake nobody else in the contest has, now SC-132: **"Turning off ads is the same thing as changing the budget. So, never turn off more than 20% of the spend on any day."**
- **Nobody in this contest defends killing a PROFITABLE high spender.** The four leave-on voices defend profitable top spenders, he cuts unprofitable ones. Most of the apparent 4-to-1 split was a disagreement about which ad was being described. What survives is narrow: whether an unprofitable-LOOKING top spender is actually unprofitable or is a top-of-funnel engine. Still zero controlled data.

### ⚠ Law 4a: "few ads" contains MORE creative variants than "20-plus ads"

- Charley T's structure stated plainly: **5 ad objects per ad set, each a 3x2x2**, which is about **60 creative combinations live**. Against Ben Heath's 20-plus he is not running fewer creative variants. He is running fewer AD OBJECTS with variation pushed inside the ad unit.
- Shiver's unit pinned: **5 to 10 live-concurrent in one ABO ad set at a $100/day floor.** Two things this codex attributed to him are NOT in his transcripts, the $200/day figure and the ten-ad-sets-at-$5 anti-pattern line.
- Blue Sense gives 3 to 6, up to 10, then says the sentence that should end most of these arguments: **"transparently nobody knows what the actual right amount is."**
- Theriot, after SEVEN transcripts, still states no live count. New and better than the revenue ladder we had: his launch rate is set by **headcount**. "That's just cuz what my creative strategists are paid to do."

### ⚠ Law 7: a step size is a CEILING PER QUALIFYING DAY, not a growth rate (SC-134)

- Theriot says "bumping up that budget by 20% a day" on a screen-shared account, and in the same breath dates its history: $100/day to $5,000/day over **almost a year**. Compounding 20% daily covers that in about **22 days**. It took roughly 365.
- So the realised average step is a small fraction of 1% per day. **Anyone reading a percentage as a plan models 50x in three weeks and is wrong by a factor of sixteen.** That plausibly explains the entire 3%-to-100% spread: ceilings and realised cadences are different quantities. Same failure mode as live-versus-launched ad counts.
- **Piliero now has a THIRD incompatible figure**, "doubling spend is common practice. We don't worry about increasing by 10 or 12 or 15%", which explicitly rejects the band we have him inside. **His step-size testimony is no longer usable as a point estimate.**
- Charley T publishes three named methods, not one number: linear ($10-50/day), fractional (2% daily), marginal (the margin between actual and target CPA, 7-day lookback). He is the only operator on file with a scale-down protocol: half the up-speed, then **48 to 72 hours untouched**.

### Other laws that moved

- **Law 1a.** Strongest UI reading yet. Heath names Meta's "controls" and "suggestion audience" sections off the screen and demonstrates both hardening switches. **Then contradicts himself ten days later** with detailed targeting being "always" a suggestion. Never accept a blanket claim without the account and the date.
- **Law 5.** The 50 is soft in both directions. Heath sees exits at 20 and 40 a week and has never seen above 50 stay limited. Blue Sense: **"for 90% of ad accounts... The answer is you don't."** His upstream-cascade model is banked at LS-063 and is explicitly **T3 assertion, not documentation**, since he shows no Meta page at any point.
- **The most actionable thing in the pass, and it applies to every account we run (LS-063).** In the sub-threshold state ad-level CPM drives allocation, and video CPMs sit above image CPMs, so a mixed-format ad set pools spend into the statics and **the video never gets read**. We mix statics and video in one ad set routinely.
- **Law 4b.** The vocabulary half is closed. Theriot's definition confirmed in the UI: three videos identical, varying only the VISUAL hook, so a hook swap cannot carry a new argument by construction. And the empirical half moved slightly: Fraser Cottrell now CLAIMS a re-cut revived a fatigued ad, with no before, no after and no spend, attributing it to a guess. One assertion is not evidence.
- **Law 2.** The collapse side got its most confident statement yet and still showed nothing. Fraser asserts every ad carries a "similarity score... behind the scenes in Meta". His whole evidence is eyeballing two thumbnail grids, and he concedes the account he calls collapsed **is currently working**. Four operators, eight months, still no entity ID and no unique-reach figure from anyone.

### New shown data (T2 rose 90 to 93)

- **MD-116.** A campaign configured cold spent **$80,000 with about 40% going to engaged and existing customers, and took more than half of its 942 purchases there.** The measured consequence of law 1a, and the instrument is free. **Never opened on any of our five accounts.**
- **CR-175.** Renaming a lead magnet with the creative held identical: **CPL $6.10 to $4.14 to $3.33**, CTR 1.50% to 2.14% to 2.68%. Mechanism is specificity plus a format noun. Honest limits: $30-50 per variant over 3-4 days, and landing pages were not matched, so part of the gain is click-side. **The cheapest test we are not running on any lead-gen client.**
- **MD-117.** Meta's creative testing tool guarantees test ads a **floor, not an equal split**, and the incumbent can be starved. Observed split $30/$30/$50 against an intended even one. A creative test left running past the point a winner emerges is no longer a clean test.

### Gaps and honest notes

- **Re-source owed on two Piliero claims.** Four of his transcripts read in full and neither "4 to 6 live ads is the sweet spot" nor "purchase only, never add to cart" appears in any. Probably sourced to earlier videos, so this is verification and not refutation, but his 2026-06-15 video argues near the opposite on events.
- **Title numbers are not evidence, and this batch was full of them.** "$100K/Day" never appears in the Theriot transcript at all (he says $5.4M in trailing-30-day agency-wide client spend, and the only figure on screen is one account at $5,000/day). "500 static ads" becomes "hundreds" in the body. "$450M" and "$300M" appear only in titles. All credentialing.
- **The AI-creative finding survives another 5 creative-heavy transcripts unchanged (CR-169).** Still zero comparisons against non-AI creative. Every stated advantage remains speed, cost or volume.
- **One item refused outright.** Blue Sense on specificity: "it immediately builds authority, despite it might not even being true when you've just made it up." The specificity principle is banked. The fabrication half is an FTC and Meta-policy breach and is incompatible with our chiropractic and vehicle-finance clients.
- Backlog stands at **217**, still overwhelmingly Blue Sense (101 at the start of today) and 2025-dated.

"""

p = os.path.join(SCI, "Harvest Log.md")
t = open(p, encoding="utf-8").read()
anchor = "One line per Research run: what came in, what changed. Quiet days get one line and nothing else.\n"
assert anchor in t, "harvest log anchor missing"
if "## 2026-08-23" in t:
    print("harvest log entry already present, skipped")
else:
    t = t.replace(anchor, anchor + "\n" + ENTRY, 1)
    open(p, "w", encoding="utf-8").write(t)
    print("harvest log entry written")
