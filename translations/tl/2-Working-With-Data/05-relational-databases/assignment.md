<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "25b37acdfb2452917c1aa2e2ca44317a",
  "translation_date": "2025-10-24T09:57:18+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/assignment.md",
  "language_code": "tl"
}
-->
# Pagpapakita ng datos ng paliparan

Binigyan ka ng isang [database](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) na ginawa gamit ang [SQLite](https://sqlite.org/index.html) na naglalaman ng impormasyon tungkol sa mga paliparan. Ang schema ay ipinapakita sa ibaba. Gagamitin mo ang [SQLite extension](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) sa [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) upang ipakita ang impormasyon tungkol sa mga paliparan sa iba't ibang lungsod.

## Mga Instruksyon

Upang simulan ang gawain, kailangan mong gawin ang ilang hakbang. Kailangan mong mag-install ng ilang mga tool at i-download ang sample na database.

### I-setup ang iyong sistema

Maaari mong gamitin ang Visual Studio Code at ang SQLite extension upang makipag-ugnayan sa database.

1. Pumunta sa [code.visualstudio.com](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) at sundin ang mga tagubilin upang i-install ang Visual Studio Code
1. I-install ang [SQLite extension](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) extension ayon sa mga tagubilin sa Marketplace page

### I-download at buksan ang database

Susunod, i-download at buksan ang database.

1. I-download ang [database file mula sa GitHub](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) at i-save ito sa isang direktoryo
1. Buksan ang Visual Studio Code
1. Buksan ang database sa SQLite extension sa pamamagitan ng pagpili ng **Ctl-Shift-P** (o **Cmd-Shift-P** sa Mac) at i-type ang `SQLite: Open database`
1. Piliin ang **Choose database from file** at buksan ang **airports.db** file na iyong na-download
1. Pagkatapos buksan ang database (hindi ka makakakita ng update sa screen), gumawa ng bagong query window sa pamamagitan ng pagpili ng **Ctl-Shift-P** (o **Cmd-Shift-P** sa Mac) at i-type ang `SQLite: New query`

Kapag bukas na, magagamit ang bagong query window upang magpatakbo ng mga SQL statement laban sa database. Maaari mong gamitin ang command na **Ctl-Shift-Q** (o **Cmd-Shift-Q** sa Mac) upang magpatakbo ng mga query laban sa database.

> [!NOTE] 
> Para sa karagdagang impormasyon tungkol sa SQLite extension, maaari mong konsultahin ang [documentation](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum)

## Schema ng Database

Ang schema ng isang database ay ang disenyo at istruktura ng mga table nito. Ang **airports** database ay may dalawang table, `cities`, na naglalaman ng listahan ng mga lungsod sa United Kingdom at Ireland, at `airports`, na naglalaman ng listahan ng lahat ng paliparan. Dahil ang ilang lungsod ay maaaring may maraming paliparan, dalawang table ang ginawa upang i-store ang impormasyon. Sa aktibidad na ito, gagamit ka ng joins upang ipakita ang impormasyon para sa iba't ibang lungsod.

| Mga Lungsod       |
| ----------------- |
| id (PK, integer)  |
| city (text)       |
| country (text)    |

| Mga Paliparan                     |
| --------------------------------- |
| id (PK, integer)                 |
| name (text)                      |
| code (text)                      |
| city_id (FK sa id sa **Cities**) |

## Gawain

Gumawa ng mga query upang makuha ang sumusunod na impormasyon:

1. lahat ng pangalan ng lungsod sa `Cities` table
1. lahat ng lungsod sa Ireland sa `Cities` table
1. lahat ng pangalan ng paliparan kasama ang kanilang lungsod at bansa
1. lahat ng paliparan sa London, United Kingdom

## Rubric

| Napakahusay | Katanggap-tanggap | Kailangan ng Pagpapabuti |
| ----------- | ----------------- | ------------------------ |

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat sinisikap naming maging tumpak, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.