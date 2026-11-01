# Abdeckungsmatrix – Level-Kolloquium 3: Zeit, Zufall und Eingabe

Erzeugt mit `werkzeuge/karten.py` aus `ingenieurinformatik1/quellen/level3_karten.yaml`. 22 Karten, 10 prüfbare Inhalte, 0 Wiederholungsfragen.

## Karten je Typ

| Typ | Anzahl |
|---|---:|
| Klausurfalle | 3 |
| Begriff ↔ Erklärung | 2 |
| Lückentext im Code | 2 |
| Was gibt der Code aus? | 5 |
| Finde den Fehler | 3 |
| Schreib Code, der … | 2 |
| Was ist der Unterschied …? | 1 |
| Warum so? (Entscheidung begründen) | 3 |
| Trace-Tabelle (Werte Schritt für Schritt) | 1 |
| **Summe** | **22** |

Karten mit Bild: 0.


## Konzepte → Karten

Gewicht: 3 = in vielen Aufgaben gebraucht, 2 = mehrfach, 1 = selten. F. = Seite im Skript-PDF, Aufg. = Aufgabe im Ordner Informatik-1---Aufgaben-und-Beispiele.

| Konzept | Gewicht | Quelle | Karten | Typen |
|---|---:|---|---|---|
| import random / import time, Aufruf als modul.funktion() | 3 | F. 173, 178 | L3.001, L3.002 | 2 |
| random.randint(a, b): beide Grenzen möglich; Zufallselement per Index 0 … len - 1; random.seed | 3 | Aufg. 2.5, 2.9 | L3.003, L3.004, L3.005, L3.006 | 4 |
| time.sleep(s) pausiert; zufällige Wartezeit gegen Raten | 2 | Aufg. 1.3 | L3.001, L3.007 | 2 |
| time.time(): Sekunden seit 1.1.1970 als float; Dauer = Ende − Start | 3 | Ergänzung (Dozent: erlaubt, wenn erklärbar) | L3.008, L3.009, L3.010 | 3 |
| input() wartet auf Enter, liefert immer str; nur Enter → leerer String | 3 | F. 49, 52 | L3.011, L3.012, L3.013, L3.015 | 4 |
| Fehlstart: Enter im Eingabepuffer → input() kehrt sofort zurück (< 0,1 s); Grenze: kein Abbruch nach X s | 3 | Level-Konzept | L3.007, L3.014, L3.015, L3.019 | 2 |
| Eingabepuffer leeren: while-Schleife mit Startwert verwirft Enter unter 0,3 s | 2 | F. 125 · Level-Konzept | L3.016, L3.017 | 2 |
| Zeit ausgeben: f"{zeit:.3f}" rundet, int() schneidet ab, Umrechnung in ms | 2 | F. 116 · Aufg. 3.11 | L3.009, L3.020 | 2 |
| None als „kein Ergebnis“ (Fehlstart) und Prüfung mit is not None | 2 | Aufg. 5.3 | L3.021, L3.022 | 2 |
| Auswertung mit if/elif/else: Fehlstart, zu langsam, geschafft; Grenzfall genau auf dem Limit | 2 | F. 115 | L3.018, L3.019 | 2 |

## Annahmen

- Typische einfache Reaktionszeiten (rund 0,2–0,3 s) sind Allgemeinwissen, nicht aus dem Stoff; auf der Karte als Ergänzung markiert.
- Die Fehlstart-Schwelle 0,1 s ist die im Level-Konzept getestete Wahl, keine Vorgabe.

## Karten-Index

| ID | Typ | Folien | Frage |
|---|---|---|---|
| L3.001 | code_luecke | F. 173 · Aufg. 1.3, 2.5 | Ergänze so, dass das Programm 2 bis 5 s zufällig wartet. ```python ___ ___  time.sleep(random.randint(2, 5)) p |
| L3.002 | code_fehler | Aufg. 1.3 | Der Code bricht ab. Welche Meldung, und warum? ```python import time  sleep(1) print("weiter") ``` |
| L3.003 | begriff | Aufg. 2.5 | Was liefert `random.randint(2, 5)` – und welche Werte sind möglich? |
| L3.004 | code_fehler | F. 141 · Aufg. 2.5 | Das Programm stürzt bei 100 Runden fast sicher ab. Warum? ```python import random  richtungen = ["LINKS", "REC |
| L3.005 | code_schreiben | F. 141 · Aufg. 2.5 | Wähle zufällig ein Kommando aus `richtungen` und gib es aus – nur mit Mitteln aus dem Stoff. |
| L3.006 | code_ausgabe | Aufg. 2.9 | Was gibt der Code aus – und wofür ist das beim Testen deiner Stationen nützlich? ```python import random  rand |
| L3.007 | begruenden | Aufg. 1.3, 2.5 · Level-Konzept | Warum wartet der Lianen-Sprung `time.sleep(random.randint(2, 5))` und nicht immer genau 3 s? |
| L3.008 | begriff | Ergänzung (Dozent: erlaubt, wenn erklärbar) | Was liefert `time.time()`, und warum kannst du damit eine Reaktionszeit messen? |
| L3.009 | code_schreiben | Ergänzung (Dozent: erlaubt, wenn erklärbar) | Miss, wie lange der Spieler bis zum Enter braucht, und gib die Zeit mit drei Nachkommastellen aus. |
| L3.010 | falle | Ergänzung (Dozent: erlaubt, wenn erklärbar) | Was misst dieser Code wirklich – und was ist falsch? ```python import time  start = time.time()   # Ergänzung  |
| L3.011 | code_ausgabe | F. 49 | Der Spieler drückt bei „RUHIG“ nur Enter. Was gibt der Code aus? ```python antwort = input() print(antwort ==  |
| L3.012 | code_fehler | F. 49, 75 | Der Spieler tippt `1.0`. Warum bricht der Code ab, und wie behebst du es? ```python zeitlimit = input() dauer  |
| L3.013 | unterschied | F. 75 | Der Spieler tippt `2.5`. Was passiert bei `int(input())`, was bei `float(input())`? |
| L3.014 | begruenden | Level-Konzept | Warum wertest du eine Reaktion **unter 0,1 s** als Fehlstart? |
| L3.015 | falle | Level-Konzept | Warum kann dein Programm eine Eingabe nicht nach 1,5 s abbrechen, und wie prüfst du das Zeitlimit stattdessen? |
| L3.016 | trace | F. 125 · Level-Konzept | Im Puffer liegen 2 alte Enter, dann drückt der Spieler nach 1,2 s. Wie oft läuft die Schleife, welchen Wert ha |
| L3.017 | code_luecke | F. 125 | Warum muss vor der Schleife `dauer = 0` stehen? Ergänze die Lücken. ```python ___ while ___:     start = time. |
| L3.018 | code_ausgabe | F. 115 | Was gibt der Code aus? ```python def bewerten(reaktion, zeitlimit_s):     if reaktion < 0.1:         return "F |
| L3.019 | falle | F. 115 | Was gibt der Code für `reaktion = 0.05` aus – und was ist falsch daran? ```python reaktion = 0.05 if reaktion  |
| L3.020 | code_ausgabe | F. 116 · Aufg. 3.11 | Was gibt der Code aus? ```python reaktion = 0.4127 print(f"{reaktion:.3f} s") print(f"{reaktion * 1000:.0f} ms |
| L3.021 | code_ausgabe | Aufg. 5.3 | Was gibt der Code aus? ```python def auswerten(reaktion):     if reaktion < 0.1:         return None     retur |
| L3.022 | begruenden | Aufg. 5.3 | Warum gibt `reaktion_messen()` bei einem Fehlstart `None` zurück und nicht `0`? |
