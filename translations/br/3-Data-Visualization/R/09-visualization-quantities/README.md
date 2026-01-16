<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "22acf28f518a4769ea14fa42f4734b9f",
  "translation_date": "2025-08-27T18:33:01+00:00",
  "source_file": "3-Data-Visualization/R/09-visualization-quantities/README.md",
  "language_code": "br"
}
-->
# Visualizando Quantidades
|![ Sketchnote por [(@sketchthedocs)](https://sketchthedocs.dev) ](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/sketchnotes/09-Visualizing-Quantities.png)|
|:---:|
| Visualizando Quantidades - _Sketchnote por [@nitya](https://twitter.com/nitya)_ |

Nesta lição, você explorará como usar algumas das muitas bibliotecas de pacotes disponíveis no R para aprender a criar visualizações interessantes em torno do conceito de quantidade. Usando um conjunto de dados limpo sobre os pássaros de Minnesota, você pode aprender muitos fatos interessantes sobre a vida selvagem local.  
## [Quiz pré-aula](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/16)

## Observe a envergadura com ggplot2
Uma excelente biblioteca para criar gráficos e diagramas simples e sofisticados de vários tipos é o [ggplot2](https://cran.r-project.org/web/packages/ggplot2/index.html). Em termos gerais, o processo de plotar dados usando essas bibliotecas inclui identificar as partes do seu dataframe que você deseja analisar, realizar as transformações necessárias nesses dados, atribuir valores aos eixos x e y, decidir o tipo de gráfico a ser exibido e, por fim, exibir o gráfico.

O `ggplot2` é um sistema para criar gráficos de forma declarativa, baseado na Gramática dos Gráficos. A [Gramática dos Gráficos](https://en.wikipedia.org/wiki/Ggplot2) é um esquema geral para visualização de dados que divide os gráficos em componentes semânticos, como escalas e camadas. Em outras palavras, a facilidade de criar gráficos para dados univariados ou multivariados com pouco código torna o `ggplot2` o pacote mais popular para visualizações no R. O usuário informa ao `ggplot2` como mapear as variáveis para os elementos visuais, os elementos gráficos a serem usados, e o `ggplot2` cuida do restante.

> ✅ Gráfico = Dados + Estética + Geometria  
> - Dados referem-se ao conjunto de dados  
> - Estética indica as variáveis a serem estudadas (variáveis x e y)  
> - Geometria refere-se ao tipo de gráfico (gráfico de linha, gráfico de barras, etc.)  

Escolha a melhor geometria (tipo de gráfico) de acordo com seus dados e a história que você deseja contar por meio do gráfico.

> - Para analisar tendências: linha, coluna  
> - Para comparar valores: barra, coluna, pizza, dispersão  
> - Para mostrar como as partes se relacionam com o todo: pizza  
> - Para mostrar a distribuição dos dados: dispersão, barra  
> - Para mostrar relações entre valores: linha, dispersão, bolha  

✅ Você também pode conferir este [cheatsheet](https://nyu-cdsc.github.io/learningr/assets/data-visualization-2.1.pdf) descritivo para ggplot2.

## Construa um gráfico de linha sobre os valores de envergadura de pássaros

Abra o console do R e importe o conjunto de dados.  
> Nota: O conjunto de dados está armazenado na raiz deste repositório na pasta `/data`.

Vamos importar o conjunto de dados e observar as primeiras linhas (topo) dos dados.

```r
birds <- read.csv("../../data/birds.csv",fileEncoding="UTF-8-BOM")
head(birds)
```  
O início dos dados contém uma mistura de texto e números:

|      | Nome                         | NomeCientífico         | Categoria             | Ordem        | Família  | Gênero      | StatusConservação | ComprimentoMín | ComprimentoMáx | MassaCorporalMín | MassaCorporalMáx | EnvergaduraMín | EnvergaduraMáx |
| ---: | :--------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :---------------- | --------------: | --------------: | ----------------: | ----------------: | --------------: | --------------: |
|    0 | Pato-assobiador-de-barriga-preta | Dendrocygna autumnalis | Patos/Gansos/AvesAquáticas | Anseriformes | Anatidae | Dendrocygna | LC                 |        47       |        56       |         652       |        1020       |          76     |          94     |
|    1 | Pato-assobiador-fulvo         | Dendrocygna bicolor    | Patos/Gansos/AvesAquáticas | Anseriformes | Anatidae | Dendrocygna | LC                 |        45       |        53       |         712       |        1050       |          85     |          93     |
|    2 | Ganso-das-neves              | Anser caerulescens     | Patos/Gansos/AvesAquáticas | Anseriformes | Anatidae | Anser       | LC                 |        64       |        79       |        2050       |        4050       |         135     |         165     |
|    3 | Ganso-de-Ross                | Anser rossii           | Patos/Gansos/AvesAquáticas | Anseriformes | Anatidae | Anser       | LC                 |      57.3       |        64       |        1066       |        1567       |         113     |         116     |
|    4 | Ganso-de-testa-branca-maior  | Anser albifrons        | Patos/Gansos/AvesAquáticas | Anseriformes | Anatidae | Anser       | LC                 |        64       |        81       |        1930       |        3310       |         130     |         165     |

Vamos começar plotando alguns dos dados numéricos usando um gráfico de linha básico. Suponha que você queira visualizar a envergadura máxima desses pássaros interessantes.

```r
install.packages("ggplot2")
library("ggplot2")
ggplot(data=birds, aes(x=Name, y=MaxWingspan,group=1)) +
  geom_line() 
```  
Aqui, você instala o pacote `ggplot2` e o importa para o ambiente de trabalho usando o comando `library("ggplot2")`. Para plotar qualquer gráfico no ggplot, a função `ggplot()` é usada, e você especifica o conjunto de dados, as variáveis x e y como atributos. Neste caso, usamos a função `geom_line()` porque queremos plotar um gráfico de linha.

![MaxWingspan-lineplot](../../../../../translated_images/br/MaxWingspan-lineplot.b12169f99d26fdd263f291008dfd73c18a4ba8f3d32b1fda3d74af51a0a28616.png)

O que você percebe imediatamente? Parece haver pelo menos um outlier - que envergadura impressionante! Uma envergadura de mais de 2000 centímetros equivale a mais de 20 metros - será que há Pterodáctilos em Minnesota? Vamos investigar.

Embora você possa fazer uma classificação rápida no Excel para encontrar esses outliers, que provavelmente são erros de digitação, continue o processo de visualização trabalhando diretamente no gráfico.

Adicione rótulos ao eixo x para mostrar quais tipos de pássaros estão em questão:

```r
ggplot(data=birds, aes(x=Name, y=MaxWingspan,group=1)) +
  geom_line() +
  theme(axis.text.x = element_text(angle = 45, hjust=1))+
  xlab("Birds") +
  ylab("Wingspan (CM)") +
  ggtitle("Max Wingspan in Centimeters")
```  
Especificamos o ângulo no `theme` e definimos os rótulos dos eixos x e y em `xlab()` e `ylab()`, respectivamente. O `ggtitle()` dá um nome ao gráfico.

![MaxWingspan-lineplot-improved](../../../../../translated_images/br/MaxWingspan-lineplot-improved.04b73b4d5a59552a6bc7590678899718e1f065abe9eada9ebb4148939b622fd4.png)

Mesmo com a rotação dos rótulos ajustada para 45 graus, ainda há muitos para ler. Vamos tentar uma estratégia diferente: rotular apenas os outliers e definir os rótulos dentro do gráfico. Você pode usar um gráfico de dispersão para criar mais espaço para os rótulos:

```r
ggplot(data=birds, aes(x=Name, y=MaxWingspan,group=1)) +
  geom_point() +
  geom_text(aes(label=ifelse(MaxWingspan>500,as.character(Name),'')),hjust=0,vjust=0) + 
  theme(axis.title.x=element_blank(), axis.text.x=element_blank(), axis.ticks.x=element_blank())
  ylab("Wingspan (CM)") +
  ggtitle("Max Wingspan in Centimeters") + 
```  
O que está acontecendo aqui? Você usou a função `geom_point()` para plotar pontos de dispersão. Com isso, você adicionou rótulos para os pássaros cuja `MaxWingspan > 500` e também ocultou os rótulos no eixo x para desobstruir o gráfico.

O que você descobre?

![MaxWingspan-scatterplot](../../../../../translated_images/br/MaxWingspan-scatterplot.60dc9e0e19d32700283558f253841fdab5104abb62bc96f7d97f9c0ee857fa8b.png)

## Filtre seus dados

Tanto a Águia-careca quanto o Falcão-das-pradarias, embora provavelmente sejam pássaros muito grandes, parecem estar rotulados incorretamente, com um zero extra adicionado à sua envergadura máxima. É improvável que você encontre uma Águia-careca com uma envergadura de 25 metros, mas, se encontrar, por favor, nos avise! Vamos criar um novo dataframe sem esses dois outliers:

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
Criamos um novo dataframe `birds_filtered` e, em seguida, plotamos um gráfico de dispersão. Ao filtrar os outliers, seus dados agora estão mais coesos e compreensíveis.

![MaxWingspan-scatterplot-improved](../../../../../translated_images/br/MaxWingspan-scatterplot-improved.7d0af81658c65f3e75b8fedeb2335399e31108257e48db15d875ece608272051.png)

Agora que temos um conjunto de dados mais limpo, pelo menos em termos de envergadura, vamos descobrir mais sobre esses pássaros.

Embora gráficos de linha e dispersão possam exibir informações sobre valores de dados e suas distribuições, queremos pensar nos valores inerentes a este conjunto de dados. Você poderia criar visualizações para responder às seguintes perguntas sobre quantidade:

> Quantas categorias de pássaros existem e quais são seus números?  
> Quantos pássaros estão extintos, ameaçados, raros ou comuns?  
> Quantos existem dos vários gêneros e ordens na terminologia de Lineu?  

## Explore gráficos de barras

Gráficos de barras são práticos quando você precisa mostrar agrupamentos de dados. Vamos explorar as categorias de pássaros que existem neste conjunto de dados para ver qual é a mais comum em número.  
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
No trecho a seguir, instalamos os pacotes [dplyr](https://www.rdocumentation.org/packages/dplyr/versions/0.7.8) e [lubridate](https://www.rdocumentation.org/packages/lubridate/versions/1.8.0) para ajudar a manipular e agrupar dados a fim de plotar um gráfico de barras empilhadas. Primeiro, agrupamos os dados pela `Categoria` do pássaro e, em seguida, resumimos as colunas `MinLength`, `MaxLength`, `MinBodyMass`, `MaxBodyMass`, `MinWingspan`, `MaxWingspan`. Depois, plotamos o gráfico de barras usando o pacote `ggplot2`, especificando as cores para as diferentes categorias e os rótulos.

![Stacked bar chart](../../../../../translated_images/br/stacked-bar-chart.0c92264e89da7b391a7490224d1e7059a020e8b74dcd354414aeac78871c02f1.png)

Este gráfico de barras, no entanto, é ilegível porque há muitos dados não agrupados. Você precisa selecionar apenas os dados que deseja plotar, então vamos observar o comprimento dos pássaros com base em sua categoria.

Filtre seus dados para incluir apenas a categoria do pássaro.

Como há muitas categorias, você pode exibir este gráfico verticalmente e ajustar sua altura para acomodar todos os dados:

```r
birds_count<-dplyr::count(birds_filtered, Category, sort = TRUE)
birds_count$Category <- factor(birds_count$Category, levels = birds_count$Category)
ggplot(birds_count,aes(Category,n))+geom_bar(stat="identity")+coord_flip()
```  
Primeiro, contamos os valores únicos na coluna `Categoria` e, em seguida, os classificamos em um novo dataframe `birds_count`. Esses dados classificados são então organizados no mesmo nível para que sejam plotados de forma ordenada. Usando o `ggplot2`, você então plota os dados em um gráfico de barras. O `coord_flip()` plota barras horizontais.

![category-length](../../../../../translated_images/br/category-length.7e34c296690e85d64f7e4d25a56077442683eca96c4f5b4eae120a64c0755636.png)

Este gráfico de barras mostra uma boa visão do número de pássaros em cada categoria. Em um piscar de olhos, você vê que o maior número de pássaros nesta região está na categoria Patos/Gansos/AvesAquáticas. Minnesota é a "terra dos 10.000 lagos", então isso não é surpreendente!

✅ Experimente outras contagens neste conjunto de dados. Algo te surpreende?

## Comparando dados

Você pode tentar diferentes comparações de dados agrupados criando novos eixos. Experimente uma comparação do ComprimentoMáximo de um pássaro, com base em sua categoria:

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
Agrupamos os dados `birds_filtered` por `Categoria` e, em seguida, plotamos um gráfico de barras.

![comparing data](../../../../../translated_images/br/comparingdata.f486a450d61c7ca5416f27f3f55a6a4465d00df3be5e6d33936e9b07b95e2fdd.png)

Nada surpreendente aqui: beija-flores têm o menor ComprimentoMáximo em comparação com Pelicanos ou Gansos. É bom quando os dados fazem sentido lógico!

Você pode criar visualizações mais interessantes de gráficos de barras sobrepondo dados. Vamos sobrepor os valores de ComprimentoMínimo e ComprimentoMáximo em uma determinada categoria de pássaro:

```r
ggplot(data=birds_grouped, aes(x=Category)) +
  geom_bar(aes(y=MaxLength), stat="identity", position ="identity",  fill='blue') +
  geom_bar(aes(y=MinLength), stat="identity", position="identity", fill='orange')+
  coord_flip()
```  
![super-imposed values](../../../../../translated_images/br/superimposed-values.5363f0705a1da4167625a373a1064331ea3cb7a06a297297d0734fcc9b3819a0.png)

## 🚀 Desafio

Este conjunto de dados de pássaros oferece uma riqueza de informações sobre diferentes tipos de pássaros dentro de um ecossistema específico. Pesquise na internet e veja se consegue encontrar outros conjuntos de dados relacionados a pássaros. Pratique a construção de gráficos e diagramas sobre esses pássaros para descobrir fatos que você não conhecia.  
## [Quiz pós-aula](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/17)

## Revisão e Autoestudo

Esta primeira lição forneceu algumas informações sobre como usar o `ggplot2` para visualizar quantidades. Pesquise outras maneiras de trabalhar com conjuntos de dados para visualização. Pesquise e procure por conjuntos de dados que você possa visualizar usando outros pacotes como [Lattice](https://stat.ethz.ch/R-manual/R-devel/library/lattice/html/Lattice.html) e [Plotly](https://github.com/plotly/plotly.R#readme).

## Tarefa  
[Linhas, Dispersões e Barras](assignment.md)  

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.