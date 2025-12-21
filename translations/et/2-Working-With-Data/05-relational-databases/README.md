<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11739c7b40e7c6b16ad29e3df4e65862",
  "translation_date": "2025-12-19T12:36:42+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/README.md",
  "language_code": "et"
}
-->
# Andmetega töötamine: relatsioonandmebaasid

|![ Sketchnote autorilt [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/05-RelationalData.png)|
|:---:|
| Andmetega töötamine: relatsioonandmebaasid - _Sketchnote autorilt [@nitya](https://twitter.com/nitya)_ |

Tõenäoliselt olete varem kasutanud tabelarvutusprogrammi teabe salvestamiseks. Teil oli ridade ja veergude kogum, kus read sisaldasid teavet (või andmeid) ja veerud kirjeldasid teavet (mõnikord nimetatakse seda metainfoks). Relatsioonandmebaas põhineb sellel põhiprintsiibil – veerud ja read tabelites, võimaldades teil hoida teavet mitmes tabelis. See võimaldab teil töötada keerukamate andmetega, vältida dubleerimist ja olla paindlikum andmete uurimisel. Vaatame relatsioonandmebaasi mõisteid.

## [Eel-loengu viktoriin](https://ff-quizzes.netlify.app/en/ds/quiz/8)

## Kõik algab tabelitest

Relatsioonandmebaasi tuumaks on tabelid. Nagu tabelarvutusprogrammis, on tabel veergude ja ridade kogum. Rida sisaldab andmeid või teavet, millega soovime töötada, näiteks linna nime või sademete hulka. Veerud kirjeldavad andmeid, mida nad hoiavad.

Alustame uurimist, luues tabeli linnade teabe salvestamiseks. Võiksime alustada nende nime ja riigiga. Seda võiks tabelis hoida järgmiselt:

| Linn     | Riik          |
| -------- | ------------- |
| Tokyo    | Jaapan        |
| Atlanta  | Ameerika Ühendriigid |
| Auckland | Uus-Meremaa   |

Pange tähele veergude nimed **Linn**, **Riik** ja **Rahvaarv**, mis kirjeldavad salvestatavaid andmeid, ning iga rida sisaldab teavet ühe linna kohta.

## Ühe tabeli lähenemise puudused

Tõenäoliselt tundub ülaltoodud tabel teile üsna tuttav. Lisame oma kasvavasse andmebaasi täiendavaid andmeid – aastased sademed (millimeetrites). Keskendume aastatele 2018, 2019 ja 2020. Kui lisaksime need Tokyo kohta, võiks see välja näha umbes nii:

| Linn  | Riik   | Aasta | Kogus |
| ----- | ------ | ----- | ----- |
| Tokyo | Jaapan | 2020  | 1690  |
| Tokyo | Jaapan | 2019  | 1874  |
| Tokyo | Jaapan | 2018  | 1445  |

Mida te meie tabelist märkate? Võite märgata, et kordame linna nime ja riiki ikka ja jälle. See võib võtta üsna palju salvestusruumi ning on suuresti tarbetu mitut koopiat hoida. Lõppude lõpuks on Tokyol ainult üks nimi, mis meid huvitab.

Proovime midagi muud. Lisame iga aasta jaoks uued veerud:

| Linn     | Riik          | 2018 | 2019 | 2020 |
| -------- | ------------- | ---- | ---- | ---- |
| Tokyo    | Jaapan        | 1445 | 1874 | 1690 |
| Atlanta  | Ameerika Ühendriigid | 1779 | 1111 | 1683 |
| Auckland | Uus-Meremaa   | 1386 | 942  | 1176 |

Kuigi see väldib ridade dubleerimist, tekitab see mõned teised väljakutsed. Me peaksime iga kord, kui tuleb uus aasta, muutma tabeli struktuuri. Lisaks, kui meie andmed kasvavad, teeb aastate veergudena hoidmine väärtuste pärimise ja arvutamise keerulisemaks.

Seetõttu vajame mitut tabelit ja seoseid. Andmete lahutamisega saame vältida dubleerimist ja olla paindlikumad andmetega töötamisel.

## Seoste mõisted

Tagasi meie andmete juurde ja otsustame, kuidas neid jagada. Teame, et soovime salvestada linnade nime ja riigi, seega sobib see tõenäoliselt kõige paremini ühte tabelisse.

| Linn     | Riik          |
| -------- | ------------- |
| Tokyo    | Jaapan        |
| Atlanta  | Ameerika Ühendriigid |
| Auckland | Uus-Meremaa   |

Enne järgmise tabeli loomist peame välja mõtlema, kuidas iga linna viidata. Me vajame mingit identifikaatorit, ID-d või (tehnilises andmebaasi mõistes) esmavõtit. Esmavõti on väärtus, mida kasutatakse ühe konkreetse rea tuvastamiseks tabelis. Kuigi see võiks põhineda väärtusel endal (näiteks võiksime kasutada linna nime), peaks see peaaegu alati olema number või muu identifikaator. Me ei taha, et id kunagi muutuks, sest see rikuks seose. Enamasti on esmavõti või id automaatselt genereeritud number.

> ✅ Esmavõtit lühendatakse sageli PK-ks

### linnad

| city_id | Linn     | Riik          |
| ------- | -------- | ------------- |
| 1       | Tokyo    | Jaapan        |
| 2       | Atlanta  | Ameerika Ühendriigid |
| 3       | Auckland | Uus-Meremaa   |

> ✅ Märkate, et selle tunni jooksul kasutame termineid "id" ja "esmavõti" vaheldumisi. Need mõisted kehtivad ka DataFrame'ide puhul, mida uurite hiljem. DataFrame'id ei kasuta terminit "esmavõti", kuid käituvad sarnaselt.

Kui meie linnade tabel on loodud, salvestame sademed. Selle asemel, et dubleerida kogu linna teavet, võime kasutada id-d. Samuti peaksime tagama, et uuel tabelil oleks *id* veerg, sest kõigil tabelitel peaks olema id või esmavõti.

### sademed

| rainfall_id | city_id | Aasta | Kogus |
| ----------- | ------- | ----- | ----- |
| 1           | 1       | 2018  | 1445  |
| 2           | 1       | 2019  | 1874  |
| 3           | 1       | 2020  | 1690  |
| 4           | 2       | 2018  | 1779  |
| 5           | 2       | 2019  | 1111  |
| 6           | 2       | 2020  | 1683  |
| 7           | 3       | 2018  | 1386  |
| 8           | 3       | 2019  | 942   |
| 9           | 3       | 2020  | 1176  |

Pange tähele veergu **city_id** äsja loodud tabelis **sademed**. See veerg sisaldab väärtusi, mis viitavad ID-dele tabelis **linnad**. Tehnilises relatsioonandmete mõistes nimetatakse seda **võõrvõtmeks**; see on esmavõti teisest tabelist. Võite seda lihtsalt mõelda kui viidet või osutajat. **city_id** 1 viitab Tokyole.

> [!NOTE] 
> Võõrvõtit lühendatakse sageli FK-ks

## Andmete pärimine

Kui meie andmed on jagatud kaheks tabeliks, võite mõelda, kuidas neid pärida. Kui kasutame relatsioonandmebaasi nagu MySQL, SQL Server või Oracle, saame kasutada keelt nimega Structured Query Language ehk SQL. SQL (mõnikord hääldatakse "sequel") on standardkeel, mida kasutatakse relatsioonandmebaasis andmete pärimiseks ja muutmiseks.

Andmete pärimiseks kasutatakse käsku `SELECT`. Põhimõtteliselt **valite** veerud, mida soovite näha, **tabelist**, kus need asuvad. Kui soovite kuvada ainult linnade nimesid, võiksite kasutada järgmist:

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
> SQL süntaks ei ole tõstutundlik, mis tähendab, et `select` ja `SELECT` tähendavad sama asja. Kuid sõltuvalt andmebaasi tüübist võivad veerud ja tabelid olla tõstutundlikud. Seetõttu on hea tava käsitleda kõike programmeerimises nagu see oleks tõstutundlik. SQL päringute kirjutamisel on tavapärane panna võtmesõnad suurte tähtedega.

Ülaltoodud päring kuvab kõik linnad. Kujutame ette, et soovime kuvada ainult Uus-Meremaa linnu. Me vajame mingit filtrit. SQL võtmesõna selleks on `WHERE`, ehk "kus midagi on tõene".

```sql
SELECT city
FROM cities
WHERE country = 'New Zealand';

-- Output:
-- Auckland
```

## Andmete ühendamine

Senini oleme pärinud andmeid ühest tabelist. Nüüd tahame tuua andmed kokku nii tabelist **linnad** kui ka **sademed**. Seda tehakse nende *ühendamisega*. Teisisõnu loote õmbluse kahe tabeli vahele ja sobitate veergude väärtused.

Meie näites sobitame veeru **city_id** tabelis **sademed** veeruga **city_id** tabelis **linnad**. See seob sademete väärtuse vastava linnaga. Ühenduse tüüp, mida teeme, on nn *sisemine* ühendus, mis tähendab, et kui mõni rida ei sobi teise tabeli ühegi reaga, siis seda ei kuvata. Meie puhul on igal linnal sademed, seega kuvatakse kõik.

Võtame pärimiseks 2019. aasta sademed kõigi linnade kohta.

Teeme seda sammhaaval. Esimene samm on andmete ühendamine, näidates veerge, mille järgi õmblus tehakse – **city_id**, nagu eelnevalt rõhutatud.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
```

Oleme esile tõstnud kaks veergu, mida soovime, ja selle, et tahame ühendada tabelid veeru **city_id** alusel. Nüüd saame lisada `WHERE` lause, et filtreerida ainult aasta 2019 andmed.

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

Relatsioonandmebaasid põhinevad teabe jagamisel mitmesse tabelisse, mis seejärel tuuakse kuvamiseks ja analüüsiks uuesti kokku. See annab suure paindlikkuse arvutuste tegemiseks ja andmete manipuleerimiseks. Olete näinud relatsioonandmebaasi põhikontseptsioone ja kuidas teha ühendust kahe tabeli vahel.

## 🚀 Väljakutse

Internetis on saadaval palju relatsioonandmebaase. Saate uurida andmeid, kasutades siin õpitud oskusi.

## Järgmise loengu viktoriin

## [Järgmise loengu viktoriin](https://ff-quizzes.netlify.app/en/ds/quiz/9)

## Kordamine ja iseseisev õpe

[Microsoft Learn](https://docs.microsoft.com/learn?WT.mc_id=academic-77958-bethanycheum) pakub mitmeid ressursse, et jätkata SQL ja relatsioonandmebaasi mõistete uurimist

- [Kirjeldage relatsioonandmete mõisteid](https://docs.microsoft.com//learn/modules/describe-concepts-of-relational-data?WT.mc_id=academic-77958-bethanycheum)
- [Alustamine päringutega Transact-SQL-iga](https://docs.microsoft.com//learn/paths/get-started-querying-with-transact-sql?WT.mc_id=academic-77958-bethanycheum) (Transact-SQL on SQL versioon)
- [SQL sisu Microsoft Learn'is](https://docs.microsoft.com/learn/browse/?products=azure-sql-database%2Csql-server&expanded=azure&WT.mc_id=academic-77958-bethanycheum)

## Kodutöö

[Lennujaama andmete kuvamine](assignment.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastutusest loobumine**:
See dokument on tõlgitud kasutades tehisintellektil põhinevat tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi püüame tagada täpsust, palun arvestage, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti mõistmiste eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->