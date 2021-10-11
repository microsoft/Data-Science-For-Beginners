# Visualizando Quantidades

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../../sketchnotes/09-Visualizing-Quantities.png)|
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
![Envergadura máxima](../images/max-wingspan.png)

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
![Envergadura com labels (identificadores)](../images/max-wingspan-labels.png)

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

![outliers](../images/labeled-wingspan.png)

## Filtrar seus dados

Apesar de grandes, tanto a Bald Eagle e o Prairie Falcon parecem ter valores errados, com um `0` a mais na envergadura máxima. É imporvável que você encontra uma Bald Eagle com envergadura de 25 metros, mas, se encontrar, por favor nos diga! Agora, vamos criar um novo dataframe sem esses dois outliers:

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

Ao remover esses outliers, seus dados ficaram mais coesos e compreensíveis.

![Dispersão das envergaduras](../images/scatterplot-wingspan.png)

Agora que temos um dataset mais limpo ao menos em termos de envergadura, vamos aprender mais sobre esses pássaros

Enquanto gráficos de linha e dispersão conseguem mostrar informações sobre valores e suas distribuições, nós queremos pensar sobre os valores intrínsecos a esse dataset. Você poderia criar visualizações para responder as seguintes perguntas sobre quantidade:

> Quantas categorias de pássaros existem, e quais são seus números?
> Quantos pássaros estão extintos, em risco de extinção, raros ou comuns?
> Quantos gêneros e ordens da taxonomia de Lineu (nome científico) existem no dataset?

## Explorar gráfico de barras

Gráfico de barras são práticos quando se precisa mostrar agrupamentos de dados. Vamos explorar as categorias de pássaros que existem nesse dataset para obrservar qual é o mais comum em quantidade.

No arquivo notebook, crie um gráfico de barras simples

✅ Note que, você pode remover os dois pássaros outliers que foram identificados anteriormente, editar o erro de digitação na envergadura ou deixá-los nesses exercícios que não dependem dos valores da envergadura.

Se você quer criar um gráfico de barras, você pode selecionar os dados que quer focar. Gráfico de barras pode ser criado a partir de dados brutos:

```python
birds.plot(x='Category',
        kind='bar',
        stacked=True,
        title='Birds of Minnesota')

```
![full data as a bar chart](../images/full-data-bar.png)

No entanto, esse gráfico de barras é ilegível porque existem muitos dados não agrupados. Você precisa selecionar somente os dados que quer plotar, então vamos olhar o comprimento de pássaros com base na sua categoria.

Filtre os dados para incluir somente a categoria do pássaro.

✅ Note que você usa o Pandas para lidar com os dados, e deixa a criação de gráficos para o Matplotlib.

Já que existem muitas categorias, você pode mostrar esse gráfico verticalmente e ajustar sua altura para acomodar todos os dados:

```python
category_count = birds.value_counts(birds['Category'].values, sort=True)
plt.rcParams['figure.figsize'] = [6, 12]
category_count.plot.barh()
```
![category and length](../images/category-counts.png)

Esse gráfico de barras mostra uma boa visão do número de pássaros em cada categoria. Em um piscar de olhos, você vê que a maior quantidade de pássaros nessa região pertence à categoria de Ducks/Geese/Waterfowl (patos/gansos/cisnes). Minnesota é 'a terra de 10.000 lagos', então isso não é surpreendente!

✅ Tente contar outras quantidades nesse dataset. Algo te surpreende?

## Comparando dados

Você pode tentar diferentes comparações de dados agrupados criando novos eixos. Tente comparar o comprimento máximo de um pássaro, baseado na sua categoria:

```python
maxlength = birds['MaxLength']
plt.barh(y=birds['Category'], width=maxlength)
plt.rcParams['figure.figsize'] = [6, 12]
plt.show()
```
![comparing data](../images/category-length.png)

Nada é surpreendente aqui: hummingbirds (beija-flores) tem o menor comprimento comparados com pelicans (pelicanos) ou geese (gansos). É muito bom quando os dados fazem sentido!

Você pode criar visualizações mais interessantes de gráficos de barras ao sobrepor dados. Vamos sobrepor o comprimento mínimo e máximo de uma dada categoria de pássaros:

```python
minLength = birds['MinLength']
maxLength = birds['MaxLength']
category = birds['Category']

plt.barh(category, maxLength)
plt.barh(category, minLength)

plt.show()
```

Nesse gráfico, você pode ver o intervalo de comprimento mínimo e máximo por categoria de pássaro. Você pode seguramente dizer, a partir desses dados, que quanto maior o pássaro, maior seu intervalo de comprimento. Fascinante!

![superimposed values](../images/superimposed.png)

## 🚀 Desafio

Esse dataset de pássaros oferece uma riqueza de informações sobre os diferentes tipos de pássaros de um ecossistema particular. Tente achar na internet outros datasets com dados sobre pássaros. Pratique construir gráficos sobre esses pássaros e tente descobrir fatos que você ainda não havia percebido.

## [Quiz pós-aula](https://red-water-0103e7a0f.azurestaticapps.net/quiz/17)

## Revisão e autoestudo

Essa primeira aula lhe deu informações sobre como usar o Matplotlib para visualizar quantidades. Procure por outras formas de trabalhar com dataset para visualização. [Plotly](https://github.com/plotly/plotly.py) é uma que não será abordada nas aulas, então dê uma olhada no que ela pode oferecer.

## Tarefa

[Lines, Scatters, and Bars](assignment.md)
