<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "25b37acdfb2452917c1aa2e2ca44317a",
  "translation_date": "2025-10-24T09:53:35+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/assignment.md",
  "language_code": "ja"
}
-->
# 空港データの表示

[SQLite](https://sqlite.org/index.html)を基盤とした[データベース](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db)が提供されています。このデータベースには空港に関する情報が含まれています。以下にスキーマが表示されています。[Visual Studio Code](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum)の[SQLite拡張機能](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum)を使用して、さまざまな都市の空港情報を表示します。

## 手順

課題を始めるには、いくつかのステップを実行する必要があります。ツールをインストールし、サンプルデータベースをダウンロードしてください。

### システムのセットアップ

Visual Studio CodeとSQLite拡張機能を使用してデータベースと対話できます。

1. [code.visualstudio.com](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum)にアクセスし、指示に従ってVisual Studio Codeをインストールしてください。
1. Marketplaceページの指示に従い、[SQLite拡張機能](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum)をインストールしてください。

### データベースのダウンロードと開く

次に、データベースをダウンロードして開きます。

1. [GitHubからデータベースファイル](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db)をダウンロードし、任意のディレクトリに保存してください。
1. Visual Studio Codeを開きます。
1. **Ctl-Shift-P**（Macの場合は**Cmd-Shift-P**）を選択し、`SQLite: Open database`と入力してSQLite拡張機能でデータベースを開きます。
1. **Choose database from file**を選択し、先ほどダウンロードした**airports.db**ファイルを開きます。
1. データベースを開いた後（画面に更新は表示されません）、**Ctl-Shift-P**（Macの場合は**Cmd-Shift-P**）を選択し、`SQLite: New query`と入力して新しいクエリウィンドウを作成します。

新しいクエリウィンドウを開くと、データベースに対してSQL文を実行できます。**Ctl-Shift-Q**（Macの場合は**Cmd-Shift-Q**）を使用してデータベースにクエリを実行できます。

> [!NOTE] 
> SQLite拡張機能の詳細については、[ドキュメント](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum)を参照してください。

## データベーススキーマ

データベースのスキーマは、テーブルの設計と構造を指します。**airports**データベースには、イギリスとアイルランドの都市リストを含む`cities`テーブルと、すべての空港リストを含む`airports`テーブルの2つのテーブルがあります。一部の都市には複数の空港があるため、情報を保存するために2つのテーブルが作成されました。この演習では、結合を使用して異なる都市の情報を表示します。

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

## 課題

以下の情報を返すクエリを作成してください：

1. `Cities`テーブル内のすべての都市名
1. `Cities`テーブル内のアイルランドのすべての都市
1. 都市と国とともにすべての空港名
1. イギリスのロンドンにあるすべての空港

## 評価基準

| 優秀 | 適切 | 改善が必要 |
| ---- | ---- | ---------- |

---

**免責事項**:  
この文書はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。元の言語で記載された文書を正式な情報源としてご参照ください。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤認について、当方は一切の責任を負いません。