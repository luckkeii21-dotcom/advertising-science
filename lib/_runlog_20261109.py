# Repair the Publish section of the 2026-11-09 research run log.
import io

P = r"E:\claude code marketing skill\.claude\skills\advertising-science\runs\2026-11-09-research-log.md"
s = io.open(P, encoding="utf-8").read()

OLD = """Vault committed and pushed to  as , "Science research run 2026-11-09: Marketing API
v27.0, GA-100, AT-134". The AU-084, GA-073 and GA-100 edits had already been swept up by the vault auto-commit hook at
16:27 () before the manual commit, so they are on the same branch under two commits rather than one.

: **team repo sync pushed, 1,417 claims. Personal mirror pushed.**
"""
NEW = """Vault committed and pushed to `god-level-marketing-vault` as `57a9deb`, "Science research run 2026-11-09: Marketing
API v27.0, GA-100, AT-134". The AU-084, GA-073 and GA-100 edits had already been swept up by the vault auto-commit
hook at 16:27 (`01e00e9`) before the manual commit, so they sit on the same branch under two commits rather than one.

`bin/Sync-TeamRepo.ps1`: **team repo sync pushed, 1,417 claims. Personal mirror pushed.**
"""
assert s.count(OLD) == 1, s.count(OLD)
s = s.replace(OLD, NEW)
io.open(P, "w", encoding="utf-8", newline="").write(s)
print("publish section repaired")
