# Research merge, 2026-09-10
import io, os

BASE = r"E:\claude code marketing skill\Obsidian God-level Marketing Vault\God-level Marketing\wiki\science"
MD = os.path.join(BASE, "Meta Delivery & Andromeda.md")
CR = os.path.join(BASE, "Creative Science.md")

s = io.open(MD, encoding="utf-8").read()
before = len(s)

# --- MD-150: provenance on the Sales/Leads scope -----------------------------
a = "**Loomer's unofficial scope, T3, and he labels it unofficial himself.**"
assert s.count(a) == 1, ("anchor a", s.count(a))
add = (
    "**Provenance on that scope tightened on 2026-09-09 and it is still T3.** In the podcast episode of that date "
    "Loomer names where the scope came from: \"A contact within Meta's product team reached out to me to clarify "
    "that this will only apply to bottom of the funnel campaign objectives.\" **An unnamed employee relayed "
    "second-hand is testimony, not documentation, so this does not move the tier.** It does mean the "
    "Sales-and-Leads-only boundary is the one part of the rollout story with a Meta-side origin rather than an "
    "advertiser inference, and it is the part Heath contradicts.\n\n"
)
s = s.replace(a, add + a, 1)

# --- MD-151: name the three account-level placements -------------------------
b = ("**It is account-wide**, so it cannot differ between two clients or two offers sharing an account, and the "
     "selectable set is narrower than what the ad set used to offer.")
assert s.count(b) == 1, ("anchor b", s.count(b))
s = s.replace(
    b,
    b + " **Loomer names that set on 2026-09-09 and it is three things: Audience Network, Facebook Marketplace and "
        "Facebook right column.** Against the 17 to 21 placements selectable in the ad set, that is the true size of "
        "the surviving off switch, and not one of the three is a feed, a Reels or a Stories placement. His own advice "
        "on it is to leave it alone: \"I wouldn't recommend you do that, but it does remain an option.\"",
    1,
)

# --- MD-151 + Harvest Log echo: the Reels-for-reach failure mode --------------
c = ("link clicks and landing-page views on Audience Network, and ThruPlay on **Audience Network Rewarded Video**, "
     "where third-party apps pay users in virtual currency to watch.")
assert s.count(c) == 1, ("anchor c", s.count(c))
s = s.replace(
    c,
    c + " **A third pairing was named on 2026-09-09: the REACH objective and the ads-on-Facebook-Reels placement**, "
        "which Meta leans on because it is cheap and carries enormous inventory, and which Loomer calls \"an easily "
        "ignored placement\". The three cases collapse into one sentence worth keeping: **Meta buys the cheapest "
        "inventory that technically satisfies the goal you named, so the fault sits in the goal and not in the "
        "placement.**",
    1,
)

MD_NEW = """
### MD-152 - Under conversion optimisation Meta barely spends on Audience Network at all, so the placement pruning most advertisers do on Sales and Leads campaigns is protecting them from a risk that is not there
Tier: T3 | Status: active
The empirical half of the placement-control story, and it is the half that decides whether MD-150 costs us anything. Jon Loomer, 2026-09-09: **"I've found that Meta doesn't even try to show ads on Audience Network when optimizing for conversions, for example. Or if money is spent there, it's a very small percentage."** The stated mechanism is that the algorithm is guided by the action you asked for, so a placement whose whole business is cheap impressions and accidental clicks has nothing to offer a system being graded on purchases.

**His stronger claim, and it is load-bearing for the entire change:** "there aren't any placements that are known to be sources of cheap and low-quality purchases. It's just not a thing." He calls advertiser placement pruning under conversion optimisation "intentionally hurting their results", and reads Meta's withdrawal of the control as a reaction to advertisers doing it.

**The purchase claim and the LEAD claim are not the same strength, and every client we run is lead gen.** On purchases he asserts it flatly. On leads he hedges twice: "I haven't seen this apply to leads, either", and "I have doubts whether a placement is a source of cheap and low-quality leads." He also separates lead quality from placement explicitly: "you can get cheap and low-quality leads, for sure, but I haven't seen that connected directly to a placement." **So the honest status for our book is asserted for purchases, unmeasured for leads, and nobody has published a lead-side placement breakdown on either side of the argument.**

**The test he prescribes is cheap, it is ours to run, and it upgrades this to T2 with our own numbers.** Run on Advantage+ placements, wait for meaningful results, then open the **breakdown by placement** and read what share of spend landed where. The instrument is already in Ads Manager and we have never run it on a single client account.

**The guard on reading that breakdown, and it is why most people who run it draw the wrong conclusion.** Do not rank placements by conversion rate and prune the losers: "I'm not talking about trying to micromanage placements by conversion rates, which is a waste of time. Impressions have value, even when they don't lead to the highest conversion rate. Meta's job is to balance costs and impressions and conversion rate to get you the best overall results." **The breakdown answers a share-of-spend question, never a conversion-rate question.** That is the placement-level restatement of the judge-at-ad-set-level rule this codex already holds: a row is not a decision.

One operator, no numbers shown, no account named, and he happens to be arguing for the position the platform change requires. Weigh it accordingly, then go and read our own breakdowns.
Sources: Jon Loomer, What Does the Removal of Placement Control Mean?, 2026-09-09
Last touched: 2026-09-10

### MD-153 - Meta published five named advertiser results across five different AI products on 2026-09-03, and three of the five numbers use incrementality language while two do not, printed identically
Tier: T1 for what Meta published, T3 and T4 for the numbers themselves | Status: active
First new post on Meta for Business News since 11 June 2026, a ceiling that had held across eleven consecutive daily checks in this log. **Read it for the product names and for how the numbers are worded, not for the numbers.**

**The five, verbatim, with the product each advertiser used:**
1. **Underneat**, Advantage+ Sales Campaigns: "a **13% incremental lift in purchases** and **16% more add-to-cart conversions**."
2. **Zanskar Health**, Advantage+ Creative with generative AI: "**64% lower cost per purchase**, with faster iteration and more creative variations to test."
3. **HubX**, Partnership Ads with creators: "**28% more incremental subscriptions** and **23% lower cost per subscription**."
4. **Movida**, Meta Business Agent on WhatsApp: "a **54% increase in daily bookings** through WhatsApp compared to the same period the prior year", plus "**85% of conversations are resolved instantly**."
5. **General Motors**, Omni for Automotive: "a **4.4% lift in vehicle sales**."

**The finding is the wording split and it is not decoration.** Three of the five say *incremental* or *lift*, which is the language of a holdout: Underneat, HubX, General Motors. Two do not. Zanskar's 64% is a cost-per-purchase comparison, and **Movida's 54% is an explicit year-over-year comparison against the same period the prior year**, which is the weakest instrument on the page and shares nothing with a lift study except the sentence shape it is printed in. **Meta publishes no methodology, no test window, no holdout size and no absolute figures for any of the five.** A year-over-year booking comparison for a Brazilian car-rental firm carries every seasonal and market effect of a full year, and it is set beside a stated incremental lift with no visual distinction whatsoever.

**The operating rule this produces, and it generalises well past this page: before repeating any platform-published case-study number, find the word.** *Incremental* or *lift* means somebody at least claims a holdout. *Increase*, *more*, *lower cost* or *compared to last year* means a before-and-after, and a before-and-after is not evidence that the product caused anything. Same discipline this codex already applies to a client report.

**One genuinely new product name: Omni for Automotive**, described as connecting digital ads to dealership sales, and it appears nowhere else in this codex. **Worth watching for our own book, because SJR Commercial and Phoenix Truxx are both vehicle dealerships** and an ads-to-vehicle-sales signal product points straight at them. Nothing on the page says it is available to an independent dealer, and a General Motors deployment tells us nothing about whether it is.

Sits beside [[Creative Science#CR-002|CR-002]], which carries Meta's own +22% ROAS and +7% conversions figures for Advantage+ creative under the same missing-methodology caveat. Two years apart, same genre, same missing denominators.
Sources: Meta for Business News, Businesses driving results with Meta AI ads, 2026-09-03 (read 2026-09-10; the page geo-renders in Hindi from our egress and was read in English through a locale override)
Last touched: 2026-09-10
"""

s = s.rstrip("\n") + "\n" + MD_NEW
io.open(MD, "w", encoding="utf-8").write(s)
print("MD ok", before, "->", len(s))

# ============================ Creative Science ==============================
t = io.open(CR, encoding="utf-8").read()
before = len(t)

# --- CR-190: second source for longest-active != top-performing --------------
d = ("The detail panel also exposes the exact run window and the variation count under one ad entry, e.g. "
     "\"We can see there's the three variations of this ad that was run\"")
assert t.count(d) == 1, ("anchor d", t.count(d))
pre = (
    "**A second operator reached the same correction from the paid-tool side on 2026-09-09, which matters because it "
    "is the same finding arrived at through a different instrument.** Nick Theriot, reading a third-party library: "
    "\"even though it's been active for a really long time, it doesn't mean it's top performing.\" His separator is an "
    "ordinal spend rank inside the advertiser's own account rather than an impression count, and he gives the "
    "threshold in plain terms: an ad at 57 of 97 is mid-pack, and \"if it's 83 or 94 out of 97, it's like it's barely "
    "getting any spend\", while 1 of 97 is \"taking majority of all of the spend in that account\". **Two operators, "
    "two different instruments, one conclusion: runtime alone is not a winner signal and never was.** See the tier "
    "warning on that rank field at [[Creative Science#CR-206|CR-206]] before quoting the number itself.\n"
)
t = t.replace(d, pre + d, 1)
t = t.replace(
    "Sources: Ben Heath, How To Spy On Your Competitors Meta Ads for FREE, 2026-04-14\nLast touched: 2026-08-27",
    "Sources: Ben Heath, How To Spy On Your Competitors Meta Ads for FREE, 2026-04-14; Nick Theriot, How To Spy On Your "
    "Competitor's Facebook Ads in 2026, 2026-09-09\nLast touched: 2026-09-10",
    1,
)

# --- CR-206: the negative reading of duplicate count -------------------------
e = ("He is explicit that this replaces the usual heuristic: \"you're no longer just going off vibes or by what's the "
     "longest running in the ad account.\"")
assert t.count(e) == 1, ("anchor e", t.count(e))
qual = (
    "\n\n**THE QUALIFICATION THIS CLAIM WAS MISSING, added 2026-09-09 from a second operator, and it cuts at our own "
    "practice.** Duplicate count was banked here as a one-way winner signal. It is not. Nick Theriot names the other "
    "reasons an advertiser duplicates an ad: \"it's like usually ads that are like constantly getting banned or not "
    "necessarily banned, but they're turned off or you can duplicate to other campaigns for other countries or yada "
    "yada yada. There's a reason why it keeps getting duplicated... So, there could have some like negative drawbacks "
    "to it.\" **So a high duplicate count has at least three causes and only one of them is a win: the ad performed and "
    "was cloned to scale, the ad was disapproved or switched off and was relaunched, or the ad was cloned sideways into "
    "another country or campaign where it proves nothing about this one.** From outside an account the three are "
    "indistinguishable.\n\n**Read duplicate count with a companion signal or not at all.** Theriot's own resolution is "
    "to read the spend rank alongside it, and the ad he actually selects is \"rising really good right now, and it's top "
    "18%\" rather than the most-duplicated one. **This is the sharpest correction available to our own winning-ad "
    "definition, which treats kept-active plus duplicated as confirmation.** Kept active survives untouched. "
    "Duplication needs the second signal.\n\n**Provenance note that applies to this claim, to [[Creative Science#CR-170|"
    "CR-170]] and to [[Creative Science#CR-209|CR-209]] equally: every operator teaching competitor research on this "
    "roster is now demonstrating a paid tool.** Cottrell ran a vendor demo with a paid link. Theriot states his own "
    "conflict on camera, \"Yes, I am technically sponsored by Trend Track\", and gives a discount code. Piliero sells "
    "the workflow at CR-209. **Three operators, three paid instruments, and still nobody has validated a single "
    "estimated spend, rank or revenue figure against an account whose real numbers are known.** Bank the methods, "
    "never the estimates."
)
t = t.replace(e, e + qual, 1)
t = t.replace(
    "Sources: Fraser Cottrell, How to use AI to Copy Winning Ads (Step by Step), 2026-05-17\nLast touched: 2026-08-30",
    "Sources: Fraser Cottrell, How to use AI to Copy Winning Ads (Step by Step), 2026-05-17; Nick Theriot, How To Spy "
    "On Your Competitor's Facebook Ads in 2026, 2026-09-09\nLast touched: 2026-09-10",
    1,
)

CR_NEW = """
### CR-231 - After the competitor teardown there are exactly three places to differentiate, and they are checked in order: creative FORMAT they are not running, MECHANISM they cannot claim, then AVATAR they are ignoring
Tier: T4 | Status: active
The decision rule at the end of a competitor audit, which is the step most teardown workflows never reach. Nick Theriot, 2026-09-09, having pulled a category's direct and indirect competitors apart ad by ad. **The output of a teardown is not a swipe file, it is a choice about where you are going to be different.** Three gaps, checked in this order.

**1. The format gap. Is there a creative format none of them are running that we can execute well?** His worked case is native ads: "when like native ads really took off and blew up... it was this almost like not undiscovered but slept on technically creative format because there wasn't a lot of people utilizing it. And because not many people are utilizing it, it felt new to people." **He then dates its own decay in the same breath, which is the honest part: "you could still technically do it today, but it's just it's become a little bit more saturated than it was in, you know, a year ago."** So a format gap is a decaying asset, not a position, and the window is roughly a year in this instance.

**2. The mechanism gap. What can we claim about the product that they cannot?** Read off the competitor set he pulls: one brand's whole argument is the FORM of the ingredient, one is the COUNT of forms, one is a purity comparison against a named alternative source. Each is a different answer to the same buyer question.

**3. The avatar gap, and it is the fallback when the first two are empty.** Keep the problem and the desire exactly as the category states them, and narrow WHO. His example: everyone in the category sells to people who cannot sleep, so sell to night-shift workers who cannot sleep during the day. **Explicitly not a change of desire: "I'm not saying we need to go and change the desire."** This is the only one of the three that is always available, because it costs nothing but a decision.

**Why the order matters.** Format and mechanism are properties of the market and may genuinely not be there. Avatar is a property of the brief, so it is always there, which makes it the tempting first answer and the weakest one to reach for early. **The rule is to look for a real gap twice before manufacturing one.**

Then he writes the hypothesis down before producing anything: avatar, problem, desire, mechanism, format, and why the test matters. That is the same discipline as the pre-launch test specification at [[Creative Science#CR-222|CR-222]], arrived at independently, and it is the part worth copying regardless of what one thinks of the three gaps.

No data of any kind attached, one operator, and the video is a sponsored tool walkthrough. It is a framework for structuring a decision, never evidence about which gap pays.
Sources: Nick Theriot, How To Spy On Your Competitor's Facebook Ads in 2026, 2026-09-09
Last touched: 2026-09-10
"""

t = t.rstrip("\n") + "\n" + CR_NEW
io.open(CR, "w", encoding="utf-8").write(t)
print("CR ok", before, "->", len(t))
