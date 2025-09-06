<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "661dad02c3ac239644d34c1eb51e76f8",
  "translation_date": "2025-09-06T20:09:59+00:00",
  "source_file": "4-Data-Science-Lifecycle/15-analyzing/README.md",
  "language_code": "en"
}
-->
# The Data Science Lifecycle: Analyzing

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/15-Analyzing.png)|
|:---:|
| Data Science Lifecycle: Analyzing - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

## [Pre-Lecture Quiz](https://ff-quizzes.netlify.app/en/ds/quiz/28)

The "Analyzing" phase in the data lifecycle ensures that the data can answer the proposed questions or solve a specific problem. This step may also involve verifying that a model is effectively addressing these questions and problems. This lesson focuses on Exploratory Data Analysis (EDA), which includes techniques for identifying features and relationships within the data and preparing it for modeling.

We’ll use an example dataset from [Kaggle](https://www.kaggle.com/balaka18/email-spam-classification-dataset-csv/version/1) to demonstrate how this can be done using Python and the Pandas library. This dataset contains counts of common words found in emails, with the sources of these emails anonymized. Use the [notebook](notebook.ipynb) in this directory to follow along.

## Exploratory Data Analysis

The "Capture" phase of the lifecycle involves acquiring data and defining the problems and questions at hand. But how can we confirm that the data will support the desired outcomes?  
Remember, a data scientist might ask the following questions when acquiring data:
-   Do I have enough data to solve this problem?
-   Is the data of sufficient quality for this problem?
-   If I uncover new insights from this data, should we consider revising or redefining the goals?

Exploratory Data Analysis is the process of familiarizing yourself with the data. It can help answer these questions and identify challenges associated with the dataset. Let’s explore some techniques used to achieve this.

## Data Profiling, Descriptive Statistics, and Pandas

How can we determine if we have enough data to solve the problem? Data profiling summarizes and gathers general information about the dataset using descriptive statistics. Data profiling helps us understand what is available, while descriptive statistics help us understand how much is available.

In previous lessons, we used Pandas to generate descriptive statistics with the [`describe()` function](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html). This function provides the count, maximum and minimum values, mean, standard deviation, and quantiles for numerical data. Using descriptive statistics like `describe()` can help you evaluate whether you have enough data or need more.

## Sampling and Querying

Exploring an entire large dataset can be time-consuming and is often left to computers. However, sampling is a useful tool for understanding the data. It allows you to gain insights into what the dataset contains and represents. With a sample, you can apply probability and statistics to draw general conclusions about the data. While there’s no strict rule on how much data to sample, it’s important to note that the more data you sample, the more accurate your generalizations will be.

Pandas includes the [`sample()` function](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sample.html), which allows you to specify the number of random samples you want to retrieve and use.

General querying of the data can help answer specific questions or test theories. Unlike sampling, queries allow you to focus on particular parts of the data that you’re curious about. The [`query()` function](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html) in the Pandas library lets you select columns and retrieve rows to answer specific questions about the data.

## Exploring with Visualizations

You don’t need to wait until the data is fully cleaned and analyzed to start creating visualizations. In fact, visualizations during the exploration phase can help identify patterns, relationships, and issues in the data. Additionally, visualizations are a great way to communicate findings to stakeholders who may not be directly involved in managing the data. They can also help surface new questions that weren’t addressed during the "Capture" phase. Refer to the [section on Visualizations](../../../../../../../../../3-Data-Visualization) to learn more about popular methods for visual exploration.

## Exploring to Identify Inconsistencies

The techniques covered in this lesson can help identify missing or inconsistent values, but Pandas also provides specific functions for this purpose. The [isna() or isnull()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.isna.html) functions can check for missing values. A key part of exploring these values is understanding why they are missing in the first place. This can guide you in deciding what [actions to take to address them](/2-Working-With-Data/08-data-preparation/notebook.ipynb).

## [Post-Lecture Quiz](https://ff-quizzes.netlify.app/en/ds/quiz/29)

## Assignment

[Exploring for answers](assignment.md)

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please note that automated translations may contain errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is recommended. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.