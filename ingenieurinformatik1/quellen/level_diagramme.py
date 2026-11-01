"""Bilder für die Kolloquiums-Karten zum Dschungel-Level (level*_karten.yaml) im Dunkelstil der App.

Aufruf aus dem Repo-Wurzelordner: python3 ingenieurinformatik1/quellen/level_diagramme.py
- level_pap_reaktion.png      PAP der Funktion reaktion_messen (Baustein 3)
- level_raster_index.png      Spieler zählt ab 1, Python ab 0 (Treibsand-Raster)
- level_bubblesort.png        ein Durchlauf Bubble Sort an vier Reaktionszeiten
"""
import os
import sys

from matplotlib.patches import FancyBboxPatch, Polygon, Rectangle

WURZEL = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(WURZEL, "werkzeuge"))
from stil import FARBEN, neues_diagramm, speichern  # noqa: E402

ZIEL = os.path.join(WURZEL, "ingenieurinformatik1", "bilder")
T = FARBEN["text"]


def text(ax, x, y, s, groesse=12, farbe=T, **kw):
    ax.text(x, y, s, ha="center", va="center", color=farbe, fontsize=groesse, **kw)


def pfeil(ax, x1, y1, x2, y2, beschriftung=None, seite="rechts"):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="-|>", color=FARBEN["grau"], lw=1.6, mutation_scale=16))
    if beschriftung:
        dx = 0.25 if seite == "rechts" else -0.25
        ax.text((x1 + x2) / 2 + dx, (y1 + y2) / 2 + 0.12, beschriftung, color=FARBEN["orange"],
                fontsize=11, ha="left" if seite == "rechts" else "right", va="bottom", fontweight="bold")


def oval(ax, x, y, s, b=3.2, h=0.7):
    ax.add_patch(FancyBboxPatch((x - b / 2, y - h / 2), b, h, boxstyle="round,pad=0,rounding_size=0.35",
                                fc="#1b2a1b", ec=FARBEN["gruen"], lw=2))
    text(ax, x, y, s)


def rechteck(ax, x, y, s, b=4.4, h=0.7):
    ax.add_patch(Rectangle((x - b / 2, y - h / 2), b, h, fc="#16233a", ec=FARBEN["blau"], lw=2))
    text(ax, x, y, s, family="DejaVu Sans Mono", groesse=11)


def parallelogramm(ax, x, y, s, b=4.4, h=0.7):
    v = 0.3
    ax.add_patch(Polygon([(x - b / 2 + v, y + h / 2), (x + b / 2 + v, y + h / 2), (x + b / 2 - v, y - h / 2),
                          (x - b / 2 - v, y - h / 2)], closed=True, fc="#2e2410", ec=FARBEN["orange"], lw=2))
    text(ax, x, y, s, groesse=11)


def raute(ax, x, y, s, b=4.0, h=1.3):
    ax.add_patch(Polygon([(x, y + h / 2), (x + b / 2, y), (x, y - h / 2), (x - b / 2, y)], closed=True,
                         fc="#331616", ec=FARBEN["rot"], lw=2))
    text(ax, x, y, s, family="DejaVu Sans Mono", groesse=11)


def pap_reaktion():
    fig, ax = neues_diagramm(8.2, 10.6, achsen_aus=True)
    ax.set_xlim(-5.2, 6.2)
    ax.set_ylim(1.0, 14.6)
    x = 0
    oval(ax, x, 14, "Start: reaktion_messen(zeitlimit_s)", b=5.6)
    rechteck(ax, x, 12.8, "time.sleep(random.randint(2, 5))", b=5.4)
    rechteck(ax, x, 11.6, "start = time.time()")
    parallelogramm(ax, x, 10.4, "Ausgabe „SPRING!“, Enter abwarten", b=5.4)
    rechteck(ax, x, 9.2, "reaktion = time.time() - start", b=5.4)
    raute(ax, x, 7.6, "reaktion < 0.1 ?")
    parallelogramm(ax, 4.1, 7.6, "„Fehlstart!“", b=2.6)
    oval(ax, 4.1, 6.1, "return None", b=2.6)
    raute(ax, x, 5.2, "reaktion > zeitlimit_s ?", b=5.8)
    parallelogramm(ax, 3.4, 3.6, "„Zu langsam“", b=2.6)
    parallelogramm(ax, -3.0, 3.6, "„Geschafft“", b=2.6)
    oval(ax, x, 1.6, "return reaktion  (Ende)", b=4.2)
    for y1, y2 in [(13.65, 13.15), (12.45, 11.95), (11.25, 10.75), (10.05, 9.55), (8.85, 8.25)]:
        pfeil(ax, x, y1, x, y2)
    pfeil(ax, 2.0, 7.6, 2.75, 7.6)
    ax.text(2.1, 7.75, "Ja", color=FARBEN["orange"], fontsize=11, fontweight="bold")
    pfeil(ax, 4.1, 7.25, 4.1, 6.45)
    pfeil(ax, x, 6.95, x, 5.85, "Nein")
    ax.plot([2.9, 3.4], [5.2, 5.2], color=FARBEN["grau"], lw=1.6)
    pfeil(ax, 3.4, 5.2, 3.4, 3.95)
    ax.text(3.0, 5.32, "Ja", color=FARBEN["orange"], fontsize=11, fontweight="bold")
    ax.plot([-2.9, -3.0], [5.2, 5.2], color=FARBEN["grau"], lw=1.6)
    pfeil(ax, -3.0, 5.2, -3.0, 3.95)
    ax.text(-2.95, 5.32, "Nein", color=FARBEN["orange"], fontsize=11, fontweight="bold", ha="right")
    ax.plot([3.4, 3.4, 0.6], [3.25, 2.5, 2.5], color=FARBEN["grau"], lw=1.6)
    ax.plot([-3.0, -3.0, -0.6], [3.25, 2.5, 2.5], color=FARBEN["grau"], lw=1.6)
    pfeil(ax, 0, 2.5, 0, 1.95)
    ax.plot([-0.6, 0.6], [2.5, 2.5], color=FARBEN["grau"], lw=1.6)
    speichern(fig, os.path.join(ZIEL, "level_pap_reaktion.png"))


def raster_index():
    fig, ax = neues_diagramm(7.6, 6.2, achsen_aus=True)
    ax.set_xlim(-1.6, 5.6)
    ax.set_ylim(-1.6, 6.0)
    for r in range(5):
        for s in range(5):
            markiert = (r, s) == (2, 3)
            ax.add_patch(Rectangle((s, 4 - r), 1, 1, fc="#331616" if markiert else "#111111",
                                   ec=FARBEN["rot"] if markiert else FARBEN["grau"], lw=2.5 if markiert else 1))
            text(ax, s + 0.5, 4 - r + 0.5, f"[{r}][{s}]", groesse=10,
                 farbe=FARBEN["rot"] if markiert else FARBEN["grau"], family="DejaVu Sans Mono")
    for i in range(5):
        text(ax, i + 0.5, 5.35, str(i + 1), groesse=14, farbe=FARBEN["orange"], fontweight="bold")
        text(ax, -0.45, 4 - i + 0.5, str(i + 1), groesse=14, farbe=FARBEN["orange"], fontweight="bold")
    text(ax, 2.5, 5.8, "Spalte (Spieler zählt ab 1)", groesse=12, farbe=FARBEN["orange"])
    ax.text(-1.05, 2.5, "Reihe (Spieler)", rotation=90, color=FARBEN["orange"], fontsize=12, va="center",
            ha="center")
    text(ax, 2.5, -0.55, "Eingabe Reihe 3, Spalte 4  →  raster[3 - 1][4 - 1] = raster[2][3]", groesse=12,
         farbe=FARBEN["rot"])
    text(ax, 2.5, -1.15, "Eingabe 0  →  Index -1 = letztes Feld, KEIN IndexError", groesse=12, farbe=FARBEN["gruen"])
    speichern(fig, os.path.join(ZIEL, "level_raster_index.png"))


def bubblesort():
    werte = [0.41, 0.30, 0.66, 0.29]
    schritte = []
    w = list(werte)
    for j in range(len(w) - 1):
        vorher = list(w)
        tausch = w[j] > w[j + 1]
        if tausch:
            w[j], w[j + 1] = w[j + 1], w[j]
        schritte.append((j, vorher, list(w), tausch))
    fig, ax = neues_diagramm(8.0, 6.4, achsen_aus=True)
    ax.set_xlim(-2.6, 6.4)
    ax.set_ylim(-0.6, 5.0)
    zeilen = [("Start", werte, None, None)] + [(f"j = {j}", nachher, j, t) for j, _, nachher, t in schritte]
    for n, (titel, liste, j, tausch) in enumerate(zeilen):
        y = 4.2 - n * 1.15
        text(ax, -1.5, y + 0.35, titel, groesse=13, farbe=FARBEN["orange"], family="DejaVu Sans Mono")
        for i, v in enumerate(liste):
            aktiv = j is not None and i in (j, j + 1)
            fc = "#331616" if aktiv and tausch else ("#1b2a1b" if aktiv else "#111111")
            ec = FARBEN["rot"] if aktiv and tausch else (FARBEN["gruen"] if aktiv else FARBEN["grau"])
            ax.add_patch(Rectangle((i * 1.2, y), 1.1, 0.7, fc=fc, ec=ec, lw=2))
            text(ax, i * 1.2 + 0.55, y + 0.35, f"{v:.2f}", groesse=13, family="DejaVu Sans Mono")
        if j is not None:
            text(ax, 5.55, y + 0.35, "getauscht" if tausch else "bleibt", groesse=12,
                 farbe=FARBEN["rot"] if tausch else FARBEN["gruen"])
    text(ax, 2.4, -0.35, "Nach Durchlauf 1 steht die größte Zeit hinten.", groesse=12)
    speichern(fig, os.path.join(ZIEL, "level_bubblesort.png"))


pap_reaktion()
raster_index()
bubblesort()
print("3 Bilder geschrieben")
