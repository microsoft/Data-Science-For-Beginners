<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1441550a0d789796b2821e04f7f4cc94",
  "translation_date": "2025-08-24T13:30:50+00:00",
  "source_file": "3-Data-Visualization/README.md",
  "language_code": "ja"
}
-->
# ビジュアライゼーション

![ラベンダーの花にとまるミツバチ](../../../3-Data-Visualization/images/bee.jpg)
> 写真提供: <a href="https://unsplash.com/@jenna2980?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Jenna Lee</a> on <a href="https://unsplash.com/s/photos/bees-in-a-meadow?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

データの可視化は、データサイエンティストにとって最も重要なタスクの1つです。画像は千の言葉に値すると言われるように、ビジュアライゼーションはデータの中に潜む興味深い部分、例えばスパイク、外れ値、グループ化、傾向などを特定し、データが語ろうとしているストーリーを理解する助けとなります。

この5つのレッスンでは、自然から得られたデータを探求し、さまざまな手法を用いて興味深く美しいビジュアライゼーションを作成します。

| トピック番号 | トピック | リンクされたレッスン | 著者 |
| :-----------: | :--: | :-----------: | :----: |
| 1. | 数量の可視化 | <ul> <li> [Python](09-visualization-quantities/README.md)</li>  <li>[R](../../../3-Data-Visualization/R/09-visualization-quantities) </li> </ul>|<ul> <li> [Jen Looper](https://twitter.com/jenlooper)</li><li> [Vidushi Gupta](https://github.com/Vidushi-Gupta)</li> <li>[Jasleen Sondhi](https://github.com/jasleen101010)</li></ul> |
| 2. | 分布の可視化 | <ul> <li> [Python](10-visualization-distributions/README.md)</li>  <li>[R](../../../3-Data-Visualization/R/10-visualization-distributions) </li> </ul>|<ul> <li> [Jen Looper](https://twitter.com/jenlooper)</li><li> [Vidushi Gupta](https://github.com/Vidushi-Gupta)</li> <li>[Jasleen Sondhi](https://github.com/jasleen101010)</li></ul> |
| 3. | 比率の可視化 | <ul> <li> [Python](11-visualization-proportions/README.md)</li>  <li>[R](../../../3-Data-Visualization) </li> </ul>|<ul> <li> [Jen Looper](https://twitter.com/jenlooper)</li><li> [Vidushi Gupta](https://github.com/Vidushi-Gupta)</li> <li>[Jasleen Sondhi](https://github.com/jasleen101010)</li></ul> |
| 4. | 関係性の可視化 | <ul> <li> [Python](12-visualization-relationships/README.md)</li>  <li>[R](../../../3-Data-Visualization) </li> </ul>|<ul> <li> [Jen Looper](https://twitter.com/jenlooper)</li><li> [Vidushi Gupta](https://github.com/Vidushi-Gupta)</li> <li>[Jasleen Sondhi](https://github.com/jasleen101010)</li></ul> |
| 5. | 意味のあるビジュアライゼーションの作成 | <ul> <li> [Python](13-meaningful-visualizations/README.md)</li>  <li>[R](../../../3-Data-Visualization) </li> </ul>|<ul> <li> [Jen Looper](https://twitter.com/jenlooper)</li><li> [Vidushi Gupta](https://github.com/Vidushi-Gupta)</li> <li>[Jasleen Sondhi](https://github.com/jasleen101010)</li></ul> |

### クレジット

これらのビジュアライゼーションのレッスンは、[Jen Looper](https://twitter.com/jenlooper)、[Jasleen Sondhi](https://github.com/jasleen101010)、[Vidushi Gupta](https://github.com/Vidushi-Gupta) によって🌸を込めて作成されました。

🍯 アメリカのハチミツ生産に関するデータは、Jessica Li の [Kaggle](https://www.kaggle.com/jessicali9530/honey-production) プロジェクトから取得しました。この[データ](https://usda.library.cornell.edu/concern/publications/rn301137d)は、[アメリカ農務省](https://www.nass.usda.gov/About_NASS/index.php)から派生したものです。

🍄 キノコに関するデータは、Hatteras Dunton によって改訂された [Kaggle](https://www.kaggle.com/hatterasdunton/mushroom-classification-updated-dataset) から取得しました。このデータセットには、Agaricus および Lepiota 科に属する23種のひだのあるキノコに対応する仮想サンプルの説明が含まれています。データは『The Audubon Society Field Guide to North American Mushrooms (1981)』から引用され、1987年に UCI ML 27 に寄贈されました。

🦆 ミネソタ州の鳥に関するデータは、[Hannah Collins](https://www.kaggle.com/hannahcollins/minnesota-birds) によって [Wikipedia](https://en.wikipedia.org/wiki/List_of_birds_of_Minnesota) からスクレイピングされ、[Kaggle](https://www.kaggle.com/hannahcollins/minnesota-birds) に提供されました。

これらのデータセットはすべて [CC0: Creative Commons](https://creativecommons.org/publicdomain/zero/1.0/) ライセンスの下で提供されています。

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知ください。元の言語で記載された文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤認について、当方は一切の責任を負いません。