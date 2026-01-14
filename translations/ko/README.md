<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7c31d1a22c746b1d0f0582d4f54702ba",
  "translation_date": "2025-12-24T23:04:32+00:00",
  "source_file": "README.md",
  "language_code": "ko"
}
-->
# 초보자를 위한 데이터 사이언스 - 커리큘럼

[![GitHub Codespaces에서 열기](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?hide_repo_select=true&ref=main&repo=344191198)

[![GitHub 라이선스](https://img.shields.io/github/license/microsoft/Data-Science-For-Beginners.svg)](https://github.com/microsoft/Data-Science-For-Beginners/blob/master/LICENSE)
[![GitHub 기여자](https://img.shields.io/github/contributors/microsoft/Data-Science-For-Beginners.svg)](https://GitHub.com/microsoft/Data-Science-For-Beginners/graphs/contributors/)
[![GitHub 이슈](https://img.shields.io/github/issues/microsoft/Data-Science-For-Beginners.svg)](https://GitHub.com/microsoft/Data-Science-For-Beginners/issues/)
[![GitHub 풀 리퀘스트](https://img.shields.io/github/issues-pr/microsoft/Data-Science-For-Beginners.svg)](https://GitHub.com/microsoft/Data-Science-For-Beginners/pulls/)
[![PR 환영](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![GitHub 관찰자](https://img.shields.io/github/watchers/microsoft/Data-Science-For-Beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/Data-Science-For-Beginners/watchers/)
[![GitHub 포크](https://img.shields.io/github/forks/microsoft/Data-Science-For-Beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/Data-Science-For-Beginners/network/)
[![GitHub 스타](https://img.shields.io/github/stars/microsoft/Data-Science-For-Beginners.svg?style=social&label=Star)](https://GitHub.com/microsoft/Data-Science-For-Beginners/stargazers/)


[![Microsoft Foundry 디스코드](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Microsoft Foundry 개발자 포럼](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

마이크로소프트의 Azure Cloud Advocates는 데이터 사이언스에 관한 10주, 20강짜리 커리큘럼을 제공합니다. 각 강의에는 강의 전/후 퀴즈, 강의를 완료하기 위한 서면 지침, 솔루션 및 과제가 포함되어 있습니다. 프로젝트 기반 교수법은 학습하면서 직접 만들도록 하여 새로운 기술이 잘 '정착'되도록 돕는 입증된 방법입니다.

**저자들께 깊이 감사드립니다:** [Jasmine Greenaway](https://www.twitter.com/paladique), [Dmitry Soshnikov](http://soshnikov.com), [Nitya Narasimhan](https://twitter.com/nitya), [Jalen McGee](https://twitter.com/JalenMcG), [Jen Looper](https://twitter.com/jenlooper), [Maud Levy](https://twitter.com/maudstweets), [Tiffany Souterre](https://twitter.com/TiffanySouterre), [Christopher Harrison](https://www.twitter.com/geektrainer).

**🙏 특별 감사 🙏 우리 [Microsoft 학생 홍보대사](https://studentambassadors.microsoft.com/) 저자, 검토자 및 콘텐츠 기여자들에게,** 특히 Aaryan Arora, [Aditya Garg](https://github.com/AdityaGarg00), [Alondra Sanchez](https://www.linkedin.com/in/alondra-sanchez-molina/), [Ankita Singh](https://www.linkedin.com/in/ankitasingh007), [Anupam Mishra](https://www.linkedin.com/in/anupam--mishra/), [Arpita Das](https://www.linkedin.com/in/arpitadas01/), ChhailBihari Dubey, [Dibri Nsofor](https://www.linkedin.com/in/dibrinsofor), [Dishita Bhasin](https://www.linkedin.com/in/dishita-bhasin-7065281bb), [Majd Safi](https://www.linkedin.com/in/majd-s/), [Max Blum](https://www.linkedin.com/in/max-blum-6036a1186/), [Miguel Correa](https://www.linkedin.com/in/miguelmque/), [Mohamma Iftekher (Iftu) Ebne Jalal](https://twitter.com/iftu119), [Nawrin Tabassum](https://www.linkedin.com/in/nawrin-tabassum), [Raymond Wangsa Putra](https://www.linkedin.com/in/raymond-wp/), [Rohit Yadav](https://www.linkedin.com/in/rty2423), Samridhi Sharma, [Sanya Sinha](https://www.linkedin.com/mwlite/in/sanya-sinha-13aab1200),
[Sheena Narula](https://www.linkedin.com/in/sheena-narua-n/), [Tauqeer Ahmad](https://www.linkedin.com/in/tauqeerahmad5201/), Yogendrasingh Pawar , [Vidushi Gupta](https://www.linkedin.com/in/vidushi-gupta07/), [Jasleen Sondhi](https://www.linkedin.com/in/jasleen-sondhi/)

|![스케치노트 작성자 @sketchthedocs https://sketchthedocs.dev](../../translated_images/00-Title.8af36cd35da1ac555b678627fbdc6e320c75f0100876ea41d30ea205d3b08d22.ko.png)|
|:---:|
| 초보자를 위한 데이터 사이언스 - _스케치노트 작성자 [@nitya](https://twitter.com/nitya)_ |

### 🌐 다국어 지원

#### GitHub 액션을 통해 지원 (자동화 및 항상 최신 유지)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[아랍어](../ar/README.md) | [벵골어](../bn/README.md) | [불가리아어](../bg/README.md) | [버마어 (미얀마)](../my/README.md) | [중국어(간체)](../zh/README.md) | [중국어(번체, 홍콩)](../hk/README.md) | [중국어(번체, 마카오)](../mo/README.md) | [중국어(번체, 대만)](../tw/README.md) | [크로아티아어](../hr/README.md) | [체코어](../cs/README.md) | [덴마크어](../da/README.md) | [네덜란드어](../nl/README.md) | [에스토니아어](../et/README.md) | [핀란드어](../fi/README.md) | [프랑스어](../fr/README.md) | [독일어](../de/README.md) | [그리스어](../el/README.md) | [히브리어](../he/README.md) | [힌디어](../hi/README.md) | [헝가리어](../hu/README.md) | [인도네시아어](../id/README.md) | [이탈리아어](../it/README.md) | [일본어](../ja/README.md) | [칸나다어](../kn/README.md) | [한국어](./README.md) | [리투아니아어](../lt/README.md) | [말레이어](../ms/README.md) | [말라얄람어](../ml/README.md) | [마라티어](../mr/README.md) | [네팔어](../ne/README.md) | [나이지리아 피진어](../pcm/README.md) | [노르웨이어](../no/README.md) | [페르시아어(파르시)](../fa/README.md) | [폴란드어](../pl/README.md) | [포르투갈어(브라질)](../br/README.md) | [포르투갈어(포르투갈)](../pt/README.md) | [펀자브어(구르무키)](../pa/README.md) | [루마니아어](../ro/README.md) | [러시아어](../ru/README.md) | [세르비아어(키릴)](../sr/README.md) | [슬로바키아어](../sk/README.md) | [슬로베니아어](../sl/README.md) | [스페인어](../es/README.md) | [스와힐리어](../sw/README.md) | [스웨덴어](../sv/README.md) | [타갈로그어(필리핀)](../tl/README.md) | [타밀어](../ta/README.md) | [텔루구어](../te/README.md) | [태국어](../th/README.md) | [터키어](../tr/README.md) | [우크라이나어](../uk/README.md) | [우르두어](../ur/README.md) | [베트남어](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**추가 번역을 원하시면 지원되는 언어 목록은 [여기](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**

#### 커뮤니티에 참여하세요 
[![Microsoft Foundry 디스코드](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

우리는 Discord에서 Learn with AI 시리즈를 진행하고 있습니다. 자세한 내용 및 참여는 [AI와 함께 배우기 시리즈](https://aka.ms/learnwithai/discord)에서 확인하세요. 기간: 2025년 9월 18일 - 30일. GitHub Copilot을 데이터 사이언스에 활용하는 팁과 요령을 얻을 수 있습니다.

![AI와 함께 배우기 시리즈](../../translated_images/1.2b28cdc6205e26fef6a21817fe5d83ae8b50fbd0a33e9fed0df05845da5b30b6.ko.jpg)

# 학생이신가요?

다음 리소스로 시작하세요:

- [학생 허브 페이지](https://docs.microsoft.com/en-gb/learn/student-hub?WT.mc_id=academic-77958-bethanycheum) 이 페이지에서는 초보자용 리소스, 학생 팩 및 무료 인증 바우처를 받을 수 있는 방법 등을 찾아볼 수 있습니다. 이 페이지는 즐겨찾기에 추가해 두고 최소 한 달에 한 번씩 내용을 교체하므로 가끔 확인하는 것이 좋습니다.
- [Microsoft Learn 학생 홍보대사](https://studentambassadors.microsoft.com?WT.mc_id=academic-77958-bethanycheum) 전 세계 학생 홍보대사 커뮤니티에 참여하세요. 이것이 마이크로소프트에 들어가는 하나의 방법이 될 수 있습니다.

# 시작하기

## 📚 문서

- **[설치 가이드](INSTALLATION.md)** - 초보자를 위한 단계별 설정 지침
- **[사용 가이드](USAGE.md)** - 예제 및 일반적인 워크플로
- **[문제 해결](TROUBLESHOOTING.md)** - 일반적인 문제 해결 방법
- **[기여 가이드](CONTRIBUTING.md)** - 이 프로젝트에 기여하는 방법
- **[교사용 자료](for-teachers.md)** - 교수 안내 및 수업 자료

## 👨‍🎓 학생을 위한 안내
> **완전 초보자**: 데이터 과학이 처음이신가요? [초보자 친화적인 예제](examples/README.md)로 시작하세요! 이러한 간단하고 주석이 잘 달린 예제들은 전체 커리큘럼에 들어가기 전에 기본을 이해하는 데 도움이 됩니다.
> **[Students](https://aka.ms/student-page)**: 이 커리큘럼을 스스로 사용하려면 리포지토리를 포크하고 강의 전 퀴즈부터 시작하여 연습 문제들을 스스로 완료하세요. 그런 다음 강의를 읽고 나머지 활동을 완료하세요. 솔루션 코드를 복사하기보다는 강의를 이해하면서 프로젝트를 만드는 것을 시도해 보세요; 하지만 해당 코드는 각 프로젝트 지향 수업의 /solutions 폴더에서 제공됩니다. 또 다른 방법은 친구들과 스터디 그룹을 만들어 함께 콘텐츠를 진행하는 것입니다. 추가 학습을 위해 [Microsoft Learn](https://docs.microsoft.com/en-us/users/jenlooper-2911/collections/qprpajyoy3x0g7?WT.mc_id=academic-77958-bethanycheum)을 권장합니다.

**빠른 시작:**
1. 환경을 설정하려면 [설치 가이드](INSTALLATION.md)를 확인하세요
2. 커리큘럼 작업 방법을 배우려면 [사용 가이드](USAGE.md)를 검토하세요
3. 1과부터 시작하여 순차적으로 진행하세요
4. 지원을 위해 [Discord 커뮤니티](https://aka.ms/ds4beginners/discord)에 참여하세요

## 👩‍🏫 교사용

> **교사 분들**: 이 커리큘럼을 사용하는 방법에 대한 [몇 가지 제안](for-teachers.md)을 포함했습니다. 의견을 [토론 포럼](https://github.com/microsoft/Data-Science-For-Beginners/discussions)에서 알려주세요!

## 팀을 만나보세요

[![프로모션 비디오](../../ds-for-beginners.gif)](https://youtu.be/8mzavjQSMM4 "프로모션 비디오")

**GIF 제작자** [Mohit Jaisal](https://www.linkedin.com/in/mohitjaisal)
> 🎥 위 이미지를 클릭하면 프로젝트  그것을 만든 사람들에 대한 비디오를 볼 수 있습니다!

## 교수법

우리는 이 커리큘럼을 구성하면서 두 가지 교수법적 원칙을 선택했습니다: 프로젝트 기반 학습을 보장하고 자주 퀴즈를 포함하는 것입니다. 이 시리즈가 끝날 무렵, 학생들은 윤리적 개념, 데이터 준비, 다양한 데이터 작업 방식, 데이터 시각화, 데이터 분석, 데이터 과학의 실제 사용 사례 등 데이터 과학의 기본 원리를 배우게 됩니다.

또한 수업 전의 낮은 부담의 퀴즈는 학생이 주제 학습에 의도를 설정하게 하고, 수업 후의 두 번째 퀴즈는 추가적인 기억 유지에 도움을 줍니다. 이 커리큘럼은 유연하고 재미있게 설계되었으며 전체 또는 일부만 수강할 수 있습니다. 프로젝트는 작게 시작하여 10주 사이클의 끝에 점점 더 복잡해집니다.

> 다음 문서를 확인하세요: [행동 강령](CODE_OF_CONDUCT.md), [기여 안내](CONTRIBUTING.md),  [번역](TRANSLATIONS.md) 지침. 건설적인 피드백을 환영합니다!

## 각 수업에는 다음이 포함됩니다:

- 선택적 스케치노트
- 선택적 보조 비디오
- 수업 전 준비 퀴즈
- 서면 강의
- 프로젝트 기반 수업의 경우 프로젝트를 만드는 단계별 가이드
- 지식 점검
- 도전 과제
- 보조 읽을거리
- 과제
- [수업 후 퀴즈](https://ff-quizzes.netlify.app/en/)

> **퀴즈에 대한 참고**: 모든 퀴즈는 Quiz-App 폴더에 포함되어 있으며, 총 40개의 퀴즈(각 3문제)가 있습니다. 퀴즈들은 수업 내에서 링크되어 있지만, 퀴즈 앱은 로컬에서 실행하거나 Azure에 배포할 수 있습니다; `quiz-app` 폴더의 지침을 따르세요. 퀴즈는 점진적으로 현지화되고 있습니다.

## 🎓 초보자 친화적 예제

**데이터 과학이 처음이신가요?** 우리는 시작하는 데 도움이 되는 간단하고 주석이 잘 달린 코드를 포함한 특별한 [예제 디렉터리](examples/README.md)를 만들었습니다:

- 🌟 **Hello World** - 당신의 첫 번째 데이터 과학 프로그램
- 📂 **Loading Data** - 데이터셋을 읽고 탐색하는 방법 배우기
- 📊 **Simple Analysis** - 통계를 계산하고 패턴 찾기
- 📈 **Basic Visualization** - 차트와 그래프 만들기
- 🔬 **Real-World Project** - 시작부터 끝까지 전체 워크플로우

각 예제는 모든 단계를 설명하는 자세한 주석을 포함하고 있어 절대 초보자에게 적합합니다!

👉 **[예제부터 시작하기](examples/README.md)** 👈

## Lessons


|![ 스케치노트 작성자 @sketchthedocs https://sketchthedocs.dev](../../translated_images/00-Roadmap.4905d6567dff47532b9bfb8e0b8980fc6b0b1292eebb24181c1a9753b33bc0f5.ko.png)|
|:---:|
| 초보자를 위한 데이터 과학: 로드맵 - _스케치노트 작성자 [@nitya](https://twitter.com/nitya)_ |


| 수업 번호 | 주제 | 수업 분류 | 학습 목표 | 연결된 수업 | 저자 |
| :-----------: | :----------------------------------------: | :--------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------: | :----: |
| 01 | 데이터 과학 정의 | [Introduction](1-Introduction/README.md) | 데이터 과학의 기본 개념과 그것이 인공지능, 머신러닝, 빅데이터와 어떻게 관련되는지 배우세요. | [수업](1-Introduction/01-defining-data-science/README.md) [비디오](https://youtu.be/beZ7Mb_oz9I) | [Dmitry](http://soshnikov.com) |
| 02 | 데이터 과학 윤리 | [Introduction](1-Introduction/README.md) | 데이터 윤리 개념, 과제 및 프레임워크. | [수업](1-Introduction/02-ethics/README.md) | [Nitya](https://twitter.com/nitya) |
| 03 | 데이터 정의 | [Introduction](1-Introduction/README.md) | 데이터가 어떻게 분류되고 그 일반적인 출처는 무엇인지. | [수업](1-Introduction/03-defining-data/README.md) | [Jasmine](https://www.twitter.com/paladique) |
| 04 | 통계학 및 확률 소개 | [Introduction](1-Introduction/README.md) | 데이터를 이해하기 위한 확률 및 통계의 수학적 기법. | [수업](1-Introduction/04-stats-and-probability/README.md) [비디오](https://youtu.be/Z5Zy85g4Yjw) | [Dmitry](http://soshnikov.com) |
| 05 | 관계형 데이터 작업 | [Working With Data](2-Working-With-Data/README.md) | 관계형 데이터 소개 및 구조화된 질의 언어(Structured Query Language, 약칭 SQL, 발음 “see-quell”)를 사용하여 관계형 데이터를 탐색하고 분석하는 기초. | [수업](2-Working-With-Data/05-relational-databases/README.md) | [Christopher](https://www.twitter.com/geektrainer) | | |
| 06 | 비관계형 데이터 작업 | [Working With Data](2-Working-With-Data/README.md) | 비관계형 데이터, 그 다양한 유형 및 문서형 데이터베이스를 탐색하고 분석하는 기초. | [수업](2-Working-With-Data/06-non-relational/README.md) | [Jasmine](https://twitter.com/paladique)|
| 07 | Python으로 작업하기 | [Working With Data](2-Working-With-Data/README.md) | Pandas와 같은 라이브러리를 사용한 데이터 탐색을 위한 Python 사용 기초. Python 프로그래밍의 기초 이해가 권장됩니다. | [수업](2-Working-With-Data/07-python/README.md) [비디오](https://youtu.be/dZjWOGbsN4Y) | [Dmitry](http://soshnikov.com) |
| 08 | 데이터 준비 | [Working With Data](2-Working-With-Data/README.md) | 결측, 부정확 또는 불완전한 데이터를 처리하기 위한 정리 및 변환 기술. | [수업](2-Working-With-Data/08-data-preparation/README.md) | [Jasmine](https://www.twitter.com/paladique) |
| 09 | 수량 시각화 | [Data Visualization](3-Data-Visualization/README.md) | Matplotlib를 사용하여 새 데이터를 시각화하는 방법을 배우세요 🦆 | [수업](3-Data-Visualization/09-visualization-quantities/README.md) | [Jen](https://twitter.com/jenlooper) |
| 10 | 데이터 분포 시각화 | [Data Visualization](3-Data-Visualization/README.md) | 구간 내 관측값과 추세 시각화. | [수업](3-Data-Visualization/10-visualization-distributions/README.md) | [Jen](https://twitter.com/jenlooper) |
| 11 | 비율 시각화 | [Data Visualization](3-Data-Visualization/README.md) | 이산적 및 그룹화된 백분율 시각화. | [수업](3-Data-Visualization/11-visualization-proportions/README.md) | [Jen](https://twitter.com/jenlooper) |
| 12 | 관계 시각화 | [Data Visualization](3-Data-Visualization/README.md) | 데이터 집합과 변수들 간의 연결 및 상관관계 시각화. | [수업](3-Data-Visualization/12-visualization-relationships/README.md) | [Jen](https://twitter.com/jenlooper) |
| 13 | 의미 있는 시각화 | [Data Visualization](3-Data-Visualization/README.md) | 효과적인 문제 해결과 인사이트 도출을 위해 시각화를 가치 있게 만드는 기술과 지침. | [수업](3-Data-Visualization/13-meaningful-visualizations/README.md) | [Jen](https://twitter.com/jenlooper) |
| 14 | 데이터 과학 수명주기 소개 | [Lifecycle](4-Data-Science-Lifecycle/README.md) | 데이터 과학 수명주기 소개와 데이터 수집 및 추출이라는 첫 단계. | [수업](4-Data-Science-Lifecycle/14-Introduction/README.md) | [Jasmine](https://twitter.com/paladique) |
| 15 | 분석 | [Lifecycle](4-Data-Science-Lifecycle/README.md) | 데이터 과학 수명주기의 이 단계는 데이터를 분석하는 기법에 초점을 맞춥니다. | [수업](4-Data-Science-Lifecycle/15-analyzing/README.md) | [Jasmine](https://twitter.com/paladique) | | |
| 16 | 커뮤니케이션 | [Lifecycle](4-Data-Science-Lifecycle/README.md) | 데이터의 통찰을 의사결정자가 이해하기 쉽게 제시하는 것에 초점을 맞춘 데이터 과학 수명주기의 단계. | [수업](4-Data-Science-Lifecycle/16-communication/README.md) | [Jalen](https://twitter.com/JalenMcG) | | |
| 17 | 클라우드에서의 데이터 과학 | [Cloud Data](5-Data-Science-In-Cloud/README.md) | 클라우드에서의 데이터 과학과 그 이점을 소개하는 일련의 수업입니다. | [수업](5-Data-Science-In-Cloud/17-Introduction/README.md) | [Tiffany](https://twitter.com/TiffanySouterre) and [Maud](https://twitter.com/maudstweets) |
| 18 | 클라우드에서의 데이터 과학 | [Cloud Data](5-Data-Science-In-Cloud/README.md) | Low Code 도구를 사용하여 모델을 학습시키기. |[수업](5-Data-Science-In-Cloud/18-Low-Code/README.md) | [Tiffany](https://twitter.com/TiffanySouterre) and [Maud](https://twitter.com/maudstweets) |
| 19 | 클라우드에서의 데이터 과학 | [Cloud Data](5-Data-Science-In-Cloud/README.md) | Azure Machine Learning Studio로 모델 배포. | [수업](5-Data-Science-In-Cloud/19-Azure/README.md)| [Tiffany](https://twitter.com/TiffanySouterre) and [Maud](https://twitter.com/maudstweets) |
| 20 | 현장의 데이터 과학 | [In the Wild](6-Data-Science-In-Wild/README.md) | 실제 세계에서의 데이터 과학 기반 프로젝트. | [수업](6-Data-Science-In-Wild/20-Real-World-Examples/README.md) | [Nitya](https://twitter.com/nitya) |

## GitHub Codespaces

Follow these steps to open this sample in a Codespace:
1. Code 드롭다운 메뉴를 클릭한 다음 Open with Codespaces 옵션을 선택하세요.
2. 창의 하단 패널에서 + New codespace를 선택하세요.
For more info, check out the [GitHub documentation](https://docs.github.com/en/codespaces/developing-in-codespaces/creating-a-codespace-for-a-repository#creating-a-codespace).

## VSCode Remote - Containers
Follow these steps to open this repo in a container using your local machine and VSCode using  the VS Code Remote - Containers extension:

1. If this is your first time using a development container, please ensure your system meets the pre-reqs (i.e. have Docker installed) in [the getting started documentation](https://code.visualstudio.com/docs/devcontainers/containers#_getting-started).

To use this repository, you can either open the repository in an isolated Docker volume:

**Note**: Under the hood, this will use the Remote-Containers: **Clone Repository in Container Volume...** command to clone the source code in a Docker volume instead of the local filesystem. [Volumes](https://docs.docker.com/storage/volumes/) are the preferred mechanism for persisting container data.

Or open a locally cloned or downloaded version of the repository:

- 이 저장소를 로컬 파일시스템에 복제하세요.
- F1을 누른 다음 **Remote-Containers: Open Folder in Container...** 명령을 선택하세요.
- 복제한 이 폴더를 선택하고 컨테이너가 시작될 때까지 기다린 다음 사용해 보세요.

## Offline access

You can run this documentation offline by using [Docsify](https://docsify.js.org/#/). Fork this repo, [install Docsify](https://docsify.js.org/#/quickstart) on your local machine,  then in the root folder of this repo, type `docsify serve`. The website will be served on port 3000 on your localhost: `localhost:3000`.

> 참고: Docsify에서는 노트북이 렌더링되지 않으므로 노트북을 실행해야 하는 경우 VS Code에서 Python 커널을 실행하여 별도로 수행하세요.

## Other Curricula

Our team produces other curricula! Check out:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j for Beginners](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js for Beginners](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / Agents
[![초보자를 위한 AZD](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![초보자를 위한 Edge AI](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![초보자를 위한 MCP](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![초보자를 위한 AI 에이전트](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### 생성형 AI 시리즈
[![초보자를 위한 생성형 AI](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![생성형 AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![생성형 AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![생성형 AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### 핵심 학습
[![초보자를 위한 ML](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![초보자를 위한 데이터 과학](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![초보자를 위한 AI](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![초보자를 위한 사이버보안](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![초보자를 위한 웹 개발](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![초보자를 위한 IoT](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![초보자를 위한 XR 개발](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### 코파일럿 시리즈
[![AI 페어 프로그래밍을 위한 Copilot](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![C#/.NET을 위한 Copilot](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot 어드벤처](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## 도움받기

**문제가 발생했나요?** 일반적인 문제에 대한 해결책은 [문제 해결 안내서](TROUBLESHOOTING.md)에서 확인하세요.

AI 앱을 만드는 동안 막히거나 질문이 있나요? MCP에 대해 다른 학습자 및 경험 많은 개발자들과 토론에 참여하세요. 질문을 환영하고 지식을 자유롭게 공유하는 지원 커뮤니티입니다.

[![Microsoft Foundry 디스코드](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

제품에 대한 피드백이나 빌드 중 발생한 오류가 있으면 다음을 방문하세요:

[![Microsoft Foundry 개발자 포럼](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
면책 조항:
이 문서는 AI 번역 서비스인 Co-op Translator(https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있으나 자동 번역에는 오류나 부정확성이 포함될 수 있음을 알려드립니다. 원문(원어) 문서를 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역의 사용으로 인해 발생하는 오해나 잘못된 해석에 대해서는 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->