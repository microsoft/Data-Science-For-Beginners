<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11739c7b40e7c6b16ad29e3df4e65862",
  "translation_date": "2025-12-19T12:39:15+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/README.md",
  "language_code": "pcm"
}
-->
# Working with Data: Relational Databases

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/05-RelationalData.png)|
|:---:|
| Working With Data: Relational Databases - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

Chances be say you don use spreadsheet before to store information. You get set of rows and columns, wey rows get the information (or data), and columns dey describe the information (sometimes dem dey call am metadata). Relational database na based on this main principle of columns and rows for tables, e dey allow you to get information wey spread for many tables. Dis one dey allow you work with more complex data, avoid duplication, and get flexibility for how you go explore the data. Make we explore the concepts of relational database.

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ds/quiz/8)

## E all dey start with tables

Relational database get tables for inside am. Just like spreadsheet, table na collection of columns and rows. Row get the data or information we want work with, like the name of city or how much rain fall. Columns dey describe the data wey dem store.

Make we start our exploration by starting table to store information about cities. We fit start with their name and country. You fit store am for table like this:

| City     | Country       |
| -------- | ------------- |
| Tokyo    | Japan         |
| Atlanta  | United States |
| Auckland | New Zealand   |

You go notice say the column names **city**, **country** and **population** dey describe the data wey dem dey store, and each row get information about one city.

## The shortcomings of a single table approach

Chances be say, the table wey dey above dey look familiar to you. Make we start add some more data to our growing database - annual rainfall (for millimeters). We go focus on years 2018, 2019 and 2020. If we wan add am for Tokyo, e fit look like this:

| City  | Country | Year | Amount |
| ----- | ------- | ---- | ------ |
| Tokyo | Japan   | 2020 | 1690   |
| Tokyo | Japan   | 2019 | 1874   |
| Tokyo | Japan   | 2018 | 1445   |

Wetin you notice for our table? You fit notice say we dey duplicate the name and country of the city again and again. That one fit take plenty storage, and e no really necessary to get many copies. After all, Tokyo get only one name wey we dey interested in.

OK, make we try another way. Make we add new columns for each year:

| City     | Country       | 2018 | 2019 | 2020 |
| -------- | ------------- | ---- | ---- | ---- |
| Tokyo    | Japan         | 1445 | 1874 | 1690 |
| Atlanta  | United States | 1779 | 1111 | 1683 |
| Auckland | New Zealand   | 1386 | 942  | 1176 |

Even though this one no dey duplicate rows, e get some other wahala. We go need change the structure of our table anytime new year show. Plus, as our data dey grow, to get years as columns go make am hard to retrieve and calculate values.

Na why we need many tables and relationships. If we break our data, we fit avoid duplication and get more flexibility for how we go work with our data.

## The concepts of relationships

Make we go back to our data and decide how we wan split am. We sabi say we wan store name and country for our cities, so this one go best for one table.

| City     | Country       |
| -------- | ------------- |
| Tokyo    | Japan         |
| Atlanta  | United States |
| Auckland | New Zealand   |

But before we create next table, we need find how to reference each city. We need some kind identifier, ID or (for technical database talk) primary key. Primary key na value wey dem use identify one specific row for table. Even though e fit be based on value itself (like city name), e suppose almost always be number or other identifier. We no want id to change because e go spoil the relationship. For most cases, primary key or id go be auto-generated number.

> ✅ Primary key dey often short as PK

### cities

| city_id | City     | Country       |
| ------- | -------- | ------------- |
| 1       | Tokyo    | Japan         |
| 2       | Atlanta  | United States |
| 3       | Auckland | New Zealand   |

> ✅ You go notice say we dey use "id" and "primary key" to mean the same thing for this lesson. The concepts here dey apply to DataFrames, wey you go explore later. DataFrames no dey use "primary key" term, but you go see say dem dey behave the same way.

With our cities table ready, make we store rainfall. Instead of duplicating full info about city, we fit use the id. We also need make sure the new table get *id* column too, because all tables suppose get id or primary key.

### rainfall

| rainfall_id | city_id | Year | Amount |
| ----------- | ------- | ---- | ------ |
| 1           | 1       | 2018 | 1445   |
| 2           | 1       | 2019 | 1874   |
| 3           | 1       | 2020 | 1690   |
| 4           | 2       | 2018 | 1779   |
| 5           | 2       | 2019 | 1111   |
| 6           | 2       | 2020 | 1683   |
| 7           | 3       | 2018 | 1386   |
| 8           | 3       | 2019 | 942    |
| 9           | 3       | 2020 | 1176   |

You go notice the **city_id** column inside the new **rainfall** table. This column get values wey dey reference the IDs for **cities** table. For technical relational data talk, this one na **foreign key**; na primary key from another table. You fit just think am as reference or pointer. **city_id** 1 dey reference Tokyo.

> [!NOTE] 
> Foreign key dey often short as FK

## Retrieving the data

With our data split into two tables, you fit dey wonder how we go take retrieve am. If we dey use relational database like MySQL, SQL Server or Oracle, we fit use language wey dem dey call Structured Query Language or SQL. SQL (sometimes dem dey pronounce am sequel) na standard language wey dem dey use to retrieve and change data for relational database.

To retrieve data you go use command `SELECT`. For inside, you **select** the columns wey you want see **from** the table wey dem dey. If you want show only the names of cities, you fit use this one:

```sql
SELECT city
FROM cities;

-- Output:
-- Tokyo
-- Atlanta
-- Auckland
```

`SELECT` na where you list the columns, and `FROM` na where you list the tables.

> [!NOTE] 
> SQL syntax no dey case-sensitive, meaning `select` and `SELECT` mean the same thing. But, depending on the type of database you dey use, columns and tables fit dey case sensitive. So, e good make you always treat everything for programming as if e dey case sensitive. When you dey write SQL queries, common way na to put keywords for all upper-case letters.

The query wey dey above go show all cities. Make we imagine say we want show only cities for New Zealand. We need some kind filter. The SQL keyword for this na `WHERE`, or "where something dey true".

```sql
SELECT city
FROM cities
WHERE country = 'New Zealand';

-- Output:
-- Auckland
```

## Joining data

Until now, we don dey retrieve data from one table. Now we want join data from both **cities** and **rainfall**. This one na *joining* them together. You go create seam between the two tables, and match values from column from each table.

For our example, we go match **city_id** column for **rainfall** with **city_id** column for **cities**. This one go match rainfall value with the correct city. The kind join we go do na *inner* join, meaning if any rows no match anything from the other table, dem no go show am. For our case, every city get rainfall, so everything go show.

Make we retrieve rainfall for 2019 for all our cities.

We go do am step by step. First step na to join data together by showing the columns for the seam - **city_id** as we highlight before.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
```

We don highlight the two columns we want, and say we want join tables together by **city_id**. Now we fit add `WHERE` statement to filter only year 2019.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
WHERE rainfall.year = 2019

-- Output

-- city     | amount
-- -------- | ------
-- Tokyo    | 1874
-- Atlanta  | 1111
-- Auckland |  942
```

## Summary

Relational databases dey focus on dividing information between many tables wey dem go bring back together for display and analysis. This one dey give plenty flexibility to do calculations and manipulate data. You don see the main concepts of relational database, and how to do join between two tables.

## 🚀 Challenge

Plenty relational databases dey internet. You fit explore data by using the skills wey you don learn above.

## Post-Lecture Quiz

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ds/quiz/9)

## Review & Self Study

Plenty resources dey for [Microsoft Learn](https://docs.microsoft.com/learn?WT.mc_id=academic-77958-bethanycheum) to help you continue your exploration of SQL and relational database concepts

- [Describe concepts of relational data](https://docs.microsoft.com//learn/modules/describe-concepts-of-relational-data?WT.mc_id=academic-77958-bethanycheum)
- [Get Started Querying with Transact-SQL](https://docs.microsoft.com//learn/paths/get-started-querying-with-transact-sql?WT.mc_id=academic-77958-bethanycheum) (Transact-SQL na version of SQL)
- [SQL content on Microsoft Learn](https://docs.microsoft.com/learn/browse/?products=azure-sql-database%2Csql-server&expanded=azure&WT.mc_id=academic-77958-bethanycheum)

## Assignment

[Displaying airport data](assignment.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even though we dey try make am correct, abeg sabi say automated translation fit get some errors or mistakes. Di original document wey dey im own language na di correct one. If na serious matter, e better make human professional translate am. We no go responsible for any misunderstanding or wrong meaning wey fit come from dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->