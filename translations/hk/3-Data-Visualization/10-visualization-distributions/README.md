<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "87faccac113d772551486a67a607153e",
  "translation_date": "2025-08-24T13:37:30+00:00",
  "source_file": "3-Data-Visualization/10-visualization-distributions/README.md",
  "language_code": "hk"
}
-->
# 可視化分佈

|![由 [(@sketchthedocs)](https://sketchthedocs.dev) 繪製的速記筆記](../../sketchnotes/10-Visualizing-Distributions.png)|
|:---:|
| 可視化分佈 - _由 [@nitya](https://twitter.com/nitya) 繪製的速記筆記_ |

在上一課中，你學到了一些關於明尼蘇達州鳥類數據集的有趣事實。通過可視化異常值，你發現了一些錯誤的數據，並查看了不同鳥類分類的最大長度差異。

## [課前測驗](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/18)
## 探索鳥類數據集

另一種深入了解數據的方法是查看其分佈，即數據如何沿著某個軸排列。例如，你可能想了解這個數據集中鳥類的最大翼展或最大體重的一般分佈。

讓我們來發現一些關於這個數據集中分佈的事實。在本課文件夾根目錄中的 _notebook.ipynb_ 文件中，導入 Pandas、Matplotlib 和你的數據：

```python
import pandas as pd
import matplotlib.pyplot as plt
birds = pd.read_csv('../../data/birds.csv')
birds.head()
```

|      | 名稱                         | 學名                   | 類別                  | 目            | 科       | 屬          | 保育狀況           | 最小長度 | 最大長度 | 最小體重     | 最大體重     | 最小翼展     | 最大翼展     |
| ---: | :--------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :----------------- | --------: | --------: | ----------: | ----------: | ----------: | ----------: |
|    0 | 黑腹樹鴨                     | Dendrocygna autumnalis | 鴨/鵝/水禽            | 雁形目       | 鴨科     | 樹鴨屬      | LC                 |        47 |        56 |         652 |        1020 |          76 |          94 |
|    1 | 棕樹鴨                       | Dendrocygna bicolor    | 鴨/鵝/水禽            | 雁形目       | 鴨科     | 樹鴨屬      | LC                 |        45 |        53 |         712 |        1050 |          85 |          93 |
|    2 | 雪鵝                         | Anser caerulescens     | 鴨/鵝/水禽            | 雁形目       | 鴨科     | 雁屬        | LC                 |        64 |        79 |        2050 |        4050 |         135 |         165 |
|    3 | 羅斯鵝                       | Anser rossii           | 鴨/鵝/水禽            | 雁形目       | 鴨科     | 雁屬        | LC                 |      57.3 |        64 |        1066 |        1567 |         113 |         116 |
|    4 | 大白額鵝                     | Anser albifrons        | 鴨/鵝/水禽            | 雁形目       | 鴨科     | 雁屬        | LC                 |        64 |        81 |        1930 |        3310 |         130 |         165 |

通常，你可以通過使用散點圖快速查看數據的分佈方式，就像我們在上一課中所做的那樣：

```python
birds.plot(kind='scatter',x='MaxLength',y='Order',figsize=(12,8))

plt.title('Max Length per Order')
plt.ylabel('Order')
plt.xlabel('Max Length')

plt.show()
```
![每個目最大長度](../../../../3-Data-Visualization/10-visualization-distributions/images/scatter-wb.png)

這提供了每個鳥類目身體長度的一般分佈概覽，但這並不是顯示真實分佈的最佳方式。這項任務通常通過創建直方圖來完成。

## 使用直方圖

Matplotlib 提供了非常好的方法來使用直方圖可視化數據分佈。這種類型的圖表類似於柱狀圖，分佈可以通過柱狀的升降來看到。要構建直方圖，你需要數值數據。要構建直方圖，你可以繪製一個圖表，將類型定義為 'hist' 以表示直方圖。此圖表顯示了整個數據集的最大體重分佈。通過將給定的數據數組分成更小的區間，它可以顯示數據值的分佈：

```python
birds['MaxBodyMass'].plot(kind = 'hist', bins = 10, figsize = (12,12))
plt.show()
```
![整個數據集的分佈](../../../../3-Data-Visualization/10-visualization-distributions/images/dist1-wb.png)

如你所見，這個數據集中的 400 多種鳥類大多數的最大體重都在 2000 以下。通過將 `bins` 參數更改為更高的數字，例如 30，可以獲得更多洞察：

```python
birds['MaxBodyMass'].plot(kind = 'hist', bins = 30, figsize = (12,12))
plt.show()
```
![使用更大 bins 參數的分佈](../../../../3-Data-Visualization/10-visualization-distributions/images/dist2-wb.png)

此圖表以更細緻的方式顯示了分佈。通過確保僅選擇給定範圍內的數據，可以創建一個不太偏向左側的圖表：

篩選你的數據以僅獲取體重低於 60 的鳥類，並顯示 40 個 `bins`：

```python
filteredBirds = birds[(birds['MaxBodyMass'] > 1) & (birds['MaxBodyMass'] < 60)]      
filteredBirds['MaxBodyMass'].plot(kind = 'hist',bins = 40,figsize = (12,12))
plt.show()     
```
![篩選後的直方圖](../../../../3-Data-Visualization/10-visualization-distributions/images/dist3-wb.png)

✅ 嘗試其他篩選器和數據點。要查看數據的完整分佈，移除 `['MaxBodyMass']` 篩選器以顯示標籤分佈。

直方圖還提供了一些不錯的顏色和標籤增強功能可以嘗試：

創建一個 2D 直方圖來比較兩個分佈之間的關係。讓我們比較 `MaxBodyMass` 和 `MaxLength`。Matplotlib 提供了一種內置方法來通過更亮的顏色顯示收斂：

```python
x = filteredBirds['MaxBodyMass']
y = filteredBirds['MaxLength']

fig, ax = plt.subplots(tight_layout=True)
hist = ax.hist2d(x, y)
```
似乎這兩個元素沿著預期的軸存在預期的相關性，其中有一個特別強的收斂點：

![2D 圖](../../../../3-Data-Visualization/10-visualization-distributions/images/2D-wb.png)

直方圖默認對數值數據效果很好。如果你需要根據文本數據查看分佈怎麼辦？

## 使用文本數據探索數據集的分佈

此數據集還包括有關鳥類類別及其屬、種、科以及保育狀況的良好信息。讓我們深入了解這些保育信息。根據保育狀況，鳥類的分佈是什麼樣的？

> ✅ 在數據集中，使用了幾個縮寫來描述保育狀況。這些縮寫來自 [IUCN 紅色名錄分類](https://www.iucnredlist.org/)，一個記錄物種狀況的組織。
> 
> - CR: 極危
> - EN: 瀕危
> - EX: 滅絕
> - LC: 無危
> - NT: 近危
> - VU: 易危

這些是基於文本的值，因此你需要進行轉換以創建直方圖。使用篩選後的鳥類數據框，顯示其保育狀況及其最小翼展。你看到了什麼？

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

![翼展和保育狀況的對比](../../../../3-Data-Visualization/10-visualization-distributions/images/histogram-conservation-wb.png)

最小翼展和保育狀況之間似乎沒有良好的相關性。使用此方法測試數據集的其他元素。你也可以嘗試不同的篩選器。你是否發現任何相關性？

## 密度圖

你可能已經注意到，我們到目前為止看到的直方圖是“階梯式”的，並沒有平滑地呈弧形。要顯示更平滑的密度圖，你可以嘗試密度圖。

要使用密度圖，請熟悉一個新的繪圖庫 [Seaborn](https://seaborn.pydata.org/generated/seaborn.kdeplot.html)。

加載 Seaborn，嘗試一個基本的密度圖：

```python
import seaborn as sns
import matplotlib.pyplot as plt
sns.kdeplot(filteredBirds['MinWingspan'])
plt.show()
```
![密度圖](../../../../3-Data-Visualization/10-visualization-distributions/images/density1.png)

你可以看到該圖表反映了之前的最小翼展數據；它只是稍微平滑了一些。根據 Seaborn 的文檔，“相對於直方圖，KDE 可以生成一個不那麼混亂且更易於解釋的圖表，尤其是在繪製多個分佈時。但如果基礎分佈是有界的或不平滑的，它可能會引入失真。與直方圖一樣，表示的質量也取決於選擇良好的平滑參數。” [來源](https://seaborn.pydata.org/generated/seaborn.kdeplot.html) 換句話說，異常值一如既往地會使你的圖表表現不佳。

如果你想重新訪問第二個圖表中那條鋸齒狀的 MaxBodyMass 線，你可以通過使用此方法非常好地將其平滑化：

```python
sns.kdeplot(filteredBirds['MaxBodyMass'])
plt.show()
```
![平滑的體重線](../../../../3-Data-Visualization/10-visualization-distributions/images/density2.png)

如果你想要一條平滑但不過於平滑的線，請編輯 `bw_adjust` 參數：

```python
sns.kdeplot(filteredBirds['MaxBodyMass'], bw_adjust=.2)
plt.show()
```
![較少平滑的體重線](../../../../3-Data-Visualization/10-visualization-distributions/images/density3.png)

✅ 閱讀此類圖表可用的參數並進行實驗！

這種類型的圖表提供了非常具有解釋性的可視化。例如，通過幾行代碼，你可以顯示每個鳥類目最大體重的密度：

```python
sns.kdeplot(
   data=filteredBirds, x="MaxBodyMass", hue="Order",
   fill=True, common_norm=False, palette="crest",
   alpha=.5, linewidth=0,
)
```

![每個目體重密度](../../../../3-Data-Visualization/10-visualization-distributions/images/density4.png)

你還可以在一個圖表中映射多個變量的密度。測試鳥類的最大長度和最小長度與其保育狀況的關係：

```python
sns.kdeplot(data=filteredBirds, x="MinLength", y="MaxLength", hue="ConservationStatus")
```

![多個密度，疊加](../../../../3-Data-Visualization/10-visualization-distributions/images/multi.png)

或許值得研究根據鳥類長度的“易危”群體是否具有意義。

## 🚀 挑戰

直方圖是一種比基本散點圖、柱狀圖或折線圖更複雜的圖表類型。上網搜索直方圖的良好使用示例。它們如何使用，它們展示了什麼，以及它們通常在哪些領域或研究領域中使用？

## [課後測驗](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/19)

## 回顧與自學

在本課中，你使用了 Matplotlib 並開始使用 Seaborn 來顯示更複雜的圖表。研究 Seaborn 中的 `kdeplot`，這是一個“在一個或多個維度上的連續概率密度曲線”。閱讀 [文檔](https://seaborn.pydata.org/generated/seaborn.kdeplot.html) 以了解其工作原理。

## 作業

[應用你的技能](assignment.md)

**免責聲明**：  
本文件已使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要信息，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋概不負責。