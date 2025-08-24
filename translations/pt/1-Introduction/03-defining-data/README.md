<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "356d12cffc3125db133a2d27b827a745",
  "translation_date": "2025-08-24T00:00:03+00:00",
  "source_file": "1-Introduction/03-defining-data/README.md",
  "language_code": "pt"
}
-->
# Definindo Dados

|![ Sketchnote por [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/03-DefiningData.png)|
|:---:|
|Definindo Dados - _Sketchnote por [@nitya](https://twitter.com/nitya)_ |

Dados são factos, informações, observações e medições que são utilizados para fazer descobertas e apoiar decisões informadas. Um ponto de dados é uma unidade única de dados dentro de um conjunto de dados, que é uma coleção de pontos de dados. Conjuntos de dados podem ter diferentes formatos e estruturas, geralmente baseados na sua origem ou na fonte dos dados. Por exemplo, os rendimentos mensais de uma empresa podem estar numa folha de cálculo, enquanto os dados de frequência cardíaca por hora de um smartwatch podem estar no formato [JSON](https://stackoverflow.com/a/383699). É comum que cientistas de dados trabalhem com diferentes tipos de dados dentro de um conjunto de dados.

Esta lição foca-se em identificar e classificar dados pelas suas características e pelas suas fontes.

## [Questionário Pré-Aula](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/4)

## Como os Dados são Descritos

### Dados Brutos
Dados brutos são dados que vêm da sua fonte no estado inicial e que não foram analisados ou organizados. Para compreender o que está a acontecer num conjunto de dados, é necessário organizá-lo num formato que possa ser entendido por humanos, bem como pela tecnologia que pode ser usada para analisá-lo mais profundamente. A estrutura de um conjunto de dados descreve como ele está organizado e pode ser classificada como estruturada, não estruturada e semi-estruturada. Estes tipos de estrutura variam dependendo da fonte, mas encaixam-se, em última instância, nestas três categorias.

### Dados Quantitativos
Dados quantitativos são observações numéricas dentro de um conjunto de dados e podem, geralmente, ser analisados, medidos e utilizados matematicamente. Alguns exemplos de dados quantitativos são: a população de um país, a altura de uma pessoa ou os rendimentos trimestrais de uma empresa. Com alguma análise adicional, dados quantitativos podem ser usados para descobrir tendências sazonais do Índice de Qualidade do Ar (AQI) ou estimar a probabilidade de trânsito na hora de ponta num dia típico de trabalho.

### Dados Qualitativos
Dados qualitativos, também conhecidos como dados categóricos, são dados que não podem ser medidos objetivamente como as observações de dados quantitativos. Geralmente, são vários formatos de dados subjetivos que capturam a qualidade de algo, como um produto ou processo. Por vezes, dados qualitativos são numéricos, mas não seriam normalmente utilizados matematicamente, como números de telefone ou marcas de tempo. Alguns exemplos de dados qualitativos são: comentários em vídeos, a marca e modelo de um carro ou a cor favorita dos seus amigos mais próximos. Dados qualitativos podem ser usados para compreender quais produtos os consumidores preferem ou identificar palavras-chave populares em currículos de candidaturas de emprego.

### Dados Estruturados
Dados estruturados são dados organizados em linhas e colunas, onde cada linha terá o mesmo conjunto de colunas. As colunas representam um valor de um tipo específico e serão identificadas com um nome que descreve o que o valor representa, enquanto as linhas contêm os valores reais. As colunas frequentemente têm um conjunto específico de regras ou restrições sobre os valores, para garantir que os valores representam com precisão a coluna. Por exemplo, imagine uma folha de cálculo de clientes onde cada linha deve ter um número de telefone e os números de telefone nunca contêm caracteres alfabéticos. Podem ser aplicadas regras na coluna de número de telefone para garantir que nunca está vazia e contém apenas números.

Uma vantagem dos dados estruturados é que podem ser organizados de forma a serem relacionados com outros dados estruturados. No entanto, como os dados são projetados para serem organizados de uma forma específica, fazer alterações na sua estrutura geral pode exigir muito esforço. Por exemplo, adicionar uma coluna de email à folha de cálculo de clientes que não pode estar vazia significa que será necessário descobrir como adicionar esses valores às linhas existentes de clientes no conjunto de dados.

Exemplos de dados estruturados: folhas de cálculo, bases de dados relacionais, números de telefone, extratos bancários.

### Dados Não Estruturados
Dados não estruturados geralmente não podem ser categorizados em linhas ou colunas e não contêm um formato ou conjunto de regras a seguir. Como os dados não estruturados têm menos restrições na sua estrutura, é mais fácil adicionar novas informações em comparação com um conjunto de dados estruturado. Se um sensor que captura dados sobre pressão barométrica a cada 2 minutos receber uma atualização que agora permite medir e registar temperatura, não será necessário alterar os dados existentes se forem não estruturados. No entanto, isso pode tornar a análise ou investigação deste tipo de dados mais demorada. Por exemplo, um cientista que deseja encontrar a temperatura média do mês anterior nos dados do sensor, mas descobre que o sensor registou um "e" em alguns dos seus dados para indicar que estava avariado, em vez de um número típico, o que significa que os dados estão incompletos.

Exemplos de dados não estruturados: ficheiros de texto, mensagens de texto, ficheiros de vídeo.

### Dados Semi-Estruturados
Dados semi-estruturados têm características que os tornam uma combinação de dados estruturados e não estruturados. Geralmente, não seguem um formato de linhas e colunas, mas são organizados de uma forma considerada estruturada e podem seguir um formato fixo ou conjunto de regras. A estrutura varia entre fontes, como uma hierarquia bem definida ou algo mais flexível que permite uma fácil integração de novas informações. Metadados são indicadores que ajudam a decidir como os dados são organizados e armazenados e terão vários nomes, dependendo do tipo de dados. Alguns nomes comuns para metadados são tags, elementos, entidades e atributos. Por exemplo, uma mensagem de email típica terá um assunto, corpo e um conjunto de destinatários e pode ser organizada por quem ou quando foi enviada.

Exemplos de dados semi-estruturados: HTML, ficheiros CSV, JavaScript Object Notation (JSON).

## Fontes de Dados

Uma fonte de dados é o local inicial onde os dados foram gerados ou onde "vivem" e varia com base em como e quando foram recolhidos. Dados gerados pelos seus utilizadores são conhecidos como dados primários, enquanto dados secundários vêm de uma fonte que recolheu dados para uso geral. Por exemplo, um grupo de cientistas que recolhe observações numa floresta tropical seria considerado primário e, se decidirem partilhá-lo com outros cientistas, seria considerado secundário para aqueles que o utilizam.

Bases de dados são uma fonte comum e dependem de um sistema de gestão de bases de dados para hospedar e manter os dados, onde os utilizadores utilizam comandos chamados consultas para explorar os dados. Ficheiros como fontes de dados podem ser ficheiros de áudio, imagem e vídeo, bem como folhas de cálculo como Excel. Fontes da internet são um local comum para hospedar dados, onde bases de dados e ficheiros podem ser encontrados. Interfaces de programação de aplicações, também conhecidas como APIs, permitem que programadores criem formas de partilhar dados com utilizadores externos através da internet, enquanto o processo de web scraping extrai dados de uma página web. As [lições em Trabalhar com Dados](../../../../../../../../../2-Working-With-Data) focam-se em como utilizar várias fontes de dados.

## Conclusão

Nesta lição aprendemos:

- O que são dados
- Como os dados são descritos
- Como os dados são classificados e categorizados
- Onde os dados podem ser encontrados

## 🚀 Desafio

O Kaggle é uma excelente fonte de conjuntos de dados abertos. Utilize a [ferramenta de pesquisa de conjuntos de dados](https://www.kaggle.com/datasets) para encontrar alguns conjuntos de dados interessantes e classifique 3-5 conjuntos de dados com este critério:

- Os dados são quantitativos ou qualitativos?
- Os dados são estruturados, não estruturados ou semi-estruturados?

## [Questionário Pós-Aula](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/5)

## Revisão e Autoestudo

- Esta unidade do Microsoft Learn, intitulada [Classifique os seus Dados](https://docs.microsoft.com/en-us/learn/modules/choose-storage-approach-in-azure/2-classify-data), tem uma explicação detalhada sobre dados estruturados, semi-estruturados e não estruturados.

## Tarefa

[Classificar Conjuntos de Dados](assignment.md)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original no seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se uma tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes do uso desta tradução.