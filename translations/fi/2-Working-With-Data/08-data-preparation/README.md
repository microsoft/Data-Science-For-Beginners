<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "90a815d332aea41a222f4c6372e7186e",
  "translation_date": "2025-09-04T19:39:17+00:00",
  "source_file": "2-Working-With-Data/08-data-preparation/README.md",
  "language_code": "fi"
}
-->
# Työskentely datan kanssa: Datan valmistelu

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/08-DataPreparation.png)|
|:---:|
|Datan valmistelu - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

## [Ennakkokysely](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/14)

Riippuen datan lähteestä, raakadata voi sisältää epäjohdonmukaisuuksia, jotka aiheuttavat haasteita analyysissä ja mallinnuksessa. Toisin sanoen, tämä data voidaan luokitella "likaiseksi" ja se täytyy siivota. Tämä oppitunti keskittyy tekniikoihin, joilla dataa puhdistetaan ja muokataan käsittelemään puuttuvaa, epätarkkaa tai epätäydellistä dataa. Oppitunnin aiheet hyödyntävät Pythonia ja Pandas-kirjastoa, ja niitä [havainnollistetaan notebookissa](notebook.ipynb) tässä hakemistossa.

## Datan puhdistamisen merkitys

- **Helppokäyttöisyys ja uudelleenkäyttö**: Kun data on asianmukaisesti järjestetty ja normalisoitu, sitä on helpompi etsiä, käyttää ja jakaa muiden kanssa.

- **Johdonmukaisuus**: Data-analytiikka vaatii usein työskentelyä useamman datasetin kanssa, jolloin eri lähteistä tulevat datasetit täytyy yhdistää. Varmistamalla, että jokainen yksittäinen datasetti noudattaa yhteisiä standardeja, varmistetaan datan hyödyllisyys, kun ne yhdistetään yhdeksi datasetiksi.

- **Mallin tarkkuus**: Puhdistettu data parantaa mallien tarkkuutta, jotka perustuvat siihen.

## Yleiset puhdistustavoitteet ja -strategiat

- **Datasetin tutkiminen**: Datan tutkiminen, joka käsitellään [myöhemmässä oppitunnissa](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/4-Data-Science-Lifecycle/15-analyzing), auttaa tunnistamaan datan, joka täytyy siivota. Datasetin arvojen visuaalinen tarkastelu voi luoda odotuksia siitä, miltä loput datasetistä näyttää, tai antaa käsityksen ongelmista, jotka voidaan ratkaista. Tutkiminen voi sisältää peruskyselyitä, visualisointeja ja näytteenottoa.

- **Muotoilu**: Riippuen lähteestä, datassa voi olla epäjohdonmukaisuuksia sen esitystavassa. Tämä voi aiheuttaa ongelmia arvon etsimisessä ja esittämisessä, jolloin arvo näkyy datasetissä, mutta ei ole asianmukaisesti esitetty visualisoinneissa tai kyselytuloksissa. Yleisiä muotoiluongelmia ovat välilyöntien, päivämäärien ja datatyypin korjaaminen. Muotoiluongelmien ratkaiseminen on yleensä datan käyttäjien vastuulla. Esimerkiksi päivämäärien ja numeroiden esitystavat voivat vaihdella maittain.

- **Kaksoiskappaleet**: Data, jossa on useampi esiintymä, voi tuottaa epätarkkoja tuloksia ja yleensä tulisi poistaa. Tämä on yleistä, kun yhdistetään kaksi tai useampi datasetti. On kuitenkin tilanteita, joissa yhdistettyjen datasetien kaksoiskappaleet sisältävät lisätietoa, joka voi olla tarpeen säilyttää.

- **Puuttuva data**: Puuttuva data voi aiheuttaa epätarkkuuksia sekä heikkoja tai puolueellisia tuloksia. Joskus nämä voidaan ratkaista lataamalla data uudelleen, täyttämällä puuttuvat arvot laskennalla ja koodilla, kuten Pythonilla, tai yksinkertaisesti poistamalla arvo ja vastaava data. Syyt datan puuttumiseen voivat vaihdella, ja toimenpiteet puuttuvien arvojen korjaamiseksi riippuvat siitä, miten ja miksi ne ovat kadonneet.

## DataFramen tietojen tutkiminen
> **Oppimistavoite:** Tämän osion lopussa sinun tulisi olla mukava löytää yleistä tietoa pandas DataFrameihin tallennetusta datasta.

Kun olet ladannut datasi pandas-kirjastoon, se on todennäköisesti DataFrame-muodossa (katso edellinen [oppitunti](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/2-Working-With-Data/07-python#dataframe) saadaksesi yksityiskohtaisen yleiskatsauksen). Mutta jos DataFramessa on 60 000 riviä ja 400 saraketta, mistä edes aloitat saadaksesi käsityksen siitä, mitä sinulla on? Onneksi [pandas](https://pandas.pydata.org/) tarjoaa käteviä työkaluja, joilla voit nopeasti tarkastella DataFramen yleistä tietoa sekä sen ensimmäisiä ja viimeisiä rivejä.

Tämän toiminnallisuuden tutkimiseksi tuomme Pythonin scikit-learn-kirjaston ja käytämme ikonista datasettiä: **Iris-datasettiä**.

```python
import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()
iris_df = pd.DataFrame(data=iris['data'], columns=iris['feature_names'])
```
|                                        |sepal length (cm)|sepal width (cm)|petal length (cm)|petal width (cm)|
|----------------------------------------|-----------------|----------------|-----------------|----------------|
|0                                       |5.1              |3.5             |1.4              |0.2             |
|1                                       |4.9              |3.0             |1.4              |0.2             |
|2                                       |4.7              |3.2             |1.3              |0.2             |
|3                                       |4.6              |3.1             |1.5              |0.2             |
|4                                       |5.0              |3.6             |1.4              |0.2             |

- **DataFrame.info**: Aloitetaan `info()`-metodilla, joka tulostaa yhteenvedon DataFramen sisällöstä. Katsotaanpa tätä datasettiä:
```python
iris_df.info()
```
```
RangeIndex: 150 entries, 0 to 149
Data columns (total 4 columns):
 #   Column             Non-Null Count  Dtype  
---  ------             --------------  -----  
 0   sepal length (cm)  150 non-null    float64
 1   sepal width (cm)   150 non-null    float64
 2   petal length (cm)  150 non-null    float64
 3   petal width (cm)   150 non-null    float64
dtypes: float64(4)
memory usage: 4.8 KB
```
Tästä tiedämme, että *Iris*-datasetissä on 150 merkintää neljässä sarakkeessa, eikä siinä ole puuttuvia arvoja. Kaikki data on tallennettu 64-bittisinä liukulukuina.

- **DataFrame.head()**: Seuraavaksi tarkastellaan DataFramen varsinaista sisältöä `head()`-metodilla. Katsotaanpa, miltä `iris_df`:n ensimmäiset rivit näyttävät:
```python
iris_df.head()
```
```
   sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
0                5.1               3.5                1.4               0.2
1                4.9               3.0                1.4               0.2
2                4.7               3.2                1.3               0.2
3                4.6               3.1                1.5               0.2
4                5.0               3.6                1.4               0.2
```
- **DataFrame.tail()**: Vastaavasti tarkastellaan DataFramen viimeisiä rivejä `tail()`-metodilla:
```python
iris_df.tail()
```
```
     sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
145                6.7               3.0                5.2               2.3
146                6.3               2.5                5.0               1.9
147                6.5               3.0                5.2               2.0
148                6.2               3.4                5.4               2.3
149                5.9               3.0                5.1               1.8
```
> **Yhteenveto:** Jo pelkästään tarkastelemalla DataFramen metatietoja tai sen ensimmäisiä ja viimeisiä arvoja, voit saada välittömän käsityksen datan koosta, muodosta ja sisällöstä.

## Puuttuvan datan käsittely
> **Oppimistavoite:** Tämän osion lopussa sinun tulisi osata korvata tai poistaa DataFramen null-arvot.

Useimmiten datasetit, joita haluat käyttää (tai joudut käyttämään), sisältävät puuttuvia arvoja. Puuttuvan datan käsittelyyn liittyy hienovaraisia kompromisseja, jotka voivat vaikuttaa lopulliseen analyysiin ja todellisiin tuloksiin.

Pandas käsittelee puuttuvia arvoja kahdella tavalla. Ensimmäinen, jonka olet nähnyt aiemmissa osioissa, on `NaN` eli Not a Number. Tämä on erityinen arvo, joka kuuluu IEEE-liukuluku-määrittelyyn ja sitä käytetään vain puuttuvien liukulukuarvojen merkitsemiseen.

Muiden kuin liukulukuarvojen puuttumiseen pandas käyttää Pythonin `None`-objektia. Vaikka voi tuntua hämmentävältä, että kohtaat kaksi erilaista arvoa, jotka tarkoittavat käytännössä samaa asiaa, tähän suunnitteluratkaisuun on hyvät ohjelmalliset syyt, ja käytännössä tämä lähestymistapa mahdollistaa pandasille hyvän kompromissin useimmissa tapauksissa. Tästä huolimatta sekä `None` että `NaN` sisältävät rajoituksia, jotka sinun tulee ottaa huomioon niiden käyttöön liittyen.

Lisätietoja `NaN`- ja `None`-arvoista löytyy [notebookista](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/4-Data-Science-Lifecycle/15-analyzing/notebook.ipynb)!

- **Null-arvojen havaitseminen**: Pandasissa `isnull()`- ja `notnull()`-metodit ovat ensisijaisia menetelmiä null-datan havaitsemiseen. Molemmat palauttavat Boolean-maskit datan päälle. Käytämme `numpy`-kirjastoa `NaN`-arvojen kanssa:
```python
import numpy as np

example1 = pd.Series([0, np.nan, '', None])
example1.isnull()
```
```
0    False
1     True
2    False
3     True
dtype: bool
```
Katso tarkasti tulosta. Yllättääkö jokin? Vaikka `0` on aritmeettinen null, se on silti täysin kelvollinen kokonaisluku, ja pandas käsittelee sen sellaisena. `''` on hieman hienovaraisempi. Vaikka käytimme sitä osassa 1 tyhjän merkkijonon edustamiseen, se on silti merkkijono-objekti eikä null-arvon edustus pandasissa.

Käännetään tämä nyt ympäri ja käytetään näitä metodeja enemmän käytännönläheisesti. Voit käyttää Boolean-maskeja suoraan ``Series``- tai ``DataFrame``-indeksinä, mikä voi olla hyödyllistä, kun yrität työskennellä eristettyjen puuttuvien (tai olemassa olevien) arvojen kanssa.

> **Yhteenveto**: Sekä `isnull()`- että `notnull()`-metodit tuottavat samanlaisia tuloksia, kun käytät niitä `DataFrame`-muodossa: ne näyttävät tulokset ja niiden indeksit, mikä auttaa sinua valtavasti datan käsittelyssä.

- **Null-arvojen poistaminen**: Null-arvojen tunnistamisen lisäksi pandas tarjoaa kätevän tavan poistaa null-arvot `Series`- ja `DataFrame`-muodoista. (Erityisesti suurissa dataseteissä on usein suositeltavampaa yksinkertaisesti poistaa puuttuvat [NA] arvot analyysistä kuin käsitellä niitä muilla tavoilla.) Katsotaanpa tätä käytännössä `example1`-datasetillä:
```python
example1 = example1.dropna()
example1
```
```
0    0
2     
dtype: object
```
Huomaa, että tämän pitäisi näyttää samalta kuin tuloksesi `example3[example3.notnull()]`. Ero on siinä, että `dropna` on poistanut puuttuvat arvot `Series`-muodosta `example1`.

Koska `DataFrame`-muodossa on kaksi ulottuvuutta, se tarjoaa enemmän vaihtoehtoja datan poistamiseen.

```python
example2 = pd.DataFrame([[1,      np.nan, 7], 
                         [2,      5,      8], 
                         [np.nan, 6,      9]])
example2
```
|      | 0 | 1 | 2 |
|------|---|---|---|
|0     |1.0|NaN|7  |
|1     |2.0|5.0|8  |
|2     |NaN|6.0|9  |

(Huomasitko, että pandas muutti kaksi saraketta liukuluvuiksi mukauttaakseen `NaN`-arvot?)

Et voi poistaa yksittäistä arvoa `DataFrame`-muodosta, joten sinun täytyy poistaa kokonaisia rivejä tai sarakkeita. Riippuen siitä, mitä teet, saatat haluta tehdä jomman kumman, ja pandas antaa sinulle vaihtoehtoja molempiin. Koska data-analytiikassa sarakkeet edustavat yleensä muuttujia ja rivit havaintoja, olet todennäköisemmin poistamassa rivejä datasta; `dropna()`-metodin oletusasetus on poistaa kaikki rivit, jotka sisältävät null-arvoja:

```python
example2.dropna()
```
```
	0	1	2
1	2.0	5.0	8
```
Tarvittaessa voit poistaa NA-arvot sarakkeista. Käytä `axis=1` tehdäksesi niin:
```python
example2.dropna(axis='columns')
```
```
	2
0	7
1	8
2	9
```
Huomaa, että tämä voi poistaa paljon dataa, jonka haluaisit säilyttää, erityisesti pienemmissä dataseteissä. Entä jos haluat poistaa vain rivit tai sarakkeet, jotka sisältävät useita tai jopa kaikki null-arvot? Voit määrittää nämä asetukset `dropna`-metodissa `how`- ja `thresh`-parametreilla.

Oletuksena `how='any'` (jos haluat tarkistaa itse tai nähdä, mitä muita parametreja metodilla on, suorita `example4.dropna?` koodisolussa). Voit vaihtoehtoisesti määrittää `how='all'`, jolloin poistetaan vain rivit tai sarakkeet, jotka sisältävät kaikki null-arvot. Laajennetaan esimerkkimme `DataFrame`-muotoa nähdäksesi tämä käytännössä.

```python
example2[3] = np.nan
example2
```
|      |0  |1  |2  |3  |
|------|---|---|---|---|
|0     |1.0|NaN|7  |NaN|
|1     |2.0|5.0|8  |NaN|
|2     |NaN|6.0|9  |NaN|

`thresh`-parametri antaa sinulle tarkemman hallinnan: voit asettaa rivin tai sarakkeen tarvitsemien *ei-null* arvojen määrän, jotta se säilytetään:
```python
example2.dropna(axis='rows', thresh=3)
```
```
	0	1	2	3
1	2.0	5.0	8	NaN
```
Tässä ensimmäinen ja viimeinen rivi on poistettu, koska niissä on vain kaksi ei-null-arvoa.

- **Null-arvojen täyttäminen**: Riippuen datasetistäsi, voi joskus olla järkevämpää täyttää null-arvot kelvollisilla arvoilla kuin poistaa ne. Voisit käyttää `isnull`-metodia tehdäksesi tämän paikan päällä, mutta se voi olla työlästä, erityisesti jos sinulla on paljon arvoja täytettävänä. Koska tämä on niin yleinen tehtävä data-analytiikassa, pandas tarjoaa `fillna`-metodin, joka palauttaa kopion `Series`- tai `DataFrame`-muodosta, jossa puuttuvat arvot on korvattu valitsemallasi arvolla. Luodaan toinen esimerkki `Series`-muodosta nähdäksesi, miten tämä toimii käytännössä.
```python
example3 = pd.Series([1, np.nan, 2, None, 3], index=list('abcde'))
example3
```
```
a    1.0
b    NaN
c    2.0
d    NaN
e    3.0
dtype: float64
```
Voit täyttää kaikki null-arvot yhdellä arvolla, kuten `0`:
```python
example3.fillna(0)
```
```
a    1.0
b    0.0
c    2.0
d    0.0
e    3.0
dtype: float64
```
Voit **täyttää eteenpäin** null-arvot, eli käyttää viimeistä kelvollista arvoa null-arvon täyttämiseen:
```python
example3.fillna(method='ffill')
```
```
a    1.0
b    1.0
c    2.0
d    2.0
e    3.0
dtype: float64
```
Voit myös **täyttää taaksepäin**, jolloin seuraava kelvollinen arvo täyttää null-arvon taaksepäin:
```python
example3.fillna(method='bfill')
```
```
a    1.0
b    2.0
c    2.0
d    3.0
e    3.0
dtype: float64
```
Kuten arvata saattaa, tämä toimii samalla tavalla `DataFrame`-muodossa, mutta voit myös määrittää `axis`-parametrin, jonka mukaan null-arvot täytetään. Käytetään aiemmin käytettyä `example2`-datasettiä uudelleen:
```python
example2.fillna(method='ffill', axis=1)
```
```
	0	1	2	3
0	1.0	1.0	7.0	7.0
1	2.0	5.0	8.0	8.0
2	NaN	6.0	9.0	9.0
```
Huomaa, että kun edellinen arvo ei ole saatavilla eteenpäin täyttämiseen, null-arvo jää ennalleen.
> **Pääpointti:** Puuttuvien arvojen käsittelyyn on useita tapoja. Käyttämäsi strategia (poistaminen, korvaaminen tai tapa, jolla korvaat ne) tulisi määritellä datan erityispiirteiden mukaan. Saat paremman käsityksen puuttuvien arvojen käsittelystä, kun työskentelet ja vuorovaikutat datasetien kanssa enemmän.

## Dublikaattidatan poistaminen

> **Oppimistavoite:** Tämän alajakson lopussa sinun tulisi osata tunnistaa ja poistaa dublikaattiarvot DataFrameista.

Puuttuvan datan lisäksi kohtaat usein dublikaattidataa todellisissa datasetissä. Onneksi `pandas` tarjoaa helpon tavan havaita ja poistaa dublikaattimerkinnät.

- **Dublikaattien tunnistaminen: `duplicated`**: Voit helposti havaita dublikaattiarvot käyttämällä pandas-kirjaston `duplicated`-metodia, joka palauttaa Boolean-maskin, joka osoittaa, onko `DataFrame`-merkintä aiemman merkinnän dublikaatti. Luodaan toinen esimerkkidataframe, jotta näet tämän toiminnassa.
```python
example4 = pd.DataFrame({'letters': ['A','B'] * 2 + ['B'],
                         'numbers': [1, 2, 1, 3, 3]})
example4
```
|      |kirjaimet|numerot|
|------|---------|-------|
|0     |A        |1      |
|1     |B        |2      |
|2     |A        |1      |
|3     |B        |3      |
|4     |B        |3      |

```python
example4.duplicated()
```
```
0    False
1    False
2     True
3    False
4     True
dtype: bool
```
- **Dublikaattien poistaminen: `drop_duplicates`:** palauttaa yksinkertaisesti kopion datasta, jossa kaikki `duplicated`-arvot ovat `False`:
```python
example4.drop_duplicates()
```
```
	letters	numbers
0	A	1
1	B	2
3	B	3
```
Sekä `duplicated` että `drop_duplicates` oletuksena tarkastelevat kaikkia sarakkeita, mutta voit määrittää, että ne tarkastelevat vain tiettyä sarakejoukkoa `DataFrame`-rakenteessasi:
```python
example4.drop_duplicates(['letters'])
```
```
letters	numbers
0	A	1
1	B	2
```

> **Pääpointti:** Dublikaattidatan poistaminen on olennainen osa lähes jokaista data-analytiikkaprojektia. Dublikaattidata voi muuttaa analyysiesi tuloksia ja antaa virheellisiä lopputuloksia!


## 🚀 Haaste

Kaikki käsitelty materiaali on saatavilla [Jupyter Notebook](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/2-Working-With-Data/08-data-preparation/notebook.ipynb) -tiedostona. Lisäksi jokaisen osion jälkeen on harjoituksia, kokeile niitä!

## [Luennon jälkeinen kysely](https://ff-quizzes.netlify.app/en/ds/)



## Kertaus & Itseopiskelu

On olemassa monia tapoja löytää ja lähestyä datan valmistelua analyysia ja mallinnusta varten, ja datan puhdistaminen on tärkeä vaihe, joka vaatii "kädet savessa" -kokemusta. Kokeile näitä Kaggle-haasteita tutkiaksesi tekniikoita, joita tämä oppitunti ei käsitellyt.

- [Data Cleaning Challenge: Parsing Dates](https://www.kaggle.com/rtatman/data-cleaning-challenge-parsing-dates/)

- [Data Cleaning Challenge: Scale and Normalize Data](https://www.kaggle.com/rtatman/data-cleaning-challenge-scale-and-normalize-data)


## Tehtävä

[Arvioi lomakkeen dataa](assignment.md)

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.