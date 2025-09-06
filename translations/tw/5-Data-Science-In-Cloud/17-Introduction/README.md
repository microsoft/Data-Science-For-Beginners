<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f8e7cdefa096664ae86f795be571580",
  "translation_date": "2025-09-05T11:43:34+00:00",
  "source_file": "5-Data-Science-In-Cloud/17-Introduction/README.md",
  "language_code": "tw"
}
-->
# 雲端中的資料科學介紹

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/17-DataScience-Cloud.png)|
|:---:|
| 雲端中的資料科學：介紹 - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

在本課程中，您將學習雲端的基本原則，了解使用雲端服務來執行資料科學項目的好處，並探索一些在雲端中運行的資料科學項目範例。

## [課前測驗](https://ff-quizzes.netlify.app/en/ds/quiz/32)

## 什麼是雲端？

雲端，或稱雲端運算，是透過網際網路提供一系列按需付費的運算服務，這些服務基於一個基礎架構上運行。服務包括存儲、資料庫、網路、軟體、分析以及智能服務等解決方案。

我們通常將公有雲、私有雲和混合雲區分如下：

* 公有雲：公有雲由第三方雲端服務提供商擁有和運營，並透過網際網路向公眾提供其運算資源。
* 私有雲：私有雲指的是專門由單一企業或組織使用的雲端運算資源，服務和基礎架構維護在私人網路上。
* 混合雲：混合雲是一種結合公有雲和私有雲的系統。使用者可以選擇本地數據中心，同時允許數據和應用程式在一個或多個公有雲上運行。

大多數雲端運算服務分為三類：基礎架構即服務 (IaaS)、平台即服務 (PaaS) 和軟體即服務 (SaaS)。

* 基礎架構即服務 (IaaS)：使用者租用 IT 基礎架構，例如伺服器和虛擬機 (VM)、存儲、網路、操作系統。
* 平台即服務 (PaaS)：使用者租用一個開發、測試、交付和管理軟體應用程式的環境。使用者不需要擔心設置或管理伺服器、存儲、網路和資料庫等基礎架構。
* 軟體即服務 (SaaS)：使用者透過網際網路按需訪問軟體應用程式，通常以訂閱方式提供。使用者不需要擔心托管和管理軟體應用程式、基礎架構或維護，例如軟體升級和安全修補。

一些最大的雲端提供商包括 Amazon Web Services、Google Cloud Platform 和 Microsoft Azure。

## 為什麼選擇雲端進行資料科學？

開發者和 IT 專業人士選擇使用雲端的原因有很多，包括以下幾點：

* 創新：您可以透過將雲端提供商創建的創新服務直接整合到您的應用程式中來提升應用程式的功能。
* 靈活性：您只需支付所需的服務費用，並可從多種服務中選擇。通常採用按需付費模式，並根據需求調整服務。
* 預算：您不需要進行初期投資來購買硬體和軟體，設置和運行本地數據中心，僅需支付使用的費用。
* 可擴展性：您的資源可以根據項目需求進行擴展，這意味著您的應用程式可以根據外部因素在任何時間點使用更多或更少的運算能力、存儲和頻寬。
* 生產力：您可以專注於業務，而不是花時間處理可以由其他人管理的任務，例如管理數據中心。
* 可靠性：雲端運算提供多種方式來持續備份您的數據，並可設置災難恢復計劃，即使在危機時期也能保持業務和服務運行。
* 安全性：您可以受益於加強項目安全性的政策、技術和控制措施。

以上是人們選擇使用雲端服務的一些常見原因。現在我們對雲端及其主要優勢有了更好的理解，接下來我們將更具體地探討資料科學家和處理數據的開發者的工作，以及雲端如何幫助他們應對可能面臨的多種挑戰：

* 存儲大量數據：與其購買、管理和保護大型伺服器，您可以直接將數據存儲在雲端，例如使用 Azure Cosmos DB、Azure SQL Database 和 Azure Data Lake Storage。
* 執行數據整合：數據整合是資料科學的重要部分，讓您從數據收集過渡到採取行動。透過雲端提供的數據整合服務，您可以從多個來源收集、轉換和整合數據到單一數據倉庫，例如使用 Data Factory。
* 處理數據：處理大量數據需要大量運算能力，而並非每個人都能擁有足夠強大的機器，因此許多人選擇直接利用雲端的巨大運算能力來運行和部署解決方案。
* 使用數據分析服務：雲端服務如 Azure Synapse Analytics、Azure Stream Analytics 和 Azure Databricks，幫助您將數據轉化為可行的洞察。
* 使用機器學習和數據智能服務：與其從零開始，您可以使用雲端提供商提供的機器學習算法，例如 AzureML。您還可以使用認知服務，例如語音轉文字、文字轉語音、電腦視覺等。

## 雲端中的資料科學範例

讓我們透過幾個場景來更具體地了解。

### 即時社交媒體情緒分析
我們從一個常見的機器學習入門場景開始：即時社交媒體情緒分析。

假設您運營一個新聞媒體網站，並希望利用即時數據來了解讀者可能感興趣的內容。為了更深入了解，您可以建立一個程序，對 Twitter 上與讀者相關的主題進行即時情緒分析。

您需要關注的關鍵指標是特定主題（標籤）的推文數量和情緒，情緒是透過分析工具對指定主題進行情緒分析得出的。

建立此項目所需的步驟如下：

* 創建一個事件中心以收集 Twitter 的輸入數據流
* 配置並啟動 Twitter 客戶端應用程式，調用 Twitter Streaming APIs
* 創建一個 Stream Analytics 作業
* 指定作業輸入和查詢
* 創建輸出接收器並指定作業輸出
* 啟動作業

查看完整過程，請參考[文件](https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?WT.mc_id=academic-77958-bethanycheum&ocid=AID30411099)。

### 科學論文分析
讓我們看另一個由本課程作者之一 [Dmitry Soshnikov](http://soshnikov.com) 創建的項目範例。

Dmitry 創建了一個分析 COVID 論文的工具。透過審視此項目，您將了解如何創建一個工具，從科學論文中提取知識，獲得洞察，並幫助研究人員高效地瀏覽大量論文。

以下是使用的不同步驟：
* 使用 [Text Analytics for Health](https://docs.microsoft.com/azure/cognitive-services/text-analytics/how-tos/text-analytics-for-health?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) 提取和預處理信息
* 使用 [Azure ML](https://azure.microsoft.com/services/machine-learning?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) 進行並行處理
* 使用 [Cosmos DB](https://azure.microsoft.com/services/cosmos-db?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) 存儲和查詢信息
* 使用 Power BI 創建交互式儀表板進行數據探索和可視化

查看完整過程，請訪問 [Dmitry 的博客](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/)。

如您所見，我們可以以多種方式利用雲端服務來進行資料科學。

## 備註

來源：
* https://azure.microsoft.com/overview/what-is-cloud-computing?ocid=AID3041109  
* https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?ocid=AID3041109  
* https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/  

## 課後測驗

## [課後測驗](https://ff-quizzes.netlify.app/en/ds/quiz/33)

## 作業

[市場研究](assignment.md)

---

**免責聲明**：  
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原始語言的文件作為權威來源。對於關鍵資訊，建議尋求專業人工翻譯。我們對因使用此翻譯而產生的任何誤解或錯誤解讀概不負責。