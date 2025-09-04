<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8bbb3fa0d4ad61384a3b4b5f7560226f",
  "translation_date": "2025-09-04T22:18:05+00:00",
  "source_file": "1-Introduction/04-stats-and-probability/README.md",
  "language_code": "hu"
}
-->
# Rövid bevezetés a statisztikába és valószínűségszámításba

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/04-Statistics-Probability.png)|
|:---:|
| Statisztika és valószínűségszámítás - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

A statisztika és a valószínűségszámítás két szorosan összefüggő matematikai terület, amelyek rendkívül fontosak az adatelemzés szempontjából. Bár lehetséges adatokkal dolgozni mély matematikai ismeretek nélkül, mégis hasznos, ha legalább az alapfogalmakkal tisztában vagyunk. Itt egy rövid bevezetőt nyújtunk, amely segít az indulásban.

[![Bevezető videó](../../../../1-Introduction/04-stats-and-probability/images/video-prob-and-stats.png)](https://youtu.be/Z5Zy85g4Yjw)

## [Előadás előtti kvíz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/6)

## Valószínűség és véletlen változók

A **valószínűség** egy 0 és 1 közötti szám, amely kifejezi, hogy egy **esemény** mennyire valószínű. Úgy definiáljuk, mint a pozitív kimenetelek számának (amelyek az eseményhez vezetnek) és az összes lehetséges kimenetel számának hányadosát, feltételezve, hogy minden kimenetel egyformán valószínű. Például, ha dobunk egy kockával, annak a valószínűsége, hogy páros számot kapunk, 3/6 = 0,5.

Amikor eseményekről beszélünk, **véletlen változókat** használunk. Például a véletlen változó, amely a kockadobás eredményét reprezentálja, az 1-től 6-ig terjedő értékeket veheti fel. Az 1-től 6-ig terjedő számok halmazát **minta-térnek** nevezzük. Beszélhetünk egy véletlen változó adott értéket felvevő valószínűségéről, például P(X=3)=1/6.

Az előző példában szereplő véletlen változót **diszkrétnek** nevezzük, mert a minta-tér megszámlálható, azaz különálló értékek sorolhatók fel. Vannak azonban olyan esetek, amikor a minta-tér egy valós számokból álló intervallum, vagy az egész valós számhalmaz. Az ilyen változókat **folytonosnak** nevezzük. Jó példa erre a busz érkezési ideje.

## Valószínűségi eloszlás

Diszkrét véletlen változók esetén könnyű leírni az egyes események valószínűségét egy P(X) függvénnyel. A minta-tér *S* minden egyes *s* értékéhez egy 0 és 1 közötti számot rendelünk, úgy, hogy az összes eseményre vonatkozó P(X=s) értékek összege 1 legyen.

A legismertebb diszkrét eloszlás az **egyenletes eloszlás**, amelyben a minta-tér N elemből áll, és mindegyikük valószínűsége 1/N.

Folytonos változók esetén nehezebb leírni a valószínűségi eloszlást, ha az értékek egy [a,b] intervallumból, vagy az egész valós számhalmazból ℝ származnak. Vegyük például a busz érkezési idejét. Valójában egy adott érkezési időpont *t* esetén annak a valószínűsége, hogy a busz pontosan akkor érkezik, 0!

> Most már tudod, hogy 0 valószínűségű események is előfordulnak, és nagyon gyakran! Legalábbis minden alkalommal, amikor a busz megérkezik!

Csak arról beszélhetünk, hogy egy változó egy adott értéktartományba esik, például P(t<sub>1</sub>≤X<t<sub>2</sub>). Ebben az esetben a valószínűségi eloszlást egy **sűrűségfüggvény** p(x) írja le, amelyre igaz, hogy

![P(t_1\le X<t_2)=\int_{t_1}^{t_2}p(x)dx](../../../../1-Introduction/04-stats-and-probability/images/probability-density.png)

Az egyenletes eloszlás folytonos megfelelőjét **folytonos egyenletes eloszlásnak** nevezzük, amely egy véges intervallumon van definiálva. Annak a valószínűsége, hogy az X érték egy l hosszúságú intervallumba esik, arányos l-lel, és legfeljebb 1 lehet.

Egy másik fontos eloszlás a **normális eloszlás**, amelyről részletesebben az alábbiakban lesz szó.

## Átlag, szórás és variancia

Tegyük fel, hogy egy véletlen változó X n mintáját vesszük: x<sub>1</sub>, x<sub>2</sub>, ..., x<sub>n</sub>. Az **átlagot** (vagy **számtani közepet**) a hagyományos módon definiálhatjuk: (x<sub>1</sub>+x<sub>2</sub>+...+x<sub>n</sub>)/n. Ha növeljük a minta méretét (azaz n→∞), megkapjuk az eloszlás átlagát (más néven **várható értékét**). A várható értéket **E**(x)-szel jelöljük.

> Kimutatható, hogy bármely diszkrét eloszlás esetén, amelynek értékei {x<sub>1</sub>, x<sub>2</sub>, ..., x<sub>N</sub>} és megfelelő valószínűségei p<sub>1</sub>, p<sub>2</sub>, ..., p<sub>N</sub>, a várható érték E(X)=x<sub>1</sub>p<sub>1</sub>+x<sub>2</sub>p<sub>2</sub>+...+x<sub>N</sub>p<sub>N</sub>.

Az értékek szóródásának meghatározásához kiszámíthatjuk a varianciát: σ<sup>2</sup> = ∑(x<sub>i</sub> - μ)<sup>2</sup>/n, ahol μ a minta átlaga. A σ értéket **szórásnak**, a σ<sup>2</sup>-et pedig **varianciának** nevezzük.

## Módusz, medián és kvartilisek

Az átlag nem mindig ad megfelelő képet az "átlagos" értékről. Például, ha néhány szélsőséges érték jelentősen eltér a többitől, ezek befolyásolhatják az átlagot. Egy másik jó mutató a **medián**, amely olyan érték, amelynél az adatok fele kisebb, a másik fele pedig nagyobb.

Az adatok eloszlásának megértéséhez hasznos a **kvartilisekről** beszélni:

* Az első kvartilis (Q1) az az érték, amely alatt az adatok 25%-a található.
* A harmadik kvartilis (Q3) az az érték, amely alatt az adatok 75%-a található.

Grafikusan a medián és a kvartilisek kapcsolatát egy **dobozdiagramon** (box plot) ábrázolhatjuk:

<img src="images/boxplot_explanation.png" width="50%"/>

Itt kiszámítjuk az **interkvartilis tartományt** (IQR=Q3-Q1), valamint az úgynevezett **kiugró értékeket** - azokat az értékeket, amelyek a [Q1-1.5*IQR, Q3+1.5*IQR] határokon kívül esnek.

Ha az eloszlás véges és kevés lehetséges értéket tartalmaz, egy jó "tipikus" érték az, amely a leggyakrabban fordul elő, ezt nevezzük **módusznak**. Ez gyakran alkalmazható kategóriákra, például színekre. Vegyünk egy példát, ahol két csoport van: az egyik a pirosat, a másik a kéket részesíti előnyben. Ha a színeket számokkal kódoljuk, az átlagos kedvenc szín valahol a narancs-zöld spektrumban lenne, ami egyik csoport preferenciáját sem tükrözi. A módusz viszont vagy az egyik szín, vagy mindkettő lehet, ha azonos számú ember szavaz rájuk (ebben az esetben az eloszlást **multimodálisnak** nevezzük).

## Valós adatok

Amikor valós életből származó adatokat elemzünk, azok gyakran nem tekinthetők véletlen változóknak abban az értelemben, hogy nem ismeretlen eredményű kísérletek eredményei. Például vegyünk egy baseballcsapatot, és az ő testadataikat, mint például magasság, súly és életkor. Ezek a számok nem teljesen véletlenek, de ugyanazokat a matematikai fogalmakat alkalmazhatjuk rájuk. Például az emberek súlyának sorozata tekinthető egy véletlen változóból származó értékek sorozatának. Az alábbiakban a [Major League Baseball](http://mlb.mlb.com/index.jsp) játékosainak súlyadatai láthatók, amelyeket [ebből az adatbázisból](http://wiki.stat.ucla.edu/socr/index.php/SOCR_Data_MLB_HeightsWeights) vettünk (a könnyebb érthetőség kedvéért csak az első 20 értéket mutatjuk):

```
[180.0, 215.0, 210.0, 210.0, 188.0, 176.0, 209.0, 200.0, 231.0, 180.0, 188.0, 180.0, 185.0, 160.0, 180.0, 185.0, 197.0, 189.0, 185.0, 219.0]
```

> **Megjegyzés**: Ha szeretnéd látni, hogyan dolgozhatsz ezzel az adathalmazzal, nézd meg a [kapcsolódó notebookot](../../../../1-Introduction/04-stats-and-probability/notebook.ipynb). Az óra során számos kihívás is található, amelyeket a notebookhoz kód hozzáadásával oldhatsz meg. Ha nem vagy biztos abban, hogyan kell adatokat kezelni, ne aggódj - később visszatérünk az adatok Pythonban történő feldolgozására. Ha nem tudod, hogyan futtass kódot Jupyter Notebookban, olvasd el [ezt a cikket](https://soshnikov.com/education/how-to-execute-notebooks-from-github/).

Itt látható egy dobozdiagram, amely bemutatja az adatok átlagát, mediánját és kvartilisét:

![Súly dobozdiagram](../../../../1-Introduction/04-stats-and-probability/images/weight-boxplot.png)

Mivel adataink különböző játékos **szerepekről** tartalmaznak információt, készíthetünk szerepek szerinti dobozdiagramot is - ez lehetővé teszi, hogy képet kapjunk arról, hogyan különböznek az értékek a szerepek között. Ezúttal a magasságot vizsgáljuk:

![Dobozdiagram szerepek szerint](../../../../1-Introduction/04-stats-and-probability/images/boxplot_byrole.png)

Ez a diagram azt sugallja, hogy az első bázisjátékosok átlagos magassága nagyobb, mint a második bázisjátékosoké. Később az órán megtanuljuk, hogyan tesztelhetjük ezt a hipotézist formálisabban, és hogyan bizonyíthatjuk, hogy adataink statisztikailag szignifikánsak.

> Amikor valós adatokkal dolgozunk, feltételezzük, hogy minden adatpont egy valószínűségi eloszlásból származó minta. Ez a feltételezés lehetővé teszi számunkra, hogy gépi tanulási technikákat alkalmazzunk és működő prediktív modelleket építsünk.

Adataink eloszlásának megismeréséhez készíthetünk egy **hisztogramot**. Az X-tengely különböző súlyintervallumokat (úgynevezett **bin-eket**) tartalmaz, míg a függőleges tengely azt mutatja, hogy a véletlen változó mintája hányszor esett egy adott intervallumba.

![Valós adatok hisztogramja](../../../../1-Introduction/04-stats-and-probability/images/weight-histogram.png)

Ebből a hisztogramból látható, hogy az összes érték egy bizonyos átlagos súly körül koncentrálódik, és minél távolabb megyünk ettől a súlytól, annál kevesebb ilyen érték fordul elő. Azaz nagyon valószínűtlen, hogy egy baseballjátékos súlya jelentősen eltér az átlagtól. A súlyok szórása azt mutatja, hogy a súlyok mennyire térhetnek el az átlagtól.

> Ha más emberek, például egyetemi hallgatók súlyát vizsgálnánk, az eloszlás valószínűleg eltérő lenne. Azonban az eloszlás alakja ugyanaz maradna, csak az átlag és a szórás változna. Tehát, ha modellünket baseballjátékosokon képezzük, valószínűleg rossz eredményeket adna, ha egyetemistákra alkalmaznánk, mert az alapul szolgáló eloszlás eltérő.

## Normális eloszlás

A fent látott súlyeloszlás nagyon tipikus, és sok valós mérést ugyanilyen típusú eloszlás követ, de eltérő átlaggal és szórással. Ezt az eloszlást **normális eloszlásnak** nevezzük, és nagyon fontos szerepet játszik a statisztikában.

A normális eloszlás helyes módja a potenciális baseballjátékosok véletlenszerű súlyainak generálására. Ha ismerjük az átlagos súlyt `mean` és a szórást `std`, akkor 1000 súlymintát generálhatunk az alábbi módon:
```python
samples = np.random.normal(mean,std,1000)
``` 

Ha a generált minták hisztogramját ábrázoljuk, nagyon hasonló képet kapunk a fentiekhez. Ha növeljük a minták és a bin-ek számát, egyre inkább megközelítjük az ideális normális eloszlás képét:

![Normális eloszlás átlag=0 és szórás=1](../../../../1-Introduction/04-stats-and-probability/images/normal-histogram.png)

*Normális eloszlás átlag=0 és szórás=1*

## Konfidencia intervallumok

Amikor a baseballjátékosok súlyáról beszélünk, feltételezzük, hogy létezik egy bizonyos **W véletlen változó**, amely az összes baseballjátékos súlyának ideális valószínűségi eloszlásának felel meg (az úgynevezett **populáció**). A súlyaink sorozata az összes baseballjátékos egy részhalmazának felel meg, amelyet **mintának** nevezünk. Egy érdekes kérdés az, hogy megismerhetjük-e a W eloszlásának paramétereit, azaz a populáció átlagát és szórását?

A legegyszerűbb válasz az lenne, hogy kiszámítjuk a minta átlagát és szórását. Azonban előfordulhat, hogy a véletlen mintánk nem pontosan reprezentálja a teljes populációt. Ezért van értelme **konfidencia intervallumokról** beszélni.
> **Konfidencia intervallum** a populáció valódi átlagának becslése a mintánk alapján, amely egy bizonyos valószínűséggel (vagyis egy **bizonyossági szinttel**) pontos.
Tegyük fel, hogy van egy mintánk X<sub>1</sub>, ..., X<sub>n</sub> az eloszlásunkból. Minden alkalommal, amikor mintát veszünk az eloszlásunkból, más átlagértéket, μ-t kapunk. Így μ tekinthető véletlen változónak. Egy **konfidencia intervallum** p konfidenciaszinttel egy (L<sub>p</sub>,R<sub>p</sub>) értékpár, amelyre **P**(L<sub>p</sub>≤μ≤R<sub>p</sub>) = p, azaz annak valószínűsége, hogy a mért átlagérték az intervallumba esik, p-vel egyenlő.

Rövid bevezetőnk keretein túlmutat, hogy részletesen tárgyaljuk, hogyan számítják ki ezeket a konfidencia intervallumokat. További részletek találhatók [a Wikipédián](https://en.wikipedia.org/wiki/Confidence_interval). Röviden, meghatározzuk a számított mintaátlag eloszlását a populáció valódi átlagához viszonyítva, amit **Student-eloszlásnak** neveznek.

> **Érdekes tény**: A Student-eloszlást William Sealy Gosset matematikusról nevezték el, aki "Student" álnéven publikálta tanulmányát. Gosset a Guinness sörgyárban dolgozott, és az egyik verzió szerint munkáltatója nem akarta, hogy a nagyközönség tudomást szerezzen arról, hogy statisztikai teszteket használnak a nyersanyagok minőségének meghatározására.

Ha a populációnk átlagát, μ-t szeretnénk p konfidenciaszinttel becsülni, akkor a Student-eloszlás *(1-p)/2-edik percentilisét* kell vennünk, amelyet táblázatokból vagy statisztikai szoftverek (pl. Python, R stb.) beépített függvényeivel lehet kiszámítani. Ekkor az μ intervalluma X±A*D/√n lesz, ahol X a minta kapott átlaga, D a szórás.

> **Megjegyzés**: Nem tárgyaljuk részletesen a [szabadságfokok](https://en.wikipedia.org/wiki/Degrees_of_freedom_(statistics)) fontos fogalmát, amely a Student-eloszlással kapcsolatban lényeges. A statisztika átfogóbb könyveiben mélyebben megértheted ezt a fogalmat.

Egy példát a súlyok és magasságok konfidencia intervallumának kiszámítására az [mellékelt jegyzetfüzetben](../../../../1-Introduction/04-stats-and-probability/notebook.ipynb) találhatsz.

| p    | Súly átlaga |
|------|-------------|
| 0.85 | 201.73±0.94 |
| 0.90 | 201.73±1.08 |
| 0.95 | 201.73±1.28 |

Figyeld meg, hogy minél magasabb a konfidencia valószínűsége, annál szélesebb a konfidencia intervallum.

## Hipotézisvizsgálat

A baseball játékosok adatbázisában különböző játékos szerepek találhatók, amelyeket az alábbi táblázatban foglalhatunk össze (nézd meg az [mellékelt jegyzetfüzetet](../../../../1-Introduction/04-stats-and-probability/notebook.ipynb), hogy láthatod, hogyan számítható ki ez a táblázat):

| Szerep             | Magasság | Súly   | Darabszám |
|--------------------|----------|--------|-----------|
| Catcher           | 72.723684 | 204.328947 | 76        |
| Designated_Hitter | 74.222222 | 220.888889 | 18        |
| First_Baseman     | 74.000000 | 213.109091 | 55        |
| Outfielder        | 73.010309 | 199.113402 | 194       |
| Relief_Pitcher    | 74.374603 | 203.517460 | 315       |
| Second_Baseman    | 71.362069 | 184.344828 | 58        |
| Shortstop         | 71.903846 | 182.923077 | 52        |
| Starting_Pitcher  | 74.719457 | 205.163636 | 221       |
| Third_Baseman     | 73.044444 | 200.955556 | 45        |

Láthatjuk, hogy az első bázisjátékosok átlagos magassága nagyobb, mint a második bázisjátékosoké. Ezért kísértésbe eshetünk, hogy azt a következtetést vonjuk le, hogy **az első bázisjátékosok magasabbak, mint a második bázisjátékosok**.

> Ezt az állítást **hipotézisnek** nevezzük, mert nem tudjuk, hogy a tény valóban igaz-e vagy sem.

Azonban nem mindig egyértelmű, hogy levonhatjuk-e ezt a következtetést. Az előzőekben tárgyaltakból tudjuk, hogy minden átlagnak van egy hozzá tartozó konfidencia intervalluma, így ez a különbség lehet pusztán statisztikai hiba is. Szükségünk van egy formálisabb módszerre a hipotézis teszteléséhez.

Számítsuk ki külön az első és második bázisjátékosok magasságának konfidencia intervallumait:

| Konfidencia | Első bázisjátékosok | Második bázisjátékosok |
|-------------|---------------------|------------------------|
| 0.85        | 73.62..74.38       | 71.04..71.69          |
| 0.90        | 73.56..74.44       | 70.99..71.73          |
| 0.95        | 73.47..74.53       | 70.92..71.81          |

Láthatjuk, hogy egyik konfidenciaszintnél sem fedik át egymást az intervallumok. Ez bizonyítja a hipotézisünket, hogy az első bázisjátékosok magasabbak, mint a második bázisjátékosok.

Formálisabban, a probléma, amit megoldunk, az annak vizsgálata, hogy **két valószínűségi eloszlás azonos-e**, vagy legalábbis azonos paraméterekkel rendelkezik-e. Az eloszlástól függően különböző teszteket kell alkalmaznunk. Ha tudjuk, hogy az eloszlásaink normálisak, alkalmazhatjuk a **[Student t-tesztet](https://en.wikipedia.org/wiki/Student%27s_t-test)**.

A Student t-tesztben kiszámítjuk az úgynevezett **t-értéket**, amely az átlagok közötti különbséget jelzi, figyelembe véve a szórást. Kimutatták, hogy a t-érték követi a **Student-eloszlást**, amely lehetővé teszi, hogy egy adott konfidenciaszinthez **p** küszöbértéket kapjunk (ez kiszámítható vagy numerikus táblázatokból kikereshető). Ezután összehasonlítjuk a t-értéket ezzel a küszöbértékkel, hogy elfogadjuk vagy elutasítsuk a hipotézist.

Pythonban használhatjuk a **SciPy** csomagot, amely tartalmazza a `ttest_ind` függvényt (sok más hasznos statisztikai függvény mellett!). Ez kiszámítja nekünk a t-értéket, és fordítottan megkeresi a konfidencia p-értékét is, így egyszerűen a konfidenciát nézve levonhatjuk a következtetést.

Például az első és második bázisjátékosok magasságának összehasonlítása a következő eredményeket adja:  
```python
from scipy.stats import ttest_ind

tval, pval = ttest_ind(df.loc[df['Role']=='First_Baseman',['Height']], df.loc[df['Role']=='Designated_Hitter',['Height']],equal_var=False)
print(f"T-value = {tval[0]:.2f}\nP-value: {pval[0]}")
```  
```
T-value = 7.65
P-value: 9.137321189738925e-12
```  
Esetünkben a p-érték nagyon alacsony, ami azt jelenti, hogy erős bizonyíték van arra, hogy az első bázisjátékosok magasabbak.

További hipotézisek, amelyeket tesztelhetünk:
* Annak bizonyítása, hogy egy adott minta követ egy eloszlást. Esetünkben feltételeztük, hogy a magasságok normális eloszlásúak, de ezt formálisan is igazolni kell.
* Annak bizonyítása, hogy egy minta átlagértéke megfelel egy előre meghatározott értéknek.
* Több minta átlagának összehasonlítása (pl. milyen különbségek vannak a boldogsági szintek között különböző korcsoportokban).

## Nagy számok törvénye és központi határeloszlás tétel

Az egyik ok, amiért a normális eloszlás olyan fontos, az az úgynevezett **központi határeloszlás tétel**. Tegyük fel, hogy van egy nagy, független N értékből álló mintánk X<sub>1</sub>, ..., X<sub>N</sub>, amely bármilyen eloszlásból származik, átlag μ-val és szórás σ<sup>2</sup>-vel. Ekkor, ha N elég nagy (más szavakkal, amikor N→∞), az átlag Σ<sub>i</sub>X<sub>i</sub> normális eloszlású lesz, átlag μ-val és szórás σ<sup>2</sup>/N-nel.

> A központi határeloszlás tétel másik értelmezése az, hogy függetlenül az eloszlástól, ha bármilyen véletlen változók összegének átlagát számítjuk, normális eloszlást kapunk.

A központi határeloszlás tételből az is következik, hogy amikor N→∞, a mintaátlag μ-hoz való valószínűsége 1 lesz. Ezt nevezzük **nagy számok törvényének**.

## Kovariancia és korreláció

Az egyik dolog, amit az adatelemzés során keresünk, az adatok közötti kapcsolatok megtalálása. Azt mondjuk, hogy két sorozat **korrelál**, ha hasonló viselkedést mutatnak egyidejűleg, azaz egyszerre emelkednek/csökkennek, vagy az egyik emelkedik, amikor a másik csökken, és fordítva. Más szavakkal, úgy tűnik, hogy van valamilyen kapcsolat a két sorozat között.

> A korreláció nem feltétlenül jelenti azt, hogy a két sorozat között ok-okozati kapcsolat van; néha mindkét változó valamilyen külső oknak van alávetve, vagy pusztán véletlen, hogy a két sorozat korrelál. Azonban az erős matematikai korreláció jó jelzés arra, hogy a két változó valamilyen módon összefügg.

Matematikailag a két véletlen változó közötti kapcsolatot mutató fő fogalom a **kovariancia**, amelyet így számítunk ki: Cov(X,Y) = **E**\[(X-**E**(X))(Y-**E**(Y))\]. Kiszámítjuk mindkét változó eltérését az átlagértéküktől, majd ezeknek az eltéréseknek a szorzatát. Ha mindkét változó együtt tér el, a szorzat mindig pozitív érték lesz, ami pozitív kovarianciát eredményez. Ha mindkét változó eltérése nincs szinkronban (azaz az egyik az átlag alá esik, amikor a másik az átlag fölé emelkedik), mindig negatív számokat kapunk, amelyek negatív kovarianciát eredményeznek. Ha az eltérések nem függenek össze, akkor nagyjából nullát kapunk.

A kovariancia abszolút értéke nem sokat mond arról, hogy mekkora a korreláció, mert az az aktuális értékek nagyságától függ. Ennek normalizálásához eloszthatjuk a kovarianciát mindkét változó szórásával, hogy megkapjuk a **korrelációt**. A jó hír az, hogy a korreláció mindig [-1,1] tartományban van, ahol 1 erős pozitív korrelációt, -1 erős negatív korrelációt, és 0 semmilyen korrelációt (függetlenséget) jelez.

**Példa**: Számítsuk ki a baseball játékosok súlya és magassága közötti korrelációt az említett adatbázisból:
```python
print(np.corrcoef(weights,heights))
```  
Ennek eredményeként egy **korrelációs mátrixot** kapunk, például ilyet:  
```
array([[1.        , 0.52959196],
       [0.52959196, 1.        ]])
```  

> A korrelációs mátrix C bármilyen számú bemeneti sorozatra S<sub>1</sub>, ..., S<sub>n</sub> kiszámítható. A C<sub>ij</sub> értéke az S<sub>i</sub> és S<sub>j</sub> közötti korreláció, és a diagonális elemek mindig 1-ek (ami az S<sub>i</sub> önkorrelációja).

Esetünkben a 0.53 érték azt jelzi, hogy van némi korreláció egy személy súlya és magassága között. Készíthetünk egy szórásdiagramot is, amely az egyik értéket a másik ellen ábrázolja, hogy vizuálisan lássuk a kapcsolatot:

![Kapcsolat a súly és magasság között](../../../../1-Introduction/04-stats-and-probability/images/weight-height-relationship.png)

> További példák a korrelációra és kovarianciára az [mellékelt jegyzetfüzetben](../../../../1-Introduction/04-stats-and-probability/notebook.ipynb) találhatók.

## Következtetés

Ebben a szakaszban megtanultuk:

* az adatok alapvető statisztikai tulajdonságait, mint az átlag, szórás, módusz és kvartilisek
* a véletlen változók különböző eloszlásait, beleértve a normális eloszlást
* hogyan találjuk meg a különböző tulajdonságok közötti korrelációt
* hogyan használjuk a matematika és statisztika megalapozott eszközeit hipotézisek bizonyítására
* hogyan számítsunk konfidencia intervallumokat véletlen változókhoz adott minta alapján

Bár ez nem kimerítő lista a valószínűség és statisztika témakörében, elegendő alapot nyújt a kurzus folytatásához.

## 🚀 Kihívás

Használd a jegyzetfüzetben található mintakódot az alábbi hipotézisek tesztelésére:
1. Az első bázisjátékosok idősebbek, mint a második bázisjátékosok.
2. Az első bázisjátékosok magasabbak, mint a harmadik bázisjátékosok.
3. A shortstopok magasabbak, mint a második bázisjátékosok.

## [Előadás utáni kvíz](https://ff-quizzes.netlify.app/en/ds/)

## Áttekintés és önálló tanulás

A valószínűség és statisztika olyan széleskörű téma, hogy megérdemel egy külön kurzust. Ha mélyebben szeretnél elmerülni az elméletben, érdemes lehet folytatni az alábbi könyvek olvasását:

1. [Carlos Fernandez-Granda](https://cims.nyu.edu/~cfgranda/) a New York-i Egyetemről nagyszerű előadásjegyzeteket készített [Probability and Statistics for Data Science](https://cims.nyu.edu/~cfgranda/pages/stuff/probability_stats_for_DS.pdf) címmel (elérhető online).
2. [Peter és Andrew Bruce. Practical Statistics for Data Scientists.](https://www.oreilly.com/library/view/practical-statistics-for/9781491952955/) [[mintakód R-ben](https://github.com/andrewgbruce/statistics-for-data-scientists)].
3. [James D. Miller. Statistics for Data Science](https://www.packtpub.com/product/statistics-for-data-science/9781788290678) [[mintakód R-ben](https://github.com/PacktPublishing/Statistics-for-Data-Science)].

## Feladat

[Kis diabétesz tanulmány](assignment.md)

## Köszönetnyilvánítás

Ezt a leckét ♥️-vel készítette [Dmitry Soshnikov](http://soshnikov.com).

---

**Felelősségkizárás**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével készült. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális, emberi fordítást igénybe venni. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.