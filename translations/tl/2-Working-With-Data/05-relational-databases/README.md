<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11739c7b40e7c6b16ad29e3df4e65862",
  "translation_date": "2025-12-19T11:54:51+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/README.md",
  "language_code": "tl"
}
-->
# Paggamit ng Data: Relational Databases

|![ Sketchnote ni [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/05-RelationalData.png)|
|:---:|
| Paggamit ng Data: Relational Databases - _Sketchnote ni [@nitya](https://twitter.com/nitya)_ |

Malamang na nakagamit ka na ng spreadsheet noon upang mag-imbak ng impormasyon. Mayroon kang hanay ng mga row at column, kung saan ang mga row ay naglalaman ng impormasyon (o data), at ang mga column ay naglalarawan ng impormasyon (minsan tinatawag na metadata). Ang relational database ay binuo sa pangunahing prinsipyong ito ng mga column at row sa mga talahanayan, na nagpapahintulot sa iyo na magkaroon ng impormasyon na nakakalat sa maraming talahanayan. Pinapayagan ka nitong magtrabaho sa mas kumplikadong data, maiwasan ang pag-uulit, at magkaroon ng kakayahang umangkop sa paraan ng pag-explore ng data. Tuklasin natin ang mga konsepto ng isang relational database.

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ds/quiz/8)

## Nagsisimula ito sa mga talahanayan

Ang relational database ay may sentro nitong mga talahanayan. Katulad ng sa spreadsheet, ang isang talahanayan ay koleksyon ng mga column at row. Ang row ay naglalaman ng data o impormasyon na nais nating gamitin, tulad ng pangalan ng isang lungsod o ang dami ng ulan. Ang mga column ay naglalarawan ng data na kanilang iniimbak.

Magsimula tayo sa paglikha ng isang talahanayan upang mag-imbak ng impormasyon tungkol sa mga lungsod. Maaaring magsimula tayo sa kanilang pangalan at bansa. Maaari mo itong iimbak sa isang talahanayan tulad ng sumusunod:

| Lungsod  | Bansa         |
| -------- | ------------- |
| Tokyo    | Japan         |
| Atlanta  | United States |
| Auckland | New Zealand   |

Pansinin ang mga pangalan ng column na **lungsod**, **bansa** at **populasyon** na naglalarawan ng data na iniimbak, at bawat row ay may impormasyon tungkol sa isang lungsod.

## Mga kakulangan ng isang talahanayan lamang

Malamang na pamilyar sa iyo ang talahanayan sa itaas. Magsimula tayong magdagdag ng karagdagang data sa ating lumalaking database - taunang dami ng ulan (sa millimeters). Tututukan natin ang mga taon 2018, 2019 at 2020. Kung idaragdag natin ito para sa Tokyo, maaaring ganito ang itsura:

| Lungsod | Bansa | Taon | Dami  |
| ------- | ----- | ---- | ----- |
| Tokyo   | Japan | 2020 | 1690  |
| Tokyo   | Japan | 2019 | 1874  |
| Tokyo   | Japan | 2018 | 1445  |

Ano ang napapansin mo tungkol sa ating talahanayan? Maaaring mapansin mo na inuulit natin ang pangalan at bansa ng lungsod nang paulit-ulit. Maaari itong kumain ng maraming imbakan, at hindi naman kailangan na magkaroon ng maraming kopya nito. Pagkatapos ng lahat, iisa lang ang pangalan ng Tokyo na interesado tayo.

Sige, subukan natin ang iba pa. Magdagdag tayo ng mga bagong column para sa bawat taon:

| Lungsod  | Bansa         | 2018 | 2019 | 2020 |
| -------- | ------------- | ---- | ---- | ---- |
| Tokyo    | Japan         | 1445 | 1874 | 1690 |
| Atlanta  | United States | 1779 | 1111 | 1683 |
| Auckland | New Zealand   | 1386 | 942  | 1176 |

Bagaman naiiwasan nito ang pag-uulit ng mga row, nagdudulot ito ng ilang iba pang hamon. Kailangan nating baguhin ang istruktura ng ating talahanayan sa tuwing may bagong taon. Bukod pa rito, habang lumalaki ang data natin, ang pagkakaroon ng mga taon bilang mga column ay magpapahirap sa pagkuha at pagkalkula ng mga halaga.

Ito ang dahilan kung bakit kailangan natin ng maraming talahanayan at mga relasyon. Sa pamamagitan ng paghahati-hati ng data, maiiwasan natin ang pag-uulit at magkakaroon tayo ng mas maraming kakayahang umangkop sa paraan ng paggamit ng data.

## Mga konsepto ng mga relasyon

Balikan natin ang ating data at tukuyin kung paano natin nais hatiin ang mga bagay. Alam natin na nais nating iimbak ang pangalan at bansa para sa ating mga lungsod, kaya't ito ay malamang na pinakamahusay na ilagay sa isang talahanayan.

| Lungsod  | Bansa         |
| -------- | ------------- |
| Tokyo    | Japan         |
| Atlanta  | United States |
| Auckland | New Zealand   |

Ngunit bago tayo gumawa ng susunod na talahanayan, kailangan nating alamin kung paano i-referensiya ang bawat lungsod. Kailangan natin ng isang uri ng identifier, ID o (sa teknikal na termino ng database) isang primary key. Ang primary key ay isang halaga na ginagamit upang tukuyin ang isang partikular na row sa isang talahanayan. Bagaman maaari itong batay sa isang halaga mismo (maaari nating gamitin ang pangalan ng lungsod, halimbawa), dapat ito ay isang numero o ibang identifier. Ayaw nating magbago ang id dahil masisira nito ang relasyon. Sa karamihan ng mga kaso, ang primary key o id ay isang auto-generated na numero.

> ✅ Ang Primary key ay madalas pinaikling PK

### lungsod

| city_id | Lungsod  | Bansa         |
| ------- | -------- | ------------- |
| 1       | Tokyo    | Japan         |
| 2       | Atlanta  | United States |
| 3       | Auckland | New Zealand   |

> ✅ Mapapansin mo na ginagamit natin ang mga terminong "id" at "primary key" nang palitan sa araling ito. Ang mga konsepto dito ay naaangkop sa DataFrames, na iyong tatalakayin sa hinaharap. Hindi ginagamit ng DataFrames ang terminolohiyang "primary key", ngunit mapapansin mong kumikilos ito sa halos parehong paraan.

Sa pagkakaroon ng ating lungsod na talahanayan, iimbak naman natin ang dami ng ulan. Sa halip na ulitin ang buong impormasyon tungkol sa lungsod, maaari nating gamitin ang id. Dapat din nating tiyakin na ang bagong likhang talahanayan ay may *id* na column, dahil lahat ng talahanayan ay dapat may id o primary key.

### dami ng ulan

| rainfall_id | city_id | Taon | Dami  |
| ----------- | ------- | ---- | ----- |
| 1           | 1       | 2018 | 1445  |
| 2           | 1       | 2019 | 1874  |
| 3           | 1       | 2020 | 1690  |
| 4           | 2       | 2018 | 1779  |
| 5           | 2       | 2019 | 1111  |
| 6           | 2       | 2020 | 1683  |
| 7           | 3       | 2018 | 1386  |
| 8           | 3       | 2019 | 942   |
| 9           | 3       | 2020 | 1176  |

Pansinin ang column na **city_id** sa loob ng bagong likhang **rainfall** na talahanayan. Ang column na ito ay naglalaman ng mga halaga na nagre-refer sa mga ID sa **lungsod** na talahanayan. Sa teknikal na termino ng relational data, ito ay tinatawag na **foreign key**; ito ay isang primary key mula sa ibang talahanayan. Maaari mo itong isipin bilang isang reference o pointer. Ang **city_id** 1 ay nagre-refer sa Tokyo.

> [!NOTE] 
> Ang Foreign key ay madalas pinaikling FK

## Pagkuha ng data

Sa paghahati ng data sa dalawang talahanayan, maaaring nagtatanong ka kung paano ito kukunin. Kung gumagamit tayo ng relational database tulad ng MySQL, SQL Server o Oracle, maaari nating gamitin ang isang wika na tinatawag na Structured Query Language o SQL. Ang SQL (minsan binibigkas na sequel) ay isang standard na wika na ginagamit upang kunin at baguhin ang data sa isang relational database.

Upang kunin ang data, ginagamit mo ang utos na `SELECT`. Sa pinakapayak na anyo, **pinipili** mo ang mga column na nais mong makita **mula sa** talahanayan kung saan ito nakapaloob. Kung nais mo lamang ipakita ang mga pangalan ng mga lungsod, maaari mong gamitin ang sumusunod:

```sql
SELECT city
FROM cities;

-- Output:
-- Tokyo
-- Atlanta
-- Auckland
```

`SELECT` ay kung saan inililista mo ang mga column, at `FROM` ay kung saan inililista mo ang mga talahanayan.

> [!NOTE] 
> Ang syntax ng SQL ay hindi case-sensitive, ibig sabihin `select` at `SELECT` ay pareho ang ibig sabihin. Gayunpaman, depende sa uri ng database na ginagamit mo, maaaring case sensitive ang mga column at talahanayan. Dahil dito, pinakamainam na ituring ang lahat sa programming na case sensitive. Sa pagsulat ng mga SQL query, karaniwang convention ang paggamit ng mga keyword sa lahat ng malalaking titik.

Ipinapakita ng query sa itaas ang lahat ng lungsod. Isipin natin na nais lamang nating ipakita ang mga lungsod sa New Zealand. Kailangan natin ng isang uri ng filter. Ang SQL keyword para dito ay `WHERE`, o "kung saan ang isang bagay ay totoo".

```sql
SELECT city
FROM cities
WHERE country = 'New Zealand';

-- Output:
-- Auckland
```

## Pagsasama-sama ng data

Hanggang ngayon, kumuha tayo ng data mula sa isang talahanayan lamang. Ngayon nais nating pagsamahin ang data mula sa parehong **lungsod** at **rainfall**. Ginagawa ito sa pamamagitan ng *joining* ng mga ito. Epektibo kang gagawa ng isang ugnayan sa pagitan ng dalawang talahanayan, at itutugma ang mga halaga mula sa isang column ng bawat talahanayan.

Sa ating halimbawa, itutugma natin ang column na **city_id** sa **rainfall** sa column na **city_id** sa **lungsod**. Itutugma nito ang halaga ng ulan sa kaukulang lungsod. Ang uri ng join na gagawin natin ay tinatawag na *inner* join, ibig sabihin kung may mga row na hindi tumutugma sa anumang bagay mula sa kabilang talahanayan, hindi ito ipapakita. Sa ating kaso, bawat lungsod ay may dami ng ulan, kaya lahat ay ipapakita.

Kunin natin ang dami ng ulan para sa 2019 para sa lahat ng ating mga lungsod.

Gagawin natin ito sa mga hakbang. Ang unang hakbang ay pagsamahin ang data sa pamamagitan ng pagtukoy sa mga column para sa ugnayan - **city_id** tulad ng na-highlight kanina.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
```

Na-highlight natin ang dalawang column na gusto natin, at ang katotohanan na nais nating pagsamahin ang mga talahanayan sa pamamagitan ng **city_id**. Ngayon maaari nating idagdag ang `WHERE` na pahayag upang i-filter lamang ang taon 2019.

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

## Buod

Ang mga relational database ay nakasentro sa paghahati ng impormasyon sa maraming talahanayan na pagkatapos ay pinagsasama-sama para sa pagpapakita at pagsusuri. Nagbibigay ito ng mataas na antas ng kakayahang umangkop upang magsagawa ng mga kalkulasyon at iba pang manipulasyon ng data. Nakita mo ang mga pangunahing konsepto ng isang relational database, at kung paano magsagawa ng join sa pagitan ng dalawang talahanayan.

## 🚀 Hamon

Maraming mga relational database ang makukuha sa internet. Maaari mong tuklasin ang data gamit ang mga kasanayang natutunan mo sa itaas.

## Post-Lecture Quiz

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ds/quiz/9)

## Review & Self Study

Mayroong ilang mga mapagkukunan sa [Microsoft Learn](https://docs.microsoft.com/learn?WT.mc_id=academic-77958-bethanycheum) para ipagpatuloy mo ang iyong pag-aaral tungkol sa SQL at mga konsepto ng relational database

- [Ilarawan ang mga konsepto ng relational data](https://docs.microsoft.com//learn/modules/describe-concepts-of-relational-data?WT.mc_id=academic-77958-bethanycheum)
- [Magsimula sa Pag-query gamit ang Transact-SQL](https://docs.microsoft.com//learn/paths/get-started-querying-with-transact-sql?WT.mc_id=academic-77958-bethanycheum) (Ang Transact-SQL ay isang bersyon ng SQL)
- [Nilalaman ng SQL sa Microsoft Learn](https://docs.microsoft.com/learn/browse/?products=azure-sql-database%2Csql-server&expanded=azure&WT.mc_id=academic-77958-bethanycheum)

## Assignment

[Pagpapakita ng data ng paliparan](assignment.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Paalala**:
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa kanyang sariling wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->