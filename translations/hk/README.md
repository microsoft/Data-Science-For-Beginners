<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "33d252f7491b696d85df7f680e7e7b90",
  "translation_date": "2026-01-16T10:12:43+00:00",
  "source_file": "README.md",
  "language_code": "hk"
}
-->
# 初學者數據科學課程大綱

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

微軟 Azure Cloud Advocates 很高興能提供一個長達 10 週、包含 20 課的完整數據科學課程。每個課程包含課前和課後的小測驗、完成課程的書面指示、解答方案及作業。我們的專案導向教學法讓你在實作中學習，是一種證明能讓新技能更易吸收的學習方式。

**衷心感謝我們的作者：** [Jasmine Greenaway](https://www.twitter.com/paladique)、[Dmitry Soshnikov](http://soshnikov.com)、[Nitya Narasimhan](https://twitter.com/nitya)、[Jalen McGee](https://twitter.com/JalenMcG)、[Jen Looper](https://twitter.com/jenlooper)、[Maud Levy](https://twitter.com/maudstweets)、[Tiffany Souterre](https://twitter.com/TiffanySouterre)、[Christopher Harrison](https://www.twitter.com/geektrainer)。

**🙏 特別感謝 🙏 我們的 [Microsoft 學生大使](https://studentambassadors.microsoft.com/) 作者、審查者及內容貢獻者，** 包括 Aaryan Arora、[Aditya Garg](https://github.com/AdityaGarg00)、[Alondra Sanchez](https://www.linkedin.com/in/alondra-sanchez-molina/)、[Ankita Singh](https://www.linkedin.com/in/ankitasingh007)、[Anupam Mishra](https://www.linkedin.com/in/anupam--mishra/)、[Arpita Das](https://www.linkedin.com/in/arpitadas01/)、ChhailBihari Dubey、[Dibri Nsofor](https://www.linkedin.com/in/dibrinsofor)、[Dishita Bhasin](https://www.linkedin.com/in/dishita-bhasin-7065281bb)、[Majd Safi](https://www.linkedin.com/in/majd-s/)、[Max Blum](https://www.linkedin.com/in/max-blum-6036a1186/)、[Miguel Correa](https://www.linkedin.com/in/miguelmque/)、[Mohamma Iftekher (Iftu) Ebne Jalal](https://twitter.com/iftu119)、[Nawrin Tabassum](https://www.linkedin.com/in/nawrin-tabassum)、[Raymond Wangsa Putra](https://www.linkedin.com/in/raymond-wp/)、[Rohit Yadav](https://www.linkedin.com/in/rty2423)、Samridhi Sharma、[Sanya Sinha](https://www.linkedin.com/mwlite/in/sanya-sinha-13aab1200)、[Sheena Narula](https://www.linkedin.com/in/sheena-narua-n/)、[Tauqeer Ahmad](https://www.linkedin.com/in/tauqeerahmad5201/)、Yogendrasingh Pawar、[Vidushi Gupta](https://www.linkedin.com/in/vidushi-gupta07/)、[Jasleen Sondhi](https://www.linkedin.com/in/jasleen-sondhi/)

|![Sketchnote by @sketchthedocs https://sketchthedocs.dev](../../../../translated_images/hk/00-Title.8af36cd35da1ac55.webp)|
|:---:|
| 初學者數據科學 - _筆記速寫由 [@nitya](https://twitter.com/nitya) 製作_ |

### 🌐 多語言支援

#### 透過 GitHub Action 支援（自動且保持最新）

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[阿拉伯文](../ar/README.md) | [孟加拉文](../bn/README.md) | [保加利亞文](../bg/README.md) | [緬甸語](../my/README.md) | [中文 (簡體)](../zh/README.md) | [中文 (繁體, 香港)](./README.md) | [中文 (繁體, 澳門)](../mo/README.md) | [中文 (繁體, 台灣)](../tw/README.md) | [克羅地亞文](../hr/README.md) | [捷克文](../cs/README.md) | [丹麥文](../da/README.md) | [荷蘭文](../nl/README.md) | [愛沙尼亞文](../et/README.md) | [芬蘭文](../fi/README.md) | [法文](../fr/README.md) | [德文](../de/README.md) | [希臘文](../el/README.md) | [希伯來文](../he/README.md) | [印地文](../hi/README.md) | [匈牙利文](../hu/README.md) | [印尼文](../id/README.md) | [義大利文](../it/README.md) | [日文](../ja/README.md) | [卡納達語](../kn/README.md) | [韓文](../ko/README.md) | [立陶宛文](../lt/README.md) | [馬來文](../ms/README.md) | [馬拉雅拉姆語](../ml/README.md) | [馬拉地語](../mr/README.md) | [尼泊爾語](../ne/README.md) | [尼日利亞皮欽語](../pcm/README.md) | [挪威文](../no/README.md) | [波斯文 (法爾西語)](../fa/README.md) | [波蘭文](../pl/README.md) | [葡萄牙文 (巴西)](../br/README.md) | [葡萄牙文 (葡萄牙)](../pt/README.md) | [旁遮普文 (古魯穆奇)](../pa/README.md) | [羅馬尼亞文](../ro/README.md) | [俄文](../ru/README.md) | [塞爾維亞文 (西里爾字母)](../sr/README.md) | [斯洛伐克文](../sk/README.md) | [斯洛維尼亞文](../sl/README.md) | [西班牙文](../es/README.md) | [斯瓦希里語](../sw/README.md) | [瑞典文](../sv/README.md) | [他加祿語 (菲律賓語)](../tl/README.md) | [泰米爾語](../ta/README.md) | [泰盧固語](../te/README.md) | [泰文](../th/README.md) | [土耳其文](../tr/README.md) | [烏克蘭文](../uk/README.md) | [烏爾都語](../ur/README.md) | [越南文](../vi/README.md)

> **偏好本地克隆？**

> 本倉庫包含超過 50 種語言的翻譯，這會大幅增加下載大小。若想不包含翻譯檔案克隆，請使用 sparse checkout：
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/Data-Science-For-Beginners.git
> cd Data-Science-For-Beginners
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> 如此，你將擁有完成課程所需的一切，且下載速度更快。
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**如果你希望我們支援更多翻譯語言，請參閱 [這裡](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**

#### 加入我們的社群  
[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

我們正在 Discord 舉辦 Learn with AI 系列活動，詳情及加入請見 [Learn with AI 系列](https://aka.ms/learnwithai/discord)。活動期間為 2025 年 9 月 18 日至 30 日。你將學到如何使用 GitHub Copilot 進行數據科學的技巧。

![Learn with AI series](../../../../translated_images/hk/1.2b28cdc6205e26fe.webp)

# 你是學生嗎？

開始使用以下資源：

- [學生中心頁面](https://docs.microsoft.com/en-gb/learn/student-hub?WT.mc_id=academic-77958-bethanycheum) 此頁面包含初學者資源、學生套裝，甚至取得免費認證憑證的方法。這是一個你應該加到書籤並不時瀏覽的頁面，因為我們至少每月會更新內容。
- [Microsoft Learn 學生大使](https://studentambassadors.microsoft.com?WT.mc_id=academic-77958-bethanycheum) 加入全球學生大使社群，這或許是你踏入微軟的途徑。

# 快速入門

## 📚 文件資料

- **[安裝指南](INSTALLATION.md)** — 適合初學者的逐步安裝說明
- **[使用指南](USAGE.md)** — 範例與常見工作流程
- **[疑難排解](TROUBLESHOOTING.md)** — 常見問題解決方案
- **[貢獻指南](CONTRIBUTING.md)** — 如何為此專案做出貢獻
- **[給老師的資源](for-teachers.md)** — 教學指導與教室資源

## 👨‍🎓 學生專區
> **完全初學者**：不熟悉數據科學？可從我們的[初學者友善範例](examples/README.md)開始！這些簡單且有充分註解的範例幫助你理解基礎，然後再投入完整課程。
> **[學生](https://aka.ms/student-page)**：若想自己使用此課程，請 fork 全部資源，自行完成練習，先從課前測驗開始，再閱讀課程並完成剩餘活動。嘗試透過理解課程內容自行建立專案，而非直接複製解答代碼；不過這些解答代碼在每個專案導向課程的 /solutions 資料夾中可查閱。另一個方法是與朋友組成讀書會，共同學習。進階學習我們推薦 [Microsoft Learn](https://docs.microsoft.com/en-us/users/jenlooper-2911/collections/qprpajyoy3x0g7?WT.mc_id=academic-77958-bethanycheum)。

**快速開始：**
1. 查閱[安裝指南](INSTALLATION.md)，設置你的環境
2. 參考[使用指南](USAGE.md)，瞭解課程操作方式
3. 從第一課開始，依序完成
4. 加入我們的[Discord 社群](https://aka.ms/ds4beginners/discord)尋求支援

## 👩‍🏫 老師專區

> **老師們**：我們提供了[使用建議](for-teachers.md)參考。期待你在[討論論壇](https://github.com/microsoft/Data-Science-For-Beginners/discussions)分享回饋！

## 認識團隊
[![Promo video](../../ds-for-beginners.gif)](https://youtu.be/8mzavjQSMM4 "Promo video")

**動圖作者** [Mohit Jaisal](https://www.linkedin.com/in/mohitjaisal)

> 🎥 點擊上方圖片觀看關於此專案及創作者的影片！

## 教學法

我們在建立此課程時選擇了兩個教學原則：確保課程以專案為基礎並包含頻繁的測驗。完成此系列後，學生將學習到資料科學的基本原理，包括倫理概念、資料準備、不同的資料處理方式、資料視覺化、資料分析、資料科學的實際應用案例等。

此外，課前的低壓力測驗能設定學生學習主題的意向，課後的第二次測驗則確保學習的鞏固。此課程設計靈活且有趣，可以完整或部分學習。專案從簡單開始，並在十週週期結束時變得越來越複雜。

> 查看我們的 [行為守則](CODE_OF_CONDUCT.md)、[貢獻指南](CONTRIBUTING.md)、[翻譯指南](TRANSLATIONS.md)。歡迎您提供建設性回饋！

## 每堂課包括：

- 非必需的草圖筆記
- 非必需的補充影片
- 課前熱身測驗
- 書面課程內容
- 專案課程附帶專案建立的逐步指南
- 知識檢查
- 挑戰任務
- 補充閱讀資料
- 作業
- [課後測驗](https://ff-quizzes.netlify.app/en/)

> **關於測驗的說明**：全部測驗都包含在 Quiz-App 資料夾中，共有 40 個測驗，每個測驗三個問題。測驗在課程內有連結，但該測驗應用程式可在本地執行或部署到 Azure；請依照 `quiz-app` 資料夾內的說明操作。測驗正在逐步在地化。

## 🎓 初學者友善範例

**資料科學新手？** 我們創建了特別的[範例目錄](examples/README.md)，提供簡單、註解詳盡的程式碼，助你入門：

- 🌟 **Hello World** - 你的第一個資料科學程式
- 📂 **載入資料** - 學習讀取與探索資料集
- 📊 **簡單分析** - 計算統計數據並找出模式
- 📈 **基礎視覺化** - 製作圖表和曲線圖
- 🔬 **真實專案** - 從頭到尾完成工作流程

每個範例都包含詳細註解，解釋每一步，適合完全沒有經驗的初學者！

👉 **[從範例開始](examples/README.md)** 👈

## 課程列表


|![ Sketchnote by @sketchthedocs https://sketchthedocs.dev](../../../../translated_images/hk/00-Roadmap.4905d6567dff4753.webp)|
|:---:|
| 資料科學初學者路線圖 - _草圖筆記由 [@nitya](https://twitter.com/nitya) 製作_ |


| 課程編號 | 主題 | 課程分組 | 學習目標 | 連結課程 | 作者 |
| :-----------: | :----------------------------------------: | :--------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------: | :----: |
| 01 | 定義資料科學 | [介紹](1-Introduction/README.md) | 了解資料科學背後的基本概念，以及它如何與人工智慧、機器學習和大數據相關。 | [課程](1-Introduction/01-defining-data-science/README.md) [影片](https://youtu.be/beZ7Mb_oz9I) | [Dmitry](http://soshnikov.com) |
| 02 | 資料科學倫理 | [介紹](1-Introduction/README.md) | 資料倫理概念、挑戰與框架。 | [課程](1-Introduction/02-ethics/README.md) | [Nitya](https://twitter.com/nitya) |
| 03 | 定義資料 | [介紹](1-Introduction/README.md) | 資料如何分類及其常見來源。 | [課程](1-Introduction/03-defining-data/README.md) | [Jasmine](https://www.twitter.com/paladique) |
| 04 | 統計與機率入門 | [介紹](1-Introduction/README.md) | 了解機率與統計的數學技術以理解資料。 | [課程](1-Introduction/04-stats-and-probability/README.md) [影片](https://youtu.be/Z5Zy85g4Yjw) | [Dmitry](http://soshnikov.com) |
| 05 | 處理關聯式資料 | [資料處理](2-Working-With-Data/README.md) | 介紹關聯式資料，並使用結構化查詢語言（SQL，發音為“see-quell”）探究與分析關聯式資料的基礎。 | [課程](2-Working-With-Data/05-relational-databases/README.md) | [Christopher](https://www.twitter.com/geektrainer) | | |
| 06 | 處理 NoSQL 資料 | [資料處理](2-Working-With-Data/README.md) | 介紹非關聯式資料及其不同種類，並介紹探索與分析文件型資料庫的基礎。 | [課程](2-Working-With-Data/06-non-relational/README.md) | [Jasmine](https://twitter.com/paladique)|
| 07 | 使用 Python | [資料處理](2-Working-With-Data/README.md) | 使用 Python 進行資料探索的基礎，涵蓋 Pandas 等程式庫。建議具備基礎的 Python 程式設計知識。 | [課程](2-Working-With-Data/07-python/README.md) [影片](https://youtu.be/dZjWOGbsN4Y) | [Dmitry](http://soshnikov.com) |
| 08 | 資料準備 | [資料處理](2-Working-With-Data/README.md) | 介紹清理與轉換資料的技術，應對缺失、不準確或不完整資料的挑戰。 | [課程](2-Working-With-Data/08-data-preparation/README.md) | [Jasmine](https://www.twitter.com/paladique) |
| 09 | 視覺化數量 | [資料視覺化](3-Data-Visualization/README.md) | 學習使用 Matplotlib 視覺化鳥類資料 🦆 | [課程](3-Data-Visualization/09-visualization-quantities/README.md) | [Jen](https://twitter.com/jenlooper) |
| 10 | 視覺化資料分佈 | [資料視覺化](3-Data-Visualization/README.md) | 視覺化觀察值及區間內趨勢。 | [課程](3-Data-Visualization/10-visualization-distributions/README.md) | [Jen](https://twitter.com/jenlooper) |
| 11 | 視覺化比例 | [資料視覺化](3-Data-Visualization/README.md) | 視覺化離散值與分組百分比。 | [課程](3-Data-Visualization/11-visualization-proportions/README.md) | [Jen](https://twitter.com/jenlooper) |
| 12 | 視覺化關係 | [資料視覺化](3-Data-Visualization/README.md) | 視覺化資料集合與其變數間的連結與相關關係。 | [課程](3-Data-Visualization/12-visualization-relationships/README.md) | [Jen](https://twitter.com/jenlooper) |
| 13 | 有意義的視覺化 | [資料視覺化](3-Data-Visualization/README.md) | 製作有效解決問題並獲得洞察的視覺化技巧與指導。 | [課程](3-Data-Visualization/13-meaningful-visualizations/README.md) | [Jen](https://twitter.com/jenlooper) |
| 14 | 資料科學生命週期入門 | [生命週期](4-Data-Science-Lifecycle/README.md) | 介紹資料科學生命週期及其第一步：取得與擷取資料。 | [課程](4-Data-Science-Lifecycle/14-Introduction/README.md) | [Jasmine](https://twitter.com/paladique) |
| 15 | 分析階段 | [生命週期](4-Data-Science-Lifecycle/README.md) | 資料科學生命週期中專注於資料分析的階段。 | [課程](4-Data-Science-Lifecycle/15-analyzing/README.md) | [Jasmine](https://twitter.com/paladique) | | |
| 16 | 溝通階段 | [生命週期](4-Data-Science-Lifecycle/README.md) | 專注於用易於決策者理解的方式呈現資料洞察的生命週期階段。 | [課程](4-Data-Science-Lifecycle/16-communication/README.md) | [Jalen](https://twitter.com/JalenMcG) | | |
| 17 | 雲端資料科學 | [雲端資料](5-Data-Science-In-Cloud/README.md) | 介紹雲端資料科學及其優勢的系列課程。 | [課程](5-Data-Science-In-Cloud/17-Introduction/README.md) | [Tiffany](https://twitter.com/TiffanySouterre) 和 [Maud](https://twitter.com/maudstweets) |
| 18 | 雲端資料科學 | [雲端資料](5-Data-Science-In-Cloud/README.md) | 使用低程式碼工具訓練模型。 |[課程](5-Data-Science-In-Cloud/18-Low-Code/README.md) | [Tiffany](https://twitter.com/TiffanySouterre) 和 [Maud](https://twitter.com/maudstweets) |
| 19 | 雲端資料科學 | [雲端資料](5-Data-Science-In-Cloud/README.md) | 使用 Azure Machine Learning Studio 部署模型。 | [課程](5-Data-Science-In-Cloud/19-Azure/README.md)| [Tiffany](https://twitter.com/TiffanySouterre) 和 [Maud](https://twitter.com/maudstweets) |
| 20 | 實務資料科學 | [實務](6-Data-Science-In-Wild/README.md) | 資料科學驅動的真實世界專案。 | [課程](6-Data-Science-In-Wild/20-Real-World-Examples/README.md) | [Nitya](https://twitter.com/nitya) |

## GitHub Codespaces

按照以下步驟在 Codespace 中開啟此範例：
1. 點擊 Code 下拉選單並選擇 Open with Codespaces 選項。
2. 在面板底部點選 + New codespace。
欲了解更多資訊，請參考 [GitHub 文件](https://docs.github.com/en/codespaces/developing-in-codespaces/creating-a-codespace-for-a-repository#creating-a-codespace)。

## VSCode Remote - Containers
按照以下步驟使用本地機器及 VSCode 的 VS Code Remote - Containers 擴充套件，在容器中開啟此專案庫：

1. 如果您是第一次使用開發容器，請先確保系統符合前置需求（例如安裝 Docker），詳見[入門文件](https://code.visualstudio.com/docs/devcontainers/containers#_getting-started)。

您可以選擇在獨立 Docker 卷中開啟此專案庫：

**注意**：這會使用 Remote-Containers 的 **Clone Repository in Container Volume...** 命令，將原始碼克隆到 Docker 卷中，而非本機檔案系統。[卷](https://docs.docker.com/storage/volumes/)是持久化容器資料的推薦機制。

或者開啟已本地克隆或下載的專案庫版本：

- 將此專案庫克隆到本機檔案系統。
- 按 F1 並選擇 **Remote-Containers: Open Folder in Container...** 命令。
- 選擇本機克隆的資料夾，等待容器啟動後開始使用。

## 離線存取

您可以使用 [Docsify](https://docsify.js.org/#/) 離線運行此文件。先 Fork 此倉庫，於本機安裝 [Docsify](https://docsify.js.org/#/quickstart)，接著在本專案根目錄輸入 `docsify serve`。網站將在本地主機的 3000 埠運行：`localhost:3000`。

> 注意，筆記本不會被 Docsify 呈現，若需要運行筆記本，請在 VS Code 以 Python 核心單獨運行。

## 其他課程

我們團隊還製作其他課程！請參考：

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j for Beginners](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js for Beginners](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

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

## 尋求協助

**遇到問題？** 請查看我們的[疑難解答指南](TROUBLESHOOTING.md)，了解常見問題的解決方法。

如果你卡住了或對構建 AI 應用有任何疑問，歡迎加入 MCP 的學習者與經驗豐富的開發者討論社群。這是一個支持性的社區，歡迎提出問題並自由分享知識。

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

如果你在構建過程中有產品反饋或錯誤，請造訪：

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工作翻譯。因使用本翻譯而產生的任何誤解或誤釋，本公司概不負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->