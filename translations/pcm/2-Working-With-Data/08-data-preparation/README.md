<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1b560955ff39a2bcf2a049fce474a951",
  "translation_date": "2025-11-18T18:20:18+00:00",
  "source_file": "2-Working-With-Data/08-data-preparation/README.md",
  "language_code": "pcm"
}
-->
# Work wit Data: Data Preparation

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/08-DataPreparation.png)|
|:---:|
|Data Preparation - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

## [Pre-Lecture Quiz](https://ff-quizzes.netlify.app/en/ds/quiz/14)

Dependin on di source, raw data fit get some wahala wey go make analysis and modeling hard. Dis kain data na wetin dem dey call “dirty” data, and e go need clean up. Dis lesson go show techniques wey go help clean and change di data so e go fit handle wahala like missing, wrong, or incomplete data. Di topics wey dem go cover for dis lesson go use Python and di Pandas library, and dem go [show am for di notebook](notebook.ipynb) wey dey inside dis folder.

## Why e dey important to clean data

- **E easy to use and reuse**: Wen data dey well arranged and normalized, e go dey easy to search, use, and share am wit other people.

- **Consistency**: For data science, you go dey work wit more than one dataset most times. Datasets wey come from different sources go need join together. If each dataset get di same standardization, e go make sure say di data still dey useful wen dem join am as one.

- **Model accuracy**: Clean data dey make di models wey dey depend on am dey more accurate.

## Common cleaning goals and strategies

- **Exploring a dataset**: Data exploration (we go talk about am for [later lesson](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/4-Data-Science-Lifecycle/15-analyzing)) fit help you see di data wey need clean up. Wen you look di values for di dataset, e fit give you idea of wetin di rest go look like or di wahala wey you fit solve. Exploration fit involve basic querying, visualizations, and sampling.

- **Formatting**: Di way data dey show fit get wahala dependin on di source. Dis fit make e hard to search or represent di value well, even if e dey inside di dataset. Common formatting wahala na things like whitespace, dates, and data types. Na di people wey dey use di data go decide how dem go fix di formatting wahala. For example, di way dem dey show dates and numbers fit dey different for different countries.

- **Duplications**: If data dey repeat, e fit give wrong results, so e better make you remove am. Dis dey happen wella wen you dey join two or more datasets. But sometimes, di duplicated data fit get extra information wey you go need keep.

- **Missing Data**: Missing data fit make results dey wrong or biased. Sometimes, you fit reload di data, fill di missing values wit computation and code like Python, or just remove di value and di data wey follow am. Di reason why data dey miss fit plenty, and how you go fix am go depend on why e miss.

## Exploring DataFrame information
> **Learning goal:** By di end of dis subsection, you go sabi how to find general information about di data wey dey pandas DataFrames.

Wen you don load your data into pandas, e go dey inside DataFrame (check di [previous lesson](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/2-Working-With-Data/07-python#dataframe) for detailed overview). But if di DataFrame get 60,000 rows and 400 columns, how you go start to understand wetin you dey work wit? Luckily, [pandas](https://pandas.pydata.org/) get tools wey go help you quickly see di overall information about di DataFrame plus di first few and last few rows.

To explore dis functionality, we go import di Python scikit-learn library and use one popular dataset: di **Iris data set**.

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

- **DataFrame.info**: To start, di `info()` method dey print summary of di content wey dey inside di `DataFrame`. Make we check dis dataset to see wetin we get:
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
From dis, we sabi say di *Iris* dataset get 150 entries for four columns wit no null entries. All di data dey store as 64-bit floating-point numbers.

- **DataFrame.head()**: Next, to check di actual content of di `DataFrame`, we go use di `head()` method. Make we see wetin di first few rows of our `iris_df` look like:
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
- **DataFrame.tail()**: To check di last few rows of di `DataFrame`, we go use di `tail()` method:
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
> **Takeaway:** Just by looking di metadata about di information for DataFrame or di first and last few values, you fit quickly get idea about di size, shape, and content of di data wey you dey deal wit.

## Dealing wit Missing Data
> **Learning goal:** By di end of dis subsection, you go sabi how to replace or remove null values from DataFrames.

Most times, di datasets wey you wan use (or must use) get missing values. How you handle missing data fit affect di final analysis and real-world results.

Pandas dey handle missing values in two ways. Di first one na `NaN`, or Not a Number. Dis na special value wey dey part of di IEEE floating-point specification, and e dey used only for missing floating-point values.

For missing values wey no be floats, pandas dey use di Python `None` object. Even though e fit look confusing to get two different kinds of values wey mean di same thing, di design choice dey make sense programmatically and e dey work well for most cases. But both `None` and `NaN` get restrictions wey you need to understand for how you fit use dem.

Check more about `NaN` and `None` from di [notebook](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/4-Data-Science-Lifecycle/15-analyzing/notebook.ipynb)!

- **Detecting null values**: For `pandas`, di `isnull()` and `notnull()` methods na di main methods to detect null data. Both dey return Boolean masks over your data. We go use `numpy` for `NaN` values:
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
Look di output well. E surprise you? Even though `0` na arithmetic null, e still be valid integer and pandas dey treat am like dat. `''` dey more tricky. Even though we use am for Section 1 to mean empty string value, e still be string object and pandas no dey see am as null.

Now, make we use dis methods di way you go use dem normally. You fit use Boolean masks directly as ``Series`` or ``DataFrame`` index, wey dey useful wen you wan work wit missing (or present) values.

> **Takeaway**: Both `isnull()` and `notnull()` dey show similar results wen you use dem for `DataFrame`s: dem dey show di results and di index of di results, wey go help you wella as you dey work wit your data.

- **Dropping null values**: Apart from identifying missing values, pandas get easy way to remove null values from `Series` and `DataFrame`s. (For big datasets, e better to just remove missing [NA] values from your analysis than dey try fix dem.) Make we see dis for action wit `example1`:
```python
example1 = example1.dropna()
example1
```
```
0    0
2     
dtype: object
```
Dis one suppose look like your output from `example3[example3.notnull()]`. Di difference na say, instead of just indexing di masked values, `dropna` don remove di missing values from di `Series` `example1`.

Because `DataFrame`s get two dimensions, e get more options to drop data.

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

(Did you notice say pandas don upcast two of di columns to floats to fit di `NaN`s?)

You no fit drop single value from `DataFrame`, so you go need drop full rows or columns. Depending on wetin you dey do, you fit wan drop one or di other, and pandas dey give you options for both. For data science, columns dey represent variables and rows dey represent observations, so you go likely drop rows of data; di default setting for `dropna()` na to drop all rows wey get any null values:

```python
example2.dropna()
```
```
	0	1	2
1	2.0	5.0	8
```
If e dey necessary, you fit drop NA values from columns. Use `axis=1` to do am:
```python
example2.dropna(axis='columns')
```
```
	2
0	7
1	8
2	9
```
Notice say dis fit drop plenty data wey you fit wan keep, especially for small datasets. Wetin if you wan drop rows or columns wey get plenty or even all null values? You fit set di `how` and `thresh` parameters for `dropna`.

By default, `how='any'` (if you wan check am or see di other parameters wey di method get, run `example4.dropna?` for code cell). You fit also set `how='all'` to drop only rows or columns wey get all null values. Make we expand our example `DataFrame` to see dis for action.

```python
example2[3] = np.nan
example2
```
|      |0  |1  |2  |3  |
|------|---|---|---|---|
|0     |1.0|NaN|7  |NaN|
|1     |2.0|5.0|8  |NaN|
|2     |NaN|6.0|9  |NaN|

Di `thresh` parameter dey give you more control: you go set di number of *non-null* values wey row or column need get to remain:
```python
example2.dropna(axis='rows', thresh=3)
```
```
	0	1	2	3
1	2.0	5.0	8	NaN
```
Here, di first and last row don drop, because dem get only two non-null values.

- **Filling null values**: Sometimes e go make sense to fill null values wit valid ones instead of dropping dem. You fit use `isnull` to do dis directly, but e fit dey stressful if di values wey you wan fill plenty. Because dis na common task for data science, pandas get `fillna`, wey dey return copy of di `Series` or `DataFrame` wit di missing values replaced wit wetin you choose. Make we create another example `Series` to see how dis dey work.

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
You fit fill all di null entries wit one value, like `0`:
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
You fit **forward-fill** null values, wey mean use di last valid value to fill di null:
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
You fit also **back-fill** to use di next valid value backward to fill di null:
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
As you fit guess, dis dey work di same way wit `DataFrame`s, but you fit also set `axis` to fill null values. Using di `example2` wey we don use before:
```python
example2.fillna(method='ffill', axis=1)
```
```
	0	1	2	3
0	1.0	1.0	7.0	7.0
1	2.0	5.0	8.0	8.0
2	NaN	6.0	9.0	9.0
```
Notice say if previous value no dey for forward-filling, di null value go remain.
> **Takeaway:** E get plenty ways wey you fit take handle missing values for your datasets. Di particular way wey you go use (whether na to remove am, replace am, or even how you go replace am) go depend on di kind data wey you dey work with. Di more you dey work with datasets, di more you go sabi how to handle missing values.

## How to remove duplicate data

> **Learning goal:** By di end of dis subsection, you suppose sabi how to find and remove duplicate values from DataFrames.

Apart from missing data, you go also see duplicated data for real-world datasets. E good say `pandas` get easy way to detect and remove duplicate entries.

- **How to find duplicates: `duplicated`**: You fit use di `duplicated` method for pandas to find duplicate values. E go return Boolean mask wey go show whether one entry for `DataFrame` na duplicate of di one wey dey before am. Make we create another example `DataFrame` to see how e dey work.
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
- **How to remove duplicates: `drop_duplicates`:** E go just return copy of di data wey all di `duplicated` values na `False`:
```python
example4.drop_duplicates()
```
```
	letters	numbers
0	A	1
1	B	2
3	B	3
```
Both `duplicated` and `drop_duplicates` dey default to check all di columns but you fit tell am make e check only some columns for your `DataFrame`:
```python
example4.drop_duplicates(['letters'])
```
```
letters	numbers
0	A	1
1	B	2
```

> **Takeaway:** Removing duplicate data na very important part of almost every data-science project. Duplicate data fit change di results of your analysis and give you wrong results!


## 🚀 Challenge

All di things wey we talk about dey inside [Jupyter Notebook](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/2-Working-With-Data/08-data-preparation/notebook.ipynb). Plus, exercises dey after each section, try dem out!

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ds/quiz/15)



## Review & Self Study

E get plenty ways wey you fit take prepare your data for analysis and modeling, and cleaning di data na important step wey you go need to do by yourself. Try dis challenges from Kaggle to learn techniques wey dis lesson no cover.

- [Data Cleaning Challenge: Parsing Dates](https://www.kaggle.com/rtatman/data-cleaning-challenge-parsing-dates/)

- [Data Cleaning Challenge: Scale and Normalize Data](https://www.kaggle.com/rtatman/data-cleaning-challenge-scale-and-normalize-data)


## Assignment

[Evaluating Data from a Form](assignment.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis document don use AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) take translate am. Even though we dey try make e accurate, abeg sabi say automated translations fit get mistake or no correct well. Di original document for di native language na di main correct source. For important information, e better make una use professional human translation. We no go fit take responsibility for any misunderstanding or wrong interpretation wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->