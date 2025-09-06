<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2f2d7693f28e4b2675f275e489dc5aac",
  "translation_date": "2025-08-25T16:17:50+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/assignment.md",
  "language_code": "ja"
}
-->
# 空港データの表示

[SQLite](https://sqlite.org/index.html) を使用して構築された [データベース](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) が提供されています。このデータベースには空港に関する情報が含まれています。スキーマは以下に示されています。[Visual Studio Code](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) の [SQLite 拡張機能](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) を使用して、さまざまな都市の空港情報を表示します。

## 手順

この課題を始めるには、いくつかのステップを実行する必要があります。ツールをインストールし、サンプルデータベースをダウンロードしてください。

### システムのセットアップ

Visual Studio Code と SQLite 拡張機能を使用してデータベースと対話できます。

1. [code.visualstudio.com](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) にアクセスし、指示に従って Visual Studio Code をインストールします
1. [SQLite 拡張機能](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) を Marketplace ページの指示に従ってインストールします

### データベースのダウンロードとオープン

次に、データベースをダウンロードして開きます。

1. [GitHub からデータベースファイル](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) をダウンロードし、任意のディレクトリに保存します
1. Visual Studio Code を開きます
1. **Ctl-Shift-P**（Mac の場合は **Cmd-Shift-P**）を押して `SQLite: Open database` と入力し、SQLite 拡張機能でデータベースを開きます
1. **Choose database from file** を選択し、先ほどダウンロードした **airports.db** ファイルを開きます
1. データベースを開いた後（画面に更新は表示されません）、**Ctl-Shift-P**（Mac の場合は **Cmd-Shift-P**）を押して `SQLite: New query` と入力し、新しいクエリウィンドウを作成します

新しいクエリウィンドウを開くと、データベースに対して SQL ステートメントを実行できます。**Ctl-Shift-Q**（Mac の場合は **Cmd-Shift-Q**）を使用してクエリを実行できます。

> [!NOTE] SQLite 拡張機能の詳細については、[ドキュメント](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) を参照してください

## データベーススキーマ

データベースのスキーマとは、テーブルの設計と構造のことです。**airports** データベースには 2 つのテーブルがあります。`cities` はイギリスとアイルランドの都市のリストを含み、`airports` はすべての空港のリストを含みます。一部の都市には複数の空港がある可能性があるため、情報を保存するために 2 つのテーブルが作成されました。この演習では、結合を使用してさまざまな都市の情報を表示します。

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

1. `Cities` テーブル内のすべての都市名
1. `Cities` テーブル内のアイルランドのすべての都市
1. 各空港名とその都市および国
1. ロンドン（イギリス）のすべての空港

## 評価基準

| 優秀 | 適切 | 改善が必要 |
| ---- | ---- | ---------- |

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知ください。元の言語で記載された文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解釈について、当社は責任を負いません。