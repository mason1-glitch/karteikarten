"""Karteikarten aus einer YAML-Quelle bauen und prüfen (StudyCards-CSV).

Quelle je Kapitel, z. B. bwl/quellen/kap1-2_karten.yaml:

    fach: bwl
    csv: bwl/karten/kap1-2_einleitung-grundlagen.csv
    matrix: bwl/quellen/kap1-2_abdeckung.md
    titel: BWL Kapitel 1–2
    ausgelassen:   [{folien: "1–5", grund: "Organisatorisches"}]
    inhalte:       [{id: f27.wirtschaften, folie: 27, text: "Definition Wirtschaften"}]
    wiederholungsfragen: [{id: W01, folie: 22, frage: "Was ist wirtschaften?", braucht: [f27.wirtschaften]}]
    karten:
      - typ: definition            # siehe TYPEN
        folien: [27]
        deckt: [f27.wirtschaften]  # Inhalte aus der Liste oben
        w: W01                     # nur bei Musterantworten zu Wiederholungsfragen
        frage: |-
          Definiere **Wirtschaften**.
        antwort: |-
          „Wirtschaften ist …“      # „…“ = Wortlaut des Skripts (wird geprüft)
        rechnung: [...]            # optional, wird nachgerechnet (siehe RECHNER)

Bilder: {{bild:<datei ohne .png>|Beschreibung}} wird zum Raw-Link auf <fach>/bilder/.
Code: ```sprache … ```-Blöcke werden zu farbigen Bildern (werkzeuge/codebilder.py).
Die Folienangabe (*F. …*) hängt das Werkzeug an jede Antwort an.

Aufrufe (aus dem Repo-Wurzelordner):
    python3 werkzeuge/karten.py bauen   bwl/quellen/kap1-2_karten.yaml
    python3 werkzeuge/karten.py pruefen bwl/quellen/kap1-2_karten.yaml --skript skript.pdf [--urls] [--bericht datei.md]
    python3 werkzeuge/karten.py liste   bwl/quellen/kap1-2_karten.yaml > karten.md   (Übersicht zum Gegenlesen)

`bauen` prüft Aufbau, Abdeckung, LaTeX-Reste und Rechnungen und schreibt CSV + Abdeckungsmatrix.
`pruefen` vergleicht zusätzlich jedes „Zitat“ per difflib mit dem Folientext (pdftotext, bei
Bildfolien Tesseract-OCR) und testet mit --urls, ob alle Bild-Links erreichbar sind.
"""
import argparse
import collections
import csv
import difflib
import io
import os
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.request

import yaml

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from codebilder import code_einsetzen  # Code-Blöcke → farbige Bilder (werkzeuge/codebilder.py)

WURZEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO_RAW = "https://raw.githubusercontent.com/mason1-glitch/karteikarten/main"

TYPEN = {
    "definition": "Definition (Begriff → Wortlaut)",
    "rueckwaerts": "Definition rückwärts (Wortlaut → Begriff)",
    "formel": "Formel/Kennzahl",
    "aufzaehlung": "Aufzählung vollständig",
    "luecke": "Aufzählung zerlegt (Lückenkarte)",
    "fakt": "Einzelfakt",
    "verwechslung": "Verwechslungskarte",
    "falle": "Klausurfalle",
    "anwendung": "Anwendung (Fall → Einordnung)",
    "rechnen": "Rechenkarte",
    "skizze": "Skizze zeichnen",
    "maske": "Schaubild mit verdecktem Feld",
    "unstimmigkeit": "Unstimmigkeit im Skript",
    "klausurfrage": "Musterantwort Wiederholungsfrage",
}

LATEX_MUSTER = [r"\$", r"\\frac", r"\\cdot", r"\\times", r"\\text", r"\\\(", r"\\\[", r"\^\{", r"_\{",
                r"\\le\b", r"\\ge\b", r"\\approx", r"\\sum", r"\\varnothing", r"\\emptyset"]


# ---------------------------------------------------------------- Laden und Aufbereiten

def lade(pfad):
    with open(pfad, encoding="utf-8") as f:
        q = yaml.safe_load(f)
    for i, k in enumerate(q["karten"], 1):
        k["id"] = f"K{i:03d}"
    return q


def folien_text(folien):
    f = sorted(set(folien))
    if len(f) == 1:
        return f"F. {f[0]}"
    if f == list(range(f[0], f[-1] + 1)) and len(f) > 2:
        return f"F. {f[0]}–{f[-1]}"
    return "F. " + ", ".join(str(x) for x in f)


def bilder_einsetzen(text, fach):
    def ersetze(m):
        name, _, alt = m.group(1).partition("|")
        return f"![{alt or name}]({REPO_RAW}/{fach}/bilder/{name}.png)"
    return re.sub(r"\{\{bild:([^}]+)\}\}", ersetze, text)


def felder(q, k):
    frage = code_einsetzen(bilder_einsetzen(k["frage"].strip(), q["fach"]), q["fach"])
    antwort = code_einsetzen(bilder_einsetzen(k["antwort"].strip(), q["fach"]), q["fach"])
    antwort += f"\n\n*{folien_text(k['folien'])}*"
    return frage, antwort


def bildnamen(text):
    return re.findall(r"\{\{bild:([^}|]+)", text)


# ---------------------------------------------------------------- Rechner (unabhängige Nachrechnung)

def zahl(s):
    """Erste Zahl im deutschen Format aus einem Text (1.234,5 → 1234.5; −0,3 → -0.3)."""
    m = re.search(r"[−-]?\d[\d.]*(?:,\d+)?", s)
    if not m:
        raise ValueError(f"keine Zahl in {s!r}")
    t = m.group(0).replace("−", "-").replace(".", "").replace(",", ".")
    return float(t)


def nachkommastellen(s):
    m = re.search(r"\d[\d.]*(?:,(\d+))?", s)
    return len(m.group(1)) if m and m.group(1) else 0


def kmu_klasse(b, u, bs):
    """EU-Abgrenzung F. 41: Beschäftigte UND (Umsatz ODER Bilanzsumme); Rest = groß."""
    if b < 10 and (u <= 2 or bs <= 2):
        return "Kleinstunternehmen"
    if b <= 49 and (u <= 10 or bs <= 10):
        return "kleines Unternehmen"
    if b <= 249 and (u <= 50 or bs <= 43):
        return "mittleres Unternehmen"
    return "Großunternehmen"


def mitbestimmung(b, montan=False, rechtsform="AG"):
    """F. 46 (Kapitalgesellschaften/eG)."""
    if montan and b >= 1000 and rechtsform != "eG":
        return "volle Parität"
    if b > 2000:
        return "Unterparität"
    if 500 < b < 2000:
        return "Drittelparität"
    return "keine"


RECHNER = {
    "effizienz": lambda r: r["erfolg"] / r["aufwand"],
    "produktivitaet": lambda r: r["output"] / r["input"],
    "wirtschaftlichkeit": lambda r: r["ertrag"] / r["aufwand"],
    "gewinn": lambda r: r["erloese"] - r["kosten"],
    "rentabilitaet": lambda r: 100 * r["gewinn"] / (
        r["kapital"] if "kapital" in r else (r["kapital_anfang"] + r["kapital_ende"]) / 2),
    "prozentpunkte": lambda r: r["neu"] - r["alt"],
    "aenderung_prozent": lambda r: 100 * (r["neu"] - r["alt"]) / r["alt"],
    "kmu": lambda r: kmu_klasse(r["beschaeftigte"], r["umsatz"], r["bilanzsumme"]),
    "mitbestimmung": lambda r: mitbestimmung(r["beschaeftigte"], r.get("montan", False), r.get("rechtsform", "AG")),
}


def pruefe_rechnung(k):
    fehler, protokoll = [], []
    eintraege = k.get("rechnung") or []
    if isinstance(eintraege, dict):
        eintraege = [eintraege]
    _, antwort = k["frage"], k["antwort"]
    for r in eintraege:
        art = r["art"]
        soll = str(r["ergebnis"])
        ist = RECHNER[art](r)
        if isinstance(ist, str):
            ok = ist.lower() == soll.lower()
            protokoll.append(f"{k['id']} {art}: Code = {ist} | Karte = {soll} → {'OK' if ok else 'FEHLER'}")
        else:
            stellen = nachkommastellen(soll)
            ok = abs(round(ist, stellen) - zahl(soll)) < 1e-9
            protokoll.append(f"{k['id']} {art}: Code = {ist:.6g} | Karte = {soll} → {'OK' if ok else 'FEHLER'}")
        if not ok:
            fehler.append(f"{k['id']}: Rechnung {art} ergibt {ist}, Karte sagt {soll}")
        if soll not in antwort:
            fehler.append(f"{k['id']}: Ergebnis „{soll}“ steht nicht wörtlich in der Antwort")
    return fehler, protokoll


# ---------------------------------------------------------------- Strukturprüfung

def pruefe_aufbau(q):
    fehler, warnungen = [], []
    inhalte = {i["id"]: i for i in q["inhalte"]}
    if len(inhalte) != len(q["inhalte"]):
        fehler.append("doppelte Inhalts-IDs")
    wfragen = {w["id"]: w for w in q["wiederholungsfragen"]}
    gedeckt = collections.defaultdict(list)
    fragen_gesehen = {}
    for k in q["karten"]:
        for feld in ("typ", "folien", "deckt", "frage", "antwort"):
            if not k.get(feld):
                fehler.append(f"{k['id']}: Feld „{feld}“ fehlt")
        if k.get("typ") not in TYPEN:
            fehler.append(f"{k['id']}: unbekannter Typ {k.get('typ')}")
        for d in k.get("deckt", []):
            if d not in inhalte:
                fehler.append(f"{k['id']}: unbekannter Inhalt {d}")
            gedeckt[d].append(k["id"])
        if k.get("w") and k["w"] not in wfragen:
            fehler.append(f"{k['id']}: unbekannte Wiederholungsfrage {k['w']}")
        if k.get("typ") == "klausurfrage" and not k.get("w"):
            fehler.append(f"{k['id']}: Klausurfrage ohne w:")
        schluessel = re.sub(r"\W+", " ", k["frage"]).strip().lower()
        if schluessel in fragen_gesehen:
            fehler.append(f"{k['id']}: gleiche Frage wie {fragen_gesehen[schluessel]}")
        fragen_gesehen[schluessel] = k["id"]
        for feld in ("frage", "antwort"):
            for muster in LATEX_MUSTER:
                if re.search(muster, k[feld]):
                    fehler.append(f"{k['id']}: LaTeX-Rest {muster} in {feld}")
            for name in bildnamen(k[feld]):
                if not os.path.exists(os.path.join(WURZEL, q["fach"], "bilder", name + ".png")):
                    fehler.append(f"{k['id']}: Bild {name}.png fehlt")
            if re.search(r"[^\x00-\uffff]", k[feld]):
                warnungen.append(f"{k['id']}: Zeichen außerhalb BMP (Emoji?) in {feld}")
        woerter = len(re.sub(r"\{\{bild:[^}]+\}\}", "", k["antwort"]).split())
        if woerter > 90 and k["typ"] not in ("klausurfrage", "skizze", "unstimmigkeit"):
            warnungen.append(f"{k['id']}: Antwort mit {woerter} Wörtern – noch atomar?")
        rf, _ = pruefe_rechnung(k)
        fehler += rf
        if k["typ"] == "rechnen" and not k.get("rechnung"):
            fehler.append(f"{k['id']}: Rechenkarte ohne rechnung:")
    for iid in inhalte:
        if not gedeckt[iid]:
            fehler.append(f"Inhalt {iid} ({inhalte[iid]['text']}) ist durch keine Karte abgedeckt")
    for wid, w in wfragen.items():
        karten = [k["id"] for k in q["karten"] if k.get("w") == wid]
        if not karten:
            fehler.append(f"{wid}: keine Musterantwort-Karte")
        for b in w.get("braucht", []):
            if b not in inhalte:
                fehler.append(f"{wid}: braucht unbekannten Inhalt {b}")
            elif not gedeckt[b]:
                fehler.append(f"{wid}: benötigter Inhalt {b} nicht abgedeckt")
    return fehler, warnungen, gedeckt


# ---------------------------------------------------------------- CSV und Matrix

def csv_text(q):
    puffer = io.StringIO()
    w = csv.writer(puffer, quoting=csv.QUOTE_ALL, lineterminator="\n")
    for k in q["karten"]:
        w.writerow(felder(q, k))
    return puffer.getvalue()


def pruefe_csv(pfad):
    fehler = []
    with open(pfad, encoding="utf-8", newline="") as f:
        roh = f.read()
    if roh.startswith("\ufeff"):
        fehler.append("CSV beginnt mit BOM")
    zeilen = list(csv.reader(io.StringIO(roh)))
    laengen = collections.Counter(len(z) for z in zeilen)
    if set(laengen) != {2}:
        fehler.append(f"Spaltenzahlen nicht konstant 2: {dict(laengen)}")
    for n, z in enumerate(zeilen, 1):
        if any(not feld.strip() for feld in z):
            fehler.append(f"Zeile {n}: leeres Feld")
    if zeilen and zeilen[0][0].strip().lower() in ("frage", "question", "vorderseite"):
        fehler.append("erste Zeile sieht wie eine Kopfzeile aus")
    for n, z in enumerate(zeilen, 1):
        for feld in z:
            for muster in LATEX_MUSTER:
                if re.search(muster, feld):
                    fehler.append(f"Zeile {n}: LaTeX-Rest {muster}")
    return fehler, len(zeilen)


def matrix_text(q, gedeckt):
    inhalte = q["inhalte"]
    karten = {k["id"]: k for k in q["karten"]}
    z = [f"# Abdeckungsmatrix – {q['titel']}", "",
         f"Erzeugt mit `werkzeuge/karten.py` aus `{os.path.relpath(q['_pfad'], WURZEL)}`. "
         f"{len(q['karten'])} Karten, {len(inhalte)} prüfbare Inhalte, "
         f"{len(q['wiederholungsfragen'])} Wiederholungsfragen.", ""]
    z += ["## Karten je Typ", "", "| Typ | Anzahl |", "|---|---:|"]
    zaehler = collections.Counter(k["typ"] for k in q["karten"])
    for t in TYPEN:
        if zaehler[t]:
            z.append(f"| {TYPEN[t]} | {zaehler[t]} |")
    z.append(f"| **Summe** | **{len(q['karten'])}** |")
    mit_bild = sum(1 for k in q["karten"] if bildnamen(k["frage"] + k["antwort"]))
    z += ["", f"Karten mit Bild: {mit_bild}.", ""]

    z += ["## Wiederholungsfragen (F. 22, F. 51)", "",
          "| Nr. | Folie | Frage | Musterantwort | benötigte Inhalte | abgedeckt durch |", "|---|---|---|---|---|---|"]
    for w in q["wiederholungsfragen"]:
        muster = ", ".join(k["id"] for k in q["karten"] if k.get("w") == w["id"])
        durch = sorted({kid for b in w["braucht"] for kid in gedeckt[b]})
        ok = all(gedeckt[b] for b in w["braucht"])
        z.append(f"| {w['id']} | {w['folie']} | {w['frage']} | {muster} | {len(w['braucht'])} {'✓' if ok else '✗'} | "
                 f"{', '.join(durch)} |")

    z += ["", "## Inhalte je Folie", "", "| Folie | Inhalt | Karten |", "|---|---|---|"]
    for i in inhalte:
        z.append(f"| {i['folie']} | {i['text']} | {', '.join(gedeckt[i['id']]) or '**fehlt**'} |")

    z += ["", "## Bewusst ausgelassene Folien", "", "| Folien | Grund |", "|---|---|"]
    for a in q.get("ausgelassen", []):
        z.append(f"| {a['folien']} | {a['grund']} |")

    unst = [k for k in q["karten"] if k["typ"] == "unstimmigkeit"]
    if unst:
        z += ["", "## Unstimmigkeiten im Skript (je eine Karte)", ""]
        for k in unst:
            z.append(f"- {k['id']} ({folien_text(k['folien'])}): {k['frage'].splitlines()[0]}")

    if q.get("annahmen"):
        z += ["", "## Annahmen", ""] + [f"- {a}" for a in q["annahmen"]]

    z += ["", "## Karten-Index", "", "| ID | Typ | Folien | Frage |", "|---|---|---|---|"]
    for k in q["karten"]:
        frage = re.sub(r"\{\{bild:[^}]+\}\}", "[Bild]", k["frage"]).replace("\n", " ").replace("|", "/")
        z.append(f"| {k['id']} | {k['typ']} | {folien_text(k['folien'])} | {frage[:110]} |")
    return "\n".join(z) + "\n"


def liste_text(q):
    z = []
    for k in q["karten"]:
        frage, antwort = felder(q, k)
        z += [f"## {k['id']} · {TYPEN[k['typ']]} · {folien_text(k['folien'])}", "", "**Frage**", "", frage, "",
              "**Antwort**", "", antwort, "", "---", ""]
    return "\n".join(z)


# ---------------------------------------------------------------- Wortlaut-Prüfung

def normiere(t):
    t = re.sub(r"(\w)-\n\s*(\w)", r"\1\2", t)          # Silbentrennung am Zeilenende
    t = t.replace("\u00ad", "")
    t = re.sub(r"[•§▪è➔■◆=]|\uf0a7|\uf0d8|\uf0e0", " ", t)
    t = re.sub(r"[„“”\"‚‘’']", "", t)
    t = t.replace("–", "-").replace("—", "-").replace("−", "-")
    t = re.sub(r"\*\*|\*", "", t)
    t = re.sub(r"\s+", " ", t)
    return t.strip().lower()


def folien_quellen(pdf, folien, ocr_folien, tessdata):
    texte = {}
    for f in folien:
        teile = []
        for layout in ([], ["-layout"]):
            r = subprocess.run(["pdftotext", *layout, "-f", str(f), "-l", str(f), pdf, "-"],
                               capture_output=True, text=True, check=True)
            teile.append(r.stdout)
        if f in ocr_folien and shutil.which("tesseract"):
            with tempfile.TemporaryDirectory() as tmp:
                png = os.path.join(tmp, "s")
                subprocess.run(["pdftoppm", "-r", "300", "-png", "-singlefile", "-f", str(f), "-l", str(f), pdf, png],
                               check=True)
                umg = dict(os.environ)
                if tessdata:
                    umg["TESSDATA_PREFIX"] = tessdata
                for psm in ("3", "6", "4"):
                    r = subprocess.run(["tesseract", png + ".png", "-", "-l", "deu", "--psm", psm],
                                       capture_output=True, text=True, env=umg)
                    teile.append(r.stdout)
        texte[f] = [normiere(t) for t in teile]
    return texte


def bester_treffer(zitat, quellen):
    best = (0.0, "")
    for src in quellen:
        if zitat in src:
            return 1.0, zitat
        sm = difflib.SequenceMatcher(None, src, zitat, autojunk=False)
        for a, b, n in sorted(sm.get_matching_blocks(), key=lambda m: -m.size)[:6]:
            if n < 4:
                continue
            start0 = a - b
            for d in range(-12, 13, 2):
                for dl in range(-10, 11, 2):
                    s = max(0, start0 + d)
                    kand = src[s:s + len(zitat) + dl]
                    r = difflib.SequenceMatcher(None, kand, zitat, autojunk=False).ratio()
                    if r > best[0]:
                        best = (r, kand)
    return best


def pruefe_wortlaut(q, pdf, tessdata):
    alle_folien = sorted({f for k in q["karten"] for f in k["folien"]})
    quellen = folien_quellen(pdf, alle_folien, set(q.get("ocr_folien", [])), tessdata)
    ergebnisse = []
    for k in q["karten"]:
        for zitat in re.findall(r"„(.+?)“", k["antwort"], flags=re.S):
            for teil in re.split(r"…|\.\.\.", zitat):
                teil_n = normiere(teil)
                if len(teil_n) < 12:
                    continue
                pool = [t for f in k["folien"] for t in quellen[f]]
                ratio, treffer = bester_treffer(teil_n, pool)
                ergebnisse.append((k["id"], ratio, teil.strip(), treffer))
    return ergebnisse


def pruefe_urls(q):
    fehler = []
    namen = sorted({n for k in q["karten"] for n in bildnamen(k["frage"] + k["antwort"])})
    for n in namen:
        url = f"{REPO_RAW}/{q['fach']}/bilder/{n}.png"
        try:
            with urllib.request.urlopen(urllib.request.Request(url, method="GET"), timeout=20) as r:
                typ = r.headers.get("Content-Type", "")
                if r.status != 200 or not typ.startswith("image/png"):
                    fehler.append(f"{url}: Status {r.status}, Typ {typ}")
        except Exception as e:  # noqa: BLE001
            fehler.append(f"{url}: {e}")
    return fehler, len(namen)


# ---------------------------------------------------------------- Hauptprogramm

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("befehl", choices=["bauen", "pruefen", "liste"])
    ap.add_argument("quelle")
    ap.add_argument("--skript", help="Skript-PDF für den Wortlaut-Abgleich")
    ap.add_argument("--tessdata", help="Ordner mit deu.traineddata (falls nicht systemweit)")
    ap.add_argument("--urls", action="store_true", help="Bild-Links im Netz prüfen")
    ap.add_argument("--bericht", help="Prüfbericht als Markdown hierhin schreiben")
    ap.add_argument("--schwelle", type=float, default=1.0, help="Zitate unter dieser Ähnlichkeit melden")
    args = ap.parse_args()

    q = lade(args.quelle)
    q["_pfad"] = os.path.abspath(args.quelle)

    if args.befehl == "liste":
        print(liste_text(q))
        return

    fehler, warnungen, gedeckt = pruefe_aufbau(q)
    bericht = []
    if args.befehl == "bauen":
        if fehler:
            print("\n".join(["FEHLER:"] + fehler), file=sys.stderr)
            sys.exit(1)
        ziel = os.path.join(WURZEL, q["csv"])
        os.makedirs(os.path.dirname(ziel), exist_ok=True)
        with open(ziel, "w", encoding="utf-8", newline="") as f:
            f.write(csv_text(q))
        with open(os.path.join(WURZEL, q["matrix"]), "w", encoding="utf-8") as f:
            f.write(matrix_text(q, gedeckt))
        zaehler = collections.Counter(k["typ"] for k in q["karten"])
        print(f"{len(q['karten'])} Karten → {q['csv']}")
        for t in TYPEN:
            if zaehler[t]:
                print(f"  {zaehler[t]:4d}  {TYPEN[t]}")
        for w in warnungen:
            print("Warnung:", w)
        return

    # pruefen
    bericht.append("# Prüfbericht\n")
    cf, n = pruefe_csv(os.path.join(WURZEL, q["csv"]))
    bericht.append(f"## CSV\n\n{n} Zeilen, je 2 Felder: {'OK' if not cf else 'FEHLER'}\n")
    bericht += [f"- {x}" for x in cf + fehler]
    if warnungen:
        bericht.append("\nWarnungen:\n")
        bericht += [f"- {w}" for w in warnungen]
    protokoll = []
    for k in q["karten"]:
        protokoll += pruefe_rechnung(k)[1]
    bericht.append(f"\n## Rechnungen ({len(protokoll)} nachgerechnet)\n")
    bericht += [f"- {p}" for p in protokoll]
    if args.skript:
        erg = pruefe_wortlaut(q, args.skript, args.tessdata)
        abw = [e for e in erg if e[1] < args.schwelle]
        bericht.append(f"\n## Wortlaut (difflib)\n\n{len(erg)} Zitatteile geprüft, {len(erg) - len(abw)} wörtlich gefunden, "
                       f"{len(abw)} mit Abweichung:\n")
        bericht.append("| Karte | Ähnlichkeit | Karte sagt | Folientext (beste Stelle) |\n|---|---:|---|---|")
        for kid, r, teil, treffer in sorted(abw, key=lambda e: e[1]):
            bericht.append(f"| {kid} | {r:.3f} | {teil} | {treffer} |")
    if args.urls:
        uf, nu = pruefe_urls(q)
        bericht.append(f"\n## Bild-Links\n\n{nu} Links geprüft: {'alle erreichbar (200, image/png)' if not uf else 'FEHLER'}\n")
        bericht += [f"- {x}" for x in uf]
    text = "\n".join(bericht) + "\n"
    if args.bericht:
        with open(args.bericht, "w", encoding="utf-8") as f:
            f.write(text)
    print(text)
    if cf or fehler:
        sys.exit(1)


if __name__ == "__main__":
    main()
