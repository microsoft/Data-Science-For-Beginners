<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11739c7b40e7c6b16ad29e3df4e65862",
  "translation_date": "2025-12-19T10:51:06+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/README.md",
  "language_code": "ja"
}
-->
# データ操作：リレーショナルデータベース

|![ スケッチノート by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/05-RelationalData.png)|
|:---:|
| データ操作：リレーショナルデータベース - _スケッチノート by [@nitya](https://twitter.com/nitya)_ |

過去に情報を保存するためにスプレッドシートを使ったことがあるかもしれません。行と列のセットがあり、行には情報（またはデータ）が含まれ、列はその情報を説明していました（時にはメタデータと呼ばれます）。リレーショナルデータベースは、テーブル内の列と行というこの基本原則に基づいて構築されており、複数のテーブルに情報を分散させることができます。これにより、より複雑なデータを扱い、重複を避け、データの探索方法に柔軟性を持たせることができます。リレーショナルデータベースの概念を探ってみましょう。

## [事前講義クイズ](https://ff-quizzes.netlify.app/en/ds/quiz/8)

## すべてはテーブルから始まる

リレーショナルデータベースの中心にはテーブルがあります。スプレッドシートと同様に、テーブルは列と行の集合です。行には、都市の名前や降雨量など、扱いたいデータや情報が含まれます。列は格納されるデータを説明します。

都市に関する情報を保存するテーブルを作成することから始めましょう。名前と国を保存することから始めるかもしれません。次のようにテーブルに保存できます：

| City     | Country       |
| -------- | ------------- |
| Tokyo    | Japan         |
| Atlanta  | United States |
| Auckland | New Zealand   |

**city**、**country**、**population** の列名は保存されるデータを説明しており、各行は1つの都市に関する情報を持っていることに注目してください。

## 単一テーブルアプローチの欠点

上記のテーブルは比較的馴染みがあるかもしれません。成長しつつあるデータベースに追加のデータ、例えば年間降雨量（ミリメートル単位）を追加してみましょう。2018年、2019年、2020年のデータに注目します。東京のデータを追加すると次のようになるかもしれません：

| City  | Country | Year | Amount |
| ----- | ------- | ---- | ------ |
| Tokyo | Japan   | 2020 | 1690   |
| Tokyo | Japan   | 2019 | 1874   |
| Tokyo | Japan   | 2018 | 1445   |

このテーブルで何に気づきますか？都市の名前と国を何度も繰り返していることに気づくかもしれません。これはかなりのストレージを消費し、複数のコピーを持つ必要はほとんどありません。結局のところ、東京には1つの名前しかありません。

では、別の方法を試してみましょう。各年のために新しい列を追加します：

| City     | Country       | 2018 | 2019 | 2020 |
| -------- | ------------- | ---- | ---- | ---- |
| Tokyo    | Japan         | 1445 | 1874 | 1690 |
| Atlanta  | United States | 1779 | 1111 | 1683 |
| Auckland | New Zealand   | 1386 | 942  | 1176 |

これにより行の重複は避けられますが、いくつかの別の課題が生じます。新しい年が追加されるたびにテーブルの構造を変更する必要があります。さらに、データが増えると、年を列として持つことは値の取得や計算を難しくします。

これが複数のテーブルとリレーションシップが必要な理由です。データを分割することで重複を避け、データの操作に柔軟性を持たせることができます。

## リレーションシップの概念

データに戻り、どのように分割するかを決めましょう。都市の名前と国を保存したいことはわかっているので、これは1つのテーブルにまとめるのが最適でしょう。

| City     | Country       |
| -------- | ------------- |
| Tokyo    | Japan         |
| Atlanta  | United States |
| Auckland | New Zealand   |

しかし、次のテーブルを作成する前に、各都市を参照する方法を決める必要があります。識別子、ID、または（技術的なデータベース用語で）主キーが必要です。主キーはテーブル内の特定の行を識別するために使われる値です。これは値自体に基づくこともできます（例えば都市名を使うことも可能です）が、ほとんどの場合は数字や他の識別子であるべきです。IDが変わるとリレーションシップが壊れてしまうためです。ほとんどの場合、主キーやIDは自動生成された番号になります。

> ✅ 主キーはしばしばPKと略されます

### cities

| city_id | City     | Country       |
| ------- | -------- | ------------- |
| 1       | Tokyo    | Japan         |
| 2       | Atlanta  | United States |
| 3       | Auckland | New Zealand   |

> ✅ このレッスンでは「id」と「主キー」を同じ意味で使っています。この概念は後で学ぶDataFrameにも適用されます。DataFrameは「主キー」という用語は使いませんが、同様の動作をします。

citiesテーブルを作成したので、降雨量を保存しましょう。都市の完全な情報を重複させる代わりに、idを使います。新しく作成するテーブルにも*id*列を持たせるべきです。すべてのテーブルはidまたは主キーを持つべきだからです。

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

新しく作成した**rainfall**テーブル内の**city_id**列に注目してください。この列は**cities**テーブルのIDを参照する値を含んでいます。技術的なリレーショナルデータ用語では、これは**外部キー**と呼ばれます。別のテーブルの主キーです。単に参照やポインタと考えてください。**city_id** 1は東京を参照しています。

> [!NOTE] 
> 外部キーはしばしばFKと略されます

## データの取得

データを2つのテーブルに分けたので、どのように取得するか疑問に思うかもしれません。MySQL、SQL Server、Oracleなどのリレーショナルデータベースを使う場合、SQL（Structured Query Language）という言語を使います。SQL（時にシークエルと発音される）はリレーショナルデータベースのデータを取得・変更するための標準言語です。

データを取得するには`SELECT`コマンドを使います。基本的に、表示したい列を**SELECT**で選び、それらが含まれるテーブルを**FROM**で指定します。都市の名前だけを表示したい場合、次のようにします：

```sql
SELECT city
FROM cities;

-- Output:
-- Tokyo
-- Atlanta
-- Auckland
```

`SELECT`は列をリストし、`FROM`はテーブルをリストします。

> [!NOTE] 
> SQLの構文は大文字小文字を区別しません。つまり`select`も`SELECT`も同じ意味です。ただし、使用するデータベースの種類によっては列名やテーブル名は大文字小文字を区別する場合があります。そのため、プログラミングではすべてを大文字小文字を区別するものとして扱うのがベストプラクティスです。SQLクエリを書く際はキーワードをすべて大文字にするのが一般的です。

上記のクエリはすべての都市を表示します。ニュージーランドの都市だけを表示したい場合、フィルターが必要です。SQLのキーワードは`WHERE`で、「何かが真である場所」という意味です。

```sql
SELECT city
FROM cities
WHERE country = 'New Zealand';

-- Output:
-- Auckland
```

## データの結合

これまでは単一のテーブルからデータを取得してきました。今度は**cities**と**rainfall**の両方のデータを結合して取得したいです。これは*結合*（ジョイン）によって行います。2つのテーブルの間に継ぎ目を作り、それぞれのテーブルの列の値を一致させます。

例では、**rainfall**の**city_id**列と**cities**の**city_id**列を一致させます。これにより降雨量の値が対応する都市と結びつきます。行が他のテーブルのどの行とも一致しない場合は表示されない*内部結合*（inner join）を行います。今回の場合、すべての都市に降雨量があるので全て表示されます。

2019年のすべての都市の降雨量を取得しましょう。

段階的に行います。最初のステップは、結合する列を示してデータを結合することです。先ほど強調した**city_id**です。

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
```

結合したい2つの列を強調し、**city_id**でテーブルを結合することを示しました。次に`WHERE`文を追加して2019年だけをフィルターします。

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

## まとめ

リレーショナルデータベースは情報を複数のテーブルに分割し、それを表示や分析のために再結合することを中心にしています。これにより計算やデータ操作に高い柔軟性が得られます。リレーショナルデータベースの基本概念と2つのテーブル間の結合方法を見てきました。

## 🚀 チャレンジ

インターネット上には多くのリレーショナルデータベースがあります。ここで学んだスキルを使ってデータを探索してみましょう。

## 講義後クイズ

## [講義後クイズ](https://ff-quizzes.netlify.app/en/ds/quiz/9)

## 復習と自主学習

[Microsoft Learn](https://docs.microsoft.com/learn?WT.mc_id=academic-77958-bethanycheum)にはSQLやリレーショナルデータベースの概念をさらに学べるリソースがいくつかあります。

- [リレーショナルデータの概念を説明する](https://docs.microsoft.com//learn/modules/describe-concepts-of-relational-data?WT.mc_id=academic-77958-bethanycheum)
- [Transact-SQLでのクエリの開始](https://docs.microsoft.com//learn/paths/get-started-querying-with-transact-sql?WT.mc_id=academic-77958-bethanycheum)（Transact-SQLはSQLの一種です）
- [Microsoft LearnのSQLコンテンツ](https://docs.microsoft.com/learn/browse/?products=azure-sql-database%2Csql-server&expanded=azure&WT.mc_id=academic-77958-bethanycheum)

## 課題

[空港データの表示](assignment.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：  
本書類はAI翻訳サービス「Co-op Translator」（https://github.com/Azure/co-op-translator）を使用して翻訳されました。正確性の向上に努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語による文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や誤訳についても、当方は一切の責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->