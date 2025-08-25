<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3ade580a06b5f04d57cc83a768a8fb77",
  "translation_date": "2025-08-25T16:18:18+00:00",
  "source_file": "2-Working-With-Data/08-data-preparation/README.md",
  "language_code": "zh"
}
-->
# 数据处理：数据准备

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/08-DataPreparation.png)|
|:---:|
|数据准备 - _由 [@nitya](https://twitter.com/nitya) 绘制的速记图_ |

## [课前测验](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/14)

根据数据来源，原始数据可能存在一些不一致性，这会在分析和建模时带来挑战。换句话说，这些数据可以被归类为“脏数据”，需要进行清理。本课程重点介绍清理和转换数据的技术，以解决数据缺失、不准确或不完整的问题。本课程将使用 Python 和 Pandas 库，并在本目录中的[笔记本](../../../../2-Working-With-Data/08-data-preparation/notebook.ipynb)中进行演示。

## 清理数据的重要性

- **易于使用和复用**：当数据被正确组织和规范化时，更容易搜索、使用和与他人共享。

- **一致性**：数据科学通常需要处理多个数据集，不同来源的数据集需要合并在一起。确保每个单独的数据集具有统一的标准化，可以保证在合并为一个数据集时数据仍然有用。

- **模型准确性**：清理过的数据可以提高依赖于这些数据的模型的准确性。

## 常见的清理目标和策略

- **探索数据集**：数据探索（将在[后续课程](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/4-Data-Science-Lifecycle/15-analyzing)中介绍）可以帮助发现需要清理的数据。通过可视化观察数据集中的值，可以设定对其余数据的期望，或者提供解决问题的思路。探索可以包括基本查询、可视化和采样。

- **格式化**：根据数据来源，数据在呈现方式上可能存在不一致性。这可能会导致在搜索和表示值时出现问题，数据虽然在数据集中可见，但在可视化或查询结果中未正确表示。常见的格式化问题包括解决空白、日期和数据类型问题。解决格式化问题通常由使用数据的人来决定。例如，不同国家对日期和数字的表示标准可能不同。

- **重复数据**：重复出现的数据可能会产生不准确的结果，通常需要删除。这在合并两个或多个数据集时很常见。然而，有些情况下，合并数据集中的重复数据可能包含额外信息，需要保留。

- **缺失数据**：缺失数据可能导致结果不准确或偏差。有时可以通过重新加载数据、使用 Python 等代码计算填充缺失值，或者简单地删除缺失值及其相关数据来解决。数据缺失的原因有很多，解决缺失值的方式可能取决于数据缺失的原因和方式。

## 探索 DataFrame 信息
> **学习目标**：在本小节结束时，您应该能够熟练地查找存储在 pandas DataFrame 中的总体数据信息。

将数据加载到 pandas 后，数据通常会以 DataFrame 的形式存储（详细概述请参考之前的[课程](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/2-Working-With-Data/07-python#dataframe)）。然而，如果您的 DataFrame 数据集有 60,000 行和 400 列，如何开始了解您正在处理的数据呢？幸运的是，[pandas](https://pandas.pydata.org/) 提供了一些方便的工具，可以快速查看 DataFrame 的总体信息以及前几行和后几行。

为了探索这些功能，我们将导入 Python 的 scikit-learn 库，并使用一个经典数据集：**Iris 数据集**。

```python
import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()
iris_df = pd.DataFrame(data=iris['data'], columns=iris['feature_names'])
```
|                                        |sepal length (cm)|sepal width (cm)|petal length (cm)|petal width (cm)|
|----------------------------------------|-----------------|----------------|-----------------|----------------|
|0                                       |5.1              |3.5             |1.4              |0.2             |
|1                                       |4.9              |3.0             |1.4              |0.2             |
|2                                       |4.7              |3.2             |1.3              |0.2             |
|3                                       |4.6              |3.1             |1.5              |0.2             |
|4                                       |5.0              |3.6             |1.4              |0.2             |

- **DataFrame.info**：首先，`info()` 方法用于打印 `DataFrame` 中内容的摘要。让我们看看这个数据集包含哪些内容：
```python
iris_df.info()
```
```
RangeIndex: 150 entries, 0 to 149
Data columns (total 4 columns):
 #   Column             Non-Null Count  Dtype  
---  ------             --------------  -----  
 0   sepal length (cm)  150 non-null    float64
 1   sepal width (cm)   150 non-null    float64
 2   petal length (cm)  150 non-null    float64
 3   petal width (cm)   150 non-null    float64
dtypes: float64(4)
memory usage: 4.8 KB
```
从中我们可以知道 *Iris* 数据集有 150 条记录，分布在四列中，没有空值。所有数据都存储为 64 位浮点数。

- **DataFrame.head()**：接下来，为了检查 `DataFrame` 的实际内容，我们使用 `head()` 方法。让我们看看 `iris_df` 的前几行：
```python
iris_df.head()
```
```
   sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
0                5.1               3.5                1.4               0.2
1                4.9               3.0                1.4               0.2
2                4.7               3.2                1.3               0.2
3                4.6               3.1                1.5               0.2
4                5.0               3.6                1.4               0.2
```
- **DataFrame.tail()**：相反，为了检查 `DataFrame` 的最后几行，我们使用 `tail()` 方法：
```python
iris_df.tail()
```
```
     sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
145                6.7               3.0                5.2               2.3
146                6.3               2.5                5.0               1.9
147                6.5               3.0                5.2               2.0
148                6.2               3.4                5.4               2.3
149                5.9               3.0                5.1               1.8
```
> **总结**：仅通过查看 DataFrame 的元数据或前几行和后几行的值，您就可以立即了解数据的大小、形状和内容。

## 处理缺失数据
> **学习目标**：在本小节结束时，您应该知道如何替换或删除 DataFrame 中的空值。

大多数情况下，您想使用（或必须使用）的数据集中会有缺失值。如何处理缺失数据会带来微妙的权衡，这可能会影响最终分析和实际结果。

Pandas 处理缺失值有两种方式。第一种您在之前的章节中已经见过：`NaN`，即非数字。这实际上是 IEEE 浮点规范的一部分，用于表示缺失的浮点值。

对于浮点值以外的缺失值，pandas 使用 Python 的 `None` 对象。虽然同时遇到两种表示缺失值的方式可能会让人困惑，但这种设计选择有其合理的编程原因，实际上，这种方式为绝大多数情况提供了良好的折中方案。尽管如此，`None` 和 `NaN` 都有一些限制，您需要注意它们的使用方式。

在[笔记本](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/4-Data-Science-Lifecycle/15-analyzing/notebook.ipynb)中了解更多关于 `NaN` 和 `None` 的信息！

- **检测空值**：在 `pandas` 中，`isnull()` 和 `notnull()` 方法是检测空数据的主要方法。两者都会返回布尔掩码。我们将使用 `numpy` 来处理 `NaN` 值：
```python
import numpy as np

example1 = pd.Series([0, np.nan, '', None])
example1.isnull()
```
```
0    False
1     True
2    False
3     True
dtype: bool
```
仔细观察输出。是否有任何结果让您感到惊讶？虽然 `0` 是一个算术上的空值，但它仍然是一个有效的整数，pandas 将其视为有效值。`''` 则稍微复杂一些。虽然我们在第 1 节中用它表示空字符串值，但它仍然是一个字符串对象，而不是 pandas 所认为的空值。

现在，让我们反过来以更实际的方式使用这些方法。您可以直接将布尔掩码用作 `Series` 或 `DataFrame` 的索引，这在处理孤立的缺失值（或存在值）时非常有用。

> **总结**：在 `DataFrame` 中使用 `isnull()` 和 `notnull()` 方法时，它们会显示结果及其索引，这在处理数据时非常有帮助。

- **删除空值**：除了识别缺失值，pandas 还提供了一种方便的方法来从 `Series` 和 `DataFrame` 中删除空值。（特别是在大型数据集上，通常建议直接删除缺失值，而不是以其他方式处理它们。）让我们回到 `example1` 来看看：
```python
example1 = example1.dropna()
example1
```
```
0    0
2     
dtype: object
```
注意，这应该与您的 `example3[example3.notnull()]` 输出类似。不同之处在于，`dropna` 删除了 `Series` `example1` 中的缺失值，而不是仅仅索引掩码值。

由于 `DataFrame` 是二维的，它提供了更多删除数据的选项。

```python
example2 = pd.DataFrame([[1,      np.nan, 7], 
                         [2,      5,      8], 
                         [np.nan, 6,      9]])
example2
```
|      | 0 | 1 | 2 |
|------|---|---|---|
|0     |1.0|NaN|7  |
|1     |2.0|5.0|8  |
|2     |NaN|6.0|9  |

（您是否注意到 pandas 将两列数据类型提升为浮点型以容纳 `NaN`？）

您无法从 `DataFrame` 中删除单个值，因此必须删除整行或整列。根据您的需求，您可能需要删除其中之一，因此 pandas 提供了两种选项。由于在数据科学中，列通常表示变量，行表示观察值，您更可能删除数据行；`dropna()` 的默认设置是删除所有包含任何空值的行：

```python
example2.dropna()
```
```
	0	1	2
1	2.0	5.0	8
```
如果需要，您可以从列中删除 NA 值。使用 `axis=1` 来实现：
```python
example2.dropna(axis='columns')
```
```
	2
0	7
1	8
2	9
```
注意，这可能会删除许多您可能希望保留的数据，特别是在较小的数据集中。如果您只想删除包含多个或所有空值的行或列，可以在 `dropna` 中使用 `how` 和 `thresh` 参数进行设置。

默认情况下，`how='any'`（如果您想自己检查或查看方法的其他参数，请在代码单元中运行 `example4.dropna?`）。您可以选择指定 `how='all'`，以便仅删除包含所有空值的行或列。让我们扩展示例 `DataFrame` 来看看效果。

```python
example2[3] = np.nan
example2
```
|      |0  |1  |2  |3  |
|------|---|---|---|---|
|0     |1.0|NaN|7  |NaN|
|1     |2.0|5.0|8  |NaN|
|2     |NaN|6.0|9  |NaN|

`thresh` 参数提供了更细粒度的控制：您可以设置行或列需要保留的*非空值*数量：
```python
example2.dropna(axis='rows', thresh=3)
```
```
	0	1	2	3
1	2.0	5.0	8	NaN
```
这里，第一行和最后一行被删除，因为它们只有两个非空值。

- **填充空值**：根据您的数据集，有时用有效值填充空值比删除它们更合理。您可以使用 `isnull` 来就地填充，但这可能很繁琐，特别是当您有很多值需要填充时。由于这是数据科学中的常见任务，pandas 提供了 `fillna` 方法，它返回一个 `Series` 或 `DataFrame` 的副本，其中的缺失值被您选择的值替换。让我们创建另一个示例 `Series` 来看看实际效果。
```python
example3 = pd.Series([1, np.nan, 2, None, 3], index=list('abcde'))
example3
```
```
a    1.0
b    NaN
c    2.0
d    NaN
e    3.0
dtype: float64
```
您可以用单个值（例如 `0`）填充所有空值：
```python
example3.fillna(0)
```
```
a    1.0
b    0.0
c    2.0
d    0.0
e    3.0
dtype: float64
```
您可以**向前填充**空值，即使用最后一个有效值填充空值：
```python
example3.fillna(method='ffill')
```
```
a    1.0
b    1.0
c    2.0
d    2.0
e    3.0
dtype: float64
```
您还可以**向后填充**，即将下一个有效值向后传播以填充空值：
```python
example3.fillna(method='bfill')
```
```
a    1.0
b    2.0
c    2.0
d    3.0
e    3.0
dtype: float64
```
正如您可能猜到的，这对 `DataFrame` 同样适用，但您还可以指定沿哪个 `axis` 填充空值。再次使用之前的 `example2`：
```python
example2.fillna(method='ffill', axis=1)
```
```
	0	1	2	3
0	1.0	1.0	7.0	7.0
1	2.0	5.0	8.0	8.0
2	NaN	6.0	9.0	9.0
```
注意，当没有前一个值可用于向前填充时，空值仍然保留。
> **要点总结：** 处理数据集中缺失值的方法有很多。具体采用哪种策略（删除、替换，甚至如何替换）应根据数据的具体情况决定。随着你处理和分析更多的数据集，你会逐渐培养出更好的应对缺失值的能力。

## 删除重复数据

> **学习目标：** 在本小节结束时，你应该能够熟练地识别并删除 DataFrame 中的重复值。

除了缺失数据外，你还会经常在实际数据集中遇到重复数据。幸运的是，`pandas` 提供了一种简单的方法来检测和删除重复条目。

- **识别重复值：`duplicated`**：你可以使用 pandas 的 `duplicated` 方法轻松找到重复值。该方法返回一个布尔掩码，指示 `DataFrame` 中某条记录是否是之前记录的重复项。让我们创建另一个示例 `DataFrame` 来实际操作一下。
```python
example4 = pd.DataFrame({'letters': ['A','B'] * 2 + ['B'],
                         'numbers': [1, 2, 1, 3, 3]})
example4
```
|      |letters|numbers|
|------|-------|-------|
|0     |A      |1      |
|1     |B      |2      |
|2     |A      |1      |
|3     |B      |3      |
|4     |B      |3      |

```python
example4.duplicated()
```
```
0    False
1    False
2     True
3    False
4     True
dtype: bool
```
- **删除重复值：`drop_duplicates`**：该方法返回一个副本，其中所有 `duplicated` 值为 `False` 的数据被保留：
```python
example4.drop_duplicates()
```
```
	letters	numbers
0	A	1
1	B	2
3	B	3
```
`duplicated` 和 `drop_duplicates` 默认会考虑所有列，但你可以指定它们只检查 `DataFrame` 中的某些列：
```python
example4.drop_duplicates(['letters'])
```
```
letters	numbers
0	A	1
1	B	2
```

> **要点总结：** 删除重复数据是几乎每个数据科学项目中的重要步骤。重复数据可能会改变分析结果，导致不准确的结论！


## 🚀 挑战

所有讨论的内容都可以在 [Jupyter Notebook](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/2-Working-With-Data/08-data-preparation/notebook.ipynb) 中找到。此外，每节课后还有练习题，试着完成它们吧！

## [课后测验](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/15)



## 复习与自学

准备数据进行分析和建模的方法有很多，而清洗数据是一个需要“亲自动手”的重要步骤。试试 Kaggle 上的这些挑战，探索本课未涉及的技术。

- [数据清洗挑战：解析日期](https://www.kaggle.com/rtatman/data-cleaning-challenge-parsing-dates/)

- [数据清洗挑战：数据缩放与归一化](https://www.kaggle.com/rtatman/data-cleaning-challenge-scale-and-normalize-data)


## 作业

[评估表单中的数据](assignment.md)

**免责声明**：  
本文档使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用此翻译而产生的任何误解或误读不承担责任。