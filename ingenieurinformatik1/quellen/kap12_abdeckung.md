# Abdeckungsmatrix – Kapitel 12: CSV-Dateien und pandas

Erzeugt mit `werkzeuge/karten.py` aus `ingenieurinformatik1/quellen/kap12_karten.yaml`. 17 Karten, 7 prüfbare Inhalte, 0 Wiederholungsfragen.

## Karten je Typ

| Typ | Anzahl |
|---|---:|
| Begriff ↔ Erklärung | 5 |
| Lückentext im Code | 4 |
| Was gibt der Code aus? | 6 |
| Finde den Fehler | 2 |
| **Summe** | **17** |

Karten mit Bild: 0.


## Konzepte → Karten

Gewicht: 3 = in vielen Aufgaben gebraucht, 2 = mehrfach, 1 = selten. F. = Seite im Skript-PDF, Aufg. = Aufgabe im Ordner Informatik-1---Aufgaben-und-Beispiele.

| Konzept | Gewicht | Quelle | Karten | Typen |
|---|---:|---|---|---|
| CSV-Format: ein Datensatz pro Zeile, Trennzeichen, Kopfzeile | 1 | F. 198 · Aufg. 6.3 | K12.001, K12.002 | 2 |
| pd.read_csv() → DataFrame; Spaltennamen exakt (KeyError) | 2 | F. 199–201 · Aufg. 6.3–6.5 | K12.002, K12.003, K12.004, K12.005 | 4 |
| DataFrame aus Dictionary, Spalte df["Name"], len(df), head() | 2 | F. 200 · Aufg. 6.3, 6.4 | K12.006, K12.007, K12.008 | 3 |
| Zeilen filtern: df[df["Spalte"] > wert] | 2 | F. 200 · Aufg. 6.3–6.5 | K12.009, K12.010, K12.011 | 3 |
| sort_values(by=…, ascending=…) | 2 | Aufg. 6.3, 6.4 | K12.012, K12.013 | 2 |
| groupby("A")["B"].mean() – Mittelwert je Gruppe | 1 | F. 200 · Aufg. 6.3 | K12.014, K12.015 | 2 |
| value_counts() – Häufigkeit jedes Werts | 1 | Aufg. 6.5 | K12.016, K12.017 | 2 |

## Annahmen

- Die Ausgaben wurden mit pandas 2.3 und 3.1 geprüft. Ältere pandas-Versionen (vor 2.0) benennen das Ergebnis von value_counts() anders; deshalb fragt keine Karte nach dessen vollständiger Ausgabe.

## Karten-Index

| ID | Typ | Folien | Frage |
|---|---|---|---|
| K12.001 | begriff | F. 198 | Was ist eine **CSV-Datei**? |
| K12.002 | code_ausgabe | F. 198, 201 · Aufg. 6.3 | Die Datei `autos.csv` enthält: ```text Marke,Baujahr,Verbrauch BMW,2015,9.2 VW,2019,5.9 Audi,2020,6.4 ``` Was  |
| K12.003 | code_luecke | F. 201 · Aufg. 6.3 | Ergänze die Funktion, die eine CSV-Datei in einen DataFrame einliest. ```python import pandas as pd df = pd.__ |
| K12.004 | code_fehler | Aufg. 6.3 | Die Kopfzeile von `autos.csv` lautet `Marke,Baujahr,Kraftstoffverbrauch (l/100km)`. Welche Fehlermeldung ersch |
| K12.005 | begriff | F. 199, 200 | Wofür setzt man die Bibliothek **pandas** im Ingenieurbereich ein? |
| K12.006 | code_ausgabe | Aufg. 6.3 | Was gibt der Code aus? ```python import pandas as pd daten = {"Maschine": ["Presse", "Fräse"],          "Stund |
| K12.007 | code_luecke | Aufg. 6.3 | Ergänze, sodass nur die Spalte **Stunden** ausgegeben wird. ```python import pandas as pd df = pd.DataFrame({" |
| K12.008 | begriff | Aufg. 6.3 | Was ist ein **DataFrame** in pandas, und was liefert `df.head()`? |
| K12.009 | code_ausgabe | F. 200 · Aufg. 6.3 | Was gibt der Code aus? ```python import pandas as pd df = pd.DataFrame({"Teil": ["A", "B", "C"],               |
| K12.010 | code_luecke | Aufg. 6.4 | Es sollen nur die Zeilen der Anlage `"Machine 1"` übrig bleiben. Ergänze den Operator. ```python import pandas |
| K12.011 | code_fehler | Aufg. 6.3 | Gewünscht sind die **Zeilen** mit Kosten über 4000. Was erscheint stattdessen, und wie lautet der richtige Fil |
| K12.012 | code_ausgabe | Aufg. 6.3 | Was gibt der Code aus? ```python import pandas as pd df = pd.DataFrame({"Teil": ["A", "B", "C"],               |
| K12.013 | code_luecke | Aufg. 6.3, 6.4 | Die Fahrzeuge sollen **aufsteigend** nach CO2-Ausstoß sortiert werden. Ergänze das Argument. ```python import  |
| K12.014 | code_ausgabe | F. 200 · Aufg. 6.3 | Was gibt der Code aus? ```python import pandas as pd daten = {"Maschine": ["Presse", "Fräse", "Presse"],       |
| K12.015 | begriff | F. 200 · Aufg. 6.3 | Was berechnet `df.groupby("Stadt")["Umsatz"].mean()`? |
| K12.016 | code_ausgabe | Aufg. 6.5 | Was gibt der Code aus? ```python import pandas as pd marken = ["VW", "BMW", "VW", "VW"] df = pd.DataFrame({"Ma |
| K12.017 | begriff | Aufg. 6.5 | Was liefert `df["Marke"].value_counts()`, und wie nutzt man es für ein Balkendiagramm? |
