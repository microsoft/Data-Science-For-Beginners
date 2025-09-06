<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1cf49f029ba1f25a54f0d5bc2fa575fc",
  "translation_date": "2025-09-05T16:13:17+00:00",
  "source_file": "1-Introduction/04-stats-and-probability/README.md",
  "language_code": "lt"
}
-->
# Trumpas įvadas į statistiką ir tikimybių teoriją

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/04-Statistics-Probability.png)|
|:---:|
| Statistika ir tikimybių teorija - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

Statistika ir tikimybių teorija yra dvi glaudžiai susijusios matematikos sritys, kurios yra labai svarbios duomenų mokslui. Nors galima dirbti su duomenimis neturint gilių matematikos žinių, vis tiek naudinga suprasti bent pagrindines sąvokas. Čia pateiksime trumpą įvadą, kuris padės jums pradėti.

[![Intro Video](../../../../1-Introduction/04-stats-and-probability/images/video-prob-and-stats.png)](https://youtu.be/Z5Zy85g4Yjw)

## [Prieš paskaitos testas](https://ff-quizzes.netlify.app/en/ds/quiz/6)

## Tikimybė ir atsitiktiniai kintamieji

**Tikimybė** yra skaičius tarp 0 ir 1, kuris parodo, kaip tikėtinas yra tam tikras **įvykis**. Ji apibrėžiama kaip teigiamų rezultatų (kurie veda į įvykį) skaičius, padalintas iš visų rezultatų skaičiaus, jei visi rezultatai yra vienodai tikėtini. Pavyzdžiui, metant kauliuką, tikimybė, kad gausime lyginį skaičių, yra 3/6 = 0.5.

Kalbėdami apie įvykius, naudojame **atsitiktinius kintamuosius**. Pavyzdžiui, atsitiktinis kintamasis, kuris reprezentuoja skaičių, gautą metant kauliuką, gali turėti reikšmes nuo 1 iki 6. Skaičių rinkinys nuo 1 iki 6 vadinamas **imties erdve**. Galime kalbėti apie tikimybę, kad atsitiktinis kintamasis įgaus tam tikrą reikšmę, pavyzdžiui, P(X=3)=1/6.

Ankstesniame pavyzdyje atsitiktinis kintamasis vadinamas **diskrečiu**, nes jo imties erdvė yra skaičiuojama, t. y. yra atskiri reikšmės, kurias galima išvardinti. Yra atvejų, kai imties erdvė yra realių skaičių intervalas arba visas realių skaičių rinkinys. Tokie kintamieji vadinami **tęstiniais**. Geras pavyzdys yra autobuso atvykimo laikas.

## Tikimybių pasiskirstymas

Diskrečių atsitiktinių kintamųjų atveju lengva aprašyti kiekvieno įvykio tikimybę funkcija P(X). Kiekvienai reikšmei *s* iš imties erdvės *S* ji suteiks skaičių nuo 0 iki 1, taip, kad visų P(X=s) reikšmių suma visiems įvykiams būtų lygi 1.

Labiausiai žinomas diskretus pasiskirstymas yra **vienodas pasiskirstymas**, kuriame yra N elementų imties erdvė, su vienoda tikimybe 1/N kiekvienam iš jų.

Sunkiau aprašyti tęstinio kintamojo tikimybių pasiskirstymą, kai reikšmės yra iš tam tikro intervalo [a,b] arba viso realių skaičių rinkinio ℝ. Pavyzdžiui, autobuso atvykimo laikas. Iš tiesų, kiekvienam tiksliam atvykimo laikui *t* tikimybė, kad autobusas atvyks būtent tuo metu, yra 0!

> Dabar žinote, kad įvykiai su 0 tikimybe įvyksta, ir labai dažnai! Bent jau kiekvieną kartą, kai atvyksta autobusas!

Galime kalbėti tik apie tikimybę, kad kintamasis pateks į tam tikrą reikšmių intervalą, pvz., P(t<sub>1</sub>≤X<t<sub>2</sub>). Tokiu atveju tikimybių pasiskirstymas aprašomas **tikimybių tankio funkcija** p(x), tokia, kad

![P(t_1\le X<t_2)=\int_{t_1}^{t_2}p(x)dx](../../../../1-Introduction/04-stats-and-probability/images/probability-density.png)

Tęstinis vienodo pasiskirstymo analogas vadinamas **tęstiniu vienodu pasiskirstymu**, kuris apibrėžiamas baigtiniame intervale. Tikimybė, kad reikšmė X pateks į intervalo ilgį l, yra proporcinga l ir didėja iki 1.

Kitas svarbus pasiskirstymas yra **normalusis pasiskirstymas**, apie kurį kalbėsime išsamiau žemiau.

## Vidurkis, dispersija ir standartinis nuokrypis

Tarkime, kad ištraukiame n atsitiktinio kintamojo X imčių seką: x<sub>1</sub>, x<sub>2</sub>, ..., x<sub>n</sub>. Galime apibrėžti **vidurkį** (arba **aritmetinį vidurkį**) tradiciniu būdu kaip (x<sub>1</sub>+x<sub>2</sub>+x<sub>n</sub>)/n. Didinant imties dydį (t. y. imant ribą su n→∞), gausime pasiskirstymo vidurkį (dar vadinamą **lūkesčiu**). Lūkesčius žymėsime **E**(x).

> Galima parodyti, kad bet kuriam diskrečiam pasiskirstymui su reikšmėmis {x<sub>1</sub>, x<sub>2</sub>, ..., x<sub>N</sub>} ir atitinkamomis tikimybėmis p<sub>1</sub>, p<sub>2</sub>, ..., p<sub>N</sub>, lūkesčiai bus lygūs E(X)=x<sub>1</sub>p<sub>1</sub>+x<sub>2</sub>p<sub>2</sub>+...+x<sub>N</sub>p<sub>N</sub>.

Norėdami nustatyti, kaip toli reikšmės yra išsisklaidžiusios, galime apskaičiuoti dispersiją σ<sup>2</sup> = ∑(x<sub>i</sub> - μ)<sup>2</sup>/n, kur μ yra sekos vidurkis. Reikšmė σ vadinama **standartiniu nuokrypiu**, o σ<sup>2</sup> vadinama **dispersija**.

## Moda, mediana ir kvartiliai

Kartais vidurkis nepakankamai gerai atspindi „tipinę“ duomenų reikšmę. Pavyzdžiui, kai yra keletas ekstremalių reikšmių, kurios visiškai iškrenta iš diapazono, jos gali paveikti vidurkį. Kitas geras rodiklis yra **mediana**, reikšmė, tokia, kad pusė duomenų taškų yra mažesni už ją, o kita pusė - didesni.

Norėdami geriau suprasti duomenų pasiskirstymą, naudinga kalbėti apie **kvartilius**:

* Pirmasis kvartilis, arba Q1, yra reikšmė, tokia, kad 25% duomenų yra mažesni už ją
* Trečiasis kvartilis, arba Q3, yra reikšmė, tokia, kad 75% duomenų yra mažesni už ją

Grafiškai galime pavaizduoti medianos ir kvartilių santykį diagramoje, vadinamoje **dėžės diagrama**:

<img src="images/boxplot_explanation.png" width="50%"/>

Čia taip pat apskaičiuojame **tarpkvartilinį diapazoną** IQR=Q3-Q1 ir vadinamuosius **išskirtinius taškus** - reikšmes, kurios yra už ribų [Q1-1.5*IQR,Q3+1.5*IQR].

Baigtiniam pasiskirstymui, kuriame yra nedaug galimų reikšmių, gera „tipinė“ reikšmė yra ta, kuri pasirodo dažniausiai, vadinama **moda**. Ji dažnai taikoma kategoriniams duomenims, tokiems kaip spalvos. Įsivaizduokite situaciją, kai turime dvi žmonių grupes - vieni stipriai mėgsta raudoną spalvą, o kiti mėgsta mėlyną. Jei koduotume spalvas skaičiais, vidutinė mėgstamos spalvos reikšmė būtų kažkur oranžinės-žalios spektro dalyje, kuri neatspindėtų tikrosios nei vienos grupės preferencijos. Tačiau moda būtų viena iš spalvų arba abi spalvos, jei žmonių, balsuojančių už jas, skaičius būtų vienodas (tokiu atveju imtis vadinama **daugiamodine**).

## Realūs duomenys

Analizuojant realaus pasaulio duomenis, jie dažnai nėra atsitiktiniai kintamieji, ta prasme, kad neatliekame eksperimentų su nežinomu rezultatu. Pavyzdžiui, apsvarstykime beisbolo žaidėjų komandą ir jų kūno duomenis, tokius kaip ūgis, svoris ir amžius. Šie skaičiai nėra visiškai atsitiktiniai, tačiau vis tiek galime taikyti tuos pačius matematinius konceptus. Pavyzdžiui, žmonių svorių seka gali būti laikoma reikšmių seka, paimta iš tam tikro atsitiktinio kintamojo. Žemiau pateikiama faktinių beisbolo žaidėjų svorių seka iš [Major League Baseball](http://mlb.mlb.com/index.jsp), paimta iš [šio duomenų rinkinio](http://wiki.stat.ucla.edu/socr/index.php/SOCR_Data_MLB_HeightsWeights) (patogumui pateikiamos tik pirmos 20 reikšmių):

```
[180.0, 215.0, 210.0, 210.0, 188.0, 176.0, 209.0, 200.0, 231.0, 180.0, 188.0, 180.0, 185.0, 160.0, 180.0, 185.0, 197.0, 189.0, 185.0, 219.0]
```

> **Pastaba**: Norėdami pamatyti, kaip dirbti su šiuo duomenų rinkiniu, peržiūrėkite [pridedamą užrašų knygelę](../../../../1-Introduction/04-stats-and-probability/notebook.ipynb). Pamokoje taip pat yra keletas užduočių, kurias galite atlikti pridėdami kodą į tą užrašų knygelę. Jei nesate tikri, kaip dirbti su duomenimis, nesijaudinkite - vėliau grįšime prie darbo su duomenimis naudojant Python. Jei nežinote, kaip vykdyti kodą Jupyter užrašų knygelėje, peržiūrėkite [šį straipsnį](https://soshnikov.com/education/how-to-execute-notebooks-from-github/).

Štai dėžės diagrama, rodanti vidurkį, medianą ir kvartilius mūsų duomenims:

![Weight Box Plot](../../../../1-Introduction/04-stats-and-probability/images/weight-boxplot.png)

Kadangi mūsų duomenyse yra informacija apie skirtingus žaidėjų **vaidmenis**, galime sudaryti dėžės diagramą pagal vaidmenį - tai leis mums suprasti, kaip parametrų reikšmės skiriasi tarp vaidmenų. Šį kartą apsvarstysime ūgį:

![Box plot by role](../../../../1-Introduction/04-stats-and-probability/images/boxplot_byrole.png)

Ši diagrama rodo, kad, vidutiniškai, pirmosios bazės žaidėjų ūgis yra didesnis nei antrosios bazės žaidėjų ūgis. Vėliau šioje pamokoje išmoksime, kaip formaliau patikrinti šią hipotezę ir kaip parodyti, kad mūsų duomenys yra statistiškai reikšmingi tai įrodyti.

> Dirbant su realaus pasaulio duomenimis, darome prielaidą, kad visi duomenų taškai yra imtys, paimtos iš tam tikro tikimybių pasiskirstymo. Ši prielaida leidžia taikyti mašininio mokymosi metodus ir kurti veikiančius prognozavimo modelius.

Norėdami pamatyti, koks yra mūsų duomenų pasiskirstymas, galime sudaryti grafiką, vadinamą **histograma**. X ašis turėtų turėti skirtingų svorio intervalų skaičių (vadinamų **dėžėmis**), o vertikali ašis turėtų rodyti, kiek kartų mūsų atsitiktinio kintamojo imtis buvo tam tikrame intervale.

![Histogram of real world data](../../../../1-Introduction/04-stats-and-probability/images/weight-histogram.png)

Iš šios histogramos matote, kad visos reikšmės yra sutelktos aplink tam tikrą vidutinį svorį, o kuo toliau nuo to svorio - tuo mažiau svorių su ta reikšme yra aptinkama. Kitaip tariant, labai mažai tikėtina, kad beisbolo žaidėjo svoris labai skirsis nuo vidutinio svorio. Svorio dispersija rodo, kiek svoriai gali skirtis nuo vidurkio.

> Jei paimtume kitų žmonių, ne iš beisbolo lygos, svorius, pasiskirstymas greičiausiai būtų kitoks. Tačiau pasiskirstymo forma išliktų ta pati, tik vidurkis ir dispersija pasikeistų. Taigi, jei treniruosime savo modelį su beisbolo žaidėjais, jis greičiausiai duos neteisingus rezultatus, kai bus taikomas universiteto studentams, nes pagrindinis pasiskirstymas yra kitoks.

## Normalusis pasiskirstymas

Svorio pasiskirstymas, kurį matėme aukščiau, yra labai tipiškas, ir daugelis realaus pasaulio matavimų seka tokio paties tipo pasiskirstymą, bet su skirtingu vidurkiu ir dispersija. Šis pasiskirstymas vadinamas **normaliuoju pasiskirstymu**, ir jis vaidina labai svarbų vaidmenį statistikoje.

Naudoti normalųjį pasiskirstymą yra teisingas būdas generuoti potencialių beisbolo žaidėjų atsitiktinius svorius. Kai žinome vidutinį svorį `mean` ir standartinį nuokrypį `std`, galime sugeneruoti 1000 svorio imčių šiuo būdu:
```python
samples = np.random.normal(mean,std,1000)
```

Jei sudarysime sugeneruotų imčių histogramą, pamatysime vaizdą, labai panašų į aukščiau pateiktą. O jei padidinsime imčių skaičių ir dėžių skaičių, galime sugeneruoti normalaus pasiskirstymo vaizdą, kuris yra artimesnis idealiam:

![Normal Distribution with mean=0 and std.dev=1](../../../../1-Introduction/04-stats-and-probability/images/normal-histogram.png)

*Normalusis pasiskirstymas su vidurkiu=0 ir standartiniu nuokrypiu=1*

## Pasitikėjimo intervalai

Kalbėdami apie beisbolo žaidėjų svorius, darome prielaidą, kad yra tam tikras **atsitiktinis kintamasis W**, kuris atitinka idealų visų beisbolo žaidėjų svorių tikimybių pasiskirstymą (vadinamą **populiacija**). Mūsų svorių seka atitinka visų beisbolo žaidėjų pogrupį, kurį vadiname **imčiu**. Įdomus klausimas yra, ar galime žinoti W pasiskirstymo parametrus, t. y. populiacijos vidurkį ir dispersiją?

Lengviausias atsakymas būtų apskaičiuoti mūsų imties vidurkį ir dispersiją. Tačiau gali nutikti taip, kad mūsų atsitiktinė imtis tiksliai neatspindi visos populiacijos. Todėl prasminga kalbėti apie **pasitikėjimo intervalą**.

> **Pasitikėjimo intervalas** yra tikrojo populiacijos vidurkio įvertinimas, atsižvelgiant į mūsų imtį, kuris yra tikslus tam tikra tikimybe (arba **pasitikėjimo lygiu**).

Tarkime, turime imtį X

1<sub>1</sub>, ..., X<sub>n</sub> iš mūsų paskirstymo. Kiekvieną kartą, kai imame pavyzdį iš paskirstymo, gauname skirtingą vidutinę reikšmę μ. Taigi, μ gali būti laikoma atsitiktiniu kintamuoju. **Pasitikėjimo intervalas** su pasitikėjimu p yra reikšmių pora (L<sub>p</sub>,R<sub>p</sub>), tokia, kad **P**(L<sub>p</sub>≤μ≤R<sub>p</sub>) = p, t. y. tikimybė, kad išmatuota vidutinė reikšmė pateks į intervalą, lygi p.

Išsamiai aptarti, kaip skaičiuojami pasitikėjimo intervalai, viršija mūsų trumpo įvado ribas. Daugiau informacijos galima rasti [Vikipedijoje](https://en.wikipedia.org/wiki/Confidence_interval). Trumpai tariant, mes apibrėžiame apskaičiuoto pavyzdžio vidurkio paskirstymą, palyginti su tikru populiacijos vidurkiu, kuris vadinamas **studento paskirstymu**.

> **Įdomus faktas**: Studentų paskirstymas pavadintas matematikos mokslininko William Sealy Gosset garbei, kuris savo darbą publikavo pseudonimu „Student“. Jis dirbo Guinness alaus darykloje, ir, pasak vienos versijos, jo darbdavys nenorėjo, kad visuomenė žinotų, jog jie naudoja statistinius testus žaliavų kokybei nustatyti.

Jei norime įvertinti populiacijos vidurkį μ su pasitikėjimu p, turime paimti *(1-p)/2-tą procentilę* iš Studentų paskirstymo A, kurią galima rasti lentelėse arba apskaičiuoti naudojant statistinės programinės įrangos (pvz., Python, R ir kt.) funkcijas. Tada μ intervalas būtų X±A*D/√n, kur X yra gautas pavyzdžio vidurkis, D yra standartinis nuokrypis.

> **Pastaba**: Taip pat praleidžiame svarbios sąvokos [laisvės laipsniai](https://en.wikipedia.org/wiki/Degrees_of_freedom_(statistics)) aptarimą, kuri yra svarbi studentų paskirstymui. Norėdami geriau suprasti šią sąvoką, galite kreiptis į išsamesnes statistikos knygas.

Pavyzdys, kaip apskaičiuoti pasitikėjimo intervalą svoriams ir ūgiams, pateiktas [pridedamuose užrašuose](../../../../1-Introduction/04-stats-and-probability/notebook.ipynb).

| p | Vidutinis svoris |
|-----|----------------|
| 0.85 | 201.73±0.94 |
| 0.90 | 201.73±1.08 |
| 0.95 | 201.73±1.28 |

Atkreipkite dėmesį, kad kuo didesnė pasitikėjimo tikimybė, tuo platesnis pasitikėjimo intervalas.

## Hipotezių testavimas

Mūsų beisbolo žaidėjų duomenų rinkinyje yra skirtingos žaidėjų pozicijos, kurios gali būti apibendrintos žemiau (žr. [pridedamą užrašų knygelę](../../../../1-Introduction/04-stats-and-probability/notebook.ipynb), kad pamatytumėte, kaip ši lentelė gali būti apskaičiuota):

| Pozicija | Ūgis | Svoris | Kiekis |
|----------|------|--------|--------|
| Gaudytojas | 72.723684 | 204.328947 | 76 |
| Smūgiuotojas | 74.222222 | 220.888889 | 18 |
| Pirmasis bazės žaidėjas | 74.000000 | 213.109091 | 55 |
| Lauko žaidėjas | 73.010309 | 199.113402 | 194 |
| Atsarginis metikas | 74.374603 | 203.517460 | 315 |
| Antrasis bazės žaidėjas | 71.362069 | 184.344828 | 58 |
| Trumpasis žaidėjas | 71.903846 | 182.923077 | 52 |
| Pradinis metikas | 74.719457 | 205.163636 | 221 |
| Trečiasis bazės žaidėjas | 73.044444 | 200.955556 | 45 |

Galime pastebėti, kad pirmųjų bazės žaidėjų vidutinis ūgis yra didesnis nei antrųjų bazės žaidėjų. Taigi galime manyti, kad **pirmieji bazės žaidėjai yra aukštesni nei antrieji bazės žaidėjai**.

> Šis teiginys vadinamas **hipoteze**, nes mes nežinome, ar tai iš tikrųjų tiesa.

Tačiau ne visada akivaizdu, ar galime padaryti tokią išvadą. Iš aukščiau pateiktos diskusijos žinome, kad kiekvienas vidurkis turi susijusį pasitikėjimo intervalą, todėl šis skirtumas gali būti tik statistinė klaida. Mums reikia formalesnio būdo hipotezei patikrinti.

Apskaičiuokime pasitikėjimo intervalus atskirai pirmųjų ir antrųjų bazės žaidėjų ūgiams:

| Pasitikėjimas | Pirmieji bazės žaidėjai | Antrieji bazės žaidėjai |
|---------------|-------------------------|-------------------------|
| 0.85 | 73.62..74.38 | 71.04..71.69 |
| 0.90 | 73.56..74.44 | 70.99..71.73 |
| 0.95 | 73.47..74.53 | 70.92..71.81 |

Matome, kad jokiu pasitikėjimo lygiu intervalai nesutampa. Tai įrodo mūsų hipotezę, kad pirmieji bazės žaidėjai yra aukštesni nei antrieji bazės žaidėjai.

Formaliau, problema, kurią sprendžiame, yra patikrinti, ar **dvi tikimybių paskirstymo funkcijos yra vienodos**, arba bent jau turi tuos pačius parametrus. Priklausomai nuo paskirstymo, tam reikia naudoti skirtingus testus. Jei žinome, kad mūsų paskirstymai yra normalūs, galime taikyti **[Studento t-testą](https://en.wikipedia.org/wiki/Student%27s_t-test)**.

Studento t-teste apskaičiuojame vadinamąją **t-reikšmę**, kuri nurodo vidurkių skirtumą, atsižvelgiant į dispersiją. Įrodyta, kad t-reikšmė atitinka **studento paskirstymą**, kuris leidžia mums gauti ribinę reikšmę tam tikram pasitikėjimo lygiui **p** (tai galima apskaičiuoti arba rasti skaitmeninėse lentelėse). Tada palyginame t-reikšmę su šia ribine reikšme, kad patvirtintume arba atmestume hipotezę.

Python programoje galime naudoti **SciPy** paketą, kuris apima funkciją `ttest_ind` (be daugelio kitų naudingų statistinių funkcijų!). Ji apskaičiuoja t-reikšmę už mus ir taip pat atlieka atvirkštinį pasitikėjimo p-reikšmės paiešką, kad galėtume tiesiog pažvelgti į pasitikėjimą ir padaryti išvadą.

Pavyzdžiui, mūsų palyginimas tarp pirmųjų ir antrųjų bazės žaidėjų ūgių duoda šiuos rezultatus: 
```python
from scipy.stats import ttest_ind

tval, pval = ttest_ind(df.loc[df['Role']=='First_Baseman',['Height']], df.loc[df['Role']=='Designated_Hitter',['Height']],equal_var=False)
print(f"T-value = {tval[0]:.2f}\nP-value: {pval[0]}")
```
```
T-value = 7.65
P-value: 9.137321189738925e-12
```
Mūsų atveju p-reikšmė yra labai maža, tai reiškia, kad yra stiprūs įrodymai, patvirtinantys, kad pirmieji bazės žaidėjai yra aukštesni.

Taip pat yra kitų hipotezių tipų, kuriuos galime norėti patikrinti, pavyzdžiui:
* Įrodyti, kad tam tikras pavyzdys atitinka tam tikrą paskirstymą. Mūsų atveju mes darėme prielaidą, kad ūgiai yra normaliai paskirstyti, tačiau tai reikia formaliai statistiškai patikrinti.
* Įrodyti, kad pavyzdžio vidutinė reikšmė atitinka tam tikrą iš anksto nustatytą reikšmę
* Palyginti kelių pavyzdžių vidurkius (pvz., koks yra laimės lygio skirtumas tarp skirtingų amžiaus grupių)

## Didelių skaičių dėsnis ir centrinė ribinė teorema

Viena iš priežasčių, kodėl normalus paskirstymas yra toks svarbus, yra vadinamoji **centrinė ribinė teorema**. Tarkime, turime didelį nepriklausomų N reikšmių X<sub>1</sub>, ..., X<sub>N</sub> pavyzdį, paimtą iš bet kokio paskirstymo su vidurkiu μ ir dispersija σ<sup>2</sup>. Tada, kai N yra pakankamai didelis (kitaip tariant, kai N→∞), vidurkis Σ<sub>i</sub>X<sub>i</sub> bus normaliai paskirstytas, su vidurkiu μ ir dispersija σ<sup>2</sup>/N.

> Kitas būdas interpretuoti centrinę ribinę teoremą yra pasakyti, kad nepriklausomai nuo paskirstymo, kai apskaičiuojate bet kokių atsitiktinių kintamųjų reikšmių sumos vidurkį, gaunate normalų paskirstymą.

Iš centrinės ribinės teoremos taip pat išplaukia, kad, kai N→∞, tikimybė, kad pavyzdžio vidurkis bus lygus μ, tampa 1. Tai vadinama **didelių skaičių dėsniu**.

## Kovariacija ir koreliacija

Viena iš duomenų mokslo užduočių yra rasti ryšius tarp duomenų. Sakome, kad dvi sekos **koreliuoja**, kai jos rodo panašų elgesį tuo pačiu metu, t. y. jos arba kyla/krenta kartu, arba viena kyla, kai kita krenta, ir atvirkščiai. Kitaip tariant, atrodo, kad tarp dviejų sekų yra tam tikras ryšys.

> Koreliacija nebūtinai rodo priežastinį ryšį tarp dviejų sekų; kartais abu kintamieji gali priklausyti nuo išorinės priežasties, arba tai gali būti grynas atsitiktinumas, kad dvi sekos koreliuoja. Tačiau stipri matematinė koreliacija yra geras rodiklis, kad du kintamieji yra kažkaip susiję.

Matematiškai pagrindinė sąvoka, rodanti ryšį tarp dviejų atsitiktinių kintamųjų, yra **kovariacija**, kuri apskaičiuojama taip: Cov(X,Y) = **E**\[(X-**E**(X))(Y-**E**(Y))\]. Mes apskaičiuojame abiejų kintamųjų nuokrypį nuo jų vidutinių reikšmių, o tada šių nuokrypių sandaugą. Jei abu kintamieji nukrypsta kartu, sandauga visada bus teigiama reikšmė, kuri prisidės prie teigiamos kovariacijos. Jei abu kintamieji nukrypsta nesinchronizuotai (t. y. vienas nukrenta žemiau vidurkio, kai kitas pakyla virš vidurkio), visada gausime neigiamas reikšmes, kurios prisidės prie neigiamos kovariacijos. Jei nuokrypiai nėra priklausomi, jie maždaug sudarys nulį.

Kovariacijos absoliuti reikšmė nepasako daug apie tai, koks stiprus yra ryšys, nes ji priklauso nuo faktinių reikšmių dydžio. Norėdami ją normalizuoti, galime padalyti kovariaciją iš abiejų kintamųjų standartinio nuokrypio, kad gautume **koreliaciją**. Geras dalykas yra tas, kad koreliacija visada yra intervale [-1,1], kur 1 rodo stiprią teigiamą koreliaciją tarp reikšmių, -1 - stiprią neigiamą koreliaciją, o 0 - jokios koreliacijos (kintamieji yra nepriklausomi).

**Pavyzdys**: Galime apskaičiuoti koreliaciją tarp beisbolo žaidėjų svorių ir ūgių iš aukščiau paminėto duomenų rinkinio:
```python
print(np.corrcoef(weights,heights))
```
Rezultatas yra **koreliacijos matrica**, panaši į šią:
```
array([[1.        , 0.52959196],
       [0.52959196, 1.        ]])
```

> Koreliacijos matrica C gali būti apskaičiuota bet kokiam skaičiui įvesties sekų S<sub>1</sub>, ..., S<sub>n</sub>. C<sub>ij</sub> reikšmė yra koreliacija tarp S<sub>i</sub> ir S<sub>j</sub>, o diagonalės elementai visada yra 1 (tai taip pat yra S<sub>i</sub> savikoreliacija).

Mūsų atveju reikšmė 0.53 rodo, kad yra tam tikra koreliacija tarp žmogaus svorio ir ūgio. Taip pat galime sudaryti sklaidos diagramą, kurioje viena reikšmė vaizduojama prieš kitą, kad vizualiai pamatytume ryšį:

![Ryšys tarp svorio ir ūgio](../../../../1-Introduction/04-stats-and-probability/images/weight-height-relationship.png)

> Daugiau koreliacijos ir kovariacijos pavyzdžių galima rasti [pridedamoje užrašų knygelėje](../../../../1-Introduction/04-stats-and-probability/notebook.ipynb).

## Išvada

Šioje dalyje išmokome:

* pagrindines statistines duomenų savybes, tokias kaip vidurkis, dispersija, moda ir kvartiliai
* skirtingus atsitiktinių kintamųjų paskirstymus, įskaitant normalų paskirstymą
* kaip rasti koreliaciją tarp skirtingų savybių
* kaip naudoti matematikos ir statistikos metodus hipotezėms įrodyti
* kaip apskaičiuoti pasitikėjimo intervalus atsitiktiniam kintamajam, remiantis duomenų pavyzdžiu

Nors tai tikrai nėra išsamus tikimybių ir statistikos temų sąrašas, jis turėtų būti pakankamas, kad suteiktų jums gerą pradžią šiam kursui.

## 🚀 Iššūkis

Naudokite pavyzdinį kodą užrašų knygelėje, kad patikrintumėte kitas hipotezes:
1. Pirmieji bazės žaidėjai yra vyresni nei antrieji bazės žaidėjai
2. Pirmieji bazės žaidėjai yra aukštesni nei trečieji bazės žaidėjai
3. Trumpieji žaidėjai yra aukštesni nei antrieji bazės žaidėjai

## [Po paskaitos testas](https://ff-quizzes.netlify.app/en/ds/quiz/7)

## Peržiūra ir savarankiškas mokymasis

Tikimybė ir statistika yra tokia plati tema, kad ji nusipelno atskiro kurso. Jei norite gilintis į teoriją, galite tęsti skaitydami šias knygas:

1. [Carlos Fernandez-Granda](https://cims.nyu.edu/~cfgranda/) iš Niujorko universiteto turi puikius paskaitų užrašus [Tikimybė ir statistika duomenų mokslui](https://cims.nyu.edu/~cfgranda/pages/stuff/probability_stats_for_DS.pdf) (prieinami internete)
1. [Peter ir Andrew Bruce. Praktinė statistika duomenų mokslininkams.](https://www.oreilly.com/library/view/practical-statistics-for/9781491952955/) [[pavyzdinis kodas R](https://github.com/andrewgbruce/statistics-for-data-scientists)]. 
1. [James D. Miller. Statistika duomenų mokslui](https://www.packtpub.com/product/statistics-for-data-science/9781788290678) [[pavyzdinis kodas R](https://github.com/PacktPublishing/Statistics-for-Data-Science)]

## Užduotis

[Mažas diabeto tyrimas](assignment.md)

## Kreditas

Ši pamoka sukurta su ♥️ [Dmitry Soshnikov](http://soshnikov.com)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius naudojant šį vertimą.