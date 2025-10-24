<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "25b37acdfb2452917c1aa2e2ca44317a",
  "translation_date": "2025-10-24T09:53:17+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/assignment.md",
  "language_code": "hk"
}
-->
# 顯示機場數據

你已獲得一個基於 [SQLite](https://sqlite.org/index.html) 的 [數據庫](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db)，其中包含有關機場的信息。以下是其架構。你將使用 [SQLite 擴展](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) 在 [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) 中顯示不同城市的機場信息。

## 指引

要開始這項任務，你需要完成幾個步驟。你需要安裝一些工具並下載示例數據庫。

### 設置你的系統

你可以使用 Visual Studio Code 和 SQLite 擴展來與數據庫交互。

1. 前往 [code.visualstudio.com](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum)，按照指示安裝 Visual Studio Code
1. 按照 Marketplace 頁面的指示安裝 [SQLite 擴展](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum)

### 下載並打開數據庫

接下來，你需要下載並打開數據庫。

1. 從 [GitHub 下載數據庫文件](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db)，並將其保存到一個目錄中
1. 打開 Visual Studio Code
1. 在 SQLite 擴展中打開數據庫，按 **Ctl-Shift-P**（或在 Mac 上按 **Cmd-Shift-P**），然後輸入 `SQLite: Open database`
1. 選擇 **Choose database from file**，並打開之前下載的 **airports.db** 文件
1. 打開數據庫後（屏幕上不會有更新），通過按 **Ctl-Shift-P**（或在 Mac 上按 **Cmd-Shift-P**），輸入 `SQLite: New query` 創建一個新的查詢窗口

打開後，可以使用新的查詢窗口對數據庫運行 SQL 語句。你可以使用命令 **Ctl-Shift-Q**（或在 Mac 上按 **Cmd-Shift-Q**）對數據庫運行查詢。

> [!NOTE] 
> 有關 SQLite 擴展的更多信息，你可以參考 [文檔](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum)

## 數據庫架構

數據庫的架構是其表的設計和結構。**airports** 數據庫有兩個表，`cities` 包含英國和愛爾蘭的城市列表，`airports` 包含所有機場的列表。由於某些城市可能有多個機場，因此創建了兩個表來存儲信息。在此練習中，你將使用連接來顯示不同城市的信息。

| Cities           |
| ---------------- |
| id (PK, integer) |
| city (text)      |
| country (text)   |

| Airports                         |
| -------------------------------- |
| id (PK, integer)                 |
| name (text)                      |
| code (text)                      |
| city_id (FK to id in **Cities**) |

## 任務

創建查詢以返回以下信息：

1. `Cities` 表中的所有城市名稱
1. `Cities` 表中所有位於愛爾蘭的城市
1. 所有機場名稱及其所在城市和國家
1. 所有位於英國倫敦的機場

## 評分標準

| 優秀       | 合格       | 需要改進       |
| --------- | --------- | ------------- |

---

**免責聲明**：  
此文件已使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要信息，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤釋不承擔責任。