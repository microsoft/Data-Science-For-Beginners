<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a33c5d4b4156a2b41788d8720b6f724c",
  "translation_date": "2025-08-31T11:03:47+00:00",
  "source_file": "3-Data-Visualization/R/12-visualization-relationships/README.md",
  "language_code": "en"
}
-->
# Visualizing Relationships: All About Honey 🍯

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../../sketchnotes/12-Visualizing-Relationships.png)|
|:---:|
|Visualizing Relationships - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

Continuing with the nature focus of our research, let's explore fascinating ways to visualize the relationships between different types of honey, based on a dataset from the [United States Department of Agriculture](https://www.nass.usda.gov/About_NASS/index.php).

This dataset, containing around 600 entries, showcases honey production across various U.S. states. For instance, it includes data on the number of colonies, yield per colony, total production, stocks, price per pound, and the value of honey produced in each state from 1998 to 2012, with one row per year for each state.

It would be intriguing to visualize the relationship between a state's annual production and, for example, the price of honey in that state. Alternatively, you could examine the relationship between honey yield per colony across states. This time period also includes the emergence of the devastating 'CCD' or 'Colony Collapse Disorder' first observed in 2006 (http://npic.orst.edu/envir/ccd.html), making this dataset particularly meaningful to study. 🐝

## [Pre-lecture quiz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/22)

In this lesson, you'll use ggplot2, a library you've worked with before, to visualize relationships between variables. One of the highlights of ggplot2 is its `geom_point` and `qplot` functions, which allow you to create scatter plots and line plots to quickly visualize '[statistical relationships](https://ggplot2.tidyverse.org/)'. These tools help data scientists better understand how variables interact with one another.

## Scatterplots

Use a scatterplot to illustrate how the price of honey has changed year over year in each state. ggplot2, with its `ggplot` and `geom_point` functions, makes it easy to group state data and display data points for both categorical and numeric variables.

Let's begin by importing the data and Seaborn:

```r
honey=read.csv('../../data/honey.csv')
head(honey)
```
You'll notice that the honey dataset contains several interesting columns, including year and price per pound. Let's explore this data, grouped by U.S. state:

| state | numcol | yieldpercol | totalprod | stocks   | priceperlb | prodvalue | year |
| ----- | ------ | ----------- | --------- | -------- | ---------- | --------- | ---- |
| AL    | 16000  | 71          | 1136000   | 159000   | 0.72       | 818000    | 1998 |
| AZ    | 55000  | 60          | 3300000   | 1485000  | 0.64       | 2112000   | 1998 |
| AR    | 53000  | 65          | 3445000   | 1688000  | 0.59       | 2033000   | 1998 |
| CA    | 450000 | 83          | 37350000  | 12326000 | 0.62       | 23157000  | 1998 |
| CO    | 27000  | 72          | 1944000   | 1594000  | 0.7        | 1361000   | 1998 |
| FL    | 230000 | 98          |22540000   | 4508000  | 0.64       | 14426000  | 1998 |

Create a basic scatterplot to show the relationship between the price per pound of honey and its U.S. state of origin. Adjust the `y` axis to ensure all states are visible:

```r
library(ggplot2)
ggplot(honey, aes(x = priceperlb, y = state)) +
  geom_point(colour = "blue")
```
![scatterplot 1](../../../../../3-Data-Visualization/R/12-visualization-relationships/images/scatter1.png)

Next, use a honey-inspired color scheme to visualize how the price changes over the years. You can achieve this by adding the 'scale_color_gradientn' parameter to highlight year-over-year changes:

> ✅ Learn more about the [scale_color_gradientn](https://www.rdocumentation.org/packages/ggplot2/versions/0.9.1/topics/scale_colour_gradientn) - try a beautiful rainbow color scheme!

```r
ggplot(honey, aes(x = priceperlb, y = state, color=year)) +
  geom_point()+scale_color_gradientn(colours = colorspace::heat_hcl(7))
```
![scatterplot 2](../../../../../3-Data-Visualization/R/12-visualization-relationships/images/scatter2.png)

With this color scheme, you can clearly see a strong upward trend in honey prices over the years. If you examine a specific state, such as Arizona, you'll notice a consistent pattern of price increases year over year, with only a few exceptions:

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

Another way to visualize this trend is by using size instead of color. For colorblind users, this might be a better option. Modify your visualization to represent price increases with larger dot sizes:

```r
ggplot(honey, aes(x = priceperlb, y = state)) +
  geom_point(aes(size = year),colour = "blue") +
  scale_size_continuous(range = c(0.25, 3))
```
You can observe the dots growing larger over time.

![scatterplot 3](../../../../../3-Data-Visualization/R/12-visualization-relationships/images/scatter3.png)

Is this simply a case of supply and demand? Could factors like climate change and colony collapse be reducing honey availability year over year, leading to price increases?

To investigate correlations between variables in this dataset, let's explore line charts.

## Line charts

Question: Is there a clear upward trend in honey prices per pound year over year? The simplest way to find out is by creating a single line chart:

```r
qplot(honey$year,honey$priceperlb, geom='smooth', span =0.5, xlab = "year",ylab = "priceperlb")
```
Answer: Yes, although there are some exceptions around 2003:

![line chart 1](../../../../../3-Data-Visualization/R/12-visualization-relationships/images/line1.png)

Question: In 2003, can we also observe a spike in honey supply? What happens if you examine total production year over year?

```python
qplot(honey$year,honey$totalprod, geom='smooth', span =0.5, xlab = "year",ylab = "totalprod")
```

![line chart 2](../../../../../3-Data-Visualization/R/12-visualization-relationships/images/line2.png)

Answer: Not really. Total production seems to have increased in 2003, even though overall honey production appears to be declining during these years.

Question: In that case, what might have caused the spike in honey prices around 2003?

To explore this, let's use a facet grid.

## Facet grids

Facet grids allow you to focus on one aspect of your dataset (e.g., 'year') and create a plot for each facet based on your chosen x and y coordinates. This makes comparisons easier. Does 2003 stand out in this type of visualization?

Create a facet grid using `facet_wrap` as recommended by [ggplot2's documentation](https://ggplot2.tidyverse.org/reference/facet_wrap.html).

```r
ggplot(honey, aes(x=yieldpercol, y = numcol,group = 1)) + 
  geom_line() + facet_wrap(vars(year))
```
In this visualization, you can compare yield per colony and number of colonies year over year, with a wrap set at 3 columns:

![facet grid](../../../../../3-Data-Visualization/R/12-visualization-relationships/images/facet.png)

For this dataset, nothing particularly stands out regarding the number of colonies and their yield year over year or state by state. Is there another way to identify correlations between these two variables?

## Dual-line Plots

Try a multiline plot by overlaying two line plots using R's `par` and `plot` functions. Plot the year on the x-axis and display two y-axes: yield per colony and number of colonies, superimposed:

```r
par(mar = c(5, 4, 4, 4) + 0.3)              
plot(honey$year, honey$numcol, pch = 16, col = 2,type="l")              
par(new = TRUE)                             
plot(honey$year, honey$yieldpercol, pch = 17, col = 3,              
     axes = FALSE, xlab = "", ylab = "",type="l")
axis(side = 4, at = pretty(range(y2)))      
mtext("colony yield", side = 4, line = 3)   
```
![superimposed plots](../../../../../3-Data-Visualization/R/12-visualization-relationships/images/dual-line.png)

While nothing significant stands out around 2003, this visualization ends the lesson on a slightly positive note: although the number of colonies is declining overall, it appears to be stabilizing, even if their yield per colony is decreasing.

Go, bees, go!

🐝❤️
## 🚀 Challenge

In this lesson, you learned more about scatterplots and line grids, including facet grids. Challenge yourself to create a facet grid using a different dataset, perhaps one you've used in previous lessons. Note how long it takes to create and consider how many grids are practical to draw using these techniques.

## [Post-lecture quiz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/23)

## Review & Self Study

Line plots can range from simple to complex. Spend some time reading the [ggplot2 documentation](https://ggplot2.tidyverse.org/reference/geom_path.html#:~:text=geom_line()%20connects%20them%20in,which%20cases%20are%20connected%20together) to learn about the various ways to build them. Try enhancing the line charts you created in this lesson using other methods described in the documentation.

## Assignment

[Dive into the beehive](assignment.md)

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.