<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "25b37acdfb2452917c1aa2e2ca44317a",
  "translation_date": "2025-10-24T09:52:20+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/assignment.md",
  "language_code": "ru"
}
-->
# Отображение данных аэропортов

Вам предоставлена [база данных](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db), созданная на основе [SQLite](https://sqlite.org/index.html), которая содержит информацию об аэропортах. Схема базы данных представлена ниже. Вы будете использовать [расширение SQLite](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) в [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) для отображения информации об аэропортах различных городов.

## Инструкции

Чтобы начать выполнение задания, вам нужно выполнить несколько шагов. Вам потребуется установить необходимые инструменты и скачать пример базы данных.

### Настройка системы

Вы можете использовать Visual Studio Code и расширение SQLite для работы с базой данных.

1. Перейдите на [code.visualstudio.com](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) и следуйте инструкциям для установки Visual Studio Code
1. Установите расширение [SQLite extension](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum), следуя инструкциям на странице Marketplace

### Скачивание и открытие базы данных

Далее вам нужно скачать и открыть базу данных.

1. Скачайте [файл базы данных с GitHub](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) и сохраните его в папке
1. Откройте Visual Studio Code
1. Откройте базу данных в расширении SQLite, выбрав **Ctl-Shift-P** (или **Cmd-Shift-P** на Mac) и введя `SQLite: Open database`
1. Выберите **Choose database from file** и откройте файл **airports.db**, который вы скачали ранее
1. После открытия базы данных (на экране не будет видимых изменений), создайте новое окно для запросов, выбрав **Ctl-Shift-P** (или **Cmd-Shift-P** на Mac) и введя `SQLite: New query`

После открытия нового окна для запросов вы сможете выполнять SQL-запросы к базе данных. Вы можете использовать команду **Ctl-Shift-Q** (или **Cmd-Shift-Q** на Mac) для выполнения запросов к базе данных.

> [!NOTE] 
> Для получения дополнительной информации о расширении SQLite вы можете ознакомиться с [документацией](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum)

## Схема базы данных

Схема базы данных — это структура и дизайн её таблиц. База данных **airports** содержит две таблицы: `cities`, которая включает список городов в Великобритании и Ирландии, и `airports`, которая содержит список всех аэропортов. Поскольку некоторые города могут иметь несколько аэропортов, были созданы две таблицы для хранения информации. В этом упражнении вы будете использовать соединения для отображения информации о различных городах.

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

## Задание

Создайте запросы для получения следующей информации:

1. все названия городов из таблицы `Cities`
1. все города в Ирландии из таблицы `Cities`
1. все названия аэропортов с указанием их города и страны
1. все аэропорты в Лондоне, Великобритания

## Критерии оценки

| Превосходно | Удовлетворительно | Требует улучшения |
| ----------- | ----------------- | ----------------- |

---

**Отказ от ответственности**:  
Этот документ был переведен с использованием сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Хотя мы стремимся к точности, пожалуйста, учитывайте, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его родном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные интерпретации, возникающие в результате использования данного перевода.