<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b4039f1c76548d144a0aee0bf28304ec",
  "translation_date": "2025-08-26T23:11:01+00:00",
  "source_file": "3-Data-Visualization/R/13-meaningful-vizualizations/README.md",
  "language_code": "sv"
}
-->
# Skapa Meningsfulla Visualiseringar

|![ Sketchnote av [(@sketchthedocs)](https://sketchthedocs.dev) ](../../../sketchnotes/13-MeaningfulViz.png)|
|:---:|
| Meningsfulla Visualiseringar - _Sketchnote av [@nitya](https://twitter.com/nitya)_ |

> "Om du torterar data tillräckligt länge, kommer det att erkänna vad som helst" -- [Ronald Coase](https://en.wikiquote.org/wiki/Ronald_Coase)

En av de grundläggande färdigheterna hos en dataanalytiker är förmågan att skapa en meningsfull datavisualisering som hjälper till att besvara frågor du kan ha. Innan du visualiserar din data måste du se till att den har blivit rensad och förberedd, som du gjorde i tidigare lektioner. Därefter kan du börja bestämma hur du bäst presenterar datan.

I denna lektion kommer du att gå igenom:

1. Hur man väljer rätt typ av diagram
2. Hur man undviker vilseledande diagram
3. Hur man arbetar med färg
4. Hur man stylar diagram för läsbarhet
5. Hur man bygger animerade eller 3D-lösningar för diagram
6. Hur man skapar en kreativ visualisering

## [Quiz före lektionen](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/24)

## Välj rätt typ av diagram

I tidigare lektioner experimenterade du med att skapa olika typer av intressanta datavisualiseringar med Matplotlib och Seaborn för diagram. Generellt kan du välja [rätt typ av diagram](https://chartio.com/learn/charts/how-to-select-a-data-vizualization/) för den fråga du ställer med hjälp av denna tabell:

| Du behöver:                | Du bör använda:                 |
| -------------------------- | ------------------------------- |
| Visa datatrender över tid  | Linje                           |
| Jämföra kategorier         | Stapel, Tårta                   |
| Jämföra totaler            | Tårta, Staplad stapel           |
| Visa relationer            | Spridning, Linje, Facet, Dubbel linje |
| Visa distributioner        | Spridning, Histogram, Låddiagram |
| Visa proportioner          | Tårta, Donut, Waffle            |

> ✅ Beroende på datans sammansättning kan du behöva konvertera den från text till numerisk för att få ett visst diagram att fungera.

## Undvik vilseledning

Även om en dataanalytiker är noggrann med att välja rätt diagram för rätt data, finns det många sätt att visa data på ett sätt som bevisar en poäng, ofta på bekostnad av att undergräva själva datan. Det finns många exempel på vilseledande diagram och infografik!

[![How Charts Lie av Alberto Cairo](../../../../../translated_images/tornado.2880ffc7f135f82b5e5328624799010abefd1080ae4b7ecacbdc7d792f1d8849.sv.png)](https://www.youtube.com/watch?v=oX74Nge8Wkw "How charts lie")

> 🎥 Klicka på bilden ovan för en konferensföreläsning om vilseledande diagram

Detta diagram vänder X-axeln för att visa motsatsen till sanningen, baserat på datum:

![dåligt diagram 1](../../../../../translated_images/bad-chart-1.596bc93425a8ac301a28b8361f59a970276e7b961658ce849886aa1fed427341.sv.png)

[Detta diagram](https://media.firstcoastnews.com/assets/WTLV/images/170ae16f-4643-438f-b689-50d66ca6a8d8/170ae16f-4643-438f-b689-50d66ca6a8d8_1140x641.jpg) är ännu mer vilseledande, eftersom ögat dras till höger för att dra slutsatsen att COVID-fallen har minskat över tid i olika län. Faktum är att om du tittar noga på datumen, upptäcker du att de har omarrangerats för att ge den vilseledande nedåtgående trenden.

![dåligt diagram 2](../../../../../translated_images/bad-chart-2.62edf4d2f30f4e519f5ef50c07ce686e27b0196a364febf9a4d98eecd21f9f60.sv.jpg)

Detta ökända exempel använder färg OCH en vänd Y-axel för att vilseleda: istället för att dra slutsatsen att vapenvåld ökade efter införandet av vapenvänlig lagstiftning, luras ögat att tro att motsatsen är sann:

![dåligt diagram 3](../../../../../translated_images/bad-chart-3.e201e2e915a230bc2cde289110604ec9abeb89be510bd82665bebc1228258972.sv.jpg)

Detta märkliga diagram visar hur proportioner kan manipuleras, med komisk effekt:

![dåligt diagram 4](../../../../../translated_images/bad-chart-4.8872b2b881ffa96c3e0db10eb6aed7793efae2cac382c53932794260f7bfff07.sv.jpg)

Att jämföra det ojämförbara är ytterligare ett skumt knep. Det finns en [fantastisk webbplats](https://tylervigen.com/spurious-correlations) som handlar om 'spurious correlations' och visar 'fakta' som korrelerar saker som skilsmässofrekvensen i Maine och konsumtionen av margarin. En Reddit-grupp samlar också [fula användningar](https://www.reddit.com/r/dataisugly/top/?t=all) av data.

Det är viktigt att förstå hur lätt ögat kan luras av vilseledande diagram. Även om dataanalytikerns intention är god, kan valet av en dålig typ av diagram, såsom ett tårtdiagram med för många kategorier, vara vilseledande.

## Färg

Du såg i diagrammet om 'vapenvåld i Florida' ovan hur färg kan ge en extra nivå av mening till diagram, särskilt sådana som inte är designade med bibliotek som ggplot2 och RColorBrewer, vilka kommer med olika granskade färgbibliotek och paletter. Om du skapar ett diagram manuellt, studera lite [färgteori](https://colormatters.com/color-and-design/basic-color-theory).

> ✅ Var medveten om att tillgänglighet är en viktig aspekt av visualisering när du designar diagram. Vissa av dina användare kan vara färgblinda - visas ditt diagram bra för användare med synnedsättningar?

Var försiktig när du väljer färger för ditt diagram, eftersom färg kan förmedla en mening du kanske inte avser. De 'rosa damerna' i diagrammet om 'höjd' ovan förmedlar en tydligt 'feminin' tillskriven mening som bidrar till diagrammets märklighet.

Även om [färgers betydelse](https://colormatters.com/color-symbolism/the-meanings-of-colors) kan vara olika i olika delar av världen och tenderar att ändras beroende på nyans, inkluderar generella färgbetydelser:

| Färg   | Betydelse           |
| ------ | ------------------- |
| röd    | styrka              |
| blå    | tillit, lojalitet   |
| gul    | glädje, försiktighet|
| grön   | ekologi, tur, avund |
| lila   | glädje              |
| orange | livfullhet          |

Om du får i uppdrag att skapa ett diagram med anpassade färger, se till att dina diagram är både tillgängliga och att färgen du väljer överensstämmer med den mening du försöker förmedla.

## Styla dina diagram för läsbarhet

Diagram är inte meningsfulla om de inte är läsbara! Ta dig tid att överväga att styla bredden och höjden på ditt diagram så att det passar bra med din data. Om en variabel (som alla 50 stater) behöver visas, visa dem vertikalt på Y-axeln om möjligt för att undvika ett diagram som kräver horisontell scrollning.

Märk dina axlar, tillhandahåll en legend om det behövs, och erbjud verktygstips för bättre förståelse av data.

Om din data är textbaserad och omfattande på X-axeln, kan du vinkla texten för bättre läsbarhet. [plot3D](https://cran.r-project.org/web/packages/plot3D/index.html) erbjuder 3D-plotting, om din data stödjer det. Sofistikerade datavisualiseringar kan skapas med det.

![3d diagram](../../../../../translated_images/3d.db1734c151eee87d924989306a00e23f8cddac6a0aab122852ece220e9448def.sv.png)

## Animation och 3D-diagram

Några av de bästa datavisualiseringarna idag är animerade. Shirley Wu har fantastiska exempel gjorda med D3, såsom '[film flowers](http://bl.ocks.org/sxywu/raw/d612c6c653fb8b4d7ff3d422be164a5d/)', där varje blomma är en visualisering av en film. Ett annat exempel för Guardian är 'bussed out', en interaktiv upplevelse som kombinerar visualiseringar med Greensock och D3 plus ett scrollytelling-artikelformat för att visa hur NYC hanterar sitt hemlöshetsproblem genom att bussa ut människor från staden.

![bussing](../../../../../translated_images/busing.8157cf1bc89a3f65052d362a78c72f964982ceb9dcacbe44480e35909c3dce62.sv.png)

> "Bussed Out: How America Moves its Homeless" från [the Guardian](https://www.theguardian.com/us-news/ng-interactive/2017/dec/20/bussed-out-america-moves-homeless-people-country-study). Visualiseringar av Nadieh Bremer & Shirley Wu

Även om denna lektion inte går tillräckligt djupt för att lära ut dessa kraftfulla visualiseringsbibliotek, prova att använda D3 i en Vue.js-app med ett bibliotek för att visa en visualisering av boken "Dangerous Liaisons" som ett animerat socialt nätverk.

> "Les Liaisons Dangereuses" är en brevroman, eller en roman presenterad som en serie brev. Skriven 1782 av Choderlos de Laclos, berättar den historien om de hänsynslösa, moraliskt bankrutta sociala manövrerna av två rivaliserande protagonister från den franska aristokratin i slutet av 1700-talet, Vicomte de Valmont och Marquise de Merteuil. Båda möter sitt öde i slutet, men inte utan att orsaka stor social skada. Romanen utvecklas som en serie brev skrivna till olika personer i deras kretsar, med planer på hämnd eller bara för att skapa problem. Skapa en visualisering av dessa brev för att upptäcka de stora nyckelpersonerna i berättelsen, visuellt.

Du kommer att slutföra en webbapp som visar en animerad vy av detta sociala nätverk. Den använder ett bibliotek som skapades för att skapa en [visualisering av ett nätverk](https://github.com/emiliorizzo/vue-d3-network) med Vue.js och D3. När appen körs kan du dra runt noderna på skärmen för att omorganisera datan.

![liaisons](../../../../../translated_images/liaisons.90ce7360bcf8476558f700bbbaf198ad697d5b5cb2829ba141a89c0add7c6ecd.sv.png)

## Projekt: Skapa ett diagram för att visa ett nätverk med D3.js

> Denna lektionsmapp innehåller en `solution`-mapp där du kan hitta det färdiga projektet som referens.

1. Följ instruktionerna i README.md-filen i startmappens rot. Se till att du har NPM och Node.js installerat på din dator innan du installerar projektets beroenden.

2. Öppna `starter/src`-mappen. Du hittar en `assets`-mapp där det finns en .json-fil med alla brev från romanen, numrerade, med en 'to' och 'from'-annotering.

3. Slutför koden i `components/Nodes.vue` för att möjliggöra visualiseringen. Leta efter metoden som heter `createLinks()` och lägg till följande nästlade loop.

Loopa genom .json-objektet för att fånga 'to' och 'from'-data för breven och bygg upp `links`-objektet så att visualiseringsbiblioteket kan använda det:

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

Kör din app från terminalen (npm run serve) och njut av visualiseringen!

## 🚀 Utmaning

Utforska internet för att upptäcka vilseledande visualiseringar. Hur lurar författaren användaren, och är det avsiktligt? Försök korrigera visualiseringarna för att visa hur de borde se ut.

## [Quiz efter lektionen](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/25)

## Granskning & Självstudier

Här är några artiklar att läsa om vilseledande datavisualiseringar:

https://gizmodo.com/how-to-lie-with-data-visualization-1563576606

http://ixd.prattsi.org/2017/12/visual-lies-usability-in-deceptive-data-visualizations/

Ta en titt på dessa intressanta visualiseringar för historiska tillgångar och artefakter:

https://handbook.pubpub.org/

Läs denna artikel om hur animation kan förbättra dina visualiseringar:

https://medium.com/@EvanSinar/use-animation-to-supercharge-data-visualization-cd905a882ad4

## Uppgift

[Skapa din egen anpassade visualisering](assignment.md)

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiserade översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.