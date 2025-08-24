<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ea67c0c40808fd723594de6896c37ccf",
  "translation_date": "2025-08-24T13:46:39+00:00",
  "source_file": "3-Data-Visualization/R/10-visualization-distributions/README.md",
  "language_code": "ko"
}
-->
# 분포 시각화

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/sketchnotes/10-Visualizing-Distributions.png)|
|:---:|
| 분포 시각화 - _스케치노트 by [@nitya](https://twitter.com/nitya)_ |

이전 강의에서, 미네소타의 새들에 대한 데이터셋에서 흥미로운 사실들을 배웠습니다. 이상치를 시각화하여 오류 데이터를 발견하고, 새 카테고리 간 최대 길이의 차이를 살펴보았습니다.

## [강의 전 퀴즈](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/18)
## 새 데이터셋 탐색하기

데이터를 탐구하는 또 다른 방법은 데이터가 축을 따라 어떻게 조직되어 있는지, 즉 분포를 살펴보는 것입니다. 예를 들어, 미네소타 새들의 최대 날개 길이나 최대 몸무게의 일반적인 분포를 알고 싶을 수도 있습니다.

이 데이터셋의 분포에 대한 몇 가지 사실을 알아봅시다. R 콘솔에서 `ggplot2`와 데이터베이스를 가져오세요. 이전 주제에서 했던 것처럼 데이터베이스에서 이상치를 제거하세요.

```r
library(ggplot2)

birds <- read.csv("../../data/birds.csv",fileEncoding="UTF-8-BOM")

birds_filtered <- subset(birds, MaxWingspan < 500)
head(birds_filtered)
```
|      | 이름                          | 학명                   | 카테고리              | 목          | 과       | 속          | 보존 상태         | 최소 길이 | 최대 길이 | 최소 몸무게 | 최대 몸무게 | 최소 날개 길이 | 최대 날개 길이 |
| ---: | :--------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :----------------- | --------: | --------: | ----------: | ----------: | ----------: | ----------: |
|    0 | 검은배 휘파람오리             | Dendrocygna autumnalis | 오리/기러기/물새      | Anseriformes | Anatidae | Dendrocygna | LC                 |        47 |        56 |         652 |        1020 |          76 |          94 |
|    1 | 황갈색 휘파람오리             | Dendrocygna bicolor    | 오리/기러기/물새      | Anseriformes | Anatidae | Dendrocygna | LC                 |        45 |        53 |         712 |        1050 |          85 |          93 |
|    2 | 흰기러기                     | Anser caerulescens     | 오리/기러기/물새      | Anseriformes | Anatidae | Anser       | LC                 |        64 |        79 |        2050 |        4050 |         135 |         165 |
|    3 | 로스기러기                   | Anser rossii           | 오리/기러기/물새      | Anseriformes | Anatidae | Anser       | LC                 |      57.3 |        64 |        1066 |        1567 |         113 |         116 |
|    4 | 큰흰이마기러기               | Anser albifrons        | 오리/기러기/물새      | Anseriformes | Anatidae | Anser       | LC                 |        64 |        81 |        1930 |        3310 |         130 |         165 |

일반적으로, 데이터가 어떻게 분포되어 있는지 빠르게 확인하려면 이전 강의에서 했던 것처럼 산점도를 사용할 수 있습니다:

```r
ggplot(data=birds_filtered, aes(x=Order, y=MaxLength,group=1)) +
  geom_point() +
  ggtitle("Max Length per order") + coord_flip()
```
![목별 최대 길이](../../../../../3-Data-Visualization/R/10-visualization-distributions/images/max-length-per-order.png)

이 산점도는 새 목(Order)별 몸 길이의 일반적인 분포를 보여주지만, 실제 분포를 표시하기에는 최적의 방법이 아닙니다. 이 작업은 일반적으로 히스토그램을 생성하여 수행됩니다.

## 히스토그램 작업하기

`ggplot2`는 히스토그램을 사용하여 데이터 분포를 시각화하는 데 매우 유용한 방법을 제공합니다. 이 차트는 막대 차트와 비슷하며, 막대의 상승과 하강을 통해 분포를 볼 수 있습니다. 히스토그램을 생성하려면 숫자 데이터를 사용해야 합니다. 히스토그램을 생성하려면 차트 유형을 'hist'로 정의하여 차트를 그릴 수 있습니다. 이 차트는 데이터셋의 전체 범위에 대한 MaxBodyMass의 분포를 보여줍니다. 데이터 배열을 더 작은 범위로 나누어 데이터 값의 분포를 표시할 수 있습니다:

```r
ggplot(data = birds_filtered, aes(x = MaxBodyMass)) + 
  geom_histogram(bins=10)+ylab('Frequency')
```
![전체 데이터셋 분포](../../../../../3-Data-Visualization/R/10-visualization-distributions/images/distribution-over-the-entire-dataset.png)

보시다시피, 이 데이터셋에 포함된 400개 이상의 새들 중 대부분은 Max Body Mass가 2000 이하 범위에 속합니다. `bins` 매개변수를 30과 같은 더 높은 숫자로 변경하여 데이터를 더 자세히 살펴보세요:

```r
ggplot(data = birds_filtered, aes(x = MaxBodyMass)) + geom_histogram(bins=30)+ylab('Frequency')
```

![30개의 bins 분포](../../../../../3-Data-Visualization/R/10-visualization-distributions/images/distribution-30bins.png)

이 차트는 분포를 조금 더 세부적으로 보여줍니다. 왼쪽으로 덜 치우친 차트를 생성하려면 특정 범위 내의 데이터만 선택하도록 설정할 수 있습니다:

몸무게가 60 이하인 새들만 필터링하고 30개의 `bins`를 표시하세요:

```r
birds_filtered_1 <- subset(birds_filtered, MaxBodyMass > 1 & MaxBodyMass < 60)
ggplot(data = birds_filtered_1, aes(x = MaxBodyMass)) + 
  geom_histogram(bins=30)+ylab('Frequency')
```

![필터링된 히스토그램](../../../../../3-Data-Visualization/R/10-visualization-distributions/images/filtered-histogram.png)

✅ 다른 필터와 데이터 포인트를 시도해보세요. 데이터의 전체 분포를 보려면 `['MaxBodyMass']` 필터를 제거하여 라벨이 있는 분포를 표시하세요.

히스토그램은 색상과 라벨을 개선할 수 있는 멋진 기능도 제공합니다:

두 분포 간의 관계를 비교하기 위해 2D 히스토그램을 생성하세요. `MaxBodyMass`와 `MaxLength`를 비교해봅시다. `ggplot2`는 더 밝은 색상을 사용하여 수렴을 표시하는 내장 기능을 제공합니다:

```r
ggplot(data=birds_filtered_1, aes(x=MaxBodyMass, y=MaxLength) ) +
  geom_bin2d() +scale_fill_continuous(type = "viridis")
```
이 두 요소가 예상 축을 따라 예상되는 상관관계를 가지며, 특히 강한 수렴 지점이 하나 있습니다:

![2D 플롯](../../../../../3-Data-Visualization/R/10-visualization-distributions/images/2d-plot.png)

히스토그램은 기본적으로 숫자 데이터에 잘 작동합니다. 텍스트 데이터에 따라 분포를 확인해야 한다면 어떻게 해야 할까요?

## 텍스트 데이터를 사용하여 데이터셋의 분포 탐색하기

이 데이터셋에는 새의 카테고리, 속, 종, 과뿐만 아니라 보존 상태에 대한 유용한 정보도 포함되어 있습니다. 이 보존 정보를 탐구해봅시다. 새들의 보존 상태에 따른 분포는 어떻게 될까요?

> ✅ 데이터셋에는 보존 상태를 설명하는 몇 가지 약어가 사용됩니다. 이 약어들은 [IUCN 적색 목록 카테고리](https://www.iucnredlist.org/)에서 가져온 것으로, 종의 상태를 분류하는 조직입니다.
> 
> - CR: 심각한 멸종 위기
> - EN: 멸종 위기
> - EX: 멸종
> - LC: 관심 필요 없음
> - NT: 근접 위협
> - VU: 취약

이 값들은 텍스트 기반이므로 히스토그램을 생성하려면 변환이 필요합니다. 필터링된 새 데이터프레임을 사용하여 보존 상태와 최소 날개 길이를 함께 표시하세요. 무엇을 발견할 수 있나요?

```r
birds_filtered_1$ConservationStatus[birds_filtered_1$ConservationStatus == 'EX'] <- 'x1' 
birds_filtered_1$ConservationStatus[birds_filtered_1$ConservationStatus == 'CR'] <- 'x2'
birds_filtered_1$ConservationStatus[birds_filtered_1$ConservationStatus == 'EN'] <- 'x3'
birds_filtered_1$ConservationStatus[birds_filtered_1$ConservationStatus == 'NT'] <- 'x4'
birds_filtered_1$ConservationStatus[birds_filtered_1$ConservationStatus == 'VU'] <- 'x5'
birds_filtered_1$ConservationStatus[birds_filtered_1$ConservationStatus == 'LC'] <- 'x6'

ggplot(data=birds_filtered_1, aes(x = MinWingspan, fill = ConservationStatus)) +
  geom_histogram(position = "identity", alpha = 0.4, bins = 20) +
  scale_fill_manual(name="Conservation Status",values=c("red","green","blue","pink"),labels=c("Endangered","Near Threathened","Vulnerable","Least Concern"))
```

![날개 길이와 보존 상태](../../../../../3-Data-Visualization/R/10-visualization-distributions/images/wingspan-conservation-collation.png)

최소 날개 길이와 보존 상태 간에 뚜렷한 상관관계는 없는 것 같습니다. 이 방법을 사용하여 데이터셋의 다른 요소를 테스트해보세요. 다른 필터를 시도해보세요. 상관관계를 발견할 수 있나요?

## 밀도 플롯

지금까지 살펴본 히스토그램은 '단계적'이며 부드럽게 흐르지 않습니다. 더 부드러운 밀도 차트를 표시하려면 밀도 플롯을 시도할 수 있습니다.

이제 밀도 플롯을 작업해봅시다!

```r
ggplot(data = birds_filtered_1, aes(x = MinWingspan)) + 
  geom_density()
```
![밀도 플롯](../../../../../3-Data-Visualization/R/10-visualization-distributions/images/density-plot.png)

이 플롯은 이전의 최소 날개 길이 데이터에 대한 플롯을 반영하며, 조금 더 부드럽게 표현됩니다. 두 번째로 생성한 MaxBodyMass의 울퉁불퉁한 선을 이 방법을 사용하여 매우 부드럽게 재생성할 수 있습니다:

```r
ggplot(data = birds_filtered_1, aes(x = MaxBodyMass)) + 
  geom_density()
```
![몸무게 밀도](../../../../../3-Data-Visualization/R/10-visualization-distributions/images/bodymass-smooth.png)

너무 부드럽지 않은 선을 원한다면 `adjust` 매개변수를 수정하세요:

```r
ggplot(data = birds_filtered_1, aes(x = MaxBodyMass)) + 
  geom_density(adjust = 1/5)
```
![덜 부드러운 몸무게](../../../../../3-Data-Visualization/R/10-visualization-distributions/images/less-smooth-bodymass.png)

✅ 이 유형의 플롯에 사용할 수 있는 매개변수에 대해 읽어보고 실험해보세요!

이 유형의 차트는 설명력이 뛰어난 시각화를 제공합니다. 예를 들어, 몇 줄의 코드로 새 목(Order)별 최대 몸무게 밀도를 표시할 수 있습니다:

```r
ggplot(data=birds_filtered_1,aes(x = MaxBodyMass, fill = Order)) +
  geom_density(alpha=0.5)
```
![목별 몸무게](../../../../../3-Data-Visualization/R/10-visualization-distributions/images/bodymass-per-order.png)

## 🚀 도전 과제

히스토그램은 기본적인 산점도, 막대 차트, 선 차트보다 더 정교한 유형의 차트입니다. 인터넷에서 히스토그램 사용 사례를 찾아보세요. 히스토그램은 어떻게 사용되며, 무엇을 보여주고, 어떤 분야나 연구 영역에서 주로 사용되는지 조사해보세요.

## [강의 후 퀴즈](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/19)

## 복습 및 자기 학습

이 강의에서는 `ggplot2`를 사용하여 더 정교한 차트를 생성하기 시작했습니다. `geom_density_2d()`에 대해 조사해보세요. 이는 "하나 이상의 차원에서 연속적인 확률 밀도 곡선"을 생성합니다. [문서](https://ggplot2.tidyverse.org/reference/geom_density_2d.html)를 읽고 작동 방식을 이해하세요.

## 과제

[기술을 적용해보세요](assignment.md)

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전을 권위 있는 출처로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 책임을 지지 않습니다.