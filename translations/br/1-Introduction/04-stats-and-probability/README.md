<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b706a07cfa87ba091cbb91e0aa775600",
  "translation_date": "2025-08-27T17:27:28+00:00",
  "source_file": "1-Introduction/04-stats-and-probability/README.md",
  "language_code": "br"
}
-->
# Uma Breve Introdução à Estatística e Probabilidade

|![ Sketchnote por [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/04-Statistics-Probability.png)|
|:---:|
| Estatística e Probabilidade - _Sketchnote por [@nitya](https://twitter.com/nitya)_ |

A Teoria da Estatística e Probabilidade são duas áreas altamente relacionadas da Matemática que têm grande relevância para a Ciência de Dados. É possível trabalhar com dados sem um conhecimento profundo de matemática, mas ainda assim é melhor conhecer pelo menos alguns conceitos básicos. Aqui apresentaremos uma breve introdução que ajudará você a começar.

[![Vídeo de Introdução](../../../../translated_images/video-prob-and-stats.e4282e5efa2f2543400843ed98b1057065c9600cebfc8a728e8931b5702b2ae4.br.png)](https://youtu.be/Z5Zy85g4Yjw)

## [Quiz pré-aula](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/6)

## Probabilidade e Variáveis Aleatórias

**Probabilidade** é um número entre 0 e 1 que expressa o quão provável é um **evento**. Ela é definida como o número de resultados positivos (que levam ao evento), dividido pelo número total de resultados, dado que todos os resultados são igualmente prováveis. Por exemplo, ao lançar um dado, a probabilidade de obter um número par é 3/6 = 0.5.

Quando falamos de eventos, usamos **variáveis aleatórias**. Por exemplo, a variável aleatória que representa o número obtido ao lançar um dado assumiria valores de 1 a 6. O conjunto de números de 1 a 6 é chamado de **espaço amostral**. Podemos falar sobre a probabilidade de uma variável aleatória assumir um determinado valor, por exemplo P(X=3)=1/6.

A variável aleatória no exemplo anterior é chamada de **discreta**, porque possui um espaço amostral contável, ou seja, há valores separados que podem ser enumerados. Existem casos em que o espaço amostral é um intervalo de números reais ou o conjunto completo de números reais. Essas variáveis são chamadas de **contínuas**. Um bom exemplo é o horário de chegada de um ônibus.

## Distribuição de Probabilidade

No caso de variáveis aleatórias discretas, é fácil descrever a probabilidade de cada evento por uma função P(X). Para cada valor *s* do espaço amostral *S*, ela fornecerá um número entre 0 e 1, de forma que a soma de todos os valores de P(X=s) para todos os eventos seja 1.

A distribuição discreta mais conhecida é a **distribuição uniforme**, na qual há um espaço amostral de N elementos, com probabilidade igual de 1/N para cada um deles.

É mais difícil descrever a distribuição de probabilidade de uma variável contínua, com valores retirados de algum intervalo [a,b], ou do conjunto completo de números reais ℝ. Considere o caso do horário de chegada de um ônibus. Na verdade, para cada horário exato de chegada *t*, a probabilidade de o ônibus chegar exatamente nesse horário é 0!

> Agora você sabe que eventos com probabilidade 0 acontecem, e com muita frequência! Pelo menos toda vez que o ônibus chega!

Só podemos falar sobre a probabilidade de uma variável cair em um determinado intervalo de valores, por exemplo, P(t<sub>1</sub>≤X<t<sub>2</sub>). Nesse caso, a distribuição de probabilidade é descrita por uma **função densidade de probabilidade** p(x), tal que

![P(t_1\le X<t_2)=\int_{t_1}^{t_2}p(x)dx](../../../../translated_images/probability-density.a8aad29f17a14afb519b407c7b6edeb9f3f9aa5f69c9e6d9445f604e5f8a2bf7.br.png)

Um análogo contínuo da distribuição uniforme é chamado de **uniforme contínua**, que é definido em um intervalo finito. A probabilidade de o valor X cair em um intervalo de comprimento l é proporcional a l, e aumenta até 1.

Outra distribuição importante é a **distribuição normal**, sobre a qual falaremos mais detalhadamente abaixo.

## Média, Variância e Desvio Padrão

Suponha que extraímos uma sequência de n amostras de uma variável aleatória X: x<sub>1</sub>, x<sub>2</sub>, ..., x<sub>n</sub>. Podemos definir o valor **médio** (ou **média aritmética**) da sequência da maneira tradicional como (x<sub>1</sub>+x<sub>2</sub>+x<sub>n</sub>)/n. À medida que aumentamos o tamanho da amostra (ou seja, tomamos o limite com n→∞), obteremos a média (também chamada de **expectativa**) da distribuição. Denotaremos a expectativa por **E**(x).

> Pode-se demonstrar que, para qualquer distribuição discreta com valores {x<sub>1</sub>, x<sub>2</sub>, ..., x<sub>N</sub>} e probabilidades correspondentes p<sub>1</sub>, p<sub>2</sub>, ..., p<sub>N</sub>, a expectativa seria igual a E(X)=x<sub>1</sub>p<sub>1</sub>+x<sub>2</sub>p<sub>2</sub>+...+x<sub>N</sub>p<sub>N</sub>.

Para identificar o quão dispersos os valores estão, podemos calcular a variância σ<sup>2</sup> = ∑(x<sub>i</sub> - μ)<sup>2</sup>/n, onde μ é a média da sequência. O valor σ é chamado de **desvio padrão**, e σ<sup>2</sup> é chamado de **variância**.

## Moda, Mediana e Quartis

Às vezes, a média não representa adequadamente o valor "típico" dos dados. Por exemplo, quando há alguns valores extremos completamente fora do intervalo, eles podem afetar a média. Outra boa indicação é a **mediana**, um valor tal que metade dos pontos de dados são menores que ele, e a outra metade - maiores.

Para nos ajudar a entender a distribuição dos dados, é útil falar sobre **quartis**:

* Primeiro quartil, ou Q1, é um valor tal que 25% dos dados estão abaixo dele
* Terceiro quartil, ou Q3, é um valor tal que 75% dos dados estão abaixo dele

Graficamente, podemos representar a relação entre mediana e quartis em um diagrama chamado **box plot**:

<img src="images/boxplot_explanation.png" width="50%"/>

Aqui também calculamos o **intervalo interquartil** IQR=Q3-Q1, e os chamados **outliers** - valores que estão fora dos limites [Q1-1.5*IQR,Q3+1.5*IQR].

Para uma distribuição finita que contém um pequeno número de valores possíveis, um bom valor "típico" é aquele que aparece com mais frequência, chamado de **moda**. Ele é frequentemente aplicado a dados categóricos, como cores. Considere uma situação em que temos dois grupos de pessoas - algumas que preferem fortemente vermelho, e outras que preferem azul. Se codificarmos as cores por números, o valor médio para uma cor favorita estaria em algum lugar no espectro laranja-verde, o que não indica a preferência real de nenhum dos grupos. No entanto, a moda seria uma das cores ou ambas, se o número de pessoas votando por elas for igual (nesse caso, chamamos a amostra de **multimodal**).

## Dados do Mundo Real

Quando analisamos dados da vida real, eles frequentemente não são variáveis aleatórias propriamente ditas, no sentido de que não realizamos experimentos com resultados desconhecidos. Por exemplo, considere um time de jogadores de beisebol e seus dados corporais, como altura, peso e idade. Esses números não são exatamente aleatórios, mas ainda podemos aplicar os mesmos conceitos matemáticos. Por exemplo, uma sequência de pesos de pessoas pode ser considerada uma sequência de valores retirados de alguma variável aleatória. Abaixo está a sequência de pesos de jogadores reais de beisebol da [Major League Baseball](http://mlb.mlb.com/index.jsp), retirada deste [conjunto de dados](http://wiki.stat.ucla.edu/socr/index.php/SOCR_Data_MLB_HeightsWeights) (para sua conveniência, apenas os primeiros 20 valores são mostrados):

```
[180.0, 215.0, 210.0, 210.0, 188.0, 176.0, 209.0, 200.0, 231.0, 180.0, 188.0, 180.0, 185.0, 160.0, 180.0, 185.0, 197.0, 189.0, 185.0, 219.0]
```

> **Nota**: Para ver o exemplo de trabalho com este conjunto de dados, dê uma olhada no [notebook complementar](notebook.ipynb). Há também vários desafios ao longo desta lição, e você pode completá-los adicionando algum código a esse notebook. Se você não tem certeza de como operar com dados, não se preocupe - voltaremos a trabalhar com dados usando Python mais tarde. Se você não sabe como executar código em Jupyter Notebook, confira [este artigo](https://soshnikov.com/education/how-to-execute-notebooks-from-github/).

Aqui está o box plot mostrando média, mediana e quartis para nossos dados:

![Box Plot de Peso](../../../../translated_images/weight-boxplot.1dbab1c03af26f8a008fff4e17680082c8ab147d6df646cbac440bbf8f5b9c42.br.png)

Como nossos dados contêm informações sobre diferentes **funções** de jogadores, também podemos fazer o box plot por função - isso nos permitirá ter uma ideia de como os valores dos parâmetros diferem entre as funções. Desta vez, consideraremos a altura:

![Box plot por função](../../../../translated_images/boxplot_byrole.036b27a1c3f52d42f66fba2324ec5cde0a1bca6a01a619eeb0ce7cd054b2527b.br.png)

Este diagrama sugere que, em média, a altura dos jogadores de primeira base é maior que a altura dos jogadores de segunda base. Mais tarde nesta lição, aprenderemos como podemos testar essa hipótese de forma mais formal e como demonstrar que nossos dados são estatisticamente significativos para mostrar isso.

> Ao trabalhar com dados do mundo real, assumimos que todos os pontos de dados são amostras retiradas de alguma distribuição de probabilidade. Essa suposição nos permite aplicar técnicas de aprendizado de máquina e construir modelos preditivos funcionais.

Para ver qual é a distribuição de nossos dados, podemos plotar um gráfico chamado **histograma**. O eixo X conteria um número de diferentes intervalos de peso (os chamados **bins**), e o eixo vertical mostraria o número de vezes que a amostra da variável aleatória esteve dentro de um determinado intervalo.

![Histograma de dados do mundo real](../../../../translated_images/weight-histogram.bfd00caf7fc30b145b21e862dba7def41c75635d5280de25d840dd7f0b00545e.br.png)

A partir deste histograma, você pode ver que todos os valores estão centrados em torno de um certo peso médio, e quanto mais nos afastamos desse peso - menos pesos desse valor são encontrados. Ou seja, é muito improvável que o peso de um jogador de beisebol seja muito diferente do peso médio. A variância dos pesos mostra a extensão em que os pesos provavelmente diferem da média.

> Se pegarmos pesos de outras pessoas, não da liga de beisebol, a distribuição provavelmente será diferente. No entanto, o formato da distribuição será o mesmo, mas a média e a variância mudariam. Assim, se treinarmos nosso modelo com jogadores de beisebol, é provável que ele forneça resultados errados quando aplicado a estudantes de uma universidade, porque a distribuição subjacente é diferente.

## Distribuição Normal

A distribuição de pesos que vimos acima é muito típica, e muitas medições do mundo real seguem o mesmo tipo de distribuição, mas com diferentes médias e variâncias. Essa distribuição é chamada de **distribuição normal**, e ela desempenha um papel muito importante na estatística.

Usar a distribuição normal é uma maneira correta de gerar pesos aleatórios de potenciais jogadores de beisebol. Uma vez que sabemos o peso médio `mean` e o desvio padrão `std`, podemos gerar 1000 amostras de peso da seguinte forma:
```python
samples = np.random.normal(mean,std,1000)
``` 

Se plotarmos o histograma das amostras geradas, veremos uma imagem muito semelhante à mostrada acima. E se aumentarmos o número de amostras e o número de bins, podemos gerar uma imagem de uma distribuição normal mais próxima do ideal:

![Distribuição Normal com média=0 e desvio padrão=1](../../../../translated_images/normal-histogram.dfae0d67c202137d552d0015fb87581eca263925e512404f3c12d8885315432e.br.png)

*Distribuição Normal com média=0 e desvio padrão=1*

## Intervalos de Confiança

Quando falamos sobre os pesos dos jogadores de beisebol, assumimos que existe uma **variável aleatória W** que corresponde à distribuição de probabilidade ideal dos pesos de todos os jogadores de beisebol (o chamado **população**). Nossa sequência de pesos corresponde a um subconjunto de todos os jogadores de beisebol que chamamos de **amostra**. Uma pergunta interessante é: podemos conhecer os parâmetros da distribuição de W, ou seja, a média e a variância da população?

A resposta mais simples seria calcular a média e a variância de nossa amostra. No entanto, pode acontecer que nossa amostra aleatória não represente com precisão a população completa. Assim, faz sentido falar sobre **intervalo de confiança**.
> **Intervalo de confiança** é a estimativa da média verdadeira de uma população com base na nossa amostra, que é precisa dentro de uma determinada probabilidade (ou **nível de confiança**).
Suponha que temos uma amostra X<sub>1</sub>, ..., X<sub>n</sub> da nossa distribuição. Cada vez que extraímos uma amostra da nossa distribuição, acabamos com um valor médio diferente μ. Assim, μ pode ser considerado uma variável aleatória. Um **intervalo de confiança** com confiança p é um par de valores (L<sub>p</sub>,R<sub>p</sub>), tal que **P**(L<sub>p</sub>≤μ≤R<sub>p</sub>) = p, ou seja, a probabilidade de o valor médio medido estar dentro do intervalo é igual a p.

Vai além da nossa breve introdução discutir em detalhes como esses intervalos de confiança são calculados. Mais detalhes podem ser encontrados [na Wikipedia](https://en.wikipedia.org/wiki/Confidence_interval). Em resumo, definimos a distribuição da média amostral calculada em relação à média verdadeira da população, que é chamada de **distribuição t de Student**.

> **Fato interessante**: A distribuição t de Student foi nomeada em homenagem ao matemático William Sealy Gosset, que publicou seu artigo sob o pseudônimo "Student". Ele trabalhava na cervejaria Guinness e, segundo uma das versões, seu empregador não queria que o público soubesse que eles estavam usando testes estatísticos para determinar a qualidade das matérias-primas.

Se quisermos estimar a média μ da nossa população com confiança p, precisamos pegar o *(1-p)/2-ésimo percentil* de uma distribuição t de Student A, que pode ser obtido em tabelas ou calculado usando algumas funções integradas de softwares estatísticos (por exemplo, Python, R, etc.). Então, o intervalo para μ seria dado por X±A*D/√n, onde X é a média obtida da amostra e D é o desvio padrão.

> **Nota**: Também omitimos a discussão de um conceito importante de [graus de liberdade](https://en.wikipedia.org/wiki/Degrees_of_freedom_(statistics)), que é relevante em relação à distribuição t de Student. Você pode consultar livros mais completos sobre estatística para entender esse conceito mais profundamente.

Um exemplo de cálculo de intervalo de confiança para pesos e alturas é dado nos [notebooks complementares](notebook.ipynb).

| p    | Média do peso |
|------|---------------|
| 0.85 | 201.73±0.94   |
| 0.90 | 201.73±1.08   |
| 0.95 | 201.73±1.28   |

Observe que quanto maior a probabilidade de confiança, mais amplo é o intervalo de confiança.

## Teste de Hipóteses

No nosso conjunto de dados de jogadores de beisebol, existem diferentes funções de jogadores, que podem ser resumidas abaixo (veja o [notebook complementar](notebook.ipynb) para ver como esta tabela pode ser calculada):

| Função             | Altura     | Peso       | Contagem |
|--------------------|------------|------------|----------|
| Catcher           | 72.723684  | 204.328947 | 76       |
| Designated_Hitter | 74.222222  | 220.888889 | 18       |
| First_Baseman     | 74.000000  | 213.109091 | 55       |
| Outfielder        | 73.010309  | 199.113402 | 194      |
| Relief_Pitcher    | 74.374603  | 203.517460 | 315      |
| Second_Baseman    | 71.362069  | 184.344828 | 58       |
| Shortstop         | 71.903846  | 182.923077 | 52       |
| Starting_Pitcher  | 74.719457  | 205.163636 | 221      |
| Third_Baseman     | 73.044444  | 200.955556 | 45       |

Podemos notar que a média das alturas dos jogadores de primeira base é maior do que a dos jogadores de segunda base. Assim, podemos ser tentados a concluir que **jogadores de primeira base são mais altos do que jogadores de segunda base**.

> Essa afirmação é chamada de **hipótese**, porque não sabemos se o fato é realmente verdadeiro ou não.

No entanto, nem sempre é óbvio se podemos fazer essa conclusão. Pela discussão acima, sabemos que cada média tem um intervalo de confiança associado e, portanto, essa diferença pode ser apenas um erro estatístico. Precisamos de uma maneira mais formal de testar nossa hipótese.

Vamos calcular os intervalos de confiança separadamente para as alturas dos jogadores de primeira e segunda base:

| Confiança | Primeira Base | Segunda Base |
|-----------|---------------|--------------|
| 0.85      | 73.62..74.38  | 71.04..71.69 |
| 0.90      | 73.56..74.44  | 70.99..71.73 |
| 0.95      | 73.47..74.53  | 70.92..71.81 |

Podemos ver que, sob nenhuma confiança, os intervalos se sobrepõem. Isso prova nossa hipótese de que jogadores de primeira base são mais altos do que jogadores de segunda base.

Mais formalmente, o problema que estamos resolvendo é verificar se **duas distribuições de probabilidade são iguais**, ou pelo menos têm os mesmos parâmetros. Dependendo da distribuição, precisamos usar diferentes testes para isso. Se sabemos que nossas distribuições são normais, podemos aplicar o **[teste t de Student](https://en.wikipedia.org/wiki/Student%27s_t-test)**.

No teste t de Student, calculamos o chamado **valor t**, que indica a diferença entre as médias, levando em conta a variância. É demonstrado que o valor t segue a **distribuição t de Student**, o que nos permite obter o valor limite para um nível de confiança **p** (isso pode ser calculado ou consultado em tabelas numéricas). Em seguida, comparamos o valor t com esse limite para aprovar ou rejeitar a hipótese.

No Python, podemos usar o pacote **SciPy**, que inclui a função `ttest_ind` (além de muitas outras funções estatísticas úteis!). Ela calcula o valor t para nós e também faz a busca reversa do valor de confiança p, para que possamos apenas olhar para a confiança e tirar a conclusão.

Por exemplo, nossa comparação entre as alturas dos jogadores de primeira e segunda base nos dá os seguintes resultados: 
```python
from scipy.stats import ttest_ind

tval, pval = ttest_ind(df.loc[df['Role']=='First_Baseman',['Height']], df.loc[df['Role']=='Designated_Hitter',['Height']],equal_var=False)
print(f"T-value = {tval[0]:.2f}\nP-value: {pval[0]}")
```
```
T-value = 7.65
P-value: 9.137321189738925e-12
```
No nosso caso, o valor p é muito baixo, o que significa que há evidências fortes de que os jogadores de primeira base são mais altos.

Existem também outros tipos de hipóteses que podemos querer testar, por exemplo:
* Provar que uma amostra segue alguma distribuição. No nosso caso, assumimos que as alturas são distribuídas normalmente, mas isso precisa de verificação estatística formal.
* Provar que o valor médio de uma amostra corresponde a algum valor pré-definido.
* Comparar as médias de várias amostras (por exemplo, qual é a diferença nos níveis de felicidade entre diferentes faixas etárias).

## Lei dos Grandes Números e Teorema Central do Limite

Uma das razões pelas quais a distribuição normal é tão importante é o chamado **teorema central do limite**. Suponha que temos uma grande amostra de N valores independentes X<sub>1</sub>, ..., X<sub>N</sub>, amostrados de qualquer distribuição com média μ e variância σ<sup>2</sup>. Então, para N suficientemente grande (em outras palavras, quando N→∞), a média Σ<sub>i</sub>X<sub>i</sub> seria normalmente distribuída, com média μ e variância σ<sup>2</sup>/N.

> Outra maneira de interpretar o teorema central do limite é dizer que, independentemente da distribuição, ao calcular a média de uma soma de valores de variáveis aleatórias, você acaba com uma distribuição normal.

Do teorema central do limite também segue que, quando N→∞, a probabilidade de a média da amostra ser igual a μ torna-se 1. Isso é conhecido como **a lei dos grandes números**.

## Covariância e Correlação

Uma das coisas que a Ciência de Dados faz é encontrar relações entre dados. Dizemos que duas sequências **correlacionam** quando exibem comportamento semelhante ao mesmo tempo, ou seja, elas sobem/descem simultaneamente, ou uma sequência sobe quando outra cai e vice-versa. Em outras palavras, parece haver alguma relação entre duas sequências.

> Correlação não indica necessariamente uma relação causal entre duas sequências; às vezes, ambas as variáveis podem depender de alguma causa externa, ou pode ser puramente por acaso que as duas sequências se correlacionam. No entanto, uma correlação matemática forte é uma boa indicação de que duas variáveis estão de alguma forma conectadas.

Matematicamente, o principal conceito que mostra a relação entre duas variáveis aleatórias é a **covariância**, que é calculada assim: Cov(X,Y) = **E**\[(X-**E**(X))(Y-**E**(Y))\]. Calculamos o desvio de ambas as variáveis em relação aos seus valores médios e, em seguida, o produto desses desvios. Se ambas as variáveis se desviam juntas, o produto será sempre um valor positivo, que se somará a uma covariância positiva. Se ambas as variáveis se desviam fora de sincronia (ou seja, uma cai abaixo da média quando outra sobe acima da média), sempre obteremos números negativos, que se somarão a uma covariância negativa. Se os desvios não forem dependentes, eles se somarão a aproximadamente zero.

O valor absoluto da covariância não nos diz muito sobre o quão grande é a correlação, porque depende da magnitude dos valores reais. Para normalizá-lo, podemos dividir a covariância pelo desvio padrão de ambas as variáveis, para obter a **correlação**. A vantagem é que a correlação está sempre no intervalo de [-1,1], onde 1 indica forte correlação positiva entre os valores, -1 - forte correlação negativa, e 0 - nenhuma correlação (variáveis independentes).

**Exemplo**: Podemos calcular a correlação entre pesos e alturas dos jogadores de beisebol do conjunto de dados mencionado acima:
```python
print(np.corrcoef(weights,heights))
```
Como resultado, obtemos uma **matriz de correlação** como esta:
```
array([[1.        , 0.52959196],
       [0.52959196, 1.        ]])
```

> A matriz de correlação C pode ser calculada para qualquer número de sequências de entrada S<sub>1</sub>, ..., S<sub>n</sub>. O valor de C<sub>ij</sub> é a correlação entre S<sub>i</sub> e S<sub>j</sub>, e os elementos diagonais são sempre 1 (que também é a autocorrelação de S<sub>i</sub>).

No nosso caso, o valor 0.53 indica que há alguma correlação entre o peso e a altura de uma pessoa. Também podemos fazer o gráfico de dispersão de um valor contra o outro para ver a relação visualmente:

![Relação entre peso e altura](../../../../translated_images/weight-height-relationship.3f06bde4ca2aba9974182c4ef037ed602acd0fbbbbe2ca91cefd838a9e66bcf9.br.png)

> Mais exemplos de correlação e covariância podem ser encontrados no [notebook complementar](notebook.ipynb).

## Conclusão

Nesta seção, aprendemos:

* propriedades estatísticas básicas dos dados, como média, variância, moda e quartis
* diferentes distribuições de variáveis aleatórias, incluindo a distribuição normal
* como encontrar correlação entre diferentes propriedades
* como usar o aparato matemático e estatístico para provar algumas hipóteses
* como calcular intervalos de confiança para variáveis aleatórias com base em amostras de dados

Embora esta lista definitivamente não seja exaustiva dos tópicos que existem dentro de probabilidade e estatística, ela deve ser suficiente para dar um bom início neste curso.

## 🚀 Desafio

Use o código de exemplo no notebook para testar outras hipóteses:
1. Jogadores de primeira base são mais velhos do que jogadores de segunda base.
2. Jogadores de primeira base são mais altos do que jogadores de terceira base.
3. Shortstops são mais altos do que jogadores de segunda base.

## [Quiz pós-aula](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/7)

## Revisão e Autoestudo

Probabilidade e estatística é um tópico tão amplo que merece seu próprio curso. Se você estiver interessado em aprofundar na teoria, pode querer continuar lendo alguns dos seguintes livros:

1. [Carlos Fernandez-Granda](https://cims.nyu.edu/~cfgranda/) da Universidade de Nova York tem ótimos apontamentos [Probability and Statistics for Data Science](https://cims.nyu.edu/~cfgranda/pages/stuff/probability_stats_for_DS.pdf) (disponível online).
1. [Peter e Andrew Bruce. Practical Statistics for Data Scientists.](https://www.oreilly.com/library/view/practical-statistics-for/9781491952955/) [[código de exemplo em R](https://github.com/andrewgbruce/statistics-for-data-scientists)].
1. [James D. Miller. Statistics for Data Science](https://www.packtpub.com/product/statistics-for-data-science/9781788290678) [[código de exemplo em R](https://github.com/PacktPublishing/Statistics-for-Data-Science)].

## Tarefa

[Pequeno Estudo sobre Diabetes](assignment.md)

## Créditos

Esta lição foi criada com ♥️ por [Dmitry Soshnikov](http://soshnikov.com)

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.