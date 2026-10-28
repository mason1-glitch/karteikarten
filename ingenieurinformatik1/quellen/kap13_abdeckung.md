# Abdeckungsmatrix – Kapitel 13: Daten visualisieren mit matplotlib und plotly

Erzeugt mit `werkzeuge/karten.py` aus `ingenieurinformatik1/quellen/kap13_karten.yaml`. 27 Karten, 11 prüfbare Inhalte, 0 Wiederholungsfragen.

## Karten je Typ

| Typ | Anzahl |
|---|---:|
| Begriff ↔ Erklärung | 4 |
| Lückentext im Code | 7 |
| Was gibt der Code aus? | 2 |
| Finde den Fehler | 4 |
| Schreib Code, der … | 7 |
| Was ist der Unterschied …? | 3 |
| **Summe** | **27** |

Karten mit Bild: 2.


## Konzepte → Karten

Gewicht: 3 = in vielen Aufgaben gebraucht, 2 = mehrfach, 1 = selten. F. = Seite im Skript-PDF, Aufg. = Aufgabe im Ordner Informatik-1---Aufgaben-und-Beispiele.

| Konzept | Gewicht | Quelle | Karten | Typen |
|---|---:|---|---|---|
| import matplotlib.pyplot as plt, plt.plot(x, y), plt.show() | 2 | F. 205 · Aufg. 2.1, 2.9 | K13.001, K13.002, K13.003 | 3 |
| Linienstil: Formatstring "b-o", color, linestyle, linewidth, marker | 1 | F. 206 · Aufg. 2.1 | K13.004, K13.005 | 2 |
| title, xlabel, ylabel, grid – vor show() | 2 | F. 205 · Aufg. 2.1, 6.1, 6.5 | K13.006, K13.007, K13.008 | 3 |
| label=… und plt.legend() | 1 | F. 205 · Aufg. 2.1, 6.5 | K13.009, K13.010 | 2 |
| Balkendiagramm plt.bar(kategorien, werte) | 2 | F. 207 · Aufg. 6.1, 6.5 | K13.011, K13.012, K13.013 | 3 |
| Histogramm plt.hist(daten, bins=…) | 1 | F. 207 · Aufg. 6.5 | K13.014, K13.015 | 2 |
| Streudiagramm plt.scatter(x, y) | 1 | Aufg. 6.5 | K13.016, K13.017 | 2 |
| Mehrere Diagramme: fig, (ax1, ax2) = plt.subplots(1, 2), ax.set_title, tight_layout | 1 | Aufg. 6.5 | K13.018, K13.019 | 2 |
| plt.savefig("datei.png", dpi=…) vor plt.show() | 1 | F. 208 · Aufg. 6.5 | K13.020, K13.021 | 2 |
| x und y müssen gleich lang sein (ValueError) | 1 | F. 205 | K13.022, K13.023 | 2 |
| plotly.express: px.line, px.scatter_3d(color=…), update_layout, fig.show() | 1 | F. 209 · Aufg. 6.4 | K13.024, K13.025, K13.026, K13.027 | 4 |

## Annahmen

- Skript F. 208: savefig lege die Grafik „im Speicherort des Programmskripts“ ab. Tatsächlich landet eine Datei ohne Pfad im aktuellen Arbeitsordner (in Jupyter meist der Ordner des Notebooks); beides stimmt nur überein, wenn das Programm aus seinem eigenen Ordner gestartet wird. Die Karte nennt den Arbeitsordner und die Abweichung.

## Karten-Index

| ID | Typ | Folien | Frage |
|---|---|---|---|
| K13.001 | code_schreiben | F. 205 · Aufg. 2.1 | Zeichne den Temperaturverlauf `stunden = [8, 9, 10]`, `temp = [72, 78, 81]` als **Liniendiagramm** und zeige e |
| K13.002 | code_luecke | F. 205 · Aufg. 2.9 | Ergänze die Funktion, die die Kraft über dem Weg als **Linie** zeichnet. ```python import matplotlib.pyplot as |
| K13.003 | begriff | F. 205 | Was ist **pyplot**, und wie wird es üblicherweise importiert? |
| K13.004 | code_ausgabe | F. 206 · Aufg. 2.1 | Wie sieht die gezeichnete Weg-Zeit-Linie aus? ```python import matplotlib.pyplot as plt t = [1, 2, 3, 4]  # Ze |
| K13.005 | code_luecke | F. 206 | Der Ausschuss pro Tag soll als grüne, **gestrichelte** Linie mit Kreis-Markern erscheinen. Ergänze den Liniens |
| K13.006 | code_luecke | F. 205 · Aufg. 2.1 | Ergänze die Funktion, die die **x-Achse** beschriftet. ```python import matplotlib.pyplot as plt plt.plot([8,  |
| K13.007 | code_fehler | F. 205 | Was ist an der Beschriftung dieses Diagramms falsch? ```python import matplotlib.pyplot as plt zeit = [0, 10,  |
| K13.008 | code_schreiben | F. 205 · Aufg. 2.1, 6.1 | Zeichne die Punkte `[8, 9, 10]` / `[72, 78, 81]` als Linie mit Titel `Temperaturverlauf`, Achsenbeschriftungen |
| K13.009 | code_schreiben | F. 205 · Aufg. 2.1 | Zeichne Soll- und Ist-Temperatur in **ein** Diagramm – `[60, 60, 60]` als „Soll“ und `[52, 58, 61]` als „Ist“  |
| K13.010 | code_fehler | F. 205 | Die Legende bleibt leer. Was fehlt? ```python import matplotlib.pyplot as plt plt.plot([1, 2, 3], [20, 22, 21] |
| K13.011 | code_ausgabe | F. 207 · Aufg. 6.5 | Welches Diagramm entsteht? ```python import matplotlib.pyplot as plt hallen = ["Halle 1", "Halle 2", "Halle 3" |
| K13.012 | code_luecke | F. 207 · Aufg. 6.1 | Die Stückzahlen der drei Schichten sollen als Diagramm mit **senkrechten Balken (Säulen)** erscheinen. Ergänze |
| K13.013 | code_schreiben | F. 207 · Aufg. 6.5 | `df` hat eine Spalte `Status` (z. B. „OK“, „Ausschuss“). Zeichne ein Balkendiagramm mit der **Anzahl der Teile |
| K13.014 | begriff | F. 207 · Aufg. 6.5 | Was zeigt ein **Histogramm**, und was legt `bins` fest? |
| K13.015 | code_luecke | F. 207 · Aufg. 6.5 | Ergänze den Parameter, sodass das Histogramm der gemessenen Durchmesser **4 Klassen** hat. ```python import ma |
| K13.016 | unterschied | F. 205 · Aufg. 6.5 | Was ist der Unterschied zwischen `plt.plot(x, y)` und `plt.scatter(x, y)`? |
| K13.017 | code_schreiben | Aufg. 6.5 | Stelle `drehzahl = [1000, 2000, 3000]` (x) gegen `vibration = [0.8, 1.5, 2.9]` (y) als **Streudiagramm** mit A |
| K13.018 | code_schreiben | Aufg. 6.5 | Zeige ein Liniendiagramm und ein Balkendiagramm **nebeneinander** in einer Abbildung, jeweils mit eigenem Tite |
| K13.019 | unterschied | Aufg. 6.5 | Was ist der Unterschied zwischen `plt.title("…")` und `ax1.set_title("…")`? |
| K13.020 | code_fehler | F. 208 · Aufg. 6.5 | Die gespeicherte Datei `stueckzahl.png` ist leer. Warum? ```python import matplotlib.pyplot as plt plt.bar(["L |
| K13.021 | code_luecke | F. 208 · Aufg. 6.5 | Die Federkennlinie soll mit **300 dpi** als PNG gespeichert werden. Ergänze den Parameter. ```python import ma |
| K13.022 | code_fehler | F. 205 | Welche Fehlermeldung erscheint? ```python import matplotlib.pyplot as plt zeit = [0, 1, 2] temp = [20, 25] plt |
| K13.023 | begriff | F. 205 | Welche Bedingung müssen die Listen `x` und `y` bei `plt.plot(x, y)` erfüllen? |
| K13.024 | code_luecke | Aufg. 6.4 | Ergänze die plotly-Funktion, die den Drehzahlverlauf als **Liniendiagramm** aus dem DataFrame zeichnet. ```pyt |
| K13.025 | code_schreiben | F. 209 · Aufg. 6.4 | Lies `pruefstand.csv` (Spalten `Motor`, `Drehzahl`, `Drehmoment`, `Temperatur`) ein und erstelle einen **3D-St |
| K13.026 | unterschied | F. 204, 209 · Aufg. 6.4, 6.5 | Was ist der Unterschied zwischen Diagrammen aus **matplotlib** und aus **plotly express**? |
| K13.027 | begriff | Aufg. 6.4 | Wie änderst du bei einem fertigen plotly-Diagramm `fig` nachträglich den Titel? |
