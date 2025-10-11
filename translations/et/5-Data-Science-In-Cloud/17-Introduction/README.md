<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f8e7cdefa096664ae86f795be571580",
  "translation_date": "2025-10-11T15:29:17+00:00",
  "source_file": "5-Data-Science-In-Cloud/17-Introduction/README.md",
  "language_code": "et"
}
-->
# Sissejuhatus andmeteadusesse pilves

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/17-DataScience-Cloud.png)|
|:---:|
| Andmeteadus pilves: Sissejuhatus - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

Selles õppetükis õpid pilveteenuste põhimõtteid, saad teada, miks võib olla huvitav kasutada pilveteenuseid oma andmeteaduse projektide käitamiseks, ning vaatame mõningaid näiteid andmeteaduse projektidest, mis on pilves teostatud.

## [Eelloengu viktoriin](https://ff-quizzes.netlify.app/en/ds/quiz/32)

## Mis on pilv?

Pilv, või pilvearvutus, tähendab mitmesuguste tasuliste arvutiteenuste pakkumist interneti kaudu. Teenused hõlmavad lahendusi nagu salvestusruum, andmebaasid, võrgundus, tarkvara, analüütika ja intelligentsed teenused.

Tavaliselt eristatakse avalikku, privaatset ja hübriidpilve järgmiselt:

* Avalik pilv: avalik pilv kuulub ja seda haldab kolmanda osapoole pilveteenuse pakkuja, kes pakub oma arvutusressursse interneti kaudu avalikkusele.
* Privaatne pilv: viitab pilvearvutuse ressurssidele, mida kasutab ainult üks ettevõte või organisatsioon, kus teenused ja infrastruktuur on hallatud privaatvõrgus.
* Hübriidpilv: hübriidpilv on süsteem, mis ühendab avaliku ja privaatse pilve. Kasutajad valivad kohapealse andmekeskuse, võimaldades samal ajal andmete ja rakenduste käitamist ühes või mitmes avalikus pilves.

Enamik pilvearvutuse teenuseid jaguneb kolme kategooriasse: infrastruktuur kui teenus (IaaS), platvorm kui teenus (PaaS) ja tarkvara kui teenus (SaaS).

* Infrastruktuur kui teenus (IaaS): kasutajad rendivad IT-infrastruktuuri, nagu serverid ja virtuaalmasinad (VM-id), salvestusruumid, võrgud, operatsioonisüsteemid.
* Platvorm kui teenus (PaaS): kasutajad rendivad keskkonna tarkvararakenduste arendamiseks, testimiseks, tarnimiseks ja haldamiseks. Kasutajad ei pea muretsema serverite, salvestusruumide, võrkude ja andmebaaside infrastruktuuri seadistamise või haldamise pärast.
* Tarkvara kui teenus (SaaS): kasutajad saavad tarkvararakendustele interneti kaudu juurdepääsu nõudmisel ja tavaliselt tellimuse alusel. Kasutajad ei pea muretsema tarkvararakenduse majutamise ja haldamise, infrastruktuuri ega hoolduse, nagu tarkvarauuenduste ja turvaparanduste pärast.

Mõned suurimad pilveteenuste pakkujad on Amazon Web Services, Google Cloud Platform ja Microsoft Azure.

## Miks valida pilv andmeteaduseks?

Arendajad ja IT-spetsialistid valivad pilve kasutamise mitmel põhjusel, sealhulgas:

* Innovatsioon: saate oma rakendusi täiustada, integreerides pilveteenuse pakkujate loodud innovaatilisi teenuseid otse oma rakendustesse.
* Paindlikkus: maksate ainult nende teenuste eest, mida vajate, ja saate valida laia valiku teenuste hulgast. Tavaliselt maksate vastavalt kasutusele ja kohandate teenuseid vastavalt oma muutuvatele vajadustele.
* Eelarve: te ei pea tegema esialgseid investeeringuid riistvara ja tarkvara ostmiseks, kohapealsete andmekeskuste seadistamiseks ja haldamiseks; maksate ainult selle eest, mida kasutate.
* Mastaapsus: teie ressursid võivad vastavalt projekti vajadustele mastaapselt kasvada või kahaneda, mis tähendab, et teie rakendused saavad kasutada rohkem või vähem arvutusvõimsust, salvestusruumi ja ribalaiust, kohandudes igal ajahetkel väliste teguritega.
* Tootlikkus: saate keskenduda oma ärile, selle asemel et kulutada aega ülesannetele, mida saab hallata keegi teine, näiteks andmekeskuste haldamine.
* Usaldusväärsus: pilvearvutus pakub mitmeid viise oma andmete pidevaks varundamiseks ja saate luua katastroofide taastamise plaanid, et hoida oma äri ja teenused käimas ka kriisi ajal.
* Turvalisus: saate kasu poliitikast, tehnoloogiatest ja kontrollidest, mis tugevdavad teie projekti turvalisust.

Need on mõned kõige levinumad põhjused, miks inimesed valivad pilveteenuste kasutamise. Nüüd, kui meil on parem arusaam sellest, mis on pilv ja millised on selle peamised eelised, vaatame lähemalt andmeteadlaste ja arendajate tööd, kes töötavad andmetega, ning kuidas pilv saab aidata neil lahendada mitmeid väljakutseid:

* Suurte andmemahtude salvestamine: selle asemel, et osta, hallata ja kaitsta suuri servereid, saate oma andmeid otse pilves salvestada, kasutades lahendusi nagu Azure Cosmos DB, Azure SQL Database ja Azure Data Lake Storage.
* Andmete integreerimine: andmete integreerimine on andmeteaduse oluline osa, mis võimaldab teil liikuda andmete kogumisest tegevuste tegemiseni. Pilves pakutavate andmete integreerimise teenustega saate koguda, teisendada ja integreerida andmeid erinevatest allikatest ühte andmelattu, kasutades Data Factoryt.
* Andmete töötlemine: suurte andmemahtude töötlemine nõuab palju arvutusvõimsust ja mitte kõigil pole juurdepääsu piisavalt võimsatele masinatele, mistõttu paljud inimesed otsustavad kasutada pilve suurt arvutusvõimsust oma lahenduste käitamiseks ja juurutamiseks.
* Andmeanalüütika teenuste kasutamine: pilveteenused nagu Azure Synapse Analytics, Azure Stream Analytics ja Azure Databricks aitavad teil muuta oma andmed praktilisteks teadmisteks.
* Masinõppe ja andmeteaduse teenuste kasutamine: selle asemel, et alustada nullist, saate kasutada pilveteenuse pakkuja pakutavaid masinõppe algoritme, näiteks AzureML. Samuti saate kasutada kognitiivseid teenuseid, nagu kõne tekstiks, tekst kõneks, arvutinägemine ja palju muud.

## Näited andmeteadusest pilves

Teeme selle konkreetsemaks, vaadates mõningaid stsenaariume.

### Reaalajas sotsiaalmeedia sentimentide analüüs
Alustame stsenaariumiga, mida sageli uurivad inimesed, kes alustavad masinõppega: reaalajas sotsiaalmeedia sentimentide analüüs.

Oletame, et haldate uudiste veebisaiti ja soovite kasutada reaalajas andmeid, et mõista, milline sisu võiks teie lugejatele huvi pakkuda. Selleks saate luua programmi, mis analüüsib reaalajas Twitteri postituste sentimenti teemadel, mis on teie lugejatele olulised.

Peamised näitajad, mida te jälgite, on konkreetsete teemade (hashtagide) kohta tehtud säutsude maht ja sentiment, mis määratakse analüütikavahendite abil, mis teostavad sentimentide analüüsi määratud teemade ümber.

Selle projekti loomiseks vajalikud sammud on järgmised:

* Looge sündmuste keskus voogesituse sisendi jaoks, mis kogub andmeid Twitterist.
* Konfigureerige ja käivitage Twitteri kliendirakendus, mis kutsub Twitteri voogesituse API-sid.
* Looge voogesituse analüütika töö.
* Määrake töö sisend ja päring.
* Looge väljund ja määrake töö väljund.
* Käivitage töö.

Täieliku protsessi vaatamiseks vaadake [dokumentatsiooni](https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?WT.mc_id=academic-77958-bethanycheum&ocid=AID30411099).

### Teaduslike artiklite analüüs
Vaatame teist näidet projektist, mille on loonud [Dmitry Soshnikov](http://soshnikov.com), üks selle õppekava autoritest.

Dmitry lõi tööriista, mis analüüsib COVID-teemalisi artikleid. Selle projekti ülevaatamisel näete, kuidas saate luua tööriista, mis eraldab teadusartiklitest teadmisi, kogub teadmisi ja aitab teadlastel tõhusalt navigeerida suurtes artiklikogudes.

Vaatame selle projekti erinevaid samme:

* Informatsiooni eraldamine ja eeltöötlemine [Text Analytics for Health](https://docs.microsoft.com/azure/cognitive-services/text-analytics/how-tos/text-analytics-for-health?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) abil.
* [Azure ML](https://azure.microsoft.com/services/machine-learning?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) kasutamine töötlemise paralleelseks teostamiseks.
* Informatsiooni salvestamine ja päringute tegemine [Cosmos DB](https://azure.microsoft.com/services/cosmos-db?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) abil.
* Interaktiivse armatuurlaua loomine andmete uurimiseks ja visualiseerimiseks Power BI abil.

Täieliku protsessi vaatamiseks külastage [Dmitry blogi](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/).

Nagu näete, saame pilveteenuseid mitmel viisil kasutada andmeteaduse teostamiseks.

## Lõppsõna

Allikad:
* https://azure.microsoft.com/overview/what-is-cloud-computing?ocid=AID3041109  
* https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?ocid=AID3041109  
* https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/  

## Järelloengu viktoriin

## [Järelloengu viktoriin](https://ff-quizzes.netlify.app/en/ds/quiz/33)

## Ülesanne

[Turu-uuring](assignment.md)

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.