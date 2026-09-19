import re, urllib.request, pathlib, json
UA=("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/127.0 Safari/537.36")
def get(url,timeout=45):
    req=urllib.request.Request(url,headers={"User-Agent":UA,"Accept":"*/*"})
    with urllib.request.urlopen(req,timeout=timeout) as r:
        return r.status, r.read().decode("utf-8","replace")

CACHE=pathlib.Path(r"E:\claude code marketing skill\.claude\skills\advertising-science\cache")
ANN="https://support.google.com/google-ads/announcements/9048695"
st,body=get(ANN)
fresh=set(re.findall(r"/google-ads/answer/(\d+)",body))
cached=set(re.findall(r"/google-ads/answer/(\d+)",(CACHE/"google-ads-announcements-today.html").read_text(encoding="utf-8",errors="replace")))
print("GOOGLE ANNOUNCEMENTS status",st)
print("fresh ids",len(fresh),"cached ids",len(cached))
print("added",sorted(fresh-cached))
print("removed",sorted(cached-fresh))
# second fetch to confirm stability
st2,body2=get(ANN)
fresh2=set(re.findall(r"/google-ads/answer/(\d+)",body2))
print("second fetch ids",len(fresh2),"identical:",fresh2==fresh)
pathlib.Path(CACHE/"_google-ann-fresh-20260919.html").write_text(body,encoding="utf-8")
