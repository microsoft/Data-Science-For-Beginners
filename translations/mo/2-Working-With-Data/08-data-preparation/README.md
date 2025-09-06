<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1b560955ff39a2bcf2a049fce474a951",
  "translation_date": "2025-09-06T06:55:21+00:00",
  "source_file": "2-Working-With-Data/08-data-preparation/README.md",
  "language_code": "mo"
}
-->
# 資料處理：資料準備

|![由 [(@sketchthedocs)](https://sketchthedocs.dev) 繪製的速記筆記](../../sketchnotes/08-DataPreparation.png)|
|:---:|
|資料準備 - _由 [@nitya](https://twitter.com/nitya) 繪製的速記筆記_ |

## [課前測驗](https://ff-quizzes.netlify.app/en/ds/quiz/14)

根據資料來源，原始資料可能包含一些不一致性，這些不一致性會在分析和建模時帶來挑戰。換句話說，這些資料可以被歸類為「髒資料」，需要進行清理。本課程重點介紹清理和轉換資料的技術，以處理缺失、不準確或不完整的資料。本課程涵蓋的主題將使用 Python 和 Pandas 庫，並在本目錄中的[筆記本](../../../../2-Working-With-Data/08-data-preparation/notebook.ipynb)中進行演示。

## 清理資料的重要性

- **使用和重用的便利性**：當資料被妥善組織和標準化時，更容易搜尋、使用並與他人共享。

- **一致性**：資料科學通常需要處理多個資料集，來自不同來源的資料集需要合併在一起。確保每個資料集具有共同的標準化，能確保合併後的資料仍然有用。

- **模型準確性**：清理過的資料能提高依賴該資料的模型的準確性。

## 常見的清理目標與策略

- **探索資料集**：資料探索（在[後續課程](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/4-Data-Science-Lifecycle/15-analyzing)中涵蓋）可以幫助您發現需要清理的資料。透過視覺化觀察資料集中的值，可以設置對其餘部分的期望，或提供解決問題的思路。探索可以包括基本查詢、視覺化和抽樣。

- **格式化**：根據來源，資料可能在呈現方式上存在不一致性。這可能導致搜尋和表示值時出現問題，資料雖然在資料集中可見，但在視覺化或查詢結果中未正確表示。常見的格式化問題包括解決空白、日期和資料類型。解決格式問題通常由使用資料的人來完成。例如，不同國家對日期和數字的表示標準可能不同。

- **重複資料**：重複出現的資料可能會產生不準確的結果，通常應該移除。這在合併兩個或多個資料集時很常見。然而，有些情況下，合併資料集中的重複部分可能提供額外資訊，需要保留。

- **缺失資料**：缺失資料可能導致不準確以及結果偏弱或有偏差。有時可以通過重新載入資料、使用 Python 等程式碼計算填補缺失值，或者直接移除該值及其相關資料來解決。資料缺失的原因有很多，解決缺失值的方式可能取決於其缺失的原因。

## 探索 DataFrame 資訊
> **學習目標**：完成本小節後，您應該能夠熟練地查找存儲在 pandas DataFrame 中的資料的基本資訊。

當您將資料載入 pandas 時，它通常會以 DataFrame 的形式存在（請參考之前的[課程](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/2-Working-With-Data/07-python#dataframe)以獲取詳細概述）。然而，如果您的 DataFrame 中的資料集有 60,000 行和 400 列，您該如何開始了解您正在處理的內容？幸運的是，[pandas](https://pandas.pydata.org/) 提供了一些方便的工具，可以快速查看 DataFrame 的整體資訊以及前幾行和後幾行。

為了探索這些功能，我們將導入 Python 的 scikit-learn 庫並使用一個經典的資料集：**Iris 資料集**。

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

- **DataFrame.info**：首先，`info()` 方法用於列印 `DataFrame` 中內容的摘要。讓我們看看這個資料集的內容：
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
從中我們知道 *Iris* 資料集有 150 條記錄，分布在四個欄位中，且沒有空值。所有資料都存儲為 64 位浮點數。

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
- **DataFrame.tail()**：相反地，為了檢查 `DataFrame` 的最後幾行，我們使用 `tail()` 方法：
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
> **重點**：僅僅通過查看 DataFrame 中的元數據或前幾個和最後幾個值，您就可以立即了解您正在處理的資料的大小、形狀和內容。

## 處理缺失資料
> **學習目標**：完成本小節後，您應該知道如何替換或移除 DataFrame 中的空值。

大多數情況下，您想使用（或必須使用）的資料集中都會有缺失值。如何處理缺失資料涉及微妙的權衡，這可能會影響您的最終分析和實際結果。

Pandas 以兩種方式處理缺失值。第一種方式您在之前的部分中已經看到過：`NaN`，即非數值（Not a Number）。這實際上是一個特殊值，是 IEEE 浮點規範的一部分，僅用於表示缺失的浮點值。

對於浮點數以外的缺失值，pandas 使用 Python 的 `None` 對象。雖然遇到兩種不同的值來表示基本相同的事情可能會讓人感到困惑，但這種設計選擇有其合理的程式設計原因，實際上，這種方式為大多數情況提供了一個良好的折衷。不過，`None` 和 `NaN` 都有一些限制，您需要注意它們的使用方式。

在[筆記本](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/4-Data-Science-Lifecycle/15-analyzing/notebook.ipynb)中了解更多關於 `NaN` 和 `None` 的資訊！

- **檢測空值**：在 `pandas` 中，`isnull()` 和 `notnull()` 方法是檢測空資料的主要方法。這兩個方法都返回布林掩碼。接下來我們將使用 `numpy` 來處理 `NaN` 值：
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
仔細查看輸出。是否有任何結果讓您感到驚訝？雖然 `0` 是一個算術空值，但它仍然是一個完全有效的整數，pandas 將其視為整數。`''` 則稍微微妙一些。雖然我們在第一部分中使用它來表示空字串值，但它仍然是一個字串對象，而不是 pandas 所認為的空值。

現在，讓我們反過來以更接近實際使用的方式使用這些方法。您可以直接將布林掩碼用作 ``Series`` 或 ``DataFrame`` 的索引，這在處理孤立的缺失（或存在）值時非常有用。

> **重點**：`isnull()` 和 `notnull()` 方法在 `DataFrame` 中的使用結果相似：它們顯示結果及其索引，這將在您處理資料時幫助您。

- **移除空值**：除了識別缺失值，pandas 還提供了一種方便的方法來移除 `Series` 和 `DataFrame` 中的空值。（特別是在大型資料集上，通常更建議直接移除缺失 [NA] 值，而不是以其他方式處理它們。）讓我們回到 `example1` 來看看這一點：
```python
example1 = example1.dropna()
example1
```
```
0    0
2     
dtype: object
```
注意，這應該看起來像您的 `example3[example3.notnull()]` 的輸出。不同之處在於，`dropna` 不僅索引了掩碼值，還移除了 `Series` `example1` 中的缺失值。

由於 `DataFrame` 是二維的，它提供了更多移除資料的選項。

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

（您是否注意到 pandas 將兩列提升為浮點數以容納 `NaN`？）

您無法從 `DataFrame` 中移除單個值，因此必須移除整行或整列。根據您的操作，您可能需要選擇其中一種方式，因此 pandas 提供了兩者的選項。由於在資料科學中，列通常表示變數，行表示觀察值，您更可能移除資料的行；`dropna()` 的預設設置是移除所有包含任何空值的行：

```python
example2.dropna()
```
```
	0	1	2
1	2.0	5.0	8
```
如果需要，您可以移除列中的 NA 值。使用 `axis=1` 來完成：
```python
example2.dropna(axis='columns')
```
```
	2
0	7
1	8
2	9
```
注意，這可能會移除您可能想保留的大量資料，特別是在較小的資料集中。如果您只想移除包含幾個甚至所有空值的行或列，您可以在 `dropna` 中使用 `how` 和 `thresh` 參數指定這些設置。

預設情況下，`how='any'`（如果您想自己檢查或查看該方法的其他參數，請在程式碼單元中運行 `example4.dropna?`）。您也可以選擇指定 `how='all'`，以便僅移除包含所有空值的行或列。讓我們擴展我們的示例 `DataFrame` 來看看這一點。

```python
example2[3] = np.nan
example2
```
|      |0  |1  |2  |3  |
|------|---|---|---|---|
|0     |1.0|NaN|7  |NaN|
|1     |2.0|5.0|8  |NaN|
|2     |NaN|6.0|9  |NaN|

`thresh` 參數提供了更細緻的控制：您可以設置行或列需要保留的*非空*值的數量：
```python
example2.dropna(axis='rows', thresh=3)
```
```
	0	1	2	3
1	2.0	5.0	8	NaN
```
在這裡，第一行和最後一行被移除，因為它們僅包含兩個非空值。

- **填充空值**：根據您的資料集，有時填充空值比移除它們更合理。您可以使用 `isnull` 直接進行填充，但這可能會很繁瑣，特別是當您有大量值需要填充時。由於這是資料科學中的常見任務，pandas 提供了 `fillna`，它返回一個 `Series` 或 `DataFrame` 的副本，其中的缺失值被替換為您選擇的值。讓我們創建另一個示例 `Series` 來看看這在實際中的運作方式。
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
您可以用單一值（例如 `0`）填充所有空條目：
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
您可以**向前填充**空值，即使用最後一個有效值填充空值：
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
您也可以**向後填充**，即向後傳播下一個有效值以填充空值：
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
如您所料，這對 `DataFrame` 也適用，但您還可以指定沿著哪個 `axis` 填充空值。再次使用之前的 `example2`：
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
> **重點:** 處理資料集中缺失值的方法有很多種。你採用的具體策略（移除、替換，甚至替換的方式）應該根據該資料的特性來決定。隨著你處理和接觸更多的資料集，你將更能掌握如何應對缺失值的技巧。
## 移除重複數據

> **學習目標：** 在本小節結束時，你應該能夠熟練地識別並移除 DataFrame 中的重複值。

除了缺失數據之外，你在真實世界的數據集中還會經常遇到重複的數據。幸運的是，`pandas` 提供了一種簡單的方法來檢測和移除重複的條目。

- **識別重複值：`duplicated`**：你可以使用 pandas 的 `duplicated` 方法輕鬆地找到重複值。該方法返回一個布林掩碼，指示 `DataFrame` 中某條目是否與之前的條目重複。我們來創建另一個示例 `DataFrame`，看看這個方法的實際效果。
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
- **移除重複值：`drop_duplicates`**：該方法簡單地返回一個副本，其中所有 `duplicated` 值為 `False` 的數據：
```python
example4.drop_duplicates()
```
```
	letters	numbers
0	A	1
1	B	2
3	B	3
```
`duplicated` 和 `drop_duplicates` 預設會考慮所有列，但你可以指定它們僅檢查 `DataFrame` 中的一部分列：
```python
example4.drop_duplicates(['letters'])
```
```
letters	numbers
0	A	1
1	B	2
```

> **重點提示：** 移除重複數據是幾乎每個數據科學項目中的重要步驟。重複數據可能會改變你的分析結果，導致不準確的結論！


## 🚀 挑戰

所有討論過的材料都提供為一個 [Jupyter Notebook](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/2-Working-With-Data/08-data-preparation/notebook.ipynb)。此外，每個部分之後還有練習題，試著完成它們吧！

## [課後測驗](https://ff-quizzes.netlify.app/en/ds/quiz/15)



## 回顧與自學

有許多方法可以發現並準備你的數據進行分析和建模，而清理數據是一個需要「親自動手」的關鍵步驟。試試 Kaggle 上的這些挑戰，探索本課未涵蓋的技術。

- [數據清理挑戰：解析日期](https://www.kaggle.com/rtatman/data-cleaning-challenge-parsing-dates/)

- [數據清理挑戰：數據縮放與標準化](https://www.kaggle.com/rtatman/data-cleaning-challenge-scale-and-normalize-data)


## 作業

[評估表單中的數據](assignment.md)

---

**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們努力確保翻譯的準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於關鍵信息，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋不承擔責任。