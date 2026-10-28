# Konzeptanalyse Ingenieurinformatik I (Python) – Grundlage der Karteikarten

Stand: 28.10.2026. Grundlage: alle Aufgaben, Lösungen und Daten aus `Informatik-1---Aufgaben-und-Beispiele-main` (Kapitel 01–06, 41 Lösungs-Notebooks und die zugehörigen Aufgaben) und das Skript `Info1_Skript_WS26.pdf` (212 Seiten; „F.“ = Seite im PDF, die aufgedruckte Foliennummer weicht ab).

## Vorgehen und Gewichtung

1. Jedes Lösungs-Notebook wurde gelesen; ein Skript zählte zusätzlich, in wie vielen Lösungen eine Syntaxform vorkommt (z. B. f-Strings in 21, `input()` in 18, `for` in 11, `def` in 6, `groupby` in 1 Lösung). Die Zählung wurde von Hand bereinigt (z. B. `%` in Zeitformaten ist kein Modulo).
2. Gewicht **3**: in vielen Aufgaben nötig (≥ 8 Lösungen) oder Grundlage fast jeder Aufgabe (Ein-/Ausgabe, Typumwandlung, Verzweigungen, Schleifen, Funktionen). Gewicht **2**: in 3–7 Lösungen oder eigener Skriptabschnitt. Gewicht **1**: in 1–2 Lösungen oder nur im Skript.
3. Umfang folgt dem Gewicht: Gewicht 3 → 3–7 Karten (Ø 4,7), Gewicht 2 → 2–5 Karten (Ø 3,3), Gewicht 1 → 2–4 Karten (Ø 2,2). Jedes Konzept hat mindestens zwei Karten **unterschiedlichen Typs**.

## Kartentypen und Umfang – Begründung

Nach dem Minimum-Information-Prinzip (Wozniak, *20 rules of formulating knowledge*) fragt jede Karte genau eine Sache ab, Code bleibt bei höchstens 8 Zeilen, und Aufzählungen werden vermieden. Weil aktives Abrufen besser behalten wird als Wiederlesen (Testing-Effekt, Roediger & Karpicke 2006), dominieren Karten, auf denen man selbst etwas erzeugt: Ausgaben vorhersagen trainiert das Code-Lesen Zeile für Zeile, das in Studien das Programmieren von Anfängern verbessert (Xie, Nelson & Ko 2018); Lückentexte (Cloze) und „Schreib Code, der …“ trainieren exakte Syntax wie bei Code auf Papier; „Finde den Fehler“ übt das Lesen echter englischer Fehlermeldungen. Der Umfang (434 Karten) ergibt sich aus 142 Konzepten × 2–7 Karten; bei 20–25 neuen Karten am Tag ist der Satz in drei Wochen eingeführt und bis zur Klausur mehrfach wiederholt.

| Typ | Was trainiert er? |
|---|---|
| Was gibt der Code aus? | Code Zeile für Zeile verfolgen (Schreibtischtest), Fallen erkennen |
| Lückentext im Code | exakte Syntax eines Elements (Operator, Methode, Parameter) |
| Finde den Fehler | Fehlermeldung (englisch, letzte Zeile wie im Terminal) deuten und korrigieren |
| Schreib Code, der … | kleine Aufgabe frei lösen (wie in Labor und Klausur) |
| Begriff ↔ Erklärung | Fachbegriffe und Regeln aus dem Skript |
| Was ist der Unterschied …? | ähnliche Dinge auseinanderhalten (`/` vs. `//`, `pop` vs. `remove`) |

## Prüfregeln der Karten

- Jeder Python-Block wird mit `werkzeuge/karten.py code` unter Python 3.9 (wie in deiner `.venv`) **und** 3.13 ausgeführt; Ausgabe bzw. letzte Zeile der Fehlermeldung muss dem Text-Block der Karte entsprechen.
- Fehlermeldungen, deren Wortlaut zwischen den Versionen abweicht (SyntaxError, „Did you mean …“), nennen nur die Fehlerart und werden auf diese Art geprüft.
- Code mit Eingaben wird mit festgelegten Eingaben getestet, Datei-Karten mit den auf der Karte gezeigten Dateien.

## Nicht aufgenommen

- `lambda`, `map()`, `filter()`: kommen weder in den Aufgaben noch im Skript vor (nur `lambda` in der Schlüsselwort-Tabelle F. 62). Das Funktions-als-Argument-Prinzip deckt `sort(key=…)` ab (F. 147).
- Reine Rechnerarchitektur-Theorie (EVA, Von-Neumann, CPU, Bits/Bytes, Analog/Digital, Bereiche der Informatik): für das Lösen der Programmieraufgaben nicht nötig; Zahlensysteme sind wegen Aufg. 5.4 enthalten.
- Echte Arrays mit dem Modul `array` (F. 157, „nice to know“), seaborn (F. 211), `open(…, "r+")` (F. 195, nur ein Beispiel ohne Aufgabe; in der Abdeckungsmatrix von Kapitel 11 als ausgelassen vermerkt).

## Auffälligkeiten im Skript (auf den Karten berücksichtigt)

- F. 104: `4 / 2` „erhält den Wert 2“ – Python liefert `2.0`. „% (oder MOD)“: MOD gibt es in Python nicht. `//` „schneidet ab“ – bei negativen Zahlen wird abgerundet.
- F. 105/106: `=`, `<>`, `!`, `&&`, `||` sind Schreibweisen anderer Sprachen, in Python 3 ungültig.
- F. 119: In Python haben alle Vergleichsoperatoren denselben Rang (die Tabelle stuft `<`, `>` … über `==`, `!=`).
- F. 97: `1 / 3 * 3` ergibt in Python genau `1.0`; Rundungsfehler zeigen z. B. `0.1 + 0.2` oder `85.0 - 72.4`.
- F. 164: Kommentar „(Hier die erste)“ über `d[:,2]` – gemeint ist die dritte Spalte.
- F. 182: Zuweisungen in einer **Schleife** wirken sehr wohl außerhalb; nur Funktionen haben einen eigenen Gültigkeitsbereich.
- F. 195: Kommentar „Überschreiben des bisherigen Inhalts“ bei `"r+"` – r+ überschreibt nur ab Dateianfang so viele Zeichen, wie geschrieben werden.
- F. 208: `savefig` speichert nicht „im Speicherort des Programmskripts“, sondern im aktuellen Arbeitsordner (in Jupyter meist der Ordner des Notebooks). Gleiches gilt für relative Pfade bei `open()`.
- Aufg. 5.6 sagt, eine Funktion erhalte „eine Kopie des Wertes“. Genauer: Der Parameter ist eine eigene lokale Variable, eine Neuzuweisung wirkt nicht nach außen – eine Liste, die in der Funktion mit `append` verändert wird, ist aber auch außen verändert (Karte als Ergänzung).
- Aufgaben 3.7/3.8: Die Lösungsdateien sind gegenüber den Dateinamen vertauscht betitelt; die Karten nutzen die Dateinummer.

## Externe Prüfung

Vier unabhängige Prüfdurchgänge (ohne Kenntnis der Entstehung): (A) mechanisch – alle Code-Karten unter Python 3.9 und 3.13 mit zwei Hash-Seeds ausgeführt, Abdeckung nachgezählt, CSV-Format und alle Code-Bilder geprüft; (B–D) fachlich und didaktisch je ein Kapitelblock. Alle Befunde der Schwere „hoch“ und „mittel“ sind korrigiert (u. a. 1:1 übernommene Aufgabenbeispiele durch neue Szenarien ersetzt, Dubletten umgebaut, zusammengesetzte Karten geteilt, Ergänzungen gekennzeichnet); danach liefen alle Tests erneut fehlerfrei.

## Konzepte nach Kapitel

### Kapitel 1: Ein- und Ausgabe, Strings ausgeben, Kommentare (`kap01_ein-ausgabe.csv`)

| Konzept / Syntax | Gewicht | Skript | Aufgaben | Karten |
|---|---:|---|---|---:|
| print() mit mehreren Argumenten (Leerzeichen dazwischen), Leerzeile mit print() | 3 | F. 48 | 1.1, 2.3 | 6 |
| print(..., end="") unterdrückt den Zeilenumbruch | 2 | F. 52 | 1.3, 4.3 | 3 |
| Escape-Sequenz \n (Zeilenumbruch) | 2 | F. 52–53 | 1.3, 1.4 | 3 |
| Escape-Sequenz \t (Tabulator) | 2 | F. 53 | 1.3, 1.4 | 4 |
| Steuerzeichen \r (Wagenrücklauf) und \b (Backspace) | 1 | F. 53 | 1.3 | 3 |
| Anführungszeichen und Backslash im String: \", \', \\ | 1 | F. 69 | – | 2 |
| input() liefert immer einen String; Prompt ohne Zeilenumbruch | 3 | F. 49, 52 | 1.1, 1.2, 3.5 | 5 |
| String-Verkettung mit + (nur str + str, Leerzeichen selbst setzen) | 3 | F. 135 | 1.1, 1.2 | 5 |
| String-Wiederholung mit * ("#" * 5) | 1 | – | 1.3 | 2 |
| f-Strings: Variablen und Ausdrücke in {} | 3 | F. 116, 178 | 2.6–2.9, 3.2–3.8, 5.1–6.3 | 6 |
| Formatangabe {wert:.2f} (Nachkommastellen, rundet) | 2 | – | 3.11, 5.3 | 4 |
| Kommentare: # einzeilig, """ mehrzeilig, auskommentieren | 2 | F. 59–60 | 2.1 | 3 |

Typische Fehlerquellen:

- `input()` liefert immer `str` – `"230" + "120"` ergibt `230120`, `"40" * 2` ergibt `4040`.
- `+` mit Zahl und String → `TypeError: can only concatenate str (not "int") to str`.
- Bei `+` fehlen Leerzeichen; bei Kommas in print() kommt ein ungewolltes Leerzeichen dazu (z. B. nach `\n`).
- f vor dem String vergessen → `{temperatur}` erscheint wörtlich.
- `/t` statt `\t`, `C:\temp` enthält unbemerkt `\t`.

### Kapitel 2: Variablen und Datentypen (`kap02_variablen-datentypen.csv`)

| Konzept / Syntax | Gewicht | Skript | Aufgaben | Karten |
|---|---:|---|---|---:|
| Variable, Zuweisung mit =, Initialisierung, Reihenfolge der Zuweisungen | 3 | F. 49, 70–71 | 2.3 | 5 |
| Regeln für Bezeichner, Groß-/Kleinschreibung, reservierte Schlüsselwörter | 2 | F. 58, 62 | 2.3 | 3 |
| Standarddatentypen int, float, str, bool | 3 | F. 64–68 | 2.3 | 5 |
| type() gibt den Datentyp aus (<class 'int'> …) | 2 | F. 66 | 2.2–2.4 | 4 |
| Datentyp ändert sich mit dem zugewiesenen Wert (keine Deklaration wie in C++) | 1 | F. 70–71 | – | 2 |
| / liefert immer float (auch 1500 / 2) | 3 | F. 104 | 2.2 | 3 |
| Implizite Typumwandlung: int mit float → float, int * int bleibt int | 2 | F. 74 | 2.2 | 3 |
| int(): String → Ganzzahl, float → Ganzzahl (schneidet ab, rundet nicht) | 3 | F. 75 | 1.2, 2.4 | 5 |
| float(): String → Kommazahl, Punkt statt Komma | 3 | F. 67, 75 | 2.4, 3.5 | 4 |
| str(): Zahl → Text (z. B. für Verkettung) | 2 | F. 75, 135 | 1.3 | 3 |
| ValueError bei ungültiger Umwandlung (int("72.4"), float("72,4")) | 2 | F. 75 | 2.4 | 3 |
| Rundungsfehler bei Gleitkommazahlen (0.1 + 0.2, 85.0 - 72.4) | 2 | F. 67, 97 | 2.4 | 3 |
| bool: True/False, Vergleiche liefern bool | 2 | F. 66, 112 | 3.1 | 4 |
| Syntax und Semantik | 1 | F. 57 | – | 2 |

Typische Fehlerquellen:

- `/` liefert immer float (`1500 / 2` → `750.0`), danach scheitert z. B. `"#" * 7.0`.
- `int()` schneidet ab statt zu runden (`int(72.9)` → 72, `int(-3.7)` → -3).
- `int("72.4")` und `float("72,4")` → ValueError (Dezimalpunkt!).
- Rundungsfehler: `85.0 - 72.4` → `12.599999999999994`.
- Variable vor der Zuweisung benutzt → NameError; `true` statt `True`.

### Kapitel 3: Operatoren und Zahlensysteme (`kap03_operatoren.csv`)

| Konzept / Syntax | Gewicht | Skript | Aufgaben | Karten |
|---|---:|---|---|---:|
| Arithmetische Operatoren + - * / // % ** | 3 | F. 103–104 | 3.1, 3.2 | 3 |
| Ganzzahldivision // (abrunden), Ergebnis-Typ | 3 | F. 104 | 3.1, 3.9, 3.10, 5.4 | 6 |
| Modulo %: Rest, Teilbarkeit (x % n == 0), gerade/ungerade | 3 | F. 104 | 3.1, 3.9, 3.10, 5.4 | 6 |
| Ziffern einer Zahl mit // und % zerlegen (Quersumme) | 2 | – | 3.1, 5.4 | 3 |
| Potenz ** | 1 | F. 104 | 3.2 | 2 |
| Vergleichsoperatoren == != < > <= >= liefern bool; int und float vergleichbar, str und int nicht | 3 | F. 105 | 3.1–3.10 | 4 |
| = (Zuweisung) vs. == (Vergleich) | 3 | F. 113 | 3.1 | 3 |
| Logische Operatoren and, or, not | 3 | F. 106 | 3.1, 3.7, 3.11 | 5 |
| Rangfolge: ** vor * / // % vor + -, Klammern | 2 | F. 119 | 3.2 | 5 |
| Rangfolge: Arithmetik vor Vergleich vor not vor and vor or | 2 | F. 119 | 3.2 | 3 |
| Kurzschlussauswertung (Short-Circuit) bei or/and | 1 | – | 3.2 | 2 |
| Erweiterte Zuweisung += -= *= //= | 2 | F. 117, 119 | 3.8, 3.10, 6.1 | 3 |
| Binärsystem: Dezimal ↔ Binär (fortgesetzte Division durch 2) | 1 | F. 85–90 | 5.4 | 3 |
| Hexadezimalsystem (Nibble, 0–9/A–F, 0x-Schreibweise) | 1 | F. 91–95 | – | 3 |

Typische Fehlerquellen:

- Rangfolge: `**` vor `*` vor `+`; `%` vor `+`; `and` vor `or` – fehlende Klammern.
- `=` statt `==` in Bedingungen; `&&`/`||`/`<>` gibt es in Python nicht (SyntaxError).
- `//` rundet bei negativen Zahlen ab (`-7 // 2` → -4) und liefert bei float-Operanden float.
- Vergleich von String und Zahl (`"85" > 80`) → TypeError.
- `+=` ohne Startwert → NameError.

### Kapitel 4: Verzweigungen (if, elif, else) und Einrückung (`kap04_verzweigungen.csv`)

| Konzept / Syntax | Gewicht | Skript | Aufgaben | Karten |
|---|---:|---|---|---:|
| if/else: Bedingung, Doppelpunkt, eingerückter Block, else optional | 3 | F. 112–116 | 3.1, 3.5 | 5 |
| if/elif/else-Kette: nur der erste wahre Zweig läuft, Reihenfolge der Bedingungen | 3 | F. 115 | 3.3, 3.4, 3.5 | 4 |
| Einrückung bestimmt die Blockzugehörigkeit, IndentationError | 3 | F. 117 | 3.3 | 5 |
| Verschachtelte Verzweigungen | 2 | F. 118 | 3.6 | 3 |
| Strings vergleichen (Groß-/Kleinschreibung, "3" ≠ 3) | 2 | – | 3.5, 3.7 | 3 |
| Grundstrukturen: sequentiell, auswählend, iterativ, springend; Anweisung, Folge, Bedingung | 1 | F. 109–111 | – | 2 |

Typische Fehlerquellen:

- Doppelpunkt nach `if …`/`else` vergessen (SyntaxError).
- Reihenfolge der elif-Bedingungen: die weitere Bedingung zuerst „frisst“ die engere.
- Zwei getrennte `if` statt `if/elif` → mehrere Zweige laufen.
- Falsch eingerückte Zeile gehört ungewollt zum Block (oder fehlt darin); `IndentationError: unexpected indent`.
- Eingabe `"3"` mit Zahl `3` verglichen; Groß-/Kleinschreibung bei Strings.

### Kapitel 5: Schleifen (while, for, range, break, continue) (`kap05_schleifen.csv`)

| Konzept / Syntax | Gewicht | Skript | Aufgaben | Karten |
|---|---:|---|---|---:|
| while-Schleife: läuft, solange die Bedingung wahr ist; Zähler | 3 | F. 123, 125 | 2.9, 3.7, 3.10 | 5 |
| Endlosschleife (Bedingung bleibt wahr, Zähler vergessen) | 2 | F. 126 | – | 3 |
| while mit zwei Bedingungen (and) und Auswertung nach der Schleife | 2 | – | 3.7 | 3 |
| Eingabe wiederholen, bis sie passt (Startwert vor der Schleife) | 2 | F. 125 | 3.7 | 3 |
| for-Schleife über Liste/String; Schleifensteuerung und -rumpf | 3 | F. 123, 143 | 3.8, 4.2, 6.1 | 5 |
| range(stop), range(start, stop, schritt): Endwert ausgeschlossen | 3 | F. 128 | 3.9, 3.11, 4.3 | 7 |
| range mit negativer Schrittweite (rückwärts zählen) | 1 | F. 129 | – | 2 |
| Summe/Zähler/Zinseszins in der Schleife (Startwert vor der Schleife) | 3 | – | 3.11, 6.1 | 5 |
| break beendet die Schleife sofort | 2 | – | 3.8 | 4 |
| continue überspringt den Rest des Durchlaufs | 2 | – | 3.8 | 3 |
| Merker-Variable (gefunden = False) über die Schleife hinweg | 2 | – | 4.4, 4.5 | 3 |
| Ablauf verfolgen: Durchläufe zählen, Werte nach der Schleife | 2 | – | 3.8, 3.10, 5.2 | 4 |

Typische Fehlerquellen:

- `range(1, 7)` endet bei 6 (Endwert ausgeschlossen); `range(anzahl / 2)` → TypeError (float).
- Zähler im while-Rumpf nicht verändert → Endlosschleife.
- Startwert der Summe/des Zählers in der Schleife statt davor.
- Merker-Variable im else-Zweig wieder zurückgesetzt.
- Nach einer while-Schleife mit zwei Bedingungen nicht geprüft, warum sie endete; `break` vs. `continue` verwechselt.

### Kapitel 6: Zeichenketten – Index, Slicing, find, replace, count (`kap06_strings.csv`)

| Konzept / Syntax | Gewicht | Skript | Aufgaben | Karten |
|---|---:|---|---|---:|
| len() – Anzahl der Zeichen (Leerzeichen zählen mit) | 3 | F. 136 | 4.1, 4.4 | 4 |
| Zugriff s[i]: Index ab 0, s[-1] letztes Zeichen | 3 | F. 136 | 4.1 | 4 |
| IndexError: string index out of range | 1 | F. 136 | – | 2 |
| Slicing s[von:bis] (bis ausgeschlossen, Grenzen weglassbar) | 2 | F. 137 | 4.1 | 5 |
| Slicing mit Schrittweite s[von:bis:schritt] | 1 | F. 137 | – | 2 |
| find(): Startposition, -1 wenn nicht gefunden, Suche ab Position | 2 | F. 138 | 4.1 | 4 |
| replace(): ersetzt alle Vorkommen, liefert neuen String, verkettbar | 2 | F. 138 | 4.1, 6.2 | 4 |
| count(): Vorkommen zählen (Groß-/Kleinschreibung beachten) | 2 | F. 146 | 6.1 | 3 |
| Strings sind unveränderlich (Ergebnis neu zuweisen) | 1 | F. 138 | 4.1 | 3 |
| Strings mit find() und Slicing zerlegen und neu zusammensetzen | 2 | F. 137–138 | 4.1 | 3 |

Typische Fehlerquellen:

- Index ab 0, letzter Index `len(s) - 1` → `IndexError: string index out of range`.
- Slicing: End-Index ausgeschlossen; `komma + 2` wegen Leerzeichen.
- `find()` liefert -1 statt eines Fehlers.
- `replace()` ändert den String nicht – Ergebnis zuweisen (Strings sind unveränderlich).
- `count()` unterscheidet Groß- und Kleinschreibung.

### Kapitel 7: Listen, 2D-Listen und Tupel (`kap07_listen.csv`)

| Konzept / Syntax | Gewicht | Skript | Aufgaben | Karten |
|---|---:|---|---|---:|
| Liste anlegen (eckige Klammern, gemischte Typen, leere Liste) | 3 | F. 141–142 | 4.2 | 4 |
| Element lesen/ändern über den Index, IndexError | 3 | F. 142–143 | 4.2 | 4 |
| append(): Element am Ende anfügen (liefert None) | 2 | F. 144 | 4.2, 6.2 | 4 |
| insert(pos, wert): an Position einfügen | 2 | F. 144 | 4.2, 5.4 | 3 |
| pop(index): Element an Position entfernen und zurückgeben | 2 | F. 145 | 4.2 | 4 |
| remove(wert): erstes passendes Element löschen | 2 | F. 145 | 4.2 | 3 |
| index(wert): Position eines Werts | 1 | F. 146 | 4.2 | 2 |
| count(), sort(), reverse(), clear() | 1 | F. 145–146 | – | 2 |
| sort(key=funktion, reverse=…): nach eigenem Kriterium sortieren | 1 | F. 147 | – | 2 |
| Liste durchlaufen: for x in liste / for i in range(len(liste)) | 3 | F. 143, 148, 152 | 3.8, 4.4 | 4 |
| in: prüfen, ob ein Wert in der Liste ist | 1 | – | 3.8 | 2 |
| enumerate(): Index und Element zugleich | 1 | – | 4.4 | 2 |
| 2D-Liste: matrix[zeile][spalte] | 2 | F. 150–151 | 4.3–4.5 | 4 |
| Verschachtelte Schleifen über eine 2D-Liste | 2 | F. 151–152 | 4.3–4.5 | 3 |
| List-Comprehension zum Anlegen von Listen/Rastern | 1 | – | 4.3 | 2 |
| Benutzereingabe ab 1 → Index ab 0 (reihe - 1) | 2 | – | 4.3, 4.5 | 3 |
| Tupel: unveränderlich, runde Klammern, Entpacken | 1 | F. 155 | 5.2, 5.6 | 3 |
| Zuweisung kopiert keine Liste/kein Array (Referenz) – .copy() | 1 | – | 4.6 | 2 |

Typische Fehlerquellen:

- `liste = liste.append(x)` → `None`.
- `pop(i)` (Position) und `remove(x)` (Wert) verwechselt; remove löscht nur das erste Vorkommen.
- Benutzereingabe ab 1 nicht in Index ab 0 umgerechnet → IndexError.
- Laufvariable `w = w * 10` ändert die Liste nicht.
- `backup = liste` ist keine Kopie; Tupel lassen sich nicht ändern.

### Kapitel 8: NumPy-Arrays (`kap08_numpy.csv`)

| Konzept / Syntax | Gewicht | Skript | Aufgaben | Karten |
|---|---:|---|---|---:|
| import numpy as np, np.array() aus Liste (1D/2D), Ausgabeformat | 2 | F. 158, 162 | 4.6 | 4 |
| np.zeros(), np.ones(), np.full() mit Form (zeilen, spalten) | 1 | F. 163 | 4.6 | 2 |
| Zugriff a[i, j], ganze Zeile a[i, :], ganze Spalte a[:, j] | 2 | F. 164 | 4.6 | 3 |
| Ganze Zeile/Spalte auf einen Wert setzen | 1 | F. 165 | 4.6 | 2 |
| Elementweise Rechnung (Broadcasting), Arrays gleicher Form verrechnen | 2 | F. 166 | 4.6 | 3 |
| NumPy-Array vs. Liste (gleicher Datentyp, Geschwindigkeit, * verhält sich anders) | 1 | F. 159–161 | – | 2 |

Typische Fehlerquellen:

- Import `import numpy as np` vergessen.
- `d[:, 2]` ist die dritte Spalte (Index 2).
- `liste * 2` wiederholt, `array * 2` multipliziert.
- Arrays unterschiedlicher Form verrechnet → ValueError (broadcast).
- Zuweisung statt `.copy()` (Karten dazu in Kapitel 7, gilt für Listen und Arrays).

### Kapitel 9: Funktionen (def, return, Parameter, Gültigkeit) (`kap09_funktionen.csv`)

| Konzept / Syntax | Gewicht | Skript | Aufgaben | Karten |
|---|---:|---|---|---:|
| Funktion definieren: def name(parameter): + eingerückter Rumpf | 3 | F. 171, 180 | 5.1–5.6 | 4 |
| Aufruf und Programmablauf: Definition läuft erst beim Aufruf, Sprung hin und zurück | 3 | F. 177–178 | 5.2 | 4 |
| return gibt einen Wert zurück und beendet die Funktion | 3 | F. 173, 180 | 5.3, 5.5 | 6 |
| print() vs. return; Funktion ohne return liefert None | 3 | F. 172 | 5.3 | 4 |
| Parameter: Anzahl und Reihenfolge beim Aufruf | 2 | F. 176 | 5.1 | 3 |
| TypeError bei fehlenden oder zu vielen Argumenten | 2 | F. 176 | 5.1 | 2 |
| Erst definieren, dann aufrufen (NameError) | 2 | F. 175 | 5.1 | 3 |
| Mehrere Rückgabewerte (return a, b) und Entpacken | 2 | – | 5.2, 5.6 | 3 |
| Lokale Variablen: nur innerhalb der Funktion gültig | 2 | F. 182 | 5.6 | 3 |
| Schlüsselwort global | 1 | F. 183 | 5.6 | 2 |
| Neuzuweisung eines Parameters ändert die Variable des Aufrufers nicht | 2 | F. 182 | 5.6 | 5 |
| Prozedur, Funktion, Methode | 1 | F. 172–174 | – | 2 |
| Wozu Funktionen: Wiederverwendung, Modularisierung (Refactoring) | 1 | F. 170 | 5.3 | 2 |
| Ablauf mit Trace-Ausgaben/Debugger verfolgen | 1 | F. 177–178 | 5.2 | 3 |

Typische Fehlerquellen:

- Funktion vor ihrer Definition aufgerufen → NameError; Doppelpunkt nach `def` vergessen.
- print() statt return → Rückgabewert `None`, danach TypeError beim Rechnen.
- Falsche Anzahl/Reihenfolge der Argumente → TypeError bzw. vertauschte Werte.
- Rückgabewert nicht gespeichert (`verdopple(temp)` ohne `temp = …`).
- Erwartet, dass Neuzuweisung eines Parameters oder eine lokale Variable außen wirkt.

### Kapitel 10: Bibliotheken – import, math, random, time, datetime, qrcode (`kap10_bibliotheken.csv`)

| Konzept / Syntax | Gewicht | Skript | Aufgaben | Karten |
|---|---:|---|---|---:|
| import modul, Aufruf modul.funktion(), fehlender Import → NameError | 3 | F. 77–79 | 2.5–2.9, 3.4, 6.1–6.5 | 4 |
| import … as … (np, pd, plt) und from … import … | 2 | F. 205 | 2.1, 4.3, 4.6, 6.3 | 3 |
| math.sqrt, math.pi, math.ceil (aufrunden) | 2 | – | 2.5, 2.6 | 4 |
| random.randint(a, b) – beide Grenzen eingeschlossen | 2 | – | 2.5, 2.9, 3.4, 3.6 | 4 |
| time.sleep(sekunden) – Programm anhalten | 2 | – | 1.3, 2.7, 2.9 | 2 |
| Zeit formatieren mit strftime: %d %m %Y %H %M %S | 2 | – | 2.5, 2.8, 2.9, 5.5 | 5 |
| datetime.datetime.now() und .strftime() | 2 | F. 194 | 5.5, 6.2 | 3 |
| Bibliotheken installieren (pip install) vs. importieren | 1 | – | 2.5 | 2 |
| qrcode.make(text) und display() im Notebook | 1 | – | 2.6–2.8 | 3 |

Typische Fehlerquellen:

- `import` vergessen → NameError.
- `random.randint(1, 6)` schließt 6 ein, `range(1, 6)` nicht.
- `%y` (zweistellig) statt `%Y` (vierstellig); `%M` (Minute) vs. `%m` (Monat).
- `math.ceil` (aufrunden) mit `int()` (abschneiden) verwechselt.
- Bibliothek installieren (`pip install`) mit importieren verwechselt.

### Kapitel 11: Dateien öffnen, lesen, schreiben (`kap11_dateien.csv`)

| Konzept / Syntax | Gewicht | Skript | Aufgaben | Karten |
|---|---:|---|---|---:|
| open(pfad, modus): "r", "w", "a"; ohne Modus "r" | 2 | F. 189, 193 | 6.1, 6.2 | 3 |
| read() ganze Datei, read(n) n Zeichen | 2 | F. 190 | 6.1 | 3 |
| Zeilenweise lesen mit for zeile in datei; jede Zeile endet mit \n | 2 | F. 191 | 6.1, 6.2 | 3 |
| readlines() (Liste der Zeilen) und readline() | 1 | F. 191 | 6.1 | 2 |
| write(): nur Strings, kein automatischer Zeilenumbruch | 2 | F. 194 | 6.2 | 3 |
| "w" überschreibt, "a" hängt an | 2 | F. 193–194 | 6.2 | 4 |
| close(): Datei schließen; danach kein Zugriff mehr | 2 | F. 190, 194 | 6.1, 6.2 | 2 |
| Relativer Pfad (../Daten/…) und FileNotFoundError | 1 | F. 189 | 6.1 | 2 |
| Dateiinhalt zeilenweise auswerten (float(zeile), zählen, ersetzen) | 2 | F. 187 | 6.1, 6.2 | 3 |

Typische Fehlerquellen:

- Modus `"w"` löscht den alten Inhalt; zum Anhängen `"a"`.
- `write()` schreibt kein `\n` und nur Strings (`TypeError: write() argument must be str, not int`).
- Gelesene Zeilen enden mit `\n` → doppelte Leerzeilen bei print().
- Zugriff nach `close()` → `ValueError: I/O operation on closed file.`
- Falscher relativer Pfad → FileNotFoundError.

### Kapitel 12: CSV-Dateien und pandas (`kap12_pandas.csv`)

| Konzept / Syntax | Gewicht | Skript | Aufgaben | Karten |
|---|---:|---|---|---:|
| CSV-Format: ein Datensatz pro Zeile, Trennzeichen, Kopfzeile | 1 | F. 198 | 6.3 | 2 |
| pd.read_csv() → DataFrame; Spaltennamen exakt (KeyError) | 2 | F. 199–201 | 6.3–6.5 | 4 |
| DataFrame aus Dictionary, Spalte df["Name"], len(df), head() | 2 | F. 200 | 6.3, 6.4 | 4 |
| Zeilen filtern: df[df["Spalte"] > wert] | 2 | F. 200 | 6.3–6.5 | 3 |
| sort_values(by=…, ascending=…) | 2 | – | 6.3, 6.4 | 2 |
| groupby("A")["B"].mean() – Mittelwert je Gruppe | 1 | F. 200 | 6.3 | 2 |
| value_counts() – Häufigkeit jedes Werts | 1 | – | 6.5 | 2 |

Typische Fehlerquellen:

- Spaltenname nicht exakt (Einheit in Klammern) → KeyError.
- `df["Temp"] > 80` allein filtert nicht, erst `df[df["Temp"] > 80]`.
- Nach `sort_values` bleibt der alte Index erhalten.
- `ascending=False` für absteigend vergessen.
- Kopfzeile wird nicht als Datenzeile gezählt.

### Kapitel 13: Daten visualisieren mit matplotlib und plotly (`kap13_visualisierung.csv`)

| Konzept / Syntax | Gewicht | Skript | Aufgaben | Karten |
|---|---:|---|---|---:|
| import matplotlib.pyplot as plt, plt.plot(x, y), plt.show() | 2 | F. 205 | 2.1, 2.9 | 3 |
| Linienstil: Formatstring "b-o", color, linestyle, linewidth, marker | 1 | F. 206 | 2.1 | 2 |
| title, xlabel, ylabel, grid – vor show() | 2 | F. 205 | 2.1, 6.1, 6.5 | 3 |
| label=… und plt.legend() | 1 | F. 205 | 2.1, 6.5 | 2 |
| Balkendiagramm plt.bar(kategorien, werte) | 2 | F. 207 | 6.1, 6.5 | 3 |
| Histogramm plt.hist(daten, bins=…) | 1 | F. 207 | 6.5 | 2 |
| Streudiagramm plt.scatter(x, y) | 1 | – | 6.5 | 2 |
| Mehrere Diagramme: fig, (ax1, ax2) = plt.subplots(1, 2), ax.set_title, tight_layout | 1 | – | 6.5 | 2 |
| plt.savefig("datei.png", dpi=…) vor plt.show() | 1 | F. 208 | 6.5 | 2 |
| x und y müssen gleich lang sein (ValueError) | 1 | F. 205 | – | 2 |
| plotly.express: px.line, px.scatter_3d(color=…), update_layout, fig.show() | 1 | F. 209 | 6.4 | 4 |

Typische Fehlerquellen:

- `savefig` erst nach `plt.show()`; x- und y-Beschriftung vertauscht (das erste Argument von `plot` liegt auf der x-Achse).
- x- und y-Liste unterschiedlich lang → ValueError.
- `legend()` ohne `label=` → leere Legende.
- Bei Subplots `plt.title` statt `ax.set_title`.
- Bei plotly Spaltennamen statt Listen übergeben.
