<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6bb17a440fdabf0823105136a5b81029",
  "translation_date": "2025-08-25T16:07:16+00:00",
  "source_file": "README.md",
  "language_code": "ko"
}
-->
# 데이터 과학 입문 - 커리큘럼

Azure Cloud Advocates는 데이터 과학에 관한 10주, 20강의 커리큘럼을 제공합니다. 각 강의는 사전 및 사후 퀴즈, 강의 내용을 완성하기 위한 작성 지침, 솔루션, 과제를 포함합니다. 프로젝트 기반 학습 방식은 새로운 기술을 효과적으로 익히는 검증된 방법입니다.

**저자들에게 깊은 감사의 마음을 전합니다:** [Jasmine Greenaway](https://www.twitter.com/paladique), [Dmitry Soshnikov](http://soshnikov.com), [Nitya Narasimhan](https://twitter.com/nitya), [Jalen McGee](https://twitter.com/JalenMcG), [Jen Looper](https://twitter.com/jenlooper), [Maud Levy](https://twitter.com/maudstweets), [Tiffany Souterre](https://twitter.com/TiffanySouterre), [Christopher Harrison](https://www.twitter.com/geektrainer).

**🙏 특별히 감사드립니다 🙏 [Microsoft Student Ambassador](https://studentambassadors.microsoft.com/) 저자, 리뷰어 및 콘텐츠 기여자들,** 특히 Aaryan Arora, [Aditya Garg](https://github.com/AdityaGarg00), [Alondra Sanchez](https://www.linkedin.com/in/alondra-sanchez-molina/), [Ankita Singh](https://www.linkedin.com/in/ankitasingh007), [Anupam Mishra](https://www.linkedin.com/in/anupam--mishra/), [Arpita Das](https://www.linkedin.com/in/arpitadas01/), ChhailBihari Dubey, [Dibri Nsofor](https://www.linkedin.com/in/dibrinsofor), [Dishita Bhasin](https://www.linkedin.com/in/dishita-bhasin-7065281bb), [Majd Safi](https://www.linkedin.com/in/majd-s/), [Max Blum](https://www.linkedin.com/in/max-blum-6036a1186/), [Miguel Correa](https://www.linkedin.com/in/miguelmque/), [Mohamma Iftekher (Iftu) Ebne Jalal](https://twitter.com/iftu119), [Nawrin Tabassum](https://www.linkedin.com/in/nawrin-tabassum), [Raymond Wangsa Putra](https://www.linkedin.com/in/raymond-wp/), [Rohit Yadav](https://www.linkedin.com/in/rty2423), Samridhi Sharma, [Sanya Sinha](https://www.linkedin.com/mwlite/in/sanya-sinha-13aab1200), [Sheena Narula](https://www.linkedin.com/in/sheena-narua-n/), [Tauqeer Ahmad](https://www.linkedin.com/in/tauqeerahmad5201/), Yogendrasingh Pawar, [Vidushi Gupta](https://www.linkedin.com/in/vidushi-gupta07/), [Jasleen Sondhi](https://www.linkedin.com/in/jasleen-sondhi/)

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](./sketchnotes/00-Title.png)|
|:---:|
| 데이터 과학 입문 - _스케치노트 by [@nitya](https://twitter.com/nitya)_ |

## 공지 - 생성형 AI에 관한 새로운 커리큘럼이 출시되었습니다!

12강으로 구성된 생성형 AI 커리큘럼이 새롭게 출시되었습니다. 다음과 같은 내용을 배울 수 있습니다:

- 프롬프트 및 프롬프트 엔지니어링
- 텍스트 및 이미지 앱 생성
- 검색 앱

강의, 과제, 지식 점검 및 도전 과제가 포함되어 있습니다.

확인해보세요:

> https://aka.ms/genai-beginners

# 학생이신가요?

다음 리소스를 통해 시작해보세요:

- [Student Hub 페이지](https://docs.microsoft.com/en-gb/learn/student-hub?WT.mc_id=academic-77958-bethanycheum) 이 페이지에서는 초보자를 위한 리소스, 학생 팩, 무료 인증서 바우처를 얻는 방법 등을 찾을 수 있습니다. 이 페이지를 즐겨찾기에 추가하고 정기적으로 확인하세요. 콘텐츠는 최소 월별로 업데이트됩니다.
- [Microsoft Learn Student Ambassadors](https://studentambassadors.microsoft.com?WT.mc_id=academic-77958-bethanycheum) 글로벌 학생 대사 커뮤니티에 가입하세요. Microsoft로의 첫걸음이 될 수 있습니다.

# 시작하기

> **교사들**: 이 커리큘럼을 활용하는 방법에 대한 [제안](for-teachers.md)을 포함했습니다. [토론 포럼](https://github.com/microsoft/Data-Science-For-Beginners/discussions)에서 피드백을 공유해주세요!

> **[학생들](https://aka.ms/student-page)**: 이 커리큘럼을 독학으로 사용하려면 전체 저장소를 포크하고 사전 강의 퀴즈부터 시작하여 스스로 연습 문제를 완료하세요. 강의를 읽고 나머지 활동을 완료하세요. 솔루션 코드를 복사하기보다는 강의를 이해하며 프로젝트를 만들어보세요. 하지만 솔루션 코드는 각 프로젝트 기반 강의의 /solutions 폴더에 있습니다. 또 다른 방법은 친구들과 스터디 그룹을 만들어 함께 콘텐츠를 학습하는 것입니다. 추가 학습을 위해 [Microsoft Learn](https://docs.microsoft.com/en-us/users/jenlooper-2911/collections/qprpajyoy3x0g7?WT.mc_id=academic-77958-bethanycheum)을 추천합니다.

## 팀 소개

[![프로모션 비디오](../../ds-for-beginners.gif)](https://youtu.be/8mzavjQSMM4 "프로모션 비디오")

**Gif 제작자** [Mohit Jaisal](https://www.linkedin.com/in/mohitjaisal)

> 🎥 위 이미지를 클릭하면 프로젝트와 제작자들에 대한 비디오를 볼 수 있습니다!

## 교육 방식

이 커리큘럼을 설계할 때 두 가지 교육 원칙을 따랐습니다: 프로젝트 기반 학습과 빈번한 퀴즈 포함. 이 시리즈가 끝날 때 학생들은 데이터 과학의 기본 원칙, 윤리적 개념, 데이터 준비, 데이터 작업 방식, 데이터 시각화, 데이터 분석, 데이터 과학의 실제 사례 등을 배우게 됩니다.

또한, 수업 전에 간단한 퀴즈를 통해 학생들이 주제에 집중할 수 있도록 하고, 수업 후 퀴즈를 통해 학습 내용을 더 잘 기억할 수 있도록 합니다. 이 커리큘럼은 유연하고 재미있게 설계되었으며 전체 또는 일부만 학습할 수 있습니다. 프로젝트는 작게 시작하여 10주 과정이 끝날 때 점점 복잡해집니다.

> [행동 강령](CODE_OF_CONDUCT.md), [기여](CONTRIBUTING.md), [번역](TRANSLATIONS.md) 지침을 확인하세요. 건설적인 피드백을 환영합니다!

## 각 강의는 다음을 포함합니다:

- 선택적 스케치노트
- 선택적 보충 비디오
- 사전 강의 준비 퀴즈
- 작성된 강의
- 프로젝트 기반 강의의 경우, 프로젝트를 구축하는 단계별 가이드
- 지식 점검
- 도전 과제
- 보충 자료
- 과제
- 사후 강의 퀴즈

> **퀴즈에 대한 참고 사항**: 모든 퀴즈는 Quiz-App 폴더에 포함되어 있으며, 총 40개의 퀴즈가 각 3문제로 구성되어 있습니다. 강의 내에서 링크로 연결되어 있지만, 퀴즈 앱은 로컬에서 실행하거나 Azure에 배포할 수 있습니다. `quiz-app` 폴더의 지침을 따르세요. 퀴즈는 점차적으로 현지화되고 있습니다.

## 강의 목록

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](./sketchnotes/00-Roadmap.png)|
|:---:|
| 데이터 과학 입문: 로드맵 - _스케치노트 by [@nitya](https://twitter.com/nitya)_ |

| 강의 번호 | 주제 | 강의 그룹 | 학습 목표 | 링크된 강의 | 저자 |
| :-----------: | :----------------------------------------: | :--------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------: | :----: |
| 01 | 데이터 과학 정의 | [소개](1-Introduction/README.md) | 데이터 과학의 기본 개념과 인공지능, 머신러닝, 빅데이터와의 관계를 배웁니다. | [강의](1-Introduction/01-defining-data-science/README.md) [비디오](https://youtu.be/beZ7Mb_oz9I) | [Dmitry](http://soshnikov.com) |
| 02 | 데이터 과학 윤리 | [소개](1-Introduction/README.md) | 데이터 윤리 개념, 과제 및 프레임워크. | [강의](1-Introduction/02-ethics/README.md) | [Nitya](https://twitter.com/nitya) |
| 03 | 데이터 정의 | [소개](1-Introduction/README.md) | 데이터가 어떻게 분류되고 일반적인 출처는 무엇인지 배웁니다. | [강의](1-Introduction/03-defining-data/README.md) | [Jasmine](https://www.twitter.com/paladique) |
| 04 | 통계 및 확률 소개 | [소개](1-Introduction/README.md) | 데이터를 이해하기 위한 확률 및 통계의 수학적 기법. | [강의](1-Introduction/04-stats-and-probability/README.md) [비디오](https://youtu.be/Z5Zy85g4Yjw) | [Dmitry](http://soshnikov.com) |
| 05 | 관계형 데이터 작업 | [데이터 작업](2-Working-With-Data/README.md) | 관계형 데이터 소개 및 SQL(Structured Query Language)을 사용하여 관계형 데이터를 탐색하고 분석하는 기본 사항. | [강의](2-Working-With-Data/05-relational-databases/README.md) | [Christopher](https://www.twitter.com/geektrainer) | | |
| 06 | NoSQL 데이터 작업 | [데이터 작업](2-Working-With-Data/README.md) | 비관계형 데이터 소개, 다양한 유형 및 문서 데이터베이스를 탐색하고 분석하는 기본 사항. | [강의](2-Working-With-Data/06-non-relational/README.md) | [Jasmine](https://twitter.com/paladique)|
| 07 | Python 작업 | [데이터 작업](2-Working-With-Data/README.md) | Pandas와 같은 라이브러리를 사용하여 데이터를 탐색하는 Python 사용 기본 사항. Python 프로그래밍에 대한 기초 이해가 권장됩니다. | [강의](2-Working-With-Data/07-python/README.md) [비디오](https://youtu.be/dZjWOGbsN4Y) | [Dmitry](http://soshnikov.com) |
| 08 | 데이터 준비 | [데이터 작업하기](2-Working-With-Data/README.md) | 누락되거나 부정확하거나 불완전한 데이터를 처리하기 위한 데이터 정리 및 변환 기술에 대한 주제. | [수업](2-Working-With-Data/08-data-preparation/README.md) | [Jasmine](https://www.twitter.com/paladique) |
| 09 | 수량 시각화 | [데이터 시각화](3-Data-Visualization/README.md) | Matplotlib을 사용하여 새 데이터 🦆를 시각화하는 방법 배우기 | [수업](3-Data-Visualization/09-visualization-quantities/README.md) | [Jen](https://twitter.com/jenlooper) |
| 10 | 데이터 분포 시각화 | [데이터 시각화](3-Data-Visualization/README.md) | 특정 구간 내 관찰 및 추세를 시각화하기. | [수업](3-Data-Visualization/10-visualization-distributions/README.md) | [Jen](https://twitter.com/jenlooper) |
| 11 | 비율 시각화 | [데이터 시각화](3-Data-Visualization/README.md) | 개별 및 그룹화된 비율을 시각화하기. | [수업](3-Data-Visualization/11-visualization-proportions/README.md) | [Jen](https://twitter.com/jenlooper) |
| 12 | 관계 시각화 | [데이터 시각화](3-Data-Visualization/README.md) | 데이터 세트와 변수 간의 연결 및 상관관계를 시각화하기. | [수업](3-Data-Visualization/12-visualization-relationships/README.md) | [Jen](https://twitter.com/jenlooper) |
| 13 | 의미 있는 시각화 | [데이터 시각화](3-Data-Visualization/README.md) | 효과적인 문제 해결과 통찰력을 위한 시각화를 가치 있게 만드는 기술과 가이드. | [수업](3-Data-Visualization/13-meaningful-visualizations/README.md) | [Jen](https://twitter.com/jenlooper) |
| 14 | 데이터 과학 생애주기 소개 | [생애주기](4-Data-Science-Lifecycle/README.md) | 데이터 과학 생애주기와 데이터 획득 및 추출의 첫 번째 단계 소개. | [수업](4-Data-Science-Lifecycle/14-Introduction/README.md) | [Jasmine](https://twitter.com/paladique) |
| 15 | 분석하기 | [생애주기](4-Data-Science-Lifecycle/README.md) | 데이터 과학 생애주기의 이 단계는 데이터 분석 기술에 중점을 둡니다. | [수업](4-Data-Science-Lifecycle/15-analyzing/README.md) | [Jasmine](https://twitter.com/paladique) | | |
| 16 | 커뮤니케이션 | [생애주기](4-Data-Science-Lifecycle/README.md) | 데이터 과학 생애주기의 이 단계는 데이터에서 얻은 통찰력을 의사 결정자가 쉽게 이해할 수 있도록 제시하는 데 중점을 둡니다. | [수업](4-Data-Science-Lifecycle/16-communication/README.md) | [Jalen](https://twitter.com/JalenMcG) | | |
| 17 | 클라우드에서의 데이터 과학 | [클라우드 데이터](5-Data-Science-In-Cloud/README.md) | 클라우드에서의 데이터 과학과 그 이점을 소개하는 일련의 수업. | [수업](5-Data-Science-In-Cloud/17-Introduction/README.md) | [Tiffany](https://twitter.com/TiffanySouterre) 및 [Maud](https://twitter.com/maudstweets) |
| 18 | 클라우드에서의 데이터 과학 | [클라우드 데이터](5-Data-Science-In-Cloud/README.md) | 로우 코드 도구를 사용하여 모델 훈련하기. | [수업](5-Data-Science-In-Cloud/18-Low-Code/README.md) | [Tiffany](https://twitter.com/TiffanySouterre) 및 [Maud](https://twitter.com/maudstweets) |
| 19 | 클라우드에서의 데이터 과학 | [클라우드 데이터](5-Data-Science-In-Cloud/README.md) | Azure Machine Learning Studio를 사용하여 모델 배포하기. | [수업](5-Data-Science-In-Cloud/19-Azure/README.md) | [Tiffany](https://twitter.com/TiffanySouterre) 및 [Maud](https://twitter.com/maudstweets) |
| 20 | 실제 환경에서의 데이터 과학 | [실제 환경](6-Data-Science-In-Wild/README.md) | 실제 세계에서 데이터 과학 기반 프로젝트. | [수업](6-Data-Science-In-Wild/20-Real-World-Examples/README.md) | [Nitya](https://twitter.com/nitya) |

## GitHub Codespaces

Codespace에서 이 샘플을 열려면 다음 단계를 따르세요:
1. Code 드롭다운 메뉴를 클릭하고 Codespaces로 열기 옵션을 선택하세요.
2. 창 하단에서 + New codespace를 선택하세요.
자세한 내용은 [GitHub 문서](https://docs.github.com/en/codespaces/developing-in-codespaces/creating-a-codespace-for-a-repository#creating-a-codespace)를 확인하세요.

## VSCode Remote - Containers
로컬 머신과 VSCode를 사용하여 VS Code Remote - Containers 확장을 통해 이 저장소를 컨테이너에서 열려면 다음 단계를 따르세요:

1. 개발 컨테이너를 처음 사용하는 경우, 시스템이 사전 요구 사항을 충족하는지 확인하세요 (예: Docker 설치). [시작 문서](https://code.visualstudio.com/docs/devcontainers/containers#_getting-started)를 참조하세요.

이 저장소를 사용하려면 다음 중 하나를 선택하세요:

- 저장소를 격리된 Docker 볼륨에서 열기:

**참고**: 내부적으로 Remote-Containers: **Clone Repository in Container Volume...** 명령을 사용하여 소스 코드를 로컬 파일 시스템 대신 Docker 볼륨에 복제합니다. [볼륨](https://docs.docker.com/storage/volumes/)은 컨테이너 데이터를 지속적으로 저장하는 데 선호되는 메커니즘입니다.

- 로컬 파일 시스템에 복제하거나 다운로드한 버전을 열기:

- 이 저장소를 로컬 파일 시스템에 복제하세요.
- F1을 누르고 **Remote-Containers: Open Folder in Container...** 명령을 선택하세요.
- 이 폴더의 복제본을 선택하고 컨테이너가 시작될 때까지 기다린 후 테스트를 진행하세요.

## 오프라인 액세스

[Docsify](https://docsify.js.org/#/)를 사용하여 이 문서를 오프라인으로 실행할 수 있습니다. 이 저장소를 포크하고, 로컬 머신에 [Docsify 설치](https://docsify.js.org/#/quickstart)를 한 다음, 이 저장소의 루트 폴더에서 `docsify serve`를 입력하세요. 웹사이트는 localhost의 포트 3000에서 제공됩니다: `localhost:3000`.

> 참고: Docsify를 통해 노트북은 렌더링되지 않으므로 노트북을 실행해야 할 때는 Python 커널을 실행하는 VS Code에서 별도로 실행하세요.

## 도움 요청!

커리큘럼의 전체 또는 일부를 번역하고 싶다면 [번역 가이드](TRANSLATIONS.md)를 따라주세요.

## 기타 커리큘럼

우리 팀은 다른 커리큘럼도 제작합니다! 확인해보세요:

- [Generative AI for Beginners](https://aka.ms/genai-beginners)
- [Generative AI for Beginners .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [Generative AI with JavaScript](https://github.com/microsoft/generative-ai-with-javascript)
- [Generative AI with Java](https://aka.ms/genaijava)
- [AI for Beginners](https://aka.ms/ai-beginners)
- [Data Science for Beginners](https://aka.ms/datascience-beginners)
- [ML for Beginners](https://aka.ms/ml-beginners)
- [Cybersecurity for Beginners](https://github.com/microsoft/Security-101) 
- [Web Dev for Beginners](https://aka.ms/webdev-beginners)
- [IoT for Beginners](https://aka.ms/iot-beginners)
- [XR Development for Beginners](https://github.com/microsoft/xr-development-for-beginners)
- [Mastering GitHub Copilot for Paired Programming](https://github.com/microsoft/Mastering-GitHub-Copilot-for-Paired-Programming)
- [Mastering GitHub Copilot for C#/.NET Developers](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers)
- [Choose Your Own Copilot Adventure](https://github.com/microsoft/CopilotAdventures)

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전을 권위 있는 출처로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 책임을 지지 않습니다.