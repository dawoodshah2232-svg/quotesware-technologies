(function(){
  const menuBtn=document.querySelector('.menu-button');
  const mobile=document.querySelector('.mobile-panel');
  if(menuBtn&&mobile){
    menuBtn.addEventListener('click',()=>{
      const open=mobile.classList.toggle('open');
      menuBtn.setAttribute('aria-expanded',String(open));
      document.body.classList.toggle('menu-open',open);
    });
    mobile.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>{
      mobile.classList.remove('open'); menuBtn.setAttribute('aria-expanded','false'); document.body.classList.remove('menu-open');
    }));
  }
  const io=new IntersectionObserver((entries)=>{
    entries.forEach(entry=>{if(entry.isIntersecting){entry.target.classList.add('in');io.unobserve(entry.target)}});
  },{threshold:.12,rootMargin:'0px 0px -6%'});
  document.querySelectorAll('.reveal,.stagger').forEach(el=>io.observe(el));
  document.querySelectorAll('[data-year]').forEach(el=>el.textContent=new Date().getFullYear());
  document.querySelectorAll('[data-contact-form]').forEach(form=>{
    form.addEventListener('submit',e=>{
      e.preventDefault();
      if(!form.reportValidity()) return;
      const payload=Object.fromEntries(new FormData(form).entries());
      try{localStorage.setItem('quotesware-demo-request-draft',JSON.stringify({...payload,savedAt:new Date().toISOString()}))}catch(_e){}
      const status=form.querySelector('.contact-status');
      if(status){status.textContent='Your request is saved on this device, but QuotesWare has not connected a production inbox/CRM endpoint to this website yet. No message has been sent.';status.classList.add('show');}
    });
  });
  const stage=document.querySelector('[data-stage]');
  if(stage && matchMedia('(pointer:fine)').matches && !matchMedia('(prefers-reduced-motion:reduce)').matches){
    stage.addEventListener('pointermove',e=>{const r=stage.getBoundingClientRect();const x=(e.clientX-r.left)/r.width-.5;const y=(e.clientY-r.top)/r.height-.5;stage.style.transform=`translate3d(${x*5}px,${y*4}px,0)`;});
    stage.addEventListener('pointerleave',()=>stage.style.transform='');
  }
})();
