<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b29e427401499e81f4af55a8c4afea76",
  "translation_date": "2025-09-05T07:44:29+00:00",
  "source_file": "3-Data-Visualization/12-visualization-relationships/README.md",
  "language_code": "en"
}
-->
# Visualizing Relationships: All About Honey 🍯

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/12-Visualizing-Relationships.png)|
|:---:|
|Visualizing Relationships - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

Continuing with the nature focus of our research, let's explore some fascinating visualizations to illustrate the relationships between different types of honey, based on a dataset from the [United States Department of Agriculture](https://www.nass.usda.gov/About_NASS/index.php).

This dataset, containing around 600 entries, showcases honey production across various U.S. states. For instance, you can examine the number of colonies, yield per colony, total production, stocks, price per pound, and the value of honey produced in a specific state from 1998 to 2012, with one row per year for each state.

It would be intriguing to visualize the relationship between a state's annual production and, for example, the price of honey in that state. Alternatively, you could explore the relationship between states' honey yield per colony. This time period includes the emergence of the devastating 'CCD' or 'Colony Collapse Disorder,' first observed in 2006 (http://npic.orst.edu/envir/ccd.html), making this dataset particularly significant. 🐝

## [Pre-lecture quiz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/22)

In this lesson, you’ll use Seaborn, a library you’ve worked with before, to visualize relationships between variables. A particularly useful feature is Seaborn's `relplot` function, which enables scatter plots and line plots to quickly visualize '[statistical relationships](https://seaborn.pydata.org/tutorial/relational.html?highlight=relationships).' This helps data scientists better understand how variables interact.

## Scatterplots

Use a scatterplot to illustrate how the price of honey has changed year over year in each state. Seaborn's `relplot` makes it easy to group state data and display both categorical and numerical data points.

Let’s begin by importing the data and Seaborn:

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
honey = pd.read_csv('../../data/honey.csv')
honey.head()
```
You’ll notice that the honey dataset contains several interesting columns, including year and price per pound. Let’s explore this data, grouped by U.S. state:

| state | numcol | yieldpercol | totalprod | stocks   | priceperlb | prodvalue | year |
| ----- | ------ | ----------- | --------- | -------- | ---------- | --------- | ---- |
| AL    | 16000  | 71          | 1136000   | 159000   | 0.72       | 818000    | 1998 |
| AZ    | 55000  | 60          | 3300000   | 1485000  | 0.64       | 2112000   | 1998 |
| AR    | 53000  | 65          | 3445000   | 1688000  | 0.59       | 2033000   | 1998 |
| CA    | 450000 | 83          | 37350000  | 12326000 | 0.62       | 23157000  | 1998 |
| CO    | 27000  | 72          | 1944000   | 1594000  | 0.7        | 1361000   | 1998 |

Create a basic scatterplot to show the relationship between the price per pound of honey and its state of origin. Adjust the `y` axis to ensure all states are visible:

```python
sns.relplot(x="priceperlb", y="state", data=honey, height=15, aspect=.5);
```
![scatterplot 1](../../../../3-Data-Visualization/12-visualization-relationships/images/scatter1.png)

Next, use a honey-inspired color scheme to show how the price evolves over the years. Add a 'hue' parameter to highlight year-over-year changes:

> ✅ Learn more about the [color palettes you can use in Seaborn](https://seaborn.pydata.org/tutorial/color_palettes.html) - try a beautiful rainbow color scheme!

```python
sns.relplot(x="priceperlb", y="state", hue="year", palette="YlOrBr", data=honey, height=15, aspect=.5);
```
![scatterplot 2](../../../../3-Data-Visualization/12-visualization-relationships/images/scatter2.png)

With this color scheme, you can clearly see a strong upward trend in honey prices over the years. For example, if you examine Arizona's data, you’ll notice a consistent pattern of price increases year over year, with only a few exceptions:

| state | numcol | yieldpercol | totalprod | stocks  | priceperlb | prodvalue | year |
| ----- | ------ | ----------- | --------- | ------- | ---------- | --------- | ---- |
| AZ    | 55000  | 60          | 3300000   | 1485000 | 0.64       | 2112000   | 1998 |
| AZ    | 52000  | 62          | 3224000   | 1548000 | 0.62       | 1999000   | 1999 |
| AZ    | 40000  | 59          | 2360000   | 1322000 | 0.73       | 1723000   | 2000 |
| AZ    | 43000  | 59          | 2537000   | 1142000 | 0.72       | 1827000   | 2001 |
| AZ    | 38000  | 63          | 2394000   | 1197000 | 1.08       | 2586000   | 2002 |
| AZ    | 35000  | 72          | 2520000   | 983000  | 1.34       | 3377000   | 2003 |
| AZ    | 32000  | 55          | 1760000   | 774000  | 1.11       | 1954000   | 2004 |
| AZ    | 36000  | 50          | 1800000   | 720000  | 1.04       | 1872000   | 2005 |
| AZ    | 30000  | 65          | 1950000   | 839000  | 0.91       | 1775000   | 2006 |
| AZ    | 30000  | 64          | 1920000   | 902000  | 1.26       | 2419000   | 2007 |
| AZ    | 25000  | 64          | 1600000   | 336000  | 1.26       | 2016000   | 2008 |
| AZ    | 20000  | 52          | 1040000   | 562000  | 1.45       | 1508000   | 2009 |
| AZ    | 24000  | 77          | 1848000   | 665000  | 1.52       | 2809000   | 2010 |
| AZ    | 23000  | 53          | 1219000   | 427000  | 1.55       | 1889000   | 2011 |
| AZ    | 22000  | 46          | 1012000   | 253000  | 1.79       | 1811000   | 2012 |

Another way to visualize this trend is by using size instead of color. For colorblind users, this might be a better option. Modify your visualization to show price increases through larger dot sizes:

```python
sns.relplot(x="priceperlb", y="state", size="year", data=honey, height=15, aspect=.5);
```
You’ll notice the dots gradually increasing in size.

![scatterplot 3](../../../../3-Data-Visualization/12-visualization-relationships/images/scatter3.png)

Could this simply be a case of supply and demand? Are factors like climate change and colony collapse reducing the honey supply year over year, leading to higher prices?

To investigate correlations between variables in this dataset, let’s explore some line charts.

## Line charts

Question: Is there a clear upward trend in honey prices per pound year over year? A single line chart can help answer this:

```python
sns.relplot(x="year", y="priceperlb", kind="line", data=honey);
```
Answer: Yes, although there are some exceptions around 2003:

![line chart 1](../../../../3-Data-Visualization/12-visualization-relationships/images/line1.png)

✅ Seaborn aggregates data into one line, displaying "multiple measurements at each x value by plotting the mean and the 95% confidence interval around the mean." [Source](https://seaborn.pydata.org/tutorial/relational.html). You can disable this behavior by adding `ci=None`.

Question: In 2003, was there also a spike in honey supply? What happens if you examine total production year over year?

```python
sns.relplot(x="year", y="totalprod", kind="line", data=honey);
```

![line chart 2](../../../../3-Data-Visualization/12-visualization-relationships/images/line2.png)

Answer: Not really. Total production actually seems to have increased in 2003, even though honey production generally declined during these years.

Question: If not supply, what could have caused the price spike in 2003?

To investigate, let’s use a facet grid.

## Facet grids

Facet grids allow you to break down your dataset into smaller subsets (facets). For example, you can use 'year' as a facet to avoid creating too many grids. Seaborn can then plot each facet side by side for easier comparison. Does 2003 stand out in this comparison?

Create a facet grid using `relplot` as recommended in [Seaborn's documentation](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html?highlight=facetgrid#seaborn.FacetGrid).

```python
sns.relplot(
    data=honey, 
    x="yieldpercol", y="numcol",
    col="year", 
    col_wrap=3,
    kind="line"
```
In this visualization, you can compare yield per colony and number of colonies year over year, with columns wrapped at 3:

![facet grid](../../../../3-Data-Visualization/12-visualization-relationships/images/facet.png)

For this dataset, nothing particularly stands out regarding the number of colonies and their yield year over year or state by state. Is there another way to explore correlations between these variables?

## Dual-line Plots

Try a multiline plot by overlaying two line plots, using Seaborn's 'despine' to remove the top and right spines, and `ax.twinx` [from Matplotlib](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.twinx.html). Twinx allows you to share the x-axis while displaying two y-axes. Plot yield per colony and number of colonies together:

```python
fig, ax = plt.subplots(figsize=(12,6))
lineplot = sns.lineplot(x=honey['year'], y=honey['numcol'], data=honey, 
                        label = 'Number of bee colonies', legend=False)
sns.despine()
plt.ylabel('# colonies')
plt.title('Honey Production Year over Year');

ax2 = ax.twinx()
lineplot2 = sns.lineplot(x=honey['year'], y=honey['yieldpercol'], ax=ax2, color="r", 
                         label ='Yield per colony', legend=False) 
sns.despine(right=False)
plt.ylabel('colony yield')
ax.figure.legend();
```
![superimposed plots](../../../../3-Data-Visualization/12-visualization-relationships/images/dual-line.png)

While nothing particularly stands out around 2003, this visualization ends the lesson on a slightly positive note: although the number of colonies is declining overall, it seems to be stabilizing, even if their yield per colony is decreasing.

Go, bees, go!

🐝❤️
## 🚀 Challenge

In this lesson, you explored scatterplots, line grids, and facet grids. Challenge yourself to create a facet grid using a different dataset, perhaps one you’ve used in previous lessons. Pay attention to how long it takes to create and how to manage the number of grids effectively.

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ds/)

## Review & Self Study

Line plots can range from simple to complex. Spend some time reading the [Seaborn documentation](https://seaborn.pydata.org/generated/seaborn.lineplot.html) to learn about the various ways to build them. Try enhancing the line charts you created in this lesson using other methods from the documentation.

## Assignment

[Dive into the beehive](assignment.md)

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please note that automated translations may contain errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is recommended. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.