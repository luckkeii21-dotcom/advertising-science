"""Quote verifier for the Advertising Science Engine.

Reads a TSV of  <transcript-path>\t<quote>  and confirms each quote appears
VERBATIM in the file body. Whitespace is normalised (transcripts are one long
line), but no character, casing or word-level change is tolerated.

Usage: python _verify_quotes.py <tsv-file>
Exit 0 = every quote verified. Exit 1 = at least one failed.
"""
import io, os, re, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")


def norm(s):
    s = s.replace("’", "'").replace("‘", "'")
    s = s.replace("“", '"').replace("”", '"')
    s = s.replace("—", "-").replace("–", "-")
    return re.sub(r"\s+", " ", s).strip()


def main(tsv):
    rows = [l for l in open(tsv, encoding="utf-8").read().splitlines() if l.strip()]
    bodies = {}
    ok = fail = 0
    for i, line in enumerate(rows, 1):
        path, _, quote = line.partition("\t")
        path, quote = path.strip(), quote.strip().strip('"')
        if not quote:
            continue
        if path not in bodies:
            if not os.path.exists(path):
                print(f"{i:3} MISSING FILE  {path}")
                fail += 1
                continue
            bodies[path] = norm(open(path, encoding="utf-8").read())
        if norm(quote) in bodies[path]:
            ok += 1
        else:
            fail += 1
            print(f"{i:3} FAIL  {os.path.basename(path)[:55]}")
            print(f"     quote: {quote[:150]}")
            # locate the longest verbatim prefix so the drift is visible
            q = norm(quote)
            lo, hi = 0, len(q)
            while lo < hi:
                mid = (lo + hi + 1) // 2
                if q[:mid] in bodies[path]:
                    lo = mid
                else:
                    hi = mid - 1
            print(f"     longest verbatim prefix ({lo} chars): {q[:lo][-90:]!r}")
            print(f"     first divergence at: {q[lo:lo+70]!r}")
    print(f"\nVERIFIED {ok}  FAILED {fail}  TOTAL {ok+fail}")
    return 1 if fail else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
