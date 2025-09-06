<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "42119bcc97bee88254e381156d770f3c",
  "translation_date": "2025-09-05T19:03:52+00:00",
  "source_file": "3-Data-Visualization/11-visualization-proportions/README.md",
  "language_code": "sr"
}
-->
# Визуализација пропорција

|![ Скетч од [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/11-Visualizing-Proportions.png)|
|:---:|
|Визуализација пропорција - _Скетч од [@nitya](https://twitter.com/nitya)_ |

У овој лекцији, користићете другачији сет података фокусиран на природу како бисте визуализовали пропорције, као што је број различитих врста гљива у датом сету података о печуркама. Истражимо ове фасцинантне гљиве користећи сет података из Audubon-а који садржи детаље о 23 врсте гљива са ламелама из породица Agaricus и Lepiota. Експериментисаћете са укусним визуализацијама као што су:

- Пита графикони 🥧
- Донат графикони 🍩
- Вафл графикони 🧇

> 💡 Веома занимљив пројекат под називом [Charticulator](https://charticulator.com) од Microsoft Research-а нуди бесплатан интерфејс за визуализацију података методом "превуци и пусти". У једном од њихових туторијала такође користе овај сет података о печуркама! Тако можете истражити податке и истовремено научити библиотеку: [Charticulator туторијал](https://charticulator.com/tutorials/tutorial4.html).

## [Квиз пре предавања](https://ff-quizzes.netlify.app/en/ds/quiz/20)

## Упознајте своје печурке 🍄

Печурке су веома занимљиве. Увезимо сет података да их проучимо:

```python
import pandas as pd
import matplotlib.pyplot as plt
mushrooms = pd.read_csv('../../data/mushrooms.csv')
mushrooms.head()
```
Табела се приказује са одличним подацима за анализу:


| class     | cap-shape | cap-surface | cap-color | bruises | odor    | gill-attachment | gill-spacing | gill-size | gill-color | stalk-shape | stalk-root | stalk-surface-above-ring | stalk-surface-below-ring | stalk-color-above-ring | stalk-color-below-ring | veil-type | veil-color | ring-number | ring-type | spore-print-color | population | habitat |
| --------- | --------- | ----------- | --------- | ------- | ------- | --------------- | ------------ | --------- | ---------- | ----------- | ---------- | ------------------------ | ------------------------ | ---------------------- | ---------------------- | --------- | ---------- | ----------- | --------- | ----------------- | ---------- | ------- |
| Отровна   | Конвексна | Глатка      | Браон     | Модрице | Јак мирис | Слободна        | Густа        | Уска      | Црна       | Широка      | Једнака    | Глатка                   | Глатка                   | Бела                   | Бела                   | Делимична | Бела       | Један       | Висећа    | Црна              | Расута     | Урбана  |
| Јестива   | Конвексна | Глатка      | Жута      | Модрице | Бадем    | Слободна        | Густа        | Широка    | Црна       | Широка      | Клупа      | Глатка                   | Глатка                   | Бела                   | Бела                   | Делимична | Бела       | Један       | Висећа    | Браон             | Бројна     | Трава   |
| Јестива   | Звонаста  | Глатка      | Бела      | Модрице | Анис     | Слободна        | Густа        | Широка    | Браон      | Широка      | Клупа      | Глатка                   | Глатка                   | Бела                   | Бела                   | Делимична | Бела       | Један       | Висећа    | Браон             | Бројна     | Ливаде  |
| Отровна   | Конвексна | Љускава     | Бела      | Модрице | Јак мирис | Слободна        | Густа        | Уска      | Браон      | Широка      | Једнака    | Глатка                   | Глатка                   | Бела                   | Бела                   | Делимична | Бела       | Један       | Висећа    | Црна              | Расута     | Урбана  |

Одмах примећујете да су сви подаци текстуални. Мораћете да конвертујете ове податке како бисте их могли користити у графикону. Већина података је, у ствари, представљена као објекат:

```python
print(mushrooms.select_dtypes(["object"]).columns)
```

Резултат је:

```output
Index(['class', 'cap-shape', 'cap-surface', 'cap-color', 'bruises', 'odor',
       'gill-attachment', 'gill-spacing', 'gill-size', 'gill-color',
       'stalk-shape', 'stalk-root', 'stalk-surface-above-ring',
       'stalk-surface-below-ring', 'stalk-color-above-ring',
       'stalk-color-below-ring', 'veil-type', 'veil-color', 'ring-number',
       'ring-type', 'spore-print-color', 'population', 'habitat'],
      dtype='object')
```
Узмите ове податке и конвертујте колону 'class' у категорију:

```python
cols = mushrooms.select_dtypes(["object"]).columns
mushrooms[cols] = mushrooms[cols].astype('category')
```

```python
edibleclass=mushrooms.groupby(['class']).count()
edibleclass
```

Сада, ако испишете податке о печуркама, можете видети да су груписани у категорије према класи отровна/јестива:


|           | cap-shape | cap-surface | cap-color | bruises | odor | gill-attachment | gill-spacing | gill-size | gill-color | stalk-shape | ... | stalk-surface-below-ring | stalk-color-above-ring | stalk-color-below-ring | veil-type | veil-color | ring-number | ring-type | spore-print-color | population | habitat |
| --------- | --------- | ----------- | --------- | ------- | ---- | --------------- | ------------ | --------- | ---------- | ----------- | --- | ------------------------ | ---------------------- | ---------------------- | --------- | ---------- | ----------- | --------- | ----------------- | ---------- | ------- |
| class     |           |             |           |         |      |                 |              |           |            |             |     |                          |                        |                        |           |            |             |           |                   |            |         |
| Јестива   | 4208      | 4208        | 4208      | 4208    | 4208 | 4208            | 4208         | 4208      | 4208       | 4208        | ... | 4208                     | 4208                   | 4208                   | 4208      | 4208       | 4208        | 4208      | 4208              | 4208       | 4208    |
| Отровна   | 3916      | 3916        | 3916      | 3916    | 3916 | 3916            | 3916         | 3916      | 3916       | 3916        | ... | 3916                     | 3916                   | 3916                   | 3916      | 3916       | 3916        | 3916      | 3916              | 3916       | 3916    |

Ако следите редослед представљен у овој табели за креирање ознака категорија класе, можете направити пита графикон:

## Пита!

```python
labels=['Edible','Poisonous']
plt.pie(edibleclass['population'],labels=labels,autopct='%.1f %%')
plt.title('Edible?')
plt.show()
```
Ето, пита графикон који приказује пропорције ових података према овим двема класама печурака. Веома је важно добити редослед ознака исправно, посебно овде, па обавезно проверите редослед којим је направљен низ ознака!

![пита графикон](../../../../3-Data-Visualization/11-visualization-proportions/images/pie1-wb.png)

## Донати!

Мало визуелно занимљивији пита графикон је донат графикон, који је пита графикон са рупом у средини. Погледајмо наше податке користећи овај метод.

Погледајте различита станишта где расту печурке:

```python
habitat=mushrooms.groupby(['habitat']).count()
habitat
```
Овде групишете своје податке према станишту. Постоји 7 наведених, па их користите као ознаке за ваш донат графикон:

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

![донат графикон](../../../../3-Data-Visualization/11-visualization-proportions/images/donut-wb.png)

Овај код црта графикон и централни круг, а затим додаје тај централни круг у графикон. Уредите ширину централног круга променом `0.40` на другу вредност.

Донат графикони могу се прилагодити на неколико начина како би се промениле ознаке. Ознаке се посебно могу истакнути ради боље читљивости. Сазнајте више у [документацији](https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_and_donut_labels.html?highlight=donut).

Сада када знате како да групишете своје податке и затим их прикажете као пита или донат, можете истражити друге типове графикона. Пробајте вафл графикон, који је само другачији начин истраживања количине.
## Вафли!

'Вафл' тип графикона је другачији начин визуализације количина као 2Д низ квадрата. Пробајте да визуализујете различите количине боја капа печурака у овом сету података. Да бисте то урадили, потребно је да инсталирате помоћну библиотеку под називом [PyWaffle](https://pypi.org/project/pywaffle/) и користите Matplotlib:

```python
pip install pywaffle
```

Изаберите сегмент својих података за груписање:

```python
capcolor=mushrooms.groupby(['cap-color']).count()
capcolor
```

Направите вафл графикон креирањем ознака и затим груписањем својих података:

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

Користећи вафл графикон, можете јасно видети пропорције боја капа у овом сету података о печуркама. Занимљиво је да постоји много печурака са зеленим капама!

![вафл графикон](../../../../3-Data-Visualization/11-visualization-proportions/images/waffle.png)

✅ Pywaffle подржава иконе унутар графикона које користе било коју икону доступну у [Font Awesome](https://fontawesome.com/). Урадите неке експерименте да направите још занимљивији вафл графикон користећи иконе уместо квадрата.

У овој лекцији, научили сте три начина за визуализацију пропорција. Прво, потребно је да групишете своје податке у категорије, а затим да одлучите који је најбољи начин за приказивање података - пита, донат или вафл. Сви су укусни и пружају кориснику тренутни снимак сета података.

## 🚀 Изазов

Пробајте да поново направите ове укусне графиконе у [Charticulator](https://charticulator.com).
## [Квиз после предавања](https://ff-quizzes.netlify.app/en/ds/quiz/21)

## Преглед и самостално учење

Понекад није очигледно када користити пита, донат или вафл графикон. Ево неких чланака за читање на ову тему:

https://www.beautiful.ai/blog/battle-of-the-charts-pie-chart-vs-donut-chart

https://medium.com/@hypsypops/pie-chart-vs-donut-chart-showdown-in-the-ring-5d24fd86a9ce

https://www.mit.edu/~mbarker/formula1/f1help/11-ch-c6.htm

https://medium.datadriveninvestor.com/data-visualization-done-the-right-way-with-tableau-waffle-chart-fdf2a19be402

Истражите и пронађите више информација о овој тешкој одлуци.
## Задатак

[Пробајте у Excel-у](assignment.md)

---

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем услуге за превођење помоћу вештачке интелигенције [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да обезбедимо тачност, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати меродавним извором. За критичне информације препоручује се професионални превод од стране људи. Не преузимамо одговорност за било каква погрешна тумачења или неспоразуме који могу настати услед коришћења овог превода.