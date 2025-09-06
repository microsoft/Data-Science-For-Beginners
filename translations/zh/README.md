<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5443b88ba402d2ec7b000e4de6cecb8",
  "translation_date": "2025-08-30T08:47:13+00:00",
  "source_file": "README.md",
  "language_code": "zh"
}
-->
# 数据科学入门 - 课程大纲

Azure Cloud Advocates团队很高兴为大家提供一个为期10周、共20节课的课程，全面介绍数据科学。每节课都包含课前和课后测验、完成课程的书面指导、解决方案以及作业。我们的项目式教学法让您在实践中学习，这是一种让新技能牢固掌握的有效方法。

**衷心感谢我们的作者们：** [Jasmine Greenaway](https://www.twitter.com/paladique)、[Dmitry Soshnikov](http://soshnikov.com)、[Nitya Narasimhan](https://twitter.com/nitya)、[Jalen McGee](https://twitter.com/JalenMcG)、[Jen Looper](https://twitter.com/jenlooper)、[Maud Levy](https://twitter.com/maudstweets)、[Tiffany Souterre](https://twitter.com/TiffanySouterre)、[Christopher Harrison](https://www.twitter.com/geektrainer)。

**🙏 特别感谢 🙏 我们的 [Microsoft Student Ambassador](https://studentambassadors.microsoft.com/) 作者、审阅者和内容贡献者们，** 特别是 Aaryan Arora、[Aditya Garg](https://github.com/AdityaGarg00)、[Alondra Sanchez](https://www.linkedin.com/in/alondra-sanchez-molina/)、[Ankita Singh](https://www.linkedin.com/in/ankitasingh007)、[Anupam Mishra](https://www.linkedin.com/in/anupam--mishra/)、[Arpita Das](https://www.linkedin.com/in/arpitadas01/)、ChhailBihari Dubey、[Dibri Nsofor](https://www.linkedin.com/in/dibrinsofor)、[Dishita Bhasin](https://www.linkedin.com/in/dishita-bhasin-7065281bb)、[Majd Safi](https://www.linkedin.com/in/majd-s/)、[Max Blum](https://www.linkedin.com/in/max-blum-6036a1186/)、[Miguel Correa](https://www.linkedin.com/in/miguelmque/)、[Mohamma Iftekher (Iftu) Ebne Jalal](https://twitter.com/iftu119)、[Nawrin Tabassum](https://www.linkedin.com/in/nawrin-tabassum)、[Raymond Wangsa Putra](https://www.linkedin.com/in/raymond-wp/)、[Rohit Yadav](https://www.linkedin.com/in/rty2423)、Samridhi Sharma、[Sanya Sinha](https://www.linkedin.com/mwlite/in/sanya-sinha-13aab1200)、[Sheena Narula](https://www.linkedin.com/in/sheena-narua-n/)、[Tauqeer Ahmad](https://www.linkedin.com/in/tauqeerahmad5201/)、Yogendrasingh Pawar、[Vidushi Gupta](https://www.linkedin.com/in/vidushi-gupta07/)、[Jasleen Sondhi](https://www.linkedin.com/in/jasleen-sondhi/)。

|![由 @sketchthedocs 绘制的速写笔记 https://sketchthedocs.dev](../../translated_images/00-Title.8af36cd35da1ac555b678627fbdc6e320c75f0100876ea41d30ea205d3b08d22.zh.png)|
|:---:|
| 数据科学入门 - _速写笔记由 [@nitya](https://twitter.com/nitya)_ 绘制 |

### 🌐 多语言支持

#### 通过 GitHub Action 支持（自动更新且始终保持最新）

[法语](../fr/README.md) | [西班牙语](../es/README.md) | [德语](../de/README.md) | [俄语](../ru/README.md) | [阿拉伯语](../ar/README.md) | [波斯语](../fa/README.md) | [乌尔都语](../ur/README.md) | [中文（简体）](./README.md) | [中文（繁体，澳门）](../mo/README.md) | [中文（繁体，香港）](../hk/README.md) | [中文（繁体，台湾）](../tw/README.md) | [日语](../ja/README.md) | [韩语](../ko/README.md) | [印地语](../hi/README.md) | [孟加拉语](../bn/README.md) | [马拉地语](../mr/README.md) | [尼泊尔语](../ne/README.md) | [旁遮普语（古木基文）](../pa/README.md) | [葡萄牙语（葡萄牙）](../pt/README.md) | [葡萄牙语（巴西）](../br/README.md) | [意大利语](../it/README.md) | [波兰语](../pl/README.md) | [土耳其语](../tr/README.md) | [希腊语](../el/README.md) | [泰语](../th/README.md) | [瑞典语](../sv/README.md) | [丹麦语](../da/README.md) | [挪威语](../no/README.md) | [芬兰语](../fi/README.md) | [荷兰语](../nl/README.md) | [希伯来语](../he/README.md) | [越南语](../vi/README.md) | [印尼语](../id/README.md) | [马来语](../ms/README.md) | [他加禄语（菲律宾语）](../tl/README.md) | [斯瓦希里语](../sw/README.md) | [匈牙利语](../hu/README.md) | [捷克语](../cs/README.md) | [斯洛伐克语](../sk/README.md) | [罗马尼亚语](../ro/README.md) | [保加利亚语](../bg/README.md) | [塞尔维亚语（西里尔文）](../sr/README.md) | [克罗地亚语](../hr/README.md) | [斯洛文尼亚语](../sl/README.md) | [乌克兰语](../uk/README.md) | [缅甸语](../my/README.md)

**如果您希望支持其他翻译语言，请查看 [这里](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**

#### 加入我们的社区
[![Azure AI Discord](https://dcbadge.limes.pink/api/server/kzRShWzttr)](https://discord.gg/kzRShWzttr)

# 您是学生吗？

通过以下资源开始学习：

- [学生中心页面](https://docs.microsoft.com/en-gb/learn/student-hub?WT.mc_id=academic-77958-bethanycheum) 在此页面，您可以找到入门资源、学生礼包，甚至获取免费认证券的方法。此页面值得收藏，并定期查看，因为我们至少每月更新内容。
- [Microsoft Learn 学生大使](https://studentambassadors.microsoft.com?WT.mc_id=academic-77958-bethanycheum) 加入全球学生大使社区，这可能是您进入微软的途径。

# 入门指南

> **教师们**：我们[提供了一些建议](for-teachers.md)来帮助您使用此课程。我们期待您在[讨论论坛](https://github.com/microsoft/Data-Science-For-Beginners/discussions)中提供反馈！

> **[学生们](https://aka.ms/student-page)**：如果您想独立使用此课程，请将整个仓库分叉并自行完成练习，从课前测验开始。然后阅读课程内容并完成其他活动。尝试通过理解课程内容来创建项目，而不是直接复制解决方案代码；不过，这些代码可以在每个项目课程的 /solutions 文件夹中找到。另一个建议是与朋友组成学习小组，共同学习内容。对于进一步学习，我们推荐 [Microsoft Learn](https://docs.microsoft.com/en-us/users/jenlooper-2911/collections/qprpajyoy3x0g7?WT.mc_id=academic-77958-bethanycheum)。

## 团队介绍

[![宣传视频](../../ds-for-beginners.gif)](https://youtu.be/8mzavjQSMM4 "宣传视频")

**Gif 制作人** [Mohit Jaisal](https://www.linkedin.com/in/mohitjaisal)

> 🎥 点击上方图片观看关于项目及其创建者的视频！

## 教学法

我们在设计此课程时选择了两个教学原则：确保课程是基于项目的，并且包含频繁的测验。在本系列课程结束时，学生将学习数据科学的基本原理，包括伦理概念、数据准备、不同的数据处理方式、数据可视化、数据分析、数据科学的实际应用案例等。

此外，课前的低压力测验可以让学生专注于学习主题，而课后的第二次测验则有助于进一步巩固知识。此课程设计灵活有趣，可以完整学习，也可以部分学习。项目从简单开始，到10周课程结束时逐渐变得复杂。
> 查阅我们的[行为准则](CODE_OF_CONDUCT.md)、[贡献指南](CONTRIBUTING.md)、[翻译指南](TRANSLATIONS.md)。我们欢迎您的建设性反馈！
## 每节课程包括：

- 可选的手绘笔记
- 可选的补充视频
- 课前热身测验
- 书面课程
- 对于基于项目的课程，提供逐步指导如何构建项目
- 知识检查
- 挑战任务
- 补充阅读材料
- 作业
- [课后测验](https://ff-quizzes.netlify.app/en/)

> **关于测验的说明**：所有测验都包含在 Quiz-App 文件夹中，共有 40 个测验，每个测验包含三个问题。测验链接嵌入在课程中，但测验应用可以在本地运行或部署到 Azure；请按照 `quiz-app` 文件夹中的说明操作。这些测验正在逐步进行本地化。

## 课程列表

|![由 @sketchthedocs 绘制的手绘笔记 https://sketchthedocs.dev](../../translated_images/00-Roadmap.4905d6567dff47532b9bfb8e0b8980fc6b0b1292eebb24181c1a9753b33bc0f5.zh.png)|
|:---:|
| 数据科学入门：路线图 - _手绘笔记由 [@nitya](https://twitter.com/nitya)_ |

| 课程编号 | 主题 | 课程分组 | 学习目标 | 课程链接 | 作者 |
| :-----------: | :----------------------------------------: | :--------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------: | :----: |
| 01 | 数据科学定义 | [简介](1-Introduction/README.md) | 学习数据科学的基本概念，以及它与人工智能、机器学习和大数据的关系。 | [课程](1-Introduction/01-defining-data-science/README.md) [视频](https://youtu.be/beZ7Mb_oz9I) | [Dmitry](http://soshnikov.com) |
| 02 | 数据科学伦理 | [简介](1-Introduction/README.md) | 数据伦理的概念、挑战与框架。 | [课程](1-Introduction/02-ethics/README.md) | [Nitya](https://twitter.com/nitya) |
| 03 | 数据定义 | [简介](1-Introduction/README.md) | 数据的分类及其常见来源。 | [课程](1-Introduction/03-defining-data/README.md) | [Jasmine](https://www.twitter.com/paladique) |
| 04 | 统计与概率简介 | [简介](1-Introduction/README.md) | 使用概率和统计的数学技术来理解数据。 | [课程](1-Introduction/04-stats-and-probability/README.md) [视频](https://youtu.be/Z5Zy85g4Yjw) | [Dmitry](http://soshnikov.com) |
| 05 | 使用关系型数据 | [数据操作](2-Working-With-Data/README.md) | 关系型数据简介，以及使用结构化查询语言（SQL，发音为“see-quell”）探索和分析关系型数据的基础知识。 | [课程](2-Working-With-Data/05-relational-databases/README.md) | [Christopher](https://www.twitter.com/geektrainer) | | |
| 06 | 使用 NoSQL 数据 | [数据操作](2-Working-With-Data/README.md) | 非关系型数据简介、其各种类型以及探索和分析文档数据库的基础知识。 | [课程](2-Working-With-Data/06-non-relational/README.md) | [Jasmine](https://twitter.com/paladique)|
| 07 | 使用 Python | [数据操作](2-Working-With-Data/README.md) | 使用 Python 进行数据探索的基础知识，包括 Pandas 等库。建议具备 Python 编程的基础知识。 | [课程](2-Working-With-Data/07-python/README.md) [视频](https://youtu.be/dZjWOGbsN4Y) | [Dmitry](http://soshnikov.com) |
| 08 | 数据准备 | [数据操作](2-Working-With-Data/README.md) | 数据清理和转换技术，处理缺失、不准确或不完整数据的相关主题。 | [课程](2-Working-With-Data/08-data-preparation/README.md) | [Jasmine](https://www.twitter.com/paladique) |
| 09 | 可视化数量 | [数据可视化](3-Data-Visualization/README.md) | 学习如何使用 Matplotlib 可视化鸟类数据 🦆 | [课程](3-Data-Visualization/09-visualization-quantities/README.md) | [Jen](https://twitter.com/jenlooper) |
| 10 | 可视化数据分布 | [数据可视化](3-Data-Visualization/README.md) | 可视化区间内的观察结果和趋势。 | [课程](3-Data-Visualization/10-visualization-distributions/README.md) | [Jen](https://twitter.com/jenlooper) |
| 11 | 可视化比例 | [数据可视化](3-Data-Visualization/README.md) | 可视化离散和分组百分比。 | [课程](3-Data-Visualization/11-visualization-proportions/README.md) | [Jen](https://twitter.com/jenlooper) |
| 12 | 可视化关系 | [数据可视化](3-Data-Visualization/README.md) | 可视化数据集及其变量之间的连接和相关性。 | [课程](3-Data-Visualization/12-visualization-relationships/README.md) | [Jen](https://twitter.com/jenlooper) |
| 13 | 有意义的可视化 | [数据可视化](3-Data-Visualization/README.md) | 提供有效问题解决和洞察的可视化技术和指导。 | [课程](3-Data-Visualization/13-meaningful-visualizations/README.md) | [Jen](https://twitter.com/jenlooper) |
| 14 | 数据科学生命周期简介 | [生命周期](4-Data-Science-Lifecycle/README.md) | 数据科学生命周期简介及其第一步：数据获取和提取。 | [课程](4-Data-Science-Lifecycle/14-Introduction/README.md) | [Jasmine](https://twitter.com/paladique) |
| 15 | 数据分析 | [生命周期](4-Data-Science-Lifecycle/README.md) | 数据科学生命周期的这一阶段专注于数据分析技术。 | [课程](4-Data-Science-Lifecycle/15-analyzing/README.md) | [Jasmine](https://twitter.com/paladique) | | |
| 16 | 数据沟通 | [生命周期](4-Data-Science-Lifecycle/README.md) | 数据科学生命周期的这一阶段专注于以易于决策者理解的方式呈现数据洞察。 | [课程](4-Data-Science-Lifecycle/16-communication/README.md) | [Jalen](https://twitter.com/JalenMcG) | | |
| 17 | 云端数据科学 | [云端数据](5-Data-Science-In-Cloud/README.md) | 这一系列课程介绍了云端数据科学及其优势。 | [课程](5-Data-Science-In-Cloud/17-Introduction/README.md) | [Tiffany](https://twitter.com/TiffanySouterre) 和 [Maud](https://twitter.com/maudstweets) |
| 18 | 云端数据科学 | [云端数据](5-Data-Science-In-Cloud/README.md) | 使用低代码工具训练模型。 |[课程](5-Data-Science-In-Cloud/18-Low-Code/README.md) | [Tiffany](https://twitter.com/TiffanySouterre) 和 [Maud](https://twitter.com/maudstweets) |
| 19 | 云端数据科学 | [云端数据](5-Data-Science-In-Cloud/README.md) | 使用 Azure Machine Learning Studio 部署模型。 | [课程](5-Data-Science-In-Cloud/19-Azure/README.md)| [Tiffany](https://twitter.com/TiffanySouterre) 和 [Maud](https://twitter.com/maudstweets) |
| 20 | 野外数据科学 | [野外数据](6-Data-Science-In-Wild/README.md) | 数据科学驱动的真实世界项目。 | [课程](6-Data-Science-In-Wild/20-Real-World-Examples/README.md) | [Nitya](https://twitter.com/nitya) |

## GitHub Codespaces

按照以下步骤在 Codespace 中打开此示例：
1. 点击代码下拉菜单，选择“Open with Codespaces”选项。
2. 在面板底部选择 + New codespace。
有关更多信息，请查看 [GitHub 文档](https://docs.github.com/en/codespaces/developing-in-codespaces/creating-a-codespace-for-a-repository#creating-a-codespace)。

## VSCode Remote - Containers

按照以下步骤使用本地机器和 VSCode 的 VS Code Remote - Containers 扩展在容器中打开此仓库：

1. 如果这是您第一次使用开发容器，请确保您的系统满足前置条件（例如安装了 Docker），请参考 [入门文档](https://code.visualstudio.com/docs/devcontainers/containers#_getting-started)。

要使用此仓库，您可以选择在隔离的 Docker 卷中打开仓库：

**注意**：底层将使用 Remote-Containers: **Clone Repository in Container Volume...** 命令将源代码克隆到 Docker 卷中，而不是本地文件系统。[卷](https://docs.docker.com/storage/volumes/) 是持久化容器数据的首选机制。

或者打开本地克隆或下载的仓库版本：

- 将此仓库克隆到您的本地文件系统。
- 按 F1 并选择 **Remote-Containers: Open Folder in Container...** 命令。
- 选择克隆的文件夹，等待容器启动，然后尝试操作。

## 离线访问

您可以使用 [Docsify](https://docsify.js.org/#/) 离线运行此文档。Fork 此仓库，在本地机器上 [安装 Docsify](https://docsify.js.org/#/quickstart)，然后在此仓库的根文件夹中输入 `docsify serve`。网站将通过 localhost 的 3000 端口提供服务：`localhost:3000`。

> 注意，笔记本文件不会通过 Docsify 渲染，因此当您需要运行笔记本时，请在 VS Code 中单独运行 Python 内核。

## 其他课程

我们的团队还制作了其他课程！请查看：

- [生成式 AI 入门](https://aka.ms/genai-beginners)
- [生成式 AI 入门 .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [使用 JavaScript 的生成式 AI](https://github.com/microsoft/generative-ai-with-javascript)
- [使用 Java 的生成式 AI](https://aka.ms/genaijava)
- [AI 入门](https://aka.ms/ai-beginners)
- [数据科学入门](https://aka.ms/datascience-beginners)
- [机器学习入门](https://aka.ms/ml-beginners)
- [网络安全入门](https://github.com/microsoft/Security-101) 
- [Web 开发入门](https://aka.ms/webdev-beginners)
- [物联网入门](https://aka.ms/iot-beginners)
- [XR 开发入门](https://github.com/microsoft/xr-development-for-beginners)
- [掌握 GitHub Copilot 进行配对编程](https://github.com/microsoft/Mastering-GitHub-Copilot-for-Paired-Programming)
- [掌握 GitHub Copilot 进行 C#/.NET 开发](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers)
- [选择你的 Copilot 冒险](https://github.com/microsoft/CopilotAdventures)

---

**免责声明**：  
本文档使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原始语言的文档作为权威来源。对于重要信息，建议使用专业人工翻译。我们不对因使用此翻译而产生的任何误解或误读承担责任。