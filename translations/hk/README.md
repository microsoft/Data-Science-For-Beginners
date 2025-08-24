<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6bb17a440fdabf0823105136a5b81029",
  "translation_date": "2025-08-24T11:51:12+00:00",
  "source_file": "README.md",
  "language_code": "hk"
}
-->
# 初學者的數據科學課程

Azure Cloud Advocates 團隊很高興為大家提供一個為期10週、共20課的數據科學課程。每節課都包含課前和課後測驗、詳細的課程指導、解決方案以及作業。我們採用基於項目的教學法，讓您在實際操作中學習，這是一種能讓新技能更牢固掌握的有效方法。

**衷心感謝我們的作者：** [Jasmine Greenaway](https://www.twitter.com/paladique)、[Dmitry Soshnikov](http://soshnikov.com)、[Nitya Narasimhan](https://twitter.com/nitya)、[Jalen McGee](https://twitter.com/JalenMcG)、[Jen Looper](https://twitter.com/jenlooper)、[Maud Levy](https://twitter.com/maudstweets)、[Tiffany Souterre](https://twitter.com/TiffanySouterre)、[Christopher Harrison](https://www.twitter.com/geektrainer)。

**🙏 特別感謝 🙏 我們的 [Microsoft 學生大使](https://studentambassadors.microsoft.com/) 作者、審稿人和內容貢獻者，** 特別是 Aaryan Arora、[Aditya Garg](https://github.com/AdityaGarg00)、[Alondra Sanchez](https://www.linkedin.com/in/alondra-sanchez-molina/)、[Ankita Singh](https://www.linkedin.com/in/ankitasingh007)、[Anupam Mishra](https://www.linkedin.com/in/anupam--mishra/)、[Arpita Das](https://www.linkedin.com/in/arpitadas01)、ChhailBihari Dubey、[Dibri Nsofor](https://www.linkedin.com/in/dibrinsofor)、[Dishita Bhasin](https://www.linkedin.com/in/dishita-bhasin-7065281bb)、[Majd Safi](https://www.linkedin.com/in/majd-s/)、[Max Blum](https://www.linkedin.com/in/max-blum-6036a1186/)、[Miguel Correa](https://www.linkedin.com/in/miguelmque/)、[Mohamma Iftekher (Iftu) Ebne Jalal](https://twitter.com/iftu119)、[Nawrin Tabassum](https://www.linkedin.com/in/nawrin-tabassum)、[Raymond Wangsa Putra](https://www.linkedin.com/in/raymond-wp/)、[Rohit Yadav](https://www.linkedin.com/in/rty2423)、Samridhi Sharma、[Sanya Sinha](https://www.linkedin.com/mwlite/in/sanya-sinha-13aab1200)、[Sheena Narula](https://www.linkedin.com/in/sheena-narua-n/)、[Tauqeer Ahmad](https://www.linkedin.com/in/tauqeerahmad5201/)、Yogendrasingh Pawar、[Vidushi Gupta](https://www.linkedin.com/in/vidushi-gupta07/)、[Jasleen Sondhi](https://www.linkedin.com/in/jasleen-sondhi/)。

|![由 [(@sketchthedocs)](https://sketchthedocs.dev) 繪製的速寫筆記](./sketchnotes/00-Title.png)|
|:---:|
| 初學者的數據科學 - _速寫筆記由 [@nitya](https://twitter.com/nitya) 繪製_ |

## 公告 - 新的生成式 AI 課程已發布！

我們剛剛發布了一個包含12課的生成式 AI 課程。學習內容包括：

- 提示設計與提示工程
- 文本與圖像應用生成
- 搜索應用

和往常一樣，每節課都包含課程內容、作業、知識檢查和挑戰。

查看課程：

> https://aka.ms/genai-beginners

# 你是學生嗎？

可以從以下資源開始：

- [學生中心頁面](https://docs.microsoft.com/en-gb/learn/student-hub?WT.mc_id=academic-77958-bethanycheum) 在這個頁面中，您可以找到初學者資源、學生包，甚至有機會獲得免費認證券。這是一個值得收藏並定期查看的頁面，因為我們至少每月更新一次內容。
- [Microsoft Learn 學生大使](https://studentambassadors.microsoft.com?WT.mc_id=academic-77958-bethanycheum) 加入全球學生大使社群，這可能是您進入 Microsoft 的途徑。

# 開始學習

> **教師們**：我們[提供了一些建議](for-teachers.md)來幫助您使用這個課程。我們非常期待您在[討論論壇](https://github.com/microsoft/Data-Science-For-Beginners/discussions)中的反饋！

> **[學生們](https://aka.ms/student-page)**：如果您想自行使用這個課程，可以 fork 整個 repo 並自行完成練習，從課前測驗開始。然後閱讀課程內容並完成其他活動。嘗試通過理解課程來創建項目，而不是直接複製解決方案代碼；不過，解決方案代碼可以在每個基於項目的課程的 /solutions 文件夾中找到。另一個建議是與朋友組成學習小組，一起學習內容。進一步學習的話，我們推薦 [Microsoft Learn](https://docs.microsoft.com/en-us/users/jenlooper-2911/collections/qprpajyoy3x0g7?WT.mc_id=academic-77958-bethanycheum)。

## 認識團隊

[![宣傳視頻](../../ds-for-beginners.gif)](https://youtu.be/8mzavjQSMM4 "宣傳視頻")

**Gif 作者** [Mohit Jaisal](https://www.linkedin.com/in/mohitjaisal)

> 🎥 點擊上方圖片觀看關於這個項目及其創作者的視頻！

## 教學法

我們在設計這個課程時選擇了兩個教學原則：確保課程是基於項目的，並且包含頻繁的測驗。在這個系列結束時，學生將學習到數據科學的基本原則，包括倫理概念、數據準備、不同的數據處理方式、數據可視化、數據分析、數據科學的實際應用案例等。

此外，課前的低壓測驗可以幫助學生集中注意力學習某個主題，而課後的測驗則能進一步加深記憶。這個課程設計靈活有趣，可以完整學習，也可以選擇部分內容。項目從簡單開始，到10週課程結束時逐漸變得複雜。

> 查看我們的 [行為準則](CODE_OF_CONDUCT.md)、[貢獻指南](CONTRIBUTING.md)、[翻譯指南](TRANSLATIONS.md)。我們歡迎您的建設性反饋！

## 每節課包括：

- 可選的速寫筆記
- 可選的補充視頻
- 課前熱身測驗
- 書面課程
- 對於基於項目的課程，提供逐步指導如何完成項目
- 知識檢查
- 挑戰
- 補充閱讀
- 作業
- 課後測驗

> **關於測驗的說明**：所有測驗都包含在 Quiz-App 文件夾中，共40個測驗，每個測驗有三個問題。測驗在課程中有鏈接，但測驗應用可以在本地運行或部署到 Azure；請按照 `quiz-app` 文件夾中的指導進行操作。測驗正在逐步本地化。

## 課程列表

|![由 [(@sketchthedocs)](https://sketchthedocs.dev) 繪製的速寫筆記](./sketchnotes/00-Roadmap.png)|
|:---:|
| 初學者的數據科學：課程路線圖 - _速寫筆記由 [@nitya](https://twitter.com/nitya) 繪製_ |

| 課程編號 | 主題 | 課程分組 | 學習目標 | 課程鏈接 | 作者 |
| :-----------: | :----------------------------------------: | :--------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------: | :----: |
| 01 | 定義數據科學 | [介紹](1-Introduction/README.md) | 學習數據科學的基本概念及其與人工智能、機器學習和大數據的關係。 | [課程](1-Introduction/01-defining-data-science/README.md) [視頻](https://youtu.be/beZ7Mb_oz9I) | [Dmitry](http://soshnikov.com) |
| 02 | 數據科學倫理 | [介紹](1-Introduction/README.md) | 數據倫理的概念、挑戰與框架。 | [課程](1-Introduction/02-ethics/README.md) | [Nitya](https://twitter.com/nitya) |
| 03 | 定義數據 | [介紹](1-Introduction/README.md) | 數據的分類及其常見來源。 | [課程](1-Introduction/03-defining-data/README.md) | [Jasmine](https://www.twitter.com/paladique) |
| 04 | 統計與概率入門 | [介紹](1-Introduction/README.md) | 使用概率和統計的數學技術來理解數據。 | [課程](1-Introduction/04-stats-and-probability/README.md) [視頻](https://youtu.be/Z5Zy85g4Yjw) | [Dmitry](http://soshnikov.com) |
| 05 | 使用關聯數據 | [數據處理](2-Working-With-Data/README.md) | 介紹關聯數據及使用結構化查詢語言（SQL）探索和分析關聯數據的基礎知識。 | [課程](2-Working-With-Data/05-relational-databases/README.md) | [Christopher](https://www.twitter.com/geektrainer) | | |
| 06 | 使用 NoSQL 數據 | [數據處理](2-Working-With-Data/README.md) | 介紹非關聯數據的各種類型及探索和分析文檔數據庫的基礎知識。 | [課程](2-Working-With-Data/06-non-relational/README.md) | [Jasmine](https://twitter.com/paladique)|
| 07 | 使用 Python | [數據處理](2-Working-With-Data/README.md) | 使用 Python 進行數據探索的基礎知識，包括使用 Pandas 等庫。建議具備 Python 編程的基礎知識。 | [課程](2-Working-With-Data/07-python/README.md) [視頻](https://youtu.be/dZjWOGbsN4Y) | [Dmitry](http://soshnikov.com) |
| 08 | 數據準備 | [處理數據](2-Working-With-Data/README.md) | 有關清理和轉換數據的技術主題，以應對缺失、不準確或不完整數據的挑戰。 | [課程](2-Working-With-Data/08-data-preparation/README.md) | [Jasmine](https://www.twitter.com/paladique) |
| 09 | 數量可視化 | [數據可視化](3-Data-Visualization/README.md) | 學習如何使用 Matplotlib 可視化鳥類數據 🦆 | [課程](3-Data-Visualization/09-visualization-quantities/README.md) | [Jen](https://twitter.com/jenlooper) |
| 10 | 數據分佈可視化 | [數據可視化](3-Data-Visualization/README.md) | 可視化區間內的觀察和趨勢。 | [課程](3-Data-Visualization/10-visualization-distributions/README.md) | [Jen](https://twitter.com/jenlooper) |
| 11 | 比例可視化 | [數據可視化](3-Data-Visualization/README.md) | 可視化離散和分組百分比。 | [課程](3-Data-Visualization/11-visualization-proportions/README.md) | [Jen](https://twitter.com/jenlooper) |
| 12 | 關係可視化 | [數據可視化](3-Data-Visualization/README.md) | 可視化數據集及其變量之間的連接和相關性。 | [課程](3-Data-Visualization/12-visualization-relationships/README.md) | [Jen](https://twitter.com/jenlooper) |
| 13 | 有意義的可視化 | [數據可視化](3-Data-Visualization/README.md) | 提供使可視化更有價值的技術和指導，以便有效解決問題並獲得洞察。 | [課程](3-Data-Visualization/13-meaningful-visualizations/README.md) | [Jen](https://twitter.com/jenlooper) |
| 14 | 數據科學生命周期簡介 | [生命周期](4-Data-Science-Lifecycle/README.md) | 數據科學生命周期的簡介及其第一步：獲取和提取數據。 | [課程](4-Data-Science-Lifecycle/14-Introduction/README.md) | [Jasmine](https://twitter.com/paladique) |
| 15 | 分析 | [生命周期](4-Data-Science-Lifecycle/README.md) | 數據科學生命周期的這一階段專注於分析數據的技術。 | [課程](4-Data-Science-Lifecycle/15-analyzing/README.md) | [Jasmine](https://twitter.com/paladique) | | |
| 16 | 溝通 | [生命周期](4-Data-Science-Lifecycle/README.md) | 數據科學生命周期的這一階段專注於以易於決策者理解的方式呈現數據洞察。 | [課程](4-Data-Science-Lifecycle/16-communication/README.md) | [Jalen](https://twitter.com/JalenMcG) | | |
| 17 | 雲端中的數據科學 | [雲端數據](5-Data-Science-In-Cloud/README.md) | 這系列課程介紹了雲端中的數據科學及其優勢。 | [課程](5-Data-Science-In-Cloud/17-Introduction/README.md) | [Tiffany](https://twitter.com/TiffanySouterre) 和 [Maud](https://twitter.com/maudstweets) |
| 18 | 雲端中的數據科學 | [雲端數據](5-Data-Science-In-Cloud/README.md) | 使用低代碼工具訓練模型。 | [課程](5-Data-Science-In-Cloud/18-Low-Code/README.md) | [Tiffany](https://twitter.com/TiffanySouterre) 和 [Maud](https://twitter.com/maudstweets) |
| 19 | 雲端中的數據科學 | [雲端數據](5-Data-Science-In-Cloud/README.md) | 使用 Azure Machine Learning Studio 部署模型。 | [課程](5-Data-Science-In-Cloud/19-Azure/README.md)| [Tiffany](https://twitter.com/TiffanySouterre) 和 [Maud](https://twitter.com/maudstweets) |
| 20 | 野外的數據科學 | [野外應用](6-Data-Science-In-Wild/README.md) | 現實世界中的數據科學驅動項目。 | [課程](6-Data-Science-In-Wild/20-Real-World-Examples/README.md) | [Nitya](https://twitter.com/nitya) |

## GitHub Codespaces

按照以下步驟在 Codespace 中打開此範例：
1. 點擊 Code 下拉菜單，選擇 Open with Codespaces 選項。
2. 在面板底部選擇 + New codespace。
如需更多資訊，請查看 [GitHub 文檔](https://docs.github.com/en/codespaces/developing-in-codespaces/creating-a-codespace-for-a-repository#creating-a-codespace)。

## VSCode Remote - Containers
按照以下步驟使用本地機器和 VSCode 的 VS Code Remote - Containers 擴展在容器中打開此倉庫：

1. 如果您是第一次使用開發容器，請確保您的系統符合前置要求（例如已安裝 Docker），請參考 [入門文檔](https://code.visualstudio.com/docs/devcontainers/containers#_getting-started)。

要使用此倉庫，您可以選擇以下方式之一：

**注意**：在底層，這將使用 Remote-Containers: **Clone Repository in Container Volume...** 命令將源代碼克隆到 Docker 卷中，而不是本地文件系統。[卷](https://docs.docker.com/storage/volumes/) 是持久化容器數據的首選機制。

或者打開本地克隆或下載的倉庫版本：

- 將此倉庫克隆到您的本地文件系統。
- 按 F1 並選擇 **Remote-Containers: Open Folder in Container...** 命令。
- 選擇此文件夾的克隆副本，等待容器啟動，然後嘗試操作。

## 離線訪問

您可以使用 [Docsify](https://docsify.js.org/#/) 離線運行此文檔。Fork 此倉庫，在您的本地機器上 [安裝 Docsify](https://docsify.js.org/#/quickstart)，然後在此倉庫的根文件夾中輸入 `docsify serve`。網站將在本地端口 3000 上提供服務：`localhost:3000`。

> 注意，筆記本文件不會通過 Docsify 渲染，因此當您需要運行筆記本時，請在 VS Code 中使用 Python 核心單獨運行。

## 尋求幫助！

如果您希望翻譯全部或部分課程，請遵循我們的 [翻譯指南](TRANSLATIONS.md)。

## 其他課程

我們的團隊還製作了其他課程！查看以下內容：

- [生成式 AI 初學者課程](https://aka.ms/genai-beginners)
- [生成式 AI 初學者課程 .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [使用 JavaScript 的生成式 AI](https://github.com/microsoft/generative-ai-with-javascript)
- [使用 Java 的生成式 AI](https://aka.ms/genaijava)
- [AI 初學者課程](https://aka.ms/ai-beginners)
- [數據科學初學者課程](https://aka.ms/datascience-beginners)
- [機器學習初學者課程](https://aka.ms/ml-beginners)
- [網絡安全初學者課程](https://github.com/microsoft/Security-101) 
- [Web 開發初學者課程](https://aka.ms/webdev-beginners)
- [物聯網初學者課程](https://aka.ms/iot-beginners)
- [XR 開發初學者課程](https://github.com/microsoft/xr-development-for-beginners)
- [掌握 GitHub Copilot 進行配對編程](https://github.com/microsoft/Mastering-GitHub-Copilot-for-Paired-Programming)
- [掌握 GitHub Copilot 用於 C#/.NET 開發者](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers)
- [選擇您的 Copilot 冒險](https://github.com/microsoft/CopilotAdventures)

**免責聲明**：  
本文件使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原文文件作為權威來源。對於關鍵資訊，建議尋求專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤釋不承擔責任。