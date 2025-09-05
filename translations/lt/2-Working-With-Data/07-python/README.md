<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "577a611517482c3ceaf76d3d8142cba9",
  "translation_date": "2025-09-05T16:03:09+00:00",
  "source_file": "2-Working-With-Data/07-python/README.md",
  "language_code": "lt"
}
-->
# Darbas su duomenimis: Python ir Pandas biblioteka

| ![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/07-WorkWithPython.png) |
| :-------------------------------------------------------------------------------------------------------: |
|                 Darbas su Python - _Sketchnote by [@nitya](https://twitter.com/nitya)_                   |

[![Intro Video](../../../../2-Working-With-Data/07-python/images/video-ds-python.png)](https://youtu.be/dZjWOGbsN4Y)

Nors duomenų bazės siūlo labai efektyvius būdus saugoti duomenis ir užklausas vykdyti naudojant užklausų kalbas, lankstiausias duomenų apdorojimo būdas yra rašyti savo programą, kuri manipuliuoja duomenimis. Daugeliu atvejų duomenų bazės užklausa būtų efektyvesnis sprendimas. Tačiau kai kuriais atvejais, kai reikalingas sudėtingesnis duomenų apdorojimas, tai negali būti lengvai atlikta naudojant SQL. 
Duomenų apdorojimas gali būti programuojamas bet kuria programavimo kalba, tačiau yra tam tikrų kalbų, kurios yra aukštesnio lygio dirbant su duomenimis. Duomenų mokslininkai dažniausiai renkasi vieną iš šių kalbų:

* **[Python](https://www.python.org/)** – universali programavimo kalba, kuri dažnai laikoma viena geriausių pasirinkimų pradedantiesiems dėl savo paprastumo. Python turi daugybę papildomų bibliotekų, kurios gali padėti išspręsti daugelį praktinių problemų, pavyzdžiui, išgauti duomenis iš ZIP archyvo ar konvertuoti paveikslėlį į pilką spalvą. Be duomenų mokslo, Python taip pat dažnai naudojama interneto svetainių kūrimui.
* **[R](https://www.r-project.org/)** – tradicinė įrankių dėžė, sukurta statistinių duomenų apdorojimui. Ji taip pat turi didelę bibliotekų saugyklą (CRAN), todėl yra geras pasirinkimas duomenų apdorojimui. Tačiau R nėra universali programavimo kalba ir retai naudojama už duomenų mokslo ribų.
* **[Julia](https://julialang.org/)** – kita kalba, sukurta specialiai duomenų mokslui. Ji skirta geresniam našumui nei Python, todėl yra puikus įrankis moksliniams eksperimentams.

Šioje pamokoje mes sutelksime dėmesį į Python naudojimą paprastam duomenų apdorojimui. Mes prielaida, kad turite pagrindines žinias apie šią kalbą. Jei norite giliau susipažinti su Python, galite pasinaudoti vienu iš šių šaltinių:

* [Mokykitės Python smagiai su Turtle Graphics ir Fractals](https://github.com/shwars/pycourse) – greitas įvadas į Python programavimą GitHub platformoje
* [Pradėkite savo pirmuosius žingsnius su Python](https://docs.microsoft.com/en-us/learn/paths/python-first-steps/?WT.mc_id=academic-77958-bethanycheum) Mokymosi kelias [Microsoft Learn](http://learn.microsoft.com/?WT.mc_id=academic-77958-bethanycheum)

Duomenys gali būti įvairių formų. Šioje pamokoje mes apsvarstysime tris duomenų formas – **lentelinius duomenis**, **tekstą** ir **vaizdus**.

Mes sutelksime dėmesį į keletą duomenų apdorojimo pavyzdžių, o ne pateiksime visą susijusių bibliotekų apžvalgą. Tai leis jums suprasti pagrindinę idėją, kas įmanoma, ir paliks jums supratimą, kur rasti sprendimus savo problemoms, kai jų prireiks.

> **Naudingiausias patarimas**. Kai reikia atlikti tam tikrą operaciją su duomenimis, kurios nežinote, kaip atlikti, pabandykite ieškoti informacijos internete. [Stackoverflow](https://stackoverflow.com/) dažnai turi daug naudingų Python kodo pavyzdžių daugeliui tipinių užduočių.



## [Prieš pamokos testas](https://ff-quizzes.netlify.app/en/ds/quiz/12)

## Lenteliniai duomenys ir duomenų rėmeliai

Jūs jau susipažinote su lenteliniais duomenimis, kai kalbėjome apie reliacines duomenų bazes. Kai turite daug duomenų, kurie yra saugomi skirtingose susietose lentelėse, tikrai verta naudoti SQL darbui su jais. Tačiau yra daug atvejų, kai turime duomenų lentelę ir norime gauti tam tikrą **supratimą** ar **įžvalgas** apie šiuos duomenis, pavyzdžiui, pasiskirstymą, vertybių koreliaciją ir pan. Duomenų moksle dažnai reikia atlikti tam tikras pradinio duomenų transformacijas, po kurių seka vizualizacija. Abi šios užduotys gali būti lengvai atliktos naudojant Python.

Yra dvi naudingiausios Python bibliotekos, kurios gali padėti dirbti su lenteliniais duomenimis:
* **[Pandas](https://pandas.pydata.org/)** leidžia manipuliuoti vadinamaisiais **duomenų rėmeliais**, kurie yra analogiški reliacinėms lentelėms. Galite turėti pavadintas stulpelius ir atlikti įvairias operacijas su eilutėmis, stulpeliais ir duomenų rėmeliais apskritai.
* **[Numpy](https://numpy.org/)** yra biblioteka, skirta dirbti su **tensoriais**, t. y. daugiamačiais **masyvais**. Masyvas turi tos pačios pagrindinės rūšies vertybes, yra paprastesnis nei duomenų rėmelis, tačiau siūlo daugiau matematinių operacijų ir sukuria mažiau apkrovos.

Taip pat yra keletas kitų bibliotekų, kurias verta žinoti:
* **[Matplotlib](https://matplotlib.org/)** – biblioteka, naudojama duomenų vizualizacijai ir grafų braižymui
* **[SciPy](https://www.scipy.org/)** – biblioteka su papildomomis mokslinėmis funkcijomis. Jau susidūrėme su šia biblioteka, kai kalbėjome apie tikimybes ir statistiką

Štai kodo fragmentas, kurį paprastai naudotumėte šių bibliotekų importavimui Python programos pradžioje:
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import ... # you need to specify exact sub-packages that you need
``` 

Pandas yra pagrįsta keliais pagrindiniais konceptais.

### Serijos 

**Serijos** yra vertybių seka, panaši į sąrašą ar numpy masyvą. Pagrindinis skirtumas yra tas, kad serijos taip pat turi **indeksą**, ir kai atliekame operacijas su serijomis (pvz., jas sudedame), indeksas yra įtraukiamas į skaičiavimus. Indeksas gali būti toks paprastas kaip eilutės numeris (tai yra numatytasis indeksas, kai serija kuriama iš sąrašo ar masyvo), arba jis gali turėti sudėtingą struktūrą, pvz., datos intervalą.

> **Pastaba**: Įvadinis Pandas kodas pateiktas pridedamame užrašų knygelėje [`notebook.ipynb`](../../../../2-Working-With-Data/07-python/notebook.ipynb). Čia pateikiame tik keletą pavyzdžių, tačiau tikrai kviečiame peržiūrėti visą užrašų knygelę.

Pavyzdžiui, norime analizuoti mūsų ledų parduotuvės pardavimus. Sukurkime seriją pardavimų skaičių (kiekvieną dieną parduotų prekių skaičius) tam tikram laikotarpiui:

```python
start_date = "Jan 1, 2020"
end_date = "Mar 31, 2020"
idx = pd.date_range(start_date,end_date)
print(f"Length of index is {len(idx)}")
items_sold = pd.Series(np.random.randint(25,50,size=len(idx)),index=idx)
items_sold.plot()
```
![Laiko serijos grafikas](../../../../2-Working-With-Data/07-python/images/timeseries-1.png)

Dabar tarkime, kad kiekvieną savaitę organizuojame vakarėlį draugams ir pasiimame papildomus 10 ledų pakuočių vakarėliui. Galime sukurti kitą seriją, indeksuotą pagal savaitę, kad tai parodytume:
```python
additional_items = pd.Series(10,index=pd.date_range(start_date,end_date,freq="W"))
```
Kai sudedame dvi serijas, gauname bendrą skaičių:
```python
total_items = items_sold.add(additional_items,fill_value=0)
total_items.plot()
```
![Laiko serijos grafikas](../../../../2-Working-With-Data/07-python/images/timeseries-2.png)

> **Pastaba**: Mes nenaudojame paprastos sintaksės `total_items+additional_items`. Jei tai darytume, gautume daug `NaN` (*Not a Number*) reikšmių rezultato serijoje. Taip yra todėl, kad kai kurių indeksų taškų serijoje `additional_items` trūksta reikšmių, o sudėjus `NaN` su bet kuo gaunamas `NaN`. Todėl reikia nurodyti `fill_value` parametrą sudėties metu.

Su laiko serijomis taip pat galime **perdaryti** seriją su skirtingais laiko intervalais. Pavyzdžiui, jei norime apskaičiuoti vidutinį pardavimų kiekį mėnesiui, galime naudoti šį kodą:
```python
monthly = total_items.resample("1M").mean()
ax = monthly.plot(kind='bar')
```
![Mėnesio laiko serijos vidurkiai](../../../../2-Working-With-Data/07-python/images/timeseries-3.png)

### Duomenų rėmelis

Duomenų rėmelis iš esmės yra serijų kolekcija su tuo pačiu indeksu. Galime sujungti kelias serijas į duomenų rėmelį:
```python
a = pd.Series(range(1,10))
b = pd.Series(["I","like","to","play","games","and","will","not","change"],index=range(0,9))
df = pd.DataFrame([a,b])
```
Tai sukurs horizontalią lentelę, panašią į šią:
|     | 0   | 1    | 2   | 3   | 4      | 5   | 6      | 7    | 8    |
| --- | --- | ---- | --- | --- | ------ | --- | ------ | ---- | ---- |
| 0   | 1   | 2    | 3   | 4   | 5      | 6   | 7      | 8    | 9    |
| 1   | I   | like | to  | use | Python | and | Pandas | very | much |

Taip pat galime naudoti serijas kaip stulpelius ir nurodyti stulpelių pavadinimus naudodami žodyną:
```python
df = pd.DataFrame({ 'A' : a, 'B' : b })
```
Tai suteiks mums lentelę, panašią į šią:

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

**Pastaba**: Taip pat galime gauti šį lentelės išdėstymą transponuodami ankstesnę lentelę, pvz., rašydami 
```python
df = pd.DataFrame([a,b]).T..rename(columns={ 0 : 'A', 1 : 'B' })
```
Čia `.T` reiškia duomenų rėmelio transponavimo operaciją, t. y. eilučių ir stulpelių keitimą, o `rename` operacija leidžia pervadinti stulpelius, kad atitiktų ankstesnį pavyzdį.

Štai keletas svarbiausių operacijų, kurias galime atlikti su duomenų rėmeliais:

**Stulpelių pasirinkimas**. Galime pasirinkti atskirus stulpelius rašydami `df['A']` – ši operacija grąžina seriją. Taip pat galime pasirinkti stulpelių pogrupį į kitą duomenų rėmelį rašydami `df[['B','A']]` – tai grąžina kitą duomenų rėmelį.

**Filtravimas** tik tam tikrų eilučių pagal kriterijus. Pavyzdžiui, norėdami palikti tik eilutes, kuriose stulpelis `A` yra didesnis nei 5, galime rašyti `df[df['A']>5]`.

> **Pastaba**: Filtravimas veikia taip. Išraiška `df['A']<5` grąžina loginę seriją, kuri nurodo, ar išraiška yra `True` ar `False` kiekvienam pradiniam serijos `df['A']` elementui. Kai loginė serija naudojama kaip indeksas, ji grąžina eilučių pogrupį duomenų rėmelyje. Todėl negalima naudoti bet kokios Python loginės išraiškos, pavyzdžiui, rašyti `df[df['A']>5 and df['A']<7]` būtų neteisinga. Vietoj to turėtumėte naudoti specialią `&` operaciją loginėms serijoms, rašydami `df[(df['A']>5) & (df['A']<7)]` (*skliaustai čia yra svarbūs*).

**Naujų skaičiuojamų stulpelių kūrimas**. Galime lengvai sukurti naujus skaičiuojamus stulpelius savo duomenų rėmelyje naudodami intuityvią išraišką, pvz.:
```python
df['DivA'] = df['A']-df['A'].mean() 
``` 
Šis pavyzdys apskaičiuoja A nukrypimą nuo jo vidutinės vertės. Kas iš tikrųjų vyksta, yra tai, kad mes apskaičiuojame seriją ir tada priskiriame šią seriją kairiajai pusei, sukurdami kitą stulpelį. Todėl negalime naudoti jokių operacijų, kurios nesuderinamos su serijomis, pavyzdžiui, žemiau pateiktas kodas yra neteisingas:
```python
# Wrong code -> df['ADescr'] = "Low" if df['A'] < 5 else "Hi"
df['LenB'] = len(df['B']) # <- Wrong result
``` 
Pastarasis pavyzdys, nors sintaksiškai teisingas, duoda neteisingą rezultatą, nes priskiria serijos `B` ilgį visoms stulpelio reikšmėms, o ne atskirų elementų ilgį, kaip buvo numatyta.

Jei reikia apskaičiuoti sudėtingas išraiškas, galime naudoti `apply` funkciją. Paskutinis pavyzdys gali būti parašytas taip:
```python
df['LenB'] = df['B'].apply(lambda x : len(x))
# or 
df['LenB'] = df['B'].apply(len)
```

Po aukščiau pateiktų operacijų turėsime tokį duomenų rėmelį:

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

**Eilučių pasirinkimas pagal numerius** gali būti atliekamas naudojant `iloc` konstrukciją. Pavyzdžiui, norėdami pasirinkti pirmas 5 eilutes iš duomenų rėmelio:
```python
df.iloc[:5]
```

**Grupavimas** dažnai naudojamas norint gauti rezultatą, panašų į *pivot lenteles* Excel programoje. Tarkime, kad norime apskaičiuoti vidutinę stulpelio `A` vertę kiekvienam `LenB` skaičiui. Tada galime grupuoti savo duomenų rėmelį pagal `LenB` ir iškviesti `mean`:
```python
df.groupby(by='LenB').mean()
```
Jei reikia apskaičiuoti vidurkį ir elementų skaičių grupėje, tada galime naudoti sudėtingesnę `aggregate` funkciją:
```python
df.groupby(by='LenB') \
 .aggregate({ 'DivA' : len, 'A' : lambda x: x.mean() }) \
 .rename(columns={ 'DivA' : 'Count', 'A' : 'Mean'})
```
Tai suteikia mums tokią lentelę:

| LenB | Count | Mean     |
| ---- | ----- | -------- |
| 1    | 1     | 1.000000 |
| 2    | 1     | 3.000000 |
| 3    | 2     | 5.000000 |
| 4    | 3     | 6.333333 |
| 6    | 2     | 6.000000 |

### Duomenų gavimas
Mes jau matėme, kaip lengva sukurti Series ir DataFrames iš Python objektų. Tačiau duomenys dažniausiai pateikiami kaip tekstinis failas arba Excel lentelė. Laimei, Pandas siūlo paprastą būdą įkelti duomenis iš disko. Pavyzdžiui, CSV failo skaitymas yra toks paprastas:
```python
df = pd.read_csv('file.csv')
```
Daugiau duomenų įkėlimo pavyzdžių, įskaitant jų gavimą iš išorinių svetainių, aptarsime „Iššūkio“ skyriuje.

### Spausdinimas ir Vizualizavimas

Duomenų mokslininkas dažnai turi tyrinėti duomenis, todėl svarbu mokėti juos vizualizuoti. Kai DataFrame yra didelis, dažnai norime tiesiog įsitikinti, kad viską darome teisingai, išspausdindami pirmas kelias eilutes. Tai galima padaryti iškviečiant `df.head()`. Jei tai vykdote iš Jupyter Notebook, jis išspausdins DataFrame gražioje lentelės formoje.

Mes taip pat matėme `plot` funkcijos naudojimą kai kurių stulpelių vizualizavimui. Nors `plot` yra labai naudinga daugeliui užduočių ir palaiko daugybę skirtingų grafiko tipų per `kind=` parametrą, visada galite naudoti „matplotlib“ biblioteką, kad sukurtumėte sudėtingesnį grafiką. Duomenų vizualizavimą išsamiai aptarsime atskirose kurso pamokose.

Ši apžvalga apima svarbiausias Pandas koncepcijas, tačiau biblioteka yra labai turtinga, ir nėra ribų, ką su ja galite nuveikti! Dabar pritaikykime šias žinias sprendžiant konkrečią problemą.

## 🚀 Iššūkis 1: COVID plitimo analizė

Pirmoji problema, į kurią sutelksime dėmesį, yra COVID-19 epidemijos plitimo modeliavimas. Tam naudosime duomenis apie užsikrėtusių asmenų skaičių skirtingose šalyse, kuriuos pateikė [Sistemų mokslo ir inžinerijos centras](https://systems.jhu.edu/) (CSSE) iš [Johns Hopkins universiteto](https://jhu.edu/). Duomenų rinkinys pasiekiamas [šiame GitHub saugykloje](https://github.com/CSSEGISandData/COVID-19).

Kadangi norime parodyti, kaip dirbti su duomenimis, kviečiame atidaryti [`notebook-covidspread.ipynb`](../../../../2-Working-With-Data/07-python/notebook-covidspread.ipynb) ir perskaityti jį nuo pradžios iki pabaigos. Taip pat galite vykdyti langelius ir atlikti keletą iššūkių, kuriuos palikome jums pabaigoje.

![COVID plitimas](../../../../2-Working-With-Data/07-python/images/covidspread.png)

> Jei nežinote, kaip vykdyti kodą Jupyter Notebook, peržiūrėkite [šį straipsnį](https://soshnikov.com/education/how-to-execute-notebooks-from-github/).

## Darbas su nestruktūruotais duomenimis

Nors duomenys dažnai pateikiami lentelės forma, kai kuriais atvejais turime dirbti su mažiau struktūruotais duomenimis, pavyzdžiui, tekstu ar vaizdais. Tokiu atveju, norėdami taikyti aukščiau aptartas duomenų apdorojimo technikas, turime kažkaip **išgauti** struktūruotus duomenis. Štai keletas pavyzdžių:

* Raktažodžių ištraukimas iš teksto ir jų pasirodymo dažnumo analizė
* Neuroninių tinklų naudojimas informacijai apie objektus paveikslėlyje išgauti
* Informacijos apie žmonių emocijas vaizdo kameros sraute gavimas

## 🚀 Iššūkis 2: COVID mokslinių straipsnių analizė

Šiame iššūkyje tęsime COVID pandemijos temą ir sutelksime dėmesį į mokslinių straipsnių apie šią temą apdorojimą. Yra [CORD-19 duomenų rinkinys](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge), kuriame yra daugiau nei 7000 (rašymo metu) straipsnių apie COVID, pateikiamų su metaduomenimis ir santraukomis (apie pusę jų taip pat pateikiamas visas tekstas).

Pilnas šio duomenų rinkinio analizės pavyzdys naudojant [Text Analytics for Health](https://docs.microsoft.com/azure/cognitive-services/text-analytics/how-tos/text-analytics-for-health/?WT.mc_id=academic-77958-bethanycheum) kognityvinę paslaugą aprašytas [šiame tinklaraščio įraše](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/). Aptarsime supaprastintą šios analizės versiją.

> **NOTE**: Mes nepateikiame duomenų rinkinio kopijos kaip šios saugyklos dalies. Pirmiausia gali tekti atsisiųsti [`metadata.csv`](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge?select=metadata.csv) failą iš [šio Kaggle duomenų rinkinio](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge). Gali reikėti registracijos Kaggle. Taip pat galite atsisiųsti duomenų rinkinį be registracijos [iš čia](https://ai2-semanticscholar-cord-19.s3-us-west-2.amazonaws.com/historical_releases.html), tačiau jis apims visus pilnus tekstus, be metaduomenų failo.

Atidarykite [`notebook-papers.ipynb`](../../../../2-Working-With-Data/07-python/notebook-papers.ipynb) ir perskaitykite jį nuo pradžios iki pabaigos. Taip pat galite vykdyti langelius ir atlikti keletą iššūkių, kuriuos palikome jums pabaigoje.

![COVID medicininis gydymas](../../../../2-Working-With-Data/07-python/images/covidtreat.png)

## Vaizdų duomenų apdorojimas

Pastaruoju metu buvo sukurti labai galingi AI modeliai, leidžiantys suprasti vaizdus. Yra daug užduočių, kurias galima išspręsti naudojant iš anksto apmokytus neuroninius tinklus arba debesų paslaugas. Keletas pavyzdžių:

* **Vaizdų klasifikavimas**, kuris gali padėti suskirstyti vaizdą į vieną iš iš anksto apibrėžtų klasių. Galite lengvai apmokyti savo vaizdų klasifikatorius naudodami tokias paslaugas kaip [Custom Vision](https://azure.microsoft.com/services/cognitive-services/custom-vision-service/?WT.mc_id=academic-77958-bethanycheum)
* **Objektų aptikimas**, skirtas aptikti skirtingus objektus vaizde. Tokios paslaugos kaip [computer vision](https://azure.microsoft.com/services/cognitive-services/computer-vision/?WT.mc_id=academic-77958-bethanycheum) gali aptikti daugybę bendrų objektų, o jūs galite apmokyti [Custom Vision](https://azure.microsoft.com/services/cognitive-services/custom-vision-service/?WT.mc_id=academic-77958-bethanycheum) modelį aptikti tam tikrus specifinius objektus.
* **Veidų aptikimas**, įskaitant amžiaus, lyties ir emocijų aptikimą. Tai galima atlikti naudojant [Face API](https://azure.microsoft.com/services/cognitive-services/face/?WT.mc_id=academic-77958-bethanycheum).

Visos šios debesų paslaugos gali būti iškviečiamos naudojant [Python SDKs](https://docs.microsoft.com/samples/azure-samples/cognitive-services-python-sdk-samples/cognitive-services-python-sdk-samples/?WT.mc_id=academic-77958-bethanycheum), todėl jas lengva įtraukti į jūsų duomenų tyrinėjimo darbo eigą.

Štai keletas pavyzdžių, kaip tyrinėti duomenis iš vaizdų šaltinių:
* Tinklaraščio įraše [Kaip mokytis duomenų mokslo be programavimo](https://soshnikov.com/azure/how-to-learn-data-science-without-coding/) mes tyrinėjame Instagram nuotraukas, bandydami suprasti, kas skatina žmones daugiau „patinka“ nuotraukai. Pirmiausia iš paveikslėlių išgauname kuo daugiau informacijos naudodami [computer vision](https://azure.microsoft.com/services/cognitive-services/computer-vision/?WT.mc_id=academic-77958-bethanycheum), o tada naudojame [Azure Machine Learning AutoML](https://docs.microsoft.com/azure/machine-learning/concept-automated-ml/?WT.mc_id=academic-77958-bethanycheum), kad sukurtume interpretuojamą modelį.
* [Veidų tyrimų dirbtuvėse](https://github.com/CloudAdvocacy/FaceStudies) mes naudojame [Face API](https://azure.microsoft.com/services/cognitive-services/face/?WT.mc_id=academic-77958-bethanycheum), kad išgautume emocijas žmonių nuotraukose iš renginių, bandydami suprasti, kas daro žmones laimingus.

## Išvada

Nesvarbu, ar jau turite struktūruotus, ar nestruktūruotus duomenis, naudodami Python galite atlikti visus duomenų apdorojimo ir supratimo veiksmus. Tai turbūt lankstiausias duomenų apdorojimo būdas, todėl dauguma duomenų mokslininkų naudoja Python kaip pagrindinį įrankį. Mokytis Python išsamiai yra gera idėja, jei rimtai žiūrite į savo duomenų mokslo kelionę!

## [Po paskaitos testas](https://ff-quizzes.netlify.app/en/ds/quiz/13)

## Apžvalga ir savarankiškas mokymasis

**Knygos**
* [Wes McKinney. Python for Data Analysis: Data Wrangling with Pandas, NumPy, and IPython](https://www.amazon.com/gp/product/1491957662)

**Internetiniai ištekliai**
* Oficialus [10 minučių Pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html) vadovas
* [Dokumentacija apie Pandas vizualizavimą](https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html)

**Python mokymasis**
* [Mokykitės Python smagiai su Turtle Graphics ir Fractals](https://github.com/shwars/pycourse)
* [Pradėkite savo pirmuosius žingsnius su Python](https://docs.microsoft.com/learn/paths/python-first-steps/?WT.mc_id=academic-77958-bethanycheum) mokymosi kelias [Microsoft Learn](http://learn.microsoft.com/?WT.mc_id=academic-77958-bethanycheum)

## Užduotis

[Atlikite išsamesnį duomenų tyrimą aukščiau pateiktiems iššūkiams](assignment.md)

## Kreditas

Ši pamoka sukurta su ♥️ [Dmitry Soshnikov](http://soshnikov.com)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.