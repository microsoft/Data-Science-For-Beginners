<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f95679140c7cb39c30ccba535cd8f03f",
  "translation_date": "2025-09-04T17:50:50+00:00",
  "source_file": "6-Data-Science-In-Wild/20-Real-World-Examples/README.md",
  "language_code": "br"
}
-->
# Ciência de Dados no Mundo Real

| ![ Sketchnote por [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-RealWorld.png) |
| :--------------------------------------------------------------------------------------------------------------: |
|               Ciência de Dados no Mundo Real - _Sketchnote por [@nitya](https://twitter.com/nitya)_               |

Estamos quase no fim desta jornada de aprendizado!

Começamos com definições de ciência de dados e ética, exploramos várias ferramentas e técnicas para análise e visualização de dados, revisamos o ciclo de vida da ciência de dados e analisamos como escalar e automatizar fluxos de trabalho de ciência de dados com serviços de computação em nuvem. Então, você provavelmente está se perguntando: _"Como exatamente posso aplicar tudo isso em contextos do mundo real?"_

Nesta lição, vamos explorar aplicações reais da ciência de dados em diferentes indústrias e mergulhar em exemplos específicos nos contextos de pesquisa, humanidades digitais e sustentabilidade. Também veremos oportunidades de projetos para estudantes e concluiremos com recursos úteis para ajudar você a continuar sua jornada de aprendizado!

## Quiz Pré-Aula

[Quiz pré-aula](https://ff-quizzes.netlify.app/en/ds/)

## Ciência de Dados + Indústria

Graças à democratização da IA, os desenvolvedores estão encontrando mais facilidade para projetar e integrar tomadas de decisão baseadas em IA e insights orientados por dados em experiências de usuário e fluxos de trabalho de desenvolvimento. Aqui estão alguns exemplos de como a ciência de dados é "aplicada" em contextos reais na indústria:

 * [Google Flu Trends](https://www.wired.com/2015/10/can-learn-epic-failure-google-flu-trends/) utilizou ciência de dados para correlacionar termos de busca com tendências de gripe. Embora a abordagem tenha apresentado falhas, ela trouxe à tona as possibilidades (e desafios) de previsões de saúde baseadas em dados.

 * [Previsões de Rotas da UPS](https://www.technologyreview.com/2018/11/21/139000/how-ups-uses-ai-to-outsmart-bad-weather/) - explica como a UPS usa ciência de dados e aprendizado de máquina para prever rotas ideais de entrega, considerando condições climáticas, padrões de tráfego, prazos de entrega e mais.

 * [Visualização de Rotas de Táxi em NYC](http://chriswhong.github.io/nyctaxi/) - dados obtidos por meio das [Leis de Liberdade de Informação](https://chriswhong.com/open-data/foil_nyc_taxi/) ajudaram a visualizar um dia na vida dos táxis de NYC, permitindo entender como eles navegam pela cidade movimentada, o dinheiro que ganham e a duração das viagens ao longo de um período de 24 horas.

 * [Uber Data Science Workbench](https://eng.uber.com/dsw/) - utiliza dados (sobre locais de embarque e desembarque, duração das viagens, rotas preferidas etc.) coletados de milhões de viagens diárias para construir uma ferramenta de análise de dados que ajuda em decisões de preços, segurança, detecção de fraudes e navegação.

 * [Análise Esportiva](https://towardsdatascience.com/scope-of-analytics-in-sports-world-37ed09c39860) - foca em _análise preditiva_ (análise de equipes e jogadores - pense em [Moneyball](https://datasciencedegree.wisconsin.edu/blog/moneyball-proves-importance-big-data-big-ideas/) - e gestão de fãs) e _visualização de dados_ (painéis de equipes e fãs, jogos etc.) com aplicações como recrutamento de talentos, apostas esportivas e gestão de inventário/locais.

 * [Ciência de Dados no Setor Bancário](https://data-flair.training/blogs/data-science-in-banking/) - destaca o valor da ciência de dados na indústria financeira com aplicações que vão desde modelagem de risco e detecção de fraudes até segmentação de clientes, previsão em tempo real e sistemas de recomendação. A análise preditiva também impulsiona medidas críticas como [pontuação de crédito](https://dzone.com/articles/using-big-data-and-predictive-analytics-for-credit).

 * [Ciência de Dados na Saúde](https://data-flair.training/blogs/data-science-in-healthcare/) - destaca aplicações como imagem médica (por exemplo, ressonância magnética, raio-X, tomografia), genômica (sequenciamento de DNA), desenvolvimento de medicamentos (avaliação de risco, previsão de sucesso), análise preditiva (cuidados com pacientes e logística de suprimentos), rastreamento e prevenção de doenças etc.

![Aplicações de Ciência de Dados no Mundo Real](../../../../translated_images/data-science-applications.4e5019cd8790ebac2277ff5f08af386f8727cac5d30f77727c7090677e6adb9c.br.png) Crédito da Imagem: [Data Flair: 6 Amazing Data Science Applications ](https://data-flair.training/blogs/data-science-applications/)

A figura mostra outros domínios e exemplos de aplicação de técnicas de ciência de dados. Quer explorar outras aplicações? Confira a seção [Revisão e Autoestudo](../../../../6-Data-Science-In-Wild/20-Real-World-Examples) abaixo.

## Ciência de Dados + Pesquisa

| ![ Sketchnote por [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-Research.png) |
| :---------------------------------------------------------------------------------------------------------------: |
|              Ciência de Dados & Pesquisa - _Sketchnote por [@nitya](https://twitter.com/nitya)_              |

Embora as aplicações do mundo real frequentemente se concentrem em casos de uso na indústria em larga escala, as aplicações e projetos de _pesquisa_ podem ser úteis sob duas perspectivas:

* _oportunidades de inovação_ - explorar protótipos rápidos de conceitos avançados e testar experiências de usuário para aplicações de próxima geração.
* _desafios de implementação_ - investigar possíveis danos ou consequências não intencionais das tecnologias de ciência de dados em contextos reais.

Para estudantes, esses projetos de pesquisa podem oferecer oportunidades de aprendizado e colaboração que melhoram sua compreensão do tema e ampliam sua conscientização e engajamento com pessoas ou equipes relevantes que trabalham em áreas de interesse. Então, como são os projetos de pesquisa e como eles podem causar impacto?

Vamos analisar um exemplo - o [MIT Gender Shades Study](http://gendershades.org/overview.html) de Joy Buolamwini (MIT Media Labs) com um [artigo de pesquisa de destaque](http://proceedings.mlr.press/v81/buolamwini18a/buolamwini18a.pdf) coautorado com Timnit Gebru (então na Microsoft Research) que focou em:

 * **O quê:** O objetivo do projeto de pesquisa era _avaliar o viés presente em algoritmos e conjuntos de dados de análise facial automatizada_ com base em gênero e tipo de pele. 
 * **Por quê:** A análise facial é usada em áreas como aplicação da lei, segurança em aeroportos, sistemas de contratação e mais - contextos onde classificações imprecisas (por exemplo, devido a viés) podem causar danos econômicos e sociais potenciais a indivíduos ou grupos afetados. Entender (e eliminar ou mitigar) esses vieses é essencial para garantir justiça no uso.
 * **Como:** Os pesquisadores perceberam que os benchmarks existentes usavam predominantemente sujeitos de pele mais clara e criaram um novo conjunto de dados (mais de 1000 imagens) que era _mais equilibrado_ em termos de gênero e tipo de pele. O conjunto de dados foi usado para avaliar a precisão de três produtos de classificação de gênero (da Microsoft, IBM e Face++). 

Os resultados mostraram que, embora a precisão geral da classificação fosse boa, havia uma diferença perceptível nas taxas de erro entre vários subgrupos - com **erros de classificação de gênero** sendo mais altos para mulheres ou pessoas com pele mais escura, indicando viés.

**Principais Resultados:** Aumentou a conscientização de que a ciência de dados precisa de mais _conjuntos de dados representativos_ (subgrupos equilibrados) e mais _equipes inclusivas_ (diversidade de origens) para reconhecer e eliminar ou mitigar esses vieses mais cedo em soluções de IA. Esforços de pesquisa como este também são fundamentais para muitas organizações definirem princípios e práticas para _IA responsável_ visando melhorar a justiça em seus produtos e processos de IA.

**Quer saber mais sobre esforços de pesquisa relevantes na Microsoft?** 

* Confira [Projetos de Pesquisa da Microsoft](https://www.microsoft.com/research/research-area/artificial-intelligence/?facet%5Btax%5D%5Bmsr-research-area%5D%5B%5D=13556&facet%5Btax%5D%5Bmsr-content-type%5D%5B%5D=msr-project) em Inteligência Artificial.
* Explore projetos de estudantes da [Microsoft Research Data Science Summer School](https://www.microsoft.com/en-us/research/academic-program/data-science-summer-school/).
* Confira o projeto [Fairlearn](https://fairlearn.org/) e as iniciativas de [IA Responsável](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1%3aprimaryr6).

## Ciência de Dados + Humanidades

| ![ Sketchnote por [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-Humanities.png) |
| :---------------------------------------------------------------------------------------------------------------: |
|              Ciência de Dados & Humanidades Digitais - _Sketchnote por [@nitya](https://twitter.com/nitya)_              |

Humanidades Digitais [são definidas](https://digitalhumanities.stanford.edu/about-dh-stanford) como "uma coleção de práticas e abordagens que combinam métodos computacionais com investigação humanística". Projetos da [Stanford](https://digitalhumanities.stanford.edu/projects) como _"rebooting history"_ e _"poetic thinking"_ ilustram a ligação entre [Humanidades Digitais e Ciência de Dados](https://digitalhumanities.stanford.edu/digital-humanities-and-data-science) - enfatizando técnicas como análise de redes, visualização de informações, análise espacial e textual que podem nos ajudar a revisitar conjuntos de dados históricos e literários para obter novos insights e perspectivas.

*Quer explorar e expandir um projeto neste espaço?*

Confira ["Emily Dickinson and the Meter of Mood"](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671) - um ótimo exemplo de [Jen Looper](https://twitter.com/jenlooper) que pergunta como podemos usar ciência de dados para revisitar poesias familiares e reavaliar seu significado e as contribuições de seu autor em novos contextos. Por exemplo, _podemos prever a estação do ano em que um poema foi escrito analisando seu tom ou sentimento_ - e o que isso nos diz sobre o estado de espírito do autor durante o período relevante?

Para responder a essa pergunta, seguimos os passos do ciclo de vida da ciência de dados:
 * [`Aquisição de Dados`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#acquiring-the-dataset) - para coletar um conjunto de dados relevante para análise. As opções incluem usar uma API (por exemplo, [Poetry DB API](https://poetrydb.org/index.html)) ou fazer scraping de páginas da web (por exemplo, [Project Gutenberg](https://www.gutenberg.org/files/12242/12242-h/12242-h.htm)) usando ferramentas como [Scrapy](https://scrapy.org/).
 * [`Limpeza de Dados`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#clean-the-data) - explica como o texto pode ser formatado, sanitizado e simplificado usando ferramentas básicas como Visual Studio Code e Microsoft Excel.
 * [`Análise de Dados`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#working-with-the-data-in-a-notebook) - explica como podemos importar o conjunto de dados para "Notebooks" para análise usando pacotes Python (como pandas, numpy e matplotlib) para organizar e visualizar os dados.
 * [`Análise de Sentimento`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#sentiment-analysis-using-cognitive-services) - explica como podemos integrar serviços em nuvem como Text Analytics, usando ferramentas de baixo código como [Power Automate](https://flow.microsoft.com/en-us/) para fluxos de trabalho automatizados de processamento de dados.

Usando esse fluxo de trabalho, podemos explorar os impactos sazonais no sentimento dos poemas e nos ajudar a formar nossas próprias perspectivas sobre o autor. Experimente você mesmo - depois expanda o notebook para fazer outras perguntas ou visualizar os dados de novas maneiras!

> Você pode usar algumas das ferramentas no [Digital Humanities toolkit](https://github.com/Digital-Humanities-Toolkit) para seguir essas linhas de investigação.

## Ciência de Dados + Sustentabilidade

| ![ Sketchnote por [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-Sustainability.png) |
| :---------------------------------------------------------------------------------------------------------------: |
|              Ciência de Dados & Sustentabilidade - _Sketchnote por [@nitya](https://twitter.com/nitya)_              |

A [Agenda 2030 para o Desenvolvimento Sustentável](https://sdgs.un.org/2030agenda) - adotada por todos os membros das Nações Unidas em 2015 - identifica 17 objetivos, incluindo aqueles que se concentram em **Proteger o Planeta** contra a degradação e os impactos das mudanças climáticas. A iniciativa [Microsoft Sustainability](https://www.microsoft.com/en-us/sustainability) apoia esses objetivos explorando maneiras pelas quais soluções tecnológicas podem promover futuros mais sustentáveis com um [foco em 4 metas](https://dev.to/azure/a-visual-guide-to-sustainable-software-engineering-53hh) - ser carbono negativo, positivo em água, zero desperdício e biodiverso até 2030.

Enfrentar esses desafios de maneira escalável e oportuna exige pensamento em escala de nuvem - e dados em grande escala. A iniciativa [Planetary Computer](https://planetarycomputer.microsoft.com/) fornece 4 componentes para ajudar cientistas de dados e desenvolvedores nesse esforço:

 * [Catálogo de Dados](https://planetarycomputer.microsoft.com/catalog) - com petabytes de dados de sistemas terrestres (gratuitos e hospedados no Azure).
 * [API Planetária](https://planetarycomputer.microsoft.com/docs/reference/stac/) - para ajudar os usuários a buscar dados relevantes no espaço e no tempo.
 * [Hub](https://planetarycomputer.microsoft.com/docs/overview/environment/) - ambiente gerenciado para cientistas processarem conjuntos de dados geoespaciais massivos.
 * [Aplicações](https://planetarycomputer.microsoft.com/applications) - mostram casos de uso e ferramentas para insights de sustentabilidade.
**O Projeto Planetary Computer está atualmente em fase de prévia (a partir de setembro de 2021)** - veja como você pode começar a contribuir para soluções de sustentabilidade usando ciência de dados.

* [Solicite acesso](https://planetarycomputer.microsoft.com/account/request) para iniciar a exploração e se conectar com outros profissionais.
* [Explore a documentação](https://planetarycomputer.microsoft.com/docs/overview/about) para entender os conjuntos de dados e APIs suportados.
* Explore aplicações como [Monitoramento de Ecossistemas](https://analytics-lab.org/ecosystemmonitoring/) para se inspirar em ideias de aplicações.

Pense em como você pode usar visualização de dados para expor ou amplificar insights relevantes em áreas como mudanças climáticas e desmatamento. Ou reflita sobre como esses insights podem ser usados para criar novas experiências de usuário que motivem mudanças comportamentais para um estilo de vida mais sustentável.

## Ciência de Dados + Estudantes

Já falamos sobre aplicações no mundo real na indústria e na pesquisa, e exploramos exemplos de aplicações de ciência de dados nas humanidades digitais e na sustentabilidade. Então, como você pode desenvolver suas habilidades e compartilhar sua expertise como iniciante em ciência de dados?

Aqui estão alguns exemplos de projetos de estudantes em ciência de dados para inspirar você.

* [Escola de Verão de Ciência de Dados da MSR](https://www.microsoft.com/en-us/research/academic-program/data-science-summer-school/#!projects) com [projetos](https://github.com/msr-ds3) no GitHub explorando tópicos como:
   - [Viés racial no uso da força pela polícia](https://www.microsoft.com/en-us/research/video/data-science-summer-school-2019-replicating-an-empirical-analysis-of-racial-differences-in-police-use-of-force/) | [Github](https://github.com/msr-ds3/stop-question-frisk)
   - [Confiabilidade do sistema de metrô de Nova York](https://www.microsoft.com/en-us/research/video/data-science-summer-school-2018-exploring-the-reliability-of-the-nyc-subway-system/) | [Github](https://github.com/msr-ds3/nyctransit)
* [Digitalizando a Cultura Material: Explorando distribuições socioeconômicas em Sirkap](https://claremont.maps.arcgis.com/apps/Cascade/index.html?appid=bdf2aef0f45a4674ba41cd373fa23afc) - de [Ornella Altunyan](https://twitter.com/ornelladotcom) e equipe em Claremont, usando [ArcGIS StoryMaps](https://storymaps.arcgis.com/).

## 🚀 Desafio

Procure artigos que recomendem projetos de ciência de dados para iniciantes - como [esses 50 tópicos](https://www.upgrad.com/blog/data-science-project-ideas-topics-beginners/) ou [essas 21 ideias de projetos](https://www.intellspot.com/data-science-project-ideas) ou [esses 16 projetos com código fonte](https://data-flair.training/blogs/data-science-project-ideas/) que você pode desconstruir e remixar. E não se esqueça de blogar sobre suas jornadas de aprendizado e compartilhar seus insights com todos nós.

## Quiz Pós-Aula

## [Quiz pós-aula](https://ff-quizzes.netlify.app/en/ds/)

## Revisão & Autoestudo

Quer explorar mais casos de uso? Aqui estão alguns artigos relevantes:
* [17 Aplicações e Exemplos de Ciência de Dados](https://builtin.com/data-science/data-science-applications-examples) - Jul 2021
* [11 Aplicações Impressionantes de Ciência de Dados no Mundo Real](https://myblindbird.com/data-science-applications-real-world/) - Mai 2021
* [Ciência de Dados no Mundo Real](https://towardsdatascience.com/data-science-in-the-real-world/home) - Coleção de Artigos
* Ciência de Dados em: [Educação](https://data-flair.training/blogs/data-science-in-education/), [Agricultura](https://data-flair.training/blogs/data-science-in-agriculture/), [Finanças](https://data-flair.training/blogs/data-science-in-finance/), [Filmes](https://data-flair.training/blogs/data-science-at-movies/) e mais.

## Tarefa

[Explore um Conjunto de Dados do Planetary Computer](assignment.md)

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.