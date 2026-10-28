"""Antwortbilder für die Diagramm-Karten (Kapitel 13) im Dunkelstil der App.

Aufruf aus dem Repo-Wurzelordner: python3 ingenieurinformatik1/quellen/diagramme.py
Die Daten entsprechen genau dem Code auf den Karten; nur der Hintergrund ist dunkel (werkzeuge/stil.py).
"""
import os
import sys

WURZEL = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(WURZEL, "werkzeuge"))
from stil import FARBEN, neues_diagramm, speichern  # noqa: E402

ZIEL = os.path.join(WURZEL, "ingenieurinformatik1", "bilder")

# Karte K13: plt.plot(x, y, "r--o")
fig, ax = neues_diagramm(6.4, 4)
ax.plot([1, 2, 3, 4], [2, 4, 6, 8], "r--o")
speichern(fig, os.path.join(ZIEL, "plot_formatstring.png"))

# Karte K13: plt.bar(hallen, verbrauch)
fig, ax = neues_diagramm(6.4, 4)
ax.bar(["Halle 1", "Halle 2", "Halle 3"], [120, 85, 140])
ax.set_title("Stromverbrauch (MWh)", color=FARBEN["text"])
speichern(fig, os.path.join(ZIEL, "plot_balken_hallen.png"))
print("2 Bilder geschrieben")
