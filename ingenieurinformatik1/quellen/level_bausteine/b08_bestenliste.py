# Baustein 8: Bestenliste in einer Datei speichern, laden und selbst sortieren
dateiname = "bestenliste.txt"   # Konstante klein, wie im Code-Leitfaden 2.6


def bestenliste_speichern(name, zeit_s):
    """Hängt einen Eintrag als Zeile "Name;Zeit" an die Datei an."""
    datei = open(dateiname, "a")
    datei.write(f"{name};{zeit_s:.3f}\n")
    datei.close()


def bestenliste_laden():
    """Gibt eine Liste von Dictionaries zurück; leer, wenn es die Datei noch nicht gibt."""
    eintraege = []
    try:
        datei = open(dateiname, "r")
    except FileNotFoundError:
        return eintraege                 # erster Start: noch keine Datei
    for zeile in datei:
        trenner = zeile.find(";")
        try:
            zeit = float(zeile[trenner + 1:])   # \n am Ende stört float() nicht
            eintraege.append({"name": zeile[0:trenner], "zeit": zeit})
        except ValueError:
            print("Kaputte Zeile übersprungen:", zeile[0:trenner])
    datei.close()
    return eintraege


def bestenliste_sortieren(eintraege):
    """Bubble Sort: kleinste Zeit nach vorn; bricht ab, wenn nichts mehr getauscht wird."""
    n = len(eintraege)
    getauscht = True
    durchlauf = 0
    while getauscht:
        getauscht = False
        for j in range(n - 1 - durchlauf):
            if eintraege[j]["zeit"] > eintraege[j + 1]["zeit"]:
                merker = eintraege[j]
                eintraege[j] = eintraege[j + 1]
                eintraege[j + 1] = merker
                getauscht = True
        durchlauf += 1


def top5_zeigen(eintraege):
    """Zeigt höchstens die ersten fünf Einträge."""
    for i in range(len(eintraege)):
        if i < 5:
            print(f"{i + 1}. {eintraege[i]['name']}\t{eintraege[i]['zeit']:.3f} s")


for name, zeit in [("Max", 0.412), ("Lea", 0.298), ("Tom", 0.655), ("Ina", 0.301), ("Ben", 0.5), ("Kim", 0.7)]:
    bestenliste_speichern(name, zeit)
datei = open(dateiname, "a")
datei.write("Ole;schnell\n")     # kaputte Zeile zum Testen
datei.close()
liste = bestenliste_laden()
bestenliste_sortieren(liste)
top5_zeigen(liste)
