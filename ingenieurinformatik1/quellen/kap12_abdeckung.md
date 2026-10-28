# Abdeckungsmatrix – Kapitel 12: CSV-Dateien und pandas

Erzeugt mit `werkzeuge/karten.py` aus `ingenieurinformatik1/quellen/kap12_karten.yaml`. 18 Karten, 7 prüfbare Inhalte, 0 Wiederholungsfragen.

## Karten je Typ

| Typ | Anzahl |
|---|---:|
| Begriff ↔ Erklärung | 5 |
| Lückentext im Code | 5 |
| Was gibt der Code aus? | 6 |
| Finde den Fehler | 2 |
| **Summe** | **18** |

Karten mit Bild: 0.


## Konzepte → Karten

Gewicht: 3 = in vielen Aufgaben gebraucht, 2 = mehrfach, 1 = selten. F. = Seite im Skript-PDF, Aufg. = Aufgabe im Ordner Informatik-1---Aufgaben-und-Beispiele.

| Konzept | Gewicht | Quelle | Karten | Typen |
|---|---:|---|---|---|
| CSV-Format: ein Datensatz pro Zeile, Trennzeichen, Kopfzeile | 1 | F. 198 · Aufg. 6.3 | K12.001, K12.002 | 2 |
| pd.read_csv() → DataFrame; Spaltennamen exakt (KeyError) | 2 | F. 199–201 · Aufg. 6.3–6.5 | K12.002, K12.003, K12.004, K12.005 | 4 |
| DataFrame aus Dictionary, Spalte df["Name"], len(df), head() | 2 | F. 200 · Aufg. 6.3, 6.4 | K12.006, K12.007, K12.008, K12.009 | 3 |
| Zeilen filtern: df[df["Spalte"] > wert] | 2 | F. 200 · Aufg. 6.3–6.5 | K12.010, K12.011, K12.012 | 3 |
| sort_values(by=…, ascending=…) | 2 | Aufg. 6.3, 6.4 | K12.013, K12.014 | 2 |
| groupby("A")["B"].mean() – Mittelwert je Gruppe | 1 | F. 200 · Aufg. 6.3 | K12.015, K12.016 | 2 |
| value_counts() – Häufigkeit jedes Werts | 1 | Aufg. 6.5 | K12.017, K12.018 | 2 |

## Annahmen

- Die Ausgaben wurden mit pandas 2.3 und 3.1 geprüft. Ältere pandas-Versionen (vor 2.0) benennen das Ergebnis von value_counts() anders; deshalb fragt keine Karte nach dessen vollständiger Ausgabe.

## Karten-Index

| ID | Typ | Folien | Frage |
|---|---|---|---|
| K12.001 | begriff | F. 198 | Was ist eine **CSV-Datei**? |
| K12.002 | code_ausgabe | F. 198, 201 · Aufg. 6.3 | Die Datei `messung.csv` enthält: ```text Zeit,Temperatur,Druck 0,20.1,1.01 10,22.4,1.03 20,24.9,1.06 ``` Was g |
| K12.003 | code_luecke | F. 201 · Aufg. 6.3 | Ergänze die Funktion, die eine CSV-Datei in einen DataFrame einliest. ```python import pandas as pd df = pd.__ |
| K12.004 | code_fehler | Aufg. 6.3 | Die Kopfzeile von `autos.csv` lautet `Marke,Baujahr,Kraftstoffverbrauch (l/100km)`. Welche Fehlermeldung ersch |
| K12.005 | begriff | F. 199, 200 | Wofür setzt man die Bibliothek **pandas** im Ingenieurbereich ein? |
| K12.006 | code_ausgabe | Aufg. 6.3 | Was gibt der Code aus? ```python import pandas as pd daten = {"Sensor": ["T1", "T2"],          "Wert": [21.5,  |
| K12.007 | code_luecke | Aufg. 6.3 | Ergänze, sodass nur die Spalte **Druck** ausgegeben wird. ```python import pandas as pd df = pd.DataFrame({"Pu |
| K12.008 | begriff | Aufg. 6.3 | Was ist ein **DataFrame** in pandas? |
| K12.009 | code_luecke | Aufg. 6.3, 6.4 | Nach dem Einlesen sollen nur die **ersten fünf Zeilen** zur Kontrolle angezeigt werden. Ergänze die Methode. ` |
| K12.010 | code_ausgabe | F. 200 · Aufg. 6.3 | Was gibt der Code aus? ```python import pandas as pd daten = {"Bauteil": ["Welle", "Lager", "Gehäuse"],        |
| K12.011 | code_luecke | Aufg. 6.4 | Es sollen nur die Zeilen der Fertigungslinie `"B"` übrig bleiben. Ergänze den Operator. ```python import panda |
| K12.012 | code_fehler | Aufg. 6.3 | Gewünscht sind die **Zeilen** mit einer Temperatur über 80 °C. Was erscheint stattdessen, und wie lautet der r |
| K12.013 | code_ausgabe | Aufg. 6.3 | Was gibt der Code aus? ```python import pandas as pd df = pd.DataFrame({"Lager": ["L1", "L2", "L3"],           |
| K12.014 | code_luecke | Aufg. 6.3, 6.4 | Die Bohrungen sollen **aufsteigend** nach Durchmesser `d` sortiert werden. Ergänze das Argument. ```python imp |
| K12.015 | code_ausgabe | F. 200 · Aufg. 6.3 | Was gibt der Code aus? ```python import pandas as pd daten = {"Anlage": ["Ofen", "Kessel", "Ofen"],          " |
| K12.016 | begriff | F. 200 · Aufg. 6.3 | Was berechnet `df.groupby("Schicht")["Ausschuss"].mean()`? |
| K12.017 | code_ausgabe | Aufg. 6.5 | Was gibt der Code aus? ```python import pandas as pd codes = ["E1", "E3", "E1", "E1"] df = pd.DataFrame({"Fehl |
| K12.018 | begriff | Aufg. 6.5 | Was liefert `df["Fehler"].value_counts()`? |
