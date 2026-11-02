# Abdeckungsmatrix – Level-Kolloquium 4: Mechaniken der Stationen

Erzeugt mit `werkzeuge/karten.py` aus `ingenieurinformatik1/quellen/level4_karten.yaml`. 32 Karten, 10 prüfbare Inhalte, 0 Wiederholungsfragen.

## Karten je Typ

| Typ | Anzahl |
|---|---:|
| Klausurfalle | 4 |
| Anwendung (Fall → Einordnung) | 1 |
| Was gibt der Code aus? | 12 |
| Finde den Fehler | 1 |
| Schreib Code, der … | 6 |
| Was ist der Unterschied …? | 1 |
| Warum so? (Entscheidung begründen) | 5 |
| Trace-Tabelle (Werte Schritt für Schritt) | 2 |
| **Summe** | **32** |

Karten mit Bild: 1.


## Konzepte → Karten

Gewicht: 3 = in vielen Aufgaben gebraucht, 2 = mehrfach, 1 = selten. F. = Seite im Skript-PDF, Aufg. = Aufgabe im Ordner Informatik-1---Aufgaben-und-Beispiele.

| Konzept | Gewicht | Quelle | Karten | Typen |
|---|---:|---|---|---|
| Folge als String aufbauen: folge += taste in einer for-Schleife; Zufallsindex | 3 | F. 135 · Level-Konzept | L4.001, L4.002, L4.003, L4.004, L4.030 | 3 |
| String/Liste durchlaufen: for zeichen in text, for i in range(len(text)), text[i] | 3 | F. 136, 143 | L4.003, L4.009, L4.010 | 2 |
| Strings mit == vergleichen: exakt (Groß/Klein, Leerzeichen); replace(" ", "") | 3 | F. 105, 138 | L4.007, L4.008, L4.028 | 2 |
| Verdecken mit print("\n" * 40): String-Wiederholung, \n ist ein Zeichen | 2 | F. 53, 135 | L4.005, L4.006 | 2 |
| Tippfehler zählen: IndexError bei zu kurzer Eingabe, Reihenfolge der Bedingungen bei or, Grenzen des Positionsvergleichs | 3 | Level-Konzept | L4.009, L4.010, L4.011, L4.012, L4.013, L4.014 | 4 |
| Zusammengesetzte Bedingung mit and (richtige Taste und schnell genug) | 2 | F. 106 · Level-Konzept | L4.015, L4.016, L4.028, L4.029 | 3 |
| 2D-Liste per List-Comprehension anlegen, raster[reihe][spalte], mit verschachtelten Schleifen und end ausgeben | 3 | F. 150–153 · Aufg. 4.3 | L4.017, L4.018, L4.019, L4.024, L4.032 | 3 |
| Spieler zählt ab 1, Python ab 0; Eingabe 0 → Index -1 ohne Fehler; Bereichsprüfung mit and | 3 | Aufg. 4.3–4.5 | L4.020, L4.021, L4.022, L4.031 | 4 |
| Raster mit range(len()) durchsuchen und Position ausgeben | 2 | F. 152 · Aufg. 4.4 | L4.023, L4.024 | 2 |
| Runden und Leben: for bei fester Rundenzahl, while mit zwei Bedingungen, break | 3 | F. 125, 128 · Aufg. 3.7, 3.8 | L4.004, L4.025, L4.026, L4.027 | 3 |

## Annahmen

- Dass `or` die rechte Seite nicht mehr auswertet, wenn die linke schon wahr ist (Kurzschluss), steht nicht im Skript (F. 106 zeigt nur Wahrheitstafeln); auf den Karten als Ergänzung markiert.
- `[[…] * 3] * 2` (Liste mal Zahl) ist nicht im Stoff; die Karte warnt davor und ist als Ergänzung markiert.

## Karten-Index

| ID | Typ | Folien | Frage |
|---|---|---|---|
| L4.001 | code_ausgabe | F. 135, 141 | Was gibt der Code aus? ```python tasten = ["a", "t", "f"] folge = "" for i in [2, 0, 0, 1]:     folge += taste |
| L4.002 | code_schreiben | F. 128, 135 · Aufg. 2.5 | Erzeuge eine zufällige Affen-Folge aus den Tasten `a`, `t`, `f` mit der Länge `laenge = 4`. |
| L4.003 | code_ausgabe | F. 143, 151 · Laborskript Dictionaries F. 6 | Was gibt der Code aus? ```python tiere = {"a": "Affe", "t": "Tukan", "f": "Frosch"} for taste in "taf":     pr |
| L4.004 | trace | F. 128, 151 | Welche Werte nimmt `laenge` an, wie oft läuft die innere Schleife jeweils, und was wird ausgegeben? ```python  |
| L4.005 | begruenden | F. 53, 135 · Level-Konzept | Wie verdeckst du die Affen-Folge, bevor der Spieler sie nachtippt, und warum so? |
| L4.006 | code_ausgabe | F. 53, 135, 136 | Was gibt der Code aus? ```python print("ab" * 3) print(len("\n" * 40)) print("-" * 5 + "/") ``` |
| L4.007 | falle | F. 105 | Was gibt der Code aus? ```python folge = "atf" print("atf" == folge) print("ATF" == folge) print("a t f" == fo |
| L4.008 | code_schreiben | F. 138 | Der Spieler soll die Folge auch mit Leerzeichen eintippen dürfen (`a t f`). Schreib den Vergleich nur mit Mitt |
| L4.009 | code_ausgabe | F. 136, 152 | Was gibt der Code aus? ```python spruch = "Zisch" eingabe = "Zosch" fehler = 0 for i in range(len(spruch)):    |
| L4.010 | code_fehler | F. 136 | Der Spieler tippt nur `Zis`. Warum stürzt der Code ab? ```python spruch = "Zisch" eingabe = "Zis" fehler = 0 f |
| L4.011 | code_ausgabe | F. 106, 136 | Was gibt der Code aus – und warum stürzt er jetzt nicht ab? (Ergänzung) ```python spruch = "Zisch" eingabe = " |
| L4.012 | falle | F. 106 | Gleiche Idee, Bedingungen vertauscht. Was passiert bei `eingabe = "Zis"`? (Ergänzung) ```python spruch = "Zisc |
| L4.013 | begruenden | Level-Konzept | Der Spieler vergisst bei `Zisch` nur das `i` und tippt `Zsch`. Dein Code meldet 4 Fehler. Wie erklärst du das  |
| L4.014 | code_ausgabe | F. 136 | Was gibt der Code aus? ```python spruch = "Zisch" eingabe = "Zischhh" fehler = 0 if len(eingabe) > len(spruch) |
| L4.015 | code_ausgabe | F. 106 | Was gibt der Code aus? ```python gegenrichtung = {"LINKS": ["d", "D"], "RUHIG": [""]} kommando = "LINKS" antwo |
| L4.016 | begruenden | Level-Konzept | Warum gibt es bei der Hängebrücke das Kommando „RUHIG“, bei dem nur Enter richtig ist? |
| L4.017 | code_ausgabe | F. 150, 153 | Was gibt der Code aus? ```python raster = [["o" for s in range(3)] for r in range(2)] print(raster) print(len( |
| L4.018 | code_ausgabe | F. 151 · Aufg. 4.3 | Was gibt der Code aus? ```python raster = [["o" for s in range(3)] for r in range(2)] raster[1][2] = "~" for r |
| L4.019 | falle | F. 153 | Warum legst du das Raster mit einer List-Comprehension an und nicht so? (Ergänzung) ```python raster = [["o"]  |
| L4.020 | anwendung | Aufg. 4.3, 4.5 | Der Spieler gibt **Reihe 3, Spalte 4** ein. Welches Feld liest dein Code, und was passiert bei Reihe 0? [Bild] |
| L4.021 | code_ausgabe | F. 141 | Was gibt der Code aus? ```python reihe = ["o", "o", "~", "o", "~"] eingabe = 0 print(reihe[eingabe - 1]) einga |
| L4.022 | code_schreiben | F. 105, 106 | Schreib die Bedingung: `zahl` ist nur gültig, wenn sie zwischen 1 und 5 liegt (beide eingeschlossen). |
| L4.023 | code_ausgabe | F. 152 · Aufg. 4.4 | Was gibt der Code aus? ```python raster = [["o", "~", "o"], ["~", "o", "o"]] for i in range(len(raster)):      |
| L4.024 | code_schreiben | Aufg. 2.5, 4.3 | Setz in jede der 5 Reihen von `raster` genau ein Treibsandfeld `"~"` an eine zufällige Spalte. |
| L4.025 | code_ausgabe | Aufg. 3.8 | Was gibt der Code aus? ```python ergebnisse = [True, True, False, True] for runde in range(len(ergebnisse)):   |
| L4.026 | trace | F. 125 · Aufg. 3.7 | Verfolge `runde` und `leben` Durchlauf für Durchlauf. Was wird ausgegeben? ```python ergebnisse = [False, True |
| L4.027 | unterschied | F. 125, 128 | Wann nimmst du in deinem Level `for`, wann `while`? |
| L4.028 | falle | F. 119 · Probe-Kolloquium | Warum stehen die erlaubten Tasten als Liste `["d", "D"]` und nicht als String `"dD"`? Was gibt der Code aus? ` |
| L4.029 | begruenden | Probe-Kolloquium; Level-Konzept | Prüfer: „Wie gewinnt man bei der Hängebrücke jedes ‚RUHIG‘, ohne hinzusehen?“ Was antwortest du, und was baust |
| L4.030 | code_schreiben | F. 141 · Probe-Kolloquium | Prüfer: „Fügen Sie beim Affen-Echo einen Papagei auf Taste `p` hinzu.“ Welche Stellen änderst du? |
| L4.031 | begruenden | Probe-Kolloquium; Level-Konzept | Prüfer: „Wie groß ist die Chance, das Treibsand-Raster ohne Hinsehen zu schaffen?“ |
| L4.032 | code_schreiben | F. 144, 153 · Aufg. 4.3 · Probe-Kolloquium | Prüfer: „Schreiben Sie das 5×5-Raster ohne List-Comprehension, mit gewöhnlichen Schleifen.“ |
