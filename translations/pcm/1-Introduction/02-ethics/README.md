<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "58860ce9a4b8a564003d2752f7c72851",
  "translation_date": "2025-11-18T18:32:37+00:00",
  "source_file": "1-Introduction/02-ethics/README.md",
  "language_code": "pcm"
}
-->
# Introduction to Data Ethics

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/02-Ethics.png)|
|:---:|
| Data Science Ethics - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

---

All of us na data people wey dey live for world wey full with data.

Market trend dey show say by 2022, 1 out of 3 big companies go dey buy and sell their data for online [Marketplaces and Exchanges](https://www.gartner.com/smarterwithgartner/gartner-top-10-trends-in-data-and-analytics-for-2020/). As **App Developers**, e go dey easier and cheaper for us to use data to give insight and use algorithm to make things automatic for everyday user experience. But as AI dey everywhere now, we go need understand the wahala wey fit happen if dem use [weaponization](https://www.youtube.com/watch?v=TQHs8SA1qpk) of this kind algorithm anyhow.

Trend dey show say by 2025, we go dey create and use over [180 zettabytes](https://www.statista.com/statistics/871513/worldwide-data-created/) of data. For **Data Scientists**, this plenty information go give us chance to get access to personal and behavior data wey never happen before. With this power, we fit build detailed user profile and dey influence decision-making small small—sometimes in way wey go make people think say dem dey choose freely when e no be so. This kind thing fit help push users go where we want, but e also dey bring big question about data privacy, freedom, and the limit wey dey for how algorithm fit dey influence people.

Data ethics na _necessary guardrails_ for data science and engineering, e dey help us reduce wahala and things wey we no plan for wey fit happen because of how we dey use data. The [Gartner Hype Cycle for AI](https://www.gartner.com/smarterwithgartner/2-megatrends-dominate-the-gartner-hype-cycle-for-artificial-intelligence-2020/) dey show trend for digital ethics, responsible AI, and AI governance as big things wey dey push _democratization_ and _industrialization_ of AI.

![Gartner's Hype Cycle for AI - 2020](https://images-cdn.newscred.com/Zz1mOWJhNzlkNDA2ZTMxMWViYjRiOGFiM2IyMjQ1YmMwZQ==)

For this lesson, we go look the interesting area of data ethics - from the main ideas and wahala, to case studies and how AI dey work like governance - wey dey help build ethics culture for teams and companies wey dey work with data and AI.




## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ds/quiz/2) 🎯

## Basic Definitions

Make we first understand the basic words.

The word "ethics" come from the [Greek word "ethikos"](https://en.wikipedia.org/wiki/Ethics) (and the root "ethos") wey mean _character or moral nature_. 

**Ethics** na the shared values and moral rules wey dey guide how we dey behave for society. Ethics no dey based on law but on the things wey people agree say na "right vs. wrong". But, ethics fit affect how companies dey do their governance and how government dey make rules wey go make people follow.

**Data Ethics** na [new branch of ethics](https://royalsocietypublishing.org/doi/full/10.1098/rsta.2016.0360#sec-1) wey dey "study and check moral wahala wey dey related to _data, algorithms and the way we dey use them_". For here, **"data"** dey talk about things like how we dey create, record, arrange, process, share, and use data, **"algorithms"** dey focus on AI, agents, machine learning, and robots, and **"practices"** dey talk about things like responsible innovation, programming, hacking, and ethics codes.

**Applied Ethics** na the [practical way we dey use moral ideas](https://en.wikipedia.org/wiki/Applied_ethics). E mean say we dey look into ethical wahala for _real-world actions, products and processes_, and dey take action to make sure say dem dey follow the ethical values wey we don set.

**Ethics Culture** na about [_making applied ethics work_](https://hbr.org/2019/05/how-to-design-an-ethical-organization) to make sure say the ethical rules and ways wey we dey do things dey used well and fit work for the whole company. Good ethics culture dey define company-wide ethical rules, give good reason for people to follow, and dey encourage and show the kind behavior wey we want for every level of the company.


## Ethics Concepts

For this part, we go talk about things like **shared values** (principles) and **ethical wahala** (problems) for data ethics - and we go look **case studies** wey go help you understand these ideas for real-world situations.

### 1. Ethics Principles

Every data ethics plan dey start with defining _ethical principles_ - the "shared values" wey dey describe the kind behavior wey we go accept, and dey guide the actions wey go follow the rules, for our data & AI projects. You fit define these for individual or team level. But, most big companies dey write these for _ethical AI_ mission statement or framework wey dem dey set for company level and dey make sure say all teams dey follow am.

**Example:** Microsoft's [Responsible AI](https://www.microsoft.com/en-us/ai/responsible-ai) mission statement talk say: _"We dey committed to the growth of AI wey dey follow ethical rules wey dey put people first"_ - dem identify 6 ethical principles for the framework wey dey below:

![Responsible AI at Microsoft](https://docs.microsoft.com/en-gb/azure/cognitive-services/personalizer/media/ethics-and-responsible-use/ai-values-future-computed.png)

Make we look these principles small. _Transparency_ and _accountability_ na the main values wey other principles dey build on - so make we start from there:

* [**Accountability**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) dey make people wey dey work with data & AI responsible for their actions, and make sure say dem dey follow these ethical rules.
* [**Transparency**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) dey make sure say data and AI actions dey _clear_ (understandable) to users, explaining wetin and why dem make decisions.
* [**Fairness**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1%3aprimaryr6) - dey focus on making sure say AI dey treat _everybody_ fairly, and dey fix any bias wey dey for data and systems.
* [**Reliability & Safety**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) - dey make sure say AI dey behave _well_ with the values wey we don set, and dey reduce wahala or things wey we no plan for.
* [**Privacy & Security**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) - dey talk about understanding data lineage, and dey give _data privacy and protection_ to users.
* [**Inclusiveness**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) - dey talk about designing AI solutions wey go fit meet _plenty human needs_ & abilities.

> 🚨 Think about wetin your data ethics mission statement fit be. Check ethical AI frameworks from other companies - here na examples from [IBM](https://www.ibm.com/cloud/learn/ai-ethics), [Google](https://ai.google/principles), and [Facebook](https://ai.facebook.com/blog/facebooks-five-pillars-of-responsible-ai/). Wetin dem get in common for their shared values? How these principles dey connect to the AI product or industry wey dem dey work for?

### 2. Ethics Challenges

After we don define ethical principles, the next thing na to check our data and AI actions to see if dem dey follow those shared values. Think about your actions for two parts: _data collection_ and _algorithm design_. 

For data collection, actions go involve **personal data** or personally identifiable information (PII) wey fit identify living people. This one include [different types of non-personal data](https://ec.europa.eu/info/law/law-topic/data-protection/reform/what-personal-data_en) wey _together_ fit identify person. Ethical wahala fit dey about _data privacy_, _data ownership_, and things like _informed consent_ and _intellectual property rights_ for users.

For algorithm design, actions go involve collecting & arranging **datasets**, then using them to train & deploy **data models** wey dey predict things or dey make decisions for real-world situations. Ethical wahala fit come from _dataset bias_, _data quality_ problems, _unfairness_, and _misrepresentation_ for algorithms - including some wahala wey dey inside the system.

For both cases, ethics wahala dey show where our actions fit no follow our shared values. To find, reduce, or remove these problems - we need ask moral "yes/no" questions about our actions, then take action to fix am. Make we look some ethical wahala and the moral questions wey dem dey bring:


#### 2.1 Data Ownership

Data collection dey involve personal data wey fit identify the people wey the data belong to. [Data ownership](https://permission.io/blog/data-ownership) na about _control_ and [_user rights_](https://permission.io/blog/data-ownership) for how data dey created, processed, and shared. 

The moral questions wey we need ask na: 
 * Who get the data? (user or company)
 * Wetin be the rights wey data people get? (ex: access, erasure, portability)
 * Wetin be the rights wey companies get? (ex: fix bad user reviews)

#### 2.2 Informed Consent

[Informed consent](https://legaldictionary.net/informed-consent/) na when users agree to something (like data collection) with _full understanding_ of the facts like the purpose, risks, and other options. 

Questions to ask na:
 * The user (data person) give permission for data collection and use?
 * The user understand the reason why dem collect the data?
 * The user understand the risks wey fit happen because dem participate?

#### 2.3 Intellectual Property

[Intellectual property](https://en.wikipedia.org/wiki/Intellectual_property) na the things wey people create wey fit get economic value for them or their business. 

Questions to ask na:
 * The data wey dem collect get economic value for user or business?
 * The **user** get intellectual property for this matter?
 * The **company** get intellectual property for this matter?
 * If these rights dey, how we dey protect them?

#### 2.4 Data Privacy

[Data privacy](https://www.northeastern.edu/graduate/blog/what-is-data-privacy/) or information privacy na about keeping user privacy and protecting their identity for personal data. 

Questions to ask na:
 * The users' (personal) data dey safe from hacks and leaks?
 * The users' data dey accessible only to people wey suppose see am?
 * The users' anonymity dey kept when data dey shared or spread?
 * Person fit remove their identity from data wey dem don anonymize?

#### 2.5 Right To Be Forgotten

The [Right To Be Forgotten](https://en.wikipedia.org/wiki/Right_to_be_forgotten) or [Right to Erasure](https://www.gdpreu.org/right-to-be-forgotten/) dey give extra protection for personal data to users. E dey allow users request make their personal data dey deleted or removed from Internet searches and other places, _under certain conditions_ - so dem fit start fresh online without their past actions dey affect them.

Questions to ask na:
 * The system dey allow data people request make their data dey deleted?
 * If user withdraw their consent, e suppose trigger automatic deletion?
 * Dem collect data without consent or in illegal way?
 * We dey follow government rules for data privacy?

#### 2.6 Dataset Bias

Dataset or [Collection Bias](http://researcharticles.com/index.php/bias-in-data-collection-in-research/) na when we select _data wey no represent everybody_ for algorithm development, e fit cause unfair results for different groups. Types of bias include selection or sampling bias, volunteer bias, and instrument bias. 

Questions to ask na:
 * We recruit data people wey represent everybody well?
 * We test the data wey we collect or arrange for different bias?
 * We fit reduce or remove any bias wey we find?

#### 2.7 Data Quality

[Data Quality](https://lakefs.io/data-quality-testing/) dey check the dataset wey we arrange for our algorithms, to see if the features and records dey meet the level of accuracy and consistency wey we need for our AI purpose.

Questions to ask na:
 * We capture valid _features_ for our use case?
 * The data wey we capture dey _consistent_ across different sources?
 * The dataset dey _complete_ for different conditions or situations?
* Di information wey dem capture dey _accurate_ to show wetin dey happen for real life?

#### 2.8 Algorithm Fairness

[Algorithm Fairness](https://towardsdatascience.com/what-is-algorithm-fairness-3182e161cf9f) dey check whether di way dem design di algorithm dey do bad thing against some group of people wey dey inside di data. Dis one fit cause [wahala](https://docs.microsoft.com/en-us/azure/machine-learning/concept-fairness-ml) for _allocation_ (where dem no gree give resources or dem hold am back for di group) and _quality of service_ (where AI no dey accurate for some group like e dey for others).

Questions wey you fit ask for dis one na:
* We don check di model accuracy for different group of people and conditions?
* We don look di system well to see if e fit cause wahala (like stereotyping)?
* We fit change di data or train di model again to stop di wahala wey we don see?

Make you check resources like [AI Fairness checklists](https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RE4t6dA) to sabi more.

#### 2.9 Misrepresentation

[Data Misrepresentation](https://www.sciencedirect.com/topics/computer-science/misrepresentation) na to ask whether di way we dey show di data insight dey honest or we dey use am lie to push wetin we want make people believe.

Questions wey you fit ask for dis one na:
* We dey report data wey no complete or wey no correct?
* Di way we dey show di data fit make people misunderstand wetin e mean?
* We dey use some kind statistical method to change di result?
* Other explanation dey wey fit show different conclusion?

#### 2.10 Free Choice
Di [Illusion of Free Choice](https://www.datasciencecentral.com/profiles/blogs/the-illusion-of-choice) na when di system dey use decision-making algorithm to push people to choose wetin dem want, but e go look like say dem get options and control. Dis [dark patterns](https://www.darkpatterns.org/) fit cause social and economic wahala for users. Di choice wey users dey make fit affect their behavior profile, and dis one fit make di wahala big or long.

Questions wey you fit ask for dis one na:
* Di user sabi wetin e mean to make dat choice?
* Di user sabi di other options wey dey and di good and bad side of each one?
* Di user fit change di choice wey di system or influence make am choose later?

### 3. Case Studies

To understand how dis ethical wahala dey affect real life, e good to look case studies wey dey show di wahala and di effect for people and society when dem no follow ethics. 

Here be some examples:

| Ethics Wahala | Case Study  | 
|--- |--- |
| **Informed Consent** | 1972 - [Tuskegee Syphilis Study](https://en.wikipedia.org/wiki/Tuskegee_Syphilis_Study) - African American men wey join di study dem promise dem free medical care _but dem lie_ give dem. Di researchers no tell dem say dem get di sickness or say treatment dey. Many people die and di wahala affect their partners and children; di study last for 40 years. | 
| **Data Privacy** |  2007 - Di [Netflix data prize](https://www.wired.com/2007/12/why-anonymous-data-sometimes-isnt/) give researchers _10M anonymized movie rankings from 50K customers_ to help improve recommendation algorithms. But researchers fit match di anonymized data with personal data from _external datasets_ (like IMDb comments) - dem "de-anonymize" some Netflix subscribers.|
| **Collection Bias**  | 2013 - Di City of Boston [develop Street Bump](https://www.boston.gov/transportation/street-bump), one app wey citizens fit use report potholes, to help di city get better road data to fix di wahala. But [people wey dey low income group no get cars and phones](https://hbr.org/2013/04/the-hidden-biases-in-big-data), so di wahala for their road no show for di app. Di developers work with academics to fix di wahala of _equitable access and digital divides_ for fairness. |
| **Algorithmic Fairness**  | 2018 - Di MIT [Gender Shades Study](http://gendershades.org/overview.html) check di accuracy of gender classification AI products, dem see say e no dey accurate for women and people of color. For [2019 Apple Card](https://www.wired.com/story/the-apple-card-didnt-see-genderand-thats-the-problem/) e look like say dem give women less credit than men. Both show di wahala of algorithm bias wey dey cause socio-economic wahala.|
| **Data Misrepresentation** | 2020 - Di [Georgia Department of Public Health release COVID-19 charts](https://www.vox.com/covid-19-coronavirus-us-response-trump/2020/5/18/21262265/georgia-covid-19-cases-declining-reopening) wey dey mislead citizens about di trend of confirmed cases with di way dem arrange di x-axis. Dis one show misrepresentation through di way dem show di data. |
| **Illusion of free choice** | 2020 - Learning app [ABCmouse pay $10M to settle FTC complaint](https://www.washingtonpost.com/business/2020/09/04/abcmouse-10-million-ftc-settlement/) wey trap parents to dey pay for subscription wey dem no fit cancel. Dis one show dark patterns for di way dem design di choice system, wey dey push users to make bad choices. |
| **Data Privacy & User Rights** | 2021 - Facebook [Data Breach](https://www.npr.org/2021/04/09/986005820/after-data-breach-exposes-530-million-facebook-says-it-will-not-notify-users) expose data of 530M users, dem pay $5B settlement to FTC. But dem no gree tell users about di breach, wey dey against user rights for data transparency and access. |

You wan see more case studies? Check dis resources:
* [Ethics Unwrapped](https://ethicsunwrapped.utexas.edu/case-studies) - ethics wahala for different industries. 
* [Data Science Ethics course](https://www.coursera.org/learn/data-science-ethics#syllabus) - landmark case studies wey dem discuss.
* [Where things don go wrong](https://deon.drivendata.org/examples/) - deon checklist with examples

> 🚨 Think about di case studies wey you don see - you don experience or dem don affect you with similar ethical wahala for your life? You fit think of at least one other case study wey show one of di ethical wahala wey we don talk for dis section?

## Applied Ethics

We don talk about ethics concepts, wahala, and case studies for real life. But how we go start to _apply_ ethical principles and practices for our projects? And how we go _operationalize_ dis practices for better governance? Make we look some real-life solutions: 

### 1. Professional Codes

Professional Codes na one way wey organizations fit use to "encourage" members to support their ethical principles and mission statement. Codes na _moral guidelines_ for professional behavior, wey dey help employees or members make decisions wey match di organization principles. Di code go work well if members dey follow am by choice; but many organizations dey give reward and punishment to make members follow am.

Examples na:

* [Oxford Munich](http://www.code-of-ethics.org/code-of-conduct/) Code of Ethics
* [Data Science Association](http://datascienceassn.org/code-of-conduct.html) Code of Conduct (dem create am for 2013)
* [ACM Code of Ethics and Professional Conduct](https://www.acm.org/code-of-ethics) (since 1993)

> 🚨 You dey part of any professional engineering or data science organization? Check their site to see if dem get professional code of ethics. Wetin e talk about their ethical principles? How dem dey "encourage" members to follow di code?

### 2. Ethics Checklists

While professional codes dey show di _ethical behavior_ wey dem expect from practitioners, dem [get known limitations](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md) for enforcement, especially for big projects. Instead, many data science experts [dey support checklists](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md), wey fit **connect principles to practices** in ways wey dem fit track and use.

Checklists dey turn questions to "yes/no" tasks wey dem fit use for standard product release workflows. 

Examples na:
* [Deon](https://deon.drivendata.org/) - one general-purpose data ethics checklist wey dem create from [industry recommendations](https://deon.drivendata.org/#checklist-citations) with one command-line tool wey easy to use.
* [Privacy Audit Checklist](https://cyber.harvard.edu/ecommerce/privacyaudit.html) - e dey give general advice for how to handle information from legal and social exposure side.
* [AI Fairness Checklist](https://www.microsoft.com/en-us/research/project/ai-fairness-checklist/) - AI practitioners create am to help fairness checks for AI development cycles.
* [22 questions for ethics in data and AI](https://medium.com/the-organization/22-questions-for-ethics-in-data-and-ai-efb68fd19429) - e dey open-ended, structured to help explore ethical issues for design, implementation, and organizational contexts.

### 3. Ethics Regulations

Ethics na to define shared values and do di right thing _by choice_. **Compliance** na to _follow di law_ if e dey. **Governance** na di way organizations dey operate to enforce ethical principles and follow di law.

Today, governance dey two ways for organizations. First, na to define **ethical AI** principles and set practices to make sure dem dey use am for all AI-related projects for di organization. Second, na to follow all government-mandated **data protection regulations** for di places wey dem dey operate.

Examples of data protection and privacy regulations:

* `1974`, [US Privacy Act](https://www.justice.gov/opcl/privacy-act-1974) - e dey regulate _federal govt._ collection, use, and disclosure of personal information.
* `1996`, [US Health Insurance Portability & Accountability Act (HIPAA)](https://www.cdc.gov/phlp/publications/topic/hipaa.html) - e dey protect personal health data.
* `1998`, [US Children's Online Privacy Protection Act (COPPA)](https://www.ftc.gov/enforcement/rules/rulemaking-regulatory-reform-proceedings/childrens-online-privacy-protection-rule) - e dey protect data privacy of children wey dey under 13.
* `2018`, [General Data Protection Regulation (GDPR)](https://gdpr-info.eu/) - e dey give user rights, data protection, and privacy.
* `2018`, [California Consumer Privacy Act (CCPA)](https://www.oag.ca.gov/privacy/ccpa) - e dey give consumers more _rights_ over their (personal) data.
* `2021`, China's [Personal Information Protection Law](https://www.reuters.com/world/china/china-passes-new-personal-data-privacy-law-take-effect-nov-1-2021-08-20/) - e dey one of di strongest online data privacy regulations for di world.

> 🚨 Di European Union wey define GDPR (General Data Protection Regulation) na one of di most important data privacy regulations today. You sabi say e also define [8 user rights](https://www.freeprivacypolicy.com/blog/8-user-rights-gdpr) to protect citizens' digital privacy and personal data? Learn about wetin dem be and why dem matter.

### 4. Ethics Culture

Make you sabi say e get one gap between _compliance_ (to do wetin di law talk) and di way we dey address [big wahala](https://www.coursera.org/learn/data-science-ethics/home/week/4) (like ossification, information asymmetry, and distributional unfairness) wey fit make AI turn weapon fast. 

To fix dis one, e need [collaborative ways to define ethics cultures](https://towardsdatascience.com/why-ai-ethics-requires-a-culture-driven-approach-26f451afa29f) wey go build emotional connection and shared values _across organizations_ for di industry. Dis one dey call for more [formalized data ethics cultures](https://www.codeforamerica.org/news/formalizing-an-ethical-data-culture/) for organizations - e go allow _anybody_ to [pull di Andon cord](https://en.wikipedia.org/wiki/Andon_(manufacturing)) (to raise ethics wahala early for di process) and make _ethical assessments_ (like for hiring) one important criteria for team formation for AI projects.

---
## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ds/quiz/3) 🎯
## Review & Self Study 

Courses and books dey help to understand di main ethics concepts and wahala, while case studies and tools dey help for applied ethics practices for real life. Here be some resources to start with.
* [Machine Learning For Beginners](https://github.com/microsoft/ML-For-Beginners/blob/main/1-Introduction/3-fairness/README.md) - lesson wey dey talk about Fairness, from Microsoft.  
* [Principles of Responsible AI](https://docs.microsoft.com/en-us/learn/modules/responsible-ai-principles/) - free learning path from Microsoft Learn.  
* [Ethics and Data Science](https://resources.oreilly.com/examples/0636920203964) - O'Reilly EBook (M. Loukides, H. Mason et. al)  
* [Data Science Ethics](https://www.coursera.org/learn/data-science-ethics#syllabus) - online course from University of Michigan.  
* [Ethics Unwrapped](https://ethicsunwrapped.utexas.edu/case-studies) - case studies from University of Texas.  

# Assignment  

[Write A Data Ethics Case Study](assignment.md)  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI translet service [Co-op Translator](https://github.com/Azure/co-op-translator) do di translet. Even as we dey try make am correct, abeg make you sabi say machine translet fit get mistake or no dey accurate well. Di original dokyument for im native language na di one wey you go take as di correct source. For important mata, e good make professional human translet am. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translet.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->