# -*- coding: utf-8 -*-
"""Second 2026-08-29 pass: the two Jon Loomer transcripts."""
import pathlib
import re
S = pathlib.Path(r'Obsidian God-level Marketing Vault/God-level Marketing/wiki/science')
TODAY = '2026-08-29'


def read(fn):
    return (S / fn).read_text(encoding='utf-8')


def write(fn, t):
    (S / fn).write_text(t, encoding='utf-8')


def amend(fn, cid, add_body=None, add_source=None, new_status=None):
    lines = read(fn).split('\n')
    start = None
    for i, l in enumerate(lines):
        if re.match(r'^### ' + re.escape(cid) + r'[ ·\-]', l):
            start = i
            break
    if start is None:
        raise SystemExit('claim not found: ' + cid + ' in ' + fn)
    end = len(lines)
    for j in range(start + 1, len(lines)):
        if lines[j].startswith('### '):
            end = j
            break
    blk = lines[start:end]
    si = li = None
    for k, l in enumerate(blk):
        if l.startswith('Sources:'):
            si = k
        if l.startswith('Last touched:'):
            li = k
    if si is None or li is None:
        raise SystemExit('no Sources/Last touched in ' + cid)
    if new_status is not None:
        blk[1] = re.sub(r'Status: \w+', 'Status: ' + new_status, blk[1])
    if add_body:
        blk[si:si] = [add_body.strip()]
        si += 1
        li += 1
    if add_source:
        blk[si] = blk[si].rstrip() + '; ' + add_source
    blk[li] = 'Last touched: ' + TODAY
    lines[start:end] = blk
    write(fn, '\n'.join(lines))
    print('amended', cid)


amend('Attribution & Incrementality.md', 'AT-066', add_body=(
    "**A second named operator on the same position, added 2026-08-29, and he converts it from a verdict into a "
    "procedure.** Jon Loomer's list of the excuses he reads most often is precisely the set this claim rejects: seasonal "
    "downturns, Meta outages, Advantage+ enhancements switching themselves on, and \"I can't target the people I want "
    "because Meta keeps reaching whoever they want\". **His concession is important and matches Faris's: these are not "
    "fictional.** \"It's not that there isn't a little bit of truth in all these complaints, which is why they're popular "
    "in the first place ... There are outages. Now, that doesn't mean they're always impacting you.\" The test he applies "
    "is whether the thing is actionable, not whether it is real.\n"
    "**The diagnostic ladder he substitutes, which is the transferable part.** First, read the BREAKDOWNS before forming "
    "any theory, specifically \"by time, demographics, platform, placement, and location\", to isolate where delivery or "
    "performance actually shifted. Then apply a fix from a list whose members are chosen because they follow from how the "
    "system works rather than from folklore: campaign and budget consolidation, the performance goal, Advantage+ settings, "
    "and value rules \"when you have information that Meta doesn't\". Then check the things on your own side that get "
    "skipped, event tracking, the conversions API, the landing page and site performance. **His stated prior is that the "
    "cause is usually local: \"We love to think something Meta did change everything. It's typically something on our end "
    "that we haven't thought about.\"**\n"
    "**And the ending he gives when the breakdowns come back clean, which is the half operators resist.** \"This ad has "
    "worked for months and then it just stopped working\" is, once nothing shows in the breakdowns, most often simply true: "
    "\"it's entirely possible the ad just isn't that effective anymore. Stop trying to force your favorite ad to work.\" "
    "That routes the diagnosis back into creative rather than into settings. **He also names the professional cost, which "
    "is why this belongs in a client-facing codex: \"Are you seriously going to tell a client it's Meta's fault?\"** "
    "Asserted from long practice, no data, and it is an opinion piece rather than a test. It earns its place by "
    "independently reproducing Faris's conclusion from a different account and adding an ordered checklist Faris does not "
    "give."),
    add_source='Jon Loomer, Your Excuses Are Holding Back Your Results, 2026-04-20')

amend('Learning & Signal.md', 'LS-025', add_body=(
    "**The asset-ownership structure this argument keeps assuming, stated explicitly and independently, added 2026-08-29.** "
    "Jon Loomer answers the onboarding question directly and the answer is our standing rule. **The client must own their "
    "own Business Manager and every asset inside it**, ad account, Page, Instagram account, pixel and other data sets, and "
    "catalogue. The named mistake is the agency creating any of those under its own Business Manager: \"Do not do this.\" "
    "The agency is then added as a PARTNER, never as a person, which is what an employee would be. **Three reasons he "
    "gives, and they run in both directions:** the partner boundary insulates the agency from whatever the client does and "
    "the client from whatever is happening in the agency's other accounts, up to and including account bans; and it "
    "guarantees the client keeps their assets when the relationship ends, which he notes always eventually happens. Access "
    "level is then scoped per asset: partial access on the ad account (manage campaigns, view performance, manage "
    "mock-ups) with full control flagged as rare because it exposes settings, finance and permissions; full control "
    "typically wanted on catalogue, custom conversions and data sets; Page and Instagram access set by whether the agency "
    "handles messages and comments. The agency then adds its own staff as people inside its own Business Manager. **Shared "
    "login credentials are ruled out entirely.** This is the practical form of the ownership argument recorded in the "
    "contested note above: whichever level the accumulated learning actually lives at, this structure is what keeps it "
    "with the client. Prescriptive, restating Meta's documented partner model; no data and none needed."),
    add_source='Jon Loomer, Are You Setting Up Client Access the Wrong Way?, 2026-04-29')

print('second merge complete')
