<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "408c55cab2880daa4e78616308bd5db7",
  "translation_date": "2025-08-25T17:28:29+00:00",
  "source_file": "5-Data-Science-In-Cloud/17-Introduction/README.md",
  "language_code": "hk"
}
-->
# 雲端中的數據科學簡介

|![ 由 [(@sketchthedocs)](https://sketchthedocs.dev) 繪製的手繪筆記 ](../../sketchnotes/17-DataScience-Cloud.png)|
|:---:|
| 雲端中的數據科學：簡介 - _手繪筆記由 [@nitya](https://twitter.com/nitya) 提供_ |

在這節課中，你將學習雲端的基本原則，了解為什麼使用雲端服務來運行數據科學項目對你可能有吸引力，並且我們還會看看一些在雲端運行的數據科學項目範例。

## [課前測驗](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/32)

## 什麼是雲端？

雲端，或稱雲端運算，是一種通過互聯網提供多種按需付費的運算服務的方式，這些服務基於一個基礎設施。服務包括存儲、數據庫、網絡、軟件、分析和智能服務等解決方案。

我們通常將雲端分為以下幾種類型：

* 公有雲：公有雲由第三方雲端服務提供商擁有和運營，並通過互聯網向公眾提供其運算資源。
* 私有雲：私有雲是指僅供單一企業或組織使用的雲端運算資源，其服務和基礎設施維護在一個私有網絡上。
* 混合雲：混合雲是一種結合了公有雲和私有雲的系統。用戶可以選擇使用內部數據中心，同時允許數據和應用程序在一個或多個公有雲上運行。

大多數雲端運算服務可分為三種類別：基礎設施即服務 (IaaS)、平台即服務 (PaaS) 和軟件即服務 (SaaS)。

* 基礎設施即服務 (IaaS)：用戶租用 IT 基礎設施，例如伺服器和虛擬機 (VM)、存儲、網絡和操作系統。
* 平台即服務 (PaaS)：用戶租用一個用於開發、測試、交付和管理軟件應用程序的環境。用戶無需擔心設置或管理開發所需的伺服器、存儲、網絡和數據庫等基礎設施。
* 軟件即服務 (SaaS)：用戶按需通過互聯網訪問軟件應用程序，通常以訂閱方式提供。用戶無需擔心託管和管理軟件應用程序、基礎設施或維護（如軟件升級和安全補丁）。

一些最大的雲端提供商包括 Amazon Web Services、Google Cloud Platform 和 Microsoft Azure。

## 為什麼選擇雲端進行數據科學？

開發者和 IT 專業人士選擇使用雲端的原因有很多，包括以下幾點：

* 創新：你可以通過將雲端提供商創建的創新服務直接整合到你的應用程序中來提升應用程序的功能。
* 靈活性：你只需支付所需的服務費用，並且可以從多種服務中進行選擇。通常採用按需付費模式，並根據不斷變化的需求調整服務。
* 預算：你無需進行初期投資來購買硬件和軟件，設置和運行內部數據中心，只需支付實際使用的費用。
* 可擴展性：你的資源可以根據項目的需求進行擴展，這意味著你的應用程序可以根據外部因素隨時調整計算能力、存儲和帶寬。
* 生產力：你可以專注於業務，而不是花時間處理可以由他人管理的任務，例如管理數據中心。
* 可靠性：雲端運算提供多種方式來持續備份數據，並且你可以設置災難恢復計劃，即使在危機時期也能保持業務和服務的運行。
* 安全性：你可以受益於加強項目安全性的政策、技術和控制措施。

這些是人們選擇使用雲端服務的一些常見原因。現在我們對雲端的基本概念和主要優勢有了更好的了解，接下來我們將更具體地探討數據科學家和處理數據的開發者的工作，以及雲端如何幫助他們應對可能面臨的多種挑戰：

* 存儲大量數據：與其購買、管理和保護大型伺服器，不如直接將數據存儲在雲端，例如使用 Azure Cosmos DB、Azure SQL Database 和 Azure Data Lake Storage 等解決方案。
* 執行數據整合：數據整合是數據科學的重要組成部分，它使你能夠從數據收集過渡到採取行動。通過雲端提供的數據整合服務，你可以使用 Data Factory 從多個來源收集、轉換和整合數據到一個單一的數據倉庫中。
* 處理數據：處理大量數據需要大量的計算能力，而並非每個人都能獲得足夠強大的機器，因此許多人選擇直接利用雲端的強大計算能力來運行和部署解決方案。
* 使用數據分析服務：雲端服務如 Azure Synapse Analytics、Azure Stream Analytics 和 Azure Databricks 可以幫助你將數據轉化為可行的洞察。
* 使用機器學習和數據智能服務：與其從零開始，你可以使用雲端提供商提供的機器學習算法，例如 AzureML。你還可以使用認知服務，例如語音轉文字、文字轉語音、計算機視覺等。

## 雲端中的數據科學範例

讓我們通過幾個場景來更具體地了解這些應用。

### 實時社交媒體情感分析

我們從一個常見的機器學習入門場景開始：實時社交媒體情感分析。

假設你運營一個新聞媒體網站，並希望利用實時數據來了解讀者可能感興趣的內容。為了更好地了解這一點，你可以構建一個程序，對 Twitter 上與讀者相關的主題進行實時情感分析。

你需要關注的關鍵指標是特定主題（標籤）的推文數量和情感，情感是通過使用分析工具對指定主題進行情感分析來確定的。

創建這個項目所需的步驟如下：

* 創建一個事件中心來流式輸入，收集來自 Twitter 的數據
* 配置並啟動一個 Twitter 客戶端應用程序，調用 Twitter Streaming APIs
* 創建一個 Stream Analytics 任務
* 指定任務輸入和查詢
* 創建一個輸出接收器並指定任務輸出
* 啟動任務

要查看完整過程，請參閱[文檔](https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?WT.mc_id=academic-77958-bethanycheum&ocid=AID30411099)。

### 科學論文分析

讓我們再看一個由本課程作者之一 [Dmitry Soshnikov](http://soshnikov.com) 創建的項目範例。

Dmitry 創建了一個分析 COVID 論文的工具。通過回顧這個項目，你將了解如何創建一個工具來從科學論文中提取知識、獲取洞察，並幫助研究人員高效地瀏覽大量論文。

以下是使用的不同步驟：

* 使用 [Text Analytics for Health](https://docs.microsoft.com/azure/cognitive-services/text-analytics/how-tos/text-analytics-for-health?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) 提取和預處理信息
* 使用 [Azure ML](https://azure.microsoft.com/services/machine-learning?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) 進行並行處理
* 使用 [Cosmos DB](https://azure.microsoft.com/services/cosmos-db?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) 存儲和查詢信息
* 使用 Power BI 創建一個交互式儀表板，用於數據探索和可視化

要查看完整過程，請訪問 [Dmitry 的博客](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/)。

正如你所見，我們可以以多種方式利用雲端服務來進行數據科學。

## 備註

來源：
* https://azure.microsoft.com/overview/what-is-cloud-computing?ocid=AID3041109  
* https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?ocid=AID3041109  
* https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/  

## 課後測驗

[課後測驗](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/33)

## 作業

[市場調查](assignment.md)

**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋概不負責。