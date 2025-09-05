<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c182e87f9f80be7e7cdffc7b40bbfccf",
  "translation_date": "2025-09-05T19:34:05+00:00",
  "source_file": "2-Working-With-Data/06-non-relational/README.md",
  "language_code": "sl"
}
-->
# Delo z podatki: Nerelacijski podatki

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/06-NoSQL.png)|
|:---:|
|Delo z NoSQL podatki - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

## [Predhodni kviz](https://ff-quizzes.netlify.app/en/ds/quiz/10)

Podatki niso omejeni le na relacijske baze podatkov. Ta lekcija se osredotoča na nerelacijske podatke in bo zajela osnove preglednic ter NoSQL.

## Preglednice

Preglednice so priljubljen način shranjevanja in raziskovanja podatkov, saj zahtevajo manj dela za nastavitev in začetek uporabe. V tej lekciji boste spoznali osnovne komponente preglednice, kot tudi formule in funkcije. Primeri bodo prikazani z Microsoft Excelom, vendar bodo večina delov in tem imeli podobna imena ter korake v primerjavi z drugo programsko opremo za preglednice.

![Prazna delovna knjiga Microsoft Excel z dvema delovnima listoma](../../../../2-Working-With-Data/06-non-relational/images/parts-of-spreadsheet.png)

Preglednica je datoteka, ki bo dostopna v datotečnem sistemu računalnika, naprave ali v datotečnem sistemu v oblaku. Sama programska oprema je lahko brskalniška ali aplikacija, ki jo je treba namestiti na računalnik ali prenesti kot aplikacijo. V Excelu so te datoteke opredeljene kot **delovne knjige**, in ta terminologija bo uporabljena v preostanku te lekcije.

Delovna knjiga vsebuje enega ali več **delovnih listov**, kjer so posamezni delovni listi označeni z zavihki. Znotraj delovnega lista so pravokotniki, imenovani **celice**, ki vsebujejo dejanske podatke. Celica je presečišče vrstice in stolpca, kjer so stolpci označeni z abecednimi znaki, vrstice pa številčno. Nekatere preglednice bodo imele glave v prvih nekaj vrsticah, ki opisujejo podatke v celici.

Z osnovnimi elementi Excelove delovne knjige bomo uporabili primer iz [Microsoft Templates](https://templates.office.com/), osredotočen na inventar, da preučimo dodatne dele preglednice.

### Upravljanje inventarja

Datoteka preglednice z imenom "InventoryExample" je oblikovana preglednica predmetov v inventarju, ki vsebuje tri delovne liste, kjer so zavihki označeni kot "Inventory List", "Inventory Pick List" in "Bin Lookup". Vrstica 4 delovnega lista Inventory List je glava, ki opisuje vrednost vsake celice v stolpcu glave.

![Označena formula iz primernega inventarnega seznama v Microsoft Excelu](../../../../2-Working-With-Data/06-non-relational/images/formula-excel.png)

Obstajajo primeri, kjer je celica odvisna od vrednosti drugih celic za generiranje svoje vrednosti. Preglednica Inventory List spremlja stroške vsakega predmeta v inventarju, kaj pa, če potrebujemo vrednost celotnega inventarja? [**Formule**](https://support.microsoft.com/en-us/office/overview-of-formulas-34519a4e-1e8d-4f4b-84d4-d642c4f63263) izvajajo dejanja na podatkih v celicah in se uporabljajo za izračun stroškov inventarja v tem primeru. Ta preglednica uporablja formulo v stolpcu Inventory Value za izračun vrednosti vsakega predmeta z množenjem količine pod glavo QTY in stroškov pod glavo COST. Dvoklik ali označitev celice bo prikazala formulo. Opazili boste, da formule začnejo z znakom enakosti, ki mu sledi izračun ali operacija.

![Označena funkcija iz primernega inventarnega seznama v Microsoft Excelu](../../../../2-Working-With-Data/06-non-relational/images/function-excel.png)

Za izračun skupne vrednosti inventarja lahko uporabimo drugo formulo. To bi lahko izračunali z dodajanjem vsake celice, da dobimo vsoto, vendar je to lahko zamudno opravilo. Excel ima [**funkcije**](https://support.microsoft.com/en-us/office/sum-function-043e1c7d-7726-4e80-8f32-07b23e057f89), ali vnaprej določene formule za izvajanje izračunov na vrednostih celic. Funkcije zahtevajo argumente, ki so potrebne vrednosti za izvedbo teh izračunov. Ko funkcije zahtevajo več kot en argument, jih je treba navesti v določenem vrstnem redu, sicer funkcija morda ne bo izračunala pravilne vrednosti. Ta primer uporablja funkcijo SUM in uporablja vrednosti v stolpcu Inventory Value kot argument za generiranje skupne vrednosti, navedene pod vrstico 3, stolpec B (imenovan tudi B3).

## NoSQL

NoSQL je krovni izraz za različne načine shranjevanja nerelacijskih podatkov in ga je mogoče interpretirati kot "ne-SQL", "nerelacijski" ali "ne samo SQL". Te vrste podatkovnih sistemov lahko razvrstimo v 4 tipe.

![Grafični prikaz podatkovne shrambe ključ-vrednost, ki prikazuje 4 edinstvene numerične ključe, povezane s 4 različnimi vrednostmi](../../../../2-Working-With-Data/06-non-relational/images/kv-db.png)
> Vir: [Michał Białecki Blog](https://www.michalbialecki.com/2018/03/18/azure-cosmos-db-key-value-database-cloud/)

[Ključ-vrednost](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#keyvalue-data-stores) baze podatkov povezujejo unikatne ključe, ki so edinstveni identifikatorji, povezani z vrednostjo. Ti pari so shranjeni z uporabo [hash tabele](https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/tutorial/) z ustrezno hash funkcijo.

![Grafični prikaz grafične podatkovne shrambe, ki prikazuje odnose med ljudmi, njihovimi interesi in lokacijami](../../../../2-Working-With-Data/06-non-relational/images/graph-db.png)
> Vir: [Microsoft](https://docs.microsoft.com/en-us/azure/cosmos-db/graph/graph-introduction#graph-database-by-example)

[Graf](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#graph-data-stores) baze podatkov opisujejo odnose v podatkih in so predstavljene kot zbirka vozlišč in povezav. Vozlišče predstavlja entiteto, nekaj, kar obstaja v resničnem svetu, kot je študent ali bančni izpisek. Povezave predstavljajo odnos med dvema entitetama. Vsako vozlišče in povezava imata lastnosti, ki zagotavljajo dodatne informacije o vozliščih in povezavah.

![Grafični prikaz stolpčne podatkovne shrambe, ki prikazuje bazo podatkov strank z dvema družinama stolpcev, imenovanima Identity in Contact Info](../../../../2-Working-With-Data/06-non-relational/images/columnar-db.png)

[Stolpčne](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#columnar-data-stores) podatkovne shrambe organizirajo podatke v stolpce in vrstice, podobno kot relacijska podatkovna struktura, vendar je vsak stolpec razdeljen v skupine, imenovane družina stolpcev, kjer so vsi podatki pod enim stolpcem povezani in jih je mogoče pridobiti ter spremeniti kot eno enoto.

### Dokumentne podatkovne shrambe z Azure Cosmos DB

[Dokumentne](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#document-data-stores) podatkovne shrambe temeljijo na konceptu shrambe ključ-vrednost in so sestavljene iz serije polj in objektov. Ta razdelek bo raziskal dokumentne baze podatkov z emulatorjem Cosmos DB.

Baza podatkov Cosmos DB ustreza definiciji "ne samo SQL", kjer dokumentna baza podatkov Cosmos DB uporablja SQL za poizvedovanje podatkov. [Prejšnja lekcija](../05-relational-databases/README.md) o SQL zajema osnove jezika, in nekatere poizvedbe bomo lahko uporabili tudi v dokumentni bazi podatkov tukaj. Uporabili bomo emulator Cosmos DB, ki nam omogoča ustvarjanje in raziskovanje dokumentne baze podatkov lokalno na računalniku. Več o emulatorju preberite [tukaj](https://docs.microsoft.com/en-us/azure/cosmos-db/local-emulator?tabs=ssl-netstd21).

Dokument je zbirka polj in objektnih vrednosti, kjer polja opisujejo, kaj objektna vrednost predstavlja. Spodaj je primer dokumenta.

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

Polja, ki nas zanimajo v tem dokumentu, so: `firstname`, `id` in `age`. Ostala polja z podčrtaji so bila generirana s Cosmos DB.

#### Raziskovanje podatkov z emulatorjem Cosmos DB

Emulator lahko prenesete in namestite [za Windows tukaj](https://aka.ms/cosmosdb-emulator). Za možnosti, kako zagnati emulator na macOS in Linux, si oglejte to [dokumentacijo](https://docs.microsoft.com/en-us/azure/cosmos-db/local-emulator?tabs=ssl-netstd21#run-on-linux-macos).

Emulator odpre okno brskalnika, kjer pogled Explorer omogoča raziskovanje dokumentov.

![Pogled Explorer v emulatorju Cosmos DB](../../../../2-Working-With-Data/06-non-relational/images/cosmosdb-emulator-explorer.png)

Če sledite navodilom, kliknite "Start with Sample", da ustvarite vzorčno bazo podatkov z imenom SampleDB. Če razširite SampleDB s klikom na puščico, boste našli vsebnik z imenom `Persons`. Vsebnik vsebuje zbirko predmetov, ki so dokumenti znotraj vsebnika. Raziskujete lahko štiri posamezne dokumente pod `Items`.

![Raziskovanje vzorčnih podatkov v emulatorju Cosmos DB](../../../../2-Working-With-Data/06-non-relational/images/cosmosdb-emulator-persons.png)

#### Poizvedovanje dokumentnih podatkov z emulatorjem Cosmos DB

Vzorčne podatke lahko poizvedujemo tudi s klikom na gumb za novo SQL poizvedbo (drugi gumb z leve).

`SELECT * FROM c` vrne vse dokumente v vsebniku. Dodajmo stavek where in poiščimo vse, ki so mlajši od 40 let.

`SELECT * FROM c where c.age < 40`

![Izvajanje poizvedbe SELECT na vzorčnih podatkih v emulatorju Cosmos DB za iskanje dokumentov, ki imajo vrednost polja age manjšo od 40](../../../../2-Working-With-Data/06-non-relational/images/cosmosdb-emulator-persons-query.png)

Poizvedba vrne dva dokumenta, opazite, da je vrednost age za vsak dokument manjša od 40.

#### JSON in dokumenti

Če poznate JavaScript Object Notation (JSON), boste opazili, da dokumenti izgledajo podobno kot JSON. V tej mapi je datoteka `PersonsData.json` z več podatki, ki jih lahko naložite v vsebnik Persons v emulatorju prek gumba `Upload Item`.

V večini primerov lahko API-ji, ki vračajo JSON podatke, neposredno prenesejo in shranijo podatke v dokumentne baze podatkov. Spodaj je še en dokument, ki predstavlja tvite z Microsoftovega Twitter računa, pridobljene z uporabo Twitter API-ja, nato pa vstavljene v Cosmos DB.

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

Obstaja datoteka `TwitterData.json`, ki jo lahko naložite v bazo podatkov SampleDB. Priporočljivo je, da jo dodate v ločen vsebnik. To lahko storite tako:

1. Kliknite gumb za nov vsebnik v zgornjem desnem kotu
1. Izberite obstoječo bazo podatkov (SampleDB) in ustvarite ID za vsebnik
1. Nastavite ključ particije na `/id`
1. Kliknite OK (preostale informacije v tem pogledu lahko ignorirate, saj gre za majhen nabor podatkov, ki se izvaja lokalno na vašem računalniku)
1. Odprite nov vsebnik in naložite datoteko Twitter Data prek gumba `Upload Item`

Poskusite izvesti nekaj poizvedb SELECT za iskanje dokumentov, ki imajo v polju text besedo Microsoft. Namig: poskusite uporabiti [ključno besedo LIKE](https://docs.microsoft.com/en-us/azure/cosmos-db/sql/sql-query-keywords#using-like-with-the--wildcard-character).

## [Kviz po predavanju](https://ff-quizzes.netlify.app/en/ds/quiz/11)

## Pregled in samostojno učenje

- Obstajajo dodatne oblike in funkcije, dodane tej preglednici, ki jih ta lekcija ne pokriva. Microsoft ima [veliko knjižnico dokumentacije in videoposnetkov](https://support.microsoft.com/excel) o Excelu, če vas zanima več.

- Ta arhitekturna dokumentacija podrobno opisuje značilnosti različnih vrst nerelacijskih podatkov: [Nerelacijski podatki in NoSQL](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data)

- Cosmos DB je podatkovna baza v oblaku, ki lahko shranjuje tudi različne tipe NoSQL, omenjene v tej lekciji. Več o teh tipih si preberite v tem [učnem modulu Cosmos DB Microsoft Learn](https://docs.microsoft.com/en-us/learn/paths/work-with-nosql-data-in-azure-cosmos-db/).

## Naloga

[Soda Profits](assignment.md)

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna napačna razumevanja ali napačne interpretacije, ki bi nastale zaradi uporabe tega prevoda.