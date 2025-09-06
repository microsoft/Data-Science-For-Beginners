<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "80a20467e046d312809d008395051fc7",
  "translation_date": "2025-09-06T08:34:05+00:00",
  "source_file": "3-Data-Visualization/10-visualization-distributions/README.md",
  "language_code": "br"
}
-->
# Visualizando Distribuições

|![ Sketchnote por [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/10-Visualizing-Distributions.png)|
|:---:|
| Visualizando Distribuições - _Sketchnote por [@nitya](https://twitter.com/nitya)_ |

Na lição anterior, você aprendeu alguns fatos interessantes sobre um conjunto de dados sobre os pássaros de Minnesota. Você encontrou alguns dados errôneos ao visualizar outliers e analisou as diferenças entre categorias de pássaros com base no comprimento máximo.

## [Quiz pré-aula](https://ff-quizzes.netlify.app/en/ds/quiz/18)
## Explore o conjunto de dados dos pássaros

Outra maneira de explorar os dados é analisando sua distribuição, ou como os dados estão organizados ao longo de um eixo. Talvez, por exemplo, você queira aprender sobre a distribuição geral, para este conjunto de dados, da envergadura máxima ou da massa corporal máxima dos pássaros de Minnesota.

Vamos descobrir alguns fatos sobre as distribuições de dados neste conjunto de dados. No arquivo _notebook.ipynb_ na raiz da pasta desta lição, importe Pandas, Matplotlib e seus dados:

```python
import pandas as pd
import matplotlib.pyplot as plt
birds = pd.read_csv('../../data/birds.csv')
birds.head()
```

|      | Nome                         | NomeCientífico         | Categoria              | Ordem        | Família   | Gênero       | StatusConservação | ComprimentoMin | ComprimentoMax | MassaCorporalMin | MassaCorporalMax | EnvergaduraMin | EnvergaduraMax |
| ---: | :--------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :----------------- | --------: | --------: | ----------: | ----------: | ----------: | ----------: |
|    0 | Pato-silvo-de-barriga-preta  | Dendrocygna autumnalis | Patos/Gansos/AvesAquáticas | Anseriformes | Anatidae | Dendrocygna | LC                 |        47 |        56 |         652 |        1020 |          76 |          94 |
|    1 | Pato-silvo-ferrugem          | Dendrocygna bicolor    | Patos/Gansos/AvesAquáticas | Anseriformes | Anatidae | Dendrocygna | LC                 |        45 |        53 |         712 |        1050 |          85 |          93 |
|    2 | Ganso-da-neve                | Anser caerulescens     | Patos/Gansos/AvesAquáticas | Anseriformes | Anatidae | Anser       | LC                 |        64 |        79 |        2050 |        4050 |         135 |         165 |
|    3 | Ganso-de-Ross                | Anser rossii           | Patos/Gansos/AvesAquáticas | Anseriformes | Anatidae | Anser       | LC                 |      57.3 |        64 |        1066 |        1567 |         113 |         116 |
|    4 | Ganso-de-testa-branca-maior  | Anser albifrons        | Patos/Gansos/AvesAquáticas | Anseriformes | Anatidae | Anser       | LC                 |        64 |        81 |        1930 |        3310 |         130 |         165 |

Em geral, você pode rapidamente observar como os dados estão distribuídos usando um gráfico de dispersão, como fizemos na lição anterior:

```python
birds.plot(kind='scatter',x='MaxLength',y='Order',figsize=(12,8))

plt.title('Max Length per Order')
plt.ylabel('Order')
plt.xlabel('Max Length')

plt.show()
```
![comprimento máximo por ordem](../../../../3-Data-Visualization/10-visualization-distributions/images/scatter-wb.png)

Isso fornece uma visão geral da distribuição do comprimento corporal por ordem de pássaros, mas não é a maneira ideal de exibir distribuições reais. Essa tarefa geralmente é realizada criando um histograma.

## Trabalhando com histogramas

O Matplotlib oferece ótimas maneiras de visualizar a distribuição de dados usando histogramas. Esse tipo de gráfico é semelhante a um gráfico de barras, onde a distribuição pode ser vista pelo aumento e diminuição das barras. Para construir um histograma, você precisa de dados numéricos. Para criar um histograma, você pode plotar um gráfico definindo o tipo como 'hist' para histograma. Este gráfico mostra a distribuição de MassaCorporalMax para o intervalo de dados numéricos de todo o conjunto de dados. Dividindo o array de dados em pequenos intervalos, ele pode exibir a distribuição dos valores dos dados:

```python
birds['MaxBodyMass'].plot(kind = 'hist', bins = 10, figsize = (12,12))
plt.show()
```
![distribuição em todo o conjunto de dados](../../../../3-Data-Visualization/10-visualization-distributions/images/dist1-wb.png)

Como você pode ver, a maioria dos 400+ pássaros neste conjunto de dados está na faixa de menos de 2000 para sua Massa Corporal Máxima. Obtenha mais informações sobre os dados alterando o parâmetro `bins` para um número maior, como 30:

```python
birds['MaxBodyMass'].plot(kind = 'hist', bins = 30, figsize = (12,12))
plt.show()
```
![distribuição em todo o conjunto de dados com maior parâmetro de bins](../../../../3-Data-Visualization/10-visualization-distributions/images/dist2-wb.png)

Este gráfico mostra a distribuição de forma um pouco mais detalhada. Um gráfico menos inclinado para a esquerda poderia ser criado garantindo que você selecione apenas dados dentro de um determinado intervalo:

Filtre seus dados para obter apenas os pássaros cuja massa corporal seja inferior a 60 e mostre 40 `bins`:

```python
filteredBirds = birds[(birds['MaxBodyMass'] > 1) & (birds['MaxBodyMass'] < 60)]      
filteredBirds['MaxBodyMass'].plot(kind = 'hist',bins = 40,figsize = (12,12))
plt.show()     
```
![histograma filtrado](../../../../3-Data-Visualization/10-visualization-distributions/images/dist3-wb.png)

✅ Experimente outros filtros e pontos de dados. Para ver a distribuição completa dos dados, remova o filtro `['MaxBodyMass']` para mostrar distribuições rotuladas.

O histograma oferece algumas melhorias de cor e rotulagem interessantes para experimentar também:

Crie um histograma 2D para comparar a relação entre duas distribuições. Vamos comparar `MaxBodyMass` vs. `MaxLength`. O Matplotlib oferece uma maneira integrada de mostrar convergência usando cores mais brilhantes:

```python
x = filteredBirds['MaxBodyMass']
y = filteredBirds['MaxLength']

fig, ax = plt.subplots(tight_layout=True)
hist = ax.hist2d(x, y)
```
Parece haver uma correlação esperada entre esses dois elementos ao longo de um eixo esperado, com um ponto particularmente forte de convergência:

![gráfico 2D](../../../../3-Data-Visualization/10-visualization-distributions/images/2D-wb.png)

Os histogramas funcionam bem por padrão para dados numéricos. E se você precisar ver distribuições de acordo com dados textuais? 
## Explore o conjunto de dados para distribuições usando dados textuais 

Este conjunto de dados também inclui boas informações sobre a categoria do pássaro, seu gênero, espécie e família, bem como seu status de conservação. Vamos explorar essas informações de conservação. Qual é a distribuição dos pássaros de acordo com seu status de conservação?

> ✅ No conjunto de dados, vários acrônimos são usados para descrever o status de conservação. Esses acrônimos vêm das [Categorias da Lista Vermelha da IUCN](https://www.iucnredlist.org/), uma organização que cataloga o status das espécies.
> 
> - CR: Criticamente Ameaçado
> - EN: Ameaçado
> - EX: Extinto
> - LC: Pouco Preocupante
> - NT: Quase Ameaçado
> - VU: Vulnerável

Esses valores são baseados em texto, então você precisará fazer uma transformação para criar um histograma. Usando o dataframe filteredBirds, exiba seu status de conservação ao lado de sua Envergadura Mínima. O que você observa?

```python
x1 = filteredBirds.loc[filteredBirds.ConservationStatus=='EX', 'MinWingspan']
x2 = filteredBirds.loc[filteredBirds.ConservationStatus=='CR', 'MinWingspan']
x3 = filteredBirds.loc[filteredBirds.ConservationStatus=='EN', 'MinWingspan']
x4 = filteredBirds.loc[filteredBirds.ConservationStatus=='NT', 'MinWingspan']
x5 = filteredBirds.loc[filteredBirds.ConservationStatus=='VU', 'MinWingspan']
x6 = filteredBirds.loc[filteredBirds.ConservationStatus=='LC', 'MinWingspan']

kwargs = dict(alpha=0.5, bins=20)

plt.hist(x1, **kwargs, color='red', label='Extinct')
plt.hist(x2, **kwargs, color='orange', label='Critically Endangered')
plt.hist(x3, **kwargs, color='yellow', label='Endangered')
plt.hist(x4, **kwargs, color='green', label='Near Threatened')
plt.hist(x5, **kwargs, color='blue', label='Vulnerable')
plt.hist(x6, **kwargs, color='gray', label='Least Concern')

plt.gca().set(title='Conservation Status', ylabel='Min Wingspan')
plt.legend();
```

![envergadura e status de conservação](../../../../3-Data-Visualization/10-visualization-distributions/images/histogram-conservation-wb.png)

Não parece haver uma boa correlação entre envergadura mínima e status de conservação. Teste outros elementos do conjunto de dados usando este método. Você encontra alguma correlação?

## Gráficos de densidade

Você pode ter notado que os histogramas que analisamos até agora são 'escalonados' e não fluem suavemente em um arco. Para mostrar um gráfico de densidade mais suave, você pode tentar um gráfico de densidade.

Para trabalhar com gráficos de densidade, familiarize-se com uma nova biblioteca de plotagem, [Seaborn](https://seaborn.pydata.org/generated/seaborn.kdeplot.html). 

Carregando o Seaborn, experimente um gráfico de densidade básico:

```python
import seaborn as sns
import matplotlib.pyplot as plt
sns.kdeplot(filteredBirds['MinWingspan'])
plt.show()
```
![Gráfico de densidade](../../../../3-Data-Visualization/10-visualization-distributions/images/density1.png)

Você pode ver como o gráfico reflete o anterior para os dados de Envergadura Mínima; é apenas um pouco mais suave. De acordo com a documentação do Seaborn, "Em relação a um histograma, o KDE pode produzir um gráfico menos confuso e mais interpretável, especialmente ao desenhar várias distribuições. Mas ele tem o potencial de introduzir distorções se a distribuição subjacente for limitada ou não suave. Como um histograma, a qualidade da representação também depende da seleção de bons parâmetros de suavização." [fonte](https://seaborn.pydata.org/generated/seaborn.kdeplot.html) Em outras palavras, outliers, como sempre, farão seus gráficos se comportarem mal.

Se você quisesse revisitar aquela linha irregular de MassaCorporalMax no segundo gráfico que construiu, poderia suavizá-la muito bem recriando-a usando este método:

```python
sns.kdeplot(filteredBirds['MaxBodyMass'])
plt.show()
```
![linha de massa corporal suavizada](../../../../3-Data-Visualization/10-visualization-distributions/images/density2.png)

Se você quisesse uma linha suave, mas não muito suave, edite o parâmetro `bw_adjust`: 

```python
sns.kdeplot(filteredBirds['MaxBodyMass'], bw_adjust=.2)
plt.show()
```
![linha de massa corporal menos suave](../../../../3-Data-Visualization/10-visualization-distributions/images/density3.png)

✅ Leia sobre os parâmetros disponíveis para este tipo de gráfico e experimente!

Este tipo de gráfico oferece visualizações explicativas muito bonitas. Com algumas linhas de código, por exemplo, você pode mostrar a densidade de massa corporal máxima por ordem de pássaros:

```python
sns.kdeplot(
   data=filteredBirds, x="MaxBodyMass", hue="Order",
   fill=True, common_norm=False, palette="crest",
   alpha=.5, linewidth=0,
)
```

![massa corporal por ordem](../../../../3-Data-Visualization/10-visualization-distributions/images/density4.png)

Você também pode mapear a densidade de várias variáveis em um único gráfico. Teste o ComprimentoMáximo e ComprimentoMínimo de um pássaro em comparação com seu status de conservação:

```python
sns.kdeplot(data=filteredBirds, x="MinLength", y="MaxLength", hue="ConservationStatus")
```

![múltiplas densidades, sobrepostas](../../../../3-Data-Visualization/10-visualization-distributions/images/multi.png)

Talvez valha a pena pesquisar se o agrupamento de pássaros 'Vulneráveis' de acordo com seus comprimentos é significativo ou não.

## 🚀 Desafio

Os histogramas são um tipo de gráfico mais sofisticado do que gráficos de dispersão, gráficos de barras ou gráficos de linhas básicos. Faça uma busca na internet para encontrar bons exemplos do uso de histogramas. Como eles são usados, o que demonstram e em quais campos ou áreas de estudo tendem a ser utilizados?

## [Quiz pós-aula](https://ff-quizzes.netlify.app/en/ds/quiz/19)

## Revisão e Autoestudo

Nesta lição, você usou o Matplotlib e começou a trabalhar com o Seaborn para mostrar gráficos mais sofisticados. Pesquise sobre `kdeplot` no Seaborn, uma "curva de densidade de probabilidade contínua em uma ou mais dimensões". Leia a [documentação](https://seaborn.pydata.org/generated/seaborn.kdeplot.html) para entender como funciona.

## Tarefa

[Coloque suas habilidades em prática](assignment.md)

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.