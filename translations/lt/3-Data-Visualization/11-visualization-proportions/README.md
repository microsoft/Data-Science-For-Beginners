<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "42119bcc97bee88254e381156d770f3c",
  "translation_date": "2025-09-05T16:08:58+00:00",
  "source_file": "3-Data-Visualization/11-visualization-proportions/README.md",
  "language_code": "lt"
}
-->
# Vizualizuojame proporcijas

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/11-Visualizing-Proportions.png)|
|:---:|
|Vizualizuojame proporcijas - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

Šioje pamokoje naudosite kitą gamtos tematikos duomenų rinkinį, kad vizualizuotumėte proporcijas, pavyzdžiui, kiek skirtingų grybų rūšių yra tam tikrame duomenų rinkinyje apie grybus. Panagrinėkime šiuos įdomius grybus naudodami duomenų rinkinį iš Audubon, kuriame pateikiama informacija apie 23 rūšis grybų su lakšteliais iš Agaricus ir Lepiota šeimų. Eksperimentuosite su skaniais vizualizacijų tipais, tokiais kaip:

- Pyrago diagramos 🥧
- Spurgos diagramos 🍩
- Vaflių diagramos 🧇

> 💡 Labai įdomus projektas, vadinamas [Charticulator](https://charticulator.com) iš Microsoft Research, siūlo nemokamą „drag and drop“ sąsają duomenų vizualizacijoms. Viename iš jų mokymų taip pat naudojamas šis grybų duomenų rinkinys! Taigi galite tyrinėti duomenis ir tuo pačiu metu mokytis naudotis biblioteka: [Charticulator tutorial](https://charticulator.com/tutorials/tutorial4.html).

## [Prieš paskaitą - testas](https://ff-quizzes.netlify.app/en/ds/quiz/20)

## Susipažinkite su savo grybais 🍄

Grybai yra labai įdomūs. Importuokime duomenų rinkinį, kad juos išnagrinėtume:

```python
import pandas as pd
import matplotlib.pyplot as plt
mushrooms = pd.read_csv('../../data/mushrooms.csv')
mushrooms.head()
```
Atspausdinama lentelė su puikiais duomenimis analizei:


| klasė     | kepurėlės forma | kepurėlės paviršius | kepurėlės spalva | mėlynės | kvapas    | lakštelių tvirtinimas | lakštelių tarpai | lakštelių dydis | lakštelių spalva | kotelio forma | kotelio šaknis | kotelio paviršius virš žiedo | kotelio paviršius po žiedu | kotelio spalva virš žiedo | kotelio spalva po žiedu | šydo tipas | šydo spalva | žiedų skaičius | žiedo tipas | sporų atspaudo spalva | populiacija | buveinė |
| --------- | -------------- | ------------------- | ---------------- | ------- | -------- | -------------------- | ---------------- | -------------- | ---------------- | ------------- | ------------- | -------------------------- | -------------------------- | ------------------------ | ------------------------ | --------- | ---------- | ------------- | --------- | --------------------- | ---------- | ------- |
| Nuodingas | Išgaubta       | Lygi                | Ruda             | Mėlynės | Aitrus   | Laisvas              | Tankus           | Siauras         | Juoda            | Platėjantis   | Lygi          | Lygi                     | Lygi                     | Balta                   | Balta                   | Dalinis   | Balta      | Vienas        | Pakabukas | Juoda                 | Išsibarstę  | Miestas |
| Valgomas  | Išgaubta       | Lygi                | Geltona          | Mėlynės | Migdolų | Laisvas              | Tankus           | Platus          | Juoda            | Platėjantis   | Klubas        | Lygi                     | Lygi                     | Balta                   | Balta                   | Dalinis   | Balta      | Vienas        | Pakabukas | Ruda                  | Daugybė     | Žolės   |
| Valgomas  | Varpelis       | Lygi                | Balta            | Mėlynės | Anyžinis | Laisvas              | Tankus           | Platus          | Ruda             | Platėjantis   | Klubas        | Lygi                     | Lygi                     | Balta                   | Balta                   | Dalinis   | Balta      | Vienas        | Pakabukas | Ruda                  | Daugybė     | Pievos  |
| Nuodingas | Išgaubta       | Žvynuota            | Balta            | Mėlynės | Aitrus   | Laisvas              | Tankus           | Siauras         | Ruda             | Platėjantis   | Lygi          | Lygi                     | Lygi                     | Balta                   | Balta                   | Dalinis   | Balta      | Vienas        | Pakabukas | Juoda                 | Išsibarstę  | Miestas |

Iškart pastebite, kad visi duomenys yra tekstiniai. Turėsite konvertuoti šiuos duomenis, kad galėtumėte juos naudoti diagramoje. Dauguma duomenų iš tiesų yra pateikti kaip objektas:

```python
print(mushrooms.select_dtypes(["object"]).columns)
```

Rezultatas:

```output
Index(['class', 'cap-shape', 'cap-surface', 'cap-color', 'bruises', 'odor',
       'gill-attachment', 'gill-spacing', 'gill-size', 'gill-color',
       'stalk-shape', 'stalk-root', 'stalk-surface-above-ring',
       'stalk-surface-below-ring', 'stalk-color-above-ring',
       'stalk-color-below-ring', 'veil-type', 'veil-color', 'ring-number',
       'ring-type', 'spore-print-color', 'population', 'habitat'],
      dtype='object')
```
Paimkite šiuos duomenis ir konvertuokite „klasės“ stulpelį į kategoriją:

```python
cols = mushrooms.select_dtypes(["object"]).columns
mushrooms[cols] = mushrooms[cols].astype('category')
```

```python
edibleclass=mushrooms.groupby(['class']).count()
edibleclass
```

Dabar, jei atspausdinsite grybų duomenis, pamatysite, kad jie buvo suskirstyti į kategorijas pagal nuodingų/valgomų grybų klasę:


|           | kepurėlės forma | kepurėlės paviršius | kepurėlės spalva | mėlynės | kvapas | lakštelių tvirtinimas | lakštelių tarpai | lakštelių dydis | lakštelių spalva | kotelio forma | ... | kotelio paviršius po žiedu | kotelio spalva virš žiedo | kotelio spalva po žiedu | šydo tipas | šydo spalva | žiedų skaičius | žiedo tipas | sporų atspaudo spalva | populiacija | buveinė |
| --------- | -------------- | ------------------- | ---------------- | ------- | ------ | -------------------- | ---------------- | -------------- | ---------------- | ------------- | --- | -------------------------- | ------------------------ | ------------------------ | --------- | ---------- | ------------- | --------- | --------------------- | ---------- | ------- |
| klasė     |                |                     |                  |         |        |                      |                  |                |                  |               |     |                          |                        |                        |           |            |               |           |                     |            |         |
| Valgomas  | 4208           | 4208               | 4208             | 4208    | 4208   | 4208                | 4208             | 4208           | 4208             | 4208          | ... | 4208                     | 4208                   | 4208                   | 4208      | 4208       | 4208          | 4208      | 4208                 | 4208       | 4208    |
| Nuodingas | 3916           | 3916               | 3916             | 3916    | 3916   | 3916                | 3916             | 3916           | 3916             | 3916          | ... | 3916                     | 3916                   | 3916                   | 3916      | 3916       | 3916          | 3916      | 3916                 | 3916       | 3916    |

Jei laikysitės šioje lentelėje pateiktos tvarkos, kad sukurtumėte klasės kategorijos etiketes, galėsite sukurti pyrago diagramą:

## Pyragas!

```python
labels=['Edible','Poisonous']
plt.pie(edibleclass['population'],labels=labels,autopct='%.1f %%')
plt.title('Edible?')
plt.show()
```
Štai pyrago diagrama, rodanti šių duomenų proporcijas pagal šias dvi grybų klases. Labai svarbu teisingai nustatyti etikečių tvarką, ypač čia, todėl būtinai patikrinkite tvarką, kuria kuriamas etikečių masyvas!

![pyrago diagrama](../../../../3-Data-Visualization/11-visualization-proportions/images/pie1-wb.png)

## Spurgos!

Šiek tiek vizualiai įdomesnė pyrago diagrama yra spurgos diagrama, tai yra pyrago diagrama su skylute viduryje. Pažvelkime į mūsų duomenis naudodami šį metodą.

Pažvelkite į įvairias buveines, kuriose auga grybai:

```python
habitat=mushrooms.groupby(['habitat']).count()
habitat
```
Čia grupuojate savo duomenis pagal buveinę. Yra 7 išvardytos buveinės, todėl naudokite jas kaip etiketes savo spurgos diagramai:

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

![spurgos diagrama](../../../../3-Data-Visualization/11-visualization-proportions/images/donut-wb.png)

Šis kodas nupiešia diagramą ir centrinį apskritimą, tada prideda tą centrinį apskritimą į diagramą. Redaguokite centrinio apskritimo plotį pakeisdami „0.40“ į kitą reikšmę.

Spurgos diagramas galima koreguoti įvairiais būdais, kad pakeistumėte etiketes. Etiketės ypač gali būti paryškintos, kad būtų lengviau jas perskaityti. Sužinokite daugiau [dokumentacijoje](https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_and_donut_labels.html?highlight=donut).

Dabar, kai žinote, kaip grupuoti savo duomenis ir juos rodyti kaip pyrago ar spurgos diagramą, galite tyrinėti kitus diagramų tipus. Išbandykite vaflių diagramą, kuri yra tiesiog kitoks būdas tyrinėti kiekius.
## Vafliai!

„Vaflio“ tipo diagrama yra kitoks būdas vizualizuoti kiekius kaip 2D kvadratų masyvą. Pabandykite vizualizuoti skirtingus grybų kepurėlių spalvų kiekius šiame duomenų rinkinyje. Norėdami tai padaryti, turite įdiegti pagalbinę biblioteką, vadinamą [PyWaffle](https://pypi.org/project/pywaffle/) ir naudoti Matplotlib:

```python
pip install pywaffle
```

Pasirinkite duomenų segmentą grupavimui:

```python
capcolor=mushrooms.groupby(['cap-color']).count()
capcolor
```

Sukurkite vaflio diagramą, sukurdami etiketes ir tada grupuodami savo duomenis:

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

Naudodami vaflio diagramą, galite aiškiai matyti grybų kepurėlių spalvų proporcijas šiame duomenų rinkinyje. Įdomu tai, kad yra daug grybų su žaliomis kepurėlėmis!

![vaflio diagrama](../../../../3-Data-Visualization/11-visualization-proportions/images/waffle.png)

✅ Pywaffle palaiko piktogramas diagramose, kurios naudoja bet kokią piktogramą, esančią [Font Awesome](https://fontawesome.com/). Eksperimentuokite, kad sukurtumėte dar įdomesnę vaflio diagramą, naudodami piktogramas vietoj kvadratų.

Šioje pamokoje išmokote tris būdus vizualizuoti proporcijas. Pirmiausia turite grupuoti savo duomenis į kategorijas, o tada nuspręsti, kuris būdas geriausiai tinka duomenims rodyti - pyragas, spurga ar vaflis. Visi yra skanūs ir suteikia vartotojui greitą duomenų rinkinio vaizdą.

## 🚀 Iššūkis

Pabandykite atkurti šias skanias diagramas [Charticulator](https://charticulator.com).
## [Po paskaitos - testas](https://ff-quizzes.netlify.app/en/ds/quiz/21)

## Apžvalga ir savarankiškas mokymasis

Kartais nėra akivaizdu, kada naudoti pyrago, spurgos ar vaflio diagramą. Štai keletas straipsnių šia tema:

https://www.beautiful.ai/blog/battle-of-the-charts-pie-chart-vs-donut-chart

https://medium.com/@hypsypops/pie-chart-vs-donut-chart-showdown-in-the-ring-5d24fd86a9ce

https://www.mit.edu/~mbarker/formula1/f1help/11-ch-c6.htm

https://medium.datadriveninvestor.com/data-visualization-done-the-right-way-with-tableau-waffle-chart-fdf2a19be402

Atlikite tyrimus, kad rastumėte daugiau informacijos apie šį sudėtingą sprendimą.
## Užduotis

[Pabandykite tai Excel](assignment.md)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.