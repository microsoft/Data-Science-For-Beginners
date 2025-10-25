<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "80d80300002ef4e77cc7631d5904bd6e",
  "translation_date": "2025-10-25T19:01:43+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/README.md",
  "language_code": "tl"
}
-->
# Paggamit ng Data: Relational Databases

|![ Sketchnote ni [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/05-RelationalData.png)|
|:---:|
| Paggamit ng Data: Relational Databases - _Sketchnote ni [@nitya](https://twitter.com/nitya)_ |

Malamang na gumamit ka na ng spreadsheet noon para mag-imbak ng impormasyon. Mayroon kang hanay ng mga row at column, kung saan ang mga row ay naglalaman ng impormasyon (o data), at ang mga column ay naglalarawan sa impormasyon (minsan tinatawag na metadata). Ang relational database ay nakabatay sa pangunahing prinsipyo ng mga column at row sa mga talahanayan, na nagbibigay-daan sa iyo na magkaroon ng impormasyon na nakakalat sa maraming talahanayan. Pinapayagan ka nitong magtrabaho sa mas kumplikadong data, maiwasan ang pag-uulit, at magkaroon ng flexibility sa paraan ng paggalugad sa data. Tuklasin natin ang mga konsepto ng relational database.

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ds/quiz/8)

## Nagsisimula ang lahat sa mga talahanayan

Ang relational database ay may mga talahanayan bilang pangunahing bahagi nito. Tulad ng spreadsheet, ang talahanayan ay koleksyon ng mga column at row. Ang row ay naglalaman ng data o impormasyon na nais nating gamitin, tulad ng pangalan ng isang lungsod o dami ng ulan. Ang mga column naman ay naglalarawan sa data na kanilang iniimbak.

Simulan natin ang ating pag-aaral sa pamamagitan ng paggawa ng isang talahanayan para mag-imbak ng impormasyon tungkol sa mga lungsod. Maaaring magsimula tayo sa kanilang pangalan at bansa. Maaari mong iimbak ito sa isang talahanayan tulad ng sumusunod:

| Lungsod  | Bansa         |
| -------- | ------------- |
| Tokyo    | Japan         |
| Atlanta  | United States |
| Auckland | New Zealand   |

Pansinin ang mga pangalan ng column na **lungsod**, **bansa**, at **populasyon** na naglalarawan sa data na iniimbak, at bawat row ay may impormasyon tungkol sa isang lungsod.

## Mga limitasyon ng isang talahanayan

Malamang, ang talahanayan sa itaas ay pamilyar sa iyo. Subukan nating magdagdag ng karagdagang data sa ating lumalaking database - taunang dami ng ulan (sa millimeters). Mag-focus tayo sa mga taon 2018, 2019, at 2020. Kung idagdag natin ito para sa Tokyo, maaaring ganito ang hitsura:

| Lungsod | Bansa | Taon | Dami   |
| ------- | ----- | ---- | ------ |
| Tokyo   | Japan | 2020 | 1690   |
| Tokyo   | Japan | 2019 | 1874   |
| Tokyo   | Japan | 2018 | 1445   |

Ano ang napapansin mo sa ating talahanayan? Maaaring mapansin mo na inuulit-ulit natin ang pangalan at bansa ng lungsod. Maaari itong kumain ng maraming storage, at hindi naman talaga kinakailangan na magkaroon ng maraming kopya. Pagkatapos ng lahat, iisa lang ang pangalan ng Tokyo na interesado tayo.

Sige, subukan natin ang ibang paraan. Magdagdag tayo ng bagong mga column para sa bawat taon:

| Lungsod  | Bansa         | 2018 | 2019 | 2020 |
| -------- | ------------- | ---- | ---- | ---- |
| Tokyo    | Japan         | 1445 | 1874 | 1690 |
| Atlanta  | United States | 1779 | 1111 | 1683 |
| Auckland | New Zealand   | 1386 | 942  | 1176 |

Bagama't naiiwasan nito ang pag-uulit ng row, nagdadala naman ito ng iba pang hamon. Kailangan nating baguhin ang istruktura ng ating talahanayan tuwing may bagong taon. Bukod dito, habang lumalaki ang ating data, ang pagkakaroon ng mga taon bilang mga column ay magpapahirap sa pagkuha at pagkalkula ng mga halaga.

Ito ang dahilan kung bakit kailangan natin ng maraming talahanayan at mga relasyon. Sa pamamagitan ng paghahati-hati ng ating data, maiiwasan natin ang pag-uulit at magkakaroon ng mas maraming flexibility sa kung paano natin ito gagamitin.

## Ang mga konsepto ng relasyon

Balikan natin ang ating data at tukuyin kung paano natin ito hahatiin. Alam natin na nais nating iimbak ang pangalan at bansa ng ating mga lungsod, kaya't ito ay malamang na pinakamahusay na gumana sa isang talahanayan.

| Lungsod  | Bansa         |
| -------- | ------------- |
| Tokyo    | Japan         |
| Atlanta  | United States |
| Auckland | New Zealand   |

Ngunit bago tayo lumikha ng susunod na talahanayan, kailangan nating malaman kung paano ire-refer ang bawat lungsod. Kailangan natin ng isang uri ng identifier, ID o (sa teknikal na database terms) isang primary key. Ang primary key ay isang halaga na ginagamit upang tukuyin ang isang partikular na row sa isang talahanayan. Bagama't maaari itong batay sa isang halaga mismo (maaari nating gamitin ang pangalan ng lungsod, halimbawa), halos palaging dapat itong isang numero o ibang identifier. Ayaw nating magbago ang id dahil masisira nito ang relasyon. Sa karamihan ng mga kaso, ang primary key o id ay isang auto-generated na numero.

> ✅ Ang primary key ay madalas na pinaikli bilang PK

### mga lungsod

| city_id | Lungsod  | Bansa         |
| ------- | -------- | ------------- |
| 1       | Tokyo    | Japan         |
| 2       | Atlanta  | United States |
| 3       | Auckland | New Zealand   |

> ✅ Mapapansin mo na ginagamit namin ang mga terminong "id" at "primary key" nang palitan sa araling ito. Ang mga konsepto dito ay naaangkop sa DataFrames, na iyong matutuklasan sa susunod. Ang DataFrames ay hindi gumagamit ng terminolohiya ng "primary key", gayunpaman mapapansin mo na kumikilos sila nang halos pareho.

Kapag nagawa na ang ating talahanayan ng mga lungsod, iimbak natin ang dami ng ulan. Sa halip na ulitin ang buong impormasyon tungkol sa lungsod, maaari nating gamitin ang id. Dapat din nating tiyakin na ang bagong talahanayan ay may column na *id*, dahil ang lahat ng talahanayan ay dapat may id o primary key.

### dami ng ulan

| rainfall_id | city_id | Taon | Dami   |
| ----------- | ------- | ---- | ------ |
| 1           | 1       | 2018 | 1445   |
| 2           | 1       | 2019 | 1874   |
| 3           | 1       | 2020 | 1690   |
| 4           | 2       | 2018 | 1779   |
| 5           | 2       | 2019 | 1111   |
| 6           | 2       | 2020 | 1683   |
| 7           | 3       | 2018 | 1386   |
| 8           | 3       | 2019 | 942    |
| 9           | 3       | 2020 | 1176   |

Pansinin ang column na **city_id** sa loob ng bagong talahanayan na **rainfall**. Ang column na ito ay naglalaman ng mga halaga na tumutukoy sa mga ID sa talahanayan ng **cities**. Sa teknikal na relational data terms, ito ay tinatawag na **foreign key**; ito ay isang primary key mula sa ibang talahanayan. Maaari mo itong isipin bilang isang reference o pointer. Ang **city_id** 1 ay tumutukoy sa Tokyo.

> [!NOTE] 
> Ang foreign key ay madalas na pinaikli bilang FK

## Pagkuha ng data

Sa paghihiwalay ng ating data sa dalawang talahanayan, maaaring iniisip mo kung paano ito kukunin. Kung gumagamit tayo ng relational database tulad ng MySQL, SQL Server o Oracle, maaari tayong gumamit ng isang wika na tinatawag na Structured Query Language o SQL. Ang SQL (minsan binibigkas na sequel) ay isang standard na wika na ginagamit upang kunin at baguhin ang data sa isang relational database.

Upang kunin ang data, ginagamit mo ang command na `SELECT`. Sa pinakasimpleng anyo nito, **piliin** mo ang mga column na nais mong makita **mula** sa talahanayan kung saan sila nakapaloob. Kung nais mong ipakita lamang ang mga pangalan ng mga lungsod, maaari mong gamitin ang sumusunod:

```sql
SELECT city
FROM cities;

-- Output:
-- Tokyo
-- Atlanta
-- Auckland
```

Ang `SELECT` ay kung saan mo ililista ang mga column, at ang `FROM` ay kung saan mo ililista ang mga talahanayan.

> [!NOTE] 
> Ang syntax ng SQL ay case-insensitive, ibig sabihin ang `select` at `SELECT` ay pareho lang. Gayunpaman, depende sa uri ng database na ginagamit mo, maaaring case-sensitive ang mga column at talahanayan. Bilang resulta, magandang kasanayan na palaging ituring ang lahat sa programming na parang case-sensitive. Kapag nagsusulat ng mga SQL query, karaniwang convention na ilagay ang mga keyword sa lahat ng upper-case na letra.

Ang query sa itaas ay magpapakita ng lahat ng lungsod. Isipin natin na nais lamang nating ipakita ang mga lungsod sa New Zealand. Kailangan natin ng isang uri ng filter. Ang SQL keyword para dito ay `WHERE`, o "kung saan ang isang bagay ay totoo".

```sql
SELECT city
FROM cities
WHERE country = 'New Zealand';

-- Output:
-- Auckland
```

## Pagsasama ng data

Hanggang ngayon, kumukuha tayo ng data mula sa isang talahanayan. Ngayon nais nating pagsamahin ang data mula sa parehong **cities** at **rainfall**. Ginagawa ito sa pamamagitan ng *pagsasama* sa kanila. Epektibo kang lilikha ng isang seam sa pagitan ng dalawang talahanayan, at itutugma ang mga halaga mula sa isang column mula sa bawat talahanayan.

Sa ating halimbawa, itutugma natin ang column na **city_id** sa **rainfall** sa column na **city_id** sa **cities**. Ito ay magtutugma sa halaga ng ulan sa kani-kanilang lungsod. Ang uri ng pagsasama na gagawin natin ay tinatawag na *inner* join, ibig sabihin kung may mga row na hindi tumutugma sa anumang bagay mula sa ibang talahanayan, hindi ito ipapakita. Sa ating kaso, ang bawat lungsod ay may dami ng ulan, kaya't lahat ay ipapakita.

Kunin natin ang dami ng ulan para sa 2019 para sa lahat ng ating lungsod.

Gagawin natin ito sa mga hakbang. Ang unang hakbang ay pagsamahin ang data sa pamamagitan ng pagtukoy sa mga column para sa seam - **city_id** na binanggit kanina.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
```

Ipinakita namin ang dalawang column na nais namin, at ang katotohanan na nais naming pagsamahin ang mga talahanayan sa pamamagitan ng **city_id**. Ngayon maaari nating idagdag ang `WHERE` statement upang i-filter lamang ang taon 2019.

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

Ang mga relational database ay nakasentro sa paghahati ng impormasyon sa pagitan ng maraming talahanayan na pagkatapos ay pinagsasama-sama para sa pagpapakita at pagsusuri. Nagbibigay ito ng mataas na antas ng flexibility upang magsagawa ng mga kalkulasyon at iba pang manipulasyon ng data. Nakita mo ang mga pangunahing konsepto ng relational database, at kung paano magsagawa ng pagsasama sa pagitan ng dalawang talahanayan.

## 🚀 Hamon

Maraming mga relational databases ang makikita sa internet. Maaari mong tuklasin ang data gamit ang mga kasanayan na natutunan mo sa itaas.

## Post-Lecture Quiz

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ds/quiz/9)

## Review & Self Study

Maraming mga mapagkukunan ang makikita sa [Microsoft Learn](https://docs.microsoft.com/learn?WT.mc_id=academic-77958-bethanycheum) para ipagpatuloy ang iyong pag-aaral sa mga konsepto ng SQL at relational database.

- [Ilarawan ang mga konsepto ng relational data](https://docs.microsoft.com//learn/modules/describe-concepts-of-relational-data?WT.mc_id=academic-77958-bethanycheum)
- [Simulan ang Pagtatanong gamit ang Transact-SQL](https://docs.microsoft.com//learn/paths/get-started-querying-with-transact-sql?WT.mc_id=academic-77958-bethanycheum) (Ang Transact-SQL ay isang bersyon ng SQL)
- [SQL na nilalaman sa Microsoft Learn](https://docs.microsoft.com/learn/browse/?products=azure-sql-database%2Csql-server&expanded=azure&WT.mc_id=academic-77958-bethanycheum)

## Takdang-Aralin

[Assignment Title](assignment.md)

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat sinisikap naming maging tumpak, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na mapagkakatiwalaang pinagmulan. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.