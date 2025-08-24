<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "408c55cab2880daa4e78616308bd5db7",
  "translation_date": "2025-08-24T13:05:24+00:00",
  "source_file": "5-Data-Science-In-Cloud/17-Introduction/README.md",
  "language_code": "zh"
}
-->
# 云端数据科学简介

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/17-DataScience-Cloud.png)|
|:---:|
| 云端数据科学：简介 - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

在本课程中，您将学习云的基本原理，了解为什么使用云服务来运行您的数据科学项目可能会很有趣，并且我们将查看一些在云端运行的数据科学项目示例。

## [课前测验](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/32)

## 什么是云？

云，或云计算，是通过互联网提供的按需付费的各种计算服务，这些服务托管在基础设施上。服务包括存储、数据库、网络、软件、分析和智能服务等解决方案。

我们通常将公共云、私有云和混合云区分如下：

* 公共云：公共云由第三方云服务提供商拥有和运营，通过互联网向公众提供其计算资源。
* 私有云：指专门供单一企业或组织使用的云计算资源，服务和基础设施维护在私有网络上。
* 混合云：混合云是结合公共云和私有云的系统。用户选择本地数据中心，同时允许数据和应用程序在一个或多个公共云上运行。

大多数云计算服务分为三类：基础设施即服务（IaaS）、平台即服务（PaaS）和软件即服务（SaaS）。

* 基础设施即服务（IaaS）：用户租用IT基础设施，例如服务器和虚拟机（VM）、存储、网络、操作系统。
* 平台即服务（PaaS）：用户租用一个开发、测试、交付和管理软件应用程序的环境。用户无需担心设置或管理开发所需的服务器、存储、网络和数据库的底层基础设施。
* 软件即服务（SaaS）：用户通过互联网按需访问软件应用程序，通常是基于订阅的。用户无需担心托管和管理软件应用程序、底层基础设施或维护，例如软件升级和安全补丁。

一些最大的云服务提供商包括亚马逊AWS、谷歌云平台和微软Azure。

## 为什么选择云进行数据科学？

开发人员和IT专业人员选择使用云的原因有很多，包括以下几点：

* 创新：您可以通过将云服务提供商创建的创新服务直接集成到您的应用程序中来增强应用程序功能。
* 灵活性：您只需支付所需的服务费用，并可以从广泛的服务中进行选择。通常按需付费，并根据不断变化的需求调整服务。
* 预算：您无需进行初始投资来购买硬件和软件、设置和运行本地数据中心，只需支付您实际使用的费用。
* 可扩展性：您的资源可以根据项目需求进行扩展，这意味着您的应用程序可以根据外部因素随时调整计算能力、存储和带宽。
* 生产力：您可以专注于业务，而不是花时间处理可以由其他人管理的任务，例如管理数据中心。
* 可靠性：云计算提供多种方式来持续备份您的数据，并可以设置灾难恢复计划，即使在危机时期也能保持业务和服务的运行。
* 安全性：您可以利用政策、技术和控制措施来增强项目的安全性。

以上是人们选择使用云服务的一些常见原因。现在我们对云是什么以及它的主要优势有了更好的理解，让我们更具体地看看数据科学家和处理数据的开发人员的工作，以及云如何帮助他们解决可能面临的各种挑战：

* 存储大量数据：与其购买、管理和保护大型服务器，您可以直接将数据存储在云中，例如使用Azure Cosmos DB、Azure SQL Database和Azure Data Lake Storage。
* 执行数据集成：数据集成是数据科学的重要组成部分，它使您能够从数据收集过渡到采取行动。通过云提供的数据集成服务，您可以从各种来源收集、转换和集成数据到单一数据仓库，例如使用Data Factory。
* 处理数据：处理大量数据需要强大的计算能力，并不是每个人都能获得足够强大的机器，这就是为什么许多人选择直接利用云的巨大计算能力来运行和部署解决方案。
* 使用数据分析服务：云服务如Azure Synapse Analytics、Azure Stream Analytics和Azure Databricks可以帮助您将数据转化为可操作的洞察。
* 使用机器学习和数据智能服务：与从头开始相比，您可以使用云提供商提供的机器学习算法，例如AzureML服务。您还可以使用认知服务，例如语音转文字、文字转语音、计算机视觉等。

## 云端数据科学示例

让我们通过几个场景来使这一点更具体。

### 实时社交媒体情感分析

我们从一个常见的机器学习入门场景开始：实时社交媒体情感分析。

假设您运营一个新闻媒体网站，希望利用实时数据来了解读者可能感兴趣的内容。为了了解更多，您可以构建一个程序，对Twitter上的相关主题进行实时情感分析。

您关注的关键指标是特定主题（标签）的推文数量和情感，这些情感通过分析工具对指定主题进行情感分析来确定。

创建此项目所需的步骤如下：

* 创建一个事件中心以收集Twitter数据流输入
* 配置并启动一个Twitter客户端应用程序，调用Twitter流API
* 创建一个流分析作业
* 指定作业输入和查询
* 创建输出接收器并指定作业输出
* 启动作业

查看完整流程，请参阅[文档](https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?WT.mc_id=academic-77958-bethanycheum&ocid=AID30411099)。

### 科学论文分析

让我们看另一个由本课程作者之一[Dmitry Soshnikov](http://soshnikov.com)创建的项目示例。

Dmitry创建了一个分析COVID论文的工具。通过审查此项目，您将了解如何创建一个工具，从科学论文中提取知识，获得洞察，并帮助研究人员高效地浏览大量论文。

以下是使用的不同步骤：

* 使用[Text Analytics for Health](https://docs.microsoft.com/azure/cognitive-services/text-analytics/how-tos/text-analytics-for-health?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109)提取和预处理信息
* 使用[Azure ML](https://azure.microsoft.com/services/machine-learning?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109)并行化处理
* 使用[Cosmos DB](https://azure.microsoft.com/services/cosmos-db?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109)存储和查询信息
* 使用Power BI创建交互式仪表板进行数据探索和可视化

查看完整流程，请访问[Dmitry的博客](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/)。

如您所见，我们可以通过多种方式利用云服务来进行数据科学。

## 脚注

来源：
* https://azure.microsoft.com/overview/what-is-cloud-computing?ocid=AID3041109  
* https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?ocid=AID3041109  
* https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/  

## 课后测验

[课后测验](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/33)

## 作业

[市场研究](assignment.md)

**免责声明**：  
本文档使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。虽然我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于重要信息，建议使用专业人工翻译。我们不对因使用此翻译而产生的任何误解或误读承担责任。