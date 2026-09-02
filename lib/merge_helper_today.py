"""Claim merge helper for the Advertising Science codex.

Two operations, both idempotent-checked:
  amend(file, claim_id, paragraph, new_sources, tier=None, status=None)
      inserts `paragraph` immediately before the claim's `Sources:` line,
      appends `new_sources` to that line, and stamps `Last touched`.
  mint(file, claim_id, title, tier, status, body, sources)
      appends a brand-new claim block at the end of the topic file.

Refuses to write if the claim ID is missing, if the paragraph is already
present (double-run guard), or if a minted ID already exists.
"""
import re
from pathlib import Path

BASE = Path(r"E:\claude code marketing skill\Obsidian God-level Marketing Vault"
            r"\God-level Marketing\wiki\science")
TODAY = "2026-09-02"
DOT = "·"  # the middle dot the codex uses in headings and tier lines


def _read(fn):
    return (BASE / fn).read_text(encoding="utf-8")


def _write(fn, t):
    (BASE / fn).write_text(t, encoding="utf-8")


def _block(text, claim_id):
    """Return (start, end) span of the claim block for claim_id."""
    m = re.search(r"^###\s+" + re.escape(claim_id) + r"(?![0-9A-Za-z-])",
                  text, re.M)
    if not m:
        raise KeyError(f"claim {claim_id} not found")
    nxt = re.search(r"^###\s", text[m.end():], re.M)
    end = m.end() + nxt.start() if nxt else len(text)
    return m.start(), end


def amend(fn, claim_id, paragraph, new_sources=(), tier=None, status=None):
    text = _read(fn)
    s, e = _block(text, claim_id)
    block = text[s:e]

    probe = paragraph.strip()[:70]
    if probe and probe in block:
        print(f"  SKIP {claim_id}: paragraph already present")
        return False

    m = re.search(r"^Sources:(.*)$", block, re.M)
    if not m:
        raise ValueError(f"{claim_id}: no Sources line")

    existing = m.group(1).strip()
    add = [s_ for s_ in new_sources if s_ not in existing]
    src_line = "Sources:" + (" " + existing if existing else "")
    if add:
        src_line += ("; " if existing else " ") + "; ".join(add)

    new_block = block[:m.start()] + paragraph.strip() + "\n" + src_line + block[m.end():]
    new_block = re.sub(r"^Last touched:.*$", f"Last touched: {TODAY}", new_block, flags=re.M)

    if tier or status:
        def fix(mo):
            t = tier or mo.group(1)
            st = status or mo.group(2)
            return f"Tier: {t} {DOT} Status: {st}"
        new_block = re.sub(r"^Tier:\s*(T\d)\s*.\s*Status:\s*(\w+)", fix,
                           new_block, count=1, flags=re.M)

    _write(fn, text[:s] + new_block + text[e:])
    print(f"  amended {claim_id}" + (f"  [{tier or ''}{'/' if tier and status else ''}{status or ''}]"
                                     if (tier or status) else ""))
    return True


def mint(fn, claim_id, title, tier, status, body, sources):
    text = _read(fn)
    if re.search(r"^###\s+" + re.escape(claim_id) + r"(?![0-9A-Za-z-])", text, re.M):
        print(f"  SKIP {claim_id}: already exists")
        return False
    entry = (f"\n### {claim_id} {DOT} {title}\n"
             f"Tier: {tier} {DOT} Status: {status}\n"
             f"{body.strip()}\n"
             f"Sources: {'; '.join(sources)}\n"
             f"Last touched: {TODAY}\n")
    _write(fn, text.rstrip("\n") + "\n" + entry)
    print(f"  minted {claim_id} [{tier}/{status}]")
    return True


def audit():
    """Recompute counts from the topic files. Never carry counts forward."""
    import collections
    tiers, stat = collections.Counter(), collections.Counter()
    total = 0
    per = {}
    for f in sorted(BASE.glob("*.md")):
        t = f.read_text(encoding="utf-8", errors="replace")
        ids = re.findall(r"^###\s+([A-Z]{2}-\d+[a-z]?)", t, re.M)
        if not ids:
            continue
        per[f.name] = len(ids)
        total += len(ids)
        for a, b in re.findall(r"^Tier:\s*(T\d)\s*.\s*Status:\s*(\w+)", t, re.M):
            tiers[a] += 1
            stat[b] += 1
        dupes = [k for k, v in collections.Counter(ids).items() if v > 1]
        if dupes:
            print(f"  !! DUPLICATE IDS in {f.name}: {dupes}")
    return total, dict(tiers), dict(stat), per
