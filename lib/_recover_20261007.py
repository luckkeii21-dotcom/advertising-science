"""Recover videos the 2026-10-07 harvest marked out_of_window because the
3-day daily window could not cover the 2026-10-03..06 outage gap."""
import json, os, re, sys, urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime

SKILL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
state = json.load(open(os.path.join(SKILL, "state.json"), encoding="utf-8"))
chans = json.load(open(os.path.join(SKILL, "channels.json"), encoding="utf-8"))
chans = chans["roster"]
CUTOFF = "2026-10-01"

NS = {"a": "http://www.w3.org/2005/Atom",
      "yt": "http://www.youtube.com/xml/schemas/2015"}

found, cleared = [], []
for ch in chans:
    url = f"https://www.youtube.com/feeds/videos.xml?channel_id={ch['channel_id']}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=30) as r:
            tree = ET.fromstring(r.read())
    except Exception as e:
        print(f"[{ch['slug']}] RSS failed: {e}")
        continue
    for entry in tree.findall("a:entry", NS):
        vid = entry.find("yt:videoId", NS).text
        pub = entry.find("a:published", NS).text[:10]
        title = entry.find("a:title", NS).text
        if pub < CUTOFF:
            continue
        st = state["seen"].get(vid, {})
        found.append((ch["slug"], pub, st.get("status", "NOT-SEEN"), vid, title))
        if st.get("status") == "out_of_window":
            del state["seen"][vid]
            cleared.append((ch["slug"], pub, vid, title))

print(f"\n--- videos published >= {CUTOFF} on roster RSS: {len(found)} ---")
for s, p, st, v, t in sorted(found, key=lambda x: x[1], reverse=True):
    print(f"{p}  {st:16s} {s:22s} {t[:70]}")
print(f"\n--- cleared from state for re-fetch: {len(cleared)} ---")
for s, p, v, t in cleared:
    print(f"{p}  {s:22s} {t[:70]}")

if cleared and "--commit" in sys.argv:
    json.dump(state, open(os.path.join(SKILL, "state.json"), "w", encoding="utf-8"), indent=1)
    print("\nstate.json written")
