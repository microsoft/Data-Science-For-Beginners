<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "42119bcc97bee88254e381156d770f3c",
  "translation_date": "2025-09-06T08:12:28+00:00",
  "source_file": "3-Data-Visualization/11-visualization-proportions/README.md",
  "language_code": "pa"
}
-->
# ਅਨੁਪਾਤਾਂ ਦੀ ਦ੍ਰਿਸ਼ਟੀਕਰਨ

|![ [(@sketchthedocs)] ਦੁਆਰਾ ਸਕੈਚਨੋਟ](https://sketchthedocs.dev) ](../../sketchnotes/11-Visualizing-Proportions.png)|
|:---:|
|ਅਨੁਪਾਤਾਂ ਦੀ ਦ੍ਰਿਸ਼ਟੀਕਰਨ - _[@nitya](https://twitter.com/nitya) ਦੁਆਰਾ ਸਕੈਚਨੋਟ_ |

ਇਸ ਪਾਠ ਵਿੱਚ, ਤੁਸੀਂ ਮਸ਼ਰੂਮਾਂ ਬਾਰੇ ਇੱਕ ਦਿੱਤੇ ਗਏ ਡਾਟਾਸੈਟ ਵਿੱਚ ਵੱਖ-ਵੱਖ ਕਿਸਮਾਂ ਦੇ ਫੰਗਸ ਦੀ ਗਿਣਤੀ ਵਰਗੇ ਅਨੁਪਾਤਾਂ ਨੂੰ ਦ੍ਰਿਸ਼ਟੀਕਰਣ ਕਰਨ ਲਈ ਇੱਕ ਵੱਖਰੇ ਕੁਦਰਤ-ਕੇਂਦਰਤ ਡਾਟਾਸੈਟ ਦੀ ਵਰਤੋਂ ਕਰੋਗੇ। ਆਓ ਅਗਾਰਿਕਸ ਅਤੇ ਲੇਪਿਓਟਾ ਪਰਿਵਾਰਾਂ ਦੇ 23 ਪ੍ਰਜਾਤੀਆਂ ਦੇ ਗਿਲਡ ਮਸ਼ਰੂਮਾਂ ਬਾਰੇ ਆਡੂਬਨ ਤੋਂ ਪ੍ਰਾਪਤ ਡਾਟਾ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇਹ ਦਿਲਚਸਪ ਫੰਗਸ ਦੀ ਖੋਜ ਕਰੀਏ। ਤੁਸੀਂ ਹੇਠਾਂ ਦਿੱਤੇ ਦ੍ਰਿਸ਼ਟੀਕਰਣਾਂ ਨਾਲ ਪ੍ਰਯੋਗ ਕਰੋਗੇ:

- ਪਾਈ ਚਾਰਟ 🥧
- ਡੋਨਟ ਚਾਰਟ 🍩
- ਵਾਫਲ ਚਾਰਟ 🧇

> 💡 ਮਾਈਕਰੋਸਾਫਟ ਰਿਸਰਚ ਦੁਆਰਾ ਇੱਕ ਬਹੁਤ ਦਿਲਚਸਪ ਪ੍ਰੋਜੈਕਟ [Charticulator](https://charticulator.com) ਇੱਕ ਮੁਫ਼ਤ ਡ੍ਰੈਗ ਅਤੇ ਡ੍ਰਾਪ ਇੰਟਰਫੇਸ ਪੇਸ਼ ਕਰਦਾ ਹੈ ਜੋ ਡਾਟਾ ਦ੍ਰਿਸ਼ਟੀਕਰਣ ਲਈ ਹੈ। ਆਪਣੇ ਇੱਕ ਟਿਊਟੋਰਿਅਲ ਵਿੱਚ ਉਹ ਇਸ ਮਸ਼ਰੂਮ ਡਾਟਾਸੈਟ ਦੀ ਵੀ ਵਰਤੋਂ ਕਰਦੇ ਹਨ! ਇਸ ਲਈ ਤੁਸੀਂ ਡਾਟਾ ਦੀ ਖੋਜ ਕਰ ਸਕਦੇ ਹੋ ਅਤੇ ਲਾਇਬ੍ਰੇਰੀ ਨੂੰ ਇੱਕੋ ਸਮੇਂ ਸਿੱਖ ਸਕਦੇ ਹੋ: [Charticulator ਟਿਊਟੋਰਿਅਲ](https://charticulator.com/tutorials/tutorial4.html)।

## [ਪ੍ਰੀ-ਪਾਠ ਕਵਿਜ਼](https://ff-quizzes.netlify.app/en/ds/quiz/20)

## ਆਪਣੇ ਮਸ਼ਰੂਮਾਂ ਨੂੰ ਜਾਣੋ 🍄

ਮਸ਼ਰੂਮ ਬਹੁਤ ਦਿਲਚਸਪ ਹੁੰਦੇ ਹਨ। ਆਓ ਇੱਕ ਡਾਟਾਸੈਟ ਨੂੰ ਆਯਾਤ ਕਰਕੇ ਉਨ੍ਹਾਂ ਦਾ ਅਧਿਐਨ ਕਰੀਏ:

```python
import pandas as pd
import matplotlib.pyplot as plt
mushrooms = pd.read_csv('../../data/mushrooms.csv')
mushrooms.head()
```
ਇੱਕ ਟੇਬਲ ਪ੍ਰਿੰਟ ਕੀਤੀ ਜਾਂਦੀ ਹੈ ਜਿਸ ਵਿੱਚ ਵਿਸ਼ਲੇਸ਼ਣ ਲਈ ਕੁਝ ਸ਼ਾਨਦਾਰ ਡਾਟਾ ਹੁੰਦਾ ਹੈ:

| class     | cap-shape | cap-surface | cap-color | bruises | odor    | gill-attachment | gill-spacing | gill-size | gill-color | stalk-shape | stalk-root | stalk-surface-above-ring | stalk-surface-below-ring | stalk-color-above-ring | stalk-color-below-ring | veil-type | veil-color | ring-number | ring-type | spore-print-color | population | habitat |
| --------- | --------- | ----------- | --------- | ------- | ------- | --------------- | ------------ | --------- | ---------- | ----------- | ---------- | ------------------------ | ------------------------ | ---------------------- | ---------------------- | --------- | ---------- | ----------- | --------- | ----------------- | ---------- | ------- |
| Poisonous | Convex    | Smooth      | Brown     | Bruises | Pungent | Free            | Close        | Narrow    | Black      | Enlarging   | Equal      | Smooth                   | Smooth                   | White                  | White                  | Partial   | White      | One         | Pendant   | Black             | Scattered  | Urban   |
| Edible    | Convex    | Smooth      | Yellow    | Bruises | Almond  | Free            | Close        | Broad     | Black      | Enlarging   | Club       | Smooth                   | Smooth                   | White                  | White                  | Partial   | White      | One         | Pendant   | Brown             | Numerous   | Grasses |
| Edible    | Bell      | Smooth      | White     | Bruises | Anise   | Free            | Close        | Broad     | Brown      | Enlarging   | Club       | Smooth                   | Smooth                   | White                  | White                  | Partial   | White      | One         | Pendant   | Brown             | Numerous   | Meadows |
| Poisonous | Convex    | Scaly       | White     | Bruises | Pungent | Free            | Close        | Narrow    | Brown      | Enlarging   | Equal      | Smooth                   | Smooth                   | White                  | White                  | Partial   | White      | One         | Pendant   | Black             | Scattered  | Urban   |

ਤੁਰੰਤ ਹੀ, ਤੁਸੀਂ ਨੋਟ ਕਰਦੇ ਹੋ ਕਿ ਸਾਰਾ ਡਾਟਾ ਟੈਕਸਟ ਦੇ ਰੂਪ ਵਿੱਚ ਹੈ। ਤੁਹਾਨੂੰ ਇਸ ਡਾਟੇ ਨੂੰ ਚਾਰਟ ਵਿੱਚ ਵਰਤਣ ਯੋਗ ਬਣਾਉਣ ਲਈ ਇਸ ਨੂੰ ਰੂਪਾਂਤਰਿਤ ਕਰਨਾ ਪਵੇਗਾ। ਅਸਲ ਵਿੱਚ, ਜ਼ਿਆਦਾਤਰ ਡਾਟਾ ਇੱਕ ਆਬਜੈਕਟ ਦੇ ਰੂਪ ਵਿੱਚ ਦਰਸਾਇਆ ਗਿਆ ਹੈ:

```python
print(mushrooms.select_dtypes(["object"]).columns)
```

ਆਉਟਪੁੱਟ ਹੈ:

```output
Index(['class', 'cap-shape', 'cap-surface', 'cap-color', 'bruises', 'odor',
       'gill-attachment', 'gill-spacing', 'gill-size', 'gill-color',
       'stalk-shape', 'stalk-root', 'stalk-surface-above-ring',
       'stalk-surface-below-ring', 'stalk-color-above-ring',
       'stalk-color-below-ring', 'veil-type', 'veil-color', 'ring-number',
       'ring-type', 'spore-print-color', 'population', 'habitat'],
      dtype='object')
```
ਇਸ ਡਾਟੇ ਨੂੰ ਲਓ ਅਤੇ 'class' ਕਾਲਮ ਨੂੰ ਇੱਕ ਸ਼੍ਰੇਣੀ ਵਿੱਚ ਰੂਪਾਂਤਰਿਤ ਕਰੋ:

```python
cols = mushrooms.select_dtypes(["object"]).columns
mushrooms[cols] = mushrooms[cols].astype('category')
```

```python
edibleclass=mushrooms.groupby(['class']).count()
edibleclass
```

ਹੁਣ, ਜੇ ਤੁਸੀਂ ਮਸ਼ਰੂਮਾਂ ਦਾ ਡਾਟਾ ਪ੍ਰਿੰਟ ਕਰਦੇ ਹੋ, ਤਾਂ ਤੁਸੀਂ ਦੇਖ ਸਕਦੇ ਹੋ ਕਿ ਇਸਨੂੰ ਜ਼ਹਿਰੀਲੇ/ਖਾਣਯੋਗ ਸ਼੍ਰੇਣੀ ਦੇ ਅਨੁਸਾਰ ਸ਼੍ਰੇਣੀਆਂ ਵਿੱਚ ਸਮੂਹਬੱਧ ਕੀਤਾ ਗਿਆ ਹੈ:

|           | cap-shape | cap-surface | cap-color | bruises | odor | gill-attachment | gill-spacing | gill-size | gill-color | stalk-shape | ... | stalk-surface-below-ring | stalk-color-above-ring | stalk-color-below-ring | veil-type | veil-color | ring-number | ring-type | spore-print-color | population | habitat |
| --------- | --------- | ----------- | --------- | ------- | ---- | --------------- | ------------ | --------- | ---------- | ----------- | --- | ------------------------ | ---------------------- | ---------------------- | --------- | ---------- | ----------- | --------- | ----------------- | ---------- | ------- |
| class     |           |             |           |         |      |                 |              |           |            |             |     |                          |                        |                        |           |            |             |           |                   |            |         |
| Edible    | 4208      | 4208        | 4208      | 4208    | 4208 | 4208            | 4208         | 4208      | 4208       | 4208        | ... | 4208                     | 4208                   | 4208                   | 4208      | 4208       | 4208        | 4208      | 4208              | 4208       | 4208    |
| Poisonous | 3916      | 3916        | 3916      | 3916    | 3916 | 3916            | 3916         | 3916      | 3916       | 3916        | ... | 3916                     | 3916                   | 3916                   | 3916      | 3916       | 3916        | 3916      | 3916              | 3916       | 3916    |

ਜੇ ਤੁਸੀਂ ਇਸ ਟੇਬਲ ਵਿੱਚ ਪੇਸ਼ ਕੀਤੇ ਕ੍ਰਮ ਨੂੰ ਫਾਲੋ ਕਰਦੇ ਹੋ ਤਾਂ ਤੁਸੀਂ ਆਪਣੀਆਂ ਸ਼੍ਰੇਣੀ ਲੇਬਲਾਂ ਬਣਾਉਣ ਲਈ ਪਾਈ ਚਾਰਟ ਤਿਆਰ ਕਰ ਸਕਦੇ ਹੋ:

## ਪਾਈ!

```python
labels=['Edible','Poisonous']
plt.pie(edibleclass['population'],labels=labels,autopct='%.1f %%')
plt.title('Edible?')
plt.show()
```
ਲੋ ਜੀ, ਇੱਕ ਪਾਈ ਚਾਰਟ ਜੋ ਮਸ਼ਰੂਮਾਂ ਦੀਆਂ ਦੋ ਸ਼੍ਰੇਣੀਆਂ ਦੇ ਅਨੁਪਾਤਾਂ ਨੂੰ ਦਰਸਾਉਂਦਾ ਹੈ। ਲੇਬਲਾਂ ਦੇ ਕ੍ਰਮ ਨੂੰ ਸਹੀ ਪ੍ਰਾਪਤ ਕਰਨਾ ਬਹੁਤ ਮਹੱਤਵਪੂਰਨ ਹੈ, ਖਾਸ ਕਰਕੇ ਇੱਥੇ, ਇਸ ਲਈ ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਲੇਬਲ ਐਰੇ ਬਣਾਉਣ ਦੇ ਕ੍ਰਮ ਦੀ ਪੁਸ਼ਟੀ ਕਰੋ!

![pie chart](../../../../3-Data-Visualization/11-visualization-proportions/images/pie1-wb.png)

## ਡੋਨਟ!

ਪਾਈ ਚਾਰਟ ਦਾ ਇੱਕ ਹੋਰ ਦ੍ਰਿਸ਼ਟੀਕਰਣ ਡੋਨਟ ਚਾਰਟ ਹੈ, ਜੋ ਪਾਈ ਚਾਰਟ ਹੈ ਜਿਸਦੇ ਵਿਚਕਾਰ ਇੱਕ ਛੇਦ ਹੁੰਦਾ ਹੈ। ਆਓ ਆਪਣੇ ਡਾਟੇ ਨੂੰ ਇਸ ਤਰੀਕੇ ਨਾਲ ਦੇਖੀਏ।

ਮਸ਼ਰੂਮਾਂ ਦੇ ਵੱਖ-ਵੱਖ ਆਵਾਸਾਂ ਨੂੰ ਦੇਖੋ:

```python
habitat=mushrooms.groupby(['habitat']).count()
habitat
```
ਇੱਥੇ, ਤੁਸੀਂ ਆਪਣੇ ਡਾਟੇ ਨੂੰ ਆਵਾਸ ਦੇ ਅਨੁਸਾਰ ਸਮੂਹਬੱਧ ਕਰ ਰਹੇ ਹੋ। ਇੱਥੇ 7 ਆਵਾਸ ਦਿੱਤੇ ਗਏ ਹਨ, ਇਸ ਲਈ ਆਪਣੇ ਡੋਨਟ ਚਾਰਟ ਲਈ ਉਹਨਾਂ ਨੂੰ ਲੇਬਲਾਂ ਵਜੋਂ ਵਰਤੋ:

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

![donut chart](../../../../3-Data-Visualization/11-visualization-proportions/images/donut-wb.png)

ਇਹ ਕੋਡ ਇੱਕ ਚਾਰਟ ਅਤੇ ਇੱਕ ਕੇਂਦਰੀ ਸਰਕਲ ਖਿੱਚਦਾ ਹੈ, ਫਿਰ ਉਸ ਕੇਂਦਰੀ ਸਰਕਲ ਨੂੰ ਚਾਰਟ ਵਿੱਚ ਸ਼ਾਮਲ ਕਰਦਾ ਹੈ। ਕੇਂਦਰੀ ਸਰਕਲ ਦੀ ਚੌੜਾਈ ਨੂੰ `0.40` ਨੂੰ ਕਿਸੇ ਹੋਰ ਮੁੱਲ ਵਿੱਚ ਬਦਲ ਕੇ ਸੰਪਾਦਿਤ ਕਰੋ।

ਡੋਨਟ ਚਾਰਟਾਂ ਨੂੰ ਕਈ ਤਰੀਕਿਆਂ ਨਾਲ ਸੰਪਾਦਿਤ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ ਤਾਂ ਜੋ ਲੇਬਲਾਂ ਨੂੰ ਵਧੀਆ ਪੜ੍ਹਨਯੋਗ ਬਣਾਇਆ ਜਾ ਸਕੇ। ਇਸ ਬਾਰੇ ਹੋਰ ਜਾਣਕਾਰੀ ਲਈ [ਡਾਕੂਮੈਂਟ](https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_and_donut_labels.html?highlight=donut) ਵਿੱਚ ਪੜ੍ਹੋ।

ਹੁਣ ਜਦੋਂ ਤੁਸੀਂ ਆਪਣੇ ਡਾਟੇ ਨੂੰ ਸਮੂਹਬੱਧ ਕਰਨਾ ਅਤੇ ਇਸਨੂੰ ਪਾਈ ਜਾਂ ਡੋਨਟ ਵਜੋਂ ਦਿਖਾਉਣਾ ਸਿੱਖ ਲਿਆ ਹੈ, ਤਾਂ ਤੁਸੀਂ ਹੋਰ ਕਿਸਮਾਂ ਦੇ ਚਾਰਟਾਂ ਦੀ ਖੋਜ ਕਰ ਸਕਦੇ ਹੋ। ਇੱਕ ਵਾਫਲ ਚਾਰਟ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰੋ, ਜੋ ਮਾਤਰਾ ਦੀ ਖੋਜ ਕਰਨ ਦਾ ਇੱਕ ਵੱਖਰਾ ਤਰੀਕਾ ਹੈ।

## ਵਾਫਲ!

'ਵਾਫਲ' ਕਿਸਮ ਦਾ ਚਾਰਟ ਮਾਤਰਾ ਨੂੰ 2D ਐਰੇ ਦੇ ਚੌਰਸਾਂ ਵਜੋਂ ਦ੍ਰਿਸ਼ਟੀਕਰਣ ਕਰਨ ਦਾ ਇੱਕ ਵੱਖਰਾ ਤਰੀਕਾ ਹੈ। ਇਸ ਡਾਟਾਸੈਟ ਵਿੱਚ ਮਸ਼ਰੂਮ ਕੈਪ ਰੰਗਾਂ ਦੀਆਂ ਵੱਖ-ਵੱਖ ਮਾਤਰਾਂ ਨੂੰ ਦ੍ਰਿਸ਼ਟੀਕਰਣ ਕਰਨ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰੋ। ਇਸ ਲਈ, ਤੁਹਾਨੂੰ [PyWaffle](https://pypi.org/project/pywaffle/) ਨਾਮਕ ਇੱਕ ਸਹਾਇਕ ਲਾਇਬ੍ਰੇਰੀ ਨੂੰ ਇੰਸਟਾਲ ਕਰਨ ਦੀ ਜ਼ਰੂਰਤ ਹੈ ਅਤੇ ਮੈਟਪਲਾਟਲਿਬ ਦੀ ਵਰਤੋਂ ਕਰਨ ਦੀ ਜ਼ਰੂਰਤ ਹੈ:

```python
pip install pywaffle
```

ਆਪਣੇ ਡਾਟੇ ਦੇ ਇੱਕ ਖੰਡ ਨੂੰ ਸਮੂਹਬੱਧ ਕਰਨ ਲਈ ਚੁਣੋ:

```python
capcolor=mushrooms.groupby(['cap-color']).count()
capcolor
```

ਲੇਬਲ ਬਣਾਕੇ ਅਤੇ ਫਿਰ ਆਪਣੇ ਡਾਟੇ ਨੂੰ ਸਮੂਹਬੱਧ ਕਰਕੇ ਇੱਕ ਵਾਫਲ ਚਾਰਟ ਬਣਾਓ:

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

ਵਾਫਲ ਚਾਰਟ ਦੀ ਵਰਤੋਂ ਕਰਕੇ, ਤੁਸੀਂ ਇਸ ਮਸ਼ਰੂਮ ਡਾਟਾਸੈਟ ਦੇ ਕੈਪ ਰੰਗਾਂ ਦੇ ਅਨੁਪਾਤਾਂ ਨੂੰ ਸਪਸ਼ਟ ਤੌਰ 'ਤੇ ਦੇਖ ਸਕਦੇ ਹੋ। ਦਿਲਚਸਪ ਗੱਲ ਇਹ ਹੈ ਕਿ ਬਹੁਤ ਸਾਰੇ ਹਰੇ ਕੈਪ ਵਾਲੇ ਮਸ਼ਰੂਮ ਹਨ!

![waffle chart](../../../../3-Data-Visualization/11-visualization-proportions/images/waffle.png)

✅ PyWaffle [Font Awesome](https://fontawesome.com/) ਵਿੱਚ ਉਪਲਬਧ ਕਿਸੇ ਵੀ ਆਈਕਨ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਚਾਰਟਾਂ ਵਿੱਚ ਆਈਕਨ ਦਾ ਸਮਰਥਨ ਕਰਦਾ ਹੈ। ਚੌਰਸਾਂ ਦੀ ਬਜਾਏ ਆਈਕਨ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇੱਕ ਹੋਰ ਦਿਲਚਸਪ ਵਾਫਲ ਚਾਰਟ ਬਣਾਉਣ ਲਈ ਕੁਝ ਪ੍ਰਯੋਗ ਕਰੋ।

ਇਸ ਪਾਠ ਵਿੱਚ, ਤੁਸੀਂ ਅਨੁਪਾਤਾਂ ਨੂੰ ਦ੍ਰਿਸ਼ਟੀਕਰਣ ਕਰਨ ਦੇ ਤਿੰਨ ਤਰੀਕੇ ਸਿੱਖੇ। ਪਹਿਲਾਂ, ਤੁਹਾਨੂੰ ਆਪਣੇ ਡਾਟੇ ਨੂੰ ਸ਼੍ਰੇਣੀਆਂ ਵਿੱਚ ਸਮੂਹਬੱਧ ਕਰਨ ਦੀ ਜ਼ਰੂਰਤ ਹੈ ਅਤੇ ਫਿਰ ਇਹ ਫੈਸਲਾ ਕਰਨ ਦੀ ਜ਼ਰੂਰਤ ਹੈ ਕਿ ਡਾਟੇ ਨੂੰ ਦਿਖਾਉਣ ਦਾ ਸਭ ਤੋਂ ਵਧੀਆ ਤਰੀਕਾ ਕਿਹੜਾ ਹੈ - ਪਾਈ, ਡੋਨਟ, ਜਾਂ ਵਾਫਲ। ਸਾਰੇ ਸੁੰਦਰ ਹਨ ਅਤੇ ਉਪਭੋਗਤਾ ਨੂੰ ਡਾਟਾਸੈਟ ਦੀ ਤੁਰੰਤ ਝਲਕ ਦੇ ਕੇ ਸੰਤੁਸ਼ਟ ਕਰਦੇ ਹਨ।

## 🚀 ਚੁਣੌਤੀ

ਇਹ ਸੁੰਦਰ ਚਾਰਟਾਂ ਨੂੰ [Charticulator](https://charticulator.com) ਵਿੱਚ ਦੁਬਾਰਾ ਬਣਾਉਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰੋ।
## [ਪੋਸਟ-ਪਾਠ ਕਵਿਜ਼](https://ff-quizzes.netlify.app/en/ds/quiz/21)

## ਸਮੀਖਿਆ ਅਤੇ ਸਵੈ ਅਧਿਐਨ

ਕਈ ਵਾਰ ਇਹ ਸਪਸ਼ਟ ਨਹੀਂ ਹੁੰਦਾ ਕਿ ਪਾਈ, ਡੋਨਟ, ਜਾਂ ਵਾਫਲ ਚਾਰਟ ਕਦੋਂ ਵਰਤਣਾ ਹੈ। ਇਸ ਵਿਸ਼ੇ 'ਤੇ ਪੜ੍ਹਨ ਲਈ ਕੁਝ ਲੇਖ ਇੱਥੇ ਹਨ:

https://www.beautiful.ai/blog/battle-of-the-charts-pie-chart-vs-donut-chart

https://medium.com/@hypsypops/pie-chart-vs-donut-chart-showdown-in-the-ring-5d24fd86a9ce

https://www.mit.edu/~mbarker/formula1/f1help/11-ch-c6.htm

https://medium.datadriveninvestor.com/data-visualization-done-the-right-way-with-tableau-waffle-chart-fdf2a19be402

ਹੋਰ ਜਾਣਕਾਰੀ ਪ੍ਰਾਪਤ ਕਰਨ ਲਈ ਕੁਝ ਖੋਜ ਕਰੋ ਅਤੇ ਇਸ ਫੈਸਲੇ 'ਤੇ ਹੋਰ ਪੜ੍ਹਾਈ ਕਰੋ।

## ਅਸਾਈਨਮੈਂਟ

[Excel ਵਿੱਚ ਇਸਨੂੰ ਅਜ਼ਮਾਓ](assignment.md)

---

**ਅਸਵੀਕਾਰਨਾ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁਚਨਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਇਸਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।