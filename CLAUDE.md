# Karteikarten für StudyCards

Maschinenbau, Ostfalia (BM1b, PO2025). Karteikarten zum Import in die App StudyCards, dazu die Bilder für die Karten. Ein Ordner pro Fach:

```
<fach>/karten/   CSV-Dateien zum Import, eine pro Kapitel oder Thema
<fach>/bilder/   PNG-Bilder, die in den Karten verlinkt sind
werkzeuge/       stil.py – einheitlicher Diagrammstil
```
Fächer: bwl, mathe1, ingenieurinformatik1, konstruktionsgrundlagen, cad, werkstoffkunde-labor. Für ein neues Fach denselben Aufbau anlegen.

**Dieses Repo ist öffentlich.** Die App lädt die Bilder über öffentliche Links. Skripte (PDF) gehören NICHT hierher, sie liegen im privaten Repo `mason1-glitch/studium` (`<fach>/skripte/`, fertige Lernzettel in `<fach>/lernzettel/`). Dieses Repo bei Bedarf als Quelle hinzuziehen.

## Kartenformat (in der App getestet)
- CSV, UTF-8, **keine Kopfzeile** (sonst wird sie zur Karte).
- Zwei Spalten: Frage, Antwort. Beide Felder immer in `"…"`; Anführungszeichen im Text verdoppeln (`""`).
- Zeilenumbrüche innerhalb eines Feldes sind erlaubt.
- Markdown funktioniert: **fett**, Listen, Tabellen, Absätze.
- **Kein LaTeX** – wird nicht gerendert. Formeln in Unicode schreiben: σ = F / S₀, ε, Δl, ², ≈, ≤, ·, √.
- Bilder als Markdown-Link mit vollem Raw-Link:
  `![Beschreibung](https://raw.githubusercontent.com/mason1-glitch/karteikarten/main/<fach>/bilder/<datei>.png)`
- Dateiname der CSV: `<thema>.csv` bzw. `kap<nr>_<thema>.csv`, nur Kleinbuchstaben, Bindestriche, keine Umlaute.

## Gute Karten (Standard – ein Auftrag im Chat, z. B. ein Rieseberg-Prompt, geht vor)
- Eine Karte = eine abfragbare Sache (Begriff, Formel mit Bedeutung der Größen und Einheiten, Zusammenhang, Diagramm deuten).
- Frage so stellen, dass man aktiv erinnern muss; Antwort knapp, Details als Liste/Tabelle.
- Inhalte aus Skript, Lernzettel oder Besprechung; nichts erfinden. Unklares nachfragen.
- Ergänzungen über das Skript hinaus nur, wenn der Auftrag es verlangt – dann auf der Karte kennzeichnen (z. B. „Ergänzung:“), damit klar ist, was nicht aus dem Skript stammt.

## Bilder
- Bevorzugt selbst zeichnen (Python/matplotlib) mit `werkzeuge/stil.py`: schwarzer Hintergrund, helle Schrift, deutsche Beschriftung – die App läuft im Dunkelmodus, schwarze Schrift auf transparentem Grund ist dort unsichtbar.
- Ausschnitte aus Skripten sind erlaubt (Entscheidung des Repo-Besitzers), aber nur das Nötige, und nur wenn Neuzeichnen nicht sinnvoll ist.
- Format PNG, Dateinamen wie bei den CSVs. Vor dem Commit jedes Bild ansehen: Ist alles lesbar?

## Nach jedem fertigen Kartensatz
1. CSV und Bilder committen. Commit-Nachricht: `Karten <Fach>: <Thema>`.
2. Branch pushen und Pull Request nach `main` erstellen, ohne Nachfrage. Beschreibung kurz: Anzahl Karten, Bilder, offene Fragen. In Cloud-Sitzungen funktioniert `gh pr create` nicht (kein GraphQL) – stattdessen die REST-API: `gh api repos/mason1-glitch/karteikarten/pulls -f title=… -f head=<branch> -f base=main -f body=…`.
3. Der Workflow `.github/workflows/auto-merge.yml` merged jeden PR automatisch per **Squash and merge** und löscht den Branch (dauert ca. 10 Sekunden). Ist er nach etwa einer Minute nicht gemerged, selbst per Squash and merge mergen (`gh api -X PUT repos/mason1-glitch/karteikarten/pulls/<nr>/merge -f merge_method=squash`), ohne auf Bestätigung zu warten. Gilt für alle Änderungen im Repo.
4. Dem Nutzer die Datei als Download schicken, damit er sie direkt importieren kann. Hinweis: Neue Bilder kann GitHub erst nach einigen Minuten ausliefern.
