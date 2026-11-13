# Amendments for the 2026-11-13 research run: AT-022, AT-023, AT-125.
# Line-anchored (insert immediately before each claim's own Sources: line) so
# the repeated "Sources: Andrew Faris, DTC Brands..." string cannot mis-target.
import io

AT = (r"E:\claude code marketing skill\Obsidian God-level Marketing Vault"
      r"\God-level Marketing\wiki\science\Attribution & Incrementality.md")

AMEND_022 = """**Amended 2026-11-13: both major platforms now publish this ordering themselves, and they agree with it.** The hierarchy above was built from practitioner reasoning and tiered T3 accordingly. Meta's own measurement series states the same ranking in its own words ([[Attribution & Incrementality#AT-138|AT-138]], May 2025): randomized control experiments "provide the most accurate measure of incrementality", and the job it assigns MTA and MMM is to be calibrated by those experiments rather than to adjudicate between them. Google says the same for Meridian GeoX at [[Attribution & Incrementality#AT-115|AT-115]], and Meta's Chief Data Officer states the sequencing flatly at [[Attribution & Incrementality#AT-136|AT-136]]: run the experiment first, then the model. **The tier here stays T3 and that is deliberate.** Two interested platforms publishing an ordering is agreement, not evidence, and both of them sell the experiment that sits at the top of it. What genuinely changed is that the hierarchy is no longer ours alone to defend to a client. One useful scope limit arrives with it, from Meta: experiments are "particularly effective for single channel evaluations and in-channel optimization", which concedes that the cross-channel allocation question belongs to the calibrated model rather than to any single holdout."""

AMEND_023 = """**Amended 2026-11-13, and Position B just gained a T1 endorser.** Meta's own published calibration recipe ([[Attribution & Incrementality#AT-135|AT-135]], October 2025) prescribes exactly Position B: take one Conversion Lift result, divide lift conversions by attributed conversions, and apply the resulting scalar to that channel "going forward". Meta's worked example is 150/100 = 1.5x. **That is a static per-channel discount factor published by the platform itself**, which moves Position B from one practitioner's working rule to platform doctrine, and it is the most significant movement on this claim since it was opened. **It does not refute Position A and the status stays contested.** Haus's objection is that a factor decays, and Meta's own hedge concedes the same problem without quantifying it: multipliers "should be updated periodically to stay accurate", with no interval, no refresh trigger and no staleness test anywhere in the post. So the T1 lands on the side of the method and says nothing about the frequency, which is the half the disagreement is actually about. Note also that Meta's recipe has no equivalent of Haus's pooling: nothing regresses a noisy single test toward a cross-advertiser index, and Meta's residual step assigns the leftover conversions to organic, which is the opposite of conservative."""

AMEND_125 = """**Amended 2026-11-13: the design wording sharpens, and the refinement is intention-to-treat.** This claim records Meta naming the design as one group seeing the ads and one holdout group not. Meta's 12 November 2026 post ([[Attribution & Incrementality#AT-137|AT-137]]) states it more precisely: Conversion Lift compares outcomes "between people who were eligible to see ads and a randomized holdout group". **Eligibility defines the treated arm, not exposure.** That is the standard intention-to-treat construction, and it matters for reading the output: the measured lift is diluted by everyone eligible who never actually saw an ad, so it is a floor on the effect among the exposed rather than an estimate of it. Meta also hedges the verb in the same sentence, "is designed to measure", and the 2025 root post of the series calls randomized control experiments the "most accurate measure of incrementality" without ever publishing a precision figure. Nothing here changes the duration claim above, which is still the most useful thing in the original post and still falsifiable against our own next study."""

L = io.open(AT, encoding="utf-8").read().split("\n")


def insert_before_own_sources(claim_prefix, text):
    for i, line in enumerate(L):
        if line.startswith(claim_prefix):
            for j in range(i, min(i + 60, len(L))):
                if L[j].startswith("Sources:"):
                    assert text[:40] not in "\n".join(L[i:j]), "already amended"
                    L.insert(j, text)
                    print("inserted into %s at line %d" % (claim_prefix.strip(), j + 1))
                    return
            raise SystemExit("no Sources: line for " + claim_prefix)
    raise SystemExit("claim not found: " + claim_prefix)


# Deepest first so earlier inserts do not shift later targets.
insert_before_own_sources("### AT-125 ", AMEND_125)
insert_before_own_sources("### AT-023 ", AMEND_023)
insert_before_own_sources("### AT-022 ", AMEND_022)

io.open(AT, "w", encoding="utf-8").write("\n".join(L))
print("WROTE amendments")
