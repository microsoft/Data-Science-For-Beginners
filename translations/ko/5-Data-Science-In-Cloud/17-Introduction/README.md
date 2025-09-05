<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f8e7cdefa096664ae86f795be571580",
  "translation_date": "2025-09-05T12:57:00+00:00",
  "source_file": "5-Data-Science-In-Cloud/17-Introduction/README.md",
  "language_code": "ko"
}
-->
# 클라우드에서의 데이터 과학 소개

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/17-DataScience-Cloud.png)|
|:---:|
| 클라우드에서의 데이터 과학: 소개 - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

이 강의에서는 클라우드의 기본 원칙을 배우고, 클라우드 서비스를 사용하여 데이터 과학 프로젝트를 실행하는 것이 왜 흥미로울 수 있는지 알아본 후, 클라우드에서 실행된 데이터 과학 프로젝트의 몇 가지 예를 살펴보겠습니다.

## [강의 전 퀴즈](https://ff-quizzes.netlify.app/en/ds/quiz/32)

## 클라우드란 무엇인가?

클라우드 또는 클라우드 컴퓨팅은 인터넷을 통해 인프라에 호스팅된 다양한 종량제 컴퓨팅 서비스를 제공하는 것입니다. 서비스에는 스토리지, 데이터베이스, 네트워킹, 소프트웨어, 분석 및 지능형 서비스와 같은 솔루션이 포함됩니다.

일반적으로 퍼블릭, 프라이빗, 하이브리드 클라우드를 다음과 같이 구분합니다:

* 퍼블릭 클라우드: 퍼블릭 클라우드는 제3자 클라우드 서비스 제공자가 소유하고 운영하며, 인터넷을 통해 대중에게 컴퓨팅 자원을 제공합니다.
* 프라이빗 클라우드: 특정 기업이나 조직에서 독점적으로 사용하는 클라우드 컴퓨팅 자원을 의미하며, 서비스와 인프라는 프라이빗 네트워크에서 유지됩니다.
* 하이브리드 클라우드: 하이브리드 클라우드는 퍼블릭 클라우드와 프라이빗 클라우드를 결합한 시스템입니다. 사용자는 온프레미스 데이터센터를 선택하면서 데이터와 애플리케이션을 하나 이상의 퍼블릭 클라우드에서 실행할 수 있습니다.

대부분의 클라우드 컴퓨팅 서비스는 다음 세 가지 범주로 나뉩니다: 서비스형 인프라(IaaS), 서비스형 플랫폼(PaaS), 서비스형 소프트웨어(SaaS).

* 서비스형 인프라(IaaS): 사용자는 서버, 가상 머신(VM), 스토리지, 네트워크, 운영 체제와 같은 IT 인프라를 임대합니다.
* 서비스형 플랫폼(PaaS): 사용자는 소프트웨어 애플리케이션을 개발, 테스트, 배포 및 관리하기 위한 환경을 임대합니다. 개발에 필요한 서버, 스토리지, 네트워크 및 데이터베이스의 기본 인프라를 설정하거나 관리할 필요가 없습니다.
* 서비스형 소프트웨어(SaaS): 사용자는 인터넷을 통해 소프트웨어 애플리케이션에 액세스하며, 일반적으로 구독 방식으로 제공됩니다. 소프트웨어 애플리케이션의 호스팅, 관리, 유지보수(예: 소프트웨어 업그레이드 및 보안 패치)를 걱정할 필요가 없습니다.

가장 큰 클라우드 제공업체로는 Amazon Web Services, Google Cloud Platform, Microsoft Azure가 있습니다.

## 데이터 과학을 위해 클라우드를 선택하는 이유는 무엇인가?

개발자와 IT 전문가가 클라우드를 선택하는 이유는 다음과 같습니다:

* 혁신: 클라우드 제공업체가 만든 혁신적인 서비스를 애플리케이션에 직접 통합하여 애플리케이션을 강화할 수 있습니다.
* 유연성: 필요한 서비스만 사용하며 다양한 서비스 중에서 선택할 수 있습니다. 일반적으로 종량제로 비용을 지불하며, 변화하는 요구에 따라 서비스를 조정할 수 있습니다.
* 예산: 하드웨어와 소프트웨어를 구매하고 온프레미스 데이터센터를 설정 및 운영하는 초기 투자 없이 사용한 만큼만 비용을 지불하면 됩니다.
* 확장성: 프로젝트의 요구에 따라 자원을 확장할 수 있어, 애플리케이션이 외부 요인에 따라 컴퓨팅 파워, 스토리지, 대역폭을 더 많이 또는 적게 사용할 수 있습니다.
* 생산성: 데이터센터 관리와 같은 다른 사람이 처리할 수 있는 작업에 시간을 소비하지 않고 비즈니스에 집중할 수 있습니다.
* 신뢰성: 클라우드 컴퓨팅은 데이터를 지속적으로 백업하는 여러 방법을 제공하며, 위기 상황에서도 비즈니스와 서비스를 유지할 수 있는 재해 복구 계획을 설정할 수 있습니다.
* 보안: 프로젝트의 보안을 강화하는 정책, 기술 및 제어를 활용할 수 있습니다.

이것이 사람들이 클라우드 서비스를 선택하는 가장 일반적인 이유입니다. 이제 클라우드가 무엇인지와 주요 이점에 대해 더 잘 이해했으니, 데이터 과학자와 데이터 작업을 하는 개발자의 역할에 대해 더 구체적으로 살펴보고, 클라우드가 그들이 직면할 수 있는 여러 과제를 어떻게 해결할 수 있는지 알아보겠습니다:

* 대량의 데이터 저장: 큰 서버를 구매, 관리 및 보호하는 대신, Azure Cosmos DB, Azure SQL Database, Azure Data Lake Storage와 같은 솔루션을 사용하여 데이터를 클라우드에 직접 저장할 수 있습니다.
* 데이터 통합 수행: 데이터 통합은 데이터 과학의 필수적인 부분으로, 데이터 수집에서 행동으로 전환할 수 있게 합니다. 클라우드에서 제공되는 데이터 통합 서비스를 사용하면 다양한 소스에서 데이터를 수집, 변환 및 통합하여 단일 데이터 웨어하우스로 만들 수 있습니다(Data Factory 사용).
* 데이터 처리: 방대한 데이터를 처리하려면 많은 컴퓨팅 파워가 필요하며, 모든 사람이 강력한 기계를 사용할 수 있는 것은 아닙니다. 그래서 많은 사람들이 클라우드의 막대한 컴퓨팅 파워를 활용하여 솔루션을 실행하고 배포합니다.
* 데이터 분석 서비스 사용: Azure Synapse Analytics, Azure Stream Analytics, Azure Databricks와 같은 클라우드 서비스를 사용하여 데이터를 실행 가능한 인사이트로 전환할 수 있습니다.
* 머신 러닝 및 데이터 지능 서비스 사용: 처음부터 시작하는 대신 클라우드 제공업체가 제공하는 머신 러닝 알고리즘을 사용할 수 있으며, AzureML과 같은 서비스를 활용할 수 있습니다. 또한 음성-텍스트 변환, 텍스트-음성 변환, 컴퓨터 비전 등과 같은 인지 서비스를 사용할 수 있습니다.

## 클라우드에서의 데이터 과학 예시

몇 가지 시나리오를 통해 이를 더 구체적으로 살펴보겠습니다.

### 실시간 소셜 미디어 감정 분석
머신 러닝을 시작하는 사람들이 흔히 연구하는 시나리오인 실시간 소셜 미디어 감정 분석을 살펴보겠습니다.

뉴스 미디어 웹사이트를 운영한다고 가정하고, 독자가 관심을 가질 만한 콘텐츠를 이해하기 위해 실시간 데이터를 활용하고 싶다고 해봅시다. 이를 위해 Twitter 게시물 데이터를 실시간으로 분석하여 독자와 관련된 주제에 대한 감정 분석을 수행하는 프로그램을 만들 수 있습니다.

주요 지표는 특정 주제(해시태그)에 대한 트윗의 양과 감정입니다. 감정은 지정된 주제에 대한 감정 분석을 수행하는 분석 도구를 사용하여 설정됩니다.

이 프로젝트를 생성하기 위해 필요한 단계는 다음과 같습니다:

* Twitter 데이터를 수집할 이벤트 허브 생성
* Twitter Streaming API를 호출할 Twitter 클라이언트 애플리케이션 구성 및 시작
* Stream Analytics 작업 생성
* 작업 입력 및 쿼리 지정
* 출력 싱크 생성 및 작업 출력 지정
* 작업 시작

전체 프로세스를 보려면 [문서](https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?WT.mc_id=academic-77958-bethanycheum&ocid=AID30411099)를 확인하세요.

### 과학 논문 분석
이 커리큘럼의 저자 중 한 명인 [Dmitry Soshnikov](http://soshnikov.com)가 만든 프로젝트를 예로 들어보겠습니다.

Dmitry는 COVID 논문을 분석하는 도구를 만들었습니다. 이 프로젝트를 검토하면 과학 논문에서 지식을 추출하고 인사이트를 얻으며, 연구자가 방대한 논문 컬렉션을 효율적으로 탐색할 수 있도록 돕는 도구를 만드는 방법을 알 수 있습니다.

다음은 사용된 단계입니다:
* [Text Analytics for Health](https://docs.microsoft.com/azure/cognitive-services/text-analytics/how-tos/text-analytics-for-health?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109)를 사용하여 정보 추출 및 전처리
* [Azure ML](https://azure.microsoft.com/services/machine-learning?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109)을 사용하여 처리 병렬화
* [Cosmos DB](https://azure.microsoft.com/services/cosmos-db?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109)를 사용하여 정보 저장 및 쿼리
* Power BI를 사용하여 데이터 탐색 및 시각화를 위한 대화형 대시보드 생성

전체 프로세스를 보려면 [Dmitry의 블로그](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/)를 방문하세요.

이처럼 클라우드 서비스를 활용하여 다양한 방식으로 데이터 과학을 수행할 수 있습니다.

## 각주

출처:
* https://azure.microsoft.com/overview/what-is-cloud-computing?ocid=AID3041109  
* https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?ocid=AID3041109  
* https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/  

## 강의 후 퀴즈

## [강의 후 퀴즈](https://ff-quizzes.netlify.app/en/ds/quiz/33)

## 과제

[시장 조사](assignment.md)

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서를 해당 언어로 작성된 상태에서 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.  