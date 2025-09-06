<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f8e7cdefa096664ae86f795be571580",
  "translation_date": "2025-09-05T16:00:08+00:00",
  "source_file": "5-Data-Science-In-Cloud/17-Introduction/README.md",
  "language_code": "lt"
}
-->
# Duomenų mokslas debesyje: Įvadas

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/17-DataScience-Cloud.png)|
|:---:|
| Duomenų mokslas debesyje: Įvadas - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

Šioje pamokoje sužinosite pagrindinius debesijos principus, kodėl gali būti naudinga naudoti debesijos paslaugas savo duomenų mokslo projektams vykdyti, ir peržiūrėsime keletą pavyzdžių, kaip duomenų mokslo projektai vykdomi debesyje.

## [Prieš paskaitą: testas](https://ff-quizzes.netlify.app/en/ds/quiz/32)

## Kas yra debesija?

Debesija arba debesų kompiuterija – tai įvairių mokamų pagal poreikį kompiuterinių paslaugų, kurios yra talpinamos infrastruktūroje internete, teikimas. Paslaugos apima tokius sprendimus kaip saugyklos, duomenų bazės, tinklai, programinė įranga, analizė ir intelektualiosios paslaugos.

Paprastai skiriame viešąjį, privatųjį ir hibridinį debesis:

* Viešasis debesis: viešasis debesis priklauso trečiosios šalies debesijos paslaugų teikėjui, kuris savo kompiuterinius išteklius teikia viešai per internetą.
* Privatus debesis: tai debesijos ištekliai, naudojami tik vienos įmonės ar organizacijos, su paslaugomis ir infrastruktūra, palaikoma privačiame tinkle.
* Hibridinis debesis: tai sistema, kuri sujungia viešuosius ir privačius debesis. Vartotojai renkasi vietinį duomenų centrą, tačiau leidžia duomenims ir programoms veikti viename ar keliuose viešuosiuose debesyse.

Dauguma debesijos paslaugų skirstomos į tris kategorijas: infrastruktūra kaip paslauga (IaaS), platforma kaip paslauga (PaaS) ir programinė įranga kaip paslauga (SaaS).

* Infrastruktūra kaip paslauga (IaaS): vartotojai nuomojasi IT infrastruktūrą, tokią kaip serveriai, virtualios mašinos (VM), saugyklos, tinklai, operacinės sistemos.
* Platforma kaip paslauga (PaaS): vartotojai nuomojasi aplinką programų kūrimui, testavimui, pristatymui ir valdymui. Vartotojams nereikia rūpintis serverių, saugyklų, tinklų ir duomenų bazių infrastruktūros nustatymu ar valdymu.
* Programinė įranga kaip paslauga (SaaS): vartotojai gauna prieigą prie programinės įrangos per internetą pagal poreikį, dažniausiai prenumeratos pagrindu. Vartotojams nereikia rūpintis programinės įrangos talpinimu, valdymu, infrastruktūra ar priežiūra, pvz., atnaujinimais ir saugumo pataisomis.

Didžiausi debesijos paslaugų teikėjai yra Amazon Web Services, Google Cloud Platform ir Microsoft Azure.

## Kodėl rinktis debesiją duomenų mokslui?

Kūrėjai ir IT specialistai renkasi debesiją dėl daugelio priežasčių, įskaitant šias:

* Inovacijos: galite integruoti debesijos teikėjų sukurtas inovatyvias paslaugas tiesiai į savo programas.
* Lankstumas: mokate tik už tas paslaugas, kurių jums reikia, ir galite rinktis iš plataus paslaugų spektro. Paprastai mokate pagal naudojimą ir pritaikote paslaugas pagal savo poreikius.
* Biudžetas: nereikia pradinių investicijų įrangai ir programinei įrangai įsigyti, vietiniams duomenų centrams įrengti ir valdyti – mokate tik už tai, ką naudojate.
* Skalavimas: jūsų ištekliai gali būti pritaikyti pagal projekto poreikius, o tai reiškia, kad jūsų programos gali naudoti daugiau ar mažiau skaičiavimo galios, saugyklos ir pralaidumo, prisitaikydamos prie išorinių veiksnių bet kuriuo metu.
* Produktyvumas: galite sutelkti dėmesį į savo verslą, o ne gaišti laiką užduotims, kurias gali atlikti kiti, pvz., duomenų centrų valdymui.
* Patikimumas: debesija siūlo įvairius būdus nuolat kurti duomenų atsargines kopijas ir galite nustatyti atkūrimo po nelaimių planus, kad jūsų verslas ir paslaugos veiktų net krizės metu.
* Saugumas: galite pasinaudoti politikomis, technologijomis ir kontrolės priemonėmis, kurios sustiprina jūsų projekto saugumą.

Tai yra keletas dažniausiai minimų priežasčių, kodėl žmonės renkasi debesijos paslaugas. Dabar, kai geriau suprantame, kas yra debesija ir kokie jos pagrindiniai privalumai, pažvelkime konkrečiau į duomenų mokslininkų ir kūrėjų, dirbančių su duomenimis, darbus ir kaip debesija gali padėti spręsti įvairius iššūkius:

* Didelių duomenų saugojimas: vietoj to, kad pirktumėte, valdytumėte ir apsaugotumėte didelius serverius, galite saugoti savo duomenis tiesiogiai debesyje, naudodami tokius sprendimus kaip Azure Cosmos DB, Azure SQL Database ir Azure Data Lake Storage.
* Duomenų integracija: duomenų integracija yra esminė duomenų mokslo dalis, leidžianti pereiti nuo duomenų rinkimo prie veiksmų. Naudodamiesi debesijos siūlomomis duomenų integracijos paslaugomis, galite rinkti, transformuoti ir integruoti duomenis iš įvairių šaltinių į vieną duomenų saugyklą, naudodami Data Factory.
* Duomenų apdorojimas: didelių duomenų apdorojimas reikalauja daug skaičiavimo galios, o ne visi turi prieigą prie pakankamai galingų mašinų, todėl daugelis renkasi tiesiogiai naudotis debesijos didžiule skaičiavimo galia savo sprendimams vykdyti ir diegti.
* Duomenų analizės paslaugos: debesijos paslaugos, tokios kaip Azure Synapse Analytics, Azure Stream Analytics ir Azure Databricks, padeda paversti jūsų duomenis į veiksmingas įžvalgas.
* Mašininis mokymasis ir duomenų intelekto paslaugos: vietoj to, kad pradėtumėte nuo nulio, galite naudoti debesijos teikėjo siūlomus mašininio mokymosi algoritmus, pvz., AzureML. Taip pat galite naudotis kognityvinėmis paslaugomis, tokiomis kaip kalbos atpažinimas, teksto į kalbą konvertavimas, kompiuterinė rega ir kt.

## Duomenų mokslas debesyje: pavyzdžiai

Pažvelkime į keletą scenarijų, kad tai būtų aiškiau.

### Socialinių tinklų nuotaikų analizė realiuoju laiku

Pradėkime nuo scenarijaus, kurį dažnai nagrinėja pradedantieji mašininio mokymosi srityje: socialinių tinklų nuotaikų analizė realiuoju laiku.

Tarkime, jūs valdote naujienų svetainę ir norite naudoti tiesioginius duomenis, kad suprastumėte, kokiu turiniu jūsų skaitytojai galėtų būti suinteresuoti. Norėdami tai sužinoti, galite sukurti programą, kuri atlieka realaus laiko nuotaikų analizę iš „Twitter“ publikacijų, susijusių su jūsų skaitytojams aktualiomis temomis.

Pagrindiniai rodikliai, kuriuos stebėsite, yra tviterių apimtis tam tikromis temomis (žymomis) ir nuotaikos, kurios nustatomos naudojant analizės įrankius, atliekančius nuotaikų analizę pagal nurodytas temas.

Šio projekto kūrimo žingsniai yra šie:

* Sukurti įvykių centrą duomenų srautui rinkti, kuris rinks duomenis iš „Twitter“.
* Suaktyvinti ir paleisti „Twitter“ kliento programą, kuri naudos „Twitter“ srautų API.
* Sukurti srautų analizės užduotį.
* Nustatyti užduoties įvestį ir užklausą.
* Sukurti išvesties saugyklą ir nurodyti užduoties išvestį.
* Paleisti užduotį.

Visą procesą galite peržiūrėti [dokumentacijoje](https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?WT.mc_id=academic-77958-bethanycheum&ocid=AID30411099).

### Mokslinių straipsnių analizė

Pažvelkime į kitą projektą, kurį sukūrė [Dmitrijus Sošnikovas](http://soshnikov.com), vienas iš šios mokymo programos autorių.

Dmitrijus sukūrė įrankį, kuris analizuoja COVID straipsnius. Peržiūrėję šį projektą, pamatysite, kaip galite sukurti įrankį, kuris išgauna žinias iš mokslinių straipsnių, gauna įžvalgas ir padeda tyrėjams efektyviai naršyti per dideles straipsnių kolekcijas.

Štai kokie žingsniai buvo naudojami:

* Informacijos išgavimas ir išankstinis apdorojimas naudojant [Text Analytics for Health](https://docs.microsoft.com/azure/cognitive-services/text-analytics/how-tos/text-analytics-for-health?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).
* Naudojant [Azure ML](https://azure.microsoft.com/services/machine-learning?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) apdorojimo procesų lygiagretinimui.
* Informacijos saugojimas ir užklausų vykdymas naudojant [Cosmos DB](https://azure.microsoft.com/services/cosmos-db?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).
* Interaktyvios duomenų tyrimo ir vizualizacijos ataskaitų srities kūrimas naudojant Power BI.

Visą procesą galite peržiūrėti [Dmitrijaus tinklaraštyje](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/).

Kaip matote, debesijos paslaugos gali būti naudojamos įvairiais būdais duomenų mokslui vykdyti.

## Pastabos

Šaltiniai:
* https://azure.microsoft.com/overview/what-is-cloud-computing?ocid=AID3041109  
* https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?ocid=AID3041109  
* https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/  

## Po paskaitos: testas

## [Po paskaitos: testas](https://ff-quizzes.netlify.app/en/ds/quiz/33)

## Užduotis

[Rinkos tyrimas](assignment.md)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.