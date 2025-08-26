<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "870a0086adbc313a8eea5489bdcb2522",
  "translation_date": "2025-08-26T14:28:15+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/README.md",
  "language_code": "sw"
}
-->
# Kufanya Kazi na Data: Hifadhidata za Kihusiano

|![ Sketchnote na [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/05-RelationalData.png)|
|:---:|
| Kufanya Kazi na Data: Hifadhidata za Kihusiano - _Sketchnote na [@nitya](https://twitter.com/nitya)_ |

Inawezekana umewahi kutumia lahajedwali hapo awali kuhifadhi taarifa. Uliona seti ya safu na nguzo, ambapo safu zilikuwa na taarifa (au data), na nguzo zilielezea taarifa hiyo (wakati mwingine huitwa metadata). Hifadhidata ya kihusiano inajengwa juu ya kanuni hii ya msingi ya nguzo na safu katika jedwali, ikikuruhusu kuwa na taarifa iliyosambazwa katika majedwali mengi. Hii inakuruhusu kufanya kazi na data ngumu zaidi, kuepuka kurudia, na kuwa na urahisi katika jinsi unavyotafuta data. Hebu tuchunguze dhana za hifadhidata ya kihusiano.

## [Jaribio la awali la somo](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/8)

## Yote huanza na majedwali

Hifadhidata ya kihusiano ina msingi wake katika majedwali. Kama ilivyo kwenye lahajedwali, jedwali ni mkusanyiko wa nguzo na safu. Safu ina data au taarifa tunayotaka kufanya kazi nayo, kama jina la jiji au kiasi cha mvua. Nguzo zinaelezea data wanayohifadhi.

Hebu tuanze uchunguzi wetu kwa kuunda jedwali la kuhifadhi taarifa kuhusu miji. Tunaweza kuanza na majina yao na nchi zao. Unaweza kuhifadhi hii katika jedwali kama ifuatavyo:

| Jiji     | Nchi          |
| -------- | ------------- |
| Tokyo    | Japani        |
| Atlanta  | Marekani      |
| Auckland | New Zealand   |

Angalia majina ya nguzo **jiji**, **nchi**, na **idadi ya watu** yanavyoelezea data inayohifadhiwa, na kila safu ina taarifa kuhusu jiji moja.

## Mapungufu ya mbinu ya jedwali moja

Inawezekana, jedwali hapo juu linaonekana kuwa la kawaida kwako. Hebu tuanze kuongeza data ya ziada kwenye hifadhidata yetu inayokua - mvua ya kila mwaka (katika milimita). Tutazingatia miaka ya 2018, 2019, na 2020. Ikiwa tungeongeza kwa Tokyo, inaweza kuonekana kama hii:

| Jiji  | Nchi   | Mwaka | Kiasi  |
| ----- | -------| ----- | ------ |
| Tokyo | Japani | 2020  | 1690   |
| Tokyo | Japani | 2019  | 1874   |
| Tokyo | Japani | 2018  | 1445   |

Unaona nini kuhusu jedwali letu? Unaweza kugundua tunarudia jina na nchi ya jiji mara kwa mara. Hii inaweza kuchukua nafasi nyingi za kuhifadhi, na kwa kiasi kikubwa si lazima kuwa na nakala nyingi. Baada ya yote, Tokyo lina jina moja tu tunalovutiwa nalo.

Sawa, hebu tujaribu kitu kingine. Hebu tuongeze nguzo mpya kwa kila mwaka:

| Jiji     | Nchi          | 2018 | 2019 | 2020 |
| -------- | ------------- | ---- | ---- | ---- |
| Tokyo    | Japani        | 1445 | 1874 | 1690 |
| Atlanta  | Marekani      | 1779 | 1111 | 1683 |
| Auckland | New Zealand   | 1386 | 942  | 1176 |

Ingawa hii inazuia kurudia safu, inaongeza changamoto nyingine. Tunahitaji kurekebisha muundo wa jedwali letu kila mara kuna mwaka mpya. Aidha, data yetu inavyokua, kuwa na miaka kama nguzo itafanya iwe ngumu zaidi kupata na kuhesabu thamani.

Hii ndiyo sababu tunahitaji majedwali mengi na mahusiano. Kwa kugawanya data yetu tunaweza kuepuka kurudia na kuwa na urahisi zaidi katika jinsi tunavyofanya kazi na data yetu.

## Dhana za mahusiano

Hebu turudi kwenye data yetu na kuamua jinsi tunavyotaka kuigawanya. Tunajua tunataka kuhifadhi jina na nchi za miji yetu, kwa hivyo hii itafanya kazi vizuri zaidi katika jedwali moja.

| Jiji     | Nchi          |
| -------- | ------------- |
| Tokyo    | Japani        |
| Atlanta  | Marekani      |
| Auckland | New Zealand   |

Lakini kabla ya kuunda jedwali linalofuata, tunahitaji kujua jinsi ya kurejelea kila jiji. Tunahitaji aina fulani ya kitambulisho, ID au (katika istilahi za hifadhidata za kiufundi) ufunguo wa msingi. Ufunguo wa msingi ni thamani inayotumika kutambua safu moja maalum katika jedwali. Ingawa hii inaweza kutegemea thamani yenyewe (tunaweza kutumia jina la jiji, kwa mfano), inapaswa kuwa namba au kitambulisho kingine. Hatutaki ID ibadilike kwani itavunja uhusiano. Utakuta katika hali nyingi ufunguo wa msingi au ID itakuwa namba inayozalishwa kiotomatiki.

> ✅ Ufunguo wa msingi mara nyingi hufupishwa kama PK

### miji

| city_id | Jiji     | Nchi          |
| ------- | -------- | ------------- |
| 1       | Tokyo    | Japani        |
| 2       | Atlanta  | Marekani      |
| 3       | Auckland | New Zealand   |

> ✅ Utagundua tunatumia maneno "id" na "ufunguo wa msingi" kwa kubadilishana wakati wa somo hili. Dhana hizi zinatumika kwa DataFrames, ambazo utachunguza baadaye. DataFrames hazitumii istilahi ya "ufunguo wa msingi", hata hivyo utagundua zinatenda kwa njia sawa.

Kwa jedwali letu la miji kuundwa, hebu tuhifadhi mvua. Badala ya kurudia taarifa kamili kuhusu jiji, tunaweza kutumia ID. Tunapaswa pia kuhakikisha jedwali jipya lililoundwa lina safu ya *id*, kwani majedwali yote yanapaswa kuwa na ID au ufunguo wa msingi.

### mvua

| rainfall_id | city_id | Mwaka | Kiasi  |
| ----------- | ------- | ----- | ------ |
| 1           | 1       | 2018  | 1445   |
| 2           | 1       | 2019  | 1874   |
| 3           | 1       | 2020  | 1690   |
| 4           | 2       | 2018  | 1779   |
| 5           | 2       | 2019  | 1111   |
| 6           | 2       | 2020  | 1683   |
| 7           | 3       | 2018  | 1386   |
| 8           | 3       | 2019  | 942    |
| 9           | 3       | 2020  | 1176   |

Angalia safu ya **city_id** ndani ya jedwali jipya la **mvua**. Safu hii ina thamani zinazorejelea ID katika jedwali la **miji**. Katika istilahi za kiufundi za data ya kihusiano, hii inaitwa **ufunguo wa kigeni**; ni ufunguo wa msingi kutoka jedwali lingine. Unaweza kufikiria tu kama rejeleo au pointer. **city_id** 1 inarejelea Tokyo.

> [!NOTE] Ufunguo wa kigeni mara nyingi hufupishwa kama FK

## Kupata data

Kwa data yetu kugawanywa katika majedwali mawili, unaweza kuwa unajiuliza jinsi tunavyopata. Ikiwa tunatumia hifadhidata ya kihusiano kama MySQL, SQL Server au Oracle, tunaweza kutumia lugha inayoitwa Structured Query Language au SQL. SQL (wakati mwingine hutamkwa "sequel") ni lugha ya kawaida inayotumika kupata na kurekebisha data katika hifadhidata ya kihusiano.

Ili kupata data unatumia amri `SELECT`. Kwa msingi wake, unachagua nguzo unazotaka kuona kutoka kwenye jedwali wanapopatikana. Ikiwa ungependa kuonyesha tu majina ya miji, unaweza kutumia yafuatayo:

```sql
SELECT city
FROM cities;

-- Output:
-- Tokyo
-- Atlanta
-- Auckland
```

`SELECT` ni mahali unapoorodhesha nguzo, na `FROM` ni mahali unapoorodhesha majedwali.

> [NOTE] Sintaksia ya SQL haizingatii herufi kubwa na ndogo, ikimaanisha `select` na `SELECT` ni sawa. Hata hivyo, kulingana na aina ya hifadhidata unayotumia, nguzo na majedwali yanaweza kuzingatia herufi kubwa na ndogo. Kwa hivyo, ni mazoea bora kila mara kuchukulia kila kitu katika programu kama kinazingatia herufi kubwa na ndogo. Wakati wa kuandika maswali ya SQL, kawaida ni kuweka maneno muhimu kwa herufi kubwa.

Swali hapo juu litaonyesha miji yote. Hebu tufikirie tunataka kuonyesha miji ya New Zealand pekee. Tunahitaji aina fulani ya kichujio. Neno muhimu la SQL kwa hili ni `WHERE`, au "mahali ambapo kitu ni kweli".

```sql
SELECT city
FROM cities
WHERE country = 'New Zealand';

-- Output:
-- Auckland
```

## Kuunganisha data

Hadi sasa tumepata data kutoka jedwali moja. Sasa tunataka kuleta data pamoja kutoka **miji** na **mvua**. Hii inafanywa kwa *kuunganisha* majedwali pamoja. Kimsingi utaunda mshono kati ya majedwali mawili, na kulinganisha thamani kutoka safu kutoka kila jedwali.

Katika mfano wetu, tutalinganisha safu ya **city_id** katika **mvua** na safu ya **city_id** katika **miji**. Hii italinganisha thamani ya mvua na jiji lake husika. Aina ya muunganiko tutakaofanya inaitwa *inner join*, ikimaanisha ikiwa safu yoyote haifani na kitu chochote kutoka jedwali lingine haitakuwa imeonyeshwa. Katika kesi yetu kila jiji lina mvua, kwa hivyo kila kitu kitaonyeshwa.

Hebu tupate mvua ya mwaka 2019 kwa miji yetu yote.

Tunaenda kufanya hili kwa hatua. Hatua ya kwanza ni kuunganisha data pamoja kwa kuonyesha safu za mshono - **city_id** kama ilivyoangaziwa hapo awali.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
```

Tumeelezea safu mbili tunazotaka, na ukweli kwamba tunataka kuunganisha majedwali pamoja kwa **city_id**. Sasa tunaweza kuongeza taarifa ya `WHERE` ili kuchuja mwaka wa 2019 pekee.

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

Hifadhidata za kihusiano zinazingatia kugawanya taarifa kati ya majedwali mengi ambayo kisha huletwa pamoja kwa kuonyesha na kuchambua. Hii inatoa kiwango cha juu cha urahisi wa kufanya mahesabu na vinginevyo kudhibiti data. Umeona dhana za msingi za hifadhidata ya kihusiano, na jinsi ya kufanya muunganiko kati ya majedwali mawili.

## 🚀 Changamoto

Kuna hifadhidata nyingi za kihusiano zinazopatikana kwenye mtandao. Unaweza kuchunguza data kwa kutumia ujuzi uliyojifunza hapo juu.

## Jaribio la Baada ya Somo

## [Jaribio la baada ya somo](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/9)

## Mapitio na Kujisomea

Kuna rasilimali kadhaa zinazopatikana kwenye [Microsoft Learn](https://docs.microsoft.com/learn?WT.mc_id=academic-77958-bethanycheum) kwa ajili ya kuendelea kuchunguza dhana za SQL na hifadhidata za kihusiano

- [Eleza dhana za data ya kihusiano](https://docs.microsoft.com//learn/modules/describe-concepts-of-relational-data?WT.mc_id=academic-77958-bethanycheum)
- [Anza Kujifunza Kuuliza na Transact-SQL](https://docs.microsoft.com//learn/paths/get-started-querying-with-transact-sql?WT.mc_id=academic-77958-bethanycheum) (Transact-SQL ni toleo la SQL)
- [Maudhui ya SQL kwenye Microsoft Learn](https://docs.microsoft.com/learn/browse/?products=azure-sql-database%2Csql-server&expanded=azure&WT.mc_id=academic-77958-bethanycheum)

## Kazi

[Kichwa cha Kazi](assignment.md)

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.