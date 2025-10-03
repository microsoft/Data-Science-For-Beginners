<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "58860ce9a4b8a564003d2752f7c72851",
  "translation_date": "2025-10-03T16:24:25+00:00",
  "source_file": "1-Introduction/02-ethics/README.md",
  "language_code": "pt"
}
-->
# Introdução à Ética de Dados

|![ Sketchnote por [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/02-Ethics.png)|
|:---:|
| Ética em Ciência de Dados - _Sketchnote por [@nitya](https://twitter.com/nitya)_ |

---

Somos todos cidadãos de dados a viver num mundo dataficado.

As tendências de mercado indicam que, até 2022, 1 em cada 3 grandes organizações comprará e venderá os seus dados através de [Mercados e Bolsas](https://www.gartner.com/smarterwithgartner/gartner-top-10-trends-in-data-and-analytics-for-2020/) online. Como **Desenvolvedores de Aplicações**, será mais fácil e barato integrar insights baseados em dados e automação orientada por algoritmos nas experiências diárias dos utilizadores. Mas, à medida que a IA se torna omnipresente, também será necessário compreender os potenciais danos causados pela [armamentização](https://www.youtube.com/watch?v=TQHs8SA1qpk) desses algoritmos em larga escala.

As tendências sugerem que, até 2025, iremos gerar e consumir mais de [180 zettabytes](https://www.statista.com/statistics/871513/worldwide-data-created/) de dados. Para **Cientistas de Dados**, esta explosão de informação oferece acesso sem precedentes a dados pessoais e comportamentais. Com isso, surge o poder de construir perfis detalhados de utilizadores e influenciar subtilmente a tomada de decisões—frequentemente de formas que promovem uma [ilusão de escolha livre](https://www.datasciencecentral.com/the-pareto-set-and-the-paradox-of-choice/). Embora isso possa ser usado para orientar os utilizadores em direção a resultados preferidos, também levanta questões críticas sobre privacidade de dados, autonomia e os limites éticos da influência algorítmica.

A ética de dados é agora _uma barreira necessária_ para a ciência e engenharia de dados, ajudando-nos a minimizar potenciais danos e consequências não intencionais das nossas ações orientadas por dados. O [Ciclo de Hype da Gartner para IA](https://www.gartner.com/smarterwithgartner/2-megatrends-dominate-the-gartner-hype-cycle-for-artificial-intelligence-2020/) identifica tendências relevantes em ética digital, IA responsável e governança de IA como motores-chave para megatendências maiores em torno da _democratização_ e _industrialização_ da IA.

![Ciclo de Hype da Gartner para IA - 2020](https://images-cdn.newscred.com/Zz1mOWJhNzlkNDA2ZTMxMWViYjRiOGFiM2IyMjQ1YmMwZQ==)

Nesta lição, exploraremos a área fascinante da ética de dados - desde conceitos e desafios fundamentais até estudos de caso e conceitos aplicados de IA, como governança - que ajudam a estabelecer uma cultura de ética em equipas e organizações que trabalham com dados e IA.

## [Questionário pré-aula](https://ff-quizzes.netlify.app/en/ds/quiz/2) 🎯

## Definições Básicas

Vamos começar por compreender a terminologia básica.

A palavra "ética" vem da [palavra grega "ethikos"](https://en.wikipedia.org/wiki/Ethics) (e sua raiz "ethos"), que significa _caráter ou natureza moral_.

**Ética** refere-se aos valores partilhados e princípios morais que governam o nosso comportamento na sociedade. A ética não se baseia em leis, mas em normas amplamente aceites sobre o que é "certo vs. errado". No entanto, considerações éticas podem influenciar iniciativas de governança corporativa e regulamentações governamentais que criam mais incentivos para conformidade.

**Ética de Dados** é um [novo ramo da ética](https://royalsocietypublishing.org/doi/full/10.1098/rsta.2016.0360#sec-1) que "estuda e avalia problemas morais relacionados a _dados, algoritmos e práticas correspondentes_". Aqui, **"dados"** foca-se em ações relacionadas à geração, gravação, curadoria, processamento, disseminação, partilha e uso; **"algoritmos"** foca-se em IA, agentes, aprendizagem automática e robôs; e **"práticas"** foca-se em tópicos como inovação responsável, programação, hacking e códigos de ética.

**Ética Aplicada** é a [aplicação prática de considerações morais](https://en.wikipedia.org/wiki/Applied_ethics). Trata-se do processo de investigar ativamente questões éticas no contexto de _ações, produtos e processos do mundo real_, e tomar medidas corretivas para garantir que permaneçam alinhados com os nossos valores éticos definidos.

**Cultura de Ética** refere-se a [_operacionalizar_ a ética aplicada](https://hbr.org/2019/05/how-to-design-an-ethical-organization) para garantir que os nossos princípios e práticas éticos sejam adotados de forma consistente e escalável em toda a organização. Culturas de ética bem-sucedidas definem princípios éticos em toda a organização, oferecem incentivos significativos para conformidade e reforçam normas éticas ao encorajar e amplificar comportamentos desejados em todos os níveis da organização.

## Conceitos de Ética

Nesta secção, discutiremos conceitos como **valores partilhados** (princípios) e **desafios éticos** (problemas) para ética de dados - e exploraremos **estudos de caso** que ajudam a compreender esses conceitos em contextos do mundo real.

### 1. Princípios Éticos

Toda estratégia de ética de dados começa por definir _princípios éticos_ - os "valores partilhados" que descrevem comportamentos aceitáveis e orientam ações conformes nos nossos projetos de dados e IA. Pode-se defini-los a nível individual ou de equipa. No entanto, a maioria das grandes organizações delineia-os numa declaração de missão ou estrutura de _IA ética_ definida a nível corporativo e aplicada de forma consistente em todas as equipas.

**Exemplo:** A declaração de missão de [IA Responsável](https://www.microsoft.com/en-us/ai/responsible-ai) da Microsoft afirma: _"Estamos comprometidos com o avanço da IA orientada por princípios éticos que colocam as pessoas em primeiro lugar"_ - identificando 6 princípios éticos na estrutura abaixo:

![IA Responsável na Microsoft](https://docs.microsoft.com/en-gb/azure/cognitive-services/personalizer/media/ethics-and-responsible-use/ai-values-future-computed.png)

Vamos explorar brevemente esses princípios. _Transparência_ e _responsabilidade_ são valores fundamentais sobre os quais outros princípios se constroem - então vamos começar por aí:

* [**Responsabilidade**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) torna os profissionais _responsáveis_ pelas suas operações de dados e IA, e pela conformidade com esses princípios éticos.
* [**Transparência**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) garante que as ações de dados e IA sejam _compreensíveis_ (interpretáveis) para os utilizadores, explicando o quê e o porquê por trás das decisões.
* [**Justiça**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1%3aprimaryr6) - foca-se em garantir que a IA trate _todas as pessoas_ de forma justa, abordando quaisquer preconceitos socio-técnicos sistémicos ou implícitos nos dados e sistemas.
* [**Fiabilidade e Segurança**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) - garante que a IA se comporte de forma _consistente_ com os valores definidos, minimizando potenciais danos ou consequências não intencionais.
* [**Privacidade e Segurança**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) - trata de compreender a linhagem dos dados e fornecer _privacidade de dados e proteções relacionadas_ aos utilizadores.
* [**Inclusividade**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) - trata de projetar soluções de IA com intenção, adaptando-as para atender a uma _ampla gama de necessidades e capacidades humanas_.

> 🚨 Pense no que poderia ser a sua declaração de missão de ética de dados. Explore estruturas de IA ética de outras organizações - aqui estão exemplos da [IBM](https://www.ibm.com/cloud/learn/ai-ethics), [Google](https://ai.google/principles) e [Facebook](https://ai.facebook.com/blog/facebooks-five-pillars-of-responsible-ai/). Que valores partilhados têm em comum? Como esses princípios se relacionam com o produto ou indústria de IA em que operam?

### 2. Desafios Éticos

Depois de definir os princípios éticos, o próximo passo é avaliar as nossas ações de dados e IA para ver se estão alinhadas com esses valores partilhados. Pense nas suas ações em duas categorias: _coleta de dados_ e _design de algoritmos_.

Na coleta de dados, as ações provavelmente envolverão **dados pessoais** ou informações pessoalmente identificáveis (PII) de indivíduos identificáveis. Isso inclui [diversos itens de dados não pessoais](https://ec.europa.eu/info/law/law-topic/data-protection/reform/what-personal-data_en) que, _coletivamente_, identificam um indivíduo. Os desafios éticos podem estar relacionados à _privacidade de dados_, _propriedade de dados_ e tópicos relacionados, como _consentimento informado_ e _direitos de propriedade intelectual_ dos utilizadores.

No design de algoritmos, as ações envolverão a coleta e curadoria de **conjuntos de dados**, e o uso desses dados para treinar e implementar **modelos de dados** que preveem resultados ou automatizam decisões em contextos do mundo real. Os desafios éticos podem surgir de _viés nos conjuntos de dados_, problemas de _qualidade dos dados_, _injustiça_ e _má representação_ nos algoritmos - incluindo alguns problemas que são sistémicos por natureza.

Em ambos os casos, os desafios éticos destacam áreas onde as nossas ações podem entrar em conflito com os nossos valores partilhados. Para detetar, mitigar, minimizar ou eliminar essas preocupações, precisamos fazer perguntas morais de "sim/não" relacionadas às nossas ações e tomar medidas corretivas conforme necessário. Vamos analisar alguns desafios éticos e as questões morais que eles levantam:

#### 2.1 Propriedade de Dados

A coleta de dados frequentemente envolve dados pessoais que podem identificar os sujeitos dos dados. [Propriedade de dados](https://permission.io/blog/data-ownership) trata do _controlo_ e [_direitos dos utilizadores_](https://permission.io/blog/data-ownership) relacionados à criação, processamento e disseminação de dados.

As questões morais que precisamos perguntar são:
 * Quem é o proprietário dos dados? (utilizador ou organização)
 * Que direitos têm os sujeitos dos dados? (ex: acesso, eliminação, portabilidade)
 * Que direitos têm as organizações? (ex: retificar avaliações maliciosas de utilizadores)

#### 2.2 Consentimento Informado

[Consentimento informado](https://legaldictionary.net/informed-consent/) define o ato de os utilizadores concordarem com uma ação (como coleta de dados) com um _entendimento completo_ dos factos relevantes, incluindo o propósito, os riscos potenciais e as alternativas.

Questões a explorar aqui são:
 * O utilizador (sujeito dos dados) deu permissão para a captura e uso dos dados?
 * O utilizador compreendeu o propósito para o qual os dados foram capturados?
 * O utilizador compreendeu os riscos potenciais da sua participação?

#### 2.3 Propriedade Intelectual

[Propriedade intelectual](https://en.wikipedia.org/wiki/Intellectual_property) refere-se a criações intangíveis resultantes da iniciativa humana, que podem _ter valor económico_ para indivíduos ou empresas.

Questões a explorar aqui são:
 * Os dados coletados têm valor económico para um utilizador ou empresa?
 * O **utilizador** tem propriedade intelectual aqui?
 * A **organização** tem propriedade intelectual aqui?
 * Se esses direitos existem, como estamos a protegê-los?

#### 2.4 Privacidade de Dados

[Privacidade de dados](https://www.northeastern.edu/graduate/blog/what-is-data-privacy/) ou privacidade de informações refere-se à preservação da privacidade do utilizador e proteção da identidade do utilizador em relação a informações pessoalmente identificáveis.

Questões a explorar aqui são:
 * Os dados (pessoais) dos utilizadores estão protegidos contra ataques e vazamentos?
 * Os dados dos utilizadores estão acessíveis apenas a utilizadores e contextos autorizados?
 * A anonimidade dos utilizadores é preservada quando os dados são partilhados ou disseminados?
 * Um utilizador pode ser desidentificado de conjuntos de dados anonimizados?

#### 2.5 Direito ao Esquecimento

O [Direito ao Esquecimento](https://en.wikipedia.org/wiki/Right_to_be_forgotten) ou [Direito à Eliminação](https://www.gdpreu.org/right-to-be-forgotten/) oferece proteção adicional de dados pessoais aos utilizadores. Especificamente, dá aos utilizadores o direito de solicitar a eliminação ou remoção de dados pessoais de pesquisas na Internet e outros locais, _sob circunstâncias específicas_ - permitindo-lhes um novo começo online sem que ações passadas sejam usadas contra eles.

Questões a explorar aqui são:
 * O sistema permite que os sujeitos dos dados solicitem a eliminação?
 * A retirada do consentimento do utilizador deve acionar a eliminação automática?
 * Os dados foram coletados sem consentimento ou por meios ilegais?
 * Estamos em conformidade com as regulamentações governamentais de privacidade de dados?

#### 2.6 Viés nos Conjuntos de Dados

Viés nos conjuntos de dados ou [Viés de Coleta](http://researcharticles.com/index.php/bias-in-data-collection-in-research/) refere-se à seleção de um subconjunto _não representativo_ de dados para o desenvolvimento de algoritmos, criando potencial injustiça nos resultados para grupos diversos. Tipos de viés incluem viés de seleção ou amostragem, viés de voluntariado e viés de instrumento.

Questões a explorar aqui são:
 * Recrutámos um conjunto representativo de sujeitos dos dados?
 * Testámos o nosso conjunto de dados coletado ou curado para vários tipos de viés?
 * Podemos mitigar ou remover quaisquer vieses descobertos?

#### 2.7 Qualidade dos Dados

[Qualidade dos Dados](https://lakefs.io/data-quality-testing/) analisa a validade do conjunto de dados curado usado para desenvolver os nossos algoritmos, verificando se as características e os registos atendem aos requisitos para o nível de precisão e consistência necessário para o nosso propósito de IA.

Questões a explorar aqui são:
 * Capturámos características válidas para o nosso caso de uso?
 * Os dados foram capturados de forma _consistente_ em diversas fontes de dados?
 * O conjunto de dados está _completo_ para condições ou cenários diversos?
* A informação foi capturada _com precisão_ ao refletir a realidade?

#### 2.8 Justiça dos Algoritmos

[A Justiça dos Algoritmos](https://towardsdatascience.com/what-is-algorithm-fairness-3182e161cf9f) verifica se o design do algoritmo discrimina sistematicamente subgrupos específicos de sujeitos de dados, levando a [potenciais danos](https://docs.microsoft.com/en-us/azure/machine-learning/concept-fairness-ml) na _distribuição_ (onde recursos são negados ou retidos desse grupo) e na _qualidade do serviço_ (onde a IA não é tão precisa para alguns subgrupos como é para outros).

Perguntas a explorar aqui incluem:
* Avaliámos a precisão do modelo para diversos subgrupos e condições?
* Examinámos o sistema para identificar potenciais danos (por exemplo, estereótipos)?
* Podemos rever os dados ou re-treinar os modelos para mitigar os danos identificados?

Explore recursos como [checklists de Justiça na IA](https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RE4t6dA) para saber mais.

#### 2.9 Deturpação

[A Deturpação de Dados](https://www.sciencedirect.com/topics/computer-science/misrepresentation) trata de questionar se estamos a comunicar insights de dados relatados honestamente de forma enganosa para apoiar uma narrativa desejada.

Perguntas a explorar aqui incluem:
* Estamos a relatar dados incompletos ou imprecisos?
* Estamos a visualizar dados de forma a induzir conclusões enganosas?
* Estamos a usar técnicas estatísticas seletivas para manipular resultados?
* Existem explicações alternativas que possam oferecer uma conclusão diferente?

#### 2.10 Livre Escolha

A [Ilusão de Livre Escolha](https://www.datasciencecentral.com/profiles/blogs/the-illusion-of-choice) ocorre quando "arquiteturas de escolha" do sistema utilizam algoritmos de tomada de decisão para influenciar as pessoas a tomarem um resultado preferido, enquanto aparentam dar-lhes opções e controlo. Estes [padrões obscuros](https://www.darkpatterns.org/) podem causar danos sociais e económicos aos utilizadores. Como as decisões dos utilizadores impactam os perfis de comportamento, estas ações podem potencialmente impulsionar escolhas futuras que amplificam ou prolongam o impacto desses danos.

Perguntas a explorar aqui incluem:
* O utilizador compreendeu as implicações de fazer essa escolha?
* O utilizador estava ciente de (alternativas) escolhas e dos prós e contras de cada uma?
* O utilizador pode reverter uma escolha automatizada ou influenciada posteriormente?

### 3. Estudos de Caso

Para colocar estes desafios éticos em contextos do mundo real, é útil analisar estudos de caso que destacam os potenciais danos e consequências para indivíduos e para a sociedade, quando estas violações éticas são ignoradas.

Aqui estão alguns exemplos:

| Desafio Ético | Estudo de Caso | 
|--- |--- |
| **Consentimento Informado** | 1972 - [Estudo de Sífilis de Tuskegee](https://en.wikipedia.org/wiki/Tuskegee_Syphilis_Study) - Homens afro-americanos que participaram no estudo foram prometidos cuidados médicos gratuitos _mas enganados_ por investigadores que não informaram os sujeitos sobre o seu diagnóstico ou sobre a disponibilidade de tratamento. Muitos sujeitos morreram e parceiros ou filhos foram afetados; o estudo durou 40 anos. | 
| **Privacidade de Dados** | 2007 - O [prémio de dados da Netflix](https://www.wired.com/2007/12/why-anonymous-data-sometimes-isnt/) forneceu aos investigadores _10M classificações de filmes anonimizadas de 50K clientes_ para ajudar a melhorar os algoritmos de recomendação. No entanto, os investigadores conseguiram correlacionar dados anonimizados com dados pessoalmente identificáveis em _conjuntos de dados externos_ (por exemplo, comentários no IMDb) - efetivamente "desanonimizando" alguns assinantes da Netflix. |
| **Viés na Coleta de Dados** | 2013 - A cidade de Boston [desenvolveu Street Bump](https://www.boston.gov/transportation/street-bump), uma aplicação que permitia aos cidadãos reportar buracos na estrada, dando à cidade melhores dados sobre vias para encontrar e resolver problemas. No entanto, [pessoas em grupos de rendimentos mais baixos tinham menos acesso a carros e telemóveis](https://hbr.org/2013/04/the-hidden-biases-in-big-data), tornando os seus problemas de vias invisíveis nesta aplicação. Os desenvolvedores trabalharam com académicos para abordar questões de _acesso equitativo e divisões digitais_ para garantir justiça. |
| **Justiça Algorítmica** | 2018 - O MIT [Estudo Gender Shades](http://gendershades.org/overview.html) avaliou a precisão de produtos de IA de classificação de género, expondo lacunas na precisão para mulheres e pessoas de cor. Um [Cartão Apple de 2019](https://www.wired.com/story/the-apple-card-didnt-see-genderand-thats-the-problem/) parecia oferecer menos crédito às mulheres do que aos homens. Ambos ilustraram problemas de viés algorítmico que levam a danos socioeconómicos. |
| **Deturpação de Dados** | 2020 - O [Departamento de Saúde Pública da Geórgia divulgou gráficos de COVID-19](https://www.vox.com/covid-19-coronavirus-us-response-trump/2020/5/18/21262265/georgia-covid-19-cases-declining-reopening) que pareciam enganar os cidadãos sobre tendências de casos confirmados com ordenação não cronológica no eixo x. Isto ilustra deturpação através de truques de visualização. |
| **Ilusão de Livre Escolha** | 2020 - A aplicação de aprendizagem [ABCmouse pagou $10M para resolver uma queixa da FTC](https://www.washingtonpost.com/business/2020/09/04/abcmouse-10-million-ftc-settlement/) onde os pais ficaram presos a pagar por subscrições que não podiam cancelar. Isto ilustra padrões obscuros em arquiteturas de escolha, onde os utilizadores foram influenciados a tomar escolhas potencialmente prejudiciais. |
| **Privacidade de Dados e Direitos dos Utilizadores** | 2021 - A [Violação de Dados do Facebook](https://www.npr.org/2021/04/09/986005820/after-data-breach-exposes-530-million-facebook-says-it-will-not-notify-users) expôs dados de 530M utilizadores, resultando num acordo de $5B com a FTC. No entanto, recusou-se a notificar os utilizadores sobre a violação, violando os direitos dos utilizadores em relação à transparência e ao acesso aos dados. |

Quer explorar mais estudos de caso? Veja estes recursos:
* [Ethics Unwrapped](https://ethicsunwrapped.utexas.edu/case-studies) - dilemas éticos em diversas indústrias. 
* [Curso de Ética em Ciência de Dados](https://www.coursera.org/learn/data-science-ethics#syllabus) - estudos de caso marcantes explorados.
* [Onde as coisas correram mal](https://deon.drivendata.org/examples/) - checklist de Deon com exemplos.

> 🚨 Pense nos estudos de caso que viu - já experienciou ou foi afetado por um desafio ético semelhante na sua vida? Consegue pensar em pelo menos um outro estudo de caso que ilustre um dos desafios éticos discutidos nesta secção?

## Ética Aplicada

Falámos sobre conceitos éticos, desafios e estudos de caso em contextos do mundo real. Mas como começamos a _aplicar_ princípios e práticas éticas nos nossos projetos? E como _operacionalizamos_ estas práticas para uma melhor governança? Vamos explorar algumas soluções do mundo real:

### 1. Códigos Profissionais

Os Códigos Profissionais oferecem uma opção para as organizações "incentivarem" os membros a apoiar os seus princípios éticos e declaração de missão. Os códigos são _diretrizes morais_ para o comportamento profissional, ajudando os funcionários ou membros a tomar decisões que estejam alinhadas com os princípios da organização. Eles são tão eficazes quanto a conformidade voluntária dos membros; no entanto, muitas organizações oferecem recompensas e penalidades adicionais para motivar a conformidade dos membros.

Exemplos incluem:

* [Oxford Munich](http://www.code-of-ethics.org/code-of-conduct/) Código de Ética
* [Data Science Association](http://datascienceassn.org/code-of-conduct.html) Código de Conduta (criado em 2013)
* [ACM Código de Ética e Conduta Profissional](https://www.acm.org/code-of-ethics) (desde 1993)

> 🚨 Pertence a uma organização profissional de engenharia ou ciência de dados? Explore o site para ver se definem um código profissional de ética. O que isso diz sobre os seus princípios éticos? Como estão a "incentivar" os membros a seguir o código?

### 2. Checklists de Ética

Enquanto os códigos profissionais definem o comportamento ético _necessário_ dos profissionais, eles [têm limitações conhecidas](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md) na aplicação, particularmente em projetos de grande escala. Em vez disso, muitos especialistas em ciência de dados [defendem checklists](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md), que podem **conectar princípios a práticas** de forma mais determinística e acionável.

Os checklists convertem perguntas em tarefas "sim/não" que podem ser operacionalizadas, permitindo que sejam rastreadas como parte dos fluxos de trabalho padrão de lançamento de produtos.

Exemplos incluem:
* [Deon](https://deon.drivendata.org/) - um checklist de ética em dados de uso geral criado a partir de [recomendações da indústria](https://deon.drivendata.org/#checklist-citations) com uma ferramenta de linha de comando para fácil integração.
* [Checklist de Auditoria de Privacidade](https://cyber.harvard.edu/ecommerce/privacyaudit.html) - fornece orientações gerais para práticas de manuseio de informações sob perspetivas legais e sociais.
* [Checklist de Justiça na IA](https://www.microsoft.com/en-us/research/project/ai-fairness-checklist/) - criado por profissionais de IA para apoiar a adoção e integração de verificações de justiça nos ciclos de desenvolvimento de IA.
* [22 perguntas para ética em dados e IA](https://medium.com/the-organization/22-questions-for-ethics-in-data-and-ai-efb68fd19429) - estrutura mais aberta, organizada para exploração inicial de questões éticas no design, implementação e contextos organizacionais.

### 3. Regulamentações Éticas

A ética trata de definir valores compartilhados e fazer o que é certo _voluntariamente_. **Conformidade** trata de _seguir a lei_ onde e quando definida. **Governança** cobre amplamente todas as formas como as organizações operam para aplicar princípios éticos e cumprir leis estabelecidas.

Hoje, a governança assume duas formas dentro das organizações. Primeiro, trata-se de definir princípios de **IA ética** e estabelecer práticas para operacionalizar a adoção em todos os projetos relacionados à IA na organização. Segundo, trata-se de cumprir todas as regulamentações de **proteção de dados** mandatadas pelo governo nas regiões onde opera.

Exemplos de regulamentações de proteção de dados e privacidade:

* `1974`, [Lei de Privacidade dos EUA](https://www.justice.gov/opcl/privacy-act-1974) - regula a coleta, uso e divulgação de informações pessoais pelo _governo federal_.
* `1996`, [Lei de Portabilidade e Responsabilidade de Seguro de Saúde dos EUA (HIPAA)](https://www.cdc.gov/phlp/publications/topic/hipaa.html) - protege dados de saúde pessoais.
* `1998`, [Lei de Proteção à Privacidade Online das Crianças dos EUA (COPPA)](https://www.ftc.gov/enforcement/rules/rulemaking-regulatory-reform-proceedings/childrens-online-privacy-protection-rule) - protege a privacidade de dados de crianças menores de 13 anos.
* `2018`, [Regulamento Geral de Proteção de Dados (GDPR)](https://gdpr-info.eu/) - fornece direitos dos utilizadores, proteção de dados e privacidade.
* `2018`, [Lei de Privacidade do Consumidor da Califórnia (CCPA)](https://www.oag.ca.gov/privacy/ccpa) - dá aos consumidores mais _direitos_ sobre os seus dados pessoais.
* `2021`, [Lei de Proteção de Informações Pessoais da China](https://www.reuters.com/world/china/china-passes-new-personal-data-privacy-law-take-effect-nov-1-2021-08-20/) - recentemente aprovada, criando uma das regulamentações de privacidade de dados online mais fortes do mundo.

> 🚨 A União Europeia definiu o GDPR (Regulamento Geral de Proteção de Dados), que continua a ser uma das regulamentações de privacidade de dados mais influentes atualmente. Sabia que também define [8 direitos dos utilizadores](https://www.freeprivacypolicy.com/blog/8-user-rights-gdpr) para proteger a privacidade digital e os dados pessoais dos cidadãos? Descubra quais são e por que são importantes.

### 4. Cultura Ética

Note que permanece uma lacuna intangível entre _conformidade_ (fazer o suficiente para cumprir "a letra da lei") e abordar [questões sistémicas](https://www.coursera.org/learn/data-science-ethics/home/week/4) (como ossificação, assimetria de informação e injustiça distributiva) que podem acelerar a armação da IA.

A última exige [abordagens colaborativas para definir culturas éticas](https://towardsdatascience.com/why-ai-ethics-requires-a-culture-driven-approach-26f451afa29f) que construam conexões emocionais e valores compartilhados consistentes _entre organizações_ na indústria. Isto requer mais [culturas éticas formalizadas de dados](https://www.codeforamerica.org/news/formalizing-an-ethical-data-culture/) nas organizações - permitindo que _qualquer pessoa_ [puxe o cordão Andon](https://en.wikipedia.org/wiki/Andon_(manufacturing)) (para levantar preocupações éticas cedo no processo) e tornando as _avaliações éticas_ (por exemplo, na contratação) um critério central na formação de equipas em projetos de IA.

---
## [Questionário pós-aula](https://ff-quizzes.netlify.app/en/ds/quiz/3) 🎯
## Revisão e Autoestudo

Cursos e livros ajudam a compreender os conceitos e desafios éticos fundamentais, enquanto estudos de caso e ferramentas ajudam com práticas éticas aplicadas em contextos do mundo real. Aqui estão alguns recursos para começar.
* [Machine Learning Para Principiantes](https://github.com/microsoft/ML-For-Beginners/blob/main/1-Introduction/3-fairness/README.md) - aula sobre Justiça, da Microsoft.  
* [Princípios de IA Responsável](https://docs.microsoft.com/en-us/learn/modules/responsible-ai-principles/) - percurso de aprendizagem gratuito no Microsoft Learn.  
* [Ética e Ciência de Dados](https://resources.oreilly.com/examples/0636920203964) - EBook da O'Reilly (M. Loukides, H. Mason et. al)  
* [Ética na Ciência de Dados](https://www.coursera.org/learn/data-science-ethics#syllabus) - curso online da Universidade de Michigan.  
* [Ethics Unwrapped](https://ethicsunwrapped.utexas.edu/case-studies) - estudos de caso da Universidade do Texas.  

# Tarefa  

[Escrever Um Estudo de Caso Sobre Ética de Dados](assignment.md)  

---

**Aviso**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, é importante notar que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se uma tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.