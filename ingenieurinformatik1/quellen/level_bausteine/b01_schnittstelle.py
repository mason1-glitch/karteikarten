# Baustein 1: Schnittstelle zwischen main.py und dem Level
# Das spieler-Dictionary legt main.py an; jedes Level bekommt es übergeben.


def leben_abziehen(spieler):
    """Zieht ein Leben ab und meldet den neuen Stand."""
    spieler["leben"] -= 1   # verändert das Dictionary des Aufrufers (kein global nötig)
    print(f"Autsch! Noch {spieler['leben']} Leben.")


def level_dschungel_reflexe(spieler):
    """Spielt das Level; gibt True zurück, wenn der Spieler es geschafft hat."""
    print(f"{spieler['name']} flieht durch den Dschungel ...")
    leben_abziehen(spieler)            # Platzhalter für eine verpatzte Station
    if spieler["leben"] > 0:
        spieler["inventar"].append("Ziffer 7")
        return True
    return False


# === So nutzt main.py das Level ===
spieler = {"name": "Max", "leben": 3, "inventar": [], "punkte": 0}
geschafft = level_dschungel_reflexe(spieler)
if geschafft:
    print("Level geschafft! Inventar:", spieler["inventar"])
else:
    print("Game over.")
