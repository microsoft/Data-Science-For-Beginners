<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "54c5a1c74aecb69d2f9099300a4b7eea",
  "translation_date": "2025-09-05T05:56:26+00:00",
  "source_file": "2-Working-With-Data/06-non-relational/README.md",
  "language_code": "sl"
}
-->
# Delo s podatki: Nerelacijski podatki

|![ Sketchnote avtorja [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/06-NoSQL.png)|
|:---:|
|Delo z NoSQL podatki - _Sketchnote avtorja [@nitya](https://twitter.com/nitya)_ |

## [Predavanje: Kviz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/10)

Podatki niso omejeni le na relacijske baze podatkov. Ta lekcija se osredotoča na nerelacijske podatke in zajema osnove preglednic ter NoSQL.

## Preglednice

Preglednice so priljubljen način za shranjevanje in raziskovanje podatkov, saj zahtevajo manj priprave za začetek dela. V tej lekciji boste spoznali osnovne komponente preglednice, formule in funkcije. Primeri bodo prikazani z Microsoft Excelom, vendar bodo večina delov in tem imeli podobna imena in korake tudi v drugih programih za preglednice.

![Prazna Microsoft Excel delovna knjiga z dvema delovnima listoma](../../../../2-Working-With-Data/06-non-relational/images/parts-of-spreadsheet.png)

Preglednica je datoteka, ki je dostopna v datotečnem sistemu računalnika, naprave ali oblaka. Programska oprema je lahko brskalniška ali aplikacija, ki jo je treba namestiti na računalnik ali prenesti kot aplikacijo. V Excelu so te datoteke definirane kot **delovne knjige**, in ta terminologija bo uporabljena v preostanku te lekcije.

Delovna knjiga vsebuje enega ali več **delovnih listov**, ki so označeni z zavihki. Znotraj delovnega lista so pravokotniki, imenovani **celice**, ki vsebujejo dejanske podatke. Celica je presečišče vrstice in stolpca, kjer so stolpci označeni z abecednimi znaki, vrstice pa številčno. Nekatere preglednice vsebujejo glave v prvih nekaj vrsticah, ki opisujejo podatke v celici.

Z uporabo teh osnovnih elementov Excelove delovne knjige bomo uporabili primer iz [Microsoft Templates](https://templates.office.com/), osredotočen na inventar, da bomo preučili dodatne dele preglednice.

### Upravljanje inventarja

Datoteka preglednice z imenom "InventoryExample" je oblikovana preglednica predmetov v inventarju, ki vsebuje tri delovne liste, kjer so zavihki označeni kot "Inventory List", "Inventory Pick List" in "Bin Lookup". Vrstica 4 na delovnem listu Inventory List je glava, ki opisuje vrednost vsake celice v stolpcu glave.

![Označena formula iz primernega seznama inventarja v Microsoft Excelu](../../../../2-Working-With-Data/06-non-relational/images/formula-excel.png)

Obstajajo primeri, kjer je vrednost celice odvisna od vrednosti drugih celic. Preglednica Inventory List spremlja stroške vsakega predmeta v inventarju, kaj pa, če želimo vedeti vrednost celotnega inventarja? [**Formule**](https://support.microsoft.com/en-us/office/overview-of-formulas-34519a4e-1e8d-4f4b-84d4-d642c4f63263) izvajajo operacije na podatkih v celicah in se uporabljajo za izračun vrednosti inventarja v tem primeru. Ta preglednica uporablja formulo v stolpcu Inventory Value za izračun vrednosti vsakega predmeta tako, da pomnoži količino pod glavo QTY in stroške pod glavo COST. Dvoklik ali označitev celice prikaže formulo. Opazili boste, da formule začnejo z znakom za enačbo, ki mu sledi izračun ali operacija.

![Označena funkcija iz primernega seznama inventarja v Microsoft Excelu](../../../../2-Working-With-Data/06-non-relational/images/function-excel.png)

Za seštevanje vseh vrednosti stolpca Inventory Value lahko uporabimo drugo formulo. To bi lahko izračunali z dodajanjem vsake celice posebej, vendar je to lahko zamudno. Excel ima [**funkcije**](https://support.microsoft.com/en-us/office/sum-function-043e1c7d-7726-4e80-8f32-07b23e057f89), ali vnaprej določene formule za izvajanje izračunov na vrednostih celic. Funkcije zahtevajo argumente, kar so potrebne vrednosti za izvedbo teh izračunov. Če funkcije zahtevajo več kot en argument, jih je treba navesti v določenem vrstnem redu, sicer funkcija morda ne bo pravilno izračunala vrednosti. Ta primer uporablja funkcijo SUM in uporablja vrednosti stolpca Inventory Value kot argument za izračun skupne vrednosti, navedene v vrstici 3, stolpec B (imenovan tudi B3).

## NoSQL

NoSQL je splošen izraz za različne načine shranjevanja nerelacijskih podatkov in ga lahko interpretiramo kot "non-SQL", "nerelacijski" ali "ne samo SQL". Te vrste podatkovnih sistemov lahko razvrstimo v 4 tipe.

![Grafični prikaz shrambe podatkov ključ-vrednost, ki prikazuje 4 unikatne numerične ključe, povezane z različnimi vrednostmi](../../../../2-Working-With-Data/06-non-relational/images/kv-db.png)
> Vir: [Michał Białecki Blog](https://www.michalbialecki.com/2018/03/18/azure-cosmos-db-key-value-database-cloud/)

[Podatkovne baze ključ-vrednost](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#keyvalue-data-stores) povezujejo unikatne ključe, ki so unikatni identifikatorji, z vrednostmi. Ti pari so shranjeni z uporabo [hash tabele](https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/tutorial/) z ustrezno hash funkcijo.

![Grafični prikaz grafične shrambe podatkov, ki prikazuje odnose med ljudmi, njihovimi interesi in lokacijami](../../../../2-Working-With-Data/06-non-relational/images/graph-db.png)
> Vir: [Microsoft](https://docs.microsoft.com/en-us/azure/cosmos-db/graph/graph-introduction#graph-database-by-example)

[Grafične](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#graph-data-stores) podatkovne baze opisujejo odnose med podatki in so predstavljene kot zbirka vozlišč in povezav. Vozlišče predstavlja entiteto, nekaj, kar obstaja v resničnem svetu, kot je študent ali bančni izpisek. Povezave predstavljajo odnose med dvema entitetama. Vsako vozlišče in povezava imata lastnosti, ki zagotavljajo dodatne informacije o vozliščih in povezavah.

![Grafični prikaz stolpčne shrambe podatkov, ki prikazuje bazo podatkov strank z dvema družinama stolpcev, imenovanima Identity in Contact Info](../../../../2-Working-With-Data/06-non-relational/images/columnar-db.png)

[Stolpčne](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#columnar-data-stores) shrambe podatkov organizirajo podatke v stolpce in vrstice, podobno kot relacijska struktura podatkov, vendar je vsak stolpec razdeljen v skupine, imenovane družine stolpcev, kjer so vsi podatki pod enim stolpcem povezani in jih je mogoče pridobiti in spremeniti kot eno enoto.

### Dokumentne shrambe podatkov z Azure Cosmos DB

[Dokumentne](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#document-data-stores) shrambe podatkov temeljijo na konceptu shrambe ključ-vrednost in so sestavljene iz serije polj in objektov. Ta razdelek bo raziskal dokumentne baze podatkov z emulatorjem Cosmos DB.

Cosmos DB baza podatkov ustreza definiciji "Ne samo SQL", kjer dokumentna baza podatkov Cosmos DB uporablja SQL za poizvedovanje podatkov. [Prejšnja lekcija](../05-relational-databases/README.md) o SQL zajema osnove jezika, in nekatere poizvedbe bomo lahko uporabili tudi tukaj. Uporabili bomo emulator Cosmos DB, ki omogoča ustvarjanje in raziskovanje dokumentne baze podatkov lokalno na računalniku. Več o emulatorju preberite [tukaj](https://docs.microsoft.com/en-us/azure/cosmos-db/local-emulator?tabs=ssl-netstd21).

Dokument je zbirka polj in vrednosti objektov, kjer polja opisujejo, kaj vrednost objekta predstavlja. Spodaj je primer dokumenta.

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

Polja, ki nas zanimajo v tem dokumentu, so: `firstname`, `id` in `age`. Ostala polja z podčrtaji so bila ustvarjena s strani Cosmos DB.

#### Raziskovanje podatkov z emulatorjem Cosmos DB

Emulator lahko prenesete in namestite [za Windows tukaj](https://aka.ms/cosmosdb-emulator). Za možnosti uporabe emulatorja na macOS in Linuxu si oglejte to [dokumentacijo](https://docs.microsoft.com/en-us/azure/cosmos-db/local-emulator?tabs=ssl-netstd21#run-on-linux-macos).

Emulator odpre okno brskalnika, kjer pogled Explorer omogoča raziskovanje dokumentov.

![Pogled Explorer v emulatorju Cosmos DB](../../../../2-Working-With-Data/06-non-relational/images/cosmosdb-emulator-explorer.png)

Če sledite navodilom, kliknite "Start with Sample", da ustvarite vzorčno bazo podatkov z imenom SampleDB. Če razširite SampleDB s klikom na puščico, boste našli zbirko z imenom `Persons`. Zbirka vsebuje zbirko elementov, ki so dokumenti znotraj zbirke. Raziskujete lahko štiri posamezne dokumente pod `Items`.

![Raziskovanje vzorčnih podatkov v emulatorju Cosmos DB](../../../../2-Working-With-Data/06-non-relational/images/cosmosdb-emulator-persons.png)

#### Poizvedovanje dokumentnih podatkov z emulatorjem Cosmos DB

Vzorčne podatke lahko poizvedujete s klikom na gumb za novo SQL poizvedbo (drugi gumb z leve).

`SELECT * FROM c` vrne vse dokumente v zbirki. Dodajmo stavek WHERE in poiščimo vse, ki so mlajši od 40 let.

`SELECT * FROM c where c.age < 40`

![Izvajanje poizvedbe SELECT na vzorčnih podatkih v emulatorju Cosmos DB za iskanje dokumentov, kjer je vrednost polja age manjša od 40](../../../../2-Working-With-Data/06-non-relational/images/cosmosdb-emulator-persons-query.png)

Poizvedba vrne dva dokumenta, opazite, da je vrednost polja age za vsak dokument manjša od 40.

#### JSON in dokumenti

Če poznate JavaScript Object Notation (JSON), boste opazili, da so dokumenti podobni JSON-u. V tej mapi je datoteka `PersonsData.json` z več podatki, ki jih lahko naložite v zbirko Persons v emulatorju prek gumba `Upload Item`.

V večini primerov lahko API-ji, ki vračajo JSON podatke, neposredno prenesejo in shranijo podatke v dokumentne baze podatkov. Spodaj je še en dokument, ki predstavlja tvite z Microsoftovega Twitter računa, pridobljene z uporabo Twitter API-ja in nato vstavljene v Cosmos DB.

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

Polja, ki nas zanimajo v tem dokumentu, so: `created_at`, `id` in `text`.

## 🚀 Izziv

V tej mapi je datoteka `TwitterData.json`, ki jo lahko naložite v bazo podatkov SampleDB. Priporočljivo je, da jo dodate v ločeno zbirko. To lahko storite tako:

1. Kliknite gumb za novo zbirko v zgornjem desnem kotu.
2. Izberite obstoječo bazo podatkov (SampleDB) in ustvarite ID zbirke za zbirko.
3. Nastavite ključ particije na `/id`.
4. Kliknite OK (preostale informacije v tem pogledu lahko ignorirate, saj gre za majhen nabor podatkov, ki se izvaja lokalno na vašem računalniku).
5. Odprite novo zbirko in naložite datoteko Twitter Data z gumbom `Upload Item`.

Poskusite izvesti nekaj poizvedb SELECT, da poiščete dokumente, ki vsebujejo besedo Microsoft v polju text. Namig: poskusite uporabiti [ključ LIKE](https://docs.microsoft.com/en-us/azure/cosmos-db/sql/sql-query-keywords#using-like-with-the--wildcard-character).

## [Kviz po predavanju](https://ff-quizzes.netlify.app/en/ds/)

## Pregled in samostojno učenje

- Obstajajo dodatne možnosti oblikovanja in funkcije, dodane tej preglednici, ki jih ta lekcija ne zajema. Microsoft ima [obsežno knjižnico dokumentacije in videoposnetkov](https://support.microsoft.com/excel) o Excelu, če vas zanima več.

- Ta arhitekturna dokumentacija podrobno opisuje značilnosti različnih vrst nerelacijskih podatkov: [Nerelacijski podatki in NoSQL](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data).

- Cosmos DB je oblačna nerelacijska baza podatkov, ki lahko shranjuje tudi različne vrste NoSQL, omenjene v tej lekciji. Več o teh vrstah si preberite v tem [modulu Microsoft Learn za Cosmos DB](https://docs.microsoft.com/en-us/learn/paths/work-with-nosql-data-in-azure-cosmos-db/).

## Naloga

[Soda Profits](assignment.md)

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki bi nastale zaradi uporabe tega prevoda.