# Baustein 7: 5x5-Raster, kurz zeigen, Koordinate sicher einlesen
import random
import time

# "o" = Stein, "~" = Treibsand
raster = [["o" for spalte in range(5)] for reihe in range(5)]
for reihe in range(5):
    raster[reihe][random.randint(0, 4)] = "~"   # je Reihe ein Treibsandfeld


def raster_zeigen(raster):
    """Gibt das Raster mit Reihen- und Spaltennummern aus."""
    print("  1 2 3 4 5")
    for i in range(len(raster)):
        print(i + 1, end=" ")
        for feld in raster[i]:
            print(feld, end=" ")
        print()


def zahl_einlesen(text, kleinste, groesste):
    """Liest eine ganze Zahl im Bereich ein und fragt bei Fehlern erneut."""
    eingabe_ok = False
    while not eingabe_ok:
        try:
            zahl = int(input(text))
            if zahl >= kleinste and zahl <= groesste:   # 0 wäre Index -1, kein Fehler!
                eingabe_ok = True
            else:
                print(f"Nur {kleinste} bis {groesste}!")
        except ValueError:
            print("Bitte eine ganze Zahl eingeben!")
    return zahl


raster_zeigen(raster)
time.sleep(3)
print("\n" * 40)
reihe = zahl_einlesen("Reihe (1-5): ", 1, 5)
spalte = zahl_einlesen("Spalte (1-5): ", 1, 5)
if raster[reihe - 1][spalte - 1] == "~":   # Spieler zählt ab 1, Python ab 0
    print("Du versinkst im Treibsand!")
else:
    print("Fester Stein.")
