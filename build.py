#!/usr/bin/env python3
"""Generates the static pages. Edit content here, then run: python3 build.py"""
import os
ROOT = os.path.dirname(os.path.abspath(__file__))
PHONE, PHONE_HREF, EMAIL = "816-387-7126", "tel:+18163877126", "koliver@midwestpse.com"
FB, TT, YT = "https://facebook.com/midwestpse", "https://www.tiktok.com/@heavyrescue20", "https://www.youtube.com/@MidwestPSE"
IC = {
 'phone': '<svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"/></svg>',
 'mail': '<svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor"><path d="M20 4H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2zm0 4-8 5-8-5V6l8 5 8-5z"/></svg>',
 'pin': '<svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a7 7 0 0 0-7 7c0 5.25 7 13 7 13s7-7.75 7-13a7 7 0 0 0-7-7zm0 9.5A2.5 2.5 0 1 1 12 6.5a2.5 2.5 0 0 1 0 5z"/></svg>',
 'fb': '<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M14 8V6c0-.9.6-1 1-1h3V1h-4c-3.3 0-4 2.4-4 4v3H7v4h3v11h4V12h3.4l.6-4z"/></svg>',
 'tt': '<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M16.6 2h-3.4v13.4a2.9 2.9 0 1 1-2.1-2.8V9.1a6.3 6.3 0 1 0 5.5 6.3V8.6a8 8 0 0 0 4.4 1.4V6.6A4.6 4.6 0 0 1 16.6 2z"/></svg>',
 'yt': '<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M23 7.2a3 3 0 0 0-2.1-2.1C19 4.6 12 4.6 12 4.6s-7 0-8.9.5A3 3 0 0 0 1 7.2 31 31 0 0 0 .5 12a31 31 0 0 0 .5 4.8 3 3 0 0 0 2.1 2.1c1.9.5 8.9.5 8.9.5s7 0 8.9-.5a3 3 0 0 0 2.1-2.1 31 31 0 0 0 .5-4.8 31 31 0 0 0-.5-4.8zM9.75 15.02V8.98L15.5 12z"/></svg>',
}
RH = "https://responder-hub.com"
NAV = [("/", "Home"), ("/services/", "Services"), ("/completed-projects/", "Projects"), ("/our-team/", "Our Team"), ("/responderhub/", "ResponderHub")]
SERVICES = [
 ("upfitting", "Emergency Vehicle Upfitting", "Warning lights, sirens, consoles, partitions and equipment mounts, wired cleanly and installed to get your crew on the road."),
 ("comms", "Communications Equipment", "New and used mobile and portable radios, installed and programmed for your department."),
 ("grants", "Grant Writing", "Need funding for a large purchase? We help departments find, write and win grants for apparatus and equipment."),
 ("outfitting", "Public Safety Outfitting", "Uniforms, duty gear, equipment and accessories for fire, EMS and law enforcement."),
 ("cpr", "CPR Classes", "American Heart Association certified Heartsaver and BLS classes for your agency, business or community group."),
 ("tech", "Technical Solutions", "Command posts, mobile data and in-vehicle tech. Let us coordinate your technical needs."),
 ("audio", "Vehicle Audio", "Head units, speakers and amplifiers that bring your personal vehicle up to date and sound great."),
 ("aftermarket", "Aftermarket Accessories", "Lighting, bumpers and custom options that turn your current vehicle into something you love to drive."),
]
BUILDS = [("mercer", "Mercer County, MO", "Fire Protection District"), ("harrison", "Harrison County, MO", "Recent build"),
          ("pettis", "Pettis County, MO", "Ambulance District"), ("savannah", "Savannah, MO", "Police Department")]
BRANDS = [("whelen","Whelen"),("havis","Havis"),("511","5.11 Tactical"),("streamlight","Streamlight"),("blackhawk","Blackhawk"),("rothco","Rothco"),
 ("first-tactical","First Tactical"),("under-armour","Under Armour"),("power-products","Power Products / Newmar"),("auxbeam","Auxbeam"),("noco","NOCO"),
 ("blue-sea","Blue Sea Systems"),("proclip","ProClip"),("magnetic-mic","Magnetic Mic"),("bulletpoint","Bulletpoint Mounting Solutions"),
 ("thunderstruck","Thunderstruck"),("boston-leather","Boston Leather"),("pro-fusion-fab","Pro Fusion Fab"),("stat-packs","StatPacks")]
PROJECTS = [
 ("STIO7wITv6A", "pettis", "Ambulance District", "Pettis County Ambulance District", "2024 Chevrolet Tahoe command vehicles with full Whelen CORE builds, HAVIS consoles and Pro Fusion Fab command boxes.", ["2024 Chevy Tahoe", "Whelen CORE", "HAVIS consoles", "Pro Fusion Fab"]),
 ("5Bd8f-iaYnI", "mercer", "Fire Protection District", "Mercer County Fire Protection District", "2024 Chevrolet Silverado 2500HD with a full Whelen lighting build.", ["2024 Silverado 2500HD", "Full Whelen build"]),
 ("PxshODwFmVo", "doniphan", "Rural Fire District", "Doniphan County Rural Fire District #5", "2018 Ford F-350 upfit built with the department's repurposed equipment to stretch their budget.", ["2018 Ford F-350", "Repurposed equipment"]),
 ("OanifwWUaTk", "dekalb", "Fire Protection District", "Central Dekalb Fire Protection District", "Stewart & Stevenson military truck brought into service with Whelen and repurposed equipment.", ["Stewart & Stevenson", "Whelen", "Repurposed equipment"]),
 ("CnW66F1nj0g", "gower", "Fire Protection District", "Gower Fire Protection District", "Lighting updated to new Whelen LEDs.", ["Whelen LED upgrade"]),
]

def page(path, title, desc, body):
    cur = "/" + path.strip("/") + ("/" if path.strip("/") else "")
    AC = ' aria-current="page"'
    nav = "".join(f'<a href="{h}"{AC if h == cur else ""}>{t}</a>' for h, t in NAV)
    html = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:image" content="https://www.midwestpse.com/assets/logo.png">
<meta name="theme-color" content="#0b0b0d"><link rel="icon" href="/assets/favicon.png" type="image/png"><link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Saira+Condensed:ital,wght@0,600;0,800;1,700;1,800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/site.css">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"LocalBusiness","name":"Midwest Public Safety Equipment, LLC","url":"https://www.midwestpse.com","telephone":"+1-816-387-7126","email":"{EMAIL}","foundingDate":"2020","address":{{"@type":"PostalAddress","addressLocality":"Savannah","addressRegion":"MO","addressCountry":"US"}},"sameAs":["{FB}","{YT}","{TT}"]}}</script>
</head><body>
<div class="lightbar"></div>
<header class="hdr"><div class="wrap">
<a class="brand" href="/" aria-label="Midwest Public Safety Equipment home"><img src="/assets/img/logo-sm.webp" alt="" width="50" height="50"><b>Midwest Public Safety Equipment, LLC</b></a>
<button class="menu-btn" aria-label="Menu" aria-expanded="false"><svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor"><path d="M3 6h18v2H3zm0 5h18v2H3zm0 5h18v2H3z"/></svg></button>
<nav class="nav">{nav}<a class="btn btn-red" href="/contact/">Get a quote</a></nav>
</div></header>
<main>{body}</main>
<footer><div class="wrap"><div class="f-grid">
<div><img class="f-logo" src="/assets/img/logo.webp" alt="Midwest Public Safety Equipment – Communications and Lighting" loading="lazy"><p>Full-service emergency vehicle upfitter and public safety equipment outfitter in Northwest Missouri, serving agencies anywhere in the United States.</p>
<div class="socials"><a href="{FB}" aria-label="Facebook" rel="noopener" target="_blank">{IC["fb"]}</a><a href="{YT}" aria-label="YouTube" rel="noopener" target="_blank">{IC["yt"]}</a><a href="{TT}" aria-label="TikTok" rel="noopener" target="_blank">{IC["tt"]}</a></div></div>
<div><h4>Company</h4><ul>{"".join(f'<li><a href="{h}">{t}</a></li>' for h,t in NAV)}<li><a href="/contact/">Contact</a></li><li><a href="{RH}" target="_blank" rel="noopener">responder-hub.com</a></li></ul></div>
<div><h4>Services</h4><ul>{"".join(f'<li><a href="/services/#{k}">{t}</a></li>' for k,t,_ in SERVICES[:6])}</ul></div>
<div><h4>Contact</h4><ul><li><a href="{PHONE_HREF}">{PHONE}</a></li><li><a href="mailto:{EMAIL}">{EMAIL}</a></li><li>Savannah, Missouri</li></ul></div>
</div><div class="f-bot"><span>&copy; <span data-year>2025</span> Midwest Public Safety Equipment, LLC</span><span>Affordable solutions for the career and volunteer.</span></div></div></footer>
<script src="/assets/site.js" defer></script>
</body></html>
'''
    out = os.path.join(ROOT, path, "index.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w").write(html)

def band(title, text):
    return f'''<section class="band"><img src="/assets/img/shop-night.webp" alt="" loading="lazy"><div class="wrap reveal">
<div><h2>{title}</h2><p>{text}</p></div><div class="cta-row"><a class="btn btn-red" href="/contact/">Request a quote</a><a class="btn btn-ghost" href="{PHONE_HREF}">Call {PHONE}</a></div></div></section>'''

def brands():
    return '<div class="brands reveal">' + "".join(f'<div><img src="/assets/brands/{k}.webp" alt="{n}" loading="lazy"></div>' for k, n in BRANDS) + '</div>'

def svc_cards(n=None):
    return "".join(f'''<a class="card svc reveal" href="/services/#{k}"><div class="ph"><img src="/assets/img/svc-{k}.webp" alt="{t}" loading="lazy"></div>
<div class="bd"><span class="num">0{i+1}</span><h3>{t}</h3><p>{d}</p></div></a>''' for i, (k, t, d) in enumerate(SERVICES[:n]))


SVC_FULL = "".join(f'<div class="card svc reveal" id="{k}"><div class="ph"><img src="/assets/img/svc-{k}.webp" alt="{t}" loading="lazy"></div><div class="bd"><span class="num">0{i+1}</span><h3>{t}</h3><p>{d}</p></div></div>' for i, (k, t, d) in enumerate(SERVICES))
BUILD_CARDS = "".join(f'<a class="card reveal" href="/completed-projects/"><div class="ph"><img src="/assets/img/build-{k}.webp" alt="{n} build" loading="lazy"></div><div class="bd"><span class="tag">{s}</span><h3>{n}</h3></div></a>' for k, n, s in BUILDS)

RH_PILLARS = [
 ("schedule", "Scheduling that fills itself", "Rotations like 24/48, Kelly or your own, auto-fill by certification, shift bids, trades, call-ins and time off."),
 ("timeclock", "Hours you can defend", "GPS-located punches checked against the schedule, approved timesheets and payroll export with 7(k) overtime rules."),
 ("inventory", "Rigs, stations & narcotics", "Rig checks that open work orders, preventive maintenance, supply restock and a witnessed narcotics chain of custody."),
 ("hr", "Paperwork without the paper", "W-4, I-9, direct deposit and exposure reports signed in the app and encrypted at rest."),
 ("incident", "Command from the first unit", "An editable ICS board, pre-plans and maps, ICS forms and personnel hours per incident."),
 ("publicdesk", "A front door for the public", "Public notices, messages and records requests, all landing in one office inbox."),
]
RH_CARDS = "".join(f'<div class="card reveal"><div class="ph rh-ph"><img src="/assets/rh/{k}.webp" alt="ResponderHub {t}" loading="lazy"></div><div class="bd"><h3>{t}</h3><p>{d}</p></div></div>' for k, t, d in RH_PILLARS)
RH_SECTION = f'''<section class="s rh-band"><div class="wrap split">
<div class="reveal"><span class="eyebrow">Our software</span><img class="rh-logo" src="/assets/rh/logo.webp" alt="ResponderHub – Fire and EMS Management Suite" width="900" height="255" loading="lazy">
<h2 class="disp" style="font-size:clamp(30px,3.6vw,44px);margin:6px 0 18px">Run the agency. Not the spreadsheets.</h2>
<p>ResponderHub is a product of Midwest Public Safety Equipment, LLC. It runs your agency's scheduling, time clock and payroll, rig checks and maintenance, narcotics custody, HR paperwork, training records, incident command and public notices from one secure hub that crews open on any phone or computer.</p>
<p>Built by a working Firefighter/Paramedic for ambulance districts, fire departments and county systems. Nothing to install.</p>
<div class="cta-row" style="margin-top:28px"><a class="btn btn-red" href="{RH}" target="_blank" rel="noopener">Visit responder-hub.com &nearr;</a><a class="btn btn-ghost" href="/responderhub/">Learn more</a></div></div>
<div class="reveal"><div class="rh-frame"><img src="/assets/rh/schedule.webp" alt="ResponderHub weekly schedule" loading="lazy"></div></div>
</div></section>'''

# ---------- Home
page("", "Midwest Public Safety Equipment | Emergency Vehicle Upfitting – Savannah, MO",
 "Full-service emergency vehicle upfitter and public safety equipment outfitter in Northwest Missouri. Lighting, radios, consoles, outfitting, grants and CPR classes.", f'''
<section class="hero"><img src="/assets/img/build-savannah.webp" alt="Savannah, MO police vehicle with Whelen emergency lighting" fetchpriority="high">
<div class="wrap"><div><span class="eyebrow">Savannah, Missouri &middot; Est. 2020</span>
<h1>Upfitting built for the <em>career &amp; volunteer.</em></h1>
<p class="lead">Midwest Public Safety Equipment is a full-service emergency vehicle upfitter and public safety outfitter. Lighting, radios, consoles and gear, installed right and priced for real department budgets.</p>
<div class="cta-row"><a class="btn btn-red" href="/contact/">Request a quote</a><a class="btn btn-ghost" href="/completed-projects/">See our builds &rarr;</a></div>
<div class="hero-meta"><div><b>Fire &middot; EMS &middot; LE</b>Agencies served</div><div><b>Nationwide</b>Based in NW Missouri</div><div><b>AHA</b>Certified CPR classes</div></div>
</div><div class="hero-logo"><img src="/assets/img/logo.webp" alt="Midwest Public Safety Equipment – Communications and Lighting – 816-387-7126" width="400" height="400"></div></div></section>

<section class="s"><div class="wrap split">
<div class="reveal"><span class="eyebrow">Our story</span><h2 class="disp" style="font-size:clamp(32px,4vw,50px);margin:14px 0 22px">Northwest Missouri needed an upfitter. So we became one.</h2>
<p>Located in Northwest Missouri, Midwest Public Safety Equipment, LLC is a full-service emergency vehicle upfitter and public safety equipment outfitter. Established in 2020, we saw the lack of this service in our region and made it our goal to provide an affordable service to individuals and public safety agencies anywhere in the United States.</p>
<p>We're run by first responders, so we know what a truck needs to do on a call. We offer the products consumers and agencies rely on to do their job effectively every day.</p>
<ul class="checks"><li>Emergency lighting &amp; sirens</li><li>Radios &amp; communications</li><li>Consoles &amp; mounts</li><li>Uniforms &amp; duty gear</li><li>Grant writing help</li><li>CPR / BLS classes</li></ul>
<a class="btn btn-ghost" href="/services/">Explore services &rarr;</a></div>
<div class="photo-stack reveal"><img src="/assets/img/build-mercer.webp" alt="Mercer County FPD Silverado build" loading="lazy"><img src="/assets/img/build-pettis.webp" alt="Pettis County Tahoe console build" loading="lazy"><div class="badge-float"><b>2020</b>Serving since</div></div>
</div></section>

<section class="s s-alt"><div class="wrap">
<div class="s-head"><div><span class="eyebrow">Recent builds</span><h2>Fresh out of the shop</h2></div><p>A few of the agencies we've upfitted lately. Tap a video to watch, or swipe for more on your phone. Watch full walkarounds on our projects page.</p></div>
<div class="rb"><article class="rb-feat reveal"><button class="vid" data-src="/assets/video/push-jeep.mp4" aria-label="Play video: Push Jeep lighting install"><img src="/assets/img/video-push-jeep.webp" alt="Jeep Wrangler push jeep with new warning lights" loading="lazy"><span class="play"><i></i></span></button>
<div class="rb-cap"><span class="tag">Lighting install</span><h3>Push Jeep</h3><p>Warning lights added to a Jeep Wrangler push jeep.</p></div></article>
<article class="rb-feat reveal"><button class="vid" data-src="/assets/video/gentry-so.mp4" aria-label="Play video: Gentry County Sheriff's Department Ford Police Interceptor Utility"><img src="/assets/img/video-gentry.webp" alt="Gentry County Sheriff's Department Ford Police Interceptor Utility build" loading="lazy"><span class="play"><i></i></span></button>
<div class="rb-cap"><span class="tag">Sheriff's Department</span><h3>Gentry County, MO</h3><p>Ford Police Interceptor Utility finished with Whelen Ions and Tracers, a Thunderstruck bumper and a Setina prisoner transport system.</p></div></article>
<article class="rb-feat reveal"><button class="vid" data-src="/assets/video/bethany-pd.mp4" aria-label="Play video: Bethany, MO Police Department Dodge Durango build"><img src="/assets/img/video-bethany.webp" alt="Bethany, MO Police Department Dodge Durango build" loading="lazy"><span class="play"><i></i></span></button>
<div class="rb-cap"><span class="tag">Police Department</span><h3>Bethany, MO</h3><p>Dodge Durango patrol unit. Watch it run through pursuit and park modes.</p></div></article>
<article class="rb-feat reveal"><button class="vid" data-src="/assets/video/griswold-fd.mp4" aria-label="Play video: Griswold, IA Fire Department brush rig"><img src="/assets/img/video-griswold.webp" alt="Griswold, Iowa Fire Department brush rig lighting update" loading="lazy"><span class="play"><i></i></span></button>
<div class="rb-cap"><span class="tag">Fire Department</span><h3>Griswold, IA</h3><p>Brush rig lighting update: old halogens swapped for Whelen.</p></div></article></div>
<div class="grid g4" style="margin-top:24px">{BUILD_CARDS}</div>
</div></section>

<section class="s"><div class="wrap">
<div class="s-head"><div><span class="eyebrow">What we do</span><h2>Everything your department rolls with</h2></div><a class="btn btn-ghost" href="/services/">All services &rarr;</a></div>
<div class="grid g3">{svc_cards(6)}</div>
</div></section>

{RH_SECTION}
<section class="s s-alt"><div class="wrap">
<div class="s-head"><div><span class="eyebrow">Products we provide</span><h2>Brands first responders trust</h2></div><p>We source, install and support equipment from the names you already know.</p></div>
{brands()}
</div></section>
{band("Ready to outfit your next unit?", "Tell us about your vehicle and budget. We'll put together a build that fits, from a single light bar to a full command vehicle.")}
''')

# ---------- Services
page("services", "Services | Midwest Public Safety Equipment",
 "Emergency vehicle upfitting, communications equipment, grant writing, public safety outfitting, CPR classes, vehicle audio and more.", f'''
<section class="page-hero"><img src="/assets/img/svc-upfitting.webp" alt=""><div class="wrap"><span class="eyebrow">Services</span><h1>What we do</h1>
<p>From wiring a full Whelen package to helping you fund the truck it goes on, we cover the work that keeps your department running.</p></div></section>
<section class="s"><div class="wrap"><div class="grid g2">
{SVC_FULL}
</div></div></section>
<section class="s s-alt"><div class="wrap"><div class="s-head"><div><span class="eyebrow">Products we provide</span><h2>Brands we work with</h2></div></div>{brands()}</div></section>
{band("Have a project in mind?", "Lighting, radios, outfitting or a grant application: send us the details and we'll follow up fast.")}
''')

# ---------- Projects
def proj(v, k, tag, name, d, specs):
    spans = "".join(f"<span>{x}</span>" for x in specs)
    return f'''<article class="proj reveal"><button class="vid" data-id="{v}" aria-label="Play video: {name}"><img src="/assets/img/video-{k}.webp" alt="{name} build" loading="lazy"><span class="play"><i></i></span></button>
<div><span class="tag">{tag}</span><h2>{name}</h2><p>{d}</p><div class="spec">{spans}</div></div></article>'''
page("completed-projects", "Completed Projects | Midwest Public Safety Equipment",
 "Recent emergency vehicle builds for Gentry County Sheriff's Department, Bethany, MO Police Department, Griswold, IA Fire Department, Pettis County Ambulance District, Mercer County FPD, Doniphan County RFD #5, Central Dekalb FPD and Gower FPD.", f'''
<section class="page-hero"><img src="/assets/img/build-mercer.webp" alt=""><div class="wrap"><span class="eyebrow">Completed projects</span><h1>Our builds</h1>
<p>Tap any video to see the walkaround. More on our <a href="{YT}" target="_blank" rel="noopener">YouTube channel</a>.</p></div></section>
<section class="s"><div class="wrap">
<article class="proj reveal"><button class="vid" data-src="/assets/video/push-jeep.mp4" aria-label="Play video: Push Jeep lighting install"><img src="/assets/img/video-push-jeep.webp" alt="Jeep Wrangler push jeep with new warning lights" loading="lazy"><span class="play"><i></i></span></button>
<div><span class="tag">Lighting install</span><h2>Push Jeep</h2><p>We put warning lights on this Jeep Wrangler push jeep.</p><div class="spec"><span>Jeep Wrangler</span><span>Warning lights</span></div></div></article>
<article class="proj reveal"><button class="vid" data-src="/assets/video/gentry-so.mp4" aria-label="Play video: Gentry County Sheriff's Department"><img src="/assets/img/video-gentry.webp" alt="Gentry County Sheriff's Department Ford Police Interceptor Utility build" loading="lazy"><span class="play"><i></i></span></button>
<div><span class="tag">Sheriff's Department</span><h2>Gentry County Sheriff's Department</h2><p>This new Ford Police Interceptor Utility came to us with some Code 3 equipment pre-installed. We gave it the Whelen touch and finished it out with Ions and Tracers, plus a Thunderstruck bumper, Getac DVR system, Setina Pro-Cell prisoner transport system and a triple gun mount.</p><div class="spec"><span>Ford PI Utility</span><span>Whelen Ion &amp; Tracer</span><span>Thunderstruck bumper</span><span>Getac DVR</span><span>Setina Pro-Cell</span><span>Triple gun mount</span></div></div></article>
<article class="proj reveal"><button class="vid" data-src="/assets/video/bethany-pd.mp4" aria-label="Play video: Bethany, MO Police Department"><img src="/assets/img/video-bethany.webp" alt="Bethany, MO Police Department Dodge Durango build" loading="lazy"><span class="play"><i></i></span></button>
<div><span class="tag">Police Department</span><h2>Bethany, MO Police Department</h2><p>Dodge Durango patrol unit upfitted with emergency lighting, shown in pursuit mode and park mode.</p><div class="spec"><span>Dodge Durango</span><span>Emergency lighting</span><span>Patrol unit</span></div></div></article>
<article class="proj reveal"><button class="vid" data-src="/assets/video/griswold-fd.mp4" aria-label="Play video: Griswold, IA Fire Department"><img src="/assets/img/video-griswold.webp" alt="Griswold, Iowa Fire Department brush rig lighting update" loading="lazy"><span class="play"><i></i></span></button>
<div><span class="tag">Fire Department</span><h2>Griswold, Iowa Fire Department</h2><p>Out with the old, in with the new. We swapped all of the old halogen lighting on the department's brush rig for top-of-the-line Whelen equipment.</p><div class="spec"><span>Brush rig</span><span>Halogen to Whelen LED</span><span>Lighting update</span></div></div></article>
{"".join(proj(*p) for p in PROJECTS)}
<article class="proj reveal"><div class="still"><img src="/assets/img/grant-nta-ems.webp" alt="NTA EMS Rescue 2024 Demers Transit ambulance delivered" loading="lazy"></div>
<div><span class="tag">Grant acquisition</span><h2>NTA EMS Rescue</h2><p>We helped NTA EMS Rescue secure the grant funding to purchase a new 2024 Demers Transit ambulance, now delivered and in service.</p><div class="spec"><span>Grant writing</span><span>2024 Demers Transit TSE</span></div>
<p style="margin-top:22px"><a class="btn btn-ghost" href="/services/#grants">About grant writing &rarr;</a></p></div></article>
</div></section>
{band("Want your unit featured here?", "Every build starts with a conversation. Let's talk about yours.")}
''')

# ---------- Team
page("our-team", "Our Team | Midwest Public Safety Equipment",
 "Meet the first responders and builders behind Midwest Public Safety Equipment.", f'''
<section class="page-hero"><img src="/assets/img/shop-night.webp" alt=""><div class="wrap"><span class="eyebrow">Our team</span><h1>Built by responders</h1>
<p>We've worked both sides of the volunteer and career service, so we build every unit like we're the ones riding in it.</p></div></section>
<section class="s"><div class="wrap">
<div class="member reveal"><div class="m-ph"><img src="/assets/img/team-kyler.webp" alt="Kyler Oliver" loading="lazy"></div>
<div><span class="eyebrow">Founder</span><h2>Kyler Oliver, M.S., NRP</h2><div class="role">Firefighter / Paramedic</div>
<p>Kyler is the founder of Midwest Public Safety Equipment, LLC. He is a full-time Firefighter/Paramedic with over 12 years of experience in public safety and emergency communications.</p>
<p>He holds a Master's degree in Emergency Services Management and has worked in both the volunteer and career sides of public safety. He and his family live in Savannah.</p></div></div>
<div class="member rev reveal"><div class="m-ph"><img src="/assets/img/team-kyle.webp" alt="Kyle Price" loading="lazy" style="object-position:50% 30%"></div>
<div><span class="eyebrow">Installs &amp; fabrication</span><h2>Kyle Price</h2><div class="role">The muscle of the operation</div>
<p>Kyle's background in construction and vehicle mechanics makes him an invaluable member of our team. He brings a tremendous amount of knowledge to every vehicle, finds solutions to tough problems, and customizes each build to the customer's needs.</p></div></div>
</div></section>
{band("Let's build something together.", "Questions about a build, equipment or a class? We're a call away.")}
''')

# ---------- ResponderHub
page("responderhub", "ResponderHub | Fire & EMS Management Suite by Midwest PSE",
 "ResponderHub, a product of Midwest Public Safety Equipment: scheduling, time clock, payroll, rig checks, narcotics custody, HR forms and incident command for fire and EMS agencies.", f'''
<section class="page-hero rh-hero"><img src="/assets/rh/schedule.webp" alt=""><div class="wrap"><span class="eyebrow">A Midwest PSE product</span>
<img class="rh-logo" src="/assets/rh/logo.webp" alt="ResponderHub – Fire and EMS Management Suite" width="900" height="255" style="max-width:520px;margin:18px 0 10px">
<p>One secure hub for fire and EMS agencies: scheduling, time clock and payroll, rig checks, narcotics custody, HR paperwork, training and incident command. It runs in the browser on any phone or computer.</p>
<div class="cta-row" style="margin-top:28px"><a class="btn btn-red" href="{RH}" target="_blank" rel="noopener">Request a demo at responder-hub.com &nearr;</a><a class="btn btn-ghost" href="{RH}/signin" target="_blank" rel="noopener">Agency sign in</a></div></div></section>
<section class="s"><div class="wrap"><div class="s-head"><div><span class="eyebrow">What it does</span><h2>Every hub your agency needs</h2></div><p>Turn each hub on or off per agency. One login per employee, nothing to install.</p></div>
<div class="grid g3">{RH_CARDS}</div></div></section>
<section class="s s-alt"><div class="wrap"><div class="s-head"><div><span class="eyebrow">Who it's for</span><h2>Built for responders</h2></div></div><div class="grid g3">
<div class="card reveal"><div class="bd"><h3>Ambulance districts &amp; EMS</h3><p>Career, part-time and PRN crews across stations and units, with narcotics custody and supply tracking built in.</p></div></div>
<div class="card reveal"><div class="bd"><h3>Fire departments</h3><p>Career and combination departments: apparatus checks that create work orders, pre-plans and maps, an ICS board and training due dates.</p></div></div>
<div class="card reveal"><div class="bd"><h3>County &amp; multi-agency systems</h3><p>Several agencies on one platform, each with its own database, logins, branding and feature set.</p></div></div>
</div></div></section>
<section class="band"><img src="/assets/img/shop-night.webp" alt="" loading="lazy"><div class="wrap reveal"><div><h2>See ResponderHub in action</h2><p>Request a demo and we'll walk your agency through every hub.</p></div>
<div class="cta-row"><a class="btn btn-red" href="{RH}" target="_blank" rel="noopener">Go to responder-hub.com</a><a class="btn btn-ghost" href="{PHONE_HREF}">Call {PHONE}</a></div></div></section>
''')

# ---------- Contact
opts = "".join(f"<option>{t}</option>" for _, t, _ in SERVICES) + "<option>Other</option>"
page("contact", "Contact | Midwest Public Safety Equipment",
 "Request a quote for emergency vehicle upfitting, equipment, outfitting or CPR classes. Call 816-387-7126.", f'''
<section class="page-hero"><img src="/assets/img/build-savannah.webp" alt=""><div class="wrap"><span class="eyebrow">Contact</span><h1>Get a quote</h1>
<p>Tell us what you're working with and we'll get back to you.</p></div></section>
<section class="s"><div class="wrap contact-grid">
<div class="reveal">
<a class="c-item" href="{PHONE_HREF}"><span class="ic">{IC["phone"]}</span><span><small>Call or text</small><b>{PHONE}</b></span></a>
<a class="c-item" href="mailto:{EMAIL}"><span class="ic">{IC["mail"]}</span><span><small>Email</small><b>{EMAIL}</b></span></a>
<div class="c-item"><span class="ic">{IC["pin"]}</span><span><small>Based in</small><b>Savannah, Missouri</b><br><span style="color:var(--mut);font-size:14px">Serving agencies nationwide</span></span></div>
<a class="c-item" href="{FB}" target="_blank" rel="noopener"><span class="ic">{IC["fb"]}</span><span><small>Follow us</small><b>facebook.com/midwestpse</b></span></a>
</div>
<form class="quote reveal"><h3>Request a quote</h3><p>Opens an email to us with your details filled in.</p>
<div class="fr"><label>Name<input name="Name" required autocomplete="name"></label><label>Agency / company<input name="Agency"></label></div>
<div class="fr"><label>Phone<input name="Phone" type="tel" autocomplete="tel"></label><label>Email<input name="Email" type="email" autocomplete="email"></label></div>
<div class="fr"><label>Service<select name="Service">{opts}</select></label><label>Vehicle (year / make / model)<input name="Vehicle"></label></div>
<label>Project details<textarea name="message" placeholder="Lighting package, radios, timeline, budget…"></textarea></label>
<button class="btn btn-red" type="submit" style="width:100%">Send request</button></form>
</div></section>
''')

for old in ("home",):
    p = os.path.join(ROOT, old, "index.html"); os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w").write('<!doctype html><meta http-equiv="refresh" content="0;url=/"><link rel="canonical" href="/">')
open(os.path.join(ROOT, "404.html"), "w").write('<!doctype html><meta http-equiv="refresh" content="0;url=/"><title>Not found</title>')
print("built")
