# Abdeckungsmatrix – Kapitel 3: Operatoren und Zahlensysteme

Erzeugt mit `werkzeuge/karten.py` aus `ingenieurinformatik1/quellen/kap03_karten.yaml`. 46 Karten, 14 prüfbare Inhalte, 0 Wiederholungsfragen.

## Karten je Typ

| Typ | Anzahl |
|---|---:|
| Begriff ↔ Erklärung | 11 |
| Lückentext im Code | 3 |
| Was gibt der Code aus? | 18 |
| Finde den Fehler | 6 |
| Schreib Code, der … | 5 |
| Was ist der Unterschied …? | 3 |
| **Summe** | **46** |

Karten mit Bild: 0.


## Konzepte → Karten

Gewicht: 3 = in vielen Aufgaben gebraucht, 2 = mehrfach, 1 = selten. F. = Seite im Skript-PDF, Aufg. = Aufgabe im Ordner Informatik-1---Aufgaben-und-Beispiele.

| Konzept | Gewicht | Quelle | Karten | Typen |
|---|---:|---|---|---|
| Arithmetische Operatoren + - * / // % ** | 3 | F. 103–104 · Aufg. 3.1, 3.2 | K03.001, K03.002, K03.003 | 3 |
| Ganzzahldivision // (abrunden), Ergebnis-Typ | 3 | F. 104 · Aufg. 3.1, 3.9, 3.10, 5.4 | K03.002, K03.003, K03.004, K03.005, K03.006, K03.007 | 5 |
| Modulo %: Rest, Teilbarkeit (x % n == 0), gerade/ungerade | 3 | F. 104 · Aufg. 3.1, 3.9, 3.10, 5.4 | K03.003, K03.006, K03.008, K03.009, K03.010, K03.011 | 4 |
| Ziffern einer Zahl mit // und % zerlegen (Quersumme) | 2 | Aufg. 3.1, 5.4 | K03.012, K03.013, K03.014 | 3 |
| Potenz ** | 1 | F. 104 · Aufg. 3.2 | K03.015, K03.016 | 2 |
| Vergleichsoperatoren == != < > <= >= liefern bool; int und float vergleichbar, str und int nicht | 3 | F. 105 · Aufg. 3.1–3.10 | K03.017, K03.018, K03.019, K03.020 | 3 |
| = (Zuweisung) vs. == (Vergleich) | 3 | F. 113 · Aufg. 3.1 | K03.021, K03.022, K03.023 | 3 |
| Logische Operatoren and, or, not | 3 | F. 106 · Aufg. 3.1, 3.7, 3.11 | K03.024, K03.025, K03.026, K03.027, K03.028 | 4 |
| Rangfolge: ** vor * / // % vor + -, Klammern | 2 | F. 119 · Aufg. 3.2 | K03.015, K03.029, K03.030, K03.031, K03.032 | 3 |
| Rangfolge: Arithmetik vor Vergleich vor not vor and vor or | 2 | F. 119 · Aufg. 3.2 | K03.033, K03.034, K03.035 | 3 |
| Kurzschlussauswertung (Short-Circuit) bei or/and | 1 | Aufg. 3.2 | K03.036, K03.037 | 2 |
| Erweiterte Zuweisung += -= *= //= | 2 | F. 117, 119 · Aufg. 3.8, 3.10, 6.1 | K03.038, K03.039, K03.040 | 3 |
| Binärsystem: Dezimal ↔ Binär (fortgesetzte Division durch 2) | 1 | F. 85–90 · Aufg. 5.4 | K03.041, K03.042, K03.043 | 2 |
| Hexadezimalsystem (Nibble, 0–9/A–F, 0x-Schreibweise) | 1 | F. 91–95 | K03.044, K03.045, K03.046 | 2 |

## Annahmen

- Skript F. 104 beschreibt // als „Nachkommateil wird abgeschnitten“. Für negative Zahlen rundet Python ab (-7 // 2 = -4); die Karte K03 zu -7 // 2 weist darauf hin.
- Skript F. 105/106 nennt Schreibweisen anderer Sprachen (=, <>, MOD, !, &&, ||). In Python 3 gibt es nur ==, !=, %, not, and, or – die Karten verwenden ausschließlich diese.
- Skript F. 119 ordnet <, <=, >, >= über == und != ein. In Python haben alle Vergleichsoperatoren denselben Rang; keine Karte fragt danach.

## Karten-Index

| ID | Typ | Folien | Frage |
|---|---|---|---|
| K03.001 | code_ausgabe | F. 104 · Aufg. 3.1 | Was gibt der Code aus? ```python print(23 / 4) print(23 // 4) print(23 % 4) ``` |
| K03.002 | unterschied | F. 104 · Aufg. 2.2, 3.1 | Was ist der Unterschied zwischen `/` und `//`? |
| K03.003 | code_schreiben | F. 104 · Aufg. 3.9 | 47 Lagerbolzen sollen in Kisten zu je 12 Stück. Schreib Code, der ausgibt, wie viele **volle Kisten** es gibt  |
| K03.004 | code_ausgabe | F. 104 | Was gibt der Code aus? ```python print(-7 // 2) ``` |
| K03.005 | code_ausgabe | F. 104 | Was gibt der Code aus? ```python laenge = 7.5 print(laenge // 2) ``` |
| K03.006 | code_luecke | F. 104 | Ergänze die Operatoren, sodass `2 h 15 min` ausgegeben wird. ```python minuten = 135 print(minuten ___ 60, "h" |
| K03.007 | begriff | F. 104 · Aufg. 3.10 | Wofür verwendet man die **Ganzzahldivision** `//` typischerweise? |
| K03.008 | code_ausgabe | F. 104 · Aufg. 3.9 | Was gibt der Code aus? ```python print(10 % 3) print(12 % 4) print(3 % 5) ``` |
| K03.009 | code_luecke | F. 104 · Aufg. 3.1 | Jedes **fünfte** Teil (Nummer 5, 10, 15 …) soll geprüft werden. Ergänze die Lücke. ```python teil_nr = 35 if t |
| K03.010 | code_schreiben | F. 104 · Aufg. 3.10 | Schreib Code, der für eine Ganzzahl `n` ausgibt, ob sie `gerade` oder `ungerade` ist (Beispiel `n = 7`). |
| K03.011 | begriff | F. 104 · Aufg. 3.9 | Wie prüfst du mit `%`, ob `a` durch `b` **teilbar** ist? |
| K03.012 | code_ausgabe | Aufg. 3.1 | Was gibt der Code aus? ```python zahl = 472 print(zahl // 100) print(zahl // 10 % 10) print(zahl % 10) ``` |
| K03.013 | code_schreiben | Aufg. 3.1 | Schreib Code, der die Ziffern der dreistelligen Zahl `n = 805` mit `//` und `%` zerlegt und **rückwärts** als  |
| K03.014 | code_luecke | Aufg. 5.4 | Ergänze, sodass `einer` die **letzte Ziffer** von `zahl` enthält. ```python zahl = 2026 einer = zahl ___ print |
| K03.015 | code_ausgabe | F. 104, 119 · Aufg. 3.2 | Was gibt der Code aus? ```python print(3 ** 2) print(4 * 3 ** 2) ``` |
| K03.016 | code_schreiben | F. 104 | Berechne mit dem Potenzoperator die Fläche eines Kreises mit `r = 2` (A = 3.14 · r²) und gib sie aus. |
| K03.017 | code_ausgabe | F. 105 | Was gibt der Code aus? ```python druck = 6 print(druck >= 6) print(druck != 6) ``` |
| K03.018 | code_ausgabe | F. 105 · Aufg. 3.2 | Was gibt der Code aus? ```python hub = 120 print(hub == 240 / 2) ``` |
| K03.019 | code_fehler | F. 105 | Welche Fehlermeldung erscheint, und wie behebst du sie? ```python messwert = "85" print(messwert > 80) ``` |
| K03.020 | begriff | F. 105 | Mit welchem Operator prüfst du in Python auf **Ungleichheit**? |
| K03.021 | unterschied | F. 113 | Was ist der Unterschied zwischen `a = 5` und `a == 5`? |
| K03.022 | code_fehler | F. 113 | Der Code bricht schon beim Start ab. Welche Fehlerart meldet Python, und wo liegt der Fehler? ```python status |
| K03.023 | code_ausgabe | F. 113 | Was gibt der Code aus? ```python stufe = 3 ok = stufe == 3 print(ok) ``` |
| K03.024 | code_ausgabe | F. 106 | Was gibt der Code aus? ```python temperatur = 70 druck = 9 print(temperatur > 80 or druck > 8) print(temperatu |
| K03.025 | code_ausgabe | F. 106 | Was gibt der Code aus? ```python gefunden = False print(not gefunden) print(not 3 > 2) ``` |
| K03.026 | code_schreiben | F. 106 · Aufg. 3.1 | Schreib Code, der `Freigabe` ausgibt, wenn die Temperatur `t` zwischen 20 und 30 °C liegt (beide Grenzen einge |
| K03.027 | unterschied | F. 106 | Was ist der Unterschied zwischen `and` und `or`? |
| K03.028 | code_fehler | F. 106 | Der Code bricht beim Start ab. Welche Fehlerart meldet Python, und was ist falsch? ```python druck = 3 temp =  |
| K03.029 | code_ausgabe | F. 119 · Aufg. 3.2 | Was gibt der Code aus? ```python punkte = 3 * 2 ** 3 // 4 print(punkte) ``` |
| K03.030 | code_ausgabe | F. 119 · Aufg. 3.2 | Was gibt der Code aus? ```python teile = 12 print(teile + 3 % 4 - 1) ``` |
| K03.031 | code_fehler | F. 119 | Der Mittelwert von zwei Messungen soll `15.0` sein. Was gibt der Code aus, und wie korrigierst du ihn? ```pyth |
| K03.032 | begriff | F. 119 | In welcher Reihenfolge wertet Python `**`, `*`/`/`/`//`/`%` und `+`/`-` aus? |
| K03.033 | code_ausgabe | F. 119 · Aufg. 3.2 | Was gibt der Code aus? ```python print(False and False or True) print(False and (False or True)) ``` |
| K03.034 | code_fehler | F. 119 · Aufg. 3.2 | Alarm soll nur kommen, wenn (Druck > 8 **oder** Temperatur > 90) **und** die Anlage läuft. Die Anlage steht –  |
| K03.035 | begriff | F. 119 | In welcher Reihenfolge werden in einer Bedingung Rechenoperatoren, Vergleiche, `not`, `and` und `or` ausgewert |
| K03.036 | begriff | Aufg. 3.2 | Was bedeutet **Kurzschlussauswertung** (short-circuit) bei `A or B`? |
| K03.037 | code_ausgabe | Aufg. 3.2 | Was gibt der Code aus? ```python divisor = 0 print(divisor == 0 or 10 / divisor > 1) ``` |
| K03.038 | code_ausgabe | F. 117 · Aufg. 3.10 | Was gibt der Code aus? ```python stueck = 10 stueck += 5 stueck *= 2 stueck -= 1 print(stueck) ``` |
| K03.039 | begriff | F. 117, 119 | Wofür ist `zaehler += 1` die Kurzschreibweise? |
| K03.040 | code_fehler | F. 117 | Welche Fehlermeldung erscheint, und was fehlt? ```python for i in range(3):     anzahl += 1 print(anzahl) ``` |
| K03.041 | begriff | F. 90 · Aufg. 5.4 | Wie rechnest du eine Dezimalzahl in eine Binärzahl um? Zeig es an 22. |
| K03.042 | code_ausgabe | F. 90 · Aufg. 5.4 | Was gibt der Code aus? ```python zahl = 6 ziffern = [] while zahl > 0:     ziffern.insert(0, zahl % 2)     zah |
| K03.043 | begriff | F. 89 | Welche Dezimalzahl ist die Binärzahl **1011**? |
| K03.044 | begriff | F. 91 | Wie viele Bit fasst eine Hexadezimalziffer zusammen? |
| K03.045 | begriff | F. 91 | Welche 16 Zeichen verwendet das Hexadezimalsystem? |
| K03.046 | code_ausgabe | F. 93, 95 | Ergänzung: Python versteht die im Skript (F. 95) gezeigte Schreibweise `0x…` direkt als Hexadezimalzahl. Was g |
