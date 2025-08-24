<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "87faccac113d772551486a67a607153e",
  "translation_date": "2025-08-24T13:39:07+00:00",
  "source_file": "3-Data-Visualization/10-visualization-distributions/README.md",
  "language_code": "ko"
}
-->
# 분포 시각화

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/10-Visualizing-Distributions.png)|
|:---:|
| 분포 시각화 - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

이전 강의에서, 미네소타의 새들에 대한 데이터셋에서 흥미로운 사실들을 배웠습니다. 이상치를 시각화하여 오류 데이터를 발견하고, 새 카테고리 간 최대 길이의 차이를 살펴보았습니다.

## [강의 전 퀴즈](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/18)
## 새 데이터셋 탐색하기

데이터를 탐구하는 또 다른 방법은 데이터의 분포, 즉 데이터가 축을 따라 어떻게 조직되어 있는지를 살펴보는 것입니다. 예를 들어, 미네소타 새들의 최대 날개 길이나 최대 몸무게의 일반적인 분포를 알고 싶을 수도 있습니다.

이 데이터셋의 데이터 분포에 대한 몇 가지 사실을 알아봅시다. 이 강의 폴더의 루트에 있는 _notebook.ipynb_ 파일에서 Pandas, Matplotlib, 그리고 데이터를 가져옵니다:

```python
import pandas as pd
import matplotlib.pyplot as plt
birds = pd.read_csv('../../data/birds.csv')
birds.head()
```

|      | Name                         | ScientificName         | Category              | Order        | Family   | Genus       | ConservationStatus | MinLength | MaxLength | MinBodyMass | MaxBodyMass | MinWingspan | MaxWingspan |
| ---: | :--------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :----------------- | --------: | --------: | ----------: | ----------: | ----------: | ----------: |
|    0 | Black-bellied whistling-duck | Dendrocygna autumnalis | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Dendrocygna | LC                 |        47 |        56 |         652 |        1020 |          76 |          94 |
|    1 | Fulvous whistling-duck       | Dendrocygna bicolor    | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Dendrocygna | LC                 |        45 |        53 |         712 |        1050 |          85 |          93 |
|    2 | Snow goose                   | Anser caerulescens     | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Anser       | LC                 |        64 |        79 |        2050 |        4050 |         135 |         165 |
|    3 | Ross's goose                 | Anser rossii           | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Anser       | LC                 |      57.3 |        64 |        1066 |        1567 |         113 |         116 |
|    4 | Greater white-fronted goose  | Anser albifrons        | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Anser       | LC                 |        64 |        81 |        1930 |        3310 |         130 |         165 |

일반적으로, 데이터가 어떻게 분포되어 있는지 빠르게 확인하려면 이전 강의에서 했던 것처럼 산점도를 사용할 수 있습니다:

```python
birds.plot(kind='scatter',x='MaxLength',y='Order',figsize=(12,8))

plt.title('Max Length per Order')
plt.ylabel('Order')
plt.xlabel('Max Length')

plt.show()
```
![max length per order](../../../../3-Data-Visualization/10-visualization-distributions/images/scatter-wb.png)

이 차트는 새의 Order별 몸 길이의 일반적인 분포를 보여주지만, 실제 분포를 표시하기에는 최적의 방법이 아닙니다. 이 작업은 일반적으로 히스토그램을 생성하여 수행됩니다.

## 히스토그램 작업하기

Matplotlib는 히스토그램을 사용하여 데이터 분포를 시각화하는 데 매우 유용한 방법을 제공합니다. 이 차트 유형은 막대 차트와 비슷하며, 막대의 상승과 하락을 통해 분포를 볼 수 있습니다. 히스토그램을 생성하려면 숫자 데이터를 사용해야 합니다. 히스토그램을 생성하려면 차트 유형을 'hist'로 정의하여 차트를 그릴 수 있습니다. 이 차트는 데이터셋의 전체 범위에 대한 MaxBodyMass의 분포를 보여줍니다. 데이터 배열을 작은 bin으로 나누어 데이터 값의 분포를 표시할 수 있습니다:

```python
birds['MaxBodyMass'].plot(kind = 'hist', bins = 10, figsize = (12,12))
plt.show()
```
![distribution over the entire dataset](../../../../3-Data-Visualization/10-visualization-distributions/images/dist1-wb.png)

보시다시피, 이 데이터셋의 400개 이상의 새들 중 대부분은 Max Body Mass가 2000 이하의 범위에 속합니다. `bins` 매개변수를 더 높은 숫자, 예를 들어 30으로 변경하여 데이터를 더 자세히 살펴보세요:

```python
birds['MaxBodyMass'].plot(kind = 'hist', bins = 30, figsize = (12,12))
plt.show()
```
![distribution over the entire dataset with larger bins param](../../../../3-Data-Visualization/10-visualization-distributions/images/dist2-wb.png)

이 차트는 분포를 조금 더 세부적으로 보여줍니다. 왼쪽으로 덜 치우친 차트를 생성하려면 특정 범위 내의 데이터만 선택하도록 설정할 수 있습니다:

몸무게가 60 이하인 새들만 필터링하고 40개의 `bins`를 표시하세요:

```python
filteredBirds = birds[(birds['MaxBodyMass'] > 1) & (birds['MaxBodyMass'] < 60)]      
filteredBirds['MaxBodyMass'].plot(kind = 'hist',bins = 40,figsize = (12,12))
plt.show()     
```
![filtered histogram](../../../../3-Data-Visualization/10-visualization-distributions/images/dist3-wb.png)

✅ 다른 필터와 데이터 포인트를 시도해 보세요. 데이터의 전체 분포를 보려면 `['MaxBodyMass']` 필터를 제거하여 라벨이 있는 분포를 표시하세요.

히스토그램은 색상과 라벨링을 개선할 수 있는 멋진 기능도 제공합니다:

두 분포 간의 관계를 비교하기 위해 2D 히스토그램을 생성하세요. `MaxBodyMass`와 `MaxLength`를 비교해 봅시다. Matplotlib는 더 밝은 색상을 사용하여 수렴을 보여주는 내장 방법을 제공합니다:

```python
x = filteredBirds['MaxBodyMass']
y = filteredBirds['MaxLength']

fig, ax = plt.subplots(tight_layout=True)
hist = ax.hist2d(x, y)
```
이 두 요소 간에 예상 축을 따라 예상되는 상관관계가 있는 것으로 보이며, 특히 강한 수렴 지점이 하나 있습니다:

![2D plot](../../../../3-Data-Visualization/10-visualization-distributions/images/2D-wb.png)

히스토그램은 기본적으로 숫자 데이터에 잘 작동합니다. 텍스트 데이터를 기준으로 분포를 확인해야 한다면 어떻게 해야 할까요?

## 텍스트 데이터를 사용하여 데이터셋의 분포 탐색하기

이 데이터셋에는 새의 카테고리, 속(genus), 종(species), 과(family) 및 보존 상태에 대한 유용한 정보도 포함되어 있습니다. 이 보존 상태 정보를 탐구해 봅시다. 새들이 보존 상태에 따라 어떻게 분포되어 있는지 확인해 보세요.

> ✅ 데이터셋에는 보존 상태를 설명하는 여러 약어가 사용됩니다. 이 약어들은 [IUCN 적색 목록 카테고리](https://www.iucnredlist.org/)에서 가져온 것으로, 종의 상태를 분류하는 조직입니다.
> 
> - CR: 심각한 멸종 위기(Critically Endangered)
> - EN: 멸종 위기(Endangered)
> - EX: 멸종(Extinct)
> - LC: 관심 필요 없음(Least Concern)
> - NT: 근접 위기(Near Threatened)
> - VU: 취약(Vulnerable)

이 값들은 텍스트 기반이므로 히스토그램을 생성하려면 변환이 필요합니다. 필터링된 새 데이터프레임을 사용하여 보존 상태와 최소 날개 길이를 표시하세요. 무엇을 발견할 수 있나요?

```python
x1 = filteredBirds.loc[filteredBirds.ConservationStatus=='EX', 'MinWingspan']
x2 = filteredBirds.loc[filteredBirds.ConservationStatus=='CR', 'MinWingspan']
x3 = filteredBirds.loc[filteredBirds.ConservationStatus=='EN', 'MinWingspan']
x4 = filteredBirds.loc[filteredBirds.ConservationStatus=='NT', 'MinWingspan']
x5 = filteredBirds.loc[filteredBirds.ConservationStatus=='VU', 'MinWingspan']
x6 = filteredBirds.loc[filteredBirds.ConservationStatus=='LC', 'MinWingspan']

kwargs = dict(alpha=0.5, bins=20)

plt.hist(x1, **kwargs, color='red', label='Extinct')
plt.hist(x2, **kwargs, color='orange', label='Critically Endangered')
plt.hist(x3, **kwargs, color='yellow', label='Endangered')
plt.hist(x4, **kwargs, color='green', label='Near Threatened')
plt.hist(x5, **kwargs, color='blue', label='Vulnerable')
plt.hist(x6, **kwargs, color='gray', label='Least Concern')

plt.gca().set(title='Conservation Status', ylabel='Min Wingspan')
plt.legend();
```

![wingspan and conservation collation](../../../../3-Data-Visualization/10-visualization-distributions/images/histogram-conservation-wb.png)

최소 날개 길이와 보존 상태 간에 뚜렷한 상관관계는 없는 것 같습니다. 이 방법을 사용하여 데이터셋의 다른 요소를 테스트해 보세요. 다른 필터를 시도해 보세요. 상관관계를 발견할 수 있나요?

## 밀도 플롯

지금까지 살펴본 히스토그램은 '단계적'이며 부드럽게 흐르지 않는다는 것을 눈치챘을 것입니다. 더 부드러운 밀도 차트를 표시하려면 밀도 플롯을 시도해 볼 수 있습니다.

밀도 플롯을 사용하려면 새로운 플롯 라이브러리인 [Seaborn](https://seaborn.pydata.org/generated/seaborn.kdeplot.html)을 익혀야 합니다.

Seaborn을 로드하고 기본 밀도 플롯을 시도해 보세요:

```python
import seaborn as sns
import matplotlib.pyplot as plt
sns.kdeplot(filteredBirds['MinWingspan'])
plt.show()
```
![Density plot](../../../../3-Data-Visualization/10-visualization-distributions/images/density1.png)

이 플롯은 이전의 최소 날개 길이 데이터 차트를 반영하며, 조금 더 부드럽습니다. Seaborn의 문서에 따르면, "히스토그램에 비해 KDE는 덜 복잡하고 더 해석 가능한 플롯을 생성할 수 있습니다. 특히 여러 분포를 그릴 때 유용합니다. 하지만 기본 분포가 경계가 있거나 부드럽지 않은 경우 왜곡을 초래할 가능성이 있습니다. 히스토그램과 마찬가지로 표현의 품질은 좋은 매개변수를 선택하는 데 달려 있습니다." [출처](https://seaborn.pydata.org/generated/seaborn.kdeplot.html) 즉, 항상 그렇듯이 이상치는 차트의 동작을 나쁘게 만들 수 있습니다.

두 번째로 생성한 MaxBodyMass의 울퉁불퉁한 선을 다시 방문하고 싶다면, 이 방법을 사용하여 매우 부드럽게 만들 수 있습니다:

```python
sns.kdeplot(filteredBirds['MaxBodyMass'])
plt.show()
```
![smooth bodymass line](../../../../3-Data-Visualization/10-visualization-distributions/images/density2.png)

너무 부드럽지 않은 선을 원한다면 `bw_adjust` 매개변수를 편집하세요:

```python
sns.kdeplot(filteredBirds['MaxBodyMass'], bw_adjust=.2)
plt.show()
```
![less smooth bodymass line](../../../../3-Data-Visualization/10-visualization-distributions/images/density3.png)

✅ 이 유형의 플롯에 사용할 수 있는 매개변수에 대해 읽어보고 실험해 보세요!

이 유형의 차트는 설명력이 뛰어난 시각화를 제공합니다. 예를 들어, 몇 줄의 코드로 새 Order별 최대 몸무게 밀도를 표시할 수 있습니다:

```python
sns.kdeplot(
   data=filteredBirds, x="MaxBodyMass", hue="Order",
   fill=True, common_norm=False, palette="crest",
   alpha=.5, linewidth=0,
)
```

![bodymass per order](../../../../3-Data-Visualization/10-visualization-distributions/images/density4.png)

하나의 차트에서 여러 변수의 밀도를 매핑할 수도 있습니다. 새의 최대 길이와 최소 길이를 보존 상태와 비교해 보세요:

```python
sns.kdeplot(data=filteredBirds, x="MinLength", y="MaxLength", hue="ConservationStatus")
```

![multiple densities, superimposed](../../../../3-Data-Visualization/10-visualization-distributions/images/multi.png)

'취약(Vulnerable)' 상태의 새들이 길이에 따라 클러스터링된 것이 의미가 있는지 연구할 가치가 있을지도 모릅니다.

## 🚀 도전 과제

히스토그램은 기본적인 산점도, 막대 차트, 선 차트보다 더 정교한 유형의 차트입니다. 인터넷에서 히스토그램 사용의 좋은 예를 찾아보세요. 히스토그램은 어떻게 사용되며, 무엇을 보여주고, 어떤 분야나 연구 영역에서 주로 사용되는지 조사해 보세요.

## [강의 후 퀴즈](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/19)

## 복습 및 자기 학습

이 강의에서는 Matplotlib를 사용하고 Seaborn을 시작하여 더 정교한 차트를 생성했습니다. Seaborn의 `kdeplot`에 대해 연구해 보세요. 이는 "하나 이상의 차원에서 연속적인 확률 밀도 곡선"을 생성합니다. [문서](https://seaborn.pydata.org/generated/seaborn.kdeplot.html)를 읽고 작동 방식을 이해하세요.

## 과제

[기술을 적용해 보세요](assignment.md)

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전을 권위 있는 출처로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 책임을 지지 않습니다.