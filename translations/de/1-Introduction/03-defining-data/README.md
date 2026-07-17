# Definition von Daten

|![ Sketchnote von [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/03-DefiningData.png)|
|:---:|
|Definition von Daten - _Sketchnote von [@nitya](https://twitter.com/nitya)_ |

Daten sind Fakten, Informationen, Beobachtungen und Messungen, die verwendet werden, um Entdeckungen zu machen und fundierte Entscheidungen zu unterstützen. Ein Datenpunkt ist eine einzelne Einheit von Daten innerhalb eines Datensatzes, welcher eine Sammlung von Datenpunkten ist. Datensätze können in verschiedenen Formaten und Strukturen vorliegen und basieren in der Regel auf ihrer Quelle oder dem Ursprung der Daten. Zum Beispiel könnten die monatlichen Einnahmen eines Unternehmens in einer Tabelle vorliegen, während stündliche Herzfrequenzdaten einer Smartwatch im [JSON](https://stackoverflow.com/a/383699)-Format vorliegen. Es ist üblich, dass Datenwissenschaftler mit verschiedenen Datentypen innerhalb eines Datensatzes arbeiten. 

Diese Lektion konzentriert sich darauf, Daten anhand ihrer Eigenschaften und ihrer Quellen zu identifizieren und zu klassifizieren.

## [Vortrag-Quiz](https://ff-quizzes.netlify.app/en/ds/quiz/4)
## Wie Daten beschrieben werden

### Rohdaten
Rohdaten sind Daten, die von ihrer Quelle im Anfangszustand stammen und nicht analysiert oder organisiert wurden. Um zu verstehen, was mit einem Datensatz passiert, muss er in ein Format organisiert werden, das von Menschen sowie von der Technologie verstanden werden kann, die zur weiteren Analyse verwendet wird. Die Struktur eines Datensatzes beschreibt, wie er organisiert ist, und kann als strukturiert, unstrukturiert oder halbstrukturiert klassifiziert werden. Diese Strukturtypen variieren je nach Quelle, passen aber letztlich in diese drei Kategorien. 

### Quantitative Daten
Quantitative Daten sind numerische Beobachtungen innerhalb eines Datensatzes, die typischerweise analysiert, gemessen und mathematisch verwendet werden können. Einige Beispiele für quantitative Daten sind: die Bevölkerung eines Landes, die Körpergröße einer Person oder die vierteljährlichen Einnahmen eines Unternehmens. Mit zusätzlicher Analyse könnten quantitative Daten verwendet werden, um saisonale Trends des Luftqualitätsindex (AQI) zu entdecken oder die Wahrscheinlichkeit von Stoßzeiten im Berufsverkehr an einem typischen Arbeitstag abzuschätzen.

### Qualitative Daten
Qualitative Daten, auch bekannt als kategoriale Daten, sind Daten, die nicht objektiv wie quantitative Daten gemessen werden können. Es handelt sich meist um verschiedene Formen subjektiver Daten, die die Qualität von etwas, wie einem Produkt oder Prozess, erfassen. Manchmal sind qualitative Daten numerisch, werden jedoch in der Regel nicht mathematisch genutzt, wie Telefonnummern oder Zeitstempel. Beispiele für qualitative Daten sind: Videokommentare, Marke und Modell eines Autos oder die Lieblingsfarbe deiner engsten Freunde. Qualitative Daten könnten verwendet werden, um zu verstehen, welche Produkte Verbraucher am meisten mögen oder um beliebte Schlüsselwörter in Lebensläufen zu identifizieren.

### Strukturierte Daten
Strukturierte Daten sind Daten, die in Zeilen und Spalten organisiert sind, wobei jede Zeile denselben Satz von Spalten hat. Spalten repräsentieren einen Wert eines bestimmten Typs und werden mit einem Namen identifiziert, der beschreibt, was der Wert repräsentiert, während Zeilen die tatsächlichen Werte enthalten. Spalten haben oft festgelegte Regeln oder Einschränkungen für die Werte, um sicherzustellen, dass die Werte die Spalte korrekt repräsentieren. Zum Beispiel stelle dir eine Kundentabelle vor, in der jede Zeile eine Telefonnummer haben muss und die Telefonnummern keine alphabetischen Zeichen enthalten dürfen. Es könnten Regeln für die Spalte mit Telefonnummern gelten, die sicherstellen, dass sie nie leer ist und nur Zahlen enthält. 

Ein Vorteil strukturierter Daten ist, dass sie so organisiert werden können, dass sie mit anderen strukturierten Daten in Beziehung gesetzt werden können. Da die Daten jedoch so gestaltet sind, dass sie auf eine bestimmte Weise organisiert sind, kann das Ändern der Gesamtstruktur viel Aufwand erfordern. Zum Beispiel bedeutet das Hinzufügen einer E-Mail-Spalte zu einer Kundentabelle, die nicht leer sein darf, dass du herausfinden musst, wie du diese Werte in die bereits vorhandenen Kundenzeilen im Datensatz integrieren kannst. 

Beispiele für strukturierte Daten: Tabellen, relationale Datenbanken, Telefonnummern, Kontoauszüge

### Unstrukturierte Daten
Unstrukturierte Daten lassen sich typischerweise nicht in Zeilen oder Spalten kategorisieren und enthalten kein Format oder Regelwerk, dem sie folgen. Da unstrukturierte Daten weniger Einschränkungen in ihrer Struktur haben, ist es einfacher, neue Informationen hinzuzufügen, verglichen mit strukturierten Datensätzen. Wenn ein Sensor, der alle 2 Minuten Daten zum Luftdruck erfasst, ein Update erhält, das ihm erlaubt, Temperatur zu messen und aufzuzeichnen, muss die bestehende Datenstruktur bei unstrukturierten Daten nicht verändert werden. Das kann jedoch die Analyse oder Untersuchung dieser Datenart verlängern. Beispielsweise möchte ein Wissenschaftler die Durchschnittstemperatur des letzten Monats anhand der Sensordaten ermitteln, entdeckt jedoch, dass der Sensor an manchen Stellen ein „e“ aufgezeichnet hat, um anzuzeigen, dass er defekt war, anstatt einer üblichen Zahl – was bedeutet, dass die Daten unvollständig sind.

Beispiele für unstrukturierte Daten: Textdateien, Textnachrichten, Videodateien

### Halbstrukturierte Daten
Halbstrukturierte Daten besitzen Merkmale, die sie als Kombination aus strukturierten und unstrukturierten Daten kennzeichnen. Sie entsprechen typischerweise nicht dem Format von Zeilen und Spalten, sind aber so organisiert, dass sie als strukturiert gelten und einem festen Format oder Regelwerk folgen können. Die Struktur variiert je nach Quelle, etwa von einer gut definierten Hierarchie bis hin zu flexibleren Strukturen, die eine einfache Integration neuer Informationen erlauben. Metadaten sind Indikatoren, die helfen, zu entscheiden, wie Daten organisiert und gespeichert werden, und tragen je nach Datentyp unterschiedliche Bezeichnungen. Häufige Bezeichnungen für Metadaten sind Tags, Elemente, Entitäten und Attribute. Zum Beispiel hat eine typische E-Mail-Nachricht einen Betreff, einen Textkörper und eine Empfängerliste und kann nach Absender oder Versandzeit organisiert werden. 

Beispiele für halbstrukturierte Daten: HTML, CSV-Dateien, JavaScript Object Notation (JSON)

## Datenquellen 

Eine Datenquelle ist der Ursprungsort, an dem die Daten erzeugt wurden oder „leben“, und variiert je nachdem, wie und wann sie gesammelt wurden. Daten, die von ihren Nutzer:innen generiert werden, bezeichnet man als Primärdaten, während Sekundärdaten aus einer Quelle stammen, die Daten für allgemeine Nutzung gesammelt hat. Zum Beispiel wäre eine Gruppe von Wissenschaftlern, die Beobachtungen in einem Regenwald sammelt, als primär anzusehen und wenn sie diese mit anderen Wissenschaftlern teilen, gelten diese Daten für diese als sekundär.

Datenbanken sind eine häufige Quelle und basieren auf einem Datenbankmanagementsystem, das die Daten hostet und verwaltet, wobei Nutzer:innen Befehle, sogenannte Abfragen, verwenden, um die Daten zu durchsuchen. Dateien als Datenquelle können Audio-, Bild- und Videodateien sowie Tabellen wie Excel sein. Internetquellen sind ein verbreiteter Ort zur Datenbereitstellung, wo sowohl Datenbanken als auch Dateien gefunden werden können. Application Programming Interfaces, auch bekannt als APIs, ermöglichen Programmierern, Daten über das Internet mit externen Nutzern zu teilen, während der Prozess des Webscrapings Daten von Webseiten extrahiert. Die [Lektionen in Working with Data](../../../../../../../../../2-Working-With-Data) konzentrieren sich darauf, wie verschiedene Datenquellen genutzt werden.

## Fazit

In dieser Lektion haben wir gelernt:

- Was Daten sind
- Wie Daten beschrieben werden
- Wie Daten klassifiziert und kategorisiert werden
- Wo Daten zu finden sind

## 🚀 Herausforderung

Kaggle ist eine ausgezeichnete Quelle für offene Datensätze. Nutze das [Datensatz-Suchtool](https://www.kaggle.com/datasets), um einige interessante Datensätze zu finden und klassifiziere 3-5 Datensätze nach diesen Kriterien:

- Sind die Daten quantitativ oder qualitativ?
- Sind die Daten strukturiert, unstrukturiert oder halbstrukturiert?

## [Nachtrag-Quiz](https://ff-quizzes.netlify.app/en/ds/quiz/5)



## Review & Selbststudium

- Diese Microsoft Learn-Einheit, mit dem Titel [Datenformate identifizieren](https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats?pivots=text), bietet eine detaillierte Aufschlüsselung von strukturierten, halbstrukturierten und unstrukturierten Daten.

## Aufgabe

[Datensätze klassifizieren](assignment.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->