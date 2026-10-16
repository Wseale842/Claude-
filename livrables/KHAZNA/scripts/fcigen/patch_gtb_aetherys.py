"""Patch the KHAZNA FCI (PROSYB template, xlsx) with the AETHERYS GTB offer of 16/10/2026.

Edits sheet4.xml (DPGF) in place so the template's drawings/styles are preserved.
Usage: python3 patch_gtb_aetherys.py <in.xlsx> <out.xlsx>
"""
import html, re, sys, zipfile

SRC, OUT = sys.argv[1], sys.argv[2]
AE = "AETHERYS DPGF GTB du 16/10/2026"
# row: (constructeur, référence, description, PRU MAT, h monteur, h technicien, h BE)
GTB = {
    106: ("AETHERYS / WAGO", "750-8112",
          f"MO : pose et raccordement en TGBT par PROSYB 3 h ; configuration AETHERYS | {AE} : contrôleur PFC100 750-8112 949 € "
          "+ 2 × entrées TOR 16 voies 750-1405 273 € + borne finale 750-600 26 € par TGBT", 1248.00, 0, 3, 0),
    107: ("AETHERYS / WAGO", "787-1212", f"MO : pose 0,5 h | {AE} : alimentation à découpage 24 V 2,5 A 787-1212", 78.00, 0, 0.5, 0),
    108: ("", "", "MO : cordon / liaison Cat. 6A vers switch terrain (PROSYB) | ", 30.00, 1, 0, 0),
    109: ("", "", "MO : ≈ 20 contacts SD/TOR par TGBT × 0,25 h + contrôle ; fils et borniers 80 € (liste de points AETHERYS : 22 TOR Hub 1, "
          "21 Hub 2, 15 Hub 3) | ", 80.00, 5, 1, 0),
    110: ("", "", "MO : bus RS485 vers centrales de mesure ≈ 30 m + raccordement ; connecteur RS485 750-960 cité au mémoire AETHERYS "
          "mais non chiffré (à confirmer) | ", 40.00, 2, 1, 0),
    111: ("AETHERYS / HP", "ProDesk 4 SFF G1i",
          f"MO : assistance PROSYB 0,5 h (fourniture et installation AETHERYS) | {AE} : HP ProDesk 4 SFF G1i (9H7K4ET) + clavier/souris "
          "1 430 € + 2 écrans iiyama 23,8\" G2441HSU-B1 234 €", 1664.00, 0, 0.5, 0),
    112: ("AETHERYS / Inductive Automation", "Ignition Edge",
          "MO : coordination, essais avec les lots, recette PROSYB 8 h + BE 4 h | "
          f"{AE} (sous-traitance) : dossier technique d'exécution 3 240 € + paramétrage 810 € + développement GTB 6 480 € + mise en "
          "service et essais 4 j 3 240 € + DOE 405 € + formation 405 € + licence Ignition Edge IGN-EDGE-PANEL-83 (basic CARE 24 mois) "
          "3 413,80 € + routeur IXON 5G avec antenne extérieure 902,20 € + abonnement 5G 24 mois 936 € + TMA à distance 24 mois "
          "3 240 € = 23 072 € ; + provision ESTIMATIVE 870 € pour porter TMA et 5G à 29 mois de chantier (5 × 39 € + 5 × 135 €). "
          "Alertes SMS : passerelle non décrite par AETHERYS (à confirmer).", 23942.00, 0, 8, 4),
}
TITLE = (105, "GTB / GTE (offre AETHERYS du 16/10/2026)")
NOTA_OLD = "lot GTB provisoire dans l'attente de l'offre Aetherys."
NOTA_NEW = "lot GTB selon offre AETHERYS du 16/10/2026 (TMA et 5G prolongées à 29 mois par provision)."


def esc(t):
    return html.escape(str(t), quote=False)


def set_cell(row_xml, ref, style_default, value):
    """Replace cell `ref` in row_xml keeping its style; strings inline, numbers as <v>."""
    m = re.search(r'<c r="%s"( s="(\d+)")?[^>]*?(/>|>.*?</c>)' % ref, row_xml, re.S)
    style = m.group(2) if m and m.group(2) else style_default
    if value in (None, "", 0):
        new = '<c r="%s" s="%s"/>' % (ref, style)
    elif isinstance(value, (int, float)):
        new = '<c r="%s" s="%s"><v>%s</v></c>' % (ref, style, value)
    else:
        new = '<c r="%s" s="%s" t="inlineStr"><is><t xml:space="preserve">%s</t></is></c>' % (ref, style, esc(value))
    return row_xml.replace(m.group(0), new) if m else row_xml


zin = zipfile.ZipFile(SRC)
s = zin.read("xl/worksheets/sheet4.xml").decode("utf-8")
for r, (cons, ref, desc, pru, hm, ht, hb) in GTB.items():
    m = re.search(r'<row r="%d" .*?</row>' % r, s, re.S)
    row = m.group(0)
    for col, st, val in (("E", "458", cons), ("F", "503", ref), ("G", "503", desc), ("J", "444", pru),
                         ("L", "445", hm), ("N", "506", ht), ("P", "507", hb)):
        row = set_cell(row, "%s%d" % (col, r), st, val)
    s = s.replace(m.group(0), row)
r, t = TITLE
s = re.sub(r'(<c r="B%d" s="563" t="inlineStr"><is><t xml:space="preserve">).*?(  —  TVA 20 %%</t>)' % r,
           lambda m: m.group(1) + esc(t) + m.group(2), s, flags=re.S)
s = s.replace(esc(NOTA_OLD), esc(NOTA_NEW))
with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
    for item in zin.infolist():
        z.writestr(item, s.encode("utf-8") if item.filename == "xl/worksheets/sheet4.xml" else zin.read(item.filename))
print("ok", OUT)
