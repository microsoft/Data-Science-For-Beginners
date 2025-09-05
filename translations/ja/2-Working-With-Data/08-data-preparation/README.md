<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1b560955ff39a2bcf2a049fce474a951",
  "translation_date": "2025-09-05T12:41:03+00:00",
  "source_file": "2-Working-With-Data/08-data-preparation/README.md",
  "language_code": "ja"
}
-->
# データの取り扱い: データ準備

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/08-DataPreparation.png)|
|:---:|
|データ準備 - _スケッチノート by [@nitya](https://twitter.com/nitya)_ |

## [講義前クイズ](https://ff-quizzes.netlify.app/en/ds/quiz/14)

データの出所によっては、生データに一貫性のない部分が含まれていることがあり、これが分析やモデリングの際に課題を引き起こす可能性があります。言い換えれば、このようなデータは「汚れている」と分類され、クリーンアップが必要です。このレッスンでは、欠損、不正確、または不完全なデータに対処するためのデータのクリーニングと変換の技術に焦点を当てます。このレッスンで取り上げるトピックは、PythonとPandasライブラリを使用し、このディレクトリ内の[ノートブック](../../../../2-Working-With-Data/08-data-preparation/notebook.ipynb)で実演されます。

## データをクリーンにする重要性

- **使いやすさと再利用性**: データが適切に整理され正規化されていると、検索、利用、他者との共有が容易になります。

- **一貫性**: データサイエンスでは、複数のデータセットを扱うことがよくあります。異なるソースからのデータセットを結合する必要がある場合、それぞれのデータセットが共通の標準化を持っていることが重要です。これにより、すべてのデータセットを1つに統合した際にも有用性が保たれます。

- **モデルの精度**: クリーンなデータは、それに依存するモデルの精度を向上させます。

## 一般的なクリーニングの目標と戦略

- **データセットの探索**: データ探索（[後のレッスン](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/4-Data-Science-Lifecycle/15-analyzing)で取り上げます）は、クリーンアップが必要なデータを発見するのに役立ちます。データセット内の値を視覚的に観察することで、他の部分がどのように見えるかの期待値を設定したり、解決可能な問題のアイデアを得ることができます。探索には、基本的なクエリ、可視化、サンプリングが含まれます。

- **フォーマットの統一**: データの出所によっては、データの提示方法に一貫性がない場合があります。これにより、検索や値の表現に問題が生じる可能性があります。一般的なフォーマットの問題には、空白、日付、データ型の解決が含まれます。フォーマットの問題を解決する方法は、データを使用する人々に委ねられることが多いです。例えば、日付や数字の表現方法に関する標準は国によって異なる場合があります。

- **重複**: データが複数回出現すると、不正確な結果を生む可能性があり、通常は削除する必要があります。これは、2つ以上のデータセットを結合する際によく見られる現象です。ただし、結合されたデータセット内の重複が追加情報を提供する場合があり、その場合は保持する必要があることもあります。

- **欠損データ**: 欠損データは、不正確さや弱い、または偏った結果を引き起こす可能性があります。これらは、データの「再読み込み」や、Pythonのようなコードを使用して欠損値を補完することで解決できる場合があります。または、単に値と対応するデータを削除することもあります。データが欠損する理由はさまざまであり、それを解決するためのアクションは、欠損の原因や理由に依存することがあります。

## DataFrame情報の探索
> **学習目標:** このセクションの終わりまでに、pandas DataFrameに格納されたデータの一般的な情報を見つけることに慣れることができます。

データをpandasにロードすると、それはほとんどの場合DataFrameに格納されます（詳細は[前のレッスン](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/2-Working-With-Data/07-python#dataframe)を参照してください）。しかし、DataFrame内のデータセットが60,000行と400列ある場合、どのようにして扱うデータの概要を把握すればよいのでしょうか？幸いなことに、[pandas](https://pandas.pydata.org/)は、DataFrameの全体的な情報をすばやく確認するための便利なツールを提供しています。

この機能を探索するために、Pythonのscikit-learnライブラリをインポートし、象徴的なデータセットである**Irisデータセット**を使用します。

```python
import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()
iris_df = pd.DataFrame(data=iris['data'], columns=iris['feature_names'])
```
|                                        |sepal length (cm)|sepal width (cm)|petal length (cm)|petal width (cm)|
|----------------------------------------|-----------------|----------------|-----------------|----------------|
|0                                       |5.1              |3.5             |1.4              |0.2             |
|1                                       |4.9              |3.0             |1.4              |0.2             |
|2                                       |4.7              |3.2             |1.3              |0.2             |
|3                                       |4.6              |3.1             |1.5              |0.2             |
|4                                       |5.0              |3.6             |1.4              |0.2             |

- **DataFrame.info**: 最初に、`info()`メソッドを使用して、`DataFrame`内の内容の概要を表示します。このデータセットを見てみましょう。
```python
iris_df.info()
```
```
RangeIndex: 150 entries, 0 to 149
Data columns (total 4 columns):
 #   Column             Non-Null Count  Dtype  
---  ------             --------------  -----  
 0   sepal length (cm)  150 non-null    float64
 1   sepal width (cm)   150 non-null    float64
 2   petal length (cm)  150 non-null    float64
 3   petal width (cm)   150 non-null    float64
dtypes: float64(4)
memory usage: 4.8 KB
```
これにより、*Iris*データセットには4列に150エントリがあり、欠損値がないことがわかります。すべてのデータは64ビット浮動小数点数として格納されています。

- **DataFrame.head()**: 次に、`DataFrame`の実際の内容を確認するために、`head()`メソッドを使用します。`iris_df`の最初の数行を見てみましょう。
```python
iris_df.head()
```
```
   sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
0                5.1               3.5                1.4               0.2
1                4.9               3.0                1.4               0.2
2                4.7               3.2                1.3               0.2
3                4.6               3.1                1.5               0.2
4                5.0               3.6                1.4               0.2
```
- **DataFrame.tail()**: 逆に、`DataFrame`の最後の数行を確認するには、`tail()`メソッドを使用します。
```python
iris_df.tail()
```
```
     sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
145                6.7               3.0                5.2               2.3
146                6.3               2.5                5.0               1.9
147                6.5               3.0                5.2               2.0
148                6.2               3.4                5.4               2.3
149                5.9               3.0                5.1               1.8
```
> **ポイント:** DataFrameの情報や最初と最後の数値を確認するだけでも、扱うデータのサイズ、形状、内容について即座に把握することができます。

## 欠損データの処理
> **学習目標:** このセクションの終わりまでに、DataFrameから欠損値を置き換えたり削除したりする方法を理解できるようになります。

使用したい（または使用せざるを得ない）データセットには、ほとんどの場合欠損値が含まれています。欠損データの処理方法には、最終的な分析や現実世界の結果に影響を与える微妙なトレードオフが伴います。

Pandasでは、欠損値を処理する方法が2つあります。1つ目は、以前のセクションで見た`NaN`（Not a Number）です。これは、IEEE浮動小数点仕様の一部であり、欠損浮動小数点値を示すためにのみ使用されます。

浮動小数点以外の欠損値については、pandasはPythonの`None`オブジェクトを使用します。`None`と`NaN`の2種類の欠損値が存在するのは混乱を招くように思えるかもしれませんが、この設計選択には合理的なプログラム上の理由があり、実際にはほとんどのケースで良い妥協点を提供します。それにもかかわらず、`None`と`NaN`の両方には、それらの使用方法に関する制約があることを覚えておく必要があります。

`NaN`と`None`についての詳細は、[ノートブック](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/4-Data-Science-Lifecycle/15-analyzing/notebook.ipynb)を参照してください！

- **欠損値の検出**: `pandas`では、`isnull()`と`notnull()`メソッドが欠損データを検出するための主な方法です。どちらもデータに対してブールマスクを返します。`numpy`を使用して`NaN`値を扱います。
```python
import numpy as np

example1 = pd.Series([0, np.nan, '', None])
example1.isnull()
```
```
0    False
1     True
2    False
3     True
dtype: bool
```
出力をよく見てください。何か驚くことはありますか？`0`は算術的にはnullですが、それでも完全に有効な整数であり、pandasはそのように扱います。`''`はもう少し微妙です。セクション1では空の文字列値を表すために使用しましたが、それでも文字列オブジェクトであり、pandasにとってはnullの表現ではありません。

次に、これらのメソッドを実際に使用する方法に近い形で使用してみましょう。ブールマスクを直接`Series`や`DataFrame`のインデックスとして使用することができ、欠損値（または存在する値）を扱う際に便利です。

> **ポイント:** `isnull()`と`notnull()`メソッドは、`DataFrame`で使用すると似たような結果を生成します。結果とそのインデックスを表示するため、データを扱う際に非常に役立ちます。

- **欠損値の削除**: 欠損値を特定するだけでなく、pandasは`Series`や`DataFrame`から欠損値を削除する便利な方法を提供します（特に大規模なデータセットでは、欠損値を他の方法で処理するよりも、分析から削除する方が望ましい場合が多いです）。これを実際に見てみましょう。
```python
example1 = example1.dropna()
example1
```
```
0    0
2     
dtype: object
```
これは、`example3[example3.notnull()]`の出力と同じように見えるはずです。違いは、マスクされた値をインデックスする代わりに、`dropna`が`Series` `example1`から欠損値を削除した点です。

`DataFrame`は2次元であるため、データを削除するためのオプションが増えます。

```python
example2 = pd.DataFrame([[1,      np.nan, 7], 
                         [2,      5,      8], 
                         [np.nan, 6,      9]])
example2
```
|      | 0 | 1 | 2 |
|------|---|---|---|
|0     |1.0|NaN|7  |
|1     |2.0|5.0|8  |
|2     |NaN|6.0|9  |

（pandasが`NaN`に対応するために2つの列を浮動小数点型にアップキャストしたことに気づきましたか？）

`DataFrame`から単一の値を削除することはできないため、行または列全体を削除する必要があります。状況に応じて、どちらかを選択することになります。データサイエンスでは、列が変数を、行が観測値を表すことが多いため、データの行を削除する方が一般的です。`dropna()`のデフォルト設定は、null値を含むすべての行を削除することです。

```python
example2.dropna()
```
```
	0	1	2
1	2.0	5.0	8
```
必要に応じて、列からNA値を削除することもできます。これを行うには、`axis=1`を指定します。
```python
example2.dropna(axis='columns')
```
```
	2
0	7
1	8
2	9
```
これにより、小さなデータセットでは保持したいデータが多く削除される可能性があります。すべてのnull値を含む行や列だけを削除したい場合はどうすればよいでしょうか？`dropna`の`how`および`thresh`パラメータを使用してこれを指定できます。

デフォルトでは、`how='any'`です（確認したい場合や、メソッドに他のパラメータがあるかを確認したい場合は、コードセルで`example4.dropna?`を実行してください）。代わりに、`how='all'`を指定して、すべてのnull値を含む行や列のみを削除することもできます。例を拡張してみましょう。

```python
example2[3] = np.nan
example2
```
|      |0  |1  |2  |3  |
|------|---|---|---|---|
|0     |1.0|NaN|7  |NaN|
|1     |2.0|5.0|8  |NaN|
|2     |NaN|6.0|9  |NaN|

`thresh`パラメータを使用すると、より細かい制御が可能になります。保持するために必要な*非null*値の数を設定します。
```python
example2.dropna(axis='rows', thresh=3)
```
```
	0	1	2	3
1	2.0	5.0	8	NaN
```
ここでは、最初と最後の行が削除されています。これは、それらが非null値を2つしか含んでいないためです。

- **欠損値の補完**: データセットによっては、欠損値を削除するよりも有効な値で補完する方が理にかなっている場合があります。これをインプレースで行うために`isnull`を使用することもできますが、多くの値を補完する必要がある場合は手間がかかります。このため、pandasは`fillna`を提供しており、これを使用すると、欠損値を指定した値で置き換えた`Series`や`DataFrame`のコピーを返します。別の例を作成して、これがどのように機能するかを見てみましょう。
```python
example3 = pd.Series([1, np.nan, 2, None, 3], index=list('abcde'))
example3
```
```
a    1.0
b    NaN
c    2.0
d    NaN
e    3.0
dtype: float64
```
すべての欠損エントリを単一の値（例えば`0`）で補完することができます。
```python
example3.fillna(0)
```
```
a    1.0
b    0.0
c    2.0
d    0.0
e    3.0
dtype: float64
```
欠損値を**前方補完**することもできます。これは、最後の有効な値を使用して欠損値を補完する方法です。
```python
example3.fillna(method='ffill')
```
```
a    1.0
b    1.0
c    2.0
d    2.0
e    3.0
dtype: float64
```
また、**後方補完**を使用して、次の有効な値を後方に伝播させて欠損値を補完することもできます。
```python
example3.fillna(method='bfill')
```
```
a    1.0
b    2.0
c    2.0
d    3.0
e    3.0
dtype: float64
```
予想される通り、これは`DataFrame`でも同様に機能しますが、null値を補完する軸を指定することもできます。以前使用した`example2`を再度使用してみましょう。
```python
example2.fillna(method='ffill', axis=1)
```
```
	0	1	2	3
0	1.0	1.0	7.0	7.0
1	2.0	5.0	8.0	8.0
2	NaN	6.0	9.0	9.0
```
前方補完のための以前の値が利用できない場合、null値はそのまま残ることに注意してください。
> **ポイント:** データセット内の欠損値に対処する方法は複数あります。使用する具体的な戦略（削除する、置き換える、またはどのように置き換えるか）は、そのデータの特性によって決定されるべきです。データセットを扱い、操作する経験を積むことで、欠損値への対処方法に対する感覚がより磨かれていきます。
## 重複データの削除

> **学習目標:** このセクションの終わりまでに、DataFrameから重複する値を特定し削除する方法に慣れることを目指します。

欠損データに加えて、現実世界のデータセットでは重複データに遭遇することもよくあります。幸いなことに、`pandas`を使えば、重複エントリを簡単に検出して削除することができます。

- **重複の特定: `duplicated`**: pandasの`duplicated`メソッドを使うと、簡単に重複値を見つけることができます。このメソッドは、`DataFrame`内のエントリが以前のエントリと重複しているかどうかを示すブール値のマスクを返します。これを実際に試すために、別の例の`DataFrame`を作成してみましょう。
```python
example4 = pd.DataFrame({'letters': ['A','B'] * 2 + ['B'],
                         'numbers': [1, 2, 1, 3, 3]})
example4
```
|      |letters|numbers|
|------|-------|-------|
|0     |A      |1      |
|1     |B      |2      |
|2     |A      |1      |
|3     |B      |3      |
|4     |B      |3      |

```python
example4.duplicated()
```
```
0    False
1    False
2     True
3    False
4     True
dtype: bool
```
- **重複の削除: `drop_duplicates`**: `duplicated`の値がすべて`False`であるデータのコピーを返します。
```python
example4.drop_duplicates()
```
```
	letters	numbers
0	A	1
1	B	2
3	B	3
```
`duplicated`と`drop_duplicates`はデフォルトで全ての列を考慮しますが、`DataFrame`内の特定の列のみに限定して処理を行うよう指定することも可能です。
```python
example4.drop_duplicates(['letters'])
```
```
letters	numbers
0	A	1
1	B	2
```

> **まとめ:** 重複データの削除は、ほぼすべてのデータサイエンスプロジェクトにおいて重要なステップです。重複データは分析結果を変えてしまい、不正確な結果をもたらす可能性があります！


## 🚀 チャレンジ

ここで学んだ内容はすべて[Jupyter Notebook](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/2-Working-With-Data/08-data-preparation/notebook.ipynb)として提供されています。また、各セクションの後には演習問題が用意されているので、ぜひ挑戦してみてください！

## [講義後のクイズ](https://ff-quizzes.netlify.app/en/ds/quiz/15)



## 復習と自己学習

データを分析やモデリングのために準備する方法は多岐にわたり、データのクリーニングは「実践的」な経験が重要なステップです。このレッスンでカバーされていないテクニックを探求するために、Kaggleの以下のチャレンジに挑戦してみてください。

- [データクリーニングチャレンジ: 日付の解析](https://www.kaggle.com/rtatman/data-cleaning-challenge-parsing-dates/)

- [データクリーニングチャレンジ: データのスケールと正規化](https://www.kaggle.com/rtatman/data-cleaning-challenge-scale-and-normalize-data)


## 課題

[フォームからのデータ評価](assignment.md)

---

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期すよう努めておりますが、自動翻訳には誤りや不正確な表現が含まれる可能性があります。原文（元の言語で記載された文書）が公式な情報源と見なされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤認について、当社は一切の責任を負いません。