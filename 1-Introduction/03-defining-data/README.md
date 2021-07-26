# Defining Data

## Introduction
Data are facts, information, observations and measurements that are used to make discoveries and to support informed decisions. A dataset, which is a collection of data may come in different formats and structures, and will usually be based on its source, or where the data came from. For example, a company's monthly earnings might be in a spreadsheet but hourly heart rate data from a smartwatch may be in [JSON](https://stackoverflow.com/a/383699) format. It's common for data scientists to work with different types of data within a dataset. 


This lesson focuses on identifying and classifying data by its characteristics and its sources.

## Pre-Lecture Quiz

[Pre-lecture quiz]()


## How Data is Described

### Raw Data
### Numerical
### Categorical


## How Data is Structured

## Structured Data
Structured data is data that is organized into rows and columns, where each row will have the same set of columns. Columns represent a value of a particular type and will be identified with a name describing what the value represents, while rows contain the actual values. Columns will often have a specific set of rules or restrictions on the values, to ensure that the values accurately represent the column. For example imagine a spreadsheet of customers where each row must have a phone number and the phone numbers never contain alphabetical characters. There may be rules applied on the phone number column to make sure it's never empty and only contains numbers. 

A benefit of structured data is that it can be organized in such a way that it can be related to other structured data. However, because the data is designed to be organized in a specific way, making changes to its overall structure can take a lot of effort to do. For example, adding an email column to the customer spreadsheet that cannot be empty means you'll need figure out how you'll add these values to the existing rows of customers in the dataset. 

Examples of structured data: spreadsheets, relational databases, phone numbers, bank statements

![image of type]()
*type description*

## Unstructured Data
Unstructured data typically cannot be categorized into into rows or columns and doesn't contain a format or set of rules to follow. Because unstructured data has less restrictions on its structure it's easier to add new information in comparison to a structured dataset. If a sensor capturing data on barometric pressure every 2 minutes has received an update that measures and records temperature, it doesn't require altering the existing data. However, this may make analyzing or investigating this type of data take longer. For example, a scientist who wants to find the average temperature of the previous month from the sensors data, but discovers that the sensor recorded an "e" in some of its recorded data to note that it was broken instead of a typical number, which means the data is incomplete.

Examples of unstructured data:  text files, text messages, video files

![image of type]()
*type description*

## Semi-structured
Semi-structured data has features that make it a combination of structured and unstructured data. It doesn't typically conform to a format of rows and columns but is organized in a way that is considered structured and may follow a fixed format or set of rules. The structure will vary between sources, such as a well defined hierarchy to something more flexible that allows for easy integration of new information. Metadata are indicators that help decide how the data is organized and stored and will have various names, based on the type of data. Some common names for metadata are tags, elements, entities and attributes.

Examples of unstructured data:  HTML, JSON, CSV files, emails

## Sources of Data
### Internet
#### APIs
#### Scraping
### Spreadsheets


## 🚀 Challenge


## Post-Lecture Quiz

[Post-lecture quiz]()

## Review & Self Study


## Assignment

[Assignment Title](assignment.md)
