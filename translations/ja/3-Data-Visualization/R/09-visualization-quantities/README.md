<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "22acf28f518a4769ea14fa42f4734b9f",
  "translation_date": "2025-08-24T13:54:54+00:00",
  "source_file": "3-Data-Visualization/R/09-visualization-quantities/README.md",
  "language_code": "ja"
}
-->
# 数量の可視化
|![ [(@sketchthedocs)](https://sketchthedocs.dev) によるスケッチノート ](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/sketchnotes/09-Visualizing-Quantities.png)|
|:---:|
| 数量の可視化 - _[@nitya](https://twitter.com/nitya) によるスケッチノート_ |

このレッスンでは、Rの利用可能なパッケージライブラリを使って、数量の概念を中心に興味深い可視化を作成する方法を学びます。ミネソタ州の鳥に関するクリーンなデータセットを使用して、地元の野生生物について多くの興味深い事実を学ぶことができます。
## [講義前のクイズ](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/16)

## ggplot2で翼幅を観察する
シンプルで洗練されたさまざまな種類のプロットやチャートを作成するための優れたライブラリが[ggplot2](https://cran.r-project.org/web/packages/ggplot2/index.html)です。一般的に、これらのライブラリを使用してデータをプロットするプロセスには、ターゲットにしたいデータフレームの部分を特定し、必要に応じてそのデータに変換を行い、x軸とy軸の値を割り当て、表示するプロットの種類を決定し、プロットを表示することが含まれます。

`ggplot2`は、The Grammar of Graphics（グラフィックスの文法）に基づいてグラフィックスを宣言的に作成するためのシステムです。[The Grammar of Graphics](https://en.wikipedia.org/wiki/Ggplot2)は、スケールやレイヤーなどの意味的なコンポーネントにグラフを分割するデータ可視化の一般的なスキームです。言い換えれば、少ないコードで単変量または多変量データのプロットやグラフを簡単に作成できるため、`ggplot2`はRで最も人気のある可視化パッケージです。ユーザーは`ggplot2`に変数を美学にマッピングする方法、使用するグラフィカルプリミティブを指示し、残りは`ggplot2`が処理します。

> ✅ プロット = データ + 美学 + ジオメトリ
> - データはデータセットを指します
> - 美学は研究対象の変数（x軸とy軸の変数）を示します
> - ジオメトリはプロットの種類（折れ線グラフ、棒グラフなど）を指します

データとプロットを通じて伝えたいストーリーに応じて、最適なジオメトリ（プロットの種類）を選択してください。

> - トレンドを分析する: 折れ線、縦棒
> - 値を比較する: 棒、縦棒、円、散布図
> - 部分が全体にどのように関連しているかを示す: 円
> - データの分布を示す: 散布図、棒
> - 値間の関係を示す: 折れ線、散布図、バブル

✅ ggplot2の説明的な[チートシート](https://nyu-cdsc.github.io/learningr/assets/data-visualization-2.1.pdf)もチェックしてみてください。

## 鳥の翼幅値について折れ線グラフを作成する

Rコンソールを開き、データセットをインポートします。
> 注: データセットはこのリポジトリのルートにある`/data`フォルダーに保存されています。

データセットをインポートし、データの先頭（上位5行）を観察しましょう。

```r
birds <- read.csv("../../data/birds.csv",fileEncoding="UTF-8-BOM")
head(birds)
```
データの先頭にはテキストと数値が混在しています:

|      | Name                         | ScientificName         | Category              | Order        | Family   | Genus       | ConservationStatus | MinLength | MaxLength | MinBodyMass | MaxBodyMass | MinWingspan | MaxWingspan |
| ---: | :--------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :----------------- | --------: | --------: | ----------: | ----------: | ----------: | ----------: |
|    0 | Black-bellied whistling-duck | Dendrocygna autumnalis | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Dendrocygna | LC                 |        47 |        56 |         652 |        1020 |          76 |          94 |
|    1 | Fulvous whistling-duck       | Dendrocygna bicolor    | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Dendrocygna | LC                 |        45 |        53 |         712 |        1050 |          85 |          93 |
|    2 | Snow goose                   | Anser caerulescens     | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Anser       | LC                 |        64 |        79 |        2050 |        4050 |         135 |         165 |
|    3 | Ross's goose                 | Anser rossii           | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Anser       | LC                 |      57.3 |        64 |        1066 |        1567 |         113 |         116 |
|    4 | Greater white-fronted goose  | Anser albifrons        | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Anser       | LC                 |        64 |        81 |        1930 |        3310 |         130 |         165 |

数値データを基本的な折れ線グラフでプロットすることから始めましょう。この興味深い鳥たちの最大翼幅を表示したいとします。

```r
install.packages("ggplot2")
library("ggplot2")
ggplot(data=birds, aes(x=Name, y=MaxWingspan,group=1)) +
  geom_line() 
```
ここでは、`ggplot2`パッケージをインストールし、`library("ggplot2")`コマンドを使用してワークスペースにインポートします。ggplotでプロットを作成するには、`ggplot()`関数を使用し、データセット、x軸とy軸の変数を属性として指定します。この場合、折れ線グラフをプロットするために`geom_line()`関数を使用します。

![MaxWingspan-lineplot](../../../../../3-Data-Visualization/R/09-visualization-quantities/images/MaxWingspan-lineplot.png)

何がすぐに気づきますか？少なくとも1つの外れ値があるようです。これはかなりの翼幅ですね！2000センチメートル以上の翼幅は20メートル以上に相当します。ミネソタ州にプテロダクティルスがいるのでしょうか？調査してみましょう。

Excelで外れ値をすばやくソートすることもできますが、プロット内から作業を続けて可視化プロセスを進めましょう。

x軸にラベルを追加して、どの種類の鳥が対象であるかを表示します:

```r
ggplot(data=birds, aes(x=Name, y=MaxWingspan,group=1)) +
  geom_line() +
  theme(axis.text.x = element_text(angle = 45, hjust=1))+
  xlab("Birds") +
  ylab("Wingspan (CM)") +
  ggtitle("Max Wingspan in Centimeters")
```
`theme`で角度を指定し、`xlab()`と`ylab()`でx軸とy軸のラベルを指定します。`ggtitle()`はグラフ/プロットに名前を付けます。

![MaxWingspan-lineplot-improved](../../../../../3-Data-Visualization/R/09-visualization-quantities/images/MaxWingspan-lineplot-improved.png)

ラベルの回転を45度に設定しても、読むには多すぎます。別の戦略を試してみましょう: 外れ値のみをラベル付けし、チャート内にラベルを設定します。散布図を使用してラベル付けのスペースを増やします:

```r
ggplot(data=birds, aes(x=Name, y=MaxWingspan,group=1)) +
  geom_point() +
  geom_text(aes(label=ifelse(MaxWingspan>500,as.character(Name),'')),hjust=0,vjust=0) + 
  theme(axis.title.x=element_blank(), axis.text.x=element_blank(), axis.ticks.x=element_blank())
  ylab("Wingspan (CM)") +
  ggtitle("Max Wingspan in Centimeters") + 
```
ここで何が起こっているのでしょうか？`geom_point()`関数を使用して散布点をプロットしました。これにより、`MaxWingspan > 500`の鳥にラベルを追加し、プロットを整理するためにx軸のラベルを非表示にしました。

何がわかりますか？

![MaxWingspan-scatterplot](../../../../../3-Data-Visualization/R/09-visualization-quantities/images/MaxWingspan-scatterplot.png)

## データをフィルタリングする

ハクトウワシとプレーリーファルコンは、おそらく非常に大きな鳥ですが、最大翼幅に余分な0が追加されているようです。翼幅25メートルのハクトウワシに出会う可能性は低いですが、もしそうなら教えてください！これら2つの外れ値を除外した新しいデータフレームを作成しましょう:

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
新しいデータフレーム`birds_filtered`を作成し、散布図をプロットしました。外れ値を除外することで、データがよりまとまり、理解しやすくなりました。

![MaxWingspan-scatterplot-improved](../../../../../3-Data-Visualization/R/09-visualization-quantities/images/MaxWingspan-scatterplot-improved.png)

翼幅に関して少なくともクリーンなデータセットができたので、これらの鳥についてさらに発見してみましょう。

折れ線グラフや散布図はデータ値やその分布に関する情報を表示できますが、このデータセットに内在する値について考えたいと思います。このデータセットに関する以下の質問に答えるための可視化を作成できます:

> 鳥のカテゴリーはいくつあり、それぞれの数はどれくらいですか？
> 絶滅、絶滅危惧種、希少種、一般種の鳥はそれぞれ何羽いますか？
> リンネの分類法における属や目の数はどれくらいですか？
## 棒グラフを探索する

棒グラフはデータのグループ化を表示する必要がある場合に実用的です。このデータセットに存在する鳥のカテゴリーを調べて、どのカテゴリーが最も一般的かを確認しましょう。
フィルタリングされたデータで棒グラフを作成します。

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
以下のスニペットでは、データを操作してグループ化し、積み上げ棒グラフをプロットするために[dplyr](https://www.rdocumentation.org/packages/dplyr/versions/0.7.8)と[lubridate](https://www.rdocumentation.org/packages/lubridate/versions/1.8.0)パッケージをインストールします。まず、鳥の`Category`でデータをグループ化し、`MinLength`、`MaxLength`、`MinBodyMass`、`MaxBodyMass`、`MinWingspan`、`MaxWingspan`列を要約します。その後、`ggplot2`パッケージを使用して棒グラフをプロットし、異なるカテゴリーの色とラベルを指定します。

![積み上げ棒グラフ](../../../../../3-Data-Visualization/R/09-visualization-quantities/images/stacked-bar-chart.png)

しかし、この棒グラフはデータがグループ化されていないため読みにくいです。プロットしたいデータだけを選択する必要がありますので、鳥のカテゴリーに基づいて長さを見てみましょう。

データをフィルタリングして鳥のカテゴリーのみを含めます。

カテゴリーが多いため、このチャートを縦に表示し、その高さを調整してすべてのデータを表示できるようにします:

```r
birds_count<-dplyr::count(birds_filtered, Category, sort = TRUE)
birds_count$Category <- factor(birds_count$Category, levels = birds_count$Category)
ggplot(birds_count,aes(Category,n))+geom_bar(stat="identity")+coord_flip()
```
まず`Category`列のユニークな値をカウントし、それを新しいデータフレーム`birds_count`にソートします。このソートされたデータを同じレベルでファクタリングし、ソートされた方法でプロットされるようにします。その後、`ggplot2`を使用してデータを棒グラフでプロットします。`coord_flip()`は水平棒をプロットします。

![カテゴリーの長さ](../../../../../3-Data-Visualization/R/09-visualization-quantities/images/category-length.png)

この棒グラフは、各カテゴリーの鳥の数を良い視点で示しています。一目で、この地域で最も多い鳥がカモ/ガン/水鳥のカテゴリーに属していることがわかります。ミネソタ州は「1万の湖の地」と呼ばれているので、これは驚くべきことではありません！

✅ このデータセットで他のカウントを試してみてください。何か驚くことはありますか？

## データの比較

新しい軸を作成してグループ化されたデータの異なる比較を試すことができます。鳥のカテゴリーに基づいて鳥の最大長さを比較してみましょう:

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

![データの比較](../../../../../3-Data-Visualization/R/09-visualization-quantities/images/comparingdata.png)

ここには驚くべきことはありません: ハチドリはペリカンやガンと比較して最大長さが最も短いです。データが論理的に意味を持つのは良いことです！

棒グラフをより興味深いものにするために、データを重ね合わせることができます。鳥のカテゴリーに基づいて最小長さと最大長さを重ね合わせてみましょう:

```r
ggplot(data=birds_grouped, aes(x=Category)) +
  geom_bar(aes(y=MaxLength), stat="identity", position ="identity",  fill='blue') +
  geom_bar(aes(y=MinLength), stat="identity", position="identity", fill='orange')+
  coord_flip()
```
![重ね合わせた値](../../../../../3-Data-Visualization/R/09-visualization-quantities/images/superimposed-values.png)

## 🚀 チャレンジ

この鳥のデータセットは、特定の生態系内のさまざまな種類の鳥についての豊富な情報を提供します。インターネットを検索して、他の鳥に関するデータセットを見つけてみてください。これらの鳥に関するチャートやグラフを作成して、知らなかった事実を発見してください。
## [講義後のクイズ](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/17)

## 復習と自己学習

この最初のレッスンでは、`ggplot2`を使用して数量を可視化する方法についての情報を提供しました。データセットを可視化するための他の方法について調査してください。[Lattice](https://stat.ethz.ch/R-manual/R-devel/library/lattice/html/Lattice.html)や[Plotly](https://github.com/plotly/plotly.R#readme)などのパッケージを使用して可視化できるデータセットを探してみてください。

## 課題
[折れ線、散布図、棒グラフ](assignment.md)

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知ください。元の言語で記載された文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解釈について、当社は責任を負いません。