<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "22acf28f518a4769ea14fa42f4734b9f",
  "translation_date": "2025-08-25T18:25:14+00:00",
  "source_file": "3-Data-Visualization/R/09-visualization-quantities/README.md",
  "language_code": "ko"
}
-->
# 수량 시각화
|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/sketchnotes/09-Visualizing-Quantities.png)|
|:---:|
| 수량 시각화 - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

이 강의에서는 다양한 R 패키지 라이브러리를 사용하여 수량 개념을 중심으로 흥미로운 시각화를 만드는 방법을 탐구합니다. 미네소타의 새들에 대한 정리된 데이터셋을 사용하여 지역 야생 동물에 대한 많은 흥미로운 사실을 배울 수 있습니다.  
## [강의 전 퀴즈](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/16)

## ggplot2로 날개 길이 관찰하기
다양한 종류의 간단하고 정교한 플롯과 차트를 만드는 데 탁월한 라이브러리는 [ggplot2](https://cran.r-project.org/web/packages/ggplot2/index.html)입니다. 일반적으로 이러한 라이브러리를 사용하여 데이터를 시각화하는 과정은 데이터프레임에서 대상 부분을 식별하고, 필요한 데이터 변환을 수행하며, x축과 y축 값을 할당하고, 표시할 플롯 유형을 결정한 다음 플롯을 표시하는 것을 포함합니다.

`ggplot2`는 그래픽을 선언적으로 생성하는 시스템으로, The Grammar of Graphics에 기반을 둡니다. [Grammar of Graphics](https://en.wikipedia.org/wiki/Ggplot2)는 데이터 시각화를 위한 일반적인 체계로, 그래프를 스케일과 레이어 같은 의미적 구성 요소로 나눕니다. 즉, 적은 코드로 단변량 또는 다변량 데이터의 플롯과 그래프를 쉽게 생성할 수 있어 `ggplot2`는 R에서 가장 인기 있는 시각화 패키지입니다. 사용자는 `ggplot2`에 변수와 그래픽 속성을 어떻게 매핑할지, 사용할 그래픽 기본 요소를 알려주면 나머지는 `ggplot2`가 처리합니다.

> ✅ 플롯 = 데이터 + 미학 + 기하학
> - 데이터: 데이터셋을 의미합니다.
> - 미학: 연구할 변수(x와 y 변수)를 나타냅니다.
> - 기하학: 플롯 유형(선형 플롯, 막대 플롯 등)을 나타냅니다.

데이터와 플롯을 통해 전달하려는 이야기에 따라 가장 적합한 기하학(플롯 유형)을 선택하세요.

> - 추세 분석: 선형, 세로 막대
> - 값 비교: 막대, 세로 막대, 원형, 산점도
> - 부분과 전체의 관계: 원형
> - 데이터 분포 표시: 산점도, 막대
> - 값 간 관계 표시: 선형, 산점도, 버블

✅ 이 [cheatsheet](https://nyu-cdsc.github.io/learningr/assets/data-visualization-2.1.pdf)를 참고하여 ggplot2에 대한 설명을 확인할 수 있습니다.

## 새의 날개 길이 값을 기반으로 선형 플롯 만들기

R 콘솔을 열고 데이터셋을 가져옵니다.  
> 참고: 데이터셋은 이 저장소의 `/data` 폴더에 저장되어 있습니다.

데이터셋을 가져오고 데이터의 헤드(상위 5개 행)를 관찰해 봅시다.

```r
birds <- read.csv("../../data/birds.csv",fileEncoding="UTF-8-BOM")
head(birds)
```  
데이터의 헤드는 텍스트와 숫자가 혼합되어 있습니다:

|      | Name                         | ScientificName         | Category              | Order        | Family   | Genus       | ConservationStatus | MinLength | MaxLength | MinBodyMass | MaxBodyMass | MinWingspan | MaxWingspan |
| ---: | :--------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :----------------- | --------: | --------: | ----------: | ----------: | ----------: | ----------: |
|    0 | Black-bellied whistling-duck | Dendrocygna autumnalis | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Dendrocygna | LC                 |        47 |        56 |         652 |        1020 |          76 |          94 |
|    1 | Fulvous whistling-duck       | Dendrocygna bicolor    | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Dendrocygna | LC                 |        45 |        53 |         712 |        1050 |          85 |          93 |
|    2 | Snow goose                   | Anser caerulescens     | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Anser       | LC                 |        64 |        79 |        2050 |        4050 |         135 |         165 |
|    3 | Ross's goose                 | Anser rossii           | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Anser       | LC                 |      57.3 |        64 |        1066 |        1567 |         113 |         116 |
|    4 | Greater white-fronted goose  | Anser albifrons        | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Anser       | LC                 |        64 |        81 |        1930 |        3310 |         130 |         165 |

이 흥미로운 새들의 최대 날개 길이를 시각화하는 기본 선형 플롯을 그려봅시다.

```r
install.packages("ggplot2")
library("ggplot2")
ggplot(data=birds, aes(x=Name, y=MaxWingspan,group=1)) +
  geom_line() 
```  
여기서는 `ggplot2` 패키지를 설치한 후 `library("ggplot2")` 명령을 사용하여 작업 공간에 가져옵니다. ggplot에서 플롯을 그리려면 `ggplot()` 함수를 사용하며 데이터셋, x 및 y 변수 등을 속성으로 지정합니다. 이 경우 선형 플롯을 그리기 위해 `geom_line()` 함수를 사용합니다.

![MaxWingspan-lineplot](../../../../../translated_images/ko/MaxWingspan-lineplot.b12169f99d26fdd263f291008dfd73c18a4ba8f3d32b1fda3d74af51a0a28616.png)

즉시 눈에 띄는 점은 무엇인가요? 적어도 하나의 이상치가 있는 것 같습니다. 2000cm 이상의 날개 길이는 20미터가 넘습니다. 미네소타에 프테로닥틸이 살고 있는 걸까요? 조사해 봅시다.

엑셀에서 빠르게 정렬하여 이러한 이상치를 찾을 수도 있지만, 플롯 내에서 작업을 계속하며 시각화 과정을 진행해 봅시다.

x축에 레이블을 추가하여 어떤 종류의 새들이 있는지 표시해 봅시다:

```r
ggplot(data=birds, aes(x=Name, y=MaxWingspan,group=1)) +
  geom_line() +
  theme(axis.text.x = element_text(angle = 45, hjust=1))+
  xlab("Birds") +
  ylab("Wingspan (CM)") +
  ggtitle("Max Wingspan in Centimeters")
```  
`theme`에서 각도를 지정하고 `xlab()`과 `ylab()`에서 x축과 y축 레이블을 지정합니다. `ggtitle()`은 그래프/플롯에 이름을 부여합니다.

![MaxWingspan-lineplot-improved](../../../../../translated_images/ko/MaxWingspan-lineplot-improved.04b73b4d5a59552a6bc7590678899718e1f065abe9eada9ebb4148939b622fd4.png)

레이블을 45도 회전시켰음에도 불구하고 읽기에는 너무 많습니다. 다른 전략을 시도해 봅시다: 이상치만 레이블을 지정하고 차트 내에서 레이블을 설정합니다. 산점도를 사용하여 레이블링 공간을 더 확보할 수 있습니다:

```r
ggplot(data=birds, aes(x=Name, y=MaxWingspan,group=1)) +
  geom_point() +
  geom_text(aes(label=ifelse(MaxWingspan>500,as.character(Name),'')),hjust=0,vjust=0) + 
  theme(axis.title.x=element_blank(), axis.text.x=element_blank(), axis.ticks.x=element_blank())
  ylab("Wingspan (CM)") +
  ggtitle("Max Wingspan in Centimeters") + 
```  
여기서 무슨 일이 일어나고 있나요? `geom_point()` 함수를 사용하여 산점도를 그렸습니다. 이를 통해 `MaxWingspan > 500`인 새들에 대한 레이블을 추가하고 x축 레이블을 숨겨 플롯을 깔끔하게 정리했습니다.

무엇을 발견했나요?

![MaxWingspan-scatterplot](../../../../../translated_images/ko/MaxWingspan-scatterplot.60dc9e0e19d32700283558f253841fdab5104abb62bc96f7d97f9c0ee857fa8b.png)

## 데이터 필터링

Bald Eagle과 Prairie Falcon은 아마도 매우 큰 새일 가능성이 높지만, 최대 날개 길이에 0이 추가된 잘못된 레이블로 보입니다. 25미터 날개 길이를 가진 Bald Eagle을 만날 가능성은 낮지만, 만약 그렇다면 꼭 알려주세요! 이 두 이상치를 제외한 새로운 데이터프레임을 만들어 봅시다:

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
새로운 데이터프레임 `birds_filtered`를 만들고 산점도를 그렸습니다. 이상치를 필터링함으로써 데이터가 더 일관되고 이해하기 쉬워졌습니다.

![MaxWingspan-scatterplot-improved](../../../../../translated_images/ko/MaxWingspan-scatterplot-improved.7d0af81658c65f3e75b8fedeb2335399e31108257e48db15d875ece608272051.png)

이제 날개 길이에 관한 데이터가 더 깨끗해졌으니, 이 새들에 대해 더 알아봅시다.

선형 플롯과 산점도는 데이터 값과 분포에 대한 정보를 표시할 수 있지만, 이 데이터셋에 내재된 값을 고려해 봐야 합니다. 다음과 같은 수량에 대한 질문을 시각화하여 답을 찾을 수 있습니다:

> 새의 카테고리는 몇 가지이며, 각각의 수는 얼마나 될까요?  
> 멸종, 위기, 희귀, 일반적인 새는 몇 마리인가요?  
> 린네의 용어로 다양한 속(genus)과 목(order)은 몇 가지인가요?  
## 막대 차트 탐구하기

막대 차트는 데이터를 그룹화하여 보여줄 때 실용적입니다. 이 데이터셋에 존재하는 새의 카테고리를 탐구하여 가장 일반적인 카테고리를 확인해 봅시다. 필터링된 데이터를 사용하여 막대 차트를 만들어 봅시다.

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
다음 코드 스니펫에서는 데이터를 조작하고 그룹화하여 누적 막대 차트를 그리기 위해 [dplyr](https://www.rdocumentation.org/packages/dplyr/versions/0.7.8)과 [lubridate](https://www.rdocumentation.org/packages/lubridate/versions/1.8.0) 패키지를 설치합니다. 먼저 새의 `Category`로 데이터를 그룹화한 후 `MinLength`, `MaxLength`, `MinBodyMass`, `MaxBodyMass`, `MinWingspan`, `MaxWingspan` 열을 요약합니다. 그런 다음 `ggplot2` 패키지를 사용하여 막대 차트를 그리고 각 카테고리에 대한 색상과 레이블을 지정합니다.

![Stacked bar chart](../../../../../translated_images/ko/stacked-bar-chart.0c92264e89da7b391a7490224d1e7059a020e8b74dcd354414aeac78871c02f1.png)

하지만 이 막대 차트는 너무 많은 비그룹화된 데이터로 인해 읽기 어렵습니다. 플롯하려는 데이터만 선택해야 합니다. 새의 카테고리를 기준으로 길이를 살펴봅시다.

데이터를 새의 카테고리만 포함하도록 필터링합니다.

카테고리가 많으므로 이 차트를 세로로 표시하고 모든 데이터를 표시할 수 있도록 높이를 조정합니다:

```r
birds_count<-dplyr::count(birds_filtered, Category, sort = TRUE)
birds_count$Category <- factor(birds_count$Category, levels = birds_count$Category)
ggplot(birds_count,aes(Category,n))+geom_bar(stat="identity")+coord_flip()
```  
먼저 `Category` 열의 고유 값을 계산한 후 이를 새 데이터프레임 `birds_count`로 정렬합니다. 이 정렬된 데이터를 동일한 수준으로 팩터링하여 정렬된 방식으로 플롯됩니다. 그런 다음 `ggplot2`를 사용하여 데이터를 막대 차트로 플롯합니다. `coord_flip()`은 수평 막대를 플롯합니다.

![category-length](../../../../../translated_images/ko/category-length.7e34c296690e85d64f7e4d25a56077442683eca96c4f5b4eae120a64c0755636.png)

이 막대 차트는 각 카테고리의 새 수를 잘 보여줍니다. 한눈에 미네소타 지역에서 가장 많은 새가 Ducks/Geese/Waterfowl 카테고리에 속한다는 것을 알 수 있습니다. 미네소타는 '10,000개의 호수의 땅'이므로 놀랍지 않습니다!

✅ 이 데이터셋에서 다른 카운트를 시도해 보세요. 놀라운 점이 있나요?

## 데이터 비교

새로운 축을 생성하여 그룹화된 데이터의 다양한 비교를 시도할 수 있습니다. 새의 카테고리를 기준으로 MaxLength를 비교해 봅시다:

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
`birds_filtered` 데이터를 `Category`로 그룹화한 후 막대 그래프를 플롯합니다.

![comparing data](../../../../../translated_images/ko/comparingdata.f486a450d61c7ca5416f27f3f55a6a4465d00df3be5e6d33936e9b07b95e2fdd.png)

여기서 놀라운 점은 없습니다: 벌새는 펠리컨이나 기러기에 비해 MaxLength가 가장 적습니다. 데이터가 논리적으로 맞아떨어지는 것은 좋은 일입니다!

막대 차트를 더 흥미롭게 만들기 위해 데이터를 중첩하여 표시할 수 있습니다. 특정 새 카테고리에서 최소 및 최대 길이를 중첩하여 표시해 봅시다:

```r
ggplot(data=birds_grouped, aes(x=Category)) +
  geom_bar(aes(y=MaxLength), stat="identity", position ="identity",  fill='blue') +
  geom_bar(aes(y=MinLength), stat="identity", position="identity", fill='orange')+
  coord_flip()
```  
![super-imposed values](../../../../../translated_images/ko/superimposed-values.5363f0705a1da4167625a373a1064331ea3cb7a06a297297d0734fcc9b3819a0.png)

## 🚀 도전 과제

이 새 데이터셋은 특정 생태계 내 다양한 새 유형에 대한 풍부한 정보를 제공합니다. 인터넷을 검색하여 다른 새 관련 데이터셋을 찾아보세요. 이러한 새를 중심으로 차트와 그래프를 만들어 보며 몰랐던 사실을 발견해 보세요.  
## [강의 후 퀴즈](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/17)

## 복습 및 자기 학습

이 첫 번째 강의에서는 `ggplot2`를 사용하여 수량을 시각화하는 방법에 대한 정보를 제공했습니다. 데이터셋을 시각화하기 위한 다른 방법에 대해 연구해 보세요. [Lattice](https://stat.ethz.ch/R-manual/R-devel/library/lattice/html/Lattice.html) 및 [Plotly](https://github.com/plotly/plotly.R#readme)와 같은 패키지를 사용하여 시각화할 수 있는 데이터셋을 찾아보세요.

## 과제
[Lines, Scatters, and Bars](assignment.md)  

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전이 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 책임을 지지 않습니다.