# HaNa Nail Rev 5 build. Design: Desire's mock (05-mockup/output/mock.html, brief 04-brief/output/design_brief.md); Codor's job here is the live build.
import json, html, os
from PIL import Image
R='/workspace/sites/hana-nail/'; B='/hana-nail/'; SITE='https://answerfirstai-ai.github.io/hana-nail/'
SRC='/workspace/clients/la-salon-hana-nail/05-mockup/output/img/'; OUT=R+'assets/img/p/'; os.makedirs(OUT,exist_ok=True)
TEL='tel:+12139059015'; PHONE='(213) 905-9015'; IG='https://www.instagram.com/hananail.la/'; DM='https://ig.me/m/hananail.la'
MAPS='https://www.google.com/maps/place/HaNa+Nail+%ED%95%98%EB%82%98%EB%84%A4%EC%9D%BC/data=!4m7!3m6!1s0x80c2b9566291d6e5:0x386873d0bf8ea02e!8m2!3d34.0654932!4d-118.3094635!16s%2Fg%2F11h4nhpdqh!19sChIJ5daRYla5woARLqCOv9BzaDg'
def exp(name,widths,top=0,out=None,box=None,src=None):
  im=Image.open((src or SRC)+name+'.jpg').convert('RGB')
  if box: W,H=im.size; im=im.crop((int(box[0]*W),int(box[1]*H),int(box[2]*W),int(box[3]*H)))
  if top: im=im.crop((0,int(im.height*top),im.width,im.height))  # drop the car-interior strip (top 30%) of the sheer-charms photo
  name=out or name; ws=sorted({min(w,im.width) for w in widths})
  for w in ws:
    p=f'{OUT}{name}-{w}'
    if not os.path.exists(p+'.avif'):
      r=im.resize((w,round(im.height*w/im.width)),Image.LANCZOS); r.save(p+'.webp',quality=82); r.save(p+'.avif',quality=60)
  return dict(n=name,ws=ws,w=im.width,h=im.height)
IMG={'daisy-french':exp('daisy-french',[640,960,1280,1920,2560]),'magenta-chrome':exp('magenta-chrome',[480,800,1193]),'periwinkle-bows':exp('periwinkle-bows',[480,800,1300]),
 'watercolor':exp('watercolor',[480,800,1300]),'cherry-bow':exp('cherry-bow',[480,800,912]),'pink-fade-bows':exp('pink-fade-bows',[480,800,1300]),'peri-detail':exp('hana_08',[400,655],out='peri-detail',box=(0.50,0.22,0.955,0.82),src='/workspace/clients/la-salon-hana-nail/photos/social/'),'sheer-charms':exp('hana_03',[400,542],out='charms-hand',box=(0.5,0.27,1.0,0.58),src='/workspace/clients/la-salon-hana-nail/photos/social/')}
def pic(n,alt,sizes,lazy=True,hi=False,cls='',pos=''):
  d=IMG[n]; ss=lambda e:', '.join(f'{B}assets/img/p/{d['n']}-{w}.{e} {w}w' for w in d['ws'])
  mid=d['ws'][min(2,len(d['ws'])-1)]
  at=(' fetchpriority="high"' if hi else '')+(' loading="lazy"' if lazy else '')+(f' class="{cls}"' if cls else '')
  return f'<picture><source type="image/avif" srcset="{ss("avif")}" sizes="{sizes}"><img src="{B}assets/img/p/{d['n']}-{mid}.webp" srcset="{ss("webp")}" sizes="{sizes}" width="{d["w"]}" height="{d["h"]}" alt="{html.escape(alt)}"{at} decoding="async"></picture>'
S5='(max-width:900px) 100vw, min(37vw, 547px)'   # 5 columns, content capped at 1312px => never past 2x of these sources
SETS=[ # id, tone, colour var, class, h3, fact, post
 ('daisy','dark','yellow','s1','Butter-yellow daisy French','Hand-painted daisies and gold rings.','DbKhw6tlOfz'),
 ('magenta','light','magenta','s3','Magenta chrome stilettos','Mirror finish on long points.','DW5tI3RDov8'),
 ('periwinkle','dark','peri','s4','Periwinkle bow stilettos','Matte blue-violet with a tiny bow on each hand.','DWvS3gXlRlt'),
 ('watercolor','dark','coral','s2','Watercolor swirls','Pink, blue and orange washed over short nails.','Dcwt5n0gQRf'),
 ('cherry','dark','leaf','s5','Cherry and bow','Tiny drawn cherries and bow outlines on sheer nails.','DauKIC-lKcw'),
 ('pinkfade','dark','blush','s6','Pink fade, silver bows','A soft pink fade with a bow drawn in silver.','Dcw_qgjCTF8'),
 ('charms','dark','clay','s7','Sheer pink, crystal charms','A pale butterfly, pearls and small crystals on sheer pink nails.','DcPzitLOSsH')]
def cap(h,f,p): return f'<div class="cap"><h3 class="kt">{h}</h3><p class="fact">{f} <a href="https://www.instagram.com/p/{p}/" target="_blank" rel="noopener">Photo: @hananail.la<span class="sr"> (opens Instagram)</span></a></p></div>'
def art(i):
  sid,tone,col,cl,h,f,p=SETS[i]; c=cap(h,f,p)
  im={'daisy':pic('daisy-french','Butter-yellow daisy French tips with gold rings and rhinestones on almond nails','(max-width:900px) 100vw, min(53vw, 765px)'),
   'magenta':pic('magenta-chrome','Long magenta chrome stiletto nails with a mirrored finish',S5),
   'periwinkle':pic('periwinkle-bows','Periwinkle stiletto nails with bow charms',S5,cls='a')+pic('peri-detail','Close crop of periwinkle stiletto nails, one with a small raised bow','(max-width:900px) 1px, 319px',cls='b'),
   'watercolor':pic('watercolor','Short nails with pink, blue and orange watercolor swirls',S5),
   'cherry':pic('cherry-bow','Sheer nails with a drawn cherry and bow among green leaves','(max-width:900px) 100vw, min(30vw, 428px)'),
   'pinkfade':pic('pink-fade-bows','Pink fade nails with silver bow line art on a white ground',S5),
   'charms':pic('sheer-charms','Right hand with sheer pink nails: one with small pearls and crystals, one with a pale butterfly charm edged in gold, one with a clear crystal charm','(max-width:900px) 270px, 270px')}[sid]
  body=(c+im) if sid in('watercolor','cherry') else (im+c)
  return f'<article class="set {cl}" id="{sid}" style="--c:var(--{col})" data-tone="{tone}">{body}</article>'
LABEL=['Butter-yellow daisy French','Magenta chrome stilettos','Periwinkle bow stilettos','Watercolor swirls','Cherry and bow','Pink fade with silver bows','Sheer pink with crystal charms']
RAIL=['yellow','magenta','peri','coral','leaf','blush','clay']; HREF=['daisy','magenta','periwinkle','watercolor','cherry','pinkfade','charms']
rail=''.join(f'<li><a href="#{h}" style="--c:var(--{c})" aria-label="{l}"></a></li>' for h,c,l in zip(HREF,RAIL,LABEL))
LD={"@context":"https://schema.org","@type":"NailSalon","@id":SITE+"#salon","name":"HaNa Nail","alternateName":"하나네일","url":SITE,"telephone":"+1-213-905-9015","image":SITE+"assets/img/og.jpg",
 "address":{"@type":"PostalAddress","streetAddress":"4157 5th St, Suite 228","addressLocality":"Los Angeles","addressRegion":"CA","postalCode":"90020","addressCountry":"US"},
 "geo":{"@type":"GeoCoordinates","latitude":34.0654932,"longitude":-118.3094635},"hasMap":MAPS,"areaServed":"Koreatown, Los Angeles","sameAs":[IG]}
TITLE='HaNa Nail · nail sets by appointment in Koreatown, Los Angeles'
DESC='HaNa Nail takes nail appointments by phone or Instagram in Suite 228, 4157 5th St, Koreatown, Los Angeles.'
dm=f'<a class="link" href="{DM}" target="_blank" rel="noopener">Message on Instagram<span class="sr"> (opens Instagram)</span></a>'
ALT_D='Both hands with almond nails in butter-yellow daisy French tips, gold rings and rhinestones, held against a slate wall'
hero=f'''<section class="hero">
  <div class="say"><h1 class="kt">HaNa Nail</h1><p class="lede">Nail sets in colour, by appointment, in Koreatown.</p>
    <div class="acts"><a class="btn" href="{TEL}">Call {PHONE}</a>{dm}</div></div>
  <div class="mosaic" aria-label="Recent sets from @hananail.la">
    <figure class="tile t-a">{pic('daisy-french',ALT_D,'(max-width:900px) 62vw, 34vw',lazy=False,hi=True)}</figure>
    <figure class="tile t-b">{pic('magenta-chrome','Hands with long magenta chrome stiletto nails on concrete','(max-width:900px) 24vw, 14vw',lazy=False)}</figure>
    <figure class="tile t-c">{pic('periwinkle-bows','Periwinkle stiletto nails with small bow charms against a blue-grey wall','(max-width:900px) 24vw, 14vw',lazy=False)}</figure>
    <figure class="tile t-d">{pic('cherry-bow','Sheer nails with a small cherry and a bow, shot among green leaves','(max-width:900px) 24vw, 14vw',lazy=False)}</figure>
    <figure class="tile t-e">{pic('watercolor','Short nails painted with pink, blue and orange watercolor swirls','(max-width:900px) 24vw, 14vw',lazy=False)}</figure>
  </div></section>'''
body=f'''<header class="top"><a class="mark" href="#top">HaNa Nail</a><nav aria-label="Sets by colour"><ul class="rail">{rail}</ul></nav><a class="btn" href="{TEL}">Call to book</a></header>
<main id="top">{hero}
<section class="cat" id="sets"><div class="cat-head"><h2>Seven sets, each in its own colour.</h2><p>Every photo is from the HaNa Instagram. Tap a swatch at the top to jump to a set.</p></div>
{"".join(art(i) for i in range(7))}</section>
<section class="book" id="book"><h2>By appointment, by phone.</h2><div class="body">
<p>Call, or send a message on Instagram with the set you like and ask what is open. Gel, Gel-X, nail art, pedicures and lashes are listed on HaNa's public profiles, so ask when you call. Prices: ask when you call.</p>
<div class="acts"><a class="btn alt" href="{TEL}">Call {PHONE}</a>{dm}<a class="link" href="{IG}" target="_blank" rel="noopener">@hananail.la<span class="sr"> (opens Instagram)</span></a></div></div></section>
<section class="visit" id="visit"><h2>Find Suite 228.</h2>
<div class="col a"><b>Address</b><p>4157 5th St, Suite 228<br>Los Angeles, CA 90020<br>Koreatown</p><p><a class="link" href="{MAPS}" target="_blank" rel="noopener">Directions<span class="sr"> in Google Maps (opens Google Maps)</span></a></p></div>
<div class="col b"><b>Hours</b><p>Mon to Fri, 9 to 7<br>Sat, 9 to 6<br>Sun, closed</p><p class="note">As listed on Google. Appointment only, so call to confirm.</p></div></section></main>
<footer>Photos: @hananail.la</footer>'''
def page(path,body,title=TITLE,extra='',head=''):
  return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title><meta name="description" content="{html.escape(DESC)}"><link rel="canonical" href="{SITE}{path}">
<meta name="theme-color" content="#e4e2db"><meta property="og:type" content="website"><meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(DESC)}"><meta property="og:url" content="{SITE}{path}"><meta property="og:image" content="{SITE}assets/img/og.jpg"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{B}assets/img/favicon.svg" type="image/svg+xml"><link rel="preload" href="{B}assets/fonts/librefranklin-700-latin.woff2" as="font" type="font/woff2" crossorigin><link rel="preload" href="{B}assets/fonts/sourceserif4-latin.woff2" as="font" type="font/woff2" crossorigin>{extra}
<link rel="stylesheet" href="{B}assets/css/site.css">{head}
<script type="application/ld+json">{json.dumps(LD,ensure_ascii=False)}</script></head><body>{body}
<script src="{B}assets/js/site.js" defer></script></body></html>'''
d=IMG['daisy-french']
pre=f'<link rel="preload" as="image" type="image/avif" imagesrcset="{", ".join(f"{B}assets/img/p/daisy-french-{w}.avif {w}w" for w in d["ws"])}" imagesizes="(max-width:900px) 62vw, 34vw" fetchpriority="high">'
open(R+'index.html','w').write(page('',body,extra=pre))
# the old /visit/ URL is live: keep it as a redirect to the Visit band
os.makedirs(R+'visit',exist_ok=True)
open(R+'visit/index.html','w').write(f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Visit HaNa Nail</title><meta name="viewport" content="width=device-width,initial-scale=1"><link rel="canonical" href="{SITE}"><meta name="robots" content="noindex"><meta http-equiv="refresh" content="0;url={B}#visit"></head><body><p><a href="{B}#visit">Visit HaNa Nail: address and hours</a></p></body></html>')
nf=f'<header class="top"><a class="mark" href="{B}">HaNa Nail</a><span></span><a class="btn" href="{TEL}">Call to book</a></header><main><section class="book"><h2>That page is not here.</h2><div class="body"><div class="acts"><a class="btn alt" href="{B}">Back to the sets</a></div></div></section></main>'
open(R+'404.html','w').write(page('404.html',nf,title='Page not found | HaNa Nail').replace('<link rel="canonical"','<meta name="robots" content="noindex"><link rel="x-canonical"'))
open(R+'sitemap.xml','w').write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>{SITE}</loc><lastmod>2026-10-23</lastmod></url></urlset>')
open(R+'robots.txt','w').write(f'User-agent: *\nAllow: /\nSitemap: {SITE}sitemap.xml\n'); open(R+'.nojekyll','w').write('')
print('built')
