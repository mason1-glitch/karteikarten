# Abdeckungsmatrix – Kapitel 1: Ein- und Ausgabe, Strings ausgeben, Kommentare

Erzeugt mit `werkzeuge/karten.py` aus `ingenieurinformatik1/quellen/kap01_karten.yaml`. 42 Karten, 12 prüfbare Inhalte, 0 Wiederholungsfragen.

## Karten je Typ

| Typ | Anzahl |
|---|---:|
| Begriff ↔ Erklärung | 9 |
| Lückentext im Code | 5 |
| Was gibt der Code aus? | 17 |
| Finde den Fehler | 5 |
| Schreib Code, der … | 3 |
| Was ist der Unterschied …? | 3 |
| **Summe** | **42** |

Karten mit Bild: 0.


## Konzepte → Karten

Gewicht: 3 = in vielen Aufgaben gebraucht, 2 = mehrfach, 1 = selten. F. = Seite im Skript-PDF, Aufg. = Aufgabe im Ordner Informatik-1---Aufgaben-und-Beispiele.

| Konzept | Gewicht | Quelle | Karten | Typen |
|---|---:|---|---|---|
| print() mit mehreren Argumenten (Leerzeichen dazwischen), Leerzeile mit print() | 3 | F. 48 · Aufg. 1.1, 2.3 | K01.001, K01.002, K01.003, K01.004, K01.009, K01.027 | 4 |
| print(..., end="") unterdrückt den Zeilenumbruch | 2 | F. 52 · Aufg. 1.3, 4.3 | K01.005, K01.006, K01.007 | 3 |
| Escape-Sequenz \n (Zeilenumbruch) | 2 | F. 52–53 · Aufg. 1.3, 1.4 | K01.008, K01.009, K01.010 | 2 |
| Escape-Sequenz \t (Tabulator) | 2 | F. 53 · Aufg. 1.3, 1.4 | K01.011, K01.012, K01.013, K01.018 | 3 |
| Steuerzeichen \r (Wagenrücklauf) und \b (Backspace) | 1 | F. 53 · Aufg. 1.3 | K01.014, K01.015, K01.016 | 2 |
| Anführungszeichen und Backslash im String: \", \', \\ | 1 | F. 69 | K01.017, K01.018 | 2 |
| input() liefert immer einen String; Prompt ohne Zeilenumbruch | 3 | F. 49, 52 · Aufg. 1.1, 1.2, 3.5 | K01.019, K01.020, K01.021, K01.022, K01.023 | 4 |
| String-Verkettung mit + (nur str + str, Leerzeichen selbst setzen) | 3 | F. 135 · Aufg. 1.1, 1.2 | K01.020, K01.024, K01.025, K01.026, K01.027 | 3 |
| String-Wiederholung mit * ("#" * 5) | 1 | Aufg. 1.3 | K01.028, K01.029 | 2 |
| f-Strings: Variablen und Ausdrücke in {} | 3 | F. 116, 178 · Aufg. 2.6–2.9, 3.2–3.8, 5.1–6.3 | K01.030, K01.031, K01.032, K01.033, K01.034, K01.035 | 4 |
| Formatangabe {wert:.2f} (Nachkommastellen, rundet) | 2 | Aufg. 3.11, 5.3 | K01.036, K01.037, K01.038, K01.039 | 3 |
| Kommentare: # einzeilig, """ mehrzeilig, auskommentieren | 2 | F. 59–60 · Aufg. 2.1 | K01.040, K01.041, K01.042 | 2 |

## Karten-Index

| ID | Typ | Folien | Frage |
|---|---|---|---|
| K01.001 | code_ausgabe | F. 48 · Aufg. 2.3 | Was gibt der Code aus? ```python spannung = 230 print("Spannung:", spannung, "V") ``` |
| K01.002 | code_ausgabe | F. 52 · Aufg. 1.3 | Was gibt der Code aus? ```python print("Messung 1") print() print("Messung 2") ``` |
| K01.003 | begriff | F. 48 | Was bezeichnet das Skript als **Parameterliste** einer Funktion, z. B. bei `print("Druck:", 2.5)`? |
| K01.004 | code_schreiben | F. 48 · Aufg. 2.3 | Gegeben ist `druck = 2.5`. Schreib **eine** print-Zeile ohne `+`, die Folgendes ausgibt: ```text Druck: 2.5 ba |
| K01.005 | code_ausgabe | F. 52 · Aufg. 1.3 | Was gibt der Code aus? ```python print("Lade", end="") print("...", end="") print("fertig") ``` |
| K01.006 | code_luecke | F. 52 · Aufg. 1.3 | Ergänze die Lücke, sodass genau `Status: OK` in **einer** Zeile erscheint. ```python print("Status:", end=___) |
| K01.007 | unterschied | F. 52 · Aufg. 1.3 | Was ist der Unterschied zwischen `print("A")` und `print("A", end="")`? |
| K01.008 | code_ausgabe | F. 53 · Aufg. 1.4 | Was gibt der Code aus? ```python print("Sensor A: OK\nSensor B: FEHLER") ``` |
| K01.009 | code_ausgabe | F. 48, 53 | Was gibt der Code aus? Achte auf jedes Leerzeichen. ```python print("Druck:\n", 3, "bar") ``` |
| K01.010 | begriff | F. 53 | Was ist eine **Escape-Sequenz** (Steuerzeichen) in einem String? |
| K01.011 | begriff | F. 53 · Aufg. 1.3, 1.4 | Was bewirkt `\t` in einem String? |
| K01.012 | code_luecke | F. 53 · Aufg. 1.4 | Ergänze das Steuerzeichen, sodass Bezeichnung und Wert durch einen **Tabulator** getrennt sind. ```python prin |
| K01.013 | code_fehler | F. 53 · Aufg. 1.4 | Gewünscht ist ein Tabulator zwischen `Strom:` und `OK`. Was gibt der Code stattdessen aus, und wo liegt der Fe |
| K01.014 | begriff | F. 53 · Aufg. 1.3 | Was bewirkt das Steuerzeichen `\r` (carriage return)? |
| K01.015 | begriff | F. 53 · Aufg. 1.3 | Was bewirkt das Steuerzeichen `\b` (backspace)? |
| K01.016 | code_luecke | F. 52, 53 · Aufg. 1.3 | Der Fortschritt soll sich auf **derselben Zeile** aktualisieren (`10 %`, dann `20 %` …). Ergänze das Steuerzei |
| K01.017 | code_ausgabe | F. 69 | Was gibt der Code aus? ```python print("Bauteil \"A7\" geprüft") ``` |
| K01.018 | code_fehler | F. 53, 69 | Gewünscht ist die Ausgabe `Ordner: C:\temp`. Warum klappt das nicht, und wie lautet die Korrektur? ```python p |
| K01.019 | begriff | F. 49 · Aufg. 1.2 | Welchen Datentyp liefert `input()` zurück, wenn der Nutzer `230` eintippt? |
| K01.020 | code_ausgabe | F. 49 · Aufg. 1.2 | Der Nutzer tippt nacheinander `12` und `5` ein (jeweils Enter). Was gibt der Code aus? ```python a = input() b |
| K01.021 | code_fehler | F. 49, 75 · Aufg. 1.2 | Der Nutzer tippt `40` (Länge in mm). Erwartet wird `80`. Was gibt der Code aus, und wie korrigierst du ihn? `` |
| K01.022 | code_schreiben | F. 49, 75 · Aufg. 3.5 | Schreib Code, der einen Druck in bar als **Kommazahl** einliest (Eingabeaufforderung `Druck in bar: `) und den |
| K01.023 | begriff | F. 52 | Warum steht die Eingabe des Nutzers direkt hinter dem Text von `input("Bitte Namen eingeben:")` und nicht in e |
| K01.024 | code_ausgabe | F. 135 | Was gibt der Code aus? ```python bauteil = "Welle" nummer = "07" print(bauteil + "-" + nummer) ``` |
| K01.025 | code_fehler | F. 135 · Aufg. 1.2 | Welche Fehlermeldung erscheint, und wie behebst du den Fehler? ```python drehzahl = 1500 print("Drehzahl: " +  |
| K01.026 | code_ausgabe | F. 135 · Aufg. 1.1 | Was gibt der Code aus? ```python name = "Presse" print("Maschine" + name + "aktiv") ``` |
| K01.027 | unterschied | F. 48, 135 | Was ist der Unterschied zwischen `print("Wert:", x)` und `print("Wert:" + str(x))`? |
| K01.028 | code_ausgabe | Aufg. 1.3 | Was gibt der Code aus? ```python print("#" * 4 + "." * 2) ``` |
| K01.029 | code_schreiben | Aufg. 1.3 | Schreib eine Zeile, die eine Trennlinie aus **20 Bindestrichen** ausgibt, ohne die Striche einzeln zu tippen. |
| K01.030 | code_ausgabe | Aufg. 2.6 | Was gibt der Code aus? ```python kraft = 250 flaeche = 50 print(f"Spannung: {kraft / flaeche} N/mm²") ``` |
| K01.031 | code_luecke | Aufg. 2.6 | Ergänze die Lücke, sodass `Sensor T3: 21.5 °C` ausgegeben wird. ```python sensor = "T3" wert = 21.5 print(___" |
| K01.032 | code_fehler | Aufg. 2.6 | Gewünscht ist `Temperatur: 85 °C`. Was erscheint stattdessen, und was fehlt? ```python temperatur = 85 print(" |
| K01.033 | code_ausgabe | Aufg. 2.9 | Was gibt der Code aus? ```python for i in range(2):     print(f"Messung {i + 1}") ``` |
| K01.034 | code_ausgabe | Aufg. 2.6 | Was gibt der Code aus? ```python name = "Fräse" text = f"""Maschine: {name} Status: OK""" print(text) ``` |
| K01.035 | begriff | Aufg. 2.6 | Was ist ein **f-String**? |
| K01.036 | code_ausgabe | Aufg. 3.11 | Was gibt der Code aus? ```python guthaben = 1234.5678 print(f"{guthaben:.2f} €") ``` |
| K01.037 | code_luecke | Aufg. 5.3 | Ergänze die Formatangabe, sodass `Volumen: 6.4 l` ausgegeben wird (eine Nachkommastelle). ```python volumen =  |
| K01.038 | code_ausgabe | Aufg. 3.11 | Was gibt der Code aus? ```python stueck = 7 print(f"{stueck:.2f}") ``` |
| K01.039 | unterschied | F. 75 · Aufg. 2.4, 3.11 | Was ist der Unterschied zwischen `int(9.99)` und `f"{9.99:.0f}"`? |
| K01.040 | code_ausgabe | F. 59, 60 · Aufg. 2.1 | Was gibt der Code aus? ```python # print("Start") print("Messung läuft")  # Status #print("Debug") ``` |
| K01.041 | begriff | F. 59 · Aufg. 2.1 | Was bedeutet es, eine Codezeile **auszukommentieren**? |
| K01.042 | code_ausgabe | F. 60 | Was gibt der Code aus? ```python """ print("Debug: Rohwerte") """ print("Messung gestartet") ``` |
