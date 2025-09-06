<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "47028abaaafa2bcb1079702d20569066",
  "translation_date": "2025-08-24T22:57:22+00:00",
  "source_file": "3-Data-Visualization/R/11-visualization-proportions/README.md",
  "language_code": "pt"
}
-->
# Visualizar Proporções

|![ Sketchnote por [(@sketchthedocs)](https://sketchthedocs.dev) ](../../../sketchnotes/11-Visualizing-Proportions.png)|
|:---:|
|Visualizar Proporções - _Sketchnote por [@nitya](https://twitter.com/nitya)_ |

Nesta lição, vais utilizar um conjunto de dados focado na natureza para visualizar proporções, como, por exemplo, quantos tipos diferentes de fungos estão presentes num determinado conjunto de dados sobre cogumelos. Vamos explorar estes fascinantes fungos utilizando um conjunto de dados obtido da Audubon, que lista detalhes sobre 23 espécies de cogumelos com lâminas das famílias Agaricus e Lepiota. Vais experimentar visualizações interessantes como:

- Gráficos de pizza 🥧  
- Gráficos de rosca 🍩  
- Gráficos de waffle 🧇  

> 💡 Um projeto muito interessante chamado [Charticulator](https://charticulator.com) da Microsoft Research oferece uma interface gratuita de arrastar e soltar para visualizações de dados. Num dos seus tutoriais, eles também utilizam este conjunto de dados sobre cogumelos! Assim, podes explorar os dados e aprender a biblioteca ao mesmo tempo: [Tutorial do Charticulator](https://charticulator.com/tutorials/tutorial4.html).

## [Questionário pré-aula](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/20)

## Conhece os teus cogumelos 🍄

Os cogumelos são muito interessantes. Vamos importar um conjunto de dados para os estudar:

```r
mushrooms = read.csv('../../data/mushrooms.csv')
head(mushrooms)
```  
Uma tabela é exibida com alguns dados excelentes para análise:

| classe     | formato-do-chapéu | superfície-do-chapéu | cor-do-chapéu | hematomas | odor    | fixação-das-lâminas | espaçamento-das-lâminas | tamanho-das-lâminas | cor-das-lâminas | formato-do-pé | raiz-do-pé | superfície-acima-do-anel | superfície-abaixo-do-anel | cor-acima-do-anel | cor-abaixo-do-anel | tipo-de-véu | cor-do-véu | número-de-aneis | tipo-de-anel | cor-dos-esporos | população | habitat |
| --------- | ----------------- | -------------------- | ------------- | --------- | ------- | ------------------- | ----------------------- | ------------------- | --------------- | ------------- | ---------- | ------------------------ | ------------------------ | ----------------- | ----------------- | ----------- | ----------- | --------------- | ------------- | --------------- | --------- | ------- |
| Venenoso  | Convexo           | Liso                | Castanho      | Hematomas | Pungente | Livre              | Fechado                | Estreito           | Preto           | Alargado      | Igual       | Liso                     | Liso                     | Branco            | Branco            | Parcial     | Branco      | Um              | Pendente      | Preto            | Disperso  | Urbano  |
| Comestível| Convexo           | Liso                | Amarelo       | Hematomas | Amêndoa  | Livre              | Fechado                | Largo              | Preto           | Alargado      | Club        | Liso                     | Liso                     | Branco            | Branco            | Parcial     | Branco      | Um              | Pendente      | Castanho         | Numeroso  | Relvados |
| Comestível| Sino             | Liso                | Branco        | Hematomas | Anis     | Livre              | Fechado                | Largo              | Castanho        | Alargado      | Club        | Liso                     | Liso                     | Branco            | Branco            | Parcial     | Branco      | Um              | Pendente      | Castanho         | Numeroso  | Prados  |
| Venenoso  | Convexo           | Escamoso            | Branco        | Hematomas | Pungente | Livre              | Fechado                | Estreito           | Castanho        | Alargado      | Igual       | Liso                     | Liso                     | Branco            | Branco            | Parcial     | Branco      | Um              | Pendente      | Preto            | Disperso  | Urbano  |
| Comestível| Convexo           | Liso                | Verde         | Sem Hematomas | Nenhum | Livre              | Aglomerado             | Largo              | Preto           | Afunilado     | Igual       | Liso                     | Liso                     | Branco            | Branco            | Parcial     | Branco      | Um              | Evanescente   | Castanho         | Abundante | Relvados |
| Comestível| Convexo           | Escamoso            | Amarelo       | Hematomas | Amêndoa  | Livre              | Fechado                | Largo              | Castanho        | Alargado      | Club        | Liso                     | Liso                     | Branco            | Branco            | Parcial     | Branco      | Um              | Pendente      | Preto            | Numeroso  | Relvados |

De imediato, percebes que todos os dados são textuais. Terás de converter estes dados para os poderes utilizar num gráfico. Na verdade, a maior parte dos dados está representada como um objeto:

```r
names(mushrooms)
```

O resultado é:

```output
[1] "class"                    "cap.shape"               
 [3] "cap.surface"              "cap.color"               
 [5] "bruises"                  "odor"                    
 [7] "gill.attachment"          "gill.spacing"            
 [9] "gill.size"                "gill.color"              
[11] "stalk.shape"              "stalk.root"              
[13] "stalk.surface.above.ring" "stalk.surface.below.ring"
[15] "stalk.color.above.ring"   "stalk.color.below.ring"  
[17] "veil.type"                "veil.color"              
[19] "ring.number"              "ring.type"               
[21] "spore.print.color"        "population"              
[23] "habitat"            
```  
Converte os dados da coluna 'class' para uma categoria:

```r
library(dplyr)
grouped=mushrooms %>%
  group_by(class) %>%
  summarise(count=n())
```

Agora, se imprimires os dados dos cogumelos, podes ver que foram agrupados em categorias de acordo com a classe venenoso/comestível:  
```r
View(grouped)
```

| classe | contagem |
| --------- | --------- |
| Comestível | 4208 |
| Venenoso   | 3916 |

Se seguires a ordem apresentada nesta tabela para criar as etiquetas das categorias, podes construir um gráfico de pizza.

## Pizza!

```r
pie(grouped$count,grouped$class, main="Edible?")
```  
Voilà, um gráfico de pizza que mostra as proporções destes dados de acordo com estas duas classes de cogumelos. É muito importante garantir que a ordem das etiquetas esteja correta, especialmente aqui, por isso verifica sempre a ordem com que o array de etiquetas é construído!

![gráfico de pizza](../../../../../translated_images/pie1-wb.685df063673751f4b0b82127f7a52c7f9a920192f22ae61ad28412ba9ace97bf.pt.png)

## Roscas!

Um gráfico de pizza um pouco mais interessante visualmente é o gráfico de rosca, que é um gráfico de pizza com um buraco no meio. Vamos observar os nossos dados utilizando este método.

Observa os vários habitats onde os cogumelos crescem:

```r
library(dplyr)
habitat=mushrooms %>%
  group_by(habitat) %>%
  summarise(count=n())
View(habitat)
```  
O resultado é:  
| habitat | contagem |
| --------- | --------- |
| Relvados  | 2148 |
| Folhas    | 832 |
| Prados    | 292 |
| Trilhos   | 1144 |
| Urbano    | 368 |
| Resíduos  | 192 |
| Madeira   | 3148 |

Aqui, estás a agrupar os teus dados por habitat. Existem 7 listados, por isso utiliza-os como etiquetas para o teu gráfico de rosca:

```r
library(ggplot2)
library(webr)
PieDonut(habitat, aes(habitat, count=count))
```

![gráfico de rosca](../../../../../translated_images/donut-wb.34e6fb275da9d834c2205145e39a3de9b6878191dcdba6f7a9e85f4b520449bc.pt.png)

Este código utiliza duas bibliotecas - ggplot2 e webr. Usando a função PieDonut da biblioteca webr, podemos criar um gráfico de rosca facilmente!

Os gráficos de rosca em R também podem ser feitos utilizando apenas a biblioteca ggplot2. Podes aprender mais sobre isso [aqui](https://www.r-graph-gallery.com/128-ring-or-donut-plot.html) e experimentar por ti mesmo.

Agora que sabes como agrupar os teus dados e depois exibi-los como um gráfico de pizza ou rosca, podes explorar outros tipos de gráficos. Experimenta um gráfico de waffle, que é apenas uma forma diferente de explorar quantidades.

## Waffles!

Um gráfico do tipo 'waffle' é uma forma diferente de visualizar quantidades como uma matriz 2D de quadrados. Experimenta visualizar as diferentes quantidades de cores do chapéu dos cogumelos neste conjunto de dados. Para isso, precisas de instalar uma biblioteca auxiliar chamada [waffle](https://cran.r-project.org/web/packages/waffle/waffle.pdf) e utilizá-la para gerar a tua visualização:

```r
install.packages("waffle", repos = "https://cinc.rud.is")
```

Seleciona um segmento dos teus dados para agrupar:

```r
library(dplyr)
cap_color=mushrooms %>%
  group_by(cap.color) %>%
  summarise(count=n())
View(cap_color)
```

Cria um gráfico de waffle criando etiquetas e depois agrupando os teus dados:

```r
library(waffle)
names(cap_color$count) = paste0(cap_color$cap.color)
waffle((cap_color$count/10), rows = 7, title = "Waffle Chart")+scale_fill_manual(values=c("brown", "#F0DC82", "#D2691E", "green", 
                                                                                     "pink", "purple", "red", "grey", 
                                                                                     "yellow","white"))
```

Usando um gráfico de waffle, podes ver claramente as proporções das cores dos chapéus neste conjunto de dados de cogumelos. Curiosamente, existem muitos cogumelos com chapéus verdes!

![gráfico de waffle](../../../../../translated_images/waffle.aaa75c5337735a6ef32ace0ffb6506ef49e5aefe870ffd72b1bb080f4843c217.pt.png)

Nesta lição, aprendeste três formas de visualizar proporções. Primeiro, precisas de agrupar os teus dados em categorias e depois decidir qual é a melhor forma de exibir os dados - pizza, rosca ou waffle. Todas são deliciosas e oferecem ao utilizador uma visão instantânea de um conjunto de dados.

## 🚀 Desafio

Tenta recriar estes gráficos deliciosos no [Charticulator](https://charticulator.com).  
## [Questionário pós-aula](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/21)

## Revisão e Autoestudo

Por vezes, não é óbvio quando usar um gráfico de pizza, rosca ou waffle. Aqui estão alguns artigos para leres sobre este tema:

https://www.beautiful.ai/blog/battle-of-the-charts-pie-chart-vs-donut-chart

https://medium.com/@hypsypops/pie-chart-vs-donut-chart-showdown-in-the-ring-5d24fd86a9ce

https://www.mit.edu/~mbarker/formula1/f1help/11-ch-c6.htm

https://medium.datadriveninvestor.com/data-visualization-done-the-right-way-with-tableau-waffle-chart-fdf2a19be402

Faz alguma pesquisa para encontrares mais informações sobre esta decisão difícil.

## Tarefa

[Experimenta no Excel](assignment.md)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original no seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se uma tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes do uso desta tradução.