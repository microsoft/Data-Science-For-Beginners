<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "42119bcc97bee88254e381156d770f3c",
  "translation_date": "2025-09-05T17:50:43+00:00",
  "source_file": "3-Data-Visualization/11-visualization-proportions/README.md",
  "language_code": "cs"
}
-->
# Vizualizace poměrů

|![ Sketchnote od [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/11-Visualizing-Proportions.png)|
|:---:|
|Vizualizace poměrů - _Sketchnote od [@nitya](https://twitter.com/nitya)_ |

V této lekci použijete dataset zaměřený na přírodu k vizualizaci poměrů, například kolik různých druhů hub se nachází v daném datasetu o houbách. Pojďme prozkoumat tyto fascinující houby pomocí datasetu od Audubon, který obsahuje podrobnosti o 23 druzích lupenatých hub z rodů Agaricus a Lepiota. Budete experimentovat s chutnými vizualizacemi, jako jsou:

- Koláčové grafy 🥧
- Donutové grafy 🍩
- Waflové grafy 🧇

> 💡 Velmi zajímavý projekt od Microsoft Research nazvaný [Charticulator](https://charticulator.com) nabízí bezplatné rozhraní pro vizualizaci dat pomocí drag and drop. V jednom z jejich tutoriálů také používají tento dataset o houbách! Můžete tedy prozkoumat data a zároveň se naučit používat tuto knihovnu: [Charticulator tutorial](https://charticulator.com/tutorials/tutorial4.html).

## [Kvíz před lekcí](https://ff-quizzes.netlify.app/en/ds/quiz/20)

## Poznejte své houby 🍄

Houby jsou velmi zajímavé. Importujme dataset, abychom je mohli studovat:

```python
import pandas as pd
import matplotlib.pyplot as plt
mushrooms = pd.read_csv('../../data/mushrooms.csv')
mushrooms.head()
```
Tabulka se vytiskne s některými skvělými daty pro analýzu:


| class     | cap-shape | cap-surface | cap-color | bruises | odor    | gill-attachment | gill-spacing | gill-size | gill-color | stalk-shape | stalk-root | stalk-surface-above-ring | stalk-surface-below-ring | stalk-color-above-ring | stalk-color-below-ring | veil-type | veil-color | ring-number | ring-type | spore-print-color | population | habitat |
| --------- | --------- | ----------- | --------- | ------- | ------- | --------------- | ------------ | --------- | ---------- | ----------- | ---------- | ------------------------ | ------------------------ | ---------------------- | ---------------------- | --------- | ---------- | ----------- | --------- | ----------------- | ---------- | ------- |
| Jedovaté  | Konvexní  | Hladký      | Hnědý     | Modřiny | Štiplavý| Volný           | Těsný        | Úzký      | Černý      | Rozšiřující | Rovný      | Hladký                   | Hladký                   | Bílý                   | Bílý                   | Částečný  | Bílý       | Jeden       | Visící   | Černý             | Rozptýlený | Městský |
| Jedlé     | Konvexní  | Hladký      | Žlutý     | Modřiny | Mandlový| Volný           | Těsný        | Široký    | Černý      | Rozšiřující | Klubový    | Hladký                   | Hladký                   | Bílý                   | Bílý                   | Částečný  | Bílý       | Jeden       | Visící   | Hnědý             | Početný    | Trávy  |
| Jedlé     | Zvoncový  | Hladký      | Bílý      | Modřiny | Anýzový | Volný           | Těsný        | Široký    | Hnědý      | Rozšiřující | Klubový    | Hladký                   | Hladký                   | Bílý                   | Bílý                   | Částečný  | Bílý       | Jeden       | Visící   | Hnědý             | Početný    | Louky  |
| Jedovaté  | Konvexní  | Šupinatý    | Bílý      | Modřiny | Štiplavý| Volný           | Těsný        | Úzký      | Hnědý      | Rozšiřující | Rovný      | Hladký                   | Hladký                   | Bílý                   | Bílý                   | Částečný  | Bílý       | Jeden       | Visící   | Černý             | Rozptýlený | Městský |

Hned si všimnete, že všechna data jsou textová. Budete je muset převést, abyste je mohli použít v grafu. Většina dat je ve skutečnosti reprezentována jako objekt:

```python
print(mushrooms.select_dtypes(["object"]).columns)
```

Výstup je:

```output
Index(['class', 'cap-shape', 'cap-surface', 'cap-color', 'bruises', 'odor',
       'gill-attachment', 'gill-spacing', 'gill-size', 'gill-color',
       'stalk-shape', 'stalk-root', 'stalk-surface-above-ring',
       'stalk-surface-below-ring', 'stalk-color-above-ring',
       'stalk-color-below-ring', 'veil-type', 'veil-color', 'ring-number',
       'ring-type', 'spore-print-color', 'population', 'habitat'],
      dtype='object')
```
Převeďte tato data a sloupec 'class' na kategorii:

```python
cols = mushrooms.select_dtypes(["object"]).columns
mushrooms[cols] = mushrooms[cols].astype('category')
```

```python
edibleclass=mushrooms.groupby(['class']).count()
edibleclass
```

Nyní, pokud vytisknete data o houbách, uvidíte, že byla rozdělena do kategorií podle jedovaté/jedlé třídy:


|           | cap-shape | cap-surface | cap-color | bruises | odor | gill-attachment | gill-spacing | gill-size | gill-color | stalk-shape | ... | stalk-surface-below-ring | stalk-color-above-ring | stalk-color-below-ring | veil-type | veil-color | ring-number | ring-type | spore-print-color | population | habitat |
| --------- | --------- | ----------- | --------- | ------- | ---- | --------------- | ------------ | --------- | ---------- | ----------- | --- | ------------------------ | ---------------------- | ---------------------- | --------- | ---------- | ----------- | --------- | ----------------- | ---------- | ------- |
| class     |           |             |           |         |      |                 |              |           |            |             |     |                          |                        |                        |           |            |             |           |                   |            |         |
| Jedlé     | 4208      | 4208        | 4208      | 4208    | 4208 | 4208            | 4208         | 4208      | 4208       | 4208        | ... | 4208                     | 4208                   | 4208                   | 4208      | 4208       | 4208        | 4208      | 4208              | 4208       | 4208    |
| Jedovaté  | 3916      | 3916        | 3916      | 3916    | 3916 | 3916            | 3916         | 3916      | 3916       | 3916        | ... | 3916                     | 3916                   | 3916                   | 3916      | 3916       | 3916        | 3916      | 3916              | 3916       | 3916    |

Pokud budete postupovat podle pořadí uvedeného v této tabulce při vytváření štítků kategorií třídy, můžete vytvořit koláčový graf:

## Koláč!

```python
labels=['Edible','Poisonous']
plt.pie(edibleclass['population'],labels=labels,autopct='%.1f %%')
plt.title('Edible?')
plt.show()
```
Voila, koláčový graf zobrazující poměry těchto dat podle těchto dvou tříd hub. Je velmi důležité získat pořadí štítků správně, zejména zde, takže si ověřte pořadí, ve kterém je pole štítků vytvořeno!

![koláčový graf](../../../../3-Data-Visualization/11-visualization-proportions/images/pie1-wb.png)

## Donuty!

Poněkud vizuálně zajímavější koláčový graf je donutový graf, což je koláčový graf s dírou uprostřed. Podívejme se na naše data pomocí této metody.

Podívejte se na různá stanoviště, kde houby rostou:

```python
habitat=mushrooms.groupby(['habitat']).count()
habitat
```
Zde seskupujete svá data podle stanoviště. Je jich uvedeno 7, takže je použijte jako štítky pro svůj donutový graf:

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

![donutový graf](../../../../3-Data-Visualization/11-visualization-proportions/images/donut-wb.png)

Tento kód vykreslí graf a středový kruh, poté přidá tento středový kruh do grafu. Upravte šířku středového kruhu změnou hodnoty `0.40` na jinou.

Donutové grafy lze upravit několika způsoby, aby se změnily štítky. Štítky lze zejména zvýraznit pro lepší čitelnost. Více se dozvíte v [dokumentaci](https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_and_donut_labels.html?highlight=donut).

Nyní, když víte, jak seskupit svá data a poté je zobrazit jako koláč nebo donut, můžete prozkoumat jiné typy grafů. Vyzkoušejte waflový graf, což je jen jiný způsob zkoumání množství.
## Wafle!

Graf typu 'waffle' je jiný způsob vizualizace množství jako 2D pole čtverců. Zkuste vizualizovat různé množství barev klobouků hub v tomto datasetu. K tomu potřebujete nainstalovat pomocnou knihovnu nazvanou [PyWaffle](https://pypi.org/project/pywaffle/) a použít Matplotlib:

```python
pip install pywaffle
```

Vyberte segment svých dat pro seskupení:

```python
capcolor=mushrooms.groupby(['cap-color']).count()
capcolor
```

Vytvořte waflový graf vytvořením štítků a poté seskupením svých dat:

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

Pomocí waflového grafu můžete jasně vidět poměry barev klobouků v tomto datasetu hub. Zajímavé je, že existuje mnoho hub se zelenými klobouky!

![waflový graf](../../../../3-Data-Visualization/11-visualization-proportions/images/waffle.png)

✅ Pywaffle podporuje ikony v grafech, které používají jakoukoli ikonu dostupnou v [Font Awesome](https://fontawesome.com/). Udělejte několik experimentů a vytvořte ještě zajímavější waflový graf pomocí ikon místo čtverců.

V této lekci jste se naučili tři způsoby vizualizace poměrů. Nejprve musíte seskupit svá data do kategorií a poté rozhodnout, který způsob zobrazení dat je nejlepší - koláč, donut nebo wafle. Všechny jsou chutné a uživatele potěší okamžitým přehledem datasetu.

## 🚀 Výzva

Zkuste znovu vytvořit tyto chutné grafy v [Charticulator](https://charticulator.com).
## [Kvíz po lekci](https://ff-quizzes.netlify.app/en/ds/quiz/21)

## Přehled & Samostudium

Někdy není zřejmé, kdy použít koláčový, donutový nebo waflový graf. Zde je několik článků, které si můžete přečíst na toto téma:

https://www.beautiful.ai/blog/battle-of-the-charts-pie-chart-vs-donut-chart

https://medium.com/@hypsypops/pie-chart-vs-donut-chart-showdown-in-the-ring-5d24fd86a9ce

https://www.mit.edu/~mbarker/formula1/f1help/11-ch-c6.htm

https://medium.datadriveninvestor.com/data-visualization-done-the-right-way-with-tableau-waffle-chart-fdf2a19be402

Proveďte výzkum a najděte více informací o tomto nelehkém rozhodnutí.
## Úkol

[Vyzkoušejte to v Excelu](assignment.md)

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlady [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vzniklé v důsledku použití tohoto překladu.