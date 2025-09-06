<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1341f6da63d434f5ba31b08ea951b02c",
  "translation_date": "2025-09-06T08:37:30+00:00",
  "source_file": "1-Introduction/02-ethics/README.md",
  "language_code": "br"
}
-->
# Introdução à Ética de Dados

|![ Sketchnote por [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/02-Ethics.png)|
|:---:|
| Ética em Ciência de Dados - _Sketchnote por [@nitya](https://twitter.com/nitya)_ |

---

Somos todos cidadãos de dados vivendo em um mundo dataficado.

Tendências de mercado indicam que, até 2022, 1 em cada 3 grandes organizações comprará e venderá seus dados por meio de [Mercados e Exchanges](https://www.gartner.com/smarterwithgartner/gartner-top-10-trends-in-data-and-analytics-for-2020/) online. Como **Desenvolvedores de Aplicativos**, será mais fácil e barato integrar insights baseados em dados e automação orientada por algoritmos nas experiências diárias dos usuários. Mas, à medida que a IA se torna onipresente, também precisaremos entender os potenciais danos causados pela [armazenização](https://www.youtube.com/watch?v=TQHs8SA1qpk) desses algoritmos em larga escala.

As tendências também indicam que criaremos e consumiremos mais de [180 zettabytes](https://www.statista.com/statistics/871513/worldwide-data-created/) de dados até 2025. Como **Cientistas de Dados**, isso nos dá níveis sem precedentes de acesso a dados pessoais. Isso significa que podemos construir perfis comportamentais de usuários e influenciar a tomada de decisões de maneiras que criam uma [ilusão de escolha livre](https://www.datasciencecentral.com/profiles/blogs/the-illusion-of-choice), enquanto potencialmente direcionamos os usuários para resultados que preferimos. Isso também levanta questões mais amplas sobre privacidade de dados e proteção dos usuários.

A ética de dados agora é um _guia necessário_ para ciência e engenharia de dados, ajudando-nos a minimizar danos potenciais e consequências não intencionais de nossas ações baseadas em dados. O [Ciclo de Hype da Gartner para IA](https://www.gartner.com/smarterwithgartner/2-megatrends-dominate-the-gartner-hype-cycle-for-artificial-intelligence-2020/) identifica tendências relevantes em ética digital, IA responsável e governança de IA como fatores-chave para megatendências maiores em torno da _democratização_ e _industrialização_ da IA.

![Ciclo de Hype da Gartner para IA - 2020](https://images-cdn.newscred.com/Zz1mOWJhNzlkNDA2ZTMxMWViYjRiOGFiM2IyMjQ1YmMwZQ==)

Nesta lição, exploraremos a fascinante área da ética de dados - desde conceitos e desafios fundamentais até estudos de caso e conceitos aplicados de IA, como governança - que ajudam a estabelecer uma cultura ética em equipes e organizações que trabalham com dados e IA.

## [Questionário pré-aula](https://ff-quizzes.netlify.app/en/ds/quiz/2) 🎯

## Definições Básicas

Vamos começar entendendo a terminologia básica.

A palavra "ética" vem da [palavra grega "ethikos"](https://en.wikipedia.org/wiki/Ethics) (e sua raiz "ethos"), que significa _caráter ou natureza moral_.

**Ética** trata dos valores compartilhados e princípios morais que governam nosso comportamento na sociedade. A ética não se baseia em leis, mas em normas amplamente aceitas do que é "certo versus errado". No entanto, considerações éticas podem influenciar iniciativas de governança corporativa e regulamentações governamentais que criam mais incentivos para conformidade.

**Ética de Dados** é um [novo ramo da ética](https://royalsocietypublishing.org/doi/full/10.1098/rsta.2016.0360#sec-1) que "estuda e avalia problemas morais relacionados a _dados, algoritmos e práticas correspondentes_". Aqui, **"dados"** se concentra em ações relacionadas à geração, registro, curadoria, processamento, disseminação, compartilhamento e uso; **"algoritmos"** se concentra em IA, agentes, aprendizado de máquina e robôs; e **"práticas"** se concentra em tópicos como inovação responsável, programação, hacking e códigos de ética.

**Ética Aplicada** é a [aplicação prática de considerações morais](https://en.wikipedia.org/wiki/Applied_ethics). É o processo de investigar ativamente questões éticas no contexto de _ações, produtos e processos do mundo real_ e tomar medidas corretivas para garantir que permaneçam alinhados com nossos valores éticos definidos.

**Cultura Ética** trata de [_operacionalizar_ a ética aplicada](https://hbr.org/2019/05/how-to-design-an-ethical-organization) para garantir que nossos princípios e práticas éticas sejam adotados de maneira consistente e escalável em toda a organização. Culturas éticas bem-sucedidas definem princípios éticos em toda a organização, fornecem incentivos significativos para conformidade e reforçam normas éticas, incentivando e amplificando comportamentos desejados em todos os níveis da organização.

## Conceitos de Ética

Nesta seção, discutiremos conceitos como **valores compartilhados** (princípios) e **desafios éticos** (problemas) para ética de dados - e exploraremos **estudos de caso** que ajudam a entender esses conceitos em contextos do mundo real.

### 1. Princípios Éticos

Toda estratégia de ética de dados começa definindo _princípios éticos_ - os "valores compartilhados" que descrevem comportamentos aceitáveis e orientam ações em conformidade em nossos projetos de dados e IA. Você pode defini-los em nível individual ou de equipe. No entanto, a maioria das grandes organizações os descreve em uma declaração de missão ou estrutura de _IA ética_ definida em níveis corporativos e aplicada de forma consistente em todas as equipes.

**Exemplo:** A declaração de missão de [IA Responsável](https://www.microsoft.com/en-us/ai/responsible-ai) da Microsoft diz: _"Estamos comprometidos com o avanço da IA orientada por princípios éticos que colocam as pessoas em primeiro lugar"_ - identificando 6 princípios éticos na estrutura abaixo:

![IA Responsável na Microsoft](https://docs.microsoft.com/en-gb/azure/cognitive-services/personalizer/media/ethics-and-responsible-use/ai-values-future-computed.png)

Vamos explorar brevemente esses princípios. _Transparência_ e _responsabilidade_ são valores fundamentais sobre os quais outros princípios são construídos - então vamos começar por aí:

* [**Responsabilidade**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) torna os profissionais _responsáveis_ por suas operações de dados e IA e pela conformidade com esses princípios éticos.
* [**Transparência**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) garante que as ações de dados e IA sejam _compreensíveis_ (interpretáveis) para os usuários, explicando o que e por que por trás das decisões.
* [**Justiça**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1%3aprimaryr6) - foca em garantir que a IA trate _todas as pessoas_ de forma justa, abordando quaisquer preconceitos sociotécnicos sistêmicos ou implícitos em dados e sistemas.
* [**Confiabilidade e Segurança**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) - garante que a IA se comporte _consistentemente_ com os valores definidos, minimizando danos potenciais ou consequências não intencionais.
* [**Privacidade e Segurança**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) - trata de entender a linhagem dos dados e fornecer _privacidade de dados e proteções relacionadas_ aos usuários.
* [**Inclusividade**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) - trata de projetar soluções de IA com intenção, adaptando-as para atender a uma _ampla gama de necessidades e capacidades humanas_.

> 🚨 Pense em qual poderia ser sua declaração de missão de ética de dados. Explore estruturas de IA ética de outras organizações - aqui estão exemplos da [IBM](https://www.ibm.com/cloud/learn/ai-ethics), [Google](https://ai.google/principles) e [Facebook](https://ai.facebook.com/blog/facebooks-five-pillars-of-responsible-ai/). Quais valores compartilhados eles têm em comum? Como esses princípios se relacionam com o produto ou setor de IA em que operam?

### 2. Desafios Éticos

Depois de definir os princípios éticos, o próximo passo é avaliar nossas ações de dados e IA para ver se estão alinhadas com esses valores compartilhados. Pense em suas ações em duas categorias: _coleta de dados_ e _design de algoritmos_.

Na coleta de dados, as ações provavelmente envolverão **dados pessoais** ou informações pessoalmente identificáveis (PII) de indivíduos identificáveis. Isso inclui [diversos itens de dados não pessoais](https://ec.europa.eu/info/law/law-topic/data-protection/reform/what-personal-data_en) que, _coletivamente_, identificam um indivíduo. Os desafios éticos podem estar relacionados à _privacidade de dados_, _propriedade de dados_ e tópicos relacionados, como _consentimento informado_ e _direitos de propriedade intelectual_ dos usuários.

No design de algoritmos, as ações envolverão a coleta e curadoria de **conjuntos de dados**, e o uso deles para treinar e implantar **modelos de dados** que preveem resultados ou automatizam decisões em contextos do mundo real. Os desafios éticos podem surgir de _viés nos conjuntos de dados_, problemas de _qualidade dos dados_, _injustiças_ e _distorções_ nos algoritmos - incluindo algumas questões que são sistêmicas por natureza.

Em ambos os casos, os desafios éticos destacam áreas onde nossas ações podem entrar em conflito com nossos valores compartilhados. Para detectar, mitigar, minimizar ou eliminar essas preocupações, precisamos fazer perguntas morais de "sim/não" relacionadas às nossas ações e tomar medidas corretivas conforme necessário. Vamos dar uma olhada em alguns desafios éticos e nas questões morais que eles levantam:

#### 2.1 Propriedade de Dados

A coleta de dados muitas vezes envolve dados pessoais que podem identificar os sujeitos dos dados. [Propriedade de dados](https://permission.io/blog/data-ownership) trata do _controle_ e [_direitos dos usuários_](https://permission.io/blog/data-ownership) relacionados à criação, processamento e disseminação de dados.

As questões morais que precisamos fazer são:
 * Quem é o proprietário dos dados? (usuário ou organização)
 * Quais direitos os sujeitos dos dados possuem? (ex: acesso, exclusão, portabilidade)
 * Quais direitos as organizações possuem? (ex: retificar avaliações maliciosas de usuários)

#### 2.2 Consentimento Informado

[Consentimento informado](https://legaldictionary.net/informed-consent/) define o ato de os usuários concordarem com uma ação (como coleta de dados) com um _entendimento completo_ dos fatos relevantes, incluindo o propósito, os riscos potenciais e as alternativas.

Questões a explorar aqui são:
 * O usuário (sujeito dos dados) deu permissão para a captura e uso dos dados?
 * O usuário entendeu o propósito para o qual os dados foram capturados?
 * O usuário compreendeu os riscos potenciais de sua participação?

#### 2.3 Propriedade Intelectual

[Propriedade intelectual](https://en.wikipedia.org/wiki/Intellectual_property) refere-se a criações intangíveis resultantes da iniciativa humana, que podem _ter valor econômico_ para indivíduos ou empresas.

Questões a explorar aqui são:
 * Os dados coletados têm valor econômico para um usuário ou empresa?
 * O **usuário** possui propriedade intelectual aqui?
 * A **organização** possui propriedade intelectual aqui?
 * Se esses direitos existem, como estamos protegendo-os?

#### 2.4 Privacidade de Dados

[Privacidade de dados](https://www.northeastern.edu/graduate/blog/what-is-data-privacy/) ou privacidade da informação refere-se à preservação da privacidade do usuário e proteção da identidade do usuário em relação a informações pessoalmente identificáveis.

Questões a explorar aqui são:
 * Os dados (pessoais) dos usuários estão protegidos contra invasões e vazamentos?
 * Os dados dos usuários estão acessíveis apenas a usuários e contextos autorizados?
 * O anonimato dos usuários é preservado quando os dados são compartilhados ou disseminados?
 * Um usuário pode ser desidentificado de conjuntos de dados anonimizados?

#### 2.5 Direito ao Esquecimento

O [Direito ao Esquecimento](https://en.wikipedia.org/wiki/Right_to_be_forgotten) ou [Direito à Exclusão](https://www.gdpreu.org/right-to-be-forgotten/) fornece proteção adicional de dados pessoais aos usuários. Especificamente, dá aos usuários o direito de solicitar a exclusão ou remoção de dados pessoais de buscas na Internet e outros locais, _sob circunstâncias específicas_ - permitindo-lhes um novo começo online sem que ações passadas sejam usadas contra eles.

Questões a explorar aqui são:
 * O sistema permite que os sujeitos dos dados solicitem a exclusão?
 * A retirada do consentimento do usuário deve acionar a exclusão automática?
 * Os dados foram coletados sem consentimento ou por meios ilegais?
 * Estamos em conformidade com as regulamentações governamentais para privacidade de dados?

#### 2.6 Viés nos Conjuntos de Dados

Viés nos conjuntos de dados ou [Viés de Coleta](http://researcharticles.com/index.php/bias-in-data-collection-in-research/) trata da seleção de um subconjunto _não representativo_ de dados para o desenvolvimento de algoritmos, criando potencial injustiça nos resultados para grupos diversos. Tipos de viés incluem viés de seleção ou amostragem, viés de voluntariado e viés de instrumento.

Questões a explorar aqui são:
 * Recrutamos um conjunto representativo de sujeitos dos dados?
 * Testamos nosso conjunto de dados coletado ou curado para diversos vieses?
 * Podemos mitigar ou remover quaisquer vieses descobertos?

#### 2.7 Qualidade dos Dados

[Qualidade dos Dados](https://lakefs.io/data-quality-testing/) analisa a validade do conjunto de dados curado usado para desenvolver nossos algoritmos, verificando se os recursos e registros atendem aos requisitos para o nível de precisão e consistência necessários para nosso propósito de IA.

Questões a explorar aqui são:
 * Capturamos _recursos_ válidos para nosso caso de uso?
 * Os dados foram capturados _consistentemente_ em diversas fontes de dados?
 * O conjunto de dados está _completo_ para diversas condições ou cenários?
 * As informações capturadas refletem a realidade com _precisão_?

#### 2.8 Justiça nos Algoritmos
[Verificação de Justiça Algorítmica](https://towardsdatascience.com/what-is-algorithm-fairness-3182e161cf9f) analisa se o design do algoritmo discrimina sistematicamente subgrupos específicos de sujeitos de dados, levando a [potenciais danos](https://docs.microsoft.com/en-us/azure/machine-learning/concept-fairness-ml) na _alocação_ (onde recursos são negados ou retidos desse grupo) e na _qualidade do serviço_ (onde a IA não é tão precisa para alguns subgrupos quanto é para outros).

Perguntas para explorar aqui são:
 * Avaliamos a precisão do modelo para diversos subgrupos e condições?
 * Examinamos o sistema para potenciais danos (por exemplo, estereotipagem)?
 * Podemos revisar os dados ou re-treinar os modelos para mitigar os danos identificados?

Explore recursos como [checklists de Justiça em IA](https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RE4t6dA) para aprender mais.

#### 2.9 Representação Errada

[Representação Errada de Dados](https://www.sciencedirect.com/topics/computer-science/misrepresentation) trata de perguntar se estamos comunicando insights de dados relatados honestamente de maneira enganosa para apoiar uma narrativa desejada.

Perguntas para explorar aqui são:
 * Estamos relatando dados incompletos ou imprecisos?
 * Estamos visualizando dados de maneira que induza conclusões enganosas?
 * Estamos usando técnicas estatísticas seletivas para manipular resultados?
 * Existem explicações alternativas que podem oferecer uma conclusão diferente?

#### 2.10 Livre Escolha
A [Ilusão de Livre Escolha](https://www.datasciencecentral.com/profiles/blogs/the-illusion-of-choice) ocorre quando "arquiteturas de escolha" do sistema usam algoritmos de tomada de decisão para influenciar pessoas a tomarem um resultado preferido, enquanto aparentam dar opções e controle. Esses [padrões obscuros](https://www.darkpatterns.org/) podem causar danos sociais e econômicos aos usuários. Como as decisões dos usuários impactam perfis de comportamento, essas ações potencialmente impulsionam escolhas futuras que podem amplificar ou estender o impacto desses danos.

Perguntas para explorar aqui são:
 * O usuário entendeu as implicações de fazer essa escolha?
 * O usuário estava ciente das escolhas (alternativas) e dos prós e contras de cada uma?
 * O usuário pode reverter uma escolha automatizada ou influenciada posteriormente?

### 3. Estudos de Caso

Para colocar esses desafios éticos em contextos do mundo real, é útil olhar para estudos de caso que destacam os potenciais danos e consequências para indivíduos e a sociedade, quando essas violações éticas são ignoradas.

Aqui estão alguns exemplos:

| Desafio Ético | Estudo de Caso  | 
|--- |--- |
| **Consentimento Informado** | 1972 - [Estudo de Sífilis de Tuskegee](https://en.wikipedia.org/wiki/Tuskegee_Syphilis_Study) - Homens afro-americanos que participaram do estudo foram prometidos cuidados médicos gratuitos, _mas foram enganados_ por pesquisadores que não informaram os sujeitos sobre seu diagnóstico ou sobre a disponibilidade de tratamento. Muitos morreram e parceiros ou filhos foram afetados; o estudo durou 40 anos. | 
| **Privacidade de Dados** |  2007 - O [prêmio de dados da Netflix](https://www.wired.com/2007/12/why-anonymous-data-sometimes-isnt/) forneceu aos pesquisadores _10 milhões de classificações de filmes anonimizadas de 50 mil clientes_ para ajudar a melhorar algoritmos de recomendação. No entanto, os pesquisadores conseguiram correlacionar dados anonimizados com dados pessoalmente identificáveis em _conjuntos de dados externos_ (por exemplo, comentários no IMDb) - efetivamente "desanonimizando" alguns assinantes da Netflix.|
| **Viés na Coleta**  | 2013 - A cidade de Boston [desenvolveu o Street Bump](https://www.boston.gov/transportation/street-bump), um aplicativo que permitia aos cidadãos reportar buracos, fornecendo à cidade melhores dados sobre as estradas para encontrar e corrigir problemas. No entanto, [pessoas de grupos de baixa renda tinham menos acesso a carros e telefones](https://hbr.org/2013/04/the-hidden-biases-in-big-data), tornando seus problemas nas estradas invisíveis no aplicativo. Os desenvolvedores trabalharam com acadêmicos para abordar questões de _acesso equitativo e divisões digitais_ para justiça. |
| **Justiça Algorítmica**  | 2018 - O MIT [Estudo Gender Shades](http://gendershades.org/overview.html) avaliou a precisão de produtos de IA de classificação de gênero, expondo lacunas na precisão para mulheres e pessoas de cor. Um [Apple Card de 2019](https://www.wired.com/story/the-apple-card-didnt-see-genderand-thats-the-problem/) parecia oferecer menos crédito para mulheres do que para homens. Ambos ilustraram problemas de viés algorítmico levando a danos socioeconômicos.|
| **Representação Errada de Dados** | 2020 - O [Departamento de Saúde Pública da Geórgia divulgou gráficos de COVID-19](https://www.vox.com/covid-19-coronavirus-us-response-trump/2020/5/18/21262265/georgia-covid-19-cases-declining-reopening) que pareciam enganar os cidadãos sobre tendências de casos confirmados com ordenação não cronológica no eixo x. Isso ilustra representação errada por meio de truques de visualização. |
| **Ilusão de Livre Escolha** | 2020 - O aplicativo de aprendizado [ABCmouse pagou $10 milhões para resolver uma reclamação da FTC](https://www.washingtonpost.com/business/2020/09/04/abcmouse-10-million-ftc-settlement/) onde os pais foram presos em assinaturas que não podiam cancelar. Isso ilustra padrões obscuros em arquiteturas de escolha, onde os usuários foram influenciados a fazer escolhas potencialmente prejudiciais. |
| **Privacidade de Dados e Direitos do Usuário** | 2021 - O [Vazamento de Dados do Facebook](https://www.npr.org/2021/04/09/986005820/after-data-breach-exposes-530-million-facebook-says-it-will-not-notify-users) expôs dados de 530 milhões de usuários, resultando em um acordo de $5 bilhões com a FTC. No entanto, a empresa se recusou a notificar os usuários sobre o vazamento, violando os direitos dos usuários em relação à transparência e acesso aos dados. |

Quer explorar mais estudos de caso? Confira esses recursos:
* [Ethics Unwrapped](https://ethicsunwrapped.utexas.edu/case-studies) - dilemas éticos em diversas indústrias. 
* [Curso de Ética em Ciência de Dados](https://www.coursera.org/learn/data-science-ethics#syllabus) - estudos de caso marcantes explorados.
* [Onde as coisas deram errado](https://deon.drivendata.org/examples/) - checklist de Deon com exemplos.

> 🚨 Pense nos estudos de caso que você viu - você já experimentou ou foi afetado por um desafio ético semelhante em sua vida? Consegue pensar em pelo menos um outro estudo de caso que ilustre um dos desafios éticos discutidos nesta seção?

## Ética Aplicada

Falamos sobre conceitos éticos, desafios e estudos de caso em contextos do mundo real. Mas como começar a _aplicar_ princípios e práticas éticas em nossos projetos? E como _operacionalizar_ essas práticas para uma melhor governança? Vamos explorar algumas soluções do mundo real:

### 1. Códigos Profissionais

Códigos Profissionais oferecem uma opção para organizações "incentivarem" membros a apoiar seus princípios éticos e declaração de missão. Códigos são _diretrizes morais_ para comportamento profissional, ajudando funcionários ou membros a tomar decisões que estejam alinhadas com os princípios da organização. Eles são tão bons quanto a conformidade voluntária dos membros; no entanto, muitas organizações oferecem recompensas e penalidades adicionais para motivar a conformidade.

Exemplos incluem:

 * [Oxford Munich](http://www.code-of-ethics.org/code-of-conduct/) Código de Ética
 * [Data Science Association](http://datascienceassn.org/code-of-conduct.html) Código de Conduta (criado em 2013)
 * [ACM Código de Ética e Conduta Profissional](https://www.acm.org/code-of-ethics) (desde 1993)

> 🚨 Você pertence a uma organização profissional de engenharia ou ciência de dados? Explore o site deles para ver se definem um código de ética profissional. O que isso diz sobre seus princípios éticos? Como estão "incentivando" os membros a seguir o código?

### 2. Checklists de Ética

Enquanto os códigos profissionais definem o _comportamento ético_ exigido dos profissionais, eles [têm limitações conhecidas](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md) na aplicação, particularmente em projetos de grande escala. Em vez disso, muitos especialistas em ciência de dados [defendem checklists](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md), que podem **conectar princípios a práticas** de maneiras mais determinísticas e acionáveis.

Checklists convertem perguntas em tarefas "sim/não" que podem ser operacionalizadas, permitindo que sejam rastreadas como parte dos fluxos de trabalho padrão de lançamento de produtos.

Exemplos incluem:
 * [Deon](https://deon.drivendata.org/) - um checklist de ética em dados de uso geral criado a partir de [recomendações da indústria](https://deon.drivendata.org/#checklist-citations) com uma ferramenta de linha de comando para fácil integração.
 * [Checklist de Auditoria de Privacidade](https://cyber.harvard.edu/ecommerce/privacyaudit.html) - fornece orientação geral para práticas de manuseio de informações sob perspectivas legais e sociais.
 * [Checklist de Justiça em IA](https://www.microsoft.com/en-us/research/project/ai-fairness-checklist/) - criado por profissionais de IA para apoiar a adoção e integração de verificações de justiça nos ciclos de desenvolvimento de IA.
 * [22 perguntas para ética em dados e IA](https://medium.com/the-organization/22-questions-for-ethics-in-data-and-ai-efb68fd19429) - estrutura mais aberta, estruturada para exploração inicial de questões éticas em design, implementação e contextos organizacionais.

### 3. Regulamentações Éticas

Ética trata de definir valores compartilhados e fazer a coisa certa _voluntariamente_. **Conformidade** trata de _seguir a lei_ onde definida. **Governança** cobre amplamente todas as formas pelas quais as organizações operam para aplicar princípios éticos e cumprir leis estabelecidas.

Hoje, a governança assume duas formas dentro das organizações. Primeiro, trata-se de definir princípios de **IA ética** e estabelecer práticas para operacionalizar a adoção em todos os projetos relacionados à IA na organização. Segundo, trata-se de cumprir todas as regulamentações de **proteção de dados** exigidas pelo governo nas regiões em que opera.

Exemplos de regulamentações de proteção e privacidade de dados:

 * `1974`, [Lei de Privacidade dos EUA](https://www.justice.gov/opcl/privacy-act-1974) - regula a coleta, uso e divulgação de informações pessoais pelo _governo federal_.
 * `1996`, [Lei de Portabilidade e Responsabilidade de Seguro de Saúde dos EUA (HIPAA)](https://www.cdc.gov/phlp/publications/topic/hipaa.html) - protege dados pessoais de saúde.
 * `1998`, [Lei de Proteção à Privacidade Online das Crianças dos EUA (COPPA)](https://www.ftc.gov/enforcement/rules/rulemaking-regulatory-reform-proceedings/childrens-online-privacy-protection-rule) - protege a privacidade de dados de crianças menores de 13 anos.
 * `2018`, [Regulamento Geral de Proteção de Dados (GDPR)](https://gdpr-info.eu/) - fornece direitos aos usuários, proteção de dados e privacidade.
 * `2018`, [Lei de Privacidade do Consumidor da Califórnia (CCPA)](https://www.oag.ca.gov/privacy/ccpa) - dá aos consumidores mais _direitos_ sobre seus dados pessoais.
 * `2021`, [Lei de Proteção de Informações Pessoais da China](https://www.reuters.com/world/china/china-passes-new-personal-data-privacy-law-take-effect-nov-1-2021-08-20/) - recentemente aprovada, criando uma das regulamentações de privacidade de dados online mais fortes do mundo.

> 🚨 A União Europeia definiu o GDPR (Regulamento Geral de Proteção de Dados), que continua sendo uma das regulamentações de privacidade de dados mais influentes hoje. Você sabia que ele também define [8 direitos dos usuários](https://www.freeprivacypolicy.com/blog/8-user-rights-gdpr) para proteger a privacidade digital e os dados pessoais dos cidadãos? Aprenda quais são esses direitos e por que eles são importantes.

### 4. Cultura Ética

Note que ainda existe uma lacuna intangível entre _conformidade_ (fazer o suficiente para atender "à letra da lei") e abordar [questões sistêmicas](https://www.coursera.org/learn/data-science-ethics/home/week/4) (como ossificação, assimetria de informações e injustiça distributiva) que podem acelerar a armação da IA.

O último requer [abordagens colaborativas para definir culturas éticas](https://towardsdatascience.com/why-ai-ethics-requires-a-culture-driven-approach-26f451afa29f) que construam conexões emocionais e valores compartilhados consistentes _entre organizações_ na indústria. Isso exige mais [culturas éticas formalizadas de dados](https://www.codeforamerica.org/news/formalizing-an-ethical-data-culture/) nas organizações - permitindo que _qualquer pessoa_ [puxe o cordão Andon](https://en.wikipedia.org/wiki/Andon_(manufacturing)) (para levantar preocupações éticas cedo no processo) e tornando _avaliações éticas_ (por exemplo, na contratação) um critério central na formação de equipes em projetos de IA.

---
## [Quiz pós-aula](https://ff-quizzes.netlify.app/en/ds/quiz/3) 🎯
## Revisão e Autoestudo 

Cursos e livros ajudam a entender conceitos éticos fundamentais e desafios, enquanto estudos de caso e ferramentas ajudam com práticas éticas aplicadas em contextos do mundo real. Aqui estão alguns recursos para começar:

* [Machine Learning For Beginners](https://github.com/microsoft/ML-For-Beginners/blob/main/1-Introduction/3-fairness/README.md) - lição sobre Justiça, da Microsoft.
* [Princípios de IA Responsável](https://docs.microsoft.com/en-us/learn/modules/responsible-ai-principles/) - trilha de aprendizado gratuita do Microsoft Learn.  
* [Ética e Ciência de Dados](https://resources.oreilly.com/examples/0636920203964) - EBook da O'Reilly (M. Loukides, H. Mason et. al)  
* [Ética na Ciência de Dados](https://www.coursera.org/learn/data-science-ethics#syllabus) - curso online da Universidade de Michigan.  
* [Ética Desvendada](https://ethicsunwrapped.utexas.edu/case-studies) - estudos de caso da Universidade do Texas.  

# Tarefa  

[Escreva um Estudo de Caso sobre Ética de Dados](assignment.md)  

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.