import base64, pathlib, sys
from playwright.sync_api import sync_playwright
B = pathlib.Path(sys.argv[1]); out = sys.argv[2]; ver = sys.argv[3] if len(sys.argv) > 3 else "v1.2"
logo = base64.b64encode((B/"logo-prosyb.png").read_bytes()).decode()
header = f"""<div style="width:100%;margin:0 18mm;font-family:Arial;font-size:7.5pt;color:#6E6A86;display:flex;justify-content:space-between;align-items:center;border-bottom:.3mm solid #E4E1F0;padding-bottom:2mm;-webkit-print-color-adjust:exact">
<img src="data:image/png;base64,{logo}" style="height:8mm"><span>Mémoire technique · KHAZNA ORY01 · Base vie &amp; chantier · Courants faibles · {ver}</span></div>"""
footer = """<div style="width:100%;margin:0 18mm;font-family:Arial;font-size:7pt;color:#6E6A86;display:flex;justify-content:space-between;border-top:.3mm solid #E4E1F0;padding-top:1.5mm">
<span>PROSYB · SIREN 941 519 092</span><span>Confidentiel · réservé à l'usage exclusif de EXYTE</span><span>p. <span class="pageNumber"></span> / <span class="totalPages"></span></span></div>"""
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/opt/pw-browsers/chromium-1194/chrome-linux/chrome", args=["--no-sandbox"])
    pg = b.new_page()
    pg.goto((B/"memoire.html").resolve().as_uri(), wait_until="networkidle")
    pg.pdf(path=out+".a.pdf", format="A4", print_background=True, prefer_css_page_size=True,
           display_header_footer=True, header_template=header, footer_template=footer)
    pg.pdf(path=out+".b.pdf", format="A4", print_background=True, prefer_css_page_size=True)
    b.close()
from pypdf import PdfReader, PdfWriter
a, bb = PdfReader(out+".a.pdf"), PdfReader(out+".b.pdf")
assert len(a.pages) == len(bb.pages), (len(a.pages), len(bb.pages))
w = PdfWriter(); w.add_page(bb.pages[0])
for pgx in a.pages[1:]: w.add_page(pgx)
w.add_metadata({"/Title": "Mémoire technique PROSYB — KHAZNA ORY01 — Courants faibles base vie et chantier " + ver, "/Author": "PROSYB"})
w.write(out); pathlib.Path(out+".a.pdf").unlink(); pathlib.Path(out+".b.pdf").unlink()
print("ok", out, len(a.pages), "pages")
