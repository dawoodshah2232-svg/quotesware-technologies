/* QuotesWare Technologies — motion layer (Apple principles: instant response, interruptible, transform/opacity only) */
(function(){
  "use strict";
  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var finePointer = window.matchMedia("(pointer: fine)").matches;

  /* ---- Word-by-word splitting ---- */
  function splitWords(el){
    var text = el.textContent.trim().split(/\s+/);
    el.setAttribute("aria-label", el.textContent.trim());
    el.textContent = "";
    text.forEach(function(word, i){
      var s = document.createElement("span");
      s.className = "w";
      s.textContent = word;
      s.setAttribute("aria-hidden", "true");
      s.style.transitionDelay = (i * 55) + "ms";
      el.appendChild(s);
      el.appendChild(document.createTextNode(" "));
    });
  }
  var heroTitle = document.getElementById("heroTitle");
  if (heroTitle && !reduceMotion){
    splitWords(heroTitle);
    requestAnimationFrame(function(){
      requestAnimationFrame(function(){
        heroTitle.querySelectorAll(".w").forEach(function(w){ w.classList.add("in"); });
      });
    });
  }
  document.querySelectorAll(".reveal-words").forEach(function(el){
    if (reduceMotion) return;
    splitWords(el);
  });

  /* ---- Scroll reveals (IntersectionObserver, staggered) ---- */
  var io = new IntersectionObserver(function(entries){
    entries.forEach(function(e){
      if (!e.isIntersecting) return;
      var el = e.target;
      if (el.hasAttribute("data-stagger")){
        var kids = el.querySelectorAll(":scope > .reveal");
        kids.forEach(function(k, i){ k.style.transitionDelay = (i * 90) + "ms"; k.classList.add("in"); });
      } else {
        el.classList.add("in");
        if (el.classList.contains("reveal-words")){
          el.querySelectorAll(".w").forEach(function(w, i){
            w.style.transitionDelay = (i * 45) + "ms";
          });
        }
      }
      io.unobserve(el);
    });
  }, { threshold: 0.12, rootMargin: "0px 0px -8% 0px" });
  document.querySelectorAll(".reveal, .reveal-words, [data-stagger]").forEach(function(el){ io.observe(el); });

  /* ---- Animated nav: hide on scroll down, reveal on up ---- */
  var nav = document.getElementById("nav");
  var lastY = window.scrollY;
  var ticking = false;
  function onScroll(){
    var y = window.scrollY;
    if (y > 140 && y > lastY + 4) nav.classList.add("nav-hidden");
    else if (y < lastY - 4 || y < 140) nav.classList.remove("nav-hidden");
    lastY = y;
    ticking = false;
  }
  window.addEventListener("scroll", function(){
    if (!ticking){ requestAnimationFrame(onScroll); ticking = true; }
  }, { passive: true });

  /* ---- Mobile menu ---- */
  var toggle = document.getElementById("navToggle");
  var menu = document.getElementById("mobileMenu");
  toggle.addEventListener("click", function(){
    var open = menu.classList.toggle("open");
    toggle.setAttribute("aria-expanded", open ? "true" : "false");
    toggle.setAttribute("aria-label", open ? "Close menu" : "Open menu");
  });
  menu.querySelectorAll("a").forEach(function(a){
    a.addEventListener("click", function(){
      menu.classList.remove("open");
      toggle.setAttribute("aria-expanded", "false");
    });
  });

  /* ---- Hero canvas: slow-drifting gradient blobs (GPU-cheap) ---- */
  var canvas = document.getElementById("heroBg");
  if (canvas && !reduceMotion){
    var ctx = canvas.getContext("2d");
    var blobs = [
      { x:.22, y:.30, r:.34, c:"46,91,255",  a:.34, sx:.00016, sy:.00011, p:0.0 },
      { x:.78, y:.62, r:.30, c:"120,80,255", a:.22, sx:.00012, sy:.00017, p:2.1 },
      { x:.55, y:.18, r:.24, c:"40,200,255", a:.16, sx:.00019, sy:.00009, p:4.2 }
    ];
    var W, H, t0 = performance.now();
    function size(){
      var r = canvas.parentElement.getBoundingClientRect();
      W = canvas.width = Math.floor(r.width);
      H = canvas.height = Math.floor(r.height);
    }
    size();
    window.addEventListener("resize", size);
    var heroInner = document.querySelector(".hero-inner");
    var lift = 0, targetLift = 0;
    window.addEventListener("scroll", function(){
      targetLift = Math.min(window.scrollY * 0.12, 160);
    }, { passive: true });
    (function draw(now){
      var t = (now - t0) / 1000;
      ctx.clearRect(0, 0, W, H);
      blobs.forEach(function(b){
        var x = (b.x + Math.sin(t * b.sx * 1000 + b.p) * 0.06) * W;
        var y = (b.y + Math.cos(t * b.sy * 1000 + b.p) * 0.06) * H;
        var g = ctx.createRadialGradient(x, y, 0, x, y, b.r * Math.max(W, H));
        g.addColorStop(0, "rgba(" + b.c + "," + b.a + ")");
        g.addColorStop(1, "rgba(" + b.c + ",0)");
        ctx.fillStyle = g;
        ctx.fillRect(0, 0, W, H);
      });
      lift += (targetLift - lift) * 0.08; /* critically-damped-ish follow */
      if (heroInner) heroInner.style.transform = "translate3d(0," + (-lift).toFixed(1) + "px,0)";
      requestAnimationFrame(draw);
    })(t0);
  }

  /* ---- Magnetic buttons (desktop only) ---- */
  if (finePointer && !reduceMotion){
    document.querySelectorAll(".magnetic").forEach(function(btn){
      var x = 0, y = 0, tx = 0, ty = 0, raf = null;
      function loop(){
        x += (tx - x) * 0.18; y += (ty - y) * 0.18;
        btn.style.transform = "translate3d(" + x.toFixed(1) + "px," + y.toFixed(1) + "px,0)";
        if (Math.abs(tx - x) > 0.1 || Math.abs(ty - y) > 0.1) raf = requestAnimationFrame(loop);
        else { btn.style.transform = ""; raf = null; }
      }
      btn.addEventListener("pointermove", function(e){
        var r = btn.getBoundingClientRect();
        tx = (e.clientX - (r.left + r.width / 2)) * 0.22;
        ty = (e.clientY - (r.top + r.height / 2)) * 0.28;
        if (!raf) raf = requestAnimationFrame(loop);
      });
      btn.addEventListener("pointerleave", function(){
        tx = 0; ty = 0;
        if (!raf) raf = requestAnimationFrame(loop);
      });
    });

    /* ---- Tilt cards (desktop only) ---- */
    document.querySelectorAll(".tilt").forEach(function(card){
      var raf = null;
      card.addEventListener("pointermove", function(e){
        if (raf) return;
        raf = requestAnimationFrame(function(){
          var r = card.getBoundingClientRect();
          var rx = ((e.clientY - r.top) / r.height - 0.5) * -7;
          var ry = ((e.clientX - r.left) / r.width - 0.5) * 9;
          card.style.transform = "perspective(900px) rotateX(" + rx.toFixed(2) + "deg) rotateY(" + ry.toFixed(2) + "deg) translateY(-4px)";
          raf = null;
        });
      });
      card.addEventListener("pointerleave", function(){
        card.style.transform = ""; /* spring-back via CSS transition */
      });
    });
  }

  /* ---- Contact form (front-end only; wire to inbox on content pass) ---- */
  var form = document.getElementById("contactForm");
  var note = document.getElementById("formNote");
  form.addEventListener("submit", function(e){
    e.preventDefault();
    if (!form.checkValidity()){ form.reportValidity(); return; }
    note.textContent = "Thanks — your message is noted. We'll be in touch shortly.";
    form.querySelectorAll("input, textarea").forEach(function(f){ f.value = ""; });
  });
})();
