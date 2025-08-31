<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "32ddfef8121650f2ca2f3416fd283c37",
  "translation_date": "2025-08-31T10:57:17+00:00",
  "source_file": "2-Working-With-Data/06-non-relational/README.md",
  "language_code": "en"
}
-->
# Working with Data: Non-Relational Data

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/06-NoSQL.png)|
|:---:|
|Working with NoSQL Data - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

## [Pre-Lecture Quiz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/10)

Data isn't limited to relational databases. This lesson focuses on non-relational data and introduces the basics of spreadsheets and NoSQL.

## Spreadsheets

Spreadsheets are a widely used method for storing and analyzing data because they require minimal setup to get started. In this lesson, you'll learn the fundamental components of a spreadsheet, along with formulas and functions. Examples will be demonstrated using Microsoft Excel, but most spreadsheet software will have similar features and steps.

![An empty Microsoft Excel workbook with two worksheets](../../../../2-Working-With-Data/06-non-relational/images/parts-of-spreadsheet.png)

A spreadsheet is a file that can be accessed on a computer, device, or cloud-based file system. The software itself might be browser-based or require installation as an application or app. In Excel, these files are referred to as **workbooks**, and this term will be used throughout the lesson.

A workbook contains one or more **worksheets**, each labeled with tabs. Within a worksheet are rectangles called **cells**, which hold the actual data. A cell is the intersection of a row and column, with columns labeled alphabetically and rows labeled numerically. Some spreadsheets include headers in the first few rows to describe the data in the cells.

Using these basic elements of an Excel workbook, we'll explore an example from [Microsoft Templates](https://templates.office.com/) focused on inventory management to dive deeper into spreadsheet features.

### Managing an Inventory 

The spreadsheet file named "InventoryExample" is a formatted inventory spreadsheet containing three worksheets, with tabs labeled "Inventory List," "Inventory Pick List," and "Bin Lookup." Row 4 of the Inventory List worksheet serves as the header, describing the value of each cell in the corresponding column.

![A highlighted formula from an example inventory list in Microsoft Excel](../../../../2-Working-With-Data/06-non-relational/images/formula-excel.png)

Sometimes, a cell's value depends on other cells to calculate its own value. For example, the Inventory List spreadsheet tracks the cost of each item in the inventory, but what if we need to calculate the total value of the inventory? [**Formulas**](https://support.microsoft.com/en-us/office/overview-of-formulas-34519a4e-1e8d-4f4b-84d4-d642c4f63263) perform operations on cell data, and in this case, a formula is used in the Inventory Value column to calculate the value of each item by multiplying the quantity (under the QTY header) by the cost (under the COST header). Double-clicking or highlighting a cell reveals the formula. Formulas always start with an equals sign, followed by the calculation or operation.

![A highlighted function from an example inventory list in Microsoft Excel](../../../../2-Working-With-Data/06-non-relational/images/function-excel.png)

To find the total inventory value, we can use another formula to sum up all the values in the Inventory Value column. While manually adding each cell is possible, it can be tedious. Excel provides [**functions**](https://support.microsoft.com/en-us/office/sum-function-043e1c7d-7726-4e80-8f32-07b23e057f89), which are predefined formulas for performing calculations on cell values. Functions require arguments—the values needed for the calculation. If a function requires multiple arguments, they must be listed in the correct order to ensure accurate results. In this example, the SUM function is used to add up the values in the Inventory Value column, with the total displayed in row 3, column B (B3).

## NoSQL

NoSQL is a broad term encompassing various methods for storing non-relational data. It can be interpreted as "non-SQL," "non-relational," or "not only SQL." These database systems are categorized into four main types.

![Graphical representation of a key-value data store showing 4 unique numerical keys that are associated with 4 various values](../../../../2-Working-With-Data/06-non-relational/images/kv-db.png)
> Source from [Michał Białecki Blog](https://www.michalbialecki.com/2018/03/18/azure-cosmos-db-key-value-database-cloud/)

[Key-value](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#keyvalue-data-stores) databases pair unique keys (identifiers) with associated values. These pairs are stored using a [hash table](https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/tutorial/) and an appropriate hashing function.

![Graphical representation of a graph data store showing the relationships between people, their interests and locations](../../../../2-Working-With-Data/06-non-relational/images/graph-db.png)
> Source from [Microsoft](https://docs.microsoft.com/en-us/azure/cosmos-db/graph/graph-introduction#graph-database-by-example)

[Graph](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#graph-data-stores) databases represent relationships in data as collections of nodes and edges. Nodes represent entities (e.g., a student or bank statement), while edges represent relationships between entities. Both nodes and edges have properties that provide additional information.

![Graphical representation of a columnar data store showing a customer database with two column families named Identity and Contact Info](../../../../2-Working-With-Data/06-non-relational/images/columnar-db.png)

[Columnar](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#columnar-data-stores) data stores organize data into rows and columns, similar to relational databases, but group columns into column families. All data within a column family is related and can be retrieved or modified as a single unit.

### Document Data Stores with the Azure Cosmos DB 

[Document](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#document-data-stores) data stores expand on the concept of key-value stores, consisting of fields and objects. This section explores document databases using the Cosmos DB emulator.

Cosmos DB fits the "Not Only SQL" definition, as its document database uses SQL for querying data. The [previous lesson](../05-relational-databases/README.md) on SQL covers the basics of the language, which can be applied to document databases here. We'll use the Cosmos DB Emulator to create and explore a document database locally. Learn more about the Emulator [here](https://docs.microsoft.com/en-us/azure/cosmos-db/local-emulator?tabs=ssl-netstd21).

A document is a collection of fields and object values, where fields describe the object values. Below is an example of a document.

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

Key fields in this document include `firstname`, `id`, and `age`. Other fields with underscores are generated by Cosmos DB.

#### Exploring Data with the Cosmos DB Emulator

You can download and install the emulator [for Windows here](https://aka.ms/cosmosdb-emulator). For macOS and Linux, refer to this [documentation](https://docs.microsoft.com/en-us/azure/cosmos-db/local-emulator?tabs=ssl-netstd21#run-on-linux-macos).

The Emulator opens in a browser window, where the Explorer view lets you explore documents.

![The Explorer view of the Cosmos DB Emulator](../../../../2-Working-With-Data/06-non-relational/images/cosmosdb-emulator-explorer.png)

If you're following along, click "Start with Sample" to generate a sample database called SampleDB. Expanding SampleDB reveals a container called `Persons`, which holds a collection of items (documents). You can explore the four individual documents under `Items`.

![Exploring sample data in the Cosmos DB Emulator](../../../../2-Working-With-Data/06-non-relational/images/cosmosdb-emulator-persons.png)

#### Querying Document Data with the Cosmos DB Emulator

You can query the sample data by clicking the "New SQL Query" button (second button from the left).

`SELECT * FROM c` retrieves all documents in the container. Adding a WHERE clause allows filtering, such as finding everyone younger than 40:

`SELECT * FROM c where c.age < 40`

![Running a SELECT query on sample data in the Cosmos DB Emulator to find documents that have an age field value that is less than 40](../../../../2-Working-With-Data/06-non-relational/images/cosmosdb-emulator-persons-query.png)

The query returns two documents, both with age values less than 40.

#### JSON and Documents

If you're familiar with JavaScript Object Notation (JSON), you'll notice that documents resemble JSON. A `PersonsData.json` file in this directory contains additional data that can be uploaded to the Persons container in the Emulator using the `Upload Item` button.

APIs that return JSON data can often be directly stored in document databases. Below is another document, representing tweets from the Microsoft Twitter account retrieved via the Twitter API and inserted into Cosmos DB.

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

Key fields in this document include `created_at`, `id`, and `text`.

## 🚀 Challenge

A `TwitterData.json` file can be uploaded to the SampleDB database. It's recommended to add it to a separate container. To do this:

1. Click the "New Container" button in the top right.
2. Select the existing database (SampleDB), create a container ID for the container.
3. Set the partition key to `/id`.
4. Click OK (you can ignore the rest of the information since this is a small dataset running locally).
5. Open your new container and upload the Twitter Data file using the `Upload Item` button.

Try running a few SELECT queries to find documents containing "Microsoft" in the text field. Hint: Use the [LIKE keyword](https://docs.microsoft.com/en-us/azure/cosmos-db/sql/sql-query-keywords#using-like-with-the--wildcard-character).

## [Post-Lecture Quiz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/11)

## Review & Self Study

- This lesson doesn't cover all the formatting and features available in spreadsheets. Microsoft offers a [comprehensive library of documentation and videos](https://support.microsoft.com/excel) for Excel if you'd like to learn more.

- Learn more about the characteristics of different types of non-relational data in this architectural documentation: [Non-relational Data and NoSQL](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data).

- Cosmos DB is a cloud-based non-relational database that supports the NoSQL types discussed in this lesson. Explore these types further in this [Cosmos DB Microsoft Learn Module](https://docs.microsoft.com/en-us/learn/paths/work-with-nosql-data-in-azure-cosmos-db/).

## Assignment

[Soda Profits](assignment.md)

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.