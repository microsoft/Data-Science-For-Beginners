<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "32ddfef8121650f2ca2f3416fd283c37",
  "translation_date": "2025-08-23T23:40:03+00:00",
  "source_file": "2-Working-With-Data/06-non-relational/README.md",
  "language_code": "de"
}
-->
# Arbeiten mit Daten: Nicht-relationale Daten

|![ Sketchnote von [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/06-NoSQL.png)|
|:---:|
|Arbeiten mit NoSQL-Daten - _Sketchnote von [@nitya](https://twitter.com/nitya)_ |

## [Quiz vor der Vorlesung](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/10)

Daten sind nicht auf relationale Datenbanken beschränkt. Diese Lektion konzentriert sich auf nicht-relationale Daten und behandelt die Grundlagen von Tabellenkalkulationen und NoSQL.

## Tabellenkalkulationen

Tabellenkalkulationen sind eine beliebte Methode, um Daten zu speichern und zu analysieren, da sie weniger Aufwand für die Einrichtung und den Einstieg erfordern. In dieser Lektion lernst du die grundlegenden Bestandteile einer Tabellenkalkulation sowie Formeln und Funktionen kennen. Die Beispiele werden mit Microsoft Excel illustriert, aber die meisten Teile und Themen haben ähnliche Bezeichnungen und Schritte im Vergleich zu anderer Tabellenkalkulationssoftware.

![Eine leere Microsoft Excel-Arbeitsmappe mit zwei Arbeitsblättern](../../../../2-Working-With-Data/06-non-relational/images/parts-of-spreadsheet.png)

Eine Tabellenkalkulation ist eine Datei und wird im Dateisystem eines Computers, Geräts oder cloudbasierten Dateisystems zugänglich sein. Die Software selbst kann browserbasiert oder eine Anwendung sein, die auf einem Computer installiert oder als App heruntergeladen werden muss. In Excel werden diese Dateien auch als **Arbeitsmappen** definiert, und diese Terminologie wird im Rest dieser Lektion verwendet.

Eine Arbeitsmappe enthält ein oder mehrere **Arbeitsblätter**, die durch Tabs gekennzeichnet sind. Innerhalb eines Arbeitsblatts befinden sich Rechtecke, die als **Zellen** bezeichnet werden und die eigentlichen Daten enthalten. Eine Zelle ist der Schnittpunkt einer Zeile und einer Spalte, wobei die Spalten mit alphabetischen Zeichen und die Zeilen numerisch gekennzeichnet sind. Einige Tabellenkalkulationen enthalten in den ersten Zeilen Kopfzeilen, die die Daten in einer Zelle beschreiben.

Mit diesen grundlegenden Elementen einer Excel-Arbeitsmappe verwenden wir ein Beispiel aus den [Microsoft-Vorlagen](https://templates.office.com/), das sich auf ein Inventar konzentriert, um einige zusätzliche Teile einer Tabellenkalkulation zu erläutern.

### Verwaltung eines Inventars

Die Tabellenkalkulationsdatei mit dem Namen "InventoryExample" ist eine formatierte Tabelle von Artikeln in einem Inventar, die drei Arbeitsblätter enthält, deren Tabs mit "Inventory List", "Inventory Pick List" und "Bin Lookup" beschriftet sind. Zeile 4 des Arbeitsblatts "Inventory List" ist die Kopfzeile, die den Wert jeder Zelle in der Kopfspalte beschreibt.

![Eine hervorgehobene Formel aus einer Beispiel-Inventarliste in Microsoft Excel](../../../../2-Working-With-Data/06-non-relational/images/formula-excel.png)

Es gibt Fälle, in denen der Wert einer Zelle von den Werten anderer Zellen abhängt, um berechnet zu werden. Die Tabelle "Inventory List" verfolgt die Kosten jedes Artikels im Inventar, aber was ist, wenn wir den Gesamtwert des Inventars wissen müssen? [**Formeln**](https://support.microsoft.com/de-de/office/overview-of-formulas-34519a4e-1e8d-4f4b-84d4-d642c4f63263) führen Aktionen mit Zellenwerten aus und werden in diesem Beispiel verwendet, um die Kosten des Inventars zu berechnen. Diese Tabelle verwendet eine Formel in der Spalte "Inventory Value", um den Wert jedes Artikels zu berechnen, indem die Menge unter der Kopfzeile "QTY" mit den Kosten unter der Kopfzeile "COST" multipliziert wird. Durch Doppelklicken oder Markieren einer Zelle wird die Formel angezeigt. Du wirst feststellen, dass Formeln mit einem Gleichheitszeichen beginnen, gefolgt von der Berechnung oder Operation.

![Eine hervorgehobene Funktion aus einer Beispiel-Inventarliste in Microsoft Excel](../../../../2-Working-With-Data/06-non-relational/images/function-excel.png)

Wir können eine weitere Formel verwenden, um alle Werte der Spalte "Inventory Value" zusammenzuzählen und den Gesamtwert zu erhalten. Dies könnte berechnet werden, indem jede Zelle einzeln addiert wird, aber das wäre eine mühsame Aufgabe. Excel verfügt über [**Funktionen**](https://support.microsoft.com/de-de/office/sum-function-043e1c7d-7726-4e80-8f32-07b23e057f89), also vordefinierte Formeln, um Berechnungen mit Zellenwerten durchzuführen. Funktionen erfordern Argumente, also die benötigten Werte, um diese Berechnungen auszuführen. Wenn Funktionen mehr als ein Argument benötigen, müssen diese in einer bestimmten Reihenfolge angegeben werden, sonst berechnet die Funktion möglicherweise nicht den korrekten Wert. In diesem Beispiel wird die SUM-Funktion verwendet, die die Werte der Spalte "Inventory Value" als Argument verwendet, um die Summe zu berechnen, die unter Zeile 3, Spalte B (auch als B3 bezeichnet) aufgeführt ist.

## NoSQL

NoSQL ist ein Sammelbegriff für die verschiedenen Möglichkeiten, nicht-relationale Daten zu speichern, und kann als "non-SQL", "nicht-relational" oder "nicht nur SQL" interpretiert werden. Diese Art von Datenbanksystemen kann in 4 Typen kategorisiert werden.

![Grafische Darstellung eines Key-Value-Datenspeichers mit 4 eindeutigen numerischen Schlüsseln, die mit 4 verschiedenen Werten verknüpft sind](../../../../2-Working-With-Data/06-non-relational/images/kv-db.png)
> Quelle: [Michał Białecki Blog](https://www.michalbialecki.com/2018/03/18/azure-cosmos-db-key-value-database-cloud/)

[Key-Value](https://docs.microsoft.com/de-de/azure/architecture/data-guide/big-data/non-relational-data#keyvalue-data-stores)-Datenbanken verknüpfen eindeutige Schlüssel, die als eindeutige Kennung mit einem Wert verbunden sind. Diese Paare werden mithilfe einer [Hash-Tabelle](https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/tutorial/) mit einer geeigneten Hash-Funktion gespeichert.

![Grafische Darstellung eines Graph-Datenspeichers, der die Beziehungen zwischen Personen, ihren Interessen und Standorten zeigt](../../../../2-Working-With-Data/06-non-relational/images/graph-db.png)
> Quelle: [Microsoft](https://docs.microsoft.com/de-de/azure/cosmos-db/graph/graph-introduction#graph-database-by-example)

[Graph](https://docs.microsoft.com/de-de/azure/architecture/data-guide/big-data/non-relational-data#graph-data-stores)-Datenbanken beschreiben Beziehungen in Daten und werden als Sammlung von Knoten und Kanten dargestellt. Ein Knoten repräsentiert eine Entität, etwas, das in der realen Welt existiert, wie ein Student oder ein Kontoauszug. Kanten repräsentieren die Beziehung zwischen zwei Entitäten. Jeder Knoten und jede Kante hat Eigenschaften, die zusätzliche Informationen über die Knoten und Kanten liefern.

![Grafische Darstellung eines spaltenbasierten Datenspeichers, der eine Kundendatenbank mit zwei Spaltenfamilien namens Identity und Contact Info zeigt](../../../../2-Working-With-Data/06-non-relational/images/columnar-db.png)

[Spaltenbasierte](https://docs.microsoft.com/de-de/azure/architecture/data-guide/big-data/non-relational-data#columnar-data-stores) Datenspeicher organisieren Daten in Spalten und Zeilen wie eine relationale Datenstruktur, aber jede Spalte wird in Gruppen namens Spaltenfamilien unterteilt, wobei alle Daten unter einer Spalte miteinander verbunden sind und als Einheit abgerufen und geändert werden können.

### Dokumenten-Datenspeicher mit der Azure Cosmos DB

[Dokumenten](https://docs.microsoft.com/de-de/azure/architecture/data-guide/big-data/non-relational-data#document-data-stores)-Datenspeicher basieren auf dem Konzept eines Key-Value-Datenspeichers und bestehen aus einer Reihe von Feldern und Objekten. Dieser Abschnitt untersucht Dokumenten-Datenbanken mit dem Cosmos DB-Emulator.

Eine Cosmos DB-Datenbank entspricht der Definition von "Nicht nur SQL", wobei die Dokumenten-Datenbank von Cosmos DB auf SQL angewiesen ist, um die Daten abzufragen. Die [vorherige Lektion](../05-relational-databases/README.md) über SQL behandelt die Grundlagen der Sprache, und wir können einige der gleichen Abfragen hier auf eine Dokumenten-Datenbank anwenden. Wir verwenden den Cosmos DB-Emulator, der es uns ermöglicht, eine Dokumenten-Datenbank lokal auf einem Computer zu erstellen und zu erkunden. Weitere Informationen über den Emulator findest du [hier](https://docs.microsoft.com/de-de/azure/cosmos-db/local-emulator?tabs=ssl-netstd21).

Ein Dokument ist eine Sammlung von Feldern und Objektwerten, wobei die Felder beschreiben, was der Objektwert darstellt. Unten ist ein Beispiel für ein Dokument.

```json
{
    "firstname": "Eva",
    "age": 44,
    "id": "8c74a315-aebf-4a16-bb38-2430a9896ce5",
    "_rid": "bHwDAPQz8s0BAAAAAAAAAA==",
    "_self": "dbs/bHwDAA==/colls/bHwDAPQz8s0=/docs/bHwDAPQz8s0BAAAAAAAAAA==/",
    "_etag": "\"00000000-0000-0000-9f95-010a691e01d7\"",
    "_attachments": "attachments/",
    "_ts": 1630544034
}
```

Die interessanten Felder in diesem Dokument sind: `firstname`, `id` und `age`. Die restlichen Felder mit den Unterstrichen wurden von Cosmos DB generiert.

#### Daten mit dem Cosmos DB-Emulator erkunden

Du kannst den Emulator [für Windows hier herunterladen und installieren](https://aka.ms/cosmosdb-emulator). Sieh dir diese [Dokumentation](https://docs.microsoft.com/de-de/azure/cosmos-db/local-emulator?tabs=ssl-netstd21#run-on-linux-macos) für Optionen an, wie du den Emulator unter macOS und Linux ausführen kannst.

Der Emulator öffnet ein Browserfenster, in dem die Explorer-Ansicht es ermöglicht, Dokumente zu erkunden.

![Die Explorer-Ansicht des Cosmos DB-Emulators](../../../../2-Working-With-Data/06-non-relational/images/cosmosdb-emulator-explorer.png)

Wenn du mitmachst, klicke auf "Start with Sample", um eine Beispieldatenbank namens SampleDB zu generieren. Wenn du SampleDB erweiterst, indem du auf den Pfeil klickst, findest du einen Container namens `Persons`. Ein Container enthält eine Sammlung von Elementen, die die Dokumente innerhalb des Containers sind. Du kannst die vier einzelnen Dokumente unter `Items` erkunden.

![Beispieldaten im Cosmos DB-Emulator erkunden](../../../../2-Working-With-Data/06-non-relational/images/cosmosdb-emulator-persons.png)

#### Dokumentendaten mit dem Cosmos DB-Emulator abfragen

Wir können die Beispieldaten auch abfragen, indem wir auf die Schaltfläche "New SQL Query" (zweite Schaltfläche von links) klicken.

`SELECT * FROM c` gibt alle Dokumente im Container zurück. Fügen wir eine WHERE-Klausel hinzu und suchen alle Personen, die jünger als 40 sind.

`SELECT * FROM c where c.age < 40`

![Eine SELECT-Abfrage auf Beispieldaten im Cosmos DB-Emulator ausführen, um Dokumente zu finden, deren Altersfeld kleiner als 40 ist](../../../../2-Working-With-Data/06-non-relational/images/cosmosdb-emulator-persons-query.png)

Die Abfrage gibt zwei Dokumente zurück. Beachte, dass der Alterswert für jedes Dokument kleiner als 40 ist.

#### JSON und Dokumente

Wenn du mit JavaScript Object Notation (JSON) vertraut bist, wirst du feststellen, dass Dokumente JSON ähneln. In diesem Verzeichnis gibt es eine Datei namens `PersonsData.json` mit weiteren Daten, die du in den Container `Persons` im Emulator hochladen kannst, indem du die Schaltfläche `Upload Item` verwendest.

In den meisten Fällen können APIs, die JSON-Daten zurückgeben, direkt in Dokumenten-Datenbanken übertragen und gespeichert werden. Unten ist ein weiteres Dokument, das Tweets vom Microsoft-Twitter-Konto darstellt, die mit der Twitter-API abgerufen und dann in Cosmos DB eingefügt wurden.

```json
{
    "created_at": "2021-08-31T19:03:01.000Z",
    "id": "1432780985872142341",
    "text": "Blank slate. Like this tweet if you’ve ever painted in Microsoft Paint before. https://t.co/cFeEs8eOPK",
    "_rid": "dhAmAIUsA4oHAAAAAAAAAA==",
    "_self": "dbs/dhAmAA==/colls/dhAmAIUsA4o=/docs/dhAmAIUsA4oHAAAAAAAAAA==/",
    "_etag": "\"00000000-0000-0000-9f84-a0958ad901d7\"",
    "_attachments": "attachments/",
    "_ts": 1630537000
```

Die interessanten Felder in diesem Dokument sind: `created_at`, `id` und `text`.

## 🚀 Herausforderung

Es gibt eine Datei namens `TwitterData.json`, die du in die SampleDB-Datenbank hochladen kannst. Es wird empfohlen, sie in einem separaten Container hinzuzufügen. Dies kann wie folgt erfolgen:

1. Klicke auf die Schaltfläche "New Container" oben rechts.
1. Wähle die bestehende Datenbank (SampleDB) aus und erstelle eine Container-ID für den Container.
1. Setze den Partitionsschlüssel auf `/id`.
1. Klicke auf OK (du kannst den Rest der Informationen in dieser Ansicht ignorieren, da es sich um einen kleinen Datensatz handelt, der lokal auf deinem Computer läuft).
1. Öffne deinen neuen Container und lade die Twitter-Daten-Datei mit der Schaltfläche `Upload Item` hoch.

Versuche, ein paar SELECT-Abfragen auszuführen, um die Dokumente zu finden, die "Microsoft" im Textfeld enthalten. Tipp: Versuche, das [LIKE-Schlüsselwort](https://docs.microsoft.com/de-de/azure/cosmos-db/sql/sql-query-keywords#using-like-with-the--wildcard-character) zu verwenden.

## [Quiz nach der Vorlesung](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/11)

## Wiederholung & Selbststudium

- Es gibt einige zusätzliche Formatierungen und Funktionen, die in dieser Lektion nicht behandelt werden. Microsoft bietet eine [große Bibliothek mit Dokumentationen und Videos](https://support.microsoft.com/excel) zu Excel, falls du mehr lernen möchtest.

- Diese architektonische Dokumentation beschreibt die Merkmale der verschiedenen Arten von nicht-relationalen Daten: [Nicht-relationale Daten und NoSQL](https://docs.microsoft.com/de-de/azure/architecture/data-guide/big-data/non-relational-data).

- Cosmos DB ist eine cloudbasierte nicht-relationale Datenbank, die auch die verschiedenen in dieser Lektion erwähnten NoSQL-Typen speichern kann. Erfahre mehr über diese Typen in diesem [Cosmos DB Microsoft Learn Modul](https://docs.microsoft.com/de-de/learn/paths/work-with-nosql-data-in-azure-cosmos-db/).

## Aufgabe

[Soda Profits](assignment.md)

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, weisen wir darauf hin, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.