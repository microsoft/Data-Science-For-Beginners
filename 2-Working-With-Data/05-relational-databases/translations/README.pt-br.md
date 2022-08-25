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

Com os nossos dados separados em duas tabelas, você pode se perguntar como acessá-los. Se usarmos uma base de dados relacional, como MySQL, SQL Server ou Oracle, podemos usar uma linguagem chamada Structured Query Language (Linguagem de Consulta Estruturada) ou SQL. A SQL (às vezes lida como "sequel" em inglês) é uma linguagem padronizada para buscar e modificar dados em uma base de dados relacional.

Para buscar dados, usamos o comando `SELECT` (que significa "selecionar"). No fundo, você **seleciona** as colunas que você quer ver **desde** a tabela em que elas estão contidas. Se você quer apenas mostrar os nomes das cidades, você pode usar o seguinte comando:   

```sql
SELECT cidade
FROM cidades;

-- Resultado:
-- Tóquio
-- Atlanta
-- Auckland
```

`SELECT` é onde você lista as colunas, e `FROM` é onde você lista as tabelas.

> [NOTE] A sintaxe de SQL não é sensível a maiúsculas e minúsculas, que significa que  `select` e `SELECT` são a mesma coisa. Entretanto, dependendo do tipo de base de dados que você usa, as colunas e tabelas podem ser sensíveis a maiúsculas e minúsculas. Por causa disso, é uma boa prática sempre presumir que tudo em programação é sensível. Quando se escreve uma query (consulta) em SQL, a convenção é usar as palavras-chave todas em maiúsculas.

A query acima mostrará todas as cidades. Imaginemos que só queremos mostrar as cidades da Nova Zelândia. Vamos precisar de alguma forma de filtro. A palavra-chave em SQL para isso é `WHERE` ("onde"), ou  "onde certa afirmação é verdadeira".

```sql
SELECT cidade
FROM cidades
WHERE pais = 'Nova Zelândia';

-- Resultado:
-- Auckland
```

## Juntando dados

Até agora nós conseguimos buscar dados de uma única tabela. Agora queremos juntas or dados de ambas as tabelas **cidades** e **precipitacao**. Isso se faz juntando (em inglês, "*joining*") elas. Dessa forma você vai "costurar" as duas tabelas, e combinar os valoras de uma coluna de cada tabela.

Em nosso exemplo, vamos combinar a coluna **cidade_id** em **precipitacao** com a coluna **cidade_id** em **cidades**. Isso irá combinar a precipitação com sua respectiva cidade. O tipo de "join" que faremos é chamado de *inner* join ("juntar internamente"), que significa que caso as linhas não combinem com nada da outra tabela, elas não serão mostradas. No nosso caso, cada cidade tem uma precipitação, então tudo será mostrado.

Agora vamos buscar a precipitação em 2019 para todas as nossas cidades.

Faremos isso em alguns passos. O primeiro passo é juntar os dados indicando as colunas para a "costura" - **cidade_id** como dito anteriormente.


```sql
SELECT cidades.cidade
    precipitacao.quantidade
FROM cidades
    INNER JOIN precipitacao ON cidades.cidade_id = precipitacao.cidade_id
```

Escolhemos as duas colunas que queremos, e o fato de querermos juntar as tabelas pelo **cidade_id**. Agora podemos adicionar o `WHERE` para filtrar apenas o ano 2019.

```sql
SELECT cidades.cidade
    precipitacao.quantidade
FROM cidades
    INNER JOIN precipitacao ON cidades.cidade_id = precipitacao.cidade_id
WHERE precipitacao.ano = 2019

-- Resultado

-- cidade   | quantidade
-- -------- | ------
-- Tóquio   | 1874
-- Atlanta  | 1111
-- Auckland |  942
```

## Resumo
Bases de dados relacionais funcionam dividindo a informação entre várias tabelas, que depois são juntas novamente para serem mostradas e analizadas. Isso nos dá um alto grau de flexibilidade para fazer cálculos e manipular dados. Você viu os principais conceitos de uma base de dados relacional, e como fazer um "join" entre duas tabelas.


## 🚀 Desafio

Há muitas bases de dados relacionais disponíveis na internet. Você pode explorar os dados usando as técnicas que você aprendeu acima. 


## Quiz Pós-Aula

## [Quiz pós-aula](https://red-water-0103e7a0f.azurestaticapps.net/quiz/9)

## Revisão & Auto-Estudo

Há muitos recursos em [Microsoft Learn](https://docs.microsoft.com/learn?WT.mc_id=academic-40229-cxa) para você continuar sua exploração sobre SQL e conceitos de bases de dados relacionais.

- [Descreva conceitos de bases de dados relacionais](https://docs.microsoft.com//learn/modules/describe-concepts-of-relational-data?WT.mc_id=academic-40229-cxa)
- [Comece a fazer queries com Transact-SQL](https://docs.microsoft.com//learn/paths/get-started-querying-with-transact-sql?WT.mc_id=academic-40229-cxa) (Transact-SQL é uma versão de SQL)
- [Conteúdo de SQL em Microsoft Learn](https://docs.microsoft.com/learn/browse/?products=azure-sql-database%2Csql-server&expanded=azure&WT.mc_id=academic-40229-cxa)

## Trabalho

[Título do Trabalho](assignment.md)
