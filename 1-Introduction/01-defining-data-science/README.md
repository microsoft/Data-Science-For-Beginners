# Defining Data Science

## Pre-Lecture Quiz

[Pre-lecture quiz]()

## What is Data?

In our everyday life, we are always surrounded by **data**. The text you are reading now is data, the list of phone numbers of your friends in your smartphone is data, as well as current time displayed on your watch. As human beings, we naturally operate with data, counting the amount of money we have, or writing letters to our friends.

However, data became much more important with the creation of **computers**. The main role of computers is to perform *computations*, but they need data to operate on. Thus, we need to understand how computers store and process data.

With the emergence of Internet, the role of computers as data handling devices increased. If you think of it, we now use computers more and more for data processing and communication, rather than actual computations. When we write an e-mail to a friend, or search some information on the Internet - we are essentially creating, storing, transmitting, and manipulating data.

> Can you remember the last time you have used computers to actually compute something? 

## What is Data Science?

In [Wikipedia](https://en.wikipedia.org/wiki/Data_science), **Data Science** is defined as *scientific field that uses scientific methods to extract knowledge and insights from structured and unstructured data, and apply knowledge and actionable insights from data across a broad range of application domains*. 

This definition highlights the following important aspects of data science:

* The main goal of data science is to **extract knowledge** from data, in order words - to **understand** data, find some hidden relationships and build a **model**.
* Data science uses **scientific methods**, such as probability and statistics. In fact, when the term *data science* was first introduced, some people argued that data science is just a new fancy name for statistics. Nowadays it becomes evident that the field is much more broad.    
* Obtained knowledge should be applied to produce some **actionable insights**.
* We should be able to operate on both **structured** and **unstructured** data. We will come back to discuss different types of data later in the course.
* **Application domain** is an important concept, and data scientist often needs at least some degree of expertise in the problem domain.

> Another important aspect of Data Science is that it studies how data can be gathered, stored and operated upon using computers. While statistics gives us mathematical foundations, data science applies mathematical concepts to actually draw insights from data.

One of the ways (attributed to [Jim Gray](https://en.wikipedia.org/wiki/Jim_Gray_(computer_scientist))) to look at the data science is to consider it to be a separate paradigm of science:
* **Empyrical**, in which we rely mostly on observations and results of experiments
* **Theoretical**, where new concepts emerge from existing scientific knowledge
* **Computational**, where we discover new principles based on some computational experiments
* **Data-Driven**, based on discovering relationships and patterns in the data  

## Other Related Fields

Since data is pervasive concept, data science itself is also a broad field, touching many other related disciplines.

<dl>
<dt>Databases</dt>
<dd>
The most obvious thing to consider is **how to store** the data, i.e. how to structure them in a way that allows faster processing. There are different types of databases that store structured and unstructured data, which [we will consider in our course](../../2-Working-With-Data/README.md).
</dd>
<dt>Big Data</dt>
<dd>
Often we need to store and process really large quantities of data with relatively simple structure. There are special approaches and tools to store that data in a distributed manner on a computer cluster, and process them efficiently.
</dd>
<dt>Machine Learning</dt>
<dd>
One of the ways to understand the data is to **build a model** that will be able to predict desired outcome. Being able to learn such models from data is the area studied in **machine learning**. You may want to have a look at our [Machine Learning for Beginners](https://github.com/microsoft/ML-For-Beginners/) Curriculum to get deeper into that field.
</dd>
<dt>Artificial Intelligence</dt>
<dd>
As machine learning, artificial intelligence also relies on data, and it involves building high complexity models that will exhibit the behavior similar to a human being. Also, AI methods often allow us to turn unstructured data (eg. natural language) into structured by extracting some insights. 
</dd>
<dt>Visualization</dt>
<dd>
Vast amounts of data are incomprehensible for a human being, but once we create useful visualizations - we can start making much more sense of data, and drawing some conclusions. Thus, it is important to know many ways to visualize information - something that we will cover in [Section 3](../../3-Data-Visualization/README.md) of our course. Related fields also include **Infographics**, and **Human-Computer Interaction** in general. 
</dd>
</dl>

## Types of Data

As we have already mentioned - data is everywhere, we just need to capture it in the right way! It is useful to distinguish between **structured** and **unstructured** data - the former are typically represented in some well-structured form, often as a table or number of tables, while latter is just a collection of files. Sometimes we can also talk about **semistructured** data, that have some sort of a structure that may vary greatly.

| Structured | Semi-structured | Unstructured |
|----------- |-----------------|--------------|
| List of people with their phone numbers | Wikipedia pages with links | Text of Encyclopaedia Brittanica |
| Temperature in all rooms of a building at every minute for the last 20 years | Collection of scientific papers in JSON format with authors, data of publication, and abstract | File share with corporate documents |
| Data for age and gender for all people entering the building | Internet pages | Raw video feed from surveillance camera |

## Where to get Data

There are many possible sources of data, and it will be impossible to list all of them! However, let's mention some of the typical places where you can get data:
  
## What you can do with Data



## Digitalization and Digital Transformation

In the last decade, many businesses started to understand the importance of data when making business decisions. To apply data science principles to running a business one first needs to collect some data, i.e. somehow turn business processes into digital form. This is known as **digitalization**, and followed by using data science techniques to guide decisions it often leads to significant increase of productivity (or even business pivot), called **digital transformation**.

Let's consider an example. Suppose, we have a data science course (like this one), which we deliver online to students, and we want to use data science to improve it. How can we do it?

We can start with thinking "what can be digitized?". The simplest way would be to measure time it takes each student to complete each module, and the obtained knowledge (eg. by giving multiple-choice test at the end of each module). By averaging time-to-complete across all students, we can find out which modules cause the most problems to students, and work on simplifying them.

> You may argue that this approach is not ideal, because modules can be of different length. It is probably more fair to divide the time by the length of the module (in number of characters), and compare those values instead.

When we start analyzing results of multiple-choice tests, we can try to find out specific concepts that students understand poorly, and improve the content. To do that, we need to design tests in such a way that each question maps to a certain concept or chunk of knowledge.

If we want to get even more complicated, we can plot the time taken for each module against the age category of students. We might find out that for some age categories it takes inappropriately long time to complete the module, or students drop out at certain point. This can help us provide age recommendation for the module, and minimize people's dissatisfaction from wrong expectations.

## 🚀 Challenge

In this challenge, we will try to find concepts relevant to the field of Data Science by looking at texts. We will take Wikipedia article on Data Science, download and process the text, and then build a word cloud like this one:

![Word Cloud for Data Science](images/ds_wordcloud.png)
## Post-Lecture Quiz

[Post-lecture quiz]()

## Review & Self Study

## Assignment

[Assignment Title](assignment.md)
