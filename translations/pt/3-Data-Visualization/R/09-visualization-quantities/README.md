<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "22acf28f518a4769ea14fa42f4734b9f",
  "translation_date": "2025-08-24T22:48:55+00:00",
  "source_file": "3-Data-Visualization/R/09-visualization-quantities/README.md",
  "language_code": "pt"
}
-->
# Visualizar Quantidades
|![ Sketchnote por [(@sketchthedocs)](https://sketchthedocs.dev) ](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/sketchnotes/09-Visualizing-Quantities.png)|
|:---:|
| Visualizar Quantidades - _Sketchnote por [@nitya](https://twitter.com/nitya)_ |

Nesta lição, vais explorar como utilizar algumas das muitas bibliotecas de pacotes disponíveis no R para aprender a criar visualizações interessantes em torno do conceito de quantidade. Usando um conjunto de dados limpo sobre os pássaros do Minnesota, podes aprender muitos factos interessantes sobre a vida selvagem local.  
## [Questionário pré-aula](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/16)

## Observar a envergadura com ggplot2
Uma biblioteca excelente para criar gráficos e diagramas simples e sofisticados de vários tipos é [ggplot2](https://cran.r-project.org/web/packages/ggplot2/index.html). Em termos gerais, o processo de criação de gráficos usando estas bibliotecas inclui identificar as partes do teu dataframe que queres analisar, realizar as transformações necessárias nos dados, atribuir os valores dos eixos x e y, decidir o tipo de gráfico a mostrar e, finalmente, exibir o gráfico.

`ggplot2` é um sistema para criar gráficos de forma declarativa, baseado na Gramática dos Gráficos. A [Gramática dos Gráficos](https://en.wikipedia.org/wiki/Ggplot2) é um esquema geral para visualização de dados que divide os gráficos em componentes semânticos, como escalas e camadas. Em outras palavras, a facilidade de criar gráficos para dados univariados ou multivariados com pouco código torna o `ggplot2` o pacote mais popular usado para visualizações em R. O utilizador informa ao `ggplot2` como mapear as variáveis para os elementos visuais, os primitivos gráficos a usar, e o `ggplot2` cuida do resto.

> ✅ Gráfico = Dados + Estética + Geometria  
> - Dados referem-se ao conjunto de dados  
> - Estética indica as variáveis a serem estudadas (variáveis x e y)  
> - Geometria refere-se ao tipo de gráfico (gráfico de linhas, barras, etc.)  

Escolhe a melhor geometria (tipo de gráfico) de acordo com os teus dados e a história que queres contar através do gráfico.  

> - Para analisar tendências: linha, coluna  
> - Para comparar valores: barra, coluna, circular, dispersão  
> - Para mostrar como as partes se relacionam com o todo: circular  
> - Para mostrar a distribuição dos dados: dispersão, barra  
> - Para mostrar relações entre valores: linha, dispersão, bolha  

✅ Também podes consultar este [cheatsheet descritivo](https://nyu-cdsc.github.io/learningr/assets/data-visualization-2.1.pdf) para ggplot2.

## Criar um gráfico de linhas sobre os valores de envergadura das aves

Abre o console do R e importa o conjunto de dados.  
> Nota: O conjunto de dados está armazenado na raiz deste repositório na pasta `/data`.

Vamos importar o conjunto de dados e observar as primeiras linhas (topo 5) dos dados.

```r
birds <- read.csv("../../data/birds.csv",fileEncoding="UTF-8-BOM")
head(birds)
```  
O início dos dados tem uma mistura de texto e números:

|      | Nome                         | NomeCientífico         | Categoria              | Ordem        | Família   | Género       | EstadoConservação | MinComprimento | MaxComprimento | MinMassaCorporal | MaxMassaCorporal | MinEnvergadura | MaxEnvergadura |
| ---: | :--------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :----------------- | --------: | --------: | ----------: | ----------: | ----------: | ----------: |
|    0 | Pato-silvo-de-barriga-preta  | Dendrocygna autumnalis | Patos/Gansos/AvesAquáticas | Anseriformes | Anatidae | Dendrocygna | LC                 |        47 |        56 |         652 |        1020 |          76 |          94 |
|    1 | Pato-silvo-fulvo             | Dendrocygna bicolor    | Patos/Gansos/AvesAquáticas | Anseriformes | Anatidae | Dendrocygna | LC                 |        45 |        53 |         712 |        1050 |          85 |          93 |
|    2 | Ganso-da-neve                | Anser caerulescens     | Patos/Gansos/AvesAquáticas | Anseriformes | Anatidae | Anser       | LC                 |        64 |        79 |        2050 |        4050 |         135 |         165 |
|    3 | Ganso-de-Ross                | Anser rossii           | Patos/Gansos/AvesAquáticas | Anseriformes | Anatidae | Anser       | LC                 |      57.3 |        64 |        1066 |        1567 |         113 |         116 |
|    4 | Ganso-de-testa-branca-maior  | Anser albifrons        | Patos/Gansos/AvesAquáticas | Anseriformes | Anatidae | Anser       | LC                 |        64 |        81 |        1930 |        3310 |         130 |         165 |

Vamos começar por representar graficamente alguns dos dados numéricos usando um gráfico de linhas básico. Suponhamos que queres visualizar a envergadura máxima destas aves interessantes.

```r
install.packages("ggplot2")
library("ggplot2")
ggplot(data=birds, aes(x=Name, y=MaxWingspan,group=1)) +
  geom_line() 
```  
Aqui, instalas o pacote `ggplot2` e depois importas para o ambiente de trabalho usando o comando `library("ggplot2")`. Para criar qualquer gráfico no ggplot, usa-se a função `ggplot()` e especifica-se o conjunto de dados, as variáveis x e y como atributos. Neste caso, usamos a função `geom_line()` porque queremos criar um gráfico de linhas.

![MaxWingspan-lineplot](../../../../../translated_images/MaxWingspan-lineplot.b12169f99d26fdd263f291008dfd73c18a4ba8f3d32b1fda3d74af51a0a28616.pt.png)

O que notas imediatamente? Parece haver pelo menos um valor atípico - que envergadura impressionante! Uma envergadura de mais de 2000 centímetros equivale a mais de 20 metros - será que há Pterodáctilos a voar em Minnesota? Vamos investigar.

Embora pudesses fazer uma ordenação rápida no Excel para encontrar esses valores atípicos, que provavelmente são erros de digitação, continua o processo de visualização trabalhando diretamente no gráfico.

Adiciona rótulos ao eixo x para mostrar que tipo de aves estão em questão:

```r
ggplot(data=birds, aes(x=Name, y=MaxWingspan,group=1)) +
  geom_line() +
  theme(axis.text.x = element_text(angle = 45, hjust=1))+
  xlab("Birds") +
  ylab("Wingspan (CM)") +
  ggtitle("Max Wingspan in Centimeters")
```  
Especificamos o ângulo no `theme` e definimos os rótulos dos eixos x e y em `xlab()` e `ylab()` respetivamente. O `ggtitle()` dá um nome ao gráfico.

![MaxWingspan-lineplot-improved](../../../../../translated_images/MaxWingspan-lineplot-improved.04b73b4d5a59552a6bc7590678899718e1f065abe9eada9ebb4148939b622fd4.pt.png)

Mesmo com a rotação dos rótulos definida para 45 graus, há demasiados para ler. Vamos tentar uma estratégia diferente: rotular apenas os valores atípicos e definir os rótulos dentro do gráfico. Podes usar um gráfico de dispersão para criar mais espaço para os rótulos:

```r
ggplot(data=birds, aes(x=Name, y=MaxWingspan,group=1)) +
  geom_point() +
  geom_text(aes(label=ifelse(MaxWingspan>500,as.character(Name),'')),hjust=0,vjust=0) + 
  theme(axis.title.x=element_blank(), axis.text.x=element_blank(), axis.ticks.x=element_blank())
  ylab("Wingspan (CM)") +
  ggtitle("Max Wingspan in Centimeters") + 
```  
O que está a acontecer aqui? Usaste a função `geom_point()` para criar pontos de dispersão. Com isso, adicionaste rótulos para aves cuja `MaxWingspan > 500` e também ocultaste os rótulos no eixo x para desobstruir o gráfico.

O que descobres?

![MaxWingspan-scatterplot](../../../../../translated_images/MaxWingspan-scatterplot.60dc9e0e19d32700283558f253841fdab5104abb62bc96f7d97f9c0ee857fa8b.pt.png)

## Filtrar os teus dados

Tanto a Águia-careca como o Falcão-das-pradarias, embora provavelmente sejam aves muito grandes, parecem estar mal rotulados, com um zero extra adicionado à sua envergadura máxima. É improvável que encontres uma Águia-careca com uma envergadura de 25 metros, mas, se isso acontecer, avisa-nos! Vamos criar um novo dataframe sem esses dois valores atípicos:

```r
birds_filtered <- subset(birds, MaxWingspan < 500)

ggplot(data=birds_filtered, aes(x=Name, y=MaxWingspan,group=1)) +
  geom_point() +
  ylab("Wingspan (CM)") +
  xlab("Birds") +
  ggtitle("Max Wingspan in Centimeters") + 
  geom_text(aes(label=ifelse(MaxWingspan>500,as.character(Name),'')),hjust=0,vjust=0) +
  theme(axis.text.x=element_blank(), axis.ticks.x=element_blank())
```  
Criámos um novo dataframe `birds_filtered` e depois representámos um gráfico de dispersão. Ao filtrar os valores atípicos, os teus dados tornam-se mais coesos e compreensíveis.

![MaxWingspan-scatterplot-improved](../../../../../translated_images/MaxWingspan-scatterplot-improved.7d0af81658c65f3e75b8fedeb2335399e31108257e48db15d875ece608272051.pt.png)

Agora que temos um conjunto de dados mais limpo, pelo menos em termos de envergadura, vamos descobrir mais sobre estas aves.

Embora gráficos de linhas e dispersão possam exibir informações sobre valores de dados e suas distribuições, queremos pensar nos valores inerentes a este conjunto de dados. Podes criar visualizações para responder às seguintes perguntas sobre quantidade:

> Quantas categorias de aves existem e quais são os seus números?  
> Quantas aves estão extintas, em perigo, raras ou comuns?  
> Quantas existem dos vários géneros e ordens na terminologia de Linnaeus?  

## Explorar gráficos de barras

Os gráficos de barras são práticos quando precisas de mostrar agrupamentos de dados. Vamos explorar as categorias de aves que existem neste conjunto de dados para ver qual é a mais comum em número.  
Vamos criar um gráfico de barras com os dados filtrados.

```r
install.packages("dplyr")
install.packages("tidyverse")

library(lubridate)
library(scales)
library(dplyr)
library(ggplot2)
library(tidyverse)

birds_filtered %>% group_by(Category) %>%
  summarise(n=n(),
  MinLength = mean(MinLength),
  MaxLength = mean(MaxLength),
  MinBodyMass = mean(MinBodyMass),
  MaxBodyMass = mean(MaxBodyMass),
  MinWingspan=mean(MinWingspan),
  MaxWingspan=mean(MaxWingspan)) %>% 
  gather("key", "value", - c(Category, n)) %>%
  ggplot(aes(x = Category, y = value, group = key, fill = key)) +
  geom_bar(stat = "identity") +
  scale_fill_manual(values = c("#D62728", "#FF7F0E", "#8C564B","#2CA02C", "#1F77B4", "#9467BD")) +                   
  xlab("Category")+ggtitle("Birds of Minnesota")

```  
No seguinte trecho, instalamos os pacotes [dplyr](https://www.rdocumentation.org/packages/dplyr/versions/0.7.8) e [lubridate](https://www.rdocumentation.org/packages/lubridate/versions/1.8.0) para ajudar a manipular e agrupar dados para criar um gráfico de barras empilhado. Primeiro, agrupas os dados pela `Categoria` das aves e depois resumes as colunas `MinLength`, `MaxLength`, `MinBodyMass`, `MaxBodyMass`, `MinWingspan`, `MaxWingspan`. Em seguida, crias o gráfico de barras usando o pacote `ggplot2` e especificas as cores para as diferentes categorias e os rótulos.

![Stacked bar chart](../../../../../translated_images/stacked-bar-chart.0c92264e89da7b391a7490224d1e7059a020e8b74dcd354414aeac78871c02f1.pt.png)

Este gráfico de barras, no entanto, é ilegível porque há demasiados dados não agrupados. Precisamos de selecionar apenas os dados que queremos representar, então vamos observar o comprimento das aves com base na sua categoria.

Filtra os teus dados para incluir apenas a categoria das aves.

Como há muitas categorias, podes exibir este gráfico verticalmente e ajustar a sua altura para acomodar todos os dados:

```r
birds_count<-dplyr::count(birds_filtered, Category, sort = TRUE)
birds_count$Category <- factor(birds_count$Category, levels = birds_count$Category)
ggplot(birds_count,aes(Category,n))+geom_bar(stat="identity")+coord_flip()
```  
Primeiro, contas os valores únicos na coluna `Categoria` e depois ordenas num novo dataframe `birds_count`. Estes dados ordenados são então considerados no mesmo nível para que sejam representados de forma ordenada. Usando o `ggplot2`, crias o gráfico de barras. O `coord_flip()` cria barras horizontais.

![category-length](../../../../../translated_images/category-length.7e34c296690e85d64f7e4d25a56077442683eca96c4f5b4eae120a64c0755636.pt.png)

Este gráfico de barras mostra uma boa visão do número de aves em cada categoria. Num piscar de olhos, vês que o maior número de aves nesta região pertence à categoria de Patos/Gansos/AvesAquáticas. Minnesota é a 'terra dos 10.000 lagos', então isto não é surpreendente!

✅ Experimenta algumas outras contagens neste conjunto de dados. Algo te surpreende?

## Comparar dados

Podes tentar diferentes comparações de dados agrupados criando novos eixos. Experimenta uma comparação do MaxLength de uma ave, com base na sua categoria:

```r
birds_grouped <- birds_filtered %>%
  group_by(Category) %>%
  summarise(
  MaxLength = max(MaxLength, na.rm = T),
  MinLength = max(MinLength, na.rm = T)
           ) %>%
  arrange(Category)
  
ggplot(birds_grouped,aes(Category,MaxLength))+geom_bar(stat="identity")+coord_flip()
```  
Agrupamos os dados `birds_filtered` pela `Categoria` e depois criamos um gráfico de barras.

![comparing data](../../../../../translated_images/comparingdata.f486a450d61c7ca5416f27f3f55a6a4465d00df3be5e6d33936e9b07b95e2fdd.pt.png)

Nada é surpreendente aqui: os beija-flores têm o menor MaxLength em comparação com os Pelicanos ou Gansos. É bom quando os dados fazem sentido lógico!

Podes criar visualizações mais interessantes de gráficos de barras sobrepondo dados. Vamos sobrepor o Comprimento Mínimo e Máximo numa determinada categoria de aves:

```r
ggplot(data=birds_grouped, aes(x=Category)) +
  geom_bar(aes(y=MaxLength), stat="identity", position ="identity",  fill='blue') +
  geom_bar(aes(y=MinLength), stat="identity", position="identity", fill='orange')+
  coord_flip()
```  
![super-imposed values](../../../../../translated_images/superimposed-values.5363f0705a1da4167625a373a1064331ea3cb7a06a297297d0734fcc9b3819a0.pt.png)

## 🚀 Desafio

Este conjunto de dados sobre aves oferece uma riqueza de informações sobre diferentes tipos de aves dentro de um ecossistema particular. Procura na internet e vê se consegues encontrar outros conjuntos de dados relacionados com aves. Pratica a criação de gráficos e diagramas sobre estas aves para descobrir factos que não conhecias.  
## [Questionário pós-aula](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/17)

## Revisão & Autoestudo

Esta primeira lição deu-te algumas informações sobre como usar o `ggplot2` para visualizar quantidades. Faz alguma pesquisa sobre outras formas de trabalhar com conjuntos de dados para visualização. Pesquisa e procura conjuntos de dados que possas visualizar usando outros pacotes como [Lattice](https://stat.ethz.ch/R-manual/R-devel/library/lattice/html/Lattice.html) e [Plotly](https://github.com/plotly/plotly.R#readme).

## Tarefa  
[Linhas, Dispersões e Barras](assignment.md)  

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original no seu idioma nativo deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se uma tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes do uso desta tradução.