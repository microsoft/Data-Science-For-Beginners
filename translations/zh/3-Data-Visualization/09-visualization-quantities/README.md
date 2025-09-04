<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "69b32b6789a91f796ebc7a02f5575e03",
  "translation_date": "2025-09-04T12:22:36+00:00",
  "source_file": "3-Data-Visualization/09-visualization-quantities/README.md",
  "language_code": "zh"
}
-->
# 可视化数量

|![由 [(@sketchthedocs)](https://sketchthedocs.dev) 绘制的草图笔记](../../sketchnotes/09-Visualizing-Quantities.png)|
|:---:|
| 可视化数量 - _草图笔记由 [@nitya](https://twitter.com/nitya) 绘制_ |

在本课中，你将学习如何使用众多可用的 Python 库之一，围绕数量的概念创建有趣的可视化。通过一个关于明尼苏达州鸟类的清理数据集，你可以了解许多关于当地野生动物的有趣事实。

## [课前测验](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/16)

## 使用 Matplotlib 观察翼展

[Matplotlib](https://matplotlib.org/stable/index.html) 是一个非常优秀的库，可以用来创建各种简单或复杂的图表和图形。一般来说，使用这些库绘制数据的过程包括：确定数据框中你想要处理的部分，对数据进行必要的转换，分配 x 和 y 轴的值，决定展示哪种图表，然后显示图表。Matplotlib 提供了多种可视化方式，但在本课中，我们将重点关注最适合可视化数量的图表：折线图、散点图和柱状图。

> ✅ 根据数据的结构和你想讲述的故事选择最合适的图表。
> - 分析时间趋势：折线图
> - 比较数值：柱状图、条形图、饼图、散点图
> - 展示部分与整体的关系：饼图
> - 展示数据分布：散点图、柱状图
> - 展示趋势：折线图、条形图
> - 展示数值之间的关系：折线图、散点图、气泡图

如果你有一个数据集并需要了解某个特定项目的数量，第一步通常是检查其数值。

✅ 这里有一些非常好的 Matplotlib [速查表](https://matplotlib.org/cheatsheets/cheatsheets.pdf)。

## 绘制关于鸟类翼展值的折线图

打开本课文件夹根目录下的 `notebook.ipynb` 文件并添加一个单元格。

> 注意：数据存储在本仓库根目录的 `/data` 文件夹中。

```python
import pandas as pd
import matplotlib.pyplot as plt
birds = pd.read_csv('../../data/birds.csv')
birds.head()
```

这些数据是文本和数字的混合：

|      | 名称                          | 学名                   | 类别                  | 目           | 科       | 属          | 保护状态           | 最小长度 | 最大长度 | 最小体重   | 最大体重   | 最小翼展   | 最大翼展   |
| ---: | :--------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :----------------- | --------: | --------: | ----------: | ----------: | ----------: | ----------: |
|    0 | 黑腹树鸭                     | Dendrocygna autumnalis | 鸭类/鹅类/水禽        | 雁形目       | 鸭科     | 树鸭属       | LC                 |        47 |        56 |         652 |        1020 |          76 |          94 |
|    1 | 棕树鸭                       | Dendrocygna bicolor    | 鸭类/鹅类/水禽        | 雁形目       | 鸭科     | 树鸭属       | LC                 |        45 |        53 |         712 |        1050 |          85 |          93 |
|    2 | 雪鹅                         | Anser caerulescens     | 鸭类/鹅类/水禽        | 雁形目       | 鸭科     | 鹅属         | LC                 |        64 |        79 |        2050 |        4050 |         135 |         165 |
|    3 | 罗斯鹅                       | Anser rossii           | 鸭类/鹅类/水禽        | 雁形目       | 鸭科     | 鹅属         | LC                 |      57.3 |        64 |        1066 |        1567 |         113 |         116 |
|    4 | 大白额雁                     | Anser albifrons        | 鸭类/鹅类/水禽        | 雁形目       | 鸭科     | 鹅属         | LC                 |        64 |        81 |        1930 |        3310 |         130 |         165 |

让我们从使用基本折线图绘制一些数值数据开始。假设你想查看这些有趣鸟类的最大翼展。

```python
wingspan = birds['MaxWingspan'] 
wingspan.plot()
```

![最大翼展](../../../../translated_images/max-wingspan-02.e79fd847b2640b89e21e340a3a9f4c5d4b224c4fcd65f54385e84f1c9ed26d52.zh.png)

你立刻注意到了什么？似乎至少有一个异常值——这翼展也太大了吧！2300 厘米的翼展相当于 23 米——难道明尼苏达州有翼龙在飞翔？让我们调查一下。

虽然你可以在 Excel 中快速排序找到这些可能是输入错误的异常值，但继续通过图表进行可视化处理。

为 x 轴添加标签以显示涉及的鸟类种类：

```
plt.title('Max Wingspan in Centimeters')
plt.ylabel('Wingspan (CM)')
plt.xlabel('Birds')
plt.xticks(rotation=45)
x = birds['Name'] 
y = birds['MaxWingspan']

plt.plot(x, y)

plt.show()
```

![带标签的翼展](../../../../translated_images/max-wingspan-labels-02.aa90e826ca49a9d1dde78075e9755c1849ef56a4e9ec60f7e9f3806daf9283e2.zh.png)

即使将标签旋转 45 度，仍然太多了，无法阅读。让我们尝试另一种策略：仅标记那些异常值，并将标签设置在图表内。你可以使用散点图来为标签腾出更多空间：

```python
plt.title('Max Wingspan in Centimeters')
plt.ylabel('Wingspan (CM)')
plt.tick_params(axis='both',which='both',labelbottom=False,bottom=False)

for i in range(len(birds)):
    x = birds['Name'][i]
    y = birds['MaxWingspan'][i]
    plt.plot(x, y, 'bo')
    if birds['MaxWingspan'][i] > 500:
        plt.text(x, y * (1 - 0.05), birds['Name'][i], fontsize=12)
    
plt.show()
```

这里发生了什么？你使用了 `tick_params` 隐藏了底部标签，然后对鸟类数据集进行了循环。通过使用 `bo` 绘制小蓝点，你检查了是否有鸟类的最大翼展超过 500，如果是，则在点旁边显示其标签。你稍微偏移了 y 轴上的标签位置（`y * (1 - 0.05)`），并使用鸟类名称作为标签。

你发现了什么？

![异常值](../../../../translated_images/labeled-wingspan-02.6110e2d2401cd5238ccc24dfb6d04a6c19436101f6cec151e3992e719f9f1e1f.zh.png)

## 筛选数据

尽管秃鹰和草原隼可能是非常大的鸟类，但它们的最大翼展似乎被错误标记，多加了一个 `0`。遇到翼展 25 米的秃鹰的可能性不大，但如果真的遇到了，请告诉我们！让我们创建一个新的数据框，去掉这两个异常值：

```python
plt.title('Max Wingspan in Centimeters')
plt.ylabel('Wingspan (CM)')
plt.xlabel('Birds')
plt.tick_params(axis='both',which='both',labelbottom=False,bottom=False)
for i in range(len(birds)):
    x = birds['Name'][i]
    y = birds['MaxWingspan'][i]
    if birds['Name'][i] not in ['Bald eagle', 'Prairie falcon']:
        plt.plot(x, y, 'bo')
plt.show()
```

通过筛选掉异常值，你的数据现在更加连贯且易于理解。

![翼展散点图](../../../../translated_images/scatterplot-wingspan-02.1c33790094ce36a75f5fb45b25ed2cf27f0356ea609e43c11e97a2cedd7011a4.zh.png)

现在我们至少在翼展方面有了一个更干净的数据集，让我们进一步了解这些鸟类。

虽然折线图和散点图可以显示数据值及其分布的信息，但我们想要思考这个数据集中固有的数值。你可以创建可视化来回答以下关于数量的问题：

> 有多少种鸟类类别？它们的数量是多少？
> 有多少鸟类是灭绝的、濒危的、稀有的或常见的？
> 根据林奈分类法，有多少种不同的属和目？

## 探索柱状图

当你需要展示数据分组时，柱状图非常实用。让我们探索这个数据集中存在的鸟类类别，看看哪种类别的数量最多。

在 notebook 文件中创建一个基本柱状图。

✅ 注意，你可以选择筛选掉我们在上一节中识别的两个异常鸟类，修正它们翼展的输入错误，或者将它们保留在这些不依赖翼展值的练习中。

如果你想创建一个柱状图，可以选择你想要关注的数据。柱状图可以从原始数据中创建：

```python
birds.plot(x='Category',
        kind='bar',
        stacked=True,
        title='Birds of Minnesota')

```

![完整数据柱状图](../../../../translated_images/full-data-bar-02.aaa3fda71c63ed564b917841a1886c177dd9a26424142e510c0c0498fd6ca160.zh.png)

然而，这个柱状图难以阅读，因为数据没有分组。你需要选择你想要绘制的数据，因此让我们根据鸟类的类别查看它们的数量。

筛选数据以仅包含鸟类的类别。

✅ 注意，你使用 Pandas 来管理数据，然后让 Matplotlib 进行绘图。

由于类别较多，你可以垂直显示此图表，并调整其高度以适应所有数据：

```python
category_count = birds.value_counts(birds['Category'].values, sort=True)
plt.rcParams['figure.figsize'] = [6, 12]
category_count.plot.barh()
```

![类别和数量](../../../../translated_images/category-counts-02.0b9a0a4de42275ae5096d0f8da590d8bf520d9e7e40aad5cc4fc8d276480cc32.zh.png)

这个柱状图很好地展示了每个类别中鸟类的数量。一眼就能看出，这个地区数量最多的鸟类是鸭类/鹅类/水禽。明尼苏达州是“万湖之地”，这并不令人意外！

✅ 尝试对这个数据集进行其他计数。有发现让你感到惊讶吗？

## 比较数据

你可以通过创建新轴尝试不同的分组数据比较。尝试比较基于类别的鸟类最大长度：

```python
maxlength = birds['MaxLength']
plt.barh(y=birds['Category'], width=maxlength)
plt.rcParams['figure.figsize'] = [6, 12]
plt.show()
```

![比较数据](../../../../translated_images/category-length-02.7304bf519375c9807d8165cc7ec60dd2a60f7b365b23098538e287d89adb7d76.zh.png)

这里没有什么令人惊讶的：与鹈鹕或鹅相比，蜂鸟的最大长度最小。当数据符合逻辑时，这是一件好事！

你可以通过叠加数据创建更有趣的柱状图可视化。让我们叠加最小长度和最大长度在给定鸟类类别上的数据：

```python
minLength = birds['MinLength']
maxLength = birds['MaxLength']
category = birds['Category']

plt.barh(category, maxLength)
plt.barh(category, minLength)

plt.show()
```

在这个图表中，你可以看到每个鸟类类别的最小长度和最大长度范围。你可以有把握地说，根据这些数据，鸟越大，其长度范围越大。真是令人着迷！

![叠加值](../../../../translated_images/superimposed-02.f03058536baeb2ed7864f01102538464d4c2fd7ade881ddd7d5ba74dc5d2fdae.zh.png)

## 🚀 挑战

这个鸟类数据集提供了关于特定生态系统中不同类型鸟类的大量信息。在网上搜索，看看你是否能找到其他与鸟类相关的数据集。练习围绕这些鸟类构建图表和图形，发现你之前未曾意识到的事实。

## [课后测验](https://ff-quizzes.netlify.app/en/ds/)

## 复习与自学

本课的第一部分为你提供了一些关于如何使用 Matplotlib 可视化数量的信息。研究其他可视化数据集的方法。[Plotly](https://github.com/plotly/plotly.py) 是我们不会在这些课程中涵盖的一个工具，所以看看它能提供什么。

## 作业

[折线图、散点图和柱状图](assignment.md)

---

**免责声明**：  
本文档使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。尽管我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原始语言的文档作为权威来源。对于关键信息，建议使用专业人工翻译。因使用本翻译而导致的任何误解或误读，我们概不负责。