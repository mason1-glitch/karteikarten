# Abdeckungsmatrix – Level-Kolloquium 8: Erklären, Begründen, Ändern

Erzeugt mit `werkzeuge/karten.py` aus `ingenieurinformatik1/quellen/level8_karten.yaml`. 21 Karten, 9 prüfbare Inhalte, 0 Wiederholungsfragen.

## Karten je Typ

| Typ | Anzahl |
|---|---:|
| Aufzählung vollständig | 1 |
| Klausurfalle | 1 |
| Anwendung (Fall → Einordnung) | 7 |
| Unstimmigkeit im Skript | 1 |
| Begriff ↔ Erklärung | 2 |
| Was gibt der Code aus? | 3 |
| Schreib Code, der … | 2 |
| Was ist der Unterschied …? | 2 |
| Warum so? (Entscheidung begründen) | 2 |
| **Summe** | **21** |

Karten mit Bild: 0.


## Konzepte → Karten

Gewicht: 3 = in vielen Aufgaben gebraucht, 2 = mehrfach, 1 = selten. F. = Seite im Skript-PDF, Aufg. = Aufgabe im Ordner Informatik-1---Aufgaben-und-Beispiele.

| Konzept | Gewicht | Quelle | Karten | Typen |
|---|---:|---|---|---|
| Eine Funktion in fünf Punkten erklären: Zweck, Parameter, Ablauf, Rückgabe, Sonderfälle | 3 | Laboraufgabe F. 3; Level-Konzept | L8.001, L8.002, L8.003, L8.004 | 2 |
| Auf Zuruf ändern: Leben, neue Station, Rastergröße – wo genau? | 3 | Level-Konzept | L8.005, L8.006, L8.007 | 2 |
| Hilfsfunktionen statt Kopien; feste Zahlen als Variable; Kommentar, Docstring, auskommentierter Code | 2 | F. 170 | L8.007, L8.008, L8.009, L8.010 | 3 |
| Datentypen im Level: int, float, str, bool, None, list, dict; type() | 2 | F. 64–68 | L8.011, L8.012 | 2 |
| Tupel: unveränderlich, runde Klammern; return a, b liefert ein Tupel, Entpacken | 2 | F. 155 · Aufg. 5.2, 5.6 | L8.013, L8.014 | 2 |
| Lokale Variablen gleichen Namens in verschiedenen Funktionen; Schleifenvariable gilt nach der Schleife weiter | 2 | F. 182 | L8.015, L8.016 | 2 |
| Traceback lesen, Trace-Ausgaben, auskommentieren | 2 | F. 59, 177–178 · Aufg. 5.1, 5.2 | L8.010, L8.017, L8.018 | 3 |
| Grenzfälle durchdenken: vorgetippte Eingaben, doppelte Tasten, leere Bestenliste | 2 | Level-Konzept | L8.019, L8.020 | 2 |
| Algorithmus: endlich, eindeutig, reproduzierbar – und der Zufall im Level | 1 | F. 42 | L8.004, L8.021 | 2 |

## Unstimmigkeiten im Skript (je eine Karte)

- L8.016 (F. 182 · Code-Leitfaden 4): Das Skript (F. 182) sagt, Variablen in **Schleifen** seien lokal. Was gibt der Code aus?

## Annahmen

- Wie das Kolloquium abläuft (Dauer, ob live am Rechner geändert wird), steht nicht auf den Folien. Die Karten bereiten auf beides vor: mündlich erklären und Code auf Zuruf ändern. Dafür gibt es zusätzlich die Übungen in level_kolloquium-training.md.

## Karten-Index

| ID | Typ | Folien | Frage |
|---|---|---|---|
| L8.001 | aufzaehlung | Level-Konzept | Mit welchen **fünf Punkten** erklärst du im Kolloquium jede deiner Funktionen? |
| L8.002 | anwendung | Baustein b03; Level-Konzept | Erkläre `reaktion_messen(zeitlimit_s)` in den fünf Punkten. |
| L8.003 | anwendung | Baustein b08; Level-Konzept | Erkläre `bestenliste_laden()` in den fünf Punkten. |
| L8.004 | anwendung | Level-Konzept | Beschreib den Gesamtablauf deines Levels von Anfang bis Ende (so wie dein PAP). |
| L8.005 | anwendung | Level-Konzept | Kolloquium: „Der Spieler soll 5 statt 3 Leben haben.“ Wo änderst du das – und warum nicht in deinem Level? |
| L8.006 | anwendung | Level-Konzept | Kolloquium: „Füge eine sechste Station Glühwürmchen hinzu.“ Welche drei Stellen fasst du an? |
| L8.007 | code_schreiben | F. 153 · Level-Konzept | Kolloquium: „Mach das Treibsand-Raster 4×4.“ Wie hast du den Code gebaut, damit das **eine** Änderung ist? |
| L8.008 | begruenden | Code-Leitfaden 2.6 | Warum schreibst du `groesse = 5` oben in den Code, statt überall direkt `5` einzusetzen? |
| L8.009 | begruenden | F. 170 | Warum gibt es Hilfsfunktionen wie `zahl_einlesen()` und `eingabepuffer_leeren()`, statt den Code in jede Stati |
| L8.010 | unterschied | F. 59, 60 · Aufg. 5.5 | Was ist der Unterschied zwischen Kommentar, Docstring und auskommentiertem Code? |
| L8.011 | code_ausgabe | F. 66 | Was gibt der Code aus? ```python werte = [3, 0.412, "atf", True, None, [1], {"a": 1}] for wert in werte:     p |
| L8.012 | anwendung | F. 64–68 | Welche Datentypen kommen in deinem Level vor – je ein Beispiel? |
| L8.013 | code_ausgabe | F. 155 · Aufg. 5.2 | Was gibt der Code aus? ```python def ergebnis_station():     return 2, 0.412  fehler, zeit = ergebnis_station( |
| L8.014 | unterschied | F. 155 | Was unterscheidet ein **Tupel** von einer **Liste** – und wo bietet sich in deinem Level ein Tupel an? |
| L8.015 | code_ausgabe | F. 182 | Was gibt der Code aus? ```python def station_a():     fehler = 2     return fehler def station_b():     fehler |
| L8.016 | unstimmigkeit | F. 182 · Code-Leitfaden 4 | Das Skript (F. 182) sagt, Variablen in **Schleifen** seien lokal. Was gibt der Code aus? ```python for runde i |
| L8.017 | begriff | F. 175 · Aufg. 5.1 | Dein Spiel stürzt mit einem Traceback ab. Wie liest du ihn? |
| L8.018 | code_schreiben | F. 177, 178 · Aufg. 5.2, 2.1 | Die Hängebrücke verhält sich seltsam. Wie machst du den Ablauf sichtbar, ohne einen Debugger? |
| L8.019 | falle | Level-Konzept | Während das Treibsand-Raster 3 s sichtbar ist, tippt der Spieler schon `3` und Enter. Was passiert beim folgen |
| L8.020 | anwendung | Level-Konzept | Welche Grenzfälle testest du vor der Abgabe gezielt? Nenne fünf. |
| L8.021 | begriff | F. 42 | Welche Eigenschaften muss ein **Algorithmus** laut Skript haben – und wie passt der Zufall in deinem Level daz |
