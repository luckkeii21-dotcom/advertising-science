# -*- coding: utf-8 -*-
"""Hot-layer update for the 2026-10-20 research run."""
from pathlib import Path

SKILL = Path(r"E:\claude code marketing skill\.claude\skills\advertising-science\SKILL.md")
ANCHOR = ("Updated only when the codex changes at law level. Each law cites its claims; depth lives "
          "in the codex. ")

NEW = (
    "**The 2026-10-20 pass gave law 1 the best T1 sentence it has ever had, and the same post "
    "carries a word that will be misread in every client conversation if it is not pinned down now** "
    "(6 new claims: MD-184, MD-185, MD-186, CR-287, AT-131, AU-100; twelve merges, into MD-001, "
    "MD-022, MD-070, MD-120, MD-171, MD-177, MD-178, MD-179, CR-003, AU-084, AU-085 and AT-130). "
    "Meta published GenRecs Tokenization on 19 October and it was read in full. **The ad's own text "
    "and images are now stated, by Meta, to be what the model reads to build its representation of "
    "the ad**: \"Pre-trained multimodal models read each ad, product, and page, including its text "
    "and images\" (MD-184). Law 1 has been argued for fourteen months off practitioner testimony and "
    "a taxonomy line. This is the pixels, named as an input. The per-item ID is being replaced by a "
    "stable vocabulary of semantic tokens across ads, products, pages and pixels, in both retrieval "
    "and ranking. **\u26a0 And here is the word. \"Generative recommenders\" does NOT mean Meta "
    "retrieves generatively, and it does not mean Meta writes ads.** The paper Meta's own post cites "
    "for its retrieval work, by the post's own first two authors, is titled **\"The Case Against "
    "Generation for Retrieval\"** and concludes that the classic discriminative two-tower "
    "architecture \"remains an exceptionally competitive and practical solution\" (MD-186). What is "
    "generative is the REPRESENTATION. The retrieval mechanism is unchanged. **Never tell a client "
    "Meta generates their ads on the strength of the word generative; the clearest refutation is "
    "Meta's own citation.** **The second real gain is an item-side cold start, which this file has "
    "never had.** MD-179 holds Meta's user-side path, where a missing user-ad pair inherits the "
    "user's own recent embeddings. The item side is now published too: a brand-new ad inherits the "
    "representation of semantically similar items **\"even before anyone sees the new ad\"** "
    "(MD-185). Neither side of the pair starts from zero, and the long argument about new ads taking "
    "no spend has to be read against that. **Cross-campaign transfer is now a Meta sentence, and the "
    "difference from our T3 claim is load-bearing.** Meta says the stable vocabulary lets its models "
    "\"carry insights across campaigns for advertisers\". That is the MODEL's representation of an "
    "item moving, not an ad object's delivery history moving, so MD-070 stays T3 and nobody may read "
    "this as proof that re-uploading a winner skips anything. **Where Meta says the benefit "
    "concentrates is not our book**: large product catalogues and tail inventory, and \"Tail ad "
    "inventory is where semantic tokens contribute most and where advertiser impact is largest\". "
    "Our local service clients have no catalogue; the tail-ad half is the closer fit, because a "
    "four-figure monthly budget accumulates few impressions per ad, and nothing about either group is "
    "quantified. **The number in the post is the smallest Meta has published to this engine, and it "
    "sharpens the footnote rule rather than settling anything.** +0.35% in conversions, jointly "
    "attributed to GenRecs Tokenization, GEM and the Adaptive Ranking Model, so no part of it is "
    "separable. It is the first Meta ads figure in months to carry a footnote at all, and the "
    "footnote reads in full \"Meta Internal Data, measured in February 2026\": a data owner and a "
    "month, with no population, no window, no control and no sample, published eight months after it "
    "was measured. **So the rule changes shape: the presence of a footnote is not the test, the "
    "presence of a population and a counterfactual is** (MD-171). And set it beside MD-177, which "
    "carries GEM's published 18.9% conversion improvement. **Two Meta posts seven days apart, GEM in "
    "both, two orders of magnitude apart, neither saying what the other measures. Neither figure goes "
    "in front of a client and the pair never goes in a forecast.** **One Meta page published eleven "
    "numbers the same week with no footnote at all, and one of its four cases is our vertical.** Four "
    "agency lift studies, no sample, no window, no spend and no eligibility floor on any of them "
    "(AT-131). The dealership case is the one to keep: people who saw Meta ads viewed 7.67 times as "
    "many vehicle listing pages and generated 14% more paid search traffic. **Direction only, the "
    "digits are unusable, and it is T1-adjacent support for the standing rule that a zero-lead "
    "last-click column means no last-click leads attributed and never waste.** We run two commercial "
    "truck dealerships on exactly that reporting. The method is at least a randomised holdout, which "
    "beats the adopter-versus-non-adopter comparison Meta usually publishes, but every parameter of "
    "the design is missing. Google's counterpart shipped as 15 queryable metrics on a campaign "
    "resource the day before (AT-130); Meta shipped case studies. **Two outside papers say the "
    "pre-produced creative set is now the ceiling, and the headline number does not say what it looks "
    "like it says.** A deployed Kuaishou system reports CTR +2.87%, CVR +2.74% and ARPU +9.85% for "
    "per-user generated video creative, **over a generative baseline rather than over retrieval**, so "
    "nothing there quantifies generated creative against a human-made library (CR-287). What is worth "
    "keeping is the shape: ARPU moved three times as hard as CTR, so the value landed downstream of "
    "the click, which is where AU-097 already puts a CPM-down, CPA-up account's losses. **And Meta "
    "named its scaling axes for the first time: sequence length, training data, and model "
    "architecture. Parameter count is absent** (AU-100), which puts a Meta statement on both sides of "
    "the axis distinction AU-085 opened. The reading rule stands unchanged: when a source says "
    "scaling, ask which axis before carrying the claim. "
)


def main():
    text = SKILL.read_text(encoding="utf-8")
    if ANCHOR not in text:
        raise SystemExit("REFUSING: anchor not found in SKILL.md")
    if "MD-184" in text:
        raise SystemExit("REFUSING: law layer already carries today's pass")
    SKILL.write_text(text.replace(ANCHOR, ANCHOR + NEW, 1), encoding="utf-8")
    print(f"hot layer updated, +{len(NEW)} chars")


if __name__ == "__main__":
    main()
