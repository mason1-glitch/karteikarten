# Baustein 6: Spruch abtippen und Tippfehler Zeichen für Zeichen zählen
import time

spruch = "Sssalabim sssalabum"
print("Tippe genau:", spruch)
start = time.time()                 # Ergänzung (nicht im Stoff)
eingabe = input("> ")
dauer = time.time() - start

fehler = 0
for i in range(len(spruch)):
    # erst die Länge prüfen: eingabe[i] gäbe sonst einen IndexError
    if i >= len(eingabe) or eingabe[i] != spruch[i]:
        fehler += 1
if len(eingabe) > len(spruch):
    fehler += len(eingabe) - len(spruch)   # zu viel getippte Zeichen

print(f"{fehler} Fehler in {dauer:.1f} s")


# Variante 2 zum Vergleich: dieselbe Zählung mit try/except statt Längenprüfung
def tippfehler_zaehlen(soll, ist):
    """Zählt Abweichungen; fängt den IndexError bei zu kurzer Eingabe ab."""
    fehler = 0
    for i in range(len(soll)):
        try:
            if ist[i] != soll[i]:
                fehler += 1
        except IndexError:
            fehler += 1
    if len(ist) > len(soll):
        fehler += len(ist) - len(soll)   # zu viel getippte Zeichen
    return fehler


print(tippfehler_zaehlen("Zisch", "Zich"))
