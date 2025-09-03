<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3a34157cc63516eba97c89a0b2f8c3e6",
  "translation_date": "2025-09-03T21:04:24+00:00",
  "source_file": "1-Introduction/02-ethics/README.md",
  "language_code": "ko"
}
-->
# 데이터 윤리 소개

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/02-Ethics.png)|
|:---:|
| 데이터 과학 윤리 - _스케치노트 by [@nitya](https://twitter.com/nitya)_ |

---

우리는 모두 데이터화된 세상에서 살아가는 데이터 시민입니다.

시장 동향에 따르면 2022년까지 대규모 조직의 3분의 1이 온라인 [마켓플레이스와 거래소](https://www.gartner.com/smarterwithgartner/gartner-top-10-trends-in-data-and-analytics-for-2020/)를 통해 데이터를 사고팔게 될 것이라고 합니다. **앱 개발자**로서 우리는 데이터 기반 통찰력과 알고리즘 기반 자동화를 일상적인 사용자 경험에 통합하는 것이 더 쉽고 저렴해질 것입니다. 그러나 AI가 널리 퍼지면서, 대규모로 이러한 알고리즘이 [무기화](https://www.youtube.com/watch?v=TQHs8SA1qpk)될 때 발생할 수 있는 잠재적 피해를 이해해야 할 필요도 생깁니다.

또한, 2025년까지 [180제타바이트](https://www.statista.com/statistics/871513/worldwide-data-created/) 이상의 데이터를 생성하고 소비할 것이라는 전망도 있습니다. **데이터 과학자**로서 이는 개인 데이터에 대한 전례 없는 접근을 가능하게 합니다. 이를 통해 사용자 행동 프로파일을 구축하고, 사용자가 자유롭게 선택하는 것처럼 보이게 하면서도 우리가 선호하는 결과로 유도할 수 있습니다. 이는 데이터 프라이버시와 사용자 보호에 대한 더 넓은 질문을 제기합니다.

데이터 윤리는 데이터 과학과 엔지니어링의 _필수적인 가드레일_로, 데이터 기반 행동으로 인해 발생할 수 있는 잠재적 피해와 의도치 않은 결과를 최소화하는 데 도움을 줍니다. [Gartner의 AI 하이프 사이클](https://www.gartner.com/smarterwithgartner/2-megatrends-dominate-the-gartner-hype-cycle-for-artificial-intelligence-2020/)은 디지털 윤리, 책임 있는 AI, AI 거버넌스와 같은 관련 트렌드를 AI의 _민주화_와 _산업화_라는 더 큰 메가트렌드의 주요 동력으로 식별합니다.

![Gartner의 AI 하이프 사이클 - 2020](https://images-cdn.newscred.com/Zz1mOWJhNzlkNDA2ZTMxMWViYjRiOGFiM2IyMjQ1YmMwZQ==)

이 강의에서는 데이터 윤리의 핵심 개념과 도전 과제, 사례 연구, 거버넌스와 같은 적용된 AI 개념을 탐구하여 데이터와 AI를 다루는 팀과 조직에서 윤리 문화를 구축하는 방법을 알아볼 것입니다.

## [강의 전 퀴즈](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/2) 🎯

## 기본 정의

먼저 기본 용어를 이해해 봅시다.

"윤리"라는 단어는 [그리스어 "ethikos"](https://en.wikipedia.org/wiki/Ethics) (그리고 그 뿌리인 "ethos")에서 유래했으며, 이는 _성격 또는 도덕적 본질_을 의미합니다.

**윤리**는 사회에서 우리의 행동을 지배하는 공유된 가치와 도덕적 원칙에 관한 것입니다. 윤리는 법이 아니라 "옳고 그름"에 대한 널리 받아들여지는 규범에 기반을 둡니다. 그러나 윤리적 고려는 기업 거버넌스 이니셔티브와 정부 규정을 통해 준수를 위한 더 많은 인센티브를 창출할 수 있습니다.

**데이터 윤리**는 "_데이터, 알고리즘 및 관련 관행_"과 관련된 도덕적 문제를 "연구하고 평가"하는 [윤리의 새로운 분야](https://royalsocietypublishing.org/doi/full/10.1098/rsta.2016.0360#sec-1)입니다. 여기서 **"데이터"**는 생성, 기록, 큐레이션, 처리, 배포, 공유 및 사용과 관련된 행동에 초점을 맞추고, **"알고리즘"**은 AI, 에이전트, 머신러닝 및 로봇에 초점을 맞추며, **"관행"**은 책임 있는 혁신, 프로그래밍, 해킹 및 윤리 코드와 같은 주제에 초점을 맞춥니다.

**응용 윤리**는 [도덕적 고려의 실질적 적용](https://en.wikipedia.org/wiki/Applied_ethics)을 의미합니다. 이는 _현실 세계의 행동, 제품 및 프로세스_와 관련된 윤리적 문제를 적극적으로 조사하고, 정의된 윤리적 가치와 일치하도록 유지하기 위해 수정 조치를 취하는 과정입니다.

**윤리 문화**는 [_응용 윤리를 운영화_](https://hbr.org/2019/05/how-to-design-an-ethical-organization)하여 윤리적 원칙과 관행이 조직 전체에서 일관되고 확장 가능하게 채택되도록 하는 것입니다. 성공적인 윤리 문화는 조직 전체의 윤리적 원칙을 정의하고, 준수를 위한 의미 있는 인센티브를 제공하며, 조직의 모든 수준에서 원하는 행동을 장려하고 증폭함으로써 윤리적 규범을 강화합니다.

## 윤리 개념

이 섹션에서는 데이터 윤리를 위한 **공유된 가치**(원칙)와 **윤리적 도전 과제**(문제)와 같은 개념을 논의하고, 이러한 개념을 현실 세계의 맥락에서 이해할 수 있도록 돕는 **사례 연구**를 탐구할 것입니다.

### 1. 윤리 원칙

모든 데이터 윤리 전략은 _윤리적 원칙_을 정의하는 것으로 시작됩니다. 이는 데이터 및 AI 프로젝트에서 허용 가능한 행동을 설명하고, 준수 행동을 안내하는 "공유된 가치"입니다. 개인 또는 팀 수준에서 이를 정의할 수 있습니다. 그러나 대부분의 대규모 조직은 이를 기업 수준에서 정의하고 모든 팀에 일관되게 시행되는 _윤리적 AI_ 미션 선언문 또는 프레임워크에 포함시킵니다.

**예시:** Microsoft의 [책임 있는 AI](https://www.microsoft.com/en-us/ai/responsible-ai) 미션 선언문은 _"우리는 사람을 우선으로 하는 윤리적 원칙에 의해 추진되는 AI 발전에 전념합니다"_라고 읽으며, 아래 프레임워크에서 6가지 윤리적 원칙을 식별합니다:

![Microsoft의 책임 있는 AI](https://docs.microsoft.com/en-gb/azure/cognitive-services/personalizer/media/ethics-and-responsible-use/ai-values-future-computed.png)

이 원칙들을 간단히 살펴보겠습니다. _투명성_과 _책임성_은 다른 원칙들이 기반을 두는 기초적인 가치입니다. 따라서 여기서부터 시작해 봅시다:

* [**책임성**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6)은 실무자가 데이터 및 AI 운영과 이러한 윤리적 원칙 준수에 대해 _책임을 지도록_ 합니다.
* [**투명성**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6)은 데이터와 AI 행동이 사용자에게 _이해 가능_하도록 하여 결정의 이유와 과정을 설명합니다.
* [**공정성**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1%3aprimaryr6)은 AI가 _모든 사람_을 공정하게 대우하도록 하며, 데이터와 시스템에서 발생할 수 있는 체계적 또는 암묵적 사회-기술적 편향을 해결합니다.
* [**신뢰성 및 안전성**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6)은 AI가 정의된 가치에 따라 _일관되게_ 행동하며, 잠재적 피해나 의도치 않은 결과를 최소화합니다.
* [**프라이버시 및 보안**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6)은 데이터 계보를 이해하고 사용자에게 _데이터 프라이버시 및 관련 보호_를 제공하는 것입니다.
* [**포용성**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6)은 AI 솔루션을 의도적으로 설계하여 _다양한 인간의 필요와 능력_을 충족하도록 적응시키는 것입니다.

> 🚨 여러분의 데이터 윤리 미션 선언문은 무엇일 수 있을지 생각해 보세요. 다른 조직의 윤리적 AI 프레임워크를 탐구해 보세요. 여기에는 [IBM](https://www.ibm.com/cloud/learn/ai-ethics), [Google](https://ai.google/principles), [Facebook](https://ai.facebook.com/blog/facebooks-five-pillars-of-responsible-ai/)의 예시가 포함됩니다. 이들이 공통적으로 가지고 있는 공유된 가치는 무엇인가요? 이러한 원칙은 그들이 운영하는 AI 제품 또는 산업과 어떻게 관련이 있나요?

### 2. 윤리적 도전 과제

윤리적 원칙을 정의한 후에는 데이터와 AI 행동이 이러한 공유된 가치와 일치하는지 평가하는 것이 다음 단계입니다. 여러분의 행동을 _데이터 수집_과 _알고리즘 설계_라는 두 가지 범주로 생각해 보세요.

데이터 수집의 경우, 행동은 **개인 데이터** 또는 살아 있는 개인을 식별할 수 있는 개인 식별 정보(PII)를 포함할 가능성이 높습니다. 여기에는 _집합적으로_ 개인을 식별할 수 있는 [다양한 비개인 데이터 항목](https://ec.europa.eu/info/law/law-topic/data-protection/reform/what-personal-data_en)이 포함됩니다. 윤리적 도전 과제는 _데이터 프라이버시_, _데이터 소유권_, 그리고 _정보 제공 동의_ 및 사용자에 대한 _지적 재산권_과 같은 관련 주제와 관련될 수 있습니다.

알고리즘 설계의 경우, 행동은 **데이터셋**을 수집 및 큐레이션한 후 이를 사용하여 **데이터 모델**을 훈련 및 배포하여 현실 세계의 맥락에서 결과를 예측하거나 결정을 자동화하는 것을 포함합니다. 윤리적 도전 과제는 _데이터셋 편향_, _데이터 품질_ 문제, _불공정성_, 그리고 알고리즘에서의 _오해_와 관련될 수 있으며, 일부 문제는 체계적일 수 있습니다.

두 경우 모두 윤리적 도전 과제는 우리의 행동이 공유된 가치와 충돌할 수 있는 영역을 강조합니다. 이러한 문제를 감지, 완화, 최소화 또는 제거하기 위해서는 우리의 행동과 관련된 도덕적 "예/아니오" 질문을 던지고 필요한 수정 조치를 취해야 합니다. 이제 윤리적 도전 과제와 그들이 제기하는 도덕적 질문을 살펴보겠습니다:

#### 2.1 데이터 소유권

데이터 수집은 종종 데이터 주체를 식별할 수 있는 개인 데이터를 포함합니다. [데이터 소유권](https://permission.io/blog/data-ownership)은 데이터 생성, 처리 및 배포와 관련된 _통제_와 [_사용자 권리_](https://permission.io/blog/data-ownership)에 관한 것입니다.

우리가 물어봐야 할 도덕적 질문은 다음과 같습니다:
 * 데이터를 소유하는 사람은 누구인가요? (사용자 또는 조직)
 * 데이터 주체는 어떤 권리를 가지고 있나요? (예: 접근, 삭제, 이동성)
 * 조직은 어떤 권리를 가지고 있나요? (예: 악의적인 사용자 리뷰 수정)

#### 2.2 정보 제공 동의

[정보 제공 동의](https://legaldictionary.net/informed-consent/)는 사용자들이 데이터 수집과 같은 행동에 대해 _관련 사실_을 완전히 이해한 상태에서 동의하는 행위를 정의합니다. 여기에는 목적, 잠재적 위험, 대안이 포함됩니다.

여기서 탐구해야 할 질문은 다음과 같습니다:
 * 사용자가 데이터 캡처 및 사용에 대한 허가를 제공했나요?
 * 사용자가 데이터가 캡처된 목적을 이해했나요?
 * 사용자가 참여로 인해 발생할 수 있는 잠재적 위험을 이해했나요?

#### 2.3 지적 재산권

[지적 재산권](https://en.wikipedia.org/wiki/Intellectual_property)은 인간의 창의적 활동에서 발생한 무형의 창작물로, 개인이나 기업에게 _경제적 가치_를 가질 수 있습니다.

여기서 탐구해야 할 질문은 다음과 같습니다:
 * 수집된 데이터가 사용자나 기업에게 경제적 가치를 가지고 있나요?
 * **사용자**가 여기서 지적 재산권을 가지고 있나요?
 * **조직**이 여기서 지적 재산권을 가지고 있나요?
 * 이러한 권리가 존재한다면, 우리는 이를 어떻게 보호하고 있나요?

#### 2.4 데이터 프라이버시

[데이터 프라이버시](https://www.northeastern.edu/graduate/blog/what-is-data-privacy/) 또는 정보 프라이버시는 개인 식별 정보를 포함한 사용자 프라이버시를 보존하고 사용자 신원을 보호하는 것을 의미합니다.

여기서 탐구해야 할 질문은 다음과 같습니다:
 * 사용자의 (개인) 데이터가 해킹 및 유출로부터 안전한가요?
 * 사용자의 데이터가 승인된 사용자와 맥락에서만 접근 가능한가요?
 * 데이터가 공유되거나 배포될 때 사용자의 익명성이 보존되나요?
 * 익명화된 데이터셋에서 사용자를 재식별할 수 있나요?

#### 2.5 잊힐 권리

[잊힐 권리](https://en.wikipedia.org/wiki/Right_to_be_forgotten) 또는 [삭제 요청 권리](https://www.gdpreu.org/right-to-be-forgotten/)는 사용자에게 추가적인 개인 데이터 보호를 제공합니다. 특히, 특정 상황에서 인터넷 검색 및 기타 위치에서 개인 데이터를 삭제하거나 제거할 수 있는 권리를 사용자에게 부여하여, 과거 행동이 사용자에게 불리하게 작용하지 않도록 온라인에서 새 출발을 할 수 있게 합니다.

여기서 탐구해야 할 질문은 다음과 같습니다:
 * 시스템이 데이터 주체가 삭제를 요청할 수 있도록 허용하나요?
 * 사용자의 동의 철회가 자동 삭제를 유발해야 하나요?
 * 데이터가 동의 없이 또는 불법적으로 수집되었나요?
 * 데이터 프라이버시에 대한 정부 규정을 준수하고 있나요?

#### 2.6 데이터셋 편향

데이터셋 또는 [수집 편향](http://researcharticles.com/index.php/bias-in-data-collection-in-research/)은 알고리즘 개발을 위해 _대표성이 없는_ 데이터 하위 집합을 선택하는 것으로, 다양한 그룹에 대해 결과의 공정성을 저해할 수 있습니다. 편향의 유형에는 선택 또는 샘플링 편향, 자발적 편향, 도구 편향이 포함됩니다.

여기서 탐구해야 할 질문은 다음과 같습니다:
 * 대표적인 데이터 주체 집합을 모집했나요?
 * 수집하거나 큐레이션한 데이터셋에서 다양한 편향을 테스트했나요?
 * 발견된 편향을 완화하거나 제거할 수 있나요?

#### 2.7 데이터 품질

[데이터 품질](https://lakefs.io/data-quality-testing/)은 알고리즘 개발에 사용된 큐레이션된 데이터셋의 유효성을 살펴보며, AI 목적에 필요한 정확성과 일관성 수준을 충족하는지 확인합니다.

여기서 탐구해야 할 질문은 다음과 같습니다:
 * 우리의 사용 사례에 유효한 _특징_을 캡처했나요?
 * 다양한 데이터 소스에서 데이터를 _일관되게_ 캡처했나요?
 * 다양한 조건이나 시나리오에 대해 데이터셋이 _완전_한가요?
 * 현실을 반영하는 정보가 _정확하게_ 캡처되었나요?

#### 2.8 알고리즘 공정성
[Algorithm Fairness](https://towardsdatascience.com/what-is-algorithm-fairness-3182e161cf9f)는 알고리즘 설계가 특정 데이터 주체 하위 그룹에 대해 체계적으로 차별을 일으켜 _자원 배분_ (그 그룹에 자원이 거부되거나 보류되는 경우) 및 _서비스 품질_ (AI가 일부 하위 그룹에 대해 다른 그룹보다 덜 정확한 경우)에서 [잠재적 피해](https://docs.microsoft.com/en-us/azure/machine-learning/concept-fairness-ml)를 초래하는지 확인합니다.

여기서 탐구해야 할 질문은 다음과 같습니다:
 * 다양한 하위 그룹과 조건에 대해 모델 정확도를 평가했는가?
 * 잠재적 피해(예: 고정관념)를 시스템에서 면밀히 조사했는가?
 * 확인된 피해를 완화하기 위해 데이터를 수정하거나 모델을 재학습할 수 있는가?

[AI 공정성 체크리스트](https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RE4t6dA)와 같은 리소스를 탐색하여 더 알아보세요.

#### 2.9 오해의 소지

[데이터 오해의 소지](https://www.sciencedirect.com/topics/computer-science/misrepresentation)는 정직하게 보고된 데이터에서 통찰을 전달하면서 원하는 서사를 지원하기 위해 기만적인 방식으로 전달하고 있는지 묻는 것입니다.

여기서 탐구해야 할 질문은 다음과 같습니다:
 * 불완전하거나 부정확한 데이터를 보고하고 있는가?
 * 오해를 불러일으킬 수 있는 방식으로 데이터를 시각화하고 있는가?
 * 결과를 조작하기 위해 선택적인 통계 기법을 사용하고 있는가?
 * 다른 결론을 제시할 수 있는 대안적 설명이 있는가?

#### 2.10 자유 선택

[자유 선택의 환상](https://www.datasciencecentral.com/profiles/blogs/the-illusion-of-choice)은 시스템의 "선택 아키텍처"가 사람들이 옵션과 통제권을 제공받는 것처럼 보이게 하면서 선호하는 결과를 선택하도록 유도하는 의사 결정 알고리즘을 사용할 때 발생합니다. 이러한 [다크 패턴](https://www.darkpatterns.org/)은 사용자에게 사회적, 경제적 피해를 줄 수 있습니다. 사용자 결정은 행동 프로파일에 영향을 미치므로 이러한 행동은 잠재적으로 미래 선택을 주도하여 피해의 영향을 확대하거나 연장할 수 있습니다.

여기서 탐구해야 할 질문은 다음과 같습니다:
 * 사용자가 그 선택을 했을 때의 함의를 이해했는가?
 * 사용자가 (대안적) 선택과 각각의 장단점을 알고 있었는가?
 * 사용자가 자동화되거나 영향을 받은 선택을 나중에 되돌릴 수 있는가?

### 3. 사례 연구

이러한 윤리적 도전을 실제 세계의 맥락에서 이해하려면, 윤리 위반이 간과될 때 개인과 사회에 미칠 수 있는 잠재적 피해와 결과를 강조하는 사례 연구를 살펴보는 것이 도움이 됩니다.

다음은 몇 가지 예입니다:

| 윤리적 도전 | 사례 연구  | 
|--- |--- |
| **정보 제공 동의** | 1972년 - [터스키기 매독 연구](https://en.wikipedia.org/wiki/Tuskegee_Syphilis_Study) - 연구에 참여한 아프리카계 미국인 남성들은 무료 의료 서비스를 약속받았으나, 연구자들은 진단이나 치료 가능성에 대해 피험자들에게 알리지 않아 _기만당했습니다_. 많은 피험자가 사망했고, 배우자나 자녀에게도 영향을 미쳤으며, 연구는 40년 동안 지속되었습니다. | 
| **데이터 프라이버시** | 2007년 - [넷플릭스 데이터 상](https://www.wired.com/2007/12/why-anonymous-data-sometimes-isnt/)은 연구자들에게 _50K 고객의 10M 익명화된 영화 평점_을 제공하여 추천 알고리즘을 개선하도록 했습니다. 그러나 연구자들은 익명화된 데이터를 _외부 데이터셋_ (예: IMDb 댓글)과 연관시켜 일부 넷플릭스 구독자를 사실상 "익명 해제"할 수 있었습니다.|
| **수집 편향**  | 2013년 - 보스턴시는 [Street Bump](https://www.boston.gov/transportation/street-bump)이라는 앱을 개발하여 시민들이 도로의 움푹 팬 곳을 보고하도록 하여 도시가 문제를 파악하고 해결할 수 있도록 더 나은 도로 데이터를 제공했습니다. 그러나 [저소득층은 자동차와 휴대폰 접근성이 낮아](https://hbr.org/2013/04/the-hidden-biases-in-big-data) 이 앱에서 그들의 도로 문제가 보이지 않게 되었습니다. 개발자들은 공정성을 위해 _공평한 접근성과 디지털 격차_ 문제를 해결하기 위해 학계와 협력했습니다. |
| **알고리즘 공정성**  | 2018년 - MIT [Gender Shades Study](http://gendershades.org/overview.html)는 성별 분류 AI 제품의 정확성을 평가하여 여성과 유색 인종에 대한 정확성 격차를 드러냈습니다. [2019년 애플 카드](https://www.wired.com/story/the-apple-card-didnt-see-genderand-thats-the-problem/)는 남성보다 여성에게 적은 신용을 제공하는 것으로 보였습니다. 두 사례 모두 알고리즘 편향이 사회경제적 피해를 초래하는 문제를 보여줍니다.|
| **데이터 오해의 소지** | 2020년 - [조지아 공중보건부는 COVID-19 차트를 발표](https://www.vox.com/covid-19-coronavirus-us-response-trump/2020/5/18/21262265/georgia-covid-19-cases-declining-reopening)했는데, x축의 비연대적 순서로 시민들에게 확진 사례의 추세에 대해 오해를 불러일으키는 것으로 보였습니다. 이는 시각화 트릭을 통한 오해의 소지를 보여줍니다. |
| **자유 선택의 환상** | 2020년 - 학습 앱 [ABCmouse는 FTC 불만을 해결하기 위해 $10M을 지불](https://www.washingtonpost.com/business/2020/09/04/abcmouse-10-million-ftc-settlement/)했는데, 부모들이 취소할 수 없는 구독료를 지불하도록 유도되었습니다. 이는 사용자들이 잠재적으로 해로운 선택을 하도록 유도하는 선택 아키텍처의 다크 패턴을 보여줍니다. |
| **데이터 프라이버시 및 사용자 권리** | 2021년 - 페이스북 [데이터 유출](https://www.npr.org/2021/04/09/986005820/after-data-breach-exposes-530-million-facebook-says-it-will-not-notify-users)은 5억 3천만 명의 사용자 데이터를 유출시켜 FTC에 $5B의 합의를 초래했습니다. 그러나 사용자들에게 유출 사실을 알리지 않아 데이터 투명성과 접근성에 대한 사용자 권리를 위반했습니다. |

더 많은 사례 연구를 탐구하고 싶으신가요? 다음 리소스를 확인하세요:
* [Ethics Unwrapped](https://ethicsunwrapped.utexas.edu/case-studies) - 다양한 산업의 윤리적 딜레마.
* [데이터 과학 윤리 과정](https://www.coursera.org/learn/data-science-ethics#syllabus) - 주요 사례 연구 탐구.
* [문제가 발생한 사례](https://deon.drivendata.org/examples/) - Deon 체크리스트와 예시.

> 🚨 여러분이 본 사례 연구를 생각해보세요 - 여러분의 삶에서 비슷한 윤리적 도전에 영향을 받거나 경험한 적이 있나요? 이 섹션에서 논의한 윤리적 도전 중 하나를 보여주는 또 다른 사례 연구를 생각해볼 수 있나요?

## 응용 윤리

윤리 개념, 도전 과제, 그리고 실제 사례 연구에 대해 이야기했습니다. 하지만 프로젝트에서 윤리적 원칙과 관행을 _적용_하려면 어떻게 시작해야 할까요? 그리고 더 나은 거버넌스를 위해 이러한 관행을 _운영화_하려면 어떻게 해야 할까요? 몇 가지 실제 솔루션을 탐구해봅시다:

### 1. 전문 코드

전문 코드는 조직이 윤리적 원칙과 사명 선언을 지원하도록 구성원을 "장려"하는 한 가지 옵션을 제공합니다. 코드는 전문적 행동에 대한 _도덕적 지침_으로, 직원이나 구성원이 조직의 원칙에 부합하는 결정을 내릴 수 있도록 돕습니다. 이는 구성원의 자발적 준수에 따라 달라지지만, 많은 조직은 구성원의 준수를 동기화하기 위해 추가적인 보상과 처벌을 제공합니다.

예시:
 * [Oxford Munich](http://www.code-of-ethics.org/code-of-conduct/) 윤리 강령
 * [데이터 과학 협회](http://datascienceassn.org/code-of-conduct.html) 행동 강령 (2013년 생성)
 * [ACM 윤리 및 전문 행동 강령](https://www.acm.org/code-of-ethics) (1993년부터)

> 🚨 여러분은 전문 엔지니어링 또는 데이터 과학 조직에 속해 있나요? 그들의 웹사이트를 탐색하여 전문 윤리 강령을 정의하고 있는지 확인하세요. 그들의 윤리적 원칙에 대해 무엇을 말하고 있나요? 구성원이 강령을 따르도록 어떻게 "장려"하고 있나요?

### 2. 윤리 체크리스트

전문 코드는 실무자에게 요구되는 _윤리적 행동_을 정의하지만, [대규모 프로젝트에서의 한계](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md)가 알려져 있습니다. 대신, 많은 데이터 과학 전문가들은 [체크리스트](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md)를 **원칙을 실천으로 연결**하는 더 결정적이고 실행 가능한 방법으로 권장합니다.

체크리스트는 질문을 "예/아니오" 작업으로 변환하여 운영화할 수 있으며, 이를 표준 제품 출시 워크플로의 일부로 추적할 수 있습니다.

예시:
 * [Deon](https://deon.drivendata.org/) - [업계 추천](https://deon.drivendata.org/#checklist-citations)에서 생성된 일반 목적 데이터 윤리 체크리스트로, 명령줄 도구를 통해 쉽게 통합 가능.
 * [프라이버시 감사 체크리스트](https://cyber.harvard.edu/ecommerce/privacyaudit.html) - 법적 및 사회적 노출 관점에서 정보 처리 관행에 대한 일반적인 지침 제공.
 * [AI 공정성 체크리스트](https://www.microsoft.com/en-us/research/project/ai-fairness-checklist/) - AI 개발 주기에 공정성 검사를 채택하고 통합하도록 지원하기 위해 AI 실무자가 생성.
 * [데이터와 AI 윤리를 위한 22가지 질문](https://medium.com/the-organization/22-questions-for-ethics-in-data-and-ai-efb68fd19429) - 설계, 구현, 조직적 맥락에서 윤리적 문제를 초기 탐구하기 위한 더 개방적인 프레임워크.

### 3. 윤리 규제

윤리는 공유된 가치를 정의하고 _자발적으로_ 올바른 일을 하는 것입니다. **준수**는 정의된 법을 _따르는 것_입니다. **거버넌스**는 조직이 윤리적 원칙을 시행하고 확립된 법을 준수하기 위해 운영하는 모든 방법을 포괄합니다.

오늘날 거버넌스는 조직 내에서 두 가지 형태를 취합니다. 첫째, **윤리적 AI** 원칙을 정의하고 조직 내 모든 AI 관련 프로젝트에서 채택을 운영화하는 관행을 수립하는 것입니다. 둘째, 조직이 운영하는 지역의 모든 정부가 규정한 **데이터 보호 규정**을 준수하는 것입니다.

데이터 보호 및 프라이버시 규제의 예:
 * `1974년`, [미국 프라이버시법](https://www.justice.gov/opcl/privacy-act-1974) - _연방 정부_의 개인 정보 수집, 사용 및 공개를 규제.
 * `1996년`, [미국 건강보험 이동성 및 책임법 (HIPAA)](https://www.cdc.gov/phlp/publications/topic/hipaa.html) - 개인 건강 데이터를 보호.
 * `1998년`, [미국 아동 온라인 프라이버시 보호법 (COPPA)](https://www.ftc.gov/enforcement/rules/rulemaking-regulatory-reform-proceedings/childrens-online-privacy-protection-rule) - 13세 미만 아동의 데이터 프라이버시를 보호.
 * `2018년`, [일반 데이터 보호 규정 (GDPR)](https://gdpr-info.eu/) - 사용자 권리, 데이터 보호 및 프라이버시 제공.
 * `2018년`, [캘리포니아 소비자 프라이버시법 (CCPA)](https://www.oag.ca.gov/privacy/ccpa) - 소비자에게 (개인) 데이터에 대한 더 많은 _권리_ 제공.
 * `2021년`, 중국 [개인 정보 보호법](https://www.reuters.com/world/china/china-passes-new-personal-data-privacy-law-take-effect-nov-1-2021-08-20/) - 세계에서 가장 강력한 온라인 데이터 프라이버시 규제 중 하나를 새로 통과.

> 🚨 유럽 연합이 정의한 GDPR(일반 데이터 보호 규정)은 오늘날 가장 영향력 있는 데이터 프라이버시 규제 중 하나로 남아 있습니다. 이 규정이 시민의 디지털 프라이버시와 개인 데이터를 보호하기 위해 [8가지 사용자 권리](https://www.freeprivacypolicy.com/blog/8-user-rights-gdpr)를 정의한다는 것을 알고 계셨나요? 이 권리가 무엇인지, 왜 중요한지 알아보세요.

### 4. 윤리 문화

_준수_ (법의 "문자"를 충족하기 위해 충분히 하는 것)와 [체계적 문제](https://www.coursera.org/learn/data-science-ethics/home/week/4) (예: 경직화, 정보 비대칭, 분배적 불공정성)를 해결하는 것 사이에는 여전히 무형의 격차가 있습니다. 후자는 AI의 무기화를 가속화할 수 있습니다.

후자는 [윤리 문화를 정의하기 위한 협력적 접근](https://towardsdatascience.com/why-ai-ethics-requires-a-culture-driven-approach-26f451afa29f)을 요구하며, 산업 내 조직 간에 감정적 연결과 일관된 공유 가치를 구축합니다. 이는 조직 내에서 더 [공식화된 데이터 윤리 문화](https://www.codeforamerica.org/news/formalizing-an-ethical-data-culture)를 요구하며, _누구나_ [안돈 코드](https://en.wikipedia.org/wiki/Andon_(manufacturing))를 당겨 (윤리적 문제를 초기 단계에서 제기) AI 프로젝트 팀 구성에서 _윤리적 평가_를 핵심 기준으로 삼을 수 있도록 합니다.

---
## [강의 후 퀴즈](https://ff-quizzes.netlify.app/en/ds/) 🎯
## 복습 및 자기 학습

강의와 책은 핵심 윤리 개념과 도전 과제를 이해하는 데 도움을 주며, 사례 연구와 도구는 실제 세계의 맥락에서 응용 윤리 관행을 돕습니다. 시작할 몇 가지 리소스를 소개합니다.

* [초보자를 위한 머신 러닝](https://github.com/microsoft/ML-For-Beginners/blob/main/1-Introduction/3-fairness/README.md) - Microsoft의 공정성에 대한 강의.
* [책임 있는 AI의 원칙](https://docs.microsoft.com/en-us/learn/modules/responsible-ai-principles/) - Microsoft Learn에서 제공하는 무료 학습 경로.
* [윤리와 데이터 과학](https://resources.oreilly.com/examples/0636920203964) - O'Reilly EBook (M. Loukides, H. Mason 등)
* [데이터 과학 윤리](https://www.coursera.org/learn/data-science-ethics#syllabus) - 미시간 대학교의 온라인 강좌.
* [윤리 해설](https://ethicsunwrapped.utexas.edu/case-studies) - 텍사스 대학교의 사례 연구.

# 과제 

[데이터 윤리 사례 연구 작성하기](assignment.md)

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전을 권위 있는 출처로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 책임을 지지 않습니다.