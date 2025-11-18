<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "80d80300002ef4e77cc7631d5904bd6e",
  "translation_date": "2025-11-18T18:23:26+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/README.md",
  "language_code": "pcm"
}
-->
# Work Wit Data: Relational Databases

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/05-RelationalData.png)|
|:---:|
| Work Wit Data: Relational Databases - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

E fit be say you don use spreadsheet before to store information. You go get rows and columns, where the rows go carry the information (or data), and the columns go describe wetin dey inside (sometimes dem dey call am metadata). Relational database dey build on top this idea of columns and rows for tables, wey go allow you spread information across plenty tables. This one go help you work wit more complex data, avoid repetition, and give you freedom to explore the data anyhow you like. Make we check wetin relational database mean.

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ds/quiz/8)

## E dey start wit tables

Relational database dey base on tables. Just like spreadsheet, table na collection of columns and rows. The row dey carry the data or information wey we wan work wit, like name of city or amount of rainfall. The columns dey describe the data wey dem dey store.

Make we start to explore by creating table to store information about cities. We fit start wit their name and country. You fit store am for table like this:

| City     | Country       |
| -------- | ------------- |
| Tokyo    | Japan         |
| Atlanta  | United States |
| Auckland | New Zealand   |

See as the column names **city**, **country** and **population** dey describe the data wey dem dey store, and each row get information about one city.

## The wahala of single table approach

E fit be say the table wey dey up dey familiar to you. Make we add more data to our small database - annual rainfall (for millimeters). We go focus on the years 2018, 2019 and 2020. If we wan add am for Tokyo, e go look like this:

| City  | Country | Year | Amount |
| ----- | ------- | ---- | ------ |
| Tokyo | Japan   | 2020 | 1690   |
| Tokyo | Japan   | 2019 | 1874   |
| Tokyo | Japan   | 2018 | 1445   |

Wetin you notice for our table? You fit notice say we dey repeat the name and country of the city again and again. This one fit take plenty storage, and e no dey necessary to get multiple copies. After all, Tokyo get only one name wey we dey interested in.

OK, make we try another way. Make we add new columns for each year:

| City     | Country       | 2018 | 2019 | 2020 |
| -------- | ------------- | ---- | ---- | ---- |
| Tokyo    | Japan         | 1445 | 1874 | 1690 |
| Atlanta  | United States | 1779 | 1111 | 1683 |
| Auckland | New Zealand   | 1386 | 942  | 1176 |

Even though this one avoid row repetition, e still get some wahala. We go need to change the structure of our table every time new year show. Plus, as our data dey grow, to use years as columns go make am hard to retrieve and calculate values.

Na why we need multiple tables and relationships. If we break our data apart, we fit avoid repetition and get more freedom to work wit our data.

## The idea of relationships

Make we go back to our data and decide how we wan split am. We sabi say we wan store the name and country for our cities, so e go make sense to put am for one table.

| City     | Country       |
| -------- | ------------- |
| Tokyo    | Japan         |
| Atlanta  | United States |
| Auckland | New Zealand   |

But before we create the next table, we need to figure out how we go take reference each city. We need something like identifier, ID or (for database terms) primary key. Primary key na value wey dem dey use to identify one specific row for table. Even though we fit use the name of the city, e better make we use number or another identifier. We no want make the id ever change because e go scatter the relationship. Most times, primary key or id dey auto-generated number.

> ✅ Primary key dey often short as PK

### cities

| city_id | City     | Country       |
| ------- | -------- | ------------- |
| 1       | Tokyo    | Japan         |
| 2       | Atlanta  | United States |
| 3       | Auckland | New Zealand   |

> ✅ You go notice say we dey use "id" and "primary key" interchangeably for this lesson. The idea still apply to DataFrames, wey you go learn later. DataFrames no dey use "primary key" name, but dem dey behave almost the same way.

Now we don create our cities table, make we store the rainfall. Instead of repeating the full information about the city, we fit use the id. We go also make sure say the new table get *id* column too, because all tables suppose get id or primary key.

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

See the **city_id** column inside the new **rainfall** table. This column get values wey dey reference the IDs for the **cities** table. For relational data terms, dem dey call this one **foreign key**; e be primary key from another table. You fit just think am as reference or pointer. **city_id** 1 dey point to Tokyo.

> [!NOTE] 
> Foreign key dey often short as FK

## How to retrieve the data

Now we don separate our data into two tables, you fit dey wonder how we go take retrieve am. If we dey use relational database like MySQL, SQL Server or Oracle, we fit use language wey dem dey call Structured Query Language or SQL. SQL (sometimes dem dey call am sequel) na standard language wey dem dey use to retrieve and modify data for relational database.

To retrieve data, you go use command `SELECT`. For the basic level, you go **select** the columns wey you wan see **from** the table wey dem dey. If you wan display only the names of the cities, you fit use this:

```sql
SELECT city
FROM cities;

-- Output:
-- Tokyo
-- Atlanta
-- Auckland
```

`SELECT` na where you go list the columns, and `FROM` na where you go list the tables.

> [!NOTE] 
> SQL syntax no dey case-sensitive, meaning `select` and `SELECT` mean the same thing. But, depending on the type of database wey you dey use, the columns and tables fit dey case-sensitive. So, e better make you always treat everything for programming like say e dey case-sensitive. When you dey write SQL queries, the common way na to put the keywords for all upper-case letters.

The query wey dey up go display all cities. Make we imagine say we wan display only cities wey dey New Zealand. We need filter. The SQL keyword for this one na `WHERE`, or "where something dey true".

```sql
SELECT city
FROM cities
WHERE country = 'New Zealand';

-- Output:
-- Auckland
```

## How to join data

So far, we don dey retrieve data from one table. Now we wan bring the data together from both **cities** and **rainfall**. This one dey happen by *joining* dem together. You go create connection between the two tables, and match the values from one column for each table.

For our example, we go match the **city_id** column for **rainfall** wit the **city_id** column for **cities**. This one go match the rainfall value wit the city wey e belong to. The type of join we go do na *inner* join, meaning if any row no match wit anything from the other table, e no go show. For our case, every city get rainfall, so everything go show.

Make we retrieve the rainfall for 2019 for all our cities.

We go do am step by step. The first step na to join the data together by showing the columns for the connection - **city_id** as we don talk before.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
```

We don highlight the two columns wey we want, and the fact say we wan join the tables together by the **city_id**. Now we fit add the `WHERE` statement to filter only year 2019.

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

Relational databases dey focus on dividing information between plenty tables wey dem go later bring back together for display and analysis. This one dey give plenty freedom to calculate and manipulate data. You don see the main ideas of relational database, and how to join two tables together.

## 🚀 Challenge

Plenty relational databases dey online. You fit explore the data by using the skills wey you don learn for here.

## Post-Lecture Quiz

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ds/quiz/9)

## Review & Self Study

Plenty resources dey for [Microsoft Learn](https://docs.microsoft.com/learn?WT.mc_id=academic-77958-bethanycheum) wey you fit use to continue your SQL and relational database journey.

- [Describe concepts of relational data](https://docs.microsoft.com//learn/modules/describe-concepts-of-relational-data?WT.mc_id=academic-77958-bethanycheum)
- [Get Started Querying with Transact-SQL](https://docs.microsoft.com//learn/paths/get-started-querying-with-transact-sql?WT.mc_id=academic-77958-bethanycheum) (Transact-SQL na one version of SQL)
- [SQL content on Microsoft Learn](https://docs.microsoft.com/learn/browse/?products=azure-sql-database%2Csql-server&expanded=azure&WT.mc_id=academic-77958-bethanycheum)

## Assignment

[Assignment Title](assignment.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis document don use AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) take translate am. Even though we dey try make sure say e correct, abeg no forget say automated translation fit get mistake or no dey accurate well. Di original document for di language wey dem write am first na im you suppose take as di main source. For important information, e good make you use professional human translation. We no go fit take responsibility for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->