HEADER = """<header class="site-header">
  <div class="wrap nav">
    <a class="brand" href="index.html" aria-label="QuotesWare Technologies home"><img src="assets/logo.png" alt="QuotesWare Technologies" width="172" height="42"></a>
    <nav class="nav-links" aria-label="Primary">
      <div class="has-drop">
        <button class="nav-link" type="button" aria-haspopup="true">Products <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M6 9l6 6 6-6"/></svg></button>
        <div class="drop" role="menu">
          <a href="platform.html"><span><b>Trading Platform</b><span>The connected Orbit ecosystem</span></span></a>
          <a href="trader.html"><span><b>Orbit Trader</b><span>Charts, orders, positions — web, Android, Windows</span></span></a>
          <a href="web-terminal.html"><span><b>Web Terminal</b><span>Zero-install browser trading</span></span></a>
          <a href="mobile.html"><span><b>Mobile</b><span>Orbit Trader for Android</span></span></a>
          <a href="algo.html"><span><b>Algo & Automation</b><span>Bots, testing and automation roadmap</span></span></a>
          <a href="manager.html"><span><b>Orbit Manager</b><span>Clients, exposure, dealing, reporting</span></span></a>
          <a href="administrator.html"><span><b>Orbit Administrator</b><span>Symbols, groups, permissions, infrastructure</span></span></a>
          <a href="white-label.html"><span><b>White Label</b><span>Your brand on Orbit technology</span></span></a>
          <a href="downloads.html"><span><b>Downloads</b><span>Platform availability</span></span></a>
        </div>
      </div>
      <div class="has-drop">
        <button class="nav-link" type="button" aria-haspopup="true">Technology <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M6 9l6 6 6-6"/></svg></button>
        <div class="drop" role="menu">
          <a href="connectivity.html"><span><b>Connectivity</b><span>Market data and feed adapters</span></span></a>
          <a href="developers.html"><span><b>Developer Platform</b><span>APIs, SDKs and integration surfaces</span></span></a>
          <a href="security.html"><span><b>Security</b><span>Access control, audit and resilience</span></span></a>
          <a href="developers.html#apis"><span><b>APIs</b><span>REST, WebSocket, webhooks, FIX roadmap</span></span></a>
          <a href="brokers.html"><span><b>Broker Infrastructure</b><span>Deployment and operations</span></span></a>
        </div>
      </div>
      <div><a class="nav-link" href="brokers.html">For Brokers</a></div>
      <div><a class="nav-link" href="company.html">Company</a></div>
      <div><a class="nav-link" href="resources.html">Resources</a></div>
    </nav>
    <div class="nav-cta">
      <a class="btn btn-ghost" href="downloads.html">Downloads</a>
      <a class="btn btn-primary" href="contact.html">Request Demo</a>
      <button class="burger" aria-label="Open menu" aria-expanded="false"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button>
    </div>
  </div>
  <nav class="mobile-menu" aria-label="Mobile">
    <a class="mlink" href="platform.html">Trading Platform</a>
    <a class="mlink" href="trader.html">Orbit Trader</a>
    <a class="mlink" href="manager.html">Orbit Manager</a>
    <a class="mlink" href="administrator.html">Orbit Administrator</a>
    <a class="mlink" href="white-label.html">White Label</a>
    <a class="mlink" href="web-terminal.html">Web Terminal</a>
    <a class="mlink" href="mobile.html">Mobile</a>
    <a class="mlink" href="algo.html">Algo & Automation</a>
    <a class="mlink" href="news.html">News</a>
    <a class="mlink" href="connectivity.html">Connectivity</a>
    <a class="mlink" href="developers.html">Developers</a>
    <a class="mlink" href="security.html">Security</a>
    <a class="mlink" href="brokers.html">For Brokers</a>
    <a class="mlink" href="company.html">Company</a>
    <a class="mlink" href="resources.html">Resources</a>
    <div class="mrow">
      <a class="btn btn-ghost" href="downloads.html" style="flex:1">Downloads</a>
      <a class="btn btn-primary" href="contact.html" style="flex:1">Request Demo</a>
    </div>
  </nav>
</header>"""

FOOTER = """<footer>
  <div class="wrap">
    <div class="foot-grid">
      <div class="foot-brand"><img src="assets/logo-light.png" alt="QuotesWare Technologies" width="172" height="42"><p>Modern trading technology: Orbit Trader for traders, Orbit Manager and Administrator for brokerages.</p></div>
      <div class="foot-col"><h4>Products</h4><a href="trader.html">Orbit Trader</a><a href="web-terminal.html">Web Terminal</a><a href="mobile.html">Mobile</a><a href="manager.html">Orbit Manager</a><a href="administrator.html">Orbit Administrator</a><a href="algo.html">Algo & Automation</a><a href="white-label.html">White Label</a></div>
      <div class="foot-col"><h4>Technology</h4><a href="connectivity.html">Connectivity</a><a href="developers.html">Developer Platform</a><a href="security.html">Security</a><a href="downloads.html">Downloads</a></div>
      <div class="foot-col"><h4>Business</h4><a href="brokers.html">For Brokers</a><a href="contact.html">Request Demo</a><a href="resources.html">Resources</a></div>
      <div class="foot-col"><h4>Company</h4><a href="company.html">About QuotesWare</a><a href="news.html">News</a><a href="careers.html">Careers</a><a href="media.html">Media Kit</a><a href="resources.html#roadmap">Roadmap</a><a href="contact.html">Contact</a></div>
    </div>
    <div class="foot-base"><span>&copy; <span data-year>2026</span> QuotesWare Technologies. All rights reserved.</span><span><a href="privacy.html" style="color:rgba(255,255,255,.72)">Privacy</a> &middot; <a href="terms.html" style="color:rgba(255,255,255,.72)">Terms</a> &middot; <a href="cookies.html" style="color:rgba(255,255,255,.72)">Cookies</a></span></div>
    <p class="foot-disc">QuotesWare Technologies provides trading software technology only. It does not provide investment, brokerage, or financial services, and does not accept client funds.</p>
  </div>
</footer>
<script src="v5.js"></script>"""


PAGES = []
def page(slug, title, desc, body):
    PAGES.append((slug, title, desc, body))

def crumb(label):
    return f'<div class="crumb rv"><a href="index.html">Home</a> &middot; <span>{label}</span></div>'

def hero(img, eyebrow, title, lede, buttons, alt, label, variant="split"):
    btns = "".join(buttons)
    c = crumb(label)
    if variant == "min":
        return f"""<section class="hero hero-min"><div class="wrap">{c}<span class="eyebrow rv">{eyebrow}</span><h1 class="rv">{title}</h1><p class="lede rv d1">{lede}</p></div></section>"""
    if variant == "center":
        return f"""<section class="hero hero-center"><div class="wrap">{c}<span class="eyebrow rv">{eyebrow}</span><h1 class="rv">{title}</h1><p class="lede rv d1">{lede}</p><div class="hero-btns rv d2">{btns}</div><div class="vis rv d3"><img class="main" src="{img}" alt="{alt}" loading="lazy"></div></div></section>"""
    vcls = {"split": "", "flip": " flip", "dark": " dark", "light": " light"}[variant]
    return f"""<section class="hero{vcls}"><div class="wrap split">
<div class="vis rv"><img class="main" src="{img}" alt="{alt}" loading="lazy"></div>
<div class="rv d1">{c}<span class="eyebrow">{eyebrow}</span><h1>{title}</h1><p class="lede">{lede}</p><div class="hero-btns">{btns}</div></div>
</div></section>"""

def feat(icon, t, d):
    return f"""<div class="feat-card rv"><div class="fic">{ICONS[icon]}</div><h3>{t}</h3><p>{d}</p></div>"""

def checklist(items):
    lis = "".join(f"<li>{i}</li>" for i in items)
    return f'<ul class="checklist">{lis}</ul>'

def stats_band(stats):
    cells = "".join(f'<div class="stat rv"><b>{v}</b><span>{l}</span></div>' for v, l in stats)
    return f'<section class="section" style="padding-top:0"><div class="wrap"><div class="stat-band">{cells}</div></div></section>'

def steps(items):
    cards = "".join(f'<div class="step rv"><div class="n">{i+1}</div><div><h3>{t}</h3><p>{d}</p></div></div>' for i, (t, d) in enumerate(items))
    return f'<div class="steps">{cards}</div>'

def band_cta(h, p, btn, href):
    return f"""<section class="section"><div class="wrap"><div class="band-cta rv"><div><h2>{h}</h2><p>{p}</p></div><a class="btn btn-primary" href="{href}">{btn}</a></div></div></section>"""

ICONS = {
"chart": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 3v18h18"/><path d="M7 15l4-6 4 3 4-7"/></svg>',
"bolt": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2L4.5 13.5H11L9.5 22 19 9.5h-6.5L13 2z"/></svg>',
"shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2l8 3.5v5.2c0 5-3.4 9.4-8 11.3-4.6-1.9-8-6.3-8-11.3V5.5L12 2z"/><path d="M9 12l2 2 4-4"/></svg>',
"users": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="8" r="3.5"/><path d="M2.5 20c.8-3.5 3.4-5.5 6.5-5.5s5.7 2 6.5 5.5"/><circle cx="17" cy="9" r="2.6"/><path d="M16 14.6c2.9.2 4.9 2 5.5 5.4"/></svg>',
"globe": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.6 3.8 5.7 3.8 9s-1.3 6.4-3.8 9c-2.5-2.6-3.8-5.7-3.8-9S9.5 5.6 12 3z"/></svg>',
"layers": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2l9 5-9 5-9-5 9-5z"/><path d="M3 12l9 5 9-5"/><path d="M3 17l9 5 9-5"/></svg>',
"cog": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3.2"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M4.9 4.9l2.1 2.1M17 17l2.1 2.1M19.1 4.9L17 7M7 17l-2.1 2.1"/></svg>',
"code": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M16 18l6-6-6-6M8 6l-6 6 6 6"/></svg>',
"star": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2.5l2.9 6 6.6.9-4.8 4.6 1.2 6.5L12 17.4 6.1 20.5l1.2-6.5L2.5 9.4l6.6-.9 2.9-6z"/></svg>',
"phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="7" y="2.5" width="10" height="19" rx="2.5"/><path d="M11 18.5h2"/></svg>',
"check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12.5l5 5L20 6.5"/></svg>',
}

# ================= PLATFORM (dark hero) =================
page("platform.html", "The Orbit Platform — One Stack for the Entire Brokerage",
     "Orbit is a connected trading technology stack: Orbit Trader for clients, Orbit Manager for operations, Orbit Administrator for control.",
     hero("assets/products/orbit-ecosystem-dark.png", "The Orbit Platform", "One stack.<br>Entire brokerage.",
          "Orbit is a connected trading technology stack — a trader terminal, broker operations, and platform administration designed together and deployed as one.",
          ['<a class="btn btn-primary" href="contact.html">Request Demo</a>', '<a class="btn btn-ghost" href="trader.html">Explore Orbit Trader</a>'],
          "Orbit ecosystem on laptop, tablet and phone", "Platform", "dark")
     + stats_band([("3", "Core products"), ("3", "Client platforms"), ("1", "Integrated stack"), ("1", "Technology partner")])
     + """<section class="section alt"><div class="wrap">
<div class="sec-head rv"><span class="eyebrow">The stack</span><h2>Three products. One philosophy.</h2><p>Every surface shares the same design language, the same account model, and the same commitment to clarity.</p></div>
<div class="fam-grid">
<article class="fam-card rv"><div class="fam-shot"><img src="assets/products/orbit-trader-light.png" alt="Orbit Trader" loading="lazy" style="object-position:center"></div><div class="fam-body"><span class="tag">For traders</span><h3>Orbit Trader</h3><p>Market Watch, advanced charts, order ticket and positions — on web, Android and Windows.</p><a class="more" href="trader.html">Explore Trader</a></div></article>
<article class="fam-card rv d1"><div class="fam-shot"><img src="assets/products/orbit-manager-light.png" alt="Orbit Manager" loading="lazy" style="object-position:center"></div><div class="fam-body"><span class="tag">For brokers</span><h3>Orbit Manager</h3><p>Client oversight, exposure, dealing workflows and reporting for the dealing desk.</p><a class="more" href="manager.html">Explore Manager</a></div></article>
<article class="fam-card rv d2"><div class="fam-shot"><img src="assets/products/orbit-admin-dark.png" alt="Orbit Administrator" loading="lazy" style="object-position:center"></div><div class="fam-body"><span class="tag">For admins</span><h3>Orbit Administrator</h3><p>Symbols, groups, permissions, servers and audit — platform control in one place.</p><a class="more" href="administrator.html">Explore Administrator</a></div></article>
</div></div></section>"""
     + """<section class="section tint"><div class="wrap split flip">
<div class="vis rv"><img class="main" src="assets/products/orbit-trader-devices.png" alt="Orbit Trader across devices" loading="lazy"></div>
<div class="rv d1"><span class="eyebrow">Consistency</span><h2>One account. Every screen.</h2>
<p class="lede">A position opened on the desktop terminal is visible on the web and on mobile — same watchlists, same orders, same state.</p>
""" + checklist(["Shared account model across products", "Consistent design language", "Single integration surface for brokers", "White-label ready throughout"]) + """
<a class="btn btn-primary" href="white-label.html">White Label Options</a></div></div></section>"""
     + band_cta("See the stack in action.", "Request a guided walkthrough of the full Orbit platform.", "Request Demo", "contact.html"))

# ================= TRADER (light hero) =================
page("trader.html", "Orbit Trader — Professional Trading Terminal",
     "Orbit Trader: Market Watch, advanced charts, precise order entry and full position management on web, Android and Windows.",
     hero("assets/products/orbit-trader-light.png", "Orbit Trader", "Professional trading.<br>Clean execution.",
          "Market Watch, advanced charts, a precise order ticket and full position management — a terminal that stays out of the trader's way.",
          ['<a class="btn btn-primary" href="contact.html">Request Demo</a>', '<a class="btn btn-ghost" href="downloads.html">Get the App</a>'],
          "Orbit Trader light-theme terminal on laptop", "Orbit Trader", "light")
     + """<section class="section alt"><div class="wrap">
<div class="sec-head rv"><span class="eyebrow">The terminal</span><h2>Everything a trader needs. Nothing they don't.</h2></div>
<div class="feat-grid">"""
     + feat("globe", "Market Watch", "Multi-asset quotes with bid/ask and change — search, sort and organize by symbol.")
     + feat("chart", "Advanced Charts", "Candlestick charts across timeframes with indicators and drawing tools.")
     + feat("bolt", "Order Ticket", "Market, limit and stop orders with SL/TP, margin estimate and spread before you commit.")
     + feat("layers", "Positions & Orders", "Live positions with P/L, working orders and full trade history.")
     + feat("star", "Multi-Asset", "FX, metals, crypto, indices and stocks in one watchlist, one ticket.")
     + feat("check", "Cross-Device Sync", "Watchlists, positions and orders follow the account across web, Android and Windows.")
     + """</div></div></section>"""
     + """<section class="section dark"><div class="wrap split">
<div class="rv"><span class="eyebrow">Charting</span><h2 style="color:#fff">Charts that reward attention.</h2>
<p class="lede" style="color:rgba(255,255,255,.7)">Multiple timeframes, indicator overlays and precise crosshairs — built for traders who read price, not decoration.</p>
""" + checklist(["Candlestick charts across timeframes", "RSI, MACD and moving averages", "Volume profile at a glance", "Drawing tools for levels and zones"]) + """
</div><div class="vis rv d1"><img class="main" src="assets/products/orbit-chart-dark.png" alt="Orbit Trader chart with order ticket" loading="lazy"></div>
</div></section>"""
     + """<section class="section tint"><div class="wrap">
<div class="sec-head rv"><span class="eyebrow">Platforms</span><h2>Trade where your traders are.</h2></div>
<div class="plat-grid">
<div class="plat-card rv"><div class="picon">""" + ICONS["globe"] + """</div><h3>Web Terminal</h3><p>Zero-install trading in any modern browser.</p><a class="btn btn-ghost" href="web-terminal.html">Explore Web</a></div>
<div class="plat-card rv d1"><div class="picon">""" + ICONS["phone"] + """</div><h3>Android</h3><p>The full terminal in your pocket.</p><a class="btn btn-ghost" href="mobile.html">Explore Mobile</a></div>
<div class="plat-card rv d2"><div class="picon">""" + ICONS["layers"] + """</div><h3>Windows</h3><p>Native desktop power for dealing screens.</p><a class="btn btn-ghost" href="downloads.html">Downloads</a></div>
</div></div></section>"""
     + band_cta("Put Orbit Trader in front of traders.", "Request a demo and see the terminal live.", "Request Demo", "contact.html"))

# ================= WEB TERMINAL (light hero) =================
page("web-terminal.html", "Orbit Trader Web Terminal — Zero-Install Browser Trading",
     "Trade from any browser with the Orbit Trader web terminal: market watch, advanced charts, order entry and positions with no install.",
     hero("assets/products/orbit-web-light.png", "Web Terminal", "The terminal,<br>in your browser.",
          "Zero-install trading with Market Watch, advanced charts, order entry and positions — on any modern browser, on any machine.",
          ['<a class="btn btn-primary" href="contact.html">Request Demo</a>', '<a class="btn btn-ghost" href="trader.html">Orbit Trader</a>'],
          "Orbit Trader web terminal interface", "Web Terminal", "light")
     + """<section class="section alt"><div class="wrap">
<div class="sec-head rv"><span class="eyebrow">Browser trading</span><h2>No download. No update prompts. No friction.</h2><p>The web terminal removes every barrier between a new client and their first trade.</p></div>
<div class="feat-grid">"""
     + feat("bolt", "Instant Access", "Launch from your brokerage domain and trade — no installer, no admin rights, no waiting.")
     + feat("chart", "Full Charting", "Multi-timeframe candlestick charts with indicators and drawing tools, just like desktop.")
     + feat("layers", "Order Management", "Market, limit and stop orders with SL/TP, plus live positions and history.")
     + feat("globe", "Responsive Layout", "Adapts gracefully from ultrawide dealing screens to small laptop browsers.")
     + feat("shield", "Secure Sessions", "Encrypted sessions with idle timeout and re-authentication controls.")
     + feat("check", "Always Current", "Every client runs the latest version — updates ship server-side, silently.")
     + """</div></div></section>"""
     + """<section class="section tint"><div class="wrap split">
<div class="vis rv"><img class="main" src="assets/products/crop-trader-laptop.png" alt="Web terminal on laptop" loading="lazy"></div>
<div class="rv d1"><span class="eyebrow">Parity</span><h2>A first-class terminal — not a lite companion.</h2>
<p class="lede">The web terminal carries the full trading workflow, so browser traders never feel like second-class clients.</p>
""" + checklist(["Market Watch with live bid/ask", "Advanced charts and indicators", "Full order ticket with SL/TP", "Positions, orders and history", "Same account state as mobile and desktop"]) + """
<a class="btn btn-primary" href="contact.html">Request Demo</a></div></div></section>"""
     + band_cta("Trade from anywhere.", "Ask for web terminal access for your brokerage.", "Request Demo", "contact.html"))

# ================= MOBILE (light hero) =================
page("mobile.html", "Orbit Trader Mobile — Professional Trading on Android",
     "Orbit Trader for Android: Market Watch, advanced charts, one-tap order entry and full position management on mobile.",
     hero("assets/products/orbit-mobile-light.png", "Mobile", "The full terminal,<br>in your pocket.",
          "Market Watch, charts, orders and positions on Android — professional mobile trading without compromise.",
          ['<a class="btn btn-primary" href="contact.html">Request Demo</a>', '<a class="btn btn-ghost" href="downloads.html">Get the App</a>'],
          "Orbit Trader mobile app on two phones", "Mobile", "light")
     + """<section class="section alt"><div class="wrap">
<div class="sec-head rv"><span class="eyebrow">Mobile trading</span><h2>Built for thumbs. Serious about trading.</h2><p>A mobile terminal designed around how traders actually use their phones — glanceable, fast, and complete.</p></div>
<div class="feat-grid">"""
     + feat("globe", "Market Watch", "Multi-asset quotes with bid/ask and change, searchable and organized by symbol.")
     + feat("chart", "Touch Charts", "Candlestick charts with timeframes and indicators, tuned for touch interaction.")
     + feat("bolt", "One-Tap Ticket", "Buy/Sell ticket with volume, SL/TP and margin estimate — decisive when it counts.")
     + feat("layers", "Positions", "Live positions with P/L, plus working orders and history tabs.")
     + feat("check", "Watchlist Sync", "The same watchlists and account state as web and desktop.")
     + feat("star", "Clean Design", "A calm, readable interface that stays legible in bright sunlight and late nights.")
     + """</div></div></section>"""
     + """<section class="section tint"><div class="wrap split flip">
<div class="vis rv"><img class="main" src="assets/products/crop-phone.png" alt="Orbit Trader mobile watchlist" loading="lazy"></div>
<div class="rv d1"><span class="eyebrow">Platforms</span><h2>Android now. iOS on the roadmap.</h2>
<p class="lede">Orbit Trader mobile leads on Android, sharing full account state with web and Windows.</p>
""" + checklist(["Android app available now", "Web terminal on mobile browsers", "iOS on the public roadmap", "Identical positions everywhere"]) + """
<a class="btn btn-primary" href="downloads.html">Platform availability</a></div></div></section>"""
     + band_cta("Put Orbit Trader in your clients' pockets.", "Ask about mobile distribution for your brand.", "Request Demo", "contact.html"))
print("batch A done")

# ================= MANAGER (light hero) =================
page("manager.html", "Orbit Manager — Broker Operations Workspace",
     "Orbit Manager: client oversight, exposure monitoring, dealing workflows and reporting for modern brokerages.",
     hero("assets/products/orbit-manager-light.png", "Orbit Manager", "Run the brokerage.<br>See everything.",
          "Client oversight, exposure monitoring, dealing workflows and reporting — the operations workspace your team lives in.",
          ['<a class="btn btn-primary" href="contact.html">Request Demo</a>', '<a class="btn btn-ghost" href="brokers.html">For Brokers</a>'],
          "Orbit Manager dashboard with KPIs and client table", "Orbit Manager", "light")
     + """<section class="section alt"><div class="wrap">
<div class="sec-head rv"><span class="eyebrow">Operations</span><h2>The dealing desk, uncluttered.</h2><p>Every number the operations team needs, one glance away — clients, exposure, activity and risk.</p></div>
<div class="feat-grid">"""
     + feat("users", "Client Oversight", "Search, segment and manage client accounts with balances, status and activity at hand.")
     + feat("chart", "Exposure View", "Aggregate exposure by symbol, group and book — see concentration before it matters.")
     + feat("bolt", "Dealing Workflows", "Review, adjust and manage orders and positions with clear audit context.")
     + feat("layers", "Groups & Books", "Organize clients into groups with distinct conditions, spreads and permissions.")
     + feat("star", "Reporting", "Activity, volume and P/L reports designed for operations and finance teams.")
     + feat("shield", "Control & Audit", "Role-based access with an audit trail of who changed what, and when.")
     + """</div></div></section>"""
     + """<section class="section tint"><div class="wrap split">
<div class="vis tintbg rv"><img class="main" src="assets/products/crop-manager.png" alt="Orbit Manager operations view" loading="lazy"></div>
<div class="rv d1"><span class="eyebrow">Workflow</span><h2>From alert to action in seconds.</h2>
<p class="lede">When exposure spikes or a client needs attention, the path from noticing to acting is short and obvious.</p>
""" + checklist(["Live KPI cards for clients, volume and activity", "Drill from totals to individual accounts", "Act on orders and positions directly", "Every action recorded in the audit log"]) + """
<a class="btn btn-primary" href="contact.html">See a Live Walkthrough</a></div></div></section>"""
     + band_cta("Give your ops team superpowers.", "Request a Manager walkthrough tailored to your desk.", "Request Demo", "contact.html"))

# ================= ADMINISTRATOR (dark hero) =================
page("administrator.html", "Orbit Administrator — Platform Control",
     "Orbit Administrator: symbols, groups, permissions, servers and audit — complete control over the Orbit platform.",
     hero("assets/products/orbit-admin-dark.png", "Orbit Administrator", "Total control.<br>Zero guesswork.",
          "Symbols, groups, permissions, servers and audit — the control plane for the entire Orbit platform.",
          ['<a class="btn btn-primary" href="contact.html">Request Demo</a>', '<a class="btn btn-ghost" href="security.html">Security Model</a>'],
          "Orbit Administrator server status and permissions", "Orbit Administrator", "dark")
     + """<section class="section alt"><div class="wrap">
<div class="sec-head rv"><span class="eyebrow">Control plane</span><h2>Configure everything. Break nothing.</h2><p>Platform administration with guardrails — powerful controls, clear consequences, full history.</p></div>
<div class="feat-grid">"""
     + feat("cog", "Symbol Configuration", "Define symbols, sessions, spreads, swaps and contract specs per group.")
     + feat("users", "Groups & Permissions", "Role-based access for admins, managers and support — least privilege by default.")
     + feat("globe", "Server Management", "Monitor services, health and capacity from one status grid.")
     + feat("layers", "Backups & Recovery", "Backup policies and recovery procedures designed for continuity.")
     + feat("shield", "Audit Log", "An immutable record of administrative actions — who, what, when.")
     + feat("check", "Change Safety", "Review consequential changes before they apply, with rollback context.")
     + """</div></div></section>"""
     + """<section class="section tint"><div class="wrap split flip">
<div class="vis rv"><img class="main" src="assets/products/orbit-ecosystem-dark.png" alt="Orbit platform devices" loading="lazy"></div>
<div class="rv d1"><span class="eyebrow">Governance</span><h2>Built for regulated operations.</h2>
<p class="lede">Segregation of duties, permission scoping and audit trails map naturally to compliance workflows.</p>
""" + checklist(["Separate admin, manager and support roles", "Scoped permissions per team and function", "Complete audit trail of changes", "Designed for oversight and review"]) + """
<a class="btn btn-primary" href="security.html">Our Security Approach</a></div></div></section>"""
     + band_cta("Take control of your platform.", "See Administrator in a guided session.", "Request Demo", "contact.html"))

# ================= ALGO (dark hero) =================
page("algo.html", "Algo & Automation — Orbit Automation Roadmap",
     "The Orbit automation direction: algorithmic trading, strategy testing and broker workflow automation — current status and roadmap.",
     hero("assets/products/orbit-chart-dark.png", "Algo & Automation", "Trading,<br>automated responsibly.",
          "Our automation direction covers algorithmic trading, strategy testing and broker workflow automation. Status is stated honestly — what's live, what's in design, what's next.",
          ['<a class="btn btn-primary" href="contact.html">Request Early Access</a>', '<a class="btn btn-ghost" href="developers.html">Developer Platform</a>'],
          "Orbit Trader chart with order ticket", "Algo & Automation", "dark")
     + """<section class="section alt"><div class="wrap">
<div class="sec-head rv"><span class="eyebrow">Roadmap</span><h2>Where automation is headed.</h2><p>Each capability is labeled with its real status — no vaporware sold as shipped.</p></div>
<div class="feat-grid">"""
     + feat("code", "Trading Bots [In design]", "Automated strategies running against Orbit market data and order entry.")
     + feat("chart", "Strategy Testing [Roadmap]", "Backtesting and optimization over historical market data.")
     + feat("layers", "Custom Indicators [Roadmap]", "Custom indicators and drawing automation for the terminal.")
     + feat("bolt", "Broker Workflows [In design]", "Event rules for onboarding, alerts and operational automation.")
     + feat("globe", "API Automation [Available]", "REST, WebSocket and webhooks ready for programmatic workflows today.")
     + feat("shield", "Safe by Design [Principle]", "Permissions, limits and audit planned into every automation surface.")
     + """</div></div></section>"""
     + """<section class="section tint"><div class="wrap split">
<div class="rv"><span class="eyebrow">Today</span><h2>Automate with APIs now.</h2>
<p class="lede">While terminal automation is on the roadmap, the integration layer is ready for programmatic workflows today.</p>
""" + checklist(["REST API for accounts, orders and data", "WebSocket for streaming market data", "Webhooks for event-driven flows", "FIX connectivity on the roadmap"]) + """
<a class="btn btn-primary" href="developers.html">Explore the APIs</a></div>
<div class="vis rv d1"><img class="main" src="assets/products/orbit-ecosystem-hero.png" alt="Orbit ecosystem" loading="lazy"></div>
</div></section>"""
     + band_cta("Shape the automation roadmap.", "Request early access and tell us what you'd automate first.", "Request Early Access", "contact.html"))

# ================= BROKERS (split hero + steps) =================
page("brokers.html", "For Brokers — Launch Your Brokerage on Orbit",
     "Launch and run your brokerage on the Orbit stack: white label, dealing operations, platform control and a path from demo to go-live.",
     hero("assets/products/crop-manager.png", "For Brokers", "Launch a brokerage<br>on modern rails.",
          "White label, dealing operations and platform control — everything a new or migrating brokerage needs to go live on Orbit.",
          ['<a class="btn btn-primary" href="contact.html">Talk to Sales</a>', '<a class="btn btn-ghost" href="white-label.html">White Label</a>'],
          "Orbit Manager broker operations", "For Brokers", "split")
     + stats_band([("3", "Core products"), ("3", "Client platforms"), ("1", "Integrated stack"), ("1", "Technology partner")])
     + """<section class="section alt"><div class="wrap">
<div class="sec-head rv"><span class="eyebrow">Why Orbit</span><h2>Built for brokerages that want to move fast.</h2></div>
<div class="feat-grid">"""
     + feat("star", "Your Brand", "Full white label — your name, logo, colors and domain across every surface.")
     + feat("bolt", "Fast Go-Live", "A structured path from first demo to live clients, without legacy migration pain.")
     + feat("users", "Ops Included", "Manager and Administrator workspaces are part of the stack — not add-ons.")
     + feat("cog", "Your Model", "Groups, symbols, spreads and conditions configured around your business model.")
     + feat("globe", "Multi-Asset", "FX, metals, crypto, indices and stocks from day one.")
     + feat("shield", "Governance", "Roles, permissions and audit designed for serious operations.")
     + """</div></div></section>"""
     + """<section class="section tint"><div class="wrap">
<div class="sec-head rv"><span class="eyebrow">Go-live path</span><h2>From demo to live in four steps.</h2></div>"""
     + steps([
         ("Discovery", "We map your business model, instruments, client base and operational needs."),
         ("Configuration", "Symbols, groups, spreads, permissions and branding are set up on your environment."),
         ("Branding", "White label applied — your identity across terminal, mobile, web and emails."),
         ("Go-live", "Pilot with a controlled group, then open the doors. We stay with you after launch."),
     ]) + """
<div style="margin-top:36px"><a class="btn btn-primary" href="contact.html">Start with Discovery</a></div>
</div></section>"""
     + band_cta("Let's talk about your brokerage.", "Tell us your model — we'll map the Orbit stack to it.", "Talk to Sales", "contact.html"))
print("batch B done")

# ================= WHITE LABEL (center hero) =================
page("white-label.html", "White Label — Your Brand on Orbit Technology",
     "Launch your branded trading offering on the Orbit stack: your name, logo, colors and domain across terminal, mobile and web.",
     hero("assets/products/orbit-whitelabel.png", "White Label", "Your brand.<br>Our technology.",
          "Launch a branded trading experience on the Orbit stack — your identity on every surface your clients touch.",
          ['<a class="btn btn-primary" href="contact.html">Start White Label</a>', '<a class="btn btn-ghost" href="brokers.html">For Brokers</a>'],
          "White label trading platform branded Meridian", "White Label", "center")
     + """<section class="section alt"><div class="wrap">
<div class="sec-head rv"><span class="eyebrow">Branding</span><h2>Every pixel can carry your identity.</h2><p>White label on Orbit goes deeper than a logo swap — it's your brand as the product.</p></div>
<div class="feat-grid">"""
     + feat("star", "Brand Identity", "Your name, logo, colors and typography across terminal, mobile and web.")
     + feat("globe", "Your Domain", "Web terminal and client surfaces served from your own domain.")
     + feat("phone", "Branded Apps", "Mobile apps published under your brand identity.")
     + feat("layers", "Themed UI", "Light and dark themes tuned to your brand palette.")
     + feat("check", "Client Communications", "System emails and notifications in your voice, from your domain.")
     + feat("shield", "Brand Control", "You own the client relationship — technology stays invisible.")
     + """</div></div></section>"""
     + """<section class="section tint"><div class="wrap">
<div class="sec-head rv"><span class="eyebrow">Process</span><h2>Branded and live in three moves.</h2></div>"""
     + steps([
         ("Brand kit", "Share your logo, colors, typography and tone — we map them onto the Orbit surfaces."),
         ("Configuration", "Domains, app identities, emails and themes are set up and reviewed with you."),
         ("Launch", "A branded pilot first, then full launch. Your brand, our technology, one go-live."),
     ]) + """
</div></section>"""
     + band_cta("Launch your branded trading experience.", "Start the white-label conversation today.", "Start White Label", "contact.html"))

# ================= CONNECTIVITY =================
page("connectivity.html", "Connectivity — Market Data & Execution Infrastructure",
     "Orbit connectivity: aggregated market data, execution routing, bridge-ready architecture and hosting designed for trading workloads.",
     hero("assets/products/orbit-trader-devices.png", "Connectivity", "Plugged into<br>the markets.",
          "Aggregated market data, execution routing and hosting designed for trading workloads — the pipes behind the Orbit stack.",
          ['<a class="btn btn-primary" href="contact.html">Discuss Connectivity</a>', '<a class="btn btn-ghost" href="developers.html">APIs</a>'],
          "Orbit Trader across laptop and phone", "Connectivity", "split")
     + """<section class="section alt"><div class="wrap">
<div class="sec-head rv"><span class="eyebrow">Infrastructure</span><h2>Data in. Orders out. Reliably.</h2><p>The connectivity layer is designed around what brokerages actually need: clean data and dependable execution paths.</p></div>
<div class="feat-grid">"""
     + feat("globe", "Market Data", "Multi-asset price feeds aggregated and normalized into one stream for the whole stack.")
     + feat("bolt", "Execution Routing", "Order routing architecture designed for straight-through processing to liquidity.")
     + feat("layers", "Bridge-Ready", "Integration points for bridge and liquidity workflows as your setup grows.")
     + feat("cog", "Feed Management", "Symbol mapping, session calendars and feed health monitoring in one place.")
     + feat("shield", "Resilient Design", "Redundancy and failover designed into data and execution paths.")
     + feat("chart", "FIX on Roadmap", "FIX connectivity for institutional flows is on the public roadmap.")
     + """</div>
<div class="rv" style="margin-top:26px;background:#FFF7E8;border:1px solid #F0DDA6;border-radius:16px;padding:18px 22px;color:#7A5B12;font-size:14px;max-width:60rem">Specific feed providers, liquidity venues and bridge integrations are scoped per implementation during discovery — we don't list partners we haven't signed.</div>
</div></section>"""
     + """<section class="section tint"><div class="wrap split flip">
<div class="vis rv"><img class="main" src="assets/products/orbit-chart-dark.png" alt="Market data chart" loading="lazy"></div>
<div class="rv d1"><span class="eyebrow">Hosting</span><h2>Run where it performs.</h2>
<p class="lede">Deployment options matched to your latency needs, compliance requirements and growth plans.</p>
""" + checklist(["Cloud or dedicated infrastructure options", "Regions chosen for execution latency", "Monitoring and alerting built in", "Scaling path from pilot to full book"]) + """
<a class="btn btn-primary" href="contact.html">Plan Your Deployment</a></div></div></section>"""
     + band_cta("Let's design your connectivity.", "Tell us your markets — we'll map the data and execution paths.", "Discuss Connectivity", "contact.html"))

# ================= DEVELOPERS =================
page("developers.html", "Developer Platform — APIs for the Orbit Stack",
     "Build on Orbit: REST and WebSocket APIs, webhooks and integration guides for brokerages, fintechs and institutional teams.",
     hero("assets/products/crop-trader-laptop.png", "Developers", "Build on<br>the Orbit stack.",
          "REST and WebSocket APIs, webhooks and integration guides — for brokerages, fintechs and institutional teams building on Orbit.",
          ['<a class="btn btn-primary" href="contact.html">Get API Access</a>', '<a class="btn btn-ghost" href="algo.html">Automation Roadmap</a>'],
          "Developer laptop with trading terminal", "Developers", "flip")
     + """<section class="section alt"><div class="wrap">
<div class="sec-head rv"><span class="eyebrow">Integration surface</span><h2>APIs that respect your time.</h2><p>Consistent, documented and versioned — the same care we put into the terminal goes into the API.</p></div>
<div class="feat-grid">"""
     + feat("code", "REST API", "Accounts, orders, positions, symbols and reporting — the back office as an API.")
     + feat("bolt", "WebSocket Streams", "Real-time quotes, account updates and order events pushed to your systems.")
     + feat("globe", "Webhooks", "Event-driven callbacks for onboarding, trading and operational events.")
     + feat("layers", "FIX [Roadmap]", "FIX connectivity for institutional order flow is on the public roadmap.")
     + feat("shield", "Auth & Scopes", "Token auth with scoped permissions — least privilege for integrations too.")
     + feat("check", "Versioned & Documented", "Stable versioning, changelogs and guides that stay current.")
     + """</div></div></section>"""
     + """<section class="section tint"><div class="wrap split">
<div class="rv"><span class="eyebrow">Taste</span><h2>Up and running in minutes.</h2>
<p class="lede">A sense of the integration style — clean resources, predictable shapes.</p>
<div class="code-card"><span class="c"># Stream live quotes over WebSocket</span><br><span class="k">const</span> ws = <span class="k">new</span> WebSocket(<span class="s">"wss://api.orbit.example/v1/stream"</span>);<br>ws.onopen = () => ws.send(JSON.stringify({<br>&nbsp;&nbsp;<span class="s">"action"</span>: <span class="s">"subscribe"</span>,<br>&nbsp;&nbsp;<span class="s">"symbols"</span>: [<span class="s">"XAUUSD"</span>, <span class="s">"EURUSD"</span>]<br>}));<br>ws.onmessage = (e) => {<br>&nbsp;&nbsp;<span class="k">const</span> tick = JSON.parse(e.data);<br>&nbsp;&nbsp;renderQuote(tick); <span class="c">// { symbol, bid, ask, ts }</span><br>};</div>
</div>
<div class="rv d1"><span class="eyebrow">Guides</span><h2>Docs that answer.</h2>
<p class="lede">Integration guides walk through the common builds step by step.</p>
""" + checklist(["Authentication and token scopes", "Subscribing to market data", "Placing and managing orders", "Receiving webhooks reliably", "Going live checklist"]) + """
<a class="btn btn-primary" href="contact.html">Get API Access</a></div>
</div></section>"""
     + band_cta("Start building on Orbit.", "Get API credentials and integration support.", "Get API Access", "contact.html"))

# ================= DOWNLOADS (center hero + platform cards) =================
page("downloads.html", "Downloads — Orbit Trader for Web, Android & Windows",
     "Get Orbit Trader: zero-install web terminal, Android app and Windows desktop — availability and system requirements.",
     hero("assets/products/orbit-ecosystem-hero.png", "Downloads", "Get Orbit Trader.<br>On every screen.",
          "Web, Android and Windows — choose your platform. Client apps are distributed through your brokerage.",
          [], "Orbit Trader on all devices", "Downloads", "center")
     + """<section class="section alt"><div class="wrap">
<div class="sec-head rv"><span class="eyebrow">Platforms</span><h2>Pick your platform.</h2><p>Production apps are branded and distributed per brokerage — request access and we'll route you correctly.</p></div>
<div class="plat-grid">
<div class="plat-card rv"><div class="picon">""" + ICONS["globe"] + """</div><h3>Web Terminal</h3><p>Zero-install — trade from any modern browser, no download needed.</p><a class="btn btn-ghost" href="web-terminal.html">About Web</a></div>
<div class="plat-card rv d1"><div class="picon">""" + ICONS["phone"] + """</div><h3>Android</h3><p>Native app with the full terminal — Market Watch, charts, ticket.</p><a class="btn btn-ghost" href="mobile.html">About Mobile</a></div>
<div class="plat-card rv d2"><div class="picon">""" + ICONS["layers"] + """</div><h3>Windows</h3><p>Native desktop terminal for dealing screens and power users.</p><a class="btn btn-ghost" href="contact.html">Request Access</a></div>
</div></div></section>"""
     + """<section class="section tint"><div class="wrap split">
<div class="rv"><span class="eyebrow">Requirements</span><h2>Light on your machine.</h2>
<p class="lede">Orbit Trader is engineered to run well on everyday hardware — no workstation required.</p>
""" + checklist(["Web: any modern browser (Chrome, Edge, Firefox, Safari)", "Android: Android 9.0 and above", "Windows: Windows 10/11, 64-bit", "A stable internet connection for live data"]) + """
</div><div class="vis rv d1"><img class="main" src="assets/products/orbit-mobile-light.png" alt="Orbit Trader mobile" loading="lazy"></div>
</div></section>"""
     + band_cta("Need client distribution?", "Brokerages: ask about branded app distribution for your clients.", "Contact Us", "contact.html"))
print("batch C done")

# ================= INSTITUTIONS (flip hero) =================
page("institutions.html", "For Institutions — Funds, Prop Firms & Enterprises",
     "Orbit technology for hedge funds, prop firms and financial institutions: multi-asset trading, APIs and broker-grade operations.",
     hero("assets/products/orbit-trader-suite.png", "For Institutions", "Institutional workflows,<br>modern stack.",
          "For hedge funds, prop firms and financial institutions that need professional trading technology without legacy drag.",
          ['<a class="btn btn-primary" href="contact.html">Talk to Sales</a>', '<a class="btn btn-ghost" href="developers.html">APIs</a>'],
          "Orbit Trader suite across devices", "For Institutions", "flip")
     + """<section class="section alt"><div class="wrap">
<div class="sec-head rv"><span class="eyebrow">Who it's for</span><h2>Professional scale, three ways.</h2></div>
<div class="feat-grid">"""
     + feat("chart", "Hedge Funds", "Multi-asset execution with programmatic access and operational oversight.")
     + feat("users", "Prop Firms", "Evaluation and funded workflows with clear account operations and reporting.")
     + feat("layers", "Enterprises", "Branded deployments and integrations for financial institutions.")
     + feat("code", "API-First Teams", "REST, WebSocket and webhooks available today; FIX on the roadmap.")
     + feat("cog", "Operations Desks", "Manager workspaces for client, exposure and activity oversight.")
     + feat("shield", "Governance Needs", "Role-based access and audit trails designed for oversight.")
     + """</div></div></section>"""
     + """<section class="section tint"><div class="wrap split">
<div class="vis tintbg rv"><img class="main" src="assets/products/crop-manager.png" alt="Operations workspace" loading="lazy"></div>
<div class="rv d1"><span class="eyebrow">Prop firms</span><h2>Challenges, run cleanly.</h2>
<p class="lede">Prop firms can run evaluation and funded workflows on the Orbit stack with transparent account operations.</p>
""" + checklist(["Account operations and grouping", "Performance and activity reporting", "Risk and exposure visibility", "API-driven workflows"]) + """
<a class="btn btn-primary" href="contact.html">Discuss Your Model</a></div></div></section>"""
     + band_cta("Tell us about your institution.", "We'll map the Orbit stack to your workflows.", "Talk to Sales", "contact.html"))

# ================= COMPANY (min hero) =================
page("company.html", "About QuotesWare Technologies",
     "QuotesWare Technologies builds modern trading infrastructure — the Orbit product family for traders, brokers and institutions.",
     hero("", "Company", "Trading technology,<br>built properly.",
          "QuotesWare Technologies is a trading technology company. We build the Orbit product family — modern infrastructure for traders, brokerages and institutions — with a bias for clarity, reliability and honest communication.",
          [], "", "Company", "min")
     + """<section class="section alt"><div class="wrap">
<div class="sec-head rv"><span class="eyebrow">How we work</span><h2>Principles, not slogans.</h2></div>
<div class="feat-grid">"""
     + feat("check", "Honest Status", "We label what's shipped, what's in design and what's roadmap — on this site and in sales calls.")
     + feat("star", "Design Matters", "Trading tools are used for hours daily. They should feel considered, not tolerated.")
     + feat("shield", "Reliability First", "A missed quote costs real money. We engineer for the moments that matter.")
     + feat("users", "Broker Success", "Our customers run businesses on Orbit. Their go-live is our deadline.")
     + feat("code", "Integration Friendly", "Open APIs and clean integration surfaces — your stack, your choice.")
     + feat("globe", "Multi-Asset World", "FX, metals, crypto, indices, stocks — modern traders don't live in one market.")
     + """</div></div></section>"""
     + """<section class="section tint"><div class="wrap split">
<div class="vis rv"><img class="main" src="assets/products/orbit-ecosystem-dark.png" alt="Orbit ecosystem" loading="lazy"></div>
<div class="rv d1"><span class="eyebrow">The products</span><h2>One family: Orbit.</h2>
<p class="lede">Everything we build serves the same mission — better trading technology for everyone in the trade.</p>
""" + checklist(["Orbit Trader — the trader terminal", "Orbit Manager — broker operations", "Orbit Administrator — platform control", "White label, connectivity and APIs"]) + """
<a class="btn btn-primary" href="platform.html">Explore the Platform</a></div></div></section>"""
     + band_cta("Work with QuotesWare.", "Start a conversation about your trading technology needs.", "Contact Us", "contact.html"))

# ================= NEWS (min hero + cards) =================
page("news.html", "News — QuotesWare Updates & Releases",
     "Product releases, company updates and announcements from QuotesWare Technologies.",
     hero("", "Newsroom", "Updates from<br>QuotesWare.",
          "Product releases and company announcements — published when there's something real to say.",
          [], "", "News", "min")
     + """<section class="section alt"><div class="wrap">
<div class="sec-head rv"><span class="eyebrow">Latest</span><h2>Release notes & announcements.</h2></div>
<div class="fam-grid">
<article class="fam-card rv"><div class="fam-shot"><img src="assets/products/orbit-trader-light.png" alt="QuotesWare website" loading="lazy" style="object-position:center"></div>
<div class="fam-body"><span class="tag">4 Oct 2026</span><h3>New QuotesWare corporate website</h3><p>A rebuilt, image-led corporate site covering the Orbit product family — Trader, Manager, Administrator, white label and developer platform.</p></div></article>
<article class="fam-card rv d1"><div class="fam-shot"><img src="assets/products/orbit-mobile-light.png" alt="Orbit Trader 5.8" loading="lazy" style="object-position:center"></div>
<div class="fam-body"><span class="tag">4 Oct 2026</span><h3>Orbit Trader 5.8 ships</h3><p>New Android, Windows desktop and web releases of the Orbit Trader terminal.</p></div></article>
<article class="fam-card rv d2"><div class="fam-shot"><img src="assets/products/orbit-manager-light.png" alt="Orbit Manager" loading="lazy" style="object-position:center"></div>
<div class="fam-body"><span class="tag">Roadmap</span><h3>Manager & Administrator previews</h3><p>Broker operations and platform administration workspaces in preview — request a walkthrough to see the current state.</p><a class="more" href="contact.html">Request a walkthrough</a></div></article>
</div></div></section>"""
     + band_cta("Stay in the loop.", "Contact us for release updates relevant to your implementation.", "Contact Us", "contact.html"))

# ================= CAREERS (min hero) =================
page("careers.html", "Careers — Work at QuotesWare",
     "Open roles and working principles at QuotesWare Technologies.",
     hero("", "Careers", "Build trading<br>technology with us.",
          "We're a focused team building modern trading infrastructure. Current openings are listed below — honestly.",
          [], "", "Careers", "min")
     + """<section class="section alt"><div class="wrap">
<div class="sec-head rv"><span class="eyebrow">Open roles</span><h2>No current openings.</h2><p>We're not hiring right now. When roles open, they'll be listed here with real descriptions — never placeholders.</p></div>
<div class="feat-grid">"""
     + feat("code", "Engineering", "Trading terminals, broker operations, feeds and infrastructure.")
     + feat("chart", "Product & Design", "Interfaces traders and broker teams rely on every day.")
     + feat("users", "Growth & Partnerships", "Working with brokerages adopting the Orbit stack.")
     + """</div>
<div class="band-cta rv" style="margin-top:44px"><div><h2>Interested in the future?</h2><p>Send your background and what you'd like to build — we'll keep it on file.</p></div><a class="btn btn-primary" href="contact.html">Get in Touch</a></div>
</div></section>"""
     + band_cta("Follow our progress.", "News and releases are published as they happen.", "See News", "news.html"))

# ================= MEDIA (min hero + gallery) =================
page("media.html", "Media Kit — QuotesWare Brand Assets",
     "Official QuotesWare Technologies logos, brand colors, product screenshots and company boilerplate for press and partners.",
     hero("", "For press & partners", "QuotesWare,<br>presented properly.",
          "Official logos, brand colors, product visuals and boilerplate — with simple usage guidelines.",
          [], "", "Media Kit", "min")
     + """<section class="section alt"><div class="wrap">
<div class="sec-head rv"><span class="eyebrow">Brand assets</span><h2>Logos & colors.</h2></div>
<div class="feat-grid">"""
     + feat("star", "Primary Logo", "Full-color QuotesWare mark for light backgrounds. File: assets/logo.png")
     + feat("check", "Reversed Logo", "White version for dark backgrounds. File: assets/logo-light.png")
     + feat("layers", "Brand Colors", "Deep Navy #071B36 · Teal #12D0BB · Blue #0A4A8A · Background #F7FAFC")
     + """</div></div></section>"""
     + """<section class="section tint"><div class="wrap">
<div class="sec-head rv"><span class="eyebrow">Product visuals</span><h2>Approved screenshots.</h2><p>Current product renders approved for editorial and partner use.</p></div>
<div class="fam-grid">
<article class="fam-card rv"><div class="fam-shot"><img src="assets/products/orbit-trader-light.png" alt="Orbit Trader light" loading="lazy" style="object-position:center"></div><div class="fam-body"><h3>Orbit Trader — light</h3><p>Desktop terminal, light theme.</p></div></article>
<article class="fam-card rv d1"><div class="fam-shot"><img src="assets/products/orbit-manager-light.png" alt="Orbit Manager light" loading="lazy" style="object-position:center"></div><div class="fam-body"><h3>Orbit Manager — light</h3><p>Broker operations dashboard.</p></div></article>
<article class="fam-card rv d2"><div class="fam-shot"><img src="assets/products/orbit-ecosystem-dark.png" alt="Orbit ecosystem dark" loading="lazy" style="object-position:center"></div><div class="fam-body"><h3>Ecosystem — dark</h3><p>Laptop, tablet and phone together.</p></div></article>
</div></div></section>"""
     + """<section class="section alt"><div class="wrap split">
<div class="rv"><span class="eyebrow">Boilerplate</span><h2>Company description.</h2>
<p class="lede">"QuotesWare Technologies builds modern trading infrastructure — Orbit Trader for traders, Orbit Manager and Orbit Administrator for brokerages, plus white label, connectivity and APIs."</p>
""" + checklist(["Don't stretch, recolor or rearrange the logo", "Don't place the logo on clashing backgrounds", "Don't imply endorsement or partnership without agreement"]) + """
</div><div class="rv d1"><div class="form-card"><h3 style="margin-bottom:12px">Press contact</h3><p style="color:var(--muted);margin-bottom:20px">For interviews, assets and partnership inquiries.</p><a class="btn btn-primary" href="contact.html">Contact Us</a></div></div>
</div></section>"""
     + band_cta("Need something specific?", "Ask for the asset or information you need.", "Contact Us", "contact.html"))

# ================= RESOURCES (min hero + guides + faq + roadmap) =================
page("resources.html", "Resources — Guides, FAQ & Roadmap",
     "Guides, frequently asked questions and the public roadmap for the Orbit platform by QuotesWare Technologies.",
     hero("", "Resources", "Learn the<br>Orbit platform.",
          "Guides, answers and the public roadmap — everything you need to evaluate and adopt Orbit.",
          [], "", "Resources", "min")
     + """<section class="section alt" id="guides"><div class="wrap">
<div class="sec-head rv"><span class="eyebrow">Guides</span><h2>Start here.</h2></div>
<div class="feat-grid">"""
     + feat("globe", "Platform Overview", "What Orbit is, who it's for, and how the products fit together.")
     + feat("users", "For Brokerages", "How brokers launch, operate and grow on the Orbit stack.")
     + feat("code", "API Quickstart", "Authentication, market data and orders — the integration essentials.")
     + feat("shield", "Security Model", "How we think about protecting accounts, data and operations.")
     + feat("star", "White Label Guide", "What gets branded, how the process runs, and what to prepare.")
     + feat("chart", "Migration Notes", "Moving from legacy platforms: what to plan for.")
     + """</div>
<div class="rv" style="margin-top:26px;background:#EFF6FF;border:1px solid #C9E2FF;border-radius:16px;padding:18px 22px;color:#0A4A8A;font-size:14px;max-width:60rem">Full guide content is published progressively. For anything urgent, <a href="contact.html" style="font-weight:700;color:#0A4A8A">ask us directly</a> — a human answers.</div>
</div></section>"""
     + """<section class="section tint" id="faq"><div class="wrap">
<div class="sec-head rv"><span class="eyebrow">FAQ</span><h2>Common questions.</h2></div>
<div class="faq">"""
     + "".join(f"""<div class="faq-item rv"><button class="faq-q">{q}<span class="faq-x">+</span></button><div class="faq-a"><p>{a}</p></div></div>""" for q, a in [
         ("Is QuotesWare a broker?", "No. QuotesWare Technologies provides trading software technology only. We don't offer brokerage services, accept client funds, or give investment advice."),
         ("Which platforms does Orbit Trader run on?", "Web (any modern browser), Android, and Windows. iOS is on the public roadmap."),
         ("Can we white-label the platform?", "Yes — your brand across terminal, mobile, web, domain and communications. See the White Label page."),
         ("Do you offer a demo?", "Yes. Request a demo and we'll arrange a guided walkthrough of the products relevant to you."),
         ("Is there an API?", "Yes — REST and WebSocket APIs plus webhooks are available today. FIX is on the roadmap."),
         ("How does pricing work?", "Pricing is scoped per implementation — products, branding, and deployment. Talk to sales for a proposal."),
     ]) + """</div></div></section>"""
     + """<section class="section alt" id="roadmap"><div class="wrap">
<div class="sec-head rv"><span class="eyebrow">Roadmap</span><h2>Where Orbit is headed.</h2><p>Status labels are honest — shipped, in design, or planned.</p></div>"""
     + steps([
         ("Orbit Trader — Web, Android, Windows [Available]", "The trader terminal across three platforms, in active development with regular releases."),
         ("APIs — REST, WebSocket, Webhooks [Available]", "Programmatic access for integrations and automation, available today."),
         ("Orbit Manager & Administrator [In preview]", "Broker operations and platform administration workspaces — request a walkthrough."),
         ("Algo & Automation [In design]", "Trading bots, strategy testing and workflow automation — early access on request."),
         ("iOS App [Planned]", "Native iOS terminal on the public roadmap."),
         ("FIX Connectivity [Planned]", "Institutional FIX connectivity on the public roadmap."),
     ]) + """
</div></section>"""
     + band_cta("Can't find your answer?", "Ask us — a human replies.", "Contact Us", "contact.html"))

# ================= CONTACT (kept form page) =================
page("contact.html", "Contact — Request a Demo",
     "Contact QuotesWare Technologies: request a product demo, discuss white label, or ask about the Orbit platform.",
     hero("", "Contact", "Let's talk<br>trading technology.",
          "Request a demo, discuss white label, or ask anything about the Orbit platform.",
          [], "", "Contact", "min")
     + """<section class="section alt"><div class="wrap split">
<div class="rv"><span class="eyebrow">What happens next</span><h2>A real conversation.</h2>
<p class="lede">Tell us about your goals and we'll arrange the right walkthrough — no generic sales deck.</p>
""" + checklist(["A product specialist replies personally", "Demo tailored to your use case", "Technical questions welcomed", "No obligation, no pressure"]) + """
</div>
<div class="rv d1"><form class="form-card" id="demoForm" novalidate>
<h3 style="margin-bottom:6px">Request a demo</h3>
<p style="color:var(--muted);font-size:14px;margin-bottom:22px">Fields marked * are required.</p>
<div class="frow"><div class="field"><label for="f-name">Full name *</label><input id="f-name" name="name" required autocomplete="name"></div>
<div class="field"><label for="f-email">Work email *</label><input id="f-email" name="email" type="email" required autocomplete="email"></div></div>
<div class="frow"><div class="field"><label for="f-company">Company</label><input id="f-company" name="company" autocomplete="organization"></div>
<div class="field"><label for="f-role">Your role</label><select id="f-role" name="role"><option>Founder / Executive</option><option>Operations / Dealing</option><option>Technology</option><option>Other</option></select></div></div>
<div class="field"><label for="f-type">I am interested in</label><select id="f-type" name="interest"><option>Orbit Trader</option><option>Orbit Manager</option><option>Orbit Administrator</option><option>White Label</option><option>APIs / Integration</option><option>Other</option></select></div>
<div class="field"><label for="f-msg">Message *</label><textarea id="f-msg" name="message" required placeholder="Tell us about your goals, timelines and what you'd like to see."></textarea></div>
<button class="btn btn-primary" type="submit" style="width:100%;justify-content:center">Request Demo</button>
<p class="form-note">This form is front-end only right now — nothing is sent anywhere yet. We'll connect it to our inbox next.</p>
</form></div></div></section>"""
     + band_cta("Prefer to explore first?", "Browse the platform overview at your own pace.", "Explore Platform", "platform.html"))

# ================= LEGAL (min heroes) =================
page("privacy.html", "Privacy Policy",
     "How QuotesWare Technologies handles information submitted through this website.",
     hero("", "Legal", "Your privacy,<br>stated plainly.",
          "What this website collects, why, and your choices. Last updated: October 2026.",
          [], "", "Privacy", "min")
     + """<section class="section alt"><div class="wrap" style="max-width:46rem"><div class="rv">
<h2 style="font-size:24px;margin-bottom:12px">What we collect</h2>
<p style="color:var(--muted);margin-bottom:28px">If you submit the demo request form, we receive the details you provide: name, work email, company, role, company type and message. We use this only to respond to your inquiry about our products.</p>
<h2 style="font-size:24px;margin-bottom:12px">What we don't do</h2>
<p style="color:var(--muted);margin-bottom:28px">We don't sell personal information. We don't run advertising trackers on this site. We don't collect information you don't explicitly provide.</p>
<h2 style="font-size:24px;margin-bottom:12px">Cookies</h2>
<p style="color:var(--muted);margin-bottom:28px">This site uses only essential technical storage (such as remembering a form draft on your own device). See our <a href="cookies.html" style="color:var(--blue);font-weight:700">cookie notice</a>.</p>
<h2 style="font-size:24px;margin-bottom:12px">Your choices</h2>
<p style="color:var(--muted);margin-bottom:28px">To ask what we hold about you, or to ask for it to be removed, contact us via the <a href="contact.html" style="color:var(--blue);font-weight:700">contact page</a>.</p>
<p style="color:var(--muted);font-size:14px">This page is general information, not legal advice. Specific data-processing terms are agreed per implementation.</p>
</div></div></section>"""
     + band_cta("Questions about privacy?", "Ask us directly.", "Contact Us", "contact.html"))

page("terms.html", "Terms of Use",
     "Terms for using the QuotesWare Technologies website.",
     hero("", "Legal", "The fine print,<br>in plain language.",
          "The rules for using this website. Last updated: October 2026.",
          [], "", "Terms", "min")
     + """<section class="section alt"><div class="wrap" style="max-width:46rem"><div class="rv">
<h2 style="font-size:24px;margin-bottom:12px">What this site is</h2>
<p style="color:var(--muted);margin-bottom:28px">This website describes the software products of QuotesWare Technologies. Product descriptions, roadmaps and availability statements reflect the current state of development and may change.</p>
<h2 style="font-size:24px;margin-bottom:12px">Not financial advice</h2>
<p style="color:var(--muted);margin-bottom:28px">Nothing on this site is investment advice or an offer of financial services. QuotesWare Technologies provides trading software technology only — it does not provide investment, brokerage or financial services and does not accept client funds.</p>
<h2 style="font-size:24px;margin-bottom:12px">Intellectual property</h2>
<p style="color:var(--muted);margin-bottom:28px">The QuotesWare name, logo, Orbit product names and site content belong to QuotesWare Technologies or its licensors. Don't copy or reuse them without permission — see the <a href="media.html" style="color:var(--blue);font-weight:700">media kit</a> for approved uses.</p>
<h2 style="font-size:24px;margin-bottom:12px">Acceptable use</h2>
<p style="color:var(--muted);margin-bottom:28px">Don't misuse the contact forms, attempt to disrupt the site, or misrepresent your identity when contacting us.</p>
<p style="color:var(--muted);font-size:14px">This page is general information, not legal advice.</p>
</div></div></section>"""
     + band_cta("Questions about these terms?", "Ask us directly.", "Contact Us", "contact.html"))

page("cookies.html", "Cookie Notice",
     "How QuotesWare Technologies uses cookies and local storage on this website.",
     hero("", "Legal", "Cookies,<br>kept minimal.",
          "What this site stores on your device and why. Last updated: October 2026.",
          [], "", "Cookies", "min")
     + """<section class="section alt"><div class="wrap" style="max-width:46rem"><div class="rv">
<h2 style="font-size:24px;margin-bottom:12px">Essential storage</h2>
<p style="color:var(--muted);margin-bottom:28px">This website may store a draft of your demo request form on your own device (local storage) so you don't lose what you typed. This never leaves your browser unless you submit the form.</p>
<h2 style="font-size:24px;margin-bottom:12px">No tracking cookies</h2>
<p style="color:var(--muted);margin-bottom:28px">We don't use advertising trackers, cross-site tracking cookies or third-party analytics beacons on this site. If that changes, this notice will be updated first.</p>
<h2 style="font-size:24px;margin-bottom:12px">Your control</h2>
<p style="color:var(--muted);margin-bottom:28px">You can clear site storage at any time in your browser settings — the site keeps working without it.</p>
<p style="color:var(--muted);font-size:14px">This page is general information, not legal advice.</p>
</div></div></section>"""
     + band_cta("Questions?", "Ask us directly.", "Contact Us", "contact.html"))
print("batch D done")

# ---------------- writer ----------------
import os, re
BASE = os.path.dirname(os.path.abspath(__file__))
for slug, title, desc, body in PAGES:
    m = re.search(r'src="(assets/[^"]+)"', body)
    og = m.group(1) if m else "assets/products/orbit-ecosystem-hero.png"
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title} | QuotesWare Technologies</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="https://dawoodshah2232-svg.github.io/quotesware-technologies/{slug}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title} | QuotesWare Technologies">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="https://dawoodshah2232-svg.github.io/quotesware-technologies/{og}">
<link rel="icon" href="assets/favicon-32.png">
<link rel="stylesheet" href="styles.css">
</head>
<body>
{HEADER}
<main>
{body}
</main>
{FOOTER}
<script src="v5.js"></script>
</body>
</html>"""
    open(os.path.join(BASE, slug), "w").write(html)
    print("wrote", slug, len(html), "bytes")
