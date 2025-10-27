<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "80d80300002ef4e77cc7631d5904bd6e",
  "translation_date": "2025-10-25T18:34:11+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/README.md",
  "language_code": "de"
}
-->
# Arbeiten mit Daten: Relationale Datenbanken

|![ Sketchnote von [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/05-RelationalData.png)|
|:---:|
| Arbeiten mit Daten: Relationale Datenbanken - _Sketchnote von [@nitya](https://twitter.com/nitya)_ |

Wahrscheinlich haben Sie in der Vergangenheit schon einmal eine Tabellenkalkulation verwendet, um Informationen zu speichern. Sie hatten eine Reihe von Zeilen und Spalten, wobei die Zeilen die Informationen (oder Daten) enthielten und die Spalten die Informationen beschrieben (manchmal als Metadaten bezeichnet). Eine relationale Datenbank basiert auf diesem Grundprinzip von Spalten und Zeilen in Tabellen, wodurch Informationen auf mehrere Tabellen verteilt werden können. Dies ermöglicht es Ihnen, mit komplexeren Daten zu arbeiten, Duplikate zu vermeiden und Flexibilität bei der Erkundung der Daten zu haben. Lassen Sie uns die Konzepte einer relationalen Datenbank erkunden.

## [Quiz vor der Vorlesung](https://ff-quizzes.netlify.app/en/ds/quiz/8)

## Alles beginnt mit Tabellen

Eine relationale Datenbank hat Tabellen als Kernbestandteil. Genau wie bei der Tabellenkalkulation ist eine Tabelle eine Sammlung von Spalten und Zeilen. Die Zeile enthält die Daten oder Informationen, mit denen wir arbeiten möchten, wie z. B. den Namen einer Stadt oder die Niederschlagsmenge. Die Spalten beschreiben die Daten, die sie speichern.

Beginnen wir unsere Erkundung, indem wir eine Tabelle erstellen, um Informationen über Städte zu speichern. Wir könnten mit ihrem Namen und Land beginnen. Sie könnten dies in einer Tabelle wie folgt speichern:

| Stadt     | Land          |
| --------- | ------------- |
| Tokio     | Japan         |
| Atlanta   | Vereinigte Staaten |
| Auckland  | Neuseeland    |

Beachten Sie, dass die Spaltennamen **Stadt**, **Land** und **Bevölkerung** die gespeicherten Daten beschreiben und jede Zeile Informationen über eine Stadt enthält.

## Die Nachteile eines Ansatzes mit einer einzigen Tabelle

Wahrscheinlich kommt Ihnen die obige Tabelle relativ vertraut vor. Fangen wir an, einige zusätzliche Daten zu unserer wachsenden Datenbank hinzuzufügen - jährlicher Niederschlag (in Millimetern). Wir konzentrieren uns auf die Jahre 2018, 2019 und 2020. Wenn wir dies für Tokio hinzufügen würden, könnte es so aussehen:

| Stadt  | Land    | Jahr | Menge |
| ------ | ------- | ---- | ----- |
| Tokio  | Japan   | 2020 | 1690  |
| Tokio  | Japan   | 2019 | 1874  |
| Tokio  | Japan   | 2018 | 1445  |

Was fällt Ihnen an unserer Tabelle auf? Sie könnten bemerken, dass wir den Namen und das Land der Stadt immer wieder duplizieren. Das könnte ziemlich viel Speicherplatz beanspruchen und ist größtenteils unnötig, da Tokio nur einen Namen hat, der uns interessiert.

Okay, versuchen wir etwas anderes. Fügen wir neue Spalten für jedes Jahr hinzu:

| Stadt     | Land          | 2018 | 2019 | 2020 |
| --------- | ------------- | ---- | ---- | ---- |
| Tokio     | Japan         | 1445 | 1874 | 1690 |
| Atlanta   | Vereinigte Staaten | 1779 | 1111 | 1683 |
| Auckland  | Neuseeland    | 1386 | 942  | 1176 |

Während dies die Zeilenduplikation vermeidet, bringt es einige andere Herausforderungen mit sich. Wir müssten die Struktur unserer Tabelle jedes Mal ändern, wenn ein neues Jahr hinzukommt. Außerdem wird es mit zunehmender Datenmenge schwieriger, Werte zu abrufen und zu berechnen, wenn unsere Jahre als Spalten dargestellt werden.

Deshalb brauchen wir mehrere Tabellen und Beziehungen. Indem wir unsere Daten aufteilen, können wir Duplikate vermeiden und mehr Flexibilität bei der Arbeit mit unseren Daten gewinnen.

## Die Konzepte von Beziehungen

Kehren wir zu unseren Daten zurück und bestimmen, wie wir sie aufteilen möchten. Wir wissen, dass wir den Namen und das Land unserer Städte speichern möchten, daher funktioniert dies wahrscheinlich am besten in einer Tabelle.

| Stadt     | Land          |
| --------- | ------------- |
| Tokio     | Japan         |
| Atlanta   | Vereinigte Staaten |
| Auckland  | Neuseeland    |

Aber bevor wir die nächste Tabelle erstellen, müssen wir herausfinden, wie wir jede Stadt referenzieren möchten. Wir brauchen eine Art Identifikator, ID oder (in technischen Datenbankbegriffen) einen Primärschlüssel. Ein Primärschlüssel ist ein Wert, der verwendet wird, um eine bestimmte Zeile in einer Tabelle zu identifizieren. Obwohl dies auf einem Wert selbst basieren könnte (wir könnten beispielsweise den Namen der Stadt verwenden), sollte es fast immer eine Zahl oder ein anderer Identifikator sein. Wir möchten nicht, dass sich die ID jemals ändert, da dies die Beziehung brechen würde. In den meisten Fällen wird der Primärschlüssel oder die ID automatisch generiert.

> ✅ Der Primärschlüssel wird häufig als PK abgekürzt.

### Städte

| stadt_id | Stadt     | Land          |
| -------- | --------- | ------------- |
| 1        | Tokio     | Japan         |
| 2        | Atlanta   | Vereinigte Staaten |
| 3        | Auckland  | Neuseeland    |

> ✅ Sie werden bemerken, dass wir die Begriffe "id" und "Primärschlüssel" während dieser Lektion austauschbar verwenden. Die Konzepte hier gelten auch für DataFrames, die Sie später erkunden werden. DataFrames verwenden nicht die Terminologie "Primärschlüssel", aber Sie werden feststellen, dass sie sich ähnlich verhalten.

Nachdem wir unsere Städte-Tabelle erstellt haben, speichern wir den Niederschlag. Anstatt die vollständigen Informationen über die Stadt zu duplizieren, können wir die ID verwenden. Wir sollten auch sicherstellen, dass die neu erstellte Tabelle eine *id*-Spalte hat, da alle Tabellen eine ID oder einen Primärschlüssel haben sollten.

### Niederschlag

| niederschlag_id | stadt_id | Jahr | Menge |
| --------------- | -------- | ---- | ----- |
| 1               | 1        | 2018 | 1445  |
| 2               | 1        | 2019 | 1874  |
| 3               | 1        | 2020 | 1690  |
| 4               | 2        | 2018 | 1779  |
| 5               | 2        | 2019 | 1111  |
| 6               | 2        | 2020 | 1683  |
| 7               | 3        | 2018 | 1386  |
| 8               | 3        | 2019 | 942   |
| 9               | 3        | 2020 | 1176  |

Beachten Sie die **stadt_id**-Spalte in der neu erstellten **niederschlag**-Tabelle. Diese Spalte enthält Werte, die auf die IDs in der **städte**-Tabelle verweisen. In technischen relationalen Datenbegriffen wird dies als **Fremdschlüssel** bezeichnet; es ist ein Primärschlüssel aus einer anderen Tabelle. Sie können es einfach als Referenz oder Zeiger betrachten. **stadt_id** 1 verweist auf Tokio.

> [!NOTE] 
> Fremdschlüssel wird häufig als FK abgekürzt.

## Daten abrufen

Mit unseren Daten, die in zwei Tabellen aufgeteilt sind, fragen Sie sich vielleicht, wie wir sie abrufen können. Wenn wir eine relationale Datenbank wie MySQL, SQL Server oder Oracle verwenden, können wir eine Sprache namens Structured Query Language oder SQL verwenden. SQL (manchmal als "Sequel" ausgesprochen) ist eine Standardsprache, die verwendet wird, um Daten in einer relationalen Datenbank abzurufen und zu ändern.

Um Daten abzurufen, verwenden Sie den Befehl `SELECT`. Im Kern **wählen** Sie die Spalten aus, die Sie sehen möchten, **aus** der Tabelle, in der sie enthalten sind. Wenn Sie nur die Namen der Städte anzeigen möchten, könnten Sie Folgendes verwenden:

```sql
SELECT city
FROM cities;

-- Output:
-- Tokyo
-- Atlanta
-- Auckland
```

`SELECT` ist der Ort, an dem Sie die Spalten auflisten, und `FROM` ist der Ort, an dem Sie die Tabellen auflisten.

> [!NOTE] 
> Die SQL-Syntax ist nicht zwischen Groß- und Kleinschreibung unterscheidend, was bedeutet, dass `select` und `SELECT` dasselbe bedeuten. Je nach Art der verwendeten Datenbank können die Spalten und Tabellen jedoch zwischen Groß- und Kleinschreibung unterscheiden. Daher ist es eine bewährte Praxis, in der Programmierung immer alles so zu behandeln, als ob es zwischen Groß- und Kleinschreibung unterscheidet. Beim Schreiben von SQL-Abfragen ist es üblich, die Schlüsselwörter in Großbuchstaben zu schreiben.

Die obige Abfrage zeigt alle Städte an. Stellen wir uns vor, wir möchten nur Städte in Neuseeland anzeigen. Wir brauchen eine Art Filter. Das SQL-Schlüsselwort dafür ist `WHERE`, oder "wo etwas wahr ist".

```sql
SELECT city
FROM cities
WHERE country = 'New Zealand';

-- Output:
-- Auckland
```

## Daten verknüpfen

Bis jetzt haben wir Daten aus einer einzigen Tabelle abgerufen. Jetzt möchten wir die Daten aus **städte** und **niederschlag** zusammenführen. Dies geschieht durch *Verknüpfen* der Tabellen. Sie erstellen effektiv eine Verbindung zwischen den beiden Tabellen und ordnen die Werte aus einer Spalte jeder Tabelle einander zu.

In unserem Beispiel werden wir die **stadt_id**-Spalte in **niederschlag** mit der **stadt_id**-Spalte in **städte** verknüpfen. Dies ordnet den Niederschlagswert der jeweiligen Stadt zu. Die Art der Verknüpfung, die wir durchführen, wird als *innerer* Join bezeichnet, was bedeutet, dass alle Zeilen, die nicht mit einer anderen Tabelle übereinstimmen, nicht angezeigt werden. In unserem Fall hat jede Stadt Niederschlagsdaten, sodass alles angezeigt wird.

Lassen Sie uns die Niederschlagsdaten für 2019 für alle unsere Städte abrufen.

Wir werden dies in Schritten tun. Der erste Schritt besteht darin, die Daten zusammenzuführen, indem wir die Spalten für die Verbindung angeben - **stadt_id**, wie zuvor hervorgehoben.

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

Relationale Datenbanken basieren darauf, Informationen auf mehrere Tabellen zu verteilen, die dann zur Anzeige und Analyse wieder zusammengeführt werden. Dies bietet ein hohes Maß an Flexibilität, um Berechnungen durchzuführen und Daten auf andere Weise zu manipulieren. Sie haben die Kernkonzepte einer relationalen Datenbank kennengelernt und erfahren, wie man eine Verknüpfung zwischen zwei Tabellen herstellt.

## 🚀 Herausforderung

Es gibt zahlreiche relationale Datenbanken im Internet. Sie können die Daten erkunden, indem Sie die oben erlernten Fähigkeiten anwenden.

## Quiz nach der Vorlesung

## [Quiz nach der Vorlesung](https://ff-quizzes.netlify.app/en/ds/quiz/9)

## Überprüfung & Selbststudium

Es gibt mehrere Ressourcen auf [Microsoft Learn](https://docs.microsoft.com/learn?WT.mc_id=academic-77958-bethanycheum), die Ihnen helfen können, Ihre Erkundung von SQL und relationalen Datenbankkonzepten fortzusetzen.

- [Konzepte relationaler Daten beschreiben](https://docs.microsoft.com//learn/modules/describe-concepts-of-relational-data?WT.mc_id=academic-77958-bethanycheum)
- [Erste Schritte mit Transact-SQL](https://docs.microsoft.com//learn/paths/get-started-querying-with-transact-sql?WT.mc_id=academic-77958-bethanycheum) (Transact-SQL ist eine Version von SQL)
- [SQL-Inhalte auf Microsoft Learn](https://docs.microsoft.com/learn/browse/?products=azure-sql-database%2Csql-server&expanded=azure&WT.mc_id=academic-77958-bethanycheum)

## Aufgabe

[Aufgabentitel](assignment.md)

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.