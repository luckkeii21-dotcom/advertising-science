"""2026-08-27 research pass, part 3: two remaining creative entries."""
import io
from pathlib import Path

SCI = Path(r"E:\claude code marketing skill\Obsidian God-level Marketing Vault\God-level Marketing\wiki\science")

CR = r'''
### CR-193 · Putting the exact clicked video at the top of the landing page: three accounts, and not one performance number
Tier: T3 · Status: active
Pairs directly with the LP-versus-PDP result at [[Creative Science#CR-189|CR-189]], and it is the mechanism-free version of the same idea: make the page continuous with the ad.
**The spec, which is concrete enough to build from.** Above the fold sits "a full 4x5 view of the video that they just clicked on playing in real time in the background with no noise", with a sticky add-to-cart and price laid over it, and listicle-style education below. The stated failure it replaces is one page serving every angle: "they all land on the same landing page, which then has 5,000 benefits listed".
**⚠ The evidence is a spend level, not a result, and this is the whole guard.** The only figure in the file is "We took them from spending pretty much nothing to $1,000 a day within about a 7-day period". **Spend is an INPUT.** There is no ROAS, no CPA, no conversion rate, no AOV and no click-through rate anywhere in the transcript. Breadth is asserted without measurement too: "We've now tested this on three separate accounts and seen really good success across all of them", with no test design, control or metric for any of the three.
**So the honest statement is that a named operator scaled an account to $1,000/day within a week of shipping this page and attributes it to the page. That is a hypothesis worth testing, not a result.**
He predicts his own tactic decays once page generation is automated: "I think that this opportunity will probably just be arbitrageed out of the market." He also names the reason nobody tests upper-funnel page strategies, which is a measurement problem rather than a creative one: you "just can't run strategies like that without being able to have clarity over the incremental impact".
Sources: Blue Sense Digital, New Strategy To Scale Meta Ads Faster, 2025-05-02
Last touched: 2026-08-27

### CR-194 · Segmenting creative by PURCHASE TRIGGER rather than by brand message, and an audience that opened 25 years younger
Tier: T3 · Status: active
A Google-agency account team describing the same move law 1 describes from the Meta side, reached independently.
**The core claim:** "It was really when we segmented out these campaigns in our ads by purchase trigger, by pain point that we saw significant growth." **NO NUMBER GIVEN**, here or anywhere in the file.
**The concrete case is the useful part.** A fashion brand where "their core demographics for the past 50 years has been women 60 plus" opened women 35-60 by reframing the product as an investment purchase, in language borrowed from competitor messaging, without changing the product. The reported outcome is hedged by the speaker herself: "we definitely saw that demographic has you know grown exponentially in the past three months". **NO NUMBER GIVEN.**
**They also state law 1's mechanism in weaker, more careful terms than most operators use, and the hedge is worth copying:** "Meta at times can even take your creative and your ad copy into account when showing your ad to users." **"At times" and "can even" is a more honest statement of what [[Meta Delivery & Andromeda#MD-120|MD-120]] actually documents than the flat "creative is the targeting" shorthand.**
**Two operating rules with nothing behind them but both cheap.** A refresh must be a genuine change: "We never want to launch one version of creative and launch the same thing a month later with no changes". And demographic-matched creative decays if every segment lands on the same page, which is the post-click half of [[Creative Science#CR-189|CR-189]].
**Guards, and they are the story of this file.** Every claim is unquantified. The portfolio-level summary is the emptiest sentence in this pass: "we saw really, really great success out of the gate. really significant year-over-year gains." **A prospecting frequency range of "three or four" is offered with no window and no source.**
**⚠ It also conflicts with [[Scaling Models#SC-149|SC-149]].** Jon Loomer's qualifying test for any demographic restriction is that your data contains something Meta lacks, at lifetime-value grade. No LTV data appears here. Note the conflict is narrow: they are segmenting CREATIVE by demographic, which Loomer never objects to, and also recommending hard demographic targeting, which he does.
Sources: Solutions 8, eCommerce Success with Demographic-Focused Creatives, 2025-09-15
Last touched: 2026-08-27
'''

with io.open(SCI / 'Creative Science.md', 'a', encoding='utf-8') as f:
    f.write(CR)
print("appended -> Creative Science.md")
