# Introdução a Ética de Dados

|![ Sketchnote por [(@sketchthedocs)](https://sketchthedocs.dev) ](../../../sketchnotes/02-Ethics.png)|
|:---:|
| Ética em Ciência de Dados - _Sketchnote por [@nitya](https://twitter.com/nitya)_ |

---

Nós somos todos cidadãos dos dados vivendo em um mundo de dados.

Tendências do mercado nos mostram que até 2022, 1 em 3 grandes organizações irá comprar e vender seus dados através de [Marketplaces e Exchanges](https://www.gartner.com/smarterwithgartner/gartner-top-10-trends-in-data-and-analytics-for-2020/) online. Como **Desenvolvedores de Aplicativos**, nós vamos achar mais fácil e mais barato integrar insights baseados em dados e automações baseadas em algoritmos nas experiências diárias dos usuário. Mas conforme IA se torna mais difundida, nós também vamos precisar entender os danos potenciais causado pelo uso desses algoritmos [como uma arma](https://www.youtube.com/watch?v=TQHs8SA1qpk).

Tendências também indicam que nós vamos criar e consumir mais de [180 zettabytes](https://www.statista.com/statistics/871513/worldwide-data-created/) de dados em 2025. Como **Cientistas de Dados**, isso nos dará níveis de acesso sem precedentes à dados pessoais. Isso significa que poderemos construir perfis comportamentais dos usuário e influenciar tomadas de decisão de uma forma que crie a [ilusão da livre escolha](https://www.datasciencecentral.com/profiles/blogs/the-illusion-of-choice) enquanto potencialmente direcionando os usuários na direção do resultado que nós preferimos. Isso também levanta questões mais amplas sobre privacidade dos dados e proteção dos usuários.

Ética dos dados é agora uma _proteção necessário_ para ciẽncia de dados e engenharia, nos ajudando a minimizar potenciais danos e consequências não intencionas das nossas ações realizadas com base em dados. O [Gartner Hype Cycle for AI](https://www.gartner.com/smarterwithgartner/2-megatrends-dominate-the-gartner-hype-cycle-for-artificial-intelligence-2020/) identifica tendências relevantes ná ética digital, IAs responsáveis, e governanças de IA como principais impulsionadores para grandes mega tendências sobre _democratização_ e _industrialização_ da IA.

![Gartner's Hype Cycle for AI - 2020](https://images-cdn.newscred.com/Zz1mOWJhNzlkNDA2ZTMxMWViYjRiOGFiM2IyMjQ1YmMwZQ==)

Nessa aula, nós vamos explorar a área fascinante de ética dos dados - desde conceitos essenciais e desafios, para estudos de caso e conceitos de IA aplicados como governança - isso ajuda a estabelecer a cultura da ética nos times e organizações que trabalham com dados e IA.




## [Quiz pré aula](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/2) 🎯

## Definição Básica

Vamos começar entendendo o básico da terminologia.

A palavra "ética" vem da [palavra Grega "ethikos"](https://en.wikipedia.org/wiki/Ethics) (e sua raíz "ethos") que significa _caráter ou natureza moral_.

**Ética** é sobre os valores e princípios morais compartilhados que governam o nosso comportamento em sociedade. Ética é baseada não nas leis mas nas normas amplamente aceitas sobre o que é "certo vs. errado". No entanto, considerações éticas podem influenciar iniciativas de governança corporativa e regulamentações governamentais que criam mais incentivos para conformidade (compliance).

**Ética de Dados** é uma [nova ramificação da ética](https://royalsocietypublishing.org/doi/full/10.1098/rsta.2016.0360#sec-1) que "estuda e avalia problemas morais relacionados a _dados, algoritmos e práticas correspondentes_". Aqui, **"dados"** focam nas ações relacionadas a geração, gravação, curadoria, disseminação de processamento, compartilhamento, e uso, **"algoritmos"** focam em IA, agentes, aprendizado de máquina, e robôs, e **"práticas"** focam em tópicos como inovação responsável, programação, hacking e códigos de ética.

**Ética Aplicada** é a [aplicação prática de considerações morais](https://en.wikipedia.org/wiki/Applied_ethics). É o processo de investigar ativamente problemáticas éticas no contexto de _ações do mundo real, produtos e processos_, e tomar medidas corretivas para fazer com que esses permanecam alianhados com o nossos valores éticos definidos.

**Cultura Ética** é sobre [operacionalizar a ética aplicada](https://hbr.org/2019/05/how-to-design-an-ethical-organization) para garantir que nossos princípios e práticas éticas sejam adotados de maneira consistente e escalável em toda a organização. Culturas éticas de sucesso definem princípios éticos em toda a organização, fornecem incentivos significativos para consistência, e reinforça as normas éticas encorajando e amplificando comportmentos desejados em todos os níveis da organização.


## Conceitos Éticos

Nessa seção, nós vamos discutir conceitos como **valores compartilhados** (princípios) e **desafios éticos** (problemas) para a ética de dados - e explorar **estudos de caso** que ajudam você a entender esses conceitos em contextos do mundo real.

### 1. Princípios Éticos

Toda estratégia de ética de dados começa definindo _pricípios éticos_ - os "valores compartilhados" que descrevem comportamentos aceitáveis, e guia ações complacentes, nos nossos dados e nos projetos de IA. Você pode definir eles individualmente ou com um time. No entando, a maioria das grandes organizações descreve eles em uma declaração de missão ou de estrutura de _IA ética_ que é definida em níveis corporativos e aplicadas consistentemente em todos os times.

**Exemplo:** a declaração de missão da [IA responsável](https://www.microsoft.com/pt-br/ai/responsible-ai?activetab=pivot1:primaryr6) da Microsoft afirma: _"Estamos comprometidos com o avanço da AI impulsionados por princípios éticos que colocam as pessoas em primeiro lugar."_ - identificando 6 princípios éticos na estrutura abaixo:

![IA Responśavel na Microsoft](https://docs.microsoft.com/en-gb/azure/cognitive-services/personalizer/media/ethics-and-responsible-use/ai-values-future-computed.png)

Vamos explorar brevemente esses princípios. _Transparência_ e _responsabilidade_ são valores fundamentais nos quais outros princípios construíram sobre - então vamos começar aí:

* [**Responsabilidade**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) torna os profissionais _responsáveis_ pelos seus dados e operações da IA, e conformidade (compliance) com esses princípios éticos.
* [**Transparência**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) garante que os dados e as ações da IA são _compreesíveis_ (interpretáveis) para os usuários, explicando o que e o porquê por trás de cada decisão.
* [**Justiça**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1%3aprimaryr6) - foca em garantir que a IA _trate_ todas as pessoas de forma justa, abordando quaisquer preconceitos sociotécnicos implícitos ou sistêmicos nos dados e sistemas.
* [**Confiabilidade e Segurança**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) - garante que a IA comporte de maneira _consistente_ com os valores definidos, minimizando potenciais danos ou consequências não pretendidas.
* [**Segurança e Privacidade**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) - é sobre compreender as linhagem dos dados, e fornecer _privacidade de dados e proteções relacionadas_ aos usuários.
* [**Inclusão**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) - é sobre projetar soluções de IA com intenção, adaptando elas para atender uma _vasta game de necessidades humanas_ & capacidades.

> 🚨 Pense sobre qual poderia ser a frase de missão da sua ética de dados. Explore estruturas éticas de IA de outras organizações - aqui estão alguns exemplos da [IBM](https://www.ibm.com/cloud/learn/ai-ethics), [Google](https://ai.google/principles), e [Facebook](https://ai.facebook.com/blog/facebooks-five-pillars-of-responsible-ai/). Quais valores compartilhados vocês tem em comum? Como esses princípios se relacionam ao produto de IA ou à indústria na qual eles operam?

### 2. Desafios de Ética

Uma vez que nossos princípios éticos estão definidos, o próximo passo é avaliar nossos dados e ações da IA  para ver se eles estão alinhados com aqueles valores compartilhados. Pense sobre suas ações em duas categorias: _coleção de dados_ e _design de algoritmo_.

Com coleções dados, ações irão, provavelmente, envolver **dados pessoais** ou informação pessoalmente identificável (do Inglês, personally identifiable information, ou PII) para indivíduos vivos identificáveis. Isso inclui [itens diversos de dados não pessoais](https://ec.europa.eu/info/law/law-topic/data-protection/reform/what-personal-data_en) que _coletivamente_ identificam um indivíduo. Desafios éticos podem estar relacionados à _privacidade dos dados_, _qualidade dos dados_, e tópicos relacionados como _consentimento informado_ e _direitos de propriedades intelectuais_ para os usuários.

Com o design de algoritmo, as ações envolverão coleta e curadoria dos **datasets**, e então o uso deles para treinar e implantar **modelos de dados** que predizem resultados ou automatizam decisões em contextos do mundo real. Desafios éticos podem surgir de _vieses do dataset_ (biases), problemas com a _qualidade de dados_, _injustiça_, e _má representação_ nos algoritmos - incluindo alguns problemas que são sistêmicos na natureza.

Em ambos os casos, desafios de ética destacam áreas onde nossas ações podem conflitar com nossos valores compartilhados. Para detectar, mitigar, minimizar, ou eliminar, essas preocupações - nós precisamos perguntar questões morais de "sim ou não" relacionadas as nossas ações, e então tomar uma ação corretiva conforme necessário. Vamos olhar alguns desafios éticos e as questões morais que eles levantam:


#### 2.1 Propriedade de Dados

A coleta de dados geralmente envolve dados pessoais que podem identificar os titulares dos dados. [Propriedade de dados](https://permission.io/blog/data-ownership) é sobre o _controle_ e [_direitos dos usuários_](https://permission.io/blog/data-ownership) relacionados à criação, processamento, e disseminação dos dados.

As questões morais que precisamos nos perguntar são:
 * Quem detêm/possui os dados? (usuário ou organização)
 * Quais direitos os titulares dos dados tem? (ex: acesso, apagar, portabilidade)
 * Quais direitos as organizações tem? (ex: retificar reviews maliciosas de usuários)

#### 2.2 Consentimento Informado

[Consentimento Informado](https://legaldictionary.net/informed-consent/) define o ato dos usuários aceitar uma ação (como a coleta de dados) com um _compreendimento total_ de fatos relevantes incluindo propósito, potenciais riscos, e alternativas.

Questões a se explorar aqui são:
 * O usuário (titular dos dados) deu permissão para a captação e uso dos dados?
 * O usuário entendeu o propósito para o qual aqueles dados foram coletados?
 * O usuário entendeu os potenciais riscos de sua participação?

#### 2.3 Propriedade Intelectual

[Propriedade intelectual](https://en.wikipedia.org/wiki/Intellectual_property) se refere a criações intangíveis que foram resultados das iniciativas humanas, que podem _ter valor econômico_ para indivíduos ou negócios.

Questões a se explorar aqui são:
 * Os dados coletados tem valor econômicos para um usuário ou negócio?
 * O **usuário** tem propriedade intelectual aqui?
 * As **organizações** tem propriedade intelectual aqui?
 * Se esses direitos existem, como estamos protejendo eles?

#### 2.4 Privacidade de Dados

[Privacidade de dados](https://www.northeastern.edu/graduate/blog/what-is-data-privacy/) ou privacidade da informação se refere a preservação da privacidade do usuário e proteção da identidade do usuário com relação as informações de indentificação pessoal.

Questões a se explorar aqui são:
 * Os dados (pessoais) dos usuários estão protegidos contra hacks e vazamentos?
 * Os dados do usuário são acessíveis somente a usuários e contextos autorizados?
 * A anonimidade do usuário são preservados quando os dados são compartilhados ou disseminados?
 * Um usuário podem ser desindentificado de datasets anônimos?


#### 2.5 Direito a Ser Esquecido

o [Direito a Ser Esquecido](https://en.wikipedia.org/wiki/Right_to_be_forgotten) ou [Direito de Apagar](https://www.gdpreu.org/right-to-be-forgotten/) fornecem proteções de dados adicionais para os usuários. Especificamente, dá aos usuários o direito de pedir deleção ou remoção dos dados pessoais das buscas da Internet e outros locais, _sobre circunstâncias específicas_ - permitindo a eles um novo começo online sem que as ações passadas sejam colocadas contra eles.

Questões a se explorar aqui são:
 * O sistema permite que os titulares dos dados peçam o apagamento dos mesmos?
 * A retirada do consentimento do usuário deve acionar um apagamento automático?
 * Dados foram colocados sem o consentimento ou por meios ilegais?
 * Estamos de acordo com regulações governamentais para a privacidade de dados?


#### 2.6 Viéses dos Datasets

[Viéses da Coleção ou do Dataset](http://researcharticles.com/index.php/bias-in-data-collection-in-research/) é sobre selecionar um subset de dados _não representativos_ para o desenvolvimento de um algoritmo, criando potenciais injustiças nos resultados para grupos diversos. Os tipos de viéses incluem seleção ou viés da amostra, viés voluntário, e viés do instrumento.

Questões a se explorar aqui são:
 * Recrutamos um conjunto representativo de titulares de dados?
 * Nós testamos nossos datasets colecionados ou com curadoria para diversos viéses?
 * Nós podemos mitigar ou remover quaisquer viéses descobertos?

#### 2.7 Qualidade de Dados

[Qualidade de Dados](https://lakefs.io/data-quality-testing/) procura pela validade do dataset com curadoria usado para desenvolver nossos algoritmos, checando para ver se recursos e registros atendem os requisitos para o nível de acurácia e consistência necessários para o propósito da nossa IA.

Questões a se explorar aqui são:
 * Nós coletamos _features_ válidos para nosso caso de uso?
 * Os dados foram coletados _consistentemente_ em diversas fontes de dados?
 * O dataset é _completo_ para diversas condições e cenários?
 * As informações capturadas refletem _com precisão_ a realidade?

#### 2.8 Justiça do Algoritmo

[Justiça do Algoritmo](https://towardsdatascience.com/what-is-algorithm-fairness-3182e161cf9f) checa para ver se o design do algoritmo discrimina sistematicamente subgrupos específicos dos titulares dos dados levando a [potenciais danos](https://docs.microsoft.com/en-us/azure/machine-learning/concept-fairness-ml) em _alocação_ (onde recursos são negados ou detidos daquele grupo) e _qualidade de serviço_ (onde IA não é tão acurada para alguns subgrupos quanto é para outros).

Questões a se explorar aqui são:
 * Nós avaliamos a acurácia do modelo para diversos subgrupos e condições?
 * Nós examinamos o sistema em busca de danos potenciais (ex. estereótipos)?
 * Nós podemos revisar os dados ou retreinar os modelos para mitigar danos identificados?

Explore recursos como [Checklist de Justiça de IA](https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RE4t6dA) para saber mais.

#### 2.9 Má Representação

[Má Representação dos Dados](https://www.sciencedirect.com/topics/computer-science/misrepresentation) é sobre perguntar se nós estamos comunicando insights de dados honestamente relatados de uma maneira enganosa para suportar uma narrativa desejada.

Questões a se explorar aqui são:
 * Estamos relatando dados completos ou inacurados?
 * Estamos visualizando dados de uma maneira que conduz a uma conclusão errada?
 * Estamos usando técnicas estatísticas seletivas para manipular os resultados?
 * Existem explicações alternativas que podem oferecer uma conclusão diferente?

#### 2.10 Livre Escolha
A [Ilusão da Livre Escolha](https://www.datasciencecentral.com/profiles/blogs/the-illusion-of-choice) ocorre quando as "arquiteturas de escolha" do sistema utiliza algoritmos de tomada de decisão para incentivar as pessoas a obterem um resultado preferido enquanto parece lhe dar opções e controle. Esses [dark patterns](https://www.darkpatterns.org/) podem causar danos sociais e econômicos aos usuários. Já que as decisões do usuário impactam perfis de comportamento, essas ações potencialmente conduzem as escolhas futuras que podem aplificar ou extender o impacto desses danos.

Questões a se explorar aqui são:
 * O usuário entende as implicações de fazer aquela escolha?
 * O usuário estava ciente das escolhas (alternativas) e dos prós e contras de cada uma?
 * O usuário pode reverter um escolha automatizada ou influenciada depois?

### 3. Estudo de Casos

Para colocar esses desafios éticos em contextos do mundo real, ajuda olhar para estudo de casos que destacam potenciais danos e consequências para indivíduos e sociedade, quando essas violações éticas são negligenciadas.

Aqui estão alguns exemplos:

| Desafios de Éticas | Estudo de Caso  | 
|--- |--- |
| **Consentimento Informado** | 1972 - [Tuskegee Syphillis Study](https://en.wikipedia.org/wiki/Tuskegee_Syphilis_Study) - Homens afro-americanos que participaram no estudo foram prometidos cuidados médicos livres de custo _mas foram enganados_ pelos pesquisadores que não informaram os participantes de seus diagnósticos ou sobre a avaliabilidade de tratamentos. Muitos participantes morreram e parceiros e ciranças foram afetados; oe studo durou por 40 anos. | 
| **Privacidade de Dados** |  2007 - O [Netflix data prize](https://www.wired.com/2007/12/why-anonymous-data-sometimes-isnt/) forneceu a pesquisadores _10M de avaliações anônimas de filmes de 50K clientes_ para ajudar a melhorar os algoritmos de recomendação. No entanto, os pesquisadores conseguiram correlacionar os dados anônimos com dados de identificação pessoal em _datasets externos_ (ex. comentários no IMDb) - "desanonimizando" efetivamente alguns assinates da Netflix.|
| **Viéses dos Datasets**  | 2013 - A Cidade de Boston [desenvolveu Street Bump](https://www.boston.gov/transportation/street-bump), um aplicativo que deixa os usuários relatarem burcos nas ruas, dando à cidade melhores dados rodoviários para encontrar e consertar problemas. No entanto, [pessoas que faziam parte de grupos de baixa renda tinham menos acesso a carros e celulares](https://hbr.org/2013/04/the-hidden-biases-in-big-data), fazendo com que os seus problema rodoviários fossem invisíveis nesse aplicativo. Desenvolvedores trabalharm com acadêmicos para questões de _acesso equitativo e divisões digitais_ para justiça. |
| **Justiça do Algoritmo**  | 2018 - [O Gender Shades Study do MIT](http://gendershades.org/overview.html) avaliou a acurácia de produtos de IA de classificação de gêneros, expondo lacunas na acurácia para mulheres e pessoas não brancas. Um [Apple Card de 2019](https://www.wired.com/story/the-apple-card-didnt-see-genderand-thats-the-problem/) parece oferecer menos créditos para mulheres do que oferece para homens. Ambos ilustraram questões de viés algorítmico levando a danos socioeconômicos.|
| **Má Representação de Dados** | 2020 - O [Departamento de Sáude Pública da Georgia (Georgia Department of Public Health) liberou gráficos da COVID-19](https://www.vox.com/covid-19-coronavirus-us-response-trump/2020/5/18/21262265/georgia-covid-19-cases-declining-reopening) que aparentam a levar os cidadãos a conclusões errôneas sobre as tendências em casos confirmados em uma ordem não cronológica no eixo x. Isso ilustra a má representação atráves de truques de visualização. |
| **Ilusão da Livre Escolha** | 2020 - Aplicativo de aprendizado [ABCmouse pagou $10M para resolver uma reclamação do FTC](https://www.washingtonpost.com/business/2020/09/04/abcmouse-10-million-ftc-settlement/) onde os pais foram enganados a pagar assinaturas que eles não podiam cancelar. Isso ilustra "dark patterns" em arquiteturas de escolha, onde usuários foram direcionados a escolhas potencialmente prejudiciais. |
| **Privacidade de Dados & Direitos do Usuário** | 2021 - [Violação de Dados do facebook](https://www.npr.org/2021/04/09/986005820/after-data-breach-exposes-530-million-facebook-says-it-will-not-notify-users) expôs dados de mais de 530M de usuários, resultando em um acordo de $5B com o FTC (Federal Trade Commission). No entanto, o Facebook se recusou a notificar os usuários sobre a violação dos dados violando os direitos dos usuários de transparência e acesso de dados. |

Gostaria de explorar mais estudos de caso? Confira:
* [Ethics Unwrapped](https://ethicsunwrapped.utexas.edu/case-studies) - dilemas éticos em indústrias diversas.
* [Data Science Ethics course](https://www.coursera.org/learn/data-science-ethics#syllabus) - estudos de caso marcantes explorados.
* [Where things have gone wrong](https://deon.drivendata.org/examples/) - checklists da deon com exemplos

> 🚨 Pense sobre estudos de caso que você ja viu - você ja experienciou, ou foi afetado por, um desafio ético similar em sua vida? Voce consegue pensar em pelo menos um estudo de caso que ilustre um ou mais desafios éticos que discutimos nessa seção?

## Ética aplicada

Nós falamos sobre conceitos de éticas, desafios, e casos de estudo em contextos do mundo real. Mas como nós começamos a _aplicar_ esses princípios éticos em nossos projetos? E como nós _operacionalizamos_ essas práticas para melhor governância? Vamos explorar algumas soluções do mundo real:

### 1. Códigos Profissionais

Códigos Profisionais oferecem uma opção para organizações para "incentivar" membros a apoiar os princípios éticos e frase de missão. Códigos são _diretrizes morais_ para comportamento profissional, ajudando funcionários ou membros a tomar decisões que alinhem com os princípios da sua organização. Eles são tão bons quanto a conformidade voluntária dos membros; no entanto, muitas organizações oferecem recompensas e penalidades adicionais para motivar a conformidade dos membros.

Exemplos incluem:

 * [Oxford Munich](http://www.code-of-ethics.org/code-of-conduct/) Código de Ética
 * [Data Science Association](http://datascienceassn.org/code-of-conduct.html) Código de Conduta (criado em 2013)
 * [ACM Code of Ethics and Professional Conduct](https://www.acm.org/code-of-ethics) (desde 1993)

> 🚨 Você faz parte de uma organização profissional de engenharia ou de ciências de dados? Explore o site deles para ver se eles definem um código de ética profissional. O que diz sobre os princípios éticos deles? Como eles estão "incentivando" os membros a seguir o código?

### 2. Checklists de Éticas

Enquanto códigos profissionais definem _comportamentos ético_ requiridos de seus praticantes, eles [tem limitações conhecidas](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md) na execução, particularmente em projetos de larga escala. Ao invés disso, muitos experts em Ciência de Dados [defendem as checklists](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md), que podem **conectar princípios a práticas** de maneiras para determinísticas e acionáveis.

Checklists convertem as questões em tarefas de "sim/não" que podem ser operacionalizadas, permitindo eles serem rastreados como parte dos fluxos de trabalho de liberação de produtos padrão. 

Exemplos incluem:
 * [Deon](https://deon.drivendata.org/) - uma checklist de propósito gerak criado a partir de [recomendações da insústria](https://deon.drivendata.org/#checklist-citations) com uma ferramenta de linha de comando para fácil integração.
 * [Privacy Audit Checklist](https://cyber.harvard.edu/ecommerce/privacyaudit.html) - fornece orientação geral para práticas de manipulação de informação a partir de perspectivas de exposição legal e social.
 * [AI Fairness Checklist](https://www.microsoft.com/en-us/research/project/ai-fairness-checklist/) - criado por praticantes de IA para apoiar a adoção e integração de verificações de justiça dentro dos ciclos de desenvolvimento de IA.
 * [22 questions for ethics in data and AI](https://medium.com/the-organization/22-questions-for-ethics-in-data-and-ai-efb68fd19429) - estrutura mais aberto-fechado, estrturado para exploração inicial de problemas éticos em contextos de design, implementação, e organizacional.

### 3. Regulações Éticas

Ética é sobre definir valores compartilhados e fazer a coisa certa _voluntariamente_. **Compliance (Conformidade)** é sobre _seguir a lei_ se e onde definida. **Governância** abrange amplamente todos as formas de como as organizações operam para garantir princípios éticos e cumprir as leis estabelecidas.

Hoje, governância assume duas formas dentro das organizações. Primeira, é sobre definir princípios de **IA ética** e estabelecer práticas para operacionalizar a adoção em todos os projetos de IA na organização. Segundo, trata-se de cumprir com todos os **regulamentos de proteção de dados** para as regiões em que operam.

Exemplos de proteção de dados e regulamentos de privacidade:

 * `1974`, [US Privacy Act](https://www.justice.gov/opcl/privacy-act-1974) - regula a coleta, o uso, e divulgação de informações pessoais por parte do _governo federal_.
 * `1996`, [US Health Insurance Portability & Accountability Act (HIPAA)](https://www.cdc.gov/phlp/publications/topic/hipaa.html) - protege dados de sáude pessoais.
 * `1998`, [US Children's Online Privacy Protection Act (COPPA)](https://www.ftc.gov/enforcement/rules/rulemaking-regulatory-reform-proceedings/childrens-online-privacy-protection-rule) - protege a privacidade de dados de crianças menores de 13 anos de idade.
 * `2018`, [General Data Protection Regulation (GDPR)](https://gdpr-info.eu/) - fornece direitos aos usuário, proteção de dados, e privacidade.
 * `2018`, [California Consumer Privacy Act (CCPA)](https://www.oag.ca.gov/privacy/ccpa) dá aos consumidores mais _direitos_ sobre seus dados (pessoais).
 * `2021`, [A Lei de Proteção de Informação Pessoal](https://www.reuters.com/world/china/china-passes-new-personal-data-privacy-law-take-effect-nov-1-2021-08-20/) da China acabou de ser passado, criando uma das regulações de privacidade de dados online mais forte do mundo.

> 🚨 A GDPR (General Data Protection Regulation) da União Europia continua sendo umas das regulações de privacidade de dados mais influentes hoje em dia. Você sabia que a mesma também define [8 direitos dos usuário](https://www.freeprivacypolicy.com/blog/8-user-rights-gdpr) para proteger a privacidade dos cidadãos e dados pessoais? Saiba mais sobre o que são e porque eles importam.


### 4. Cultura Ética

Note que existe uma lacuna intangível entre _compliance_ (fazer o suficiente para cumprir a "a carta da lei") e abordar [problemas sistêmicos](https://www.coursera.org/learn/data-science-ethics/home/week/4) (como ossificação, assimetria informacional, e injustiça distribucional) que podem acelerar o uso da IA como uma arma.

Este último requere [abordagens colaborativas para definir culturas éticas](https://towardsdatascience.com/why-ai-ethics-requires-a-culture-driven-approach-26f451afa29f) que constrói conexões emocionais e valores compartilhados consistentes _em todas as organizações_ na indústria. Isso requere mais [culturas de ética de dados formalizadas](https://www.codeforamerica.org/news/formalizing-an-ethical-data-culture/) nas organizações - permitindo _qualquer um_ a [puxar o cordão Andom](https://en.wikipedia.org/wiki/Andon_(manufacturing)) (para aumentar as preocupações éticas mais cedo no processo) e fazendo _avaliações éticas_ (ex. na contratação) um critério fundamental na formação de times em projetos de IA.

---
## [Quiz pós aula](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/3) 🎯
## Revisão e Autoestudo

Cursos e livros ajudam a entender os conceitos essencias da ética, enquanto estudos de caso e ferramentas ajudam com práticas da ética aplicado em contextos do mundo real. Aqui estão alguns recursos para começar.

* [Machine Learning For Beginners](https://github.com/microsoft/ML-For-Beginners/blob/main/1-Introduction/3-fairness/README.md) - aula sobre Justiça, da Microsoft.
* [Principles of Responsible AI](https://docs.microsoft.com/en-us/learn/modules/responsible-ai-principles/) - programa de aprendizado gratuito da Microsoft Learn.
* [Ethics and Data Science](https://resources.oreilly.com/examples/0636920203964) - O'Reilly EBook (M. Loukides, H. Mason et. al)
* [Data Science Ethics](https://www.coursera.org/learn/data-science-ethics#syllabus) - curso online da Universidade de Michigan.
* [Ethics Unwrapped](https://ethicsunwrapped.utexas.edu/case-studies) - estudos de caso da Universidade do Texas.

# Tarefa 

[Escreva um Caso de Uso de Ética de Dados](assignment.pt-br.md)
