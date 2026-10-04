#!/usr/bin/env python3
"""Build QuotesWare inner pages from shared header/footer + page content."""
import os

BASE = os.path.dirname(os.path.abspath(__file__))

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

ICONS = {
    "chart": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 3v18h18"/><path d="M7 15l4-6 4 3 4-7"/></svg>',
    "bolt": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2L4.5 13.5H11L10 22l8.5-11.5H12L13 2z"/></svg>',
    "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2l8 3.5v5.2c0 5-3.4 9.3-8 10.8-4.6-1.5-8-5.8-8-10.8V5.5L12 2z"/><path d="M9 12l2 2 4-4"/></svg>',
    "users": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 00-4-4H7a4 4 0 00-4 4v2"/><circle cx="10" cy="7" r="4"/><path d="M21 11h-6"/></svg>',
    "cog": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M4.9 4.9l2.1 2.1M17 17l2.1 2.1M19.1 4.9L17 7M7 17l-2.1 2.1"/></svg>',
    "globe": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.6 3.8 5.7 3.8 9s-1.3 6.4-3.8 9c-2.5-2.6-3.8-5.7-3.8-9S9.5 5.6 12 3z"/></svg>',
    "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="7" y="2.5" width="10" height="19" rx="2.5"/><path d="M11 18.5h2"/></svg>',
    "desk": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4.5" width="18" height="12" rx="2"/><path d="M9 20.5h6M12 16.5v4"/></svg>',
    "doc": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8l-6-6z"/><path d="M14 2v6h6M9 13h6M9 17h6"/></svg>',
    "code": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M16 18l6-6-6-6M8 6l-6 6 6 6"/></svg>',
    "check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6L9 17l-5-5"/></svg>',
    "star": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2l2.9 6.26L21.5 9.3l-4.75 4.87L17.8 21 12 17.77 6.2 21l1.05-6.83L2.5 9.3l6.6-1.04L12 2z"/></svg>',
    "layers": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2l9 5-9 5-9-5 9-5z"/><path d="M3 12l9 5 9-5M3 17l9 5 9-5"/></svg>',
}

def feat(icon, title, text):
    return f'<div class="feat rv">{ICONS[icon]}<h3>{title}</h3><p>{text}</p></div>'

def page(slug, title, desc, og_img, body):
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
<meta property="og:image" content="https://dawoodshah2232-svg.github.io/quotesware-technologies/{og_img}">
<link rel="icon" href="assets/favicon-32.png">
<link rel="stylesheet" href="styles.css">
</head>
<body>
{HEADER}
<main>
{body}
</main>
{FOOTER}
</body>
</html>"""
    with open(os.path.join(BASE, slug), "w") as f:
        f.write(html)
    print("wrote", slug, len(html), "bytes")

def hero(crumbs, eyebrow, h1, lede, ctas, img, alt):
    cta_html = "".join(ctas)
    return f"""<section class="page-hero">
  <div class="wrap split">
    <div class="rv in">
      <p class="crumbs"><a href="index.html">Home</a> &middot; {crumbs}</p>
      <span class="eyebrow">{eyebrow}</span>
      <h1>{h1}</h1>
      <p class="lede">{lede}</p>
      <div class="hero-cta">{cta_html}</div>
    </div>
    <div class="vis rv in d1"><img class="main" src="{img}" alt="{alt}" fetchpriority="high"></div>
  </div>
</section>"""

def band_cta(h2, p, btn, href):
    return f"""<section class="section alt"><div class="wrap"><div class="band-cta rv">
<div><h2>{h2}</h2><p>{p}</p></div>
<a class="btn btn-primary" href="{href}">{btn}</a>
</div></div></section>"""

def checklist(items):
    lis = "".join(f"<li>{ICONS['check']}{t}</li>" for t in items)
    return f'<ul class="check-list">{lis}</ul>'

# ---------------- platform.html ----------------
page("platform.html",
    "Trading Platform — The Orbit Ecosystem",
    "The Orbit trading platform: Orbit Trader, Orbit Manager and Orbit Administrator working as one connected ecosystem across web, Android and Windows.",
    "assets/products/orbit-ecosystem-hero.png",
    hero("Trading Platform", "The Orbit ecosystem", "One platform.<br>Every role.",
         "Orbit Trader for clients, Orbit Manager for broker teams, Orbit Administrator for platform control — one connected technology stack.",
         ['<a class="btn btn-primary" href="contact.html">Request Demo</a>', '<a class="btn btn-ghost" href="trader.html">Explore Orbit Trader</a>'],
         "assets/products/orbit-ecosystem-hero.png", "Orbit Manager, Orbit Trader terminal and mobile app as one ecosystem")
    + """<section class="section alt"><div class="wrap">
<div class="sec-head rv"><span class="eyebrow">Three products, one stack</span><h2>Each role gets its own surface.</h2></div>
<div class="fam-grid">
<article class="fam-card rv"><div class="fam-shot"><img src="assets/products/crop-trader-laptop.png" alt="Orbit Trader terminal" loading="lazy"></div><div class="fam-body"><span class="tag">For traders</span><h3>Orbit Trader</h3><p>Market watch, advanced charts, order entry and positions on web, Android and Windows.</p><a class="more" href="trader.html">Explore</a></div></article>
<article class="fam-card rv d1"><div class="fam-shot"><img src="assets/products/crop-manager.png" alt="Orbit Manager dashboard" loading="lazy"></div><div class="fam-body"><span class="tag">For broker teams</span><h3>Orbit Manager</h3><p>Clients, exposure, dealing, requests and reporting in one operations workspace.</p><a class="more" href="manager.html">Explore</a></div></article>
<article class="fam-card rv d2"><div class="fam-shot"><img src="assets/products/orbit-ecosystem-hero.png" alt="Orbit Administrator control layer" loading="lazy" style="object-position:center"></div><div class="fam-body"><span class="tag">For platform owners</span><h3>Orbit Administrator</h3><p>Symbols, groups, permissions, trading conditions and infrastructure control.</p><a class="more" href="administrator.html">Explore</a></div></article>
</div></div></section>"""
    + """<section class="section tint"><div class="wrap split flip">
<div class="vis rv"><img class="main" src="assets/products/orbit-trader-suite.png" alt="Orbit Trader across desktop and mobile" loading="lazy"></div>
<div class="rv d1"><span class="eyebrow">Consistency</span><h2>Same state, every screen.</h2>
<p class="lede">Watchlists, positions and orders stay consistent as traders move between desktop, web and mobile.</p>
""" + checklist(["Web terminal — no install", "Android app", "Windows desktop"]) + """
<a class="btn btn-primary" href="downloads.html">Platform availability</a></div></div></section>"""
    + band_cta("See the full stack in action.", "Trader, Manager and Administrator — one demo, every role.", "Request Product Demo", "contact.html"))

# ---------------- trader.html ----------------
page("trader.html",
    "Orbit Trader — Web, Android & Windows Trading Terminal",
    "Orbit Trader is the trader-facing terminal for quotes, charting, order entry, positions and account workflows across web, Android and Windows.",
    "assets/products/orbit-trader-suite.png",
    hero("Orbit Trader", "Orbit Trader", "Professional trading.<br>Cleaner by design.",
         "Market Watch, advanced charts, order entry, positions and history — across web, Android and Windows.",
         ['<a class="btn btn-primary" href="contact.html">Request Demo</a>', '<a class="btn btn-ghost" href="downloads.html">Platform availability</a>'],
         "assets/products/orbit-trader-suite.png", "Orbit Trader desktop terminal with XAUUSD chart, order ticket and mobile apps")
    + """<section class="section alt"><div class="wrap">
<div class="sec-head rv"><span class="eyebrow">Core experience</span><h2>Everything between an idea and an order.</h2><p>A focused workspace for quotes, symbols, charts, orders and live positions.</p></div>
<div class="feat-grid">"""
    + feat("globe", "Market Watch", "Multi-asset quotes with bid/ask, change and symbol search across FX, metals, crypto, indices and stocks.")
    + feat("chart", "Advanced Charts", "Multi-timeframe candlestick charts with indicators, drawing tools and volume — including XAUUSD workflows.")
    + feat("bolt", "Order Entry", "Market, limit and stop orders with volume control, margin estimate, pip value and spread visibility.")
    + feat("layers", "Positions & History", "Live positions with P/L, pending orders, trade history and one-tap close actions.")
    + feat("phone", "Mobile Trading", "Watchlist, chart, trade ticket and positions — the full terminal on Android.")
    + feat("desk", "Web & Windows", "Zero-install web terminal and a native-feel Windows desktop experience.")
    + """</div></div></section>"""
    + """<section class="section tint"><div class="wrap split">
<div class="vis rv"><img class="main" src="assets/products/orbit-trader-devices.png" alt="Orbit Trader on laptop and phones" loading="lazy"></div>
<div class="rv d1"><span class="eyebrow">Execution workflow</span><h2>From quote to fill in seconds.</h2>
<p class="lede">A tight loop designed for active traders: watch, analyse, ticket, manage.</p>
""" + checklist(["Watch — multi-asset Market Watch with live bid/ask", "Analyse — XAUUSD-style charting with indicators", "Ticket — one-tap Sell/Buy with SL/TP options", "Manage — positions, orders and history in one view"]) + """
</div></div></section>"""
    + band_cta("See Orbit Trader in action.", "Request a guided walkthrough for your brokerage.", "Request Demo", "contact.html"))

# ---------------- manager.html ----------------
page("manager.html",
    "Orbit Manager — Broker Operations & Risk",
    "Orbit Manager gives broker teams a professional workspace for clients, positions, exposure, requests, dealing and reporting.",
    "assets/products/crop-manager.png",
    hero("Orbit Manager", "Orbit Manager", "Broker operations in<br>one working console.",
         "Clients, positions, exposure, requests and reports — without jumping between disconnected tools.",
         ['<a class="btn btn-primary" href="contact.html">Request Manager Demo</a>', '<a class="btn btn-ghost" href="administrator.html">Orbit Administrator</a>'],
         "assets/products/crop-manager.png", "Orbit Manager dashboard: clients, growth, distribution and recent activity")
    + """<section class="section alt"><div class="wrap">
<div class="sec-head rv"><span class="eyebrow">Operations workspace</span><h2>Designed around the dealing desk.</h2></div>
<div class="feat-grid">"""
    + feat("users", "Clients & Accounts", "Client overview, account status, groups and operational actions in one list.")
    + feat("chart", "Positions & Exposure", "Live positions, pending orders and exposure views for the dealing team.")
    + feat("doc", "Requests", "Operational requests tracked from submission to resolution.")
    + feat("bolt", "Dealing", "Order flow visibility and dealing actions with clear audit context.")
    + feat("layers", "Groups", "Client grouping with leverage and trading-condition control.")
    + feat("globe", "Reports", "Activity, volume and P/L reporting for operations and management.")
    + """</div></div></section>"""
    + """<section class="section tint"><div class="wrap split flip">
<div class="vis tintbg rv"><img class="main" src="assets/products/crop-manager.png" alt="Orbit Manager operations workspace" loading="lazy"></div>
<div class="rv d1"><span class="eyebrow">Risk & audit</span><h2>Exposure you can act on.</h2>
<p class="lede">Risk controls and reporting sit next to the operational workflow — not in a separate tool.</p>
""" + checklist(["Client & account operations", "Positions & exposure monitoring", "Risk controls", "Reporting & audit trail"]) + """
<a class="btn btn-primary" href="contact.html">Request Demo</a></div></div></section>"""
    + band_cta("Run the back office like a product.", "See Orbit Manager on your own workflows.", "Request Product Demo", "contact.html"))

# ---------------- administrator.html ----------------
page("administrator.html",
    "Orbit Administrator — Platform Control for Brokerages",
    "Orbit Administrator is the broker control plane for symbols, groups, permissions, servers, security and platform configuration.",
    "assets/products/orbit-ecosystem-hero.png",
    hero("Orbit Administrator", "Orbit Administrator", "Control the platform<br>from one place.",
         "Symbols, groups, staff permissions, servers, trading conditions and security — in a dedicated administration workspace.",
         ['<a class="btn btn-primary" href="contact.html">Request Administrator Demo</a>', '<a class="btn btn-ghost" href="manager.html">Orbit Manager</a>'],
         "assets/products/orbit-ecosystem-hero.png", "Orbit Administrator control layer across the Orbit ecosystem")
    + """<section class="section alt"><div class="wrap">
<div class="sec-head rv"><span class="eyebrow">Control plane</span><h2>Configure once. Govern everywhere.</h2></div>
<div class="feat-grid">"""
    + feat("globe", "Symbols", "Instrument setup, sessions and feed mapping for every symbol class.")
    + feat("layers", "Groups", "Client groups with leverage, margin and trading-condition templates.")
    + feat("shield", "Permissions", "Scoped staff roles for dealing, risk, support and administration.")
    + feat("cog", "Servers", "Server topology, sessions and operational diagnostics.")
    + feat("doc", "Trading Conditions", "Spreads, commissions, swaps and execution settings per group.")
    + feat("check", "Audit Logs", "Explicit, permissioned and auditable configuration changes.")
    + """</div></div></section>"""
    + """<section class="section tint"><div class="wrap split">
<div class="vis tintbg rv"><img class="main" src="assets/products/crop-manager.png" alt="Orbit Administrator workspace" loading="lazy"></div>
<div class="rv d1"><span class="eyebrow">Platform configuration</span><h2>White label, governed.</h2>
<p class="lede">Branding, domains and release configuration managed from the same control plane.</p>
""" + checklist(["Platform configuration", "White-label setup", "Security policies", "Audit logs"]) + """
<div class="hero-cta"><a class="btn btn-primary" href="white-label.html">Explore White Label</a><a class="btn btn-ghost" href="security.html">Security</a></div>
</div></div></section>"""
    + band_cta("A cleaner control layer for a serious trading business.", "See Orbit Administrator in a guided demo.", "Request Demo", "contact.html"))

print("batch 1 done")

# ---------------- brokers.html ----------------
page("brokers.html",
    "For Brokers — Launch on Orbit Technology",
    "QuotesWare gives brokerages a complete technology stack: Orbit Trader for clients, Orbit Manager for operations, Orbit Administrator for control, plus white label and APIs.",
    "assets/products/orbit-ecosystem-hero.png",
    hero("For Brokers", "For brokers", "Launch your brokerage<br>on Orbit technology.",
         "A complete, modern alternative to legacy stacks — trading terminal, back office and platform control in one product family.",
         ['<a class="btn btn-primary" href="contact.html">Talk to Sales</a>', '<a class="btn btn-ghost" href="white-label.html">White Label</a>'],
         "assets/products/orbit-ecosystem-hero.png", "Orbit ecosystem for brokerages")
    + """<section class="section alt"><div class="wrap">
<div class="sec-head rv"><span class="eyebrow">Why Orbit</span><h2>Everything a brokerage needs to operate.</h2></div>
<div class="feat-grid">"""
    + feat("phone", "Client Terminal", "Orbit Trader on web, Android and Windows — the product your clients touch every day.")
    + feat("users", "Back Office", "Orbit Manager: clients, exposure, dealing, requests and reporting.")
    + feat("cog", "Platform Control", "Orbit Administrator: symbols, groups, permissions and infrastructure.")
    + feat("star", "White Label", "Your brand, colors, domain and app identity on the Orbit stack.")
    + feat("bolt", "Connectivity", "Market-data adapters and feed architecture designed for reliability.")
    + feat("code", "APIs", "REST, WebSocket and webhooks for CRM, payments and custom integrations.")
    + """</div></div></section>"""
    + """<section class="section tint"><div class="wrap split flip">
<div class="vis tintbg rv"><img class="main" src="assets/products/crop-manager.png" alt="Orbit Manager broker operations" loading="lazy"></div>
<div class="rv d1"><span class="eyebrow">Operations</span><h2>One stack, from onboarding to reporting.</h2>
<p class="lede">Client operations, risk and platform configuration stay connected — no patchwork of tools.</p>
""" + checklist(["Client & account operations", "Exposure & risk controls", "Groups, leverage & trading conditions", "Reporting & audit"]) + """
<div class="hero-cta"><a class="btn btn-primary" href="manager.html">Explore Manager</a><a class="btn btn-ghost" href="administrator.html">Administrator</a></div>
</div></div></section>"""
    + band_cta("Bring your brand and business model.", "QuotesWare provides the technology layer. Let's talk about your launch.", "Request Product Demo", "contact.html"))

# ---------------- white-label.html ----------------
page("white-label.html",
    "White Label — Your Brand on Orbit Technology",
    "Launch a fully branded trading experience: custom logo, colors, app identity and domain on web, Android and Windows.",
    "assets/products/orbit-trader-devices.png",
    hero("White Label", "White label", "Your brand.<br>Orbit technology.",
         "A fully branded trading experience on the Orbit stack — your identity across web, Android and Windows.",
         ['<a class="btn btn-primary" href="contact.html">Start a White Label</a>', '<a class="btn btn-ghost" href="brokers.html">For Brokers</a>'],
         "assets/products/orbit-trader-devices.png", "White label Orbit Trader across web, Android and Windows")
    + """<section class="section alt"><div class="wrap">
<div class="sec-head rv"><span class="eyebrow">Brand control</span><h2>Every surface, your identity.</h2></div>
<div class="feat-grid">"""
    + feat("star", "Custom Logo", "Your mark across the terminal, app icons, splash screens and web.")
    + feat("layers", "Broker Color Palette", "Theme the interface to your brand colors.")
    + feat("phone", "Custom App Identity", "App name, icons and store presence under your brand.")
    + feat("globe", "Custom Domain", "Web terminal served from your own domain.")
    + feat("desk", "Web Delivery", "Branded zero-install web trading.")
    + feat("check", "Android & Windows", "Branded mobile and desktop distribution.")
    + """</div></div></section>"""
    + """<section class="section tint"><div class="wrap split">
<div class="vis rv"><img class="main" src="assets/products/crop-phone.png" alt="White label Orbit Trader mobile app" loading="lazy" style="max-width:340px;margin:0 auto"></div>
<div class="rv d1"><span class="eyebrow">How it works</span><h2>From brand kit to launch.</h2>
<p class="lede">A guided path from your brand assets to branded builds on every platform.</p>
""" + checklist(["Share your logo, colors and domain", "We configure your branded theme", "Review on web, Android and Windows", "Launch with your clients"]) + """
<a class="btn btn-primary" href="contact.html">Explore White Label</a></div></div></section>"""
    + band_cta("Launch a better branded trading experience.", "Your brand. Our technology layer.", "Request Product Demo", "contact.html"))

# ---------------- connectivity.html ----------------
page("connectivity.html",
    "Connectivity — Market Data & Feed Architecture",
    "Orbit connectivity: market-data adapters, feed quality monitoring and a routing architecture built for reliable trading.",
    "assets/products/orbit-trader-suite.png",
    hero("Connectivity", "Connectivity", "Market data,<br>engineered for reliability.",
         "Feed adapters, quality monitoring and routing architecture — the data layer behind every Orbit quote and candle.",
         ['<a class="btn btn-primary" href="contact.html">Talk to Sales</a>', '<a class="btn btn-ghost" href="developers.html">Developer Platform</a>'],
         "assets/products/orbit-trader-suite.png", "Orbit Trader with real-time market data")
    + """<section class="section alt"><div class="wrap">
<div class="sec-head rv"><span class="eyebrow">Data layer</span><h2>Quotes you can build a business on.</h2></div>
<div class="feat-grid">"""
    + feat("bolt", "Feed Adapters", "Modular adapters connect market-data sources to the Orbit pricing layer.")
    + feat("chart", "Quality Monitoring", "Feed health, staleness detection and honest status shown in the terminal.")
    + feat("layers", "Symbol Mapping", "Consistent instrument definitions across data sources and the terminal.")
    + feat("shield", "Failover Design", "Architecture designed to degrade gracefully and recover cleanly.")
    + feat("globe", "Multi-Asset", "FX, metals, crypto, indices and stocks through one normalized feed.")
    + feat("cog", "Routing", "Configurable routing between the pricing layer and execution venues.")
    + """</div></div></section>"""
    + """<section class="section tint"><div class="wrap">
<div class="sec-head rv"><span class="eyebrow">Architecture</span><h2>How data flows.</h2><p>Market-data sources feed the Orbit pricing layer, which serves the Trader terminal, Manager operations and API consumers from one normalized stream.</p></div>
<div class="feat-grid">"""
    + feat("globe", "Sources", "External market-data providers via adapters.")
    + feat("bolt", "Orbit Pricing Layer", "Normalization, monitoring and distribution.")
    + feat("phone", "Consumers", "Trader, Manager, Administrator and APIs read one stream.")
    + """</div></div></section>"""
    + band_cta("Design your market-data setup with us.", "Tell us your instruments and regions — we'll map the connectivity.", "Request Demo", "contact.html"))

# ---------------- developers.html ----------------
page("developers.html",
    "Developer Platform — APIs, SDKs & Integrations",
    "Build on Orbit: REST API, WebSocket streams, webhooks and a FIX roadmap — plus SDKs and integration surfaces for broker workflows.",
    "assets/products/orbit-trader-suite.png",
    hero("Developers", "Developer platform", "Build on the<br>Orbit stack.",
         "REST, WebSocket and webhooks for accounts, orders and market data — with SDKs and a FIX roadmap for institutional flows.",
         ['<a class="btn btn-primary" href="contact.html">Get API Access</a>', '<a class="btn btn-ghost" href="connectivity.html">Connectivity</a>'],
         "assets/products/orbit-trader-suite.png", "Orbit Trader ecosystem with developer integration surfaces")
    + """<section class="section alt" id="apis"><div class="wrap">
<div class="sec-head rv"><span class="eyebrow">Integration surfaces</span><h2>APIs for every layer.</h2></div>
<div class="feat-grid">"""
    + feat("code", "REST API", "Accounts, orders, positions and market data over HTTPS with scoped keys.")
    + feat("bolt", "WebSocket", "Streaming quotes, positions and account events in real time.")
    + feat("globe", "Webhooks", "Event-driven callbacks for onboarding, trading and operational events.")
    + feat("layers", "FIX Roadmap", "Institutional FIX connectivity on the roadmap for qualifying partners.")
    + feat("shield", "Auth & Scopes", "Key-based auth with granular scopes per integration.")
    + feat("doc", "SDKs & Docs", "Client libraries and integration guides for common stacks.")
    + """</div></div></section>"""
    + """<section class="section tint"><div class="wrap split">
<div class="rv"><span class="eyebrow">Example</span><h2>Streaming quotes in minutes.</h2>
<p class="lede">Connect, subscribe and receive normalized market data on one stream.</p>
""" + checklist(["Scoped API keys per integration", "Normalized symbols across asset classes", "Sandbox for integration testing"]) + """
<a class="btn btn-primary" href="contact.html">Get API Access</a></div>
<div class="vis rv d1"><div class="form-card" style="font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:13.5px;background:#071B36;color:#C9E8E2;border:none"><pre style="white-space:pre-wrap;margin:0">// subscribe to quotes over WebSocket
const ws = new WebSocket("wss://api.broker.example/stream");
ws.onopen = () =&gt; ws.send(JSON.stringify({
  action: "subscribe",
  symbols: ["XAUUSD", "EURUSD", "BTCUSD"]
}));
ws.onmessage = (e) =&gt; {
  const q = JSON.parse(e.data);
  renderQuote(q.symbol, q.bid, q.ask);
};</pre></div></div>
</div></section>"""
    + band_cta("Start integrating with Orbit.", "Get sandbox access and integration guides.", "Get API Access", "contact.html"))

print("batch 2 done")

# ---------------- security.html ----------------
page("security.html",
    "Security — Access Control, Audit & Resilience",
    "How QuotesWare approaches security: role-based access, audit trails, encrypted communications, backups and operational resilience.",
    "assets/products/orbit-ecosystem-hero.png",
    hero("Security", "Security", "Serious software,<br>serious controls.",
         "Access control, auditability and resilience are designed into the Orbit stack — not bolted on.",
         ['<a class="btn btn-primary" href="contact.html">Talk to Sales</a>', '<a class="btn btn-ghost" href="developers.html">Developer Platform</a>'],
         "assets/products/orbit-ecosystem-hero.png", "Orbit ecosystem with security controls")
    + """<section class="section alt"><div class="wrap">
<div class="sec-head rv"><span class="eyebrow">Controls</span><h2>Designed for regulated operations.</h2><p>QuotesWare provides the technology controls brokerages need to run governed operations. Specific certifications and deployment attestations are confirmed per implementation.</p></div>
<div class="feat-grid">"""
    + feat("shield", "Role-Based Access", "Scoped permissions for traders, dealers, risk, support and administrators.")
    + feat("doc", "Audit Trails", "Configuration and operational actions recorded with actor and timestamp.")
    + feat("check", "Encrypted Communications", "Transport encryption across client, API and service layers.")
    + feat("layers", "Tenant Isolation", "Logical separation between broker deployments and their data.")
    + feat("cog", "Backups & Recovery", "Backup and recovery procedures as part of every deployment plan.")
    + feat("bolt", "Operational Monitoring", "Feed health, session and service visibility for operations teams.")
    + """</div></div></section>"""
    + band_cta("Review the security model with us.", "We walk through controls, deployment and responsibilities on every demo.", "Request Demo", "contact.html"))

# ---------------- downloads.html ----------------
page("downloads.html",
    "Downloads — Orbit Platform Availability",
    "Orbit Trader availability across web, Android and Windows. Check the current distribution for each platform.",
    "assets/products/orbit-trader-devices.png",
    hero("Downloads", "Downloads", "Get Orbit<br>on every screen.",
         "Orbit Trader is delivered across web, Android and Windows — availability per platform below.",
         ['<a class="btn btn-primary" href="contact.html">Request Access</a>'],
         "assets/products/orbit-trader-devices.png", "Orbit Trader on laptop and mobile")
    + """<section class="section alt"><div class="wrap">
<div class="sec-head rv"><span class="eyebrow">Platforms</span><h2>Choose your platform.</h2></div>
<div class="dl-grid">
<div class="dl-card rv">""" + ICONS["globe"] + """<h3>Web Terminal</h3><p>Zero-install trading in the browser. Nothing to download — launch from your broker's domain.</p><a class="btn btn-primary" href="contact.html">Request Access</a></div>
<div class="dl-card rv d1">""" + ICONS["phone"] + """<h3>Android</h3><p>Orbit Trader for Android — Market Watch, charts, orders and positions on the go.</p><a class="btn btn-primary" href="contact.html">Request Access</a></div>
<div class="dl-card rv d2">""" + ICONS["desk"] + """<h3>Windows</h3><p>Orbit Trader for Windows desktop — the full terminal experience on PC.</p><a class="btn btn-primary" href="contact.html">Request Access</a></div>
</div>
<p class="rv" style="margin-top:28px;color:var(--muted);font-size:15px;max-width:44rem">Distribution is managed per broker implementation, including white-label builds. Contact us for the correct installer or link for your brokerage.</p>
</div></section>"""
    + band_cta("Need a specific build?", "White-label and broker-specific distribution is arranged per implementation.", "Contact Us", "contact.html"))

# ---------------- company.html ----------------
page("company.html",
    "About QuotesWare Technologies",
    "QuotesWare Technologies builds modern trading infrastructure: Orbit Trader, Orbit Manager, Orbit Administrator, white label and APIs.",
    "assets/products/orbit-ecosystem-hero.png",
    hero("Company", "About QuotesWare", "Trading infrastructure,<br>built properly.",
         "QuotesWare Technologies is a software company focused on one thing: modern technology for trading businesses.",
         ['<a class="btn btn-primary" href="contact.html">Contact Us</a>', '<a class="btn btn-ghost" href="platform.html">The Platform</a>'],
         "assets/products/orbit-ecosystem-hero.png", "The Orbit product family")
    + """<section class="section alt"><div class="wrap">
<div class="sec-head rv"><span class="eyebrow">What we do</span><h2>Software for trading businesses.</h2><p>We build the Orbit product family — trader terminals, broker operations and platform administration — plus the connectivity and APIs around them.</p></div>
<div class="feat-grid">"""
    + feat("phone", "Orbit Trader", "The trader-facing terminal across web, Android and Windows.")
    + feat("users", "Orbit Manager", "Broker operations: clients, exposure, dealing and reporting.")
    + feat("cog", "Orbit Administrator", "Platform control: symbols, groups, permissions, infrastructure.")
    + """</div></div></section>"""
    + """<section class="section tint"><div class="wrap split">
<div class="rv"><span class="eyebrow">Principles</span><h2>How we build.</h2>
<p class="lede">A few things we hold constant across every release.</p>
""" + checklist(["Real product over mockups — what we show is what we ship", "Honest status — beta and roadmap labels where they apply", "Broker-first design — operations are a product, not an afterthought", "No invented claims — no fake metrics, awards or integrations"]) + """
</div>
<div class="vis rv d1"><img class="main" src="assets/products/orbit-trader-suite.png" alt="Orbit Trader product family" loading="lazy"></div>
</div></section>"""
    + band_cta("Work with QuotesWare.", "Tell us about your brokerage and where you're headed.", "Contact Us", "contact.html"))

# ---------------- resources.html ----------------
page("resources.html",
    "Resources — Docs, Guides & Roadmap",
    "QuotesWare resources: product documentation, integration guides, release notes and the public roadmap.",
    "assets/products/orbit-trader-suite.png",
    hero("Resources", "Resources", "Docs, guides<br>& roadmap.",
         "Product documentation, integration guides and the public roadmap for the Orbit platform.",
         ['<a class="btn btn-primary" href="contact.html">Contact Us</a>'],
         "assets/products/orbit-trader-suite.png", "Orbit Trader resources")
    + """<section class="section alt"><div class="wrap">
<div class="sec-head rv"><span class="eyebrow">Learn</span><h2>Documentation & guides.</h2></div>
<div class="feat-grid">"""
    + feat("doc", "Trader Guides", "Market Watch, charts, order entry, positions and account workflows.")
    + feat("users", "Manager Guides", "Clients, exposure, dealing, requests and reporting workflows.")
    + feat("cog", "Administrator Guides", "Symbols, groups, permissions and platform configuration.")
    + feat("code", "API References", "REST, WebSocket and webhook references with integration examples.")
    + feat("bolt", "Connectivity Notes", "Feed architecture, symbol mapping and monitoring concepts.")
    + feat("shield", "Security Overview", "Access control, audit and resilience model.")
    + """</div>
<p class="rv" style="margin-top:24px;color:var(--muted)">Full documentation is provided with every implementation. Contact us for access to the current docs set.</p>
</div></section>"""
    + """<section class="section tint" id="roadmap"><div class="wrap">
<div class="sec-head rv"><span class="eyebrow">Roadmap</span><h2>Where the platform is headed.</h2><p>Directions we're actively working toward. Availability is confirmed per implementation — nothing here is promised as shipped.</p></div>
<div class="feat-grid">"""
    + feat("bolt", "FIX Connectivity", "Institutional FIX on the roadmap for qualifying partners.")
    + feat("phone", "iOS", "iOS availability is planned — Android, web and Windows lead today.")
    + feat("code", "Algo & Automation", "Automation surfaces for broker workflows and strategy tooling.")
    + """</div></div></section>"""
    + band_cta("Need a specific resource?", "Ask us — we'll point you to the right guide.", "Contact Us", "contact.html"))

# ---------------- contact.html ----------------
page("contact.html",
    "Request Demo — Talk to QuotesWare",
    "Request a demo of Orbit Trader, Orbit Manager and Orbit Administrator. Tell us about your brokerage and we'll arrange a walkthrough.",
    "assets/products/orbit-ecosystem-hero.png",
    hero("Contact", "Request demo", "Let's talk about<br>your brokerage.",
         "Request a guided demo of Orbit Trader, Orbit Manager and Orbit Administrator — or ask about white label and APIs.",
         [],
         "assets/products/orbit-ecosystem-hero.png", "Orbit ecosystem demo")
    + """<section class="section alt"><div class="wrap split">
<div class="rv"><span class="eyebrow">Request a demo</span><h2>Tell us about your business.</h2>
<p class="lede">Share a few details and we'll arrange a walkthrough of the Orbit stack for your team.</p>
""" + checklist(["Guided Trader, Manager and Administrator tour", "White-label and branding discussion", "Connectivity and API scoping"]) + """
</div>
<div class="rv d1"><form class="form-card" data-contact-form>
<div class="frow">
<div class="field"><label for="f-name">Full name</label><input id="f-name" name="name" required autocomplete="name" placeholder="Jane Cooper"></div>
<div class="field"><label for="f-email">Work email</label><input id="f-email" name="email" type="email" required autocomplete="email" placeholder="jane@brokerage.com"></div>
</div>
<div class="frow">
<div class="field"><label for="f-company">Company</label><input id="f-company" name="company" required autocomplete="organization" placeholder="Brokerage Ltd"></div>
<div class="field"><label for="f-role">Role</label><input id="f-role" name="role" autocomplete="organization-title" placeholder="Head of Dealing"></div>
</div>
<div class="field"><label for="f-type">Company type</label><select id="f-type" name="company_type"><option>Brokerage</option><option>Prop firm</option><option>Financial institution</option><option>Technology partner</option><option>Other</option></select></div>
<div class="field"><label for="f-msg">What are you looking to do?</label><textarea id="f-msg" name="message" rows="4" placeholder="Tell us about your timelines, platforms and regions."></textarea></div>
<div class="field"><label style="display:flex;gap:10px;align-items:flex-start;font-weight:500;font-size:14.5px"><input type="checkbox" required style="width:auto;margin-top:4px"> I agree to be contacted about a product demo.</label></div>
<button class="btn btn-primary" type="submit" style="width:100%">Request Product Demo</button>
<p class="contact-status" hidden style="margin-top:16px;font-size:14.5px;color:var(--blue);font-weight:600"></p>
</form></div>
</div></section>"""
    + band_cta("Prefer a direct conversation?", "Tell us who you are and we'll set up the right call.", "Request Product Demo", "contact.html"))

print("batch 3 done")

# ---------------- web-terminal.html ----------------
page("web-terminal.html",
    "Orbit Trader Web Terminal — Zero-Install Browser Trading",
    "Trade from any browser with the Orbit Trader web terminal: market watch, advanced charts, order entry and positions with no install.",
    "assets/products/crop-trader-laptop.png",
    hero("Web Terminal", "Orbit Trader", "The terminal,<br>in your browser.",
         "Zero-install trading with market watch, advanced charts, order entry and positions — on any modern browser.",
         ['<a class="btn btn-primary" href="contact.html">Request Demo</a>', '<a class="btn btn-ghost" href="trader.html">Orbit Trader</a>'],
         "assets/products/crop-trader-laptop.png", "Orbit Trader web terminal with XAUUSD chart")
    + """<section class="section alt"><div class="wrap">
<div class="sec-head rv"><span class="eyebrow">Browser trading</span><h2>Nothing to install. Nothing to miss.</h2></div>
<div class="feat-grid">"""
    + feat("globe", "Zero Install", "Launch from your broker's domain and trade — no download, no admin rights, no updates to manage.")
    + feat("chart", "Full Charting", "Multi-timeframe charts with indicators and drawing tools, just like desktop.")
    + feat("bolt", "Order Entry", "Market, limit and stop orders with SL/TP, margin estimate and spread visibility.")
    + feat("layers", "Responsive Layouts", "Adapts from ultrawide dealing screens to laptop browsers.")
    + feat("shield", "Secure Sessions", "Encrypted sessions with timeout and re-authentication controls.")
    + feat("phone", "Continuity", "Same watchlists, positions and orders as mobile and desktop.")
    + """</div></div></section>"""
    + """<section class="section tint"><div class="wrap split">
<div class="vis rv"><img class="main" src="assets/products/orbit-trader-suite.png" alt="Orbit Trader across web, desktop and mobile" loading="lazy"></div>
<div class="rv d1"><span class="eyebrow">Parity</span><h2>Web that keeps up with desktop.</h2>
<p class="lede">The web terminal is a first-class trading surface — not a lite companion.</p>
""" + checklist(["Market Watch with live bid/ask", "Advanced charts and indicators", "Order ticket with SL/TP", "Positions, orders and history"]) + """
<a class="btn btn-primary" href="contact.html">Request Demo</a></div></div></section>"""
    + band_cta("Trade from anywhere.", "Ask for web terminal access for your brokerage.", "Request Demo", "contact.html"))

# ---------------- mobile.html ----------------
page("mobile.html",
    "Orbit Trader Mobile — Professional Trading on Android",
    "Orbit Trader for Android: Market Watch, advanced charts, one-tap order entry and full position management on mobile.",
    "assets/products/crop-phone.png",
    hero("Mobile", "Orbit Trader", "The full terminal,<br>in your pocket.",
         "Market Watch, charts, orders and positions on Android — professional mobile trading without compromise.",
         ['<a class="btn btn-primary" href="contact.html">Request Demo</a>', '<a class="btn btn-ghost" href="downloads.html">Get the App</a>'],
         "assets/products/crop-phone.png", "Orbit Trader mobile app with market watch")
    + """<section class="section alt"><div class="wrap">
<div class="sec-head rv"><span class="eyebrow">Mobile trading</span><h2>Built for thumbs. Serious about trading.</h2></div>
<div class="feat-grid">"""
    + feat("globe", "Market Watch", "Multi-asset quotes with bid/ask and change, searchable by symbol.")
    + feat("chart", "Mobile Charts", "Candlestick charts with timeframes and indicators, optimized for touch.")
    + feat("bolt", "One-Tap Ticket", "Sell/Buy ticket with volume, SL/TP and margin estimate.")
    + feat("layers", "Positions", "Live positions with P/L, plus orders and history tabs.")
    + feat("shield", "Secure Access", "Session controls designed for trading on the go.")
    + feat("check", "Android Today", "Available for Android now — iOS is on the roadmap.")
    + """</div></div></section>"""
    + """<section class="section tint"><div class="wrap split flip">
<div class="vis rv"><img class="main" src="assets/products/orbit-trader-devices.png" alt="Orbit Trader on Android and laptop" loading="lazy"></div>
<div class="rv d1"><span class="eyebrow">Platforms</span><h2>Android now. iOS planned.</h2>
<p class="lede">Orbit Trader mobile leads on Android, with the same account state as web and Windows.</p>
""" + checklist(["Android app available", "Web terminal on mobile browsers", "iOS on the roadmap", "Same positions everywhere"]) + """
<a class="btn btn-primary" href="downloads.html">Platform availability</a></div></div></section>"""
    + band_cta("Put Orbit Trader in your clients' pockets.", "Ask about mobile distribution for your brand.", "Request Demo", "contact.html"))

# ---------------- algo.html ----------------
page("algo.html",
    "Algo & Automation — Orbit Automation Roadmap",
    "The Orbit automation direction: algorithmic trading, strategy testing and broker workflow automation — current status and roadmap.",
    "assets/products/orbit-trader-suite.png",
    hero("Algo & Automation", "Automation", "Trading,<br>automated responsibly.",
         "Our automation direction covers algorithmic trading, strategy testing and broker workflow automation. Current status is stated honestly below.",
         ['<a class="btn btn-primary" href="contact.html">Request Early Access</a>', '<a class="btn btn-ghost" href="developers.html">Developer Platform</a>'],
         "assets/products/orbit-trader-suite.png", "Orbit Trader with automation roadmap")
    + """<section class="section alt"><div class="wrap">
<div class="sec-head rv"><span class="eyebrow">Direction</span><h2>Where automation is headed.</h2><p>These capabilities are in design or early development — marked honestly, not sold as shipped.</p></div>
<div class="feat-grid">"""
    + feat("code", "Trading Bots", "Automated strategies running against Orbit market data and order entry. In design.")
    + feat("chart", "Strategy Testing", "Backtesting and optimization over historical data. On the roadmap.")
    + feat("layers", "Indicators", "Custom indicators and drawing automation. On the roadmap.")
    + feat("bolt", "Broker Workflows", "Event rules for onboarding, alerts and operational automation. In design.")
    + feat("globe", "API Automation", "Available today: REST, WebSocket and webhooks for programmatic workflows.")
    + feat("shield", "Safe by Design", "Permissions, limits and audit planned into every automation surface.")
    + """</div></div></section>"""
    + """<section class="section tint"><div class="wrap split">
<div class="rv"><span class="eyebrow">Today</span><h2>Automate with APIs now.</h2>
<p class="lede">While terminal automation is on the roadmap, the integration layer is ready for programmatic workflows today.</p>
""" + checklist(["REST API for accounts and orders", "WebSocket for streaming data", "Webhooks for event-driven flows"]) + """
<a class="btn btn-primary" href="developers.html">Explore the APIs</a></div>
<div class="vis rv d1"><img class="main" src="assets/products/orbit-ecosystem-hero.png" alt="Orbit ecosystem" loading="lazy"></div>
</div></section>"""
    + band_cta("Follow the automation roadmap.", "Request early access and help shape what we build.", "Request Early Access", "contact.html"))

# ---------------- news.html ----------------
page("news.html",
    "News — QuotesWare Updates & Releases",
    "Product releases, company updates and announcements from QuotesWare Technologies.",
    "assets/products/orbit-ecosystem-hero.png",
    hero("News", "Newsroom", "Updates from<br>QuotesWare.",
         "Product releases and company announcements — published when there's something real to say.",
         [],
         "assets/products/orbit-ecosystem-hero.png", "QuotesWare news and updates")
    + """<section class="section alt"><div class="wrap">
<div class="sec-head rv"><span class="eyebrow">Latest</span><h2>Release notes & announcements.</h2></div>
<div class="fam-grid">
<article class="fam-card rv"><div class="fam-shot"><img src="assets/products/orbit-ecosystem-hero.png" alt="QuotesWare website" loading="lazy" style="object-position:center"></div>
<div class="fam-body"><span class="tag">4 Oct 2026</span><h3>New QuotesWare corporate website</h3><p>A rebuilt, image-led corporate site covering the Orbit product family — Trader, Manager, Administrator, white label and developer platform.</p></div></article>
<article class="fam-card rv d1"><div class="fam-shot"><img src="assets/products/orbit-trader-suite.png" alt="Orbit Trader 5.8" loading="lazy" style="object-position:center"></div>
<div class="fam-body"><span class="tag">4 Oct 2026</span><h3>Orbit Trader 5.8 ships</h3><p>New Android, Windows desktop and web releases of the Orbit Trader terminal.</p></div></article>
<article class="fam-card rv d2"><div class="fam-shot"><img src="assets/products/crop-manager.png" alt="Orbit Manager" loading="lazy" style="object-position:center top"></div>
<div class="fam-body"><span class="tag">Roadmap</span><h3>Manager & Administrator previews</h3><p>Broker operations and platform administration workspaces in preview — request a walkthrough to see the current state.</p><a class="more" href="contact.html">Request a walkthrough</a></div></article>
</div></div></section>"""
    + band_cta("Stay in the loop.", "Contact us for release updates relevant to your implementation.", "Contact Us", "contact.html"))

# ---------------- careers.html ----------------
page("careers.html",
    "Careers — Work at QuotesWare",
    "Open roles and working principles at QuotesWare Technologies.",
    "assets/products/orbit-trader-suite.png",
    hero("Careers", "Careers", "Build trading<br>technology with us.",
         "We're a focused team building modern trading infrastructure. Current openings are listed below — honestly.",
         [],
         "assets/products/orbit-trader-suite.png", "Careers at QuotesWare")
    + """<section class="section alt"><div class="wrap">
<div class="sec-head rv"><span class="eyebrow">Open roles</span><h2>No current openings.</h2><p>We're not hiring right now. When roles open, they'll be listed here with real descriptions — never placeholders.</p></div>
<div class="feat-grid">"""
    + feat("code", "Engineering", "Trading terminals, broker operations, feeds and infrastructure.")
    + feat("chart", "Product & Design", "Interfaces traders and broker teams rely on every day.")
    + feat("users", "Growth & Partnerships", "Working with brokerages adopting the Orbit stack.")
    + """</div>
<div class="band-cta rv" style="margin-top:44px"><div><h2>Interested in the future?</h2><p>Send your background and what you'd like to build — we'll keep it on file.</p></div><a class="btn btn-primary" href="contact.html">Get in Touch</a></div>
</div></section>"""
    + band_cta("Want to follow our progress?", "News and releases are published as they happen.", "See News", "news.html"))

# ---------------- media.html ----------------
page("media.html",
    "Media Kit — QuotesWare Brand Assets",
    "Official QuotesWare Technologies logos, brand colors, product screenshots and company boilerplate for press and partners.",
    "assets/products/orbit-ecosystem-hero.png",
    hero("Media Kit", "For press & partners", "QuotesWare,<br>presented properly.",
         "Official logos, brand colors, product visuals and boilerplate — with simple usage guidelines.",
         [],
         "assets/products/orbit-ecosystem-hero.png", "QuotesWare media kit")
    + """<section class="section alt"><div class="wrap">
<div class="sec-head rv"><span class="eyebrow">Brand assets</span><h2>Logos & colors.</h2></div>
<div class="feat-grid">"""
    + feat("star", "Primary Logo", "Full-color QuotesWare mark for light backgrounds. Download: assets/logo.png")
    + feat("check", "Reversed Logo", "White version for dark backgrounds. Download: assets/logo-light.png")
    + feat("layers", "Brand Colors", "Deep Navy #071B36 · Teal #12D0BB · Blue #0A4A8A · Background #F7FAFC")
    + """</div></div></section>"""
    + """<section class="section tint"><div class="wrap">
<div class="sec-head rv"><span class="eyebrow">Product visuals</span><h2>Approved screenshots.</h2><p>Current product renders approved for editorial and partner use.</p></div>
<div class="fam-grid">
<article class="fam-card rv"><div class="fam-shot"><img src="assets/products/orbit-ecosystem-hero.png" alt="Orbit ecosystem" loading="lazy" style="object-position:center"></div><div class="fam-body"><h3>Ecosystem hero</h3><p>Manager, Trader terminal and mobile together.</p></div></article>
<article class="fam-card rv d1"><div class="fam-shot"><img src="assets/products/orbit-trader-devices.png" alt="Orbit Trader devices" loading="lazy" style="object-position:center"></div><div class="fam-body"><h3>Trader devices</h3><p>Desktop terminal and mobile apps.</p></div></article>
<article class="fam-card rv d2"><div class="fam-shot"><img src="assets/products/crop-manager.png" alt="Orbit Manager" loading="lazy" style="object-position:center top"></div><div class="fam-body"><h3>Orbit Manager</h3><p>Broker operations dashboard.</p></div></article>
</div></div></section>"""
    + """<section class="section alt"><div class="wrap split">
<div class="rv"><span class="eyebrow">Boilerplate</span><h2>Company description.</h2>
<p class="lede">"QuotesWare Technologies builds modern trading infrastructure — Orbit Trader for traders, Orbit Manager and Orbit Administrator for brokerages, plus white label, connectivity and APIs."</p>
""" + checklist(["Don't stretch, recolor or rearrange the logo", "Don't place the logo on clashing backgrounds", "Don't imply endorsement or partnership without agreement"]) + """
</div><div class="rv d1"><div class="form-card"><h3 style="margin-bottom:12px">Press contact</h3><p style="color:var(--muted);margin-bottom:20px">For interviews, assets and partnership inquiries.</p><a class="btn btn-primary" href="contact.html">Contact Us</a></div></div>
</div></section>"""
    + band_cta("Need something specific?", "Ask for the asset or information you need.", "Contact Us", "contact.html"))

# ---------------- privacy.html ----------------
page("privacy.html",
    "Privacy Policy",
    "How QuotesWare Technologies handles information submitted through this website.",
    "assets/products/orbit-ecosystem-hero.png",
    hero("Legal", "Privacy policy", "Your privacy,<br>stated plainly.",
         "What this website collects, why, and your choices. Last updated: October 2026.",
         [],
         "assets/products/orbit-ecosystem-hero.png", "QuotesWare privacy")
    + """<section class="section alt"><div class="wrap" style="max-width:46rem">
<div class="rv">
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

# ---------------- terms.html ----------------
page("terms.html",
    "Terms of Use",
    "Terms for using the QuotesWare Technologies website.",
    "assets/products/orbit-ecosystem-hero.png",
    hero("Legal", "Terms of use", "The fine print,<br>in plain language.",
         "The rules for using this website. Last updated: October 2026.",
         [],
         "assets/products/orbit-ecosystem-hero.png", "QuotesWare terms")
    + """<section class="section alt"><div class="wrap" style="max-width:46rem">
<div class="rv">
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

# ---------------- cookies.html ----------------
page("cookies.html",
    "Cookie Notice",
    "How QuotesWare Technologies uses cookies and local storage on this website.",
    "assets/products/orbit-ecosystem-hero.png",
    hero("Legal", "Cookie notice", "Cookies,<br>kept minimal.",
         "What this site stores on your device and why. Last updated: October 2026.",
         [],
         "assets/products/orbit-ecosystem-hero.png", "QuotesWare cookies")
    + """<section class="section alt"><div class="wrap" style="max-width:46rem">
<div class="rv">
<h2 style="font-size:24px;margin-bottom:12px">Essential storage</h2>
<p style="color:var(--muted);margin-bottom:28px">This website may store a draft of your demo request form on your own device (local storage) so you don't lose what you typed. This never leaves your browser unless you submit the form.</p>
<h2 style="font-size:24px;margin-bottom:12px">No tracking cookies</h2>
<p style="color:var(--muted);margin-bottom:28px">We don't use advertising trackers, cross-site tracking cookies or third-party analytics beacons on this site. If that changes, this notice will be updated first.</p>
<h2 style="font-size:24px;margin-bottom:12px">Your control</h2>
<p style="color:var(--muted);margin-bottom:28px">You can clear site storage at any time in your browser settings — the site keeps working without it.</p>
<p style="color:var(--muted);font-size:14px">This page is general information, not legal advice.</p>
</div></div></section>"""
    + band_cta("Questions?", "Ask us directly.", "Contact Us", "contact.html"))

# ---------------- institutions.html ----------------
page("institutions.html",
    "For Institutions — Funds, Prop Firms & Enterprises",
    "Orbit technology for hedge funds, prop firms and financial institutions: multi-asset trading, APIs and broker-grade operations.",
    "assets/products/orbit-ecosystem-hero.png",
    hero("For Institutions", "For institutions", "Institutional workflows,<br>modern stack.",
         "For hedge funds, prop firms and financial institutions that need professional trading technology without legacy drag.",
         ['<a class="btn btn-primary" href="contact.html">Talk to Sales</a>', '<a class="btn btn-ghost" href="developers.html">APIs</a>'],
         "assets/products/orbit-ecosystem-hero.png", "Orbit technology for institutions")
    + """<section class="section alt"><div class="wrap">
<div class="sec-head rv"><span class="eyebrow">Use cases</span><h2>Built for professional scale.</h2></div>
<div class="feat-grid">"""
    + feat("chart", "Multi-Asset Trading", "FX, metals, crypto, indices and stocks through one terminal and one feed.")
    + feat("code", "Programmatic Access", "REST, WebSocket and webhooks available today; FIX on the roadmap.")
    + feat("users", "Team Operations", "Manager workspaces for client and exposure oversight.")
    + feat("cog", "Platform Control", "Administrator control over symbols, groups, permissions and conditions.")
    + feat("star", "White Label", "Branded deployment for client-facing offerings.")
    + feat("shield", "Governance", "Role-based access and audit trails designed for oversight.")
    + """</div></div></section>"""
    + """<section class="section tint"><div class="wrap split flip">
<div class="vis tintbg rv"><img class="main" src="assets/products/crop-manager.png" alt="Operations workspace" loading="lazy"></div>
<div class="rv d1"><span class="eyebrow">Prop firms</span><h2>Challenges, the clean way.</h2>
<p class="lede">Prop firms can run evaluation and funded workflows on the Orbit stack with clear account operations and reporting.</p>
""" + checklist(["Account operations & grouping", "Performance & activity reporting", "Risk visibility", "API-driven workflows"]) + """
<a class="btn btn-primary" href="contact.html">Discuss Your Model</a></div></div></section>"""
    + band_cta("Tell us about your institution.", "We'll map the Orbit stack to your workflows.", "Talk to Sales", "contact.html"))

print("batch 4 done")
