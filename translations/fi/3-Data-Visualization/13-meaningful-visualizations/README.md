<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cfb068050337a36e348debaa502a24fa",
  "translation_date": "2025-09-05T22:44:01+00:00",
  "source_file": "3-Data-Visualization/13-meaningful-visualizations/README.md",
  "language_code": "fi"
}
-->
# Merkityksellisten Visualisointien Luominen

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/13-MeaningfulViz.png)|
|:---:|
| Merkitykselliset visualisoinnit - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

> "Jos kidutat dataa tarpeeksi kauan, se tunnustaa mitä tahansa" -- [Ronald Coase](https://en.wikiquote.org/wiki/Ronald_Coase)

Yksi datatieteilijän perustaidoista on kyky luoda merkityksellinen datavisualisointi, joka auttaa vastaamaan kysymyksiin, joita sinulla saattaa olla. Ennen kuin visualisoit dataasi, sinun on varmistettava, että se on puhdistettu ja valmisteltu, kuten teit aiemmissa oppitunneissa. Tämän jälkeen voit alkaa päättää, miten data esitetään parhaiten.

Tässä oppitunnissa tarkastelet:

1. Kuinka valita oikea kaaviotyyppi
2. Kuinka välttää harhaanjohtavia kaavioita
3. Kuinka käyttää värejä
4. Kuinka muotoilla kaaviot luettavuuden parantamiseksi
5. Kuinka rakentaa animoituja tai 3D-kaavioita
6. Kuinka luoda luovia visualisointeja

## [Esiluennon kysely](https://ff-quizzes.netlify.app/en/ds/quiz/24)

## Valitse oikea kaaviotyyppi

Aiemmissa oppitunneissa kokeilit erilaisten mielenkiintoisten datavisualisointien rakentamista Matplotlibin ja Seabornin avulla. Yleisesti ottaen voit valita [oikeanlaisen kaavion](https://chartio.com/learn/charts/how-to-select-a-data-vizualization/) kysymyksesi perusteella seuraavan taulukon avulla:

| Tarve:                     | Käytä:                         |
| -------------------------- | ------------------------------- |
| Näytä datan trendit ajan myötä | Viivakaavio                   |
| Vertaile kategorioita      | Pylväskaavio, Piirakkakaavio    |
| Vertaile kokonaismääriä    | Piirakkakaavio, Pinottu pylväskaavio |
| Näytä suhteita             | Hajontakaavio, Viivakaavio, Facet, Kaksoisviiva |
| Näytä jakaumia             | Hajontakaavio, Histogrammi, Laatikko |
| Näytä osuuksia             | Piirakkakaavio, Donitsi, Vohveli |

> ✅ Riippuen datasi rakenteesta, saatat joutua muuntamaan sen tekstistä numeeriseksi, jotta kaavio tukee sitä.

## Vältä harhaanjohtavuutta

Vaikka datatieteilijä valitsisi oikean kaavion oikealle datalle, on monia tapoja esittää dataa niin, että se tukee tiettyä näkökulmaa, usein datan kustannuksella. On olemassa lukuisia esimerkkejä harhaanjohtavista kaavioista ja infografiikoista!

[![How Charts Lie by Alberto Cairo](../../../../3-Data-Visualization/13-meaningful-visualizations/images/tornado.png)](https://www.youtube.com/watch?v=oX74Nge8Wkw "How charts lie")

> 🎥 Klikkaa yllä olevaa kuvaa nähdäksesi konferenssipuheen harhaanjohtavista kaavioista

Tässä kaaviossa X-akseli on käännetty näyttämään totuuden vastakohta päivämäärän perusteella:

![huono kaavio 1](../../../../3-Data-Visualization/13-meaningful-visualizations/images/bad-chart-1.png)

[Tämä kaavio](https://media.firstcoastnews.com/assets/WTLV/images/170ae16f-4643-438f-b689-50d66ca6a8d8/170ae16f-4643-438f-b689-50d66ca6a8d8_1140x641.jpg) on vielä harhaanjohtavampi, sillä katsojan huomio kiinnittyy oikealle, mikä antaa vaikutelman, että COVID-tapaukset ovat vähentyneet eri maakunnissa ajan myötä. Tarkemmin katsottuna päivämäärät on kuitenkin järjestetty uudelleen luomaan harhaanjohtava laskeva trendi.

![huono kaavio 2](../../../../3-Data-Visualization/13-meaningful-visualizations/images/bad-chart-2.jpg)

Tämä tunnettu esimerkki käyttää värejä JA käännettyä Y-akselia harhauttaakseen: sen sijaan, että asekuolemat olisivat lisääntyneet aselainsäädännön jälkeen, katsoja saadaan uskomaan päinvastaista:

![huono kaavio 3](../../../../3-Data-Visualization/13-meaningful-visualizations/images/bad-chart-3.jpg)

Tämä outo kaavio näyttää, kuinka mittasuhteita voidaan manipuloida, huvittavin seurauksin:

![huono kaavio 4](../../../../3-Data-Visualization/13-meaningful-visualizations/images/bad-chart-4.jpg)

Vertailu, joka ei ole vertailukelpoista, on toinen kyseenalainen temppu. On olemassa [mahtava verkkosivusto](https://tylervigen.com/spurious-correlations), joka esittelee 'näennäisiä korrelaatioita', kuten Mainen avioeroprosentin ja margariinin kulutuksen välisiä 'faktoja'. Reddit-ryhmä kerää myös [huonoja datan käyttöesimerkkejä](https://www.reddit.com/r/dataisugly/top/?t=all).

On tärkeää ymmärtää, kuinka helposti silmä voidaan harhauttaa harhaanjohtavilla kaavioilla. Vaikka datatieteilijän tarkoitus olisi hyvä, huonon kaaviotyypin, kuten liian monia kategorioita sisältävän piirakkakaavion, valinta voi olla harhaanjohtavaa.

## Värit

Yllä olevassa 'Floridan aserikollisuus' -kaaviossa näit, kuinka värit voivat lisätä merkitystä kaavioihin, erityisesti sellaisiin, joita ei ole suunniteltu Matplotlibin ja Seabornin kaltaisten kirjastojen avulla, jotka sisältävät erilaisia tarkistettuja värikirjastoja ja -paletteja. Jos teet kaavion käsin, tutustu hieman [väriteoriaan](https://colormatters.com/color-and-design/basic-color-theory).

> ✅ Ole tietoinen, kun suunnittelet kaavioita, että saavutettavuus on tärkeä osa visualisointia. Jotkut käyttäjistäsi saattavat olla värisokeita – näkyykö kaaviosi hyvin näkövammaisille käyttäjille?

Ole varovainen valitessasi värejä kaavioosi, sillä värit voivat välittää merkityksiä, joita et ehkä tarkoittanut. Yllä olevan 'pinkit naiset' -kaavion 'korkeus' viittaa selvästi 'feminiiniseen' merkitykseen, mikä lisää kaavion outoutta.

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

Merkitse akselisi, tarjoa selite tarvittaessa ja lisää työkaluja datan paremman ymmärtämisen tueksi.

Jos datasi on tekstuaalista ja laajaa X-akselilla, voit kallistaa tekstiä luettavuuden parantamiseksi. [Matplotlib](https://matplotlib.org/stable/tutorials/toolkits/mplot3d.html) tarjoaa 3D-plottausta, jos datasi tukee sitä. Kehittyneitä datavisualisointeja voidaan tuottaa käyttämällä `mpl_toolkits.mplot3d`.

![3d kaaviot](../../../../3-Data-Visualization/13-meaningful-visualizations/images/3d.png)

## Animaatio ja 3D-kaavioiden näyttö

Jotkut parhaista datavisualisoinneista nykyään ovat animoituja. Shirley Wu on tehnyt upeita visualisointeja D3:lla, kuten '[film flowers](http://bl.ocks.org/sxywu/raw/d612c6c653fb8b4d7ff3d422be164a5d/)', jossa jokainen kukka on elokuvan visualisointi. Toinen esimerkki Guardianille on 'bussed out', interaktiivinen kokemus, joka yhdistää visualisointeja Greensockin ja D3:n avulla sekä artikkelin, joka kertoo, kuinka NYC käsittelee kodittomien ongelmaa lähettämällä ihmisiä pois kaupungista.

![busing](../../../../3-Data-Visualization/13-meaningful-visualizations/images/busing.png)

> "Bussed Out: How America Moves its Homeless" [Guardianista](https://www.theguardian.com/us-news/ng-interactive/2017/dec/20/bussed-out-america-moves-homeless-people-country-study). Visualisoinnit: Nadieh Bremer & Shirley Wu

Vaikka tämä oppitunti ei riitä opettamaan näitä tehokkaita visualisointikirjastoja syvällisesti, kokeile D3:ta Vue.js-sovelluksessa käyttämällä kirjastoa, joka näyttää visualisoinnin kirjasta "Dangerous Liaisons" animoituna sosiaalisena verkostona.

> "Les Liaisons Dangereuses" on kirjeromaanimuotoinen teos, joka koostuu kirjeistä. Vuonna 1782 Choderlos de Laclosin kirjoittama teos kertoo kahden ranskalaisen aristokraatin, Vicomte de Valmontin ja Marquise de Merteuilin, moraalittomista juonitteluista. Molemmat kohtaavat lopulta tuhon, mutta eivät ennen kuin aiheuttavat suurta sosiaalista vahinkoa. Kirjeiden avulla voit visualisoida tarinan keskeiset hahmot visuaalisesti.

Toteutat verkkosovelluksen, joka näyttää animoidun näkymän tästä sosiaalisesta verkostosta. Se käyttää kirjastoa, joka on rakennettu [verkoston visualisointiin](https://github.com/emiliorizzo/vue-d3-network) Vue.js:n ja D3:n avulla. Kun sovellus on käynnissä, voit siirrellä solmuja näytöllä järjestelläksesi dataa.

![liaisons](../../../../3-Data-Visualization/13-meaningful-visualizations/images/liaisons.png)

## Projekti: Rakenna kaavio, joka näyttää verkoston D3.js:llä

> Tämän oppitunnin kansiossa on `solution`-kansio, josta löydät valmiin projektin viitteeksi.

1. Seuraa README.md-tiedoston ohjeita aloituskansion juuresta. Varmista, että sinulla on NPM ja Node.js asennettuna koneellesi ennen projektin riippuvuuksien asentamista.

2. Avaa `starter/src`-kansio. Löydät `assets`-kansiosta .json-tiedoston, jossa on kaikki kirjeet, numeroituina, ja 'to' ja 'from' -merkinnät.

3. Täydennä koodi `components/Nodes.vue`-tiedostossa mahdollistamaan visualisointi. Etsi metodi nimeltä `createLinks()` ja lisää seuraava sisäkkäinen silmukka.

Käy läpi .json-objekti kerätäksesi kirjeiden 'to' ja 'from' -data ja rakenna `links`-objekti, jotta visualisointikirjasto voi käyttää sitä:

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

Tutustu internetissä harhaanjohtaviin visualisointeihin. Kuinka tekijä harhauttaa käyttäjää, ja onko se tarkoituksellista? Yritä korjata visualisoinnit näyttämään, miltä niiden pitäisi näyttää.

## [Jälkiluennon kysely](https://ff-quizzes.netlify.app/en/ds/quiz/25)

## Kertaus ja itseopiskelu

Tässä muutamia artikkeleita harhaanjohtavista datavisualisoinneista:

https://gizmodo.com/how-to-lie-with-data-visualization-1563576606

http://ixd.prattsi.org/2017/12/visual-lies-usability-in-deceptive-data-visualizations/

Tutustu näihin mielenkiintoisiin visualisointeihin historiallisista aineistoista ja esineistä:

https://handbook.pubpub.org/

Lue tämä artikkeli siitä, kuinka animaatio voi parantaa visualisointeja:

https://medium.com/@EvanSinar/use-animation-to-supercharge-data-visualization-cd905a882ad4

## Tehtävä

[Rakenna oma mukautettu visualisointisi](assignment.md)

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Pyrimme tarkkuuteen, mutta huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulee pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinkäsityksistä tai virhetulkinnoista.