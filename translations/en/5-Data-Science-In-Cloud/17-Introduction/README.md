<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "408c55cab2880daa4e78616308bd5db7",
  "translation_date": "2025-08-31T10:56:02+00:00",
  "source_file": "5-Data-Science-In-Cloud/17-Introduction/README.md",
  "language_code": "en"
}
-->
# Introduction to Data Science in the Cloud

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/17-DataScience-Cloud.png)|
|:---:|
| Data Science In The Cloud: Introduction - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

In this lesson, you will learn the basic principles of the Cloud, understand why using Cloud services can be beneficial for your data science projects, and explore examples of data science projects implemented in the Cloud.

## [Pre-Lecture Quiz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/32)

## What is the Cloud?

The Cloud, or Cloud Computing, refers to the delivery of a variety of pay-as-you-go computing services hosted on infrastructure over the internet. These services include storage, databases, networking, software, analytics, and intelligent services.

We typically distinguish between Public, Private, and Hybrid clouds as follows:

* Public cloud: A public cloud is owned and operated by a third-party cloud service provider that delivers its computing resources over the Internet to the public.
* Private cloud: Refers to cloud computing resources used exclusively by a single business or organization, with services and infrastructure maintained on a private network.
* Hybrid cloud: A hybrid cloud combines public and private clouds. Users can maintain an on-premises datacenter while running data and applications on one or more public clouds.

Most cloud computing services fall into three main categories: Infrastructure as a Service (IaaS), Platform as a Service (PaaS), and Software as a Service (SaaS).

* Infrastructure as a Service (IaaS): Users rent IT infrastructure such as servers, virtual machines (VMs), storage, networks, and operating systems.
* Platform as a Service (PaaS): Users rent an environment for developing, testing, delivering, and managing software applications without worrying about the underlying infrastructure.
* Software as a Service (SaaS): Users access software applications over the Internet, typically on a subscription basis, without managing hosting, infrastructure, or maintenance tasks like updates and security patches.

Some of the largest Cloud providers include Amazon Web Services, Google Cloud Platform, and Microsoft Azure.

## Why Choose the Cloud for Data Science?

Developers and IT professionals choose to work with the Cloud for several reasons, including:

* Innovation: Integrate innovative services provided by Cloud providers directly into your applications.
* Flexibility: Pay only for the services you need, with a wide range of options. You can adapt services as your needs evolve.
* Budget: Avoid upfront investments in hardware and software, and pay only for what you use.
* Scalability: Scale resources up or down based on project needs, allowing applications to adjust computing power, storage, and bandwidth dynamically.
* Productivity: Focus on your business instead of managing datacenters and other infrastructure tasks.
* Reliability: Benefit from continuous data backups and disaster recovery plans to ensure business continuity during crises.
* Security: Leverage policies, technologies, and controls to enhance the security of your projects.

These are some of the most common reasons for using Cloud services. Now that we understand what the Cloud is and its benefits, let’s explore how it can help data scientists and developers address challenges such as:

* Storing large amounts of data: Instead of managing large servers, store data in the Cloud using solutions like Azure Cosmos DB, Azure SQL Database, and Azure Data Lake Storage.
* Performing Data Integration: Transition from data collection to actionable insights using Cloud-based data integration services like Data Factory.
* Processing data: Harness the Cloud’s computing power to process large datasets without needing powerful local machines.
* Using data analytics services: Turn data into actionable insights with services like Azure Synapse Analytics, Azure Stream Analytics, and Azure Databricks.
* Using Machine Learning and data intelligence services: Leverage pre-built machine learning algorithms and cognitive services like speech-to-text, text-to-speech, and computer vision with services like AzureML.

## Examples of Data Science in the Cloud

Let’s make this more concrete by exploring a couple of scenarios.

### Real-time social media sentiment analysis

A common beginner project in machine learning is real-time sentiment analysis of social media data.

Imagine you run a news media website and want to use live data to understand what content your readers might be interested in. You could build a program to analyze the sentiment of Twitter posts in real time on topics relevant to your audience.

Key indicators include the volume of tweets on specific topics (hashtags) and sentiment, determined using analytics tools.

Steps to create this project:

* Create an event hub to collect streaming input from Twitter.
* Configure and start a Twitter client application to call the Twitter Streaming APIs.
* Create a Stream Analytics job.
* Specify the job input and query.
* Create an output sink and specify the job output.
* Start the job.

For the full process, refer to the [documentation](https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?WT.mc_id=academic-77958-bethanycheum&ocid=AID30411099).

### Scientific papers analysis

Here’s another example: a project by [Dmitry Soshnikov](http://soshnikov.com), one of the authors of this curriculum.

Dmitry created a tool to analyze COVID-related scientific papers. This project demonstrates how to extract knowledge from scientific papers, gain insights, and help researchers navigate large collections of papers efficiently.

Steps involved:

* Extract and preprocess information using [Text Analytics for Health](https://docs.microsoft.com/azure/cognitive-services/text-analytics/how-tos/text-analytics-for-health?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).
* Use [Azure ML](https://azure.microsoft.com/services/machine-learning?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) to parallelize processing.
* Store and query information with [Cosmos DB](https://azure.microsoft.com/services/cosmos-db?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).
* Create an interactive dashboard for data exploration and visualization using Power BI.

For the full process, visit [Dmitry’s blog](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/).

As you can see, Cloud services offer numerous ways to perform Data Science.

## Footnote

Sources:
* https://azure.microsoft.com/overview/what-is-cloud-computing?ocid=AID3041109  
* https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?ocid=AID3041109  
* https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/  

## Post-Lecture Quiz

[Post-lecture quiz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/33)

## Assignment

[Market Research](assignment.md)

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.