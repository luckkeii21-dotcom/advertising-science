# -*- coding: utf-8 -*-
"""Claim merge for the 2026-10-07 research pass.

Sources actually read in full this pass:
  - Professor Charley T, "Your Black Friday Facebook Ads Strategy Sucks",
    2026-10-06, 51 min, 8,643-word auto-transcript.
  - Andrew Faris, "The Black Friday Offer & Website Playbook From Intelligems'
    CEO" (guest: Drew Marconi, Intelligems), 2026-10-05, 8,703 words.
  - Meta for Business, "Advertising Week New York 2026: New AI Capabilities to
    Guide Campaigns and Reach Customers", 2026-10-06.
  - Google Merchant Center changelog entry, "Loyalty program updates: Loyalty
    Customer Match via Merchant API", 2026-09-24.
"""
import io, os, re, sys

SCI = r"E:\claude code marketing skill\Obsidian God-level Marketing Vault\God-level Marketing\wiki\science"

def read(f):
    with io.open(os.path.join(SCI, f), encoding="utf-8") as h:
        return h.read()

def write(f, t):
    with io.open(os.path.join(SCI, f), "w", encoding="utf-8", newline="") as h:
        h.write(t)

def append(fname, block):
    t = read(fname)
    if not t.endswith("\n"):
        t += "\n"
    write(fname, t + "\n" + block.strip() + "\n")
    print("APPENDED -> %s : %s" % (fname, block.strip().splitlines()[0][:95]))

def amend(fname, claim_id, insert):
    """Insert text immediately before the claim's 'Sources:' line."""
    t = read(fname)
    m = re.search(r"(?m)^### %s\b.*?(?=^### |\Z)" % re.escape(claim_id), t, re.S)
    if not m:
        print("!! NOT FOUND: %s in %s" % (claim_id, fname)); return False
    block = m.group(0)
    sm = re.search(r"(?m)^Sources:", block)
    if not sm:
        print("!! NO Sources LINE: %s" % claim_id); return False
    new = block[:sm.start()] + insert.strip() + "\n" + block[sm.start():]
    new = re.sub(r"(?m)^Last touched: .*$", "Last touched: 2026-10-07", new)
    write(fname, t[:m.start()] + new + t[m.end():])
    print("AMENDED  -> %s : %s" % (fname, claim_id))
    return True

RUN = r"E:\claude code marketing skill\.claude\skills\advertising-science\runs\2026-10-07"

def load(fn):
    with io.open(os.path.join(RUN, fn), encoding="utf-8") as h:
        return h.read()

# ---- appends
txt = load("new-claims.md")
parts = re.split(r"(?m)^@@APPEND:(.+?)@@$", txt)
for i in range(1, len(parts), 2):
    target, body = parts[i].strip(), parts[i + 1].strip()
    if body:
        append(target, body)

# ---- amendments
txt = load("amendments.md")
parts = re.split(r"(?m)^@@AMEND:(.+?):([A-Z]{2}-\d+)@@$", txt)
for i in range(1, len(parts), 3):
    target, cid, body = parts[i].strip(), parts[i + 1].strip(), parts[i + 2].strip()
    if body:
        amend(target, cid, body)

print("\nMERGE COMPLETE")
