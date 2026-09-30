"""Merge pass for the 2026-09-30 research run."""
from pathlib import Path

SCI = Path(r"E:\claude code marketing skill\Obsidian God-level Marketing Vault\God-level Marketing\wiki\science")


def load(name):
    b = (SCI / name).read_bytes()
    nl = "\r\n" if b"\r\n" in b else "\n"
    return b.decode("utf-8").replace("\r\n", "\n").split("\n"), nl


def save(name, lines, nl):
    (SCI / name).write_bytes(nl.join(lines).encode("utf-8"))


def bounds(lines, cid):
    s = next(i for i, l in enumerate(lines) if l.startswith("### " + cid + " "))
    e = next((i for i in range(s + 1, len(lines)) if lines[i].startswith("### ")), len(lines))
    return s, e


def insert_before(lines, cid, prefix, block):
    s, e = bounds(lines, cid)
    j = max(i for i in range(s, e) if lines[i].startswith(prefix))
    return lines[:j] + block + lines[j:]


def append_source(lines, cid, prefix, extra):
    s, e = bounds(lines, cid)
    j = max(i for i in range(s, e) if lines[i].startswith(prefix))
    lines[j] = lines[j].rstrip() + "; " + extra
    return lines


def set_touched(lines, cid, date):
    s, e = bounds(lines, cid)
    j = max(i for i in range(s, e) if lines[i].startswith("Last touched:"))
    lines[j] = "Last touched: " + date
    return lines


def append_claim(lines, text):
    while lines and lines[-1] == "":
        lines.pop()
    return lines + text.split("\n")


HEATH = ("Ben Heath, AI Just Changed Facebook Ads Forever!, 2026-09-29, "
         "youtube.com/watch?v=RTrRKB0iXwQ, 19 min, read in full")
MUSE = ("Meta Newsroom, The Future Is for Everyone: Muse for Small Business, 2026-09-29, "
        "about.fb.com/news/2026/09/introducing-muse-small-business/, read in full")

# ===================== Creative Science =====================
lines, nl = load("Creative Science.md")

CR124 = [
    "",
    "**META'S OWN PRODUCT NOW INSTRUCTS THE HOOK SWAP, 2026-09-29, and it settles one side of this argument at the source.** "
    "Ads Creative Studio ([[Meta Delivery & Andromeda#MD-168|MD-168]]) offers \"try new video hooks\" as a named lever on a proven asset, "
    "describes it in Meta's own interface copy as \"swap out the first 3 to 5 seconds of a video with a different approach\", gives the "
    "operator a hook-type menu (satisfying intro, emotional storytelling, skit, fear of missing out, or auto), and then generates the "
    "variants. **That is the exact operation this claim has failed to settle across four passes, recommended by the platform and built "
    "into the platform.**",
    "",
    "**What it settles.** The delivery folklore. Practitioners have circulated for a year that Meta penalises hook-only variants or no "
    "longer counts them as creative testing, and Fraser Cottrell's February 2026 position above is the strongest version of it on file. "
    "Meta shipping a button for the move is direct evidence against the penalty story.",
    "",
    "**What it does not settle, and the gap is the same size it was yesterday.** A platform recommending a move is not a measured result. "
    "Meta sells more inventory when advertisers ship more assets, and [[Meta Delivery & Andromeda#MD-105|MD-105]] already records this same "
    "recommendation engine telling a campaign to enable a setting that was already enabled. **The surviving empirical question is unchanged: "
    "does re-cutting the first 3 to 5 seconds of an EXISTING shoot revive a fatigued winner? Nobody has run it, including Meta, which shows "
    "no outcome data for anything the studio generates.**",
]
lines = insert_before(lines, "CR-124", "Added sources:", CR124)
lines = append_source(lines, "CR-124", "Added sources:", HEATH)
lines = set_touched(lines, "CR-124", "2026-09-30")

CR176 = [
    "**THE CUSTOM-METRIC BUILD IS BEING RETIRED BY META, 2026-09-29, and the finding above survives it intact.** The line above records that "
    "Meta does not provide hook rate natively. Ads Creative Studio ([[Meta Delivery & Andromeda#MD-168|MD-168]]) reports **hook rate, hold "
    "rate and thruplay as native columns** on its top-creatives leaderboard. Heath's read of why is that advertisers built these as custom "
    "metrics for long enough that Meta adopted them. The surface is in limited rollout, so keep the custom metric until the studio appears on "
    "an account. **Nothing in this claim changes.** A native column makes the metric cheaper to read. It does not make it predict cost per "
    "result, which is the whole reason this entry exists.",
]
lines = insert_before(lines, "CR-176", "Sources:", CR176)
lines = append_source(lines, "CR-176", "Sources:", HEATH)
lines = set_touched(lines, "CR-176", "2026-09-30")

CR281 = """
### CR-281 · Meta now shows a NUMBER for minimum acceptable creative performance, split by image and video, and the advertiser can move it with a slider, which is what tells you it is a reporting filter rather than a benchmark
Tier: T2 · Status: active
Read off one live account inside Ads Creative Studio ([[Meta Delivery & Andromeda#MD-168|MD-168]]), 2026-09-29. The figures were on screen. Their derivation was not.

**The figures as shown.** Click-through rate threshold for image ads **2.92%**. Cost per result threshold **$20.13**. Heath states the video click-through threshold is "a whole percent higher", so about 3.92%, and says the image and video cost-per-result thresholds differ slightly while reading very close. Record 2.92% and $20.13 as read, and the video figures as his description of the screen rather than as numbers.

**Why this is new information and not a restatement.** Until now the only creative grade Ads Manager published was Above average, Average or Below average. [[Creative Science#CR-248|CR-248]] measured what that grade is worth on our own accounts: it is a percentile against a pool the platform picks, and it returned Above average for 22 of 24 of our ads in one week, which is a column that does not separate the ads it grades. A number, split by format, carries more than a three-band grade does.

**The slider is the finding, and it should change how the number is read.** Each threshold carries a slider and a reset button, so the advertiser sets it. **A value the advertiser can move is not an auction input and is not a statement about what the market achieves.** It decides which of your own ads the studio flags as underperforming, and therefore which advice you are shown. Moving it changes what you get told. It does not change what you get charged. Never quote a threshold to a client as a category benchmark, and never print one in a report as Meta's benchmark for their industry.

**What is unsourced, and it is the interesting half.** Heath says the numbers come from "our data and also data from our competitors". That is his reading of the interface, not a Meta statement, and the screen carries no methodology, no window and no pool definition. If the cross-account half is real it is the same reach that makes [[Meta Delivery & Andromeda#MD-105|MD-105]] worth having. It is not established here.

**The cheap test, when the surface reaches us.** Read the default threshold on each account before touching the slider and compare it to that account's own trailing click-through rate. If the default is just the account's own history, the competitor story is decoration.
Sources: __HEATH__
Last touched: 2026-09-30
""".replace("__HEATH__", HEATH)
lines = append_claim(lines, CR281)
save("Creative Science.md", lines, nl)
print("Creative Science.md: CR-124 amended, CR-176 amended, CR-281 added")

# ===================== Learning & Signal =====================
lines, nl = load("Learning & Signal.md")

LS076 = [
    "**The boundary now has traffic across it, 2026-09-29.** Meta announced Muse for Small Business, which \"can connect your Instagram "
    "professional account analytics, Facebook Pages, and Meta ad accounts in a few clicks\", and published an advertising use case for it: "
    "analyse what is working and draft next week's campaign. **Muse reading an ad account runs the opposite direction from Muse conversations "
    "feeding the ad systems, so the sentence banked above is not contradicted and the tier is unchanged.** It is recorded because the two "
    "surfaces now sit inside one agent, which is the condition under which a launch-day commitment is most likely to be quietly revised. Full "
    "entry at [[Meta Delivery & Andromeda#MD-169|MD-169]].",
]
lines = insert_before(lines, "LS-076", "Sources:", LS076)
lines = append_source(lines, "LS-076", "Sources:", MUSE + " (context only)")
lines = set_touched(lines, "LS-076", "2026-09-30")

LS084 = """
### LS-084 · A second billion-user ad platform reports putting a large-model reasoning layer inside ad ranking, and reports the result in platform revenue: Kuaishou, 9.6% estimated lift in local-services advertising
Tier: T2 · Status: active
arXiv 2607.26621v3, *OneLatent: Latent Reasoning for Efficient Foundation Recommendation Models*, this version announced 2026-09-30. Abstract read in full. **It is a replace, not a new paper.** Version 1 dates to July 2026, so the work is not news and only this announcement is.

**What was built.** A foundation recommendation model that compresses chain-of-thought reasoning traces into a few learnable latent tokens, so the model reasons without generating the text of the reasoning. Reported against the explicit chain-of-thought variant: 17.44% on the paper's ranking metric and **over 17x online inference throughput**. The authors also built a production serving system for it.

**The advertising result, which is one sentence and an estimate.** "An online A/B test in Kuaishou's local-services advertising scenario shows that deploying OneLatent with this system yields an estimated 9.6% revenue lift over strong online baselines, including OneRec and OneReason."

**Why it earns an ID instead of a discard.** On its own it changes nothing we do. Beside [[Learning & Signal#LS-083|LS-083]], which recorded Tencent running a compressed shared user-behaviour representation in production for ten months, it makes two large ad platforms reporting the same architectural move inside one month: put a large-model reasoning or understanding layer into the ranking stack, then compress it until it is cheap enough to serve. **One observation is a company. Two is a direction**, and it is the direction Meta describes with unified representations. In both papers the binding constraint is serving throughput rather than accuracy, which is the part an operator should carry.

**Three limits, and they are large.** Kuaishou is neither Meta nor Google, so this is evidence about what a platform at that scale finds worth building. The lift is labelled "estimated", with no absolute baseline, no window and no spend. And **a revenue lift for the platform is not an advertiser's cost per result** and must never be quoted as one.

**Filter note for the watchlist.** The only bank-list term in the abstract is `advertis`, appearing once, in the second-to-last sentence. That is the outcome-clause shape recorded as a false-positive signature on 2026-09-07 and twice on 2026-09-25, and this one is a partial true positive: the deployment is genuinely inside an ad system while the method is not about advertising. Reading the abstract is again the only step that decided it, and it is a second counter-example against shipping the first-or-last-sentence rule as code, after [[Learning & Signal#LS-083|LS-083]].
Sources: arXiv 2607.26621v3, OneLatent: Latent Reasoning for Efficient Foundation Recommendation Models, arxiv.org/abs/2607.26621, abstract read in full 2026-09-30
Last touched: 2026-09-30
"""
lines = append_claim(lines, LS084)
save("Learning & Signal.md", lines, nl)
print("Learning & Signal.md: LS-076 amended, LS-084 added")

# ===================== Meta Delivery & Andromeda =====================
lines, nl = load("Meta Delivery & Andromeda.md")

MD105 = [
    "**The 20% account-issue figure is now on record in two incompatible forms, 2026-09-29.** The line above quotes Meta's published \"20% "
    "increased resolution rates of common account issues\". Heath restates the same figure from a Meta briefing as the assistant being \"able "
    "to resolve about 20% of account issues\". A 20% relative improvement in a resolution rate and a 20% absolute resolution rate are "
    "different claims, and one of the two readings is wrong. **Neither carries a methodology, so the figure is unusable in either form** and "
    "should never be repeated to a client. Ads Creative Studio, built on this same assistant, is at [[Meta Delivery & Andromeda#MD-168|MD-168]].",
]
lines = insert_before(lines, "MD-105", "Sources:", MD105)
lines = append_source(lines, "MD-105", "Sources:", HEATH)
lines = set_touched(lines, "MD-105", "2026-09-30")

MD168 = """
### MD-168 · Meta is rolling out Ads Creative Studio, a second AI surface in Ads Manager that grades each asset against a numeric threshold, compares it to top performers in your category, and generates variations of your own winners
Tier: T2 · Status: active
Ben Heath, 2026-09-29, demonstrated live in a client ad account and preceded by a private briefing from the Meta team building the feature. T2 covers the surface and the interface copy, which were on screen. **Nothing the studio produces has any performance data attached, so every outcome implication below is untested.**

**Access and rollout state.** Three-line menu, then All tools, then under Advertise, "Ads creative studio". Live in a small number of accounts as a pre-release test, with Heath reporting Meta intends a broad rollout soon. Meta told him the surface will be extended, so the panel list here is a starting state and not a specification.

**It sits on top of the AI business assistant at [[Meta Delivery & Andromeda#MD-105|MD-105]].** That is the account-level chat surface. This is the creative-level version of the same machine: the same benchmarking reach beyond your own account, the same generate-a-recommendation layer, pointed at individual assets instead of at campaigns. The same human-filter caution applies, for the same reason.

**Panel 1, Improve creatives.** Lists assets failing the minimum performance threshold ([[Creative Science#CR-281|CR-281]]) with a written diagnosis of why. One diagnosis verbatim: "the creative underperforms because it relies on static flatlay that lacks human connection and trust signals." It then states what the category's top performers do differently, verbatim: "When analyzing top performing ads in your category, we found that successful creatives often feature products in use by a model or styled in a studio setting with a strong focus on specific material benefits and quality", with "clear trust signals such as a multi-year warranty, official certifications" named. It closes with three named creative styles and generated example images for each.

**Panel 2, Scale top creatives.** A leaderboard of the account's best assets, breakable by product, objective or audience, filterable to image or video, with a selectable ranking metric and a time window. Columns shown: spend, ROAS, trend over time, cost per result, frequency, and for video **hook rate, hold rate and thruplay**, which is the native-column change recorded against [[Creative Science#CR-176|CR-176]].

**The generation layer, and the lever names are the part worth keeping**, because they are Meta stating which edits it believes are worth making to a proven asset.

- **Video:** new hooks, described in-product as "swap out the first 3 to 5 seconds of a video with a different approach", with hook types selectable as satisfying intro, emotional storytelling, skit, fear of missing out, or auto. Also add subtitles, and generate a voiceover with a specified voice type. Video generation is quoted in-product at "up to 15 minutes".
- **Image:** resize to match placements, animate the still by moving its elements over time, swap a different product image into the frame while holding everything else, change visual elements while preserving the text and the core idea, update the text on the creative while holding the visuals, or try a new style.

**The hook lever is the one that matters beyond the feature list**, because it is Meta recommending and generating the exact operation the codex has been unable to settle for four passes. Full reading at [[Creative Science#CR-124|CR-124]].

**Limits, stated plainly.** One account, one operator, one session. No generated asset was shown, because the demo ran on a live client account. No hit rate, no before-and-after, no cost per result for anything the studio made. Heath's own guard is the same one MD-105 earns, "you need to be the filter", and he names the case where the written diagnosis would be wrong for an account that has already tested what it recommends.

**Two ROAS figures quoted from the assistant during the same demo, an 82% decrease and a 99% drop, are deliberately not banked.** They come from an auto-transcript that garbles the metric name throughout, they are internally inconsistent as read, and no dashboard was shown.
Sources: __HEATH__
Last touched: 2026-09-30

### MD-169 · Meta's consumer AI agent now connects to Meta ad accounts in a few clicks and drafts campaigns, which puts an agent with ad-account access in front of the small-business owner rather than in front of a developer
Tier: T1 · Status: active
Meta Newsroom, 2026-09-29, "The Future Is for Everyone: Muse for Small Business". Meta's own announcement, read in full.

**The load-bearing sentence:** "Muse can connect your Instagram professional account analytics, Facebook Pages, and Meta ad accounts in a few clicks, and it already understands your business: what you sell, what your brand sounds like, and what customers keep asking you about."

**One of the five use cases Meta publishes is an advertising one, with the prompt written out:** "How do I improve my ads and content? Can you analyze what's working or not, and draft a campaign for next week? Make sure to look at what's trending." A second is "Analyze this year's sales, campaigns, and social and make me a growth plan to meet my business goals for next year."

**Why it gets an ID.** [[Meta Delivery & Andromeda#MD-159|MD-159]] recorded the first agent-reachable Meta buying surface, the Meta Ads MCP connector, which is a developer route. This is the same class of capability arriving through a consumer app aimed at the business owner directly. Muse is US and Canada, connects to dozens of third-party tools including Canva, supports custom connectors, and Meta says it acts proactively rather than only on request. **Meta names no ad-account write scope and no permission model in the post**, so what "draft a campaign" actually creates is unknown.

**The commercial read, and it is a reason to watch rather than to act.** Our clients are exactly the population this is aimed at. An owner who can ask an agent to analyse the ads and draft next week's campaign is being handed the surface layer of what an agency does, free, inside an app they already have. What it does not do is media-buying judgement, and Meta's recommendation layer has a recorded failure rate at [[Meta Delivery & Andromeda#MD-105|MD-105]], including the incentive problem when the platform recommends raising budgets. Carry it as a positioning fact to answer when a client raises it.

**It also moves [[Learning & Signal#LS-076|LS-076]] from a watch note to a live question.** LS-076 banks Meta's launch-day sentence that Muse conversations and VM data do not reach the ad systems. Three weeks later Muse reads ad accounts. Reading an ad account is the opposite direction from feeding the ad systems, so nothing is contested and the tier there is unchanged. The two surfaces now sit inside one agent, which is why the re-check matters.
Sources: __MUSE__
Last touched: 2026-09-30
""".replace("__HEATH__", HEATH).replace("__MUSE__", MUSE)
lines = append_claim(lines, MD168)
save("Meta Delivery & Andromeda.md", lines, nl)
print("Meta Delivery & Andromeda.md: MD-105 amended, MD-168 and MD-169 added")
