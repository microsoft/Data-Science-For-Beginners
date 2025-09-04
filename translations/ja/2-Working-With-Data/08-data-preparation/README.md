<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "90a815d332aea41a222f4c6372e7186e",
  "translation_date": "2025-09-04T13:14:50+00:00",
  "source_file": "2-Working-With-Data/08-data-preparation/README.md",
  "language_code": "ja"
}
-->
# データの取り扱い: データ準備

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/08-DataPreparation.png)|
|:---:|
|データ準備 - _スケッチノート by [@nitya](https://twitter.com/nitya)_ |

## [講義前クイズ](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/14)

データの出所によっては、生データに不整合が含まれていることがあり、分析やモデリングに課題をもたらす可能性があります。言い換えれば、このデータは「汚れている」と分類され、クリーンアップが必要です。このレッスンでは、欠損、不正確、または不完全なデータの課題に対処するためのデータのクリーニングと変換技術に焦点を当てます。このレッスンで扱うトピックは、PythonとPandasライブラリを使用し、このディレクトリ内の[ノートブックで実演](notebook.ipynb)されます。

## データをクリーンアップする重要性

- **使いやすさと再利用性**: データが適切に整理され正規化されていると、検索、使用、他者との共有が容易になります。

- **一貫性**: データサイエンスでは、複数のデータセットを扱うことがよくあります。異なる出所からのデータセットを結合する際、各データセットが共通の標準化を持つことが重要です。これにより、すべてのデータセットが1つに統合された際にも有用性が保たれます。

- **モデルの精度**: クリーンアップされたデータは、それに依存するモデルの精度を向上させます。

## 一般的なクリーニングの目標と戦略

- **データセットの探索**: データ探索は、[後のレッスン](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/4-Data-Science-Lifecycle/15-analyzing)で扱いますが、クリーンアップが必要なデータを発見するのに役立ちます。データセット内の値を視覚的に観察することで、他の部分がどのように見えるかの期待値を設定したり、解決可能な問題のアイデアを得ることができます。探索には基本的なクエリ、視覚化、サンプリングが含まれます。

- **フォーマットの整備**: データの出所によっては、提示方法に不整合がある場合があります。これにより、データセット内で値が見られるものの、視覚化やクエリ結果で正しく表現されない問題が発生する可能性があります。一般的なフォーマットの問題には、空白、日付、データ型の解決が含まれます。フォーマットの問題を解決する責任は通常、データを使用する人々にあります。例えば、日付や数字の表現方法に関する標準は国によって異なる場合があります。

- **重複**: データが複数回出現すると、不正確な結果を生む可能性があり、通常は削除する必要があります。これは、2つ以上のデータセットを結合する際に一般的に発生します。ただし、結合されたデータセット内の重複が追加情報を提供する場合があり、保持する必要がある場合もあります。

- **欠損データ**: 欠損データは、不正確な結果や弱い、偏った結果を引き起こす可能性があります。これらはデータの「再ロード」、Pythonのようなコードを使用して欠損値を補完する、または単に値と対応するデータを削除することで解決される場合があります。データが欠損する理由はさまざまであり、欠損値を解決するために取られる行動は、欠損の原因や理由に依存する場合があります。

## DataFrame情報の探索
> **学習目標:** このセクションの終わりまでに、pandas DataFrameに格納されたデータの一般的な情報を見つけることに慣れることができます。

データをpandasにロードすると、ほとんどの場合DataFrameに格納されます（詳細な概要については[前のレッスン](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/2-Working-With-Data/07-python#dataframe)を参照してください）。しかし、DataFrame内のデータセットが60,000行と400列ある場合、どのようにして扱うデータの概要を把握するのでしょうか？幸いなことに、[pandas](https://pandas.pydata.org/)はDataFrameの全体的な情報を迅速に確認するための便利なツールを提供しており、最初と最後の数行も確認できます。

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

- **DataFrame.info**: 最初に、`info()`メソッドを使用して`DataFrame`内の内容の概要を出力します。このデータセットを見てみましょう。
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
これにより、*Iris*データセットには150件のエントリがあり、4つの列に分かれていて、欠損エントリがないことがわかります。すべてのデータは64ビット浮動小数点数として保存されています。

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
> **ポイント:** DataFrameの情報や最初と最後の数値を確認するだけで、扱うデータのサイズ、形状、内容について即座に把握することができます。

## 欠損データの処理
> **学習目標:** このセクションの終わりまでに、DataFrameからnull値を置き換えたり削除したりする方法を理解することができます。

使用したい（または使用しなければならない）データセットには、ほとんどの場合欠損値が含まれています。欠損データの処理方法には微妙なトレードオフがあり、最終的な分析や現実世界の結果に影響を与える可能性があります。

Pandasは欠損値を2つの方法で処理します。1つ目は以前のセクションで見た`NaN`（Not a Number）です。これは実際にはIEEE浮動小数点仕様の一部であり、欠損浮動小数点値を示すためだけに使用されます。

浮動小数点以外の欠損値については、pandasはPythonの`None`オブジェクトを使用します。これら2つの異なる欠損値が存在することは混乱を招くように思えるかもしれませんが、この設計選択には合理的なプログラム上の理由があり、実際にはほとんどのケースで良い妥協点を提供します。それにもかかわらず、`None`と`NaN`には、それらの使用方法に関して注意すべき制限があります。

`NaN`と`None`についての詳細は[ノートブック](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/4-Data-Science-Lifecycle/15-analyzing/notebook.ipynb)をチェックしてください！

- **null値の検出**: `pandas`では、`isnull()`と`notnull()`メソッドがnullデータを検出するための主要な方法です。どちらもデータに対してブールマスクを返します。`numpy`を使用して`NaN`値を扱います。
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
出力をよく見てください。何か驚くことはありますか？`0`は算術的にはnullですが、それでも完全に有効な整数であり、pandasはそれをそのように扱います。`''`は少し微妙です。セクション1で空の文字列値を表すために使用しましたが、それでも文字列オブジェクトであり、pandasにとってはnullの表現ではありません。

次に、これを実際に使用する方法に近い形で使用してみましょう。ブールマスクを直接`Series`や`DataFrame`のインデックスとして使用することができ、欠損値（または存在する値）を分離して扱う際に役立ちます。

> **ポイント:** `isnull()`と`notnull()`メソッドは、`DataFrame`で使用するときに似た結果を生成します。結果とそのインデックスを表示し、データを扱う際に非常に役立ちます。

- **null値の削除**: 欠損値を特定するだけでなく、pandasは`Series`や`DataFrame`からnull値を削除する便利な方法を提供します。（特に大規模なデータセットでは、欠損値を他の方法で処理するよりも、分析から単に削除する方が望ましい場合が多いです。）これを実際に見てみるために、`example1`に戻りましょう。
```python
example1 = example1.dropna()
example1
```
```
0    0
2     
dtype: object
```
これが`example3[example3.notnull()]`の出力と似ていることに注意してください。ここでの違いは、マスクされた値をインデックスするのではなく、`dropna`が`Series` `example1`から欠損値を削除したことです。

`DataFrame`には2次元があるため、データを削除するためのオプションが増えます。

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

（pandasが`NaN`を収容するために2つの列を浮動小数点にアップキャストしたことに気づきましたか？）

`DataFrame`から単一の値を削除することはできないため、完全な行または列を削除する必要があります。行う内容によって、どちらかを選択する場合があり、pandasは両方のオプションを提供します。データサイエンスでは、列は通常変数を表し、行は観測値を表すため、データの行を削除する可能性が高くなります。`dropna()`のデフォルト設定は、null値を含むすべての行を削除することです。

```python
example2.dropna()
```
```
	0	1	2
1	2.0	5.0	8
```
必要に応じて、列からNA値を削除することもできます。`axis=1`を使用してください。
```python
example2.dropna(axis='columns')
```
```
	2
0	7
1	8
2	9
```
これにより、保持したいデータが多く削除される可能性があります。特に小規模なデータセットでは注意が必要です。すべてのnull値を含む行や列だけを削除したい場合はどうすればよいでしょうか？`dropna`の`how`と`thresh`パラメータでその設定を指定できます。

デフォルトでは、`how='any'`です（自分で確認したり、メソッドの他のパラメータを確認したい場合は、コードセルで`example4.dropna?`を実行してください）。代わりに`how='all'`を指定して、すべてのnull値を含む行や列だけを削除することもできます。この動作を確認するために、例の`DataFrame`を拡張してみましょう。

```python
example2[3] = np.nan
example2
```
|      |0  |1  |2  |3  |
|------|---|---|---|---|
|0     |1.0|NaN|7  |NaN|
|1     |2.0|5.0|8  |NaN|
|2     |NaN|6.0|9  |NaN|

`thresh`パラメータを使用すると、より細かい制御が可能になります。行や列が保持されるためには、必要な*非null*値の数を設定します。
```python
example2.dropna(axis='rows', thresh=3)
```
```
	0	1	2	3
1	2.0	5.0	8	NaN
```
ここでは、最初と最後の行が削除されています。これらは非null値が2つしか含まれていないためです。

- **null値の補完**: データセットによっては、null値を削除するよりも有効な値で補完する方が理にかなっている場合があります。これをインプレースで行うために`isnull`を使用することもできますが、多くの値を補完する場合は手間がかかる可能性があります。データサイエンスではこの作業が非常に一般的であるため、pandasは`fillna`を提供しており、欠損値を選択した値で置き換えた`Series`や`DataFrame`のコピーを返します。これが実際にどのように機能するかを確認するために、別の例の`Series`を作成してみましょう。
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
すべてのnullエントリを単一の値（例えば`0`）で補完することができます。
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
null値を**前方補完**することができます。つまり、最後の有効な値を使用してnullを補完します。
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
また、**後方補完**を行い、次の有効な値を後方に伝播してnullを補完することもできます。
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
予想通り、これは`DataFrame`でも同じように機能しますが、null値を補完する軸を指定することもできます。以前使用した`example2`を再度使用します。
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
> **重要なポイント:** データセット内の欠損値を処理する方法は複数あります。使用する具体的な戦略（削除、置換、またはどのように置換するか）は、そのデータの特性によって決まります。データセットを扱い、操作する経験を積むことで、欠損値への対処方法に関する感覚が磨かれていきます。

## 重複データの削除

> **学習目標:** このセクションの終わりまでに、DataFrameから重複値を特定し削除する方法に慣れることができます。

欠損データに加えて、実際のデータセットでは重複データに遭遇することもよくあります。幸いなことに、`pandas`は重複エントリを検出し削除する簡単な方法を提供しています。

- **重複の特定: `duplicated`**: pandasの`duplicated`メソッドを使用すると、簡単に重複値を特定できます。このメソッドは、`DataFrame`内のエントリが以前のエントリと重複しているかどうかを示すブールマスクを返します。これを実際に試すために、別の例の`DataFrame`を作成してみましょう。
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
- **重複の削除: `drop_duplicates`**: `duplicated`値がすべて`False`であるデータのコピーを返します。
```python
example4.drop_duplicates()
```
```
	letters	numbers
0	A	1
1	B	2
3	B	3
```
`duplicated`と`drop_duplicates`はデフォルトですべての列を考慮しますが、`DataFrame`内の特定の列のみに限定して調べるよう指定することもできます。
```python
example4.drop_duplicates(['letters'])
```
```
letters	numbers
0	A	1
1	B	2
```

> **重要なポイント:** 重複データの削除は、ほぼすべてのデータサイエンスプロジェクトにおいて重要なステップです。重複データは分析結果を変え、誤った結果をもたらす可能性があります！


## 🚀 チャレンジ

このセクションで説明した内容はすべて[Jupyter Notebook](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/2-Working-With-Data/08-data-preparation/notebook.ipynb)として提供されています。また、各セクションの後には演習が用意されていますので、ぜひ挑戦してみてください！

## [講義後のクイズ](https://ff-quizzes.netlify.app/en/ds/)



## 復習と自己学習

データを分析やモデリングのために準備する方法を発見し、アプローチする方法はさまざまです。データをクリーンアップすることは重要なステップであり、「実践的な」経験が求められます。このレッスンでカバーされていない技術を探求するために、Kaggleの以下のチャレンジに挑戦してみてください。

- [データクリーニングチャレンジ: 日付の解析](https://www.kaggle.com/rtatman/data-cleaning-challenge-parsing-dates/)

- [データクリーニングチャレンジ: データのスケールと正規化](https://www.kaggle.com/rtatman/data-cleaning-challenge-scale-and-normalize-data)


## 課題

[フォームからのデータ評価](assignment.md)

---

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知ください。元の言語で記載された文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解釈について、当方は責任を負いません。