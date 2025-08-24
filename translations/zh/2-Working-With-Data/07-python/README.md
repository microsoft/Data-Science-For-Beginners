<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "116c5d361fbe812e59a73f37ce721d36",
  "translation_date": "2025-08-24T12:08:41+00:00",
  "source_file": "2-Working-With-Data/07-python/README.md",
  "language_code": "zh"
}
-->
# 使用数据：Python 和 Pandas 库

| ![ 由 [(@sketchthedocs)](https://sketchthedocs.dev) 绘制的速记图 ](../../sketchnotes/07-WorkWithPython.png) |
| :-------------------------------------------------------------------------------------------------------: |
|                 使用 Python - _由 [@nitya](https://twitter.com/nitya) 绘制的速记图_                        |

[![介绍视频](../../../../2-Working-With-Data/07-python/images/video-ds-python.png)](https://youtu.be/dZjWOGbsN4Y)

尽管数据库提供了非常高效的方式来存储数据并通过查询语言进行查询，但最灵活的数据处理方式是编写自己的程序来操作数据。在许多情况下，使用数据库查询可能更有效。然而，当需要更复杂的数据处理时，SQL 可能无法轻松实现。  
数据处理可以用任何编程语言编写，但某些语言在处理数据方面更高级。数据科学家通常偏好以下语言之一：

* **[Python](https://www.python.org/)** 是一种通用编程语言，因其简单性常被认为是初学者的最佳选择之一。Python 拥有许多额外的库，可以帮助解决许多实际问题，例如从 ZIP 压缩包中提取数据，或将图片转换为灰度图像。除了数据科学，Python 还常用于 Web 开发。
* **[R](https://www.r-project.org/)** 是一个为统计数据处理而开发的传统工具箱。它包含大量的库资源（CRAN），使其成为数据处理的良好选择。然而，R 不是通用编程语言，很少在数据科学领域之外使用。
* **[Julia](https://julialang.org/)** 是另一种专为数据科学开发的语言。它旨在提供比 Python 更好的性能，是科学实验的强大工具。

在本课程中，我们将专注于使用 Python 进行简单的数据处理。我们假设您对该语言已有基本了解。如果您想深入学习 Python，可以参考以下资源之一：

* [通过 Turtle Graphics 和分形趣味学习 Python](https://github.com/shwars/pycourse) - 基于 GitHub 的 Python 编程快速入门课程
* [迈出 Python 的第一步](https://docs.microsoft.com/en-us/learn/paths/python-first-steps/?WT.mc_id=academic-77958-bethanycheum) - [Microsoft Learn](http://learn.microsoft.com/?WT.mc_id=academic-77958-bethanycheum) 上的学习路径

数据可以有多种形式。在本课程中，我们将讨论三种数据形式：**表格数据**、**文本**和**图像**。

我们将专注于一些数据处理的示例，而不是全面介绍所有相关库。这将帮助您了解主要概念，并在需要时知道在哪里找到解决问题的方法。

> **最有用的建议**：当您需要对数据执行某些操作但不知道如何实现时，尝试在互联网上搜索。[Stackoverflow](https://stackoverflow.com/) 通常包含许多关于 Python 的有用代码示例，适用于许多典型任务。

## [课前测验](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/12)

## 表格数据和数据框

当我们讨论关系型数据库时，您已经接触过表格数据。当您有大量数据，并且这些数据包含在许多不同的关联表中时，使用 SQL 来处理它们是非常有意义的。然而，在许多情况下，我们只有一个数据表，并且需要对这些数据获得一些**理解**或**洞察**，例如分布情况、值之间的相关性等。在数据科学中，常常需要对原始数据进行一些转换，然后进行可视化。这两个步骤都可以通过 Python 轻松完成。

Python 中有两个最有用的库可以帮助您处理表格数据：
* **[Pandas](https://pandas.pydata.org/)** 允许您操作所谓的 **DataFrame**，它类似于关系型表格。您可以拥有命名的列，并对行、列和整个 DataFrame 执行各种操作。
* **[Numpy](https://numpy.org/)** 是一个用于处理 **张量**（即多维**数组**）的库。数组的值具有相同的底层类型，比 DataFrame 更简单，但提供了更多数学操作，并且开销更小。

此外，还有一些其他值得了解的库：
* **[Matplotlib](https://matplotlib.org/)** 是一个用于数据可视化和绘制图表的库
* **[SciPy](https://www.scipy.org/)** 是一个包含一些额外科学函数的库。我们在讨论概率和统计时已经接触过这个库

以下是您通常在 Python 程序开头导入这些库的代码：
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import ... # you need to specify exact sub-packages that you need
``` 

Pandas 围绕几个基本概念构建。

### Series

**Series** 是一组值的序列，类似于列表或 numpy 数组。主要区别在于 Series 还具有一个 **索引**，当我们对 Series 进行操作（例如相加）时，会考虑索引。索引可以是简单的整数行号（从列表或数组创建 Series 时默认使用的索引），也可以是复杂的结构，例如日期区间。

> **注意**：在配套的笔记本文件 [`notebook.ipynb`](../../../../2-Working-With-Data/07-python/notebook.ipynb) 中有一些 Pandas 的入门代码。这里仅列出部分示例，您可以查看完整的笔记本文件。

举个例子：我们想分析冰淇淋店的销售情况。让我们生成一段时间内的销售数据（每天售出的商品数量）：
```python
start_date = "Jan 1, 2020"
end_date = "Mar 31, 2020"
idx = pd.date_range(start_date,end_date)
print(f"Length of index is {len(idx)}")
items_sold = pd.Series(np.random.randint(25,50,size=len(idx)),index=idx)
items_sold.plot()
```
![时间序列图](../../../../2-Working-With-Data/07-python/images/timeseries-1.png)

假设每周我们都会为朋友举办聚会，并额外带 10 盒冰淇淋。我们可以创建另一个以周为索引的 Series 来表示：
```python
additional_items = pd.Series(10,index=pd.date_range(start_date,end_date,freq="W"))
```
当我们将两个 Series 相加时，就得到了总数：
```python
total_items = items_sold.add(additional_items,fill_value=0)
total_items.plot()
```
![时间序列图](../../../../2-Working-With-Data/07-python/images/timeseries-2.png)

> **注意** 我们没有使用简单的语法 `total_items+additional_items`。如果这样做，结果 Series 中会有许多 `NaN`（*非数字*）值。这是因为在 `additional_items` Series 的某些索引点上缺少值，而将 `NaN` 加到任何值都会得到 `NaN`。因此，我们需要在相加时指定 `fill_value` 参数。

对于时间序列，我们还可以使用不同的时间间隔对其进行**重采样**。例如，假设我们想计算每月的平均销售量，可以使用以下代码：
```python
monthly = total_items.resample("1M").mean()
ax = monthly.plot(kind='bar')
```
![每月时间序列平均值](../../../../2-Working-With-Data/07-python/images/timeseries-3.png)

### DataFrame

DataFrame 本质上是具有相同索引的多个 Series 的集合。我们可以将多个 Series 组合成一个 DataFrame：
```python
a = pd.Series(range(1,10))
b = pd.Series(["I","like","to","play","games","and","will","not","change"],index=range(0,9))
df = pd.DataFrame([a,b])
```
这将创建如下的水平表格：
|     | 0   | 1    | 2   | 3   | 4      | 5   | 6      | 7    | 8    |
| --- | --- | ---- | --- | --- | ------ | --- | ------ | ---- | ---- |
| 0   | 1   | 2    | 3   | 4   | 5      | 6   | 7      | 8    | 9    |
| 1   | I   | like | to  | use | Python | and | Pandas | very | much |

我们还可以将 Series 用作列，并通过字典指定列名：
```python
df = pd.DataFrame({ 'A' : a, 'B' : b })
```
这将生成如下表格：

|     | A   | B      |
| --- | --- | ------ |
| 0   | 1   | I      |
| 1   | 2   | like   |
| 2   | 3   | to     |
| 3   | 4   | use    |
| 4   | 5   | Python |
| 5   | 6   | and    |
| 6   | 7   | Pandas |
| 7   | 8   | very   |
| 8   | 9   | much   |

**注意** 我们还可以通过转置前一个表格来获得这种表格布局，例如：
```python
df = pd.DataFrame([a,b]).T..rename(columns={ 0 : 'A', 1 : 'B' })
```
这里 `.T` 表示对 DataFrame 进行转置操作，即交换行和列，而 `rename` 操作允许我们重命名列以匹配前面的示例。

以下是我们可以对 DataFrame 执行的一些最重要的操作：

**列选择**。我们可以通过 `df['A']` 选择单个列——此操作返回一个 Series。我们还可以通过 `df[['B','A']]` 选择列的子集到另一个 DataFrame 中——此操作返回另一个 DataFrame。

**按条件过滤行**。例如，要仅保留列 `A` 大于 5 的行，可以写 `df[df['A']>5]`。

> **注意**：过滤的工作原理如下。表达式 `df['A']<5` 返回一个布尔 Series，指示原始 Series `df['A']` 中每个元素的表达式是 `True` 还是 `False`。当布尔 Series 用作索引时，它返回 DataFrame 中的行子集。因此，不能使用任意的 Python 布尔表达式，例如，写 `df[df['A']>5 and df['A']<7]` 是错误的。相反，您应该对布尔 Series 使用特殊的 `&` 操作，写作 `df[(df['A']>5) & (df['A']<7)]`（*括号在这里很重要*）。

**创建新的可计算列**。我们可以通过直观的表达式轻松为 DataFrame 创建新的可计算列：
```python
df['DivA'] = df['A']-df['A'].mean() 
``` 
此示例计算列 A 偏离其平均值的差异。实际发生的情况是我们计算了一个 Series，然后将其分配给左侧，创建了另一个列。因此，我们不能使用与 Series 不兼容的任何操作，例如，以下代码是错误的：
```python
# Wrong code -> df['ADescr'] = "Low" if df['A'] < 5 else "Hi"
df['LenB'] = len(df['B']) # <- Wrong result
``` 
后一个示例虽然语法正确，但会给出错误的结果，因为它将 Series `B` 的长度分配给列中的所有值，而不是我们预期的每个元素的长度。

如果我们需要计算这样的复杂表达式，可以使用 `apply` 函数。最后一个示例可以写成如下：
```python
df['LenB'] = df['B'].apply(lambda x : len(x))
# or 
df['LenB'] = df['B'].apply(len)
```

经过上述操作后，我们将得到以下 DataFrame：

|     | A   | B      | DivA | LenB |
| --- | --- | ------ | ---- | ---- |
| 0   | 1   | I      | -4.0 | 1    |
| 1   | 2   | like   | -3.0 | 4    |
| 2   | 3   | to     | -2.0 | 2    |
| 3   | 4   | use    | -1.0 | 3    |
| 4   | 5   | Python | 0.0  | 6    |
| 5   | 6   | and    | 1.0  | 3    |
| 6   | 7   | Pandas | 2.0  | 6    |
| 7   | 8   | very   | 3.0  | 4    |
| 8   | 9   | much   | 4.0  | 4    |

**基于行号选择行** 可以使用 `iloc` 构造。例如，要选择 DataFrame 的前 5 行：
```python
df.iloc[:5]
```

**分组** 通常用于获得类似于 Excel 中 *数据透视表* 的结果。例如，假设我们想计算列 `A` 的平均值，按 `LenB` 的不同值分组。我们可以按 `LenB` 对 DataFrame 进行分组，然后调用 `mean`：
```python
df.groupby(by='LenB').mean()
```
如果我们需要计算平均值和组中元素的数量，则可以使用更复杂的 `aggregate` 函数：
```python
df.groupby(by='LenB') \
 .aggregate({ 'DivA' : len, 'A' : lambda x: x.mean() }) \
 .rename(columns={ 'DivA' : 'Count', 'A' : 'Mean'})
```
这将生成以下表格：

| LenB | Count | Mean     |
| ---- | ----- | -------- |
| 1    | 1     | 1.000000 |
| 2    | 1     | 3.000000 |
| 3    | 2     | 5.000000 |
| 4    | 3     | 6.333333 |
| 6    | 2     | 6.000000 |

### 获取数据
我们已经看到如何轻松地从 Python 对象构建 Series 和 DataFrame。然而，数据通常以文本文件或 Excel 表格的形式存在。幸运的是，Pandas 为我们提供了一种简单的方法来从磁盘加载数据。例如，读取 CSV 文件就像这样简单：
```python
df = pd.read_csv('file.csv')
```
我们将在“挑战”部分中看到更多加载数据的示例，包括从外部网站获取数据。

### 打印和绘图

数据科学家经常需要探索数据，因此能够可视化数据非常重要。当 DataFrame 很大时，我们通常只需要打印出前几行以确保操作正确。这可以通过调用 `df.head()` 来完成。如果你在 Jupyter Notebook 中运行，它会以漂亮的表格形式打印出 DataFrame。

我们还见过使用 `plot` 函数来可视化某些列。虽然 `plot` 对许多任务非常有用，并且通过 `kind=` 参数支持多种不同的图表类型，但你也可以使用原始的 `matplotlib` 库来绘制更复杂的图表。我们将在单独的课程中详细讲解数据可视化。

这个概述涵盖了 Pandas 的重要概念，但这个库非常丰富，你可以用它做无限多的事情！现在让我们应用这些知识来解决具体问题。

## 🚀 挑战 1：分析 COVID 传播

我们将关注的第一个问题是 COVID-19 的疫情传播建模。为此，我们将使用由 [约翰霍普金斯大学](https://jhu.edu/) 的 [系统科学与工程中心](https://systems.jhu.edu/) (CSSE) 提供的不同国家感染人数数据。数据集可以在 [这个 GitHub 仓库](https://github.com/CSSEGISandData/COVID-19) 中找到。

由于我们想展示如何处理数据，我们邀请你打开 [`notebook-covidspread.ipynb`](../../../../2-Working-With-Data/07-python/notebook-covidspread.ipynb) 并从头到尾阅读。你还可以执行单元格，并完成我们在最后为你留下的一些挑战。

![COVID 传播](../../../../2-Working-With-Data/07-python/images/covidspread.png)

> 如果你不知道如何在 Jupyter Notebook 中运行代码，可以查看 [这篇文章](https://soshnikov.com/education/how-to-execute-notebooks-from-github/)。

## 处理非结构化数据

虽然数据通常以表格形式出现，但在某些情况下我们需要处理较少结构化的数据，例如文本或图像。在这种情况下，为了应用我们上面看到的数据处理技术，我们需要以某种方式**提取**结构化数据。以下是一些示例：

* 从文本中提取关键词，并查看这些关键词出现的频率
* 使用神经网络从图片中提取有关对象的信息
* 获取视频摄像头画面中人物的情感信息

## 🚀 挑战 2：分析 COVID 论文

在这个挑战中，我们将继续关注 COVID 疫情的主题，重点处理关于该主题的科学论文。有一个 [CORD-19 数据集](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge)，其中包含超过 7000 篇（撰写时）关于 COVID 的论文，提供了元数据和摘要（其中约一半还提供了全文）。

使用 [Text Analytics for Health](https://docs.microsoft.com/azure/cognitive-services/text-analytics/how-tos/text-analytics-for-health/?WT.mc_id=academic-77958-bethanycheum) 认知服务分析该数据集的完整示例已在 [这篇博客文章](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/) 中描述。我们将讨论此分析的简化版本。

> **NOTE**: 我们没有在此仓库中提供数据集副本。你可能需要先从 [Kaggle 上的这个数据集](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge?select=metadata.csv) 下载 [`metadata.csv`](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge?select=metadata.csv) 文件。可能需要注册 Kaggle。你也可以从 [这里](https://ai2-semanticscholar-cord-19.s3-us-west-2.amazonaws.com/historical_releases.html) 下载数据集，无需注册，但它将包括所有全文以及元数据文件。

打开 [`notebook-papers.ipynb`](../../../../2-Working-With-Data/07-python/notebook-papers.ipynb) 并从头到尾阅读。你还可以执行单元格，并完成我们在最后为你留下的一些挑战。

![COVID 医疗处理](../../../../2-Working-With-Data/07-python/images/covidtreat.png)

## 处理图像数据

最近，开发了非常强大的 AI 模型，可以帮助我们理解图像。通过预训练的神经网络或云服务，可以解决许多任务。以下是一些示例：

* **图像分类**，可以帮助你将图像分类到预定义的类别中。你可以使用诸如 [Custom Vision](https://azure.microsoft.com/services/cognitive-services/custom-vision-service/?WT.mc_id=academic-77958-bethanycheum) 的服务轻松训练自己的图像分类器。
* **对象检测**，用于检测图像中的不同对象。诸如 [计算机视觉](https://azure.microsoft.com/services/cognitive-services/computer-vision/?WT.mc_id=academic-77958-bethanycheum) 的服务可以检测许多常见对象，你也可以训练 [Custom Vision](https://azure.microsoft.com/services/cognitive-services/custom-vision-service/?WT.mc_id=academic-77958-bethanycheum) 模型来检测一些特定的兴趣对象。
* **人脸检测**，包括年龄、性别和情感检测。这可以通过 [Face API](https://azure.microsoft.com/services/cognitive-services/face/?WT.mc_id=academic-77958-bethanycheum) 来完成。

所有这些云服务都可以通过 [Python SDKs](https://docs.microsoft.com/samples/azure-samples/cognitive-services-python-sdk-samples/cognitive-services-python-sdk-samples/?WT.mc_id=academic-77958-bethanycheum) 调用，因此可以轻松地集成到你的数据探索工作流中。

以下是一些从图像数据源探索数据的示例：
* 在博客文章 [如何在不编程的情况下学习数据科学](https://soshnikov.com/azure/how-to-learn-data-science-without-coding/) 中，我们探索 Instagram 照片，试图了解是什么让人们对一张照片点赞更多。我们首先使用 [计算机视觉](https://azure.microsoft.com/services/cognitive-services/computer-vision/?WT.mc_id=academic-77958-bethanycheum) 从图片中提取尽可能多的信息，然后使用 [Azure Machine Learning AutoML](https://docs.microsoft.com/azure/machine-learning/concept-automated-ml/?WT.mc_id=academic-77958-bethanycheum) 构建可解释的模型。
* 在 [面部研究工作坊](https://github.com/CloudAdvocacy/FaceStudies) 中，我们使用 [Face API](https://azure.microsoft.com/services/cognitive-services/face/?WT.mc_id=academic-77958-bethanycheum) 提取活动照片中人物的情感，以试图了解是什么让人们感到快乐。

## 结论

无论你已经拥有结构化数据还是非结构化数据，使用 Python 都可以完成与数据处理和理解相关的所有步骤。这可能是数据处理最灵活的方式，这也是为什么大多数数据科学家将 Python 作为主要工具的原因。如果你认真对待自己的数据科学之旅，深入学习 Python 可能是一个好主意！

## [课后测验](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/13)

## 复习与自学

**书籍**
* [Wes McKinney. Python for Data Analysis: Data Wrangling with Pandas, NumPy, and IPython](https://www.amazon.com/gp/product/1491957662)

**在线资源**
* 官方 [10 分钟 Pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html) 教程
* [Pandas 可视化文档](https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html)

**学习 Python**
* [通过 Turtle Graphics 和分形以有趣的方式学习 Python](https://github.com/shwars/pycourse)
* [通过 Microsoft Learn 学习路径](https://docs.microsoft.com/learn/paths/python-first-steps/?WT.mc_id=academic-77958-bethanycheum) [迈出 Python 的第一步](http://learn.microsoft.com/?WT.mc_id=academic-77958-bethanycheum)

## 作业

[对上述挑战进行更详细的数据研究](assignment.md)

## 致谢

本课程由 [Dmitry Soshnikov](http://soshnikov.com) ❤️ 创作。

**免责声明**：  
本文档使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于关键信息，建议使用专业人工翻译。我们对因使用此翻译而产生的任何误解或误读不承担责任。