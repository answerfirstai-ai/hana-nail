# HaNa Nail rev3, taste-skill direction "contact-sheet" (seed 56053772). Concept: /workspace/vault/Design/Concepts/hana-nail.md
exec(open('/workspace/sites/hana-nail/src/lib_head.py').read())
SETS=[('hana_05','Cream French, gold bands','Cream-yellow French tips with painted flowers, crystals and gold bands.'),
 ('hana_04','Watercolor rainbow','Short round nails in washed pinks, yellows and blues.'),
 ('hana_02','Sheer pink, white bows','Almond nails, sheer pink with fine white bow line art.'),
 ('hana_03','Clear jelly, 3D bubbles','Clear jelly nails with raised bubble accents.'),
 ('hana_08','Lilac, 3D bows','Long stilettos in flat lilac with sculpted bows.'),
 ('hana_06','Cherries and bows','Sheer nude with tiny painted cherries and bows.'),
 ('hana_07','Hot pink chrome','Long stilettos in hot pink chrome.')]
PAL={k:palette(k) for k,_,_ in SETS}
# detail crops of the same photo (real pixels, never upscaled); boxes are fractions of the source
CROPS={'hana_05':[(0,.1,.5,.75),(.45,.15,1,.7),(.05,.15,.4,.55)],'hana_04':[(.05,0,.7,.5),(.25,0,.75,.35),(.45,0,1,.45)],'hana_02':[(.25,.2,.55,.55),(.5,.2,.8,.55),(.2,.15,.8,.6)],
 'hana_03':[(0,.25,.55,.75),(.45,.2,1,.7),(.25,.55,.85,1)],'hana_08':[(.5,.05,1,.5),(.35,.05,.85,.5),(.05,.05,.55,.5)],'hana_06':[(.1,.15,.65,.6),(.4,.2,1,.7),(.15,.45,.6,.85)],'hana_07':[(.15,0,.75,.45),(0,.4,.6,.9),(.4,.35,1,.85)]}
FR={}
for k,_,_ in SETS:
  FR[k]=[export(k,[260,400,640],name=k+'-t0')]+[export(k,[260,400],crop=c,name=f'{k}-t{i+1}') for i,c in enumerate(CROPS[k])]
HERO=export('hana_05',[800,1200,1600,2000,2600,3175])
PREV={k:export(k,[480,720,960]) for k,_,_ in SETS}
NAVY='#2B2D31'
LD={"@context":"https://schema.org","@type":"NailSalon","@id":SITE+"#salon","name":NAME,"alternateName":KO,"url":SITE,"telephone":"+1-213-905-9015","image":SITE+"assets/img/og.jpg",
 "address":{"@type":"PostalAddress","streetAddress":ADDR,"addressLocality":"Los Angeles","addressRegion":"CA","postalCode":"90020","addressCountry":"US"},
 "geo":{"@type":"GeoCoordinates","latitude":34.0654932,"longitude":-118.3094635},"hasMap":MAPS,"areaServed":"Koreatown, Los Angeles","sameAs":[IG]}
FONTS2='@font-face{font-family:"Switzer";src:url(%sassets/fonts/switzer-400.woff2) format("woff2");font-weight:400;font-display:swap}@font-face{font-family:"Switzer";src:url(%sassets/fonts/switzer-500.woff2) format("woff2");font-weight:500;font-display:swap}@font-face{font-family:"Switzer";src:url(%sassets/fonts/switzer-600.woff2) format("woff2");font-weight:600;font-display:swap}@font-face{font-family:"IBM Plex Sans KR";src:url(%sassets/fonts/plexkr-ko-400.woff2) format("woff2");font-weight:400 600;font-display:swap;unicode-range:U+AC00-D7A3}'%(B,B,B,B)
def page(path,title,desc,body,cur='',extra=''):
  can=SITE+path
  a=lambda h,t:f'<a href="{B}{h}"{" aria-current=\"page\"" if cur==h else ""}>{t}</a>'
  links=a('#sets','Sets')+a('#palettes','Palettes')+a('visit/','Visit')+f'<a href="{IG}" target="_blank" rel="noopener">Instagram<span class="sr"> (opens Instagram)</span></a>'
  return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title><meta name="description" content="{html.escape(desc)}"><link rel="canonical" href="{can}">
<meta name="theme-color" content="{NAVY}"><meta property="og:type" content="website"><meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}"><meta property="og:url" content="{can}"><meta property="og:image" content="{SITE}assets/img/og.jpg"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{B}assets/img/favicon.svg" type="image/svg+xml"><link rel="preload" href="{B}assets/fonts/switzer-600.woff2" as="font" type="font/woff2" crossorigin><link rel="preload" href="{B}assets/fonts/switzer-400.woff2" as="font" type="font/woff2" crossorigin>{extra}
<style>{FONTS2}</style><link rel="stylesheet" href="{B}assets/css/site.css">
<script type="application/ld+json">{json.dumps(LD,ensure_ascii=False)}</script></head><body>
<a class="skip" href="#main">Skip to content</a>
<header class="top"><a class="mark" href="{B}" aria-label="HaNa Nail 하나네일, home">HaNa Nail</a>
<nav aria-label="Main"><div class="links">{links}</div><a class="b b-acc tel" href="{TEL}">Call {PHONE}</a>
<details class="mnav"><summary aria-label="Open menu">Menu</summary><div class="mpanel"><a href="{B}">Home</a>{links}<a href="{TEL}">Call {PHONE}</a></div></details></nav></header>
<main id="main">{body}</main>
<footer class="foot"><p>HaNa Nail, Koreatown nail sets</p><p class="f-links"><a href="{TEL}">{PHONE}</a><a href="{IG}" target="_blank" rel="noopener">{IGH}</a><a href="{B}visit/">Visit</a></p><p class="f-r">© 2026 · demo site</p>
<p class="fine">Photos: {IGH}, the salon's own Instagram. Palette colors are sampled from those photos. Services and hours are from public listings, so call to confirm.</p></footer>
<script src="{B}assets/js/site.js" defer></script></body></html>'''
dot=lambda c,cls='sw':f'<span class="{cls}" style="--c:{c}"></span>'
img=lambda d,alt,sizes,lazy=True,fp=False:pic(d,alt,sizes,lazy=lazy,fp=fp)
hero_img=f'<picture><source type="image/avif" srcset="{", ".join(f"{B}assets/img/w/hana_05-{w}.avif {w}w" for w in HERO["ws"])}" sizes="(max-width:760px) 100vw, 58vw"><img src="{B}assets/img/w/hana_05-1600.webp" srcset="{", ".join(f"{B}assets/img/w/hana_05-{w}.webp {w}w" for w in HERO["ws"])}" sizes="(max-width:760px) 100vw, 58vw" width="1600" height="{round(1600*HERO["h"]/HERO["w"])}" alt="Two hands with cream-yellow French tips, painted flowers, crystals and gold bands, held against a grey stucco wall in daylight." fetchpriority="high" decoding="async"></picture>'
def run(i,k,n,d,first=False):
  fr=FR[k]; out=f'<div class="run" data-k="{k}"><p class="run-t">{n}</p><div class="frames">'
  for j,f in enumerate(fr):
    out+=f'<a class="fr" href="{POST[k]}" target="_blank" rel="noopener" style="--r:{f["w"]/f["h"]:.3f}">{img(f,(n+", detail" if j else n)+". Photo from @hananail.la"+(" (opens Instagram post)" if j==0 else ""),"(max-width:760px) 44vw, 260px",lazy=not first)}</a>'
  return out+'</div></div>'
runs=''.join(run(i,k,n,d) for i,(k,n,d) in enumerate(SETS))
home=f'''<section class="hero" aria-labelledby="h1">
<h1 id="h1">HaNa Nail <span lang="ko">하나네일</span></h1>
<div class="band">
<p class="lead">Nail sets by appointment in suite #228, Koreatown. Every one is photographed in daylight and posted to {IGH}.</p>
<div><p class="lbl">Book</p><p>Appointment only. The salon's Instagram bio says text or call <a href="{TEL}">{PHONE}</a>.</p></div>
<div><p class="lbl">Listings mention</p><ul><li>Gel manicure</li><li>Gel-X extensions</li><li>Nail art</li><li>Pedicure</li><li>Lashes</li></ul></div>
<div><p class="lbl">Where</p><p>4157 5th St #228<br>Los Angeles 90020</p><p><a href="{B}visit/">Hours and directions</a></p></div>
<div class="band-cta"><a class="b b-acc" href="{TEL}">Call to book</a><a class="tl" href="{IG}" target="_blank" rel="noopener">See every set on Instagram<span class="sr"> (opens Instagram)</span></a></div>
</div>
<div class="sheet-top"><figure class="big">{hero_img}<figcaption>Cream French, gold bands</figcaption></figure>
<div class="first-runs">{run(0,*SETS[0],first=True)}{run(1,*SETS[1])}</div></div></section>
<section class="sheet" id="sets" aria-labelledby="sets-h"><h2 id="sets-h">Seven recent sets, frame by frame</h2>
<p class="sheet-p">Each set is the full photo plus close crops of the same picture. Tap any frame to open the post.</p>
<div class="runs">{''.join(run(i,k,n,d) for i,(k,n,d) in enumerate(SETS[2:],2))}</div></section>
<section class="pals" id="palettes" aria-labelledby="pal-h"><div class="pal-list"><h2 id="pal-h">The palette of each set</h2>
<p class="pal-p">Five colors sampled from each photo. Point at or tap a set to see it.</p>
<ol class="rows">{''.join(f'<li><button type="button" class="row" data-k="{k}" aria-controls="pv" aria-pressed="{"true" if k=="hana_08" else "false"}"><span class="rn">{dot(PAL[k][2],"dot")}{n}</span><span class="rv">{"".join(dot(c) for c in PAL[k])}</span></button><div class="inl">{img(PREV[k],n+". "+d,"(max-width:760px) 90vw, 1px")}</div></li>' for i,(k,n,d) in enumerate(SETS))}</ol></div>
<figure class="pv" id="pv" aria-live="polite">{''.join(f'<div class="pv-i{" on" if k=="hana_08" else ""}" data-k="{k}">{img(PREV[k],n+". "+d,"(max-width:760px) 1px, min(36vw, 480px)")}<figcaption><b>{n}</b> {d}<span class="hexes">{" ".join(PAL[k])}</span></figcaption></div>' for i,(k,n,d) in enumerate(SETS))}</figure></section>
<section class="contact" aria-labelledby="c-h"><h2 id="c-h" class="sr">Book a set</h2><p class="c-s">Bring a photo or an idea. Book a time by calling, or by text as the salon's bio says.</p>
<div class="c-img">{img(FR['hana_06'][2],"Cherries and bows, detail. Photo from @hananail.la","160px")}</div>
<div class="c-q"><p class="q">Ready for a set?</p><p><a href="{TEL}">Call {PHONE}</a></p><p><a href="{IG}" target="_blank" rel="noopener">Message {IGH}<span class="sr"> (opens Instagram)</span></a></p><p class="soft">Suite #228, 4157 5th St, Koreatown. Listed hours Mon-Sat; call to confirm.</p></div></section>'''
PRE=f'<link rel="preload" as="image" type="image/avif" imagesrcset="{", ".join(f"{B}assets/img/w/hana_05-{w}.avif {w}w" for w in HERO["ws"])}" imagesizes="(max-width:760px) 100vw, 58vw" fetchpriority="high">'
H=[("Monday","9 AM – 7 PM"),("Tuesday","9 AM – 7 PM"),("Wednesday","9 AM – 7 PM"),("Thursday","9 AM – 7 PM"),("Friday","9 AM – 7 PM"),("Saturday","9 AM – 6 PM"),("Sunday","Closed")]
visit=f'''<section class="v" aria-labelledby="h1"><h1 id="h1">Suite #228, 4157 5th St</h1>
<div class="v-g"><div><p class="lead">HaNa Nail is inside the building at 4157 5th St, Los Angeles 90020, in Koreatown. Ask about parking when you book.</p>
<p class="v-cta"><a class="b b-acc" href="{DIR}" target="_blank" rel="noopener">Get directions<span class="sr"> (opens Google Maps)</span></a><a class="tl" href="{TEL}">Call {PHONE}</a></p>
<figure class="v-img">{img(PREV['hana_08'],"Lilac stilettos with sculpted bows against a blue-grey wall. Photo from @hananail.la","(max-width:760px) 92vw, 480px",lazy=False)}</figure></div>
<div><h2>Listed hours</h2><ul class="hrs">{''.join(f'<li><span>{d}</span><span>{h}</span></li>' for d,h in H)}</ul>
<p class="soft">Per Google and Yahoo listings. Appointment only, so call to confirm a time.</p><p><a href="{MAPS}" target="_blank" rel="noopener">Open in Google Maps<span class="sr"> (opens Google Maps)</span></a></p></div></div></section>'''
nf=f'<section class="v"><h1>Page not found</h1><p class="lead">That page doesn\'t exist.</p><p class="v-cta"><a class="b b-acc" href="{B}">Back home</a><a class="tl" href="{TEL}">Call {PHONE}</a></p></section>'
open(R+'index.html','w').write(page('','HaNa Nail 하나네일 | Nail Sets by Appointment, Koreatown LA',"HaNa Nail, suite #228 at 4157 5th St in Koreatown, Los Angeles. Nail sets by appointment: call (213) 905-9015 or see @hananail.la.",home,'',PRE))
os.makedirs(R+'visit',exist_ok=True)
open(R+'visit/index.html','w').write(page('visit/','Hours & Directions | HaNa Nail, Koreatown LA','HaNa Nail is in suite #228 at 4157 5th St, Los Angeles 90020. Listed hours Mon-Sat; appointment only. Call (213) 905-9015.',visit,'visit/'))
open(R+'404.html','w').write(page('404.html','Page not found | HaNa Nail','Page not found.',nf).replace('<link rel="canonical"','<meta name="robots" content="noindex"><link rel="x-canonical"'))
open(R+'sitemap.xml','w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>{SITE}{p}</loc><lastmod>2026-10-22</lastmod></url>' for p in ['','visit/'])+'</urlset>')
open(R+'robots.txt','w').write(f'User-agent: *\nAllow: /\nSitemap: {SITE}sitemap.xml\n'); open(R+'.nojekyll','w').write('')
im=Image.open(SP+'hana_05.jpg').convert('RGB'); W,Hh=im.size; ch=int(W*630/1200); im.crop((0,(Hh-ch)//2,W,(Hh-ch)//2+ch)).resize((1200,630),Image.LANCZOS).save(R+'assets/img/og.jpg',quality=84)
json.dump(PAL,open(R+'src/palettes.json','w'),indent=1); print('ok')
