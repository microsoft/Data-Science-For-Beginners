<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a0516588d172f82f35f7a0d4a001e5d0",
  "translation_date": "2025-09-05T21:52:57+00:00",
  "source_file": "1-Introduction/01-defining-data-science/README.md",
  "language_code": "sv"
}
-->
## Typer av data

Som vi redan nämnt, finns data överallt. Vi behöver bara fånga den på rätt sätt! Det är användbart att skilja mellan **strukturerad** och **ostrukturerad** data. Den förstnämnda representeras ofta i en välstrukturerad form, ofta som en tabell eller flera tabeller, medan den sistnämnda bara är en samling filer. Ibland kan vi också tala om **semistrukturerad** data, som har någon form av struktur som kan variera mycket.

| Strukturerad                                                                | Semistrukturerad                                                                               | Ostrukturerad                          |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | --------------------------------------- |
| Lista över personer med deras telefonnummer                                 | Wikipediasidor med länkar                                                                      | Text från Encyclopedia Britannica      |
| Temperatur i alla rum i en byggnad varje minut under de senaste 20 åren     | Samling av vetenskapliga artiklar i JSON-format med författare, publiceringsdatum och abstrakt | Filarkiv med företagsdokument          |
| Data om ålder och kön för alla som går in i byggnaden                       | Internetsidor                                                                                  | Rå videoström från övervakningskamera  |

## Var man kan få tag på data

Det finns många möjliga källor till data, och det är omöjligt att lista alla! Men låt oss nämna några typiska platser där du kan få tag på data:

* **Strukturerad**
  - **Internet of Things** (IoT), inklusive data från olika sensorer, såsom temperatur- eller trycksensorer, ger mycket användbar data. Till exempel, om en kontorsbyggnad är utrustad med IoT-sensorer, kan vi automatiskt kontrollera uppvärmning och belysning för att minimera kostnader.
  - **Enkäter** som vi ber användare att fylla i efter ett köp eller efter att ha besökt en webbplats.
  - **Beteendeanalys** kan till exempel hjälpa oss att förstå hur djupt en användare går in på en webbplats och vad som är den typiska orsaken till att lämna sidan.
* **Ostrukturerad**
  - **Texter** kan vara en rik källa till insikter, såsom ett övergripande **sentimentsbetyg** eller att extrahera nyckelord och semantisk betydelse.
  - **Bilder** eller **Video**. En video från en övervakningskamera kan användas för att uppskatta trafik på vägen och informera människor om potentiella trafikstockningar.
  - **Loggar** från webbservrar kan användas för att förstå vilka sidor på vår webbplats som besöks mest och hur länge.
* **Semistrukturerad**
  - **Sociala nätverks** grafer kan vara utmärkta källor till data om användares personligheter och potentiell effektivitet i att sprida information.
  - När vi har en samling fotografier från en fest kan vi försöka extrahera data om **gruppdynamik** genom att bygga en graf över personer som tar bilder med varandra.

Genom att känna till olika möjliga datakällor kan du försöka tänka på olika scenarier där datavetenskapliga tekniker kan tillämpas för att förstå situationen bättre och förbättra affärsprocesser.

## Vad du kan göra med data

Inom datavetenskap fokuserar vi på följande steg i datans resa:

## Digitalisering och digital transformation

Under det senaste decenniet har många företag börjat förstå vikten av data vid affärsbeslut. För att tillämpa datavetenskapliga principer på att driva ett företag måste man först samla in data, det vill säga översätta affärsprocesser till digital form. Detta kallas **digitalisering**. Att använda datavetenskapliga tekniker på denna data för att vägleda beslut kan leda till betydande produktivitetsökningar (eller till och med en affärsomvandling), vilket kallas **digital transformation**.

Låt oss ta ett exempel. Anta att vi har en datavetenskapskurs (som denna) som vi levererar online till studenter, och vi vill använda datavetenskap för att förbättra den. Hur kan vi göra det?

Vi kan börja med att fråga "Vad kan digitaliseras?" Det enklaste sättet skulle vara att mäta tiden det tar för varje student att slutföra varje modul och att mäta den förvärvade kunskapen genom att ge ett flervalsprov i slutet av varje modul. Genom att beräkna genomsnittlig tid för att slutföra modulerna över alla studenter kan vi ta reda på vilka moduler som orsakar mest svårigheter för studenterna och arbeta på att förenkla dem.
> Du kanske hävdar att denna metod inte är optimal, eftersom moduler kan ha olika längder. Det är förmodligen mer rättvist att dela tiden med modulens längd (i antal tecken) och jämföra dessa värden istället.
När vi börjar analysera resultaten från flervalsprov kan vi försöka identifiera vilka koncept som elever har svårt att förstå, och använda den informationen för att förbättra innehållet. För att göra detta behöver vi utforma prov på ett sätt där varje fråga kopplas till ett visst koncept eller kunskapsområde.

Om vi vill göra det ännu mer avancerat kan vi jämföra tiden som krävs för att slutföra varje modul med studenternas ålderskategori. Vi kanske upptäcker att det tar orimligt lång tid för vissa åldersgrupper att slutföra modulen, eller att studenter hoppar av innan de är klara. Detta kan hjälpa oss att ge åldersrekommendationer för modulen och minimera missnöje som uppstår från felaktiga förväntningar.

## 🚀 Utmaning

I denna utmaning ska vi försöka hitta koncept som är relevanta för området Data Science genom att analysera texter. Vi kommer att ta en Wikipedia-artikel om Data Science, ladda ner och bearbeta texten, och sedan skapa ett ordmoln som detta:

![Ordmoln för Data Science](../../../../1-Introduction/01-defining-data-science/images/ds_wordcloud.png)

Besök [`notebook.ipynb`](../../../../../../../../../1-Introduction/01-defining-data-science/notebook.ipynb ':ignore') för att läsa igenom koden. Du kan också köra koden och se hur den utför alla datatransformationer i realtid.

> Om du inte vet hur man kör kod i en Jupyter Notebook, ta en titt på [denna artikel](https://soshnikov.com/education/how-to-execute-notebooks-from-github/).

## [Quiz efter föreläsningen](https://ff-quizzes.netlify.app/en/ds/quiz/1)

## Uppgifter

* **Uppgift 1**: Modifiera koden ovan för att hitta relaterade koncept för områdena **Big Data** och **Machine Learning**  
* **Uppgift 2**: [Fundera över scenarier inom Data Science](assignment.md)

## Krediter

Denna lektion har skapats med ♥️ av [Dmitry Soshnikov](http://soshnikov.com)

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiserade översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som kan uppstå vid användning av denna översättning.