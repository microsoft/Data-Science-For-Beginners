# 클라우드에서의 데이터 사이언스 소개

|![ [(@sketchthedocs)의 스케치노트](https://sketchthedocs.dev) ](../../../sketchnotes/17-DataScience-Cloud.png)|
|:---:|
| 클라우드의 데이터 사이언스: 소개 - _[@nitya](https://twitter.com/nitya)_ 의 스케치노트 |


이 강의에서는 클라우드의 기본 원칙을 배운 다음 클라우드 서비스를 사용하여 데이터 사이언스 프로젝트를 실행하는 것이 왜 흥미로운지 알게 되고, 클라우드에서 실행되는 데이터 사이언스 프로젝트들 중 몇가지 예시를 보게 될 것이다.


## [강의전 퀴즈](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/32)


## 클라우드란?

클라우드 또는 클라우드 컴퓨팅은 인터넷을 통해 인프라에서 호스팅되는 다양한 종량제 컴퓨팅 서비스를 제공하는 것입니다. 서비스에는 스토리지, 데이터베이스, 네트워킹, 소프트웨어, 분석 및 지능형 서비스와 같은 솔루션이 포함됩니다.

일반적으로 다음과 같이 퍼블릭, 프라이빗 및 하이브리드 클라우드를 구분합니다.

* 퍼블릭 클라우드: 퍼블릭 클라우드는 인터넷을 통해 대중에게 컴퓨팅 리소스를 제공하는 타사 클라우드 서비스 제공업체가 소유하고 운영합니다.
* 프라이빗 클라우드: 단일 기업이나 조직에서 독점적으로 사용하는 클라우드 컴퓨팅 자원을 말하며, 사설망에서 서비스와 인프라를 유지 관리합니다.
* 하이브리드 클라우드: 하이브리드 클라우드는 퍼블릭 클라우드와 프라이빗 클라우드를 결합한 시스템입니다. 사용자는 온프레미스 데이터 센터를 선택하는 동시에 데이터와 애플리케이션을 하나 이상의 퍼블릭 클라우드에서 실행할 수 있습니다.

대부분의 클라우드 컴퓨팅 서비스는 IaaS(Infrastructure as a Service), PaaS(Platform as a Service) 및 SaaS(Software as a Service)의 세 가지 범주로 나뉩니다.

* IaaS(Infrastructure as a Service): 사용자는 서버 및 가상 머신(VM), 스토리지, 네트워크, 운영 체제와 같은 IT 인프라를 임대합니다.
* PaaS(Platform as a Service): 사용자는 소프트웨어 애플리케이션을 개발, 테스트, 제공 및 관리하기 위한 환경을 임대합니다. 사용자는 개발에 필요한 서버, 스토리지, 네트워크 및 데이터베이스의 기본 인프라를 설정하거나 관리하는 것에 대해 걱정할 필요가 없습니다.
* SaaS(Software as a Service): 사용자는 주문형 및 일반적으로 구독 기반으로 인터넷을 통해 소프트웨어 응용 프로그램에 액세스할 수 있습니다. 사용자는 소프트웨어 업그레이드 및 보안 패치와 같은 유지 관리, 기본 인프라 또는 소프트웨어 애플리케이션의 호스팅 및 관리에 대해 걱정할 필요가 없습니다.

가장 큰 클라우드 제공업체로는 Amazon Web Services, Google Cloud Platform 및 Microsoft Azure가 있습니다.
## 데이터 사이언스을 위해 클라우드를 선택하는 이유는 무엇입니까?

개발자와 IT 전문가는 다음을 비롯한 여러 가지 이유로 클라우드와 함께 작업하기로 결정했습니다.

* 혁신: 클라우드 공급자가 만든 혁신적인 서비스를 앱에 직접 통합하여 애플리케이션을 강화할 수 있습니다.
* 유연성: 필요한 서비스에 대해서만 비용을 지불하고 다양한 서비스 중에서 선택할 수 있습니다. 일반적으로 사용한 만큼 지불하고, 진화하는 요구 사항에 따라 서비스를 조정합니다.
* 예산: 하드웨어 및 소프트웨어 구입, 현장 데이터 센터 설정 및 실행을 위해 초기 투자를 할 필요가 없으며 사용한 만큼만 비용을 지불하면 됩니다.
* 확장성: 리소스는 프로젝트의 요구 사항에 따라 확장될 수 있습니다. 즉, 앱은 주어진 시간에 외부 요인에 적응하여 컴퓨팅 성능, 스토리지 및 대역폭을 어느 정도 사용할 수 있습니다.
* 생산성: 데이터 센터 관리와 같이 다른 사람이 관리할 수 있는 작업에 시간을 할애하지 않고 비즈니스에 집중할 수 있습니다.
* 안정성: 클라우드 컴퓨팅은 데이터를 지속적으로 백업할 수 있는 여러 가지 방법을 제공하며 위기 상황에서도 비즈니스와 서비스를 계속 운영할 수 있도록 재해 복구 계획을 세울 수 있습니다.
* 보안: 프로젝트 보안을 강화하는 정책, 기술 및 제어의 이점을 누릴 수 있습니다.

 사람들이 클라우드 서비스를 선택하는 가장 일반적인 이유 중 일부는 다음과 같습니다. 이제 클라우드가 무엇이고 주요 이점이 무엇인지 더 잘 이해했으므로 데이터를 다루는 데이터 과학자 및 개발자의 작업과, 그들이 직면할 수 있는 여러 문제를 클라우드가  어떻게 도울 수 있는지 자세히 살펴보겠습니다.

* 대용량 데이터 저장: 대용량 서버를 구입, 관리 및 보호하는 대신 Azure Cosmos DB, Azure SQL Database 및 Azure Data Lake Storage와 같은 솔루션을 사용하여 클라우드에 직접 데이터를 저장할 수 있습니다.
* 데이터 통합 ​​수행: 데이터 통합은 데이터 수집에서 데이터 변환을 수행할 수 있도록 변환해주는 데이터 사이언스의 필수 부분입니다. 클라우드에서 제공되는 데이터 통합 ​​서비스를 사용하면 Data Factory를 사용하여 다양한 소스의 데이터를 수집, 변환 및 단일 데이터 웨어하우스로 통합할 수 있습니다.
* 데이터 처리: 방대한 양의 데이터를 처리하려면 많은 컴퓨팅 성능이 필요하며 모든 사람이 그에 적합한 강력한 시스템에 액세스할 수 있는 것은 아닙니다. 그래서 많은 사람들이 클라우드의 엄청난 컴퓨팅 성능을 직접 활용하여 솔루션을 실행하고 배포하는 방법을 선택합니다.
* 데이터 분석 서비스 사용: 데이터를 실행 가능한 통찰력으로 전환하는 데 도움이 되는 Azure Synapse Analytics, Azure Stream Analytics 및 Azure Databricks와 같은 클라우드 서비스가 있습니다.
* 기계 학습 및 데이터 인텔리전스(data intelligence) 서비스 사용: 처음부터 시작하는 대신 AzureML과 같은 서비스와 함께 클라우드 공급자가 제공하는 기계 학습 알고리즘을 사용할 수 있습니다. 또한 음성을 텍스트로 변환, 텍스트를 음성으로 변환, 컴퓨터 비전 등과 같은 인지 서비스를 사용할 수 있습니다.

## 클라우드 데이터 사이언스의 예

몇 가지 시나리오를 살펴봄으로 더 확실히 이해해봅시다.
 
### 실시간 소셜 미디어 감성 분석
기계 학습을 시작하는 사람들이 일반적으로 연구하는 시나리오인 실시간 소셜 미디어 감정 분석부터 시작하겠습니다.

뉴스 미디어 웹사이트를 운영 중이고 실시간 데이터를 활용하여 독자들이 어떤 콘텐츠에 관심을 가질 수 있는지 이해하고 싶다고 가정해 보겠습니다. 이에 대해 자세히 알아보기 위해, 독자와 관련된 주제에 대해, Twitter 출판물의 데이터에 대한 실시간 감정 분석을 수행하는 프로그램을 구축할 수 있습니다.

주요 지표는 특정 주제(해시태그)에 대한 트윗의 양과 특정 주제에 대한 감정 분석을 수행하는 분석 도구를 사용하여 설정한 감정입니다.

이 프로젝트를 만드는 데 필요한 단계는 다음과 같습니다.

* Twitter에서 데이터를 수집할 스트리밍 입력을 위한 이벤트 허브 만들기
* Twitter 스트리밍 API를 호출할 Twitter 클라이언트 애플리케이션 구성 및 시작
* Stream Analytics 작업 만들기
* 작업 입력 및 쿼리 지정
* 출력 싱크 생성 및 작업 출력 지정
* Job 실행

전체 프로세스를 보려면 [문서](https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?WT.mc_id=academic-77958-bethanycheum&ocid)를 확인하세요. =AID30411099).
### 과학 논문 분석
이 커리큘럼의 저자 중 한 명인 [Dmitry Soshnikov](http://soshnikov.com)가 만든 프로젝트의 또 다른 예를 들어보겠습니다.

Dmitry는 COVID 논문을 분석하는 도구를 만들었습니다. 이 프로젝트를 검토하면 과학 논문에서 지식을 추출하고 통찰력을 얻으며 연구자가 효율적인 방식으로 방대한 논문 컬렉션을 탐색하는 데 도움이 되는 도구를 만드는 방법을 알 수 있습니다.

이를 위해 사용된 다양한 단계를 살펴보겠습니다.
* [Text Analytics for Health](https://docs.microsoft.com/azure/cognitive-services/text-analytics/how-tos/text-analytics-for-health?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109)로 정보 추출 및 전처리
* [Azure ML](https://azure.microsoft.com/services/machine-learning?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109)을 사용하여 처리 병렬화
* [Cosmos DB](https://azure.microsoft.com/services/cosmos-db?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109)로 정보 저장 및 조회
* Power BI를 사용하여 데이터 탐색 및 시각화를 위한 대화형 대시보드 만들기

전체 과정을 보려면 [Dmitry의 블로그](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/)를 방문하세요.
 
보시다시피 클라우드 서비스를 다양한 방식으로 활용하여 데이터 사이언스을 수행할 수 있습니다.
## 각주

출처:
* https://azure.microsoft.com/overview/what-is-cloud-computing?ocid=AID3041109
* https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?ocid=AID3041109
* https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/

## 강의 후 퀴즈

[강의 후 퀴즈](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/33)

## 과제

[시장조사](./assignment.ko.md)
