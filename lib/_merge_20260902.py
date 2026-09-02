# -*- coding: utf-8 -*-
"""Claim merge for the 2026-09-02 research pass.

Five new transcripts (Blue Sense founder-ad masterclass, Ben Heath campaign
setup, Matt Shiver coaching P&L, Nick Theriot $1M campaign teardown, Solutions 8
keyword count) plus two arXiv cs.IR papers that passed the advertising filter.
"""
import sys
sys.stdout.reconfigure(encoding="utf-8")
import merge_helper
merge_helper.TODAY = "2026-09-02"   # stamp for this pass
from merge_helper import amend, mint, audit

CR = "Creative Science.md"
SC = "Scaling Models.md"
MM = "Marketing Math & Unit Economics.md"
LS = "Learning & Signal.md"
MD = "Meta Delivery & Andromeda.md"
AU = "Auction Mechanics & Bidding.md"
GA = "Google Auction & Smart Bidding.md"

BS = "Blue Sense Digital, How To Create Founder Ads That Scale (Masterclass), 2026-09-01"
BH = "Ben Heath, Use this Facebook Ads set up you'll thank me later, 2026-09-01"
NT = "Nick Theriot, Inside a $1,000,000 Facebook Ads Campaign, 2026-08-31"
MS = "Dr. Matt Shiver, The Harsh Truth About $100k+/mo Coaching Businesses, 2026-09-01"
S8 = "Solutions 8, Are You Using Too Many Keywords in Google Ads, 2026-09-01"

print("== Creative Science ==")

mint(CR, "CR-212",
     "The founder's face is the strongest sameness signal an account can carry, and the cheapest fix is the SHOOTING LOCATION rather than a new script",
     "T3", "active",
     """The problem stated plainly by an operator who is on pace to spend $400 million on Meta this year. Founder ads work, so the account makes more of them, and then "your face as the founder is the strongest sameness signal in the account. So, past a point, more founder videos just all look the same to the end consumer, which limits the diversity." A talking-head founder in the same chair fatigues fast because the face, the scene and the framing are constant across every asset.
**The intervention, and it is the cheapest one on file for this problem.** Same script, same edit, same B-roll, shot in the gym and then shot outdoors at the front of the gym. "That change alone has allowed us to take a fatigued ad of the person in the gym, and then continue to pump another $40,000 of spend through it just by changing the scene." He states it holds under Andromeda: reshooting the same script is fine "as long as there is enough variation in either the editing, so the editing is very different, or the scenes in which it's getting shot is very different."
**Ordering that matters, because it tells you what to try first.** He splits the fix into format variation and concept diversification, and calls format variation the easy half and concept diversification the hard half. Concept means persona, angle or offer. **Offer is the easiest to vary** because the founder can tell a new story about a different product. **Angle is hard** because a brand usually has exactly one unique mechanism. **Persona is hardest of all in this format specifically**, because a large part of what makes a persona resonate is who is on screen, and the founder's own age and sex are fixed. His worked example of beating that constraint without lying: a 30-year-old male creatine founder re-angles the same true story through his mother refusing chalky powder, which opens an older-women persona and a flavour-line offer at the same time.
**Escalation ladder as volume grows:** move around the location, then travel to a genuinely new set, then change format entirely (tier-list video, founder walking a shop aisle handling competitor products) rather than staying in talking head.
**Guards.** The $40,000 is a single unnamed account with no before-and-after screen, no CPA and no date. Nothing was shown on camera. The claim is a mechanism plus one anecdote, so it is a cheap thing to try and never a measured result. Read it against [[Creative Science#CR-124|CR-124]] on hook swaps and MD-003 on near-duplicate collapse, because "change the scene" and "change the hook" are competing answers to the same delivery question and nobody has run them against each other.""",
     [BS])

mint(CR, "CR-213",
     "The founder's INVOLVEMENT is a five-rung ladder (face, voice, evidence, proxy, absent), which buys format diversity on one script and one concept",
     "T4", "active",
     """A taxonomy rather than a finding, banked because it turns "the founder will not go on camera" from a blocker into a menu, and because it generates format variation without touching the script.
1. **Face.** Founder on camera speaking. The top of the pyramid and the ideal.
2. **Voice.** Founder narrates over B-roll, animation or a creator's footage. No face required, useful when the founder is uncomfortable on camera.
3. **Evidence.** Founder appears as proof rather than as a presenter: photographs in the lab, certificates, a shot walking through the factory facing away from camera. He concedes this is "starting to stretch away from this being a true founder ad."
4. **Proxy.** An employee, a credentialed expert such as a dietitian, or the supplier tells the founder's story. Stated as less effective than the founder telling it.
5. **Absent.** No face, voice, evidence or proxy, and the founder's journey is told end to end anyway. His named vehicle is animation or AI-generated animation, with the argument that animation can show the mechanism viscerally in a way live action cannot: "you could go into the cells and show how the cells changed as a product of the unique mechanism."
**Why it is worth the file space.** Rungs 2 to 5 use the same script and the same concept as rung 1, so they are format diversification at close to zero incremental scripting cost, which is exactly the lever [[Creative Science#CR-212|CR-212]] says to pull first. It is also the answer to the founder-availability constraint at eight and nine figures, where the scarce input is the founder's hours rather than the idea.
**Nothing here is measured.** No rung is compared against another, no spend is attached to any of them, and the ordering by effectiveness is his judgement. Treat the ladder as a production checklist and the ranking as an opinion.""",
     [BS])

mint(CR, "CR-214",
     "The founder's ROLE inside the script is a testable variable: protagonist, witness, interviewer, reader; about 99% of founder ads use only the first",
     "T3", "active",
     """The second diversification device from the same masterclass, and it moves the script rather than the shoot.
- **Protagonist**, first person, "I built this". He puts this at roughly 99% of all founder ads.
- **Witness**, first person about someone else: "a customer emailed me last week and they said this."
- **Interviewer**, the founder asks and someone else answers: "I asked our lab, why?" The answerer can be the lab, the manufacturing team, or the buyer who made a decision in the customer's favour.
- **Reader**, the founder reads a document aloud: "I just got a one-star review, let me read it out for you."
**The scoping rule he attaches is the operationally useful part.** Role swapping is high leverage for a six or seven-figure business that will not pay creators and is making everything itself. It is lower priority at eight to ten figures, where founder time is the scarce input and the non-protagonist roles can be handed to someone who is not the founder without losing much, because the authority is carried by the document or the interviewee rather than by the founder's own claim.
**Ties to the renewable-variable split in [[Creative Science#CR-217|CR-217]]:** witness and reader roles run on inbound material (reviews, support emails) that regenerates weekly, which is what makes them repeatable where the protagonist origin story is used up after one telling.
**Asserted. No performance comparison between roles, no account, nothing shown.** The 99% is a figure of speech, not a count.""",
     [BS])

mint(CR, "CR-215",
     "The founder-ad script structure ranked highest across $400M of managed spend: adversarial CLAIM, immediate PROOF of the claim, unique mechanism, founder-story proof, then CTA with offer, scarcity and social proof",
     "T3", "active",
     """**Read the method before the finding, because the method is what raises this above a preference and it is also where the limits are.** He states he pulled, through the Meta MCP, every founder ad reachable from his business manager across the $400 million he is on pace to spend this year, had the model watch the videos via screenshots rather than read titles, pulled the scripts, ranked them on total spend and performance over time, then distilled the common structures. The structure below is the one that recurred in **the top 15 founder ads** by that ranking.
**The structure.**
1. **A claim, and normally an adversarial one.** His example shape: "The big supermarkets are trying to sell you this, but it actually is full of plastic." The claim doubles as the hook, which he names as one reason the structure performs.
2. **Immediate proof of the claim.** This is the load-bearing step and it comes with the pass's clearest negative finding: **"we've never seen a founder ad script within all the ads that I pulled, none of them performed well when they just had a claim."** A large claim with nothing behind it failed every time in the set. His worked version on creatine gummies: assert that competitors' gummies contain almost no creatine, then cite the study showing they carry a hundredth of the stated dose.
3. **The unique mechanism**, tied into the founder story. The adversarial claim supplies the reason the founder went and built something different.
4. **More proof, delivered as founder story.** Flew to the factory, commissioned third-party testing, here is the ingredients label. This is the step where the founder's presence is doing work that a third party could not do as cheaply.
5. **CTA, offer, scarcity and urgency, then customer social proof** to close.
**Guards, and they are real.** n is 15 ads. No spend figure, ROAS or ranking score is published for any of them. No losing structure is shown for comparison, so the negative finding in step 2 is his recall of the set rather than a tabulated result. The corpus is his own agency's business manager, so it is his own house style being measured as much as the market. And the model-assisted ranking pipeline is described but not audited. **Treat it as the best-sourced founder-ad script structure currently on file and still as one agency's read of its own ads.**
**Where it agrees with what we already hold.** Steps 1 to 3 are the same shape as the adversarial "us versus them" comparison format in [[Creative Science#CR-054|CR-054]], and step 5's position at the end is consistent with [[Creative Science#CR-127|CR-127]] on holding the product back. The same session says he does not bother testing CTA variants at all, because average watch time means almost nobody reaches the CTA.""",
     [BS])

mint(CR, "CR-216",
     "Nobody cares about the founder: a founder ad converts when the viewer recognises their OWN story in it, so the story has to be told through the viewer's eyes",
     "T3", "active",
     """He flags this himself as "arguably the most important one to two minutes in the whole video", and it is the correction to every founder ad that is really a founder biography.
**The statement.** "Nobody cares about the founder. At the end of the day, everyone has a story... Just a founder talking about their story is meaningless to most people." Founder ads that only tell the founder's story sometimes work and mostly do not.
**The mechanism he gives.** The viewer watches because of familiarity, not interest in the founder. His example: makeup causing acne. "They're not watching it because they care about you or care about your story... Instead, they're watching it because they have familiarity. They go, 'Oh, this is me. This is the story that I have had to deal with.'" The sequence that follows is problem agitation to hold the watch, a curiosity gap opened on the fact that the founder solved it, the mechanism walked through, and the gap closed at the end.
**Selection consequence, and it is the practical one.** The founder story worth telling is the one a large number of buyers have also lived. A true origin story that nobody else shares is a bad ad even though it is a good story, which is a different selection rule from "tell your story authentically".
**This is why [[Creative Science#CR-212|CR-212]]'s persona problem bites.** If the ad converts on recognition, the founder's demographics bound who can recognise themselves, which is exactly why persona is the hardest concept variable to move in this format.
Asserted as a principle across a 60-minute masterclass, no split test, no account. It is consistent with the desire-transfer rule already in this file, which says to channel an existing desire rather than to educate a market into one.""",
     [BS])

mint(CR, "CR-217",
     "The founder story is FINITE: separate the static variables (origin, personal problem) from the renewable ones (reviews, support inbox, supplier calls, complaints) and run a collection system to feed them",
     "T3", "active",
     """The structural reason founder ads run dry, and the pipeline answer to it.
**Static, and they must stay consistent or credibility goes.** The origin of the problem, why the company was started, the founder's own personal problem, and the co-founders' story of why they came together. "There's probably only one story. It needs to stay consistent over time, or you lose credibility." A two-founder brand gets three static stories rather than one, which is the only way listed to widen this bucket honestly.
**Renewable, and they regenerate weekly.** Customer reviews, and one-star reviews specifically ("you will continue to get one-star reviews if you're big enough"). The support inbox. Supplier calls and supplier interviews, which renew because the product keeps being iterated and because suppliers themselves change. Day-to-day conversations about the business. In-person complaints ("the product's too expensive", "I don't like this new flavour").
**The system, and this is the part to actually build.** Because the founder shoots once a month or once a quarter rather than daily, the raw material has to be accumulated between shoots: reviews piling into a database, the support inbox piped into a model for a weekly pull of anything usable, supplier communications recorded and noted, one-star reviews and complaints captured as they happen. The stated throughput target this feeds is **40 founder ads a month** as one part of a wider content mix, produced as a pipeline rather than scripted and shot one at a time.
**The ethics line he draws, and it has a commercial reason attached.** Asked directly whether to invent a founder story, his answer is that it is black hat, and the business reason he gives is exit value rather than morality: fabricated static variables are the ones that cannot survive diligence.
**Why it matters to a small account.** This is the cheapest content-supply system in the file. It needs no creators, no shoot budget and no agency, and the inputs are things a business already generates and throws away.
Asserted from agency practice. No production-rate data, no account, and the 40 a month is a target he sets rather than a measured output.""",
     [BS])

mint(CR, "CR-218",
     "Low-fi footage does not damage a premium product's positioning provided the PRODUCT IS NOT ON SCREEN during the low-fi segment; it builds contrast instead of association",
     "T4", "active",
     """The answer to the standing objection that scrappy creative cheapens a premium brand, and it is a rule about sequencing rather than about quality.
Reading a live electric-toothbrush ad that front-loads low-fi footage of competitor brushes and holds its own product back for the first 40 seconds before switching to high-end shots: "People think that you can impact branding by having obviously low-fi content in the creative mix, but as long as the product's not being introduced in that content at the same time, then you're not building associations. In fact, you're actually building contrast because you're contrasting all of the shots, all of the product right now with the low-quality shots at the start."
**The operating rule.** Associations attach to what is on screen with the product. Low-fi footage of the problem, of competitor products, or of the founder's search costs nothing in brand terms as long as the hero product does not appear in it. The moment the product enters the frame, the production value of that frame is the brand statement.
**Why we care.** It removes the forced choice between a scroll-stopping low-fi opener and a premium-looking asset, and it makes the two compatible inside one ad. It is also the mechanism that makes the product-held-back structure in [[Creative Science#CR-127|CR-127]] safe for brands that were refusing it on brand-safety grounds.
**T4 and it stays T4.** This is one operator reading someone else's ad on screen, with no brand-lift measurement, no account and no test of the opposite construction. It is a plausible rule, cheap to follow, and unproven. It sits next to [[Creative Science#CR-100|CR-100]], which argues from the other direction that polished campaign-shoot assets only perform on pre-existing brand equity.""",
     [BS])

mint(CR, "CR-219",
     "Four production rules for founder ads, and the reason most brands conclude 'founder ads do not work for us' is the founder's first ten hours on camera",
     "T3", "active",
     """Craft rules from the same masterclass, banked together because each one is a named failure mode with a named fix.
1. **Never ship a raw talking head.** "You can't just have a founder talking to camera... Unless they're famous and people want to watch them talk, they won't work." Required: fast dynamic editing, overlays, real cuts, ideally two cameras and some motion. The asset has to clear the bar of a piece of organic content someone would actually watch.
2. **Hook variants must bridge into the body.** The common failure is hooks shot for the sake of a variant count that then cut into a body with nothing to do with them: the founder opens with "back 10 years ago, this happened to me" and the body never picks it up. He names this as a big issue across founder talking-head ads specifically.
3. **If the founder is bad on a teleprompter, give them the sentence-by-sentence structure and let them go off script.** The diagnosis is the valuable half: **"if you haven't spoken for tens of hours on camera before, it's very unnatural in the first 10 hours of talking."** The founder reads robotically, the ads fail, and the brand concludes the format does not work for them when what failed was the first attempt at being on camera. That reframes a category of write-offs as a skill curve.
4. **Move constantly during the shoot.** If you have the founder for one hour, do not shoot it all in one spot. This is the production-side statement of [[Creative Science#CR-212|CR-212]].
**Shoot economics stated alongside, and read the ratio carefully.** He puts 10 hooks against 3 bodies at 30 ads, and 60 with two CTA variants, from "about 4 minutes to 5 minutes of the camera recording". That is camera time only. His own framing is that "99% of the performance, 99% of the work, actually comes from the scripting, the copywriting, the ideation", so the cheap number is the shoot and the expensive one is everything before it. He reports clients producing 200 to 400 ads a month with content teams of one or two people, and a one to two hour founder shoot yielding three to four months of assets. Every figure here is asserted, none is shown, and the 99% is rhetorical.""",
     [BS])

amend(CR, "CR-124",
      """**THE SAME OPERATOR NOW PUBLISHES A CAP, 2026-09-01, and it collides with the 15-hooks-per-body arithmetic above.** Asked how many hooks per body, Blue Sense answers "generally, what that ends up coming out to is between like two to four. And you could go up if you want to like eight different hooks", and gives a delivery reason rather than a production reason: **"if you're going to like 10, 20, 30 different hook variations, you are just going to spread your testing budget super thin."** His worked version is $1,000 a day landing across 3 ads instead of across 20 to 40, where the thinner spread is "not really optimal for the machine to be able to learn and get out of learning phase, exit, get conversions, get data." He also states his own range has been much wider in practice: one body with 40 hook variations in one account, nine in another.
**The reconciliation, and it is ours rather than his, because he never addresses the conflict.** The 15-hooks and 50-hooks material in this claim is about REVIVING an asset that already earned scale, where the budget is already committed and the audience is already exposed. The 2-to-4 cap is about LAUNCH, where a fixed test budget has to reach statistical usefulness on each variant. Read that way the two positions are answering different questions and both can hold. Read as a single rule they cannot, so never quote "2 bodies x 15 hooks beats 5 bodies x 2 hooks" and the 2-to-4 sweet spot in the same breath without saying which stage each belongs to.
He restates in the same session that hook variations still work under Andromeda and that reshooting the hook is the easiest way to extend a high performer, so the cap is about test economics rather than about delivery collapse.""",
      [BS])

amend(CR, "CR-127",
      """**A SECOND, DIFFERENT AWARENESS SPLIT from the same shop, 2026-09-01, and the disagreement is about where stage three sits.** Grading a founder ad that opens straight into product benefits, Blue Sense states the allocation as: "you want to be placing most of them in stage one, two, and three, and then have 20% of your ads in stage four and five." The headline 80/20 matches the split above. The BOUNDARY does not. The earlier version puts solution aware (stage three) inside the small 10% band with product aware; this one puts solution aware inside the large band with unaware and problem aware. On a real production plan that moves a whole stage's worth of creative, so treat 80/20 as the converged number and the placement of stage three as unsettled between two statements from the same source.
**The worked negative that produced it is the useful part.** The graded ad opens with the founder's oil under her makeup and testimonial photos, which he calls a good bottom-of-funnel asset and a bad one to put a quarter of a million dollars behind in a cold top-of-funnel campaign, because it addresses no problem and offers no education. He applies the same diagnosis to the whole Blueprint (Bryan Johnson) ad library: every ad sits at stage four or five, leans entirely on an existing personal brand, and opens on taste and cost-per-pill objection handling, which are closing arguments rather than reasons for a cold viewer to care. **His conclusion is an account-level one worth carrying: a library with no stage one-to-three inventory cannot scale on cold traffic no matter how good the individual ads are.** Named brand, read off the public ad library, with no account access and no spend data, so it is an inference from library composition.""",
      [BS])

amend(CR, "CR-058",
      """**A FOUNDER-SPECIFIC EFFECT SIZE, 2026-09-01, and it is bounded on both ends.** Running a founder ad as a partnership ad through the founder's personal handle rather than through the company page: "I can say from firsthand experience that this always performs better. I've actually almost never seen running ads through the company page perform better than the equivalent on a partnership ad, particularly on the founder." He then caps it himself: **"when I say better, I'm not talking about like 10x better. Like you're not leaving millions of dollars on the table. We're talking about between 5% to 30% better performance."**
**The condition is what makes it actionable.** The size of the lift tracks how much relevant content the personal page actually carries. His own case sits at the top of the band because the company page is nearly empty while his personal Instagram posts every two hours. A founder page with no relevant content gets close to nothing, and he says those brands should stay on the company page: "I'm not saying like photos of you at the park with your dog, I mean photos that are relevant to the founder store."
**The cost he names against it** is brand association: running through the person builds equity in the person rather than in the brand and creates a dependency where "people are buying you instead", which is the same exposure recorded at [[Scaling Models#SC-051|SC-051]]. His default recommendation for most brands is still the company page.
5% to 30% is a stated range from agency experience with no split test, no account and nothing shown, so it is a prior for sizing a test rather than a result.""",
      [BS])

print("== Scaling Models ==")

mint(SC, "SC-154",
     "Shown case against the CBO-plus-minimum-spend objection: one CBO, 180 ad sets accumulated one idea at a time, $25/day ad-set floors, scaled $100/day to $5,000/day over 365 days at a $50 cost per purchase",
     "T3", "active",
     """A full-year account walkthrough read off Ads Manager, and it matters most because it runs the exact structure [[Scaling Models#SC-133|SC-133]] reports as underperforming.
**The account.** Oral care e-commerce, $97 average order value, USA and Canada in one campaign because the ads and the site are shared. **$1.3 million spent in one campaign over 365 days, roughly 26,000 purchases, $50 average cost per purchase, scaled from about $100/day to $5,000/day.** Ad spend across all channels adds about $800,000; Triple Whale puts the brand at $4.6 million for the year at a 2.17 blended return, about $800,000 of profit on a 17% net margin, $53 new-customer acquisition cost.
**Arithmetic gate: every stated figure recomputes.** $1.3M / 26,000 = $50.00 exactly. 26,000 x $97 = $2,522,000 against the $2.6 million he states from ads, 3% apart. $2.6M / $1.3M = 2.0, matching his stated 2x in-platform return. $4.6M / ($1.3M + $0.8M) = 2.19 against his stated 2.17. 17% of $4.6M = $782,000 against "roughly 800k". The 20% budget ladder he narrates ($5,000 to $6,000 to $7,200 to "like $8,600", actual $8,640) also holds.
**The structure.** One CBO, highest volume, no cost or bid caps, 7-day click and 1-day view, Advantage+ targeting, 21+ only because younger ages kept getting the ads rejected. **One ad IDEA per ad set, about three ads inside it**, more when the creator shot extra hooks, and he explicitly refuses to split a fourth ad into its own ad set. Ad sets are never consolidated, they accumulate: he started with one or two and finished the year at 180, and **he names a 200 ad-set-per-campaign cap** which he expects to hit within weeks, at which point he opens a second campaign rather than restructuring the first. Top of funnel, middle and bottom all sit in the same campaign on Advantage+ and Meta decides who sees which.
**The minimum-spend floor, and this is the direct collision.** "We do do a small minimum spend on each ad set. I do $25 a day." At $5,000/day that is 0.5% of campaign budget per ad set. He scales the floor with the budget: "if I was spending $100 a day, I'd probably only put $5 a day just to nudge ads forward." **[[Scaling Models#SC-133|SC-133]] records the same construction as performing worse than plain ABO, from an operator who says he cannot explain why. This account is the counter-case and it is the larger and longer of the two.** Neither side shows a controlled comparison, so SC-133 is now contested rather than superseded.
**Why the floor is the interesting part for our book.** [[Scaling Models#SC-058|SC-058]] and our own accounts record CBO starving new creative, and a proportional per-ad-set floor at roughly 0.5% of campaign budget is the cheapest control anyone has stated for it that does not require duplicating the ad set and discarding its learning.
**Guards.** One account, one vertical, one operator, read off screen with no export. The 180 ad sets accumulated over a year include an unstated number of paused ones, so the live count is unknown. Nothing isolates the floor from the other choices in the account.""",
     [NT])

amend(SC, "SC-133",
      """**CONTESTED as of 2026-09-02, by the largest and longest counter-case on file.** Nick Theriot runs precisely this construction, a CBO with per-ad-set minimum spend, and reports scaling it from about $100/day to $5,000/day across 365 days at a $50 cost per purchase on $1.3 million of spend, with the floor set at $25/day per ad set (0.5% of a $5,000 campaign budget) and scaled down proportionally at lower budgets. The full account is at [[Scaling Models#SC-154|SC-154]] and its stated figures recompute.
**What does NOT resolve.** Neither operator ran the comparison. Blue Sense reports the CBO-with-floors version losing to ABO and says outright he does not know the mechanism; Theriot never ran the ABO alternative on this account, so he has no comparison either. **One important difference in how the floor is sized: Theriot's is a small proportional nudge at 0.5% of campaign budget, and Blue Sense never states what floor level he tried.** A floor large enough to override delivery is a different intervention from one that only stops an ad sitting at zero, and that distinction is the most likely place the disagreement lives. Do not treat either side as settled, and if we run it ourselves, record the floor as a percentage of campaign budget.""",
      [NT], status="contested")

amend(SC, "SC-001",
      """**THE THERIOT CPA GATE IS RE-SOURCED, 2026-08-31, which retires the caveat added on 2026-08-20.** That correction downgraded the gate to "one video's condition" because five later transcripts confirmed the 20% step without restating the condition. He now states it as a standing rule and to the cent: **"we just keep increasing budget by 20% if this cost per purchase is below $50. $50 is our target... it's not a vague rule of, well, it's $51. No, it's $49.99 and we scale or it's $50 and we decrease budget or we hold budget."** Two qualifications he adds in the same walkthrough. The target is per account, not a number to copy ("that doesn't mean $50 is your target"). And the read is taken on a 30-day average rather than on yesterday, against operators "literally look at a day to day and are tweaking out over results day to day", which also revises the earlier record of this gate as running on yesterday's cost per acquisition.
**The gate is read at the CAMPAIGN level, not on the ad that changed.** After a new winner landed he says explicitly "I don't look at this number on that specific ad. I look at overall", and the ladder he then walks is $5,000 to $6,000 to $7,200 to about $8,600, which recomputes. The hold period is still not stated by him, so the unresolved half of this claim stands unchanged.""",
      [NT])

amend(SC, "SC-007",
      """**The procedure restated in full, 2026-08-31, and it is read at the CAMPAIGN level with no ad set selected.** Open the campaign, click into Ads (not Ad sets), set the window to the last 7 days, sort by amount spent descending, then require every ad below the top spender to carry a LOWER cost per purchase than the top spender. Anything above it goes off. He walks the list live and kills at 52, then 77, against a leader in the low forties. Everything else is left alone: "that's all I do. And that's it."
Two boundaries in the same session. New ads are allowed to take spend freely rather than being judged early. And the campaign-level number, not the individual ad's, is what gates the budget decision that follows, which is the gate re-sourced at [[Scaling Models#SC-001|SC-001]]. The rule is stated as practice on a $5,000/day account; no test of the rule against not applying it exists on either side of this contest.""",
      [NT])

amend(SC, "SC-051",
      """**The founder-ad version of this failure, 2026-09-01, and it names an exit-value cost the rest of this claim does not.** Blue Sense reports repeatedly meeting brands that did $20 to $30 million of revenue off essentially one founder ad plus hook swaps and variants, and says his exposure comes from them "finding us after it's already too late": the concept fatigues, everyone in the target region has seen it, they respond by making more variants of the same concept instead of building other formats, "and then the business continues to decay." His own agency's stated control when a founder ad breaks out is to lean in without overweighting, on explicit portfolio grounds.
**The new cost, and it is worth carrying into any founder-led account we run.** He names a risk that has nothing to do with delivery: "there is no real downside to putting the founder in content other than potentially risking against an exit because if their ads start holding a lot of spend, it is going to be a marker within the term sheet that's going to cause issues." A brand whose acquisition depends on a person the buyer is not acquiring is a diligence problem. Same shape as the personal-page dependency recorded at [[Creative Science#CR-058|CR-058]].
Client anecdotes with no brand named, no spend shown and no term sheet quoted.""",
      [BS])

print("== Marketing Math ==")

mint(MM, "MM-198",
     "Department cost model for a coaching or consulting business at $100k/month: fulfilment 20%, sales 15%, marketing 20%, operations 15%, leaving 30% net, and every published cell recomputes",
     "T3", "active",
     """A full P&L allocation for the offer type several of our prospective clients run, stated as target percentages of revenue.
- **Fulfilment 20%**, split 15% to assistant coaches and 5% to the head coach. He names an over-allocation here as the most common structural error, with 40% splits imported from gym compensation models, and says 40% is not scalable in coaching. Agency and done-for-you offers can carry 30 to 40% because ticket price is higher and the selling is easier.
- **Sales 15%**, split 10% to the closer on new deals and 5% to the setter. Stated as a maximum, reducible with an hourly setter or an AI setter.
- **Marketing 20% minimum**, which at $100k/month is $20,000 of ad spend. **His band is the useful part: 10% "is too slow, it's going to maintain your business", 20% grows it slowly, and up to 40% is aggressive and puts most of the owner's take-home back into acquisition.**
- **Operations 15% maximum**, covering virtual assistants, onboarding, software, insurance and any physical overhead.
- **30% net margin** is what remains, which he calls healthy at this size.
**Arithmetic gate: every stated cell holds.** 20 + 15 + 20 = 55, leaving 45%, which is the $45k he states. Less 15% operations leaves 30%, the $30k he states. At 40% tax that is $18,000 take-home, and 30,000 x 0.6 = 18,000 exactly. His $500k/month illustration at the same margin gives $150,000, correct. **One transcribed sentence is inverted and worth flagging so nobody quotes it as written:** he states his own target as $20,000 a month and then says the $18,000 result is "still under 18k". The intended point, which the numbers support, is that $100k/month at a 30% margin does not reach his own $20,000 target.
**The consequence he draws is the reason to bank this.** Owners arrive assuming $100k/month is their goal, and reverse-engineering the take-home moves the real target to $250k to $300k/month. Every percentage point recovered has to come from the owner personally occupying a department: doing sales himself returns the 15%, doing marketing himself returns another slice, and 30% plus is only reachable by inserting yourself somewhere or by compressing operations with tooling.
**Guards.** These are prescriptions from a coaching operator to coaching clients, not an audited P&L, and no client's actual statement is shown. Read against [[Marketing Math & Unit Economics#MM-119|MM-119]], which gives the DTC equivalent at marketing 20-30%, G&A 10-20% and COGS about 25%: the marketing tranches agree closely across two very different business models, which is mild independent support for 20 to 30% as the workable band and for treating anything past that as a business-model problem rather than a media-buying one.""",
     [MS])

mint(MM, "MM-199",
     "The ceiling on an e-commerce account is the allowable acquisition cost, which is set by the back end, so the next scaling step is a product decision rather than a media-buying one",
     "T3", "active",
     """Stated as the closing diagnosis on an account the same operator had just scaled 50x in daily budget, which is what makes it worth recording.
The account runs a 2x blended return at a 17% net margin on a $50 cost per purchase and a $97 average order value. His own read: "I'm not going to say that's bad, but I'm not going to say that's good either." **The stated blocker on further scale is not the campaign, the creative or the bid: "if we really want to get to the next level, we need to be able to start building this business to accept a $100 cost per acquisition. That's literally double what we're getting now. It'll allow us to spend significantly more money."** The named route to doubling allowable acquisition cost is launching back-end products so existing customers buy again, and that work sits with the client rather than with the media buyer.
**Why this is worth its own entry rather than a line inside a scaling claim.** It is a media buyer, mid-walkthrough of his own best case, naming the limit of his own discipline. The account had already absorbed a year of creative testing, 180 ad sets and a 20% budget ladder, and the thing standing between $5,000/day and $10,000/day is a merchandising decision. It is the operating form of the tranche argument in [[Marketing Math & Unit Economics#MM-119|MM-119]] and of the recurring-revenue denominator rule already in this file: when the front end is efficient and the account still will not grow, the next lever is what a customer is worth, not what an impression costs.
Narrated from one account with the margin and return figures stated on screen. No back-end test has been run, and the $100 target is an aspiration rather than a modelled number.""",
     [NT])

print("== Learning & Signal ==")

mint(LS, "LS-074",
     "Conditional logic on a Meta Instant Form changes the OPTIMISATION TARGET, because a respondent routed to a non-lead end page never registers as a lead",
     "T3", "active",
     """The mechanism is the point, and it is one line: a disqualified respondent who is sent to a separate end page is not counted as a lead, so the event Meta is optimising toward silently narrows from "anyone who submits" to "anyone who qualifies".
Ben Heath, demonstrating in Ads Manager, builds a multiple-choice budget question, then uses the form's Logic setting to send anyone answering "less than 1K" to a different thank-you page with no lead conversion. **"None of these people that say they have less than 1K actually register as leads. Only the people that say they have 1K and above register as leads. So, in that instance, Meta is still just trying to get you leads, but who qualifies makes all the difference in the world."** His framing throughout is that "Meta's optimization system is very literal. It will get you exactly what you ask it to get you." His named question types are budget, timeline (a wedding photographer disqualifying people with no date set), industry for B2B, and location, and he singles out location as the fix for the common complaint of opt-ins arriving from outside the service area, because the disqualification teaches delivery where the served area is.
**The same construction on a landing page** is stated as harder to build and identical in principle: disqualified answers land on a page carrying no conversion event.
**Form type, and this is the second lever in the same panel.** He moves off the default "more volume" to **"higher intent" plus phone-number verification by one-time passcode**, on the grounds that it blocks fake numbers, blocks bots, and leaves only people willing to receive an SMS, which also makes the follow-up call easier. He rates the review-step option as "somewhat useful, but not a big needle mover."
**He is reversing his own published advice and says so, which is the dateable part.** "Previously, I have recommended go with more volume, don't have any conditional logic, reduce friction, get as many leads as possible. But I think we're now at a place where we're seeing so many poor quality leads come through with that setup... that we're by default switching more and more accounts to this setup." That is a named operator with 13 years and a stated $300 million of Meta spend moving from a low-friction default to a qualified default, dated 2026-09-01.
**Scope check against our own book, and it is a live one.** Four of our five accounts run Instant Forms, and our standing rule is that a form's job is to qualify and capture contact while the voice agent books. Conditional logic is exactly that rule expressed inside the form, and the OTP option is the one part to weigh separately, because a phone-verification step that suppresses a real opt-in costs us a call the agent would otherwise have made. **Nothing here is measured.** No before-and-after on lead volume, cost per opt-in, show rate or close rate is given for either lever, and the trade being made (fewer opt-ins for better ones) has no figure attached anywhere in the video. It is a mechanism plus a practitioner's reversal, and it is cheap to test on one ad set.""",
     [BH])

print("== Auction Mechanics ==")

mint(AU, "AU-084",
     "Two more deployed non-Meta ad systems publish A/B results showing that scaling user-sequence models and collapsing the cascaded ranking stages still buys revenue, which corroborates Meta's no-saturation claim from outside Meta",
     "T1", "active",
     """Picked up on the arXiv cs.IR lane on 2026-09-02. Same handling rules as [[Auction Mechanics & Bidding#AU-079|AU-079]]: these document OTHER platforms and must never be quoted as documentation of Meta. What they buy is independent, dated confirmation that the direction Meta describes is the industry's direction, measured on someone else's traffic.
**ReST (arXiv 2609.01240), a recommendation-native Transformer scaling framework.** Its authors report "a one-week online A/B test on a production advertising platform improves online AUC by 1.31% and lifts a core revenue metric by 11.93% within a 50 ms P99 budget", and say it is now fully deployed. Two structural details map directly onto what we already hold. First, the computation asymmetry they design around: "each request scores many candidates against one shared user history under tight latency budgets", which they solve by factorising into "a heavy reusable encoder and a lightweight cross decoder" with compute-once, decode-many-times ranking. **That is the same offline-user-model / online-ranking-model split Meta documents at [[Meta Delivery & Andromeda#MD-119|MD-119]], arrived at independently by another platform under the same latency constraint.** Second, their headline conclusion is that "behavior-sequence scaling remains a promising, under-exploited axis for production ranking", and that LLM-style Transformer blocks saturate where their recommendation-native design does not. Meta's own post says "the sequence model scaling law shows no signs of saturation". Two platforms, same finding, and neither cites the other.
**TGR (arXiv 2609.00986), Tencent's generative recommendation framework, deployed across Tencent surfaces serving hundreds of millions of users.** Its stated motivation is that "industrial recommender systems typically rely on cascaded retrieval, pre-ranking, ranking, and reranking stages, whose separately optimized models limit scaling, fragment decision making, and lack semantic knowledge and reasoning". Reported A/B results include **"+3.57% CTR and +1.71% advertising revenue"** from its unified ranking model, fully launched on two of five tested surfaces.
**The read, and it is a direction rather than a lever.** Everything this codex holds about Meta describes a cascade: retrieval, early ranking, late ranking, auction. Both papers say the industry is now spending its engineering budget on making that cascade less cascaded, by scaling one sequence model across it or by unifying the stages outright. Nothing in either paper changes an operating decision this week. What it changes is the expected direction of travel: **the parts of delivery an advertiser can address with settings keep shrinking, and the parts addressed by what the creative and the user history contain keep growing**, which is the same direction law 1a already points.
**Guards, all of them load-bearing.** Different platforms, different markets, authors reporting on their own systems, and the optimised metrics are platform revenue and CTR rather than advertiser outcome. Percentage lifts on someone else's baseline mean nothing for our accounts and must never be quoted as an expectable gain. Abstracts read in full on 2026-09-02; the full papers were not read. A third paper the filter surfaced the same morning, CoGR (arXiv 2609.00638), was read and NOT banked: its ad-relevant content restates the cascade already documented at [[Meta Delivery & Andromeda#MD-022|MD-022]] and its contribution is LLM-generated keyword representations for search retrieval, which touches nothing we operate.""",
     ["ReST: From Language to Behavior, arXiv 2609.01240, abstract read 2026-09-02 via cs.IR feed",
      "TGR: Tencent Generative Recommendation, arXiv 2609.00986, abstract read 2026-09-02 via cs.IR feed"])

amend(MD, "MD-119",
      """**INDEPENDENT CORROBORATION FROM ANOTHER PLATFORM, 2026-09-02.** A deployed production advertising platform publishes the same two-stage split, reached independently and for the same reason. ReST (arXiv 2609.01240) factorises ranking into "a heavy reusable encoder and a lightweight cross decoder", with "user-level shared-prefix training with shared-prefix serving for compute-once, decode-many-times ranking", explicitly because "each request scores many candidates against one shared user history under tight latency budgets". They report a one-week A/B lifting online AUC 1.31% and a core revenue metric 11.93% inside a 50 ms P99 budget, and state that behaviour-sequence scaling has not saturated, which is the same finding as Meta's "no signs of saturation" line above. **This does not amend anything here and it does raise confidence that the architecture Meta describes is a constraint-driven design rather than a Meta-specific choice.** Different platform, authors reporting their own system, abstract read rather than full paper. Full handling at [[Auction Mechanics & Bidding#AU-084|AU-084]].""",
      ["ReST, arXiv 2609.01240, abstract read 2026-09-02"])

print("== Google ==")

mint(GA, "GA-070",
     "There is no correct keyword count; the test is whether one ad group's keywords can be served by ONE intent, ONE set of ads and ONE landing page, and single-keyword ad groups are no longer the default answer",
     "T4", "active",
     """A structural rule with no data behind it, banked because it replaces a number people keep asking for with a test they can actually apply.
**The stated position.** Google will not stop you building an account of any size, so "there is no magic number" of keywords per ad group. The question to ask instead: "Could one set of ads credibly speak to all of the searches in this ad group? Could one landing page satisfy them well? Do these keywords belong to the same buyer conversation? Will this grouping make optimization easier or muddier?" If the answer goes fuzzy, split.
**The one number offered, and it is explicitly a soft trigger rather than a limit.** Past roughly 20 keywords in an ad group, stop and re-check that the group still carries a single coherent intent. He states directly that 21 is not a problem in itself.
**Three levels, checked in order.** Ad group first, then campaign (where individually acceptable ad groups reveal overlap, redundancy and low-value groupings that make budget harder to control and optimisation slower), then account (where accumulated structure becomes legible only to whoever built it).
**The worked split.** A premium office chair group holding office chair, ergonomic chair, best office chair, office chair near me, gaming chair, desk chair for back pain, office furniture, executive chair, cheap office chair, office chair sale, standing desk chair and buy office chair online mixes category, ergonomic, local, price, gaming and use-case intent in one place, so the ads go generic and no landing page serves all of it. Split into ergonomic, deals and gaming groups and the ads, the pages and the reporting all resolve.
**The claim that dates this.** Single keyword ad groups "definitely had their moment and they earned it. But match types and machine learning have changed the environment fundamentally", so the fix for a bloated account is tighter intent rather than one keyword per group. The match-type multiplication habit, building exact plus phrase plus broad variants of near-identical keywords for coverage, is named as a main cause of bloat.
**T4 and it stays there.** No account, no data, no test, and the 20 is offered as a rule of thumb by the presenter's own description. It is a useful audit question set and it decides nothing on its own.""",
     [S8])

print()
total, tiers, stat, per = audit()
print("TOTAL", total)
print("TIERS", tiers)
print("STATUS", stat)
for k, v in per.items():
    print(f"  {v:5d}  {k}")
