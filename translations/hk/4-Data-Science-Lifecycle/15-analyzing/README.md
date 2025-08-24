<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d92f57eb110dc7f765c05cbf0f837c77",
  "translation_date": "2025-08-24T13:21:08+00:00",
  "source_file": "4-Data-Science-Lifecycle/15-analyzing/README.md",
  "language_code": "hk"
}
-->
# 數據科學生命周期：分析

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/15-Analyzing.png)|
|:---:|
| 數據科學生命周期：分析 - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

## 課前測驗

## [課前測驗](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/28)

在數據生命周期中的分析階段，確認數據是否能回答提出的問題或解決特定問題。這個步驟也可以用來確認模型是否正確地解決了這些問題。本課重點是探索性數據分析（Exploratory Data Analysis，EDA），這是一種用於定義數據特徵和關係的技術，並可用於為建模準備數據。

我們將使用 [Kaggle](https://www.kaggle.com/balaka18/email-spam-classification-dataset-csv/version/1) 的示例數據集，展示如何使用 Python 和 Pandas 庫應用這些技術。這個數據集包含一些常見詞彙在電子郵件中的出現次數，這些電子郵件的來源是匿名的。使用此目錄中的 [notebook](../../../../4-Data-Science-Lifecycle/15-analyzing/notebook.ipynb) 跟隨學習。

## 探索性數據分析

在生命周期的捕獲階段，數據被收集，同時也確定了問題和提出的問題，但我們如何知道數據能否支持最終結果？
回想一下，數據科學家在獲取數據時可能會問以下問題：
-   我是否有足夠的數據來解決這個問題？
-   這些數據的質量是否適合解決這個問題？
-   如果通過這些數據發現了額外的信息，我們是否應該考慮更改或重新定義目標？

探索性數據分析是了解數據的過程，可以用來回答這些問題，並識別處理數據集的挑戰。讓我們專注於一些用於實現這些目標的技術。

## 數據剖析、描述性統計和 Pandas
我們如何評估是否有足夠的數據來解決這個問題？數據剖析可以通過描述性統計技術總結並收集數據集的一些整體信息。數據剖析幫助我們了解可用的數據，而描述性統計幫助我們了解數據的數量。

在之前的一些課程中，我們使用 Pandas 的 [`describe()` 函數](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html) 提供了一些描述性統計。它可以提供數量、最大值和最小值、平均值、標準差以及數據的分位數。使用像 `describe()` 函數這樣的描述性統計可以幫助你評估數據的數量以及是否需要更多數據。

## 抽樣和查詢
探索大型數據集中的所有內容可能非常耗時，通常由計算機完成。然而，抽樣是一種理解數據的有用工具，能幫助我們更好地了解數據集中的內容及其代表的含義。通過抽樣，你可以應用概率和統計來對數據得出一些一般性的結論。雖然沒有明確的規則規定應抽取多少數據，但需要注意的是，抽取的數據越多，對數據的概括就越精確。

Pandas 提供了 [`sample()` 函數](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sample.html)，你可以傳遞一個參數來指定希望獲取的隨機樣本數量並使用它。

對數據進行一般性查詢可以幫助你回答一些普遍的問題和假設。與抽樣相比，查詢允許你控制並專注於數據中你感興趣的特定部分。
Pandas 庫中的 [`query()` 函數](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html) 允許你選擇列並通過檢索的行獲得關於數據的簡單答案。

## 使用可視化進行探索
你不需要等到數據完全清理和分析後才開始創建可視化。事實上，在探索過程中擁有可視化表示可以幫助識別數據中的模式、關係和問題。此外，可視化為那些未參與數據管理的人提供了一種溝通方式，並且可以是一個分享和澄清捕獲階段未解決問題的機會。參考 [可視化部分](../../../../../../../../../3-Data-Visualization) 了解一些流行的可視化探索方法。

## 探索以識別不一致
本課中的所有主題都可以幫助識別缺失或不一致的值，但 Pandas 提供了一些函數來檢查這些問題。[isna() 或 isnull()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.isna.html) 可以檢查缺失值。探索這些值在數據中出現的原因是一個重要的步驟，這可以幫助你決定 [採取哪些行動來解決它們](../../../../../../../../../2-Working-With-Data/08-data-preparation/notebook.ipynb)。

## [課前測驗](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/27)

## 作業

[探索答案](assignment.md)

**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們致力於提供準確的翻譯，請注意自動翻譯可能包含錯誤或不準確之處。原始語言的文件應被視為具權威性的來源。對於重要資訊，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋概不負責。