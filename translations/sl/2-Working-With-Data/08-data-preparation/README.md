<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3ade580a06b5f04d57cc83a768a8fb77",
  "translation_date": "2025-08-30T18:17:03+00:00",
  "source_file": "2-Working-With-Data/08-data-preparation/README.md",
  "language_code": "sl"
}
-->
# Delo z podatki: Priprava podatkov

|![ Sketchnote avtorja [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/08-DataPreparation.png)|
|:---:|
|Priprava podatkov - _Sketchnote avtorja [@nitya](https://twitter.com/nitya)_ |

## [Predhodni kviz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/14)

Odvisno od vira lahko surovi podatki vsebujejo nedoslednosti, ki otežujejo analizo in modeliranje. Z drugimi besedami, takšni podatki so lahko "neurejeni" in jih je treba očistiti. Ta lekcija se osredotoča na tehnike čiščenja in preoblikovanja podatkov za reševanje težav, kot so manjkajoči, netočni ali nepopolni podatki. Obravnavane teme v tej lekciji uporabljajo Python in knjižnico Pandas ter bodo [prikazane v zvezku](notebook.ipynb) v tej mapi.

## Pomen čiščenja podatkov

- **Enostavnost uporabe in ponovne uporabe**: Ko so podatki pravilno organizirani in normalizirani, jih je lažje iskati, uporabljati in deliti z drugimi.

- **Konsistentnost**: Podatkovna znanost pogosto zahteva delo z več nabori podatkov, kjer je treba združiti podatke iz različnih virov. Zagotavljanje, da ima vsak posamezen nabor podatkov skupne standarde, zagotavlja uporabnost podatkov tudi po združitvi v en nabor.

- **Natančnost modela**: Očiščeni podatki izboljšajo natančnost modelov, ki se nanje zanašajo.

## Pogosti cilji in strategije čiščenja

- **Raziskovanje nabora podatkov**: Raziskovanje podatkov, ki je obravnavano v [kasnejši lekciji](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/4-Data-Science-Lifecycle/15-analyzing), vam lahko pomaga odkriti podatke, ki jih je treba očistiti. Vizualno opazovanje vrednosti v naboru podatkov lahko ustvari pričakovanja o tem, kako izgleda preostanek, ali pa ponudi vpogled v težave, ki jih je treba rešiti. Raziskovanje lahko vključuje osnovno poizvedovanje, vizualizacije in vzorčenje.

- **Formatiranje**: Glede na vir lahko podatki vsebujejo nedoslednosti v načinu predstavitve. To lahko povzroči težave pri iskanju in prikazovanju vrednosti, kjer so podatki vidni v naboru, vendar niso pravilno predstavljeni v vizualizacijah ali rezultatih poizvedb. Pogoste težave s formatiranjem vključujejo odpravljanje presledkov, datume in tipe podatkov. Reševanje teh težav je običajno naloga uporabnikov podatkov. Na primer, standardi za prikazovanje datumov in številk se lahko razlikujejo glede na državo.

- **Podvajanja**: Podatki z več pojavitvami lahko povzročijo netočne rezultate in jih je običajno treba odstraniti. To je pogost pojav pri združevanju dveh ali več naborov podatkov. Vendar pa obstajajo primeri, ko podvajanje v združenih naborih vsebuje dodatne informacije, ki jih je morda treba ohraniti.

- **Manjkajoči podatki**: Manjkajoči podatki lahko povzročijo netočnosti ter šibke ali pristranske rezultate. Te težave je včasih mogoče rešiti z "ponovnim nalaganjem" podatkov, zapolnjevanjem manjkajočih vrednosti s pomočjo izračunov in kode, kot je Python, ali preprosto z odstranitvijo vrednosti in ustreznih podatkov. Razlogi za manjkajoče podatke so številni, ukrepi za njihovo reševanje pa so odvisni od tega, kako in zakaj so podatki manjkali.

## Raziskovanje informacij v DataFrame
> **Cilj učenja:** Do konca tega podpoglavja bi morali biti sposobni pridobiti splošne informacije o podatkih, shranjenih v pandas DataFrame.

Ko naložite podatke v pandas, bodo ti najverjetneje v obliki DataFrame (glejte prejšnjo [lekcijo](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/2-Working-With-Data/07-python#dataframe) za podroben pregled). Če pa ima DataFrame 60.000 vrstic in 400 stolpcev, kako sploh začeti razumeti, s čim delate? Na srečo pandas ponuja nekaj priročnih orodij za hitro pregledovanje splošnih informacij o DataFrame, poleg prvih in zadnjih nekaj vrstic.

Za raziskovanje te funkcionalnosti bomo uvozili knjižnico Python scikit-learn in uporabili ikoničen nabor podatkov: **Iris dataset**.

```python
import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()
iris_df = pd.DataFrame(data=iris['data'], columns=iris['feature_names'])
```
|                                        |dolžina čašnega lista (cm)|širina čašnega lista (cm)|dolžina venčnega lista (cm)|širina venčnega lista (cm)|
|----------------------------------------|--------------------------|--------------------------|---------------------------|--------------------------|
|0                                       |5.1                       |3.5                       |1.4                        |0.2                       |
|1                                       |4.9                       |3.0                       |1.4                        |0.2                       |
|2                                       |4.7                       |3.2                       |1.3                        |0.2                       |
|3                                       |4.6                       |3.1                       |1.5                        |0.2                       |
|4                                       |5.0                       |3.6                       |1.4                        |0.2                       |

- **DataFrame.info**: Za začetek se metoda `info()` uporablja za izpis povzetka vsebine, prisotne v `DataFrame`. Poglejmo si ta nabor podatkov:
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
Iz tega vemo, da ima nabor podatkov *Iris* 150 vnosov v štirih stolpcih brez praznih vnosov. Vsi podatki so shranjeni kot 64-bitne številske vrednosti s plavajočo vejico.

- **DataFrame.head()**: Nato za preverjanje dejanske vsebine `DataFrame` uporabimo metodo `head()`. Poglejmo, kako izgledajo prve vrstice našega `iris_df`:
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
- **DataFrame.tail()**: Nasprotno pa za preverjanje zadnjih nekaj vrstic `DataFrame` uporabimo metodo `tail()`:
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
> **Ključna misel:** Že samo z ogledom metapodatkov o informacijah v DataFrame ali prvih in zadnjih nekaj vrednosti lahko takoj dobite predstavo o velikosti, obliki in vsebini podatkov, s katerimi delate.

## Reševanje manjkajočih podatkov
> **Cilj učenja:** Do konca tega podpoglavja bi morali vedeti, kako zamenjati ali odstraniti prazne vrednosti iz DataFrame.

Večino časa nabori podatkov, ki jih želite (ali morate) uporabiti, vsebujejo manjkajoče vrednosti. Način obravnave manjkajočih podatkov vključuje subtilne kompromise, ki lahko vplivajo na vašo končno analizo in rezultate v resničnem svetu.

Pandas obravnava manjkajoče vrednosti na dva načina. Prvi, ki ste ga že videli v prejšnjih razdelkih, je `NaN` ali Not a Number. To je pravzaprav posebna vrednost, ki je del IEEE specifikacije za števila s plavajočo vejico in se uporablja samo za označevanje manjkajočih številsko-plavajočih vrednosti.

Za manjkajoče vrednosti, ki niso številske, pandas uporablja Pythonov objekt `None`. Čeprav se morda zdi zmedeno, da boste naleteli na dve različni vrsti vrednosti, ki v bistvu pomenita isto, obstajajo utemeljeni programerski razlogi za to oblikovalsko odločitev, ki v praksi omogoča pandasu, da ponudi dobro rešitev za večino primerov. Kljub temu pa imata tako `None` kot `NaN` omejitve, na katere morate biti pozorni glede njihove uporabe.

Več o `NaN` in `None` si oglejte v [zvezku](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/4-Data-Science-Lifecycle/15-analyzing/notebook.ipynb)!

- **Zaznavanje praznih vrednosti**: V `pandas` sta metodi `isnull()` in `notnull()` vaši glavni orodji za zaznavanje praznih podatkov. Obe vrneta logične maske nad vašimi podatki. Uporabili bomo `numpy` za vrednosti `NaN`:
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
Pozorno si oglejte izpis. Vas kaj preseneča? Čeprav je `0` aritmetična ničla, je še vedno povsem veljavna cela številka in pandas jo tako tudi obravnava. `''` je nekoliko bolj subtilen. Čeprav smo ga v razdelku 1 uporabili za predstavitev prazne nizovne vrednosti, je še vedno nizovni objekt in ne predstavlja prazne vrednosti v smislu pandas.

Zdaj pa obrnimo to okoli in uporabimo te metode na način, kot jih boste uporabljali v praksi. Logične maske lahko neposredno uporabite kot indeks `Series` ali `DataFrame`, kar je uporabno pri delu z izoliranimi manjkajočimi (ali prisotnimi) vrednostmi.

> **Ključna misel:** Tako metodi `isnull()` kot `notnull()` prikažeta podobne rezultate, ko ju uporabite v `DataFrame`: prikažeta rezultate in indeks teh rezultatov, kar vam bo v veliko pomoč pri delu s podatki.

- **Odstranjevanje praznih vrednosti**: Poleg prepoznavanja manjkajočih vrednosti pandas omogoča priročen način za odstranjevanje praznih vrednosti iz `Series` in `DataFrame`. (Še posebej pri velikih naborih podatkov je pogosto bolj priporočljivo preprosto odstraniti manjkajoče [NA] vrednosti iz analize, kot pa se z njimi ukvarjati na druge načine.) Da to vidimo v praksi, se vrnimo k `example1`:
```python
example1 = example1.dropna()
example1
```
```
0    0
2     
dtype: object
```
Opazite, da bi to moralo izgledati kot vaš izpis iz `example3[example3.notnull()]`. Razlika je v tem, da je `dropna` odstranil manjkajoče vrednosti iz `Series` `example1`, namesto da bi jih le indeksiral.

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

(Ste opazili, da je pandas dve stolpci pretvoril v števila s plavajočo vejico, da bi prilagodil `NaN`?)

Iz `DataFrame` ne morete odstraniti posamezne vrednosti, zato morate odstraniti cele vrstice ali stolpce. Glede na to, kaj počnete, boste morda želeli narediti eno ali drugo, zato pandas ponuja možnosti za oboje. Ker v podatkovni znanosti stolpci običajno predstavljajo spremenljivke, vrstice pa opazovanja, boste bolj verjetno odstranili vrstice podatkov; privzeta nastavitev za `dropna()` je odstranitev vseh vrstic, ki vsebujejo kakršne koli prazne vrednosti:

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
Opazite, da lahko to odstrani veliko podatkov, ki jih morda želite obdržati, še posebej v manjših naborih podatkov. Kaj pa, če želite odstraniti samo vrstice ali stolpce, ki vsebujejo več ali celo vse prazne vrednosti? Te nastavitve določite v `dropna` s parametroma `how` in `thresh`.

Privzeto je `how='any'` (če želite preveriti sami ali videti, katere druge parametre ima metoda, zaženite `example4.dropna?` v kodi). Lahko pa določite `how='all'`, da odstranite samo vrstice ali stolpce, ki vsebujejo vse prazne vrednosti. Razširimo naš primer `DataFrame`, da to vidimo v praksi.

```python
example2[3] = np.nan
example2
```
|      |0  |1  |2  |3  |
|------|---|---|---|---|
|0     |1.0|NaN|7  |NaN|
|1     |2.0|5.0|8  |NaN|
|2     |NaN|6.0|9  |NaN|

Parameter `thresh` vam omogoča natančnejši nadzor: nastavite število *ne-praznih* vrednosti, ki jih mora imeti vrstica ali stolpec, da se ohrani:
```python
example2.dropna(axis='rows', thresh=3)
```
```
	0	1	2	3
1	2.0	5.0	8	NaN
```
Tukaj sta bili prvi in zadnji vrstici odstranjeni, ker vsebujeta le dve ne-prazni vrednosti.

- **Zapolnjevanje praznih vrednosti**: Glede na vaš nabor podatkov je včasih smiselneje zapolniti prazne vrednosti z veljavnimi, namesto da jih odstranite. To bi lahko naredili z `isnull` na mestu, vendar je to lahko zamudno, še posebej, če imate veliko vrednosti za zapolniti. Ker je to tako pogosta naloga v podatkovni znanosti, pandas ponuja `fillna`, ki vrne kopijo `Series` ali `DataFrame` z manjkajočimi vrednostmi, nadomeščenimi z izbrano vrednostjo. Ustvarimo še en primer `Series`, da vidimo, kako to deluje v praksi.
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
Vse prazne vnose lahko zapolnite z eno samo vrednostjo, na primer `0`:
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
Lahko **naprej zapolnite** prazne vrednosti, kar pomeni, da uporabite zadnjo veljavno vrednost za zapolnitev prazne:
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
Lahko tudi **nazaj zapolnite**, da propagirate naslednjo veljavno vrednost nazaj za zapolnitev prazne:
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
Kot si lahko predstavljate, to deluje enako z `DataFrame`, vendar lahko določite tudi `axis`, vzdolž katerega zapolnite prazne vrednosti. Ponovno uporabimo prej uporabljeni `example2`:
```python
example2.fillna(method='ffill', axis=1)
```
```
	0	1	2	3
0	1.0	1.0	7.0	7.0
1	2.0	5.0	8.0	8.0
2	NaN	6.0	9.0	9.0
```
Opazite, da ko prejšnja vrednost ni na voljo za naprej zapolnjevanje, prazna vrednost ostane.
> **Ključna misel:** Obstaja več načinov za obravnavo manjkajočih vrednosti v vaših podatkovnih nizih. Specifična strategija, ki jo uporabite (odstranjevanje, zamenjava ali način zamenjave), naj bo prilagojena značilnostim teh podatkov. Bolj ko boste delali s podatkovnimi nizi, bolj boste razvili občutek za obravnavo manjkajočih vrednosti.

## Odstranjevanje podvojenih podatkov

> **Cilj učenja:** Do konca tega podpoglavja bi morali biti sposobni prepoznati in odstraniti podvojene vrednosti iz DataFrame-ov.

Poleg manjkajočih podatkov boste v resničnih podatkovnih nizih pogosto naleteli na podvojene podatke. Na srečo `pandas` ponuja preprost način za zaznavanje in odstranjevanje podvojenih vnosov.

- **Prepoznavanje podvojenih vrednosti: `duplicated`**: Podvojene vrednosti lahko enostavno prepoznate z metodo `duplicated` v pandas, ki vrne logično masko, ki označuje, ali je vnos v `DataFrame` podvojen glede na prejšnjega. Ustvarimo še en primer `DataFrame`, da vidimo, kako to deluje.
```python
example4 = pd.DataFrame({'letters': ['A','B'] * 2 + ['B'],
                         'numbers': [1, 2, 1, 3, 3]})
example4
```
|      |črke  |številke|
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
- **Odstranjevanje podvojenih vrednosti: `drop_duplicates`:** preprosto vrne kopijo podatkov, pri katerih so vse vrednosti `duplicated` označene kot `False`:
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

Vsi obravnavani materiali so na voljo kot [Jupyter Notebook](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/2-Working-With-Data/08-data-preparation/notebook.ipynb). Poleg tega so po vsakem razdelku na voljo vaje – preizkusite jih!

## [Kvizi po predavanju](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/15)



## Pregled in samostojno učenje

Obstaja veliko načinov za odkrivanje in pripravo podatkov za analizo ter modeliranje, čiščenje podatkov pa je pomemben korak, ki zahteva praktično izkušnjo. Preizkusite te izzive na Kagglu, da raziščete tehnike, ki jih ta lekcija ni zajela.

- [Izziv čiščenja podatkov: Razčlenjevanje datumov](https://www.kaggle.com/rtatman/data-cleaning-challenge-parsing-dates/)

- [Izziv čiščenja podatkov: Skaliranje in normalizacija podatkov](https://www.kaggle.com/rtatman/data-cleaning-challenge-scale-and-normalize-data)


## Naloga

[Ocenjevanje podatkov iz obrazca](assignment.md)

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za strojno prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitne nesporazume ali napačne razlage, ki izhajajo iz uporabe tega prevoda.