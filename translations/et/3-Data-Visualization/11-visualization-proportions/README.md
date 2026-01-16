<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "42119bcc97bee88254e381156d770f3c",
  "translation_date": "2025-10-11T15:55:13+00:00",
  "source_file": "3-Data-Visualization/11-visualization-proportions/README.md",
  "language_code": "et"
}
-->
# Proportsioonide visualiseerimine

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/11-Visualizing-Proportions.png)|
|:---:|
|Proportsioonide visualiseerimine - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

Selles õppetükis kasutad loodusele keskenduvat andmestikku, et visualiseerida proportsioone, näiteks kui palju erinevaid seeneliike esineb antud andmestikus seente kohta. Uurime neid põnevaid seeni, kasutades Auduboni andmestikku, mis sisaldab üksikasju 23 liigi kohta, mis kuuluvad Agaricus ja Lepiota perekondadesse. Katsetad maitsvaid visualiseerimismeetodeid, nagu:

- Pirukadiagrammid 🥧
- Sõõrikdiagrammid 🍩
- Vahvlidiagrammid 🧇

> 💡 Microsoft Researchi väga huvitav projekt nimega [Charticulator](https://charticulator.com) pakub tasuta lohistamisliidest andmete visualiseerimiseks. Ühes nende õpetuses kasutatakse samuti seda seente andmestikku! Nii saad andmeid uurida ja samal ajal raamatukogu tundma õppida: [Charticulator õpetus](https://charticulator.com/tutorials/tutorial4.html).

## [Eelloengu viktoriin](https://ff-quizzes.netlify.app/en/ds/quiz/20)

## Tutvu oma seentega 🍄

Seened on väga huvitavad. Impordime andmestiku, et neid uurida:

```python
import pandas as pd
import matplotlib.pyplot as plt
mushrooms = pd.read_csv('../../data/mushrooms.csv')
mushrooms.head()
```
Tabelis kuvatakse suurepärased andmed analüüsimiseks:


| klass     | kübara kuju | kübara pind | kübara värv | sinikad | lõhn    | eoslehe kinnitus | eoslehe vahe | eoslehe suurus | eoslehe värv | jala kuju | jala alus | jala pind rõnga kohal | jala pind rõnga all | jala värv rõnga kohal | jala värv rõnga all | loor tüüp | loor värv | rõngaste arv | rõnga tüüp | eospulbri värv | populatsioon | elupaik |
| --------- | ----------- | ----------- | ----------- | ------- | ------- | ----------------- | ------------ | -------------- | ------------ | --------- | --------- | --------------------- | --------------------- | --------------------- | --------------------- | --------- | --------- | ------------ | ----------- | -------------- | ------------ | ------- |
| Mürgine   | Kumer       | Sile        | Pruun       | Sinikad | Terav   | Vaba              | Tihe         | Kitsas         | Must         | Suurenev  | Võrdne    | Sile                   | Sile                   | Valge                 | Valge                 | Osaline   | Valge     | Üks          | Rippuv     | Must            | Hajus       | Linn    |
| Söödav    | Kumer       | Sile        | Kollane     | Sinikad | Mandli  | Vaba              | Tihe         | Lai            | Must         | Suurenev  | Klubikujuline | Sile                   | Sile                   | Valge                 | Valge                 | Osaline   | Valge     | Üks          | Rippuv     | Pruun           | Arvukas     | Rohumaa |
| Söödav    | Kellukakujuline | Sile    | Valge       | Sinikad | Aniisi  | Vaba              | Tihe         | Lai            | Pruun        | Suurenev  | Klubikujuline | Sile                   | Sile                   | Valge                 | Valge                 | Osaline   | Valge     | Üks          | Rippuv     | Pruun           | Arvukas     | Niit    |
| Mürgine   | Kumer       | Kaaluline   | Valge       | Sinikad | Terav   | Vaba              | Tihe         | Kitsas         | Pruun        | Suurenev  | Võrdne    | Sile                   | Sile                   | Valge                 | Valge                 | Osaline   | Valge     | Üks          | Rippuv     | Must            | Hajus       | Linn    |

Kohe märkad, et kõik andmed on tekstilised. Pead need andmed teisendama, et neid diagrammis kasutada. Enamik andmeid on tegelikult esitatud objektina:

```python
print(mushrooms.select_dtypes(["object"]).columns)
```

Väljund on:

```output
Index(['class', 'cap-shape', 'cap-surface', 'cap-color', 'bruises', 'odor',
       'gill-attachment', 'gill-spacing', 'gill-size', 'gill-color',
       'stalk-shape', 'stalk-root', 'stalk-surface-above-ring',
       'stalk-surface-below-ring', 'stalk-color-above-ring',
       'stalk-color-below-ring', 'veil-type', 'veil-color', 'ring-number',
       'ring-type', 'spore-print-color', 'population', 'habitat'],
      dtype='object')
```
Teisenda need andmed ja muuda 'klass' veerg kategooriaks:

```python
cols = mushrooms.select_dtypes(["object"]).columns
mushrooms[cols] = mushrooms[cols].astype('category')
```

```python
edibleclass=mushrooms.groupby(['class']).count()
edibleclass
```

Kui prindid seente andmed välja, näed, et need on rühmitatud kategooriatesse vastavalt mürgiste/söödavate klassidele:


|           | kübara kuju | kübara pind | kübara värv | sinikad | lõhn | eoslehe kinnitus | eoslehe vahe | eoslehe suurus | eoslehe värv | jala kuju | ... | jala pind rõnga all | jala värv rõnga kohal | jala värv rõnga all | loor tüüp | loor värv | rõngaste arv | rõnga tüüp | eospulbri värv | populatsioon | elupaik |
| --------- | ----------- | ----------- | ----------- | ------- | ---- | ----------------- | ------------ | -------------- | ------------ | --------- | --- | --------------------- | --------------------- | --------------------- | --------- | --------- | ------------ | ----------- | -------------- | ------------ | ------- |
| klass     |             |             |             |         |      |                   |              |                |              |           |     |                       |                       |                       |           |           |              |             |                |              |         |
| Söödav    | 4208        | 4208        | 4208        | 4208    | 4208 | 4208              | 4208         | 4208           | 4208         | 4208      | ... | 4208                 | 4208                 | 4208                 | 4208      | 4208      | 4208         | 4208        | 4208            | 4208         | 4208    |
| Mürgine   | 3916        | 3916        | 3916        | 3916    | 3916 | 3916              | 3916         | 3916           | 3916         | 3916      | ... | 3916                 | 3916                 | 3916                 | 3916      | 3916      | 3916         | 3916        | 3916            | 3916         | 3916    |

Kui järgida tabelis esitatud järjekorda klassi kategooria siltide loomiseks, saad koostada pirukadiagrammi:

## Pirukas!

```python
labels=['Edible','Poisonous']
plt.pie(edibleclass['population'],labels=labels,autopct='%.1f %%')
plt.title('Edible?')
plt.show()
```
Voila, pirukadiagramm, mis näitab andmete proportsioone vastavalt nendele kahele seente klassile. On üsna oluline saada siltide järjekord õigeks, eriti siin, seega kontrolli kindlasti järjekorda, millega siltide massiiv on koostatud!

![pirukadiagramm](../../../../translated_images/et/pie1-wb.e201f2fcc335413143ce37650fb7f5f0bb21358e7823a327ed8644dfb84be9db.png)

## Sõõrikud!

Visuaalselt huvitavam pirukadiagramm on sõõrikdiagramm, mis on pirukadiagramm, mille keskel on auk. Vaatame meie andmeid selle meetodi abil.

Vaata erinevaid elupaiku, kus seened kasvavad:

```python
habitat=mushrooms.groupby(['habitat']).count()
habitat
```
Siin rühmitad oma andmed elupaikade järgi. Neid on loetletud 7, seega kasuta neid sõõrikdiagrammi siltidena:

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

![sõõrikdiagramm](../../../../translated_images/et/donut-wb.be3c12a22712302b5d10c40014d5389d4a1ae4412fe1655b3cf4af57b64f799a.png)

See kood joonistab diagrammi ja keskse ringi, seejärel lisab selle keskse ringi diagrammi. Muuda keskse ringi laiust, muutes `0.40` mõneks teiseks väärtuseks.

Sõõrikdiagramme saab mitmel viisil kohandada, et muuta silte. Eriti silte saab esile tõsta loetavuse parandamiseks. Loe rohkem [dokumentatsioonist](https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_and_donut_labels.html?highlight=donut).

Nüüd, kui tead, kuidas oma andmeid rühmitada ja seejärel kuvada neid piruka või sõõrikuna, saad uurida teisi diagrammitüüpe. Proovi vahvlidiagrammi, mis on lihtsalt teistsugune viis koguste uurimiseks.
## Vahvlid!

'Vahvli' tüüpi diagramm on teistsugune viis koguste visualiseerimiseks 2D ruutude massiivina. Proovi visualiseerida erinevaid seente kübara värvide koguseid selles andmestikus. Selleks pead installima abiraamatukogu nimega [PyWaffle](https://pypi.org/project/pywaffle/) ja kasutama Matplotlibi:

```python
pip install pywaffle
```

Vali oma andmetest segment, mida rühmitada:

```python
capcolor=mushrooms.groupby(['cap-color']).count()
capcolor
```

Loo vahvlidiagramm, luues sildid ja seejärel rühmitades oma andmed:

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

Vahvlidiagrammi abil näed selgelt seente kübara värvide proportsioone selles andmestikus. Huvitaval kombel on palju rohelise kübaraga seeni!

![vahvlidiagramm](../../../../translated_images/et/waffle.5455dbae4ccf17d53bb40ff0a657ecef7b8aa967e27a19cc96325bd81598f65e.png)

✅ PyWaffle toetab ikoone diagrammides, mis kasutavad kõiki ikoone, mis on saadaval [Font Awesome](https://fontawesome.com/) lehel. Katseta, et luua veelgi huvitavam vahvlidiagramm, kasutades ruutude asemel ikoone.

Selles õppetükis õppisid kolme viisi proportsioonide visualiseerimiseks. Kõigepealt pead oma andmed rühmitama kategooriatesse ja seejärel otsustama, milline on parim viis andmete kuvamiseks - pirukas, sõõrik või vahvel. Kõik on maitsvad ja pakuvad kasutajale kohest ülevaadet andmestikust.

## 🚀 Väljakutse

Proovi neid maitsvaid diagramme uuesti luua [Charticulatoris](https://charticulator.com).
## [Järelloengu viktoriin](https://ff-quizzes.netlify.app/en/ds/quiz/21)

## Ülevaade ja iseseisev õppimine

Mõnikord pole ilmne, millal kasutada piruka-, sõõriku- või vahvlidiagrammi. Siin on mõned artiklid, mida sellel teemal lugeda:

https://www.beautiful.ai/blog/battle-of-the-charts-pie-chart-vs-donut-chart

https://medium.com/@hypsypops/pie-chart-vs-donut-chart-showdown-in-the-ring-5d24fd86a9ce

https://www.mit.edu/~mbarker/formula1/f1help/11-ch-c6.htm

https://medium.datadriveninvestor.com/data-visualization-done-the-right-way-with-tableau-waffle-chart-fdf2a19be402

Tee uurimistööd, et leida rohkem teavet selle keerulise otsuse kohta.
## Ülesanne

[Proovi Excelis](assignment.md)

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.