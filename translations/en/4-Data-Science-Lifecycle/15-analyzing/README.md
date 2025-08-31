<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d92f57eb110dc7f765c05cbf0f837c77",
  "translation_date": "2025-08-31T11:00:04+00:00",
  "source_file": "4-Data-Science-Lifecycle/15-analyzing/README.md",
  "language_code": "en"
}
-->
# The Data Science Lifecycle: Analyzing

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/15-Analyzing.png)|
|:---:|
| Data Science Lifecycle: Analyzing - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

## Pre-Lecture Quiz

## [Pre-Lecture Quiz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/28)

The "Analyzing" phase in the data lifecycle ensures that the data can address the questions posed or solve a specific problem. This step may also involve verifying that a model is effectively tackling these questions and issues. This lesson focuses on Exploratory Data Analysis (EDA), which includes techniques for identifying features and relationships within the data, as well as preparing the data for modeling.

We'll use an example dataset from [Kaggle](https://www.kaggle.com/balaka18/email-spam-classification-dataset-csv/version/1) to demonstrate how this can be done using Python and the Pandas library. This dataset contains counts of common words found in emails, with the sources of these emails anonymized. Use the [notebook](../../../../4-Data-Science-Lifecycle/15-analyzing/notebook.ipynb) in this directory to follow along.

## Exploratory Data Analysis

The "Capture" phase of the lifecycle involves acquiring data and defining the problems and questions at hand. But how can we confirm that the data will support the desired outcomes? 
A data scientist might ask the following questions when working with acquired data:
-   Do I have enough data to solve this problem?
-   Is the data of sufficient quality for this problem?
-   If new insights emerge from the data, should we consider revising or redefining the goals?

Exploratory Data Analysis is the process of familiarizing yourself with the data and can help answer these questions, as well as identify challenges associated with the dataset. Let’s explore some techniques used to achieve this.

## Data Profiling, Descriptive Statistics, and Pandas
How can we determine if we have enough data to solve the problem? Data profiling provides a summary and general overview of the dataset using descriptive statistics techniques. Data profiling helps us understand what is available, while descriptive statistics help us understand how much is available.

In previous lessons, we used Pandas to generate descriptive statistics with the [`describe()` function](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html). This function provides the count, maximum and minimum values, mean, standard deviation, and quantiles for numerical data. Using descriptive statistics like `describe()` can help you evaluate whether you have sufficient data or need more.

## Sampling and Querying
Exploring every detail in a large dataset can be time-consuming and is often left to computers. However, sampling is a useful technique for gaining a better understanding of the data and what it represents. By working with a sample, you can apply probability and statistics to draw general conclusions about the dataset. While there’s no strict rule for how much data to sample, it’s worth noting that larger samples lead to more accurate generalizations about the data.

Pandas includes the [`sample()` function](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sample.html), which allows you to specify the number of random samples you want to extract and use.

General querying of the data can help answer specific questions or test theories you may have. Unlike sampling, queries allow you to focus on particular parts of the dataset that are relevant to your questions. The [`query()` function](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html) in the Pandas library lets you select columns and retrieve rows to answer specific questions about the data.

## Exploring with Visualizations
You don’t need to wait until the data is fully cleaned and analyzed to start creating visualizations. In fact, visualizations can be helpful during exploration, as they can reveal patterns, relationships, and issues within the data. Additionally, visualizations provide a way to communicate findings to people who aren’t directly involved in managing the data, offering an opportunity to share and refine questions that may not have been addressed during the "Capture" phase. Refer to the [section on Visualizations](../../../../../../../../../3-Data-Visualization) to learn more about popular methods for visual exploration.

## Exploring to Identify Inconsistencies
The techniques covered in this lesson can help identify missing or inconsistent values, but Pandas also offers specific functions for detecting these issues. [isna() or isnull()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.isna.html) can be used to check for missing values. An important part of exploring these values is understanding why they are missing in the first place. This insight can guide you in deciding what [actions to take to resolve them](../../../../../../../../../2-Working-With-Data/08-data-preparation/notebook.ipynb).

## [Pre-Lecture Quiz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/27)

## Assignment

[Exploring for answers](assignment.md)

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.