# Abdeckungsmatrix – Kapitel 8: NumPy-Arrays

Erzeugt mit `werkzeuge/karten.py` aus `ingenieurinformatik1/quellen/kap08_karten.yaml`. 18 Karten, 7 prüfbare Inhalte, 0 Wiederholungsfragen.

## Karten je Typ

| Typ | Anzahl |
|---|---:|
| Begriff ↔ Erklärung | 1 |
| Lückentext im Code | 3 |
| Was gibt der Code aus? | 9 |
| Finde den Fehler | 2 |
| Schreib Code, der … | 1 |
| Was ist der Unterschied …? | 2 |
| **Summe** | **18** |

Karten mit Bild: 0.


## Konzepte → Karten

Gewicht: 3 = in vielen Aufgaben gebraucht, 2 = mehrfach, 1 = selten. F. = Seite im Skript-PDF, Aufg. = Aufgabe im Ordner Informatik-1---Aufgaben-und-Beispiele.

| Konzept | Gewicht | Quelle | Karten | Typen |
|---|---:|---|---|---|
| import numpy as np, np.array() aus Liste (1D/2D), Ausgabeformat | 2 | F. 158, 162 · Aufg. 4.6 | K08.001, K08.002, K08.003, K08.004 | 3 |
| np.zeros(), np.ones(), np.full() mit Form (zeilen, spalten) | 1 | F. 163 · Aufg. 4.6 | K08.005, K08.006 | 2 |
| Zugriff a[i, j], ganze Zeile a[i, :], ganze Spalte a[:, j] | 2 | F. 164 · Aufg. 4.6 | K08.007, K08.008, K08.009 | 3 |
| Ganze Zeile/Spalte auf einen Wert setzen | 1 | F. 165 · Aufg. 4.6 | K08.010, K08.011 | 2 |
| Elementweise Rechnung (Broadcasting), Arrays gleicher Form verrechnen | 2 | F. 166 · Aufg. 4.6 | K08.012, K08.013, K08.014 | 2 |
| NumPy-Array vs. Liste (gleicher Datentyp, Geschwindigkeit, * verhält sich anders) | 1 | F. 159–161 | K08.015, K08.016 | 2 |
| Zuweisung erzeugt keine Kopie – .copy() | 1 | Aufg. 4.6 | K08.017, K08.018 | 2 |

## Annahmen

- Skript F. 164: Der Kommentar „Zugriff auf eine bestimmte Spalte des Arrays (Hier die erste)“ steht über d[:,2] – das ist die dritte Spalte (Index 2), wie auch die Ausgabe [3, 10] zeigt.

## Karten-Index

| ID | Typ | Folien | Frage |
|---|---|---|---|
| K08.001 | code_ausgabe | F. 162 | Was gibt der Code aus? ```python import numpy as np a = np.array([1, 2, 3]) print(a) ``` |
| K08.002 | code_ausgabe | F. 162 | Was gibt der Code aus? ```python import numpy as np b = np.array([[1, 2], [3, 4]]) print(b) ``` |
| K08.003 | begriff | F. 158, 162 · Aufg. 4.6 | Wie importiert man NumPy üblicherweise, und wie wird aus der Liste `[19.5, 20.1]` ein Array? |
| K08.004 | code_fehler | F. 162 | Welche Fehlermeldung erscheint, und was fehlt? ```python a = np.array([1, 2, 3]) print(a) ``` |
| K08.005 | code_ausgabe | F. 163 · Aufg. 4.6 | Was gibt der Code aus? ```python import numpy as np print(np.full((2, 3), 7)) ``` |
| K08.006 | code_luecke | F. 163 | Ergänze, sodass ein Array mit 2 Zeilen und 3 Spalten aus **Nullen** entsteht. ```python import numpy as np a = |
| K08.007 | code_ausgabe | F. 164 · Aufg. 4.6 | Was gibt der Code aus? ```python import numpy as np d = np.array([[1, 2, 3], [4, 5, 6]]) print(d[1, 2]) print( |
| K08.008 | code_luecke | F. 164 | Ergänze, sodass die **dritte Spalte** ausgegeben wird (`[3 6]`). ```python import numpy as np d = np.array([[1 |
| K08.009 | unterschied | F. 164 | Was ist der Unterschied zwischen `d[1, :]` und `d[:, 1]`? |
| K08.010 | code_ausgabe | F. 165 · Aufg. 4.6 | Was gibt der Code aus? ```python import numpy as np t = np.full((2, 3), 20) t[1, :] = 85 print(t) ``` |
| K08.011 | code_schreiben | F. 165 | Erzeuge ein 3×3-Array aus Nullen und setze die **erste Spalte** auf 1 – mit einer einzigen Zuweisung. Gib das  |
| K08.012 | code_ausgabe | F. 166 · Aufg. 4.6 | Was gibt der Code aus? ```python import numpy as np werte = np.array([10.0, 20.0, 30.0]) print(werte * 2) prin |
| K08.013 | code_ausgabe | F. 166 · Aufg. 4.6 | Was gibt der Code aus? ```python import numpy as np ist = np.array([21, 19, 24]) soll = np.array([20, 20, 20]) |
| K08.014 | code_fehler | F. 166 | Welche Fehlermeldung erscheint? ```python import numpy as np a = np.array([1, 2]) b = np.array([1, 2, 3]) prin |
| K08.015 | code_ausgabe | F. 159, 166 | Was gibt der Code aus? ```python import numpy as np liste = [1, 2] arr = np.array([1, 2]) print(liste * 2) pri |
| K08.016 | unterschied | F. 159–161 | Was ist laut Skript der Unterschied zwischen einer Python-Liste und einem NumPy-Array? |
| K08.017 | code_ausgabe | Aufg. 4.6 | Was gibt der Code aus? ```python import numpy as np soll = np.full(3, 20.0) backup = soll backup[0] = 999 prin |
| K08.018 | code_luecke | Aufg. 4.6 | Ergänze, sodass `backup` eine **echte Kopie** ist und `soll` unverändert bleibt. ```python import numpy as np  |
