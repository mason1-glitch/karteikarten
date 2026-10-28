# Abdeckung Konzept → Karten (alle Kapitel)

143 Konzepte, 438 Karten. Lücken (Konzept ohne Karte oder mit weniger als zwei Kartentypen): **0**.

| Kartentyp | Anzahl |
|---|---:|
| Was gibt der Code aus? | 158 |
| Begriff ↔ Erklärung | 87 |
| Finde den Fehler | 56 |
| Lückentext im Code | 53 |
| Schreib Code, der … | 49 |
| Was ist der Unterschied …? | 35 |

## Kapitel 1: Ein- und Ausgabe, Strings ausgeben, Kommentare – `kap01_ein-ausgabe.csv` (42 Karten)

| Konzept | Gewicht | Karten | Typen |
|---|---:|---|---|
| print() mit mehreren Argumenten (Leerzeichen dazwischen), Leerzeile mit print() | 3 | K01.001, K01.002, K01.003, K01.004, K01.009, K01.027 | Begriff ↔ Erklärung, Was gibt der Code aus?, Schreib Code, der …, Was ist der Unterschied …? |
| print(..., end="") unterdrückt den Zeilenumbruch | 2 | K01.005, K01.006, K01.007, K01.016 | Was gibt der Code aus?, Lückentext im Code, Was ist der Unterschied …? |
| Escape-Sequenz \n (Zeilenumbruch) | 2 | K01.008, K01.009, K01.010 | Begriff ↔ Erklärung, Was gibt der Code aus? |
| Escape-Sequenz \t (Tabulator) | 2 | K01.011, K01.012, K01.013, K01.018 | Begriff ↔ Erklärung, Finde den Fehler, Lückentext im Code |
| Steuerzeichen \r (Wagenrücklauf) und \b (Backspace) | 1 | K01.014, K01.015, K01.016 | Begriff ↔ Erklärung, Lückentext im Code |
| Anführungszeichen und Backslash im String: \", \', \\ | 1 | K01.017, K01.018 | Was gibt der Code aus?, Finde den Fehler |
| input() liefert immer einen String; Prompt ohne Zeilenumbruch | 3 | K01.019, K01.020, K01.021, K01.022, K01.023 | Begriff ↔ Erklärung, Was gibt der Code aus?, Finde den Fehler, Schreib Code, der … |
| String-Verkettung mit + (nur str + str, Leerzeichen selbst setzen) | 3 | K01.020, K01.024, K01.025, K01.026, K01.027 | Was gibt der Code aus?, Finde den Fehler, Was ist der Unterschied …? |
| String-Wiederholung mit * ("#" * 5) | 1 | K01.028, K01.029 | Was gibt der Code aus?, Schreib Code, der … |
| f-Strings: Variablen und Ausdrücke in {} | 3 | K01.030, K01.031, K01.032, K01.033, K01.034, K01.035 | Begriff ↔ Erklärung, Was gibt der Code aus?, Finde den Fehler, Lückentext im Code |
| Formatangabe {wert:.2f} (Nachkommastellen, rundet) | 2 | K01.036, K01.037, K01.038, K01.039 | Was gibt der Code aus?, Lückentext im Code, Was ist der Unterschied …? |
| Kommentare: # einzeilig, """ mehrzeilig, auskommentieren | 2 | K01.040, K01.041, K01.042 | Begriff ↔ Erklärung, Was gibt der Code aus? |

## Kapitel 2: Variablen und Datentypen – `kap02_variablen-datentypen.csv` (46 Karten)

| Konzept | Gewicht | Karten | Typen |
|---|---:|---|---|
| Variable, Zuweisung mit =, Initialisierung, Reihenfolge der Zuweisungen | 3 | K02.001, K02.002, K02.003, K02.004, K02.005 | Begriff ↔ Erklärung, Was gibt der Code aus?, Finde den Fehler |
| Regeln für Bezeichner, Groß-/Kleinschreibung, reservierte Schlüsselwörter | 2 | K02.006, K02.007, K02.008 | Begriff ↔ Erklärung, Was ist der Unterschied …? |
| Standarddatentypen int, float, str, bool | 3 | K02.009, K02.010, K02.011, K02.012, K02.013 | Begriff ↔ Erklärung, Was gibt der Code aus?, Schreib Code, der …, Was ist der Unterschied …? |
| type() gibt den Datentyp aus (<class 'int'> …) | 2 | K02.009, K02.014, K02.015, K02.016 | Was gibt der Code aus?, Lückentext im Code |
| Datentyp ändert sich mit dem zugewiesenen Wert (keine Deklaration wie in C++) | 1 | K02.017, K02.018 | Was gibt der Code aus?, Was ist der Unterschied …? |
| / liefert immer float (auch 1500 / 2) | 3 | K02.019, K02.020, K02.021, K02.022 | Begriff ↔ Erklärung, Was gibt der Code aus?, Finde den Fehler |
| Implizite Typumwandlung: int mit float → float, int * int bleibt int | 2 | K02.022, K02.023, K02.024, K02.025 | Begriff ↔ Erklärung, Was gibt der Code aus? |
| int(): String → Ganzzahl, float → Ganzzahl (schneidet ab, rundet nicht) | 3 | K02.026, K02.027, K02.028, K02.029, K02.037 | Was gibt der Code aus?, Finde den Fehler, Lückentext im Code |
| float(): String → Kommazahl, Punkt statt Komma | 3 | K02.030, K02.031, K02.032, K02.033 | Was gibt der Code aus?, Finde den Fehler, Schreib Code, der … |
| str(): Zahl → Text (z. B. für Verkettung) | 2 | K02.034, K02.035, K02.036 | Begriff ↔ Erklärung, Was gibt der Code aus?, Lückentext im Code |
| ValueError bei ungültiger Umwandlung (int("72.4"), float("72,4")) | 2 | K02.031, K02.037, K02.038 | Begriff ↔ Erklärung, Finde den Fehler |
| Rundungsfehler bei Gleitkommazahlen (0.1 + 0.2, 85.0 - 72.4) | 2 | K02.039, K02.040, K02.041 | Begriff ↔ Erklärung, Was gibt der Code aus? |
| bool: True/False, Vergleiche liefern bool | 2 | K02.014, K02.042, K02.043, K02.044 | Begriff ↔ Erklärung, Was gibt der Code aus?, Lückentext im Code |
| Syntax und Semantik | 1 | K02.045, K02.046 | Begriff ↔ Erklärung, Was ist der Unterschied …? |

## Kapitel 3: Operatoren und Zahlensysteme – `kap03_operatoren.csv` (45 Karten)

| Konzept | Gewicht | Karten | Typen |
|---|---:|---|---|
| Arithmetische Operatoren + - * / // % ** | 3 | K03.001, K03.002, K03.003 | Was gibt der Code aus?, Schreib Code, der …, Was ist der Unterschied …? |
| Ganzzahldivision // (abrunden), Ergebnis-Typ | 3 | K03.002, K03.003, K03.004, K03.005, K03.006, K03.007 | Begriff ↔ Erklärung, Was gibt der Code aus?, Lückentext im Code, Schreib Code, der …, Was ist der Unterschied …? |
| Modulo %: Rest, Teilbarkeit (x % n == 0), gerade/ungerade | 3 | K03.003, K03.006, K03.008, K03.009, K03.010, K03.011 | Begriff ↔ Erklärung, Was gibt der Code aus?, Lückentext im Code, Schreib Code, der … |
| Ziffern einer Zahl mit // und % zerlegen (Quersumme) | 2 | K03.012, K03.013, K03.014 | Was gibt der Code aus?, Lückentext im Code, Schreib Code, der … |
| Potenz ** | 1 | K03.015, K03.016 | Was gibt der Code aus?, Schreib Code, der … |
| Vergleichsoperatoren == != < > <= >= liefern bool; int und float vergleichbar, str und int nicht | 3 | K03.017, K03.018, K03.019, K03.020 | Begriff ↔ Erklärung, Was gibt der Code aus?, Finde den Fehler |
| = (Zuweisung) vs. == (Vergleich) | 3 | K03.021, K03.022, K03.023 | Was gibt der Code aus?, Finde den Fehler, Was ist der Unterschied …? |
| Logische Operatoren and, or, not | 3 | K03.024, K03.025, K03.026, K03.027, K03.028 | Was gibt der Code aus?, Finde den Fehler, Schreib Code, der …, Was ist der Unterschied …? |
| Rangfolge: ** vor * / // % vor + -, Klammern | 2 | K03.015, K03.029, K03.030, K03.031, K03.032 | Begriff ↔ Erklärung, Was gibt der Code aus?, Finde den Fehler |
| Rangfolge: Arithmetik vor Vergleich vor not vor and vor or | 2 | K03.033, K03.034, K03.035 | Begriff ↔ Erklärung, Was gibt der Code aus?, Finde den Fehler |
| Kurzschlussauswertung (Short-Circuit) bei or/and | 1 | K03.036, K03.037 | Begriff ↔ Erklärung, Was gibt der Code aus? |
| Erweiterte Zuweisung += -= *= //= | 2 | K03.038, K03.039, K03.040 | Begriff ↔ Erklärung, Was gibt der Code aus?, Finde den Fehler |
| Binärsystem: Dezimal ↔ Binär (fortgesetzte Division durch 2) | 1 | K03.041, K03.042, K03.043 | Begriff ↔ Erklärung, Was gibt der Code aus? |
| Hexadezimalsystem (Nibble, 0–9/A–F, 0x-Schreibweise) | 1 | K03.044, K03.045 | Begriff ↔ Erklärung, Was gibt der Code aus? |

## Kapitel 4: Verzweigungen (if, elif, else) und Einrückung – `kap04_verzweigungen.csv` (22 Karten)

| Konzept | Gewicht | Karten | Typen |
|---|---:|---|---|
| if/else: Bedingung, Doppelpunkt, eingerückter Block, else optional | 3 | K04.001, K04.002, K04.003, K04.004, K04.005 | Begriff ↔ Erklärung, Was gibt der Code aus?, Finde den Fehler, Schreib Code, der … |
| if/elif/else-Kette: nur der erste wahre Zweig läuft, Reihenfolge der Bedingungen | 3 | K04.006, K04.007, K04.008, K04.009 | Begriff ↔ Erklärung, Was gibt der Code aus?, Finde den Fehler, Schreib Code, der … |
| Einrückung bestimmt die Blockzugehörigkeit, IndentationError | 3 | K04.010, K04.011, K04.012, K04.013, K04.014 | Begriff ↔ Erklärung, Was gibt der Code aus?, Finde den Fehler |
| Verschachtelte Verzweigungen | 2 | K04.015, K04.016, K04.017 | Was gibt der Code aus?, Schreib Code, der …, Was ist der Unterschied …? |
| Strings vergleichen (Groß-/Kleinschreibung, "3" ≠ 3) | 2 | K04.018, K04.019, K04.020 | Was gibt der Code aus?, Finde den Fehler, Schreib Code, der … |
| Grundstrukturen: sequentiell, auswählend, iterativ, springend; Anweisung, Folge, Bedingung | 1 | K04.021, K04.022 | Begriff ↔ Erklärung, Was ist der Unterschied …? |

## Kapitel 5: Schleifen (while, for, range, break, continue) – `kap05_schleifen.csv` (44 Karten)

| Konzept | Gewicht | Karten | Typen |
|---|---:|---|---|
| while-Schleife: läuft, solange die Bedingung wahr ist; Zähler | 3 | K05.001, K05.002, K05.003, K05.004, K05.005, K05.018 | Begriff ↔ Erklärung, Was gibt der Code aus?, Lückentext im Code, Schreib Code, der …, Was ist der Unterschied …? |
| Endlosschleife (Bedingung bleibt wahr, Zähler vergessen) | 2 | K05.006, K05.007, K05.008 | Begriff ↔ Erklärung, Finde den Fehler, Lückentext im Code |
| while mit zwei Bedingungen (and) und Auswertung nach der Schleife | 2 | K05.009, K05.010, K05.011 | Begriff ↔ Erklärung, Was gibt der Code aus?, Lückentext im Code |
| Eingabe wiederholen, bis sie passt (Startwert vor der Schleife) | 2 | K05.012, K05.013, K05.014 | Begriff ↔ Erklärung, Was gibt der Code aus?, Schreib Code, der … |
| for-Schleife über Liste/String; Schleifensteuerung und -rumpf | 3 | K05.015, K05.016, K05.017, K05.018, K05.019 | Begriff ↔ Erklärung, Was gibt der Code aus?, Schreib Code, der …, Was ist der Unterschied …? |
| range(stop), range(start, stop, schritt): Endwert ausgeschlossen | 3 | K05.020, K05.021, K05.022, K05.023, K05.024, K05.025, K05.028 | Begriff ↔ Erklärung, Was gibt der Code aus?, Finde den Fehler, Lückentext im Code |
| range mit negativer Schrittweite (rückwärts zählen) | 1 | K05.026, K05.027 | Was gibt der Code aus?, Lückentext im Code |
| Summe/Zähler/Zinseszins in der Schleife (Startwert vor der Schleife) | 3 | K05.028, K05.029, K05.030, K05.031, K05.032 | Was gibt der Code aus?, Finde den Fehler, Schreib Code, der … |
| break beendet die Schleife sofort | 2 | K05.033, K05.034, K05.035, K05.037 | Begriff ↔ Erklärung, Was gibt der Code aus?, Schreib Code, der …, Was ist der Unterschied …? |
| continue überspringt den Rest des Durchlaufs | 2 | K05.036, K05.037, K05.038 | Was gibt der Code aus?, Lückentext im Code, Was ist der Unterschied …? |
| Merker-Variable (gefunden = False) über die Schleife hinweg | 2 | K05.039, K05.040, K05.041 | Was gibt der Code aus?, Finde den Fehler, Schreib Code, der … |
| Ablauf verfolgen: Durchläufe zählen, Werte nach der Schleife | 2 | K05.002, K05.042, K05.043, K05.044 | Begriff ↔ Erklärung, Was gibt der Code aus? |

## Kapitel 6: Zeichenketten – Index, Slicing, find, replace, count – `kap06_strings.csv` (33 Karten)

| Konzept | Gewicht | Karten | Typen |
|---|---:|---|---|
| len() – Anzahl der Zeichen (Leerzeichen zählen mit) | 3 | K06.001, K06.002, K06.003, K06.004, K06.008 | Was gibt der Code aus?, Lückentext im Code, Schreib Code, der … |
| Zugriff s[i]: Index ab 0, s[-1] letztes Zeichen | 3 | K06.003, K06.005, K06.006, K06.007, K06.008 | Begriff ↔ Erklärung, Was gibt der Code aus?, Lückentext im Code |
| IndexError: string index out of range | 1 | K06.009, K06.010 | Begriff ↔ Erklärung, Finde den Fehler |
| Slicing s[von:bis] (bis ausgeschlossen, Grenzen weglassbar) | 2 | K06.011, K06.012, K06.013, K06.014, K06.015 | Begriff ↔ Erklärung, Was gibt der Code aus?, Lückentext im Code, Schreib Code, der … |
| Slicing mit Schrittweite s[von:bis:schritt] | 1 | K06.016, K06.017 | Was gibt der Code aus?, Lückentext im Code |
| find(): Startposition, -1 wenn nicht gefunden, Suche ab Position | 2 | K06.018, K06.019, K06.020, K06.021 | Begriff ↔ Erklärung, Was gibt der Code aus?, Schreib Code, der … |
| replace(): ersetzt alle Vorkommen, liefert neuen String, verkettbar | 2 | K06.022, K06.023, K06.024, K06.025 | Was gibt der Code aus?, Finde den Fehler, Lückentext im Code |
| count(): Vorkommen zählen (Groß-/Kleinschreibung beachten) | 2 | K06.026, K06.027, K06.028 | Was gibt der Code aus?, Schreib Code, der … |
| Strings sind unveränderlich (Ergebnis neu zuweisen) | 1 | K06.023, K06.029, K06.030 | Begriff ↔ Erklärung, Finde den Fehler |
| Strings mit find() und Slicing zerlegen und neu zusammensetzen | 2 | K06.021, K06.031, K06.032, K06.033 | Begriff ↔ Erklärung, Was gibt der Code aus?, Schreib Code, der … |

## Kapitel 7: Listen, 2D-Listen und Tupel – `kap07_listen.csv` (51 Karten)

| Konzept | Gewicht | Karten | Typen |
|---|---:|---|---|
| Liste anlegen (eckige Klammern, gemischte Typen, leere Liste) | 3 | K07.001, K07.002, K07.003, K07.004 | Begriff ↔ Erklärung, Was gibt der Code aus?, Schreib Code, der …, Was ist der Unterschied …? |
| Element lesen/ändern über den Index, IndexError | 3 | K07.005, K07.006, K07.007, K07.008 | Was gibt der Code aus?, Finde den Fehler, Lückentext im Code |
| append(): Element am Ende anfügen (liefert None) | 2 | K07.009, K07.010, K07.011, K07.013 | Was gibt der Code aus?, Finde den Fehler, Schreib Code, der …, Was ist der Unterschied …? |
| insert(pos, wert): an Position einfügen | 2 | K07.012, K07.013, K07.014 | Was gibt der Code aus?, Lückentext im Code, Was ist der Unterschied …? |
| pop(index): Element an Position entfernen und zurückgeben | 2 | K07.015, K07.016, K07.017, K07.020 | Was gibt der Code aus?, Finde den Fehler, Was ist der Unterschied …? |
| remove(wert): erstes passendes Element löschen | 2 | K07.018, K07.019, K07.020 | Was gibt der Code aus?, Finde den Fehler, Was ist der Unterschied …? |
| index(wert): Position eines Werts | 1 | K07.021, K07.022 | Was gibt der Code aus?, Schreib Code, der … |
| count(), sort(), reverse(), clear() | 1 | K07.023, K07.024 | Was gibt der Code aus?, Lückentext im Code |
| sort(key=funktion, reverse=…): nach eigenem Kriterium sortieren | 1 | K07.025, K07.026 | Begriff ↔ Erklärung, Was gibt der Code aus? |
| Liste durchlaufen: for x in liste / for i in range(len(liste)) | 3 | K07.027, K07.028, K07.029, K07.030 | Was gibt der Code aus?, Finde den Fehler, Schreib Code, der …, Was ist der Unterschied …? |
| in: prüfen, ob ein Wert in der Liste ist | 1 | K07.031, K07.032 | Was gibt der Code aus?, Lückentext im Code |
| enumerate(): Index und Element zugleich | 1 | K07.033, K07.034 | Was gibt der Code aus?, Was ist der Unterschied …? |
| 2D-Liste: matrix[zeile][spalte] | 2 | K07.035, K07.036, K07.037, K07.038 | Begriff ↔ Erklärung, Was gibt der Code aus?, Lückentext im Code |
| Verschachtelte Schleifen über eine 2D-Liste | 2 | K07.039, K07.040, K07.041 | Begriff ↔ Erklärung, Was gibt der Code aus?, Schreib Code, der … |
| List-Comprehension zum Anlegen von Listen/Rastern | 1 | K07.042, K07.043 | Was gibt der Code aus?, Lückentext im Code |
| Benutzereingabe ab 1 → Index ab 0 (reihe - 1) | 2 | K07.044, K07.045, K07.046 | Begriff ↔ Erklärung, Was gibt der Code aus?, Finde den Fehler |
| Tupel: unveränderlich, runde Klammern, Entpacken | 1 | K07.047, K07.048, K07.049 | Was gibt der Code aus?, Finde den Fehler, Was ist der Unterschied …? |
| Zuweisung kopiert keine Liste (Referenz) – .copy() | 1 | K07.050, K07.051 | Was gibt der Code aus?, Lückentext im Code |

## Kapitel 8: NumPy-Arrays – `kap08_numpy.csv` (18 Karten)

| Konzept | Gewicht | Karten | Typen |
|---|---:|---|---|
| import numpy as np, np.array() aus Liste (1D/2D), Ausgabeformat | 2 | K08.001, K08.002, K08.003, K08.004 | Begriff ↔ Erklärung, Was gibt der Code aus?, Finde den Fehler |
| np.zeros(), np.ones(), np.full() mit Form (zeilen, spalten) | 1 | K08.005, K08.006 | Was gibt der Code aus?, Lückentext im Code |
| Zugriff a[i, j], ganze Zeile a[i, :], ganze Spalte a[:, j] | 2 | K08.007, K08.008, K08.009 | Was gibt der Code aus?, Lückentext im Code, Was ist der Unterschied …? |
| Ganze Zeile/Spalte auf einen Wert setzen | 1 | K08.010, K08.011 | Was gibt der Code aus?, Schreib Code, der … |
| Elementweise Rechnung (Broadcasting), Arrays gleicher Form verrechnen | 2 | K08.012, K08.013, K08.014 | Was gibt der Code aus?, Finde den Fehler |
| NumPy-Array vs. Liste (gleicher Datentyp, Geschwindigkeit, * verhält sich anders) | 1 | K08.015, K08.016 | Was gibt der Code aus?, Was ist der Unterschied …? |
| Zuweisung erzeugt keine Kopie – .copy() | 1 | K08.017, K08.018 | Was gibt der Code aus?, Lückentext im Code |

## Kapitel 9: Funktionen (def, return, Parameter, Gültigkeit) – `kap09_funktionen.csv` (42 Karten)

| Konzept | Gewicht | Karten | Typen |
|---|---:|---|---|
| Funktion definieren: def name(parameter): + eingerückter Rumpf | 3 | K09.001, K09.002, K09.003, K09.004 | Begriff ↔ Erklärung, Was gibt der Code aus?, Finde den Fehler, Schreib Code, der … |
| Aufruf und Programmablauf: Definition läuft erst beim Aufruf, Sprung hin und zurück | 3 | K09.005, K09.006, K09.007, K09.008 | Begriff ↔ Erklärung, Was gibt der Code aus? |
| return gibt einen Wert zurück und beendet die Funktion | 3 | K09.003, K09.009, K09.010, K09.011, K09.012, K09.019 | Begriff ↔ Erklärung, Was gibt der Code aus?, Lückentext im Code, Schreib Code, der … |
| print() vs. return; Funktion ohne return liefert None | 3 | K09.013, K09.014, K09.015, K09.016 | Was gibt der Code aus?, Finde den Fehler, Was ist der Unterschied …? |
| Parameter: Anzahl und Reihenfolge beim Aufruf | 2 | K09.017, K09.018, K09.019 | Begriff ↔ Erklärung, Was gibt der Code aus?, Schreib Code, der … |
| TypeError bei fehlenden oder zu vielen Argumenten | 2 | K09.020, K09.021 | Begriff ↔ Erklärung, Finde den Fehler |
| Erst definieren, dann aufrufen (NameError) | 2 | K09.022, K09.023, K09.024 | Begriff ↔ Erklärung, Was gibt der Code aus?, Finde den Fehler |
| Mehrere Rückgabewerte (return a, b) und Entpacken | 2 | K09.025, K09.026, K09.027 | Was gibt der Code aus?, Lückentext im Code, Schreib Code, der … |
| Lokale Variablen: nur innerhalb der Funktion gültig | 2 | K09.028, K09.029, K09.030 | Begriff ↔ Erklärung, Was gibt der Code aus?, Finde den Fehler |
| Schlüsselwort global | 1 | K09.031, K09.032 | Begriff ↔ Erklärung, Was gibt der Code aus? |
| Neuzuweisung eines Parameters ändert die Variable des Aufrufers nicht | 2 | K09.027, K09.033, K09.034, K09.035, K09.036 | Begriff ↔ Erklärung, Was gibt der Code aus?, Finde den Fehler, Schreib Code, der … |
| Prozedur, Funktion, Methode | 1 | K09.037, K09.038 | Begriff ↔ Erklärung, Was ist der Unterschied …? |
| Wozu Funktionen: Wiederverwendung, Modularisierung (Refactoring) | 1 | K09.039, K09.040 | Begriff ↔ Erklärung, Schreib Code, der … |
| Ablauf mit Trace-Ausgaben/Debugger verfolgen | 1 | K09.007, K09.041, K09.042 | Begriff ↔ Erklärung, Was gibt der Code aus? |

## Kapitel 10: Bibliotheken – import, math, random, time, datetime, qrcode – `kap10_bibliotheken.csv` (27 Karten)

| Konzept | Gewicht | Karten | Typen |
|---|---:|---|---|
| import modul, Aufruf modul.funktion(), fehlender Import → NameError | 3 | K10.001, K10.002, K10.003, K10.004 | Begriff ↔ Erklärung, Was gibt der Code aus?, Finde den Fehler, Lückentext im Code |
| import … as … (np, pd, plt) und from … import … | 2 | K10.005, K10.006, K10.007 | Was gibt der Code aus?, Lückentext im Code, Was ist der Unterschied …? |
| math.sqrt, math.pi, math.ceil (aufrunden) | 2 | K10.001, K10.007, K10.008, K10.009, K10.010 | Was gibt der Code aus?, Schreib Code, der …, Was ist der Unterschied …? |
| random.randint(a, b) – beide Grenzen eingeschlossen | 2 | K10.011, K10.012, K10.013, K10.014 | Begriff ↔ Erklärung, Lückentext im Code, Schreib Code, der …, Was ist der Unterschied …? |
| time.sleep(sekunden) – Programm anhalten | 2 | K10.015, K10.016 | Begriff ↔ Erklärung, Lückentext im Code |
| Zeit formatieren mit strftime: %d %m %Y %H %M %S | 2 | K10.017, K10.018, K10.019, K10.020, K10.022 | Begriff ↔ Erklärung, Was gibt der Code aus?, Finde den Fehler, Lückentext im Code, Was ist der Unterschied …? |
| datetime.datetime.now() und .strftime() | 2 | K10.021, K10.022, K10.023 | Lückentext im Code, Schreib Code, der …, Was ist der Unterschied …? |
| Bibliotheken installieren (pip install) vs. importieren | 1 | K10.024, K10.025 | Begriff ↔ Erklärung, Was ist der Unterschied …? |
| qrcode.make(text) und display() im Notebook | 1 | K10.026, K10.027 | Begriff ↔ Erklärung, Schreib Code, der … |

## Kapitel 11: Dateien öffnen, lesen, schreiben – `kap11_dateien.csv` (24 Karten)

| Konzept | Gewicht | Karten | Typen |
|---|---:|---|---|
| open(pfad, modus): "r", "w", "a"; ohne Modus "r" | 2 | K11.001, K11.002, K11.003 | Begriff ↔ Erklärung, Finde den Fehler, Lückentext im Code |
| read() ganze Datei, read(n) n Zeichen | 2 | K11.004, K11.005, K11.006 | Was gibt der Code aus?, Was ist der Unterschied …? |
| Zeilenweise lesen mit for zeile in datei; jede Zeile endet mit \n | 2 | K11.007, K11.008, K11.009 | Begriff ↔ Erklärung, Was gibt der Code aus?, Finde den Fehler |
| readlines() (Liste der Zeilen) und readline() | 1 | K11.010, K11.011 | Was gibt der Code aus?, Was ist der Unterschied …? |
| write(): nur Strings, kein automatischer Zeilenumbruch | 2 | K11.012, K11.013, K11.014 | Was gibt der Code aus?, Finde den Fehler, Schreib Code, der … |
| "w" überschreibt, "a" hängt an | 2 | K11.002, K11.015, K11.016, K11.017 | Was gibt der Code aus?, Lückentext im Code, Was ist der Unterschied …? |
| close(): Datei schließen; danach kein Zugriff mehr | 2 | K11.018, K11.019 | Begriff ↔ Erklärung, Finde den Fehler |
| Relativer Pfad (../Daten/…) und FileNotFoundError | 1 | K11.020, K11.021 | Begriff ↔ Erklärung, Finde den Fehler |
| Dateiinhalt zeilenweise auswerten (float(zeile), zählen, ersetzen) | 2 | K11.022, K11.023, K11.024 | Was gibt der Code aus?, Schreib Code, der … |

## Kapitel 12: CSV-Dateien und pandas – `kap12_pandas.csv` (17 Karten)

| Konzept | Gewicht | Karten | Typen |
|---|---:|---|---|
| CSV-Format: ein Datensatz pro Zeile, Trennzeichen, Kopfzeile | 1 | K12.001, K12.002 | Begriff ↔ Erklärung, Was gibt der Code aus? |
| pd.read_csv() → DataFrame; Spaltennamen exakt (KeyError) | 2 | K12.002, K12.003, K12.004, K12.005 | Begriff ↔ Erklärung, Was gibt der Code aus?, Finde den Fehler, Lückentext im Code |
| DataFrame aus Dictionary, Spalte df["Name"], len(df), head() | 2 | K12.006, K12.007, K12.008 | Begriff ↔ Erklärung, Was gibt der Code aus?, Lückentext im Code |
| Zeilen filtern: df[df["Spalte"] > wert] | 2 | K12.009, K12.010, K12.011 | Was gibt der Code aus?, Finde den Fehler, Lückentext im Code |
| sort_values(by=…, ascending=…) | 2 | K12.012, K12.013 | Was gibt der Code aus?, Lückentext im Code |
| groupby("A")["B"].mean() – Mittelwert je Gruppe | 1 | K12.014, K12.015 | Begriff ↔ Erklärung, Was gibt der Code aus? |
| value_counts() – Häufigkeit jedes Werts | 1 | K12.016, K12.017 | Begriff ↔ Erklärung, Was gibt der Code aus? |

## Kapitel 13: Daten visualisieren mit matplotlib und plotly – `kap13_visualisierung.csv` (27 Karten)

| Konzept | Gewicht | Karten | Typen |
|---|---:|---|---|
| import matplotlib.pyplot as plt, plt.plot(x, y), plt.show() | 2 | K13.001, K13.002, K13.003 | Begriff ↔ Erklärung, Lückentext im Code, Schreib Code, der … |
| Linienstil: Formatstring "b-o", color, linestyle, linewidth, marker | 1 | K13.004, K13.005 | Was gibt der Code aus?, Lückentext im Code |
| title, xlabel, ylabel, grid – vor show() | 2 | K13.006, K13.007, K13.008 | Finde den Fehler, Lückentext im Code, Schreib Code, der … |
| label=… und plt.legend() | 1 | K13.009, K13.010 | Finde den Fehler, Schreib Code, der … |
| Balkendiagramm plt.bar(kategorien, werte) | 2 | K13.011, K13.012, K13.013 | Was gibt der Code aus?, Lückentext im Code, Schreib Code, der … |
| Histogramm plt.hist(daten, bins=…) | 1 | K13.014, K13.015 | Begriff ↔ Erklärung, Lückentext im Code |
| Streudiagramm plt.scatter(x, y) | 1 | K13.016, K13.017 | Schreib Code, der …, Was ist der Unterschied …? |
| Mehrere Diagramme: fig, (ax1, ax2) = plt.subplots(1, 2), ax.set_title, tight_layout | 1 | K13.018, K13.019 | Schreib Code, der …, Was ist der Unterschied …? |
| plt.savefig("datei.png", dpi=…) vor plt.show() | 1 | K13.020, K13.021 | Finde den Fehler, Lückentext im Code |
| x und y müssen gleich lang sein (ValueError) | 1 | K13.022, K13.023 | Begriff ↔ Erklärung, Finde den Fehler |
| plotly.express: px.line, px.scatter_3d(color=…), update_layout, fig.show() | 1 | K13.024, K13.025, K13.026, K13.027 | Begriff ↔ Erklärung, Lückentext im Code, Schreib Code, der …, Was ist der Unterschied …? |
