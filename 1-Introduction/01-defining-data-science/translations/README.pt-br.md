# Definindo Ciências de Dados

|![ Sketchnote por [(@sketchthedocs)](https://sketchthedocs.dev) ](../../../sketchnotes/01-Definitions.png)|
|:---:|
|Definindo Ciências de Dados - _Sketchnote por [@nitya](https://twitter.com/nitya)_ |

---

[![Definindo Ciências de Dados](../images/video-def-ds.png)](https://youtu.be/pqqsm5reGvs)

## [Quiz pré-aula](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/0)

## O que são Dados?
Na nossa vida cotidiana, nós estamos constantemente cercados por dados. O texto que você está lendo agora é um dado, a lista de telefones dos seus amigos no seu celular é um dado, assim como o horário atual mostrado no seu relógio. Como seres humanos, nós operamos naturalmente com dados. contando o dinheiro que temos ou escrevendo cartas para os nossos amigos.

No entanto, os dados se tornaram muito mais críticos com a criação de computadores. O papel principal dos computadores é realizar computações, mas eles precisam de dados para operar sobre. Portanto, nós precisamos entender como os computadores armazenam e processam dados.

Com o surgimento da Internet, o papel dos computadores como dispositivos de manipulação de dados aumentou. Se você parar para pensar, agora nós usamos computadores cada vez mais para processamento de dados e comunicação, ao invés de cálculos reais. Quando escrevemos um e-mail para um amigo ou procuramos por alguma informação na Internet - nós estamos essencialmente criando, armazenando, transmitindo, e manipulando dados.
> Você consegue se lembrar da última vez que usou computadores para de fato computar algo?

## O que é Ciência de Dados?

Na [Wikipedia (PT-BR)](https://pt.wikipedia.org/wiki/Ci%C3%AAncia_de_dados), **Ciência de Dados** é definida como *uma área interdisciplinar voltada para o estudo e a análise de dados econômicos, financeiros e sociais, estruturados e não-estruturados, que visa a extração de conhecimento, detecção de padrões e/ou obtenção de insights para possíveis tomadas de decisão*.

Essa definição destaca os seguintes aspectos importantes da ciência de dados:

* O principal objetivo da ciência de dados é **extrair conhecimento** dos dados, em outras palavras - **entender** os dados, encontrar alguma relação escondida e construir um **modelo**.
* Ciência de dados utiliza **métodos científicos**, como probabilidade e estatística. Na verdade, quando o termo *ciência de dados* foi introduzido pela primeira vez, algumas pessoas argumentaram que ciência de dados é apenas um nome chique para estatística. Hoje em dia ficou mais evidente que esse campo é muito mais amplo.
* Conhecimento adquirido deve ser aplicado para produzir algum **insight para possível tomada de decisão**.
* Nós devemos ser capazes de operar tanto nos dados **estruturados** quanto nos **não estruturados**. Nós voltaremos a discutir diferentes tipos de dados mais para a frente no curso.
* **Domínio de aplicação** é um conceito importante, e cientistas de dados frequentemente precisam de pelo menos algum grau de perícia no domínio do problema.

> Outro importante aspecto da Ciência de Dados é que ela estuda como os dados podem ser coletados, armazenados e operados por meio de computadores. Enquanto estatística nos fornece fundações matemáticas, ciência de dados aplica conceitos matemáticos para de fato desenhar percepções a partir dos dados.

Uma das formas (atribuída a [Jim Gray](https://en.wikipedia.org/wiki/Jim_Gray_(computer_scientist))) para olhar para ciência de dados é considerar que ela é um paradigma separado da ciência:
* **Empírico**, onde nos baseamos majoritariamente nas observações e resultados dos experimentos
* **Teórico**, onde novos conceitos surgem a partir de conhecimentos cientificos já existentes
* **Computacional**, onde nós descobrimos novos princípios baseado em algum experimento computacional
* **Orientado por Dados**, baseado na descoberta de relações e padrões nos dados

## Outros Campos Relacionados

Já que dados são um conceito difundido, a ciência de dados em si também é um campo amplo, abrangendo muitas outras disciplinas relacionadas.

<dl>
<dt>Banco de Dados</dt>
<dd>
A coisa mais óbvia a considerar é **como armazenar** os dados, ex. como estruturá-los de uma forma que permite um processamento rápido. Existem diferentes tipos de banco de dados que armazenam dados estruturados e não estruturados, que <a href="../../../2-Working-With-Data/README.md">nós vamos considerar nesse curso</a>.
</dd>
<dt>Big Data</dt>
<dd>
Frequentemente precisamos armazenar e processar quantidades muito grandes de dados com estruturas relativamente simples. Existem algumas abordagens e ferramentas especiais para armazenar esses dados de uma forma distribuída em um cluster de computer, e processá-los de forma eficiente.
</dd>
<dt>Aprendizado de Máquina</dt>
<dd>
Uma das maneiras de entender dados é **construir um modelo** que será capaz de predizer o resultado esperado. Ser capaz de aprender esses modelos a partir de dados é a área estudada em **aprendizado de máquina**. Você talvez queira olhar o nosso Currículo de <a href="https://aka.ms/ml-beginners">Aprendizado de Máquina para Iniciantes</a> para ir mais a fundo nessa área.
</dd>
<dt>Inteligência Artificial</dt>
<dd>
Como aprendizado de máquina, inteligência artificial também se baseia em dados, e envolve construir modelos de alta complexidade que irão exibir um comportamento similar ao dos seres humanos. Além disso, métodos de IA frequentemente nos permite transformar dados não estruturados (ex. linguagem natural) em dados estruturados extraindo algumas percepções.
</dd>
<dt>Visualização</dt>
<dd>
Vastas quantidades de dados são incompreensíveis para o ser humano, mas uma vez que criamos visualizações úteis - nós podemos começar a dar muito mais sentido aos dados, e desenhar algumas conclusões. Portanto, é importante conhecer várias formas de visualizar informação - algo que vamos cobrir na <a href="../../../3-Data-Visualization/README.md">Seção 3</a> do nosso curso. Áreas relacionadas também incluem **Infográficos**, e **Interação Humano-Computador** no geral.
</dd>
</dl>

## Tipos de Dados

Como nós já mencionamos - dados estão em todos os lugares, nós só precisamos coletá-los da maneira certa! É útil distinguir entre dados **estruturados** e **não estruturados**. Os primeiros são tipicamente representados em alguma forma bem estruturado, frequentemente como uma ou várias tabelas, enquanto o segundo é apenas uma coleção de arquivos. Algumas vezes nós também podemos falar de dados **semi estruturados**, que possuem alguma estrutura que pode variar muito.

| Estruturado | Semi-estruturado | Não estruturado |
|----------- |-----------------|--------------|
| Lista de pessoas com seus números de telefones | Páginas da Wikipédia com links | Texto da Encyclopædia Britannica |
| Temperatura de todos os quartos de um prédio a cada minuto nos últimos 20 anos | Coleções de artigos cientificos em formato JSON com autores, datas de publicação, e abstract | Compartilhamento de arquivos com documentos corporativos |
| Dados para idades e gêneros de todas as pessoas entrando em um prédio | Páginas da Internet | Feed de vídeo bruto da câmera de vigilância |

## Onde conseguir Dados

Existem muitas fontes possíveis de dados, e será impossível listar todas elas. No entanto, vamos mencionar alguns dos lugares típicos onde você pode obter dados:

* **Estruturado**
  - **Internet das Coisas**, incluindo dados de diferentes sensores, como sensores de temperatura ou de pressão, fornece muitos dados úteis. Por exemplo, se um escritório de um prédio é equipado com sensores IoT, nós podemos automaticamente controlar o aquecimento e a iluminação com o objetivo de minimizar custos.
  - **Pesquisas** que podemos fazer para os usuários depois de uma compra, ou visitar um web site.
  - **Análise de comportamento** pode, por exemplo, nos ajudar a entender o quão longe um usuário vai dentro de um site, e qual tipicamente é a razão para deixar um site.
* **Não estruturado**
  - **Textos** podem ser uma fonte rica de insights, começando da **pontuação geral de sentimento** (sentiment score), até a extração de palavras chaves e até algum significado semântico.
  - **Imagens** ou **Vídeo**. Um vídeo de uma câmera de vigilância pode ser usado para estimar o tráfico na rua, e informar as pessoas sobre possíveis engarrafamentos.
  - **Logs**  de servidores web pode ser usado para entender quais páginas do nosso site são mais visitadas, e por quanto tempo.
* Semi-estruturado
  - Grafos das **Redes Sociais** podem ser uma boa fonte de dados sobre a personalidade do usuário e a eficácia potencial em espalhar informações.
  - Quando nós temos um monte de fotos de uma festa, nós podemos tentar extrair dados sobre **Dinâmicas de Grupo** construindo um grafo de pessoas tirando fotos umas das outras.

Conhecendo as diferentes fontes possíveis de dados, você pode tentar pensar sobre diferentes cenários onde técnicas de ciência de dados podem ser aplicadas para conhecer a situação melhor, e melhorar o processo de negócio.

## O que você pode fazer com Dados

Em Ciência de Dados, nós focamos em seguir os passos da jornada dos dados:

<dl>
<dt>1) Aquisição de Dados</dt>
<dd>
Primeiro passo é coletar os dados. Enquanto em muitos casos isso pode ser um processo direto, como dados vindo para um banco de dados a partir de uma aplicação web, algumas vezes nós precisamos usar técnicas especiais. Por exemplo, dados de sensores de IoT podem ser muito pesados, e é uma boa prática usar buffering endpoints como Hub de IoT para coletar todos os dados antes de processá-los.
</dd>
<dt>2) Armazenamento de Dados</dt>
<dd>
Armazenar os dados pode ser desafiador, especialmente se estamos falando de big data. Enquanto decide como armazenar os dados, faz sentido antecipar a forma como você gostaria de consultá-los mais tarde. Existem diversas formas de como os dados podem ser armazenados:
<ul>
<li> Bancos de dados relacionais armazenam uma coleção de tabelas, e utilizam uma linguagem especial chamada SQL para consultá-los. Tipicamente, tabelas seriam conectadas umas às outras usando algum schema. Em vários casas nós precisamos converter os dados da forma original para ajustar al schema.</li>
<li>Bancos de dados <a href="https://en.wikipedia.org/wiki/NoSQL">NoSQL</a>, como <a href="https://azure.microsoft.com/services/cosmos-db/?WT.mc_id=academic-77958-bethanycheum">CosmosDB</a>, não impõe schema nos dados, e permite o armazenamento de dados mais complexos, como por exemplo, documentos hierárquicos JSON ou grafos. No entanto, bancos de dados NoSQL não possuem a capacidade rica de consulta do SQL, e não podem impor integridade referencial entre os dados.</li>
<li>Armazenamento em <a href="https://en.wikipedia.org/wiki/Data_lake">Data Lake</a> é usado para grandes coleções de dados na forma bruta. Data lakes são frequentemente usados para big data, onde todos não podem se encaixar em uma máquina, e precisam ser armazenados e processados por um cluster. <a href="https://en.wikipedia.org/wiki/Apache_Parquet">Parquet</a> é o formato de dado que é frequentemente usado em conjunção com big data.</li> 
</ul>
</dd>
<dt>3) Processamento de Dados</dt>
<dd>
Esse é a parte mais emocionante da jornada dos dados, que envolve processar os dados de sua forma original para a forma que pode ser usada para visualização/treinamento do modelo. Quando lidando com dados não estruturados como textos ou imagens, nós podemos precisar de algumas técnicas de IA para extrair **features** dos dados, convertendo-os então para a forma estruturada.
</dd>
<dt>4) Visualização / Percepções Humanas</dt>
<dd>
Frequentemente para entender os dados precisamos visualizar eles. Tendo várias técnicas de visualização diferentes na nossa caixa de ferramentas, nós podemos encontrar a visualização certa para termos um insight. Frequentemente, cientistas de dados precisam "brincar com dos dados", visualizando-os várias vezes e procurando alguma relação. Também, nós podemos usar algumas técnicas de estatísticas para testar alguma hipótese ou provar uma correlação entre pedaços diferentes de dados.
</dd>
<dt>5) Treinando modelos preditivos</dt>
<dd>
Já que o maior objetivo da ciência de dados é ser capaz de tomar decisões baseadas em dados, nós podemos querer usar técnicas de <a href="http://github.com/microsoft/ml-for-beginners">Aprendizando de Máquina</a> para construir modelos preditivos que serão capazes de resolver nosso problema.
</dd>
</dl>

Claro, dependendo dos dados em si alguns passos podem ser ignorados (ex., quando já temos os dados em nosso banco de dados, ou quando não precisamos treinar o modelo), ou repetidos várias vezes (como processamento de dados).

## Digitalização e Transformação Digital

Na última década, muitos negócios começaram a entender a importância dos dados para fazer uma decisão de negócio. Para aplicar os princípios da ciência de dados para gerenciar um negócio é necessário coletar alguns dados, ex. transformar de alguma forma processos de negócio em formato digital. Isso é conhecido como **digitalização**, seguido pelo uso técnicas de ciência de dados para guiar as decisões frequentemente leva a um aumento significante da produtividade (ou mesmo pivô de negócios), chamado de **transformação digital**.

Vamos considerar um exemplo. Suponha que temos um curso de ciência de dados (como esse), que é feito online pelos estudantes, e que queremos usar ciência de dados para melhorá-lo. Como podemos fazer isso?

Nós podemos começar pensando "o que pode ser digitalizado?". A maneira mais simples seria medir o tempo que cada estudante leva para completar cada módulo, e o conhecimento obtido (ex. dando questões de múltipla escolha no final de cada módulo). Tendo a média que todos os estudantes levam para completar, nós podemos descobrir quais módulos causam mais problemas para os estudantes, e trabalhar para simplificá-los.

> Você pode argumentar que essa abordagem não é ideal, pois os módulos podem ter tamanhos diferentes. Provavelmente seria mais justo dividir o tempo pelo tamanho do módulo (em número de caracteres), e comparar esses valores.

Quando começamos a analisar os resultados das questões de múltipla escolha, nós podemos tentar descobrir conceitos específicos que os estudantes não entendem muito bem, e melhorar o conteúdo. Para fazer isso nós precisamos fazer questões de uma forma que cada questão mapeia para um certo conteúdo ou conhecimento.

Se nós quiséssemos complicar ainda mais, nós podemos "plotar" o tempo levado para cada módulo em relação à categoria de idade de cada estudante. Nós podemos descobrir que alguma categoria de idade leva um tempo inapropriadamente longo para completar o módulo, ou os estudantes que abandonam em um certo ponto. Isso pode nos ajudar a fornecer recomendações de idade para o módulo, e minimizar a insatisfação das pessoas para expectativas erradas.

## 🚀 Desafio

Nesse desafio, nós vamos tentar encontrar conceitos relevantes para a área de Ciência de Dados olhando textos. Nós vamos pegar um artigo da Wikipedia sobre Ciência de Dados, baixar e processar o texto, e então construir uma nuvem de palavras como essa:

![Nuvem de Palavras para Ciência de Dados](../images/ds_wordcloud.png)

Visite [`notebook.ipynb`](../notebook.ipynb) para ler o código. Você também pode rodar esse código, e ver como ele performa toda a transformação de dados em tempo real.

> Se você não sabe como rodar códigos no Jupyter Notebook, dê uma olhada [nesse artigo](https://soshnikov.com/education/how-to-execute-notebooks-from-github/).



## [Quiz pós-aula](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/1)

## Tarefas

* **Tarefa 1**: Modifique o código acima para descobrir conceitos relacionados para as áreas de **Big Data** e **Aprendizado de Máquina**
* **Tarefa 2**: [Pense Sobre Cenários de Ciência de Dados](assignment.pt-br.md)

## Créditos

Essa aula foi autorado com ♥️ por [Dmitry Soshnikov](http://soshnikov.com)
