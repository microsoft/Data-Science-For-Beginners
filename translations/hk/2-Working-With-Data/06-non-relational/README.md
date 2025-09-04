<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "54c5a1c74aecb69d2f9099300a4b7eea",
  "translation_date": "2025-09-04T12:42:31+00:00",
  "source_file": "2-Working-With-Data/06-non-relational/README.md",
  "language_code": "hk"
}
-->
# 使用數據：非關聯式數據

|![由 [(@sketchthedocs)](https://sketchthedocs.dev) 繪製的速記筆記](../../sketchnotes/06-NoSQL.png)|
|:---:|
|使用 NoSQL 數據 - _速記筆記由 [@nitya](https://twitter.com/nitya) 繪製_ |

## [課前測驗](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/10)

數據並不限於關聯式數據庫。本課程聚焦於非關聯式數據，並涵蓋電子表格和 NoSQL 的基礎知識。

## 電子表格

電子表格是一種流行的數據存儲和探索方式，因為它需要較少的設置工作即可開始使用。在本課程中，您將學習電子表格的基本組成部分，以及公式和函數。示例將以 Microsoft Excel 為例，但大多數部分和主題在其他電子表格軟件中都有類似的名稱和步驟。

![一個空的 Microsoft Excel 工作簿，包含兩個工作表](../../../../translated_images/parts-of-spreadsheet.120711c82aa18a45c3e62a491a15bba0a31ab0e9db407ec022702fed8ffd89bf.hk.png)

電子表格是一個文件，可以在電腦、設備或基於雲的文件系統中訪問。軟件本身可能是基於瀏覽器的，也可能是必須安裝在電腦上的應用程序或下載的應用。 在 Excel 中，這些文件也被定義為 **工作簿**，本課程的其餘部分將使用這一術語。

工作簿包含一個或多個 **工作表**，每個工作表都由標籤標記。在工作表中有稱為 **儲存格** 的矩形，這些儲存格包含實際數據。儲存格是行和列的交叉點，其中列用字母標記，行用數字標記。一些電子表格會在前幾行中包含標題，以描述儲存格中的數據。

基於 Excel 工作簿的這些基本元素，我們將使用 [Microsoft 模板](https://templates.office.com/) 中的一個專注於庫存的示例來演示電子表格的其他部分。

### 管理庫存

名為 "InventoryExample" 的電子表格文件是一個格式化的庫存項目表，包含三個工作表，標籤分別為 "Inventory List"、"Inventory Pick List" 和 "Bin Lookup"。Inventory List 工作表的第 4 行是標題，描述了標題列中每個儲存格的值。

![Microsoft Excel 中庫存列表示例中的公式高亮顯示](../../../../translated_images/formula-excel.ad1068c220892f5ead570d12f2394897961d31a5043a1dd4e6fc5d7690c7a14e.hk.png)

有些情況下，儲存格的值依賴於其他儲存格的值來生成。在庫存列表電子表格中，我們跟蹤庫存中每個項目的成本，但如果我們需要知道整個庫存的價值呢？[**公式**](https://support.microsoft.com/en-us/office/overview-of-formulas-34519a4e-1e8d-4f4b-84d4-d642c4f63263) 用於對儲存格數據執行操作，在此示例中用於計算庫存的成本。此電子表格在 Inventory Value 列中使用公式，通過將 QTY 標題下的數量與 COST 標題下的成本相乘來計算每個項目的價值。雙擊或高亮顯示儲存格將顯示公式。您會注意到公式以等號開頭，後面是計算或操作。

![Microsoft Excel 中庫存列表示例中的函數高亮顯示](../../../../translated_images/function-excel.be2ae4feddc10ca089f3d4363040d93b7fd046c8d4f83ba975ec46483ee99895.hk.png)

我們可以使用另一個公式將所有 Inventory Value 的值相加以獲得其總價值。這可以通過逐個儲存格相加來計算總和，但這可能是一項繁瑣的任務。Excel 提供了 [**函數**](https://support.microsoft.com/en-us/office/sum-function-043e1c7d-7726-4e80-8f32-07b23e057f89)，即預定義的公式，用於對儲存格值進行計算。函數需要參數，即執行這些計算所需的值。當函數需要多個參數時，它們需要按特定順序列出，否則函數可能無法計算正確的值。此示例使用 SUM 函數，並使用 Inventory Value 的值作為參數來生成列於第 3 行、第 B 列（也稱為 B3）的總和。

## NoSQL

NoSQL 是一個涵蓋非關聯式數據存儲方式的術語，可以解釋為 "非 SQL"、"非關聯式" 或 "不僅僅是 SQL"。這些類型的數據庫系統可以分為四種類型。

![鍵值數據存儲的圖形表示，顯示 4 個唯一的數字鍵與 4 個不同的值相關聯](../../../../translated_images/kv-db.e8f2b75686bbdfcba0c827b9272c10ae0821611ea0fe98429b9d13194383afa6.hk.png)
> 來源：[Michał Białecki Blog](https://www.michalbialecki.com/2018/03/18/azure-cosmos-db-key-value-database-cloud/)

[鍵值](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#keyvalue-data-stores)數據庫將唯一鍵（唯一標識符）與值配對。這些配對使用 [哈希表](https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/tutorial/) 和適當的哈希函數存儲。

![圖形數據存儲的圖形表示，顯示人、他們的興趣和位置之間的關係](../../../../translated_images/graph-db.d13629152f79a9dac895b20fa7d841d4d4d6f6008b1382227c3bbd200fd4cfa1.hk.png)
> 來源：[Microsoft](https://docs.microsoft.com/en-us/azure/cosmos-db/graph/graph-introduction#graph-database-by-example)

[圖形](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#graph-data-stores)數據庫描述數據中的關係，並表示為節點和邊的集合。節點表示實體，即現實世界中存在的事物，例如學生或銀行賬單。邊表示兩個實體之間的關係。每個節點和邊都有屬性，提供有關每個節點和邊的附加信息。

![列式數據存儲的圖形表示，顯示一個客戶數據庫，包含兩個列族，分別命名為 Identity 和 Contact Info](../../../../translated_images/columnar-db.ffcfe73c3e9063a8c8f93f8ace85e1200863584b1e324eb5159d8ca10f62ec04.hk.png)

[列式](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#columnar-data-stores)數據存儲將數據組織為列和行，類似於關聯式數據結構，但每列被分為稱為列族的組，其中一列下的所有數據都是相關的，可以作為一個單元檢索和更改。

### 使用 Azure Cosmos DB 的文檔數據存儲

[文檔](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#document-data-stores)數據存儲基於鍵值數據存儲的概念，由一系列字段和對象組成。本節將使用 Cosmos DB 模擬器探索文檔數據庫。

Cosmos DB 數據庫符合 "不僅僅是 SQL" 的定義，其中 Cosmos DB 的文檔數據庫依賴 SQL 來查詢數據。[上一課](../05-relational-databases/README.md) 關於 SQL 涵蓋了該語言的基礎知識，我們將能夠在此處將一些相同的查詢應用於文檔數據庫。我們將使用 Cosmos DB 模擬器，它允許我們在電腦上本地創建和探索文檔數據庫。閱讀更多關於模擬器的信息 [此處](https://docs.microsoft.com/en-us/azure/cosmos-db/local-emulator?tabs=ssl-netstd21)。

文檔是字段和對象值的集合，其中字段描述對象值代表的內容。以下是一個文檔示例。

```json
{
    "firstname": "Eva",
    "age": 44,
    "id": "8c74a315-aebf-4a16-bb38-2430a9896ce5",
    "_rid": "bHwDAPQz8s0BAAAAAAAAAA==",
    "_self": "dbs/bHwDAA==/colls/bHwDAPQz8s0=/docs/bHwDAPQz8s0BAAAAAAAAAA==/",
    "_etag": "\"00000000-0000-0000-9f95-010a691e01d7\"",
    "_attachments": "attachments/",
    "_ts": 1630544034
}
```

此文檔中的關鍵字段包括：`firstname`、`id` 和 `age`。其餘帶有下劃線的字段由 Cosmos DB 自動生成。

#### 使用 Cosmos DB 模擬器探索數據

您可以 [在此處下載並安裝 Windows 版模擬器](https://aka.ms/cosmosdb-emulator)。有關如何在 macOS 和 Linux 上運行模擬器的選項，請參考 [此文檔](https://docs.microsoft.com/en-us/azure/cosmos-db/local-emulator?tabs=ssl-netstd21#run-on-linux-macos)。

模擬器啟動後會打開一個瀏覽器窗口，其中的 Explorer 視圖允許您探索文檔。

![Cosmos DB 模擬器的 Explorer 視圖](../../../../translated_images/cosmosdb-emulator-explorer.a1c80b1347206fe2f30f88fc123821636587d04fc5a56a9eb350c7da6b31f361.hk.png)

如果您正在跟隨教程，請點擊 "Start with Sample" 生成一個名為 SampleDB 的示例數據庫。如果通過點擊箭頭展開 SampleDB，您會找到一個名為 `Persons` 的容器，容器包含一系列項目，即容器內的文檔。您可以探索 `Items` 下的四個單獨文檔。

![在 Cosmos DB 模擬器中探索示例數據](../../../../translated_images/cosmosdb-emulator-persons.bf640586a7077c8985dfd3071946465c8e074c722c7c202d6d714de99a93b90a.hk.png)

#### 使用 Cosmos DB 模擬器查詢文檔數據

我們還可以通過點擊 "New SQL Query" 按鈕（左側第二個按鈕）來查詢示例數據。

`SELECT * FROM c` 返回容器中的所有文檔。讓我們添加一個 where 子句，查找年齡小於 40 的人。

`SELECT * FROM c where c.age < 40`

![在 Cosmos DB 模擬器中運行 SELECT 查詢，查找 age 字段值小於 40 的文檔](../../../../translated_images/cosmosdb-emulator-persons-query.6905ebb497e3cd047cd96e55a0a03f69ce1b91b2b3d8c147e617b746b22b7e33.hk.png)

查詢返回了兩個文檔，注意每個文檔的 age 值都小於 40。

#### JSON 與文檔

如果您熟悉 JavaScript Object Notation (JSON)，您會注意到文檔看起來與 JSON 類似。此目錄中有一個 `PersonsData.json` 文件，包含更多數據，您可以通過模擬器中的 `Upload Item` 按鈕將其上傳到 Persons 容器。

在大多數情況下，返回 JSON 數據的 API 可以直接轉移並存儲到文檔數據庫中。以下是另一個文檔，它表示從 Microsoft Twitter 帳戶檢索的推文，該推文使用 Twitter API 獲取，然後插入到 Cosmos DB 中。

```json
{
    "created_at": "2021-08-31T19:03:01.000Z",
    "id": "1432780985872142341",
    "text": "Blank slate. Like this tweet if you’ve ever painted in Microsoft Paint before. https://t.co/cFeEs8eOPK",
    "_rid": "dhAmAIUsA4oHAAAAAAAAAA==",
    "_self": "dbs/dhAmAA==/colls/dhAmAIUsA4o=/docs/dhAmAIUsA4oHAAAAAAAAAA==/",
    "_etag": "\"00000000-0000-0000-9f84-a0958ad901d7\"",
    "_attachments": "attachments/",
    "_ts": 1630537000
```

此文檔中的關鍵字段包括：`created_at`、`id` 和 `text`。

## 🚀 挑戰

目錄中有一個 `TwitterData.json` 文件，您可以將其上傳到 SampleDB 數據庫。建議您將其添加到一個單獨的容器中。這可以通過以下步驟完成：

1. 點擊右上角的 "New Container" 按鈕
1. 選擇現有數據庫 (SampleDB)，為容器創建一個容器 ID
1. 將分區鍵設置為 `/id`
1. 點擊 OK（您可以忽略此視圖中的其他信息，因為這是一個在本地運行的小型數據集）
1. 打開您的新容器，並使用 `Upload Item` 按鈕上傳 Twitter Data 文件

嘗試運行一些 SELECT 查詢，查找 text 字段中包含 Microsoft 的文檔。提示：嘗試使用 [LIKE 關鍵字](https://docs.microsoft.com/en-us/azure/cosmos-db/sql/sql-query-keywords#using-like-with-the--wildcard-character)。

## [課後測驗](https://ff-quizzes.netlify.app/en/ds/)

## 回顧與自學

- 本課程未涵蓋此電子表格中添加的一些額外格式和功能。如果您有興趣了解更多，Microsoft 提供了 [大量的 Excel 文檔和視頻庫](https://support.microsoft.com/excel)。

- 此架構文檔詳細介紹了不同類型非關聯式數據的特徵：[非關聯式數據和 NoSQL](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data)。

- Cosmos DB 是一個基於雲的非關聯式數據庫，也可以存儲本課程中提到的不同 NoSQL 類型。了解更多這些類型的信息，請參考 [Cosmos DB Microsoft Learn 模塊](https://docs.microsoft.com/en-us/learn/paths/work-with-nosql-data-in-azure-cosmos-db/)。

## 作業

[Soda Profits](assignment.md)

---

**免責聲明**：  
本文件已使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。原始語言的文件應被視為權威來源。對於重要信息，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋概不負責。