<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a167aa0bfb1c46ece1b3d21ae939cc0d",
  "translation_date": "2025-09-04T17:45:10+00:00",
  "source_file": "4-Data-Science-Lifecycle/15-analyzing/README.md",
  "language_code": "br"
}
-->
# O Ciclo de Vida da Ciência de Dados: Análise

|![ Sketchnote por [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/15-Analyzing.png)|
|:---:|
| Ciclo de Vida da Ciência de Dados: Análise - _Sketchnote por [@nitya](https://twitter.com/nitya)_ |

## Quiz Pré-Aula

## [Quiz Pré-Aula](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/28)

A análise no ciclo de vida dos dados confirma que os dados podem responder às perguntas propostas ou resolver um problema específico. Esta etapa também pode se concentrar em confirmar se um modelo está abordando corretamente essas questões e problemas. Esta lição é focada na Análise Exploratória de Dados (EDA), que são técnicas para definir características e relações dentro dos dados e podem ser usadas para preparar os dados para modelagem.

Usaremos um conjunto de dados de exemplo do [Kaggle](https://www.kaggle.com/balaka18/email-spam-classification-dataset-csv/version/1) para mostrar como isso pode ser aplicado com Python e a biblioteca Pandas. Este conjunto de dados contém uma contagem de algumas palavras comuns encontradas em e-mails, sendo que as fontes desses e-mails são anônimas. Use o [notebook](notebook.ipynb) neste diretório para acompanhar.

## Análise Exploratória de Dados

A fase de captura do ciclo de vida é onde os dados são adquiridos, bem como os problemas e perguntas em questão, mas como sabemos se os dados podem ajudar a apoiar o resultado final?  
Lembre-se de que um cientista de dados pode fazer as seguintes perguntas ao adquirir os dados:  
- Eu tenho dados suficientes para resolver este problema?  
- Os dados têm qualidade aceitável para este problema?  
- Se eu descobrir informações adicionais por meio desses dados, devemos considerar mudar ou redefinir os objetivos?  

A Análise Exploratória de Dados é o processo de conhecer os dados e pode ser usada para responder a essas perguntas, além de identificar os desafios de trabalhar com o conjunto de dados. Vamos nos concentrar em algumas das técnicas usadas para alcançar isso.

## Perfilamento de Dados, Estatísticas Descritivas e Pandas

Como avaliamos se temos dados suficientes para resolver este problema? O perfilamento de dados pode resumir e reunir algumas informações gerais sobre nosso conjunto de dados por meio de técnicas de estatísticas descritivas. O perfilamento de dados nos ajuda a entender o que está disponível para nós, e as estatísticas descritivas nos ajudam a entender quantas coisas estão disponíveis para nós.

Em algumas das lições anteriores, usamos o Pandas para fornecer algumas estatísticas descritivas com a função [`describe()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html). Ela fornece a contagem, valores máximos e mínimos, média, desvio padrão e quantis nos dados numéricos. Usar estatísticas descritivas como a função `describe()` pode ajudar você a avaliar quanto você tem e se precisa de mais.

## Amostragem e Consultas

Explorar tudo em um grande conjunto de dados pode ser muito demorado e geralmente é uma tarefa deixada para o computador. No entanto, a amostragem é uma ferramenta útil para entender os dados e permite que tenhamos uma melhor compreensão do que está no conjunto de dados e o que ele representa. Com uma amostra, você pode aplicar probabilidade e estatísticas para chegar a algumas conclusões gerais sobre seus dados. Embora não haja uma regra definida sobre quanto dos dados você deve amostrar, é importante observar que quanto mais dados você amostrar, mais precisa será a generalização que você pode fazer sobre os dados.  
O Pandas possui a função [`sample()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sample.html) em sua biblioteca, onde você pode passar um argumento de quantas amostras aleatórias deseja receber e usar.

Consultas gerais aos dados podem ajudar você a responder algumas perguntas e teorias gerais que possa ter. Em contraste com a amostragem, as consultas permitem que você tenha controle e se concentre em partes específicas dos dados sobre as quais tem perguntas.  
A função [`query()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html) na biblioteca Pandas permite selecionar colunas e receber respostas simples sobre os dados por meio das linhas recuperadas.

## Explorando com Visualizações

Você não precisa esperar até que os dados estejam completamente limpos e analisados para começar a criar visualizações. Na verdade, ter uma representação visual enquanto explora pode ajudar a identificar padrões, relações e problemas nos dados. Além disso, as visualizações fornecem um meio de comunicação com aqueles que não estão envolvidos na gestão dos dados e podem ser uma oportunidade para compartilhar e esclarecer questões adicionais que não foram abordadas na etapa de captura. Consulte a [seção sobre Visualizações](../../../../../../../../../3-Data-Visualization) para aprender mais sobre algumas formas populares de explorar visualmente.

## Explorando para Identificar Inconsistências

Todos os tópicos desta lição podem ajudar a identificar valores ausentes ou inconsistentes, mas o Pandas fornece funções para verificar alguns deles. [isna() ou isnull()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.isna.html) podem verificar valores ausentes. Uma parte importante de explorar esses valores dentro de seus dados é investigar por que eles acabaram dessa forma. Isso pode ajudar você a decidir quais [ações tomar para resolvê-los](/2-Working-With-Data/08-data-preparation/notebook.ipynb).

## [Quiz Pós-Aula](https://ff-quizzes.netlify.app/en/ds/)

## Tarefa

[Explorando para respostas](assignment.md)

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.