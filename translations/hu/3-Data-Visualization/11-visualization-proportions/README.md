<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "42119bcc97bee88254e381156d770f3c",
  "translation_date": "2025-09-05T17:32:24+00:00",
  "source_file": "3-Data-Visualization/11-visualization-proportions/README.md",
  "language_code": "hu"
}
-->
# Arányok vizualizálása

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/11-Visualizing-Proportions.png)|
|:---:|
|Arányok vizualizálása - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

Ebben a leckében egy természetközpontú adatállományt fogsz használni, hogy vizualizáld az arányokat, például azt, hogy hány különböző gombafaj található egy adott adatállományban a gombákról. Fedezzük fel ezeket a lenyűgöző gombákat egy Audubon által összeállított adatállomány segítségével, amely 23 lemezes gombafaj részleteit tartalmazza az Agaricus és Lepiota családokból. Kísérletezz ínycsiklandó vizualizációkkal, mint például:

- Torta diagramok 🥧
- Fánk diagramok 🍩
- Waffle diagramok 🧇

> 💡 A Microsoft Research által létrehozott [Charticulator](https://charticulator.com) nevű projekt egy ingyenes drag and drop felületet kínál az adatvizualizációkhoz. Az egyik oktatóanyagukban szintén ezt a gomba adatállományt használják! Így egyszerre fedezheted fel az adatokat és tanulhatod meg a könyvtár használatát: [Charticulator oktatóanyag](https://charticulator.com/tutorials/tutorial4.html).

## [Előadás előtti kvíz](https://ff-quizzes.netlify.app/en/ds/quiz/20)

## Ismerd meg a gombáidat 🍄

A gombák nagyon érdekesek. Importáljunk egy adatállományt, hogy tanulmányozhassuk őket:

```python
import pandas as pd
import matplotlib.pyplot as plt
mushrooms = pd.read_csv('../../data/mushrooms.csv')
mushrooms.head()
```
Egy táblázat jelenik meg, amely remek adatokat tartalmaz elemzéshez:


| class     | cap-shape | cap-surface | cap-color | bruises | odor    | gill-attachment | gill-spacing | gill-size | gill-color | stalk-shape | stalk-root | stalk-surface-above-ring | stalk-surface-below-ring | stalk-color-above-ring | stalk-color-below-ring | veil-type | veil-color | ring-number | ring-type | spore-print-color | population | habitat |
| --------- | --------- | ----------- | --------- | ------- | ------- | --------------- | ------------ | --------- | ---------- | ----------- | ---------- | ------------------------ | ------------------------ | ---------------------- | ---------------------- | --------- | ---------- | ----------- | --------- | ----------------- | ---------- | ------- |
| Mérgező   | Domború   | Sima        | Barna     | Zúzódik | Szúrós  | Szabad          | Szoros       | Keskeny   | Fekete     | Táguló      | Egyenlő    | Sima                     | Sima                     | Fehér                  | Fehér                  | Részleges | Fehér      | Egy         | Függő     | Fekete            | Szórványos | Városi  |
| Ehető     | Domború   | Sima        | Sárga     | Zúzódik | Mandula | Szabad          | Szoros       | Széles    | Fekete     | Táguló      | Klub       | Sima                     | Sima                     | Fehér                  | Fehér                  | Részleges | Fehér      | Egy         | Függő     | Barna             | Számos     | Füves   |
| Ehető     | Harang    | Sima        | Fehér     | Zúzódik | Ánizs   | Szabad          | Szoros       | Széles    | Barna      | Táguló      | Klub       | Sima                     | Sima                     | Fehér                  | Fehér                  | Részleges | Fehér      | Egy         | Függő     | Barna             | Számos     | Mezők   |
| Mérgező   | Domború   | Pikkelyes   | Fehér     | Zúzódik | Szúrós  | Szabad          | Szoros       | Keskeny   | Barna      | Táguló      | Egyenlő    | Sima                     | Sima                     | Fehér                  | Fehér                  | Részleges | Fehér      | Egy         | Függő     | Fekete            | Szórványos | Városi  |

Rögtön észreveheted, hogy az összes adat szöveges. Az adatokat át kell alakítanod, hogy diagramon használhatóak legyenek. Valójában az adatok többsége objektumként van ábrázolva:

```python
print(mushrooms.select_dtypes(["object"]).columns)
```

Az eredmény:

```output
Index(['class', 'cap-shape', 'cap-surface', 'cap-color', 'bruises', 'odor',
       'gill-attachment', 'gill-spacing', 'gill-size', 'gill-color',
       'stalk-shape', 'stalk-root', 'stalk-surface-above-ring',
       'stalk-surface-below-ring', 'stalk-color-above-ring',
       'stalk-color-below-ring', 'veil-type', 'veil-color', 'ring-number',
       'ring-type', 'spore-print-color', 'population', 'habitat'],
      dtype='object')
```
Konvertáld az 'osztály' oszlopot kategóriává:

```python
cols = mushrooms.select_dtypes(["object"]).columns
mushrooms[cols] = mushrooms[cols].astype('category')
```

```python
edibleclass=mushrooms.groupby(['class']).count()
edibleclass
```

Most, ha kinyomtatod a gomba adatokat, láthatod, hogy azokat kategóriákba csoportosították a mérgező/ehető osztály szerint:


|           | cap-shape | cap-surface | cap-color | bruises | odor | gill-attachment | gill-spacing | gill-size | gill-color | stalk-shape | ... | stalk-surface-below-ring | stalk-color-above-ring | stalk-color-below-ring | veil-type | veil-color | ring-number | ring-type | spore-print-color | population | habitat |
| --------- | --------- | ----------- | --------- | ------- | ---- | --------------- | ------------ | --------- | ---------- | ----------- | --- | ------------------------ | ---------------------- | ---------------------- | --------- | ---------- | ----------- | --------- | ----------------- | ---------- | ------- |
| class     |           |             |           |         |      |                 |              |           |            |             |     |                          |                        |                        |           |            |             |           |                   |            |         |
| Ehető     | 4208      | 4208        | 4208      | 4208    | 4208 | 4208            | 4208         | 4208      | 4208       | 4208        | ... | 4208                     | 4208                   | 4208                   | 4208      | 4208       | 4208        | 4208      | 4208              | 4208       | 4208    |
| Mérgező   | 3916      | 3916        | 3916      | 3916    | 3916 | 3916            | 3916         | 3916      | 3916       | 3916        | ... | 3916                     | 3916                   | 3916                   | 3916      | 3916       | 3916        | 3916      | 3916              | 3916       | 3916    |

Ha követed a táblázatban bemutatott sorrendet az osztály kategória címkék létrehozásához, készíthetsz egy torta diagramot:

## Torta!

```python
labels=['Edible','Poisonous']
plt.pie(edibleclass['population'],labels=labels,autopct='%.1f %%')
plt.title('Edible?')
plt.show()
```
Voilá, egy torta diagram, amely megmutatja az adatok arányait a gombák két osztálya szerint. Nagyon fontos, hogy a címkék sorrendje helyes legyen, különösen itt, ezért ellenőrizd a címke tömb létrehozásának sorrendjét!

![torta diagram](../../../../3-Data-Visualization/11-visualization-proportions/images/pie1-wb.png)

## Fánkok!

Egy vizuálisan érdekesebb torta diagram a fánk diagram, amely egy lyukkal rendelkező torta diagram. Nézzük meg az adatainkat ezzel a módszerrel.

Nézd meg a különböző élőhelyeket, ahol a gombák nőnek:

```python
habitat=mushrooms.groupby(['habitat']).count()
habitat
```
Itt az adatokat élőhely szerint csoportosítod. Hét élőhely van felsorolva, így ezeket használd címkékként a fánk diagramhoz:

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

![fánk diagram](../../../../3-Data-Visualization/11-visualization-proportions/images/donut-wb.png)

Ez a kód egy diagramot és egy középső kört rajzol, majd hozzáadja azt a diagramhoz. A középső kör szélességét a `0.40` érték megváltoztatásával módosíthatod.

A fánk diagramok többféleképpen is testreszabhatók, például a címkék olvashatóságának javítása érdekében. További információt a [dokumentációban](https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_and_donut_labels.html?highlight=donut) találsz.

Most, hogy tudod, hogyan csoportosítsd az adatokat, és hogyan jelenítsd meg őket torta vagy fánk formájában, felfedezhetsz más típusú diagramokat is. Próbálj ki egy waffle diagramot, amely egy másik módja a mennyiségek vizualizálásának.
## Waffle!

A 'waffle' típusú diagram egy másik módja a mennyiségek vizualizálásának egy 2D négyzetes tömb formájában. Próbáld meg vizualizálni a gombák kalapszíneinek különböző mennyiségeit ebben az adatállományban. Ehhez telepítened kell egy segédkönyvtárat, a [PyWaffle](https://pypi.org/project/pywaffle/) nevűt, és használnod kell a Matplotlib-et:

```python
pip install pywaffle
```

Válassz ki egy adat szegmenst csoportosításhoz:

```python
capcolor=mushrooms.groupby(['cap-color']).count()
capcolor
```

Hozz létre egy waffle diagramot címkék létrehozásával, majd csoportosítsd az adatokat:

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

A waffle diagram segítségével egyértelműen láthatod a gombák kalapszíneinek arányait ebben az adatállományban. Érdekes módon sok zöld kalapú gomba van!

![waffle diagram](../../../../3-Data-Visualization/11-visualization-proportions/images/waffle.png)

✅ A PyWaffle támogatja az ikonokat a diagramokon belül, amelyek bármelyik [Font Awesome](https://fontawesome.com/) ikon használatát lehetővé teszik. Kísérletezz, hogy még érdekesebb waffle diagramot készíts ikonok helyett négyzetekkel.

Ebben a leckében három módot tanultál meg az arányok vizualizálására. Először csoportosítanod kell az adatokat kategóriákba, majd eldönteni, hogy melyik a legjobb módja az adatok megjelenítésének - torta, fánk vagy waffle. Mindegyik ínycsiklandó, és azonnali pillanatképet nyújt az adatállományról.

## 🚀 Kihívás

Próbáld meg újra elkészíteni ezeket az ínycsiklandó diagramokat a [Charticulator](https://charticulator.com) segítségével.
## [Előadás utáni kvíz](https://ff-quizzes.netlify.app/en/ds/quiz/21)

## Áttekintés és önálló tanulás

Néha nem egyértelmű, hogy mikor használjunk torta, fánk vagy waffle diagramot. Íme néhány cikk, amit elolvashatsz a témában:

https://www.beautiful.ai/blog/battle-of-the-charts-pie-chart-vs-donut-chart

https://medium.com/@hypsypops/pie-chart-vs-donut-chart-showdown-in-the-ring-5d24fd86a9ce

https://www.mit.edu/~mbarker/formula1/f1help/11-ch-c6.htm

https://medium.datadriveninvestor.com/data-visualization-done-the-right-way-with-tableau-waffle-chart-fdf2a19be402

Végezz kutatást, hogy további információkat találj erről a nehéz döntésről.
## Feladat

[Próbáld ki Excelben](assignment.md)

---

**Felelősség kizárása**:  
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével került lefordításra. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.