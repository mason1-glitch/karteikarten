# Karteikarten

Karteikarten für die App StudyCards, ein Ordner pro Fach.

**Karten importieren:** CSV aus `<fach>/karten/` herunterladen, in StudyCards *Importieren → CSV* wählen.
**Karten bestellen:** Sitzung mit diesem Repo starten, z. B. „Karteikarten zu Werkstoffkunde: Zugversuch“.
**Bilder:** liegen in `<fach>/bilder/` und werden von den Karten direkt aus diesem Repo geladen – deshalb ist das Repo öffentlich.
**Quellen und Werkzeuge:** Größere Kartensätze entstehen aus einer YAML-Datei in `<fach>/quellen/` mit `werkzeuge/karten.py` (baut die CSV, prüft Abdeckung, Rechnungen und Wortlaut); Schaubilder schneidet `werkzeuge/folienbilder.py` aus dem Skript aus.

Die Arbeitsregeln für Claude stehen in `CLAUDE.md`. Pull Requests werden automatisch per Squash and merge übernommen (`.github/workflows/auto-merge.yml`).

**Bild-Links in Karten:** `https://raw.githubusercontent.com/mason1-glitch/karteikarten/main/<fach>/bilder/<datei>.png`
