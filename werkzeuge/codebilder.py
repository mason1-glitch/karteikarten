"""Code-Blöcke in Karten als farbige Bilder (StudyCards kann kein Syntax-Highlighting).

In der App getestet: ```-Blöcke werden nur einfarbig dargestellt, Sprachangaben und HTML
werden ignoriert. Deshalb wird jeder Code-Block als PNG gerendert (Pygments, Farbschema
„One Dark“) und durch einen Bild-Link ersetzt. Inline-Code (`x`) bleibt Text.

In Karten (CSV oder YAML-Quelle) Code ganz normal als Markdown-Block schreiben:

    ```python
    for i in range(3):
        print(i)
    ```

Aufrufe (aus dem Repo-Wurzelordner):
    python3 werkzeuge/codebilder.py <fach>/karten/<datei>.csv          CSV umschreiben, Bilder erzeugen
    python3 werkzeuge/codebilder.py <fach>/karten/<datei>.csv --vorschau   nur anzeigen, nichts schreiben
`karten.py bauen` ruft das automatisch auf (Funktion `code_einsetzen`).

Bildname: <fach>/bilder/code_<hash>.png – aus Sprache + Code berechnet, gleicher Code
ergibt also immer dieselbe Datei (erneutes Ausführen erzeugt keine Duplikate).
Ohne Sprachangabe wird Python angenommen; `text` für einfarbige Ausgaben.
Benötigt: pip install pygments pillow
"""
import argparse
import csv
import hashlib
import io
import os
import re
import sys

WURZEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO_RAW = "https://raw.githubusercontent.com/mason1-glitch/karteikarten/main"
STANDARD_SPRACHE = "python"
STIL = "one-dark"

# ```sprache … ``` oder ~~~sprache … ~~~ (Zaun muss am Zeilenanfang stehen)
BLOCK = re.compile(r"^(?P<zaun>```|~~~)[ \t]*(?P<sprache>[\w+#.-]*)[ \t]*\n(?P<code>.*?)\n?^(?P=zaun)[ \t]*$",
                   re.M | re.S)


def bild_name(code, sprache):
    h = hashlib.sha1(f"{sprache}\n{code}".encode("utf-8")).hexdigest()[:10]
    return f"code_{h}"


def rendern(code, sprache, ziel):
    """Code als PNG im Dunkelstil der App schreiben."""
    from pygments import highlight
    from pygments.formatters import ImageFormatter
    from pygments.lexers import TextLexer, get_lexer_by_name
    from pygments.util import ClassNotFound

    try:
        lexer = get_lexer_by_name(sprache) if sprache else TextLexer()
    except ClassNotFound:
        print(f"  Hinweis: Sprache „{sprache}“ unbekannt – einfarbig gerendert.", file=sys.stderr)
        lexer = TextLexer()
    fmt = ImageFormatter(style=STIL, font_size=28, line_numbers=False, image_pad=28,
                         line_pad=6, font_name="DejaVu Sans Mono")
    png = highlight(code.expandtabs(4), lexer, fmt)
    os.makedirs(os.path.dirname(ziel), exist_ok=True)
    with open(ziel, "wb") as f:
        f.write(png)


def code_einsetzen(text, fach, schreiben=True, erzeugt=None):
    """Alle Code-Blöcke in `text` durch Bild-Links ersetzen (und Bilder erzeugen)."""
    def ersetze(m):
        sprache = (m["sprache"] or STANDARD_SPRACHE).lower()
        code = m["code"].rstrip("\n")
        name = bild_name(code, sprache)
        pfad = os.path.join(WURZEL, fach, "bilder", name + ".png")
        if schreiben and not os.path.exists(pfad):
            rendern(code, "" if sprache == "text" else sprache, pfad)
        if erzeugt is not None:
            erzeugt.append(os.path.relpath(pfad, WURZEL))
        return f"![Code ({sprache})]({REPO_RAW}/{fach}/bilder/{name}.png)"
    return BLOCK.sub(ersetze, text)


def csv_umschreiben(pfad, schreiben=True):
    rel = os.path.relpath(os.path.abspath(pfad), WURZEL)
    fach = rel.split(os.sep)[0]
    with open(pfad, encoding="utf-8", newline="") as f:
        zeilen = list(csv.reader(f))
    erzeugt = []
    neu = [[code_einsetzen(feld, fach, schreiben, erzeugt) for feld in z] for z in zeilen]
    if schreiben and neu != zeilen:
        puffer = io.StringIO()
        csv.writer(puffer, quoting=csv.QUOTE_ALL, lineterminator="\n").writerows(neu)
        with open(pfad, "w", encoding="utf-8", newline="") as f:
            f.write(puffer.getvalue())
    return neu, sorted(set(erzeugt))


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("csv", nargs="+")
    ap.add_argument("--vorschau", action="store_true", help="nichts schreiben, nur Ergebnis zeigen")
    a = ap.parse_args()
    for pfad in a.csv:
        neu, bilder = csv_umschreiben(pfad, schreiben=not a.vorschau)
        print(f"{pfad}: {len(bilder)} Code-Bild(er)")
        for b in bilder:
            print("  ", b)
        if a.vorschau:
            csv.writer(sys.stdout, quoting=csv.QUOTE_ALL, lineterminator="\n").writerows(neu)


if __name__ == "__main__":
    main()
