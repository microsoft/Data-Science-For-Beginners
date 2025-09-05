<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "42119bcc97bee88254e381156d770f3c",
  "translation_date": "2025-09-05T17:12:34+00:00",
  "source_file": "3-Data-Visualization/11-visualization-proportions/README.md",
  "language_code": "sw"
}
-->
# Kuonyesha Uwiano

|![ Sketchnote na [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/11-Visualizing-Proportions.png)|
|:---:|
|Kuonyesha Uwiano - _Sketchnote na [@nitya](https://twitter.com/nitya)_ |

Katika somo hili, utatumia seti ya data inayohusiana na asili ili kuonyesha uwiano, kama vile idadi ya aina tofauti za uyoga zinazopatikana katika seti ya data kuhusu uyoga. Hebu tuchunguze uyoga huu wa kuvutia kwa kutumia seti ya data kutoka Audubon inayoorodhesha maelezo kuhusu spishi 23 za uyoga wenye magamba katika familia za Agaricus na Lepiota. Utajaribu mbinu za kuvutia za kuonyesha data kama:

- Chati za pai 🥧
- Chati za donati 🍩
- Chati za waffle 🧇

> 💡 Mradi wa kuvutia sana unaoitwa [Charticulator](https://charticulator.com) na Microsoft Research unatoa kiolesura cha bure cha kuburuta na kudondosha kwa ajili ya kuonyesha data. Katika mojawapo ya mafunzo yao wanatumia seti hii ya data ya uyoga! Kwa hivyo unaweza kuchunguza data na kujifunza maktaba kwa wakati mmoja: [Mafunzo ya Charticulator](https://charticulator.com/tutorials/tutorial4.html).

## [Jaribio la awali la somo](https://ff-quizzes.netlify.app/en/ds/quiz/20)

## Fahamu uyoga wako 🍄

Uyoga ni wa kuvutia sana. Hebu tuingize seti ya data ili kuwasoma:

```python
import pandas as pd
import matplotlib.pyplot as plt
mushrooms = pd.read_csv('../../data/mushrooms.csv')
mushrooms.head()
```
Jedwali linachapishwa likiwa na data nzuri kwa uchambuzi:


| darasa    | umbo la kofia | uso wa kofia | rangi ya kofia | majeraha | harufu   | kiambatisho cha magamba | nafasi ya magamba | ukubwa wa magamba | rangi ya magamba | umbo la shina | mzizi wa shina | uso wa shina juu ya pete | uso wa shina chini ya pete | rangi ya shina juu ya pete | rangi ya shina chini ya pete | aina ya pazia | rangi ya pazia | idadi ya pete | aina ya pete | rangi ya uchapaji wa spora | idadi ya watu | makazi |
| --------- | ------------- | ------------ | -------------- | -------- | -------- | ----------------------- | ----------------- | ----------------- | ---------------- | ------------- | ------------- | ------------------------ | ------------------------ | -------------------------- | -------------------------- | ------------- | ------------- | ------------- | ----------- | ------------------------ | ------------- | ------ |
| Sumu      | Mbonyeo       | Laini        | Kahawia        | Majeraha | Chungu   | Huru                   | Karibu            | Nyembamba         | Nyeusi          | Inapanuka     | Sawa          | Laini                   | Laini                   | Nyeupe                  | Nyeupe                  | Sehemu         | Nyeupe         | Moja          | Inaning'inia | Nyeusi                  | Imetawanyika  | Mjini  |
| Chakula   | Mbonyeo       | Laini        | Njano          | Majeraha | Mlozi    | Huru                   | Karibu            | Pana              | Nyeusi          | Inapanuka     | Klabu         | Laini                   | Laini                   | Nyeupe                  | Nyeupe                  | Sehemu         | Nyeupe         | Moja          | Inaning'inia | Kahawia                | Wengi          | Nyasi  |
| Chakula   | Kengele       | Laini        | Nyeupe         | Majeraha | Anise    | Huru                   | Karibu            | Pana              | Kahawia         | Inapanuka     | Klabu         | Laini                   | Laini                   | Nyeupe                  | Nyeupe                  | Sehemu         | Nyeupe         | Moja          | Inaning'inia | Kahawia                | Wengi          | Malisho |
| Sumu      | Mbonyeo       | Magamba      | Nyeupe         | Majeraha | Chungu   | Huru                   | Karibu            | Nyembamba         | Kahawia         | Inapanuka     | Sawa          | Laini                   | Laini                   | Nyeupe                  | Nyeupe                  | Sehemu         | Nyeupe         | Moja          | Inaning'inia | Nyeusi                  | Imetawanyika  | Mjini  |

Mara moja, unagundua kuwa data yote ni ya maandishi. Utalazimika kubadilisha data hii ili uweze kuitumia katika chati. Kwa kweli, data nyingi inawakilishwa kama kitu:

```python
print(mushrooms.select_dtypes(["object"]).columns)
```

Matokeo ni:

```output
Index(['class', 'cap-shape', 'cap-surface', 'cap-color', 'bruises', 'odor',
       'gill-attachment', 'gill-spacing', 'gill-size', 'gill-color',
       'stalk-shape', 'stalk-root', 'stalk-surface-above-ring',
       'stalk-surface-below-ring', 'stalk-color-above-ring',
       'stalk-color-below-ring', 'veil-type', 'veil-color', 'ring-number',
       'ring-type', 'spore-print-color', 'population', 'habitat'],
      dtype='object')
```
Chukua data hii na ubadilishe safu ya 'darasa' kuwa kategoria:

```python
cols = mushrooms.select_dtypes(["object"]).columns
mushrooms[cols] = mushrooms[cols].astype('category')
```

```python
edibleclass=mushrooms.groupby(['class']).count()
edibleclass
```

Sasa, ukichapisha data ya uyoga, utaona kuwa imepangwa katika kategoria kulingana na darasa la sumu/chakula:


|           | umbo la kofia | uso wa kofia | rangi ya kofia | majeraha | harufu | kiambatisho cha magamba | nafasi ya magamba | ukubwa wa magamba | rangi ya magamba | umbo la shina | ... | uso wa shina chini ya pete | rangi ya shina juu ya pete | rangi ya shina chini ya pete | aina ya pazia | rangi ya pazia | idadi ya pete | aina ya pete | rangi ya uchapaji wa spora | idadi ya watu | makazi |
| --------- | ------------- | ------------ | -------------- | -------- | ------ | ----------------------- | ----------------- | ----------------- | ---------------- | ------------- | --- | ------------------------ | -------------------------- | -------------------------- | ------------- | ------------- | ------------- | ----------- | ------------------------ | ------------- | ------ |
| darasa    |               |              |                |          |        |                         |                   |                   |                  |               |     |                          |                          |                          |               |               |               |             |                          |               |        |
| Chakula   | 4208          | 4208         | 4208           | 4208     | 4208   | 4208                    | 4208              | 4208              | 4208             | 4208          | ... | 4208                     | 4208                     | 4208                     | 4208          | 4208          | 4208          | 4208        | 4208                    | 4208           | 4208   |
| Sumu      | 3916          | 3916         | 3916           | 3916     | 3916   | 3916                    | 3916              | 3916              | 3916             | 3916          | ... | 3916                     | 3916                     | 3916                     | 3916          | 3916          | 3916          | 3916        | 3916                    | 3916           | 3916   |

Ukifuata mpangilio uliowasilishwa katika jedwali hili kuunda lebo za kategoria za darasa lako, unaweza kuunda chati ya pai:

## Pai!

```python
labels=['Edible','Poisonous']
plt.pie(edibleclass['population'],labels=labels,autopct='%.1f %%')
plt.title('Edible?')
plt.show()
```
Voila, chati ya pai inayoonyesha uwiano wa data hii kulingana na madarasa haya mawili ya uyoga. Ni muhimu sana kupata mpangilio wa lebo sahihi, hasa hapa, kwa hivyo hakikisha unathibitisha mpangilio ambao safu ya lebo imejengwa!

![chati ya pai](../../../../3-Data-Visualization/11-visualization-proportions/images/pie1-wb.png)

## Donati!

Chati ya pai yenye kuvutia zaidi kwa macho ni chati ya donati, ambayo ni chati ya pai yenye shimo katikati. Hebu tuangalie data yetu kwa kutumia mbinu hii.

Angalia makazi mbalimbali ambapo uyoga hukua:

```python
habitat=mushrooms.groupby(['habitat']).count()
habitat
```
Hapa, unapangilia data yako kulingana na makazi. Kuna 7 yaliyoorodheshwa, kwa hivyo tumia hayo kama lebo za chati yako ya donati:

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

![chati ya donati](../../../../3-Data-Visualization/11-visualization-proportions/images/donut-wb.png)

Msimbo huu unachora chati na mduara wa katikati, kisha unaongeza mduara huo wa katikati kwenye chati. Hariri upana wa mduara wa katikati kwa kubadilisha `0.40` kuwa thamani nyingine.

Chati za donati zinaweza kubadilishwa kwa njia kadhaa ili kubadilisha lebo. Lebo hasa zinaweza kuangaziwa ili kusomeka vizuri. Jifunze zaidi katika [docs](https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_and_donut_labels.html?highlight=donut).

Sasa kwa kuwa unajua jinsi ya kupanga data yako na kisha kuionyesha kama pai au donati, unaweza kuchunguza aina nyingine za chati. Jaribu chati ya waffle, ambayo ni njia tofauti ya kuchunguza idadi.

## Waffles!

Chati ya aina ya 'waffle' ni njia tofauti ya kuonyesha idadi kama safu ya 2D ya miraba. Jaribu kuonyesha idadi tofauti za rangi za kofia za uyoga katika seti hii ya data. Ili kufanya hivyo, unahitaji kusakinisha maktaba ya msaidizi inayoitwa [PyWaffle](https://pypi.org/project/pywaffle/) na kutumia Matplotlib:

```python
pip install pywaffle
```

Chagua sehemu ya data yako ili kuipanga:

```python
capcolor=mushrooms.groupby(['cap-color']).count()
capcolor
```

Unda chati ya waffle kwa kuunda lebo na kisha kupanga data yako:

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

Kwa kutumia chati ya waffle, unaweza kuona wazi uwiano wa rangi za kofia za uyoga katika seti hii ya data. Kwa kushangaza, kuna uyoga wengi wenye kofia za kijani!

![chati ya waffle](../../../../3-Data-Visualization/11-visualization-proportions/images/waffle.png)

✅ Pywaffle inaunga mkono ikoni ndani ya chati zinazotumia ikoni yoyote inayopatikana katika [Font Awesome](https://fontawesome.com/). Fanya majaribio kuunda chati ya waffle ya kuvutia zaidi kwa kutumia ikoni badala ya miraba.

Katika somo hili, ulijifunza njia tatu za kuonyesha uwiano. Kwanza, unahitaji kupanga data yako katika kategoria na kisha kuamua ni njia gani bora ya kuonyesha data - pai, donati, au waffle. Zote ni tamu na zinamfurahisha mtumiaji kwa muhtasari wa haraka wa seti ya data.

## 🚀 Changamoto

Jaribu kuunda upya chati hizi tamu katika [Charticulator](https://charticulator.com).
## [Jaribio la baada ya somo](https://ff-quizzes.netlify.app/en/ds/quiz/21)

## Mapitio & Kujisomea

Wakati mwingine si rahisi kujua ni lini utumie pai, donati, au chati ya waffle. Hapa kuna makala za kusoma kuhusu mada hii:

https://www.beautiful.ai/blog/battle-of-the-charts-pie-chart-vs-donut-chart

https://medium.com/@hypsypops/pie-chart-vs-donut-chart-showdown-in-the-ring-5d24fd86a9ce

https://www.mit.edu/~mbarker/formula1/f1help/11-ch-c6.htm

https://medium.datadriveninvestor.com/data-visualization-done-the-right-way-with-tableau-waffle-chart-fdf2a19be402

Fanya utafiti ili kupata maelezo zaidi kuhusu uamuzi huu mgumu.

## Kazi

[Jaribu katika Excel](assignment.md)

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya kutafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.