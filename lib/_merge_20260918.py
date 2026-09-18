# -*- coding: utf-8 -*-
"""Advertising Science merge, 2026-09-18.

Sources actually read in full today:
  * matt-shiver/2026-09-17 "YouTube Ads Playbook for Coaches in 2026" (49 min, 12,377 words)
  * Meta for Business, "IAB Global Creator Week...", 2026-09-15
  * Meta for Business, "Introducing Meta One plans for businesses", 2026-09-15
"""
import io
import os
import re

SCI = os.path.join("Obsidian God-level Marketing Vault", "God-level Marketing",
                   "wiki", "science")
TODAY = "2026-09-18"


def read(name):
    with io.open(os.path.join(SCI, name), encoding="utf-8") as f:
        return f.read()


def write(name, text):
    with io.open(os.path.join(SCI, name), "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def insert_in_section(text, section, block):
    """Insert block at the END of the named '## section', before the next '## '."""
    m = re.search(r"^## " + re.escape(section) + r"\s*$", text, re.M)
    if not m:
        raise SystemExit("section not found: " + section)
    nxt = re.search(r"^## ", text[m.end():], re.M)
    at = len(text) if not nxt else m.end() + nxt.start()
    return text[:at].rstrip("\n") + "\n\n" + block.strip("\n") + "\n\n" + text[at:]


def append_eof(text, block):
    return text.rstrip("\n") + "\n\n" + block.strip("\n") + "\n"


def amend(text, claim_id, block):
    """Append a paragraph inside an existing claim, before its Sources line."""
    m = re.search(r"^### " + re.escape(claim_id) + r" ", text, re.M)
    if not m:
        raise SystemExit("claim not found: " + claim_id)
    tail = text[m.end():]
    s = re.search(r"^Sources: ", tail, re.M)
    if not s:
        raise SystemExit("no Sources line for " + claim_id)
    at = m.end() + s.start()
    out = text[:at].rstrip("\n") + "\n\n" + block.strip("\n") + "\n\n" + text[at:]
    m2 = re.search(r"^### " + re.escape(claim_id) + r" ", out, re.M)
    seg_end = re.search(r"^### ", out[m2.end():], re.M)
    seg_stop = len(out) if not seg_end else m2.end() + seg_end.start()
    seg = out[m2.end():seg_stop]
    seg = re.sub(r"^Last touched: .*$", "Last touched: " + TODAY, seg,
                 count=1, flags=re.M)
    return out[:m2.end()] + seg + out[seg_stop:]


SRC_MS = ("Sources: Dr. Matt Shiver, YouTube Ads Playbook for Coaches in 2026, "
          "2026-09-17, read in full 2026-09-18")
LT = "Last touched: " + TODAY

# ---------------------------------------------------------------- GOOGLE

GA074 = u"""### GA-074 · YouTube's two back-to-back targeting changes removed keyword and channel placement, moved buying into Demand Gen, and an operator who sells the transition says the result is a higher scale ceiling
Tier: T3 · Status: active
**What the operator says changed, in order.** First, content targeting went away: you could previously put an ad in front of a specific keyword's viewers or a specific channel's audience, and that instrument was withdrawn in favour of audience-based targeting. Second, YouTube buying was folded into Demand Gen, which serves in-stream ads, Shorts ads, in-feed ads in search results and suggested videos, and video inventory on partner surfaces off YouTube. He says Google handled the handover badly, and that advertisers who moved without changing their method saw worse initial results and concluded the channel had broken.

**The instruments he names in place of content targeting.** Custom intent audiences built from what people search on Google, YouTube and Google Maps, served to that person the next time they open YouTube inside a recency window. URL affinity, which targets people who visit a named website, his examples being a competitor site or a category site. A top-10% household income layer stacked on either. His worked target for a nutrition offer is people searching how to count calories, layered with the income bracket.

**The claim that matters and the reason he gives for it.** Before the change he describes YouTube as a "highly highly profitable lowspend platform" where he could beat an advertiser's Meta results and then hit a ceiling on how far the campaign would go. He attributes that ceiling to targeting what someone is watching right now, and says audience targeting lifted it by targeting who the person is and what they searched recently. **No spend figure, no CPA and no before-and-after is attached to the ceiling claim.**

**His scaling shape, which is the transferable half.** He frames YouTube as closer to traditional media buying than Meta: find the keyword or audience that works, buy more of it, measure where diminishing returns start, hold it there and launch another campaign. His image is a forest of campaigns grown from many seeds, against a balloon inflated until it pops. On Meta he characterises the same operation as handing the system every magazine and every channel at once and asking it to find the buyers, which scales impressively and leaves the operator with no account of where the next pocket came from.

**A caution he volunteers, and it applies directly to every account we run.** Performance Max is the wrong container for lead generation, because it bundles Demand Gen with Shopping, Search and Display and leaves less direct control over targeting and therefore over lead quality. He says it is skewed to e-commerce. Demand Gen is where he puts lead-gen budget.

**This runs opposite to the only measured Demand Gen evidence in this codex, and neither side resolves the other.** [[Google Auction & Smart Bidding#GA-055|GA-055]], [[Google Auction & Smart Bidding#GA-056|GA-056]] and [[Attribution & Incrementality#AT-072|AT-072]] are one 21-day geo holdout that found no statistically relevant new-customer lift from Demand Gen, with the whole measured lift landing on returning customers. That test was a single e-commerce advertiser. This claim comes from a lead-gen coaching and consulting operator describing a different objective, a different funnel and a different conversion event, so the two are not a like-for-like contradiction. **What is true of both: he shows no holdout, and the holdout tested no lead-gen account.**

**Commercial interest, recorded because he states it himself.** His value proposition during the transition was helping advertisers move over, sold as training and as done-for-you. A claim that the change was good for advertisers is also a claim that his product was worth buying.

**One figure inside this, carried as an unverified recollection.** He puts YouTube Premium penetration under 10% of users, "between like you know seven and 9%" in the United States and lower elsewhere, then immediately says "I don't have the exact stats right now". Do not repeat those numbers as data. His argument around them does not depend on them: an advertiser pays nothing to fail to reach an unreachable user, so Premium removes reach rather than adding cost, and ad-supported tiers are growing on YouTube, Netflix and Amazon rather than shrinking.
""" + SRC_MS + u"""
""" + LT + u"""
"""

GA075 = u"""### GA-075 · An operator running YouTube lead gen prefers a target CPA cap over maximize conversions specifically BECAUSE Google throttles spend when it cannot hit the target
Tier: T3 · Status: active
**The setup.** On Demand Gen and YouTube you pay on impressions and bid on a conversion. The available strategies are the four already banked at [[Google Auction & Smart Bidding#GA-001|GA-001]]. His preference is target CPA over maximize conversions or maximize conversion value, and he applies it even when the target is set well above what he expects to pay, because the point is having a ceiling rather than hitting a specific number.

**His stated reason, and it inverts the usual complaint.** "Google actually will limit the spend on your campaign if it doesn't think it can achieve the CPA, which is actually good because it means that like I'm getting okay, I'm going to get like a average cost per conversion within the range of that CPA." Most operators treat a throttled campaign as the price of running a cap. He treats the throttle as the product. His trade preference follows from it: a higher budget with a CPA cap over a lower budget with no cap.

**Where this is stronger than Google's own documentation.** [[Google Auction & Smart Bidding#GA-003|GA-003]] is T1 from Google's help centre and says target CPA holds the AVERAGE cost per conversion at target, with individual conversions allowed to cost more or less, judged over at least 30 days and 30 conversions. His "within a percentage range" is a tighter promise than Google makes, and he does not say over what window he reads it. Where the two conflict, the documentation wins.

**The cost he never quantifies.** A campaign Google declines to spend on is a campaign delivering no volume, and he gives no figure for how often a capped campaign under-delivers, by how much, or what that costs against the same budget run uncapped. He also never separates a cap that throttles from a cap set so low the campaign never leaves the gate. **Nothing was shown on screen: no account, no CPA, no spend, no comparison against maximize conversions.** It is an operating preference from real spend, which is what T3 means, and it is cheap to A/B on one of our own Google accounts.
""" + SRC_MS + u"""
""" + LT + u"""
"""

# ---------------------------------------------------------------- CREATIVE

CR248 = u"""### CR-248 · An operator puts YouTube creative refresh at quarterly under $1,000 a day against weekly on Meta, and attributes the roughly 13x gap to intent targeting replenishing its own audience
Tier: T3 · Status: active
**The numbers as given.** On YouTube, an account spending under $1,000 a day can refresh creative quarterly. Accounts spending heavily move to monthly or bi-weekly. He says he tells Meta operators the quarterly figure and they call it insane. The interviewer, who runs Meta, confirms his own cadence on camera as "literally every week new".

**The mechanism he claims for the gap.** YouTube's targeting is built on intent, so the audience replenishes itself: new people type the search term every day and the pool refills underneath a campaign that has not changed. Meta's targeting resolves to a pocket of people, and that pocket exhausts. He does not claim YouTube creative never fatigues, and he supplies his own counter-example unprompted: his PDF ad ran for years, decayed, and has recently recovered, which he puts down to fatiguing his own audience rather than the format dying.

**This agrees with the codex on mechanism and disagrees only on where each platform sits.** Ben Heath's claim already on file is that accounts over $100k a month fatigue within days, that the driver is audience size against spend rather than creative quality, and that "better ads will last longer" is false. If exhaustion of a finite pocket is the driver, a platform whose audience refills by construction should carry creative longer, which is exactly the shape of this claim. **So the two are consistent, and this one is unmeasured where Heath's is also unmeasured.**

**Guards, and they are not small.** No data, no account, no fatigue curve, one operator. He sells YouTube training and done-for-you YouTube management, and a lower cost of creative ownership is a selling point for that product. The $1,000-a-day threshold is stated without derivation. The comparison against Meta is his characterisation of somebody else's platform.

**What it does NOT license for our own book.** Every account we run on Meta stays on its current weekly to fortnightly cadence; nothing here touches that. The claim is useful only as a cost estimate for a YouTube test: it says the creative bill for sustaining a YouTube campaign is a fraction of the Meta bill, which changes what a test costs to keep alive rather than what it is likely to return.
""" + SRC_MS + u"""
""" + LT + u"""
"""

CR249 = u"""### CR-249 · The closest thing on file to an AI-versus-non-AI creative comparison: three arms, all-AI worst, AI-hook-then-real-footage best, and the operator says the ranking has since reversed as AI stopped being novel
Tier: T3 · Status: active
**Why this claim exists.** [[Creative Science#CR-169|CR-169]] holds that nobody in this codex's AI-creative sources has compared AI creative against non-AI creative in the same account, and that every stated advantage is therefore a production-cost claim. This is the first source read into the codex that describes running that comparison. **It still does not close CR-169**, for the reasons listed at the bottom, and CR-169 stays open.

**The three arms, in his words.** Ads with no AI. Ads that are entirely AI. Ads with an AI-generated hook in the first 8 seconds followed by conventional footage for the rest.

**The result he reports for the period roughly six months before recording.** All-AI was the worst. The hybrid outperformed everything. No-AI sat in the middle. His stated reason the all-AI arm lost: it fails to build know, like and trust, because the viewer cannot work out who the brand is.

**The reversal he reports as current, and it is the more useful half.** No-AI ads are performing better again and the hybrid's edge has decayed. He attributes this to AI video no longer being novel, and says the bar has moved: an AI video now has to be a better AI video to earn the same result. His forward position is that the pendulum keeps swinging, so the finding has a short shelf life by his own account.

**The hybrid hooks he names, and what they have in common.** Every one puts HIM inside a stylised world rather than replacing him: walking a medieval street as "king of YouTube" over a line about living in medieval times, a revenue roller coaster, a Pixar style, a Lego character, an anime character, an astronaut. His read on why a SET of them works is persona-shaped rather than novelty-shaped: each style captures the slice of the audience that likes that style, which he compares explicitly to varying backgrounds and characters on Meta so the system can find who responds. That is the logic of [[Creative Science#CR-212|CR-212]] on the founder face as a sameness signal, applied to style instead of scene.

**The enrolment anecdote is not evidence and he does not present it as any.** A client told him on a group call that he enrolled because he saw the Lego ad and loves Lego. One person self-reporting a reason for a purchase is the weakest attribution there is, and it is told as a joke against himself.

**Why CR-169 stays open.** No cost per result, no spend, no impressions, no window, no sample size. The arms were not held constant beyond the AI variable, and he does not say whether the offer, the funnel or the targeting moved. The whole account is recalled from memory about a period he places around six months earlier, and he separately says in the same conversation that he has not personally checked his own funnel stats in about a year. **File as a directional recollection, not as a test.**

**The one part cheap enough to act on now.** The hybrid structure does not require committing to synthetic creative. An AI-generated first 8 seconds bolted onto otherwise conventional footage is a hook swap in the sense of [[Creative Science#CR-124|CR-124]], which we already run, so it costs one asset per concept to try, and it is the matched-pair test CR-169 asks for.
""" + SRC_MS + u"""
""" + LT + u"""
"""

CR250 = u"""### CR-250 · Putting a non-founder spokesperson in the ad is gated on SPEND: below roughly $100k a month it costs the founder's credibility and buys nothing, and the working build hands to the founder at 30 seconds
Tier: T3 · Status: active
**The rule as a spend gate.** "If you're spending less than 100 grand a month, definitely like less than 30, like you really shouldn't do that." He calls it an advanced strategy that makes sense at a certain level of scale, and the gate is the scale rather than the creative brief.

**Three reasons he gives, and the third is the one nobody says out loud.** One, you lose the branding value of positioning the founder as the expert, which for an expert-led business is part of what the ad spend buys. Two, not everyone articulates the offer as well as the founder does, so a spokesperson is a range of outcomes and some of them are worse. Three, an early-stage company has no company credibility for a new face to borrow, so an unknown presenter fronting an unknown founder opens two credibility gaps where there was one. His phrasing: "who is this other person? But then also, who are you? What's your track record?"

**The inverse case, and why it works there.** At scale the ad is building the company brand rather than the founder's, the company already has a track record the presenter can stand on, and the new face reaches a group the founder's face was not reaching. He cites a competitor with a large team and a long client list as someone for whom it works for exactly that reason.

**His worked build, which is the transferable part.** The spokesperson opens and carries the hook. At about 30 seconds she hands over explicitly ("let me introduce you to...") and the founder speaks to camera. The founder hands back, and she takes the call to action. The stated purpose of the handoff is to get the founder's face into an ad fronted by somebody else, so the ad reaches the new audience without giving up the positioning. **They then tested the landing page both ways, founder alone and both faces, and kept both faces.** Production detail he volunteers: they rented an Airbnb for the backdrop rather than shooting in the usual room.

**The hook in that ad, for the record.** A time claim plus a company result: ten minutes to learn the strategy, tied to $200 million generated for clients. He notes the hook outlived the spokesperson and that he has since delivered the same hook himself.

**Guards.** No CPA, no spend on those specific ads, and no comparison against the founder-only version of the same ad. The $30k and $100k thresholds are asserted with no derivation. The campaign is a recollection from several years earlier, during a period he describes as hyper-scaling with a peak month around $400k of ad spend, and he says the account no longer runs at that level. The interviewer offers a contradicting data point from his own account, where a female employee's ads "didn't do the best", and neither side is measured.

**Where it sits against what we already hold.** [[Creative Science#CR-212|CR-212]] says persona is the hardest thing to vary in a founder-led format, because the founder's age and sex are fixed, and recommends varying scene and format first because they are cheap. This claim is the expensive way through the same wall, and its contribution is naming the spend level at which it becomes available at all. Our own standing rule that a creator never speaks the call to action is not in conflict: here the spokesperson is the brand's own employee rather than a creator, and the CTA is hers by design.
""" + SRC_MS + u"""
""" + LT + u"""
"""

# ---------------------------------------------------------------- MATH

MM218 = u"""### MM-218 · The "Trojan horse PDF" funnel: a downloadable PDF opts in at a higher rate than a free training video, and the email is deliberately delayed 8 minutes so people watch the video while they wait
Tier: T3 · Status: active
**The build, step by step as described.** The ad shows the physical PDF held on camera while the presenter talks through what is inside it, and the call to action is to download it. The click goes to an opt-in page that captures contact details. The thank-you page then says the PDF is on its way to the email inbox and offers "now watch the video version of the PDF while you wait". The video leads into booking a call.

**The deliberate mechanic, and he names it as deliberate.** The PDF email is held back 8 minutes on purpose, and the page pre-frames the wait with a line saying it can take 5 to 10 minutes. "We tested this. That makes them more likely to watch the video." His own reaction on camera is "I feel bad", followed by the reasoning that a viewer who starts the video is in, while a viewer who gets the PDF first skims it and files it for later.

**Why the PDF beats the video as the thing in the gate.** People opt in for a PDF at a higher rate than for a training video, which he puts down to the PDF being a thing they do not want to miss out on rather than a commitment of time.

**The numbers he gives, and the sentence that qualifies all of them.** About 60% of opt-ins watched the video, with a view-rate curve he describes as matching what they saw when people signed up for a VSL directly, and a materially lower cost per opt-in. **Immediately after giving the 60% he says "I have to check the stats now. I haven't checked in like a year."** Nothing was on screen. The interviewer's corroborating figure is about the thing being replaced rather than the replacement: he abandoned the VSL opt-in step entirely because it reached $100-plus per opt-in on a specific avatar.

**The sales-floor half, which is the part most people who copy this funnel leave behind.** The outbound call to an opt-in who has not booked opens "I just wanted to make sure you got our PDF, I know sometimes it goes to spam" instead of "have you watched our video". A service frame rather than a sales frame, and the caller is asking about a deliverable the prospect actually requested. Both parties on the call agree that is the meaningful difference.

**His current configuration, for scale.** A 30-minute VSL he rewrites annually plus a 19-page PDF on the coaching offer, and a separate 5-to-7-minute direct-offer funnel for the done-for-you offer, on the stated ground that done-for-you buyers do not want the 30 minutes and want track record and differentiation instead.

**Where it sits against what we hold.** [[Marketing Math & Unit Economics#MM-161|MM-161]] already carries page-level rates for the three call-funnel shapes and says nothing about which bribe belongs in the gate. This claim answers that and says nothing about booking rates, so the two stack rather than conflict. He also reports the format decayed for years and has recently recovered, which he attributes to fatiguing his own audience rather than to the format dying, consistent with [[Creative Science#CR-248|CR-248]].

**Our own position on the 8-minute delay, recorded so nobody repeats it blind.** The email really does arrive, so the line is not a false claim. It is still a manufactured wait presented in language that reads as a technical limitation. Before any version of "this can take 5 to 10 minutes" goes into our copy, say out loud that the delay is a choice, and check it against the client's own tolerance for that.
""" + SRC_MS + u"""
""" + LT + u"""
"""

MM219 = u"""### MM-219 · Booking-source mix on a working B2B coaching and done-for-you funnel: roughly 50 to 60% direct and retargeting, 30 to 40% appointment setters, under 10% email
Tier: T3 · Status: active
**The split, with his own hedge attached.** Asked where bookings come from, he gives "ballpark numbers" and says he does not have them separated: a little more than half books directly through the marketing funnel, with retargeting lumped into that same bucket, roughly 30 to 40% comes from appointment setters dialling, and email is "less than 10%".

**The email collapse has a stated cause and a stated date.** He attributes it to Gmail's promotions-tab change roughly two years earlier, after which list performance dropped. The workaround was a weekly value-first newsletter ending in a call booking, which worked for a period and then decayed, which he attributes to newsletter saturation across the category while conceding "or maybe that's just mine" because he has run his for a long time.

**Why it is worth banking despite being ballpark.** A coaching and agency offer with a funnel this operator has spent years tuning still gets a third or more of its booked calls from humans on the phone. **Any forecast for this offer type that assumes the funnel books everything is wrong by 30 to 40% of bookings.** That is a staffing line in a P&L rather than a marketing detail, and it belongs beside any proposal we write for an offer of this shape.

**Guards.** One account. Figures given as ballpark and never reconciled to 100%. Direct and retargeting are not separated, which matters because retargeting bookings are created by spend counted elsewhere. No CRM was shown. The email figure is a share of bookings and says nothing about the profitability of the list.
""" + SRC_MS + u"""
""" + LT + u"""
"""

# ---------------------------------------------------------------- META

MD159 = u"""### MD-159 · Meta's 15 September creator release: Creator Marketing Hub global, three APIs expanded, Partnership Ads coming to the Meta Ads MCP connector, and Instagram Live video ads generally available from 29 September 2026
Tier: T1 · Status: active
Meta's own Business News post is the source for every product and date here, announced at the IAB's first Global Creator Week.

**Meta Creator Marketing Hub expands globally from 15 September**, with the named features rolling out across the rest of 2026: discovery filters that surface creators and content featuring your products, including a filter for known and predicted affiliate content; content-level permissions with expiry dates; one-click Partnership Ad creation inside the Hub; content recommendations that suggest an ad objective such as sales or awareness; ad-readiness editing that strips common blockers like copyrighted music and stickers; and Partnership Messaging moved inside the Hub so discovery, outreach and activation happen in one tool.

**Three API changes.** Facebook creators join Instagram creators in the Creator Marketplace API, so both are reachable through a single integration. A new Messaging API enables creator outreach, with what Meta calls built-in protections for creators. The Content Discovery API expands to carry recommendations on top-performing organic creator content, advanced filters, keyword search, organic insights and a flag for which content is ready to run as an ad.

**Two agent-facing changes, and the second is the one to watch.** The Meta AI business assistant is being integrated into the Hub for creator search and workflow guidance. And **Partnership Ads are coming to the Meta Ads MCP connector**, so an advertiser can create Partnership Ads and manage creator permissions from an external agent. No date is given for either.

**One dated launch, and it is the only hard date in the post.** Live video ads already run on Facebook and are **expanding to Instagram, reaching general availability beginning 29 September 2026**, available to all advertisers and agencies. Paired with Partnership Ads, a creator's live content can be amplified as a Partnership Ad.

**The two figures and exactly what stands behind them.** Creator recommendations influence 45% of all consumer purchases, and creator-economy ad spend has reached $37 billion, growing 4x faster than media overall. Both are footnoted to the 2025 IAB Creator Economy Report and Meta Modern Shopper Research Q4 2025. **No methodology, no population and no definition of "influence" is given, and one of the two cited sources is Meta's own research.** Quote them as industry figures with that attribution or not at all.

**The vendor line with nothing behind it.** Meta writes that Partnership Ads "have become one of the strongest-performing formats", with no comparison, no metric and no population. That is an assertion in a launch post, and it does not upgrade [[Creative Science#CR-058|CR-058]], which already holds the creator-versus-brand-produced performance claim from practitioner sources.

**Not one performance figure is attached to any of the launches.** T1 covers what the products are, which surfaces they touch and the 29 September date, on the [[Meta Delivery & Andromeda#MD-099|MD-099]] precedent of T1-for-existence-and-surface-only. Nothing here measures anything.

**What is actionable for our own book, honestly scoped.** We run no creator partnerships on any account today, so the Hub and the creator APIs are not actionable. Two things are worth carrying forward. The 29 September Instagram Live video ads date, because it is a new placement arriving on a platform we already buy. And the MCP connector line, because a Meta buying surface reachable from an external agent is the first one our own tooling could drive directly, and it is worth knowing it exists before somebody asks for it.

**It also turns an observation into a shipped product.** The codex already records, from one attendee at Meta's 2026 Performance Marketing Summit, that Meta said little about mass-generating AI creative and pushed creators and partnership ads hard instead. This release is Meta spending engineering on the second half of that, which is corroboration by roadmap rather than by statement.
Sources: Meta for Business, "IAB Global Creator Week: Making it Easier for Businesses to Partner with Creators and Turn Discovery into Purchase", 2026-09-15, read in full 2026-09-18
""" + LT + u"""
"""

# ---------------------------------------------------------------- amendments

AM_MD157 = u"""**Amended 2026-09-18 from Meta's BUSINESS-facing version of the same announcement, which carries three things the newsroom post does not.**

**One, the pricing unit, and it is the material addition.** The business post states "(pricing per asset)" and then, plainly: **"Plans are priced per profile, so each plan covers one account."** The newsroom post does not say this. It changes the arithmetic for anyone running more than one profile, and it is the fact that explains the $45-a-month figure flagged above: a per-profile price means a business covering Instagram, Facebook and WhatsApp is not buying one subscription, which is how that operator arrived at a number Meta never published. **Still do not repeat the $45.** Quote the per-profile rule instead and send the client to their own subscription flow.

**Two, Meta Verified is being folded in.** "We're bringing the best of Meta Verified into Meta One." Current Meta Verified subscribers are explicitly unchanged for now, with migration plans in progress and a notification promised when they can switch. So Meta Verified sits on a deprecation path rather than running alongside, and any client already paying for it should expect a migration prompt.

**Three, Meta Business Agent is metered by tier.** It is free to start, and a Meta One plan on WhatsApp buys more Business Agent responses per month. It answers customer messages on WhatsApp Business on the business's behalf, with the operator able to take over a conversation and to train it. Worth knowing because it is Meta's own text-answering agent sitting in the same job our voice agent does, and because the limit is a response count rather than a feature flag.

**The feature list confirms the closing line above rather than changing it.** Competitive Insights on Instagram comparing up to 10 public accounts on public metrics, extended insights history beyond 90 days with CSV export, Custom Audience Insights on Facebook covering people who engage but do not follow, content scheduling up to a year ahead for reels and posts and 30 days for stories, links in organic posts and reels, an Instagram link page holding up to 20 links, a bold follow button, verified WhatsApp channels and a custom WhatsApp web URL. **Every one of those is organic, profile or support tooling. Nothing in Meta One touches ad delivery, ad cost or ad ranking.**
Sources (added 2026-09-18): Meta for Business, "Introducing Meta One plans for businesses", 2026-09-15, read in full 2026-09-18"""

AM_CR169 = u"""**Amended 2026-09-18. The gap is still open, and the closest attempt on file is now recorded at [[Creative Science#CR-249|CR-249]].** A YouTube lead-gen operator describes running exactly the comparison this claim says nobody runs: three arms, no AI, all AI, and an AI hook in the first 8 seconds followed by conventional footage. He reports all-AI worst, the hybrid best at the time, and the ranking since reversing as AI stopped being novel.

**Read why that does not close this claim, because the reasons are the ones this claim exists for.** No cost per result, no spend, no window, no sample size, arms not held constant beyond the AI variable, and the whole account recalled from memory about a period roughly six months before recording. It is a direction rather than a measurement. **The rule in this claim is unchanged: any AI-creative claim we repeat is labelled a production-cost claim until somebody shows the comparison with numbers.**

**What it does improve is the test design this claim asks for.** The hybrid arm is the cheap version: an AI-generated first 8 seconds on otherwise conventional footage is a hook swap, which our accounts already produce on cadence, so the matched pair costs one extra asset per concept instead of a parallel production line."""

AM_MM161 = u"""**Amended 2026-09-18.** These three rates say nothing about WHICH lead magnet belongs in the opt-in gate. [[Marketing Math & Unit Economics#MM-218|MM-218]] answers that from a different operator: a downloadable PDF opts in at a higher rate than a free training video, and the video is then placed on the thank-you page behind a deliberate 8-minute delay on the PDF email. That claim carries no booking rate, so it stacks onto this one rather than competing with it."""


def main():
    n = "Google Auction & Smart Bidding.md"
    t = read(n)
    t = insert_in_section(t, "Channel Fit: Where Google Belongs and When YouTube Pays", GA074)
    t = insert_in_section(t, "Smart Bidding Mechanics", GA075)
    write(n, t)

    n = "Creative Science.md"
    t = read(n)
    t = insert_in_section(t, "Creative volume and fatigue", CR248)
    t = insert_in_section(t, "Creator, UGC and AI creative", CR249)
    t = insert_in_section(t, "Creator, UGC and AI creative", CR250)
    t = amend(t, "CR-169", AM_CR169)
    write(n, t)

    n = "Marketing Math & Unit Economics.md"
    t = read(n)
    t = insert_in_section(t, "Lead-Gen Funnel Rates", MM218)
    t = insert_in_section(t, "Lead-Gen Funnel Rates", MM219)
    t = amend(t, "MM-161", AM_MM161)
    write(n, t)

    n = "Meta Delivery & Andromeda.md"
    t = read(n)
    t = append_eof(t, MD159)
    t = amend(t, "MD-157", AM_MD157)
    write(n, t)

    print("merged: GA-074 GA-075 CR-248 CR-249 CR-250 MM-218 MM-219 MD-159 "
          "| amended: CR-169 MM-161 MD-157")


if __name__ == "__main__":
    main()
