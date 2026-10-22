# Hero exports. Final run uses Real-ESRGAN x4 outputs (src/d4.png, src/m4.png); downsample only.
import sys,os
from PIL import Image
O='assets/img/'; S='src/'
d=Image.open(S+('d4.png' if os.path.exists(S+'d4.png') else 'd.jpg')).convert('RGB')
m=Image.open(S+('m4.png' if os.path.exists(S+'m4.png') else 'm.jpg')).convert('RGB')
W,H=m.size; h=round(W*5/4); m=m.crop((0,H-h,W,H))  # 4:5 keep top water for H1, koi lower
def out(im,name,widths,size,qa=58):
  for w in widths:
    r=im.resize((w,round(w*size[1]/size[0])),Image.LANCZOS); r.save(f'{O}{name}-{w}.avif',quality=qa); r.save(f'{O}{name}-{w}.webp',quality=82,method=6)
out(d.resize((2880,1620),Image.LANCZOS) if d.width>=2880 else d,'hero-d',(1280,1920,2880),(2880,1620))
out(m,'hero-m',(800,1200,1600),(1600,2000))
og=d.resize((1200,675),Image.LANCZOS).crop((0,22,1200,652))
from PIL import ImageDraw,ImageFont
dr=ImageDraw.Draw(og,'RGBA');f=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',20);g=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',56)
dr.text((60,420),'HaNa Nail',font=g,fill='#22302B');dr.text((60,495),'Suite #228, 4157 5th St, Koreatown',font=f,fill='#22302B')
dr.rectangle((960,580,1185,612),fill=(34,48,43,190));dr.text((972,585),'ILLUSTRATIVE (AI)',font=f,fill='#EEF0EC')
og.save(O+'og.jpg',quality=85);print('src',d.size,m.size)
