<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dc8f035ce92e4eaa078ab19caa68267a",
  "translation_date": "2025-08-23T23:38:22+00:00",
  "source_file": "2-Working-With-Data/07-python/assignment.md",
  "language_code": "de"
}
-->
# Aufgabe zur Datenverarbeitung in Python

In dieser Aufgabe bitten wir Sie, den Code, den wir in unseren Herausforderungen begonnen haben, weiterzuentwickeln. Die Aufgabe besteht aus zwei Teilen:

## Modellierung der COVID-19-Ausbreitung

 - [ ] Erstellen Sie *R* Graphen für 5-6 verschiedene Länder auf einem Diagramm zum Vergleich oder auf mehreren Diagrammen nebeneinander.
 - [ ] Untersuchen Sie, wie die Anzahl der Todesfälle und Genesungen mit der Anzahl der Infektionsfälle korreliert.
 - [ ] Finden Sie heraus, wie lange eine typische Krankheit dauert, indem Sie die Infektionsrate und die Sterberate visuell korrelieren und nach Anomalien suchen. Möglicherweise müssen Sie verschiedene Länder betrachten, um dies herauszufinden.
 - [ ] Berechnen Sie die Sterblichkeitsrate und wie sie sich im Laufe der Zeit verändert. *Sie sollten die Dauer der Krankheit in Tagen berücksichtigen, um eine Zeitreihe zu verschieben, bevor Sie Berechnungen durchführen.*

## Analyse von COVID-19-Publikationen

- [ ] Erstellen Sie eine Co-Occurrence-Matrix für verschiedene Medikamente und untersuchen Sie, welche Medikamente häufig zusammen auftreten (d.h. in einem Abstract erwähnt werden). Sie können den Code zur Erstellung der Co-Occurrence-Matrix für Medikamente und Diagnosen anpassen.
- [ ] Visualisieren Sie diese Matrix mit einer Heatmap.
- [ ] Als zusätzliche Herausforderung: Visualisieren Sie die Co-Occurrence von Medikamenten mit einem [Chord-Diagramm](https://en.wikipedia.org/wiki/Chord_diagram). [Diese Bibliothek](https://pypi.org/project/chord/) könnte Ihnen helfen, ein Chord-Diagramm zu erstellen.
- [ ] Als weitere Herausforderung: Extrahieren Sie Dosierungen verschiedener Medikamente (wie **400mg** in *nehmen Sie täglich 400mg Chloroquin*) mithilfe von regulären Ausdrücken und erstellen Sie ein DataFrame, das verschiedene Dosierungen für verschiedene Medikamente zeigt. **Hinweis**: Berücksichtigen Sie numerische Werte, die sich in der Nähe des Medikamentennamens befinden.

## Bewertungskriterien

Exzellent | Angemessen | Verbesserungswürdig
--- | --- | -- |
Alle Aufgaben sind abgeschlossen, grafisch dargestellt und erklärt, einschließlich mindestens einer der beiden zusätzlichen Herausforderungen | Mehr als 5 Aufgaben sind abgeschlossen, keine zusätzlichen Herausforderungen wurden versucht, oder die Ergebnisse sind nicht klar | Weniger als 5 (aber mehr als 3) Aufgaben sind abgeschlossen, Visualisierungen helfen nicht, den Punkt zu verdeutlichen

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, weisen wir darauf hin, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.