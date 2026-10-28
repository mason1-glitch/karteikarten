# Abdeckungsmatrix – Kapitel 9: Funktionen (def, return, Parameter, Gültigkeit)

Erzeugt mit `werkzeuge/karten.py` aus `ingenieurinformatik1/quellen/kap09_karten.yaml`. 42 Karten, 14 prüfbare Inhalte, 0 Wiederholungsfragen.

## Karten je Typ

| Typ | Anzahl |
|---|---:|
| Begriff ↔ Erklärung | 12 |
| Lückentext im Code | 2 |
| Was gibt der Code aus? | 16 |
| Finde den Fehler | 6 |
| Schreib Code, der … | 4 |
| Was ist der Unterschied …? | 2 |
| **Summe** | **42** |

Karten mit Bild: 0.


## Konzepte → Karten

Gewicht: 3 = in vielen Aufgaben gebraucht, 2 = mehrfach, 1 = selten. F. = Seite im Skript-PDF, Aufg. = Aufgabe im Ordner Informatik-1---Aufgaben-und-Beispiele.

| Konzept | Gewicht | Quelle | Karten | Typen |
|---|---:|---|---|---|
| Funktion definieren: def name(parameter): + eingerückter Rumpf | 3 | F. 171, 180 · Aufg. 5.1–5.6 | K09.001, K09.002, K09.003, K09.004 | 4 |
| Aufruf und Programmablauf: Definition läuft erst beim Aufruf, Sprung hin und zurück | 3 | F. 177–178 · Aufg. 5.2 | K09.005, K09.006, K09.007, K09.008 | 2 |
| return gibt einen Wert zurück und beendet die Funktion | 3 | F. 173, 180 · Aufg. 5.3, 5.5 | K09.003, K09.009, K09.010, K09.011, K09.012, K09.019 | 4 |
| print() vs. return; Funktion ohne return liefert None | 3 | F. 172 · Aufg. 5.3 | K09.013, K09.014, K09.015, K09.016 | 3 |
| Parameter: Anzahl und Reihenfolge beim Aufruf | 2 | F. 176 · Aufg. 5.1 | K09.017, K09.018, K09.019 | 3 |
| TypeError bei fehlenden oder zu vielen Argumenten | 2 | F. 176 · Aufg. 5.1 | K09.020, K09.021 | 2 |
| Erst definieren, dann aufrufen (NameError) | 2 | F. 175 · Aufg. 5.1 | K09.022, K09.023, K09.024 | 3 |
| Mehrere Rückgabewerte (return a, b) und Entpacken | 2 | Aufg. 5.2, 5.6 | K09.025, K09.026, K09.027 | 3 |
| Lokale Variablen: nur innerhalb der Funktion gültig | 2 | F. 182 · Aufg. 5.6 | K09.028, K09.029, K09.030 | 3 |
| Schlüsselwort global | 1 | F. 183 · Aufg. 5.6 | K09.031, K09.032 | 2 |
| Neuzuweisung eines Parameters ändert die Variable des Aufrufers nicht | 2 | F. 182 · Aufg. 5.6 | K09.027, K09.033, K09.034, K09.035, K09.036 | 4 |
| Prozedur, Funktion, Methode | 1 | F. 172–174 | K09.037, K09.038 | 2 |
| Wozu Funktionen: Wiederverwendung, Modularisierung (Refactoring) | 1 | F. 170 · Aufg. 5.3 | K09.039, K09.040 | 2 |
| Ablauf mit Trace-Ausgaben/Debugger verfolgen | 1 | F. 177–178 · Aufg. 5.2 | K09.007, K09.041, K09.042 | 2 |

## Annahmen

- Aufg. 5.6 erklärt, eine Funktion erhalte „eine Kopie des Wertes“. Die Karten formulieren genauer: Der Parameter ist eine eigene lokale Variable, eine Neuzuweisung wirkt nicht nach außen. Eine als „Ergänzung“ markierte Karte zeigt, dass eine Liste, die in der Funktion verändert wird (append), auch außen verändert ist.

## Karten-Index

| ID | Typ | Folien | Frage |
|---|---|---|---|
| K09.001 | code_ausgabe | F. 171 | Was gibt der Code aus? ```python def begruessung(name):     print("Hallo", name)  begruessung("Team") begruess |
| K09.002 | code_fehler | F. 171 | Der Code bricht beim Start ab. Welche Fehlerart meldet Python, und was fehlt? ```python def leistung(spannung, |
| K09.003 | code_schreiben | F. 171, 180 · Aufg. 5.3 | Schreib eine Funktion `kreisflaeche(d)`, die für den Durchmesser `d` die Fläche A = π · d² / 4 **zurückgibt**  |
| K09.004 | begriff | F. 171 | Aus welchen Teilen besteht die erste Zeile einer Funktionsdefinition, und was folgt darunter? |
| K09.005 | code_ausgabe | F. 178 · Aufg. 5.2 | Was gibt der Code aus? ```python def melden():     print("B")  print("A") melden() print("C") ``` |
| K09.006 | code_ausgabe | F. 178 · Aufg. 5.2 | Was gibt der Code aus? ```python def starten():     print("Motor startet")  print("Programm fertig") ``` |
| K09.007 | code_ausgabe | F. 178 · Aufg. 5.2 | Was gibt der Code aus? ```python def quadrat(x):     print("in quadrat")     return x * x  print("vorher") y = |
| K09.008 | begriff | F. 178 · Aufg. 5.2 | Was passiert im Programmablauf, wenn eine Funktion aufgerufen wird? |
| K09.009 | code_ausgabe | F. 180 | Was gibt der Code aus? ```python def volumen(l, b, h):     return l * b * h  v = volumen(2, 3, 4) print(v / 2) |
| K09.010 | code_ausgabe | F. 180 | Was gibt der Code aus? ```python def pruefe(wert):     if wert < 0:         return "negativ"     return "ok"   |
| K09.011 | code_luecke | F. 180 · Aufg. 5.5 | Die Funktion soll den Durchsatz **zurückgeben**. Ergänze das Schlüsselwort. ```python def durchsatz(stueck, st |
| K09.012 | begriff | F. 173, 180 | Was bewirkt `return wert` in einer Funktion? |
| K09.013 | code_ausgabe | Aufg. 5.3 | Was gibt der Code aus? ```python def addiere(a, b):     print(a + b)  ergebnis = addiere(3, 4) print("Rückgabe |
| K09.014 | code_fehler | Aufg. 5.3 | Was erscheint auf dem Bildschirm, und wie korrigierst du die Funktion? ```python def flaeche(b, h):     print( |
| K09.015 | unterschied | Aufg. 5.3 | Was ist der Unterschied zwischen `print(ergebnis)` und `return ergebnis` in einer Funktion? |
| K09.016 | code_ausgabe | Aufg. 5.3 | Was gibt der Code aus? ```python def teile(a, b):     if b == 0:         return None     return a / b  print(t |
| K09.017 | code_ausgabe | F. 176 · Aufg. 5.1 | Was gibt der Code aus? ```python def bewegen(richtung, tempo):     print(richtung, "mit", tempo)  bewegen(50,  |
| K09.018 | begriff | F. 176 | Was legt die Parameterliste in der def-Zeile fest, und was muss beim Aufruf übereinstimmen? |
| K09.019 | code_schreiben | F. 176 | Schreib eine Funktion `spannung(kraft, flaeche)`, die σ = F / A zurückgibt, und gib das Ergebnis für F = 500 N |
| K09.020 | code_fehler | F. 176 · Aufg. 5.1 | Welche Fehlermeldung erscheint? ```python def ventil(nr, zustand):     print("Ventil", nr, zustand)  ventil(3) |
| K09.021 | begriff | F. 176 · Aufg. 5.1 | Was bedeutet diese Fehlermeldung? ```text TypeError: ventil() takes 2 positional arguments but 3 were given `` |
| K09.022 | code_fehler | F. 175 · Aufg. 5.1 | Welche Fehlermeldung erscheint, und wie behebst du sie? ```python starten()  def starten():     print("Start") |
| K09.023 | code_ausgabe | F. 175 | Was gibt der Code aus? ```python def a():     b()  def b():     print("b läuft")  a() ``` |
| K09.024 | begriff | F. 175 | Welche Reihenfolge von Definition und Aufruf schreibt Python bei Funktionen vor, und welcher Fehler entsteht s |
| K09.025 | code_ausgabe | Aufg. 5.2, 5.6 | Was gibt der Code aus? ```python def zerlege(minuten):     return minuten // 60, minuten % 60  h, m = zerlege( |
| K09.026 | code_luecke | Aufg. 5.2 | Die Funktion liefert Start- und Endzeit. Ergänze die linke Seite, sodass beide Werte in eigenen Variablen land |
| K09.027 | code_schreiben | Aufg. 5.6 | Schreib eine Funktion `tausche(x, y)`, die beide Werte vertauscht **zurückgibt**, und vertausche damit `links  |
| K09.028 | code_ausgabe | F. 182 · Aufg. 5.6 | Was gibt der Code aus? ```python def kalibrieren():     offset = 5     print("innen:", offset)  offset = 0 kal |
| K09.029 | code_fehler | F. 182 | Welche Fehlermeldung erscheint? ```python def messen():     wert = 42  messen() print(wert) ``` |
| K09.030 | begriff | F. 182 | Was ist eine **lokale** Variable? |
| K09.031 | code_ausgabe | F. 183 · Aufg. 5.6 | Was gibt der Code aus? ```python zaehler = 0 def zaehlen():     global zaehler     zaehler += 1  zaehlen() zae |
| K09.032 | begriff | F. 183 · Aufg. 5.6 | Warum sollte man `global` sparsam einsetzen, und was ist die bessere Alternative? |
| K09.033 | code_ausgabe | Aufg. 5.6 | Was gibt der Code aus? ```python def verdopple(wert):     wert = wert * 2     return wert  temp = 80 verdopple |
| K09.034 | code_fehler | Aufg. 5.6 | Die Werte sollen getauscht werden. Was gibt der Code aus, und warum klappt es nicht? ```python def tausche(x,  |
| K09.035 | begriff | F. 182 · Aufg. 5.6 | Warum ändert `wert = wert * 2` in einer Funktion nicht die Variable, die der Aufrufer übergeben hat? |
| K09.036 | code_ausgabe | Aufg. 5.6 | **Ergänzung** (nicht im Skript): Was gibt der Code aus? ```python def anfuegen(liste):     liste.append(99)  w |
| K09.037 | unterschied | F. 172–174 | Was ist laut Skript der Unterschied zwischen einer **Prozedur** und einer **Funktion**, und was ist eine **Met |
| K09.038 | begriff | F. 174 | Ordne nach Skript zu: Ist `melden`, `doppelt` bzw. `append` eine Prozedur, eine Funktion oder eine Methode? `` |
| K09.039 | begriff | F. 170 | Welche Vorteile nennt das Skript für Funktionen? |
| K09.040 | code_schreiben | F. 170 · Aufg. 5.3 | Fasse die doppelte Berechnung in eine Funktion `volumen(masse, dichte)` zusammen, sodass dieselbe Ausgabe ents |
| K09.041 | begriff | F. 177, 178 · Aufg. 5.2 | Wie machst du sichtbar, in welcher Reihenfolge ein Programm mit Funktionen tatsächlich abläuft? |
| K09.042 | code_ausgabe | Aufg. 5.2 | Was gibt der Code aus? ```python def b():     print("  b") def a():     print("a Start")     b()     print("a  |
