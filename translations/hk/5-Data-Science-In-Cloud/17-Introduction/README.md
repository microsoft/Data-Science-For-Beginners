<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6a0556b17de4c8d1a9470b02247b01d4",
  "translation_date": "2025-09-04T12:41:27+00:00",
  "source_file": "5-Data-Science-In-Cloud/17-Introduction/README.md",
  "language_code": "hk"
}
-->
# 雲端中的數據科學入門

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/17-DataScience-Cloud.png)|
|:---:|
| 雲端中的數據科學：入門 - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

在這節課中，你將學習雲端的基本原則，了解為什麼使用雲端服務來執行數據科學項目可能對你有吸引力，並且我們會看一些在雲端中運行的數據科學項目示例。

## [課前測驗](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/32)

## 什麼是雲端？

雲端，或稱雲端計算，是通過互聯網提供一系列按需付費的計算服務，這些服務基於一個基礎設施。服務包括存儲、數據庫、網絡、軟件、分析以及智能服務等解決方案。

我們通常將公有雲、私有雲和混合雲區分如下：

* 公有雲：公有雲由第三方雲端服務提供商擁有和運營，並通過互聯網向公眾提供其計算資源。
* 私有雲：私有雲指的是專門由單一企業或組織使用的雲端計算資源，服務和基礎設施維護在私有網絡上。
* 混合雲：混合雲是一種結合公有雲和私有雲的系統。用戶選擇使用內部數據中心，同時允許數據和應用程序在一個或多個公有雲上運行。

大多數雲端計算服務分為三類：基礎設施即服務（IaaS）、平台即服務（PaaS）和軟件即服務（SaaS）。

* 基礎設施即服務（IaaS）：用戶租用IT基礎設施，例如伺服器和虛擬機（VM）、存儲、網絡、操作系統。
* 平台即服務（PaaS）：用戶租用一個開發、測試、交付和管理軟件應用程序的環境。用戶不需要擔心設置或管理開發所需的伺服器、存儲、網絡和數據庫等基礎設施。
* 軟件即服務（SaaS）：用戶通過互聯網按需訪問軟件應用程序，通常是基於訂閱模式。用戶不需要擔心托管和管理軟件應用程序、基礎設施或維護，例如軟件升級和安全修補。

一些最大的雲端提供商包括 Amazon Web Services、Google Cloud Platform 和 Microsoft Azure。

## 為什麼選擇雲端進行數據科學？

開發者和IT專業人士選擇使用雲端的原因有很多，包括以下幾點：

* 創新：你可以通過將雲端提供商創建的創新服務直接整合到你的應用程序中來提升應用程序的能力。
* 靈活性：你只需支付所需的服務費用，並可以從多種服務中選擇。通常採用按需付費模式，並根據不斷變化的需求調整服務。
* 預算：你不需要進行初期投資來購買硬件和軟件，設置和運行本地數據中心，只需支付使用的費用。
* 可擴展性：你的資源可以根據項目的需求進行擴展，這意味著你的應用程序可以根據外部因素在任何時間使用更多或更少的計算能力、存儲和帶寬。
* 生產力：你可以專注於你的業務，而不是花時間處理可以由其他人管理的任務，例如管理數據中心。
* 可靠性：雲端計算提供多種方式來持續備份你的數據，並可以設置災難恢復計劃，即使在危機時期也能保持業務和服務的運行。
* 安全性：你可以受益於加強項目安全性的政策、技術和控制措施。

以上是人們選擇使用雲端服務的一些常見原因。現在我們對雲端及其主要優勢有了更好的理解，讓我們更具體地了解數據科學家和處理數據的開發者的工作，以及雲端如何幫助他們解決可能面臨的幾個挑戰：

* 存儲大量數據：與其購買、管理和保護大型伺服器，你可以直接將數據存儲在雲端，例如使用 Azure Cosmos DB、Azure SQL Database 和 Azure Data Lake Storage。
* 執行數據整合：數據整合是數據科學的重要部分，讓你從數據收集過渡到採取行動。通過雲端提供的數據整合服務，你可以從多個來源收集、轉換和整合數據到單一數據倉庫，例如使用 Data Factory。
* 處理數據：處理大量數據需要大量計算能力，而並非每個人都能獲得足夠強大的機器，因此許多人選擇直接利用雲端的巨大計算能力來運行和部署解決方案。
* 使用數據分析服務：雲端服務如 Azure Synapse Analytics、Azure Stream Analytics 和 Azure Databricks 可以幫助你將數據轉化為可行的洞察。
* 使用機器學習和數據智能服務：與其從零開始，你可以使用雲端提供商提供的機器學習算法，例如 AzureML。你還可以使用認知服務，例如語音轉文字、文字轉語音、計算機視覺等。

## 雲端中的數據科學示例

讓我們通過幾個場景來使這些概念更具體化。

### 實時社交媒體情感分析
我們從一個常見的機器學習入門場景開始：實時社交媒體情感分析。

假設你運營一個新聞媒體網站，並希望利用實時數據來了解讀者可能感興趣的內容。為了更好地了解這一點，你可以構建一個程序，對 Twitter 上與讀者相關的主題進行實時情感分析。

你需要關注的關鍵指標是特定主題（標籤）的推文量和情感，情感是通過分析工具對指定主題進行情感分析得出的。

創建此項目所需的步驟如下：

* 創建一個事件中心來收集 Twitter 的流式輸入數據
* 配置並啟動 Twitter 客戶端應用程序，調用 Twitter Streaming APIs
* 創建一個流分析作業
* 指定作業輸入和查詢
* 創建輸出接收器並指定作業輸出
* 啟動作業

查看完整過程，請參考[文檔](https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?WT.mc_id=academic-77958-bethanycheum&ocid=AID30411099)。

### 科學論文分析
讓我們看另一個由本課程作者之一 [Dmitry Soshnikov](http://soshnikov.com) 創建的項目示例。

Dmitry 創建了一個工具來分析 COVID 論文。通過審視這個項目，你將看到如何創建一個工具，從科學論文中提取知識，獲得洞察，並幫助研究人員高效地瀏覽大量論文。

以下是使用的不同步驟：
* 使用 [Text Analytics for Health](https://docs.microsoft.com/azure/cognitive-services/text-analytics/how-tos/text-analytics-for-health?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) 提取和預處理信息
* 使用 [Azure ML](https://azure.microsoft.com/services/machine-learning?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) 進行並行處理
* 使用 [Cosmos DB](https://azure.microsoft.com/services/cosmos-db?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) 存儲和查詢信息
* 使用 Power BI 創建交互式儀表板進行數據探索和可視化

查看完整過程，請訪問 [Dmitry 的博客](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/)。

如你所見，我們可以以多種方式利用雲端服務來進行數據科學。

## 備註

來源：
* https://azure.microsoft.com/overview/what-is-cloud-computing?ocid=AID3041109  
* https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?ocid=AID3041109  
* https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/  

## 課後測驗

## [課後測驗](https://ff-quizzes.netlify.app/en/ds/)

## 作業

[市場研究](assignment.md)

---

**免責聲明**：  
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯。我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原始語言的文件作為權威來源。對於關鍵資訊，建議尋求專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解讀概不負責。