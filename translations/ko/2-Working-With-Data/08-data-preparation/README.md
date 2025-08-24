<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3ade580a06b5f04d57cc83a768a8fb77",
  "translation_date": "2025-08-24T12:07:07+00:00",
  "source_file": "2-Working-With-Data/08-data-preparation/README.md",
  "language_code": "ko"
}
-->
# 데이터 작업: 데이터 준비

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/08-DataPreparation.png)|
|:---:|
|데이터 준비 - _스케치노트 by [@nitya](https://twitter.com/nitya)_ |

## [강의 전 퀴즈](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/14)

데이터의 출처에 따라 원시 데이터는 분석 및 모델링에 어려움을 줄 수 있는 불일치를 포함할 수 있습니다. 즉, 이러한 데이터는 "더럽다"고 간주될 수 있으며 정리가 필요합니다. 이 강의는 누락되거나 부정확하거나 불완전한 데이터를 처리하기 위해 데이터를 정리하고 변환하는 기술에 중점을 둡니다. 이 강의에서 다룰 주제는 Python과 Pandas 라이브러리를 활용하며, 이 디렉토리 내의 [노트북](../../../../2-Working-With-Data/08-data-preparation/notebook.ipynb)에서 시연됩니다.

## 데이터를 정리하는 것의 중요성

- **사용 및 재사용의 용이성**: 데이터가 적절히 정리되고 정규화되면 검색, 사용 및 다른 사람과 공유하기가 더 쉬워집니다.

- **일관성**: 데이터 과학은 종종 여러 데이터셋을 함께 작업해야 하며, 서로 다른 출처에서 온 데이터셋을 결합해야 할 때가 많습니다. 각 데이터셋이 공통 표준화를 갖추고 있으면 모든 데이터를 하나의 데이터셋으로 병합했을 때도 유용성을 유지할 수 있습니다.

- **모델 정확도**: 정리된 데이터는 이를 기반으로 하는 모델의 정확도를 향상시킵니다.

## 일반적인 데이터 정리 목표와 전략

- **데이터셋 탐색**: [후속 강의](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/4-Data-Science-Lifecycle/15-analyzing)에서 다룰 데이터 탐색은 정리가 필요한 데이터를 발견하는 데 도움을 줄 수 있습니다. 데이터셋 내 값을 시각적으로 관찰하면 나머지 데이터가 어떻게 보일지에 대한 기대치를 설정하거나 해결할 수 있는 문제를 파악할 수 있습니다. 탐색은 기본 쿼리, 시각화 및 샘플링을 포함할 수 있습니다.

- **형식 지정**: 데이터 출처에 따라 데이터가 표현되는 방식에 불일치가 있을 수 있습니다. 이는 데이터셋 내에서 값이 보이지만 시각화나 쿼리 결과에서 제대로 표현되지 않는 문제를 일으킬 수 있습니다. 일반적인 형식 문제는 공백, 날짜, 데이터 유형을 해결하는 것을 포함합니다. 형식 문제를 해결하는 것은 데이터를 사용하는 사람들에게 달려 있는 경우가 많습니다. 예를 들어, 날짜와 숫자가 표현되는 방식에 대한 표준은 국가마다 다를 수 있습니다.

- **중복**: 데이터가 여러 번 나타나면 부정확한 결과를 초래할 수 있으며 일반적으로 제거해야 합니다. 이는 두 개 이상의 데이터셋을 결합할 때 흔히 발생할 수 있습니다. 그러나 결합된 데이터셋의 중복이 추가 정보를 제공할 수 있는 경우에는 이를 보존해야 할 수도 있습니다.

- **누락된 데이터**: 누락된 데이터는 부정확하거나 약하거나 편향된 결과를 초래할 수 있습니다. 때로는 데이터를 "다시 로드"하거나, Python과 같은 코드로 누락된 값을 채우거나, 단순히 해당 값과 관련 데이터를 제거하여 해결할 수 있습니다. 데이터가 누락된 이유에 따라 이를 해결하는 방법이 달라질 수 있습니다.

## DataFrame 정보 탐색
> **학습 목표:** 이 섹션이 끝날 때까지 pandas DataFrame에 저장된 데이터에 대한 일반 정보를 찾는 데 익숙해져야 합니다.

데이터를 pandas에 로드하면 대부분 DataFrame에 저장됩니다(자세한 개요는 [이전 강의](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/2-Working-With-Data/07-python#dataframe)를 참조하세요). 그러나 DataFrame에 60,000개의 행과 400개의 열이 있는 경우, 어디서부터 작업을 시작해야 할까요? 다행히도 [pandas](https://pandas.pydata.org/)는 DataFrame의 전체 정보를 빠르게 확인할 수 있는 몇 가지 편리한 도구를 제공합니다. 또한 처음 몇 행과 마지막 몇 행도 확인할 수 있습니다.

이 기능을 탐색하기 위해 Python scikit-learn 라이브러리를 가져오고 대표적인 데이터셋인 **Iris 데이터셋**을 사용하겠습니다.

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

- **DataFrame.info**: 먼저, `info()` 메서드는 `DataFrame`에 있는 내용의 요약을 출력하는 데 사용됩니다. 이 데이터셋을 살펴보겠습니다:
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
이로부터 *Iris* 데이터셋에는 4개의 열에 150개의 항목이 있으며, 누락된 항목이 없다는 것을 알 수 있습니다. 모든 데이터는 64비트 부동 소수점 숫자로 저장됩니다.

- **DataFrame.head()**: 다음으로, `DataFrame`의 실제 내용을 확인하려면 `head()` 메서드를 사용합니다. `iris_df`의 처음 몇 행을 살펴보겠습니다:
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
- **DataFrame.tail()**: 반대로, `DataFrame`의 마지막 몇 행을 확인하려면 `tail()` 메서드를 사용합니다:
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
> **핵심 요약:** DataFrame의 정보 메타데이터나 처음 및 마지막 몇 개의 값을 확인하는 것만으로도 데이터의 크기, 형태, 내용을 즉시 파악할 수 있습니다.

## 누락된 데이터 처리
> **학습 목표:** 이 섹션이 끝날 때까지 DataFrame에서 null 값을 대체하거나 제거하는 방법을 알게 될 것입니다.

대부분의 경우, 사용하고자 하는 데이터셋(또는 사용해야 하는 데이터셋)에는 누락된 값이 포함되어 있습니다. 누락된 데이터를 처리하는 방식은 최종 분석 및 실제 결과에 영향을 미칠 수 있는 미묘한 트레이드오프를 수반합니다.

Pandas는 누락된 값을 두 가지 방식으로 처리합니다. 첫 번째는 이전 섹션에서 본 `NaN`(Not a Number)입니다. 이는 실제로 IEEE 부동 소수점 사양의 일부로, 누락된 부동 소수점 값을 나타내는 데만 사용됩니다.

부동 소수점 외의 누락된 값에 대해 pandas는 Python의 `None` 객체를 사용합니다. 두 가지 다른 종류의 누락 값을 만나게 되는 것이 혼란스러울 수 있지만, 이러한 설계 선택에는 타당한 프로그래밍적 이유가 있으며, 실제로 이 접근 방식은 대부분의 경우에 대해 pandas가 적절한 절충안을 제공할 수 있도록 합니다. 그럼에도 불구하고, `None`과 `NaN` 모두 사용 방법에 제한이 있다는 점을 염두에 두어야 합니다.

`NaN`과 `None`에 대한 자세한 내용은 [노트북](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/4-Data-Science-Lifecycle/15-analyzing/notebook.ipynb)을 확인하세요!

- **null 값 감지**: `pandas`에서 `isnull()` 및 `notnull()` 메서드는 null 데이터를 감지하는 주요 메서드입니다. 둘 다 데이터에 대해 Boolean 마스크를 반환합니다. 우리는 `numpy`를 사용하여 `NaN` 값을 다룰 것입니다:
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
출력을 자세히 살펴보세요. 놀라운 점이 있나요? `0`은 산술적으로 null이지만, 여전히 완벽한 정수로 간주되며 pandas는 이를 그렇게 처리합니다. `''`는 조금 더 미묘합니다. 섹션 1에서 빈 문자열 값을 나타내는 데 사용했지만, 여전히 문자열 객체이며 pandas가 null로 간주하지 않습니다.

이제 이러한 메서드를 실제로 사용하는 방식으로 전환해 보겠습니다. Boolean 마스크를 직접 `Series` 또는 `DataFrame` 인덱스로 사용할 수 있으며, 이는 누락된(또는 존재하는) 값을 고립시켜 작업할 때 유용합니다.

> **핵심 요약:** `isnull()` 및 `notnull()` 메서드는 `DataFrame`에서 사용될 때 유사한 결과를 생성합니다. 결과와 해당 결과의 인덱스를 보여주며, 이는 데이터를 다룰 때 매우 유용합니다.

- **null 값 제거**: 누락된 값을 식별하는 것 외에도 pandas는 `Series` 및 `DataFrame`에서 null 값을 제거하는 편리한 방법을 제공합니다. (특히 대규모 데이터셋에서는 누락된 [NA] 값을 다른 방식으로 처리하는 것보다 분석에서 단순히 제거하는 것이 더 바람직할 때가 많습니다.) 이를 실습으로 확인하기 위해 `example1`로 돌아가 보겠습니다:
```python
example1 = example1.dropna()
example1
```
```
0    0
2     
dtype: object
```
이는 `example3[example3.notnull()]`의 출력과 유사하게 보일 것입니다. 여기서 차이점은 마스크된 값만 인덱싱하는 대신, `dropna`가 `Series` `example1`에서 누락된 값을 제거했다는 점입니다.

`DataFrame`은 2차원이므로 데이터를 삭제할 때 더 많은 옵션을 제공합니다.

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

(pandas가 `NaN`을 수용하기 위해 두 개의 열을 부동 소수점으로 업캐스트한 것을 눈치채셨나요?)

`DataFrame`에서 단일 값을 삭제할 수는 없으므로 전체 행이나 열을 삭제해야 합니다. 수행 중인 작업에 따라 하나를 선택해야 할 수 있으며, pandas는 둘 다에 대한 옵션을 제공합니다. 데이터 과학에서는 일반적으로 열이 변수를 나타내고 행이 관측치를 나타내므로 데이터를 삭제할 때 행을 삭제하는 경우가 더 많습니다. `dropna()`의 기본 설정은 null 값을 포함하는 모든 행을 삭제하는 것입니다:

```python
example2.dropna()
```
```
	0	1	2
1	2.0	5.0	8
```
필요한 경우 열에서 NA 값을 삭제할 수도 있습니다. `axis=1`을 사용하여 수행하세요:
```python
example2.dropna(axis='columns')
```
```
	2
0	7
1	8
2	9
```
이 방법은 특히 작은 데이터셋에서 유지하고 싶은 많은 데이터를 삭제할 수 있습니다. 모든 null 값을 포함하는 행이나 열만 삭제하고 싶다면 어떻게 해야 할까요? `dropna`의 `how` 및 `thresh` 매개변수를 사용하여 이러한 설정을 지정할 수 있습니다.

기본적으로 `how='any'`입니다(직접 확인하거나 메서드의 다른 매개변수를 보려면 코드 셀에서 `example4.dropna?`를 실행하세요). 또는 `how='all'`을 지정하여 모든 null 값을 포함하는 행이나 열만 삭제할 수 있습니다. 이 동작을 확인하기 위해 예제 `DataFrame`을 확장해 보겠습니다.

```python
example2[3] = np.nan
example2
```
|      |0  |1  |2  |3  |
|------|---|---|---|---|
|0     |1.0|NaN|7  |NaN|
|1     |2.0|5.0|8  |NaN|
|2     |NaN|6.0|9  |NaN|

`thresh` 매개변수는 더 세밀한 제어를 제공합니다. 즉, 행이나 열이 유지되기 위해 필요한 *null이 아닌* 값의 수를 설정합니다:
```python
example2.dropna(axis='rows', thresh=3)
```
```
	0	1	2	3
1	2.0	5.0	8	NaN
```
여기서 첫 번째와 마지막 행은 null이 아닌 값이 두 개만 포함되어 있기 때문에 삭제되었습니다.

- **null 값 채우기**: 데이터셋에 따라 null 값을 삭제하는 대신 유효한 값으로 채우는 것이 더 적합할 때가 있습니다. 이를 위해 `isnull`을 사용하여 직접 처리할 수 있지만, 값이 많을 경우 번거로울 수 있습니다. 데이터 과학에서 매우 일반적인 작업이기 때문에 pandas는 `fillna`를 제공하며, 이는 null 값을 선택한 값으로 대체한 `Series` 또는 `DataFrame`의 복사본을 반환합니다. 이를 실습으로 확인하기 위해 또 다른 예제 `Series`를 만들어 보겠습니다.
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
모든 null 항목을 단일 값(예: `0`)으로 채울 수 있습니다:
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
null 값을 **앞으로 채우기**(forward-fill)하여 마지막 유효 값을 사용해 null을 채울 수 있습니다:
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
또한 **뒤로 채우기**(back-fill)를 사용하여 다음 유효 값을 뒤로 전파하여 null을 채울 수 있습니다:
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
예상하셨겠지만, 이는 `DataFrame`에서도 동일하게 작동하며 null 값을 채울 축(`axis`)을 지정할 수도 있습니다. 이전에 사용한 `example2`를 다시 사용해 보겠습니다:
```python
example2.fillna(method='ffill', axis=1)
```
```
	0	1	2	3
0	1.0	1.0	7.0	7.0
1	2.0	5.0	8.0	8.0
2	NaN	6.0	9.0	9.0
```
이전 값이 없어 forward-fill을 사용할 수 없는 경우 null 값이 그대로 남아 있는 것을 확인하세요.
> **핵심 요약:** 데이터셋에서 누락된 값을 처리하는 방법은 여러 가지가 있습니다. 어떤 전략을 사용할지(값을 제거하거나 대체하거나, 대체 방법을 선택하는 것)는 데이터의 특성에 따라 결정되어야 합니다. 데이터셋을 다루고 상호작용할수록 누락된 값을 처리하는 감각이 더 나아질 것입니다.

## 중복 데이터 제거하기

> **학습 목표:** 이 단원을 마치면, DataFrame에서 중복 값을 식별하고 제거하는 데 익숙해질 것입니다.

누락된 데이터 외에도, 실제 데이터셋에서는 중복된 데이터를 자주 접하게 됩니다. 다행히도, `pandas`는 중복 항목을 감지하고 제거하는 간단한 방법을 제공합니다.

- **중복 식별: `duplicated`**: pandas의 `duplicated` 메서드를 사용하면 중복 값을 쉽게 확인할 수 있습니다. 이 메서드는 `DataFrame`에서 이전 항목과 중복된 항목인지 여부를 나타내는 Boolean 마스크를 반환합니다. 이를 직접 확인하기 위해 또 다른 예제 `DataFrame`을 만들어 보겠습니다.
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
- **중복 제거: `drop_duplicates`:** `duplicated` 값이 `False`인 데이터만 복사하여 반환합니다:
```python
example4.drop_duplicates()
```
```
	letters	numbers
0	A	1
1	B	2
3	B	3
```
`duplicated`와 `drop_duplicates`는 기본적으로 모든 열을 고려하지만, 특정 열만 검사하도록 지정할 수도 있습니다:
```python
example4.drop_duplicates(['letters'])
```
```
letters	numbers
0	A	1
1	B	2
```

> **핵심 요약:** 중복 데이터를 제거하는 것은 거의 모든 데이터 과학 프로젝트에서 필수적인 단계입니다. 중복 데이터는 분석 결과를 왜곡시키고 부정확한 결과를 초래할 수 있습니다!


## 🚀 도전 과제

논의된 모든 자료는 [Jupyter Notebook](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/2-Working-With-Data/08-data-preparation/notebook.ipynb)으로 제공됩니다. 또한 각 섹션 뒤에는 연습 문제가 포함되어 있으니, 직접 시도해 보세요!

## [강의 후 퀴즈](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/15)



## 복습 및 자기 학습

데이터를 분석 및 모델링을 위해 준비하는 방법을 발견하고 접근하는 방법은 다양하며, 데이터를 정리하는 과정은 "직접 해보는" 경험이 중요합니다. 이 강의에서 다루지 않은 기술을 탐구하기 위해 Kaggle의 다음 도전 과제를 시도해 보세요.

- [데이터 정리 도전 과제: 날짜 파싱](https://www.kaggle.com/rtatman/data-cleaning-challenge-parsing-dates/)

- [데이터 정리 도전 과제: 데이터 스케일링 및 정규화](https://www.kaggle.com/rtatman/data-cleaning-challenge-scale-and-normalize-data)


## 과제

[폼 데이터 평가하기](assignment.md)

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전이 권위 있는 출처로 간주되어야 합니다. 중요한 정보에 대해서는 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 책임을 지지 않습니다.