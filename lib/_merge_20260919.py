# -*- coding: utf-8 -*-
"""2026-09-19 research pass merge."""
import re, pathlib

SCI = pathlib.Path(r"E:\claude code marketing skill\Obsidian God-level Marketing Vault\God-level Marketing\wiki\science")
TODAY = "2026-09-19"
report = []


def load(name):
    return (SCI / name).read_text(encoding="utf-8")


def save(name, txt):
    (SCI / name).write_text(txt, encoding="utf-8")


def block_span(txt, cid):
    m = re.search(r"^### " + re.escape(cid) + r" ", txt, re.M)
    if not m:
        raise SystemExit("claim not found: " + cid)
    n = re.search(r"^### [A-Z]{2}-\d+ ", txt[m.end():], re.M)
    end = m.end() + n.start() if n else len(txt)
    return m.start(), end


def amend(name, cid, para, new_source, new_tier=None):
    txt = load(name)
    s, e = block_span(txt, cid)
    blk = txt[s:e]
    if new_tier:
        blk = re.sub(r"^Tier: T\d", "Tier: " + new_tier, blk, count=1, flags=re.M)
    sm = re.search(r"^Sources: (.*)$", blk, re.M)
    lm = re.search(r"^Last touched: .*$", blk, re.M)
    if not sm or not lm:
        raise SystemExit("no Sources/Last touched in " + cid)
    blk = blk[:sm.start()] + para.strip() + "\n" + blk[sm.start():]
    sm = re.search(r"^Sources: (.*)$", blk, re.M)
    if new_source and new_source not in blk:
        blk = blk[:sm.start()] + "Sources: " + sm.group(1).rstrip() + "; " + new_source + blk[sm.end():]
    blk = re.sub(r"^Last touched: .*$", "Last touched: " + TODAY, blk, count=1, flags=re.M)
    save(name, txt[:s] + blk + txt[e:])
    report.append("amended " + cid + " in " + name)


def append_claim(name, body):
    txt = load(name).rstrip("\n")
    save(name, txt + "\n\n" + body.strip() + "\n")
    report.append("added " + body.strip().split("\n")[0][:70] + " to " + name)


CRE = "Creative Science.md"
MET = "Meta Delivery & Andromeda.md"
GOO = "Google Auction & Smart Bidding.md"
MMF = "Marketing Math & Unit Economics.md"

NT = "Nick Theriot, This Static Ad Spent $234,853 (Here's How), 2026-09-18"
PL = 'Meta Newsroom Poland, "Prostujemy: fakty o walce z oszukanczymi reklamami w Polsce", 2026-09, read in full 2026-09-19'

# ---------------------------------------------------------------- CR-117
amend(CRE, "CR-117", """
**The $260,000 above is a THREE-AD SUM, and the same operator disclosed it eleven days later on 2026-09-18.** Walking through the same asset, same client, same headline, he gives the figure as **$234,853 over the last 12 months at a $27 cost per lead**, then adds the line the earlier telling did not carry: "we do have it in three different cities. So that's why it's three different times right there. But if you put them all together, over $234,000 all was spent on this." **Per ad that is roughly $78,300 across 12 months, so this tail point sits 52 to 112 times the $700 to $1,500 mean rather than the 170 to 370 times recorded above.** The two numbers reconcile on WINDOW rather than contradicting: the asset was built 2025-07-19, so a trailing-12-month read drops its first seven weeks, and $260,000 lifetime against $234,853 trailing-12 is the shape that predicts. **The transferable rule costs this claim one of its three tail points: a headline single-ad spend figure is a SUM until the operator says otherwise.** The 2026-09-07 telling said "this particular static ad right here", named one build date and one spend, and flagged no split; the disclosure arrived only because a later video happened to re-walk the same asset. The Charley T $2 million ad and the Blue Sense quarter-million-a-month VSL carry exactly the same exposure and neither has been re-told.
""", NT)

# ---------------------------------------------------------------- CR-048
amend(CRE, "CR-048", """
**Correction to the longevity outlier immediately above, from the same operator on 2026-09-18.** The acne static is three ads running in three cities, and the headline figure is all three added together: **$234,853 over the last 12 months at a $27 cost per lead, which is roughly $78,300 per ad.** So the entry above overstates the single-asset lifetime by about 3x, and the count of operators reporting six-figure spend on ONE static drops from three to two. The format point that entry was making survives at the lower number, because $78,300 on one static is still two orders of magnitude above the $700 to $1,500 mean at [[Creative Science#CR-117|CR-117]]. Full correction and the reading rule it produces are at [[Creative Science#CR-117|CR-117]].
""", NT)

# ---------------------------------------------------------------- CR-021
amend(CRE, "CR-021", """
**The same operator decomposed the winning line on 2026-09-18 and named which part does which job.** "Viral new laser treatment vanishes acne in 30 minutes" splits into a NAMED new mechanism (laser treatment), the problem (acne), and an enlargement of the promise through SPEED (30 minutes). He marks "new" as novelty filler that does no work on its own. **Two instructions fall out that this claim did not carry.** First, the mechanism has to be given a NAME, and the name is chosen for appeal rather than for accuracy: "you have to like give it some type of new name itself and that's something you just develop yourself. There's no real like science behind that. It's just what sounds sexy to people." Second, a mechanism carrying no superiority axis has no place in the reader's mind at all, which is the go/no-go test at [[Creative Science#CR-252|CR-252]]. He also states the awareness call for this market plainly and it cuts against the obvious read: **problem-aware is the target, because a solution-aware "clear skin" hook on its own loses the people who actually have acne**, and an unaware ad is never run here because "it's on your face. You see it every time everywhere you go."
""", NT)

# ---------------------------------------------------------------- CR-023
amend(CRE, "CR-023", """
**The full five-stage ladder, stated on 2026-09-18 by an operator walking a live asset that has taken six figures of spend rather than citing the book, which lifts this claim from T4 to T3.** His working definition of sophistication is a count: "how many times was that promise made before and how skeptical people are." Stage 1, direct promise, state the desired result ("how to get rid of acne"). Stage 2, enlarged promise, the same promise made stronger, faster or cheaper ("how to get rid of acne fast", "overnight"). Stage 3, introduce a mechanism, keep the familiar promise and give a fresher explanation of how the result is reached, which is where his own scaled static sits. Stage 4, elaborate the mechanism, take the now-familiar method and name a meaningful improvement ("the world's first painless laser acne treatment"), **and he notes stage 4 needs a competing mechanism to improve on, which his own account does not have, so he sits at stage 3 by availability rather than by choice.** Stage 5, identification, open on an experience, a value or a self-image the reader recognises and only then connect it to the problem. He says stage 5 opens the same way an unaware market does, which is the same structure this operator already stated at [[Creative Science#CR-022|CR-022]], so treat it as one position stated twice and not as two sources.
""", NT, new_tier="T3")

# ---------------------------------------------------------------- CR-252 (new)
append_claim(CRE, """
### CR-252 · A new mechanism has to compete on speed, price, simplicity or without-what-they-hate, and an operator refuses accounts whose mechanism competes on none of the four
Tier: T3 · Status: active
The test, in his words: "people buy for four things, speed, price, simplicity, or without what they hate." So once a mechanism is named, ask what it beats the incumbent on. His own scaled static answers SPEED and says so in the headline, "in 30 minutes". **A mechanism that answers none of the four he calls "the least superior mechanism there, and it's not something that we're going to want to scale."** He states the commercial consequence as a client-selection rule rather than as a creative note: "we typically stay away from people with products like that because they're just not going to do great when it comes onto Facebook ads. It's going to be extremely hard." The inverse is the reason he gives for the acne account being easy to run: "we upload a few creatives here and there to it. We just push more spend to it. It works really well cuz they have a new mechanism that's sexy and that people want and it's easier to scale."
**Why this is worth having as a separate test.** [[Creative Science#CR-231|CR-231]] already says a mechanism the competitor cannot claim is one of the three places to differentiate. This is the prior question: whether the mechanism has any pulling power at all, answerable from the offer alone before a single ad is made. It is also the cheapest pre-flight check in this file, because it needs no account, no spend and no creative.
**Honest limit.** One operator, asserted, no test and no comparison between offers that pass the four and offers that fail them. The axes are a memorised heuristic and he presents them as one. What raises it above a slogan is that he attaches a refusal to it, which is a practitioner betting revenue on his own rule.
**Where it bites on our own book.** Ask the four questions of each client offer before the next batch. A $49 introductory session competes on PRICE; a voice agent that calls an opt-in within minutes competes on SPEED; a done-for-you build competes on SIMPLICITY. An offer where the honest answer to all four is "nothing" is a brief to fix the offer, not a brief to write more ads.
Sources: """ + NT + """
Last touched: """ + TODAY)

# ---------------------------------------------------------------- MD-149
amend(MET, "MD-149", """
**Restated by Meta in a SECOND Polish-language Newsroom post, read in full 2026-09-19, and the global target is unchanged three weeks on.** The post is a rebuttal to an Instrat Foundation report and it repeats both halves: verification required of 100% of financial-services advertisers directing ads to Poland, and "aby do konca 2026 roku 90% przychodow reklamowych Mety na swiecie pochodzilo od zweryfikowanych reklamodawcow", by the end of 2026 90% of Meta's worldwide advertising revenue should come from verified advertisers. **This telling DROPS the 70%-in-2025 baseline the 2026-08-28 post carried, so the 20-point move rests on the earlier post alone and has to keep being quoted from it.** The same post adds the enforcement half of the programme: Poland is in the first group of European countries to receive a new anti-impersonation AI system, and Meta states it has detected and removed 50% more ads impersonating public figures in Poland than the system it replaced. That is Meta's own number about Meta's own system, with no method and no external audit, and it belongs beside the removal-taxonomy point at [[Meta Delivery & Andromeda#MD-160|MD-160]].
""", PL)

# ---------------------------------------------------------------- MD-160 (new)
append_claim(MET, """
### MD-160 · Meta says an ad REMOVAL is not a fraud finding, because enforcement fires across restricted goods, third-party intellectual property, ad quality and format as well, so a removal count is never a violation-category count
Tier: T1 · Status: active
Stated by Meta in its own words, rebutting a third-party report that had used removals as its fraud proxy. The report's method, quoted by Meta: "Aby okreslic, ktore reklamy w zbiorze danych byly oszukancze, wykorzystalismy informacje o tym, czy zostaly one usuniete przez Mete", that is, to decide which ads in the dataset were fraudulent the authors used whether Meta had removed them. **Meta's answer names the taxonomy: its systems act on a broad range of advertising standards and policies covering restricted goods and services, third-party intellectual property, ad quality and ad format, "oraz wielu innych", and many others, "a nie wylacznie oszustw", and not exclusively fraud.**
**Why this is worth banking as a mechanism rather than as news.** It is the first statement on file from Meta about what the POPULATION of removed ads actually contains, and it cuts two ways at once. Outward: any third-party estimate of scam-ad revenue built on removal counts is inflated by every non-fraud enforcement category in it, and the inflation factor is unpublished. Inward, and this is the half that touches our own accounts: **a removal on a client account carries no information about which policy fired until the notice itself is read.** Our chiropractic accounts sit under the health and personal-attributes sections and our dealership accounts under vehicle and finance rules, and treating any takedown as a policy-category signal without reading the notice is the same error at account scale.
**The enforcement figures in the same post, all self-reported, no external audit.** 137,000 fraudulent ads removed in Poland between July 2025 and June 2026, over 88% of them actioned before anyone reported them. The scam-ad report rate, which Meta defines as how often users reported a fraudulent ad per ad impression, down 83% in Poland between July 2024 and June 2026. **Read the second one carefully: a report RATE falling is consistent with fewer scam ads and equally consistent with fewer users bothering to report, and Meta publishes no way to separate the two.** Same standing as every vendor-computed number at law 4c.
**Honest limit.** T1 for what Meta says about its own enforcement taxonomy, which is the durable half. Meta is a defendant in litigation brought by the party whose law firm prepared the report it is rebutting, and Meta says so in the post, so nothing here settles who is right about Poland. The reading rule for the report's arithmetic is at [[Marketing Math & Unit Economics#MM-220|MM-220]]. Read in the Polish original on Meta's own Newsroom rather than through a machine translation.
Sources: """ + PL + """
Last touched: """ + TODAY)

# ---------------------------------------------------------------- MM-220 (new)
append_claim(MMF, """
### MM-220 · A published estimate of ad spend or ad revenue built as reach times frequency times CPM is usually two assumptions and one guess, and the five defects Meta named in one are the checklist
Tier: T3 · Status: active
The instrument, not the verdict. Meta published a line-by-line rebuttal of a third-party estimate of fraudulent-ad revenue in Poland, and the defects it names are generic to this whole class of number. **The estimate multiplied three values: how many people saw the ad, how often they saw it, and what it cost. Two of the three were assumptions and one was an estimate, and the product was presented as a single headline figure.**
**The five checks, each stated against the source's own method.** One, REACH: EU-wide reach figures covering 27 countries were applied as if they described one country's users. Two, FREQUENCY: every ad was assumed to be seen three times, on a number taken from a US vendor's website built on 2,800 of that vendor's own customers, with no connection to the country or to the ad type in question. Three, PRICE: the authors state they could not estimate CPM empirically, so the figure at the base of the multiplication is an abstract number, quoted as 20.65 zloty. Four, SAMPLE: part of the conclusion rests on 108 ads observed on a single iOS device whose profile the authors had deliberately conditioned by viewing and clicking to attract those ad types, which is not what an ordinary user is served. Five, EXTRAPOLATION: full-year conclusions drawn from three single days in October, December and January that differed from each other by up to 80%, averaged and multiplied to an annual value with no margin of error.
**The transferable rule.** When a published figure about ad spend, ad revenue or ad exposure is a product of reach, frequency and price, **ask which of the three was MEASURED before repeating the figure**, and ask what window the annualisation ran on. Same shape as law 11a's find-the-word test for incrementality claims, applied to a different class of number. The authors' own admission is the sharpest tell available and it appears in most reports of this kind if you look for it: Meta quotes them conceding that a different classification decision would have produced a number "close to 70%", which says the result moves with a judgement call rather than with the data.
**Honest limit, and it is load-bearing.** This is Meta's account of somebody else's method, read in Meta's own post; the report itself was not read here. Meta is a defendant in litigation brought by the party whose law firm prepared the report, which is a direct interest in the outcome. **So the five checks are worth adopting and the verdict on this particular report is not banked.** Each check is verifiable against any report's own stated methodology section, which is where to use it.
Sources: """ + PL + """
Last touched: """ + TODAY)

# ---------------------------------------------------------------- GA-076 (new)
append_claim(GOO, """
### GA-076 · Journey-aware bidding lets a Search campaign learn from conversion goals it is NOT bidding on, which changes what a secondary conversion action costs you to track
Tier: T1 · Status: active
Google's own wording: "When you track your full lead to sales journey, Search Ads campaigns optimizing to a Target CPA will be able to learn from both biddable and non-biddable conversion goals", the goals it names being "phone calls, form submission, newsletter signups and more". The product page states the scope as Search campaigns on **Target CPA and Maximize conversions**, and describes campaigns that "learn from every goal, biddable or not, to sharpen predictions". Status is **beta**. The stated data requirement sits on the advertiser: give Google AI enough visibility into the lead journey by importing the necessary conversion actions.
**Why this matters more than a feature line.** Until now a conversion action was either counted, and therefore bid on and therefore able to distort a Target CPA, or it was secondary and therefore inert. **This makes a third state available: an action that feeds the prediction without entering the bid target.** For a lead-gen account that is the whole argument for tracking the mid-funnel, because the reason operators refuse to track booked calls, show-ups and closed deals as conversions is that adding them moves the target. A signal path that does not move it is a different trade.
**The operating consequence, and the failure mode is timing.** The feature only pays if the downstream outcome reaches Google while the campaign can still learn from it, so a CRM that uploads closed-won weekly or monthly hands the algorithm an outcome too late to be useful. Any account we put on this needs its offline upload cadence checked first.
**Honest limit.** T1 for what the product IS, for the two bid strategies and for the beta status, on the [[Meta Delivery & Andromeda#MD-099|MD-099]] precedent of T1-for-existence-and-surface-only. **Google publishes no performance figure for it, no eligibility threshold and no general-availability date.** Nobody here has run it. Note also that this is not fresh news: it was announced at Google Marketing Live 2026 and this codex had zero coverage of it until today, which is a four-month gap in the Google lane rather than a launch.
Sources: Google Ads & Commerce Blog, "Bidding and budgeting news from Google Marketing Live 2026", read 2026-09-19; Google Ads product announcement page, "Journey-aware bidding", read 2026-09-19; surfaced by Google Ads & Commerce Blog, "Build campaigns that drive high-converting, sales-ready leads", 2026-09-18
Last touched: """ + TODAY)

# ---------------------------------------------------------------- GA-077 (new)
append_claim(GOO, """
### GA-077 · Demand-led pacing moves Search and Shopping spend between days to follow demand, held inside a MONTHLY budget rather than a daily one
Tier: T1 · Status: active
Google's wording: Google AI will "optimize spend to follow consumer demand, capturing more demand on peak days and reducing spend on slower days, all while never going beyond your monthly budget and daily spending limits." Scope is Search and Shopping campaigns. Timing is stated only as "in the coming months", so it is not live.
**The structural part is the budget unit.** A daily budget with a 2x daily overspend allowance is a per-day constraint that happens to average out; a monthly budget with demand-led pacing is an explicitly monthly constraint the system is allowed to shape inside. **That changes what a mid-month spend readout means**, because a week running hot is the intended behaviour rather than a pacing fault, and a client reading a daily average will call it a problem. It also changes what a mid-month intervention does, since manually pulling budget in a hot week removes exactly the demand the system was buying.
**Honest limit.** T1 for existence, surfaces and the stated constraint only. **No performance figure, no date, no eligibility, and it is not live**, so nothing here is actionable this week. Carry it as a watch item for Search and Shopping accounts and check whether the budget object in the account changes shape when it ships.
Sources: Google Ads & Commerce Blog, "Bidding and budgeting news from Google Marketing Live 2026", read 2026-09-19
Last touched: """ + TODAY)

# ---------------------------------------------------------------- GA-078 (new)
append_claim(GOO, """
### GA-078 · Lead intent scores grade every Google form submission High, Medium or Low, and the score prioritises the call list without entering the bid
Tier: T1 · Status: active
Google's own page describes it as: "Stop guessing which leads to call first and start using conversion probability to prioritize your sales queue." Every submission is categorised **High, Medium or Low intent** using Google's signals, the stated purposes being to work the most likely converters first and to filter spam and unqualified submissions out of a sales queue. Google's page labels it "New for 2026". The 2026-09-18 Ads Decoded post calls it a **pilot**. The two descriptions disagree on maturity and the pilot wording is the more recent, so treat it as a pilot.
**Where it sits relative to bidding, which is the thing to get right.** Nothing on Google's page says the score feeds Smart Bidding. It is presented as a prioritisation and reporting label on the submission, so it answers "who do we call first" and not "who does Google buy more of". The bidding half of the same problem is [[Google Auction & Smart Bidding#GA-076|GA-076]], which is a separate product.
**Why it is worth watching on our own book.** Our delivery model already calls every opt-in with a voice agent regardless of order, so a priority label changes nothing about coverage. Where it could pay is the reverse direction: **a Google-side intent grade sitting beside our own outcome data is a free external check on whether the opt-ins an account produces are getting worse**, which is the question that turns into an argument about quality on every underperforming account. That only works if the grade can be exported and joined to the outcome, which is untested here.
**Honest limit.** T1 for existence, the three-tier scale and the stated purpose. **No eligibility, no campaign-type scope, no accuracy figure, no method for how the score is computed, and no case data of any kind on Google's page.** A vendor-computed quality grade with an unpublished method has the same standing as Opportunity Score at law 4c: usable as a hint, never quotable to a client as a measurement. Nobody here has seen one. Announced at Google Marketing Live 2026 and absent from this codex until today.
Sources: Google Ads product announcement page, "Lead intent scores", read 2026-09-19; Google Ads & Commerce Blog, "Build campaigns that drive high-converting, sales-ready leads", 2026-09-18
Last touched: """ + TODAY)

print("\n".join(report))
print("OK", len(report), "operations")
