# Definiera Data

|![ Sketchnote av [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/03-DefiningData.png)|
|:---:|
|Definiera Data - _Sketchnote av [@nitya](https://twitter.com/nitya)_ |

Data är fakta, information, observationer och mätningar som används för att göra upptäckter och stödja informerade beslut. En datapunkt är en enskild datadel inom en dataset, vilket är en samling datapunkter. Dataset kan komma i olika format och strukturer, och baseras vanligtvis på dess källa, eller varifrån datan kom. Till exempel kan ett företags månatliga intäkter finnas i ett kalkylblad medan timvisa data om hjärtfrekvens från en smartklocka kan vara i [JSON](https://stackoverflow.com/a/383699)-format. Det är vanligt att datavetare arbetar med olika typer av data inom en dataset. 

Denna lektion fokuserar på att identifiera och klassificera data efter dess egenskaper och dess källor.

## [Förföreläsningsquiz](https://ff-quizzes.netlify.app/en/ds/quiz/4)
## Hur data beskrivs

### Rå Data
Rå data är data som kommer från sin källa i sitt ursprungliga tillstånd och som inte har analyserats eller organiserats. För att förstå vad som händer med en dataset måste den organiseras i ett format som kan förstås av människor samt den teknik de kan använda för vidare analys. Strukturen i en dataset beskriver hur den är organiserad och kan klassificeras som strukturerad, ostrukturerad och semi-strukturerad. Dessa typer av struktur varierar beroende på källan men passar slutligen in i dessa tre kategorier. 

### Kvantitativ Data
Kvantitativ data är numeriska observationer inom en dataset och kan vanligen analyseras, mätas och användas matematiskt. Några exempel på kvantitativ data är: ett lands befolkning, en persons längd eller ett företags kvartalsintäkter. Med ytterligare analys kan kvantitativ data användas för att upptäcka säsongstrender av Air Quality Index (AQI) eller uppskatta sannolikheten för rusningstrafik en typisk arbetsdag.

### Kvalitativ Data
Kvalitativ data, även känd som kategorisk data, är data som inte kan mätas objektivt som observationer av kvantitativ data. Det är vanligtvis olika former av subjektiv data som fångar kvaliteten på något, såsom en produkt eller process. Ibland är kvalitativ data numerisk och används normalt inte matematiskt, som telefonnummer eller tidsstämplar. Några exempel på kvalitativ data är: videokommentarer, bilmärke och modell eller närmsta vänners favoritfärg. Kvalitativ data kan användas för att förstå vilka produkter konsumenter gillar bäst eller identifiera populära nyckelord i jobbansöknings-CV:n.

### Strukturerad Data
Strukturerad data är data som är organiserad i rader och kolumner, där varje rad har samma uppsättning av kolumner. Kolumner representerar ett värde av en viss typ och identifieras med ett namn som beskriver vad värdet representerar, medan rader innehåller de faktiska värdena. Kolumner har ofta en specifik uppsättning regler eller begränsningar för värdena, för att säkerställa att värdena korrekt representerar kolumnen. Till exempel, föreställ dig ett kalkylblad med kunder där varje rad måste ha ett telefonnummer och telefonnumren aldrig innehåller bokstäver. Det kan finnas regler för telefonnummerkolumnen för att säkerställa att den aldrig är tom och bara innehåller siffror. 

En fördel med strukturerad data är att den kan organiseras så att den kan relateras till annan strukturerad data. Men eftersom datan är utformad för att organiseras på ett specifikt sätt kan det ta mycket ansträngning att ändra dess övergripande struktur. Till exempel, att lägga till en e-postkolumn till kundkalkylbladet som inte får vara tom betyder att du måste komma på hur du lägger till dessa värden till de befintliga kundraderna i datasetet. 

Exempel på strukturerad data: kalkylblad, relationsdatabaser, telefonnummer, bankutdrag

### Ostrukturerad Data
Ostrukturerad data kan vanligtvis inte kategoriseras i rader eller kolumner och innehåller inte ett format eller en uppsättning regler att följa. Eftersom ostrukturerad data har färre begränsningar på sin struktur är det enklare att lägga till ny information jämfört med en strukturerad dataset. Om en sensor som mäter barometertryck varannan minut får en uppdatering som gör att den numera kan mäta och registrera temperatur krävs det ingen ändring av befintlig data om den är ostrukturerad. Detta kan dock göra analys eller undersökning av denna typ av data längre. Till exempel, en forskare som vill hitta genomsnittstemperaturen för föregående månad från sensorens data, upptäcker att sensorn registrerat ett "e" i vissa av sina registrerade data för att notera att den var trasig istället för ett vanligt nummer, vilket gör datan ofullständig.

Exempel på ostrukturerad data: textfiler, textmeddelanden, videofiler

### Semi-strukturerad
Semi-strukturerad data har egenskaper som gör den till en kombination av strukturerad och ostrukturerad data. Den följer vanligtvis inte ett format med rader och kolumner men är organiserad på ett sätt som anses strukturerat och kan följa ett fast format eller en uppsättning regler. Strukturen varierar mellan källor, från en väl definierad hierarki till något mer flexibelt som tillåter enkel integration av ny information. Metadata är indikatorer som hjälper till att avgöra hur data är organiserad och lagrad och har olika namn beroende på typen av data. Några vanliga namn för metadata är taggar, element, enheter och attribut. Till exempel, ett typiskt e-postmeddelande har en ämnesrad, innehåll och en uppsättning mottagare och kan organiseras efter vem eller när det skickades. 

Exempel på semi-strukturerad data: HTML, CSV-filer, JavaScript Object Notation (JSON)

## Datakällor 

En datakälla är den ursprungliga platsen där datan skapades eller där den "bor" och varierar beroende på hur och när den samlades in. Data som genereras av dess användare kallas primärdata medan sekundärdata kommer från en källa som samlat in data för allmänt bruk. Till exempel skulle en grupp forskare som samlar observationer i en regnskog betraktas som primär och om de bestämmer sig för att dela det med andra forskare skulle det betraktas som sekundär för dem som använder det. 

Databaser är en vanlig källa och förlitar sig på ett databashanteringssystem för att vara värd för och underhålla datan där användare använder kommandon kallade frågor för att utforska datan. Filer som datakällor kan vara ljud-, bild- och videofiler samt kalkylblad som Excel. Internetsidor är en vanlig plats för värd för data, där databaser såväl som filer kan hittas. Programmeringsgränssnitt, även kallade API:er, tillåter programmerare att skapa sätt att dela data med externa användare via internet, medan processen webbskrapning extraherar data från en webbsida. [Lektionerna i Arbete med Data](../../../../../../../../../2-Working-With-Data) fokuserar på hur man använder olika datakällor. 

## Sammanfattning

I denna lektion har vi lärt oss:

- Vad data är
- Hur data beskrivs
- Hur data klassificeras och kategoriseras
- Var data kan hittas

## 🚀 Utmaning

Kaggle är en utmärkt källa för öppna dataset. Använd [datasetsökverktyget](https://www.kaggle.com/datasets) för att hitta några intressanta dataset och klassificera 3-5 dataset enligt dessa kriterier:

- Är datan kvantitativ eller kvalitativ?
- Är datan strukturerad, ostrukturerad eller semi-strukturerad?

## [Efterföreläsningsquiz](https://ff-quizzes.netlify.app/en/ds/quiz/5)



## Granskning & Självstudier

- Denna Microsoft Learn-enhet, med titeln [Identify data formats](https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats?pivots=text) har en detaljerad översikt av strukturerad, semi-strukturerad och ostrukturerad data.

## Uppgift

[Klassificering av Dataset](assignment.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->