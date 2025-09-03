<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3a34157cc63516eba97c89a0b2f8c3e6",
  "translation_date": "2025-09-03T20:48:08+00:00",
  "source_file": "1-Introduction/02-ethics/README.md",
  "language_code": "en"
}
-->
# Introduction to Data Ethics

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/02-Ethics.png)|
|:---:|
| Data Science Ethics - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

---

We are all data citizens living in a world shaped by data.

Market trends suggest that by 2022, one in three large organizations will buy and sell their data through online [Marketplaces and Exchanges](https://www.gartner.com/smarterwithgartner/gartner-top-10-trends-in-data-and-analytics-for-2020/). As **App Developers**, it will become easier and more affordable to integrate data-driven insights and algorithm-based automation into everyday user experiences. However, as AI becomes more widespread, we must also understand the potential harms caused by the [weaponization](https://www.youtube.com/watch?v=TQHs8SA1qpk) of such algorithms on a large scale.

Trends also show that by 2025, we will create and consume over [180 zettabytes](https://www.statista.com/statistics/871513/worldwide-data-created/) of data. As **Data Scientists**, this provides unprecedented access to personal data, enabling us to build behavioral profiles of users and influence decision-making in ways that create an [illusion of free choice](https://www.datasciencecentral.com/profiles/blogs/the-illusion-of-choice) while potentially nudging users toward outcomes we prefer. This raises broader questions about data privacy and user protections.

Data ethics now serve as _necessary guardrails_ for data science and engineering, helping us minimize potential harms and unintended consequences from our data-driven actions. The [Gartner Hype Cycle for AI](https://www.gartner.com/smarterwithgartner/2-megatrends-dominate-the-gartner-hype-cycle-for-artificial-intelligence-2020/) highlights trends in digital ethics, responsible AI, and AI governance as key drivers for larger megatrends around the _democratization_ and _industrialization_ of AI.

![Gartner's Hype Cycle for AI - 2020](https://images-cdn.newscred.com/Zz1mOWJhNzlkNDA2ZTMxMWViYjRiOGFiM2IyMjQ1YmMwZQ==)

In this lesson, we'll dive into the fascinating field of data ethics—covering core concepts and challenges, case studies, and applied AI concepts like governance—that help establish an ethics culture within teams and organizations working with data and AI.

## [Pre-lecture quiz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/2) 🎯

## Basic Definitions

Let’s begin by understanding some basic terminology.

The word "ethics" comes from the [Greek word "ethikos"](https://en.wikipedia.org/wiki/Ethics) (and its root "ethos"), meaning _character or moral nature_. 

**Ethics** refers to the shared values and moral principles that guide our behavior in society. Ethics are not based on laws but on widely accepted norms of what is "right vs. wrong." However, ethical considerations can influence corporate governance initiatives and government regulations, creating incentives for compliance.

**Data Ethics** is a [new branch of ethics](https://royalsocietypublishing.org/doi/full/10.1098/rsta.2016.0360#sec-1) that "studies and evaluates moral problems related to _data, algorithms, and corresponding practices_." Here, **"data"** focuses on actions like generation, recording, curation, processing, dissemination, sharing, and usage; **"algorithms"** focuses on AI, agents, machine learning, and robots; and **"practices"** focuses on topics like responsible innovation, programming, hacking, and ethics codes.

**Applied Ethics** is the [practical application of moral considerations](https://en.wikipedia.org/wiki/Applied_ethics). It involves actively investigating ethical issues in the context of _real-world actions, products, and processes_ and taking corrective measures to ensure alignment with defined ethical values.

**Ethics Culture** is about [_operationalizing_ applied ethics](https://hbr.org/2019/05/how-to-design-an-ethical-organization) to ensure that ethical principles and practices are consistently and scalably adopted across an organization. Successful ethics cultures define organization-wide ethical principles, provide meaningful incentives for compliance, and reinforce ethical norms by encouraging and amplifying desired behaviors at every level of the organization.

## Ethics Concepts

In this section, we’ll discuss concepts like **shared values** (principles) and **ethical challenges** (problems) in data ethics—and explore **case studies** to understand these concepts in real-world contexts.

### 1. Ethics Principles

Every data ethics strategy starts by defining _ethical principles_—the "shared values" that describe acceptable behaviors and guide compliant actions in data and AI projects. These can be defined at an individual or team level, but most large organizations outline them in an _ethical AI_ mission statement or framework that is defined at the corporate level and enforced consistently across all teams.

**Example:** Microsoft's [Responsible AI](https://www.microsoft.com/en-us/ai/responsible-ai) mission statement reads: _"We are committed to the advancement of AI driven by ethical principles that put people first"_—identifying six ethical principles in the framework below:

![Responsible AI at Microsoft](https://docs.microsoft.com/en-gb/azure/cognitive-services/personalizer/media/ethics-and-responsible-use/ai-values-future-computed.png)

Let’s briefly explore these principles. _Transparency_ and _accountability_ are foundational values upon which other principles are built—so let’s start there:

* [**Accountability**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) makes practitioners _responsible_ for their data and AI operations and compliance with ethical principles.
* [**Transparency**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) ensures that data and AI actions are _understandable_ (interpretable) to users, explaining the what and why behind decisions.
* [**Fairness**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1%3aprimaryr6) focuses on ensuring AI treats _all people_ fairly, addressing systemic or implicit socio-technical biases in data and systems.
* [**Reliability & Safety**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) ensures that AI behaves _consistently_ with defined values, minimizing potential harms or unintended consequences.
* [**Privacy & Security**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) involves understanding data lineage and providing _data privacy and related protections_ to users.
* [**Inclusiveness**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) focuses on designing AI solutions with intention, adapting them to meet a _broad range of human needs_ and capabilities.

> 🚨 Think about what your data ethics mission statement could be. Explore ethical AI frameworks from other organizations—examples include [IBM](https://www.ibm.com/cloud/learn/ai-ethics), [Google](https://ai.google/principles), and [Facebook](https://ai.facebook.com/blog/facebooks-five-pillars-of-responsible-ai/). What shared values do they have in common? How do these principles relate to the AI products or industries they operate in?

### 2. Ethics Challenges

After defining ethical principles, the next step is to evaluate our data and AI actions to ensure they align with those shared values. Consider your actions in two categories: _data collection_ and _algorithm design_.

In data collection, actions often involve **personal data** or personally identifiable information (PII) for identifiable living individuals. This includes [various types of non-personal data](https://ec.europa.eu/info/law/law-topic/data-protection/reform/what-personal-data_en) that, when combined, can identify an individual. Ethical challenges may relate to _data privacy_, _data ownership_, and topics like _informed consent_ and _intellectual property rights_ for users.

In algorithm design, actions involve collecting and curating **datasets**, then using them to train and deploy **data models** that predict outcomes or automate decisions in real-world contexts. Ethical challenges may arise from _dataset bias_, _data quality_ issues, _unfairness_, and _misrepresentation_ in algorithms—including systemic issues.

In both cases, ethical challenges highlight areas where actions may conflict with shared values. To detect, mitigate, minimize, or eliminate these concerns, we need to ask moral "yes/no" questions about our actions and take corrective measures as needed. Let’s examine some ethical challenges and the moral questions they raise:

#### 2.1 Data Ownership

Data collection often involves personal data that can identify individuals. [Data ownership](https://permission.io/blog/data-ownership) concerns _control_ and [_user rights_](https://permission.io/blog/data-ownership) related to the creation, processing, and dissemination of data.

Moral questions to consider:
* Who owns the data? (user or organization)
* What rights do data subjects have? (e.g., access, erasure, portability)
* What rights do organizations have? (e.g., rectifying malicious user reviews)

#### 2.2 Informed Consent

[Informed consent](https://legaldictionary.net/informed-consent/) involves users agreeing to an action (like data collection) with a _full understanding_ of relevant facts, including the purpose, potential risks, and alternatives.

Questions to explore:
* Did the user (data subject) give permission for data capture and usage?
* Did the user understand the purpose of data collection?
* Did the user understand the potential risks of their participation?

#### 2.3 Intellectual Property

[Intellectual property](https://en.wikipedia.org/wiki/Intellectual_property) refers to intangible creations resulting from human initiative that may _have economic value_ to individuals or businesses.

Questions to explore:
* Did the collected data have economic value to a user or business?
* Does the **user** have intellectual property rights here?
* Does the **organization** have intellectual property rights here?
* If these rights exist, how are they being protected?

#### 2.4 Data Privacy

[Data privacy](https://www.northeastern.edu/graduate/blog/what-is-data-privacy/) refers to preserving user privacy and protecting user identity with respect to personally identifiable information.

Questions to explore:
* Is users' (personal) data secured against hacks and leaks?
* Is users' data accessible only to authorized users and contexts?
* Is users' anonymity preserved when data is shared or disseminated?
* Can a user be de-identified from anonymized datasets?

#### 2.5 Right To Be Forgotten

The [Right To Be Forgotten](https://en.wikipedia.org/wiki/Right_to_be_forgotten) or [Right to Erasure](https://www.gdpreu.org/right-to-be-forgotten/) provides additional personal data protection to users. It allows users to request deletion or removal of personal data from Internet searches and other locations, _under specific circumstances_—giving them a fresh start online without past actions being held against them.

Questions to explore:
* Does the system allow data subjects to request erasure?
* Should the withdrawal of user consent trigger automated erasure?
* Was data collected without consent or by unlawful means?
* Are we compliant with government regulations for data privacy?

#### 2.6 Dataset Bias

Dataset or [Collection Bias](http://researcharticles.com/index.php/bias-in-data-collection-in-research/) involves selecting a _non-representative_ subset of data for algorithm development, potentially creating unfairness in outcomes for diverse groups. Types of bias include selection or sampling bias, volunteer bias, and instrument bias.

Questions to explore:
* Did we recruit a representative set of data subjects?
* Did we test our collected or curated dataset for various biases?
* Can we mitigate or remove any discovered biases?

#### 2.7 Data Quality

[Data Quality](https://lakefs.io/data-quality-testing/) examines the validity of the curated dataset used to develop algorithms, ensuring features and records meet the required level of accuracy and consistency for the intended AI purpose.

Questions to explore:
* Did we capture valid _features_ for our use case?
* Was data captured _consistently_ across diverse data sources?
* Is the dataset _complete_ for diverse conditions or scenarios?
* Is information captured _accurately_ to reflect reality?

#### 2.8 Algorithm Fairness
[Algorithm Fairness](https://towardsdatascience.com/what-is-algorithm-fairness-3182e161cf9f) examines whether the design of an algorithm systematically discriminates against specific subgroups of individuals, potentially causing [harm](https://docs.microsoft.com/en-us/azure/machine-learning/concept-fairness-ml) in areas such as _allocation_ (where resources are denied or withheld from certain groups) and _quality of service_ (where AI performs less accurately for some subgroups compared to others).

Questions to consider:
 * Have we assessed the model's accuracy across diverse subgroups and conditions?
 * Have we analyzed the system for potential harms (e.g., stereotyping)?
 * Can we adjust the data or retrain the models to address identified harms?

Explore resources like [AI Fairness checklists](https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RE4t6dA) for further learning.

#### 2.9 Misrepresentation

[Data Misrepresentation](https://www.sciencedirect.com/topics/computer-science/misrepresentation) involves questioning whether insights derived from data are being communicated in a misleading way to support a specific narrative.

Questions to consider:
 * Are we presenting incomplete or inaccurate data?
 * Are we visualizing data in ways that lead to false conclusions?
 * Are we selectively using statistical techniques to manipulate outcomes?
 * Are there alternative explanations that could lead to different conclusions?

#### 2.10 Free Choice
The [Illusion of Free Choice](https://www.datasciencecentral.com/profiles/blogs/the-illusion-of-choice) arises when decision-making algorithms in "choice architectures" subtly push users toward a preferred outcome while giving the appearance of options and control. These [dark patterns](https://www.darkpatterns.org/) can result in social and economic harm to users. Since user decisions influence behavior profiles, these actions can shape future choices, amplifying the impact of these harms.

Questions to consider:
 * Did the user fully understand the consequences of their choice?
 * Was the user aware of alternative options and the pros and cons of each?
 * Can the user later reverse an automated or influenced decision?

### 3. Case Studies

To understand these ethical challenges in real-world scenarios, case studies can illustrate the potential harms and societal consequences when ethical violations are ignored.

Here are some examples:

| Ethics Challenge | Case Study  | 
|--- |--- |
| **Informed Consent** | 1972 - [Tuskegee Syphilis Study](https://en.wikipedia.org/wiki/Tuskegee_Syphilis_Study) - African American men were promised free medical care but were deceived by researchers who did not inform them of their diagnosis or available treatment. Many participants died, and their families were affected. The study lasted 40 years. | 
| **Data Privacy** | 2007 - The [Netflix data prize](https://www.wired.com/2007/12/why-anonymous-data-sometimes-isnt/) provided researchers with _10M anonymized movie ratings from 50K customers_ to improve recommendation algorithms. However, researchers were able to link anonymized data to personally identifiable information in _external datasets_ (e.g., IMDb comments), effectively "de-anonymizing" some Netflix users. |
| **Collection Bias** | 2013 - The City of Boston [developed Street Bump](https://www.boston.gov/transportation/street-bump), an app for citizens to report potholes, helping the city collect better roadway data. However, [lower-income groups had less access to cars and smartphones](https://hbr.org/2013/04/the-hidden-biases-in-big-data), making their roadway issues invisible in the app. Developers collaborated with academics to address _equitable access and digital divide_ issues for fairness. |
| **Algorithmic Fairness** | 2018 - The MIT [Gender Shades Study](http://gendershades.org/overview.html) evaluated the accuracy of gender classification AI products, revealing disparities in accuracy for women and people of color. A [2019 Apple Card](https://www.wired.com/story/the-apple-card-didnt-see-genderand-thats-the-problem/) appeared to offer less credit to women than men, highlighting algorithmic bias and its socio-economic consequences. |
| **Data Misrepresentation** | 2020 - The [Georgia Department of Public Health released COVID-19 charts](https://www.vox.com/covid-19-coronavirus-us-response-trump/2020/5/18/21262265/georgia-covid-19-cases-declining-reopening) that misled citizens about case trends by using non-chronological ordering on the x-axis. This demonstrates misrepresentation through visualization techniques. |
| **Illusion of free choice** | 2020 - Learning app [ABCmouse paid $10M to settle an FTC complaint](https://www.washingtonpost.com/business/2020/09/04/abcmouse-10-million-ftc-settlement/) where parents were trapped into paying for subscriptions they couldn't cancel. This illustrates dark patterns in choice architectures, nudging users toward harmful decisions. |
| **Data Privacy & User Rights** | 2021 - Facebook [Data Breach](https://www.npr.org/2021/04/09/986005820/after-data-breach-exposes-530-million-facebook-says-it-will-not-notify-users) exposed data from 530M users, resulting in a $5B settlement to the FTC. However, Facebook refused to notify users of the breach, violating their rights to data transparency and access. |

Want to explore more case studies? Check out these resources:
* [Ethics Unwrapped](https://ethicsunwrapped.utexas.edu/case-studies) - ethics dilemmas across various industries. 
* [Data Science Ethics course](https://www.coursera.org/learn/data-science-ethics#syllabus) - landmark case studies explored.
* [Where things have gone wrong](https://deon.drivendata.org/examples/) - deon checklist with examples.

> 🚨 Reflect on the case studies you've encountered—have you experienced or been affected by a similar ethical challenge? Can you think of another case study that illustrates one of the ethical challenges discussed here?

## Applied Ethics

We've explored ethical concepts, challenges, and case studies in real-world contexts. But how can we start _applying_ ethical principles and practices in our projects? And how can we _operationalize_ these practices for better governance? Let’s examine some practical solutions:

### 1. Professional Codes

Professional Codes provide a way for organizations to "encourage" members to align with their ethical principles and mission statement. These codes act as _moral guidelines_ for professional behavior, helping employees or members make decisions consistent with their organization's values. Their effectiveness depends on voluntary compliance, but many organizations offer rewards or penalties to motivate adherence.

Examples include:
 * [Oxford Munich](http://www.code-of-ethics.org/code-of-conduct/) Code of Ethics
 * [Data Science Association](http://datascienceassn.org/code-of-conduct.html) Code of Conduct (created 2013)
 * [ACM Code of Ethics and Professional Conduct](https://www.acm.org/code-of-ethics) (since 1993)

> 🚨 Are you part of a professional engineering or data science organization? Check their website to see if they have a professional code of ethics. What does it say about their ethical principles? How do they "encourage" members to follow the code?

### 2. Ethics Checklists

While professional codes define expected _ethical behavior_, they [have limitations](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md) in enforcement, especially in large-scale projects. Many data science experts [recommend checklists](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md) to **translate principles into actionable practices**.

Checklists turn questions into "yes/no" tasks that can be integrated into standard workflows, making them easier to track during product development.

Examples include:
 * [Deon](https://deon.drivendata.org/) - a general-purpose data ethics checklist based on [industry recommendations](https://deon.drivendata.org/#checklist-citations), with a command-line tool for easy integration.
 * [Privacy Audit Checklist](https://cyber.harvard.edu/ecommerce/privacyaudit.html) - offers general guidance for handling information from legal and social perspectives.
 * [AI Fairness Checklist](https://www.microsoft.com/en-us/research/project/ai-fairness-checklist/) - created by AI practitioners to integrate fairness checks into AI development cycles.
 * [22 questions for ethics in data and AI](https://medium.com/the-organization/22-questions-for-ethics-in-data-and-ai-efb68fd19429) - an open-ended framework for exploring ethical issues in design, implementation, and organizational contexts.

### 3. Ethics Regulations

Ethics involves defining shared values and voluntarily doing the right thing. **Compliance** focuses on _following the law_ where applicable. **Governance** encompasses all organizational efforts to enforce ethical principles and comply with legal requirements.

Governance today has two main aspects. First, it involves defining **ethical AI** principles and implementing practices to ensure adoption across all AI-related projects. Second, it requires compliance with government-mandated **data protection regulations** in the regions where the organization operates.

Examples of data protection and privacy regulations:
 * `1974`, [US Privacy Act](https://www.justice.gov/opcl/privacy-act-1974) - regulates _federal government_ collection, use, and disclosure of personal information.
 * `1996`, [US Health Insurance Portability & Accountability Act (HIPAA)](https://www.cdc.gov/phlp/publications/topic/hipaa.html) - protects personal health data.
 * `1998`, [US Children's Online Privacy Protection Act (COPPA)](https://www.ftc.gov/enforcement/rules/rulemaking-regulatory-reform-proceedings/childrens-online-privacy-protection-rule) - safeguards the privacy of children under 13.
 * `2018`, [General Data Protection Regulation (GDPR)](https://gdpr-info.eu/) - provides user rights, data protection, and privacy.
 * `2018`, [California Consumer Privacy Act (CCPA)](https://www.oag.ca.gov/privacy/ccpa) - grants consumers more control over their personal data.
 * `2021`, China's [Personal Information Protection Law](https://www.reuters.com/world/china/china-passes-new-personal-data-privacy-law-take-effect-nov-1-2021-08-20/) - one of the strongest online data privacy regulations globally.

> 🚨 The European Union's GDPR (General Data Protection Regulation) is one of the most influential data privacy regulations today. Did you know it also defines [8 user rights](https://www.freeprivacypolicy.com/blog/8-user-rights-gdpr) to protect citizens' digital privacy and personal data? Learn about these rights and why they matter.

### 4. Ethics Culture

There is often a gap between _compliance_ (meeting legal requirements) and addressing [systemic issues](https://www.coursera.org/learn/data-science-ethics/home/week/4) (such as ossification, information asymmetry, and distributional unfairness) that can accelerate the misuse of AI.

Addressing these issues requires [collaborative efforts to build ethics cultures](https://towardsdatascience.com/why-ai-ethics-requires-a-culture-driven-approach-26f451afa29f) that foster emotional connections and shared values across organizations and industries. This involves creating [formalized data ethics cultures](https://www.codeforamerica.org/news/formalizing-an-ethical-data-culture/) within organizations, empowering _anyone_ to [raise concerns early](https://en.wikipedia.org/wiki/Andon_(manufacturing)) and making ethical considerations (e.g., in hiring) a core criterion for forming AI project teams.

---
## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ds/) 🎯
## Review & Self Study 

Courses and books help build a foundation in ethics concepts and challenges, while case studies and tools provide practical insights into applying ethics in real-world scenarios. Here are some resources to get started:

* [Machine Learning For Beginners](https://github.com/microsoft/ML-For-Beginners/blob/main/1-Introduction/3-fairness/README.md) - lesson on Fairness, from Microsoft.
* [Principles of Responsible AI](https://docs.microsoft.com/en-us/learn/modules/responsible-ai-principles/) - free learning path from Microsoft Learn.  
* [Ethics and Data Science](https://resources.oreilly.com/examples/0636920203964) - O'Reilly EBook (M. Loukides, H. Mason et. al)  
* [Data Science Ethics](https://www.coursera.org/learn/data-science-ethics#syllabus) - online course from the University of Michigan.  
* [Ethics Unwrapped](https://ethicsunwrapped.utexas.edu/case-studies) - case studies from the University of Texas.  

# Assignment  

[Write A Data Ethics Case Study](assignment.md)  

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.