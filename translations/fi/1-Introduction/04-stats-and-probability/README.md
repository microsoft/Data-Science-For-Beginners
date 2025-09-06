<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1cf49f029ba1f25a54f0d5bc2fa575fc",
  "translation_date": "2025-09-05T22:47:04+00:00",
  "source_file": "1-Introduction/04-stats-and-probability/README.md",
  "language_code": "fi"
}
-->
# Lyhyt johdatus tilastotieteeseen ja todennäköisyyksiin

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/04-Statistics-Probability.png)|
|:---:|
| Tilastotiede ja todennäköisyydet - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

Tilastotiede ja todennäköisyysteoria ovat kaksi läheisesti toisiinsa liittyvää matematiikan osa-aluetta, jotka ovat erittäin merkityksellisiä datatieteessä. Vaikka dataa voi käsitellä ilman syvällistä matematiikan tuntemusta, on silti hyödyllistä ymmärtää ainakin peruskäsitteet. Tässä esittelemme lyhyen johdannon, joka auttaa sinua pääsemään alkuun.

[![Intro Video](../../../../1-Introduction/04-stats-and-probability/images/video-prob-and-stats.png)](https://youtu.be/Z5Zy85g4Yjw)

## [Ennakkokysely ennen luentoa](https://ff-quizzes.netlify.app/en/ds/quiz/6)

## Todennäköisyys ja satunnaismuuttujat

**Todennäköisyys** on luku välillä 0 ja 1, joka ilmaisee, kuinka todennäköinen jokin **tapahtuma** on. Se määritellään positiivisten lopputulosten (jotka johtavat tapahtumaan) lukumääränä jaettuna kaikkien lopputulosten lukumäärällä, olettaen että kaikki lopputulokset ovat yhtä todennäköisiä. Esimerkiksi, kun heitämme noppaa, todennäköisyys saada parillinen luku on 3/6 = 0.5.

Kun puhumme tapahtumista, käytämme **satunnaismuuttujia**. Esimerkiksi satunnaismuuttuja, joka edustaa nopanheiton tulosta, voi saada arvoja välillä 1–6. Lukuja 1–6 kutsutaan **otosavaruudeksi**. Voimme puhua satunnaismuuttujan todennäköisyydestä saada tietty arvo, esimerkiksi P(X=3)=1/6.

Edellä mainittu satunnaismuuttuja on **diskreetti**, koska sen otosavaruus on laskettavissa, eli siinä on erillisiä arvoja, jotka voidaan luetella. On myös tapauksia, joissa otosavaruus on reaaliarvojen väli tai koko reaaliarvojen joukko. Tällaisia muuttujia kutsutaan **jatkuviksi**. Hyvä esimerkki on bussin saapumisaika.

## Todennäköisyysjakauma

Diskreettien satunnaismuuttujien tapauksessa on helppo kuvata kunkin tapahtuman todennäköisyys funktiolla P(X). Jokaiselle otosavaruuden *S* arvolle *s* funktio antaa luvun välillä 0 ja 1, siten että kaikkien P(X=s) arvojen summa on 1.

Tunnetuin diskreetti jakauma on **tasajakauma**, jossa otosavaruudessa on N elementtiä, ja jokaisen elementin todennäköisyys on 1/N.

Jatkuvan muuttujan todennäköisyysjakauman kuvaaminen on vaikeampaa, kun arvot ovat peräisin jostain välistä [a,b] tai koko reaaliarvojen joukosta ℝ. Mietitään esimerkiksi bussin saapumisaikaa. Todellisuudessa todennäköisyys, että bussi saapuu täsmälleen tiettynä aikana *t*, on 0!

> Nyt tiedät, että tapahtumat, joiden todennäköisyys on 0, tapahtuvat – ja vieläpä usein! Ainakin joka kerta, kun bussi saapuu!

Voimme puhua vain todennäköisyydestä, että muuttuja osuu tiettyyn arvojen väliin, esim. P(t<sub>1</sub>≤X<t<sub>2</sub>). Tässä tapauksessa todennäköisyysjakauma kuvataan **todennäköisyystiheysfunktiolla** p(x), siten että

![P(t_1\le X<t_2)=\int_{t_1}^{t_2}p(x)dx](../../../../1-Introduction/04-stats-and-probability/images/probability-density.png)

Jatkuvan tasajakauman analogi on **jatkuva tasajakauma**, joka määritellään rajallisella välillä. Todennäköisyys, että arvo X osuu väliin, jonka pituus on l, on verrannollinen l:ään ja kasvaa arvoon 1.

Toinen tärkeä jakauma on **normaalijakauma**, josta puhumme tarkemmin myöhemmin.

## Keskiarvo, varianssi ja keskihajonta

Oletetaan, että otamme satunnaismuuttujasta X n näytettä: x<sub>1</sub>, x<sub>2</sub>, ..., x<sub>n</sub>. Voimme määritellä **keskiarvon** (tai **aritmeettisen keskiarvon**) perinteisellä tavalla: (x<sub>1</sub>+x<sub>2</sub>+x<sub>n</sub>)/n. Kun kasvatamme otoksen kokoa (eli otamme rajan n→∞), saamme jakauman keskiarvon (jota kutsutaan myös **odotusarvoksi**). Merkitsemme odotusarvoa **E**(x).

> On osoitettu, että mille tahansa diskreetille jakaumalle, jonka arvot ovat {x<sub>1</sub>, x<sub>2</sub>, ..., x<sub>N</sub>} ja vastaavat todennäköisyydet p<sub>1</sub>, p<sub>2</sub>, ..., p<sub>N</sub>, odotusarvo on E(X)=x<sub>1</sub>p<sub>1</sub>+x<sub>2</sub>p<sub>2</sub>+...+x<sub>N</sub>p<sub>N</sub>.

Arvojen hajonnan tunnistamiseksi voimme laskea varianssin σ<sup>2</sup> = ∑(x<sub>i</sub> - μ)<sup>2</sup>/n, missä μ on otoksen keskiarvo. Arvoa σ kutsutaan **keskihajonnaksi**, ja σ<sup>2</sup> on **varianssi**.

## Moodi, mediaani ja kvartiilit

Joskus keskiarvo ei kuvaa riittävän hyvin "tyypillistä" arvoa datalle. Esimerkiksi, jos datassa on muutama äärimmäinen arvo, ne voivat vaikuttaa keskiarvoon. Toinen hyvä indikaattori on **mediaani**, arvo, jonka alapuolella on puolet datan pisteistä ja yläpuolella toinen puoli.

Datan jakauman ymmärtämiseksi on hyödyllistä puhua **kvartiileista**:

* Ensimmäinen kvartiili, eli Q1, on arvo, jonka alapuolella on 25 % datasta
* Kolmas kvartiili, eli Q3, on arvo, jonka alapuolella on 75 % datasta

Graafisesti voimme kuvata mediaanin ja kvartiilien suhdetta diagrammilla, jota kutsutaan **laatikko-kaavioksi**:

<img src="images/boxplot_explanation.png" width="50%"/>

Tässä laskemme myös **kvartiilivälin** IQR=Q3-Q1 ja niin sanotut **poikkeamat** – arvot, jotka ovat alueen [Q1-1.5*IQR,Q3+1.5*IQR] ulkopuolella.

Pienelle diskreetille jakaumalle, jossa on vain muutama mahdollinen arvo, hyvä "tyypillinen" arvo on se, joka esiintyy useimmin, ja sitä kutsutaan **moodiksi**. Moodia käytetään usein kategoriselle datalle, kuten väreille. Mietitään tilannetta, jossa meillä on kaksi ryhmää ihmisiä – osa suosii vahvasti punaista ja osa sinistä. Jos koodaisimme värit numeroilla, keskiarvo suosikkivärille olisi jossain oranssin ja vihreän välillä, mikä ei kuvaisi kummankaan ryhmän todellista mieltymystä. Moodi sen sijaan olisi joko yksi väreistä tai molemmat, jos niiden kannattajien määrä on sama (tässä tapauksessa otosta kutsutaan **multimodaaliseksi**).

## Reaaliaikainen data

Kun analysoimme tosielämän dataa, ne eivät usein ole varsinaisia satunnaismuuttujia siinä mielessä, että emme tee kokeita tuntemattomalla tuloksella. Esimerkiksi, mietitään baseball-joukkueen pelaajia ja heidän kehon tietojaan, kuten pituutta, painoa ja ikää. Nämä luvut eivät ole täysin satunnaisia, mutta voimme silti soveltaa samoja matemaattisia käsitteitä. Esimerkiksi ihmisten painojen sarjaa voidaan pitää satunnaismuuttujasta otettuna arvosarjana. Alla on Major League Baseball -pelaajien painojen sarja, joka on otettu [tästä datasetistä](http://wiki.stat.ucla.edu/socr/index.php/SOCR_Data_MLB_HeightsWeights) (mukavuuden vuoksi vain ensimmäiset 20 arvoa näytetään):

```
[180.0, 215.0, 210.0, 210.0, 188.0, 176.0, 209.0, 200.0, 231.0, 180.0, 188.0, 180.0, 185.0, 160.0, 180.0, 185.0, 197.0, 189.0, 185.0, 219.0]
```

> **Huomio**: Katso esimerkki tämän datasetin käsittelystä [liitteenä olevasta muistikirjasta](../../../../1-Introduction/04-stats-and-probability/notebook.ipynb). Tässä oppitunnissa on myös useita haasteita, jotka voit suorittaa lisäämällä koodia muistikirjaan. Jos et ole varma, miten dataa käsitellään, älä huoli – palaamme datan käsittelyyn Pythonilla myöhemmin. Jos et tiedä, miten suorittaa koodia Jupyter Notebookissa, katso [tämä artikkeli](https://soshnikov.com/education/how-to-execute-notebooks-from-github/).

Tässä on laatikko-kaavio, joka näyttää datan keskiarvon, mediaanin ja kvartiilit:

![Painon laatikko-kaavio](../../../../1-Introduction/04-stats-and-probability/images/weight-boxplot.png)

Koska datamme sisältää tietoa eri pelaajien **rooleista**, voimme myös tehdä laatikko-kaavion roolin mukaan – tämä antaa meille käsityksen siitä, miten parametrit eroavat roolien välillä. Tällä kertaa tarkastelemme pituutta:

![Laatikko-kaavio roolin mukaan](../../../../1-Introduction/04-stats-and-probability/images/boxplot_byrole.png)

Tämä diagrammi viittaa siihen, että keskimäärin ensimmäisen pesän pelaajien pituus on suurempi kuin toisen pesän pelaajien pituus. Myöhemmin tässä oppitunnissa opimme, miten voimme testata tätä hypoteesia muodollisemmin ja miten voimme osoittaa, että datamme on tilastollisesti merkittävää tämän osoittamiseksi.

> Kun työskentelemme tosielämän datan kanssa, oletamme, että kaikki datapisteet ovat otoksia jostain todennäköisyysjakaumasta. Tämä oletus mahdollistaa koneoppimistekniikoiden soveltamisen ja toimivien ennustemallien rakentamisen.

Jotta voimme nähdä, millainen datamme jakauma on, voimme piirtää diagrammin, jota kutsutaan **histogrammiksi**. X-akselilla on eri painovälien lukumäärä (niin sanotut **binssit**), ja pystyakseli näyttää, kuinka monta kertaa satunnaismuuttujan otos osui tiettyyn väliin.

![Reaaliaikaisen datan histogrammi](../../../../1-Introduction/04-stats-and-probability/images/weight-histogram.png)

Tästä histogrammista näet, että kaikki arvot keskittyvät tietyn keskimääräisen painon ympärille, ja mitä kauemmas keskiarvosta mennään, sitä harvemmin kyseistä painoa esiintyy. Eli on hyvin epätodennäköistä, että baseball-pelaajan paino poikkeaisi merkittävästi keskiarvosta. Painojen varianssi osoittaa, kuinka paljon painot todennäköisesti eroavat keskiarvosta.

> Jos otamme muiden ihmisten painoja, jotka eivät ole baseball-liigasta, jakauma on todennäköisesti erilainen. Jakauman muoto pysyy kuitenkin samana, mutta keskiarvo ja varianssi muuttuvat. Jos siis koulutamme mallimme baseball-pelaajilla, se todennäköisesti antaa vääriä tuloksia, kun sitä sovelletaan yliopisto-opiskelijoihin, koska taustalla oleva jakauma on erilainen.

## Normaalijakauma

Painojen jakauma, jonka näimme yllä, on hyvin tyypillinen, ja monet tosielämän mittaukset noudattavat samaa tyyppistä jakaumaa, mutta eri keskiarvolla ja varianssilla. Tätä jakaumaa kutsutaan **normaalijakaumaksi**, ja sillä on erittäin tärkeä rooli tilastotieteessä.

Normaalijakauman käyttäminen on oikea tapa luoda satunnaisia painoja potentiaalisille baseball-pelaajille. Kun tiedämme keskimääräisen painon `mean` ja keskihajonnan `std`, voimme luoda 1000 painonäytettä seuraavalla tavalla:
```python
samples = np.random.normal(mean,std,1000)
``` 

Jos piirrämme histogrammin luoduista näytteistä, näemme kuvan, joka on hyvin samanlainen kuin yllä oleva. Ja jos lisäämme näytteiden määrää ja binssien määrää, voimme luoda kuvan normaalijakaumasta, joka on lähempänä ideaalista:

![Normaalijakauma, keskiarvo=0 ja keskihajonta=1](../../../../1-Introduction/04-stats-and-probability/images/normal-histogram.png)

*Normaalijakauma, keskiarvo=0 ja keskihajonta=1*

## Luottamusvälit

Kun puhumme baseball-pelaajien painoista, oletamme, että on olemassa tietty **satunnaismuuttuja W**, joka vastaa kaikkien baseball-pelaajien painojen ideaalista todennäköisyysjakaumaa (niin sanottu **populaatio**). Painojen sarjamme vastaa kaikkien baseball-pelaajien osajoukkoa, jota kutsumme **otokseksi**. Mielenkiintoinen kysymys on, voimmeko tietää W:n jakauman parametrit, eli populaation keskiarvon ja varianssin?

Helpoin vastaus olisi laskea otoksen keskiarvo ja varianssi. Kuitenkin voi käydä niin, että satunnainen otoksemme ei edusta tarkasti koko populaatiota. Siksi on järkevää puhua **luottamusvälistä**.

> **Luottamusväli** on arvio populaation todellisesta keskiarvosta otoksemme perusteella, joka on tietyllä todennäköisyydellä (tai **luottamustasolla**) tarkka.

Oletetaan, että meillä on otos X

1</sub>, ..., X<sub>n</sub> otoksestamme. Joka kerta, kun otamme otoksen jakaumastamme, saamme eri keskiarvon μ. Näin ollen μ voidaan pitää satunnaismuuttujana. **Luottamusväli** luottamustasolla p on arvojen pari (L<sub>p</sub>,R<sub>p</sub>), siten että **P**(L<sub>p</sub>≤μ≤R<sub>p</sub>) = p, eli todennäköisyys, että mitattu keskiarvo osuu välin sisään, on p.

On tämän lyhyen johdannon ulkopuolella käsitellä yksityiskohtaisesti, miten nämä luottamusvälit lasketaan. Lisätietoja löytyy [Wikipediasta](https://en.wikipedia.org/wiki/Confidence_interval). Lyhyesti sanottuna määrittelemme lasketun otoskeskiarvon jakauman suhteessa populaation todelliseen keskiarvoon, jota kutsutaan **Studentin jakaumaksi**.

> **Mielenkiintoinen fakta**: Studentin jakauma on nimetty matemaatikko William Sealy Gossetin mukaan, joka julkaisi tutkimuksensa salanimellä "Student". Hän työskenteli Guinnessin panimossa, ja erään version mukaan hänen työnantajansa ei halunnut yleisön tietävän, että he käyttivät tilastollisia testejä raaka-aineiden laadun määrittämiseen.

Jos haluamme arvioida populaation keskiarvon μ luottamustasolla p, meidän on otettava *(1-p)/2-prosenttipiste* Studentin jakaumasta A, joka voidaan joko hakea taulukoista tai laskea tilasto-ohjelmistojen sisäänrakennetuilla funktioilla (esim. Python, R jne.). Tällöin μ:n väli olisi X±A*D/√n, missä X on otoksen saatu keskiarvo ja D on keskihajonta.

> **Huomio**: Ohitamme myös tärkeän käsitteen [vapausasteet](https://en.wikipedia.org/wiki/Degrees_of_freedom_(statistics)), joka on tärkeä Studentin jakauman yhteydessä. Voit perehtyä syvällisemmin tilastotieteen kirjoihin ymmärtääksesi tämän käsitteen paremmin.

Esimerkki painojen ja pituuksien luottamusvälin laskemisesta löytyy [liitteenä olevista muistikirjoista](../../../../1-Introduction/04-stats-and-probability/notebook.ipynb).

| p | Painon keskiarvo |
|-----|----------------|
| 0.85 | 201.73±0.94 |
| 0.90 | 201.73±1.08 |
| 0.95 | 201.73±1.28 |

Huomaa, että mitä korkeampi luottamustodennäköisyys, sitä laajempi luottamusväli.

## Hypoteesin testaus

Baseball-pelaajien aineistossamme on erilaisia pelaajarooleja, jotka voidaan tiivistää alla olevaan taulukkoon (katso [liitteenä oleva muistikirja](../../../../1-Introduction/04-stats-and-probability/notebook.ipynb), miten tämä taulukko on laskettu):

| Rooli | Pituus | Paino | Lukumäärä |
|-------|--------|-------|-----------|
| Catcher | 72.723684 | 204.328947 | 76 |
| Designated_Hitter | 74.222222 | 220.888889 | 18 |
| First_Baseman | 74.000000 | 213.109091 | 55 |
| Outfielder | 73.010309 | 199.113402 | 194 |
| Relief_Pitcher | 74.374603 | 203.517460 | 315 |
| Second_Baseman | 71.362069 | 184.344828 | 58 |
| Shortstop | 71.903846 | 182.923077 | 52 |
| Starting_Pitcher | 74.719457 | 205.163636 | 221 |
| Third_Baseman | 73.044444 | 200.955556 | 45 |

Voimme huomata, että ensimmäisten basemenien keskipituus on suurempi kuin toisten basemenien. Näin ollen voimme olla taipuvaisia päättelemään, että **ensimmäiset basemenit ovat pidempiä kuin toiset basemenit**.

> Tätä väitettä kutsutaan **hypoteesiksi**, koska emme tiedä, onko se oikeasti totta vai ei.

Kuitenkin ei ole aina ilmeistä, voimmeko tehdä tämän johtopäätöksen. Kuten edellä keskustelimme, jokaisella keskiarvolla on siihen liittyvä luottamusväli, ja näin ollen tämä ero voi olla vain tilastollinen virhe. Tarvitsemme muodollisemman tavan testata hypoteesimme.

Lasketaan luottamusvälit erikseen ensimmäisten ja toisten basemenien pituuksille:

| Luottamus | Ensimmäiset basemenit | Toiset basemenit |
|-----------|-----------------------|------------------|
| 0.85 | 73.62..74.38 | 71.04..71.69 |
| 0.90 | 73.56..74.44 | 70.99..71.73 |
| 0.95 | 73.47..74.53 | 70.92..71.81 |

Voimme nähdä, että missään luottamustasossa välit eivät mene päällekkäin. Tämä todistaa hypoteesimme, että ensimmäiset basemenit ovat pidempiä kuin toiset basemenit.

Muodollisemmin, ratkaisemamme ongelma on nähdä, ovatko **kaksi todennäköisyysjakaumaa samat**, tai ainakin onko niillä samat parametrit. Riippuen jakaumasta, meidän on käytettävä erilaisia testejä. Jos tiedämme, että jakaumamme ovat normaalijakaumia, voimme soveltaa **[Studentin t-testiä](https://en.wikipedia.org/wiki/Student%27s_t-test)**.

Studentin t-testissä laskemme niin sanotun **t-arvon**, joka osoittaa keskiarvojen eron ottaen huomioon varianssin. On osoitettu, että t-arvo noudattaa **Studentin jakaumaa**, mikä mahdollistaa kynnysarvon saamisen annetulle luottamustasolle **p** (tämä voidaan laskea tai katsoa numeerisista taulukoista). Vertaillemme sitten t-arvoa tähän kynnysarvoon hyväksyäksemme tai hylätäksemme hypoteesin.

Pythonissa voimme käyttää **SciPy**-kirjastoa, joka sisältää `ttest_ind`-funktion (monien muiden hyödyllisten tilastollisten funktioiden lisäksi!). Se laskee t-arvon puolestamme ja tekee myös käänteisen luottamustason p-arvon haun, jotta voimme vain tarkastella luottamustasoa johtopäätöksen tekemiseksi.

Esimerkiksi vertailumme ensimmäisten ja toisten basemenien pituuksista antaa seuraavat tulokset: 
```python
from scipy.stats import ttest_ind

tval, pval = ttest_ind(df.loc[df['Role']=='First_Baseman',['Height']], df.loc[df['Role']=='Designated_Hitter',['Height']],equal_var=False)
print(f"T-value = {tval[0]:.2f}\nP-value: {pval[0]}")
```
```
T-value = 7.65
P-value: 9.137321189738925e-12
```
Tässä tapauksessa p-arvo on erittäin pieni, mikä tarkoittaa, että on vahvaa näyttöä siitä, että ensimmäiset basemenit ovat pidempiä.

On myös muita hypoteeseja, joita voimme haluta testata, esimerkiksi:
* Todistaa, että annettu otos noudattaa jotain jakaumaa. Oletimme esimerkiksi, että pituudet ovat normaalijakautuneita, mutta tämä vaatii muodollisen tilastollisen vahvistuksen.
* Todistaa, että otoksen keskiarvo vastaa jotain ennalta määriteltyä arvoa.
* Verrata useiden otosten keskiarvoja (esim. mikä on ero onnellisuustasoissa eri ikäryhmien välillä).

## Suurten lukujen laki ja keskeinen raja-arvolause

Yksi syy, miksi normaalijakauma on niin tärkeä, on niin sanottu **keskeinen raja-arvolause**. Oletetaan, että meillä on suuri otos riippumattomia N arvoja X<sub>1</sub>, ..., X<sub>N</sub>, jotka on otettu mistä tahansa jakaumasta, jonka keskiarvo on μ ja varianssi σ<sup>2</sup>. Tällöin, kun N on riittävän suuri (toisin sanoen, kun N→∞), keskiarvo Σ<sub>i</sub>X<sub>i</sub> on normaalijakautunut, keskiarvolla μ ja varianssilla σ<sup>2</sup>/N.

> Toinen tapa tulkita keskeistä raja-arvolausetta on sanoa, että riippumatta jakaumasta, kun lasket minkä tahansa satunnaismuuttujan arvojen summan keskiarvon, päädyt normaalijakaumaan.

Keskeisestä raja-arvolauseesta seuraa myös, että kun N→∞, otoskeskiarvon todennäköisyys olla yhtä suuri kuin μ lähestyy arvoa 1. Tätä kutsutaan **suurten lukujen laiksi**.

## Kovaranssi ja korrelaatio

Yksi asioista, joita data-analytiikka tekee, on löytää yhteyksiä datan välillä. Sanomme, että kaksi sarjaa **korreloivat**, kun ne käyttäytyvät samankaltaisesti samaan aikaan, eli ne joko nousevat/laskevat samanaikaisesti tai toinen sarja nousee, kun toinen laskee ja päinvastoin. Toisin sanoen, sarjojen välillä näyttää olevan jokin yhteys.

> Korrelaatio ei välttämättä tarkoita kausaalista suhdetta kahden sarjan välillä; joskus molemmat muuttujat voivat riippua jostain ulkoisesta syystä, tai voi olla puhdasta sattumaa, että kaksi sarjaa korreloivat. Kuitenkin vahva matemaattinen korrelaatio on hyvä osoitus siitä, että kaksi muuttujaa ovat jollain tavalla yhteydessä.

Matemaattisesti pääkäsite, joka osoittaa yhteyden kahden satunnaismuuttujan välillä, on **kovarianssi**, joka lasketaan näin: Cov(X,Y) = **E**\[(X-**E**(X))(Y-**E**(Y))\]. Laskemme molempien muuttujien poikkeaman niiden keskiarvoista ja sitten näiden poikkeamien tulon. Jos molemmat muuttujat poikkeavat yhdessä, tulo on aina positiivinen arvo, joka lisää positiivista kovarianssia. Jos molemmat muuttujat poikkeavat epäsynkronisesti (eli toinen laskee keskiarvon alapuolelle, kun toinen nousee keskiarvon yläpuolelle), saamme aina negatiivisia lukuja, jotka lisäävät negatiivista kovarianssia. Jos poikkeamat eivät ole riippuvaisia, ne summautuvat suunnilleen nollaan.

Kovarianssin itseisarvo ei kerro paljon siitä, kuinka suuri korrelaatio on, koska se riippuu todellisten arvojen suuruudesta. Normalisoidaksemme sen voimme jakaa kovarianssin molempien muuttujien keskihajonnalla saadaksemme **korrelaation**. Hyvä puoli on, että korrelaatio on aina välillä [-1,1], missä 1 tarkoittaa vahvaa positiivista korrelaatiota arvojen välillä, -1 vahvaa negatiivista korrelaatiota ja 0 ei korrelaatiota ollenkaan (muuttujat ovat riippumattomia).

**Esimerkki**: Voimme laskea korrelaation baseball-pelaajien painojen ja pituuksien välillä yllä mainitusta aineistosta:
```python
print(np.corrcoef(weights,heights))
```
Tuloksena saamme **korrelaatiomatriisin**, joka näyttää tältä:
```
array([[1.        , 0.52959196],
       [0.52959196, 1.        ]])
```

> Korrelaatiomatriisi C voidaan laskea mille tahansa määrälle syötesarjoja S<sub>1</sub>, ..., S<sub>n</sub>. C<sub>ij</sub>-arvo on korrelaatio S<sub>i</sub>:n ja S<sub>j</sub>:n välillä, ja diagonaalielementit ovat aina 1 (mikä on myös S<sub>i</sub>:n itsekorrelaatio).

Tässä tapauksessa arvo 0.53 osoittaa, että henkilön painon ja pituuden välillä on jonkin verran korrelaatiota. Voimme myös tehdä hajontakaavion yhdestä arvosta toista vastaan nähdäksesi suhteen visuaalisesti:

![Painon ja pituuden välinen suhde](../../../../1-Introduction/04-stats-and-probability/images/weight-height-relationship.png)

> Lisää esimerkkejä korrelaatiosta ja kovarianssista löytyy [liitteenä olevasta muistikirjasta](../../../../1-Introduction/04-stats-and-probability/notebook.ipynb).

## Yhteenveto

Tässä osiossa opimme:

* datan perus tilastolliset ominaisuudet, kuten keskiarvo, varianssi, moodi ja kvartiilit
* satunnaismuuttujien erilaiset jakaumat, mukaan lukien normaalijakauma
* kuinka löytää korrelaatio eri ominaisuuksien välillä
* kuinka käyttää matemaattisia ja tilastollisia menetelmiä hypoteesien todistamiseen
* kuinka laskea satunnaismuuttujan luottamusvälejä otoksen perusteella

Vaikka tämä ei olekaan tyhjentävä luettelo todennäköisyyslaskennan ja tilastotieteen aiheista, sen pitäisi antaa sinulle hyvä lähtökohta tähän kurssiin.

## 🚀 Haaste

Käytä muistikirjan esimerkkikoodia testataksesi muita hypoteeseja:
1. Ensimmäiset basemenit ovat vanhempia kuin toiset basemenit
2. Ensimmäiset basemenit ovat pidempiä kuin kolmannet basemenit
3. Shortstopit ovat pidempiä kuin toiset basemenit

## [Luennon jälkeinen kysely](https://ff-quizzes.netlify.app/en/ds/quiz/7)

## Kertaus ja itseopiskelu

Todennäköisyyslaskenta ja tilastotiede on niin laaja aihe, että se ansaitsee oman kurssinsa. Jos haluat syventyä teoriaan, voit jatkaa lukemista seuraavista kirjoista:

1. [Carlos Fernandez-Granda](https://cims.nyu.edu/~cfgranda/) New Yorkin yliopistosta on laatinut erinomaiset luentomuistiinpanot [Probability and Statistics for Data Science](https://cims.nyu.edu/~cfgranda/pages/stuff/probability_stats_for_DS.pdf) (saatavilla verkossa).
1. [Peter ja Andrew Bruce. Practical Statistics for Data Scientists.](https://www.oreilly.com/library/view/practical-statistics-for/9781491952955/) [[esimerkkikoodi R:llä](https://github.com/andrewgbruce/statistics-for-data-scientists)].
1. [James D. Miller. Statistics for Data Science](https://www.packtpub.com/product/statistics-for-data-science/9781788290678) [[esimerkkikoodi R:llä](https://github.com/PacktPublishing/Statistics-for-Data-Science)].

## Tehtävä

[Small Diabetes Study](assignment.md)

## Kiitokset

Tämän oppitunnin on laatinut ♥️:lla [Dmitry Soshnikov](http://soshnikov.com).

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä johtuvista väärinkäsityksistä tai virhetulkinnoista.