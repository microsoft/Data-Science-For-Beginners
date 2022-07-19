# 수량 시각화

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../../sketchnotes/09-Visualizing-Quantities.png)|
|:---:|
| 수량 시각화 - _제작자 : [@nitya](https://twitter.com/nitya)_ |

이 강의에서는 사용할 수 있는 많은 파이썬 라이브러리 중에 하나를 사용하여 수량 개념과 관련된 흥미로운 시각화를 만드는 방법을 알아봅니다. 여러분은 미네소타의 새들에 대한 정리된 데이터 세트를 사용하여, 지역 야생동물에 대한 많은 흥미로운 사실들을 배울 수 있습니다.
## [강의 전 퀴즈](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/16)

## Matplotlib으로 날개 길이 관찰하기

다양한 종류의 간단하고 정교한 플롯과 차트를 모두 생성할 수 있는 훌륭한 라이브러리는 [Matplotlib](https://matplotlib.org/stable/index.html) 입니다. 일반적으로 이러한 라이브러리를 사용하여 데이터를 그리는 프로세스에는 대상으로 지정하려는 데이터 프레임 부분 식별, 필요한 해당 데이터에 대한 변환 수행, x 및 y축 값 할당, 표시할 플롯 종류를 결정한 다음 그림을 표시하는 작업이 포함됩니다. Matplotlib은 다양한 시각화를 제공하지만, 이 강의에서는 수량 시각화에 가장 적합한 선형 차트, 산점도 및 막대그래프에 중점을 두겠습니다.

> ✅ 데이터 구조와 전달하려는 내용에 가장 적합한 차트를 사용하세요.
> - 시간 경과에 따른 추세 분석: 선
> - 값을 비교하기: 막대, 세로 막대형, 파이, 산점도
> - 부분이 전체와 어떻게 관련되어 있는지 보여주기: 파이
> - 데이터 분포 표시: 산점도, 막대
> - 추세 표시: 선, 세로 막대형
> - 값 사이의 관계 표시: 선, 산점도, 버블

데이터 세트가 있고 주어진 항목이 얼마나 포함되어 있는지 확인해야 하는 경우에, 가장 먼저 처리해야 하는 작업 중 하나는 해당 값을 검사하는 것입니다.

✅ Matplotlib에 사용할 수 있는 매우 좋은 '치트 시트'가 있습니다. [here](https://matplotlib.org/cheatsheets/cheatsheets.pdf).

## 새 날개 길이 값에 대한 선 그래프 작성하기

이 강의 폴더의 루트에 있는 `notebook.ipynb` 파일을 열고 셀을 추가합니다.

> 참고: 데이터는 '/데이터'폴더의 이 repo 루트에 저장됩니다.

```python
import pandas as pd
import matplotlib.pyplot as plt
birds = pd.read_csv('../../data/birds.csv')
birds.head()
```
이 데이터는 텍스트와 숫자의 혼합으로 이루어져있습니다:


|      | Name                         | ScientificName         | Category              | Order        | Family   | Genus       | ConservationStatus | MinLength | MaxLength | MinBodyMass | MaxBodyMass | MinWingspan | MaxWingspan |
| ---: | :--------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :----------------- | --------: | --------: | ----------: | ----------: | ----------: | ----------: |
|    0 | Black-bellied whistling-duck | Dendrocygna autumnalis | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Dendrocygna | LC                 |        47 |        56 |         652 |        1020 |          76 |          94 |
|    1 | Fulvous whistling-duck       | Dendrocygna bicolor    | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Dendrocygna | LC                 |        45 |        53 |         712 |        1050 |          85 |          93 |
|    2 | Snow goose                   | Anser caerulescens     | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Anser       | LC                 |        64 |        79 |        2050 |        4050 |         135 |         165 |
|    3 | Ross's goose                 | Anser rossii           | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Anser       | LC                 |      57.3 |        64 |        1066 |        1567 |         113 |         116 |
|    4 | Greater white-fronted goose  | Anser albifrons        | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Anser       | LC                 |        64 |        81 |        1930 |        3310 |         130 |         165 |

먼저 기본 선 그래프을 사용하여 숫자 데이터 중 일부를 표시해 보겠습니다. 여러분이 이 흥미로운 새들의 최대 날개 길이를 보고싶다고 가정해 보겠습니다.

```python
wingspan = birds['MaxWingspan'] 
wingspan.plot()
```
![Max Wingspan](../images/max-wingspan.png)

여러분은 바로 무언가를 알아차리셨나요? 적어도 하나의 이상값이 있는 것 같은데, 날개 폭이 꽤 넓군요! 2300센티미터의 날개 폭은 23미터와 같습니다. 미네소타를 배회하는 익룡이 있는 걸까요? 조사해 봅시다.

Excel에서 빠른 정렬을 수행하여 오타일 가능성이 있는 이상값을 찾을 수 있지만, 플롯 내에서 작업하여 시각화 프로세스를 계속합니다.

x축에 label을 추가하여 문제의 새 종류를 표시합니다.

```
plt.title('Max Wingspan in Centimeters')
plt.ylabel('Wingspan (CM)')
plt.xlabel('Birds')
plt.xticks(rotation=45)
x = birds['Name'] 
y = birds['MaxWingspan']

plt.plot(x, y)

plt.show()
```
![wingspan with labels](../images/max-wingspan-labels.png)

label의 회전을 45도로 설정해도 읽기에는 너무 많습니다. 다른 전략을 시도해 보겠습니다. 해당 이상값에만 label을 지정하고 차트 내에 label을 설정합니다. 분산형 차트를 사용하여 labeling을 위한 더 많은 공간을 만들 수 있습니다.

```python
plt.title('Max Wingspan in Centimeters')
plt.ylabel('Wingspan (CM)')
plt.tick_params(axis='both',which='both',labelbottom=False,bottom=False)

for i in range(len(birds)):
    x = birds['Name'][i]
    y = birds['MaxWingspan'][i]
    plt.plot(x, y, 'bo')
    if birds['MaxWingspan'][i] > 500:
        plt.text(x, y * (1 - 0.05), birds['Name'][i], fontsize=12)
    
plt.show()
```
무슨 일이 일어나고 있는 거죠? `tick_params`를 사용하여 하단 레이블을 숨긴 다음 새 데이터(bird data) 에 루프를 만들었습니다. 'bo'를 이용해 작고 동그란 파란 점으로 차트를 표시하면 최대 날개 길이가 500을 초과하는 새가 있는지 확인하고 점 옆에 label을 표시했습니다. label을 y축에서 약간 오프셋(`y * (1 - 0.05)`)하고 새 이름을 레이블로 사용했습니다.
What did you discover?

![outliers](../images/labeled-wingspan.png)
## 데이터 필터링

대머리 독수리(Bald eagle)와 대머리 매(Prairie falcon)은 아마도 매우 큰 새일 것이지만, 이들의 최대 날개 길이에 '0'이 추가되어 잘못 표기된 것으로 보입니다. 여러분이 25미터의 날개폭을 가진 흰머리 독수리를 만날 것 같지는 않지만, 만약 만난다면 우리에게 알려주세요! 이제 이 두 가지 이상치를 제외하고 새 데이터 프레임을 생성해 보겠습니다.

```python
plt.title('Max Wingspan in Centimeters')
plt.ylabel('Wingspan (CM)')
plt.xlabel('Birds')
plt.tick_params(axis='both',which='both',labelbottom=False,bottom=False)
for i in range(len(birds)):
    x = birds['Name'][i]
    y = birds['MaxWingspan'][i]
    if birds['Name'][i] not in ['Bald eagle', 'Prairie falcon']:
        plt.plot(x, y, 'bo')
plt.show()
```

이상치를 필터링함으로써 이제 데이터의 응집력이 높아지고 이해하기 쉬워졌습니다.

![scatterplot of wingspans](../images/scatterplot-wingspan.png)

이제 우리는 적어도 날개 길이 측면에서 더 깨끗한 데이터 셋를 얻었으므로 이 새들에 대해 더 자세히 알아보겠습니다.

선 그래프 및 산점도 그래프는 데이터 값과 그 분포에 대한 정보를 표시할 수 있지만, 이 데이터 셋에 내재된 값에 대해 고려하려고 합니다. 수량에 대한 다음 질문에 답하기 위해 시각화를 만들 수 있습니다.

> 새의 종류는 몇 가지이며 그 수는 얼마인가요?
> 얼마나 많은 새들이 멸종했고, 멸종위기에 처해있고, 희귀하거나 흔할까요?
> Linnaeus의 용어에는 얼마나 많은 다양한 속과 목들이 있나요?
## 막대 차트 탐색

막대형 차트는 데이터 그룹화를 보여줘야 할 때 유용합니다. 이 데이터셋에 있는 새들의 를 탐색하여 숫자로 가장 흔한 새가 무엇인지 알아보겠습니다.

노트북 파일에서 기본 막대 차트를 만듭니다.

✅ 참고, 앞 섹션에서 식별한 두 개의 이상값 새를 필터링하거나, 날개 폭의 오타를 편집하거나, 날개 폭 값에 의존하지 않는 연습에 사용할 수 있습니다.

막대 차트를 만들고 싶다면 초점을 맞출 데이터를 선택하면 됩니다. 원시 데이터로 막대 차트를 만들 수 있습니다.

```python
birds.plot(x='Category',
        kind='bar',
        stacked=True,
        title='Birds of Minnesota')

```
![full data as a bar chart](../images/full-data-bar.png)

그러나 그룹화되지 않은 데이터가 너무 많기 때문에 이 막대 차트를 읽을 수 없습니다. 표시할 데이터만 선택해야 하므로 카테고리를 기준으로 새의 길이를 살펴보겠습니다.

새 카테고리만 포함하도록 데이터를 필터링합니다.

✅ Pandas를 사용하여 데이터를 관리한 다음 Matplotlib으로 차트 작성을 합니다.

카테고리가 많으므로 이 차트를 세로로 표시하고 모든 데이터를 설명하도록 높이를 조정할 수 있습니다.

```python
category_count = birds.value_counts(birds['Category'].values, sort=True)
plt.rcParams['figure.figsize'] = [6, 12]
category_count.plot.barh()
```
![category and length](../images/category-counts.png)

이 막대 차트는 각 카테고리의 새의 수를 잘 보여줍니다. 눈 깜짝할 사이에 이 지역에서 가장 많은 수의 새가 오리(Ducks)/거위(Geese)/물새(Waterfowl) 카테고리에 있음을 알 수 있습니다. 미네소타는 '10,000개의 호수의 땅'이므로 이것은 놀라운 일이 아닙니다!

✅ 이 데이터 세트에서 다른 수를 시도하세요. 여러분을 놀라게 하는 것이 있나요?

## 데이터 비교

새로운 축을 만들어 그룹화된 데이터의 다양한 비교를 시도할 수 있습니다. 카테고리에 따라 새의 MaxLength를 비교하세요.

```python
maxlength = birds['MaxLength']
plt.barh(y=birds['Category'], width=maxlength)
plt.rcParams['figure.figsize'] = [6, 12]
plt.show()
```
![comparing data](../images/category-length.png)

여기서 놀라운 것은 없습니다. 벌새(hummingbirds)는 펠리컨(Pelicans)이나 기러기(Geese)에 비해 MaxLength가 가장 짧습니다. 데이터가 논리적으로 타당할 때 좋습니다!

데이터를 중첩하여 막대 차트에 대한 더 흥미로운 시각화를 만들 수 있습니다. 주어진 새 카테고리에 최소 및 최대 길이를 중첩해 보겠습니다.

```python
minLength = birds['MinLength']
maxLength = birds['MaxLength']
category = birds['Category']

plt.barh(category, maxLength)
plt.barh(category, minLength)

plt.show()
```
이 플롯에서는 최소 길이 및 최대 길이의 새 카테고리당 범위를 볼 수 있습니다. 이 데이터를 고려할 때, 새의 몸길이가 클수록 새의 몸길이는 더 넓어진다고 해도 무방할 것입니다. 신기하지 않나요!

![superimposed values](../images/superimposed.png)

## 🚀 도전

이 새 데이터 셋은 특정 생태계 내의 다양한 종류의 새에 대한 풍부한 정보를 제공합니다. 인터넷을 검색하여 다른 조류 지향 데이터 셋을 찾을 수 있는지 확인해 보세요. 여러분이 깨닫지 못한 사실을 발견하기 위해 이 새들에 대한 차트와 그래프를 만드는 연습을 하세요.
## [이전 강의 퀴즈](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/17)

## 복습 & 자기주도학습

이번 첫번째 강의에서는 Matplotlib을 사용하여 수량을 시각화하는 방법에 대한 몇 가지 정보를 배웠습니다. 시각화를 위해 데이터셋으로 작업할 수 있는 다른 방법에 대해 알아보세요. [Plotly](https://github.com/plotly/plotly.py) 는 이 강의에서 다루지 않을 내용입니다. 어떤 기능을 제공하는지 살펴보세요.
## 과제

[선, 산점도, 막대 그래프](assignment.md)
