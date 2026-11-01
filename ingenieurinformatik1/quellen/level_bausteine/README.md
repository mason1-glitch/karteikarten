# Bausteine für das Dschungel-Reaktionslevel (Welle 1)

Kurze, isolierte Beispiele je Mechanik – **keine fertigen Stationen**, das Level wird selbst geschrieben.
Sie sind die Grundlage der Kolloquiums-Karten `ingenieurinformatik1/karten/level*.csv`:
`werkzeuge/inventar.py` listet jedes Sprachelement darin auf und prüft, ob es eine Karte dazu gibt.

Stil nach Code-Leitfaden: deutsche snake_case-Namen, deutsche Kommentare, alles außerhalb des
Stoffs mit `# Ergänzung (nicht im Stoff): …` markiert. Läuft unter Python 3.9 und 3.13.

**Welle 2 (nach dem Code-Freeze am 26.11.):** dieselbe Prüfung mit dem echten Level-Code:

    python3 werkzeuge/inventar.py abdeckung level_dschungel.py --karten ingenieurinformatik1/quellen/level*_karten.yaml

Jedes Element ohne Karte bekommt dann eine; Karten zu Bausteinen, die im Level anders gelöst sind,
werden durch Karten zu den eigenen Zeilen ersetzt.
