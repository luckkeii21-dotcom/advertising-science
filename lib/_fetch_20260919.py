import re, urllib.request, html, sys
UA=("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/127.0 Safari/537.36")
def get(url,timeout=60):
    req=urllib.request.Request(url,headers={"User-Agent":UA,"Accept":"*/*"})
    with urllib.request.urlopen(req,timeout=timeout) as r:
        return r.status, r.read().decode("utf-8","replace")
def text(h):
    h=re.sub(r"(?is)<(script|style|noscript)[^>]*>.*?</\1>"," ",h)
    h=re.sub(r"(?i)</(p|div|h\d|li|br)>","\n",h)
    h=re.sub(r"<[^>]+>"," ",h)
    h=html.unescape(h)
    h=re.sub(r"[ \t]+"," ",h)
    h=re.sub(r"\n\s*\n+","\n",h)
    return h.strip()
for url in sys.argv[1:]:
    try:
        st,b=get(url)
        print("="*100)
        print(url,"status",st,"bytes",len(b))
        print("-"*100)
        print(text(b)[:9000])
    except Exception as e:
        print("="*100); print(url,"ERROR",e)
