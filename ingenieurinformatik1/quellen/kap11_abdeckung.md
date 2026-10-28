# Abdeckungsmatrix – Kapitel 11: Dateien öffnen, lesen, schreiben

Erzeugt mit `werkzeuge/karten.py` aus `ingenieurinformatik1/quellen/kap11_karten.yaml`. 25 Karten, 9 prüfbare Inhalte, 0 Wiederholungsfragen.

## Karten je Typ

| Typ | Anzahl |
|---|---:|
| Begriff ↔ Erklärung | 4 |
| Lückentext im Code | 1 |
| Was gibt der Code aus? | 9 |
| Finde den Fehler | 6 |
| Schreib Code, der … | 2 |
| Was ist der Unterschied …? | 3 |
| **Summe** | **25** |

Karten mit Bild: 0.


## Konzepte → Karten

Gewicht: 3 = in vielen Aufgaben gebraucht, 2 = mehrfach, 1 = selten. F. = Seite im Skript-PDF, Aufg. = Aufgabe im Ordner Informatik-1---Aufgaben-und-Beispiele.

| Konzept | Gewicht | Quelle | Karten | Typen |
|---|---:|---|---|---|
| open(pfad, modus): "r", "w", "a"; ohne Modus "r" | 2 | F. 189, 193 · Aufg. 6.1, 6.2 | K11.001, K11.002, K11.003, K11.004 | 3 |
| read() ganze Datei, read(n) n Zeichen | 2 | F. 190 · Aufg. 6.1 | K11.005, K11.006, K11.007 | 2 |
| Zeilenweise lesen mit for zeile in datei; jede Zeile endet mit \n | 2 | F. 191 · Aufg. 6.1, 6.2 | K11.008, K11.009, K11.010 | 3 |
| readlines() (Liste der Zeilen) und readline() | 1 | F. 191 · Aufg. 6.1 | K11.011, K11.012 | 2 |
| write(): nur Strings, kein automatischer Zeilenumbruch | 2 | F. 194 · Aufg. 6.2 | K11.013, K11.014, K11.015 | 3 |
| "w" überschreibt, "a" hängt an | 2 | F. 193–194 · Aufg. 6.2 | K11.003, K11.016, K11.017, K11.018 | 3 |
| close(): Datei schließen; danach kein Zugriff mehr | 2 | F. 190, 194 · Aufg. 6.1, 6.2 | K11.019, K11.020 | 2 |
| Relativer Pfad (../Daten/…) und FileNotFoundError | 1 | F. 189 · Aufg. 6.1 | K11.021, K11.022 | 2 |
| Dateiinhalt zeilenweise auswerten (float(zeile), zählen, ersetzen) | 2 | F. 187 · Aufg. 6.1, 6.2 | K11.023, K11.024, K11.025 | 2 |

## Bewusst ausgelassene Folien

| Folien | Grund |
|---|---|
| 195 | Modus "r+" (Lesen und Schreiben): nur ein Beispiel, in keiner Aufgabe genutzt. Der Kommentar „Überschreiben des bisherigen Inhalts“ ist ungenau: r+ überschreibt ab Dateianfang nur so viele Zeichen, wie geschrieben werden (geprüft). |

## Karten-Index

| ID | Typ | Folien | Frage |
|---|---|---|---|
| K11.001 | begriff | F. 189, 193 | Welche drei Dateimodi für `open()` nennt das Skript auf F. 189 und 193? |
| K11.002 | code_fehler | F. 189 | Die Datei `log.txt` existiert. Welche Fehlermeldung erscheint, und warum? ```python datei = open("log.txt") da |
| K11.003 | code_luecke | F. 189, 194 · Aufg. 6.2 | Neue Einträge sollen **ans Ende** der vorhandenen Logdatei angehängt werden. Ergänze den Modus. ```python date |
| K11.004 | code_fehler | F. 189 | Welche Fehlermeldung erscheint, und was ist falsch? ```python datei = open("werte.txt", "w") inhalt = datei.re |
| K11.005 | code_ausgabe | F. 190 | Die Datei `temp.txt` enthält: ```text -0.2 -1.1 -1.4 ``` Was gibt der Code aus? ```python datei = open("temp.t |
| K11.006 | code_ausgabe | F. 190 · Aufg. 6.1 | Die Datei `status.txt` enthält: ```text Presse: OK Fräse: FEHLER ``` Was gibt der Code aus? ```python datei =  |
| K11.007 | unterschied | F. 190 | Was ist der Unterschied zwischen `datei.read()` und `datei.read(10)`? |
| K11.008 | code_fehler | F. 191 · Aufg. 6.1 | Die Datei `teile.txt` enthält: ```text Kolben Ventil ``` Warum erscheint zwischen den Teilen eine Leerzeile, u |
| K11.009 | code_ausgabe | F. 191 · Aufg. 6.1 | Die Datei `teile.txt` enthält: ```text Kolben Ventil Lager ``` Was gibt der Code aus? ```python datei = open(" |
| K11.010 | begriff | F. 191 · Aufg. 6.2 | Welches Zeichen steht am Ende jeder Zeile, die man mit `for zeile in datei:` liest? |
| K11.011 | code_ausgabe | F. 191 · Aufg. 6.1 | Die Datei `teile.txt` enthält (mit Zeilenumbruch am Ende): ```text Kolben Ventil ``` Was gibt der Code aus? `` |
| K11.012 | unterschied | F. 191 | Was ist der Unterschied zwischen `datei.readlines()` und `datei.readline()`? |
| K11.013 | code_ausgabe | F. 194 · Aufg. 6.2 | Was gibt der Code aus? ```python datei = open("log.txt", "w") datei.write("Start") datei.write("Stopp") datei. |
| K11.014 | code_fehler | F. 194 · Aufg. 6.2 | Welche Fehlermeldung erscheint, und wie behebst du sie? ```python drehzahl = 1500 datei = open("log.txt", "w") |
| K11.015 | code_schreiben | F. 194 · Aufg. 6.2 | Schreib die Werte `[20.5, 21.0]` **zeilenweise** in die Datei `messung.txt` (vorhandenen Inhalt überschreiben) |
| K11.016 | code_ausgabe | F. 194 · Aufg. 6.2 | Die Datei `log.txt` enthält vorher (mit Zeilenumbruch am Ende): ```text A ``` Was gibt der Code aus? ```python |
| K11.017 | code_ausgabe | F. 193, 194 · Aufg. 6.2 | Die Datei `log.txt` enthält vorher: ```text A ``` Was gibt der Code aus? Achte auf den Modus. ```python d = op |
| K11.018 | unterschied | F. 193, 194 | Was ist der Unterschied zwischen `open("log.txt", "w")` und `open("log.txt", "a")`? |
| K11.019 | begriff | F. 190, 194 · Aufg. 6.1 | Warum muss eine Datei nach der Arbeit mit `close()` geschlossen werden? |
| K11.020 | code_fehler | F. 194 | Welche Fehlermeldung erscheint? ```python datei = open("log.txt", "w") datei.close() datei.write("Ende\n") ``` |
| K11.021 | code_fehler | F. 189 · Aufg. 6.1 | Im aktuellen Ordner gibt es keine Datei `Beschreibung.txt`. Welche Fehlermeldung erscheint? ```python datei =  |
| K11.022 | begriff | Aufg. 6.1 | Was bedeutet der Pfad `"../Daten/Beschreibung.txt"`? |
| K11.023 | code_ausgabe | F. 191 | Die Datei `werte.txt` enthält: ```text 1.5 2.0 2.5 ``` Was gibt der Code aus? ```python datei = open("werte.tx |
| K11.024 | code_schreiben | F. 187 · Aufg. 6.1 | Zähle, wie viele Zeilen der Datei `log.txt` den Text `FEHLER` enthalten, und gib die Anzahl aus (nutze `find() |
| K11.025 | code_ausgabe | Aufg. 6.2 | Die Datei `werte.txt` enthält: ```text 20,5 21,0 ``` Was gibt der Code aus? ```python datei = open("werte.txt" |
