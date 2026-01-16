<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "22acf28f518a4769ea14fa42f4734b9f",
  "translation_date": "2025-08-25T18:24:31+00:00",
  "source_file": "3-Data-Visualization/R/09-visualization-quantities/README.md",
  "language_code": "ja"
}
-->
# 量を視覚化する
|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/sketchnotes/09-Visualizing-Quantities.png)|
|:---:|
| 量を視覚化する - _スケッチノート by [@nitya](https://twitter.com/nitya)_ |

このレッスンでは、Rのさまざまなパッケージライブラリを使用して、量の概念に基づいた興味深い視覚化を作成する方法を学びます。ミネソタ州の鳥に関するクリーンなデータセットを使用して、地元の野生生物について多くの興味深い事実を学ぶことができます。

## [講義前のクイズ](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/16)

## ggplot2で翼幅を観察する
さまざまな種類のシンプルで洗練されたプロットやチャートを作成するのに優れたライブラリが[ggplot2](https://cran.r-project.org/web/packages/ggplot2/index.html)です。一般的に、これらのライブラリを使用してデータをプロットするプロセスは、ターゲットにしたいデータフレームの部分を特定し、必要に応じてそのデータを変換し、x軸とy軸の値を割り当て、表示するプロットの種類を決定し、プロットを表示するという手順を含みます。

`ggplot2`は、The Grammar of Graphics（グラフィックスの文法）に基づいてグラフィックを宣言的に作成するためのシステムです。[The Grammar of Graphics](https://en.wikipedia.org/wiki/Ggplot2)は、スケールやレイヤーなどの意味的なコンポーネントにグラフを分解するデータ視覚化の一般的なスキームです。言い換えれば、少ないコードで単変量または多変量データのプロットやグラフを簡単に作成できるため、`ggplot2`はRで最も人気のある視覚化パッケージです。ユーザーは、`ggplot2`に変数を美的要素にマッピングする方法、使用するグラフィカルプリミティブを指示し、残りは`ggplot2`が処理します。

> ✅ プロット = データ + 美的要素 + ジオメトリ
> - データ: データセットを指します
> - 美的要素: 調査対象の変数（x軸とy軸の変数）を示します
> - ジオメトリ: プロットの種類（折れ線グラフ、棒グラフなど）を指します

データとプロットを通じて伝えたいストーリーに応じて、最適なジオメトリ（プロットの種類）を選択してください。

> - 傾向を分析するには: 折れ線グラフ、縦棒グラフ
> - 値を比較するには: 棒グラフ、縦棒グラフ、円グラフ、散布図
> - 全体に対する部分の関係を示すには: 円グラフ
> - データの分布を示すには: 散布図、棒グラフ
> - 値間の関係を示すには: 折れ線グラフ、散布図、バブルチャート

✅ この説明的な[チートシート](https://nyu-cdsc.github.io/learningr/assets/data-visualization-2.1.pdf)もチェックしてみてください。

## 鳥の翼幅値に関する折れ線グラフを作成する

Rコンソールを開き、データセットをインポートします。
> 注: データセットはこのリポジトリのルートにある`/data`フォルダに保存されています。

データセットをインポートし、データの先頭（最初の5行）を観察してみましょう。

```r
birds <- read.csv("../../data/birds.csv",fileEncoding="UTF-8-BOM")
head(birds)
```
データの先頭には、テキストと数値が混在しています。

|      | 名前                          | 学名                   | カテゴリ              | 目           | 科       | 属          | 保全状況         | 最小長さ | 最大長さ | 最小体重   | 最大体重   | 最小翼幅   | 最大翼幅   |
| ---: | :--------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :---------------- | --------: | --------: | ----------: | ----------: | ----------: | ----------: |
|    0 | クロハラアカガモ             | Dendrocygna autumnalis | カモ/ガン/水鳥        | カモ目       | カモ科   | Dendrocygna | LC                 |        47 |        56 |         652 |        1020 |          76 |          94 |
|    1 | フルボアカガモ               | Dendrocygna bicolor    | カモ/ガン/水鳥        | カモ目       | カモ科   | Dendrocygna | LC                 |        45 |        53 |         712 |        1050 |          85 |          93 |
|    2 | ハクガン                     | Anser caerulescens     | カモ/ガン/水鳥        | カモ目       | カモ科   | Anser       | LC                 |        64 |        79 |        2050 |        4050 |         135 |         165 |
|    3 | ロスガン                     | Anser rossii           | カモ/ガン/水鳥        | カモ目       | カモ科   | Anser       | LC                 |      57.3 |        64 |        1066 |        1567 |         113 |         116 |
|    4 | マガン                       | Anser albifrons        | カモ/ガン/水鳥        | カモ目       | カモ科   | Anser       | LC                 |        64 |        81 |        1930 |        3310 |         130 |         165 |

これらの興味深い鳥の最大翼幅を視覚化するために、基本的な折れ線グラフをプロットしてみましょう。

```r
install.packages("ggplot2")
library("ggplot2")
ggplot(data=birds, aes(x=Name, y=MaxWingspan,group=1)) +
  geom_line() 
```
ここでは、`ggplot2`パッケージをインストールし、`library("ggplot2")`コマンドを使用してワークスペースにインポートします。`ggplot`でプロットを作成するには、`ggplot()`関数を使用し、データセット、x軸とy軸の変数を属性として指定します。この場合、折れ線グラフをプロットするために`geom_line()`関数を使用します。

![MaxWingspan-lineplot](../../../../../translated_images/ja/MaxWingspan-lineplot.b12169f99d26fdd263f291008dfd73c18a4ba8f3d32b1fda3d74af51a0a28616.png)

何がすぐに目に留まりますか？少なくとも1つの外れ値があるようです。これはかなりの翼幅ですね！2000センチメートル以上の翼幅は20メートル以上に相当します。ミネソタ州にプテラノドンがいるのでしょうか？調査してみましょう。

Excelで外れ値を簡単にソートすることもできますが、プロット内で作業を続けて視覚化プロセスを進めましょう。

x軸にラベルを追加して、どの鳥が対象であるかを表示します。

```r
ggplot(data=birds, aes(x=Name, y=MaxWingspan,group=1)) +
  geom_line() +
  theme(axis.text.x = element_text(angle = 45, hjust=1))+
  xlab("Birds") +
  ylab("Wingspan (CM)") +
  ggtitle("Max Wingspan in Centimeters")
```
`theme`で角度を指定し、`xlab()`と`ylab()`でx軸とy軸のラベルを指定します。`ggtitle()`でグラフ/プロットに名前を付けます。

![MaxWingspan-lineplot-improved](../../../../../translated_images/ja/MaxWingspan-lineplot-improved.04b73b4d5a59552a6bc7590678899718e1f065abe9eada9ebb4148939b622fd4.png)

ラベルの回転を45度に設定しても、読み取るには多すぎます。別の戦略を試してみましょう。外れ値のみをラベル付けし、チャート内にラベルを設定します。散布図を使用してラベル付けのスペースを確保します。

```r
ggplot(data=birds, aes(x=Name, y=MaxWingspan,group=1)) +
  geom_point() +
  geom_text(aes(label=ifelse(MaxWingspan>500,as.character(Name),'')),hjust=0,vjust=0) + 
  theme(axis.title.x=element_blank(), axis.text.x=element_blank(), axis.ticks.x=element_blank())
  ylab("Wingspan (CM)") +
  ggtitle("Max Wingspan in Centimeters") + 
```
ここでは、`geom_point()`関数を使用して散布点をプロットしました。これにより、`MaxWingspan > 500`の鳥にラベルを追加し、プロットを整理するためにx軸のラベルを非表示にしました。

何がわかりますか？

![MaxWingspan-scatterplot](../../../../../translated_images/ja/MaxWingspan-scatterplot.60dc9e0e19d32700283558f253841fdab5104abb62bc96f7d97f9c0ee857fa8b.png)

## データをフィルタリングする

ハクトウワシとプレーリーハヤブサは非常に大きな鳥である可能性がありますが、最大翼幅に余分な0が追加されているようです。翼幅25メートルのハクトウワシに出会うことはまずないでしょうが、もしそうならぜひ教えてください！これら2つの外れ値を除外した新しいデータフレームを作成しましょう。

```r
birds_filtered <- subset(birds, MaxWingspan < 500)

ggplot(data=birds_filtered, aes(x=Name, y=MaxWingspan,group=1)) +
  geom_point() +
  ylab("Wingspan (CM)") +
  xlab("Birds") +
  ggtitle("Max Wingspan in Centimeters") + 
  geom_text(aes(label=ifelse(MaxWingspan>500,as.character(Name),'')),hjust=0,vjust=0) +
  theme(axis.text.x=element_blank(), axis.ticks.x=element_blank())
```
新しいデータフレーム`birds_filtered`を作成し、散布図をプロットしました。外れ値を除外することで、データがより一貫性があり理解しやすくなりました。

![MaxWingspan-scatterplot-improved](../../../../../translated_images/ja/MaxWingspan-scatterplot-improved.7d0af81658c65f3e75b8fedeb2335399e31108257e48db15d875ece608272051.png)

翼幅に関して少なくともクリーンなデータセットが得られたので、これらの鳥についてさらに発見してみましょう。

折れ線グラフや散布図はデータ値やその分布に関する情報を表示できますが、このデータセットに内在する値について考えてみましょう。このデータセットに基づいて以下のような量に関する質問に答える視覚化を作成できます。

> 鳥のカテゴリはいくつあり、それぞれの数はどれくらいか？
> 絶滅、絶滅危惧種、希少種、または一般的な鳥はどれくらいいるか？
> リンネの分類学における属や目の数はどれくらいか？

## 棒グラフを探る

棒グラフはデータのグループを表示する必要がある場合に実用的です。このデータセットに存在する鳥のカテゴリを調べ、どのカテゴリが最も一般的かを確認してみましょう。

フィルタリングされたデータに基づいて棒グラフを作成します。

```r
install.packages("dplyr")
install.packages("tidyverse")

library(lubridate)
library(scales)
library(dplyr)
library(ggplot2)
library(tidyverse)

birds_filtered %>% group_by(Category) %>%
  summarise(n=n(),
  MinLength = mean(MinLength),
  MaxLength = mean(MaxLength),
  MinBodyMass = mean(MinBodyMass),
  MaxBodyMass = mean(MaxBodyMass),
  MinWingspan=mean(MinWingspan),
  MaxWingspan=mean(MaxWingspan)) %>% 
  gather("key", "value", - c(Category, n)) %>%
  ggplot(aes(x = Category, y = value, group = key, fill = key)) +
  geom_bar(stat = "identity") +
  scale_fill_manual(values = c("#D62728", "#FF7F0E", "#8C564B","#2CA02C", "#1F77B4", "#9467BD")) +                   
  xlab("Category")+ggtitle("Birds of Minnesota")

```
以下のスニペットでは、データを操作してグループ化し、積み上げ棒グラフをプロットするために[dplyr](https://www.rdocumentation.org/packages/dplyr/versions/0.7.8)と[lubridate](https://www.rdocumentation.org/packages/lubridate/versions/1.8.0)パッケージをインストールします。まず、鳥の`Category`でデータをグループ化し、`MinLength`、`MaxLength`、`MinBodyMass`、`MaxBodyMass`、`MinWingspan`、`MaxWingspan`列を要約します。その後、`ggplot2`パッケージを使用して棒グラフをプロットし、異なるカテゴリの色とラベルを指定します。

![Stacked bar chart](../../../../../translated_images/ja/stacked-bar-chart.0c92264e89da7b391a7490224d1e7059a020e8b74dcd354414aeac78871c02f1.png)

この棒グラフは、グループ化されていないデータが多すぎるため、読み取りにくいです。プロットしたいデータのみを選択する必要があります。鳥のカテゴリに基づいて長さを調べてみましょう。

データをフィルタリングして、鳥のカテゴリのみを含めます。

カテゴリが多いため、このチャートを縦に表示し、その高さを調整してすべてのデータを表示できるようにします。

```r
birds_count<-dplyr::count(birds_filtered, Category, sort = TRUE)
birds_count$Category <- factor(birds_count$Category, levels = birds_count$Category)
ggplot(birds_count,aes(Category,n))+geom_bar(stat="identity")+coord_flip()
```
まず、`Category`列のユニークな値をカウントし、それを新しいデータフレーム`birds_count`にソートします。このソートされたデータを同じレベルでファクタリングし、ソートされた方法でプロットされるようにします。その後、`ggplot2`を使用して棒グラフをプロットします。`coord_flip()`を使用して水平棒をプロットします。

![category-length](../../../../../translated_images/ja/category-length.7e34c296690e85d64f7e4d25a56077442683eca96c4f5b4eae120a64c0755636.png)

この棒グラフは、各カテゴリの鳥の数をよく示しています。一目で、この地域で最も多い鳥がカモ/ガン/水鳥カテゴリに属していることがわかります。ミネソタ州は「1万の湖の地」として知られているので、これは驚くべきことではありません！

✅ このデータセットで他のカウントを試してみてください。何か驚くことはありますか？

## データの比較

新しい軸を作成して、グループ化されたデータのさまざまな比較を試すことができます。鳥のカテゴリに基づいて鳥の最大長さを比較してみましょう。

```r
birds_grouped <- birds_filtered %>%
  group_by(Category) %>%
  summarise(
  MaxLength = max(MaxLength, na.rm = T),
  MinLength = max(MinLength, na.rm = T)
           ) %>%
  arrange(Category)
  
ggplot(birds_grouped,aes(Category,MaxLength))+geom_bar(stat="identity")+coord_flip()
```
`birds_filtered`データを`Category`でグループ化し、棒グラフをプロットします。

![comparing data](../../../../../translated_images/ja/comparingdata.f486a450d61c7ca5416f27f3f55a6a4465d00df3be5e6d33936e9b07b95e2fdd.png)

ここには驚くことはありません。ハチドリの最大長さはペリカンやガンと比較して最も短いです。データが論理的に意味をなすのは良いことです！

棒グラフをより興味深いものにするために、データを重ね合わせることができます。鳥のカテゴリに基づいて最小長さと最大長さを重ね合わせてみましょう。

```r
ggplot(data=birds_grouped, aes(x=Category)) +
  geom_bar(aes(y=MaxLength), stat="identity", position ="identity",  fill='blue') +
  geom_bar(aes(y=MinLength), stat="identity", position="identity", fill='orange')+
  coord_flip()
```
![super-imposed values](../../../../../translated_images/ja/superimposed-values.5363f0705a1da4167625a373a1064331ea3cb7a06a297297d0734fcc9b3819a0.png)

## 🚀 チャレンジ

この鳥のデータセットは、特定の生態系内のさまざまな種類の鳥に関する豊富な情報を提供します。インターネットで他の鳥に関するデータセットを探してみてください。これらの鳥に関するチャートやグラフを作成して、知らなかった事実を発見してみましょう。

## [講義後のクイズ](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/17)

## 復習と自己学習

この最初のレッスンでは、`ggplot2`を使用して量を視覚化する方法についての情報をいくつか提供しました。データセットを視覚化するための他の方法について調査してみてください。[Lattice](https://stat.ethz.ch/R-manual/R-devel/library/lattice/html/Lattice.html)や[Plotly](https://github.com/plotly/plotly.R#readme)などの他のパッケージを使用して視覚化できるデータセットを探してみてください。

## 課題
[折れ線、散布図、棒グラフ](assignment.md)

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知ください。元の言語で記載された文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤認について、当方は一切の責任を負いません。