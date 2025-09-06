<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "12339119c0165da569a93ddba05f9339",
  "translation_date": "2025-09-05T22:09:02+00:00",
  "source_file": "1-Introduction/03-defining-data/README.md",
  "language_code": "da"
}
-->
# Definering af Data

|![ Sketchnote af [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/03-DefiningData.png)|
|:---:|
|Definering af Data - _Sketchnote af [@nitya](https://twitter.com/nitya)_ |

Data er fakta, information, observationer og målinger, der bruges til at gøre opdagelser og træffe informerede beslutninger. Et datapunkt er en enkelt enhed af data i et datasæt, som er en samling af datapunkter. Datasæt kan komme i forskellige formater og strukturer og vil typisk være baseret på deres kilde, eller hvor dataene stammer fra. For eksempel kan en virksomheds månedlige indtjening være i et regneark, mens timebaserede pulsdata fra et smartwatch kan være i [JSON](https://stackoverflow.com/a/383699)-format. Det er almindeligt, at dataspecialister arbejder med forskellige typer data inden for et datasæt.

Denne lektion fokuserer på at identificere og klassificere data ud fra deres karakteristika og kilder.

## [Quiz før lektionen](https://ff-quizzes.netlify.app/en/ds/quiz/4)

## Hvordan data beskrives

### Rådata
Rådata er data, der kommer fra deres kilde i deres oprindelige tilstand og ikke er blevet analyseret eller organiseret. For at forstå, hvad der sker i et datasæt, skal det organiseres i et format, der kan forstås af både mennesker og den teknologi, de bruger til yderligere analyse. Strukturen af et datasæt beskriver, hvordan det er organiseret, og kan klassificeres som struktureret, ustruktureret og semistruktureret. Disse strukturer varierer afhængigt af kilden, men vil i sidste ende passe ind i disse tre kategorier.

### Kvantitative data
Kvantitative data er numeriske observationer i et datasæt og kan typisk analyseres, måles og bruges matematisk. Nogle eksempler på kvantitative data er: et lands befolkning, en persons højde eller en virksomheds kvartalsvise indtjening. Med yderligere analyse kan kvantitative data bruges til at opdage sæsonmæssige tendenser i luftkvalitetsindekset (AQI) eller estimere sandsynligheden for myldretidstrafik på en typisk arbejdsdag.

### Kvalitative data
Kvalitative data, også kendt som kategoriske data, er data, der ikke kan måles objektivt som observationer af kvantitative data. Det er generelt forskellige formater af subjektive data, der fanger kvaliteten af noget, såsom et produkt eller en proces. Nogle gange er kvalitative data numeriske, men bruges typisk ikke matematisk, som for eksempel telefonnumre eller tidsstempler. Nogle eksempler på kvalitative data er: videokommentarer, mærke og model på en bil eller dine nærmeste venners yndlingsfarve. Kvalitative data kan bruges til at forstå, hvilke produkter forbrugerne bedst kan lide, eller til at identificere populære nøgleord i jobansøgninger.

### Strukturerede data
Strukturerede data er data, der er organiseret i rækker og kolonner, hvor hver række har det samme sæt kolonner. Kolonner repræsenterer en værdi af en bestemt type og identificeres med et navn, der beskriver, hvad værdien repræsenterer, mens rækker indeholder de faktiske værdier. Kolonner har ofte et specifikt sæt regler eller begrænsninger for værdierne for at sikre, at værdierne nøjagtigt repræsenterer kolonnen. For eksempel forestil dig et regneark med kunder, hvor hver række skal have et telefonnummer, og telefonnumrene aldrig indeholder bogstaver. Der kan være regler for telefonnummerkolonnen for at sikre, at den aldrig er tom og kun indeholder tal.

En fordel ved strukturerede data er, at de kan organiseres på en måde, der kan relateres til andre strukturerede data. Men fordi dataene er designet til at være organiseret på en bestemt måde, kan det kræve meget arbejde at ændre deres overordnede struktur. For eksempel, hvis du tilføjer en e-mail-kolonne til kunderegnearket, der ikke må være tom, skal du finde ud af, hvordan du tilføjer disse værdier til de eksisterende rækker i datasættet.

Eksempler på strukturerede data: regneark, relationelle databaser, telefonnumre, kontoudtog.

### Ustrukturerede data
Ustrukturerede data kan typisk ikke kategoriseres i rækker eller kolonner og har ikke et format eller et sæt regler at følge. Fordi ustrukturerede data har færre begrænsninger på deres struktur, er det lettere at tilføje ny information sammenlignet med et struktureret datasæt. Hvis en sensor, der registrerer data om barometertryk hvert andet minut, får en opdatering, der nu gør det muligt at måle og registrere temperatur, kræver det ikke ændringer i de eksisterende data, hvis de er ustrukturerede. Dette kan dog gøre det mere tidskrævende at analysere eller undersøge denne type data. For eksempel kan en forsker, der ønsker at finde gennemsnitstemperaturen for den foregående måned fra sensorens data, opdage, at sensoren har registreret et "e" i nogle af sine data for at angive, at den var i stykker, hvilket betyder, at dataene er ufuldstændige.

Eksempler på ustrukturerede data: tekstfiler, tekstbeskeder, videofiler.

### Semistrukturerede data
Semistrukturerede data har egenskaber, der gør dem til en kombination af strukturerede og ustrukturerede data. De følger typisk ikke et format med rækker og kolonner, men er organiseret på en måde, der anses for struktureret og kan følge et fast format eller et sæt regler. Strukturen varierer mellem kilder, fra en veldefineret hierarki til noget mere fleksibelt, der gør det nemt at integrere ny information. Metadata er indikatorer, der hjælper med at bestemme, hvordan dataene er organiseret og gemt, og de har forskellige navne afhængigt af datatypen. Nogle almindelige navne for metadata er tags, elementer, enheder og attributter. For eksempel vil en typisk e-mailbesked have et emne, en brødtekst og en række modtagere og kan organiseres efter, hvem eller hvornår den blev sendt.

Eksempler på semistrukturerede data: HTML, CSV-filer, JavaScript Object Notation (JSON).

## Datakilder

En datakilde er det oprindelige sted, hvor dataene blev genereret, eller hvor de "bor", og det vil variere afhængigt af, hvordan og hvornår de blev indsamlet. Data genereret af brugeren/brugerne kaldes primære data, mens sekundære data kommer fra en kilde, der har indsamlet data til generel brug. For eksempel vil en gruppe forskere, der indsamler observationer i en regnskov, blive betragtet som primære, og hvis de beslutter at dele det med andre forskere, vil det blive betragtet som sekundære for dem, der bruger det.

Databaser er en almindelig kilde og er afhængige af et databasehåndteringssystem til at hoste og vedligeholde dataene, hvor brugere bruger kommandoer kaldet forespørgsler til at udforske dataene. Filer som datakilder kan være lyd-, billed- og videofiler samt regneark som Excel. Internettet er en almindelig placering for hosting af data, hvor både databaser og filer kan findes. Application programming interfaces, også kendt som API'er, giver programmører mulighed for at skabe måder at dele data med eksterne brugere via internettet, mens processen med web scraping udtrækker data fra en webside. [Lektionerne i Arbejde med Data](../../../../../../../../../2-Working-With-Data) fokuserer på, hvordan man bruger forskellige datakilder.

## Konklusion

I denne lektion har vi lært:

- Hvad data er
- Hvordan data beskrives
- Hvordan data klassificeres og kategoriseres
- Hvor data kan findes

## 🚀 Udfordring

Kaggle er en fremragende kilde til åbne datasæt. Brug [værktøjet til datasætsøgning](https://www.kaggle.com/datasets) til at finde nogle interessante datasæt og klassificer 3-5 datasæt med følgende kriterier:

- Er dataene kvantitative eller kvalitative?
- Er dataene strukturerede, ustrukturerede eller semistrukturerede?

## [Quiz efter lektionen](https://ff-quizzes.netlify.app/en/ds/quiz/5)

## Gennemgang & Selvstudie

- Denne Microsoft Learn-enhed, med titlen [Klassificer dine data](https://docs.microsoft.com/en-us/learn/modules/choose-storage-approach-in-azure/2-classify-data), har en detaljeret gennemgang af strukturerede, semistrukturerede og ustrukturerede data.

## Opgave

[Klassificering af datasæt](assignment.md)

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os ikke ansvar for eventuelle misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.