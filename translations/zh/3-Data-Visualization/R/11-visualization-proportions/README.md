<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "47028abaaafa2bcb1079702d20569066",
  "translation_date": "2025-08-24T13:59:47+00:00",
  "source_file": "3-Data-Visualization/R/11-visualization-proportions/README.md",
  "language_code": "zh"
}
-->
# 可视化比例

|![ 由 [(@sketchthedocs)](https://sketchthedocs.dev) 绘制的速记图 ](../../../sketchnotes/11-Visualizing-Proportions.png)|
|:---:|
|可视化比例 - _速记图由 [@nitya](https://twitter.com/nitya) 绘制_ |

在本课中，您将使用一个以自然为主题的数据集来可视化比例，例如在关于蘑菇的数据集中，不同种类的真菌数量占比。让我们通过一个来自 Audubon 的数据集来探索这些迷人的真菌，该数据集列出了 Agaricus 和 Lepiota 家族中 23 种有鳃蘑菇的详细信息。您将尝试一些有趣的可视化方式，例如：

- 饼图 🥧  
- 环形图 🍩  
- 华夫图 🧇  

> 💡 微软研究院的一个非常有趣的项目 [Charticulator](https://charticulator.com) 提供了一个免费的拖放界面用于数据可视化。在他们的一个教程中也使用了这个蘑菇数据集！因此，您可以一边探索数据，一边学习这个工具库：[Charticulator 教程](https://charticulator.com/tutorials/tutorial4.html)。

## [课前测验](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/20)

## 了解您的蘑菇 🍄

蘑菇非常有趣。让我们导入一个数据集来研究它们：

```r
mushrooms = read.csv('../../data/mushrooms.csv')
head(mushrooms)
```  
打印出了一张表格，包含一些适合分析的优秀数据：  

| 类别       | 菌盖形状 | 菌盖表面 | 菌盖颜色 | 是否有瘀伤 | 气味    | 鳃附着方式 | 鳃间距   | 鳃大小   | 鳃颜色   | 茎形状     | 茎根部     | 茎环上表面          | 茎环下表面          | 茎环上颜色          | 茎环下颜色          | 幔类型   | 幔颜色   | 环数量   | 环类型   | 孢子印颜色       | 种群数量   | 栖息地   |
| --------- | --------- | --------- | --------- | --------- | ------- | ----------- | --------- | --------- | --------- | ----------- | ---------- | ------------------ | ------------------ | ------------------ | ------------------ | --------- | --------- | --------- | --------- | --------------- | --------- | ------- |
| 有毒      | 凸形      | 光滑      | 棕色      | 有瘀伤    | 刺鼻    | 游离        | 紧密      | 窄        | 黑色      | 扩大        | 等粗        | 光滑               | 光滑               | 白色               | 白色               | 部分      | 白色      | 一个      | 垂饰      | 黑色             | 分散      | 城市     |
| 可食用    | 凸形      | 光滑      | 黄色      | 有瘀伤    | 杏仁    | 游离        | 紧密      | 宽        | 黑色      | 扩大        | 棍状        | 光滑               | 光滑               | 白色               | 白色               | 部分      | 白色      | 一个      | 垂饰      | 棕色             | 众多      | 草地     |
| 可食用    | 钟形      | 光滑      | 白色      | 有瘀伤    | 茴香    | 游离        | 紧密      | 宽        | 棕色      | 扩大        | 棍状        | 光滑               | 光滑               | 白色               | 白色               | 部分      | 白色      | 一个      | 垂饰      | 棕色             | 众多      | 草原     |
| 有毒      | 凸形      | 鳞状      | 白色      | 有瘀伤    | 刺鼻    | 游离        | 紧密      | 窄        | 棕色      | 扩大        | 等粗        | 光滑               | 光滑               | 白色               | 白色               | 部分      | 白色      | 一个      | 垂饰      | 黑色             | 分散      | 城市     |
| 可食用    | 凸形      | 光滑      | 绿色      | 无瘀伤    | 无气味  | 游离        | 拥挤      | 宽        | 黑色      | 锥形        | 等粗        | 光滑               | 光滑               | 白色               | 白色               | 部分      | 白色      | 一个      | 消失      | 棕色             | 丰富      | 草地     |
| 可食用    | 凸形      | 鳞状      | 黄色      | 有瘀伤    | 杏仁    | 游离        | 紧密      | 宽        | 棕色      | 扩大        | 棍状        | 光滑               | 光滑               | 白色               | 白色               | 部分      | 白色      | 一个      | 垂饰      | 黑色             | 众多      | 草地     |

您会立刻注意到，所有数据都是文本格式。为了在图表中使用这些数据，您需要将其转换。实际上，大部分数据都以对象形式表示：

```r
names(mushrooms)
```  

输出为：  

```output
[1] "class"                    "cap.shape"               
 [3] "cap.surface"              "cap.color"               
 [5] "bruises"                  "odor"                    
 [7] "gill.attachment"          "gill.spacing"            
 [9] "gill.size"                "gill.color"              
[11] "stalk.shape"              "stalk.root"              
[13] "stalk.surface.above.ring" "stalk.surface.below.ring"
[15] "stalk.color.above.ring"   "stalk.color.below.ring"  
[17] "veil.type"                "veil.color"              
[19] "ring.number"              "ring.type"               
[21] "spore.print.color"        "population"              
[23] "habitat"            
```  
将这些数据转换，将 'class' 列转为类别：  

```r
library(dplyr)
grouped=mushrooms %>%
  group_by(class) %>%
  summarise(count=n())
```  

现在，如果打印蘑菇数据，您会看到它已根据有毒/可食用类别分组：  
```r
View(grouped)
```  

| 类别   | 数量   |
| --------- | --------- |
| 可食用    | 4208      |
| 有毒      | 3916      |

如果按照此表中呈现的顺序创建类别标签，您可以绘制一个饼图。

## 饼图！

```r
pie(grouped$count,grouped$class, main="Edible?")
```  
瞧，一个饼图展示了这两类蘑菇数据的比例。在这里，确保标签数组的顺序正确非常重要，因此务必验证标签的构建顺序！

![饼图](../../../../../3-Data-Visualization/R/11-visualization-proportions/images/pie1-wb.png)

## 环形图！

环形图是一种更具视觉吸引力的饼图，它在中间有一个空洞。让我们用这种方法查看数据。

看看蘑菇生长的各种栖息地：

```r
library(dplyr)
habitat=mushrooms %>%
  group_by(habitat) %>%
  summarise(count=n())
View(habitat)
```  
输出为：  

| 栖息地   | 数量   |
| --------- | --------- |
| 草地      | 2148      |
| 树叶      | 832       |
| 草原      | 292       |
| 小路      | 1144      |
| 城市      | 368       |
| 废地      | 192       |
| 木材      | 3148      |

在这里，您将数据按栖息地分组。共有 7 个栖息地，因此将它们用作环形图的标签：

```r
library(ggplot2)
library(webr)
PieDonut(habitat, aes(habitat, count=count))
```  

![环形图](../../../../../3-Data-Visualization/R/11-visualization-proportions/images/donut-wb.png)  

此代码使用了两个库 - ggplot2 和 webr。通过 webr 库的 PieDonut 函数，我们可以轻松创建环形图！

仅使用 ggplot2 库也可以在 R 中制作环形图。您可以在 [这里](https://www.r-graph-gallery.com/128-ring-or-donut-plot.html) 学习更多内容并尝试自己制作。

现在您知道如何分组数据并以饼图或环形图显示，接下来可以尝试其他类型的图表。例如华夫图，这是一种不同的数量可视化方式。

## 华夫图！

华夫图是一种以二维方块阵列形式可视化数量的图表。尝试用此数据集可视化蘑菇菌盖颜色的不同数量。为此，您需要安装一个名为 [waffle](https://cran.r-project.org/web/packages/waffle/waffle.pdf) 的辅助库，并使用它生成可视化图表：

```r
install.packages("waffle", repos = "https://cinc.rud.is")
```  

选择一部分数据进行分组：  

```r
library(dplyr)
cap_color=mushrooms %>%
  group_by(cap.color) %>%
  summarise(count=n())
View(cap_color)
```  

通过创建标签并分组数据来生成华夫图：  

```r
library(waffle)
names(cap_color$count) = paste0(cap_color$cap.color)
waffle((cap_color$count/10), rows = 7, title = "Waffle Chart")+scale_fill_manual(values=c("brown", "#F0DC82", "#D2691E", "green", 
                                                                                     "pink", "purple", "red", "grey", 
                                                                                     "yellow","white"))
```  

通过华夫图，您可以清楚地看到蘑菇菌盖颜色的比例。有趣的是，有许多绿色菌盖的蘑菇！

![华夫图](../../../../../3-Data-Visualization/R/11-visualization-proportions/images/waffle.png)

在本课中，您学习了三种可视化比例的方法。首先，您需要将数据分组为类别，然后决定哪种方式最适合展示数据——饼图、环形图或华夫图。每种方式都直观且能快速呈现数据集的概况。

## 🚀 挑战

尝试在 [Charticulator](https://charticulator.com) 中重新创建这些有趣的图表。

## [课后测验](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/21)

## 复习与自学

有时很难决定何时使用饼图、环形图或华夫图。以下是一些相关文章供您阅读：  

https://www.beautiful.ai/blog/battle-of-the-charts-pie-chart-vs-donut-chart  

https://medium.com/@hypsypops/pie-chart-vs-donut-chart-showdown-in-the-ring-5d24fd86a9ce  

https://www.mit.edu/~mbarker/formula1/f1help/11-ch-c6.htm  

https://medium.datadriveninvestor.com/data-visualization-done-the-right-way-with-tableau-waffle-chart-fdf2a19be402  

进行一些研究，了解更多关于如何做出这种选择的信息。

## 作业

[在 Excel 中尝试](assignment.md)  

**免责声明**：  
本文档使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。虽然我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于关键信息，建议使用专业人工翻译。我们对因使用此翻译而产生的任何误解或误读不承担责任。