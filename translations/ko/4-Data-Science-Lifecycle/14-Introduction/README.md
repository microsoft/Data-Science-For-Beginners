<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "07478c2092203a69087b9c76b1f4dd56",
  "translation_date": "2025-09-05T13:01:41+00:00",
  "source_file": "4-Data-Science-Lifecycle/14-Introduction/README.md",
  "language_code": "ko"
}
-->
# 데이터 과학 생애 주기 소개

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/14-DataScience-Lifecycle.png)|
|:---:|
| 데이터 과학 생애 주기 소개 - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

## [강의 전 퀴즈](https://ff-quizzes.netlify.app/en/ds/quiz/26)

지금쯤 데이터 과학이 하나의 과정이라는 것을 깨달았을 것입니다. 이 과정은 다음의 5단계로 나눌 수 있습니다:

- 데이터 수집
- 데이터 처리
- 데이터 분석
- 결과 전달
- 유지 관리

이번 강의에서는 생애 주기의 3가지 부분인 데이터 수집, 처리, 유지 관리에 초점을 맞춥니다.

![데이터 과학 생애 주기 다이어그램](../../../../4-Data-Science-Lifecycle/14-Introduction/images/data-science-lifecycle.jpg)
> 사진 출처: [Berkeley School of Information](https://ischoolonline.berkeley.edu/data-science/what-is-data-science/)

## 데이터 수집

생애 주기의 첫 번째 단계는 매우 중요합니다. 이후 단계들이 이 단계에 의존하기 때문입니다. 이 단계는 사실상 두 가지 단계를 하나로 결합한 것으로, 데이터를 획득하고 해결해야 할 목적과 문제를 정의하는 것입니다.  
프로젝트의 목표를 정의하려면 문제나 질문에 대한 깊은 맥락이 필요합니다. 먼저, 문제 해결이 필요한 사람들을 식별하고 획득해야 합니다. 이들은 비즈니스의 이해관계자나 프로젝트의 후원자일 수 있으며, 이 프로젝트로부터 누가 또는 무엇이 혜택을 받을지, 그리고 왜 필요한지를 식별하는 데 도움을 줄 수 있습니다. 잘 정의된 목표는 측정 가능하고 정량화할 수 있어야 하며, 이를 통해 수용 가능한 결과를 정의할 수 있습니다.

데이터 과학자가 할 수 있는 질문:
- 이 문제가 이전에 접근된 적이 있는가? 어떤 결과가 발견되었는가?
- 모든 관련자가 목적과 목표를 이해하고 있는가?
- 모호함이 있는가? 이를 어떻게 줄일 수 있는가?
- 제약 조건은 무엇인가?
- 최종 결과는 어떤 모습일 가능성이 있는가?
- 사용할 수 있는 자원(시간, 인력, 계산 능력)은 얼마나 되는가?

다음 단계는 목표를 달성하기 위해 필요한 데이터를 식별, 수집, 탐색하는 것입니다. 이 데이터 획득 단계에서 데이터 과학자는 데이터의 양과 질을 평가해야 합니다. 이를 위해 데이터 탐색을 수행하여 획득한 데이터가 원하는 결과를 지원할 수 있는지 확인해야 합니다.

데이터에 대해 데이터 과학자가 할 수 있는 질문:
- 이미 사용할 수 있는 데이터는 무엇인가?
- 이 데이터의 소유자는 누구인가?
- 개인정보 보호 문제는 무엇인가?
- 이 문제를 해결하기에 충분한 데이터가 있는가?
- 이 문제에 대해 데이터의 품질이 적합한가?
- 이 데이터를 통해 추가 정보를 발견하면 목표를 변경하거나 재정의해야 하는가?

## 데이터 처리

생애 주기의 처리 단계는 데이터에서 패턴을 발견하고 모델링하는 데 초점을 맞춥니다. 처리 단계에서 사용되는 일부 기술은 통계적 방법을 통해 패턴을 발견하는 데 필요합니다. 일반적으로 대규모 데이터 세트를 인간이 직접 처리하기에는 번거롭기 때문에 컴퓨터를 활용하여 작업 속도를 높입니다. 이 단계는 데이터 과학과 머신 러닝이 교차하는 지점이기도 합니다. 첫 번째 강의에서 배운 것처럼, 머신 러닝은 데이터를 이해하기 위해 모델을 구축하는 과정입니다. 모델은 데이터 내 변수 간의 관계를 나타내며 결과를 예측하는 데 도움을 줍니다.

이 단계에서 사용되는 일반적인 기술은 ML for Beginners 커리큘럼에서 다룹니다. 아래 링크를 통해 더 자세히 알아보세요:

- [분류(Classification)](https://github.com/microsoft/ML-For-Beginners/tree/main/4-Classification): 데이터를 카테고리로 분류하여 효율적으로 활용.
- [군집화(Clustering)](https://github.com/microsoft/ML-For-Beginners/tree/main/5-Clustering): 데이터를 유사한 그룹으로 묶음.
- [회귀(Regression)](https://github.com/microsoft/ML-For-Beginners/tree/main/2-Regression): 변수 간의 관계를 파악하여 값을 예측하거나 전망.

## 유지 관리

생애 주기 다이어그램에서 유지 관리가 데이터 수집과 처리 사이에 위치한 것을 볼 수 있습니다. 유지 관리는 프로젝트 과정 동안 데이터를 관리, 저장, 보호하는 지속적인 과정이며, 프로젝트 전체에서 고려되어야 합니다.

### 데이터 저장

데이터를 어떻게, 어디에 저장할지에 대한 고려는 저장 비용뿐만 아니라 데이터 접근 속도에도 영향을 미칠 수 있습니다. 이러한 결정은 데이터 과학자가 단독으로 내리기보다는 데이터 저장 방식에 따라 작업 방식을 선택해야 할 수도 있습니다.

현대 데이터 저장 시스템의 몇 가지 측면:
**온프레미스 vs 오프프레미스 vs 퍼블릭 또는 프라이빗 클라우드**

온프레미스는 데이터를 자체 장비에 호스팅하고 관리하는 것을 의미하며, 예를 들어 서버와 하드 드라이브를 소유하여 데이터를 저장하는 방식입니다. 반면 오프프레미스는 소유하지 않은 장비(예: 데이터 센터)를 사용하는 것을 의미합니다. 퍼블릭 클라우드는 데이터가 정확히 어디에 저장되는지 알 필요가 없는 인기 있는 선택지이며, 퍼블릭은 클라우드를 사용하는 모든 사용자에게 공유되는 통합된 기본 인프라를 의미합니다. 일부 조직은 엄격한 보안 정책을 가지고 있어 데이터가 호스팅되는 장비에 완전한 접근 권한을 요구하며, 자체 클라우드 서비스를 제공하는 프라이빗 클라우드를 사용할 수 있습니다. 클라우드에서의 데이터에 대한 내용은 [추후 강의](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/5-Data-Science-In-Cloud)에서 더 자세히 배울 수 있습니다.

**콜드 데이터 vs 핫 데이터**

모델을 훈련할 때 더 많은 훈련 데이터가 필요할 수 있습니다. 모델이 만족스러울 경우, 모델이 목적을 수행하기 위해 더 많은 데이터가 도착할 것입니다. 어떤 경우든 데이터를 더 많이 축적할수록 저장 및 접근 비용이 증가합니다. 자주 사용되지 않는 데이터를 콜드 데이터라고 하며, 자주 접근하는 핫 데이터와 분리하면 하드웨어 또는 소프트웨어 서비스를 통해 더 저렴한 데이터 저장 옵션을 제공할 수 있습니다. 콜드 데이터를 접근해야 할 경우, 핫 데이터에 비해 검색 시간이 조금 더 걸릴 수 있습니다.

### 데이터 관리

데이터를 작업하면서 일부 데이터를 정리해야 할 필요성을 발견할 수 있습니다. 이는 [데이터 준비](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/2-Working-With-Data/08-data-preparation) 강의에서 다룬 기술을 사용하여 정확한 모델을 구축하기 위함입니다. 새로운 데이터가 도착하면 동일한 기술을 적용하여 데이터 품질의 일관성을 유지해야 합니다. 일부 프로젝트에서는 데이터를 최종 위치로 이동하기 전에 자동화 도구를 사용하여 데이터 정리, 집계, 압축을 수행할 수 있습니다. Azure Data Factory는 이러한 도구의 예입니다.

### 데이터 보안

데이터 보안의 주요 목표 중 하나는 데이터를 작업하는 사람들이 수집된 데이터와 그 사용 맥락을 통제할 수 있도록 하는 것입니다. 데이터를 안전하게 유지하려면 데이터 접근을 필요한 사람들로 제한하고, 지역 법률 및 규정을 준수하며, [윤리 강의](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/1-Introduction/02-ethics)에서 다룬 윤리적 기준을 유지해야 합니다.

보안을 염두에 둔 팀이 할 수 있는 작업:
- 모든 데이터가 암호화되었는지 확인
- 고객에게 데이터 사용 방식에 대한 정보를 제공
- 프로젝트를 떠난 사람들의 데이터 접근 권한 제거
- 특정 프로젝트 멤버만 데이터 수정 가능

## 🚀 도전 과제

데이터 과학 생애 주기의 다양한 버전이 존재하며, 각 단계는 다른 이름과 단계 수를 가질 수 있지만 이 강의에서 언급된 동일한 과정을 포함합니다.

[Team Data Science Process 생애 주기](https://docs.microsoft.com/en-us/azure/architecture/data-science-process/lifecycle)와 [데이터 마이닝을 위한 산업 표준 프로세스(CRISP-DM)](https://www.datascience-pm.com/crisp-dm-2/)를 탐색하세요. 두 가지 사이의 3가지 유사점과 차이점을 작성하세요.

|Team Data Science Process (TDSP)|Cross-industry standard process for data mining (CRISP-DM)|
|--|--|
|![Team Data Science Lifecycle](../../../../4-Data-Science-Lifecycle/14-Introduction/images/tdsp-lifecycle2.png) | ![Data Science Process Alliance Image](../../../../4-Data-Science-Lifecycle/14-Introduction/images/CRISP-DM.png) |
| 이미지 출처: [Microsoft](https://docs.microsoft.comazure/architecture/data-science-process/lifecycle) | 이미지 출처: [Data Science Process Alliance](https://www.datascience-pm.com/crisp-dm-2/) |

## [강의 후 퀴즈](https://ff-quizzes.netlify.app/en/ds/quiz/27)

## 복습 및 자기 학습

데이터 과학 생애 주기를 적용하는 데는 여러 역할과 작업이 필요하며, 일부는 각 단계의 특정 부분에 집중할 수 있습니다. Team Data Science Process는 프로젝트에서 누군가가 맡을 수 있는 역할과 작업 유형을 설명하는 몇 가지 자료를 제공합니다.

* [Team Data Science Process 역할 및 작업](https://docs.microsoft.com/en-us/azure/architecture/data-science-process/roles-tasks)
* [데이터 과학 작업 실행: 탐색, 모델링, 배포](https://docs.microsoft.com/en-us/azure/architecture/data-science-process/execute-data-science-tasks)

## 과제

[데이터셋 평가하기](assignment.md)

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서를 해당 언어로 작성된 상태에서 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.  