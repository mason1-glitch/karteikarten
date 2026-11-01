# Baustein 5: Folge merken und nachtippen
import random
import time

tiere = {"a": "Affe", "t": "Tukan", "f": "Frosch"}
tasten = ["a", "t", "f"]
print("Tasten: a = Affe, t = Tukan, f = Frosch")

for laenge in range(3, 6):             # 3, 4, 5 Zeichen
    folge = ""
    for i in range(laenge):
        folge += tasten[random.randint(0, len(tasten) - 1)]
    for taste in folge:
        print(tiere[taste], end=" ")
    print()
    time.sleep(2)
    print("\n" * 40)                   # Folge aus dem Sichtfeld schieben
    eingabe = input("Folge (z. B. atf): ")
    if eingabe == folge:
        print("Die Affen jubeln!")
    else:
        print("Falsch! Richtig war:", folge)
        break
