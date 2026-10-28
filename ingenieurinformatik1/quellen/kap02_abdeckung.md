# Abdeckungsmatrix – Kapitel 2: Variablen und Datentypen

Erzeugt mit `werkzeuge/karten.py` aus `ingenieurinformatik1/quellen/kap02_karten.yaml`. 43 Karten, 14 prüfbare Inhalte, 0 Wiederholungsfragen.

## Karten je Typ

| Typ | Anzahl |
|---|---:|
| Begriff ↔ Erklärung | 12 |
| Lückentext im Code | 4 |
| Was gibt der Code aus? | 17 |
| Finde den Fehler | 4 |
| Schreib Code, der … | 2 |
| Was ist der Unterschied …? | 4 |
| **Summe** | **43** |

Karten mit Bild: 0.


## Konzepte → Karten

Gewicht: 3 = in vielen Aufgaben gebraucht, 2 = mehrfach, 1 = selten. F. = Seite im Skript-PDF, Aufg. = Aufgabe im Ordner Informatik-1---Aufgaben-und-Beispiele.

| Konzept | Gewicht | Quelle | Karten | Typen |
|---|---:|---|---|---|
| Variable, Zuweisung mit =, Initialisierung, Reihenfolge der Zuweisungen | 3 | F. 49, 70–71 · Aufg. 2.3 | K02.001, K02.002, K02.003, K02.004, K02.005 | 3 |
| Regeln für Bezeichner, Groß-/Kleinschreibung, reservierte Schlüsselwörter | 2 | F. 58, 62 · Aufg. 2.3 | K02.006, K02.007, K02.008 | 2 |
| Standarddatentypen int, float, str, bool | 3 | F. 64–68 · Aufg. 2.3 | K02.009, K02.010, K02.011, K02.012, K02.013 | 4 |
| type() gibt den Datentyp aus (<class 'int'> …) | 2 | F. 66 · Aufg. 2.2–2.4 | K02.009, K02.014, K02.015, K02.016 | 2 |
| Datentyp ändert sich mit dem zugewiesenen Wert (keine Deklaration wie in C++) | 1 | F. 70–71 | K02.017, K02.018 | 2 |
| / liefert immer float (auch 1500 / 2) | 3 | F. 104 · Aufg. 2.2 | K02.019, K02.020, K02.021 | 3 |
| Implizite Typumwandlung: int mit float → float, int * int bleibt int | 2 | F. 74 · Aufg. 2.2 | K02.021, K02.022, K02.023 | 2 |
| int(): String → Ganzzahl, float → Ganzzahl (schneidet ab, rundet nicht) | 3 | F. 75 · Aufg. 1.2, 2.4 | K02.024, K02.025, K02.026, K02.034 | 3 |
| float(): String → Kommazahl, Punkt statt Komma | 3 | F. 67, 75 · Aufg. 2.4, 3.5 | K02.027, K02.028, K02.029, K02.030 | 3 |
| str(): Zahl → Text (z. B. für Verkettung) | 2 | F. 75, 135 · Aufg. 1.3 | K02.031, K02.032, K02.033 | 3 |
| ValueError bei ungültiger Umwandlung (int("72.4"), float("72,4")) | 2 | F. 75 · Aufg. 2.4 | K02.028, K02.034, K02.035 | 2 |
| Rundungsfehler bei Gleitkommazahlen (0.1 + 0.2, 85.0 - 72.4) | 2 | F. 67, 97 · Aufg. 2.4 | K02.036, K02.037, K02.038 | 2 |
| bool: True/False, Vergleiche liefern bool | 2 | F. 66, 112 · Aufg. 3.1 | K02.014, K02.039, K02.040, K02.041 | 3 |
| Syntax und Semantik | 1 | F. 57 | K02.042, K02.043 | 2 |

## Annahmen

- Skript F. 97 nennt als Rundungsfehler-Beispiel 1 / 3 * 3 = 0,99999999998. In Python ergibt print(1 / 3 * 3) genau 1.0 – die Karten nutzen deshalb 0.1 + 0.2 und 85.0 - 72.4 (Aufg. 2.4).

## Karten-Index

| ID | Typ | Folien | Frage |
|---|---|---|---|
| K02.001 | begriff | F. 49, 70 | Was ist eine **Variable** (laut Skript)? |
| K02.002 | begriff | F. 71 | Was bezeichnet man als **Initialisierung** einer Variablen? |
| K02.003 | code_ausgabe | F. 49 | Was gibt der Code aus? ```python druck = 2 druck = druck + 3 druck = druck * 2 print(druck) ``` |
| K02.004 | code_ausgabe | F. 70, 71 | Was gibt der Code aus? ```python soll = 5 ist = soll soll = 7 print(ist) ``` |
| K02.005 | code_fehler | F. 49 | Welche Fehlermeldung erscheint, und warum? ```python print(temperatur) temperatur = 20 ``` |
| K02.006 | begriff | F. 58, 62 | Welche dieser Bezeichner sind in Python **ungültig**, und warum? `max_temp`, `2te_messung`, `_zaehler`, `druck |
| K02.007 | unterschied | F. 58 | Was ist der Unterschied zwischen den Bezeichnern `Ergebnis`, `ERGEBNIS` und `ergebnis`? |
| K02.008 | begriff | F. 62 | Was sind **reservierte Schlüsselwörter**? |
| K02.009 | code_ausgabe | F. 66–68 | Was gibt der Code aus? ```python print(type(85.5)) print(type("85.5")) ``` |
| K02.010 | code_ausgabe | F. 67 · Aufg. 2.3 | Was gibt der Code aus? ```python drehmoment = 45.0 print(type(drehmoment)) ``` |
| K02.011 | code_schreiben | F. 67, 68 · Aufg. 2.3 | Lege für eine Pumpe drei Variablen mit passendem Datentyp an: Inventarnummer **7731** (Ganzzahl), Förderhöhe * |
| K02.012 | unterschied | F. 64, 67, 68 | Was ist der Unterschied zwischen `5`, `5.0` und `"5"`? |
| K02.013 | begriff | F. 64 | Welche drei Arten von Daten unterscheidet die elektronische Datenverarbeitung laut Skript? |
| K02.014 | code_ausgabe | F. 66 | Was gibt der Code aus? ```python print(type(True)) ``` |
| K02.015 | code_luecke | F. 66 · Aufg. 2.2 | Ergänze die Lücke, sodass der **Datentyp** von `messwert` ausgegeben wird. ```python messwert = 0.75 print(___ |
| K02.016 | code_ausgabe | F. 49, 66 · Aufg. 3.5 | Der Nutzer tippt `42` ein. Was gibt der Code aus? ```python eingabe = input() wert = float(eingabe) print(type |
| K02.017 | code_ausgabe | F. 71 | Was gibt der Code aus? ```python wert = 25 wert = "25" print(type(wert)) ``` |
| K02.018 | unterschied | F. 70, 71 | Was ist laut Skript der Unterschied zwischen Variablen in C++ und in Python? |
| K02.019 | code_ausgabe | F. 104 · Aufg. 2.2 | Was gibt der Code aus? ```python a = 4 b = 2 print(a / b) ``` |
| K02.020 | code_fehler | Aufg. 2.2 | Welche Fehlermeldung erscheint, und wie behebst du sie? ```python leistung = 900 / 2 balken = leistung // 100  |
| K02.021 | begriff | Aufg. 2.2 | Warum liefert `12 * 3` einen int, `12 / 3` aber einen float – obwohl beide Ergebnisse ganzzahlig sind? |
| K02.022 | code_ausgabe | F. 74 · Aufg. 2.2 | Was gibt der Code aus? ```python print(3 * 2) print(3 * 2.0) ``` |
| K02.023 | begriff | F. 74 | Was versteht man unter **impliziter** Typumwandlung? |
| K02.024 | code_ausgabe | F. 75 · Aufg. 1.2 | Was gibt der Code aus? ```python laenge1 = "1250" laenge2 = "380" print(int(laenge1) + int(laenge2)) ``` |
| K02.025 | code_ausgabe | F. 75 | Was gibt der Code aus? ```python print(int(-3.7)) ``` |
| K02.026 | code_luecke | F. 75 · Aufg. 2.4 | Ergänze die Lücke, sodass die Nachkommastellen **abgeschnitten** werden (Ergebnis `18`). ```python laenge = 18 |
| K02.027 | code_ausgabe | F. 75 · Aufg. 2.4 | Was gibt der Code aus? ```python luftdruck = "1013.25" wert = float(luftdruck) print(wert + 1) ``` |
| K02.028 | code_fehler | F. 67, 75 · Aufg. 2.4 | Welche Fehlermeldung erscheint, und wie lautet die Korrektur? ```python wert = float("72,4") print(wert) ``` |
| K02.029 | code_ausgabe | F. 75 | Was gibt der Code aus? ```python print(float(3)) ``` |
| K02.030 | code_schreiben | F. 75 · Aufg. 2.4 | Ein Drucksensor liefert `druck_text = "2.5"` (Text, in bar). Schreib Code, der den Druck in kPa ausgibt (1 bar |
| K02.031 | code_ausgabe | F. 75 | Was gibt der Code aus? ```python print(str(25) + str(4)) ``` |
| K02.032 | code_luecke | F. 135 | Ergänze die Lücke, sodass `Prüfjahr: 2026` ausgegeben wird. ```python pruefjahr = 2026 print("Prüfjahr: " + __ |
| K02.033 | begriff | F. 75, 135 | Wozu braucht man `str()` typischerweise? |
| K02.034 | code_fehler | F. 75 | Welche Fehlermeldung erscheint, und wie kommst du trotzdem zur Ganzzahl `72`? ```python print(int("72.4")) ``` |
| K02.035 | begriff | F. 75 | Was bedeutet die Fehlermeldung? ```text ValueError: invalid literal for int() with base 10: 'abc' ``` |
| K02.036 | code_ausgabe | F. 67, 97 · Aufg. 2.4 | Was gibt der Code aus? ```python soll_mm = 25.0 ist_mm = 24.9 print(soll_mm - ist_mm) ``` |
| K02.037 | code_ausgabe | F. 67, 97 | Was gibt der Code aus? ```python print(0.1 + 0.2) ``` |
| K02.038 | begriff | F. 67, 97 | Warum ergibt `0.1 + 0.2 == 0.3` in Python `False`? |
| K02.039 | code_ausgabe | F. 66, 112 | Was gibt der Code aus? ```python temperatur = 92 alarm = temperatur > 85 print(alarm, type(alarm)) ``` |
| K02.040 | begriff | F. 66 | Welche Werte kann der Datentyp `bool` annehmen, und wie schreibt man sie in Python? |
| K02.041 | code_luecke | F. 66 | Die Variable `fehler` soll den Wahrheitswert **falsch** bekommen. Ergänze die Lücke. ```python fehler = ___ pr |
| K02.042 | begriff | F. 57 | Was legt die **Syntax** einer Programmiersprache fest? |
| K02.043 | unterschied | F. 57 | Was ist der Unterschied zwischen **Syntax** und **Semantik**? |
