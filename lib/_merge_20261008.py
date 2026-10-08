# -*- coding: utf-8 -*-
"""Claim merge for the 2026-10-08 research pass.

Sources actually read in full this pass:
  - Ben Heath, "The BEST NEW Facebook Ads Feature Has Arrived!", 2026-10-07,
    18 min, 4,080-word auto-transcript.
  - Jon Loomer, "A Simple, Volume-Focused Ad Strategy", 2026-10-07, 9 min,
    1,455-word auto-transcript.
  - Meta for Business, "Together creates better: building for a creator-first
    future" (creator marketing white paper), 2026-10-07, read via WebFetch on
    the en_GB shelf in two passes.

Amendments append at the END of a claim block, after the last "Last touched:"
line, which is the convention every pass since 2026-08-25 has used in these
files. The older amend() helper inserted before the FIRST "Sources:" line,
which lands mid-claim on any block that has already been amended once.
"""
import io, os, re, sys

SCI = r"E:\claude code marketing skill\Obsidian God-level Marketing Vault\God-level Marketing\wiki\science"
RUN = r"E:\claude code marketing skill\.claude\skills\advertising-science\runs\2026-10-08"


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


def amend_end(fname, claim_id, insert):
    """Append text at the end of the claim's block, before the next heading."""
    t = read(fname)
    m = re.search(r"(?m)^### %s\b.*?(?=^### |\Z)" % re.escape(claim_id), t, re.S)
    if not m:
        print("!! NOT FOUND: %s in %s" % (claim_id, fname))
        return False
    block = m.group(0).rstrip("\n")
    if "Last touched:" not in block:
        print("!! NO Last touched LINE: %s" % claim_id)
        return False
    new = block + "\n\n" + insert.strip() + "\n\n"
    write(fname, t[:m.start()] + new + t[m.end():])
    print("AMENDED  -> %s : %s" % (fname, claim_id))
    return True


def load(fn):
    with io.open(os.path.join(RUN, fn), encoding="utf-8") as h:
        return h.read()


ok = True

# ---- new claims
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
        ok = amend_end(target, cid, body) and ok

print("\nMERGE COMPLETE" if ok else "\nMERGE COMPLETE WITH FAILURES")
sys.exit(0 if ok else 1)
