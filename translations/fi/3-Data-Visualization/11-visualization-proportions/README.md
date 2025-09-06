<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "42119bcc97bee88254e381156d770f3c",
  "translation_date": "2025-09-05T22:42:54+00:00",
  "source_file": "3-Data-Visualization/11-visualization-proportions/README.md",
  "language_code": "fi"
}
-->
# Visualisoi osuuksia

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/11-Visualizing-Proportions.png)|
|:---:|
|Osuuksien visualisointi - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

Tässä oppitunnissa käytät toista luontoon keskittyvää tietojoukkoa visualisoidaksesi osuuksia, kuten kuinka monta erilaista sienityyppiä esiintyy tietojoukossa, joka käsittelee sieniä. Tutustutaan näihin kiehtoviin sieniin Audubonin tietojoukosta, joka sisältää tietoja 23 kiduksellisen sienen lajista Agaricus- ja Lepiota-suvuista. Kokeilet herkullisia visualisointeja, kuten:

- Piirakkakaavioita 🥧
- Donitsikaavioita 🍩
- Vohvelikaavioita 🧇

> 💡 Microsoft Researchin erittäin mielenkiintoinen projekti nimeltä [Charticulator](https://charticulator.com) tarjoaa ilmaisen vedä ja pudota -käyttöliittymän datavisualisointeihin. Yhdessä heidän tutoriaaleistaan käytetään myös tätä sienitietojoukkoa! Voit siis tutkia dataa ja oppia kirjaston käyttöä samanaikaisesti: [Charticulator-tutoriaali](https://charticulator.com/tutorials/tutorial4.html).

## [Esiluennon kysely](https://ff-quizzes.netlify.app/en/ds/quiz/20)

## Tutustu sieniin 🍄

Sienet ovat todella mielenkiintoisia. Tuodaan tietojoukko niiden tutkimiseksi:

```python
import pandas as pd
import matplotlib.pyplot as plt
mushrooms = pd.read_csv('../../data/mushrooms.csv')
mushrooms.head()
```
Tulostetaan taulukko, jossa on loistavaa analysoitavaa dataa:


| luokka    | lakin muoto | lakin pinta | lakin väri | mustelmat | haju    | kidusten kiinnitys | kidusten väli | kidusten koko | kidusten väri | jalan muoto | jalan juuri | jalan pinta renkaan yläpuolella | jalan pinta renkaan alapuolella | jalan väri renkaan yläpuolella | jalan väri renkaan alapuolella | kalvon tyyppi | kalvon väri | renkaiden määrä | renkaan tyyppi | itiöiden väri | populaatio | elinympäristö |
| --------- | ----------- | ----------- | ---------- | --------- | ------- | ------------------ | ------------- | ------------- | ------------- | ----------- | ----------- | ----------------------------- | ----------------------------- | ----------------------------- | ----------------------------- | ------------- | ----------- | --------------- | ------------- | ------------- | ----------- | ------------- |
| Myrkyllinen | Kupera     | Sileä       | Ruskea     | Mustelmat | Pistävä | Vapaa              | Tiheä         | Kapea         | Musta         | Laajeneva   | Tasainen    | Sileä                        | Sileä                        | Valkoinen                     | Valkoinen                     | Osittainen    | Valkoinen   | Yksi            | Riippuva      | Musta         | Hajallaan   | Kaupunki      |
| Syötävä    | Kupera     | Sileä       | Keltainen  | Mustelmat | Manteli | Vapaa              | Tiheä         | Leveä         | Musta         | Laajeneva   | Nuija       | Sileä                        | Sileä                        | Valkoinen                     | Valkoinen                     | Osittainen    | Valkoinen   | Yksi            | Riippuva      | Ruskea        | Lukuisia    | Nurmikot      |
| Syötävä    | Kellomainen | Sileä       | Valkoinen  | Mustelmat | Anis    | Vapaa              | Tiheä         | Leveä         | Ruskea        | Laajeneva   | Nuija       | Sileä                        | Sileä                        | Valkoinen                     | Valkoinen                     | Osittainen    | Valkoinen   | Yksi            | Riippuva      | Ruskea        | Lukuisia    | Niityt        |
| Myrkyllinen | Kupera     | Suomuinen   | Valkoinen  | Mustelmat | Pistävä | Vapaa              | Tiheä         | Kapea         | Ruskea        | Laajeneva   | Tasainen    | Sileä                        | Sileä                        | Valkoinen                     | Valkoinen                     | Osittainen    | Valkoinen   | Yksi            | Riippuva      | Musta         | Hajallaan   | Kaupunki      |

Heti huomaat, että kaikki data on tekstimuotoista. Sinun täytyy muuntaa tämä data, jotta voit käyttää sitä kaaviossa. Suurin osa datasta on itse asiassa esitetty objektina:

```python
print(mushrooms.select_dtypes(["object"]).columns)
```

Tuloste on:

```output
Index(['class', 'cap-shape', 'cap-surface', 'cap-color', 'bruises', 'odor',
       'gill-attachment', 'gill-spacing', 'gill-size', 'gill-color',
       'stalk-shape', 'stalk-root', 'stalk-surface-above-ring',
       'stalk-surface-below-ring', 'stalk-color-above-ring',
       'stalk-color-below-ring', 'veil-type', 'veil-color', 'ring-number',
       'ring-type', 'spore-print-color', 'population', 'habitat'],
      dtype='object')
```
Muunna tämän datan 'luokka'-sarake kategorioiksi:

```python
cols = mushrooms.select_dtypes(["object"]).columns
mushrooms[cols] = mushrooms[cols].astype('category')
```

```python
edibleclass=mushrooms.groupby(['class']).count()
edibleclass
```

Nyt, kun tulostat sienidatan, huomaat, että se on ryhmitelty kategorioihin myrkyllisen/syötävän luokan mukaan:


|           | lakin muoto | lakin pinta | lakin väri | mustelmat | haju | kidusten kiinnitys | kidusten väli | kidusten koko | kidusten väri | jalan muoto | ... | jalan pinta renkaan alapuolella | jalan väri renkaan yläpuolella | jalan väri renkaan alapuolella | kalvon tyyppi | kalvon väri | renkaiden määrä | renkaan tyyppi | itiöiden väri | populaatio | elinympäristö |
| --------- | ----------- | ----------- | ---------- | --------- | ---- | ------------------ | ------------- | ------------- | ------------- | ----------- | --- | ----------------------------- | ----------------------------- | ----------------------------- | ------------- | ----------- | --------------- | ------------- | ------------- | ----------- | ------------- |
| luokka    |             |             |            |           |      |                    |               |               |               |             |     |                               |                               |                               |               |             |                 |               |               |             |               |
| Syötävä   | 4208        | 4208        | 4208       | 4208      | 4208 | 4208               | 4208          | 4208          | 4208          | 4208        | ... | 4208                          | 4208                          | 4208                          | 4208          | 4208        | 4208            | 4208          | 4208          | 4208        | 4208          |
| Myrkyllinen | 3916      | 3916        | 3916       | 3916      | 3916 | 3916               | 3916          | 3916          | 3916          | 3916        | ... | 3916                          | 3916                          | 3916                          | 3916          | 3916        | 3916            | 3916          | 3916          | 3916        | 3916          |

Jos noudatat tämän taulukon järjestystä luodessasi luokkakategorioiden tunnisteita, voit rakentaa piirakkakaavion:

## Piirakka!

```python
labels=['Edible','Poisonous']
plt.pie(edibleclass['population'],labels=labels,autopct='%.1f %%')
plt.title('Edible?')
plt.show()
```
Kas näin, piirakkakaavio, joka näyttää tämän datan osuudet näiden kahden sieniluokan mukaan. On erittäin tärkeää saada tunnisteiden järjestys oikein, erityisesti tässä, joten varmista, että tarkistat tunnisteiden järjestyksen.

![piirakkakaavio](../../../../3-Data-Visualization/11-visualization-proportions/images/pie1-wb.png)

## Donitsit!

Hieman visuaalisesti kiinnostavampi piirakkakaavio on donitsikaavio, joka on piirakkakaavio, jossa on reikä keskellä. Katsotaanpa dataamme tällä tavalla.

Tarkastellaan eri elinympäristöjä, joissa sienet kasvavat:

```python
habitat=mushrooms.groupby(['habitat']).count()
habitat
```
Tässä ryhmittelet datasi elinympäristön mukaan. Niitä on listattu 7, joten käytä niitä donitsikaavion tunnisteina:

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

![donitsikaavio](../../../../3-Data-Visualization/11-visualization-proportions/images/donut-wb.png)

Tämä koodi piirtää kaavion ja keskirenkaan, ja lisää sitten keskirenkaan kaavioon. Muokkaa keskirenkaan leveyttä muuttamalla `0.40` toiseen arvoon.

Donitsikaavioita voi säätää monin tavoin, esimerkiksi tunnisteiden luettavuuden parantamiseksi. Lue lisää [dokumentaatiosta](https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_and_donut_labels.html?highlight=donut).

Nyt kun tiedät, miten ryhmitellä dataa ja esittää se piirakkana tai donitsina, voit tutkia muita kaaviotyyppejä. Kokeile vohvelikaaviota, joka on vain erilainen tapa tarkastella määriä.
## Vohvelit!

'Vohveli'-tyyppinen kaavio on erilainen tapa visualisoida määriä 2D-ruudukon avulla. Kokeile visualisoida tämän tietojoukon eri lakin värit. Tätä varten sinun täytyy asentaa apukirjasto nimeltä [PyWaffle](https://pypi.org/project/pywaffle/) ja käyttää Matplotlibia:

```python
pip install pywaffle
```

Valitse osa datastasi ryhmittelyä varten:

```python
capcolor=mushrooms.groupby(['cap-color']).count()
capcolor
```

Luo vohvelikaavio luomalla tunnisteet ja ryhmittelemällä datasi:

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

Vohvelikaavion avulla näet selvästi tämän sienitietojoukon lakin värien osuudet. Mielenkiintoista on, että on olemassa paljon vihreälakkisia sieniä!

![vohvelikaavio](../../../../3-Data-Visualization/11-visualization-proportions/images/waffle.png)

✅ PyWaffle tukee kuvakkeita kaavioissa, ja voit käyttää mitä tahansa [Font Awesomen](https://fontawesome.com/) kuvaketta. Kokeile luoda vielä mielenkiintoisempi vohvelikaavio käyttämällä kuvakkeita neliöiden sijaan.

Tässä oppitunnissa opit kolme tapaa visualisoida osuuksia. Ensin sinun täytyy ryhmitellä datasi kategorioihin ja sitten päättää, mikä on paras tapa esittää data - piirakka, donitsi tai vohveli. Kaikki ovat herkullisia ja tarjoavat käyttäjälle välittömän katsauksen tietojoukkoon.

## 🚀 Haaste

Kokeile luoda nämä herkulliset kaaviot uudelleen [Charticulatorissa](https://charticulator.com).
## [Jälkiluennon kysely](https://ff-quizzes.netlify.app/en/ds/quiz/21)

## Kertaus ja itseopiskelu

Aina ei ole selvää, milloin käyttää piirakka-, donitsi- tai vohvelikaaviota. Tässä muutamia artikkeleita aiheesta:

https://www.beautiful.ai/blog/battle-of-the-charts-pie-chart-vs-donut-chart

https://medium.com/@hypsypops/pie-chart-vs-donut-chart-showdown-in-the-ring-5d24fd86a9ce

https://www.mit.edu/~mbarker/formula1/f1help/11-ch-c6.htm

https://medium.datadriveninvestor.com/data-visualization-done-the-right-way-with-tableau-waffle-chart-fdf2a19be402

Tee tutkimusta löytääksesi lisää tietoa tästä hankalasta päätöksestä.
## Tehtävä

[Kokeile Excelissä](assignment.md)

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulee pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskääntämistä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinkäsityksistä tai virhetulkinnoista.