<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "80a20467e046d312809d008395051fc7",
  "translation_date": "2025-09-05T13:23:37+00:00",
  "source_file": "3-Data-Visualization/10-visualization-distributions/README.md",
  "language_code": "pt"
}
-->
# Visualizar Distribuições

|![ Sketchnote por [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/10-Visualizing-Distributions.png)|
|:---:|
| Visualizar Distribuições - _Sketchnote por [@nitya](https://twitter.com/nitya)_ |

Na lição anterior, aprendeste alguns factos interessantes sobre um conjunto de dados sobre as aves do Minnesota. Identificaste dados errados ao visualizar outliers e analisaste as diferenças entre categorias de aves com base no seu comprimento máximo.

## [Questionário pré-aula](https://ff-quizzes.netlify.app/en/ds/quiz/18)
## Explorar o conjunto de dados das aves

Outra forma de explorar os dados é analisando a sua distribuição, ou como os dados estão organizados ao longo de um eixo. Talvez, por exemplo, queiras saber mais sobre a distribuição geral, neste conjunto de dados, da envergadura máxima ou da massa corporal máxima das aves do Minnesota.

Vamos descobrir alguns factos sobre as distribuições dos dados neste conjunto. No ficheiro _notebook.ipynb_ na raiz da pasta desta lição, importa Pandas, Matplotlib e os teus dados:

```python
import pandas as pd
import matplotlib.pyplot as plt
birds = pd.read_csv('../../data/birds.csv')
birds.head()
```

|      | Nome                         | NomeCientífico         | Categoria              | Ordem        | Família   | Género       | EstadoConservação | ComprimentoMin | ComprimentoMax | MassaCorporalMin | MassaCorporalMax | EnvergaduraMin | EnvergaduraMax |
| ---: | :--------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :----------------- | --------: | --------: | ----------: | ----------: | ----------: | ----------: |
|    0 | Pato-silvo-de-barriga-preta  | Dendrocygna autumnalis | Patos/Gansos/AvesAquáticas | Anseriformes | Anatidae | Dendrocygna | LC                 |        47 |        56 |         652 |        1020 |          76 |          94 |
|    1 | Pato-silvo-fulvo             | Dendrocygna bicolor    | Patos/Gansos/AvesAquáticas | Anseriformes | Anatidae | Dendrocygna | LC                 |        45 |        53 |         712 |        1050 |          85 |          93 |
|    2 | Ganso-da-neve                | Anser caerulescens     | Patos/Gansos/AvesAquáticas | Anseriformes | Anatidae | Anser       | LC                 |        64 |        79 |        2050 |        4050 |         135 |         165 |
|    3 | Ganso-de-Ross                | Anser rossii           | Patos/Gansos/AvesAquáticas | Anseriformes | Anatidae | Anser       | LC                 |      57.3 |        64 |        1066 |        1567 |         113 |         116 |
|    4 | Ganso-de-testa-branca-maior  | Anser albifrons        | Patos/Gansos/AvesAquáticas | Anseriformes | Anatidae | Anser       | LC                 |        64 |        81 |        1930 |        3310 |         130 |         165 |

De forma geral, podes rapidamente observar como os dados estão distribuídos utilizando um gráfico de dispersão, como fizemos na lição anterior:

```python
birds.plot(kind='scatter',x='MaxLength',y='Order',figsize=(12,8))

plt.title('Max Length per Order')
plt.ylabel('Order')
plt.xlabel('Max Length')

plt.show()
```
![comprimento máximo por ordem](../../../../3-Data-Visualization/10-visualization-distributions/images/scatter-wb.png)

Isto dá uma visão geral da distribuição do comprimento corporal por Ordem de aves, mas não é a forma ideal de mostrar distribuições reais. Essa tarefa é geralmente realizada através da criação de um Histograma.

## Trabalhar com histogramas

O Matplotlib oferece ótimas formas de visualizar a distribuição de dados utilizando Histogramas. Este tipo de gráfico é semelhante a um gráfico de barras, onde a distribuição pode ser vista através da subida e descida das barras. Para construir um histograma, precisas de dados numéricos. Para criar um Histograma, podes desenhar um gráfico definindo o tipo como 'hist' para Histograma. Este gráfico mostra a distribuição de MassaCorporalMax para o intervalo de dados numéricos de todo o conjunto de dados. Dividindo o array de dados em pequenos intervalos, é possível exibir a distribuição dos valores dos dados:

```python
birds['MaxBodyMass'].plot(kind = 'hist', bins = 10, figsize = (12,12))
plt.show()
```
![distribuição em todo o conjunto de dados](../../../../3-Data-Visualization/10-visualization-distributions/images/dist1-wb.png)

Como podes ver, a maioria das mais de 400 aves neste conjunto de dados tem uma Massa Corporal Máxima abaixo de 2000. Obtém mais informações sobre os dados alterando o parâmetro `bins` para um número maior, como 30:

```python
birds['MaxBodyMass'].plot(kind = 'hist', bins = 30, figsize = (12,12))
plt.show()
```
![distribuição em todo o conjunto de dados com maior parâmetro bins](../../../../3-Data-Visualization/10-visualization-distributions/images/dist2-wb.png)

Este gráfico mostra a distribuição de forma um pouco mais detalhada. Um gráfico menos inclinado para a esquerda poderia ser criado garantindo que apenas selecionas dados dentro de um determinado intervalo:

Filtra os teus dados para obter apenas as aves cuja massa corporal seja inferior a 60 e mostra 40 `bins`:

```python
filteredBirds = birds[(birds['MaxBodyMass'] > 1) & (birds['MaxBodyMass'] < 60)]      
filteredBirds['MaxBodyMass'].plot(kind = 'hist',bins = 40,figsize = (12,12))
plt.show()     
```
![histograma filtrado](../../../../3-Data-Visualization/10-visualization-distributions/images/dist3-wb.png)

✅ Experimenta outros filtros e pontos de dados. Para ver a distribuição completa dos dados, remove o filtro `['MaxBodyMass']` para mostrar distribuições etiquetadas.

O histograma oferece algumas melhorias de cor e etiquetagem interessantes para experimentar também:

Cria um histograma 2D para comparar a relação entre duas distribuições. Vamos comparar `MaxBodyMass` vs. `MaxLength`. O Matplotlib oferece uma forma integrada de mostrar convergência utilizando cores mais brilhantes:

```python
x = filteredBirds['MaxBodyMass']
y = filteredBirds['MaxLength']

fig, ax = plt.subplots(tight_layout=True)
hist = ax.hist2d(x, y)
```
Parece haver uma correlação esperada entre estes dois elementos ao longo de um eixo esperado, com um ponto de convergência particularmente forte:

![gráfico 2D](../../../../3-Data-Visualization/10-visualization-distributions/images/2D-wb.png)

Os histogramas funcionam bem por padrão para dados numéricos. E se precisarmos de ver distribuições de acordo com dados textuais?

## Explorar o conjunto de dados para distribuições utilizando dados textuais 

Este conjunto de dados também inclui boas informações sobre a categoria das aves, o seu género, espécie e família, bem como o seu estado de conservação. Vamos explorar esta informação de conservação. Qual é a distribuição das aves de acordo com o seu estado de conservação?

> ✅ No conjunto de dados, vários acrónimos são usados para descrever o estado de conservação. Estes acrónimos vêm das [Categorias da Lista Vermelha da IUCN](https://www.iucnredlist.org/), uma organização que cataloga o estado das espécies.
> 
> - CR: Criticamente em Perigo
> - EN: Em Perigo
> - EX: Extinto
> - LC: Pouca Preocupação
> - NT: Quase Ameaçado
> - VU: Vulnerável

Estes são valores baseados em texto, por isso será necessário fazer uma transformação para criar um histograma. Utilizando o dataframe filteredBirds, exibe o estado de conservação juntamente com a sua Envergadura Mínima. O que observas?

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

![colagem de envergadura e conservação](../../../../3-Data-Visualization/10-visualization-distributions/images/histogram-conservation-wb.png)

Não parece haver uma boa correlação entre a envergadura mínima e o estado de conservação. Testa outros elementos do conjunto de dados utilizando este método. Podes experimentar diferentes filtros também. Encontras alguma correlação?

## Gráficos de densidade

Podes ter notado que os histogramas que analisámos até agora são 'escalonados' e não fluem suavemente em arco. Para mostrar um gráfico de densidade mais suave, podes experimentar um gráfico de densidade.

Para trabalhar com gráficos de densidade, familiariza-te com uma nova biblioteca de gráficos, [Seaborn](https://seaborn.pydata.org/generated/seaborn.kdeplot.html). 

Carregando o Seaborn, experimenta um gráfico de densidade básico:

```python
import seaborn as sns
import matplotlib.pyplot as plt
sns.kdeplot(filteredBirds['MinWingspan'])
plt.show()
```
![Gráfico de densidade](../../../../3-Data-Visualization/10-visualization-distributions/images/density1.png)

Podes ver como o gráfico reflete o anterior para os dados de Envergadura Mínima; é apenas um pouco mais suave. De acordo com a documentação do Seaborn, "Em relação a um histograma, o KDE pode produzir um gráfico menos confuso e mais interpretável, especialmente ao desenhar múltiplas distribuições. Mas tem o potencial de introduzir distorções se a distribuição subjacente for limitada ou não suave. Tal como um histograma, a qualidade da representação também depende da seleção de bons parâmetros de suavização." [fonte](https://seaborn.pydata.org/generated/seaborn.kdeplot.html) Em outras palavras, outliers, como sempre, farão com que os teus gráficos se comportem mal.

Se quisesses revisitar aquela linha irregular de MassaCorporalMax no segundo gráfico que construíste, poderias suavizá-la muito bem recriando-a utilizando este método:

```python
sns.kdeplot(filteredBirds['MaxBodyMass'])
plt.show()
```
![linha de massa corporal suave](../../../../3-Data-Visualization/10-visualization-distributions/images/density2.png)

Se quisesses uma linha suave, mas não demasiado suave, edita o parâmetro `bw_adjust`: 

```python
sns.kdeplot(filteredBirds['MaxBodyMass'], bw_adjust=.2)
plt.show()
```
![linha de massa corporal menos suave](../../../../3-Data-Visualization/10-visualization-distributions/images/density3.png)

✅ Lê sobre os parâmetros disponíveis para este tipo de gráfico e experimenta!

Este tipo de gráfico oferece visualizações explicativas muito bonitas. Com algumas linhas de código, por exemplo, podes mostrar a densidade de massa corporal máxima por Ordem de aves:

```python
sns.kdeplot(
   data=filteredBirds, x="MaxBodyMass", hue="Order",
   fill=True, common_norm=False, palette="crest",
   alpha=.5, linewidth=0,
)
```

![massa corporal por ordem](../../../../3-Data-Visualization/10-visualization-distributions/images/density4.png)

Também podes mapear a densidade de várias variáveis num único gráfico. Testa o ComprimentoMáximo e ComprimentoMínimo de uma ave em comparação com o seu estado de conservação:

```python
sns.kdeplot(data=filteredBirds, x="MinLength", y="MaxLength", hue="ConservationStatus")
```

![múltiplas densidades, sobrepostas](../../../../3-Data-Visualization/10-visualization-distributions/images/multi.png)

Talvez valha a pena investigar se o agrupamento de aves 'Vulneráveis' de acordo com os seus comprimentos é significativo ou não.

## 🚀 Desafio

Os histogramas são um tipo de gráfico mais sofisticado do que gráficos de dispersão, gráficos de barras ou gráficos de linhas básicos. Faz uma pesquisa na internet para encontrar bons exemplos do uso de histogramas. Como são utilizados, o que demonstram e em que áreas ou campos de investigação tendem a ser usados?

## [Questionário pós-aula](https://ff-quizzes.netlify.app/en/ds/quiz/19)

## Revisão & Autoestudo

Nesta lição, utilizaste o Matplotlib e começaste a trabalhar com o Seaborn para mostrar gráficos mais sofisticados. Faz alguma pesquisa sobre `kdeplot` no Seaborn, uma "curva de densidade de probabilidade contínua em uma ou mais dimensões". Lê a [documentação](https://seaborn.pydata.org/generated/seaborn.kdeplot.html) para entender como funciona.

## Tarefa

[Aplica as tuas competências](assignment.md)

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte oficial. Para informações críticas, recomenda-se uma tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes do uso desta tradução.