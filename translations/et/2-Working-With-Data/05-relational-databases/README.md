<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9399d7b4767e75068f95ce5c660b285c",
  "translation_date": "2025-10-11T15:24:19+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/README.md",
  "language_code": "et"
}
-->
# Töötamine andmetega: Relatsioonilised andmebaasid

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/05-RelationalData.png)|
|:---:|
| Töötamine andmetega: Relatsioonilised andmebaasid - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

Tõenäoliselt olete varem kasutanud arvutustabelit teabe salvestamiseks. Teil oli ridade ja veergude komplekt, kus read sisaldasid teavet (või andmeid) ja veerud kirjeldasid teavet (mida mõnikord nimetatakse metaandmeteks). Relatsiooniline andmebaas põhineb sellel põhimõttel, kus tabelites on veerud ja read, võimaldades teil teavet jagada mitme tabeli vahel. See võimaldab teil töötada keerukamate andmetega, vältida dubleerimist ja olla paindlikum andmete uurimisel. Vaatame relatsioonilise andmebaasi põhimõtteid.

## [Eelloengu viktoriin](https://ff-quizzes.netlify.app/en/ds/quiz/8)

## Kõik algab tabelitest

Relatsioonilise andmebaasi keskmes on tabelid. Nagu arvutustabelis, on tabel veergude ja ridade kogum. Rida sisaldab andmeid või teavet, millega soovime töötada, näiteks linna nimi või sademete hulk. Veerud kirjeldavad andmeid, mida nad salvestavad.

Alustame uurimist, luues tabeli, kuhu salvestame teavet linnade kohta. Võime alustada nende nime ja riigiga. Seda võiks salvestada tabelisse järgmiselt:

| Linn     | Riik          |
| -------- | ------------- |
| Tokyo    | Jaapan        |
| Atlanta  | Ameerika Ühendriigid |
| Auckland | Uus-Meremaa   |

Pange tähele, et veerunimed **linn**, **riik** ja **rahvaarv** kirjeldavad salvestatavaid andmeid ning iga rida sisaldab teavet ühe linna kohta.

## Ühe tabeli lähenemise puudused

Tõenäoliselt tundub ülaltoodud tabel teile üsna tuttav. Lisame oma kasvavasse andmebaasi täiendavaid andmeid - aastased sademed (millimeetrites). Keskendume aastatele 2018, 2019 ja 2020. Kui lisaksime need Tokyo kohta, võiks see välja näha järgmiselt:

| Linn  | Riik   | Aasta | Kogus  |
| ----- | ------ | ----- | ------ |
| Tokyo | Jaapan | 2020  | 1690   |
| Tokyo | Jaapan | 2019  | 1874   |
| Tokyo | Jaapan | 2018  | 1445   |

Mida te tabeli juures märkate? Võite märgata, et kordame linna nime ja riiki ikka ja jälle. See võib võtta üsna palju salvestusruumi ja on suuresti tarbetu, kuna Tokyo kohta on meil huvi ainult ühe nime vastu.

Proovime midagi muud. Lisame uued veerud iga aasta kohta:

| Linn     | Riik          | 2018 | 2019 | 2020 |
| -------- | ------------- | ---- | ---- | ---- |
| Tokyo    | Jaapan        | 1445 | 1874 | 1690 |
| Atlanta  | Ameerika Ühendriigid | 1779 | 1111 | 1683 |
| Auckland | Uus-Meremaa   | 1386 | 942  | 1176 |

Kuigi see väldib ridade dubleerimist, tekitab see paar muud väljakutset. Me peaksime tabeli struktuuri muutma iga kord, kui lisandub uus aasta. Lisaks, kui meie andmed kasvavad, muudab aastate veergudena hoidmine väärtuste leidmise ja arvutamise keerulisemaks.

Seetõttu vajame mitut tabelit ja seoseid. Jagades andmed mitmeks tabeliks, saame vältida dubleerimist ja olla paindlikumad andmetega töötamisel.

## Seoste mõisted

Vaatame uuesti oma andmeid ja otsustame, kuidas neid jagada. Teame, et tahame salvestada linnade nimed ja riigid, seega sobib see ilmselt kõige paremini ühte tabelisse.

| Linn     | Riik          |
| -------- | ------------- |
| Tokyo    | Jaapan        |
| Atlanta  | Ameerika Ühendriigid |
| Auckland | Uus-Meremaa   |

Enne järgmise tabeli loomist peame välja mõtlema, kuidas iga linna viidata. Vajame mingisugust identifikaatorit, ID-d või (tehnilises andmebaasi keeles) primaarvõtit. Primaarvõti on väärtus, mida kasutatakse konkreetse rea tuvastamiseks tabelis. Kuigi see võiks põhineda väärtusel endal (näiteks linna nimel), peaks see peaaegu alati olema number või muu identifikaator. Me ei taha, et ID kunagi muutuks, kuna see rikuks seose. Enamasti on primaarvõti või ID automaatselt genereeritud number.

> ✅ Primaarvõtit lühendatakse sageli kui PK

### linnad

| linn_id | Linn     | Riik          |
| ------- | -------- | ------------- |
| 1       | Tokyo    | Jaapan        |
| 2       | Atlanta  | Ameerika Ühendriigid |
| 3       | Auckland | Uus-Meremaa   |

> ✅ Märkate, et kasutame termineid "ID" ja "primaarvõti" vaheldumisi selle õppetunni jooksul. Need mõisted kehtivad ka DataFrame'ide puhul, mida uurite hiljem. Kuigi DataFrame'id ei kasuta terminit "primaarvõti", käituvad nad väga sarnaselt.

Kui meie linnade tabel on loodud, salvestame sademete andmed. Selle asemel, et dubleerida kogu teavet linna kohta, saame kasutada ID-d. Samuti peaksime tagama, et äsja loodud tabelil oleks *ID*-veerg, kuna kõigil tabelitel peaks olema ID või primaarvõti.

### sademed

| sademed_id | linn_id | Aasta | Kogus  |
| ---------- | ------- | ----- | ------ |
| 1          | 1       | 2018  | 1445   |
| 2          | 1       | 2019  | 1874   |
| 3          | 1       | 2020  | 1690   |
| 4          | 2       | 2018  | 1779   |
| 5          | 2       | 2019  | 1111   |
| 6          | 2       | 2020  | 1683   |
| 7          | 3       | 2018  | 1386   |
| 8          | 3       | 2019  | 942    |
| 9          | 3       | 2020  | 1176   |

Pange tähele **linn_id** veergu äsja loodud **sademed** tabelis. See veerg sisaldab väärtusi, mis viitavad **linnad** tabeli ID-dele. Tehnilises relatsiooniliste andmete keeles nimetatakse seda **võõrvõtmeks**; see on primaarvõti teisest tabelist. Võite seda lihtsalt mõelda kui viidet või osutit. **linn_id** 1 viitab Tokyole.

> [!NOTE] Võõrvõtit lühendatakse sageli kui FK

## Andmete pärimine

Kui meie andmed on jagatud kaheks tabeliks, võite mõelda, kuidas neid pärida. Kui kasutame relatsioonilist andmebaasi nagu MySQL, SQL Server või Oracle, saame kasutada keelt nimega Structured Query Language ehk SQL. SQL (mõnikord hääldatakse "sequel") on standardne keel, mida kasutatakse relatsioonilises andmebaasis andmete pärimiseks ja muutmiseks.

Andmete pärimiseks kasutate käsku `SELECT`. Põhimõtteliselt **valite** veerud, mida soovite näha, **tabelist**, kus need asuvad. Kui soovite kuvada ainult linnade nimed, võiksite kasutada järgmist:

```sql
SELECT city
FROM cities;

-- Output:
-- Tokyo
-- Atlanta
-- Auckland
```

`SELECT` on koht, kus loetlete veerud, ja `FROM` on koht, kus loetlete tabelid.

> [NOTE] SQL süntaks ei ole tõstutundlik, mis tähendab, et `select` ja `SELECT` tähendavad sama. Kuid sõltuvalt andmebaasi tüübist võivad veerud ja tabelid olla tõstutundlikud. Seetõttu on parim tava alati käsitleda kõike programmeerimises nagu see oleks tõstutundlik. SQL-päringute kirjutamisel on tavaks kirjutada märksõnad suurte tähtedega.

Ülaltoodud päring kuvab kõik linnad. Kujutame ette, et soovime kuvada ainult Uus-Meremaa linnad. Vajame mingisugust filtrit. SQL märksõna selleks on `WHERE`, ehk "kus midagi on tõene".

```sql
SELECT city
FROM cities
WHERE country = 'New Zealand';

-- Output:
-- Auckland
```

## Andmete ühendamine

Siiani oleme pärinud andmeid ühest tabelist. Nüüd tahame tuua andmed kokku nii **linnad** kui **sademed** tabelist. Seda tehakse nende *ühendamise* teel. Sisuliselt loote kahe tabeli vahel seose ja sobitate veeru väärtused mõlemast tabelist.

Meie näites sobitame **linn_id** veeru **sademed** tabelis **linn_id** veeruga **linnad** tabelis. See sobitab sademete väärtuse vastava linnaga. Ühenduse tüüp, mida me teeme, on nn *sisemine* ühendus, mis tähendab, et kui mõni rida ei sobi teise tabeli ühegi väärtusega, siis neid ei kuvata. Meie puhul on igal linnal sademete andmed, seega kuvatakse kõik.

Vaatame 2019. aasta sademete andmeid kõigi meie linnade kohta.

Teeme seda sammude kaupa. Esimene samm on andmete ühendamine, näidates veerud, mida soovime sobitada - **linn_id**, nagu varem rõhutatud.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
```

Oleme rõhutanud kahte veergu, mida soovime, ja fakti, et tahame tabelid **linn_id** kaudu ühendada. Nüüd saame lisada `WHERE` lause, et filtreerida ainult 2019. aasta.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
WHERE rainfall.year = 2019

-- Output

-- city     | amount
-- -------- | ------
-- Tokyo    | 1874
-- Atlanta  | 1111
-- Auckland |  942
```

## Kokkuvõte

Relatsioonilised andmebaasid keskenduvad teabe jagamisele mitme tabeli vahel, mis seejärel tuuakse tagasi kuvamiseks ja analüüsiks. See pakub suurt paindlikkust arvutuste tegemiseks ja andmete manipuleerimiseks. Olete näinud relatsioonilise andmebaasi põhimõisteid ja kuidas teha ühendust kahe tabeli vahel.

## 🚀 Väljakutse

Internetis on saadaval arvukalt relatsioonilisi andmebaase. Saate andmeid uurida, kasutades ülaltoodud oskusi.

## Järelloengu viktoriin

## [Järelloengu viktoriin](https://ff-quizzes.netlify.app/en/ds/quiz/9)

## Ülevaade ja iseseisev õppimine

Microsoft Learnis on saadaval mitmeid ressursse, et jätkata SQL-i ja relatsiooniliste andmebaaside kontseptsioonide uurimist.

- [Relatsiooniliste andmete kontseptsioonide kirjeldamine](https://docs.microsoft.com//learn/modules/describe-concepts-of-relational-data?WT.mc_id=academic-77958-bethanycheum)
- [Alustamine päringutega Transact-SQL-is](https://docs.microsoft.com//learn/paths/get-started-querying-with-transact-sql?WT.mc_id=academic-77958-bethanycheum) (Transact-SQL on SQL-i versioon)
- [SQL-i sisu Microsoft Learnis](https://docs.microsoft.com/learn/browse/?products=azure-sql-database%2Csql-server&expanded=azure&WT.mc_id=academic-77958-bethanycheum)

## Ülesanne

[Ülesande pealkiri](assignment.md)

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.