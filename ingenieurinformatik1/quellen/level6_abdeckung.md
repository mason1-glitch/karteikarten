# Abdeckungsmatrix – Level-Kolloquium 6: Bestenliste, Sortieralgorithmus, Rekursion

Erzeugt mit `werkzeuge/karten.py` aus `ingenieurinformatik1/quellen/level6_karten.yaml`. 37 Karten, 12 prüfbare Inhalte, 0 Wiederholungsfragen.

## Karten je Typ

| Typ | Anzahl |
|---|---:|
| Einzelfakt | 1 |
| Klausurfalle | 3 |
| Begriff ↔ Erklärung | 2 |
| Lückentext im Code | 2 |
| Was gibt der Code aus? | 11 |
| Finde den Fehler | 5 |
| Schreib Code, der … | 3 |
| Was ist der Unterschied …? | 4 |
| Warum so? (Entscheidung begründen) | 5 |
| Trace-Tabelle (Werte Schritt für Schritt) | 1 |
| **Summe** | **37** |

Karten mit Bild: 1.


## Konzepte → Karten

Gewicht: 3 = in vielen Aufgaben gebraucht, 2 = mehrfach, 1 = selten. F. = Seite im Skript-PDF, Aufg. = Aufgabe im Ordner Informatik-1---Aufgaben-und-Beispiele.

| Konzept | Gewicht | Quelle | Karten | Typen |
|---|---:|---|---|---|
| Eintrag anhängen: open(…, "a"), write() nur mit str, \n selbst setzen, close() | 3 | F. 193–194 | L6.001, L6.002, L6.003, L6.005 | 4 |
| Dateimodi r, w, a: was passiert mit vorhandenem Inhalt, was bei fehlender Datei | 3 | F. 189, 193 | L6.004, L6.005 | 2 |
| Zeilenweise lesen mit for zeile in datei; jede Zeile endet mit \n; read() | 3 | F. 190–191 | L6.001, L6.006, L6.007, L6.012 | 3 |
| Zeile zerlegen mit find(";") und Slicing; float() verträgt das \n | 3 | F. 137–138 | L6.008, L6.009, L6.010, L6.033 | 4 |
| Kaputte Zeile mit try/except ValueError oder continue überspringen | 2 | Level-Konzept | L6.011, L6.012, L6.033, L6.037 | 3 |
| Einträge als Liste von Dictionaries {"name", "zeit"}; Zugriff eintraege[i]["zeit"] | 2 | Level-Konzept | L6.013, L6.014, L6.022 | 2 |
| Bubble Sort: Nachbarn vergleichen und tauschen, größtes Element wandert nach hinten; Schleifengrenzen | 3 | Labor KW45 (Vorgriff) | L6.015, L6.016, L6.019, L6.020, L6.021, L6.026, L6.028, L6.034, L6.035 | 7 |
| Zwei Elemente tauschen mit Merker-Variable; ganze Dictionaries tauschen | 3 | Labor KW45 (Vorgriff) | L6.014, L6.017, L6.018, L6.019, L6.022 | 5 |
| Merker getauscht für frühen Abbruch; Anzahl Vergleiche n·(n−1)/2 | 2 | Labor KW45 (Vorgriff) | L6.023, L6.024 | 2 |
| Eingebautes liste.sort(reverse=…, key=funktion) vs. eigener Algorithmus | 2 | F. 146–147 | L6.025, L6.026 | 2 |
| Höchstens die ersten fünf Einträge anzeigen; Platzierung i + 1 | 2 | Level-Konzept | L6.027, L6.028 | 2 |
| Rekursion: Funktion ruft sich selbst auf, Abbruchbedingung, RecursionError; Vergleich mit Schleife | 2 | Labor KW45 (Vorgriff) | L6.029, L6.030, L6.031, L6.032, L6.036 | 4 |

## Annahmen

- Welcher Sortieralgorithmus im Labor (KW45) gezeigt wird, ist noch offen. Die Karten nehmen Bubble Sort, den gängigsten Einstiegsalgorithmus; nach dem Labor mit den Folien abgleichen und ggf. Karten zum dort gezeigten Verfahren ergänzen.
- Rekursion ist im Level optional (Countdown); auch hier Vorgriff auf KW45.
- Dateiformat der Bestenliste: eine Zeile „Name;Zeit“ je Eintrag – eigene Festlegung im Level-Konzept.

## Karten-Index

| ID | Typ | Folien | Frage |
|---|---|---|---|
| L6.001 | code_ausgabe | F. 190, 194 | Was gibt der Code aus? (`bestenliste.txt` gibt es noch nicht.) ```python datei = open("bestenliste.txt", "a")  |
| L6.002 | code_fehler | F. 194 | Der Code bricht ab. Warum? ```python zeit = 0.412 datei = open("bestenliste.txt", "a") datei.write(zeit) datei |
| L6.003 | code_schreiben | F. 194 · Level-Konzept | Schreib `bestenliste_speichern(name, zeit_s)`: hängt eine Zeile `Name;Zeit` mit drei Nachkommastellen an `best |
| L6.004 | unterschied | F. 189, 193 | Vergleiche die Dateimodi `"r"`, `"w"` und `"a"`. |
| L6.005 | falle | F. 193 | Was gibt der Code aus – und warum wäre das für die Bestenliste fatal? ```python for name in ["Max", "Lea"]:    |
| L6.006 | code_ausgabe | F. 191 | `bestenliste.txt` enthält zwei Zeilen. Was gibt der Code aus, und warum sieht es so aus? ```python datei = ope |
| L6.007 | unterschied | F. 190, 191 | Was liefern `datei.read()`, `datei.readlines()` und `for zeile in datei:`? |
| L6.008 | code_ausgabe | F. 137, 138 | Was gibt der Code aus? ```python zeile = "Lea;0.298\n" trenner = zeile.find(";") name = zeile[0:trenner] zeit  |
| L6.009 | code_luecke | F. 137, 138 | Ergänze die Indizes so, dass `name = "Ina"` und `zeit = 0.301` herauskommen. ```python zeile = "Ina;0.301\n" t |
| L6.010 | unterschied | F. 138, 153 | Warum zerlegst du die Zeile mit `find` und Slicing und nicht mit `split(";")`? |
| L6.011 | code_ausgabe | F. 138 · Level-Konzept; Labor KW46 (Vorgriff) | Was gibt der Code aus? ```python for zeile in ["Max;0.412\n", "Ole;schnell\n"]:     trenner = zeile.find(";")  |
| L6.012 | begruenden | Level-Konzept | Warum steht beim Laden das `try` um die **einzelne Zeile** und nicht um die ganze `for`-Schleife? |
| L6.013 | code_ausgabe | F. 151 · Level-Konzept | Was gibt der Code aus? ```python eintraege = [] eintraege.append({"name": "Max", "zeit": 0.412}) eintraege.app |
| L6.014 | begruenden | Level-Konzept | Warum speicherst du die Bestenliste als Liste von Dictionaries und nicht als zwei Listen `namen` und `zeiten`? |
| L6.015 | begriff | Labor KW45 (Vorgriff) | Wie funktioniert **Bubble Sort**? |
| L6.016 | trace | Labor KW45 (Vorgriff) | Führe den **ersten Durchlauf** von Bubble Sort an `[0.41, 0.30, 0.66, 0.29]` aus. Wie sieht die Liste nach jed |
| L6.017 | code_luecke | Labor KW45 (Vorgriff) | Tausche die beiden Zeiten, wenn sie falsch herum stehen. ```python zeiten = [0.41, 0.30] if zeiten[0] > zeiten |
| L6.018 | code_fehler | Labor KW45 (Vorgriff) | Das soll tauschen. Was kommt heraus, und warum? ```python zeiten = [0.41, 0.30] zeiten[0] = zeiten[1] zeiten[1 |
| L6.019 | code_schreiben | Labor KW45 (Vorgriff) | Sortiere `zeiten = [0.41, 0.30, 0.66, 0.29]` aufsteigend mit Bubble Sort und gib die Liste aus. |
| L6.020 | begruenden | Labor KW45 (Vorgriff) | Warum läuft die innere Schleife nur bis `len(zeiten) - 1 - durchlauf`? |
| L6.021 | code_fehler | Labor KW45 (Vorgriff) | Der Code bricht ab. Warum? ```python zeiten = [0.41, 0.30, 0.66] for j in range(len(zeiten)):     if zeiten[j] |
| L6.022 | code_ausgabe | Level-Konzept; Labor KW45 (Vorgriff) | Was gibt der Code aus? ```python eintraege = [{"name": "Max", "zeit": 0.41},              {"name": "Lea", "zei |
| L6.023 | begruenden | Labor KW45 (Vorgriff) | Wozu dient in deiner Bestenliste-Sortierung der Merker `getauscht`? |
| L6.024 | fakt | Labor KW45 (Vorgriff) | Wie viele Vergleiche braucht Bubble Sort ohne frühen Abbruch für n Einträge, und wie viele bei 10? |
| L6.025 | code_ausgabe | F. 146, 147 | Was gibt der Code aus? ```python def nach_zeit(eintrag):     return eintrag["zeit"]  liste = [{"name": "Max",  |
| L6.026 | begruenden | F. 146, 147 · Laboraufgabe F. 2 | Python hat `liste.sort()`. Warum sortierst du die Bestenliste trotzdem selbst? |
| L6.027 | code_ausgabe | F. 152 · Level-Konzept | Was gibt der Code aus? ```python namen = ["Lea", "Ina", "Max", "Ben", "Tom", "Kim"] for i in range(len(namen)) |
| L6.028 | code_schreiben | Level-Konzept | Kolloquium: „Ändere deine Sortierung so, dass die **langsamste** Zeit vorne steht.“ Was änderst du? |
| L6.029 | begriff | Labor KW45 (Vorgriff); Laborfolie IDE F. 3 (Thonny-Beispiel fact) | Was ist **Rekursion**, und welche zwei Teile braucht jede rekursive Funktion? |
| L6.030 | code_ausgabe | Labor KW45 (Vorgriff) | Was gibt der Code aus? ```python def countdown(n):     if n == 0:         print("LOS!")         return     pri |
| L6.031 | code_fehler | Labor KW45 (Vorgriff) | Was passiert hier, und warum? ```python def countdown(n):     print(n)     countdown(n - 1)  countdown(3) ``` |
| L6.032 | unterschied | F. 128 · Labor KW45 (Vorgriff) | Countdown als Schleife oder rekursiv – was spricht wofür? |
| L6.033 | falle | F. 137, 138 · Probe-Kolloquium | In der Bestenliste steht eine Zeile **ohne** Semikolon: `5`. Was gibt der Code aus? ```python zeile = "5\n" tr |
| L6.034 | falle | F. 146, 173 · Probe-Kolloquium | Deine Sortierfunktion ändert die übergebene Liste direkt und hat kein `return`. Was gibt der Code aus? ```pyth |
| L6.035 | code_ausgabe | Probe-Kolloquium | Du sortierst die Bestenliste testweise nach **Namen**. Was gibt der Code aus? (Ergänzung) ```python print("Zoe |
| L6.036 | code_fehler | Probe-Kolloquium; Labor KW45 (Vorgriff) | `countdown(3)` läuft. Was passiert bei `countdown(-1)`, und wie machst du die Funktion sicher? ```python def c |
| L6.037 | code_ausgabe | F. 138 · Aufg. 3.8 | Was gibt der Code aus? ```python for zeile in ["Max;0.412\n", "5\n", "Lea;0.298\n"]:     trenner = zeile.find( |
