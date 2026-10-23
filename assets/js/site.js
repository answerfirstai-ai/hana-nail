(function(){
  var d=document,root=d.documentElement,reduce=matchMedia('(prefers-reduced-motion:reduce)').matches;
  if(!reduce)root.classList.add('js');
  var sets=[].slice.call(d.querySelectorAll('.set')),links=[].slice.call(d.querySelectorAll('.rail a')),top=d.querySelector('.top');
  // the header ground follows the set under the 35% line (instant under reduced motion; the CSS transition is gated)
  function activate(el){
    links.forEach(function(a){a.setAttribute('aria-current',el&&a.getAttribute('href')==='#'+el.id?'true':'false')});
    if(el){top.style.setProperty('--hc',getComputedStyle(el).backgroundColor);top.style.setProperty('--hi',el.dataset.tone==='light'?'#fff':'#24241f')}
    else{top.style.removeProperty('--hc');top.style.removeProperty('--hi')}
  }
  var ticking=false;
  function tick(){ticking=false;var line=innerHeight*0.35,cur=null;sets.forEach(function(s){var r=s.getBoundingClientRect();if(r.top<=line&&r.bottom>line)cur=s});activate(cur)}
  function req(){if(!ticking){ticking=true;requestAnimationFrame(tick)}}
  addEventListener('scroll',req,{passive:true});addEventListener('resize',req);tick();
  // photographs open once with a clip reveal; anything already in view, jumped to, or printed shows at once
  if(!reduce&&'IntersectionObserver' in window){
    var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{threshold:.12});
    sets.forEach(function(s){io.observe(s)});
    addEventListener('hashchange',function(){var t=d.querySelector(location.hash||'#none');if(t&&t.classList.contains('set'))t.classList.add('in')});
    addEventListener('beforeprint',function(){sets.forEach(function(s){s.classList.add('in')})});
  }else sets.forEach(function(s){s.classList.add('in')});
  // kinetic type: each headline rises out of one mask (per-word inline-block masks made the inspector flag ragged-edges, so the mask wraps the whole headline) (text stays readable without script; hidden start state lives only in CSS under no-preference)
  d.querySelectorAll('.kt').forEach(function(h){var t=h.textContent.trim();h.setAttribute('aria-label',t);h.innerHTML='<span class="w" aria-hidden="true"><span>'+t+'</span></span>'});
  // holographic sheen on the chrome photo: pointer on desktop, scroll position on phones; no listeners under reduced motion
  var holo=d.querySelector('.holo');
  if(holo&&!reduce){
    var setx=function(t){holo.style.setProperty('--x',(t*150-20)+'%')},hq=false;
    holo.addEventListener('pointermove',function(e){var r=holo.getBoundingClientRect();setx((e.clientX-r.left)/r.width)});
    addEventListener('scroll',function(){if(hq)return;hq=true;requestAnimationFrame(function(){hq=false;var r=holo.getBoundingClientRect();if(r.bottom>0&&r.top<innerHeight)setx(Math.min(1,Math.max(0,1-r.top/innerHeight)))})},{passive:true});
  }
  // Esc closes anything open (the design has no menu; kept for any <details> added later)
  d.addEventListener('keydown',function(e){if(e.key==='Escape'){var o=d.querySelector('details[open]');if(o)o.removeAttribute('open')}});
})();
