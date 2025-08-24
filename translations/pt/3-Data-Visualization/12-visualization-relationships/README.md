<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cad419b574d5c35eaa417e9abfdcb0c8",
  "translation_date": "2025-08-24T01:04:10+00:00",
  "source_file": "3-Data-Visualization/12-visualization-relationships/README.md",
  "language_code": "pt"
}
-->
# Visualizar Relações: Tudo Sobre Mel 🍯

|![ Sketchnote por [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/12-Visualizing-Relationships.png)|
|:---:|
|Visualizar Relações - _Sketchnote por [@nitya](https://twitter.com/nitya)_ |

Continuando com o foco na natureza da nossa pesquisa, vamos descobrir visualizações interessantes para mostrar as relações entre vários tipos de mel, de acordo com um conjunto de dados derivado do [Departamento de Agricultura dos Estados Unidos](https://www.nass.usda.gov/About_NASS/index.php). 

Este conjunto de dados, com cerca de 600 itens, exibe a produção de mel em muitos estados dos EUA. Por exemplo, é possível observar o número de colónias, rendimento por colónia, produção total, stocks, preço por libra e valor do mel produzido num determinado estado entre 1998 e 2012, com uma linha por ano para cada estado.

Será interessante visualizar a relação entre a produção anual de um estado e, por exemplo, o preço do mel nesse estado. Alternativamente, pode-se visualizar a relação entre o rendimento de mel por colónia em diferentes estados. Este período cobre o devastador 'CCD' ou 'Colony Collapse Disorder' (Desordem do Colapso das Colónias), observado pela primeira vez em 2006 (http://npic.orst.edu/envir/ccd.html), tornando este um conjunto de dados comovente para estudar. 🐝

## [Questionário pré-aula](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/22)

Nesta lição, pode usar o Seaborn, que já utilizou anteriormente, como uma boa biblioteca para visualizar relações entre variáveis. Particularmente interessante é o uso da função `relplot` do Seaborn, que permite criar gráficos de dispersão e gráficos de linhas para visualizar rapidamente '[relações estatísticas](https://seaborn.pydata.org/tutorial/relational.html?highlight=relationships)', ajudando o cientista de dados a compreender melhor como as variáveis se relacionam.

## Gráficos de dispersão

Use um gráfico de dispersão para mostrar como o preço do mel evoluiu, ano após ano, por estado. O Seaborn, utilizando `relplot`, agrupa convenientemente os dados por estado e exibe pontos de dados para dados categóricos e numéricos.

Vamos começar por importar os dados e o Seaborn:

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
honey = pd.read_csv('../../data/honey.csv')
honey.head()
```
Repare que os dados sobre o mel têm várias colunas interessantes, incluindo ano e preço por libra. Vamos explorar estes dados, agrupados por estado dos EUA:

| estado | numcol | yieldpercol | totalprod | stocks   | priceperlb | prodvalue | year |
| ------ | ------ | ----------- | --------- | -------- | ---------- | --------- | ---- |
| AL     | 16000  | 71          | 1136000   | 159000   | 0.72       | 818000    | 1998 |
| AZ     | 55000  | 60          | 3300000   | 1485000  | 0.64       | 2112000   | 1998 |
| AR     | 53000  | 65          | 3445000   | 1688000  | 0.59       | 2033000   | 1998 |
| CA     | 450000 | 83          | 37350000  | 12326000 | 0.62       | 23157000  | 1998 |
| CO     | 27000  | 72          | 1944000   | 1594000  | 0.7        | 1361000   | 1998 |

Crie um gráfico de dispersão básico para mostrar a relação entre o preço por libra de mel e o estado de origem nos EUA. Faça com que o eixo `y` seja suficientemente alto para exibir todos os estados:

```python
sns.relplot(x="priceperlb", y="state", data=honey, height=15, aspect=.5);
```
![scatterplot 1](../../../../3-Data-Visualization/12-visualization-relationships/images/scatter1.png)

Agora, mostre os mesmos dados com um esquema de cores de mel para ilustrar como o preço evolui ao longo dos anos. Pode fazer isso adicionando um parâmetro 'hue' para mostrar a mudança, ano após ano:

> ✅ Saiba mais sobre as [paletas de cores que pode usar no Seaborn](https://seaborn.pydata.org/tutorial/color_palettes.html) - experimente um esquema de cores arco-íris bonito!

```python
sns.relplot(x="priceperlb", y="state", hue="year", palette="YlOrBr", data=honey, height=15, aspect=.5);
```
![scatterplot 2](../../../../3-Data-Visualization/12-visualization-relationships/images/scatter2.png)

Com esta mudança no esquema de cores, pode-se perceber claramente uma forte progressão ao longo dos anos no que diz respeito ao preço do mel por libra. De facto, se observar um conjunto de amostras nos dados para verificar (escolha um estado, como o Arizona, por exemplo), pode ver um padrão de aumento de preços ano após ano, com poucas exceções:

| estado | numcol | yieldpercol | totalprod | stocks  | priceperlb | prodvalue | year |
| ------ | ------ | ----------- | --------- | ------- | ---------- | --------- | ---- |
| AZ     | 55000  | 60          | 3300000   | 1485000 | 0.64       | 2112000   | 1998 |
| AZ     | 52000  | 62          | 3224000   | 1548000 | 0.62       | 1999000   | 1999 |
| AZ     | 40000  | 59          | 2360000   | 1322000 | 0.73       | 1723000   | 2000 |
| AZ     | 43000  | 59          | 2537000   | 1142000 | 0.72       | 1827000   | 2001 |
| AZ     | 38000  | 63          | 2394000   | 1197000 | 1.08       | 2586000   | 2002 |
| AZ     | 35000  | 72          | 2520000   | 983000  | 1.34       | 3377000   | 2003 |
| AZ     | 32000  | 55          | 1760000   | 774000  | 1.11       | 1954000   | 2004 |
| AZ     | 36000  | 50          | 1800000   | 720000  | 1.04       | 1872000   | 2005 |
| AZ     | 30000  | 65          | 1950000   | 839000  | 0.91       | 1775000   | 2006 |
| AZ     | 30000  | 64          | 1920000   | 902000  | 1.26       | 2419000   | 2007 |
| AZ     | 25000  | 64          | 1600000   | 336000  | 1.26       | 2016000   | 2008 |
| AZ     | 20000  | 52          | 1040000   | 562000  | 1.45       | 1508000   | 2009 |
| AZ     | 24000  | 77          | 1848000   | 665000  | 1.52       | 2809000   | 2010 |
| AZ     | 23000  | 53          | 1219000   | 427000  | 1.55       | 1889000   | 2011 |
| AZ     | 22000  | 46          | 1012000   | 253000  | 1.79       | 1811000   | 2012 |

Outra forma de visualizar esta progressão é usar o tamanho, em vez da cor. Para utilizadores daltónicos, esta pode ser uma opção melhor. Edite a sua visualização para mostrar o aumento do preço através do aumento do tamanho dos pontos:

```python
sns.relplot(x="priceperlb", y="state", size="year", data=honey, height=15, aspect=.5);
```
Pode ver o tamanho dos pontos a aumentar gradualmente.

![scatterplot 3](../../../../3-Data-Visualization/12-visualization-relationships/images/scatter3.png)

Será este um caso simples de oferta e procura? Devido a fatores como mudanças climáticas e colapso das colónias, haverá menos mel disponível para compra ano após ano, e, assim, o preço aumenta?

Para descobrir uma correlação entre algumas das variáveis deste conjunto de dados, vamos explorar alguns gráficos de linhas.

## Gráficos de linhas

Pergunta: Há um aumento claro no preço do mel por libra ao longo dos anos? Pode descobrir isso facilmente criando um único gráfico de linhas:

```python
sns.relplot(x="year", y="priceperlb", kind="line", data=honey);
```
Resposta: Sim, com algumas exceções por volta do ano 2003:

![line chart 1](../../../../3-Data-Visualization/12-visualization-relationships/images/line1.png)

✅ Como o Seaborn está a agregar dados numa única linha, ele exibe "as múltiplas medições em cada valor de x, traçando a média e o intervalo de confiança de 95% em torno da média". [Fonte](https://seaborn.pydata.org/tutorial/relational.html). Este comportamento, que consome tempo, pode ser desativado adicionando `ci=None`.

Pergunta: Bem, em 2003 também podemos ver um aumento na oferta de mel? E se observarmos a produção total ao longo dos anos?

```python
sns.relplot(x="year", y="totalprod", kind="line", data=honey);
```

![line chart 2](../../../../3-Data-Visualization/12-visualization-relationships/images/line2.png)

Resposta: Não exatamente. Se observarmos a produção total, parece que ela realmente aumentou nesse ano específico, embora, de forma geral, a quantidade de mel produzido esteja em declínio durante esses anos.

Pergunta: Nesse caso, o que poderia ter causado o aumento no preço do mel por volta de 2003?

Para descobrir isso, pode explorar uma grelha de facetas.

## Grelhas de facetas

As grelhas de facetas pegam numa faceta do seu conjunto de dados (neste caso, pode escolher 'ano' para evitar produzir demasiadas facetas). O Seaborn pode então criar um gráfico para cada uma dessas facetas das coordenadas x e y escolhidas, facilitando a comparação visual. O ano de 2003 destaca-se neste tipo de comparação?

Crie uma grelha de facetas continuando a usar `relplot`, conforme recomendado pela [documentação do Seaborn](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html?highlight=facetgrid#seaborn.FacetGrid).

```python
sns.relplot(
    data=honey, 
    x="yieldpercol", y="numcol",
    col="year", 
    col_wrap=3,
    kind="line"
```
Nesta visualização, pode comparar o rendimento por colónia e o número de colónias ao longo dos anos, lado a lado, com um limite de 3 colunas:

![facet grid](../../../../3-Data-Visualization/12-visualization-relationships/images/facet.png)

Para este conjunto de dados, nada particularmente se destaca em relação ao número de colónias e ao seu rendimento, ano após ano e estado após estado. Há uma forma diferente de procurar uma correlação entre estas duas variáveis?

## Gráficos de linhas duplas

Experimente um gráfico de linhas múltiplas sobrepondo dois gráficos de linhas um sobre o outro, utilizando o 'despine' do Seaborn para remover as margens superior e direita, e usando `ax.twinx` [derivado do Matplotlib](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.twinx.html). O Twinx permite que um gráfico partilhe o eixo x e exiba dois eixos y. Assim, exiba o rendimento por colónia e o número de colónias, sobrepostos:

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

Embora nada salte à vista em torno do ano 2003, isso permite-nos terminar esta lição com uma nota um pouco mais feliz: embora o número de colónias esteja a diminuir no geral, ele está a estabilizar, mesmo que o rendimento por colónia esteja a diminuir.

Força, abelhas, força!

🐝❤️
## 🚀 Desafio

Nesta lição, aprendeu um pouco mais sobre outros usos de gráficos de dispersão e grelhas de linhas, incluindo grelhas de facetas. Desafie-se a criar uma grelha de facetas usando um conjunto de dados diferente, talvez um que tenha usado antes destas lições. Note quanto tempo demora a criar e como precisa de ter cuidado com o número de grelhas que precisa de desenhar usando estas técnicas.
## [Questionário pós-aula](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/23)

## Revisão e Autoestudo

Os gráficos de linhas podem ser simples ou bastante complexos. Faça uma leitura na [documentação do Seaborn](https://seaborn.pydata.org/generated/seaborn.lineplot.html) sobre as várias formas de construí-los. Tente melhorar os gráficos de linhas que criou nesta lição com outros métodos listados na documentação.
## Tarefa

[Explore a colmeia](assignment.md)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original no seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se uma tradução profissional realizada por um humano. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes do uso desta tradução.