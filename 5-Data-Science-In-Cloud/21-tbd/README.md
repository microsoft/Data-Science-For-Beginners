# Data Science in the Cloud: in progress
In this lesson, you will learn the fundamental principles of the Cloud, then you will see why it can be interesting for you to use Cloud services to run your data science projects and we'll look at some examples of data science projects run in the Cloud. 


## Pre-Lecture Quiz

[Pre-lecture quiz]()

## What is the Cloud?

The Cloud, or Cloud Computing, is the delivery of a wide range of pay-as-you-go computing services hosted on an infrastructure over the internet. Services include solutions such as storage, databases, networking, software, analytics, and intelligent services. 

We usually differentiate the Public, Private and Hybrid clouds: 

* Public cloud: a public cloud is owned and operated by a third-party cloud service provider which delivers their computing resources over the Internet to the public 

* Private cloud: refers to cloud computing resources used exclusively by a single business or organization, with services and an infrastructure maintained on a private network. 

* Hybrid cloud: the hybrid cloud is a system that combines public and private clouds. Users opt for an on-premises datacenter, while allowing data and applications to be run on one or more public clouds. 

Most cloud computing services fall into three categories: infrastructure as a service (IaaS), platform as a service (PaaS) and software as a service (SaaS). 

* Infrastructure as a service (IaaS): users rent an IT infrastructure — servers and virtual machines (VMs), storage, networks, operating systems 

* Platform as a service (PaaS): users rent an environment for developing, testing, delivering, and managing software applications. Users don’t need to worry about setting up or managing the underlying infrastructure of servers, storage, network, and databases needed for development. 

* Software as a service (SaaS): users get access to software applications over the Internet, on demand and typically on a subscription basis. Users don’t need to worry about hosting, managing the software application, the underlying infrastructure or the maintenance, like software upgrades and security patching. 


Some of the largest Cloud providers are Amazon Web Services, Google Cloud Platform and Microsoft Azure.

## Why Choose the Cloud for Data Science? 

Developers and IT professionals chose to work with the Cloud for many reasons, including the following: 

* Innovation: you can power your applications by integrating innovative services created by Cloud providers directly into your apps 

* Flexibility: you only pay for the services that you need and can choose from a wide range of services. You typically pay as you go and adapt your services according to your evolving needs. 

* Budget: you don’t need to make initial investments to purchase hardware and software, set up and run on-site datacenters and you can just pay for what you use 

* Scalability: your resources can scale according to the needs of your project, which means that your apps can use more or less computing power, storage and bandwidth, by adapting to external factors at any given time 

* Productivity: you can focus on your business rather than spend time on tasks that can be managed by someone else, such as managing datacenters 

* Reliability: cloud computing offers several ways to continuously back up your data and you can set up disaster recovery plans to keep your business going 

* Security: you can benefit from policies, technologies, and controls that strengthen the security of your project 

 These are some of the most reasons why people choose to use Cloud services. Now that we have a better understanding of what the Cloud is and what its main benefits are, let's look more specifically into the jobs of Data scientists and developers working with data, and how the Cloud can help them with several of the specific challenges they face: 

* Storing large amounts of data: instead of buying, managing and protecting big servers, you can store your data directly in the cloud, with solutions such as Azure Cosmos DB, Azure SQL Database and Azure Data Lake Storage 

* Performing data integration: data integration is an essential part of data science, that lets you go from data collection to taking actions. With data integration services offered in the cloud, you can collect, transform and integrate data from various sources into a single data warehouse, with Data Factory 

* Processing data: processing vast amounts of data requires a lot of computing power, and not everyone has access to machines powerful enough for that, which is why many people choose to directly harness the cloud’s huge computing power to run and deploy their solutions 

* Using data analytics services: to turn your data into actionable insights, with Azure Synapse Analytics, Azure Stream Analytics, Azure Databricks 

* Using Machine Learning and data intelligence services: Instead of starting from scratch, you can use machine learning algorithms offered by the cloud provider, with services such as AzureML, and you can use cognitive services such as speech-to-text, text to speech, computer vision and more  

 
## Examples of Data Science in the Cloud 

 

Let’s make this more tangible by looking at a couple of scenarios. 

 

We’ll start with a scenario commonly studied by people who start with machine learning: social media sentiment analysis in real time. 

 

Let's say you run a news media website, and you want to leverage live data to understand what content your readers could be interested in. To know more about that, you can build a program that performs real-time sentiment analysis of data from Twitter publications, on topics that are relevant to your readers. 

 

The key indicators you will look at is the volume of tweets on specific topics (hashtags), and sentiment, which is established using analytics tools that perform sentiment analysis around the specified topics. 

 

The steps necessary to create this projects are the following: 

* Create an event hub for streaming input, which will collect data from Twitter 

* Configure and start a Twitter client application, which will call the Twitter Streaming APIs 

* Create a Stream Analytics job 

* Specify the job input and query 

* Create an output sink and specify the job output 

* Start the job 

 

Let’s take a more original example of a project created by Dmitry Soshnikov, one of the authors of this curriculum. 

 

To view the full process, check out the [documentation](https://docs.microsoft.com/en-us/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends). 

 

Dmitry created a Generative Adversarial Network and taught it to create artificial paintings. We will see the different steps used to for this: 

 

* Creating artificial paintings 

* Training the network on paintings from a dataset 

* Training a GAN, or Generative Adversarial Network 

* Creating a discriminator model and a generator model 

* Training the script in the Cloud with Azure ML 

* Generating new images 

 

As you can see, we can leverage Cloud services in many ways to perform Data Science. 

 

To see the full process, visit [Dmitry’s blog](https://soshnikov.com/scienceart/creating-generative-art-using-gan-on-azureml). 

## Post-Lecture Quiz

[Post-lecture quiz]()

## Review & Self Study


## Assignment

[Assignment Title](assignment.md)
