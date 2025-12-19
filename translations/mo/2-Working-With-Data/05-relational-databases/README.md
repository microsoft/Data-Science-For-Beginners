<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11739c7b40e7c6b16ad29e3df4e65862",
  "translation_date": "2025-12-19T10:43:38+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/README.md",
  "language_code": "mo"
}
-->
# 處理數據：關聯式資料庫

|![ Sketchnote 由 [(@sketchthedocs)](https://sketchthedocs.dev) 製作 ](../../sketchnotes/05-RelationalData.png)|
|:---:|
| 處理數據：關聯式資料庫 - _Sketchnote 由 [@nitya](https://twitter.com/nitya) 製作_ |

你很可能過去曾使用過試算表來儲存資訊。你有一組列和欄，列包含資訊（或數據），欄描述該資訊（有時稱為元資料）。關聯式資料庫建立在表格中欄和列的核心原則上，允許你將資訊分散在多個表格中。這讓你能處理更複雜的數據，避免重複，並在探索數據時擁有彈性。讓我們來探索關聯式資料庫的概念。

## [課前測驗](https://ff-quizzes.netlify.app/en/ds/quiz/8)

## 一切從表格開始

關聯式資料庫的核心是表格。就像試算表一樣，表格是欄和列的集合。列包含我們想處理的數據或資訊，例如城市名稱或降雨量。欄描述它們所儲存的數據。

讓我們開始探索，建立一個表格來儲存城市資訊。我們可能會從城市名稱和國家開始。你可以將它儲存在表格中，如下所示：

| City     | Country       |
| -------- | ------------- |
| Tokyo    | Japan         |
| Atlanta  | United States |
| Auckland | New Zealand   |

注意欄名 **city**、**country** 和 **population** 描述所儲存的數據，每一列包含一個城市的資訊。

## 單一表格方法的缺點

你可能覺得上面的表格相當熟悉。讓我們開始為我們的新資料庫添加一些額外數據——年度降雨量（以毫米計）。我們將關注2018、2019和2020年。如果我們為東京添加，可能會是這樣：

| City  | Country | Year | Amount |
| ----- | ------- | ---- | ------ |
| Tokyo | Japan   | 2020 | 1690   |
| Tokyo | Japan   | 2019 | 1874   |
| Tokyo | Japan   | 2018 | 1445   |

你注意到表格有什麼嗎？你可能會注意到我們不斷重複城市的名稱和國家。這可能佔用相當多的儲存空間，而且多份複製基本上是不必要的。畢竟，東京只有一個我們感興趣的名稱。

好，讓我們試試別的方法。為每年新增欄位：

| City     | Country       | 2018 | 2019 | 2020 |
| -------- | ------------- | ---- | ---- | ---- |
| Tokyo    | Japan         | 1445 | 1874 | 1690 |
| Atlanta  | United States | 1779 | 1111 | 1683 |
| Auckland | New Zealand   | 1386 | 942  | 1176 |

雖然這避免了列的重複，但帶來了其他挑戰。每當有新的一年時，我們需要修改表格結構。此外，隨著數據增長，將年份作為欄位會使檢索和計算數值變得更複雜。

這就是為什麼我們需要多個表格和關聯。透過拆分數據，我們可以避免重複，並在處理數據時擁有更多彈性。

## 關聯的概念

讓我們回到數據，決定如何拆分。我們知道要儲存城市的名稱和國家，所以這可能最好放在一個表格中。

| City     | Country       |
| -------- | ------------- |
| Tokyo    | Japan         |
| Atlanta  | United States |
| Auckland | New Zealand   |

但在建立下一個表格之前，我們需要找出如何參考每個城市。我們需要某種識別符、ID或（在技術資料庫術語中）主鍵。主鍵是用來識別表格中特定一列的值。雖然這可以基於值本身（例如使用城市名稱），但幾乎總是應該是數字或其他識別符。我們不希望ID改變，因為那會破壞關聯。你會發現大多數情況下主鍵或ID會是自動生成的數字。

> ✅ 主鍵常縮寫為 PK

### cities

| city_id | City     | Country       |
| ------- | -------- | ------------- |
| 1       | Tokyo    | Japan         |
| 2       | Atlanta  | United States |
| 3       | Auckland | New Zealand   |

> ✅ 你會注意到在本課程中，我們交替使用「id」和「主鍵」這兩個術語。這些概念也適用於你稍後會探索的 DataFrames。DataFrames 不使用「主鍵」這個術語，但你會發現它們的行為非常相似。

建立了城市表格後，讓我們儲存降雨量。與其重複城市的完整資訊，我們可以使用ID。我們還應確保新建立的表格也有一個 *id* 欄位，因為所有表格都應該有id或主鍵。

### rainfall

| rainfall_id | city_id | Year | Amount |
| ----------- | ------- | ---- | ------ |
| 1           | 1       | 2018 | 1445   |
| 2           | 1       | 2019 | 1874   |
| 3           | 1       | 2020 | 1690   |
| 4           | 2       | 2018 | 1779   |
| 5           | 2       | 2019 | 1111   |
| 6           | 2       | 2020 | 1683   |
| 7           | 3       | 2018 | 1386   |
| 8           | 3       | 2019 | 942    |
| 9           | 3       | 2020 | 1176   |

注意新建立的 **rainfall** 表格中的 **city_id** 欄。這欄包含參考 **cities** 表中ID的值。在技術關聯資料術語中，這稱為 **外鍵**；它是另一個表的主鍵。你可以把它當作參考或指標。**city_id** 1 參考東京。

> [!NOTE]  
> 外鍵常縮寫為 FK

## 取回數據

將數據分成兩個表格後，你可能想知道如何取回它。如果我們使用像 MySQL、SQL Server 或 Oracle 這樣的關聯式資料庫，我們可以使用一種叫做結構化查詢語言（Structured Query Language，SQL）的語言。SQL（有時讀作 sequel）是用來取回和修改關聯式資料庫中數據的標準語言。

取回數據時使用命令 `SELECT`。基本上，你**選擇**想看的欄位，**從**它們所在的表格中取出。如果你只想顯示城市名稱，可以使用以下語句：

```sql
SELECT city
FROM cities;

-- Output:
-- Tokyo
-- Atlanta
-- Auckland
```

`SELECT` 是列出欄位的地方，`FROM` 是列出表格的地方。

> [!NOTE]  
> SQL 語法不區分大小寫，`select` 和 `SELECT` 意思相同。但根據你使用的資料庫類型，欄位和表格名稱可能區分大小寫。因此，最佳實務是將程式碼中所有東西都視為區分大小寫。撰寫 SQL 查詢時，常見慣例是將關鍵字全部大寫。

上述查詢會顯示所有城市。假設我們只想顯示紐西蘭的城市，我們需要某種過濾條件。SQL 的關鍵字是 `WHERE`，意思是「在某條件為真時」。

```sql
SELECT city
FROM cities
WHERE country = 'New Zealand';

-- Output:
-- Auckland
```

## 連接數據

到目前為止，我們只從單一表格取回數據。現在我們想將 **cities** 和 **rainfall** 的數據合併。這是透過*連接*它們完成的。你會在兩個表格之間建立一個接縫，並匹配每個表格中某欄的值。

在我們的例子中，我們會將 **rainfall** 中的 **city_id** 欄與 **cities** 中的 **city_id** 欄匹配。這會將降雨量與其對應的城市匹配起來。我們執行的連接類型稱為*內部*連接，意思是如果有任何列在另一個表中找不到匹配，就不會顯示。在我們的情況中，每個城市都有降雨量，所以全部都會顯示。

讓我們取回2019年所有城市的降雨量。

我們將分步進行。第一步是透過指定接縫的欄位——前面提到的 **city_id**，將數據連接起來。

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
```

我們已標示出想要的兩個欄位，以及我們想用 **city_id** 連接表格。現在我們可以加上 `WHERE` 語句，只篩選2019年。

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
WHERE rainfall.year = 2019

-- Output

-- city     | amount
-- -------- | ------
-- Tokyo    | 1874
-- Atlanta  | 1111
-- Auckland |  942
```

## 總結

關聯式資料庫的核心是將資訊分散在多個表格中，然後再合併顯示和分析。這提供了高度的彈性來執行計算和操作數據。你已經看到關聯式資料庫的核心概念，以及如何在兩個表格之間執行連接。

## 🚀 挑戰

網路上有許多關聯式資料庫可用。你可以利用上述學到的技能來探索數據。

## 課後測驗

## [課後測驗](https://ff-quizzes.netlify.app/en/ds/quiz/9)

## 複習與自學

在 [Microsoft Learn](https://docs.microsoft.com/learn?WT.mc_id=academic-77958-bethanycheum) 上有多個資源，供你繼續探索 SQL 和關聯式資料庫概念

- [描述關聯數據的概念](https://docs.microsoft.com//learn/modules/describe-concepts-of-relational-data?WT.mc_id=academic-77958-bethanycheum)
- [開始使用 Transact-SQL 查詢](https://docs.microsoft.com//learn/paths/get-started-querying-with-transact-sql?WT.mc_id=academic-77958-bethanycheum)（Transact-SQL 是 SQL 的一個版本）
- [Microsoft Learn 上的 SQL 內容](https://docs.microsoft.com/learn/browse/?products=azure-sql-database%2Csql-server&expanded=azure&WT.mc_id=academic-77958-bethanycheum)

## 作業

[顯示機場數據](assignment.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我哋致力於確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件之母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。對於因使用本翻譯而引起之任何誤解或誤釋，我哋概不負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->