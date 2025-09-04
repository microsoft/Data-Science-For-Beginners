<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6a0556b17de4c8d1a9470b02247b01d4",
  "translation_date": "2025-09-04T13:38:11+00:00",
  "source_file": "5-Data-Science-In-Cloud/17-Introduction/README.md",
  "language_code": "pt"
}
-->
# Introdução à Ciência de Dados na Nuvem

|![ Sketchnote por [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/17-DataScience-Cloud.png)|
|:---:|
| Ciência de Dados na Nuvem: Introdução - _Sketchnote por [@nitya](https://twitter.com/nitya)_ |

Nesta lição, irá aprender os princípios fundamentais da Nuvem, verá porque pode ser interessante utilizar serviços na Nuvem para executar os seus projetos de ciência de dados e analisaremos alguns exemplos de projetos de ciência de dados realizados na Nuvem.

## [Questionário Pré-Aula](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/32)

## O que é a Nuvem?

A Nuvem, ou Computação na Nuvem, é a entrega de uma ampla gama de serviços de computação sob demanda, hospedados numa infraestrutura através da internet. Os serviços incluem soluções como armazenamento, bases de dados, redes, software, análises e serviços inteligentes.

Normalmente, distinguimos as Nuvens Públicas, Privadas e Híbridas da seguinte forma:

* Nuvem pública: uma nuvem pública é propriedade e operada por um fornecedor de serviços de nuvem de terceiros que disponibiliza os seus recursos de computação através da Internet ao público.
* Nuvem privada: refere-se a recursos de computação na nuvem utilizados exclusivamente por uma única empresa ou organização, com serviços e infraestrutura mantidos numa rede privada.
* Nuvem híbrida: a nuvem híbrida é um sistema que combina nuvens públicas e privadas. Os utilizadores optam por um centro de dados local, enquanto permitem que dados e aplicações sejam executados numa ou mais nuvens públicas.

A maioria dos serviços de computação na nuvem enquadra-se em três categorias: Infraestrutura como Serviço (IaaS), Plataforma como Serviço (PaaS) e Software como Serviço (SaaS).

* Infraestrutura como Serviço (IaaS): os utilizadores alugam uma infraestrutura de TI, como servidores e máquinas virtuais (VMs), armazenamento, redes, sistemas operativos.
* Plataforma como Serviço (PaaS): os utilizadores alugam um ambiente para desenvolver, testar, entregar e gerir aplicações de software. Os utilizadores não precisam preocupar-se em configurar ou gerir a infraestrutura subjacente de servidores, armazenamento, rede e bases de dados necessárias para o desenvolvimento.
* Software como Serviço (SaaS): os utilizadores têm acesso a aplicações de software através da Internet, sob demanda e, geralmente, com base numa subscrição. Os utilizadores não precisam preocupar-se em hospedar e gerir a aplicação de software, a infraestrutura subjacente ou a manutenção, como atualizações de software e correções de segurança.

Alguns dos maiores fornecedores de Nuvem são Amazon Web Services, Google Cloud Platform e Microsoft Azure.

## Por que escolher a Nuvem para Ciência de Dados?

Desenvolvedores e profissionais de TI escolhem trabalhar com a Nuvem por várias razões, incluindo as seguintes:

* Inovação: pode potenciar as suas aplicações ao integrar serviços inovadores criados pelos fornecedores de Nuvem diretamente nas suas aplicações.
* Flexibilidade: paga apenas pelos serviços que necessita e pode escolher entre uma ampla gama de serviços. Normalmente, paga conforme utiliza e adapta os serviços às suas necessidades em evolução.
* Orçamento: não precisa fazer investimentos iniciais para adquirir hardware e software, configurar e operar centros de dados locais, podendo simplesmente pagar pelo que utiliza.
* Escalabilidade: os seus recursos podem ser ajustados conforme as necessidades do seu projeto, o que significa que as suas aplicações podem utilizar mais ou menos poder de computação, armazenamento e largura de banda, adaptando-se a fatores externos a qualquer momento.
* Produtividade: pode concentrar-se no seu negócio em vez de gastar tempo em tarefas que podem ser geridas por outra pessoa, como gerir centros de dados.
* Fiabilidade: a Computação na Nuvem oferece várias formas de fazer backups contínuos dos seus dados e pode configurar planos de recuperação de desastres para manter o seu negócio e serviços em funcionamento, mesmo em tempos de crise.
* Segurança: pode beneficiar de políticas, tecnologias e controlos que reforçam a segurança do seu projeto.

Estas são algumas das razões mais comuns pelas quais as pessoas escolhem utilizar serviços na Nuvem. Agora que temos uma melhor compreensão do que é a Nuvem e quais são os seus principais benefícios, vamos analisar mais especificamente o trabalho de cientistas de dados e desenvolvedores que trabalham com dados, e como a Nuvem pode ajudá-los com vários desafios que podem enfrentar:

* Armazenar grandes volumes de dados: em vez de comprar, gerir e proteger grandes servidores, pode armazenar os seus dados diretamente na nuvem, com soluções como Azure Cosmos DB, Azure SQL Database e Azure Data Lake Storage.
* Realizar integração de dados: a integração de dados é uma parte essencial da Ciência de Dados, que permite fazer a transição da coleta de dados para a tomada de ações. Com serviços de integração de dados oferecidos na nuvem, pode coletar, transformar e integrar dados de várias fontes num único armazém de dados, com o Data Factory.
* Processar dados: processar grandes volumes de dados requer muito poder de computação, e nem todos têm acesso a máquinas suficientemente poderosas para isso, razão pela qual muitas pessoas optam por utilizar diretamente o enorme poder de computação da nuvem para executar e implementar as suas soluções.
* Utilizar serviços de análise de dados: serviços na nuvem como Azure Synapse Analytics, Azure Stream Analytics e Azure Databricks ajudam a transformar os seus dados em insights acionáveis.
* Utilizar serviços de Machine Learning e inteligência de dados: em vez de começar do zero, pode utilizar algoritmos de machine learning oferecidos pelo fornecedor de nuvem, com serviços como AzureML. Também pode utilizar serviços cognitivos como conversão de fala para texto, texto para fala, visão computacional e mais.

## Exemplos de Ciência de Dados na Nuvem

Vamos tornar isto mais tangível analisando alguns cenários.

### Análise de sentimento em redes sociais em tempo real

Começaremos com um cenário comumente estudado por pessoas que iniciam com machine learning: análise de sentimento em redes sociais em tempo real.

Imagine que gere um site de notícias e quer aproveitar dados em tempo real para entender que tipo de conteúdo pode interessar aos seus leitores. Para saber mais sobre isso, pode criar um programa que realiza análise de sentimento em tempo real de dados de publicações no Twitter, sobre tópicos relevantes para os seus leitores.

Os indicadores-chave que irá analisar são o volume de tweets sobre tópicos específicos (hashtags) e o sentimento, que é estabelecido utilizando ferramentas de análise que realizam análise de sentimento em torno dos tópicos especificados.

Os passos necessários para criar este projeto são os seguintes:

* Criar um hub de eventos para entrada de streaming, que irá coletar dados do Twitter.
* Configurar e iniciar uma aplicação cliente do Twitter, que irá chamar as APIs de Streaming do Twitter.
* Criar um trabalho de Stream Analytics.
* Especificar a entrada e a consulta do trabalho.
* Criar um destino de saída e especificar a saída do trabalho.
* Iniciar o trabalho.

Para ver o processo completo, consulte a [documentação](https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?WT.mc_id=academic-77958-bethanycheum&ocid=AID30411099).

### Análise de artigos científicos

Vamos analisar outro exemplo de um projeto criado por [Dmitry Soshnikov](http://soshnikov.com), um dos autores deste currículo.

Dmitry criou uma ferramenta que analisa artigos sobre COVID. Ao revisar este projeto, verá como pode criar uma ferramenta que extrai conhecimento de artigos científicos, obtém insights e ajuda os pesquisadores a navegar por grandes coleções de artigos de forma eficiente.

Vamos ver os diferentes passos utilizados para isso:

* Extrair e pré-processar informações com [Text Analytics for Health](https://docs.microsoft.com/azure/cognitive-services/text-analytics/how-tos/text-analytics-for-health?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).
* Utilizar [Azure ML](https://azure.microsoft.com/services/machine-learning?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) para paralelizar o processamento.
* Armazenar e consultar informações com [Cosmos DB](https://azure.microsoft.com/services/cosmos-db?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).
* Criar um painel interativo para exploração e visualização de dados utilizando Power BI.

Para ver o processo completo, visite o [blog de Dmitry](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/).

Como pode ver, podemos aproveitar os serviços na Nuvem de várias formas para realizar Ciência de Dados.

## Nota de Rodapé

Fontes:
* https://azure.microsoft.com/overview/what-is-cloud-computing?ocid=AID3041109  
* https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?ocid=AID3041109  
* https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/  

## Questionário Pós-Aula

## [Questionário Pós-Aula](https://ff-quizzes.netlify.app/en/ds/)

## Tarefa

[Pesquisa de Mercado](assignment.md)

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, é importante ter em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se uma tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.