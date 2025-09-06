<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "12339119c0165da569a93ddba05f9339",
  "translation_date": "2025-09-05T14:03:08+00:00",
  "source_file": "1-Introduction/03-defining-data/README.md",
  "language_code": "de"
}
-->
# Definition von Daten

|![ Sketchnote von [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/03-DefiningData.png)|
|:---:|
|Definition von Daten - _Sketchnote von [@nitya](https://twitter.com/nitya)_ |

Daten sind Fakten, Informationen, Beobachtungen und Messungen, die genutzt werden, um Entdeckungen zu machen und fundierte Entscheidungen zu unterstützen. Ein Datenpunkt ist eine einzelne Einheit innerhalb eines Datensatzes, der eine Sammlung von Datenpunkten darstellt. Datensätze können in unterschiedlichen Formaten und Strukturen vorliegen, abhängig von ihrer Quelle oder Herkunft. Zum Beispiel könnten die monatlichen Einnahmen eines Unternehmens in einer Tabellenkalkulation vorliegen, während stündliche Herzfrequenzdaten von einer Smartwatch im [JSON](https://stackoverflow.com/a/383699)-Format gespeichert sein könnten. Es ist üblich, dass Datenwissenschaftler mit verschiedenen Datentypen innerhalb eines Datensatzes arbeiten.

Diese Lektion konzentriert sich darauf, Daten anhand ihrer Eigenschaften und ihrer Herkunft zu identifizieren und zu klassifizieren.

## [Quiz vor der Vorlesung](https://ff-quizzes.netlify.app/en/ds/quiz/4)

## Wie Daten beschrieben werden

### Rohdaten
Rohdaten sind Daten, die direkt aus ihrer Quelle stammen und sich in ihrem ursprünglichen Zustand befinden, ohne analysiert oder organisiert worden zu sein. Um zu verstehen, was in einem Datensatz vor sich geht, müssen die Daten in ein Format gebracht werden, das sowohl für Menschen als auch für die Technologie, die sie weiter analysieren soll, verständlich ist. Die Struktur eines Datensatzes beschreibt, wie er organisiert ist, und kann als strukturiert, unstrukturiert oder semi-strukturiert klassifiziert werden. Diese Strukturen variieren je nach Quelle, fallen aber letztlich in eine dieser drei Kategorien.

### Quantitative Daten
Quantitative Daten sind numerische Beobachtungen innerhalb eines Datensatzes, die typischerweise analysiert, gemessen und mathematisch verwendet werden können. Beispiele für quantitative Daten sind: die Bevölkerung eines Landes, die Körpergröße einer Person oder die vierteljährlichen Einnahmen eines Unternehmens. Mit zusätzlicher Analyse könnten quantitative Daten genutzt werden, um saisonale Trends des Luftqualitätsindex (AQI) zu entdecken oder die Wahrscheinlichkeit von Berufsverkehr an einem typischen Arbeitstag zu schätzen.

### Qualitative Daten
Qualitative Daten, auch als kategoriale Daten bekannt, sind Daten, die nicht objektiv wie quantitative Daten gemessen werden können. Sie umfassen in der Regel verschiedene Formate subjektiver Daten, die die Qualität von etwas erfassen, wie z. B. ein Produkt oder einen Prozess. Manchmal sind qualitative Daten numerisch, werden aber normalerweise nicht mathematisch verwendet, wie Telefonnummern oder Zeitstempel. Beispiele für qualitative Daten sind: Videokommentare, die Marke und das Modell eines Autos oder die Lieblingsfarbe Ihrer engsten Freunde. Qualitative Daten könnten genutzt werden, um herauszufinden, welche Produkte Verbraucher am meisten mögen, oder um beliebte Schlüsselwörter in Lebensläufen zu identifizieren.

### Strukturierte Daten
Strukturierte Daten sind Daten, die in Zeilen und Spalten organisiert sind, wobei jede Zeile denselben Satz von Spalten enthält. Spalten repräsentieren einen bestimmten Werttyp und werden mit einem Namen versehen, der beschreibt, was der Wert darstellt, während die Zeilen die tatsächlichen Werte enthalten. Spalten haben oft spezifische Regeln oder Einschränkungen für die Werte, um sicherzustellen, dass die Werte die Spalte korrekt repräsentieren. Stellen Sie sich beispielsweise eine Kunden-Tabelle vor, in der jede Zeile eine Telefonnummer enthalten muss und Telefonnummern keine Buchstaben enthalten dürfen. Es könnten Regeln für die Telefonnummernspalte gelten, um sicherzustellen, dass sie niemals leer ist und nur Zahlen enthält.

Ein Vorteil strukturierter Daten ist, dass sie so organisiert werden können, dass sie mit anderen strukturierten Daten in Beziehung gesetzt werden können. Da die Daten jedoch so gestaltet sind, dass sie auf eine bestimmte Weise organisiert sind, kann es viel Aufwand erfordern, ihre Struktur zu ändern. Zum Beispiel würde das Hinzufügen einer E-Mail-Spalte zur Kundentabelle, die nicht leer sein darf, bedeuten, dass Sie herausfinden müssen, wie Sie diese Werte für die bestehenden Kundenzeilen im Datensatz hinzufügen.

Beispiele für strukturierte Daten: Tabellenkalkulationen, relationale Datenbanken, Telefonnummern, Kontoauszüge

### Unstrukturierte Daten
Unstrukturierte Daten können in der Regel nicht in Zeilen oder Spalten kategorisiert werden und folgen keinem bestimmten Format oder Regelwerk. Da unstrukturierte Daten weniger Einschränkungen hinsichtlich ihrer Struktur haben, ist es einfacher, neue Informationen hinzuzufügen, im Vergleich zu einem strukturierten Datensatz. Wenn ein Sensor, der alle zwei Minuten Daten zum Luftdruck erfasst, ein Update erhält, das es ihm ermöglicht, auch die Temperatur zu messen und aufzuzeichnen, erfordert dies keine Änderung der bestehenden Daten, wenn diese unstrukturiert sind. Dies könnte jedoch die Analyse oder Untersuchung dieser Art von Daten zeitaufwändiger machen. Ein Wissenschaftler, der beispielsweise die durchschnittliche Temperatur des letzten Monats aus den Sensordaten ermitteln möchte, könnte feststellen, dass der Sensor in einigen seiner aufgezeichneten Daten ein "e" notiert hat, um anzuzeigen, dass er defekt war, anstatt eine typische Zahl aufzuzeichnen, was bedeutet, dass die Daten unvollständig sind.

Beispiele für unstrukturierte Daten: Textdateien, Textnachrichten, Videodateien

### Semi-strukturierte Daten
Semi-strukturierte Daten haben Merkmale, die sie zu einer Kombination aus strukturierten und unstrukturierten Daten machen. Sie folgen in der Regel keinem Format aus Zeilen und Spalten, sind jedoch auf eine Weise organisiert, die als strukturiert gilt, und können einem festen Format oder Regelwerk folgen. Die Struktur variiert je nach Quelle, von einer klar definierten Hierarchie bis hin zu etwas Flexiblerem, das eine einfache Integration neuer Informationen ermöglicht. Metadaten sind Indikatoren, die helfen, zu entscheiden, wie die Daten organisiert und gespeichert werden, und haben je nach Datentyp verschiedene Namen. Häufige Namen für Metadaten sind Tags, Elemente, Entitäten und Attribute. Ein typisches E-Mail-Nachricht enthält beispielsweise einen Betreff, einen Textkörper und eine Empfängerliste und kann nach Absender oder Versandzeit organisiert werden.

Beispiele für semi-strukturierte Daten: HTML, CSV-Dateien, JavaScript Object Notation (JSON)

## Datenquellen

Eine Datenquelle ist der ursprüngliche Ort, an dem die Daten generiert wurden oder "leben", und variiert je nach Art und Zeitpunkt der Erfassung. Daten, die von ihren Benutzer*innen generiert werden, werden als Primärdaten bezeichnet, während Sekundärdaten aus einer Quelle stammen, die Daten für allgemeine Zwecke gesammelt hat. Zum Beispiel würde eine Gruppe von Wissenschaftler*innen, die Beobachtungen in einem Regenwald sammelt, als primär betrachtet, und wenn sie diese Daten mit anderen Wissenschaftler*innen teilen, würden diese sie als sekundär betrachten.

Datenbanken sind eine häufige Quelle und basieren auf einem Datenbankmanagementsystem, das die Daten hostet und verwaltet, wobei Benutzer*innen Befehle, sogenannte Abfragen, verwenden, um die Daten zu durchsuchen. Dateien als Datenquellen können Audio-, Bild- und Videodateien sowie Tabellenkalkulationen wie Excel sein. Internetquellen sind ein häufiger Ort, an dem Daten gehostet werden, wobei sowohl Datenbanken als auch Dateien gefunden werden können. Programmierschnittstellen, auch bekannt als APIs, ermöglichen es Programmierer*innen, Wege zu schaffen, um Daten über das Internet mit externen Benutzer*innen zu teilen, während das Web-Scraping Daten von einer Webseite extrahiert. Die [Lektionen in "Arbeiten mit Daten"](../../../../../../../../../2-Working-With-Data) konzentrieren sich darauf, wie verschiedene Datenquellen genutzt werden können.

## Fazit

In dieser Lektion haben wir gelernt:

- Was Daten sind
- Wie Daten beschrieben werden
- Wie Daten klassifiziert und kategorisiert werden
- Wo Daten gefunden werden können

## 🚀 Herausforderung

Kaggle ist eine ausgezeichnete Quelle für offene Datensätze. Verwenden Sie das [Dataset-Suchtool](https://www.kaggle.com/datasets), um einige interessante Datensätze zu finden, und klassifizieren Sie 3-5 Datensätze nach diesen Kriterien:

- Sind die Daten quantitativ oder qualitativ?
- Sind die Daten strukturiert, unstrukturiert oder semi-strukturiert?

## [Quiz nach der Vorlesung](https://ff-quizzes.netlify.app/en/ds/quiz/5)

## Überprüfung & Selbststudium

- Diese Microsoft Learn-Einheit mit dem Titel [Klassifizieren Sie Ihre Daten](https://docs.microsoft.com/en-us/learn/modules/choose-storage-approach-in-azure/2-classify-data) bietet eine detaillierte Aufschlüsselung von strukturierten, semi-strukturierten und unstrukturierten Daten.

## Aufgabe

[Datensätze klassifizieren](assignment.md)

---

**Haftungsausschluss**:  
Dieses Dokument wurde mithilfe des KI-Übersetzungsdienstes [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, weisen wir darauf hin, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.