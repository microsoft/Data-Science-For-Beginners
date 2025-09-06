<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "661dad02c3ac239644d34c1eb51e76f8",
  "translation_date": "2025-09-06T20:26:41+00:00",
  "source_file": "4-Data-Science-Lifecycle/15-analyzing/README.md",
  "language_code": "zh"
}
-->
# 数据科学生命周期：分析

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/15-Analyzing.png)|
|:---:|
| 数据科学生命周期：分析 - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

## [课前测验](https://ff-quizzes.netlify.app/en/ds/quiz/28)

数据生命周期中的分析阶段旨在确认数据是否能够回答提出的问题或解决特定问题。这一步还可以用于验证模型是否正确地解决了这些问题。本课程重点介绍探索性数据分析（EDA），这是一种定义数据特征和关系的技术，并可用于为建模准备数据。

我们将使用 [Kaggle](https://www.kaggle.com/balaka18/email-spam-classification-dataset-csv/version/1) 提供的示例数据集，展示如何通过 Python 和 Pandas 库应用这些技术。该数据集包含一些常见单词在电子邮件中的出现次数，这些电子邮件的来源是匿名的。请使用本目录中的 [notebook](notebook.ipynb) 跟随学习。

## 探索性数据分析

生命周期的捕获阶段是获取数据以及明确问题和问题所在，但我们如何知道数据能够支持最终结果呢？  
回想一下，数据科学家在获取数据时可能会问以下问题：
-   我是否有足够的数据来解决这个问题？
-   数据的质量是否适合解决这个问题？
-   如果通过数据发现了额外的信息，我们是否应该考虑改变或重新定义目标？

探索性数据分析是了解数据的过程，可以用来回答这些问题，同时识别处理数据集时可能面临的挑战。让我们来看看实现这些目标的一些技术。

## 数据分析、描述性统计和 Pandas

我们如何评估是否有足够的数据来解决问题？数据分析可以通过描述性统计技术总结并收集数据集的一些总体信息。数据分析帮助我们了解可用的数据，而描述性统计帮助我们了解数据的数量。

在之前的一些课程中，我们使用 Pandas 的 [`describe()` 函数](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html) 提供了一些描述性统计信息。它可以对数值数据提供计数、最大值和最小值、平均值、标准差以及分位数等信息。使用像 `describe()` 这样的描述性统计方法可以帮助你评估数据量是否足够，是否需要更多数据。

## 抽样和查询

在大型数据集中探索所有内容可能非常耗时，通常由计算机完成。然而，抽样是一种理解数据的有用工具，可以帮助我们更好地了解数据集的内容及其代表的意义。通过抽样，你可以应用概率和统计方法对数据得出一些总体结论。虽然没有明确规定应该抽取多少数据，但需要注意的是，抽取的数据越多，对数据的总体概括就越精确。

Pandas 提供了 [`sample()` 函数](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sample.html)，你可以传递参数来指定需要的随机样本数量。

对数据进行一般查询可以帮助你回答一些普遍的问题和假设。与抽样不同，查询允许你控制并专注于数据中你感兴趣的特定部分。  
Pandas 库中的 [`query()` 函数](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html) 允许你选择列并通过检索的行获得关于数据的简单答案。

## 使用可视化进行探索

你不必等到数据完全清理和分析后再开始创建可视化。事实上，在探索阶段创建可视化可以帮助识别数据中的模式、关系和问题。此外，可视化为那些未直接参与数据管理的人提供了一种沟通方式，同时也可以是一个机会，用于分享和澄清捕获阶段未解决的额外问题。参考 [可视化部分](../../../../../../../../../3-Data-Visualization) 了解一些流行的可视化方法。

## 探索以识别不一致性

本课程中的所有主题都可以帮助识别缺失或不一致的值，而 Pandas 提供了一些函数来检查这些问题。[isna() 或 isnull()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.isna.html) 可以检查缺失值。探索这些值为何会出现缺失是一个重要的步骤，这可以帮助你决定采取哪些 [措施来解决这些问题](/2-Working-With-Data/08-data-preparation/notebook.ipynb)。

## [课后测验](https://ff-quizzes.netlify.app/en/ds/quiz/29)

## 作业

[探索答案](assignment.md)

---

**免责声明**：  
本文档使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。尽管我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原始语言的文档作为权威来源。对于关键信息，建议使用专业人工翻译。因使用本翻译而导致的任何误解或误读，我们概不负责。