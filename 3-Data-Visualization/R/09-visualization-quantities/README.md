# Visualizing Quantities
|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/sketchnotes/09-Visualizing-Quantities.png)|
|:---:|
| Visualizing Quantities - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

In this lesson you will explore how to use some of the many available R packages libraries to learn how to create interesting visualizations all around the concept of quantity. Using a cleaned dataset about the birds of Minnesota, you can learn many interesting facts about local wildlife. 
## [Pre-lecture quiz]() TO BE LINKED

## Observe wingspan with ggplot2
An excellent library to create both simple and sophisticated plots and charts of various kinds is [ggplot2](https://cran.r-project.org/web/packages/ggplot2/index.html). In general terms, the process of plotting data using these libraries includes identifying the parts of your dataframe that you want to target, performing any transforms on that data necessary, assigning its x and y axis values, deciding what kind of plot to show, and then showing the plot.

`ggplot2` is a system for declaratively creating graphics, based on The Grammar of Graphics. The [Grammar of Graphics](https://en.wikipedia.org/wiki/Ggplot2) is a general scheme for data visualization which breaks up graphs into semantic components such as scales and layers. In other words, the ease of creating plots and graphs for univariate or multivariate data with little code makes `ggplot2` the most popular package used for visualizations in R. The user tells `ggplot2` how to map the variables to aesthetics, the graphical primitives to use, and `ggplot2` takes care of the remaining.

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

## Build a line plot about bird wingspan values

Open the R console and import the dataset. 
> Note: The dataset is stored in the root of this repo in the `/data` folder.

Let's import the dataset and observe the head (top 5 rows) of the data.

```r
birds <- read.csv("../../data/birds.csv",fileEncoding="UTF-8-BOM")
head(birds)
```
The head of the data has a mix of text and numbers:

|      | Name                         | ScientificName         | Category              | Order        | Family   | Genus       | ConservationStatus | MinLength | MaxLength | MinBodyMass | MaxBodyMass | MinWingspan | MaxWingspan |
| ---: | :--------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :----------------- | --------: | --------: | ----------: | ----------: | ----------: | ----------: |
|    0 | Black-bellied whistling-duck | Dendrocygna autumnalis | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Dendrocygna | LC                 |        47 |        56 |         652 |        1020 |          76 |          94 |
|    1 | Fulvous whistling-duck       | Dendrocygna bicolor    | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Dendrocygna | LC                 |        45 |        53 |         712 |        1050 |          85 |          93 |
|    2 | Snow goose                   | Anser caerulescens     | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Anser       | LC                 |        64 |        79 |        2050 |        4050 |         135 |         165 |
|    3 | Ross's goose                 | Anser rossii           | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Anser       | LC                 |      57.3 |        64 |        1066 |        1567 |         113 |         116 |
|    4 | Greater white-fronted goose  | Anser albifrons        | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Anser       | LC                 |        64 |        81 |        1930 |        3310 |         130 |         165 |

Let's start by plotting some of the numeric data using a basic line plot. Suppose you wanted a view of the maximum wingspan for these interesting birds.

```r
install.packages("ggplot2")
library("ggplot2")
ggplot(data=birds, aes(x=Name, y=MaxWingspan,group=1))
+     geom_line()
+     theme(axis.text.x = element_text(angle = 45, hjust=1))
+     xlab("Birds")
+     ylab("Wingspan (CM)") +
+     ggtitle("Max Wingspan in Centimeters")

```
