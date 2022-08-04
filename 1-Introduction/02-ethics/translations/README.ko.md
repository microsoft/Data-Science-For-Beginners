# 데이터 윤리 소개

| ![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../../sketchnotes/02-Ethics.png) |
| :-----------------------------------------------------------------------------------------------: |
|              데이터 과학 윤리 - _Sketchnote by [@nitya](https://twitter.com/nitya)_               |

---

우리는 모두 데이터화된 세계(datafied world)에 살고 있는 데이터 시민(data citizens)입니다.

시장 동향에 따르면 2022년까지 3분의 1 규모의 대규모 조직이 온라인 [마켓플레이스 및 거래소](https://www.gartner.com/smarterwithgartner/gartner-top-10-trends-in-data-and-analytics-for-2020/)를 통해 데이터를 사고 팔 것입니다. **앱 개발자**로서 우리는 데이터를 기반으로 한 인사이트(data-driven insight)와 알고리즘 기반 자동화(algorithm-driven automation)를 일상적인 사용자 경험에 통합하는 것이 더 쉽고, 더 저렴하다는 것을 알게 될 것입니다. 그러나 AI가 보편화 됨에 따라, 그러한 알고리즘이 규모적으로 [무기화](https://www.youtube.com/watch?v=TQHs8SA1qpk)로 인한 잠재적 위험을 지니고 있음을 이해해야 합니다.

또한 트렌드에 따르면 우리가 2025년까지 [180 제타 바이트](https://www.statista.com/statistics/871513/worldwide-data-created/) 이상의 데이터를 생성하고 사용할 것을 알려줍니다. **데이터 과학자**로서, 이러한 트렌드는 개인 데이터에 대한 전례 없는 수준의 접근을 제공합니다. 이는 사용자의 행동 프로파일(behavioral profiles)을 구축하고, 우리가 선호하는 결과로 사용자를 유도하는 [자유 선택의 환상](https://www.datasciencecentral.com/profiles/blogs/the-illusion-of-choice)을 만들어내므로 의사결정 과정에 영향을 미칩니다.

데이터 윤리는 이제 데이터 과학 및 데이터 엔지니어링에 _필수적인 가드레일_ 이 되어 데이터 기반 작업으로 인한 잠재적 피해와 의도하지 않은 결과를 최소화하는 데 도움이 됩니다. [가트너(Gartner)의 AI 하이프사이클(Hype Cycle)](https://www.gartner.com/smarterwithgartner/2-megatrends-dominate-the-gartner-hype-cycle-for-artificial-intelligence-2020/)은 AI의 _민주화(democratization)_ 와 _산업화(industrialization)_ 에 대한 더 큰 메가트렌드의 핵심 요인으로 디지털 윤리와 관련된 트렌드, 책임감 있는 AI(responsible AI), AI 거버넌스를 가리킵니다.

![가트너(Gartner)의 AI 하이프사이클(Hype Cycle) - 2020](https://images-cdn.newscred.com/Zz1mOWJhNzlkNDA2ZTMxMWViYjRiOGFiM2IyMjQ1YmMwZQ==)

이 강의에서는 핵심 개념 및 과제부터 사례 연구 및 거버넌스와 같은 응용 AI 개념에 이르기까지, 데이터와 AI를 사용하여 작업하는 팀과 조직에서 윤리 문화를 확립하는 데 도움이 되는 데이터 윤리의 멋진 영역을 살펴볼 것입니다.




## [강의 전 퀴즈](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/2) 🎯

## 기본 정의

기본 용어를 이해하는 것부터 시작해보겠습니다.

윤리라는 단어는 _성격 또는 본성_ 을 의미하는 (그 어원은 "ethos"인) [그리스어 "ethikos"](https://en.wikipedia.org/wiki/Ethics)에서 유래했습니다.

**윤리**는 사회에서 우리의 행동을 지배하는 공유된 가치와 도덕적 원칙에 관한 것입니다. 윤리는 법에 근거한 것이 아니라
무엇이 "옳고 그른지"에 대해 널리 받아들여지는 규범에 근거합니다. 그러나 윤리적인 고려 사항은 규정 준수에 대한 더 많은 인센티브를 생성하는 기업 거버넌스 이니셔티브 및 정부 규정에 영향을 미칠 수 있습니다.

**데이터 윤리**는 "_데이터, 알고리즘, 그에 해당하는 실행(practice)_ 과 연관된 도덕적 문제를 측정하고 연구"하는 [윤리의 새로운 분과(branch)](https://royalsocietypublishing.org/doi/full/10.1098/rsta.2016.0360#sec-1)입니다. 여기서 **"데이터"** 는 생성, 기록, 큐레이션, 처리 보급, 공유 및 사용과 관련된 작업에 중점을 두고, **"알고리즘"** 은 AI, 에이전트, 머신러닝 및 로봇에 중점을 둡니다. **"실행(practice)"** 은 책임 있는 혁신, 프로그래밍, 해킹 및 윤리 강령과 같은 주제에 중점을 둡니다.

**응용 윤리**는 [도덕적 고려사항의 실제적인 적용](https://en.wikipedia.org/wiki/Applied_ethics)을 말합니다. 이는 _실제 행동, 제품 및 프로세스_ 의 맥락에서 윤리적 문제를 적극적으로 조사하고 우리가 정의한 윤리적 가치와 일치하도록 수정하는 조치를 취하는 과정입니다.

**윤리 문화**는 우리의 윤리 원칙과 관행이 다음과 같이 채택되도록 [_운영화_ 응용 윤리](https://hbr.org/2019/05/how-to-design-an-ethical-organization)에 관한 것입니다. 조직 전체에 걸쳐 일관되고 확장 가능한 방식. 성공적인 윤리 문화는 조직 전체의 윤리 원칙을 정의하고 준수를 위한 의미 있는 인센티브를 제공하며 조직의 모든 수준에서 바람직한 행동을 장려하고 증폭함으로써 윤리 규범을 강화합니다.


## 윤리적 개념

이 섹션에서는 데이터 윤리에 대한 **공유 가치**(원칙) 및 **윤리적 과제**(문제)와 같은 개념을 논의하고 이러한 개념을 이해하는 데 도움이 되는 **케이스 스터디**를 살펴볼 것입니다.

### 1. 윤리 원칙

모든 데이터 윤리에 대한 전략은 _윤리 원칙_-데이터 및 AI 프로젝트에서, 허용되는 행동을 설명하고 규정 준수 조치에 대해 설명하는 "공유된 가치"-이 무엇인지 정의하는 것으로부터 시작됩니다. 개인 또는 팀 단위로 정의할 수 있습니다. 그러나 대부분의 대규모 조직은 이런 _윤리적인 AI_ 의 Mission 선언문이나 프레임워크를 회사 차원에서 정의하고, 모든 팀에 일관되게 시행하므로 간략하게 정의합니다.

**예시:** 마이크로소프트의 [책임있는 AI](https://www.microsoft.com/en-us/ai/responsible-ai) Mission 선언문은 다음과 같습니다: _"우리는 사람을 최우선으로 하는 융리 원칙에 따라 AI 기반의 발전에 전념합니다."_ - 아래 프레임워크에서 6가지 윤리 원칙을 식별합니다.

![Microsoft의 책임있는 AI](https://docs.microsoft.com/en-gb/azure/cognitive-services/personalizer/media/ethics-and-responsible-use/ai-values-future-computed.png)

이러한 원칙을 간략하게 살펴보겠습니다. _투명성_ 과 _책임성_ 은 다른 원칙들의 기반이 되는 기본적인 가치입니다. 여기에서부터 시작하겠습니다.

* [**책임**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6)은 실무자가 데이터 및 AI 운영과 이러한 윤리적 원칙 준수에 대해 _책임_ 을 지도록 합니다.
* [**투명성**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6)은 데이터 및 AI 작업이 사용자에게 _이해 가능_(해석 가능)하도록 보장하여 결정의 배경과 이유를 설명합니다.
* [**공평성**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1%3aprimaryr6) - AI가 _모든 사람_ 을 공정하게 대하도록 하는 데 중점을 두고, 데이터 및 시스템의 모든 시스템적 또는 암묵적 사회∙기술적 편견을 해결합니다.
* [**신뢰성 & 안전**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6)은 AI가 정의된 값으로 _일관되게_ 동작하도록 하여 잠재적인 피해나 의도하지 않은 결과를 최소화합니다.
* [**프라이버시 & 보안**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6)는 데이터 계보(Data Lineage)를 이해하고, 사용자에게 _데이터 개인 정보 보호 및 관련 보호 기능_ 을 제공하는 것입니다.
* [**포용**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6)은 AI 솔루션을 의도적으로 설계하고 _광범위한 인간의 요구_ 와 기능을 충족하도록 조정하는 것 입니다.

> 🚨 데이터 윤리 Mission 선언문이 무엇인지 생각해보십시오. 다른 조직의 윤리적 AI 프레임워크를 탐색해보세요. - 다음과 같은 예시가 있습니다. [IBM](https://www.ibm.com/cloud/learn/ai-ethics), [Google](https://ai.google/principles) ,and [Facebook](https://ai.facebook.com/blog/facebooks-five-pillars-of-responsible-ai/). 이들의 공통점은 무엇입니까? 이러한 원칙은 그들이 운영하는 AI 제품 또는 산업과 어떤 관련이 있습니까?

### 2. 윤리적 과제

윤리적 원칙이 정의되면 다음 단계는 데이터와 AI 작업을 평가하여 이러한 공유 가치와 일치하는지 확인하는 것입니다. _데이터 수집_ 과 _알고리즘 디자인_, 이 두 가지 범주에서 당신의 행동(Action)을 생각해 보십시오.

데이터 수집을 통해, 그 행동에는 식별 가능한(idenitifiable) 살아있는 개인에 대한 **개인 데이터** 또는 개인 식별 정보(PII, Personally Identifiable Information)이 포함될 수 있습니다. 여기에는 종합적으로 개인을 식별할 수 있는 [비개인 데이터의 다양한 항목](https://ec.europa.eu/info/law/law-topic/data-protection/reform/what-personal-data_en)도 포함됩니다. 윤리적인 문제는 _데이터 프라이버시(개인 정보 보호)_, _데이터 소유권(ownership)_, 그리고 사용자의 _정보 제공 동의_ 와 _지적 재산권_ 과 같은 관련된 주제와 연관될 수 있습니다.

알고리즘 설계(design)을 사용하면, **데이터 셋**을 수집 및 선별란 다음 이를 사용하여 결과를 예측하거나 실제 상황에서 의사결정을 자동화하는 **데이터 모델**을 교육 및 배포하는 작업이 포함됩니다. 윤리적인 문제는 본질적으로 시스템적인 일부 문제를 포함하여 알고리즘의 _데이터 셋 편향_, _데이터 품질_ 문제, _불공정_ 및 _잘못된 표현_ 으로 인해 발생할 수 있습니다.

두 경우 모두 윤리 문제는 우리의 행동이 공유 가치와 충돌할 수 있는 영역을 강조합니다. 이러한 우려를 감지, 완화, 최소화 또는 제거하려면 우리의 행동과 관련된 도덕적 "예/아니오" 질문을 하고 필요에 따라 수정 조치를 취하십시오. 몇 가지 윤리적 챌린지와 그것이 제기하는 도덕적 질문을 살펴보겠습니다.


#### 2.1 데이터 소유권

데이터 수집에는 종종 데이터 주체를 식별할 수 있는 개인 데이터가 포함됩니다. [데이터 소유권](https://permission.io/blog/data-ownership)은 데이터의 생성, 처리 및 보급과 관련된 _제어(control)_ 와 [_사용자 권한_](https://permission.io/blog/data-ownership)에 관한 것입니다.

우리가 물어야 할 도덕적 질문은 다음과 같습니다.: 
 * 누가 데이터를 소유합니까? (사용자 또는 조직)
 * 데이터 주체(data subjects)는 어떤 권리를 가지고 있나요? (예: 접근, 삭제, 이동성)
 * 조직은 어떤 권리를 가지고 있습니까? (예: 악의적인 사용자 리뷰 수정)

#### 2.2 정보 제공 동의

[정보 제공 동의](https://legaldictionary.net/informed-consent/)는 목적, 잠재적 위험 및 대안을 포함한 관련 사실을 _완전히 이해_ 한 사용자가 데이터 수집과 같은 조치에 동의하는 행위를 말합니다.

여기에서 탐색할 질문은 다음과 같습니다.:
 * 사용자(데이터 주체)가 데이터 캡처 및 사용에 대한 권한을 부여했습니까?
 * 사용자가 해당 데이터가 수집된 목적을 이해했습니까?
 * 사용자가 참여로 인한 잠재적 위험을 이해했습니까?

#### 2.3 지적 재산권

[지적 재산권](https://en.wikipedia.org/wiki/Intellectual_property)은 인간의 주도(human initiative)로 인해 생긴 개인이나 기업에 _경제적 가치가 있을 수 있는_ 무형의 창조물을 말합니다. 

여기에서 탐색할 질문은 다음과 같습니다:
 * 수집된 데이터가 사용자나 비즈니스에 경제적 가치가 있었습니까?
 * **사용자**가 여기에 지적 재산권을 가지고 있습니까?
 * **조직**에 지적 재산권이 있습니까?
 * 이러한 권리가 존재한다면, 어떻게 보호가 됩니까?

#### 2.4 데이터 프라이버시

[데이터 프라이버시](https://www.northeastern.edu/graduate/blog/what-is-data-privacy/) 또는 정보 프라이버시는 개인 식별 정보에 대한 사용자 개인 정보 보호 및 사용자 신원 보호를 의미합니다.

여기서 살펴볼 질문은 다음과 같습니다:
 * 사용자(개인) 데이터는 해킹 및 유출로부터 안전하게 보호되고 있습니까?
 * 승인된 사용자 및 컨텍스트만 사용자 데이터에 액세스할 수 있습니까?
 * 데이터를 공유하거나 유포할 때 사용자의 익명성이 유지됩니까?
 * 익명화된 데이터 세트에서 사용자를 익명화할 수 있습니까?


#### 2.5 잊혀질 권리

[잊혀질 권리](https://en.wikipedia.org/wiki/Right_to_be_forgotten) 또는 [삭제할 권리](https://www.gdpreu.org/right-to-be-forgotten/)는 사용자에 대한 추가적인 개인 데이터 보호를 제공합니다. 특히, 사용자에게 _특정 상황에서_ 인터넷 검색 및 기타 위치에서 개인 데이터 삭제 또는 제거를 요청할 수 있는 권리를 부여하여, 사용자가 과거 조치(action)를 취하지 않고 온라인에서 새로운 출발을 할 수 있게 합니다.

여기서는 다음 질문들을 살펴볼 것입니다:
 * 시스템에서 데이터 주체(Data Subject)가 삭제를 요청할 수 있습니까?
 * 사용자 동의 철회 시 자동으로 데이터를 삭제해야 하나요?
 * 데이터가 동의 없이 또는 불법적인 방법으로 수집되었나요?
 * 우리는 데이터 개인 정보 보호에 대한 정부 규정을 준수합니까?


#### 2.6 데이터셋 편향(Bias)

데이터셋 또는 [데이터 콜렉션 편향](http://researcharticles.com/index.php/bias-in-data-collection-in-research/)은 알고리즘 개발을 위해 _대표적이지 않은(non-representative)_ 데이터 하위 집합을 선택하여, 다양한 그룹의 결과에서 잠재적인 불공정이 발생하는 것에 관한 것입니다. 편향의 유형에는 선택 또는 샘플링 편향, 자원자 편향, 도구 편향이 있습니다.

여기서는 다음 질문들을 살펴볼 것입니다:
 * 데이터 주체의 대표적인 데이터들을 모집했는가?
 * 다양한 편향에 대해 수집되거나 선별된 데이터 셋을 테스트 했습니까?
 * 발견된 편향을 완화하거나 제거할 수 있습니까?

#### 2.7 데이터 품질

[데이터 품질](https://lakefs.io/data-quality-testing/)은 알고리즘을 개발하는 데 사용된 선별된 데이터 셋의 유효성을 살펴보고, 기능과 레코드가 우리의 AI 목적에 필요한 정확성 및 일관성 수준에 대한 요구사항을 충족하는 지 확인합니다.

여기서는 다음 질문들을 살펴볼 것입니다:
 * 유스케이스(use case)에 대한 유효한 _기능_ 을 캡처했습니까?
 * 다양한 데이터 소스에서 데이터가 _일관되게_ 캡처되었습니까?
 * 데이터셋은 다양한 조건 또는 시나리오에 대해 _완전_ 합니까?
 * 포착된 정보가 현실을 _정확하게_ 반영합니까?

#### 2.8 알고리즘 공정성

[알고리즘 공정성](https://towardsdatascience.com/what-is-algorithm-fairness-3182e161cf9f)은, _할당(해당 그룹에서 리소스가 거부되거나 보류되는 경우)_ 및 _서비스 품질(일부 하위 그룹의 경우 AI가 다른 그룹의 경우만큼 정확하지 않음)_ 에서, 알고리즘 설계가 [잠재적인 피해](https://docs.microsoft.com/en-us/azure/machine-learning/concept-fairness-ml)로 이어지는 데이터 주체의 특정 하위 그룹을 체계적으로 구별하는지 확인합니다.

여기서는 다음 질문들을 살펴볼 것입니다:
 * 다양한 하위 그룹 및 조건에 대해 모델 정확도를 평가했습니까?
 * 잠재적인 피해(예: 고정 관념)에 대해 시스템을 면밀히 조사했습니까?
 * 식별된 피해를 완화하기 위해 데이터를 수정하거나 모델을 다시 학습시킬 수 있습니까?

더 알아보고 싶다면, 다음 자료를 살펴보세요: [AI 공정성 체크리스트](https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RE4t6dA)

#### 2.9 와전(Misrepresentation)

[데이터 와전(Misrepresentation)](https://www.sciencedirect.com/topics/computer-science/misrepresentation)은 정직하게 보고된 데이터의 통찰력을, 원하는 내러티브(Narrative)에 맞춰 기만적인 방식으로 전달하고 있는지 묻는 것입니다.

여기서는 다음 질문들을 살펴볼 것입니다:
 * 불완전하거나 부정확한 데이터를 보고하고 있습니까?
 * 오해의 소지가 있는 결론을 도출하는 방식으로 데이터를 시각화하고 있습니까?
 * 결과를 조작하기 위해 선택적 통계 기법을 사용하고 있습니까?
 * 다른 결론을 제시할 수 있는 대안적인 설명이 있습니까?

#### 2.10 자유로운 선택
[자유롭게 선택하고 있다는 환상](https://www.datasciencecentral.com/profiles/blogs/the-illusion-of-choice)은 시스템 '선택 아키텍처'가 의사결정 알고리즘을 사용하여 사람들에게 선택권과 통제권을 주는 것처럼 하면서 시스템이 선호하는 결과를 선택하도록 유도할 때 발생합니다. 이런 [다크 패턴(dark pattern)](https://www.darkpatterns.org/)은 사용자에게 사회적, 경제적 피해를 줄 수 있습니다. 사용자 결정은 행동 프로파일에 영향을 미치기 때문에, 이러한 행동은 잠재적으로 이러한 피해의 영향을 증폭하거나 확장할 수 있는 향후의 선택을 유도합니다.

여기서는 다음 질문들을 살펴볼 것입니다:
 * 사용자는 그 선택의 의미를 이해했습니까?
 * 사용자는 (대안이 되는) 선택과 각각의 장단점을 알고 있습니까?
 * 사용자가 나중에 자동화되거나 영향을 받은 선택을 되돌릴 수 있습니까?

### 3. 케이스 스터디

이러한 윤리적 문제를 실제 상황에 적용하려면, 그러한 윤리 위반이 간과 되었을 때 개인과 사회에 미칠 잠재적인 피해와 결과를 강조하는 케이스 스터디를 살펴보는 것이 도움이 됩니다. 

다음은 몇 가지 예입니다.

| 윤리적 과제                    | Case Study                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **통보 동의** | 1972 - [Tuskegee 매독 연구](https://en.wikipedia.org/wiki/Tuskegee_Syphilis_Study) - 피험자로 연구에 참여한 아프리카계 미국인 남성은 피험자에게 진단이나 정보를 알려주지 않은 연구원들에게 무료 의료 서비스를 약속받았지만, 약속은 지켜지지 않았다. 많은 피험자가 사망하고 배우자와 자녀들이 영향을 받았습니다. 연구는 40년 동안 지속되었습니다.                                                                                                                                                   |
| **데이터 프라이버시(Privacy)**               | 2007 - [넷플릭스 Data Prize](https://www.wired.com/2007/12/why-anonymous-data-sometimes-isnt/) 는 추천 알고리즘을 개선하기 위해 연구원들에게 _5만명 고객으로부터 수집한 1천만개의 비식별화된(anonymized) 영화 순위_를 제공했습니다. 그러나 연구원들은 비식별화된(anonymized) 데이터를 _외부 데이터셋_ (예를 들어, IMDb 댓글)에 있는 개인식별 데이터(personally-identifiable data)와 연관시킴으로, 효과적으로 일부 Netflix 가입자를 '비익명화(de-anonymizing)' 할 수 있었습니다. |
| **편향 수집**            | 2013 - 보스턴 시는 시민들이 움푹 들어간 곳을 보고할 수 있는 앱인 [Street Bump](https://www.boston.gov/transportation/street-bump)를 개발하여 시에서 문제를 찾고 수정할 수 있는 더 나은 도로 데이터를 제공합니다. 그러나 [저소득층의 사람들은 자동차와 전화에 대한 접근성이 낮기 때문에](https://hbr.org/2013/04/the-hidden-biases-in-big-data) 이 앱에서 도로 문제를 볼 수 없었습니다. 개발자들은 학계와 협력하여 공정성을 위한 _공평한 접근 및 디지털 격차_ 문제를 해결했습니다. |
| **알고리즘 공정성** | 2018 - MIT [성별 유색인종 연구](http://gendershades.org/overview.html)에서 성별 분류 AI 제품의 정확도를 평가하여 여성과 유색인의 정확도 격차를 드러냈습니다. [2019년도 Apple Card](https://www.wired.com/story/the-apple-card-didnt-see-genderand-thats-the-problem/)는 남성보다 여성에게 신용을 덜 제공하는 것으로 보입니다. 둘 다 사회 경제적 피해로 이어지는 알고리즘 편향의 문제를 나타냅니다.  |
| **데이터 허위 진술** | 2020년 - [조지아 보건부 코로나19 차트 발표](https://www.vox.com/covid-19-coronavirus-us-response-trump/2020/5/18/21262265/georgia-covid- 19건-거절-재개)의 x축이 시간순이 아닌 순서로 표시된 확인된 사례의 추세에 대해 시민들을 잘못된 방향으로 이끄는 것으로 나타났습니다. 이 발표 시각화 트릭을 통해 잘못된 표현을 나타냈습니다. |
| **자유 선택의 환상** | 2020 - 학습 앱인 [ABCmouse는 부모들이 취소할 수 없는 구독료에 빠지게 되는 FTC 불만 해결을 위해 1천만 달러 지불](https://www.washingtonpost.com/business/2020/09/04/abcmouse-10-million-ftc-settlement/) 했습니다. 이는 사용자가 잠재적으로 해로운 선택을 하도록 유도하는 선택 아키텍처의 어두운 패턴을 보여줍니다. |
| **데이터 개인정보 보호 및 사용자 권한** | 2021 - Facebook 의 [데이터 침해](https://www.npr.org/2021/04/09/986005820/after-data-breach-exposes-530-million-facebook-says-it-will-not-notify- 사용자) 는 5억 3천만 명의 사용자의 데이터를 노출하여 FTC에 50억 달러의 합의금을 냈습니다. 그러나 데이터 투명성 및 액세스에 대한 사용자 권한을 위반하는 위반 사항을 사용자에게 알리는 것을 거부했습니다. |

더 많은 사례 연구를 살펴보고 싶으십니까? 다음 리소스를 확인하세요.:
* [윤리를 풀다(ethic unwrapped)](https://ethicsunwrapped.utexas.edu/case-studies) - 다양한 산업 분야의 윤리 딜레마
* [데이터 과학 윤리 과정](https://www.coursera.org/learn/data-science-ethics#syllabus) - 획기적인 사례 연구 탐구
* [문제가 발생한 곳](https://deon.drivendata.org/examples/) - 사례와 함께 살펴보는 데온(deon)의 체크리스트

> 🚨 당신이 본 사례 연구에 대해 생각해보십시오. 당신은 당신의 삶에서 유사한 윤리적 도전을 경험했거나 영향을 받은 적이 있습니까? 이 섹션에서 논의한 윤리적 문제 중 하나에 대한 다른 사례 연구를 하나 이상 생각할 수 있습니까?

## 응용 윤리(Applied Ethics)

우리는 실제 상황에서 윤리 개념, 도전 과제 및 사례 연구에 대해 이야기했습니다. 그러나 프로젝트에서 윤리적 원칙과 관행을 _적용_ 하기 시작하려면 어떻게 해야 합니까? 그리고 더 나은 거버넌스를 위해 이러한 관행을 어떻게 _운영_ 할 수 있습니까? 몇 가지 실제 솔루션을 살펴보겠습니다: 

### 1. 전문 코드(Professional Codes)

전문 강령(Professional Codes)은 조직이 구성원의 윤리 원칙과 사명 선언문을 지지하도록 "인센티브"를 제공하는 하나의 옵션을 제공합니다. 강령은 직원이나 구성원이 조직의 원칙에 부합하는 결정을 내리는 데 도움이 되는 직업적 행동에 대한 _도덕적 지침_ 입니다. 이는 회원들의 자발적인 준수에 달려 있습니다. 그러나 많은 조직에서 구성원의 규정 준수를 유도하기 위해 추가 보상과 처벌을 제공합니다.

다음과 같은 사례가 있습니다:

 * [Oxford Munich](http://www.code-of-ethics.org/code-of-conduct/) 윤리강령
 * [데이터 과학 협회](http://datascienceassn.org/code-of-conduct.html) 행동강령 (2013년 제정)
 * [ACM 윤리 및 직업 행동 강령](https://www.acm.org/code-of-ethics) (1993년 이후)

> 🚨 전문 엔지니어링 또는 데이터 과학 조직에 속해 있습니까? 그들의 사이트를 탐색하여 그들이 직업적 윤리 강령을 정의하는지 확인하십시오. 이것은 그들의 윤리적 원칙에 대해 무엇을 말합니까? 구성원들이 코드를 따르도록 "인센티브"를 제공하는 방법은 무엇입니까?

### 2. 윤리 체크리스트

전문 강령은 실무자에게 필요한 _윤리적 행동_ 을 정의하지만 특히 대규모 프로젝트 시행에서 [자주 사용되는 제한 사항이 있습니다](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md). 이로 인해 많은 데이터 과학 전문가들이 [체크리스트를 따름으로](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md) 보다 결정적이고 실행 가능한 방식으로 **원칙과 사례를 연결** 할 수 있습니다.

체크리스트는 질문을 운영 가능한 "예/아니오" 작업으로 변환하여 표준 제품 릴리스 워크플로의 일부로 추적할 수 있도록 합니다.

다음과 같은 사례가 있습니다:
 * [Deon](https://deon.drivendata.org/) - 쉬운 통합을 위한 Command Line Tool 형태의 범용적인 윤리 체크리스트 ([업계 권고사항](https://deon.drivedata.org/#checklist-citations)에서 만들어짐)
 * [개인정보 감사 체크리스트](https://cyber.harvard.edu/ecommerce/privacyaudit.html) - 법적 및 사회적 노출 관점에서 정보 처리 관행에 대한 일반적인 지침을 제공합니다.
 * [AI 공정성 체크리스트](https://www.microsoft.com/en-us/research/project/ai-fairness-checklist/) - 공정성 검사의 채택 및 AI 개발 주기 통합을 지원하기 위해 AI 실무자가 작성.
 * [데이터 및 AI의 윤리에 대한 22가지 질문](https://medium.com/the-organization/22-questions-for-ethics-in-data-and-ai-efb68fd19429) - 디자인, 구현 및 조직적 맥락에서 윤리적 문제의 초기 탐색을 위한, 보다 개방적인 프레임워크, 구조화.

### 3. 윤리 규정

윤리는 공유 가치를 정의하고 옳은 일을 _자발적으로_ 하는 것입니다. **규정 준수**는 정의된 경우 _법률 준수_ 에 관한 것입니다. **거버넌스**는 조직이 윤리 원칙을 시행하고 확립된 법률을 준수하기 위해 운영하는 모든 방식을 광범위하게 포함합니다.

오늘날 거버넌스는 조직 내에서 두 가지 형태를 취합니다. 첫째, **윤리적 AI** 원칙을 정의하고 조직의 모든 AI 관련 프로젝트에서 채택을 운영하기 위한 관행을 수립하는 것입니다. 둘째, 사업을 영위하는 지역에 대해 정부에서 의무화한 모든 **데이터 보호 규정**을 준수하는 것입니다.

데이터 보호 및 개인 정보 보호 규정 사례:

 * `1974`, [미국 개인 정보 보호법](https://www.justice.gov/opcl/privacy-act-1974) - _연방 정부_ 의 개인 정보 수집, 사용 및 공개를 규제합니다.
 * `1996`, [미국 HIPAA(Health Insurance Portability & Accountability Act)](https://www.cdc.gov/phlp/publications/topic/hipaa.html) - 개인 건강 데이터를 보호합니다.
 * `1998`, [미국 아동 온라인 개인정보 보호법(COPPA)](https://www.ftc.gov/enforcement/rules/rulemaking-regulatory-reform-proceedings/childrens-online-privacy-protection-rule) - 13세 미만 어린이의 데이터 프라이버시를 보호합니다.
 * `2018`, [GDPR(일반 데이터 보호 규정)](https://gdpr-info.eu/) - 사용자 권한, 데이터 보호 및 개인 정보 보호를 제공합니다.
 * `2018`, [캘리포니아 소비자 개인정보 보호법(CCPA)](https://www.oag.ca.gov/privacy/ccpa) 소비자에게 자신의 (개인) 데이터에 대해 더 많은 _권리_ 를 부여합니다.
 * `2021`, 중국의 [개인정보보호법](https://www.reuters.com/world/china/china-passes-new-personal-data-privacy-law-take-effect-nov-1-2021-08-20/) 막 통과되어 전 세계적으로 가장 강력한 온라인 데이터 개인 정보 보호 규정 중 하나를 만들었습니다.

> 🚨 유럽 연합에서 정의한 GDPR(일반 데이터 보호 규정)은 오늘날 가장 영향력 있는 데이터 개인 정보 보호 규정 중 하나입니다. 시민의 디지털 프라이버시와 개인 데이터를 보호하기 위헌 [8가지 사용자 권한](https://www.freeprivacypolicy.com/blog/8-user-rights-gdpr)도 정의하고 있다는 사실을 알고 계셨습니까? 이것이 무엇이며 왜 중요한지 알아보십시오.


### 4. 윤리 문화

_준수_ ("법규"를 충족하기 위해 충분히 노력함)와 (골화, 정보 비대칭 및 분배 불공정과 같은) AI의 무기화를 가속화할 수 있는 [시스템 문제](https://www.coursera.org/learn/data-science-ethics/home/week) 해결 사이에는 무형의 격차가 있습니다.

후자는 산업에서 _조직 전체적으로_ 정서적 연결과 일관된 공유 가치를 구축하는 [윤리 문화를 정의하기 위한 협력적 접근 방식](https://towardsdatascience.com/why-ai-ethics-requires-a-culture-driven-approach-26f451afa29f)이 필요합니다. 이것은 조직에서 더 많은 [공식화된 데이터 윤리 문화](https://www.codeforamerica.org/news/formalizing-an-ethical-data-culture/)를 요구합니다. 이런 문화는 _누구나_ (프로세스 초기에 윤리 문제 제기를 위해) [Andon 강령을 사용하고](https://en.wikipedia.org/wiki/Andon_(manufacturing)) _윤리적 평가_ (예: 고용 시)를 AI 프로젝트의 핵심 기준 팀 구성으로 만듭니다.

---
## [강의 후 퀴즈](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/3) 🎯
## 복습 & 독학

과정과 책은 핵심 윤리 개념과 과제를 이해하는 데 도움이 되며, Case Study와 도구는 실제 상황에서 윤리 사항들을 적용하는 데 도움이 됩니다. 다음은 시작을 할 때 도움이 되는 몇가지 자료들입니다.

* [초보자를 위한 기계 학습](https://github.com/microsoft/ML-For-Beginners/blob/main/1-Introduction/3-fairness/README.md) - 공정성(fairness)에 대한 강의, from Microsoft.
* [책임있는 AI 원칙](https://docs.microsoft.com/en-us/learn/modules/responsible-ai-principles/) - 무료 학습 경로, from Microsoft Learn.
* [윤리와 데이터 과학](https://resources.oreilly.com/examples/0636920203964) - O'Reilly EBook (M. Loukides, H. Mason et. al)
* [데이터 과학 윤리](https://www.coursera.org/learn/data-science-ethics#syllabus) - 미시간 대학의 온라인 학습 과정.
* [Ethics Unwrapped](https://ethicsunwrapped.utexas.edu/case-studies) - 텍사스 대의 Case Study.

# 과제

[데이터 윤리 Case Study 작성](./assignment.ko.md)