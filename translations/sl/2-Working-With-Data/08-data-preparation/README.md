<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1b560955ff39a2bcf2a049fce474a951",
  "translation_date": "2025-09-05T19:36:12+00:00",
  "source_file": "2-Working-With-Data/08-data-preparation/README.md",
  "language_code": "sl"
}
-->
# Delo z podatki: Priprava podatkov

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/08-DataPreparation.png)|
|:---:|
|Priprava podatkov - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

## [Predhodni kviz](https://ff-quizzes.netlify.app/en/ds/quiz/14)

Odvisno od izvora lahko surovi podatki vsebujejo nedoslednosti, ki otežujejo analizo in modeliranje. Z drugimi besedami, ti podatki so lahko "neurejeni" in jih je treba očistiti. Ta lekcija se osredotoča na tehnike čiščenja in preoblikovanja podatkov za reševanje težav, kot so manjkajoči, netočni ali nepopolni podatki. Tematike, obravnavane v tej lekciji, uporabljajo Python in knjižnico Pandas ter so [prikazane v zvezku](../../../../2-Working-With-Data/08-data-preparation/notebook.ipynb) znotraj te mape.

## Pomen čiščenja podatkov

- **Enostavnost uporabe in ponovne uporabe**: Ko so podatki pravilno organizirani in normalizirani, jih je lažje iskati, uporabljati in deliti z drugimi.

- **Konsistentnost**: Podatkovna znanost pogosto zahteva delo z več kot enim naborom podatkov, kjer je treba združiti nabore podatkov iz različnih virov. Zagotavljanje, da ima vsak posamezen nabor podatkov skupno standardizacijo, zagotavlja uporabnost podatkov, ko so združeni v en nabor.

- **Natančnost modela**: Očiščeni podatki izboljšajo natančnost modelov, ki se nanje zanašajo.

## Pogosti cilji in strategije čiščenja

- **Raziskovanje nabora podatkov**: Raziskovanje podatkov, ki je obravnavano v [kasnejši lekciji](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/4-Data-Science-Lifecycle/15-analyzing), vam lahko pomaga odkriti podatke, ki jih je treba očistiti. Vizualno opazovanje vrednosti v naboru podatkov lahko ustvari pričakovanja o tem, kako bo izgledal preostanek, ali pa ponudi idejo o težavah, ki jih je mogoče rešiti. Raziskovanje lahko vključuje osnovno poizvedovanje, vizualizacije in vzorčenje.

- **Formatiranje**: Odvisno od izvora lahko podatki vsebujejo nedoslednosti v načinu predstavitve. To lahko povzroči težave pri iskanju in prikazovanju vrednosti, kjer so vidne v naboru podatkov, vendar niso pravilno predstavljene v vizualizacijah ali rezultatih poizvedb. Pogoste težave s formatiranjem vključujejo odpravljanje presledkov, datume in tipe podatkov. Reševanje težav s formatiranjem je običajno naloga uporabnikov podatkov. Na primer, standardi za predstavitev datumov in številk se lahko razlikujejo glede na državo.

- **Podvojitve**: Podatki, ki se pojavijo večkrat, lahko povzročijo netočne rezultate in jih je običajno treba odstraniti. To je pogost pojav pri združevanju dveh ali več naborov podatkov. Vendar pa obstajajo primeri, ko podvojitve v združenih naborih podatkov vsebujejo dodatne informacije, ki jih je morda treba ohraniti.

- **Manjkajoči podatki**: Manjkajoči podatki lahko povzročijo netočnosti ter šibke ali pristranske rezultate. Včasih jih je mogoče rešiti z "ponovnim nalaganjem" podatkov, zapolnjevanjem manjkajočih vrednosti z izračuni in kodo, kot je Python, ali preprosto odstranitvijo vrednosti in ustreznih podatkov. Obstaja veliko razlogov, zakaj podatki manjkajo, in ukrepi za reševanje teh manjkajočih vrednosti so lahko odvisni od tega, kako in zakaj so izginili.

## Raziskovanje informacij o DataFrame
> **Cilj učenja:** Do konca tega podpoglavja bi morali biti sposobni najti splošne informacije o podatkih, shranjenih v pandas DataFrame.

Ko naložite podatke v pandas, bodo najverjetneje v obliki DataFrame (glejte prejšnjo [lekcijo](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/2-Working-With-Data/07-python#dataframe) za podroben pregled). Če pa ima nabor podatkov v vašem DataFrame 60.000 vrstic in 400 stolpcev, kako sploh začeti razumeti, s čim delate? Na srečo [pandas](https://pandas.pydata.org/) ponuja nekaj priročnih orodij za hitro pregledovanje splošnih informacij o DataFrame, poleg prvih in zadnjih nekaj vrstic.

Za raziskovanje te funkcionalnosti bomo uvozili knjižnico Python scikit-learn in uporabili ikoničen nabor podatkov: **Iris dataset**.

```python
import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()
iris_df = pd.DataFrame(data=iris['data'], columns=iris['feature_names'])
```
|                                        |dolžina čašnih listov (cm)|širina čašnih listov (cm)|dolžina venčnih listov (cm)|širina venčnih listov (cm)|
|----------------------------------------|--------------------------|--------------------------|---------------------------|--------------------------|
|0                                       |5.1                       |3.5                       |1.4                       |0.2                       |
|1                                       |4.9                       |3.0                       |1.4                       |0.2                       |
|2                                       |4.7                       |3.2                       |1.3                       |0.2                       |
|3                                       |4.6                       |3.1                       |1.5                       |0.2                       |
|4                                       |5.0                       |3.6                       |1.4                       |0.2                       |

- **DataFrame.info**: Za začetek se metoda `info()` uporablja za izpis povzetka vsebine, prisotne v `DataFrame`. Poglejmo si ta nabor podatkov, da vidimo, kaj imamo:
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
Iz tega vemo, da ima nabor podatkov *Iris* 150 vnosov v štirih stolpcih brez manjkajočih vnosov. Vsi podatki so shranjeni kot 64-bitne plavajoče točke.

- **DataFrame.head()**: Nato, da preverimo dejansko vsebino `DataFrame`, uporabimo metodo `head()`. Poglejmo, kako izgledajo prve vrstice našega `iris_df`:
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
- **DataFrame.tail()**: Nasprotno, za preverjanje zadnjih nekaj vrstic `DataFrame` uporabimo metodo `tail()`:
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
> **Ključna misel:** Že samo z ogledom metapodatkov o informacijah v DataFrame ali prvih in zadnjih nekaj vrednosti v njem lahko takoj dobite idejo o velikosti, obliki in vsebini podatkov, s katerimi delate.

## Obvladovanje manjkajočih podatkov
> **Cilj učenja:** Do konca tega podpoglavja bi morali vedeti, kako zamenjati ali odstraniti manjkajoče vrednosti iz DataFrame.

Večino časa nabori podatkov, ki jih želite (ali morate) uporabiti, vsebujejo manjkajoče vrednosti. Način obravnave manjkajočih podatkov prinaša subtilne kompromise, ki lahko vplivajo na vašo končno analizo in rezultate v resničnem svetu.

Pandas obravnava manjkajoče vrednosti na dva načina. Prvi ste že videli v prejšnjih razdelkih: `NaN`, ali Not a Number. To je pravzaprav posebna vrednost, ki je del IEEE specifikacije za plavajoče točke in se uporablja samo za označevanje manjkajočih vrednosti plavajočih točk.

Za manjkajoče vrednosti, ki niso plavajoče točke, pandas uporablja Pythonov objekt `None`. Čeprav se morda zdi zmedeno, da boste naleteli na dve različni vrsti vrednosti, ki v bistvu pomenita isto, obstajajo utemeljeni programerski razlogi za to oblikovno izbiro, ki v praksi omogoča pandas, da ponudi dobro kompromisno rešitev za večino primerov. Kljub temu pa imata `None` in `NaN` omejitve, ki jih morate upoštevati glede tega, kako ju lahko uporabljate.

Več o `NaN` in `None` si oglejte v [zvezku](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/4-Data-Science-Lifecycle/15-analyzing/notebook.ipynb)!

- **Odkrivanje manjkajočih vrednosti**: V `pandas` sta metodi `isnull()` in `notnull()` vaši glavni metodi za odkrivanje manjkajočih podatkov. Obe vrneta logične maske nad vašimi podatki. Uporabili bomo `numpy` za vrednosti `NaN`:
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
Pozorno si oglejte izhod. Vas kaj preseneča? Čeprav je `0` aritmetična ničla, je kljub temu povsem veljavno celo število in pandas ga tako obravnava. `''` je nekoliko bolj subtilen. Čeprav smo ga v razdelku 1 uporabili za predstavitev prazne vrednosti niza, je kljub temu objekt niza in ne predstavitev ničle v smislu pandas.

Zdaj pa obrnimo to okoli in uporabimo te metode na način, kot jih boste uporabljali v praksi. Logične maske lahko neposredno uporabite kot indeks ``Series`` ali ``DataFrame``, kar je uporabno pri delu z izoliranimi manjkajočimi (ali prisotnimi) vrednostmi.

> **Ključna misel:** Obe metodi `isnull()` in `notnull()` dajeta podobne rezultate, ko ju uporabljate v `DataFrame`: prikazujeta rezultate in indeks teh rezultatov, kar vam bo izjemno pomagalo pri delu s podatki.

- **Odstranjevanje manjkajočih vrednosti**: Poleg identifikacije manjkajočih vrednosti pandas ponuja priročen način za odstranjevanje manjkajočih vrednosti iz `Series` in `DataFrame`. (Še posebej pri velikih naborih podatkov je pogosto bolj priporočljivo preprosto odstraniti manjkajoče [NA] vrednosti iz analize kot pa se ukvarjati z njimi na druge načine.) Da to vidimo v praksi, se vrnimo k `example1`:
```python
example1 = example1.dropna()
example1
```
```
0    0
2     
dtype: object
```
Opazite, da bi to moralo izgledati kot vaš izhod iz `example3[example3.notnull()]`. Razlika je v tem, da je `dropna` odstranil manjkajoče vrednosti iz `Series` `example1`, namesto da bi jih le indeksiral.

Ker imajo `DataFrame` dve dimenziji, omogočajo več možnosti za odstranjevanje podatkov.

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

(Ste opazili, da je pandas dve stolpci spremenil v plavajoče točke, da bi prilagodil `NaN`?)

Iz `DataFrame` ne morete odstraniti posamezne vrednosti, zato morate odstraniti cele vrstice ali stolpce. Odvisno od tega, kaj počnete, boste morda želeli narediti eno ali drugo, zato pandas ponuja možnosti za oboje. Ker v podatkovni znanosti stolpci običajno predstavljajo spremenljivke, vrstice pa opazovanja, boste bolj verjetno odstranili vrstice podatkov; privzeta nastavitev za `dropna()` je odstranitev vseh vrstic, ki vsebujejo kakršne koli manjkajoče vrednosti:

```python
example2.dropna()
```
```
	0	1	2
1	2.0	5.0	8
```
Če je potrebno, lahko odstranite vrednosti NA iz stolpcev. Uporabite `axis=1` za to:
```python
example2.dropna(axis='columns')
```
```
	2
0	7
1	8
2	9
```
Opazite, da lahko to odstrani veliko podatkov, ki jih morda želite obdržati, zlasti v manjših naborih podatkov. Kaj pa, če želite odstraniti le vrstice ali stolpce, ki vsebujejo več ali celo vse manjkajoče vrednosti? Te nastavitve lahko določite v `dropna` s parametroma `how` in `thresh`.

Privzeto je `how='any'` (če želite preveriti sami ali videti, katere druge parametre ima metoda, zaženite `example4.dropna?` v kodi). Lahko pa določite `how='all'`, da odstranite le vrstice ali stolpce, ki vsebujejo vse manjkajoče vrednosti. Razširimo naš primer `DataFrame`, da to vidimo v praksi.

```python
example2[3] = np.nan
example2
```
|      |0  |1  |2  |3  |
|------|---|---|---|---|
|0     |1.0|NaN|7  |NaN|
|1     |2.0|5.0|8  |NaN|
|2     |NaN|6.0|9  |NaN|

Parameter `thresh` vam omogoča bolj natančen nadzor: nastavite število *ne-null* vrednosti, ki jih mora vrstica ali stolpec imeti, da se ohrani:
```python
example2.dropna(axis='rows', thresh=3)
```
```
	0	1	2	3
1	2.0	5.0	8	NaN
```
Tukaj sta bila prva in zadnja vrstica odstranjeni, ker vsebujeta le dve ne-null vrednosti.

- **Zapolnjevanje manjkajočih vrednosti**: Odvisno od vašega nabora podatkov je včasih bolj smiselno zapolniti manjkajoče vrednosti z veljavnimi, kot pa jih odstraniti. Lahko uporabite `isnull` za to neposredno, vendar je to lahko zamudno, zlasti če imate veliko vrednosti za zapolnitev. Ker je to tako pogosta naloga v podatkovni znanosti, pandas ponuja `fillna`, ki vrne kopijo `Series` ali `DataFrame` z manjkajočimi vrednostmi, zamenjanimi z vrednostjo po vaši izbiri. Ustvarimo še en primer `Series`, da vidimo, kako to deluje v praksi.
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
Vse manjkajoče vnose lahko zapolnite z eno samo vrednostjo, na primer `0`:
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
Manjkajoče vrednosti lahko **zapolnite naprej**, kar pomeni, da uporabite zadnjo veljavno vrednost za zapolnitev manjkajoče:
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
Manjkajoče vrednosti lahko tudi **zapolnite nazaj**, kar pomeni, da propagirate naslednjo veljavno vrednost nazaj za zapolnitev manjkajoče:
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
Kot lahko uganete, to deluje enako z `DataFrame`, vendar lahko določite tudi `axis`, vzdolž katerega zapolnite manjkajoče vrednosti. Uporabimo ponovno prej uporabljeni `example2`:
```python
example2.fillna(method='ffill', axis=1)
```
```
	0	1	2	3
0	1.0	1.0	7.0	7.0
1	2.0	5.0	8.0	8.0
2	NaN	6.0	9.0	9.0
```
Opazite, da ko prejšnja vrednost ni na voljo za zapolnitev naprej, manjkajoča vrednost ostane.
> **Ključna misel:** Obstaja več načinov za obravnavo manjkajočih vrednosti v vaših podatkovnih nizih. Konkretna strategija, ki jo uporabite (odstranjevanje, zamenjava ali način zamenjave), naj bo prilagojena značilnostim teh podatkov. Boljši občutek za obravnavo manjkajočih vrednosti boste razvili z večjo izkušnjo pri delu in interakciji s podatkovnimi nizi.
## Odstranjevanje podvojenih podatkov

> **Cilj učenja:** Do konca tega podpoglavja bi morali biti sposobni prepoznati in odstraniti podvojene vrednosti iz DataFrame-ov.

Poleg manjkajočih podatkov boste v resničnih podatkovnih zbirkah pogosto naleteli na podvojene podatke. Na srečo `pandas` ponuja enostaven način za zaznavanje in odstranjevanje podvojenih vnosov.

- **Prepoznavanje podvojenih vrednosti: `duplicated`**: Podvojene vrednosti lahko enostavno prepoznate z metodo `duplicated` v pandas, ki vrne Boolean masko, ki označuje, ali je vnos v `DataFrame` podvojen glede na prejšnjega. Ustvarimo še en primer `DataFrame`, da to vidimo v praksi.
```python
example4 = pd.DataFrame({'letters': ['A','B'] * 2 + ['B'],
                         'numbers': [1, 2, 1, 3, 3]})
example4
```
|      |črke   |številke|
|------|-------|--------|
|0     |A      |1       |
|1     |B      |2       |
|2     |A      |1       |
|3     |B      |3       |
|4     |B      |3       |

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
- **Odstranjevanje podvojenih vrednosti: `drop_duplicates`:** preprosto vrne kopijo podatkov, pri katerih so vse vrednosti `duplicated` nastavljene na `False`:
```python
example4.drop_duplicates()
```
```
	letters	numbers
0	A	1
1	B	2
3	B	3
```
Tako `duplicated` kot `drop_duplicates` privzeto upoštevata vse stolpce, vendar lahko določite, da pregledujeta le podmnožico stolpcev v vašem `DataFrame`:
```python
example4.drop_duplicates(['letters'])
```
```
letters	numbers
0	A	1
1	B	2
```

> **Ključna misel:** Odstranjevanje podvojenih podatkov je bistven del skoraj vsakega projekta podatkovne znanosti. Podvojeni podatki lahko spremenijo rezultate vaših analiz in vam dajo netočne rezultate!


## 🚀 Izziv

Vsi obravnavani materiali so na voljo kot [Jupyter Notebook](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/2-Working-With-Data/08-data-preparation/notebook.ipynb). Poleg tega so po vsakem razdelku na voljo vaje, preizkusite jih!

## [Kvizi po predavanju](https://ff-quizzes.netlify.app/en/ds/quiz/15)



## Pregled & Samostojno učenje

Obstaja veliko načinov za odkrivanje in pripravo podatkov za analizo ter modeliranje, čiščenje podatkov pa je pomemben korak, ki zahteva praktično izkušnjo. Preizkusite te izzive na Kaggle, da raziščete tehnike, ki jih ta lekcija ni obravnavala.

- [Izziv čiščenja podatkov: Razčlenjevanje datumov](https://www.kaggle.com/rtatman/data-cleaning-challenge-parsing-dates/)

- [Izziv čiščenja podatkov: Skaliranje in normalizacija podatkov](https://www.kaggle.com/rtatman/data-cleaning-challenge-scale-and-normalize-data)


## Naloga

[Ocenjevanje podatkov iz obrazca](assignment.md)

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna napačna razumevanja ali napačne interpretacije, ki bi nastale zaradi uporabe tega prevoda.