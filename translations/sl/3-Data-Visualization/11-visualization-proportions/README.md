<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cc490897ee2d276870472bcb31602d03",
  "translation_date": "2025-09-05T06:01:54+00:00",
  "source_file": "3-Data-Visualization/11-visualization-proportions/README.md",
  "language_code": "sl"
}
-->
# Vizualizacija deležev

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/11-Visualizing-Proportions.png)|
|:---:|
|Vizualizacija deležev - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

V tej lekciji boste uporabili naravoslovno usmerjen nabor podatkov za vizualizacijo deležev, na primer koliko različnih vrst gliv je prisotnih v danem naboru podatkov o gobah. Raziskali bomo te fascinantne glive z naborom podatkov, pridobljenim iz Audubona, ki vsebuje podrobnosti o 23 vrstah gob z lističi iz družin Agaricus in Lepiota. Eksperimentirali boste z okusnimi vizualizacijami, kot so:

- Tabelni diagrami 🥧
- Krožni diagrami 🍩
- Waffle diagrami 🧇

> 💡 Zelo zanimiv projekt [Charticulator](https://charticulator.com) Microsoft Research ponuja brezplačen vmesnik za vizualizacijo podatkov z metodo povleci in spusti. V enem od njihovih vaj uporabljajo tudi ta nabor podatkov o gobah! Tako lahko raziskujete podatke in hkrati spoznate knjižnico: [Charticulator tutorial](https://charticulator.com/tutorials/tutorial4.html).

## [Kvizi po predavanju](https://ff-quizzes.netlify.app/en/ds/)

## Spoznajte svoje gobe 🍄

Gobe so zelo zanimive. Uvozimo nabor podatkov, da jih preučimo:

```python
import pandas as pd
import matplotlib.pyplot as plt
mushrooms = pd.read_csv('../../data/mushrooms.csv')
mushrooms.head()
```
Izpiše se tabela z odličnimi podatki za analizo:


| class     | cap-shape | cap-surface | cap-color | bruises | odor    | gill-attachment | gill-spacing | gill-size | gill-color | stalk-shape | stalk-root | stalk-surface-above-ring | stalk-surface-below-ring | stalk-color-above-ring | stalk-color-below-ring | veil-type | veil-color | ring-number | ring-type | spore-print-color | population | habitat |
| --------- | --------- | ----------- | --------- | ------- | ------- | --------------- | ------------ | --------- | ---------- | ----------- | ---------- | ------------------------ | ------------------------ | ---------------------- | ---------------------- | --------- | ---------- | ----------- | --------- | ----------------- | ---------- | ------- |
| Strupena  | Konveksna | Gladka      | Rjava     | Modrice | Ostra   | Prosta          | Tesna        | Ozka      | Črna       | Širša       | Enaka      | Gladka                   | Gladka                   | Bela                   | Bela                   | Delna     | Bela       | Ena         | Viseča    | Črna              | Razpršena  | Urbana  |
| Užitna    | Konveksna | Gladka      | Rumena    | Modrice | Mandelj | Prosta          | Tesna        | Široka    | Črna       | Širša       | Klub       | Gladka                   | Gladka                   | Bela                   | Bela                   | Delna     | Bela       | Ena         | Viseča    | Rjava             | Številna   | Trava   |
| Užitna    | Zvonec    | Gladka      | Bela      | Modrice | Janež   | Prosta          | Tesna        | Široka    | Rjava      | Širša       | Klub       | Gladka                   | Gladka                   | Bela                   | Bela                   | Delna     | Bela       | Ena         | Viseča    | Rjava             | Številna   | Travniki |
| Strupena  | Konveksna | Luskasta    | Bela      | Modrice | Ostra   | Prosta          | Tesna        | Ozka      | Rjava      | Širša       | Enaka      | Gladka                   | Gladka                   | Bela                   | Bela                   | Delna     | Bela       | Ena         | Viseča    | Črna              | Razpršena  | Urbana  |

Takoj opazite, da so vsi podatki besedilni. Te podatke boste morali pretvoriti, da jih boste lahko uporabili v diagramu. Večina podatkov je dejansko predstavljena kot objekt:

```python
print(mushrooms.select_dtypes(["object"]).columns)
```

Rezultat je:

```output
Index(['class', 'cap-shape', 'cap-surface', 'cap-color', 'bruises', 'odor',
       'gill-attachment', 'gill-spacing', 'gill-size', 'gill-color',
       'stalk-shape', 'stalk-root', 'stalk-surface-above-ring',
       'stalk-surface-below-ring', 'stalk-color-above-ring',
       'stalk-color-below-ring', 'veil-type', 'veil-color', 'ring-number',
       'ring-type', 'spore-print-color', 'population', 'habitat'],
      dtype='object')
```
Pretvorite podatke in stolpec 'class' spremenite v kategorijo:

```python
cols = mushrooms.select_dtypes(["object"]).columns
mushrooms[cols] = mushrooms[cols].astype('category')
```

```python
edibleclass=mushrooms.groupby(['class']).count()
edibleclass
```

Če zdaj izpišete podatke o gobah, lahko vidite, da so razvrščeni v kategorije glede na razred strupenosti/užitnosti:


|           | cap-shape | cap-surface | cap-color | bruises | odor | gill-attachment | gill-spacing | gill-size | gill-color | stalk-shape | ... | stalk-surface-below-ring | stalk-color-above-ring | stalk-color-below-ring | veil-type | veil-color | ring-number | ring-type | spore-print-color | population | habitat |
| --------- | --------- | ----------- | --------- | ------- | ---- | --------------- | ------------ | --------- | ---------- | ----------- | --- | ------------------------ | ---------------------- | ---------------------- | --------- | ---------- | ----------- | --------- | ----------------- | ---------- | ------- |
| class     |           |             |           |         |      |                 |              |           |            |             |     |                          |                        |                        |           |            |             |           |                   |            |         |
| Užitna    | 4208      | 4208        | 4208      | 4208    | 4208 | 4208            | 4208         | 4208      | 4208       | 4208        | ... | 4208                     | 4208                   | 4208                   | 4208      | 4208       | 4208        | 4208      | 4208              | 4208       | 4208    |
| Strupena  | 3916      | 3916        | 3916      | 3916    | 3916 | 3916            | 3916         | 3916      | 3916       | 3916        | ... | 3916                     | 3916                   | 3916                   | 3916      | 3916       | 3916        | 3916      | 3916              | 3916       | 3916    |

Če sledite vrstnemu redu, predstavljenemu v tej tabeli, da ustvarite oznake kategorij razreda, lahko ustvarite tabelni diagram:

## Tabela!

```python
labels=['Edible','Poisonous']
plt.pie(edibleclass['population'],labels=labels,autopct='%.1f %%')
plt.title('Edible?')
plt.show()
```
Voila, tabelni diagram, ki prikazuje deleže teh podatkov glede na dva razreda gob. Zelo pomembno je, da pravilno določite vrstni red oznak, še posebej tukaj, zato preverite vrstni red, s katerim je zgrajeno polje oznak!

![pie chart](../../../../3-Data-Visualization/11-visualization-proportions/images/pie1-wb.png)

## Krogi!

Vizualno nekoliko bolj zanimiv tabelni diagram je krožni diagram, ki je tabelni diagram z luknjo na sredini. Poglejmo naše podatke s to metodo.

Oglejte si različna življenjska okolja, kjer rastejo gobe:

```python
habitat=mushrooms.groupby(['habitat']).count()
habitat
```
Tukaj razvrščate podatke po življenjskem okolju. Naštetih je 7, zato jih uporabite kot oznake za krožni diagram:

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

Ta koda nariše diagram in osrednji krog, nato pa ta osrednji krog doda v diagram. Širino osrednjega kroga lahko uredite tako, da spremenite `0.40` v drugo vrednost.

Krožni diagrami se lahko prilagodijo na več načinov, da spremenite oznake. Oznake je mogoče posebej poudariti za boljšo berljivost. Več o tem si preberite v [dokumentaciji](https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_and_donut_labels.html?highlight=donut).

Zdaj, ko veste, kako razvrstiti podatke in jih nato prikazati kot tabelo ali krog, lahko raziščete druge vrste diagramov. Poskusite waffle diagram, ki je le drugačen način raziskovanja količine.
## Waffle!

Diagram tipa 'waffle' je drugačen način vizualizacije količin kot 2D matrika kvadratov. Poskusite vizualizirati različne količine barv klobukov gob v tem naboru podatkov. Za to morate namestiti pomožno knjižnico [PyWaffle](https://pypi.org/project/pywaffle/) in uporabiti Matplotlib:

```python
pip install pywaffle
```

Izberite segment svojih podatkov za razvrščanje:

```python
capcolor=mushrooms.groupby(['cap-color']).count()
capcolor
```

Ustvarite waffle diagram tako, da ustvarite oznake in nato razvrstite svoje podatke:

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

Z uporabo waffle diagrama lahko jasno vidite deleže barv klobukov v tem naboru podatkov o gobah. Zanimivo je, da je veliko gob z zelenimi klobuki!

![waffle chart](../../../../3-Data-Visualization/11-visualization-proportions/images/waffle.png)

✅ Pywaffle podpira ikone znotraj diagramov, ki uporabljajo katero koli ikono, ki je na voljo v [Font Awesome](https://fontawesome.com/). Eksperimentirajte in ustvarite še bolj zanimiv waffle diagram z uporabo ikon namesto kvadratov.

V tej lekciji ste se naučili treh načinov vizualizacije deležev. Najprej morate razvrstiti podatke v kategorije in nato odločiti, kateri je najboljši način za prikaz podatkov - tabela, krog ali waffle. Vsi so okusni in uporabniku takoj ponudijo vpogled v nabor podatkov.

## 🚀 Izziv

Poskusite ponovno ustvariti te okusne diagrame v [Charticulator](https://charticulator.com).
## [Kvizi po predavanju](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/21)

## Pregled in samostojno učenje

Včasih ni očitno, kdaj uporabiti tabelo, krog ali waffle diagram. Tukaj je nekaj člankov za branje na to temo:

https://www.beautiful.ai/blog/battle-of-the-charts-pie-chart-vs-donut-chart

https://medium.com/@hypsypops/pie-chart-vs-donut-chart-showdown-in-the-ring-5d24fd86a9ce

https://www.mit.edu/~mbarker/formula1/f1help/11-ch-c6.htm

https://medium.datadriveninvestor.com/data-visualization-done-the-right-way-with-tableau-waffle-chart-fdf2a19be402

Raziskujte in poiščite več informacij o tej težki odločitvi.
## Naloga

[Poskusite v Excelu](assignment.md)

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki bi nastale zaradi uporabe tega prevoda.