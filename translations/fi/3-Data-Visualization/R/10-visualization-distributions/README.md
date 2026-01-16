<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ea67c0c40808fd723594de6896c37ccf",
  "translation_date": "2025-08-26T22:58:42+00:00",
  "source_file": "3-Data-Visualization/R/10-visualization-distributions/README.md",
  "language_code": "fi"
}
-->
# Visualisoi jakaumia

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/sketchnotes/10-Visualizing-Distributions.png)|
|:---:|
| Jakaumien visualisointi - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

Edellisessä oppitunnissa opit mielenkiintoisia asioita Minnesotan lintudatasta. Löysit virheellisiä tietoja visualisoimalla poikkeamia ja tarkastelit lintukategorioiden eroja niiden maksimipituuden perusteella.

## [Esiluennon kysely](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/18)
## Tutki lintudataa

Toinen tapa tutkia dataa on tarkastella sen jakaumaa eli sitä, miten data on järjestetty akselilla. Ehkä haluaisit esimerkiksi oppia, miten tämän datasetin lintujen maksimisiipiväli tai maksimikehon massa jakautuu yleisesti.

Tutkitaanpa joitakin faktoja tämän datasetin jakaumista. Tuo `ggplot2` ja tietokanta R-konsoliisi. Poista poikkeamat tietokannasta samalla tavalla kuin edellisessä aiheessa.

```r
library(ggplot2)

birds <- read.csv("../../data/birds.csv",fileEncoding="UTF-8-BOM")

birds_filtered <- subset(birds, MaxWingspan < 500)
head(birds_filtered)
```
|      | Nimi                         | TieteellinenNimi       | Kategoria             | Lahko        | Heimo    | Suku        | Suojelustatus       | MinPituus | MaxPituus | MinKehonMassa | MaxKehonMassa | MinSiipiväli | MaxSiipiväli |
| ---: | :--------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :----------------- | --------: | --------: | ------------: | ------------: | -----------: | -----------: |
|    0 | Mustavatsaviheltäjäsorsa     | Dendrocygna autumnalis | Sorsat/hanhet/vesilinnut | Anseriformes | Anatidae | Dendrocygna | LC                 |        47 |        56 |           652 |          1020 |           76 |           94 |
|    1 | Ruostoviheltäjäsorsa         | Dendrocygna bicolor    | Sorsat/hanhet/vesilinnut | Anseriformes | Anatidae | Dendrocygna | LC                 |        45 |        53 |           712 |          1050 |           85 |           93 |
|    2 | Lumihanhi                    | Anser caerulescens     | Sorsat/hanhet/vesilinnut | Anseriformes | Anatidae | Anser       | LC                 |        64 |        79 |          2050 |          4050 |          135 |          165 |
|    3 | Rossin hanhi                 | Anser rossii           | Sorsat/hanhet/vesilinnut | Anseriformes | Anatidae | Anser       | LC                 |      57.3 |        64 |          1066 |          1567 |          113 |          116 |
|    4 | Tundrahanhi                  | Anser albifrons        | Sorsat/hanhet/vesilinnut | Anseriformes | Anatidae | Anser       | LC                 |        64 |        81 |          1930 |          3310 |          130 |          165 |

Yleisesti ottaen voit nopeasti tarkastella datan jakaumaa käyttämällä hajontakaaviota, kuten teimme edellisessä oppitunnissa:

```r
ggplot(data=birds_filtered, aes(x=Order, y=MaxLength,group=1)) +
  geom_point() +
  ggtitle("Max Length per order") + coord_flip()
```
![maksimipituus per lahko](../../../../../translated_images/fi/max-length-per-order.e5b283d952c78c12b091307c5d3cf67132dad6fefe80a073353b9dc5c2bd3eb8.png)

Tämä antaa yleiskuvan kehon pituuden jakaumasta lintulahkoittain, mutta se ei ole paras tapa esittää todellisia jakaumia. Tätä tehtävää varten käytetään yleensä histogrammia.

## Työskentely histogrammien kanssa

`ggplot2` tarjoaa erinomaisia tapoja visualisoida datan jakaumia histogrammien avulla. Tämä kaaviotyyppi muistuttaa pylväsdiagrammia, jossa jakauma näkyy pylväiden nousuina ja laskuina. Histogrammin luomiseen tarvitset numeerista dataa. Histogrammin luomiseksi voit piirtää kaavion määrittämällä tyypiksi 'hist' histogrammia varten. Tämä kaavio näyttää MaxBodyMass-jakauman koko datasetin numeerisen datan osalta. Jakamalla data pienempiin osiin (binseihin) se voi näyttää datan arvojen jakauman:

```r
ggplot(data = birds_filtered, aes(x = MaxBodyMass)) + 
  geom_histogram(bins=10)+ylab('Frequency')
```
![jakauma koko datasetissä](../../../../../translated_images/fi/distribution-over-the-entire-dataset.d22afd3fa96be854e4c82213fedec9e3703cba753d07fad4606aadf58cf7e78e.png)

Kuten näet, suurin osa tämän datasetin yli 400 linnusta kuuluu alle 2000:n Max Body Mass -alueeseen. Saat lisää tietoa datasta muuttamalla `bins`-parametrin suuremmaksi, esimerkiksi 30:ksi:

```r
ggplot(data = birds_filtered, aes(x = MaxBodyMass)) + geom_histogram(bins=30)+ylab('Frequency')
```

![jakauma-30bins](../../../../../translated_images/fi/distribution-30bins.6a3921ea7a421bf71f06bf5231009e43d1146f1b8da8dc254e99b5779a4983e5.png)

Tämä kaavio näyttää jakauman hieman tarkemmin. Vähemmän vasemmalle vinoutunut kaavio voidaan luoda varmistamalla, että valitset vain tietyn alueen sisällä olevan datan:

Suodata dataa saadaksesi vain ne linnut, joiden kehon massa on alle 60, ja näytä 30 `bins`:

```r
birds_filtered_1 <- subset(birds_filtered, MaxBodyMass > 1 & MaxBodyMass < 60)
ggplot(data = birds_filtered_1, aes(x = MaxBodyMass)) + 
  geom_histogram(bins=30)+ylab('Frequency')
```

![suodatettu histogrammi](../../../../../translated_images/fi/filtered-histogram.6bf5d2bfd82533220e1bd4bc4f7d14308f43746ed66721d9ec8f460732be6674.png)

✅ Kokeile muita suodattimia ja datapisteitä. Näyttääksesi datan koko jakauman, poista `['MaxBodyMass']`-suodatin ja näytä nimettyjä jakaumia.

Histogrammi tarjoaa myös mukavia väri- ja nimikointiparannuksia, joita voit kokeilla:

Luo 2D-histogrammi vertaillaksesi kahden jakauman välistä suhdetta. Verrataan `MaxBodyMass` ja `MaxLength`. `ggplot2` tarjoaa sisäänrakennetun tavan näyttää yhtymäkohdat kirkkaampien värien avulla:

```r
ggplot(data=birds_filtered_1, aes(x=MaxBodyMass, y=MaxLength) ) +
  geom_bin2d() +scale_fill_continuous(type = "viridis")
```
Näyttää siltä, että näiden kahden elementin välillä on odotettu korrelaatio odotetun akselin mukaisesti, ja yksi erityisen vahva yhtymäkohta:

![2d kaavio](../../../../../translated_images/fi/2d-plot.c504786f439bd7ebceebf2465c70ca3b124103e06c7ff7214bf24e26f7aec21e.png)

Histogrammit toimivat oletuksena hyvin numeeriselle datalle. Entä jos haluat nähdä jakaumia tekstidatan perusteella? 
## Tutki datasettiä jakaumien osalta tekstidatan avulla 

Tämä datasetti sisältää myös hyvää tietoa lintukategoriasta sekä niiden suvusta, lajista ja heimosta sekä suojelustatuksesta. Tutkitaanpa tätä suojelustatustietoa. Mikä on lintujen jakauma niiden suojelustatuksen mukaan?

> ✅ Datasetissä käytetään useita lyhenteitä kuvaamaan suojelustatusta. Nämä lyhenteet tulevat [IUCN:n uhanalaisuusluokituksista](https://www.iucnredlist.org/), joka luokittelee lajien tilaa.
> 
> - CR: Äärimmäisen uhanalainen
> - EN: Erittäin uhanalainen
> - EX: Sukupuuttoon kuollut
> - LC: Elinvoimainen
> - NT: Silmälläpidettävä
> - VU: Vaarantunut

Nämä ovat tekstipohjaisia arvoja, joten sinun täytyy tehdä muunnos histogrammin luomiseksi. Käytä filteredBirds-dataframea ja näytä sen suojelustatus yhdessä minimisiipivälin kanssa. Mitä huomaat? 

```r
birds_filtered_1$ConservationStatus[birds_filtered_1$ConservationStatus == 'EX'] <- 'x1' 
birds_filtered_1$ConservationStatus[birds_filtered_1$ConservationStatus == 'CR'] <- 'x2'
birds_filtered_1$ConservationStatus[birds_filtered_1$ConservationStatus == 'EN'] <- 'x3'
birds_filtered_1$ConservationStatus[birds_filtered_1$ConservationStatus == 'NT'] <- 'x4'
birds_filtered_1$ConservationStatus[birds_filtered_1$ConservationStatus == 'VU'] <- 'x5'
birds_filtered_1$ConservationStatus[birds_filtered_1$ConservationStatus == 'LC'] <- 'x6'

ggplot(data=birds_filtered_1, aes(x = MinWingspan, fill = ConservationStatus)) +
  geom_histogram(position = "identity", alpha = 0.4, bins = 20) +
  scale_fill_manual(name="Conservation Status",values=c("red","green","blue","pink"),labels=c("Endangered","Near Threathened","Vulnerable","Least Concern"))
```

![siipiväli ja suojelustatus](../../../../../translated_images/fi/wingspan-conservation-collation.4024e9aa6910866aa82f0c6cb6a6b4b925bd10079e6b0ef8f92eefa5a6792f76.png)

Näyttää siltä, ettei minimisiipivälin ja suojelustatuksen välillä ole selvää korrelaatiota. Testaa datasetin muita elementtejä tällä menetelmällä. Voit kokeilla myös erilaisia suodattimia. Löydätkö mitään korrelaatiota?

## Tiheyskäyrät

Olet ehkä huomannut, että tähän mennessä tarkastellut histogrammit ovat "askelmaisia" eivätkä virtaa tasaisesti kaarena. Näyttääksesi tasaisemman tiheyskäyrän voit kokeilla tiheyskäyrää.

Työskennellään nyt tiheyskäyrien parissa!

```r
ggplot(data = birds_filtered_1, aes(x = MinWingspan)) + 
  geom_density()
```
![tiheyskäyrä](../../../../../translated_images/fi/density-plot.675ccf865b76c690487fb7f69420a8444a3515f03bad5482886232d4330f5c85.png)

Näet, kuinka käyrä muistuttaa aiempaa minimisiipivälin kaaviota; se on vain hieman tasaisempi. Jos haluat tarkastella uudelleen sitä epätasaista MaxBodyMass-käyrää, jonka loit toisessa kaaviossa, voit tasoittaa sen hyvin luomalla sen uudelleen tällä menetelmällä:

```r
ggplot(data = birds_filtered_1, aes(x = MaxBodyMass)) + 
  geom_density()
```
![kehon massan tiheys](../../../../../translated_images/fi/bodymass-smooth.d31ce526d82b0a1f19a073815dea28ecfbe58145ec5337e4ef7e8cdac81120b3.png)

Jos haluat tasaisen, mutta ei liian tasaisen käyrän, muokkaa `adjust`-parametria: 

```r
ggplot(data = birds_filtered_1, aes(x = MaxBodyMass)) + 
  geom_density(adjust = 1/5)
```
![vähemmän tasainen kehon massa](../../../../../translated_images/fi/less-smooth-bodymass.10f4db8b683cc17d17b2d33f22405413142004467a1493d416608dafecfdee23.png)

✅ Lue tämän kaaviotyypin käytettävissä olevista parametreista ja kokeile!

Tämä kaaviotyyppi tarjoaa kauniita ja selittäviä visualisointeja. Esimerkiksi muutamalla koodirivillä voit näyttää lintulahkojen maksimikehon massan tiheyden:

```r
ggplot(data=birds_filtered_1,aes(x = MaxBodyMass, fill = Order)) +
  geom_density(alpha=0.5)
```
![kehon massa per lahko](../../../../../translated_images/fi/bodymass-per-order.9d2b065dd931b928c839d8cdbee63067ab1ae52218a1b90717f4bc744354f485.png)

## 🚀 Haaste

Histogrammit ovat kehittyneempiä kaaviotyyppejä kuin perushajontakaaviot, pylväsdiagrammit tai viivakaaviot. Etsi internetistä hyviä esimerkkejä histogrammien käytöstä. Miten niitä käytetään, mitä ne osoittavat ja millä aloilla tai tutkimusalueilla niitä yleensä käytetään?

## [Jälkiluennon kysely](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/19)

## Kertaus ja itseopiskelu

Tässä oppitunnissa käytit `ggplot2`:ta ja aloitit kehittyneempien kaavioiden luomisen. Tee tutkimusta `geom_density_2d()`-funktiosta, joka on "jatkuva todennäköisyystiheyskäyrä yhdessä tai useammassa ulottuvuudessa". Lue [dokumentaatio](https://ggplot2.tidyverse.org/reference/geom_density_2d.html) ymmärtääksesi, miten se toimii.

## Tehtävä

[Sovella taitojasi](assignment.md)

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä johtuvista väärinkäsityksistä tai virhetulkinnoista.