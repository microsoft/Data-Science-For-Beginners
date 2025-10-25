<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "80d80300002ef4e77cc7631d5904bd6e",
  "translation_date": "2025-10-25T18:48:42+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/README.md",
  "language_code": "pt"
}
-->
# Trabalhando com Dados: Bases de Dados Relacionais

|![ Sketchnote por [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/05-RelationalData.png)|
|:---:|
| Trabalhando com Dados: Bases de Dados Relacionais - _Sketchnote por [@nitya](https://twitter.com/nitya)_ |

É bem provável que já tenha usado uma folha de cálculo no passado para armazenar informações. Você tinha um conjunto de linhas e colunas, onde as linhas continham as informações (ou dados) e as colunas descreviam essas informações (às vezes chamadas de metadados). Uma base de dados relacional é construída com base nesse princípio de colunas e linhas em tabelas, permitindo que você tenha informações distribuídas por várias tabelas. Isso possibilita trabalhar com dados mais complexos, evitar duplicações e ter flexibilidade na forma como explora os dados. Vamos explorar os conceitos de uma base de dados relacional.

## [Questionário pré-aula](https://ff-quizzes.netlify.app/en/ds/quiz/8)

## Tudo começa com tabelas

Uma base de dados relacional tem como núcleo as tabelas. Assim como na folha de cálculo, uma tabela é uma coleção de colunas e linhas. A linha contém os dados ou informações com as quais queremos trabalhar, como o nome de uma cidade ou a quantidade de precipitação. As colunas descrevem os dados que armazenam.

Vamos começar nossa exploração criando uma tabela para armazenar informações sobre cidades. Podemos começar com o nome e o país delas. Você poderia armazenar isso em uma tabela como a seguinte:

| Cidade   | País          |
| -------- | ------------- |
| Tóquio   | Japão         |
| Atlanta  | Estados Unidos|
| Auckland | Nova Zelândia |

Note que os nomes das colunas **cidade**, **país** e **população** descrevem os dados armazenados, e cada linha tem informações sobre uma cidade.

## As limitações de uma abordagem de tabela única

Provavelmente, a tabela acima parece relativamente familiar para você. Vamos começar a adicionar alguns dados adicionais à nossa crescente base de dados - precipitação anual (em milímetros). Vamos focar nos anos de 2018, 2019 e 2020. Se fôssemos adicioná-los para Tóquio, poderia ficar algo assim:

| Cidade | País   | Ano | Quantidade |
| ------ | ------ | --- | ---------- |
| Tóquio | Japão  | 2020| 1690       |
| Tóquio | Japão  | 2019| 1874       |
| Tóquio | Japão  | 2018| 1445       |

O que você percebe sobre nossa tabela? Pode notar que estamos duplicando o nome e o país da cidade várias vezes. Isso pode ocupar bastante espaço de armazenamento e é, em grande parte, desnecessário ter várias cópias. Afinal, Tóquio tem apenas um nome que nos interessa.

Ok, vamos tentar outra coisa. Vamos adicionar novas colunas para cada ano:

| Cidade   | País          | 2018 | 2019 | 2020 |
| -------- | ------------- | ---- | ---- | ---- |
| Tóquio   | Japão         | 1445 | 1874 | 1690 |
| Atlanta  | Estados Unidos| 1779 | 1111 | 1683 |
| Auckland | Nova Zelândia | 1386 | 942  | 1176 |

Embora isso evite a duplicação de linhas, traz outros desafios. Precisaríamos modificar a estrutura da nossa tabela cada vez que houvesse um novo ano. Além disso, à medida que nossos dados crescem, ter os anos como colunas tornará mais difícil recuperar e calcular valores.

É por isso que precisamos de múltiplas tabelas e relacionamentos. Dividindo nossos dados, podemos evitar duplicações e ter mais flexibilidade na forma como trabalhamos com eles.

## Os conceitos de relacionamentos

Vamos voltar aos nossos dados e determinar como queremos dividi-los. Sabemos que queremos armazenar o nome e o país das nossas cidades, então isso provavelmente funcionará melhor em uma tabela.

| Cidade   | País          |
| -------- | ------------- |
| Tóquio   | Japão         |
| Atlanta  | Estados Unidos|
| Auckland | Nova Zelândia |

Mas antes de criarmos a próxima tabela, precisamos descobrir como referenciar cada cidade. Precisamos de algum tipo de identificador, ID ou (em termos técnicos de base de dados) uma chave primária. Uma chave primária é um valor usado para identificar uma linha específica em uma tabela. Embora isso possa ser baseado em um valor em si (poderíamos usar o nome da cidade, por exemplo), quase sempre deve ser um número ou outro identificador. Não queremos que o ID mude, pois isso quebraria o relacionamento. Você verá que, na maioria dos casos, a chave primária ou ID será um número gerado automaticamente.

> ✅ Chave primária é frequentemente abreviada como PK

### cidades

| city_id | Cidade   | País          |
| ------- | -------- | ------------- |
| 1       | Tóquio   | Japão         |
| 2       | Atlanta  | Estados Unidos|
| 3       | Auckland | Nova Zelândia |

> ✅ Você notará que usamos os termos "id" e "chave primária" de forma intercambiável durante esta lição. Os conceitos aqui se aplicam a DataFrames, que você explorará mais tarde. DataFrames não utilizam a terminologia de "chave primária", no entanto, você perceberá que eles se comportam de maneira muito semelhante.

Com nossa tabela de cidades criada, vamos armazenar os dados de precipitação. Em vez de duplicar as informações completas sobre a cidade, podemos usar o ID. Também devemos garantir que a tabela recém-criada tenha uma coluna *id*, já que todas as tabelas devem ter um ID ou chave primária.

### precipitação

| rainfall_id | city_id | Ano | Quantidade |
| ----------- | ------- | --- | ---------- |
| 1           | 1       | 2018| 1445       |
| 2           | 1       | 2019| 1874       |
| 3           | 1       | 2020| 1690       |
| 4           | 2       | 2018| 1779       |
| 5           | 2       | 2019| 1111       |
| 6           | 2       | 2020| 1683       |
| 7           | 3       | 2018| 1386       |
| 8           | 3       | 2019| 942        |
| 9           | 3       | 2020| 1176       |

Note a coluna **city_id** dentro da tabela recém-criada **precipitação**. Esta coluna contém valores que referenciam os IDs na tabela **cidades**. Em termos técnicos de dados relacionais, isso é chamado de **chave estrangeira**; é uma chave primária de outra tabela. Você pode pensar nela como uma referência ou um apontador. **city_id** 1 refere-se a Tóquio.

> [!NOTE] 
> Chave estrangeira é frequentemente abreviada como FK

## Recuperando os dados

Com nossos dados separados em duas tabelas, você pode estar se perguntando como recuperá-los. Se estivermos usando uma base de dados relacional como MySQL, SQL Server ou Oracle, podemos usar uma linguagem chamada Structured Query Language ou SQL. SQL (às vezes pronunciado como "sequel") é uma linguagem padrão usada para recuperar e modificar dados em uma base de dados relacional.

Para recuperar dados, você usa o comando `SELECT`. Em sua essência, você **seleciona** as colunas que deseja ver **de** uma tabela onde elas estão contidas. Se você quisesse exibir apenas os nomes das cidades, poderia usar o seguinte:

```sql
SELECT city
FROM cities;

-- Output:
-- Tokyo
-- Atlanta
-- Auckland
```

`SELECT` é onde você lista as colunas, e `FROM` é onde você lista as tabelas.

> [!NOTE] 
> A sintaxe do SQL não diferencia maiúsculas de minúsculas, ou seja, `select` e `SELECT` significam a mesma coisa. No entanto, dependendo do tipo de base de dados que você está usando, as colunas e tabelas podem ser sensíveis a maiúsculas e minúsculas. Como resultado, é uma boa prática sempre tratar tudo em programação como sensível a maiúsculas e minúsculas. Ao escrever consultas SQL, a convenção comum é colocar as palavras-chave em letras maiúsculas.

A consulta acima exibirá todas as cidades. Vamos imaginar que queremos exibir apenas as cidades da Nova Zelândia. Precisamos de algum tipo de filtro. A palavra-chave SQL para isso é `WHERE`, ou "onde algo é verdadeiro".

```sql
SELECT city
FROM cities
WHERE country = 'New Zealand';

-- Output:
-- Auckland
```

## Unindo dados

Até agora, recuperamos dados de uma única tabela. Agora queremos reunir os dados de **cidades** e **precipitação**. Isso é feito *unindo* as tabelas. Você efetivamente criará uma ligação entre as duas tabelas e combinará os valores de uma coluna de cada tabela.

No nosso exemplo, vamos combinar a coluna **city_id** em **precipitação** com a coluna **city_id** em **cidades**. Isso combinará o valor da precipitação com sua respectiva cidade. O tipo de união que realizaremos é chamado de união *interna*, o que significa que, se alguma linha não corresponder a nada da outra tabela, ela não será exibida. No nosso caso, todas as cidades têm dados de precipitação, então tudo será exibido.

Vamos recuperar os dados de precipitação de 2019 para todas as nossas cidades.

Vamos fazer isso em etapas. O primeiro passo é unir os dados indicando as colunas para a ligação - **city_id**, como destacado anteriormente.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
```

Destacamos as duas colunas que queremos e o fato de que queremos unir as tabelas pela **city_id**. Agora podemos adicionar a instrução `WHERE` para filtrar apenas o ano de 2019.

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

Bases de dados relacionais são centradas na divisão de informações entre múltiplas tabelas, que são então reunidas para exibição e análise. Isso proporciona um alto grau de flexibilidade para realizar cálculos e manipular dados de outras formas. Você viu os conceitos principais de uma base de dados relacional e como realizar uma união entre duas tabelas.

## 🚀 Desafio

Existem inúmeras bases de dados relacionais disponíveis na internet. Você pode explorar os dados usando as habilidades que aprendeu acima.

## Questionário Pós-Aula

## [Questionário pós-aula](https://ff-quizzes.netlify.app/en/ds/quiz/9)

## Revisão e Autoestudo

Existem vários recursos disponíveis no [Microsoft Learn](https://docs.microsoft.com/learn?WT.mc_id=academic-77958-bethanycheum) para você continuar sua exploração dos conceitos de SQL e bases de dados relacionais.

- [Descrever conceitos de dados relacionais](https://docs.microsoft.com//learn/modules/describe-concepts-of-relational-data?WT.mc_id=academic-77958-bethanycheum)
- [Introdução à consulta com Transact-SQL](https://docs.microsoft.com//learn/paths/get-started-querying-with-transact-sql?WT.mc_id=academic-77958-bethanycheum) (Transact-SQL é uma versão do SQL)
- [Conteúdo de SQL no Microsoft Learn](https://docs.microsoft.com/learn/browse/?products=azure-sql-database%2Csql-server&expanded=azure&WT.mc_id=academic-77958-bethanycheum)

## Tarefa

[Título da Tarefa](assignment.md)

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se uma tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.