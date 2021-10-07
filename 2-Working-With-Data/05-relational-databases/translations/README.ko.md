# 데이터 작업: 관계형 데이터베이스

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/05-RelationalData.png)|
|:---:|
| 데이터 작업: 관계형 데이터베이스 - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

과거에 스프레드 시트를 통해 정보를 저장한 경험이 있을 것입니다. 이는 행(rows)과 열(columns)을 가지고 있으며, 행(rows)에는 정보(혹은 데이터)를 나타내고 열(columns)에는 해당 정보(또는 메타데이터)를 정의합니다. 관계형 데이터베이스는 테이블의 행과 열의 핵심 원리를 기반으로 구축되며 여러 테이블에 정보를 분산시킬 수 있습니다. 이를 통해 더 복잡한 데이터를 다룰 수 있을 뿐만 아니라 중복을 방지하고, 데이터 탐색 방식에서 유연성을 가질 수 있습니다. 관계형 데이터베이스의 개념을 좀 더 살펴보겠습니다.

## [Pre-lecture quiz](https://red-water-0103e7a0f.azurestaticapps.net/quiz/8)

## 모든 것의 시작 : 테이블(table)

A relational database has at its core tables. 스프레드 시트와 마찬가지로 테이블은 열과 행으로 이루어져 있습니다. 행에는 도시 이름이나 강우량등의 작업하고자 하는 데이터나 정보를 나타냅니다. 열에는 저장된 데이터에 대한 설명을 나타냅니다.

그렇다면 이제 실습을 시작해보겠습니다. 우선 도시 정보를 저장하는 테이블을 생성해 보도록 하겠습니다. 아래와 같이 나라와 도시 이름을 저장할 수 있을 것입니다.:

| City     | Country       |
| -------- | ------------- |
| Tokyo    | Japan         |
| Atlanta  | United States |
| Auckland | New Zealand   |

**city**, **country** 및 **population**의 열 이름은 저장 중인 데이터를 가리키며, 각 행에는 도시에 대한 정보가 저장되어 있습니다.

## 단일 테이블의 단점

위의 테이블은 비교적 친숙해 보일 수도 있습니다. 이제 데이터베이스에 급증하는 연간 강우량(밀리미터 단위)에 대한 몇가지 데이터를 추가해 보겠습니다. 만약 우리가 2018,2018 그리고 2020년의 데이터를 추가한다면, 다음과 같을 것입니다.:

| City  | Country | Year | Amount |
| ----- | ------- | ---- | ------ |
| Tokyo | Japan   | 2020 | 1690   |
| Tokyo | Japan   | 2019 | 1874   |
| Tokyo | Japan   | 2018 | 1445   |

테이블에서 뭔가 알아차리셨나요? 도시의 이름과 국가를 계속해서 중복적으로 사용하고 있는 것을 발견했을 것입니다. 이러한 경우 불필요한 복사본을 저장함에 따라 저장소 낭비가 발생하게 됩니다. 결국, Tokyo는 하나만 존재해야 합니다.

그렇다면 다른 방식으로 접근해 보겠습니다. 각 연도에 대한 새 열을 추가하겠습니다.:

| City     | Country       | 2018 | 2019 | 2020 |
| -------- | ------------- | ---- | ---- | ---- |
| Tokyo    | Japan         | 1445 | 1874 | 1690 |
| Atlanta  | United States | 1779 | 1111 | 1683 |
| Auckland | New Zealand   | 1386 | 942  | 1176 |

이러한 방식은 행에 대한 중복을 피할수는 있지만, 몇 가지 해결해야할 과제가 존재합니다. 우선, 새로운 연도가 추가될 때마다 테이블의 구조를 수정해야만 합니다. 또한, 데이터가 증가함에 따라 값을 검색하고 계산하는 것이 더 어려워집니다.

이것이 여러 테이블의 관계가 필요한 이유입니다. 데이터를 분리함으로써 중복을 방지하고, 데이터를 보다 유연하게 사용할 수 있습니다.

## 관계의 개념

다시 데이터를 보며 어떻게 데이터를 분할할 것인지 결정해 보겠습니다. 이미 우리는 City의 Name과 Country를 저장하는 것이 최선의 방법인 것을 알고 있고, 실제로 가장 잘 동작할 것입니다.

| City     | Country       |
| -------- | ------------- |
| Tokyo    | Japan         |
| Atlanta  | United States |
| Auckland | New Zealand   |

하지만 우리가 다음 테이블을 생성하기 이전에, 우리는 각각의 도시를 어떻게 참조할 것인지 생각해 봐야합니다. 구분 지을 수 있는 여러 형태의 식별자,ID 또는 기본키(Primary key)가 필요합니다. 기본키(Primary key)는 테이블에서 특정 행을 식별하는데 사용되는 값입니다. 기본키로 값 자체(ex. 도시 이름)를 사용할 수도 있지만, 대부분 숫자 또는 다른 식별자가 사용됩니다. ID 값이 바뀌면서 관계를 깨뜨릴 수 있기 때문에 대부분 기본키 또는 자동 생성된 번호를 사용합니다.  

> ✅ 기본키(Primary key)는 주로 PK라고 약칭 됩니다.

### 도시

| city_id | City     | Country       |
| ------- | -------- | ------------- |
| 1       | Tokyo    | Japan         |
| 2       | Atlanta  | United States |
| 3       | Auckland | New Zealand   |

> ✅ 이번 강의에서 우리는 "id"와 "기본키(Primary key)"를 혼용해서 사용하고 있습니다. 이에 대한 자세한 개념은 나중에 살펴볼 데이터 프레임(DataFrames)에 적용됩니다. 데이터 프레임(DataFrames)이 "기본 키"라는 용어를 사용하지는 않지만, 동일한 방식인 것을 알 수 있습니다.

도시 테이블이 생성되었으니, 강우량 테이블을 만들어 보겠습니다. 도시에 대한 전체 정보를 가져오는 대신, 이제 우리는 id를 사용할 수 있습니다. 모든 테이블은 id 또는 기본 키를 가져야 하므로, 새로 생성되는 테이블도 *id* 열을 가져야 합니다.

### 강수량

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

새롭게 생성된 **강수량** 테이블의 **city_id** 열이 추가 되었습니다. 이 열은 **cities** 테이블의 참조 값(reference id)을 나타냅니다. 기술적 용어로 이것을, **왜래 키(foreign key)**라고 부릅니다; 이는 다른 테이블의 기본키입니다. 참조나 포인터의 개념이라고 생각할 수 있습니다. **city_id** 1은 Tokyo를 참조합니다.

> ✅ 외래키(Foreign key)는 주로 FK라고 약칭합니다.

## 데이터 조회

With our data separated into two tables, you may be wondering how we retrieve it. If we are using a relational database such as MySQL, SQL Server or Oracle, we can use a language called Structured Query Language or SQL. SQL (sometimes pronounced sequel) is a standard language used to retrieve and modify data in a relational database.

To retrieve data you use the command `SELECT`. At its core, you **select** the columns you want to see **from** the table they're contained in. If you wanted to display just the names of the cities, you could use the following:

```sql
SELECT city
FROM cities;

-- Output:
-- Tokyo
-- Atlanta
-- Auckland
```

`SELECT` is where you list the columns, and `FROM` is where you list the tables.

> [NOTE] SQL syntax is case-insensitive, meaning `select` and `SELECT` mean the same thing. However, depending on the type of database you are using the columns and tables might be case sensitive. As a result, it's a best practice to always treat everything in programming like it's case sensitive. When writing SQL queries common convention is to put the keywords in all upper-case letters.

The query above will display all cities. Let's imagine we only wanted to display cities in New Zealand. We need some form of a filter. The SQL keyword for this is `WHERE`, or "where something is true".

```sql
SELECT city
FROM cities
WHERE country = 'New Zealand';

-- Output:
-- Auckland
```

## 데이터 조인

Until now we've retrieved data from a single table. Now we want to bring the data together from both **cities** and **rainfall**. This is done by *joining* them together. You will effectively create a seam between the two tables, and match up the values from a column from each table.

In our example, we will match the **city_id** column in **rainfall** with the **city_id** column in **cities**. This will match the rainfall value with its respective city. The type of join we will perform is what's called an *inner* join, meaning if any rows don't match with anything from the other table they won't be displayed. In our case every city has rainfall, so everything will be displayed.

Let's retrieve the rainfall for 2019 for all our cities.

We're going to do this in steps. The first step is to join the data together by indicating the columns for the seam - **city_id** as highlighted before.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
```

We have highlighted the two columns we want, and the fact we want to join the tables together by the **city_id**. Now we can add the `WHERE` statement to filter out only year 2019.

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

## 요약

Relational databases are centered around dividing information between multiple tables which is then brought back together for display and analysis. This provides a high degree of flexibility to perform calculations and otherwise manipulate data. You have seen the core concepts of a relational database, and how to perform a join between two tables.

## 🚀 챌린지

There are numerous relational databases available on the internet. You can explore the data by using the skills you've learned above.

## 강의 후 퀴즈

## [Post-lecture quiz](https://red-water-0103e7a0f.azurestaticapps.net/quiz/9)

## Review & Self Study

There are several resources available on [Microsoft Learn](https://docs.microsoft.com/learn?WT.mc_id=academic-40229-cxa) for you to continue your exploration of SQL and relational database concepts

- [Describe concepts of relational data](https://docs.microsoft.com//learn/modules/describe-concepts-of-relational-data?WT.mc_id=academic-40229-cxa)
- [Get Started Querying with Transact-SQL](https://docs.microsoft.com//learn/paths/get-started-querying-with-transact-sql?WT.mc_id=academic-40229-cxa) (Transact-SQL is a version of SQL)
- [SQL content on Microsoft Learn](https://docs.microsoft.com/learn/browse/?products=azure-sql-database%2Csql-server&expanded=azure&WT.mc_id=academic-40229-cxa)

## 과제

[Assignment Title](assignment.md)
