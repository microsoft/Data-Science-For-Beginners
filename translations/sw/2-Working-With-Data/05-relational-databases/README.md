<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "80d80300002ef4e77cc7631d5904bd6e",
  "translation_date": "2025-10-25T19:02:38+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/README.md",
  "language_code": "sw"
}
-->
# Kufanya Kazi na Data: Hifadhidata za Uhusiano

|![ Sketchnote na [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/05-RelationalData.png)|
|:---:|
| Kufanya Kazi na Data: Hifadhidata za Uhusiano - _Sketchnote na [@nitya](https://twitter.com/nitya)_ |

Inawezekana umewahi kutumia lahajedwali hapo awali kuhifadhi taarifa. Ulipata seti ya safu na nguzo, ambapo safu zilikuwa na taarifa (au data), na nguzo zilielezea taarifa hiyo (wakati mwingine huitwa metadata). Hifadhidata ya uhusiano inajengwa juu ya kanuni hii ya msingi ya nguzo na safu kwenye meza, ikiruhusu uwe na taarifa zilizotawanyika kwenye meza nyingi. Hii inakuruhusu kufanya kazi na data ngumu zaidi, kuepuka kurudia, na kuwa na urahisi wa kuchunguza data. Hebu tuchunguze dhana za hifadhidata ya uhusiano.

## [Jaribio la awali la mihadhara](https://ff-quizzes.netlify.app/en/ds/quiz/8)

## Yote huanza na meza

Hifadhidata ya uhusiano ina meza kama msingi wake. Kama ilivyo kwa lahajedwali, meza ni mkusanyiko wa nguzo na safu. Safu ina data au taarifa tunayotaka kufanya kazi nayo, kama jina la mji au kiasi cha mvua. Nguzo zinaelezea data wanayohifadhi.

Hebu tuanze uchunguzi wetu kwa kuanzisha meza ya kuhifadhi taarifa kuhusu miji. Tunaweza kuanza na jina lao na nchi yao. Unaweza kuhifadhi hii kwenye meza kama ifuatavyo:

| Mji      | Nchi          |
| -------- | ------------- |
| Tokyo    | Japani        |
| Atlanta  | Marekani      |
| Auckland | New Zealand   |

Angalia majina ya nguzo **mji**, **nchi** na **idadi ya watu** yanaelezea data inayohifadhiwa, na kila safu ina taarifa kuhusu mji mmoja.

## Mapungufu ya mbinu ya meza moja

Inawezekana, meza hapo juu inaonekana kuwa ya kawaida kwako. Hebu tuanze kuongeza data ya ziada kwenye hifadhidata yetu inayokua - mvua ya kila mwaka (katika milimita). Tutazingatia miaka ya 2018, 2019 na 2020. Ikiwa tungeongeza kwa Tokyo, inaweza kuonekana kama hii:

| Mji   | Nchi   | Mwaka | Kiasi |
| ----- | ------ | ----- | ----- |
| Tokyo | Japani | 2020  | 1690  |
| Tokyo | Japani | 2019  | 1874  |
| Tokyo | Japani | 2018  | 1445  |

Je, unaona nini kuhusu meza yetu? Unaweza kugundua tunarudia jina na nchi ya mji mara kwa mara. Hiyo inaweza kuchukua nafasi nyingi za kuhifadhi, na kwa kiasi kikubwa si lazima kuwa na nakala nyingi. Baada ya yote, Tokyo ina jina moja tu tunalovutiwa nalo.

Sawa, hebu jaribu kitu kingine. Hebu tuongeze nguzo mpya kwa kila mwaka:

| Mji      | Nchi          | 2018 | 2019 | 2020 |
| -------- | ------------- | ---- | ---- | ---- |
| Tokyo    | Japani        | 1445 | 1874 | 1690 |
| Atlanta  | Marekani      | 1779 | 1111 | 1683 |
| Auckland | New Zealand   | 1386 | 942  | 1176 |

Ingawa hii inazuia kurudia kwa safu, inaongeza changamoto nyingine. Tunahitaji kubadilisha muundo wa meza yetu kila mara kunapokuwa na mwaka mpya. Zaidi ya hayo, kadri data yetu inavyokua, kuwa na miaka kama nguzo kutafanya iwe ngumu zaidi kupata na kuhesabu thamani.

Hii ndiyo sababu tunahitaji meza nyingi na uhusiano. Kwa kugawanya data yetu tunaweza kuepuka kurudia na kuwa na urahisi zaidi wa jinsi tunavyofanya kazi na data yetu.

## Dhana za uhusiano

Hebu turudi kwenye data yetu na kuamua jinsi tunavyotaka kuigawanya. Tunajua tunataka kuhifadhi jina na nchi ya miji yetu, kwa hivyo hii itafanya kazi vizuri zaidi kwenye meza moja.

| Mji      | Nchi          |
| -------- | ------------- |
| Tokyo    | Japani        |
| Atlanta  | Marekani      |
| Auckland | New Zealand   |

Lakini kabla ya kuunda meza inayofuata, tunahitaji kujua jinsi ya kurejelea kila mji. Tunahitaji aina fulani ya kitambulisho, ID au (katika istilahi za kiufundi za hifadhidata) ufunguo wa msingi. Ufunguo wa msingi ni thamani inayotumika kutambua safu moja maalum kwenye meza. Ingawa hii inaweza kutegemea thamani yenyewe (tunaweza kutumia jina la mji, kwa mfano), inapaswa kuwa namba au kitambulisho kingine. Hatutaki id ibadilike kamwe kwani itavunja uhusiano. Utapata katika hali nyingi ufunguo wa msingi au id itakuwa namba inayozalishwa kiotomatiki.

> ✅ Ufunguo wa msingi mara nyingi hufupishwa kama PK

### miji

| city_id | Mji      | Nchi          |
| ------- | -------- | ------------- |
| 1       | Tokyo    | Japani        |
| 2       | Atlanta  | Marekani      |
| 3       | Auckland | New Zealand   |

> ✅ Utagundua tunatumia maneno "id" na "ufunguo wa msingi" kwa kubadilishana wakati wa somo hili. Dhana hizi zinatumika kwa DataFrames, ambazo utachunguza baadaye. DataFrames hazitumii istilahi ya "ufunguo wa msingi", hata hivyo utagundua zinatenda kwa njia sawa.

Kwa meza yetu ya miji kuundwa, hebu tuhifadhi mvua. Badala ya kurudia taarifa kamili kuhusu mji, tunaweza kutumia id. Tunapaswa pia kuhakikisha meza mpya iliyoundwa ina safu ya *id*, kwani meza zote zinapaswa kuwa na id au ufunguo wa msingi.

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

Angalia safu ya **city_id** ndani ya meza mpya ya **mvua**. Safu hii ina thamani ambazo zinarejelea ID kwenye meza ya **miji**. Katika istilahi za kiufundi za data ya uhusiano, hii inaitwa **ufunguo wa kigeni**; ni ufunguo wa msingi kutoka meza nyingine. Unaweza kufikiria tu kama rejeleo au pointer. **city_id** 1 inarejelea Tokyo.

> [!NOTE] 
> Ufunguo wa kigeni mara nyingi hufupishwa kama FK

## Kupata data

Kwa data yetu kutenganishwa katika meza mbili, unaweza kuwa unajiuliza jinsi ya kuipata. Ikiwa tunatumia hifadhidata ya uhusiano kama MySQL, SQL Server au Oracle, tunaweza kutumia lugha inayoitwa Structured Query Language au SQL. SQL (wakati mwingine hutamkwa kama "sequel") ni lugha ya kawaida inayotumika kupata na kurekebisha data katika hifadhidata ya uhusiano.

Ili kupata data unatumia amri `SELECT`. Kwa msingi wake, unachagua nguzo unazotaka kuona kutoka kwenye meza ambazo zimo. Ikiwa ungependa kuonyesha tu majina ya miji, unaweza kutumia yafuatayo:

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
> Sintaksia ya SQL haibagui herufi kubwa na ndogo, ikimaanisha `select` na `SELECT` ni sawa. Hata hivyo, kulingana na aina ya hifadhidata unayotumia, nguzo na meza zinaweza kuwa na herufi kubwa na ndogo. Kwa hivyo, ni mazoea bora kila mara kutibu kila kitu katika programu kama kinachobagua herufi kubwa na ndogo. Wakati wa kuandika maswali ya SQL, kawaida ni kuweka maneno muhimu kwa herufi kubwa.

Swali hapo juu litaonyesha miji yote. Hebu tufikirie tunataka kuonyesha tu miji ya New Zealand. Tunahitaji aina fulani ya kichujio. Neno muhimu la SQL kwa hili ni `WHERE`, au "mahali ambapo kitu ni kweli".

```sql
SELECT city
FROM cities
WHERE country = 'New Zealand';

-- Output:
-- Auckland
```

## Kuunganisha data

Hadi sasa tumepata data kutoka meza moja. Sasa tunataka kuleta data pamoja kutoka kwa **miji** na **mvua**. Hii inafanywa kwa *kuunganisha* pamoja. Utaunda kiunganishi kati ya meza mbili, na kulinganisha thamani kutoka safu kutoka kila meza.

Katika mfano wetu, tutalinganisha safu ya **city_id** katika **mvua** na safu ya **city_id** katika **miji**. Hii italinganisha thamani ya mvua na mji wake husika. Aina ya muunganiko tutakaofanya ni kile kinachoitwa *muunganiko wa ndani*, ikimaanisha ikiwa safu yoyote haifani na chochote kutoka meza nyingine haitakuwa imeonyeshwa. Katika kesi yetu kila mji una mvua, kwa hivyo kila kitu kitaonyeshwa.

Hebu tupate mvua ya mwaka 2019 kwa miji yetu yote.

Tutaifanya hii kwa hatua. Hatua ya kwanza ni kuunganisha data pamoja kwa kuonyesha safu za kiunganishi - **city_id** kama ilivyoangaziwa hapo awali.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
```

Tumeelezea safu mbili tunazotaka, na ukweli tunataka kuunganisha meza pamoja kwa **city_id**. Sasa tunaweza kuongeza taarifa ya `WHERE` kuchuja mwaka wa 2019 pekee.

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

Hifadhidata za uhusiano zinazingatia kugawanya taarifa kati ya meza nyingi ambazo kisha huletwa pamoja kwa kuonyesha na kuchambua. Hii inatoa kiwango cha juu cha urahisi wa kufanya mahesabu na vinginevyo kudhibiti data. Umeona dhana za msingi za hifadhidata ya uhusiano, na jinsi ya kufanya muunganiko kati ya meza mbili.

## 🚀 Changamoto

Kuna hifadhidata nyingi za uhusiano zinazopatikana kwenye mtandao. Unaweza kuchunguza data kwa kutumia ujuzi uliyojifunza hapo juu.

## Jaribio la Baada ya Mihadhara

## [Jaribio la baada ya mihadhara](https://ff-quizzes.netlify.app/en/ds/quiz/9)

## Mapitio na Kujisomea

Kuna rasilimali kadhaa zinazopatikana kwenye [Microsoft Learn](https://docs.microsoft.com/learn?WT.mc_id=academic-77958-bethanycheum) kwa ajili ya kuendelea kuchunguza dhana za SQL na hifadhidata za uhusiano.

- [Eleza dhana za data ya uhusiano](https://docs.microsoft.com//learn/modules/describe-concepts-of-relational-data?WT.mc_id=academic-77958-bethanycheum)
- [Anza Kujifunza na Transact-SQL](https://docs.microsoft.com//learn/paths/get-started-querying-with-transact-sql?WT.mc_id=academic-77958-bethanycheum) (Transact-SQL ni toleo la SQL)
- [Maudhui ya SQL kwenye Microsoft Learn](https://docs.microsoft.com/learn/browse/?products=azure-sql-database%2Csql-server&expanded=azure&WT.mc_id=academic-77958-bethanycheum)

## Kazi ya Nyumbani

[Title ya Kazi ya Nyumbani](assignment.md)

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.