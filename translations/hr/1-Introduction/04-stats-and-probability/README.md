<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1cf49f029ba1f25a54f0d5bc2fa575fc",
  "translation_date": "2025-09-05T19:26:37+00:00",
  "source_file": "1-Introduction/04-stats-and-probability/README.md",
  "language_code": "hr"
}
-->
# Kratki uvod u statistiku i vjerojatnost

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/04-Statistics-Probability.png)|
|:---:|
| Statistika i vjerojatnost - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

Teorija statistike i vjerojatnosti dva su međusobno povezana područja matematike koja su izuzetno važna za znanost o podacima. Moguće je raditi s podacima bez dubokog poznavanja matematike, ali ipak je bolje razumjeti barem osnovne pojmove. Ovdje ćemo predstaviti kratki uvod koji će vam pomoći da započnete.

[![Intro Video](../../../../1-Introduction/04-stats-and-probability/images/video-prob-and-stats.png)](https://youtu.be/Z5Zy85g4Yjw)

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ds/quiz/6)

## Vjerojatnost i slučajne varijable

**Vjerojatnost** je broj između 0 i 1 koji izražava koliko je neki **događaj** vjerojatan. Definira se kao broj pozitivnih ishoda (koji vode do događaja) podijeljen s ukupnim brojem ishoda, pod uvjetom da su svi ishodi jednako vjerojatni. Na primjer, kada bacimo kocku, vjerojatnost da dobijemo paran broj je 3/6 = 0.5.

Kada govorimo o događajima, koristimo **slučajne varijable**. Na primjer, slučajna varijabla koja predstavlja broj dobiven bacanjem kocke uzima vrijednosti od 1 do 6. Skup brojeva od 1 do 6 naziva se **prostor uzorka**. Možemo govoriti o vjerojatnosti da slučajna varijabla uzme određenu vrijednost, na primjer P(X=3)=1/6.

Slučajna varijabla u prethodnom primjeru naziva se **diskretna**, jer ima prebrojiv prostor uzorka, tj. postoje odvojene vrijednosti koje se mogu nabrojati. Postoje slučajevi kada je prostor uzorka raspon realnih brojeva ili cijeli skup realnih brojeva. Takve varijable nazivaju se **kontinuirane**. Dobar primjer je vrijeme dolaska autobusa.

## Distribucija vjerojatnosti

U slučaju diskretnih slučajnih varijabli, lako je opisati vjerojatnost svakog događaja funkcijom P(X). Za svaku vrijednost *s* iz prostora uzorka *S* ona će dati broj između 0 i 1, tako da zbroj svih vrijednosti P(X=s) za sve događaje bude 1.

Najpoznatija diskretna distribucija je **uniformna distribucija**, u kojoj postoji prostor uzorka od N elemenata, s jednakom vjerojatnošću od 1/N za svaki od njih.

Teže je opisati distribuciju vjerojatnosti kontinuirane varijable, s vrijednostima izvučenim iz nekog intervala [a,b] ili cijelog skupa realnih brojeva ℝ. Razmislite o slučaju vremena dolaska autobusa. Zapravo, za svako točno vrijeme dolaska *t*, vjerojatnost da autobus stigne točno u to vrijeme je 0!

> Sada znate da se događaji s vjerojatnošću 0 događaju, i to vrlo često! Barem svaki put kad autobus stigne!

Možemo govoriti samo o vjerojatnosti da varijabla padne u određeni interval vrijednosti, npr. P(t<sub>1</sub>≤X<t<sub>2</sub>). U ovom slučaju, distribucija vjerojatnosti opisuje se **funkcijom gustoće vjerojatnosti** p(x), tako da

![P(t_1\le X<t_2)=\int_{t_1}^{t_2}p(x)dx](../../../../1-Introduction/04-stats-and-probability/images/probability-density.png)

Kontinuirani analog uniformne distribucije naziva se **kontinuirana uniformna**, koja je definirana na konačnom intervalu. Vjerojatnost da vrijednost X padne u interval duljine l proporcionalna je l i raste do 1.

Druga važna distribucija je **normalna distribucija**, o kojoj ćemo detaljnije govoriti u nastavku.

## Srednja vrijednost, varijanca i standardna devijacija

Pretpostavimo da uzimamo niz od n uzoraka slučajne varijable X: x<sub>1</sub>, x<sub>2</sub>, ..., x<sub>n</sub>. Možemo definirati **srednju vrijednost** (ili **aritmetički prosjek**) niza na tradicionalan način kao (x<sub>1</sub>+x<sub>2</sub>+x<sub>n</sub>)/n. Kako povećavamo veličinu uzorka (tj. uzimamo granicu s n→∞), dobit ćemo srednju vrijednost (također nazvanu **očekivanje**) distribucije. Očekivanje ćemo označiti s **E**(x).

> Može se pokazati da za bilo koju diskretnu distribuciju s vrijednostima {x<sub>1</sub>, x<sub>2</sub>, ..., x<sub>N</sub>} i odgovarajućim vjerojatnostima p<sub>1</sub>, p<sub>2</sub>, ..., p<sub>N</sub>, očekivanje bi bilo E(X)=x<sub>1</sub>p<sub>1</sub>+x<sub>2</sub>p<sub>2</sub>+...+x<sub>N</sub>p<sub>N</sub>.

Kako bismo identificirali koliko su vrijednosti raspršene, možemo izračunati varijancu σ<sup>2</sup> = ∑(x<sub>i</sub> - μ)<sup>2</sup>/n, gdje je μ srednja vrijednost niza. Vrijednost σ naziva se **standardna devijacija**, a σ<sup>2</sup> naziva se **varijanca**.

## Mod, medijan i kvartili

Ponekad srednja vrijednost ne predstavlja adekvatno "tipičnu" vrijednost za podatke. Na primjer, kada postoje nekoliko ekstremnih vrijednosti koje su potpuno izvan raspona, one mogu utjecati na srednju vrijednost. Drugi dobar pokazatelj je **medijan**, vrijednost takva da je polovica podataka niža od nje, a druga polovica - viša.

Kako bismo bolje razumjeli distribuciju podataka, korisno je govoriti o **kvartilima**:

* Prvi kvartil, ili Q1, je vrijednost takva da 25% podataka pada ispod nje
* Treći kvartil, ili Q3, je vrijednost takva da 75% podataka pada ispod nje

Grafički možemo prikazati odnos između medijana i kvartila u dijagramu zvanom **box plot**:

<img src="images/boxplot_explanation.png" width="50%"/>

Ovdje također izračunavamo **interkvartilni raspon** IQR=Q3-Q1 i tzv. **outliers** - vrijednosti koje leže izvan granica [Q1-1.5*IQR,Q3+1.5*IQR].

Za konačnu distribuciju koja sadrži mali broj mogućih vrijednosti, dobra "tipična" vrijednost je ona koja se najčešće pojavljuje, a naziva se **mod**. Često se primjenjuje na kategorijske podatke, poput boja. Zamislite situaciju kada imamo dvije skupine ljudi - jedni koji snažno preferiraju crvenu boju, a drugi plavu. Ako kodiramo boje brojevima, srednja vrijednost za omiljenu boju bila bi negdje u spektru narančasto-zelene, što ne pokazuje stvarnu preferenciju nijedne skupine. Međutim, mod bi bio jedna od boja ili obje boje, ako je broj ljudi koji glasaju za njih jednak (u tom slučaju uzorak nazivamo **multimodalnim**).

## Podaci iz stvarnog svijeta

Kada analiziramo podatke iz stvarnog života, oni često nisu slučajne varijable u pravom smislu, u smislu da ne provodimo eksperimente s nepoznatim rezultatom. Na primjer, razmislite o timu bejzbol igrača i njihovim tjelesnim podacima, poput visine, težine i dobi. Ti brojevi nisu baš slučajni, ali još uvijek možemo primijeniti iste matematičke koncepte. Na primjer, niz težina ljudi može se smatrati nizom vrijednosti izvučenih iz neke slučajne varijable. Ispod je niz težina stvarnih bejzbol igrača iz [Major League Baseball](http://mlb.mlb.com/index.jsp), preuzet iz [ovog skupa podataka](http://wiki.stat.ucla.edu/socr/index.php/SOCR_Data_MLB_HeightsWeights) (za vašu praktičnost, prikazano je samo prvih 20 vrijednosti):

```
[180.0, 215.0, 210.0, 210.0, 188.0, 176.0, 209.0, 200.0, 231.0, 180.0, 188.0, 180.0, 185.0, 160.0, 180.0, 185.0, 197.0, 189.0, 185.0, 219.0]
```

> **Napomena**: Za primjer rada s ovim skupom podataka, pogledajte [prateću bilježnicu](../../../../1-Introduction/04-stats-and-probability/notebook.ipynb). Također postoji niz izazova kroz ovu lekciju, a možete ih riješiti dodavanjem koda u tu bilježnicu. Ako niste sigurni kako raditi s podacima, ne brinite - vratit ćemo se radu s podacima koristeći Python kasnije. Ako ne znate kako pokrenuti kod u Jupyter Notebooku, pogledajte [ovaj članak](https://soshnikov.com/education/how-to-execute-notebooks-from-github/).

Ovdje je box plot koji prikazuje srednju vrijednost, medijan i kvartile za naše podatke:

![Weight Box Plot](../../../../1-Introduction/04-stats-and-probability/images/weight-boxplot.png)

Budući da naši podaci sadrže informacije o različitim **ulogama** igrača, možemo napraviti i box plot prema ulozi - to će nam omogućiti da steknemo ideju o tome kako se vrijednosti parametara razlikuju među ulogama. Ovaj put ćemo razmotriti visinu:

![Box plot by role](../../../../1-Introduction/04-stats-and-probability/images/boxplot_byrole.png)

Ovaj dijagram sugerira da je, u prosjeku, visina igrača na prvoj bazi veća od visine igrača na drugoj bazi. Kasnije u ovoj lekciji naučit ćemo kako možemo formalnije testirati ovu hipotezu i kako pokazati da su naši podaci statistički značajni za dokazivanje toga.

> Kada radimo s podacima iz stvarnog svijeta, pretpostavljamo da su svi podaci uzorci izvučeni iz neke distribucije vjerojatnosti. Ova pretpostavka omogućuje nam primjenu tehnika strojnog učenja i izgradnju funkcionalnih prediktivnih modela.

Kako bismo vidjeli kakva je distribucija naših podataka, možemo nacrtati graf nazvan **histogram**. X-os će sadržavati broj različitih intervala težine (tzv. **bins**), a vertikalna os pokazivat će broj puta kada je uzorak naše slučajne varijable bio unutar određenog intervala.

![Histogram of real world data](../../../../1-Introduction/04-stats-and-probability/images/weight-histogram.png)

Iz ovog histograma možete vidjeti da su sve vrijednosti koncentrirane oko određene srednje težine, a što dalje idemo od te težine - to se rjeđe susreću težine te vrijednosti. Drugim riječima, vrlo je malo vjerojatno da će težina bejzbol igrača biti vrlo različita od srednje težine. Varijanca težina pokazuje koliko su težine sklone odstupanju od srednje vrijednosti.

> Ako uzmemo težine drugih ljudi, ne iz bejzbol lige, distribucija će vjerojatno biti drugačija. Međutim, oblik distribucije ostat će isti, ali srednja vrijednost i varijanca će se promijeniti. Dakle, ako treniramo naš model na bejzbol igračima, vjerojatno će dati pogrešne rezultate kada se primijeni na studente sveučilišta, jer je temeljna distribucija drugačija.

## Normalna distribucija

Distribucija težina koju smo vidjeli gore vrlo je tipična, i mnoge mjere iz stvarnog svijeta slijede isti tip distribucije, ali s različitim srednjim vrijednostima i varijancama. Ova distribucija naziva se **normalna distribucija**, i igra vrlo važnu ulogu u statistici.

Korištenje normalne distribucije ispravan je način za generiranje slučajnih težina potencijalnih bejzbol igrača. Kada znamo srednju težinu `mean` i standardnu devijaciju `std`, možemo generirati 1000 uzoraka težine na sljedeći način:
```python
samples = np.random.normal(mean,std,1000)
```

Ako nacrtamo histogram generiranih uzoraka, vidjet ćemo sliku vrlo sličnu onoj prikazanoj gore. A ako povećamo broj uzoraka i broj bins, možemo generirati sliku normalne distribucije koja je bliža idealnoj:

![Normal Distribution with mean=0 and std.dev=1](../../../../1-Introduction/04-stats-and-probability/images/normal-histogram.png)

*Normalna distribucija sa srednjom vrijednošću=0 i standardnom devijacijom=1*

## Intervali pouzdanosti

Kada govorimo o težinama bejzbol igrača, pretpostavljamo da postoji određena **slučajna varijabla W** koja odgovara idealnoj distribuciji vjerojatnosti težina svih bejzbol igrača (tzv. **populacija**). Naš niz težina odgovara podskupu svih bejzbol igrača koji nazivamo **uzorak**. Zanimljivo pitanje je, možemo li znati parametre distribucije W, tj. srednju vrijednost i varijancu populacije?

Najlakši odgovor bio bi izračunati srednju vrijednost i varijancu našeg uzorka. Međutim, moglo bi se dogoditi da naš slučajni uzorak ne predstavlja točno cijelu populaciju. Stoga ima smisla govoriti o **intervalu pouzdanosti**.

> **Interval pouzdanosti** je procjena stvarne srednje vrijednosti populacije na temelju našeg uzorka, koja je točna s određenom vjerojatnošću (ili **razinom pouzdanosti**).

Pretpostavimo da imamo uzorak X...

1</sub>, ..., X<sub>n</sub> iz naše distribucije. Svaki put kad uzmemo uzorak iz naše distribucije, dobit ćemo različitu srednju vrijednost μ. Stoga se μ može smatrati slučajnom varijablom. **Interval pouzdanosti** s pouzdanošću p je par vrijednosti (L<sub>p</sub>,R<sub>p</sub>), takav da **P**(L<sub>p</sub>≤μ≤R<sub>p</sub>) = p, tj. vjerojatnost da izmjerena srednja vrijednost padne unutar intervala jednaka je p.

Detaljna rasprava o tome kako se ti intervali pouzdanosti izračunavaju prelazi okvire našeg kratkog uvoda. Više detalja možete pronaći [na Wikipediji](https://en.wikipedia.org/wiki/Confidence_interval). Ukratko, definiramo distribuciju izračunate srednje vrijednosti uzorka u odnosu na stvarnu srednju vrijednost populacije, što se naziva **studentova distribucija**.

> **Zanimljiva činjenica**: Studentova distribucija nazvana je po matematičaru Williamu Sealyju Gossetu, koji je svoj rad objavio pod pseudonimom "Student". Radio je u pivovari Guinness, a prema jednoj verziji, njegov poslodavac nije želio da šira javnost zna da koriste statističke testove za određivanje kvalitete sirovina.

Ako želimo procijeniti srednju vrijednost μ naše populacije s pouzdanošću p, trebamo uzeti *(1-p)/2-ti percentil* studentove distribucije A, koji se može uzeti iz tablica ili izračunati pomoću ugrađenih funkcija statističkog softvera (npr. Python, R, itd.). Tada bi interval za μ bio dan s X±A*D/√n, gdje je X dobivena srednja vrijednost uzorka, a D standardna devijacija.

> **Napomena**: Također izostavljamo raspravu o važnom konceptu [stupnjeva slobode](https://en.wikipedia.org/wiki/Degrees_of_freedom_(statistics)), koji je važan u vezi sa studentovom distribucijom. Možete se obratiti potpunijim knjigama o statistici kako biste dublje razumjeli ovaj koncept.

Primjer izračuna intervala pouzdanosti za težine i visine dan je u [priloženim bilježnicama](../../../../1-Introduction/04-stats-and-probability/notebook.ipynb).

| p | Srednja težina |
|-----|-----------|
| 0.85 | 201.73±0.94 |
| 0.90 | 201.73±1.08 |
| 0.95 | 201.73±1.28 |

Primijetite da što je veća vjerojatnost pouzdanosti, to je širi interval pouzdanosti.

## Testiranje hipoteza

U našem skupu podataka o igračima bejzbola postoje različite uloge igrača, koje se mogu sažeti u tablici ispod (pogledajte [priloženu bilježnicu](../../../../1-Introduction/04-stats-and-probability/notebook.ipynb) kako biste vidjeli kako se ova tablica može izračunati):

| Uloga | Visina | Težina | Broj |
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

Možemo primijetiti da je srednja visina igrača na prvoj bazi veća od one igrača na drugoj bazi. Stoga bismo mogli zaključiti da su **igrači na prvoj bazi viši od igrača na drugoj bazi**.

> Ova izjava naziva se **hipoteza**, jer ne znamo je li činjenica zapravo istinita ili ne.

Međutim, nije uvijek očito možemo li donijeti ovaj zaključak. Iz prethodne rasprave znamo da svaka srednja vrijednost ima pridruženi interval pouzdanosti, pa ta razlika može biti samo statistička pogreška. Potrebno nam je formalniji način za testiranje naše hipoteze.

Izračunajmo intervale pouzdanosti zasebno za visine igrača na prvoj i drugoj bazi:

| Pouzdanost | Prva baza | Druga baza |
|------------|---------------|----------------|
| 0.85 | 73.62..74.38 | 71.04..71.69 |
| 0.90 | 73.56..74.44 | 70.99..71.73 |
| 0.95 | 73.47..74.53 | 70.92..71.81 |

Možemo vidjeti da se intervali ne preklapaju ni pod jednom pouzdanošću. To dokazuje našu hipotezu da su igrači na prvoj bazi viši od igrača na drugoj bazi.

Formalnije, problem koji rješavamo je vidjeti jesu li **dvije distribucije vjerojatnosti iste**, ili barem imaju iste parametre. Ovisno o distribuciji, trebamo koristiti različite testove za to. Ako znamo da su naše distribucije normalne, možemo primijeniti **[Studentov t-test](https://en.wikipedia.org/wiki/Student%27s_t-test)**.

U Studentovom t-testu izračunavamo tzv. **t-vrijednost**, koja pokazuje razliku između srednjih vrijednosti, uzimajući u obzir varijancu. Pokazano je da t-vrijednost slijedi **studentovu distribuciju**, što nam omogućuje dobivanje granične vrijednosti za danu razinu pouzdanosti **p** (to se može izračunati ili pronaći u numeričkim tablicama). Zatim uspoređujemo t-vrijednost s ovom granicom kako bismo odobrili ili odbacili hipotezu.

U Pythonu možemo koristiti paket **SciPy**, koji uključuje funkciju `ttest_ind` (uz mnoge druge korisne statističke funkcije!). Ona za nas izračunava t-vrijednost, a također obavlja obrnuto traženje p-vrijednosti pouzdanosti, tako da možemo samo pogledati pouzdanost kako bismo donijeli zaključak.

Na primjer, naša usporedba visina igrača na prvoj i drugoj bazi daje nam sljedeće rezultate:
```python
from scipy.stats import ttest_ind

tval, pval = ttest_ind(df.loc[df['Role']=='First_Baseman',['Height']], df.loc[df['Role']=='Designated_Hitter',['Height']],equal_var=False)
print(f"T-value = {tval[0]:.2f}\nP-value: {pval[0]}")
```
```
T-value = 7.65
P-value: 9.137321189738925e-12
```
U našem slučaju, p-vrijednost je vrlo niska, što znači da postoje jaki dokazi koji podržavaju da su igrači na prvoj bazi viši.

Postoje i različite druge vrste hipoteza koje bismo mogli testirati, na primjer:
* Dokazati da određeni uzorak slijedi neku distribuciju. U našem slučaju pretpostavili smo da su visine normalno distribuirane, ali to treba formalno statistički provjeriti.
* Dokazati da srednja vrijednost uzorka odgovara nekoj unaprijed definiranoj vrijednosti
* Usporediti srednje vrijednosti više uzoraka (npr. koja je razlika u razinama sreće među različitim dobnim skupinama)

## Zakon velikih brojeva i centralna granična teorema

Jedan od razloga zašto je normalna distribucija toliko važna je tzv. **centralna granična teorema**. Pretpostavimo da imamo veliki uzorak neovisnih N vrijednosti X<sub>1</sub>, ..., X<sub>N</sub>, uzorkovanih iz bilo koje distribucije sa srednjom vrijednošću μ i varijancom σ<sup>2</sup>. Tada, za dovoljno velik N (drugim riječima, kad N→∞), srednja vrijednost Σ<sub>i</sub>X<sub>i</sub> bit će normalno distribuirana, sa srednjom vrijednošću μ i varijancom σ<sup>2</sup>/N.

> Drugi način interpretacije centralne granične teoreme je reći da bez obzira na distribuciju, kad izračunate srednju vrijednost zbroja bilo kojih vrijednosti slučajnih varijabli, završavate s normalnom distribucijom.

Iz centralne granične teoreme također slijedi da, kad N→∞, vjerojatnost da srednja vrijednost uzorka bude jednaka μ postaje 1. Ovo je poznato kao **zakon velikih brojeva**.

## Kovarianca i korelacija

Jedna od stvari koju Data Science radi je pronalaženje odnosa između podataka. Kažemo da se dvije sekvence **koreliraju** kad pokazuju slično ponašanje u isto vrijeme, tj. ili istovremeno rastu/padaju, ili jedna sekvenca raste kad druga pada i obrnuto. Drugim riječima, čini se da postoji neka veza između dvije sekvence.

> Korelacija ne mora nužno ukazivati na uzročnu vezu između dvije sekvence; ponekad obje varijable mogu ovisiti o nekom vanjskom uzroku, ili može biti čista slučajnost da se dvije sekvence koreliraju. Međutim, jaka matematička korelacija dobar je pokazatelj da su dvije varijable nekako povezane.

Matematički, glavni koncept koji pokazuje vezu između dvije slučajne varijable je **kovarianca**, koja se izračunava ovako: Cov(X,Y) = **E**\[(X-**E**(X))(Y-**E**(Y))\]. Izračunavamo odstupanje obje varijable od njihovih srednjih vrijednosti, a zatim produkt tih odstupanja. Ako obje varijable odstupaju zajedno, produkt će uvijek biti pozitivna vrijednost, koja će se zbrojiti u pozitivnu kovariancu. Ako obje varijable odstupaju nesinkronizirano (tj. jedna pada ispod prosjeka kad druga raste iznad prosjeka), uvijek ćemo dobiti negativne brojeve, koji će se zbrojiti u negativnu kovariancu. Ako odstupanja nisu ovisna, zbrojit će se na otprilike nulu.

Apsolutna vrijednost kovariance ne govori nam mnogo o tome koliko je velika korelacija, jer ovisi o veličini stvarnih vrijednosti. Da bismo je normalizirali, možemo podijeliti kovariancu sa standardnom devijacijom obje varijable, kako bismo dobili **korelaciju**. Dobra stvar je da je korelacija uvijek u rasponu [-1,1], gdje 1 označava jaku pozitivnu korelaciju između vrijednosti, -1 - jaku negativnu korelaciju, a 0 - nikakvu korelaciju (varijable su neovisne).

**Primjer**: Možemo izračunati korelaciju između težina i visina igrača bejzbola iz gore spomenutog skupa podataka:
```python
print(np.corrcoef(weights,heights))
```
Kao rezultat, dobivamo **matricu korelacije** poput ove:
```
array([[1.        , 0.52959196],
       [0.52959196, 1.        ]])
```

> Matrica korelacije C može se izračunati za bilo koji broj ulaznih sekvenci S<sub>1</sub>, ..., S<sub>n</sub>. Vrijednost C<sub>ij</sub> je korelacija između S<sub>i</sub> i S<sub>j</sub>, a dijagonalni elementi su uvijek 1 (što je također samokorelacija S<sub>i</sub>).

U našem slučaju, vrijednost 0.53 ukazuje na to da postoji neka korelacija između težine i visine osobe. Također možemo napraviti scatter plot jedne vrijednosti u odnosu na drugu kako bismo vizualno vidjeli odnos:

![Odnos između težine i visine](../../../../1-Introduction/04-stats-and-probability/images/weight-height-relationship.png)

> Više primjera korelacije i kovariance možete pronaći u [priloženoj bilježnici](../../../../1-Introduction/04-stats-and-probability/notebook.ipynb).

## Zaključak

U ovom dijelu naučili smo:

* osnovna statistička svojstva podataka, poput srednje vrijednosti, varijance, moda i kvartila
* različite distribucije slučajnih varijabli, uključujući normalnu distribuciju
* kako pronaći korelaciju između različitih svojstava
* kako koristiti matematički i statistički aparat za dokazivanje hipoteza
* kako izračunati intervale pouzdanosti za slučajnu varijablu na temelju uzorka podataka

Iako ovo definitivno nije iscrpan popis tema koje postoje unutar teorije vjerojatnosti i statistike, trebalo bi biti dovoljno za dobar početak ovog tečaja.

## 🚀 Izazov

Koristite uzorak koda u bilježnici za testiranje drugih hipoteza:
1. Igrači na prvoj bazi su stariji od igrača na drugoj bazi
2. Igrači na prvoj bazi su viši od igrača na trećoj bazi
3. Shortstopovi su viši od igrača na drugoj bazi

## [Post-predavanje kviz](https://ff-quizzes.netlify.app/en/ds/quiz/7)

## Pregled i samostalno učenje

Vjerojatnost i statistika su toliko široka tema da zaslužuju vlastiti tečaj. Ako želite dublje ući u teoriju, možda ćete htjeti nastaviti čitati neke od sljedećih knjiga:

1. [Carlos Fernandez-Granda](https://cims.nyu.edu/~cfgranda/) s New York University ima odlične bilješke s predavanja [Probability and Statistics for Data Science](https://cims.nyu.edu/~cfgranda/pages/stuff/probability_stats_for_DS.pdf) (dostupno online)
1. [Peter i Andrew Bruce. Practical Statistics for Data Scientists.](https://www.oreilly.com/library/view/practical-statistics-for/9781491952955/) [[uzorak koda u R](https://github.com/andrewgbruce/statistics-for-data-scientists)]. 
1. [James D. Miller. Statistics for Data Science](https://www.packtpub.com/product/statistics-for-data-science/9781788290678) [[uzorak koda u R](https://github.com/PacktPublishing/Statistics-for-Data-Science)]

## Zadatak

[Mala studija o dijabetesu](assignment.md)

## Zasluge

Ovo predavanje je napisano s ♥️ od strane [Dmitry Soshnikov](http://soshnikov.com)

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane ljudskog prevoditelja. Ne snosimo odgovornost za bilo kakve nesporazume ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.