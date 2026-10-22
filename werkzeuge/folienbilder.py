"""Schaubilder aus einem Foliensatz (PDF) ausschneiden und maskierte Varianten erzeugen.

Die Bildliste steht in einer YAML-Datei je Kapitel (z. B. bwl/quellen/kap1-2_bilder.yaml):

    fach: bwl
    dpi: 300            # Auflösung beim Rendern (alle Koordinaten beziehen sich darauf)
    max_breite: 1600    # fertige PNGs werden höchstens so breit
    bilder:
      - name: kap1_bezugsrahmen       # Dateiname ohne .png
        folie: 11
        ausschnitt: [290, 515, 3190, 2270]          # x0, y0, x1, y1 – oder eine Liste
                                                    # solcher Rechtecke (werden untereinander gesetzt)
        masken:                                     # optional: je Maske ein weiteres PNG
          beschaffungsmarkt: [372, 1000, 502, 1680] # -> kap1_bezugsrahmen-ohne-beschaffungsmarkt.png
          personal: [[700, 840, 960, 940], [1105, 840, 1490, 940]]  # mehrere Rechtecke = ein Feld

Aufruf (aus dem Repo-Wurzelordner):

    python3 werkzeuge/folienbilder.py bwl/quellen/kap1-2_bilder.yaml --skript /pfad/zum/skript.pdf

Das Skript-PDF bleibt außerhalb dieses öffentlichen Repos (es liegt im privaten Repo „studium“).
Koordinaten findet man z. B. mit `pdftotext -bbox-layout` (pt × dpi/72) oder per Tesseract-TSV.
"""
import argparse
import os
import subprocess
import sys
import tempfile

import yaml
from PIL import Image, ImageDraw, ImageFont

WURZEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MASKE_FUELLUNG = "#f5a623"  # Orange aus stil.py
MASKE_RAND = "#000000"
SCHRIFT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def rendere_folie(pdf, folie, dpi, ordner):
    ziel = os.path.join(ordner, f"f{folie:03d}")
    pfad = ziel + ".png"
    if not os.path.exists(pfad):
        subprocess.run(
            ["pdftoppm", "-r", str(dpi), "-png", "-singlefile", "-f", str(folie), "-l", str(folie), pdf, ziel],
            check=True,
        )
    return Image.open(pfad).convert("RGB")


def als_rechtecke(wert):
    """[x0,y0,x1,y1] oder [[...], [...]] -> Liste von Rechtecken."""
    if isinstance(wert[0], (int, float)):
        return [list(wert)]
    return [list(r) for r in wert]


def schrift(groesse):
    try:
        return ImageFont.truetype(SCHRIFT, groesse)
    except OSError:
        return ImageFont.load_default()


def maskiere(bild, rechtecke):
    bild = bild.copy()
    zeichnen = ImageDraw.Draw(bild)
    for x0, y0, x1, y1 in rechtecke:
        zeichnen.rectangle([x0, y0, x1, y1], fill=MASKE_FUELLUNG, outline=MASKE_RAND, width=5)
        groesse = int(max(28, min(140, (y1 - y0) * 0.75, (x1 - x0) * 0.75)))
        f = schrift(groesse)
        bx0, by0, bx1, by1 = zeichnen.textbbox((0, 0), "?", font=f)
        zeichnen.text(
            ((x0 + x1) / 2 - (bx1 - bx0) / 2 - bx0, (y0 + y1) / 2 - (by1 - by0) / 2 - by0),
            "?", fill="#000000", font=f,
        )
    return bild


def baue(seite, ausschnitte, masken_rechtecke=None):
    """Schneidet die Ausschnitte aus, maskiert (in Seitenkoordinaten) und setzt sie untereinander."""
    if masken_rechtecke:
        seite = maskiere(seite, masken_rechtecke)
    teile = [seite.crop(tuple(r)) for r in ausschnitte]
    if len(teile) == 1:
        return teile[0]
    luecke = 24
    breite = max(t.width for t in teile)
    hoehe = sum(t.height for t in teile) + luecke * (len(teile) - 1)
    gesamt = Image.new("RGB", (breite, hoehe), "white")
    y = 0
    for t in teile:
        gesamt.paste(t, (0, y))
        y += t.height + luecke
    return gesamt


def speichere(bild, pfad, max_breite):
    if bild.width > max_breite:
        h = round(bild.height * max_breite / bild.width)
        bild = bild.resize((max_breite, h), Image.LANCZOS)
    bild.save(pfad, optimize=True)
    return pfad


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("spec")
    ap.add_argument("--skript", required=True, help="Pfad zum Skript-PDF (nicht im Repo)")
    ap.add_argument("--nur", help="nur dieses Bild (name) erzeugen")
    args = ap.parse_args()

    spec = yaml.safe_load(open(args.spec, encoding="utf-8"))
    dpi = spec.get("dpi", 300)
    max_breite = spec.get("max_breite", 1600)
    ziel_ordner = os.path.join(WURZEL, spec["fach"], "bilder")
    os.makedirs(ziel_ordner, exist_ok=True)

    erzeugt = []
    with tempfile.TemporaryDirectory() as tmp:
        for b in spec["bilder"]:
            if args.nur and b["name"] != args.nur:
                continue
            seite = rendere_folie(args.skript, b["folie"], dpi, tmp)
            ausschnitte = als_rechtecke(b["ausschnitt"])
            erzeugt.append(speichere(baue(seite, ausschnitte), os.path.join(ziel_ordner, b["name"] + ".png"), max_breite))
            for feld, rechtecke in (b.get("masken") or {}).items():
                pfad = os.path.join(ziel_ordner, f"{b['name']}-ohne-{feld}.png")
                erzeugt.append(speichere(baue(seite, ausschnitte, als_rechtecke(rechtecke)), pfad, max_breite))
    for p in erzeugt:
        print(os.path.relpath(p, WURZEL))
    print(f"{len(erzeugt)} Bilder erzeugt.", file=sys.stderr)


if __name__ == "__main__":
    main()
