<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1cf49f029ba1f25a54f0d5bc2fa575fc",
  "translation_date": "2025-09-05T22:27:10+00:00",
  "source_file": "1-Introduction/04-stats-and-probability/README.md",
  "language_code": "no"
}
-->
# En kort introduksjon til statistikk og sannsynlighet

|![ Sketchnote av [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/04-Statistics-Probability.png)|
|:---:|
| Statistikk og sannsynlighet - _Sketchnote av [@nitya](https://twitter.com/nitya)_ |

Statistikk og sannsynlighetsteori er to nært beslektede områder innen matematikk som er svært relevante for datavitenskap. Det er mulig å jobbe med data uten dyp kunnskap om matematikk, men det er likevel bedre å kjenne til noen grunnleggende konsepter. Her vil vi presentere en kort introduksjon som kan hjelpe deg i gang.

[![Introduksjonsvideo](../../../../1-Introduction/04-stats-and-probability/images/video-prob-and-stats.png)](https://youtu.be/Z5Zy85g4Yjw)

## [Quiz før forelesning](https://ff-quizzes.netlify.app/en/ds/quiz/6)

## Sannsynlighet og tilfeldige variabler

**Sannsynlighet** er et tall mellom 0 og 1 som uttrykker hvor sannsynlig en **hendelse** er. Det defineres som antall positive utfall (som fører til hendelsen), delt på totalt antall utfall, gitt at alle utfall er like sannsynlige. For eksempel, når vi kaster en terning, er sannsynligheten for å få et partall 3/6 = 0,5.

Når vi snakker om hendelser, bruker vi **tilfeldige variabler**. For eksempel vil den tilfeldige variabelen som representerer tallet vi får når vi kaster en terning, ta verdier fra 1 til 6. Mengden av tall fra 1 til 6 kalles **utvalgsrom**. Vi kan snakke om sannsynligheten for at en tilfeldig variabel tar en bestemt verdi, for eksempel P(X=3)=1/6.

Den tilfeldige variabelen i det forrige eksempelet kalles **diskret**, fordi den har et tellbart utvalgsrom, dvs. det finnes separate verdier som kan telles opp. Det finnes tilfeller der utvalgsrommet er et intervall av reelle tall, eller hele mengden av reelle tall. Slike variabler kalles **kontinuerlige**. Et godt eksempel er tidspunktet når bussen ankommer.

## Sannsynlighetsfordeling

I tilfellet med diskrete tilfeldige variabler er det enkelt å beskrive sannsynligheten for hver hendelse med en funksjon P(X). For hver verdi *s* fra utvalgsrommet *S* vil den gi et tall fra 0 til 1, slik at summen av alle verdier av P(X=s) for alle hendelser blir 1.

Den mest kjente diskrete fordelingen er **uniform fordeling**, der det finnes et utvalgsrom med N elementer, med lik sannsynlighet på 1/N for hver av dem.

Det er vanskeligere å beskrive sannsynlighetsfordelingen til en kontinuerlig variabel, med verdier hentet fra et intervall [a,b], eller hele mengden av reelle tall ℝ. Tenk på tilfellet med busstiden. Faktisk, for hvert eksakte tidspunkt *t*, er sannsynligheten for at bussen ankommer akkurat da, 0!

> Nå vet du at hendelser med sannsynlighet 0 skjer, og ganske ofte! I hvert fall hver gang bussen ankommer!

Vi kan bare snakke om sannsynligheten for at en variabel faller innenfor et gitt intervall av verdier, f.eks. P(t<sub>1</sub>≤X<t<sub>2</sub>). I dette tilfellet beskrives sannsynlighetsfordelingen av en **tetthetsfunksjon** p(x), slik at

![P(t_1\le X<t_2)=\int_{t_1}^{t_2}p(x)dx](../../../../1-Introduction/04-stats-and-probability/images/probability-density.png)

En kontinuerlig analog av uniform fordeling kalles **kontinuerlig uniform**, som er definert på et endelig intervall. Sannsynligheten for at verdien X faller innenfor et intervall med lengde l er proporsjonal med l, og stiger opp til 1.

En annen viktig fordeling er **normalfordeling**, som vi skal snakke mer om nedenfor.

## Gjennomsnitt, varians og standardavvik

Anta at vi trekker en sekvens av n prøver av en tilfeldig variabel X: x<sub>1</sub>, x<sub>2</sub>, ..., x<sub>n</sub>. Vi kan definere **gjennomsnitt** (eller **aritmetisk middelverdi**) for sekvensen på tradisjonelt vis som (x<sub>1</sub>+x<sub>2</sub>+x<sub>n</sub>)/n. Når vi øker størrelsen på prøven (dvs. tar grensen når n→∞), vil vi oppnå gjennomsnittet (også kalt **forventning**) for fordelingen. Vi vil betegne forventning med **E**(x).

> Det kan vises at for enhver diskret fordeling med verdier {x<sub>1</sub>, x<sub>2</sub>, ..., x<sub>N</sub>} og tilsvarende sannsynligheter p<sub>1</sub>, p<sub>2</sub>, ..., p<sub>N</sub>, vil forventningen være E(X)=x<sub>1</sub>p<sub>1</sub>+x<sub>2</sub>p<sub>2</sub>+...+x<sub>N</sub>p<sub>N</sub>.

For å identifisere hvor spredt verdiene er, kan vi beregne variansen σ<sup>2</sup> = ∑(x<sub>i</sub> - μ)<sup>2</sup>/n, der μ er gjennomsnittet for sekvensen. Verdien σ kalles **standardavvik**, og σ<sup>2</sup> kalles **varians**.

## Typetall, median og kvartiler

Noen ganger representerer ikke gjennomsnittet den "typiske" verdien for dataene på en god måte. For eksempel, når det finnes noen ekstreme verdier som er helt utenfor rekkevidde, kan de påvirke gjennomsnittet. Et annet godt mål er **median**, en verdi slik at halvparten av datapunktene er lavere enn den, og den andre halvparten - høyere.

For å hjelpe oss med å forstå fordelingen av dataene, er det nyttig å snakke om **kvartiler**:

* Første kvartil, eller Q1, er en verdi slik at 25 % av dataene ligger under den
* Tredje kvartil, eller Q3, er en verdi slik at 75 % av dataene ligger under den

Grafisk kan vi representere forholdet mellom median og kvartiler i et diagram kalt **boksplott**:

<img src="images/boxplot_explanation.png" width="50%"/>

Her beregner vi også **interkvartilavstand** IQR=Q3-Q1, og såkalte **uteliggere** - verdier som ligger utenfor grensene [Q1-1.5*IQR,Q3+1.5*IQR].

For en endelig fordeling som inneholder et lite antall mulige verdier, er en god "typisk" verdi den som forekommer oftest, og som kalles **typetall**. Det brukes ofte på kategoriske data, som farger. Tenk på en situasjon der vi har to grupper mennesker - noen som sterkt foretrekker rødt, og andre som foretrekker blått. Hvis vi koder farger med tall, vil gjennomsnittsverdien for en favorittfarge være et sted i det oransje-grønne spekteret, noe som ikke indikerer den faktiske preferansen til noen av gruppene. Typetallet vil imidlertid være en av fargene, eller begge fargene, hvis antallet personer som stemmer på dem er likt (i dette tilfellet kaller vi utvalget **multimodalt**).

## Data fra virkeligheten

Når vi analyserer data fra virkeligheten, er de ofte ikke tilfeldige variabler i streng forstand, i den forstand at vi ikke utfører eksperimenter med ukjent resultat. For eksempel, vurder et lag med baseballspillere og deres kroppslige data, som høyde, vekt og alder. Disse tallene er ikke akkurat tilfeldige, men vi kan fortsatt bruke de samme matematiske konseptene. For eksempel kan en sekvens av folks vekter betraktes som en sekvens av verdier hentet fra en tilfeldig variabel. Nedenfor er sekvensen av vekter til faktiske baseballspillere fra [Major League Baseball](http://mlb.mlb.com/index.jsp), hentet fra [dette datasettet](http://wiki.stat.ucla.edu/socr/index.php/SOCR_Data_MLB_HeightsWeights) (for enkelhets skyld vises kun de første 20 verdiene):

```
[180.0, 215.0, 210.0, 210.0, 188.0, 176.0, 209.0, 200.0, 231.0, 180.0, 188.0, 180.0, 185.0, 160.0, 180.0, 185.0, 197.0, 189.0, 185.0, 219.0]
```

> **Merk**: For å se et eksempel på hvordan du jobber med dette datasettet, ta en titt på [den medfølgende notatboken](../../../../1-Introduction/04-stats-and-probability/notebook.ipynb). Det finnes også en rekke utfordringer gjennom denne leksjonen, og du kan fullføre dem ved å legge til litt kode i den notatboken. Hvis du ikke er sikker på hvordan du opererer med data, ikke bekymre deg - vi kommer tilbake til å jobbe med data ved hjelp av Python senere. Hvis du ikke vet hvordan du kjører kode i Jupyter Notebook, ta en titt på [denne artikkelen](https://soshnikov.com/education/how-to-execute-notebooks-from-github/).

Her er boksplottet som viser gjennomsnitt, median og kvartiler for dataene våre:

![Vekt boksplott](../../../../1-Introduction/04-stats-and-probability/images/weight-boxplot.png)

Siden dataene våre inneholder informasjon om forskjellige spiller**roller**, kan vi også lage boksplott etter rolle - dette vil gi oss en idé om hvordan parameterverdiene varierer mellom rollene. Denne gangen vil vi vurdere høyde:

![Boksplott etter rolle](../../../../1-Introduction/04-stats-and-probability/images/boxplot_byrole.png)

Dette diagrammet antyder at høyden til førstemenn på laget i gjennomsnitt er høyere enn høyden til andremenn. Senere i denne leksjonen vil vi lære hvordan vi kan teste denne hypotesen mer formelt, og hvordan vi kan vise at dataene våre er statistisk signifikante for å bevise dette.

> Når vi jobber med data fra virkeligheten, antar vi at alle datapunkter er prøver hentet fra en sannsynlighetsfordeling. Denne antagelsen lar oss bruke maskinlæringsteknikker og bygge fungerende prediktive modeller.

For å se hvordan fordelingen av dataene våre er, kan vi lage en graf kalt et **histogram**. X-aksen vil inneholde et antall forskjellige vektintervaller (såkalte **bøtter**), og Y-aksen vil vise antall ganger vår tilfeldige variabelprøve var innenfor et gitt intervall.

![Histogram av data fra virkeligheten](../../../../1-Introduction/04-stats-and-probability/images/weight-histogram.png)

Fra dette histogrammet kan du se at alle verdier er sentrert rundt en viss gjennomsnittsvekt, og jo lenger vi beveger oss fra den vekten, desto færre vekter av den verdien blir observert. Det vil si, det er svært usannsynlig at vekten til en baseballspiller vil være veldig forskjellig fra gjennomsnittsvekten. Variansen i vektene viser i hvilken grad vektene sannsynligvis avviker fra gjennomsnittet.

> Hvis vi tar vektene til andre mennesker, ikke fra baseballigaen, vil fordelingen sannsynligvis være annerledes. Imidlertid vil formen på fordelingen være den samme, men gjennomsnittet og variansen vil endre seg. Så hvis vi trener modellen vår på baseballspillere, vil den sannsynligvis gi feil resultater når den brukes på studenter ved et universitet, fordi den underliggende fordelingen er annerledes.

## Normalfordeling

Fordelingen av vekter som vi har sett ovenfor er svært typisk, og mange målinger fra virkeligheten følger samme type fordeling, men med forskjellig gjennomsnitt og varians. Denne fordelingen kalles **normalfordeling**, og den spiller en svært viktig rolle i statistikk.

Å bruke normalfordeling er en korrekt måte å generere tilfeldige vekter for potensielle baseballspillere. Når vi kjenner gjennomsnittsvekten `mean` og standardavviket `std`, kan vi generere 1000 vektprøver på følgende måte:
```python
samples = np.random.normal(mean,std,1000)
```

Hvis vi plottet histogrammet for de genererte prøvene, vil vi se et bilde som ligner veldig på det som er vist ovenfor. Og hvis vi øker antall prøver og antall bøtter, kan vi generere et bilde av en normalfordeling som er nærmere ideell:

![Normalfordeling med gjennomsnitt=0 og std.avvik=1](../../../../1-Introduction/04-stats-and-probability/images/normal-histogram.png)

*Normalfordeling med gjennomsnitt=0 og std.avvik=1*

## Konfidensintervaller

Når vi snakker om vektene til baseballspillere, antar vi at det finnes en viss **tilfeldig variabel W** som tilsvarer den ideelle sannsynlighetsfordelingen av vektene til alle baseballspillere (den såkalte **populasjonen**). Vår sekvens av vekter tilsvarer et utvalg av alle baseballspillere som vi kaller **utvalg**. Et interessant spørsmål er: Kan vi vite parameterne for fordelingen av W, dvs. gjennomsnittet og variansen for populasjonen?

Det enkleste svaret ville være å beregne gjennomsnittet og variansen for vårt utvalg. Men det kan hende at vårt tilfeldige utvalg ikke nøyaktig representerer hele populasjonen. Derfor gir det mening å snakke om **konfidensintervaller**.

> **Konfidensintervall** er en estimering av den sanne middelverdien for populasjonen gitt vårt utvalg, som er nøyaktig med en viss sannsynlighet (eller **konfidensnivå**).

Anta at vi har et utvalg X...

1</sub>, ..., X<sub>n</sub> fra vår fordeling. Hver gang vi trekker et utvalg fra fordelingen, vil vi ende opp med en forskjellig gjennomsnittsverdi μ. Dermed kan μ betraktes som en stokastisk variabel. Et **konfidensintervall** med konfidens p er et par verdier (L<sub>p</sub>,R<sub>p</sub>), slik at **P**(L<sub>p</sub>≤μ≤R<sub>p</sub>) = p, altså sannsynligheten for at den målte gjennomsnittsverdien faller innenfor intervallet er lik p.

Det går utover vår korte introduksjon å diskutere i detalj hvordan disse konfidensintervallene beregnes. Flere detaljer kan finnes [på Wikipedia](https://en.wikipedia.org/wiki/Confidence_interval). Kort sagt definerer vi fordelingen av beregnet utvalgsgjennomsnitt i forhold til populasjonens sanne gjennomsnitt, som kalles **studentfordeling**.

> **Interessant fakta**: Studentfordelingen er oppkalt etter matematikeren William Sealy Gosset, som publiserte sitt arbeid under pseudonymet "Student". Han jobbet i Guinness-bryggeriet, og ifølge en av versjonene ønsket ikke arbeidsgiveren at allmennheten skulle vite at de brukte statistiske tester for å bestemme kvaliteten på råvarene.

Hvis vi ønsker å estimere gjennomsnittet μ av vår populasjon med konfidens p, må vi ta *(1-p)/2-te persentil* av en Studentfordeling A, som enten kan hentes fra tabeller eller beregnes ved hjelp av innebygde funksjoner i statistikkprogramvare (f.eks. Python, R, osv.). Da vil intervallet for μ være gitt av X±A*D/√n, hvor X er det oppnådde gjennomsnittet av utvalget, og D er standardavviket.

> **Merk**: Vi utelater også diskusjonen om et viktig konsept kalt [frihetsgrader](https://en.wikipedia.org/wiki/Degrees_of_freedom_(statistics)), som er viktig i forhold til Studentfordelingen. Du kan referere til mer komplette bøker om statistikk for å forstå dette konseptet dypere.

Et eksempel på beregning av konfidensintervall for vekt og høyde er gitt i [tilhørende notatbøker](../../../../1-Introduction/04-stats-and-probability/notebook.ipynb).

| p | Vektgjennomsnitt |
|-----|----------------|
| 0.85 | 201.73±0.94 |
| 0.90 | 201.73±1.08 |
| 0.95 | 201.73±1.28 |

Legg merke til at jo høyere konfidenssannsynligheten er, desto bredere er konfidensintervallet.

## Hypotesetesting 

I vårt datasett med baseballspillere finnes det ulike spillerroller, som kan oppsummeres nedenfor (se [tilhørende notatbok](../../../../1-Introduction/04-stats-and-probability/notebook.ipynb) for å se hvordan denne tabellen kan beregnes):

| Rolle | Høyde | Vekt | Antall |
|-------|-------|------|--------|
| Catcher | 72.723684 | 204.328947 | 76 |
| Designated_Hitter | 74.222222 | 220.888889 | 18 |
| First_Baseman | 74.000000 | 213.109091 | 55 |
| Outfielder | 73.010309 | 199.113402 | 194 |
| Relief_Pitcher | 74.374603 | 203.517460 | 315 |
| Second_Baseman | 71.362069 | 184.344828 | 58 |
| Shortstop | 71.903846 | 182.923077 | 52 |
| Starting_Pitcher | 74.719457 | 205.163636 | 221 |
| Third_Baseman | 73.044444 | 200.955556 | 45 |

Vi kan legge merke til at gjennomsnittshøyden til førstemenn er høyere enn for andremenn. Dermed kan vi bli fristet til å konkludere at **førstemenn er høyere enn andremenn**.

> Denne påstanden kalles **en hypotese**, fordi vi ikke vet om dette faktisk er sant eller ikke.

Det er imidlertid ikke alltid åpenbart om vi kan trekke denne konklusjonen. Fra diskusjonen ovenfor vet vi at hvert gjennomsnitt har et tilhørende konfidensintervall, og dermed kan denne forskjellen bare være en statistisk feil. Vi trenger en mer formell måte å teste hypotesen vår på.

La oss beregne konfidensintervaller separat for høydene til førstemenn og andremenn:

| Konfidens | Førstemenn | Andremenn |
|-----------|------------|-----------|
| 0.85 | 73.62..74.38 | 71.04..71.69 |
| 0.90 | 73.56..74.44 | 70.99..71.73 |
| 0.95 | 73.47..74.53 | 70.92..71.81 |

Vi kan se at under ingen konfidens overlapper intervallene. Dette beviser vår hypotese om at førstemenn er høyere enn andremenn.

Mer formelt er problemet vi løser å se om **to sannsynlighetsfordelinger er de samme**, eller i det minste har de samme parameterne. Avhengig av fordelingen må vi bruke forskjellige tester for dette. Hvis vi vet at fordelingene våre er normale, kan vi bruke **[Student t-test](https://en.wikipedia.org/wiki/Student%27s_t-test)**.

I Student t-test beregner vi den såkalte **t-verdien**, som indikerer forskjellen mellom gjennomsnittene, tatt i betraktning variansen. Det er vist at t-verdien følger **studentfordelingen**, som lar oss finne terskelverdien for et gitt konfidensnivå **p** (dette kan beregnes eller slås opp i numeriske tabeller). Vi sammenligner deretter t-verdien med denne terskelen for å godkjenne eller forkaste hypotesen.

I Python kan vi bruke **SciPy**-pakken, som inkluderer funksjonen `ttest_ind` (i tillegg til mange andre nyttige statistiske funksjoner!). Den beregner t-verdien for oss, og gjør også det omvendte oppslaget av konfidens p-verdi, slik at vi bare kan se på konfidensen for å trekke en konklusjon.

For eksempel gir vår sammenligning mellom høydene til førstemenn og andremenn følgende resultater: 
```python
from scipy.stats import ttest_ind

tval, pval = ttest_ind(df.loc[df['Role']=='First_Baseman',['Height']], df.loc[df['Role']=='Designated_Hitter',['Height']],equal_var=False)
print(f"T-value = {tval[0]:.2f}\nP-value: {pval[0]}")
```
```
T-value = 7.65
P-value: 9.137321189738925e-12
```
I vårt tilfelle er p-verdien svært lav, noe som betyr at det er sterk evidens for at førstemenn er høyere.

Det finnes også andre typer hypoteser vi kan teste, for eksempel:
* Å bevise at et gitt utvalg følger en bestemt fordeling. I vårt tilfelle har vi antatt at høydene er normalfordelte, men dette trenger formell statistisk bekreftelse.
* Å bevise at gjennomsnittsverdien av et utvalg tilsvarer en forhåndsdefinert verdi.
* Å sammenligne gjennomsnittene av flere utvalg (f.eks. hva er forskjellen i lykkenivåer mellom ulike aldersgrupper).

## Store talls lov og sentralgrenseteoremet

En av grunnene til at normalfordelingen er så viktig, er det såkalte **sentralgrenseteoremet**. Anta at vi har et stort utvalg av uavhengige N verdier X<sub>1</sub>, ..., X<sub>N</sub>, trukket fra en hvilken som helst fordeling med gjennomsnitt μ og varians σ<sup>2</sup>. Da, for tilstrekkelig stort N (med andre ord, når N→∞), vil gjennomsnittet Σ<sub>i</sub>X<sub>i</sub> være normalfordelt, med gjennomsnitt μ og varians σ<sup>2</sup>/N.

> En annen måte å tolke sentralgrenseteoremet på er å si at uansett fordeling, når du beregner gjennomsnittet av summen av tilfeldige variabelverdier, ender du opp med en normalfordeling.

Fra sentralgrenseteoremet følger det også at når N→∞, blir sannsynligheten for at utvalgsgjennomsnittet er lik μ lik 1. Dette er kjent som **store talls lov**.

## Kovarians og korrelasjon

En av oppgavene i Data Science er å finne relasjoner mellom data. Vi sier at to sekvenser **korrelerer** når de viser lignende oppførsel samtidig, dvs. de enten stiger/faller samtidig, eller én sekvens stiger når en annen faller og omvendt. Med andre ord ser det ut til å være en relasjon mellom de to sekvensene.

> Korrelasjon indikerer ikke nødvendigvis en årsakssammenheng mellom to sekvenser; noen ganger kan begge variablene avhenge av en ekstern årsak, eller det kan være ren tilfeldighet at de to sekvensene korrelerer. Likevel er sterk matematisk korrelasjon en god indikasjon på at to variabler på en eller annen måte er koblet.

Matematisk er hovedkonseptet som viser relasjonen mellom to stokastiske variabler **kovarians**, som beregnes slik: Cov(X,Y) = **E**\[(X-**E**(X))(Y-**E**(Y))\]. Vi beregner avviket til begge variablene fra deres gjennomsnittsverdier, og deretter produktet av disse avvikene. Hvis begge variablene avviker sammen, vil produktet alltid være en positiv verdi, som vil gi positiv kovarians. Hvis begge variablene avviker usynkront (dvs. én faller under gjennomsnittet når en annen stiger over gjennomsnittet), vil vi alltid få negative tall, som vil gi negativ kovarians. Hvis avvikene er uavhengige, vil de summere seg til omtrent null.

Den absolutte verdien av kovarians sier ikke mye om hvor sterk korrelasjonen er, fordi den avhenger av størrelsen på de faktiske verdiene. For å normalisere den kan vi dele kovariansen på standardavviket til begge variablene for å få **korrelasjon**. Det fine er at korrelasjonen alltid er i området [-1,1], hvor 1 indikerer sterk positiv korrelasjon mellom verdier, -1 - sterk negativ korrelasjon, og 0 - ingen korrelasjon i det hele tatt (variablene er uavhengige).

**Eksempel**: Vi kan beregne korrelasjonen mellom vekter og høyder til baseballspillere fra datasettet nevnt ovenfor:
```python
print(np.corrcoef(weights,heights))
```
Som et resultat får vi **korrelasjonsmatrisen** som denne:
```
array([[1.        , 0.52959196],
       [0.52959196, 1.        ]])
```

> Korrelasjonsmatrisen C kan beregnes for et hvilket som helst antall inngangssekvenser S<sub>1</sub>, ..., S<sub>n</sub>. Verdien av C<sub>ij</sub> er korrelasjonen mellom S<sub>i</sub> og S<sub>j</sub>, og diagonalelementene er alltid 1 (som også er selvkorrelasjonen til S<sub>i</sub>).

I vårt tilfelle indikerer verdien 0.53 at det er en viss korrelasjon mellom en persons vekt og høyde. Vi kan også lage et spredningsdiagram av én verdi mot den andre for å se relasjonen visuelt:

![Forhold mellom vekt og høyde](../../../../1-Introduction/04-stats-and-probability/images/weight-height-relationship.png)

> Flere eksempler på korrelasjon og kovarians kan finnes i [tilhørende notatbok](../../../../1-Introduction/04-stats-and-probability/notebook.ipynb).

## Konklusjon

I denne delen har vi lært:

* grunnleggende statistiske egenskaper ved data, som gjennomsnitt, varians, modus og kvartiler
* ulike fordelinger av stokastiske variabler, inkludert normalfordeling
* hvordan finne korrelasjon mellom ulike egenskaper
* hvordan bruke matematikk og statistikk for å bevise hypoteser
* hvordan beregne konfidensintervaller for stokastiske variabler gitt et datasett

Selv om dette definitivt ikke er en uttømmende liste over emner innen sannsynlighet og statistikk, bør det være nok til å gi deg en god start på dette kurset.

## 🚀 Utfordring

Bruk eksempelkoden i notatboken for å teste andre hypoteser som: 
1. Førstemenn er eldre enn andremenn
2. Førstemenn er høyere enn tredjemenn
3. Shortstops er høyere enn andremenn

## [Quiz etter forelesning](https://ff-quizzes.netlify.app/en/ds/quiz/7)

## Gjennomgang og selvstudium

Sannsynlighet og statistikk er et så bredt emne at det fortjener sitt eget kurs. Hvis du er interessert i å gå dypere inn i teorien, kan du lese noen av følgende bøker:

1. [Carlos Fernandez-Granda](https://cims.nyu.edu/~cfgranda/) fra New York University har flotte forelesningsnotater [Probability and Statistics for Data Science](https://cims.nyu.edu/~cfgranda/pages/stuff/probability_stats_for_DS.pdf) (tilgjengelig online)
1. [Peter og Andrew Bruce. Practical Statistics for Data Scientists.](https://www.oreilly.com/library/view/practical-statistics-for/9781491952955/) [[eksempelkode i R](https://github.com/andrewgbruce/statistics-for-data-scientists)]. 
1. [James D. Miller. Statistics for Data Science](https://www.packtpub.com/product/statistics-for-data-science/9781788290678) [[eksempelkode i R](https://github.com/PacktPublishing/Statistics-for-Data-Science)]

## Oppgave

[Lite diabetesstudie](assignment.md)

## Kreditering

Denne leksjonen er laget med ♥️ av [Dmitry Soshnikov](http://soshnikov.com)

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.