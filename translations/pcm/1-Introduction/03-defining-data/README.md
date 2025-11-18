<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "12339119c0165da569a93ddba05f9339",
  "translation_date": "2025-11-18T18:31:43+00:00",
  "source_file": "1-Introduction/03-defining-data/README.md",
  "language_code": "pcm"
}
-->
# Defining Data

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/03-DefiningData.png)|
|:---:|
|Defining Data - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

Data na facts, information, wetin person observe and measure wey dem dey use to make discovery and take make better decision. One data point na one single unit of data wey dey inside dataset, wey be collection of data points. Datasets fit dey for different formats and structure, and e go usually depend on where e come from or the source of the data. For example, one company monthly earnings fit dey for spreadsheet but hourly heart rate data from smartwatch fit dey for [JSON](https://stackoverflow.com/a/383699) format. E dey normal for data scientists to dey work with different types of data inside one dataset.

This lesson go focus on how to identify and classify data based on e characteristics and e source.

## [Pre-Lecture Quiz](https://ff-quizzes.netlify.app/en/ds/quiz/4)
## How Data dey Described

### Raw Data
Raw data na data wey come from e source as e be originally and dem never analyze or arrange am. To fit understand wetin dey happen for one dataset, dem go need arrange am for format wey humans and the technology wey dem dey use fit understand. The structure of dataset dey describe how dem arrange am and e fit dey classified as structured, unstructured, and semi-structured. This type of structure go depend on the source but e go still fall under these three categories.

### Quantitative Data
Quantitative data na numbers wey dem observe inside dataset and e fit dey analyzed, measured, and used mathematically. Some example of quantitative data na: population of one country, height of one person, or quarterly earnings of one company. If dem analyze quantitative data well, e fit help discover seasonal trends for Air Quality Index (AQI) or estimate the chance of rush hour traffic for normal work day.

### Qualitative Data
Qualitative data, wey people dey also call categorical data, na data wey person no fit measure like quantitative data. E dey usually be different formats of data wey dey capture the quality of something, like product or process. Sometimes, qualitative data fit be numbers but e no dey used mathematically, like phone numbers or timestamps. Some example of qualitative data na: video comments, the make and model of one car, or your close friends favorite color. Qualitative data fit help understand which product customers like pass or identify popular keywords for job application resumes.

### Structured Data
Structured data na data wey dem arrange for rows and columns, where each row go get the same set of columns. Columns dey represent value of one particular type and dem go get name wey dey describe wetin the value mean, while rows dey carry the actual values. Columns go often get specific rules or restrictions for the values to make sure say the values dey represent the column well. For example, imagine one spreadsheet of customers where each row must get phone number and the phone numbers no fit get alphabetical characters. Dem fit put rules for the phone number column to make sure say e no dey empty and e only get numbers.

One benefit of structured data na say e fit dey arranged in way wey e fit relate to other structured data. But because the data dey designed to dey arranged in specific way, to change the overall structure fit take plenty effort. For example, if you wan add email column to the customer spreadsheet wey no fit dey empty, you go need figure out how you go take add these values to the existing rows of customers for the dataset.

Examples of structured data: spreadsheets, relational databases, phone numbers, bank statements

### Unstructured Data
Unstructured data no dey fit categorize into rows or columns and e no get format or set of rules to follow. Because unstructured data no get plenty restrictions for e structure, e dey easier to add new information compared to structured dataset. If one sensor wey dey capture data for barometric pressure every 2 minutes don get update wey go allow am measure and record temperature, e no go need change the existing data if e dey unstructured. But this fit make analyzing or investigating this type of data take longer. For example, one scientist wey wan find the average temperature of the previous month from the sensor data fit discover say the sensor record "e" for some of e data to show say e spoil instead of normal number, wey mean say the data no complete.

Examples of unstructured data: text files, text messages, video files

### Semi-structured
Semi-structured data get features wey make am be mix of structured and unstructured data. E no dey usually follow format of rows and columns but e dey arranged in way wey dem fit call structured and e fit follow fixed format or set of rules. The structure go vary between sources, like well-defined hierarchy to something wey dey more flexible wey go allow easy integration of new information. Metadata na indicators wey dey help decide how dem go arrange and store the data and e go get different names based on the type of data. Some common names for metadata na tags, elements, entities, and attributes. For example, one typical email message go get subject, body, and set of recipients and e fit dey arranged by who or when dem send am.

Examples of semi-structured data: HTML, CSV files, JavaScript Object Notation (JSON)

## Sources of Data 

Data source na the original place where the data dey come from or where e "live" and e go vary based on how and when dem collect am. Data wey e user(s) generate na primary data while secondary data dey come from source wey don collect data for general use. For example, one group of scientists wey dey collect observations for rainforest go be primary and if dem decide to share am with other scientists, e go be secondary to those wey dey use am.

Databases na common source and dem dey rely on database management system to host and maintain the data where users dey use commands wey dem dey call queries to explore the data. Files as data sources fit be audio, image, and video files as well as spreadsheets like Excel. Internet sources na common place wey dem dey host data, where databases and files fit dey. Application programming interfaces, wey people dey call APIs, dey allow programmers create ways to share data with external users through internet, while the process of web scraping dey extract data from web page. The [lessons in Working with Data](../../../../../../../../../2-Working-With-Data) dey focus on how to use different data sources.

## Conclusion

For this lesson we don learn:

- Wetin data be
- How dem dey describe data
- How dem dey classify and categorize data
- Where dem fit find data

## 🚀 Challenge

Kaggle na better place to find open datasets. Use the [dataset search tool](https://www.kaggle.com/datasets) to find some interesting datasets and classify 3-5 datasets with this criteria:

- The data na quantitative or qualitative?
- The data na structured, unstructured, or semi-structured?

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ds/quiz/5)



## Review & Self Study

- This Microsoft Learn unit, wey dem title [Classify your Data](https://docs.microsoft.com/en-us/learn/modules/choose-storage-approach-in-azure/2-classify-data) get detailed breakdown of structured, semi-structured, and unstructured data.

## Assignment

[Classifying Datasets](assignment.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI transleto service [Co-op Translator](https://github.com/Azure/co-op-translator) do di translation. Even though we dey try make am accurate, abeg sabi say machine translation fit get mistake or no dey correct well. Di original dokyument wey dey for im native language na di main source wey you go trust. For important information, e better make professional human transleto check am. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->