<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11b166fbcb7eaf82308cdc24b562f687",
  "translation_date": "2025-09-04T17:43:44+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/README.md",
  "language_code": "br"
}
-->
# Trabalhando com Dados: Bancos de Dados Relacionais

|![ Sketchnote por [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/05-RelationalData.png)|
|:---:|
| Trabalhando com Dados: Bancos de Dados Relacionais - _Sketchnote por [@nitya](https://twitter.com/nitya)_ |

É bem provável que você já tenha usado uma planilha no passado para armazenar informações. Você tinha um conjunto de linhas e colunas, onde as linhas continham as informações (ou dados) e as colunas descreviam essas informações (às vezes chamadas de metadados). Um banco de dados relacional é construído com base nesse princípio central de colunas e linhas em tabelas, permitindo que você tenha informações distribuídas em várias tabelas. Isso possibilita trabalhar com dados mais complexos, evitar duplicação e ter flexibilidade na forma como explora os dados. Vamos explorar os conceitos de um banco de dados relacional.

## [Quiz pré-aula](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/8)

## Tudo começa com tabelas

Um banco de dados relacional tem como base as tabelas. Assim como na planilha, uma tabela é uma coleção de colunas e linhas. A linha contém os dados ou informações com as quais queremos trabalhar, como o nome de uma cidade ou a quantidade de chuva. As colunas descrevem os dados que armazenam.

Vamos começar nossa exploração criando uma tabela para armazenar informações sobre cidades. Podemos começar com o nome e o país delas. Você poderia armazenar isso em uma tabela como a seguinte:

| Cidade   | País          |
| -------- | ------------- |
| Tóquio   | Japão         |
| Atlanta  | Estados Unidos|
| Auckland | Nova Zelândia |

Observe que os nomes das colunas **cidade**, **país** e **população** descrevem os dados armazenados, e cada linha tem informações sobre uma cidade.

## As limitações de uma abordagem de tabela única

Provavelmente, a tabela acima parece relativamente familiar para você. Vamos começar a adicionar alguns dados adicionais ao nosso banco de dados em crescimento - precipitação anual (em milímetros). Vamos focar nos anos de 2018, 2019 e 2020. Se fôssemos adicionar isso para Tóquio, poderia ficar algo assim:

| Cidade | País  | Ano | Quantidade |
| ------ | ----- | --- | ---------- |
| Tóquio | Japão | 2020| 1690       |
| Tóquio | Japão | 2019| 1874       |
| Tóquio | Japão | 2018| 1445       |

O que você percebe sobre nossa tabela? Você pode notar que estamos duplicando o nome e o país da cidade várias vezes. Isso pode ocupar bastante espaço de armazenamento e é amplamente desnecessário ter várias cópias. Afinal, Tóquio tem apenas um nome que nos interessa.

OK, vamos tentar outra abordagem. Vamos adicionar novas colunas para cada ano:

| Cidade   | País          | 2018 | 2019 | 2020 |
| -------- | ------------- | ---- | ---- | ---- |
| Tóquio   | Japão         | 1445 | 1874 | 1690 |
| Atlanta  | Estados Unidos| 1779 | 1111 | 1683 |
| Auckland | Nova Zelândia | 1386 | 942  | 1176 |

Embora isso evite a duplicação de linhas, adiciona outros desafios. Precisaríamos modificar a estrutura da tabela cada vez que houver um novo ano. Além disso, conforme nossos dados crescem, ter os anos como colunas tornará mais difícil recuperar e calcular valores.

É por isso que precisamos de múltiplas tabelas e relacionamentos. Dividindo nossos dados, podemos evitar duplicação e ter mais flexibilidade na forma como trabalhamos com eles.

## Os conceitos de relacionamentos

Vamos voltar aos nossos dados e determinar como queremos dividi-los. Sabemos que queremos armazenar o nome e o país das nossas cidades, então isso provavelmente funcionará melhor em uma tabela.

| Cidade   | País          |
| -------- | ------------- |
| Tóquio   | Japão         |
| Atlanta  | Estados Unidos|
| Auckland | Nova Zelândia |

Mas antes de criarmos a próxima tabela, precisamos descobrir como referenciar cada cidade. Precisamos de algum tipo de identificador, ID ou (em termos técnicos de banco de dados) uma chave primária. Uma chave primária é um valor usado para identificar uma linha específica em uma tabela. Embora isso possa ser baseado em um valor em si (poderíamos usar o nome da cidade, por exemplo), quase sempre deve ser um número ou outro identificador. Não queremos que o ID mude, pois isso quebraria o relacionamento. Você verá que, na maioria dos casos, a chave primária ou ID será um número gerado automaticamente.

> ✅ Chave primária é frequentemente abreviada como PK

### cidades

| city_id | Cidade   | País          |
| ------- | -------- | ------------- |
| 1       | Tóquio   | Japão         |
| 2       | Atlanta  | Estados Unidos|
| 3       | Auckland | Nova Zelândia |

> ✅ Você notará que usamos os termos "id" e "chave primária" de forma intercambiável durante esta lição. Os conceitos aqui se aplicam a DataFrames, que você explorará mais tarde. DataFrames não usam a terminologia de "chave primária", mas você notará que eles se comportam de maneira muito semelhante.

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

Observe a coluna **city_id** dentro da tabela recém-criada **precipitação**. Essa coluna contém valores que referenciam os IDs na tabela **cidades**. Em termos técnicos de dados relacionais, isso é chamado de **chave estrangeira**; é uma chave primária de outra tabela. Você pode pensar nisso como uma referência ou um ponteiro. **city_id** 1 referencia Tóquio.

> [!NOTE] Chave estrangeira é frequentemente abreviada como FK

## Recuperando os dados

Com nossos dados separados em duas tabelas, você pode estar se perguntando como recuperá-los. Se estivermos usando um banco de dados relacional como MySQL, SQL Server ou Oracle, podemos usar uma linguagem chamada Structured Query Language ou SQL. SQL (às vezes pronunciado como "sequel") é uma linguagem padrão usada para recuperar e modificar dados em um banco de dados relacional.

Para recuperar dados, você usa o comando `SELECT`. Em sua essência, você **seleciona** as colunas que deseja ver **de** dentro da tabela onde estão contidas. Se você quisesse exibir apenas os nomes das cidades, poderia usar o seguinte:

```sql
SELECT city
FROM cities;

-- Output:
-- Tokyo
-- Atlanta
-- Auckland
```

`SELECT` é onde você lista as colunas, e `FROM` é onde você lista as tabelas.

> [NOTE] A sintaxe do SQL não diferencia maiúsculas de minúsculas, o que significa que `select` e `SELECT` têm o mesmo significado. No entanto, dependendo do tipo de banco de dados que você está usando, as colunas e tabelas podem ser sensíveis a maiúsculas e minúsculas. Como resultado, é uma boa prática sempre tratar tudo em programação como sensível a maiúsculas e minúsculas. Ao escrever consultas SQL, a convenção comum é colocar as palavras-chave em letras maiúsculas.

A consulta acima exibirá todas as cidades. Vamos imaginar que queremos exibir apenas cidades na Nova Zelândia. Precisamos de algum tipo de filtro. A palavra-chave SQL para isso é `WHERE`, ou "onde algo é verdadeiro".

```sql
SELECT city
FROM cities
WHERE country = 'New Zealand';

-- Output:
-- Auckland
```

## Unindo dados

Até agora, recuperamos dados de uma única tabela. Agora queremos reunir os dados de **cidades** e **precipitação**. Isso é feito por meio de um *join*. Você efetivamente criará uma ligação entre as duas tabelas e combinará os valores de uma coluna de cada tabela.

No nosso exemplo, vamos combinar a coluna **city_id** em **precipitação** com a coluna **city_id** em **cidades**. Isso combinará o valor de precipitação com sua respectiva cidade. O tipo de join que realizaremos é chamado de *inner join*, o que significa que, se alguma linha não corresponder a nada da outra tabela, ela não será exibida. No nosso caso, todas as cidades têm dados de precipitação, então tudo será exibido.

Vamos recuperar os dados de precipitação de 2019 para todas as nossas cidades.

Vamos fazer isso em etapas. A primeira etapa é unir os dados indicando as colunas para a ligação - **city_id**, conforme destacado anteriormente.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
```

Destacamos as duas colunas que queremos e o fato de que queremos unir as tabelas por **city_id**. Agora podemos adicionar a cláusula `WHERE` para filtrar apenas o ano de 2019.

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

Bancos de dados relacionais são centrados em dividir informações entre várias tabelas, que são então reunidas para exibição e análise. Isso oferece um alto grau de flexibilidade para realizar cálculos e manipular dados. Você viu os conceitos principais de um banco de dados relacional e como realizar um join entre duas tabelas.

## 🚀 Desafio

Existem inúmeros bancos de dados relacionais disponíveis na internet. Você pode explorar os dados usando as habilidades que aprendeu acima.

## Quiz pós-aula

## [Quiz pós-aula](https://ff-quizzes.netlify.app/en/ds/)

## Revisão e Autoestudo

Há vários recursos disponíveis no [Microsoft Learn](https://docs.microsoft.com/learn?WT.mc_id=academic-77958-bethanycheum) para você continuar sua exploração de conceitos de SQL e bancos de dados relacionais.

- [Descrever conceitos de dados relacionais](https://docs.microsoft.com//learn/modules/describe-concepts-of-relational-data?WT.mc_id=academic-77958-bethanycheum)
- [Introdução à consulta com Transact-SQL](https://docs.microsoft.com//learn/paths/get-started-querying-with-transact-sql?WT.mc_id=academic-77958-bethanycheum) (Transact-SQL é uma versão do SQL)
- [Conteúdo de SQL no Microsoft Learn](https://docs.microsoft.com/learn/browse/?products=azure-sql-database%2Csql-server&expanded=azure&WT.mc_id=academic-77958-bethanycheum)

## Tarefa

[Título da Tarefa](assignment.md)

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.