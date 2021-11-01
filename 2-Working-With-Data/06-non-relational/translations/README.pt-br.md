# Trabalhando com dados: Dados não-relacionais

|![ Ilustrado por [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/06-NoSQL.png)|
|:---:|
|Trabalhando com dados NoSQL - _Ilustrado por [@nitya](https://twitter.com/nitya)_ |

## [Quiz pré-aula](https://red-water-0103e7a0f.azurestaticapps.net/quiz/10)

Dados não estão limitados a bancos de dados relacionais. Esta aula foca em dados não-relacionais e vai cobrir o básico de planilhas e NoSQL.

## Planilhas

Planilhas são uma forma popular de armazenar e explorar dados porque elas requerem menos trabalho para configurar e começar.
Nesta aula você irá aprender os componentes básicos de uma planilha, assim como fórmulas e funções. Os exemplos serão ilustrados com Microsoft Excel, porém a maioria das partes e tópicos terão nomes e passos similares em comparação com outros softwares de planilhas.

![Uma aba de Microsoft Excel com duas planilhas](images/parts-of-spreadsheet.png)

Uma planilha é um arquivo e é acessível através do sistema de arquivos de um computador, dispositivo, ou sistema de arquivos baseado em nuvem. O software em si pode ser baseado em navegador ou em uma aplicação que deve ser instalada em um computador ou baixada como um app. No Excel, estes arquivos também podem ser definidos como **arquivo Excel** e esta terminologia será usada até o final desta aula.

Um arquivo Excel contém uma ou mais **planilhas Excel**, onde cada planilha é dividida por abas. Dentro de uma planilha existem retângulos chamados de **células**, as quais irão conter os dados propriamente ditos. Uma célula é uma intersecção de uma linha e coluna, na qual as colunas são nomeadas com caracteres em ordem alfabética e linhas são nomeadas numericamente. Algumas planilhas conterão cabeçalhos nas primeiras linhas para descrever os dados de uma célula.

Com estes elementos básicos de um arquivo Excel, nós usaremos um exemplo vindo dos [Modelos Microsoft](https://templates.office.com/) focado em um inventário para explicar aguns detalhes adicionais de uma planilha.

### Administrando um inventário

O arquivo de planilhas chamado de "InventoryExample" é um arquivo formatado de itens de um inventário que contém três planilhas, onde as abas estão nomeadas como "Inventory List", "Inventory Pick List" e "Bin Lookup". A linha 4 da planilha Inventory List é o cabeçalho, o qual descreve o valor de cada célula da coluna.

![Uma fórmula realçada de um exemplo de listagem de invetário no Microsoft Excel](images/formula-excel.png)

Existem situações nas quais uma célula depende do valor de outras células para gerar seu valor. A planilha Inventory List mantém o controle do custo de cada item em seu inventário, mas e se nós precisarmos saber o valor de todas as coisas no inventário? [**Fórmulas**](https://support.microsoft.com/en-us/office/overview-of-formulas-34519a4e-1e8d-4f4b-84d4-d642c4f63263) realizam ações nos dados das células e são usadas para calcular o custo do inventário, neste exemplo. Esta planilha usou uma fórmula na coluna Inventory Value para calcular o valor de cada item através da multiplicação da quantidade abaixo do cabeçalho QTY e seu custo pelas células abaixo do cabeçalho COST. Clicar duas vezes (ou 'realçar') uma célula faz com que a fórmula seja mostrada. Você perceberá que fórmulas começam com um sinal de 'igual', seguido do cálculo ou operação.

![Uma função realçada de um exemplo de listagem de invetário no Microsoft Excel](images/function-excel.png)

Nós podemos usar outra fórmula para adicionar todos os valores de Inventory Value para pegar seu valor total. Isso poderia ser calculado adicionando cada célula para gerar a soma, mas essa pode ser uma tarefa tediosa. O Excel tem [**funções**](https://support.microsoft.com/en-us/office/sum-function-043e1c7d-7726-4e80-8f32-07b23e057f89), ou fórmulas pré-definidas para performar cálculos no valor de células. Funções requerem argumentos, os quais são os valores obrigatórios para realizar esses cálculos. Quando as funções requerem mais e um argumento, eles devem ser listados numa ordem específica, senão a função pode não calculá-los corretamente. Este exemplo usa a função SUM, e usa os valores de Inventory Value como argumento para gerar o Total, listado abaixo da linha 3, coluna B (também chamado de B3).

## NoSQL
NoSQL é um termo 'guarda-chuva' para as diferentes formas de armazenar dados não-relacionais e pode ser interpretado como "não-SQL", "não-relacional" ou "não apenas SQL". Estes tipos de sistema de banco de dados podem ser categorizados em 4 tipos.

![Representação gráfica de um armazenamento chave-valor mostrando 4 chaves numéricas únicas que são associadas com 4 diferentes valores](images/kv-db.png)
> Fonte: [Michał Białecki Blog](https://www.michalbialecki.com/2018/03/18/azure-cosmos-db-key-value-database-cloud/)

[Bancos de dados chave-valor](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#keyvalue-data-stores) (key-value) atrelam chaves únicas (unique keys), as quais são identificadores únicos, a um determinado valor. Esses pares são armazenados utilizando uma [Tabela de dispersão](https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/tutorial/) (Hash table) com uma função 'hash' apropriada.

![Representação gráfica de um armazenamento de dados de gráfico mostrando os relacionamentos entre pessoas, seus interesses e locais](images/graph-db.png)
> Fonte: [Microsoft](https://docs.microsoft.com/en-us/azure/cosmos-db/graph/graph-introduction#graph-database-by-example)

[Bancos de dados de Gráfico](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#graph-data-stores) descrevem relacionamentos entre dados e são representados como uma coleção de nós e arestas. Um nó representa uma entidade, algo que exista no mundo real, como um estudante ou um extrato bancário. Arestas representam o relacionamento entre duas entidades. Cada nó e aresta possui propriedades que provêem informações adicionais sobre eles.

![Representação gráfica de um armazenamento de dados orientado a colunas mostrando um banco de dados de clientes com duas famílias de colunas chamadas de Identity e Contact Info](images/columnar-db.png)

[Bancos de dados orientados a colunas](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#columnar-data-stores) organizam dados em colunas e linhas como uma estrutura de dados relacional, mas cada column é dividida em um grupo de colunas chamado de Família de Colunas, onde todos os dados abaixo de uma determinada coluna é relacionado e pode ser buscado e modificado de uma vez só.

### Banco de dados orientado a Documentos com Azure Cosmos DB 

[Banco de dados orientado a Documentos](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#document-data-stores) são construídos a partir do conceito de um armazenamento de dados chave-valor e é feito de uma série de campos e objetos. Esta seção irá explorar bancos de dados orientado a documentos com a ferramenta Cosmos DB emulator.

Um banco de dados do Cosmos DB cabe na definição de "Não apenas SQL", onde o banco de dados orientado a documentos do Cosmos DB depende de SQL para consultar os dados. A [aula anterior](../05-relational-databases/README.md) sobre SQL cobre o básico da linguagem, e nós poderemos aplicar algumas das mesmas consultas para um banco de dados de documentos aqui. Nós usaremos o Cosmos DB Emulator, o qual possibilita criar e explorar um banco de dados de documentos localmente no computador. Leia mais sobre o emulador [aqui](https://docs.microsoft.com/en-us/azure/cosmos-db/local-emulator?tabs=ssl-netstd21).

Um documento é uma coleção de campos e valores de objeto, onde os campos descrevem o que o valor do objeto representa. Abaixo está o exemplo de um documento.

```json
{
    "firstname": "Eva",
    "age": 44,
    "id": "8c74a315-aebf-4a16-bb38-2430a9896ce5",
    "_rid": "bHwDAPQz8s0BAAAAAAAAAA==",
    "_self": "dbs/bHwDAA==/colls/bHwDAPQz8s0=/docs/bHwDAPQz8s0BAAAAAAAAAA==/",
    "_etag": "\"00000000-0000-0000-9f95-010a691e01d7\"",
    "_attachments": "attachments/",
    "_ts": 1630544034
}
```
Os campos de interesse neste documento são `firstname` (primeiro nome), `age` (idade) e id. O resto dos campos com o underscore foram gerados pelo Cosmos DB.

#### Explorando dados com o Cosmos DB Emulator

Você pode baixar e instalar o emulador para Windows [aqui](https://aka.ms/cosmosdb-emulator). Siga a [documentação](https://docs.microsoft.com/en-us/azure/cosmos-db/local-emulator?tabs=ssl-netstd21#run-on-linux-macos) para opções de como rodar o emulador para macOS e Linux.

O emulador abre uma janela de navegador, onde a visão Explorer lhe permite explorar documentos.

![A visão Explorer do Cosmos DB Emulator](images/cosmosdb-emulator-explorer.png)

Se você está acompanhando, clique em "Start with Sample" para gerar um banco de dados de amostra chamado de SampleDB. Se você expandir SampleDB clicando na flecha, você irá encontrar um container chamado `Persons`. Um container armazena uma coleção de items, que são os documentos dentro do container. Você pode explorar os quatro documentos individuais em `Items`.

![Explorando dados de exemplo no Cosmos DB Emulator](images/cosmosdb-emulator-persons.png)

#### Consultando Dados de Documento com o Cosmos DB Emulator

Nós também podemos consultar os dados de amostra clicando no novo botão SQL Query (segundo botão a partir da esquerda).

`SELECT * FROM c` retorna todos os documentos no container. Vamos adicionar uma cláusula 'where' e encontrar todas as pessoas mais novas que 40 anos.

`SELECT * FROM c where c.age < 40`

 ![Rodando um SELECT em dados de amostra no Cosmos DB Emulator para encontrar documentos com o valor do campo 'age' menor que 40](images/cosmosdb-emulator-persons-query.png)

A consulta retorna dois documentos, note que o valor de 'age' para cada documento é menor que 40.

#### JSON e Documentos

Se você está familiarizado com JavaScript Object Notation (JSON) você irá perceber que documentos são muito similares a JSONs. Há um arquivo chamado `PersonsData.json` neste diretório com mais dados que você pode upar para o container Persons no emulador através do botão `Upload Item`.

Na maioria das vezes, APIs que retornam dados JSON podem ser diretamente transferidas e armazenadas em bancos de dados de documentos. Abaixo há um outro documento, ele representa tweets da conta do Twitter da Microsoft que foram buscados usando a Twitter API, e então inseridos no CosmosDB.

```json
{
    "created_at": "2021-08-31T19:03:01.000Z",
    "id": "1432780985872142341",
    "text": "Blank slate. Like this tweet if you’ve ever painted in Microsoft Paint before. https://t.co/cFeEs8eOPK",
    "_rid": "dhAmAIUsA4oHAAAAAAAAAA==",
    "_self": "dbs/dhAmAA==/colls/dhAmAIUsA4o=/docs/dhAmAIUsA4oHAAAAAAAAAA==/",
    "_etag": "\"00000000-0000-0000-9f84-a0958ad901d7\"",
    "_attachments": "attachments/",
    "_ts": 1630537000
```

Os campos de interesse neste documento são: `created_at`, `id`, e `text`.

## 🚀 Desafio


Há um arquivo `TwitterData.json` que você pode upar para o banco de dados SampleDB. É recomendado que você o adicione a um container separado. Isto pode ser feito por:

1. Clicar no botão 'new container' no canto superior direito
1. Selecionar o banco de dados existente (SampleDB), criando um container id para o container
1. Definir a chave de partição (partition key) para `/id`
1. Clicar em OK (você pode ignorar o resto da informação nesta visão pois é um dataset pequeno rodando localmente na sua máquina)
1. Abrir seu novo container e upar o arquivo Twitter Data no botão `Upload Item`

Tente rodar algumas consultas 'select' para encontra os documentos que possuem Microsoft no campo 'text'. Dica: tente usar a palavra-chave [LIKE](https://docs.microsoft.com/en-us/azure/cosmos-db/sql/sql-query-keywords#using-like-with-the--wildcard-character)


## [Quiz pós-aula](https://red-water-0103e7a0f.azurestaticapps.net/quiz/11)



## Revisão e auto-estudo

- Existem alguns recursos de formatação adicionais adicionados a esta planilha que esta aula não cobre. A Microsoft tem uma [vasta biblioteca de documentação e vídeos](https://support.microsoft.com/excel) sobre Excel se você estiver interessado em aprender mais.

- Esta documentação arquitetural detalha as características dos diferentes tipos de dados não-relacionais: [Dados não-relacionais e NoSQL](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data)

- Cosmos DB é uma base de dados não relacionais baseada em nuvem que também consegue guardar os diferentes tipos NoSQL mencionados nesta aula. Aprenda mais sobre estes tipos neste [Módulo de aprendizado Microsoft Cosmos DB](https://docs.microsoft.com/en-us/learn/paths/work-with-nosql-data-in-azure-cosmos-db/)

## Exercício

[Lucros de refrigerante](assignment.md)
