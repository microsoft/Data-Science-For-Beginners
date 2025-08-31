<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2f2d7693f28e4b2675f275e489dc5aac",
  "translation_date": "2025-08-30T18:13:59+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/assignment.md",
  "language_code": "sr"
}
-->
# Приказивање података о аеродромима

Добијена вам је [база података](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) изграђена на [SQLite](https://sqlite.org/index.html) која садржи информације о аеродромима. Шема базе је приказана испод. Користићете [SQLite екстензију](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) у [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) за приказивање информација о аеродромима у различитим градовима.

## Упутства

Да бисте започели задатак, потребно је да извршите неколико корака. Биће неопходно да инсталирате одређене алате и преузмете пример базе података.

### Подешавање система

Можете користити Visual Studio Code и SQLite екстензију за интеракцију са базом података.

1. Идите на [code.visualstudio.com](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) и пратите упутства за инсталацију Visual Studio Code-а
1. Инсталирајте [SQLite екстензију](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) како је наведено на страници Marketplace-а

### Преузимање и отварање базе података

Следећи корак је преузимање и отварање базе података.

1. Преузмите [датотеку базе података са GitHub-а](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) и сачувајте је у одређени директоријум
1. Отворите Visual Studio Code
1. Отворите базу података у SQLite екстензији тако што ћете изабрати **Ctl-Shift-P** (или **Cmd-Shift-P** на Mac-у) и укуцати `SQLite: Open database`
1. Изаберите **Choose database from file** и отворите датотеку **airports.db** коју сте претходно преузели
1. Након отварања базе података (нећете видети промену на екрану), креирајте нови прозор за упите тако што ћете изабрати **Ctl-Shift-P** (или **Cmd-Shift-P** на Mac-у) и укуцати `SQLite: New query`

Када се отвори нови прозор за упите, можете га користити за извршавање SQL наредби над базом података. Команду **Ctl-Shift-Q** (или **Cmd-Shift-Q** на Mac-у) можете користити за покретање упита над базом података.

> [!NOTE] За више информација о SQLite екстензији, можете консултовати [документацију](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum)

## Шема базе података

Шема базе података представља дизајн и структуру њених табела. База података **airports** садржи две табеле: `cities`, која садржи листу градова у Уједињеном Краљевству и Ирској, и `airports`, која садржи листу свих аеродрома. Пошто неки градови могу имати више аеродрома, креиране су две табеле за чување информација. У овом задатку користићете спајања (joins) за приказивање информација о различитим градовима.

| Градови (Cities) |
| ---------------- |
| id (PK, integer) |
| city (text)      |
| country (text)   |

| Аеродроми (Airports)             |
| -------------------------------- |
| id (PK, integer)                 |
| name (text)                      |
| code (text)                      |
| city_id (FK to id in **Cities**) |

## Задатак

Креирајте упите који враћају следеће информације:

1. сва имена градова у табели `Cities`
1. све градове у Ирској у табели `Cities`
1. сва имена аеродрома са њиховим градом и државом
1. све аеродроме у Лондону, Уједињено Краљевство

## Рубрика

| Изузетно | Задовољавајуће | Потребна побољшања |
| -------- | ------------- | ------------------ |

---

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем услуге за превођење помоћу вештачке интелигенције [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да обезбедимо тачност, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални превод од стране људи. Не сносимо одговорност за било каква погрешна тумачења или неспоразуме који могу произаћи из коришћења овог превода.