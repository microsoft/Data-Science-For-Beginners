<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "408c55cab2880daa4e78616308bd5db7",
  "translation_date": "2025-08-31T05:36:04+00:00",
  "source_file": "5-Data-Science-In-Cloud/17-Introduction/README.md",
  "language_code": "lt"
}
-->
# Įvadas į duomenų mokslą debesyje

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/17-DataScience-Cloud.png)|
|:---:|
| Duomenų mokslas debesyje: Įvadas - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

Šioje pamokoje sužinosite pagrindinius debesų kompiuterijos principus, kodėl verta naudoti debesų paslaugas savo duomenų mokslo projektams vykdyti, ir peržiūrėsime keletą pavyzdžių, kaip duomenų mokslas vykdomas debesyje.

## [Prieš paskaitą: testas](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/32)

## Kas yra debesis?

Debesis, arba debesų kompiuterija, yra įvairių mokamų pagal poreikį kompiuterinių paslaugų teikimas, kurios yra talpinamos infrastruktūroje internete. Paslaugos apima sprendimus, tokius kaip saugyklos, duomenų bazės, tinklai, programinė įranga, analizė ir intelektualios paslaugos.

Paprastai skiriame viešąjį, privatųjį ir hibridinį debesį:

* Viešasis debesis: viešasis debesis priklauso ir yra valdomas trečiosios šalies debesų paslaugų teikėjo, kuris teikia savo kompiuterinius išteklius internetu visuomenei.
* Privatus debesis: tai debesų kompiuterijos ištekliai, naudojami tik vienos įmonės ar organizacijos, su paslaugomis ir infrastruktūra, palaikoma privačiame tinkle.
* Hibridinis debesis: hibridinis debesis yra sistema, kuri sujungia viešuosius ir privačiuosius debesis. Vartotojai pasirenka vietinį duomenų centrą, tuo pačiu leidžiant duomenims ir programoms veikti viename ar keliuose viešuosiuose debesyse.

Dauguma debesų kompiuterijos paslaugų skirstomos į tris kategorijas: infrastruktūra kaip paslauga (IaaS), platforma kaip paslauga (PaaS) ir programinė įranga kaip paslauga (SaaS).

* Infrastruktūra kaip paslauga (IaaS): vartotojai nuomojasi IT infrastruktūrą, tokią kaip serveriai, virtualios mašinos (VM), saugyklos, tinklai, operacinės sistemos.
* Platforma kaip paslauga (PaaS): vartotojai nuomojasi aplinką programinės įrangos kūrimui, testavimui, pristatymui ir valdymui. Vartotojams nereikia rūpintis serverių, saugyklų, tinklų ir duomenų bazių infrastruktūros nustatymu ar valdymu.
* Programinė įranga kaip paslauga (SaaS): vartotojai gauna prieigą prie programinės įrangos internetu pagal poreikį, dažniausiai prenumeratos pagrindu. Vartotojams nereikia rūpintis programinės įrangos talpinimu, valdymu, infrastruktūra ar priežiūra, pvz., programinės įrangos atnaujinimais ir saugumo pataisomis.

Kai kurie didžiausi debesų paslaugų teikėjai yra Amazon Web Services, Google Cloud Platform ir Microsoft Azure.

## Kodėl verta rinktis debesį duomenų mokslui?

Kūrėjai ir IT specialistai renkasi darbą su debesimi dėl daugelio priežasčių, įskaitant šias:

* Inovacijos: galite integruoti inovatyvias paslaugas, sukurtas debesų teikėjų, tiesiai į savo programas.
* Lankstumas: mokate tik už tas paslaugas, kurių jums reikia, ir galite rinktis iš daugybės paslaugų. Paprastai mokate pagal poreikį ir pritaikote paslaugas pagal savo besikeičiančius poreikius.
* Biudžetas: nereikia investuoti į pradinį aparatūros ir programinės įrangos pirkimą, vietinių duomenų centrų nustatymą ir valdymą – mokate tik už tai, ką naudojate.
* Skalavimas: jūsų ištekliai gali būti pritaikyti pagal projekto poreikius, tai reiškia, kad jūsų programos gali naudoti daugiau ar mažiau kompiuterinės galios, saugyklos ir pralaidumo, prisitaikydamos prie išorinių veiksnių bet kuriuo metu.
* Produktyvumas: galite susitelkti į savo verslą, užuot skyrę laiką užduotims, kurias gali valdyti kiti, pvz., duomenų centrų valdymui.
* Patikimumas: debesų kompiuterija siūlo kelis būdus nuolat kurti duomenų atsargines kopijas ir galite nustatyti atkūrimo po nelaimių planus, kad jūsų verslas ir paslaugos veiktų net krizės metu.
* Saugumas: galite pasinaudoti politikomis, technologijomis ir kontrolėmis, kurios stiprina jūsų projekto saugumą.

Tai yra keletas dažniausiai pasitaikančių priežasčių, kodėl žmonės renkasi debesų paslaugas. Dabar, kai geriau suprantame, kas yra debesis ir kokie jo pagrindiniai privalumai, pažvelkime konkrečiau į duomenų mokslininkų ir kūrėjų, dirbančių su duomenimis, darbus ir kaip debesis gali padėti jiems spręsti įvairius iššūkius:

* Didelių duomenų saugojimas: vietoj to, kad pirktumėte, valdytumėte ir apsaugotumėte didelius serverius, galite saugoti savo duomenis tiesiogiai debesyje, naudodami tokius sprendimus kaip Azure Cosmos DB, Azure SQL Database ir Azure Data Lake Storage.
* Duomenų integravimas: duomenų integravimas yra esminė duomenų mokslo dalis, leidžianti pereiti nuo duomenų rinkimo prie veiksmų atlikimo. Naudodami debesyje siūlomas duomenų integravimo paslaugas, galite rinkti, transformuoti ir integruoti duomenis iš įvairių šaltinių į vieną duomenų saugyklą, naudodami Data Factory.
* Duomenų apdorojimas: didelių duomenų apdorojimas reikalauja daug kompiuterinės galios, ir ne visi turi prieigą prie pakankamai galingų mašinų, todėl daugelis žmonių renkasi tiesiogiai naudoti debesies didžiulę kompiuterinę galią savo sprendimams vykdyti ir diegti.
* Duomenų analizės paslaugų naudojimas: debesų paslaugos, tokios kaip Azure Synapse Analytics, Azure Stream Analytics ir Azure Databricks, padeda paversti jūsų duomenis į veiksmingas įžvalgas.
* Mašininio mokymosi ir duomenų intelekto paslaugų naudojimas: vietoj to, kad pradėtumėte nuo nulio, galite naudoti debesų teikėjo siūlomus mašininio mokymosi algoritmus, su paslaugomis, tokiomis kaip AzureML. Taip pat galite naudoti kognityvines paslaugas, tokias kaip kalbos į tekstą, tekstas į kalbą, kompiuterinė vizija ir daugiau.

## Duomenų mokslas debesyje: pavyzdžiai

Padarykime tai konkretesniu, pažvelgdami į keletą scenarijų.

### Socialinių tinklų nuotaikų analizė realiu laiku

Pradėsime nuo scenarijaus, dažnai nagrinėjamo pradedantiesiems mašininio mokymosi srityje: socialinių tinklų nuotaikų analizė realiu laiku.

Tarkime, jūs valdote naujienų svetainę ir norite pasinaudoti tiesioginiais duomenimis, kad suprastumėte, kokiu turiniu jūsų skaitytojai galėtų būti suinteresuoti. Norėdami sužinoti daugiau apie tai, galite sukurti programą, kuri atlieka realaus laiko nuotaikų analizę iš „Twitter“ publikacijų, susijusių su jūsų skaitytojams aktualiomis temomis.

Pagrindiniai rodikliai, kuriuos stebėsite, yra „Twitter“ žinučių kiekis tam tikromis temomis (hashtag'ais) ir nuotaikos, kurios nustatomos naudojant analizės įrankius, atliekančius nuotaikų analizę apie nurodytas temas.

Šio projekto kūrimo žingsniai yra šie:

* Sukurkite įvykių centrą srauto įvestims, kuris rinks duomenis iš „Twitter“.
* Konfigūruokite ir paleiskite „Twitter“ klientų programą, kuri naudos „Twitter Streaming“ API.
* Sukurkite srauto analizės užduotį.
* Nurodykite užduoties įvestį ir užklausą.
* Sukurkite išvesties saugyklą ir nurodykite užduoties išvestį.
* Paleiskite užduotį.

Norėdami peržiūrėti visą procesą, apsilankykite [dokumentacijoje](https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?WT.mc_id=academic-77958-bethanycheum&ocid=AID30411099).

### Mokslinių straipsnių analizė

Pažvelkime į kitą projekto pavyzdį, sukurtą [Dmitrijaus Sošnikovo](http://soshnikov.com), vieno iš šios mokymo programos autorių.

Dmitrijus sukūrė įrankį, kuris analizuoja COVID straipsnius. Peržiūrėdami šį projektą, pamatysite, kaip galite sukurti įrankį, kuris išgauna žinias iš mokslinių straipsnių, gauna įžvalgas ir padeda tyrėjams efektyviai naršyti per dideles straipsnių kolekcijas.

Pažiūrėkime, kokie žingsniai buvo naudojami:

* Informacijos išgavimas ir išankstinis apdorojimas naudojant [Text Analytics for Health](https://docs.microsoft.com/azure/cognitive-services/text-analytics/how-tos/text-analytics-for-health?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).
* Naudojant [Azure ML](https://azure.microsoft.com/services/machine-learning?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) apdorojimo paralelizavimui.
* Informacijos saugojimas ir užklausų vykdymas naudojant [Cosmos DB](https://azure.microsoft.com/services/cosmos-db?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).
* Interaktyvios duomenų tyrimo ir vizualizacijos ataskaitų kūrimas naudojant Power BI.

Norėdami peržiūrėti visą procesą, apsilankykite [Dmitrijaus tinklaraštyje](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/).

Kaip matote, debesų paslaugas galima panaudoti įvairiais būdais duomenų mokslui vykdyti.

## Pastabos

Šaltiniai:
* https://azure.microsoft.com/overview/what-is-cloud-computing?ocid=AID3041109  
* https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?ocid=AID3041109  
* https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/  

## Po paskaitos: testas

[Po paskaitos: testas](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/33)

## Užduotis

[Rinkos tyrimas](assignment.md)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, atkreipkite dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus aiškinimus, kylančius dėl šio vertimo naudojimo.