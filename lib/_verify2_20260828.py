import pathlib, re
R = pathlib.Path(r'Obsidian God-level Marketing Vault/God-level Marketing/wiki/sources/transcripts')
def norm(s):
    return re.sub(r'\s+',' ', s.replace('\u2019',"'").replace('\u2018',"'").replace('\u201c','"').replace('\u201d','"')).lower()
def findall(chan, frag):
    out=[]
    for p in (R/chan).rglob('*.md'):
        if norm(frag) in norm(p.read_text(encoding='utf-8',errors='replace')):
            out.append(p.name)
    return out
CH = [
 ('nick-theriot', "nine times out of ten we're wrong"),
 ('bluesense-digital', "didn't even have audience segments defined in Meta"),
 ('bluesense-digital', "do not launch in the US unless you're doing at bare minimum 3 mil"),
 ('bluesense-digital', "scaling isn't just increasing spend"),
 ('fraser-cottrell', "normally going back and doing label replacement"),
 ('fraser-cottrell', "you can't upload references of people"),
 ('charley-t', "getting bigger by being smaller"),
 ('matt-shiver', "at least one times your cost per call"),
 ('matt-shiver', "cost per call is going to be $200 to $500"),
 ('bluesense-digital', "we run split tests almost every two days"),
 ('bluesense-digital', "over 120 Facebook ad accounts"),
 ('fraser-cottrell', "15,000 plus ads that I've made over my career"),
]
for c,f in CH:
    h=findall(c,f)
    print(('OK  ' if h else 'MISS'), f'[{c}] "{f[:58]}"')
    for x in h: print('        ', x)
