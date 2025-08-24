<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "af6a12015c6e250e500b570a9fa42593",
  "translation_date": "2025-08-24T14:08:37+00:00",
  "source_file": "3-Data-Visualization/11-visualization-proportions/README.md",
  "language_code": "hk"
}
-->
# 視覺化比例

|![由 [(@sketchthedocs)](https://sketchthedocs.dev) 繪製的速記筆記](../../sketchnotes/11-Visualizing-Proportions.png)|
|:---:|
|視覺化比例 - _由 [@nitya](https://twitter.com/nitya) 繪製的速記筆記_ |

在這節課中，你將使用一個以自然為主題的數據集來視覺化比例，例如在一個關於蘑菇的數據集中有多少不同種類的真菌。讓我們使用一個來自 Audubon 的數據集來探索這些迷人的真菌，該數據集列出了 Agaricus 和 Lepiota 家族中 23 種有鰓蘑菇的詳細信息。你將嘗試一些有趣的視覺化方式，例如：

- 餅圖 🥧  
- 圓環圖 🍩  
- 格子圖 🧇  

> 💡 微軟研究的一個非常有趣的項目 [Charticulator](https://charticulator.com) 提供了一個免費的拖放界面來進行數據視覺化。在他們的一個教程中也使用了這個蘑菇數據集！因此，你可以同時探索數據並學習這個庫：[Charticulator 教程](https://charticulator.com/tutorials/tutorial4.html)。

## [課前測驗](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/20)

## 認識你的蘑菇 🍄

蘑菇非常有趣。讓我們導入一個數據集來研究它們：

```python
import pandas as pd
import matplotlib.pyplot as plt
mushrooms = pd.read_csv('../../data/mushrooms.csv')
mushrooms.head()
```  
一個表格被打印出來，包含一些很棒的分析數據：

| 類別       | 菌蓋形狀 | 菌蓋表面 | 菌蓋顏色 | 是否有瘀傷 | 氣味    | 鰓附著方式     | 鰓間距      | 鰓大小   | 鰓顏色   | 菌柄形狀   | 菌柄根部 | 菌柄環上表面          | 菌柄環下表面          | 菌柄環上顏色          | 菌柄環下顏色          | 菌幕類型 | 菌幕顏色 | 環數量     | 環類型   | 孢子印顏色       | 分布情況   | 棲息地   |
| --------- | --------- | --------- | --------- | --------- | ------- | --------------- | ------------ | --------- | ---------- | ----------- | ---------- | ------------------------ | ------------------------ | ---------------------- | ---------------------- | --------- | ---------- | ----------- | --------- | ----------------- | ---------- | ------- |
| 有毒       | 凸形      | 光滑      | 棕色      | 有瘀傷    | 刺鼻    | 自由            | 緊密        | 狹窄     | 黑色      | 擴大       | 等長      | 光滑                   | 光滑                   | 白色                  | 白色                  | 部分      | 白色      | 一個       | 垂懸     | 黑色             | 分散       | 城市     |
| 可食用     | 凸形      | 光滑      | 黃色      | 有瘀傷    | 杏仁味  | 自由            | 緊密        | 寬廣     | 黑色      | 擴大       | 棍狀      | 光滑                   | 光滑                   | 白色                  | 白色                  | 部分      | 白色      | 一個       | 垂懸     | 棕色             | 數量多     | 草地     |
| 可食用     | 鐘形      | 光滑      | 白色      | 有瘀傷    | 茴香味  | 自由            | 緊密        | 寬廣     | 棕色      | 擴大       | 棍狀      | 光滑                   | 光滑                   | 白色                  | 白色                  | 部分      | 白色      | 一個       | 垂懸     | 棕色             | 數量多     | 草原     |
| 有毒       | 凸形      | 鱗片狀    | 白色      | 有瘀傷    | 刺鼻    | 自由            | 緊密        | 狹窄     | 棕色      | 擴大       | 等長      | 光滑                   | 光滑                   | 白色                  | 白色                  | 部分      | 白色      | 一個       | 垂懸     | 黑色             | 分散       | 城市     |

你會立刻注意到所有的數據都是文本格式。你需要將這些數據轉換才能在圖表中使用。事實上，大部分數據是以對象形式表示的：

```python
print(mushrooms.select_dtypes(["object"]).columns)
```  

輸出為：

```output
Index(['class', 'cap-shape', 'cap-surface', 'cap-color', 'bruises', 'odor',
       'gill-attachment', 'gill-spacing', 'gill-size', 'gill-color',
       'stalk-shape', 'stalk-root', 'stalk-surface-above-ring',
       'stalk-surface-below-ring', 'stalk-color-above-ring',
       'stalk-color-below-ring', 'veil-type', 'veil-color', 'ring-number',
       'ring-type', 'spore-print-color', 'population', 'habitat'],
      dtype='object')
```  
將這些數據轉換，將 '類別' 列轉換為分類：

```python
cols = mushrooms.select_dtypes(["object"]).columns
mushrooms[cols] = mushrooms[cols].astype('category')
```  

```python
edibleclass=mushrooms.groupby(['class']).count()
edibleclass
```  

現在，如果你打印出蘑菇數據，你可以看到它已經根據有毒/可食用類別分組：

|           | 菌蓋形狀 | 菌蓋表面 | 菌蓋顏色 | 是否有瘀傷 | 氣味 | 鰓附著方式     | 鰓間距      | 鰓大小   | 鰓顏色   | 菌柄形狀   | ... | 菌柄環下表面          | 菌柄環上顏色          | 菌柄環下顏色          | 菌幕類型 | 菌幕顏色 | 環數量     | 環類型   | 孢子印顏色       | 分布情況   | 棲息地   |
| --------- | --------- | --------- | --------- | --------- | ---- | --------------- | ------------ | --------- | ---------- | ----------- | --- | ------------------------ | ---------------------- | ---------------------- | --------- | ---------- | ----------- | --------- | ----------------- | ---------- | ------- |
| 類別       |           |           |           |           |      |                 |              |           |            |             |     |                          |                        |                        |           |            |             |           |                   |            |         |
| 可食用     | 4208      | 4208      | 4208      | 4208      | 4208 | 4208            | 4208         | 4208      | 4208       | 4208        | ... | 4208                     | 4208                   | 4208                   | 4208      | 4208       | 4208        | 4208      | 4208              | 4208       | 4208    |
| 有毒       | 3916      | 3916      | 3916      | 3916      | 3916 | 3916            | 3916         | 3916      | 3916       | 3916        | ... | 3916                     | 3916                   | 3916                   | 3916      | 3916       | 3916        | 3916      | 3916              | 3916       | 3916    |

如果你按照這個表格中呈現的順序來創建你的類別標籤，你可以製作一個餅圖：

## 餅圖！

```python
labels=['Edible','Poisonous']
plt.pie(edibleclass['population'],labels=labels,autopct='%.1f %%')
plt.title('Edible?')
plt.show()
```  
完成，一個餅圖展示了根據這兩類蘑菇的數據比例。正確排列標籤的順序非常重要，尤其是在這裡，因此請務必核對標籤數組的順序！

![餅圖](../../../../3-Data-Visualization/11-visualization-proportions/images/pie1-wb.png)

## 圓環圖！

一個更具視覺吸引力的餅圖是圓環圖，它是一個中間有洞的餅圖。讓我們用這種方法來查看數據。

看看蘑菇生長的各種棲息地：

```python
habitat=mushrooms.groupby(['habitat']).count()
habitat
```  
在這裡，你將數據按棲息地分組。共有 7 種棲息地，因此使用它們作為圓環圖的標籤：

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

![圓環圖](../../../../3-Data-Visualization/11-visualization-proportions/images/donut-wb.png)

這段代碼繪製了一個圖表和一個中心圓，然後將該中心圓添加到圖表中。通過更改 `0.40` 的值來編輯中心圓的寬度。

圓環圖可以通過多種方式進行調整以更改標籤。特別是標籤可以被突出顯示以提高可讀性。更多信息請參考 [文檔](https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_and_donut_labels.html?highlight=donut)。

現在你知道如何分組數據並將其顯示為餅圖或圓環圖，你可以探索其他類型的圖表。試試格子圖，這是一種不同的方式來探索數量。

## 格子圖！

格子圖是一種以 2D 方塊陣列視覺化數量的方式。試著視覺化這個數據集中蘑菇菌蓋顏色的不同數量。為此，你需要安裝一個名為 [PyWaffle](https://pypi.org/project/pywaffle/) 的輔助庫並使用 Matplotlib：

```python
pip install pywaffle
```  

選擇一段數據進行分組：

```python
capcolor=mushrooms.groupby(['cap-color']).count()
capcolor
```  

通過創建標籤並分組數據來製作格子圖：

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

使用格子圖，你可以清楚地看到這個蘑菇數據集中菌蓋顏色的比例。有趣的是，有很多綠色菌蓋的蘑菇！

![格子圖](../../../../3-Data-Visualization/11-visualization-proportions/images/waffle.png)

✅ PyWaffle 支持在圖表中使用 [Font Awesome](https://fontawesome.com/) 中的任何圖標。嘗試使用圖標代替方塊來創建更有趣的格子圖。

在這節課中，你學到了三種視覺化比例的方法。首先，你需要將數據分組到分類中，然後決定哪種方式最適合展示數據——餅圖、圓環圖或格子圖。這些方法都很有趣，能讓用戶快速了解數據集。

## 🚀 挑戰

試著在 [Charticulator](https://charticulator.com) 中重現這些有趣的圖表。

## [課後測驗](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/21)

## 回顧與自學

有時候，何時使用餅圖、圓環圖或格子圖並不明顯。以下是一些相關文章：

https://www.beautiful.ai/blog/battle-of-the-charts-pie-chart-vs-donut-chart  

https://medium.com/@hypsypops/pie-chart-vs-donut-chart-showdown-in-the-ring-5d24fd86a9ce  

https://www.mit.edu/~mbarker/formula1/f1help/11-ch-c6.htm  

https://medium.datadriveninvestor.com/data-visualization-done-the-right-way-with-tableau-waffle-chart-fdf2a19be402  

進行一些研究以獲取更多關於這個選擇的資訊。

## 作業

[在 Excel 中試試看](assignment.md)  

**免責聲明**：  
本文件已使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要信息，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋概不負責。