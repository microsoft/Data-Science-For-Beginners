# Definindo Dados

|![ Sketchnote por [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/03-DefiningData.png)|
|:---:|
|Definindo Dados - _Sketchnote por [@nitya](https://twitter.com/nitya)_ |

Dados são fatos, informações, observações e medições que são usados para fazer descobertas e apoiar decisões informadas. Um ponto de dado é uma unidade única de dados dentro de um conjunto de dados, que é uma coleção de pontos de dados. Conjuntos de dados podem vir em diferentes formatos e estruturas, e geralmente vão se basear na sua fonte, ou de onde os dados vieram. Por exemplo, os ganhos mensais de uma empresa podem estar em uma planilha, mas os dados de frequência cardíaca por hora de um smartwatch podem estar em formato [JSON](https://stackoverflow.com/a/383699). É comum que cientistas de dados trabalhem com diferentes tipos de dados dentro de um conjunto de dados.

Esta lição foca em identificar e classificar dados por suas características e suas fontes.

## [Pré-quiz da aula](https://ff-quizzes.netlify.app/en/ds/quiz/4)
## Como os Dados são Descritos

### Dados Brutos
Dados brutos são dados que vieram da sua fonte em seu estado inicial e não foram analisados ou organizados. Para entender o que está acontecendo com um conjunto de dados, ele precisa ser organizado em um formato que possa ser compreendido por humanos assim como pela tecnologia que pode ser usada para analisá-lo mais a fundo. A estrutura de um conjunto de dados descreve como ele está organizado e pode ser classificada como estruturada, não estruturada e semi-estruturada. Esses tipos de estrutura variam dependendo da fonte mas, em última análise, se encaixam nessas três categorias.

### Dados Quantitativos
Dados quantitativos são observações numéricas dentro de um conjunto de dados e normalmente podem ser analisados, medidos e usados matematicamente. Alguns exemplos de dados quantitativos são: a população de um país, a altura de uma pessoa ou os ganhos trimestrais de uma empresa. Com alguma análise adicional, dados quantitativos podem ser usados para descobrir tendências sazonais do Índice de Qualidade do Ar (AQI) ou estimar a probabilidade de tráfego intenso no horário de pico de um dia típico de trabalho.

### Dados Qualitativos
Dados qualitativos, também conhecidos como dados categóricos, são dados que não podem ser medidos objetivamente como observações de dados quantitativos. Geralmente são diversos formatos de dados subjetivos que capturam a qualidade de algo, como um produto ou processo. Às vezes, dados qualitativos são numéricos e normalmente não seriam usados matematicamente, como números de telefone ou carimbos de data/hora. Alguns exemplos de dados qualitativos são: comentários em vídeos, a marca e modelo de um carro ou a cor favorita dos seus amigos mais próximos. Dados qualitativos podem ser usados para entender quais produtos os consumidores preferem ou identificar palavras-chave populares em currículos de candidatura a empregos.

### Dados Estruturados
Dados estruturados são dados organizados em linhas e colunas, onde cada linha terá o mesmo conjunto de colunas. Colunas representam um valor de um tipo particular e serão identificadas com um nome que descreve o que o valor representa, enquanto linhas contêm os valores reais. Colunas frequentemente têm um conjunto específico de regras ou restrições nos valores, para garantir que os valores representem com precisão a coluna. Por exemplo, imagine uma planilha de clientes onde cada linha deve ter um número de telefone e esses números nunca contêm caracteres alfabéticos. Podem haver regras aplicadas à coluna de número de telefone para garantir que nunca esteja vazia e contenha apenas números.

Um benefício dos dados estruturados é que eles podem ser organizados de modo a se relacionarem com outros dados estruturados. No entanto, porque os dados são projetados para serem organizados de uma forma específica, fazer alterações em sua estrutura geral pode exigir muito esforço. Por exemplo, adicionar uma coluna de e-mail à planilha de clientes que não pode ficar vazia significa que será preciso descobrir como adicionar esses valores às linhas existentes dos clientes no conjunto de dados.

Exemplos de dados estruturados: planilhas, bancos de dados relacionais, números de telefone, extratos bancários

### Dados Não Estruturados
Dados não estruturados normalmente não podem ser categorizados em linhas ou colunas e não possuem um formato ou conjunto de regras a seguir. Como dados não estruturados têm menos restrições em sua estrutura, é mais fácil adicionar novas informações em comparação com um conjunto de dados estruturado. Se um sensor que captura dados da pressão barométrica a cada 2 minutos recebeu uma atualização que agora permite medir e registrar a temperatura, não é necessário alterar os dados existentes se eles forem não estruturados. No entanto, isso pode fazer com que a análise ou investigação desse tipo de dado demore mais. Por exemplo, um cientista que deseja encontrar a temperatura média do mês anterior a partir dos dados do sensor, mas descobre que o sensor registrou um "e" em alguns dados anotando que estava quebrado em vez de um número típico, o que significa que os dados estão incompletos.

Exemplos de dados não estruturados: arquivos de texto, mensagens de texto, arquivos de vídeo

### Semi-estruturado
Dados semi-estruturados têm características que combinam dados estruturados e não estruturados. Normalmente não seguem um formato de linhas e colunas, mas são organizados de uma forma considerada estruturada e podem seguir um formato fixo ou conjunto de regras. A estrutura varia entre fontes, podendo ser uma hierarquia bem definida até algo mais flexível que permite fácil integração de novas informações. Metadados são indicadores que ajudam a decidir como os dados são organizados e armazenados e terão vários nomes, dependendo do tipo de dado. Alguns nomes comuns para metadados são tags, elementos, entidades e atributos. Por exemplo, uma mensagem típica de e-mail terá um assunto, corpo e conjunto de destinatários e pode ser organizada por quem ou quando foi enviada.

Exemplos de dados semi-estruturados: HTML, arquivos CSV, JavaScript Object Notation (JSON)

## Fontes de Dados

Uma fonte de dados é o local inicial onde os dados foram gerados, ou onde "moram", e varia com base em como e quando foram coletados. Dados gerados por seus usuários são conhecidos como dados primários enquanto dados secundários vêm de uma fonte que coletou dados para uso geral. Por exemplo, um grupo de cientistas coletando observações em uma floresta tropical seria considerado primário e se decidirem compartilhar com outros cientistas, para esses outros seria considerado secundário.

Bancos de dados são uma fonte comum e dependem de um sistema de gerenciamento de banco de dados para hospedar e manter os dados onde usuários usam comandos chamados de consultas para explorar os dados. Arquivos como fontes de dados podem ser arquivos de áudio, imagem e vídeo, assim como planilhas como Excel. Fontes da internet são um local comum para hospedar dados, onde bancos de dados e arquivos podem ser encontrados. Interfaces de programação de aplicativos, também conhecidas como APIs, permitem que programadores criem formas de compartilhar dados com usuários externos pela internet, enquanto o processo de web scraping extrai dados de páginas web. As [lições em Trabalhando com Dados](../../../../../../../../../2-Working-With-Data) focam em como usar várias fontes de dados.

## Conclusão

Nesta lição aprendemos:

- O que são dados
- Como os dados são descritos
- Como os dados são classificados e categorizados
- Onde os dados podem ser encontrados

## 🚀 Desafio

Kaggle é uma excelente fonte de conjuntos de dados abertos. Use a [ferramenta de busca de datasets](https://www.kaggle.com/datasets) para encontrar alguns conjuntos de dados interessantes e classifique de 3 a 5 datasets com esse critério:

- Os dados são quantitativos ou qualitativos?
- Os dados são estruturados, não estruturados ou semi-estruturados?

## [Quiz pós-aula](https://ff-quizzes.netlify.app/en/ds/quiz/5)



## Revisão & Estudo Autônomo

- Esta unidade do Microsoft Learn, intitulada [Identificar formatos de dados](https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats?pivots=text) tem uma análise detalhada de dados estruturados, semi-estruturados e não estruturados.

## Tarefa

[Classificando Conjuntos de Dados](assignment.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->