<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "408c55cab2880daa4e78616308bd5db7",
  "translation_date": "2025-08-24T00:28:19+00:00",
  "source_file": "5-Data-Science-In-Cloud/17-Introduction/README.md",
  "language_code": "pt"
}
-->
# Introdução à Ciência de Dados na Cloud

|![ Sketchnote por [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/17-DataScience-Cloud.png)|
|:---:|
| Ciência de Dados na Cloud: Introdução - _Sketchnote por [@nitya](https://twitter.com/nitya)_ |

Nesta lição, vais aprender os princípios fundamentais da Cloud, perceber porque pode ser interessante utilizares serviços de Cloud para executar os teus projetos de ciência de dados e analisar alguns exemplos de projetos de ciência de dados realizados na Cloud.

## [Questionário Pré-Aula](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/32)

## O que é a Cloud?

A Cloud, ou Computação na Cloud, refere-se à disponibilização de uma ampla gama de serviços de computação, pagos conforme o uso, hospedados numa infraestrutura através da internet. Estes serviços incluem soluções como armazenamento, bases de dados, redes, software, análises e serviços inteligentes.

Normalmente, distinguimos entre Cloud Pública, Privada e Híbrida da seguinte forma:

* Cloud Pública: uma cloud pública é propriedade e operada por um fornecedor de serviços de cloud de terceiros, que disponibiliza os seus recursos de computação ao público através da Internet.
* Cloud Privada: refere-se a recursos de computação na cloud utilizados exclusivamente por uma única empresa ou organização, com serviços e infraestrutura mantidos numa rede privada.
* Cloud Híbrida: a cloud híbrida é um sistema que combina clouds públicas e privadas. Os utilizadores optam por um datacenter local, permitindo que dados e aplicações sejam executados numa ou mais clouds públicas.

A maioria dos serviços de computação na cloud enquadra-se em três categorias: Infraestrutura como Serviço (IaaS), Plataforma como Serviço (PaaS) e Software como Serviço (SaaS).

* Infraestrutura como Serviço (IaaS): os utilizadores alugam uma infraestrutura de TI, como servidores e máquinas virtuais (VMs), armazenamento, redes e sistemas operativos.
* Plataforma como Serviço (PaaS): os utilizadores alugam um ambiente para desenvolver, testar, entregar e gerir aplicações de software. Não precisam de se preocupar em configurar ou gerir a infraestrutura subjacente de servidores, armazenamento, redes e bases de dados necessárias para o desenvolvimento.
* Software como Serviço (SaaS): os utilizadores têm acesso a aplicações de software através da Internet, sob demanda e, geralmente, com base numa subscrição. Não precisam de se preocupar com a hospedagem e gestão da aplicação de software, da infraestrutura subjacente ou da manutenção, como atualizações de software e correções de segurança.

Alguns dos maiores fornecedores de Cloud são Amazon Web Services, Google Cloud Platform e Microsoft Azure.

## Por que escolher a Cloud para Ciência de Dados?

Desenvolvedores e profissionais de TI escolhem trabalhar com a Cloud por várias razões, incluindo as seguintes:

* Inovação: podes potenciar as tuas aplicações integrando serviços inovadores criados pelos fornecedores de Cloud diretamente nas tuas apps.
* Flexibilidade: pagas apenas pelos serviços de que precisas e podes escolher entre uma ampla gama de serviços. Normalmente, pagas conforme o uso e adaptas os serviços às tuas necessidades em evolução.
* Orçamento: não precisas de fazer investimentos iniciais para comprar hardware e software, configurar e operar datacenters locais; pagas apenas pelo que utilizas.
* Escalabilidade: os teus recursos podem ser escalados de acordo com as necessidades do teu projeto, o que significa que as tuas apps podem usar mais ou menos poder de computação, armazenamento e largura de banda, adaptando-se a fatores externos a qualquer momento.
* Produtividade: podes focar-te no teu negócio em vez de perder tempo com tarefas que podem ser geridas por terceiros, como a gestão de datacenters.
* Confiabilidade: a Computação na Cloud oferece várias formas de fazer backups contínuos dos teus dados e podes configurar planos de recuperação de desastres para manter o teu negócio e serviços em funcionamento, mesmo em tempos de crise.
* Segurança: podes beneficiar de políticas, tecnologias e controlos que reforçam a segurança do teu projeto.

Estas são algumas das razões mais comuns pelas quais as pessoas escolhem usar serviços de Cloud. Agora que temos uma melhor compreensão do que é a Cloud e dos seus principais benefícios, vamos analisar mais especificamente o trabalho de cientistas de dados e desenvolvedores que trabalham com dados, e como a Cloud pode ajudá-los a enfrentar vários desafios:

* Armazenar grandes volumes de dados: em vez de comprar, gerir e proteger grandes servidores, podes armazenar os teus dados diretamente na cloud, com soluções como Azure Cosmos DB, Azure SQL Database e Azure Data Lake Storage.
* Realizar Integração de Dados: a integração de dados é uma parte essencial da Ciência de Dados, permitindo a transição da recolha de dados para a tomada de ações. Com serviços de integração de dados oferecidos na cloud, podes recolher, transformar e integrar dados de várias fontes num único data warehouse, com o Data Factory.
* Processar dados: processar grandes volumes de dados requer muito poder de computação, e nem todos têm acesso a máquinas suficientemente potentes para isso, razão pela qual muitas pessoas optam por aproveitar diretamente o enorme poder de computação da cloud para executar e implementar as suas soluções.
* Utilizar serviços de análise de dados: serviços de cloud como Azure Synapse Analytics, Azure Stream Analytics e Azure Databricks ajudam-te a transformar os teus dados em insights acionáveis.
* Utilizar serviços de Machine Learning e inteligência de dados: em vez de começar do zero, podes usar algoritmos de machine learning oferecidos pelo fornecedor de cloud, com serviços como AzureML. Também podes usar serviços cognitivos, como conversão de fala para texto, texto para fala, visão computacional e muito mais.

## Exemplos de Ciência de Dados na Cloud

Vamos tornar isto mais tangível analisando alguns cenários.

### Análise de sentimento em redes sociais em tempo real
Começaremos com um cenário frequentemente estudado por quem inicia em machine learning: análise de sentimento em redes sociais em tempo real.

Imagina que geres um site de notícias e queres aproveitar dados em tempo real para entender que tipo de conteúdo pode interessar aos teus leitores. Para saber mais sobre isso, podes criar um programa que realiza análise de sentimento em tempo real de dados provenientes de publicações no Twitter, sobre tópicos relevantes para os teus leitores.

Os indicadores-chave que vais analisar são o volume de tweets sobre tópicos específicos (hashtags) e o sentimento, que é determinado usando ferramentas de análise que realizam análise de sentimento em torno dos tópicos especificados.

Os passos necessários para criar este projeto são os seguintes:

* Criar um hub de eventos para entrada de streaming, que irá recolher dados do Twitter.
* Configurar e iniciar uma aplicação cliente do Twitter, que irá chamar as APIs de Streaming do Twitter.
* Criar um trabalho de Stream Analytics.
* Especificar a entrada e a consulta do trabalho.
* Criar um destino de saída e especificar a saída do trabalho.
* Iniciar o trabalho.

Para ver o processo completo, consulta a [documentação](https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?WT.mc_id=academic-77958-bethanycheum&ocid=AID30411099).

### Análise de artigos científicos
Vamos analisar outro exemplo de um projeto criado por [Dmitry Soshnikov](http://soshnikov.com), um dos autores deste currículo.

Dmitry criou uma ferramenta que analisa artigos sobre a COVID. Ao rever este projeto, vais perceber como podes criar uma ferramenta que extrai conhecimento de artigos científicos, obtém insights e ajuda investigadores a navegar por grandes coleções de artigos de forma eficiente.

Vamos ver os diferentes passos utilizados para isto:
* Extrair e pré-processar informações com [Text Analytics for Health](https://docs.microsoft.com/azure/cognitive-services/text-analytics/how-tos/text-analytics-for-health?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).
* Utilizar [Azure ML](https://azure.microsoft.com/services/machine-learning?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) para paralelizar o processamento.
* Armazenar e consultar informações com [Cosmos DB](https://azure.microsoft.com/services/cosmos-db?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).
* Criar um painel interativo para exploração e visualização de dados usando Power BI.

Para ver o processo completo, visita o [blog do Dmitry](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/).

Como podes ver, podemos aproveitar os serviços de Cloud de várias formas para realizar Ciência de Dados.

## Nota de Rodapé

Fontes:
* https://azure.microsoft.com/overview/what-is-cloud-computing?ocid=AID3041109  
* https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?ocid=AID3041109  
* https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/  

## Questionário Pós-Aula

[Questionário pós-aula](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/33)

## Tarefa

[Pesquisa de Mercado](assignment.md)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original no seu idioma nativo deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se uma tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes do uso desta tradução.