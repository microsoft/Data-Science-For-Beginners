<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "356d12cffc3125db133a2d27b827a745",
  "translation_date": "2025-08-27T17:20:31+00:00",
  "source_file": "1-Introduction/03-defining-data/README.md",
  "language_code": "br"
}
-->
# Definindo Dados

|![ Sketchnote por [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/03-DefiningData.png)|
|:---:|
|Definindo Dados - _Sketchnote por [@nitya](https://twitter.com/nitya)_ |

Dados são fatos, informações, observações e medições que são usados para fazer descobertas e apoiar decisões informadas. Um ponto de dado é uma unidade única de dados dentro de um conjunto de dados, que é uma coleção de pontos de dados. Conjuntos de dados podem vir em diferentes formatos e estruturas, geralmente baseados em sua origem ou de onde os dados vieram. Por exemplo, os ganhos mensais de uma empresa podem estar em uma planilha, enquanto os dados de frequência cardíaca por hora de um smartwatch podem estar no formato [JSON](https://stackoverflow.com/a/383699). É comum que cientistas de dados trabalhem com diferentes tipos de dados dentro de um conjunto de dados.

Esta lição foca em identificar e classificar dados por suas características e suas fontes.

## [Quiz Pré-Aula](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/4)

## Como os Dados são Descritos

### Dados Brutos
Dados brutos são dados que vêm de sua fonte em seu estado inicial e não foram analisados ou organizados. Para entender o que está acontecendo com um conjunto de dados, ele precisa ser organizado em um formato que possa ser compreendido por humanos, bem como pela tecnologia que pode ser usada para analisá-lo mais profundamente. A estrutura de um conjunto de dados descreve como ele está organizado e pode ser classificada como estruturada, não estruturada e semiestruturada. Esses tipos de estrutura variam dependendo da fonte, mas geralmente se encaixam nessas três categorias.

### Dados Quantitativos
Dados quantitativos são observações numéricas dentro de um conjunto de dados e podem ser analisados, medidos e usados matematicamente. Alguns exemplos de dados quantitativos são: a população de um país, a altura de uma pessoa ou os ganhos trimestrais de uma empresa. Com alguma análise adicional, dados quantitativos podem ser usados para descobrir tendências sazonais do Índice de Qualidade do Ar (AQI) ou estimar a probabilidade de tráfego no horário de pico em um dia típico de trabalho.

### Dados Qualitativos
Dados qualitativos, também conhecidos como dados categóricos, são dados que não podem ser medidos objetivamente como observações de dados quantitativos. Geralmente são formatos variados de dados subjetivos que capturam a qualidade de algo, como um produto ou processo. Às vezes, dados qualitativos são numéricos, mas não seriam usados matematicamente, como números de telefone ou marcas de tempo. Alguns exemplos de dados qualitativos são: comentários em vídeos, a marca e modelo de um carro ou a cor favorita dos seus amigos mais próximos. Dados qualitativos podem ser usados para entender quais produtos os consumidores mais gostam ou identificar palavras-chave populares em currículos de candidatos a emprego.

### Dados Estruturados
Dados estruturados são organizados em linhas e colunas, onde cada linha terá o mesmo conjunto de colunas. As colunas representam um valor de um tipo específico e serão identificadas com um nome que descreve o que o valor representa, enquanto as linhas contêm os valores reais. As colunas frequentemente têm um conjunto específico de regras ou restrições sobre os valores, para garantir que os valores representem com precisão a coluna. Por exemplo, imagine uma planilha de clientes onde cada linha deve ter um número de telefone e os números de telefone nunca contêm caracteres alfabéticos. Podem haver regras aplicadas na coluna de número de telefone para garantir que ela nunca esteja vazia e contenha apenas números.

Um benefício dos dados estruturados é que eles podem ser organizados de forma que possam ser relacionados a outros dados estruturados. No entanto, como os dados são projetados para serem organizados de uma maneira específica, fazer alterações em sua estrutura geral pode exigir muito esforço. Por exemplo, adicionar uma coluna de e-mail à planilha de clientes que não pode estar vazia significa que você precisará descobrir como adicionar esses valores às linhas existentes de clientes no conjunto de dados.

Exemplos de dados estruturados: planilhas, bancos de dados relacionais, números de telefone, extratos bancários.

### Dados Não Estruturados
Dados não estruturados geralmente não podem ser categorizados em linhas ou colunas e não contêm um formato ou conjunto de regras a seguir. Como os dados não estruturados têm menos restrições em sua estrutura, é mais fácil adicionar novas informações em comparação a um conjunto de dados estruturado. Se um sensor que captura dados de pressão barométrica a cada 2 minutos recebeu uma atualização que agora permite medir e registrar temperatura, isso não exige alteração nos dados existentes se forem não estruturados. No entanto, isso pode tornar a análise ou investigação desse tipo de dado mais demorada. Por exemplo, um cientista que deseja encontrar a temperatura média do mês anterior nos dados do sensor, mas descobre que o sensor registrou um "e" em alguns de seus dados para indicar que estava quebrado, em vez de um número típico, o que significa que os dados estão incompletos.

Exemplos de dados não estruturados: arquivos de texto, mensagens de texto, arquivos de vídeo.

### Dados Semiestruturados
Dados semiestruturados têm características que os tornam uma combinação de dados estruturados e não estruturados. Eles geralmente não seguem um formato de linhas e colunas, mas são organizados de uma maneira considerada estruturada e podem seguir um formato fixo ou conjunto de regras. A estrutura varia entre as fontes, como uma hierarquia bem definida ou algo mais flexível que permite fácil integração de novas informações. Metadados são indicadores que ajudam a decidir como os dados são organizados e armazenados e terão vários nomes, dependendo do tipo de dado. Alguns nomes comuns para metadados são tags, elementos, entidades e atributos. Por exemplo, uma mensagem de e-mail típica terá um assunto, corpo e um conjunto de destinatários e pode ser organizada por quem ou quando foi enviada.

Exemplos de dados semiestruturados: HTML, arquivos CSV, JavaScript Object Notation (JSON).

## Fontes de Dados

Uma fonte de dados é o local inicial de onde os dados foram gerados ou onde "vivem" e varia com base em como e quando foram coletados. Dados gerados por seus usuários são conhecidos como dados primários, enquanto dados secundários vêm de uma fonte que coletou dados para uso geral. Por exemplo, um grupo de cientistas coletando observações em uma floresta tropical seria considerado primário, e se decidirem compartilhá-lo com outros cientistas, seria considerado secundário para aqueles que o utilizam.

Bancos de dados são uma fonte comum e dependem de um sistema de gerenciamento de banco de dados para hospedar e manter os dados, onde os usuários utilizam comandos chamados consultas para explorar os dados. Arquivos como fontes de dados podem ser arquivos de áudio, imagem e vídeo, bem como planilhas como Excel. Fontes da internet são um local comum para hospedar dados, onde bancos de dados e arquivos podem ser encontrados. Interfaces de programação de aplicativos, também conhecidas como APIs, permitem que programadores criem maneiras de compartilhar dados com usuários externos pela internet, enquanto o processo de web scraping extrai dados de uma página da web. As [lições em Trabalhando com Dados](../../../../../../../../../2-Working-With-Data) focam em como usar várias fontes de dados.

## Conclusão

Nesta lição, aprendemos:

- O que são dados
- Como os dados são descritos
- Como os dados são classificados e categorizados
- Onde os dados podem ser encontrados

## 🚀 Desafio

O Kaggle é uma excelente fonte de conjuntos de dados abertos. Use a [ferramenta de busca de conjuntos de dados](https://www.kaggle.com/datasets) para encontrar alguns conjuntos de dados interessantes e classifique de 3 a 5 conjuntos de dados com os seguintes critérios:

- Os dados são quantitativos ou qualitativos?
- Os dados são estruturados, não estruturados ou semiestruturados?

## [Quiz Pós-Aula](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/5)

## Revisão & Autoestudo

- Esta unidade do Microsoft Learn, intitulada [Classifique seus Dados](https://docs.microsoft.com/en-us/learn/modules/choose-storage-approach-in-azure/2-classify-data), tem uma explicação detalhada sobre dados estruturados, semiestruturados e não estruturados.

## Tarefa

[Classificando Conjuntos de Dados](assignment.md)

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.