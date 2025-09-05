<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9399d7b4767e75068f95ce5c660b285c",
  "translation_date": "2025-09-05T13:17:57+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/README.md",
  "language_code": "pt"
}
-->
# Trabalhar com Dados: Bases de Dados Relacionais

|![ Sketchnote por [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/05-RelationalData.png)|
|:---:|
| Trabalhar com Dados: Bases de Dados Relacionais - _Sketchnote por [@nitya](https://twitter.com/nitya)_ |

É provável que já tenha utilizado uma folha de cálculo no passado para armazenar informações. Tinha um conjunto de linhas e colunas, onde as linhas continham as informações (ou dados) e as colunas descreviam essas informações (por vezes chamadas de metadados). Uma base de dados relacional é construída com base neste princípio fundamental de colunas e linhas em tabelas, permitindo que tenha informações distribuídas por várias tabelas. Isto permite trabalhar com dados mais complexos, evitar duplicação e ter flexibilidade na forma como explora os dados. Vamos explorar os conceitos de uma base de dados relacional.

## [Questionário pré-aula](https://ff-quizzes.netlify.app/en/ds/quiz/8)

## Tudo começa com tabelas

Uma base de dados relacional tem como núcleo as tabelas. Tal como numa folha de cálculo, uma tabela é uma coleção de colunas e linhas. A linha contém os dados ou informações com que queremos trabalhar, como o nome de uma cidade ou a quantidade de precipitação. As colunas descrevem os dados que armazenam.

Vamos começar a nossa exploração criando uma tabela para armazenar informações sobre cidades. Podemos começar com o nome e o país. Poderia armazenar isto numa tabela como segue:

| Cidade   | País          |
| -------- | ------------- |
| Tóquio   | Japão         |
| Atlanta  | Estados Unidos|
| Auckland | Nova Zelândia |

Repare que os nomes das colunas **cidade**, **país** e **população** descrevem os dados que estão a ser armazenados, e cada linha tem informações sobre uma cidade.

## As limitações de uma abordagem de tabela única

Provavelmente, a tabela acima parece-lhe relativamente familiar. Vamos começar a adicionar alguns dados adicionais à nossa base de dados em crescimento - precipitação anual (em milímetros). Vamos focar-nos nos anos 2018, 2019 e 2020. Se adicionássemos os dados para Tóquio, poderia ficar algo assim:

| Cidade | País  | Ano | Quantidade |
| ------ | ----- | --- | ---------- |
| Tóquio | Japão | 2020| 1690       |
| Tóquio | Japão | 2019| 1874       |
| Tóquio | Japão | 2018| 1445       |

O que nota na nossa tabela? Pode reparar que estamos a duplicar o nome e o país da cidade várias vezes. Isso pode ocupar bastante espaço de armazenamento e é, em grande parte, desnecessário ter múltiplas cópias. Afinal, Tóquio tem apenas um nome que nos interessa.

OK, vamos tentar outra abordagem. Vamos adicionar novas colunas para cada ano:

| Cidade   | País          | 2018 | 2019 | 2020 |
| -------- | ------------- | ---- | ---- | ---- |
| Tóquio   | Japão         | 1445 | 1874 | 1690 |
| Atlanta  | Estados Unidos| 1779 | 1111 | 1683 |
| Auckland | Nova Zelândia | 1386 | 942  | 1176 |

Embora isto evite a duplicação de linhas, adiciona outros desafios. Teríamos de modificar a estrutura da tabela cada vez que houvesse um novo ano. Além disso, à medida que os dados crescem, ter os anos como colunas tornará mais difícil recuperar e calcular valores.

É por isso que precisamos de múltiplas tabelas e relações. Ao dividir os dados, podemos evitar duplicação e ter mais flexibilidade na forma como trabalhamos com eles.

## Os conceitos de relações

Vamos voltar aos nossos dados e determinar como queremos dividi-los. Sabemos que queremos armazenar o nome e o país das nossas cidades, por isso isto funcionará melhor numa tabela.

| Cidade   | País          |
| -------- | ------------- |
| Tóquio   | Japão         |
| Atlanta  | Estados Unidos|
| Auckland | Nova Zelândia |

Mas antes de criarmos a próxima tabela, precisamos de descobrir como referenciar cada cidade. Precisamos de algum tipo de identificador, ID ou (em termos técnicos de bases de dados) uma chave primária. Uma chave primária é um valor usado para identificar uma linha específica numa tabela. Embora isto possa ser baseado num valor em si (poderíamos usar o nome da cidade, por exemplo), deve quase sempre ser um número ou outro identificador. Não queremos que o ID mude, pois isso quebraria a relação. Na maioria dos casos, a chave primária ou ID será um número gerado automaticamente.

> ✅ Chave primária é frequentemente abreviada como PK

### cidades

| cidade_id | Cidade   | País          |
| --------- | -------- | ------------- |
| 1         | Tóquio   | Japão         |
| 2         | Atlanta  | Estados Unidos|
| 3         | Auckland | Nova Zelândia |

> ✅ Vai reparar que usamos os termos "id" e "chave primária" de forma intercambiável durante esta lição. Os conceitos aqui aplicam-se a DataFrames, que irá explorar mais tarde. Os DataFrames não utilizam a terminologia de "chave primária", mas irá notar que se comportam de forma muito semelhante.

Com a nossa tabela de cidades criada, vamos armazenar os dados de precipitação. Em vez de duplicar as informações completas sobre a cidade, podemos usar o ID. Devemos também garantir que a tabela recém-criada tem uma coluna *id*, já que todas as tabelas devem ter um ID ou chave primária.

### precipitação

| precipitação_id | cidade_id | Ano | Quantidade |
| --------------- | --------- | --- | ---------- |
| 1               | 1         | 2018| 1445       |
| 2               | 1         | 2019| 1874       |
| 3               | 1         | 2020| 1690       |
| 4               | 2         | 2018| 1779       |
| 5               | 2         | 2019| 1111       |
| 6               | 2         | 2020| 1683       |
| 7               | 3         | 2018| 1386       |
| 8               | 3         | 2019| 942        |
| 9               | 3         | 2020| 1176       |

Repare na coluna **cidade_id** dentro da tabela recém-criada **precipitação**. Esta coluna contém valores que referenciam os IDs na tabela **cidades**. Em termos técnicos de dados relacionais, isto é chamado de **chave estrangeira**; é uma chave primária de outra tabela. Pode pensar nela como uma referência ou um apontador. **cidade_id** 1 refere-se a Tóquio.

> [!NOTE] Chave estrangeira é frequentemente abreviada como FK

## Recuperar os dados

Com os nossos dados separados em duas tabelas, pode estar a perguntar-se como os recuperamos. Se estivermos a usar uma base de dados relacional como MySQL, SQL Server ou Oracle, podemos usar uma linguagem chamada Structured Query Language ou SQL. SQL (por vezes pronunciado "sequel") é uma linguagem padrão usada para recuperar e modificar dados numa base de dados relacional.

Para recuperar dados, utiliza-se o comando `SELECT`. Na sua essência, **seleciona-se** as colunas que se quer ver **a partir** da tabela onde estão contidas. Se quisesse exibir apenas os nomes das cidades, poderia usar o seguinte:

```sql
SELECT city
FROM cities;

-- Output:
-- Tokyo
-- Atlanta
-- Auckland
```

`SELECT` é onde lista as colunas, e `FROM` é onde lista as tabelas.

> [NOTE] A sintaxe SQL não distingue maiúsculas de minúsculas, o que significa que `select` e `SELECT` têm o mesmo significado. No entanto, dependendo do tipo de base de dados que está a usar, as colunas e tabelas podem ser sensíveis a maiúsculas e minúsculas. Como resultado, é uma boa prática tratar sempre tudo em programação como sendo sensível a maiúsculas e minúsculas. Quando escreve consultas SQL, a convenção comum é colocar as palavras-chave em letras maiúsculas.

A consulta acima exibirá todas as cidades. Vamos imaginar que só queríamos exibir cidades na Nova Zelândia. Precisamos de algum tipo de filtro. A palavra-chave SQL para isto é `WHERE`, ou "onde algo é verdadeiro".

```sql
SELECT city
FROM cities
WHERE country = 'New Zealand';

-- Output:
-- Auckland
```

## Juntar dados

Até agora, recuperámos dados de uma única tabela. Agora queremos reunir os dados das tabelas **cidades** e **precipitação**. Isto é feito ao *juntar* as tabelas. Irá efetivamente criar uma ligação entre as duas tabelas e combinar os valores de uma coluna de cada tabela.

No nosso exemplo, iremos combinar a coluna **cidade_id** em **precipitação** com a coluna **cidade_id** em **cidades**. Isto irá associar o valor de precipitação à sua respetiva cidade. O tipo de junção que iremos realizar é chamado de *inner join*, o que significa que, se alguma linha não corresponder a nada da outra tabela, não será exibida. No nosso caso, todas as cidades têm dados de precipitação, por isso tudo será exibido.

Vamos recuperar os dados de precipitação de 2019 para todas as nossas cidades.

Vamos fazer isto em etapas. O primeiro passo é juntar os dados indicando as colunas para a ligação - **cidade_id**, como destacado anteriormente.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
```

Destacámos as duas colunas que queremos e o facto de querermos juntar as tabelas através da **cidade_id**. Agora podemos adicionar a instrução `WHERE` para filtrar apenas o ano de 2019.

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

## Resumo

Bases de dados relacionais são centradas na divisão de informações entre múltiplas tabelas, que são depois reunidas para exibição e análise. Isto proporciona um elevado grau de flexibilidade para realizar cálculos e manipular dados. Viu os conceitos fundamentais de uma base de dados relacional e como realizar uma junção entre duas tabelas.

## 🚀 Desafio

Existem inúmeras bases de dados relacionais disponíveis na internet. Pode explorar os dados utilizando as competências que aprendeu acima.

## Questionário pós-aula

## [Questionário pós-aula](https://ff-quizzes.netlify.app/en/ds/quiz/9)

## Revisão & Autoestudo

Existem vários recursos disponíveis no [Microsoft Learn](https://docs.microsoft.com/learn?WT.mc_id=academic-77958-bethanycheum) para continuar a sua exploração de conceitos de SQL e bases de dados relacionais.

- [Descrever conceitos de dados relacionais](https://docs.microsoft.com//learn/modules/describe-concepts-of-relational-data?WT.mc_id=academic-77958-bethanycheum)
- [Introdução à consulta com Transact-SQL](https://docs.microsoft.com//learn/paths/get-started-querying-with-transact-sql?WT.mc_id=academic-77958-bethanycheum) (Transact-SQL é uma versão de SQL)
- [Conteúdo de SQL no Microsoft Learn](https://docs.microsoft.com/learn/browse/?products=azure-sql-database%2Csql-server&expanded=azure&WT.mc_id=academic-77958-bethanycheum)

## Tarefa

[Título da Tarefa](assignment.md)

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, é importante notar que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.