# Definindo Dados

|![ Sketchnote por [(@sketchthedocs)](https://sketchthedocs.dev) ](../../../sketchnotes/03-DefiningData.png)|
|:---:|
|Definindo Dados - _Sketchnote por [@nitya](https://twitter.com/nitya)_ |

Dados são fatos, informações, observações e medidas que são usadas para fazer descobertas e apoiar decisões informadas. Um ponto de dado é uma unidade única dentro de um dataset, que é uma coleção de pontos de dados. Datasets podem vir em diferentes formatos e estruturas, e normalmente será baseado em sua fonte, ou de onde os dados vieram. Por exemplo, os ganhos mensais de uma empresa podem estar em uma planilha mas a frequência cardíaca (por hora) de um smartwatch pode estar em formato [JSON](https://stackoverflow.com/a/383699). É comum para cientistas de dados terem que trabalhar com diferentes tipos de dados em um dataset.

Essa aula irá focar em identificar e classificar dados baseados em sua características e fontes.

## [Quiz Pré Aula](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/4)
## Como Dados são Descritos
**Dados Brutos (Raw data)** são dados que vieram em seu estado inicial de sua fonte e não foram analisados ou organizados. Para entender o que está acontecendo com um conjunto de dados, é necessário organizar os dados em um formato que possa ser entendido pelos humanos e também pela tecnologia que pode ser usada para analisar os mesmos. A estrutura do dataset descreve como estão organizados e pode ser classificada em estruturada, não estruturada e semi estruturada. Esses tipos de estruturas irão variar, dependendo da fonte mas irão ultimamente se encaixar nessas categorias.

### Dados Qualitativos
Dados qualitativos, também conhecidos como dados categóricos são dados que não podem ser medidos objetivamente como observações de dados quantitativos. São geralmente vários formatos de dados subjetivos que coletam a qualidade de algo, como um produto ou processo. Algumas vezes, dados qualitativos são numéricos e tipicamente não seriam usados matematicamente, como números de telefones e marcas de tempo. Alguns exemplos de dados qualitativos são: comentários de vídeos, a marca e modelo de um carro e a cor favorita do seu melhor amigo. Dados qualitativos podem ser usados para entender quais produtos os consumidores mais gostam ou identificar palavras-chaves populares em cúrriculos para aplicação em uma vaga de trabalho.

### Dados Estruturados
Dados estruturados são dados que estão organizados em linhas e colunas, onde cada linha tem a mesma quantidade de colunas. Colunas representam um valor de um tipo particular e são identificadas com um nome descrevendo o que aquele valor representa, enquanto cada linha contém o valor. Colunas geralmente vão possuir um conjunto específico de regras e restrições nesses valores, para garantir que os valores representam precisamente a coluna. Por exemplo, imagine uma planilha de clientes onde cada linha deve ter um número de telefone e o mesmo nunca pode conter caractéres alfabéticos. Podem existir regras aplicadas na coluna do número de telefone para garantir que nunca esteja vazio e contenha apenas números.

Um benefício de dados estruturados é que podem ser organizados de uma forma que pode ser relacionada a um outro dado estruturado. No entanto, devido ao fato dos dados serem feitos para serem organizados de uma forma específica, fazer mudanças na estrutura em geral pode requerer muito esforço. Por exemplo, adicionar uma coluna de email na planilha de clientes que não pode ser vazia, significa que você terá que decidir como você irá adicionar os valores nas linhas já existentes no dataset.

Exemplos de dados estruturados: planilhas/spreadsheets, bancos de dados relacionais, números de telefone, extratos bancários

### Dados Não Estruturados
Dados não estruturados tipicamente não podem ser categorizado em linhas e colunas e não possuem um formato ou um conjunto de regras a ser seguido. Devido ao fato de dados não estruturados possuirem menos restrições na sua estrutura é mais fácil adicionar novas informações quando comparados com um dataset estruturado. Se um sensor que coleta dados de pressão bariométrica a cada 2 minutos recebeu uma atualização que agora permite que o mesmo meça e grave a temperatura, não é preciso alterar os dados já existentes se eles são não estruturados. No entanto, isso pode fazer com que a análise ou investigação desses dados leve mais tempo. Por exemplo, um cientista que quer descobrir a temperatura média do mês passado a partir dos dados do sensor, mas descobre que o sensor gravou um "e" em alguns dados gravados indicando que estava quebrado ao invés de um número típico, o que significa que os dados estão incompletos.

Exemplos de dados não estruturados: arquivos de texto, mensagens de texto, arquivo de vídeo

### Dados Semi Estruturados
Dados semi estruturados possui recursos que o fazem ser uma combinação de dados estruturados e não estruturados. Tipicamente não está em conformidade com linhas e colunas mas estão organizados de uma forma que são considerados estruturados e podem seguir um formato fizo ou um conjunto de regras. A estrutura pode variar entre as fontes, desde uma hierarquia bem definida até algo mais flexível que permite uma fácil integração de novas informação. Metadados são indicadores que ajudam a decidir como os dados são organizados e armazenados e terão vários nomes, baseado no tipo de dado. Alguns nomes comuns para metadados são tags, elementos, entidades e atributos. Por exemplo, uma mensaem de email típica terá um assunto, corpo e um conjunto de recipientes e podem ser organizados por quem ou quando foi mandado.

Exemplos de dados não estruturados: HTML, arquivos CSV, JavaScript Object Notation (JSON)

## Fontes de Dados

Uma fonte de dados é o local inicial onde os dados foram gerados, ou onde "vivem" e irá variar com base em como e quando foram coletados. Dados gerados por seus usuários são conhecidos como dados primários enquanto dados secundários vem de uma fonte que coletou os dados para uso geral. Por exemplo, um grupo de cientistas fazendo observações em uma floresta tropical seriam considerados dados primários e se eles decidirem compartilhar com outros cientistas seriam considerados dados secundários para aqueles que usarem.

Banco de dados são fontes comuns e dependem de um sistema de gerenciamente de banco de dados para hospedar e manter os dados onde usuários usam comandos chamados de "queries" para explorar os dados. Arquivos como fonte de dados podem ser aúdio, imagens, e arquivos de vídeo assim como planilhas como o Excel. Fontes da internet são lugares comuns para hospedar dados, onde banco de dados e arquivos podem ser encontrados. Application programming interfaces, ou APIs, permitem programadores a criarem formas de compartilhar dados com usuários externos através da interet, enquanto processos de "web scraping" extrai dados de uma página da web. As [tarefas em Trabalhando com Dados](../../../2-Working-With-Data) focam em como usar várias fontes de dados.

## Conclusão

Nessa aula nós aprendemos:

- O que são dados
- Como dados são descritos
- Como dados são classificados e categorizados
- Onde os dados podem ser encontrados

## 🚀 Desafio

O Kaggle é uma excelente fonte para datasets abertos. Use a [ferramenta de busca de dataset](https://www.kaggle.com/datasets) para encontrar alguns datasets interessantes e classificar de três a cinco datasets com esses critérios:

- Os dados são quantitativos ou qualitativos?
- Os dados são estruturados, não estruturados, ou semi estruturados?

## [Quiz Pós Aula](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/5)



## Revisão e Auto Estudo

- Essa unidade do Microsoft Lean, entitulada [Classifique seus Dados (Classify your Data)](https://docs.microsoft.com/en-us/learn/modules/choose-storage-approach-in-azure/2-classify-data) tem uma análise detalhada de dados estruturados, semi estruturados, e não estruturados.

## Tarefa

[Classificando Datasets](assignment.pt-br.md)
