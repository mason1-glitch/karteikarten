# Abdeckungsmatrix – Kapitel 10: Bibliotheken – import, math, random, time, datetime, qrcode

Erzeugt mit `werkzeuge/karten.py` aus `ingenieurinformatik1/quellen/kap10_karten.yaml`. 27 Karten, 9 prüfbare Inhalte, 0 Wiederholungsfragen.

## Karten je Typ

| Typ | Anzahl |
|---|---:|
| Begriff ↔ Erklärung | 6 |
| Lückentext im Code | 6 |
| Was gibt der Code aus? | 4 |
| Finde den Fehler | 2 |
| Schreib Code, der … | 4 |
| Was ist der Unterschied …? | 5 |
| **Summe** | **27** |

Karten mit Bild: 0.


## Konzepte → Karten

Gewicht: 3 = in vielen Aufgaben gebraucht, 2 = mehrfach, 1 = selten. F. = Seite im Skript-PDF, Aufg. = Aufgabe im Ordner Informatik-1---Aufgaben-und-Beispiele.

| Konzept | Gewicht | Quelle | Karten | Typen |
|---|---:|---|---|---|
| import modul, Aufruf modul.funktion(), fehlender Import → NameError | 3 | F. 77–79 · Aufg. 2.5–2.9, 3.4, 6.1–6.5 | K10.001, K10.002, K10.003, K10.004 | 4 |
| import … as … (np, pd, plt) und from … import … | 2 | F. 205 · Aufg. 2.1, 4.3, 4.6, 6.3 | K10.005, K10.006, K10.007 | 3 |
| math.sqrt, math.pi, math.ceil (aufrunden) | 2 | Aufg. 2.5, 2.6 | K10.001, K10.007, K10.008, K10.009, K10.010 | 3 |
| random.randint(a, b) – beide Grenzen eingeschlossen | 2 | Aufg. 2.5, 2.9, 3.4, 3.6 | K10.011, K10.012, K10.013, K10.014 | 4 |
| time.sleep(sekunden) – Programm anhalten | 2 | Aufg. 1.3, 2.7, 2.9 | K10.015, K10.016 | 2 |
| Zeit formatieren mit strftime: %d %m %Y %H %M %S | 2 | Aufg. 2.5, 2.8, 2.9, 5.5 | K10.017, K10.018, K10.019, K10.020, K10.022 | 5 |
| datetime.datetime.now() und .strftime() | 2 | F. 194 · Aufg. 5.5, 6.2 | K10.021, K10.022, K10.023 | 3 |
| Bibliotheken installieren (pip install) vs. importieren | 1 | Aufg. 2.5 | K10.024, K10.025 | 2 |
| qrcode.make(text) und display() im Notebook | 1 | Aufg. 2.6–2.8 | K10.026, K10.027 | 2 |

## Annahmen

- Damit Ausgaben prüfbar sind, erzeugen zwei Karten einen festen Zeitpunkt mit datetime.datetime(2026, …) statt now(); das ist auf den Karten als Ergänzung vermerkt.
- Fehlt ein import, meldet Python 3.12+ zusätzlich „Did you forget to import …?“. Die Karte nennt deshalb nur die Fehlerart NameError.

## Karten-Index

| ID | Typ | Folien | Frage |
|---|---|---|---|
| K10.001 | code_ausgabe | F. 79 · Aufg. 2.5 | Was gibt der Code aus? ```python import math print(math.sqrt(16)) ``` |
| K10.002 | code_fehler | Aufg. 2.5 | Welche **Fehlerart** meldet Python, und was fehlt? ```python toleranz = math.sqrt(16.0) print(toleranz) ``` |
| K10.003 | begriff | F. 77, 78 · Aufg. 2.5 | Was ist eine **Bibliothek** (ein Modul) in Python, und wie macht man ihre Funktionen im Programm verfügbar? |
| K10.004 | code_luecke | Aufg. 2.5 | Ergänze die erste Zeile, damit `random.randint` verfügbar ist. ```python ___ random wurf = random.randint(1, 6 |
| K10.005 | code_luecke | F. 205 · Aufg. 2.1 | Ergänze, sodass das Modul unter dem Kurznamen `plt` angesprochen werden kann. ```python import matplotlib.pypl |
| K10.006 | unterschied | Aufg. 4.3 | Was ist der Unterschied zwischen `import math` und `from math import ceil`? |
| K10.007 | code_ausgabe | Aufg. 4.3 | Was gibt der Code aus? ```python from math import ceil print(ceil(7.2)) ``` |
| K10.008 | code_ausgabe | Aufg. 2.5, 2.6 | Was gibt der Code aus? ```python import math print(math.ceil(7.2)) print(math.ceil(7.0)) ``` |
| K10.009 | code_schreiben | Aufg. 2.5 | Berechne den Umfang einer Welle mit `r = 5` cm (U = 2 · π · r) mit `math.pi` und gib ihn mit zwei Nachkommaste |
| K10.010 | unterschied | F. 75 · Aufg. 2.6 | Was ist der Unterschied zwischen `math.ceil(3520.4)` und `int(3520.4)`? |
| K10.011 | begriff | Aufg. 3.4 | Welche Werte kann `random.randint(1, 6)` liefern? |
| K10.012 | unterschied | Aufg. 3.4, 3.9 | Was ist der Unterschied zwischen den Grenzen bei `random.randint(1, 6)` und `range(1, 6)`? |
| K10.013 | code_luecke | Aufg. 3.4 | Erzeuge eine zufällige Diagnosenummer von **0 bis 7** (beide möglich). Ergänze die Argumente. ```python import |
| K10.014 | code_schreiben | Aufg. 2.9 | Simuliere **fünf** ganzzahlige Temperaturwerte zwischen 50 und 90 °C und sammle sie in einer Liste. |
| K10.015 | begriff | Aufg. 2.7 | Was bewirkt `time.sleep(3)`? |
| K10.016 | code_luecke | Aufg. 2.9 | Zwischen den Messungen soll eine halbe Sekunde Pause sein. Ergänze den Funktionsnamen. ```python import time f |
| K10.017 | code_ausgabe | Aufg. 2.8, 5.5 | Was gibt der Code aus? (Ergänzung: `datetime.datetime(…)` erzeugt hier einen festen Zeitpunkt statt der aktuel |
| K10.018 | begriff | Aufg. 2.8, 5.5 | Wofür stehen in einem strftime-Format `%d`, `%m`, `%Y`, `%H`, `%M` und `%S`? |
| K10.019 | code_luecke | Aufg. 2.9 | Ergänze das Format, sodass die aktuelle Uhrzeit als `Stunde:Minute:Sekunde` erscheint (z. B. `14:30:05`). ```p |
| K10.020 | code_fehler | Aufg. 2.8 | Gewünscht ist das Datum mit **vierstelligem** Jahr. Was gibt der Code aus, und was ist falsch? (Fester Zeitpun |
| K10.021 | code_schreiben | Aufg. 5.5 | Gib einen Protokolleintrag im Format `[2026-10-28 14:30:00] Maschine 3 gestartet` mit der **aktuellen** Zeit a |
| K10.022 | unterschied | Aufg. 2.8, 5.5 | Was ist der Unterschied zwischen `time.strftime(format, time.localtime())` und `datetime.datetime.now().strfti |
| K10.023 | code_luecke | Aufg. 6.2 | Ergänze den Aufruf, der den **aktuellen** Zeitpunkt liefert. ```python import datetime jetzt = datetime.dateti |
| K10.024 | begriff | Aufg. 2.5 | Wie installierst du direkt in einem Jupyter-Notebook eine Bibliothek, die nicht vorinstalliert ist (z. B. qrco |
| K10.025 | unterschied | Aufg. 2.5 | Was ist der Unterschied zwischen `pip install qrcode` und `import qrcode`? |
| K10.026 | code_schreiben | Aufg. 2.6 | Erzeuge im Notebook aus dem Text `"ID: 1042"` einen QR-Code und zeige ihn an. |
| K10.027 | begriff | Aufg. 2.6, 2.7 | Was liefert `qrcode.make(text)`, und wie bringst du mehrere Zeilen Maschinendaten in einen QR-Code? |
