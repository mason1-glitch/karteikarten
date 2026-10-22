"""Einheitlicher Diagrammstil für StudyCards (Dunkelmodus).

Verwendung:
    import sys; sys.path.insert(0, "werkzeuge")
    from stil import neues_diagramm, speichern, FARBEN
    fig, ax = neues_diagramm()
    ax.plot(x, y, color=FARBEN["blau"], lw=3)
    speichern(fig, "werkstoffkunde-labor/bilder/beispiel.png")
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

FARBEN = {
    "hintergrund": "#000000",
    "text": "#e6e6e6",
    "grau": "#9a9a9a",
    "blau": "#4a90e2",
    "orange": "#f5a623",
    "gruen": "#7ed321",
    "rot": "#ff6b6b",
}


def neues_diagramm(breite=8, hoehe=5.2, achsen_aus=False):
    """Figur mit schwarzem Hintergrund und hellen Achsen."""
    fig, ax = plt.subplots(figsize=(breite, hoehe), dpi=150)
    fig.patch.set_facecolor(FARBEN["hintergrund"])
    ax.set_facecolor(FARBEN["hintergrund"])
    for seite in ax.spines.values():
        seite.set_color(FARBEN["grau"])
    ax.tick_params(colors=FARBEN["text"], labelsize=11)
    ax.xaxis.label.set_color(FARBEN["text"])
    ax.yaxis.label.set_color(FARBEN["text"])
    ax.title.set_color(FARBEN["text"])
    if achsen_aus:
        ax.axis("off")
    return fig, ax


def speichern(fig, pfad):
    fig.savefig(pfad, facecolor=FARBEN["hintergrund"], bbox_inches="tight")
    plt.close(fig)
