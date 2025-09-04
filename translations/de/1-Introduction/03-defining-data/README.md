<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1228edf3572afca7d7cdcd938b6b4984",
  "translation_date": "2025-09-04T14:16:48+00:00",
  "source_file": "1-Introduction/03-defining-data/README.md",
  "language_code": "de"
}
-->
# Definition von Daten

|![ Sketchnote von [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/03-DefiningData.png)|
|:---:|
|Definition von Daten - _Sketchnote von [@nitya](https://twitter.com/nitya)_ |

Daten sind Fakten, Informationen, Beobachtungen und Messungen, die verwendet werden, um Entdeckungen zu machen und fundierte Entscheidungen zu unterstützen. Ein Datenpunkt ist eine einzelne Einheit innerhalb eines Datensatzes, der eine Sammlung von Datenpunkten darstellt. Datensätze können in verschiedenen Formaten und Strukturen vorliegen und basieren in der Regel auf ihrer Quelle oder dem Ursprung der Daten. Beispielsweise könnten die monatlichen Einnahmen eines Unternehmens in einer Tabellenkalkulation vorliegen, während stündliche Herzfrequenzdaten von einer Smartwatch im [JSON](https://stackoverflow.com/a/383699)-Format gespeichert sein könnten. Es ist üblich, dass Datenwissenschaftler mit verschiedenen Arten von Daten innerhalb eines Datensatzes arbeiten.

Diese Lektion konzentriert sich darauf, Daten anhand ihrer Eigenschaften und ihrer Quellen zu identifizieren und zu klassifizieren.

## [Quiz vor der Vorlesung](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/4)

## Wie Daten beschrieben werden

### Rohdaten
Rohdaten sind Daten, die aus ihrer Quelle in ihrem ursprünglichen Zustand stammen und noch nicht analysiert oder organisiert wurden. Um zu verstehen, was mit einem Datensatz passiert, müssen die Daten in ein Format organisiert werden, das sowohl für Menschen als auch für die Technologie, die sie möglicherweise weiter analysiert, verständlich ist. Die Struktur eines Datensatzes beschreibt, wie er organisiert ist, und kann als strukturiert, unstrukturiert und halbstrukturiert klassifiziert werden. Diese Strukturtypen variieren je nach Quelle, passen jedoch letztendlich in diese drei Kategorien.

### Quantitative Daten
Quantitative Daten sind numerische Beobachtungen innerhalb eines Datensatzes und können typischerweise analysiert, gemessen und mathematisch verwendet werden. Einige Beispiele für quantitative Daten sind: die Bevölkerung eines Landes, die Körpergröße einer Person oder die vierteljährlichen Einnahmen eines Unternehmens. Mit zusätzlicher Analyse könnten quantitative Daten verwendet werden, um saisonale Trends des Luftqualitätsindex (AQI) zu entdecken oder die Wahrscheinlichkeit von Berufsverkehr an einem typischen Arbeitstag zu schätzen.

### Qualitative Daten
Qualitative Daten, auch bekannt als kategoriale Daten, sind Daten, die nicht objektiv wie quantitative Daten gemessen werden können. Es handelt sich in der Regel um verschiedene Formate subjektiver Daten, die die Qualität von etwas erfassen, wie z. B. eines Produkts oder Prozesses. Manchmal sind qualitative Daten numerisch, werden jedoch normalerweise nicht mathematisch verwendet, wie Telefonnummern oder Zeitstempel. Einige Beispiele für qualitative Daten sind: Videokommentare, die Marke und das Modell eines Autos oder die Lieblingsfarbe Ihrer engsten Freunde. Qualitative Daten könnten verwendet werden, um zu verstehen, welche Produkte Verbraucher am meisten mögen oder um beliebte Schlüsselwörter in Lebensläufen zu identifizieren.

### Strukturierte Daten
Strukturierte Daten sind Daten, die in Zeilen und Spalten organisiert sind, wobei jede Zeile denselben Satz von Spalten hat. Spalten repräsentieren einen Wert eines bestimmten Typs und werden mit einem Namen identifiziert, der beschreibt, was der Wert darstellt, während Zeilen die tatsächlichen Werte enthalten. Spalten haben oft eine spezifische Reihe von Regeln oder Einschränkungen für die Werte, um sicherzustellen, dass die Werte die Spalte genau repräsentieren. Stellen Sie sich beispielsweise eine Tabelle mit Kunden vor, in der jede Zeile eine Telefonnummer enthalten muss und die Telefonnummern keine alphabetischen Zeichen enthalten dürfen. Es könnten Regeln für die Spalte "Telefonnummer" gelten, um sicherzustellen, dass sie niemals leer ist und nur Zahlen enthält.

Ein Vorteil strukturierter Daten ist, dass sie so organisiert werden können, dass sie mit anderen strukturierten Daten in Beziehung gesetzt werden können. Da die Daten jedoch so gestaltet sind, dass sie auf eine bestimmte Weise organisiert sind, kann es viel Aufwand erfordern, Änderungen an ihrer Gesamtstruktur vorzunehmen. Beispielsweise bedeutet das Hinzufügen einer E-Mail-Spalte zur Kundentabelle, die nicht leer sein darf, dass Sie herausfinden müssen, wie Sie diese Werte zu den vorhandenen Kundendatensätzen hinzufügen.

Beispiele für strukturierte Daten: Tabellenkalkulationen, relationale Datenbanken, Telefonnummern, Kontoauszüge

### Unstrukturierte Daten
Unstrukturierte Daten können in der Regel nicht in Zeilen oder Spalten kategorisiert werden und enthalten kein Format oder keine Regeln, denen sie folgen müssen. Da unstrukturierte Daten weniger Einschränkungen hinsichtlich ihrer Struktur haben, ist es einfacher, neue Informationen hinzuzufügen, verglichen mit einem strukturierten Datensatz. Wenn ein Sensor, der alle 2 Minuten Daten zum Luftdruck erfasst, ein Update erhält, das es ihm ermöglicht, auch die Temperatur zu messen und aufzuzeichnen, erfordert dies keine Änderung der vorhandenen Daten, wenn sie unstrukturiert sind. Dies kann jedoch dazu führen, dass die Analyse oder Untersuchung dieser Art von Daten länger dauert. Beispielsweise möchte ein Wissenschaftler die durchschnittliche Temperatur des letzten Monats aus den Sensordaten berechnen, stellt jedoch fest, dass der Sensor in einigen seiner aufgezeichneten Daten ein "e" vermerkt hat, um anzuzeigen, dass er defekt war, anstatt eine typische Zahl zu verwenden, was bedeutet, dass die Daten unvollständig sind.

Beispiele für unstrukturierte Daten: Textdateien, Textnachrichten, Videodateien

### Halbstrukturierte Daten
Halbstrukturierte Daten haben Merkmale, die sie zu einer Kombination aus strukturierten und unstrukturierten Daten machen. Sie entsprechen normalerweise nicht einem Format aus Zeilen und Spalten, sind jedoch auf eine Weise organisiert, die als strukturiert angesehen wird und möglicherweise einem festen Format oder einer Reihe von Regeln folgt. Die Struktur variiert je nach Quelle, von einer gut definierten Hierarchie bis hin zu etwas Flexiblerem, das eine einfache Integration neuer Informationen ermöglicht. Metadaten sind Indikatoren, die helfen, zu entscheiden, wie die Daten organisiert und gespeichert werden, und haben je nach Datentyp verschiedene Namen. Einige gängige Namen für Metadaten sind Tags, Elemente, Entitäten und Attribute. Beispielsweise hat eine typische E-Mail-Nachricht einen Betreff, einen Text und eine Gruppe von Empfängern und kann nach Absender oder Zeitpunkt organisiert werden.

Beispiele für halbstrukturierte Daten: HTML, CSV-Dateien, JavaScript Object Notation (JSON)

## Datenquellen

Eine Datenquelle ist der ursprüngliche Ort, an dem die Daten generiert wurden oder "leben", und variiert je nachdem, wie und wann sie gesammelt wurden. Daten, die von ihren Benutzer*innen generiert werden, werden als Primärdaten bezeichnet, während Sekundärdaten aus einer Quelle stammen, die Daten für allgemeine Zwecke gesammelt hat. Beispielsweise würde eine Gruppe von Wissenschaftler*innen, die Beobachtungen in einem Regenwald sammelt, als primär betrachtet, und wenn sie diese mit anderen Wissenschaftler*innen teilen, würde dies für die Nutzenden als sekundär gelten.

Datenbanken sind eine häufige Quelle und basieren auf einem Datenbankverwaltungssystem, um die Daten zu hosten und zu pflegen, wobei Benutzer*innen Befehle, sogenannte Abfragen, verwenden, um die Daten zu erkunden. Dateien als Datenquellen können Audio-, Bild- und Videodateien sowie Tabellenkalkulationen wie Excel sein. Internetquellen sind ein häufiger Ort für das Hosting von Daten, wo sowohl Datenbanken als auch Dateien zu finden sind. Application Programming Interfaces, auch bekannt als APIs, ermöglichen es Programmierer*innen, Wege zu schaffen, Daten über das Internet mit externen Benutzer*innen zu teilen, während der Prozess des Web-Scrapings Daten aus einer Webseite extrahiert. Die [Lektionen in Arbeiten mit Daten](../../../../../../../../../2-Working-With-Data) konzentrieren sich darauf, wie verschiedene Datenquellen verwendet werden können.

## Fazit

In dieser Lektion haben wir gelernt:

- Was Daten sind
- Wie Daten beschrieben werden
- Wie Daten klassifiziert und kategorisiert werden
- Wo Daten zu finden sind

## 🚀 Herausforderung

Kaggle ist eine ausgezeichnete Quelle für offene Datensätze. Verwenden Sie das [Suchtool für Datensätze](https://www.kaggle.com/datasets), um einige interessante Datensätze zu finden und klassifizieren Sie 3-5 Datensätze nach diesen Kriterien:

- Sind die Daten quantitativ oder qualitativ?
- Sind die Daten strukturiert, unstrukturiert oder halbstrukturiert?

## [Quiz nach der Vorlesung](https://ff-quizzes.netlify.app/en/ds/)

## Überprüfung & Selbststudium

- Diese Microsoft Learn-Einheit mit dem Titel [Classify your Data](https://docs.microsoft.com/en-us/learn/modules/choose-storage-approach-in-azure/2-classify-data) bietet eine detaillierte Übersicht über strukturierte, halbstrukturierte und unstrukturierte Daten.

## Aufgabe

[Datensätze klassifizieren](assignment.md)

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, weisen wir darauf hin, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.