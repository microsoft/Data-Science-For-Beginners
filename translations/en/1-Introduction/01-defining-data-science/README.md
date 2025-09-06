<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a76ab694b1534fa57981311975660bfe",
  "translation_date": "2025-09-06T11:58:59+00:00",
  "source_file": "1-Introduction/01-defining-data-science/README.md",
  "language_code": "en"
}
-->
Of course, depending on the specific data, some steps might be skipped (e.g., if the data is already stored in a database or if model training isn't necessary), or some steps might be repeated multiple times (such as data processing).

## Digitalization and Digital Transformation

Over the past decade, many businesses have come to realize the importance of data in making informed decisions. To apply data science principles to business operations, the first step is to collect relevant data, which involves converting business processes into digital formats. This process is known as **digitalization**. Using data science techniques on this data to guide decision-making can lead to significant improvements in productivity—or even a complete business pivot—referred to as **digital transformation**.

Let’s look at an example. Suppose we have an online data science course (like this one) that we deliver to students, and we want to use data science to enhance it. How can we achieve this?

We can begin by asking, "What can be digitized?" The simplest approach might be to track the time each student spends completing each module and assess their knowledge by administering a multiple-choice test at the end of each module. By calculating the average time-to-complete across all students, we can identify which modules are the most challenging and focus on simplifying them.
You might argue that this approach isn't perfect, as modules can vary in length. It would probably be fairer to divide the time by the module's length (measured in the number of characters) and compare those values instead.
When analyzing the results of multiple-choice tests, we can identify concepts that students struggle to understand and use this information to improve the content. To achieve this, tests should be designed so that each question corresponds to a specific concept or piece of knowledge.

For a more advanced approach, we can compare the time taken to complete each module with the age group of the students. This might reveal that certain age groups take an unusually long time to finish a module or that students drop out before completing it. Such insights can help us recommend appropriate age ranges for the module and reduce dissatisfaction caused by mismatched expectations.

## 🚀 Challenge

In this challenge, we will explore concepts related to Data Science by analyzing text. We'll use a Wikipedia article on Data Science, download and process the text, and then create a word cloud similar to this one:

![Word Cloud for Data Science](../../../../translated_images/ds_wordcloud.664a7c07dca57de017c22bf0498cb40f898d48aa85b3c36a80620fea12fadd42.en.png)

Check out [`notebook.ipynb`](../../../../1-Introduction/01-defining-data-science/notebook.ipynb ':ignore') to review the code. You can also run the code to see how it performs all data transformations in real time.

> If you're unfamiliar with running code in a Jupyter Notebook, refer to [this article](https://soshnikov.com/education/how-to-execute-notebooks-from-github/).

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ds/quiz/1)

## Assignments

* **Task 1**: Modify the code above to identify related concepts for the fields of **Big Data** and **Machine Learning**.
* **Task 2**: [Reflect on Data Science Scenarios](assignment.md)

## Credits

This lesson was created with ♥️ by [Dmitry Soshnikov](http://soshnikov.com)

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please note that automated translations may contain errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is recommended. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.