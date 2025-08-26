<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b706a07cfa87ba091cbb91e0aa775600",
  "translation_date": "2025-08-26T15:33:54+00:00",
  "source_file": "1-Introduction/04-stats-and-probability/README.md",
  "language_code": "hu"
}
-->
# A statisztika és a valószínűség rövid bemutatása

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/04-Statistics-Probability.png)|
|:---:|
| Statisztika és valószínűség - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

A statisztika és a valószínűségelmélet a matematika két szorosan összefüggő területe, amelyek kiemelten fontosak az adatelemzés szempontjából. Bár lehetséges adatokkal dolgozni mély matematikai ismeretek nélkül, mégis hasznos, ha legalább az alapfogalmakat ismerjük. Ebben a rövid bevezetőben bemutatjuk az induláshoz szükséges alapokat.

[![Bevezető videó](../../../../translated_images/video-prob-and-stats.e4282e5efa2f2543400843ed98b1057065c9600cebfc8a728e8931b5702b2ae4.hu.png)](https://youtu.be/Z5Zy85g4Yjw)

## [Előadás előtti kvíz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/6)

## Valószínűség és véletlen változók

**Valószínűség** egy 0 és 1 közötti szám, amely kifejezi, hogy egy **esemény** mennyire valószínű. Úgy definiáljuk, mint a pozitív kimenetelek számát (amelyek az eseményhez vezetnek), osztva az összes lehetséges kimenetel számával, feltételezve, hogy minden kimenetel egyformán valószínű. Például, ha dobunk egy kockával, annak a valószínűsége, hogy páros számot kapunk, 3/6 = 0,5.

Amikor eseményekről beszélünk, **véletlen változókat** használunk. Például a véletlen változó, amely a kockadobás eredményét reprezentálja, 1-től 6-ig terjedő értékeket vehet fel. Az 1-től 6-ig terjedő számok halmazát **minta-térnek** nevezzük. Beszélhetünk annak a valószínűségéről, hogy egy véletlen változó egy adott értéket vesz fel, például P(X=3)=1/6.

Az előző példában szereplő véletlen változót **diszkrétnek** nevezzük, mert számlálható minta-térrel rendelkezik, azaz különálló értékek vannak, amelyeket felsorolhatunk. Vannak olyan esetek, amikor a minta-tér valós számok egy tartománya, vagy az egész valós számhalmaz. Az ilyen változókat **folytonosnak** nevezzük. Jó példa erre a busz érkezési ideje.

## Valószínűségi eloszlás

Diszkrét véletlen változók esetén könnyű leírni az egyes események valószínűségét egy P(X) függvénnyel. A minta-tér *S* minden *s* értékére egy 0 és 1 közötti számot ad, úgy, hogy az összes P(X=s) érték összege minden eseményre 1 legyen.

A legismertebb diszkrét eloszlás az **egyenletes eloszlás**, amelyben a minta-tér N elemből áll, és mindegyikük valószínűsége 1/N.

Folytonos változók esetén nehezebb leírni a valószínűségi eloszlást, ha az értékek egy [a,b] intervallumból, vagy az egész valós számhalmazból ℝ származnak. Vegyük például a busz érkezési idejét. Valójában minden pontos érkezési idő *t* esetén annak a valószínűsége, hogy a busz pontosan akkor érkezik, 0!

> Most már tudod, hogy 0 valószínűségű események is megtörténnek, és nagyon gyakran! Legalábbis minden alkalommal, amikor a busz megérkezik!

Csak arról beszélhetünk, hogy egy változó egy adott értéktartományba esik, például P(t<sub>1</sub>≤X<t<sub>2</sub>). Ebben az esetben a valószínűségi eloszlást egy **valószínűségi sűrűségfüggvény** p(x) írja le, amelyre igaz, hogy

![P(t_1\le X<t_2)=\int_{t_1}^{t_2}p(x)dx](../../../../translated_images/probability-density.a8aad29f17a14afb519b407c7b6edeb9f3f9aa5f69c9e6d9445f604e5f8a2bf7.hu.png)

Az egyenletes eloszlás folytonos analógját **folytonos egyenletes eloszlásnak** nevezzük, amely egy véges intervallumon van definiálva. Annak a valószínűsége, hogy az X érték egy l hosszúságú intervallumba esik, arányos l-lel, és legfeljebb 1 lehet.

Egy másik fontos eloszlás a **normális eloszlás**, amelyről később részletesebben beszélünk.

## Átlag, szórás és standard deviáció

Tegyük fel, hogy egy véletlen változó X n mintáját vesszük: x<sub>1</sub>, x<sub>2</sub>, ..., x<sub>n</sub>. Az értékek **átlagát** (vagy **aritmetikai közepét**) hagyományos módon definiálhatjuk: (x<sub>1</sub>+x<sub>2</sub>+x<sub>n</sub>)/n. Ahogy növeljük a minta méretét (azaz n→∞ határértéket veszünk), megkapjuk az eloszlás átlagát (más néven **várható értékét**). A várható értéket **E**(x)-szel jelöljük.

> Kimutatható, hogy bármely diszkrét eloszlás esetén, amelynek értékei {x<sub>1</sub>, x<sub>2</sub>, ..., x<sub>N</sub>} és megfelelő valószínűségei p<sub>1</sub>, p<sub>2</sub>, ..., p<sub>N</sub>, a várható érték E(X)=x<sub>1</sub>p<sub>1</sub>+x<sub>2</sub>p<sub>2</sub>+...+x<sub>N</sub>p<sub>N</sub>.

Annak meghatározására, hogy az értékek mennyire szóródnak, kiszámíthatjuk a szórást: σ<sup>2</sup> = ∑(x<sub>i</sub> - μ)<sup>2</sup>/n, ahol μ a sorozat átlaga. Az értéket **standard deviációnak** nevezzük, míg σ<sup>2</sup>-t **varianciának**.

## Módusz, medián és kvartilisek

Az átlag nem mindig tükrözi megfelelően az "általános" értéket az adatokban. Például, ha néhány szélsőséges érték teljesen kilóg a tartományból, ezek befolyásolhatják az átlagot. Egy másik jó mutató a **medián**, egy olyan érték, amelynél az adatok fele kisebb, a másik fele pedig nagyobb.

Az adatok eloszlásának megértéséhez hasznos a **kvartilisekről** beszélni:

* Az első kvartilis, vagy Q1, egy olyan érték, amelynél az adatok 25%-a alatta van
* A harmadik kvartilis, vagy Q3, egy olyan érték, amelynél az adatok 75%-a alatta van

Grafikusan a medián és a kvartilisek kapcsolatát egy **box plot** diagramon ábrázolhatjuk:

<img src="images/boxplot_explanation.png" width="50%"/>

Itt kiszámítjuk az **interkvartilis tartományt** IQR=Q3-Q1, valamint az úgynevezett **kiugró értékeket** - azokat az értékeket, amelyek kívül esnek a [Q1-1.5*IQR,Q3+1.5*IQR] határokon.

Ha az eloszlás véges, és csak kis számú lehetséges értéket tartalmaz, egy jó "általános" érték az, amely a leggyakrabban fordul elő, ezt nevezzük **módusznak**. Gyakran alkalmazzák kategóriákra, például színekre. Vegyünk egy helyzetet, amikor két csoport van - az egyik erősen kedveli a pirosat, a másik pedig a kéket. Ha a színeket számokkal kódoljuk, a kedvenc szín átlagértéke valahol a narancs-zöld spektrumban lenne, ami nem tükrözi egyik csoport tényleges preferenciáját sem. A módusz viszont vagy az egyik szín, vagy mindkettő lehet, ha az emberek száma, akik azokat választják, egyenlő (ebben az esetben az eloszlást **multimodálisnak** nevezzük).

## Valós adatok

Amikor valós adatokat elemzünk, gyakran nem véletlen változókról van szó abban az értelemben, hogy nem végezünk kísérleteket ismeretlen eredménnyel. Például vegyünk egy baseballcsapatot, és az ő testadataikat, mint magasság, súly és életkor. Ezek a számok nem teljesen véletlenek, de mégis alkalmazhatjuk rájuk ugyanazokat a matematikai fogalmakat. Például az emberek súlyának sorozata tekinthető egy véletlen változóból származó értékek sorozatának. Az alábbiakban a baseball játékosok súlyának sorozata látható a [Major League Baseball](http://mlb.mlb.com/index.jsp) csapatából, amelyet [ebből az adatbázisból](http://wiki.stat.ucla.edu/socr/index.php/SOCR_Data_MLB_HeightsWeights) vettünk (a könnyebb érthetőség kedvéért csak az első 20 érték van megadva):

```
[180.0, 215.0, 210.0, 210.0, 188.0, 176.0, 209.0, 200.0, 231.0, 180.0, 188.0, 180.0, 185.0, 160.0, 180.0, 185.0, 197.0, 189.0, 185.0, 219.0]
```

> **Note**: Ha szeretnéd látni, hogyan dolgozhatsz ezzel az adatbázissal, nézd meg a [kapcsolódó notebookot](notebook.ipynb). Az órán számos kihívás található, amelyeket úgy oldhatsz meg, hogy kódot adsz hozzá a notebookhoz. Ha nem vagy biztos abban, hogyan kell adatokat kezelni, ne aggódj - később visszatérünk az adatok Python segítségével történő feldolgozásához. Ha nem tudod, hogyan kell kódot futtatni Jupyter Notebookban, olvasd el [ezt a cikket](https://soshnikov.com/education/how-to-execute-notebooks-from-github/).

Itt látható a box plot, amely az átlagot, mediánt és kvartiliseket mutatja az adatainkhoz:

![Súly Box Plot](../../../../translated_images/weight-boxplot.1dbab1c03af26f8a008fff4e17680082c8ab147d6df646cbac440bbf8f5b9c42.hu.png)

Mivel adataink különböző játékos **szerepekről** tartalmaznak információt, készíthetünk box plotot szerepek szerint is - ez lehetővé teszi, hogy megértsük, hogyan különböznek az értékek szerepek szerint. Ezúttal a magasságot vizsgáljuk:

![Box plot szerepek szerint](../../../../translated_images/boxplot_byrole.036b27a1c3f52d42f66fba2324ec5cde0a1bca6a01a619eeb0ce7cd054b2527b.hu.png)

Ez a diagram azt sugallja, hogy átlagosan az első bázisjátékosok magassága nagyobb, mint a második bázisjátékosoké. Később az órán megtanuljuk, hogyan tesztelhetjük ezt a hipotézist formálisabban, és hogyan mutathatjuk ki, hogy adataink statisztikailag jelentősek-e ennek bizonyítására.

> Valós adatokkal dolgozva feltételezzük, hogy minden adatpont egy valószínűségi eloszlásból származó minta. Ez a feltételezés lehetővé teszi számunkra, hogy gépi tanulási technikákat alkalmazzunk és működő prediktív modelleket építsünk.

Az adatok eloszlásának megértéséhez készíthetünk egy **hisztogramot**. Az X-tengelyen különböző súlytartományok (úgynevezett **bin-ek**) szerepelnek, míg a függőleges tengelyen azt mutatjuk, hogy hányszor esett a véletlen változó mintája egy adott tartományba.

![Valós adatok hisztogramja](../../../../translated_images/weight-histogram.bfd00caf7fc30b145b21e862dba7def41c75635d5280de25d840dd7f0b00545e.hu.png)

Ebből a hisztogramból látható, hogy az összes érték egy bizonyos átlagos súly köré csoportosul, és minél távolabb megyünk ettől a súlytól, annál kevesebb ilyen érték fordul elő. Azaz nagyon valószínűtlen, hogy egy baseball játékos súlya jelentősen eltér az átlagos súlytól. A súlyok varianciája megmutatja, hogy mennyire valószínű, hogy a súlyok eltérnek az átlagtól.

> Ha más emberek, például egyetemi hallgatók súlyát vizsgáljuk, az eloszlás valószínűleg eltérő lesz. Azonban az eloszlás alakja ugyanaz marad, csak az átlag és a variancia változik. Tehát, ha a modellünket baseball játékosokon tanítjuk, valószínűleg rossz eredményeket ad, ha egyetemi hallgatókra alkalmazzuk, mert az alapul szolgáló eloszlás eltérő.

## Normális eloszlás

A súlyok eloszlása, amelyet fentebb láttunk, nagyon tipikus, és sok valós mérések ugyanilyen típusú eloszlást követnek, de eltérő átlaggal és varianciával. Ezt az eloszlást **normális eloszlásnak** nevezzük, és nagyon fontos szerepet játszik a statisztikában.

A normális eloszlás használata helyes módja annak, hogy véletlenszerű súlyokat generáljunk potenciális baseball játékosok számára. Ha ismerjük az átlagos súlyt `mean` és a standard deviációt `std`, 1000 súlymintát generálhatunk az alábbi módon:
```python
samples = np.random.normal(mean,std,1000)
``` 

Ha a generált minták hisztogramját ábrázoljuk, nagyon hasonló képet kapunk, mint amit fentebb láttunk. Ha növeljük a minták számát és a bin-ek számát, egy ideális normális eloszlás képét kapjuk:

![Normális eloszlás átlag=0 és std.dev=1](../../../../translated_images/normal-histogram.dfae0d67c202137d552d0015fb87581eca263925e512404f3c12d8885315432e.hu.png)

*Normális eloszlás átlag=0 és std.dev=1*

## Konfidencia intervallumok

Amikor a baseball játékosok súlyáról beszélünk, feltételezzük, hogy létezik egy **W véletlen változó**, amely az összes baseball játékos súlyának ideális valószínűségi eloszlását (úgynevezett **populációt**) képviseli. A súlyok sorozata az összes baseball játékos egy részhalmazának felel meg, amelyet **mintának** nevezünk. Érdekes kérdés, hogy meg tudjuk-e határozni a W eloszlásának paramétereit, azaz a populáció átlagát és varianciáját.

A legegyszerűbb válasz az lenne, hogy kiszámítjuk a minta átlagát és varianciáját. Azonban előfordulhat, hogy a véletlen mintánk nem pontosan reprezentálja a teljes populációt. Ezért van értelme **konfidencia intervallumokról** beszélni.
> **Konfidencia intervallum** a populáció valódi átlagának becslése a mintánk alapján, amely egy bizonyos valószínűséggel (vagyis **bizalmi szinttel**) pontos.
Tegyük fel, hogy van egy mintánk X<sub>1</sub>, ..., X<sub>n</sub> az eloszlásunkból. Minden alkalommal, amikor mintát veszünk az eloszlásunkból, eltérő átlagértéket, μ-t kapunk. Ezért μ tekinthető véletlen változónak. Egy **konfidencia-intervallum** konfidencia p értékkel egy (L<sub>p</sub>,R<sub>p</sub>) értékpár, amelyre igaz, hogy **P**(L<sub>p</sub>≤μ≤R<sub>p</sub>) = p, azaz a mért átlagérték intervallumba esésének valószínűsége p.

Rövid bevezetőnkön túlmutat, hogy részletesen tárgyaljuk, hogyan számítják ki ezeket a konfidencia-intervallumokat. További részletek találhatók [a Wikipédián](https://en.wikipedia.org/wiki/Confidence_interval). Röviden, meghatározzuk a számított mintaátlag eloszlását a populáció valódi átlagához viszonyítva, amit **Student-eloszlásnak** nevezünk.

> **Érdekes tény**: A Student-eloszlás nevét William Sealy Gosset matematikusról kapta, aki "Student" álnéven publikálta tanulmányát. Gosset a Guinness sörgyárban dolgozott, és az egyik verzió szerint munkáltatója nem akarta, hogy a nagyközönség tudomást szerezzen arról, hogy statisztikai teszteket használnak a nyersanyagok minőségének meghatározására.

Ha a populáció átlagát, μ-t szeretnénk p konfidenciával becsülni, akkor a Student-eloszlás *(1-p)/2-edik percentilisét* kell venni, amelyet táblázatokból vagy statisztikai szoftverek (pl. Python, R stb.) beépített függvényeivel lehet kiszámítani. Ezután az μ intervalluma X±A*D/√n lesz, ahol X a minta kapott átlaga, D a szórás.

> **Megjegyzés**: Az [szabadságfokok](https://en.wikipedia.org/wiki/Degrees_of_freedom_(statistics)) fontos fogalmának tárgyalását is kihagyjuk, amely a Student-eloszlással kapcsolatban lényeges. További statisztikai könyvekben mélyebben megérthető ez a fogalom.

A súlyok és magasságok konfidencia-intervallumának kiszámítására példa található az [kísérő jegyzetfüzetekben](notebook.ipynb).

| p | Súly átlaga |
|-----|-----------|
| 0.85 | 201.73±0.94 |
| 0.90 | 201.73±1.08 |
| 0.95 | 201.73±1.28 |

Figyeljük meg, hogy minél nagyobb a konfidencia valószínűsége, annál szélesebb a konfidencia-intervallum.

## Hipotézisvizsgálat

A baseball játékosok adatállományában különböző játékos szerepek találhatók, amelyeket az alábbiakban összefoglalhatunk (nézd meg az [kísérő jegyzetfüzetet](notebook.ipynb), hogy látható legyen, hogyan számítható ki ez a táblázat):

| Szerep | Magasság | Súly | Darabszám |
|------|--------|--------|-------|
| Catcher | 72.723684 | 204.328947 | 76 |
| Designated_Hitter | 74.222222 | 220.888889 | 18 |
| First_Baseman | 74.000000 | 213.109091 | 55 |
| Outfielder | 73.010309 | 199.113402 | 194 |
| Relief_Pitcher | 74.374603 | 203.517460 | 315 |
| Second_Baseman | 71.362069 | 184.344828 | 58 |
| Shortstop | 71.903846 | 182.923077 | 52 |
| Starting_Pitcher | 74.719457 | 205.163636 | 221 |
| Third_Baseman | 73.044444 | 200.955556 | 45 |

Láthatjuk, hogy az első bázisjátékosok átlagos magassága nagyobb, mint a második bázisjátékosoké. Ezért kísértésbe eshetünk, hogy azt a következtetést vonjuk le, hogy **az első bázisjátékosok magasabbak, mint a második bázisjátékosok**.

> Ezt az állítást **hipotézisnek** nevezzük, mert nem tudjuk, hogy a tény valóban igaz-e vagy sem.

Azonban nem mindig egyértelmű, hogy levonhatjuk-e ezt a következtetést. Az előzőekből tudjuk, hogy minden átlaghoz tartozik egy konfidencia-intervallum, és így ez a különbség lehet pusztán statisztikai hiba. Szükségünk van egy formálisabb módszerre a hipotézis teszteléséhez.

Számítsuk ki külön-külön az első és második bázisjátékosok magasságának konfidencia-intervallumait:

| Konfidencia | Első bázisjátékosok | Második bázisjátékosok |
|------------|---------------|----------------|
| 0.85 | 73.62..74.38 | 71.04..71.69 |
| 0.90 | 73.56..74.44 | 70.99..71.73 |
| 0.95 | 73.47..74.53 | 70.92..71.81 |

Láthatjuk, hogy egyetlen konfidencia esetén sem fedik át egymást az intervallumok. Ez bizonyítja a hipotézisünket, hogy az első bázisjátékosok magasabbak, mint a második bázisjátékosok.

Formálisabban, az általunk megoldandó probléma annak vizsgálata, hogy **két valószínűségi eloszlás azonos-e**, vagy legalábbis ugyanazokkal a paraméterekkel rendelkezik-e. Az eloszlástól függően különböző teszteket kell alkalmaznunk. Ha tudjuk, hogy eloszlásaink normálisak, alkalmazhatjuk a **[Student t-tesztet](https://en.wikipedia.org/wiki/Student%27s_t-test)**.

A Student t-tesztben kiszámítjuk az úgynevezett **t-értéket**, amely jelzi az átlagok közötti különbséget, figyelembe véve a szórást. Kimutatták, hogy a t-érték követi a **Student-eloszlást**, amely lehetővé teszi számunkra, hogy megkapjuk a küszöbértéket egy adott konfidencia szinthez **p** (ez kiszámítható vagy numerikus táblázatokból kikereshető). Ezután összehasonlítjuk a t-értéket ezzel a küszöbértékkel, hogy elfogadjuk vagy elutasítsuk a hipotézist.

Pythonban használhatjuk a **SciPy** csomagot, amely tartalmazza a `ttest_ind` függvényt (sok más hasznos statisztikai függvény mellett!). Ez kiszámítja nekünk a t-értéket, és fordított keresést végez a konfidencia p-értékére, így csak a konfidenciát kell megnéznünk, hogy következtetést vonjunk le.

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

Más típusú hipotéziseket is tesztelhetünk, például:
* Annak bizonyítása, hogy egy adott minta követ egy eloszlást. Esetünkben feltételeztük, hogy a magasságok normálisan oszlanak el, de ezt formális statisztikai ellenőrzésnek kell alávetni.
* Annak bizonyítása, hogy egy minta átlagértéke megfelel egy előre meghatározott értéknek.
* Több minta átlagának összehasonlítása (pl. mi a különbség a boldogság szintek között különböző korcsoportokban).

## Nagyszámok törvénye és a központi határeloszlás tétele

Az egyik ok, amiért a normál eloszlás olyan fontos, az úgynevezett **központi határeloszlás tétele**. Tegyük fel, hogy van egy nagy mintánk független N értékekből X<sub>1</sub>, ..., X<sub>N</sub>, amelyek bármilyen eloszlásból származnak, átlag μ-val és szórás σ<sup>2</sup>-vel. Ekkor, ha N elég nagy (más szóval, amikor N→∞), az átlag Σ<sub>i</sub>X<sub>i</sub> normálisan oszlik el, átlag μ-val és szórás σ<sup>2</sup>/N-nel.

> A központi határeloszlás tételének másik értelmezése az, hogy függetlenül az eloszlástól, amikor bármely véletlen változó értékeinek összegének átlagát számítjuk, normál eloszlást kapunk.

A központi határeloszlás tételéből az is következik, hogy amikor N→∞, a mintaátlag μ-val való egyenlőségének valószínűsége 1 lesz. Ezt **nagyszámok törvényének** nevezik.

## Kovariancia és korreláció

Az egyik dolog, amit az adatelemzés végez, az adatok közötti kapcsolatok keresése. Azt mondjuk, hogy két sorozat **korrelál**, amikor hasonló viselkedést mutatnak ugyanabban az időben, azaz egyszerre emelkednek/csökkennek, vagy az egyik sorozat emelkedik, amikor a másik csökken, és fordítva. Más szóval, úgy tűnik, hogy van valamilyen kapcsolat a két sorozat között.

> A korreláció nem feltétlenül jelzi, hogy két sorozat között ok-okozati kapcsolat van; néha mindkét változó függhet valamilyen külső okból, vagy pusztán véletlen lehet, hogy a két sorozat korrelál. Azonban az erős matematikai korreláció jó jelzés arra, hogy két változó valamilyen módon összefügg.

Matematikailag a fő fogalom, amely megmutatja két véletlen változó közötti kapcsolatot, a **kovariancia**, amelyet így számítunk: Cov(X,Y) = **E**\[(X-**E**(X))(Y-**E**(Y))\]. Számítjuk mindkét változó eltérését az átlagértéküktől, majd ezeknek az eltéréseknek a szorzatát. Ha mindkét változó együtt tér el, a szorzat mindig pozitív érték lesz, ami pozitív kovarianciát eredményez. Ha mindkét változó eltérése nincs szinkronban (azaz az egyik az átlag alá esik, amikor a másik az átlag fölé emelkedik), mindig negatív számokat kapunk, amelyek negatív kovarianciává adódnak össze. Ha az eltérések nem függenek egymástól, nagyjából nullára adódnak össze.

A kovariancia abszolút értéke nem sokat mond arról, hogy mekkora a korreláció, mert az az értékek nagyságától függ. Normalizálásához eloszthatjuk a kovarianciát mindkét változó szórásával, hogy megkapjuk a **korrelációt**. Az előnye, hogy a korreláció mindig [-1,1] tartományban van, ahol 1 erős pozitív korrelációt jelez az értékek között, -1 erős negatív korrelációt, és 0 azt jelzi, hogy nincs korreláció (a változók függetlenek).

**Példa**: Számíthatunk korrelációt a baseball játékosok súlya és magassága között az említett adatállományból:
```python
print(np.corrcoef(weights,heights))
```
Ennek eredményeként kapunk egy **korrelációs mátrixot**, például ilyet:
```
array([[1.        , 0.52959196],
       [0.52959196, 1.        ]])
```

> A korrelációs mátrix C bármely számú bemeneti sorozatra S<sub>1</sub>, ..., S<sub>n</sub> kiszámítható. A C<sub>ij</sub> értéke az S<sub>i</sub> és S<sub>j</sub> közötti korreláció, és a diagonális elemek mindig 1-ek (ami az S<sub>i</sub> önkorrelációja).

Esetünkben a 0.53 érték azt jelzi, hogy van némi korreláció egy személy súlya és magassága között. Készíthetünk egy szórási diagramot az egyik értékről a másik ellen, hogy vizuálisan lássuk a kapcsolatot:

![Kapcsolat a súly és magasság között](../../../../translated_images/weight-height-relationship.3f06bde4ca2aba9974182c4ef037ed602acd0fbbbbe2ca91cefd838a9e66bcf9.hu.png)

> További példák a korrelációra és kovarianciára találhatók az [kísérő jegyzetfüzetben](notebook.ipynb).

## Következtetés

Ebben a szakaszban megtanultuk:

* az adatok alapvető statisztikai tulajdonságait, mint például az átlag, szórás, módusz és kvartilisek
* különböző véletlen változók eloszlásait, beleértve a normál eloszlást
* hogyan találjuk meg a korrelációt különböző tulajdonságok között
* hogyan használjuk a matematika és statisztika megalapozott eszközeit hipotézisek bizonyítására
* hogyan számítsunk konfidencia-intervallumokat véletlen változókhoz adott adatminták alapján

Bár ez nem kimerítő lista a valószínűség és statisztika témaköreiben, elegendőnek kell lennie ahhoz, hogy jó kezdést nyújtson ehhez a kurzushoz.

## 🚀 Kihívás

Használd a jegyzetfüzetben található mintakódot más hipotézisek tesztelésére:
1. Az első bázisjátékosok idősebbek, mint a második bázisjátékosok
2. Az első bázisjátékosok magasabbak, mint a harmadik bázisjátékosok
3. A shortstopok magasabbak, mint a második bázisjátékosok

## [Utólagos kvíz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/7)

## Áttekintés és önálló tanulás

A valószínűség és statisztika olyan széles téma, hogy megérdemelne egy saját kurzust. Ha mélyebben szeretnél belemerülni az elméletbe, érdemes lehet folytatni az alábbi könyvek olvasását:

1. [Carlos Fernandez-Granda](https://cims.nyu.edu/~cfgranda/) a New York Egyetemről nagyszerű előadásjegyzeteket készített [Valószínűség és statisztika az adatelemzéshez](https://cims.nyu.edu/~cfgranda/pages/stuff/probability_stats_for_DS.pdf) (elérhető online)
1. [Peter és Andrew Bruce. Gyakorlati statisztika adatelemzőknek.](https://www.oreilly.com/library/view/practical-statistics-for/9781491952955/) [[mintakód R-ben](https://github.com/andrewgbruce/statistics-for-data-scientists)]. 
1. [James D. Miller. Statisztika az adatelemzéshez](https://www.packtpub.com/product/statistics-for-data-science/9781788290678) [[mintakód R-ben](https://github.com/PacktPublishing/Statistics-for-Data-Science)]

## Feladat

[Kis diabétesz tanulmány](assignment.md)

## Köszönetnyilvánítás

Ezt a leckét ♥️-vel készítette [Dmitry Soshnikov](http://soshnikov.com).

---

**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Fontos információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.