<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cc490897ee2d276870472bcb31602d03",
  "translation_date": "2025-09-04T13:45:05+00:00",
  "source_file": "3-Data-Visualization/11-visualization-proportions/README.md",
  "language_code": "pt"
}
-->
# Visualizar Proporções

|![ Sketchnote por [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/11-Visualizing-Proportions.png)|
|:---:|
|Visualizar Proporções - _Sketchnote por [@nitya](https://twitter.com/nitya)_ |

Nesta lição, vais usar um conjunto de dados com foco na natureza para visualizar proporções, como o número de diferentes tipos de fungos que compõem um conjunto de dados sobre cogumelos. Vamos explorar estes fascinantes fungos utilizando um conjunto de dados obtido da Audubon, que lista detalhes sobre 23 espécies de cogumelos com lamelas das famílias Agaricus e Lepiota. Vais experimentar visualizações apelativas como:

- Gráficos de pizza 🥧
- Gráficos de donut 🍩
- Gráficos de waffle 🧇

> 💡 Um projeto muito interessante chamado [Charticulator](https://charticulator.com) da Microsoft Research oferece uma interface gratuita de arrastar e soltar para visualizações de dados. Num dos seus tutoriais, eles também utilizam este conjunto de dados sobre cogumelos! Assim, podes explorar os dados e aprender a biblioteca ao mesmo tempo: [Tutorial do Charticulator](https://charticulator.com/tutorials/tutorial4.html).

## [Questionário pós-aula](https://ff-quizzes.netlify.app/en/ds/)

## Conhece os teus cogumelos 🍄

Os cogumelos são muito interessantes. Vamos importar um conjunto de dados para estudá-los:

```python
import pandas as pd
import matplotlib.pyplot as plt
mushrooms = pd.read_csv('../../data/mushrooms.csv')
mushrooms.head()
```
Uma tabela é exibida com alguns dados excelentes para análise:

| class     | cap-shape | cap-surface | cap-color | bruises | odor    | gill-attachment | gill-spacing | gill-size | gill-color | stalk-shape | stalk-root | stalk-surface-above-ring | stalk-surface-below-ring | stalk-color-above-ring | stalk-color-below-ring | veil-type | veil-color | ring-number | ring-type | spore-print-color | population | habitat |
| --------- | --------- | ----------- | --------- | ------- | ------- | --------------- | ------------ | --------- | ---------- | ----------- | ---------- | ------------------------ | ------------------------ | ---------------------- | ---------------------- | --------- | ---------- | ----------- | --------- | ----------------- | ---------- | ------- |
| Poisonous | Convex    | Smooth      | Brown     | Bruises | Pungent | Free            | Close        | Narrow    | Black      | Enlarging   | Equal      | Smooth                   | Smooth                   | White                  | White                  | Partial   | White      | One         | Pendant   | Black             | Scattered  | Urban   |
| Edible    | Convex    | Smooth      | Yellow    | Bruises | Almond  | Free            | Close        | Broad     | Black      | Enlarging   | Club       | Smooth                   | Smooth                   | White                  | White                  | Partial   | White      | One         | Pendant   | Brown             | Numerous   | Grasses |
| Edible    | Bell      | Smooth      | White     | Bruises | Anise   | Free            | Close        | Broad     | Brown      | Enlarging   | Club       | Smooth                   | Smooth                   | White                  | White                  | Partial   | White      | One         | Pendant   | Brown             | Numerous   | Meadows |
| Poisonous | Convex    | Scaly       | White     | Bruises | Pungent | Free            | Close        | Narrow    | Brown      | Enlarging   | Equal      | Smooth                   | Smooth                   | White                  | White                  | Partial   | White      | One         | Pendant   | Black             | Scattered  | Urban   |

De imediato, percebes que todos os dados são textuais. Vais precisar converter estes dados para poder utilizá-los num gráfico. Na verdade, a maior parte dos dados está representada como um objeto:

```python
print(mushrooms.select_dtypes(["object"]).columns)
```

O resultado é:

```output
Index(['class', 'cap-shape', 'cap-surface', 'cap-color', 'bruises', 'odor',
       'gill-attachment', 'gill-spacing', 'gill-size', 'gill-color',
       'stalk-shape', 'stalk-root', 'stalk-surface-above-ring',
       'stalk-surface-below-ring', 'stalk-color-above-ring',
       'stalk-color-below-ring', 'veil-type', 'veil-color', 'ring-number',
       'ring-type', 'spore-print-color', 'population', 'habitat'],
      dtype='object')
```
Converte os dados da coluna 'class' para uma categoria:

```python
cols = mushrooms.select_dtypes(["object"]).columns
mushrooms[cols] = mushrooms[cols].astype('category')
```

```python
edibleclass=mushrooms.groupby(['class']).count()
edibleclass
```

Agora, se imprimires os dados dos cogumelos, podes ver que foram agrupados em categorias de acordo com a classe venenoso/comestível:

|           | cap-shape | cap-surface | cap-color | bruises | odor | gill-attachment | gill-spacing | gill-size | gill-color | stalk-shape | ... | stalk-surface-below-ring | stalk-color-above-ring | stalk-color-below-ring | veil-type | veil-color | ring-number | ring-type | spore-print-color | population | habitat |
| --------- | --------- | ----------- | --------- | ------- | ---- | --------------- | ------------ | --------- | ---------- | ----------- | --- | ------------------------ | ---------------------- | ---------------------- | --------- | ---------- | ----------- | --------- | ----------------- | ---------- | ------- |
| class     |           |             |           |         |      |                 |              |           |            |             |     |                          |                        |                        |           |            |             |           |                   |            |         |
| Edible    | 4208      | 4208        | 4208      | 4208    | 4208 | 4208            | 4208         | 4208      | 4208       | 4208        | ... | 4208                     | 4208                   | 4208                   | 4208      | 4208       | 4208        | 4208      | 4208              | 4208       | 4208    |
| Poisonous | 3916      | 3916        | 3916      | 3916    | 3916 | 3916            | 3916         | 3916      | 3916       | 3916        | ... | 3916                     | 3916                   | 3916                   | 3916      | 3916       | 3916        | 3916      | 3916              | 3916       | 3916    |

Se seguires a ordem apresentada nesta tabela para criar os rótulos da categoria 'class', podes construir um gráfico de pizza:

## Pizza!

```python
labels=['Edible','Poisonous']
plt.pie(edibleclass['population'],labels=labels,autopct='%.1f %%')
plt.title('Edible?')
plt.show()
```
Voilá, um gráfico de pizza mostrando as proporções destes dados de acordo com estas duas classes de cogumelos. É bastante importante obter a ordem dos rótulos correta, especialmente aqui, por isso certifica-te de verificar a ordem com que o array de rótulos é construído!

![pie chart](../../../../translated_images/pie1-wb.e201f2fcc335413143ce37650fb7f5f0bb21358e7823a327ed8644dfb84be9db.pt.png)

## Donuts!

Um gráfico de pizza visualmente mais interessante é o gráfico de donut, que é um gráfico de pizza com um buraco no meio. Vamos olhar para os nossos dados usando este método.

Observa os vários habitats onde os cogumelos crescem:

```python
habitat=mushrooms.groupby(['habitat']).count()
habitat
```
Aqui, estás a agrupar os teus dados por habitat. Existem 7 listados, por isso usa-os como rótulos para o teu gráfico de donut:

```python
labels=['Grasses','Leaves','Meadows','Paths','Urban','Waste','Wood']

plt.pie(habitat['class'], labels=labels,
        autopct='%1.1f%%', pctdistance=0.85)
  
center_circle = plt.Circle((0, 0), 0.40, fc='white')
fig = plt.gcf()

fig.gca().add_artist(center_circle)
  
plt.title('Mushroom Habitats')
  
plt.show()
```

![donut chart](../../../../translated_images/donut-wb.be3c12a22712302b5d10c40014d5389d4a1ae4412fe1655b3cf4af57b64f799a.pt.png)

Este código desenha um gráfico e um círculo central, depois adiciona esse círculo central ao gráfico. Edita a largura do círculo central alterando `0.40` para outro valor.

Os gráficos de donut podem ser ajustados de várias formas para alterar os rótulos. Os rótulos, em particular, podem ser destacados para melhorar a legibilidade. Aprende mais nos [docs](https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_and_donut_labels.html?highlight=donut).

Agora que sabes como agrupar os teus dados e depois exibi-los como pizza ou donut, podes explorar outros tipos de gráficos. Experimenta um gráfico de waffle, que é apenas uma forma diferente de explorar quantidades.

## Waffles!

Um gráfico do tipo 'waffle' é uma forma diferente de visualizar quantidades como uma matriz 2D de quadrados. Experimenta visualizar as diferentes quantidades de cores de chapéus de cogumelos neste conjunto de dados. Para isso, precisas de instalar uma biblioteca auxiliar chamada [PyWaffle](https://pypi.org/project/pywaffle/) e usar Matplotlib:

```python
pip install pywaffle
```

Seleciona um segmento dos teus dados para agrupar:

```python
capcolor=mushrooms.groupby(['cap-color']).count()
capcolor
```

Cria um gráfico de waffle criando rótulos e depois agrupando os teus dados:

```python
import pandas as pd
import matplotlib.pyplot as plt
from pywaffle import Waffle
  
data ={'color': ['brown', 'buff', 'cinnamon', 'green', 'pink', 'purple', 'red', 'white', 'yellow'],
    'amount': capcolor['class']
     }
  
df = pd.DataFrame(data)
  
fig = plt.figure(
    FigureClass = Waffle,
    rows = 100,
    values = df.amount,
    labels = list(df.color),
    figsize = (30,30),
    colors=["brown", "tan", "maroon", "green", "pink", "purple", "red", "whitesmoke", "yellow"],
)
```

Usando um gráfico de waffle, podes ver claramente as proporções das cores dos chapéus neste conjunto de dados de cogumelos. Curiosamente, há muitos cogumelos com chapéus verdes!

![waffle chart](../../../../translated_images/waffle.5455dbae4ccf17d53bb40ff0a657ecef7b8aa967e27a19cc96325bd81598f65e.pt.png)

✅ Pywaffle suporta ícones dentro dos gráficos que utilizam qualquer ícone disponível no [Font Awesome](https://fontawesome.com/). Faz algumas experiências para criar um gráfico de waffle ainda mais interessante usando ícones em vez de quadrados.

Nesta lição, aprendeste três formas de visualizar proporções. Primeiro, precisas de agrupar os teus dados em categorias e depois decidir qual é a melhor forma de exibir os dados - pizza, donut ou waffle. Todos são deliciosos e proporcionam ao utilizador uma visão instantânea de um conjunto de dados.

## 🚀 Desafio

Tenta recriar estes gráficos apelativos no [Charticulator](https://charticulator.com).
## [Questionário pós-aula](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/21)

## Revisão & Autoestudo

Por vezes, não é óbvio quando usar um gráfico de pizza, donut ou waffle. Aqui estão alguns artigos para ler sobre este tema:

https://www.beautiful.ai/blog/battle-of-the-charts-pie-chart-vs-donut-chart

https://medium.com/@hypsypops/pie-chart-vs-donut-chart-showdown-in-the-ring-5d24fd86a9ce

https://www.mit.edu/~mbarker/formula1/f1help/11-ch-c6.htm

https://medium.datadriveninvestor.com/data-visualization-done-the-right-way-with-tableau-waffle-chart-fdf2a19be402

Faz alguma pesquisa para encontrar mais informações sobre esta decisão difícil.

## Tarefa

[Experimenta no Excel](assignment.md)

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original no seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se uma tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes do uso desta tradução.