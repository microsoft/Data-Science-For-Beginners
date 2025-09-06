<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a49d78e32e280c410f04e5f2a2068e77",
  "translation_date": "2025-09-05T22:43:25+00:00",
  "source_file": "3-Data-Visualization/09-visualization-quantities/README.md",
  "language_code": "fi"
}
-->
# Määrien visualisointi

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/09-Visualizing-Quantities.png)|
|:---:|
| Määrien visualisointi - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

Tässä oppitunnissa opit käyttämään yhtä monista Python-kirjastoista luodaksesi mielenkiintoisia visualisointeja määrän käsitteen ympärillä. Käyttämällä puhdistettua tietojoukkoa Minnesotan linnuista voit oppia monia mielenkiintoisia faktoja paikallisesta eläimistöstä.  
## [Esiluentavisa](https://ff-quizzes.netlify.app/en/ds/quiz/16)

## Tarkastele siipiväliä Matplotlibilla

Erinomainen kirjasto erilaisten yksinkertaisten ja monimutkaisten kaavioiden ja kuvaajien luomiseen on [Matplotlib](https://matplotlib.org/stable/index.html). Yleisesti ottaen tietojen visualisointi näiden kirjastojen avulla sisältää seuraavat vaiheet: määritä, mitä osia tietokehyksestäsi haluat käyttää, tee tarvittavat muunnokset, määritä x- ja y-akselin arvot, päätä, millainen kaavio halutaan näyttää, ja näytä kaavio. Matplotlib tarjoaa laajan valikoiman visualisointeja, mutta tässä oppitunnissa keskitymme niihin, jotka sopivat parhaiten määrien visualisointiin: viivakaaviot, hajontakaaviot ja pylväskaaviot.

> ✅ Valitse paras kaavio tietosi rakenteen ja kertomasi tarinan mukaan.  
> - Aikatrendien analysointiin: viivakaavio  
> - Arvojen vertailuun: pylväs-, palkki-, piirakka- tai hajontakaavio  
> - Osien ja kokonaisuuden suhteen näyttämiseen: piirakkakaavio  
> - Tietojen jakauman näyttämiseen: hajonta- tai pylväskaavio  
> - Trendien näyttämiseen: viiva- tai palkkikaavio  
> - Arvojen välisten suhteiden näyttämiseen: viiva-, hajonta- tai kuplakaavio  

Jos sinulla on tietojoukko ja haluat selvittää, kuinka paljon tiettyä kohdetta on mukana, ensimmäinen tehtäväsi on tarkastella sen arvoja.  

✅ Matplotlibille on saatavilla erinomaisia 'lunttilappuja' [täällä](https://matplotlib.org/cheatsheets/cheatsheets.pdf).

## Luo viivakaavio lintujen siipiväliarvoista

Avaa tämän oppitunnin kansion juuresta tiedosto `notebook.ipynb` ja lisää solu.

> Huom: tiedot on tallennettu tämän repositorion juureen `/data`-kansioon.

```python
import pandas as pd
import matplotlib.pyplot as plt
birds = pd.read_csv('../../data/birds.csv')
birds.head()
```  
Nämä tiedot sisältävät sekä tekstiä että numeroita:

|      | Nimi                          | TieteellinenNimi       | Kategoria             | Lahko         | Heimo    | Suku         | Suojelustatus       | MinPituus | MaxPituus | MinPaino    | MaxPaino    | MinSiipiväli | MaxSiipiväli |
| ---: | :---------------------------- | :--------------------- | :-------------------- | :------------ | :------- | :----------- | :----------------- | --------: | --------: | ----------: | ----------: | -----------: | -----------: |
|    0 | Mustavatsaviheltäjäsorsa      | Dendrocygna autumnalis | Sorsat/hanhet/vesilinnut | Anseriformes | Anatidae | Dendrocygna  | LC                 |        47 |        56 |         652 |        1020 |          76  |          94  |
|    1 | Ruostoviheltäjäsorsa          | Dendrocygna bicolor    | Sorsat/hanhet/vesilinnut | Anseriformes | Anatidae | Dendrocygna  | LC                 |        45 |        53 |         712 |        1050 |          85  |          93  |
|    2 | Lumihanhi                     | Anser caerulescens     | Sorsat/hanhet/vesilinnut | Anseriformes | Anatidae | Anser        | LC                 |        64 |        79 |        2050 |        4050 |         135  |         165  |
|    3 | Rossin hanhi                  | Anser rossii           | Sorsat/hanhet/vesilinnut | Anseriformes | Anatidae | Anser        | LC                 |      57.3 |        64 |        1066 |        1567 |         113  |         116  |
|    4 | Metsähanhi                    | Anser albifrons        | Sorsat/hanhet/vesilinnut | Anseriformes | Anatidae | Anser        | LC                 |        64 |        81 |        1930 |        3310 |         130  |         165  |

Aloitetaan piirtämällä joitakin numeerisia tietoja perusviivakaavion avulla. Oletetaan, että haluat tarkastella näiden lintujen maksimisiipiväliä.

```python
wingspan = birds['MaxWingspan'] 
wingspan.plot()
```  
![Max Wingspan](../../../../3-Data-Visualization/09-visualization-quantities/images/max-wingspan-02.png)

Mitä huomaat heti? Näyttää siltä, että ainakin yksi poikkeava arvo on mukana – melko vaikuttava siipiväli! 2300 senttimetrin siipiväli vastaa 23 metriä – liikkuuko Minnesotassa pterodaktyylejä? Tutkitaanpa asiaa.

Vaikka voisit tehdä nopean lajittelun Excelissä löytääksesi nämä poikkeamat, jotka ovat todennäköisesti kirjoitusvirheitä, jatka visualisointiprosessia työskentelemällä suoraan kaavion kanssa.

Lisää x-akselille tunnisteet, jotka näyttävät, mistä linnuista on kyse:

```
plt.title('Max Wingspan in Centimeters')
plt.ylabel('Wingspan (CM)')
plt.xlabel('Birds')
plt.xticks(rotation=45)
x = birds['Name'] 
y = birds['MaxWingspan']

plt.plot(x, y)

plt.show()
```  
![wingspan with labels](../../../../3-Data-Visualization/09-visualization-quantities/images/max-wingspan-labels-02.png)

Vaikka tunnisteiden kiertokulma on asetettu 45 asteeseen, niitä on silti liikaa luettavaksi. Kokeillaan toista strategiaa: merkitään vain poikkeamat ja asetetaan tunnisteet kaavion sisälle. Voit käyttää hajontakaaviota tehdäksesi tilaa tunnisteille:

```python
plt.title('Max Wingspan in Centimeters')
plt.ylabel('Wingspan (CM)')
plt.tick_params(axis='both',which='both',labelbottom=False,bottom=False)

for i in range(len(birds)):
    x = birds['Name'][i]
    y = birds['MaxWingspan'][i]
    plt.plot(x, y, 'bo')
    if birds['MaxWingspan'][i] > 500:
        plt.text(x, y * (1 - 0.05), birds['Name'][i], fontsize=12)
    
plt.show()
```  
Mitä tässä tapahtuu? Käytit `tick_params`-funktiota piilottaaksesi alareunan tunnisteet ja loit sitten silmukan lintudatasetin yli. Piirtämällä kaavion pienillä sinisillä pisteillä käyttämällä `bo`, tarkistit, onko linnulla maksimisiipiväli yli 500, ja näytit sen nimen pisteen vieressä, jos näin oli. Siirsit tunnisteita hieman y-akselilla (`y * (1 - 0.05)`) ja käytit linnun nimeä tunnisteena.

Mitä havaitsit?

![outliers](../../../../3-Data-Visualization/09-visualization-quantities/images/labeled-wingspan-02.png)  
## Suodata tietosi

Sekä valkopäämerikotka että preeriakotka, vaikka ne ovatkin todennäköisesti suuria lintuja, näyttävät olevan virheellisesti merkittyjä, ja niiden maksimisiipiväliin on lisätty ylimääräinen `0`. On epätodennäköistä, että kohtaisit valkopäämerikotkan, jonka siipiväli on 25 metriä, mutta jos näin käy, kerro meille! Luodaan uusi tietokehys ilman näitä kahta poikkeamaa:

```python
plt.title('Max Wingspan in Centimeters')
plt.ylabel('Wingspan (CM)')
plt.xlabel('Birds')
plt.tick_params(axis='both',which='both',labelbottom=False,bottom=False)
for i in range(len(birds)):
    x = birds['Name'][i]
    y = birds['MaxWingspan'][i]
    if birds['Name'][i] not in ['Bald eagle', 'Prairie falcon']:
        plt.plot(x, y, 'bo')
plt.show()
```  

Suodattamalla poikkeamat pois tietosi ovat nyt yhtenäisempiä ja helpommin ymmärrettäviä.

![scatterplot of wingspans](../../../../3-Data-Visualization/09-visualization-quantities/images/scatterplot-wingspan-02.png)

Nyt kun meillä on puhtaampi tietojoukko ainakin siipivälin osalta, tutkitaan lisää näitä lintuja.

Vaikka viiva- ja hajontakaaviot voivat näyttää tietoja arvoista ja niiden jakaumista, haluamme pohtia tämän tietojoukon sisältämiä arvoja. Voisit luoda visualisointeja vastataksesi seuraaviin kysymyksiin määristä:

> Kuinka monta lintukategoriaa on olemassa ja kuinka monta lintua niihin kuuluu?  
> Kuinka monta lintua on sukupuuttoon kuolleita, uhanalaisia, harvinaisia tai yleisiä?  
> Kuinka monta eri sukua ja lahkoa on Linnaeuksen terminologian mukaan?  
## Tutki pylväskaavioita

Pylväskaaviot ovat käytännöllisiä, kun haluat näyttää tietojen ryhmittelyjä. Tutkitaan tämän tietojoukon lintukategorioita nähdäksemme, mikä niistä on yleisin.

Luo peruspylväskaavio notebook-tiedostossa.

✅ Huomaa, että voit joko suodattaa pois aiemmin tunnistetut kaksi poikkeavaa lintua, korjata niiden siipiväliin liittyvän kirjoitusvirheen tai jättää ne mukaan näihin harjoituksiin, jotka eivät riipu siipiväliarvoista.

Jos haluat luoda pylväskaavion, voit valita tiedot, joihin haluat keskittyä. Pylväskaavioita voidaan luoda raakadatan perusteella:

```python
birds.plot(x='Category',
        kind='bar',
        stacked=True,
        title='Birds of Minnesota')

```  
![full data as a bar chart](../../../../3-Data-Visualization/09-visualization-quantities/images/full-data-bar-02.png)

Tämä pylväskaavio on kuitenkin lukukelvoton, koska siinä on liikaa ryhmittelemätöntä dataa. Sinun täytyy valita vain ne tiedot, jotka haluat piirtää, joten tarkastellaan lintujen pituutta niiden kategorian perusteella.

Suodata tietosi sisältämään vain lintujen kategoriat.

✅ Huomaa, että käytät Pandasia tietojen hallintaan ja annat Matplotlibin hoitaa kaavioiden piirtämisen.

Koska kategorioita on paljon, voit näyttää tämän kaavion pystysuunnassa ja säätää sen korkeutta, jotta kaikki tiedot mahtuvat mukaan:

```python
category_count = birds.value_counts(birds['Category'].values, sort=True)
plt.rcParams['figure.figsize'] = [6, 12]
category_count.plot.barh()
```  
![category and length](../../../../3-Data-Visualization/09-visualization-quantities/images/category-counts-02.png)

Tämä pylväskaavio antaa hyvän yleiskuvan lintujen lukumäärästä kategoriaa kohden. Silmänräpäyksessä näet, että suurin osa tämän alueen linnuista kuuluu kategoriaan Sorsat/hanhet/vesilinnut. Minnesota on "10 000 järven maa", joten tämä ei ole yllättävää!

✅ Kokeile joitakin muita laskentoja tästä tietojoukosta. Yllättääkö jokin sinua?

## Tietojen vertailu

Voit kokeilla eri ryhmiteltyjen tietojen vertailuja luomalla uusia akseleita. Kokeile vertailla lintujen MaxPituutta niiden kategorian perusteella:

```python
maxlength = birds['MaxLength']
plt.barh(y=birds['Category'], width=maxlength)
plt.rcParams['figure.figsize'] = [6, 12]
plt.show()
```  
![comparing data](../../../../3-Data-Visualization/09-visualization-quantities/images/category-length-02.png)

Tässä ei ole mitään yllättävää: kolibrit ovat pienimpiä MaxPituuden osalta verrattuna pelikaaniin tai hanhiin. On hyvä, kun tiedot ovat loogisia!

Voit luoda mielenkiintoisempia pylväskaavioita päällekkäistämällä tietoja. Päällekkäistään Minimi- ja Maksimipituus tietyn lintukategorian kohdalla:

```python
minLength = birds['MinLength']
maxLength = birds['MaxLength']
category = birds['Category']

plt.barh(category, maxLength)
plt.barh(category, minLength)

plt.show()
```  
Tässä kaaviossa näet kunkin lintukategorian Minimi- ja Maksimipituuden vaihteluvälin. Voit turvallisesti todeta, että tämän datan perusteella mitä suurempi lintu, sitä laajempi sen pituusvaihteluväli. Mielenkiintoista!

![superimposed values](../../../../3-Data-Visualization/09-visualization-quantities/images/superimposed-02.png)

## 🚀 Haaste

Tämä lintudatasetti tarjoaa runsaasti tietoa eri lintutyypeistä tietyssä ekosysteemissä. Etsi internetistä muita lintuihin liittyviä tietojoukkoja. Harjoittele kaavioiden ja kuvaajien luomista näiden lintujen ympärille löytääksesi faktoja, joita et aiemmin tiennyt.

## [Jälkiluentavisa](https://ff-quizzes.netlify.app/en/ds/quiz/17)

## Kertaus ja itseopiskelu

Tämä ensimmäinen oppitunti on antanut sinulle tietoa siitä, miten Matplotlibia käytetään määrien visualisointiin. Tee tutkimusta muista tavoista työskennellä tietojoukkojen kanssa visualisointia varten. [Plotly](https://github.com/plotly/plotly.py) on yksi, jota emme käsittele näissä oppitunneissa, joten tutustu siihen, mitä se voi tarjota.  
## Tehtävä

[Viivat, hajonnat ja pylväät](assignment.md)

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulee pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskääntämistä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinkäsityksistä tai virhetulkinnoista.