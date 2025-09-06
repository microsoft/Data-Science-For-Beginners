<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dc8f035ce92e4eaa078ab19caa68267a",
  "translation_date": "2025-08-31T10:58:32+00:00",
  "source_file": "2-Working-With-Data/07-python/assignment.md",
  "language_code": "en"
}
-->
# Assignment for Data Processing in Python

In this assignment, we will ask you to expand upon the code we started developing in our challenges. The assignment consists of two parts:

## COVID-19 Spread Modeling

 - [ ] Plot *R* graphs for 5-6 different countries on one plot for comparison, or using several plots side-by-side.
 - [ ] Analyze how the number of deaths and recoveries correlates with the number of infected cases.
 - [ ] Determine how long a typical disease lasts by visually correlating infection rates and death rates, and identifying any anomalies. You may need to examine data from different countries to figure this out.
 - [ ] Calculate the fatality rate and observe how it changes over time. *You may want to account for the duration of the disease in days to shift one time series before performing calculations.*

## COVID-19 Papers Analysis

- [ ] Build a co-occurrence matrix for different medications and identify which medications are frequently mentioned together (i.e., in the same abstract). You can adapt the code for building a co-occurrence matrix for medications and diagnoses.
- [ ] Visualize this matrix using a heatmap.
- [ ] As a stretch goal, visualize the co-occurrence of medications using [chord diagram](https://en.wikipedia.org/wiki/Chord_diagram). [This library](https://pypi.org/project/chord/) may assist you in creating a chord diagram.
- [ ] As another stretch goal, extract dosages of different medications (e.g., **400mg** in *take 400mg of chloroquine daily*) using regular expressions, and build a dataframe that displays various dosages for different medications. **Note**: Consider numeric values that are located near the medication name in the text.

## Rubric

Exemplary | Adequate | Needs Improvement
--- | --- | --- |
All tasks are completed, graphically illustrated, and explained, including at least one of the two stretch goals | More than 5 tasks are completed, no stretch goals are attempted, or the results are unclear | Fewer than 5 (but more than 3) tasks are completed, and visualizations do not effectively demonstrate the point

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.