<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "47028abaaafa2bcb1079702d20569066",
  "translation_date": "2025-08-24T14:01:39+00:00",
  "source_file": "3-Data-Visualization/R/11-visualization-proportions/README.md",
  "language_code": "ja"
}
-->
# 比率の可視化

|![ [(@sketchthedocs)](https://sketchthedocs.dev) によるスケッチノート ](../../../sketchnotes/11-Visualizing-Proportions.png)|
|:---:|
|比率の可視化 - _[@nitya](https://twitter.com/nitya) によるスケッチノート_ |

このレッスンでは、自然に焦点を当てた異なるデータセットを使用して、キノコに関するデータセット内でどれだけ異なる種類の菌類が存在するかなどの比率を可視化します。Audubonから取得したデータセットを使用して、AgaricusおよびLepiota科に属する23種のひだ付きキノコの詳細を探ります。以下のような魅力的な可視化を試してみましょう：

- 円グラフ 🥧
- ドーナツグラフ 🍩
- ワッフルチャート 🧇

> 💡 Microsoft Researchによる非常に興味深いプロジェクト [Charticulator](https://charticulator.com) は、データ可視化のための無料のドラッグ＆ドロップインターフェースを提供しています。彼らのチュートリアルの1つでは、このキノコのデータセットも使用されています！データを探索しながらライブラリの使い方を学ぶことができます：[Charticulator tutorial](https://charticulator.com/tutorials/tutorial4.html)。

## [講義前のクイズ](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/20)

## キノコについて知ろう 🍄

キノコは非常に興味深い存在です。データセットをインポートして研究してみましょう：

```r
mushrooms = read.csv('../../data/mushrooms.csv')
head(mushrooms)
```
以下のような分析に適したデータがテーブルとして表示されます：

| class     | cap-shape | cap-surface | cap-color | bruises | odor    | gill-attachment | gill-spacing | gill-size | gill-color | stalk-shape | stalk-root | stalk-surface-above-ring | stalk-surface-below-ring | stalk-color-above-ring | stalk-color-below-ring | veil-type | veil-color | ring-number | ring-type | spore-print-color | population | habitat |
| --------- | --------- | ----------- | --------- | ------- | ------- | --------------- | ------------ | --------- | ---------- | ----------- | ---------- | ------------------------ | ------------------------ | ---------------------- | ---------------------- | --------- | ---------- | ----------- | --------- | ----------------- | ---------- | ------- |
| Poisonous | Convex    | Smooth      | Brown     | Bruises | Pungent | Free            | Close        | Narrow    | Black      | Enlarging   | Equal      | Smooth                   | Smooth                   | White                  | White                  | Partial   | White      | One         | Pendant   | Black             | Scattered  | Urban   |
| Edible    | Convex    | Smooth      | Yellow    | Bruises | Almond  | Free            | Close        | Broad     | Black      | Enlarging   | Club       | Smooth                   | Smooth                   | White                  | White                  | Partial   | White      | One         | Pendant   | Brown             | Numerous   | Grasses |
| Edible    | Bell      | Smooth      | White     | Bruises | Anise   | Free            | Close        | Broad     | Brown      | Enlarging   | Club       | Smooth                   | Smooth                   | White                  | White                  | Partial   | White      | One         | Pendant   | Brown             | Numerous   | Meadows |
| Poisonous | Convex    | Scaly       | White     | Bruises | Pungent | Free            | Close        | Narrow    | Brown      | Enlarging   | Equal      | Smooth                   | Smooth                   | White                  | White                  | Partial   | White      | One         | Pendant   | Black             | Scattered  | Urban 
| Edible | Convex       |Smooth       | Green     | No Bruises| None   |Free            | Crowded       | Broad     | Black      | Tapering   | Equal      |  Smooth | Smooth                    | White                 | White                  | Partial    | White     | One         | Evanescent | Brown             | Abundant | Grasses
|Edible  |  Convex      | Scaly   | Yellow         | Bruises  | Almond  | Free | Close  |   Broad   |   Brown  | Enlarging   |   Club                      | Smooth                  | Smooth    | White                 |  White                | Partial      | White    |  One  |  Pendant | Black   | Numerous | Grasses
      
すぐに気づくのは、すべてのデータがテキスト形式であることです。このデータをチャートで使用できるように変換する必要があります。実際、ほとんどのデータはオブジェクトとして表現されています：

```r
names(mushrooms)
```

出力は以下の通りです：

```output
[1] "class"                    "cap.shape"               
 [3] "cap.surface"              "cap.color"               
 [5] "bruises"                  "odor"                    
 [7] "gill.attachment"          "gill.spacing"            
 [9] "gill.size"                "gill.color"              
[11] "stalk.shape"              "stalk.root"              
[13] "stalk.surface.above.ring" "stalk.surface.below.ring"
[15] "stalk.color.above.ring"   "stalk.color.below.ring"  
[17] "veil.type"                "veil.color"              
[19] "ring.number"              "ring.type"               
[21] "spore.print.color"        "population"              
[23] "habitat"            
```
このデータを使用して、「class」列をカテゴリに変換します：

```r
library(dplyr)
grouped=mushrooms %>%
  group_by(class) %>%
  summarise(count=n())
```

次に、キノコのデータを印刷すると、毒性/食用のクラスに従ってカテゴリにグループ化されていることがわかります：
```r
View(grouped)
```

| class | count |
| --------- | --------- |
| Edible | 4208 |
| Poisonous| 3916 |

このテーブルに示された順序に従ってクラスカテゴリラベルを作成すれば、円グラフを作成できます。

## 円グラフ！

```r
pie(grouped$count,grouped$class, main="Edible?")
```
完成！この円グラフは、キノコのデータを毒性/食用の2つのクラスに基づいて比率を示しています。ラベルの順序が特に重要なので、ラベル配列の順序を必ず確認してください！

![円グラフ](../../../../../3-Data-Visualization/R/11-visualization-proportions/images/pie1-wb.png)

## ドーナツグラフ！

円グラフよりも視覚的に興味深いのがドーナツグラフです。これは中央に穴がある円グラフです。この方法を使ってデータを見てみましょう。

キノコが育つさまざまな生息地を見てみましょう：

```r
library(dplyr)
habitat=mushrooms %>%
  group_by(habitat) %>%
  summarise(count=n())
View(habitat)
```
出力は以下の通りです：
| habitat| count |
| --------- | --------- |
| Grasses    | 2148 |
| Leaves| 832 |
| Meadows    | 292 |
| Paths| 1144 |
| Urban    | 368 |
| Waste| 192 |
| Wood| 3148 |

ここではデータを生息地ごとにグループ化しています。7つの生息地がリストされているので、それらをドーナツグラフのラベルとして使用します：

```r
library(ggplot2)
library(webr)
PieDonut(habitat, aes(habitat, count=count))
```

![ドーナツグラフ](../../../../../3-Data-Visualization/R/11-visualization-proportions/images/donut-wb.png)

このコードでは、ggplot2とwebrの2つのライブラリを使用しています。webrライブラリのPieDonut関数を使用すると、簡単にドーナツグラフを作成できます！

Rでは、ggplot2ライブラリだけを使用してドーナツグラフを作成することも可能です。詳細は[こちら](https://www.r-graph-gallery.com/128-ring-or-donut-plot.html)で学び、自分で試してみてください。

データをグループ化して円グラフやドーナツグラフとして表示する方法を学んだので、他の種類のチャートも探索してみましょう。ワッフルチャートを試してみてください。これは数量を異なる方法で探索する方法です。

## ワッフルチャート！

「ワッフル」タイプのチャートは、数量を2D配列の四角形として可視化する異なる方法です。このデータセット内のキノコの傘の色の異なる数量を可視化してみましょう。そのためには、[waffle](https://cran.r-project.org/web/packages/waffle/waffle.pdf)というヘルパーライブラリをインストールし、それを使用して可視化を生成します：

```r
install.packages("waffle", repos = "https://cinc.rud.is")
```

データのセグメントを選択してグループ化します：

```r
library(dplyr)
cap_color=mushrooms %>%
  group_by(cap.color) %>%
  summarise(count=n())
View(cap_color)
```

ラベルを作成し、データをグループ化してワッフルチャートを作成します：

```r
library(waffle)
names(cap_color$count) = paste0(cap_color$cap.color)
waffle((cap_color$count/10), rows = 7, title = "Waffle Chart")+scale_fill_manual(values=c("brown", "#F0DC82", "#D2691E", "green", 
                                                                                     "pink", "purple", "red", "grey", 
                                                                                     "yellow","white"))
```

ワッフルチャートを使用すると、このキノコのデータセットの傘の色の比率が明確にわかります。興味深いことに、緑色の傘を持つキノコがたくさんあります！

![ワッフルチャート](../../../../../3-Data-Visualization/R/11-visualization-proportions/images/waffle.png)

このレッスンでは、比率を可視化する3つの方法を学びました。まず、データをカテゴリにグループ化し、次にデータを表示する最適な方法を決定します - 円グラフ、ドーナツグラフ、またはワッフルチャート。どれも魅力的で、データセットのスナップショットを瞬時に提供します。

## 🚀 チャレンジ

[Charticulator](https://charticulator.com)でこれらの魅力的なチャートを再現してみてください。

## [講義後のクイズ](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/21)

## 復習と自己学習

円グラフ、ドーナツグラフ、ワッフルチャートをいつ使用するべきかは、必ずしも明確ではありません。このトピックに関する以下の記事を読んでみてください：

https://www.beautiful.ai/blog/battle-of-the-charts-pie-chart-vs-donut-chart

https://medium.com/@hypsypops/pie-chart-vs-donut-chart-showdown-in-the-ring-5d24fd86a9ce

https://www.mit.edu/~mbarker/formula1/f1help/11-ch-c6.htm

https://medium.datadriveninvestor.com/data-visualization-done-the-right-way-with-tableau-waffle-chart-fdf2a19be402

さらに調査して、この難しい決定についての情報を見つけてください。

## 課題

[Excelで試してみる](assignment.md)

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。元の言語で記載された原文が公式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤認について、当方は一切の責任を負いません。