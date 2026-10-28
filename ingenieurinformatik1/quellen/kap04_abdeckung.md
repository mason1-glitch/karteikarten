# Abdeckungsmatrix – Kapitel 4: Verzweigungen (if, elif, else) und Einrückung

Erzeugt mit `werkzeuge/karten.py` aus `ingenieurinformatik1/quellen/kap04_karten.yaml`. 22 Karten, 6 prüfbare Inhalte, 0 Wiederholungsfragen.

## Karten je Typ

| Typ | Anzahl |
|---|---:|
| Begriff ↔ Erklärung | 5 |
| Was gibt der Code aus? | 6 |
| Finde den Fehler | 5 |
| Schreib Code, der … | 4 |
| Was ist der Unterschied …? | 2 |
| **Summe** | **22** |

Karten mit Bild: 0.


## Konzepte → Karten

Gewicht: 3 = in vielen Aufgaben gebraucht, 2 = mehrfach, 1 = selten. F. = Seite im Skript-PDF, Aufg. = Aufgabe im Ordner Informatik-1---Aufgaben-und-Beispiele.

| Konzept | Gewicht | Quelle | Karten | Typen |
|---|---:|---|---|---|
| if/else: Bedingung, Doppelpunkt, eingerückter Block, else optional | 3 | F. 112–116 · Aufg. 3.1, 3.5 | K04.001, K04.002, K04.003, K04.004, K04.005 | 4 |
| if/elif/else-Kette: nur der erste wahre Zweig läuft, Reihenfolge der Bedingungen | 3 | F. 115 · Aufg. 3.3, 3.4, 3.5 | K04.006, K04.007, K04.008, K04.009 | 4 |
| Einrückung bestimmt die Blockzugehörigkeit, IndentationError | 3 | F. 117 · Aufg. 3.3 | K04.010, K04.011, K04.012, K04.013, K04.014 | 3 |
| Verschachtelte Verzweigungen | 2 | F. 118 · Aufg. 3.6 | K04.015, K04.016, K04.017 | 3 |
| Strings vergleichen (Groß-/Kleinschreibung, "3" ≠ 3) | 2 | Aufg. 3.5, 3.7 | K04.018, K04.019, K04.020 | 3 |
| Grundstrukturen: sequentiell, auswählend, iterativ, springend; Anweisung, Folge, Bedingung | 1 | F. 109–111 | K04.021, K04.022 | 2 |

## Karten-Index

| ID | Typ | Folien | Frage |
|---|---|---|---|
| K04.001 | code_ausgabe | F. 114 | Was gibt der Code aus? ```python druck = 7.5 if druck > 8:     print("Ventil öffnen") else:     print("Druck o |
| K04.002 | code_fehler | F. 114 | Der Code bricht beim Start ab. Welche Fehlerart meldet Python, und was fehlt? ```python temperatur = 95 if tem |
| K04.003 | code_schreiben | F. 114, 116 · Aufg. 3.5 | Schreib Code, der eine Drehzahl als Ganzzahl einliest und `Überdrehzahl!` ausgibt, wenn sie größer als 6000 is |
| K04.004 | begriff | F. 112, 115 | Was passiert bei einem `if` **ohne** `else`, wenn die Bedingung `False` ergibt? |
| K04.005 | begriff | F. 114 | Was bezeichnet das Skript als **„wahr“-Suite** und als **„falsch“-Suite** einer if-else-Anweisung? |
| K04.006 | code_ausgabe | F. 115 · Aufg. 3.3 | Was gibt der Code aus? ```python drehzahl = 4500 if drehzahl > 3000:     print("erhöht") elif drehzahl > 4000: |
| K04.007 | code_fehler | F. 115 · Aufg. 3.4 | Bei 95 °C soll nur `kritisch` erscheinen. Was gibt der Code aus, und was ist zu ändern? ```python temp = 95 if |
| K04.008 | code_schreiben | F. 115 · Aufg. 3.4 | Ordne eine Maßabweichung `abw` (in mm) ein: unter 0.1 → `gut`, unter 0.5 → `nacharbeiten`, sonst `Ausschuss`.  |
| K04.009 | begriff | F. 115 | Wie viele Zweige einer if/elif/else-Kette werden **höchstens** ausgeführt? |
| K04.010 | code_ausgabe | F. 117 · Aufg. 3.3 | Was gibt der Code aus? ```python menge = 40 if menge > 50:     menge -= 10     print(menge) menge += 5 print(m |
| K04.011 | code_ausgabe | F. 117 · Aufg. 3.3 | Was gibt der Code aus? Achte auf die Einrückung der Zeile `menge += 5`. ```python menge = 40 if menge > 50:    |
| K04.012 | code_fehler | F. 117 · Aufg. 3.3 | `Lüfter geprüft` soll **immer** erscheinen. Bei `temp = 85` fehlt die Meldung. Warum, und wie korrigierst du d |
| K04.013 | code_fehler | F. 117 | Welche Fehlermeldung erscheint? ```python spannung = 230     print(spannung) ``` |
| K04.014 | begriff | F. 117 | Welche Aufgabe hat die **Einrückung** in Python? |
| K04.015 | code_ausgabe | F. 118 · Aufg. 3.6 | Was gibt der Code aus? ```python modus = "auto" temp = 65 if modus == "auto":     if temp > 70:         print( |
| K04.016 | code_schreiben | F. 118 | Schreib mit **zwei verschachtelten** if-Anweisungen: Wenn die Maschine läuft (`laeuft = True`) und mehr als 10 |
| K04.017 | unterschied | F. 118 | Was ist der Unterschied zwischen `if a:` mit eingerücktem `if b:` und `if a and b:`? |
| K04.018 | code_ausgabe | Aufg. 3.5 | Was gibt der Code aus? ```python modus = "Auto" if modus == "auto":     print("Regelung aktiv") else:     prin |
| K04.019 | code_fehler | Aufg. 3.5 | Der Nutzer tippt `3`. Erwartet ist `Kalibrierung`. Was erscheint, und warum? ```python code = input() if code  |
| K04.020 | code_schreiben | Aufg. 3.5 | Schreib Code, der die Farbe der Signalleuchte einliest und den Zustand ausgibt: `grün` → `Betrieb`, `gelb` → ` |
| K04.021 | begriff | F. 109 | Zu welcher Grundstruktur gehört laut Skript eine **if-Anweisung**, zu welcher eine **Schleife** und zu welcher |
| K04.022 | unterschied | F. 111 | Was ist der Unterschied zwischen einer **Anweisung** und einer **Folge (Sequenz)**? |
