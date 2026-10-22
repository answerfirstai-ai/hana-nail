// One motion idea: each section's single celadon stroke (ㅡ) draws as it enters (native scroll).
(()=>{document.querySelectorAll('.mnav a').forEach(a=>a.addEventListener('click',()=>a.closest('details').open=false));
if(matchMedia('(prefers-reduced-motion: reduce)').matches)return;const s=[...document.querySelectorAll('main .ieung path')];let t=0;
function f(){t=0;const vh=innerHeight;for(const p of s){const r=p.getBoundingClientRect();let k=(vh*.95-r.top)/(vh*.5);k=Math.max(0,Math.min(1,k));p.style.setProperty('--d',(620*(1-k)).toFixed(1))}}
addEventListener('scroll',()=>{if(!t){t=1;requestAnimationFrame(f)}},{passive:true});f();})();
