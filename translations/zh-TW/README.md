# 初學者的資料科學課程大綱

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?hide_repo_select=true&ref=main&repo=344191198)

[![GitHub license](https://img.shields.io/github/license/microsoft/Data-Science-For-Beginners.svg)](https://github.com/microsoft/Data-Science-For-Beginners/blob/master/LICENSE)
[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/Data-Science-For-Beginners.svg)](https://GitHub.com/microsoft/Data-Science-For-Beginners/graphs/contributors/)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/Data-Science-For-Beginners.svg)](https://GitHub.com/microsoft/Data-Science-For-Beginners/issues/)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/Data-Science-For-Beginners.svg)](https://GitHub.com/microsoft/Data-Science-For-Beginners/pulls/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/Data-Science-For-Beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/Data-Science-For-Beginners/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/Data-Science-For-Beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/Data-Science-For-Beginners/network/)
[![GitHub stars](https://img.shields.io/github/stars/microsoft/Data-Science-For-Beginners.svg?style=social&label=Star)](https://GitHub.com/microsoft/Data-Science-For-Beginners/stargazers/)


[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

微軟 Azure 雲端推廣者很高興提供一個為期 10 週、共 20 節課的資料科學課程。每個課程包含課前與課後測驗、完成授課內容的書面指導、解答以及作業。我們以專案為導向的教學法讓你在實作中學習，這是讓新技能穩固成形的有效方式。

**衷心感謝我們的作者：** [Jasmine Greenaway](https://www.twitter.com/paladique)、[Dmitry Soshnikov](http://soshnikov.com)、[Nitya Narasimhan](https://twitter.com/nitya)、[Jalen McGee](https://twitter.com/JalenMcG)、[Jen Looper](https://twitter.com/jenlooper)、[Maud Levy](https://twitter.com/maudstweets)、[Tiffany Souterre](https://twitter.com/TiffanySouterre)、[Christopher Harrison](https://www.twitter.com/geektrainer)。

**🙏 特別感謝 🙏 我們的 [Microsoft 學生大使](https://studentambassadors.microsoft.com/) 作者、審閱者與內容貢獻者，** 特別是 Aaryan Arora、[Aditya Garg](https://github.com/AdityaGarg00)、[Alondra Sanchez](https://www.linkedin.com/in/alondra-sanchez-molina/)、[Ankita Singh](https://www.linkedin.com/in/ankitasingh007)、[Anupam Mishra](https://www.linkedin.com/in/anupam--mishra/)、[Arpita Das](https://www.linkedin.com/in/arpitadas01/)、ChhailBihari Dubey、[Dibri Nsofor](https://www.linkedin.com/in/dibrinsofor)、[Dishita Bhasin](https://www.linkedin.com/in/dishita-bhasin-7065281bb)、[Majd Safi](https://www.linkedin.com/in/majd-s/)、[Max Blum](https://www.linkedin.com/in/max-blum-6036a1186/)、[Miguel Correa](https://www.linkedin.com/in/miguelmque/)、[Mohamma Iftekher (Iftu) Ebne Jalal](https://twitter.com/iftu119)、[Nawrin Tabassum](https://www.linkedin.com/in/nawrin-tabassum)、[Raymond Wangsa Putra](https://www.linkedin.com/in/raymond-wp/)、[Rohit Yadav](https://www.linkedin.com/in/rty2423)、Samridhi Sharma、[Sanya Sinha](https://www.linkedin.com/mwlite/in/sanya-sinha-13aab1200)、
[Sheena Narula](https://www.linkedin.com/in/sheena-narua-n/)、[Tauqeer Ahmad](https://www.linkedin.com/in/tauqeerahmad5201/)、Yogendrasingh Pawar 、[Vidushi Gupta](https://www.linkedin.com/in/vidushi-gupta07/)、[Jasleen Sondhi](https://www.linkedin.com/in/jasleen-sondhi/)

|![Sketchnote by @sketchthedocs https://sketchthedocs.dev](../../translated_images/zh-TW/00-Title.8af36cd35da1ac55.webp)|
|:---:|
| 初學者資料科學 — _速寫筆記由 [@nitya](https://twitter.com/nitya) 製作_ |

### 🌐 多語言支援

#### 透過 GitHub Action 支援（自動且持續更新）

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](./README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **偏好本地複製？**
>
> 本存放庫包含超過 50 種語言翻譯，會大幅增加下載大小。如欲不含翻譯內容之複製，請使用稀疏結帳：
>
> **Bash / macOS / Linux:**
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/Data-Science-For-Beginners.git
> cd Data-Science-For-Beginners
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
>
> **CMD (Windows):**
> ```cmd
> git clone --filter=blob:none --sparse https://github.com/microsoft/Data-Science-For-Beginners.git
> cd Data-Science-For-Beginners
> git sparse-checkout set --no-cone "/*" "!translations" "!translated_images"
> ```
>
> 這樣能讓您快速下載完成課程所需內容。
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**若您希望支援更多翻譯語言，請參考[此處](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**

#### 加入我們的社群  
[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

我們正在舉辦 Discord AI 學習系列活動，了解更多並於 2025 年 9 月 18 日至 30 日加入我們：[Learn with AI Series](https://aka.ms/learnwithai/discord)。您將獲得使用 GitHub Copilot 進行資料科學的技巧與秘訣。

![Learn with AI series](../../translated_images/zh-TW/1.2b28cdc6205e26fe.webp)

# 你是學生嗎？

請從以下資源開始：

- [學生中心頁面](https://docs.microsoft.com/en-gb/learn/student-hub?WT.mc_id=academic-77958-bethanycheum) 這個頁面包含初學者資源、學生套件，甚至還有獲取免費認證憑證券的方式。這是您想要加入書籤並定期查看的頁面，我們會每月至少更新一次內容。
- [Microsoft Learn 學生大使](https://studentambassadors.microsoft.com?WT.mc_id=academic-77958-bethanycheum) 加入全球學生大使社群，這或許是您進入微軟的途徑。

# 開始入門

## 📚 文件說明

- **[安裝指南](INSTALLATION.md)** — 初學者的一步步安裝指導
- **[使用指南](USAGE.md)** — 範例與常用工作流程
- **[除錯指南](TROUBLESHOOTING.md)** — 常見問題與解決方法
- **[貢獻指南](CONTRIBUTING.md)** — 如何參與本專案貢獻
- **[教師專區](for-teachers.md)** — 教學指導與課堂資源

## 👨‍🎓 給學生
> <strong>完全初學者</strong>：剛接觸資料科學？請先試試我們的[入門友善範例](examples/README.md)！這些簡單且有詳盡註解的範例將幫助您理解基礎，再深入完整課程。
> **[學生專區](https://aka.ms/student-page)**：欲自行使用本課程，請 fork 整個存放庫並自我完成練習，從課前測驗開始。接著閱讀授課內容並完成其餘活動。建議試著根據學到的知識自行完成專案，而非直接複製解答程式碼；不過每個以專案為導向的課程中，/solutions 目錄裡仍提供程式碼可供參考。另一想法是組成讀書會與朋友一同學習。更多進階學習建議參考 [Microsoft Learn](https://docs.microsoft.com/en-us/users/jenlooper-2911/collections/qprpajyoy3x0g7?WT.mc_id=academic-77958-bethanycheum)。

**快速入門：**
1. 查看 [安裝指南](INSTALLATION.md) 以設置您的環境
2. 閱讀 [使用指南](USAGE.md) 了解如何使用課程內容
3. 從第 1 課開始，按順序完成
4. 加入我們的 [Discord 社群](https://aka.ms/ds4beginners/discord) 獲得支援

## 👩‍🏫 教師專區
> <strong>教師們</strong>：我們已經[包含了一些建議](for-teachers.md)來幫助您使用這套課程。非常歡迎您在[我們的討論區](https://github.com/microsoft/Data-Science-For-Beginners/discussions)提供您的反饋！

## 認識團隊

[![宣傳影片](../../ds-for-beginners.gif)](https://youtu.be/8mzavjQSMM4 "宣傳影片")

**動畫 GIF 製作者** [Mohit Jaisal](https://www.linkedin.com/in/mohitjaisal)

> 🎥 點擊上方圖片，觀看關於此專案與創建團隊的影片！

## 教學法

我們在設計這套課程時，選擇了兩個教學原則：確保課程以專案為基礎並且包含頻繁的測驗。透過這系列課程結束後，學生將學會資料科學的基本原理，包括倫理概念、資料準備、不同的資料處理方式、資料視覺化、資料分析、資料科學的實務案例等等。

此外，課前的低壓測驗設定學生學習某主題的意向，而課後的第二次測驗則有助於加強記憶。此課程設計靈活且有趣，學生可以全程修習或選擇部份學習。專案由淺入深，整個 10 週學期結束時會越來越複雜。

> 請參考我們的[行為準則](CODE_OF_CONDUCT.md)、[貢獻指南](CONTRIBUTING.md)與[翻譯指南](TRANSLATIONS.md)。誠摯歡迎您的建設性意見！

## 每堂課包含：

- 選修手繪筆記
- 選修補充影片
- 課前熱身測驗
- 書面課程內容
- 對於專案型課程，提供逐步建立專案的指引
- 知識檢核
- 挑戰任務
- 補充閱讀材料
- 作業
- [課後測驗](https://ff-quizzes.netlify.app/en/)

> <strong>關於測驗的說明</strong>：所有測驗皆集中在 Quiz-App 資料夾中，共包含 40 個，每個測驗有三個問題。這些測驗會從課程中鏈結取得，但您也可以在本地端執行測驗應用，或部署至 Azure，請遵循 `quiz-app` 資料夾中的指示。測驗也逐步進行在地化。

## 🎓 適合新手的範例

**剛接觸資料科學嗎？** 我們建立了一個特別的[範例目錄](examples/README.md)，提供簡單且註解詳盡的程式碼，幫助您開始學習：

- 🌟 **Hello World** - 您的第一個資料科學程式
- 📂 <strong>讀取資料</strong> - 學習如何讀取及探索資料集
- 📊 <strong>簡單分析</strong> - 計算統計數據並發現模式
- 📈 <strong>基礎視覺化</strong> - 建立圖表與折線圖
- 🔬 <strong>真實專案</strong> - 完整的工作流程範例

每個範例都包含詳細註解，解釋每一個步驟，非常適合初學者！

👉 **[從範例開始](examples/README.md)** 👈

## 課程列表


|![ 由 @sketchthedocs 製作的手繪筆記 https://sketchthedocs.dev](../../translated_images/zh-TW/00-Roadmap.4905d6567dff4753.webp)|
|:---:|
| 初學者資料科學：學習路線圖 - _手繪筆記作者 [@nitya](https://twitter.com/nitya)_ |


| 課程號碼 | 主題 | 課程組別 | 學習目標 | 關聯課程 | 作者 |
| :------: | :-----------------------------: | :----------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :----------------------------------------------------------: | :----: |
| 01 | 定義資料科學 | [介紹](1-Introduction/README.md) | 理解資料科學的基本概念，以及它與人工智慧、機器學習和大數據的關係。 | [課程](1-Introduction/01-defining-data-science/README.md) [影片](https://youtu.be/beZ7Mb_oz9I) | [Dmitry](http://soshnikov.com) |
| 02 | 資料科學倫理 | [介紹](1-Introduction/README.md) | 資料倫理的概念、挑戰與架構。 | [課程](1-Introduction/02-ethics/README.md) | [Nitya](https://twitter.com/nitya) |
| 03 | 定義資料 | [介紹](1-Introduction/README.md) | 資料的分類與常見來源。 | [課程](1-Introduction/03-defining-data/README.md) | [Jasmine](https://www.twitter.com/paladique) |
| 04 | 統計學與機率入門 | [介紹](1-Introduction/README.md) | 利用機率與統計的數學技術來了解資料。 | [課程](1-Introduction/04-stats-and-probability/README.md) [影片](https://youtu.be/Z5Zy85g4Yjw) | [Dmitry](http://soshnikov.com) |
| 05 | 操作關聯資料 | [資料操作](2-Working-With-Data/README.md) | 關聯資料介紹，與使用結構化查詢語言（SQL，讀作「see-quell」）探索和分析關聯資料基礎。 | [課程](2-Working-With-Data/05-relational-databases/README.md) | [Christopher](https://www.twitter.com/geektrainer) |
| 06 | 操作 NoSQL 資料 | [資料操作](2-Working-With-Data/README.md) | 非關聯資料介紹，及其多種型態與使用文件資料庫進行探索及分析基礎。 | [課程](2-Working-With-Data/06-non-relational/README.md) | [Jasmine](https://twitter.com/paladique) |
| 07 | 使用 Python | [資料操作](2-Working-With-Data/README.md) | 使用 Python 及 Pandas 等函式庫進行資料探索的基礎。建議有 Python 程式設計的基礎。 | [課程](2-Working-With-Data/07-python/README.md) [影片](https://youtu.be/dZjWOGbsN4Y) | [Dmitry](http://soshnikov.com) |
| 08 | 資料準備 | [資料操作](2-Working-With-Data/README.md) | 清理與轉換資料的技術，解決缺失、錯誤或不完整資料的挑戰。 | [課程](2-Working-With-Data/08-data-preparation/README.md) | [Jasmine](https://www.twitter.com/paladique) |
| 09 | 量的視覺化 | [資料視覺化](3-Data-Visualization/README.md) | 使用 Matplotlib 來視覺化鳥類資料 🦆 | [課程](3-Data-Visualization/09-visualization-quantities/README.md) | [Jen](https://twitter.com/jenlooper) |
| 10 | 資料分布的視覺化 | [資料視覺化](3-Data-Visualization/README.md) | 在區間內視覺化觀察值與趨勢。 | [課程](3-Data-Visualization/10-visualization-distributions/README.md) | [Jen](https://twitter.com/jenlooper) |
| 11 | 比例的視覺化 | [資料視覺化](3-Data-Visualization/README.md) | 視覺化離散和分組百分比。 | [課程](3-Data-Visualization/11-visualization-proportions/README.md) | [Jen](https://twitter.com/jenlooper) |
| 12 | 關係的視覺化 | [資料視覺化](3-Data-Visualization/README.md) | 視覺化資料集及其變數之間的連結和相關性。 | [課程](3-Data-Visualization/12-visualization-relationships/README.md) | [Jen](https://twitter.com/jenlooper) |
| 13 | 有意義的視覺化 | [資料視覺化](3-Data-Visualization/README.md) | 製作有效解決問題和洞察的視覺化技巧和指導。 | [課程](3-Data-Visualization/13-meaningful-visualizations/README.md) | [Jen](https://twitter.com/jenlooper) |
| 14 | 資料科學生命週期介紹 | [生命週期](4-Data-Science-Lifecycle/README.md) | 介紹資料科學生命週期及其第一步驟——取得與萃取資料。 | [課程](4-Data-Science-Lifecycle/14-Introduction/README.md) | [Jasmine](https://twitter.com/paladique) |
| 15 | 分析 | [生命週期](4-Data-Science-Lifecycle/README.md) | 著重於資料科學生命週期中分析資料的技巧。 | [課程](4-Data-Science-Lifecycle/15-analyzing/README.md) | [Jasmine](https://twitter.com/paladique) |
| 16 | 溝通 | [生命週期](4-Data-Science-Lifecycle/README.md) | 著重於用讓決策者更容易理解的方式呈現資料洞察。 | [課程](4-Data-Science-Lifecycle/16-communication/README.md) | [Jalen](https://twitter.com/JalenMcG) |
| 17 | 雲端資料科學 | [雲端資料](5-Data-Science-In-Cloud/README.md) | 介紹雲端資料科學及其好處的一系列課程。 | [課程](5-Data-Science-In-Cloud/17-Introduction/README.md) | [Tiffany](https://twitter.com/TiffanySouterre) 與 [Maud](https://twitter.com/maudstweets) |
| 18 | 雲端資料科學 | [雲端資料](5-Data-Science-In-Cloud/README.md) | 使用低程式碼工具訓練模型。 | [課程](5-Data-Science-In-Cloud/18-Low-Code/README.md) | [Tiffany](https://twitter.com/TiffanySouterre) 與 [Maud](https://twitter.com/maudstweets) |
| 19 | 雲端資料科學 | [雲端資料](5-Data-Science-In-Cloud/README.md) | 使用 Azure Machine Learning Studio 部署模型。 | [課程](5-Data-Science-In-Cloud/19-Azure/README.md) | [Tiffany](https://twitter.com/TiffanySouterre) 與 [Maud](https://twitter.com/maudstweets) |
| 20 | 資料科學實務 | [實務應用](6-Data-Science-In-Wild/README.md) | 真實世界中資料科學驅動的專案。 | [課程](6-Data-Science-In-Wild/20-Real-World-Examples/README.md) | [Nitya](https://twitter.com/nitya) |

## GitHub Codespaces

請依下列步驟在 Codespace 中打開此範例：
1. 點選 Code 下拉選單，選擇 Open with Codespaces 選項。
2. 在窗格底部選擇 + New codespace。
更多資訊請參考[GitHub 文件](https://docs.github.com/en/codespaces/developing-in-codespaces/creating-a-codespace-for-a-repository#creating-a-codespace)。

## VSCode Remote - Containers
請依下列步驟使用本機和 VSCode 與 VS Code Remote - Containers 擴充功能，於容器中開啟本儲存庫：

1. 若您是第一次使用開發容器，請確認您系統符合先決條件（例如已安裝 Docker），可參考[快速入門文件](https://code.visualstudio.com/docs/devcontainers/containers#_getting-started)。

使用此儲存庫，可以透過隔離的 Docker 容器卷打開儲存庫：

<strong>注意</strong>：底層會使用 Remote-Containers: **Clone Repository in Container Volume...** 指令，將原始碼克隆到 Docker 容器卷中，而非本機檔案系統。[Volumes](https://docs.docker.com/storage/volumes/) 是持久化容器資料的推薦方法。

或打開本機已克隆或下載的儲存庫版本：

- 將此儲存庫克隆至本機檔案系統。
- 按下 F1、選擇 **Remote-Containers: Open Folder in Container...** 指令。
- 選擇克隆的資料夾，等待容器啟動，即可開始使用。

## 離線存取

您可以透過使用 [Docsify](https://docsify.js.org/#/) 離線瀏覽本文件。請分叉此儲存庫，於本機安裝 [Docsify](https://docsify.js.org/#/quickstart)，然後在此儲存庫根目錄執行 `docsify serve`。網站會在本地端 3000 埠口提供服務：`localhost:3000`。

> 注意，Notebook 內容無法透過 Docsify 渲染，需另行在 VS Code 裡使用 Python 核心執行。

## 其他課程

我們團隊也推出其他課程！請參考：

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j 入門](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js for Beginners](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain for Beginners](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / Agents
[![AZD for Beginners](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI for Beginners](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP for Beginners](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agents for Beginners](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### 生成式 AI 系列
[![Generative AI for Beginners](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generative AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### 核心學習
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science for Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI for Beginners](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cybersecurity for Beginners](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web Dev for Beginners](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT for Beginners](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR Development for Beginners](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot 系列
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## 獲取幫助

**遇到問題？** 請查看我們的[疑難排解指南](TROUBLESHOOTING.md)以尋找常見問題的解決方法。

如果您卡住了或者對建立 AI 應用程式有任何疑問，歡迎加入學習者及資深開發者的討論社群。這是一個支持彼此的社區，歡迎提問並自由分享知識。

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

如果您在產品使用過程中有任何反饋或錯誤，請訪問：

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯所產生的任何誤解或誤譯負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->