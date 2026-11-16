import re, urllib.request, collections
UA=("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36")
URLS={"us":"https://www.facebook.com/business/news?locale=en_US",
      "uk":"https://en-gb.facebook.com/business/news"}
MON=r"(January|February|March|April|May|June|July|August|September|October|November|December)"
PATS=[re.compile(MON+r"\s+(\d{1,2})(?:st|nd|rd|th)?,\s+(20\d\d)"),
      re.compile(r"(\d{1,2})(?:st|nd|rd|th)?\s+"+MON+r"\s+(20\d\d)")]
for k,u in URLS.items():
    try:
        req=urllib.request.Request(u, headers={"User-Agent":UA,"Accept":"*/*","Accept-Language":"en-US,en;q=0.9"})
        with urllib.request.urlopen(req, timeout=90) as r:
            st=r.status; body=r.read().decode("utf-8","replace")
    except Exception as e:
        print(k.upper(),"FETCH FAIL:",type(e).__name__,e); continue
    open(f"cache/bn-{k}-20261116.html","w",encoding="utf-8").write(body)
    print(k.upper(),"HTTP",st,len(body),"bytes")
    slugs=[]
    for m in re.finditer(r'/business/news/([a-z0-9\-]+)', body):
        s=m.group(1)
        if s not in slugs: slugs.append(s)
    print("  slugs:",len(slugs))
    for s in slugs: print("   -",s)
    dates=[]
    for p in PATS:
        for m in p.finditer(body):
            g=m.groups()
            dates.append(f"{g[0]} {g[1]} {g[2]}")
    print("  date matches:",len(dates),"distinct:",len(set(dates)))
    print("  distinct:",sorted(set(dates)))
