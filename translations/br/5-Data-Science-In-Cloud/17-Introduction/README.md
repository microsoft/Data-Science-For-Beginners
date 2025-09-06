<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f8e7cdefa096664ae86f795be571580",
  "translation_date": "2025-09-06T08:26:40+00:00",
  "source_file": "5-Data-Science-In-Cloud/17-Introduction/README.md",
  "language_code": "br"
}
-->
# Introdução à Ciência de Dados na Nuvem

|![ Sketchnote por [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/17-DataScience-Cloud.png)|
|:---:|
| Ciência de Dados na Nuvem: Introdução - _Sketchnote por [@nitya](https://twitter.com/nitya)_ |

Nesta lição, você aprenderá os princípios fundamentais da Nuvem, verá por que pode ser interessante usar serviços de Nuvem para executar seus projetos de ciência de dados e analisará alguns exemplos de projetos de ciência de dados realizados na Nuvem.

## [Quiz Pré-Aula](https://ff-quizzes.netlify.app/en/ds/quiz/32)

## O que é a Nuvem?

A Nuvem, ou Computação em Nuvem, é a entrega de uma ampla gama de serviços de computação sob demanda, hospedados em uma infraestrutura pela internet. Esses serviços incluem soluções como armazenamento, bancos de dados, redes, software, análises e serviços inteligentes.

Normalmente, diferenciamos as Nuvens Pública, Privada e Híbrida da seguinte forma:

* Nuvem pública: uma nuvem pública é propriedade e operada por um provedor de serviços de nuvem terceirizado que entrega seus recursos de computação pela Internet ao público.
* Nuvem privada: refere-se aos recursos de computação em nuvem usados exclusivamente por uma única empresa ou organização, com serviços e infraestrutura mantidos em uma rede privada.
* Nuvem híbrida: a nuvem híbrida é um sistema que combina nuvens públicas e privadas. Os usuários optam por um datacenter local, enquanto permitem que dados e aplicativos sejam executados em uma ou mais nuvens públicas.

A maioria dos serviços de computação em nuvem se enquadra em três categorias: Infraestrutura como Serviço (IaaS), Plataforma como Serviço (PaaS) e Software como Serviço (SaaS).

* Infraestrutura como Serviço (IaaS): os usuários alugam uma infraestrutura de TI, como servidores e máquinas virtuais (VMs), armazenamento, redes e sistemas operacionais.
* Plataforma como Serviço (PaaS): os usuários alugam um ambiente para desenvolver, testar, entregar e gerenciar aplicativos de software. Os usuários não precisam se preocupar em configurar ou gerenciar a infraestrutura subjacente de servidores, armazenamento, rede e bancos de dados necessários para o desenvolvimento.
* Software como Serviço (SaaS): os usuários têm acesso a aplicativos de software pela Internet, sob demanda e, geralmente, com base em assinatura. Os usuários não precisam se preocupar em hospedar e gerenciar o aplicativo de software, a infraestrutura subjacente ou a manutenção, como atualizações de software e correções de segurança.

Alguns dos maiores provedores de Nuvem são Amazon Web Services, Google Cloud Platform e Microsoft Azure.

## Por que escolher a Nuvem para Ciência de Dados?

Desenvolvedores e profissionais de TI escolhem trabalhar com a Nuvem por vários motivos, incluindo os seguintes:

* Inovação: você pode potencializar seus aplicativos integrando serviços inovadores criados por provedores de Nuvem diretamente em seus aplicativos.
* Flexibilidade: você paga apenas pelos serviços que precisa e pode escolher entre uma ampla gama de serviços. Normalmente, você paga conforme usa e adapta seus serviços de acordo com suas necessidades em evolução.
* Orçamento: você não precisa fazer investimentos iniciais para comprar hardware e software, configurar e operar datacenters locais, e pode simplesmente pagar pelo que usar.
* Escalabilidade: seus recursos podem ser escalados de acordo com as necessidades do seu projeto, o que significa que seus aplicativos podem usar mais ou menos poder de computação, armazenamento e largura de banda, adaptando-se a fatores externos a qualquer momento.
* Produtividade: você pode se concentrar no seu negócio em vez de gastar tempo em tarefas que podem ser gerenciadas por outra pessoa, como administrar datacenters.
* Confiabilidade: a Computação em Nuvem oferece várias maneiras de fazer backup contínuo de seus dados e permite configurar planos de recuperação de desastres para manter seu negócio e serviços funcionando, mesmo em tempos de crise.
* Segurança: você pode se beneficiar de políticas, tecnologias e controles que fortalecem a segurança do seu projeto.

Esses são alguns dos motivos mais comuns pelos quais as pessoas escolhem usar serviços de Nuvem. Agora que temos uma melhor compreensão do que é a Nuvem e quais são seus principais benefícios, vamos olhar mais especificamente para o trabalho de cientistas de dados e desenvolvedores que trabalham com dados, e como a Nuvem pode ajudá-los com vários desafios que podem enfrentar:

* Armazenar grandes volumes de dados: em vez de comprar, gerenciar e proteger grandes servidores, você pode armazenar seus dados diretamente na nuvem, com soluções como Azure Cosmos DB, Azure SQL Database e Azure Data Lake Storage.
* Realizar integração de dados: a integração de dados é uma parte essencial da Ciência de Dados, que permite fazer a transição da coleta de dados para a tomada de ações. Com serviços de integração de dados oferecidos na nuvem, você pode coletar, transformar e integrar dados de várias fontes em um único data warehouse, com o Data Factory.
* Processar dados: processar grandes volumes de dados requer muito poder de computação, e nem todos têm acesso a máquinas poderosas o suficiente para isso, razão pela qual muitas pessoas escolhem aproveitar diretamente o enorme poder de computação da nuvem para executar e implantar suas soluções.
* Usar serviços de análise de dados: serviços de nuvem como Azure Synapse Analytics, Azure Stream Analytics e Azure Databricks ajudam você a transformar seus dados em insights acionáveis.
* Usar serviços de aprendizado de máquina e inteligência de dados: em vez de começar do zero, você pode usar algoritmos de aprendizado de máquina oferecidos pelo provedor de nuvem, com serviços como AzureML. Você também pode usar serviços cognitivos, como conversão de fala para texto, texto para fala, visão computacional e mais.

## Exemplos de Ciência de Dados na Nuvem

Vamos tornar isso mais tangível analisando alguns cenários.

### Análise de sentimento em redes sociais em tempo real

Começaremos com um cenário comumente estudado por pessoas que iniciam no aprendizado de máquina: análise de sentimento em redes sociais em tempo real.

Imagine que você administra um site de notícias e deseja aproveitar dados ao vivo para entender quais conteúdos podem interessar aos seus leitores. Para saber mais sobre isso, você pode criar um programa que realiza análise de sentimento em tempo real de dados de publicações no Twitter, sobre tópicos relevantes para seus leitores.

Os indicadores-chave que você analisará são o volume de tweets sobre tópicos específicos (hashtags) e o sentimento, que é estabelecido usando ferramentas de análise que realizam análise de sentimento em torno dos tópicos especificados.

Os passos necessários para criar este projeto são os seguintes:

* Criar um hub de eventos para entrada de streaming, que coletará dados do Twitter.
* Configurar e iniciar um aplicativo cliente do Twitter, que chamará as APIs de Streaming do Twitter.
* Criar um trabalho de Stream Analytics.
* Especificar a entrada e a consulta do trabalho.
* Criar um destino de saída e especificar a saída do trabalho.
* Iniciar o trabalho.

Para ver o processo completo, confira a [documentação](https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?WT.mc_id=academic-77958-bethanycheum&ocid=AID30411099).

### Análise de artigos científicos

Vamos analisar outro exemplo de um projeto criado por [Dmitry Soshnikov](http://soshnikov.com), um dos autores deste currículo.

Dmitry criou uma ferramenta que analisa artigos sobre COVID. Ao revisar este projeto, você verá como criar uma ferramenta que extrai conhecimento de artigos científicos, obtém insights e ajuda pesquisadores a navegar por grandes coleções de artigos de forma eficiente.

Vamos ver os diferentes passos usados para isso:

* Extrair e pré-processar informações com [Text Analytics for Health](https://docs.microsoft.com/azure/cognitive-services/text-analytics/how-tos/text-analytics-for-health?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).
* Usar [Azure ML](https://azure.microsoft.com/services/machine-learning?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) para paralelizar o processamento.
* Armazenar e consultar informações com [Cosmos DB](https://azure.microsoft.com/services/cosmos-db?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).
* Criar um painel interativo para exploração e visualização de dados usando Power BI.

Para ver o processo completo, visite o [blog de Dmitry](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/).

Como você pode ver, podemos aproveitar os serviços de Nuvem de várias maneiras para realizar Ciência de Dados.

## Nota de Rodapé

Fontes:
* https://azure.microsoft.com/overview/what-is-cloud-computing?ocid=AID3041109  
* https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?ocid=AID3041109  
* https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/  

## Quiz Pós-Aula

## [Quiz Pós-Aula](https://ff-quizzes.netlify.app/en/ds/quiz/33)

## Tarefa

[Pesquisa de Mercado](assignment.md)

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.