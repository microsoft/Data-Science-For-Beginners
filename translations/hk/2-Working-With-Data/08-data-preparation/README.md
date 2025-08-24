<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3ade580a06b5f04d57cc83a768a8fb77",
  "translation_date": "2025-08-24T12:05:02+00:00",
  "source_file": "2-Working-With-Data/08-data-preparation/README.md",
  "language_code": "hk"
}
-->
# 處理數據：數據準備

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/08-DataPreparation.png)|
|:---:|
|數據準備 - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

## [課前測驗](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/14)

根據數據來源，原始數據可能包含一些不一致性，這些不一致性會在分析和建模過程中帶來挑戰。換句話說，這些數據可以被歸類為「髒數據」，需要進行清理。本課程重點介紹清理和轉換數據的技術，以應對缺失、不準確或不完整的數據挑戰。本課程涵蓋的主題將使用 Python 和 Pandas 庫，並在本目錄中的[筆記本](../../../../2-Working-With-Data/08-data-preparation/notebook.ipynb)中進行演示。

## 清理數據的重要性

- **易於使用和重用**：當數據被正確組織和標準化後，更容易搜索、使用和與他人共享。

- **一致性**：數據科學通常需要處理多個數據集，來自不同來源的數據集需要合併在一起。確保每個單獨的數據集具有共同的標準化，能保證合併後的數據仍然有用。

- **模型準確性**：清理過的數據能提高依賴於它的模型的準確性。

## 常見的清理目標和策略

- **探索數據集**：數據探索（在[後續課程](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/4-Data-Science-Lifecycle/15-analyzing)中會介紹）可以幫助你發現需要清理的數據。通過可視化觀察數據集中的值，可以設置對其餘部分的期望，或者提供解決問題的思路。探索可以包括基本查詢、可視化和抽樣。

- **格式化**：根據來源，數據在呈現方式上可能存在不一致性。這可能導致在搜索和表示值時出現問題，數據雖然在數據集中可見，但在可視化或查詢結果中未正確表示。常見的格式化問題包括解決空白、日期和數據類型。解決格式化問題通常由使用數據的人來完成。例如，不同國家對日期和數字的表示標準可能不同。

- **重複數據**：多次出現的數據可能會產生不準確的結果，通常應該刪除。這在合併兩個或多個數據集時很常見。然而，有些情況下，合併數據集中的重複部分可能包含額外信息，需要保留。

- **缺失數據**：缺失數據可能導致不準確以及結果偏差。有時可以通過重新加載數據、使用 Python 等代碼計算填充缺失值，或者直接刪除缺失值及其相關數據來解決。數據缺失的原因有很多，解決缺失值的行動取決於它們缺失的方式和原因。

## 探索 DataFrame 信息
> **學習目標**：完成本小節後，你應該能夠熟練地查找存儲在 pandas DataFrame 中的數據的一般信息。

當你將數據加載到 pandas 中後，它很可能會以 DataFrame 的形式存在（參考之前的[課程](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/2-Working-With-Data/07-python#dataframe)了解詳細概述）。然而，如果你的 DataFrame 中的數據集有 60,000 行和 400 列，你該如何開始了解你正在處理的內容？幸運的是，[pandas](https://pandas.pydata.org/) 提供了一些方便的工具，可以快速查看 DataFrame 的整體信息以及前幾行和後幾行。

為了探索這些功能，我們將導入 Python 的 scikit-learn 庫並使用一個經典數據集：**Iris 數據集**。

```python
import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()
iris_df = pd.DataFrame(data=iris['data'], columns=iris['feature_names'])
```
|                                        |sepal length (cm)|sepal width (cm)|petal length (cm)|petal width (cm)|
|----------------------------------------|-----------------|----------------|-----------------|----------------|
|0                                       |5.1              |3.5             |1.4              |0.2             |
|1                                       |4.9              |3.0             |1.4              |0.2             |
|2                                       |4.7              |3.2             |1.3              |0.2             |
|3                                       |4.6              |3.1             |1.5              |0.2             |
|4                                       |5.0              |3.6             |1.4              |0.2             |

- **DataFrame.info**：首先，`info()` 方法用於打印 `DataFrame` 中內容的摘要。我們來看看這個數據集：
```python
iris_df.info()
```
```
RangeIndex: 150 entries, 0 to 149
Data columns (total 4 columns):
 #   Column             Non-Null Count  Dtype  
---  ------             --------------  -----  
 0   sepal length (cm)  150 non-null    float64
 1   sepal width (cm)   150 non-null    float64
 2   petal length (cm)  150 non-null    float64
 3   petal width (cm)   150 non-null    float64
dtypes: float64(4)
memory usage: 4.8 KB
```
從中我們知道 *Iris* 數據集有 150 條記錄，分布在四列中，沒有空值。所有數據都存儲為 64 位浮點數。

- **DataFrame.head()**：接下來，為了檢查 `DataFrame` 的實際內容，我們使用 `head()` 方法。讓我們看看 `iris_df` 的前幾行：
```python
iris_df.head()
```
```
   sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
0                5.1               3.5                1.4               0.2
1                4.9               3.0                1.4               0.2
2                4.7               3.2                1.3               0.2
3                4.6               3.1                1.5               0.2
4                5.0               3.6                1.4               0.2
```
- **DataFrame.tail()**：相反，為了檢查 `DataFrame` 的後幾行，我們使用 `tail()` 方法：
```python
iris_df.tail()
```
```
     sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
145                6.7               3.0                5.2               2.3
146                6.3               2.5                5.0               1.9
147                6.5               3.0                5.2               2.0
148                6.2               3.4                5.4               2.3
149                5.9               3.0                5.1               1.8
```
> **重點**：僅僅通過查看 DataFrame 中的信息元數據或前幾行和後幾行的值，你就可以立即了解你正在處理的數據的大小、形狀和內容。

## 處理缺失數據
> **學習目標**：完成本小節後，你應該知道如何替換或刪除 DataFrame 中的空值。

大多數情況下，你想使用（或必須使用）的數據集中都會有缺失值。如何處理缺失數據涉及微妙的權衡，這可能會影響你的最終分析和現實世界的結果。

Pandas 以兩種方式處理缺失值。第一種方式你在之前的部分中已經見過：`NaN`，即非數值（Not a Number）。這實際上是一個特殊值，是 IEEE 浮點規範的一部分，僅用於表示缺失的浮點值。

對於浮點數以外的缺失值，pandas 使用 Python 的 `None` 對象。雖然你可能會覺得遇到兩種不同的值來表示基本相同的事情有些混亂，但這種設計選擇有其合理的編程原因，實際上，這種方式在大多數情況下提供了一個良好的折衷。不過，`None` 和 `NaN` 都有一些限制，你需要注意它們的使用方式。

在[筆記本](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/4-Data-Science-Lifecycle/15-analyzing/notebook.ipynb)中了解更多關於 `NaN` 和 `None` 的信息！

- **檢測空值**：在 `pandas` 中，`isnull()` 和 `notnull()` 方法是檢測空數據的主要方法。兩者都返回布爾掩碼。我們將使用 `numpy` 來處理 `NaN` 值：
```python
import numpy as np

example1 = pd.Series([0, np.nan, '', None])
example1.isnull()
```
```
0    False
1     True
2    False
3     True
dtype: bool
```
仔細查看輸出。有什麼讓你感到驚訝嗎？雖然 `0` 是一個算術空值，但它仍然是一個完全有效的整數，pandas 將其視為這樣。`''` 更微妙一些。雖然我們在第一部分中使用它來表示空字符串值，但它仍然是一個字符串對象，而不是 pandas 所認為的空值表示。

現在，讓我們反過來以更接近實際使用的方式使用這些方法。你可以直接將布爾掩碼用作 ``Series`` 或 ``DataFrame`` 的索引，這在處理孤立的缺失（或存在）值時非常有用。

> **重點**：`isnull()` 和 `notnull()` 方法在 `DataFrame` 中的使用結果相似：它們顯示結果及其索引，這對你處理數據時非常有幫助。

- **刪除空值**：除了識別缺失值，pandas 還提供了一種方便的方法來刪除 `Series` 和 `DataFrame` 中的空值。（特別是在大型數據集上，通常更建議直接刪除分析中的缺失 [NA] 值，而不是以其他方式處理它們。）讓我們回到 `example1`：
```python
example1 = example1.dropna()
example1
```
```
0    0
2     
dtype: object
```
注意，這應該看起來像你的 `example3[example3.notnull()]` 的輸出。不同之處在於，`dropna` 已經從 `Series` `example1` 中刪除了那些缺失值。

由於 `DataFrame` 是二維的，它提供了更多刪除數據的選項。

```python
example2 = pd.DataFrame([[1,      np.nan, 7], 
                         [2,      5,      8], 
                         [np.nan, 6,      9]])
example2
```
|      | 0 | 1 | 2 |
|------|---|---|---|
|0     |1.0|NaN|7  |
|1     |2.0|5.0|8  |
|2     |NaN|6.0|9  |

（你是否注意到 pandas 將兩列數據提升為浮點數以容納 `NaN`？）

你不能從 `DataFrame` 中刪除單個值，因此你必須刪除整行或整列。根據你的操作需求，你可能需要刪除其中之一，pandas 為此提供了選擇。由於在數據科學中，列通常表示變量，行表示觀察值，你更可能刪除數據行；`dropna()` 的默認設置是刪除所有包含任何空值的行：

```python
example2.dropna()
```
```
	0	1	2
1	2.0	5.0	8
```
如果需要，你可以刪除列中的 NA 值。使用 `axis=1` 來完成：
```python
example2.dropna(axis='columns')
```
```
	2
0	7
1	8
2	9
```
注意，這可能會刪除你可能想保留的大量數據，特別是在較小的數據集中。如果你只想刪除包含幾個或所有空值的行或列怎麼辦？你可以在 `dropna` 中使用 `how` 和 `thresh` 參數來指定這些設置。

默認情況下，`how='any'`（如果你想自己檢查或查看該方法的其他參數，可以在代碼單元中運行 `example4.dropna?`）。你也可以選擇指定 `how='all'`，以便僅刪除包含所有空值的行或列。讓我們擴展示例 `DataFrame` 來看看這是如何運作的。

```python
example2[3] = np.nan
example2
```
|      |0  |1  |2  |3  |
|------|---|---|---|---|
|0     |1.0|NaN|7  |NaN|
|1     |2.0|5.0|8  |NaN|
|2     |NaN|6.0|9  |NaN|

`thresh` 參數提供了更細粒度的控制：你可以設置行或列需要保留的*非空*值的數量：
```python
example2.dropna(axis='rows', thresh=3)
```
```
	0	1	2	3
1	2.0	5.0	8	NaN
```
在這裡，第一行和最後一行被刪除，因為它們只有兩個非空值。

- **填充空值**：根據你的數據集，有時填充空值比刪除它們更合理。你可以使用 `isnull` 來就地完成這項工作，但如果你有很多值需要填充，這可能會很繁瑣。由於這是數據科學中的常見任務，pandas 提供了 `fillna`，它返回一個 `Series` 或 `DataFrame` 的副本，其中的缺失值被替換為你選擇的值。讓我們創建另一個示例 `Series` 來看看這在實踐中如何運作。
```python
example3 = pd.Series([1, np.nan, 2, None, 3], index=list('abcde'))
example3
```
```
a    1.0
b    NaN
c    2.0
d    NaN
e    3.0
dtype: float64
```
你可以用單一值（例如 `0`）填充所有空值：
```python
example3.fillna(0)
```
```
a    1.0
b    0.0
c    2.0
d    0.0
e    3.0
dtype: float64
```
你可以**向前填充**空值，即使用最後一個有效值填充空值：
```python
example3.fillna(method='ffill')
```
```
a    1.0
b    1.0
c    2.0
d    2.0
e    3.0
dtype: float64
```
你也可以**向後填充**，即向後傳播下一個有效值以填充空值：
```python
example3.fillna(method='bfill')
```
```
a    1.0
b    2.0
c    2.0
d    3.0
e    3.0
dtype: float64
```
正如你可能猜到的，這對 `DataFrame` 也同樣有效，但你還可以指定沿著哪個 `axis` 填充空值。再次使用之前的 `example2`：
```python
example2.fillna(method='ffill', axis=1)
```
```
	0	1	2	3
0	1.0	1.0	7.0	7.0
1	2.0	5.0	8.0	8.0
2	NaN	6.0	9.0	9.0
```
注意，當前一個值不可用進行向前填充時，空值仍然保留。
> **重點提示：** 在處理數據集中缺失值時，有多種方法可供選擇。具體採用哪種策略（刪除、替換，甚至是如何替換）應該根據數據的特性來決定。隨著你處理和分析更多數據集，你將更能掌握如何應對缺失值。

## 刪除重複數據

> **學習目標：** 在本小節結束時，你應該能夠熟練地識別並刪除 DataFrame 中的重複值。

除了缺失數據外，你在現實世界的數據集中還會經常遇到重複數據。幸運的是，`pandas` 提供了一種簡單的方法來檢測和刪除重複條目。

- **識別重複值：`duplicated`**：你可以使用 pandas 中的 `duplicated` 方法輕鬆地找到重複值。該方法返回一個布爾掩碼，指示 `DataFrame` 中某條目是否是之前條目的重複。我們來創建另一個示例 `DataFrame`，看看它是如何運作的。
```python
example4 = pd.DataFrame({'letters': ['A','B'] * 2 + ['B'],
                         'numbers': [1, 2, 1, 3, 3]})
example4
```
|      |letters|numbers|
|------|-------|-------|
|0     |A      |1      |
|1     |B      |2      |
|2     |A      |1      |
|3     |B      |3      |
|4     |B      |3      |

```python
example4.duplicated()
```
```
0    False
1    False
2     True
3    False
4     True
dtype: bool
```
- **刪除重複值：`drop_duplicates`**：該方法返回一個副本，其中所有 `duplicated` 值為 `False` 的數據被保留：
```python
example4.drop_duplicates()
```
```
	letters	numbers
0	A	1
1	B	2
3	B	3
```
`duplicated` 和 `drop_duplicates` 默認會考慮所有列，但你可以指定它們僅檢查 `DataFrame` 中的某些列：
```python
example4.drop_duplicates(['letters'])
```
```
letters	numbers
0	A	1
1	B	2
```

> **重點提示：** 刪除重複數據是幾乎每個數據科學項目中的重要步驟。重複數據可能會改變你的分析結果，導致不準確的結論！

## 🚀 挑戰

所有討論的材料都已作為 [Jupyter Notebook](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/2-Working-With-Data/08-data-preparation/notebook.ipynb) 提供。此外，每個部分之後還有練習題，試著完成它們吧！

## [課後測驗](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/15)

## 回顧與自學

有許多方法可以發現並準備你的數據進行分析和建模，而清理數據是一個需要「親身實踐」的重要步驟。試試 Kaggle 上的這些挑戰，探索本課未涵蓋的技術。

- [數據清理挑戰：解析日期](https://www.kaggle.com/rtatman/data-cleaning-challenge-parsing-dates/)

- [數據清理挑戰：數據縮放與標準化](https://www.kaggle.com/rtatman/data-cleaning-challenge-scale-and-normalize-data)

## 作業

[評估表單中的數據](assignment.md)

**免責聲明**：  
本文件已使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原文文件作為權威來源。對於關鍵資訊，建議尋求專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋概不負責。