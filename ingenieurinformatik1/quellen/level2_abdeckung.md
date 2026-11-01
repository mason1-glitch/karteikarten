# Abdeckungsmatrix – Level-Kolloquium 2: Dictionaries

Erzeugt mit `werkzeuge/karten.py` aus `ingenieurinformatik1/quellen/level2_karten.yaml`. 24 Karten, 8 prüfbare Inhalte, 0 Wiederholungsfragen.

## Karten je Typ

| Typ | Anzahl |
|---|---:|
| Klausurfalle | 2 |
| Anwendung (Fall → Einordnung) | 1 |
| Begriff ↔ Erklärung | 1 |
| Lückentext im Code | 1 |
| Was gibt der Code aus? | 10 |
| Finde den Fehler | 2 |
| Schreib Code, der … | 3 |
| Was ist der Unterschied …? | 2 |
| Warum so? (Entscheidung begründen) | 1 |
| Trace-Tabelle (Werte Schritt für Schritt) | 1 |
| **Summe** | **24** |

Karten mit Bild: 0.


## Konzepte → Karten

Gewicht: 3 = in vielen Aufgaben gebraucht, 2 = mehrfach, 1 = selten. F. = Seite im Skript-PDF, Aufg. = Aufgabe im Ordner Informatik-1---Aufgaben-und-Beispiele.

| Konzept | Gewicht | Quelle | Karten | Typen |
|---|---:|---|---|---|
| Dictionary: Schlüssel (key) → Wert (value), geschweifte Klammern, leeres Dictionary {} | 3 | Laborskript F. 3–4, 6 | L2.001, L2.002, L2.020, L2.023 | 4 |
| Lesen mit d[key], Hinzufügen/Ändern mit d[key] = wert, KeyError bei fehlendem Schlüssel | 3 | Laborskript F. 6–7 | L2.003, L2.004, L2.005, L2.013, L2.015, L2.023 | 4 |
| Sicherer Zugriff: if key in d (prüft nur Schlüssel) | 3 | Laborskript F. 7 | L2.006, L2.007, L2.008, L2.022 | 3 |
| Löschen mit del d[key] und d.pop(key[, standard]) | 2 | Laborskript F. 8 | L2.009, L2.010, L2.011, L2.020 | 2 |
| Verschachtelte Dictionaries: d[aussen][innen]; verschachtelter Zugriff von innen nach außen | 3 | Laborskript F. 11–13 | L2.012, L2.013, L2.014, L2.015, L2.016, L2.021 | 5 |
| Alle Einträge durchlaufen: for schluessel, wert in d.items() | 2 | Aufg. 6.5 | L2.017, L2.018, L2.019 | 2 |
| Werte dürfen Zahlen, Listen oder Dictionaries sein; Zahlen als Schlüssel | 2 | Level-Konzept | L2.005, L2.008, L2.016, L2.024 | 2 |
| Warum Dictionaries im Level: Stationen-Einstellungen, Tierlaute, Gegenrichtung, spieler; Zählen mit Dictionary | 3 | Level-Konzept | L2.002, L2.021, L2.022, L2.024 | 4 |

## Annahmen

- Der Code-Leitfaden nennt für Dictionaries nur `.items()` (Aufg. 6.5) als Methode; `pop()` und `del` stehen im Laborskript F. 8. Das direkte Durchlaufen `for taste in tiere:` steht in keiner Quelle wörtlich und ist als Ergänzung markiert.
- Dass ein Dictionary die Einfügereihenfolge behält, steht nur als ergänzender Hinweis in der Markdown-Fassung des Laborskripts (F. 8); auf den Karten als Ergänzung markiert.

## Karten-Index

| ID | Typ | Folien | Frage |
|---|---|---|---|
| L2.001 | begriff | Laborskript Dictionaries F. 3–4, 6 | Was ist ein **Dictionary**, und wie legst du ein leeres an? |
| L2.002 | unterschied | Laborskript Dictionaries F. 3; Level-Konzept | Affen-Echo: Warum speicherst du die Tierlaute als Dictionary und nicht als Liste? ```python tiere = {"a": "Aff |
| L2.003 | code_ausgabe | Laborskript Dictionaries F. 6 | Was gibt der Code aus? ```python spieler = {} spieler["name"] = "Max" spieler["leben"] = 3 spieler["leben"] =  |
| L2.004 | code_fehler | Laborskript Dictionaries F. 7 | Der Code bricht ab. Welche Fehlermeldung, und warum? ```python zeitlimit = {"lianen_sprung": 0.8, "haengebruec |
| L2.005 | code_ausgabe | Laborskript Dictionaries F. 12 | Was gibt der Code aus? ```python zustand = {3: "voll", 2: "angeschlagen", 1: "kritisch"} leben = 2 print(zusta |
| L2.006 | code_schreiben | Laborskript Dictionaries F. 7 | Der Spieler tippt einen Stationsnamen. Gib das Zeitlimit aus – oder eine Meldung, wenn es die Station nicht gi |
| L2.007 | falle | Laborskript Dictionaries F. 7 | Was gibt der Code aus? ```python tiere = {"a": "Affe", "t": "Tukan"} print("a" in tiere) print("Affe" in tiere |
| L2.008 | code_ausgabe | Laborskript Dictionaries F. 7; Level-Konzept | Was gibt der Code aus? ```python gegenrichtung = {"LINKS": ["d", "D"], "RECHTS": ["a", "A"]} antwort = "D" pri |
| L2.009 | code_ausgabe | Laborskript Dictionaries F. 8 | Was gibt der Code aus? ```python tiere = {"a": "Affe", "t": "Tukan", "f": "Frosch"} del tiere["t"] print(tiere |
| L2.010 | code_ausgabe | Laborskript Dictionaries F. 8 | Was gibt der Code aus? ```python tiere = {"a": "Affe", "t": "Tukan"} weg = tiere.pop("a") print(weg) print(tie |
| L2.011 | unterschied | Laborskript Dictionaries F. 8 | Was ist der Unterschied zwischen `del tiere["x"]` und `tiere.pop("x", None)`, wenn es `"x"` nicht gibt? |
| L2.012 | code_ausgabe | Laborskript Dictionaries F. 12–13 | Was gibt der Code aus? ```python stationen = {     "haengebruecke": {"runden": 5, "zeitlimit_s": 1.5},     "af |
| L2.013 | code_luecke | Laborskript Dictionaries F. 13 | Beim Testen ist der Lianen-Sprung zu leicht. Setz das Zeitlimit auf 0,7 s und gib es aus. ```python stationen  |
| L2.014 | code_schreiben | Laborskript Dictionaries F. 13 | Füge `stationen` eine neue Station `"gluehwuermchen"` mit 2 Runden und 1 s Anzeigezeit hinzu. |
| L2.015 | code_fehler | Laborskript Dictionaries F. 7, 12 | Der Code bricht ab. Warum? ```python stationen = {     "haengebruecke": {"runden": 5, "zeitlimit_s": 1.5},     |
| L2.016 | code_ausgabe | Laborskript Dictionaries F. 11 | Was gibt der Code aus? ```python tiere = {"a": "Affe", "t": "Tukan", "f": "Frosch"} tasten = ["a", "t", "f"] p |
| L2.017 | code_ausgabe | Aufg. 6.5 | Was gibt der Code aus? ```python stationen = {"lianen_sprung": {"runden": 3},              "treibsand": {"rund |
| L2.018 | trace | Aufg. 6.5 | Welche Werte haben `name` und `werte` in **jedem** Durchlauf? ```python stationen = {"affen_echo": {"runden":  |
| L2.019 | code_ausgabe | Laborskript Dictionaries F. 13 | Was gibt der Code aus? (Ergänzung: direktes Durchlaufen eines Dictionarys) ```python tiere = {"a": "Affe", "t" |
| L2.020 | code_ausgabe | Laborskript Dictionaries F. 8 (ergänzender Hinweis) | Was gibt der Code aus? ```python tiere = {"a": "Affe", "t": "Tukan"} del tiere["a"] tiere["a"] = "Affe" print( |
| L2.021 | begruenden | Level-Konzept; Laborskript Dictionaries F. 13 | Warum stehen die Einstellungen aller Stationen in **einem** verschachtelten Dictionary statt in Variablen wie  |
| L2.022 | code_schreiben | Laborskript Dictionaries F. 3 | Zähle wie die Strichliste im Laborskript, wie oft jede Taste in `folge = "atafa"` vorkommt, und gib das Dictio |
| L2.023 | falle | Laborskript Dictionaries F. 4 | Was gibt der Code aus? (Ergänzung) ```python tiere = {"a": "Affe", "t": "Tukan", "a": "Ameise"} print(tiere) p |
| L2.024 | anwendung | Level-Konzept | Nenne vier Dictionaries in deinem Level: Schlüssel → Wert. |
