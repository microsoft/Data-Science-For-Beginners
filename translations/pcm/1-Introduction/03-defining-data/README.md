# Defining Data

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/03-DefiningData.png)|
|:---:|
|Defining Data - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

Data na facts, information, observations and measurements dem wey people dey use find tori and take support better decisions. Data point na one unit data inside dataset, wey be kumpilation of data points. Datasets fit show for different formats and structures, and e go dey depend on where e come from. For example, company monthly income fit dey for spreadsheet but heart rate data wey dey comot from smartwatch fit dey for [JSON](https://stackoverflow.com/a/383699) format. E normal for data scientists to dey work with different kain data inside dataset. 

Dis lesson go focus on how to sabi and classify data based on how e be and where e come from.

## [Pre-Lecture Quiz](https://ff-quizzes.netlify.app/en/ds/quiz/4)
## How Data is Described

### Raw Data
Raw data na data wey just come from where e start and no don analyze or organize am. To fit understand wetin dey happen for dataset, e need to organize am so that people and technology fit understand am well and fit analyze am well. How dataset take arrange na im them dey call structure and e fit be structured, unstructured or semi-structured. Dis kain structure dey different based on where e come, but e go always fit inside these three tins. 

### Quantitative Data
Quantitative data na numbers wey dey show inside dataset and people fit analyze am, measure am and use am for maths. Example be population for country, person height or company money for quarter. With small extra analysis, quantitative data fit help know seasonal pattern for Air Quality Index (AQI) or estimate how e go be for rush hour traffic for normal work day.

### Qualitative Data
Qualitative data, wey dem also dey call categorical data, na data wey you no fit measure am like quantitative data. Na subjective data wey describe quality of product or process. Sometimes qualitative data fit get numbers but you no go use am for maths, like phone numbers or timestamps. Examples be video comments, car make and model or your friends favourite color. Qualitative data fit help understand which product people like or find out popular keywords for job resumes.

### Structured Data
Structured data na data wey arrange for rows and columns, each row get the same number columns. Columns dey represent type of value wey dey inside, and e get name to show wetin e mean, while rows get the real numbers. Columns get rule or restriction so the values go correct. For example, spreadsheet for customers wey each row get phone number and phone numbers no get alphabet. Dem fit get rule for phone column to make sure no empty and na numbers only. 

Good side of structured data be say you fit relate am to other structured data. But because e get special way wey you suppose arrange am, to change am fit hard. For example, if you wan add email column for customer spreadsheet wey no fit dey empty, you need plan how to put email address for rows wey already get customer data. 

Example of structured data: spreadsheets, relational databases, phone numbers, bank statements

### Unstructured Data
Unstructured data no too fit arrange for rows and columns, e no get particular format or rule. Because e no get many restriction, e easier to add new info than structured dataset. If sensor wey dey capture barometric pressure every 2 minutes get update to measure temperature, e no need change old data if e unstructured. But e fit make analysis or investigation of this data long pass. For example, scientist wey wan find average temperature for last month from sensor data, but find say sensor record "e" for some data to show say e spoil, no be normal number, so e mean data no complete.

Example of unstructured data: text files, text messages, video files

### Semi-structured
Semi-structured data get characteristics wey combine structured and unstructured data. E no dey arrange in rows and columns like structured but e get way wey people consider organized and e fit follow fixed format or rule. Structure go different base on source, from well arranged hierarchy to flexible way wey fit easily add new info. Metadata na signs wey help decide how data take arrange and store and get different names based on data type. Some metadata names na tags, elements, entities and attributes. For example, normal email get subject, body and recipients, and you fit arrange am based on who send am or when e send. 

Example of semi-structured data: HTML, CSV files, JavaScript Object Notation (JSON)

## Sources of Data 

Data source na the place wey data start from or where e "live" and e dey different depending on how and when dem collect am. Data wey user create na primary data, secondary data dey come from source wey collect am for general use. For example, group scientists collecting observation for rainforest na primary, but if dem share am with other scientists e go be secondary to people wey use am.

Databases popular source, dem use database management system host and manage data, users use commands called queries explore data. Files fit be audio, image, video and spreadsheets like Excel. Internet also be big place for data, where you go find databases and files. Application programming interfaces (APIs) help programmers create way to share data with outside users via internet. Web scraping na process to collect data from web page. [lessons in Working with Data](../../../../../../../../../2-Working-With-Data) dey show how to use different data sources. 

## Conclusion

For dis lesson we don learn:

- Wetin data be
- How people dey describe data
- How dem dey classify and categorize data
- Where you fit find data

## 🚀 Challenge

Kaggle na beta place to find open datasets. Use the [dataset search tool](https://www.kaggle.com/datasets) find some interesting datasets and classify 3-5 datasets with this criteria:

- Na quantitative or qualitative data?
- Na structured, unstructured or semi-structured data?

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ds/quiz/5)



## Review & Self Study

- Dis Microsoft Learn unit, wey dem title am [Identify data formats](https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats?pivots=text), get detailed explanation of structured, semi-structured and unstructured data.

## Assignment

[Classifying Datasets](assignment.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->