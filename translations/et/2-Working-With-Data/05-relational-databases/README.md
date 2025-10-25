<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "80d80300002ef4e77cc7631d5904bd6e",
  "translation_date": "2025-10-25T19:15:46+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/README.md",
  "language_code": "et"
}
-->
# Andmetega töötamine: relatsioonilised andmebaasid

|![ Sketchnote autorilt [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/05-RelationalData.png)|
|:---:|
| Andmetega töötamine: relatsioonilised andmebaasid - _Sketchnote autorilt [@nitya](https://twitter.com/nitya)_ |

Tõenäoliselt olete varem kasutanud arvutustabelit teabe salvestamiseks. Teil oli ridade ja veergude komplekt, kus read sisaldasid teavet (või andmeid) ja veerud kirjeldasid teavet (mõnikord nimetatakse seda metaandmeteks). Relatsiooniline andmebaas põhineb sellel põhimõttel, kus tabelites on veerud ja read, mis võimaldavad teil teavet jaotada mitme tabeli vahel. See võimaldab teil töötada keerukamate andmetega, vältida dubleerimist ja olla paindlikum andmete uurimisel. Vaatame lähemalt relatsioonilise andmebaasi kontseptsioone.

## [Loengu-eelne viktoriin](https://ff-quizzes.netlify.app/en/ds/quiz/8)

## Kõik algab tabelitest

Relatsioonilise andmebaasi keskmes on tabelid. Nii nagu arvutustabelis, on tabel ridade ja veergude kogum. Rida sisaldab andmeid või teavet, millega soovime töötada, näiteks linna nimi või sademete hulk. Veerud kirjeldavad salvestatavaid andmeid.

Alustame uurimist, luues tabeli, kuhu salvestame teavet linnade kohta. Võime alustada nende nimede ja riikidega. Seda saab salvestada tabelisse järgmiselt:

| Linn     | Riik          |
| -------- | ------------- |
| Tokyo    | Jaapan        |
| Atlanta  | Ameerika Ühendriigid |
| Auckland | Uus-Meremaa   |

Pange tähele, et veerunimed **linn**, **riik** ja **rahvaarv** kirjeldavad salvestatavaid andmeid ning iga rida sisaldab teavet ühe linna kohta.

## Ühe tabeli lähenemise puudused

Tõenäoliselt tundub ülaltoodud tabel teile üsna tuttav. Lisame oma kasvavasse andmebaasi täiendavaid andmeid - aastased sademed (millimeetrites). Keskendume aastatele 2018, 2019 ja 2020. Kui lisaksime need Tokyo kohta, võiks see välja näha umbes selline:

| Linn  | Riik    | Aasta | Kogus  |
| ----- | ------- | ----- | ------ |
| Tokyo | Jaapan  | 2020  | 1690   |
| Tokyo | Jaapan  | 2019  | 1874   |
| Tokyo | Jaapan  | 2018  | 1445   |

Mida te meie tabeli juures märkate? Võite märgata, et kordame linna nime ja riiki ikka ja jälle. See võib võtta üsna palju salvestusruumi ja on suuresti tarbetu, kuna Tokyo on ainult üks nimi, mis meid huvitab.

Olgu, proovime midagi muud. Lisame uued veerud iga aasta kohta:

| Linn     | Riik          | 2018 | 2019 | 2020 |
| -------- | ------------- | ---- | ---- | ---- |
| Tokyo    | Jaapan        | 1445 | 1874 | 1690 |
| Atlanta  | Ameerika Ühendriigid | 1779 | 1111 | 1683 |
| Auckland | Uus-Meremaa   | 1386 | 942  | 1176 |

Kuigi see väldib ridade dubleerimist, tekitab see paar muud väljakutset. Me peaksime muutma oma tabeli struktuuri iga kord, kui lisandub uus aasta. Lisaks, kui meie andmed kasvavad, muudab aastate lisamine veergudeks väärtuste leidmise ja arvutamise keerulisemaks.

Seetõttu vajame mitut tabelit ja seoseid. Jagades andmed mitmeks tabeliks, saame vältida dubleerimist ja olla paindlikumad andmetega töötamisel.

## Seoste kontseptsioonid

Vaatame uuesti oma andmeid ja määrame, kuidas me tahame need jagada. Me teame, et tahame salvestada linnade nimed ja riigid, seega sobib see ilmselt kõige paremini ühte tabelisse.

| Linn     | Riik          |
| -------- | ------------- |
| Tokyo    | Jaapan        |
| Atlanta  | Ameerika Ühendriigid |
| Auckland | Uus-Meremaa   |

Enne järgmise tabeli loomist peame välja mõtlema, kuidas iga linna viidata. Vajame mingisugust identifikaatorit, ID-d või (tehnilises andmebaasi terminoloogias) primaarvõtit. Primaarvõti on väärtus, mida kasutatakse konkreetse rea tuvastamiseks tabelis. Kuigi see võiks põhineda väärtusel endal (näiteks võiksime kasutada linna nime), peaks see peaaegu alati olema number või muu identifikaator. Me ei taha, et ID kunagi muutuks, kuna see rikuks seose. Enamasti on primaarvõti või ID automaatselt genereeritud number.

> ✅ Primaarvõtit lühendatakse sageli kui PK

### linnad

| linn_id | Linn     | Riik          |
| ------- | -------- | ------------- |
| 1       | Tokyo    | Jaapan        |
| 2       | Atlanta  | Ameerika Ühendriigid |
| 3       | Auckland | Uus-Meremaa   |

> ✅ Märkate, et kasutame mõisteid "id" ja "primaarvõti" vaheldumisi selle õppetunni jooksul. Need kontseptsioonid kehtivad ka DataFrame'ide puhul, mida uurite hiljem. Kuigi DataFrame'id ei kasuta "primaarvõti" terminoloogiat, käituvad nad enamasti samamoodi.

Kui meie linnade tabel on loodud, salvestame sademete andmed. Selle asemel, et linna täielikku teavet dubleerida, saame kasutada ID-d. Samuti peaksime tagama, et äsja loodud tabelil oleks *id*-veerg, kuna kõigil tabelitel peaks olema ID või primaarvõti.

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

Pange tähele **linn_id** veergu äsja loodud **sademed** tabelis. See veerg sisaldab väärtusi, mis viitavad **linnad** tabeli ID-dele. Tehnilises relatsiooniliste andmete terminoloogias nimetatakse seda **võõrvõtmeks**; see on teise tabeli primaarvõti. Võite seda lihtsalt mõelda kui viidet või osutit. **linn_id** 1 viitab Tokyole.

> [!NOTE] 
> Võõrvõtit lühendatakse sageli kui FK

## Andmete päring

Kui meie andmed on jagatud kaheks tabeliks, võite mõelda, kuidas me neid pärime. Kui kasutame relatsioonilist andmebaasi, nagu MySQL, SQL Server või Oracle, saame kasutada keelt nimega Structured Query Language ehk SQL. SQL (mõnikord hääldatakse "sequel") on standardne keel, mida kasutatakse relatsioonilises andmebaasis andmete pärimiseks ja muutmiseks.

Andmete pärimiseks kasutatakse käsku `SELECT`. Põhimõtteliselt **valite** veerud, mida soovite näha, ja **FROM** määrab tabeli, milles need asuvad. Kui soovite kuvada ainult linnade nimed, võite kasutada järgmist:

```sql
SELECT city
FROM cities;

-- Output:
-- Tokyo
-- Atlanta
-- Auckland
```

`SELECT` on koht, kus loetlete veerud, ja `FROM` on koht, kus loetlete tabelid.

> [!NOTE] 
> SQL-i süntaks ei ole tõstutundlik, mis tähendab, et `select` ja `SELECT` tähendavad sama asja. Kuid sõltuvalt kasutatavast andmebaasi tüübist võivad veerud ja tabelid olla tõstutundlikud. Seetõttu on parim tava alati käsitleda kõike programmeerimises nagu see oleks tõstutundlik. SQL-päringute kirjutamisel on tavaks kirjutada märksõnad suurte tähtedega.

Ülaltoodud päring kuvab kõik linnad. Kujutame ette, et tahame kuvada ainult Uus-Meremaa linnad. Vajame mingisugust filtrit. SQL-i märksõna selleks on `WHERE`, ehk "kus midagi on tõene".

```sql
SELECT city
FROM cities
WHERE country = 'New Zealand';

-- Output:
-- Auckland
```

## Andmete ühendamine

Siiani oleme pärinud andmeid ühest tabelist. Nüüd tahame tuua andmed kokku nii **linnad** kui ka **sademed** tabelist. Seda tehakse nende *ühendamise* teel. Sisuliselt loote kahe tabeli vahel seose ja sobitate veeru väärtused mõlemast tabelist.

Meie näites sobitame **linn_id** veeru **sademed** tabelis **linn_id** veeruga **linnad** tabelis. See sobitab sademete väärtuse vastava linnaga. Tüüp ühendust, mida me teeme, on nn *sisemine* ühendus, mis tähendab, et kui mõni rida ei sobi teise tabeli ühegi rea väärtusega, siis seda ei kuvata. Meie puhul on igal linnal sademete andmed, seega kuvatakse kõik.

Vaatame 2019. aasta sademete andmeid kõigi meie linnade kohta.

Teeme seda sammudena. Esimene samm on andmete ühendamine, näidates veerud, mille kaudu seos luuakse - **linn_id**, nagu varem esile tõstetud.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
```

Oleme esile tõstnud kaks veergu, mida soovime, ja fakti, et tahame tabelid ühendada **linn_id** kaudu. Nüüd saame lisada `WHERE` lause, et filtreerida ainult 2019. aasta.

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

Relatsioonilised andmebaasid keskenduvad teabe jagamisele mitme tabeli vahel, mis seejärel tuuakse tagasi kokku kuvamiseks ja analüüsimiseks. See pakub suurt paindlikkust arvutuste tegemiseks ja muul viisil andmete töötlemiseks. Olete näinud relatsioonilise andmebaasi põhikontseptsioone ja kuidas teha ühendust kahe tabeli vahel.

## 🚀 Väljakutse

Internetis on saadaval arvukalt relatsioonilisi andmebaase. Saate andmeid uurida, kasutades ülaltoodud oskusi.

## Loengu-järgne viktoriin

## [Loengu-järgne viktoriin](https://ff-quizzes.netlify.app/en/ds/quiz/9)

## Ülevaade ja iseseisev õppimine

Microsoft Learnis on saadaval mitmeid ressursse, et jätkata SQL-i ja relatsiooniliste andmebaaside kontseptsioonide uurimist

- [Relatsiooniliste andmete kontseptsioonide kirjeldamine](https://docs.microsoft.com//learn/modules/describe-concepts-of-relational-data?WT.mc_id=academic-77958-bethanycheum)
- [Alustamine päringutega Transact-SQL-is](https://docs.microsoft.com//learn/paths/get-started-querying-with-transact-sql?WT.mc_id=academic-77958-bethanycheum) (Transact-SQL on SQL-i versioon)
- [SQL-i sisu Microsoft Learnis](https://docs.microsoft.com/learn/browse/?products=azure-sql-database%2Csql-server&expanded=azure&WT.mc_id=academic-77958-bethanycheum)

## Ülesanne

[Ülesande pealkiri](assignment.md)

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta arusaamatuste või valesti tõlgenduste eest, mis võivad tekkida selle tõlke kasutamise tõttu.