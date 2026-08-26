"""One-off merge for the 2026-08-27 research pass. Appends verified claims to codex topic files."""
import io
from pathlib import Path

SCI = Path(r"E:\claude code marketing skill\Obsidian God-level Marketing Vault\God-level Marketing\wiki\science")

MD = r'''
### MD-139 · Creative enhancements RE-ARM themselves: any touch of the ad, including a PREVIEW, can switch them back on
Tier: T3 · Status: active
[[Meta Delivery & Andromeda#MD-128|MD-128]] established that Flex Media ships ON BY DEFAULT and closed with "nobody on our book has checked it". This claim is the reason one check is not enough.
Ben Heath, 2026-08-26, recording off-schedule and unedited while on holiday because his community was reporting it in real time: "Meta is getting more and more bold in its automatically turning on of the creative enhancements even if you as the advertiser turn them off."
**The trigger list is the finding, and the last item is the one nobody would guess.** "When you do anything to that ad, a lot of the creative enhancements will be turned back on automatically." Duplicating an ad does it, editing the primary text or headline does it, and so does merely looking: "If you preview an ad, I've seen this in a number of ad accounts where you just preview an ad, the creative enhancements can be turned on."
**Operating consequence, and it changes the task from an audit into a habit.** Enhancement state is not a setting you fix once. It has to be re-checked after every touch, by every person with access. Heath names the multi-operator failure mode from his own account: "Someone else has been here looking at it."
**COMPLIANCE, and this is why it lands harder on our book than on an ecommerce book. Four of our five accounts are chiropractic and sit under Meta's health rules.** Heath: "If you are in a complianceheavy industry where you cannot say certain things in your ads... you could end up running ads that are just quite frankly not allowed to be run." An auto-applied text overlay or AI image variation is generated AFTER our compliance review, so the ad that ran is not the ad that was approved. Image variation is called out as near-universal: "That happens basically every time you upload an image."
**GUARDS, and they are heavy. T3 and thin.** No screenshot of a toggle flipping, no before/after state capture, no count of affected ads, and no performance data with enhancements on against off. "I've seen this in a number of ad accounts" is the entire evidentiary basis. Heath also discloses a standing conflict in the same video: "Meta literally tell me about stuff before they're going to come out". That cuts both ways, it gives him early sight and it makes him a channel Meta chooses to brief.
**Source-honesty note worth stealing for our own gate.** He advances a theory about Meta's internal incentives distorting its own AI evaluations and then labels it himself: "I have no evidence that's occurring. I just know that occurs in large organizations." He also reports a Meta CMO answer verbatim rather than characterising it: "our AI lawyers are better at assessing whether something is compliant or not in these high-risisk industries than uh regular lawyers are." Neither side of that exchange carries data.
Sources: Ben Heath, We have a new Facebook Ads problem, 2026-08-26
Last touched: 2026-08-27

### MD-140 · Personalized destinations: a new creative enhancement that lets Meta send the click to a DIFFERENT page than the one in the ad
Tier: T3 for existence and behaviour · Status: active
The newest member of the enhancement family at [[Meta Delivery & Andromeda#MD-139|MD-139]], and the first that changes where the traffic goes rather than what the ad looks like. Ben Heath, 2026-08-26: "It's called personalized destinations." Behaviour: "Meta can decide to send them to any other location on your website that it thinks would likely convert better."
**Rollout state, stated as hearsay and dated.** "It's only in a few ad accounts right now." He expects it to reach many more accounts over the following months, sourced to "from what I hear", so treat the timeline as rumour and the existence as observed.
**Two consequences, and the measurement one is worse than the delivery one.**
First, it overrides a designed funnel. Heath's version of the objection: "we've planned the journey. So, we want them to watch this VSSL first. We want them to opt in for this lead magnet first."
Second, and this damages the codex's own instruments, it makes landing-page results unreadable: "it can become really hard for us advertisers to work out which element actually performed well. Like, did this landing page convert well? How can I tell? I don't really know where people are going." **Any landing-page test run in an account with this enabled is confounded, including the LP-versus-PDP test at [[Creative Science#CR-188|CR-188]].**
**Do not confuse it with the per-creative destination URL at [[Meta Delivery & Andromeda#MD-124|MD-124]].** That is the ADVERTISER assigning a different URL to each creative inside one ad object, confirmed independently by Jon Loomer on 2026-05-04: "You can customize the text and destination URL for each image or video." This is META reassigning the URL at delivery time. Same surface, opposite party in control.
**Guards.** No screenshot, no account named, no performance data in either direction, and no Meta documentation read. His recommendation is to turn it off outside pure ecommerce, hedged even there: "Even then, I'm not so sure."
Sources: Ben Heath, We have a new Facebook Ads problem, 2026-08-26
Last touched: 2026-08-27

### MD-141 · "Push delivery to this ad" is a native control that forces a set share of budget onto ONE existing ad for a set window
Tier: T1 for surface existence · Status: active
The most useful new control to reach this codex in weeks, because it is the reversible answer to the fight at law 3. Jon Loomer, 2026-05-04, reading it off the product: "Some advertisers will see an option to push delivery to this ad." Mechanics: "you can push delivery to a single existing ad for a designated amount of time."
**He is explicit that this is delivery, not measurement, and the distinction is the whole value.** "So this won't be a test. It would simply be making sure that Meta spends a certain percentage of the budget on a specific ad."
**Why it matters to law 3.** Eight operators have argued about whether killing the top spender craters the ad set, with zero controlled data on either side. Sam Piliero's best idea so far was to cap the hog's spend instead of pausing it. This is better again: it funds the starved ad WITHOUT touching the hog, which is the only move in the whole argument that adds a variable rather than removing one. It serves the starved-ad problem at [[Scaling Models#SC-009|SC-009]] directly, where the stated reason not to kill low spenders is that they are the ad set's reserve.
**It is also the native replacement for a structure Loomer attacks elsewhere.** On 2026-06-08 he takes apart the one-campaign-five-ad-sets-one-ad-each pattern whose motive is forcing delivery to each ad: "If you're optimizing for purchases, you're splitting up your budget five ways to test ads. You'll already struggle to get meaningful data". Push delivery reaches the same goal without the fragmentation. **Any codex entry citing him on this needs both quotes or it reads as a contradiction.**
**Guards.** Staged rollout, so absence in an account says nothing. No percentage default is stated, no duration range is stated, and nobody has shown performance data with it on. Availability across our five accounts is unchecked.
Sources: Jon Loomer, Dont Get Attached to Your Ad Process, 2026-05-04; Jon Loomer, Every Change You Make Should Solve a Problem, 2026-06-08
Last touched: 2026-08-27

### MD-142 · Meta shipped an official Ads MCP endpoint; it creates campaigns PAUSED only, caps at 10 accounts, and cannot see creative
Tier: T2 for surface and constraints, read on screen · Status: active
Sam Piliero, 2026-05-18, connecting it live: "Name this Facebook Ads MCP, and then paste in https://mcp.facebook.com/ads." Scope as of May 2026: "Right now, the main use case is reporting, editing, and creation."
**Three hard constraints, all read off the product, and the first bounds what this codex can ever get out of it.** It is blind to creative: "This means Claude can't see your copy, it can't see your videos, it can't see your images." So it can count and compare ads and it cannot judge one. Every creative claim in this codex still needs a human or a separate pipeline.
Second, a genuine safeguard: "It can only launch campaigns in the paused state, which I think is a great safeguard." Third, a per-user ceiling: "we have 10 MCP enabled accounts", against hundreds attached to the business. Latency is seconds: "in just about 3 seconds, the name Claude is now appended to the campaign."
**His warning is the part to keep, and it is aimed at exactly the failure mode this engine keeps catching.** An LLM reading an ad account "is going to make recommendations only on numbers, not thinking holistically", with no inventory, COGS or margin context, so: "be super careful with the recommendations that you actually pull out of here, especially when they're broad."
**Attribution guard, because this number will get misattributed.** The 0.5x ROAS / 7-day ad-level kill sweep demonstrated in this video is PILIERO'S, offered as the pattern operators will reach for, and he disclaims it on camera. It is not a Charley T rule and it is not a codex rule. See [[Scaling Models#SC-137|SC-137]] for what happened the last time a round kill number travelled without its source.
Sources: Sam Piliero, Claude Has Officially Changed Facebook Ads Forever Tutorial, 2026-05-18
Last touched: 2026-08-27

### MD-143 · Andromeda removed the practitioner's ability to separate warm from cold on Meta, which is why exclusions became the only lever
Tier: T3 · Status: active
Independent corroboration for laws 1a and 1b from a fourth operator, and it supplies the WHY that those claims state only as a WHAT. Blue Sense with a Google specialist, 2025-09-10: "with the Andromeda update inside of Facebook, that's becoming a bigger and bigger problem because people realize that they can't really segment out warm users from cold users", and "it's very hard now in meta to to kind of work inside of audiences because of the Andromeda update".
**This is the mechanism behind the exclusions-over-inclusions rule at [[Meta Delivery & Andromeda#MD-123|MD-123]].** If audience-level control is gone, exclusion is the only remaining boundary, which is what three operators independently concluded from the other direction.
**A frequency claim rides along and it must NOT be promoted.** He says Meta caps individual-ad frequency near 2 on cold: "they'll rarely ever let an account have an individual ad go above a two frequency on cold audiences", attributing it to a Meta disclosure he never names or links. That is hearsay about a platform claim. It agrees with [[Meta Delivery & Andromeda#MD-138|MD-138]]'s ad-level two-impression ceiling from the SAME operator, which makes it his settled position and still not documentation. **Two unsourced statements of the same number by the same person is one source, not two.**
**He also claims a private channel as his basis: "they're just a group inside of Meta that work with the top 20 high spend accounts".** Unverifiable, and it is the kind of provenance claim that makes an assertion feel documented when it is not.
Sources: Blue Sense Digital, Cold vs Warm Tactics on Meta Google Ads with Caden, 2025-09-10
Last touched: 2026-08-27

### MD-144 · The claim that Meta scans your LANDING PAGE as a targeting input, and goes "one level deep", is stated flatly and sourced to nothing
Tier: T4 · Status: active
Banked as a GUARD, in the shape of [[Creative Science#CR-183|CR-183]], because it is the next round number waiting to be invented and because the test it is attached to is real.
Nick Theriot, 2026-08-26, explaining a genuine landing-page result: "we know that Facebook scans your product page, like whatever page you're sending people to." He describes ad and destination being read together into a targeting profile: "It takes all of the images and visuals and your video, the sounds, everything. And then it also takes everything on your PDP and it puts together this idea of who you're trying to target." Then the specific, quantified part: "Well, Facebook only goes one level deep, so it looks at this and then it looks at this."
**What is wrong with it: the "we know" carries no document, no Meta statement, and no test isolating the mechanism.** Crawl depth is a precise architectural claim about a system nobody outside Meta can see. The strongest T1 we hold, the GEM post at [[Meta Delivery & Andromeda#MD-120|MD-120]], enumerates the model's inputs as "user location, ad creative representation" and says nothing about a destination page at any depth. This claim sits outside the documented feature set entirely.
**Separate the result from the explanation, because the result is good and the explanation is free.** His LP-versus-PDP test is real and is banked at [[Creative Science#CR-188|CR-188]]. A landing page can beat a product page for reasons that require no crawling at all: better message match, an explicit qualification frame, and fewer exits. **The finding does not depend on the mechanism, and the mechanism has nothing behind it.**
**The pre-emptive rule, same as CR-183: any future note that assigns a crawl depth, a scan frequency or a weighting to Meta's treatment of destination pages invented it.** Three retractions in this codex came from exactly this shape, a real observation wearing a fabricated mechanism.
Sources: Nick Theriot, How To Lower Facebook Ads CPA in 2026 4 Things I Fix First, 2026-08-26
Last touched: 2026-08-27

### MD-145 · Meta's under-18 inventory contracts sharply in 52 US jurisdictions, and the settlement contains NO advertising provision
Tier: T1 · Status: active
Meta newsroom, 2026-08-26, announcing an agreement with "a bipartisan group of 52 attorneys general across US states, territories, and the District of Columbia". Pending judicial approval the controls apply automatically to under-18s on Instagram and Facebook, and "The majority of the terms are required to remain in place for 10 years."
The supply-side items: a default two-hour daily limit cumulative across both apps, a default block from midnight to 6am, notifications muted 8am to 3pm, usage prompts every 15 minutes, and an option for teens to "choose a non-algorithmic feed".
**Banked mainly so a future run does not misread it.** The words "advertis", "ad targeting", "monetiz" and "advertiser" appear ZERO times in either the agreement post or the accompanying open letter. This is a youth-safety settlement with a second-order inventory effect, not an ads-policy change. A future reader seeing "Meta settles with 52 AGs" and inferring new ad-targeting restrictions would be inventing them.
**Consequence for our book: none.** All five clients are local service businesses advertising to adults, and our ad sets carry an 18+ minimum age. The real effect is a contraction of teen impression supply plus a slice of teen sessions leaving the ranked feed, which touches advertisers who buy under-18 reach. We do not.
Sources: Meta Newsroom, Our Agreement With US State Attorneys General, 2026-08-26; Meta Newsroom, An Open Letter to TikTok and YouTube, 2026-08-26
Last touched: 2026-08-27
'''

CR = r'''
### CR-188 · Theriot deliberately runs three NEAR-IDENTICAL creatives in one ad set at $6M/30-day scale, which is the anti-collapse pole law 2 lost yesterday
Tier: T3 · Status: active
[[Meta Delivery & Andromeda#MD-003|MD-003]] lost its anti-collapse witness on 2026-08-26 when Blue Sense turned out to hold both positions five days apart. This is the replacement, and it is better sourced than the one it replaces, because it is a standing practice rather than an opinion.
Nick Theriot, 2026-08-26, opening on scale: "Over the last 30 days, we spent over $6 million on ads at my ad agency, specifically for our clients."
**His standard testing unit is three creatives per ad set that differ in exactly one element.** Images: "The three images are going to have the same text hook, just a different background on each of those images." Videos, and this is as near-duplicate as it gets: "this is the same exact video three times, all have the same body, same length, same everything, but the visual hook is different."
**Why this is evidence.** If Meta bundled near-duplicates into one entity with zero unique reach, this practice would be self-defeating, and it is not a stray test, it is how every ad set in the book is built. That is an operational bet placed with $6,000,000 over 30 days against the collapse thesis. Note the boundary it respects: the varied element is the VISUAL in both cases, which is consistent with the scope already recorded at MD-003, where the rebuttal is limited to swaps that change the visual.
**What has NOT changed, and this is the ninth month of it.** He shows no entity ID, no similarity score and no unique-reach figure, exactly like everyone else on both sides. **The evidentiary hole is unchanged; only the roster of the anti-collapse side changed.**
**A second Theriot practice cuts the other way and belongs in the same entry.** He also expands by swapping the person: "we'll test different ethnicities of people uh with our winning messaging and our winning creative to be able to appeal to more people, so we can spend more and scale", and reports finding a winner "by creating the exact same ad but a female version". That corroborates [[Meta Delivery & Andromeda#MD-001|MD-001]]'s avatar mechanism from a third operator. **NO NUMBER GIVEN for either the female version or the bag-avatar win.**
Sources: Nick Theriot, How To Lower Facebook Ads CPA in 2026 4 Things I Fix First, 2026-08-26
Last touched: 2026-08-27

### CR-189 · A landing page beat a product page by roughly $20 CPA, and the operator states the winning number two incompatible ways
Tier: T2 for the test, with an arithmetic conflict attached · Status: active
Banked with the failure attached rather than smoothed, per the check added 2026-08-26.
Nick Theriot ran the clean version of this test, one ad launched twice against the same audience with only the destination changed: "we launched this ad twice, one with a PDP and one with a landing page."
**Statement one, mid-video:** "the landing page spent 10 times more compared to the PDP with a nearly $20, $22 cheaper cost per purchase compared to um, the PDP itself with an $85 cost per purchase." That puts the PDP at $85 and the landing page at roughly $63 to $65.
**Statement two, in his own recap minutes later:** "spent 10 times more with a $20 cost per purchase." That puts the landing page at $20.
**These cannot both be true. $20 CHEAPER than $85 is $65, not $20.** The recap understates the landing page's cost by roughly 3x. A third statement, "we lowered cost per acquisition by $20 by doing this", agrees with statement one, so the weight of his own testimony favours $65 and the recap is the error. **Quote the delta, never the level: a roughly $20 improvement on an $85 baseline is what this test supports.**
Supporting components he reports moving the right way: cheaper cost per link click and better CPMs, with "CVR roughly stayed the same but the traffic was cheaper."
**Scope guards.** One ad, one client, one product, no date range, no spend figure, no significance test, and the 10x spend difference means the two arms were never equally funded. His explanation for WHY it worked is a separate and unsupported claim, quarantined at [[Meta Delivery & Andromeda#MD-144|MD-144]]. **A future run must not merge the two: the result is T2 and the mechanism is T4.**
Sources: Nick Theriot, How To Lower Facebook Ads CPA in 2026 4 Things I Fix First, 2026-08-26
Last touched: 2026-08-27

### CR-190 · The Ads Library now sorts by IMPRESSIONS and shows inactive ads, which repairs the broken "long-running equals winner" heuristic
Tier: T1, read off the product · Status: active
The cheapest competitor-research upgrade in the codex, and it comes with a correction to a rule this codex has repeated.
Ben Heath, 2026-04-14, walking the Library. Two capabilities that did not previously exist: "That is the ability to sort by impressions high to low", and "you can look at inactive ads as well as active ads. That's not something you used to be able to do", reached via "Just make sure in filters, you've got active status as active and inactive."
**The correction.** The old rule was runtime: "And if an ad has been active for more than 6 months a year, it probably is a best performer." He keeps it and breaks it in the same breath, because zombie ads sit active on zero spend, a problem he attributes to delivery changes: "a problem that was getting worse given how Meta Ads delivery system has updated". **The repaired signal is the intersection, not either alone:** "lots of impressions plus um been running for a long time is as close to a guarantee".
**A load-bearing filter note that will cause misreads if missed.** The Library's location filter is where the ad is DELIVERED, not where the advertiser sits: "the location you set is not where you are, or even where the competitor is based." Every geo-scoped competitor pull we run depends on that.
The detail panel also exposes the exact run window and the variation count under one ad entry, e.g. "We can see there's the three variations of this ad that was run", which is a free read on the ad-object-versus-creative-asset counting problem at [[Meta Delivery & Andromeda#MD-124|MD-124]].
Sources: Ben Heath, How To Spy On Your Competitors Meta Ads for FREE, 2026-04-14
Last touched: 2026-08-27

### CR-191 · Creative production budget as a share of media spend: 10%+ above $100k/mo, 25% at $30k/mo, and the worked model's numbers are self-declared FAKE
Tier: T3 for the allocation bands, T4 for the model · Status: active
Blue Sense, 2025-10-14, on a real starved account: "We have an ad account right now that's spending 300K per month on Meta."
**The bands, stated as anecdote and labelled as such by him:** "those that allocate about 10% or more of their budget to creative production end up seeing really good results", explicitly "based on anecdotal experience from the clients that we've worked with". The share must rise as spend falls: "When you're spending only 30k a month, you really want to be looking at something like 25% allocated to production costs." Below $5k a month there is no external budget at all and "the founder needs to be involved in content creation".
**Read the bands against our own book before using them. Every client we run sits under $30k a month, so the 25% end applies, not the 10% end.**
**The critical guard, and he supplies it himself on the record: every figure in the worked model is invented.** "I'm going to start making up numbers, so I'm not actually giving away the real numbers of this business." **So the $50 CPA, the $20K reallocation and the 6,000-conversion baseline are illustrative and must never be quoted as an account result.**
**The arithmetic inside the fake model is nonetheless correct, which is worth stating because it is the rarer outcome in this corpus.** $300K at $50 CPA is 6,000 conversions; moving $20K to production leaves $280K, which must beat 6,000 conversions, requiring a CPA at or under $46.67. His sweep lands exactly there, rejecting $48 and $47 and accepting $46, and his stated threshold "we need to see a drop in CPA by at least $4" is the correct conservative rounding.
**What is NOT in the file: any outcome.** The reallocation is a forecast, stated as a certainty it has not earned, "we will guaranteed to get at least a $4 drop in CPA by doing this over a 60-day time period". **NO OUTCOME NUMBER GIVEN.** Production rate at $20K/month is given as "about 60 new video assets per month", which computes to $333 per video.
Sources: Blue Sense Digital, Heres How Much You Should Be Spending On Creative, 2025-10-14
Last touched: 2026-08-27

### CR-192 · Consolidating 36 ads into 6 is reported with no performance number at all
Tier: T3 · Status: active
A no-number guard, banked because the ad-count debate at law 4a keeps acquiring figures that were never measured.
Jon Loomer, 2026-05-04, using the new multimedia workflow: "I took what was previously 36 ads and consolidated it into six." **NO PERFORMANCE NUMBER GIVEN.** No CPA, no ROAS, no delivery change, no before and after of any kind. The entire justification is structural: "These new six ads are truly diverse, and I eliminated the repetition that Meta discourages."
**He then states the neutrality rule that his own episode argues against:** "Now, fewer ads isn't necessarily better, just as more ads isn't necessarily worse." The reconciliation he implies is that the variable is creative DIVERSITY and the count is a side effect. **Anyone citing 36-to-6 as evidence that consolidation improves results is citing a structural preference as a result.**
Note the mechanical cause of the 6x collapse: the workflow at [[Meta Delivery & Andromeda#MD-124|MD-124]] holds up to 10 assets in one ad object, so 36 assets fit in 6 objects with no creative removed. **The asset count did not fall. Only the object count fell.** This is the counting trap at MD-124 happening in the wild, in a published note, by a careful operator.
Sources: Jon Loomer, Dont Get Attached to Your Ad Process, 2026-05-04
Last touched: 2026-08-27
'''

SC = r'''
### SC-146 · Ben Heath, the 20-plus-ads advocate, concedes only ONE TO THREE ads ever get the spend
Tier: T3 · Status: active
This dissolves most of law 4a's 10x spread, and it does it the same way the 2026-08-23 vocabulary pass did: by getting the highest-count advocate to state what he means.
Ben Heath, 2026-04-14, in an unrelated video about competitor research: "you put 5, 10, 15, 20 different ads within one ad set. Only one, two, or three of those ads get all the spend."
**Why this matters more than another operator's number.** Heath is the source of the 20-plus figure that anchors the top of law 4a's range. He is not retracting it. He is saying it describes ads LOADED, and that ads FUNDED is one to three regardless. **Loaded and funded are different quantities, which is the same confusion that produced the live-versus-launched split already recorded at [[Creative Science#CR-154|CR-154]].**
**It reconciles him with [[Meta Delivery & Andromeda#MD-137|MD-137]] almost exactly.** MD-137 has Blue Sense at roughly one funded ad on a $20-30k account and about 20 on a $200k-plus account. Heath's one-to-three sits inside that, and the two operators who looked furthest apart on ad count turn out to agree on the only number that spends money. **The surviving disagreement is narrow: how many ads to LOAD so that the funded one to three are the best available, and nobody has tested that.**
**Operating consequence for our book, and it is the same one MD-137 gives.** Every client sits under $30k a month, so creative volume buys succession and optionality for when the winner fatigues, not concurrent tests. **Read this, MD-137 and law 4d together before setting any creative quota.**
**Guards.** Said in passing, in a video about the Ads Library, with no account open and no data. He gives no spend level, so it is unclear whether one-to-three is universal or a small-account effect. He also supplies the mechanism as inference, not measurement: a weak ad loses impressions to its siblings, so "Meta would stop giving those impressions and they would uh serve the other ads within the ad sets instead."
Sources: Ben Heath, How To Spy On Your Competitors Meta Ads for FREE, 2026-04-14
Last touched: 2026-08-27

### SC-147 · Theriot runs 90+ ad sets inside ONE CBO with testing and scaling in the same campaign, and STILL never states a live count
Tier: T3 · Status: active
Law 4a has recorded across five transcripts that Nick Theriot never states a concurrency figure anywhere. He now states a container figure, which narrows the gap without closing it.
**The structure, at $6M over 30 days.** One CBO per business objective, with no separate testing campaign: "all of them are pretty much rocking the same simplified ad account structure with one CBO campaign per business objective", and "When we have new ads, we drop them into that CBO campaign." Campaigns split by COUNTRY or by product CATEGORY, never by variant: T-shirts and pants get separate campaigns, red and blue T-shirts do not.
**The number, and the caveat he attaches in the very next sentence.** "we have over 90 different ad sets in this particular campaign." Then: "Not all of them alive." Each ad set holds three creatives.
**So the honest read is that we now have a CONTAINER count of 90+ ad sets and 3 creatives each, and still no LIVE count, because he immediately disclaims that all of them are live.** Anyone converting this into "Theriot runs 270 live ads" is inventing the live rate. The gap recorded at law 4a narrows and survives.
**He also kills ad sets on cost per acquisition, which is NOT how this codex has recorded him.** "We are turning the ones off that are technically not producing a good cost per acquisition and hurting overall performance." Law 3 lists him among the leave-on voices on the strength of [[Scaling Models#SC-099|SC-099]], where a CBO improved with two concurrent top spenders and no kill.
**⚠ One sentence in this transcript appears to say he killed the HIGHEST SPENDER, and it is genuinely ambiguous. Do not resolve it in either direction.** Verbatim: "Like this one right here has a $131 cost per purchase, which is technically worse than our highest spending one right here, which actually we did turn off and, you know, start putting spend to this one right here." The second "which" can attach to the $131 ad set or to "our highest spending one". Grammatically it attaches to the nearer noun, which is the top spender. Contextually the $131 ad set is the one being criticised. **This is exactly the shape that produced three retractions in this codex, so it is banked as ambiguous and it changes nothing at law 3 until somebody watches the screen.**
His creative-testing throughput, and the arithmetic checks out: numbering starts at 100 and reads 180, giving "we've tested 80 concepts in this account since working with this client, and that comes out to roughly 240 creatives we've tested." 80 x 3 = 240, and 180 - 100 = 80. Both correct.
Sources: Nick Theriot, How To Lower Facebook Ads CPA in 2026 4 Things I Fix First, 2026-08-26
Last touched: 2026-08-27

### SC-148 · The 20%-daily-kill-cap retraction is confirmed across SIXTEEN Charley T transcripts, and his stated figures fail internal arithmetic about half the time
Tier: T2 for the arithmetic audit, T3 for the absence · Status: active
Two findings about the same source, and the second is the one that should change how this codex weights him.
**First, the retraction is settled and should never be revisited.** Three more Charley T transcripts were read in full on 2026-08-27, bringing the total to sixteen. The string "20%" appears four times, all in one file, and **all four are affiliate-commission arithmetic**: "you get 20% of the $147 every month", "you get in that case 20% for nearly a year", "because you get 20%. Which five of that equals 100% of what you pay." Zero occurrences in the other two files. **Across sixteen transcripts he has never once quantified a kill threshold in any form.** See [[Scaling Models#SC-137|SC-137]].
**Second, and this is new: his numbers do not survive being checked against each other.** Five failures in a single 2026-01-26 file, all in his own community's figures rather than ad figures, which is the scope limit on this finding.
The worst is a customer lifetime stated three mutually incompatible ways in one passage. He says "our stickiness is 88%. Meaning we have 12% turn in this community", then "somebody will stick around for about 10 to 11 months". **At 12% monthly churn the average lifetime is 1/0.12 = 8.3 months, not 10 to 11.** He then says "the average revenue per user was $92 in December and the LTV was $593". **$593/$92 = 6.4 months.** Three lifetimes, 10-11 stated, 8.3 implied by churn, 6.4 implied by LTV, in one paragraph.
Also failing: a Loom-review value given as "over $15,000" that recomputes to $7,800 at his own stated $1,300/hour and 30 minutes a month, off by roughly 2x; and a per-referral figure of "well over $300" that computes to $294 to $323 on his own lifetime range, missing at the bottom.
**What this licenses and what it does not.** It does NOT refute any advertising claim of his, and none of the failures are ad-account numbers. It does mean that **a Charley T figure quoted without its components has roughly even odds of not reconciling**, which is precisely how the invented numbers at [[Scaling Models#SC-136|SC-136]], SC-137 and [[Learning & Signal#LS-067|LS-067]] entered this codex under his name. **Recompute before banking, every time.**
He also contradicts himself on Q5's end date across two files, "through New Year's" versus "till about the second week of January, roughly around the 10th", and on where the year's CPM trough sits.
Sources: Charley T, Academy News 6 Q1 Reality Check, 2026-01-26; Charley T, Meta MBA Just Opened Q5 Goldmine, 2025-12-28; Charley T, Q1 Strategy Blueprint, 2026-01-06
Last touched: 2026-08-27

### SC-149 · Placement pruning is rational or pointless depending ENTIRELY on the optimisation event
Tier: T3 · Status: active
The cleanest resolution in this codex of an argument that is usually had without stating the condition that decides it. Jon Loomer, 2026-06-08.
**Under conversion optimisation, delivery self-corrects and manual placement removal solves nothing.** "If your customers aren't on Instagram, meta will limit your spend there." The Audience Network case is the same argument at its strongest: "If audience network is just bots, and you might be right, meta knows that you can't get conversions there." His conclusion: "when you're optimizing for conversions, there aren't placements that are known to be sources for low quality conversions".
**Under upper-funnel goals the logic inverts, because the goal is cheaply satisfiable by junk inventory.** "If you're optimizing for through play views, it matters if your customers aren't on Instagram." Thruplay, link clicks and landing-page views all qualify.
**The governing sentence: "The performance goal matters a whole lot when assessing whether there's a problem to be solved."**
**A second ordering rule from the same file, and it generalises past placements.** Where a restriction is genuinely warranted, bid down before excluding: "even then, prioritize using value rules first before removing a placement entirely", and on age: "But instead of restricting by age entirely, I'd use a value rule to bid less on that group instead." **That connects to the value-rules surface at [[Meta Delivery & Andromeda#MD-100|MD-100]] and gives it its first stated operating doctrine: value rules are the soft version of every hard exclusion in law 1a.**
**The qualifying test for any restriction, which is the useful half:** "If this finding is based on meaningful data, then you have information that Meta doesn't", with the bar set at lifetime value rather than first-purchase behaviour. Most age and gender restrictions fail it: "You're not even giving Meta a chance to find customers outside of your expected range."
**Guards.** No data on either side, no account. He also names the cost of over-splitting without measuring it: "The new problem is a combination of audience fragmentation, auction overlap, and a general watering down of your budget."
Sources: Jon Loomer, Every Change You Make Should Solve a Problem, 2026-06-08
Last touched: 2026-08-27
'''

def append(fname, text):
    p = SCI / fname
    with io.open(p, 'a', encoding='utf-8') as f:
        f.write(text)
    print("appended ->", fname)

append('Meta Delivery & Andromeda.md', MD)
append('Creative Science.md', CR)
append('Scaling Models.md', SC)
