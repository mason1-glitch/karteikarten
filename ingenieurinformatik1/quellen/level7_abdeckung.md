# Abdeckungsmatrix – Level-Kolloquium 7: Effekte, Konsole und Umgebung

Erzeugt mit `werkzeuge/karten.py` aus `ingenieurinformatik1/quellen/level7_karten.yaml`. 18 Karten, 7 prüfbare Inhalte, 0 Wiederholungsfragen.

## Karten je Typ

| Typ | Anzahl |
|---|---:|
| Aufzählung vollständig | 1 |
| Einzelfakt | 1 |
| Klausurfalle | 3 |
| Anwendung (Fall → Einordnung) | 1 |
| Begriff ↔ Erklärung | 4 |
| Was gibt der Code aus? | 4 |
| Schreib Code, der … | 2 |
| Warum so? (Entscheidung begründen) | 2 |
| **Summe** | **18** |

Karten mit Bild: 0.


## Konzepte → Karten

Gewicht: 3 = in vielen Aufgaben gebraucht, 2 = mehrfach, 1 = selten. F. = Seite im Skript-PDF, Aufg. = Aufgabe im Ordner Informatik-1---Aufgaben-und-Beispiele.

| Konzept | Gewicht | Quelle | Karten | Typen |
|---|---:|---|---|---|
| Escape-Sequenzen \n, \t, \r, \b; \r zurück an den Zeilenanfang (Countdown in einer Zeile) | 3 | F. 52–54 | L7.001, L7.002, L7.003, L7.004 | 3 |
| ASCII-Bilder: Backslash verdoppeln (\\), Anführungszeichen \", mehrzeilige Strings mit """ | 3 | F. 60, 69 | L7.001, L7.005, L7.006, L7.007 | 3 |
| print(…, end="") und flush=True für Schreibmaschinen-Text | 2 | F. 151 · Ergänzung | L7.008, L7.009 | 2 |
| ANSI-Farbcodes \033[32m … \033[0m | 2 | Ergänzung | L7.010, L7.011 | 2 |
| Ton: \a, winsound (nur Windows), Pakete; mit try/except ImportError/RuntimeError ohne Ton weiterspielen | 3 | Ergänzung; Level-Konzept | L7.012, L7.013, L7.014 | 3 |
| Virtuelle Umgebung, requirements.txt erstellen und installieren | 2 | Laborfolie IDE/venv F. 13, 28–29 | L7.015, L7.016 | 2 |
| Konsolen verhalten sich unterschiedlich; Effekte so bauen, dass das Spiel auch ohne läuft; Bilder anzeigen | 2 | Level-Konzept | L7.014, L7.017, L7.018 | 2 |

## Annahmen

- Welche Effekte genau Bonuspunkte bringen, steht in einer Stud.IP-Nachricht, die nicht im Projekt liegt. Laut Dozent: Sound und Bilder.
- Wie \r, Farben und Signalton aussehen, hängt von der Konsole ab (PyCharm-Ausgabefenster, Terminal, Windows-Eingabeaufforderung); die Karten beschreiben das übliche Verhalten.

## Karten-Index

| ID | Typ | Folien | Frage |
|---|---|---|---|
| L7.001 | begriff | F. 53, 69 | Was bewirken die Escape-Sequenzen `\n`, `\t`, `\r`, `\b`, `\"` und `\\` in einem String? |
| L7.002 | code_ausgabe | F. 53, 151 | Was sieht der Spieler am Ende in der Zeile? (Der Code zählt in **einer** Zeile herunter.) ```python import tim |
| L7.003 | falle | F. 53 | Warum endet `print("LOS!   ")` im Countdown mit Leerzeichen? Was stünde ohne sie nach `Noch 10 s` + `\r` + `LO |
| L7.004 | code_ausgabe | F. 54 | Was gibt der Code aus? ```python print("Leben:\t3") print("Punkte:\t120") print("Fehlx\b!") ``` |
| L7.005 | code_ausgabe | F. 53, 69 | Was gibt der Code aus? ```python print("\\o/ Juhu") print("/\\_/\\") print("Ast\neben") ``` |
| L7.006 | falle | F. 53, 69 | Dein Affenbild enthält `print(" //_/\ ")`. Es sieht richtig aus. Warum solltest du es trotzdem ändern? (Ergänz |
| L7.007 | code_ausgabe | F. 60 · Aufg. 2.6 | Was gibt der Code aus? ```python affe_bild = """ (o.o)  //_/\\   / \\""" print(affe_bild) ``` |
| L7.008 | begriff | F. 151 · Ergänzung | Wozu dienen `end=""` und `flush=True` beim Schreibmaschinen-Text? |
| L7.009 | code_schreiben | Aufg. 1.3 · Ergänzung | Schreib `langsam_schreiben(text)`: gibt den Text Zeichen für Zeichen mit kurzer Pause aus, am Ende ein Zeilenu |
| L7.010 | begriff | Ergänzung | Wie färbst du Text in der Konsole grün, und was bedeutet `\033`? (Ergänzung) |
| L7.011 | falle | Ergänzung | Warum gehört hinter jeden farbigen Text `\033[0m`? (Ergänzung) |
| L7.012 | aufzaehlung | Ergänzung; Level-Konzept | Welche Möglichkeiten für Ton gibt es, und welchen Haken hat jede? (Ergänzung) |
| L7.013 | code_schreiben | Ergänzung; Level-Konzept | Schreib `ton_abspielen()`: piept unter Windows; wo das nicht geht, läuft das Spiel ohne Absturz weiter. (Ergän |
| L7.014 | begruenden | Level-Konzept | Warum soll dein Spiel bei Problemen mit dem Ton **ohne Ton weiterlaufen**, statt abzustürzen oder eine Fehlerm |
| L7.015 | begriff | Laborfolie IDE/venv F. 13 | Was ist eine **virtuelle Umgebung**, und warum nutzt man sie? |
| L7.016 | fakt | Laborfolie IDE/venv F. 28–29 | Euer Spiel braucht `pygame`. Wie erstellt ihr eine `requirements.txt`, und wie installiert sie ein anderer? |
| L7.017 | begruenden | Level-Konzept | Warum testest du die Effekte früh auf dem Rechner, auf dem vorgeführt wird? |
| L7.018 | anwendung | F. 205 · Level-Konzept; Ergänzung | Bilder bringen Extrapunkte. Welche zwei Wege gibt es, und was spricht für welchen? |
