<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2f2d7693f28e4b2675f275e489dc5aac",
  "translation_date": "2025-08-26T14:34:04+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/assignment.md",
  "language_code": "bg"
}
-->
# Показване на данни за летища

Предоставена ви е [база данни](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db), изградена върху [SQLite](https://sqlite.org/index.html), която съдържа информация за летища. Схемата е показана по-долу. Ще използвате [SQLite разширението](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) в [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum), за да покажете информация за летищата в различни градове.

## Инструкции

За да започнете с задачата, ще трябва да изпълните няколко стъпки. Ще трябва да инсталирате необходимите инструменти и да изтеглите примерната база данни.

### Настройка на системата

Можете да използвате Visual Studio Code и разширението SQLite, за да взаимодействате с базата данни.

1. Отидете на [code.visualstudio.com](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) и следвайте инструкциите за инсталиране на Visual Studio Code
1. Инсталирайте [SQLite разширението](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum), както е описано на страницата в Marketplace

### Изтегляне и отваряне на базата данни

След това ще изтеглите и отворите базата данни.

1. Изтеглете [файла с базата данни от GitHub](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) и го запазете в директория
1. Отворете Visual Studio Code
1. Отворете базата данни в разширението SQLite, като изберете **Ctl-Shift-P** (или **Cmd-Shift-P** на Mac) и напишете `SQLite: Open database`
1. Изберете **Choose database from file** и отворете файла **airports.db**, който изтеглихте по-рано
1. След като отворите базата данни (няма да видите промяна на екрана), създайте нов прозорец за заявки, като изберете **Ctl-Shift-P** (или **Cmd-Shift-P** на Mac) и напишете `SQLite: New query`

След като прозорецът за заявки е отворен, можете да използвате SQL команди, за да изпълнявате заявки към базата данни. Можете да използвате командата **Ctl-Shift-Q** (или **Cmd-Shift-Q** на Mac), за да изпълнявате заявки към базата данни.

> [!NOTE] За повече информация относно разширението SQLite можете да се консултирате с [документацията](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum)

## Схема на базата данни

Схемата на базата данни представлява нейния дизайн и структура на таблиците. Базата данни **airports** има две таблици: `cities`, която съдържа списък с градове в Обединеното кралство и Ирландия, и `airports`, която съдържа списък с всички летища. Тъй като някои градове могат да имат повече от едно летище, са създадени две таблици за съхранение на информацията. В това упражнение ще използвате обединения (joins), за да покажете информация за различни градове.

| Градове           |
| ----------------- |
| id (PK, integer)  |
| city (text)       |
| country (text)    |

| Летища                          |
| -------------------------------- |
| id (PK, integer)                 |
| name (text)                      |
| code (text)                      |
| city_id (FK към id в **Cities**) |

## Задача

Създайте заявки, които връщат следната информация:

1. всички имена на градове в таблицата `Cities`
1. всички градове в Ирландия в таблицата `Cities`
1. всички имена на летища с техния град и държава
1. всички летища в Лондон, Обединеното кралство

## Оценяване

| Отлично | Задоволително | Нуждае се от подобрение |
| -------- | ------------- | ----------------------- |

---

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI услуга за превод [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи може да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Не носим отговорност за недоразумения или погрешни интерпретации, произтичащи от използването на този превод.