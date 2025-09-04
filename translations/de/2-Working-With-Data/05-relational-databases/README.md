<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11b166fbcb7eaf82308cdc24b562f687",
  "translation_date": "2025-09-04T14:08:37+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/README.md",
  "language_code": "de"
}
-->
# Arbeiten mit Daten: Relationale Datenbanken

|![ Sketchnote von [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/05-RelationalData.png)|
|:---:|
| Arbeiten mit Daten: Relationale Datenbanken - _Sketchnote von [@nitya](https://twitter.com/nitya)_ |

Wahrscheinlich hast du in der Vergangenheit eine Tabellenkalkulation verwendet, um Informationen zu speichern. Du hattest eine Reihe von Zeilen und Spalten, wobei die Zeilen die Informationen (oder Daten) enthielten und die Spalten die Informationen beschrieben (manchmal als Metadaten bezeichnet). Eine relationale Datenbank basiert auf diesem grundlegenden Prinzip von Spalten und Zeilen in Tabellen und ermöglicht es dir, Informationen über mehrere Tabellen hinweg zu verteilen. Dies erlaubt dir, mit komplexeren Daten zu arbeiten, Duplikate zu vermeiden und Flexibilität bei der Datenanalyse zu gewinnen. Lass uns die Konzepte einer relationalen Datenbank erkunden.

## [Quiz vor der Vorlesung](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/8)

## Alles beginnt mit Tabellen

Im Kern besteht eine relationale Datenbank aus Tabellen. Genau wie bei der Tabellenkalkulation ist eine Tabelle eine Sammlung von Spalten und Zeilen. Die Zeilen enthalten die Daten oder Informationen, mit denen wir arbeiten möchten, wie z. B. den Namen einer Stadt oder die Menge an Niederschlag. Die Spalten beschreiben die Daten, die sie speichern.

Beginnen wir unsere Erkundung, indem wir eine Tabelle erstellen, um Informationen über Städte zu speichern. Wir könnten mit ihrem Namen und Land beginnen. Du könntest dies in einer Tabelle wie folgt speichern:

| Stadt     | Land          |
| --------- | ------------- |
| Tokio     | Japan         |
| Atlanta   | Vereinigte Staaten |
| Auckland  | Neuseeland    |

Beachte, dass die Spaltennamen **Stadt**, **Land** und **Bevölkerung** die gespeicherten Daten beschreiben und jede Zeile Informationen über eine Stadt enthält.

## Die Nachteile eines Ansatzes mit nur einer Tabelle

Die obige Tabelle kommt dir wahrscheinlich relativ vertraut vor. Fügen wir nun einige zusätzliche Daten zu unserer wachsenden Datenbank hinzu – den jährlichen Niederschlag (in Millimetern). Wir konzentrieren uns auf die Jahre 2018, 2019 und 2020. Wenn wir die Daten für Tokio hinzufügen würden, könnte das so aussehen:

| Stadt  | Land    | Jahr | Menge  |
| ------ | ------- | ---- | ------ |
| Tokio  | Japan   | 2020 | 1690   |
| Tokio  | Japan   | 2019 | 1874   |
| Tokio  | Japan   | 2018 | 1445   |

Was fällt dir an unserer Tabelle auf? Du könntest bemerken, dass wir den Namen und das Land der Stadt immer wieder duplizieren. Das könnte ziemlich viel Speicherplatz beanspruchen und ist größtenteils unnötig. Schließlich hat Tokio nur einen Namen, der uns interessiert.

OK, versuchen wir etwas anderes. Fügen wir neue Spalten für jedes Jahr hinzu:

| Stadt     | Land          | 2018 | 2019 | 2020 |
| --------- | ------------- | ---- | ---- | ---- |
| Tokio     | Japan         | 1445 | 1874 | 1690 |
| Atlanta   | Vereinigte Staaten | 1779 | 1111 | 1683 |
| Auckland  | Neuseeland    | 1386 | 942  | 1176 |

Während dies die Zeilenduplikation vermeidet, bringt es ein paar andere Herausforderungen mit sich. Wir müssten die Struktur unserer Tabelle jedes Mal ändern, wenn ein neues Jahr hinzukommt. Außerdem wird es mit wachsendem Datenvolumen schwieriger, Werte zu berechnen und abzurufen, wenn unsere Jahre als Spalten dargestellt werden.

Deshalb brauchen wir mehrere Tabellen und Beziehungen. Indem wir unsere Daten aufteilen, können wir Duplikate vermeiden und mehr Flexibilität bei der Arbeit mit unseren Daten gewinnen.

## Die Konzepte von Beziehungen

Kehren wir zu unseren Daten zurück und überlegen, wie wir sie aufteilen möchten. Wir wissen, dass wir den Namen und das Land unserer Städte speichern möchten, daher funktioniert dies wahrscheinlich am besten in einer Tabelle.

| Stadt     | Land          |
| --------- | ------------- |
| Tokio     | Japan         |
| Atlanta   | Vereinigte Staaten |
| Auckland  | Neuseeland    |

Bevor wir die nächste Tabelle erstellen, müssen wir herausfinden, wie wir jede Stadt referenzieren. Wir brauchen eine Art Identifikator, ID oder (in technischen Datenbankbegriffen) einen Primärschlüssel. Ein Primärschlüssel ist ein Wert, der eine bestimmte Zeile in einer Tabelle identifiziert. Während dies auf einem Wert selbst basieren könnte (wir könnten z. B. den Namen der Stadt verwenden), sollte es fast immer eine Zahl oder ein anderer Identifikator sein. Wir möchten nicht, dass sich die ID jemals ändert, da dies die Beziehung zerstören würde. In den meisten Fällen wird der Primärschlüssel oder die ID automatisch generiert.

> ✅ Der Primärschlüssel wird häufig als PK abgekürzt.

### Städte

| stadt_id | Stadt     | Land          |
| -------- | --------- | ------------- |
| 1        | Tokio     | Japan         |
| 2        | Atlanta   | Vereinigte Staaten |
| 3        | Auckland  | Neuseeland    |

> ✅ Du wirst bemerken, dass wir die Begriffe "ID" und "Primärschlüssel" während dieser Lektion austauschbar verwenden. Die Konzepte gelten auch für DataFrames, die du später erkunden wirst. DataFrames verwenden nicht die Terminologie "Primärschlüssel", aber du wirst bemerken, dass sie sich ähnlich verhalten.

Nachdem wir unsere Städte-Tabelle erstellt haben, speichern wir den Niederschlag. Anstatt die vollständigen Informationen über die Stadt zu duplizieren, können wir die ID verwenden. Wir sollten auch sicherstellen, dass die neu erstellte Tabelle ebenfalls eine *ID*-Spalte hat, da alle Tabellen eine ID oder einen Primärschlüssel haben sollten.

### Niederschlag

| niederschlag_id | stadt_id | Jahr | Menge  |
| --------------- | -------- | ---- | ------ |
| 1               | 1        | 2018 | 1445   |
| 2               | 1        | 2019 | 1874   |
| 3               | 1        | 2020 | 1690   |
| 4               | 2        | 2018 | 1779   |
| 5               | 2        | 2019 | 1111   |
| 6               | 2        | 2020 | 1683   |
| 7               | 3        | 2018 | 1386   |
| 8               | 3        | 2019 | 942    |
| 9               | 3        | 2020 | 1176   |

Beachte die **stadt_id**-Spalte in der neu erstellten **niederschlag**-Tabelle. Diese Spalte enthält Werte, die die IDs in der **städte**-Tabelle referenzieren. In technischen relationalen Datenbegriffen wird dies als **Fremdschlüssel** bezeichnet; es ist ein Primärschlüssel aus einer anderen Tabelle. Du kannst es einfach als Referenz oder Zeiger betrachten. **stadt_id** 1 referenziert Tokio.

> [!NOTE] Fremdschlüssel wird häufig als FK abgekürzt.

## Daten abrufen

Mit unseren Daten, die auf zwei Tabellen aufgeteilt sind, fragst du dich vielleicht, wie wir sie abrufen. Wenn wir eine relationale Datenbank wie MySQL, SQL Server oder Oracle verwenden, können wir eine Sprache namens Structured Query Language oder SQL verwenden. SQL (manchmal als "Sequel" ausgesprochen) ist eine Standardsprache, die verwendet wird, um Daten in einer relationalen Datenbank abzurufen und zu ändern.

Um Daten abzurufen, verwendest du den Befehl `SELECT`. Im Kern **wählst** du die Spalten aus, die du sehen möchtest, **aus** der Tabelle, in der sie enthalten sind. Wenn du nur die Namen der Städte anzeigen möchtest, könntest du Folgendes verwenden:

```sql
SELECT city
FROM cities;

-- Output:
-- Tokyo
-- Atlanta
-- Auckland
```

`SELECT` ist der Ort, an dem du die Spalten auflistest, und `FROM` ist der Ort, an dem du die Tabellen auflistest.

> [NOTE] SQL-Syntax ist nicht case-sensitiv, was bedeutet, dass `select` und `SELECT` dasselbe bedeuten. Je nach Art der Datenbank, die du verwendest, könnten die Spalten und Tabellen jedoch case-sensitiv sein. Daher ist es eine bewährte Praxis, immer alles in der Programmierung so zu behandeln, als wäre es case-sensitiv. Beim Schreiben von SQL-Abfragen ist es üblich, die Schlüsselwörter in Großbuchstaben zu schreiben.

Die obige Abfrage zeigt alle Städte an. Angenommen, wir möchten nur Städte in Neuseeland anzeigen. Wir brauchen eine Art Filter. Das SQL-Schlüsselwort dafür ist `WHERE`, oder "wo etwas wahr ist".

```sql
SELECT city
FROM cities
WHERE country = 'New Zealand';

-- Output:
-- Auckland
```

## Daten verbinden

Bis jetzt haben wir Daten aus einer einzigen Tabelle abgerufen. Jetzt möchten wir die Daten aus **städte** und **niederschlag** zusammenführen. Dies geschieht durch *Verbinden* der Tabellen. Du erstellst effektiv eine Verbindung zwischen den beiden Tabellen und ordnest die Werte aus einer Spalte jeder Tabelle einander zu.

In unserem Beispiel werden wir die **stadt_id**-Spalte in **niederschlag** mit der **stadt_id**-Spalte in **städte** verbinden. Dies ordnet den Niederschlagswert der jeweiligen Stadt zu. Die Art der Verbindung, die wir durchführen, ist eine sogenannte *innere* Verbindung, was bedeutet, dass alle Zeilen, die nicht mit einer anderen Tabelle übereinstimmen, nicht angezeigt werden. In unserem Fall hat jede Stadt Niederschlagsdaten, sodass alles angezeigt wird.

Lass uns den Niederschlag für 2019 für alle unsere Städte abrufen.

Wir werden dies in Schritten tun. Der erste Schritt besteht darin, die Daten durch Angabe der Spalten für die Verbindung zu verbinden – **stadt_id**, wie zuvor hervorgehoben.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
```

Wir haben die beiden Spalten hervorgehoben, die wir möchten, und die Tatsache, dass wir die Tabellen durch die **stadt_id** verbinden möchten. Jetzt können wir die `WHERE`-Anweisung hinzufügen, um nur das Jahr 2019 herauszufiltern.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
WHERE rainfall.year = 2019

-- Output

-- city     | amount
-- -------- | ------
-- Tokyo    | 1874
-- Atlanta  | 1111
-- Auckland |  942
```

## Zusammenfassung

Relationale Datenbanken basieren darauf, Informationen auf mehrere Tabellen zu verteilen, die dann zur Anzeige und Analyse wieder zusammengeführt werden. Dies bietet ein hohes Maß an Flexibilität, um Berechnungen durchzuführen und Daten zu manipulieren. Du hast die grundlegenden Konzepte einer relationalen Datenbank gesehen und gelernt, wie man eine Verbindung zwischen zwei Tabellen herstellt.

## 🚀 Herausforderung

Es gibt zahlreiche relationale Datenbanken im Internet. Du kannst die Daten erkunden, indem du die oben erlernten Fähigkeiten anwendest.

## Quiz nach der Vorlesung

## [Quiz nach der Vorlesung](https://ff-quizzes.netlify.app/en/ds/)

## Überprüfung & Selbststudium

Es gibt mehrere Ressourcen auf [Microsoft Learn](https://docs.microsoft.com/learn?WT.mc_id=academic-77958-bethanycheum), die dir helfen, SQL und relationale Datenbankkonzepte weiter zu erkunden.

- [Konzepte relationaler Daten beschreiben](https://docs.microsoft.com//learn/modules/describe-concepts-of-relational-data?WT.mc_id=academic-77958-bethanycheum)
- [Erste Schritte mit Abfragen in Transact-SQL](https://docs.microsoft.com//learn/paths/get-started-querying-with-transact-sql?WT.mc_id=academic-77958-bethanycheum) (Transact-SQL ist eine Version von SQL)
- [SQL-Inhalte auf Microsoft Learn](https://docs.microsoft.com/learn/browse/?products=azure-sql-database%2Csql-server&expanded=azure&WT.mc_id=academic-77958-bethanycheum)

## Aufgabe

[Aufgabentitel](assignment.md)

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, weisen wir darauf hin, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.