# Visualizing Proportions
# 비율 시각화

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/11-Visualizing-Proportions.png)|
|:---:|
|Visualizing Proportions - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |
|비율 시각화 - _제작자 : [@nitya](https://twitter.com/nitya)_ |

In this lesson, you will use a different nature-focused dataset to visualize proportions, such as how many different types of fungi populate a given dataset about mushrooms. Let's explore these fascinating fungi using a dataset sourced from Audubon listing details about 23 species of gilled mushrooms in the Agaricus and Lepiota families. You will experiment with tasty visualizations such as:
이 과정에서는 버섯에 대해 주어진 데이터셋에 얼마나 많은 종류의 곰팡이가 채워져 있는지와 같은 다른 자연에 초점을 맞춘 데이터셋을 사용하여 비율을 시각화합니다. Agaricus와 Lepiota과에 속하는 23종의 구이버섯에 대한 세부 정보를 나열한 Audubon의 데이터셋을 이용하여 이 매력적인 곰팡이를 탐험해 봅시다. 다음과 같은 맛있는 시각화를 실험하게 됩니다.

- Pie charts 🥧
- Donut charts 🍩
- Waffle charts 🧇
- 원형 차트 🥧
- 도넛 차트 🍩
- 와플 차트 🧇

> 💡 A very interesting project called [Charticulator](https://charticulator.com) by Microsoft Research offers a free drag and drop interface for data visualizations. In one of their tutorials they also use this mushroom dataset! So you can explore the data and learn the library at the same time: [Charticulator tutorial](https://charticulator.com/tutorials/tutorial4.html).
> 💡 Microsoft Research의 [Charticulator](https://charticulator.com)라는 매우 흥미로운 프로젝트는 데이터 시각화를 위한 무료 끌어 놓기(드래그 앤 드랍) 인터페이스를 제공합니다. 튜토리얼 중 하나에서는 버섯 데이터 세트도 사용합니다! 따라서 데이터를 탐색하면서 라이브러리를 동시에 학습할 수 있습니다. [Charticulator tutorial](https://charticulator.com/tutorials/tutorial4.html).

## [Pre-lecture quiz](https://red-water-0103e7a0f.azurestaticapps.net/quiz/20)
## [사전 강의 퀴즈](https://red-water-0103e7a0f.azurestaticapps.net/quiz/20)

## Get to know your mushrooms 🍄
## 버섯을 알아가세요 🍄

Mushrooms are very interesting. Let's import a dataset to study them:
버섯은 매우 흥미롭습니다. 데이터셋을 가져와 연구해 보겠습니다.

```python
import pandas as pd
import matplotlib.pyplot as plt
mushrooms = pd.read_csv('../../data/mushrooms.csv')
mushrooms.head()
```
A table is printed out with some great data for analysis:
분석을 위한 몇 가지 훌륭한 데이터가 포함된 표가 인쇄됩니다:


| class     | cap-shape | cap-surface | cap-color | bruises | odor    | gill-attachment | gill-spacing | gill-size | gill-color | stalk-shape | stalk-root | stalk-surface-above-ring | stalk-surface-below-ring | stalk-color-above-ring | stalk-color-below-ring | veil-type | veil-color | ring-number | ring-type | spore-print-color | population | habitat |
| --------- | --------- | ----------- | --------- | ------- | ------- | --------------- | ------------ | --------- | ---------- | ----------- | ---------- | ------------------------ | ------------------------ | ---------------------- | ---------------------- | --------- | ---------- | ----------- | --------- | ----------------- | ---------- | ------- |
| Poisonous | Convex    | Smooth      | Brown     | Bruises | Pungent | Free            | Close        | Narrow    | Black      | Enlarging   | Equal      | Smooth                   | Smooth                   | White                  | White                  | Partial   | White      | One         | Pendant   | Black             | Scattered  | Urban   |
| Edible    | Convex    | Smooth      | Yellow    | Bruises | Almond  | Free            | Close        | Broad     | Black      | Enlarging   | Club       | Smooth                   | Smooth                   | White                  | White                  | Partial   | White      | One         | Pendant   | Brown             | Numerous   | Grasses |
| Edible    | Bell      | Smooth      | White     | Bruises | Anise   | Free            | Close        | Broad     | Brown      | Enlarging   | Club       | Smooth                   | Smooth                   | White                  | White                  | Partial   | White      | One         | Pendant   | Brown             | Numerous   | Meadows |
| Poisonous | Convex    | Scaly       | White     | Bruises | Pungent | Free            | Close        | Narrow    | Brown      | Enlarging   | Equal      | Smooth                   | Smooth                   | White                  | White                  | Partial   | White      | One         | Pendant   | Black             | Scattered  | Urban   |

Right away, you notice that all the data is textual. You will have to convert this data to be able to use it in a chart. Most of the data, in fact, is represented as an object:
바로, 모든 데이터가 텍스트임을 알 수 있습니다. 이 데이터를 차트에서 사용하려면 데이터를 변환해야 합니다. 실제로 대부분의 데이터는 개체로 표현됩니다:

```python
print(mushrooms.select_dtypes(["object"]).columns)
```

The output is:
출력은 다음과 같습니다:

```output
Index(['class', 'cap-shape', 'cap-surface', 'cap-color', 'bruises', 'odor',
       'gill-attachment', 'gill-spacing', 'gill-size', 'gill-color',
       'stalk-shape', 'stalk-root', 'stalk-surface-above-ring',
       'stalk-surface-below-ring', 'stalk-color-above-ring',
       'stalk-color-below-ring', 'veil-type', 'veil-color', 'ring-number',
       'ring-type', 'spore-print-color', 'population', 'habitat'],
      dtype='object')
```
Take this data and convert the 'class' column to a category:
이 데이터를 가져와서 '클래스' 열을 범주로 변환합니다:

```python
cols = mushrooms.select_dtypes(["object"]).columns
mushrooms[cols] = mushrooms[cols].astype('category')
```
Now, if you print out the mushrooms data, you can see that it has been grouped into categories according to the poisonous/edible class:
이제 버섯 데이터를 인쇄하면 poisonous/editable 클래스에 따라 범주로 분류되었음을 알 수 있습니다:


|           | cap-shape | cap-surface | cap-color | bruises | odor | gill-attachment | gill-spacing | gill-size | gill-color | stalk-shape | ... | stalk-surface-below-ring | stalk-color-above-ring | stalk-color-below-ring | veil-type | veil-color | ring-number | ring-type | spore-print-color | population | habitat |
| --------- | --------- | ----------- | --------- | ------- | ---- | --------------- | ------------ | --------- | ---------- | ----------- | --- | ------------------------ | ---------------------- | ---------------------- | --------- | ---------- | ----------- | --------- | ----------------- | ---------- | ------- |
| class     |           |             |           |         |      |                 |              |           |            |             |     |                          |                        |                        |           |            |             |           |                   |            |         |
| Edible    | 4208      | 4208        | 4208      | 4208    | 4208 | 4208            | 4208         | 4208      | 4208       | 4208        | ... | 4208                     | 4208                   | 4208                   | 4208      | 4208       | 4208        | 4208      | 4208              | 4208       | 4208    |
| Poisonous | 3916      | 3916        | 3916      | 3916    | 3916 | 3916            | 3916         | 3916      | 3916       | 3916        | ... | 3916                     | 3916                   | 3916                   | 3916      | 3916       | 3916        | 3916      | 3916              | 3916       | 3916    |

If you follow the order presented in this table to create your class category labels, you can build a pie chart:
이 표에 나와 있는 순서에 따라 클래스 범주 레이블을 만들면 파이 차트를 작성할 수 있습니다:

## Pie!
## 파이!

```python
labels=['Edible','Poisonous']
plt.pie(edibleclass['population'],labels=labels,autopct='%.1f %%')
plt.title('Edible?')
plt.show()
```
Voila, a pie chart showing the proportions of this data according to these two classes of mushrooms. It's quite important to get the order of the labels correct, especially here, so be sure to verify the order with which the label array is built!

![pie chart](images/pie1.png)
![파이 차트](images/pie1.png)

## Donuts!
## 도넛!

A somewhat more visually interesting pie chart is a donut chart, which is a pie chart with a hole in the middle. Let's look at our data using this method.
좀 더 시각적으로 흥미로운 파이 차트는 도넛 차트입니다. 이것은 가운데에 구멍이 있는 파이 차트입니다. 이 방법을 사용하여 우리의 데이터를 살펴봅시다.

Take a look at the various habitats where mushrooms grow:
버섯이 자라는 다양한 서식지를 살펴보세요:

```python
habitat=mushrooms.groupby(['habitat']).count()
habitat
```
Here, you are grouping your data by habitat. There are 7 listed, so use those as labels for your donut chart:
여기서는 서식지에 따라 데이터를 그룹화합니다. 7개가 나열되어 있으므로 도넛 차트의 레이블로 사용합니다:

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

![donut chart](images/donut.png)
![도넛 차트](images/donut.png)

This code draws a chart and a center circle, then adds that center circle in the chart. Edit the width of the center circle by changing `0.40` to another value.
이 코드는 차트와 중심 원을 그리고, 차트에 해당 중심 원을 추가합니다. 0.40을 다른 값으로 변경하여 중심 원의 너비를 편집합니다.

Donut charts can be tweaked in several ways to change the labels. The labels in particular can be highlighted for readability. Learn more in the [docs](https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_and_donut_labels.html?highlight=donut).
도넛 차트는 레이블을 변경하기 위해 여러 가지 방법으로 수정할 수 있습니다. 특히 라벨은 가독성을 위해 강조 표시할 수 있습니다. 자세한 내용은 [https](https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_and_donut_labels.html?highlight=donut))에서 확인하십시오.

Now that you know how to group your data and then display it as a pie or donut, you can explore other types of charts. Try a waffle chart, which is just a different way of exploring quantity.
## Waffles!
이제 데이터를 그룹화한 다음 파이 또는 도넛으로 표시하는 방법을 알았으므로 다른 유형의 차트를 살펴볼 수 있습니다. 양을 탐구하는 다른 방법인 와플 차트를 시도해 보세요.
## 와플!

A 'waffle' type chart is a different way to visualize quantities as a 2D array of squares. Try visualizing the different quantities of mushroom cap colors in this dataset. To do this, you need to install a helper library called [PyWaffle](https://pypi.org/project/pywaffle/) and use Matplotlib:
'와플' 유형 차트는 양을 2D 정사각형 배열로 시각화하는 다른 방법입니다. 이 데이터셋에 있는 버섯 머리 색상의 다양한 양을 시각화해 보십시오. 이렇게 하려면 [PyWaffle](https://pypi.org/project/pywaffle/)이라는 도우미 라이브러리를 설치하고 Matplotlib을 사용해야 합니다:

```python
pip install pywaffle
```

Select a segment of your data to group:
그룹화할 데이터의 부분 선택:

```python
capcolor=mushrooms.groupby(['cap-color']).count()
capcolor
```

Create a waffle chart by creating labels and then grouping your data:
레이블을 만든 다음 데이터를 그룹화하여 와플 차트를 만듭니다:

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

Using a waffle chart, you can plainly see the proportions of cap colors of this mushrooms dataset. Interestingly, there are many green-capped mushrooms!
와플 차트를 사용하면 이 버섯 데이터셋의 머리 색상 비율을 쉽게 알 수 있습니다. 흥미롭게도, 녹색 머리가 있는 버섯이 많이 있답니다!

![waffle chart](images/waffle.png)
![와플 차트](images/waffle.png)


✅ Pywaffle supports icons within the charts that use any icon available in [Font Awesome](https://fontawesome.com/). Do some experiments to create an even more interesting waffle chart using icons instead of squares.
✅ Pywaffle은 차트 내에서 [Font Awesome](https://fontawesome.com/))에서 사용할 수 있는 아이콘을 지원합니다. 정사각형 대신 아이콘을 사용하여 훨씬 더 흥미로운 와플 차트를 만들기 위해 몇 가지 실험을 해보세요.

In this lesson, you learned three ways to visualize proportions. First, you need to group your data into categories and then decide which is the best way to display the data - pie, donut, or waffle. All are delicious and gratify the user with an instant snapshot of a dataset.
이 과정에서는 비율을 시각화하는 세 가지 방법을 배웠습니다. 먼저 데이터를 범주로 분류한 다음 파이, 도넛 또는 와플 중 어떤 것이 데이터를 표시하는 가장 좋은 방법인지 결정해야 합니다. 이 모든 것이 맛있고 데이터셋의 즉각적인 스냅샷으로 사용자를 만족시킵니다.

## 🚀 Challenge
## 🚀 도전

Try recreating these tasty charts in [Charticulator](https://charticulator.com).
## [Post-lecture quiz](https://red-water-0103e7a0f.azurestaticapps.net/quiz/21)
[Charticulator](https://charticulator.com)에서 맛있는 차트를 다시 만들어 보십시오.
## [강의 후 퀴즈](https://red-water-0103e7a0f.azurestaticapps.net/quiz/21)

## Review & Self Study
## 리뷰 & 셀프 학습

Sometimes it's not obvious when to use a pie, donut, or waffle chart. Here are some articles to read on this topic:
때때로 언제 파이, 도넛, 와플 차트를 사용해야 하는지 명확하지 않다. 다음은 이 주제에 대해 읽을 몇 가지 기사입니다:

https://www.beautiful.ai/blog/battle-of-the-charts-pie-chart-vs-donut-chart

https://medium.com/@hypsypops/pie-chart-vs-donut-chart-showdown-in-the-ring-5d24fd86a9ce

https://www.mit.edu/~mbarker/formula1/f1help/11-ch-c6.htm

https://medium.datadriveninvestor.com/data-visualization-done-the-right-way-with-tableau-waffle-chart-fdf2a19be402

Do some research to find more information on this sticky decision.
## Assignment
이 까다로운 결정에 대한 더 많은 정보를 찾기 위해 조사를 하세요.
## 과제

[Try it in Excel](assignment.md)
[엑셀로 도전해보세요](assignment.md)
