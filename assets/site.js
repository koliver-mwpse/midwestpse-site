const mb=document.querySelector('.menu-btn'),nav=document.querySelector('.nav');
mb&&mb.addEventListener('click',()=>{const o=nav.classList.toggle('open');mb.setAttribute('aria-expanded',o)});
document.querySelectorAll('.vid[data-src]').forEach(b=>b.addEventListener('click',()=>{
  const v=document.createElement('video');v.src=b.dataset.src;v.controls=v.autoplay=v.playsInline=true;v.poster=b.querySelector('img').src;b.replaceChildren(v);v.play().catch(()=>{})},{once:true}));
document.querySelectorAll('.vid[data-id]').forEach(b=>b.addEventListener('click',()=>{
  const f=document.createElement('iframe');f.src=`https://www.youtube-nocookie.com/embed/${b.dataset.id}?autoplay=1&rel=0&playsinline=1`;
  f.allow='autoplay; encrypted-media; picture-in-picture; fullscreen';f.allowFullscreen=true;f.title=b.getAttribute('aria-label');b.replaceChildren(f)},{once:true}));
const io='IntersectionObserver' in window&&new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{threshold:.12});
document.querySelectorAll('.reveal').forEach(el=>io?io.observe(el):el.classList.add('in'));
const q=document.querySelector('form.quote');
q&&q.addEventListener('submit',e=>{e.preventDefault();const d=new FormData(q);
  const body=[...d].filter(([k,v])=>v&&k!=='message').map(([k,v])=>`${k}: ${v}`).join('\n')+'\n\n'+(d.get('message')||'');
  location.href=`mailto:koliver@midwestpse.com?subject=${encodeURIComponent('Quote request – '+(d.get('Service')||'General'))}&body=${encodeURIComponent(body)}`});
document.querySelectorAll('[data-year]').forEach(e=>e.textContent=new Date().getFullYear());
