<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a33c5d4b4156a2b41788d8720b6f724c",
  "translation_date": "2025-08-24T13:48:04+00:00",
  "source_file": "3-Data-Visualization/R/12-visualization-relationships/README.md",
  "language_code": "tw"
}
-->
# 視覺化關係：關於蜂蜜 🍯

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../../sketchnotes/12-Visualizing-Relationships.png)|
|:---:|
|視覺化關係 - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

延續我們研究的自然主題，讓我們探索一些有趣的視覺化方式，來展示不同種類蜂蜜之間的關係。這些數據集來自[美國農業部](https://www.nass.usda.gov/About_NASS/index.php)。

這個包含約600項的數據集展示了美國多個州的蜂蜜生產情況。例如，您可以查看每個州在1998年至2012年間的蜂群數量、每群產量、總產量、庫存、每磅價格以及蜂蜜的生產價值，每個州每年一行數據。

視覺化某州每年的生產量與該州蜂蜜價格之間的關係會很有趣。或者，您可以視覺化各州每群蜂蜜產量之間的關係。這段時間涵蓋了2006年首次出現的毀滅性“蜂群崩潰症”（CCD，Colony Collapse Disorder）（http://npic.orst.edu/envir/ccd.html），因此這是一個值得研究的數據集。🐝

## [課前測驗](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/22)

在本課中，您可以使用 ggplot2，這是一個您之前使用過的優秀庫，用於視覺化變量之間的關係。特別有趣的是 ggplot2 的 `geom_point` 和 `qplot` 函數，它們可以快速生成散點圖和折線圖，視覺化“[統計關係](https://ggplot2.tidyverse.org/)”，幫助數據科學家更好地理解變量之間的關聯。

## 散點圖

使用散點圖展示蜂蜜價格如何逐年在各州演變。ggplot2 的 `ggplot` 和 `geom_point` 可以方便地將州數據分組，並顯示分類和數值數據的數據點。

讓我們先導入數據和 Seaborn：

```r
honey=read.csv('../../data/honey.csv')
head(honey)
```
您會注意到蜂蜜數據中有幾個有趣的列，包括年份和每磅價格。讓我們按美國州分組來探索這些數據：

| 州    | 蜂群數量 | 每群產量 | 總產量     | 庫存     | 每磅價格   | 生產價值   | 年份 |
| ----- | -------- | -------- | ---------- | -------- | ---------- | ---------- | ---- |
| AL    | 16000    | 71       | 1136000    | 159000   | 0.72       | 818000     | 1998 |
| AZ    | 55000    | 60       | 3300000    | 1485000  | 0.64       | 2112000    | 1998 |
| AR    | 53000    | 65       | 3445000    | 1688000  | 0.59       | 2033000    | 1998 |
| CA    | 450000   | 83       | 37350000   | 12326000 | 0.62       | 23157000   | 1998 |
| CO    | 27000    | 72       | 1944000    | 1594000  | 0.7        | 1361000    | 1998 |
| FL    | 230000   | 98       | 22540000   | 4508000  | 0.64       | 14426000   | 1998 |

創建一個基本散點圖，展示蜂蜜每磅價格與其來源州之間的關係。讓 `y` 軸足夠高以顯示所有州：

```r
library(ggplot2)
ggplot(honey, aes(x = priceperlb, y = state)) +
  geom_point(colour = "blue")
```
![散點圖 1](../../../../../3-Data-Visualization/R/12-visualization-relationships/images/scatter1.png)

現在，使用蜂蜜色系展示相同數據，顯示價格如何逐年演變。您可以通過添加 'scale_color_gradientn' 參數來展示逐年變化：

> ✅ 了解更多關於 [scale_color_gradientn](https://www.rdocumentation.org/packages/ggplot2/versions/0.9.1/topics/scale_colour_gradientn) 的信息 - 試試美麗的彩虹色系！

```r
ggplot(honey, aes(x = priceperlb, y = state, color=year)) +
  geom_point()+scale_color_gradientn(colours = colorspace::heat_hcl(7))
```
![散點圖 2](../../../../../3-Data-Visualization/R/12-visualization-relationships/images/scatter2.png)

使用這種色系變化，您可以清楚地看到蜂蜜每磅價格在多年來的明顯增長。事實上，如果您查看數據中的樣本集（例如選擇亞利桑那州），您可以看到價格逐年上漲的模式，只有少數例外：

| 州    | 蜂群數量 | 每群產量 | 總產量     | 庫存     | 每磅價格   | 生產價值   | 年份 |
| ----- | -------- | -------- | ---------- | -------- | ---------- | ---------- | ---- |
| AZ    | 55000    | 60       | 3300000    | 1485000  | 0.64       | 2112000    | 1998 |
| AZ    | 52000    | 62       | 3224000    | 1548000  | 0.62       | 1999000    | 1999 |
| AZ    | 40000    | 59       | 2360000    | 1322000  | 0.73       | 1723000    | 2000 |
| AZ    | 43000    | 59       | 2537000    | 1142000  | 0.72       | 1827000    | 2001 |
| AZ    | 38000    | 63       | 2394000    | 1197000  | 1.08       | 2586000    | 2002 |
| AZ    | 35000    | 72       | 2520000    | 983000   | 1.34       | 3377000    | 2003 |
| AZ    | 32000    | 55       | 1760000    | 774000   | 1.11       | 1954000    | 2004 |
| AZ    | 36000    | 50       | 1800000    | 720000   | 1.04       | 1872000    | 2005 |
| AZ    | 30000    | 65       | 1950000    | 839000   | 0.91       | 1775000    | 2006 |
| AZ    | 30000    | 64       | 1920000    | 902000   | 1.26       | 2419000    | 2007 |
| AZ    | 25000    | 64       | 1600000    | 336000   | 1.26       | 2016000    | 2008 |
| AZ    | 20000    | 52       | 1040000    | 562000   | 1.45       | 1508000    | 2009 |
| AZ    | 24000    | 77       | 1848000    | 665000   | 1.52       | 2809000    | 2010 |
| AZ    | 23000    | 53       | 1219000    | 427000   | 1.55       | 1889000    | 2011 |
| AZ    | 22000    | 46       | 1012000    | 253000   | 1.79       | 1811000    | 2012 |

另一種視覺化這種演變的方法是使用大小而非顏色。對於色盲用戶，這可能是一個更好的選擇。編輯您的視覺化，通過點的圓周大小來展示價格的增長：

```r
ggplot(honey, aes(x = priceperlb, y = state)) +
  geom_point(aes(size = year),colour = "blue") +
  scale_size_continuous(range = c(0.25, 3))
```
您可以看到點的大小逐漸增大。

![散點圖 3](../../../../../3-Data-Visualization/R/12-visualization-relationships/images/scatter3.png)

這是否是一個簡單的供需問題？由於氣候變化和蜂群崩潰等因素，是否每年可供購買的蜂蜜減少，因此價格上漲？

為了探索數據集中某些變量之間的相關性，讓我們來看看一些折線圖。

## 折線圖

問題：蜂蜜每磅價格是否逐年明顯上漲？您可以通過創建一個單一折線圖來最簡單地發現這一點：

```r
qplot(honey$year,honey$priceperlb, geom='smooth', span =0.5, xlab = "year",ylab = "priceperlb")
```
答案：是的，但在2003年左右有一些例外：

![折線圖 1](../../../../../3-Data-Visualization/R/12-visualization-relationships/images/line1.png)

問題：那麼在2003年，我們是否也能看到蜂蜜供應的激增？如果您查看逐年總產量呢？

```python
qplot(honey$year,honey$totalprod, geom='smooth', span =0.5, xlab = "year",ylab = "totalprod")
```

![折線圖 2](../../../../../3-Data-Visualization/R/12-visualization-relationships/images/line2.png)

答案：並不完全。如果您查看總產量，實際上在那一年似乎有所增加，儘管總體而言，蜂蜜的生產量在這些年中呈下降趨勢。

問題：在這種情況下，2003年蜂蜜價格激增的原因可能是什麼？

為了探索這一點，您可以使用分面網格。

## 分面網格

分面網格可以選擇數據集的一個方面（在我們的例子中，您可以選擇“年份”，以避免生成過多的分面）。Seaborn 可以根據您選擇的 x 和 y 坐標為每個分面生成一個圖表，方便比較。2003年是否在這種比較中脫穎而出？

使用 `facet_wrap` 創建分面網格，這是 [ggplot2 文檔](https://ggplot2.tidyverse.org/reference/facet_wrap.html) 推薦的方法。

```r
ggplot(honey, aes(x=yieldpercol, y = numcol,group = 1)) + 
  geom_line() + facet_wrap(vars(year))
```
在此視覺化中，您可以比較逐年每群產量和蜂群數量，並將列的分面設置為3：

![分面網格](../../../../../3-Data-Visualization/R/12-visualization-relationships/images/facet.png)

對於此數據集，逐年和逐州的蜂群數量及其產量並未顯示出特別突出的變化。是否有其他方式可以找到這兩個變量之間的相關性？

## 雙折線圖

嘗試使用 R 的 `par` 和 `plot` 函數創建多折線圖，將兩個折線圖疊加在一起。我們將在 x 軸上繪製年份，並顯示兩個 y 軸。展示每群產量和蜂群數量的疊加：

```r
par(mar = c(5, 4, 4, 4) + 0.3)              
plot(honey$year, honey$numcol, pch = 16, col = 2,type="l")              
par(new = TRUE)                             
plot(honey$year, honey$yieldpercol, pch = 17, col = 3,              
     axes = FALSE, xlab = "", ylab = "",type="l")
axis(side = 4, at = pretty(range(y2)))      
mtext("colony yield", side = 4, line = 3)   
```
![疊加折線圖](../../../../../3-Data-Visualization/R/12-visualization-relationships/images/dual-line.png)

雖然在2003年並未有明顯的異常，但這讓我們可以以一個稍微樂觀的結論結束本課：儘管蜂群數量總體上在下降，但蜂群數量正在穩定，即使每群產量在減少。

加油，蜜蜂們，加油！

🐝❤️
## 🚀 挑戰

在本課中，您學到了更多關於散點圖和折線網格的其他用途，包括分面網格。挑戰自己使用不同的數據集創建分面網格，也許是您之前使用過的數據集。注意它們的生成時間以及需要小心處理的分面數量。

## [課後測驗](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/23)

## 回顧與自學

折線圖可以是簡單的，也可以是非常複雜的。閱讀 [ggplot2 文檔](https://ggplot2.tidyverse.org/reference/geom_path.html#:~:text=geom_line()%20connects%20them%20in,which%20cases%20are%20connected%20together)，了解構建折線圖的各種方法。嘗試使用文檔中列出的其他方法來增強您在本課中構建的折線圖。

## 作業

[深入蜂巢](assignment.md)

**免責聲明**：  
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原文文件作為權威來源。對於關鍵資訊，建議尋求專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤讀概不負責。