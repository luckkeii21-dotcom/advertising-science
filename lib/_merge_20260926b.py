# -*- coding: utf-8 -*-
"""2026-09-26 merge, part 2.

Part 1 (_merge_20260926.py) landed the two GA-068 / GA-081 amendments and then
stopped on a miss: it expected CRLF in the GA-083 Sources line and that file is
LF. It also inserted two literal CRLF into the GA-081 amendment.

This script:
  1. repairs those two stray CRLF,
  2. applies the GA-083 amendment,
  3. appends GA-085..GA-088 and CR-266, preserving each file's OWN line ending
     instead of rewriting the whole file (Creative Science.md is still CRLF).
"""
import pathlib, sys

V = pathlib.Path("Obsidian God-level Marketing Vault/God-level Marketing/wiki/science")
GA = V / "Google Auction & Smart Bidding.md"
CR = V / "Creative Science.md"

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _merge_20260926 import GA_NEW, CR_NEW, AMEND_GA083_OLD, AMEND_GA083_NEW  # noqa: E402


def read_raw(p):
    with p.open("r", encoding="utf-8-sig", newline="") as f:
        return f.read()


def write_raw(p, s):
    with p.open("w", encoding="utf-8-sig", newline="") as f:
        f.write(s)


def dominant_eol(s):
    return "\r\n" if s.count("\r\n") > s.count("\n") - s.count("\r\n") else "\n"


def main():
    # 1. repair the two stray CRLF left by part 1
    s = read_raw(GA)
    stray = s.count("\r\n")
    if stray:
        s = s.replace("\r\n", "\n")
        write_raw(GA, s)
    print("GA stray CRLF repaired: %d" % stray)

    # 2. GA-083 amendment, LF this time
    old = AMEND_GA083_OLD.replace("\r\n", "\n")
    new = AMEND_GA083_NEW.replace("\r\n", "\n")
    s = read_raw(GA)
    n = s.count(old)
    if n != 1:
        print("GA-083 AMEND FAIL count=%d" % n)
        sys.exit(1)
    write_raw(GA, s.replace(old, new))
    print("amended GA-083")

    # 3. append the new claims, each file in its own line ending
    for path, block in ((GA, GA_NEW), (CR, CR_NEW)):
        s = read_raw(path)
        eol = dominant_eol(s)
        before = len(s)
        body = block.replace("\r\n", "\n").lstrip("\n")
        if eol == "\r\n":
            body = body.replace("\n", "\r\n")
        s = s.rstrip("\r\n") + eol + body
        write_raw(path, s)
        print("%s: eol=%s  %d -> %d chars" % (path.name, repr(eol), before, len(read_raw(path))))


if __name__ == "__main__":
    main()
