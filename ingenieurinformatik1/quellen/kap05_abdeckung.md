# Abdeckungsmatrix – Kapitel 5: Schleifen (while, for, range, break, continue)

Erzeugt mit `werkzeuge/karten.py` aus `ingenieurinformatik1/quellen/kap05_karten.yaml`. 43 Karten, 12 prüfbare Inhalte, 0 Wiederholungsfragen.

## Karten je Typ

| Typ | Anzahl |
|---|---:|
| Begriff ↔ Erklärung | 7 |
| Lückentext im Code | 5 |
| Was gibt der Code aus? | 16 |
| Finde den Fehler | 6 |
| Schreib Code, der … | 7 |
| Was ist der Unterschied …? | 2 |
| **Summe** | **43** |

Karten mit Bild: 0.


## Konzepte → Karten

Gewicht: 3 = in vielen Aufgaben gebraucht, 2 = mehrfach, 1 = selten. F. = Seite im Skript-PDF, Aufg. = Aufgabe im Ordner Informatik-1---Aufgaben-und-Beispiele.

| Konzept | Gewicht | Quelle | Karten | Typen |
|---|---:|---|---|---|
| while-Schleife: läuft, solange die Bedingung wahr ist; Zähler | 3 | F. 123, 125 · Aufg. 2.9, 3.7, 3.10 | K05.001, K05.002, K05.003, K05.004, K05.017 | 4 |
| Endlosschleife (Bedingung bleibt wahr, Zähler vergessen) | 2 | F. 126 | K05.005, K05.006, K05.007 | 2 |
| while mit zwei Bedingungen (and) und Auswertung nach der Schleife | 2 | Aufg. 3.7 | K05.008, K05.009, K05.010 | 3 |
| Eingabe wiederholen, bis sie passt (Startwert vor der Schleife) | 2 | F. 125 · Aufg. 3.7 | K05.011, K05.012, K05.013 | 3 |
| for-Schleife über Liste/String; Schleifensteuerung und -rumpf | 3 | F. 123, 143 · Aufg. 3.8, 4.2, 6.1 | K05.014, K05.015, K05.016, K05.017, K05.018 | 4 |
| range(stop), range(start, stop, schritt): Endwert ausgeschlossen | 3 | F. 128 · Aufg. 3.9, 3.11, 4.3 | K05.019, K05.020, K05.021, K05.022, K05.023, K05.024, K05.027 | 4 |
| range mit negativer Schrittweite (rückwärts zählen) | 1 | F. 129 | K05.025, K05.026 | 2 |
| Summe/Zähler/Zinseszins in der Schleife (Startwert vor der Schleife) | 3 | Aufg. 3.11, 6.1 | K05.027, K05.028, K05.029, K05.030, K05.031 | 3 |
| break beendet die Schleife sofort | 2 | Aufg. 3.8 | K05.032, K05.033, K05.034, K05.036 | 4 |
| continue überspringt den Rest des Durchlaufs | 2 | Aufg. 3.8 | K05.035, K05.036, K05.037 | 3 |
| Merker-Variable (gefunden = False) über die Schleife hinweg | 2 | Aufg. 4.4, 4.5 | K05.038, K05.039, K05.040 | 3 |
| Ablauf verfolgen: Durchläufe zählen, Werte nach der Schleife | 2 | Aufg. 3.8, 3.10, 5.2 | K05.002, K05.041, K05.042, K05.043 | 2 |

## Annahmen

- Aufgabennummern folgen den Dateinamen: Aufg. 3.7 = 03_7_Fabrikzugangssystem (in der Lösung als „Aufgabe 3.8“ betitelt), Aufg. 3.8 = 03_8_Fliessband_Steuerung (dort „Aufgabe 3.7“).
- Skript F. 182 sagt, eine Zuweisung „innerhalb einer Funktion oder einer Schleife“ habe außerhalb keine Wirkung. Für Funktionen stimmt das, für Schleifen nicht: Variablen aus Schleifen behalten ihren Wert (Karte zur Laufvariablen nach der Schleife).

## Karten-Index

| ID | Typ | Folien | Frage |
|---|---|---|---|
| K05.001 | code_ausgabe | F. 123, 125 | Was gibt der Code aus? ```python i = 0 while i < 3:     print(i)     i += 1 print("Ende", i) ``` |
| K05.002 | code_ausgabe | Aufg. 3.10 | Was gibt der Code aus? ```python wert = 54 schritte = 0 while wert % 3 == 0:     wert = wert // 3     schritte |
| K05.003 | code_schreiben | F. 125 | Ein Tank mit 1000 l verliert pro Stunde 10 % seines Inhalts. Schreib eine while-Schleife, die ausgibt, nach wi |
| K05.004 | code_luecke | F. 125 | Die Schleife soll laufen, **solange** die Temperatur kleiner als 25 ist. Ergänze den Operator. ```python tempe |
| K05.005 | code_fehler | F. 126 | Was passiert beim Ausführen, und welche Zeile fehlt? ```python zaehler = 0 while zaehler < 5:     print(zaehle |
| K05.006 | begriff | F. 126 | Was ist eine **Endlosschleife**, und wodurch entsteht sie bei while typischerweise? |
| K05.007 | code_fehler | F. 126 | Warum endet diese Schleife nie, und wie machst du sie sicher? ```python hub = 1 while hub != 10:     hub += 2  |
| K05.008 | code_ausgabe | Aufg. 3.7 | Was gibt der Code aus? ```python messungen = 0 stabil = False while not stabil and messungen < 3:     messunge |
| K05.009 | code_luecke | Aufg. 3.7 | Die Schleife soll weiterlaufen, solange die PIN **nicht** `4711` ist **und** weniger als 3 Versuche gemacht wu |
| K05.010 | begriff | Aufg. 3.7 | Eine Tankfüllung läuft mit `while fuellstand < soll and messungen < 10:` – sie endet also beim Sollfüllstand * |
| K05.011 | code_ausgabe | F. 125 · Aufg. 3.7 | Der Nutzer tippt nacheinander `WARN`, `FEHLER`, `OK`. Was gibt der Code aus? ```python status = "" while statu |
| K05.012 | code_schreiben | F. 125 | Schreib Code, der so lange eine Drehzahl (Ganzzahl) einliest, bis sie **größer als 0** ist, und sie dann ausgi |
| K05.013 | begriff | F. 125 · Aufg. 3.7 | Warum steht vor `while status != "OK":` die Zeile `status = ""`? |
| K05.014 | code_ausgabe | F. 143 | Was gibt der Code aus? ```python werte = [12.5, 13.0, 12.8] for w in werte:     print(w * 2) ``` |
| K05.015 | code_ausgabe | F. 143 | Was gibt der Code aus? ```python for zeichen in "AB3":     print(zeichen) ``` |
| K05.016 | code_schreiben | F. 143 · Aufg. 4.2 | Gegeben ist `durchmesser = [3.1, 2.9, 3.4]`. Gib jeden Wert mit der Einheit `mm` in einer eigenen Zeile aus (` |
| K05.017 | unterschied | F. 123, 125, 128 | Was ist der Unterschied zwischen einer **for**- und einer **while**-Schleife? |
| K05.018 | begriff | F. 123 | Aus welchen zwei Teilen besteht eine Schleife laut Skript, und was leistet jeder Teil? |
| K05.019 | code_ausgabe | F. 128 | Was gibt der Code aus? ```python for i in range(3):     print(i) ``` |
| K05.020 | code_ausgabe | F. 128 | Was gibt der Code aus? ```python for i in range(2, 11, 4):     print(i) ``` |
| K05.021 | code_luecke | F. 128 · Aufg. 3.9 | Ergänze die range-Argumente, sodass die Zahlen **1 bis 5** ausgegeben werden. ```python for i in range(___):   |
| K05.022 | code_fehler | F. 128 · Aufg. 3.11 | Ausgegeben werden sollen die Tage 1 bis 7. Was gibt der Code aus, und wie korrigierst du ihn? ```python for ta |
| K05.023 | begriff | F. 128 | Was bedeuten die drei Werte in `range(start, stop, schritt)`, und welche Standardwerte gelten? |
| K05.024 | code_fehler | F. 128 | Welche Fehlermeldung erscheint, und wie behebst du sie? ```python anzahl = 10 for i in range(anzahl / 2):      |
| K05.025 | code_ausgabe | F. 129 | Was gibt der Code aus? ```python for i in range(10, 0, -3):     print(i) ``` |
| K05.026 | code_luecke | F. 129 | Ergänze die Lücken für einen Countdown `5 4 3 2 1` (je eine Zeile). ```python for i in range(5, ___, ___):     |
| K05.027 | code_ausgabe | Aufg. 3.11 | Was gibt der Code aus? ```python summe = 0 for i in range(1, 5):     summe += i print(summe) ``` |
| K05.028 | code_schreiben | Aufg. 6.1 | Berechne mit einer for-Schleife den **Mittelwert** der Temperaturen `[20.5, 21.0, 19.5, 21.0]` und gib ihn aus |
| K05.029 | code_fehler | Aufg. 6.1 | Die Summe der Werte soll `15` sein. Was gibt der Code aus, und was ist falsch? ```python werte = [4, 6, 5] for |
| K05.030 | code_ausgabe | Aufg. 3.11 | Was gibt der Code aus? ```python restwert = 2000 for jahr in range(2):     restwert = restwert * 0.9 print(f"{ |
| K05.031 | code_schreiben | Aufg. 6.1 | Zähle mit einer Schleife, wie viele Werte in `[0.2, 0.7, 0.4, 0.9]` größer als 0.5 sind, und gib die Anzahl au |
| K05.032 | code_ausgabe | Aufg. 3.8 | Was gibt der Code aus? ```python for wert in [21, 22, 99, 23]:     if wert > 90:         print("Grenzwert:", w |
| K05.033 | begriff | Aufg. 3.8 | Was bewirkt `break` in einer Schleife? |
| K05.034 | code_schreiben | Aufg. 3.8 | Gib aus `werte = [80, 95, 120, 130]` den **ersten** Wert über 100 aus und brich die Suche danach ab. |
| K05.035 | code_ausgabe | Aufg. 3.8 | Was gibt der Code aus? ```python for nr in [1, 2, 3, 4]:     if nr % 2 == 0:         continue     print(nr) `` |
| K05.036 | unterschied | Aufg. 3.8 | Was ist der Unterschied zwischen `break` und `continue`? |
| K05.037 | code_luecke | Aufg. 3.8 | Negative Messwerte sollen übersprungen werden, die Schleife soll aber weiterlaufen. Ergänze die Lücke. ```pyth |
| K05.038 | code_ausgabe | Aufg. 4.4 | Was gibt der Code aus? ```python teile = ["Kolben", "Ventil", "Lager"] gefunden = False for t in teile:     if |
| K05.039 | code_fehler | Aufg. 4.4 | `Ventil` ist in der Liste, trotzdem erscheint `False`. Warum? ```python teile = ["Ventil", "Lager"] gefunden = |
| K05.040 | code_schreiben | Aufg. 4.5 | Prüfe mit einer Merker-Variablen, ob in `messwerte = [2.1, 2.3, -0.4, 2.2]` ein negativer Wert vorkommt, und g |
| K05.041 | code_ausgabe | Aufg. 3.10 | Was gibt der Code aus? Notiere `n` nach jedem Durchlauf. ```python n = 100 schritte = 0 while n > 1:     n = n |
| K05.042 | code_ausgabe | F. 182 | Was gibt der Code aus? ```python for t in range(0, 10, 3):  # Messzeit in s     letzte_zeit = t print(t, letzt |
| K05.043 | begriff | Aufg. 3.8, 5.2 | Wie findest du heraus, was eine Schleife Schritt für Schritt tut, **ohne** sie auszuführen? |
