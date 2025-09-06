<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "06bac7959b46b6e8aedcae014278c476",
  "translation_date": "2025-09-06T07:04:41+00:00",
  "source_file": "6-Data-Science-In-Wild/20-Real-World-Examples/README.md",
  "language_code": "mo"
}
-->
# 數據科學在現實世界中的應用

| ![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-RealWorld.png) |
| :--------------------------------------------------------------------------------------------------------------: |
|               數據科學在現實世界中的應用 - _Sketchnote by [@nitya](https://twitter.com/nitya)_               |

我們的學習旅程即將結束！

我們從數據科學和倫理的定義開始，探索了各種數據分析和可視化工具與技術，回顧了數據科學的生命周期，並研究了如何利用雲端計算服務擴展和自動化數據科學工作流程。所以，你可能會想：_"如何將這些學到的知識應用到現實世界中？"_

在這節課中，我們將探討數據科學在各行業中的實際應用，並深入研究在研究、數字人文和可持續性方面的具體例子。我們還會介紹學生項目機會，並提供一些有用的資源，幫助你繼續學習旅程！

## 課前測驗

## [課前測驗](https://ff-quizzes.netlify.app/en/ds/quiz/38)

## 數據科學 + 行業

隨著人工智能的普及化，開發者現在更容易設計和整合基於人工智能的決策和數據驅動的洞察到用戶體驗和開發工作流程中。以下是數據科學在各行業中的一些實際應用例子：

 * [Google Flu Trends](https://www.wired.com/2015/10/can-learn-epic-failure-google-flu-trends/) 使用數據科學將搜索詞與流感趨勢相關聯。雖然這種方法存在缺陷，但它提高了人們對數據驅動的醫療預測可能性（以及挑戰）的認識。

 * [UPS 路線預測](https://www.technologyreview.com/2018/11/21/139000/how-ups-uses-ai-to-outsmart-bad-weather/) - 解釋了 UPS 如何利用數據科學和機器學習來預測最佳配送路線，考慮到天氣條件、交通模式、配送截止時間等因素。

 * [紐約市出租車路線可視化](http://chriswhong.github.io/nyctaxi/) - 使用[信息自由法](https://chriswhong.com/open-data/foil_nyc_taxi/)收集的數據幫助可視化紐約市出租車一天的運行情況，幫助我們了解它們如何在繁忙的城市中穿梭、賺取的收入以及每24小時內行程的持續時間。

 * [Uber 數據科學工作台](https://eng.uber.com/dsw/) - 利用每天從數百萬次 Uber 行程中收集的數據（如接送地點、行程時長、偏好路線等），構建數據分析工具，用於定價、安全、欺詐檢測和導航決策。

 * [體育分析](https://towardsdatascience.com/scope-of-analytics-in-sports-world-37ed09c39860) - 專注於_預測分析_（團隊和球員分析，例如[Moneyball](https://datasciencedegree.wisconsin.edu/blog/moneyball-proves-importance-big-data-big-ideas/)）和_數據可視化_（團隊和粉絲儀表板、比賽等），應用於人才挖掘、體育博彩和場地管理。

 * [銀行業中的數據科學](https://data-flair.training/blogs/data-science-in-banking/) - 強調數據科學在金融行業的價值，應用包括風險建模和欺詐檢測、客戶分群、實時預測和推薦系統。預測分析還推動了關鍵指標，如[信用評分](https://dzone.com/articles/using-big-data-and-predictive-analytics-for-credit)。

 * [醫療中的數據科學](https://data-flair.training/blogs/data-science-in-healthcare/) - 強調應用包括醫學影像（如 MRI、X光、CT掃描）、基因組學（DNA測序）、藥物開發（風險評估、成功預測）、預測分析（患者護理和供應物流）、疾病追蹤和預防等。

![數據科學在現實世界中的應用](../../../../6-Data-Science-In-Wild/20-Real-World-Examples/images/data-science-applications.png) 圖片來源：[Data Flair: 6 Amazing Data Science Applications ](https://data-flair.training/blogs/data-science-applications/)

該圖展示了其他領域和應用數據科學技術的例子。想探索更多應用？請查看下面的[回顧與自學](../../../../6-Data-Science-In-Wild/20-Real-World-Examples)部分。

## 數據科學 + 研究

| ![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-Research.png) |
| :---------------------------------------------------------------------------------------------------------------: |
|              數據科學與研究 - _Sketchnote by [@nitya](https://twitter.com/nitya)_              |

雖然現實世界的應用通常專注於行業中的大規模使用案例，_研究_應用和項目可以從兩個角度提供價值：

* _創新機會_ - 探索先進概念的快速原型設計以及下一代應用的用戶體驗測試。
* _部署挑戰_ - 調查數據科學技術在現實世界中的潛在危害或意外後果。

對於學生來說，這些研究項目既能提供學習機會，也能促進合作，幫助你加深對主題的理解，並擴展你與相關領域的專家或團隊的接觸和參與。那麼研究項目是什麼樣的？它們如何產生影響？

讓我們看一個例子——[MIT Gender Shades Study](http://gendershades.org/overview.html)，由 Joy Buolamwini（MIT Media Labs）領導，並與 Timnit Gebru（當時在 Microsoft Research）共同撰寫了一篇[重要研究論文](http://proceedings.mlr.press/v81/buolamwini18a/buolamwini18a.pdf)，該研究專注於：

 * **什麼：** 該研究項目的目的是_評估基於性別和膚色的自動面部分析算法和數據集中的偏差_。
 * **為什麼：** 面部分析被用於執法、機場安檢、招聘系統等領域——在這些情境中，由於偏差導致的不準確分類可能對受影響的個人或群體造成潛在的經濟和社會危害。理解（並消除或減輕）偏差是使用公平性的關鍵。
 * **如何：** 研究人員認識到現有基準主要使用膚色較淺的受試者，並策劃了一個新的數據集（1000+圖像），該數據集在性別和膚色方面更加平衡。該數據集被用於評估三個性別分類產品（來自 Microsoft、IBM 和 Face++）的準確性。

結果顯示，雖然整體分類準確性良好，但不同子群體之間的錯誤率存在顯著差異——女性或膚色較深的人群的**性別錯誤分類**更高，表明存在偏差。

**主要成果：** 提高了人們對數據科學需要更多_代表性數據集_（平衡的子群體）和更多_包容性團隊_（多樣化背景）的認識，以便在人工智能解決方案中更早地識別並消除或減輕這些偏差。像這樣的研究努力對許多組織制定負責任人工智能的原則和實踐也至關重要，以改善其人工智能產品和流程的公平性。

**想了解 Microsoft 的相關研究工作？**

* 查看 [Microsoft Research Projects](https://www.microsoft.com/research/research-area/artificial-intelligence/?facet%5Btax%5D%5Bmsr-research-area%5D%5B%5D=13556&facet%5Btax%5D%5Bmsr-content-type%5D%5B%5D=msr-project) 中的人工智能研究項目。
* 探索 [Microsoft Research Data Science Summer School](https://www.microsoft.com/en-us/research/academic-program/data-science-summer-school/) 的學生項目。
* 查看 [Fairlearn](https://fairlearn.org/) 項目和 [Responsible AI](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1%3aprimaryr6) 的倡議。

## 數據科學 + 人文

| ![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-Humanities.png) |
| :---------------------------------------------------------------------------------------------------------------: |
|              數據科學與數字人文 - _Sketchnote by [@nitya](https://twitter.com/nitya)_              |

數字人文[被定義為](https://digitalhumanities.stanford.edu/about-dh-stanford)“結合計算方法與人文探究的一系列實踐和方法”。[斯坦福項目](https://digitalhumanities.stanford.edu/projects)如_“重啟歷史”_和_“詩意思考”_展示了[數字人文與數據科學](https://digitalhumanities.stanford.edu/digital-humanities-and-data-science)之間的聯繫——強調網絡分析、信息可視化、空間和文本分析等技術，幫助我們重新審視歷史和文學數據集，從中獲得新的洞察和視角。

*想探索並擴展這一領域的項目？*

查看 ["Emily Dickinson and the Meter of Mood"](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671)——一個來自 [Jen Looper](https://twitter.com/jenlooper) 的精彩例子，探討如何利用數據科學重新審視熟悉的詩歌，並在新的背景下重新評估其意義及作者的貢獻。例如，_我們能否通過分析詩歌的語氣或情感來預測其創作季節_——這對於作者在相關時期的心理狀態有何啟示？

為了回答這個問題，我們遵循數據科學生命周期的步驟：
 * [`數據獲取`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#acquiring-the-dataset) - 收集相關數據集進行分析。選項包括使用 API（例如 [Poetry DB API](https://poetrydb.org/index.html)）或使用工具（如 [Scrapy](https://scrapy.org/)）抓取網頁（例如 [Project Gutenberg](https://www.gutenberg.org/files/12242/12242-h/12242-h.htm)）。
 * [`數據清理`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#clean-the-data) - 解釋如何使用基本工具（如 Visual Studio Code 和 Microsoft Excel）格式化、清理和簡化文本。
 * [`數據分析`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#working-with-the-data-in-a-notebook) - 解釋如何將數據集導入“筆記本”進行分析，使用 Python 包（如 pandas、numpy 和 matplotlib）組織和可視化數據。
 * [`情感分析`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#sentiment-analysis-using-cognitive-services) - 解釋如何使用低代碼工具（如 [Power Automate](https://flow.microsoft.com/en-us/)）集成雲服務（如文本分析）進行自動化數據處理工作流程。

通過這一工作流程，我們可以探索季節對詩歌情感的影響，並幫助我們形成對作者的獨特視角。自己試試看——然後擴展筆記本，提出其他問題或以新的方式可視化數據！

> 你可以使用 [Digital Humanities toolkit](https://github.com/Digital-Humanities-Toolkit) 中的一些工具來探索這些研究方向。

## 數據科學 + 可持續性

| ![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-Sustainability.png) |
| :---------------------------------------------------------------------------------------------------------------: |
|              數據科學與可持續性 - _Sketchnote by [@nitya](https://twitter.com/nitya)_              |

[2030可持續發展議程](https://sdgs.un.org/2030agenda)——由所有聯合國成員於2015年通過——確定了17個目標，其中包括專注於**保護地球**免受退化和氣候變化影響的目標。[Microsoft Sustainability](https://www.microsoft.com/en-us/sustainability)倡議支持這些目標，探索技術解決方案如何支持並構建更可持續的未來，並專注於[四個目標](https://dev.to/azure/a-visual-guide-to-sustainable-software-engineering-53hh)——到2030年實現碳負、正水、零廢物和生物多樣性。

以可擴展和及時的方式應對這些挑戰需要雲端規模的思維——以及大規模數據。[Planetary Computer](https://planetarycomputer.microsoft.com/)倡議提供了四個組件，幫助數據科學家和開發者應對這一努力：

 * [數據目錄](https://planetarycomputer.microsoft.com/catalog) - 提供地球系統數據的PB級數據（免費且托管於Azure）。
 * [Planetary API](https://planetarycomputer.microsoft.com/docs/reference/stac/) - 幫助用戶在空間和時間上搜索相關數據。
 * [Hub](https://planetarycomputer.microsoft.com/docs/overview/environment/) - 為科學家提供處理大規模地理空間數據集的管理環境。
 * [應用](https://planetarycomputer.microsoft.com/applications) - 展示可持續性洞察的使用案例和工具。
**Planetary Computer Project 目前處於預覽階段（截至 2021 年 9 月）** - 以下是如何開始使用數據科學為可持續性解決方案做出貢獻的指南。

* [申請訪問權限](https://planetarycomputer.microsoft.com/account/request)，開始探索並與同行建立聯繫。
* [探索文件](https://planetarycomputer.microsoft.com/docs/overview/about)，了解支持的數據集和 API。
* 探索像 [生態系統監測](https://analytics-lab.org/ecosystemmonitoring/) 這樣的應用，尋找應用創意的靈感。

思考如何利用數據可視化揭示或放大與氣候變化和森林砍伐等相關的洞察。或者思考如何利用洞察創造新的用戶體驗，激勵行為改變以實現更可持續的生活。

## 數據科學 + 學生

我們已經討論了行業和研究中的實際應用，並探索了數字人文和可持續性中的數據科學應用示例。那麼，作為數據科學初學者，你如何提升技能並分享專業知識呢？

以下是一些數據科學學生項目示例，供你參考。

 * [MSR 數據科學夏季學校](https://www.microsoft.com/en-us/research/academic-program/data-science-summer-school/#!projects) 的 GitHub [項目](https://github.com/msr-ds3)，探索以下主題：
    - [警察使用武力中的種族偏見](https://www.microsoft.com/en-us/research/video/data-science-summer-school-2019-replicating-an-empirical-analysis-of-racial-differences-in-police-use-of-force/) | [Github](https://github.com/msr-ds3/stop-question-frisk)
    - [紐約地鐵系統的可靠性](https://www.microsoft.com/en-us/research/video/data-science-summer-school-2018-exploring-the-reliability-of-the-nyc-subway-system/) | [Github](https://github.com/msr-ds3/nyctransit)
 * [數字化物質文化：探索 Sirkap 的社會經濟分佈](https://claremont.maps.arcgis.com/apps/Cascade/index.html?appid=bdf2aef0f45a4674ba41cd373fa23afc) - 由 [Ornella Altunyan](https://twitter.com/ornelladotcom) 和 Claremont 團隊使用 [ArcGIS StoryMaps](https://storymaps.arcgis.com/) 完成。

## 🚀 挑戰

搜尋推薦適合初學者的數據科學項目文章，例如 [這 50 個主題領域](https://www.upgrad.com/blog/data-science-project-ideas-topics-beginners/)、[這 21 個項目創意](https://www.intellspot.com/data-science-project-ideas) 或 [這 16 個帶有源代碼的項目](https://data-flair.training/blogs/data-science-project-ideas/)，你可以拆解並重新組合。別忘了記錄你的學習旅程，並與大家分享你的洞察。

## 課後測驗

## [課後測驗](https://ff-quizzes.netlify.app/en/ds/quiz/39)

## 回顧與自學

想探索更多用例嗎？以下是一些相關文章：
 * [17 個數據科學應用和示例](https://builtin.com/data-science/data-science-applications-examples) - 2021 年 7 月
 * [11 個令人驚嘆的數據科學實際應用](https://myblindbird.com/data-science-applications-real-world/) - 2021 年 5 月
 * [數據科學在現實世界中的應用](https://towardsdatascience.com/data-science-in-the-real-world/home) - 文章合集
 * 數據科學在：[教育](https://data-flair.training/blogs/data-science-in-education/)、[農業](https://data-flair.training/blogs/data-science-in-agriculture/)、[金融](https://data-flair.training/blogs/data-science-in-finance/)、[電影](https://data-flair.training/blogs/data-science-at-movies/) 等領域。

## 作業

[探索 Planetary Computer 數據集](assignment.md)

---

**免責聲明**：  
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們努力確保翻譯的準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於關鍵信息，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤釋不承擔責任。