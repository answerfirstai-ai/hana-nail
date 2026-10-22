# HaNa Nail rev3 "Daylight palettes" - concept: /workspace/vault/Design/Concepts/hana-nail.md
import json, html, os, colorsys
from PIL import Image
R='/workspace/sites/hana-nail/'; B='/hana-nail/'; SITE='https://answerfirstai-ai.github.io/hana-nail/'
NAME='HaNa Nail'; KO='하나네일'; TEL='tel:+12139059015'; PHONE='(213) 905-9015'
ADDR='4157 5th St #228'; CITY='Los Angeles, CA 90020'
IG='https://www.instagram.com/hananail.la/'; IGH='@hananail.la'
DIR='https://www.google.com/maps/dir/?api=1&destination=4157+5th+St+%23228+Los+Angeles+CA+90020'
MAPS='https://www.google.com/maps/search/?api=1&query=HaNa+Nail+4157+5th+St+Los+Angeles+CA+90020'
SP='/workspace/clients/la-salon-hana-nail/photos/social/'; OUT=R+'assets/img/w/'; os.makedirs(OUT,exist_ok=True)
POST={l.split(',')[0][:-4]:l.split(',')[2] for l in open(SP+'manifest.csv').read().split('\n')[1:] if l}
def export(key,widths,crop=None,name=None):
  im=Image.open(SP+key+'.jpg').convert('RGB')
  if crop: W,H=im.size; im=im.crop((int(crop[0]*W),int(crop[1]*H),int(crop[2]*W),int(crop[3]*H)))
  name=name or key; ws=sorted({min(w,im.width) for w in widths})
  for w in ws:
    p=f'{OUT}{name}-{w}'
    if not os.path.exists(p+'.avif'):
      r=im.resize((w,round(im.height*w/im.width)),Image.LANCZOS); r.save(p+'.webp',quality=80); r.save(p+'.avif',quality=56)
  return dict(n=name,ws=ws,w=im.width,h=im.height)
def palette(key,k=5):
  # quantize to 14, then farthest-point pick 5 distinct colors (weighted by pixel share) so the set's own colors show, not only skin
  im=Image.open(SP+key+'.jpg').convert('RGB'); W,H=im.size; im=im.crop((int(W*.06),int(H*.06),int(W*.94),int(H*.94))).resize((200,250)); q=im.quantize(14,method=Image.Quantize.MAXCOVERAGE); p=q.getpalette()
  C=[(n,tuple(p[i*3:i*3+3])) for n,i in sorted(q.getcolors(),reverse=True) if n>=250]
  dist=lambda a,b:sum((x-y)**2 for x,y in zip(a,b))**.5
  cs=[C[0][1]]
  while len(cs)<k and len(cs)<len(C): cs.append(max((c for n,c in C if c not in cs),key=lambda c:min(dist(c,x) for x in cs)*(1+[n for n,cc in C if cc==c][0]/50000)))
  return sorted(['#%02X%02X%02X'%c for c in cs],key=lambda h:colorsys.rgb_to_hls(*[int(h[i:i+2],16)/255 for i in (1,3,5)])[1])
def tint(h,a=.80):
  r,g,b=[int(h[i:i+2],16) for i in (1,3,5)]; return '#%02X%02X%02X'%tuple(int(v+(250-v)*a) for v in (r,g,b))
def pic(d,alt,sizes,lazy=True,cls='',fp=False):
  ss=lambda e:', '.join(f'{B}assets/img/w/{d["n"]}-{w}.{e} {w}w' for w in d['ws'])
  w0=d['ws'][min(1,len(d['ws'])-1)]; h0=round(w0*d['h']/d['w'])
  return f'<picture><source type="image/avif" srcset="{ss("avif")}" sizes="{sizes}"><img{" class=\""+cls+"\"" if cls else ""} src="{B}assets/img/w/{d["n"]}-{w0}.webp" srcset="{ss("webp")}" sizes="{sizes}" width="{w0}" height="{h0}" alt="{html.escape(alt)}"{" loading=\"lazy\"" if lazy else ""}{" fetchpriority=\"high\"" if fp else ""} decoding="async"></picture>'
