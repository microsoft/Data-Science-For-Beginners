# 데이터 작업: 데이터 전처리

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../../sketchnotes/08-DataPreparation.png)|
|:---:|
|데이터 전처리 - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

## [강의 전 퀴즈](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/14)



원본에 따라 원시 데이터에는 분석 및 모델링에 문제를 일으킬 수 있는 일부 불일치 요소가 포함될 수 있습니다. 즉, 이 데이터는 "더티"로 분류될 수 있으며 사전에 처리해야 합니다. 이 단원에서는 누락, 혹은 부정확하거나 불완전한 데이터의 문제를 처리하기 위해 데이터를 정리하고 변환하는 기술에 중점을 둡니다. 이 강의에서 다루는 주제는 Python과 Pandas 라이브러리를 활용하며 이 디렉토리의 [notebook](../notebook.ipynb)에서 시연됩니다.

## 정제 데이터의 중요성

- **사용 및 재사용 용이성**: 데이터가 적절하게 구성되고 정규화되면 검색, 사용 및 다른 사람과 공유하기가 더 쉽습니다.

- **일관성**: 데이터 과학은 종종 복수의 데이터셋으로 작업해야 하는데, 서로 다른 소스의 데이터셋은 함께 결합되야 합니다. 각 개별 데이터 세트에 공통 표준화가 적용되도록 하나의 데이터 세트로 병합될 때 더욱 유용합니다.

- **모델 정확도**: 데이터를 정제하면 해당 데이터에 의존하는 모델의 정확도가 향상됩니다.

## 공통 정제 목표 및 전략

- **데이터셋 탐색**: [이후 강의](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/4-Data-Science-Lifecycle/15-analyzing)에서 다룰 데이터 탐색은 정제해야 하는 데이터를 찾는 데 도움이 될 수 있습니다. 데이터셋 내의 값을 시각적으로 관찰하면 나머지 데이터가 어떻게 보일지에 대한 기대치를 설정하거나, 해결할 수 있는 문제에 대한 아이디어를 제공할 수 있습니다. 탐색에는 기본 쿼리, 시각화 및 샘플링이 포함될 수 있습니다.

-  **형식화(Formatting)**: 소스에 따라 데이터가 표시되는 방식에 불일치가 있을 수 있습니다. 이로 인해 데이터셋 내에서 표시되지만 시각화 또는 쿼리 결과에 제대로 표시되지 않는 값을 검색하고 표시하는 데 문제가 발생할 수 있습니다. 일반적인 형식화 문제에는 공백, 날짜 및 데이터 유형 해결이 포함되며 이러한 문제를 해결하는 것은 일반적으로 데이터를 사용하는 사람들에게 달려 있습니다. 예를 들어 날짜와 숫자가 표시되는 방식에 대한 표준은 국가마다 다를 수 있습니다.

-  **중복**: 두 번 이상 발생하는 데이터는 부정확한 결과를 생성할 수 있으므로 보통 제거해야 합니다. 이는 두 개 이상의 데이터셋을 함께 결합할 때 발생할 수 있습니다. 그러나 결합된 데이터셋의 중복이 추가 정보를 제공할 수 있으며 보존할 필요가 있는 경우도 있습니다.

- **결측치(Missing Data)**: 누락된 데이터는 부정확함과 편향된 결과를 초래할 수 있습니다. 때로는 데이터를 "다시 로드"하여 누락된 값을 Python과 같은 계산 및 코드로 채우거나 단순히 값과 해당 데이터를 제거하여 이러한 문제를 해결할 수 있습니다. 데이터가 누락되는 데는 여러 가지 이유가 있으며 이러한 누락된 값을 해결하기 위한 방법론은 초기 데이터가 누락된 이유에 따라 달라질 수 있습니다.

## DataFrame 정보 탐색
> **학습 목표:** 하위 섹션이 끝날때까지, pandas DataFrame에 저장된 데이터에 대한 정보를 능숙하게 찾을 수 있을 것입니다.

데이터를 pandas에 로드하면 DataFrame에 없을 가능성이 더 높아집니다(이전 [단원](../../07-python/translations/README.ko.md#데이터프레임) 참조. 그러나 DataFrame에 있는 데이터셋에 60,000개의 행과 400개의 열이 있는 경우). 다행스럽게도 [pandas](https://pandas.pydata.org/)는 처음 몇 행과 마지막 몇 행 외에도 DataFrame에 대한 전체 정보를 빠르게 볼 수 있는 몇 가지 편리한 도구를 제공합니다.


이 기능을 살펴보기 위해 Python scikit-learn 라이브러리를 가져오고 상징적인 데이터셋인 **Iris 데이터셋** 을 사용합니다.

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

- **DataFrame.info**: 시작하기 앞서, `info()` 메서드를 사용하여 `DataFrame`에 있는 내용의 요약을 프린트합니다. 이 데이터셋을 살펴보고 우리가 가지고 있는 것이 무엇인지 살펴보겠습니다:

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
이를 통해 *Iris* 데이터셋에는 null 항목이 없는 4개의 열에 150개의 항목이 있음을 알 수 있습니다. 모든 데이터는 64비트 부동 소수점 숫자로 저장됩니다.

- **DataFrame.head()**: 다음으로, `DataFrame`의 실제 내용을 확인하기 위해 `head()` 메소드를 사용합니다. `iris_df`의 처음 몇 행이 어떻게 생겼는지 봅시다:
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
- **DataFrame.tail()**: Conversely, to check the last few rows of the `DataFrame`, we use the `tail()` method:
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
> **추가 팁:** DataFrame의 정보에 대한 메타데이터나 하나의 처음과 마지막 몇 개의 값을 보는 것만으로도 처리 중인 데이터의 크기, 모양 및 내용에 대한 즉각적인 아이디어를 얻을 수 있습니다.

## 결측치 처리
> **학습 목표:** 이 하위 섹션이 끝나면 DataFrame에서 null 값을 대체하거나 제거하는 방법을 배울 수 있습니다.

대부분의 경우 사용하려는(사용해야 하는) 데이터셋은 누락된 값이 있습니다. 누락된 데이터를 처리하는 방법은 최종 분석 및 실제 결과에 영향을 줄 수 있는 미묘한 절충안을 수반합니다.

Pandas는 두 가지 방법으로 결측치를 처리합니다. 이전 섹션에서 본 첫 번째 항목: `NaN` 또는 숫자 아님. 이것은 실제로 IEEE 부동 소수점 사양의 일부인 특수 값이며 누락된 부동 소수점 값을 나타내는 데만 사용됩니다.

float를 제외한 누락된 값의 경우 pandas는 Python `None` 객체를 사용합니다. 본질적으로 같은 두 가지 다른 종류의 값을 만나는 것이 혼란스러울 수 있지만, 이는 합리적인 프로그램적 이유가 있으며 실제로 이 같은 로직을 따를시 Pandas가 대부분의 경우 좋은 절충안을 제공할 수 있습니다. 그럼에도 불구하고 `None`과 `NaN` 모두 사용 방법과 관련하여 유의할 필요가 있습니다.

[Notebook](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/4-Data-Science-Lifecycle/15-analyzing/notebook.ipynb)에서 'NaN' 및 'None'에 대해 자세히 알아보자!

- **null 값 감지**: `pandas`에서 `isnull()` 및 `notnull()` 메서드는 null 데이터를 감지하는 기본 메서드입니다. 둘 다 데이터에 부울(bool) 마스크를 반환합니다. `NaN` 값을 받기 위해 `numpy`를 사용할 것입니다:
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
출력값을 자세히 살펴보세요. 놀랐나요? `0`은 산술 null이지만 그럼에도 불구하고 완벽하게 좋은 정수이고 pandas는 이를 그대로 취급합니다. `''`는 조금 더 미묘합니다. 섹션 1에서 빈 문자열 값을 나타내기 위해 사용했지만 pandas에 관한 한 문자열 개체이며 null 표현이 아닙니다.

이제 이것을 바꿔서 실제로 사용하는 것과 같은 방식으로 이러한 방법을 사용하겠습니다. 부울 마스크를 ``Series`` 또는 ``DataFrame`` 인덱스로 직접 사용할 수 있으며, 이는 분리된 결측(또는 현재)치로 작업하려고 할 때 유용할 수 있습니다.

> **추가 팁**: `isnull()` 및 `notnull()` 메서드는 모두 `DataFrame`에서 사용할 때 유사한 결과를 생성합니다. 결과와 해당 결과의 인덱스를 보여주므로 데이터와 씨름할 때 엄청난 도움이 됩니다.

- **null 값 삭제**: 누락된 값을 식별하는 것 외에도 pandas는 `Series` 및 `DataFrame`에서 null 값을 제거하는 편리한 수단을 제공합니다. (특히 대용량 데이터 세트의 경우 다른 방법으로 처리하는 것보다 분석에서 누락된 [NA] 값을 제거하는 것이 종종 더 좋습니다.) 실제 사례를 보기위해 `example1`로 돌아가겠습니다:
```python
example1 = example1.dropna()
example1
```
```
0    0
2     
dtype: object
```
주목할 점은 `example3[example3.notnull()]`의 출력과 같아야 합니다. 여기서 차이점은 마스킹된 값에 대한 인덱싱뿐만 아니라 `dropna`가 `Series` `example1`에서 누락된 값을 제거했다는 것입니다.

위의 `DataFrame`은 2차원이기 때문에 데이터 삭제를 위한 더 많은 옵션을 제공합니다.

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

(Pandas가 `NaN`을 받기 위해 두 개의 열을 float로 업캐스팅한 것을 눈치채셨나요?)

`DataFrame`에서 단일 값을 삭제할 수 없으므로 전체 행이나 열을 삭제해야 합니다. 하고 있는 일에 따라 둘 중 하나를 수행하고 싶을 수 있으므로 pandas는 둘 모두에 대한 옵션을 제공합니다. 데이터 과학에서 열은 일반적으로 변수를 나타내고 행은 관찰을 나타내므로 데이터 행을 삭제할 가능성이 더 큽니다. 'dropna()'의 기본 설정은 null 값을 포함하는 모든 행을 삭제하는 것입니다:

```python
example2.dropna()
```
```
	0	1	2
1	2.0	5.0	8
```
필요한 경우 열에서 NA 값을 삭제할 수 있습니다. 이렇게 하려면 `axis=1`을 사용하세요:
```python
example2.dropna(axis='columns')
```
```
	2
0	7
1	8
2	9
```
이 경우 특히 소규모 데이터셋에서 보관하고자 하는 많은 데이터가 삭제될 수 있습니다. null 값이 여러 개 또는 모두 포함된 행이나 열을 삭제하려는 경우 어떻게 해야 할까요? `how` 및 `thresh` 매개변수를 사용하여 `dropna`에서 이러한 설정을 지정합니다.

기본적으로 `how='any'`(자신을 확인하거나 메소드에 어떤 다른 매개변수가 있는지 확인하려면 코드 셀에서 `example4.dropna?`를 실행하세요). 또는 모든 null 값을 포함하는 행이나 열만 삭제하도록 `how='all'`을 지정할 수 있습니다. 예제 `DataFrame`을 확장하여 이것이 실제로 작동하는지 살펴보겠습니다.

```python
example2[3] = np.nan
example2
```
|      |0  |1  |2  |3  |
|------|---|---|---|---|
|0     |1.0|NaN|7  |NaN|
|1     |2.0|5.0|8  |NaN|
|2     |NaN|6.0|9  |NaN|

`thresh` 매개변수는 더 세분화된 컨트롤을 제공합니다. 행 또는 열이 유지하기 위해 가져야 하는 *null이 아닌* 값의 수를 설정합니다:
```python
example2.dropna(axis='rows', thresh=3)
```
```
	0	1	2	3
1	2.0	5.0	8	NaN
```
여기에서 첫 번째 행과 마지막 행은 null이 아닌 값이 두 개만 포함되어 있기 때문에 삭제되었습니다.

- **null 값 채우기**: 데이터셋에 따라 null 값을 삭제하는 대신 유효한 값으로 채우는 것이 더 합리적일 수 있습니다. `isnull`을 사용하여 이 작업을 수행할 수 있지만 특히 채울 값이 많은 경우 힘들 수 있습니다. 이것은 데이터 과학에서 일반화된 작업입니다. pandas는 누락된 값이 선택한 값으로 대체된 'Series' 또는 'DataFrame'의 복사본을 반환하는 'fillna'를 제공합니다. 이것이 실제로 어떻게 작동하는지 보기 위해 또 다른 예제 `Series`를 만들어 보겠습니다.
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
`0`과 같은 단일 값으로 모든 null 항목을 채울 수 있습니다:
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
결측치를 **정방향 채우기**로 null 값을 채워나갈 수 있습니다. 즉, 마지막 유효 값을 사용하여 null을 채웁니다.

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
또한 **역방향 채우기**로 null을 채울 수도 있습니다: 

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
짐작할 수 있듯이 이것은 `DataFrame`과 동일하게 작동하지만 null 값을 채울 `axis(축)`을 지정할 수도 있습니다. 이전에 사용한 `example2`를 다시 가져오겠습니다:
```python
example2.fillna(method='ffill', axis=1)
```
```
	0	1	2	3
0	1.0	1.0	7.0	7.0
1	2.0	5.0	8.0	8.0
2	NaN	6.0	9.0	9.0
```
정방향 채우기에 이전 값을 사용할 수 없는 경우 null 값이 유지됩니다.

> **추가 팁:** 데이터셋의 결측값을 처리하는 방법에는 여러 가지가 있습니다. 사용하는 특정 전략(제거, 교체 또는 교체 방법)은 해당 데이터의 세부 사항에 따라 결정되어야 합니다. 데이터셋을 처리하고 상호 작용하면 할수록 누락된 값을 처리하는 방법에 대한 더 나은 감각을 개발할 수 있습니다.

## 중복 데이터 제거

> **학습 목표:** 해당 섹션이 끝나고, DataFrames에서 중복 값을 식별하고 제거하는 데 익숙해집니다.

누락된 데이터 외에도 실제 데이터 세트에서 중복 데이터를 자주 접하게 됩니다. 다행히 `pandas`는 중복 항목을 쉽게 감지하고 제거할 수 있는 수단을 제공합니다.

- **중복 식별: `duplicated`**: pandas의 `duplicated` 메서드를 사용하여 중복 값을 쉽게 찾을 수 있습니다. 이 메서드는 `DataFrame`의 항목이 이전 항목의 중복 항목인지 여부를 나타내는 부울 마스크를 반환합니다. 이 동작을 보기 위해 또 다른 예제 `DataFrame`을 만들어 보겠습니다.
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
- **중복 삭제: `drop_duplicates`:** 모든 `중복된(duplicated)` 값이 `False`인 데이터의 복사본을 반환합니다:
```python
example4.drop_duplicates()
```
```
	letters	numbers
0	A	1
1	B	2
3	B	3
```
`duplicated` 및 `drop_duplicates`는 기본적으로 모든 열을 고려하지만 `DataFrame`에서 열의 하위 집합만 검사하도록 지정할 수 있습니다.:
```python
example4.drop_duplicates(['letters'])
```
```
letters	numbers
0	A	1
1	B	2
```

> **추가 팁:** 중복 데이터를 제거하는 것은 거의 모든 데이터 과학 프로젝트에서 필수적인 부분입니다. 중복 데이터는 분석 결과를 변경하고 부정확한 결과를 제공할 수 있습니다!


## 🚀 도전과제

논의된 모든 자료는 [Jupyter Notebook](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/2-Working-With-Data/08-data-preparation/notebook.ipynb)으로 제공됩니다. 또한, 각 섹션 후에 연습 문제가 있으므로 시도해 보세요!

## [강의 후 퀴즈](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/15)



## 리뷰 & 복습

분석 및 모델링을 위해 데이터를 준비하고 접근하는 방법에는 여러 가지가 있으며, 데이터 정리는 "실제" 경험인 중요한 단계입니다. 이 강의에서 다루지 않은 기술을 살펴보기 위해 Kaggle의 관련 챌린지를 시도하세요!.

- [데이터 정제 과제: 날짜 구문 분석](https://www.kaggle.com/rtatman/data-cleaning-challenge-parsing-dates/)

- [데이터 정제 과제: 데이터 확장 및 정규화](https://www.kaggle.com/rtatman/data-cleaning-challenge-scale-and-normalize-data)


## 과제

[특정 양식에서의 데이터 평가](../assignment.md)
