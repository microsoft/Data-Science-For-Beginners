<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "43c402d9d90ae6da55d004519ada5033",
  "translation_date": "2025-08-24T14:03:54+00:00",
  "source_file": "3-Data-Visualization/09-visualization-quantities/README.md",
  "language_code": "tw"
}
-->
# 視覺化數量

|![由 [(@sketchthedocs)](https://sketchthedocs.dev) 繪製的手繪筆記](../../sketchnotes/09-Visualizing-Quantities.png)|
|:---:|
| 視覺化數量 - _手繪筆記由 [@nitya](https://twitter.com/nitya) 提供_ |

在本課程中，您將學習如何使用多種可用的 Python 函式庫之一，來創建有趣的視覺化圖表，圍繞數量的概念進行探索。透過一個關於明尼蘇達州鳥類的清理過的數據集，您可以了解許多關於當地野生動物的有趣事實。

## [課前測驗](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/16)

## 使用 Matplotlib 觀察翼展

[Matplotlib](https://matplotlib.org/stable/index.html) 是一個非常出色的函式庫，可以用來創建各種簡單或複雜的圖表和圖形。一般來說，使用這些函式庫繪製數據的過程包括：確定您想要處理的數據框部分，對數據進行必要的轉換，分配 x 和 y 軸的值，決定顯示的圖表類型，然後顯示圖表。Matplotlib 提供了多種視覺化選項，但在本課程中，我們將專注於最適合視覺化數量的圖表類型：折線圖、散點圖和條形圖。

> ✅ 選擇最適合您數據結構和想要講述故事的圖表類型。
> - 分析時間趨勢：折線圖
> - 比較數值：條形圖、柱狀圖、圓餅圖、散點圖
> - 顯示部分與整體的關係：圓餅圖
> - 顯示數據分佈：散點圖、條形圖
> - 顯示趨勢：折線圖、柱狀圖
> - 顯示數值之間的關係：折線圖、散點圖、氣泡圖

如果您有一個數據集並需要了解某個項目的數量，第一步通常是檢查其值。

✅ Matplotlib 有非常好的「速查表」，可以在[這裡](https://matplotlib.org/cheatsheets/cheatsheets.pdf)找到。

## 建立關於鳥類翼展值的折線圖

打開本課程資料夾根目錄中的 `notebook.ipynb` 文件，並新增一個單元格。

> 注意：數據存儲在此倉庫的根目錄中的 `/data` 資料夾中。

```python
import pandas as pd
import matplotlib.pyplot as plt
birds = pd.read_csv('../../data/birds.csv')
birds.head()
```  
這些數據是文字和數字的混合：

|      | 名稱                         | 學名                   | 類別                  | 目          | 科       | 屬         | 保育狀況            | 最小長度 | 最大長度 | 最小體重   | 最大體重   | 最小翼展   | 最大翼展   |
| ---: | :--------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :----------------- | --------: | --------: | ----------: | ----------: | ----------: | ----------: |
|    0 | 黑腹樹鴨                     | Dendrocygna autumnalis | 鴨/鵝/水禽            | 雁形目       | 鴨科     | 樹鴨屬     | LC                 |        47 |        56 |         652 |        1020 |          76 |          94 |
|    1 | 棕樹鴨                       | Dendrocygna bicolor    | 鴨/鵝/水禽            | 雁形目       | 鴨科     | 樹鴨屬     | LC                 |        45 |        53 |         712 |        1050 |          85 |          93 |
|    2 | 雪雁                         | Anser caerulescens     | 鴨/鵝/水禽            | 雁形目       | 鴨科     | 雁屬       | LC                 |        64 |        79 |        2050 |        4050 |         135 |         165 |
|    3 | 羅斯雁                       | Anser rossii           | 鴨/鵝/水禽            | 雁形目       | 鴨科     | 雁屬       | LC                 |      57.3 |        64 |        1066 |        1567 |         113 |         116 |
|    4 | 大白額雁                     | Anser albifrons        | 鴨/鵝/水禽            | 雁形目       | 鴨科     | 雁屬       | LC                 |        64 |        81 |        1930 |        3310 |         130 |         165 |

讓我們從使用基本折線圖繪製一些數值數據開始。假設您想查看這些有趣鳥類的最大翼展。

```python
wingspan = birds['MaxWingspan'] 
wingspan.plot()
```  
![最大翼展](../../../../3-Data-Visualization/09-visualization-quantities/images/max-wingspan-02.png)

您立即注意到什麼？似乎至少有一個異常值——這是一個相當大的翼展！2300 公分的翼展等於 23 公尺——明尼蘇達州有翼龍在飛翔嗎？讓我們調查一下。

雖然您可以在 Excel 中快速排序來找到這些可能是錯誤的異常值，但我們將繼續從圖表中進行視覺化處理。

為 x 軸添加標籤以顯示涉及的鳥類類型：

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
![帶標籤的翼展](../../../../3-Data-Visualization/09-visualization-quantities/images/max-wingspan-labels-02.png)

即使將標籤旋轉設置為 45 度，仍然太多而無法閱讀。我們嘗試另一種策略：僅標記那些異常值，並將標籤設置在圖表內。您可以使用散點圖來為標籤騰出更多空間：

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
這裡發生了什麼？您使用 `tick_params` 隱藏了底部標籤，然後對鳥類數據集進行了一個循環。通過使用 `bo` 繪製帶有小藍點的圖表，您檢查了任何最大翼展超過 500 的鳥類，並在點旁邊顯示其標籤。您在 y 軸上稍微偏移了標籤 (`y * (1 - 0.05)`)，並使用鳥類名稱作為標籤。

您發現了什麼？

![異常值](../../../../3-Data-Visualization/09-visualization-quantities/images/labeled-wingspan-02.png)

## 篩選數據

禿鷹和草原隼，雖然可能是非常大的鳥類，但似乎被錯誤標記了，其最大翼展多了一個 `0`。不太可能遇到翼展 25 公尺的禿鷹，但如果有，請告訴我們！讓我們創建一個新的數據框，去除這兩個異常值：

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

通過篩選掉異常值，您的數據現在更加一致且易於理解。

![翼展散點圖](../../../../3-Data-Visualization/09-visualization-quantities/images/scatterplot-wingspan-02.png)

現在我們至少在翼展方面有了一個更乾淨的數據集，讓我們進一步探索這些鳥類。

雖然折線圖和散點圖可以顯示數據值及其分佈的信息，但我們想要思考這個數據集中固有的數值。您可以創建視覺化圖表來回答以下關於數量的問題：

> 有多少類別的鳥類？它們的數量是多少？  
> 有多少鳥類是滅絕、瀕危、稀有或常見的？  
> 根據林奈分類法，有多少屬和目？  

## 探索條形圖

當您需要顯示數據分組時，條形圖非常實用。讓我們探索這個數據集中存在的鳥類類別，看看哪一類最常見。

在 notebook 文件中，創建一個基本條形圖。

✅ 注意，您可以選擇篩選掉我們在上一節中識別的兩隻異常鳥類，編輯其翼展中的錯誤，或者將它們保留在這些不依賴翼展值的練習中。

如果您想創建條形圖，可以選擇您想要關注的數據。條形圖可以從原始數據創建：

```python
birds.plot(x='Category',
        kind='bar',
        stacked=True,
        title='Birds of Minnesota')

```  
![完整數據條形圖](../../../../3-Data-Visualization/09-visualization-quantities/images/full-data-bar-02.png)

然而，這個條形圖因為數據未分組而難以閱讀。您需要僅選擇您想要繪製的數據，因此讓我們根據鳥類的類別來查看其數量。

篩選數據以僅包含鳥類的類別。

✅ 注意，您使用 Pandas 管理數據，然後讓 Matplotlib 繪製圖表。

由於類別很多，您可以垂直顯示此圖表，並調整其高度以適應所有數據：

```python
category_count = birds.value_counts(birds['Category'].values, sort=True)
plt.rcParams['figure.figsize'] = [6, 12]
category_count.plot.barh()
```  
![類別與數量](../../../../3-Data-Visualization/09-visualization-quantities/images/category-counts-02.png)

這個條形圖很好地展示了每個類別中鳥類的數量。一眼就能看出，這個地區最多的鳥類是鴨/鵝/水禽類別。明尼蘇達州是「萬湖之地」，所以這並不令人驚訝！

✅ 嘗試對此數據集進行其他計數。有什麼讓您感到驚訝嗎？

## 比較數據

您可以通過創建新軸嘗試不同的分組數據比較。嘗試比較鳥類的最大長度，基於其類別：

```python
maxlength = birds['MaxLength']
plt.barh(y=birds['Category'], width=maxlength)
plt.rcParams['figure.figsize'] = [6, 12]
plt.show()
```  
![比較數據](../../../../3-Data-Visualization/09-visualization-quantities/images/category-length-02.png)

這裡沒有什麼令人驚訝的：蜂鳥的最大長度最小，而鵜鶘或鵝的最大長度最大。當數據符合邏輯時，這是一件好事！

您可以通過疊加數據來創建更有趣的條形圖視覺化效果。讓我們將最小長度和最大長度疊加在給定的鳥類類別上：

```python
minLength = birds['MinLength']
maxLength = birds['MaxLength']
category = birds['Category']

plt.barh(category, maxLength)
plt.barh(category, minLength)

plt.show()
```  
在這個圖表中，您可以看到每個鳥類類別的最小長度和最大長度範圍。可以肯定地說，根據這些數據，鳥越大，其長度範圍越大。真是令人著迷！

![疊加值](../../../../3-Data-Visualization/09-visualization-quantities/images/superimposed-02.png)

## 🚀 挑戰

這個鳥類數據集提供了關於特定生態系統中不同類型鳥類的大量信息。在網路上搜尋其他與鳥類相關的數據集，練習圍繞這些鳥類構建圖表和圖形，發現您之前未曾了解的事實。

## [課後測驗](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/17)

## 回顧與自學

這第一課為您提供了一些關於如何使用 Matplotlib 視覺化數量的資訊。進一步研究其他用於數據視覺化的方法。[Plotly](https://github.com/plotly/plotly.py) 是我們不會在這些課程中涵蓋的一個工具，請查看它能提供什麼功能。

## 作業

[折線圖、散點圖和條形圖](assignment.md)

**免責聲明**：  
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原始語言的文件作為權威來源。對於關鍵資訊，建議尋求專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋概不負責。