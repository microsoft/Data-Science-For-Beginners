<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d92f57eb110dc7f765c05cbf0f837c77",
  "translation_date": "2025-08-27T09:56:19+00:00",
  "source_file": "4-Data-Science-Lifecycle/15-analyzing/README.md",
  "language_code": "mo"
}
-->
# 數據科學生命周期：分析

|![由 [(@sketchthedocs)](https://sketchthedocs.dev) 繪製的手繪筆記](../../sketchnotes/15-Analyzing.png)|
|:---:|
| 數據科學生命周期：分析 - _由 [@nitya](https://twitter.com/nitya) 繪製的手繪筆記_ |

## 課前測驗

## [課前測驗](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/28)

在數據生命周期中的分析階段，確認數據是否能回答所提出的問題或解決特定問題。這一步驟也可以用來確認模型是否正確地解決了這些問題。本課程專注於探索性數據分析（Exploratory Data Analysis，簡稱 EDA），這是一種用於定義數據特徵和關係的技術，並可用於為建模做準備。

我們將使用來自 [Kaggle](https://www.kaggle.com/balaka18/email-spam-classification-dataset-csv/version/1) 的示例數據集，展示如何使用 Python 和 Pandas 庫應用這些技術。這個數據集包含一些電子郵件中常見詞彙的計數，這些電子郵件的來源是匿名的。請使用本目錄中的 [notebook](notebook.ipynb) 來跟隨學習。

## 探索性數據分析

在生命周期的數據捕獲階段，我們獲取數據並確定問題和相關問題，但我們如何知道這些數據能否支持最終結果呢？  
回想一下，數據科學家在獲取數據時可能會提出以下問題：
-   我有足夠的數據來解決這個問題嗎？
-   這些數據的質量是否能滿足這個問題的需求？
-   如果通過這些數據發現了額外的信息，我們是否應該考慮更改或重新定義目標？

探索性數據分析是一個了解數據的過程，可以用來回答這些問題，並識別處理數據集時可能面臨的挑戰。接下來，我們將專注於一些用於實現這些目標的技術。

## 數據剖析、描述性統計和 Pandas

我們如何評估是否有足夠的數據來解決這個問題？數據剖析可以通過描述性統計技術來總結並收集數據集的一些整體信息。數據剖析幫助我們了解手頭的數據，而描述性統計則幫助我們了解數據的數量。

在之前的一些課程中，我們使用 Pandas 的 [`describe()` 函數](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html) 提供了一些描述性統計。它可以對數值數據提供計數、最大值和最小值、平均值、標準差以及分位數等信息。使用像 `describe()` 這樣的描述性統計函數可以幫助你評估數據量是否足夠，或者是否需要更多數據。

## 抽樣與查詢

在大型數據集中探索所有內容可能非常耗時，這通常是交給計算機完成的任務。然而，抽樣是一種理解數據的有用工具，能幫助我們更好地了解數據集的內容及其代表的意義。通過抽樣，你可以應用概率和統計來對數據得出一些一般性的結論。雖然沒有明確的規則規定應該抽取多少數據，但需要注意的是，抽樣的數據越多，對數據進行概括的準確性就越高。

Pandas 提供了 [`sample()` 函數](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sample.html)，你可以通過參數指定想要獲取的隨機樣本數量。

對數據進行一般性查詢可以幫助你回答一些初步的問題和假設。與抽樣不同，查詢允許你控制並專注於數據中你感興趣的特定部分。Pandas 庫中的 [`query()` 函數](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html) 允許你選擇列並通過檢索的行獲得簡單的數據答案。

## 使用可視化進行探索

你不需要等到數據徹底清理和分析後才開始創建可視化。事實上，在探索過程中使用可視化可以幫助識別數據中的模式、關係和問題。此外，可視化還能為那些未參與數據管理的人提供一種溝通方式，並且是一個分享和澄清在數據捕獲階段未解決問題的機會。請參考[可視化部分](../../../../../../../../../3-Data-Visualization)來了解一些流行的可視化探索方法。

## 探索以識別不一致性

本課程中的所有主題都可以幫助識別缺失或不一致的值，而 Pandas 提供了一些函數來檢查這些問題。[isna() 或 isnull()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.isna.html) 可以用來檢查缺失值。在探索數據中這些值的過程中，一個重要的部分是了解它們為什麼會出現。這可以幫助你決定應該採取哪些[措施來解決這些問題](/2-Working-With-Data/08-data-preparation/notebook.ipynb)。

## [課前測驗](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/27)

## 作業

[探索答案](assignment.md)

---

**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原始語言的文件作為權威來源。對於關鍵資訊，建議尋求專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤釋不承擔責任。