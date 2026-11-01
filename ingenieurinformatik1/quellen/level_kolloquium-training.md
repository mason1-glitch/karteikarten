# Kolloquium-Training zum Dschungel-Level (ergänzt die Karten)

Die Karten `ingenieurinformatik1/karten/level1…level8_*.csv` trainieren **Abruf**: Begriffe, Ausgaben, Fehler, Begründungen. Im Kolloquium (Laboraufgabe F. 3: „Fragen zu Ihrem Quellcode“, Einzelnote) kommen drei Dinge dazu, die Karteikarten schlecht abdecken:

1. **Zusammenhängend erklären** – eine ganze Funktion am eigenen Code, ohne vorzulesen.
2. **Live ändern** – eine kleine Änderung unter Beobachtung, danach läuft das Spiel noch.
3. **Rückfragen aushalten** – „Und was, wenn …?“ zu Stellen, an die man selbst nicht gedacht hat.

Dafür sind die Übungen unten. Sie brauchen den **eigenen Level-Code**, sinnvoll also ab dem Code-Freeze (Do 26.11.).

## Stapel parallel zum Bauplan

| Woche | Bau (Level-Konzept) | Karten neu dazu |
|---|---|---|
| KW45 (02.–08.11.) | Absprachen, PAP, Gerüst, Lianen-Sprung | Stapel 1 Auftrag/Schnittstelle, Stapel 3 Zeit/Zufall/Eingabe |
| KW46 (09.–15.11.) | Hängebrücke, Affen-Echo, Stationen-Dictionary, try/except | Stapel 2 Dictionaries, Stapel 5 Ausnahmen (nach dem Labor mit den Folien abgleichen) |
| KW47 (16.–22.11.) | Zauberformel, Treibsand, Bestenliste, Effekte | Stapel 4 Stationen, Stapel 6 Bestenliste/Sortieren, Stapel 7 Effekte |
| KW48 (23.–29.11.) | Zusammenbau, Test, Abgabe | Stapel 8 Kolloquiums-Mix; **Welle 2** (siehe unten) |
| KW49/50 | Kolloquium | alle Stapel gemischt, täglich 10–15 Minuten |

Neue Stapel in StudyCards importieren, sobald das Thema im Bau dran ist – so lernst du, was du gerade programmierst.

## Übungen mit dem eigenen Code

**A – Erklär-Runde (täglich eine Funktion).** Funktion auswählen, Code zuklappen, 60–90 Sekunden laut erklären nach dem 5-Punkte-Schema (Karte L8.001: Zweck, Parameter, Ablauf, Rückgabe, Sonderfälle). Mit dem Handy aufnehmen, anhören, dann mit dem Code vergleichen. Was fehlte, wird eine neue Karte.

**B – Zeilen-Lotterie.** Eine zufällige Zeilennummer ziehen und genau diese Zeile erklären: Was tut sie? Warum steht sie da? Was passiert, wenn sie fehlt? Ziel: jede Zeile in unter 30 Sekunden.

```python
import random
print(random.randint(1, 300))   # Zeilenzahl deiner Level-Datei eintragen
```

**C – Live-Änderung mit Uhr (je 5 Minuten).** Ändern, Spiel starten, prüfen. Jeder Auftrag ist in einer kleinen Änderung lösbar, wenn der Code gut gebaut ist:

1. 5 statt 3 Leben (Antwort: in `main.py`, nicht im Level – Karte L8.005)
2. Treibsand-Raster 4×4
3. Bestenliste absteigend sortieren
4. Zauberformel: Groß-/Kleinschreibung egal (nur mit Stoff-Mitteln!)
5. Neue Station „Glühwürmchen“ einhängen (Gerüst mit `pass` reicht)
6. Zeitlimit der Hängebrücke auf 1,0 s
7. Fehlstart-Schwelle auf 0,15 s
8. Top 3 statt Top 5 anzeigen
9. Affen-Folge bis 6 Zeichen
10. Kaputte Zeile der Bestenliste melden statt still überspringen

**D – Fehler finden.** Jemand aus der Gruppe baut heimlich drei Fehler in eine Kopie deines Levels (z. B. `- 1` vergessen, `>` statt `<`, Merker nie auf `True`). Finden nur mit Traceback lesen, Trace-Ausgaben und Auskommentieren (Karten L8.017–L8.018).

**E – PAP von Hand.** PAP des ganzen Levels und von `reaktion_messen` ohne Vorlage zeichnen und daran erklären (Karten L1.026–L1.027). Im Kolloquium griffbereit haben.

**F – Ergänzungen einzeln erklären.** Jede Stelle, die außerhalb des Stoffs liegt, einmal laut erklären – nach Absprache mit dem Dozenten die Bedingung dafür, dass sie erlaubt sind. Die Liste liefert das Werkzeug:

    python3 werkzeuge/inventar.py code level_dschungel.py

Alles mit „Ergänzung“ in der Spalte *Stoff* muss sitzen (bei den Bausteinen: `time.time`, `flush=True`, `\033`-Farben, `\a`, `winsound`).

**G – Probe-Kolloquium.** 20 Fragen aus `level_probekolloquium.md`, eine andere Person fragt, 15 Minuten, keine Notizen. Ziel: mindestens 18 von 20 vollständig. Jede Lücke wird eine Karte.

## Welle 2 nach dem Code-Freeze (26.11.)

Die Karten aus Welle 1 bauen auf Beispiel-Bausteinen auf (`level_bausteine/`). Wenn dein echter Code steht:

    python3 werkzeuge/inventar.py abdeckung level_dschungel.py --karten ingenieurinformatik1/quellen/level*_karten.yaml --bericht abdeckung.md

Jedes Sprachelement ohne Karte bekommt eine; Karten zu Bausteinen, die du anders gelöst hast, werden durch Karten zu **deinen eigenen Zeilen** ersetzt (gleiche Fragetypen: Was gibt das aus? Warum so? Was passiert bei …? Ändere so, dass …). Ziel bleibt 100 % Abdeckung.
