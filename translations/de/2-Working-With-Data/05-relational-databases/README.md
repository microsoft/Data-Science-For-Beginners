<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11739c7b40e7c6b16ad29e3df4e65862",
  "translation_date": "2025-12-19T10:26:28+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/README.md",
  "language_code": "de"
}
-->
# Arbeiten mit Daten: Relationale Datenbanken

|![ Sketchnote von [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/05-RelationalData.png)|
|:---:|
| Arbeiten mit Daten: Relationale Datenbanken - _Sketchnote von [@nitya](https://twitter.com/nitya)_ |

Wahrscheinlich haben Sie in der Vergangenheit eine Tabellenkalkulation verwendet, um Informationen zu speichern. Sie hatten eine Reihe von Zeilen und Spalten, wobei die Zeilen die Informationen (oder Daten) enthielten und die Spalten die Informationen beschrieben (manchmal auch Metadaten genannt). Eine relationale Datenbank basiert auf diesem Kernprinzip von Spalten und Zeilen in Tabellen, wodurch Sie Informationen über mehrere Tabellen hinweg verteilen können. Dies ermöglicht es Ihnen, mit komplexeren Daten zu arbeiten, Duplikate zu vermeiden und flexibel mit den Daten zu arbeiten. Lassen Sie uns die Konzepte einer relationalen Datenbank erkunden.

## [Vorlesungsquiz](https://ff-quizzes.netlify.app/en/ds/quiz/8)

## Alles beginnt mit Tabellen

Eine relationale Datenbank hat Tabellen als Kern. Genau wie bei der Tabellenkalkulation ist eine Tabelle eine Sammlung von Spalten und Zeilen. Die Zeile enthält die Daten oder Informationen, mit denen wir arbeiten möchten, wie z.B. den Namen einer Stadt oder die Niederschlagsmenge. Die Spalten beschreiben die Daten, die sie speichern.

Beginnen wir unsere Erkundung, indem wir eine Tabelle erstellen, um Informationen über Städte zu speichern. Wir könnten mit ihrem Namen und Land beginnen. Sie könnten dies in einer Tabelle wie folgt speichern:

| Stadt    | Land          |
| -------- | ------------- |
| Tokio    | Japan         |
| Atlanta  | Vereinigte Staaten |
| Auckland | Neuseeland    |

Beachten Sie, dass die Spaltennamen **Stadt**, **Land** und **Bevölkerung** die gespeicherten Daten beschreiben und jede Zeile Informationen über eine Stadt enthält.

## Die Nachteile eines Einzeltabellen-Ansatzes

Wahrscheinlich erscheint Ihnen die obige Tabelle relativ vertraut. Fügen wir einige zusätzliche Daten zu unserer wachsenden Datenbank hinzu – den jährlichen Niederschlag (in Millimetern). Wir konzentrieren uns auf die Jahre 2018, 2019 und 2020. Wenn wir ihn für Tokio hinzufügen würden, könnte es so aussehen:

| Stadt | Land  | Jahr | Menge |
| ----- | ----- | ---- | ----- |
| Tokio | Japan | 2020 | 1690  |
| Tokio | Japan | 2019 | 1874  |
| Tokio | Japan | 2018 | 1445  |

Was fällt Ihnen an unserer Tabelle auf? Sie könnten bemerken, dass wir den Namen und das Land der Stadt immer wieder duplizieren. Das könnte ziemlich viel Speicherplatz beanspruchen und ist größtenteils unnötig, mehrere Kopien davon zu haben. Schließlich hat Tokio nur den einen Namen, der uns interessiert.

OK, versuchen wir etwas anderes. Fügen wir neue Spalten für jedes Jahr hinzu:

| Stadt    | Land           | 2018 | 2019 | 2020 |
| -------- | -------------- | ---- | ---- | ---- |
| Tokio    | Japan          | 1445 | 1874 | 1690 |
| Atlanta  | Vereinigte Staaten | 1779 | 1111 | 1683 |
| Auckland | Neuseeland     | 1386 | 942  | 1176 |

Während dies die Zeilenduplikation vermeidet, bringt es einige andere Herausforderungen mit sich. Wir müssten die Struktur unserer Tabelle jedes Mal ändern, wenn ein neues Jahr hinzukommt. Außerdem wird es mit wachsendem Datenvolumen schwieriger, Werte abzurufen und zu berechnen, wenn unsere Jahre als Spalten dargestellt sind.

Deshalb benötigen wir mehrere Tabellen und Beziehungen. Indem wir unsere Daten aufteilen, können wir Duplikate vermeiden und haben mehr Flexibilität bei der Arbeit mit unseren Daten.

## Die Konzepte von Beziehungen

Kehren wir zu unseren Daten zurück und bestimmen, wie wir sie aufteilen wollen. Wir wissen, dass wir den Namen und das Land unserer Städte speichern möchten, daher funktioniert dies wahrscheinlich am besten in einer Tabelle.

| Stadt    | Land           |
| -------- | -------------- |
| Tokio    | Japan          |
| Atlanta  | Vereinigte Staaten |
| Auckland | Neuseeland     |

Bevor wir jedoch die nächste Tabelle erstellen, müssen wir herausfinden, wie wir auf jede Stadt verweisen wollen. Wir benötigen eine Art Identifikator, ID oder (in technischen Datenbankbegriffen) einen Primärschlüssel. Ein Primärschlüssel ist ein Wert, der verwendet wird, um eine bestimmte Zeile in einer Tabelle zu identifizieren. Obwohl dies auf einem Wert selbst basieren könnte (wir könnten zum Beispiel den Namen der Stadt verwenden), sollte es fast immer eine Zahl oder ein anderer Identifikator sein. Wir wollen nicht, dass sich die ID jemals ändert, da dies die Beziehung zerstören würde. In den meisten Fällen wird der Primärschlüssel oder die ID eine automatisch generierte Zahl sein.

> ✅ Primärschlüssel wird häufig als PK abgekürzt

### Städte

| stadt_id | Stadt    | Land           |
| -------- | -------- | -------------- |
| 1        | Tokio    | Japan          |
| 2        | Atlanta  | Vereinigte Staaten |
| 3        | Auckland | Neuseeland     |

> ✅ Sie werden feststellen, dass wir die Begriffe "id" und "Primärschlüssel" im Verlauf dieser Lektion austauschbar verwenden. Die Konzepte hier gelten auch für DataFrames, die Sie später erkunden werden. DataFrames verwenden jedoch nicht die Terminologie "Primärschlüssel", aber Sie werden feststellen, dass sie sich ähnlich verhalten.

Nachdem wir unsere Städte-Tabelle erstellt haben, speichern wir den Niederschlag. Anstatt die vollständigen Informationen über die Stadt zu duplizieren, können wir die ID verwenden. Wir sollten auch sicherstellen, dass die neu erstellte Tabelle ebenfalls eine *id*-Spalte hat, da alle Tabellen eine ID oder einen Primärschlüssel haben sollten.

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

Beachten Sie die Spalte **stadt_id** in der neu erstellten Tabelle **niederschlag**. Diese Spalte enthält Werte, die auf die IDs in der Tabelle **städte** verweisen. In technischen relationalen Datenbegriffen wird dies als **Fremdschlüssel** bezeichnet; es ist ein Primärschlüssel aus einer anderen Tabelle. Sie können es einfach als Referenz oder Zeiger betrachten. **stadt_id** 1 verweist auf Tokio.

> [!NOTE]  
> Fremdschlüssel wird häufig als FK abgekürzt

## Daten abrufen

Da unsere Daten in zwei Tabellen aufgeteilt sind, fragen Sie sich vielleicht, wie wir sie abrufen. Wenn wir eine relationale Datenbank wie MySQL, SQL Server oder Oracle verwenden, können wir eine Sprache namens Structured Query Language oder SQL verwenden. SQL (manchmal als "sequel" ausgesprochen) ist eine Standardsprache, die verwendet wird, um Daten in einer relationalen Datenbank abzurufen und zu ändern.

Um Daten abzurufen, verwenden Sie den Befehl `SELECT`. Im Kern **wählen** Sie die Spalten aus, die Sie sehen möchten, **aus** der Tabelle, in der sie enthalten sind. Wenn Sie nur die Namen der Städte anzeigen möchten, könnten Sie Folgendes verwenden:

```sql
SELECT city
FROM cities;

-- Output:
-- Tokyo
-- Atlanta
-- Auckland
```
  
`SELECT` ist, wo Sie die Spalten auflisten, und `FROM` ist, wo Sie die Tabellen auflisten.

> [!NOTE]  
> SQL-Syntax ist nicht case-sensitiv, das heißt `select` und `SELECT` bedeuten dasselbe. Je nach Datenbanktyp können jedoch Spalten- und Tabellennamen case-sensitiv sein. Daher ist es eine bewährte Praxis, in der Programmierung immer so zu tun, als ob alles case-sensitiv wäre. Beim Schreiben von SQL-Abfragen ist es üblich, die Schlüsselwörter in Großbuchstaben zu schreiben.

Die obige Abfrage zeigt alle Städte an. Stellen wir uns vor, wir möchten nur Städte in Neuseeland anzeigen. Wir benötigen eine Art Filter. Das SQL-Schlüsselwort dafür ist `WHERE`, oder "wo etwas wahr ist".

```sql
SELECT city
FROM cities
WHERE country = 'New Zealand';

-- Output:
-- Auckland
```
  
## Daten zusammenführen

Bis jetzt haben wir Daten aus einer einzelnen Tabelle abgerufen. Nun wollen wir die Daten aus **städte** und **niederschlag** zusammenführen. Dies geschieht durch *Joinen*. Sie erstellen effektiv eine Verbindung zwischen den beiden Tabellen und ordnen die Werte aus einer Spalte jeder Tabelle einander zu.

In unserem Beispiel ordnen wir die Spalte **stadt_id** in **niederschlag** der Spalte **stadt_id** in **städte** zu. Dadurch wird der Niederschlagswert der jeweiligen Stadt zugeordnet. Die Art des Joins, den wir durchführen, wird als *inner* Join bezeichnet, was bedeutet, dass Zeilen, die keine Übereinstimmung in der anderen Tabelle haben, nicht angezeigt werden. In unserem Fall hat jede Stadt Niederschlagsdaten, daher wird alles angezeigt.

Lassen Sie uns den Niederschlag für 2019 für alle unsere Städte abrufen.

Wir machen das in Schritten. Der erste Schritt ist, die Daten zusammenzuführen, indem wir die Spalten für die Verbindung angeben – **stadt_id**, wie zuvor hervorgehoben.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
```
  
Wir haben die beiden Spalten hervorgehoben, die wir wollen, und die Tatsache, dass wir die Tabellen über die **stadt_id** verbinden wollen. Nun können wir die `WHERE`-Anweisung hinzufügen, um nur das Jahr 2019 herauszufiltern.

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

Relationale Datenbanken basieren darauf, Informationen auf mehrere Tabellen zu verteilen, die dann für Anzeige und Analyse wieder zusammengeführt werden. Dies bietet eine hohe Flexibilität, um Berechnungen durchzuführen und Daten anderweitig zu manipulieren. Sie haben die Kernkonzepte einer relationalen Datenbank gesehen und wie man einen Join zwischen zwei Tabellen durchführt.

## 🚀 Herausforderung

Es gibt zahlreiche relationale Datenbanken im Internet. Sie können die Daten mit den oben erlernten Fähigkeiten erkunden.

## Nach-Vorlesungs-Quiz

## [Nach-Vorlesungs-Quiz](https://ff-quizzes.netlify.app/en/ds/quiz/9)

## Rückblick & Selbststudium

Es gibt mehrere Ressourcen auf [Microsoft Learn](https://docs.microsoft.com/learn?WT.mc_id=academic-77958-bethanycheum), mit denen Sie Ihre Erkundung von SQL und relationalen Datenbankkonzepten fortsetzen können

- [Beschreiben Sie Konzepte relationaler Daten](https://docs.microsoft.com//learn/modules/describe-concepts-of-relational-data?WT.mc_id=academic-77958-bethanycheum)
- [Erste Schritte mit Abfragen in Transact-SQL](https://docs.microsoft.com//learn/paths/get-started-querying-with-transact-sql?WT.mc_id=academic-77958-bethanycheum) (Transact-SQL ist eine Version von SQL)
- [SQL-Inhalte auf Microsoft Learn](https://docs.microsoft.com/learn/browse/?products=azure-sql-database%2Csql-server&expanded=azure&WT.mc_id=academic-77958-bethanycheum)

## Aufgabe

[Anzeige von Flughafendaten](assignment.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->