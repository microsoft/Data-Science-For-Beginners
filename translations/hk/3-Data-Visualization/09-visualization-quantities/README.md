<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "43c402d9d90ae6da55d004519ada5033",
  "translation_date": "2025-08-24T14:04:59+00:00",
  "source_file": "3-Data-Visualization/09-visualization-quantities/README.md",
  "language_code": "hk"
}
-->
# 可視化數量

|![由 [(@sketchthedocs)](https://sketchthedocs.dev) 繪製的速記筆記](../../sketchnotes/09-Visualizing-Quantities.png)|
|:---:|
| 可視化數量 - _速記筆記由 [@nitya](https://twitter.com/nitya) 繪製_ |

在這節課中，你將探索如何使用眾多可用的 Python 庫之一，學習如何圍繞數量的概念創建有趣的可視化。使用一個關於明尼蘇達州鳥類的清理過的數據集，你可以了解許多關於當地野生動物的有趣事實。

## [課前測驗](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/16)

## 使用 Matplotlib 觀察翼展

[Matplotlib](https://matplotlib.org/stable/index.html) 是一個非常出色的庫，可以用來創建各種簡單和複雜的圖表和圖形。一般來說，使用這些庫繪製數據的過程包括：識別你想要針對的數據框部分，對數據進行必要的轉換，分配其 x 和 y 軸值，決定顯示哪種類型的圖表，然後顯示圖表。Matplotlib 提供了多種可視化方式，但在這節課中，我們將重點放在最適合可視化數量的圖表上：折線圖、散點圖和柱狀圖。

> ✅ 根據數據的結構和你想要講述的故事，選擇最合適的圖表。
> - 分析時間趨勢：折線圖
> - 比較數值：柱狀圖、條形圖、餅圖、散點圖
> - 顯示部分與整體的關係：餅圖
> - 顯示數據分佈：散點圖、柱狀圖
> - 顯示趨勢：折線圖、條形圖
> - 顯示數值之間的關係：折線圖、散點圖、氣泡圖

如果你有一個數據集，需要了解某個項目的數量，第一步通常是檢查其值。

✅ Matplotlib 有非常好的「速查表」，可以在[這裡](https://matplotlib.org/cheatsheets/cheatsheets.pdf)找到。

## 建立鳥類翼展值的折線圖

打開本課文件夾根目錄中的 `notebook.ipynb` 文件，並添加一個單元格。

> 注意：數據存儲在此倉庫的根目錄 `/data` 文件夾中。

```python
import pandas as pd
import matplotlib.pyplot as plt
birds = pd.read_csv('../../data/birds.csv')
birds.head()
```
這些數據是文本和數字的混合：

|      | 名稱                         | 學名                   | 類別                  | 目            | 科       | 屬          | 保育狀況           | 最小長度 | 最大長度 | 最小體重   | 最大體重   | 最小翼展   | 最大翼展   |
| ---: | :--------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :----------------- | --------: | --------: | ----------: | ----------: | ----------: | ----------: |
|    0 | 黑腹樹鴨                     | Dendrocygna autumnalis | 鴨/鵝/水禽            | 雁形目       | 鴨科     | 樹鴨屬      | LC                 |        47 |        56 |         652 |        1020 |          76 |          94 |
|    1 | 棕樹鴨                       | Dendrocygna bicolor    | 鴨/鵝/水禽            | 雁形目       | 鴨科     | 樹鴨屬      | LC                 |        45 |        53 |         712 |        1050 |          85 |          93 |
|    2 | 雪鵝                         | Anser caerulescens     | 鴨/鵝/水禽            | 雁形目       | 鴨科     | 雁屬        | LC                 |        64 |        79 |        2050 |        4050 |         135 |         165 |
|    3 | 羅斯鵝                       | Anser rossii           | 鴨/鵝/水禽            | 雁形目       | 鴨科     | 雁屬        | LC                 |      57.3 |        64 |        1066 |        1567 |         113 |         116 |
|    4 | 大白額雁                     | Anser albifrons        | 鴨/鵝/水禽            | 雁形目       | 鴨科     | 雁屬        | LC                 |        64 |        81 |        1930 |        3310 |         130 |         165 |

讓我們開始使用基本折線圖繪製一些數字數據。假設你想查看這些有趣鳥類的最大翼展。

```python
wingspan = birds['MaxWingspan'] 
wingspan.plot()
```
![最大翼展](../../../../3-Data-Visualization/09-visualization-quantities/images/max-wingspan-02.png)

你立即注意到什麼？似乎至少有一個異常值——這是一個相當大的翼展！2300 厘米的翼展相當於 23 米——明尼蘇達州有翼龍在飛翔嗎？讓我們調查一下。

雖然你可以在 Excel 中快速排序找到這些異常值（可能是錯誤），但繼續從圖表內部進行可視化處理。

在 x 軸上添加標籤以顯示涉及哪些鳥類：

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

即使將標籤旋轉設置為 45 度，仍然太多以至於無法閱讀。讓我們嘗試另一種策略：僅標記那些異常值，並在圖表內設置標籤。你可以使用散點圖來為標籤留出更多空間：

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
這裡發生了什麼？你使用 `tick_params` 隱藏底部標籤，然後對你的鳥類數據集進行循環。通過使用 `bo` 繪製帶有小圓形藍點的圖表，你檢查了任何最大翼展超過 500 的鳥類，並在點旁邊顯示其標籤。你在 y 軸上稍微偏移標籤 (`y * (1 - 0.05)`)，並使用鳥類名稱作為標籤。

你發現了什麼？

![異常值](../../../../3-Data-Visualization/09-visualization-quantities/images/labeled-wingspan-02.png)

## 篩選數據

禿鷹和草原隼，雖然可能是非常大的鳥類，但似乎被錯誤標記了，其最大翼展多加了一個 `0`。不太可能遇到翼展 25 米的禿鷹，但如果真的遇到，請告訴我們！讓我們創建一個新的數據框，去掉這兩個異常值：

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

通過篩選掉異常值，你的數據現在更加一致且易於理解。

![翼展散點圖](../../../../3-Data-Visualization/09-visualization-quantities/images/scatterplot-wingspan-02.png)

現在我們至少在翼展方面有一個更乾淨的數據集，讓我們了解更多關於這些鳥類的信息。

雖然折線圖和散點圖可以顯示數據值及其分佈的信息，但我們想要思考這個數據集中固有的值。你可以創建可視化來回答以下關於數量的問題：

> 有多少類別的鳥類？它們的數量是多少？
> 有多少鳥類是滅絕、瀕危、稀有或常見的？
> 根據林奈的術語，有多少屬和目？

## 探索柱狀圖

當你需要顯示數據分組時，柱狀圖非常實用。讓我們探索這個數據集中存在的鳥類類別，看看哪一類最常見。

在 notebook 文件中，創建一個基本柱狀圖。

✅ 注意，你可以篩選掉我們在上一節中識別的兩隻異常鳥類，編輯它們的翼展錯誤，或者保留它們，因為這些練習不依賴於翼展值。

如果你想創建柱狀圖，可以選擇你想要關注的數據。柱狀圖可以從原始數據創建：

```python
birds.plot(x='Category',
        kind='bar',
        stacked=True,
        title='Birds of Minnesota')

```
![完整數據柱狀圖](../../../../3-Data-Visualization/09-visualization-quantities/images/full-data-bar-02.png)

然而，這個柱狀圖不可讀，因為有太多未分組的數據。你需要選擇你想要繪製的數據，所以讓我們看看基於鳥類類別的長度。

篩選數據以僅包含鳥類的類別。

✅ 注意，你使用 Pandas 管理數據，然後讓 Matplotlib 繪製圖表。

由於有許多類別，你可以垂直顯示此圖表並調整其高度以容納所有數據：

```python
category_count = birds.value_counts(birds['Category'].values, sort=True)
plt.rcParams['figure.figsize'] = [6, 12]
category_count.plot.barh()
```
![類別和長度](../../../../3-Data-Visualization/09-visualization-quantities/images/category-counts-02.png)

這個柱狀圖很好地顯示了每個類別中鳥類的數量。一眼就能看出，這個地區最多的鳥類屬於鴨/鵝/水禽類別。明尼蘇達州是「萬湖之地」，所以這並不令人驚訝！

✅ 嘗試對此數據集進行其他計數。有什麼讓你感到驚訝嗎？

## 比較數據

你可以通過創建新軸嘗試不同的分組數據比較。嘗試比較基於鳥類類別的最大長度：

```python
maxlength = birds['MaxLength']
plt.barh(y=birds['Category'], width=maxlength)
plt.rcParams['figure.figsize'] = [6, 12]
plt.show()
```
![比較數據](../../../../3-Data-Visualization/09-visualization-quantities/images/category-length-02.png)

這裡沒有什麼令人驚訝的：蜂鳥的最大長度最小，而鵜鶘或鵝的最大長度最大。當數據符合邏輯時，這是件好事！

你可以通過疊加數據創建更有趣的柱狀圖可視化。讓我們疊加最小長度和最大長度在給定鳥類類別上：

```python
minLength = birds['MinLength']
maxLength = birds['MaxLength']
category = birds['Category']

plt.barh(category, maxLength)
plt.barh(category, minLength)

plt.show()
```
在這個圖表中，你可以看到每個鳥類類別的最小長度和最大長度範圍。你可以安全地說，根據這些數據，鳥越大，其長度範圍越大。真是有趣！

![疊加值](../../../../3-Data-Visualization/09-visualization-quantities/images/superimposed-02.png)

## 🚀 挑戰

這個鳥類數據集提供了關於特定生態系統中不同類型鳥類的大量信息。在網上搜索，看看你是否能找到其他與鳥類相關的數據集。練習圍繞這些鳥類構建圖表和圖形，發現你之前未曾意識到的事實。

## [課後測驗](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/17)

## 回顧與自學

這第一節課提供了一些關於如何使用 Matplotlib 可視化數量的信息。進一步研究其他用於數據集可視化的方法。[Plotly](https://github.com/plotly/plotly.py) 是我們不會在這些課程中涵蓋的一個工具，看看它能提供什麼。

## 作業

[折線圖、散點圖和柱狀圖](assignment.md)

**免責聲明**：  
本文件已使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原文文件作為權威來源。對於關鍵資訊，建議尋求專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤釋不承擔責任。