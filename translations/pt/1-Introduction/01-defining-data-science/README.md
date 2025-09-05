<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a0516588d172f82f35f7a0d4a001e5d0",
  "translation_date": "2025-09-05T13:27:35+00:00",
  "source_file": "1-Introduction/01-defining-data-science/README.md",
  "language_code": "pt"
}
-->
# Definindo Ciência de Dados

| ![ Sketchnote por [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/01-Definitions.png) |
| :----------------------------------------------------------------------------------------------------: |
|              Definindo Ciência de Dados - _Sketchnote por [@nitya](https://twitter.com/nitya)_         |

---

[![Vídeo Definindo Ciência de Dados](../../../../1-Introduction/01-defining-data-science/images/video-def-ds.png)](https://youtu.be/beZ7Mb_oz9I)

## [Questionário pré-aula](https://ff-quizzes.netlify.app/en/ds/quiz/0)

## O que é Dados?
No nosso dia a dia, estamos constantemente rodeados por dados. O texto que está a ler agora é um dado. A lista de números de telefone dos seus amigos no seu smartphone é um dado, assim como a hora atual exibida no seu relógio. Como seres humanos, operamos naturalmente com dados ao contar o dinheiro que temos ou ao escrever cartas para os nossos amigos.

No entanto, os dados tornaram-se muito mais importantes com a criação dos computadores. A principal função dos computadores é realizar cálculos, mas eles precisam de dados para operar. Assim, precisamos entender como os computadores armazenam e processam dados.

Com o surgimento da Internet, o papel dos computadores como dispositivos de manipulação de dados aumentou. Se pensar bem, usamos cada vez mais os computadores para processar e comunicar dados, em vez de realizar cálculos propriamente ditos. Quando escrevemos um e-mail para um amigo ou pesquisamos informações na Internet, estamos essencialmente a criar, armazenar, transmitir e manipular dados.
> Consegue lembrar-se da última vez que usou um computador para realmente calcular algo?

## O que é Ciência de Dados?

Na [Wikipedia](https://en.wikipedia.org/wiki/Data_science), **Ciência de Dados** é definida como *um campo científico que utiliza métodos científicos para extrair conhecimento e insights de dados estruturados e não estruturados, e aplicar conhecimento e insights acionáveis em várias áreas de aplicação*.

Esta definição destaca os seguintes aspetos importantes da ciência de dados:

* O principal objetivo da ciência de dados é **extrair conhecimento** dos dados, ou seja, **compreender** os dados, encontrar relações ocultas e construir um **modelo**.
* A ciência de dados utiliza **métodos científicos**, como probabilidade e estatística. Na verdade, quando o termo *ciência de dados* foi introduzido pela primeira vez, algumas pessoas argumentaram que era apenas um novo nome elegante para estatística. Hoje em dia, está claro que o campo é muito mais amplo.
* O conhecimento obtido deve ser aplicado para produzir **insights acionáveis**, ou seja, insights práticos que podem ser aplicados a situações reais de negócios.
* Devemos ser capazes de operar tanto com dados **estruturados** quanto **não estruturados**. Voltaremos a discutir os diferentes tipos de dados mais adiante no curso.
* O **domínio de aplicação** é um conceito importante, e os cientistas de dados frequentemente precisam de algum grau de especialização no domínio do problema, como finanças, medicina, marketing, etc.

> Outro aspeto importante da Ciência de Dados é que ela estuda como os dados podem ser recolhidos, armazenados e manipulados usando computadores. Enquanto a estatística nos fornece as bases matemáticas, a ciência de dados aplica conceitos matemáticos para realmente extrair insights dos dados.

Uma das formas (atribuída a [Jim Gray](https://en.wikipedia.org/wiki/Jim_Gray_(computer_scientist))) de olhar para a ciência de dados é considerá-la como um paradigma separado da ciência:
* **Empírico**, no qual confiamos principalmente em observações e resultados de experiências
* **Teórico**, onde novos conceitos emergem do conhecimento científico existente
* **Computacional**, onde descobrimos novos princípios com base em experiências computacionais
* **Baseado em Dados**, focado em descobrir relações e padrões nos dados  

## Outros Campos Relacionados

Como os dados estão em todo lado, a ciência de dados também é um campo amplo, tocando em muitas outras disciplinas.

## Tipos de Dados

Como já mencionámos, os dados estão em todo lado. Só precisamos de capturá-los da forma certa! É útil distinguir entre dados **estruturados** e **não estruturados**. Os primeiros são tipicamente representados de forma bem organizada, muitas vezes como uma tabela ou várias tabelas, enquanto os últimos são apenas uma coleção de ficheiros. Às vezes, também podemos falar de dados **semi-estruturados**, que têm algum tipo de estrutura que pode variar bastante.

| Estruturados                                                                | Semi-estruturados                                                                             | Não estruturados                        |
| ---------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------- |
| Lista de pessoas com os seus números de telefone                            | Páginas da Wikipédia com links                                                                | Texto da Enciclopédia Britânica         |
| Temperatura em todas as salas de um edifício a cada minuto nos últimos 20 anos | Coleção de artigos científicos em formato JSON com autores, data de publicação e resumo       | Partilha de ficheiros com documentos corporativos |
| Dados sobre idade e género de todas as pessoas que entram no edifício       | Páginas da Internet                                                                           | Vídeo bruto de uma câmara de vigilância |

## Onde Obter Dados

Existem muitas fontes possíveis de dados, e seria impossível listar todas! No entanto, vamos mencionar alguns dos locais típicos onde pode obter dados:

* **Estruturados**
  - **Internet das Coisas** (IoT), incluindo dados de diferentes sensores, como sensores de temperatura ou pressão, fornece muitos dados úteis. Por exemplo, se um edifício de escritórios estiver equipado com sensores IoT, podemos controlar automaticamente o aquecimento e a iluminação para minimizar custos.
  - **Inquéritos** que pedimos aos utilizadores para preencherem após uma compra ou após visitarem um site.
  - **Análise de comportamento** pode, por exemplo, ajudar-nos a entender até que ponto um utilizador explora um site e qual é o motivo típico para sair do site.
* **Não estruturados**
  - **Textos** podem ser uma rica fonte de insights, como um **índice de sentimento** geral ou a extração de palavras-chave e significado semântico.
  - **Imagens** ou **Vídeos**. Um vídeo de uma câmara de vigilância pode ser usado para estimar o tráfego na estrada e informar as pessoas sobre potenciais engarrafamentos.
  - **Registos de servidores web** podem ser usados para entender quais páginas do nosso site são mais visitadas e por quanto tempo.
* **Semi-estruturados**
  - **Gráficos de Redes Sociais** podem ser ótimas fontes de dados sobre personalidades de utilizadores e a potencial eficácia na disseminação de informações.
  - Quando temos um conjunto de fotografias de uma festa, podemos tentar extrair dados de **Dinâmica de Grupo** construindo um gráfico de pessoas que tiraram fotos juntas.

Ao conhecer diferentes fontes possíveis de dados, pode tentar pensar em diferentes cenários onde as técnicas de ciência de dados podem ser aplicadas para compreender melhor a situação e melhorar os processos de negócios.

## O que Pode Fazer com Dados

Na Ciência de Dados, focamo-nos nos seguintes passos da jornada dos dados:

Claro, dependendo dos dados reais, alguns passos podem estar ausentes (por exemplo, quando já temos os dados na base de dados ou quando não precisamos de treinar um modelo), ou alguns passos podem ser repetidos várias vezes (como o processamento de dados).

## Digitalização e Transformação Digital

Na última década, muitas empresas começaram a entender a importância dos dados na tomada de decisões de negócios. Para aplicar os princípios da ciência de dados na gestão de um negócio, é necessário primeiro recolher alguns dados, ou seja, traduzir os processos de negócios para uma forma digital. Isto é conhecido como **digitalização**. Aplicar técnicas de ciência de dados a esses dados para orientar decisões pode levar a aumentos significativos na produtividade (ou até mesmo a uma mudança de direção no negócio), chamado de **transformação digital**.

Vamos considerar um exemplo. Suponha que temos um curso de ciência de dados (como este) que oferecemos online aos alunos, e queremos usar ciência de dados para melhorá-lo. Como podemos fazer isso?

Podemos começar por perguntar "O que pode ser digitalizado?" A forma mais simples seria medir o tempo que cada aluno leva para completar cada módulo e avaliar o conhecimento adquirido dando um teste de múltipla escolha no final de cada módulo. Ao calcular a média do tempo de conclusão entre todos os alunos, podemos descobrir quais módulos causam mais dificuldades e trabalhar para os simplificar.
> Pode argumentar que esta abordagem não é ideal, porque os módulos podem ter comprimentos diferentes. Provavelmente seria mais justo dividir o tempo pelo comprimento do módulo (em número de caracteres) e comparar esses valores em vez disso.
Quando começamos a analisar os resultados de testes de escolha múltipla, podemos tentar determinar quais conceitos os alunos têm dificuldade em compreender e usar essa informação para melhorar o conteúdo. Para isso, precisamos projetar os testes de forma que cada pergunta esteja associada a um determinado conceito ou bloco de conhecimento.

Se quisermos ir ainda mais longe, podemos traçar o tempo gasto em cada módulo em relação à categoria etária dos alunos. Podemos descobrir que, para algumas faixas etárias, leva um tempo excessivamente longo para concluir o módulo ou que os alunos desistem antes de terminá-lo. Isso pode nos ajudar a fornecer recomendações de idade para o módulo e minimizar a insatisfação das pessoas devido a expectativas erradas.

## 🚀 Desafio

Neste desafio, tentaremos identificar conceitos relevantes para o campo da Ciência de Dados analisando textos. Vamos pegar um artigo da Wikipédia sobre Ciência de Dados, baixar e processar o texto e, em seguida, criar uma nuvem de palavras como esta:

![Nuvem de Palavras para Ciência de Dados](../../../../1-Introduction/01-defining-data-science/images/ds_wordcloud.png)

Visite [`notebook.ipynb`](../../../../../../../../../1-Introduction/01-defining-data-science/notebook.ipynb ':ignore') para ler o código. Você também pode executar o código e ver como ele realiza todas as transformações de dados em tempo real.

> Se não souber como executar código em um Jupyter Notebook, consulte [este artigo](https://soshnikov.com/education/how-to-execute-notebooks-from-github/).

## [Questionário pós-aula](https://ff-quizzes.netlify.app/en/ds/quiz/1)

## Tarefas

* **Tarefa 1**: Modifique o código acima para identificar conceitos relacionados aos campos de **Big Data** e **Machine Learning**  
* **Tarefa 2**: [Pense em Cenários de Ciência de Dados](assignment.md)

## Créditos

Esta lição foi criada com ♥️ por [Dmitry Soshnikov](http://soshnikov.com)

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original no seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se uma tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes do uso desta tradução.