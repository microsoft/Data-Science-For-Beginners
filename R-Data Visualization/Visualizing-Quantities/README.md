# Visualizing Quantities
<em> Sketchnote comes here </em>

In this lesson you will explore how to use the [ggplot2](https://cran.r-project.org/web/packages/ggplot2/index.html) package to create meaningful visualizations around the concept of quantity. Using a clean dataset about the number of [COVID-19 cases in the world](https://docs.microsoft.com/en-in/azure/open-datasets/dataset-bing-covid-19?tabs=azure-storage), you can make these visualizations and explore the trends of the COVID-19 numbers. This dataset has many variables including the number of confirmed, recovered and deceased cases all over the world from 21-01-2020 and is updated regularly.

## [Pre-lecture quiz](_) <em> yet to be linked </em>

## Observe COVID-19 trends with ggplot2
ggplot2 is a system for declaratively creating graphics, based on The Grammar of Graphics. The [Grammar of Graphics](https://en.wikipedia.org/wiki/Ggplot2) is a general scheme for data visualization which breaks up graphs into semantic components such as scales and layers. In other words, the ease of creating plots and graphs for univariate or multivariate data with little code makes ggplot2 the most popular package used for visualizations in R. The user tells ggplot2 how to map the variables to aesthetics, the graphical primitives to use, and ggplot2 takes care of the remaining.

> ✅ Plot = Data + Aesthetics + Geometry
> - Data refers to the dataset
> - Aesthetics indicate the variables to be studied (x and y variables)
> - Geometry refers to the type of plot (line plot, bar plot, etc.)

Choose the best geometry (type of plot) according to your data and the story you want to tell through the plot. 

> - To analyze trends: line, column
> - To compare values: bar, column, pie, scatterplot
> - To show how parts relate to a whole: pie
> - To show distribution of data: scatterplot, bar
> - To show relationships between values: line, scatterplot, bubble

✅ You can also checkout this descriptive [cheatsheet](https://nyu-cdsc.github.io/learningr/assets/data-visualization-2.1.pdf) for ggplot2.

## Build a line plot on the number of COVID-19 cases
In this section, you would be plotting a line graph to analyse the trends of the confirmed, recovered and deceased COVID-19 cases in the world.

Open the R console and import the dataset. 
> Note: The dataset is stored in the root of this repo in the `/data` folder.

Let's import the dataset and observe the head (top 5 rows) of the data.

```r
df_covid <- read.csv("../../data/covid.csv")
head(df_covid)
```
The head of the data has a mix of numbers and text:

|id|updated|confirmed|confirmed_change|deaths|deaths_change|recovered|recovered_change|load_time|
| ---: | :--------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :----------------- | --------: | 
|338995|21-01-2020|262|NA|0|NA|NA|NA|09:54.1|
|338996|22-01-2020|313|51|0|0|NA|NA|09:54.1|
|338997|23-01-2020|578|265|0|0|NA|NA|09:54.1|
|338998|24-01-2020|841|263|0|0|NA|NA|09:54.1|
|338999|25-01-2020|1320|479|0|0|NA|NA|09:54.1|

Let's start visualizing this data by plotting a line graph of the confirmed, deceased and the recovered cases.



