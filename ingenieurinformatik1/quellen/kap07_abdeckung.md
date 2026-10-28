# Abdeckungsmatrix – Kapitel 7: Listen, 2D-Listen und Tupel

Erzeugt mit `werkzeuge/karten.py` aus `ingenieurinformatik1/quellen/kap07_karten.yaml`. 51 Karten, 18 prüfbare Inhalte, 0 Wiederholungsfragen.

## Karten je Typ

| Typ | Anzahl |
|---|---:|
| Begriff ↔ Erklärung | 5 |
| Lückentext im Code | 7 |
| Was gibt der Code aus? | 21 |
| Finde den Fehler | 7 |
| Schreib Code, der … | 5 |
| Was ist der Unterschied …? | 6 |
| **Summe** | **51** |

Karten mit Bild: 0.


## Konzepte → Karten

Gewicht: 3 = in vielen Aufgaben gebraucht, 2 = mehrfach, 1 = selten. F. = Seite im Skript-PDF, Aufg. = Aufgabe im Ordner Informatik-1---Aufgaben-und-Beispiele.

| Konzept | Gewicht | Quelle | Karten | Typen |
|---|---:|---|---|---|
| Liste anlegen (eckige Klammern, gemischte Typen, leere Liste) | 3 | F. 141–142 · Aufg. 4.2 | K07.001, K07.002, K07.003, K07.004 | 4 |
| Element lesen/ändern über den Index, IndexError | 3 | F. 142–143 · Aufg. 4.2 | K07.005, K07.006, K07.007, K07.008 | 3 |
| append(): Element am Ende anfügen (liefert None) | 2 | F. 144 · Aufg. 4.2, 6.2 | K07.009, K07.010, K07.011, K07.013 | 4 |
| insert(pos, wert): an Position einfügen | 2 | F. 144 · Aufg. 4.2, 5.4 | K07.012, K07.013, K07.014 | 3 |
| pop(index): Element an Position entfernen und zurückgeben | 2 | F. 145 · Aufg. 4.2 | K07.015, K07.016, K07.017, K07.020 | 3 |
| remove(wert): erstes passendes Element löschen | 2 | F. 145 · Aufg. 4.2 | K07.018, K07.019, K07.020 | 3 |
| index(wert): Position eines Werts | 1 | F. 146 · Aufg. 4.2 | K07.021, K07.022 | 2 |
| count(), sort(), reverse(), clear() | 1 | F. 145–146 | K07.023, K07.024 | 2 |
| sort(key=funktion, reverse=…): nach eigenem Kriterium sortieren | 1 | F. 147 | K07.025, K07.026 | 2 |
| Liste durchlaufen: for x in liste / for i in range(len(liste)) | 3 | F. 143, 148, 152 · Aufg. 3.8, 4.4 | K07.027, K07.028, K07.029, K07.030 | 4 |
| in: prüfen, ob ein Wert in der Liste ist | 1 | F. 119 · Aufg. 3.8 | K07.031, K07.032 | 2 |
| enumerate(): Index und Element zugleich | 1 | Aufg. 4.4 | K07.033, K07.034 | 2 |
| 2D-Liste: matrix[zeile][spalte] | 2 | F. 150–151 · Aufg. 4.3–4.5 | K07.035, K07.036, K07.037, K07.038 | 3 |
| Verschachtelte Schleifen über eine 2D-Liste | 2 | F. 151–152 · Aufg. 4.3–4.5 | K07.039, K07.040, K07.041 | 3 |
| List-Comprehension zum Anlegen von Listen/Rastern | 1 | Aufg. 4.3 | K07.042, K07.043 | 2 |
| Benutzereingabe ab 1 → Index ab 0 (reihe - 1) | 2 | Aufg. 4.3, 4.5 | K07.044, K07.045, K07.046 | 3 |
| Tupel: unveränderlich, runde Klammern, Entpacken | 1 | F. 155 · Aufg. 5.2, 5.6 | K07.047, K07.048, K07.049 | 3 |
| Zuweisung kopiert keine Liste/kein Array (Referenz) – .copy() | 1 | Aufg. 4.6 | K07.050, K07.051 | 2 |

## Annahmen

- Das Kopieren mit .copy() zeigt Aufg. 4.6 an NumPy-Arrays und sagt, dass es für Listen genauso gilt; die Karten nutzen liste.copy().

## Karten-Index

| ID | Typ | Folien | Frage |
|---|---|---|---|
| K07.001 | code_ausgabe | F. 142 | Was gibt der Code aus? ```python teile = ["Kolben", "Dichtung", 13, True] print(teile) print(len(teile)) ``` |
| K07.002 | begriff | F. 141, 142 | Was ist eine **Liste** in Python? |
| K07.003 | code_schreiben | F. 141 · Aufg. 4.2 | Gegeben sind `t1 = 20.1`, `t2 = 20.4`, `t3 = 19.8`. Fasse die drei Werte in **einer Liste** zusammen und gib s |
| K07.004 | unterschied | F. 142, 156, 157 | Was ist laut Skript der Unterschied zwischen einer Python-**Liste** und einem **Array** in vielen anderen Spra |
| K07.005 | code_ausgabe | F. 143 | Was gibt der Code aus? ```python druecke = [2.0, 2.5, 3.1, 2.8] print(druecke[1]) print(druecke[-1]) ``` |
| K07.006 | code_ausgabe | F. 142 · Aufg. 4.2 | Was gibt der Code aus? ```python lager = ["Kolben", "Ventil", "Lager"] lager[1] = "Feder" print(lager) ``` |
| K07.007 | code_fehler | F. 141 | Welche Fehlermeldung erscheint? ```python werte = [5, 7, 9] print(werte[3]) ``` |
| K07.008 | code_luecke | F. 142 | Das **letzte** Element soll auf 0 gesetzt werden. Ergänze den Index. ```python werte = [4, 8, 15] werte[___] = |
| K07.009 | code_ausgabe | F. 144 | Was gibt der Code aus? ```python messungen = [] messungen.append(20.5) messungen.append(21.0) print(messungen) |
| K07.010 | code_schreiben | F. 144 · Aufg. 4.2 | Lies mit einer for-Schleife **drei** Messwerte (Kommazahlen) ein, sammle sie in einer Liste und gib die Liste  |
| K07.011 | code_fehler | F. 144 | Was gibt der Code aus, und warum? ```python messungen = [1.2] messungen = messungen.append(1.4) print(messunge |
| K07.012 | code_ausgabe | F. 144 | Was gibt der Code aus? ```python teile = ["A", "B", "C"] teile.insert(1, "X") print(teile) ``` |
| K07.013 | unterschied | F. 144 · Aufg. 5.4 | Was ist der Unterschied zwischen `liste.append(x)` und `liste.insert(0, x)`? |
| K07.014 | code_luecke | F. 144 · Aufg. 5.4 | Jede neue Ziffer soll **vorne** in die Liste. Ergänze die Lücke. ```python ziffern = [] for z in [1, 2, 3]:    |
| K07.015 | code_ausgabe | F. 145 · Aufg. 4.2 | Was gibt der Code aus? ```python teile = ["A", "B", "C", "D"] teile.pop(1) print(teile) ``` |
| K07.016 | code_ausgabe | F. 145 | Was gibt der Code aus? ```python auftraege = [101, 102, 103] naechster = auftraege.pop(0) print(naechster, auf |
| K07.017 | code_fehler | F. 145 | Welche Fehlermeldung erscheint? ```python teile = ["A", "B"] teile.pop(2) ``` |
| K07.018 | code_ausgabe | F. 145 | Was gibt der Code aus? ```python schrauben = ["M6", "M8", "M6"] schrauben.remove("M6") print(schrauben) ``` |
| K07.019 | code_fehler | F. 145 | Welche Fehlermeldung erscheint? ```python teile = ["Welle", "Lager"] teile.remove("Ventil") ``` |
| K07.020 | unterschied | F. 145 · Aufg. 4.2 | Was ist der Unterschied zwischen `liste.pop(2)` und `liste.remove(2)`? |
| K07.021 | code_ausgabe | F. 146 · Aufg. 4.2 | Was gibt der Code aus? ```python lager = ["Kolben", "Ventil", "Lager"] print(lager.index("Lager")) ``` |
| K07.022 | code_schreiben | F. 146 · Aufg. 4.2 | Ersetze in `lager = ["Kolben", "Ventil", "Lager"]` das Teil `"Ventil"` durch `"Feder"`, **ohne** die Position  |
| K07.023 | code_ausgabe | F. 146 | Was gibt der Code aus? ```python bohrungen = [6, 8, 6, 10] print(bohrungen.count(6)) ``` |
| K07.024 | code_luecke | F. 146, 147 | Die Liste soll **absteigend** sortiert werden. Ergänze den Parameter. ```python werte = [12, 40, 7] werte.sort |
| K07.025 | code_ausgabe | F. 147 | Was gibt der Code aus? ```python def laenge(e):     return len(e)  teile = ["Welle", "Bolzen", "Rad"] teile.so |
| K07.026 | begriff | F. 147 | Was bewirkt der Parameter `key` bei `liste.sort(key=funktion)`? |
| K07.027 | code_ausgabe | F. 152 · Aufg. 4.4 | Was gibt der Code aus? ```python kanaele = ["T1", "", "T3"] for i in range(len(kanaele)):     if kanaele[i] != |
| K07.028 | unterschied | F. 143, 152 | Was ist der Unterschied zwischen `for x in liste:` und `for i in range(len(liste)):`? |
| K07.029 | code_fehler | F. 143 | Alle Werte sollen verzehnfacht werden. Was gibt der Code aus, und wie korrigierst du ihn? ```python werte = [1 |
| K07.030 | code_schreiben | F. 148 | Schreib eine Funktion `m_pro_s(kmh)`, die km/h in m/s umrechnet (÷ 3.6), und gib damit für jede Geschwindigkei |
| K07.031 | code_ausgabe | F. 119 · Aufg. 3.8 | Was gibt der Code aus? ```python gesperrt = [7, 9] print(8 in gesperrt) print(9 in gesperrt) ``` |
| K07.032 | code_luecke | F. 119 · Aufg. 3.8 | Nur Stationen, die **nicht** gesperrt sind, werden freigegeben. Ergänze die Lücke. ```python gesperrt = [7, 9] |
| K07.033 | code_ausgabe | Aufg. 4.4 | Was gibt der Code aus? ```python for nr, teil in enumerate(["Kolben", "Ventil"]):     print(nr, teil) ``` |
| K07.034 | unterschied | Aufg. 4.4 | Was ist der Unterschied zwischen `for i in range(len(teile)):` und `for i, teil in enumerate(teile):`? |
| K07.035 | code_ausgabe | F. 151 | Was gibt der Code aus? ```python raster = [[11, 12, 13], [21, 22, 23]] print(raster[1][0]) print(raster[0][2]) |
| K07.036 | code_ausgabe | F. 150, 152 | Was gibt der Code aus? ```python lager = [["A", "-"], ["-", "B"], ["C", "-"]] print(len(lager)) print(len(lage |
| K07.037 | code_luecke | F. 151 · Aufg. 4.3 | `"Feder"` soll in die **zweite Zeile, erste Spalte**. Ergänze die Indizes. ```python lager = [["-", "-"], ["-" |
| K07.038 | begriff | F. 150, 151 | Wie ist eine zweidimensionale Liste aufgebaut, und was bedeuten die Indizes in `matrix[i][j]`? |
| K07.039 | code_ausgabe | F. 151 | Was gibt der Code aus? ```python raster = [[1, 2], [3, 4]] for zeile in raster:     summe = 0     for wert in  |
| K07.040 | code_schreiben | F. 152 · Aufg. 4.4 | Suche in `lager = [["A", "-"], ["-", "B"]]` das Teil `"B"` und gib seine Position **ab 1 gezählt** aus (`Reihe |
| K07.041 | begriff | F. 151, 152 · Aufg. 4.3 | Wie oft wird der innere Rumpf zweier verschachtelter Schleifen über ein Raster mit 8 Zeilen und 8 Spalten ausg |
| K07.042 | code_ausgabe | Aufg. 4.3 | Was gibt der Code aus? ```python raster = [[0 for s in range(3)] for r in range(2)] print(raster) ``` |
| K07.043 | code_luecke | Aufg. 4.3 | Ergänze, sodass eine Liste mit **fünf Nullen** entsteht. ```python werte = [0 for i in ___] print(werte) ``` |
| K07.044 | code_fehler | Aufg. 4.3 | Der Nutzer möchte in **Reihe 2, Spalte 1** einlagern (er zählt ab 1). Welche Fehlermeldung erscheint, und was  |
| K07.045 | code_ausgabe | Aufg. 4.5 | Was gibt der Code aus? ```python lager = [["A", "B"], ["C", "D"]] reihe = 1 spalte = 2 print(lager[reihe - 1][ |
| K07.046 | begriff | Aufg. 4.3, 4.5 | Warum schreibt man bei Benutzereingaben `lager[reihe - 1][spalte - 1]`? |
| K07.047 | unterschied | F. 155 | Was ist der Unterschied zwischen einer **Liste** und einem **Tupel**? |
| K07.048 | code_fehler | F. 155 | Welche Fehlermeldung erscheint? ```python abmessungen = (120, 80, 40) abmessungen[0] = 125 ``` |
| K07.049 | code_ausgabe | F. 155 · Aufg. 5.6 | Was gibt der Code aus? ```python punkt = (3.5, 7.0) x, y = punkt print(y) ``` |
| K07.050 | code_ausgabe | Aufg. 4.6 | Was gibt der Code aus? ```python toleranzen = [0.1, 0.2, 0.1] reserve = toleranzen reserve[0] = 0.5 print(tole |
| K07.051 | code_luecke | Aufg. 4.6 | `reserve` soll eine **unabhängige** Kopie sein, damit `toleranzen` unverändert bleibt. Ergänze die Lücke. ```p |
