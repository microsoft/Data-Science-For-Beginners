<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b4039f1c76548d144a0aee0bf28304ec",
  "translation_date": "2025-08-26T23:11:32+00:00",
  "source_file": "3-Data-Visualization/R/13-meaningful-vizualizations/README.md",
  "language_code": "da"
}
-->
# Skabe Meningsfulde Visualiseringer

|![ Sketchnote af [(@sketchthedocs)](https://sketchthedocs.dev) ](../../../sketchnotes/13-MeaningfulViz.png)|
|:---:|
| Meningsfulde Visualiseringer - _Sketchnote af [@nitya](https://twitter.com/nitya)_ |

> "Hvis du torturerer data længe nok, vil de tilstå hvad som helst" -- [Ronald Coase](https://en.wikiquote.org/wiki/Ronald_Coase)

En af de grundlæggende færdigheder for en dataforsker er evnen til at skabe en meningsfuld datavisualisering, der hjælper med at besvare de spørgsmål, du måtte have. Før du visualiserer dine data, skal du sikre dig, at de er blevet renset og forberedt, som du gjorde i tidligere lektioner. Derefter kan du begynde at beslutte, hvordan du bedst præsenterer dataene.

I denne lektion vil du gennemgå:

1. Hvordan man vælger den rigtige diagramtype
2. Hvordan man undgår vildledende diagrammer
3. Hvordan man arbejder med farver
4. Hvordan man styler diagrammer for læsbarhed
5. Hvordan man bygger animerede eller 3D-diagramløsninger
6. Hvordan man skaber en kreativ visualisering

## [Quiz før lektionen](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/24)

## Vælg den rigtige diagramtype

I tidligere lektioner eksperimenterede du med at bygge alle slags interessante datavisualiseringer ved hjælp af Matplotlib og Seaborn til diagrammer. Generelt kan du vælge den [rigtige type diagram](https://chartio.com/learn/charts/how-to-select-a-data-vizualization/) til det spørgsmål, du stiller, ved hjælp af denne tabel:

| Du skal:                   | Du bør bruge:                   |
| -------------------------- | ------------------------------- |
| Vise datatrends over tid   | Linje                           |
| Sammenligne kategorier     | Søjle, Cirkel                   |
| Sammenligne totaler         | Cirkel, Stablet Søjle           |
| Vise relationer            | Punkt, Linje, Facet, Dobbelt Linje |
| Vise fordelinger           | Punkt, Histogram, Boks          |
| Vise proportioner          | Cirkel, Donut, Vaffel           |

> ✅ Afhængigt af sammensætningen af dine data kan det være nødvendigt at konvertere dem fra tekst til numerisk for at få et givet diagram til at understøtte dem.

## Undgå vildledning

Selv hvis en dataforsker er omhyggelig med at vælge det rigtige diagram til de rigtige data, er der mange måder, hvorpå data kan vises for at bevise en pointe, ofte på bekostning af at undergrave dataene selv. Der findes mange eksempler på vildledende diagrammer og infografikker!

[![How Charts Lie af Alberto Cairo](../../../../../translated_images/da/tornado.2880ffc7f135f82b5e5328624799010abefd1080ae4b7ecacbdc7d792f1d8849.png)](https://www.youtube.com/watch?v=oX74Nge8Wkw "How charts lie")

> 🎥 Klik på billedet ovenfor for en konferencepræsentation om vildledende diagrammer

Dette diagram vender X-aksen om for at vise det modsatte af sandheden, baseret på dato:

![dårligt diagram 1](../../../../../translated_images/da/bad-chart-1.596bc93425a8ac301a28b8361f59a970276e7b961658ce849886aa1fed427341.png)

[Dette diagram](https://media.firstcoastnews.com/assets/WTLV/images/170ae16f-4643-438f-b689-50d66ca6a8d8/170ae16f-4643-438f-b689-50d66ca6a8d8_1140x641.jpg) er endnu mere vildledende, da øjet drages mod højre for at konkludere, at COVID-tilfælde over tid er faldet i de forskellige amter. Faktisk, hvis du ser nøje på datoerne, vil du opdage, at de er blevet omarrangeret for at give den vildledende nedadgående tendens.

![dårligt diagram 2](../../../../../translated_images/da/bad-chart-2.62edf4d2f30f4e519f5ef50c07ce686e27b0196a364febf9a4d98eecd21f9f60.jpg)

Dette berygtede eksempel bruger farve OG en vendt Y-akse til at vildlede: i stedet for at konkludere, at våbendrab steg efter vedtagelsen af våbenvenlig lovgivning, bliver øjet faktisk narret til at tro, at det modsatte er sandt:

![dårligt diagram 3](../../../../../translated_images/da/bad-chart-3.e201e2e915a230bc2cde289110604ec9abeb89be510bd82665bebc1228258972.jpg)

Dette mærkelige diagram viser, hvordan proportioner kan manipuleres, til komisk effekt:

![dårligt diagram 4](../../../../../translated_images/da/bad-chart-4.8872b2b881ffa96c3e0db10eb6aed7793efae2cac382c53932794260f7bfff07.jpg)

At sammenligne det, der ikke kan sammenlignes, er endnu et skummelt trick. Der er en [vidunderlig hjemmeside](https://tylervigen.com/spurious-correlations) dedikeret til 'spurious correlations', der viser 'fakta', der korrelerer ting som skilsmisseraten i Maine og forbruget af margarine. En Reddit-gruppe samler også [grimme eksempler](https://www.reddit.com/r/dataisugly/top/?t=all) på data.

Det er vigtigt at forstå, hvor let øjet kan narres af vildledende diagrammer. Selv hvis dataforskerens intention er god, kan valget af en dårlig type diagram, såsom et cirkeldiagram med for mange kategorier, være vildledende.

## Farver

Du så i 'Florida våbenvold'-diagrammet ovenfor, hvordan farver kan give et ekstra lag af mening til diagrammer, især dem, der ikke er designet ved hjælp af biblioteker som ggplot2 og RColorBrewer, som kommer med forskellige godkendte farvebiblioteker og paletter. Hvis du laver et diagram manuelt, så brug lidt tid på at studere [farveteori](https://colormatters.com/color-and-design/basic-color-theory)

> ✅ Vær opmærksom på, når du designer diagrammer, at tilgængelighed er en vigtig del af visualisering. Nogle af dine brugere kan være farveblinde - vises dit diagram godt for brugere med synshandicap?

Vær forsigtig, når du vælger farver til dit diagram, da farver kan formidle betydninger, du måske ikke har til hensigt. De 'pink ladies' i 'højde'-diagrammet ovenfor formidler en tydeligt 'feminin' tilskrevet betydning, der tilføjer til diagrammets mærkværdighed.

Mens [farvebetydning](https://colormatters.com/color-symbolism/the-meanings-of-colors) kan variere i forskellige dele af verden og har tendens til at ændre betydning afhængigt af deres nuance, inkluderer generelle farvebetydninger:

| Farve  | Betydning            |
| ------ | -------------------- |
| rød    | magt                |
| blå    | tillid, loyalitet   |
| gul    | glæde, forsigtighed |
| grøn   | økologi, held, misundelse |
| lilla  | glæde               |
| orange | livlighed           |

Hvis du får til opgave at bygge et diagram med brugerdefinerede farver, skal du sikre dig, at dine diagrammer både er tilgængelige, og at den farve, du vælger, stemmer overens med den betydning, du forsøger at formidle.

## Styling af diagrammer for læsbarhed

Diagrammer er ikke meningsfulde, hvis de ikke er læsbare! Tag et øjeblik til at overveje at style bredden og højden af dit diagram, så det passer godt til dine data. Hvis en variabel (såsom alle 50 stater) skal vises, skal du vise dem lodret på Y-aksen, hvis det er muligt, for at undgå et diagram, der skal rulles horisontalt.

Mærk dine akser, giv en forklaring, hvis det er nødvendigt, og tilbyd værktøjstip for bedre forståelse af data.

Hvis dine data er tekstuelle og lange på X-aksen, kan du vinkle teksten for bedre læsbarhed. [plot3D](https://cran.r-project.org/web/packages/plot3D/index.html) tilbyder 3D-plotning, hvis dine data understøtter det. Sofistikerede datavisualiseringer kan produceres ved hjælp af det.

![3d diagrammer](../../../../../translated_images/da/3d.db1734c151eee87d924989306a00e23f8cddac6a0aab122852ece220e9448def.png)

## Animation og 3D-diagramvisning

Nogle af de bedste datavisualiseringer i dag er animerede. Shirley Wu har fantastiske eksempler lavet med D3, såsom '[film flowers](http://bl.ocks.org/sxywu/raw/d612c6c653fb8b4d7ff3d422be164a5d/)', hvor hver blomst er en visualisering af en film. Et andet eksempel for Guardian er 'bussed out', en interaktiv oplevelse, der kombinerer visualiseringer med Greensock og D3 plus en scrollytelling-artikel for at vise, hvordan NYC håndterer sit hjemløse problem ved at sende folk ud af byen.

![bussing](../../../../../translated_images/da/busing.8157cf1bc89a3f65052d362a78c72f964982ceb9dcacbe44480e35909c3dce62.png)

> "Bussed Out: How America Moves its Homeless" fra [the Guardian](https://www.theguardian.com/us-news/ng-interactive/2017/dec/20/bussed-out-america-moves-homeless-people-country-study). Visualiseringer af Nadieh Bremer & Shirley Wu

Selvom denne lektion ikke går i dybden med at lære disse kraftfulde visualiseringsbiblioteker, kan du prøve D3 i en Vue.js-app ved hjælp af et bibliotek til at vise en visualisering af bogen "Dangerous Liaisons" som et animeret socialt netværk.

> "Les Liaisons Dangereuses" er en epistolær roman, eller en roman præsenteret som en række breve. Skrevet i 1782 af Choderlos de Laclos, fortæller den historien om de ondskabsfulde, moralsk forfaldne sociale manøvrer af to rivaliserende hovedpersoner fra det franske aristokrati i slutningen af det 18. århundrede, Vicomte de Valmont og Marquise de Merteuil. Begge møder deres undergang til sidst, men ikke uden at forårsage en stor social skade. Romanen udfolder sig som en række breve skrevet til forskellige personer i deres kredse, der planlægger hævn eller blot for at skabe problemer. Skab en visualisering af disse breve for at opdage de vigtigste aktører i fortællingen, visuelt.

Du vil fuldføre en webapp, der viser en animeret visning af dette sociale netværk. Den bruger et bibliotek, der blev bygget til at skabe en [visualisering af et netværk](https://github.com/emiliorizzo/vue-d3-network) ved hjælp af Vue.js og D3. Når appen kører, kan du trække noderne rundt på skærmen for at omarrangere dataene.

![liaisons](../../../../../translated_images/da/liaisons.90ce7360bcf8476558f700bbbaf198ad697d5b5cb2829ba141a89c0add7c6ecd.png)

## Projekt: Byg et diagram til at vise et netværk ved hjælp af D3.js

> Denne lektionsmappe inkluderer en `solution`-mappe, hvor du kan finde det færdige projekt som reference.

1. Følg instruktionerne i README.md-filen i starter-mappens rod. Sørg for, at du har NPM og Node.js kørende på din maskine, før du installerer projektets afhængigheder.

2. Åbn `starter/src`-mappen. Du vil finde en `assets`-mappe, hvor du kan finde en .json-fil med alle brevene fra romanen, nummereret, med en 'to' og 'from'-annotation.

3. Fuldfør koden i `components/Nodes.vue` for at aktivere visualiseringen. Find metoden kaldet `createLinks()` og tilføj følgende indlejrede loop.

Loop gennem .json-objektet for at fange 'to' og 'from'-dataene for brevene og opbyg `links`-objektet, så visualiseringsbiblioteket kan bruge det:

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

Kør din app fra terminalen (npm run serve) og nyd visualiseringen!

## 🚀 Udfordring

Tag en tur på internettet for at opdage vildledende visualiseringer. Hvordan narrer forfatteren brugeren, og er det med vilje? Prøv at rette visualiseringerne for at vise, hvordan de burde se ud.

## [Quiz efter lektionen](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/25)

## Gennemgang & Selvstudie

Her er nogle artikler om vildledende datavisualisering:

https://gizmodo.com/how-to-lie-with-data-visualization-1563576606

http://ixd.prattsi.org/2017/12/visual-lies-usability-in-deceptive-data-visualizations/

Tag et kig på disse interessante visualiseringer af historiske aktiver og artefakter:

https://handbook.pubpub.org/

Læs denne artikel om, hvordan animation kan forbedre dine visualiseringer:

https://medium.com/@EvanSinar/use-animation-to-supercharge-data-visualization-cd905a882ad4

## Opgave

[Byg din egen brugerdefinerede visualisering](assignment.md)

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.