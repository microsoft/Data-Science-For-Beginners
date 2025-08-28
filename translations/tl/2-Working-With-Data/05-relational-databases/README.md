<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "870a0086adbc313a8eea5489bdcb2522",
  "translation_date": "2025-08-28T02:28:53+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/README.md",
  "language_code": "tl"
}
-->
# Paggamit ng Data: Relational Databases

|![ Sketchnote ni [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/05-RelationalData.png)|
|:---:|
| Paggamit ng Data: Relational Databases - _Sketchnote ni [@nitya](https://twitter.com/nitya)_ |

Malaki ang posibilidad na gumamit ka na ng spreadsheet noon para mag-imbak ng impormasyon. Mayroon kang hanay ng mga row at column, kung saan ang mga row ay naglalaman ng impormasyon (o data), at ang mga column ay naglalarawan ng impormasyon (minsan tinatawag na metadata). Ang relational database ay nakabatay sa prinsipyong ito ng mga column at row sa mga talahanayan, na nagbibigay-daan sa iyo na mag-imbak ng impormasyon sa maraming talahanayan. Sa ganitong paraan, maaari kang magtrabaho sa mas komplikadong data, maiwasan ang pag-uulit, at magkaroon ng kalayaan sa paggalugad ng data. Tuklasin natin ang mga konsepto ng relational database.

## [Pre-lecture quiz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/8)

## Nagsisimula ang lahat sa mga talahanayan

Ang relational database ay may pangunahing bahagi na mga talahanayan. Katulad ng spreadsheet, ang talahanayan ay koleksyon ng mga column at row. Ang row ay naglalaman ng data o impormasyon na nais nating gamitin, tulad ng pangalan ng isang lungsod o dami ng ulan. Ang mga column naman ay naglalarawan ng data na iniimbak.

Simulan natin ang ating paggalugad sa pamamagitan ng paggawa ng talahanayan para mag-imbak ng impormasyon tungkol sa mga lungsod. Maaaring magsimula tayo sa kanilang pangalan at bansa. Maaari mo itong iimbak sa isang talahanayan tulad nito:

| Lungsod  | Bansa          |
| -------- | -------------- |
| Tokyo    | Japan          |
| Atlanta  | United States  |
| Auckland | New Zealand    |

Pansinin ang mga pangalan ng column na **lungsod**, **bansa**, at **populasyon** na naglalarawan ng data na iniimbak, at bawat row ay may impormasyon tungkol sa isang lungsod.

## Mga limitasyon ng isang talahanayan lamang

Malaki ang posibilidad na pamilyar ka sa talahanayan sa itaas. Subukan nating magdagdag ng karagdagang data sa ating lumalaking database - taunang dami ng ulan (sa millimeters). Magpokus tayo sa mga taon 2018, 2019, at 2020. Kung idaragdag natin ito para sa Tokyo, maaaring ganito ang hitsura:

| Lungsod | Bansa  | Taon | Dami  |
| ------- | ------ | ---- | ----- |
| Tokyo   | Japan  | 2020 | 1690  |
| Tokyo   | Japan  | 2019 | 1874  |
| Tokyo   | Japan  | 2018 | 1445  |

Ano ang napapansin mo sa ating talahanayan? Mapapansin mong inuulit-ulit natin ang pangalan at bansa ng lungsod. Maaari itong kumonsumo ng maraming storage at hindi naman talaga kinakailangang ulitin. Pagkatapos ng lahat, iisa lang naman ang pangalan ng Tokyo na interesado tayo.

Sige, subukan natin ang ibang paraan. Magdagdag tayo ng bagong mga column para sa bawat taon:

| Lungsod  | Bansa          | 2018 | 2019 | 2020 |
| -------- | -------------- | ---- | ---- | ---- |
| Tokyo    | Japan          | 1445 | 1874 | 1690 |
| Atlanta  | United States  | 1779 | 1111 | 1683 |
| Auckland | New Zealand    | 1386 | 942  | 1176 |

Bagamat naiwasan nito ang pag-uulit ng mga row, nagdulot naman ito ng ibang hamon. Kailangan nating baguhin ang istruktura ng ating talahanayan tuwing may bagong taon. Bukod dito, habang lumalaki ang ating data, ang pagkakaroon ng mga taon bilang mga column ay magpapahirap sa pagkuha at pagkalkula ng mga halaga.

Ito ang dahilan kung bakit kailangan natin ng maraming talahanayan at mga relasyon. Sa pamamagitan ng paghahati ng ating data, maiiwasan natin ang pag-uulit at magkakaroon tayo ng mas maraming kalayaan sa paggamit ng ating data.

## Ang mga konsepto ng relasyon

Balikan natin ang ating data at tukuyin kung paano natin ito hahatiin. Alam natin na nais nating iimbak ang pangalan at bansa ng ating mga lungsod, kaya't ito ay pinakamainam na ilagay sa isang talahanayan.

| Lungsod  | Bansa          |
| -------- | -------------- |
| Tokyo    | Japan          |
| Atlanta  | United States  |
| Auckland | New Zealand    |

Ngunit bago tayo lumikha ng susunod na talahanayan, kailangan nating alamin kung paano ire-refer ang bawat lungsod. Kailangan natin ng isang uri ng identifier, ID o (sa teknikal na termino ng database) isang primary key. Ang primary key ay isang halaga na ginagamit upang tukuyin ang isang partikular na row sa isang talahanayan. Bagamat maaari itong batay sa isang halaga mismo (halimbawa, maaari nating gamitin ang pangalan ng lungsod), dapat itong halos palaging isang numero o ibang identifier. Ayaw nating magbago ang id dahil maaaring masira ang relasyon. Sa karamihan ng mga kaso, ang primary key o id ay isang auto-generated na numero.

> ✅ Ang primary key ay madalas na pinaikli bilang PK

### lungsod

| lungsod_id | Lungsod  | Bansa          |
| ---------- | -------- | -------------- |
| 1          | Tokyo    | Japan          |
| 2          | Atlanta  | United States  |
| 3          | Auckland | New Zealand    |

> ✅ Mapapansin mong ginagamit natin ang mga terminong "id" at "primary key" nang salitan sa araling ito. Ang mga konsepto dito ay naaangkop din sa DataFrames, na iyong matutuklasan sa susunod. Ang DataFrames ay hindi gumagamit ng terminolohiyang "primary key", ngunit mapapansin mong gumagana ang mga ito sa parehong paraan.

Kapag nagawa na ang ating talahanayan ng lungsod, iimbak natin ang dami ng ulan. Sa halip na ulitin ang buong impormasyon tungkol sa lungsod, maaari nating gamitin ang id. Dapat din nating tiyakin na ang bagong talahanayan ay may column na *id*, dahil lahat ng talahanayan ay dapat may id o primary key.

### ulan

| ulan_id | lungsod_id | Taon | Dami  |
| ------- | ---------- | ---- | ----- |
| 1       | 1          | 2018 | 1445  |
| 2       | 1          | 2019 | 1874  |
| 3       | 1          | 2020 | 1690  |
| 4       | 2          | 2018 | 1779  |
| 5       | 2          | 2019 | 1111  |
| 6       | 2          | 2020 | 1683  |
| 7       | 3          | 2018 | 1386  |
| 8       | 3          | 2019 | 942   |
| 9       | 3          | 2020 | 1176  |

Pansinin ang column na **lungsod_id** sa loob ng bagong talahanayan na **ulan**. Ang column na ito ay naglalaman ng mga halaga na tumutukoy sa mga ID sa talahanayan ng **lungsod**. Sa teknikal na termino ng relational data, ito ay tinatawag na **foreign key**; ito ay isang primary key mula sa ibang talahanayan. Maaari mo itong isipin bilang isang reference o pointer. Ang **lungsod_id** 1 ay tumutukoy sa Tokyo.

> [!NOTE] Ang foreign key ay madalas na pinaikli bilang FK

## Pagkuha ng data

Kapag ang ating data ay nahati na sa dalawang talahanayan, maaaring magtaka ka kung paano ito kukunin. Kung gumagamit tayo ng relational database tulad ng MySQL, SQL Server, o Oracle, maaari nating gamitin ang isang wika na tinatawag na Structured Query Language o SQL. Ang SQL (minsan binibigkas na sequel) ay isang standard na wika na ginagamit upang kunin at baguhin ang data sa isang relational database.

Upang kunin ang data, ginagamit mo ang utos na `SELECT`. Sa pinakasimple nito, **piliin** mo ang mga column na nais mong makita **mula sa** talahanayan kung saan ito nakapaloob. Kung nais mong ipakita lamang ang mga pangalan ng lungsod, maaari mong gamitin ang sumusunod:

```sql
SELECT city
FROM cities;

-- Output:
-- Tokyo
-- Atlanta
-- Auckland
```

Ang `SELECT` ay kung saan mo ililista ang mga column, at ang `FROM` ay kung saan mo ililista ang mga talahanayan.

> [NOTE] Ang syntax ng SQL ay case-insensitive, ibig sabihin ang `select` at `SELECT` ay pareho lang. Gayunpaman, depende sa uri ng database na iyong ginagamit, maaaring case-sensitive ang mga column at talahanayan. Bilang resulta, pinakamainam na palaging ituring na case-sensitive ang lahat sa programming. Kapag nagsusulat ng SQL queries, karaniwang convention na gawing uppercase ang mga keyword.

Ang query sa itaas ay magpapakita ng lahat ng lungsod. Halimbawa, kung nais lamang nating ipakita ang mga lungsod sa New Zealand, kailangan natin ng isang uri ng filter. Ang SQL keyword para dito ay `WHERE`, o "kung saan totoo ang isang bagay".

```sql
SELECT city
FROM cities
WHERE country = 'New Zealand';

-- Output:
-- Auckland
```

## Pagsasama ng data

Hanggang ngayon, kumuha tayo ng data mula sa isang talahanayan lamang. Ngayon, nais nating pagsamahin ang data mula sa parehong **lungsod** at **ulan**. Ginagawa ito sa pamamagitan ng *pagsasama* ng mga ito. Magkakaroon ka ng seam sa pagitan ng dalawang talahanayan, at pagtutugmain ang mga halaga mula sa isang column ng bawat talahanayan.

Sa ating halimbawa, pagtutugmain natin ang column na **lungsod_id** sa **ulan** sa column na **lungsod_id** sa **lungsod**. Ito ay magtutugma sa halaga ng ulan sa kani-kanilang lungsod. Ang uri ng pagsasama na gagawin natin ay tinatawag na *inner* join, ibig sabihin kung may mga row na hindi tumutugma sa anumang bagay mula sa kabilang talahanayan, hindi ito ipapakita. Sa ating kaso, lahat ng lungsod ay may ulan, kaya't lahat ay ipapakita.

Kunin natin ang ulan para sa 2019 para sa lahat ng ating lungsod.

Gagawin natin ito nang paunti-unti. Ang unang hakbang ay pagsamahin ang data sa pamamagitan ng pagtukoy sa mga column para sa seam - **lungsod_id** tulad ng nabanggit kanina.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
```

Ipinakita natin ang dalawang column na nais natin, at ang katotohanang nais nating pagsamahin ang mga talahanayan sa pamamagitan ng **lungsod_id**. Ngayon, maaari nating idagdag ang `WHERE` statement upang i-filter lamang ang taon 2019.

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

Ang relational databases ay nakasentro sa paghahati ng impormasyon sa maraming talahanayan na pagkatapos ay pinagsasama-sama para sa pagpapakita at pagsusuri. Nagbibigay ito ng mataas na antas ng kalayaan upang magsagawa ng mga kalkulasyon at manipulahin ang data. Nakita mo ang mga pangunahing konsepto ng relational database, at kung paano magsagawa ng join sa pagitan ng dalawang talahanayan.

## 🚀 Hamon

Maraming relational databases ang makikita sa internet. Maaari mong tuklasin ang data gamit ang mga kasanayang natutunan mo sa itaas.

## Post-Lecture Quiz

## [Post-lecture quiz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/9)

## Review at Pag-aaral sa Sarili

Maraming mapagkukunan sa [Microsoft Learn](https://docs.microsoft.com/learn?WT.mc_id=academic-77958-bethanycheum) na maaari mong gamitin upang ipagpatuloy ang iyong pag-aaral sa SQL at mga konsepto ng relational database.

- [Ilarawan ang mga konsepto ng relational data](https://docs.microsoft.com//learn/modules/describe-concepts-of-relational-data?WT.mc_id=academic-77958-bethanycheum)
- [Magsimula sa Querying gamit ang Transact-SQL](https://docs.microsoft.com//learn/paths/get-started-querying-with-transact-sql?WT.mc_id=academic-77958-bethanycheum) (Ang Transact-SQL ay isang bersyon ng SQL)
- [SQL content sa Microsoft Learn](https://docs.microsoft.com/learn/browse/?products=azure-sql-database%2Csql-server&expanded=azure&WT.mc_id=academic-77958-bethanycheum)

## Takdang-Aralin

[Titulo ng Takdang-Aralin](assignment.md)

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.