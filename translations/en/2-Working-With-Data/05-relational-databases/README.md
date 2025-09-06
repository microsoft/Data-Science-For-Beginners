<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9399d7b4767e75068f95ce5c660b285c",
  "translation_date": "2025-09-06T10:06:30+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/README.md",
  "language_code": "en"
}
-->
# Working with Data: Relational Databases

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/05-RelationalData.png)|
|:---:|
| Working With Data: Relational Databases - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

Chances are you’ve used a spreadsheet before to store information. You had rows and columns, where the rows contained the data, and the columns described the data (sometimes called metadata). A relational database is based on this same principle of rows and columns in tables, but it allows you to spread information across multiple tables. This makes it possible to work with more complex data, avoid duplication, and have more flexibility in exploring the data. Let’s dive into the concepts of relational databases.

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ds/quiz/8)

## It all starts with tables

At the heart of a relational database are tables. Just like a spreadsheet, a table is a collection of rows and columns. The rows contain the data you want to work with, such as the name of a city or the amount of rainfall. The columns describe the type of data stored.

Let’s start by creating a table to store information about cities. We might begin with their name and country. You could store this in a table like this:

| City     | Country       |
| -------- | ------------- |
| Tokyo    | Japan         |
| Atlanta  | United States |
| Auckland | New Zealand   |

Notice that the column names **city**, **country**, and **population** describe the data being stored, and each row contains information about one city.

## The shortcomings of a single table approach

The table above probably looks familiar to you. Now let’s add more data to our growing database—annual rainfall (in millimeters). We’ll focus on the years 2018, 2019, and 2020. If we were to add this for Tokyo, it might look like this:

| City  | Country | Year | Amount |
| ----- | ------- | ---- | ------ |
| Tokyo | Japan   | 2020 | 1690   |
| Tokyo | Japan   | 2019 | 1874   |
| Tokyo | Japan   | 2018 | 1445   |

What do you notice about this table? You might see that we’re repeating the name and country of the city multiple times. This could take up a lot of storage and is unnecessary since Tokyo only has one name and country.

Let’s try another approach. Let’s add new columns for each year:

| City     | Country       | 2018 | 2019 | 2020 |
| -------- | ------------- | ---- | ---- | ---- |
| Tokyo    | Japan         | 1445 | 1874 | 1690 |
| Atlanta  | United States | 1779 | 1111 | 1683 |
| Auckland | New Zealand   | 1386 | 942  | 1176 |

While this avoids repeating rows, it introduces other challenges. We’d need to change the structure of the table every time a new year is added. Additionally, as the data grows, having years as columns would make it harder to retrieve and calculate values.

This is why we need multiple tables and relationships. By splitting the data into separate tables, we can avoid duplication and gain more flexibility in working with the data.

## The concepts of relationships

Let’s revisit our data and decide how to split it up. We know we want to store the name and country of each city, so this will work best in one table.

| City     | Country       |
| -------- | ------------- |
| Tokyo    | Japan         |
| Atlanta  | United States |
| Auckland | New Zealand   |

Before creating the next table, we need a way to reference each city. We need an identifier, ID, or (in database terms) a primary key. A primary key is a value used to uniquely identify a specific row in a table. While this could be based on an existing value (like the city name), it’s better to use a number or other identifier that won’t change. If the ID changes, it would break the relationship. In most cases, the primary key or ID is an auto-generated number.

> ✅ Primary key is often abbreviated as PK

### cities

| city_id | City     | Country       |
| ------- | -------- | ------------- |
| 1       | Tokyo    | Japan         |
| 2       | Atlanta  | United States |
| 3       | Auckland | New Zealand   |

> ✅ You’ll notice we use the terms "id" and "primary key" interchangeably in this lesson. These concepts also apply to DataFrames, which you’ll explore later. While DataFrames don’t use the term "primary key," they behave similarly.

With our cities table created, let’s store the rainfall data. Instead of repeating the full city information, we can use the ID. The new table should also have an *id* column, as all tables should have an ID or primary key.

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

Notice the **city_id** column in the **rainfall** table. This column contains values that reference the IDs in the **cities** table. In relational database terms, this is called a **foreign key**—a primary key from another table. You can think of it as a reference or pointer. **city_id** 1 refers to Tokyo.

> [!NOTE] Foreign key is often abbreviated as FK

## Retrieving the data

With our data split into two tables, you might wonder how to retrieve it. If you’re using a relational database like MySQL, SQL Server, or Oracle, you can use a language called Structured Query Language (SQL). SQL (sometimes pronounced "sequel") is a standard language for retrieving and modifying data in relational databases.

To retrieve data, you use the `SELECT` command. At its core, you **select** the columns you want to see **from** the table they’re in. For example, to display just the names of the cities, you could use:

```sql
SELECT city
FROM cities;

-- Output:
-- Tokyo
-- Atlanta
-- Auckland
```

`SELECT` lists the columns, and `FROM` specifies the table.

> [NOTE] SQL syntax is case-insensitive, meaning `select` and `SELECT` are the same. However, depending on the database, column and table names might be case-sensitive. It’s a best practice to treat everything in programming as case-sensitive. In SQL, it’s common to write keywords in all uppercase.

The query above will display all cities. If you only want to display cities in New Zealand, you need a filter. The SQL keyword for this is `WHERE`, which specifies a condition.

```sql
SELECT city
FROM cities
WHERE country = 'New Zealand';

-- Output:
-- Auckland
```

## Joining data

So far, we’ve retrieved data from a single table. Now we want to combine data from both **cities** and **rainfall**. This is done by *joining* the tables. You create a connection between the two tables by matching values in a column from each table.

In our example, we’ll match the **city_id** column in **rainfall** with the **city_id** column in **cities**. This will link the rainfall data to its respective city. The type of join we’ll use is called an *inner* join, which means rows that don’t match won’t be displayed. In our case, every city has rainfall data, so all rows will be displayed.

Let’s retrieve the rainfall data for 2019 for all cities.

We’ll do this step by step. First, join the tables by specifying the columns to connect—**city_id**.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
```

We’ve highlighted the columns we want and specified that we’re joining the tables by **city_id**. Now we can add the `WHERE` clause to filter for the year 2019.

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

Relational databases are built around dividing data into multiple tables, which can then be combined for display and analysis. This approach provides flexibility for calculations and data manipulation. You’ve learned the core concepts of relational databases and how to join two tables.

## 🚀 Challenge

There are many relational databases available online. Use the skills you’ve learned to explore the data.

## Post-Lecture Quiz

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ds/quiz/9)

## Review & Self Study

Microsoft Learn offers several resources to deepen your understanding of SQL and relational database concepts:

- [Describe concepts of relational data](https://docs.microsoft.com//learn/modules/describe-concepts-of-relational-data?WT.mc_id=academic-77958-bethanycheum)
- [Get Started Querying with Transact-SQL](https://docs.microsoft.com//learn/paths/get-started-querying-with-transact-sql?WT.mc_id=academic-77958-bethanycheum) (Transact-SQL is a version of SQL)
- [SQL content on Microsoft Learn](https://docs.microsoft.com/learn/browse/?products=azure-sql-database%2Csql-server&expanded=azure&WT.mc_id=academic-77958-bethanycheum)

## Assignment

[Assignment Title](assignment.md)

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.