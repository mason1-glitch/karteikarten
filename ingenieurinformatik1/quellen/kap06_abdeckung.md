# Abdeckungsmatrix – Kapitel 6: Zeichenketten – Index, Slicing, find, replace, count

Erzeugt mit `werkzeuge/karten.py` aus `ingenieurinformatik1/quellen/kap06_karten.yaml`. 31 Karten, 10 prüfbare Inhalte, 0 Wiederholungsfragen.

## Karten je Typ

| Typ | Anzahl |
|---|---:|
| Begriff ↔ Erklärung | 5 |
| Lückentext im Code | 4 |
| Was gibt der Code aus? | 14 |
| Finde den Fehler | 3 |
| Schreib Code, der … | 5 |
| **Summe** | **31** |

Karten mit Bild: 0.


## Konzepte → Karten

Gewicht: 3 = in vielen Aufgaben gebraucht, 2 = mehrfach, 1 = selten. F. = Seite im Skript-PDF, Aufg. = Aufgabe im Ordner Informatik-1---Aufgaben-und-Beispiele.

| Konzept | Gewicht | Quelle | Karten | Typen |
|---|---:|---|---|---|
| len() – Anzahl der Zeichen (Leerzeichen zählen mit) | 3 | F. 136 · Aufg. 4.1, 4.4 | K06.001, K06.002, K06.003, K06.007 | 2 |
| Zugriff s[i]: Index ab 0, s[-1] letztes Zeichen | 3 | F. 136 · Aufg. 4.1 | K06.004, K06.005, K06.006, K06.007 | 3 |
| IndexError: string index out of range | 1 | F. 136 | K06.008, K06.009 | 2 |
| Slicing s[von:bis] (bis ausgeschlossen, Grenzen weglassbar) | 2 | F. 137 · Aufg. 4.1 | K06.010, K06.011, K06.012, K06.013, K06.014 | 4 |
| Slicing mit Schrittweite s[von:bis:schritt] | 1 | F. 137 | K06.015, K06.016 | 2 |
| find(): Startposition, -1 wenn nicht gefunden, Suche ab Position | 2 | F. 138 · Aufg. 4.1 | K06.017, K06.018, K06.019, K06.020 | 3 |
| replace(): ersetzt alle Vorkommen, liefert neuen String, verkettbar | 2 | F. 138 · Aufg. 4.1, 6.2 | K06.021, K06.022, K06.023, K06.024 | 3 |
| count(): Vorkommen zählen (Groß-/Kleinschreibung beachten) | 2 | F. 146 · Aufg. 6.1 | K06.025, K06.026, K06.027 | 2 |
| Strings sind unveränderlich (Ergebnis neu zuweisen) | 1 | F. 138 · Aufg. 4.1 | K06.022, K06.028, K06.029 | 2 |
| Strings mit find() und Slicing zerlegen und neu zusammensetzen | 2 | F. 137–138 · Aufg. 4.1 | K06.020, K06.030, K06.031 | 2 |

## Karten-Index

| ID | Typ | Folien | Frage |
|---|---|---|---|
| K06.001 | code_ausgabe | F. 136 · Aufg. 4.1 | Was gibt der Code aus? ```python kennung = "DREH-7731" print(len(kennung)) ``` |
| K06.002 | code_ausgabe | F. 136 | Was gibt der Code aus? ```python ort = "Halle 7 " print(len(ort)) ``` |
| K06.003 | code_schreiben | F. 136 | Lies eine Seriennummer ein und gib `gültig` aus, wenn sie **genau 8 Zeichen** hat, sonst `ungültig`. |
| K06.004 | code_ausgabe | F. 136 · Aufg. 4.1 | Was gibt der Code aus? ```python kennung = "FRAES-117-B" print(kennung[0]) print(kennung[-1]) print(kennung[6] |
| K06.005 | begriff | F. 136 | Welchen Index hat das **erste** Zeichen eines Strings? |
| K06.006 | code_luecke | F. 136 | Ergänze, sodass das **dritte** Zeichen (`7`) ausgegeben wird. ```python typ = "M27-B" print(typ[___]) ``` |
| K06.007 | code_ausgabe | F. 136 | Was gibt der Code aus? ```python s = "ABC" for i in range(len(s)):     print(i, s[i]) ``` |
| K06.008 | code_fehler | F. 136 | Welche Fehlermeldung erscheint? ```python code = "X7" print(code[2]) ``` |
| K06.009 | begriff | F. 136 | Welches ist der größte gültige Index eines Strings mit **5** Zeichen? |
| K06.010 | code_ausgabe | F. 137 · Aufg. 4.1 | Was gibt der Code aus? ```python schraube = "M8x40-VZ" print(schraube[0:2]) print(schraube[3:5]) print(schraub |
| K06.011 | code_ausgabe | F. 137 | Was gibt der Code aus? ```python s = "Messung" print(s[:3]) print(s[3:]) ``` |
| K06.012 | code_luecke | F. 137 | Ergänze den Ausschnitt, sodass nur die Jahreszahl `2026` ausgegeben wird. ```python datum = "2026-10-28" print |
| K06.013 | begriff | F. 137 | Welche Zeichen enthält der Ausschnitt `s[von:bis]`? |
| K06.014 | code_schreiben | F. 137 | Gib aus `datei = "messung_07.csv"` die Dateiendung (`csv`) aus – über die **letzten drei** Zeichen. |
| K06.015 | code_ausgabe | F. 137 | Was gibt der Code aus? ```python code = "A1B2C3" print(code[0:6:2]) ``` |
| K06.016 | code_luecke | F. 137 | Ergänze die Schrittweite, sodass nur die Ziffern `123` ausgegeben werden. ```python code = "A1B2C3" print(code |
| K06.017 | code_ausgabe | F. 138 · Aufg. 4.1 | Was gibt der Code aus? ```python text = "Messstelle Kühlkreis Pumpe-2" print(text.find("Pumpe")) ``` |
| K06.018 | begriff | F. 138 | Was liefert `text.find("x")`, wenn `"x"` im Text **nicht** vorkommt? |
| K06.019 | code_ausgabe | F. 138 · Aufg. 4.1 | Was gibt der Code aus? ```python eintrag = "A;B;C" erstes = eintrag.find(";") zweites = eintrag.find(";", erst |
| K06.020 | code_schreiben | F. 137, 138 | Gib aus `zeile = "Temperatur=21.5"` nur den Teil **nach** dem `=` aus – mit find() und Slicing. |
| K06.021 | code_ausgabe | F. 138 · Aufg. 6.2 | Was gibt der Code aus? ```python werte = "1,25;1,30" print(werte.replace(",", ".")) ``` |
| K06.022 | code_fehler | F. 138 · Aufg. 4.1 | Welche Fehlermeldung erscheint, und was wurde vergessen? ```python messwert = "12,5" messwert.replace(",", "." |
| K06.023 | code_ausgabe | F. 138 · Aufg. 6.2 | Was gibt der Code aus? ```python print("MOTOR".replace("O", "0").replace("R", "2")) ``` |
| K06.024 | code_luecke | F. 138 · Aufg. 4.1 | Aus `"Oelstand"` soll `"Ölstand"` werden. Ergänze den Aufruf. ```python text = "Oelstand" text = text.___ prin |
| K06.025 | code_ausgabe | Aufg. 6.1 | Was gibt der Code aus? ```python print("Messwert".count("e")) ``` |
| K06.026 | code_ausgabe | Aufg. 6.1 | Was gibt der Code aus? ```python text = "Abgas Analyse" print(text.count("a"), text.count("A")) ``` |
| K06.027 | code_schreiben | Aufg. 6.1 | Zähle, wie oft der Buchstabe e in `text = "Eine Welle"` vorkommt – **groß und klein zusammen** – und gib die Z |
| K06.028 | code_fehler | F. 138 | Welche Fehlermeldung erscheint, und wie erreichst du `B-17`? ```python kennung = "A-17" kennung[0] = "B" ``` |
| K06.029 | begriff | F. 138 | Warum muss man das Ergebnis von `replace()` einer Variablen zuweisen? |
| K06.030 | code_ausgabe | F. 137, 138 · Aufg. 4.1 | Was gibt der Code aus? ```python eintrag = "Lager, Welle" pos = eintrag.find(",") print(eintrag[:pos]) print(e |
| K06.031 | code_schreiben | F. 137, 138 · Aufg. 4.1 | Aus `name = "Holz, Sandra"` soll `Sandra Holz` werden. Schreib den Code mit find() und Slicing. |
