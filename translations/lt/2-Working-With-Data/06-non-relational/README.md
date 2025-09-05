<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c182e87f9f80be7e7cdffc7b40bbfccf",
  "translation_date": "2025-09-05T16:02:26+00:00",
  "source_file": "2-Working-With-Data/06-non-relational/README.md",
  "language_code": "lt"
}
-->
# Darbas su duomenimis: Nerelaciniai duomenys

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/06-NoSQL.png)|
|:---:|
|Darbas su NoSQL duomenimis - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

## [Prieš paskaitą: testas](https://ff-quizzes.netlify.app/en/ds/quiz/10)

Duomenys nėra apriboti relacinėmis duomenų bazėmis. Ši pamoka skirta nerelaciniams duomenims ir apims pagrindus apie skaičiuokles bei NoSQL.

## Skaičiuoklės

Skaičiuoklės yra populiarus būdas saugoti ir analizuoti duomenis, nes jų naudojimas reikalauja mažiau pastangų pradiniam nustatymui. Šioje pamokoje sužinosite pagrindinius skaičiuoklės komponentus, taip pat formules ir funkcijas. Pavyzdžiai bus iliustruoti naudojant Microsoft Excel, tačiau dauguma dalių ir temų turės panašius pavadinimus ir veiksmus, palyginti su kitomis skaičiuoklių programomis.

![Tuščias Microsoft Excel darbaknygės langas su dviem darbalapiais](../../../../2-Working-With-Data/06-non-relational/images/parts-of-spreadsheet.png)

Skaičiuoklė yra failas, kurį galima pasiekti kompiuterio, įrenginio ar debesų failų sistemoje. Programinė įranga gali būti naršyklės pagrindu arba programa, kurią reikia įdiegti kompiuteryje ar atsisiųsti kaip programėlę. Excel failai taip pat vadinami **darbaknygėmis**, ir ši terminologija bus naudojama visoje pamokoje.

Darbaknygė sudaryta iš vieno ar daugiau **darbalapių**, kurių kiekvienas pažymėtas skirtukais. Darbalapyje yra stačiakampiai, vadinami **langeliais**, kuriuose saugomi faktiniai duomenys. Langelis yra eilutės ir stulpelio sankirta, kur stulpeliai pažymėti abėcėliniais simboliais, o eilutės - skaitmenimis. Kai kurios skaičiuoklės pirmose eilutėse turi antraštes, kurios apibūdina duomenis langelyje.

Naudodami šiuos pagrindinius Excel darbaknygės elementus, pasitelksime pavyzdį iš [Microsoft Templates](https://templates.office.com/), susijusį su inventoriaus valdymu, kad aptartume papildomas skaičiuoklės dalis.

### Inventoriaus valdymas

Skaičiuoklės failas, pavadintas "InventoryExample", yra suformatuota inventoriaus elementų skaičiuoklė, kurioje yra trys darbalapiai, pažymėti skirtukais "Inventory List", "Inventory Pick List" ir "Bin Lookup". 4-oji eilutė darbalapyje "Inventory List" yra antraštė, apibūdinanti kiekvieno langelio reikšmę antraštės stulpelyje.

![Paryškinta formulė iš inventoriaus sąrašo pavyzdžio Microsoft Excel](../../../../2-Working-With-Data/06-non-relational/images/formula-excel.png)

Yra atvejų, kai langelio reikšmė priklauso nuo kitų langelių reikšmių, kad būtų sugeneruota jo reikšmė. Inventoriaus sąrašo skaičiuoklė seka kiekvieno inventoriaus elemento kainą, tačiau ką daryti, jei reikia sužinoti viso inventoriaus vertę? [**Formulės**](https://support.microsoft.com/en-us/office/overview-of-formulas-34519a4e-1e8d-4f4b-84d4-d642c4f63263) atlieka veiksmus su langelių duomenimis ir naudojamos inventoriaus vertės apskaičiavimui šiame pavyzdyje. Ši skaičiuoklė naudoja formulę stulpelyje "Inventory Value", kad apskaičiuotų kiekvieno elemento vertę, padauginant kiekį iš stulpelio "QTY" ir kainą iš stulpelio "COST". Dukart spustelėjus arba paryškinus langelį, bus matoma formulė. Pastebėsite, kad formulės prasideda lygybės ženklu, po kurio seka skaičiavimas ar operacija.

![Paryškinta funkcija iš inventoriaus sąrašo pavyzdžio Microsoft Excel](../../../../2-Working-With-Data/06-non-relational/images/function-excel.png)

Galime naudoti kitą formulę, kad sudėtume visas inventoriaus vertės reikšmes ir gautume bendrą vertę. Tai galėtų būti apskaičiuota sudedant kiekvieną langelį, tačiau tai gali būti varginantis darbas. Excel turi [**funkcijas**](https://support.microsoft.com/en-us/office/sum-function-043e1c7d-7726-4e80-8f32-07b23e057f89), arba iš anksto apibrėžtas formules, skirtas skaičiavimams su langelių reikšmėmis. Funkcijoms reikalingi argumentai, kurie yra būtinos reikšmės skaičiavimams atlikti. Kai funkcijoms reikia daugiau nei vieno argumento, jie turi būti išvardyti tam tikra tvarka, kitaip funkcija gali neteisingai apskaičiuoti reikšmę. Šiame pavyzdyje naudojama funkcija SUM, kuri naudoja inventoriaus vertės reikšmes kaip argumentą, kad sugeneruotų bendrą vertę, nurodytą 3-oje eilutėje, B stulpelyje (taip pat vadinama B3).

## NoSQL

NoSQL yra bendras terminas, apibūdinantis skirtingus būdus saugoti nerelacinius duomenis, ir gali būti interpretuojamas kaip "ne-SQL", "nerelacinis" arba "ne tik SQL". Šios duomenų bazės sistemos gali būti suskirstytos į 4 tipus.

![Grafinis vaizdas, rodantis raktų-reikšmių duomenų saugyklą su 4 unikalių skaitinių raktų, susietų su 4 skirtingomis reikšmėmis](../../../../2-Working-With-Data/06-non-relational/images/kv-db.png)
> Šaltinis: [Michał Białecki Blog](https://www.michalbialecki.com/2018/03/18/azure-cosmos-db-key-value-database-cloud/)

[Raktų-reikšmių](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#keyvalue-data-stores) duomenų bazės susieja unikalius raktus, kurie yra unikalūs identifikatoriai, susieti su reikšme. Šios poros saugomos naudojant [maišos lentelę](https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/tutorial/) su tinkama maišos funkcija.

![Grafinis vaizdas, rodantis grafų duomenų saugyklą, kurioje pavaizduoti žmonių, jų interesų ir vietų ryšiai](../../../../2-Working-With-Data/06-non-relational/images/graph-db.png)
> Šaltinis: [Microsoft](https://docs.microsoft.com/en-us/azure/cosmos-db/graph/graph-introduction#graph-database-by-example)

[Grafų](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#graph-data-stores) duomenų bazės aprašo ryšius tarp duomenų ir yra vaizduojamos kaip mazgų ir briaunų kolekcija. Mazgas atspindi objektą, egzistuojantį realiame pasaulyje, pvz., studentą ar banko išrašą. Briaunos atspindi ryšį tarp dviejų objektų. Kiekvienas mazgas ir briauna turi savybes, kurios suteikia papildomos informacijos apie mazgus ir briaunas.

![Grafinis vaizdas, rodantis stulpelinę duomenų saugyklą su klientų duomenų baze, kurioje yra dvi stulpelių šeimos, pavadintos "Identity" ir "Contact Info"](../../../../2-Working-With-Data/06-non-relational/images/columnar-db.png)

[Stulpelinės](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#columnar-data-stores) duomenų saugyklos organizuoja duomenis į stulpelius ir eilutes, panašiai kaip relacinė duomenų struktūra, tačiau kiekvienas stulpelis yra suskirstytas į grupes, vadinamas stulpelių šeimomis, kur visi duomenys po vienu stulpeliu yra susiję ir gali būti gauti ar pakeisti kaip vienetas.

### Dokumentų duomenų saugyklos su Azure Cosmos DB

[Dokumentų](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#document-data-stores) duomenų saugyklos remiasi raktų-reikšmių duomenų saugyklos koncepcija ir sudarytos iš laukų ir objektų kolekcijos. Šiame skyriuje bus nagrinėjamos dokumentų duomenų bazės naudojant Cosmos DB emuliatorių.

Cosmos DB duomenų bazė atitinka "ne tik SQL" apibrėžimą, kur Cosmos DB dokumentų duomenų bazė naudoja SQL duomenų užklausoms. [Ankstesnė pamoka](../05-relational-databases/README.md) apie SQL apima kalbos pagrindus, ir galėsime pritaikyti kai kurias tas pačias užklausas dokumentų duomenų bazėje čia. Naudosime Cosmos DB emuliatorių, kuris leidžia sukurti ir tyrinėti dokumentų duomenų bazę vietiniame kompiuteryje. Daugiau apie emuliatorių skaitykite [čia](https://docs.microsoft.com/en-us/azure/cosmos-db/local-emulator?tabs=ssl-netstd21).

Dokumentas yra laukų ir objektų reikšmių kolekcija, kur laukai apibūdina, ką objektų reikšmė atspindi. Žemiau pateiktas dokumento pavyzdys.

```json
{
    "firstname": "Eva",
    "age": 44,
    "id": "8c74a315-aebf-4a16-bb38-2430a9896ce5",
    "_rid": "bHwDAPQz8s0BAAAAAAAAAA==",
    "_self": "dbs/bHwDAA==/colls/bHwDAPQz8s0=/docs/bHwDAPQz8s0BAAAAAAAAAA==/",
    "_etag": "\"00000000-0000-0000-9f95-010a691e01d7\"",
    "_attachments": "attachments/",
    "_ts": 1630544034
}
```

Šiame dokumente svarbūs laukai yra: `firstname`, `id` ir `age`. Likę laukai su pabraukimais buvo sugeneruoti Cosmos DB.

#### Duomenų tyrinėjimas su Cosmos DB emuliatoriumi

Emuliatorių galite atsisiųsti ir įdiegti [Windows sistemai čia](https://aka.ms/cosmosdb-emulator). Žr. šią [dokumentaciją](https://docs.microsoft.com/en-us/azure/cosmos-db/local-emulator?tabs=ssl-netstd21#run-on-linux-macos) dėl galimybių paleisti emuliatorių macOS ir Linux sistemose.

Emuliatorius atidaro naršyklės langą, kuriame Explorer vaizdas leidžia tyrinėti dokumentus.

![Cosmos DB emuliatoriaus Explorer vaizdas](../../../../2-Working-With-Data/06-non-relational/images/cosmosdb-emulator-explorer.png)

Jei sekate pamoką, spustelėkite "Start with Sample", kad sugeneruotumėte pavyzdinę duomenų bazę, pavadintą SampleDB. Jei išplėsite SampleDB spustelėdami rodyklę, rasite konteinerį, pavadintą `Persons`. Konteineris saugo elementų kolekciją, kurie yra dokumentai konteineryje. Galite tyrinėti keturis atskirus dokumentus po `Items`.

![Pavyzdinių duomenų tyrinėjimas Cosmos DB emuliatoriuje](../../../../2-Working-With-Data/06-non-relational/images/cosmosdb-emulator-persons.png)

#### Dokumentų duomenų užklausos su Cosmos DB emuliatoriumi

Taip pat galime užklausti pavyzdinius duomenis spustelėdami naujos SQL užklausos mygtuką (antras mygtukas iš kairės).

`SELECT * FROM c` grąžina visus dokumentus konteineryje. Pridėkime sąlygą "where" ir suraskime visus, jaunesnius nei 40 metų.

`SELECT * FROM c where c.age < 40`

![SQL užklausos vykdymas pavyzdiniuose duomenyse Cosmos DB emuliatoriuje, siekiant rasti dokumentus, kurių amžiaus lauko reikšmė mažesnė nei 40](../../../../2-Working-With-Data/06-non-relational/images/cosmosdb-emulator-persons-query.png)

Užklausa grąžina du dokumentus, pastebėkite, kad kiekvieno dokumento amžiaus reikšmė yra mažesnė nei 40.

#### JSON ir dokumentai

Jei esate susipažinę su JavaScript Object Notation (JSON), pastebėsite, kad dokumentai atrodo panašūs į JSON. Šiame kataloge yra `PersonsData.json` failas su daugiau duomenų, kuriuos galite įkelti į `Persons` konteinerį emuliatoriuje per `Upload Item` mygtuką.

Daugeliu atvejų API, kurios grąžina JSON duomenis, gali būti tiesiogiai perduotos ir saugomos dokumentų duomenų bazėse. Žemiau pateiktas dar vienas dokumentas, jis atspindi "Microsoft" Twitter paskyros tviterius, kurie buvo gauti naudojant Twitter API, o vėliau įkelti į Cosmos DB.

```json
{
    "created_at": "2021-08-31T19:03:01.000Z",
    "id": "1432780985872142341",
    "text": "Blank slate. Like this tweet if you’ve ever painted in Microsoft Paint before. https://t.co/cFeEs8eOPK",
    "_rid": "dhAmAIUsA4oHAAAAAAAAAA==",
    "_self": "dbs/dhAmAA==/colls/dhAmAIUsA4o=/docs/dhAmAIUsA4oHAAAAAAAAAA==/",
    "_etag": "\"00000000-0000-0000-9f84-a0958ad901d7\"",
    "_attachments": "attachments/",
    "_ts": 1630537000
```

Šiame dokumente svarbūs laukai yra: `created_at`, `id` ir `text`.

## 🚀 Iššūkis

Yra `TwitterData.json` failas, kurį galite įkelti į SampleDB duomenų bazę. Rekomenduojama jį pridėti į atskirą konteinerį. Tai galima padaryti:

1. Spustelėjus naujo konteinerio mygtuką viršutiniame dešiniajame kampe
1. Pasirinkus esamą duomenų bazę (SampleDB), sukuriant konteinerio ID
1. Nustatant skaidymo raktą į `/id`
1. Spustelėjus OK (galite ignoruoti likusią informaciją šiame vaizde, nes tai yra mažas duomenų rinkinys, veikiantis vietiniame kompiuteryje)
1. Atidarykite naują konteinerį ir įkelkite Twitter Data failą per `Upload Item` mygtuką

Pabandykite atlikti kelias užklausas, kad rastumėte dokumentus, kuriuose lauke "text" yra "Microsoft". Užuomina: pabandykite naudoti [LIKE raktinį žodį](https://docs.microsoft.com/en-us/azure/cosmos-db/sql/sql-query-keywords#using-like-with-the--wildcard-character).

## [Po paskaitos: testas](https://ff-quizzes.netlify.app/en/ds/quiz/11)

## Apžvalga ir savarankiškas mokymasis

- Yra papildomų formatavimo ir funkcijų, pridėtų prie šios skaičiuoklės, kurių ši pamoka neapima. Microsoft turi [didelę dokumentacijos ir vaizdo įrašų biblioteką](https://support.microsoft.com/excel) apie Excel, jei norite sužinoti daugiau.

- Ši architektūrinė dokumentacija aprašo skirtingų nerelacinių duomenų tipų savybes: [Nerelaciniai duomenys ir NoSQL](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data)

- Cosmos DB yra debesų pagrindu veikianti nerelacinė duomenų bazė, kuri taip pat gali saugoti skirtingus NoSQL tipus, paminėtus šioje pamokoje. Sužinokite daugiau apie šiuos tipus šiame [Cosmos DB Microsoft Learn Module](https://docs.microsoft.com/en-us/learn/paths/work-with-nosql-data-in-azure-cosmos-db/)

## Užduotis

[Soda Profits](assignment.md)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius naudojant šį vertimą.