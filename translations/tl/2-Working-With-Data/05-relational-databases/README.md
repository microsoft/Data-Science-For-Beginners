<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11b166fbcb7eaf82308cdc24b562f687",
  "translation_date": "2025-09-04T20:57:42+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/README.md",
  "language_code": "tl"
}
-->
# Paggamit ng Data: Relational Databases

|![ Sketchnote ni [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/05-RelationalData.png)|
|:---:|
| Paggamit ng Data: Relational Databases - _Sketchnote ni [@nitya](https://twitter.com/nitya)_ |

Malamang gumamit ka na ng spreadsheet noon para mag-imbak ng impormasyon. Mayroon kang hanay ng mga row at column, kung saan ang mga row ay naglalaman ng impormasyon (o data), at ang mga column ay naglalarawan ng impormasyon (minsan tinatawag na metadata). Ang relational database ay nakabatay sa prinsipyong ito ng mga column at row sa mga talahanayan, na nagbibigay-daan sa iyo na magkaroon ng impormasyon na nakakalat sa iba't ibang talahanayan. Pinapayagan ka nitong magtrabaho sa mas kumplikadong data, maiwasan ang pag-uulit, at magkaroon ng flexibility sa paraan ng paggalugad sa data. Tuklasin natin ang mga konsepto ng relational database.

## [Pre-lecture quiz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/8)

## Nagsisimula ito sa mga talahanayan

Ang relational database ay may pangunahing elemento na tinatawag na mga talahanayan. Katulad ng spreadsheet, ang talahanayan ay koleksyon ng mga column at row. Ang row ay naglalaman ng data o impormasyon na nais nating gamitin, tulad ng pangalan ng lungsod o dami ng ulan. Ang mga column naman ay naglalarawan sa data na kanilang iniimbak.

Simulan natin ang ating paggalugad sa pamamagitan ng paggawa ng talahanayan para mag-imbak ng impormasyon tungkol sa mga lungsod. Maaaring magsimula tayo sa kanilang pangalan at bansa. Maaari mong iimbak ito sa isang talahanayan tulad ng sumusunod:

| Lungsod  | Bansa         |
| -------- | ------------- |
| Tokyo    | Japan         |
| Atlanta  | United States |
| Auckland | New Zealand   |

Pansinin ang mga pangalan ng column na **lungsod**, **bansa**, at **populasyon** na naglalarawan sa data na iniimbak, at bawat row ay may impormasyon tungkol sa isang lungsod.

## Mga limitasyon ng isang talahanayan

Malamang, ang talahanayan sa itaas ay pamilyar sa iyo. Subukan nating magdagdag ng karagdagang data sa ating lumalaking database - taunang dami ng ulan (sa millimeters). Mag-focus tayo sa mga taon 2018, 2019, at 2020. Kung idadagdag natin ito para sa Tokyo, maaaring ganito ang hitsura:

| Lungsod | Bansa | Taon | Dami   |
| ------- | ----- | ---- | ------ |
| Tokyo   | Japan | 2020 | 1690   |
| Tokyo   | Japan | 2019 | 1874   |
| Tokyo   | Japan | 2018 | 1445   |

Ano ang napapansin mo sa ating talahanayan? Mapapansin mo na inuulit natin ang pangalan at bansa ng lungsod nang paulit-ulit. Maaari itong kumain ng maraming storage, at hindi talaga kinakailangan na magkaroon ng maraming kopya. Pagkatapos ng lahat, ang Tokyo ay may iisang pangalan lamang na interesado tayo.

OK, subukan natin ang ibang paraan. Magdagdag tayo ng mga bagong column para sa bawat taon:

| Lungsod  | Bansa         | 2018 | 2019 | 2020 |
| -------- | ------------- | ---- | ---- | ---- |
| Tokyo    | Japan         | 1445 | 1874 | 1690 |
| Atlanta  | United States | 1779 | 1111 | 1683 |
| Auckland | New Zealand   | 1386 | 942  | 1176 |

Bagama't naiwasan nito ang pag-uulit ng mga row, nagdulot ito ng ilang iba pang hamon. Kailangan nating baguhin ang istruktura ng ating talahanayan tuwing may bagong taon. Bukod dito, habang lumalaki ang ating data, ang pagkakaroon ng mga taon bilang mga column ay magpapahirap sa pagkuha at pagkalkula ng mga halaga.

Ito ang dahilan kung bakit kailangan natin ng maraming talahanayan at mga relasyon. Sa pamamagitan ng paghahati-hati ng ating data, maiiwasan natin ang pag-uulit at magkakaroon ng mas maraming flexibility sa kung paano natin ginagamit ang ating data.

## Ang mga konsepto ng relasyon

Balikan natin ang ating data at tukuyin kung paano natin ito hahatiin. Alam natin na nais nating iimbak ang pangalan at bansa ng ating mga lungsod, kaya't ito ay pinakamahusay na gumagana sa isang talahanayan.

| Lungsod  | Bansa         |
| -------- | ------------- |
| Tokyo    | Japan         |
| Atlanta  | United States |
| Auckland | New Zealand   |

Ngunit bago tayo lumikha ng susunod na talahanayan, kailangan nating tukuyin kung paano ire-refer ang bawat lungsod. Kailangan natin ng isang uri ng identifier, ID o (sa teknikal na termino ng database) isang primary key. Ang primary key ay isang halaga na ginagamit upang tukuyin ang isang partikular na row sa isang talahanayan. Bagama't maaari itong batay sa isang halaga mismo (maaari nating gamitin ang pangalan ng lungsod, halimbawa), halos palaging dapat itong isang numero o iba pang identifier. Ayaw nating magbago ang id dahil masisira nito ang relasyon. Sa karamihan ng mga kaso, ang primary key o id ay isang auto-generated na numero.

> ✅ Ang primary key ay madalas na pinaikli bilang PK

### lungsod

| lungsod_id | Lungsod  | Bansa         |
| ---------- | -------- | ------------- |
| 1          | Tokyo    | Japan         |
| 2          | Atlanta  | United States |
| 3          | Auckland | New Zealand   |

> ✅ Mapapansin mo na ginagamit namin ang mga terminong "id" at "primary key" nang palitan sa araling ito. Ang mga konsepto dito ay nalalapat sa DataFrames, na iyong matutuklasan sa susunod. Ang DataFrames ay hindi gumagamit ng terminolohiya ng "primary key", gayunpaman mapapansin mo na kumikilos sila sa parehong paraan.

Kapag nagawa na ang ating talahanayan ng lungsod, iimbak natin ang dami ng ulan. Sa halip na ulitin ang buong impormasyon tungkol sa lungsod, maaari nating gamitin ang id. Dapat din nating tiyakin na ang bagong talahanayan ay may *id* column, dahil ang lahat ng talahanayan ay dapat may id o primary key.

### ulan

| ulan_id | lungsod_id | Taon | Dami   |
| ------- | ---------- | ---- | ------ |
| 1       | 1          | 2018 | 1445   |
| 2       | 1          | 2019 | 1874   |
| 3       | 1          | 2020 | 1690   |
| 4       | 2          | 2018 | 1779   |
| 5       | 2          | 2019 | 1111   |
| 6       | 2          | 2020 | 1683   |
| 7       | 3          | 2018 | 1386   |
| 8       | 3          | 2019 | 942    |
| 9       | 3          | 2020 | 1176   |

Pansinin ang column na **lungsod_id** sa loob ng bagong talahanayan na **ulan**. Ang column na ito ay naglalaman ng mga halaga na tumutukoy sa mga ID sa talahanayan ng **lungsod**. Sa teknikal na termino ng relational data, ito ay tinatawag na **foreign key**; ito ay isang primary key mula sa ibang talahanayan. Maaari mo itong isipin bilang isang reference o pointer. Ang **lungsod_id** 1 ay tumutukoy sa Tokyo.

> [!NOTE] Ang foreign key ay madalas na pinaikli bilang FK

## Pagkuha ng data

Kapag ang ating data ay nahati sa dalawang talahanayan, maaaring iniisip mo kung paano ito kukunin. Kung gumagamit tayo ng relational database tulad ng MySQL, SQL Server, o Oracle, maaari nating gamitin ang isang wika na tinatawag na Structured Query Language o SQL. Ang SQL (minsan binibigkas na sequel) ay isang standard na wika na ginagamit upang kunin at baguhin ang data sa isang relational database.

Upang kunin ang data, ginagamit mo ang utos na `SELECT`. Sa pinakasimple nito, **piliin** mo ang mga column na nais mong makita **mula** sa talahanayan kung saan sila nakapaloob. Kung nais mong ipakita lamang ang mga pangalan ng lungsod, maaari mong gamitin ang sumusunod:

```sql
SELECT city
FROM cities;

-- Output:
-- Tokyo
-- Atlanta
-- Auckland
```

Ang `SELECT` ay kung saan mo ililista ang mga column, at ang `FROM` ay kung saan mo ililista ang mga talahanayan.

> [NOTE] Ang syntax ng SQL ay case-insensitive, ibig sabihin ang `select` at `SELECT` ay pareho. Gayunpaman, depende sa uri ng database na iyong ginagamit, ang mga column at talahanayan ay maaaring case-sensitive. Bilang resulta, pinakamahusay na kasanayan na palaging ituring ang lahat sa programming na parang case-sensitive. Kapag nagsusulat ng SQL queries, karaniwang convention na ilagay ang mga keyword sa lahat ng uppercase na letra.

Ang query sa itaas ay magpapakita ng lahat ng lungsod. Isipin natin na nais lamang nating ipakita ang mga lungsod sa New Zealand. Kailangan natin ng isang uri ng filter. Ang SQL keyword para dito ay `WHERE`, o "kung saan ang isang bagay ay totoo".

```sql
SELECT city
FROM cities
WHERE country = 'New Zealand';

-- Output:
-- Auckland
```

## Pagsasama ng data

Hanggang ngayon, kumuha tayo ng data mula sa isang talahanayan. Ngayon nais nating pagsamahin ang data mula sa parehong **lungsod** at **ulan**. Ginagawa ito sa pamamagitan ng *pagsasama* sa kanila. Epektibong lilikha ka ng isang seam sa pagitan ng dalawang talahanayan, at itutugma ang mga halaga mula sa isang column mula sa bawat talahanayan.

Sa ating halimbawa, itutugma natin ang column na **lungsod_id** sa **ulan** sa column na **lungsod_id** sa **lungsod**. Ito ay magtutugma sa halaga ng ulan sa kani-kanilang lungsod. Ang uri ng pagsasama na gagawin natin ay tinatawag na *inner* join, ibig sabihin kung may mga row na hindi tumutugma sa anumang bagay mula sa ibang talahanayan, hindi sila ipapakita. Sa ating kaso, bawat lungsod ay may ulan, kaya't lahat ay ipapakita.

Kunin natin ang ulan para sa 2019 para sa lahat ng ating lungsod.

Gagawin natin ito sa mga hakbang. Ang unang hakbang ay pagsamahin ang data sa pamamagitan ng pagtukoy sa mga column para sa seam - **lungsod_id** tulad ng binanggit kanina.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
```

I-highlight natin ang dalawang column na nais natin, at ang katotohanan na nais nating pagsamahin ang mga talahanayan sa pamamagitan ng **lungsod_id**. Ngayon maaari nating idagdag ang `WHERE` statement upang i-filter lamang ang taon 2019.

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

Ang relational databases ay nakasentro sa paghahati ng impormasyon sa pagitan ng maraming talahanayan na pagkatapos ay pinagsama-sama para sa pagpapakita at pagsusuri. Nagbibigay ito ng mataas na antas ng flexibility upang magsagawa ng mga kalkulasyon at iba pang manipulasyon ng data. Nakita mo ang mga pangunahing konsepto ng relational database, at kung paano magsagawa ng pagsasama sa pagitan ng dalawang talahanayan.

## 🚀 Hamon

Maraming relational databases ang magagamit sa internet. Maaari mong tuklasin ang data gamit ang mga kasanayang natutunan mo sa itaas.

## Post-Lecture Quiz

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ds/)

## Review & Pag-aaral sa Sarili

Maraming mga mapagkukunan ang magagamit sa [Microsoft Learn](https://docs.microsoft.com/learn?WT.mc_id=academic-77958-bethanycheum) para ipagpatuloy ang iyong paggalugad sa SQL at mga konsepto ng relational database.

- [Paglalarawan ng mga konsepto ng relational data](https://docs.microsoft.com//learn/modules/describe-concepts-of-relational-data?WT.mc_id=academic-77958-bethanycheum)
- [Simulan ang Pagtatanong gamit ang Transact-SQL](https://docs.microsoft.com//learn/paths/get-started-querying-with-transact-sql?WT.mc_id=academic-77958-bethanycheum) (Ang Transact-SQL ay isang bersyon ng SQL)
- [SQL content sa Microsoft Learn](https://docs.microsoft.com/learn/browse/?products=azure-sql-database%2Csql-server&expanded=azure&WT.mc_id=academic-77958-bethanycheum)

## Takdang-Aralin

[Titulo ng Takdang-Aralin](assignment.md)

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.