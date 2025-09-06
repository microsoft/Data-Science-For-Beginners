<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a0516588d172f82f35f7a0d4a001e5d0",
  "translation_date": "2025-09-06T08:36:44+00:00",
  "source_file": "1-Introduction/01-defining-data-science/README.md",
  "language_code": "br"
}
-->
# Definindo Ciência de Dados

| ![ Sketchnote por [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/01-Definitions.png) |
| :----------------------------------------------------------------------------------------------------: |
|              Definindo Ciência de Dados - _Sketchnote por [@nitya](https://twitter.com/nitya)_         |

---

[![Vídeo Definindo Ciência de Dados](../../../../1-Introduction/01-defining-data-science/images/video-def-ds.png)](https://youtu.be/beZ7Mb_oz9I)

## [Quiz pré-aula](https://ff-quizzes.netlify.app/en/ds/quiz/0)

## O que é Dados?
No nosso dia a dia, estamos constantemente cercados por dados. O texto que você está lendo agora é um dado. A lista de números de telefone dos seus amigos no seu smartphone é um dado, assim como a hora atual exibida no seu relógio. Como seres humanos, operamos naturalmente com dados ao contar o dinheiro que temos ou ao escrever cartas para nossos amigos.

No entanto, os dados se tornaram muito mais críticos com a criação dos computadores. O papel principal dos computadores é realizar cálculos, mas eles precisam de dados para operar. Assim, precisamos entender como os computadores armazenam e processam dados.

Com o surgimento da Internet, o papel dos computadores como dispositivos de manipulação de dados aumentou. Se você pensar bem, usamos computadores cada vez mais para processar e comunicar dados, em vez de realizar cálculos propriamente ditos. Quando escrevemos um e-mail para um amigo ou buscamos informações na Internet, estamos essencialmente criando, armazenando, transmitindo e manipulando dados.
> Você consegue se lembrar da última vez que usou um computador para realmente calcular algo?

## O que é Ciência de Dados?

Na [Wikipedia](https://en.wikipedia.org/wiki/Data_science), **Ciência de Dados** é definida como *um campo científico que utiliza métodos científicos para extrair conhecimento e insights de dados estruturados e não estruturados, e aplicar conhecimentos e insights acionáveis em uma ampla gama de domínios de aplicação*.

Essa definição destaca os seguintes aspectos importantes da ciência de dados:

* O principal objetivo da ciência de dados é **extrair conhecimento** dos dados, ou seja, **entender** os dados, encontrar relações ocultas e construir um **modelo**.
* A ciência de dados utiliza **métodos científicos**, como probabilidade e estatística. De fato, quando o termo *ciência de dados* foi introduzido pela primeira vez, algumas pessoas argumentaram que era apenas um novo nome sofisticado para estatística. Hoje em dia, está claro que o campo é muito mais amplo.
* O conhecimento obtido deve ser aplicado para produzir **insights acionáveis**, ou seja, insights práticos que podem ser aplicados a situações reais de negócios.
* Devemos ser capazes de operar tanto com dados **estruturados** quanto **não estruturados**. Voltaremos a discutir os diferentes tipos de dados mais adiante no curso.
* O **domínio de aplicação** é um conceito importante, e os cientistas de dados frequentemente precisam de algum grau de especialização no domínio do problema, como finanças, medicina, marketing, etc.

> Outro aspecto importante da Ciência de Dados é que ela estuda como os dados podem ser coletados, armazenados e manipulados usando computadores. Enquanto a estatística nos fornece fundamentos matemáticos, a ciência de dados aplica conceitos matemáticos para realmente extrair insights dos dados.

Uma das formas (atribuída a [Jim Gray](https://en.wikipedia.org/wiki/Jim_Gray_(computer_scientist))) de enxergar a ciência de dados é considerá-la como um paradigma separado da ciência:
* **Empírico**, no qual confiamos principalmente em observações e resultados de experimentos
* **Teórico**, onde novos conceitos emergem do conhecimento científico existente
* **Computacional**, onde descobrimos novos princípios com base em experimentos computacionais
* **Baseado em Dados**, focado em descobrir relações e padrões nos dados  

## Outros Campos Relacionados

Como os dados estão em toda parte, a ciência de dados também é um campo amplo, tocando em muitas outras disciplinas.

## Tipos de Dados

Como já mencionamos, os dados estão em toda parte. Só precisamos capturá-los da maneira certa! É útil distinguir entre dados **estruturados** e **não estruturados**. O primeiro é tipicamente representado de forma bem estruturada, muitas vezes como uma tabela ou várias tabelas, enquanto o último é apenas uma coleção de arquivos. Às vezes, também podemos falar de dados **semiestruturados**, que possuem algum tipo de estrutura que pode variar bastante.

| Estruturados                                                                | Semiestruturados                                                                              | Não Estruturados                        |
| ---------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | --------------------------------------- |
| Lista de pessoas com seus números de telefone                               | Páginas da Wikipedia com links                                                               | Texto da Enciclopédia Britânica         |
| Temperatura em todos os cômodos de um prédio a cada minuto nos últimos 20 anos | Coleção de artigos científicos em formato JSON com autores, data de publicação e resumo      | Compartilhamento de arquivos corporativos |
| Dados de idade e gênero de todas as pessoas entrando no prédio              | Páginas da Internet                                                                          | Vídeo bruto de uma câmera de vigilância |

## Onde Obter Dados

Existem muitas fontes possíveis de dados, e seria impossível listar todas elas! No entanto, vamos mencionar alguns lugares típicos onde você pode obter dados:

* **Estruturados**
  - **Internet das Coisas** (IoT), incluindo dados de diferentes sensores, como sensores de temperatura ou pressão, fornece muitos dados úteis. Por exemplo, se um prédio de escritórios estiver equipado com sensores IoT, podemos controlar automaticamente o aquecimento e a iluminação para minimizar custos.
  - **Pesquisas** que pedimos aos usuários para preencher após uma compra ou após visitar um site.
  - **Análise de comportamento** pode, por exemplo, nos ajudar a entender até que ponto um usuário navega em um site e qual é o motivo típico para sair do site.
* **Não Estruturados**
  - **Textos** podem ser uma rica fonte de insights, como uma pontuação geral de **sentimento**, ou extração de palavras-chave e significado semântico.
  - **Imagens** ou **Vídeos**. Um vídeo de uma câmera de vigilância pode ser usado para estimar o tráfego na estrada e informar as pessoas sobre possíveis congestionamentos.
  - **Logs** de servidores web podem ser usados para entender quais páginas do nosso site são mais visitadas e por quanto tempo.
* **Semiestruturados**
  - **Grafos de Redes Sociais** podem ser ótimas fontes de dados sobre personalidades de usuários e a potencial eficácia na disseminação de informações.
  - Quando temos um monte de fotografias de uma festa, podemos tentar extrair dados de **Dinâmica de Grupo** construindo um grafo de pessoas tirando fotos umas com as outras.

Conhecendo diferentes fontes possíveis de dados, você pode pensar em diferentes cenários onde técnicas de ciência de dados podem ser aplicadas para entender melhor a situação e melhorar processos de negócios.

## O que Você Pode Fazer com Dados

Na Ciência de Dados, focamos nas seguintes etapas da jornada dos dados:

Claro, dependendo dos dados reais, algumas etapas podem estar ausentes (por exemplo, quando já temos os dados no banco de dados ou quando não precisamos de treinamento de modelo), ou algumas etapas podem ser repetidas várias vezes (como o processamento de dados).

## Digitalização e Transformação Digital

Na última década, muitas empresas começaram a entender a importância dos dados na tomada de decisões de negócios. Para aplicar os princípios da ciência de dados na gestão de um negócio, primeiro é necessário coletar alguns dados, ou seja, traduzir processos de negócios para a forma digital. Isso é conhecido como **digitalização**. Aplicar técnicas de ciência de dados a esses dados para orientar decisões pode levar a aumentos significativos na produtividade (ou até mesmo a uma mudança de direção nos negócios), chamado de **transformação digital**.

Vamos considerar um exemplo. Suponha que temos um curso de ciência de dados (como este) que oferecemos online para estudantes, e queremos usar ciência de dados para melhorá-lo. Como podemos fazer isso?

Podemos começar perguntando "O que pode ser digitalizado?" A maneira mais simples seria medir o tempo que cada aluno leva para completar cada módulo e medir o conhecimento adquirido dando um teste de múltipla escolha ao final de cada módulo. Ao calcular a média do tempo de conclusão entre todos os alunos, podemos descobrir quais módulos causam mais dificuldades e trabalhar para simplificá-los.
Você pode argumentar que essa abordagem não é ideal, porque os módulos podem ter comprimentos diferentes. Provavelmente seria mais justo dividir o tempo pelo comprimento do módulo (em número de caracteres) e comparar esses valores em vez disso.
Quando começamos a analisar os resultados de testes de múltipla escolha, podemos tentar determinar quais conceitos os alunos têm dificuldade em entender e usar essas informações para melhorar o conteúdo. Para isso, precisamos projetar os testes de forma que cada pergunta esteja vinculada a um determinado conceito ou bloco de conhecimento.

Se quisermos ir ainda mais longe, podemos traçar o tempo gasto em cada módulo em relação à faixa etária dos alunos. Podemos descobrir que, para algumas faixas etárias, leva um tempo excessivamente longo para concluir o módulo ou que os alunos abandonam antes de terminá-lo. Isso pode nos ajudar a fornecer recomendações de idade para o módulo e minimizar a insatisfação das pessoas devido a expectativas equivocadas.

## 🚀 Desafio

Neste desafio, tentaremos encontrar conceitos relevantes para o campo de Ciência de Dados analisando textos. Vamos pegar um artigo da Wikipedia sobre Ciência de Dados, baixar e processar o texto, e então construir uma nuvem de palavras como esta:

![Nuvem de Palavras para Ciência de Dados](../../../../1-Introduction/01-defining-data-science/images/ds_wordcloud.png)

Visite [`notebook.ipynb`](../../../../../../../../../1-Introduction/01-defining-data-science/notebook.ipynb ':ignore') para ler o código. Você também pode executar o código e ver como ele realiza todas as transformações de dados em tempo real.

> Se você não sabe como executar código em um Jupyter Notebook, confira [este artigo](https://soshnikov.com/education/how-to-execute-notebooks-from-github/).

## [Quiz pós-aula](https://ff-quizzes.netlify.app/en/ds/quiz/1)

## Tarefas

* **Tarefa 1**: Modifique o código acima para descobrir conceitos relacionados aos campos de **Big Data** e **Machine Learning**
* **Tarefa 2**: [Pense em Cenários de Ciência de Dados](assignment.md)

## Créditos

Esta lição foi criada com ♥️ por [Dmitry Soshnikov](http://soshnikov.com)

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.