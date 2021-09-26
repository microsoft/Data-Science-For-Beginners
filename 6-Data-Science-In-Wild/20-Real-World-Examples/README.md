# Data Science in the Real World


|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-RealWorld.png)|
|:---:|
| Data Science In The Real World - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

We're almost at the end of this learning journey!

We started with definitions of data science and ethics, explored various tools & techniques for data analysis, reviewed the data science lifecycle, and looked at scaling and automating data science workflows with cloud computing services. 

And right now, you're probably wondering: "_How do these lessons translate to real-world contexts?_"

In this lesson, we'll talk about the real-world applications of data science and dive into a select few examples that explore data science in research, sustainability and digital humanities contexts. And we'll conclude with resources to help you continue the learning journey and explore some of these application ideas on your own.

## Where is Data Science Used Today?

Data Science technologies and techniques are finding a home in almost every industry today - thanks in no small part due to the democratization of AI, allowing developers to integrate data insights and decision-making intelligence into user experiences and workflows.

Here are some examples of "applied" data science in the real world:

 * [Google Flu Trends](https://www.wired.com/2015/10/can-learn-epic-failure-google-flu-trends/) used data science to correlate search terms with flu trends. While the approach had flaws, it raised awareness of the possibilities (and challenges) of data-driven healthcare predictions.

 * [UPS Routing Predictions](https://www.technologyreview.com/2018/11/21/139000/how-ups-uses-ai-to-outsmart-bad-weather/) - explains how UPS uses data science and machine learning to predict optimal routes for delivery, taking into account weather conditions, traffic patterns, delivery deadlines and more.

 * [NYC Taxicab Route Visualization](http://chriswhong.github.io/nyctaxi/) - data gathered using [Freedom Of Information Laws](https://chriswhong.com/open-data/foil_nyc_taxi/) helped visualize a day in the life of NYC cabs, helping us understand how they navigate the busy city, the money they make, and the duration of trips over each 24-hour period.

 * [Uber Data Science Workbench](https://eng.uber.com/dsw/) - uses data (on pickup & dropoff locations, trip duration, preferred routes etc.) gathered from millions of uber trips *daily* to build a data analytics tool to help with pricing, safety, fraud detection and navigation decisions.

 * [Sports Analytics](https://towardsdatascience.com/scope-of-analytics-in-sports-world-37ed09c39860) - focuses on _predictive analytics_ (team and player analysis - think [Moneyball](https://datasciencedegree.wisconsin.edu/blog/moneyball-proves-importance-big-data-big-ideas/) - and fan management) and _data visualization_ (team & fan dashboards, games etc.) with applications like talent scouting, sports gambling and inventory/venue management.

 * [Data Science in Banking](https://data-flair.training/blogs/data-science-in-banking/) - highlights the value of data science in the finance industry with applications ranging from risk modeling and fraud detction, to customer segmentation, real-time prediction and recommender systems. Predictive analytics also drive critical measures like [credit scores](https://dzone.com/articles/using-big-data-and-predictive-analytics-for-credit).

 * [Data Science in Healthcare](https://data-flair.training/blogs/data-science-in-healthcare/) - highlights applications like medical imaging (e.g., MRI, X-Ray, CT-Scan), genomics (DNA sequencing), drug development (risk assessment, success prediction), predictive analytics (patient care & supply logistics), disease tracking & prevention etc.

![Data Science Applications in The Real World](data-science-applications.png) Image Credit: [Data Flair: 6 Amazing Data Science Applications ](https://data-flair.training/blogs/data-science-applications/)

There are many other application domains to consider (see the image above as one example) - check out the [Review & Self Study](?id=review-amp-self-study) section for some relevant resources. For now, let's take a slightly deeper look at a few interesting examples in the following sections.


## Research: Gender Shades Study

Researchers are often the earliest members of the technical community to explore real-world applications for big data algorithms and applied AI. The focus is often on both _exploring opportunities_ to do good and _uncovering challenges_ that lead to potential harms or unintended consequences.

Let's talk about one example - the [Gender Shades](http://gendershades.org/overview.html) project from MIT, one of the earliest to explore data ethics topics like fairness and bias, to highlight the need for more transparency in algorithm design and AI, and demand more inclusive testing of products.

The project evaluated the accuracy of AI-powered _gender classification_ products (from companies like IBM, Microsoft and Face++) using a dataset of 1270 images (from African and European countries) as the benchmark. While overall accuracy of classification was high for all products, the study identified non-trivial differences in the error rates _between different groups of users_, with misgendering being higher for female subjects or those with darker skin. 

The study had broader implications for facial analysis algorithms as a whole, highlighting the potential for individual and social harms when used in contexts like law enforcement or hiring. Many organizations have since created _responsible AI_ principles and practices to improve the fairness of AI systems.


**Want to learn about relevant research efforts in Microsoft?** 

* Check out these [Microsoft Research Projects](https://www.microsoft.com/research/research-area/artificial-intelligence/?facet%5Btax%5D%5Bmsr-research-area%5D%5B%5D=13556&facet%5Btax%5D%5Bmsr-content-type%5D%5B%5D=msr-project)
* Explore student projects and coursework from the [Microsoft Research Data Science Summer School](https://www.microsoft.com/en-us/research/academic-program/data-science-summer-school/).
* Check out the [Fairlearn](https://fairlearn.org/) open-source, community-driven effort to improve fairness in AI systems.



## Digital Humanities: Poetics 

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-Humanities.png)|
|:---:|
| Data Science & Digital Humanities - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |


Digital Humanities [has been defined](https://digitalhumanities.stanford.edu/about-dh-stanford) as "a collection of practices and approaches combining computational methods with humanistic inquiry". [Stanford projects](https://digitalhumanities.stanford.edu/projects) like _"rebooting history"_ and _"poetic thinking"_ illustrate the linkage between [Digital Humanities and Data Science](https://digitalhumanities.stanford.edu/digital-humanities-and-data-science) - emphasizing techniques like network analysis, information visualization, spatial and text analysis that can help us revisit historical and literary data sets to derive new insights and perspective.

*Want to explore and extend a project in this space?*

Check out ["Emily Dickinson and the Meter of Mood"](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671) - a great example from [Jen Looper](https://twitter.com/jenlooper) that asks how we can use data science to revisit familiar poetry and re-evaluate its meaning and the contributions of its author in new contexts. For instance, _can we predict the year in which a poem was authored by analyzing its tone or sentiment_ - and what does this tell us about the author's state of mind over the relevant period?

To answer that question, we follow the steps of our data science lifecycle:
 * [`Data Acquisition`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#acquiring-the-dataset) - to collect a relevant dataset for analysis. Options including using an API ( e.g., [Poetry DB API](https://poetrydb.org/index.html)) or scraping web pages  (e.g., [Project Gutenberg](https://www.gutenberg.org/files/12242/12242-h/12242-h.htm)) using tools like [Scrapy](https://scrapy.org/).
 * [`Data Cleaning`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#clean-the-data) - explains how text can be formatted, sanitized and simplified using basic tools like Visual Studio Code and Microsoft Excel.
 * [`Data Analysis`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#working-with-the-data-in-a-notebook) - explains how we can now import the dataset into "Notebooks" for analysis using Python packages (like pandas, numpy and matplotlib) to organize and visualize the data.
 * [`Sentiment Analysis`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#sentiment-analysis-using-cognitive-services) - explains how we can integrate cloud services like Text Analytics, using low-code tools like [Power Automate](https://flow.microsoft.com/en-us/) for automated data processing workflows.

Using this workflow, we can explore the seasonal impacts on the sentiment of the poems, and help us fashion our own perspectives on the author. Try it out yourself - then extend the notebook to ask other questions or visualize the data in new ways!


## Sustainability: Planetary Data

The [2030 Agenda For Sustainable Development](https://sdgs.un.org/2030agenda) - adopted by all United Nations members in 2015 - identifies 17 goals including ones that focus on **Protecting the Planet** from degradation and the impact of climate change. The [Microsoft Sustainability](https://www.microsoft.com/en-us/sustainability) initiative supports these goals by exploring ways in which technology solutions can support and build more sustainable futures with a [focus on 4 goals](https://dev.to/azure/a-visual-guide-to-sustainable-software-engineering-53hh) - being carbon negative, water positive, zero waste, and bio-diverse by 2030.

Tackling these challenges in a scalable and timely manner requires cloud-scale thinking - and large scale data. That's where the [Planetary Computer](https://planetarycomputer.microsoft.com/) initiative. It consists of 4 components:
 
 * [Data Catalog](https://planetarycomputer.microsoft.com/catalog) - with petabytes of data on Earth systems, hosted on Azure, available for free.
 * [Planetary API](https://planetarycomputer.microsoft.com/docs/reference/stac/) - to help users search for relevant data across space and time.
 * [Hub](https://planetarycomputer.microsoft.com/docs/overview/environment/) - a managed environment for scientists to process massive geospatial datasets.
 * [Applications](https://planetarycomputer.microsoft.com/applications) - showcasing use cases and tools using this data, for sustainability insights.

Check out [the documentation](https://planetarycomputer.microsoft.com/docs/overview/about) for more details and explore applications like [Ecosystem Monitoring](https://analytics-lab.org/ecosystemmonitoring/) to get ideas for how you can use the data sets to derive useful insights or build applications that can motivate relevant behavioral changes for sustainability.

**The Planetary Computer Project is currently in preview (as of Sep 2021)** 

Please [request access](https://planetarycomputer.microsoft.com/account/request) to get started with your own exploration and connect with your peers in this space.


## Pre-Lecture Quiz

[Pre-lecture quiz]()

## 🚀 Challenge


## Post-Lecture Quiz

[Post-lecture quiz]()

## Review & Self Study

Want to explore more use cases? Here are a few relevant articles:
 * [17 Data Science Applications and Examples](https://builtin.com/data-science/data-science-applications-examples) - Jul 2021
 * [11 Breathtaking Data Science Applications in Real World](https://myblindbird.com/data-science-applications-real-world/) - May 2021
 * [Data Science In The Real World](https://towardsdatascience.com/data-science-in-the-real-world/home) - Article Collection
 * [Data Science In Education](https://data-flair.training/blogs/data-science-in-education/)
 * [Data Science In Agriculture](https://data-flair.training/blogs/data-science-in-agriculture/)
 * [Data Science in Finance](https://data-flair.training/blogs/data-science-in-finance/)
 * [Data Science at the Movies](https://data-flair.training/blogs/data-science-at-movies/)


## Assignment

[Assignment Title](assignment.md)
