# Data Science in the Real World

| ![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-RealWorld.png) |
| :--------------------------------------------------------------------------------------------------------------: |
|               Data Science In The Real World - _Sketchnote by [@nitya](https://twitter.com/nitya)_               |

We're almost at the end of this learning journey!

We started with definitions of data science and ethics, explored various tools & techniques for data analysis and visualization, reviewed the data science lifecycle, and looked at scaling and automating data science workflows with cloud computing services. So, you're probably wondering: _"How exactly do I map all these learnings to real-world contexts?"_

In this lesson, we'll explore real-world applications of data science across industry and dive into specific examples in the research, digital humanities, and sustainability, contexts. We'll look at student project opportunities and conclude with useful resources to help you continue your learning journey!
## Pre-Lecture Quiz

[Pre-lecture quiz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/38)
## Data Science + Industry

Thanks to the democratization of AI, developers are now finding it easier to design and integrate AI-driven decision-making and data-driven insights into user experiences and development workflows. Here are a few examples of how data science is "applied" to real-world applications across the industry:

 * [Google Flu Trends](https://www.wired.com/2015/10/can-learn-epic-failure-google-flu-trends/) used data science to correlate search terms with flu trends. While the approach had flaws, it raised awareness of the possibilities (and challenges) of data-driven healthcare predictions.

 * [UPS Routing Predictions](https://www.technologyreview.com/2018/11/21/139000/how-ups-uses-ai-to-outsmart-bad-weather/) - explains how UPS uses data science and machine learning to predict optimal routes for delivery, taking into account weather conditions, traffic patterns, delivery deadlines and more.

 * [NYC Taxicab Route Visualization](http://chriswhong.github.io/nyctaxi/) - data gathered using [Freedom Of Information Laws](https://chriswhong.com/open-data/foil_nyc_taxi/) helped visualize a day in the life of NYC cabs, helping us understand how they navigate the busy city, the money they make, and the duration of trips over each 24-hour period.

 * [Uber Data Science Workbench](https://eng.uber.com/dsw/) - uses data (on pickup & dropoff locations, trip duration, preferred routes etc.) gathered from millions of uber trips *daily* to build a data analytics tool to help with pricing, safety, fraud detection and navigation decisions.

 * [Sports Analytics](https://towardsdatascience.com/scope-of-analytics-in-sports-world-37ed09c39860) - focuses on _predictive analytics_ (team and player analysis - think [Moneyball](https://datasciencedegree.wisconsin.edu/blog/moneyball-proves-importance-big-data-big-ideas/) - and fan management) and _data visualization_ (team & fan dashboards, games etc.) with applications like talent scouting, sports gambling and inventory/venue management.

 * [Data Science in Banking](https://data-flair.training/blogs/data-science-in-banking/) - highlights the value of data science in the finance industry with applications ranging from risk modeling and fraud detection, to customer segmentation, real-time prediction and recommender systems. Predictive analytics also drive critical measures like [credit scores](https://dzone.com/articles/using-big-data-and-predictive-analytics-for-credit).

 * [Data Science in Healthcare](https://data-flair.training/blogs/data-science-in-healthcare/) - highlights applications like medical imaging (e.g., MRI, X-Ray, CT-Scan), genomics (DNA sequencing), drug development (risk assessment, success prediction), predictive analytics (patient care & supply logistics), disease tracking & prevention etc.

![Data Science Applications in The Real World](./images/data-science-applications.png) Image Credit: [Data Flair: 6 Amazing Data Science Applications ](https://data-flair.training/blogs/data-science-applications/)

The figure shows other domains and examples for applying data science techniques. Want to explore other applications? Check out the [Review & Self Study](?id=review-amp-self-study) section below.

## Data Science + Research

| ![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-Research.png) |
| :---------------------------------------------------------------------------------------------------------------: |
|              Data Science & Research - _Sketchnote by [@nitya](https://twitter.com/nitya)_              |

While real-world applications often focus on industry use cases at scale, _research_ applications and projects can be useful from two perspectives:

* _innovation opportunities_ - explore rapid prototyping of advanced concepts and testing of user experiences for next-generation applications.
* _deployment challenges_ - investigate potential harms or unintended consequences of data science technologies in real-world contexts.

For students, these research projects can provide both learning and collaboration opportunities that can improve your understanding of the topic, and broaden your awareness and engagement with relevant people or teams working in areas of interest. So what do research projects look like and how can they make an impact?

Let's look at one example - the [MIT Gender Shades Study](http://gendershades.org/overview.html) from Joy Buolamwini (MIT Media Labs) with a [signature research paper](http://proceedings.mlr.press/v81/buolamwini18a/buolamwini18a.pdf) co-authored with Timnit Gebru (then at Microsoft Research) that focused on 

 * **What:** The objective of the research project was to _evaluate bias present in automated facial analysis algorithms and datasets_ based on gender and skin type. 
 * **Why:** Facial analysis is used in areas like law enforcement, airport security, hiring systems and more - contexts where inaccurate classifications (e.g., due to bias) can cause potential economic and social harms to affected individuals or groups. Understanding (and eliminating or mitigating) biases is key to fairness in usage.
 * **How:** Researchers recognized that existing benchmarks used predominantly lighter-skinned subjects, and curated a new data set (1000+ images) that was _more balanced_ by gender and skin type. The data set was used to evaluate the accuracy of three gender classification products (from Microsoft, IBM & Face++). 

Results showed that though overall classification accuracy was good, there was a noticeable difference in error rates between various subgroups - with **misgendering** being higher for females or persons with darker skin types, indicative of bias.

**Key Outcomes:** Raised awareness that data science needs more _representative datasets_ (balanced subgroups) and more _inclusive teams_ (diverse backgrounds) to recognize and eliminate or mitigate such biases earlier in AI solutions. Research efforts like this are also instrumental in many organizations defining principles and practices for _responsible AI_ to improve fairness across their AI products and processes.


**Want to learn about relevant research efforts in Microsoft?** 

* Check out [Microsoft Research Projects](https://www.microsoft.com/research/research-area/artificial-intelligence/?facet%5Btax%5D%5Bmsr-research-area%5D%5B%5D=13556&facet%5Btax%5D%5Bmsr-content-type%5D%5B%5D=msr-project) on Artificial Intelligence.
* Explore student projects from [Microsoft Research Data Science Summer School](https://www.microsoft.com/en-us/research/academic-program/data-science-summer-school/).
* Check out the [Fairlearn](https://fairlearn.org/) project and [Responsible AI](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1%3aprimaryr6) initiatives.



## Data Science + Humanities

| ![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-Humanities.png) |
| :---------------------------------------------------------------------------------------------------------------: |
|              Data Science & Digital Humanities - _Sketchnote by [@nitya](https://twitter.com/nitya)_              |


Digital Humanities [has been defined](https://digitalhumanities.stanford.edu/about-dh-stanford) as "a collection of practices and approaches combining computational methods with humanistic inquiry". [Stanford projects](https://digitalhumanities.stanford.edu/projects) like _"rebooting history"_ and _"poetic thinking"_ illustrate the linkage between [Digital Humanities and Data Science](https://digitalhumanities.stanford.edu/digital-humanities-and-data-science) - emphasizing techniques like network analysis, information visualization, spatial and text analysis that can help us revisit historical and literary data sets to derive new insights and perspective.

*Want to explore and extend a project in this space?*

Check out ["Emily Dickinson and the Meter of Mood"](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671) - a great example from [Jen Looper](https://twitter.com/jenlooper) that asks how we can use data science to revisit familiar poetry and re-evaluate its meaning and the contributions of its author in new contexts. For instance, _can we predict the season in which a poem was authored by analyzing its tone or sentiment_ - and what does this tell us about the author's state of mind over the relevant period?

To answer that question, we follow the steps of our data science lifecycle:
 * [`Data Acquisition`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#acquiring-the-dataset) - to collect a relevant dataset for analysis. Options including using an API ( e.g., [Poetry DB API](https://poetrydb.org/index.html)) or scraping web pages  (e.g., [Project Gutenberg](https://www.gutenberg.org/files/12242/12242-h/12242-h.htm)) using tools like [Scrapy](https://scrapy.org/).
 * [`Data Cleaning`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#clean-the-data) - explains how text can be formatted, sanitized and simplified using basic tools like Visual Studio Code and Microsoft Excel.
 * [`Data Analysis`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#working-with-the-data-in-a-notebook) - explains how we can now import the dataset into "Notebooks" for analysis using Python packages (like pandas, numpy and matplotlib) to organize and visualize the data.
 * [`Sentiment Analysis`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#sentiment-analysis-using-cognitive-services) - explains how we can integrate cloud services like Text Analytics, using low-code tools like [Power Automate](https://flow.microsoft.com/en-us/) for automated data processing workflows.

Using this workflow, we can explore the seasonal impacts on the sentiment of the poems, and help us fashion our own perspectives on the author. Try it out yourself - then extend the notebook to ask other questions or visualize the data in new ways!

> You can use some of the tools in the [Digital Humanities toolkit](https://github.com/Digital-Humanities-Toolkit) to pursue these avenues of inquiry


## Data Science + Sustainability

| ![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-Sustainability.png) |
| :---------------------------------------------------------------------------------------------------------------: |
|              Data Science & Sustainability - _Sketchnote by [@nitya](https://twitter.com/nitya)_              |

The [2030 Agenda For Sustainable Development](https://sdgs.un.org/2030agenda) - adopted by all United Nations members in 2015 - identifies 17 goals including ones that focus on **Protecting the Planet** from degradation and the impact of climate change. The [Microsoft Sustainability](https://www.microsoft.com/en-us/sustainability) initiative supports these goals by exploring ways in which technology solutions can support and build more sustainable futures with a [focus on 4 goals](https://dev.to/azure/a-visual-guide-to-sustainable-software-engineering-53hh) - being carbon negative, water positive, zero waste, and bio-diverse by 2030.

Tackling these challenges in a scalable and timely manner requires cloud-scale thinking - and large scale data. The [Planetary Computer](https://planetarycomputer.microsoft.com/) initiative provides 4 components to help data scientists and developers in this effort:
 
 * [Data Catalog](https://planetarycomputer.microsoft.com/catalog) - with petabytes of Earth Systems data (free & Azure-hosted).
 * [Planetary API](https://planetarycomputer.microsoft.com/docs/reference/stac/) - to help users search for relevant data across space and time.
 * [Hub](https://planetarycomputer.microsoft.com/docs/overview/environment/) - managed environment for scientists to process massive geospatial datasets.
 * [Applications](https://planetarycomputer.microsoft.com/applications) - showcase use cases & tools for sustainability insights.

**The Planetary Computer Project is currently in preview (as of Sep 2021)** - here's how you can get started contributing to sustainability solutions using data science.

* [Request access](https://planetarycomputer.microsoft.com/account/request) to start exploration and connect with peers.
* [Explore documentation](https://planetarycomputer.microsoft.com/docs/overview/about) to understand supported datasets and APIs.
* Explore applications like [Ecosystem Monitoring](https://analytics-lab.org/ecosystemmonitoring/) for inspiration on application ideas.
  
Think about how you can use data visualization to expose or amplify relevant insights into areas like climate change and deforestation. Or think about how insights can be used to create new user experiences that motivate behavioral changes for more sustainable living. 

## Data Science + Students

We've talked about real-world applications in industry and research, and explored data science application examples in digital humanities and sustainability. So how can you build your skills and share your expertise as data science beginners?

Here are some examples of data science student projects to inspire you.

 * [MSR Data Science Summer School](https://www.microsoft.com/en-us/research/academic-program/data-science-summer-school/#!projects) with GitHub [projects](https://github.com/msr-ds3) exploring topics like:
    - [Racial Bias in Police Use of Force](https://www.microsoft.com/en-us/research/video/data-science-summer-school-2019-replicating-an-empirical-analysis-of-racial-differences-in-police-use-of-force/) | [Github](https://github.com/msr-ds3/stop-question-frisk)
    - [Reliability of NYC Subway System](https://www.microsoft.com/en-us/research/video/data-science-summer-school-2018-exploring-the-reliability-of-the-nyc-subway-system/) | [Github](https://github.com/msr-ds3/nyctransit)
 * [Digitizing Material Culture: Exploring socio-economic distributions in Sirkap](https://claremont.maps.arcgis.com/apps/Cascade/index.html?appid=bdf2aef0f45a4674ba41cd373fa23afc)- from [Ornella Altunyan](https://twitter.com/ornelladotcom) and team at Claremont, using using [ArcGIS StoryMaps](https://storymaps.arcgis.com/).

## 🚀 Challenge

Search for articles that recommend data science projects that are beginner friendly - like [these 50 topic areas](https://www.upgrad.com/blog/data-science-project-ideas-topics-beginners/) or [these 21 project ideas](https://www.intellspot.com/data-science-project-ideas) or [these 16 projects with source code](https://data-flair.training/blogs/data-science-project-ideas/) that you can deconstruct and remix. And don't forget to blog about your learning journeys and share your insights with all of us.
## Post-Lecture Quiz

[Post-lecture quiz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/39)
## Review & Self Study

Want to explore more use cases? Here are a few relevant articles:
 * [17 Data Science Applications and Examples](https://builtin.com/data-science/data-science-applications-examples) - Jul 2021
 * [11 Breathtaking Data Science Applications in Real World](https://myblindbird.com/data-science-applications-real-world/) - May 2021
 * [Data Science In The Real World](https://towardsdatascience.com/data-science-in-the-real-world/home) - Article Collection
 * Data Science In: [Education](https://data-flair.training/blogs/data-science-in-education/), [Agriculture](https://data-flair.training/blogs/data-science-in-agriculture/), [Finance](https://data-flair.training/blogs/data-science-in-finance/), [Movies](https://data-flair.training/blogs/data-science-at-movies/) & more.
## Assignment

[Explore A Planetary Computer Dataset](assignment.md)
