<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2baeafe1db4d58ee5b8ec85db9de728a",
  "translation_date": "2025-09-05T13:19:20+00:00",
  "source_file": "4-Data-Science-Lifecycle/15-analyzing/README.md",
  "language_code": "pt"
}
-->
# O Ciclo de Vida da Ciência de Dados: Análise

|![ Sketchnote por [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/15-Analyzing.png)|
|:---:|
| Ciclo de Vida da Ciência de Dados: Análise - _Sketchnote por [@nitya](https://twitter.com/nitya)_ |

## Questionário Pré-Aula

## [Questionário Pré-Aula](https://ff-quizzes.netlify.app/en/ds/quiz/28)

A análise no ciclo de vida dos dados confirma se os dados podem responder às perguntas propostas ou resolver um problema específico. Esta etapa também pode focar em confirmar se um modelo está a abordar corretamente essas questões e problemas. Esta lição é centrada na Análise Exploratória de Dados (EDA), que consiste em técnicas para definir características e relações dentro dos dados e que podem ser usadas para preparar os dados para modelagem.

Usaremos um conjunto de dados de exemplo do [Kaggle](https://www.kaggle.com/balaka18/email-spam-classification-dataset-csv/version/1) para demonstrar como isso pode ser aplicado com Python e a biblioteca Pandas. Este conjunto de dados contém uma contagem de algumas palavras comuns encontradas em e-mails, sendo que as fontes desses e-mails são anónimas. Utilize o [notebook](../../../../4-Data-Science-Lifecycle/15-analyzing/notebook.ipynb) neste diretório para acompanhar.

## Análise Exploratória de Dados

A fase de captura do ciclo de vida é onde os dados são adquiridos, bem como os problemas e questões em questão, mas como sabemos se os dados podem ajudar a suportar o resultado final?  
Lembre-se de que um cientista de dados pode fazer as seguintes perguntas ao adquirir os dados:
-   Tenho dados suficientes para resolver este problema?
-   Os dados têm qualidade aceitável para este problema?
-   Se descobrir informações adicionais através destes dados, devemos considerar alterar ou redefinir os objetivos?

A Análise Exploratória de Dados é o processo de conhecer os dados e pode ser usada para responder a estas perguntas, bem como identificar os desafios de trabalhar com o conjunto de dados. Vamos focar em algumas das técnicas usadas para alcançar isso.

## Perfilagem de Dados, Estatísticas Descritivas e Pandas
Como avaliamos se temos dados suficientes para resolver este problema? A perfilagem de dados pode resumir e reunir algumas informações gerais sobre o nosso conjunto de dados através de técnicas de estatísticas descritivas. A perfilagem de dados ajuda-nos a entender o que está disponível para nós, e as estatísticas descritivas ajudam-nos a entender quantas coisas estão disponíveis para nós.

Em algumas das lições anteriores, utilizámos o Pandas para fornecer algumas estatísticas descritivas com a função [`describe()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html). Esta função fornece a contagem, valores máximos e mínimos, média, desvio padrão e quantis nos dados numéricos. Usar estatísticas descritivas como a função `describe()` pode ajudar a avaliar quanto temos e se precisamos de mais.

## Amostragem e Consultas
Explorar tudo num grande conjunto de dados pode ser muito demorado e é uma tarefa que geralmente é deixada para o computador. No entanto, a amostragem é uma ferramenta útil para compreender os dados e permite-nos ter uma melhor noção do que está no conjunto de dados e do que ele representa. Com uma amostra, pode-se aplicar probabilidade e estatísticas para chegar a algumas conclusões gerais sobre os dados. Embora não haja uma regra definida sobre a quantidade de dados que se deve amostrar, é importante notar que quanto mais dados se amostrar, mais precisa será a generalização que se pode fazer sobre os dados.  
O Pandas possui a função [`sample()` na sua biblioteca](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sample.html), onde se pode passar um argumento indicando quantas amostras aleatórias se deseja receber e usar.

Consultas gerais aos dados podem ajudar a responder a algumas perguntas e teorias gerais que se possa ter. Em contraste com a amostragem, as consultas permitem ter controlo e focar em partes específicas dos dados sobre as quais se tem perguntas.  
A função [`query()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html) na biblioteca Pandas permite selecionar colunas e obter respostas simples sobre os dados através das linhas recuperadas.

## Exploração com Visualizações
Não é necessário esperar até que os dados estejam completamente limpos e analisados para começar a criar visualizações. Na verdade, ter uma representação visual durante a exploração pode ajudar a identificar padrões, relações e problemas nos dados. Além disso, as visualizações fornecem um meio de comunicação com aqueles que não estão envolvidos na gestão dos dados e podem ser uma oportunidade para partilhar e esclarecer questões adicionais que não foram abordadas na fase de captura. Consulte a [secção sobre Visualizações](../../../../../../../../../3-Data-Visualization) para aprender mais sobre algumas formas populares de explorar visualmente.

## Exploração para identificar inconsistências
Todos os tópicos desta lição podem ajudar a identificar valores em falta ou inconsistentes, mas o Pandas fornece funções para verificar alguns destes. [isna() ou isnull()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.isna.html) podem verificar valores em falta. Uma parte importante da exploração desses valores nos seus dados é explorar por que razão eles acabaram dessa forma. Isso pode ajudar a decidir quais [ações tomar para resolvê-los](../../../../../../../../../2-Working-With-Data/08-data-preparation/notebook.ipynb).

## [Questionário Pós-Aula](https://ff-quizzes.netlify.app/en/ds/quiz/29)

## Tarefa

[Explorar para obter respostas](assignment.md)

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original no seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se uma tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes do uso desta tradução.