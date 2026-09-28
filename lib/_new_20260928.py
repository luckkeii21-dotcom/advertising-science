# -*- coding: utf-8 -*-
"""New claims banked by the 2026-09-28 research run."""
import io, os

SCI = r"E:\claude code marketing skill\Obsidian God-level Marketing Vault\God-level Marketing\wiki\science"
BS = ("Blue Sense Digital, How To Write Meta Ads That Scale: Copywriting Masterclass, "
      "2026-09-28, youtube.com/watch?v=LoL1w-k9Mgg, 181 min, read in full")


def append(p, block):
    fp = os.path.join(SCI, p)
    with io.open(fp, encoding="utf-8") as f:
        s = f.read()
    if not s.endswith("\n"):
        s += "\n"
    with io.open(fp, "w", encoding="utf-8", newline="") as f:
        f.write(s + block)
    print("appended to", p, "->", block.split("\n", 1)[0][:70])


CS = "Creative Science.md"

append(CS, u"""### CR-267 \u00b7 The nine-beat script, and the job each beat does
Tier: T3 \u00b7 Status: active
The full running order, from an operator who says he is spending about $1M a day: **hook, problem, promise, mechanism, objection, proof, offer, risk reversal, call to action.** What each one is for, in his words and compressed: the hook buys attention and pre-qualifies; the problem agitates a consequence the buyer already accommodated; the promise states what they get in their terms; the mechanism gives them a reason to believe the promise; the objection beat handles what they already tried; proof substantiates the claim; the offer presents the product; the risk reversal makes the offer survivable; the CTA asks.

**The ordering is not stylistic, it tracks the six objections in the order they arrive.** See [[Creative Science#CR-271|CR-271]]. His summary of the resulting message: this is for you, this will work, it will work specifically for you, it is worth the money, we guarantee it or you get your money back, and you have to buy today.

**Two failure modes he names for the promise beat specifically, because it is the one most often missing.** Going problem straight to mechanism with no promise at all, which he says is most common in technically minded brands and in supplements; and stacking five promises so each one loses its value. A third, subtler one: stating a promise that is really a feature. "Six clinically studied ingredients" is an input, not an outcome the buyer receives.

**The Ben Suarez rule he attaches to the promise beat: a smaller promise you can prove outsells a larger promise you cannot, every time.** That is the same direction as the independent B2B finding in [[Creative Science#CR-036|CR-036]], where a first-client promise beat a five-client promise among seven-figure applicants, which is two sources from different categories landing on the same place.

**Limits.** This is a framework taught in a teaching video, not a tested structure. No hit rate, no split test, no account numbers are attached to the nine beats as a unit. He is explicit that frameworks get a writer to roughly top 10 to 20% and that the last stretch comes from breaking them. Use it as a checklist for reading and briefing scripts, which is the use he actually claims for it, and do not present it to a client as a measured lift.
Sources: __BS__
Last touched: 2026-09-28
### CR-268 \u00b7 Agitate the ACCOMMODATION, never the symptom
Tier: T3 \u00b7 Status: active
The sharpest single idea in the source, and it is testable in an afternoon against any script already written. **A symptom is what the body or the day is doing. An accommodation is what the buyer already changed about their life to work around the symptom, usually without ever admitting they changed it.** The symptom they already know, so naming it buys nothing. The accommodation they have never said out loud, so naming it is the line that stops the scroll.

His worked pair, hair thinning. Symptom version: "if you're finding more hair in the shower drain, you're not imagining it." Accommodation version: **"you've stopped parting it in the middle. You didn't decide to do that. You just started doing it."** Three reasons he gives for the gap: the drain is a symptom, the drain is available to every competitor and the category already leans on it, and a consequence can be agitated where a symptom cannot. Second pair, bloating. Weak: "bloating can be uncomfortable and frustrating." Rewrite: "you've started planning what you wear around which days are bad."

**Six operating constraints on the problem beat.**
1. **Length, 10 to 15 seconds** in a standard script. Longer only in a format built for it, where he has seen animation and claymation VSLs agitate for two minutes and hold half a million dollars of spend. He is explicit that this is not needed on an average script.
2. **The reorder test for whether you are agitating or complaining.** If any two lines can be swapped without changing the argument, you wrote a list of symptoms instead of an escalation toward a consequence.
3. **Argue at CATEGORY level, not product level.** A viewer can dismiss a product as marketing hype and cannot dismiss a whole category, so the category borrows you authority you have not earned yet, and you are not asking for belief in you until much later in the script.
4. **Agitate one person, never two.** He calls this the single biggest predictor of whether the problem beat works.
5. **Do not resolve the problem inside the problem beat.** The job is to seat them in the discomfort.
6. **Three legal entry points:** the accommodation, the moment, or a failed solution. Entering on a failed solution locks the whole ad to solution-aware, which is fine as long as it is a decision rather than an accident.

**The brand-safety answer, which is the reason this survives a brand review.** The objection he gets is that the brand does not want to be negative. His reply is that the thing brand teams are actually objecting to is **pity**, which is what you produce when you stack symptoms and frame the buyer as a sufferer, and that a single named accommodation is an observation rather than an insult. **His rule: frame against the accommodation, never the affliction.** That is also the mechanism behind the extended-agitation failure, because a two-to-five-minute problem beat is long enough to slide from observation into sufferer framing.

**Cheapest way to use this today:** pull the problem beat out of any live script and ask whether it names a symptom or an accommodation. If it names a symptom, the fix is research and not rewriting, because you cannot invent an accommodation. T3, taught with worked rewrites and no split test.
Sources: __BS__
Last touched: 2026-09-28
### CR-269 \u00b7 The promise must precede the mechanism, and a feature with no mechanism gets cut or swapped for proof
Tier: T3 \u00b7 Status: active
**Three things do different jobs and teams routinely ship only two of them. The feature is what it is. The promise is what you get. The mechanism is why the feature produces the promise.** His sentence template makes the dependency explicit: *the feature*, which means *the promise*, which is why *the mechanism*. Worked: saw palmetto at 320 mg, which means you stop losing hair at the part, which is why DHT is what shrinks the follicle every cycle and saw palmetto blocks the enzyme that makes it.

**The ordering claim, and it is the operational one.** Lead with the promise, then the mechanism, never the reverse. His stated reason is the retention curve: an ad that opens on technical jargon loses people before the promise ever lands, whereas the promise is comprehensible to the whole addressable market and then makes the mechanism legible when it arrives. Real inverted example he cites: "lowers ghrelin and increases leptin, which makes you less hungry." His rewrite: "you stop thinking about food at 11am, because the ketones suppress ghrelin, which is the hunger hormone." **He claims 30 to 40% of ads in a normal feed get this backwards**, which is an eyeball estimate with no count behind it and should be read as "common", not as a rate.

**What each element sells on its own, and the answer is nobody.** A feature alone sells only an already-convinced audience, which on cold traffic is no one. A promise alone is available to the whole category and will not survive past sophistication stage two. The mechanism is what makes the promise believable and differentiates inside one sentence.

**The escalation ladder when a feature has no mechanism.** Find a real mechanism, or swap the feature for one that has a mechanism, or fall back to promise-and-proof alternation with no mechanism at all. He is clear the fallback underperforms and is the correct move in low-sophistication markets.

**"My product has no mechanism" is almost always false.** His answer: a mechanism is just the reason the feature produces the promise, and every physical product has one because somebody made a decision and that decision has a nameable consequence. Merino wool in a t-shirt is an argument, not an ingredient: the fibre is crimped, so it traps air, so odour stays in the fibre rather than on your skin. The manufacturing line, the supplier, the wash test and the rejected formulation are all mechanism material.

**A contradiction is not a mechanism, and it is the common counterfeit.** "As much caffeine as a coffee but you don't get the crash" opens a curiosity gap and substantiates nothing. Either introduce the mechanism (theanine cancels the jitters), promote the line to the hook where an unresolved gap is the job, or cut it.
Sources: __BS__
Last touched: 2026-09-28
### CR-270 \u00b7 The proof ladder, strongest to weakest, and proof must outrank the claim
Tier: T3 \u00b7 Status: active
**The ladder, in his order.** 1. **Demonstration**, the thing visibly working on camera, before-and-after included. 2. **Third-party verification**, clinical results, lab tests, certifications, and independent press, where he singles out real news-anchor-footage ads as some of the best performers he has seen. 3. **Volume of specific social proof**, review and customer counts. 4. **A named individual testimony.** 5. **Mechanism explanation**, which he grades as not really proof but as something that makes a claim plausible through logical selling. 6. **Founder assertion**, the weakest, and worth nothing unless the founder carries actual standing in the domain.

**Rungs 3 and 4 swap by category, and the swap is predictable.** For a considered B2B or agency purchase, one specific testimonial from a recognised peer outweighs a large undifferentiated review count, because 5,000 five-star reviews with no specificity could be anybody. For mass-market consumer goods the volume rung holds.

**The governing rule: match the proof to the claim, and modest claim plus strong proof beats large claim plus weak proof.** He ties this directly to market sophistication: inflating the claim is the stage-two move, most categories are at stage four or five, so in a normal market a bigger claim simply raises the proof you owe.

**Specificity is what converts a proof rung into a usable line.** Weak: "customers love it." Strong: "360,000 customers, and the word *finally* appears in our reviews over 6,000 times." That is the volume rung and the testimony rung in one sentence, with a count attached to each.

**The no-proof objection, and why the ladder matters most to a brand that has none.** A new brand cannot claim volume, cannot afford a clinical trial and has no founder standing, which removes rungs 2, 3 and 6. It still has rung 1 outright, because anyone can demonstrate a product on camera from day one, and it can buy rung 4 cheaply by giving the product to twenty people and asking for detail rather than a rating. T3 throughout, taught with examples, no numbers behind the ordering.
Sources: __BS__
Last touched: 2026-09-28
### CR-271 \u00b7 Six objections cover nearly every buyer, each maps to one script element, and the objection order IS the script order
Tier: T3 \u00b7 Status: active
Against the common belief that objections are specific to your business, the claim is that they generalise into six, and that each has one fix living in a named part of the script.

| Objection | What answers it |
|---|---|
| This isn't for me | Persona-specific language |
| This won't work | Mechanism plus proof |
| It might work, but not for me | Proof specific to THAT persona, usually a testimonial |
| It's not worth it | The offer, and the cost of not buying |
| What if I'm wrong | Guarantee or risk reversal |
| I'll do it later | Urgency or scarcity |

**The order in the table is the order they arrive, and therefore the order the script must answer them.** You cannot handle "what if I'm wrong" before you have established "this will work". He reads the resulting nine-beat script ([[Creative Science#CR-267|CR-267]]) as this list executed in sequence.

**Two consequences worth acting on.** Row 3 is why generalised proof underperforms: the fix is not more proof, it is proof carrying the same persona. Row 4 is why the answer is sometimes not a discount but the cost of inaction, his example being an acne cream priced against the multi-year medication path it avoids rather than against a competitor cream. Row 6 is also the structural reason Black Friday lifts sales without any creative changing.

**Pre-empting beats answering, and the material comes from research rather than invention.** Weak: "gentle enough for sensitive skin." Strong: "you're going to react to this in week one. Everyone does. That's why we made the first tube just 0.05% and why the second one bumps up." The second version names an experience the buyer has already had, in their language, and explains the product decision that anticipates it. That line only exists if the review and call corpus produced it. See [[Creative Science#CR-278|CR-278]].
Sources: __BS__
Last touched: 2026-09-28
### CR-272 \u00b7 Retention falls at the BRIDGES between beats, and hooks written in isolation cause the first drop
Tier: T3 \u00b7 Status: active
**The claim: a script's beats can each be good and the ad still bleed viewers, because the losses happen at the joins.** Two bridges carry most of it. The first is hook into body. The second is wherever the viewer goes from not knowing about the product to knowing about it, which is the product introduction and can sit anywhere.

**The discipline, stated as a chain:** the only job of line one is to get line two watched, and the only job of line two is to get line three watched. A bad bridge produces a visible step down in the retention curve rather than a smooth decay.

**How teams create the first bad bridge, and it is procedural rather than a skill problem.** Hooks get generated in a batch, often by a model, judged in isolation, and then stitched onto a body nobody checked them against. Each hook reads fine alone and several make no sense flowing into the problem beat. His instruction for anyone writing three to five hooks is that the hook has to sell line two, and that the check is reading the join rather than reading the hook.

**The second bad bridge is the TV-advertisement swerve:** good education, then "and that's why Nourish Plus is your best solution," which he reads as the moment the viewer realises they are being sold to. The fix he shows is to route around the product name entirely for another beat or two. Weak: "which is why we made Nourish Plus with six clinically studied ingredients." Rewrite: "the fix isn't a better shampoo, it's getting the follicle to stop shrinking. Three things do that, and the first is the reason most people fail." Then later, "you can buy those separately and people do, or you can take them all in one capsule." The product may appear on screen before it is named. This is the mechanic under [[Creative Science#CR-127|CR-127]].

**His honest caveat on his own worked script:** a bad second bridge is usually not repairable by editing one line, and the half of the script after it needs rebuilding so the product can be introduced where it belongs, in the offer beat or even at the CTA. T3, reasoning from a retention curve he describes rather than one he shows.
Sources: __BS__
Last touched: 2026-09-28
### CR-273 \u00b7 There is no optimal ad length; length is bought from the PROBLEM and MECHANISM beats, and longer ads scale because length forces you further up the awareness ladder
Tier: T3 \u00b7 Status: active
**The starting position: 30-second ads have spent millions and 20-minute ads have spent millions, so length is not the variable.** What length changes is production cost, hit rate and spend ceiling, and those trade against each other.

**The scaling argument, which is the non-obvious part.** He claims the longer the ad, the more scalable it tends to be, and the stated reason is that you cannot fill six minutes while staying product-aware. Length pushes you into unaware territory, where the total addressable market is largest. The observed shape in long animation ads is a story opening with no product in sight, agitation starting around ten seconds in and running for about two minutes.

**Which beats absorb length, by runtime.** The hook never lengthens; it is a one-liner at every duration. The problem goes from one line at 15 to 45 seconds, to several lines at 90 seconds, to a scene of two to three minutes at six to ten minutes. The promise does not exist at 15 seconds, is one or two sentences at 30, and never exceeds two sentences. The mechanism does not fit at 15 seconds, is one sentence at 45 to 60, expands to several at one to three minutes, and becomes load-bearing at five minutes and up. Objections do not fit at 15 seconds, run two to three sentences at 60 seconds to two minutes, and become multi-minute blocks past six minutes, usually folded into the agitation. Proof runs one to three pieces at 60 seconds to two minutes and can carry all six ladder rungs in a long ad. **The offer stays short at every length and he is explicit that you do not want to buy length there.** Risk reversal does not fit under 60 seconds and is one line above it. The CTA appears at every length, and past four minutes there are multiple CTAs at intervals with the script looping back through proof, offer and risk reversal after each.

**The loop is the actual length mechanism past a few minutes:** problem, promise, mechanism, objection, proof, then back to problem, roughly three times. The worked pattern he attributes to IM8 is a timeline vehicle, day 7 / 14 / 30 / 90 / 180, where each horizon reopens a problem and closes it with a promise.

**The economics gate, and he states it as a hit-rate question.** A five-minute ad is on the order of two days of scripting. Ten 30-second ads fit in the same two days. If the hit rate is the same 10% at both lengths, the ten short ads win outright, so a long ad has to earn its slot by raising hit rate or by raising spend capacity.

**He retracts his own earlier advice here, in a second self-correction in the same video.** The retracted version was to script one long ad, hand it to an editor and get a five-minute and a one-to-two-minute cut. "That was bad advice." **Build for the length: write the short one as its own script, because the bridges differ.**
Sources: __BS__
Last touched: 2026-09-28
### CR-274 \u00b7 Believing is not wanting, which is why a logically perfect ad passes every review meeting and still sells nothing
Tier: T3 \u00b7 Status: active
His third and largest self-correction in one video, and the one with the sharpest organisational diagnosis attached. "I used to teach the mechanism as though believing was the same as wanting, but it's not. And they're not even remotely close. You can build an argument so logical that a buyer agrees with every single sentence and still does nothing."

**The organisational failure mode, and it is why this is worth banking rather than filing as motivation.** "That ad will look completely fine in every review meeting that it goes through because everybody in the room is checking whether it's correct... but nobody in the room is checking whether anybody actually wants it." A framework makes a review meeting efficient at the wrong question. **A checklist produces competence, and competence is not what gets remembered.**

**Why it goes missing: it is the half that does not survive being turned into a framework.** Identity and emotion have no beat to sit in, cannot be given a slot number in the nine-beat structure ([[Creative Science#CR-267|CR-267]]), and should thread through every line, with a few dedicated sentences where they fit.

**The mechanical version, which keeps this out of brand-land.** Every feature and every mechanism answers an unstated "so what", and the answer is an identity rather than a benefit. Blocks DHT becomes the kind of person who starts before it is visible. 12 g of collagen becomes someone who takes it seriously rather than dabbling. Merino becomes someone who packs one bag. A 90-day guarantee becomes someone who has been burned by this category before. Absorbs in 40 seconds becomes someone out of the house by 6:30am. Third-party tested becomes someone who checks things, and he notes it does not matter whether they actually check, only that they see themselves that way.

**The constraint that makes this performance work rather than branding: identity without mechanism is a lifestyle brand with a supplement attached.** An identity claim has to tie back to something the product actually does, or it never reaches the script at all.

**One deployable pattern he offers, stated as the only framework-shaped piece of it: make the final line of the ad a play at the buyer's identity.** His worked line, "the women who keep it are the ones who started before they could see it," is doing three jobs at once, identity, urgency, and a soft persona disqualification of anyone who will not keep the habit and would churn anyway. This is stage five of market sophistication arriving as a sentence rather than as a positioning deck.
Sources: __BS__
Last touched: 2026-09-28
### CR-275 \u00b7 Storytelling is a delivery mechanism across all the beats, never a tenth beat, and three specific things break a story ad
Tier: T3 \u00b7 Status: active
**Story is not a slot in the running order.** The failure he names is treating it as an add-on, bolting thirty seconds of story onto the front, middle or end of a finished script. Every beat still has to be there; the story is how they are carried. The nearest analogy he draws is switching person, which changes the whole ad without changing a single argument.

**Four shapes cover roughly 80 to 90% of DTC story ads,** and each shape is a beat wearing a costume. The **failed-solution journey** ("I tried the rosemary oil, then the supplements, then my GP said it's hormonal") is objection handling. The **discovery** ("I found out why it happens at the part first, and it changed how I bought") is the mechanism. The **transformation with a witness** ("my sister noticed before I did") is proof. The **confession** ("I stopped parting it in the middle about a year ago, I never told anyone") is the problem beat.

**What the story actually changes is the viewer's job.** Watching an ad, her job is to evaluate you, and she audits every sentence. Inside a story, her job is to find out what happened, and the argument arrives while she is doing something else. Every beat is still delivered and none of them is being marked.

**Three break modes, and he ranks them.** (1) **The bridge**, the most common, where the story runs and then the ad starts. He deliberately left this broken in his own worked script so the join is visible, and he notes a story ad usually cannot be 30 or 45 seconds because the bridge to the offer needs room. (2) **An obviously acting narrator**, which is a real-customer-reading-a-script problem more than a casting problem. (3) **A story with no stakes**, which he calls as common as the bridge failure and traces to insufficient research rather than weak writing: the writer is not the ICP, has no accommodation, no failed solution and no moment of realisation, so they invent a sequence that never happened. Weak: "I've been looking for something to help with my hair for a while." Rewrite: "I'd stopped going to the hairdresser because I thought she'd say something."

**Three tips attached.** The default is **first person, past tense**, and switching person and tense is a cheap route to variant volume off a proven script. **Do not resolve the story in the hook**; he has seen nine-minute ads spending heavily. **If it did not happen it is fiction and has to read as fiction**, which is both an ethics and a compliance line, and he notes separately that a speaker making product claims about a product they never used is not compliant.

**The "my category isn't personal" objection fails on its own terms:** the narrator need not be a customer or even a person. The brand can tell the discovery in third person, and the thousand-year-old-remedy shape in supplements is a third-person story with no founder in it. This is the shape of most long-form advertorials and most good B2B copy. What cannot be dropped is the stakes, and a category that genuinely has none has an unfound accommodation rather than a story problem. See [[Creative Science#CR-268|CR-268]].
Sources: __BS__
Last touched: 2026-09-28
### CR-276 \u00b7 Sentence-level craft for spoken scripts, and the two tells that mark a script as AI-written
Tier: T3 \u00b7 Status: active
A script can carry every correct argument and still be unusable, because what to say and how it sounds when said are different skills. The over-the-top pair: "follicular miniaturization occurs when dihydrotestosterone binds to receptors at the base of the follicle, resulting in progressively finer hair with each successive growth cycle" against "there's a hormone that binds to the follicle. Every cycle the hair comes back a bit finer. Then one cycle it doesn't come back at all." Four reasons the second wins: one idea per sentence, the verb early where the meaning is, complex words removed, shorter sentences.

**Six decisions to make deliberately on every script.**
1. **Person.** First for storytelling, second for most scripting, third for description. His performance ordering is second, then first, then third.
2. **Tense.** Past for stories, present for mechanisms.
3. **Sentence length.** Short, but VARIED, because uniform length is what sounds robotic. His own pattern, which he points at in his own transcript, is long, long, short.
4. **Reading level.** Below grade seven as a default, raised when the buyer's own vocabulary is higher. His stated reason for not obeying the rule himself is that he is speaking to founders and marketing managers.
5. **Contractions, always.**
6. **Last word.** End the sentence on the word that matters.

**The two AI tells he names are worth recording precisely, because they are diagnostic and they are checkable by machine.** Uniformly short staccato sentences, and **contrast negation** ("it's not X, it's Y"). He adds that models default to uncontracted forms for no reason he can see. His recommendation is to put the whole list in the instruction file rather than fixing it after generation.

**The technique he rates above all the others costs four minutes and needs no tooling: stand up and read the script out loud at recording pace.** Every trip is a cut point. Every time you run out of breath the sentence is too long. Every line you feel embarrassed saying is a line to rewrite. He is explicit that reading it in your head does not work and that he has repeatedly approved scripts silently that fell apart at the teleprompter.

**Register as a volume lever.** The same angle, persona and argument rewritten in three registers gives three genuinely different ads: UGC (second person, present, casual, heavily contracted), documentary (third person, older, no enthusiasm), diary (first person, past, written to nobody).

**Note for this workspace.** Two of the tells he names independently match house style rules already in force here, the ban on contrast negation and the requirement to vary rhythm rather than default to short sentences. An outside operator arriving at the same two from a performance angle is corroboration, not a coincidence worth acting further on.
Sources: __BS__
Last touched: 2026-09-28
### CR-277 \u00b7 AI script writing: retrieval not invention, and selection is the human job
Tier: T3 \u00b7 Status: active
**The failure mode stated mechanically:** a model predicts the most probable next token, so without heavy context it regresses to the mean of its training data, and for ad copy that mean is product-description pages. His rough estimate of the ratio of Shopify product descriptions to Ogilvy in a general corpus is about 300 to 1, offered as an illustration rather than a measurement. He is explicit that this does not mean AI cannot write well and that he has shipped model-written copy unedited.

**The governing instruction: retrieval, not invention.** Give the model the research corpus and tell it to use only that, quoting the customer's own words from call recordings, reviews and testimonials. When asking it to pull external research, require it to retrieve and hyperlink rather than generate. His demonstration of the alternative: asking a chatbot what objections a hair-thinning buyer might have returns "will this actually work for me, where's the proof, how long will it take, what if I stop taking it, could it make my hair worse, are there side effects," which is the category average and describes no actual customer.

**The specific hallucination to guard against is a MECHANISM.** Asked to write against a product that has no mechanism, a model will invent one or reach for the category-standard one. Since the mechanism is load-bearing in the structure at [[Creative Science#CR-269|CR-269]], this failure is invisible in a well-formed script and fatal in a compliance review.

**Four things it is genuinely good at, and all four are downstream of a human-built argument.**
1. **Transposition.** Take a winner and change person, tense, persona or mechanism while holding everything else. He rates this as much faster than a human and as the cheapest route to volume off a proven asset.
2. **Variant volume**, given an explicit statement of what you believe makes the winner work and what must not move.
3. **Structural auditing.** Load the nine-beat framework into a file and have it check a script against it. His example exchange is "your script is missing a promise," then "give me five promise options."
4. **First drafts** when the research is done and the writer is stuck.

**Also usable with care:** lengthening and shortening, but only with explicit instruction about which beat should absorb the change, or it pads the hook and the risk reversal.

**The framing that matters most for how a team is organised: AI is not high leverage here, because writing the words was never the hard part.** The 80% is the research corpus, the mechanism, the objections and the proof, and none of that is delegable. **What the human job becomes is selection**, the judgment to read model output and know which lines are good, which are average and which need rewriting. One leverage move he does name: put the actual source material in context, the copywriting canon rather than the open internet, so the model has something better than the mean to regress toward.
Sources: __BS__
Last touched: 2026-09-28
### CR-278 \u00b7 Five research sources ranked by yield and effort, each yielding one thing none of the others do, and five outputs that map onto five of the nine beats
Tier: T3 \u00b7 Status: active
**The table, and the column that matters is the last one, because it is the reason to run all five rather than the cheapest one.**

| Source | Yield | Effort | What ONLY this gives you |
|---|---|---|---|
| Call recordings | High | High | The final objection immediately before purchase |
| Support tickets and return reasons | High | Very low | The failure modes, in the unhappy customer's own escalating language |
| Reviews | High | Lowest | The exact words the customer uses for the product |
| Post-purchase survey | Medium | Low | What they were thinking at the moment of purchase |
| Reddit, Facebook groups, forums | Medium to low | Medium | The language of people who have NOT bought |

Work top down if capacity-constrained. A startup with no customers has to work bottom up and move upward as customers arrive. **Why the post-purchase survey is capped at medium:** it is multi-choice, because submit rates collapse the moment it is not, and the respondent has not received the product yet, so the data is about an impulse rather than an experience.

**Why the failure-mode column is commercially load-bearing.** Support tickets tell you which claim the product does not deliver on. That is not a copy input, it is a copy prohibition: an angle can produce good return on ad spend and a 50% return rate, and the angle still has to be killed.

**Two collection tips.** In reviews, the value is in the **two-to-four-star** band, where the customer thinks the product is fine but has reservations, and reservations are objections in the buyer's own words. He attaches an ethics condition: using those objections in copy without fixing the product is a con. On call recordings, transcribe, then run the transcripts through a model to clean the language before searching them, because raw transcripts mis-hear words and poison the retrieval, then search for near-miss phrasings like "I nearly didn't".

**The five outputs, and each one is the raw material for a specific beat.** The **accommodation**, what they changed about their life without admitting it, becomes the problem beat. The **failed solution**, what they tried first, what it cost and why they stopped, becomes objection handling. The **nearly-didn't-buy**, the last thing standing between them and purchase, becomes the risk reversal and the offer. **The word**, the noun they actually use for the problem, becomes the hook. **The moment**, the specific week or day they started looking, becomes urgency.

**The word is the most overlooked and he argues it is the most important.** Buyers with thinning hair do not say "thinning" and never say "alopecia"; they say "shedding" and "my part" and "I can see my scalp". Bloating becomes "I looked four months pregnant by 4pm". Joint support becomes "I struggle to get off the floor without needing support". Creatine for muscle support becomes the ache at 55 that was not there before. **The general failure: packaging language asks the buyer to translate your category word into their own felt experience, and they will not do it.**

**The payoff claim: after five sources and five outputs, the ad is most of the way written before anyone has written a word.** T3, taught with a worked example and no measurement of the research pass against a skipped one.
Sources: __BS__
Last touched: 2026-09-28
### CR-279 \u00b7 The three-question differentiator test, and specificity is evidence where an adjective is only an opinion
Tier: T3 \u00b7 Status: active
**Three questions to run on any differentiator before it is allowed into copy.** Is it a proposition, meaning does it say buy this and get this specific thing? Is it unavailable to competitors? Will it move a stranger, meaning is it strong enough to pull a mass audience?

Scored examples. *Family owned since 1994*: proposition yes, unique probably, moves a stranger no. *Made in Australia*: yes, sometimes, no. *Free shipping*: yes, no, no. *Third-party lab tested with results published on the website*: yes, yes (there is a real cost barrier), yes. **Only the last one earns space.** He notes separately that "world-class service" is not even a proposition, because the buyer does not receive a thing, only a claim.

**Question three is where nearly every real-world differentiator dies, and question three is the one teams skip.** Vegan, cruelty-free and made-in-X pass the first two and fail the third, and seven or eight words spent on them is about four and a half seconds of a video ad given to something that moves nobody. **His related diagnosis: they are usually sitting in the objection-handling slot, answering an objection no buyer actually has.** His prescribed fix for that line is deletion rather than rewriting, because you cannot replace it until research tells you what belongs there.

**USP stacking is the common workaround and he grades it honestly: it works a little and it is still red ocean.** Combining two generic propositions that are rarely seen together (a genuinely good fragrance that also does not irritate) produces something technically unique. It fails the actual test anyway, because being unique is worthless if the combination does not channel an existing desire. See [[Creative Science#CR-136|CR-136]].

**The specificity ladder, from Hopkins.** Measured numbers, then a named third party, then a specific physical detail, then a specific time, then proper nouns. **The principle underneath: an adjective is the writer's opinion and any competitor can use it, where a specific is evidence.** Worked pairs: "our serum leaves skin looking healthier" against "it's 0.05% retinol and the first tube is dosed low on purpose", which also opens a curiosity gap the ad closes later; "fast absorbing" against "dry in 40 seconds, and we timed it"; "luxury craftsmanship you can feel" against "one person stitches each pair start to finish, it takes her four hours".

**Specificity also rescues urgency.** "Limited time only" is meaningless. "We make 400 ads a month, October is gone, the next batch ships on the 14th of November" is a real constraint with a real date, and honest urgency is specific by construction.

**Where the specifics come from: the boring parts of your own operation.** The Schlitz story, 1907, is the canonical case. Hopkins watched the brewery sterilise empty bottles with live steam, asked why nobody mentioned it, was told every brewer did it, ran it anyway because nobody had said it, and Schlitz went from fifth in the market to first. Three questions he derives: what does your factory do that you assume is boring, what did you reject during formulation, and what constraint did the product impose that you have never mentioned. His magnesium worked example turns a manufacturing fact (oxide is cheap and passes straight through, glycinate absorbs and is harder to produce) into a unique mechanism.

**The compliance objection is answerable: you can be specific without making a claim.** Attach the specificity to something you can evidence, such as the 90-day cycle the mechanism actually runs on, rather than to a promised outcome you cannot back.
Sources: __BS__
Last touched: 2026-09-28
### CR-280 \u00b7 The offer outranks the copy, and most offer improvements are repackaging what the business already does
Tier: T3 \u00b7 Status: active
**His ranking of what decides the outcome, in order: the offer, then the market you take it to, then the unique mechanism, then the proof and credibility, then everything else in scripting.** The reason he puts it inside a copywriting video is that a world-class script against a bad offer still does not sell, and the offer is an input to the script rather than a parallel concern.

**The offer is the product plus the value perception, and the product half is not a marketing problem.** Good marketing sells bad product, nobody repeat-buys, customer acquisition cost rises with scale no matter how good the marketing is, and what is left is a shrinking short-term arbitrage.

**Five elements of an offer the script actually consumes.** The **thing**, what I get in my own words. The **terms**, what it costs, framed. The **reversal**, what happens if it does not work. The **reason for now**. The **effort**, what I have to do and how long it takes. Each is a dependency: you cannot risk-reverse in the script if the offer has no reversal, and you cannot create urgency if nothing in the offer or the mechanism supplies one.

**Four pricing moves, each a rewrite rather than a price change.** *Anchor against the alternative*: not "was $89, now $69" but "one appointment with a specialist costs $200 and they'll tell you to take this anyway." *Reduce to the ridiculous*: not "$69 for 90 days" but "73 cents a day, less than the coffee you're drinking." *Price the problem, not the product*: name what not solving it costs. *Make the effort the price*: substantiate the cost by collapsing the effort, "one gummy every morning, you'll forget you're doing it."

**Guarantee craft, and the rule underneath it: a guarantee that costs the seller nothing proves nothing.** "30-day money-back guarantee" against "take it for 90 days, if your part hasn't changed, send us the empty tubs and we'll refund all three." Four reasons the second is better: it is specific where everyone else is generic; it is **slightly uncomfortable for the seller**, and that discomfort is exactly what signals the claim is true; it matches the mechanism's own timeline, so it reinforces the 90-day cycle rather than contradicting it; and it carries the messaging, reinforcing both the mechanism and the requirement that the product actually be used.

**The answer to "I'm just the copywriter, I can't change the offer", and it is the practical core of this claim.** Correct, and price is not yours to move. What you can do is find what the business already does, or would do at near-zero risk, and use it properly in the messaging. In his worked example four of five offer elements were already true and simply never said. A 90-day pack almost certainly already exists or is a three-pack bundle nobody objects to creating, possibly on an unlisted landing page. The urgency was already inside the mechanism, because thinning cannot be reversed and can only be stopped, so stating it changed the perceived offer without changing anything at all. **An offer is not a discount, a bundle or a shipping threshold. It is a reframe of the value from the buyer's side.**
Sources: __BS__
Last touched: 2026-09-28
""".replace("__BS__", BS))

print("CR block appended")
