# Definição de Dados

|![ Sketchnote por [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/03-DefiningData.png)|
|:---:|
|Definição de Dados - _Sketchnote por [@nitya](https://twitter.com/nitya)_ |

Dados são fatos, informações, observações e medições usados para fazer descobertas e apoiar decisões informadas. Um ponto de dados é uma unidade única de dados dentro de um conjunto de dados, que é uma coleção de pontos de dados. Os conjuntos de dados podem existir em diferentes formatos e estruturas, geralmente baseados na sua origem, ou onde os dados foram recolhidos. Por exemplo, os ganhos mensais de uma empresa podem estar numa folha de cálculo, mas os dados da frequência cardíaca horária de um relógio inteligente podem estar em formato [JSON](https://stackoverflow.com/a/383699). É comum que os cientistas de dados trabalhem com diferentes tipos de dados dentro de um conjunto.

Esta lição foca-se em identificar e classificar os dados pelas suas características e fontes.

## [Questionário Pré-Aula](https://ff-quizzes.netlify.app/en/ds/quiz/4)
## Como os Dados são Descritos

### Dados Brutos
Dados brutos são dados que vieram da sua fonte no seu estado inicial e não foram analisados nem organizados. Para compreender o que está a acontecer com um conjunto de dados, ele precisa de ser organizado num formato compreensível para humanos e para a tecnologia usada para o analisar mais a fundo. A estrutura de um conjunto de dados descreve como está organizado e pode ser classificada em estruturada, não estruturada e semi-estruturada. Estes tipos de estrutura variam dependendo da fonte, mas enquadram-se nestas três categorias.

### Dados Quantitativos
Dados quantitativos são observações numéricas dentro de um conjunto de dados que tipicamente podem ser analisadas, medidas e usadas matematicamente. Alguns exemplos de dados quantitativos são: a população de um país, a altura de uma pessoa ou os lucros trimestrais de uma empresa. Com alguma análise adicional, dados quantitativos podem ser usados para descobrir tendências sazonais do Índice de Qualidade do Ar (AQI) ou estimar a probabilidade do trânsito nas horas de ponta num dia de trabalho típico.

### Dados Qualitativos
Dados qualitativos, também conhecidos como dados categóricos, são dados que não podem ser medidos objetivamente como observações de dados quantitativos. Normalmente são vários formatos de dados subjetivos que captam a qualidade de algo, como um produto ou processo. Por vezes, dados qualitativos são numéricos mas não usados matematicamente, como números de telefone ou carimbos temporais. Alguns exemplos de dados qualitativos são: comentários em vídeos, a marca e modelo de um carro ou a cor favorita dos seus amigos mais próximos. Dados qualitativos podem ser usados para compreender quais os produtos que os consumidores preferem ou para identificar palavras-chave populares em currículos de candidatura.

### Dados Estruturados
Dados estruturados são organizados em linhas e colunas, onde cada linha terá o mesmo conjunto de colunas. As colunas representam um valor de um tipo específico e são identificadas por um nome que descreve o que representa, enquanto as linhas contêm os valores reais. As colunas terão frequentemente um conjunto específico de regras ou restrições sobre os valores para garantir que representam adequadamente a coluna. Por exemplo, imagine uma folha de cálculo de clientes onde cada linha deve ter um número de telefone e os números de telefone nunca contêm caracteres alfabéticos. Pode haver regras aplicadas na coluna do número de telefone para garantir que nunca está vazia e contém só números.

Uma vantagem dos dados estruturados é que podem ser organizados de forma a relacionarem-se com outros dados estruturados. Contudo, como o dado é projetado para estar organizado de forma específica, alterar a sua estrutura global pode requerer muito esforço. Por exemplo, adicionar uma coluna de email à folha de clientes que não pode estar vazia significa que terá de perceber como adicionar esses valores às linhas existentes do conjunto de dados.

Exemplos de dados estruturados: folhas de cálculo, bases de dados relacionais, números de telefone, extratos bancários

### Dados Não Estruturados
Dados não estruturados tipicamente não podem ser categorizados em linhas ou colunas e não têm um formato ou conjunto de regras a seguir. Porque têm menos restrições na estrutura, é mais fácil adicionar nova informação comparado a um conjunto estruturado. Se um sensor que captura dados de pressão barométrica a cada 2 minutos recebeu uma atualização para medir e registar temperatura, não é necessário alterar os dados existentes se forem não estruturados. Contudo, isto poderá tornar a análise ou investigação desses dados mais demorada. Por exemplo, um cientista que quer encontrar a temperatura média do mês anterior a partir dos dados do sensor, mas descobre que o sensor registou um "e" em alguns registos para indicar que estava avariado em vez de um número habitual, o que significa que os dados estão incompletos.

Exemplos de dados não estruturados: ficheiros de texto, mensagens de texto, ficheiros de vídeo

### Semi-estruturados
Dados semi-estruturados têm características que os colocam como uma combinação entre dados estruturados e não estruturados. Normalmente não seguem um formato de linhas e colunas, mas são organizados de uma forma considerada estruturada e podem seguir um formato fixo ou regras. A estrutura varia consoante a fonte, desde hierarquias bem definidas a algo mais flexível que permite fácil integração de nova informação. Metadados são indicadores que ajudam a decidir como os dados estão organizados e armazenados e podem ter vários nomes, dependendo do tipo de dados. Alguns nomes comuns são etiquetas, elementos, entidades e atributos. Por exemplo, uma mensagem de email típica tem um assunto, corpo e conjunto de destinatários, podendo ser organizada por quem a enviou ou quando.

Exemplos de dados semi-estruturados: HTML, ficheiros CSV, JavaScript Object Notation (JSON)

## Fontes de Dados 

Uma fonte de dados é o local inicial onde os dados foram gerados, ou onde "residem", e varia conforme como e quando foram recolhidos. Dados gerados pelos seus utilizadores são conhecidos como dados primários enquanto dados secundários provêm de uma fonte que recolheu dados para uso geral. Por exemplo, um grupo de cientistas que colhem observações numa floresta tropical são considerados primários e se decidirem partilhá-las com outros cientistas, serão secundários para esses que as usam.

Bases de dados são uma fonte comum, dependendo de um sistema de gestão de base de dados para alojar e manter os dados, onde utilizadores usam comandos chamados queries para explorar os dados. Ficheiros como fontes podem ser áudio, imagens e vídeo, bem como folhas de cálculo como Excel. Fontes na internet são locais comuns para alojar dados, onde bases de dados e ficheiros podem ser encontrados. Interfaces de programação de aplicações, conhecidas por APIs, permitem que programadores criem formas de partilhar dados com utilizadores externos pela internet, enquanto o processo de web scraping extrai dados de páginas da web. As [lições em Trabalhar com Dados](../../../../../../../../../2-Working-With-Data) focam-se em como usar várias fontes de dados.

## Conclusão

Nesta lição aprendemos:

- O que são dados
- Como os dados são descritos
- Como os dados são classificados e categorizados
- Onde os dados podem ser encontrados

## 🚀 Desafio

Kaggle é uma excelente fonte de conjuntos de dados abertos. Use a [ferramenta de pesquisa de conjuntos de dados](https://www.kaggle.com/datasets) para encontrar conjuntos de dados interessantes e classifique 3-5 conjuntos com estes critérios:

- Os dados são quantitativos ou qualitativos?
- Os dados são estruturados, não estruturados ou semi-estruturados?

## [Questionário Pós-Aula](https://ff-quizzes.netlify.app/en/ds/quiz/5)



## Revisão & Estudo Autónomo

- Esta unidade da Microsoft Learn, intitulada [Identificar formatos de dados](https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats?pivots=text) tem uma descrição detalhada de dados estruturados, semi-estruturados e não estruturados.

## Trabalho

[Classificar Conjuntos de Dados](assignment.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->