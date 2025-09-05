<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "42119bcc97bee88254e381156d770f3c",
  "translation_date": "2025-09-05T18:09:22+00:00",
  "source_file": "3-Data-Visualization/11-visualization-proportions/README.md",
  "language_code": "sk"
}
-->
# Vizualizácia proporcií

|![ Sketchnote od [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/11-Visualizing-Proportions.png)|
|:---:|
|Vizualizácia proporcií - _Sketchnote od [@nitya](https://twitter.com/nitya)_ |

V tejto lekcii použijete dataset zameraný na prírodu na vizualizáciu proporcií, napríklad koľko rôznych druhov húb sa nachádza v danom datasete o hubách. Preskúmajme tieto fascinujúce huby pomocou datasetu od Audubon, ktorý obsahuje podrobnosti o 23 druhoch húb s lupeňmi z rodov Agaricus a Lepiota. Budete experimentovať s chutnými vizualizáciami, ako sú:

- Koláčové grafy 🥧
- Donutové grafy 🍩
- Waflové grafy 🧇

> 💡 Veľmi zaujímavý projekt s názvom [Charticulator](https://charticulator.com) od Microsoft Research ponúka bezplatné rozhranie na vizualizáciu dát pomocou drag and drop. V jednom z ich tutoriálov používajú aj tento dataset o hubách! Takže môžete preskúmať dáta a zároveň sa naučiť pracovať s knižnicou: [Charticulator tutoriál](https://charticulator.com/tutorials/tutorial4.html).

## [Kvíz pred prednáškou](https://ff-quizzes.netlify.app/en/ds/quiz/20)

## Spoznajte svoje huby 🍄

Huby sú veľmi zaujímavé. Importujme dataset na ich štúdium:

```python
import pandas as pd
import matplotlib.pyplot as plt
mushrooms = pd.read_csv('../../data/mushrooms.csv')
mushrooms.head()
```
Vytlačí sa tabuľka s výbornými dátami na analýzu:


| trieda    | tvar klobúka | povrch klobúka | farba klobúka | modriny | vôňa    | pripojenie lupeňov | rozostup lupeňov | veľkosť lupeňov | farba lupeňov | tvar stonky | koreň stonky | povrch stonky nad prsteňom | povrch stonky pod prsteňom | farba stonky nad prsteňom | farba stonky pod prsteňom | typ závoja | farba závoja | počet prsteňov | typ prsteňa | farba výtrusov | populácia | biotop |
| --------- | ------------ | -------------- | ------------- | ------- | ------- | ------------------ | ---------------- | --------------- | ------------- | ----------- | ----------- | -------------------------- | -------------------------- | ------------------------ | ------------------------ | --------- | ----------- | -------------- | ----------- | ------------- | --------- | ------ |
| Jedovaté  | Konvexné     | Hladké         | Hnedé         | Modriny | Štipľavá | Voľné              | Tesné            | Úzke            | Čierne        | Rozširujúce | Rovné       | Hladké                     | Hladké                     | Biele                    | Biele                    | Čiastočné | Biele       | Jeden          | Závesné     | Čierne         | Roztrúsené | Mestské |
| Jedlé     | Konvexné     | Hladké         | Žlté          | Modriny | Mandľová | Voľné              | Tesné            | Široké          | Čierne        | Rozširujúce | Kyjakovité  | Hladké                     | Hladké                     | Biele                    | Biele                    | Čiastočné | Biele       | Jeden          | Závesné     | Hnedé          | Početné    | Trávnaté |
| Jedlé     | Zvoncovité   | Hladké         | Biele         | Modriny | Anízová  | Voľné              | Tesné            | Široké          | Hnedé         | Rozširujúce | Kyjakovité  | Hladké                     | Hladké                     | Biele                    | Biele                    | Čiastočné | Biele       | Jeden          | Závesné     | Hnedé          | Početné    | Lúky    |
| Jedovaté  | Konvexné     | Šupinaté       | Biele         | Modriny | Štipľavá | Voľné              | Tesné            | Úzke            | Hnedé         | Rozširujúce | Rovné       | Hladké                     | Hladké                     | Biele                    | Biele                    | Čiastočné | Biele       | Jeden          | Závesné     | Čierne         | Roztrúsené | Mestské |

Hneď si všimnete, že všetky dáta sú textové. Budete musieť tieto dáta konvertovať, aby ste ich mohli použiť v grafe. Väčšina dát je reprezentovaná ako objekt:

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
Vezmite tieto dáta a konvertujte stĺpec 'trieda' na kategóriu:

```python
cols = mushrooms.select_dtypes(["object"]).columns
mushrooms[cols] = mushrooms[cols].astype('category')
```

```python
edibleclass=mushrooms.groupby(['class']).count()
edibleclass
```

Teraz, keď vytlačíte dáta o hubách, môžete vidieť, že boli rozdelené do kategórií podľa triedy jedovaté/jedlé:


|           | tvar klobúka | povrch klobúka | farba klobúka | modriny | vôňa | pripojenie lupeňov | rozostup lupeňov | veľkosť lupeňov | farba lupeňov | tvar stonky | ... | povrch stonky pod prsteňom | farba stonky nad prsteňom | farba stonky pod prsteňom | typ závoja | farba závoja | počet prsteňov | typ prsteňa | farba výtrusov | populácia | biotop |
| --------- | ------------ | -------------- | ------------- | ------- | ---- | ------------------ | ---------------- | --------------- | ------------- | ----------- | --- | -------------------------- | ------------------------ | ------------------------ | --------- | ----------- | -------------- | ----------- | ------------- | --------- | ------ |
| trieda    |              |                |               |         |      |                    |                  |                 |               |             |     |                          |                        |                        |           |             |              |           |               |           |        |
| Jedlé     | 4208         | 4208           | 4208          | 4208    | 4208 | 4208              | 4208             | 4208            | 4208          | 4208        | ... | 4208                     | 4208                   | 4208                   | 4208      | 4208       | 4208          | 4208      | 4208          | 4208      | 4208   |
| Jedovaté  | 3916         | 3916           | 3916          | 3916    | 3916 | 3916              | 3916             | 3916            | 3916          | 3916        | ... | 3916                     | 3916                   | 3916                   | 3916      | 3916       | 3916          | 3916      | 3916          | 3916      | 3916   |

Ak budete postupovať podľa poradia uvedeného v tejto tabuľke na vytvorenie kategórií triedy, môžete vytvoriť koláčový graf:

## Koláč!

```python
labels=['Edible','Poisonous']
plt.pie(edibleclass['population'],labels=labels,autopct='%.1f %%')
plt.title('Edible?')
plt.show()
```
Voila, koláčový graf zobrazujúci proporcie týchto dát podľa dvoch tried húb. Je veľmi dôležité správne nastaviť poradie štítkov, najmä tu, takže si overte poradie, v akom je pole štítkov vytvorené!

![koláčový graf](../../../../3-Data-Visualization/11-visualization-proportions/images/pie1-wb.png)

## Donuty!

Trochu vizuálne zaujímavejší koláčový graf je donutový graf, čo je koláčový graf s dierou uprostred. Pozrime sa na naše dáta pomocou tejto metódy.

Pozrite sa na rôzne biotopy, kde rastú huby:

```python
habitat=mushrooms.groupby(['habitat']).count()
habitat
```
Tu zoskupujete svoje dáta podľa biotopu. Je ich uvedených 7, takže ich použite ako štítky pre váš donutový graf:

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

Tento kód nakreslí graf a stredový kruh, potom pridá tento stredový kruh do grafu. Upraviť šírku stredového kruhu môžete zmenou hodnoty `0.40` na inú hodnotu.

Donutové grafy je možné upraviť rôznymi spôsobmi, aby sa zmenili štítky. Štítky môžu byť zvýraznené pre lepšiu čitateľnosť. Viac sa dozviete v [dokumentácii](https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_and_donut_labels.html?highlight=donut).

Teraz, keď viete, ako zoskupiť svoje dáta a potom ich zobraziť ako koláč alebo donut, môžete preskúmať iné typy grafov. Skúste waflový graf, ktorý je len iným spôsobom skúmania množstva.
## Wafle!

Waflový graf je iný spôsob vizualizácie množstiev ako 2D pole štvorcov. Skúste vizualizovať rôzne množstvá farieb klobúkov húb v tomto datasete. Na to potrebujete nainštalovať pomocnú knižnicu s názvom [PyWaffle](https://pypi.org/project/pywaffle/) a použiť Matplotlib:

```python
pip install pywaffle
```

Vyberte segment svojich dát na zoskupenie:

```python
capcolor=mushrooms.groupby(['cap-color']).count()
capcolor
```

Vytvorte waflový graf vytvorením štítkov a následným zoskupením svojich dát:

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

Pomocou waflového grafu môžete jasne vidieť proporcie farieb klobúkov v tomto datasete húb. Zaujímavé je, že existuje veľa húb so zelenými klobúkmi!

![waflový graf](../../../../3-Data-Visualization/11-visualization-proportions/images/waffle.png)

✅ PyWaffle podporuje ikony v grafoch, ktoré používajú akúkoľvek ikonu dostupnú v [Font Awesome](https://fontawesome.com/). Urobte experimenty na vytvorenie ešte zaujímavejšieho waflového grafu pomocou ikon namiesto štvorcov.

V tejto lekcii ste sa naučili tri spôsoby vizualizácie proporcií. Najprv musíte zoskupiť svoje dáta do kategórií a potom rozhodnúť, ktorý spôsob zobrazenia dát je najlepší - koláč, donut alebo wafle. Všetky sú chutné a poskytujú používateľovi okamžitý prehľad o datasete.

## 🚀 Výzva

Skúste znovu vytvoriť tieto chutné grafy v [Charticulator](https://charticulator.com).
## [Kvíz po prednáške](https://ff-quizzes.netlify.app/en/ds/quiz/21)

## Prehľad a samostatné štúdium

Niekedy nie je zrejmé, kedy použiť koláčový, donutový alebo waflový graf. Tu sú niektoré články na túto tému:

https://www.beautiful.ai/blog/battle-of-the-charts-pie-chart-vs-donut-chart

https://medium.com/@hypsypops/pie-chart-vs-donut-chart-showdown-in-the-ring-5d24fd86a9ce

https://www.mit.edu/~mbarker/formula1/f1help/11-ch-c6.htm

https://medium.datadriveninvestor.com/data-visualization-done-the-right-way-with-tableau-waffle-chart-fdf2a19be402

Urobte si výskum, aby ste našli viac informácií o tomto náročnom rozhodnutí.
## Zadanie

[Skúste to v Exceli](assignment.md)

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.