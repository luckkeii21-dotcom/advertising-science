import re, sys, json, urllib.request, collections, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from watchlist_check import BANK_RE
url=("http://export.arxiv.org/api/query?search_query=cat:cs.IR"
     "&sortBy=submittedDate&sortOrder=descending&max_results=250")
raw=urllib.request.urlopen(url, timeout=120).read().decode("utf-8","replace")
open("cache/arxiv-api-csir-20261115.xml","w",encoding="utf-8").write(raw)
entries=re.findall(r"<entry>(.*?)</entry>", raw, re.S)
rows=[]
for e in entries:
    t=re.search(r"<title>(.*?)</title>", e, re.S)
    s=re.search(r"<summary>(.*?)</summary>", e, re.S)
    p=re.search(r"<published>(.*?)</published>", e)
    i=re.search(r"<id>(.*?)</id>", e)
    rows.append({"date":p.group(1)[:10],"title":" ".join(t.group(1).split()),
                 "abs":" ".join(s.group(1).split()),"id":i.group(1)})
print("entries:",len(rows),"newest:",rows[0]["date"] if rows else None)
hist=collections.Counter(r["date"] for r in rows)
for d in sorted(hist,reverse=True)[:8]: print(" ",d,hist[d])
window=[r for r in rows if r["date"]>="2026-11-11"]
print("since 2026-11-11:",len(window))
hits=[r for r in window if BANK_RE.search(r["title"]+" "+r["abs"])]
print("passed bank filter:",len(hits))
for h in hits: print("  *",h["date"],h["id"],h["title"])
