# Abdeckungsmatrix – Level-Kolloquium 5: Ausnahmebehandlung

Erzeugt mit `werkzeuge/karten.py` aus `ingenieurinformatik1/quellen/level5_karten.yaml`. 23 Karten, 10 prüfbare Inhalte, 0 Wiederholungsfragen.

## Karten je Typ

| Typ | Anzahl |
|---|---:|
| Verwechslungskarte | 1 |
| Klausurfalle | 2 |
| Anwendung (Fall → Einordnung) | 1 |
| Begriff ↔ Erklärung | 3 |
| Lückentext im Code | 1 |
| Was gibt der Code aus? | 8 |
| Finde den Fehler | 1 |
| Schreib Code, der … | 1 |
| Was ist der Unterschied …? | 1 |
| Warum so? (Entscheidung begründen) | 3 |
| Trace-Tabelle (Werte Schritt für Schritt) | 1 |
| **Summe** | **23** |

Karten mit Bild: 0.


## Konzepte → Karten

Gewicht: 3 = in vielen Aufgaben gebraucht, 2 = mehrfach, 1 = selten. F. = Seite im Skript-PDF, Aufg. = Aufgabe im Ordner Informatik-1---Aufgaben-und-Beispiele.

| Konzept | Gewicht | Quelle | Karten | Typen |
|---|---:|---|---|---|
| Ausnahme = Laufzeitfehler; ohne Behandlung Abbruch mit Traceback; typische Ausnahmen und ihre Auslöser | 3 | Laboraufgabe F. 2; Code-Leitfaden 1.10 | L5.001, L5.002 | 2 |
| try/except: Aufbau, Ablauf (Rest des try übersprungen, danach weiter hinter dem Block) | 3 | Labor KW46 (Vorgriff, Code-Leitfaden 2.7) | L5.003, L5.004, L5.005, L5.021 | 4 |
| Konkrete Ausnahme nennen, kein leeres except; falscher Typ wird nicht abgefangen; Strg+C = KeyboardInterrupt | 3 | Code-Leitfaden 2.7 | L5.006, L5.007, L5.008, L5.009 | 4 |
| ValueError bei int()/float() einer ungültigen Eingabe abfangen | 3 | Code-Leitfaden 2.7 | L5.003, L5.008, L5.010, L5.023 | 3 |
| Eingabe wiederholen: Merker eingabe_ok, while not, try/except | 3 | Code-Leitfaden 2.7 | L5.010, L5.011, L5.012 | 3 |
| Wertebereich zusätzlich mit if prüfen (0 → Index -1 ohne Fehler); if vorher prüfen vs. try abfangen | 3 | Code-Leitfaden 2.7 | L5.012, L5.013, L5.014, L5.015, L5.020 | 4 |
| FileNotFoundError beim ersten Laden der Bestenliste; "a" legt die Datei an | 2 | F. 189 · Level-Konzept | L5.016, L5.017 | 2 |
| KeyError abfangen oder vorher mit in prüfen | 1 | Laborskript Dictionaries F. 7 | L5.015, L5.018 | 2 |
| Mehrere except-Zweige; Ausnahme aus einer Funktion wird beim Aufrufer abgefangen | 2 | Labor KW46 (Vorgriff) | L5.019, L5.020, L5.021 | 2 |
| Wo und warum im Level: Koordinaten, Bestenliste, Ton, Tippfehler | 3 | Level-Konzept | L5.022, L5.023 | 2 |

## Annahmen

- try/except kommt im Labor erst in KW46. Bis dahin gilt der Rahmen aus Code-Leitfaden 2.7; die Karten nennen als Quelle „Labor KW46 (Vorgriff)“. `else` und `finally` sind bewusst weggelassen, weil offen ist, ob das Labor sie behandelt.
- Die Fehlermeldungen (`ValueError: invalid literal …`) sind unter Python 3.9 und 3.13 geprüft.

## Karten-Index

| ID | Typ | Folien | Frage |
|---|---|---|---|
| L5.001 | begriff | Laboraufgabe F. 2; Labor KW46 (Vorgriff) | Was ist eine **Ausnahme** (Exception), und was passiert, wenn niemand sie behandelt? |
| L5.002 | verwechslung | F. 175 · Code-Leitfaden 1.10 | Welche Ausnahme löst jede Zeile aus? `int("x")` · `liste[9]` bei 5 Elementen · `tiere["q"]` · `open("fehlt.txt |
| L5.003 | code_ausgabe | Labor KW46 (Vorgriff, Code-Leitfaden 2.7) | Der Spieler tippt `x`. Was gibt der Code aus? ```python try:     reihe = int(input())     print("Reihe", reihe |
| L5.004 | trace | Labor KW46 (Vorgriff, Code-Leitfaden 2.7) | Welche Zeilen laufen bei der Eingabe `3`, welche bei `x`? ```python try:                             # 1     r |
| L5.005 | code_luecke | Labor KW46 (Vorgriff, Code-Leitfaden 2.7) | Ergänze die Ausnahmebehandlung. ```python ___:     spalte = int(input()) ___ ValueError:     print("Bitte eine |
| L5.006 | falle | Code-Leitfaden 2.7 | Der Spieler tippt korrekt `3`. Was gibt der Code aus – und was lernst du daraus? ```python try:     reihe = in |
| L5.007 | code_ausgabe | Code-Leitfaden 2.7 | Der Spieler tippt `x`. Was passiert? ```python try:     reihe = int(input()) except IndexError:     print("Fel |
| L5.008 | code_fehler | Code-Leitfaden 2.7 | Bei Eingabe `3` läuft alles, bei `x` stürzt das Programm mit einer seltsamen Meldung ab. Warum? ```python try: |
| L5.009 | begriff | Labor KW46 (Vorgriff) | Was löst **Strg+C** in der Konsole aus, und wie könntest du es im Level nutzen? |
| L5.010 | code_ausgabe | Aufg. 4.4 · Code-Leitfaden 2.7 | Der Spieler tippt nacheinander `x`, `2,5`, `4`. Was gibt der Code aus? ```python eingabe_ok = False while not  |
| L5.011 | begruenden | Code-Leitfaden 2.7 | Warum steht `eingabe_ok = True` **im** try-Block direkt **nach** `int(input())`? |
| L5.012 | code_schreiben | F. 125 · Code-Leitfaden 2.7, 3.4 | Schreib `zahl_einlesen(kleinste, groesste)`: liest so lange ein, bis eine ganze Zahl im Bereich kommt, und gib |
| L5.013 | falle | F. 141 · Code-Leitfaden 2.7 | Der Spieler tippt `0`. Was passiert? ```python reihe = ["o", "~", "o", "o", "o"] try:     nr = int(input())    |
| L5.014 | code_ausgabe | Labor KW46 (Vorgriff) | Was gibt der Code aus? ```python reihe = ["o", "~", "o"] try:     print(reihe[7]) except IndexError:     print |
| L5.015 | unterschied | Code-Leitfaden 2.5, 2.7 | Wann prüfst du **vorher mit `if`**, wann fängst du **mit `try`/`except`** ab? Je ein Beispiel aus dem Level. |
| L5.016 | code_ausgabe | F. 189 · Labor KW46 (Vorgriff) | Beim ersten Spielstart gibt es noch keine Bestenliste. Was gibt der Code aus? ```python try:     datei = open( |
| L5.017 | begruenden | F. 189, 193 · Level-Konzept | Warum fängst du `FileNotFoundError` beim **Laden** der Bestenliste ab, beim **Speichern** aber nicht? |
| L5.018 | code_ausgabe | Laborskript Dictionaries F. 7 | Was gibt der Code aus? ```python tiere = {"a": "Affe", "t": "Tukan"} try:     print(tiere["x"]) except KeyErro |
| L5.019 | code_ausgabe | Labor KW46 (Vorgriff) | Was gibt der Code aus? ```python def koordinate(text):     return int(text) - 1  try:     print(koordinate("3" |
| L5.020 | code_ausgabe | Labor KW46 (Vorgriff) | Was gibt der Code aus? ```python raster = [["o", "~"], ["~", "o"]] for text in ["2", "x", "5"]:     try:       |
| L5.021 | begriff | Labor KW46 (Vorgriff) | Eine Ausnahme tritt auf. In welcher Reihenfolge sucht Python einen passenden `except`-Zweig – und was passiert |
| L5.022 | anwendung | Level-Konzept | Wo stehen in deinem Level Ausnahmebehandlungen, und welche Ausnahme fängt jede ab? |
| L5.023 | begruenden | Level-Konzept; Code-Leitfaden 2.7 | Kolloquiumsfrage: „Warum steht dein `try` genau um `int(input())` – und welcher Fehler käme ohne?“ |
