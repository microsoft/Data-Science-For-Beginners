<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0b380bb6d34102bb061eb41de23d9834",
  "translation_date": "2025-09-04T19:56:23+00:00",
  "source_file": "3-Data-Visualization/13-meaningful-visualizations/README.md",
  "language_code": "nl"
}
-->
# Betekenisvolle Visualisaties Maken

|![ Sketchnote door [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/13-MeaningfulViz.png)|
|:---:|
| Betekenisvolle Visualisaties - _Sketchnote door [@nitya](https://twitter.com/nitya)_ |

> "Als je de data lang genoeg martelt, zal het alles bekennen" -- [Ronald Coase](https://en.wikiquote.org/wiki/Ronald_Coase)

Een van de basisvaardigheden van een datawetenschapper is het vermogen om een betekenisvolle datavisualisatie te maken die helpt vragen te beantwoorden. Voordat je je data visualiseert, moet je ervoor zorgen dat deze is opgeschoond en voorbereid, zoals je in eerdere lessen hebt gedaan. Daarna kun je beginnen met beslissen hoe je de data het beste kunt presenteren.

In deze les ga je het volgende bekijken:

1. Hoe kies je het juiste type grafiek
2. Hoe vermijd je misleidende grafieken
3. Hoe werk je met kleur
4. Hoe style je grafieken voor leesbaarheid
5. Hoe bouw je geanimeerde of 3D-grafieken
6. Hoe maak je een creatieve visualisatie

## [Pre-Les Quiz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/24)

## Kies het juiste type grafiek

In eerdere lessen heb je geëxperimenteerd met het maken van allerlei interessante datavisualisaties met Matplotlib en Seaborn. Over het algemeen kun je het [juiste type grafiek](https://chartio.com/learn/charts/how-to-select-a-data-vizualization/) kiezen voor de vraag die je stelt met behulp van deze tabel:

| Je wilt:                   | Gebruik:                        |
| -------------------------- | ------------------------------- |
| Trends in data over tijd tonen | Lijn                          |
| Categorieën vergelijken    | Staaf, Taart                    |
| Totalen vergelijken         | Taart, Gestapelde Staaf         |
| Relaties tonen             | Spreiding, Lijn, Facet, Dubbele Lijn |
| Distributies tonen         | Spreiding, Histogram, Box       |
| Verhoudingen tonen         | Taart, Donut, Wafel             |

> ✅ Afhankelijk van de samenstelling van je data, moet je deze mogelijk omzetten van tekst naar numeriek om een bepaalde grafiek te ondersteunen.

## Vermijd misleiding

Zelfs als een datawetenschapper zorgvuldig het juiste type grafiek kiest voor de juiste data, zijn er genoeg manieren waarop data kan worden weergegeven om een punt te bewijzen, vaak ten koste van de data zelf. Er zijn veel voorbeelden van misleidende grafieken en infographics!

[![How Charts Lie door Alberto Cairo](../../../../translated_images/tornado.9f42168791208f970d6faefc11d1226d7ca89518013b14aa66b1c9edcd7678d2.nl.png)](https://www.youtube.com/watch?v=oX74Nge8Wkw "How charts lie")

> 🎥 Klik op de afbeelding hierboven voor een conferentietoespraak over misleidende grafieken

Deze grafiek keert de X-as om om het tegenovergestelde van de waarheid te tonen, gebaseerd op datum:

![slechte grafiek 1](../../../../translated_images/bad-chart-1.93130f495b748bedfb3423d91b1e754d9026e17f94ad967aecdc9ca7203373bf.nl.png)

[Deze grafiek](https://media.firstcoastnews.com/assets/WTLV/images/170ae16f-4643-438f-b689-50d66ca6a8d8/170ae16f-4643-438f-b689-50d66ca6a8d8_1140x641.jpg) is nog misleidender, omdat het oog naar rechts wordt getrokken om te concluderen dat COVID-gevallen in de verschillende provincies in de loop van de tijd zijn afgenomen. Als je echter goed naar de datums kijkt, zie je dat ze zijn herschikt om die misleidende dalende trend te geven.

![slechte grafiek 2](../../../../translated_images/bad-chart-2.c20e36dd4e6f617c0c325878dd421a563885bbf30a394884c147438827254e0e.nl.jpg)

Dit beruchte voorbeeld gebruikt kleur EN een omgekeerde Y-as om te misleiden: in plaats van te concluderen dat het aantal schietincidenten steeg na de invoering van gun-vriendelijke wetgeving, wordt het oog juist misleid om te denken dat het tegenovergestelde waar is:

![slechte grafiek 3](../../../../translated_images/bad-chart-3.6865d0afac4108d737558d90a61547d23a8722896397ec792264ee51a1be4be5.nl.jpg)

Deze vreemde grafiek laat zien hoe proporties kunnen worden gemanipuleerd, met hilarisch effect:

![slechte grafiek 4](../../../../translated_images/bad-chart-4.68cfdf4011b454471053ee1231172747e1fbec2403b4443567f1dc678134f4f2.nl.jpg)

Het vergelijken van het onvergelijkbare is nog een schimmige truc. Er is een [geweldige website](https://tylervigen.com/spurious-correlations) helemaal gewijd aan 'spurious correlations' die 'feiten' tonen zoals de correlatie tussen het echtscheidingspercentage in Maine en de consumptie van margarine. Een Reddit-groep verzamelt ook de [lelijke toepassingen](https://www.reddit.com/r/dataisugly/top/?t=all) van data.

Het is belangrijk om te begrijpen hoe gemakkelijk het oog kan worden misleid door misleidende grafieken. Zelfs als de intentie van de datawetenschapper goed is, kan de keuze voor een slecht type grafiek, zoals een taartdiagram met te veel categorieën, misleidend zijn.

## Kleur

Je zag in de 'Florida gun violence'-grafiek hierboven hoe kleur een extra laag betekenis kan toevoegen aan grafieken, vooral grafieken die niet zijn ontworpen met bibliotheken zoals Matplotlib en Seaborn, die verschillende goedgekeurde kleurenschema's en paletten bevatten. Als je een grafiek met de hand maakt, doe dan een beetje onderzoek naar [kleurentheorie](https://colormatters.com/color-and-design/basic-color-theory).

> ✅ Houd er rekening mee dat toegankelijkheid een belangrijk aspect is van visualisatie. Sommige gebruikers kunnen kleurenblind zijn - wordt je grafiek goed weergegeven voor gebruikers met visuele beperkingen?

Wees voorzichtig bij het kiezen van kleuren voor je grafiek, omdat kleur een betekenis kan overbrengen die je misschien niet bedoelt. De 'pink ladies' in de 'hoogte'-grafiek hierboven geven een duidelijk 'vrouwelijke' toegewezen betekenis die bijdraagt aan de eigenaardigheid van de grafiek zelf.

Hoewel [kleurbetekenis](https://colormatters.com/color-symbolism/the-meanings-of-colors) kan verschillen in verschillende delen van de wereld en de betekenis kan veranderen afhankelijk van de tint, omvatten algemene kleurbetekenissen:

| Kleur  | Betekenis           |
| ------ | ------------------- |
| rood   | kracht              |
| blauw  | vertrouwen, loyaliteit |
| geel   | geluk, voorzichtigheid |
| groen  | ecologie, geluk, jaloezie |
| paars  | geluk               |
| oranje | levendigheid         |

Als je de taak hebt om een grafiek te maken met aangepaste kleuren, zorg er dan voor dat je grafieken zowel toegankelijk zijn als dat de kleur die je kiest overeenkomt met de betekenis die je probeert over te brengen.

## Grafieken stylen voor leesbaarheid

Grafieken zijn niet betekenisvol als ze niet leesbaar zijn! Neem de tijd om de breedte en hoogte van je grafiek te stylen zodat deze goed schaalt met je data. Als één variabele (zoals alle 50 staten) moet worden weergegeven, toon ze dan verticaal op de Y-as indien mogelijk om een horizontaal scrollende grafiek te vermijden.

Label je assen, geef indien nodig een legenda en bied tooltips aan voor een betere begrip van de data.

Als je data tekstueel en uitgebreid is op de X-as, kun je de tekst schuin zetten voor een betere leesbaarheid. [Matplotlib](https://matplotlib.org/stable/tutorials/toolkits/mplot3d.html) biedt 3D-plotten aan, als je data dit ondersteunt. Geavanceerde datavisualisaties kunnen worden geproduceerd met `mpl_toolkits.mplot3d`.

![3d grafieken](../../../../translated_images/3d.0cec12bcc60f0ce7284c63baed1411a843e24716f7d7425de878715ebad54a15.nl.png)

## Animatie en 3D-grafiekweergave

Sommige van de beste datavisualisaties van vandaag zijn geanimeerd. Shirley Wu heeft geweldige voorbeelden gemaakt met D3, zoals '[film flowers](http://bl.ocks.org/sxywu/raw/d612c6c653fb8b4d7ff3d422be164a5d/)', waarbij elke bloem een visualisatie van een film is. Een ander voorbeeld voor de Guardian is 'bussed out', een interactieve ervaring die visualisaties combineert met Greensock en D3 plus een scrollytelling artikelvorm om te laten zien hoe NYC omgaat met het daklozenprobleem door mensen uit de stad te sturen.

![bussing](../../../../translated_images/busing.7b9e3b41cd4b981c6d63922cd82004cc1cf18895155536c1d98fcc0999bdd23e.nl.png)

> "Bussed Out: How America Moves its Homeless" van [the Guardian](https://www.theguardian.com/us-news/ng-interactive/2017/dec/20/bussed-out-america-moves-homeless-people-country-study). Visualisaties door Nadieh Bremer & Shirley Wu

Hoewel deze les onvoldoende diepgang biedt om deze krachtige visualisatiebibliotheken te leren, kun je proberen D3 te gebruiken in een Vue.js-app met een bibliotheek om een visualisatie van het boek "Dangerous Liaisons" als een geanimeerd sociaal netwerk weer te geven.

> "Les Liaisons Dangereuses" is een briefroman, of een roman gepresenteerd als een reeks brieven. Geschreven in 1782 door Choderlos de Laclos, vertelt het het verhaal van de wrede, moreel-bankroete sociale manoeuvres van twee strijdende protagonisten van de Franse aristocratie in de late 18e eeuw, de Vicomte de Valmont en de Marquise de Merteuil. Beide komen uiteindelijk aan hun einde, maar niet zonder veel sociale schade aan te richten. De roman ontvouwt zich als een reeks brieven geschreven aan verschillende mensen in hun kringen, met plannen voor wraak of simpelweg om problemen te veroorzaken. Maak een visualisatie van deze brieven om de belangrijkste spelers in het verhaal visueel te ontdekken.

Je zult een webapp voltooien die een geanimeerde weergave van dit sociale netwerk toont. Het gebruikt een bibliotheek die is gebouwd om een [visualisatie van een netwerk](https://github.com/emiliorizzo/vue-d3-network) te maken met Vue.js en D3. Wanneer de app draait, kun je de knooppunten op het scherm verplaatsen om de data te herschikken.

![liaisons](../../../../translated_images/liaisons.7b440b28f6d07ea430244fdf1fc4c64ff48f473f143b8e921846eda1c302aeba.nl.png)

## Project: Bouw een grafiek om een netwerk te tonen met D3.js

> Deze lesmap bevat een `solution`-map waar je het voltooide project kunt vinden, ter referentie.

1. Volg de instructies in het README.md-bestand in de root van de startermap. Zorg ervoor dat je NPM en Node.js op je machine hebt draaien voordat je de afhankelijkheden van je project installeert.

2. Open de `starter/src`-map. Je vindt een `assets`-map waar je een .json-bestand kunt vinden met alle brieven uit de roman, genummerd, met een 'to' en 'from'-annotatie.

3. Voltooi de code in `components/Nodes.vue` om de visualisatie mogelijk te maken. Zoek naar de methode genaamd `createLinks()` en voeg de volgende geneste lus toe.

Loop door het .json-object om de 'to' en 'from'-data voor de brieven vast te leggen en bouw het `links`-object op zodat de visualisatiebibliotheek het kan gebruiken:

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

Voer je app uit vanuit de terminal (npm run serve) en geniet van de visualisatie!

## 🚀 Uitdaging

Maak een rondje op het internet om misleidende visualisaties te ontdekken. Hoe misleidt de auteur de gebruiker, en is dit opzettelijk? Probeer de visualisaties te corrigeren om te laten zien hoe ze eruit zouden moeten zien.

## [Post-Les Quiz](https://ff-quizzes.netlify.app/en/ds/)

## Review & Zelfstudie

Hier zijn enkele artikelen om te lezen over misleidende datavisualisaties:

https://gizmodo.com/how-to-lie-with-data-visualization-1563576606

http://ixd.prattsi.org/2017/12/visual-lies-usability-in-deceptive-data-visualizations/

Bekijk deze interessante visualisaties van historische objecten en artefacten:

https://handbook.pubpub.org/

Lees dit artikel over hoe animatie je visualisaties kan verbeteren:

https://medium.com/@EvanSinar/use-animation-to-supercharge-data-visualization-cd905a882ad4

## Opdracht

[Maak je eigen aangepaste visualisatie](assignment.md)

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we ons best doen voor nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in zijn oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.