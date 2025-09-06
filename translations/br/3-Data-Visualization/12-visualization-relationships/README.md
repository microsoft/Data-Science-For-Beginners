<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "44de95649fcec43643cbe3962f904331",
  "translation_date": "2025-09-06T08:33:37+00:00",
  "source_file": "3-Data-Visualization/12-visualization-relationships/README.md",
  "language_code": "br"
}
-->
# Visualizando Relações: Tudo Sobre Mel 🍯

|![ Sketchnote por [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/12-Visualizing-Relationships.png)|
|:---:|
|Visualizando Relações - _Sketchnote por [@nitya](https://twitter.com/nitya)_ |

Continuando com o foco na natureza em nossa pesquisa, vamos descobrir visualizações interessantes para mostrar as relações entre vários tipos de mel, de acordo com um conjunto de dados derivado do [Departamento de Agricultura dos Estados Unidos](https://www.nass.usda.gov/About_NASS/index.php).

Este conjunto de dados, com cerca de 600 itens, exibe a produção de mel em muitos estados dos EUA. Por exemplo, você pode observar o número de colônias, rendimento por colônia, produção total, estoques, preço por libra e valor do mel produzido em um determinado estado de 1998 a 2012, com uma linha por ano para cada estado.

Será interessante visualizar a relação entre a produção anual de um estado e, por exemplo, o preço do mel nesse estado. Alternativamente, você poderia visualizar a relação entre o rendimento de mel por colônia nos estados. Este período cobre o devastador 'CCD' ou 'Colony Collapse Disorder' (Desordem do Colapso das Colônias), observado pela primeira vez em 2006 (http://npic.orst.edu/envir/ccd.html), tornando este conjunto de dados especialmente relevante para estudo. 🐝

## [Quiz pré-aula](https://ff-quizzes.netlify.app/en/ds/quiz/22)

Nesta lição, você pode usar o Seaborn, que já utilizou antes, como uma boa biblioteca para visualizar relações entre variáveis. Particularmente interessante é o uso da função `relplot` do Seaborn, que permite criar gráficos de dispersão e gráficos de linha para visualizar rapidamente '[relações estatísticas](https://seaborn.pydata.org/tutorial/relational.html?highlight=relationships)', ajudando o cientista de dados a entender melhor como as variáveis se relacionam.

## Gráficos de Dispersão

Use um gráfico de dispersão para mostrar como o preço do mel evoluiu ano após ano, por estado. O Seaborn, usando `relplot`, agrupa convenientemente os dados dos estados e exibe pontos de dados para dados categóricos e numéricos.

Vamos começar importando os dados e o Seaborn:

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
honey = pd.read_csv('../../data/honey.csv')
honey.head()
```
Você percebe que os dados de mel possuem várias colunas interessantes, incluindo ano e preço por libra. Vamos explorar esses dados, agrupados por estado dos EUA:

| estado | numcol | rendimento_por_col | produção_total | estoques | preço_por_libra | valor_prod | ano |
| ------ | ------ | ------------------ | -------------- | -------- | ---------------- | ---------- | --- |
| AL     | 16000  | 71                 | 1136000        | 159000   | 0.72             | 818000     | 1998 |
| AZ     | 55000  | 60                 | 3300000        | 1485000  | 0.64             | 2112000    | 1998 |
| AR     | 53000  | 65                 | 3445000        | 1688000  | 0.59             | 2033000    | 1998 |
| CA     | 450000 | 83                 | 37350000       | 12326000 | 0.62             | 23157000   | 1998 |
| CO     | 27000  | 72                 | 1944000        | 1594000  | 0.7              | 1361000    | 1998 |

Crie um gráfico de dispersão básico para mostrar a relação entre o preço por libra de mel e seu estado de origem nos EUA. Ajuste o eixo `y` para ser alto o suficiente para exibir todos os estados:

```python
sns.relplot(x="priceperlb", y="state", data=honey, height=15, aspect=.5);
```
![scatterplot 1](../../../../3-Data-Visualization/12-visualization-relationships/images/scatter1.png)

Agora, mostre os mesmos dados com um esquema de cores de mel para ilustrar como o preço evolui ao longo dos anos. Você pode fazer isso adicionando um parâmetro 'hue' para mostrar a mudança ano após ano:

> ✅ Saiba mais sobre as [paletas de cores que você pode usar no Seaborn](https://seaborn.pydata.org/tutorial/color_palettes.html) - experimente um belo esquema de cores em arco-íris!

```python
sns.relplot(x="priceperlb", y="state", hue="year", palette="YlOrBr", data=honey, height=15, aspect=.5);
```
![scatterplot 2](../../../../3-Data-Visualization/12-visualization-relationships/images/scatter2.png)

Com essa mudança de esquema de cores, você pode ver claramente uma forte progressão ao longo dos anos no preço do mel por libra. De fato, ao verificar um conjunto de amostra nos dados (escolha um estado, como o Arizona, por exemplo), é possível observar um padrão de aumento de preço ano após ano, com poucas exceções:

| estado | numcol | rendimento_por_col | produção_total | estoques | preço_por_libra | valor_prod | ano |
| ------ | ------ | ------------------ | -------------- | -------- | ---------------- | ---------- | --- |
| AZ     | 55000  | 60                 | 3300000        | 1485000  | 0.64             | 2112000    | 1998 |
| AZ     | 52000  | 62                 | 3224000        | 1548000  | 0.62             | 1999000    | 1999 |
| AZ     | 40000  | 59                 | 2360000        | 1322000  | 0.73             | 1723000    | 2000 |
| AZ     | 43000  | 59                 | 2537000        | 1142000  | 0.72             | 1827000    | 2001 |
| AZ     | 38000  | 63                 | 2394000        | 1197000  | 1.08             | 2586000    | 2002 |
| AZ     | 35000  | 72                 | 2520000        | 983000   | 1.34             | 3377000    | 2003 |
| AZ     | 32000  | 55                 | 1760000        | 774000   | 1.11             | 1954000    | 2004 |
| AZ     | 36000  | 50                 | 1800000        | 720000   | 1.04             | 1872000    | 2005 |
| AZ     | 30000  | 65                 | 1950000        | 839000   | 0.91             | 1775000    | 2006 |
| AZ     | 30000  | 64                 | 1920000        | 902000   | 1.26             | 2419000    | 2007 |
| AZ     | 25000  | 64                 | 1600000        | 336000   | 1.26             | 2016000    | 2008 |
| AZ     | 20000  | 52                 | 1040000        | 562000   | 1.45             | 1508000    | 2009 |
| AZ     | 24000  | 77                 | 1848000        | 665000   | 1.52             | 2809000    | 2010 |
| AZ     | 23000  | 53                 | 1219000        | 427000   | 1.55             | 1889000    | 2011 |
| AZ     | 22000  | 46                 | 1012000        | 253000   | 1.79             | 1811000    | 2012 |

Outra maneira de visualizar essa progressão é usar tamanho, em vez de cor. Para usuários com daltonismo, isso pode ser uma opção melhor. Edite sua visualização para mostrar o aumento do preço por meio do aumento na circunferência dos pontos:

```python
sns.relplot(x="priceperlb", y="state", size="year", data=honey, height=15, aspect=.5);
```
Você pode ver o tamanho dos pontos aumentando gradualmente.

![scatterplot 3](../../../../3-Data-Visualization/12-visualization-relationships/images/scatter3.png)

Isso é um caso simples de oferta e demanda? Devido a fatores como mudanças climáticas e colapso das colônias, há menos mel disponível para compra ano após ano, e, portanto, o preço aumenta?

Para descobrir uma correlação entre algumas das variáveis neste conjunto de dados, vamos explorar alguns gráficos de linha.

## Gráficos de Linha

Pergunta: Há um aumento claro no preço do mel por libra ano após ano? Você pode descobrir isso mais facilmente criando um único gráfico de linha:

```python
sns.relplot(x="year", y="priceperlb", kind="line", data=honey);
```
Resposta: Sim, com algumas exceções por volta do ano de 2003:

![line chart 1](../../../../3-Data-Visualization/12-visualization-relationships/images/line1.png)

✅ Como o Seaborn está agregando dados em torno de uma linha, ele exibe "as múltiplas medições em cada valor de x, plotando a média e o intervalo de confiança de 95% ao redor da média". [Fonte](https://seaborn.pydata.org/tutorial/relational.html). Esse comportamento que consome tempo pode ser desativado adicionando `ci=None`.

Pergunta: Bem, em 2003 também podemos ver um aumento na oferta de mel? E se você observar a produção total ano após ano?

```python
sns.relplot(x="year", y="totalprod", kind="line", data=honey);
```

![line chart 2](../../../../3-Data-Visualization/12-visualization-relationships/images/line2.png)

Resposta: Não exatamente. Se você observar a produção total, parece que ela realmente aumentou naquele ano específico, embora, de forma geral, a quantidade de mel produzida esteja em declínio durante esses anos.

Pergunta: Nesse caso, o que poderia ter causado o aumento no preço do mel por volta de 2003?

Para descobrir isso, você pode explorar uma grade de facetas.

## Grades de Facetas

Grades de facetas pegam um aspecto do seu conjunto de dados (neste caso, você pode escolher 'ano' para evitar produzir muitas facetas). O Seaborn pode então criar um gráfico para cada uma dessas facetas de suas coordenadas x e y escolhidas, facilitando a comparação visual. O ano de 2003 se destaca nesse tipo de comparação?

Crie uma grade de facetas continuando a usar `relplot`, conforme recomendado pela [documentação do Seaborn](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html?highlight=facetgrid#seaborn.FacetGrid).

```python
sns.relplot(
    data=honey, 
    x="yieldpercol", y="numcol",
    col="year", 
    col_wrap=3,
    kind="line"
```
Nesta visualização, você pode comparar o rendimento por colônia e o número de colônias ano após ano, lado a lado, com um wrap definido em 3 para as colunas:

![facet grid](../../../../3-Data-Visualization/12-visualization-relationships/images/facet.png)

Para este conjunto de dados, nada particularmente se destaca em relação ao número de colônias e seu rendimento, ano após ano e estado por estado. Existe uma maneira diferente de encontrar uma correlação entre essas duas variáveis?

## Gráficos de Linha Dupla

Experimente um gráfico de linha múltipla superpondo dois gráficos de linha um sobre o outro, usando o 'despine' do Seaborn para remover as bordas superior e direita, e usando `ax.twinx` [derivado do Matplotlib](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.twinx.html). Twinx permite que um gráfico compartilhe o eixo x e exiba dois eixos y. Então, exiba o rendimento por colônia e o número de colônias, superpostos:

```python
fig, ax = plt.subplots(figsize=(12,6))
lineplot = sns.lineplot(x=honey['year'], y=honey['numcol'], data=honey, 
                        label = 'Number of bee colonies', legend=False)
sns.despine()
plt.ylabel('# colonies')
plt.title('Honey Production Year over Year');

ax2 = ax.twinx()
lineplot2 = sns.lineplot(x=honey['year'], y=honey['yieldpercol'], ax=ax2, color="r", 
                         label ='Yield per colony', legend=False) 
sns.despine(right=False)
plt.ylabel('colony yield')
ax.figure.legend();
```
![superimposed plots](../../../../3-Data-Visualization/12-visualization-relationships/images/dual-line.png)

Embora nada salte aos olhos em torno do ano de 2003, isso nos permite terminar esta lição com uma nota um pouco mais feliz: embora o número de colônias esteja em declínio geral, ele está se estabilizando, mesmo que o rendimento por colônia esteja diminuindo.

Vai, abelhas, vai!

🐝❤️
## 🚀 Desafio

Nesta lição, você aprendeu um pouco mais sobre outros usos de gráficos de dispersão e grades de linha, incluindo grades de facetas. Desafie-se a criar uma grade de facetas usando um conjunto de dados diferente, talvez um que você tenha usado antes dessas lições. Observe quanto tempo elas levam para serem criadas e como você precisa ter cuidado com a quantidade de grades que deseja desenhar usando essas técnicas.

## [Quiz pós-aula](https://ff-quizzes.netlify.app/en/ds/quiz/23)

## Revisão & Autoestudo

Gráficos de linha podem ser simples ou bastante complexos. Leia um pouco na [documentação do Seaborn](https://seaborn.pydata.org/generated/seaborn.lineplot.html) sobre as várias maneiras de construí-los. Tente aprimorar os gráficos de linha que você criou nesta lição com outros métodos listados na documentação.

## Tarefa

[Explore a colmeia](assignment.md)

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução profissional feita por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.