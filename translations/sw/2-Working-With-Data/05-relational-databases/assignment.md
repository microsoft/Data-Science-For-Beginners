<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2f2d7693f28e4b2675f275e489dc5aac",
  "translation_date": "2025-08-26T14:32:28+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/assignment.md",
  "language_code": "sw"
}
-->
# Kuonyesha data za viwanja vya ndege

Umepewa [hifadhidata](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) iliyojengwa kwa [SQLite](https://sqlite.org/index.html) ambayo ina taarifa kuhusu viwanja vya ndege. Muundo wa hifadhidata umeonyeshwa hapa chini. Utatumia [kiendelezi cha SQLite](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) katika [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) kuonyesha taarifa kuhusu viwanja vya ndege vya miji mbalimbali.

## Maelekezo

Ili kuanza na kazi hii, utahitaji kufanya hatua kadhaa. Utahitaji kusakinisha baadhi ya zana na kupakua hifadhidata ya mfano.

### Sanidi mfumo wako

Unaweza kutumia Visual Studio Code na kiendelezi cha SQLite kuingiliana na hifadhidata.

1. Tembelea [code.visualstudio.com](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) na fuata maelekezo ya kusakinisha Visual Studio Code
1. Sakinisha [kiendelezi cha SQLite](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) kama ilivyoelekezwa kwenye ukurasa wa Marketplace

### Pakua na fungua hifadhidata

Hatua inayofuata ni kupakua na kufungua hifadhidata.

1. Pakua [faili ya hifadhidata kutoka GitHub](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) na ihifadhi kwenye folda
1. Fungua Visual Studio Code
1. Fungua hifadhidata katika kiendelezi cha SQLite kwa kuchagua **Ctl-Shift-P** (au **Cmd-Shift-P** kwenye Mac) na kuandika `SQLite: Open database`
1. Chagua **Choose database from file** na fungua faili ya **airports.db** uliyopakua awali
1. Baada ya kufungua hifadhidata (hutapata mabadiliko kwenye skrini), tengeneza dirisha jipya la maswali kwa kuchagua **Ctl-Shift-P** (au **Cmd-Shift-P** kwenye Mac) na kuandika `SQLite: New query`

Baada ya kufungua, dirisha jipya la maswali linaweza kutumika kuendesha kauli za SQL dhidi ya hifadhidata. Unaweza kutumia amri **Ctl-Shift-Q** (au **Cmd-Shift-Q** kwenye Mac) kuendesha maswali dhidi ya hifadhidata.

> [!NOTE] Kwa maelezo zaidi kuhusu kiendelezi cha SQLite, unaweza kushauriana na [nyaraka](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum)

## Muundo wa hifadhidata

Muundo wa hifadhidata ni mpangilio wa jedwali na muundo wake. Hifadhidata ya **airports** ina majedwali mawili, `cities`, ambalo lina orodha ya miji nchini Uingereza na Ireland, na `airports`, ambalo lina orodha ya viwanja vyote vya ndege. Kwa sababu baadhi ya miji inaweza kuwa na viwanja vya ndege vingi, majedwali mawili yalitengenezwa kuhifadhi taarifa. Katika zoezi hili utatumia "joins" kuonyesha taarifa za miji mbalimbali.

| Cities           |
| ---------------- |
| id (PK, integer) |
| city (text)      |
| country (text)   |

| Airports                         |
| -------------------------------- |
| id (PK, integer)                 |
| name (text)                      |
| code (text)                      |
| city_id (FK to id in **Cities**) |

## Kazi

Tengeneza maswali ya kurudisha taarifa zifuatazo:

1. majina yote ya miji katika jedwali la `Cities`
1. miji yote nchini Ireland katika jedwali la `Cities`
1. majina yote ya viwanja vya ndege pamoja na mji na nchi zao
1. viwanja vyote vya ndege vilivyopo London, Uingereza

## Rubric

| Bora Zaidi | Inayotosheleza | Inayohitaji Uboreshaji |
| ---------- | -------------- | ---------------------- |

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya kutafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.