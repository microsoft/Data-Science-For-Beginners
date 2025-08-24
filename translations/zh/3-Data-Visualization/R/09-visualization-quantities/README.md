<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "22acf28f518a4769ea14fa42f4734b9f",
  "translation_date": "2025-08-24T13:50:40+00:00",
  "source_file": "3-Data-Visualization/R/09-visualization-quantities/README.md",
  "language_code": "zh"
}
-->
# 可视化数量
|![ 由 [(@sketchthedocs)](https://sketchthedocs.dev) 绘制的速记图 ](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/sketchnotes/09-Visualizing-Quantities.png)|
|:---:|
| 可视化数量 - _速记图作者 [@nitya](https://twitter.com/nitya)_ |

在本课中，您将学习如何使用一些可用的 R 包库，围绕数量的概念创建有趣的可视化。通过一个关于明尼苏达州鸟类的清理过的数据集，您可以了解许多关于当地野生动物的有趣事实。

## [课前测验](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/16)

## 使用 ggplot2 观察翼展
一个非常优秀的库是 [ggplot2](https://cran.r-project.org/web/packages/ggplot2/index.html)，它可以用来创建各种简单或复杂的图表。一般来说，使用这些库绘制数据的过程包括：确定数据框中要处理的部分，对数据进行必要的转换，分配 x 和 y 轴的值，选择图表类型，然后显示图表。

`ggplot2` 是一个基于“图形语法”声明性创建图形的系统。[图形语法](https://en.wikipedia.org/wiki/Ggplot2) 是一种数据可视化的通用方案，将图表分解为语义组件，如比例和图层。换句话说，`ggplot2` 以少量代码轻松创建单变量或多变量数据的图表，使其成为 R 中最受欢迎的可视化包。用户告诉 `ggplot2` 如何将变量映射到美学属性、使用哪些图形元素，`ggplot2` 会处理其余部分。

> ✅ 图表 = 数据 + 美学 + 几何
> - 数据：指数据集
> - 美学：指要研究的变量（x 和 y 变量）
> - 几何：指图表类型（折线图、柱状图等）

根据您的数据和想通过图表讲述的故事，选择最佳的几何类型（图表类型）。

> - 分析趋势：折线图、柱状图  
> - 比较数值：条形图、柱状图、饼图、散点图  
> - 展示部分与整体的关系：饼图  
> - 展示数据分布：散点图、条形图  
> - 展示数值之间的关系：折线图、散点图、气泡图  

✅ 您还可以查看这个描述性的 [速查表](https://nyu-cdsc.github.io/learningr/assets/data-visualization-2.1.pdf) 来了解 ggplot2。

## 绘制鸟类翼展值的折线图

打开 R 控制台并导入数据集。  
> 注意：数据集存储在此仓库的 `/data` 文件夹中。

让我们导入数据集并查看数据的头部（前 5 行）。

```r
birds <- read.csv("../../data/birds.csv",fileEncoding="UTF-8-BOM")
head(birds)
```  
数据的头部包含文本和数字的混合：

|      | 名称                          | 学名                   | 类别                  | 目           | 科       | 属          | 保护状态         | 最小长度 | 最大长度 | 最小体重   | 最大体重   | 最小翼展   | 最大翼展   |
| ---: | :--------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :----------------- | --------: | --------: | ----------: | ----------: | ----------: | ----------: |
|    0 | 黑腹树鸭                     | Dendrocygna autumnalis | 鸭/鹅/水禽            | 雁形目       | 鸭科     | 树鸭属      | LC                 |        47 |        56 |         652 |        1020 |          76 |          94 |
|    1 | 棕树鸭                       | Dendrocygna bicolor    | 鸭/鹅/水禽            | 雁形目       | 鸭科     | 树鸭属      | LC                 |        45 |        53 |         712 |        1050 |          85 |          93 |
|    2 | 雪雁                         | Anser caerulescens     | 鸭/鹅/水禽            | 雁形目       | 鸭科     | 雁属        | LC                 |        64 |        79 |        2050 |        4050 |         135 |         165 |
|    3 | 罗斯雁                       | Anser rossii           | 鸭/鹅/水禽            | 雁形目       | 鸭科     | 雁属        | LC                 |      57.3 |        64 |        1066 |        1567 |         113 |         116 |
|    4 | 大白额雁                     | Anser albifrons        | 鸭/鹅/水禽            | 雁形目       | 鸭科     | 雁属        | LC                 |        64 |        81 |        1930 |        3310 |         130 |         165 |

让我们从绘制一些数值数据的基本折线图开始。假设您想查看这些有趣鸟类的最大翼展。

```r
install.packages("ggplot2")
library("ggplot2")
ggplot(data=birds, aes(x=Name, y=MaxWingspan,group=1)) +
  geom_line() 
```  
在这里，您安装了 `ggplot2` 包，然后使用 `library("ggplot2")` 命令将其导入工作区。要在 ggplot 中绘制任何图表，使用 `ggplot()` 函数，并将数据集、x 和 y 变量作为属性指定。在这种情况下，我们使用 `geom_line()` 函数，因为我们要绘制折线图。

![MaxWingspan-lineplot](../../../../../3-Data-Visualization/R/09-visualization-quantities/images/MaxWingspan-lineplot.png)

您立即注意到什么？似乎至少有一个异常值——那是一个相当大的翼展！2000+ 厘米的翼展超过 20 米——明尼苏达州有翼龙在飞吗？让我们调查一下。

虽然您可以在 Excel 中快速排序以找到这些可能是输入错误的异常值，但我们将继续从图表中进行可视化处理。

为 x 轴添加标签以显示涉及的鸟类种类：

```r
ggplot(data=birds, aes(x=Name, y=MaxWingspan,group=1)) +
  geom_line() +
  theme(axis.text.x = element_text(angle = 45, hjust=1))+
  xlab("Birds") +
  ylab("Wingspan (CM)") +
  ggtitle("Max Wingspan in Centimeters")
```  
我们在 `theme` 中指定了角度，并在 `xlab()` 和 `ylab()` 中分别指定了 x 和 y 轴的标签。`ggtitle()` 为图表/图形命名。

![MaxWingspan-lineplot-improved](../../../../../3-Data-Visualization/R/09-visualization-quantities/images/MaxWingspan-lineplot-improved.png)

即使将标签旋转设置为 45 度，仍然太多以至于无法阅读。让我们尝试另一种策略：仅标记那些异常值，并在图表内设置标签。您可以使用散点图来腾出更多空间进行标记：

```r
ggplot(data=birds, aes(x=Name, y=MaxWingspan,group=1)) +
  geom_point() +
  geom_text(aes(label=ifelse(MaxWingspan>500,as.character(Name),'')),hjust=0,vjust=0) + 
  theme(axis.title.x=element_blank(), axis.text.x=element_blank(), axis.ticks.x=element_blank())
  ylab("Wingspan (CM)") +
  ggtitle("Max Wingspan in Centimeters") + 
```  
这里发生了什么？您使用 `geom_point()` 函数绘制了散点图。通过此操作，您为 `MaxWingspan > 500` 的鸟类添加了标签，并隐藏了 x 轴上的标签以减少图表的混乱。

您发现了什么？

![MaxWingspan-scatterplot](../../../../../3-Data-Visualization/R/09-visualization-quantities/images/MaxWingspan-scatterplot.png)

## 筛选数据

秃鹰和草原隼虽然可能是非常大的鸟类，但它们的最大翼展似乎被错误标记，多加了一个 0。遇到翼展 25 米的秃鹰的可能性不大，但如果遇到，请告诉我们！让我们创建一个新的数据框，去掉这两个异常值：

```r
birds_filtered <- subset(birds, MaxWingspan < 500)

ggplot(data=birds_filtered, aes(x=Name, y=MaxWingspan,group=1)) +
  geom_point() +
  ylab("Wingspan (CM)") +
  xlab("Birds") +
  ggtitle("Max Wingspan in Centimeters") + 
  geom_text(aes(label=ifelse(MaxWingspan>500,as.character(Name),'')),hjust=0,vjust=0) +
  theme(axis.text.x=element_blank(), axis.ticks.x=element_blank())
```  
我们创建了一个新的数据框 `birds_filtered`，然后绘制了一个散点图。通过筛选掉异常值，您的数据现在更加连贯和易于理解。

![MaxWingspan-scatterplot-improved](../../../../../3-Data-Visualization/R/09-visualization-quantities/images/MaxWingspan-scatterplot-improved.png)

现在我们至少在翼展方面有了一个更干净的数据集，让我们进一步探索这些鸟类。

虽然折线图和散点图可以显示数据值及其分布的信息，但我们想要思考数据集中固有的值。您可以创建可视化来回答以下关于数量的问题：

> 有多少种鸟类类别？它们的数量是多少？  
> 有多少鸟类是灭绝的、濒危的、稀有的或常见的？  
> 在林奈分类法中，各种属和目有多少？  

## 探索条形图

当您需要展示数据分组时，条形图非常实用。让我们探索数据集中存在的鸟类类别，看看哪种类别的数量最多。  
让我们在筛选后的数据上创建一个条形图。

```r
install.packages("dplyr")
install.packages("tidyverse")

library(lubridate)
library(scales)
library(dplyr)
library(ggplot2)
library(tidyverse)

birds_filtered %>% group_by(Category) %>%
  summarise(n=n(),
  MinLength = mean(MinLength),
  MaxLength = mean(MaxLength),
  MinBodyMass = mean(MinBodyMass),
  MaxBodyMass = mean(MaxBodyMass),
  MinWingspan=mean(MinWingspan),
  MaxWingspan=mean(MaxWingspan)) %>% 
  gather("key", "value", - c(Category, n)) %>%
  ggplot(aes(x = Category, y = value, group = key, fill = key)) +
  geom_bar(stat = "identity") +
  scale_fill_manual(values = c("#D62728", "#FF7F0E", "#8C564B","#2CA02C", "#1F77B4", "#9467BD")) +                   
  xlab("Category")+ggtitle("Birds of Minnesota")

```  
在以下代码片段中，我们安装了 [dplyr](https://www.rdocumentation.org/packages/dplyr/versions/0.7.8) 和 [lubridate](https://www.rdocumentation.org/packages/lubridate/versions/1.8.0) 包，以帮助操作和分组数据，从而绘制堆叠条形图。首先，按鸟类的 `Category` 分组数据，然后汇总 `MinLength`、`MaxLength`、`MinBodyMass`、`MaxBodyMass`、`MinWingspan`、`MaxWingspan` 列。然后，使用 `ggplot2` 包绘制条形图，并为不同类别指定颜色和标签。

![Stacked bar chart](../../../../../3-Data-Visualization/R/09-visualization-quantities/images/stacked-bar-chart.png)

然而，这个条形图难以阅读，因为数据没有很好地分组。您需要选择要绘制的数据，因此让我们根据鸟类类别查看鸟类的长度。

筛选数据以仅包含鸟类的类别。

由于类别很多，您可以垂直显示此图表，并调整其高度以适应所有数据：

```r
birds_count<-dplyr::count(birds_filtered, Category, sort = TRUE)
birds_count$Category <- factor(birds_count$Category, levels = birds_count$Category)
ggplot(birds_count,aes(Category,n))+geom_bar(stat="identity")+coord_flip()
```  
您首先统计 `Category` 列中的唯一值，然后将它们排序到一个新的数据框 `birds_count` 中。然后将这些排序后的数据按相同的级别分组，以便按排序方式绘制。使用 `ggplot2`，您绘制了一个条形图。`coord_flip()` 绘制水平条形图。

![category-length](../../../../../3-Data-Visualization/R/09-visualization-quantities/images/category-length.png)

这个条形图很好地展示了每个类别中鸟类的数量。一眼就能看出，这个地区最多的鸟类是鸭/鹅/水禽类别。明尼苏达州是“万湖之地”，这并不令人惊讶！

✅ 尝试对该数据集进行其他计数。有什么让您感到意外吗？

## 比较数据

您可以通过创建新的轴来尝试不同的分组数据比较。尝试比较基于类别的鸟类最大长度：

```r
birds_grouped <- birds_filtered %>%
  group_by(Category) %>%
  summarise(
  MaxLength = max(MaxLength, na.rm = T),
  MinLength = max(MinLength, na.rm = T)
           ) %>%
  arrange(Category)
  
ggplot(birds_grouped,aes(Category,MaxLength))+geom_bar(stat="identity")+coord_flip()
```  
我们按 `Category` 对 `birds_filtered` 数据进行分组，然后绘制条形图。

![comparing data](../../../../../3-Data-Visualization/R/09-visualization-quantities/images/comparingdata.png)

这里没有什么令人意外的：与鹈鹕或鹅相比，蜂鸟的最大长度最小。当数据符合逻辑时，这是好事！

您可以通过叠加数据创建更有趣的条形图可视化。让我们在给定的鸟类类别上叠加最小和最大长度：

```r
ggplot(data=birds_grouped, aes(x=Category)) +
  geom_bar(aes(y=MaxLength), stat="identity", position ="identity",  fill='blue') +
  geom_bar(aes(y=MinLength), stat="identity", position="identity", fill='orange')+
  coord_flip()
```  
![super-imposed values](../../../../../3-Data-Visualization/R/09-visualization-quantities/images/superimposed-values.png)

## 🚀 挑战

这个鸟类数据集提供了关于特定生态系统中不同类型鸟类的大量信息。在互联网上搜索，看看是否能找到其他与鸟类相关的数据集。练习围绕这些鸟类构建图表和图形，发现您之前未曾意识到的事实。

## [课后测验](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/17)

## 复习与自学

本课为您提供了一些关于如何使用 `ggplot2` 可视化数量的信息。研究其他可视化数据集的方法。研究并寻找可以使用其他包（如 [Lattice](https://stat.ethz.ch/R-manual/R-devel/library/lattice/html/Lattice.html) 和 [Plotly](https://github.com/plotly/plotly.R#readme)）进行可视化的数据集。

## 作业
[折线图、散点图和条形图](assignment.md)

**免责声明**：  
本文档使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于关键信息，建议使用专业人工翻译。我们不对因使用此翻译而产生的任何误解或误读承担责任。