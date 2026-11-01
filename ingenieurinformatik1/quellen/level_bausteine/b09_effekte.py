# Baustein 9: Effekte für Extrapunkte (Bilder, Farben, Sound) und ein rekursiver Countdown
import time

affe_bild = """
   .-"-.
 _/.-.-.\\_
( ( o o ) )
 |/  "  \\|
"""

gruen = "\033[32m"   # Ergänzung (nicht im Stoff): ANSI-Farbcode
normal = "\033[0m"   # Ergänzung: Farbe zurücksetzen


def countdown(n):
    """Zählt rekursiv von n bis 1 herunter und ruft dann LOS."""
    if n <= 0:                      # Abbruchbedingung (<= fängt auch negative n ab)
        print("LOS!   ")
        return
    print(n, "...", end="\r", flush=True)   # \r: Zeilenanfang; Ergänzung: flush
    time.sleep(0.2)
    countdown(n - 1)                # Selbstaufruf mit kleinerem n


def langsam_schreiben(text):
    """Gibt den Text Zeichen für Zeichen aus (Schreibmaschinen-Effekt)."""
    for zeichen in text:
        print(zeichen, end="", flush=True)   # Ergänzung: flush=True zeigt sofort an
        time.sleep(0.02)
    print()


def ton_abspielen():
    """Piept unter Windows; auf anderen Systemen läuft das Spiel still weiter."""
    try:
        import winsound            # Ergänzung (nicht im Stoff): gibt es nur unter Windows
        winsound.Beep(880, 200)
    except ImportError:
        print("\a", end="")        # Ergänzung: Signalton, falls die Konsole ihn erlaubt
    except RuntimeError:
        pass                       # Windows ohne Tonausgabe: still weiterspielen


print(affe_bild)
countdown(3)
langsam_schreiben("Die Affen rufen ...")
print(gruen + "Geschafft!" + normal)
ton_abspielen()
