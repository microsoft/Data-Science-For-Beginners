<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "af6a12015c6e250e500b570a9fa42593",
  "translation_date": "2025-08-25T18:39:54+00:00",
  "source_file": "3-Data-Visualization/11-visualization-proportions/README.md",
  "language_code": "zh"
}
-->
# 可视化比例

|![由 [(@sketchthedocs)](https://sketchthedocs.dev) 绘制的速记图](../../sketchnotes/11-Visualizing-Proportions.png)|
|:---:|
|可视化比例 - _速记图作者 [@nitya](https://twitter.com/nitya)_ |

在本课中，你将使用一个以自然为主题的数据集来可视化比例，例如在一个关于蘑菇的数据集中有多少种不同类型的真菌。让我们通过一个来自 Audubon 的数据集来探索这些迷人的真菌，该数据集列出了 Agaricus 和 Lepiota 家族中 23 种有鳃蘑菇的详细信息。你将尝试一些有趣的可视化方法，例如：

- 饼图 🥧  
- 环形图 🍩  
- 华夫图 🧇  

> 💡 一个非常有趣的项目 [Charticulator](https://charticulator.com) 由微软研究院开发，提供了一个免费的拖放界面用于数据可视化。在他们的一个教程中也使用了这个蘑菇数据集！因此你可以同时探索数据并学习这个库：[Charticulator 教程](https://charticulator.com/tutorials/tutorial4.html)。

## [课前测验](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/20)

## 了解你的蘑菇 🍄

蘑菇非常有趣。让我们导入一个数据集来研究它们：

```python
import pandas as pd
import matplotlib.pyplot as plt
mushrooms = pd.read_csv('../../data/mushrooms.csv')
mushrooms.head()
```  
一个表格打印出来，包含一些很棒的分析数据：

| 类别       | 帽型      | 帽表面      | 帽颜色      | 是否有瘀伤 | 气味      | 鳃连接方式      | 鳃间距      | 鳃大小      | 鳃颜色      | 茎形状      | 茎根      | 环上方茎表面      | 环下方茎表面      | 环上方茎颜色      | 环下方茎颜色      | 面纱类型      | 面纱颜色      | 环数量      | 环类型      | 孢子印颜色      | 种群      | 栖息地      |
| --------- | --------- | ----------- | --------- | ------- | ------- | --------------- | ------------ | --------- | ---------- | ----------- | ---------- | ------------------------ | ------------------------ | ---------------------- | ---------------------- | --------- | ---------- | ----------- | --------- | ----------------- | ---------- | ------- |
| 有毒      | 凸形      | 光滑        | 棕色       | 有瘀伤   | 刺鼻    | 自由            | 紧密        | 狭窄      | 黑色       | 扩大        | 等长      | 光滑                   | 光滑                   | 白色                  | 白色                  | 部分      | 白色      | 一个        | 垂饰      | 黑色             | 分散      | 城市      |
| 可食用    | 凸形      | 光滑        | 黄色       | 有瘀伤   | 杏仁味  | 自由            | 紧密        | 宽广      | 黑色       | 扩大        | 棍状      | 光滑                   | 光滑                   | 白色                  | 白色                  | 部分      | 白色      | 一个        | 垂饰      | 棕色             | 众多      | 草地      |
| 可食用    | 钟形      | 光滑        | 白色       | 有瘀伤   | 茴香味  | 自由            | 紧密        | 宽广      | 棕色       | 扩大        | 棍状      | 光滑                   | 光滑                   | 白色                  | 白色                  | 部分      | 白色      | 一个        | 垂饰      | 棕色             | 众多      | 草地      |
| 有毒      | 凸形      | 鳞片状      | 白色       | 有瘀伤   | 刺鼻    | 自由            | 紧密        | 狭窄      | 棕色       | 扩大        | 等长      | 光滑                   | 光滑                   | 白色                  | 白色                  | 部分      | 白色      | 一个        | 垂饰      | 黑色             | 分散      | 城市      |

你会立即注意到所有数据都是文本格式。为了在图表中使用这些数据，你需要将其转换。事实上，大部分数据是以对象形式表示的：

```python
print(mushrooms.select_dtypes(["object"]).columns)
```  

输出为：

```output
Index(['class', 'cap-shape', 'cap-surface', 'cap-color', 'bruises', 'odor',
       'gill-attachment', 'gill-spacing', 'gill-size', 'gill-color',
       'stalk-shape', 'stalk-root', 'stalk-surface-above-ring',
       'stalk-surface-below-ring', 'stalk-color-above-ring',
       'stalk-color-below-ring', 'veil-type', 'veil-color', 'ring-number',
       'ring-type', 'spore-print-color', 'population', 'habitat'],
      dtype='object')
```  
将这些数据转换为类别，例如将“类别”列转换为分类：

```python
cols = mushrooms.select_dtypes(["object"]).columns
mushrooms[cols] = mushrooms[cols].astype('category')
```  

```python
edibleclass=mushrooms.groupby(['class']).count()
edibleclass
```  

现在，如果打印出蘑菇数据，你会看到它已经根据有毒/可食用类别分组：

|           | 帽型      | 帽表面      | 帽颜色      | 是否有瘀伤 | 气味 | 鳃连接方式      | 鳃间距      | 鳃大小      | 鳃颜色      | 茎形状      | ... | 环下方茎表面      | 环上方茎颜色      | 环下方茎颜色      | 面纱类型      | 面纱颜色      | 环数量      | 环类型      | 孢子印颜色      | 种群      | 栖息地      |
| --------- | --------- | ----------- | --------- | ------- | ---- | --------------- | ------------ | --------- | ---------- | ----------- | --- | ------------------------ | ---------------------- | ---------------------- | --------- | ---------- | ----------- | --------- | ----------------- | ---------- | ------- |
| 类别       |           |             |           |         |      |                 |              |           |            |             |     |                          |                        |                        |           |            |             |           |                   |            |         |
| 可食用    | 4208      | 4208        | 4208      | 4208    | 4208 | 4208            | 4208         | 4208      | 4208       | 4208        | ... | 4208                     | 4208                   | 4208                   | 4208      | 4208       | 4208        | 4208      | 4208              | 4208       | 4208    |
| 有毒      | 3916      | 3916        | 3916      | 3916    | 3916 | 3916            | 3916         | 3916      | 3916       | 3916        | ... | 3916                     | 3916                   | 3916                   | 3916      | 3916       | 3916        | 3916      | 3916              | 3916       | 3916    |

如果按照此表中呈现的顺序创建类别标签，你可以绘制一个饼图：

## 饼图！

```python
labels=['Edible','Poisonous']
plt.pie(edibleclass['population'],labels=labels,autopct='%.1f %%')
plt.title('Edible?')
plt.show()
```  
瞧，一个饼图展示了根据蘑菇的两种类别（有毒/可食用）数据的比例。这里正确设置标签的顺序非常重要，因此务必验证标签数组的构建顺序！

![饼图](../../../../translated_images/pie1-wb.e201f2fcc335413143ce37650fb7f5f0bb21358e7823a327ed8644dfb84be9db.zh.png)

## 环形图！

环形图是一种更具视觉吸引力的饼图，它在中间有一个空洞。让我们用这种方法查看数据。

看看蘑菇生长的各种栖息地：

```python
habitat=mushrooms.groupby(['habitat']).count()
habitat
```  
这里，你将数据按栖息地分组。共有 7 种栖息地，因此使用这些作为环形图的标签：

```python
labels=['Grasses','Leaves','Meadows','Paths','Urban','Waste','Wood']

plt.pie(habitat['class'], labels=labels,
        autopct='%1.1f%%', pctdistance=0.85)
  
center_circle = plt.Circle((0, 0), 0.40, fc='white')
fig = plt.gcf()

fig.gca().add_artist(center_circle)
  
plt.title('Mushroom Habitats')
  
plt.show()
```  

![环形图](../../../../translated_images/donut-wb.be3c12a22712302b5d10c40014d5389d4a1ae4412fe1655b3cf4af57b64f799a.zh.png)

这段代码绘制了一个图表和一个中心圆，然后将中心圆添加到图表中。通过将 `0.40` 更改为其他值来编辑中心圆的宽度。

环形图可以通过多种方式调整标签。特别是标签可以被突出显示以提高可读性。了解更多信息请参阅 [文档](https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_and_donut_labels.html?highlight=donut)。

现在你已经知道如何分组数据并将其显示为饼图或环形图，你可以探索其他类型的图表。试试华夫图，这是一种不同的方式来探索数量。

## 华夫图！

华夫图是一种以二维方块阵列可视化数量的图表。尝试可视化数据集中蘑菇帽颜色的不同数量。为此，你需要安装一个辅助库 [PyWaffle](https://pypi.org/project/pywaffle/) 并使用 Matplotlib：

```python
pip install pywaffle
```  

选择一段数据进行分组：

```python
capcolor=mushrooms.groupby(['cap-color']).count()
capcolor
```  

通过创建标签并分组数据来创建华夫图：

```python
import pandas as pd
import matplotlib.pyplot as plt
from pywaffle import Waffle
  
data ={'color': ['brown', 'buff', 'cinnamon', 'green', 'pink', 'purple', 'red', 'white', 'yellow'],
    'amount': capcolor['class']
     }
  
df = pd.DataFrame(data)
  
fig = plt.figure(
    FigureClass = Waffle,
    rows = 100,
    values = df.amount,
    labels = list(df.color),
    figsize = (30,30),
    colors=["brown", "tan", "maroon", "green", "pink", "purple", "red", "whitesmoke", "yellow"],
)
```  

使用华夫图，你可以清楚地看到蘑菇数据集中帽颜色的比例。有趣的是，有许多绿色帽子的蘑菇！

![华夫图](../../../../translated_images/waffle.5455dbae4ccf17d53bb40ff0a657ecef7b8aa967e27a19cc96325bd81598f65e.zh.png)

✅ PyWaffle 支持在图表中使用图标，这些图标可以是 [Font Awesome](https://fontawesome.com/) 中的任何图标。尝试使用图标代替方块来创建更有趣的华夫图。

在本课中，你学习了三种可视化比例的方法。首先，你需要将数据分组为类别，然后决定哪种方式最适合展示数据——饼图、环形图或华夫图。所有这些方法都能让用户快速了解数据集。

## 🚀 挑战

尝试在 [Charticulator](https://charticulator.com) 中重新创建这些有趣的图表。

## [课后测验](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/21)

## 复习与自学

有时不容易决定何时使用饼图、环形图或华夫图。以下是一些相关的文章：

https://www.beautiful.ai/blog/battle-of-the-charts-pie-chart-vs-donut-chart  

https://medium.com/@hypsypops/pie-chart-vs-donut-chart-showdown-in-the-ring-5d24fd86a9ce  

https://www.mit.edu/~mbarker/formula1/f1help/11-ch-c6.htm  

https://medium.datadriveninvestor.com/data-visualization-done-the-right-way-with-tableau-waffle-chart-fdf2a19be402  

进行一些研究以找到更多关于这个选择的信息。

## 作业

[在 Excel 中尝试](assignment.md)  

**免责声明**：  
本文档使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于关键信息，建议使用专业人工翻译。我们对因使用此翻译而产生的任何误解或误读不承担责任。