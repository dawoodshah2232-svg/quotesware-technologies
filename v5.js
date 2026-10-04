(function(){
  // mobile menu
  var burger=document.querySelector('.burger'), menu=document.querySelector('.mobile-menu');
  if(burger&&menu){
    burger.addEventListener('click',function(){
      var open=menu.classList.toggle('open');
      burger.setAttribute('aria-expanded',String(open));
    });
    menu.querySelectorAll('a').forEach(function(a){
      a.addEventListener('click',function(){menu.classList.remove('open');burger.setAttribute('aria-expanded','false');});
    });
  }
  // scroll reveal
  var io=new IntersectionObserver(function(entries){
    entries.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}});
  },{threshold:.12,rootMargin:'0px 0px -6%'});
  document.querySelectorAll('.rv').forEach(function(el){io.observe(el);});
  // footer year
  document.querySelectorAll('[data-year]').forEach(function(el){el.textContent=new Date().getFullYear();});
  // demo form (front-end only until inbox is connected)
  document.querySelectorAll('[data-contact-form]').forEach(function(form){
    form.addEventListener('submit',function(e){
      e.preventDefault();
      if(!form.reportValidity())return;
      var status=form.querySelector('.contact-status');
      if(status){status.hidden=false;status.textContent='Thanks — your request has been noted. Our team will follow up with demo access details shortly.';}
      form.reset();
    });
  });
  // subtle hero parallax (desktop pointers only)
  var hv=document.querySelector('.hero-visual');
  if(hv&&matchMedia('(pointer:fine)').matches&&!matchMedia('(prefers-reduced-motion:reduce)').matches){
    var img=hv.querySelector('img');
    hv.closest('.hero').addEventListener('pointermove',function(e){
      var r=hv.getBoundingClientRect();
      var x=(e.clientX-(r.left+r.width/2))/r.width, y=(e.clientY-(r.top+r.height/2))/r.height;
      img.style.translate=(x*10)+'px '+(y*8)+'px';
    });
    hv.closest('.hero').addEventListener('pointerleave',function(){img.style.translate='0 0';});
  }
})();
