# Baustein 3: Reaktionszeit messen (Kern von Lianen-Sprung und Hängebrücke)
import random
import time


def eingabepuffer_leeren():
    """Verwirft Enter-Drücke, die noch im Eingabepuffer liegen."""
    dauer = 0
    while dauer < 0.3:          # sofort zurückgekehrtes input() = alter Tastendruck
        start = time.time()     # Ergänzung (nicht im Stoff): Zeit in Sekunden
        input("Bereit? Weiter mit Enter ")
        dauer = time.time() - start


def reaktion_messen(zeitlimit_s):
    """Gibt die Reaktionszeit in s zurück oder None bei Fehlstart."""
    print("Halte dich an der Liane fest ...")
    time.sleep(random.randint(2, 5))   # zufällig, damit niemand den Moment rät
    start = time.time()                # Ergänzung (nicht im Stoff)
    input("SPRING! (Enter) ")
    reaktion = time.time() - start
    if reaktion < 0.1:                 # Enter lag schon im Puffer
        print("Fehlstart!")
        return None
    if reaktion > zeitlimit_s:
        print(f"Zu langsam: {reaktion:.3f} s")
    else:
        print(f"Geschafft in {reaktion:.3f} s")
    return reaktion


eingabepuffer_leeren()
zeit = reaktion_messen(0.8)
if zeit is not None:
    print("Gemessen:", zeit > 0)
