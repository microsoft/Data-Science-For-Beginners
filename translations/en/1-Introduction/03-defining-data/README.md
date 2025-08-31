<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "356d12cffc3125db133a2d27b827a745",
  "translation_date": "2025-08-31T11:10:03+00:00",
  "source_file": "1-Introduction/03-defining-data/README.md",
  "language_code": "en"
}
-->
# Defining Data

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/03-DefiningData.png)|
|:---:|
|Defining Data - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

Data consists of facts, information, observations, and measurements that are used to make discoveries and support informed decisions. A data point is a single unit of data within a dataset, which is a collection of data points. Datasets can come in various formats and structures, often depending on their source or origin. For instance, a company's monthly earnings might be stored in a spreadsheet, while hourly heart rate data from a smartwatch might be in [JSON](https://stackoverflow.com/a/383699) format. It's common for data scientists to work with different types of data within a dataset.

This lesson focuses on identifying and classifying data based on its characteristics and sources.

## [Pre-Lecture Quiz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/4)

## How Data is Described

### Raw Data
Raw data refers to data in its original state, directly from its source, without any analysis or organization. To make sense of a dataset, it needs to be organized into a format that can be understood by humans and the technology used for further analysis. The structure of a dataset describes how it is organized and can be classified as structured, unstructured, or semi-structured. These classifications depend on the source but ultimately fall into one of these three categories.

### Quantitative Data
Quantitative data consists of numerical observations within a dataset that can typically be analyzed, measured, and used mathematically. Examples of quantitative data include a country's population, a person's height, or a company's quarterly earnings. With further analysis, quantitative data can be used to identify seasonal trends in the Air Quality Index (AQI) or estimate the likelihood of rush hour traffic on a typical workday.

### Qualitative Data
Qualitative data, also known as categorical data, cannot be measured objectively like quantitative data. It often consists of subjective information that captures the quality of something, such as a product or process. Sometimes, qualitative data is numerical but not typically used mathematically, like phone numbers or timestamps. Examples of qualitative data include video comments, the make and model of a car, or your closest friends' favorite color. Qualitative data can be used to understand which products consumers prefer or to identify popular keywords in job application resumes.

### Structured Data
Structured data is organized into rows and columns, where each row has the same set of columns. Columns represent specific types of values and are identified by names describing what the values represent, while rows contain the actual data. Columns often have rules or restrictions to ensure the values accurately represent the column. For example, imagine a spreadsheet of customers where each row must include a phone number, and the phone numbers cannot contain alphabetical characters. Rules might be applied to ensure the phone number column is never empty and only contains numbers.

One advantage of structured data is that it can be organized in a way that allows it to relate to other structured data. However, because the data is designed to follow a specific structure, making changes to its overall organization can require significant effort. For instance, adding an email column to the customer spreadsheet that cannot be empty would require figuring out how to populate this column for existing rows.

Examples of structured data: spreadsheets, relational databases, phone numbers, bank statements.

### Unstructured Data
Unstructured data cannot typically be organized into rows or columns and lacks a defined format or set of rules. Because unstructured data has fewer restrictions, it is easier to add new information compared to structured datasets. For example, if a sensor measuring barometric pressure every two minutes receives an update to also record temperature, it wouldn't require altering the existing data if it's unstructured. However, analyzing or investigating unstructured data can take longer. For instance, a scientist trying to calculate the average temperature for the previous month might find that the sensor recorded an "e" in some entries to indicate it was broken, resulting in incomplete data.

Examples of unstructured data: text files, text messages, video files.

### Semi-structured Data
Semi-structured data combines features of both structured and unstructured data. It doesn't typically conform to rows and columns but is organized in a way that is considered structured and may follow a fixed format or set of rules. The structure can vary between sources, ranging from a well-defined hierarchy to something more flexible that allows for easy integration of new information. Metadata provides indicators for how the data is organized and stored, with various names depending on the type of data. Common names for metadata include tags, elements, entities, and attributes. For example, a typical email message includes a subject, body, and recipients, and can be organized by sender or date.

Examples of semi-structured data: HTML, CSV files, JavaScript Object Notation (JSON).

## Sources of Data

A data source refers to the original location where the data was generated or "lives," and it varies based on how and when it was collected. Data generated by its user(s) is known as primary data, while secondary data comes from a source that has collected data for general use. For example, scientists collecting observations in a rainforest would be considered primary data, and if they share it with other scientists, it becomes secondary data for those users.

Databases are a common data source and rely on a database management system to host and maintain the data. Users explore the data using commands called queries. Files can also serve as data sources, including audio, image, and video files, as well as spreadsheets like Excel. The internet is another common location for hosting data, where both databases and files can be found. Application programming interfaces (APIs) allow programmers to create ways to share data with external users over the internet, while web scraping extracts data from web pages. The [lessons in Working with Data](../../../../../../../../../2-Working-With-Data) focus on how to use various data sources.

## Conclusion

In this lesson, we have learned:

- What data is
- How data is described
- How data is classified and categorized
- Where data can be found

## 🚀 Challenge

Kaggle is an excellent source of open datasets. Use the [dataset search tool](https://www.kaggle.com/datasets) to find some interesting datasets and classify 3-5 datasets using the following criteria:

- Is the data quantitative or qualitative?
- Is the data structured, unstructured, or semi-structured?

## [Post-Lecture Quiz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/5)

## Review & Self Study

- This Microsoft Learn unit, titled [Classify your Data](https://docs.microsoft.com/en-us/learn/modules/choose-storage-approach-in-azure/2-classify-data), provides a detailed breakdown of structured, semi-structured, and unstructured data.

## Assignment

[Classifying Datasets](assignment.md)

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.