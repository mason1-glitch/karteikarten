"""Sprachelemente in Python-Code inventarisieren und gegen Karteikarten prüfen.

Wozu: Fürs Kolloquium muss jedes Sprachelement im eigenen Code erklärbar sein. Das Werkzeug
listet per ast/tokenize alles auf, was ein Programm verwendet (Schlüsselwörter, Operatoren,
eingebaute Funktionen, Methoden, Module, Escape-Sequenzen, Ausnahmen …), ordnet jedes Element
dem Stoff zu (Skript / Labor / Ergänzung) und prüft, ob es im Kartensatz eine Karte dazu gibt.

Zuordnung zu Karten: In der YAML-Quelle bekommt jedes Inhalt-Element eine Liste
`konstrukte: [schluessel, …]`. Ein Schlüssel gilt als abgedeckt, wenn ein Inhalt ihn nennt
und mindestens eine Karte diesen Inhalt deckt.

Aufrufe (aus dem Repo-Wurzelordner):
    python3 werkzeuge/inventar.py code <datei.py …>                  Inventar mit Stoff-Zuordnung
    python3 werkzeuge/inventar.py abdeckung <datei.py …> --karten <yaml …> [--bericht datei.md]
    python3 werkzeuge/inventar.py karten <yaml …>                    Code auf den Karten: jede Ergänzung
                                                                     muss auf der Karte als „Ergänzung“ markiert sein
Welle 2 (eigener Level-Code): `abdeckung level_dschungel.py --karten …` zeigt jede Zeile ohne Karte.
"""
import argparse
import ast
import collections
import io
import keyword
import os
import re
import sys
import tokenize

import yaml

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# ---------------------------------------------------------------- Stoff-Zuordnung
# Quelle: Code-Leitfaden (Abschnitt 1 = behandelt, 1.11 = nicht im Stoff), Laborskript Dictionaries,
# Labor-Ablauf (KW45 Sortieralgorithmen/Rekursion, KW46 Ausnahmebehandlung).
STOFF, LABOR, ERG = "Stoff", "Labor", "Ergänzung"

ZUORDNUNG = {
    # Schlüsselwörter
    "kw:def": (STOFF, "F. 171"), "kw:return": (STOFF, "F. 173"), "kw:if": (STOFF, "F. 112"),
    "kw:elif": (STOFF, "F. 115"), "kw:else": (STOFF, "F. 114"), "kw:while": (STOFF, "F. 125"),
    "kw:for": (STOFF, "F. 128"), "kw:in": (STOFF, "F. 143"), "kw:break": (STOFF, "Aufg. 3.8"),
    "kw:continue": (STOFF, "Aufg. 3.8"), "kw:pass": (STOFF, "F. 113"), "kw:global": (STOFF, "F. 183"),
    "kw:import": (STOFF, "F. 173"), "kw:as": (STOFF, "import … as"), "kw:from": (STOFF, "Aufg. 4.3"),
    "kw:and": (STOFF, "F. 106"), "kw:or": (STOFF, "F. 106"), "kw:not": (STOFF, "F. 106"),
    "kw:is": (STOFF, "Aufg. 5.3"), "kw:None": (STOFF, "Aufg. 5.3"), "kw:True": (STOFF, "F. 66"),
    "kw:False": (STOFF, "F. 66"), "kw:del": (LABOR, "Laborskript Dictionaries F. 8"),
    "kw:try": (LABOR, "Labor KW46"), "kw:except": (LABOR, "Labor KW46"),
    "kw:finally": (ERG, "nicht im Stoff"), "kw:raise": (ERG, "nicht im Stoff"),
    "kw:with": (ERG, "nicht im Stoff"), "kw:lambda": (ERG, "nicht im Stoff"),
    "kw:assert": (ERG, "nicht im Stoff"), "kw:class": (ERG, "nicht im Stoff"),
    "kw:yield": (ERG, "nicht im Stoff"), "kw:nonlocal": (ERG, "nicht im Stoff"),
    # Operatoren
    "op:+": (STOFF, "F. 103"), "op:-": (STOFF, "F. 103"), "op:*": (STOFF, "F. 103"), "op:/": (STOFF, "F. 104"),
    "op://": (STOFF, "F. 104"), "op:%": (STOFF, "F. 104"), "op:**": (STOFF, "F. 104"),
    "op:-x": (STOFF, "Vorzeichen"), "aug:+=": (STOFF, "F. 117"), "aug:-=": (STOFF, "F. 117"),
    "aug:*=": (STOFF, "F. 119"), "aug://=": (STOFF, "F. 119"), "aug:/=": (STOFF, "F. 119"),
    "cmp:==": (STOFF, "F. 105"), "cmp:!=": (STOFF, "F. 105"), "cmp:<": (STOFF, "F. 105"),
    "cmp:>": (STOFF, "F. 105"), "cmp:<=": (STOFF, "F. 105"), "cmp:>=": (STOFF, "F. 105"),
    "cmp:in": (STOFF, "Aufg. 3.8"), "cmp:not in": (STOFF, "F. 119"), "cmp:is": (STOFF, "Aufg. 5.3"),
    "cmp:is not": (STOFF, "Aufg. 5.3"),
    # Bausteine
    "zuweisung": (STOFF, "F. 49"), "entpacken": (STOFF, "Aufg. 5.2"), "index": (STOFF, "F. 136, 141"),
    "slicing": (STOFF, "F. 137 (Strings)"), "liste": (STOFF, "F. 141"), "dictionary": (LABOR, "Laborskript F. 4"),
    "tupel": (STOFF, "F. 155"), "listcomp": (STOFF, "F. 153"), "f-string": (STOFF, "F. 116"),
    "f-format": (STOFF, "Aufg. 3.11"), "docstring": (STOFF, "Aufg. 5.5"), "default-parameter": (ERG, "nicht im Stoff"),
    "rekursion": (LABOR, "Labor KW45"), "verkettete-vergleiche": (ERG, "nicht im Stoff"),
    "ternaer": (ERG, "nicht im Stoff"),
    # Escape-Sequenzen
    "esc:\\n": (STOFF, "F. 53"), "esc:\\t": (STOFF, "F. 53"), "esc:\\r": (STOFF, "F. 53"), "esc:\\b": (STOFF, "F. 53"),
    "esc:\\\"": (STOFF, "F. 69"), "esc:\\\\": (STOFF, "F. 69"), "esc:\\a": (ERG, "nicht im Stoff"),
    "esc:\\033": (ERG, "ANSI-Farbcodes, nicht im Stoff"),
    # eingebaute Funktionen
    "call:print": (STOFF, "F. 48"), "print:end": (STOFF, "F. 151"), "print:flush": (ERG, "nicht im Stoff"),
    "print:sep": (ERG, "nicht im Stoff"), "call:input": (STOFF, "F. 49"), "call:int": (STOFF, "F. 75"),
    "call:float": (STOFF, "F. 75"), "call:str": (STOFF, "F. 75"), "call:len": (STOFF, "F. 136"),
    "call:range": (STOFF, "F. 128"), "call:type": (STOFF, "F. 66"), "call:open": (STOFF, "F. 189"),
    "call:enumerate": (STOFF, "Aufg. 4.4"), "call:round": (ERG, "nur F. 47"), "call:min": (ERG, "nur F. 47"),
    "call:max": (ERG, "nur F. 47"), "call:sum": (ERG, "nur F. 47"), "call:abs": (ERG, "nur F. 47"),
    "call:sorted": (ERG, "nur F. 47"), "call:list": (ERG, "nur F. 47"), "call:dict": (ERG, "nur F. 47"),
    # Methoden
    "methode:append": (STOFF, "F. 144"), "methode:insert": (STOFF, "F. 144"), "methode:pop": (STOFF, "F. 145; Laborskript F. 8"),
    "methode:remove": (STOFF, "F. 145"), "methode:clear": (STOFF, "F. 145"), "methode:index": (STOFF, "F. 146"),
    "methode:count": (STOFF, "F. 146"), "methode:reverse": (STOFF, "F. 146"), "methode:sort": (STOFF, "F. 147"),
    "methode:copy": (STOFF, "Aufg. 4.6"), "methode:find": (STOFF, "F. 138"), "methode:replace": (STOFF, "F. 138"),
    "methode:items": (STOFF, "Aufg. 6.5"), "methode:write": (STOFF, "F. 194"), "methode:close": (STOFF, "F. 190"),
    "methode:read": (STOFF, "F. 190"), "methode:readline": (STOFF, "F. 191"), "methode:readlines": (STOFF, "F. 191"),
    "methode:split": (ERG, "nur F. 153"), "methode:strip": (ERG, "nicht im Stoff"), "methode:lower": (ERG, "nicht im Stoff"),
    "methode:upper": (ERG, "nicht im Stoff"), "methode:join": (ERG, "nicht im Stoff"), "methode:isdigit": (ERG, "nicht im Stoff"),
    "methode:keys": (ERG, "nicht im Stoff"), "methode:values": (ERG, "nicht im Stoff"), "methode:get": (ERG, "nicht im Stoff"),
    # Module
    "modul:random": (STOFF, "Aufg. 2.5"), "modul:time": (STOFF, "Aufg. 1.3"), "modul:math": (STOFF, "F. 173"),
    "modul:datetime": (STOFF, "F. 194"), "modul:os": (ERG, "nicht im Stoff"), "modul:winsound": (ERG, "nur Windows"),
    "modul:pygame": (ERG, "Paket, requirements.txt"),
    "call:random.randint": (STOFF, "Aufg. 2.5"), "call:random.seed": (STOFF, "Aufg. 2.9"),
    "call:random.choice": (ERG, "nicht im Stoff"), "call:random.shuffle": (ERG, "nicht im Stoff"),
    "call:time.sleep": (STOFF, "Aufg. 1.3"), "call:time.time": (ERG, "nicht im Stoff"),
    "call:time.strftime": (STOFF, "Aufg. 1.3"), "call:time.localtime": (STOFF, "Aufg. 1.3"),
    "call:os.system": (ERG, "nicht im Stoff"), "call:winsound.Beep": (ERG, "nur Windows"),
    "call:datetime.datetime.now": (STOFF, "F. 194"),
    # Ausnahmen
    "except:ValueError": (LABOR, "Labor KW46"), "except:IndexError": (LABOR, "Labor KW46"),
    "except:KeyError": (LABOR, "Labor KW46"), "except:FileNotFoundError": (LABOR, "Labor KW46"),
    "except:ZeroDivisionError": (LABOR, "Labor KW46"), "except:KeyboardInterrupt": (LABOR, "Labor KW46"),
    "except:ImportError": (LABOR, "Labor KW46"), "except:ModuleNotFoundError": (LABOR, "Labor KW46"),
    "except:RecursionError": (LABOR, "Labor KW46"), "except:RuntimeError": (LABOR, "Labor KW46"),
    "except:EOFError": (LABOR, "Labor KW46"), "except:PermissionError": (LABOR, "Labor KW46"),
    "except:<leer>": (LABOR, "leeres except – vermeiden!"),
}

ESCAPES = {"\n": "esc:\\n", "\t": "esc:\\t", "\r": "esc:\\r", "\b": "esc:\\b", "\a": "esc:\\a", "\x1b": "esc:\\033"}
OPS = {ast.Add: "+", ast.Sub: "-", ast.Mult: "*", ast.Div: "/", ast.FloorDiv: "//", ast.Mod: "%", ast.Pow: "**"}
CMPS = {ast.Eq: "==", ast.NotEq: "!=", ast.Lt: "<", ast.Gt: ">", ast.LtE: "<=", ast.GtE: ">=", ast.In: "in",
        ast.NotIn: "not in", ast.Is: "is", ast.IsNot: "is not"}
BUILTINS = {"print", "input", "int", "float", "str", "len", "range", "type", "open", "enumerate", "round", "min",
            "max", "sum", "abs", "sorted", "list", "dict", "zip", "map", "filter", "isinstance", "chr", "ord",
            "bool", "set", "tuple", "reversed", "any", "all", "exit", "quit", "repr", "id", "eval", "exec"}
for _name in ("zip", "map", "filter", "isinstance", "chr", "ord", "bool", "set", "tuple", "reversed", "any",
              "all", "exit", "quit", "repr", "id", "eval", "exec"):
    ZUORDNUNG.setdefault("call:" + _name, (ERG, "nur F. 47"))


# Module, die auch in Code-Ausschnitten ohne import-Zeile als Modul erkannt werden
BEKANNTE_MODULE = {"random", "time", "math", "datetime", "os", "winsound", "pygame", "level_dschungel"}

# Module der Gruppe (eigene Dateien des Spiels)
EIGENE_MODULE = {"level_dschungel", "main"}


def stoff(schluessel):
    if schluessel in ZUORDNUNG:
        return ZUORDNUNG[schluessel]
    if schluessel.startswith("call:eigene:"):
        return (STOFF, "eigene Funktion, F. 180")
    teile = schluessel.split(":", 1)
    if teile[0] in ("modul", "call") and teile[1].split(".")[0] in EIGENE_MODULE:
        return (STOFF, "eigenes Modul, Laborfolie F. 15")
    return ("unbekannt", "einordnen!")


def name_von(knoten):
    """'time.time' für time.time(), None für Methodenaufrufe auf Variablen."""
    teile = []
    while isinstance(knoten, ast.Attribute):
        teile.append(knoten.attr)
        knoten = knoten.value
    if isinstance(knoten, ast.Name):
        teile.append(knoten.id)
        return ".".join(reversed(teile))
    return None


def inventar(quelltext):
    """Zähler Schlüssel → Anzahl und Schlüssel → erste Zeilennummern."""
    zaehler, zeilen = collections.Counter(), collections.defaultdict(list)

    def merke(s, zeile):
        zaehler[s] += 1
        if len(zeilen[s]) < 5:
            zeilen[s].append(zeile)

    for tok in tokenize.generate_tokens(io.StringIO(quelltext).readline):
        if tok.type == tokenize.NAME and keyword.iskeyword(tok.string):
            merke("kw:" + tok.string, tok.start[0])
    baum = ast.parse(quelltext)
    module, eigene = set(), {}
    for k in ast.walk(baum):
        if isinstance(k, ast.Import):
            for a in k.names:
                module.add(a.asname or a.name)
                merke("modul:" + a.name, k.lineno)
        elif isinstance(k, ast.ImportFrom):
            merke("modul:" + (k.module or ""), k.lineno)
        elif isinstance(k, ast.FunctionDef):
            eigene[k.name] = k
            if k.args.defaults:
                merke("default-parameter", k.lineno)
            if (k.body and isinstance(k.body[0], ast.Expr) and isinstance(k.body[0].value, ast.Constant)
                    and isinstance(k.body[0].value.value, str)):
                merke("docstring", k.lineno)
    for k in ast.walk(baum):
        z = getattr(k, "lineno", 0)
        if isinstance(k, ast.BinOp) and type(k.op) in OPS:
            merke("op:" + OPS[type(k.op)], z)
        elif isinstance(k, ast.UnaryOp) and isinstance(k.op, ast.USub):
            merke("op:-x", z)
        elif isinstance(k, ast.AugAssign) and type(k.op) in OPS:
            merke("aug:" + OPS[type(k.op)] + "=", z)
        elif isinstance(k, ast.Compare):
            for o in k.ops:
                merke("cmp:" + CMPS[type(o)], z)
            if len(k.ops) > 1:
                merke("verkettete-vergleiche", z)
        elif isinstance(k, ast.Assign):
            merke("zuweisung", z)
            if any(isinstance(t, ast.Tuple) for t in k.targets):
                merke("entpacken", z)
        elif isinstance(k, ast.For) and isinstance(k.target, ast.Tuple):
            merke("entpacken", z)
        elif isinstance(k, ast.Subscript):
            merke("slicing" if isinstance(k.slice, ast.Slice) else "index", z)
        elif isinstance(k, ast.List):
            merke("liste", z)
        elif isinstance(k, ast.Dict):
            merke("dictionary", z)
        elif isinstance(k, ast.Tuple) and not isinstance(getattr(k, "ctx", None), ast.Store):
            merke("tupel", z)
        elif isinstance(k, ast.ListComp):
            merke("listcomp", z)
        elif isinstance(k, ast.IfExp):
            merke("ternaer", z)
        elif isinstance(k, ast.JoinedStr):
            merke("f-string", z)
            if any(isinstance(w, ast.FormattedValue) and w.format_spec for w in k.values):
                merke("f-format", z)
        elif isinstance(k, ast.Constant) and isinstance(k.value, str):
            for zeichen, s in ESCAPES.items():
                if zeichen in k.value:
                    merke(s, z)
        elif isinstance(k, ast.ExceptHandler):
            if k.type is None:
                merke("except:<leer>", z)
            else:
                for t in (k.type.elts if isinstance(k.type, ast.Tuple) else [k.type]):
                    merke("except:" + (name_von(t) or "?"), z)
        elif isinstance(k, ast.Call):
            name = name_von(k.func)
            if isinstance(k.func, ast.Name) and name in BUILTINS:
                merke("call:" + name, z)
                if name == "print":
                    for kw in k.keywords:
                        merke("print:" + (kw.arg or "**"), z)
            elif isinstance(k.func, ast.Name) and name in eigene:
                merke("call:eigene:" + name, z)
            elif isinstance(k.func, ast.Attribute):
                wurzel = name.split(".")[0] if name else None
                if wurzel in module or wurzel in BEKANNTE_MODULE:
                    merke("call:" + name, z)
                else:
                    merke("methode:" + k.func.attr, z)
            elif isinstance(k.func, ast.Name):
                merke("call:eigene:" + name, z)   # im Ausschnitt nicht definiert: Funktion des Spiels
    # Rekursion: eine Funktion ruft sich selbst auf
    for name, f in eigene.items():
        for k in ast.walk(f):
            if isinstance(k, ast.Call) and isinstance(k.func, ast.Name) and k.func.id == name:
                merke("rekursion", k.lineno)
    # Escape-Sequenzen \" und \\ stehen nur im Quelltext, nicht im Wert
    for nr, zeile in enumerate(quelltext.splitlines(), 1):
        if "\\\"" in zeile or "\\'" in zeile:
            merke("esc:\\\"", nr)
        if "\\\\" in zeile:
            merke("esc:\\\\", nr)
    return zaehler, zeilen


def eigene_funktionen_zusammenfassen(zaehler, zeilen):
    """Aufrufe eigener Funktionen zählen als ein Schlüssel „call:eigene“."""
    z2, l2 = collections.Counter(), collections.defaultdict(list)
    for s, n in zaehler.items():
        ziel = "call:eigene" if s.startswith("call:eigene:") else s
        z2[ziel] += n
        l2[ziel] += zeilen[s]
    return z2, l2


ZUORDNUNG["call:eigene"] = (STOFF, "F. 180")


def lade_karten(pfade):
    """Schlüssel → Liste (Inhalt-ID, Karten-IDs) aus den YAML-Quellen."""
    from karten import lade, pruefe_aufbau
    abdeckung = collections.defaultdict(list)
    for pfad in pfade:
        q = lade(pfad)
        _, _, gedeckt = pruefe_aufbau(q)
        for i in q["inhalte"]:
            for s in i.get("konstrukte", []):
                abdeckung[s].append((i["id"], gedeckt[i["id"]]))
    return abdeckung


def befehl_code(dateien):
    gesamt, zeilen = collections.Counter(), collections.defaultdict(list)
    for d in dateien:
        z, l = eigene_funktionen_zusammenfassen(*inventar(open(d, encoding="utf-8").read()))
        gesamt.update(z)
        for s in l:
            zeilen[s] += [f"{os.path.basename(d)}:{n}" for n in l[s]]
    print("| Element | Anzahl | Stoff | Quelle |\n|---|---:|---|---|")
    for s in sorted(gesamt):
        art, quelle = stoff(s)
        print(f"| `{s}` | {gesamt[s]} | {art} | {quelle} |")
    return gesamt, zeilen


def befehl_abdeckung(dateien, karten, bericht):
    gesamt, zeilen = collections.Counter(), collections.defaultdict(list)
    for d in dateien:
        z, l = eigene_funktionen_zusammenfassen(*inventar(open(d, encoding="utf-8").read()))
        gesamt.update(z)
        for s in l:
            zeilen[s] += [f"{os.path.basename(d)}:{n}" for n in l[s]]
    abdeckung = lade_karten(karten)
    zeilen_md, luecken = [], []
    zaehl_art = collections.Counter()
    for s in sorted(gesamt):
        art, quelle = stoff(s)
        zaehl_art[art] += 1
        treffer = [(iid, ids) for iid, ids in abdeckung.get(s, []) if ids]
        ids = sorted({k for _, kk in treffer for k in kk})
        if not ids:
            luecken.append(s)
        zeilen_md.append(f"| `{s}` | {art} | {quelle} | {gesamt[s]} | {', '.join(zeilen[s][:3])} | "
                         f"{', '.join(ids[:6]) + (' …' if len(ids) > 6 else '') or '**fehlt**'} |")
    n = len(gesamt)
    kopf = [f"# Abdeckung Code → Karten", "",
            f"Code: {', '.join(os.path.relpath(d) for d in dateien)}  ",
            f"Karten: {', '.join(os.path.relpath(k) for k in karten)}", "",
            f"**{n - len(luecken)} von {n} Sprachelementen haben mindestens eine Karte "
            f"({100 * (n - len(luecken)) / max(n, 1):.0f} %).** "
            f"Stoff: {zaehl_art[STOFF]}, Labor: {zaehl_art[LABOR]}, Ergänzung: {zaehl_art[ERG]}, "
            f"unbekannt: {zaehl_art['unbekannt']}.", "",
            "| Element | Stoff | Quelle | Anzahl | Fundstellen | Karten |", "|---|---|---|---:|---|---|"]
    text = "\n".join(kopf + zeilen_md) + "\n"
    if luecken:
        text += "\n**Ohne Karte:** " + ", ".join(f"`{s}`" for s in luecken) + "\n"
    if bericht:
        with open(bericht, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"{n - len(luecken)}/{n} abgedeckt → {bericht}")
    else:
        print(text)
    return luecken


def befehl_karten(pfade):
    """Ergänzungen im Karten-Code müssen auf der Karte als „Ergänzung“ markiert sein."""
    from karten import code_bloecke, lade
    fehler = []
    for pfad in pfade:
        q = lade(pfad)
        for k in q["karten"]:
            pb, _ = code_bloecke(k)
            text = k["frage"] + k["antwort"]
            for code in pb:
                try:
                    z, _ = inventar(code.replace("___", "x"))
                except SyntaxError:
                    continue  # absichtlich fehlerhafter Code (Finde-den-Fehler-Karte)
                for s in z:
                    art, _ = stoff(s)
                    if art == ERG and "rgänzung" not in text:
                        fehler.append(f"{k['id']}: `{s}` ist eine Ergänzung, die Karte sagt das nicht")
                    if art == "unbekannt" and k["typ"] not in ("code_fehler", "falle"):
                        fehler.append(f"{k['id']}: `{s}` ist nicht eingeordnet")
    print("\n".join(sorted(set(fehler))) or "Alle Ergänzungen auf den Karten markiert.")
    return fehler


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("befehl", choices=["code", "abdeckung", "karten"])
    ap.add_argument("dateien", nargs="+")
    ap.add_argument("--karten", nargs="+", default=[])
    ap.add_argument("--bericht")
    a = ap.parse_args()
    if a.befehl == "code":
        befehl_code(a.dateien)
    elif a.befehl == "abdeckung":
        if not a.karten:
            ap.error("--karten fehlt")
        sys.exit(1 if befehl_abdeckung(a.dateien, a.karten, a.bericht) else 0)
    else:
        sys.exit(1 if befehl_karten(a.dateien) else 0)


if __name__ == "__main__":
    main()
