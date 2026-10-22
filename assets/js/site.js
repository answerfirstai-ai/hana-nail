(()=>{const d=document.querySelector('.mnav');if(d){d.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>d.open=false));
document.addEventListener('keydown',e=>{if(e.key==='Escape'&&d.open){d.open=false;d.querySelector('summary').focus()}})}
// signature: index with preview (palette rows -> one fixed frame; inline on phones)
const rows=[...document.querySelectorAll('.row')],pv=[...document.querySelectorAll('.pv-i')];
const show=k=>{rows.forEach(r=>r.setAttribute('aria-pressed',r.dataset.k===k));pv.forEach(p=>p.classList.toggle('on',p.dataset.k===k))};
rows.forEach(r=>{r.addEventListener('click',()=>show(r.dataset.k));r.addEventListener('mouseenter',()=>matchMedia('(hover:hover)').matches&&show(r.dataset.k));r.addEventListener('focus',()=>show(r.dataset.k))});
// entrances: only for elements below the fold; heading, text, picture staggered
if(matchMedia('(prefers-reduced-motion: reduce)').matches||!('IntersectionObserver'in window))return;
document.documentElement.classList.add('js');
const groups=[...document.querySelectorAll('.feat,.sheet,.pals,.contact,.v-g,.cs .run')];
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.querySelectorAll('.pre').forEach(x=>x.classList.add('in'));io.unobserve(e.target)}}),{rootMargin:'0px 0px -8% 0px'});
groups.forEach(g=>{if(g.getBoundingClientRect().top<innerHeight)return;[...g.querySelectorAll(':scope > h2, :scope > p, :scope > .pal-list > *, :scope > div:not(.runs), :scope > figure, .rows > li, .fr')].forEach((x,i)=>{x.classList.add('pre');x.style.setProperty('--dl',Math.min(i,8)*70+'ms')});io.observe(g)});
const reveal=()=>document.querySelectorAll('.pre').forEach(x=>x.classList.add('in'));
addEventListener('hashchange',reveal);if(location.hash)reveal();addEventListener('beforeprint',reveal);})();
