<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "87faccac113d772551486a67a607153e",
  "translation_date": "2025-08-26T22:50:24+00:00",
  "source_file": "3-Data-Visualization/10-visualization-distributions/README.md",
  "language_code": "fi"
}
-->
# Visualisointi: Jakautumat

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/10-Visualizing-Distributions.png)|
|:---:|
| Jakautumien visualisointi - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

Edellisessä osiossa opit mielenkiintoisia asioita Minnesotan lintudatasta. Löysit virheellistä dataa visualisoimalla poikkeamia ja tarkastelit lintukategorioiden eroja niiden maksimipituuden perusteella.

## [Esiluennon kysely](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/18)
## Tutustu lintudataan

Yksi tapa tutkia dataa on tarkastella sen jakautumaa eli miten data on järjestetty akselilla. Ehkä haluaisit esimerkiksi oppia, miten Minnesotan lintujen maksimisiipiväli tai maksimikehon massa jakautuu tässä datasetissä.

Tutkitaanpa joitakin faktoja tämän datasetin jakautumista. Tämän osion juurikansiossa olevassa _notebook.ipynb_-tiedostossa tuo Pandas, Matplotlib ja datasi:

```python
import pandas as pd
import matplotlib.pyplot as plt
birds = pd.read_csv('../../data/birds.csv')
birds.head()
```

|      | Nimi                         | Tieteellinen nimi      | Kategoria             | Lahko        | Heimo    | Suku        | Suojelustatus       | MinPituus | MaxPituus | MinKehonMassa | MaxKehonMassa | MinSiipiväli | MaxSiipiväli |
| ---: | :--------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :----------------- | --------: | --------: | ----------: | ----------: | ----------: | ----------: |
|    0 | Mustavatsainen viheltävä ankka | Dendrocygna autumnalis | Ankat/hanhet/vesilinnut | Anseriformes | Anatidae | Dendrocygna | LC                 |        47 |        56 |         652 |        1020 |          76 |          94 |
|    1 | Ruostevatsainen viheltävä ankka | Dendrocygna bicolor    | Ankat/hanhet/vesilinnut | Anseriformes | Anatidae | Dendrocygna | LC                 |        45 |        53 |         712 |        1050 |          85 |          93 |
|    2 | Lumihanhi                   | Anser caerulescens     | Ankat/hanhet/vesilinnut | Anseriformes | Anatidae | Anser       | LC                 |        64 |        79 |        2050 |        4050 |         135 |         165 |
|    3 | Rossin hanhi                 | Anser rossii           | Ankat/hanhet/vesilinnut | Anseriformes | Anatidae | Anser       | LC                 |      57.3 |        64 |        1066 |        1567 |         113 |         116 |
|    4 | Iso valkoposkihanhi          | Anser albifrons        | Ankat/hanhet/vesilinnut | Anseriformes | Anatidae | Anser       | LC                 |        64 |        81 |        1930 |        3310 |         130 |         165 |

Yleisesti ottaen datan jakautumaa voi nopeasti tarkastella käyttämällä hajontakaaviota, kuten teimme edellisessä osiossa:

```python
birds.plot(kind='scatter',x='MaxLength',y='Order',figsize=(12,8))

plt.title('Max Length per Order')
plt.ylabel('Order')
plt.xlabel('Max Length')

plt.show()
```
![maksimipituus per lahko](../../../../translated_images/scatter-wb.9d98b0ed7f0388af979441853361a11df5f518f5307938a503ca7913e986111b.fi.png)

Tämä antaa yleiskuvan lintujen kehon pituuden jakautumisesta per lahko, mutta se ei ole paras tapa esittää todellisia jakautumia. Tämä tehtävä hoidetaan yleensä histogrammilla.

## Työskentely histogrammien kanssa

Matplotlib tarjoaa erinomaisia tapoja visualisoida datan jakautumista histogrammien avulla. Tämä kaaviotyyppi muistuttaa pylväsdiagrammia, jossa jakautuma näkyy pylväiden nousuina ja laskuina. Histogrammin luomiseen tarvitaan numeerista dataa. Histogrammin luomiseksi voit piirtää kaavion määrittämällä tyypiksi 'hist' histogrammia varten. Tämä kaavio näyttää MaxBodyMass-jakautuman koko datasetin numeerisen datan alueella. Jakamalla sille annettu data pienempiin osiin (bins), se voi näyttää datan arvojen jakautuman:

```python
birds['MaxBodyMass'].plot(kind = 'hist', bins = 10, figsize = (12,12))
plt.show()
```
![jakautuma koko datasetissä](../../../../translated_images/dist1-wb.0d0cac82e2974fbbec635826fefead401af795f82e2279e2e2678bf2c117d827.fi.png)

Kuten näet, suurin osa datasetin yli 400 linnusta sijoittuu alle 2000 Max Body Mass -arvoon. Saat lisää tietoa datasta muuttamalla `bins`-parametrin suuremmaksi, esimerkiksi 30:

```python
birds['MaxBodyMass'].plot(kind = 'hist', bins = 30, figsize = (12,12))
plt.show()
```
![jakautuma datasetissä suuremmilla bins-parametreilla](../../../../translated_images/dist2-wb.2c0a7a3499b2fbf561e9f93b69f265dfc538dc78f6de15088ba84a88152e26ba.fi.png)

Tämä kaavio näyttää jakautuman hieman tarkemmalla tavalla. Vähemmän vasemmalle vinoutunut kaavio voidaan luoda varmistamalla, että valitset vain tietyn alueen datan:

Suodata datasi saadaksesi vain ne linnut, joiden kehon massa on alle 60, ja näytä 40 `bins`:

```python
filteredBirds = birds[(birds['MaxBodyMass'] > 1) & (birds['MaxBodyMass'] < 60)]      
filteredBirds['MaxBodyMass'].plot(kind = 'hist',bins = 40,figsize = (12,12))
plt.show()     
```
![suodatettu histogrammi](../../../../translated_images/dist3-wb.64b88db7f9780200bd486a2c2a3252548dd439672dbd3f778193db7f654b100c.fi.png)

✅ Kokeile muita suodattimia ja datapisteitä. Näytä datan koko jakautuma poistamalla `['MaxBodyMass']`-suodatin ja näytä nimettyjä jakautumia.

Histogrammi tarjoaa myös mukavia värien ja nimien parannuksia, joita kannattaa kokeilla:

Luo 2D-histogrammi vertaillaksesi kahden jakautuman välistä suhdetta. Verrataan `MaxBodyMass` ja `MaxLength`. Matplotlib tarjoaa sisäänrakennetun tavan näyttää yhtymäkohdat kirkkaammilla väreillä:

```python
x = filteredBirds['MaxBodyMass']
y = filteredBirds['MaxLength']

fig, ax = plt.subplots(tight_layout=True)
hist = ax.hist2d(x, y)
```
Näyttää siltä, että näiden kahden elementin välillä on odotettu korrelaatio odotetulla akselilla, ja yksi erityisen vahva yhtymäkohta:

![2D-kaavio](../../../../translated_images/2D-wb.ae22fdd33936507a41e3af22e11e4903b04a9be973b23a4e05214efaccfd66c8.fi.png)

Histogrammit toimivat oletuksena hyvin numeerisen datan kanssa. Entä jos haluat nähdä jakautumia tekstidatan mukaan? 
## Tutki datasettiä tekstidatan jakautumien osalta 

Tämä datasetti sisältää myös hyvää tietoa lintujen kategoriasta, suvusta, lajista ja heimosta sekä niiden suojelustilasta. Tutkitaanpa tätä suojelustietoa. Mikä on lintujen jakautuma niiden suojelustilanteen mukaan?

> ✅ Datasetissä käytetään useita lyhenteitä kuvaamaan suojelustilaa. Nämä lyhenteet tulevat [IUCN Red List Categories](https://www.iucnredlist.org) -organisaatiolta, joka luokittelee lajien tilan.
> 
> - CR: Äärimmäisen uhanalainen
> - EN: Uhanalainen
> - EX: Sukupuuttoon kuollut
> - LC: Vähiten huolta aiheuttava
> - NT: Lähes uhanalainen
> - VU: Haavoittuvainen

Nämä ovat tekstipohjaisia arvoja, joten sinun täytyy tehdä muunnos histogrammin luomiseksi. Käytä filteredBirds-dataframea ja näytä sen suojelustatus yhdessä minimisiipivälin kanssa. Mitä näet?

```python
x1 = filteredBirds.loc[filteredBirds.ConservationStatus=='EX', 'MinWingspan']
x2 = filteredBirds.loc[filteredBirds.ConservationStatus=='CR', 'MinWingspan']
x3 = filteredBirds.loc[filteredBirds.ConservationStatus=='EN', 'MinWingspan']
x4 = filteredBirds.loc[filteredBirds.ConservationStatus=='NT', 'MinWingspan']
x5 = filteredBirds.loc[filteredBirds.ConservationStatus=='VU', 'MinWingspan']
x6 = filteredBirds.loc[filteredBirds.ConservationStatus=='LC', 'MinWingspan']

kwargs = dict(alpha=0.5, bins=20)

plt.hist(x1, **kwargs, color='red', label='Extinct')
plt.hist(x2, **kwargs, color='orange', label='Critically Endangered')
plt.hist(x3, **kwargs, color='yellow', label='Endangered')
plt.hist(x4, **kwargs, color='green', label='Near Threatened')
plt.hist(x5, **kwargs, color='blue', label='Vulnerable')
plt.hist(x6, **kwargs, color='gray', label='Least Concern')

plt.gca().set(title='Conservation Status', ylabel='Min Wingspan')
plt.legend();
```

![siipiväli ja suojelustilanne](../../../../translated_images/histogram-conservation-wb.3c40450eb072c14de7a1a3ec5c0fcba4995531024760741b392911b567fd8b70.fi.png)

Näyttää siltä, ettei minimisiipivälin ja suojelustilanteen välillä ole hyvää korrelaatiota. Testaa datasetin muita elementtejä tällä menetelmällä. Voit kokeilla myös erilaisia suodattimia. Löydätkö mitään korrelaatiota?

## Tiheyskaaviot

Olet ehkä huomannut, että tähän mennessä tarkastellut histogrammit ovat "askelmia" eivätkä virtaa sujuvasti kaaren muodossa. Näyttääksesi tasaisemman tiheyskaavion, voit kokeilla tiheyskaaviota.

Tiheyskaavioiden kanssa työskentelyä varten tutustu uuteen kaaviokirjastoon, [Seaborn](https://seaborn.pydata.org/generated/seaborn.kdeplot.html). 

Lataa Seaborn ja kokeile perus tiheyskaaviota:

```python
import seaborn as sns
import matplotlib.pyplot as plt
sns.kdeplot(filteredBirds['MinWingspan'])
plt.show()
```
![Tiheyskaavio](../../../../translated_images/density1.8801043bd4af2567b0f706332b5853c7614e5e4b81b457acc27eb4e092a65cbd.fi.png)

Voit nähdä, kuinka kaavio muistuttaa aiempaa minimisiipivälin kaaviota; se on vain hieman tasaisempi. Seabornin dokumentaation mukaan "histogrammiin verrattuna KDE voi tuottaa kaavion, joka on vähemmän sekava ja helpommin tulkittava, erityisesti piirtäessä useita jakautumia. Mutta se voi aiheuttaa vääristymiä, jos taustalla oleva jakautuma on rajattu tai ei tasainen. Kuten histogrammi, myös esityksen laatu riippuu hyvien tasoitusparametrien valinnasta." [lähde](https://seaborn.pydata.org/generated/seaborn.kdeplot.html) Toisin sanoen poikkeamat, kuten aina, saavat kaaviosi käyttäytymään huonosti.

Jos haluaisit palata siihen epätasaiseen MaxBodyMass-linjaan toisessa rakentamassasi kaaviossa, voisit tasoittaa sen hyvin luomalla sen uudelleen tällä menetelmällä:

```python
sns.kdeplot(filteredBirds['MaxBodyMass'])
plt.show()
```
![tasainen kehonmassalinja](../../../../translated_images/density2.8e7647257060ff544a1aaded57e8dd1887586bfe340139e9b77ac1e5287f7977.fi.png)

Jos haluaisit tasaisen, mutta ei liian tasaisen linjan, muokkaa `bw_adjust`-parametria: 

```python
sns.kdeplot(filteredBirds['MaxBodyMass'], bw_adjust=.2)
plt.show()
```
![vähemmän tasainen kehonmassalinja](../../../../translated_images/density3.84ae27da82f31e6b83ad977646f029a1d21186574d7581facd70123b3eb257ee.fi.png)

✅ Lue tämän kaaviotyypin saatavilla olevista parametreista ja kokeile!

Tämä kaaviotyyppi tarjoaa kauniisti selittäviä visualisointeja. Esimerkiksi muutamalla koodirivillä voit näyttää lintujen maksimikehon massan tiheyden per lahko:

```python
sns.kdeplot(
   data=filteredBirds, x="MaxBodyMass", hue="Order",
   fill=True, common_norm=False, palette="crest",
   alpha=.5, linewidth=0,
)
```

![kehonmassa per lahko](../../../../translated_images/density4.e9d6c033f15c500fd33df94cb592b9f5cf1ed2a3d213c448a3f9e97ba39573ce.fi.png)

Voit myös kartoittaa useiden muuttujien tiheyden yhdessä kaaviossa. Testaa linnun MaxLength ja MinLength verrattuna niiden suojelustilaan:

```python
sns.kdeplot(data=filteredBirds, x="MinLength", y="MaxLength", hue="ConservationStatus")
```

![useita tiheyksiä, päällekkäin](../../../../translated_images/multi.56548caa9eae8d0fd9012a8586295538c7f4f426e2abc714ba070e2e4b1fc2c1.fi.png)

Ehkä kannattaa tutkia, onko 'Haavoittuvainen'-lintujen klusteri niiden pituuksien mukaan merkityksellinen vai ei.

## 🚀 Haaste

Histogrammit ovat kehittyneempiä kaaviotyyppejä kuin perushajontakaaviot, pylväsdiagrammit tai viivakaaviot. Etsi internetistä hyviä esimerkkejä histogrammien käytöstä. Miten niitä käytetään, mitä ne osoittavat ja millä aloilla tai tutkimusalueilla niitä yleensä käytetään?

## [Luennon jälkeinen kysely](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/19)

## Kertaus ja itseopiskelu

Tässä osiossa käytit Matplotlibia ja aloitit työskentelyn Seabornin kanssa näyttääkseen kehittyneempiä kaavioita. Tutki `kdeplot`-toimintoa Seabornissa, "jatkuva todennäköisyystiheyskäyrä yhdessä tai useammassa ulottuvuudessa". Lue [dokumentaatio](https://seaborn.pydata.org/generated/seaborn.kdeplot.html) ymmärtääksesi, miten se toimii.

## Tehtävä

[Hyödynnä taitojasi](assignment.md)

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.