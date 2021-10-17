# Data Science in the Real World

| ![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../../sketchnotes/20-DataScience-RealWorld.png) |
|:----------------------------------------------------------------------------------------------------------------:|
| Data Science In The Real World - _Sketchnote by [@nitya](https://twitter.com/nitya)_                             |

We're almost at the end of this learning journey! 우리는 

우리는 데이터 사이언스와 윤리의 정의로 시작해서, 데이터 분석과 시각화를 위한 여러가지 툴 & 테크닉을 살펴보았고, 데이터 사이언스의 라이프 사이클을 검토하였고, 클라우드 컴퓨팅 서비스를 통한 데이터 사이언스 워크플로우 확장 및 자동화에 대해 알아보았습니다. 그래서 이제 당신은 아마도 _"내가 배운 것들을 현실에서는 어떻게 엮어서 사용하지?"_ 라는 의문점이 생길 것입니다.

이 레슨에서, 우리는 산업 전반에 걸친 데이터 과학의 실제 적용 사례를 살펴보고 연구, 디지털 인문학, 지속 가능성, 맥락에 대한 구체적인 예를 살펴보겠습니다. 학생 프로젝트 기회를 살펴보고 유용한 리소스로 마무리하여 학습 여정을 계속 이어나갈 수 있도록 도와드리겠습니다! 

## Pre-Lecture Quiz

[Pre-lecture quiz](https://red-water-0103e7a0f.azurestaticapps.net/quiz/38)

## Data Science + Industry

AI의 민주화 덕분에, 개발자들은 이제 사용자 경험과 개발 워크플로우에 대한 AI 중심의 의사 결정 및 데이터 기반 통찰력을 설계하고 통합하는 것이 더 쉬워지고 있습니다. 이것은 현실의 산업에서 데이터 사이언스가 어떻게 "적용" 되는지에 대한 몇 가지의 예입니다:

* [구글 독감 트렌드 (Google Flu Trends)](https://www.wired.com/2015/10/can-learn-epic-failure-google-flu-trends/) 데이터 사이언스를 사용하여 검색어와 독감 트렌드를 연관시켰습니다. used data science to correlate search terms with flu trends. 이 접근 방식에는 결함이 있지만 데이터 기반 의료 예측의 가능성(및 과제)에 대한 인식을 높였습니다.
  
  [UPS 라우팅 예측 (UPS Routing Predictions)](https://www.technologyreview.com/2018/11/21/139000/how-ups-uses-ai-to-outsmart-bad-weather/) - UPS가 데이터 사이언스와 머신러닝을 이용하여 배송을 위한 최적의 루트를 날씨 조건, 교통 패턴, 배달 마감일 등을 고려하여 어떻게 예측하는지에 대해 설명합니다. 

* [NYC 택시 루트 시각화 (NYC Taxicab Route Visualization)](http://chriswhong.github.io/nyctaxi/) - [정보 자유법 (Freedom Of Information Laws)](https://chriswhong.com/open-data/foil_nyc_taxi/) 을 사용하여 수집된 데이터는 뉴욕 택시 생활의 하루를 시각화하는 데 도움이 되었고, 뉴욕 택시들이 바쁜 도시를 어떻게 돌아다니는지, 그들이 버는 돈, 그리고 매 24시간 동안의 여행 기간을 이해하는 데 도움이 되었습니다. 

* [우버 데이터 사이언스 워크벤치 (Uber Data Science Workbench)](https://eng.uber.com/dsw/) - 요금, 안전, 사기 탐지 및 탐색 결정에 도움이 되는 데이터 분석 도구를 구축하기 위해 *매일* 수백만 개의 uber 여행에서 수집된 데이터(픽업 & 하차 위치, 이동 시간, 선호 경로 등)를 사용합니다. 

* [스포츠 분석 (Sports Analytics)](https://towardsdatascience.com/scope-of-analytics-in-sports-world-37ed09c39860) - 인재 스카우트, 스포츠 도박, 재고/장소 관리를 적용한 *예측 분석* (팀 및 선수 분석 - Moneyball 을 생각해보세요 - 그리고 팬 관리) 및 *데이터 시각화*  (팀 & 팬 대시보드, 게임 등) 에 중점을 둡니다. 

* [금융 산업에서의 데이터 사이언스 (Data Science in Banking)](https://data-flair.training/blogs/data-science-in-banking/) - 리스크 모델링 및 부정 행위 방지, 고객 세분화, 실시간 예측 및 추천 시스템에 이르기까지 다양한 적용을 통해 금융 산업에서 데이터 과학의 가치를 강조합니다. 예측 분석은 또한 [신용 점수 (credit scores)](https://dzone.com/articles/using-big-data-and-predictive-analytics-for-credit) 와 같은 중요한 척도를 도출합니다.

* [헬스케어에서의 데이터 사이언스 (Data Science in Healthcare)](https://data-flair.training/blogs/data-science-in-healthcare/) - 의료 영상(예: MRI, X-Ray, CT-Scan), 유전체학(DNA 시퀀싱), 약물 개발(위험 평가, 성공 예측), 예측 분석(환자 치료 & 공급 물류), 질병 추적 & 예방 등의 적용을 강조합니다.
  
  

![Data Science Applications in The Real World](../images/data-science-applications.png) 이미지 출처: [Data Flair: 6 Amazing Data Science Applications ](https://data-flair.training/blogs/data-science-applications/)

위 그림은 데이터 사이언스 기술을 적용하기 위한 다른 도메인과 예를 보여줍니다. 더 많은 적용 사례를 보고싶나요? 아래의 [Review & Self Study](?id=review-amp-self-study)를 살펴보세요.

## Data Science + Research

| ![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../../sketchnotes/20-DataScience-Research.png) |
|:---------------------------------------------------------------------------------------------------------------:|
| Data Science & Research - _Sketchnote by [@nitya](https://twitter.com/nitya)_                                   |

현실 속에서 종종 규모에 맞는 산업 활용 사례에 초점을 맞추지만, _연구_ 에 적용된 것과 프로젝트는 다음 두 가지 관점에서 유용할 수 있습니다:

* _혁신 기회_ - 차세대 애플리케이션을 위한 선진 개념의 신속한 프로토타이핑 및 사용자 경험의 테스트를 살펴봅니다. 
* _배포 과제_ - 현실 세계에서 데이터 사이언스 기술의 잠재적인 피해 또는 의도하지 않은 결과를 조사합니다.

학생들에게 이러한 연구 프로젝트는 주제에 대한 이해를 향상시킬 수 있는 학습 기회와 협업 기회를 제공할 수 있으며, 관심 분야에서 일하는 관련 직원 또는 팀과의 인식과 참여를 넓힐 수 있습니다. 그렇다면 연구 프로젝트는 어떻게 생겼고 어떻게 영향을 미칠 수 있을까요?

이 예제를 한 번 봅시다 - Joy Buolamwini (MIT Media Labs)의 [MIT 젠더 쉐이즈 연구 (MIT Gender Shades Study)](http://gendershades.org/overview.html)의 [연구 (signature research paper)](http://proceedings.mlr.press/v81/buolamwini18a/buolamwini18a.pdf) co-authored with Timnit Gebru (then at Microsoft Research) that focused on 

* **무엇:** The objective of the research project was to _evaluate bias present in automated facial analysis algorithms and datasets_ based on gender and skin type. 
* **Why:** Facial analysis is used in areas like law enforcement, airport security, hiring systems and more - contexts where inaccurate classifications (e.g., due to bias) can cause potential economic and social harms to affected individuals or groups. Understanding (and eliminating or mitigating) biases is key to fairness in usage.
* **How:** Researchers recongized that existing benchmarks used predominantly lighter-skinned subjects, and curated a new data set (1000+ images) that was _more balanced_ by gender and skin type. The data set was used to evaluate the accuracy of three gender classification products (from Microsoft, IBM & Face++). 

Results showed that though overall classification accuracy was good, there was a noticeable difference in error rates between various subgroups - with **misgendering** being higher for females or persons with darker skin types, indicative of bias.

**Key Outcomes:** Raised awareness that data science needs more _representative datasets_ (balanced subgroups) and more _inclusive teams_ (diverse backgrounds) to recognize and eliminate or mitigate such biases earlier in AI solutions. Research efforts like this are also instrumental in many organizations defining principles and practices for _responsible AI_ to improve fairness across their AI products and processes.

**Want to learn about relevant research efforts in Microsoft?** 

* Check out [Microsoft Research Projects](https://www.microsoft.com/research/research-area/artificial-intelligence/?facet%5Btax%5D%5Bmsr-research-area%5D%5B%5D=13556&facet%5Btax%5D%5Bmsr-content-type%5D%5B%5D=msr-project) on Artificial Intelligence.
* Explore student projects from [Microsoft Research Data Science Summer School](https://www.microsoft.com/en-us/research/academic-program/data-science-summer-school/).
* Check out the [Fairlearn](https://fairlearn.org/) project and [Responsible AI](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1%3aprimaryr6) initiatives.

## Data Science + Humanities

| ![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-Humanities.png) |
|:-----------------------------------------------------------------------------------------------------------------:|
| Data Science & Digital Humanities - _Sketchnote by [@nitya](https://twitter.com/nitya)_                           |

Digital Humanities [has been defined](https://digitalhumanities.stanford.edu/about-dh-stanford) as "a collection of practices and approaches combining computational methods with humanistic inquiry". [Stanford projects](https://digitalhumanities.stanford.edu/projects) like _"rebooting history"_ and _"poetic thinking"_ illustrate the linkage between [Digital Humanities and Data Science](https://digitalhumanities.stanford.edu/digital-humanities-and-data-science) - emphasizing techniques like network analysis, information visualization, spatial and text analysis that can help us revisit historical and literary data sets to derive new insights and perspective.

*Want to explore and extend a project in this space?*

Check out ["Emily Dickinson and the Meter of Mood"](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671) - a great example from [Jen Looper](https://twitter.com/jenlooper) that asks how we can use data science to revisit familiar poetry and re-evaluate its meaning and the contributions of its author in new contexts. For instance, _can we predict the season in which a poem was authored by analyzing its tone or sentiment_ - and what does this tell us about the author's state of mind over the relevant period?

To answer that question, we follow the steps of our data science lifecycle:

* [`Data Acquisition`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#acquiring-the-dataset) - to collect a relevant dataset for analysis. Options including using an API ( e.g., [Poetry DB API](https://poetrydb.org/index.html)) or scraping web pages  (e.g., [Project Gutenberg](https://www.gutenberg.org/files/12242/12242-h/12242-h.htm)) using tools like [Scrapy](https://scrapy.org/).
* [`Data Cleaning`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#clean-the-data) - explains how text can be formatted, sanitized and simplified using basic tools like Visual Studio Code and Microsoft Excel.
* [`Data Analysis`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#working-with-the-data-in-a-notebook) - explains how we can now import the dataset into "Notebooks" for analysis using Python packages (like pandas, numpy and matplotlib) to organize and visualize the data.
* [`Sentiment Analysis`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#sentiment-analysis-using-cognitive-services) - explains how we can integrate cloud services like Text Analytics, using low-code tools like [Power Automate](https://flow.microsoft.com/en-us/) for automated data processing workflows.

Using this workflow, we can explore the seasonal impacts on the sentiment of the poems, and help us fashion our own perspectives on the author. Try it out yourself - then extend the notebook to ask other questions or visualize the data in new ways!

> You can use some of the tools in the [Digital Humanities toolkit](https://github.com/Digital-Humanities-Toolkit) to pursue these avenues of inquiry

## Data Science + Sustainability

| ![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-Sustainability.png) |
|:---------------------------------------------------------------------------------------------------------------------:|
| Data Science & Sustainability - _Sketchnote by [@nitya](https://twitter.com/nitya)_                                   |

The [2030 Agenda For Sustainable Development](https://sdgs.un.org/2030agenda) - adopted by all United Nations members in 2015 - identifies 17 goals including ones that focus on **Protecting the Planet** from degradation and the impact of climate change. The [Microsoft Sustainability](https://www.microsoft.com/en-us/sustainability) initiative supports these goals by exploring ways in which technology solutions can support and build more sustainable futures with a [focus on 4 goals](https://dev.to/azure/a-visual-guide-to-sustainable-software-engineering-53hh) - being carbon negative, water positive, zero waste, and bio-diverse by 2030.

Tackling these challenges in a scalable and timely manner requires cloud-scale thinking - and large scale data. The [Planetary Computer](https://planetarycomputer.microsoft.com/) initiative provides 4 components to help data scientists and developers in this effort:

* [Data Catalog](https://planetarycomputer.microsoft.com/catalog) - with petabytes of Earth Systems data (free & Azure-hosted).
* [Planetary API](https://planetarycomputer.microsoft.com/docs/reference/stac/) - to help users search for relevant data across space and time.
* [Hub](https://planetarycomputer.microsoft.com/docs/overview/environment/) - managed environment for scientists to process massive geospatial datasets.
* [Applications](https://planetarycomputer.microsoft.com/applications) - showcase use cases & tools for sustainability insights.

**The Planetary Computer Project is currently in preview (as of Sep 2021)** - here's how you can get started contributing to sustainability solutions using data science.

* [Request access](https://planetarycomputer.microsoft.com/account/request) to start exploration and connect with peers.
* [Explore documentation](https://planetarycomputer.microsoft.com/docs/overview/about) to understand supported datasets and APIs.
* Explore applications like [Ecosystem Monitoring](https://analytics-lab.org/ecosystemmonitoring/) for inspiration on application ideas.

Think about how you can use data visualization to expose or amplify relevant insights into areas like climate change and deforestation. Or think about how insights can be used to create new user experiences that motivate behavioral changes for more sustainable living. 

## Data Science + Students

We've talked about real-world applications in industry and research, and explored data science application examples in digital humanities and sustainability. So how can you build your skills and share your expertise as data science beginners?

Here are some examples of data science student projects to inspire you.

* [MSR Data Science Summer School](https://www.microsoft.com/en-us/research/academic-program/data-science-summer-school/#!projects) with GitHub [projects](https://github.com/msr-ds3) exploring topics like:
  - [Racial Bias in Police Use of Force](https://www.microsoft.com/en-us/research/video/data-science-summer-school-2019-replicating-an-empirical-analysis-of-racial-differences-in-police-use-of-force/) | [Github](https://github.com/msr-ds3/stop-question-frisk)
  - [Reliability of NYC Subway System](https://www.microsoft.com/en-us/research/video/data-science-summer-school-2018-exploring-the-reliability-of-the-nyc-subway-system/) | [Github](https://github.com/msr-ds3/nyctransit)
* [Digitizing Material Culture: Exploring socio-economic distributions in Sirkap](https://claremont.maps.arcgis.com/apps/Cascade/index.html?appid=bdf2aef0f45a4674ba41cd373fa23afc)- from [Ornella Altunyan](https://twitter.com/ornelladotcom) and team at Claremont, using using [ArcGIS StoryMaps](https://storymaps.arcgis.com/).

## 🚀 Challenge

Search for articles that recommend data science projects that are beginner friendly - like [these 50 topic areas](https://www.upgrad.com/blog/data-science-project-ideas-topics-beginners/) or [these 21 project ideas](https://www.intellspot.com/data-science-project-ideas) or [these 16 projects with source code](https://data-flair.training/blogs/data-science-project-ideas/) that you can deconstruct and remix. And don't forget to blog about your learning journeys and share your insights with all of us.

## Post-Lecture Quiz

[Post-lecture quiz](https://red-water-0103e7a0f.azurestaticapps.net/quiz/39)

## Review & Self Study

Want to explore more use cases? Here are a few relevant articles:

* [17 Data Science Applications and Examples](https://builtin.com/data-science/data-science-applications-examples) - Jul 2021
* [11 Breathtaking Data Science Applications in Real World](https://myblindbird.com/data-science-applications-real-world/) - May 2021
* [Data Science In The Real World](https://towardsdatascience.com/data-science-in-the-real-world/home) - Article Collection
* Data Science In: [Education](https://data-flair.training/blogs/data-science-in-education/), [Agriculture](https://data-flair.training/blogs/data-science-in-agriculture/), [Finance](https://data-flair.training/blogs/data-science-in-finance/), [Movies](https://data-flair.training/blogs/data-science-at-movies/) & more.
  
  ## Assignment

[Explore A Planetary Computer Dataset](assignment.md)
