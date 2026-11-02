# Probe-Kolloquium zum Dschungel-Level (20 Prüferfragen)

Erstellt von einem unabhängigen Prüfer-Agenten, der die Karten **nicht** kannte – nur Laboraufgabe, Level-Konzept und die Bausteine. Gedacht für Übung G in `level_kolloquium-training.md`: Eine andere Person stellt die Fragen, 15 Minuten, keine Notizen; Ziel 18 von 20 vollständig.

**Zeilenangaben** beziehen sich auf die Bausteine im ersten Stand (erster Commit des Pull Requests, vor der Überarbeitung). Mehrere Schwächen, nach denen hier gefragt wird, sind in den Bausteinen inzwischen behoben (F09 Dauer-Enter bei „RUHIG“, F12 überzählige Zeichen, F16 Zeile ohne Semikolon, F18 negative Werte, F19 `flush` im Countdown, F20 `RuntimeError`) – als Übung trotzdem wertvoll: Schwäche erkennen, Lösung erklären. **In Welle 2** die Fragen auf die Zeilen des eigenen Level-Codes umschreiben.

Typen: **[E]** Erklären, **[W]** Warum so?, **[?]** Was passiert wenn?, **[Ä]** Live-Änderung, **[G]** Python-Grundlagen, **[P]** Pflichtelement oder außerhalb des Stoffs, **[U]** unbequem (deckt eine Schwäche oder Grenze auf).

---

## F01 [P][U] Pflichtelemente, Kennzeichnung, Konventionen

**Frage:** Nennen Sie die Pflichtelemente der Laboraufgabe und zeigen Sie mir für jedes eine Stelle in Ihrem Code. In keiner Ihrer Dateien finde ich eine Autor-Kennzeichnung. Woran erkenne ich, welcher Code von Ihnen stammt? Außerdem sind Hängebrücke, Affen-Echo und Treibsand in Ihren Bausteinen lose Schleifen und keine Funktionen. Wie passt das zu "eine Funktion je Station"? Und warum steht die Konstante `dateiname` klein geschrieben?

**Bezug:** b06 Z. 25-29, b07 Z. 25-32, b08 Z. 15-18 und 23-25 (Ausnahmen); b02 Z. 4-10, b04 Z. 7, b05 Z. 5 (Dictionaries); b08 Z. 30-43 (Sortieren); b09 Z. 15-22 (Rekursion); b04 Z. 9-20, b05 Z. 8-22, b07 Z. 36-44 (freier Code); b08 Z. 1 (Konstante).

**Eine volle Antwort enthält:**
- Pflicht: Ausnahmebehandlung, Kontrollstrukturen, Funktionen, dazu mindestens eines aus Dictionaries, Rekursion, Sortieralgorithmen. Der Student belegt jedes mit Datei und Zeile und weiß, dass hier alle drei Wahlelemente vorkommen.
- Die Aufgabe verlangt, Code-Anteile je Teilnehmendem per Kommentar zu kennzeichnen. Er erklärt, wie er das im Gruppencode macht (Autor-Kommentar je Funktion oder Datei) und gibt zu, dass die Bausteine das noch nicht tun.
- Er gibt zu, dass Stationen als Funktionen mit Rückgabe True oder False gedacht sind (`level_dschungel_reflexe` in b01 ist nur ein Platzhalter) und dass die losen Schleifen beim Zusammenbau in Funktionen wandern.
- Er nennt die verbindlichen Code-Konventionen (Leitfaden bzw. Labor) und räumt ein, wo sie von PEP 8 abweichen (Konstanten klein statt GROSS), mit Begründung.

---

## F02 [E][G] Gültigkeit von Variablen und veränderbare Objekte

**Frage:** In Zeile 5 heißt der Parameter `spieler`, in Zeile 22 gibt es ebenfalls eine Variable `spieler`. Sind das dieselben? Warum steht in Zeile 7 kein `global`, obwohl die Funktion den Spielstand verändert? Was würde passieren, wenn dort `spieler = {...}` stünde, oder wenn statt des Dictionarys eine Zahl `leben` übergeben würde?

**Bezug:** b01 Z. 5-8, 11-18, 22-23

**Eine volle Antwort enthält:**
- Zwei Namen in zwei Gültigkeitsbereichen: Der Parameter ist lokal in der Funktion, Z. 22 ist global. Beim Aufruf zeigt der Parameter auf dasselbe Dictionary-Objekt.
- Ein Dictionary ist veränderbar (mutable). `spieler["leben"] -= 1` verändert nur den Inhalt und weist den Namen nicht neu zu, daher ist kein `global` nötig.
- Eine Zuweisung `spieler = {...}` in der Funktion legt eine neue lokale Variable an, und das Original bleibt unverändert. Eine Zahl (int) ist unveränderbar: `leben -= 1` ändert nur die lokale Variable, und der Aufrufer sieht nichts, also bräuchte man `return`.
- Er sagt, was `main.py` mit dem Rückgabewert True oder False des Levels macht.

---

## F03 [?][U] Leben, Wiederholung und Inventar

**Frage:** Was passiert in Ihrem Level, wenn `leben_abziehen` bei 0 Leben aufgerufen wird? Wo genau entscheiden Sie "Game over"? Und was steht in `spieler["leben"]` und im Inventar, wenn der Spieler das Level nach einem Misserfolg noch einmal spielen darf?

**Bezug:** b01 Z. 5-8 (kein Check), Z. 14-18 (Entscheidung und `append`), Z. 22

**Eine volle Antwort enthält:**
- `leben_abziehen` prüft nicht auf 0, die Leben können negativ werden ("Noch -1 Leben."). Die Entscheidung steht verstreut in der Level-Funktion (`> 0`, Z. 15), und der Student sieht, dass bei mehreren Stationen die Prüfung nach jeder Station nötig ist.
- Beim Wiederholen werden die Leben nicht zurückgesetzt (die Gruppenregel dazu ist offen). "Ziffer 7" wird bei jedem Durchlauf erneut ins Inventar gehängt, also doppelt, und die Ziffer ist fest einprogrammiert statt von `main.py` vergeben.
- Verbesserungen: mit `in` prüfen, ob die Ziffer schon im Inventar liegt; Leben nicht unter 0 fallen lassen; klare Gruppenregel für Leben pro Level oder pro Spiel.

---

## F04 [E][?] Verschachteltes Dictionary, KeyError, `del` und `pop`

**Frage:** Erklären Sie Zeile 13 und Zeile 16-17. Was passiert bei `stationen["treibsand"]["zeitlimit_s"]` und was bei `del stationen["jaguar"]`? Warum steht in Zeile 28 `pop` mit zweitem Argument? Was sind `name` und `werte` in Zeile 32?

**Bezug:** b02 Z. 4-10, 13, 16-17, 20-24, 27-28, 32-33

**Eine volle Antwort enthält:**
- Zugriff verschachtelt: erst der äußere Schlüssel, dann der innere. Dictionaries werden über Schlüssel angesprochen und nicht über Positionen. Zuweisung an einen vorhandenen Schlüssel ändert den Wert, an einen neuen Schlüssel legt sie einen Eintrag an.
- `stationen["treibsand"]["zeitlimit_s"]` löst einen KeyError aus, denn Treibsand hat nur `anzeige_s`. Die Stationen haben also uneinheitliche Schlüssel. `in` prüft nur die äußere Ebene.
- `del` mit fehlendem Schlüssel löst KeyError aus. `pop(schlüssel, standardwert)` liefert den Standardwert und liefert sonst den entfernten Wert.
- `.items()` liefert Schlüssel-Wert-Paare (Tupel-Entpacken in der Schleife). `name` aus Z. 20 wird in Z. 32 überschrieben, das ist kein Fehler, aber eine globale Variable wird wiederverwendet.

---

## F05 [W][U] Wozu das Dictionary, wenn die Stationen es nicht lesen?

**Frage:** Ihr Dictionary `stationen` setzt für den Lianen-Sprung 0.7 s fest. Aber `reaktion_messen(0.8)` wird mit 0.8 aufgerufen, die Hängebrücke läuft mit `range(1, 4)` (drei Runden) statt der 5 Runden aus dem Dictionary, das Affen-Echo hat `sleep(2)` fest eingebaut und die 8.0 s der Zauberformel prüft niemand. Wofür dann das Dictionary? Zeigen Sie, wie die Hängebrücke ihre Runden und ihr Zeitlimit daraus bekommt.

**Bezug:** b02 Z. 4-10 und 16; b03 Z. 33; b04 Z. 9 und 15; b05 Z. 8 und 15; b06 Z. 4-18; b07 Z. 37

**Eine volle Antwort enthält:**
- Ehrliche Antwort: In den Bausteinen sind die Werte noch fest einprogrammiert und widersprechen dem Dictionary. Im fertigen Level müssen sie aus `stationen[...]` kommen.
- Nutzen: Alle Einstellwerte stehen an einer Stelle, Feintuning ändert nur das Dictionary, und es gibt keine "magischen Zahlen" im Code.
- Konkrete Zeile: `range(1, stationen["haengebruecke"]["runden"] + 1)` mit Begründung für das `+ 1` (Endwert von `range` ist exklusiv), und `stationen["haengebruecke"]["zeitlimit_s"]` statt `1.5`.
- Er erkennt das Risiko uneinheitlicher Schlüssel (`zeitlimit_s` oder `anzeige_s`), die zu einem KeyError führen können.

---

## F06 [E][P][?] Reaktionszeit messen, `time.time()`, Fehlstart, Rückgabe None

**Frage:** Erklären Sie `reaktion_messen` Zeile für Zeile. Was liefert `time.time()`, und warum bilden Sie eine Differenz? Was passiert technisch, wenn der Spieler schon während des `sleep` Enter drückt, und warum ist 0.1 s die Grenze? Warum geben Sie bei Fehlstart `None` zurück, und was passiert in Zeile 35, wenn dort `zeit > 0` ohne die Prüfung `is not None` stünde, oder wenn der Wert an `bestenliste_speichern` ginge?

**Bezug:** b03 Z. 15-29 und 33-35; b08 Z. 5-9

**Eine volle Antwort enthält:**
- `time.time()` liefert die Sekunden seit dem 1.1.1970 als float. Nur die Differenz zweier Zeitpunkte ist die Reaktionszeit. Das liegt außerhalb des Stoffs (im Stoff: `sleep`, `strftime`, `datetime.now`) und ist im Code als Ergänzung gekennzeichnet.
- `sleep` blockiert nur das Programm, nicht die Tastatur. Das Enter landet im Eingabepuffer, `input()` kehrt sofort zurück, und die Zeit ist fast 0. Eine menschliche Reaktion liegt bei etwa 0.15 bis 0.25 s, die Schwelle von 0.1 s ist eine begründete Annahme.
- Das Zeitlimit wird erst nach dem Enter geprüft, weil `input()` sich nicht abbrechen lässt. Auch bei "Zu langsam" wird die Zeit zurückgegeben, der Aufrufer kann das nicht unterscheiden. Die Funktion liefert also float oder None.
- `None > 0` löst einen TypeError aus, ebenso `f"{None:.3f}"` beim Speichern. Deshalb gehört `is not None` davor, und ein Fehlstart darf nie in die Bestenliste.

---

## F07 [E][?] `eingabepuffer_leeren` und `dauer = 0`

**Frage:** Erklären Sie die Funktion. Warum steht vor der Schleife `dauer = 0`? Was passiert, wenn ein sehr schneller Spieler schon nach 0.2 s Enter drückt? Ruft `reaktion_messen` die Funktion selbst auf, und was geschieht, wenn man den Aufruf vergisst?

**Bezug:** b03 Z. 6-12, 32-33

**Eine volle Antwort enthält:**
- `dauer = 0` sorgt dafür, dass die Schleifenbedingung `dauer < 0.3` beim ersten Mal wahr ist (Python hat keine Schleife mit Prüfung am Ende). Die `while`-Schleife läuft also mindestens einmal.
- Idee: Ein `input()`, das in weniger als 0.3 s zurückkehrt, ist ein alter Enter-Druck im Puffer und wird verworfen. Dann wird neu gefragt, bis der Spieler bewusst bestätigt.
- Grenze: Ein sehr schneller Spieler wird ohne Erklärung erneut gefragt, und jede Eingabe unter 0.3 s wird verworfen, auch Text mit Enter. Die Funktion ersetzt kein echtes Leeren des Puffers.
- `reaktion_messen` ruft sie nicht selbst auf, der Aufruf muss vor jeder Runde stehen, sonst können Fehlstarts aus der vorigen Runde stammen. `start` und `dauer` sind lokal.

---

## F08 [Ä][G] Wartezeit in Zehntelsekunden

**Frage:** `random.randint(2, 5)` ergibt nur die Wartezeiten 2, 3, 4 oder 5 Sekunden. Das kann ein Spieler mitzählen. Ändern Sie die Zeile bitte so, dass die Wartezeit zwischen 2.0 und 5.0 Sekunden in Zehntelsekunden-Schritten liegt.

**Bezug:** b03 Z. 18

**Eine volle Antwort enthält:**
- Beide Grenzen von `randint` sind möglich, also 4 mögliche Werte. Der Zweck der Zufallswartezeit ist, dass niemand den Moment erraten kann.
- Lösung: `time.sleep(random.randint(20, 50) / 10)`. Er begründet, dass `/` einen float liefert (`//` wäre ganzzahlig) und `sleep` auch float akzeptiert.
- Alternative `random.uniform(2, 5)` ist nicht im Stoff. Er begründet, warum er die randint-Variante wählt, und kann erklären, dass Fehlstart-Erkennung und Messung unverändert bleiben.

---

## F09 [?][U][G] Hängebrücke: Wie gewinnt man "RUHIG" ohne zu reagieren?

**Frage:** Wie kann ein Spieler die Runde "RUHIG" gewinnen, ohne die Meldung gelesen zu haben? Welche Prüfung fehlt hier gegenüber b03? Und warum steht in `gegenrichtung` eine Liste `["d", "D"]` statt eines Strings `"dD"`?

**Bezug:** b04 Z. 5-7, 12-20; Vergleich b03 Z. 22

**Eine volle Antwort enthält:**
- Ein Enter, das schon im Puffer liegt (frühere Runde oder Dauerdruck), lässt `input()` sofort `""` liefern. Das ist bei "RUHIG" die richtige Antwort, `dauer` ist fast 0 und damit `<= 1.5`, also "Gehalten!". Wer bei jeder Runde Enter hämmert, gewinnt jedes "RUHIG".
- In b04 fehlen die Mindestzeit (Fehlstart unter 0.1 s) und das Leeren des Puffers vor der Runde. Mit Fehlstart-Prüfung und `eingabepuffer_leeren` ließe sich das beheben. Außerdem kostet eine falsche Antwort hier noch kein Leben.
- `in` bei einem String prüft auf Teilstrings: `"" in "dD"` ist True, daher wäre bei LINKS ein bloßes Enter richtig, ebenso "dD". Bei einer Liste muss die Antwort exakt einem Element gleichen.
- Eine Eingabe wie `"d "` (mit Leerzeichen) gilt als falsch, denn es gibt keine Bereinigung der Eingabe.

---

## F10 [Ä][W] Affen-Echo: Papagei hinzufügen

**Frage:** Fügen Sie bitte live einen vierten Laut hinzu: Taste "p" für den Papagei. Welche Stellen müssen Sie ändern? Was passiert, wenn Sie eine vergessen? Und wie erfährt der Spieler, welche Taste zu welchem Tier gehört?

**Bezug:** b05 Z. 5-6, 8-14, 17

**Eine volle Antwort enthält:**
- Änderungen: `tiere` um `"p": "Papagei"` und `tasten` um `"p"` ergänzen, dazu `random.randint(0, 2)` ändern. Das `2` ist fest eingebaut, ohne Änderung käme der Papagei nie vor. Besser `random.randint(0, len(tasten) - 1)` (wie in b04) und die Redundanz beseitigen (`tasten` und `tiere` enthalten dieselbe Information, z. B. `list(tiere)`).
- Mit `randint(0, 3)` und der alten Liste käme es zu einem IndexError, weil beide Grenzen von `randint` inklusive sind.
- `folge += ...` baut einen String auf, Strings sind unveränderlich (jedes `+=` erzeugt einen neuen String), `for taste in folge` läuft über die Zeichen.
- Im Code erfährt der Spieler die Tastenbelegung nicht. Die Folge zeigt Tiernamen, eingegeben werden Buchstaben, und der Hinweis fehlt. Der Student erkennt das und benennt die Abhilfe (Hinweiszeile mit der Belegung).

---

## F11 [?][U] Affen-Echo: Abschreiben und die 40 Leerzeilen

**Frage:** Was passiert, wenn der Spieler seine Antwort schon eintippt und Enter drückt, während die Folge noch zwei Sekunden auf dem Bildschirm steht? Muss er sich dann überhaupt etwas merken? Und was ist, wenn das Konsolenfenster 60 Zeilen hoch ist oder der Spieler nach oben scrollt?

**Bezug:** b05 Z. 12-17

**Eine volle Antwort enthält:**
- `sleep(2)` hält nur das Programm an. Die Tastatureingaben werden gepuffert und vom nächsten `input()` übernommen. Der Spieler kann die Folge abtippen, während sie sichtbar ist, und das "Merken" entfällt.
- `print("\n" * 40)` schiebt den Text nur nach oben. Bei einem höheren Fenster bleibt die Folge sichtbar, und mit Scrollen kommt man an sie heran. Ein echtes Löschen des Bildschirms (`os.system`, ANSI-Code) liegt außerhalb des Stoffs.
- Abhilfe: Eingabepuffer nach dem Ausblenden leeren (Eingaben unter 0.3 s verwerfen wie in b03), mehr Leerzeilen. Er sagt klar, dass die Konsole mit dem Stoff keine echte Zeitkontrolle der Eingabe erlaubt.
- Nebenbei: Beim ersten Fehler bricht `break` ab, ohne Leben-Abzug und ohne Rückgabewert, und der Vergleich unterscheidet Groß- und Kleinschreibung ("ATF" ist falsch).

---

## F12 [W][U][?] Zauberformel: zwei Zählweisen und das Ergebnis von Zeile 33

**Frage:** Sie zählen die Tippfehler zweimal, einmal direkt in Z. 10-16 und einmal in der Funktion `tippfehler_zaehlen`. Warum? Liefern beide dasselbe? Was gibt Zeile 33 aus, ist das ein sinnvolles Fehlermaß, und warum haben Sie hier `try/except` statt einer `if`-Abfrage genommen, wenn Sie in Zeile 13 die Länge doch auch so prüfen? Was passiert in Zeile 13, wenn man die beiden Teile der `or`-Bedingung vertauscht?

**Bezug:** b06 Z. 10-16, 21-30, 33

**Eine volle Antwort enthält:**
- Z. 33 gibt 3 aus, nicht 1: Das fehlende "s" verschiebt alle folgenden Zeichen, und das fehlende Ende zählt als Fehler (IndexError). `tippfehler_zaehlen("Zisch", "Zischxx")` liefert 0, die Funktion zählt überzählige Zeichen nicht mit, die Inline-Variante schon. Die beiden Varianten sind also nicht gleichwertig, und eine davon gehört gestrichen.
- Er begründet, dass das positionsweise Zählen eine bewusste Vereinfachung ist, und nennt die Alternative (Abstand zwischen Texten, z. B. Levenshtein, liegt außerhalb des Stoffs).
- `try/except` ist hier nicht nötig, weil sich der Fehlerfall mit `if i >= len(ist)` vorab prüfen lässt. Ausnahmen sind sinnvoll, wo man den Fehler nicht vorab prüfen kann (`int()`, Datei). Ehrlichkeit: Hier dient es auch dem Pflichtelement.
- Kurzschlussauswertung: Bei `or` wird der rechte Teil nur ausgewertet, wenn der linke False ist. Vertauscht gäbe es einen IndexError bei zu kurzer Eingabe.

---

## F13 [G][P] Treibsand-Raster: 2D-Liste und der Aliasing-Fehler

**Frage:** Erklären Sie Zeile 6 und 8. Warum schreiben Sie nicht einfach `[["o"] * 5] * 5`? Was wäre dann nach `raster[0][0] = "~"` in `raster[3][0]`? Und ist die Schreibweise in Zeile 6 Stoff der Vorlesung?

**Bezug:** b07 Z. 6-8, 11-18, 39

**Eine volle Antwort enthält:**
- Zugriff `raster[reihe][spalte]`, Zeile 8 setzt in jeder Reihe an einer zufälligen Spalte genau ein Treibsandfeld (`randint(0, 4)`, beide Grenzen inklusive).
- Bei `[["o"] * 5] * 5` zeigen alle fünf Zeilen auf dieselbe innere Liste. Eine Änderung in `raster[0][0]` erscheint dann auch in `raster[3][0]` (Aliasing). Die verschachtelte Schreibweise erzeugt je Zeile eine neue Liste.
- Die Schleifenschreibweise in einer Zeile (List Comprehension) ist nicht im Stoff. Er sagt, dass es die Kurzform von zwei verschachtelten `for`-Schleifen mit `append` ist und kann sie so aufschreiben.
- Die Variablen `reihe`/`spalte` in Z. 6 werden nie benutzt. `reihe` kommt in Z. 7 und Z. 39 noch einmal vor, in Z. 39 wird sie überschrieben, was hier unschädlich ist.

---

## F14 [?][W] `zahl_einlesen`: Welche Eingaben passieren was?

**Frage:** Was passiert bei den Eingaben `abc`, `0`, `6`, `3.5`, ` 4 ` (mit Leerzeichen), einer leeren Eingabe und bei Strg+D? Wo wird welcher Fehler abgefangen, und warum prüfen Sie den Bereich noch einmal mit `if`, obwohl Sie schon `try/except` haben?

**Bezug:** b07 Z. 21-33, 39-41

**Eine volle Antwort enthält:**
- `abc`, `3.5` und leere Eingabe: `int()` löst einen ValueError aus, es kommt die Meldung, und die Schleife fragt neu. ` 4 ` wird akzeptiert, denn `int()` ignoriert umgebende Leerzeichen. `6` und `0` laufen in den `if`-Zweig mit der Meldung "Nur 1 bis 5!".
- Ohne Bereichsprüfung wäre `6` ein IndexError, und `0` würde als Index `-1` ohne Fehler die letzte Reihe oder Spalte treffen. Ein `try/except` fängt das nicht ab. Der Student erklärt diesen Unterschied zwischen Fehler und falschem Ergebnis.
- Strg+D (EOFError) und Strg+C (KeyboardInterrupt) werden nicht abgefangen, das Programm bricht ab. Er weiß, dass `except ValueError` nur diesen einen Fehlertyp abfängt und was ein allgemeines `except` ändern würde.
- Er erklärt die Flag-Schleife (`eingabe_ok`), warum `zahl` am Ende sicher gesetzt ist, und kennt den Index-Unterschied (Spieler zählt ab 1, Python ab 0, Z. 41).

---

## F15 [U][Ä] Treibsand: Wie schwer ist die Station wirklich?

**Frage:** Ihr Konzept sagt: Der Spieler gibt "den sicheren Weg" ein. Im Code fragen Sie ein einziges Feld ab. Wie hoch ist die Chance, dass jemand ohne hinzusehen durchkommt? Was bleibt von "Merken" übrig? Wie würden Sie die Station anpassen? Und ändern Sie bitte das Raster auf 4×4: An welchen Stellen müssen Sie etwas anfassen?

**Bezug:** b07 Z. 6-8, 13, 36-44, 39-40

**Eine volle Antwort enthält:**
- In jeder Reihe ist genau ein Feld Treibsand, also 4 von 5 Feldern sicher: Die Chance beim Raten liegt bei 80 %. Das Merken ist praktisch bedeutungslos, und es gibt weder Konsequenz noch Leben-Abzug.
- Verbesserung: je Reihe eine Koordinate abfragen (Schleife über die 5 Reihen, Chance beim Raten etwa 0.8^5, rund 33 %), bei Treibsand `leben_abziehen`, Rückgabe an das Level.
- Live-Änderung 4×4: Z. 6 (zweimal `range(5)`), Z. 8 (`randint(0, 3)`), Z. 13 (Kopfzeile mit festen Zahlen), Z. 39-40 (Bereich 1 bis 4). Mehrere Stellen, weil die Größe fest einprogrammiert ist. Besser eine Variable `groesse` und `len(raster)`.
- Nebenbei: `print("\n" * 40)` verdeckt das Raster nur unvollständig (siehe F11).

---

## F16 [E][?][U] Bestenliste: Speichern, Laden, Randfälle

**Frage:** Erklären Sie `bestenliste_laden` Zeile für Zeile. Warum `"a"` beim Speichern und `"r"` beim Laden? Was liefern `zeile.find(";")` und `zeile[trenner + 1:]`? Was passiert bei einer Zeile ohne Semikolon, etwa `5`, oder bei einem Namen, der ein Semikolon enthält? Und wo liegt die Datei eigentlich?

**Bezug:** b08 Z. 1, 5-9, 12-27, 53-60

**Eine volle Antwort enthält:**
- `"a"` hängt an und legt die Datei an, falls sie fehlt (`"w"` würde alles überschreiben). `"r"` löst einen FileNotFoundError aus, wenn die Datei fehlt, und das fängt der Code ab, indem er beim ersten Start eine leere Liste zurückgibt. `close()` nicht vergessen; die Zeilen werden mit `for` durchlaufen.
- `find` liefert den Index des ersten Semikolons oder `-1`. Slicing trennt Name (`[0:trenner]`) und Zeit (`[trenner + 1:]`, inklusive `\n`, das `float` ignoriert). Eine kaputte Zeit löst einen ValueError aus, die Zeile wird übersprungen, und es gibt eine Meldung.
- Randfälle: Eine Zeile ohne `;` gibt `trenner = -1`. Aus `5` wird dann Name "5" und Zeit 5.0, ein stilles Falschergebnis. Bei einem Namen mit `;` ("A;B") wird die Zeile als kaputt verworfen, geprüft wird das beim Speichern nicht.
- Der relative Dateiname verweist auf das Arbeitsverzeichnis und nicht auf den Ordner des Skripts. `bestenliste_speichern` hat kein `try/except` (PermissionError). Der Testcode hängt bei jedem Start sechs Einträge erneut an und erzeugt Duplikate.

---

## F17 [E][Ä] Bubble Sort vorführen

**Frage:** Führen Sie Ihren Sortieralgorithmus bitte an den Zeiten [0.412, 0.298, 0.655, 0.301, 0.5, 0.7] vor: Wie sieht die Liste nach jedem Durchlauf aus, wie viele Durchläufe gibt es, wozu dienen `getauscht` und `durchlauf`? Was passiert bei einer leeren Liste? Und ändern Sie die Funktion so, dass nach Namen sortiert wird.

**Bezug:** b08 Z. 30-43, 53-60

**Eine volle Antwort enthält:**
- Durchlauf 1: [0.298, 0.412, 0.301, 0.5, 0.655, 0.7] (3 Vertauschungen). Durchlauf 2: [0.298, 0.301, 0.412, 0.5, 0.655, 0.7] (1 Vertauschung). Durchlauf 3: keine Vertauschung, daher Abbruch. Es sind also 3 Durchläufe.
- `getauscht` bricht ab, sobald nichts mehr getauscht wird (bei sortierter Liste nur ein Durchlauf). `durchlauf` verkürzt die innere Schleife, weil nach jedem Durchlauf das größte Element hinten richtig liegt. Bei `n = 0` ist `range(-1)` leer und nichts passiert. Gleiche Zeiten werden nicht getauscht (`>`).
- Die Funktion sortiert die übergebene Liste an Ort und Stelle und gibt `None` zurück. `liste = bestenliste_sortieren(liste)` wäre ein Fehler. Aufwand wächst etwa quadratisch mit der Anzahl.
- Nach Namen: In Z. 38 `["zeit"]` durch `["name"]` ersetzen. Strings werden nach Zeichencode verglichen: "Zoe" kommt vor "adam" (Großbuchstaben zuerst).

---

## F18 [E][Ä][P] Rekursion: `countdown`

**Frage:** Spielen Sie `countdown(3)` durch: Wie viele Aufrufe gibt es, was steht wann auf dem Bildschirm? Was passiert bei `countdown(-1)` oder `countdown(2.5)`? Ändern Sie die Funktion so, dass sie dann sicher endet. Wie sähe das Gleiche mit einer Schleife aus, und warum haben Sie hier Rekursion gewählt?

**Bezug:** b09 Z. 15-22, 43

**Eine volle Antwort enthält:**
- Abbruchbedingung `n == 0`, Rekursionsschritt `n - 1`. Es gibt vier Aufrufe (3, 2, 1, 0), ausgegeben werden "3 ...", "2 ...", "1 ...", dann "LOS!". Die Aufrufe liegen verschachtelt auf dem Stapel und kehren danach der Reihe nach zurück.
- Bei `-1` oder `2.5` wird 0 nie erreicht, es gibt eine unendliche Rekursion mit RecursionError (Standardgrenze etwa 1000 Aufrufe).
- Änderung: `if n <= 0:`. Schleifenversion: `while n > 0:` mit Ausgabe, `sleep`, `n -= 1`. Ehrliche Begründung: Die Schleife wäre einfacher, die Rekursion ist hier ein bewusstes Beispiel für die Wahlaufgabe.
- `end="\r"` setzt den Cursor an den Zeilenanfang, so überschreibt die nächste Ausgabe die Zahl. Die Leerzeichen hinter "LOS!" überdecken den Rest des Vorgängertexts ("1 ..." ist länger als "LOS!").

---

## F19 [P][E] Ergänzungen außerhalb des Stoffs: ANSI-Farbe, `\r`, `flush`, ASCII-Bild

**Frage:** Erklären Sie `"\033[32m"`, `end="\r"` und `flush=True`. Warum steht `flush=True` in `langsam_schreiben`, aber nicht im Countdown? Warum hat das ASCII-Bild doppelte Backslashes? Und was sehen Sie, wenn das Programm in einer Umgebung läuft, die ANSI-Codes nicht versteht, etwa in IDLE?

**Bezug:** b09 Z. 4-9, 11-12, 20, 28, 45

**Eine volle Antwort enthält:**
- `\033` ist die Oktal-Schreibweise des Escape-Zeichens (ASCII 27), `[32m` schaltet auf grüne Schrift, `[0m` setzt zurück. Das ist eine Escape-Sequenz wie `\n`, aber nicht im Stoff. In Umgebungen ohne ANSI-Unterstützung erscheinen stattdessen Steuerzeichen als Text, und es gibt keine Rückfalllösung.
- Die Ausgabe ist gepuffert. Ohne `flush=True` erscheinen Zeichen ohne Zeilenende womöglich erst gesammelt, und der Schreibmaschineneffekt ginge verloren. Beim Countdown ist `\r` ohne `flush` inkonsequent: In einer IDE-Konsole ist das Verhalten nicht garantiert.
- `\\` ergibt einen einzelnen Backslash. Ein einzelner `\` vor `_` oder `|` wäre eine ungültige Escape-Sequenz (Warnung, in neueren Python-Versionen SyntaxWarning).
- Er kennzeichnet jede Ergänzung im Code und kann sie ohne Vorlage erklären. Der Dozent erlaubt solche Ergänzungen nur, wenn man sie erklären kann.

---

## F20 [U][P] Sound: `winsound`, `try/except` und die Extrapunkte

**Frage:** Erklären Sie `ton_abspielen`. Warum steht der Import in der Funktion und nicht oben in der Datei? Welche Ausnahme fangen Sie ab, und welche könnten trotzdem auftreten? Für Sound gibt es Extrapunkte: Glauben Sie, dass ein 200-Millisekunden-Piepton und ein ASCII-Affe das verdienen?

**Bezug:** b09 Z. 33-39, 4-9, 46

**Eine volle Antwort enthält:**
- `winsound` gibt es nur unter Windows. Ein Import ganz oben würde auf anderen Systemen sofort mit ImportError abbrechen. Im `try`-Block erkennt der Code das Fehlen und fällt auf `print("\a")` zurück. `Beep(880, 200)` bedeutet 880 Hz für 200 ms und blockiert währenddessen.
- Es wird nur ImportError (ModuleNotFoundError) gefangen. `Beep` kann auf Windows ohne Tonausgabe einen RuntimeError auslösen, der abstürzt. Ein allgemeineres `except` oder ein zweiter `except`-Zweig wäre nötig. `"\a"` piept nur, wenn die Konsole es zulässt.
- Ehrliche Einschätzung: Ein Piepton und ASCII-Art sind die Mindestlösung. Echte Sounddateien (z. B. mit pygame und `requirements.txt`) und echte Bilder (matplotlib) wären mehr, aber plattformabhängig. Er weiß, dass der Dozent "Sound und Bilder" als Extrapunkte nennt, und dass der genaue Umfang der Punkte vom Dozenten abhängt.
- Er räumt ein, dass das Spiel ohne Ton funktionieren muss und das `try/except` genau dafür da ist.
