# Baustein 4: Wahlreaktion – Gegenrichtung zum Kippen tippen
import random
import time

richtungen = ["LINKS", "RECHTS", "RUHIG"]
# je Kommando die erlaubten Antworten; "" = nur Enter drücken
gegenrichtung = {"LINKS": ["d", "D"], "RECHTS": ["a", "A"], "RUHIG": [""]}

for runde in range(1, 4):
    # beide Grenzen von randint sind möglich -> letzter Index ist len - 1
    kommando = richtungen[random.randint(0, len(richtungen) - 1)]
    start = time.time()   # Ergänzung (nicht im Stoff)
    antwort = input(f"Runde {runde}: Brücke kippt {kommando}! ")
    dauer = time.time() - start
    if dauer < 0.1:   # Enter lag schon im Puffer – sonst gewinnt Dauer-Enter jedes RUHIG
        print("Zu früh gedrückt!")
    elif antwort in gegenrichtung[kommando] and dauer <= 1.5:
        print("Gehalten!")
    elif antwort in gegenrichtung[kommando]:
        print(f"Richtig, aber zu langsam ({dauer:.2f} s)!")
    else:
        print("Falsche Taste - du rutschst ab!")
