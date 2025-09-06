<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "12339119c0165da569a93ddba05f9339",
  "translation_date": "2025-09-05T21:53:17+00:00",
  "source_file": "1-Introduction/03-defining-data/README.md",
  "language_code": "sv"
}
-->
# Definiera Data

|![ Sketchnote av [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/03-DefiningData.png)|
|:---:|
|Definiera Data - _Sketchnote av [@nitya](https://twitter.com/nitya)_ |

Data är fakta, information, observationer och mätningar som används för att göra upptäckter och stödja välgrundade beslut. En datapunkt är en enskild enhet av data inom en dataset, som är en samling av datapunkter. Dataset kan ha olika format och strukturer och baseras ofta på dess källa, eller var datan kommer ifrån. Till exempel kan ett företags månatliga intäkter finnas i ett kalkylblad, medan timdata om hjärtfrekvens från en smartklocka kan vara i [JSON](https://stackoverflow.com/a/383699)-format. Det är vanligt att dataanalytiker arbetar med olika typer av data inom en dataset.

Den här lektionen fokuserar på att identifiera och klassificera data utifrån dess egenskaper och källor.

## [Förföreläsningsquiz](https://ff-quizzes.netlify.app/en/ds/quiz/4)
## Hur Data Beskrivs

### Rådata
Rådata är data som kommer från sin källa i sitt ursprungliga tillstånd och som inte har analyserats eller organiserats. För att förstå vad som händer med en dataset måste den organiseras i ett format som kan förstås av människor såväl som av den teknik de kan använda för att analysera den vidare. Strukturen av en dataset beskriver hur den är organiserad och kan klassificeras som strukturerad, ostrukturerad och semistrukturerad. Dessa typer av strukturer varierar beroende på källan men passar i slutändan in i dessa tre kategorier.

### Kvantitativ Data
Kvantitativ data är numeriska observationer inom en dataset och kan vanligtvis analyseras, mätas och användas matematiskt. Några exempel på kvantitativ data är: ett lands befolkning, en persons längd eller ett företags kvartalsintäkter. Med ytterligare analys kan kvantitativ data användas för att upptäcka säsongstrender i luftkvalitetsindex (AQI) eller uppskatta sannolikheten för rusningstrafik under en typisk arbetsdag.

### Kvalitativ Data
Kvalitativ data, även kallad kategorisk data, är data som inte kan mätas objektivt som kvantitativa observationer. Det är generellt olika format av subjektiv data som fångar kvaliteten på något, såsom en produkt eller process. Ibland är kvalitativ data numerisk men används inte typiskt matematiskt, som telefonnummer eller tidsstämplar. Några exempel på kvalitativ data är: videokommentarer, bilmärke och modell eller din närmaste väns favoritfärg. Kvalitativ data kan användas för att förstå vilka produkter konsumenter gillar bäst eller identifiera populära nyckelord i jobbansökningar.

### Strukturerad Data
Strukturerad data är data som är organiserad i rader och kolumner, där varje rad har samma uppsättning kolumner. Kolumner representerar ett värde av en viss typ och identifieras med ett namn som beskriver vad värdet representerar, medan rader innehåller de faktiska värdena. Kolumner har ofta en specifik uppsättning regler eller begränsningar för värdena för att säkerställa att värdena korrekt representerar kolumnen. Till exempel, föreställ dig ett kalkylblad med kunder där varje rad måste ha ett telefonnummer och telefonnumren aldrig innehåller alfabetiska tecken. Det kan finnas regler för telefonnummerkolumnen för att säkerställa att den aldrig är tom och endast innehåller siffror.

En fördel med strukturerad data är att den kan organiseras på ett sätt som gör att den kan relateras till annan strukturerad data. Men eftersom datan är designad för att vara organiserad på ett specifikt sätt kan det krävas mycket arbete att ändra dess övergripande struktur. Till exempel, att lägga till en e-postkolumn i kundkalkylbladet som inte får vara tom innebär att du måste lista ut hur du ska lägga till dessa värden i de befintliga raderna av kunder i datasetet.

Exempel på strukturerad data: kalkylblad, relationsdatabaser, telefonnummer, kontoutdrag

### Ostrukturerad Data
Ostrukturerad data kan vanligtvis inte kategoriseras i rader eller kolumner och innehåller inte ett format eller en uppsättning regler att följa. Eftersom ostrukturerad data har färre begränsningar på sin struktur är det lättare att lägga till ny information jämfört med en strukturerad dataset. Om en sensor som registrerar data om barometertryck varannan minut har fått en uppdatering som nu gör det möjligt att mäta och registrera temperatur, kräver det inte att den befintliga datan ändras om den är ostrukturerad. Dock kan detta göra analys eller undersökning av denna typ av data mer tidskrävande. Till exempel, en forskare som vill hitta genomsnittstemperaturen för föregående månad från sensorns data, men upptäcker att sensorn registrerade ett "e" i vissa av sina data för att indikera att den var trasig istället för ett typiskt nummer, vilket innebär att datan är ofullständig.

Exempel på ostrukturerad data: textfiler, textmeddelanden, videofiler

### Semistrukturerad Data
Semistrukturerad data har egenskaper som gör den till en kombination av strukturerad och ostrukturerad data. Den följer vanligtvis inte ett format av rader och kolumner men är organiserad på ett sätt som anses strukturerat och kan följa ett fast format eller en uppsättning regler. Strukturen varierar mellan källor, från en väl definierad hierarki till något mer flexibelt som möjliggör enkel integration av ny information. Metadata är indikatorer som hjälper till att avgöra hur datan är organiserad och lagrad och har olika namn beroende på typen av data. Några vanliga namn för metadata är taggar, element, entiteter och attribut. Till exempel, ett typiskt e-postmeddelande har ett ämne, en kropp och en uppsättning mottagare och kan organiseras efter vem eller när det skickades.

Exempel på semistrukturerad data: HTML, CSV-filer, JavaScript Object Notation (JSON)

## Datakällor

En datakälla är den ursprungliga platsen där datan genererades, eller var den "lever" och varierar beroende på hur och när den samlades in. Data som genereras av dess användare kallas primärdata medan sekundärdata kommer från en källa som har samlat in data för allmänt bruk. Till exempel, en grupp forskare som samlar observationer i en regnskog skulle betraktas som primärdata, och om de bestämmer sig för att dela den med andra forskare skulle det betraktas som sekundärdata för dem som använder den.

Databaser är en vanlig källa och förlitar sig på ett databashanteringssystem för att vara värd för och underhålla datan där användare använder kommandon som kallas frågor för att utforska datan. Filer som datakällor kan vara ljud-, bild- och videofiler samt kalkylblad som Excel. Internetsidor är en vanlig plats för att vara värd för data, där både databaser och filer kan hittas. Applikationsprogrammeringsgränssnitt, även kända som API:er, gör det möjligt för programmerare att skapa sätt att dela data med externa användare via internet, medan processen för webbscraping extraherar data från en webbsida. [Lektionen i Att Arbeta med Data](../../../../../../../../../2-Working-With-Data) fokuserar på hur man använder olika datakällor.

## Slutsats

I den här lektionen har vi lärt oss:

- Vad data är
- Hur data beskrivs
- Hur data klassificeras och kategoriseras
- Var data kan hittas

## 🚀 Utmaning

Kaggle är en utmärkt källa för öppna dataset. Använd [verktyget för dataset-sökning](https://www.kaggle.com/datasets) för att hitta några intressanta dataset och klassificera 3-5 dataset enligt följande kriterier:

- Är datan kvantitativ eller kvalitativ?
- Är datan strukturerad, ostrukturerad eller semistrukturerad?

## [Efterföreläsningsquiz](https://ff-quizzes.netlify.app/en/ds/quiz/5)

## Granskning & Självstudier

- Denna Microsoft Learn-enhet, med titeln [Klassificera din Data](https://docs.microsoft.com/en-us/learn/modules/choose-storage-approach-in-azure/2-classify-data), har en detaljerad genomgång av strukturerad, semistrukturerad och ostrukturerad data.

## Uppgift

[Klassificera Dataset](assignment.md)

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiserade översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som kan uppstå vid användning av denna översättning.