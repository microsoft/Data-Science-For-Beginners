<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "661dad02c3ac239644d34c1eb51e76f8",
  "translation_date": "2025-11-18T18:40:47+00:00",
  "source_file": "4-Data-Science-Lifecycle/15-analyzing/README.md",
  "language_code": "pcm"
}
-->
# The Data Science Lifecycle: Analyzing

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/15-Analyzing.png)|
|:---:|
| Data Science Lifecycle: Analyzing - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

## [Pre-Lecture Quiz](https://ff-quizzes.netlify.app/en/ds/quiz/28)

Analyzing for data lifecycle na di step wey go confirm say di data fit answer di questions wey dem propose or solve one particular problem. Dis step fit also focus on confirming say one model dey address di questions and problems well. Dis lesson go focus on Exploratory Data Analysis (EDA), wey be techniques wey dey help define di features and relationships wey dey di data, and fit also prepare di data for modeling.

We go use one example dataset from [Kaggle](https://www.kaggle.com/balaka18/email-spam-classification-dataset-csv/version/1) to show how we fit use Python and Pandas library take do am. Dis dataset get count of some common words wey dey emails, but di sources of di emails dey anonymous. Use di [notebook](notebook.ipynb) wey dey dis directory to follow di steps.

## Exploratory Data Analysis

Di capture phase for di lifecycle na di stage wey dem dey collect di data and di problems/questions wey dey ground, but how we go take know say di data fit support di final result? 
Make we remember say data scientist fit ask dis kind questions when dem dey collect data:
-   I get enough data to solve dis problem?
-   Di quality of di data dey okay for dis problem?
-   If I find new information from di data, we go need change or redefine di goals?
Exploratory Data Analysis na di process wey go help us sabi di data well and fit help answer dis kind questions, plus identify di wahala wey dey di dataset. Make we look some techniques wey dem dey use to achieve dis.

## Data Profiling, Descriptive Statistics, and Pandas
How we go take know say we get enough data to solve dis problem? Data profiling fit summarize and gather general information about di dataset through descriptive statistics techniques. Data profiling dey help us understand wetin dey available, and descriptive statistics dey help us understand how many things dey available.

For some of di previous lessons, we don use Pandas take provide descriptive statistics with di [`describe()` function]( https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html). E dey show di count, max and min values, mean, standard deviation, and quantiles for di numerical data. Using descriptive statistics like di `describe()` function fit help you check how much data you get and if you need more.

## Sampling and Querying
To explore everything for one big dataset fit take plenty time, and na work wey computer dey usually do. But sampling na one helpful tool wey fit help us understand di data well and give us better idea of wetin dey di dataset and wetin e represent. With sampling, you fit use probability and statistics take reach general conclusions about di data. Even though no rule dey define how much data you suppose sample, e good make you note say di more data you sample, di more accurate your generalization go be. 
Pandas get [`sample()` function for im library](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sample.html) wey you fit use pass argument of how many random samples you want.

General querying of di data fit help you answer some general questions and theories wey you get. Unlike sampling, queries dey allow you focus on specific parts of di data wey you get questions about. 
Di [`query()` function](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html) for Pandas library fit help you select columns and get simple answers about di data through di rows wey e retrieve.

## Exploring with Visualizations
You no need wait until di data don clean well or analyze finish before you start dey create visualizations. In fact, visual representation while you dey explore fit help you see patterns, relationships, and problems for di data. Plus, visualizations dey help communicate with people wey no dey involved with di data management, and e fit be opportunity to share and clarify extra questions wey dem no address for di capture stage. Check di [section on Visualizations](../../../../../../../../../3-Data-Visualization) to learn more about popular ways to explore visually.

## Exploring to identify inconsistencies
All di topics for dis lesson fit help identify missing or inconsistent values, but Pandas get functions wey fit check for some of dem. [isna() or isnull()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.isna.html) fit check for missing values. One important thing for exploring dis kind values for your data na to check why dem dey like dat in di first place. Dis fit help you decide wetin [actions to take to resolve dem](/2-Working-With-Data/08-data-preparation/notebook.ipynb).

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ds/quiz/29)

## Assignment

[Exploring for answers](assignment.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even as we dey try make am accurate, abeg sabi say automated translations fit get mistake or no dey correct well. Di original dokyument for im native language na di main source wey you go trust. For important mata, e better make professional human translation dey use. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->