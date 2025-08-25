<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "01d1b493e8b51a6ebb42524f6b1bcfff",
  "translation_date": "2025-08-24T21:44:16+00:00",
  "source_file": "1-Introduction/04-stats-and-probability/assignment.md",
  "language_code": "de"
}
-->
# Kleine Diabetes-Studie

In dieser Aufgabe arbeiten wir mit einem kleinen Datensatz von Diabetes-Patienten, der von [hier](https://www4.stat.ncsu.edu/~boos/var.select/diabetes.html) stammt.

|   | ALTER | GESCHLECHT | BMI | BLUTDRUCK | S1 | S2 | S3 | S4 | S5 | S6 | Y  |
|---|-------|------------|-----|-----------|----|----|----|----|----|----|----|
| 0 | 59    | 2          | 32.1| 101.0     | 157| 93.2| 38.0| 4.0 | 4.8598 | 87 | 151 |
| 1 | 48    | 1          | 21.6| 87.0      | 183| 103.2| 70.0| 3.0 | 3.8918 | 69 | 75  |
| 2 | 72    | 2          | 30.5| 93.0      | 156| 93.6| 41.0| 4.0 | 4.0    | 85 | 141 |
| ... | ... | ...        | ... | ...       | ...| ... | ... | ... | ...    | ...| ... |

## Anweisungen

* Öffnen Sie das [Aufgaben-Notebook](../../../../1-Introduction/04-stats-and-probability/assignment.ipynb) in einer Jupyter-Notebook-Umgebung.
* Bearbeiten Sie alle im Notebook aufgeführten Aufgaben, nämlich:
   * [ ] Berechnen Sie Mittelwerte und Varianzen für alle Werte.
   * [ ] Erstellen Sie Boxplots für BMI, Blutdruck und Y in Abhängigkeit vom Geschlecht.
   * [ ] Wie ist die Verteilung der Variablen Alter, Geschlecht, BMI und Y?
   * [ ] Testen Sie die Korrelation zwischen verschiedenen Variablen und dem Krankheitsverlauf (Y).
   * [ ] Testen Sie die Hypothese, dass der Grad des Diabetesverlaufs zwischen Männern und Frauen unterschiedlich ist.

## Bewertungskriterien

Vorbildlich | Angemessen | Verbesserungswürdig
--- | --- | --- |
Alle erforderlichen Aufgaben sind abgeschlossen, grafisch dargestellt und erklärt | Die meisten Aufgaben sind abgeschlossen, Erklärungen oder Schlussfolgerungen aus den Grafiken und/oder den erhaltenen Werten fehlen | Nur grundlegende Aufgaben wie die Berechnung von Mittelwert/Varianz und einfache Diagramme sind abgeschlossen, es werden keine Schlussfolgerungen aus den Daten gezogen

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, weisen wir darauf hin, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.