<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ea67c0c40808fd723594de6896c37ccf",
  "translation_date": "2025-08-25T18:14:49+00:00",
  "source_file": "3-Data-Visualization/R/10-visualization-distributions/README.md",
  "language_code": "ja"
}
-->
# 分布の可視化

|![ スケッチノート by [(@sketchthedocs)](https://sketchthedocs.dev) ](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/sketchnotes/10-Visualizing-Distributions.png)|
|:---:|
| 分布の可視化 - _スケッチノート by [@nitya](https://twitter.com/nitya)_ |

前回のレッスンでは、ミネソタ州の鳥に関するデータセットについていくつか興味深い事実を学びました。外れ値を可視化することで誤ったデータを見つけ、鳥のカテゴリ間の最大長の違いを確認しました。

## [講義前のクイズ](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/18)
## 鳥のデータセットを探索する

データを掘り下げるもう一つの方法は、その分布、つまりデータが軸に沿ってどのように整理されているかを見ることです。例えば、このデータセットでミネソタ州の鳥の最大翼幅や最大体重の一般的な分布について知りたいと思うかもしれません。

このデータセットの分布に関するいくつかの事実を発見してみましょう。Rコンソールで`ggplot2`とデータベースをインポートします。前回のトピックと同様に、データベースから外れ値を削除してください。

```r
library(ggplot2)

birds <- read.csv("../../data/birds.csv",fileEncoding="UTF-8-BOM")

birds_filtered <- subset(birds, MaxWingspan < 500)
head(birds_filtered)
```
|      | 名前                         | 学名                   | カテゴリ              | 目           | 科       | 属          | 保全状況             | 最小長さ | 最大長さ | 最小体重     | 最大体重     | 最小翼幅     | 最大翼幅     |
| ---: | :--------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :----------------- | --------: | --------: | ----------: | ----------: | ----------: | ----------: |
|    0 | クロハラホシハジロ           | Dendrocygna autumnalis | カモ/ガン/水鳥         | カモ目        | カモ科    | Dendrocygna | LC                 |        47 |        56 |         652 |        1020 |          76 |          94 |
|    1 | フルボホシハジロ             | Dendrocygna bicolor    | カモ/ガン/水鳥         | カモ目        | カモ科    | Dendrocygna | LC                 |        45 |        53 |         712 |        1050 |          85 |          93 |
|    2 | ハクガン                     | Anser caerulescens     | カモ/ガン/水鳥         | カモ目        | カモ科    | Anser       | LC                 |        64 |        79 |        2050 |        4050 |         135 |         165 |
|    3 | ロスガン                     | Anser rossii           | カモ/ガン/水鳥         | カモ目        | カモ科    | Anser       | LC                 |      57.3 |        64 |        1066 |        1567 |         113 |         116 |
|    4 | マガン                       | Anser albifrons        | カモ/ガン/水鳥         | カモ目        | カモ科    | Anser       | LC                 |        64 |        81 |        1930 |        3310 |         130 |         165 |

一般的に、前回のレッスンで行ったように散布図を使用することで、データがどのように分布しているかをすばやく確認できます。

```r
ggplot(data=birds_filtered, aes(x=Order, y=MaxLength,group=1)) +
  geom_point() +
  ggtitle("Max Length per order") + coord_flip()
```
![目ごとの最大長](../../../../../translated_images/ja/max-length-per-order.e5b283d952c78c12b091307c5d3cf67132dad6fefe80a073353b9dc5c2bd3eb8.png)

これにより、鳥の目ごとの体長の一般的な分布が概観できますが、真の分布を表示する最適な方法ではありません。このタスクは通常、ヒストグラムを作成することで行われます。
## ヒストグラムの操作

`ggplot2`はヒストグラムを使用してデータ分布を視覚化する非常に優れた方法を提供します。このタイプのチャートは棒グラフのようなもので、バーの上昇と下降を通じて分布を見ることができます。ヒストグラムを作成するには数値データが必要です。ヒストグラムを作成するには、チャートの種類を「hist」と定義します。このチャートは、データセット全体の範囲における`MaxBodyMass`の分布を示します。データの配列を小さなビンに分割することで、データ値の分布を表示できます。

```r
ggplot(data = birds_filtered, aes(x = MaxBodyMass)) + 
  geom_histogram(bins=10)+ylab('Frequency')
```
![データセット全体の分布](../../../../../translated_images/ja/distribution-over-the-entire-dataset.d22afd3fa96be854e4c82213fedec9e3703cba753d07fad4606aadf58cf7e78e.png)

ご覧のように、このデータセットに含まれる400以上の鳥のほとんどは、最大体重が2000未満の範囲に収まっています。`bins`パラメータを30などのより高い数値に変更して、データについてさらに洞察を得てみましょう。

```r
ggplot(data = birds_filtered, aes(x = MaxBodyMass)) + geom_histogram(bins=30)+ylab('Frequency')
```

![30ビンの分布](../../../../../translated_images/ja/distribution-30bins.6a3921ea7a421bf71f06bf5231009e43d1146f1b8da8dc254e99b5779a4983e5.png)

このチャートは、より細かい粒度で分布を示しています。左に偏りすぎないチャートを作成するには、特定の範囲内のデータのみを選択するようにします。

体重が60未満の鳥のみをフィルタリングし、30の`bins`を表示します。

```r
birds_filtered_1 <- subset(birds_filtered, MaxBodyMass > 1 & MaxBodyMass < 60)
ggplot(data = birds_filtered_1, aes(x = MaxBodyMass)) + 
  geom_histogram(bins=30)+ylab('Frequency')
```

![フィルタリングされたヒストグラム](../../../../../translated_images/ja/filtered-histogram.6bf5d2bfd82533220e1bd4bc4f7d14308f43746ed66721d9ec8f460732be6674.png)

✅ 他のフィルタやデータポイントを試してみてください。データの完全な分布を確認するには、`['MaxBodyMass']`フィルタを削除してラベル付き分布を表示してください。

ヒストグラムには、色やラベルの強化機能もあります。

2Dヒストグラムを作成して、2つの分布間の関係を比較してみましょう。`MaxBodyMass`と`MaxLength`を比較します。`ggplot2`には、明るい色を使用して収束を表示する組み込みの方法があります。

```r
ggplot(data=birds_filtered_1, aes(x=MaxBodyMass, y=MaxLength) ) +
  geom_bin2d() +scale_fill_continuous(type = "viridis")
```
これら2つの要素間には予想される軸に沿った相関があり、特に強い収束点が1つあります。

![2Dプロット](../../../../../translated_images/ja/2d-plot.c504786f439bd7ebceebf2465c70ca3b124103e06c7ff7214bf24e26f7aec21e.png)

ヒストグラムは数値データに対してデフォルトでうまく機能します。テキストデータに基づいて分布を確認する必要がある場合はどうしますか？
## テキストデータを使用したデータセットの分布を探索する

このデータセットには、鳥のカテゴリ、属、種、科、および保全状況に関する良い情報も含まれています。この保全情報を掘り下げてみましょう。鳥の保全状況に応じた分布はどうなっていますか？

> ✅ データセットには、保全状況を説明するいくつかの略語が使用されています。これらの略語は、種の状況をカタログ化する組織である[IUCNレッドリストカテゴリ](https://www.iucnredlist.org/)から来ています。
> 
> - CR: 絶滅危惧種
> - EN: 絶滅危惧種（危機）
> - EX: 絶滅
> - LC: 軽度懸念
> - NT: 準絶滅危惧種
> - VU: 危急種

これらはテキストベースの値なので、ヒストグラムを作成するには変換が必要です。`filteredBirds`データフレームを使用して、その保全状況と最小翼幅を表示してください。何が見えますか？

```r
birds_filtered_1$ConservationStatus[birds_filtered_1$ConservationStatus == 'EX'] <- 'x1' 
birds_filtered_1$ConservationStatus[birds_filtered_1$ConservationStatus == 'CR'] <- 'x2'
birds_filtered_1$ConservationStatus[birds_filtered_1$ConservationStatus == 'EN'] <- 'x3'
birds_filtered_1$ConservationStatus[birds_filtered_1$ConservationStatus == 'NT'] <- 'x4'
birds_filtered_1$ConservationStatus[birds_filtered_1$ConservationStatus == 'VU'] <- 'x5'
birds_filtered_1$ConservationStatus[birds_filtered_1$ConservationStatus == 'LC'] <- 'x6'

ggplot(data=birds_filtered_1, aes(x = MinWingspan, fill = ConservationStatus)) +
  geom_histogram(position = "identity", alpha = 0.4, bins = 20) +
  scale_fill_manual(name="Conservation Status",values=c("red","green","blue","pink"),labels=c("Endangered","Near Threathened","Vulnerable","Least Concern"))
```

![翼幅と保全状況の集計](../../../../../translated_images/ja/wingspan-conservation-collation.4024e9aa6910866aa82f0c6cb6a6b4b925bd10079e6b0ef8f92eefa5a6792f76.png)

最小翼幅と保全状況の間に良い相関関係は見られないようです。この方法を使用してデータセットの他の要素をテストしてください。異なるフィルタを試すこともできます。何か相関関係が見つかりますか？

## 密度プロット

これまで見てきたヒストグラムは「段階的」であり、滑らかな弧を描いていないことに気付いたかもしれません。より滑らかな密度チャートを表示するには、密度プロットを試してみてください。

では、密度プロットを操作してみましょう！

```r
ggplot(data = birds_filtered_1, aes(x = MinWingspan)) + 
  geom_density()
```
![密度プロット](../../../../../translated_images/ja/density-plot.675ccf865b76c690487fb7f69420a8444a3515f03bad5482886232d4330f5c85.png)

このプロットは、最小翼幅データに関する以前のプロットを反映していますが、少し滑らかになっています。2番目に作成したギザギザの`MaxBodyMass`ラインを再現することで、この方法を使用して非常に滑らかにすることができます。

```r
ggplot(data = birds_filtered_1, aes(x = MaxBodyMass)) + 
  geom_density()
```
![体重密度](../../../../../translated_images/ja/bodymass-smooth.d31ce526d82b0a1f19a073815dea28ecfbe58145ec5337e4ef7e8cdac81120b3.png)

滑らかすぎない線を作成したい場合は、`adjust`パラメータを編集してください。

```r
ggplot(data = birds_filtered_1, aes(x = MaxBodyMass)) + 
  geom_density(adjust = 1/5)
```
![滑らかさが少ない体重](../../../../../translated_images/ja/less-smooth-bodymass.10f4db8b683cc17d17b2d33f22405413142004467a1493d416608dafecfdee23.png)

✅ このタイプのプロットで利用可能なパラメータについて調べて、実験してみてください！

このタイプのチャートは、非常に説明的な視覚化を提供します。例えば、数行のコードで鳥の目ごとの最大体重密度を表示できます。

```r
ggplot(data=birds_filtered_1,aes(x = MaxBodyMass, fill = Order)) +
  geom_density(alpha=0.5)
```
![目ごとの体重](../../../../../translated_images/ja/bodymass-per-order.9d2b065dd931b928c839d8cdbee63067ab1ae52218a1b90717f4bc744354f485.png)

## 🚀 チャレンジ

ヒストグラムは、基本的な散布図、棒グラフ、折れ線グラフよりも洗練されたタイプのチャートです。インターネットでヒストグラムの良い使用例を探してみてください。それらはどのように使用されているか、何を示しているか、どの分野や調査領域で使用される傾向があるかを調べてみましょう。

## [講義後のクイズ](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/19)

## 復習と自己学習

このレッスンでは、`ggplot2`を使用して、より洗練されたチャートを表示する作業を開始しました。`geom_density_2d()`について調査し、「1次元または複数次元の連続確率密度曲線」を理解してください。[ドキュメント](https://ggplot2.tidyverse.org/reference/geom_density_2d.html)を読み、どのように機能するかを理解してください。

## 課題

[スキルを活用する](assignment.md)

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知ください。元の言語で記載された文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解釈について、当方は一切の責任を負いません。