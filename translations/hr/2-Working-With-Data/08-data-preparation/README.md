<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3ade580a06b5f04d57cc83a768a8fb77",
  "translation_date": "2025-08-30T18:16:21+00:00",
  "source_file": "2-Working-With-Data/08-data-preparation/README.md",
  "language_code": "hr"
}
-->
# Rad s podacima: Priprema podataka

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/08-DataPreparation.png)|
|:---:|
|Priprema podataka - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

## [Pre-Lecture Quiz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/14)

Ovisno o izvoru, sirovi podaci mogu sadržavati neke nedosljednosti koje će uzrokovati poteškoće u analizi i modeliranju. Drugim riječima, ti podaci mogu biti kategorizirani kao "nečisti" i potrebno ih je očistiti. Ova lekcija fokusira se na tehnike čišćenja i transformacije podataka kako bi se riješili problemi s nedostajućim, netočnim ili nepotpunim podacima. Teme obrađene u ovoj lekciji koriste Python i biblioteku Pandas te će biti [prikazane u bilježnici](notebook.ipynb) unutar ovog direktorija.

## Važnost čišćenja podataka

- **Jednostavnost korištenja i ponovne upotrebe**: Kada su podaci pravilno organizirani i normalizirani, lakše ih je pretraživati, koristiti i dijeliti s drugima.

- **Dosljednost**: Znanost o podacima često zahtijeva rad s više skupova podataka, gdje se skupovi podataka iz različitih izvora moraju spojiti. Osiguravanje da svaki pojedini skup podataka ima zajedničku standardizaciju osigurava da podaci ostanu korisni kada se svi spoje u jedan skup podataka.

- **Točnost modela**: Očišćeni podaci poboljšavaju točnost modela koji se na njih oslanjaju.

## Uobičajeni ciljevi i strategije čišćenja

- **Istraživanje skupa podataka**: Istraživanje podataka, koje je obrađeno u [kasnijoj lekciji](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/4-Data-Science-Lifecycle/15-analyzing), može vam pomoći otkriti podatke koje treba očistiti. Vizualno promatranje vrijednosti unutar skupa podataka može postaviti očekivanja o tome kako ostatak izgleda ili pružiti ideju o problemima koje treba riješiti. Istraživanje može uključivati osnovne upite, vizualizacije i uzorkovanje.

- **Formatiranje**: Ovisno o izvoru, podaci mogu imati nedosljednosti u načinu na koji su predstavljeni. To može uzrokovati probleme u pretraživanju i prikazivanju vrijednosti, gdje se vidi unutar skupa podataka, ali nije pravilno prikazano u vizualizacijama ili rezultatima upita. Uobičajeni problemi s formatiranjem uključuju rješavanje razmaka, datuma i tipova podataka. Rješavanje problema s formatiranjem obično je odgovornost korisnika podataka. Na primjer, standardi o tome kako se datumi i brojevi prikazuju mogu se razlikovati od zemlje do zemlje.

- **Duplikati**: Podaci koji se pojavljuju više puta mogu proizvesti netočne rezultate i obično ih treba ukloniti. Ovo je česta pojava kada se spajaju dva ili više skupa podataka. Međutim, postoje slučajevi kada duplikati u spojenim skupovima podataka sadrže dijelove koji mogu pružiti dodatne informacije i možda ih treba sačuvati.

- **Nedostajući podaci**: Nedostajući podaci mogu uzrokovati netočnosti, kao i slabe ili pristrane rezultate. Ponekad se to može riješiti "ponovnim učitavanjem" podataka, popunjavanjem nedostajućih vrijednosti pomoću izračuna i koda poput Pythona ili jednostavno uklanjanjem vrijednosti i pripadajućih podataka. Postoji mnogo razloga zašto podaci mogu nedostajati, a radnje koje se poduzimaju za rješavanje tih nedostajućih vrijednosti mogu ovisiti o tome kako i zašto su nestali.

## Istraživanje informacija o DataFrameu
> **Cilj učenja:** Na kraju ovog pododjeljka trebali biste biti ugodni u pronalaženju općih informacija o podacima pohranjenim u pandas DataFrameovima.

Kada učitate svoje podatke u pandas, oni će najvjerojatnije biti u DataFrameu (pogledajte prethodnu [lekciju](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/2-Working-With-Data/07-python#dataframe) za detaljan pregled). Međutim, ako skup podataka u vašem DataFrameu ima 60.000 redaka i 400 stupaca, kako uopće početi dobivati osjećaj za ono s čime radite? Srećom, [pandas](https://pandas.pydata.org/) pruža neke praktične alate za brzo pregledavanje općih informacija o DataFrameu, uz prve i posljednje retke.

Kako bismo istražili ovu funkcionalnost, uvest ćemo Python biblioteku scikit-learn i koristiti poznati skup podataka: **Iris dataset**.

```python
import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()
iris_df = pd.DataFrame(data=iris['data'], columns=iris['feature_names'])
```
|                                        |dužina čaške (cm)|širina čaške (cm)|dužina latice (cm)|širina latice (cm)|
|----------------------------------------|-----------------|-----------------|------------------|------------------|
|0                                       |5.1              |3.5              |1.4               |0.2               |
|1                                       |4.9              |3.0              |1.4               |0.2               |
|2                                       |4.7              |3.2              |1.3               |0.2               |
|3                                       |4.6              |3.1              |1.5               |0.2               |
|4                                       |5.0              |3.6              |1.4               |0.2               |

- **DataFrame.info**: Za početak, metoda `info()` koristi se za ispis sažetka sadržaja prisutnog u `DataFrameu`. Pogledajmo ovaj skup podataka kako bismo vidjeli što imamo:
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
Iz ovoga znamo da *Iris* skup podataka ima 150 unosa u četiri stupca bez null unosa. Svi podaci pohranjeni su kao 64-bitni brojevi s pomičnim zarezom.

- **DataFrame.head()**: Zatim, kako bismo provjerili stvarni sadržaj `DataFramea`, koristimo metodu `head()`. Pogledajmo kako izgledaju prvih nekoliko redaka našeg `iris_df`:
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
- **DataFrame.tail()**: Suprotno tome, kako bismo provjerili posljednjih nekoliko redaka `DataFramea`, koristimo metodu `tail()`:
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
> **Zaključak:** Već samo promatranjem metapodataka o informacijama u DataFrameu ili prvih i posljednjih nekoliko vrijednosti u njemu, možete odmah dobiti ideju o veličini, obliku i sadržaju podataka s kojima radite.

## Rješavanje nedostajućih podataka
> **Cilj učenja:** Na kraju ovog pododjeljka trebali biste znati kako zamijeniti ili ukloniti null vrijednosti iz DataFrameova.

Većinu vremena skupovi podataka koje želite koristiti (ili morate koristiti) imaju nedostajuće vrijednosti. Način na koji se nedostajući podaci obrađuju nosi suptilne kompromise koji mogu utjecati na vašu konačnu analizu i stvarne rezultate.

Pandas obrađuje nedostajuće vrijednosti na dva načina. Prvi ste već vidjeli u prethodnim odjeljcima: `NaN`, ili Not a Number. Ovo je zapravo posebna vrijednost koja je dio IEEE specifikacije za brojeve s pomičnim zarezom i koristi se samo za označavanje nedostajućih vrijednosti s pomičnim zarezom.

Za nedostajuće vrijednosti osim brojeva s pomičnim zarezom, pandas koristi Python objekt `None`. Iako se može činiti zbunjujućim da ćete naići na dvije različite vrste vrijednosti koje u osnovi govore isto, postoje valjani programerski razlozi za ovaj dizajnerski izbor i, u praksi, ovaj pristup omogućuje pandas biblioteci da pruži dobar kompromis za veliku većinu slučajeva. Bez obzira na to, i `None` i `NaN` imaju ograničenja koja morate imati na umu u vezi s načinom na koji se mogu koristiti.

Pogledajte više o `NaN` i `None` u [bilježnici](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/4-Data-Science-Lifecycle/15-analyzing/notebook.ipynb)!

- **Otkrivanje null vrijednosti**: U `pandas`, metode `isnull()` i `notnull()` su vaše primarne metode za otkrivanje null podataka. Obje vraćaju Booleanske maske nad vašim podacima. Koristit ćemo `numpy` za `NaN` vrijednosti:
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
Pažljivo pogledajte izlaz. Iznenađuje li vas nešto? Iako je `0` aritmetički null, ipak je savršeno dobar cijeli broj i pandas ga tako tretira. `''` je malo suptilniji. Iako smo ga koristili u odjeljku 1 za predstavljanje prazne vrijednosti niza, ipak je objekt niza, a ne predstavljanje null vrijednosti prema pandas biblioteci.

Sada, okrenimo ovo i koristimo ove metode na način koji je sličniji onome kako ćete ih koristiti u praksi. Možete koristiti Booleanske maske izravno kao indeks ``Series`` ili ``DataFrame``, što može biti korisno kada pokušavate raditi s izoliranim nedostajućim (ili prisutnim) vrijednostima.

> **Zaključak**: Obje metode `isnull()` i `notnull()` proizvode slične rezultate kada ih koristite u `DataFrameovima`: prikazuju rezultate i indeks tih rezultata, što će vam uvelike pomoći dok se borite s vašim podacima.

- **Uklanjanje null vrijednosti**: Osim identificiranja nedostajućih vrijednosti, pandas pruža praktičan način za uklanjanje null vrijednosti iz `Series` i `DataFrameova`. (Posebno kod velikih skupova podataka, često je preporučljivije jednostavno ukloniti nedostajuće [NA] vrijednosti iz vaše analize nego se nositi s njima na druge načine.) Kako bismo to vidjeli u praksi, vratimo se na `example1`:
```python
example1 = example1.dropna()
example1
```
```
0    0
2     
dtype: object
```
Primijetite da bi ovo trebalo izgledati kao vaš izlaz iz `example3[example3.notnull()]`. Razlika ovdje je u tome što, umjesto da samo indeksira na maskirane vrijednosti, `dropna` je uklonio te nedostajuće vrijednosti iz `Series` `example1`.

Budući da `DataFrameovi` imaju dvije dimenzije, pružaju više opcija za uklanjanje podataka.

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

(Jeste li primijetili da je pandas promijenio dva stupca u brojeve s pomičnim zarezom kako bi prilagodio `NaN`?)

Ne možete ukloniti jednu vrijednost iz `DataFramea`, pa morate ukloniti cijele retke ili stupce. Ovisno o tome što radite, možda ćete htjeti učiniti jedno ili drugo, pa pandas daje opcije za oba. Budući da u znanosti o podacima stupci općenito predstavljaju varijable, a redovi predstavljaju opažanja, vjerojatnije je da ćete ukloniti retke podataka; zadana postavka za `dropna()` je uklanjanje svih redaka koji sadrže bilo koje null vrijednosti:

```python
example2.dropna()
```
```
	0	1	2
1	2.0	5.0	8
```
Ako je potrebno, možete ukloniti NA vrijednosti iz stupaca. Koristite `axis=1` za to:
```python
example2.dropna(axis='columns')
```
```
	2
0	7
1	8
2	9
```
Primijetite da ovo može ukloniti puno podataka koje možda želite zadržati, posebno u manjim skupovima podataka. Što ako želite ukloniti samo retke ili stupce koji sadrže nekoliko ili čak sve null vrijednosti? Te postavke možete odrediti u `dropna` pomoću parametara `how` i `thresh`.

Prema zadanim postavkama, `how='any'` (ako želite provjeriti sami ili vidjeti koje druge parametre metoda ima, pokrenite `example4.dropna?` u ćeliji koda). Alternativno, možete odrediti `how='all'` kako biste uklonili samo retke ili stupce koji sadrže sve null vrijednosti. Proširimo naš primjer `DataFrame` kako bismo to vidjeli u praksi.

```python
example2[3] = np.nan
example2
```
|      |0  |1  |2  |3  |
|------|---|---|---|---|
|0     |1.0|NaN|7  |NaN|
|1     |2.0|5.0|8  |NaN|
|2     |NaN|6.0|9  |NaN|

Parametar `thresh` daje vam precizniju kontrolu: postavljate broj *ne-null* vrijednosti koje redak ili stupac mora imati kako bi se zadržao:
```python
example2.dropna(axis='rows', thresh=3)
```
```
	0	1	2	3
1	2.0	5.0	8	NaN
```
Ovdje su prvi i posljednji redak uklonjeni jer sadrže samo dvije ne-null vrijednosti.

- **Popunjavanje null vrijednosti**: Ovisno o vašem skupu podataka, ponekad može imati više smisla popuniti null vrijednosti valjanima nego ih ukloniti. Mogli biste koristiti `isnull` za to na licu mjesta, ali to može biti zamorno, posebno ako imate puno vrijednosti za popuniti. Budući da je ovo tako čest zadatak u znanosti o podacima, pandas pruža `fillna`, koji vraća kopiju `Series` ili `DataFramea` s nedostajućim vrijednostima zamijenjenim onima koje odaberete. Stvorimo još jedan primjer `Series` kako bismo vidjeli kako ovo funkcionira u praksi.
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
Možete popuniti sve null unose jednom vrijednošću, poput `0`:
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
Možete **popuniti unaprijed** null vrijednosti, koristeći posljednju valjanu vrijednost za popunjavanje null:
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
Također možete **popuniti unatrag** kako biste propagirali sljedeću valjanu vrijednost unatrag za popunjavanje null:
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
Kao što možete pretpostaviti, ovo funkcionira isto s `DataFrameovima`, ali također možete odrediti `axis` duž kojeg želite popuniti null vrijednosti. Koristeći ponovno prethodno korišteni `example2`:
```python
example2.fillna(method='ffill', axis=1)
```
```
	0	1	2	3
0	1.0	1.0	7.0	7.0
1	2.0	5.0	8.0	8.0
2	NaN	6.0	9.0	9.0
```
Primijetite da kada prethodna vrijednost nije dostupna za popunjavanje unaprijed, null vrijednost ostaje.
> **Ključna poruka:** Postoji više načina za rješavanje nedostajućih vrijednosti u vašim skupovima podataka. Specifična strategija koju koristite (uklanjanje, zamjena ili način na koji ih zamjenjujete) trebala bi biti određena karakteristikama tih podataka. Razvijat ćete bolji osjećaj za rješavanje nedostajućih vrijednosti što više radite s podacima i analizirate ih.

## Uklanjanje dupliciranih podataka

> **Cilj učenja:** Na kraju ovog pododjeljka trebali biste se osjećati ugodno u prepoznavanju i uklanjanju dupliciranih vrijednosti iz DataFrameova.

Osim nedostajućih podataka, često ćete naići na duplicirane podatke u stvarnim skupovima podataka. Srećom, `pandas` pruža jednostavan način za otkrivanje i uklanjanje dupliciranih unosa.

- **Prepoznavanje duplikata: `duplicated`**: Lako možete uočiti duplicirane vrijednosti koristeći metodu `duplicated` u pandas biblioteci, koja vraća Booleovu masku koja pokazuje je li unos u `DataFrameu` duplikat ranijeg unosa. Napravimo još jedan primjer `DataFramea` kako bismo vidjeli kako to funkcionira.
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
- **Uklanjanje duplikata: `drop_duplicates`:** jednostavno vraća kopiju podataka za koje su sve `duplicated` vrijednosti `False`:
```python
example4.drop_duplicates()
```
```
	letters	numbers
0	A	1
1	B	2
3	B	3
```
Obje metode, `duplicated` i `drop_duplicates`, prema zadanim postavkama uzimaju u obzir sve stupce, ali možete specificirati da pregledaju samo podskup stupaca u vašem `DataFrameu`:
```python
example4.drop_duplicates(['letters'])
```
```
letters	numbers
0	A	1
1	B	2
```

> **Ključna poruka:** Uklanjanje dupliciranih podataka ključni je dio gotovo svakog projekta u području znanosti o podacima. Duplicirani podaci mogu promijeniti rezultate vaših analiza i dovesti do netočnih zaključaka!


## 🚀 Izazov

Svi materijali koji su obrađeni dostupni su kao [Jupyter Notebook](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/2-Working-With-Data/08-data-preparation/notebook.ipynb). Osim toga, nakon svakog odjeljka nalaze se vježbe – isprobajte ih!

## [Kviz nakon predavanja](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/15)



## Pregled i samostalno učenje

Postoji mnogo načina za otkrivanje i pristup pripremi vaših podataka za analizu i modeliranje, a čišćenje podataka važan je korak koji zahtijeva praktično iskustvo. Isprobajte ove izazove na Kaggleu kako biste istražili tehnike koje nisu obrađene u ovoj lekciji.

- [Izazov čišćenja podataka: Parsiranje datuma](https://www.kaggle.com/rtatman/data-cleaning-challenge-parsing-dates/)

- [Izazov čišćenja podataka: Skaliranje i normalizacija podataka](https://www.kaggle.com/rtatman/data-cleaning-challenge-scale-and-normalize-data)


## Zadatak

[Procjena podataka iz obrasca](assignment.md)

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati mjerodavnim izvorom. Za kritične informacije preporučuje se profesionalni prijevod od strane stručnjaka. Ne preuzimamo odgovornost za bilo kakve nesporazume ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.