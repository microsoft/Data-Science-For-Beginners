<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a33c5d4b4156a2b41788d8720b6f724c",
  "translation_date": "2025-08-25T18:16:40+00:00",
  "source_file": "3-Data-Visualization/R/12-visualization-relationships/README.md",
  "language_code": "zh"
}
-->
# 可视化关系：关于蜂蜜的一切 🍯

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../../sketchnotes/12-Visualizing-Relationships.png)|
|:---:|
|可视化关系 - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

延续我们研究的自然主题，让我们探索一些有趣的可视化方法，展示不同类型蜂蜜之间的关系。这些数据来源于[美国农业部](https://www.nass.usda.gov/About_NASS/index.php)。

这个包含约600项的数据集展示了美国多个州的蜂蜜生产情况。例如，你可以查看每个州从1998到2012年的蜂群数量、每群产量、总产量、库存、每磅价格以及蜂蜜生产的价值，每个州每年一行数据。

我们可以通过可视化来研究某个州每年的生产情况与该州蜂蜜价格之间的关系。或者，你也可以可视化各州每群蜂蜜产量之间的关系。这段时间涵盖了2006年首次出现的毁灭性“蜂群崩溃综合症（CCD）”（http://npic.orst.edu/envir/ccd.html），因此这是一个值得研究的引人深思的数据集。🐝

## [课前测验](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/22)

在本课中，你可以使用之前用过的ggplot2库，这是一个很好的工具，用于可视化变量之间的关系。特别有趣的是ggplot2的`geom_point`和`qplot`函数，它们可以快速生成散点图和折线图，用于可视化“[统计关系](https://ggplot2.tidyverse.org/)”，帮助数据科学家更好地理解变量之间的关联。

## 散点图

使用散点图展示蜂蜜价格在每个州逐年变化的情况。ggplot2通过`ggplot`和`geom_point`可以方便地对州数据进行分组，并显示分类和数值数据的点。

让我们从导入数据和Seaborn开始：

```r
honey=read.csv('../../data/honey.csv')
head(honey)
```
你会注意到蜂蜜数据中有几个有趣的列，包括年份和每磅价格。让我们按美国州分组来探索这些数据：

| 州   | 蜂群数量 | 每群产量 | 总产量   | 库存     | 每磅价格   | 生产价值   | 年份 |
| ----- | ------ | ----------- | --------- | -------- | ---------- | --------- | ---- |
| AL    | 16000  | 71          | 1136000   | 159000   | 0.72       | 818000    | 1998 |
| AZ    | 55000  | 60          | 3300000   | 1485000  | 0.64       | 2112000   | 1998 |
| AR    | 53000  | 65          | 3445000   | 1688000  | 0.59       | 2033000   | 1998 |
| CA    | 450000 | 83          | 37350000  | 12326000 | 0.62       | 23157000  | 1998 |
| CO    | 27000  | 72          | 1944000   | 1594000  | 0.7        | 1361000   | 1998 |
| FL    | 230000 | 98          |22540000   | 4508000  | 0.64       | 14426000  | 1998 |

创建一个基础散点图，展示蜂蜜每磅价格与其来源州之间的关系。让`y`轴足够高以显示所有州：

```r
library(ggplot2)
ggplot(honey, aes(x = priceperlb, y = state)) +
  geom_point(colour = "blue")
```
![scatterplot 1](../../../../../translated_images/zh/scatter1.86b8900674d88b26dd3353a83fe604e9ab3722c4680cc40ee9beb452ff02cdea.png)

现在，用蜂蜜色调展示同样的数据，显示价格随年份的变化。你可以通过添加`scale_color_gradientn`参数来实现逐年变化的可视化：

> ✅ 了解更多关于[scale_color_gradientn](https://www.rdocumentation.org/packages/ggplot2/versions/0.9.1/topics/scale_colour_gradientn)的信息 - 尝试一个美丽的彩虹色方案！

```r
ggplot(honey, aes(x = priceperlb, y = state, color=year)) +
  geom_point()+scale_color_gradientn(colours = colorspace::heat_hcl(7))
```
![scatterplot 2](../../../../../translated_images/zh/scatter2.4d1cbc693bad20e2b563888747eb6bdf65b73ce449d903f7cd4068a78502dcff.png)

通过这个颜色方案的变化，你可以明显看到蜂蜜每磅价格在这些年间逐年上涨。如果你查看数据中的一个样本集（例如亚利桑那州），你会发现价格逐年上涨的模式，虽然有少数例外：

| 州   | 蜂群数量 | 每群产量 | 总产量   | 库存     | 每磅价格   | 生产价值   | 年份 |
| ----- | ------ | ----------- | --------- | ------- | ---------- | --------- | ---- |
| AZ    | 55000  | 60          | 3300000   | 1485000 | 0.64       | 2112000   | 1998 |
| AZ    | 52000  | 62          | 3224000   | 1548000 | 0.62       | 1999000   | 1999 |
| AZ    | 40000  | 59          | 2360000   | 1322000 | 0.73       | 1723000   | 2000 |
| AZ    | 43000  | 59          | 2537000   | 1142000 | 0.72       | 1827000   | 2001 |
| AZ    | 38000  | 63          | 2394000   | 1197000 | 1.08       | 2586000   | 2002 |
| AZ    | 35000  | 72          | 2520000   | 983000  | 1.34       | 3377000   | 2003 |
| AZ    | 32000  | 55          | 1760000   | 774000  | 1.11       | 1954000   | 2004 |
| AZ    | 36000  | 50          | 1800000   | 720000  | 1.04       | 1872000   | 2005 |
| AZ    | 30000  | 65          | 1950000   | 839000  | 0.91       | 1775000   | 2006 |
| AZ    | 30000  | 64          | 1920000   | 902000  | 1.26       | 2419000   | 2007 |
| AZ    | 25000  | 64          | 1600000   | 336000  | 1.26       | 2016000   | 2008 |
| AZ    | 20000  | 52          | 1040000   | 562000  | 1.45       | 1508000   | 2009 |
| AZ    | 24000  | 77          | 1848000   | 665000  | 1.52       | 2809000   | 2010 |
| AZ    | 23000  | 53          | 1219000   | 427000  | 1.55       | 1889000   | 2011 |
| AZ    | 22000  | 46          | 1012000   | 253000  | 1.79       | 1811000   | 2012 |

另一种可视化这种变化的方法是使用大小而不是颜色。对于色盲用户，这可能是一个更好的选择。编辑你的可视化，用点的大小来展示价格的增长：

```r
ggplot(honey, aes(x = priceperlb, y = state)) +
  geom_point(aes(size = year),colour = "blue") +
  scale_size_continuous(range = c(0.25, 3))
```
你可以看到点的大小逐渐增大。

![scatterplot 3](../../../../../translated_images/zh/scatter3.722d21e6f20b3ea2e18339bb9b10d75906126715eb7d5fdc88fe74dcb6d7066a.png)

这是否是一个简单的供需关系？由于气候变化和蜂群崩溃等因素，是否导致蜂蜜的供应逐年减少，从而价格上涨？

为了发现数据集中一些变量之间的相关性，让我们探索一些折线图。

## 折线图

问题：蜂蜜每磅价格是否逐年明显上涨？你可以通过创建一个单一折线图来最容易地发现这一点：

```r
qplot(honey$year,honey$priceperlb, geom='smooth', span =0.5, xlab = "year",ylab = "priceperlb")
```
答案：是的，除了2003年左右的一些例外：

![line chart 1](../../../../../translated_images/zh/line1.299b576fbb2a59e60a59e7130030f59836891f90302be084e4e8d14da0562e2a.png)

问题：那么在2003年，我们是否也能看到蜂蜜供应的激增？如果你查看逐年的总产量呢？

```python
qplot(honey$year,honey$totalprod, geom='smooth', span =0.5, xlab = "year",ylab = "totalprod")
```

![line chart 2](../../../../../translated_images/zh/line2.3b18fcda7176ceba5b6689eaaabb817d49c965e986f11cac1ae3f424030c34d8.png)

答案：并不明显。如果你查看总产量，实际上在那一年似乎有所增加，尽管总体而言蜂蜜的产量在这些年间是下降的。

问题：在这种情况下，是什么导致了2003年蜂蜜价格的激增？

为了发现这一点，你可以探索一个分面网格。

## 分面网格

分面网格可以选择数据集的一个维度（在我们的例子中，你可以选择“年份”，以避免生成过多的分面）。Seaborn可以为你选择的x和y坐标生成每个分面的图表，以便更容易进行视觉比较。2003年在这种比较中是否显得特别突出？

使用`facet_wrap`创建一个分面网格，推荐参考[ggplot2的文档](https://ggplot2.tidyverse.org/reference/facet_wrap.html)。

```r
ggplot(honey, aes(x=yieldpercol, y = numcol,group = 1)) + 
  geom_line() + facet_wrap(vars(year))
```
在这个可视化中，你可以比较逐年蜂群产量和蜂群数量，并将列数设置为3：

![facet grid](../../../../../translated_images/zh/facet.491ad90d61c2a7cc69b50c929f80786c749e38217ccedbf1e22ed8909b65987c.png)

对于这个数据集，逐年和各州之间，蜂群数量和产量并没有特别突出的变化。是否有其他方法可以发现这两个变量之间的相关性？

## 双折线图

尝试使用R的`par`和`plot`函数，通过叠加两个折线图来创建多线图。我们将在x轴上绘制年份，并显示两个y轴。展示每群产量和蜂群数量的叠加：

```r
par(mar = c(5, 4, 4, 4) + 0.3)              
plot(honey$year, honey$numcol, pch = 16, col = 2,type="l")              
par(new = TRUE)                             
plot(honey$year, honey$yieldpercol, pch = 17, col = 3,              
     axes = FALSE, xlab = "", ylab = "",type="l")
axis(side = 4, at = pretty(range(y2)))      
mtext("colony yield", side = 4, line = 3)   
```
![superimposed plots](../../../../../translated_images/zh/dual-line.fc4665f360a54018d7df9bc6abcc26460112e17dcbda18d3b9ae6109b32b36c3.png)

虽然2003年没有明显的异常，但这让我们可以以一个稍微乐观的结论结束这节课：尽管蜂群数量总体上在下降，但蜂群数量正在趋于稳定，尽管每群产量在减少。

加油，蜜蜂们！

🐝❤️
## 🚀 挑战

在本课中，你学习了更多关于散点图和线网格的其他用途，包括分面网格。挑战自己使用不同的数据集创建一个分面网格，也许是你之前课程中使用过的数据集。注意创建这些网格所需的时间，以及如何谨慎选择需要绘制的网格数量。

## [课后测验](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/23)

## 复习与自学

折线图可以简单也可以非常复杂。阅读[ggplot2文档](https://ggplot2.tidyverse.org/reference/geom_path.html#:~:text=geom_line()%20connects%20them%20in,which%20cases%20are%20connected%20together)，了解构建折线图的各种方法。尝试使用文档中列出的其他方法来增强你在本课中构建的折线图。

## 作业

[深入蜂巢](assignment.md)

**免责声明**：  
本文档使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。尽管我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原始语言的文档作为权威来源。对于关键信息，建议使用专业人工翻译。对于因使用本翻译而引起的任何误解或误读，我们概不负责。