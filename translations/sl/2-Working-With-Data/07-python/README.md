<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "57f7db1f4c3ae3361c1d1fbafcdd690c",
  "translation_date": "2025-09-05T05:57:02+00:00",
  "source_file": "2-Working-With-Data/07-python/README.md",
  "language_code": "sl"
}
-->
# Delo s podatki: Python in knjižnica Pandas

| ![ Sketchnote avtorja [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/07-WorkWithPython.png) |
| :-----------------------------------------------------------------------------------------------------------: |
|                 Delo s Pythonom - _Sketchnote avtorja [@nitya](https://twitter.com/nitya)_                   |

[![Uvodni video](../../../../2-Working-With-Data/07-python/images/video-ds-python.png)](https://youtu.be/dZjWOGbsN4Y)

Medtem ko baze podatkov ponujajo zelo učinkovite načine za shranjevanje podatkov in njihovo poizvedovanje z uporabo jezikov za poizvedbe, je najbolj prilagodljiv način obdelave podatkov pisanje lastnega programa za manipulacijo podatkov. V mnogih primerih bi bila poizvedba v bazi podatkov bolj učinkovita. Vendar pa v nekaterih primerih, ko je potrebna bolj zapletena obdelava podatkov, to ni enostavno izvedljivo z uporabo SQL.  
Obdelavo podatkov je mogoče programirati v katerem koli programskem jeziku, vendar obstajajo določeni jeziki, ki so bolj primerni za delo s podatki. Podatkovni znanstveniki običajno uporabljajo enega od naslednjih jezikov:

* **[Python](https://www.python.org/)**, splošnonamenski programski jezik, ki velja za eno najboljših možnosti za začetnike zaradi svoje preprostosti. Python ima veliko dodatnih knjižnic, ki vam lahko pomagajo rešiti številne praktične težave, kot so pridobivanje podatkov iz ZIP arhiva ali pretvorba slike v sivinsko lestvico. Poleg podatkovne znanosti se Python pogosto uporablja tudi za spletni razvoj.  
* **[R](https://www.r-project.org/)** je tradicionalno orodje, razvito z mislijo na statistično obdelavo podatkov. Vsebuje tudi obsežno zbirko knjižnic (CRAN), zaradi česar je dobra izbira za obdelavo podatkov. Vendar pa R ni splošnonamenski programski jezik in se redko uporablja zunaj področja podatkovne znanosti.  
* **[Julia](https://julialang.org/)** je še en jezik, razvit posebej za podatkovno znanost. Namenjen je zagotavljanju boljše zmogljivosti kot Python, zaradi česar je odlično orodje za znanstvene eksperimente.

V tej lekciji se bomo osredotočili na uporabo Pythona za preprosto obdelavo podatkov. Predpostavljamo osnovno poznavanje jezika. Če želite bolj poglobljen vpogled v Python, si lahko ogledate enega od naslednjih virov:

* [Učite se Python na zabaven način s Turtle Graphics in fraktali](https://github.com/shwars/pycourse) - hitri uvodni tečaj programiranja v Pythonu na GitHubu  
* [Naredite prve korake s Pythonom](https://docs.microsoft.com/en-us/learn/paths/python-first-steps/?WT.mc_id=academic-77958-bethanycheum) - učna pot na [Microsoft Learn](http://learn.microsoft.com/?WT.mc_id=academic-77958-bethanycheum)

Podatki se lahko pojavijo v različnih oblikah. V tej lekciji bomo obravnavali tri oblike podatkov - **tabelarične podatke**, **besedilo** in **slike**.

Osredotočili se bomo na nekaj primerov obdelave podatkov, namesto da bi vam ponudili celoten pregled vseh povezanih knjižnic. To vam bo omogočilo, da dobite osnovno idejo o tem, kaj je mogoče, in pridobite razumevanje, kje najti rešitve za svoje težave, ko jih potrebujete.

> **Najbolj uporaben nasvet**. Ko morate izvesti določeno operacijo na podatkih, za katero ne veste, kako jo narediti, poskusite poiskati rešitev na internetu. [Stackoverflow](https://stackoverflow.com/) običajno vsebuje veliko uporabnih primerov kode v Pythonu za številne tipične naloge.

## [Predlekcijski kviz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/12)

## Tabelarični podatki in podatkovni okviri

S tabelaričnimi podatki ste se že srečali, ko smo govorili o relacijskih bazah podatkov. Ko imate veliko podatkov, ki so shranjeni v številnih različnih povezanih tabelah, je smiselno uporabiti SQL za delo z njimi. Vendar pa obstaja veliko primerov, ko imamo tabelo podatkov in želimo pridobiti nekaj **razumevanja** ali **vpogledov** o teh podatkih, kot so porazdelitev, korelacija med vrednostmi itd. V podatkovni znanosti je veliko primerov, ko moramo izvesti nekatere transformacije izvornih podatkov, ki jim sledi vizualizacija. Obe fazi je mogoče enostavno izvesti s Pythonom.

Obstajata dve najbolj uporabni knjižnici v Pythonu, ki vam lahko pomagata pri delu s tabelaričnimi podatki:
* **[Pandas](https://pandas.pydata.org/)** omogoča manipulacijo tako imenovanih **podatkovnih okvirjev** (DataFrames), ki so analogni relacijskim tabelam. Lahko imate poimenovane stolpce in izvajate različne operacije na vrsticah, stolpcih in podatkovnih okvirjih na splošno.  
* **[Numpy](https://numpy.org/)** je knjižnica za delo s **tenzorji**, tj. večdimenzionalnimi **polji**. Polje ima vrednosti iste osnovne vrste in je preprostejše od podatkovnega okvirja, vendar ponuja več matematičnih operacij in ustvarja manjšo obremenitev.

Obstajata tudi dve drugi knjižnici, ki ju je vredno poznati:
* **[Matplotlib](https://matplotlib.org/)** je knjižnica za vizualizacijo podatkov in risanje grafov  
* **[SciPy](https://www.scipy.org/)** je knjižnica z dodatnimi znanstvenimi funkcijami. S to knjižnico smo se že srečali, ko smo govorili o verjetnosti in statistiki.

Tukaj je primer kode, ki jo običajno uporabite za uvoz teh knjižnic na začetku programa v Pythonu:
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import ... # you need to specify exact sub-packages that you need
```

Pandas temelji na nekaj osnovnih konceptih.

### Series

**Series** je zaporedje vrednosti, podobno seznamu ali numpy polju. Glavna razlika je, da ima Series tudi **indeks**, in ko izvajamo operacije na Series (npr. jih seštevamo), se indeks upošteva. Indeks je lahko preprost kot celoštevilska številka vrstice (to je privzeti indeks pri ustvarjanju Series iz seznama ali polja) ali pa ima lahko kompleksno strukturo, kot je časovni interval.

> **Opomba**: V priloženem zvezku [`notebook.ipynb`](../../../../2-Working-With-Data/07-python/notebook.ipynb) je nekaj uvodne kode za Pandas. Tukaj bomo predstavili le nekaj primerov, vsekakor pa si oglejte celoten zvezek.

Razmislimo o primeru: želimo analizirati prodajo v naši sladoledarni. Ustvarimo Series številk prodaje (število prodanih enot na dan) za določeno časovno obdobje:

```python
start_date = "Jan 1, 2020"
end_date = "Mar 31, 2020"
idx = pd.date_range(start_date,end_date)
print(f"Length of index is {len(idx)}")
items_sold = pd.Series(np.random.randint(25,50,size=len(idx)),index=idx)
items_sold.plot()
```
![Graf časovne vrste](../../../../2-Working-With-Data/07-python/images/timeseries-1.png)

Recimo, da vsak teden organiziramo zabavo za prijatelje in vzamemo dodatnih 10 paketov sladoleda za zabavo. Ustvarimo lahko še eno Series, indeksirano po tednih, da to prikažemo:
```python
additional_items = pd.Series(10,index=pd.date_range(start_date,end_date,freq="W"))
```
Ko seštejemo dve Series, dobimo skupno število:
```python
total_items = items_sold.add(additional_items,fill_value=0)
total_items.plot()
```
![Graf časovne vrste](../../../../2-Working-With-Data/07-python/images/timeseries-2.png)

> **Opomba**: Ne uporabljamo preproste sintakse `total_items+additional_items`. Če bi jo, bi v rezultatih dobili veliko vrednosti `NaN` (*Not a Number*). To je zato, ker manjkajo vrednosti za nekatere točke indeksa v Series `additional_items`, in seštevanje `NaN` z nečim drugim vedno vrne `NaN`. Zato moramo med seštevanjem določiti parameter `fill_value`.

Pri časovnih vrstah lahko tudi **ponovno vzorčimo** Series z različnimi časovnimi intervali. Na primer, če želimo izračunati povprečno prodajo na mesec, lahko uporabimo naslednjo kodo:
```python
monthly = total_items.resample("1M").mean()
ax = monthly.plot(kind='bar')
```
![Mesečna povprečja časovne vrste](../../../../2-Working-With-Data/07-python/images/timeseries-3.png)

### DataFrame

Podatkovni okvir (DataFrame) je v bistvu zbirka Series z istim indeksom. Več Series lahko združimo v DataFrame:
```python
a = pd.Series(range(1,10))
b = pd.Series(["I","like","to","play","games","and","will","not","change"],index=range(0,9))
df = pd.DataFrame([a,b])
```
To bo ustvarilo horizontalno tabelo, kot je ta:
|     | 0   | 1    | 2   | 3   | 4      | 5   | 6      | 7    | 8    |
| --- | --- | ---- | --- | --- | ------ | --- | ------ | ---- | ---- |
| 0   | 1   | 2    | 3   | 4   | 5      | 6   | 7      | 8    | 9    |
| 1   | I   | like | to  | use | Python | and | Pandas | very | much |

Lahko pa uporabimo Series kot stolpce in določimo imena stolpcev z uporabo slovarja:
```python
df = pd.DataFrame({ 'A' : a, 'B' : b })
```
To nam bo dalo tabelo, kot je ta:

|     | A   | B      |
| --- | --- | ------ |
| 0   | 1   | I      |
| 1   | 2   | like   |
| 2   | 3   | to     |
| 3   | 4   | use    |
| 4   | 5   | Python |
| 5   | 6   | and    |
| 6   | 7   | Pandas |
| 7   | 8   | very   |
| 8   | 9   | much   |

**Opomba**: To tabelo lahko dobimo tudi z transponiranjem prejšnje tabele, npr. z zapisom 
```python
df = pd.DataFrame([a,b]).T..rename(columns={ 0 : 'A', 1 : 'B' })
```
Tukaj `.T` pomeni operacijo transponiranja DataFrame, tj. zamenjavo vrstic in stolpcev, operacija `rename` pa omogoča preimenovanje stolpcev, da ustrezajo prejšnjemu primeru.

Tukaj je nekaj najpomembnejših operacij, ki jih lahko izvedemo na DataFrame:

**Izbira stolpcev**. Posamezne stolpce lahko izberemo z zapisom `df['A']` - ta operacija vrne Series. Podmnožico stolpcev lahko izberemo v drug DataFrame z zapisom `df[['B','A']]` - to vrne drug DataFrame.

**Filtriranje** določenih vrstic po kriterijih. Na primer, če želimo obdržati le vrstice, kjer je stolpec `A` večji od 5, lahko zapišemo `df[df['A']>5]`.

> **Opomba**: Način delovanja filtriranja je naslednji. Izraz `df['A']<5` vrne logično Series, ki označuje, ali je izraz `True` ali `False` za vsak element izvirne Series `df['A']`. Ko se logična Series uporabi kot indeks, vrne podmnožico vrstic v DataFrame. Zato ni mogoče uporabiti poljubnega logičnega izraza v Pythonu, na primer zapis `df[df['A']>5 and df['A']<7]` bi bil napačen. Namesto tega morate uporabiti posebno operacijo `&` na logičnih Series, z zapisom `df[(df['A']>5) & (df['A']<7)]` (*oklepaji so tukaj pomembni*).

**Ustvarjanje novih izračunljivih stolpcev**. Z intuitivnim izrazom lahko enostavno ustvarimo nove izračunljive stolpce za naš DataFrame:
```python
df['DivA'] = df['A']-df['A'].mean() 
``` 
Ta primer izračuna odstopanje A od njegove povprečne vrednosti. Kar se tukaj dejansko zgodi, je, da izračunamo Series in jo nato dodelimo na levo stran, s čimer ustvarimo nov stolpec. Zato ne moremo uporabiti nobenih operacij, ki niso združljive s Series, na primer spodnja koda je napačna:
```python
# Wrong code -> df['ADescr'] = "Low" if df['A'] < 5 else "Hi"
df['LenB'] = len(df['B']) # <- Wrong result
``` 
Zadnji primer, čeprav je sintaktično pravilen, nam da napačen rezultat, ker dodeli dolžino Series `B` vsem vrednostim v stolpcu, namesto dolžine posameznih elementov, kot smo nameravali.

Če moramo izračunati zapletene izraze, lahko uporabimo funkcijo `apply`. Zadnji primer lahko zapišemo takole:
```python
df['LenB'] = df['B'].apply(lambda x : len(x))
# or 
df['LenB'] = df['B'].apply(len)
```

Po zgornjih operacijah bomo dobili naslednji DataFrame:

|     | A   | B      | DivA | LenB |
| --- | --- | ------ | ---- | ---- |
| 0   | 1   | I      | -4.0 | 1    |
| 1   | 2   | like   | -3.0 | 4    |
| 2   | 3   | to     | -2.0 | 2    |
| 3   | 4   | use    | -1.0 | 3    |
| 4   | 5   | Python | 0.0  | 6    |
| 5   | 6   | and    | 1.0  | 3    |
| 6   | 7   | Pandas | 2.0  | 6    |
| 7   | 8   | very   | 3.0  | 4    |
| 8   | 9   | much   | 4.0  | 4    |

**Izbira vrstic na podlagi številk** se lahko izvede z uporabo konstrukta `iloc`. Na primer, za izbiro prvih 5 vrstic iz DataFrame:
```python
df.iloc[:5]
```

**Skupine** se pogosto uporabljajo za pridobitev rezultata, podobnega *vrtilnim tabelam* v Excelu. Recimo, da želimo izračunati povprečno vrednost stolpca `A` za vsako dano število `LenB`. Nato lahko združimo naš DataFrame po `LenB` in pokličemo `mean`:
```python
df.groupby(by='LenB').mean()
```
Če moramo izračunati povprečje in število elementov v skupini, lahko uporabimo bolj zapleteno funkcijo `aggregate`:
```python
df.groupby(by='LenB') \
 .aggregate({ 'DivA' : len, 'A' : lambda x: x.mean() }) \
 .rename(columns={ 'DivA' : 'Count', 'A' : 'Mean'})
```
To nam da naslednjo tabelo:

| LenB | Count | Mean     |
| ---- | ----- | -------- |
| 1    | 1     | 1.000000 |
| 2    | 1     | 3.000000 |
| 3    | 2     | 5.000000 |
| 4    | 3     | 6.333333 |
| 6    | 2     | 6.000000 |

### Pridobivanje podatkov
Videli smo, kako enostavno je ustvariti Series in DataFrames iz Python objektov. Vendar pa podatki običajno prihajajo v obliki besedilne datoteke ali Excelove tabele. Na srečo nam Pandas ponuja preprost način za nalaganje podatkov z diska. Na primer, branje CSV datoteke je tako preprosto:
```python
df = pd.read_csv('file.csv')
```
V razdelku "Izziv" bomo videli več primerov nalaganja podatkov, vključno s pridobivanjem podatkov z zunanjih spletnih strani.

### Tiskanje in Vizualizacija

Podatkovni znanstvenik pogosto mora raziskovati podatke, zato je pomembno, da jih zna vizualizirati. Ko je DataFrame velik, pogosto želimo samo preveriti, ali vse deluje pravilno, tako da natisnemo prvih nekaj vrstic. To lahko storimo z uporabo funkcije `df.head()`. Če jo izvajate v Jupyter Notebooku, bo DataFrame prikazan v lepi tabelarni obliki.

Videli smo tudi uporabo funkcije `plot` za vizualizacijo nekaterih stolpcev. Čeprav je `plot` zelo uporaben za številne naloge in podpira različne vrste grafov prek parametra `kind=`, lahko vedno uporabite knjižnico `matplotlib` za risanje nečesa bolj kompleksnega. Podrobno bomo obravnavali vizualizacijo podatkov v ločenih lekcijah tečaja.

Ta pregled pokriva najpomembnejše koncepte Pandas, vendar je knjižnica zelo bogata in ni omejitev, kaj lahko z njo storite! Zdaj pa uporabimo to znanje za reševanje specifičnega problema.

## 🚀 Izziv 1: Analiza širjenja COVID-a

Prvi problem, na katerega se bomo osredotočili, je modeliranje širjenja epidemije COVID-19. Za to bomo uporabili podatke o številu okuženih posameznikov v različnih državah, ki jih zagotavlja [Center za sistemsko znanost in inženiring](https://systems.jhu.edu/) (CSSE) na [Univerzi Johns Hopkins](https://jhu.edu/). Podatkovni niz je na voljo v [tem GitHub repozitoriju](https://github.com/CSSEGISandData/COVID-19).

Ker želimo pokazati, kako ravnati s podatki, vas vabimo, da odprete [`notebook-covidspread.ipynb`](../../../../2-Working-With-Data/07-python/notebook-covidspread.ipynb) in ga preberete od začetka do konca. Prav tako lahko izvajate celice in rešite nekatere izzive, ki smo jih pustili na koncu.

![Širjenje COVID-a](../../../../2-Working-With-Data/07-python/images/covidspread.png)

> Če ne veste, kako izvajati kodo v Jupyter Notebooku, si oglejte [ta članek](https://soshnikov.com/education/how-to-execute-notebooks-from-github/).

## Delo z nestrukturiranimi podatki

Čeprav podatki pogosto prihajajo v tabelarni obliki, v nekaterih primerih moramo delati z manj strukturiranimi podatki, na primer besedilom ali slikami. V tem primeru, da uporabimo tehnike obdelave podatkov, ki smo jih videli zgoraj, moramo nekako **izvleči** strukturirane podatke. Tukaj je nekaj primerov:

* Izvlečenje ključnih besed iz besedila in preverjanje, kako pogosto se te besede pojavljajo
* Uporaba nevronskih mrež za pridobivanje informacij o objektih na sliki
* Pridobivanje informacij o čustvih ljudi na video posnetku

## 🚀 Izziv 2: Analiza COVID člankov

V tem izzivu bomo nadaljevali s temo pandemije COVID in se osredotočili na obdelavo znanstvenih člankov o tej temi. Obstaja [CORD-19 podatkovni niz](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) z več kot 7000 (v času pisanja) članki o COVID-u, ki so na voljo z metapodatki in povzetki (za približno polovico je na voljo tudi celotno besedilo).

Celoten primer analize tega podatkovnega niza z uporabo [Text Analytics for Health](https://docs.microsoft.com/azure/cognitive-services/text-analytics/how-tos/text-analytics-for-health/?WT.mc_id=academic-77958-bethanycheum) kognitivne storitve je opisan [v tem blogu](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/). Razpravljali bomo o poenostavljeni različici te analize.

> **NOTE**: Kopije podatkovnega niza ne zagotavljamo kot del tega repozitorija. Najprej boste morda morali prenesti datoteko [`metadata.csv`](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge?select=metadata.csv) iz [tega podatkovnega niza na Kaggle](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge). Registracija na Kaggle je morda potrebna. Podatkovni niz lahko prenesete tudi brez registracije [od tukaj](https://ai2-semanticscholar-cord-19.s3-us-west-2.amazonaws.com/historical_releases.html), vendar bo vključeval vsa celotna besedila poleg datoteke z metapodatki.

Odprite [`notebook-papers.ipynb`](../../../../2-Working-With-Data/07-python/notebook-papers.ipynb) in ga preberite od začetka do konca. Prav tako lahko izvajate celice in rešite nekatere izzive, ki smo jih pustili na koncu.

![Zdravljenje COVID-a](../../../../2-Working-With-Data/07-python/images/covidtreat.png)

## Obdelava slikovnih podatkov

V zadnjem času so bili razviti zelo zmogljivi AI modeli, ki nam omogočajo razumevanje slik. Obstaja veliko nalog, ki jih je mogoče rešiti z uporabo vnaprej usposobljenih nevronskih mrež ali oblačnih storitev. Nekateri primeri vključujejo:

* **Razvrščanje slik**, ki vam lahko pomaga kategorizirati sliko v eno od vnaprej določenih kategorij. Svoje razvrščevalnike slik lahko enostavno usposobite z uporabo storitev, kot je [Custom Vision](https://azure.microsoft.com/services/cognitive-services/custom-vision-service/?WT.mc_id=academic-77958-bethanycheum)
* **Prepoznavanje objektov**, za zaznavanje različnih objektov na sliki. Storitve, kot je [computer vision](https://azure.microsoft.com/services/cognitive-services/computer-vision/?WT.mc_id=academic-77958-bethanycheum), lahko zaznajo številne običajne objekte, vi pa lahko usposobite model [Custom Vision](https://azure.microsoft.com/services/cognitive-services/custom-vision-service/?WT.mc_id=academic-77958-bethanycheum) za zaznavanje specifičnih objektov.
* **Prepoznavanje obrazov**, vključno z zaznavanjem starosti, spola in čustev. To je mogoče storiti prek [Face API](https://azure.microsoft.com/services/cognitive-services/face/?WT.mc_id=academic-77958-bethanycheum).

Vse te oblačne storitve je mogoče klicati z uporabo [Python SDK-jev](https://docs.microsoft.com/samples/azure-samples/cognitive-services-python-sdk-samples/cognitive-services-python-sdk-samples/?WT.mc_id=academic-77958-bethanycheum), zato jih je mogoče enostavno vključiti v vaš potek raziskovanja podatkov.

Tukaj je nekaj primerov raziskovanja podatkov iz slikovnih virov:
* V blogu [Kako se naučiti podatkovne znanosti brez kodiranja](https://soshnikov.com/azure/how-to-learn-data-science-without-coding/) raziskujemo fotografije na Instagramu, da bi razumeli, kaj ljudi spodbudi k več všečkom na fotografiji. Najprej iz fotografij izvlečemo čim več informacij z uporabo [computer vision](https://azure.microsoft.com/services/cognitive-services/computer-vision/?WT.mc_id=academic-77958-bethanycheum), nato pa uporabimo [Azure Machine Learning AutoML](https://docs.microsoft.com/azure/machine-learning/concept-automated-ml/?WT.mc_id=academic-77958-bethanycheum) za izdelavo razložljivega modela.
* V [Delavnici študij obrazov](https://github.com/CloudAdvocacy/FaceStudies) uporabljamo [Face API](https://azure.microsoft.com/services/cognitive-services/face/?WT.mc_id=academic-77958-bethanycheum) za izvlečenje čustev ljudi na fotografijah z dogodkov, da bi razumeli, kaj ljudi osrečuje.

## Zaključek

Ne glede na to, ali že imate strukturirane ali nestrukturirane podatke, lahko z uporabo Pythona izvedete vse korake, povezane z obdelavo in razumevanjem podatkov. To je verjetno najbolj prilagodljiv način obdelave podatkov, zato večina podatkovnih znanstvenikov uporablja Python kot svoje primarno orodje. Poglobljeno učenje Pythona je verjetno dobra ideja, če ste resni glede svoje poti v podatkovni znanosti!

## [Kvizi po predavanju](https://ff-quizzes.netlify.app/en/ds/)

## Pregled in samostojno učenje

**Knjige**
* [Wes McKinney. Python for Data Analysis: Data Wrangling with Pandas, NumPy, and IPython](https://www.amazon.com/gp/product/1491957662)

**Spletni viri**
* Uradni [10 minutni Pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html) vodič
* [Dokumentacija o Pandas vizualizaciji](https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html)

**Učenje Pythona**
* [Naučite se Pythona na zabaven način z grafiko Turtle in fraktali](https://github.com/shwars/pycourse)
* [Naredite svoje prve korake s Pythonom](https://docs.microsoft.com/learn/paths/python-first-steps/?WT.mc_id=academic-77958-bethanycheum) učna pot na [Microsoft Learn](http://learn.microsoft.com/?WT.mc_id=academic-77958-bethanycheum)

## Naloga

[Izvedite podrobnejšo študijo podatkov za zgornje izzive](assignment.md)

## Zasluge

To lekcijo je z ♥️ avtoriral [Dmitry Soshnikov](http://soshnikov.com)

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni prevod s strani človeka. Ne prevzemamo odgovornosti za morebitne nesporazume ali napačne razlage, ki bi nastale zaradi uporabe tega prevoda.