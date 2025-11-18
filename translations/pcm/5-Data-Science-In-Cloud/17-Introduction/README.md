<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f8e7cdefa096664ae86f795be571580",
  "translation_date": "2025-11-18T18:27:09+00:00",
  "source_file": "5-Data-Science-In-Cloud/17-Introduction/README.md",
  "language_code": "pcm"
}
-->
# Introduction to Data Science for Cloud

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/17-DataScience-Cloud.png)|
|:---:|
| Data Science for Cloud: Introduction - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

For dis lesson, you go learn di basic principles of Cloud, den you go see why e fit make sense for you to use Cloud services to run your data science projects. We go also look some examples of data science projects wey dem dey run for Cloud. 

## [Pre-Lecture Quiz](https://ff-quizzes.netlify.app/en/ds/quiz/32)

## Wetin be Cloud?

Cloud, or Cloud Computing, na di way wey dem dey deliver plenty pay-as-you-go computing services wey dem dey host for internet infrastructure. Di services fit include storage, databases, networking, software, analytics, and intelligent services. 

We dey usually divide Cloud into three types: Public, Private, and Hybrid clouds:

* Public cloud: Public cloud na di one wey third-party cloud service provider dey own and operate, and dem dey deliver di computing resources through internet to di public. 
* Private cloud: Dis one na cloud computing resources wey only one business or organization dey use, and di services plus infrastructure dey for private network. 
* Hybrid cloud: Hybrid cloud na system wey join public and private clouds together. Users fit use on-premises datacenter, but still allow data and applications to run for one or more public clouds. 

Most cloud computing services dey fall under three categories: Infrastructure as a Service (IaaS), Platform as a Service (PaaS), and Software as a Service (SaaS).

* Infrastructure as a Service (IaaS): Users dey rent IT infrastructure like servers, virtual machines (VMs), storage, networks, operating systems. 
* Platform as a Service (PaaS): Users dey rent environment for developing, testing, delivering, and managing software applications. Dem no need worry about di infrastructure like servers, storage, network, and databases. 
* Software as a Service (SaaS): Users dey get access to software applications through internet, on demand, and usually on subscription basis. Dem no need worry about hosting or managing di software application, di infrastructure, or maintenance like software upgrades and security patching. 

Some of di biggest Cloud providers na Amazon Web Services, Google Cloud Platform, and Microsoft Azure.

## Why You Go Choose Cloud for Data Science?

Developers and IT professionals dey choose Cloud for plenty reasons, like:

* Innovation: You fit power your apps by adding innovative services wey Cloud providers don already create. 
* Flexibility: You go only pay for di services wey you need, and you fit choose from plenty options. You dey pay as you go and fit adjust di services as your needs dey change. 
* Budget: You no need to buy hardware and software or set up on-site datacenters. You go just pay for wetin you use. 
* Scalability: Your resources fit grow or reduce based on wetin your project need. Your apps fit use more or less computing power, storage, and bandwidth anytime. 
* Productivity: You fit focus on your business instead of spending time dey manage datacenters. 
* Reliability: Cloud Computing dey offer ways to back up your data and set up disaster recovery plans to keep your business dey go even for bad times. 
* Security: You fit enjoy policies, technologies, and controls wey go make your project secure. 

Dis na some of di common reasons why people dey use Cloud services. Now wey we don sabi wetin Cloud be and di benefits, make we look how Data scientists and developers wey dey work with data fit use Cloud to solve some challenges:

* Storing large amounts of data: Instead of buying and managing big servers, you fit store your data for Cloud with solutions like Azure Cosmos DB, Azure SQL Database, and Azure Data Lake Storage.
* Performing Data Integration: Data integration dey important for Data Science. E dey help you move from data collection to taking action. With Cloud services like Data Factory, you fit collect, transform, and integrate data from different sources into one data warehouse. 
* Processing data: To process plenty data, you need strong computing power. If you no get di machines, you fit use di Cloud’s big computing power to run and deploy your solutions. 
* Using data analytics services: Cloud services like Azure Synapse Analytics, Azure Stream Analytics, and Azure Databricks fit help you turn your data into useful insights. 
* Using Machine Learning and data intelligence services: Instead of starting from scratch, you fit use machine learning algorithms wey di Cloud provider don already create, like AzureML. You fit also use cognitive services like speech-to-text, text-to-speech, computer vision, and more.

## Examples of Data Science for Cloud

Make we look some examples to understand am better.

### Real-time social media sentiment analysis
We go start with one common example for machine learning: real-time social media sentiment analysis.

Imagine say you dey run one news media website and you wan use live data to know wetin your readers go like. You fit build program wey go analyze Twitter data in real-time to know di topics wey dey interest your readers. 

Di key things you go check na di number of tweets on specific topics (hashtags) and di sentiment, wey analytics tools go help you analyze. 

Steps to create dis project:

* Create event hub to collect Twitter data
* Set up and start Twitter client app to call Twitter Streaming APIs
* Create Stream Analytics job
* Set job input and query
* Create output sink and set job output
* Start di job

To see di full process, check di [documentation](https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?WT.mc_id=academic-77958-bethanycheum&ocid=AID30411099).

### Scientific papers analysis
Another example na project wey [Dmitry Soshnikov](http://soshnikov.com) create.

Dmitry build tool wey dey analyze COVID papers. Dis tool dey help researchers extract knowledge from scientific papers, gain insights, and navigate large collections of papers easily.

Steps for di project:

* Extract and pre-process info with [Text Analytics for Health](https://docs.microsoft.com/azure/cognitive-services/text-analytics/how-tos/text-analytics-for-health?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109)
* Use [Azure ML](https://azure.microsoft.com/services/machine-learning?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) to process data faster
* Store and query info with [Cosmos DB](https://azure.microsoft.com/services/cosmos-db?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109)
* Create interactive dashboard for data exploration and visualization with Power BI

To see di full process, visit [Dmitry’s blog](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/).

As you see, Cloud services fit help us do plenty things for Data Science.

## Footnote

Sources:
* https://azure.microsoft.com/overview/what-is-cloud-computing?ocid=AID3041109  
* https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?ocid=AID3041109  
* https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/  

## Post-Lecture Quiz

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ds/quiz/33)

## Assignment

[Market Research](assignment.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis document don use AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) take translate am. Even though we dey try make e accurate, abeg sabi say automated translations fit get mistake or no correct well. Di original document for di native language na di main correct source. For important information, e better make una use professional human translation. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->