<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ea67c0c40808fd723594de6896c37ccf",
  "translation_date": "2025-08-24T13:46:05+00:00",
  "source_file": "3-Data-Visualization/R/10-visualization-distributions/README.md",
  "language_code": "ja"
}
-->
# 分布の可視化

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/sketchnotes/10-Visualizing-Distributions.png)|
|:---:|
| 分布の可視化 - _スケッチノート by [@nitya](https://twitter.com/nitya)_ |

前のレッスンでは、ミネソタ州の鳥に関するデータセットについていくつか興味深い事実を学びました。外れ値を可視化することで誤ったデータを見つけ、鳥のカテゴリごとの最大長の違いを確認しました。

## [講義前クイズ](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/18)
## 鳥のデータセットを探る

データを掘り下げるもう一つの方法は、その分布、つまりデータが軸に沿ってどのように整理されているかを見ることです。たとえば、このデータセットでミネソタ州の鳥の最大翼幅や最大体重の一般的な分布について知りたいと思うかもしれません。

このデータセットの分布についていくつかの事実を発見してみましょう。Rコンソールで`ggplot2`とデータベースをインポートします。前のトピックと同様に、データベースから外れ値を削除します。

```r
library(ggplot2)

birds <- read.csv("../../data/birds.csv",fileEncoding="UTF-8-BOM")

birds_filtered <- subset(birds, MaxWingspan < 500)
head(birds_filtered)
```
|      | 名前                          | 学名                   | カテゴリ               | 目           | 科       | 属          | 保全状況         | 最小長さ | 最大長さ | 最小体重   | 最大体重   | 最小翼幅   | 最大翼幅   |
| ---: | :--------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :----------------- | --------: | --------: | ----------: | ----------: | ----------: | ----------: |
|    0 | クロハラツクシガモ            | Dendrocygna autumnalis | カモ/ガン/水鳥         | カモ目       | カモ科   | ツクシガモ属 | LC                 |        47 |        56 |         652 |        1020 |          76 |          94 |
|    1 | アカツクシガモ                | Dendrocygna bicolor    | カモ/ガン/水鳥         | カモ目       | カモ科   | ツクシガモ属 | LC                 |        45 |        53 |         712 |        1050 |          85 |          93 |
|    2 | ハクガン                      | Anser caerulescens     | カモ/ガン/水鳥         | カモ目       | カモ科   | ガン属       | LC                 |        64 |        79 |        2050 |        4050 |         135 |         165 |
|    3 | ロスガン                      | Anser rossii           | カモ/ガン/水鳥         | カモ目       | カモ科   | ガン属       | LC                 |      57.3 |        64 |        1066 |        1567 |         113 |         116 |
|    4 | マガン                        | Anser albifrons        | カモ/ガン/水鳥         | カモ目       | カモ科   | ガン属       | LC                 |        64 |        81 |        1930 |        3310 |         130 |         165 |

一般的に、前のレッスンで行ったように散布図を使用することで、データがどのように分布しているかをすばやく確認できます。

```r
ggplot(data=birds_filtered, aes(x=Order, y=MaxLength,group=1)) +
  geom_point() +
  ggtitle("Max Length per order") + coord_flip()
```
![目ごとの最大長](../../../../../3-Data-Visualization/R/10-visualization-distributions/images/max-length-per-order.png)

これにより、鳥の目ごとの体長の一般的な分布が概観できますが、真の分布を表示するには最適ではありません。このタスクは通常、ヒストグラムを作成することで行われます。

## ヒストグラムの操作

`ggplot2`は、ヒストグラムを使用してデータ分布を視覚化する優れた方法を提供します。このタイプのチャートは、棒グラフのようなもので、棒の上昇と下降を通じて分布を見ることができます。ヒストグラムを作成するには、数値データが必要です。ヒストグラムを作成するには、種類を「hist」と定義してチャートをプロットします。このチャートは、データセット全体の数値データ範囲における`MaxBodyMass`の分布を示します。データの配列を小さなビンに分割することで、データ値の分布を表示できます。

```r
ggplot(data = birds_filtered, aes(x = MaxBodyMass)) + 
  geom_histogram(bins=10)+ylab('Frequency')
```
![データセット全体の分布](../../../../../3-Data-Visualization/R/10-visualization-distributions/images/distribution-over-the-entire-dataset.png)

ご覧のとおり、このデータセットに含まれる400以上の鳥のほとんどは、最大体重が2000未満の範囲に収まっています。`bins`パラメータを30のような高い数値に変更して、データについてさらに洞察を得てみましょう。

```r
ggplot(data = birds_filtered, aes(x = MaxBodyMass)) + geom_histogram(bins=30)+ylab('Frequency')
```

![30ビンの分布](../../../../../3-Data-Visualization/R/10-visualization-distributions/images/distribution-30bins.png)

このチャートは、より詳細な分布を示しています。左に偏りすぎないチャートを作成するには、特定の範囲内のデータのみを選択するようにします。

体重が60未満の鳥のみを取得し、30の`bins`を表示します。

```r
birds_filtered_1 <- subset(birds_filtered, MaxBodyMass > 1 & MaxBodyMass < 60)
ggplot(data = birds_filtered_1, aes(x = MaxBodyMass)) + 
  geom_histogram(bins=30)+ylab('Frequency')
```

![フィルタリングされたヒストグラム](../../../../../3-Data-Visualization/R/10-visualization-distributions/images/filtered-histogram.png)

✅ 他のフィルタやデータポイントを試してみましょう。データの完全な分布を確認するには、`['MaxBodyMass']`フィルタを削除してラベル付き分布を表示します。

ヒストグラムには、色やラベルの強化機能もあります。

2Dヒストグラムを作成して、2つの分布間の関係を比較します。たとえば、`MaxBodyMass`と`MaxLength`を比較します。`ggplot2`は、明るい色を使用して収束を示す組み込みの方法を提供します。

```r
ggplot(data=birds_filtered_1, aes(x=MaxBodyMass, y=MaxLength) ) +
  geom_bin2d() +scale_fill_continuous(type = "viridis")
```
予想される軸に沿ってこれら2つの要素間に予想される相関があり、特に強い収束点が1つあります。

![2Dプロット](../../../../../3-Data-Visualization/R/10-visualization-distributions/images/2d-plot.png)

ヒストグラムは、数値データに対してデフォルトでうまく機能します。では、テキストデータに基づいて分布を確認する必要がある場合はどうでしょうか？

## テキストデータを使用したデータセットの分布を探る

このデータセットには、鳥のカテゴリ、属、種、科、および保全状況に関する良い情報も含まれています。この保全情報を掘り下げてみましょう。鳥の保全状況に基づく分布はどうなっていますか？

> ✅ このデータセットでは、保全状況を説明するためにいくつかの略語が使用されています。これらの略語は、種の状況をカタログ化する組織である[IUCNレッドリストカテゴリ](https://www.iucnredlist.org/)に由来します。
> 
> - CR: 絶滅危惧種（極度）
> - EN: 絶滅危惧種
> - EX: 絶滅
> - LC: 軽度懸念
> - NT: 近危急種
> - VU: 危急種

これらはテキストベースの値なので、ヒストグラムを作成するには変換が必要です。`filteredBirds`データフレームを使用して、保全状況と最小翼幅を表示します。何が見えますか？

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

![翼幅と保全状況の比較](../../../../../3-Data-Visualization/R/10-visualization-distributions/images/wingspan-conservation-collation.png)

最小翼幅と保全状況の間に良い相関関係は見られないようです。この方法を使用してデータセットの他の要素をテストしてください。異なるフィルタも試してみましょう。何か相関関係が見つかりますか？

## 密度プロット

これまで見てきたヒストグラムは「段階的」であり、滑らかにアークを描いていないことに気付いたかもしれません。より滑らかな密度チャートを表示するには、密度プロットを試してみてください。

では、密度プロットを操作してみましょう！

```r
ggplot(data = birds_filtered_1, aes(x = MinWingspan)) + 
  geom_density()
```
![密度プロット](../../../../../3-Data-Visualization/R/10-visualization-distributions/images/density-plot.png)

このプロットは、最小翼幅データに関して以前のものを反映していますが、少し滑らかになっています。2番目に作成したギザギザの`MaxBodyMass`ラインを再現することで、この方法を使用して非常に滑らかにすることができます。

```r
ggplot(data = birds_filtered_1, aes(x = MaxBodyMass)) + 
  geom_density()
```
![体重密度](../../../../../3-Data-Visualization/R/10-visualization-distributions/images/bodymass-smooth.png)

滑らかすぎないラインを作成したい場合は、`adjust`パラメータを編集します。

```r
ggplot(data = birds_filtered_1, aes(x = MaxBodyMass)) + 
  geom_density(adjust = 1/5)
```
![滑らかさを抑えた体重密度](../../../../../3-Data-Visualization/R/10-visualization-distributions/images/less-smooth-bodymass.png)

✅ このタイプのプロットで利用可能なパラメータについて調べて、実験してみてください！

このタイプのチャートは、美しく説明的な視覚化を提供します。たとえば、数行のコードで鳥の目ごとの最大体重密度を表示できます。

```r
ggplot(data=birds_filtered_1,aes(x = MaxBodyMass, fill = Order)) +
  geom_density(alpha=0.5)
```
![目ごとの体重密度](../../../../../3-Data-Visualization/R/10-visualization-distributions/images/bodymass-per-order.png)

## 🚀 チャレンジ

ヒストグラムは、基本的な散布図、棒グラフ、折れ線グラフよりも洗練されたタイプのチャートです。インターネットでヒストグラムの良い使用例を探してみましょう。それらはどのように使用され、何を示し、どの分野や研究領域で使用される傾向がありますか？

## [講義後クイズ](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/19)

## 復習と自己学習

このレッスンでは、`ggplot2`を使用して、より洗練されたチャートを作成し始めました。`geom_density_2d()`（「1次元またはそれ以上の連続確率密度曲線」）について調べてみてください。[ドキュメント](https://ggplot2.tidyverse.org/reference/geom_density_2d.html)を読んで、その仕組みを理解してください。

## 課題

[スキルを応用する](assignment.md)

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知ください。元の言語で記載された文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解釈について、当方は責任を負いません。