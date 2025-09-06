<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f8e7cdefa096664ae86f795be571580",
  "translation_date": "2025-09-06T10:04:41+00:00",
  "source_file": "5-Data-Science-In-Cloud/17-Introduction/README.md",
  "language_code": "en"
}
-->
# Introduction to Data Science in the Cloud

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/17-DataScience-Cloud.png)|
|:---:|
| Data Science In The Cloud: Introduction - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

In this lesson, you will learn the basic concepts of the Cloud, understand why using Cloud services can be beneficial for your data science projects, and explore examples of data science projects implemented in the Cloud.

## [Pre-Lecture Quiz](https://ff-quizzes.netlify.app/en/ds/quiz/32)

## What is the Cloud?

The Cloud, or Cloud Computing, refers to the delivery of a variety of pay-as-you-go computing services hosted on infrastructure over the internet. These services include solutions like storage, databases, networking, software, analytics, and intelligent services.

Clouds are typically categorized into Public, Private, and Hybrid clouds:

* Public cloud: A public cloud is owned and operated by a third-party cloud service provider that delivers its computing resources over the internet to the public.
* Private cloud: Refers to cloud computing resources used exclusively by a single business or organization, with services and infrastructure maintained on a private network.
* Hybrid cloud: A hybrid cloud combines public and private clouds. Users can maintain an on-premises datacenter while allowing data and applications to run on one or more public clouds.

Most cloud computing services fall into three main categories: Infrastructure as a Service (IaaS), Platform as a Service (PaaS), and Software as a Service (SaaS).

* Infrastructure as a Service (IaaS): Users rent IT infrastructure such as servers, virtual machines (VMs), storage, networks, and operating systems.
* Platform as a Service (PaaS): Users rent an environment for developing, testing, delivering, and managing software applications without worrying about the underlying infrastructure like servers, storage, networks, and databases.
* Software as a Service (SaaS): Users access software applications over the internet, typically on a subscription basis, without managing hosting, infrastructure, or maintenance tasks like software updates and security patches.

Some of the largest Cloud providers include Amazon Web Services, Google Cloud Platform, and Microsoft Azure.

## Why Choose the Cloud for Data Science?

Developers and IT professionals opt for the Cloud for various reasons, including:

* Innovation: You can enhance your applications by integrating innovative services provided by Cloud providers directly into your apps.
* Flexibility: You pay only for the services you need and can choose from a wide range of options. Typically, you pay as you go and adjust services based on your evolving needs.
* Budget: You avoid upfront investments in hardware and software, as well as the setup and operation of on-site datacenters, paying only for what you use.
* Scalability: Resources can scale according to your project’s needs, allowing your apps to use more or less computing power, storage, and bandwidth as required.
* Productivity: You can focus on your business rather than spending time on tasks like managing datacenters, which can be handled by others.
* Reliability: Cloud Computing offers continuous data backup options and disaster recovery plans to ensure your business and services remain operational during crises.
* Security: You benefit from policies, technologies, and controls that enhance the security of your project.

These are some of the common reasons why people choose Cloud services. Now that we understand the Cloud and its benefits, let’s explore how it can assist data scientists and developers working with data in overcoming challenges such as:

* Storing large amounts of data: Instead of purchasing, managing, and securing large servers, you can store data directly in the Cloud using solutions like Azure Cosmos DB, Azure SQL Database, and Azure Data Lake Storage.
* Performing Data Integration: Data integration is a crucial step in Data Science, enabling the transition from data collection to actionable insights. Cloud services like Data Factory allow you to collect, transform, and integrate data from various sources into a single data warehouse.
* Processing data: Processing large datasets requires significant computing power, which not everyone has access to. Many choose to leverage the Cloud’s vast computing resources to run and deploy their solutions.
* Using data analytics services: Cloud services like Azure Synapse Analytics, Azure Stream Analytics, and Azure Databricks help transform data into actionable insights.
* Using Machine Learning and data intelligence services: Instead of starting from scratch, you can use machine learning algorithms provided by Cloud services like AzureML. Additionally, cognitive services like speech-to-text, text-to-speech, computer vision, and more are available.

## Examples of Data Science in the Cloud

Let’s explore a couple of scenarios to make this more concrete.

### Real-time social media sentiment analysis
A common beginner project in machine learning is real-time sentiment analysis of social media data.

Imagine you run a news media website and want to use live data to understand what content your readers might be interested in. You can build a program that performs real-time sentiment analysis on Twitter data related to topics relevant to your audience.

Key indicators include the volume of tweets on specific topics (hashtags) and sentiment, determined using analytics tools that perform sentiment analysis on the specified topics.

Steps to create this project:

* Create an event hub for streaming input to collect data from Twitter.
* Configure and start a Twitter client application to call the Twitter Streaming APIs.
* Create a Stream Analytics job.
* Specify the job input and query.
* Create an output sink and specify the job output.
* Start the job.

For the full process, refer to the [documentation](https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?WT.mc_id=academic-77958-bethanycheum&ocid=AID30411099).

### Scientific papers analysis
Here’s another example from [Dmitry Soshnikov](http://soshnikov.com), one of the authors of this curriculum.

Dmitry developed a tool to analyze COVID-related scientific papers. This project demonstrates how to create a tool that extracts knowledge from scientific papers, provides insights, and helps researchers efficiently navigate large collections of papers.

Steps involved:

* Extract and preprocess information using [Text Analytics for Health](https://docs.microsoft.com/azure/cognitive-services/text-analytics/how-tos/text-analytics-for-health?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).
* Use [Azure ML](https://azure.microsoft.com/services/machine-learning?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) to parallelize processing.
* Store and query information using [Cosmos DB](https://azure.microsoft.com/services/cosmos-db?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).
* Create an interactive dashboard for data exploration and visualization using Power BI.

For the full process, visit [Dmitry’s blog](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/).

As you can see, Cloud services offer numerous ways to perform Data Science.

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

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please note that automated translations may contain errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is recommended. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.