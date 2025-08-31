<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3ade580a06b5f04d57cc83a768a8fb77",
  "translation_date": "2025-08-31T10:59:11+00:00",
  "source_file": "2-Working-With-Data/08-data-preparation/README.md",
  "language_code": "en"
}
-->
# Working with Data: Data Preparation

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/08-DataPreparation.png)|
|:---:|
|Data Preparation - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

## [Pre-Lecture Quiz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/14)

Raw data, depending on its source, may have inconsistencies that make analysis and modeling difficult. This type of data is often referred to as "dirty" and requires cleaning. This lesson focuses on techniques for cleaning and transforming data to address issues like missing, inaccurate, or incomplete data. The topics covered will use Python and the Pandas library and will be [demonstrated in the notebook](../../../../2-Working-With-Data/08-data-preparation/notebook.ipynb) in this directory.

## The importance of cleaning data

- **Ease of use and reuse**: Properly organized and normalized data is easier to search, use, and share with others.

- **Consistency**: Data science often involves working with multiple datasets, which may need to be combined. Ensuring that each dataset follows common standards makes the merged data more useful.

- **Model accuracy**: Clean data improves the accuracy of models that depend on it.

## Common cleaning goals and strategies

- **Exploring a dataset**: Data exploration, covered in a [later lesson](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/4-Data-Science-Lifecycle/15-analyzing), helps identify data that needs cleaning. Observing values visually can set expectations or highlight problems to address. Exploration can involve querying, visualizations, and sampling.

- **Formatting**: Data from different sources may have inconsistencies in presentation, which can affect searches and visualizations. Common formatting issues include whitespace, dates, and data types. Resolving these issues often depends on the user's needs, as standards for dates and numbers vary by region.

- **Duplications**: Duplicate data can lead to inaccurate results and often needs to be removed. However, in some cases, duplicates may contain additional information and should be preserved.

- **Missing Data**: Missing data can lead to inaccuracies or biased results. Solutions include reloading the data, filling in missing values programmatically, or removing the affected data. The approach depends on the reasons behind the missing data.

## Exploring DataFrame information
> **Learning goal:** By the end of this subsection, you should be comfortable finding general information about the data stored in pandas DataFrames.

Once data is loaded into pandas, it is typically stored in a DataFrame (refer to the previous [lesson](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/2-Working-With-Data/07-python#dataframe) for an overview). If your DataFrame contains 60,000 rows and 400 columns, how do you start understanding it? Fortunately, [pandas](https://pandas.pydata.org/) offers tools to quickly view overall information about a DataFrame, as well as its first and last few rows.

To explore this functionality, we will use the Python scikit-learn library and the well-known **Iris dataset**.

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

- **DataFrame.info**: The `info()` method provides a summary of the content in a `DataFrame`. Let's examine this dataset:
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
This tells us that the *Iris* dataset has 150 entries across four columns, with no null values. All data is stored as 64-bit floating-point numbers.

- **DataFrame.head()**: To view the first few rows of the `DataFrame`, use the `head()` method:
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
- **DataFrame.tail()**: To view the last few rows of the `DataFrame`, use the `tail()` method:
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
> **Takeaway:** By examining metadata and the first/last few rows of a DataFrame, you can quickly understand its size, structure, and content.

## Dealing with Missing Data
> **Learning goal:** By the end of this subsection, you should know how to replace or remove null values from DataFrames.

Datasets often contain missing values. How you handle missing data can impact your analysis and real-world outcomes.

Pandas uses two methods to represent missing values: `NaN` (Not a Number) for floating-point data and `None` for other types. While this dual approach may seem confusing, it provides flexibility for most use cases. However, both `NaN` and `None` have limitations you should be aware of.

Learn more about `NaN` and `None` in the [notebook](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/4-Data-Science-Lifecycle/15-analyzing/notebook.ipynb)!

- **Detecting null values**: Use the `isnull()` and `notnull()` methods to detect null data. Both return Boolean masks over your data. We'll use `numpy` for `NaN` values:
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
Notice the output. While `0` is an arithmetic null, pandas treats it as a valid integer. Similarly, `''` (an empty string) is considered a valid string, not null.

You can use Boolean masks directly as a `Series` or `DataFrame` index to isolate missing or present values.

> **Takeaway**: The `isnull()` and `notnull()` methods provide results with indices, making it easier to work with your data.

- **Dropping null values**: Pandas offers a convenient way to remove null values from `Series` and `DataFrame`s. For large datasets, removing missing values is often more practical than other approaches. Let's revisit `example1`:
```python
example1 = example1.dropna()
example1
```
```
0    0
2     
dtype: object
```
This output matches `example3[example3.notnull()]`, but `dropna` removes missing values directly from the `Series`.

For `DataFrame`s, you can drop entire rows or columns. By default, `dropna()` removes rows with any null values:
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

(Pandas converts columns to floats to accommodate `NaN`s.)

To drop columns with null values, use `axis=1`:
```python
example2.dropna()
```
```
	0	1	2
1	2.0	5.0	8
```
You can also drop rows or columns with all null values using `how='all'`. For finer control, use the `thresh` parameter to specify the minimum number of non-null values required to keep a row or column:
```python
example2[3] = np.nan
example2
```
|      |0  |1  |2  |3  |
|------|---|---|---|---|
|0     |1.0|NaN|7  |NaN|
|1     |2.0|5.0|8  |NaN|
|2     |NaN|6.0|9  |NaN|

```python
example2.dropna(axis='rows', thresh=3)
```
```
	0	1	2	3
1	2.0	5.0	8	NaN
```
Here, rows with fewer than three non-null values are dropped.

- **Filling null values**: Instead of dropping null values, you can replace them with valid ones using `fillna`. This method is more efficient than manually replacing values. Let's create another example `Series`:
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
You can replace all null entries with a single value, like `0`:
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
You can **forward-fill** null values using the last valid value:
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
You can also **back-fill** null values using the next valid value:
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
This works similarly for `DataFrame`s, where you can specify an `axis` for filling null values. Using `example2` again:
```python
example2.fillna(method='ffill', axis=1)
```
```
	0	1	2	3
0	1.0	1.0	7.0	7.0
1	2.0	5.0	8.0	8.0
2	NaN	6.0	9.0	9.0
```
If no previous value exists for forward-filling, the null value remains.
> **Takeaway:** There are several ways to handle missing values in your datasets. The specific approach you choose (removing them, replacing them, or even how you replace them) should depend on the characteristics of the data. The more you work with and explore datasets, the better you'll become at managing missing values.

## Removing duplicate data

> **Learning goal:** By the end of this subsection, you should feel confident identifying and removing duplicate values from DataFrames.

In addition to missing data, real-world datasets often contain duplicate entries. Luckily, `pandas` offers a straightforward way to detect and remove duplicates.

- **Identifying duplicates: `duplicated`**: You can easily identify duplicate values using the `duplicated` method in pandas. This method returns a Boolean mask that indicates whether an entry in a `DataFrame` is a duplicate of a previous one. Let’s create another example `DataFrame` to see how this works.
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
- **Dropping duplicates: `drop_duplicates`:** This method simply returns a copy of the data where all `duplicated` values are `False`:
```python
example4.drop_duplicates()
```
```
	letters	numbers
0	A	1
1	B	2
3	B	3
```
Both `duplicated` and `drop_duplicates` default to considering all columns, but you can specify that they only examine a subset of columns in your `DataFrame`:
```python
example4.drop_duplicates(['letters'])
```
```
letters	numbers
0	A	1
1	B	2
```

> **Takeaway:** Removing duplicate data is a crucial step in almost every data science project. Duplicate data can skew your analysis and lead to inaccurate results!

## 🚀 Challenge

All the materials covered are available as a [Jupyter Notebook](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/2-Working-With-Data/08-data-preparation/notebook.ipynb). Additionally, there are exercises at the end of each section—give them a try!

## [Post-Lecture Quiz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/15)

## Review & Self Study

There are many ways to explore and approach preparing your data for analysis and modeling. Cleaning your data is a critical step that requires hands-on practice. Try these Kaggle challenges to learn techniques not covered in this lesson:

- [Data Cleaning Challenge: Parsing Dates](https://www.kaggle.com/rtatman/data-cleaning-challenge-parsing-dates/)

- [Data Cleaning Challenge: Scale and Normalize Data](https://www.kaggle.com/rtatman/data-cleaning-challenge-scale-and-normalize-data)

## Assignment

[Evaluating Data from a Form](assignment.md)

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please note that automated translations may contain errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is recommended. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.