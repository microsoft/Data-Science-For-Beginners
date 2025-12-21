<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11739c7b40e7c6b16ad29e3df4e65862",
  "translation_date": "2025-12-19T10:41:14+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/README.md",
  "language_code": "zh"
}
-->
# 使用数据：关系型数据库

|![ 由 [(@sketchthedocs)](https://sketchthedocs.dev) 绘制的草图笔记 ](../../sketchnotes/05-RelationalData.png)|
|:---:|
| 使用数据：关系型数据库 - _由 [@nitya](https://twitter.com/nitya) 绘制的草图笔记_ |

你很可能过去使用过电子表格来存储信息。你有一组行和列，其中行包含信息（或数据），列描述信息（有时称为元数据）。关系型数据库建立在表中列和行的核心原则之上，允许你将信息分布在多个表中。这使你能够处理更复杂的数据，避免重复，并在探索数据的方式上具有灵活性。让我们来探索关系型数据库的概念。

## [课前测验](https://ff-quizzes.netlify.app/en/ds/quiz/8)

## 一切从表开始

关系型数据库的核心是表。就像电子表格一样，表是列和行的集合。行包含我们希望处理的数据或信息，例如城市名称或降雨量。列描述它们存储的数据。

让我们开始探索，创建一个表来存储城市信息。我们可能从它们的名称和国家开始。你可以将其存储在如下表格中：

| City     | Country       |
| -------- | ------------- |
| Tokyo    | Japan         |
| Atlanta  | United States |
| Auckland | New Zealand   |

注意，**city**、**country** 和 **population** 这些列名描述了所存储的数据，每一行包含一个城市的信息。

## 单表方法的不足

你可能觉得上面的表格相当熟悉。让我们开始向我们不断增长的数据库添加一些额外数据——年降雨量（以毫米为单位）。我们将关注2018、2019和2020年。如果我们为东京添加数据，可能看起来像这样：

| City  | Country | Year | Amount |
| ----- | ------- | ---- | ------ |
| Tokyo | Japan   | 2020 | 1690   |
| Tokyo | Japan   | 2019 | 1874   |
| Tokyo | Japan   | 2018 | 1445   |

你注意到表格有什么吗？你可能注意到我们不断重复城市的名称和国家。这可能占用相当多的存储空间，而且多份拷贝基本上是没必要的。毕竟，东京只有一个我们感兴趣的名称。

好吧，我们试试别的方法。为每一年添加新列：

| City     | Country       | 2018 | 2019 | 2020 |
| -------- | ------------- | ---- | ---- | ---- |
| Tokyo    | Japan         | 1445 | 1874 | 1690 |
| Atlanta  | United States | 1779 | 1111 | 1683 |
| Auckland | New Zealand   | 1386 | 942  | 1176 |

虽然这避免了行的重复，但带来了其他几个挑战。每当有新的一年时，我们需要修改表结构。此外，随着数据增长，将年份作为列会使检索和计算值变得更复杂。

这就是为什么我们需要多个表和关系。通过拆分数据，我们可以避免重复，并在处理数据时拥有更大的灵活性。

## 关系的概念

让我们回到数据，确定如何拆分。我们知道想存储城市的名称和国家，所以这可能最好放在一个表中。

| City     | Country       |
| -------- | ------------- |
| Tokyo    | Japan         |
| Atlanta  | United States |
| Auckland | New Zealand   |

但在创建下一个表之前，我们需要弄清楚如何引用每个城市。我们需要某种形式的标识符、ID或（在技术数据库术语中）主键。主键是用于标识表中某一特定行的值。虽然这可以基于值本身（例如我们可以使用城市名称），但它几乎总是应该是数字或其他标识符。我们不希望ID发生变化，因为这会破坏关系。你会发现大多数情况下主键或ID是自动生成的数字。

> ✅ 主键通常缩写为 PK

### cities

| city_id | City     | Country       |
| ------- | -------- | ------------- |
| 1       | Tokyo    | Japan         |
| 2       | Atlanta  | United States |
| 3       | Auckland | New Zealand   |

> ✅ 你会注意到在本课中我们交替使用“id”和“主键”这两个术语。这里的概念也适用于你稍后会探索的DataFrame。DataFrame不使用“主键”这个术语，但你会发现它们的行为非常相似。

创建了cities表后，让我们存储降雨量。我们不再重复城市的完整信息，而是使用id。我们还应确保新创建的表也有一个*id*列，因为所有表都应该有id或主键。

### rainfall

| rainfall_id | city_id | Year | Amount |
| ----------- | ------- | ---- | ------ |
| 1           | 1       | 2018 | 1445   |
| 2           | 1       | 2019 | 1874   |
| 3           | 1       | 2020 | 1690   |
| 4           | 2       | 2018 | 1779   |
| 5           | 2       | 2019 | 1111   |
| 6           | 2       | 2020 | 1683   |
| 7           | 3       | 2018 | 1386   |
| 8           | 3       | 2019 | 942    |
| 9           | 3       | 2020 | 1176   |

注意新创建的**rainfall**表中的**city_id**列。该列包含引用**cities**表中ID的值。在技术关系数据术语中，这称为**外键**；它是另一个表的主键。你可以把它看作是引用或指针。**city_id** 1引用东京。

> [!NOTE] 
> 外键通常缩写为 FK

## 检索数据

将数据分成两个表后，你可能想知道如何检索它。如果我们使用关系型数据库，如MySQL、SQL Server或Oracle，我们可以使用一种称为结构化查询语言（SQL）的语言。SQL（有时发音为sequel）是用于检索和修改关系型数据库中数据的标准语言。

要检索数据，你使用命令`SELECT`。其核心是你**选择**想要查看的列，**从**它们所在的表中。如果你只想显示城市名称，可以使用以下语句：

```sql
SELECT city
FROM cities;

-- Output:
-- Tokyo
-- Atlanta
-- Auckland
```

`SELECT` 是列出列的地方，`FROM` 是列出表的地方。

> [!NOTE] 
> SQL语法不区分大小写，意味着`select`和`SELECT`是相同的。然而，根据你使用的数据库类型，列和表可能区分大小写。因此，最佳实践是始终将编程中的所有内容视为区分大小写。编写SQL查询时，常见约定是将关键字全部大写。

上面的查询将显示所有城市。假设我们只想显示新西兰的城市。我们需要某种形式的过滤。SQL关键字是`WHERE`，意思是“在某条件为真时”。

```sql
SELECT city
FROM cities
WHERE country = 'New Zealand';

-- Output:
-- Auckland
```

## 连接数据

到目前为止，我们只从单个表中检索数据。现在我们想将**cities**和**rainfall**的数据合并。这通过*连接*它们来完成。你实际上是在两个表之间创建一个连接点，并匹配每个表中某列的值。

在我们的例子中，我们将匹配**rainfall**中的**city_id**列和**cities**中的**city_id**列。这将把降雨量值与其对应的城市匹配。我们执行的连接类型称为*内连接*，意味着如果有任何行与另一个表中的内容不匹配，则不会显示。在我们的例子中，每个城市都有降雨量数据，因此所有内容都会显示。

让我们检索所有城市2019年的降雨量。

我们将分步骤进行。第一步是通过指定连接的列——之前强调的**city_id**——将数据连接起来。

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
```

我们已经突出显示了想要的两列，以及我们希望通过**city_id**连接表。现在我们可以添加`WHERE`语句，只筛选2019年。

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

## 总结

关系型数据库围绕将信息划分到多个表中，然后再将它们组合起来进行显示和分析。这提供了高度的灵活性来执行计算和其他数据操作。你已经了解了关系型数据库的核心概念，以及如何在两个表之间执行连接。

## 🚀 挑战

互联网上有许多关系型数据库可用。你可以使用上面学到的技能来探索数据。

## 课后测验

## [课后测验](https://ff-quizzes.netlify.app/en/ds/quiz/9)

## 复习与自学

在[Microsoft Learn](https://docs.microsoft.com/learn?WT.mc_id=academic-77958-bethanycheum)上有多个资源供你继续探索SQL和关系型数据库概念

- [描述关系数据的概念](https://docs.microsoft.com//learn/modules/describe-concepts-of-relational-data?WT.mc_id=academic-77958-bethanycheum)
- [开始使用Transact-SQL查询](https://docs.microsoft.com//learn/paths/get-started-querying-with-transact-sql?WT.mc_id=academic-77958-bethanycheum)（Transact-SQL是SQL的一个版本）
- [Microsoft Learn上的SQL内容](https://docs.microsoft.com/learn/browse/?products=azure-sql-database%2Csql-server&expanded=azure&WT.mc_id=academic-77958-bethanycheum)

## 作业

[显示机场数据](assignment.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：  
本文件由人工智能翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译而成。虽然我们力求准确，但请注意自动翻译可能存在错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议使用专业人工翻译。我们不对因使用本翻译而产生的任何误解或误释承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->