---
title: "Lesson 079 - Every Gate We Built Reads Words"
type: lesson
lesson: 79
date: 2026-11-12
topic: Creative Science
claims: [CR-291, CR-169, CR-249, CR-168, CR-119, CR-024, MD-124]
tags: [advertising-science, lesson, creative-science, ai-creative, quality-gates, evidence-tiers]
---

# Lesson 079 · Every Gate We Built Reads Words

Topic: Creative Science, harvest-driven, so the pointer holds at 0. Thursday, so no video.

Yesterday's research run banked one claim and it is the first thing worth teaching from the harvest in nine days. [[Creative Science#CR-291|CR-291]], T3, new on 11 November. Jon Loomer published the control architecture he runs over AI-produced Meta ads. The useful part is not the tool list.

## 1. The mechanism

One sentence in that transcript is the whole lesson. Without operator-specific input, he says, the output is "generic and based on the average of advertising advice found on the internet."

Read that twice, because it names a failure mode precisely. A language model asked to write an ad with no constraints does not produce a bad ad. It produces the **average** ad. Every structure, every opening, every proof placement, weighted by how often it appears in everything ever written about advertising. The output is competent, and competence is the problem. The average is the one position in the auction that cannot win, because it is free and everyone can reach it.

The analogy maps exactly. You hire someone who has read every marketing book ever printed and has never met one of your customers. Ask for an ad and you get the composite of every book: the structure all of them agree on, the words all of them use. Nothing is wrong with it. Nothing in it came from your business either. What makes that hire useful is your rule book, your customer, and the stack of drafts you already rejected.

So the seven controls he names are all one control applied at seven places: force operator-specific input into the pipeline before the pipeline produces anything.

1. A written rule book for how ads get planned, updated every time he corrects something.
2. Named adversarial roles, copywriters and creative directors and designers and an auditor, each told to push back.
3. Voice fitted from his own corpus, hundreds of pages of his own blog posts, in place of a described tone.
4. A maintained list of his own AI-tell words, supplied as a block list.
5. A voice-editor role auditing every piece of copy against that corpus.
6. One reviewer whose single job is catching AI-looking visuals, run twice: once on the design plan before any image exists, once on the finished assets.
7. Three human approval gates after two automated rounds.

His own consequence of control 1 is the right way round and worth repeating: "the ads I'm creating early are bound to be the worst ads that I create." The rule book is the asset. The pipeline is the thing it governs.

## 2. The evidence

CR-291 is **T3**, and the guards on it are heavy. One operator, zero numbers, no control arm, no window, no spend, no sample. The episode closes on a paid-membership promotion. The only quantity anywhere in 1,494 words is cycle time, "a couple of hours start to finish."

Here is the part that is new to this series, and it is a rule about reading tiers rather than a rule about ads. **A claim's tier limits what you may assert. It does not limit what you may build.**

CR-291 describes an architecture. You can build an architecture from a T3 with no numbers, because the question "does this pipeline have a voice reference" is answered by looking at the pipeline, and no measurement is required to answer it. What you may never do is quote CR-291 as evidence that the architecture works, because nobody measured that.

The same transcript proves why the distinction has to be enforced. [[Creative Science#CR-169|CR-169]] holds that nobody in the AI-creative literature has compared AI creative against non-AI creative, so every stated advantage is a production-cost claim. Loomer walked straight into it. He asserts outright: "I'm actually getting better results than I was with the ads I created myself." No cost per result. No spend. No window. No sample. No control. The comparison is against his own memory of his own earlier work.

That is the first outright "better results" sentence from a high-credibility Meta operator, and it arrives with the same evidence shape as every other AI-creative claim on file. **CR-169's rule is unchanged: we never write that AI creative performs better.**

Where the rest of the file sits:

- [[Creative Science#CR-168|CR-168]] is **T2**, the only AI-creative numbers on screen anywhere: $2.2M of sales on just over $1M of spend across a month of AI-only ads. No control period, no margin, no attribution basis. A 2.2x blend on a $1M spender is unremarkable in its own right, so it establishes capability and says nothing about efficiency.
- [[Creative Science#CR-249|CR-249]] is **T3** and the closest attempt on file at the actual comparison: three arms, all-AI worst, AI-hook-then-real-footage best, and the operator reports the ranking since reversing as AI stopped being novel. Recalled from memory about a period six months before recording, no numbers.
- [[Meta Delivery & Andromeda#MD-124|MD-124]] is **T1** on the thing that creates the pressure: ten creatives inside one ad object, multiplied again by aspect ratios. That is more creative than a one-or-two-ads-at-a-time operator makes by hand, which is why this problem arrived at all.

## 3. Our accounts

Map our own stack against his seven. Six of them we already run, and five of those are executable scripts rather than good intentions.

**Control 1, the rule book, is our strongest.** Six law files sit in `orchestrator/references`, and every one is dated to the correction that caused it. The Anti-Slop Law was written on 14 August 2026, the day a client rejected 45 ChiropracticWorks captions in one line: "too AI generated with too much text." Every one of those 45 had passed the Meta compliance gate and scored 33 or higher out of 35 on the caption scorecard. Both gates were per-caption, so nothing looked across the batch. Measured after the fact: 45 of 45 opened with the exact string "Collinsville, IL:", 8 sentences repeated verbatim 15 times or more, 3 distinct structural shapes across 45 captions, 0 of 45 written in a human first-person voice. That is Loomer's mechanism sentence arriving as a client email fourteen months before he said it.

**Control 4, the block list, is real and executable.** `slop_check.py` carries 35 AI-tell phrases, 6 contrast-negation patterns and 6 hedges.

**Control 5, the voice audit, exists as five scripts** in place of a role: slop, plain, flow, turn and episode. Exit 0 ships, exit 1 rewrites.

**Control 6 we do not have at all, and that is today's finding.** All five gates read text. Every one of them. The image side has `adkit.py`, and its preflight checks safe zones, element placement and contrast ratios, which is geometry and legibility. Nothing in it can tell whether the photograph underneath looks AI-generated.

The cost of that gap is already written down, three times, in Lucky's own corrections:

| Date | What was caught | Who caught it |
|---|---|---|
| 16 Sep 2026 | Three built statics killed in one line, paper as the subject, a dated premise | Lucky, after the images existed |
| 1 Oct 2026 | SJR x Vanguard hook character, "the character is average and not looking so good" | Lucky, after the takes were generated |
| Jul 2026 | SJR's whole static set reading as AI: waxy over-sharpened skin, compositor at brightness 1.02 to 1.04 and contrast 1.04 to 1.05 | Lucky, after the finals were built |

Every one of those is control 6 performed by a human pair of eyes, downstream, on finished assets. Note what control 6 does that none of our catches did: it runs **twice**, and the first run is on the design plan before a single image exists. Paper as the subject is visible in a design plan. It costs nothing to catch there.

**Control 7, the human approval gates, is built and currently offline.** Creative Engine has been down since 10 November on a Vercel Hobby blob block that lifts 10 December.

Does any of this touch a number? Phoenix Truxx is the account where it shows. 34 live ads with 6 taking 80% of October spend, about 4 new ads shipped all month, and 5% of the last seven days' spend on creative under 30 days old against a 25% target. Lesson 078 established what that did to the price: cost per opt-in rose 51% across four months at flat spend, $12.18 in August to $18.37 in October. The pipeline that is supposed to fill that gap is an AI pipeline, and the gate it passes through checks only the words.

[[Creative Science#CR-119|CR-119]] and [[Creative Science#CR-024|CR-024]] price the alternative: roughly $300 per concept at agency rates, and 3 to 4 net-new creatives a month at our spend bracket. The production-cost case for AI creative is genuinely established and it is the only part that is. CR-291 is what makes the cheap pipeline produce something other than the average.

## 4. The decision rule

**Build from a T3 architecture freely and quote it as evidence never, and before shipping any AI-produced batch, check that the operator-specific input went in at every stage the output can go generic, including the one stage our gates cannot read.**

## 5. Quiz

Drop your answers in `_answers-inbox.md` with the lesson number.

1. CR-291's mechanism sentence says that without operator-specific input the output is "generic and based on the average of advertising advice found on the internet." Explain in one plain sentence why an average ad is a losing ad in an auction, without using the word average.

2. CR-291 is T3 with zero numbers, no control arm and a membership promotion at the end of the episode. State the one thing you are allowed to do with it and the one thing you are forbidden from doing with it, and say why the tier permits the first.

3. Our five executable gates are slop, plain, flow, turn and episode, and `adkit.py` runs a preflight on every composited image. A teammate says the image side is covered because preflight passes on every asset. Correct him in three sentences, naming what preflight actually measures.

4. On 16 September three built statics were killed for using paper as the subject. CR-291's control 6 runs twice, and the first run happens before any image exists. Say which of those two runs would have caught the paper premise, what it would have cost to catch it there, and what that implies about where to put our missing gate.

5. Phoenix Truxx ran about 4 new ads in October and put 5% of its last week's spend on creative under 30 days old against a 25% target, while cost per opt-in rose from $12.18 to $18.37 across four months at flat spend. Someone proposes closing that gap by pointing the AI pipeline at the dump lane and shipping 20 new statics next week. Using CR-169 and CR-291, say what you would agree to, what you would refuse to write in the client report, and the one control you would build first.

> [!note]- Answer key
>
> **1.** An ad every competitor can produce for free carries no reason for the auction to prefer it, so it competes only on price and the platform has no signal that it will hold attention better than the next one. Full credit for naming that the position is reachable by everyone, which is what strips it of advantage.
>
> **2.** Allowed: **build the architecture from it.** Forbidden: **cite it as evidence that the architecture improves performance.** The tier permits building because CR-291 describes a structure rather than an outcome, and "does this pipeline have a voice reference fitted from our own corpus" is answered by inspecting the pipeline, with no measurement required. The outcome claim needs measurement and nobody supplied any, which is exactly the shape [[Creative Science#CR-169|CR-169]] catalogues.
>
> **3.** Preflight measures **geometry and legibility**: safe-zone compliance, element placement inside the Meta bands, and text contrast ratios. It operates on the composited text layer and knows nothing about the photograph underneath it. So a waxy over-sharpened AI face in the correct position with passing contrast clears preflight at full marks, which is what happened to SJR's set in July.
>
> **4.** The **first** run, on the design plan, before any image exists. Cost to catch it there is one line of review on a written plan, against three fully built statics thrown away on 16 September. The implication is that our missing gate belongs at the concept-lock step rather than at the asset-review step, because the premise defects (paper, off-ICP casting, wrong setting) are all legible in words before any pixels are generated. Credit also for noting that the second run is still needed, since realism defects like waxy skin and a compositor pushed past 1.0 only exist once the image does.
>
> **5.** Agree to the volume. The production-cost case is the established one, CR-119 and CR-024 price the conventional alternative near $300 a concept, and Phoenix's problem is genuinely a creative-supply problem. Refuse to write that the AI creative will perform better, or that it caused any improvement that follows, because CR-169's rule holds and no source in the codex has shown that comparison. The control to build first is **CR-291 control 6, the visual review on the design plan**, because the batch is statics for a truck dealership where every one of our three recorded AI-look failures lived, and it is the only one of the seven we have zero of. Credit for also naming the matched-pair test CR-169 asks for: one conventionally produced asset per concept in the same ad set, which costs one extra asset and would start closing the gap on our own book.
