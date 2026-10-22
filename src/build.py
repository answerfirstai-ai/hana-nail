import json, html
R='/workspace/sites/hana-nail/'; B='/hana-nail/'; SITE='https://answerfirstai-ai.github.io/hana-nail/'
NAME='HaNa Nail'; KO='하나네일'; TEL='tel:+12139059015'; PHONE='(213) 905-9015'
ADDR='4157 5th St #228'; CITY='Los Angeles, CA 90020'
IG='https://www.instagram.com/hananail.la/'; IGH='@hananail.la'
DIR='https://www.google.com/maps/dir/?api=1&destination=4157+5th+St+%23228+Los+Angeles+CA+90020'
MAPS='https://www.google.com/maps/search/?api=1&query=HaNa+Nail+4157+5th+St+Los+Angeles+CA+90020'
ICON={'call':'<path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1L6.6 10.8Z"/>',
 'pin':'<path d="M12 2a7 7 0 0 0-7 7c0 5.25 7 13 7 13s7-7.75 7-13a7 7 0 0 0-7-7Zm0 9.5A2.5 2.5 0 1 1 12 6.5a2.5 2.5 0 0 1 0 5Z"/>',
 'ig':'<path d="M12 7.3A4.7 4.7 0 1 0 12 16.7 4.7 4.7 0 0 0 12 7.3Zm0 7.7a3 3 0 1 1 0-6 3 3 0 0 1 0 6Zm6-7.9a1.1 1.1 0 1 1-2.2 0 1.1 1.1 0 0 1 2.2 0ZM12 3.6c2.7 0 3 0 4.1.1 2.7.1 4 1.4 4.1 4.1.1 1.1.1 1.4.1 4.1s0 3-.1 4.1c-.1 2.7-1.4 4-4.1 4.1-1.1.1-1.4.1-4.1.1s-3 0-4.1-.1c-2.7-.1-4-1.4-4.1-4.1C3.7 15 3.6 14.7 3.6 12s0-3 .1-4.1C3.8 5.2 5.1 3.9 7.9 3.7 9 3.6 9.3 3.6 12 3.6ZM12 2c-2.7 0-3.1 0-4.2.1C4.2 2.2 2.2 4.2 2.1 7.8 2 8.9 2 9.3 2 12s0 3.1.1 4.2c.2 3.6 2.2 5.6 5.7 5.7 1.1.1 1.5.1 4.2.1s3.1 0 4.2-.1c3.6-.2 5.6-2.2 5.7-5.7.1-1.1.1-1.5.1-4.2s0-3.1-.1-4.2c-.2-3.6-2.2-5.6-5.7-5.7C15.1 2 14.7 2 12 2Z"/>'}
I=lambda n:f'<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor">{ICON[n]}</svg>'
call=lambda c='btn btn-plum',t=None:f'<a class="{c}" href="{TEL}">{I("call")}{t or "Call "+PHONE}</a>'
dirb=lambda c='btn btn-ink':f'<a class="{c}" href="{DIR}" target="_blank" rel="noopener">{I("pin")}Directions<span class="sr"> (opens Google Maps)</span></a>'
igb=lambda c='btn btn-ink',t='Instagram':f'<a class="{c}" href="{IG}" target="_blank" rel="noopener">{I("ig")}{t}<span class="sr"> (opens Instagram)</span></a>'
stroke='<svg class="ieung" viewBox="0 0 600 40" preserveAspectRatio="none" aria-hidden="true"><path d="M6 24 C 120 10, 300 30, 594 16"/></svg>'
LD={"@context":"https://schema.org","@type":"NailSalon","@id":SITE+"#salon","name":NAME,"alternateName":KO,"url":SITE,"telephone":"+1-213-905-9015","image":SITE+"assets/img/og.jpg",
 "address":{"@type":"PostalAddress","streetAddress":ADDR,"addressLocality":"Los Angeles","addressRegion":"CA","postalCode":"90020","addressCountry":"US"},
 "geo":{"@type":"GeoCoordinates","latitude":34.0654932,"longitude":-118.3094635},"hasMap":MAPS,"areaServed":"Koreatown, Los Angeles","sameAs":[IG]}
FF=[("Gowun Batang","gowun-700",700,"U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+2000-206F,U+20AC,U+2122,U+2212"),("Gowun Batang","gowun-ko-700",700,"U+AC00-D7A3"),("IBM Plex Sans KR","plexkr-400",400,"U+0000-00FF,U+2000-206F"),("IBM Plex Sans KR","plexkr-ko-400",400,"U+AC00-D7A3"),("IBM Plex Sans KR","plexkr-500",500,None)]
FONTS=''.join(f'@font-face{{font-family:"{f}";src:url({B}assets/fonts/{s}.woff2) format("woff2");font-weight:{w};font-display:swap{";unicode-range:"+u if u else ""}}}' for f,s,w,u in FF)
def page(path,title,desc,body,cur='',extra=''):
  can=SITE+path
  nav=lambda h,t:f'<a href="{B}{h}"{" aria-current=\"page\"" if cur==h else ""}>{t}</a>'
  links=nav('#sets','Sets')+nav('#book','Book')+nav('visit/','Visit')
  return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title><meta name="description" content="{html.escape(desc)}"><link rel="canonical" href="{can}">
<meta name="theme-color" content="#EEF0EC"><meta property="og:type" content="website"><meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}"><meta property="og:url" content="{can}"><meta property="og:image" content="{SITE}assets/img/og.jpg"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{B}assets/img/favicon.svg" type="image/svg+xml"><link rel="preload" href="{B}assets/fonts/gowun-700.woff2" as="font" type="font/woff2" crossorigin>{extra}
<style>{FONTS}</style><link rel="stylesheet" href="{B}assets/css/site.css">
<script type="application/ld+json">{json.dumps(LD,ensure_ascii=False)}</script></head><body>
<a class="skip" href="#main">Skip to content</a>
<header class="nav"><div class="nav-in"><a class="mark" href="{B}" aria-label="HaNa Nail 하나네일, home">HaNa Nail <span lang="ko">{KO}</span></a>
<nav aria-label="Main"><div class="links">{links}</div><details class="mnav"><summary aria-label="Open menu">Menu</summary><div class="mpanel"><a href="{B}">Home</a>{links}<a href="{TEL}">Call {PHONE}</a><a href="{IG}" target="_blank" rel="noopener">Instagram {IGH}</a></div></details></nav>
{call("btn btn-plum btn-sm nav-call","Call to book")}</div></header>
<main id="main">{body}</main>
<footer class="foot"><div class="wrap">{stroke}<p class="f-line">HaNa Nail · <a href="{IG}" target="_blank" rel="noopener">{IGH}</a> · <a href="{TEL}">{PHONE}</a></p>
<p>{ADDR}, {CITY} (Koreatown). By appointment.</p>{HSVG("hana")}
<p class="fine">The hero image is an AI-generated illustrative scene, not a photo of HaNa Nail or its studio. Nail set photos are from the salon's own Instagram, @hananail.la. Services and hours come from public listings; call to confirm. Demo site, © 2026 HaNa Nail.</p></div></footer>
<div class="mbar" aria-label="Quick actions">{call("btn btn-plum btn-sm","Call")}{igb("btn btn-ink btn-sm")}</div>
<script src="{B}assets/js/site.js" defer></script></body></html>'''
hero=f'''<picture><source media="(max-width:760px)" type="image/avif" srcset="{B}assets/img/hero-m-800.avif 800w, {B}assets/img/hero-m-1200.avif 1200w, {B}assets/img/hero-m-1600.avif 1600w" sizes="100vw"><source media="(max-width:760px)" type="image/webp" srcset="{B}assets/img/hero-m-800.webp 800w, {B}assets/img/hero-m-1200.webp 1200w, {B}assets/img/hero-m-1600.webp 1600w" sizes="100vw"><source type="image/avif" srcset="{B}assets/img/hero-d-1280.avif 1280w, {B}assets/img/hero-d-1920.avif 1920w, {B}assets/img/hero-d-2880.avif 2880w" sizes="100vw"><img src="{B}assets/img/hero-d-1920.webp" srcset="{B}assets/img/hero-d-1280.webp 1280w, {B}assets/img/hero-d-1920.webp 1920w, {B}assets/img/hero-d-2880.webp 2880w" sizes="100vw" width="2880" height="1620" alt="Illustrative: one empty celadon dish and an ink stone on handmade hanji paper. AI-generated, not a photo of HaNa Nail or its work." fetchpriority="high"></picture>'''
PRE=f'<link rel="preload" as="image" type="image/avif" media="(max-width:760px)" imagesrcset="{B}assets/img/hero-m-800.avif 800w, {B}assets/img/hero-m-1200.avif 1200w, {B}assets/img/hero-m-1600.avif 1600w" imagesizes="100vw" fetchpriority="high"><link rel="preload" as="image" type="image/avif" media="(min-width:761px)" imagesrcset="{B}assets/img/hero-d-1280.avif 1280w, {B}assets/img/hero-d-1920.avif 1920w, {B}assets/img/hero-d-2880.avif 2880w" imagesizes="100vw" fetchpriority="high">'
import sys as _s;_s.path.insert(0,'/workspace/sites/_kit');from social import export,pic
SP='/workspace/clients/la-salon-hana-nail/photos/social/';OUT=R+'assets/img/ig' if 'R' in globals() else 'assets/img/ig'
PH=[('hana_05',900,None,'Milky French tips with gold flake','wide'),('hana_04',450,None,'Watercolor rainbow blush nails, short round','tall'),('hana_02',450,None,'Sheer pink almond nails with fine white bow line art','tall'),('hana_03',300,(0,.33,1,1),'Clear jelly nails with 3D bubble accents and rings',''),('hana_06',300,None,'Sheer nude nails with tiny cherries and bows','')]
PD=[(export(SP+f+'.jpg',OUT,f,w,c),a,k) for f,w,c,a,k in PH]
HSVG=lambda c:f'<svg class="{c}" viewBox="0 0 210 100" aria-hidden="true" focusable="false"><text x="0" y="86" font-size="96" lang="ko">하나</text></svg>'
num=lambda n,ko:f'<p class="num" aria-hidden="true"><b>{n}</b> <span lang="ko">{ko}</span></p>'
home=f'''<section class="hero" aria-labelledby="h1"><div class="hero-img">{hero}<span class="sweep" aria-hidden="true"></span></div><span class="ill">Illustrative scene</span>
{HSVG("hana big")}
<div class="hero-in"><h1 id="h1">HaNa Nail</h1><p class="ko-sub" lang="ko">하나네일 · 코리아타운</p>
<p class="sub">By appointment, in suite #228 at 4157 5th St.</p>
<div class="ctas">{call()}{igb()}</div></div></section>
<section class="sets" id="sets" aria-labelledby="sets-h"><div class="wrap">{num("01","하나")}
<h2 id="sets-h">Recent sets</h2><p class="lede">From the salon's own Instagram, {IGH}.</p>
<ul class="gallery">{''.join(f'<li class="{k}"><figure>{pic(B,"assets/img/ig",d,a+". Photo from the salon\'s own Instagram.",sizes=("(max-width:600px) 92vw, 900px" if k=="wide" else "(max-width:600px) 92vw, 450px" if k=="tall" else "(max-width:600px) 46vw, 300px"))}<figcaption>{a}<span>Photo: {IGH}</span></figcaption></figure></li>' for d,a,k in PD)}</ul>
<div class="ctas">{igb("btn btn-ink","More sets on Instagram")}{call()}</div></div></section>
<section class="sec plate" id="book" aria-labelledby="svc-h"><div class="wrap split">{num("02","서비스")}
<div><h2 id="svc-h">Services</h2><p class="muted">Per public listings. Call to confirm what's available and for pricing. Appointment only, per the salon's Instagram bio.</p>
<p class="phone"><a href="{TEL}">{PHONE}</a></p><div class="ctas">{call()}{igb()}</div></div>
<ol class="dishes">{''.join(f'<li><span class="dish" aria-hidden="true"></span><b>{n}</b><span lang="ko">{k}</span></li>' for n,k in [('Gel manicure','젤 매니큐어'),('Gel-X extensions','젤엑스 연장'),('Nail art','네일 아트'),('Pedicure','페디큐어'),('Lashes','속눈썹')])}</ol></div></section>
<section class="sec find" aria-labelledby="find-h"><div class="wrap split">{num("03","찾아오기")}
<div><h2 id="find-h">Suite #228, 4157 5th St</h2><p>Inside the building; follow the suite numbers to #228.</p></div>
<div><p class="muted">Hours per Google listing: Mon-Fri 9 AM-7 PM, Sat 9 AM-6 PM, Sun closed. Appointment only, so call to confirm.</p><div class="ctas">{dirb()}{call("btn btn-ink")}</div></div></div></section>'''
rows=''.join(f'<tr><th scope="row">{d}</th><td>{h}</td></tr>' for d,h in [("Monday","9 AM - 7 PM"),("Tuesday","9 AM - 7 PM"),("Wednesday","9 AM - 7 PM"),("Thursday","9 AM - 7 PM"),("Friday","9 AM - 7 PM"),("Saturday","9 AM - 6 PM"),("Sunday","Closed")])
visit=f'''<section class="phero"><div class="wrap narrow"><p class="eyebrow">Visit · <span lang="ko">찾아오기</span></p><h1>Suite #228</h1>
<address>{NAME} <span lang="ko">{KO}</span><br>{ADDR}<br>{CITY} (Koreatown)<br><a href="{TEL}">{PHONE}</a></address><div class="ctas">{dirb("btn btn-plum")}{call("btn btn-ink")}{igb()}</div></div></section>
<section class="sec"><div class="wrap narrow"><h2>Hours</h2><table class="hours"><thead><tr><th scope="col">Day</th><th scope="col">Listed hours</th></tr></thead><tbody>{rows}</tbody></table>
<p class="muted">Per Google and Yahoo listings. Appointment only; <a href="{TEL}">call {PHONE}</a> to confirm a time.</p>
<h2 style="margin-top:3rem">Finding the suite</h2><p>Inside the building at 4157 5th St; follow the suite numbers to #228. Parking: ask when you book.</p><p><a href="{MAPS}" target="_blank" rel="noopener">Open in Google Maps</a></p></div></section>'''
nf=f'<section class="phero"><div class="wrap narrow"><p class="eyebrow">404</p><h1>Not here</h1><p>That page doesn\'t exist.</p><div class="ctas"><a class="btn btn-ink" href="{B}">Back home</a>{call()}</div></div></section>'
open(R+'index.html','w').write(page('','HaNa Nail 하나네일 | Nail Salon by Appointment, Koreatown LA',"HaNa Nail, suite #228 at 4157 5th St in Koreatown, Los Angeles. By appointment: call (213) 905-9015 or message @hananail.la.",home,'',PRE))
open(R+'visit/index.html','w').write(page('visit/','Hours & Directions | HaNa Nail, Koreatown LA','HaNa Nail is in suite #228 at 4157 5th St, Los Angeles 90020. Listed hours Mon-Sat; appointment only. Call (213) 905-9015.',visit,'visit/'))
open(R+'404.html','w').write(page('404.html','Page not found | HaNa Nail','Page not found.',nf).replace('<link rel="canonical"','<meta name="robots" content="noindex"><link rel="x-canonical"'))
open(R+'sitemap.xml','w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>{SITE}{p}</loc><lastmod>2026-10-22</lastmod></url>' for p in ['','visit/'])+'</urlset>')
open(R+'robots.txt','w').write(f'User-agent: *\nAllow: /\nSitemap: {SITE}sitemap.xml\n'); open(R+'.nojekyll','w').write('')
print('ok')
