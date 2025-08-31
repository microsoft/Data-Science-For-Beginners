<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3ade580a06b5f04d57cc83a768a8fb77",
  "translation_date": "2025-08-31T05:41:35+00:00",
  "source_file": "2-Working-With-Data/08-data-preparation/README.md",
  "language_code": "lt"
}
-->
# Darbas su duomenimis: Duomenų paruošimas

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/08-DataPreparation.png)|
|:---:|
|Duomenų paruošimas - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

## [Prieš paskaitą: Klausimynas](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/14)

Priklausomai nuo šaltinio, neapdoroti duomenys gali turėti tam tikrų neatitikimų, kurie sukels sunkumų analizuojant ir modeliuojant. Kitaip tariant, šie duomenys gali būti laikomi „nešvariais“ ir juos reikės išvalyti. Šioje pamokoje dėmesys skiriamas duomenų valymo ir transformavimo technikoms, siekiant spręsti problemas, susijusias su trūkstamais, netiksliais ar neišsamiais duomenimis. Pamokoje aptariamos temos bus naudojamos su Python ir Pandas biblioteka ir bus [pademonstruotos užrašų knygelėje](notebook.ipynb) šiame kataloge.

## Kodėl svarbu valyti duomenis

- **Naudojimo ir pakartotinio naudojimo paprastumas**: Kai duomenys yra tinkamai organizuoti ir normalizuoti, juos lengviau ieškoti, naudoti ir dalintis su kitais.

- **Nuoseklumas**: Duomenų mokslas dažnai reikalauja dirbti su daugiau nei vienu duomenų rinkiniu, kur duomenų rinkiniai iš skirtingų šaltinių turi būti sujungti. Užtikrinus, kad kiekvienas atskiras duomenų rinkinys būtų standartizuotas, galima užtikrinti, kad sujungti duomenys išliks naudingi.

- **Modelio tikslumas**: Išvalyti duomenys pagerina modelių, kurie jais remiasi, tikslumą.

## Dažni valymo tikslai ir strategijos

- **Duomenų rinkinio tyrimas**: Duomenų tyrimas, kuris aptariamas [vėlesnėje pamokoje](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/4-Data-Science-Lifecycle/15-analyzing), gali padėti atrasti duomenis, kuriuos reikia išvalyti. Vizualiai stebint reikšmes duomenų rinkinyje galima susidaryti lūkesčius, kaip atrodys likusi dalis, arba gauti idėjų apie problemas, kurias galima išspręsti. Tyrimas gali apimti pagrindinius užklausų vykdymus, vizualizacijas ir pavyzdžių analizę.

- **Formatavimas**: Priklausomai nuo šaltinio, duomenys gali būti pateikti nenuosekliai. Tai gali sukelti problemų ieškant ir atvaizduojant reikšmes, kai jos matomos duomenų rinkinyje, bet nėra tinkamai pateiktos vizualizacijose ar užklausų rezultatuose. Dažnos formatavimo problemos apima tarpus, datas ir duomenų tipus. Formatavimo problemų sprendimas paprastai priklauso nuo žmonių, kurie naudoja duomenis. Pavyzdžiui, standartai, kaip pateikiamos datos ir skaičiai, gali skirtis priklausomai nuo šalies.

- **Dubliavimas**: Duomenys, kurie pasikartoja, gali sukelti netikslius rezultatus ir dažniausiai turėtų būti pašalinti. Tai dažnai pasitaiko, kai sujungiami du ar daugiau duomenų rinkinių. Tačiau yra atvejų, kai dubliuoti duomenys sujungtuose rinkiniuose gali turėti papildomos informacijos ir juos gali reikėti išsaugoti.

- **Trūkstami duomenys**: Trūkstami duomenys gali sukelti netikslumus, taip pat silpnus ar šališkus rezultatus. Kartais tai galima išspręsti „pakartotinai įkeliant“ duomenis, užpildant trūkstamas reikšmes skaičiavimais ir kodu, pavyzdžiui, Python, arba tiesiog pašalinant reikšmę ir atitinkamus duomenis. Yra daugybė priežasčių, kodėl duomenys gali būti trūkstami, o veiksmai, kurių imamasi siekiant išspręsti šias problemas, gali priklausyti nuo to, kaip ir kodėl jie dingo.

## Duomenų rėmelio informacijos tyrimas
> **Mokymosi tikslas:** Šios dalies pabaigoje turėtumėte jaustis patogiai ieškodami bendros informacijos apie pandas DataFrame saugomus duomenis.

Kai duomenys įkeliami į pandas, jie greičiausiai bus DataFrame formatu (žr. ankstesnę [pamoką](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/2-Working-With-Data/07-python#dataframe) dėl išsamesnės apžvalgos). Tačiau jei jūsų DataFrame turi 60 000 eilučių ir 400 stulpelių, nuo ko pradėti suprasti, su kuo dirbate? Laimei, [pandas](https://pandas.pydata.org/) suteikia patogius įrankius greitai peržiūrėti bendrą informaciją apie DataFrame, taip pat pirmąsias ir paskutines eilutes.

Norėdami ištirti šią funkciją, importuosime Python scikit-learn biblioteką ir naudosime ikonišką duomenų rinkinį: **Iris duomenų rinkinį**.

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

- **DataFrame.info**: Pradžiai, `info()` metodas naudojamas norint atspausdinti santrauką apie `DataFrame` turinį. Pažiūrėkime į šį duomenų rinkinį:
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
Iš to sužinome, kad *Iris* duomenų rinkinys turi 150 įrašų keturiuose stulpeliuose be jokių tuščių įrašų. Visi duomenys saugomi kaip 64 bitų slankiojo kablelio skaičiai.

- **DataFrame.head()**: Toliau, norėdami patikrinti faktinį `DataFrame` turinį, naudojame `head()` metodą. Pažiūrėkime, kaip atrodo pirmosios kelios mūsų `iris_df` eilutės:
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
- **DataFrame.tail()**: Priešingai, norėdami patikrinti paskutines kelias `DataFrame` eilutes, naudojame `tail()` metodą:
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
> **Išvada:** Net ir žiūrėdami tik į metaduomenis apie informaciją `DataFrame` arba pirmąsias ir paskutines kelias reikšmes, galite iš karto susidaryti idėją apie duomenų dydį, formą ir turinį.

## Darbas su trūkstamais duomenimis
> **Mokymosi tikslas:** Šios dalies pabaigoje turėtumėte žinoti, kaip pakeisti arba pašalinti null reikšmes iš DataFrame.

Dažniausiai duomenų rinkiniai, kuriuos norite naudoti (arba privalote naudoti), turi trūkstamų reikšmių. Kaip tvarkomi trūkstami duomenys, turi subtilių kompromisų, kurie gali paveikti jūsų galutinę analizę ir realaus pasaulio rezultatus.

Pandas tvarko trūkstamas reikšmes dviem būdais. Pirmasis, kurį jau matėte ankstesnėse dalyse: `NaN`, arba Not a Number. Tai yra speciali reikšmė, kuri yra IEEE slankiojo kablelio specifikacijos dalis ir naudojama tik trūkstamoms slankiojo kablelio reikšmėms nurodyti.

Kitiems nei slankiojo kablelio trūkstamiems duomenims pandas naudoja Python `None` objektą. Nors gali atrodyti painu, kad susidursite su dviem skirtingomis reikšmėmis, kurios iš esmės reiškia tą patį, yra pagrįstų programinių priežasčių šiam dizaino pasirinkimui, o praktikoje tai leidžia pandas pateikti gerą kompromisą daugumai atvejų. Nepaisant to, tiek `None`, tiek `NaN` turi apribojimų, kuriuos reikia žinoti, kaip jie gali būti naudojami.

Daugiau apie `NaN` ir `None` galite sužinoti iš [užrašų knygelės](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/4-Data-Science-Lifecycle/15-analyzing/notebook.ipynb)!

- **Null reikšmių aptikimas**: Pandas `isnull()` ir `notnull()` metodai yra pagrindiniai metodai null duomenims aptikti. Abu grąžina Boole'o kaukes jūsų duomenims. Naudosime `numpy` `NaN` reikšmėms:
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
Atidžiai pažiūrėkite į išvestį. Ar kas nors jus nustebino? Nors `0` yra aritmetinis null, jis vis tiek yra tinkamas sveikasis skaičius ir pandas jį taip traktuoja. `''` yra šiek tiek subtilesnis. Nors jį naudojome 1 skyriuje kaip tuščios eilutės reikšmę, jis vis tiek yra eilutės objektas ir pandas nelaiko jo null reikšme.

Dabar apverskime tai ir naudokime šiuos metodus taip, kaip dažniausiai juos naudosite praktikoje. Boole'o kaukes galite naudoti tiesiogiai kaip ``Series`` arba ``DataFrame`` indeksą, kuris gali būti naudingas dirbant su atskirai trūkstamomis (arba esančiomis) reikšmėmis.

> **Išvada**: Tiek `isnull()`, tiek `notnull()` metodai duoda panašius rezultatus, kai juos naudojate `DataFrame`: jie rodo rezultatus ir tų rezultatų indeksą, kas jums labai padės dirbant su duomenimis.

- **Null reikšmių pašalinimas**: Be trūkstamų reikšmių identifikavimo, pandas suteikia patogų būdą pašalinti null reikšmes iš `Series` ir `DataFrame`. (Ypač dideliuose duomenų rinkiniuose dažnai patartina tiesiog pašalinti trūkstamas [NA] reikšmes iš analizės, o ne tvarkyti jas kitais būdais.) Norėdami tai pamatyti veiksmuose, grįžkime prie `example1`:
```python
example1 = example1.dropna()
example1
```
```
0    0
2     
dtype: object
```
Atkreipkite dėmesį, kad tai turėtų atrodyti kaip jūsų išvestis iš `example3[example3.notnull()]`. Skirtumas tas, kad vietoj to, kad būtų indeksuojamos kaukės reikšmės, `dropna` pašalino tas trūkstamas reikšmes iš `Series` `example1`.

Kadangi `DataFrame` turi dvi dimensijas, jie suteikia daugiau galimybių duomenims pašalinti.

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

(Ar pastebėjote, kad pandas pakeitė du stulpelius į slankiojo kablelio tipus, kad atitiktų `NaN`?)

Negalite pašalinti vienos reikšmės iš `DataFrame`, todėl turite pašalinti visas eilutes arba stulpelius. Priklausomai nuo to, ką darote, galite norėti daryti vieną ar kitą, todėl pandas suteikia galimybes abiem. Kadangi duomenų moksle stulpeliai paprastai atspindi kintamuosius, o eilutės - stebėjimus, dažniau pašalinsite duomenų eilutes; numatytasis `dropna()` nustatymas yra pašalinti visas eilutes, kuriose yra bet kokių null reikšmių:

```python
example2.dropna()
```
```
	0	1	2
1	2.0	5.0	8
```
Jei reikia, galite pašalinti NA reikšmes iš stulpelių. Naudokite `axis=1`, kad tai padarytumėte:
```python
example2.dropna(axis='columns')
```
```
	2
0	7
1	8
2	9
```
Atkreipkite dėmesį, kad tai gali pašalinti daug duomenų, kuriuos galbūt norėtumėte išsaugoti, ypač mažesniuose duomenų rinkiniuose. O kas, jei norite pašalinti tik tas eilutes ar stulpelius, kuriuose yra kelios arba net visos null reikšmės? Šiuos nustatymus galite nurodyti `dropna` naudodami `how` ir `thresh` parametrus.

Pagal numatytuosius nustatymus `how='any'` (jei norite patikrinti patys arba pamatyti, kokius kitus parametrus turi metodas, paleiskite `example4.dropna?` kodo langelyje). Galėtumėte alternatyviai nurodyti `how='all'`, kad pašalintumėte tik tas eilutes ar stulpelius, kuriuose yra visos null reikšmės. Išplėskime mūsų pavyzdinį `DataFrame`, kad pamatytume tai veiksmuose.

```python
example2[3] = np.nan
example2
```
|      |0  |1  |2  |3  |
|------|---|---|---|---|
|0     |1.0|NaN|7  |NaN|
|1     |2.0|5.0|8  |NaN|
|2     |NaN|6.0|9  |NaN|

`Thresh` parametras suteikia jums smulkesnę kontrolę: nustatote *ne-null* reikšmių skaičių, kurį eilutė arba stulpelis turi turėti, kad būtų išsaugotas:
```python
example2.dropna(axis='rows', thresh=3)
```
```
	0	1	2	3
1	2.0	5.0	8	NaN
```
Čia pirmoji ir paskutinė eilutės buvo pašalintos, nes jose yra tik dvi ne-null reikšmės.

- **Null reikšmių užpildymas**: Priklausomai nuo jūsų duomenų rinkinio, kartais gali būti prasmingiau užpildyti null reikšmes galiojančiomis, o ne jas pašalinti. Galėtumėte naudoti `isnull`, kad tai padarytumėte vietoje, tačiau tai gali būti varginantis darbas, ypač jei turite daug reikšmių, kurias reikia užpildyti. Kadangi tai yra tokia dažna užduotis duomenų moksle, pandas suteikia `fillna`, kuris grąžina `Series` arba `DataFrame` kopiją su trūkstamomis reikšmėmis, pakeistomis jūsų pasirinkta reikšme. Sukurkime dar vieną pavyzdinį `Series`, kad pamatytume, kaip tai veikia praktikoje.
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
Galite užpildyti visas null reikšmes viena reikšme, pavyzdžiui, `0`:
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
Galite **užpildyti pirmyn** null reikšmes, naudodami paskutinę galiojančią reikšmę null reikšmei užpildyti:
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
Taip pat galite **užpildyti atgal**, kad užpildytumėte null reikšmę naudodami kitą galiojančią reikšmę:
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
Kaip galite spėti, tai veikia taip pat su `DataFrame`, tačiau taip pat galite nurodyti `axis`, pagal kurį užpildyti null reikšmes. Naudojant anksčiau naudotą `example2`:
```python
example2.fillna(method='ffill', axis=1)
```
```
	0	1	2	3
0	1.0	1.0	7.0	7.0
1	2.0	5.0	8.0	8.0
2	NaN	6.0	9.0	9.0
```
Atkreipkite dėmesį, kad kai ankstesnė reikšmė nėra prieinama užpildymui pirmyn, null reikšmė lieka.
> **Svarbiausia:** Yra daugybė būdų, kaip spręsti trūkstamų reikšmių problemą jūsų duomenų rinkiniuose. Konkreti strategija, kurią pasirinksite (pašalinti, pakeisti ar net kaip pakeisti), turėtų būti diktuojama konkrečių duomenų ypatumų. Kuo daugiau dirbsite su duomenų rinkiniais, tuo geriau suprasite, kaip tvarkyti trūkstamas reikšmes.

## Dublikatų duomenų pašalinimas

> **Mokymosi tikslas:** Šios poskyrio pabaigoje turėtumėte jaustis užtikrintai identifikuodami ir pašalindami pasikartojančias reikšmes iš `DataFrame`.

Be trūkstamų duomenų, realiuose duomenų rinkiniuose dažnai susidursite su pasikartojančiais duomenimis. Laimei, `pandas` suteikia paprastą būdą aptikti ir pašalinti pasikartojančias įrašus.

- **Dublikatų identifikavimas: `duplicated`**: Pasikartojančias reikšmes galite lengvai aptikti naudodami `duplicated` metodą `pandas`, kuris grąžina loginę kaukę, nurodančią, ar įrašas `DataFrame` yra ankstesnio įrašo dublikatas. Sukurkime dar vieną pavyzdinį `DataFrame`, kad pamatytume, kaip tai veikia.
```python
example4 = pd.DataFrame({'letters': ['A','B'] * 2 + ['B'],
                         'numbers': [1, 2, 1, 3, 3]})
example4
```
|      |letters|numbers|
|------|-------|-------|
|0     |A      |1      |
|1     |B      |2      |
|2     |A      |1      |
|3     |B      |3      |
|4     |B      |3      |

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
- **Dublikatų pašalinimas: `drop_duplicates`:** paprasčiausiai grąžina duomenų kopiją, kurioje visos `duplicated` reikšmės yra `False`:
```python
example4.drop_duplicates()
```
```
	letters	numbers
0	A	1
1	B	2
3	B	3
```
Tiek `duplicated`, tiek `drop_duplicates` pagal numatytuosius nustatymus atsižvelgia į visas stulpelius, tačiau galite nurodyti, kad jie analizuotų tik tam tikrą `DataFrame` stulpelių dalį:
```python
example4.drop_duplicates(['letters'])
```
```
letters	numbers
0	A	1
1	B	2
```

> **Svarbiausia:** Pasikartojančių duomenų pašalinimas yra būtina beveik kiekvieno duomenų mokslo projekto dalis. Pasikartojantys duomenys gali pakeisti jūsų analizės rezultatus ir pateikti netikslius rezultatus!


## 🚀 Iššūkis

Visos aptartos medžiagos pateikiamos kaip [Jupyter Notebook](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/2-Working-With-Data/08-data-preparation/notebook.ipynb). Be to, po kiekvieno skyriaus yra pratimai – išbandykite juos!

## [Po paskaitos testas](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/15)



## Apžvalga ir savarankiškas mokymasis

Yra daugybė būdų, kaip atrasti ir pasiruošti duomenų analizavimui bei modeliavimui, o duomenų valymas yra svarbus žingsnis, reikalaujantis praktinio darbo. Išbandykite šiuos Kaggle iššūkius, kad susipažintumėte su technikomis, kurios nebuvo aptartos šioje pamokoje.

- [Duomenų valymo iššūkis: Datų analizė](https://www.kaggle.com/rtatman/data-cleaning-challenge-parsing-dates/)

- [Duomenų valymo iššūkis: Duomenų mastelio keitimas ir normalizavimas](https://www.kaggle.com/rtatman/data-cleaning-challenge-scale-and-normalize-data)


## Užduotis

[Duomenų vertinimas iš formos](assignment.md)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, atkreipkite dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus aiškinimus, kylančius dėl šio vertimo naudojimo.