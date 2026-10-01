#!/usr/bin/env python3
"""Generates the illustrative PIZERIA pizza artwork (layered SVGs) into ../assets.

These are ILLUSTRATIONS, not photographs. To use real photography later, replace
the files in /assets (same filenames) or change the paths in index.html / js/app.js.
Run:  python3 tools/generate-assets.py
"""
import math, random, os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets")
os.makedirs(OUT, exist_ok=True)
W, C = 800, 400

DEFS = """
<defs>
  <filter id="rough" x="-10%" y="-10%" width="120%" height="120%">
    <feTurbulence type="fractalNoise" baseFrequency="0.018" numOctaves="3" seed="4" result="n"/>
    <feDisplacementMap in="SourceGraphic" in2="n" scale="16"/>
  </filter>
  <filter id="roughS" x="-20%" y="-20%" width="140%" height="140%">
    <feTurbulence type="fractalNoise" baseFrequency="0.06" numOctaves="2" seed="9" result="n"/>
    <feDisplacementMap in="SourceGraphic" in2="n" scale="5"/>
  </filter>
  <filter id="shadow" x="-20%" y="-20%" width="140%" height="150%">
    <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#000" flood-opacity="0.5"/>
  </filter>
  <filter id="softShadow" x="-20%" y="-20%" width="140%" height="150%">
    <feDropShadow dx="0" dy="3" stdDeviation="2.4" flood-color="#2a0d05" flood-opacity="0.45"/>
  </filter>
  <filter id="grain" x="0" y="0" width="100%" height="100%">
    <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed="2" result="t"/>
    <feColorMatrix in="t" type="matrix" values="0 0 0 0 0.25  0 0 0 0 0.12  0 0 0 0 0.04  0 0 0 0.55 -0.12"/>
    <feComposite in2="SourceGraphic" operator="in"/>
  </filter>
  <radialGradient id="gDough" cx="50%" cy="46%" r="55%">
    <stop offset="0" stop-color="#ebbd78"/><stop offset=".78" stop-color="#d79a50"/><stop offset="1" stop-color="#b9732e"/>
  </radialGradient>
  <radialGradient id="gCrust" cx="50%" cy="50%" r="50%">
    <stop offset=".80" stop-color="#e2a85b"/><stop offset=".93" stop-color="#cf8a3c"/><stop offset="1" stop-color="#a9621f"/>
  </radialGradient>
  <radialGradient id="gTomato" cx="50%" cy="48%" r="55%">
    <stop offset="0" stop-color="#c8402f"/><stop offset="1" stop-color="#9c2a1f"/>
  </radialGradient>
  <radialGradient id="gWhite" cx="50%" cy="48%" r="55%">
    <stop offset="0" stop-color="#f2e7cc"/><stop offset="1" stop-color="#dfcda5"/>
  </radialGradient>
  <radialGradient id="gSpicy" cx="50%" cy="48%" r="55%">
    <stop offset="0" stop-color="#cf4a14"/><stop offset="1" stop-color="#8d2509"/>
  </radialGradient>
  <radialGradient id="gMozz" cx="40%" cy="35%" r="70%">
    <stop offset="0" stop-color="#fff6e0"/><stop offset="1" stop-color="#f0dfb8"/>
  </radialGradient>
  <radialGradient id="gPep" cx="42%" cy="38%" r="70%">
    <stop offset="0" stop-color="#cf3b2c"/><stop offset=".7" stop-color="#a62a1f"/><stop offset="1" stop-color="#7d1d15"/>
  </radialGradient>
  <linearGradient id="gBasil" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#4e9a43"/><stop offset="1" stop-color="#2b6a2d"/>
  </linearGradient>
  <radialGradient id="gPlate" cx="50%" cy="45%" r="55%">
    <stop offset="0" stop-color="#2b2520"/><stop offset=".85" stop-color="#1c1814"/><stop offset="1" stop-color="#312a23"/>
  </radialGradient>
  <radialGradient id="gSlate" cx="50%" cy="42%" r="75%">
    <stop offset="0" stop-color="#2a221c"/><stop offset="1" stop-color="#0f0c0a"/>
  </radialGradient>
</defs>
"""

def svg(body, size=W, viewbox=None):
    vb = viewbox or f"0 0 {W} {W}"
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="{vb}">'
            f'{DEFS}{body}</svg>')

def scatter(seed, n, rmax, mind, rmin=0.0):
    r = random.Random(seed); pts = []; tries = 0
    while len(pts) < n and tries < 40000:
        tries += 1
        a = r.uniform(0, 2 * math.pi)
        d = rmax * math.sqrt(r.uniform((rmin / rmax) ** 2, 1))
        x, y = C + d * math.cos(a), C + d * math.sin(a)
        if all((x - px) ** 2 + (y - py) ** 2 >= mind ** 2 for px, py, _ in pts):
            pts.append((x, y, r.uniform(0, 360)))
    return pts

def L_dough():
    r = random.Random(11); s = []
    s.append('<g filter="url(#shadow)"><circle cx="400" cy="400" r="352" fill="url(#gCrust)" filter="url(#rough)"/></g>')
    s.append('<circle cx="400" cy="400" r="306" fill="url(#gDough)" filter="url(#roughS)"/>')
    for _ in range(95):
        a = r.uniform(0, 2 * math.pi); d = r.uniform(312, 346)
        x, y = C + d * math.cos(a), C + d * math.sin(a)
        s.append(f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="{r.uniform(4,13):.1f}" ry="{r.uniform(3,9):.1f}" '
                 f'transform="rotate({math.degrees(a)+90:.0f} {x:.1f} {y:.1f})" fill="#6e3513" opacity="{r.uniform(.35,.7):.2f}"/>')
    for _ in range(60):
        a = r.uniform(0, 2 * math.pi); d = r.uniform(305, 348)
        x, y = C + d * math.cos(a), C + d * math.sin(a)
        s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r.uniform(1.5,4):.1f}" fill="#fbe9c4" opacity=".45"/>')
    return "".join(s)

def sauce(kind):
    g = {"tomato": "gTomato", "white": "gWhite", "spicy": "gSpicy"}[kind]
    r = random.Random({"tomato": 21, "white": 22, "spicy": 23}[kind]); s = []
    s.append(f'<circle cx="400" cy="400" r="296" fill="url(#{g})" filter="url(#rough)"/>')
    swirl = {"tomato": "#e06a50", "white": "#fffaf0", "spicy": "#f08a3a"}[kind]
    for i in range(9):
        rad = 40 + i * 30 + r.uniform(-6, 6); a0 = r.uniform(0, 360)
        x0 = C + rad * math.cos(math.radians(a0)); y0 = C + rad * math.sin(math.radians(a0))
        x1 = C + rad * math.cos(math.radians(a0 + 110)); y1 = C + rad * math.sin(math.radians(a0 + 110))
        s.append(f'<path d="M{x0:.1f} {y0:.1f} A{rad:.1f} {rad:.1f} 0 0 1 {x1:.1f} {y1:.1f}" fill="none" '
                 f'stroke="{swirl}" stroke-width="{r.uniform(5,11):.1f}" opacity=".28" stroke-linecap="round"/>')
    if kind == "spicy":
        for _ in range(70):
            a = r.uniform(0, 2 * math.pi); d = 285 * math.sqrt(r.uniform(0, 1))
            x, y = C + d * math.cos(a), C + d * math.sin(a)
            s.append(f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="{r.uniform(2,4.5):.1f}" ry="{r.uniform(1.2,2.4):.1f}" '
                     f'transform="rotate({r.uniform(0,180):.0f} {x:.1f} {y:.1f})" fill="#5c1405" opacity=".7"/>')
    if kind == "tomato":
        for _ in range(40):
            a = r.uniform(0, 2 * math.pi); d = 285 * math.sqrt(r.uniform(0, 1))
            x, y = C + d * math.cos(a), C + d * math.sin(a)
            s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r.uniform(1.5,3.5):.1f}" fill="#7a1b12" opacity=".35"/>')
    return "".join(s)

def cheese(extra=False):
    r = random.Random(31 if not extra else 37); s = []
    n = 46 if not extra else 34
    for _ in range(n):
        a = r.uniform(0, 2 * math.pi); d = 272 * math.sqrt(r.uniform(0, 1))
        x, y = C + d * math.cos(a), C + d * math.sin(a)
        rx, ry = r.uniform(26, 50), r.uniform(20, 40); rot = r.uniform(0, 180)
        s.append(f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="{rx:.1f}" ry="{ry:.1f}" transform="rotate({rot:.0f} {x:.1f} {y:.1f})" '
                 f'fill="{"url(#gMozz)" if not extra else "#f7e4b0"}" opacity=".97"/>')
        s.append(f'<ellipse cx="{x-rx*.25:.1f}" cy="{y-ry*.3:.1f}" rx="{rx*.45:.1f}" ry="{ry*.3:.1f}" '
                 f'transform="rotate({rot:.0f} {x:.1f} {y:.1f})" fill="#fff" opacity=".35"/>')
        if r.random() < (.35 if not extra else .55):
            s.append(f'<circle cx="{x+r.uniform(-rx*.4,rx*.4):.1f}" cy="{y+r.uniform(-ry*.4,ry*.4):.1f}" r="{r.uniform(4,9):.1f}" fill="#c98a3b" opacity=".55"/>')
    return f'<g filter="url(#softShadow)"><g filter="url(#roughS)">{"".join(s)}</g></g>'

def T_pepperoni():
    s = []
    for x, y, a in scatter(101, 14, 262, 76):
        r = random.Random(int(x * y))
        spots = "".join(f'<circle cx="{r.uniform(-22,22):.1f}" cy="{r.uniform(-22,22):.1f}" r="{r.uniform(2,4):.1f}" fill="#f3b49b" opacity=".5"/>' for _ in range(6))
        s.append(f'<g transform="translate({x:.1f} {y:.1f}) rotate({a:.0f})"><circle r="35" fill="url(#gPep)" stroke="#6e150f" stroke-width="2.5" filter="url(#roughS)"/>'
                 f'{spots}<ellipse cx="-9" cy="-11" rx="14" ry="7" fill="#fff" opacity=".13"/></g>')
    return f'<g filter="url(#softShadow)">{"".join(s)}</g>'

def T_mushroom(n=12, seed=102):
    s = []
    for x, y, a in scatter(seed, n, 265, 70):
        s.append(f'<g transform="translate({x:.1f} {y:.1f}) rotate({a:.0f}) scale(1.15)">'
                 '<path d="M0,-27 C23,-27 35,-8 31,6 C29,13 18,13 12,13 C10,27 8,33 0,33 C-8,33 -10,27 -12,13 C-18,13 -29,13 -31,6 C-35,-8 -23,-27 0,-27 Z" fill="#eadfca" stroke="#b79a72" stroke-width="2.5"/>'
                 '<path d="M0,-17 C14,-17 22,-6 19,3 C18,8 10,8 6,8 C5,18 3,22 0,22 C-3,22 -5,18 -6,8 C-10,8 -18,8 -19,3 C-22,-6 -14,-17 0,-17 Z" fill="#d6c2a0" opacity=".8"/></g>')
    return f'<g filter="url(#softShadow)">{"".join(s)}</g>'

def T_olive():
    s = []
    for x, y, a in scatter(103, 16, 268, 54):
        s.append(f'<g transform="translate({x:.1f} {y:.1f}) rotate({a:.0f})">'
                 '<path fill-rule="evenodd" fill="#1d1a17" stroke="#3a342d" stroke-width="2" d="M16,0 A16,16 0 1 0 -16,0 A16,16 0 1 0 16,0 Z M6,0 A6,6 0 1 1 -6,0 A6,6 0 1 1 6,0 Z"/>'
                 '<path d="M-12,-6 A13,13 0 0 1 4,-12" fill="none" stroke="#6b6358" stroke-width="2.5" stroke-linecap="round" opacity=".8"/></g>')
    return f'<g filter="url(#softShadow)">{"".join(s)}</g>'

def T_basil():
    s = []
    for x, y, a in scatter(104, 7, 250, 104):
        s.append(f'<g transform="translate({x:.1f} {y:.1f}) rotate({a:.0f}) scale(1.35)">'
                 '<path d="M0,-40 C23,-34 31,-8 18,16 C12,28 4,36 0,45 C-4,36 -12,28 -18,16 C-31,-8 -23,-34 0,-40 Z" fill="url(#gBasil)" stroke="#1f5222" stroke-width="1.5"/>'
                 '<path d="M0,-34 L0,40" stroke="#a9d896" stroke-width="2" opacity=".7"/>'
                 '<path d="M0,-14 L-13,-24 M0,-2 L-17,-12 M0,12 L-13,3 M0,-14 L13,-24 M0,-2 L17,-12 M0,12 L13,3" stroke="#a9d896" stroke-width="1.3" opacity=".5" fill="none"/></g>')
    return f'<g filter="url(#softShadow)">{"".join(s)}</g>'

def T_jalapeno():
    s = []
    for x, y, a in scatter(105, 13, 266, 62):
        r = random.Random(int(x + y))
        seeds = "".join(f'<ellipse cx="{r.uniform(-9,9):.1f}" cy="{r.uniform(-9,9):.1f}" rx="2.4" ry="1.5" fill="#f1ecb4" transform="rotate({r.uniform(0,180):.0f})"/>' for _ in range(7))
        s.append(f'<g transform="translate({x:.1f} {y:.1f}) rotate({a:.0f})"><circle r="22" fill="#6f9a30" stroke="#476a1b" stroke-width="2"/>'
                 f'<circle r="16" fill="#b8d26a"/>{seeds}</g>')
    return f'<g filter="url(#softShadow)">{"".join(s)}</g>'

def T_onion():
    s = []
    for x, y, a in scatter(106, 11, 262, 76):
        r = random.Random(int(x * 3 + y))
        arcs = ""
        for rad in (34, 22):
            arcs += (f'<path d="M{-rad},0 A{rad},{rad} 0 0 1 {rad*math.cos(math.radians(r.uniform(120,170))):.1f},{-rad*math.sin(math.radians(r.uniform(20,60))):.1f}" '
                     f'fill="none" stroke="#efe2f1" stroke-width="7" stroke-linecap="round" opacity=".92"/>')
        s.append(f'<g transform="translate({x:.1f} {y:.1f}) rotate({a:.0f})">{arcs}</g>')
    return f'<g filter="url(#softShadow)">{"".join(s)}</g>'

def T_truffle():
    s = []; r = random.Random(107)
    for x, y, a in scatter(107, 20, 262, 48):
        w, h = r.uniform(14, 24), r.uniform(7, 12)
        s.append(f'<g transform="translate({x:.1f} {y:.1f}) rotate({a:.0f})"><path d="M{-w},0 C{-w*.5},{-h} {w*.5},{-h} {w},0 C{w*.5},{h*.8} {-w*.5},{h*.8} {-w},0 Z" fill="#2a1d15" stroke="#4b382b" stroke-width="1.5"/>'
                 f'<path d="M{-w*.5},0 L{w*.5},0" stroke="#6b5444" stroke-width="1" opacity=".6"/></g>')
    return f'<g filter="url(#softShadow)">{"".join(s)}</g>'

def L_cuts():
    s = "".join(f'<line x1="400" y1="400" x2="{400+360*math.cos(math.radians(a)):.1f}" y2="{400+360*math.sin(math.radians(a)):.1f}" stroke="#1a0d06" stroke-opacity=".42" stroke-width="3.5" stroke-linecap="round"/>' for a in range(0, 360, 45))
    return f'<g clip-path="circle(340px at 400px 400px)">{s}</g>'

def L_plate():
    return ('<circle cx="400" cy="404" r="392" fill="#000" opacity=".5" filter="url(#shadow)"/>'
            '<circle cx="400" cy="400" r="392" fill="url(#gPlate)"/>'
            '<circle cx="400" cy="400" r="366" fill="none" stroke="#3b332b" stroke-width="3"/>'
            '<circle cx="400" cy="400" r="376" fill="none" stroke="#fff" stroke-opacity=".06" stroke-width="2"/>')

LAYERS = {
    "plate": L_plate, "dough": L_dough,
    "sauce-tomato": lambda: sauce("tomato"), "sauce-white": lambda: sauce("white"), "sauce-spicy": lambda: sauce("spicy"),
    "cheese-mozzarella": lambda: cheese(False), "cheese-extra": lambda: cheese(True),
    "top-pepperoni": T_pepperoni, "top-mushroom": T_mushroom, "top-olive": T_olive,
    "top-basil": T_basil, "top-jalapeno": T_jalapeno, "top-onion": T_onion, "top-truffle": T_truffle,
    "cuts": L_cuts,
}

def write(name, content):
    with open(os.path.join(OUT, name + ".svg"), "w") as f:
        f.write(content)

for name, fn in LAYERS.items():
    write(name, svg(fn()))

def card(layers, name, scale=.84):
    body = '<rect width="800" height="800" fill="url(#gSlate)"/>'
    body += f'<g transform="translate(400 400) scale({scale}) translate(-400 -400)">{"".join(LAYERS[l]() if isinstance(l,str) else l() for l in layers)}</g>'
    write(name, svg(body))

card(["plate", "dough", "sauce-tomato", "cheese-mozzarella", "top-basil"], "card-margherita")
card(["plate", "dough", "sauce-spicy", "cheese-mozzarella", "top-pepperoni", "top-jalapeno"], "card-pepperoni")
card(["plate", "dough", "sauce-white", "cheese-mozzarella", lambda: T_mushroom(17, 202), "top-truffle"], "card-truffle")
card(["plate", "dough", "sauce-tomato", "cheese-mozzarella", "top-mushroom", "top-olive", "top-onion", "top-basil"], "card-veggie")

body = '<rect width="800" height="800" fill="url(#gSlate)"/>' + "".join(LAYERS[l]() for l in ["dough", "sauce-tomato", "cheese-mozzarella", "top-basil"])
write("crust-closeup", svg(body, viewbox="400 40 400 400"))
print("assets written to", os.path.abspath(OUT), len(os.listdir(OUT)), "files")
