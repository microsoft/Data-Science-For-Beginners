<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "32ddfef8121650f2ca2f3416fd283c37",
  "translation_date": "2025-08-25T16:34:45+00:00",
  "source_file": "2-Working-With-Data/06-non-relational/README.md",
  "language_code": "ja"
}
-->
# データの操作: 非リレーショナルデータ

|![ スケッチノート by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/06-NoSQL.png)|
|:---:|
|NoSQLデータの操作 - _スケッチノート by [@nitya](https://twitter.com/nitya)_ |

## [講義前クイズ](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/10)

データはリレーショナルデータベースに限定されません。このレッスンでは、非リレーショナルデータに焦点を当て、スプレッドシートとNoSQLの基本を学びます。

## スプレッドシート

スプレッドシートは、セットアップや開始に手間がかからないため、データを保存して探索するための一般的な方法です。このレッスンでは、スプレッドシートの基本的な構成要素、数式や関数について学びます。例はMicrosoft Excelを使用して説明しますが、他のスプレッドシートソフトウェアと比較しても、ほとんどの部分やトピックは似た名前や手順を持っています。

![空のMicrosoft Excelワークブックと2つのワークシート](../../../../translated_images/parts-of-spreadsheet.120711c82aa18a45c3e62a491a15bba0a31ab0e9db407ec022702fed8ffd89bf.ja.png)

スプレッドシートはファイルであり、コンピュータ、デバイス、またはクラウドベースのファイルシステムのファイルシステムでアクセス可能です。ソフトウェア自体はブラウザベースの場合もあれば、コンピュータにインストールする必要があるアプリケーションやアプリとしてダウンロードする必要がある場合もあります。Excelでは、これらのファイルは**ワークブック**として定義されており、このレッスンではこの用語を使用します。

ワークブックには1つ以上の**ワークシート**が含まれ、それぞれのワークシートはタブでラベル付けされています。ワークシート内には**セル**と呼ばれる長方形があり、実際のデータが含まれます。セルは行と列の交差点であり、列はアルファベット文字で、行は数字でラベル付けされています。一部のスプレッドシートでは、セル内のデータを説明するために最初の数行にヘッダーが含まれています。

Excelワークブックのこれらの基本要素を使用して、[Microsoft Templates](https://templates.office.com/)の在庫管理に焦点を当てた例を使い、スプレッドシートの追加部分を見ていきます。

### 在庫管理

"InventoryExample"という名前のスプレッドシートファイルは、在庫内のアイテムをフォーマットしたスプレッドシートで、"Inventory List"、"Inventory Pick List"、"Bin Lookup"という3つのワークシートが含まれています。"Inventory List"ワークシートの4行目はヘッダーで、ヘッダー列内の各セルの値を説明しています。

![Microsoft Excelの在庫リスト例からの数式のハイライト](../../../../translated_images/formula-excel.ad1068c220892f5ead570d12f2394897961d31a5043a1dd4e6fc5d7690c7a14e.ja.png)

セルが他のセルの値に依存してその値を生成する場合があります。在庫リストスプレッドシートは、在庫内の各アイテムのコストを追跡していますが、在庫全体の価値を知りたい場合はどうすればよいでしょうか？[**数式**](https://support.microsoft.com/en-us/office/overview-of-formulas-34519a4e-1e8d-4f4b-84d4-d642c4f63263)はセルデータに対して操作を行い、この例では在庫の価値を計算するために使用されます。このスプレッドシートでは、"Inventory Value"列に数式を使用して、"QTY"ヘッダーの下の数量と"COST"ヘッダーの下のコストを掛け合わせて各アイテムの価値を計算しています。セルをダブルクリックまたはハイライトすると数式が表示されます。数式は等号（=）で始まり、その後に計算や操作が続きます。

![Microsoft Excelの在庫リスト例からの関数のハイライト](../../../../translated_images/function-excel.be2ae4feddc10ca089f3d4363040d93b7fd046c8d4f83ba975ec46483ee99895.ja.png)

在庫価値のすべての値を合計してその総価値を求めるために、別の数式を使用することもできます。これは各セルを加算して合計を生成することで計算できますが、それは手間のかかる作業です。Excelには[**関数**](https://support.microsoft.com/en-us/office/sum-function-043e1c7d-7726-4e80-8f32-07b23e057f89)と呼ばれる、セル値に対して計算を行うための事前定義された数式があります。関数には引数が必要で、これらは計算を行うために必要な値です。関数が複数の引数を必要とする場合、特定の順序でリストする必要があり、そうしないと関数が正しい値を計算できない可能性があります。この例ではSUM関数を使用し、"Inventory Value"の値を引数として使用して、B3（3行目、B列）にリストされている合計を生成しています。

## NoSQL

NoSQLは、非リレーショナルデータを保存するさまざまな方法を指す包括的な用語であり、「非SQL」、「非リレーショナル」、または「SQLだけではない」と解釈されることがあります。この種のデータベースシステムは、4つのタイプに分類できます。

![4つのユニークな数値キーとそれに関連付けられた4つの異なる値を示すキー値データストアの図](../../../../translated_images/kv-db.e8f2b75686bbdfcba0c827b9272c10ae0821611ea0fe98429b9d13194383afa6.ja.png)
> 出典: [Michał Białecki Blog](https://www.michalbialecki.com/2018/03/18/azure-cosmos-db-key-value-database-cloud/)

[キー値](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#keyvalue-data-stores)データベースは、ユニークなキー（値に関連付けられた一意の識別子）と値をペアにします。これらのペアは、適切なハッシュ関数を使用して[ハッシュテーブル](https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/tutorial/)に保存されます。

![人々、彼らの興味、場所の関係を示すグラフデータストアの図](../../../../translated_images/graph-db.d13629152f79a9dac895b20fa7d841d4d4d6f6008b1382227c3bbd200fd4cfa1.ja.png)
> 出典: [Microsoft](https://docs.microsoft.com/en-us/azure/cosmos-db/graph/graph-introduction#graph-database-by-example)

[グラフ](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#graph-data-stores)データベースはデータの関係を記述し、ノードとエッジのコレクションとして表されます。ノードは、学生や銀行の明細書など、現実世界に存在するエンティティを表します。エッジは2つのエンティティ間の関係を表します。各ノードとエッジには、それぞれの追加情報を提供するプロパティがあります。

![顧客データベースを示すカラム型データストアの図。2つのカラムファミリー「Identity」と「Contact Info」がある](../../../../translated_images/columnar-db.ffcfe73c3e9063a8c8f93f8ace85e1200863584b1e324eb5159d8ca10f62ec04.ja.png)

[カラム型](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#columnar-data-stores)データストアは、リレーショナルデータ構造のようにデータを列と行に整理しますが、各列は「カラムファミリー」と呼ばれるグループに分けられます。同じカラム内のすべてのデータは関連しており、一つの単位として取得および変更できます。

### Azure Cosmos DBを使用したドキュメントデータストア

[ドキュメント](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#document-data-stores)データストアは、キー値データストアの概念を基に構築されており、一連のフィールドとオブジェクトで構成されています。このセクションでは、Cosmos DBエミュレーターを使用してドキュメントデータベースを探ります。

Cosmos DBデータベースは「SQLだけではない」という定義に当てはまり、Cosmos DBのドキュメントデータベースはSQLを使用してデータをクエリします。[前回のレッスン](../05-relational-databases/README.md)ではSQLの基本を学びましたが、ここではドキュメントデータベースに同じクエリを適用できます。Cosmos DBエミュレーターを使用して、ローカルコンピュータ上でドキュメントデータベースを作成し、探索します。エミュレーターについての詳細は[こちら](https://docs.microsoft.com/en-us/azure/cosmos-db/local-emulator?tabs=ssl-netstd21)をご覧ください。

ドキュメントはフィールドとオブジェクト値のコレクションであり、フィールドはオブジェクト値が何を表しているかを説明します。以下はドキュメントの例です。

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

このドキュメントで注目すべきフィールドは、`firstname`、`id`、`age`です。アンダースコア付きの他のフィールドはCosmos DBによって生成されました。

#### Cosmos DBエミュレーターを使用したデータの探索

エミュレーターは[Windows用はこちら](https://aka.ms/cosmosdb-emulator)からダウンロードしてインストールできます。macOSおよびLinuxでエミュレーターを実行する方法については、この[ドキュメント](https://docs.microsoft.com/en-us/azure/cosmos-db/local-emulator?tabs=ssl-netstd21#run-on-linux-macos)を参照してください。

エミュレーターを起動するとブラウザウィンドウが開き、Explorerビューでドキュメントを探索できます。

![Cosmos DBエミュレーターのExplorerビュー](../../../../translated_images/cosmosdb-emulator-explorer.a1c80b1347206fe2f30f88fc123821636587d04fc5a56a9eb350c7da6b31f361.ja.png)

一緒に進めている場合は、「Start with Sample」をクリックしてSampleDBというサンプルデータベースを生成してください。SampleDBを展開すると、`Persons`というコンテナが見つかります。コンテナはアイテムのコレクションを保持しており、これらはコンテナ内のドキュメントです。`Items`の下にある4つの個別のドキュメントを探索できます。

![Cosmos DBエミュレーターでサンプルデータを探索](../../../../translated_images/cosmosdb-emulator-persons.bf640586a7077c8985dfd3071946465c8e074c722c7c202d6d714de99a93b90a.ja.png)

#### Cosmos DBエミュレーターを使用したドキュメントデータのクエリ

新しいSQLクエリボタン（左から2番目のボタン）をクリックすると、サンプルデータをクエリすることもできます。

`SELECT * FROM c`はコンテナ内のすべてのドキュメントを返します。where句を追加して、40歳未満の人を見つけてみましょう。

`SELECT * FROM c where c.age < 40`

![Cosmos DBエミュレーターでサンプルデータに対してSELECTクエリを実行し、ageフィールドの値が40未満のドキュメントを見つける](../../../../translated_images/cosmosdb-emulator-persons-query.6905ebb497e3cd047cd96e55a0a03f69ce1b91b2b3d8c147e617b746b22b7e33.ja.png)

クエリは2つのドキュメントを返します。それぞれのドキュメントのage値が40未満であることに注目してください。

#### JSONとドキュメント

JavaScript Object Notation (JSON)に慣れている場合、ドキュメントがJSONに似ていることに気付くでしょう。このディレクトリには`PersonsData.json`というファイルがあり、エミュレーターのPersonsコンテナにアップロードできます。`Upload Item`ボタンを使用してください。

多くの場合、JSONデータを返すAPIは、直接ドキュメントデータベースに転送して保存できます。以下は別のドキュメントで、MicrosoftのTwitterアカウントからTwitter APIを使用して取得され、Cosmos DBに挿入されたツイートを表しています。

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

`TwitterData.json`というファイルがあり、SampleDBデータベースにアップロードできます。別のコンテナに追加することをお勧めします。以下の手順で行えます：

1. 右上の新しいコンテナボタンをクリック
1. 既存のデータベース（SampleDB）を選択し、コンテナIDを作成
1. パーティションキーを`/id`に設定
1. OKをクリック（このビューの他の情報は無視して構いません。これはローカルマシン上で動作する小さなデータセットです）
1. 新しいコンテナを開き、`Upload Item`ボタンでTwitter Dataファイルをアップロード

いくつかのSELECTクエリを実行して、textフィールドにMicrosoftが含まれるドキュメントを見つけてみてください。ヒント：[LIKEキーワード](https://docs.microsoft.com/en-us/azure/cosmos-db/sql/sql-query-keywords#using-like-with-the--wildcard-character)を使用してみてください。

## [講義後クイズ](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/11)

## 復習と自己学習

- このレッスンではカバーしていない、スプレッドシートに追加されたフォーマットや機能があります。Excelについてもっと学びたい場合は、Microsoftの[豊富なドキュメントとビデオライブラリ](https://support.microsoft.com/excel)をご覧ください。

- 非リレーショナルデータのさまざまなタイプの特性については、このアーキテクチャドキュメントをご覧ください：[非リレーショナルデータとNoSQL](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data)

- Cosmos DBは、ここで説明したさまざまなNoSQLタイプを保存できるクラウドベースの非リレーショナルデータベースです。この[Cosmos DB Microsoft Learn Module](https://docs.microsoft.com/en-us/learn/paths/work-with-nosql-data-in-azure-cosmos-db/)でこれらのタイプについてさらに学びましょう。

## 課題

[Soda Profits](assignment.md)

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知ください。元の言語で記載された文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解釈について、当社は責任を負いません。