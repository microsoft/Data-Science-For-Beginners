<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "87faccac113d772551486a67a607153e",
  "translation_date": "2025-08-24T13:36:33+00:00",
  "source_file": "3-Data-Visualization/10-visualization-distributions/README.md",
  "language_code": "zh"
}
-->
# 可视化分布

|![ 由 [(@sketchthedocs)](https://sketchthedocs.dev) 绘制的速记图 ](../../sketchnotes/10-Visualizing-Distributions.png)|
|:---:|
| 可视化分布 - _由 [@nitya](https://twitter.com/nitya) 绘制的速记图_ |

在上一课中，你学习了关于明尼苏达州鸟类数据集的一些有趣事实。通过可视化异常值，你发现了一些错误数据，并通过最大长度观察了鸟类类别之间的差异。

## [课前测验](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/18)
## 探索鸟类数据集

另一种深入了解数据的方法是查看其分布，即数据如何沿某个轴组织。例如，你可能想了解这个数据集中鸟类的最大翼展或最大体重的一般分布。

让我们发现一些关于此数据集中数据分布的事实。在本课文件夹根目录的 _notebook.ipynb_ 文件中，导入 Pandas、Matplotlib 和你的数据：

```python
import pandas as pd
import matplotlib.pyplot as plt
birds = pd.read_csv('../../data/birds.csv')
birds.head()
```

|      | 名称                          | 学名                   | 类别                  | 目           | 科       | 属          | 保护状态         | 最小长度 | 最大长度 | 最小体重   | 最大体重   | 最小翼展   | 最大翼展   |
| ---: | :--------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :----------------- | --------: | --------: | ----------: | ----------: | ----------: | ----------: |
|    0 | 黑腹树鸭                     | Dendrocygna autumnalis | 鸭/鹅/水禽            | 雁形目       | 鸭科     | 树鸭属       | LC                 |        47 |        56 |         652 |        1020 |          76 |          94 |
|    1 | 棕树鸭                       | Dendrocygna bicolor    | 鸭/鹅/水禽            | 雁形目       | 鸭科     | 树鸭属       | LC                 |        45 |        53 |         712 |        1050 |          85 |          93 |
|    2 | 雪雁                         | Anser caerulescens     | 鸭/鹅/水禽            | 雁形目       | 鸭科     | 雁属         | LC                 |        64 |        79 |        2050 |        4050 |         135 |         165 |
|    3 | 小白额雁                     | Anser rossii           | 鸭/鹅/水禽            | 雁形目       | 鸭科     | 雁属         | LC                 |      57.3 |        64 |        1066 |        1567 |         113 |         116 |
|    4 | 大白额雁                     | Anser albifrons        | 鸭/鹅/水禽            | 雁形目       | 鸭科     | 雁属         | LC                 |        64 |        81 |        1930 |        3310 |         130 |         165 |

通常，你可以通过使用散点图快速查看数据的分布方式，就像我们在上一课中所做的那样：

```python
birds.plot(kind='scatter',x='MaxLength',y='Order',figsize=(12,8))

plt.title('Max Length per Order')
plt.ylabel('Order')
plt.xlabel('Max Length')

plt.show()
```
![每个目最大长度](../../../../3-Data-Visualization/10-visualization-distributions/images/scatter-wb.png)

这提供了每个鸟类目体长分布的一般概览，但这并不是显示真实分布的最佳方式。通常通过创建直方图来完成这一任务。

## 使用直方图

Matplotlib 提供了非常好的方法来使用直方图可视化数据分布。这种类型的图表类似于条形图，通过条形的升降可以看到分布情况。要构建直方图，你需要数值数据。要构建直方图，可以绘制一种类型为 'hist' 的图表。此图表显示了整个数据集中 MaxBodyMass 的分布。通过将数据数组划分为更小的区间（bins），它可以显示数据值的分布：

```python
birds['MaxBodyMass'].plot(kind = 'hist', bins = 10, figsize = (12,12))
plt.show()
```
![整个数据集的分布](../../../../3-Data-Visualization/10-visualization-distributions/images/dist1-wb.png)

如你所见，这个数据集中大多数 400 多种鸟类的最大体重都在 2000 以下。通过将 `bins` 参数更改为更高的值（例如 30），可以获得更多数据洞察：

```python
birds['MaxBodyMass'].plot(kind = 'hist', bins = 30, figsize = (12,12))
plt.show()
```
![更大 bins 参数的分布](../../../../3-Data-Visualization/10-visualization-distributions/images/dist2-wb.png)

此图表以更细致的方式显示了分布。通过仅选择给定范围内的数据，可以创建一个不那么偏向左侧的图表：

过滤数据，仅获取体重低于 60 的鸟类，并显示 40 个 `bins`：

```python
filteredBirds = birds[(birds['MaxBodyMass'] > 1) & (birds['MaxBodyMass'] < 60)]      
filteredBirds['MaxBodyMass'].plot(kind = 'hist',bins = 40,figsize = (12,12))
plt.show()     
```
![过滤后的直方图](../../../../3-Data-Visualization/10-visualization-distributions/images/dist3-wb.png)

✅ 尝试其他过滤器和数据点。要查看数据的完整分布，请移除 `['MaxBodyMass']` 过滤器以显示带标签的分布。

直方图还提供了一些不错的颜色和标签增强功能可以尝试：

创建一个二维直方图来比较两个分布之间的关系。让我们比较 `MaxBodyMass` 和 `MaxLength`。Matplotlib 提供了一种内置方法，通过更亮的颜色显示收敛：

```python
x = filteredBirds['MaxBodyMass']
y = filteredBirds['MaxLength']

fig, ax = plt.subplots(tight_layout=True)
hist = ax.hist2d(x, y)
```
可以看到，这两个元素沿预期轴存在预期的相关性，并且有一个特别强的收敛点：

![二维图](../../../../3-Data-Visualization/10-visualization-distributions/images/2D-wb.png)

直方图默认适用于数值数据。如果你需要根据文本数据查看分布，该怎么办？

## 使用文本数据探索数据集的分布

此数据集还包括关于鸟类类别、属、种、科以及保护状态的有用信息。让我们深入了解这些保护信息。根据保护状态，鸟类的分布是什么样的？

> ✅ 在数据集中，使用了一些缩写来描述保护状态。这些缩写来自 [IUCN 红色名录分类](https://www.iucnredlist.org/)，这是一个记录物种状态的组织。
> 
> - CR: 极危
> - EN: 濒危
> - EX: 灭绝
> - LC: 无危
> - NT: 近危
> - VU: 易危

这些是基于文本的值，因此你需要进行转换以创建直方图。使用 filteredBirds 数据框，显示其保护状态及其最小翼展。你看到了什么？

```python
x1 = filteredBirds.loc[filteredBirds.ConservationStatus=='EX', 'MinWingspan']
x2 = filteredBirds.loc[filteredBirds.ConservationStatus=='CR', 'MinWingspan']
x3 = filteredBirds.loc[filteredBirds.ConservationStatus=='EN', 'MinWingspan']
x4 = filteredBirds.loc[filteredBirds.ConservationStatus=='NT', 'MinWingspan']
x5 = filteredBirds.loc[filteredBirds.ConservationStatus=='VU', 'MinWingspan']
x6 = filteredBirds.loc[filteredBirds.ConservationStatus=='LC', 'MinWingspan']

kwargs = dict(alpha=0.5, bins=20)

plt.hist(x1, **kwargs, color='red', label='Extinct')
plt.hist(x2, **kwargs, color='orange', label='Critically Endangered')
plt.hist(x3, **kwargs, color='yellow', label='Endangered')
plt.hist(x4, **kwargs, color='green', label='Near Threatened')
plt.hist(x5, **kwargs, color='blue', label='Vulnerable')
plt.hist(x6, **kwargs, color='gray', label='Least Concern')

plt.gca().set(title='Conservation Status', ylabel='Min Wingspan')
plt.legend();
```

![翼展和保护状态的对比](../../../../3-Data-Visualization/10-visualization-distributions/images/histogram-conservation-wb.png)

最小翼展和保护状态之间似乎没有明显的相关性。使用此方法测试数据集的其他元素。你也可以尝试不同的过滤器。你发现了任何相关性吗？

## 密度图

你可能已经注意到，我们目前看到的直方图是“阶梯状”的，并没有平滑地呈现弧线。要显示更平滑的密度图，可以尝试密度图。

要使用密度图，请熟悉一个新的绘图库 [Seaborn](https://seaborn.pydata.org/generated/seaborn.kdeplot.html)。

加载 Seaborn，尝试一个基本的密度图：

```python
import seaborn as sns
import matplotlib.pyplot as plt
sns.kdeplot(filteredBirds['MinWingspan'])
plt.show()
```
![密度图](../../../../3-Data-Visualization/10-visualization-distributions/images/density1.png)

你可以看到，这个图表与之前的最小翼展数据图表相呼应，只是更平滑了一些。根据 Seaborn 的文档，“相对于直方图，KDE 可以生成一个更简洁、更易解释的图表，尤其是在绘制多个分布时。但如果底层分布是有界的或不平滑的，它可能会引入失真。与直方图一样，表示的质量也取决于选择良好的平滑参数。” [来源](https://seaborn.pydata.org/generated/seaborn.kdeplot.html) 换句话说，异常值一如既往地会让你的图表表现异常。

如果你想重新审视第二个图表中那条锯齿状的 MaxBodyMass 线，可以通过这种方法很好地将其平滑化：

```python
sns.kdeplot(filteredBirds['MaxBodyMass'])
plt.show()
```
![平滑的体重线](../../../../3-Data-Visualization/10-visualization-distributions/images/density2.png)

如果你想要一条平滑但不过于平滑的线，可以编辑 `bw_adjust` 参数：

```python
sns.kdeplot(filteredBirds['MaxBodyMass'], bw_adjust=.2)
plt.show()
```
![较少平滑的体重线](../../../../3-Data-Visualization/10-visualization-distributions/images/density3.png)

✅ 阅读此类型图表可用的参数并进行实验！

这种类型的图表提供了非常直观的可视化效果。例如，只需几行代码，你就可以显示每个鸟类目最大体重的密度：

```python
sns.kdeplot(
   data=filteredBirds, x="MaxBodyMass", hue="Order",
   fill=True, common_norm=False, palette="crest",
   alpha=.5, linewidth=0,
)
```

![每个目体重密度](../../../../3-Data-Visualization/10-visualization-distributions/images/density4.png)

你还可以在一张图表中映射多个变量的密度。测试鸟类的 MaxLength 和 MinLength 与其保护状态的关系：

```python
sns.kdeplot(data=filteredBirds, x="MinLength", y="MaxLength", hue="ConservationStatus")
```

![多个密度叠加](../../../../3-Data-Visualization/10-visualization-distributions/images/multi.png)

也许值得研究一下，根据长度的“易危”鸟类的聚集是否有意义。

## 🚀 挑战

直方图是一种比基本散点图、条形图或折线图更复杂的图表类型。在互联网上搜索直方图的优秀使用案例。它们是如何使用的，展示了什么内容，通常在哪些领域或研究中使用？

## [课后测验](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/19)

## 复习与自学

在本课中，你使用了 Matplotlib 并开始使用 Seaborn 来展示更复杂的图表。研究一下 Seaborn 中的 `kdeplot`，这是一种“一维或多维的连续概率密度曲线”。阅读 [文档](https://seaborn.pydata.org/generated/seaborn.kdeplot.html) 以了解其工作原理。

## 作业

[应用你的技能](assignment.md)

**免责声明**：  
本文档使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。虽然我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于关键信息，建议使用专业人工翻译。我们不对因使用此翻译而产生的任何误解或误读承担责任。