
## 1. Ethics Fundamentals
[Back To Introduction](README.md#introduction)

### 1.1 What is Ethics?

The term "ethics" [comes from](https://en.wikipedia.org/wiki/Ethics) the Greek term "ethikos" - and its root "ethos", meaning _character or moral nature_. Think of ethics as the set of **shared values** or **moral principles** that govern our behavior in society. Our code of ethics is based on widely accepted ideas on what is _right vs. wrong_, creating informal rules (or "norms") that we follow voluntarily to ensure the good of the community.

Ethics is critical for scientific research and technology advancement. The [Research Ethics timeline](https://www.niehs.nih.gov/research/resources/bioethics/timeline/index.cfm) gives examples from the past four centuries - including Charles Babbage's 1830 [Reflections on the Decline of Science in England ..](https://books.google.com/books/about/Reflections_on_the_Decline_of_Science_in.html) where he discusses dishonesty in data science approaches including fabrication of data to support desired outcomes. Ethics became _guardrails_ to prevent data misuse and protect society from unintended consequences or harms.

_Applied Ethics_ is about the practical adoption of ethical principles and practices when developing new processes or products. It's about asking moral questions ("is this right or wrong?"), evaluating tradeoffs ("does this help or harm society more?") and taking informed actions to ensure compliance at individual and organizational levels. Ethics are *not* laws. But they can influence the creation of legal or social frameworks that support governance such as:

 *  **Professional codes of conduct.** | For users or groups e.g., The [Hippocratic Oath](https://en.wikipedia.org/wiki/Hippocratic_Oath) (460-370 BC) for medical ethics defined principles like data confidentiality (led to _doctor-patient privilege_ laws) and non-maleficence (popularly known as _first, do no harm_) that are still adopted today. 
 * **Regulatory standards** | For organizations or industries e.g., The [1996 Health Insurance Portability and Accountability Act](https://en.wikipedia.org/wiki/Health_Insurance_Portability_and_Accountability_Act) (HIPAA) mandated theft and fraud protections for _personally identifiable information_ (PII) collected by the healthcare industry - and stipulated how that data could be used or disclosed.

### 1.2 What is Data Ethics?

Data ethics is the application of ethics considerations to the domain of big data and data-driven algorithms.

 * [Wikipedia](https://en.wikipedia.org/wiki/Big_data_ethics) defines big data ethics as _systemizing, defending, and recommending, concepts of right and wrong conduct in relation to data_ - focusing on implications for **personal data**.
 * A [Royal Society article](https://royalsocietypublishing.org/doi/full/10.1098/rsta.2016.0360#sec-1) defines data ethics as a new branch of ethics that _studies and evaluates moral problems related to **data, algorithms and corresponding practices** .. to formulate and support morally good solutions (right conduct or values)_.

The first definition puts it in perspective of users ("personal data") while the second puts it in perspective of operations ("data, algorithms, practices") where:

* `data` = generation, recording, curation, dissemination, sharing & usage 
* `algorithms` = AI, agents, machine learning, bots 
* `practices` = responsible innovation, ethical hacking, codes of conduct

Based on this, we can define data ethics as the study and evaluation of _moral questions_ related to data collection, algorithm development, and industry-wide models for governance. We'll explore these questions in the "how" section, but first let's talk about the "why".

### 1.3 Why Data Ethics?

To answer this question, let's look at recent trends in the big data and AI industries:
 
 * [_Statista_](https://www.statista.com/statistics/871513/worldwide-data-created/) - By 2025, we will be creating and consuming over **180 zettabytes of data**. 
 * _[Gartner](https://www.gartner.com/smarterwithgartner/gartner-top-10-trends-in-data-and-analytics-for-2020/)_ - By 2022, 35% of large orgs will buy & sell data in **online Marketplaces and Exchanges**
 * _[Gartner](https://www.gartner.com/smarterwithgartner/2-megatrends-dominate-the-gartner-hype-cycle-for-artificial-intelligence-2020/)_ - AI **democratization and industrialization** are the new Hype Cycle megatrends.

The first trend tells us that _data scientists_ will have unprecedented levels of access to personal data at global scale, building algorithms to fuel an AI-driven economy. The second trend tells us that economies of scale and efficiencies in distribution will make it easier and cheaper for _developers_ to integrate AI into more everyday consumer experiences.

The potential for harm occurs when algorithms and AI get _weaponized_ against society in unforeseen ways. In [Weapons of Math Destruction](https://www.youtube.com/watch?v=TQHs8SA1qpk) author Cathy O'Neil talks about the three elements of AI algorithms that pose a danger to society: _opacity_, _scale_ and _damage_.

 * **Opacity** refers to the black box nature of many algorithms - do we understand why a specific decision was made, and can we _explain or interpret_ the data reasoning that drove the predictions behind it?
 * **Scale** refers to the speed with which algorithms can be deployed and replicated - how quickly can a minor algorithm design flaw get "baked in" with use, leading to irreversible societal harms to affected users?
 * **Damage** refers to the social and economic impact of poor algorithmic decision-making - how can bad or unrepresentative data lead to unfair algorithms that disproportionately harm specific user groups?

So why does data ethics matter? Because democratization of AI can speed up weaponization, creating harms at scale in the absence of ethical guardrails. While industrialization of AI will motivate better governance - giving data ethics an important role in shaping policies and standards for developing responsible AI solutions.


### 1.4 How To Apply Ethics?

We know what data ethics is, and why it matters. But how do we _apply_ ethical principles or practices as data scientists or developers? It starts with us asking the right questions at every step of our data-driven pipelines and processes. These [Six questions about data science ethics](https://halpert3.medium.com/six-questions-about-data-science-ethics-252b5ae31fec) are a good starting point:

 1. Is the data fair and unbiased?
 2. Is the data being used fairly and ethically?
 3. Is (user) privacy being protected?
 4. To whom does data belong, company or user?
 5. What effects do data and algorithms have on society?
 6. Is the data manipulated or deceiving?

The [22 questions for ethics in data and AI](https://medium.com/the-organization/22-questions-for-ethics-in-data-and-ai-efb68fd19429) article expands this into a framework, grouping questions by stage of processing: _design_, _implementation & management_, _systems & organization_. The [O'Reilly Ethics and Data Science](https://resources.oreilly.com/examples/0636920203964/) book advocates strongly for _checklists_, asking simple  `have we done this? (y/n)` questions that improve ethics oversight without the overheads caused by analysis paralysis.

And tools like [deon](https://deon.drivendata.org/)
make it frictionless to integrate [ethics checklists](https://deon.drivendata.org/#data-science-ethics-checklist) into your project workflows. Deon builds on [industry practices](https://deon.drivendata.org/#checklist-citations), shares [real-world examples](https://deon.drivendata.org/examples/) that put the ethical challenges in context, and allows practitioners to derive custom checklists from the defaults, to suit specific scenarios or industries.

### 1.5 Ethics Concepts

Ethics checklists often revolve around yes/no questions related to core ethics concepts and challenges. Let's look at _a subset_ of these issues - inspired in part by the [deon ethics checklist](https://deon.drivendata.org/#data-science-ethics-checklist) - in two contexts: data (collection and storage) and algorithms (analysis and modeling).

**Data Collection & Storage**
 * _Ownership_: Does the user own the data? Or the organization? Is there an agreement that defines this?
 * _Informed Consent_: Did human subjects give permission for data capture & understand purpose/usage?
 * _Collection Bias_: Is data representative of audience? Did we identify and mitigate biases?
 * _Data Security_: Is data stored and transmitted securely? Are valid access controls enforced?
 * _Data Privacy_: Does data contain personally identifiable information? Is anonymity preserved?
 * _Right to be Forgotten_: Does user have mechanism to request deletion of their personal information?

**Data Modeling & Analysis**

 * _Data Validity_: Does data capture relevant features? Is it timeless? Is the data model valid?
 * _Misrepresentation_: Does analysis communicate honestly reported data in a deceptive manner?
 * _Auditability_: Is the data analysis or algorithm design documented well enough to be reproducible later?
 * _Explainability_: Can we explain why the data model or learning algorithm made a specific decision?
 * _Fairness_: Is the model fair (e.g., shows similar accuracy) across diverse groups of affected users?

Finally, let's talk about two abstract concepts that often underlie users' ethics concerns around technology:

 * **Trust**: Can we trust an organization with our personal data? Can we trust that algorithmic decisions are fair and do no harm? Can we trust that information is not misrepresented?
 * **Choice**: Do I have free will when I make a choice in a consumer UI/UX? Are data-driven [choice architectures](https://en.wikipedia.org/wiki/Choice_architecture) nudging me towards good choices or are [dark patterns](https://www.darkpatterns.org/) working against my self-interest?


### 1.6 Ethics History

Knowing ethics concepts is one thing - understanding the intent behind them, and the potential harms or societal consequences they bring, is another. Let's look at some case studies that help frame ethics discussions in a more concrete way with real-world examples. 

| Historical Example | Ethics Issues |
|---|---|
| _[Facebook Data Breach](https://www.npr.org/2021/04/09/986005820/after-data-breach-exposes-530-million-facebook-says-it-will-not-notify-users)_ exposes data for 530M users. Facebook pays $5B to FTC, does not notify users. | Data Privacy, Data Security, Transparency, Accountability |
| [Tuskegee Syphillis Study](https://en.wikipedia.org/wiki/Tuskegee_syphilis_experiment) - African-American men were enrolled in study without being told its true purpose. Treatments were withheld. | Informed Consent, Fairness, Social / Economic Harms |
| [MIT Gender Shades Study](http://gendershades.org/index.html) - evaluated accuracy of industry AI gender classification models (used by law enforcement), detected bias | Fairness, Social/ Economic Harms, Collection Bias |
| [Learning app ABCmouse pays $10 million to settle FTC complaint it trapped parents in subscription they couldn’t cancel](https://www.washingtonpost.com/business/2020/09/04/abcmouse-10-million-ftc-settlement/) - user experience masked context, nudged user towards choices with financial harms| Misrepresentation, Free Choice, Dark Patterns, Economic Harms |
| [Netflix Prize Dataset de-anonymized by correlation](https://www.wired.com/2007/12/why-anonymous-data-sometimes-isnt/) - showed how Netflix prize dataset of 500M users was easily de-anonymized by cross-correlation with public IMDb comments (and other such datasets) | Data Privacy, Anonymity, De-identification |
| [Georgia COVID-19 cases not declining as quickly as data suggested](https://www.vox.com/covid-19-coronavirus-us-response-trump/2020/5/18/21262265/georgia-covid-19-cases-declining-reopening) - graphs released had x-axis not ordered chronologically, misleading viewers| Misrepresentation, Social Harms |

We covered just a subset of examples, but recommend you explore these resources for more:

 * [Ethics Unwrapped](https://ethicsunwrapped.utexas.edu/case-studies) - ethics dilemmas across diverse industries. 
 * [Data Science Ethics course](https://www.coursera.org/learn/data-science-ethics#syllabus) - landmark case studies in data ethics.
 * [Where things have gone wrong](https://deon.drivendata.org/examples/) - deon checklist examples of ethical issues
