# Baustein 2: Einstellungen aller Stationen in einem verschachtelten Dictionary
# (Muster: Kantinenmenü, Laborskript Dictionaries F. 13)

stationen = {
    "lianen_sprung": {"runden": 3, "zeitlimit_s": 0.8},
    "haengebruecke": {"runden": 5, "zeitlimit_s": 1.5},
    "affen_echo": {"runden": 3, "anzeige_s": 2},
    "zauberformel": {"runden": 2, "zeitlimit_s": 8.0},
    "treibsand": {"runden": 1, "anzeige_s": 3}
}

# Zugriff: erst äußerer Schlüssel, dann innerer
print("Zeitlimit Hängebrücke:", stationen["haengebruecke"]["zeitlimit_s"], "s")

# Wert ändern und neuen Eintrag hinzufügen
stationen["lianen_sprung"]["zeitlimit_s"] = 0.7
stationen["gluehwuermchen"] = {"runden": 2, "anzeige_s": 1}

# Sicherer Zugriff mit in (sonst KeyError)
name = "jaguar"
if name in stationen:
    print(stationen[name])
else:
    print(name, "ist keine Station.")

# Eintrag löschen: del oder pop
del stationen["gluehwuermchen"]
entfernt = stationen.pop("jaguar", "nicht vorhanden")
print("pop lieferte:", entfernt)

# Alle Stationen durchlaufen (wie Aufg. 6.5)
for name, werte in stationen.items():
    print(f"{name}: {werte['runden']} Runde(n)")
