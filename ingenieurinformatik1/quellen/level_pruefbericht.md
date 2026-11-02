# Prüfbericht – Kolloquiums-Karten zum Dschungel-Level (Welle 1)

Kartensatz: `ingenieurinformatik1/karten/level1…level8_*.csv`, **213 Karten** in 8 Stapeln, Quelle je Stapel in `quellen/level<n>_karten.yaml`.
Grundlage: Laboraufgabe WS26, Labor-Einführung, Laborskript Dictionaries, Laborfolien IDE/venv, Skript Info1 WS26, Code-Leitfaden, Level-Konzept „Escape-Room – mein Dschungel-Reaktionslevel“.

## Abnahmekriterien

| Kriterium | Ergebnis |
|---|---|
| Jedes Sprachelement der Bausteine hat mindestens eine Karte (`werkzeuge/inventar.py abdeckung`) | **82 von 82 (100 %)** – Bericht: `level_abdeckung_code.md` |
| Jede Ausgabe-, Fehler- und Trace-Karte gegen die echte Ausführung geprüft (`werkzeuge/karten.py code`) | **273 Ausführungen unter Python 3.9 und 3.13, 0 Fehler**; 2 Karten mit echten Wartezeiten sind stattdessen im Baustein `b03` mit verzögerter Eingabe getestet |
| Jede Ergänzung außerhalb des Stoffs auf der Karte als „Ergänzung“ markiert (`werkzeuge/inventar.py karten`) | erfüllt, alle 8 Stapel |
| Unabhängiges Probe-Kolloquium: 20 Fragen eines Prüfers ohne Kenntnis der Karten | 1. Durchgang → 14 neue Karten; Gegenprobe nur mit den Karten: **16 von 20 voll, 74 von 78 Antwortpunkten**; die 5 verbliebenen Lücken sind danach mit eigenen Karten geschlossen |
| Unabhängige Sachprüfung aller Kartentexte | 16 Befunde (2 falsch, 14 missverständlich) – alle korrigiert |
| CSV-Format (keine Kopfzeile, 2 Spalten, kein LaTeX, alle Bilder vorhanden) | erfüllt |

## Stapel

| Stapel | Datei | Karten | Inhalt |
|---|---|---:|---|
| 1 | `level1_auftrag-schnittstelle.csv` | 29 | Pflichtelemente, Bewertung, Aufbau, `spieler`-Dictionary, `return`, `global`, Module, Konventionen, PAP |
| 2 | `level2_dictionaries.csv` | 25 | Zugriff, `in`, `del`/`pop`, verschachtelt, `items()`, Einsatz im Level |
| 3 | `level3_zeit-zufall-eingabe.csv` | 24 | `random`, `time.sleep`, `time.time()`, `input()`, Fehlstart, Eingabepuffer, Formatierung, `None` |
| 4 | `level4_stationen.csv` | 32 | Affen-Echo, Zauberformel, Hängebrücke, Treibsand-Raster (2D-Liste), Runden und Leben |
| 5 | `level5_ausnahmen.csv` | 25 | `try`/`except`, konkrete Ausnahmen, Eingabeschleife, Bereich mit `if`, Dateien |
| 6 | `level6_bestenliste-sortieren.csv` | 39 | Dateimodi, Lesen/Zerlegen, Bubble Sort, `sort()`, Top 5, Rekursion |
| 7 | `level7_effekte.csv` | 18 | Escape-Sequenzen, ASCII-Bilder, `flush`, Farben, Ton, `requirements.txt` |
| 8 | `level8_kolloquium-mix.csv` | 21 | Erklären (5-Punkte-Schema), Ändern auf Zuruf, Datentypen, Gültigkeit, Fehlersuche, Grenzfälle |

Kartentypen: Was gibt der Code aus? 60 · Warum so? 24 · Schreib Code 23 · Falle 22 · Begriff 18 · Finde den Fehler 16 · Anwendung 14 · Unterschied 12 · Lückentext 8 · Trace-Tabelle 6 · Sonstige 10.

## Offene Punkte (vor dem Kolloquium klären)

- **Labor KW45/KW46 sind Vorgriff:** Sortieralgorithmen/Rekursion (Stapel 6) und Ausnahmebehandlung (Stapel 5) stützen sich auf Code-Leitfaden 2.7, weil die Laborfolien noch fehlen. Nach dem Labor mit den Folien abgleichen (welcher Sortieralgorithmus, ob `else`/`finally` behandelt werden).
- **PAP-Symbole** (L1.026) folgen DIN 66001 – mit den Folien aus KW43 abgleichen.
- **Muss jeder Teil alle Pflichtelemente enthalten?** Steht nicht auf den Folien; die Karten gehen vom sicheren Fall aus.
- **Welle 2 nach dem Code-Freeze (26.11.):** `inventar.py abdeckung` mit dem echten Level-Code laufen lassen, Lücken mit Karten schließen, Karten zu anders gelösten Bausteinen durch Karten zu den eigenen Zeilen ersetzen; Probe-Kolloquium (`level_probekolloquium.md`) auf den eigenen Code umschreiben.
