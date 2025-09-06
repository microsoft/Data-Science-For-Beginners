<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1cf49f029ba1f25a54f0d5bc2fa575fc",
  "translation_date": "2025-09-05T22:07:11+00:00",
  "source_file": "1-Introduction/04-stats-and-probability/README.md",
  "language_code": "da"
}
-->
# En kort introduktion til statistik og sandsynlighed

|![ Sketchnote af [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/04-Statistics-Probability.png)|
|:---:|
| Statistik og sandsynlighed - _Sketchnote af [@nitya](https://twitter.com/nitya)_ |

Statistik og sandsynlighedsteori er to nært beslægtede områder inden for matematik, som er yderst relevante for datavidenskab. Det er muligt at arbejde med data uden en dyb forståelse af matematik, men det er stadig en fordel at kende til nogle grundlæggende begreber. Her præsenterer vi en kort introduktion, der kan hjælpe dig i gang.

[![Introduktionsvideo](../../../../1-Introduction/04-stats-and-probability/images/video-prob-and-stats.png)](https://youtu.be/Z5Zy85g4Yjw)

## [Quiz før forelæsning](https://ff-quizzes.netlify.app/en/ds/quiz/6)

## Sandsynlighed og stokastiske variable

**Sandsynlighed** er et tal mellem 0 og 1, der udtrykker, hvor sandsynligt en **hændelse** er. Det defineres som antallet af positive udfald (der fører til hændelsen) divideret med det samlede antal udfald, forudsat at alle udfald er lige sandsynlige. For eksempel, når vi kaster en terning, er sandsynligheden for at få et lige tal 3/6 = 0,5.

Når vi taler om hændelser, bruger vi **stokastiske variable**. For eksempel vil den stokastiske variabel, der repræsenterer et tal opnået ved at kaste en terning, tage værdier fra 1 til 6. Mængden af tal fra 1 til 6 kaldes **udfaldsrummet**. Vi kan tale om sandsynligheden for, at en stokastisk variabel tager en bestemt værdi, for eksempel P(X=3)=1/6.

Den stokastiske variabel i det foregående eksempel kaldes **diskret**, fordi den har et tælleligt udfaldsrum, dvs. der er adskilte værdier, der kan opregnes. Der findes også tilfælde, hvor udfaldsrummet er et interval af reelle tal eller hele mængden af reelle tal. Sådanne variable kaldes **kontinuerte**. Et godt eksempel er tidspunktet, hvor bussen ankommer.

## Sandsynlighedsfordeling

For diskrete stokastiske variable er det nemt at beskrive sandsynligheden for hver hændelse ved en funktion P(X). For hver værdi *s* fra udfaldsrummet *S* vil den give et tal mellem 0 og 1, sådan at summen af alle værdier af P(X=s) for alle hændelser er 1.

Den mest kendte diskrete fordeling er **den uniforme fordeling**, hvor der er et udfaldsrum med N elementer, og hver af dem har lige sandsynlighed på 1/N.

Det er mere kompliceret at beskrive sandsynlighedsfordelingen for en kontinuert variabel med værdier trukket fra et interval [a,b] eller hele mængden af reelle tal ℝ. Overvej tilfældet med bustidspunkt. Faktisk er sandsynligheden for, at bussen ankommer præcis på et bestemt tidspunkt *t*, 0!

> Nu ved du, at hændelser med sandsynlighed 0 sker, og det sker ofte! I hvert fald hver gang bussen ankommer!

Vi kan kun tale om sandsynligheden for, at en variabel falder inden for et givet interval af værdier, fx P(t<sub>1</sub>≤X<t<sub>2</sub>). I dette tilfælde beskrives sandsynlighedsfordelingen af en **sandsynlighedstæthedsfunktion** p(x), sådan at

![P(t_1\le X<t_2)=\int_{t_1}^{t_2}p(x)dx](../../../../1-Introduction/04-stats-and-probability/images/probability-density.png)

En kontinuert analog til den uniforme fordeling kaldes **kontinuerlig uniform**, som er defineret på et endeligt interval. Sandsynligheden for, at værdien X falder inden for et interval af længde l, er proportional med l og stiger op til 1.

En anden vigtig fordeling er **den normale fordeling**, som vi vil tale mere om nedenfor.

## Middelværdi, varians og standardafvigelse

Antag, at vi trækker en sekvens af n prøver af en stokastisk variabel X: x<sub>1</sub>, x<sub>2</sub>, ..., x<sub>n</sub>. Vi kan definere **middelværdien** (eller **aritmetisk gennemsnit**) af sekvensen på traditionel vis som (x<sub>1</sub>+x<sub>2</sub>+...+x<sub>n</sub>)/n. Når vi øger størrelsen af prøven (dvs. tager grænsen med n→∞), opnår vi middelværdien (også kaldet **forventningen**) af fordelingen. Vi betegner forventningen med **E**(x).

> Det kan vises, at for enhver diskret fordeling med værdier {x<sub>1</sub>, x<sub>2</sub>, ..., x<sub>N</sub>} og tilsvarende sandsynligheder p<sub>1</sub>, p<sub>2</sub>, ..., p<sub>N</sub>, vil forventningen være E(X)=x<sub>1</sub>p<sub>1</sub>+x<sub>2</sub>p<sub>2</sub>+...+x<sub>N</sub>p<sub>N</sub>.

For at identificere, hvor meget værdierne spreder sig, kan vi beregne variansen σ<sup>2</sup> = ∑(x<sub>i</sub> - μ)<sup>2</sup>/n, hvor μ er middelværdien af sekvensen. Værdien σ kaldes **standardafvigelse**, og σ<sup>2</sup> kaldes **varians**.

## Typetal, median og kvartiler

Nogle gange repræsenterer middelværdien ikke tilstrækkeligt den "typiske" værdi for data. For eksempel, når der er nogle få ekstreme værdier, der ligger helt uden for rækkevidde, kan de påvirke middelværdien. En anden god indikator er **medianen**, en værdi, sådan at halvdelen af datapunkterne er lavere end den, og den anden halvdel er højere.

For at forstå datafordelingen bedre er det nyttigt at tale om **kvartiler**:

* Første kvartil, eller Q1, er en værdi, sådan at 25% af dataene ligger under den
* Tredje kvartil, eller Q3, er en værdi, sådan at 75% af dataene ligger under den

Grafisk kan vi repræsentere forholdet mellem median og kvartiler i et diagram kaldet **boksplot**:

<img src="images/boxplot_explanation.png" width="50%"/>

Her beregner vi også **interkvartilområdet** IQR=Q3-Q1 og såkaldte **outliers** - værdier, der ligger uden for grænserne [Q1-1.5*IQR, Q3+1.5*IQR].

For en endelig fordeling, der indeholder et lille antal mulige værdier, er en god "typisk" værdi den, der forekommer hyppigst, og den kaldes **typetallet**. Det anvendes ofte på kategoriske data, såsom farver. Overvej en situation, hvor vi har to grupper af mennesker - nogle, der stærkt foretrækker rød, og andre, der foretrækker blå. Hvis vi koder farver med tal, vil middelværdien for en favoritfarve ligge et sted i det orange-grønne spektrum, hvilket ikke afspejler den faktiske præference for nogen af grupperne. Typetallet vil dog være enten en af farverne eller begge farver, hvis antallet af personer, der stemmer på dem, er lige (i dette tilfælde kalder vi prøven **multimodal**).

## Data fra den virkelige verden

Når vi analyserer data fra den virkelige verden, er de ofte ikke stokastiske variable i den forstand, at vi ikke udfører eksperimenter med ukendte resultater. For eksempel, overvej et hold af baseballspillere og deres kropsdata, såsom højde, vægt og alder. Disse tal er ikke præcis tilfældige, men vi kan stadig anvende de samme matematiske begreber. For eksempel kan en sekvens af folks vægte betragtes som en sekvens af værdier trukket fra en stokastisk variabel. Nedenfor er sekvensen af vægte for faktiske baseballspillere fra [Major League Baseball](http://mlb.mlb.com/index.jsp), taget fra [dette datasæt](http://wiki.stat.ucla.edu/socr/index.php/SOCR_Data_MLB_HeightsWeights) (for nemheds skyld vises kun de første 20 værdier):

```
[180.0, 215.0, 210.0, 210.0, 188.0, 176.0, 209.0, 200.0, 231.0, 180.0, 188.0, 180.0, 185.0, 160.0, 180.0, 185.0, 197.0, 189.0, 185.0, 219.0]
```

> **Bemærk**: For at se et eksempel på, hvordan man arbejder med dette datasæt, kan du kigge på [den tilhørende notebook](../../../../1-Introduction/04-stats-and-probability/notebook.ipynb). Der er også en række udfordringer gennem denne lektion, som du kan løse ved at tilføje noget kode til den notebook. Hvis du ikke er sikker på, hvordan du arbejder med data, skal du ikke bekymre dig - vi vender tilbage til at arbejde med data ved hjælp af Python senere. Hvis du ikke ved, hvordan du kører kode i Jupyter Notebook, kan du læse [denne artikel](https://soshnikov.com/education/how-to-execute-notebooks-from-github/).

Her er boksplottet, der viser middelværdi, median og kvartiler for vores data:

![Vægt boksplot](../../../../1-Introduction/04-stats-and-probability/images/weight-boxplot.png)

Da vores data indeholder information om forskellige spilleres **roller**, kan vi også lave et boksplot efter rolle - det giver os en idé om, hvordan parameterværdierne varierer på tværs af roller. Denne gang vil vi overveje højden:

![Boksplot efter rolle](../../../../1-Introduction/04-stats-and-probability/images/boxplot_byrole.png)

Dette diagram antyder, at højden af første basemen i gennemsnit er højere end højden af anden basemen. Senere i denne lektion vil vi lære, hvordan vi kan teste denne hypotese mere formelt, og hvordan vi kan vise, at vores data er statistisk signifikante.

> Når vi arbejder med data fra den virkelige verden, antager vi, at alle datapunkter er prøver trukket fra en sandsynlighedsfordeling. Denne antagelse giver os mulighed for at anvende maskinlæringsteknikker og bygge fungerende prædiktive modeller.

For at se, hvordan fordelingen af vores data ser ud, kan vi tegne en graf kaldet et **histogram**. X-aksen vil indeholde et antal forskellige vægtintervaller (såkaldte **bins**), og Y-aksen vil vise antallet af gange, vores stokastiske variabelprøve lå inden for et givet interval.

![Histogram af data fra den virkelige verden](../../../../1-Introduction/04-stats-and-probability/images/weight-histogram.png)

Fra dette histogram kan du se, at alle værdier er centreret omkring en vis gennemsnitsvægt, og jo længere vi bevæger os væk fra denne vægt, desto færre vægte af den værdi forekommer. Dvs. det er meget usandsynligt, at vægten af en baseballspiller vil være meget forskellig fra gennemsnitsvægten. Variansen af vægtene viser, i hvilket omfang vægtene sandsynligvis afviger fra gennemsnittet.

> Hvis vi tager vægtene af andre mennesker, der ikke er fra baseballligaen, vil fordelingen sandsynligvis være anderledes. Formen af fordelingen vil dog være den samme, men gennemsnittet og variansen vil ændre sig. Så hvis vi træner vores model på baseballspillere, vil den sandsynligvis give forkerte resultater, når den anvendes på universitetsstuderende, fordi den underliggende fordeling er anderledes.

## Normalfordeling

Den vægtfordeling, vi har set ovenfor, er meget typisk, og mange målinger fra den virkelige verden følger samme type fordeling, men med forskellige gennemsnit og varians. Denne fordeling kaldes **normalfordeling**, og den spiller en meget vigtig rolle i statistik.

At bruge normalfordeling er en korrekt måde at generere tilfældige vægte af potentielle baseballspillere. Når vi kender gennemsnitsvægten `mean` og standardafvigelsen `std`, kan vi generere 1000 vægtprøver på følgende måde:
```python
samples = np.random.normal(mean,std,1000)
```

Hvis vi tegner histogrammet for de genererede prøver, vil vi se et billede, der ligner det, der er vist ovenfor. Og hvis vi øger antallet af prøver og antallet af bins, kan vi generere et billede af en normalfordeling, der er tættere på det ideelle:

![Normalfordeling med gennemsnit=0 og std.afvigelse=1](../../../../1-Introduction/04-stats-and-probability/images/normal-histogram.png)

*Normalfordeling med gennemsnit=0 og std.afvigelse=1*

## Konfidensintervaller

Når vi taler om vægtene af baseballspillere, antager vi, at der er en vis **stokastisk variabel W**, der svarer til den ideelle sandsynlighedsfordeling af vægtene for alle baseballspillere (den såkaldte **population**). Vores sekvens af vægte svarer til et udsnit af alle baseballspillere, som vi kalder **prøven**. Et interessant spørgsmål er, om vi kan kende parametrene for fordelingen af W, dvs. gennemsnittet og variansen af populationen.

Det nemmeste svar ville være at beregne gennemsnittet og variansen af vores prøve. Det kan dog ske, at vores tilfældige prøve ikke nøjagtigt repræsenterer hele populationen. Derfor giver det mening at tale om **konfidensintervaller**.

> **Konfidensinterval** er en estimering af den sande middelværdi for populationen givet vores prøve, som er præcis med en vis sandsynlighed (eller **konfidensniveau**).

Antag, at vi har en prøve X...

1</sub>, ..., X<sub>n</sub> fra vores distribution. Hver gang vi trækker en prøve fra vores distribution, vil vi ende med en forskellig middelværdi μ. Derfor kan μ betragtes som en stokastisk variabel. Et **konfidensinterval** med konfidens p er et par af værdier (L<sub>p</sub>,R<sub>p</sub>), sådan at **P**(L<sub>p</sub>≤μ≤R<sub>p</sub>) = p, dvs. sandsynligheden for, at den målte middelværdi falder inden for intervallet, er lig med p.

Det går ud over vores korte introduktion at diskutere i detaljer, hvordan disse konfidensintervaller beregnes. Flere detaljer kan findes [på Wikipedia](https://en.wikipedia.org/wiki/Confidence_interval). Kort sagt definerer vi fordelingen af den beregnede prøve-middelværdi i forhold til den sande middelværdi af populationen, hvilket kaldes **student distribution**.

> **Interessant fakta**: Student distribution er opkaldt efter matematikeren William Sealy Gosset, som udgav sin artikel under pseudonymet "Student". Han arbejdede på Guinness-bryggeriet, og ifølge en af versionerne ønskede hans arbejdsgiver ikke, at offentligheden skulle vide, at de brugte statistiske tests til at bestemme kvaliteten af råmaterialer.

Hvis vi ønsker at estimere middelværdien μ af vores population med konfidens p, skal vi tage *(1-p)/2-percentilen* af en Student distribution A, som enten kan tages fra tabeller eller beregnes ved hjælp af indbyggede funktioner i statistisk software (f.eks. Python, R osv.). Derefter vil intervallet for μ være givet ved X±A*D/√n, hvor X er den opnåede middelværdi af prøven, og D er standardafvigelsen.

> **Note**: Vi udelader også diskussionen om et vigtigt begreb kaldet [frihedsgrader](https://en.wikipedia.org/wiki/Degrees_of_freedom_(statistics)), som er vigtigt i relation til Student distribution. Du kan henvise til mere komplette bøger om statistik for at forstå dette begreb dybere.

Et eksempel på beregning af konfidensinterval for vægt og højde er givet i de [tilhørende notebooks](../../../../1-Introduction/04-stats-and-probability/notebook.ipynb).

| p | Vægt middelværdi |
|-----|----------------|
| 0.85 | 201.73±0.94 |
| 0.90 | 201.73±1.08 |
| 0.95 | 201.73±1.28 |

Bemærk, at jo højere konfidens sandsynligheden er, jo bredere er konfidensintervallet.

## Hypotesetestning 

I vores dataset med baseballspillere er der forskellige spillerroller, som kan opsummeres nedenfor (se den [tilhørende notebook](../../../../1-Introduction/04-stats-and-probability/notebook.ipynb) for at se, hvordan denne tabel kan beregnes):

| Rolle | Højde | Vægt | Antal |
|-------|-------|------|-------|
| Catcher | 72.723684 | 204.328947 | 76 |
| Designated_Hitter | 74.222222 | 220.888889 | 18 |
| First_Baseman | 74.000000 | 213.109091 | 55 |
| Outfielder | 73.010309 | 199.113402 | 194 |
| Relief_Pitcher | 74.374603 | 203.517460 | 315 |
| Second_Baseman | 71.362069 | 184.344828 | 58 |
| Shortstop | 71.903846 | 182.923077 | 52 |
| Starting_Pitcher | 74.719457 | 205.163636 | 221 |
| Third_Baseman | 73.044444 | 200.955556 | 45 |

Vi kan bemærke, at middelhøjden for first basemen er højere end for second basemen. Derfor kan vi være fristet til at konkludere, at **first basemen er højere end second basemen**.

> Denne erklæring kaldes **en hypotese**, fordi vi ikke ved, om det faktisk er sandt eller ej.

Det er dog ikke altid indlysende, om vi kan drage denne konklusion. Fra diskussionen ovenfor ved vi, at hver middelværdi har et tilhørende konfidensinterval, og derfor kan denne forskel blot være en statistisk fejl. Vi har brug for en mere formel måde at teste vores hypotese på.

Lad os beregne konfidensintervaller separat for højderne af first og second basemen:

| Konfidens | First Basemen | Second Basemen |
|-----------|---------------|----------------|
| 0.85 | 73.62..74.38 | 71.04..71.69 |
| 0.90 | 73.56..74.44 | 70.99..71.73 |
| 0.95 | 73.47..74.53 | 70.92..71.81 |

Vi kan se, at under ingen konfidens overlapper intervallerne. Det beviser vores hypotese om, at first basemen er højere end second basemen.

Mere formelt er problemet, vi løser, at se, om **to sandsynlighedsfordelinger er de samme**, eller i det mindste har de samme parametre. Afhængigt af fordelingen skal vi bruge forskellige tests til det. Hvis vi ved, at vores fordelinger er normale, kan vi anvende **[Student t-test](https://en.wikipedia.org/wiki/Student%27s_t-test)**.

I Student t-test beregner vi den såkaldte **t-værdi**, som angiver forskellen mellem middelværdierne, idet der tages højde for variansen. Det er demonstreret, at t-værdien følger **student distribution**, hvilket giver os mulighed for at få tærskelværdien for et givet konfidensniveau **p** (dette kan beregnes eller findes i numeriske tabeller). Vi sammenligner derefter t-værdien med denne tærskel for at godkende eller afvise hypotesen.

I Python kan vi bruge **SciPy**-pakken, som inkluderer funktionen `ttest_ind` (ud over mange andre nyttige statistiske funktioner!). Den beregner t-værdien for os og udfører også den omvendte opslagning af konfidens p-værdien, så vi blot kan se på konfidensen for at drage konklusionen.

For eksempel giver vores sammenligning mellem højderne af first og second basemen os følgende resultater: 
```python
from scipy.stats import ttest_ind

tval, pval = ttest_ind(df.loc[df['Role']=='First_Baseman',['Height']], df.loc[df['Role']=='Designated_Hitter',['Height']],equal_var=False)
print(f"T-value = {tval[0]:.2f}\nP-value: {pval[0]}")
```
```
T-value = 7.65
P-value: 9.137321189738925e-12
```
I vores tilfælde er p-værdien meget lav, hvilket betyder, at der er stærke beviser for, at first basemen er højere.

Der er også forskellige andre typer hypoteser, som vi måske ønsker at teste, for eksempel:
* At bevise, at en given prøve følger en bestemt fordeling. I vores tilfælde har vi antaget, at højder er normalt fordelt, men det kræver formel statistisk verifikation. 
* At bevise, at middelværdien af en prøve svarer til en foruddefineret værdi
* At sammenligne middelværdierne af flere prøver (f.eks. hvad er forskellen i lykkeniveauer blandt forskellige aldersgrupper)

## Lov om store tal og central grænseværdi-sætning

En af grundene til, at normalfordeling er så vigtig, er den såkaldte **central grænseværdi-sætning**. Antag, at vi har en stor prøve af uafhængige N værdier X<sub>1</sub>, ..., X<sub>N</sub>, udtaget fra en hvilken som helst fordeling med middelværdi μ og varians σ<sup>2</sup>. Så, for tilstrækkeligt store N (med andre ord, når N→∞), vil middelværdien Σ<sub>i</sub>X<sub>i</sub> være normalt fordelt med middelværdi μ og varians σ<sup>2</sup>/N.

> En anden måde at fortolke den centrale grænseværdi-sætning på er at sige, at uanset fordeling, når du beregner middelværdien af en sum af vilkårlige stokastiske variabelværdier, ender du med en normalfordeling.

Fra den centrale grænseværdi-sætning følger det også, at når N→∞, bliver sandsynligheden for, at prøve-middelværdien er lig med μ, 1. Dette er kendt som **loven om store tal**.

## Kovarians og korrelation

En af de ting, Data Science gør, er at finde relationer mellem data. Vi siger, at to sekvenser **korrelerer**, når de udviser lignende adfærd på samme tid, dvs. de enten stiger/falder samtidig, eller én sekvens stiger, når en anden falder og omvendt. Med andre ord ser der ud til at være en relation mellem to sekvenser.

> Korrelation indikerer ikke nødvendigvis en årsagssammenhæng mellem to sekvenser; nogle gange kan begge variabler afhænge af en ekstern årsag, eller det kan være rent tilfældigt, at de to sekvenser korrelerer. Dog er stærk matematisk korrelation en god indikation på, at to variabler på en eller anden måde er forbundet.

Matematisk er det vigtigste begreb, der viser relationen mellem to stokastiske variabler, **kovarians**, som beregnes sådan: Cov(X,Y) = **E**\[(X-**E**(X))(Y-**E**(Y))\]. Vi beregner afvigelsen af begge variabler fra deres middelværdier og derefter produktet af disse afvigelser. Hvis begge variabler afviger sammen, vil produktet altid være en positiv værdi, der vil summere til positiv kovarians. Hvis begge variabler afviger ude af sync (dvs. én falder under gennemsnittet, når en anden stiger over gennemsnittet), vil vi altid få negative tal, der vil summere til negativ kovarians. Hvis afvigelserne ikke er afhængige, vil de summere til cirka nul.

Den absolutte værdi af kovarians fortæller os ikke meget om, hvor stor korrelationen er, fordi den afhænger af størrelsen af de faktiske værdier. For at normalisere den kan vi dividere kovarians med standardafvigelsen af begge variabler for at få **korrelation**. Det gode ved korrelation er, at den altid ligger i intervallet [-1,1], hvor 1 angiver stærk positiv korrelation mellem værdier, -1 - stærk negativ korrelation, og 0 - ingen korrelation overhovedet (variablerne er uafhængige).

**Eksempel**: Vi kan beregne korrelationen mellem vægt og højde for baseballspillere fra det nævnte dataset:
```python
print(np.corrcoef(weights,heights))
```
Som resultat får vi **korrelationsmatrix** som denne:
```
array([[1.        , 0.52959196],
       [0.52959196, 1.        ]])
```

> Korrelationsmatrix C kan beregnes for et vilkårligt antal inputsekvenser S<sub>1</sub>, ..., S<sub>n</sub>. Værdien af C<sub>ij</sub> er korrelationen mellem S<sub>i</sub> og S<sub>j</sub>, og diagonalelementerne er altid 1 (hvilket også er selvkorrelationen af S<sub>i</sub>).

I vores tilfælde indikerer værdien 0.53, at der er en vis korrelation mellem en persons vægt og højde. Vi kan også lave et scatterplot af én værdi mod den anden for at se relationen visuelt:

![Relation mellem vægt og højde](../../../../1-Introduction/04-stats-and-probability/images/weight-height-relationship.png)

> Flere eksempler på korrelation og kovarians kan findes i [den tilhørende notebook](../../../../1-Introduction/04-stats-and-probability/notebook.ipynb).

## Konklusion

I denne sektion har vi lært:

* grundlæggende statistiske egenskaber ved data, såsom middelværdi, varians, typetal og kvartiler
* forskellige fordelinger af stokastiske variabler, herunder normalfordeling
* hvordan man finder korrelation mellem forskellige egenskaber
* hvordan man bruger matematiske og statistiske metoder til at bevise nogle hypoteser
* hvordan man beregner konfidensintervaller for stokastiske variabler givet en dataprøve

Selvom dette bestemt ikke er en udtømmende liste over emner inden for sandsynlighed og statistik, bør det være nok til at give dig en god start på dette kursus.

## 🚀 Udfordring

Brug eksempelkoden i notebooken til at teste andre hypoteser:
1. First basemen er ældre end second basemen
2. First basemen er højere end third basemen
3. Shortstops er højere end second basemen

## [Quiz efter forelæsning](https://ff-quizzes.netlify.app/en/ds/quiz/7)

## Gennemgang & Selvstudie

Sandsynlighed og statistik er et så bredt emne, at det fortjener sit eget kursus. Hvis du er interesseret i at gå dybere ind i teorien, kan du overveje at læse nogle af følgende bøger:

1. [Carlos Fernandez-Granda](https://cims.nyu.edu/~cfgranda/) fra New York University har fantastiske forelæsningsnoter [Probability and Statistics for Data Science](https://cims.nyu.edu/~cfgranda/pages/stuff/probability_stats_for_DS.pdf) (tilgængelig online)
1. [Peter og Andrew Bruce. Practical Statistics for Data Scientists.](https://www.oreilly.com/library/view/practical-statistics-for/9781491952955/) [[eksempelkode i R](https://github.com/andrewgbruce/statistics-for-data-scientists)]. 
1. [James D. Miller. Statistics for Data Science](https://www.packtpub.com/product/statistics-for-data-science/9781788290678) [[eksempelkode i R](https://github.com/PacktPublishing/Statistics-for-Data-Science)]

## Opgave

[Small Diabetes Study](assignment.md)

## Credits

Denne lektion er skrevet med ♥️ af [Dmitry Soshnikov](http://soshnikov.com)

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.