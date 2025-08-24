<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "32ddfef8121650f2ca2f3416fd283c37",
  "translation_date": "2025-08-24T12:17:32+00:00",
  "source_file": "2-Working-With-Data/06-non-relational/README.md",
  "language_code": "ja"
}
-->
# データの取り扱い: 非リレーショナルデータ

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/06-NoSQL.png)|
|:---:|
|NoSQLデータの取り扱い - _スケッチノート by [@nitya](https://twitter.com/nitya)_ |

## [事前講義クイズ](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/10)

データはリレーショナルデータベースに限定されません。このレッスンでは非リレーショナルデータに焦点を当て、スプレッドシートとNoSQLの基本を学びます。

## スプレッドシート

スプレッドシートは、セットアップや開始に必要な作業が少ないため、データを保存して探索するための人気のある方法です。このレッスンでは、スプレッドシートの基本的な構成要素、さらに数式や関数について学びます。例はMicrosoft Excelを使用して説明しますが、他のスプレッドシートソフトウェアと比較してもほとんどの部分や手順は似ています。

![空のMicrosoft Excelワークブックと2つのワークシート](../../../../2-Working-With-Data/06-non-relational/images/parts-of-spreadsheet.png)

スプレッドシートはファイルであり、コンピュータ、デバイス、またはクラウドベースのファイルシステムのファイルシステムでアクセス可能です。ソフトウェア自体はブラウザベースである場合もあれば、コンピュータにインストールする必要があるアプリケーションやアプリとしてダウンロードする必要がある場合もあります。Excelではこれらのファイルは**ワークブック**として定義されており、このレッスンではこの用語を使用します。

ワークブックには1つ以上の**ワークシート**が含まれており、各ワークシートはタブでラベル付けされています。ワークシート内には**セル**と呼ばれる長方形があり、実際のデータが含まれます。セルは行と列の交差点であり、列はアルファベット文字でラベル付けされ、行は数字でラベル付けされています。一部のスプレッドシートでは、セル内のデータを説明するヘッダーが最初の数行に含まれています。

Excelワークブックのこれらの基本要素を使用して、[Microsoft Templates](https://templates.office.com/)の在庫管理に焦点を当てた例を使いながら、スプレッドシートの追加部分を説明します。

### 在庫管理

「InventoryExample」という名前のスプレッドシートファイルは、在庫内のアイテムをフォーマットしたスプレッドシートで、3つのワークシートが含まれています。タブには「Inventory List」、「Inventory Pick List」、「Bin Lookup」とラベル付けされています。Inventory Listワークシートの4行目はヘッダーであり、ヘッダー列内の各セルの値を説明しています。

![Microsoft Excelの在庫リスト例からの数式のハイライト](../../../../2-Working-With-Data/06-non-relational/images/formula-excel.png)

セルが他のセルの値に依存してその値を生成する場合があります。この在庫リストスプレッドシートは、在庫内の各アイテムのコストを追跡していますが、在庫全体の価値を知る必要がある場合はどうすればよいでしょうか。[**数式**](https://support.microsoft.com/en-us/office/overview-of-formulas-34519a4e-1e8d-4f4b-84d4-d642c4f63263)はセルデータに対して操作を行い、この例では在庫の価値を計算するために使用されます。このスプレッドシートでは、Inventory Value列の数式を使用して、QTYヘッダーの下の数量とCOSTヘッダーの下のコストを掛け合わせて各アイテムの価値を計算しています。セルをダブルクリックまたはハイライトすると数式が表示されます。数式は等号（=）で始まり、その後に計算や操作が続きます。

![Microsoft Excelの在庫リスト例からの関数のハイライト](../../../../2-Working-With-Data/06-non-relational/images/function-excel.png)

在庫価値のすべての値を合計してその総価値を得るために、別の数式を使用することができます。各セルを加算して合計を生成することもできますが、それは手間のかかる作業です。Excelには[**関数**](https://support.microsoft.com/en-us/office/sum-function-043e1c7d-7726-4e80-8f32-07b23e057f89)と呼ばれる、セル値に対して計算を行うための事前定義された数式があります。関数には引数が必要であり、これらは計算を行うために必要な値です。関数が複数の引数を必要とする場合、それらは特定の順序でリストされる必要があり、そうでないと関数が正しい値を計算できない場合があります。この例ではSUM関数を使用し、Inventory Valueの値を引数として使用して、B3（3行目、列B）にリストされた合計を生成しています。

## NoSQL

NoSQLは非リレーショナルデータを保存するさまざまな方法を指す包括的な用語であり、「非SQL」、「非リレーショナル」、または「SQLだけではない」と解釈されることがあります。このタイプのデータベースシステムは4つのタイプに分類されます。

![4つのユニークな数値キーがさまざまな値と関連付けられているキー値データストアのグラフィカル表現](../../../../2-Working-With-Data/06-non-relational/images/kv-db.png)
> 出典: [Michał Białecki Blog](https://www.michalbialecki.com/2018/03/18/azure-cosmos-db-key-value-database-cloud/)

[キー値](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#keyvalue-data-stores)データベースは、ユニークな識別子であるキーと値をペアにして保存します。これらのペアは、適切なハッシュ関数を使用して[ハッシュテーブル](https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/tutorial/)に保存されます。

![人々、彼らの興味、場所の関係を示すグラフデータストアのグラフィカル表現](../../../../2-Working-With-Data/06-non-relational/images/graph-db.png)
> 出典: [Microsoft](https://docs.microsoft.com/en-us/azure/cosmos-db/graph/graph-introduction#graph-database-by-example)

[グラフ](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#graph-data-stores)データベースはデータの関係を記述し、ノードとエッジの集合として表されます。ノードは実世界に存在するエンティティ（例: 学生や銀行の明細書）を表します。エッジは2つのエンティティ間の関係を表します。各ノードとエッジには、それぞれのノードやエッジに関する追加情報を提供するプロパティがあります。

![IdentityとContact Infoという2つの列ファミリーを持つ顧客データベースを示すカラム型データストアのグラフィカル表現](../../../../2-Working-With-Data/06-non-relational/images/columnar-db.png)

[カラム型](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#columnar-data-stores)データストアは、リレーショナルデータ構造のようにデータを列と行に整理しますが、各列は列ファミリーと呼ばれるグループに分割されます。列ファミリー内のすべてのデータは関連しており、1つの単位で取得および変更することができます。

### Azure Cosmos DBを使用したドキュメントデータストア

[ドキュメント](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#document-data-stores)データストアはキー値データストアの概念を基に構築されており、フィールドとオブジェクトの集合で構成されています。このセクションでは、Cosmos DBエミュレーターを使用してドキュメントデータベースを探ります。

Cosmos DBデータベースは「SQLだけではない」という定義に適合し、Cosmos DBのドキュメントデータベースはSQLを使用してデータをクエリします。[前回のレッスン](../05-relational-databases/README.md)ではSQLの基本を学びましたが、ここではドキュメントデータベースに同じクエリを適用することができます。Cosmos DBエミュレーターを使用して、コンピュータ上でローカルにドキュメントデータベースを作成して探索します。エミュレーターについての詳細は[こちら](https://docs.microsoft.com/en-us/azure/cosmos-db/local-emulator?tabs=ssl-netstd21)をご覧ください。

ドキュメントはフィールドとオブジェクト値の集合であり、フィールドはオブジェクト値が何を表しているかを説明します。以下はドキュメントの例です。

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

このドキュメントで注目すべきフィールドは、`firstname`、`id`、`age`です。その他のフィールドはCosmos DBによって生成されました。

#### Cosmos DBエミュレーターを使用したデータの探索

エミュレーターは[Windows用にこちらから](https://aka.ms/cosmosdb-emulator)ダウンロードしてインストールできます。macOSやLinuxでエミュレーターを実行する方法については、この[ドキュメント](https://docs.microsoft.com/en-us/azure/cosmos-db/local-emulator?tabs=ssl-netstd21#run-on-linux-macos)を参照してください。

エミュレーターはブラウザウィンドウを起動し、Explorerビューでドキュメントを探索できます。

![Cosmos DBエミュレーターのExplorerビュー](../../../../2-Working-With-Data/06-non-relational/images/cosmosdb-emulator-explorer.png)

もし一緒に進めている場合は、「Start with Sample」をクリックしてSampleDBというサンプルデータベースを生成してください。SampleDBを展開すると、`Persons`というコンテナーが見つかります。コンテナーはアイテムのコレクションを保持しており、これがコンテナー内のドキュメントです。`Items`の下にある4つの個別のドキュメントを探索できます。

![Cosmos DBエミュレーターでサンプルデータを探索](../../../../2-Working-With-Data/06-non-relational/images/cosmosdb-emulator-persons.png)

#### Cosmos DBエミュレーターを使用したドキュメントデータのクエリ

新しいSQLクエリボタン（左から2番目のボタン）をクリックすると、サンプルデータをクエリすることができます。

`SELECT * FROM c`はコンテナー内のすべてのドキュメントを返します。where句を追加して40歳未満の人を見つけてみましょう。

`SELECT * FROM c where c.age < 40`

![Cosmos DBエミュレーターでサンプルデータに対してSELECTクエリを実行し、ageフィールド値が40未満のドキュメントを見つける](../../../../2-Working-With-Data/06-non-relational/images/cosmosdb-emulator-persons-query.png)

このクエリは2つのドキュメントを返します。各ドキュメントのage値が40未満であることに注目してください。

#### JSONとドキュメント

JavaScript Object Notation (JSON)に詳しい場合、ドキュメントがJSONに似ていることに気付くでしょう。このディレクトリには`PersonsData.json`というファイルがあり、エミュレーターのPersonsコンテナーにアップロードすることでさらにデータを追加できます。`Upload Item`ボタンを使用してください。

多くの場合、JSONデータを返すAPIは、直接転送してドキュメントデータベースに保存することができます。以下は別のドキュメントで、MicrosoftのTwitterアカウントからTwitter APIを使用して取得され、Cosmos DBに挿入されたツイートを表しています。

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

このドキュメントで注目すべきフィールドは、`created_at`、`id`、`text`です。

## 🚀 チャレンジ

`TwitterData.json`というファイルをSampleDBデータベースにアップロードすることができます。別のコンテナーに追加することをお勧めします。以下の手順で行えます:

1. 右上の新しいコンテナーボタンをクリック
1. 既存のデータベース（SampleDB）を選択し、コンテナーIDを作成
1. パーティションキーを`/id`に設定
1. OKをクリック（このビューの残りの情報は無視して構いません。これはローカルマシンで実行される小さなデータセットです）
1. 新しいコンテナーを開き、`Upload Item`ボタンでTwitter Dataファイルをアップロード

いくつかのSELECTクエリを実行して、textフィールドにMicrosoftが含まれるドキュメントを見つけてみてください。ヒント: [LIKEキーワード](https://docs.microsoft.com/en-us/azure/cosmos-db/sql/sql-query-keywords#using-like-with-the--wildcard-character)を使用してみてください。

## [事後講義クイズ](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/11)

## 復習と自己学習

- このレッスンではカバーしていないスプレッドシートに追加されたフォーマットや機能がいくつかあります。Excelについてもっと学びたい場合は、Microsoftの[豊富なドキュメントとビデオライブラリ](https://support.microsoft.com/excel)をご覧ください。

- 非リレーショナルデータのさまざまなタイプの特徴についての詳細は、このアーキテクチャドキュメントをご覧ください: [非リレーショナルデータとNoSQL](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data)

- Cosmos DBは、ここで説明したNoSQLタイプを保存できるクラウドベースの非リレーショナルデータベースです。この[Cosmos DB Microsoft Learn Module](https://docs.microsoft.com/en-us/learn/paths/work-with-nosql-data-in-azure-cosmos-db/)でこれらのタイプについてさらに学ぶことができます。

## 課題

[Soda Profits](assignment.md)

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期すよう努めておりますが、自動翻訳には誤りや不正確さが含まれる可能性があります。元の言語で記載された原文が公式な情報源と見なされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の使用に起因する誤解や誤認について、当方は一切の責任を負いません。