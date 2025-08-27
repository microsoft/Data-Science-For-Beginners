<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "356d12cffc3125db133a2d27b827a745",
  "translation_date": "2025-08-26T21:37:29+00:00",
  "source_file": "1-Introduction/03-defining-data/README.md",
  "language_code": "sv"
}
-->
# Definiera Data

|![ Sketchnote av [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/03-DefiningData.png)|
|:---:|
|Definiera Data - _Sketchnote av [@nitya](https://twitter.com/nitya)_ |

Data är fakta, information, observationer och mätningar som används för att göra upptäckter och stödja välgrundade beslut. En datapunkt är en enskild enhet av data inom en dataset, som är en samling av datapunkter. Dataset kan ha olika format och strukturer och baseras ofta på sin källa, det vill säga var datan kommer ifrån. Till exempel kan ett företags månatliga intäkter finnas i ett kalkylblad, medan timvisa pulsmätningar från en smartklocka kan vara i [JSON](https://stackoverflow.com/a/383699)-format. Det är vanligt att dataforskare arbetar med olika typer av data inom en dataset.

Denna lektion fokuserar på att identifiera och klassificera data utifrån dess egenskaper och källor.

## [Förtest](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/4)
## Hur Data Beskrivs

### Rådata
Rådata är data som kommer direkt från sin källa i sitt ursprungliga tillstånd och som inte har analyserats eller organiserats. För att förstå vad som händer i en dataset måste den organiseras i ett format som kan förstås av både människor och den teknik som används för att analysera den vidare. Strukturen av en dataset beskriver hur den är organiserad och kan klassificeras som strukturerad, ostrukturerad eller semistrukturerad. Dessa typer av strukturer varierar beroende på källan men passar i slutändan in i dessa tre kategorier.

### Kvantitativ Data
Kvantitativ data är numeriska observationer inom en dataset och kan vanligtvis analyseras, mätas och användas matematiskt. Några exempel på kvantitativ data är: ett lands befolkning, en persons längd eller ett företags kvartalsintäkter. Med ytterligare analys kan kvantitativ data användas för att upptäcka säsongstrender i luftkvalitetsindexet (AQI) eller uppskatta sannolikheten för rusningstrafik under en typisk arbetsdag.

### Kvalitativ Data
Kvalitativ data, även känd som kategorisk data, är data som inte kan mätas objektivt som kvantitativ data. Det är generellt olika format av subjektiv data som fångar kvaliteten på något, som en produkt eller en process. Ibland är kvalitativ data numerisk men används inte typiskt matematiskt, som telefonnummer eller tidsstämplar. Några exempel på kvalitativ data är: videokommentarer, bilmärken och modeller eller dina närmaste vänners favoritfärg. Kvalitativ data kan användas för att förstå vilka produkter konsumenter gillar bäst eller för att identifiera populära nyckelord i jobbansökningar.

### Strukturerad Data
Strukturerad data är data som är organiserad i rader och kolumner, där varje rad har samma uppsättning kolumner. Kolumner representerar ett värde av en viss typ och identifieras med ett namn som beskriver vad värdet representerar, medan rader innehåller de faktiska värdena. Kolumner har ofta en specifik uppsättning regler eller begränsningar för värdena för att säkerställa att värdena korrekt representerar kolumnen. Till exempel, föreställ dig ett kalkylblad med kunder där varje rad måste ha ett telefonnummer och telefonnumren aldrig innehåller bokstäver. Det kan finnas regler för telefonnummerkolumnen för att säkerställa att den aldrig är tom och endast innehåller siffror.

En fördel med strukturerad data är att den kan organiseras på ett sätt som gör att den kan relateras till annan strukturerad data. Men eftersom datan är designad för att vara organiserad på ett specifikt sätt kan det krävas mycket arbete att ändra dess övergripande struktur. Till exempel, om du lägger till en e-postkolumn i kundkalkylbladet som inte får vara tom, måste du lista ut hur du ska lägga till dessa värden i de befintliga raderna i datasetet.

Exempel på strukturerad data: kalkylblad, relationsdatabaser, telefonnummer, kontoutdrag

### Ostrukturerad Data
Ostrukturerad data kan vanligtvis inte kategoriseras i rader eller kolumner och innehåller inget format eller uppsättning regler att följa. Eftersom ostrukturerad data har färre begränsningar på sin struktur är det enklare att lägga till ny information jämfört med en strukturerad dataset. Om en sensor som mäter barometertryck varannan minut får en uppdatering som gör att den nu kan mäta och registrera temperatur, kräver det ingen ändring av den befintliga datan om den är ostrukturerad. Detta kan dock göra det mer tidskrävande att analysera eller undersöka denna typ av data. Till exempel, en forskare som vill hitta medeltemperaturen för föregående månad från sensorens data men upptäcker att sensorn registrerat ett "e" i vissa av sina data för att indikera att den var trasig istället för ett typiskt nummer, vilket innebär att datan är ofullständig.

Exempel på ostrukturerad data: textfiler, textmeddelanden, videofiler

### Semistrukturerad Data
Semistrukturerad data har egenskaper som gör den till en kombination av strukturerad och ostrukturerad data. Den följer vanligtvis inte ett format av rader och kolumner men är organiserad på ett sätt som anses strukturerat och kan följa ett fast format eller en uppsättning regler. Strukturen varierar mellan källor, från en väl definierad hierarki till något mer flexibelt som möjliggör enkel integration av ny information. Metadata är indikatorer som hjälper till att avgöra hur datan är organiserad och lagrad och har olika namn beroende på datatypen. Några vanliga namn för metadata är taggar, element, entiteter och attribut. Till exempel, ett typiskt e-postmeddelande har ett ämne, en brödtext och en uppsättning mottagare och kan organiseras efter vem eller när det skickades.

Exempel på semistrukturerad data: HTML, CSV-filer, JavaScript Object Notation (JSON)

## Datakällor

En datakälla är den ursprungliga platsen där datan genererades eller där den "finns" och varierar beroende på hur och när den samlades in. Data som genereras av dess användare kallas primärdata medan sekundärdata kommer från en källa som har samlat in data för allmänt bruk. Till exempel, en grupp forskare som samlar observationer i en regnskog skulle betraktas som primärdata, och om de bestämmer sig för att dela den med andra forskare skulle den betraktas som sekundärdata för dem som använder den.

Databaser är en vanlig källa och förlitar sig på ett databashanteringssystem för att vara värd för och underhålla datan där användare använder kommandon som kallas frågor för att utforska datan. Filer som datakällor kan vara ljud-, bild- och videofiler samt kalkylblad som Excel. Internetsidor är en vanlig plats för att vara värd för data, där både databaser och filer kan hittas. Applikationsprogrammeringsgränssnitt, även kända som API:er, gör det möjligt för programmerare att skapa sätt att dela data med externa användare via internet, medan processen för web scraping extraherar data från en webbsida. [Lektionerna i Arbeta med Data](../../../../../../../../../2-Working-With-Data) fokuserar på hur man använder olika datakällor.

## Slutsats

I denna lektion har vi lärt oss:

- Vad data är
- Hur data beskrivs
- Hur data klassificeras och kategoriseras
- Var data kan hittas

## 🚀 Utmaning

Kaggle är en utmärkt källa för öppna dataset. Använd [verktyget för dataset-sökning](https://www.kaggle.com/datasets) för att hitta några intressanta dataset och klassificera 3-5 dataset enligt följande kriterier:

- Är datan kvantitativ eller kvalitativ?
- Är datan strukturerad, ostrukturerad eller semistrukturerad?

## [Eftertest](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/5)

## Granskning & Självstudier

- Denna Microsoft Learn-enhet, med titeln [Klassificera din Data](https://docs.microsoft.com/en-us/learn/modules/choose-storage-approach-in-azure/2-classify-data), har en detaljerad genomgång av strukturerad, semistrukturerad och ostrukturerad data.

## Uppgift

[Klassificera Dataset](assignment.md)

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiska översättningar kan innehålla fel eller inexaktheter. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.