<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1b560955ff39a2bcf2a049fce474a951",
  "translation_date": "2025-09-05T22:38:43+00:00",
  "source_file": "2-Working-With-Data/08-data-preparation/README.md",
  "language_code": "fi"
}
-->
# Työskentely datan kanssa: Datan valmistelu

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/08-DataPreparation.png)|
|:---:|
|Datan valmistelu - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

## [Esiluentakysely](https://ff-quizzes.netlify.app/en/ds/quiz/14)

Riippuen datan lähteestä, raakadatan mukana voi tulla epäjohdonmukaisuuksia, jotka aiheuttavat haasteita analyysissä ja mallinnuksessa. Toisin sanoen, tämä data voidaan luokitella "likaiseksi" ja se täytyy puhdistaa. Tämä oppitunti keskittyy tekniikoihin, joilla dataa puhdistetaan ja muokataan käsittelemään puuttuvaa, epätarkkaa tai epätäydellistä dataa. Oppitunnin aiheet hyödyntävät Pythonia ja Pandas-kirjastoa, ja ne [havainnollistetaan muistikirjassa](../../../../2-Working-With-Data/08-data-preparation/notebook.ipynb) tässä hakemistossa.

## Datan puhdistamisen tärkeys

- **Helppokäyttöisyys ja uudelleenkäyttö**: Kun data on asianmukaisesti järjestetty ja normalisoitu, sitä on helpompi etsiä, käyttää ja jakaa muiden kanssa.

- **Johdonmukaisuus**: Data-analyysi vaatii usein työskentelyä useamman datasetin kanssa, jolloin eri lähteistä tulevat datasetit täytyy yhdistää. Varmistamalla, että jokainen datasetti noudattaa yhteisiä standardeja, varmistetaan, että data on edelleen hyödyllistä, kun ne yhdistetään yhdeksi datasetiksi.

- **Mallien tarkkuus**: Puhdistettu data parantaa mallien tarkkuutta, jotka ovat riippuvaisia siitä.

## Yleiset puhdistustavoitteet ja -strategiat

- **Datasetin tutkiminen**: Datan tutkiminen, joka käsitellään [myöhemmässä oppitunnissa](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/4-Data-Science-Lifecycle/15-analyzing), voi auttaa löytämään dataa, joka täytyy puhdistaa. Datasetin arvojen visuaalinen tarkastelu voi luoda odotuksia siitä, miltä loput datasta näyttävät, tai antaa käsityksen ongelmista, jotka voidaan ratkaista. Tutkiminen voi sisältää peruskyselyitä, visualisointeja ja otantaa.

- **Muotoilu**: Riippuen lähteestä, datassa voi olla epäjohdonmukaisuuksia sen esitystavassa. Tämä voi aiheuttaa ongelmia arvon etsimisessä ja esittämisessä, jolloin arvo näkyy datasetissä, mutta sitä ei esitetä oikein visualisoinneissa tai kyselytuloksissa. Yleisiä muotoiluongelmia ovat välilyöntien, päivämäärien ja datatyypin korjaaminen. Muotoiluongelmien ratkaiseminen on yleensä datan käyttäjien vastuulla. Esimerkiksi päivämäärien ja numeroiden esitystavat voivat vaihdella maittain.

- **Duplikaatit**: Data, jossa on useampi esiintymä, voi tuottaa epätarkkoja tuloksia ja se tulisi yleensä poistaa. Tämä on yleistä, kun yhdistetään kaksi tai useampia datasettejä. On kuitenkin tilanteita, joissa yhdistetyissä dataseteissä olevat duplikaatit sisältävät lisätietoa ja ne täytyy säilyttää.

- **Puuttuva data**: Puuttuva data voi aiheuttaa epätarkkuuksia sekä heikkoja tai puolueellisia tuloksia. Joskus nämä voidaan ratkaista "uudelleenlataamalla" data, täyttämällä puuttuvat arvot laskennalla ja koodilla, kuten Pythonilla, tai yksinkertaisesti poistamalla arvo ja siihen liittyvä data. Puuttuvan datan syyt voivat vaihdella, ja toimenpiteet sen ratkaisemiseksi riippuvat siitä, miten ja miksi data on alun perin puuttunut.

## DataFramen tietojen tutkiminen
> **Oppimistavoite:** Tämän osion lopussa sinun tulisi osata löytää yleistä tietoa pandas DataFrameihin tallennetusta datasta.

Kun olet ladannut datasi pandas-kirjastoon, se on todennäköisesti DataFrame-muodossa (katso edellinen [oppitunti](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/2-Working-With-Data/07-python#dataframe) saadaksesi yksityiskohtaisen yleiskatsauksen). Mutta jos DataFramessa on 60 000 riviä ja 400 saraketta, mistä edes aloitat ymmärtääksesi, mitä sinulla on käsissäsi? Onneksi [pandas](https://pandas.pydata.org/) tarjoaa käteviä työkaluja, joilla voit nopeasti tarkastella DataFramen yleistä tietoa sekä sen ensimmäisiä ja viimeisiä rivejä.

Tämän toiminnallisuuden tutkimiseksi tuomme käyttöön Pythonin scikit-learn-kirjaston ja käytämme ikonista datasettiä: **Iris-datasettiä**.

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
Tästä tiedämme, että *Iris*-datasetissä on 150 riviä neljässä sarakkeessa, eikä siinä ole puuttuvia arvoja. Kaikki data on tallennettu 64-bittisinä liukulukuarvoina.

- **DataFrame.head()**: Seuraavaksi tarkastellaan `DataFrame`-sisällön ensimmäisiä rivejä `head()`-metodilla. Katsotaanpa, miltä `iris_df`:n ensimmäiset rivit näyttävät:
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
- **DataFrame.tail()**: Vastaavasti tarkastellaan `DataFrame`-sisällön viimeisiä rivejä `tail()`-metodilla:
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
> **Yhteenveto:** Jo pelkästään tarkastelemalla DataFramen metatietoja tai sen ensimmäisiä ja viimeisiä rivejä, voit saada välittömän käsityksen datan koosta, muodosta ja sisällöstä.

## Puuttuvan datan käsittely
> **Oppimistavoite:** Tämän osion lopussa sinun tulisi osata korvata tai poistaa puuttuvat arvot DataFrameista.

Useimmiten datasetit, joita haluat käyttää (tai joudut käyttämään), sisältävät puuttuvia arvoja. Puuttuvan datan käsittelyyn liittyy hienovaraisia kompromisseja, jotka voivat vaikuttaa lopulliseen analyysiin ja todellisiin tuloksiin.

Pandas käsittelee puuttuvia arvoja kahdella tavalla. Ensimmäinen, jonka olet nähnyt aiemmissa osioissa, on `NaN` (Not a Number). Tämä on erityinen arvo, joka on osa IEEE:n liukulukumääritystä, ja sitä käytetään vain puuttuvien liukulukuarvojen merkitsemiseen.

Muiden kuin liukulukujen puuttuvien arvojen kohdalla pandas käyttää Pythonin `None`-objektia. Vaikka voi tuntua hämmentävältä, että kohtaat kaksi erilaista arvoa, jotka tarkoittavat käytännössä samaa asiaa, tälle suunnitteluratkaisulle on hyvät ohjelmalliset syyt. Käytännössä tämä lähestymistapa mahdollistaa sen, että pandas tarjoaa hyvän kompromissin suurimmassa osassa tapauksia. Tästä huolimatta sekä `None` että `NaN` sisältävät rajoituksia, jotka sinun on hyvä tiedostaa niiden käyttöä koskien.

Lue lisää `NaN`- ja `None`-arvoista [muistikirjasta](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/4-Data-Science-Lifecycle/15-analyzing/notebook.ipynb)!

- **Puuttuvien arvojen tunnistaminen**: Pandasissa `isnull()`- ja `notnull()`-metodit ovat ensisijaisia tapoja tunnistaa puuttuva data. Molemmat palauttavat Boolean-maskit datan päälle. Käytämme `numpy`-kirjastoa `NaN`-arvojen kanssa:
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
Katso tarkasti tulostetta. Yllättääkö jokin? Vaikka `0` on aritmeettisesti nolla, se on silti täysin kelvollinen kokonaisluku, ja pandas käsittelee sen sellaisena. `''` on hieman hienovaraisempi. Vaikka käytimme sitä osassa 1 tyhjänä merkkijonona, se on silti merkkijono-objekti eikä pandasissa null-arvon esitys.

Nyt käännetään tämä toisinpäin ja käytetään näitä metodeja tavalla, jolla niitä käytetään käytännössä. Voit käyttää Boolean-maskeja suoraan ``Series``- tai ``DataFrame``-indeksinä, mikä on hyödyllistä, kun yrität työskennellä eristettyjen puuttuvien (tai olemassa olevien) arvojen kanssa.

> **Yhteenveto**: Sekä `isnull()`- että `notnull()`-metodit tuottavat samankaltaisia tuloksia, kun käytät niitä `DataFrame`-objekteissa: ne näyttävät tulokset ja niiden indeksit, mikä auttaa sinua valtavasti datan käsittelyssä.

- **Puuttuvien arvojen poistaminen**: Puuttuvien arvojen tunnistamisen lisäksi pandas tarjoaa kätevän tavan poistaa puuttuvat arvot `Series`- ja `DataFrame`-objekteista. (Erityisesti suurissa dataseteissä on usein suositeltavampaa yksinkertaisesti poistaa puuttuvat [NA] arvot analyysistä kuin käsitellä niitä muilla tavoilla.) Katsotaanpa tätä toiminnallisuutta `example1`-datasetillä:
```python
example1 = example1.dropna()
example1
```
```
0    0
2     
dtype: object
```
Huomaa, että tämä näyttää samalta kuin tulosteesi `example3[example3.notnull()]`. Erona on, että `dropna` on poistanut puuttuvat arvot `Series`-objektista `example1` sen sijaan, että vain indeksoisi maskattuja arvoja.

Koska `DataFrame`-objekteilla on kaksi ulottuvuutta, ne tarjoavat enemmän vaihtoehtoja datan poistamiseen.

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

(Huomasitko, että pandas muutti kaksi saraketta liukuluvuiksi mukautuakseen `NaN`-arvoihin?)

Et voi poistaa yksittäistä arvoa `DataFrame`-objektista, joten sinun täytyy poistaa kokonaisia rivejä tai sarakkeita. Riippuen siitä, mitä olet tekemässä, saatat haluta tehdä jomman kumman, ja pandas antaa sinulle vaihtoehdot molempiin. Koska data-analyysissä sarakkeet edustavat yleensä muuttujia ja rivit havaintoja, olet todennäköisemmin poistamassa rivejä; `dropna()`-metodin oletusasetuksena on poistaa kaikki rivit, jotka sisältävät minkä tahansa puuttuvan arvon:

```python
example2.dropna()
```
```
	0	1	2
1	2.0	5.0	8
```
Jos tarpeen, voit poistaa NA-arvot sarakkeista. Käytä `axis=1` tehdäksesi niin:
```python
example2.dropna(axis='columns')
```
```
	2
0	7
1	8
2	9
```
Huomaa, että tämä voi poistaa paljon dataa, jonka haluaisit säilyttää, erityisesti pienemmissä dataseteissä. Entä jos haluat poistaa vain rivit tai sarakkeet, jotka sisältävät useita tai jopa kaikki puuttuvat arvot? Voit määrittää nämä asetukset `dropna`-metodissa `how`- ja `thresh`-parametreilla.

Oletuksena `how='any'` (jos haluat tarkistaa itse tai nähdä, mitä muita parametreja metodilla on, suorita `example4.dropna?` koodisolussa). Voit vaihtoehtoisesti määrittää `how='all'`, jolloin poistetaan vain rivit tai sarakkeet, jotka sisältävät kaikki puuttuvat arvot. Laajennetaan esimerkkimme `DataFrame`-objektia nähdäksesi tämä toiminnassa.

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

- **Puuttuvien arvojen täyttäminen**: Riippuen datasetistäsi, voi joskus olla järkevämpää täyttää puuttuvat arvot kelvollisilla arvoilla kuin poistaa ne. Voisit käyttää `isnull`-metodia tehdäksesi tämän paikan päällä, mutta se voi olla työlästä, erityisesti jos täytettäviä arvoja on paljon. Koska tämä on niin yleinen tehtävä data-analyysissä, pandas tarjoaa `fillna`-metodin, joka palauttaa kopion `Series`- tai `DataFrame`-objektista, jossa puuttuvat arvot on korvattu valitsemallasi arvolla. Luodaan toinen esimerkki `Series`-objekti nähdäksesi, miten tämä toimii käytännössä.
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
Voit täyttää kaikki puuttuvat arvot yhdellä arvolla, kuten `0`:
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
Voit **täyttää eteenpäin** puuttuvat arvot, eli käyttää edellistä kelvollista arvoa täyttämään puuttuvan:
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
Voit myös **täyttää taaksepäin**, jolloin seuraava kelvollinen arvo täyttää puuttuvan:
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
Kuten arvata saattaa, tämä toimii samalla tavalla `DataFrame`-objekteissa, mutta voit myös määrittää `axis`-parametrin, jonka mukaan puuttuvat arvot täytetään. Käytetään aiemmin käytettyä `example2`-datasettiä uudelleen:
```python
example2.fillna(method='ffill', axis=1)
```
```
	0	1	2	3
0	1.0	1.0	7.0	7.0
1	2.0	5.0	8.0	8.0
2	NaN	6.0	9.0	9.0
```
Huomaa, että kun edellistä arvoa ei ole saatavilla eteenpäin täyttämiseen, puuttuva arvo jää ennalleen.
> **Tärkeää:** Puuttuvien arvojen käsittelyyn datassa on useita tapoja. Käyttämäsi strategia (poistaminen, korvaaminen tai tapa, jolla korvaat ne) tulisi määritellä datan erityispiirteiden mukaan. Saat paremman käsityksen puuttuvien arvojen käsittelystä, kun työskentelet ja vuorovaikutat datasetien kanssa enemmän.
## Poistetaan päällekkäiset tiedot

> **Oppimistavoite:** Tämän osion lopussa sinun tulisi osata tunnistaa ja poistaa päällekkäiset arvot DataFrameista.

Puuttuvien tietojen lisäksi todellisissa tietoaineistoissa törmäät usein myös päällekkäisiin tietoihin. Onneksi `pandas` tarjoaa helpon tavan havaita ja poistaa päällekkäiset merkinnät.

- **Päällekkäisten tunnistaminen: `duplicated`**: Voit helposti havaita päällekkäiset arvot käyttämällä pandas-kirjaston `duplicated`-metodia, joka palauttaa Boolean-maskin, joka osoittaa, onko `DataFrame`-merkintä päällekkäinen aiemman kanssa. Luodaan toinen esimerkkidataframe tämän havainnollistamiseksi.
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
- **Päällekkäisten poistaminen: `drop_duplicates`:** palauttaa yksinkertaisesti kopion datasta, jossa kaikki `duplicated`-arvot ovat `False`:
```python
example4.drop_duplicates()
```
```
	letters	numbers
0	A	1
1	B	2
3	B	3
```
Sekä `duplicated` että `drop_duplicates` oletuksena tarkastelevat kaikkia sarakkeita, mutta voit määrittää, että ne tarkastelevat vain tiettyä sarakejoukkoa `DataFrame`-objektissasi:
```python
example4.drop_duplicates(['letters'])
```
```
letters	numbers
0	A	1
1	B	2
```

> **Yhteenveto:** Päällekkäisten tietojen poistaminen on olennainen osa lähes jokaista data-analytiikkaprojektia. Päällekkäiset tiedot voivat vääristää analyysiesi tuloksia ja antaa epätarkkoja tuloksia!


## 🚀 Haaste

Kaikki käsitelty materiaali on saatavilla [Jupyter Notebook](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/2-Working-With-Data/08-data-preparation/notebook.ipynb) -tiedostona. Lisäksi jokaisen osion jälkeen on harjoituksia – kokeile niitä!

## [Luentojälkeinen kysely](https://ff-quizzes.netlify.app/en/ds/quiz/15)



## Kertaus ja itseopiskelu

On olemassa monia tapoja löytää ja lähestyä datan valmistelua analysointia ja mallinnusta varten, ja datan puhdistaminen on tärkeä vaihe, joka vaatii "käytännön" kokemusta. Kokeile näitä Kaggle-haasteita tutustuaksesi tekniikoihin, joita tämä oppitunti ei käsitellyt.

- [Data Cleaning Challenge: Parsing Dates](https://www.kaggle.com/rtatman/data-cleaning-challenge-parsing-dates/)

- [Data Cleaning Challenge: Scale and Normalize Data](https://www.kaggle.com/rtatman/data-cleaning-challenge-scale-and-normalize-data)


## Tehtävä

[Arvioidaan lomakkeen tietoja](assignment.md)

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulee pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskääntämistä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.