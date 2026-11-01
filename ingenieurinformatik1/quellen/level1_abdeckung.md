# Abdeckungsmatrix – Level-Kolloquium 1: Auftrag, Aufbau und Schnittstelle

Erzeugt mit `werkzeuge/karten.py` aus `ingenieurinformatik1/quellen/level1_karten.yaml`. 27 Karten, 12 prüfbare Inhalte, 0 Wiederholungsfragen.

## Karten je Typ

| Typ | Anzahl |
|---|---:|
| Aufzählung vollständig | 2 |
| Einzelfakt | 2 |
| Klausurfalle | 2 |
| Anwendung (Fall → Einordnung) | 3 |
| Begriff ↔ Erklärung | 4 |
| Lückentext im Code | 2 |
| Was gibt der Code aus? | 5 |
| Finde den Fehler | 3 |
| Schreib Code, der … | 2 |
| Was ist der Unterschied …? | 1 |
| Warum so? (Entscheidung begründen) | 1 |
| **Summe** | **27** |

Karten mit Bild: 1.


## Konzepte → Karten

Gewicht: 3 = in vielen Aufgaben gebraucht, 2 = mehrfach, 1 = selten. F. = Seite im Skript-PDF, Aufg. = Aufgabe im Ordner Informatik-1---Aufgaben-und-Beispiele.

| Konzept | Gewicht | Quelle | Karten | Typen |
|---|---:|---|---|---|
| Pflichtelemente: Ausnahmebehandlungen, Kontrollstrukturen, Funktionen + mind. eines von Dictionaries, Rekursion, Sortieralgorithmen | 3 | Laboraufgabe F. 2 | L1.001, L1.002 | 2 |
| Bewertung (Zulassung + Einzelnote im Kolloquium), Fragen zum eigenen Code, Kennzeichnung, Termine | 3 | Laboraufgabe F. 3; Labor-Einführung | L1.003, L1.004, L1.006, L1.024 | 3 |
| Geklärt: Ergänzungen erlaubt, wenn erklärbar; Kommentare nicht bewertet; 600 Zeilen Richtwert; Extrapunkte für Sound und Bilder | 2 | Absprache mit dem Dozenten | L1.005, L1.006 | 2 |
| Level als Funktion level_dschungel_reflexe(spieler), eine Funktion je Station, Rückgabe True/False an main.py | 3 | Level-Konzept | L1.002, L1.007, L1.008, L1.016, L1.027 | 4 |
| spieler-Dictionary als Parameter: Änderungen am Inhalt wirken beim Aufrufer, Neuzuweisung einer Zahl nicht | 3 | F. 182 | L1.009, L1.010, L1.011 | 3 |
| return liefert True/False (Vergleich ist ein bool); ohne erreichtes return kommt None zurück | 3 | F. 173, 180 | L1.008, L1.014, L1.015, L1.016 | 4 |
| Funktion erst definieren, dann aufrufen (NameError); der Rumpf läuft erst beim Aufruf | 2 | F. 171, 175 | L1.017, L1.018 | 2 |
| Prozedur, Funktion, Methode im eigenen Code; Docstring | 2 | F. 172–174 | L1.019, L1.020 | 2 |
| lokale und globale Variablen, Schlüsselwort global | 2 | F. 182–183 | L1.010, L1.011, L1.012, L1.013 | 4 |
| Modul = importierbare Python-Datei; import führt den Code auf oberster Ebene aus | 2 | Laborfolie IDE/venv F. 15 | L1.021, L1.022 | 2 |
| Code-Conventions (snake_case, deutsch, keine Umlaute, 4 Leerzeichen) und Kennzeichnung per Kommentar | 2 | F. 58–60 | L1.023, L1.024 | 2 |
| Grundstrukturen sequentiell, auswählend, iterativ, springend am eigenen Level; PAP | 2 | F. 109–111 | L1.025, L1.026, L1.027 | 2 |

## Annahmen

- Ob jeder Teil alle Pflichtelemente selbst enthalten muss, steht nicht auf den Folien (offene Frage an den Dozenten). Die Karten gehen vom sicheren Fall aus: Das eigene Level enthält alle Pflichtelemente.
- Der genaue Kolloquiumstermin steht noch nicht fest (Laboraufgabe F. 3: hinter „Koloq:“ kein Termin); laut Labor-Einführung KW49/KW50.
- Die PAP-Folien aus KW43 liegen nicht im Projekt. Die Karte zu den PAP-Symbolen folgt DIN 66001 und ist als Ergänzung markiert.

## Karten-Index

| ID | Typ | Folien | Frage |
|---|---|---|---|
| L1.001 | aufzaehlung | Laboraufgabe F. 2 | Welche **drei Elemente** muss das Escape-Room-Programm laut Laboraufgabe enthalten, und welche **Wahl** kommt  |
| L1.002 | anwendung | Level-Konzept | Zeig an **deinem Level**, wo jedes Pflicht- und Wahlelement steckt. |
| L1.003 | fakt | Laboraufgabe F. 3 | Wie setzt sich die Bewertung der Laboraufgabe zusammen, und **wozu** wirst du im Kolloquium befragt? |
| L1.004 | fakt | Laboraufgabe F. 2–3; Labor-Einführung | Bis wann und wohin wird das Programm abgegeben, und wann ist das Kolloquium? |
| L1.005 | aufzaehlung | Absprache mit dem Dozenten | Welche **vier Punkte** hat der Dozent zur Laboraufgabe schon geklärt? |
| L1.006 | falle | Absprache mit dem Dozenten | Dein Code steckt voller guter Kommentare. Was bringen sie dir im Kolloquium – und was nicht? |
| L1.007 | begriff | Level-Konzept | Wie ist dein Level aufgebaut, und was bekommt `main.py` zurück? |
| L1.008 | code_schreiben | F. 171, 180 · Level-Konzept | Schreib das Gerüst der Level-Funktion: Sie bekommt `spieler`, ruft `lianen_sprung(spieler)` und `haengebruecke |
| L1.009 | code_ausgabe | F. 182 | Was gibt der Code aus? ```python def leben_abziehen(spieler):     spieler["leben"] -= 1  spieler = {"name": "M |
| L1.010 | unterschied | F. 182 | Warum bleibt hier `leben` bei 3, obwohl die Funktion 1 abzieht? ```python def leben_abziehen(leben):     leben |
| L1.011 | begruenden | F. 183 · Level-Konzept | Warum übergibst du `spieler` als Parameter, statt in jeder Station `global spieler` zu schreiben? |
| L1.012 | code_ausgabe | F. 183 | Was gibt der Code aus? ```python punkte = 0  def punkte_geben():     global punkte     punkte += 10  punkte_ge |
| L1.013 | code_fehler | F. 182, 183 | Der Code bricht ab. Warum, und wie behebst du es? ```python punkte = 0  def punkte_geben():     punkte += 10   |
| L1.014 | code_ausgabe | F. 173 | Was gibt der Code aus? ```python def geschafft(leben):     return leben > 0  print(geschafft(2)) print(geschaf |
| L1.015 | falle | F. 173, 180 | Was gibt der Code aus – und warum ist das für `main.py` gefährlich? ```python def station(leben):     if leben |
| L1.016 | code_luecke | F. 112 · Level-Konzept | Ergänze `main.py`: Nur wenn das Level geschafft ist, soll die Ziffer erscheinen. ```python ___ level_dschungel |
| L1.017 | code_fehler | F. 175 | Welche Fehlermeldung kommt, und warum? ```python level_dschungel_reflexe({"leben": 3})  def level_dschungel_re |
| L1.018 | code_ausgabe | F. 178 | Was gibt der Code aus? ```python def lianen_sprung():     print("Sprung!")  def haengebruecke():     lianen_sp |
| L1.019 | begriff | F. 172–174 | Ordne aus deinem Level je ein Beispiel zu: **Prozedur, Funktion, Methode**. |
| L1.020 | code_luecke | Aufg. 5.5 | Ergänze den einzeiligen Docstring an der richtigen Stelle. ```python def reaktion_messen(zeitlimit_s):     ___ |
| L1.021 | begriff | Laborfolie IDE/venv F. 15 | Was ist ein **Modul**, und wie ruft `main.py` dein Level auf, wenn es in `level_dschungel.py` steht? |
| L1.022 | code_ausgabe | Laborfolie IDE/venv F. 15 | `level_dschungel.py`: ```python def level_dschungel_reflexe(spieler):     return True  print("Test: Level gela |
| L1.023 | code_fehler | F. 58 · Code-Leitfaden 2.1, 2.6 | Der Code läuft. Welche **Code-Conventions** verletzt er? ```python def ZeitMessen(Zeitlimit):     if(Zeitlimit |
| L1.024 | code_schreiben | Aufg. 2.1 · Laboraufgabe F. 3 | Schreib den Kopf deiner Level-Datei und die Kennzeichnung über einer Station so, dass klar ist, dass der Code  |
| L1.025 | anwendung | F. 109 | Nenne die vier **Grundstrukturen** eines Programms mit je einem Beispiel aus deinem Level. |
| L1.026 | begriff | Ergänzung: DIN 66001 (PAP-Folien KW43 nicht im Projekt) | Welche Symbole hat ein **Programmablaufplan (PAP)**, und wofür steht jedes? |
| L1.027 | anwendung | Level-Konzept; Ergänzung: DIN 66001 | Erkläre den Ablauf der Reaktionsmessung anhand des PAP. [Bild] |
