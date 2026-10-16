#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PROSYB - KHAZNA ORY01 (Fouju, 77) - Base vie et chantier
Plans d'implantation de principe des lots courants faibles (SVG vectoriels).

Fond de plan masse commun redessine (non a l'echelle, nord suppose en haut),
puis un plan par lot : SSI, IT, Video, AV/affichage, GTB, et une synthese.

Sources : dce_facts.md (sections A a H). Positions non connues = "a confirmer".
Usage : python3 plans.py   -> ecrit plan_*.svg dans le dossier du script.
"""
import math
import os
from xml.sax.saxutils import escape

OUT = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------- palette
VIOLET = "#8860FE"
BLEU = "#7598F4"
CYAN = "#66C2EB"
ENCRE = "#2B2640"
GRIS = "#6E6A86"
ZONE = "#F7F6FC"
TRAIT = "#E4E1F0"
ROUGE = "#E5484D"
P_COL = {"P2": "#8860FE", "P3": "#7598F4", "P4": "#3FA7D6"}
FONT = "Arial, 'Liberation Sans', Helvetica, sans-serif"

W, H = 1600, 1100
PANEL_X = 1172          # panneau droit (legende, hypotheses, cartouche)
PLAN_CLIP = (8, 64, 1152, 1028)

# ---------------------------------------------------------------- geometrie (repere ecran, nord suppose en haut)
FENCE = [(250, 130), (690, 130), (1100, 580), (1100, 990), (250, 990)]
# anneau fibre / fourreaux CFA : 6 px a l'interieur de la cloture
RING_W = 256            # x de la cloture ouest (interieur)
RING_N = 136            # y de la cloture nord (interieur)
RING_S = 984            # y de la cloture sud (interieur)
RING_E = 1094           # x de la cloture est (interieur)
DIAG_A = (684, 136)     # debut diagonale interieure (RD57)
DIAG_B = (1094, 586)    # fin diagonale interieure


def diag_x(y):
    """x de la cloture nord-est (diagonale RD57) a l'ordonnee y."""
    return 690 + (y - 130) * 410.0 / 450.0


def ring_diag(y):
    return (DIAG_A[0] + (y - DIAG_A[1]) * 410.0 / 450.0, y)


BUILDING = (330, 530, 800, 905)          # x0, y0, x1, y1
TRACK = (310, 505, 820, 925)
PARKING = (270, 192, 420, 430)
HUB1 = (318, 466, 380, 490)
HUB2 = (600, 936, 662, 958)
HUB3 = (95, 570, 157, 592)
PG = (430, 146, 512, 182)                # poste de garde principal
TRIPODES_A = [(524, 164), (540, 164)]
TRIPODES_B = [(640, 448), (656, 448)]
ACCESS_CTRL = (668, 441, 708, 456)
BV_LIMIT_Y = 444
ISL_W, ISL_H = 76, 44
COLS = [466, 554, 642, 730]
ROWS = [232, 292, 352]
ISLANDS = {  # n : (x, y, phase)
    1: (COLS[0], ROWS[0], "P2"), 2: (COLS[1], ROWS[0], "P2"), 3: (COLS[2], ROWS[0], "P3"),
    4: (COLS[0], ROWS[1], "P3"), 5: (COLS[1], ROWS[1], "P3"), 6: (COLS[2], ROWS[1], "P3"),
    7: (COLS[0], ROWS[2], "P3"), 8: (COLS[1], ROWS[2], "P3"), 9: (COLS[2], ROWS[2], "P3"),
    10: (COLS[3], ROWS[2], "P3"),
}
FT2 = (730, 238, 770, 270)
FT1 = (845, 378)
HSE1 = (828, 400, 890, 432)
HSE2 = (900, 462, 962, 494)
WASTE = (860, 556, 990, 616)
LIVRAISON = (860, 640, 990, 684)
STORAGE = (860, 710, 1040, 860)
BAT_TECH = (1000, 888, 1048, 936)
EA1 = (405, 130)        # emergency access NO (sur cloture nord)
EA2 = (diag_x(200), 200)  # emergency access NE (sur diagonale, pres Fire Tank 2)
GIRATOIRE = (716, 98)
DC11 = (36, 140, 204, 990)
DC11_N = (46, 186, 194, 540)
DC11_S = (46, 664, 194, 960)

# coffrets de zone / repartiteurs secondaires (sur l'anneau)
COF = {
    "R.O.1": (RING_W, 308),
    "R.N": ring_diag(330),
    "R.E.1": ring_diag(520),
    "R.E.2": (RING_E, 700),
    "R.E.3": (RING_E, 962),
    "R.O.2": (RING_W, 962),
}
HUB1_C = ((HUB1[0] + HUB1[2]) / 2, (HUB1[1] + HUB1[3]) / 2)
HUB2_C = ((HUB2[0] + HUB2[2]) / 2, (HUB2[1] + HUB2[3]) / 2)
HUB3_C = ((HUB3[0] + HUB3[2]) / 2, (HUB3[1] + HUB3[3]) / 2)
PG_C = ((PG[0] + PG[2]) / 2, (PG[1] + PG[3]) / 2)

RING_PATH = [
    (HUB1[0], 478), (RING_W, 478), (RING_W, RING_N), DIAG_A, DIAG_B,
    (RING_E, RING_S), (HUB2_C[0], RING_S), (HUB2_C[0], HUB2[3]), (HUB2_C[0], RING_S),
    (RING_W, RING_S), (RING_W, 478),
]


# ---------------------------------------------------------------- SVG helper
class SVG:
    def __init__(self):
        self.parts = []
        self.labels = []   # (x0, y0, x1, y1, text) pour controle des chevauchements

    def add(self, s):
        self.parts.append(s)

    def open_g(self, gid=None, extra=""):
        a = ' id="%s"' % gid if gid else ""
        self.add("<g%s %s>" % (a, extra))

    def close_g(self):
        self.add("</g>")

    def text(self, x, y, s, size=12, color=ENCRE, anchor="start", weight="normal",
             halo=True, italic=False, rotate=None, reg=True, opacity=None):
        st = []
        if halo:
            st.append("paint-order:stroke;stroke:#FFFFFF;stroke-width:3px;stroke-linejoin:round")
        tr = ' transform="rotate(%g %g %g)"' % (rotate, x, y) if rotate else ""
        it = ' font-style="italic"' if italic else ""
        op = ' opacity="%g"' % opacity if opacity else ""
        self.add('<text x="%.1f" y="%.1f" font-size="%g" fill="%s" text-anchor="%s" '
                 'font-weight="%s"%s%s%s style="%s">%s</text>'
                 % (x, y, size, color, anchor, weight, it, tr, op, ";".join(st), escape(s)))
        if reg and not rotate:
            w = text_w(s, size, weight)
            x0 = x - w if anchor == "end" else (x - w / 2 if anchor == "middle" else x)
            self.labels.append((x0, y - size * 0.78, x0 + w, y + size * 0.22, s))

    def render(self, title):
        head = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" '
                'font-family="%s">\n<title>%s</title>\n'
                '<rect x="0" y="0" width="%d" height="%d" fill="#FFFFFF"/>\n'
                % (W, H, W, H, FONT, escape(title), W, H))
        defs = ('<defs><clipPath id="clipPlan"><rect x="%d" y="%d" width="%d" height="%d"/></clipPath>'
                '<pattern id="hatchP4" width="8" height="8" patternUnits="userSpaceOnUse" '
                'patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="8" stroke="%s" '
                'stroke-width="1.2" opacity="0.35"/></pattern>'
                '<pattern id="hatchGray" width="7" height="7" patternUnits="userSpaceOnUse" '
                'patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="7" stroke="%s" '
                'stroke-width="1"/></pattern></defs>\n'
                % (PLAN_CLIP[0], PLAN_CLIP[1], PLAN_CLIP[2] - PLAN_CLIP[0], PLAN_CLIP[3] - PLAN_CLIP[1],
                   P_COL["P4"], TRAIT))
        return head + defs + "\n".join(self.parts) + "\n</svg>\n"

    def overlaps(self):
        out = []
        L = self.labels
        for i in range(len(L)):
            for j in range(i + 1, len(L)):
                a, b = L[i], L[j]
                if a[0] < b[2] - 1 and b[0] < a[2] - 1 and a[1] < b[3] - 1 and b[1] < a[3] - 1:
                    out.append((a[4], b[4]))
        return out


def text_w(s, size, weight="normal"):
    # largeur approximative Arial
    w = 0.0
    for ch in s:
        if ch in "il.,:;|!'I()[]-/ ":
            w += 0.30
        elif ch.isupper() or ch in "mwMW@%":
            w += 0.68
        elif ch.isdigit():
            w += 0.556
        else:
            w += 0.52
    k = 1.06 if weight == "bold" else 1.0
    return w * size * k


def pts(lst):
    return " ".join("%.1f,%.1f" % p for p in lst)


def rect(s, r, fill, stroke, sw=1, dash=None, rx=0, extra=""):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    s.add('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%g" fill="%s" stroke="%s" '
          'stroke-width="%g"%s %s/>' % (r[0], r[1], r[2] - r[0], r[3] - r[1], rx, fill, stroke, sw, d, extra))


def line(s, p, color, sw=1, dash=None, extra=""):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    s.add('<polyline points="%s" fill="none" stroke="%s" stroke-width="%g"%s '
          'stroke-linejoin="round" stroke-linecap="round" %s/>' % (pts(p), color, sw, d, extra))


def chip(s, x, y, ph, w=26):
    """pastille de phase (centre x, centre y)."""
    s.add('<rect x="%.1f" y="%.1f" width="%d" height="15" rx="7.5" fill="%s"/>' % (x - w / 2, y - 7.5, w, P_COL[ph]))
    s.text(x, y + 4, ph, size=11, color="#FFFFFF", anchor="middle", weight="bold", halo=False, reg=False)


# ---------------------------------------------------------------- symboles
def sym_dm(s, x, y, k=1.0):
    a = 6 * k
    s.add('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s" stroke="#FFFFFF" stroke-width="1"/>'
          % (x - a, y - a, 2 * a, 2 * a, ROUGE))
    s.add('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="#FFFFFF"/>' % (x, y, 2.2 * k))


def sym_ds(s, x, y, k=1.0):
    a = 8 * k
    s.add('<polygon points="%s" fill="%s" stroke="#FFFFFF" stroke-width="1"/>'
          % (pts([(x, y - a), (x + a, y + a * 0.75), (x - a, y + a * 0.75)]), ROUGE))
    # cloche / flash stylise
    s.add('<path d="M%.1f %.1f q%.1f -%.1f %.1f 0 z" fill="#FFFFFF"/>' % (x - 3 * k, y + 3.5 * k, 3 * k, 6 * k, 6 * k))
    s.add('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="#FFFFFF"/>' % (x, y + 4.6 * k, 1.1 * k))


def sym_ct3(s, x, y, k=1.0):
    w, h = 34 * k, 16 * k
    s.add('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="2" fill="%s"/>' % (x - w / 2, y - h / 2, w, h, ROUGE))
    if k >= 0.9:
        s.text(x, y + 4, "CT3", size=11, color="#FFFFFF", anchor="middle", weight="bold", halo=False, reg=False)


def sym_cr(s, x, y, k=1.0):
    w, h = 28 * k, 16 * k
    s.add('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="2" fill="#FFFFFF" stroke="%s" stroke-width="2"/>'
          % (x - w / 2, y - h / 2, w, h, ROUGE))
    if k >= 0.9:
        s.text(x, y + 4, "CR", size=11, color=ROUGE, anchor="middle", weight="bold", halo=False, reg=False)


def sym_report(s, x, y, k=1.0):
    s.add('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="#FFFFFF" stroke="%s" stroke-width="1.6"/>' % (x, y, 7.5 * k, ROUGE))
    if k >= 0.9:
        s.text(x, y + 4, "R", size=11, color=ROUGE, anchor="middle", weight="bold", halo=False, reg=False)


def sym_rp(s, x, y, k=1.0, color=VIOLET):
    w, h = 26 * k, 18 * k
    s.add('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="2" fill="%s"/>' % (x - w / 2, y - h / 2, w, h, color))
    if k >= 0.9:
        s.text(x, y + 4, "RP", size=11, color="#FFFFFF", anchor="middle", weight="bold", halo=False, reg=False)


def sym_rs(s, x, y, k=1.0, color=VIOLET):
    w, h = 26 * k, 18 * k
    s.add('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="2" fill="#FFFFFF" stroke="%s" stroke-width="2"/>'
          % (x - w / 2, y - h / 2, w, h, color))
    if k >= 0.9:
        s.text(x, y + 4, "RS", size=11, color=color, anchor="middle", weight="bold", halo=False, reg=False)


def sym_switch(s, x, y, k=1.0, color=VIOLET):
    a = 10 * k
    s.add('<polygon points="%s" fill="%s" stroke="#FFFFFF" stroke-width="1.2"/>'
          % (pts([(x, y - a), (x + a, y), (x, y + a), (x - a, y)]), color))
    s.add('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="#FFFFFF"/>' % (x, y, 2.4 * k))


def sym_wifi(s, x, y, k=1.0, color=VIOLET):
    s.add('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s"/>' % (x, y + 3 * k, 1.8 * k, color))
    for r in (5, 9):
        r *= k
        s.add('<path d="M%.1f %.1f A%.1f %.1f 0 0 1 %.1f %.1f" fill="none" stroke="%s" stroke-width="%.1f" '
              'stroke-linecap="round"/>' % (x - r * 0.75, y + 3 * k - r * 0.66, r, r, x + r * 0.75, y + 3 * k - r * 0.66,
                                             color, 1.6 * k))


def sym_salle(s, x, y, k=1.0, color=BLEU, txt="SV"):
    w, h = 24 * k, 16 * k
    s.add('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="4" fill="#FFFFFF" stroke="%s" stroke-width="1.8"/>'
          % (x - w / 2, y - h / 2, w, h, color))
    if k >= 0.9:
        s.text(x, y + 4, txt, size=11, color=color, anchor="middle", weight="bold", halo=False, reg=False)


def sym_afficheur(s, x, y, k=1.0, color=BLEU):
    w, h = 24 * k, 14 * k
    s.add('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="1.5" fill="%s"/>' % (x - w / 2, y - h / 2, w, h, color))
    s.add('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="#FFFFFF" opacity="0.9"/>'
          % (x - w / 2 + 2.5 * k, y - h / 2 + 2.5 * k, w - 5 * k, h - 5 * k))
    s.add('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="%.1f"/>'
          % (x - w / 2 - 2 * k, y - h / 2, x + w / 2 + 2 * k, y - h / 2, ENCRE, 2 * k))  # fixation murale


def sym_totem(s, x, y, k=1.0, color=BLEU):
    w, h = 12 * k, 24 * k
    s.add('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="1.5" fill="%s"/>' % (x - w / 2, y - h / 2, w, h, color))
    s.add('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="#FFFFFF" opacity="0.9"/>'
          % (x - w / 2 + 2 * k, y - h / 2 + 2 * k, w - 4 * k, h * 0.55))
    s.add('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s"/>' % (x - w / 2 - 3 * k, y + h / 2 - 1, w + 6 * k, 3 * k, ENCRE))


def sym_box(s, x, y, txt, color=ENCRE, fill=None, w=None, k=1.0):
    w = (w or max(28, text_w(txt, 11, "bold") + 10)) * k
    h = 16 * k
    s.add('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="2" fill="%s" stroke="%s" stroke-width="1.6"/>'
          % (x - w / 2, y - h / 2, w, h, fill or "#FFFFFF", color))
    if k >= 0.9:
        s.text(x, y + 4, txt, size=11, color="#FFFFFF" if fill else color, anchor="middle", weight="bold",
               halo=False, reg=False)


def sym_pc(s, x, y, k=1.0, color=ENCRE):
    w, h = 22 * k, 14 * k
    s.add('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="1.5" fill="#FFFFFF" stroke="%s" stroke-width="1.8"/>'
          % (x - w / 2, y - h / 2 - 3 * k, w, h, color))
    s.add('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s"/>' % (x - 6 * k, y + h / 2 - 1 * k, 12 * k, 2.5 * k, color))


def sym_wago(s, x, y, k=1.0, color="#3FA7D6"):
    w, h = 30 * k, 16 * k
    s.add('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="2" fill="%s"/>' % (x - w / 2, y - h / 2, w, h, color))
    if k >= 0.9:
        s.text(x, y + 4, "API", size=11, color="#FFFFFF", anchor="middle", weight="bold", halo=False, reg=False)


def sym_camera(s, x, y, ang, k=1.0, cone=True, color=BLEU, r=62, half=24):
    a = math.radians(ang)
    if cone:
        p1 = (x + r * math.cos(a - math.radians(half)), y + r * math.sin(a - math.radians(half)))
        p2 = (x + r * math.cos(a + math.radians(half)), y + r * math.sin(a + math.radians(half)))
        s.add('<path d="M%.1f %.1f L%.1f %.1f A%d %d 0 0 1 %.1f %.1f Z" fill="%s" fill-opacity="0.24" '
              'stroke="%s" stroke-opacity="0.8" stroke-width="0.8"/>' % (x, y, p1[0], p1[1], r, r, p2[0], p2[1], CYAN, CYAN))
    # corps de camera oriente
    s.add('<g transform="translate(%.1f %.1f) rotate(%.1f) scale(%.2f)">'
          '<rect x="-7" y="-4.5" width="12" height="9" rx="1.5" fill="%s" stroke="#FFFFFF" stroke-width="1"/>'
          '<polygon points="5,-3 10,-5.5 10,5.5 5,3" fill="%s"/></g>' % (x, y, ang, k, color, color))
    s.add('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s"/>' % (x, y, 1.6 * k, ENCRE))


def sym_nvr(s, x, y, k=1.0):
    sym_box(s, x, y, "NVR", color=ENCRE, fill=ENCRE, w=34, k=k)


def sym_gate(s, x, y, ang=0, color=ROUGE):
    """portillon emergency access (arc de porte)."""
    s.add('<g transform="translate(%.1f %.1f) rotate(%.1f)"><line x1="-9" y1="0" x2="9" y2="0" stroke="%s" stroke-width="3"/>'
          '<path d="M-9 0 A9 9 0 0 1 0 9" fill="none" stroke="%s" stroke-width="1.2"/>'
          '<path d="M9 0 A9 9 0 0 0 0 9" fill="none" stroke="%s" stroke-width="1.2"/></g>' % (x, y, ang, color, color, color))


def sym_tripode(s, x, y, k=1.0):
    s.add('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="#FFFFFF" stroke="%s" stroke-width="1.6"/>' % (x, y, 7 * k, BLEU))
    for t in (90, 210, 330):
        a = math.radians(t)
        s.add('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1.4"/>'
              % (x, y, x + 5 * k * math.cos(a), y - 5 * k * math.sin(a), BLEU))


# ---------------------------------------------------------------- fond de plan commun
def base(s, mode="full"):
    """Dessine le fond de plan masse commun (calques groupes)."""
    s.open_g("fond", 'clip-path="url(#clipPlan)"')

    # --- calque parcelle DC11 (phase 4, ouest)
    s.open_g("calque-dc11")
    rect(s, DC11, "url(#hatchP4)", P_COL["P4"], sw=1.4, dash="8 5")
    rect(s, DC11_N, "#FFFFFF", P_COL["P4"], sw=1, dash="4 3")
    rect(s, DC11_S, "#FFFFFF", P_COL["P4"], sw=1, dash="4 3")
    s.text(120, 160, "PARCELLE DC11", size=12, color=P_COL["P4"], anchor="middle", weight="bold")
    s.text(120, 175, "(phase 4)", size=11, color=P_COL["P4"], anchor="middle")
    s.text(120, 206, "DC11 Nord", size=12, color=ENCRE, anchor="middle", weight="bold")
    s.text(120, 222, "Base vie P4", size=11, color=GRIS, anchor="middle")
    s.text(120, 236, "îlots 1 à 20", size=11, color=GRIS, anchor="middle")
    s.text(120, 250, "(implantation", size=11, color=GRIS, anchor="middle", italic=True)
    s.text(120, 264, "à confirmer)", size=11, color=GRIS, anchor="middle", italic=True)
    s.text(120, 880, "DC11 Sud", size=12, color=ENCRE, anchor="middle", weight="bold")
    s.text(120, 896, "OSM tente, déchets", size=11, color=GRIS, anchor="middle")
    s.text(120, 910, "IRVE DC11 (60)", size=11, color=GRIS, anchor="middle")
    s.text(120, 924, "(à confirmer)", size=11, color=GRIS, anchor="middle", italic=True)
    s.close_g()

    # --- calque voies
    s.open_g("calque-voies")
    # RD57 : parallele a la diagonale, a l'exterieur
    d = (410 / 608.8, 450 / 608.8)
    n = (450 / 608.8, -410 / 608.8)
    off = 46
    A = (690 + off * n[0] - 120 * d[0], 130 + off * n[1] - 120 * d[1])
    B = (1100 + off * n[0] + 700 * d[0], 580 + off * n[1] + 700 * d[1])
    line(s, [A, B], TRAIT, sw=22)
    line(s, [A, B], GRIS, sw=1, dash="14 10")
    # giratoire
    s.add('<circle cx="%d" cy="%d" r="26" fill="%s"/>' % (GIRATOIRE[0], GIRATOIRE[1], TRAIT))
    s.add('<circle cx="%d" cy="%d" r="11" fill="#FFFFFF" stroke="%s"/>' % (GIRATOIRE[0], GIRATOIRE[1], GRIS))
    # voie d'acces giratoire -> ouest, et voie interne ouest
    line(s, [(GIRATOIRE[0] - 24, 100), (222, 100), (222, 1000)], TRAIT, sw=14)
    s.add('<circle cx="222" cy="1004" r="16" fill="%s"/>' % TRAIT)
    s.text(800, 80, "RD57", size=13, color=GRIS, weight="bold", anchor="start")
    s.text(800, 95, "vers Les Bordes", size=11, color=GRIS)
    s.text(1112, 640, "RD57", size=12, color=GRIS, weight="bold", anchor="start", rotate=47.7, reg=False)
    s.text(1104, 676, "vers Fouju", size=11, color=GRIS, anchor="start", rotate=47.7, reg=False)
    s.text(GIRATOIRE[0] - 32, 90, "Giratoire", size=11, color=GRIS, anchor="end")
    s.text(212, 820, "Voie interne ouest", size=11, color=GRIS, anchor="middle", rotate=-90, reg=False)
    s.close_g()

    # --- calque emprise + cloture
    s.open_g("calque-emprise")
    s.add('<polygon points="%s" fill="%s" stroke="none"/>' % (pts(FENCE), ZONE))
    s.close_g()
    s.open_g("calque-cloture")
    s.add('<polygon points="%s" fill="none" stroke="%s" stroke-width="1.6" stroke-dasharray="10 3 2 3"/>'
          % (pts(FENCE), GRIS))
    s.close_g()

    # --- piste chantier autour du batiment
    s.open_g("calque-piste")
    rect(s, TRACK, "none", TRAIT, sw=12, rx=10)
    s.close_g()

    # --- batiment data center
    s.open_g("calque-batiment")
    rect(s, BUILDING, "#FFFFFF", GRIS, sw=2)
    x0, y0, x1, y1 = BUILDING
    for i in range(1, 5):
        xx = x0 + (x1 - x0) * i / 5
        s.add('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" stroke-width="1.2"/>' % (xx, y0 + 2, xx, y1 - 2, TRAIT))
    s.text((x0 + x1) / 2, 700, "BÂTIMENT DATA CENTER", size=15, color=GRIS, anchor="middle", weight="bold")
    s.text((x0 + x1) / 2, 718, "« Main Building » — 5 travées (POD1 à POD5, phase 4)", size=11, color=GRIS, anchor="middle")
    s.text((x0 + x1) / 2, 733, "chantier en cours — coffrets de chantier hors CFA", size=11, color=GRIS, anchor="middle",
           italic=True)
    s.close_g()

    # --- parking VL
    s.open_g("calque-parking")
    rect(s, PARKING, "#FFFFFF", GRIS, sw=1)
    px0, py0, px1, py1 = PARKING
    rows = [(py0 + 14, "53"), (py0 + 72, "26"), (py0 + 130, "34"), (py0 + 188, "30")]
    for yy, nb in rows:
        rect(s, (px0 + 8, yy, px1 - 8, yy + 30), "url(#hatchGray)", TRAIT, sw=1)
        s.text(px1 - 14, yy + 20, nb, size=11, color=GRIS, anchor="end")
    s.text((px0 + px1) / 2, py0 + 62, "PARKING VL", size=12, color=GRIS, anchor="middle", weight="bold")
    s.text((px0 + px1) / 2, py0 + 178, "IRVE P3 : 30 bornes", size=11, color=GRIS, anchor="middle")
    s.close_g()

    # --- base vie P2/P3
    s.open_g("calque-base-vie")
    rect(s, (458, 222, diag_x(222) - 6, BV_LIMIT_Y), "none", GRIS, sw=1, dash="3 3")
    line(s, [(458, BV_LIMIT_Y), (diag_x(BV_LIMIT_Y), BV_LIMIT_Y)], GRIS, sw=1.4)
    s.text(466, 434, "BASE VIE P2/P3 — îlots 1 à 10", size=11, color=ENCRE, weight="bold")
    for n_, (x, y, ph) in ISLANDS.items():
        rect(s, (x, y, x + ISL_W, y + ISL_H), "#FFFFFF", P_COL[ph], sw=1.8, rx=2)
        s.text(x + 10, y + 16, "Îlot %d" % n_, size=12, color=ENCRE, weight="bold", halo=False)
        chip(s, x + 23, y + 32, ph)
    # annexes base vie
    rect(s, FT2, "#FFFFFF", GRIS, sw=1.4)
    s.text((FT2[0] + FT2[2]) / 2, FT2[1] + 13, "Fire", size=11, color=GRIS, anchor="middle", halo=False)
    s.text((FT2[0] + FT2[2]) / 2, FT2[1] + 26, "Tank 2", size=11, color=GRIS, anchor="middle", halo=False)
    s.add('<polygon points="%s" fill="#FFFFFF" stroke="%s" stroke-width="1.4"/>'
          % (pts([(FT1[0], FT1[1] - 14), (FT1[0] + 14, FT1[1]), (FT1[0], FT1[1] + 14), (FT1[0] - 14, FT1[1])]), GRIS))
    s.text(FT1[0] + 18, FT1[1] + 4, "Fire Tank 1", size=11, color=GRIS)
    for r_, lab in ((HSE1, "HSE tente"), (HSE2, "HSE tente")):
        rect(s, r_, "#FFFFFF", GRIS, sw=1.4)
        s.text((r_[0] + r_[2]) / 2, (r_[1] + r_[3]) / 2 + 4, lab, size=11, color=GRIS, anchor="middle", halo=False)
    s.close_g()

    # --- zones chantier
    s.open_g("calque-zones")
    rect(s, WASTE, "#FFFFFF", GRIS, sw=1.2, dash="5 3")
    s.text((WASTE[0] + WASTE[2]) / 2, WASTE[1] + 34, "Waste Area", size=12, color=GRIS, anchor="middle", weight="bold")
    rect(s, LIVRAISON, "#FFFFFF", GRIS, sw=1, dash="2 3")
    s.text((LIVRAISON[0] + LIVRAISON[2]) / 2, LIVRAISON[1] + 19, "Aire de livraison", size=11, color=GRIS, anchor="middle")
    s.text((LIVRAISON[0] + LIVRAISON[2]) / 2, LIVRAISON[1] + 33, "(supposée, à confirmer)", size=11, color=GRIS,
           anchor="middle", italic=True)
    rect(s, STORAGE, "#FFFFFF", GRIS, sw=1.2, dash="5 3")
    s.text((STORAGE[0] + STORAGE[2]) / 2, STORAGE[1] + 80, "Storage Area", size=12, color=GRIS, anchor="middle",
           weight="bold")
    rect(s, BAT_TECH, "#FFFFFF", GRIS, sw=1.4)
    s.text((BAT_TECH[0] + BAT_TECH[2]) / 2, BAT_TECH[1] + 20, "Bât.", size=11, color=GRIS, anchor="middle", halo=False)
    s.text((BAT_TECH[0] + BAT_TECH[2]) / 2, BAT_TECH[1] + 34, "tech.", size=11, color=GRIS, anchor="middle", halo=False)
    s.close_g()

    # --- postes energie (Hubs A/B/C)
    s.open_g("calque-hubs")
    for r_, nm, ge in ((HUB1, "Hub 1 (poste A)", 2), (HUB2, "Hub 2 (poste B)", 2), (HUB3, "Hub 3 (poste C)", 1)):
        rect(s, r_, "#FFFFFF", ENCRE, sw=2)
        for g in range(ge):
            rect(s, (r_[2] + 3 + g * 11, r_[1] + 4, r_[2] + 12 + g * 11, r_[3] - 4), TRAIT, GRIS, sw=1)
    s.text(HUB1[0] - 2, HUB1[1] - 6, "Hub 1 (poste A) + GE", size=11, color=ENCRE, weight="bold")
    s.text(HUB2[2] + 58, HUB2[3] - 2, "Hub 2 (poste B) + GE", size=11, color=ENCRE, weight="bold")
    s.text(HUB3[0] - 2, HUB3[1] - 6, "Hub 3 (poste C)", size=11, color=ENCRE, weight="bold")
    s.close_g()

    # --- acces : poste de garde, tripodes, emergency access
    s.open_g("calque-acces")
    rect(s, PG, "#FFFFFF", ENCRE, sw=2)
    s.text(PG[0] - 6, PG[1] + 20, "Poste de garde", size=11, color=ENCRE, weight="bold", anchor="end")
    s.text(PG[0] - 6, PG[1] + 34, "principal", size=11, color=ENCRE, weight="bold", anchor="end")
    for t in TRIPODES_A + TRIPODES_B:
        sym_tripode(s, *t)
    s.text(TRIPODES_A[1][0] + 12, TRIPODES_A[1][1] + 4, "Tripodes ×2", size=11, color=BLEU)
    rect(s, ACCESS_CTRL, "#FFFFFF", GRIS, sw=1)
    s.text(ACCESS_CTRL[2] + 4, ACCESS_CTRL[3] + 2, "Access Control + tripodes ×2", size=11, color=BLEU)
    sym_gate(s, EA1[0], EA1[1], 0)
    sym_gate(s, EA2[0], EA2[1], 47.7)
    s.text(EA1[0], EA1[1] - 8, "Emergency access", size=11, color=ROUGE, anchor="middle")
    s.text(EA2[0] + 14, EA2[1] - 6, "Emergency access", size=11, color=ROUGE)
    # acces vehicules non localise
    s.add('<circle cx="600" cy="130" r="9" fill="#FFFFFF" stroke="%s" stroke-width="1.4" stroke-dasharray="3 2"/>' % GRIS)
    s.text(600, 134, "?", size=12, color=GRIS, anchor="middle", weight="bold", halo=False, reg=False)
    s.text(600, 118, "Accès véhicules / portail : à confirmer", size=11, color=GRIS, anchor="middle", italic=True)
    s.close_g()
    s.close_g()  # fond

    # --- habillage : nord, echelle
    s.open_g("calque-habillage")
    nx, ny = 1080, 112
    s.add('<circle cx="%d" cy="%d" r="22" fill="#FFFFFF" stroke="%s"/>' % (nx, ny, TRAIT))
    s.add('<polygon points="%s" fill="%s"/>' % (pts([(nx, ny - 18), (nx + 8, ny + 10), (nx, ny + 4), (nx - 8, ny + 10)]), ENCRE))
    s.text(nx, ny - 26, "N", size=13, color=ENCRE, anchor="middle", weight="bold")
    s.text(nx, ny + 38, "nord supposé", size=11, color=GRIS, anchor="middle", italic=True)
    s.text(nx, ny + 52, "(déduit des zones R.N/R.E/R.O)", size=11, color=GRIS, anchor="middle", italic=True)
    rect(s, (1004, 184, 1140, 218), "#FFFFFF", ENCRE, sw=1)
    s.text(1072, 198, "PLAN DE PRINCIPE", size=11, color=ENCRE, anchor="middle", weight="bold", halo=False)
    s.text(1072, 212, "NON À L'ÉCHELLE", size=11, color=ENCRE, anchor="middle", weight="bold", halo=False)
    s.text(1072, 234, "emprise ≈ 400 × 300-400 m", size=11, color=GRIS, anchor="middle")
    s.text(1072, 248, "(ordre de grandeur, non coté)", size=11, color=GRIS, anchor="middle")
    s.close_g()


# ---------------------------------------------------------------- habillage commun : titre, panneau, cartouche
def frame(s, lot, sous_titre):
    s.add('<rect x="0" y="0" width="%d" height="56" fill="#FFFFFF"/>' % W)
    s.add('<rect x="16" y="14" width="6" height="30" fill="%s"/>' % VIOLET)
    s.text(32, 30, "KHAZNA ORY01 — Base vie et chantier — %s" % lot, size=20, color=ENCRE, weight="bold", halo=False)
    s.text(32, 48, sous_titre, size=12, color=GRIS, halo=False)
    s.text(W - 16, 30, "PROSYB", size=20, color=VIOLET, anchor="end", weight="bold", halo=False)
    s.text(W - 16, 48, "Offre courants faibles — EXYTE / DCE FR02201", size=11, color=GRIS, anchor="end", halo=False)
    s.add('<line x1="16" y1="58" x2="%d" y2="58" stroke="%s" stroke-width="1"/>' % (W - 16, TRAIT))
    # cadre plan
    s.add('<rect x="%d" y="%d" width="%d" height="%d" fill="none" stroke="%s"/>'
          % (PLAN_CLIP[0], PLAN_CLIP[1], PLAN_CLIP[2] - PLAN_CLIP[0], PLAN_CLIP[3] - PLAN_CLIP[1], TRAIT))
    # panneau droit
    s.add('<rect x="%d" y="64" width="%d" height="%d" rx="6" fill="%s" stroke="%s"/>'
          % (PANEL_X, W - PANEL_X - 10, 1028 - 64, ZONE, TRAIT))


def cartouche(s, lot, x=PANEL_X, y=1036):
    w = W - x - 10
    h = H - y - 8
    s.add('<rect x="%d" y="%d" width="%d" height="%d" fill="#FFFFFF" stroke="%s" stroke-width="1.5"/>' % (x, y, w, h, ENCRE))
    s.add('<rect x="%d" y="%d" width="86" height="%d" fill="%s"/>' % (x, y, h, VIOLET))
    s.text(x + 43, y + 24, "PROSYB", size=14, color="#FFFFFF", anchor="middle", weight="bold", halo=False)
    s.text(x + 43, y + 44, "indice A", size=11, color="#FFFFFF", anchor="middle", halo=False)
    tx = x + 96
    s.text(tx, y + 17, "Plan d'implantation de principe — %s" % lot, size=12, color=ENCRE, weight="bold", halo=False)
    s.text(tx, y + 32, "KHAZNA ORY01, Fouju (77) — indice A — 10/2026", size=11, color=ENCRE, halo=False)
    s.text(tx, y + 47, "Non à l'échelle — à recaler sur le plan 1007", size=11, color=ROUGE, weight="bold", halo=False)


def phase_key(s, x=470, y=1018):
    s.text(x, y + 4, "Code phase :", size=11, color=GRIS, weight="bold")
    for i, (ph, lab) in enumerate((("P2", "phase 2 — T1 14/12/26"), ("P3", "phase 3 — T2 02/02/27"),
                                   ("P4", "phase 4 — T3 18/06/27"))):
        cx = x + 96 + i * 168
        chip(s, cx, y, ph)
        s.text(cx + 17, y + 4, lab, size=11, color=ENCRE)


def wrap(t, n):
    out, cur = [], ""
    for wd in t.split(" "):
        if len(cur) + len(wd) + 1 > n and cur:
            out.append(cur)
            cur = wd
        else:
            cur = (cur + " " + wd).strip()
    if cur:
        out.append(cur)
    return out


class Panel:
    """Remplissage sequentiel du panneau droit."""

    def __init__(self, s, y=86):
        self.s, self.x, self.y = s, PANEL_X + 14, y

    def title(self, t):
        self.y += 6
        self.s.text(self.x, self.y, t, size=13, color=VIOLET, weight="bold", halo=False)
        self.s.add('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s"/>' % (self.x, self.y + 5, W - 24, self.y + 5, TRAIT))
        self.y += 22

    def item(self, draw, label, sub=None, h=22):
        draw(self.s, self.x + 16, self.y - 4)
        self.s.text(self.x + 38, self.y, label, size=11, color=ENCRE, halo=False)
        if sub:
            self.y += 14
            self.s.text(self.x + 38, self.y, sub, size=11, color=GRIS, halo=False)
        self.y += h

    def para(self, t, n=74, color=ENCRE, bullet=True, size=11):
        lines = wrap(t, n)
        for i, ln in enumerate(lines):
            pre = "• " if (bullet and i == 0) else ("  " if bullet else "")
            self.s.text(self.x + (0 if (i == 0 or not bullet) else 8), self.y, (pre if i == 0 else "") + ln,
                        size=size, color=color, halo=False)
            self.y += 14
        self.y += 2

    def space(self, h):
        self.y += h


def write(s, name, title):
    path = os.path.join(OUT, name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(s.render(title))
    ov = s.overlaps()
    print("%-22s %4d libellés, %d chevauchements" % (name, len(s.labels), len(ov)))
    for a, b in ov:
        print("     !! %r  x  %r" % (a, b))


def lead(s, p1, p2, color=GRIS):
    s.add('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="0.8"/>' % (p1 + p2 + (color,)))


# ================================================================= PLAN SSI
DM = [  # repere, x, y, categorie, emplacement, (dx, dy, anchor) libelle
    ("DM-01", 552, 178, "accès", "Tripodes NO / poste de garde", (10, 14, "start")),
    ("DM-02", 690, 466, "accès", "Tripodes sud / Access Control", (10, 4, "start")),
    ("DM-03", 372, 142, "accès", "Emergency access NO", (-10, 4, "end")),
    ("DM-04", diag_x(226) - 16, 226, "accès", "Emergency access NE", (-10, 4, "end")),
    ("DM-05", 870, 572, "chantier", "Waste Area", (10, 4, "start")),
    ("DM-06", 870, 724, "chantier", "Storage Area", (10, 4, "start")),
    ("DM-07", 900, 418, "chantier", "HSE tente / Fire Tank 1", (10, 4, "start")),
    ("DM-08", 990, 900, "chantier", "Bâtiment technique SE", (-10, 4, "end")),
    ("DM-09", 450, 530, "bâtiment", "Façade nord", (0, 20, "middle")),
    ("DM-10", 690, 530, "bâtiment", "Façade nord", (0, 20, "middle")),
    ("DM-11", 800, 610, "bâtiment", "Façade est", (-10, 4, "end")),
    ("DM-12", 800, 830, "bâtiment", "Façade est", (-10, 4, "end")),
    ("DM-13", 430, 905, "bâtiment", "Façade sud", (0, -12, "middle")),
    ("DM-14", 740, 905, "bâtiment", "Façade sud", (0, -12, "middle")),
    ("DM-15", 330, 820, "bâtiment", "Façade ouest", (10, 4, "start")),
    ("DM-16", 330, 600, "bâtiment", "Façade ouest", (10, 4, "start")),
]
DS = [
    ("DS-01", ISLANDS[1][0] + 66, ISLANDS[1][1] + 34, "base vie", "Îlot 1 (sous auvent)", (6, 22, "end")),
    ("DS-02", ISLANDS[3][0] + 66, ISLANDS[3][1] + 34, "base vie", "Îlot 3", (6, 22, "end")),
    ("DS-03", ISLANDS[7][0] + 66, ISLANDS[7][1] + 34, "base vie", "Îlot 7", (6, 22, "end")),
    ("DS-04", ISLANDS[10][0] + 66, ISLANDS[10][1] + 34, "base vie", "Îlot 10", (6, 22, "end")),
    ("DS-05", 975, 572, "chantier", "Waste Area", (-12, 4, "end")),
    ("DS-06", 1025, 724, "chantier", "Storage Area", (-12, 4, "end")),
    ("DS-07", 888, 480, "chantier", "HSE tente 2", (-12, 4, "end")),
    ("DS-08", 1024, 880, "chantier", "Bâtiment technique", (12, -6, "start")),
    ("DS-09", 570, 530, "bâtiment", "Façade nord", (0, 22, "middle")),
    ("DS-10", 800, 720, "bâtiment", "Façade est", (-12, 4, "end")),
    ("DS-11", 560, 905, "bâtiment", "Façade sud", (0, -12, "middle")),
    ("DS-12", 330, 710, "bâtiment", "Façade ouest", (12, 4, "start")),
]


def plan_ssi():
    s = SVG()
    frame(s, "Implantation SSI (reports d'alarme incendie)",
          "Plan d'implantation de principe — lot SSI prioritaire — phases 2, 3 et réserve phase 4")
    base(s)
    s.open_g("calque-ssi")
    # ---- liaisons CR1-C1 (trace de principe le long des fourreaux)
    red_l = dict(color=ROUGE, sw=2.2)
    pgx = PG[0] + 22
    bus_y = 224
    # bus vers ilots : PG -> descente x=458 -> nappe y=bus_y -> descentes de colonnes
    line(s, [(pgx, PG[3]), (pgx, bus_y - 4), (458, bus_y - 4)], **red_l)
    line(s, [(458, bus_y - 4), (COLS[3] - 6, bus_y - 4)], ROUGE, sw=2.2)
    drops = {0: 460, 1: 548, 2: 636, 3: 724}
    for c, xx in drops.items():
        yy_end = ROWS[2] + 10 if c in (0, 1, 2, 3) else ROWS[2]
        if c == 3:
            line(s, [(xx, bus_y - 4), (xx, ROWS[2] + 10)], ROUGE, sw=1.6)
        else:
            line(s, [(xx, bus_y - 4), (xx, yy_end)], ROUGE, sw=1.6)
    # reports ilots (sur facade ouest de chaque ilot)
    for n_, (x, y, ph) in ISLANDS.items():
        col = COLS.index(x)
        rx = drops[col] if col > 0 else 460
        sym_report(s, x if col == 0 else rx, y + 10)
        if col == 3:
            pass
    s.text(470, bus_y - 10, "W-SSI-RD-Îlot n — CR1-C1 5G1,5", size=11, color=ROUGE, weight="bold")
    # Hub 1 : depuis le PG par la descente ouest, puis le long de la limite base vie
    line(s, [(pgx - 8, PG[3]), (pgx - 8, 478), (HUB1[2] + 26, 478)], **red_l)
    s.text(pgx - 14, 330, "W-SSI-RD-Hub Elec.1 — CR1-C1 7G1,5", size=11, color=ROUGE, weight="bold", anchor="middle",
           rotate=-90, reg=False)
    # Hub 2 : Hub 1 -> cloture ouest -> sud -> Hub 2
    line(s, [(HUB1[0], 482), (290, 482), (290, 947), (HUB2[0], 947)], **red_l)
    s.text(300, 965, "W-SSI-RD-Hub Elec.2 — CR1-C1 7G1,5", size=11, color=ROUGE, weight="bold")
    # Hub 3 (P4) : Hub 1 -> voie ouest -> DC11
    line(s, [(HUB1[0], 474), (236, 474), (236, HUB3_C[1]), (HUB3[2] + 14, HUB3_C[1])], ROUGE, sw=2.2, dash="7 4")
    line(s, [(150, HUB3[1] - 22), (150, DC11_N[3] - 12)], ROUGE, sw=1.6, dash="7 4")
    s.text(60, 510, "Reports îlots P4 1-20", size=11, color=ROUGE, weight="bold")
    s.text(60, 524, "(réserves coffret, P4)", size=11, color=ROUGE)
    s.text(52, 612 - 6, "", size=11, reg=False)
    s.text(120, HUB3[3] + 36, "W-SSI-RD-Hub 3 (P4)", size=11, color=ROUGE, weight="bold", anchor="middle")
    s.text(120, HUB3[3] + 50, "câble à définir", size=11, color=ROUGE, italic=True, anchor="middle")

    # ---- coffret reports + centrales
    sym_cr(s, PG[0] + 22, PG_C[1])
    sym_ct3(s, PG[0] + 60, PG_C[1])
    chip(s, PG[0] + 60, PG[3] + 12, "P2")
    sym_ct3(s, HUB1[0] + 26, HUB1_C[1])
    chip(s, HUB1[0] + 16, HUB1[3] + 11, "P2")
    sym_ct3(s, HUB2_C[0], HUB2_C[1])
    chip(s, HUB2[2] + 40, HUB2_C[1], "P2")
    sym_ct3(s, HUB3_C[0], HUB3_C[1])
    chip(s, HUB3[0] + 30, HUB3[3] + 16, "P4")

    # ---- DM / DS
    for rep, x, y, cat, lieu, (dx, dy, an) in DM:
        sym_dm(s, x, y)
        s.text(x + dx, y + dy, rep, size=11, color=ROUGE, weight="bold", anchor=an)
    for rep, x, y, cat, lieu, (dx, dy, an) in DS:
        sym_ds(s, x, y)
        s.text(x + dx, y + dy, rep, size=11, color=ROUGE, weight="bold", anchor=an)
    s.close_g()

    # ---- bas de plan : code phase
    phase_key(s)
    s.text(20, 82, "Liaisons : tracé de principe le long des fourreaux CFA (2 850 ml le long de la clôture)",
           size=11, color=GRIS, italic=True)

    # ---- panneau
    p = Panel(s)
    p.title("LÉGENDE SSI")
    p.item(lambda s_, x, y: sym_cr(s_, x, y), "CR — coffret des reports d'alarme SSI",
           "poste de garde principal (alim. ondulée TGBT Hub 1)")
    p.item(lambda s_, x, y: sym_ct3(s_, x, y), "CT3 — centrale type 3 AVISS CONCEPT 3",
           "PG, Hub 1, Hub 2 (P2) — Hub 3 (P4)")
    p.item(lambda s_, x, y: sym_report(s_, x, y), "R — report contact îlot (R / C / T)",
           "centrales îlots hors lot (T4 en P2-P3, T3 en P4)")
    p.item(lambda s_, x, y: sym_dm(s_, x, y), "DM-01…16 — déclencheur manuel étanche IP65",
           "4 accès · 4 zones chantier · 8 périphérie bâtiment")
    p.item(lambda s_, x, y: sym_ds(s_, x, y), "DS-01…12 — diffuseur sonore et lumineux",
           "chantier, sous abri : 4 base vie · 4 chantier · 4 bâtiment")
    p.item(lambda s_, x, y: line(s_, [(x - 12, y), (x + 12, y)], ROUGE, sw=2.2), "Liaison CR1-C1 (W-SSI-RD-…)",
           "5G1,5 îlots — 7G1,5 Hubs et poste de garde")
    p.item(lambda s_, x, y: line(s_, [(x - 12, y), (x + 12, y)], ROUGE, sw=2.2, dash="7 4"),
           "Liaison phase 4 (Hub 3, îlots DC11)", "sur réserves « Phase 4 » du coffret")
    p.item(lambda s_, x, y: sym_gate(s_, x, y), "Emergency access (portillon)")
    p.item(lambda s_, x, y: sym_tripode(s_, x, y), "Tripode d'accès piétons")
    p.space(2)
    p.title("QUANTITÉS IMPLANTÉES")
    for t in ("Coffret de reports : 1 (PG) — 10 îlots + PG + Hub 1 + Hub 2, réserves P4",
              "Centrales type 3 : 4 (PG, Hub 1, Hub 2 en P2 ; Hub 3 en P4)",
              "Déclencheurs manuels : 16 — diffuseurs : 12 (P2, maintenus P3-P4)",
              "Raccordement DM/DS chantier : sur la CT3 la plus proche (à valider)"):
        p.para(t)
    p.space(2)
    p.title("LIAISONS (synoptique 1016)")
    for t in ("W-SSI-RD-Îlot 1 à 10 : CR1-C1 5G1,5 (R / C / T) — P2 : îlots 1-2, P3 : îlots 3-10",
              "W-SSI-RD-Hub Elec.1 / Hub Elec.2 / P.d.Garde : CR1-C1 7G1,5",
              "W-SSI-ALIM-COFFRET REPORT : CR1-C1 3G1,5 depuis départ ondulé TGBT Hub 1"):
        p.para(t, n=64)
    p.space(2)
    p.title("REPÉRAGE DM / DS (proposition PROSYB)")
    y0 = p.y
    for i, (rep, x, y, cat, lieu, _) in enumerate(DM):
        s.text(p.x, y0 + 14 * i, rep, size=11, color=ROUGE, weight="bold", halo=False)
        s.text(p.x + 42, y0 + 14 * i, lieu, size=11, color=ENCRE, halo=False)
    for i, (rep, x, y, cat, lieu, _) in enumerate(DS):
        s.text(p.x + 206, y0 + 14 * i, rep, size=11, color=ROUGE, weight="bold", halo=False)
        s.text(p.x + 246, y0 + 14 * i, lieu, size=11, color=ENCRE, halo=False)
    p.y = y0 + 14 * len(DM) + 6
    p.title("HYPOTHÈSES À VALIDER")
    for t in ("Nord supposé en haut (pas de flèche du nord au DCE).",
              "Position du poste de garde et des accès véhicules / aire de livraison non cotées : à confirmer.",
              "Implantation DM/DS = proposition PROSYB, à valider avec EXYTE et le coordinateur SSI.",
              "Câble noté « CR1-CR » au 1016, lu CR1-C1. Liaisons Hub 2 et Hub 3 à confirmer (absentes des "
              "lignes DPGF P2 / du 1016).",
              "Base vie P4 (DC11) : implantation des îlots 1 à 20 inconnue."):
        p.para(t)
    cartouche(s, "SSI")
    write(s, "plan_ssi.svg", "Plan SSI ORY01")


# ================================================================= PLAN IT
def plan_it():
    s = SVG()
    frame(s, "Implantation IT / VDI / Wi-Fi", "Plan d'implantation de principe — répartiteurs, anneau fibre OS2, Wi-Fi, salles")
    base(s)
    s.open_g("calque-it")
    # anneau fibre
    line(s, RING_PATH, VIOLET, sw=3)
    # Hub1 -> Hub3 (P4)
    line(s, [(HUB1[0], 470), (240, 470), (240, HUB3_C[1] - 6), (HUB3[2], HUB3_C[1] - 6)], P_COL["P4"], sw=3, dash="8 4")
    # Hub3 -> RS A / B
    line(s, [(HUB3_C[0] - 12, HUB3[1]), (HUB3_C[0] - 12, 470), (88, 470), (88, 440)], P_COL["P4"], sw=2.2, dash="8 4")
    line(s, [(HUB3_C[0] - 12, 470), (154, 470), (154, 440)], P_COL["P4"], sw=2.2, dash="8 4")
    # PG spur (cuivre/fibre vers repartiteur PG)
    line(s, [(PG_C[0] + 16, RING_N), (PG_C[0] + 16, PG[1])], VIOLET, sw=2)
    # base vie : liaisons cuivre depuis repartiteur principal Hub 1 (P2/P3)
    line(s, [(HUB1[2] + 24, 470), (458, 470), (458, BV_LIMIT_Y)], VIOLET, sw=1.6, dash="2 3")
    s.text(390, 462, "", size=11, reg=False)

    # repartiteurs principaux
    for c, nm, ph, lab_pos in ((HUB1_C, "Hub 1", "P2", None), (HUB2_C, "Hub 2", "P2", None), (HUB3_C, "Hub 3", "P4", None)):
        sym_rp(s, c[0] - 6, c[1])
    chip(s, HUB1[0] + 16, HUB1[3] + 11, "P2")
    chip(s, HUB2[2] + 40, HUB2_C[1], "P2")
    chip(s, HUB3[0] + 30, HUB3[3] + 16, "P4")
    # secondaires (sur anneau)
    sec = [("R.O.1", "Ouest 1", (16, 4, "start"), "P2"), ("R.N", "Nord", (16, 4, "start"), "P2"),
           ("R.E.1", "Est 1", (16, 4, "start"), "P2"), ("R.E.2", "Est 2", (-16, -4, "end"), "P2"),
           ("R.E.3", "Est 3", (-18, -14, "end"), "P2"), ("R.O.2", "Ouest 2", (16, 4, "start"), "P2")]
    for key, nm, (dx, dy, an), ph in sec:
        x, y = COF[key]
        sym_rs(s, x, y)
        s.text(x + dx, y + dy, "Rép. %s (%s)" % (nm, key), size=11, color=VIOLET, weight="bold", anchor=an)
    # repartiteur poste de garde
    sym_rs(s, PG_C[0] + 16, PG_C[1])
    # annexes x2 (P3) a confirmer
    sym_rs(s, BAT_TECH[0] - 18, (BAT_TECH[1] + BAT_TECH[3]) / 2, color=BLEU)
    s.text(BAT_TECH[0] - 36, BAT_TECH[1] + 10, "Rép. annexe 1", size=11, color=BLEU, weight="bold", anchor="end")
    s.text(BAT_TECH[0] - 36, BAT_TECH[1] + 24, "(P3, à confirmer)", size=11, color=BLEU, anchor="end")
    sym_rs(s, HSE2[0] - 18, (HSE2[1] + HSE2[3]) / 2, color=BLEU)
    s.text((HSE2[0] + HSE2[2]) / 2 - 10, HSE2[3] + 14, "Rép. annexe 2", size=11, color=BLEU, weight="bold", anchor="middle")
    s.text((HSE2[0] + HSE2[2]) / 2 - 10, HSE2[3] + 28, "(P3, à confirmer)", size=11, color=BLEU, anchor="middle")
    # base vie P4 A / B
    sym_rs(s, 88, 430, color=P_COL["P4"])
    sym_rs(s, 154, 430, color=P_COL["P4"])
    s.text(88, 410, "Rép. A", size=11, color=P_COL["P4"], weight="bold", anchor="middle")
    s.text(154, 410, "Rép. B", size=11, color=P_COL["P4"], weight="bold", anchor="middle")
    s.text(120, 290, "A : îlots 1 à 10", size=11, color=ENCRE, anchor="middle")
    s.text(120, 304, "B : îlots 11 à 20", size=11, color=ENCRE, anchor="middle")
    s.text(120, 322, "18 RJ45 / îlot = 360", size=11, color=ENCRE, anchor="middle")
    sym_wifi(s, 70, 345)
    s.text(84, 350, "60 bornes (pose)", size=11, color=VIOLET, weight="bold")
    s.text(120, 380, "salles : à confirmer", size=11, color=GRIS, anchor="middle", italic=True)

    # Wi-Fi par ilot + salles de reunion (indicatif)
    wifi_n = {1: 2, 2: 2, 3: 3, 4: 3, 5: 3, 6: 3, 7: 2, 8: 2, 9: 2, 10: 2}
    salles = {1: ["SR-01"], 2: ["SR-02", "SR-03"], 3: ["SR-04"], 4: ["SR-05"], 5: ["SR-06"], 6: ["SR-07"],
              7: ["SR-08"], 8: ["SR-09"], 9: ["SR-10"]}
    for n_, (x, y, ph) in ISLANDS.items():
        sym_wifi(s, x + 48, y + 31, color=VIOLET)
        s.text(x + 58, y + 37, "×%d" % wifi_n[n_], size=11, color=VIOLET, weight="bold", halo=False)
        if n_ in salles:
            sym_salle(s, x + ISL_W - 10, y + 10, k=0.7, color=BLEU)
            s.text(x + ISL_W / 2, y + ISL_H + 12, " / ".join(salles[n_]), size=11, color=BLEU, weight="bold",
                   anchor="middle")
    # repere des liaisons
    s.text(400, RING_S - 7, "Anneau fibre OS2 12 brins autocicatrisant — fourreaux CFA le long de la clôture",
           size=11, color=VIOLET, weight="bold")
    s.text(466, 462, "RJ45 Cat6A depuis Hub 1 (P2-P3)", size=11, color=VIOLET)
    s.close_g()

    phase_key(s)
    s.text(20, 82, "Le 1014 montre 2 anneaux (terrain / informatique-Wi-Fi) ; la DPGF n'en chiffre qu'un — à arbitrer",
           size=11, color=GRIS, italic=True)

    p = Panel(s)
    p.title("LÉGENDE IT / VDI")
    p.item(lambda s_, x, y: sym_rp(s_, x, y), "RP — répartiteur principal + switch PoE",
           "local CFA climatisé des Hubs 1, 2 (P2) et 3 (P4)")
    p.item(lambda s_, x, y: sym_rs(s_, x, y), "RS — répartiteur secondaire + switch PoE",
           "Est 1-3, Ouest 1-2 (P2), Nord (1014), poste de garde")
    p.item(lambda s_, x, y: sym_rs(s_, x, y, color=BLEU), "RS annexes ×2 (P3) — positions à confirmer")
    p.item(lambda s_, x, y: sym_rs(s_, x, y, color=P_COL["P4"]), "RS base vie A / B (P4, parcelle DC11)")
    p.item(lambda s_, x, y: line(s_, [(x - 12, y), (x + 12, y)], VIOLET, sw=3), "Anneau fibre OS2 12 brins",
           "le long de la clôture, via les répartiteurs")
    p.item(lambda s_, x, y: line(s_, [(x - 12, y), (x + 12, y)], P_COL["P4"], sw=3, dash="8 4"),
           "Fibre OS2 phase 4 (Hub 1 → Hub 3 → A / B)")
    p.item(lambda s_, x, y: line(s_, [(x - 12, y), (x + 12, y)], VIOLET, sw=1.6, dash="2 3"),
           "RJ45 Cat6A F/STP (prises îlots, depuis Hub 1)")
    p.item(lambda s_, x, y: sym_wifi(s_, x, y), "Borne Wi-Fi (×n = nombre par îlot, indicatif)")
    p.item(lambda s_, x, y: sym_salle(s_, x, y, k=0.8, txt=""), "SR — salle de réunion (emplacement à confirmer)")
    p.space(2)
    p.title("QUANTITÉS PAR PHASE (DPGF)")
    for t in ("P2 (îlots 1-2) : 24 RJ45, 4 bornes Wi-Fi (pose seule), 3 salles",
              "P3 (îlots 3-10) : 96 RJ45 + 30 liaisons techniques, 20 bornes (fourniture et pose), 7 salles",
              "P4 (DC11, îlots 1-20) : 360 RJ45, 60 bornes (pose seule)",
              "Total : 480 prises, 84 bornes, 10 salles"):
        p.para(t)
    p.title("HYPOTHÈSES À VALIDER")
    for t in ("Répartition des bornes par îlot et des salles = indicative.",
              "Fourniture des bornes P2 et P4 par EXYTE : à confirmer.",
              "Répartiteur Nord et Poste de garde : au 1014, hors DPGF.",
              "Boucle DPGF « Ouest 3 » lue comme Est 3.",
              "Annexes ×2 : bâtiments à désigner par EXYTE."):
        p.para(t)
    cartouche(s, "IT / VDI")
    write(s, "plan_it.svg", "Plan IT ORY01")


# ================================================================= PLAN VIDEO
# repere, x, y, direction (deg, 0 = est, 90 = sud), (dx, dy, anchor) libelle
CAMS = {
    "R.O.1": [((262, 142), 50, (10, 16, "start")), ((320, 142), 15, (0, -10, "middle")),
              ((590, 142), 160, (8, 12, "start")), ((672, 142), -40, (4, 16, "middle"))],
    "R.N": [((700, 150), 115, (14, 4, "start")), ((ring_diag(250)[0] - 6, 250), 160, (10, -8, "start")),
            ((452, 300), 10, (-8, 4, "end")), ((452, 438), -15, (-8, 4, "end")),
            ((ring_diag(BV_LIMIT_Y)[0] - 30, 438), 195, (0, -10, "middle")), ((ring_diag(390)[0] - 6, 390), 228, (12, 4, "start"))],
    "R.E.1": [((ring_diag(445)[0] - 6, 445), 48, (12, 4, "start")), ((ring_diag(560)[0] - 4, 560), 225, (12, 6, "start")),
              ((830, 524), 15, (-8, -8, "end"))],
    "R.E.2": [((RING_E, 610), 100, (-10, -6, "end")), ((RING_E, 800), 262, (-10, 4, "end")),
              ((1052, 870), 220, (12, 4, "start"))],
    "R.E.3": [((RING_E, RING_S), 225, (0, 0, "none")), ((980, RING_S), 285, (0, 18, "middle")),
              ((870, RING_S), 0, (0, 18, "middle")), ((775, RING_S), 300, (0, 18, "middle"))],
    "R.H.2": [((690, RING_S), 285, (0, 18, "middle")), ((545, RING_S), 200, (0, 18, "middle")),
              ((440, RING_S), 300, (0, 18, "middle"))],
    "R.O.2": [((RING_W + 4, RING_S), -40, (10, 18, "start"))],
    "R.H.1": [((RING_W + 4, 560), 40, (10, -6, "start")), ((RING_W + 4, 720), 0, (10, -8, "start")),
              ((RING_W + 4, 870), -35, (10, 16, "start")), ((300, 440), 270, (-8, 4, "end"))],
}


def plan_video():
    s = SVG()
    frame(s, "Implantation vidéosurveillance", "Plan d'implantation de principe — 28 caméras sur mâts, coffrets de zone, NVR, supervision (phase 3)")
    base(s)
    s.open_g("calque-video")
    line(s, RING_PATH, VIOLET, sw=2.6)
    coff = dict(COF)
    coff["R.H.1"] = (HUB1_C[0] - 8, HUB1_C[1])
    coff["R.H.2"] = HUB2_C
    for z, cams in CAMS.items():
        for i, ((x, y), ang, lab) in enumerate(cams, 1):
            sym_camera(s, x, y, ang)
    for z, cams in CAMS.items():
        for i, ((x, y), ang, (dx, dy, an)) in enumerate(cams, 1):
            if an == "none":
                s.text(x - 8, y - 18, "%s-%d" % (z, i), size=11, color=ENCRE, weight="bold", anchor="end")
                continue
            s.text(x + dx, y + dy, "%s-%d" % (z, i), size=11, color=ENCRE, weight="bold", anchor=an)
    # coffrets de zone
    zlab = {"R.O.1": (16, 4, "start"), "R.N": (16, -8, "start"), "R.E.1": (14, -10, "start"),
            "R.E.2": (-14, -24, "end"), "R.E.3": (-16, -12, "end"), "R.O.2": (14, -12, "start")}
    nb = {z: len(c) for z, c in CAMS.items()}
    for z, (x, y) in COF.items():
        sym_switch(s, x, y)
        dx, dy, an = zlab[z]
        s.text(x + dx, y + dy, "%s (%d cam.)" % (z, nb[z]), size=11, color=VIOLET, weight="bold", anchor=an)
    # Hub 1 : switch R.H.1 + NVR ; Hub 2 : switch R.H.2
    sym_switch(s, HUB1[0] + 14, HUB1_C[1])
    sym_nvr(s, HUB1[0] + 44, HUB1_C[1], k=0.95)
    s.text(HUB1[0] - 6, HUB1[3] + 30, "R.H.1 (4) + NVR", size=11, color=VIOLET, weight="bold", anchor="start")
    sym_switch(s, HUB2[0] + 14, HUB2_C[1])
    s.text(HUB2[0] - 8, HUB2[1] - 6, "R.H.2 (3 cam.)", size=11, color=VIOLET, weight="bold", anchor="end")
    # supervision PG
    sym_pc(s, PG_C[0] + 14, PG_C[1] + 2)
    s.text(PG[0], PG[3] + 14, "PC supervision", size=11, color=ENCRE, weight="bold", anchor="start")
    line(s, [(PG_C[0] + 30, RING_N), (PG_C[0] + 30, PG[1])], VIOLET, sw=2)
    s.close_g()
    phase_key(s)
    s.text(20, 82, "Toutes les caméras en phase 3 (DPGF §6) — 28 massifs de mât (lot GC)", size=11, color=GRIS, italic=True)

    p = Panel(s)
    p.title("LÉGENDE VIDÉOSURVEILLANCE")
    p.item(lambda s_, x, y: sym_camera(s_, x - 6, y, 0, r=26, half=24), "Caméra fixe sur mât + cône de vision",
           "HIKVISION 2560×1440, 2,8-12 mm — repère CAM <zone>-n")
    p.item(lambda s_, x, y: sym_switch(s_, x, y), "Coffret de zone (switch PoE, R-DIN fibre, alim.)",
           "R.O.1, R.N, R.E.1-3, R.O.2 ; R.H.1 / R.H.2 dans les Hubs")
    p.item(lambda s_, x, y: sym_nvr(s_, x, y, k=0.8), "NVR — local CFA Hub 1 (15 j ≈ 18-22 To)")
    p.item(lambda s_, x, y: sym_pc(s_, x, y), "PC de supervision — poste de garde")
    p.item(lambda s_, x, y: line(s_, [(x - 12, y), (x + 12, y)], VIOLET, sw=2.6), "Anneau fibre OS2 12 fo armé",
           "Hub 1 → R.O.1 → R.N → R.E.1-3 → R.H.2 → R.O.2 → Hub 1")
    p.para("Caméras raccordées en cuivre F/UTP Cat6 extérieur PoE au coffret de leur zone (non tracé).")
    p.space(2)
    p.title("RÉPARTITION (1009 / 1015)")
    rows = [("R.O.1", 4, "angle NO, parking, giratoire, tripodes"), ("R.N", 6, "base vie, clôture N / NE"),
            ("R.E.1", 3, "clôture NE / RD57 haute"), ("R.E.2", 3, "clôture E / RD57, Storage"),
            ("R.E.3", 4, "angle SE, moitié est clôture sud"), ("R.H.2", 3, "clôture sud centrale (Hub 2)"),
            ("R.O.2", 1, "angle SO"), ("R.H.1", 4, "clôture ouest (Hub 1), parking")]
    for z, n_, t in rows:
        s.text(p.x, p.y, z, size=11, color=VIOLET, weight="bold", halo=False)
        s.text(p.x + 50, p.y, "%d" % n_, size=11, color=ENCRE, weight="bold", halo=False)
        s.text(p.x + 68, p.y, t, size=11, color=ENCRE, halo=False)
        p.y += 15
    s.text(p.x, p.y, "Total", size=11, color=ENCRE, weight="bold", halo=False)
    s.text(p.x + 50, p.y, "28", size=11, color=ENCRE, weight="bold", halo=False)
    p.y += 20
    p.title("HYPOTHÈSES À VALIDER")
    for t in ("Positions de mâts et orientations : de principe, d'après le plan de couverture du 1009.",
              "Caméra R.O.2 libellée « CAM R.E.3-1 » au 1015 : renommée R.O.2-1.",
              "Alimentation : 1015 (3G2,5 depuis Hub 1) ou DPGF (TD Périphérie) à arbitrer.",
              "Intrusion par analyse vidéo ; barrières IR non chiffrées (BPU « à définir »)."):
        p.para(t)
    cartouche(s, "Vidéosurveillance")
    write(s, "plan_video.svg", "Plan vidéo ORY01")


# ================================================================= PLAN AV / AFFICHAGE
def plan_av():
    s = SVG()
    frame(s, "Implantation audiovisuel et affichage", "Plan d'implantation de principe — 6 afficheurs chantier (P3) et 10 salles visio (3 P2, 7 P3)")
    base(s)
    s.open_g("calque-av")
    # afficheurs muraux sur modules base vie
    af = [("AF-01", ISLANDS[4][0], ISLANDS[4][1] + 22, "façade côté parking", (-16, 4, "end"), 90),
          ("AF-02", ISLANDS[1][0] + 38, ISLANDS[1][1], "côté tripodes NO", (18, -8, "start"), 0),
          ("AF-03", ISLANDS[10][0] + 58, ISLANDS[10][1] + ISL_H, "côté accès sud", (16, 14, "start"), 0)]
    for rep, x, y, lieu, (dx, dy, an), rot in af:
        if rot:
            s.add('<g transform="rotate(-90 %.1f %.1f)">' % (x - 2, y))
            sym_afficheur(s, x - 2, y)
            s.add("</g>")
        else:
            sym_afficheur(s, x, y - 2 if y < 300 else y + 2)
        s.text(x + dx, y + dy, rep, size=11, color=BLEU, weight="bold", anchor=an)
    # totems
    tt = [("TT-01", PG_C[0] - 10, PG[3] + 22, "entrée poste de garde NO", (0, 0, "none")),
          ("TT-02", ACCESS_CTRL[0] + 20, ACCESS_CTRL[3] + 26, "tripodes / Access Control sud", (14, 4, "start")),
          ("TT-03", LIVRAISON[2] + 16, (LIVRAISON[1] + LIVRAISON[3]) / 2, "aire de livraison", (0, 0, "none"))]
    for rep, x, y, lieu, (dx, dy, an), in tt:
        sym_totem(s, x, y)
    s.text(PG_C[0] + 2, PG[3] + 26, "TT-01", size=11, color=BLEU, weight="bold")
    s.text(ACCESS_CTRL[0] + 34, ACCESS_CTRL[3] + 30, "TT-02", size=11, color=BLEU, weight="bold")
    s.text(LIVRAISON[2] + 28, LIVRAISON[1] + 10, "TT-03", size=11, color=BLEU, weight="bold")
    s.text(LIVRAISON[2] + 28, LIVRAISON[1] + 24, "position", size=11, color=GRIS, italic=True)
    s.text(LIVRAISON[2] + 28, LIVRAISON[1] + 38, "à confirmer", size=11, color=GRIS, italic=True)
    # salles visio dans les ilots
    sv = {1: ["SV-01"], 2: ["SV-02", "SV-03"], 3: ["SV-04"], 4: ["SV-05"], 5: ["SV-06"], 6: ["SV-07"],
          7: ["SV-08"], 8: ["SV-09"], 9: ["SV-10"]}
    for n_, reps in sv.items():
        x, y, ph = ISLANDS[n_]
        sym_salle(s, x + ISL_W - 12, y + 10, k=0.75, color=P_COL[ph])
        s.text(x + 4, y + 40, "", size=11, reg=False)
    # libelles salles en dessous de chaque rangee
    for n_, reps in sv.items():
        x, y, ph = ISLANDS[n_]
        s.text(x + ISL_W / 2, y + ISL_H + 13, " / ".join(reps), size=11, color=P_COL[ph], weight="bold",
               anchor="middle")
    # serveur de diffusion (proposition MEM)
    sym_box(s, HUB1[0] + 26, HUB1_C[1], "SRV", color=BLEU, fill=BLEU, w=32)
    s.text(HUB1[0] - 4, HUB1[3] + 30, "Serveur de diffusion (proposition)", size=11, color=BLEU, weight="bold")
    s.close_g()
    phase_key(s)
    s.text(20, 82, "Afficheurs en phase 3 (DPGF 4.1) — 3 afficheurs secourus sur l'ondulé du TGBT Hub 1",
           size=11, color=GRIS, italic=True)

    p = Panel(s)
    p.title("LÉGENDE AUDIOVISUEL / AFFICHAGE")
    p.item(lambda s_, x, y: sym_afficheur(s_, x, y), "AF — afficheur mural sur bras",
           "sous auvent / coursive des modules base vie")
    p.item(lambda s_, x, y: sym_totem(s_, x, y), "TT — totem d'affichage couvert", "entrées et aire de livraison")
    p.item(lambda s_, x, y: sym_salle(s_, x, y, k=0.8, color=P_COL["P2"]), "SV — salle visio (P2)",
           "écran 85\", barre caméra/enceinte, 5 micros")
    p.item(lambda s_, x, y: sym_salle(s_, x, y, k=0.8, color=P_COL["P3"]), "SV — salle visio (P3)")
    p.item(lambda s_, x, y: sym_box(s_, x, y, "SRV", color=BLEU, fill=BLEU, w=32), "Serveur de diffusion — baie Hub 1",
           "proposition PROSYB (VLAN 50)")
    p.space(2)
    p.title("REPÉRAGE")
    for t in ("AF-01 : îlot 4, façade côté parking",
              "AF-02 : îlot 1, façade côté tripodes NO",
              "AF-03 : îlot 10, façade côté accès sud",
              "TT-01 : entrée poste de garde NO",
              "TT-02 : tripodes / Access Control sud base vie",
              "TT-03 : aire de livraison — position à confirmer",
              "SV-01 à SV-03 : îlots 1-2 (P2) ; SV-04 à SV-10 : îlots 3-9 (P3)"):
        p.para(t, bullet=True)
    p.title("HYPOTHÈSES À VALIDER")
    for t in ("Aucun plan DCE ne localise les 6 afficheurs : répartition 3 / 2 / 1 = proposition PROSYB.",
              "Aire de livraison et accès véhicules non localisés au DCE (supposés près du Storage).",
              "Salles visio : emplacements non donnés ; supposées dans les salles de briefing des îlots.",
              "Affectation îlot / salle indicative, à arrêter avec EXYTE."):
        p.para(t)
    cartouche(s, "AV / affichage")
    write(s, "plan_av.svg", "Plan AV ORY01")


# ================================================================= PLAN GTB
def plan_gtb():
    s = SVG()
    frame(s, "Implantation GTB / GTC", "Plan d'implantation de principe — automates WAGO dans les TGBT, supervision au poste de garde")
    base(s)
    s.open_g("calque-gtb")
    TER = "#3FA7D6"
    line(s, RING_PATH, VIOLET, sw=2.4, dash="10 4")
    line(s, [(HUB1[0], 470), (240, 470), (240, HUB3_C[1] - 6), (HUB3[2], HUB3_C[1] - 6)], P_COL["P4"], sw=2.4, dash="8 4")
    line(s, [(PG_C[0] + 16, RING_N), (PG_C[0] + 16, PG[1])], VIOLET, sw=2)
    sym_wago(s, HUB1[0] + 26, HUB1_C[1])
    sym_wago(s, HUB2_C[0], HUB2_C[1])
    sym_wago(s, HUB3_C[0], HUB3_C[1])
    chip(s, HUB1[0] + 16, HUB1[3] + 11, "P2")
    chip(s, HUB2[2] + 40, HUB2_C[1], "P2")
    chip(s, HUB3[0] + 30, HUB3[3] + 16, "P4")
    sym_pc(s, PG_C[0] - 14, PG_C[1] + 2)
    sym_pc(s, PG_C[0] + 12, PG_C[1] + 2)
    s.text(PG[0], PG[3] + 14, "Supervision GTB (2 écrans)", size=11, color=ENCRE, weight="bold")

    # bulles d'information
    def bubble(x, y, w, lines, anchor_pt):
        h = 16 + 14 * len(lines)
        rect(s, (x, y, x + w, y + h), "#FFFFFF", TER, sw=1.4, rx=4)
        lead(s, anchor_pt, (x if anchor_pt[0] < x else (x + w if anchor_pt[0] > x + w else anchor_pt[0]),
                            y if anchor_pt[1] < y else y + h), TER)
        for i, (t, b) in enumerate(lines):
            s.text(x + 8, y + 16 + 14 * i, t, size=11, color=ENCRE if not b else TER, weight="bold" if b else "normal",
                   halo=False)

    bubble(345, 560, 250, [("TGBT Hub 1 — WAGO + RS485", True), ("2 compteurs Modbus (TR1 / GE1)", False),
                           ("22 entrées TOR (dont 15 défauts SD)", False), ("COM GE1 + onduleur 1", False)],
           (HUB1[0] + 26, HUB1[3]))
    bubble(560, 790, 230, [("TGBT Hub 2 — WAGO + RS485", True), ("2 compteurs (TR2 / GE2)", False),
                           ("21 TOR (dont 14 SD)", False), ("COM GE2 + onduleur 2", False)], (HUB2_C[0], HUB2[1]))
    bubble(46, 700, 150, [("TGBT Hub 3 (P4)", True), ("WAGO + RS485", False), ("2 compteurs", False),
                          ("15 TOR (8 SD)", False), ("COM GE3 + ond. 3", False)], (HUB3_C[0], HUB3[3]))
    s.text(400, RING_S - 7, "Réseau terrain « switch lot Elec » — anneau fibre OS2, Modbus TCP/IP (port X1 WAGO)",
           size=11, color=VIOLET, weight="bold")
    s.close_g()
    phase_key(s)
    s.text(20, 82, "Les TD divisionnaires ne sont pas câblés à la GTB (1017) : seuls les 3 TGBT", size=11, color=GRIS,
           italic=True)

    p = Panel(s)
    p.title("LÉGENDE GTB / GTC")
    p.item(lambda s_, x, y: sym_wago(s_, x, y), "API — automate WAGO I/O System",
           "RS485 + 2 × 16 entrées TOR, alim. 230 VAC/24 VDC")
    p.item(lambda s_, x, y: sym_pc(s_, x, y), "Poste de supervision (PC fixe, 2 écrans)",
           "poste de garde — historisation, alertes SMS / mail")
    p.item(lambda s_, x, y: line(s_, [(x - 12, y), (x + 12, y)], VIOLET, sw=2.4, dash="10 4"),
           "Réseau terrain (port X1 WAGO → switch Hub)", "via anneau fibre OS2 commun")
    p.item(lambda s_, x, y: line(s_, [(x - 12, y), (x + 12, y)], P_COL["P4"], sw=2.4, dash="8 4"),
           "Liaison phase 4 Hub 1 → Hub 3")
    p.space(2)
    p.title("POINTS REMONTÉS PAR TGBT (1017)")
    for t in ("Défaut transformateur, défaut parafoudre, position inverseur (2), présence tension normale / "
              "secourue / ondulée",
              "Défauts départs SD : 15 (Hub 1), 14 (Hub 2), 8 (Hub 3)",
              "Comptage : 2 compteurs Modbus RS485 (arrivée TR et GE)",
              "Communication : groupe électrogène et onduleur de chaque Hub"):
        p.para(t)
    p.title("ENTRÉES TOR PAR TGBT (1017)")
    tor = [("Entrée TOR", "Hub 1", "Hub 2", "Hub 3"), ("Défaut TRn", "1", "1", "1"), ("Défaut parafoudre", "1", "1", "1"),
           ("Position inverseur de sources", "2", "2", "2"), ("Présence tension normale", "1", "1", "1"),
           ("Présence tension secourue", "1", "1", "1"), ("Présence tension ondulée", "1", "1", "1"),
           ("Défauts départs (SD)", "15", "14", "8"), ("Total", "22", "21", "15")]
    for i, row in enumerate(tor):
        b_ = i in (0, len(tor) - 1)
        if i == 0:
            s.add('<rect x="%d" y="%d" width="%d" height="18" fill="#FFFFFF"/>' % (p.x - 4, p.y - 13, W - 24 - p.x + 4))
        s.text(p.x, p.y, row[0], size=11, color=ENCRE, weight="bold" if b_ else "normal", halo=False)
        for j, v in enumerate(row[1:]):
            s.text(p.x + 248 + j * 50, p.y, v, size=11, color=VIOLET if b_ else ENCRE, weight="bold" if b_ else "normal",
                   anchor="middle", halo=False)
        p.y += 16
    p.y += 6
    p.title("HYPOTHÈSES À VALIDER")
    for t in ("Automates dans le local MT/BT, sur le jeu de barres ondulé.",
              "Réseau terrain sur l'anneau fibre commun (1014 : 2 anneaux).",
              "Poste de supervision : partage du poste de garde avec SSI et vidéo, à confirmer."):
        p.para(t)
    cartouche(s, "GTB / GTC")
    write(s, "plan_gtb.svg", "Plan GTB ORY01")


# ================================================================= SYNTHESE
def plan_synthese():
    s = SVG()
    frame(s, "Synthèse tous lots", "Plan d'implantation de principe — SSI, IT, vidéo, AV/affichage, GTB (symboles réduits)")
    base(s)
    s.open_g("calque-synthese")
    line(s, RING_PATH, VIOLET, sw=2.4)
    line(s, [(HUB1[0], 470), (240, 470), (240, HUB3_C[1] - 6), (HUB3[2], HUB3_C[1] - 6)], P_COL["P4"], sw=2.4, dash="8 4")
    # video (sans cones)
    for z, cams in CAMS.items():
        for (x, y), ang, lab in cams:
            sym_camera(s, x, y, ang, k=0.85, cone=False)
    for z, (x, y) in COF.items():
        sym_switch(s, x, y, k=0.8)
        s.text(x + (12 if x < 1000 else -12), y - 10, z, size=11, color=VIOLET, weight="bold",
               anchor="start" if x < 1000 else "end")
    # SSI
    for rep, x, y, *_ in DM:
        sym_dm(s, x, y, k=0.8)
    for rep, x, y, *_ in DS:
        sym_ds(s, x, y, k=0.8)
    for n_, (x, y, ph) in ISLANDS.items():
        sym_report(s, x, y + 10, k=0.7)
        sym_wifi(s, x + 48, y + 32, k=0.8)
    # hubs : CT3 + RP + API
    for c, ph in ((HUB1_C, "P2"), (HUB2_C, "P2"), (HUB3_C, "P4")):
        sym_ct3(s, c[0] - 16, c[1] - 1, k=0.55)
        sym_rp(s, c[0] + 2, c[1], k=0.55)
        sym_wago(s, c[0] + 19, c[1], k=0.5)
    # PG : CR + CT3 + PC
    sym_cr(s, PG[0] + 16, PG_C[1], k=0.8)
    sym_ct3(s, PG[0] + 44, PG_C[1], k=0.6)
    sym_pc(s, PG[0] + 68, PG_C[1] + 2, k=0.8)
    # AV
    sym_afficheur(s, ISLANDS[4][0] - 10, ISLANDS[4][1] + 22, k=0.8)
    sym_afficheur(s, ISLANDS[1][0] + 38, ISLANDS[1][1] - 2, k=0.8)
    sym_afficheur(s, ISLANDS[10][0] + 58, ISLANDS[10][1] + ISL_H + 3, k=0.8)
    sym_totem(s, PG_C[0] - 10, PG[3] + 22, k=0.8)
    sym_totem(s, ACCESS_CTRL[0] + 20, ACCESS_CTRL[3] + 26, k=0.8)
    sym_totem(s, LIVRAISON[2] + 16, (LIVRAISON[1] + LIVRAISON[3]) / 2, k=0.8)
    s.close_g()
    phase_key(s)
    s.text(20, 82, "Détail et repérage : voir plans par lot (SSI, IT, vidéo, AV, GTB) — indice A", size=11, color=GRIS,
           italic=True)

    p = Panel(s)
    p.title("LÉGENDE (SYMBOLES RÉDUITS)")
    p.item(lambda s_, x, y: sym_cr(s_, x, y), "SSI — coffret de reports (PG)")
    p.item(lambda s_, x, y: sym_ct3(s_, x, y), "SSI — centrale type 3 (×4)")
    p.item(lambda s_, x, y: sym_dm(s_, x, y), "SSI — déclencheur manuel (×16)")
    p.item(lambda s_, x, y: sym_ds(s_, x, y), "SSI — diffuseur sonore et lumineux (×12)")
    p.item(lambda s_, x, y: sym_report(s_, x, y), "SSI — report îlot (×10, P4 : 20 en réserve)")
    p.item(lambda s_, x, y: sym_rp(s_, x, y), "IT — répartiteur principal (Hubs 1-3)")
    p.item(lambda s_, x, y: sym_switch(s_, x, y), "IT / vidéo — coffret de zone, répartiteur secondaire")
    p.item(lambda s_, x, y: sym_wifi(s_, x, y), "IT — Wi-Fi (P2 : 4, P3 : 20, P4 : 60)")
    p.item(lambda s_, x, y: line(s_, [(x - 12, y), (x + 12, y)], VIOLET, sw=2.4), "Anneau fibre OS2 (clôture)")
    p.item(lambda s_, x, y: sym_camera(s_, x - 4, y, 0, cone=False), "Vidéo — caméra sur mât (×28, P3)")
    p.item(lambda s_, x, y: sym_afficheur(s_, x, y), "AV — afficheur mural (×3)")
    p.item(lambda s_, x, y: sym_totem(s_, x, y), "AV — totem (×3, dont livraison à confirmer)")
    p.item(lambda s_, x, y: sym_wago(s_, x, y), "GTB — automate WAGO (TGBT Hubs 1-3)")
    p.item(lambda s_, x, y: sym_pc(s_, x, y), "Supervision (vidéo, GTB) — poste de garde")
    p.para("Dans chaque Hub, de gauche à droite : centrale CT3 (rouge), répartiteur principal RP (violet), "
           "automate WAGO (bleu) ; NVR et serveur de diffusion au Hub 1. Poste de garde : CR, CT3, PC supervision.")
    p.space(2)
    p.title("HYPOTHÈSES À VALIDER")
    for t in ("Nord supposé en haut ; plan non coté, à recaler sur le plan 1007 (DWG).",
              "Accès véhicules, portail et aire de livraison non localisés au DCE.",
              "Base vie P4 (DC11) : implantation des îlots 1 à 20 inconnue.",
              "Salles visio, Wi-Fi, afficheurs, DM/DS : positions proposées par PROSYB."):
        p.para(t)
    cartouche(s, "synthèse tous lots")
    write(s, "plan_synthese.svg", "Synthèse ORY01")


if __name__ == "__main__":
    plan_ssi()
    plan_it()
    plan_video()
    plan_av()
    plan_gtb()
    plan_synthese()
