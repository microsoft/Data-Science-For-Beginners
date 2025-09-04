<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0b380bb6d34102bb061eb41de23d9834",
  "translation_date": "2025-09-04T19:43:32+00:00",
  "source_file": "3-Data-Visualization/13-meaningful-visualizations/README.md",
  "language_code": "fi"
}
-->
# Merkityksellisten visualisointien luominen

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/13-MeaningfulViz.png)|
|:---:|
| Merkitykselliset visualisoinnit - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

> "Jos kidutat dataa tarpeeksi kauan, se tunnustaa mitä tahansa" -- [Ronald Coase](https://en.wikiquote.org/wiki/Ronald_Coase)

Yksi data-analyytikon perustaidosta on kyky luoda merkityksellinen datavisualisointi, joka auttaa vastaamaan kysymyksiin. Ennen datan visualisointia on varmistettava, että se on puhdistettu ja valmisteltu, kuten aiemmissa oppitunneissa tehtiin. Tämän jälkeen voit alkaa päättää, miten dataa kannattaa esittää.

Tässä oppitunnissa käsitellään:

1. Kuinka valita oikea kaaviotyyppi
2. Kuinka välttää harhaanjohtavia kaavioita
3. Kuinka käyttää värejä
4. Kuinka muotoilla kaaviot luettavuuden parantamiseksi
5. Kuinka rakentaa animoituja tai 3D-kaavioita
6. Kuinka luoda luovia visualisointeja

## [Ennakkokysely](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/24)

## Valitse oikea kaaviotyyppi

Aiemmissa oppitunneissa kokeilit erilaisten datavisualisointien luomista Matplotlibin ja Seabornin avulla. Yleisesti ottaen voit valita [oikeanlaisen kaavion](https://chartio.com/learn/charts/how-to-select-a-data-vizualization/) kysymyksesi perusteella seuraavan taulukon avulla:

| Tarve:                     | Käytä:                         |
| -------------------------- | ------------------------------- |
| Näytä datan trendit ajan myötä | Viivakaavio                   |
| Vertaa kategorioita         | Pylväskaavio, piirakka         |
| Vertaa kokonaismääriä       | Piirakka, pinottu pylväskaavio |
| Näytä suhteita              | Hajontakaavio, viiva, facet, kaksoisviiva |
| Näytä jakaumia              | Hajontakaavio, histogrammi, laatikko |
| Näytä osuuksia              | Piirakka, donitsi, vohveli     |

> ✅ Datan rakenteesta riippuen saatat joutua muuntamaan tekstin numeeriseksi, jotta kaavio tukee sitä.

## Vältä harhaanjohtamista

Vaikka data-analyytikko valitsisi oikean kaavion oikealle datalle, on silti monia tapoja esittää dataa harhaanjohtavasti, usein datan kustannuksella. Harhaanjohtavia kaavioita ja infografiikoita on lukuisia esimerkkejä!

[![How Charts Lie by Alberto Cairo](../../../../translated_images/tornado.9f42168791208f970d6faefc11d1226d7ca89518013b14aa66b1c9edcd7678d2.fi.png)](https://www.youtube.com/watch?v=oX74Nge8Wkw "How charts lie")

> 🎥 Klikkaa yllä olevaa kuvaa nähdäksesi konferenssipuheen harhaanjohtavista kaavioista

Tämä kaavio kääntää X-akselin näyttääkseen totuuden vastakohdan päivämäärän perusteella:

![huono kaavio 1](../../../../translated_images/bad-chart-1.93130f495b748bedfb3423d91b1e754d9026e17f94ad967aecdc9ca7203373bf.fi.png)

[Tämä kaavio](https://media.firstcoastnews.com/assets/WTLV/images/170ae16f-4643-438f-b689-50d66ca6a8d8/170ae16f-4643-438f-b689-50d66ca6a8d8_1140x641.jpg) on vielä harhaanjohtavampi, sillä katsojan huomio kiinnittyy oikealle ja hän saattaa päätellä, että COVID-tapaukset ovat vähentyneet eri maakunnissa ajan myötä. Todellisuudessa päivämäärät on järjestetty uudelleen antamaan harhaanjohtava laskeva trendi.

![huono kaavio 2](../../../../translated_images/bad-chart-2.c20e36dd4e6f617c0c325878dd421a563885bbf30a394884c147438827254e0e.fi.jpg)

Tämä tunnettu esimerkki käyttää väriä JA käännettyä Y-akselia harhauttamiseen: sen sijaan, että asekuolemat olisivat lisääntyneet asemyönteisen lainsäädännön jälkeen, katsoja saattaa erehtyä luulemaan päinvastaista.

![huono kaavio 3](../../../../translated_images/bad-chart-3.6865d0afac4108d737558d90a61547d23a8722896397ec792264ee51a1be4be5.fi.jpg)

Tämä outo kaavio näyttää, kuinka mittasuhteita voidaan manipuloida, huvittavin seurauksin:

![huono kaavio 4](../../../../translated_images/bad-chart-4.68cfdf4011b454471053ee1231172747e1fbec2403b4443567f1dc678134f4f2.fi.jpg)

Vertailu, joka ei ole vertailukelpoista, on toinen hämärä temppu. On olemassa [loistava verkkosivusto](https://tylervigen.com/spurious-correlations), joka esittelee 'näennäisiä korrelaatioita', kuten Mainen avioeroprosentin ja margariinin kulutuksen. Reddit-ryhmä kerää myös [huonoja datan käyttöesimerkkejä](https://www.reddit.com/r/dataisugly/top/?t=all).

On tärkeää ymmärtää, kuinka helposti silmä voi tulla harhaanjohdetuksi huonoilla kaavioilla. Vaikka data-analyytikon tarkoitus olisi hyvä, huonon kaaviotyypin valinta, kuten piirakkakaavio, jossa on liian monta kategoriaa, voi olla harhaanjohtavaa.

## Värit

Edellä mainitussa 'Floridan aseväkivalta' -kaaviossa näit, kuinka väri voi tuoda lisämerkityksen kaavioihin, erityisesti sellaisiin, joita ei ole suunniteltu Matplotlibin ja Seabornin kaltaisten kirjastojen avulla, jotka sisältävät erilaisia tarkistettuja värikirjastoja ja -paletteja. Jos teet kaavion käsin, tutustu hieman [väriteoriaan](https://colormatters.com/color-and-design/basic-color-theory).

> ✅ Ole tietoinen, kun suunnittelet kaavioita, että saavutettavuus on tärkeä osa visualisointia. Jotkut käyttäjistäsi saattavat olla värisokeita - näkyykö kaaviosi hyvin näkövammaisille käyttäjille?

Ole varovainen valitessasi värejä kaaviollesi, sillä väri voi välittää merkityksiä, joita et ehkä tarkoittanut. 'Pinkit naiset' yllä olevassa 'pituus'-kaaviossa välittävät selvästi 'naisellisen' merkityksen, joka lisää kaavion outoutta.

Vaikka [värien merkitys](https://colormatters.com/color-symbolism/the-meanings-of-colors) voi vaihdella eri puolilla maailmaa ja muuttua sävyn mukaan, yleisesti ottaen värien merkitykset sisältävät:

| Väri   | Merkitys            |
| ------ | ------------------- |
| punainen | voima              |
| sininen  | luottamus, uskollisuus |
| keltainen | ilo, varovaisuus  |
| vihreä   | ekologia, onni, kateus |
| violetti | ilo                |
| oranssi  | eloisuus           |

Jos sinua pyydetään rakentamaan kaavio mukautetuilla väreillä, varmista, että kaaviosi ovat sekä saavutettavia että valitsemasi väri vastaa haluamaasi merkitystä.

## Kaavioiden muotoilu luettavuuden parantamiseksi

Kaaviot eivät ole merkityksellisiä, jos ne eivät ole luettavia! Käytä hetki kaavion leveyden ja korkeuden muotoiluun, jotta se skaalautuu hyvin datasi kanssa. Jos yksi muuttuja (kuten kaikki 50 osavaltiota) täytyy näyttää, esitä ne pystysuunnassa Y-akselilla, jos mahdollista, jotta vältät vaakasuunnassa vieritettävän kaavion.

Merkitse akselit, tarjoa selite tarvittaessa ja lisää työkaluja datan parempaan ymmärtämiseen.

Jos datasi on tekstuaalista ja X-akselilla pitkää, voit kallistaa tekstiä paremman luettavuuden saavuttamiseksi. [Matplotlib](https://matplotlib.org/stable/tutorials/toolkits/mplot3d.html) tarjoaa 3D-plottausta, jos datasi tukee sitä. Kehittyneitä datavisualisointeja voidaan tuottaa `mpl_toolkits.mplot3d`-kirjaston avulla.

![3d-kaaviot](../../../../translated_images/3d.0cec12bcc60f0ce7284c63baed1411a843e24716f7d7425de878715ebad54a15.fi.png)

## Animaatio ja 3D-kaavioiden näyttö

Jotkut parhaista datavisualisoinneista nykyään ovat animoituja. Shirley Wu on tehnyt upeita visualisointeja D3:lla, kuten '[film flowers](http://bl.ocks.org/sxywu/raw/d612c6c653fb8b4d7ff3d422be164a5d/)', jossa jokainen kukka on elokuvan visualisointi. Toinen esimerkki Guardianille on 'bussed out', interaktiivinen kokemus, joka yhdistää visualisointeja Greensockin ja D3:n kanssa sekä artikkelin, joka kertoo, kuinka NYC käsittelee kodittomien ongelmaa kuljettamalla ihmisiä pois kaupungista.

![kuljetus](../../../../translated_images/busing.7b9e3b41cd4b981c6d63922cd82004cc1cf18895155536c1d98fcc0999bdd23e.fi.png)

> "Bussed Out: How America Moves its Homeless" Guardianilta [the Guardian](https://www.theguardian.com/us-news/ng-interactive/2017/dec/20/bussed-out-america-moves-homeless-people-country-study). Visualisoinnit: Nadieh Bremer & Shirley Wu

Vaikka tämä oppitunti ei riitä opettamaan näitä tehokkaita visualisointikirjastoja syvällisesti, kokeile D3:ta Vue.js-sovelluksessa käyttämällä kirjastoa, joka näyttää visualisoinnin kirjasta "Dangerous Liaisons" animoituna sosiaalisena verkostona.

> "Les Liaisons Dangereuses" on kirjeromaanimuotoinen teos, joka koostuu kirjeistä. Kirjoittanut Choderlos de Laclos vuonna 1782, se kertoo kahden ranskalaisen aristokraatin, Vicomte de Valmontin ja Marquise de Merteuilin, moraalittomista sosiaalisista juonitteluista 1700-luvun lopulla. Molemmat kohtaavat lopulta tuhon, mutta eivät ennen kuin aiheuttavat suurta sosiaalista vahinkoa. Romaani etenee kirjeiden kautta, joissa juonitaan kostoa tai yksinkertaisesti aiheutetaan ongelmia. Luo näiden kirjeiden visualisointi löytääksesi narratiivin keskeiset hahmot visuaalisesti.

Toteutat verkkosovelluksen, joka näyttää animoidun näkymän tästä sosiaalisesta verkostosta. Sovellus käyttää kirjastoa, joka on rakennettu [verkoston visualisointiin](https://github.com/emiliorizzo/vue-d3-network) Vue.js:n ja D3:n avulla. Kun sovellus on käynnissä, voit siirtää solmuja näytöllä ja järjestellä dataa uudelleen.

![liaisons](../../../../translated_images/liaisons.7b440b28f6d07ea430244fdf1fc4c64ff48f473f143b8e921846eda1c302aeba.fi.png)

## Projekti: Rakenna kaavio, joka näyttää verkoston D3.js:llä

> Tämän oppitunnin kansiossa on `solution`-kansio, josta löydät valmiin projektin viitteeksi.

1. Seuraa README.md-tiedoston ohjeita aloituskansion juurihakemistossa. Varmista, että NPM ja Node.js ovat asennettu koneellesi ennen projektin riippuvuuksien asentamista.

2. Avaa `starter/src`-kansio. Löydät `assets`-kansion, jossa on .json-tiedosto, joka sisältää kaikki kirjeet romaanista, numeroituina, 'to' ja 'from' -merkinnöillä.

3. Täydennä koodi `components/Nodes.vue`-tiedostossa, jotta visualisointi toimii. Etsi metodi nimeltä `createLinks()` ja lisää seuraava sisäkkäinen silmukka.

Käy läpi .json-objekti, jotta saat kirjeiden 'to' ja 'from' -datan ja rakenna `links`-objekti, jotta visualisointikirjasto voi käyttää sitä:

```javascript
//loop through letters
      let f = 0;
      let t = 0;
      for (var i = 0; i < letters.length; i++) {
          for (var j = 0; j < characters.length; j++) {
              
            if (characters[j] == letters[i].from) {
              f = j;
            }
            if (characters[j] == letters[i].to) {
              t = j;
            }
        }
        this.links.push({ sid: f, tid: t });
      }
  ```

Käynnistä sovelluksesi terminaalista (npm run serve) ja nauti visualisoinnista!

## 🚀 Haaste

Tutki internetiä löytääksesi harhaanjohtavia visualisointeja. Kuinka tekijä harhauttaa käyttäjää, ja onko se tarkoituksellista? Yritä korjata visualisoinnit näyttämään, miltä niiden pitäisi näyttää.

## [Jälkikysely](https://ff-quizzes.netlify.app/en/ds/)

## Kertaus ja itseopiskelu

Tässä muutamia artikkeleita harhaanjohtavista datavisualisoinneista:

https://gizmodo.com/how-to-lie-with-data-visualization-1563576606

http://ixd.prattsi.org/2017/12/visual-lies-usability-in-deceptive-data-visualizations/

Tutustu näihin kiinnostaviin visualisointeihin historiallisista aineistoista ja esineistä:

https://handbook.pubpub.org/

Lue tämä artikkeli siitä, kuinka animaatio voi parantaa visualisointeja:

https://medium.com/@EvanSinar/use-animation-to-supercharge-data-visualization-cd905a882ad4

## Tehtävä

[Rakenna oma mukautettu visualisointi](assignment.md)

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.