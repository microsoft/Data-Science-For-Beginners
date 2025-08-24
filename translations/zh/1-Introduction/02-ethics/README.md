<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8796f41f566a0a8ebb72863a83d558ed",
  "translation_date": "2025-08-24T12:21:07+00:00",
  "source_file": "1-Introduction/02-ethics/README.md",
  "language_code": "zh"
}
-->
# 数据伦理简介

|![ 由 [(@sketchthedocs)](https://sketchthedocs.dev) 绘制的速写笔记 ](../../sketchnotes/02-Ethics.png)|
|:---:|
| 数据科学伦理 - _速写笔记由 [@nitya](https://twitter.com/nitya) 绘制_ |

---

我们生活在一个数据化的世界中，都是数据公民。

市场趋势表明，到2022年，每三家大型组织中就有一家会通过在线[市场和交易所](https://www.gartner.com/smarterwithgartner/gartner-top-10-trends-in-data-and-analytics-for-2020/)买卖数据。作为**应用开发者**，我们将更容易、更便宜地将数据驱动的洞察和算法驱动的自动化集成到日常用户体验中。但随着人工智能的普及，我们也需要了解这种算法在大规模应用中可能带来的[武器化](https://www.youtube.com/watch?v=TQHs8SA1qpk)危害。

趋势还表明，到2025年，我们将创造和消费超过[180泽字节](https://www.statista.com/statistics/871513/worldwide-data-created/)的数据。作为**数据科学家**，这为我们提供了前所未有的个人数据访问权限。这意味着我们可以构建用户行为画像，并以某种方式影响决策，创造一种[自由选择的幻觉](https://www.datasciencecentral.com/profiles/blogs/the-illusion-of-choice)，同时可能将用户引导至我们偏好的结果。这也引发了关于数据隐私和用户保护的更广泛问题。

数据伦理现在是数据科学和工程的_必要护栏_，帮助我们最大限度地减少数据驱动行为可能带来的潜在危害和意外后果。[Gartner人工智能技术成熟度曲线](https://www.gartner.com/smarterwithgartner/2-megatrends-dominate-the-gartner-hype-cycle-for-artificial-intelligence-2020/)将数字伦理、负责任的人工智能和人工智能治理等相关趋势列为推动人工智能_民主化_和_工业化_等更大趋势的关键驱动力。

![Gartner 2020年人工智能技术成熟度曲线](https://images-cdn.newscred.com/Zz1mOWJhNzlkNDA2ZTMxMWViYjRiOGFiM2IyMjQ1YmMwZQ==)

在本课程中，我们将探索数据伦理这一迷人的领域——从核心概念和挑战，到案例研究和应用人工智能概念（如治理），帮助团队和组织建立数据和人工智能的伦理文化。

## [课前测验](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/2) 🎯

## 基本定义

让我们从理解基本术语开始。

“伦理”一词来源于[希腊词“ethikos”](https://en.wikipedia.org/wiki/Ethics)（及其词根“ethos”），意为_性格或道德本质_。

**伦理**是指在社会中规范我们行为的共同价值观和道德原则。伦理不是基于法律，而是基于广泛接受的“对与错”的规范。然而，伦理考量可以影响公司治理举措和政府法规，从而创造更多的合规激励。

**数据伦理**是一个[新的伦理分支](https://royalsocietypublishing.org/doi/full/10.1098/rsta.2016.0360#sec-1)，研究和评估与_数据、算法及相关实践_相关的道德问题。在这里，**“数据”**关注与生成、记录、管理、处理、传播、共享和使用相关的行为，**“算法”**关注人工智能、代理、机器学习和机器人，**“实践”**关注负责任的创新、编程、黑客行为和伦理规范等主题。

**应用伦理**是[道德考量的实际应用](https://en.wikipedia.org/wiki/Applied_ethics)。它是积极调查_现实世界行为、产品和流程_中的伦理问题，并采取纠正措施以确保这些行为与我们定义的伦理价值保持一致的过程。

**伦理文化**是关于[将应用伦理_付诸实践_](https://hbr.org/2019/05/how-to-design-an-ethical-organization)，确保我们的伦理原则和实践在整个组织中以一致且可扩展的方式被采纳。成功的伦理文化定义了全组织范围的伦理原则，提供有意义的合规激励，并通过鼓励和放大组织各级的期望行为来强化伦理规范。

## 伦理概念

在本节中，我们将讨论**共同价值观**（原则）和**伦理挑战**（问题）等数据伦理概念，并探索**案例研究**，帮助您在现实世界的背景中理解这些概念。

### 1. 伦理原则

每个数据伦理策略都从定义_伦理原则_开始——这些“共同价值观”描述了可接受的行为，并指导我们在数据和人工智能项目中的合规行动。您可以在个人或团队层面定义这些原则。然而，大多数大型组织会在公司层面定义这些原则，并通过_伦理人工智能_使命声明或框架在所有团队中一致执行。

**示例：**微软的[负责任的人工智能](https://www.microsoft.com/en-us/ai/responsible-ai)使命声明写道：_“我们致力于推动以人为本的伦理原则驱动的人工智能发展”_，并在以下框架中定义了6个伦理原则：

![微软的负责任人工智能](https://docs.microsoft.com/en-gb/azure/cognitive-services/personalizer/media/ethics-and-responsible-use/ai-values-future-computed.png)

让我们简要探讨这些原则。_透明性_和_问责性_是其他原则的基础价值观，因此我们从这里开始：

* [**问责性**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6)使从业者对其数据和人工智能操作以及对这些伦理原则的合规性负责。
* [**透明性**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6)确保数据和人工智能行为对用户是_可理解的_（可解释的），并解释决策背后的内容和原因。
* [**公平性**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1%3aprimaryr6)——关注确保人工智能对_所有人_公平对待，解决数据和系统中任何系统性或隐性社会技术偏见。
* [**可靠性与安全性**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6)——确保人工智能行为与定义的价值观_一致_，最大限度地减少潜在危害或意外后果。
* [**隐私与安全**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6)——关注数据来源的理解，并为用户提供_数据隐私及相关保护_。
* [**包容性**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6)——关注有意设计人工智能解决方案，使其适应_广泛的人类需求_和能力。

> 🚨 想一想您的数据伦理使命声明可能是什么。探索其他组织的伦理人工智能框架——以下是[IBM](https://www.ibm.com/cloud/learn/ai-ethics)、[Google](https://ai.google/principles)和[Facebook](https://ai.facebook.com/blog/facebooks-five-pillars-of-responsible-ai/)的示例。它们有哪些共同的价值观？这些原则如何与它们所处的人工智能产品或行业相关？

### 2. 伦理挑战

一旦我们定义了伦理原则，下一步就是评估我们的数据和人工智能行为是否与这些共同价值观一致。思考您的行为可以分为两类：_数据收集_和_算法设计_。

在数据收集方面，行为可能涉及**个人数据**或可识别的个人信息（PII），这些信息可以识别特定的活着的个人。这包括[多种非个人数据项](https://ec.europa.eu/info/law/law-topic/data-protection/reform/what-personal-data_en)，这些数据_共同_可以识别一个人。伦理挑战可能与_数据隐私_、_数据所有权_以及_知情同意_和_用户知识产权_等相关主题有关。

在算法设计方面，行为将涉及收集和管理**数据集**，然后使用它们训练和部署**数据模型**，以在现实世界中预测结果或自动化决策。伦理挑战可能来自_数据集偏差_、_数据质量_问题、_不公平性_和_算法误导_——包括一些系统性问题。

在这两种情况下，伦理挑战都突出了我们的行为可能与共同价值观发生冲突的领域。为了检测、缓解、最小化或消除这些问题，我们需要针对我们的行为提出道德上的“是/否”问题，然后根据需要采取纠正措施。让我们看看一些伦理挑战及其引发的道德问题：

#### 2.1 数据所有权

数据收集通常涉及可以识别数据主体的个人数据。[数据所有权](https://permission.io/blog/data-ownership)是关于与数据的创建、处理和传播相关的_控制_和[用户权利](https://permission.io/blog/data-ownership)。

需要提出的道德问题包括：
 * 数据的所有者是谁？（用户还是组织）
 * 数据主体拥有哪些权利？（例如：访问、删除、可移植性）
 * 组织拥有哪些权利？（例如：纠正恶意用户评论）

#### 2.2 知情同意

[知情同意](https://legaldictionary.net/informed-consent/)是指用户在_充分了解_相关事实（包括目的、潜在风险和替代方案）的情况下，同意某一行为（如数据收集）。

需要探讨的问题包括：
 * 用户（数据主体）是否同意数据的收集和使用？
 * 用户是否理解数据收集的目的？
 * 用户是否理解参与可能带来的潜在风险？

#### 2.3 知识产权

[知识产权](https://en.wikipedia.org/wiki/Intellectual_property)是指由人类创造的无形成果，这些成果可能对个人或企业具有_经济价值_。

需要探讨的问题包括：
 * 收集的数据是否对用户或企业具有经济价值？
 * **用户**是否拥有知识产权？
 * **组织**是否拥有知识产权？
 * 如果这些权利存在，我们如何保护它们？

#### 2.4 数据隐私

[数据隐私](https://www.northeastern.edu/graduate/blog/what-is-data-privacy/)或信息隐私是指在涉及个人身份信息时，保护用户隐私和身份的行为。

需要探讨的问题包括：
 * 用户的（个人）数据是否安全，防止黑客攻击和泄露？
 * 用户的数据是否仅对授权用户和上下文可访问？
 * 在数据共享或传播时，用户的匿名性是否得到保护？
 * 用户是否可以从匿名数据集中被重新识别？

#### 2.5 被遗忘权

[被遗忘权](https://en.wikipedia.org/wiki/Right_to_be_forgotten)或[删除权](https://www.gdpreu.org/right-to-be-forgotten/)为用户提供了额外的个人数据保护。具体来说，它赋予用户在_特定情况下_请求从互联网搜索和其他位置删除或移除个人数据的权利，使他们能够在线上重新开始，而不受过去行为的影响。

需要探讨的问题包括：
 * 系统是否允许数据主体请求删除数据？
 * 用户撤回同意是否应触发自动删除？
 * 数据是否未经同意或通过非法手段收集？
 * 我们是否符合政府关于数据隐私的法规？

#### 2.6 数据集偏差

数据集或[收集偏差](http://researcharticles.com/index.php/bias-in-data-collection-in-research/)是指为算法开发选择了_非代表性_的数据子集，从而可能导致对不同群体的不公平结果。偏差类型包括选择或抽样偏差、志愿者偏差和工具偏差。

需要探讨的问题包括：
 * 我们是否招募了具有代表性的数据主体？
 * 我们是否测试了收集或管理的数据集中的各种偏差？
 * 我们是否可以缓解或消除发现的任何偏差？

#### 2.7 数据质量

[数据质量](https://lakefs.io/data-quality-testing/)关注用于开发算法的管理数据集的有效性，检查特征和记录是否满足人工智能目的所需的准确性和一致性要求。

需要探讨的问题包括：
 * 我们是否捕获了适合我们用例的有效_特征_？
 * 数据是否在不同数据源之间_一致_地捕获？
 * 数据集是否_完整_，涵盖了不同条件或场景？
 * 捕获的信息是否_准确_，反映了现实？

#### 2.8 算法公平性
[算法公平性](https://towardsdatascience.com/what-is-algorithm-fairness-3182e161cf9f) 检查算法设计是否系统性地对特定数据主体的子群体存在歧视，从而导致在资源分配（_allocation_，即资源被拒绝或剥夺）和服务质量（_quality of service_，即AI对某些子群体的准确性不如其他群体）方面的[潜在危害](https://docs.microsoft.com/en-us/azure/machine-learning/concept-fairness-ml)。

需要探讨的问题包括：
 * 我们是否评估了模型在不同子群体和条件下的准确性？
 * 我们是否仔细检查了系统可能带来的危害（例如，刻板印象）？
 * 我们是否可以通过修订数据或重新训练模型来减轻已识别的危害？

探索诸如 [AI 公平性检查清单](https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RE4t6dA) 等资源以了解更多信息。

#### 2.9 数据误导

[数据误导](https://www.sciencedirect.com/topics/computer-science/misrepresentation) 是指我们是否通过对诚实报告的数据进行误导性解读来支持某种期望的叙述。

需要探讨的问题包括：
 * 我们是否报告了不完整或不准确的数据？
 * 我们是否以误导性方式可视化数据，从而得出错误的结论？
 * 我们是否使用选择性的统计技术来操纵结果？
 * 是否存在其他可能提供不同结论的解释？

#### 2.10 自由选择

[自由选择的幻觉](https://www.datasciencecentral.com/profiles/blogs/the-illusion-of-choice) 发生在系统的“选择架构”使用决策算法引导人们采取某种偏好的结果，同时看似给了他们选择和控制权。这些[暗黑模式](https://www.darkpatterns.org/)可能对用户造成社会和经济上的伤害。由于用户的决策会影响行为画像，这些行为可能进一步推动未来的选择，从而放大或延续这些伤害的影响。

需要探讨的问题包括：
 * 用户是否理解做出该选择的影响？
 * 用户是否了解（其他）选择及其各自的优缺点？
 * 用户是否可以在之后撤销自动化或被影响的选择？

### 3. 案例研究

为了将这些伦理挑战置于现实世界的背景中，可以通过案例研究来了解忽视这些伦理问题时对个人和社会可能造成的危害和后果。

以下是一些示例：

| 伦理挑战 | 案例研究  | 
|--- |--- |
| **知情同意** | 1972年 - [塔斯基吉梅毒研究](https://en.wikipedia.org/wiki/Tuskegee_Syphilis_Study) - 参与研究的非裔美国男性被承诺提供免费医疗服务，但研究人员欺骗了他们，没有告知他们的诊断或治疗的可用性。许多受试者因此死亡，其伴侣或子女也受到影响；该研究持续了40年。 | 
| **数据隐私** | 2007年 - [Netflix数据奖](https://www.wired.com/2007/12/why-anonymous-data-sometimes-isnt/) 向研究人员提供了_来自5万名客户的1000万条匿名电影评分_，以改进推荐算法。然而，研究人员能够将匿名数据与_外部数据集_（如IMDb评论）中的个人身份数据相关联，从而有效地“去匿名化”了一些Netflix用户。|
| **数据收集偏差** | 2013年 - 波士顿市[开发了Street Bump](https://www.boston.gov/transportation/street-bump)，一款让市民报告路面坑洼的应用，帮助城市更好地收集道路数据以发现和修复问题。然而，[低收入群体的人们较少拥有汽车和手机](https://hbr.org/2013/04/the-hidden-biases-in-big-data)，使得他们的道路问题在该应用中不可见。开发者与学术界合作解决_公平性和数字鸿沟_问题。 |
| **算法公平性** | 2018年 - 麻省理工学院[Gender Shades研究](http://gendershades.org/overview.html) 评估了性别分类AI产品的准确性，揭示了女性和有色人种的准确性差距。[2019年Apple Card](https://www.wired.com/story/the-apple-card-didnt-see-genderand-thats-the-problem/) 似乎为女性提供的信用额度低于男性。这两者都说明了算法偏差导致的社会经济危害问题。|
| **数据误导** | 2020年 - [乔治亚州公共卫生部发布的COVID-19图表](https://www.vox.com/covid-19-coronavirus-us-response-trump/2020/5/18/21262265/georgia-covid-19-cases-declining-reopening) 通过非时间顺序的x轴排序，似乎误导了公民对确诊病例趋势的理解。这说明了通过可视化技巧进行数据误导的现象。 |
| **自由选择的幻觉** | 2020年 - 学习应用[ABCmouse支付了1000万美元以解决FTC投诉](https://www.washingtonpost.com/business/2020/09/04/abcmouse-10-million-ftc-settlement/)，家长被迫支付无法取消的订阅费用。这说明了选择架构中的暗黑模式，用户被引导做出可能有害的选择。 |
| **数据隐私与用户权利** | 2021年 - Facebook [数据泄露](https://www.npr.org/2021/04/09/986005820/after-data-breach-exposes-530-million-facebook-says-it-will-not-notify-users) 暴露了5.3亿用户的数据，导致向FTC支付50亿美元的和解金。然而，它拒绝通知用户数据泄露，侵犯了用户关于数据透明性和访问的权利。|

想了解更多案例研究？请查看以下资源：
* [Ethics Unwrapped](https://ethicsunwrapped.utexas.edu/case-studies) - 涉及多个行业的伦理困境。
* [数据科学伦理课程](https://www.coursera.org/learn/data-science-ethics#syllabus) - 探讨标志性案例研究。
* [问题案例](https://deon.drivendata.org/examples/) - Deon清单中的示例。

> 🚨 想想你见过的案例研究——你是否经历过或受到过类似伦理挑战的影响？你能想到至少一个其他案例来说明我们在本节中讨论的伦理挑战之一吗？

## 应用伦理

我们已经讨论了伦理概念、挑战以及现实世界中的案例研究。那么，如何开始在我们的项目中_应用_伦理原则和实践？又如何_实现_这些实践以改进治理？让我们探索一些现实世界的解决方案：

### 1. 职业准则

职业准则为组织提供了一种选择，用以“激励”成员支持其伦理原则和使命声明。准则是专业行为的_道德指南_，帮助员工或成员做出符合组织原则的决策。它们的有效性取决于成员的自愿遵守；然而，许多组织提供额外的奖励和惩罚以激励成员遵守。

示例包括：

 * [Oxford Munich](http://www.code-of-ethics.org/code-of-conduct/) 伦理准则
 * [数据科学协会](http://datascienceassn.org/code-of-conduct.html) 行为准则（创建于2013年）
 * [ACM伦理与职业行为准则](https://www.acm.org/code-of-ethics)（自1993年起）

> 🚨 你是否属于某个专业工程或数据科学组织？浏览他们的网站，看看是否定义了职业伦理准则。这些准则说明了他们的伦理原则是什么？他们如何“激励”成员遵守准则？

### 2. 伦理清单

虽然职业准则定义了从业者的_伦理行为_要求，但它们在执行方面[存在已知的局限性](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md)，特别是在大规模项目中。因此，许多数据科学专家[提倡使用清单](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md)，以更确定和可操作的方式**将原则与实践联系起来**。

清单将问题转化为“是/否”任务，可以被操作化，允许它们作为标准产品发布工作流程的一部分进行跟踪。

示例包括：
 * [Deon](https://deon.drivendata.org/) - 一个通用的数据伦理清单，由[行业建议](https://deon.drivendata.org/#checklist-citations)创建，并提供命令行工具以便于集成。
 * [隐私审计清单](https://cyber.harvard.edu/ecommerce/privacyaudit.html) - 从法律和社会风险角度提供信息处理实践的一般指导。
 * [AI公平性清单](https://www.microsoft.com/en-us/research/project/ai-fairness-checklist/) - 由AI从业者创建，用于支持公平性检查在AI开发周期中的采用和集成。
 * [数据与AI伦理的22个问题](https://medium.com/the-organization/22-questions-for-ethics-in-data-and-ai-efb68fd19429) - 更开放的框架，适用于设计、实施和组织背景下伦理问题的初步探索。

### 3. 伦理法规

伦理是关于定义共同价值观并_自愿_做正确的事情。**合规**是指在有法律规定的情况下_遵守法律_。**治理**则涵盖了组织为执行伦理原则和遵守既定法律所采取的所有方式。

如今，治理在组织中有两种形式。首先，它是关于定义**伦理AI**原则并建立实践，以在组织的所有AI相关项目中实现这些原则的采用。其次，它是关于遵守其运营地区所有政府规定的**数据保护法规**。

数据保护和隐私法规的示例：

 * `1974年`，[美国隐私法案](https://www.justice.gov/opcl/privacy-act-1974) - 规范_联邦政府_对个人信息的收集、使用和披露。
 * `1996年`，[美国健康保险携带与责任法案（HIPAA）](https://www.cdc.gov/phlp/publications/topic/hipaa.html) - 保护个人健康数据。
 * `1998年`，[美国儿童在线隐私保护法案（COPPA）](https://www.ftc.gov/enforcement/rules/rulemaking-regulatory-reform-proceedings/childrens-online-privacy-protection-rule) - 保护13岁以下儿童的数据隐私。
 * `2018年`，[通用数据保护条例（GDPR）](https://gdpr-info.eu/) - 提供用户权利、数据保护和隐私。
 * `2018年`，[加州消费者隐私法案（CCPA）](https://www.oag.ca.gov/privacy/ccpa) - 赋予消费者对其（个人）数据的更多_权利_。
 * `2021年`，中国[个人信息保护法](https://www.reuters.com/world/china/china-passes-new-personal-data-privacy-law-take-effect-nov-1-2021-08-20/) 刚刚通过，成为全球最强的在线数据隐私法规之一。

> 🚨 欧盟定义的GDPR（通用数据保护条例）仍然是当今最具影响力的数据隐私法规之一。你知道它还定义了[8项用户权利](https://www.freeprivacypolicy.com/blog/8-user-rights-gdpr)以保护公民的数字隐私和个人数据吗？了解这些权利是什么以及它们为何重要。

### 4. 伦理文化

需要注意的是，在_合规_（做到“符合法律条文”）与解决[系统性问题](https://www.coursera.org/learn/data-science-ethics/home/week/4)（如僵化、信息不对称和分配不公平）之间仍然存在无形的差距，而这些问题可能加速AI的武器化。

后者需要[协作定义伦理文化](https://towardsdatascience.com/why-ai-ethics-requires-a-culture-driven-approach-26f451afa29f)，以在行业内的_组织之间_建立情感联系和一致的共同价值观。这需要在组织中[正式化数据伦理文化](https://www.codeforamerica.org/news/formalizing-an-ethical-data-culture/)，允许_任何人_ [拉动安灯绳](https://en.wikipedia.org/wiki/Andon_(manufacturing))（在过程中早期提出伦理问题），并将_伦理评估_（例如，在招聘中）作为AI项目团队组建的核心标准。

---
## [课后测验](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/3) 🎯
## 复习与自学

课程和书籍有助于理解核心伦理概念和挑战，而案例研究和工具有助于在现实世界中实践应用伦理。以下是一些入门资源：

* [机器学习初学者](https://github.com/microsoft/ML-For-Beginners/blob/main/1-Introduction/3-fairness/README.md) - 来自微软的公平性课程。
* [负责任人工智能原则](https://docs.microsoft.com/en-us/learn/modules/responsible-ai-principles/) - 来自 Microsoft Learn 的免费学习路径。
* [伦理与数据科学](https://resources.oreilly.com/examples/0636920203964) - O'Reilly 电子书 (M. Loukides, H. Mason 等人著)
* [数据科学伦理](https://www.coursera.org/learn/data-science-ethics#syllabus) - 密歇根大学的在线课程。
* [伦理解读](https://ethicsunwrapped.utexas.edu/case-studies) - 来自德克萨斯大学的案例研究。

# 作业

[撰写数据伦理案例研究](assignment.md)

**免责声明**：  
本文档使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用此翻译而产生的任何误解或误读不承担责任。