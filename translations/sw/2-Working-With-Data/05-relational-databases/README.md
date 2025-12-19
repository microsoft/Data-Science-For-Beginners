<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11739c7b40e7c6b16ad29e3df4e65862",
  "translation_date": "2025-12-19T11:57:49+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/README.md",
  "language_code": "sw"
}
-->
# Kufanya kazi na Data: Hifadhidata za Uhusiano

|![ Sketchnote na [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/05-RelationalData.png)|
|:---:|
| Kufanya kazi na Data: Hifadhidata za Uhusiano - _Sketchnote na [@nitya](https://twitter.com/nitya)_ |

Inawezekana umewahi kutumia lahajedwali hapo awali kuhifadhi taarifa. Ulikuwa na safu na nguzo, ambapo safu zilikuwa na taarifa (au data), na nguzo zilielezea taarifa (mara nyingine huitwa metadata). Hifadhidata ya uhusiano imejengwa juu ya kanuni hii kuu ya nguzo na safu katika meza, ikikuruhusu kuwa na taarifa zilizogawanyika katika meza nyingi. Hii inakuwezesha kufanya kazi na data tata zaidi, kuepuka kurudia, na kuwa na unyumbufu katika njia unazochunguza data. Hebu tuchunguze dhana za hifadhidata ya uhusiano.

## [Mtihani wa kabla ya somo](https://ff-quizzes.netlify.app/en/ds/quiz/8)

## Yote huanza na meza

Hifadhidata ya uhusiano ina meza kama msingi wake. Kama vile lahajedwali, meza ni mkusanyiko wa nguzo na safu. Safu ina data au taarifa tunayotaka kufanya kazi nayo, kama jina la mji au kiasi cha mvua. Nguzo zinaelezea data wanayohifadhi.

Hebu tuanze uchunguzi wetu kwa kuanzisha meza kuhifadhi taarifa kuhusu miji. Tunaweza kuanza na jina na nchi zao. Unaweza kuhifadhi hii katika meza kama ifuatavyo:

| Mji      | Nchi          |
| -------- | ------------- |
| Tokyo    | Japan         |
| Atlanta  | Marekani     |
| Auckland | New Zealand   |

Angalia majina ya nguzo ya **mji**, **nchi** na **idadi ya watu** yanaelezea data inayohifadhiwa, na kila safu ina taarifa kuhusu mji mmoja.

## Mapungufu ya njia ya meza moja

Inawezekana meza hapo juu inaonekana ya kawaida kwako. Hebu tuanze kuongeza data zaidi kwenye hifadhidata yetu inayokua - mvua ya kila mwaka (kwa milimita). Tutazingatia miaka 2018, 2019 na 2020. Ikiwa tungeiongeza kwa Tokyo, inaweza kuonekana kama hii:

| Mji   | Nchi    | Mwaka | Kiasi |
| ----- | ------- | ----- | ----- |
| Tokyo | Japan   | 2020  | 1690  |
| Tokyo | Japan   | 2019  | 1874  |
| Tokyo | Japan   | 2018  | 1445  |

Unaona nini kuhusu meza yetu? Unaweza kuona tunarudia jina na nchi ya mji mara kwa mara. Hii inaweza kuchukua nafasi kubwa ya kuhifadhi, na si lazima kuwa na nakala nyingi. Baada ya yote, Tokyo ina jina moja tu tunalotaka.

Sawa, hebu jaribu kitu kingine. Tuweke nguzo mpya kwa kila mwaka:

| Mji      | Nchi          | 2018 | 2019 | 2020 |
| -------- | ------------- | ---- | ---- | ---- |
| Tokyo    | Japan         | 1445 | 1874 | 1690 |
| Atlanta  | Marekani     | 1779 | 1111 | 1683 |
| Auckland | New Zealand   | 1386 | 942  | 1176 |

Ingawa hii inazuia kurudia safu, inaongeza changamoto nyingine. Tutahitaji kubadilisha muundo wa meza yetu kila wakati kuna mwaka mpya. Zaidi ya hayo, data yetu ikikua, kuwa na miaka kama nguzo kutafanya iwe vigumu kupata na kuhesabu thamani.

Hii ndiyo sababu tunahitaji meza nyingi na uhusiano. Kwa kugawanya data yetu tunaweza kuepuka kurudia na kuwa na unyumbufu zaidi katika jinsi tunavyofanya kazi na data.

## Dhana za uhusiano

Rudi kwenye data yetu na tuchague jinsi tunavyotaka kugawanya mambo. Tunajua tunataka kuhifadhi jina na nchi za miji yetu, hivyo hii itafanya kazi vizuri katika meza moja.

| Mji      | Nchi          |
| -------- | ------------- |
| Tokyo    | Japan         |
| Atlanta  | Marekani     |
| Auckland | New Zealand   |

Lakini kabla ya kuunda meza inayofuata, tunahitaji kujua jinsi ya kurejelea kila mji. Tunahitaji aina fulani ya kitambulisho, ID au (kwa istilahi za kiufundi za hifadhidata) ufunguo mkuu. Ufunguo mkuu ni thamani inayotumika kutambua safu moja maalum katika meza. Ingawa inaweza kutegemea thamani yenyewe (tunaweza kutumia jina la mji, kwa mfano), inapaswa karibu kila mara kuwa nambari au kitambulisho kingine. Hatutaki id kubadilika kamwe kwani itavunja uhusiano. Katika hali nyingi utapata ufunguo mkuu au id ni nambari inayojitengeneza yenyewe.

> ✅ Ufunguo mkuu mara nyingi huandikwa kama PK

### miji

| city_id | Mji      | Nchi          |
| ------- | -------- | ------------- |
| 1       | Tokyo    | Japan         |
| 2       | Atlanta  | Marekani     |
| 3       | Auckland | New Zealand   |

> ✅ Utaona tunatumia maneno "id" na "ufunguo mkuu" kwa kubadilishana katika somo hili. Dhana hapa zinahusiana na DataFrames, ambazo utazichunguza baadaye. DataFrames hazitumi istilahi ya "ufunguo mkuu", lakini utaona zina tabia kama hiyo.

Tukiwa na meza ya miji iliyoundwa, hebu tuhifadhi mvua. Badala ya kurudia taarifa kamili kuhusu mji, tunaweza kutumia id. Pia tunapaswa kuhakikisha meza mpya ina nguzo ya *id*, kwani meza zote zinapaswa kuwa na id au ufunguo mkuu.

### mvua

| rainfall_id | city_id | Mwaka | Kiasi |
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

Angalia nguzo ya **city_id** ndani ya meza mpya ya **mvua**. Nguzo hii ina thamani zinazorejelea ID katika meza ya **miji**. Kwa istilahi za kiufundi za data za uhusiano, hii huitwa **ufunguo wa kigeni**; ni ufunguo mkuu kutoka meza nyingine. Unaweza kuifikiria kama rejeleo au kidokezo. **city_id** 1 inarejelea Tokyo.

> [!NOTE] 
> Ufunguo wa kigeni mara nyingi huandikwa kama FK

## Kupata data

Tukiwa na data yetu imegawanyika katika meza mbili, unaweza kuwa unajiuliza jinsi tunavyopata data hiyo. Ikiwa tunatumia hifadhidata ya uhusiano kama MySQL, SQL Server au Oracle, tunaweza kutumia lugha inayoitwa Structured Query Language au SQL. SQL (mara nyingine inasemwa sequel) ni lugha ya kawaida inayotumika kupata na kubadilisha data katika hifadhidata ya uhusiano.

Kupata data unatumia amri `SELECT`. Kimsingi, unachagua nguzo unazotaka kuona **kutoka** kwenye meza zinazoihifadhi. Ikiwa ungependa kuonyesha majina tu ya miji, unaweza kutumia ifuatayo:

```sql
SELECT city
FROM cities;

-- Output:
-- Tokyo
-- Atlanta
-- Auckland
```

`SELECT` ni mahali unapoorodhesha nguzo, na `FROM` ni mahali unapoorodhesha meza.

> [!NOTE] 
> Sarufi ya SQL haina tofauti kati ya herufi kubwa na ndogo, maana `select` na `SELECT` ni sawa. Hata hivyo, kulingana na aina ya hifadhidata unayotumia, nguzo na meza zinaweza kuwa na tofauti ya herufi kubwa na ndogo. Kwa hiyo, ni desturi nzuri kutibu kila kitu katika programu kama kinavyotegemea herufi kubwa na ndogo. Wakati wa kuandika maswali ya SQL, kawaida ni kuweka maneno muhimu kwa herufi kubwa.

Swali hapo juu litaonyesha miji yote. Hebu fikiria tungependa kuonyesha miji tu ya New Zealand. Tunahitaji aina fulani ya kichujio. Neno la SQL kwa hili ni `WHERE`, au "ambapo kitu ni kweli".

```sql
SELECT city
FROM cities
WHERE country = 'New Zealand';

-- Output:
-- Auckland
```

## Kuunganisha data

Hadi sasa tumepata data kutoka meza moja. Sasa tunataka kuleta data pamoja kutoka **miji** na **mvua**. Hii hufanyika kwa *kuziunganisha* pamoja. Kwa ufanisi utaunda mshono kati ya meza mbili, na kulinganisha thamani kutoka nguzo ya kila meza.

Katika mfano wetu, tutalinganisha nguzo ya **city_id** katika **mvua** na nguzo ya **city_id** katika **miji**. Hii italinganisha thamani ya mvua na mji wake husika. Aina ya kuunganisha tutakayofanya huitwa *inner* join, maana ikiwa safu yoyote haitalingani na chochote kutoka meza nyingine haitatazamwa. Katika kesi yetu kila mji una mvua, hivyo kila kitu kitaonyeshwa.

Hebu tupate mvua ya mwaka 2019 kwa miji yote.

Tutafanya hivi kwa hatua. Hatua ya kwanza ni kuunganisha data kwa kuonyesha nguzo za mshono - **city_id** kama ilivyoangaziwa hapo awali.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
```

Tumeangazia nguzo mbili tunazotaka, na ukweli tunataka kuunganisha meza kwa **city_id**. Sasa tunaweza kuongeza kauli ya `WHERE` kuchuja mwaka 2019 tu.

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

## Muhtasari

Hifadhidata za uhusiano zinajikita katika kugawanya taarifa kati ya meza nyingi ambazo kisha huunganishwa tena kwa ajili ya kuonyeshwa na uchambuzi. Hii hutoa unyumbufu mkubwa kufanya mahesabu na kuendesha data kwa njia nyingine. Umeona dhana kuu za hifadhidata ya uhusiano, na jinsi ya kufanya kuunganisha kati ya meza mbili.

## 🚀 Changamoto

Kuna hifadhidata nyingi za uhusiano zinazopatikana mtandaoni. Unaweza kuchunguza data kwa kutumia ujuzi uliojifunza hapo juu.

## Mtihani wa Baada ya Somo

## [Mtihani wa baada ya somo](https://ff-quizzes.netlify.app/en/ds/quiz/9)

## Mapitio & Kujifunza Binafsi

Kuna rasilimali kadhaa zinazopatikana kwenye [Microsoft Learn](https://docs.microsoft.com/learn?WT.mc_id=academic-77958-bethanycheum) ili uendelee kuchunguza SQL na dhana za hifadhidata za uhusiano

- [Eleza dhana za data za uhusiano](https://docs.microsoft.com//learn/modules/describe-concepts-of-relational-data?WT.mc_id=academic-77958-bethanycheum)
- [Anza Kuuliza Maswali kwa Transact-SQL](https://docs.microsoft.com//learn/paths/get-started-querying-with-transact-sql?WT.mc_id=academic-77958-bethanycheum) (Transact-SQL ni toleo la SQL)
- [Yaliyomo ya SQL kwenye Microsoft Learn](https://docs.microsoft.com/learn/browse/?products=azure-sql-database%2Csql-server&expanded=azure&WT.mc_id=academic-77958-bethanycheum)

## Kazi ya Nyumbani

[Kuonyesha data ya uwanja wa ndege](assignment.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kiarifu cha Msamaha**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatubebei dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->