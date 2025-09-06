<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "22acf28f518a4769ea14fa42f4734b9f",
  "translation_date": "2025-08-25T18:22:36+00:00",
  "source_file": "3-Data-Visualization/R/09-visualization-quantities/README.md",
  "language_code": "hk"
}
-->
# 視覺化數量
|![由 [(@sketchthedocs)](https://sketchthedocs.dev) 繪製的速記筆記](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/sketchnotes/09-Visualizing-Quantities.png)|
|:---:|
| 視覺化數量 - _由 [@nitya](https://twitter.com/nitya) 繪製的速記筆記_ |

在這節課中，你將探索如何使用一些 R 套件庫來學習如何圍繞數量概念創建有趣的視覺化。使用一個關於明尼蘇達州鳥類的清理過的數據集，你可以了解許多關於當地野生動物的有趣事實。
## [課前測驗](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/16)

## 使用 ggplot2 觀察翼展
一個非常出色的庫是 [ggplot2](https://cran.r-project.org/web/packages/ggplot2/index.html)，它可以用來創建各種簡單和複雜的圖表。一般來說，使用這些庫繪製數據的過程包括：識別你想要針對的數據框部分，對數據進行必要的轉換，分配 x 和 y 軸的值，決定要顯示的圖表類型，然後顯示圖表。

`ggplot2` 是一個基於圖形語法（Grammar of Graphics）聲明式創建圖形的系統。[圖形語法](https://en.wikipedia.org/wiki/Ggplot2) 是一種數據視覺化的通用方案，它將圖表分解為語義組件，例如比例和層次。換句話說，`ggplot2` 使得用少量代碼為單變量或多變量數據創建圖表和圖形變得非常容易，因此成為 R 中最受歡迎的視覺化套件。用戶告訴 `ggplot2` 如何將變量映射到美學屬性，使用哪些圖形原語，然後 `ggplot2` 負責其餘部分。

> ✅ 圖表 = 數據 + 美學 + 幾何
> - 數據指的是數據集
> - 美學表示要研究的變量（x 和 y 變量）
> - 幾何指的是圖表類型（折線圖、柱狀圖等）

根據你的數據和你想通過圖表講述的故事，選擇最合適的幾何（圖表類型）。

> - 分析趨勢：折線圖、柱狀圖
> - 比較數值：條形圖、柱狀圖、餅圖、散點圖
> - 顯示部分與整體的關係：餅圖
> - 顯示數據分佈：散點圖、柱狀圖
> - 顯示數值之間的關係：折線圖、散點圖、氣泡圖

✅ 你也可以查看這份描述性的 [ggplot2 速查表](https://nyu-cdsc.github.io/learningr/assets/data-visualization-2.1.pdf)。

## 建立鳥類翼展值的折線圖

打開 R 控制台並導入數據集。
> 注意：數據集存儲在此倉庫的 `/data` 文件夾中。

讓我們導入數據集並觀察數據的頭部（前 5 行）。

```r
birds <- read.csv("../../data/birds.csv",fileEncoding="UTF-8-BOM")
head(birds)
```
數據的頭部包含文本和數字的混合：

|      | 名稱                         | 學名                   | 類別                  | 目          | 科       | 屬         | 保育狀況             | 最小長度 | 最大長度 | 最小體重   | 最大體重   | 最小翼展   | 最大翼展   |
| ---: | :--------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :----------------- | --------: | --------: | ----------: | ----------: | ----------: | ----------: |
|    0 | 黑腹吹哨鴨                   | Dendrocygna autumnalis | 鴨/鵝/水禽            | 雁形目       | 鴨科     | 吹哨鴨屬   | LC                 |        47 |        56 |         652 |        1020 |          76 |          94 |
|    1 | 棕吹哨鴨                     | Dendrocygna bicolor    | 鴨/鵝/水禽            | 雁形目       | 鴨科     | 吹哨鴨屬   | LC                 |        45 |        53 |         712 |        1050 |          85 |          93 |
|    2 | 雪鵝                         | Anser caerulescens     | 鴨/鵝/水禽            | 雁形目       | 鴨科     | 雁屬       | LC                 |        64 |        79 |        2050 |        4050 |         135 |         165 |
|    3 | 羅斯鵝                       | Anser rossii           | 鴨/鵝/水禽            | 雁形目       | 鴨科     | 雁屬       | LC                 |      57.3 |        64 |        1066 |        1567 |         113 |         116 |
|    4 | 大白額鵝                     | Anser albifrons        | 鴨/鵝/水禽            | 雁形目       | 鴨科     | 雁屬       | LC                 |        64 |        81 |        1930 |        3310 |         130 |         165 |

讓我們開始使用基本折線圖繪製一些數字數據。假設你想查看這些有趣鳥類的最大翼展。

```r
install.packages("ggplot2")
library("ggplot2")
ggplot(data=birds, aes(x=Name, y=MaxWingspan,group=1)) +
  geom_line() 
```
在這裡，你安裝了 `ggplot2` 套件，然後使用 `library("ggplot2")` 命令將其導入工作空間。要在 ggplot 中繪製任何圖表，使用 `ggplot()` 函數並指定數據集、x 和 y 變量作為屬性。在這種情況下，我們使用 `geom_line()` 函數，因為我們的目標是繪製折線圖。

![MaxWingspan-lineplot](../../../../../translated_images/MaxWingspan-lineplot.b12169f99d26fdd263f291008dfd73c18a4ba8f3d32b1fda3d74af51a0a28616.hk.png)

你立即注意到什麼？似乎至少有一個異常值——那是一個相當大的翼展！2000+ 厘米的翼展超過 20 米——明尼蘇達州有翼龍在飛嗎？讓我們調查一下。

雖然你可以在 Excel 中快速排序以找到那些異常值（可能是輸入錯誤），但繼續從圖表內部進行視覺化處理。

為 x 軸添加標籤以顯示涉及哪些鳥類：

```r
ggplot(data=birds, aes(x=Name, y=MaxWingspan,group=1)) +
  geom_line() +
  theme(axis.text.x = element_text(angle = 45, hjust=1))+
  xlab("Birds") +
  ylab("Wingspan (CM)") +
  ggtitle("Max Wingspan in Centimeters")
```
我們在 `theme` 中指定角度，並在 `xlab()` 和 `ylab()` 中分別指定 x 和 y 軸標籤。`ggtitle()` 為圖表/圖形命名。

![MaxWingspan-lineplot-improved](../../../../../translated_images/MaxWingspan-lineplot-improved.04b73b4d5a59552a6bc7590678899718e1f065abe9eada9ebb4148939b622fd4.hk.png)

即使將標籤的旋轉設置為 45 度，仍然有太多標籤難以閱讀。讓我們嘗試另一種策略：僅標記那些異常值並在圖表內設置標籤。你可以使用散點圖來為標籤留出更多空間：

```r
ggplot(data=birds, aes(x=Name, y=MaxWingspan,group=1)) +
  geom_point() +
  geom_text(aes(label=ifelse(MaxWingspan>500,as.character(Name),'')),hjust=0,vjust=0) + 
  theme(axis.title.x=element_blank(), axis.text.x=element_blank(), axis.ticks.x=element_blank())
  ylab("Wingspan (CM)") +
  ggtitle("Max Wingspan in Centimeters") + 
```
這裡發生了什麼？你使用 `geom_point()` 函數繪製散點。通過這個，你為 `MaxWingspan > 500` 的鳥類添加了標籤，並隱藏了 x 軸上的標籤以減少圖表的混亂。

你發現了什麼？

![MaxWingspan-scatterplot](../../../../../translated_images/MaxWingspan-scatterplot.60dc9e0e19d32700283558f253841fdab5104abb62bc96f7d97f9c0ee857fa8b.hk.png)

## 篩選數據

禿鷹和草原隼，雖然可能是非常大的鳥類，但似乎被錯誤標記了，最大翼展多了一個 0。遇到翼展 25 米的禿鷹的可能性不大，但如果真的遇到，請告訴我們！讓我們創建一個新的數據框，去掉這兩個異常值：

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
我們創建了一個新的數據框 `birds_filtered`，然後繪製了一個散點圖。通過篩選掉異常值，你的數據現在更加一致且易於理解。

![MaxWingspan-scatterplot-improved](../../../../../translated_images/MaxWingspan-scatterplot-improved.7d0af81658c65f3e75b8fedeb2335399e31108257e48db15d875ece608272051.hk.png)

現在我們至少在翼展方面有了一個更乾淨的數據集，讓我們了解更多關於這些鳥類的信息。

雖然折線圖和散點圖可以顯示數據值及其分佈的信息，但我們想要思考這個數據集中固有的數值。你可以創建視覺化來回答以下關於數量的問題：

> 有多少類別的鳥類？它們的數量是多少？
> 有多少鳥類是滅絕的、瀕危的、稀有的或常見的？
> 根據林奈的術語，有多少屬和目？

## 探索條形圖

當你需要顯示數據分組時，條形圖非常實用。讓我們探索這個數據集中存在的鳥類類別，看看哪一類最常見。

讓我們在篩選後的數據上創建一個條形圖。

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
在以下代碼片段中，我們安裝了 [dplyr](https://www.rdocumentation.org/packages/dplyr/versions/0.7.8) 和 [lubridate](https://www.rdocumentation.org/packages/lubridate/versions/1.8.0) 套件，以幫助操作和分組數據以繪製堆疊條形圖。首先，你按鳥類的 `Category` 分組數據，然後總結 `MinLength`、`MaxLength`、`MinBodyMass`、`MaxBodyMass`、`MinWingspan`、`MaxWingspan` 列。然後，使用 `ggplot2` 套件繪製條形圖並指定不同類別的顏色和標籤。

![堆疊條形圖](../../../../../translated_images/stacked-bar-chart.0c92264e89da7b391a7490224d1e7059a020e8b74dcd354414aeac78871c02f1.hk.png)

然而，這個條形圖難以閱讀，因為有太多未分組的數據。你需要選擇你想要繪製的數據，所以讓我們看看基於鳥類類別的鳥類長度。

篩選數據以僅包含鳥類的類別。

由於有許多類別，你可以垂直顯示此圖表並調整其高度以容納所有數據：

```r
birds_count<-dplyr::count(birds_filtered, Category, sort = TRUE)
birds_count$Category <- factor(birds_count$Category, levels = birds_count$Category)
ggplot(birds_count,aes(Category,n))+geom_bar(stat="identity")+coord_flip()
```
你首先計算 `Category` 列中的唯一值，然後將它們排序到一個新的數據框 `birds_count` 中。這些排序後的數據在相同層次中進行分級，以便按排序方式繪製。使用 `ggplot2`，你然後在條形圖中繪製數據。`coord_flip()` 繪製水平條形圖。

![類別-長度](../../../../../translated_images/category-length.7e34c296690e85d64f7e4d25a56077442683eca96c4f5b4eae120a64c0755636.hk.png)

這個條形圖很好地展示了每個類別中鳥類的數量。一眼就能看出，在這個地區最多的鳥類是鴨/鵝/水禽類別。明尼蘇達州是“萬湖之地”，所以這並不令人驚訝！

✅ 嘗試對此數據集進行其他計數。有什麼讓你感到驚訝嗎？

## 比較數據

你可以通過創建新的軸嘗試不同的分組數據比較。嘗試比較基於鳥類類別的最大長度：

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
我們按 `Category` 分組 `birds_filtered` 數據，然後繪製條形圖。

![比較數據](../../../../../translated_images/comparingdata.f486a450d61c7ca5416f27f3f55a6a4465d00df3be5e6d33936e9b07b95e2fdd.hk.png)

這裡沒有什麼令人驚訝的：蜂鳥的最大長度比鵜鶘或鵝要小得多。當數據符合邏輯時，這是件好事！

你可以通過疊加數據創建更有趣的條形圖視覺化。讓我們在給定的鳥類類別上疊加最小和最大長度：

```r
ggplot(data=birds_grouped, aes(x=Category)) +
  geom_bar(aes(y=MaxLength), stat="identity", position ="identity",  fill='blue') +
  geom_bar(aes(y=MinLength), stat="identity", position="identity", fill='orange')+
  coord_flip()
```
![疊加值](../../../../../translated_images/superimposed-values.5363f0705a1da4167625a373a1064331ea3cb7a06a297297d0734fcc9b3819a0.hk.png)

## 🚀 挑戰

這個鳥類數據集提供了大量關於特定生態系統中不同類型鳥類的信息。在網上搜索，看看你是否能找到其他與鳥類相關的數據集。練習圍繞這些鳥類構建圖表和圖形，發現你之前未曾意識到的事實。
## [課後測驗](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/17)

## 回顧與自學

這第一節課提供了一些關於如何使用 `ggplot2` 視覺化數量的信息。進行一些研究，了解其他方法來處理數據集進行視覺化。研究並尋找可以使用其他套件（如 [Lattice](https://stat.ethz.ch/R-manual/R-devel/library/lattice/html/Lattice.html) 和 [Plotly](https://github.com/plotly/plotly.R#readme)）進行視覺化的數據集。

## 作業
[折線圖、散點圖和條形圖](assignment.md)

**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。原始語言的文件應被視為權威來源。對於重要資訊，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋概不負責。