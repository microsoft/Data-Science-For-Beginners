<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7332da4946897c5885e9ca5bc24de96b",
  "translation_date": "2025-09-06T10:39:57+00:00",
  "source_file": "README.md",
  "language_code": "mo"
}
-->
# 初學者的數據科學課程

Azure Cloud Advocates 團隊很高興提供一個為期 10 週、共 20 節課的課程，內容涵蓋數據科學的基礎知識。每節課包括課前和課後測驗、詳細的課程指導、解決方案以及作業。我們採用基於項目的教學方法，讓您在實際操作中學習，這是一種能讓新技能更牢固掌握的有效方式。

**衷心感謝我們的作者：** [Jasmine Greenaway](https://www.twitter.com/paladique)、[Dmitry Soshnikov](http://soshnikov.com)、[Nitya Narasimhan](https://twitter.com/nitya)、[Jalen McGee](https://twitter.com/JalenMcG)、[Jen Looper](https://twitter.com/jenlooper)、[Maud Levy](https://twitter.com/maudstweets)、[Tiffany Souterre](https://twitter.com/TiffanySouterre)、[Christopher Harrison](https://www.twitter.com/geektrainer)。

**🙏 特別感謝 🙏 我們的 [Microsoft 學生大使](https://studentambassadors.microsoft.com/) 作者、審稿人和內容貢獻者，** 特別是 Aaryan Arora、[Aditya Garg](https://github.com/AdityaGarg00)、[Alondra Sanchez](https://www.linkedin.com/in/alondra-sanchez-molina/)、[Ankita Singh](https://www.linkedin.com/in/ankitasingh007)、[Anupam Mishra](https://www.linkedin.com/in/anupam--mishra/)、[Arpita Das](https://www.linkedin.com/in/arpitadas01)、ChhailBihari Dubey、[Dibri Nsofor](https://www.linkedin.com/in/dibrinsofor)、[Dishita Bhasin](https://www.linkedin.com/in/dishita-bhasin-7065281bb)、[Majd Safi](https://www.linkedin.com/in/majd-s/)、[Max Blum](https://www.linkedin.com/in/max-blum-6036a1186/)、[Miguel Correa](https://www.linkedin.com/in/miguelmque/)、[Mohamma Iftekher (Iftu) Ebne Jalal](https://twitter.com/iftu119)、[Nawrin Tabassum](https://www.linkedin.com/in/nawrin-tabassum)、[Raymond Wangsa Putra](https://www.linkedin.com/in/raymond-wp/)、[Rohit Yadav](https://www.linkedin.com/in/rty2423)、Samridhi Sharma、[Sanya Sinha](https://www.linkedin.com/mwlite/in/sanya-sinha-13aab1200)、[Sheena Narula](https://www.linkedin.com/in/sheena-narua-n/)、[Tauqeer Ahmad](https://www.linkedin.com/in/tauqeerahmad5201/)、Yogendrasingh Pawar、[Vidushi Gupta](https://www.linkedin.com/in/vidushi-gupta07/)、[Jasleen Sondhi](https://www.linkedin.com/in/jasleen-sondhi/)。

|![由 @sketchthedocs 繪製的速寫筆記 https://sketchthedocs.dev](../../translated_images/00-Title.8af36cd35da1ac555b678627fbdc6e320c75f0100876ea41d30ea205d3b08d22.mo.png)|
|:---:|
| 初學者的數據科學 - _由 [@nitya](https://twitter.com/nitya) 繪製的速寫筆記_ |

### 🌐 多語言支持

#### 通過 GitHub Action 支持（自動化且始終保持最新）

[法語](../fr/README.md) | [西班牙語](../es/README.md) | [德語](../de/README.md) | [俄語](../ru/README.md) | [阿拉伯語](../ar/README.md) | [波斯語 (法爾西)](../fa/README.md) | [烏爾都語](../ur/README.md) | [中文 (簡體)](../zh/README.md) | [中文 (繁體，澳門)](./README.md) | [中文 (繁體，香港)](../hk/README.md) | [中文 (繁體，台灣)](../tw/README.md) | [日語](../ja/README.md) | [韓語](../ko/README.md) | [印地語](../hi/README.md) | [孟加拉語](../bn/README.md) | [馬拉地語](../mr/README.md) | [尼泊爾語](../ne/README.md) | [旁遮普語 (古木基文)](../pa/README.md) | [葡萄牙語 (葡萄牙)](../pt/README.md) | [葡萄牙語 (巴西)](../br/README.md) | [意大利語](../it/README.md) | [波蘭語](../pl/README.md) | [土耳其語](../tr/README.md) | [希臘語](../el/README.md) | [泰語](../th/README.md) | [瑞典語](../sv/README.md) | [丹麥語](../da/README.md) | [挪威語](../no/README.md) | [芬蘭語](../fi/README.md) | [荷蘭語](../nl/README.md) | [希伯來語](../he/README.md) | [越南語](../vi/README.md) | [印尼語](../id/README.md) | [馬來語](../ms/README.md) | [塔加洛語 (菲律賓語)](../tl/README.md) | [斯瓦希里語](../sw/README.md) | [匈牙利語](../hu/README.md) | [捷克語](../cs/README.md) | [斯洛伐克語](../sk/README.md) | [羅馬尼亞語](../ro/README.md) | [保加利亞語](../bg/README.md) | [塞爾維亞語 (西里爾文)](../sr/README.md) | [克羅地亞語](../hr/README.md) | [斯洛文尼亞語](../sl/README.md) | [烏克蘭語](../uk/README.md) | [緬甸語 (緬甸)](../my/README.md)

**如果您希望支持其他翻譯語言，請參考 [此處](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**

#### 加入我們的社群 
[![Azure AI Discord](https://dcbadge.limes.pink/api/server/kzRShWzttr)](https://discord.gg/kzRShWzttr)

# 您是學生嗎？

以下是一些資源，幫助您開始：

- [學生中心頁面](https://docs.microsoft.com/en-gb/learn/student-hub?WT.mc_id=academic-77958-bethanycheum) 在此頁面，您可以找到初學者資源、學生套件，甚至獲得免費認證憑證的方式。這是一個值得收藏並定期查看的頁面，因為我們至少每月更新一次內容。
- [Microsoft 學生大使](https://studentambassadors.microsoft.com?WT.mc_id=academic-77958-bethanycheum) 加入全球學生大使社群，這可能是您進入 Microsoft 的途徑。

# 開始使用

> **教師們**：我們已[提供一些建議](for-teachers.md)來幫助您使用此課程。我們期待您在[討論論壇](https://github.com/microsoft/Data-Science-For-Beginners/discussions)中提供反饋！

> **[學生們](https://aka.ms/student-page)**：如果您想自行使用此課程，請 fork 整個 repo 並自行完成練習，從課前測驗開始。然後閱讀課程並完成其餘活動。嘗試通過理解課程內容來創建項目，而不是直接複製解決方案代碼；不過，解決方案代碼可在每個基於項目的課程的 /solutions 文件夾中找到。另一個建議是與朋友組成學習小組，共同學習內容。若需進一步學習，我們推薦 [Microsoft Learn](https://docs.microsoft.com/en-us/users/jenlooper-2911/collections/qprpajyoy3x0g7?WT.mc_id=academic-77958-bethanycheum)。

## 認識團隊

[![宣傳影片](../../ds-for-beginners.gif)](https://youtu.be/8mzavjQSMM4 "宣傳影片")

**Gif 作者** [Mohit Jaisal](https://www.linkedin.com/in/mohitjaisal)

> 🎥 點擊上方圖片觀看關於此項目及創建者的影片！

## 教學方法

我們在設計此課程時選擇了兩個教學原則：確保課程是基於項目的，並且包含頻繁的測驗。在本系列結束時，學生將學習到數據科學的基本原則，包括倫理概念、數據準備、不同的數據處理方式、數據可視化、數據分析、數據科學的實際應用案例等。

此外，課前的低壓測驗能幫助學生集中注意力學習某個主題，而課後的第二次測驗則能進一步加深記憶。此課程設計靈活有趣，可以完整學習或部分選修。項目從簡單開始，並在 10 週的課程周期內逐漸變得複雜。
> 查看我們的[行為準則](CODE_OF_CONDUCT.md)、[貢獻指南](CONTRIBUTING.md)、[翻譯指南](TRANSLATIONS.md)。我們歡迎您的建設性反饋！
## 每節課包含：

- 可選的手繪筆記
- 可選的補充影片
- 課前暖身測驗
- 書面課程
- 專案型課程的逐步指導
- 知識檢查
- 挑戰題
- 補充閱讀
- 作業
- [課後測驗](https://ff-quizzes.netlify.app/en/)

> **關於測驗的說明**：所有測驗都存放在 Quiz-App 資料夾中，共有 40 個測驗，每個測驗包含三個問題。這些測驗已在課程中提供連結，但測驗應用程式可以在本地運行或部署到 Azure，請按照 `quiz-app` 資料夾中的指示操作。目前測驗正在逐步進行本地化。

## 課程

|![由 @sketchthedocs 繪製的手繪筆記 https://sketchthedocs.dev](../../translated_images/00-Roadmap.4905d6567dff47532b9bfb8e0b8980fc6b0b1292eebb24181c1a9753b33bc0f5.mo.png)|
|:---:|
| 初學者數據科學：學習路線圖 - _手繪筆記由 [@nitya](https://twitter.com/nitya) 提供_ |

| 課程編號 | 主題 | 課程分組 | 學習目標 | 課程連結 | 作者 |
| :-----------: | :----------------------------------------: | :--------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------: | :----: |
| 01 | 定義數據科學 | [簡介](1-Introduction/README.md) | 學習數據科學的基本概念，以及它與人工智慧、機器學習和大數據的關係。 | [課程](1-Introduction/01-defining-data-science/README.md) [影片](https://youtu.be/beZ7Mb_oz9I) | [Dmitry](http://soshnikov.com) |
| 02 | 數據科學倫理 | [簡介](1-Introduction/README.md) | 數據倫理的概念、挑戰與框架。 | [課程](1-Introduction/02-ethics/README.md) | [Nitya](https://twitter.com/nitya) |
| 03 | 定義數據 | [簡介](1-Introduction/README.md) | 數據的分類及其常見來源。 | [課程](1-Introduction/03-defining-data/README.md) | [Jasmine](https://www.twitter.com/paladique) |
| 04 | 統計與機率入門 | [簡介](1-Introduction/README.md) | 使用機率與統計的數學技術來理解數據。 | [課程](1-Introduction/04-stats-and-probability/README.md) [影片](https://youtu.be/Z5Zy85g4Yjw) | [Dmitry](http://soshnikov.com) |
| 05 | 使用關聯數據 | [數據操作](2-Working-With-Data/README.md) | 關聯數據的介紹，以及使用結構化查詢語言（SQL，發音為 "see-quell"）探索和分析關聯數據的基礎知識。 | [課程](2-Working-With-Data/05-relational-databases/README.md) | [Christopher](https://www.twitter.com/geektrainer) | | |
| 06 | 使用 NoSQL 數據 | [數據操作](2-Working-With-Data/README.md) | 非關聯數據的介紹、其各種類型，以及探索和分析文件型數據庫的基礎知識。 | [課程](2-Working-With-Data/06-non-relational/README.md) | [Jasmine](https://twitter.com/paladique)|
| 07 | 使用 Python | [數據操作](2-Working-With-Data/README.md) | 使用 Python 進行數據探索的基礎知識，包括 Pandas 等庫。建議具備 Python 程式設計的基礎知識。 | [課程](2-Working-With-Data/07-python/README.md) [影片](https://youtu.be/dZjWOGbsN4Y) | [Dmitry](http://soshnikov.com) |
| 08 | 數據準備 | [數據操作](2-Working-With-Data/README.md) | 數據清理與轉換技術，應對缺失、不準確或不完整數據的挑戰。 | [課程](2-Working-With-Data/08-data-preparation/README.md) | [Jasmine](https://www.twitter.com/paladique) |
| 09 | 數量可視化 | [數據可視化](3-Data-Visualization/README.md) | 學習如何使用 Matplotlib 可視化鳥類數據 🦆 | [課程](3-Data-Visualization/09-visualization-quantities/README.md) | [Jen](https://twitter.com/jenlooper) |
| 10 | 數據分佈可視化 | [數據可視化](3-Data-Visualization/README.md) | 可視化區間內的觀察值與趨勢。 | [課程](3-Data-Visualization/10-visualization-distributions/README.md) | [Jen](https://twitter.com/jenlooper) |
| 11 | 比例可視化 | [數據可視化](3-Data-Visualization/README.md) | 可視化離散和分組百分比。 | [課程](3-Data-Visualization/11-visualization-proportions/README.md) | [Jen](https://twitter.com/jenlooper) |
| 12 | 關係可視化 | [數據可視化](3-Data-Visualization/README.md) | 可視化數據集及其變量之間的連結與相關性。 | [課程](3-Data-Visualization/12-visualization-relationships/README.md) | [Jen](https://twitter.com/jenlooper) |
| 13 | 有意義的可視化 | [數據可視化](3-Data-Visualization/README.md) | 提供有效解決問題與洞察的可視化技術與指導。 | [課程](3-Data-Visualization/13-meaningful-visualizations/README.md) | [Jen](https://twitter.com/jenlooper) |
| 14 | 數據科學生命周期簡介 | [生命周期](4-Data-Science-Lifecycle/README.md) | 數據科學生命周期的介紹及其第一步：數據的獲取與提取。 | [課程](4-Data-Science-Lifecycle/14-Introduction/README.md) | [Jasmine](https://twitter.com/paladique) |
| 15 | 數據分析 | [生命周期](4-Data-Science-Lifecycle/README.md) | 數據科學生命周期中專注於數據分析的技術。 | [課程](4-Data-Science-Lifecycle/15-analyzing/README.md) | [Jasmine](https://twitter.com/paladique) | | |
| 16 | 溝通 | [生命周期](4-Data-Science-Lifecycle/README.md) | 數據科學生命周期中專注於以易於決策者理解的方式呈現數據洞察。 | [課程](4-Data-Science-Lifecycle/16-communication/README.md) | [Jalen](https://twitter.com/JalenMcG) | | |
| 17 | 雲端數據科學 | [雲端數據](5-Data-Science-In-Cloud/README.md) | 本系列課程介紹雲端數據科學及其優勢。 | [課程](5-Data-Science-In-Cloud/17-Introduction/README.md) | [Tiffany](https://twitter.com/TiffanySouterre) 和 [Maud](https://twitter.com/maudstweets) |
| 18 | 雲端數據科學 | [雲端數據](5-Data-Science-In-Cloud/README.md) | 使用低代碼工具訓練模型。 |[課程](5-Data-Science-In-Cloud/18-Low-Code/README.md) | [Tiffany](https://twitter.com/TiffanySouterre) 和 [Maud](https://twitter.com/maudstweets) |
| 19 | 雲端數據科學 | [雲端數據](5-Data-Science-In-Cloud/README.md) | 使用 Azure Machine Learning Studio 部署模型。 | [課程](5-Data-Science-In-Cloud/19-Azure/README.md)| [Tiffany](https://twitter.com/TiffanySouterre) 和 [Maud](https://twitter.com/maudstweets) |
| 20 | 野外數據科學 | [實際應用](6-Data-Science-In-Wild/README.md) | 現實世界中的數據科學驅動專案。 | [課程](6-Data-Science-In-Wild/20-Real-World-Examples/README.md) | [Nitya](https://twitter.com/nitya) |

## GitHub Codespaces

按照以下步驟在 Codespace 中開啟此範例：
1. 點擊 Code 下拉選單，選擇 Open with Codespaces 選項。
2. 在面板底部選擇 + New codespace。
更多資訊，請參考 [GitHub 文件](https://docs.github.com/en/codespaces/developing-in-codespaces/creating-a-codespace-for-a-repository#creating-a-codespace)。

## VSCode Remote - Containers

按照以下步驟，使用本地機器和 VSCode 的 Remote - Containers 擴展在容器中開啟此倉庫：

1. 如果是第一次使用開發容器，請確保系統符合前置需求（例如安裝 Docker），詳見[入門文檔](https://code.visualstudio.com/docs/devcontainers/containers#_getting-started)。

要使用此倉庫，可以選擇在隔離的 Docker 卷中開啟倉庫：

**注意**：此操作將使用 Remote-Containers 的 **Clone Repository in Container Volume...** 命令，將原始碼克隆到 Docker 卷中，而非本地文件系統。[卷](https://docs.docker.com/storage/volumes/) 是持久化容器數據的首選機制。

或者，開啟本地克隆或下載的倉庫版本：

- 將此倉庫克隆到本地文件系統。
- 按 F1，選擇 **Remote-Containers: Open Folder in Container...** 命令。
- 選擇此資料夾的克隆副本，等待容器啟動，然後開始嘗試。

## 離線訪問

您可以使用 [Docsify](https://docsify.js.org/#/) 離線運行此文檔。Fork 此倉庫，在本地機器上[安裝 Docsify](https://docsify.js.org/#/quickstart)，然後在此倉庫的根目錄中輸入 `docsify serve`。網站將在本地端的 3000 埠上提供服務：`localhost:3000`。

> 注意，筆記本文件無法通過 Docsify 渲染，因此需要運行筆記本時，請在 VS Code 中使用 Python 核心單獨運行。

## 其他課程

我們的團隊還製作了其他課程！請查看：

- [生成式 AI 初學者課程](https://aka.ms/genai-beginners)
- [生成式 AI 初學者課程 .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [使用 JavaScript 的生成式 AI](https://github.com/microsoft/generative-ai-with-javascript)
- [使用 Java 的生成式 AI](https://aka.ms/genaijava)
- [AI 初學者課程](https://aka.ms/ai-beginners)
- [數據科學初學者課程](https://aka.ms/datascience-beginners)
- [Bash 初學者課程](https://github.com/microsoft/bash-for-beginners)
- [機器學習初學者課程](https://aka.ms/ml-beginners)
- [網絡安全初學者課程](https://github.com/microsoft/Security-101) 
- [Web 開發初學者課程](https://aka.ms/webdev-beginners)
- [物聯網初學者課程](https://aka.ms/iot-beginners)
- [機器學習初學者課程](https://aka.ms/ml-beginners)
- [XR 開發初學者課程](https://aka.ms/xr-dev-for-beginners)
- [精通 GitHub Copilot 的 AI 配對編程](https://aka.ms/GitHubCopilotAI)
- [XR 開發初學者課程](https://github.com/microsoft/xr-development-for-beginners)
- [精通 GitHub Copilot 的 C#/.NET 開發者課程](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers)
- [選擇你的 Copilot 冒險](https://github.com/microsoft/CopilotAdventures)

---

**免責聲明**：  
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原始語言的文件作為權威來源。對於關鍵資訊，建議尋求專業人工翻譯。我們對於因使用此翻譯而產生的任何誤解或錯誤解讀概不負責。