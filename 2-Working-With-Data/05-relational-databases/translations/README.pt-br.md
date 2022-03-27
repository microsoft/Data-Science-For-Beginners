# Trabalhando com dados: Bases de dados relacionais

|![ Sketchnote por [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/05-RelationalData.png)|
|:---:|
| Trabalhando Com Dados: Bases de dados Relacionais - _Sketchnote por [@nitya](https://twitter.com/nitya)_ |

Você provavelmente já usou uma planilha para guardar informações. Você tinha um conjunto de linhas e colunas, onde as linhas continham a informação (ou dados), e as colunas descreviam a informação (às vezes chamada de metadados). Uma base de dados relacional expande esse princípio de linhas e colunas em tabelas, lhe permitindo ter informações espalhadas por múltiplas tabelas. Isso lhe permite trabalhar com dados mais complexos, evitar duplicação, e ter flexibilidade na maneira de explorar os dados. Vamos explorar os conceitos de uma base de dados relacional

## [Quiz pré-aula](https://red-water-0103e7a0f.azurestaticapps.net/quiz/8)

## Tudo começa com tabelas
Uma base de dados relacional tem por princípio as tabelas. Da mesma forma que uma planilha, uma tabela é um conjunto de linhas e colunas. As colunas contém os dados ou as informações com as quais queremos trabalhas, como o nome de uma cidade ou a quantidade de chuva. As colunas descrevem os dados que elas guardam.  

Vamos começar a nossa exploração iniciando uma tabela para guardar informação sobre cidades. Nós podemos começar com os seus nomes e países. Você pode guardá-los numa tabela da seguinte forma:

| Cidade   | País           |
| -------- | -------------  |
| Tóquio   | Japão          |
| Atlanta  | Estados Unidos |
| Auckland | Nova Zelândia  |

Perceba que os nomes das colunas de **cidade**, **país** e **população** descrevem os dados que são guardados, e cada coluna tem informações sobre uma cidade

## Os problemas de se ter uma única tabela
A tabela acima provavelmente parece relativamente familiar para você. Vamos começar a preencher dados adicionais para nossa base de dados: precipitação anual (em milímetros). Focaremos nos anos de 2018, 2019 e 2020. Se fôssemos adicioná-los a Tóquio, ficaria mais ou menos assim:

| Cidade | País    | Ano  | Quantidade |
| -----  | ------- | ---- | ------     |
| Tóquio | Japão   | 2020 | 1690       |
| Tóquio | Japão   | 2019 | 1874       |
| Tóquio | Japão   | 2018 | 1445       |

O que dá para perceber na nossa tabela? Você pode notar que estamos duplicando o nome e o país da cidade diversas vezes. Isso pode usar espaço demais desnecessariamente. Afinal, Tóquio só tem um nome que nos interessa.

OK, vamos tentar algo diferente. Vamos adicionar novas colunas para cada ano:


| Cidade     | País       | 2018 | 2019 | 2020 |
| -------- | ------------- | ---- | ---- | ---- |
| Tóquio    | Japão         | 1445 | 1874 | 1690 |
| Atlanta  | Estados Unidos | 1779 | 1111 | 1683 |
| Auckland | Nova Zelândia  | 1386 | 942  | 1176 |

Enquanto isso nos permite evitar duplicação de linhas, nós temos alguns outros desafios. Nós precisaríamos modificar a estrutura da nossa tabela cada vez que temos um novo ano. Além disso, conforme nossos dados aumentam, ter os anos como colunas pode fazer com que consultar e calcular valores seja mais difícil. 

Por isso nós precisamos de várias tabelas e de relações. Dividindo nossos dados nós conseguimos evitar duplicações e então temos mais flexibilidade para trabalhar com eles.

## Os conceitos de relações
Vamos voltar para os nossos dados e vamos determinar como queremos separar as coisas. Sabemos que nós queremos guardar o nome e o país de nossas cidades, então isso provavelmente vai ser melhor se ficar em uma tabela.

| Cidade     | País       |
| -------- | ------------- |
| Tokyo    | Japão         |
| Atlanta  | Estados Unidos |
| Auckland | Nova Zelândia   |

Mas antes de criarmos a próxima tabela, precisamos descobrir como referenciar cada cidade. Precisamos de algum tipo de identificador, ID, ou (em termos de bases de dados) uma chave primária. Uma chave primária é um valor usado para identificar uma linha específica numa tabela. Enquanto essa chave pode ser baseada num valor mesmo (poderíamos usar o nome da cidade, por exemplo), ela deverá ser quase sempre um número ou outro identificador. Não queremos que o id mude nunca, já que estragaria a relação. Você vai ver que na maioria dos casos a chave primária ou id vai ser um número gerado automaticamente.


> ✅ Chave primária geralmente se abrevia com PK (do inglês "Primary Key")

### cidades

| cidade_id | Cidade     | País       |
| ------- | -------- | ------------- |
| 1       | Tóquio    | Japão         |
| 2       | Atlanta  | Estados Unidos |
| 3       | Auckland | Nova Zelândia   |

> ✅ Você pode perceber que nós usamos os termos "id" e "chave primária" como termos iguais durante essa aula. Os conceitos aqui se aplicam a DataFrames, que você vai explorar mais além. DataFrames não usam a terminologia de "chave primária", mas se comportam de uma maneira bem parecida.

Com nossa tabela de cidades criada, vamos guardar a precipitação. Em vez de duplicar a informação sobre a cidade, podemos usar o id. Também devemos nos certificar de que a tabela criada também tem uma coluna *id*, já que todas as tabelas devem ter um id ou chave primária.


### precipitacao

| precipitacao_id | cidade_id | Ano | Quantidade |
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

Perceba a coluna **cidade_id** na tabela **precipitacao** recém criada. Essa coluna contém valores que referenciam os IDs na tabela **cidades**. Em termos técnicos relacionais, isso se chama **chave externa** ou  **chave estrangeira**; é uma chave primária de outra tabela. Você pode imaginar que é apenas uma referência ou ponteiro. O **cidade_id** 1 faz referência a Tóquio.

> [!NOTE] Chave Estrangeira é abreviada como FK ("Foreign Key" em inglês)

## Buscando dados

With our data separated into two tables, you may be wondering how we retrieve it. If we are using a relational database such as MySQL, SQL Server or Oracle, we can use a language called Structured Query Language or SQL. SQL (sometimes pronounced sequel) is a standard language used to retrieve and modify data in a relational database.

To retrieve data you use the command `SELECT`. At its core, you **select** the columns you want to see **from** the table they're contained in. If you wanted to display just the names of the cities, you could use the following:

```sql
SELECT cidade
FROM cities;

-- Output:
-- Tóquio
-- Atlanta
-- Auckland
```

`SELECT` is where you list the columns, and `FROM` is where you list the tables.

> [NOTE] SQL syntax is case-insensitive, meaning `select` and `SELECT` mean the same thing. However, depending on the type of database you are using the columns and tables might be case sensitive. As a result, it's a best practice to always treat everything in programming like it's case sensitive. When writing SQL queries common convention is to put the keywords in all upper-case letters.

The query above will display all cities. Let's imagine we only wanted to display cities in Nova Zelândia. We need some form of a filter. The SQL keyword for this is `WHERE`, or "where something is true".

```sql
SELECT cidade
FROM cities
WHERE country = 'Nova Zelândia';

-- Output:
-- Auckland
```

## Joining data

Until now we've retrieved data from a single table. Now we want to bring the data together from both **cities** and **rainfall**. This is done by *joining* them together. You will effectively create a seam between the two tables, and match up the values from a column from each table.

In our example, we will match the **cidade_id** column in **rainfall** with the **cidade_id** column in **cities**. This will match the rainfall value with its respective cidade. The type of join we will perform is what's called an *inner* join, meaning if any rows don't match with anything from the other table they won't be displayed. In our case every cidade has rainfall, so everything will be displayed.

Let's retrieve the rainfall for 2019 for all our cities.

We're going to do this in steps. The first step is to join the data together by indicating the columns for the seam - **cidade_id** as highlighted before.

```sql
SELECT cities.cidade
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.cidade_id = rainfall.cidade_id
```

We have highlighted the two columns we want, and the fact we want to join the tables together by the **cidade_id**. Now we can add the `WHERE` statement to filter out only year 2019.

```sql
SELECT cities.cidade
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.cidade_id = rainfall.cidade_id
WHERE rainfall.year = 2019

-- Output

-- cidade     | amount
-- -------- | ------
-- Tóquio    | 1874
-- Atlanta  | 1111
-- Auckland |  942
```

## Summary

Relational databases are centered around dividing information between multiple tables which is then brought back together for display and analysis. This provides a high degree of flexibility to perform calculations and otherwise manipulate data. You have seen the core concepts of a relational database, and how to perform a join between two tables.

## 🚀 Challenge

There are numerous relational databases available on the internet. You can explore the data by using the skills you've learned above.

## Post-Lecture Quiz

## [Post-lecture quiz](https://red-water-0103e7a0f.azurestaticapps.net/quiz/9)

## Review & Self Study

There are several resources available on [Microsoft Learn](https://docs.microsoft.com/learn?WT.mc_id=academic-40229-cxa) for you to continue your exploration of SQL and relational database concepts

- [Describe concepts of relational data](https://docs.microsoft.com//learn/modules/describe-concepts-of-relational-data?WT.mc_id=academic-40229-cxa)
- [Get Started Querying with Transact-SQL](https://docs.microsoft.com//learn/paths/get-started-querying-with-transact-sql?WT.mc_id=academic-40229-cxa) (Transact-SQL is a version of SQL)
- [SQL content on Microsoft Learn](https://docs.microsoft.com/learn/browse/?products=azure-sql-database%2Csql-server&expanded=azure&WT.mc_id=academic-40229-cxa)

## Assignment

[Assignment Title](assignment.md)
