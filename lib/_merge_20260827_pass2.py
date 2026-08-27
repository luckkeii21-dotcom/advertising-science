"""Claim merge for the 2026-08-27 SECOND research pass (07:00 IST run).

Every claim carries the quotes it rests on. The script VERIFIES each quote against
its transcript before writing anything. If any quote fails, nothing is written.
Then it appends the claim entries to their topic files and flips `extracted: true`
on the 25 transcripts read in this batch.
"""
import io, os, re, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

VAULT = (r"E:\claude code marketing skill\Obsidian God-level Marketing Vault"
         r"\God-level Marketing")
SCI = os.path.join(VAULT, "wiki", "science")
TR = os.path.join(VAULT, "wiki", "sources", "transcripts")
BS = os.path.join(TR, "bluesense-digital")
MB = os.path.join(TR, "mark-builds-brands")
JL = os.path.join(TR, "jon-loomer")
S8 = os.path.join(TR, "solutions8")
MS = os.path.join(TR, "matt-shiver")

F = {
    "mer":  os.path.join(BS, "2025-05-29--bluesense-digital--Heres How To Fix Acquisition MER At Scale.md"),
    "opt":  os.path.join(BS, "2025-03-21--bluesense-digital--Heres How To Find Your Optimal Spend MER.md"),
    "gm":   os.path.join(BS, "2025-02-18--bluesense-digital--Why You Need Gross Margin to Set ROAS Targets.md"),
    "mgr":  os.path.join(BS, "2025-02-11--bluesense-digital--How To Calculate Your Maximum Growth Rate Free Calculator.md"),
    "cp":   os.path.join(BS, "2025-03-17--bluesense-digital--Creative Planning That Considers Finance eCommerce.md"),
    "mar":  os.path.join(BS, "2025-11-27--bluesense-digital--Margin Doesnt Expand As You Scale.md"),
    "fc":   os.path.join(BS, "2025-09-09--bluesense-digital--The Biggest Mistake Your Making in Forecasting eCommerce.md"),
    "q5":   os.path.join(BS, "2025-12-22--bluesense-digital--Q5 Is Overhyped Low CPMs Dont Mean Opportunity.md"),
    "us":   os.path.join(BS, "2025-09-22--bluesense-digital--You Will Guaranteed Underspend on Paid Ads In September October.md"),
    "mg":   os.path.join(BS, "2025-02-06--bluesense-digital--Why Meta Ads Is Beating Google Ads In 2025.md"),
    "bf":   os.path.join(BS, "2025-09-24--bluesense-digital--The Best Creative Strategy for BFCM 2025.md"),
    "pa":   os.path.join(BS, "2025-03-27--bluesense-digital--How To Make Meta Partnership Ads Work For You.md"),
    "lb":   os.path.join(BS, "2025-03-05--bluesense-digital--Limited By Budget Explained Google Ads.md"),
    "dr":   os.path.join(BS, "2025-03-22--bluesense-digital--Display Retargeting Strategy in Google Ads.md"),
    "5m":   os.path.join(BS, "2025-05-13--bluesense-digital--The 5 Metrics That Actually Matter for An eCommerce Business.md"),
    "and":  os.path.join(MB, "2025-11-26--mark-builds-brands--how to test facebook ads post andromeda update.md"),
    "neu":  os.path.join(MB, "2026-05-28--mark-builds-brands--Neuroscience Confirms this is what makes people buy from your ads.md"),
    "mbai": os.path.join(MB, "2026-01-16--mark-builds-brands--how to get disgustingly rich with AI image ads someone patch this.md"),
    "jlch": os.path.join(JL, "2026-05-18--jon-loomer--Change Will Always Be Your Biggest Problem.md"),
    "jlai": os.path.join(JL, "2026-06-03--jon-loomer--Can AI Actually Make You a Better Advertiser.md"),
    "jlhd": os.path.join(JL, "2026-04-13--jon-loomer--Stop Hiding Your Ad Account from Clients.md"),
    "lpo":  os.path.join(S8, "2025-12-03--solutions8--Ultimate Guide to Landing Page Optimization Strategies to Boost Your C.md"),
    "seo":  os.path.join(S8, "2025-11-20--solutions8--Master Landing Page SEO Quick Fixes for Traffic and Conversions.md"),
    "ac":   os.path.join(S8, "2025-11-13--solutions8--From Ad Clicks to Customer Conversions Essential Landing Page Strategi.md"),
    "mscl": os.path.join(MS, "2026-04-14--matt-shiver--Claude Just Changed Facebook Ads Forever.md"),
}

TOPIC = {
    "MD": "Meta Delivery & Andromeda.md",
    "AU": "Auction Mechanics & Bidding.md",
    "LS": "Learning & Signal.md",
    "CR": "Creative Science.md",
    "SC": "Scaling Models.md",
    "AT": "Attribution & Incrementality.md",
    "GA": "Google Auction & Smart Bidding.md",
    "MM": "Marketing Math & Unit Economics.md",
}

D = "2026-08-27"

# ---------------------------------------------------------------- claims
CLAIMS = []


def add(cid, title, tier, status, body, sources, quotes):
    CLAIMS.append(dict(id=cid, title=title, tier=tier, status=status,
                       body=body.strip(), sources=sources, quotes=quotes))


add("AU-082", "What sets your CPM: outcome value times predicted probability, which means a CPM that RISES on a winning ad set is a success signal, not fatigue",
    "T4", "active", """
The model, stated plainly: "your impression value is roughly equal to the value of the optimized outcome times the predicted probability of that outcome given that impression. This is how your CPMs are determined." Under smart bidding you are not buying impressions: "the key misunderstanding that people have is that they believe that they are paying for impressions on the platform but you're not really. You're actually paying for conversions." So the platform prices each individual impression by how likely it thinks that person is to convert.
**The consequence nobody in this codex had stated, and it inverts a routine diagnosis.** When your conversion rate beats what the platform expected, the platform re-learns and bids you into more expensive auctions: "the expected conversion rate on the campaign now goes up and now Meta might expect from you a 5% conversion rate because that's what you've been hitting. So it reweights all of its bidding models and it now starts to come into auctions more aggressively. And what happens? Your CPMs go up." **So a rising CPM on an ad set that just started converting well is the machine repricing you upward because you are winning. Read it next to cost per lead before calling it fatigue and refreshing the creative.**
The companion rule: cheap impressions are cheap because the people behind them are worth less. "if you get lower CPMs, at what cost? The cost is usually at lower CTRs and lower conversion rates because you are bidding on a worse quality user." A CPM drop after widening an audience is not a win on its own.
**⚠ Tier guard and an arithmetic failure, both load-bearing.** This is **T4**, not T1 or T2. He cites one unnamed on-screen paper he himself calls a "theoretical analysis", no platform documentation and no test. **And his own worked example does not obey his own formula.** He prices a 10%-probability user at a $90 CPM and a 0.5%-probability user at $7. The probability ratio is 20x; the CPM ratio is 90/7 = 12.86x. Back-solving the outcome value gives $1,400 from one example and $900 from the other, 55% apart. Under his stated formula the 10% user should price at $140, not $90. **Never quote the $90/$7 pair as a ratio.** The mechanism is worth holding; the numbers are illustrative and internally inconsistent.
The related reading habit: a reported CPM is a blend of many separate per-user prices. "Number one is that your CPM number is an average. What is occurring is that every single auction that occurs on an individual user who sees one of your ads, there is a different cost." An account-level CPM says nothing about what any single impression cost.
**Transfer.** Nothing here is purchase-specific. Substitute lead value for purchase value and the model runs identically on a Lead or Appointment Booked objective, which is how all five of our accounts are optimised.
""",
    "Blue Sense Digital, 2025-12-22 (Q5 Is Overhyped)",
    [(F["q5"], "your impression value is roughly equal to the value of the optimized outcome times the predicted probability of that outcome given that impression. This is how your CPMs are determined."),
     (F["q5"], "the key misunderstanding that people have is that they believe that they are paying for impressions on the platform but you're not really. You're actually paying for conversions."),
     (F["q5"], "the expected conversion rate on the campaign now goes up and now Meta might expect from you a 5% conversion rate because that's what you've been hitting. So it reweights all of its bidding models and it now starts to come into auctions more aggressively. And what happens? Your CPMs go up."),
     (F["q5"], "if you get lower CPMs, at what cost? The cost is usually at lower CTRs and lower conversion rates because you are bidding on a worse quality user."),
     (F["q5"], "Number one is that your CPM number is an average. What is occurring is that every single auction that occurs on an individual user who sees one of your ads, there is a different cost.")])

add("GA-065", "Google's \"Limited by budget\" label: the STATUS is real, the operator's causal reading came from a sales rep, and the check he ran to confirm it does not support his conclusion",
    "T3", "contested", """
This is the Google twin of the codex rule that Meta's "Learning Limited" is a LABEL rather than a diagnosis, and it is worth reading because the operator lands on the **opposite** shape.
He starts exactly where our Meta rule sits, treating the status as an upsell prompt, then abandons that position on the strength of one conversation: "firstly our or previously our opinion on this limited by budget recommendation is simply just Google getting you to spend more within your accounts but after speaking to a or after one of our team members speaking to Google rep the other day it was more that the spin gets throttled towards the end of the day through that campaign because the the campaign's actually spent through all of your spend at the beginning of the day."
**Tier the pieces separately.** The existence and wording of the status is T1, read off the interface. **The causal explanation is a verbal claim from a Google sales representative, relayed second-hand by a colleague. That is T3 testimony, not documentation, and a sales rep explaining why you should raise a budget is the least disinterested source available.**
**⚠ The check he ran to validate it FAILS on his own stated numbers, and this is the reason the claim is contested rather than active.** He segments the campaign by hour and reports spend collapsing at 3pm: "at 300 p.m. that drops down to $70 $80 per hour". He then compares against site sessions, which by his own description "holds you know very strongly all the way up until about 8:00 p.m. at night where that drops off", and calls the two a "very similar distribution". **They diverge by five hours.** Two further problems: he says that session data carries heavy organic traffic, which makes it a demand curve rather than a read on Google delivery; and if the curves genuinely matched, that would be evidence of spend FOLLOWING natural demand, which argues against throttling rather than for it. His own intraday bands are also inconsistent, describing a rise to $240-$280/hr and then a "hold" at $120-$150, which is a halving.
**What survives, and it is the method rather than the conclusion.** Segmenting by time then hour of day to inspect intraday pacing is a good habit and costs nothing. **It matters more for local service than for ecommerce, because a clinic or a dealership has a phone room with opening hours and spend landing at 9pm reaches nobody who can be called back.** Use the Ad Schedule control, which he shows on screen, to bound delivery to real opening hours.
His attached scaling warning is separately useful and separately unevidenced: "a lot of the time what Google will do when you make a budget increase is simply just increase your average cost per click um and you'll actually end up just paying more for the same amount of traffic getting pushed over to your website". No before-and-after CPC pair, no click counts, no account. **The lead-gen version of the check is to watch cost per click AND cost per lead together, since a CPC rise with a flat cost per lead is not a problem.**
""",
    "Blue Sense Digital, 2025-03-05 (Limited By Budget Explained)",
    [(F["lb"], "firstly our or previously our opinion on this limited by budget recommendation is simply just Google getting you to spend more within your accounts but after speaking to a or after one of our team members speaking to Google rep the other day it was more that the spin gets throttled towards the end of the day through that campaign because the the campaign's actually spent through all of your spend at the beginning of the day"),
     (F["lb"], "at 300 p.m. that drops down to $70 $80 per hour"),
     (F["lb"], "holds you know very strongly all the way up until about 8:00 p.m. at night where that drops off"),
     (F["lb"], "very similar distribution of sessions across the store in comparison to Google ads just to reference this store does have quite a lot of organic traffic as well"),
     (F["lb"], "a lot of the time what Google will do when you make a budget increase is simply just increase your average cost per click um and you'll actually end up just paying more for the same amount of traffic getting pushed over to your website"),
     (F["lb"], "if you you still can't get that right and you want to kind of exclude different hours of the day there is this ad schedule section down over here where you can essentially set when you want your campaign to spend")])

add("GA-066", "Google has its own suggestion-versus-control split, and it is called Optimized Targeting. It is ON by default and it expands delivery past the audience you chose",
    "T1", "active", """
Read off the Google Ads interface with the panel open: "the main thing to mention here is this optimized targeting section here essentially what this does is it expands your reach outside of the specific audience that you've selected if Google CES relevant" (the transcript garbles "sees" as "CES").
**T1 for the existence and stated function of the setting only.** Google's own panel text says the setting expands beyond the selected audience. What that costs you is a separate, unevidenced claim, filed below.
**This is the Google analogue of law 1a on the Meta side, and the codex had no entry for it.** On Meta we hold that location, minimum age, language and exclusions bind while interests, lookalikes and custom audiences are suggestions by default. Google ships the same architecture under a different name, with the same default: the audience you select is a starting point the system is licensed to leave. **An operator who has internalised "my Google audience binds because I selected it" is wrong for the same reason, on the same kind of control, on the other platform.**
His consequence claim is T3 and carries no data: "this should be turned off because this will expand your targeting outside of just your existing audience and will start pushing to cold and will end up burning through all your budget almost immediately and and not make that targeting relevant so turn that off". No spend curve, no audience breakdown, no before and after. **The speed word "almost immediately" is doing a lot of work with nothing behind it.**
**Operating consequence for our book, and it is a five-minute check rather than another transcript.** Any Google campaign built to hit one list, a past-patient list, a past-applicant list, a customer-match upload, has to be checked for this box. On a small daily budget a leak to cold does not merely dilute the campaign, it consumes it. **Check the state, do not assume it from the claim.**
Related and cheap: he recommends turning off Google's auto-generated assets in Display, because "you do sometimes get some pretty bizarre headline recommendations that are autogenerated". **For the two chiropractic accounts and the lender this is a compliance exposure and not an aesthetic one, since a machine-written headline is generated after our review.** Same shape as the Meta creative-enhancement problem banked this morning.
""",
    "Blue Sense Digital, 2025-03-22 (Display Retargeting Strategy in Google Ads)",
    [(F["dr"], "the main thing to mention here is this optimized targeting section here essentially what this does is it expands your reach outside of the specific audience that you've selected if Google CES relevant"),
     (F["dr"], "this should be turned off because this will expand your targeting outside of just your existing audience and will start pushing to cold and will end up burning through all your budget almost immediately and and not make that targeting relevant so turn that off"),
     (F["dr"], "under the additional formats or additional format options you'll have options to leave on or turn off the autogenerated assets within the display campaigns and I'd highly recommend turning these off because you do sometimes get some pretty bizarre headline recommendations that are autogenerated")])

add("MD-146", "A destination-rerouting toggle was described NINE MONTHS before we banked \"personalized destinations\" as new. Same family, different scope, and MD-140's novelty framing needs correcting",
    "T4", "contested", """
This morning's pass banked MD-140, "personalized destinations", as a newly arriving Meta enhancement that lets the platform send a click to a different page on your site than the one named in the ad. **A transcript published 2025-11-26, nine months earlier, describes a toggle doing something adjacent and tells operators to switch it off:** "And also make sure you deselect optimize website destination because if that's on, it will send to traffic outside of that direct domain, which we don't want."
**Do not fuse these two. The scopes as stated are different and the difference is the whole question.** MD-140's enhancement reroutes within your own site, to a different page. This one is described as sending traffic **outside the domain entirely**. Those are not the same behaviour, and one of the two descriptions is probably wrong, because "Meta sends your paid click to a domain you do not own" is an extraordinary claim that would not have gone unremarked for nine months.
**Held at T4 and contested, because the evidence on this side is nothing at all.** He cites no Meta documentation, runs no test, shows no data, and gives no example. It is one sentence of setup instruction inside a walkthrough. **The honest reading is that an operator saw a destination-optimisation control in late 2025, formed a belief about what it does, and stated it in passing.**
**What this DOES establish, and it is a correction to our own log rather than to Meta.** Destination-side automation is not brand new. The family of controls that lets Meta choose where a click lands has been visible in the interface since at least November 2025. **The 2026-08-27 entry describing personalized destinations as an arriving enhancement overstated its novelty.** The threat that entry names is unchanged and stands: anything that decouples the ad from its destination silently confounds every landing-page test, including the methodology gap now recorded at [[Attribution & Incrementality#AT-106|AT-106]].
**Next step is an account, not another video.** Open the ad-level panel on any of our accounts running traffic to a page and read what destination controls actually exist and what their own tooltips say. That settles MD-140, MD-146 and their relationship in one sitting.
""",
    "Mark Builds Brands, 2025-11-26 (how to test facebook ads post andromeda update); cross-reference MD-140 (banked 2026-08-27, first pass)",
    [(F["and"], "And also make sure you deselect optimize website destination because if that's on, it will send to traffic outside of that direct domain, which we don't want.")])

add("AT-106", "The landing-page test methodology gap is CLOSED, and the answer is that nobody on the roster has a threshold. One source states none at all, the other runs a five-day calendar habit, and they contradict each other",
    "T3", "active", """
The codex has been holding landing-page test RESULTS with no stated methodology behind them. Four transcripts were read specifically to close that gap. **The gap is closed with a negative finding: no source on the roster states a sample size, a conversion floor, or a confidence level for calling a landing-page winner.**
**Source one, a Google Ads agency, gets the shape right and supplies no number.** The requirement is stated as "This means that we're getting enough traffic to the [music] page and letting the page run for a long enough amount of time for those results to actually be real." **That is the entire methodology.** The only two concrete numbers anywhere in their landing-page material are a 50/50 traffic split and a warning not to call it on day one or two: "Once you launch both of those pages, [music] it could be really tempting in day one or two to say, "Oh, variant B is performing way better. Slow down." **Two days is named only as the period to avoid, never as a minimum.**
**Source two supplies a number and it is a calendar habit, not a statistical rule:** "once a week I typically do one split test per funnel. So, Monday through Friday, I'm running a split test, and then whatever I see in terms of the results will dictate the next split test we do". Five days, fixed, regardless of traffic. **This directly contradicts source one's instruction to wait for significance rather than for a window.**
**What a five-day test at his traffic actually returned: a tie.** One arm read 112 clicks of 432 visitors, which recomputes to **25.93%**, against a second arm stated as "around 26%" with no numerator or denominator given. **The honest read is a null result, and it is the outcome the codex should expect from short-window page tests at small traffic.**
**⚠ The instrumentation underneath is thinner than the conclusions drawn from it.** He states his own base and then reasons from it anyway: "And this is based off of 53 sessions. I just installed this, so there's going to be more". **At n=53 a single observed proportion carries a margin of error near plus or minus 13 points at 95% confidence, wide enough that almost any two readings overlap.** Bank this as the negative example: it is what an unstated-methodology page finding looks like underneath.
**⚠ Arithmetic failure in the same file.** "YouTube visitors converted 3.2 times the rate of paid ad visitors. Almost a 60% conversion rate versus a 20% form submission rate." **60/20 = 3.0, and "almost" 60 puts the true multiple below 3.0, not above it.** Reaching 3.2 needs roughly 64% against 20%. The underlying point survives and is worth keeping: traffic source changes page conversion rate enough that results cannot be pooled across sources. **The multiple does not survive and must not be repeated.**
**The collision that makes this urgent.** Source one's condition for a valid test is that "you make sure the traffic going to each page is 50/50 split". **Any platform behaviour that reroutes a share of clicks to a different destination silently violates that condition, and the reader of the test never sees it happen.** Read this beside [[Meta Delivery & Andromeda#MD-146|MD-146]] and MD-140 before trusting any landing-page result, ours or anyone's.
**Scope for our book.** Four of five accounts run Meta Instant Forms, which have no destination to reroute and no scroll or dwell instrumentation at all. **That is precisely why Instant Form results have to be judged on open-to-submit rate alone, and why importing a page-test threshold from these sources would be borrowing a number that does not exist.**
""",
    "Solutions 8, 2025-12-03 (Ultimate Guide to Landing Page Optimization); Solutions 8, 2025-11-13 (From Ad Clicks to Customer Conversions); Dr. Matt Shiver, 2026-04-14 (Claude Just Changed Facebook Ads Forever)",
    [(F["lpo"], "This means that we're getting enough traffic to the [music] page and letting the page run for a long enough amount of time for those results to actually be real."),
     (F["lpo"], "What's really important here [music] is that you make sure the traffic going to each page is 50/50 split."),
     (F["mscl"], "once a week I typically do one split test per funnel. So, Monday through Friday, I'm running a split test, and then whatever I see in terms of the results will dictate the next split test we do"),
     (F["mscl"], "one of them had a 29% average scroll rate. It told me where they dropped off. 78% of visitors never scrolled past 25% of the page, and then 112 of the 432 actually clicked the button of like get the resource now."),
     (F["mscl"], "if we look at this one over here, this was around 26% clicked, and that was about the same as the other one."),
     (F["mscl"], "And this is based off of 53 sessions. I just installed this, so there's going to be more"),
     (F["mscl"], "YouTube visitors converted 3.2 times the rate of paid ad visitors. Almost a 60% conversion rate versus a 20% form submission rate.")])

add("MM-176", "The densest channel on the roster fails its own arithmetic at scale, including a SIGN ERROR narrated on camera with a calculator open. Recompute before banking anything from it",
    "T2", "active", """
Twelve Blue Sense Digital transcripts were read in full in this pass. **Across them, 28 headline figures were recomputed against their own stated components and a large share failed.** This is the same finding already on file for another roster operator at [[Scaling Models#SC-148|SC-148]], now established independently for the channel this codex leans on hardest for unit economics.
**The worst single failure is a sign error, stated as a conclusion, with the calculator on screen.** Walking a scaled profit-and-loss he says: "So, we've got 280 - 104 - 80 - 108 and we are officially at $12,000 in profit." **280 minus 104 is 176; minus 80 is 96; minus 108 is MINUS 12.** The business in his own example is losing $12,000, and he reports it as making $12,000. **His own next step confirms the negative**: he removes $30,000 of overhead and lands on $18,000, and -12 + 30 = 18 while +12 + 30 = 42.
**A representative sample of the rest:**
- A spend increase from $25,000 to $40,000 is called "about an 80% increase". It is **60%**. He had first said 50%, corrected himself upward, and both of his figures are wrong.
- Overhead components of 25 + 20 + 20 + 20 + 18 are summed on camera to **108**. They sum to **103**.
- Cost of delivery is used at three different ratios inside one worked example: stated as 40%, applied as 140 on 280 (50%), then subtracted as 104 (37.1%).
- A campaign said to have "flipped negative" on incremental profit computes **positive**: spend +$11,000 against revenue +$25,000 at his own stated 50% margin yields +$12,500 of gross profit, so incremental contribution is +$1,500 and the incremental ratio is 2.27 against a break-even of 2.0.
- An ad-count instruction of "nearly 200 ads" has components summing to **150**.
- A lifespan adjustment stated as "300 rather than 100" computes to **233** (100 x 70/30).
- An exception band described as "the top 5%" is given components of "six or seven" out of 100, which is **6% to 7%**.
- A $24,000 monthly repayment against a stated $35,000 profit is said to leave "$1,000 in profit". It leaves **$11,000**.
- A two-month cash requirement of double $84,000 is stated as "$160,000". Double is **$168,000**, and doubling is the wrong operation anyway, since month two compounds off a larger base.
**The produce-more-creative rule is stated in both directions in one video, and one direction inverts it.** Twice as cost below revenue or profit; once as "you want to make sure that that expected profit is below the cost of create an asset". **Followed literally, that tells an operator to stop producing creative whenever the ads are profitable.**
**⚠ A separate finding about the HARVEST rather than the speaker.** The string "$15 to $220,000" appears in two different transcripts from this channel, in unrelated contexts (a Google spend threshold and a photo-shoot cost). **A corpus scan returned three occurrences across two files and zero elsewhere in 433 transcripts.** Both readings are incoherent as spoken. This is an auto-transcription artifact, almost certainly "$15 to $20,000" being mangled, and it is a reminder that **a figure inside an auto-generated transcript is evidence of a sound, not of a number.**
**What this does NOT license.** No advertising claim of his is refuted. Most of the failures are narration and calculator slips inside illustrative examples, and his cleanest sequence, banked at [[Marketing Math & Unit Economics#MM-177|MM-177]], recomputes perfectly on every component. **The rule is the same one that stopped three invented numbers entering this codex under another operator's name: recompute before banking, every time, and attach the failure rather than smoothing it.**
""",
    "Blue Sense Digital, 12 transcripts read 2026-08-27, principally 2025-11-27 (Margin Doesnt Expand As You Scale), 2025-03-17 (Creative Planning That Considers Finance), 2025-03-21 (Optimal Spend), 2025-02-11 (Maximum Growth Rate), 2025-02-18 (Gross Margin to Set ROAS Targets)",
    [(F["mar"], "So, we've got 280 - 104 - 80 - 108 and we are officially at $12,000 in profit."),
     (F["mar"], "They're not going to get an exact uh what is this about an 80% increase in returns."),
     (F["mar"], "this spend for this revenue was a 3.75x return. Let's say it erodess to a 3.5 return. Well, that takes revenue to 280, takes cost of delivery to 140."),
     (F["opt"], "Spend increased from $20,000 a month to $31,000 a month, which is about an 11K increase, but revenue only went up by 25K. And so revenue didn't go up incrementally enough in correlation with spends to drive increased profit contribution. And so profit contribution actually flipped negative."),
     (F["cp"], "and so between these you have nearly 200 ads with about 9 Minutes of recording"),
     (F["cp"], "your average active ad might be on for 70 days and so you're actually generating $2,000 over a 70-day period not 30 which means that your ad volume here actually needs to be 300 rather than 100"),
     (F["cp"], "you want to make sure that that expected profit is below the cost of create an asset"),
     (F["gm"], "if you see a 10 rowers or 20 rows or 30 rowers even in your platform you're not actually operating on that you just have tons of overattribution from Brand search and from you retargeting existing customers or you retargeting warm audiences that found out about you elsewhere"),
     (F["mgr"], "let's say we have to pay 6% of our uh Revenue to WL every month that would be 6% multiplied by 400,000 so we would need to pay 24,000 a month in repayment right which means that we would be left with $1,000 in profit"),
     (F["mgr"], "if you wanted to repeat that growth rate for two months we would need double this right so we would need $160,000")])

add("MM-177", "The one fully sound worked example in twelve transcripts, and its conclusion is worth acting on: gross margin decides whether accepting worse efficiency makes or destroys money",
    "T4", "active", """
Banked deliberately beside [[Marketing Math & Unit Economics#MM-176|MM-176]], because a source-reliability warning is only fair if the passages that DO hold are recorded too. **Every component of this sequence recomputes.**
The setup: "in this particular scenario with a business doing $10,000 a day a month a year it doesn't matter for this example $1,000 in spend 100 orders that's a Raz or an me of 10 and that's a CAC of $100 it's costing $100 sorry it's got $10 to acquire each of these orders". 10,000/1,000 = 10 and 1,000/100 = $10, including his live self-correction.
The scaled case at 70% gross margin: revenue $40,000, spend $14,000, gross profit $28,000, contribution $14,000, less $7,000 of operating expense leaves $7,000 net. Baseline net was $6,000 less $5,000 = $1,000. **"the profitability of this business in nominal dollar figures 7 X's when their return on ad span goes down by over 70%".** Checked: 7,000/1,000 = 7x exactly; 40,000/14,000 = 2.857 against a baseline of 10, a 71.4% decline. Net margin 17.5%, up from 10%. **Every figure holds.**
**The same decision at 40% margin destroys the business, and that is the point.** Baseline contribution 10,000 x 0.40 - 1,000 = $3,000; scaled 40,000 x 0.40 - 14,000 = $2,000. Net goes from -$2,000 to -$5,000, "losing 2.5x the amount of money", which checks at 5,000/2,000 = 2.5. *(One figure in that passage does fail: the $3,000 to $2,000 move is a 33.3% decline, stated as 50%.)*
**So the operating rule: an efficiency target is derived, never chosen.** "you may be a business that has a $100 average order value, you make $50 in gross margin on first purchase. And then of this, you might say that well, we want to make 25% in contribution margin, which means we can afford a $25 CAC". $50 - $25 = $25 kept, which is 25% of $100, implying a target ratio of 4. Checks throughout.
**Consequence for how we onboard.** "if they are going to do an audit on your business and they do not ask you for gross margin they will not provide you with a kpis and a gross road map that actually aligns with the financial outcomes of the business." **Margin per case, per truck sold, per funded loan, per retainer month is a required intake field, and on our accounts it is frequently missing.** Without it, any cost-per-lead target we set is a number we made up.
**The distinction that matters most for lead-gen** is his cleanest one-liner: "CPA is based on attributed conversions CAC is based on actual conversions within the store". **Meta's reported cost per lead is the attributed number. The real one is spend divided by new customers confirmed in the client's own system.** That gap is the same one that produced the failure pattern recorded across our own accounts, where cheap leads sat next to a show rate that destroyed the economics.
""",
    "Blue Sense Digital, 2025-02-18 (Why You Need Gross Margin to Set ROAS Targets); 2025-03-21 (Heres How To Find Your Optimal Spend MER)",
    [(F["gm"], "in this particular scenario with a business doing $10,000 a day a month a year it doesn't matter for this example $1,000 in spend 100 orders that's a Raz or an me of 10 and that's a CAC of $100 it's costing $100 sorry it's got $10 to acquire each of these orders"),
     (F["gm"], "the profitability of this business in nominal dollar figures 7 X's when their return on ad span goes down by over 70%"),
     (F["gm"], "CPA is based on attributed conversions CAC is based on actual conversions within the store"),
     (F["gm"], "if they are going to do an audit on your business and they do not ask you for gross margin they will not provide you with a kpis and a gross road map that actually aligns with the financial outcomes of the business"),
     (F["opt"], "you may be a business that has a $100 average order value, you make $50 in gross margin on first purchase. And then of this, you might say that well, we want to make 25% in contribution margin, which means we can afford a $25 CAC")])

add("MM-178", "Judge a period against the plan, not against last period. The platforms only offer the two comparisons that hide the gap",
    "T4", "active", """
"when you use Google or you use Facebook, you click the compare button and they're really your two uh ways that you can compare data over time. And so you end up indexing the performance in real time based on th those two comparison points rather than where you actually want to be against a forecast that then layers up to the financial outcomes for the financial year."
**The observation is accurate to both interfaces and the consequence is real: prior period and prior year are the only two baselines the tools hand you, so those become the baselines everyone reasons from.** A week that improves on a bad week reads as progress while the month is still missing its target.
**Why this earns a place rather than sitting as commentary.** Every weekly client report we produce compares to the previous period. Switching the primary comparison to a stated target changes what the client sees first, and it forces the gap to the plan into the open instead of letting a small week-over-week improvement bury it. **That is the same instinct as the standing honesty rule, applied to the choice of denominator rather than to the wording.**
The diagnostic that follows from it is his month-by-month variance read: months below the efficiency target were overspending months, months above it were underspending months. **He then supplies his own caveat, which is the honest half and the half that usually goes missing: "The ads might not have been as good. There might have been less creative volume. There might have been an account restructure that occurred during this period that caused an efficiency dip."** Any variance-to-plan read has to carry those confounders or it becomes a spending verdict on what was really a creative or structural change.
**Scope guard.** His wider argument, that the blended target should float across the year while the new-customer target stays fixed, rests on repeat-purchase seasonality and **his own numbers for it do not reconcile** (a stated 4.4 in February and 3.2 in July, against repeat shares of 50% and 20%, imply new-customer targets of 2.20 and 2.56, which are 16% apart rather than static). **The floating-target argument is banked as ecommerce-only and unproven.** The comparison-baseline point above stands on its own and does not depend on it.
**Where his own exception lands on our book.** He notes that a business with low repeat purchase can safely hold a flat target all year. **A truck dealer, an auto lender and a B2B company are all near-zero repeat, so a fixed cost-per-new-customer target is correct for them and the whole floating-target apparatus does not apply.**
""",
    "Blue Sense Digital, 2025-05-13 (The 5 Metrics That Actually Matter); 2025-09-09 (The Biggest Mistake Your Making in Forecasting)",
    [(F["5m"], "when you use Google or you use Facebook, you click the compare button and they're really your two uh ways that you can compare data over time. And so you end up indexing the performance in real time based on th those two comparison points rather than where you actually want to be against a forecast that then layers up to the financial outcomes for the financial year."),
     (F["fc"], "The ads might not have been as good. There might have been less creative volume. There might have been an account restructure that occurred during this period that caused an efficiency dip."),
     (F["fc"], "In Feb, we want to hope for a 4.4, but then in July, we're happy to go all the way down to a 3.2.")])

add("CR-195", "The near-duplicate question gets three more witnesses and the instrumentation hole gets wider, not smaller. One operator's whole method IS the near-duplicate case and he never checks it",
    "T4", "contested", """
Nine months, and still nobody on either side has shown an entity ID, a similarity-score reading, or a unique-reach figure. **Three more transcripts today make the absence sharper, because one of them describes a production method that is precisely the case in dispute.**
**The method: permute one recording session into up to 180 ads.** "when I record we record 10 hooks we record three bodies and we generally record two ctas that's number one and so right out of this we immediately get 60 ads now recording this takes me 4 and 1 half minutes", extended to "you have 10 * 3 which is 30 * 3 which is 90 * 2 which is 180 and so you have 180 variations in this instance". Both multiplications check (10x3x2 = 60; 10x3x3x2 = 180).
**He is manufacturing 180 permutations of one shoot and he never once asks whether the platform treats them as 180 entities.** He gets closest with a definition he leaves unmeasurable, "let's just say an ad is a unique variation that is substantially different from a counterpart", and with a judgement call that is explicitly opinion: "I don't think the call to actions are strong enough in variation to be able to substantiate doubling ad volume here and so personally when I do this I just do one CTA I don't think there's enough leverage in the last one to two seconds of the video". **He declines to count CTA swaps as real variation on aesthetic grounds, not on delivery evidence. No entity ID, no similarity score, no unique reach, no delivery data of any kind.**
**A second file confirms the diversity standard in use across the industry is a human eyeballing format categories.** "When I say make five to 10 assets for Black Friday, I don't mean make five assets that all look exactly the same and have slightly different message. I want to see video content. I want to see gift content. I want to see static content. I want to see carousels." **The rule is sound and the measurement behind it does not exist.** Format-category diversity is a weaker test than measuring repetition across a batch, which is what our own batch gate already does at sentence and structure level.
**The third witness reverses himself in seven weeks, which is worth recording because this codex now has a pattern of it.** On 2025-11-26: "This variation spamming game is just not nearly as effective as it was previously", with his split flipped "to the point where my creatives are 80% new concepts and 20% variations". On 2026-01-16, seven weeks later: "maybe you can find a unique spin on a proven concept, a proven format of a static ad, and just iterate, iterate, iterate, and you have just a bunch of variations of highly successful ad." **Neither statement carries a number, and he undercuts his own novelty framing in the same demo: "Now, is this really new concept? No, obviously."**
**Net.** The advice to diversify at concept level survives, because it is cheap insurance either way. **The mechanism is now supported by nobody with instrumentation, contradicted by nobody with instrumentation, and asserted by operators who reverse themselves inside two months.** Anyone citing collapse or its absence should be asked for an entity ID first.
""",
    "Blue Sense Digital, 2025-03-17 (Creative Planning That Considers Finance); 2025-09-24 (The Best Creative Strategy for BFCM 2025); Mark Builds Brands, 2025-11-26 and 2026-01-16",
    [(F["cp"], "when I record we record 10 hooks we record three bodies and we generally record two ctas that's number one and so right out of this we immediately get 60 ads now recording this takes me 4 and 1 half minutes"),
     (F["cp"], "you have 10 * 3 which is 30 * 3 which is 90 * 2 which is 180 and so you have 180 variations in this instance"),
     (F["cp"], "let's just say an ad is a unique variation that is substantially different from a counterpart"),
     (F["cp"], "I don't think the call to actions are strong enough in variation to be able to substantiate doubling ad volume here and so personally when I do this I just do one CTA I don't think there's enough leverage in the last one to two seconds of the video"),
     (F["bf"], "When I say make five to 10 assets for Black Friday, I don't mean make five assets that all look exactly the same and have slightly different message. I want to see video content. I want to see gift content. I want to see static content. I want to see carousels."),
     (F["and"], "This variation spamming game is just not nearly as effective as it was previously."),
     (F["and"], "But now, this has basically been completely flipped to the point where my creatives are 80% new concepts and 20% variations."),
     (F["mbai"], "maybe you can find a unique spin on a proven concept, a proven format of a static ad, and just iterate, iterate, iterate, and you have just a bunch of variations of highly successful ad."),
     (F["mbai"], "Now, is this really new concept? No, obviously.")])

add("CR-196", "Do not put images and video in the same ad set: one format takes the spend and the other gets none",
    "T3", "active", """
"typically what I see is if you throw a bunch of images and videos in the same ad set, one of them will cannibalize everything else. Like all the videos will get spent and the images will get no spend".
**Number-free.** He describes a repeated cross-account observation and states no spend split, no frequency, no sample. **It is a delivery-mechanics claim, not a category one, so it transfers to lead-gen unchanged.**
**Why it earns a place.** It is a concrete, testable, format-level version of the starvation behaviour we already have on file from our own accounts, where new creative gets starved inside campaign-budget structures. It also gives a cheap explanation for a common reading error: a static that "failed" may simply never have been funded, because a video in the same ad set absorbed the budget. **Check spend before judging a format.**
The same operator describes the general starvation shape with a worked illustration: "It could quite literally spend $99 in this one ad set and 50 cents here and 50 cents here." That sums to $100 and is consistent.
**His attached testing preference is separate and weaker:** "I typically do my testing with images cuz you can typically just do it faster." Production speed, no performance comparison. It happens to match how our static-heavy chiropractic and truck work already runs.
**Related and unevidenced, worth one line so it is not mistaken for a finding:** he claims heavy on-image text tends to raise CPMs, "I'm actually not a huge fan of having a ton of text on your image ads because a lot of times you can see it increase your CPMs, but sometimes it's worth it, you know?" **No cost figure, no threshold for how much text is too much, no test, and no Meta documentation.** It points the same direction as our own chiropractic result that the best-performing image ads carried no on-image text at all, which is corroboration of direction only.
""",
    "Mark Builds Brands, 2025-11-26 (how to test facebook ads post andromeda update); 2026-01-16 (AI image ads)",
    [(F["and"], "typically what I see is if you throw a bunch of images and videos in the same ad set, one of them will cannibalize everything else. Like all the videos will get spent and the images will get no spend"),
     (F["and"], "It could quite literally spend $99 in this one ad set and 50 cents here and 50 cents here."),
     (F["and"], "I typically do my testing with images cuz you can typically just do it faster."),
     (F["mbai"], "I'm actually not a huge fan of having a ton of text on your image ads because a lot of times you can see it increase your CPMs, but sometimes it's worth it, you know?")])

add("SC-150", "A $10-per-ad budget floor, and an exception clause that can never fire. His own minimum structure already exceeds it",
    "T4", "active", """
The rule: "Well, I have a golden rule that I would have at least $10 allocated out of my total budget per ad in the CBO." It is internally consistent with his own worked example, where 3 ad sets x 3 ads = 9 ads at $10 = a $90 daily campaign budget.
**⚠ The exception attached to it is dead logic, and it matters because operators quote exception clauses as floors.** "The one exception to this rule is I would never recommend that you run a CBO at less than $50 a day." **His own minimum recommended structure is 3 concepts x 2 variations = 6 ads, which at $10 per ad is $60 per day. The $50 floor sits below the cheapest structure he recommends, so it can never be triggered by any build he proposes.** He also flags it as opinion himself: "It's my personal opinion."
**Why this is banked rather than discarded.** Read carelessly, "$50/day minimum" becomes a rule that says several of our clients should not advertise at all. **The real content of his rule is the per-ad floor, and the per-ad floor is calibrated to a purchase event.** A purchase fires on maybe 1% to 3% of clicks; a form submission fires far more often, so the per-ad spend needed to read signal on a lead objective is lower. **Do not import $10 per ad unexamined onto a lead-gen account, and do not import $50/day as a floor at all.**
**The structure he recommends is worth reading beside laws 4a and 4d on ad counts.** "I'll tell you what I recommend is anywhere from three to five ad sets, which means three to five concepts, completely unique concepts, and anywhere from two to five variations in each of those ad set." Recomputed against his own budget rule, that shape demands $60/day at its minimum and $250/day at its maximum. **At our clients' budgets the maximum shape is unaffordable, which is the same squeeze already recorded at MD-137: how many ads Meta actually funds is a function of account spend.**
A second operator arrives at the moderate version of the same argument from the other direction, and his is the one that survives translation to a local budget: "you're probably launching 20 ads a week right now take that to 40 or 60 and that's enough you don't need to go to 300."
""",
    "Mark Builds Brands, 2025-11-26 (how to test facebook ads post andromeda update); Blue Sense Digital, 2025-03-17 (Creative Planning That Considers Finance)",
    [(F["and"], "Well, I have a golden rule that I would have at least $10 allocated out of my total budget per ad in the CBO."),
     (F["and"], "The one exception to this rule is I would never recommend that you run a CBO at less than $50 a day."),
     (F["and"], "It's my personal opinion."),
     (F["and"], "I'll tell you what I recommend is anywhere from three to five ad sets, which means three to five concepts, completely unique concepts, and anywhere from two to five variations in each of those ad set."),
     (F["cp"], "you're probably launching 20 ads a week right now take that to 40 or 60 and that's enough you don't need to go to 300")])

add("MD-147", "Rolling reach, the instrument nobody here runs: net new reach reportedly falls 70% in peak retail season while the platform leans on warm audiences",
    "T3", "active", """
The claim, with a stated method and sample size and no shown data: "I've looked at over 50 ad accounts to validate this point, which is why I say it with such confidence, which is that you can look at rolling reach in your account. And what you will see in November is that the amount of net new reach that you get in the ad account is like 70% lower than September and October."
**⚠ His two headline numbers are not consistent with each other.** He also states "It costs like 5x more to target new people during the November period." **At constant spend, a 70% fall in net new reach gives 1/(1-0.70) = 3.33x, not 5x. Reaching 5x needs an 80% fall.** Reconciling the two requires an unstated third factor of about 1.5x in CPM, which he gestures at and never states. **There is also no spend normalisation: net new reach falling 70% while spend also moves is a different claim from reach-per-dollar falling 70%, and he never says which he measured.** Held at T3 for that reason, despite the stated 50-account base.
**His mechanism is assertion:** "Meta wants to serve on these warm audiences because it knows they're the people that will convert." No documentation, no test. Note that the same behaviour falls straight out of the bidding model at [[Auction Mechanics & Bidding#AU-082|AU-082]] without anyone at Meta intending anything, so the observation does not require his explanation.
**What is genuinely worth taking, and it is the instrument rather than the number.** **Rolling reach is a metric none of our five accounts tracks.** For a local-service client it answers a question the lead count cannot: whether we are still finding new people in the catchment, or recycling the same pool at rising frequency. **In a city-radius account the ceiling on net new reach is the catchment population, not the retail calendar, so the 70% seasonal figure does not transfer and the measurement absolutely does.**
The related operating instruction, banked as his recommendation and not as evidence: "I would be focusing on heavy audience exclusions so you're actually reaching new users. I would actually be looking at rolling reach to try to increase it during Q3". **The exclusion half already matches our standing practice of putting exclusions on cold campaigns only.**
**⚠ One claim from the same file is QUARANTINED so it is never read out of context.** He says "Don't run lead campaigns. It's your way to quantify spend in an early period before Q4, but it's just a bad strategy in itself, and you end up just losing more money than if you spent on cold top ofunnel campaigns." **He is talking about email-capture campaigns used as a proxy metric ahead of a retail sale. He is not talking about lead generation as a business model.** Our entire book is lead capture closed by a phone call. **This sentence must never be quoted as "lead campaigns do not work."** It carries no comparison, no test and no account either way.
""",
    "Blue Sense Digital, 2025-09-22 (You Will Guaranteed Underspend on Paid Ads In September October)",
    [(F["us"], "I've looked at over 50 ad accounts to validate this point, which is why I say it with such confidence, which is that you can look at rolling reach in your account. And what you will see in November is that the amount of net new reach that you get in the ad account is like 70% lower than September and October."),
     (F["us"], "It costs like 5x more to target new people during the November period."),
     (F["us"], "Meta wants to serve on these warm audiences because it knows they're the people that will convert."),
     (F["us"], "I would be focusing on heavy audience exclusions so you're actually reaching new users. I would actually be looking at rolling reach to try to increase it during Q3"),
     (F["us"], "Don't run lead campaigns. It's your way to quantify spend in an early period before Q4, but it's just a bad strategy in itself, and you end up just losing more money than if you spent on cold top ofunnel campaigns.")])

add("CR-197", "A plain offer on a flat background is named the top performer across accounts and industries, which is independent support for our own zero-text finding",
    "T3", "active", """
"Number one, and this is absolutely one of the top performing assets across accounts and across industries, is the plain image with the clear offer. Something as simple as just a black background with the discount that you've got going, the name of the brand, and if you want to take it a step further, even something like a star review rating. I can guarantee majority of the time is going to be the top performing in your account during Black Friday."
**Number-free, and stated with a guarantee.** No account count, no win rate, no cost per result, no share of spend. "Majority of the time" is the closest thing to a figure and it is undefined. **Tiered T3 on the strength of a cross-account claim from a real book of business, and nothing more.**
**Why it is worth banking anyway: it is independent, from a different category, and it points the same way as our own strongest creative result.** Our chiropractic work found that 93% of winning image ads carried zero on-image text, and the client rejection that produced the batch gate was about too much text. **An ecommerce operator arriving at "plain background, the offer, a rating" from a completely different starting point is corroboration of direction.**
**The boundary matters.** His asset is the OFFER stated plainly, not a busy graphic. That is consistent with our finding and inconsistent with the reading that "static beats video". **He contradicts himself on that second point inside the same video**, arguing separately that "video content will always be one of the initial touch points for a new customer" while naming a static as his top performer. **The distinction he is reaching for and never states cleanly is that video recruits and static converts. Neither half is shown.**
**One transferable production rule from the same file, with the inventory language stripped:** build the late-flight assets from whatever is winning mid-flight rather than pre-producing them. **"stock almost sold out" has no equivalent for a clinic and would be a false scarcity claim, so take the method and drop the wording.**
**His asset-count guidance does NOT transfer and should not be quoted.** His small-brand band starts at $40,000/month, roughly 26 times a $50/day local budget, and his own counts contradict his own 80/20 evergreen-to-new ratio: 15 evergreen plus 20 new is 35 assets, which is 57% new, not 20%.
""",
    "Blue Sense Digital, 2025-09-24 (The Best Creative Strategy for BFCM 2025)",
    [(F["bf"], "Number one, and this is absolutely one of the top performing assets across accounts and across industries, is the plain image with the clear offer. Something as simple as just a black background with the discount that you've got going, the name of the brand, and if you want to take it a step further, even something like a star review rating. I can guarantee majority of the time is going to be the top performing in your account during Black Friday."),
     (F["bf"], "video content will always be one of the initial touch points for a new customer"),
     (F["bf"], "purely because I recommend taking whatever assets you're seeing winning during your launch and then turning that into your urgency messaging and literally just overlaying things like saying last chance or ends midnight or stock almost sold out and running those new assets for the last few days of your promotion."),
     (F["bf"], "And I'd go with an 80 to20 ratio here. So, 80% of your content, I would argue, should be your proven winners.")])

add("LS-073", "Another futility hedge on micromanagement, and the duration question stays open. Three transcripts, no number",
    "T4", "active", """
Read specifically to close the open question of how long to wait before reacting to a delivery wobble. **The question is not closed.**
The nearest statement: "Much of what happens in the campaign and ad set now doesn't need constant tweaking, and using AI to make automated adjustments there would likely be counterproductive." **That is consistent with the futility position already recorded for this operator, and it is another hedge. "Likely" is his own word. He gives no waiting period, no spend floor, no conversion count and no data.**
**So the codex still holds a rule with a missing number: he gates panic on DURATION and has never said what duration is enough.** Three more of his transcripts were read in full today and none supplies it.
**What did arrive is a limit-of-knowledge admission worth more than most assertions.** "It's bad because it's close to impossible to direct people to a central source of truth related to how things work today. I initially gave up on trying a few years ago." He also treats his own published material as expiring: content stops being used as a source "once it was 6 months old". **A six-month freshness rule set by one of the most careful operators on the roster is a reasonable default for anything in our own playbooks that describes a Meta feature by name.**
His evidence that feature-named documentation decays: "I produced two courses that immediately became irrelevant or mostly outdated. One for a feature that disappeared and one for a feature that completely changed." **Consequence for us: write client SOPs around outcomes, not around a named Meta feature, because the feature is the part that dies.**
**On AI in the account, his split is the useful part.** Campaign and ad set level, hands off. Creative, the opposite: "I think you're right to focus on potential uses of AI for creative development, because it's the biggest bottleneck for agencies." **And the guard: "AI is not a replacement for knowledge... they'll be executing bad strategies faster than before."** That is an argument for the grade-before-ship habit we already run, applied to anything generated.
**One capability note with its scope attached.** He reports that Meta has shipped connectors letting an advertiser attach a business portfolio to an outside AI tool, and states plainly that he has not used it in an agentic workflow. **Nothing he says afterwards is tested experience of AI operating an account.**
**Targeting: nothing usable.** The single reference across all three files is a job-description list item naming "ad targeting and audience suggestions" with no mechanism attached. **It confirms his vocabulary separates suggestions from targeting and adds no evidence about whether suggestions bind.**
""",
    "Jon Loomer, 2026-06-03 (Can AI Actually Make You a Better Advertiser); 2026-05-18 (Change Will Always Be Your Biggest Problem); 2026-04-13 (Stop Hiding Your Ad Account from Clients)",
    [(F["jlai"], "Much of what happens in the campaign and ad set now doesn't need constant tweaking, and using AI to make automated adjustments there would likely be counterproductive."),
     (F["jlch"], "It's bad because it's close to impossible to direct people to a central source of truth related to how things work today. I initially gave up on trying a few years ago."),
     (F["jlch"], "once it was 6 months old"),
     (F["jlch"], "I produced two courses that immediately became irrelevant or mostly outdated. One for a feature that disappeared and one for a feature that completely changed."),
     (F["jlai"], "I think you're right to focus on potential uses of AI for creative development, because it's the biggest bottleneck for agencies."),
     (F["jlai"], "AI is not a replacement for knowledge"),
     (F["jlai"], "they'll be executing bad strategies faster than before."),
     (F["jlhd"], "It's knowing how ad targeting and audience suggestions work now.")])

add("MM-179", "Run the client's own ad account, pixel and audiences, and give the client full visibility. The asset history is the client's, and a fresh dataset restarts learning from zero",
    "T3", "active", """
"There really two ways to manage a client's ads and do so without violating any of Meta's rules. You can probably have the client share their ad account and assets with you, which is probably cleanest and preferred. Or you can create a separate ad account for all of your clients that you own." **He asserts what Meta's rules permit without citing the policy, so treat it as practitioner practice rather than documentation.**
The substantive half: "If possible, manage the client's ad account and use their pixel, events, and audiences. That way, when your relationship inevitably ends, because they all will eventually, they will have that history and those assets to pass to the next agency."
**The reason this is an operating rule and not an ethics preference: signal history has cash value.** An account optimising on a booked-appointment or lead event carries a conversion dataset that took months to build. **Moving a client onto a fresh pixel restarts learning from zero and the client pays for that in cost per lead, twice, once on the way in and once on the way out.**
On access: "Give your client access to everything. You don't need to hide it." **It raises the bar on reporting rather than lowering it, because a client who can open the account can check every number we send. That is the same direction as the standing rule to lead a report with the real number.**
**One caveat on the attribution instruction attached to it.** He recommends never taking conversion counts at face value and breaking down by attribution setting instead. **The compare-attribution-settings view returns dashes on Instant Form leads, so this only works on the pixel-based landing-page funnels.** Four of five accounts cannot run it.
His structure preference is stated without a number: "Minimal campaigns and ad sets, minimal settings flipped." **"Minimal" is never quantified into a count, so it is a consolidation bias and cannot settle any specific structure argument.**
""",
    "Jon Loomer, 2026-04-13 (Stop Hiding Your Ad Account from Clients)",
    [(F["jlhd"], "There really two ways to manage a client's ads and do so without violating any of Meta's rules. You can probably have the client share their ad account and assets with you, which is probably cleanest and preferred. Or you can create a separate ad account for all of your clients that you own."),
     (F["jlhd"], "If possible, manage the client's ad account and use their pixel, events, and audiences. That way, when your relationship inevitably ends, because they all will eventually, they will have that history and those assets to pass to the next agency."),
     (F["jlhd"], "Give your client access to everything. You don't need to hide it."),
     (F["jlhd"], "It's knowing that you shouldn't take conversion results at face value. So you break down by attribution setting or use the compare attribution settings feature."),
     (F["jlhd"], "Minimal campaigns and ad sets, minimal settings flipped.")])

add("MM-180", "Two widely-taught lead-form rules that our own funnel already rejects, banked so nobody imports them later",
    "T4", "refuted", """
Recorded as REFUTED for our operating model specifically, with the reasoning attached, because both are stated as best practice by a credible agency and will otherwise be re-imported by whoever reads that source next.
**One: asking on the form when the person is free to talk.** "Maybe you ask about the [music] date that they can talk or what their price range is."
**Rejected on the scheduling half.** In our delivery stack a form's only job is to qualify and capture contact. The voice agent books live against a real calendar on opt-in. **A "when can you talk" field manufactures a soft commitment the agent then has to renegotiate on the call, which makes the booking harder rather than easier.** The price-range half is a legitimate qualifying question and is kept.
**Two: promising a response window on the thank-you page.** "we'll email you in 24 hours with this price and three [music] available time slots is a thousand times better than hey thanks talk to you later."
**Rejected on the timeframe.** The agent dials on opt-in regardless of the business's opening hours, so a stated window is both unnecessary and a promise we can be measured against and beaten by. *(Arithmetic note: "a thousand times better" is rhetorical, has no components and no measured comparison behind it.)*
**What survives from the pair, and it is the useful residue.** The underlying instinct is right: an end screen that states what actually happens next beats a generic thank you. **Say what happens, not when.**
**Kept from the same source, and it does transfer:** "The goal is not to have the fewest fields. It's to have the right fields for the better experience", and the observation that a phone-number field is where people commonly stall because they expect spam calls. **Field count is the main lever available on an Instant Form, and "fewer is always better" is not the rule; "the three that qualify" is.**
""",
    "Solutions 8, 2025-11-13 (From Ad Clicks to Customer Conversions)",
    [(F["ac"], "Maybe you ask about the [music] date that they can talk or what their price range is."),
     (F["ac"], "we'll email you in 24 hours with this price and three [music] available time slots is a thousand times better than hey thanks talk to you later."),
     (F["ac"], "The goal is not to have the fewest fields. It's to have the right fields for the better experience."),
     (F["lpo"], "If [music] we're only asking them for a first name, last name, phone number, and people are stopping at that phone number field, that lets us know that that's sensitive content that they're not [music] willing to give")])

add("CR-198", "A neuroscience-branded copy framework in which not one study is named. Two ideas survive on their merits, the numbers do not",
    "T4", "active", """
Banked mainly as a guard, because the material is framed as settled science and cites nothing.
**Every empirical claim in it is unsourced.** The headline figure: "And turns out your subconscious thoughts actually rule 95% of your life. 95% of your thoughts, 95% of your purchasing decisions are decided in the subconscious." **No numerator, no denominator, no measurement method, no study.** His entire sourcing is "So, there have been plenty plenty plenty of studies on this". A researcher is named with the name mangled ("Dr. Antonio Deasio") and no paper, journal or year. A second is named as "Talisho" with "I don't know if I'm pronouncing that correctly". An experiment is introduced as "There was this experiment done" with no patient count, no effect size and no latency. **The 95% figure must never appear in a client document.**
**One strand is not neuroscience at all and he says so himself:** a "levels of consciousness" scale attributed to David Hawkins, introduced with "At this point, this is getting a little unconventional. This is not directly neuroscience, even though it was developed by a doctor." **Not operational. Do not build copy guidance on it.**
**What survives, on its own merits rather than on the science framing.**
The prior-belief point is genuinely useful and matches our accounts: copy has to move the belief the reader arrives with before any claim lands, because "either install empowering beliefs or remove limiting beliefs". **Our buyers arrive with hard priors, that chiropractors are a scam, that no lender will approve them, that AI tools never work, and the hook has to break that before the offer is even readable.**
The structural order, emotional hook then logical proof then the ask, is the standard ad body shape and works for a pain hook or a financing hook. **Untested against any other order, by him or by anyone.**
**⚠ One of his techniques is a compliance hazard on two of our accounts and must carry that warning wherever it travels.** He recommends repeated second-person identity assignment: "If you repeatedly use you are or you, you can get people into kind of this hypnotic trance where you can then be able to shift their beliefs very, very effectively." **Meta's personal-attributes policy treats copy that implies the reader has a condition as a violation, and second-person identity labelling is exactly the pattern that gets chiropractic ads rejected.** The same applies to his guilt-matching advice. The abstract idea of meeting the reader in their current state transfers. **The guilt lever and the "you are" construction do not, for ChiroWorks or Chiropraise.**
""",
    "Mark Builds Brands, 2026-05-28 (Neuroscience Confirms this is what makes people buy from your ads)",
    [(F["neu"], "And turns out your subconscious thoughts actually rule 95% of your life. 95% of your thoughts, 95% of your purchasing decisions are decided in the subconscious."),
     (F["neu"], "So, there have been plenty plenty plenty of studies on this"),
     (F["neu"], "This is Dr. Antonio Deasio."),
     (F["neu"], "I don't know if I'm pronouncing that correctly"),
     (F["neu"], "There was this experiment done where scientists hooked patients up and recorded their actual brain cells firing during the decision-making process and they watched the amygdala fire first before the thinking part even lit up."),
     (F["neu"], "At this point, this is getting a little unconventional. This is not directly neuroscience, even though it was developed by a doctor."),
     (F["neu"], "So either install empowering beliefs or remove limiting beliefs."),
     (F["neu"], "It's like emotional hook, logical justification, CTA."),
     (F["neu"], "If you repeatedly use you are or you, you can get people into kind of this hypnotic trance where you can then be able to shift their beliefs very, very effectively.")])

add("MM-181", "Meta partnership ads: three conditions, no auction mechanism claimed, and a headline result the speaker disowns in the next sentence",
    "T3", "active", """
The three stated conditions for a creator-post ad to work: the post has to read organic, the caption has to match the video, and the creator has to be the target customer.
On organic feel: "So, constraint number one, the post needs to feel organic. We have tested a lot of white-listing ads recently. And if the post seems salesy, if it seems like an ad, they just don't work." **Number-free: a body of tests across accounts, reported with zero data.**
On casting: "And the closer that we've gotten to having a one-to-one on this person is identical to our exact target demographic, they're the ones that have performed the best." **This is the same rule as our own age-true casting for the 65-plus chiropractic statics and Spanish-language casting for the truck accounts, arrived at independently.**
**The operationally load-bearing detail, and the one that costs money if missed: the creator's caption cannot be edited afterwards.** "the copy that they put on there, you can't edit it. You're stuck with that copy. And so, you need to make sure that you're ideally providing the copy to that creator so that they can just go and copy your copy and paste it straight in". **Any partnership or creator-post setup has to ship the exact caption to the creator before they post.**
**⚠ The headline number is self-confounded and he says so.** He opens with a brand going from "1.5 to $2,000 a day" to "$11,000 in a single day", then immediately: "Now, in all honesty, that isn't just partnership ads in itself. It's a lot of different things that we went and implemented when we started working with this brand". **The $11,000 is a single-day peak against a prior daily average, and the "3 to 400,000" run rate is that one day multiplied by 30 ($11,000 x 30 = $330,000), not an actual 30-day total. The upper bound of $400,000 needs $13,333/day, which nothing stated supports.**
**⚠ A deliberate ABSENCE worth recording, so the codex does not infer more than the source says.** Across the whole transcript there is **no claim that the auction or delivery treats a partnership ad differently from a normal ad, and no claim that likes, comments or shares accumulate on the post or carry across ad sets.** His entire case is perceived organic-ness, caption alignment and creator match. **Nobody should cite this source for a social-proof or auction mechanism.**
""",
    "Blue Sense Digital, 2025-03-27 (How To Make Meta Partnership Ads Work For You)",
    [(F["pa"], "So, constraint number one, the post needs to feel organic. We have tested a lot of white-listing ads recently. And if the post seems salesy, if it seems like an ad, they just don't work."),
     (F["pa"], "And the closer that we've gotten to having a one-to-one on this person is identical to our exact target demographic, they're the ones that have performed the best."),
     (F["pa"], "the copy that they put on there, you can't edit it. You're stuck with that copy. And so, you need to make sure that you're ideally providing the copy to that creator so that they can just go and copy your copy and paste it straight in"),
     (F["pa"], "They were doing 1.5 to $2,000 a day. Now, just the other day, they did $11,000 in a single day."),
     (F["pa"], "Now, in all honesty, that isn't just partnership ads in itself. It's a lot of different things that we went and implemented when we started working with this brand")])

add("GA-067", "Google's top-of-funnel ceiling arrives sooner for a single suburb than for a national catalogue, and the operator's evidence for it is nothing",
    "T4", "active", """
The mechanism, asserted with no data: "Google has a top of funnel problem why Google has a top of funnel problem is because once you max out the keyword volume that is available for your particular product portfolio and yes maybe you could get some incremental uh impression share as well but the incrementality of that impression share is too expensive to be profitable or it's too low quality to be profitable". **No impression-share figure, no cost curve, no account. Pure assertion, and it is the mechanism carrying his whole thesis.**
**Banked anyway because the argument bites harder for our clients than for his.** A single suburb has far less monthly search volume than a national ecommerce catalogue, so **the keyword ceiling arrives sooner for a local clinic or a local dealership than for any Shopify brand.** That is a reason to expect Google to cap out at low spend on local-service accounts and to treat Meta as the volume channel, which is how we already run the accounts that have both.
**His stated RESULT is a budget allocation, not a performance finding, and the distinction matters.** "we used to have about a 70% skew towards Google adspend across our client portfolio now it is the opposite 70% to spend maybe even a little bit more is currently on meta". **These are shares, not dollars. With no absolute spend stated, the identical flip is produced by Google holding flat while Meta triples, or by Google collapsing while Meta holds. It cannot be read as "Google spend was cut", and it is not evidence that Google performed worse.**
**On Performance Max, his instrumented claim is the one worth keeping and it is still number-free:** "we've done incrementality tests as well with Brands as to where the performance ma is actually contributing additional new customers to the business and in a lot of instances it isn't in some instances it does but there isn't that consistency across account to account". **Real test type, real brands, and no count, no lift figure, no split between "a lot" and "some".** Usable as a reason to instrument PMax rather than trust its reported conversions, and as evidence of nothing else. It applies directly to any account of ours running PMax alongside search.
**⚠ One claim from this file must not travel into any client document:** that Google deliberately obscures its own incrementality so advertisers cannot see when it is failing. **That is an attribution of motive to a company, with no documentation, no internal source and no test. It is the weakest claim in the file and it sits underneath the video's entire thesis.**
**⚠ And one figure is unusable:** his stated Google spend threshold reads "$15 to $220,000 a month", which has no coherent reading. See [[Marketing Math & Unit Economics#MM-176|MM-176]]: the identical garbled string appears in a second transcript from this channel, so it is a transcription artifact and **no threshold claim can be carried from it.**
""",
    "Blue Sense Digital, 2025-02-06 (Why Meta Ads Is Beating Google Ads In 2025)",
    [(F["mg"], "Google has a top of funnel problem why Google has a top of funnel problem is because once you max out the keyword volume that is available for your particular product portfolio and yes maybe you could get some incremental uh impression share as well but the incrementality of that impression share is too expensive to be profitable or it's too low quality to be profitable"),
     (F["mg"], "we used to have about a 70% skew towards Google adspend across our client portfolio now it is the opposite 70% to spend maybe even a little bit more is currently on meta"),
     (F["mg"], "we've done incrementality tests as well with Brands as to where the performance ma is actually contributing additional new customers to the business and in a lot of instances it isn't in some instances it does but there isn't that consistency across account to account"),
     (F["mg"], "it's because they like to obscure the actual incremental impact of the platform as opposed to directly show you hey meta actually isn't working for you right now"),
     (F["mg"], "most people can effectively generate new customers profitably at $15 to $220,000 a month and spend on Google but past that I would really be limiting any kind of growth efforts through them as a channel")])

add("MM-182", "New-customer efficiency decays in a fixed geography, and a city-radius account saturates orders of magnitude faster than a national one",
    "T4", "active", """
"if you take time and you take a it will always degrade and ultimately it should uh no it will never degrade to zero because you continue to have new populations entering into the target market."
**Pure assertion. No saturation curve, no account, no test, and the supporting illustration is Pepsi and Coca-Cola.** Tiered T4 accordingly.
**It is banked because it transfers harder to our book than to his, and because the codex has no entry that states it.** A clinic in Collinsville or Novi advertises into a catchment measured in tens of thousands of people. **A national ecommerce brand's pool is measured in tens of millions. The same decay mechanism therefore arrives orders of magnitude sooner for us, which is the structural reason a local account's cost per lead climbs even when nothing about the creative or the offer changed.**
This is the honest counterweight to his own scaling optimism. He states elsewhere that a stable acquisition cost at higher volume means "this is a golden goose that you should just be cranking up". **That condition barely exists inside a single-city catchment**, and the same operator contradicts it flatly three months earlier: "there is one fundamental truth that exists within advertising and it's that CAC will go up it's the only thing that exists as you scale up advertising spend you will lose efficiency and there is no way around that". **The two statements are irreconcilable as stated. The practical resolution is that the February version holds inside a fixed geography and the May version needs a new geography, channel or offer to be true.**
**The lever he offers when a market saturates is genuinely useful and costs nothing to adopt:** redefine anyone past a lapse window as a new customer. "you for example could say that your attrition period on an average existing customer is 400 days. And so anyone that has purchased uh greater than 400 days ago is now redefined from a returning customer into a new customer." **A chiropractic patient who has not attended in 400 days is, operationally, a fresh acquisition, and the same applies to a lapsed truck buyer.**
**One measurement caution that applies to every campaign we split by audience temperature:** "you're inferring that your allocation of ad spend across these two P&Ls is an accurate representation of what the platforms are actually serving on which just isn't correct. Like the platforms will spend more accidentally on these audiences." **Asserted, not measured, and consistent with the exclusion-leak reconciliation already on file.**
""",
    "Blue Sense Digital, 2025-05-29 (Heres How To Fix Acquisition MER At Scale); 2025-02-18 (Why You Need Gross Margin to Set ROAS Targets)",
    [(F["mer"], "if you take time and you take a it will always degrade and ultimately it should uh no it will never degrade to zero because you continue to have new populations entering into the target market."),
     (F["mer"], "if you can spend in a place that's going to continue to deliver similar levels of CAC, then you are simply under spending. Like this is a golden goose that you should just be cranking up."),
     (F["gm"], "there is one fundamental truth that exists within advertising and it's that CAC will go up it's the only thing that exists as you scale up advertising spend you will lose efficiency and there is no way around that"),
     (F["mer"], "you for example could say that your attrition period on an average existing customer is 400 days. And so anyone that has purchased uh greater than 400 days ago is now redefined from a returning customer into a new customer."),
     (F["mer"], "you're inferring that your allocation of ad spend across these two P&Ls is an accurate representation of what the platforms are actually serving on which just isn't correct. Like the platforms will spend more accidentally on these audiences.")])

add("MM-183", "A flat budget makes forecasting impossible, and daily reads at our clients' spend are noise",
    "T3", "active", """
Two constraints from the same file that between them govern how any of our accounts can honestly be modelled.
**One: no spend variance, no forecast.** "if you've only ever spent $20,000 a month forever, right? Because then all of your data will just look like this. It'll look something like this. And so, you won't be able to draw any conclusions here because you don't have varying data sets of spend." **A client held flat at $50/day for months has no variance, which means any spend-response model built off that history is decoration.** He demonstrates a three-point regression live and concedes it is "so inaccurate", showing no error band and no fit statistic.
**Two: the window has to match the volume.** "You'd want to be an eight-figure business if you're going to look at daily data here. Um if you're a smaller business, you'd go for weekly or potentially even monthly." **The threshold is asserted with no variance or sample-size calculation behind it, so treat the number loosely and the direction firmly. Every client we run is far below it, so a daily read of cost per lead is noise and the weekly or monthly window is the only defensible one.** That is a direct argument for the reporting cadence we already run and against reacting to a single bad day.
**The correct stopping rule for spend, stated cleanly:** "the optimal point of spend is the point in which incremental profit contribution becomes negative." Standard marginal economics, nothing empirical behind it here, and it is still the right rule for setting a daily budget with cost per booked appointment standing in for order economics.
**⚠ He contradicts himself on what to do with that answer, inside the same file.** Having defined the optimal point, he says "even if we determine and we can determine using models that we have internally what your optimal spending and MER is, you still shouldn't spend that amount." **He frames the first as the answer for a business holding steady and the second as the answer for a business growing, and never says which a media buyer should act on in a given month.**
**When added spend fails to add profit, his diagnosis list is the useful part and it transfers whole:** "Maybe you just didn't have enough creative velocity to be able to sustain those high spend levels. Maybe the landing page started falling apart on the additional cold traffic that you tried layering in through different angles and so, you need more landing page testing. Maybe it was simply a product saturation issue". **Creative velocity and landing-page capacity carry over verbatim; product saturation becomes offer or geography saturation.**
""",
    "Blue Sense Digital, 2025-03-21 (Heres How To Find Your Optimal Spend MER)",
    [(F["opt"], "if you've only ever spent $20,000 a month forever, right? Because then all of your data will just look like this. It'll look something like this. And so, you won't be able to draw any conclusions here because you don't have varying data sets of spend."),
     (F["opt"], "You'd want to be an eight-figure business if you're going to look at daily data here. Um if you're a smaller business, you'd go for weekly or potentially even monthly."),
     (F["opt"], "the optimal point of spend is the point in which incremental profit contribution becomes negative."),
     (F["opt"], "even if we determine and we can determine using models that we have internally what your optimal spending and MER is, you still shouldn't spend that amount."),
     (F["opt"], "Maybe you just didn't have enough creative velocity to be able to sustain those high spend levels. Maybe the landing page started falling apart on the additional cold traffic that you tried layering in through different angles and so, you need more landing page testing. Maybe it was simply a product saturation issue")])

# ---------------------------------------------------------------- verify
def norm(s):
    s = (s.replace("’", "'").replace("‘", "'")
          .replace("“", '"').replace("”", '"')
          .replace("—", "-").replace("–", "-"))
    return re.sub(r"\s+", " ", s).strip()


bodies, ok, fail = {}, 0, 0
for c in CLAIMS:
    for path, q in c["quotes"]:
        if path not in bodies:
            bodies[path] = norm(open(path, encoding="utf-8").read())
        if norm(q) in bodies[path]:
            ok += 1
        else:
            fail += 1
            print(f"QUOTE FAIL in {c['id']}: {q[:110]}")
            n = norm(q)
            lo, hi = 0, len(n)
            while lo < hi:
                mid = (lo + hi + 1) // 2
                if n[:mid] in bodies[path]:
                    lo = mid
                else:
                    hi = mid - 1
            print(f"   longest verbatim prefix ({lo}): {n[:lo][-80:]!r}")
            print(f"   diverges at: {n[lo:lo+60]!r}")

print(f"\nQUOTES VERIFIED {ok}  FAILED {fail}")
if fail:
    print("ABORTING: nothing written.")
    sys.exit(1)

# ---------------------------------------------------------------- write
for c in CLAIMS:
    tf = os.path.join(SCI, TOPIC[c["id"][:2]])
    entry = (f"\n### {c['id']} · {c['title']}\n"
             f"Tier: {c['tier']} · Status: {c['status']}\n"
             f"{c['body']}\n"
             f"Sources: {c['sources']}\n"
             f"Last touched: {D}\n")
    with open(tf, "a", encoding="utf-8") as fh:
        fh.write(entry)
    print(f"wrote {c['id']} -> {TOPIC[c['id'][:2]]}")

# mark the 25 transcripts extracted
marked = 0
for k in F:
    p = F[k]
    t = open(p, encoding="utf-8").read()
    if "extracted: false" in t:
        open(p, "w", encoding="utf-8").write(t.replace("extracted: false", "extracted: true", 1))
        marked += 1
print(f"\nmarked extracted: {marked} of {len(F)}")
