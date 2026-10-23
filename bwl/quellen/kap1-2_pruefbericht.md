# Prüfprotokoll – BWL Kapitel 1–2

Stand des Kartensatzes: 291 Karten (`bwl/karten/kap1-2_einleitung-grundlagen.csv`).

## Zusammenfassung

| Prüfung | Ergebnis |
|---|---|
| Aufbau (Validator `werkzeuge/karten.py`) | CSV parst, 291 Zeilen × 2 Felder, keine Kopfzeile, kein BOM, keine LaTeX-Reste, alle Bilddateien vorhanden |
| Abdeckung | alle 113 prüfbaren Inhalte und alle 13 Wiederholungsfragen abgedeckt (siehe `kap1-2_abdeckung.md`) |
| Rechnungen | 24 Rechnungen und Einordnungen per Code nachgerechnet – alle stimmen |
| Wortlaut (difflib gegen pdftotext/OCR der Folien) | 80 Zitatteile, 78 wörtlich; 2 Abweichungen erklärt (unten) |
| Prüf-Agenten, Runde 1 (3 Agenten, je ein Drittel) | 281 Karten geprüft: 0 hoch, 23 mittel, 48 gering → alle eingearbeitet |
| Prüf-Agent, Runde 2 (Nachprüfung der 81 geänderten Karten) | 4 gering → eingearbeitet |

## Erklärte Wortlaut-Abweichungen

- **Rechtsformwahl (F. 44):** Die OCR liest das Wort „Rechtsformwahl“ aus dem Kasten links in die Zeile hinein; auf der Folie steht der Satz wie auf der Karte.
- **„Wirtschaften kurz und knapp“ (F. 27):** Die Folie schreibt „Endscheidungen“ (Tippfehler); die Karte schreibt „Entscheidungen“.

---


## CSV

291 Zeilen, je 2 Felder: OK


## Rechnungen (24 nachgerechnet)

- K150 kmu: Code = Kleinstunternehmen | Karte = Kleinstunternehmen → OK
- K151 kmu: Code = kleines Unternehmen | Karte = kleines Unternehmen → OK
- K152 kmu: Code = kleines Unternehmen | Karte = kleines Unternehmen → OK
- K153 kmu: Code = kleines Unternehmen | Karte = kleines Unternehmen → OK
- K154 kmu: Code = mittleres Unternehmen | Karte = mittleres Unternehmen → OK
- K155 kmu: Code = Großunternehmen | Karte = Großunternehmen → OK
- K156 kmu: Code = Großunternehmen | Karte = Großunternehmen → OK
- K227 mitbestimmung: Code = Drittelparität | Karte = Drittelparität → OK
- K228 mitbestimmung: Code = Unterparität | Karte = Unterparität → OK
- K229 mitbestimmung: Code = volle Parität | Karte = volle Parität → OK
- K258 effizienz: Code = 1.3 | Karte = 1,3 → OK
- K258 effizienz: Code = 1.2 | Karte = 1,2 → OK
- K259 produktivitaet: Code = 4 | Karte = 4 Gehäuse je Maschinenstunde → OK
- K260 aenderung_prozent: Code = 25 | Karte = 25 % → OK
- K262 produktivitaet: Code = 7.5 | Karte = 7,5 Teile je Arbeitsstunde → OK
- K263 wirtschaftlichkeit: Code = 1.2 | Karte = 1,2 → OK
- K264 wirtschaftlichkeit: Code = 0.9 | Karte = 0,9 → OK
- K265 gewinn: Code = 0.7 | Karte = 0,7 Mio. € → OK
- K266 gewinn: Code = -0.3 | Karte = −0,3 Mio. € → OK
- K267 rentabilitaet: Code = 14 | Karte = 14 % → OK
- K268 rentabilitaet: Code = 15 | Karte = 15 % → OK
- K268 rentabilitaet: Code = 14.0625 | Karte = 14,1 % → OK
- K269 prozentpunkte: Code = 2 | Karte = 2 Prozentpunkte → OK
- K269 aenderung_prozent: Code = 20 | Karte = 20 % → OK

## Wortlaut (difflib)

80 Zitatteile geprüft, 78 wörtlich gefunden, 2 mit Abweichung:

| Karte | Ähnlichkeit | Karte sagt | Folientext (beste Stelle) |
|---|---:|---|---|
| K176 | 0.952 | die Regelung der Rechtsbeziehungen zwischen den Gesellschaftern eines Unternehmens (Innenverhältnis) und den Rechtsbeziehungen zwischen dem Unternehmen und seinen externen Stakeholdern (Außenverhältnis) | die regelung der rechtsbeziehungen zwischen den gesellschaftern eines unternehmens (innenverhältnis) und den rechtsbeziehungen zwischen dem unternehmen und seinen externen rechtsformwahl stakeholdern (außenverhäl |
| K042 | 0.989 | Wirtschaften bedeutet, anhand von Zielen Entscheidungen über knappe Ressourcen zu treffen | wirtschaften bedeutet, anhand von zielen endscheidungen über knappe ressourcen zu treffen |
