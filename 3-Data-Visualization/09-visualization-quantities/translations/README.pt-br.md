# Visualizando Quantidades

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/09-Visualizing-Quantities.png)|
|:---:|
| Visualizando quantidades - _Sketchnote por [@nitya](https://twitter.com/nitya)_ |

Nessa aula você irá explorar como usar uma das muitas bibliotecas disponíveis de Python para aprender a criar visualizações interessantes relacionadas ao conceito de quantidade. Usando um dataset já limpo sobre pássaros de Minnesota, você pode aprender muitos fatos interessantes sobre a fauna selvagem local.
## [Quiz pré-aula](https://red-water-0103e7a0f.azurestaticapps.net/quiz/16)

## Observar envergadura de asa com Matplotlib

Uma biblioteca excelente para criar gráficos simples e sofisticados de diversos tipos é o [Matplotlib](https://matplotlib.org/stable/index.html). Em geral, o processo de plotar dados com essas bibliotecas inclui identificar as partes do seu dataframe que você quer focar, utilizando quaisquer transformações necessárias nestes dados, atribuindo seus valores dos eixos x e y, decidindo qual tipo de gráfico mostrar, e então mostrando o gráfico. O Matplotlib oferece uma grande variedade de visualizações, mas, nesta aula, iremos focar nos mais apropriados para visualizar quantidade: gráfico de linha, gráfico de dispersão e gráfico de barra.

> ✅ Use o melhor gráfico para se adaptar a estrutura dos dados e a história que você quer contar.
> - Para analisar tendências ao longo do tempo: linha
> - Para comparar valores: barra, coluna, pizza, dispersão
> - Para mostrar como as partes se relacionam com o todo: pizza
> - Para mostrar a distrivuição dos dados: dispersão, barra
> - Para mostrar tendências: linha, coluna
> - Para mostrar relações entre valores: linha, dispersão, bolha

Se você tem um dataset e precisa descobrir quanto de um dado item está presente, uma das primeiras coisas que você precisará fazer é examinar seus valores.


✅ Existem dicas ('cheat sheets') muito boas disponíveis para o Matplotlib [aqui](https://github.com/matplotlib/cheatsheets/blob/master/cheatsheets-1.png) e [aqui](https://github.com/matplotlib/cheatsheets/blob/master/cheatsheets-2.png).

## Construir um gráfico de linhas sobre os valores de envergadura de pássaros

Abra o arquivo `notebook.ipynb` na raiz da pasta dessa aula e adicione uma célula.

> Nota: os dados estão armazenados na raiz deste repositório na pasta `/data`.

```python
import pandas as pd
import matplotlib.pyplot as plt
birds = pd.read_csv('../../data/birds.csv')
birds.head()
```
Esses dados são uma mistura de texto e números:


|      | Name                         | ScientificName         | Category              | Order        | Family   | Genus       | ConservationStatus | MinLength | MaxLength | MinBodyMass | MaxBodyMass | MinWingspan | MaxWingspan |
| ---: | :--------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :----------------- | --------: | --------: | ----------: | ----------: | ----------: | ----------: |
|    0 | Black-bellied whistling-duck | Dendrocygna autumnalis | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Dendrocygna | LC                 |        47 |        56 |         652 |        1020 |          76 |          94 |
|    1 | Fulvous whistling-duck       | Dendrocygna bicolor    | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Dendrocygna | LC                 |        45 |        53 |         712 |        1050 |          85 |          93 |
|    2 | Snow goose                   | Anser caerulescens     | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Anser       | LC                 |        64 |        79 |        2050 |        4050 |         135 |         165 |
|    3 | Ross's goose                 | Anser rossii           | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Anser       | LC                 |      57.3 |        64 |        1066 |        1567 |         113 |         116 |
|    4 | Greater white-fronted goose  | Anser albifrons        | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Anser       | LC                 |        64 |        81 |        1930 |        3310 |         130 |         165 |

Vamos começar plotando alguns dados numéricos com um simples gráfico de linhas. Suponha que você quer uma visualização da envergadura máxima desses pássaros interessantes.

```python
wingspan = birds['MaxWingspan'] 
wingspan.plot()
```
![Envergadura máxima](images/max-wingspan.png)

O que é possível perceber imediatamente? Aparentemente existe pelo menos um outlier - e que envergadura! Uma envergadura de 2300 centímetros equivale a 23 metros - têm pterodáctilos voando em Minnesota? Vamos investigar.

Você poderia fazer uma ordenação rápida no Excel para encontrar esses outliers, que provavelmente são erros de digitação. No entanto, vamos continuar o processo de visualização trabalhando no gráfico.

Adicione labels (identificadores) no eixo x para mostrar quais tipos de pássaros estão sendo analisados:

```
plt.title('Max Wingspan in Centimeters')
plt.ylabel('Wingspan (CM)')
plt.xlabel('Birds')
plt.xticks(rotation=45)
x = birds['Name'] 
y = birds['MaxWingspan']

plt.plot(x, y)

plt.show()
```
![Envergadura com labels (identificadores)](images/max-wingspan-labels.png)

Mesmo com a rotação das labels em 45 graus, existem muitos para ler. Vamos tentar outra estratégia: identificar somente os outliers e colocar as labels dentro do gráfico. Você pode usarj um gráfico de dispersão para abrir mais espaço para identificação:

```python
plt.title('Max Wingspan in Centimeters')
plt.ylabel('Wingspan (CM)')
plt.tick_params(axis='both',which='both',labelbottom=False,bottom=False)

for i in range(len(birds)):
    x = birds['Name'][i]
    y = birds['MaxWingspan'][i]
    plt.plot(x, y, 'bo')
    if birds['MaxWingspan'][i] > 500:
        plt.text(x, y * (1 - 0.05), birds['Name'][i], fontsize=12)
    
plt.show()
```

O que aconteceu aqui? Você usou `tick_params` para esconder as labels debaixo e entrão criou um loop sobre o dataset dos paśsaros. Depois, plotou o gráfico com pequenos círculos azuis usando `bo` e procurou por pássaros com envergadura maior que 500 e, se sim, exibiu a label ao lado do círculo. Você ajustou as labels no eixo y (`y * (1 - 0.05)`) e usou o nome do pássaro como label.

O que você descobriu?

![outliers](images/labeled-wingspan.png)

## Filtrar seus dados

Both the Bald Eagle and the Prairie Falcon, while probably very large birds, appear to be mislabeled, with an extra `0` added to their maximum wingspan. It's unlikely that you'll meet a Bald Eagle with a 25 meter wingspan, but if so, please let us know! Let's create a new dataframe without those two outliers:

```python
plt.title('Max Wingspan in Centimeters')
plt.ylabel('Wingspan (CM)')
plt.xlabel('Birds')
plt.tick_params(axis='both',which='both',labelbottom=False,bottom=False)
for i in range(len(birds)):
    x = birds['Name'][i]
    y = birds['MaxWingspan'][i]
    if birds['Name'][i] not in ['Bald eagle', 'Prairie falcon']:
        plt.plot(x, y, 'bo')
plt.show()
```

By filtering out outliers, your data is now more cohesive and understandable.

![scatterplot of wingspans](images/scatterplot-wingspan.png)

Now that we have a cleaner dataset at least in terms of wingspan, let's discover more about these birds.

While line and scatter plots can display information about data values and their distributions, we want to think about the values inherent in this dataset. You could create visualizations to answer the following questions about quantity:

> How many categories of birds are there, and what are their numbers?
> How many birds are extinct, endangered, rare, or common?
> How many are there of the various genus and orders in Linnaeus's terminology?
## Explore bar charts

Bar charts are practical when you need to show groupings of data. Let's explore the categories of birds that exist in this dataset to see which is the most common by number.

In the notebook file, create a basic bar chart

✅ Note, you can either filter out the two outlier birds we identified in the previous section, edit the typo in their wingspan, or leave them in for these exercises which do not depend on wingspan values.

If you want to create a bar chart, you can select the data you want to focus on. Bar charts can be created from raw data:

```python
birds.plot(x='Category',
        kind='bar',
        stacked=True,
        title='Birds of Minnesota')

```
![full data as a bar chart](images/full-data-bar.png)

This bar chart, however, is unreadable because there is too much non-grouped data. You need to select only the data that you want to plot, so let's look at the length of birds based on their category. 

Filter your data to include only the bird's category. 

✅ Notice that that you use Pandas to manage the data, and then let Matplotlib do the charting.

Since there are many categories, you can display this chart vertically and tweak its height to account for all the data:

```python
category_count = birds.value_counts(birds['Category'].values, sort=True)
plt.rcParams['figure.figsize'] = [6, 12]
category_count.plot.barh()
```
![category and length](images/category-counts.png)

This bar chart shows a good view of the number of birds in each category. In a blink of an eye, you see that the largest number of birds in this region are in the Ducks/Geese/Waterfowl category. Minnesota is the 'land of 10,000 lakes' so this isn't surprising!

✅ Try some other counts on this dataset. Does anything surprise you?

## Comparing data

You can try different comparisons of grouped data by creating new axes. Try a comparison of the MaxLength of a bird, based on its category:

```python
maxlength = birds['MaxLength']
plt.barh(y=birds['Category'], width=maxlength)
plt.rcParams['figure.figsize'] = [6, 12]
plt.show()
```
![comparing data](images/category-length.png)

Nothing is surprising here: hummingbirds have the least MaxLength compared to Pelicans or Geese. It's good when data makes logical sense!

You can create more interesting visualizations of bar charts by superimposing data. Let's superimpose Minimum and Maximum Length on a given bird category:

```python
minLength = birds['MinLength']
maxLength = birds['MaxLength']
category = birds['Category']

plt.barh(category, maxLength)
plt.barh(category, minLength)

plt.show()
```
In this plot, you can see the range per bird category of the Minimum Length and Maximum length. You can safely say that, given this data, the bigger the bird, the larger its length range. Fascinating!

![superimposed values](images/superimposed.png)

## 🚀 Challenge

This bird dataset offers a wealth of information about different types of birds within a particular ecosystem. Search around the internet and see if you can find other bird-oriented datasets. Practice building charts and graphs around these birds to discover facts you didn't realize.
## [Post-lecture quiz](https://red-water-0103e7a0f.azurestaticapps.net/quiz/17)

## Review & Self Study

This first lesson has given you some information about how to use Matplotlib to visualize quantities. Do some research around other ways to work with datasets for visualization. [Plotly](https://github.com/plotly/plotly.py) is one that we won't cover in these lessons, so take a look at what it can offer.
## Assignment

[Lines, Scatters, and Bars](assignment.md)
