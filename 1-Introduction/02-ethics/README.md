# Data Ethics

## Pre-Lecture Quiz 🎯

[Pre-lecture quiz]() 

## Sketchnote 🖼

> A Visual Guide to Data Ethics by [Nitya Narasimhan](https://twitter.com/nitya) / [(@sketchthedocs)](https://sketchthedocs.dev)


## 1. Introduction

This lesson will look at the field of _data ethics_ - from core concepts (ethical challenges & societal consequences) to applied ethics (ethical principles, practices and culture). Let's start with the basics: definitions and motivations.

### 1.1 Definitions

**Ethics** [comes from the Greek word "ethikos" and its root "ethos"](https://en.wikipedia.org/wiki/Ethics). It refers to the set of _shared values and moral principles_ that govern our behavior in society and is based on widely-accepted ideas of _right vs. wrong_. Ethics are not laws! They can't be legally enforced but they can influence corporate initiatives and government regulations that help with compliance and governance.

**Data Ethics** is [defined as a new branch of ethics](https://royalsocietypublishing.org/doi/full/10.1098/rsta.2016.0360#sec-1) that "studies and evaluates moral problems related to _data, algorithms and corresponding practices_ .. to formulate and support morally good solutions" where:
 * `data` = generation, recording, curation, dissemination, sharing and usage
 * `algorithms` = AI, machine learning, bots
 * `practices` = responsible innovation, ethical hacking, codes of conduct

**Applied Ethics** is the [_practical application of moral considerations_](https://en.wikipedia.org/wiki/Applied_ethics). If focuses on understanding how ethical issues impact real-world actions, products and processes, by asking moral questions - like _"is this fair?"_ and _"how can this harm individuals or society as a whole?"_ when working with big data and AI algorithms. Applied ethics practices can then focus on taking corrective measures - like employing checklists (_"did we test data model accruacy with diverse groups, for fairness?"_) - to minimize or prevent any unintended consequences.

**Ethics Culture**: Applied ethics focuses on identifying moral questions and adopting ethically-motivated actions with respect to real-world scenarios and projects. Ethics culture is about _operationalizing_ these practices, collaboratively and at scale, to ensure governances at the scale of organizations and industries. [Establishing an ethics culture](https://hbr.org/2019/05/how-to-design-an-ethical-organization) requires identifying and addressing _systemic_ issues (historical or ingrained) and creating norms & incentives htat keep members accountable for adherence to ethical principles.


### 1.2 Motivation

Let's look at some emerging trends in big data and AI:

 * [By 2022](https://www.gartner.com/smarterwithgartner/gartner-top-10-trends-in-data-and-analytics-for-2020/) one-in-three large organizations will buy and sell data via online Marketplaces and Exchanges.
 * [By 2025](https://www.statista.com/statistics/871513/worldwide-data-created/) we'll be creating and consuming over 180 zettabytes of data.

**Data scientists** will have unimaginable levels of access to personal and behavioral data, helping them develop the algorithms to fuel an AI-driven economy. This raises data ethics issues around _protection of data privacy_ with implications for individual rights around personal data collection and usage.

**App developers** will find it easier and cheaper to integrate AI into everday consumer experiences, thanks to the economies of scale and efficiencies of distribution in centralized exchanges. This raises ethical issues around the [_weaponization of AI_](https://www.youtube.com/watch?v=TQHs8SA1qpk) with implications for societal harms caused by unfairness, misrepresentation and systemic biases.

**Democratization and Industrialization of AI** are seen as the two megatrends in Gartner's 2020 [Hype Cycle for AI](https://www.gartner.com/smarterwithgartner/2-megatrends-dominate-the-gartner-hype-cycle-for-artificial-intelligence-2020/), shown below. The first positions developers to be a major force in driving increased AI adoption, while the second makes responsible AI and governance a priority for industries. 


![](https://images-cdn.newscred.com/Zz1mOWJhNzlkNDA2ZTMxMWViYjRiOGFiM2IyMjQ1YmMwZQ==)

Data ethics are now **necessary guardrails** ensuring developers ask the right moral questions and adopt the right practices (to uphold ethical values). And they influence the regulations and frameworks defined (for governance) by governments and organizations.


## 2. Core Concepts

A data ethics culture requires an understanding of three things: the _shared values_ we embrace as a society, the _moral questions_ we ask (to ensure adherence to those values), and the potential _harms & consequences_ (of non-adherence).

### 2.1 Ethical AI Values

Our shared values reflect our ideas of wrong-vs-right when it comes to big data and AI. Different organizations have their own views of what responsible AI and ethical AI principles look like. 

Here is an example - the [Responsible AI Framework](https://docs.microsoft.com/en-gb/azure/cognitive-services/personalizer/media/ethics-and-responsible-use/ai-values-future-computed.png) from Microsoft defines 6 core ethics principles for all products and processes to follow, when implementing AI solutions:

 * **Accountability**: ensure AI designers & developers take _responsibility_ for its operation.
 * **Transparency**: make AI operations and decisions _understandable_ to users.
 * **Fairness**: understand biases and ensure AI _behaves comparably_ across target groups.
 * **Reliability & Safety**: make sure AI behaves consistently, and _without malicious intent_.
 * **Security & Privacy**: get _informed consent_ for data collection, provide data privacy controls.
 * **Inclusiveness**: adapt AI behaviors to _broad range of human needs_ and capabilities.

![Elements of an Responsible AI Framework at Microsoft](https://docs.microsoft.com/en-gb/azure/cognitive-services/personalizer/media/ethics-and-responsible-use/ai-values-future-computed.png)

Note that accountability and transparency are _cross-cutting_ concerns that are foundational to the top 4 values, and can be explored in their contexts. In the next section we'll look at the ethical challenges (moral questions) raised in two core contexts:

 * Data Privacy - focused on **personal data** collection & use, with consequences to individuals.
 * Fairness - focused on **algorithm** design & use, with consequences to society at large.

### 2.2 Ethics of Personal Data

[Personal data](https://en.wikipedia.org/wiki/Personal_data) or personally-identifiable information (PII) is _any data that relates to an identified or identifiable living individual_. It can also [extend to diverse pieces of non-personal data](https://ec.europa.eu/info/law/law-topic/data-protection/reform/what-personal-data_en) that collectively can lead to the identification of a specific individual. Examples include: participant data from research studies, social media interactions, mobile & web app data, online commerce transactions and more.

Here are _some_ ethical concepts and moral questions to explore in context:

* **Data Ownership**. Who owns the data - user or organization? How does this impact users' rights?
* **Informed Consent**. Did users give permissions for data capture? Did they understand purpose?
* **Intellectual Property**. Does data have economic value? What are the users' rights & controls?
* **Data Privacy**. Is data secured from hacks/leaks? Is anonymity preserved on data use or sharing?
* **Right to be Forgotten**. Can user request their data be deleted or removed to reclaim privacy?

### 2.3 Ethics of Algorithms

Algorithm design begins with collecting & curating datasets relevant to a specific AI problem or domain, then processing & analyzing it to create models that can help predict outcomes or automate decisions in real-world applications. Moral questions can now arise in various contexts, at any one of these stages.

Here are _some_ ethical concepts and moral questions to explore in context:

* **Dataset Bias** - Is data representative of target audience? Have we checked for different [data biases](https://towardsdatascience.com/survey-d4f168791e57)?
* **Data Quality** - Does dataset and feature selection provide the required [data quality assurance](https://lakefs.io/data-quality-testing/)?
* **Algorithm Fairness** - Does the data model [systematically discriminate](https://towardsdatascience.com/what-is-algorithm-fairness-3182e161cf9f) against some subgroups?
* **Misrepresentation** - Are we [communicating honestly reported data in a deceptive manner?](https://www.sciencedirect.com/topics/computer-science/misrepresentation)
* **Explainable AI** - Are the results of AI [understandable by humans](https://en.wikipedia.org/wiki/Explainable_artificial_intelligence)? White-box (vs. black-box) models.
* **Free Choice** - Did user exercise free will or did algorithm nudge them towards a desired outcome?

### 2.3 Case Studies

The above are a subset of the core ethical challenges posed for big data and AI. More organizations are defining and adopting _responsible AI_ or _ethical AI_ frameworks that may identify additional shared values and related ethical challenges for specific domains or needs. 

To understand the potential _harms and consequences_ of neglecting or violating these data ethics principles, it helps to explore this in a real-world context. Here are some famous case studies and recent examples to get you started:


* `1972`: The [Tuskegee Syphillis Study](https://en.wikipedia.org/wiki/Tuskegee_Syphilis_Study) is a landmark case study for **informed consent** in data science. African American men who participated in the study were promised free medical care _but deceived_ by researchers who failed to inform subjects of their diagnosis or about availability of treatment. Many subjects died; some partners or children were affected by complications. The study lasted 40 years.
* `2007`: The Netflix data prize provided researchers with [_10M anonymized movie rankings from 50K customers_](https://www.wired.com/2007/12/why-anonymous-data-sometimes-isnt/) to help improve recommendation algorithms. This became a landmark case study in **de-identification (data privacy)** where researchers were able to correlate the anonymized data with _other datasets_ (e.g., IMDb) that had personally identifiable information - helping them "de-anonymize" users.
* `2013`: The City of Boston [developed Street Bump](https://www.boston.gov/transportation/street-bump), an app that let citizens report potholes, giving the city better roadway data to find and fix issues. This became a case study for **collection bias** where [people in lower income groups had less access to cars and phones](https://hbr.org/2013/04/the-hidden-biases-in-big-data), making their roadway issues invisible in this app. Developers worked with academics to _equitable access and digital divides_ issues for fairness.
* `2018`: The MIT [Gender Shades Study](http://gendershades.org/overview.html) evaluated the accuracy of gender classification AI products, exposing gaps in accuracy for women and persons of color. A [2019 Apple Card](https://www.wired.com/story/the-apple-card-didnt-see-genderand-thats-the-problem/) seemed to offer less credit to women than men. Both these illustrated issues in **algorithmic fairness** and discrimination.
* `2020`: The [Georgia Department of Public Health released COVID-19 charts](https://www.vox.com/covid-19-coronavirus-us-response-trump/2020/5/18/21262265/georgia-covid-19-cases-declining-reopening) that appeared to mislead citizens about trends in confirmed cases with non-chronological ordering on the x-axis. This illustrates **data misrepresentation** where honest data is presented dishonestly to support a desired narrative.
* `2020`: Learning app [ABCmouse paid $10M to settle an FTC complaint](https://www.washingtonpost.com/business/2020/09/04/abcmouse-10-million-ftc-settlement/) where parents were trapped into paying for subscriptions they couldn't cancel. This highlights the **illusion of free choice** in algorithmic decision-making, and potential harms from dark patterns that exploit user insights.
* `2021`: Facebook [Data Breach](https://www.npr.org/2021/04/09/986005820/after-data-breach-exposes-530-million-facebook-says-it-will-not-notify-users) exposed data from 530M users, resulting in a $5B settlement to the FTC. It however refused to notify users of the breach - raising issues like **data privacy**, **data security** and **accountability**, including user rights to redress for those affected.

Want to explore more case studies on your own? Check out these resources:

 * [Ethics Unwrapped](https://ethicsunwrapped.utexas.edu/case-studies) - ethics dilemmas across diverse industries. 
 * [Data Science Ethics course](https://www.coursera.org/learn/data-science-ethics#syllabus) - landmark case studies in data ethics.
 * [Where things have gone wrong](https://deon.drivendata.org/examples/) - deon checklist examples of ethical issues

## 3. Applied Ethics

We've learned about data ethics values, and the ethical challenges (+ moral questions) associated with adherence to these values. But how do we _implement_ these ideas in real-world contexts? Here are some tools & practices that can help.

### 3.1 Have Professional Codes

Professional codes are _moral guidelines_ for professional behavior, helping employees or members _make decisions that align with organizational principles_. Codes may not be legally enforceable, making them only as good as the willing compliance of members. An organization may inspire adherence by imposing incentives & penalties accordingly.

Professional _codes of conduct_ are prescriptive rules and responsibilities that members must follow to remain in good standing with an organization. A professional *code of ethics* is more [_aspirational_](https://keydifferences.com/difference-between-code-of-ethics-and-code-of-conduct.html), defining the shared values and ideas of the organization. The terms are sometimes used interchangeably.

Examples include:

 * [Oxford Munich](http://www.code-of-ethics.org/code-of-conduct/) Code of Ethics
 * [Data Science Association](http://datascienceassn.org/code-of-conduct.html) Code of Conduct (created 2013)
 * [ACM Code of Ethics and Professional Conduct](https://www.acm.org/code-of-ethics) (since 1993)


### 3.2 Ask Moral Questions

Assuming you've already identified your shared values or ethical principles at a team or organization level, the next step is to identify the moral questions relevant to your specific use case and operational workflow.

Here are [6 basic questions about data ethics](https://halpert3.medium.com/six-questions-about-data-science-ethics-252b5ae31fec) that you can build on:

* Is the data you're collecting fair and unbiased?
* Is the data being used ethically and fairly?
* Is user privacy being protected?
* To whom does data belong - the company or the user?
* What effects do the data and algorithms have on society (individual and collective)?
* Is the data manipulated or deceptive?

For larger team or project scope, you can choose to expand on questions that reflect a specific stage of the workflow. For example here are [22 questions on ethics in data and AI](https://medium.com/the-organization/22-questions-for-ethics-in-data-and-ai-efb68fd19429) that were grouped into _design_, _implementation & management_, _systems & organization_ categories for convenience.

### 3.3 Adopt Ethics Checklists

While professional codes define required _ethical behavior_ from practitioners, they [have known limitations](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md) for implementation, particularly in large-scale projects. In [Ethics and Data Science](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md)), experts instead advocate for ethics checklists that can **connect principles to practices** in more deterministic and actionable ways.

Checklists convert questions into "yes/no" tasks that can be tracked and validated before product release. Tools like [deon](https://deon.drivendata.org/) make this frictionless, creating default checklists aligned to [industry recommendations](https://deon.drivendata.org/#checklist-citations) and enabling users to customize and integrate them into workflows using a command-line tool. Deon also provides [real-world examples](ttps://deon.drivendata.org/examples/) of ethical challenges to provide context for these decisions.

### 3.4 Track Ethics Compliance

**Ethics** is about doing the right thing, even if there are no laws to enforce it. **Compliance** is about following the law, when defined and where applicable.
**Governance** is the broader umbrella that covers all the ways in which an organization (company or government) operates to enforce ethical principles & comply with laws.

Companies are creating their own ethics frameworks (e.g., [Microsoft](https://www.microsoft.com/en-us/ai/responsible-ai), [IBM](https://www.ibm.com/cloud/learn/ai-ethics), [Google](https://ai.google/principles), [Facebook](https://ai.facebook.com/blog/facebooks-five-pillars-of-responsible-ai/), [Accenture](https://www.accenture.com/_acnmedia/PDF-149/Accenture-Responsible-AI-Final.pdf#zoom=50)) for governances, while state and national governments tend to focus on regulations that protect the data privacy and rights of their citizens. 

Here are some landmark data privacy regulations to know:
 * `1974`, [US Privacy Act](https://www.justice.gov/opcl/privacy-act-1974) - regulates _federal govt._ collection, use and disclosure of personal information.
 * `1996`, [US Health Insurance Portability & Accountability Act (HIPAA)](https://www.cdc.gov/phlp/publications/topic/hipaa.html) - protects personal health data.
 * `1998`, [US Children's Online Privacy Protection Act (COPPA)](https://www.ftc.gov/enforcement/rules/rulemaking-regulatory-reform-proceedings/childrens-online-privacy-protection-rule) - protects data privacy of children under 13.
 * `2018`, [General Data Protection Regulation (GDPR)](https://gdpr-info.eu/) - provides user rights, data protection and privacy.
 * `2018`, [California Consumer Privacy Act (CCPA)](https://www.oag.ca.gov/privacy/ccpa) gives consumers more _rights_ over their personal data.

In Aug 2021, China passed the [Personal Information Protection Law](https://www.reuters.com/world/china/china-passes-new-personal-data-privacy-law-take-effect-nov-1-2021-08-20/) (to go into effect Nov 1) which, with its Data Security Law, will create one of the strongest online data privacy regulations in the world.


### 3.5 Establish Ethics Culture

There remains an intangible gap between compliance ("doing enough to meet the letter of the law") and addressing systemic issues ([like ossification, information asymmetry and distributional unfairness](https://www.coursera.org/learn/data-science-ethics/home/week/4)) that can create self-fulfilling feedback loops to weaponizes AI further. This is motivating calls for [formalizing data ethics cultures](https://www.codeforamerica.org/news/formalizing-an-ethical-data-culture/) in organizations, where everyone is empowered to [pull the Andon cord](https://en.wikipedia.org/wiki/Andon_(manufacturing) to raise ethics concerns early. And exploring [collaborative approaches to defining this culture](https://towardsdatascience.com/why-ai-ethics-requires-a-culture-driven-approach-26f451afa29f) that build emotional connections and consistent beliefs across organizations and industries.

---

## Challenge 🚀 


## Post-Lecture Quiz 🎯

[Post-lecture quiz]() 


## Review & Self Study 


---
# Assignment 

[Assignment Title](assignment.md)

---

# Resources

[Related Resources](resources.md)