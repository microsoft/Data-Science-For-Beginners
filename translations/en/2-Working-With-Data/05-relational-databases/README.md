<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "870a0086adbc313a8eea5489bdcb2522",
  "translation_date": "2025-08-31T10:58:39+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/README.md",
  "language_code": "en"
}
-->
# Working with Data: Relational Databases

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/05-RelationalData.png)|
|:---:|
| Working With Data: Relational Databases - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

You’ve probably used a spreadsheet before to store information. It consists of rows and columns, where the rows hold the data and the columns describe the data (sometimes referred to as metadata). A relational database builds on this concept of rows and columns in tables, enabling you to spread information across multiple tables. This approach allows you to work with more complex data, reduce duplication, and gain flexibility in how you analyze the data. Let’s dive into the basics of relational databases.

## [Pre-lecture quiz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/8)

## It all starts with tables

At the heart of a relational database are tables. Similar to a spreadsheet, a table is a collection of rows and columns. Rows contain the data you want to work with, such as the name of a city or the amount of rainfall, while columns describe the type of data stored.

Let’s start by creating a table to store information about cities. For example, we might want to store their name and country. This could look like the following table:

| City     | Country       |
| -------- | ------------- |
| Tokyo    | Japan         |
| Atlanta  | United States |
| Auckland | New Zealand   |

Notice how the column names **city**, **country**, and **population** describe the data being stored, and each row contains information about a specific city.

## The shortcomings of a single table approach

The table above might look familiar to you. Now, let’s add more data to our growing database—annual rainfall (in millimeters) for the years 2018, 2019, and 2020. If we were to add this data for Tokyo, it might look like this:

| City  | Country | Year | Amount |
| ----- | ------- | ---- | ------ |
| Tokyo | Japan   | 2020 | 1690   |
| Tokyo | Japan   | 2019 | 1874   |
| Tokyo | Japan   | 2018 | 1445   |

What do you notice about this table? You might see that we’re repeating the name and country of the city multiple times. This repetition can take up unnecessary storage space. After all, Tokyo only has one name and one country.

Let’s try a different approach by adding new columns for each year:

| City     | Country       | 2018 | 2019 | 2020 |
| -------- | ------------- | ---- | ---- | ---- |
| Tokyo    | Japan         | 1445 | 1874 | 1690 |
| Atlanta  | United States | 1779 | 1111 | 1683 |
| Auckland | New Zealand   | 1386 | 942  | 1176 |

While this eliminates row duplication, it introduces other challenges. For instance, we’d need to modify the table structure every time a new year is added. Additionally, as the dataset grows, having years as columns makes it harder to retrieve and calculate values.

This is why relational databases use multiple tables and relationships. By breaking data into separate tables, we can avoid duplication and gain more flexibility in how we work with the data.

## The concepts of relationships

Let’s revisit our data and decide how to split it into multiple tables. We know we want to store the name and country of each city, so this information can go into one table:

| City     | Country       |
| -------- | ------------- |
| Tokyo    | Japan         |
| Atlanta  | United States |
| Auckland | New Zealand   |

Before creating the next table, we need a way to reference each city. This requires an identifier, often called an ID or, in database terminology, a primary key. A primary key is a unique value used to identify a specific row in a table. While we could use the city name as the identifier, it’s better to use a number or another unique value that won’t change. Most primary keys are auto-generated numbers.

> ✅ Primary key is often abbreviated as PK

### cities

| city_id | City     | Country       |
| ------- | -------- | ------------- |
| 1       | Tokyo    | Japan         |
| 2       | Atlanta  | United States |
| 3       | Auckland | New Zealand   |

> ✅ Throughout this lesson, you’ll notice we use the terms "id" and "primary key" interchangeably. These concepts also apply to DataFrames, which you’ll explore later. While DataFrames don’t use the term "primary key," they function similarly.

With our cities table created, let’s store the rainfall data. Instead of duplicating city information, we can use the city ID. The new table should also have its own ID or primary key.

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

Notice the **city_id** column in the **rainfall** table. This column contains values that reference the IDs in the **cities** table. In relational database terms, this is called a **foreign key**—a primary key from another table. You can think of it as a reference or pointer. For example, **city_id** 1 refers to Tokyo.

> [!NOTE] Foreign key is often abbreviated as FK

## Retrieving the data

With our data split into two tables, you might wonder how to retrieve it. Relational databases like MySQL, SQL Server, or Oracle use a language called Structured Query Language (SQL) for this purpose. SQL (sometimes pronounced "sequel") is a standard language for retrieving and modifying data in relational databases.

To retrieve data, you use the `SELECT` command. Essentially, you **select** the columns you want to view **from** the table they belong to. For example, to display just the names of the cities, you could use the following:

```sql
SELECT city
FROM cities;

-- Output:
-- Tokyo
-- Atlanta
-- Auckland
```

`SELECT` specifies the columns, and `FROM` specifies the table.

> [NOTE] SQL syntax is case-insensitive, meaning `select` and `SELECT` are treated the same. However, depending on the database, column and table names might be case-sensitive. As a best practice, always treat everything in programming as case-sensitive. In SQL, it’s common to write keywords in uppercase.

The query above will display all cities. If you only want to display cities in New Zealand, you can use a filter. The SQL keyword for filtering is `WHERE`, which specifies conditions.

```sql
SELECT city
FROM cities
WHERE country = 'New Zealand';

-- Output:
-- Auckland
```

## Joining data

So far, we’ve retrieved data from a single table. Now, let’s combine data from both **cities** and **rainfall**. This is done by *joining* the tables. Essentially, you create a connection between the two tables by matching values in specific columns.

In our example, we’ll match the **city_id** column in **rainfall** with the **city_id** column in **cities**. This will link rainfall data to its corresponding city. The type of join we’ll use is called an *inner* join, which only displays rows that have matching values in both tables. Since every city has rainfall data, all rows will be displayed.

Let’s retrieve the rainfall data for 2019 for all cities.

We’ll do this step by step. First, join the tables by specifying the columns to connect—**city_id** in both tables.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
```

We’ve highlighted the columns to join and specified the connection using **city_id**. Now, we can add a `WHERE` clause to filter for the year 2019.

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

Relational databases are designed to divide information across multiple tables, which can then be combined for analysis and display. This approach offers flexibility for calculations and data manipulation. You’ve learned the core concepts of relational databases and how to join data from two tables.

## 🚀 Challenge

There are many relational databases available online. Use the skills you’ve learned to explore and analyze data.

## Post-Lecture Quiz

## [Post-lecture quiz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/9)

## Review & Self Study

Microsoft Learn offers several resources to deepen your understanding of SQL and relational database concepts:

- [Describe concepts of relational data](https://docs.microsoft.com//learn/modules/describe-concepts-of-relational-data?WT.mc_id=academic-77958-bethanycheum)
- [Get Started Querying with Transact-SQL](https://docs.microsoft.com//learn/paths/get-started-querying-with-transact-sql?WT.mc_id=academic-77958-bethanycheum) (Transact-SQL is a version of SQL)
- [SQL content on Microsoft Learn](https://docs.microsoft.com/learn/browse/?products=azure-sql-database%2Csql-server&expanded=azure&WT.mc_id=academic-77958-bethanycheum)

## Assignment

[Assignment Title](assignment.md)

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please note that automated translations may contain errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is recommended. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.