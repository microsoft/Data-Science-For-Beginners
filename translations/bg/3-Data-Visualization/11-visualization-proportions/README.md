<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "42119bcc97bee88254e381156d770f3c",
  "translation_date": "2025-09-05T18:44:49+00:00",
  "source_file": "3-Data-Visualization/11-visualization-proportions/README.md",
  "language_code": "bg"
}
-->
# Визуализиране на пропорции

|![ Скетч от [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/11-Visualizing-Proportions.png)|
|:---:|
|Визуализиране на пропорции - _Скетч от [@nitya](https://twitter.com/nitya)_ |

В този урок ще използвате различен набор от данни, свързан с природата, за да визуализирате пропорции, като например колко различни видове гъби се срещат в даден набор от данни за гъби. Нека разгледаме тези очарователни гъби, използвайки набор от данни, предоставен от Audubon, който съдържа информация за 23 вида ламелни гъби от семействата Agaricus и Lepiota. Ще експериментирате с апетитни визуализации като:

- Кръгови диаграми 🥧
- Диаграми тип "поничка" 🍩
- Диаграми тип "вафла" 🧇

> 💡 Един много интересен проект, наречен [Charticulator](https://charticulator.com) от Microsoft Research, предлага безплатен интерфейс за визуализация на данни чрез влачене и пускане. В един от техните уроци те също използват този набор от данни за гъби! Така можете да изследвате данните и да научите библиотеката едновременно: [Charticulator tutorial](https://charticulator.com/tutorials/tutorial4.html).

## [Тест преди лекцията](https://ff-quizzes.netlify.app/en/ds/quiz/20)

## Запознайте се с вашите гъби 🍄

Гъбите са много интересни. Нека импортираме набор от данни, за да ги изучим:

```python
import pandas as pd
import matplotlib.pyplot as plt
mushrooms = pd.read_csv('../../data/mushrooms.csv')
mushrooms.head()
```
Таблица се отпечатва с чудесни данни за анализ:


| class     | cap-shape | cap-surface | cap-color | bruises | odor    | gill-attachment | gill-spacing | gill-size | gill-color | stalk-shape | stalk-root | stalk-surface-above-ring | stalk-surface-below-ring | stalk-color-above-ring | stalk-color-below-ring | veil-type | veil-color | ring-number | ring-type | spore-print-color | population | habitat |
| --------- | --------- | ----------- | --------- | ------- | ------- | --------------- | ------------ | --------- | ---------- | ----------- | ---------- | ------------------------ | ------------------------ | ---------------------- | ---------------------- | --------- | ---------- | ----------- | --------- | ----------------- | ---------- | ------- |
| Отровна   | Изпъкнала | Гладка      | Кафява    | Синини  | Остра   | Свободна        | Плътна       | Тясна     | Черна      | Разширяваща | Равна      | Гладка                   | Гладка                   | Бяла                   | Бяла                   | Частична  | Бяла       | Една        | Висяща   | Черна             | Разпръсната| Градска |
| Ядлива    | Изпъкнала | Гладка      | Жълта     | Синини  | Бадем   | Свободна        | Плътна       | Широка    | Черна      | Разширяваща | Клуб       | Гладка                   | Гладка                   | Бяла                   | Бяла                   | Частична  | Бяла       | Една        | Висяща   | Кафява            | Многобройна| Треви   |
| Ядлива    | Камбанка  | Гладка      | Бяла      | Синини  | Анасон  | Свободна        | Плътна       | Широка    | Кафява     | Разширяваща | Клуб       | Гладка                   | Гладка                   | Бяла                   | Бяла                   | Частична  | Бяла       | Една        | Висяща   | Кафява            | Многобройна| Ливади  |
| Отровна   | Изпъкнала | Люспеста    | Бяла      | Синини  | Остра   | Свободна        | Плътна       | Тясна     | Кафява     | Разширяваща | Равна      | Гладка                   | Гладка                   | Бяла                   | Бяла                   | Частична  | Бяла       | Една        | Висяща   | Черна             | Разпръсната| Градска |

Веднага забелязвате, че всички данни са текстови. Ще трябва да конвертирате тези данни, за да можете да ги използвате в диаграма. Всъщност повечето от данните са представени като обект:

```python
print(mushrooms.select_dtypes(["object"]).columns)
```

Резултатът е:

```output
Index(['class', 'cap-shape', 'cap-surface', 'cap-color', 'bruises', 'odor',
       'gill-attachment', 'gill-spacing', 'gill-size', 'gill-color',
       'stalk-shape', 'stalk-root', 'stalk-surface-above-ring',
       'stalk-surface-below-ring', 'stalk-color-above-ring',
       'stalk-color-below-ring', 'veil-type', 'veil-color', 'ring-number',
       'ring-type', 'spore-print-color', 'population', 'habitat'],
      dtype='object')
```
Вземете тези данни и конвертирайте колоната 'class' в категория:

```python
cols = mushrooms.select_dtypes(["object"]).columns
mushrooms[cols] = mushrooms[cols].astype('category')
```

```python
edibleclass=mushrooms.groupby(['class']).count()
edibleclass
```

Сега, ако отпечатате данните за гъбите, можете да видите, че те са групирани в категории според класа ядливи/отровни:


|           | cap-shape | cap-surface | cap-color | bruises | odor | gill-attachment | gill-spacing | gill-size | gill-color | stalk-shape | ... | stalk-surface-below-ring | stalk-color-above-ring | stalk-color-below-ring | veil-type | veil-color | ring-number | ring-type | spore-print-color | population | habitat |
| --------- | --------- | ----------- | --------- | ------- | ---- | --------------- | ------------ | --------- | ---------- | ----------- | --- | ------------------------ | ---------------------- | ---------------------- | --------- | ---------- | ----------- | --------- | ----------------- | ---------- | ------- |
| class     |           |             |           |         |      |                 |              |           |            |             |     |                          |                        |                        |           |            |             |           |                   |            |         |
| Ядлива    | 4208      | 4208        | 4208      | 4208    | 4208 | 4208            | 4208         | 4208      | 4208       | 4208        | ... | 4208                     | 4208                   | 4208                   | 4208      | 4208       | 4208        | 4208      | 4208              | 4208       | 4208    |
| Отровна   | 3916      | 3916        | 3916      | 3916    | 3916 | 3916            | 3916         | 3916      | 3916       | 3916        | ... | 3916                     | 3916                   | 3916                   | 3916      | 3916       | 3916        | 3916      | 3916              | 3916       | 3916    |

Ако следвате реда, представен в тази таблица, за да създадете етикетите на категорията 'class', можете да изградите кръгова диаграма:

## Кръг!

```python
labels=['Edible','Poisonous']
plt.pie(edibleclass['population'],labels=labels,autopct='%.1f %%')
plt.title('Edible?')
plt.show()
```
Ето я, кръгова диаграма, показваща пропорциите на тези данни според двата класа гъби. Много е важно да получите правилния ред на етикетите, особено тук, затова се уверете, че сте проверили реда, с който е изградена масивът от етикети!

![кръгова диаграма](../../../../3-Data-Visualization/11-visualization-proportions/images/pie1-wb.png)

## Понички!

Малко по-визуално интересна кръгова диаграма е диаграмата тип "поничка", която е кръгова диаграма с дупка в средата. Нека разгледаме нашите данни, използвайки този метод.

Разгледайте различните местообитания, където растат гъбите:

```python
habitat=mushrooms.groupby(['habitat']).count()
habitat
```
Тук групирате данните си по местообитание. Има 7 изброени, така че използвайте тях като етикети за вашата диаграма тип "поничка":

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

![диаграма тип "поничка"](../../../../3-Data-Visualization/11-visualization-proportions/images/donut-wb.png)

Този код рисува диаграма и централен кръг, след което добавя този централен кръг в диаграмата. Редактирайте ширината на централния кръг, като промените `0.40` на друга стойност.

Диаграмите тип "поничка" могат да бъдат променяни по няколко начина, за да се променят етикетите. Етикетите, по-специално, могат да бъдат подчертани за по-добра четимост. Научете повече в [документацията](https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_and_donut_labels.html?highlight=donut).

Сега, когато знаете как да групирате данните си и след това да ги показвате като кръг или поничка, можете да изследвате други типове диаграми. Опитайте диаграма тип "вафла", която е просто различен начин за изследване на количествата.
## Вафли!

Диаграма тип "вафла" е различен начин за визуализиране на количества като двумерна решетка от квадрати. Опитайте да визуализирате различните количества цветове на шапките на гъбите в този набор от данни. За да направите това, трябва да инсталирате помощна библиотека, наречена [PyWaffle](https://pypi.org/project/pywaffle/) и да използвате Matplotlib:

```python
pip install pywaffle
```

Изберете сегмент от вашите данни за групиране:

```python
capcolor=mushrooms.groupby(['cap-color']).count()
capcolor
```

Създайте диаграма тип "вафла", като създадете етикети и след това групирате данните си:

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

Използвайки диаграма тип "вафла", можете ясно да видите пропорциите на цветовете на шапките в този набор от данни за гъби. Интересно е, че има много гъби със зелени шапки!

![диаграма тип "вафла"](../../../../3-Data-Visualization/11-visualization-proportions/images/waffle.png)

✅ Pywaffle поддържа икони в диаграмите, които използват всяка икона, налична в [Font Awesome](https://fontawesome.com/). Направете някои експерименти, за да създадете още по-интересна диаграма тип "вафла", използвайки икони вместо квадрати.

В този урок научихте три начина за визуализиране на пропорции. Първо, трябва да групирате данните си в категории и след това да решите кой е най-добрият начин за показване на данните - кръг, поничка или вафла. Всички са вкусни и удовлетворяват потребителя с моментална снимка на набора от данни.

## 🚀 Предизвикателство

Опитайте да пресъздадете тези апетитни диаграми в [Charticulator](https://charticulator.com).
## [Тест след лекцията](https://ff-quizzes.netlify.app/en/ds/quiz/21)

## Преглед и самостоятелно обучение

Понякога не е очевидно кога да използвате кръгова, диаграма тип "поничка" или диаграма тип "вафла". Ето някои статии за четене по тази тема:

https://www.beautiful.ai/blog/battle-of-the-charts-pie-chart-vs-donut-chart

https://medium.com/@hypsypops/pie-chart-vs-donut-chart-showdown-in-the-ring-5d24fd86a9ce

https://www.mit.edu/~mbarker/formula1/f1help/11-ch-c6.htm

https://medium.datadriveninvestor.com/data-visualization-done-the-right-way-with-tableau-waffle-chart-fdf2a19be402

Направете проучване, за да намерите повече информация относно това трудно решение.
## Задача

[Опитайте го в Excel](assignment.md)

---

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI услуга за превод [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи може да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или погрешни интерпретации, произтичащи от използването на този превод.