<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "54c5a1c74aecb69d2f9099300a4b7eea",
  "translation_date": "2025-09-04T12:17:07+00:00",
  "source_file": "2-Working-With-Data/06-non-relational/README.md",
  "language_code": "zh"
}
-->
# 使用数据：非关系型数据

|![由 [(@sketchthedocs)](https://sketchthedocs.dev) 绘制的速记图](../../sketchnotes/06-NoSQL.png)|
|:---:|
|使用 NoSQL 数据 - _由 [@nitya](https://twitter.com/nitya) 绘制的速记图_ |

## [课前测验](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/10)

数据并不限于关系型数据库。本课重点介绍非关系型数据，并将涵盖电子表格和 NoSQL 的基础知识。

## 电子表格

电子表格是一种流行的数据存储和探索方式，因为它设置和使用起来相对简单。在本课中，您将学习电子表格的基本组成部分，以及公式和函数。示例将以 Microsoft Excel 为例，但大多数部分和主题在其他电子表格软件中具有类似的名称和步骤。

![一个空的 Microsoft Excel 工作簿，包含两个工作表](../../../../translated_images/parts-of-spreadsheet.120711c82aa18a45c3e62a491a15bba0a31ab0e9db407ec022702fed8ffd89bf.zh.png)

电子表格是一个文件，可以通过计算机、设备或基于云的文件系统访问。软件本身可能是基于浏览器的，也可能是需要安装在计算机上的应用程序，或者下载为应用程序。在 Excel 中，这些文件也被定义为 **工作簿**，本课将使用这一术语。

一个工作簿包含一个或多个 **工作表**，每个工作表通过标签标识。在工作表中，有称为 **单元格** 的矩形区域，这些单元格包含实际数据。单元格是行和列的交叉点，其中列用字母标识，行用数字标识。一些电子表格会在前几行中包含标题，用于描述单元格中的数据。

了解了 Excel 工作簿的这些基本元素后，我们将使用 [Microsoft 模板](https://templates.office.com/) 中的一个库存管理示例来进一步讲解电子表格的其他部分。

### 管理库存

名为 "InventoryExample" 的电子表格文件是一个格式化的库存项目表，包含三个工作表，标签分别为 "Inventory List"、"Inventory Pick List" 和 "Bin Lookup"。Inventory List 工作表的第 4 行是标题行，用于描述每列中单元格的值。

![Microsoft Excel 中库存清单示例中的一个公式被高亮显示](../../../../translated_images/formula-excel.ad1068c220892f5ead570d12f2394897961d31a5043a1dd4e6fc5d7690c7a14e.zh.png)

有时，一个单元格的值依赖于其他单元格的值来生成。在 Inventory List 电子表格中，我们记录了库存中每个项目的成本，但如果我们需要知道整个库存的总价值呢？[**公式**](https://support.microsoft.com/en-us/office/overview-of-formulas-34519a4e-1e8d-4f4b-84d4-d642c4f63263) 是对单元格数据执行操作的工具，在本例中用于计算库存的成本。该电子表格在 Inventory Value 列中使用了一个公式，通过将 QTY 标题下的数量与 COST 标题下的成本相乘来计算每个项目的价值。双击或高亮显示一个单元格即可查看公式。您会注意到，公式以等号开头，后面是计算或操作。

![Microsoft Excel 中库存清单示例中的一个函数被高亮显示](../../../../translated_images/function-excel.be2ae4feddc10ca089f3d4363040d93b7fd046c8d4f83ba975ec46483ee99895.zh.png)

我们还可以使用另一个公式将所有 Inventory Value 的值相加，得到总价值。虽然可以通过逐个相加每个单元格的值来计算总和，但这会非常繁琐。Excel 提供了 [**函数**](https://support.microsoft.com/en-us/office/sum-function-043e1c7d-7726-4e80-8f32-07b23e057f89)，即预定义的公式，用于对单元格值执行计算。函数需要参数，即执行这些计算所需的值。当函数需要多个参数时，这些参数必须按特定顺序列出，否则函数可能无法正确计算值。本例使用了 SUM 函数，并将 Inventory Value 的值作为参数，生成了 B3 单元格中的总值。

## NoSQL

NoSQL 是一个总称，涵盖了存储非关系型数据的不同方式，可以解释为 "非 SQL"、"非关系型" 或 "不仅仅是 SQL"。这类数据库系统可以分为四种类型。

![一个键值数据存储的图示，显示了 4 个唯一的数字键与 4 个不同值的关联](../../../../translated_images/kv-db.e8f2b75686bbdfcba0c827b9272c10ae0821611ea0fe98429b9d13194383afa6.zh.png)
> 来源：[Michał Białecki Blog](https://www.michalbialecki.com/2018/03/18/azure-cosmos-db-key-value-database-cloud/)

[键值](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#keyvalue-data-stores) 数据库将唯一键（唯一标识符）与值配对。这些键值对通过 [哈希表](https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/tutorial/) 和适当的哈希函数存储。

![一个图数据存储的图示，显示了人与兴趣及地点之间的关系](../../../../translated_images/graph-db.d13629152f79a9dac895b20fa7d841d4d4d6f6008b1382227c3bbd200fd4cfa1.zh.png)
> 来源：[Microsoft](https://docs.microsoft.com/en-us/azure/cosmos-db/graph/graph-introduction#graph-database-by-example)

[图](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#graph-data-stores) 数据库描述数据中的关系，并以节点和边的集合表示。节点代表实体，即现实世界中存在的事物，例如学生或银行对账单。边表示两个实体之间的关系。每个节点和边都有属性，用于提供关于节点和边的附加信息。

![一个列式数据存储的图示，显示了一个客户数据库，其中包含两个列族：Identity 和 Contact Info](../../../../translated_images/columnar-db.ffcfe73c3e9063a8c8f93f8ace85e1200863584b1e324eb5159d8ca10f62ec04.zh.png)

[列式](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#columnar-data-stores) 数据存储将数据组织为列和行，类似于关系型数据结构，但每列被分为称为列族的组，其中一列下的所有数据是相关的，可以作为一个单元进行检索和更改。

### 使用 Azure Cosmos DB 的文档数据存储

[文档](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#document-data-stores) 数据存储基于键值数据存储的概念，由一系列字段和对象组成。本节将通过 Cosmos DB 模拟器探索文档数据库。

Cosmos DB 数据库符合 "不仅仅是 SQL" 的定义，其中 Cosmos DB 的文档数据库依赖 SQL 来查询数据。[上一课](../05-relational-databases/README.md) 已介绍了 SQL 的基础知识，我们可以在这里将一些相同的查询应用于文档数据库。我们将使用 Cosmos DB 模拟器，它允许我们在本地计算机上创建和探索文档数据库。有关模拟器的更多信息，请阅读[此处](https://docs.microsoft.com/en-us/azure/cosmos-db/local-emulator?tabs=ssl-netstd21)。

文档是字段和对象值的集合，其中字段描述对象值的含义。以下是一个文档示例。

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

此文档中感兴趣的字段包括：`firstname`、`id` 和 `age`。其余带下划线的字段是由 Cosmos DB 自动生成的。

#### 使用 Cosmos DB 模拟器探索数据

您可以[在此处](https://aka.ms/cosmosdb-emulator)下载并安装适用于 Windows 的模拟器。有关在 macOS 和 Linux 上运行模拟器的选项，请参考[此文档](https://docs.microsoft.com/en-us/azure/cosmos-db/local-emulator?tabs=ssl-netstd21#run-on-linux-macos)。

模拟器会启动一个浏览器窗口，其中的 Explorer 视图允许您探索文档。

![Cosmos DB 模拟器的 Explorer 视图](../../../../translated_images/cosmosdb-emulator-explorer.a1c80b1347206fe2f30f88fc123821636587d04fc5a56a9eb350c7da6b31f361.zh.png)

如果您正在跟随操作，请点击 "Start with Sample" 以生成一个名为 SampleDB 的示例数据库。如果展开 SampleDB（点击箭头），您会发现一个名为 `Persons` 的容器。容器包含一组项目，这些项目就是容器中的文档。您可以探索 `Items` 下的四个单独文档。

![在 Cosmos DB 模拟器中探索示例数据](../../../../translated_images/cosmosdb-emulator-persons.bf640586a7077c8985dfd3071946465c8e074c722c7c202d6d714de99a93b90a.zh.png)

#### 使用 Cosmos DB 模拟器查询文档数据

我们还可以通过点击 "New SQL Query" 按钮（从左数第二个按钮）来查询示例数据。

`SELECT * FROM c` 会返回容器中的所有文档。让我们添加一个 where 子句，查找年龄小于 40 的人。

`SELECT * FROM c where c.age < 40`

![在 Cosmos DB 模拟器中运行 SELECT 查询以查找年龄字段值小于 40 的文档](../../../../translated_images/cosmosdb-emulator-persons-query.6905ebb497e3cd047cd96e55a0a03f69ce1b91b2b3d8c147e617b746b22b7e33.zh.png)

查询返回了两个文档，注意每个文档的年龄值都小于 40。

#### JSON 与文档

如果您熟悉 JavaScript 对象表示法（JSON），您会发现文档看起来与 JSON 类似。本目录中有一个 `PersonsData.json` 文件，您可以将其上传到模拟器中的 Persons 容器，方法是使用 `Upload Item` 按钮。

在大多数情况下，返回 JSON 数据的 API 可以直接将数据传输并存储到文档数据库中。以下是另一个文档示例，它表示从 Microsoft Twitter 账户获取的推文数据，这些数据通过 Twitter API 获取后插入到 Cosmos DB 中。

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

此文档中感兴趣的字段包括：`created_at`、`id` 和 `text`。

## 🚀 挑战

目录中有一个 `TwitterData.json` 文件，您可以将其上传到 SampleDB 数据库。建议将其添加到一个单独的容器中。操作步骤如下：

1. 点击右上角的 "New Container" 按钮
2. 选择现有数据库（SampleDB），为容器创建一个 ID
3. 将分区键设置为 `/id`
4. 点击 OK（可以忽略此视图中的其他信息，因为这是一个小型数据集，运行在您的本地机器上）
5. 打开新容器并使用 `Upload Item` 按钮上传 Twitter 数据文件

尝试运行一些 SELECT 查询，查找 `text` 字段中包含 "Microsoft" 的文档。提示：尝试使用 [LIKE 关键字](https://docs.microsoft.com/en-us/azure/cosmos-db/sql/sql-query-keywords#using-like-with-the--wildcard-character)。

## [课后测验](https://ff-quizzes.netlify.app/en/ds/)

## 复习与自学

- 本课未涵盖电子表格中的一些额外格式和功能。如果您有兴趣了解更多，Microsoft 提供了一个[庞大的文档和视频库](https://support.microsoft.com/excel)。

- 这篇架构文档详细介绍了非关系型数据的不同特性：[非关系型数据和 NoSQL](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data)。

- Cosmos DB 是一个基于云的非关系型数据库，也可以存储本课中提到的不同类型的 NoSQL 数据。您可以在此 [Cosmos DB Microsoft Learn 模块](https://docs.microsoft.com/en-us/learn/paths/work-with-nosql-data-in-azure-cosmos-db/) 中了解更多。

## 作业

[Soda Profits](assignment.md)

---

**免责声明**：  
本文档使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于关键信息，建议使用专业人工翻译。我们不对因使用此翻译而产生的任何误解或误读承担责任。