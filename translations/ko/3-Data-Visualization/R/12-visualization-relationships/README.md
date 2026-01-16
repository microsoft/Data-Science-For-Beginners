<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a33c5d4b4156a2b41788d8720b6f724c",
  "translation_date": "2025-08-25T18:19:23+00:00",
  "source_file": "3-Data-Visualization/R/12-visualization-relationships/README.md",
  "language_code": "ko"
}
-->
# 관계 시각화: 꿀에 대한 모든 것 🍯

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../../sketchnotes/12-Visualizing-Relationships.png)|
|:---:|
|관계 시각화 - _스케치노트 by [@nitya](https://twitter.com/nitya)_ |

자연을 중심으로 한 연구를 계속하며, 다양한 꿀 종류 간의 관계를 보여주는 흥미로운 시각화를 탐구해 봅시다. 이 데이터셋은 [미국 농무부](https://www.nass.usda.gov/About_NASS/index.php)에서 제공된 자료를 기반으로 합니다.

약 600개의 항목으로 구성된 이 데이터셋은 미국 여러 주에서의 꿀 생산을 보여줍니다. 예를 들어, 주별로 꿀벌 군집 수, 군집당 생산량, 총 생산량, 재고, 파운드당 가격, 그리고 1998년부터 2012년까지 각 주에서 생산된 꿀의 가치를 연도별로 확인할 수 있습니다.

특정 주의 연간 생산량과 해당 주의 꿀 가격 간의 관계를 시각화하면 흥미로울 것입니다. 또는 주별 꿀벌 군집당 생산량 간의 관계를 시각화할 수도 있습니다. 이 기간은 2006년에 처음 관찰된 '꿀벌 군집 붕괴 현상(CCD)'(http://npic.orst.edu/envir/ccd.html)을 포함하므로, 연구하기에 의미 있는 데이터셋입니다. 🐝

## [강의 전 퀴즈](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/22)

이번 강의에서는 이전에 사용했던 ggplot2를 활용하여 변수 간의 관계를 시각화할 수 있습니다. 특히 ggplot2의 `geom_point`와 `qplot` 함수는 산점도와 선 그래프를 빠르게 생성하여 '[통계적 관계](https://ggplot2.tidyverse.org/)'를 시각화하는 데 유용합니다. 이를 통해 데이터 과학자는 변수 간의 관계를 더 잘 이해할 수 있습니다.

## 산점도

산점도를 사용하여 주별로 꿀 가격이 연도별로 어떻게 변화했는지 보여주세요. ggplot2의 `ggplot`과 `geom_point`를 사용하면 주 데이터를 편리하게 그룹화하고 범주형 및 숫자 데이터를 모두 표시할 수 있습니다.

먼저 데이터를 가져오고 Seaborn을 가져옵니다:

```r
honey=read.csv('../../data/honey.csv')
head(honey)
```
꿀 데이터에는 연도와 파운드당 가격을 포함하여 흥미로운 열이 여러 개 있습니다. 이를 미국 주별로 그룹화하여 탐색해 봅시다:

| state | numcol | yieldpercol | totalprod | stocks   | priceperlb | prodvalue | year |
| ----- | ------ | ----------- | --------- | -------- | ---------- | --------- | ---- |
| AL    | 16000  | 71          | 1136000   | 159000   | 0.72       | 818000    | 1998 |
| AZ    | 55000  | 60          | 3300000   | 1485000  | 0.64       | 2112000   | 1998 |
| AR    | 53000  | 65          | 3445000   | 1688000  | 0.59       | 2033000   | 1998 |
| CA    | 450000 | 83          | 37350000  | 12326000 | 0.62       | 23157000  | 1998 |
| CO    | 27000  | 72          | 1944000   | 1594000  | 0.7        | 1361000   | 1998 |
| FL    | 230000 | 98          |22540000   | 4508000  | 0.64       | 14426000  | 1998 |

꿀의 파운드당 가격과 미국 주 원산지 간의 관계를 보여주는 기본 산점도를 생성하세요. `y` 축을 충분히 높게 설정하여 모든 주를 표시하세요:

```r
library(ggplot2)
ggplot(honey, aes(x = priceperlb, y = state)) +
  geom_point(colour = "blue")
```
![scatterplot 1](../../../../../translated_images/ko/scatter1.86b8900674d88b26dd3353a83fe604e9ab3722c4680cc40ee9beb452ff02cdea.png)

이제 같은 데이터를 꿀 색상 테마로 표시하여 연도별로 가격이 어떻게 변화했는지 보여주세요. 이를 위해 'scale_color_gradientn' 매개변수를 추가하여 연도별 변화를 표시할 수 있습니다:

> ✅ [scale_color_gradientn](https://www.rdocumentation.org/packages/ggplot2/versions/0.9.1/topics/scale_colour_gradientn)에 대해 자세히 알아보세요 - 아름다운 무지개 색상 테마를 시도해 보세요!

```r
ggplot(honey, aes(x = priceperlb, y = state, color=year)) +
  geom_point()+scale_color_gradientn(colours = colorspace::heat_hcl(7))
```
![scatterplot 2](../../../../../translated_images/ko/scatter2.4d1cbc693bad20e2b563888747eb6bdf65b73ce449d903f7cd4068a78502dcff.png)

이 색상 테마 변경을 통해 꿀의 파운드당 가격이 연도별로 강한 상승 추세를 보이는 것을 명확히 확인할 수 있습니다. 실제로 데이터를 샘플링하여 확인해 보면(예: 애리조나 주) 연도별로 가격이 증가하는 패턴을 확인할 수 있으며, 예외는 거의 없습니다:

| state | numcol | yieldpercol | totalprod | stocks  | priceperlb | prodvalue | year |
| ----- | ------ | ----------- | --------- | ------- | ---------- | --------- | ---- |
| AZ    | 55000  | 60          | 3300000   | 1485000 | 0.64       | 2112000   | 1998 |
| AZ    | 52000  | 62          | 3224000   | 1548000 | 0.62       | 1999000   | 1999 |
| AZ    | 40000  | 59          | 2360000   | 1322000 | 0.73       | 1723000   | 2000 |
| AZ    | 43000  | 59          | 2537000   | 1142000 | 0.72       | 1827000   | 2001 |
| AZ    | 38000  | 63          | 2394000   | 1197000 | 1.08       | 2586000   | 2002 |
| AZ    | 35000  | 72          | 2520000   | 983000  | 1.34       | 3377000   | 2003 |
| AZ    | 32000  | 55          | 1760000   | 774000  | 1.11       | 1954000   | 2004 |
| AZ    | 36000  | 50          | 1800000   | 720000  | 1.04       | 1872000   | 2005 |
| AZ    | 30000  | 65          | 1950000   | 839000  | 0.91       | 1775000   | 2006 |
| AZ    | 30000  | 64          | 1920000   | 902000  | 1.26       | 2419000   | 2007 |
| AZ    | 25000  | 64          | 1600000   | 336000  | 1.26       | 2016000   | 2008 |
| AZ    | 20000  | 52          | 1040000   | 562000  | 1.45       | 1508000   | 2009 |
| AZ    | 24000  | 77          | 1848000   | 665000  | 1.52       | 2809000   | 2010 |
| AZ    | 23000  | 53          | 1219000   | 427000  | 1.55       | 1889000   | 2011 |
| AZ    | 22000  | 46          | 1012000   | 253000  | 1.79       | 1811000   | 2012 |

색상 대신 크기를 사용하여 이 변화를 시각화하는 또 다른 방법이 있습니다. 색맹 사용자에게는 이 방법이 더 나을 수 있습니다. 점의 크기를 증가시켜 가격 상승을 표시하도록 시각화를 수정하세요:

```r
ggplot(honey, aes(x = priceperlb, y = state)) +
  geom_point(aes(size = year),colour = "blue") +
  scale_size_continuous(range = c(0.25, 3))
```
점의 크기가 점차 증가하는 것을 확인할 수 있습니다.

![scatterplot 3](../../../../../translated_images/ko/scatter3.722d21e6f20b3ea2e18339bb9b10d75906126715eb7d5fdc88fe74dcb6d7066a.png)

이것이 단순히 수요와 공급의 문제일까요? 기후 변화와 꿀벌 군집 붕괴와 같은 요인으로 인해 구매 가능한 꿀이 연도별로 줄어들고, 그 결과 가격이 상승하는 것일까요?

이 데이터셋의 변수 간 상관관계를 발견하기 위해 선 그래프를 탐구해 봅시다.

## 선 그래프

질문: 꿀의 파운드당 가격이 연도별로 명확히 상승하고 있나요? 이를 가장 쉽게 확인할 수 있는 방법은 단일 선 그래프를 생성하는 것입니다:

```r
qplot(honey$year,honey$priceperlb, geom='smooth', span =0.5, xlab = "year",ylab = "priceperlb")
```
답변: 네, 2003년을 중심으로 몇 가지 예외가 있습니다:

![line chart 1](../../../../../translated_images/ko/line1.299b576fbb2a59e60a59e7130030f59836891f90302be084e4e8d14da0562e2a.png)

질문: 그렇다면 2003년에 꿀 공급량에서도 급증이 있었나요? 연도별 총 생산량을 살펴보면 어떨까요?

```python
qplot(honey$year,honey$totalprod, geom='smooth', span =0.5, xlab = "year",ylab = "totalprod")
```

![line chart 2](../../../../../translated_images/ko/line2.3b18fcda7176ceba5b6689eaaabb817d49c965e986f11cac1ae3f424030c34d8.png)

답변: 그렇지 않습니다. 총 생산량을 보면, 특정 연도에는 실제로 증가한 것으로 보이지만, 일반적으로 꿀 생산량은 이 기간 동안 감소하는 추세입니다.

질문: 그렇다면 2003년 꿀 가격 급등의 원인은 무엇일까요?

이를 알아내기 위해 Facet Grid를 탐구해 봅시다.

## Facet Grid

Facet Grid는 데이터셋의 한 측면(예: '연도')을 선택하여 너무 많은 Facet이 생성되지 않도록 합니다. Seaborn은 선택한 x 및 y 좌표에 대해 각 Facet에 대해 플롯을 생성하여 비교를 쉽게 할 수 있습니다. 2003년이 이러한 비교에서 두드러지게 나타날까요?

[ggplot2의 문서](https://ggplot2.tidyverse.org/reference/facet_wrap.html)에 따라 `facet_wrap`을 사용하여 Facet Grid를 생성하세요.

```r
ggplot(honey, aes(x=yieldpercol, y = numcol,group = 1)) + 
  geom_line() + facet_wrap(vars(year))
```
이 시각화에서는 꿀벌 군집당 생산량과 군집 수를 연도별로 나란히 비교할 수 있습니다. 열은 3으로 설정합니다:

![facet grid](../../../../../translated_images/ko/facet.491ad90d61c2a7cc69b50c929f80786c749e38217ccedbf1e22ed8909b65987c.png)

이 데이터셋에서는 연도별, 주별로 꿀벌 군집 수와 생산량에 관해 특별히 두드러지는 점은 없습니다. 이 두 변수 간 상관관계를 찾는 다른 방법이 있을까요?

## 이중 선 그래프

R의 `par`와 `plot` 함수를 사용하여 두 개의 선 그래프를 겹쳐서 표시하는 멀티라인 플롯을 시도해 보세요. x축에는 연도를 표시하고 두 개의 y축을 표시합니다. 꿀벌 군집당 생산량과 군집 수를 겹쳐서 표시합니다:

```r
par(mar = c(5, 4, 4, 4) + 0.3)              
plot(honey$year, honey$numcol, pch = 16, col = 2,type="l")              
par(new = TRUE)                             
plot(honey$year, honey$yieldpercol, pch = 17, col = 3,              
     axes = FALSE, xlab = "", ylab = "",type="l")
axis(side = 4, at = pretty(range(y2)))      
mtext("colony yield", side = 4, line = 3)   
```
![superimposed plots](../../../../../translated_images/ko/dual-line.fc4665f360a54018d7df9bc6abcc26460112e17dcbda18d3b9ae6109b32b36c3.png)

2003년을 중심으로 눈에 띄는 점은 없지만, 이 강의를 조금 더 긍정적인 노트로 마무리할 수 있습니다: 꿀벌 군집 수는 전반적으로 감소하고 있지만, 군집 수는 안정화되고 있으며 군집당 생산량은 감소하고 있습니다.

꿀벌들, 힘내라!

🐝❤️
## 🚀 도전 과제

이번 강의에서는 산점도와 선 그래프, Facet Grid를 포함한 다양한 시각화 방법에 대해 배웠습니다. 이전 강의에서 사용했던 다른 데이터셋을 사용하여 Facet Grid를 생성해 보세요. 이를 생성하는 데 걸리는 시간과 이러한 기술을 사용할 때 생성해야 할 Grid 수에 대해 신중해야 하는 점을 주목하세요.
## [강의 후 퀴즈](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/23)

## 복습 및 자기 학습

선 그래프는 간단하거나 매우 복잡할 수 있습니다. [ggplot2 문서](https://ggplot2.tidyverse.org/reference/geom_path.html#:~:text=geom_line()%20connects%20them%20in,which%20cases%20are%20connected%20together)를 읽으며 선 그래프를 생성하는 다양한 방법에 대해 알아보세요. 이번 강의에서 생성한 선 그래프를 문서에 나와 있는 다른 방법으로 개선해 보세요.
## 과제

[꿀벌의 세계로 뛰어들기](assignment.md)

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전을 권위 있는 출처로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 책임을 지지 않습니다.