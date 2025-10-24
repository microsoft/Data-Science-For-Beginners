<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "25b37acdfb2452917c1aa2e2ca44317a",
  "translation_date": "2025-10-24T09:59:17+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/assignment.md",
  "language_code": "uk"
}
-->
# Відображення даних про аеропорти

Вам надано [базу даних](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db), створену на основі [SQLite](https://sqlite.org/index.html), яка містить інформацію про аеропорти. Схема бази даних наведена нижче. Ви будете використовувати [розширення SQLite](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) у [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) для відображення інформації про аеропорти різних міст.

## Інструкції

Щоб розпочати виконання завдання, вам потрібно виконати кілька кроків. Вам необхідно встановити деякі інструменти та завантажити приклад бази даних.

### Налаштування системи

Ви можете використовувати Visual Studio Code та розширення SQLite для взаємодії з базою даних.

1. Перейдіть на [code.visualstudio.com](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) і дотримуйтесь інструкцій для встановлення Visual Studio Code
1. Встановіть [розширення SQLite](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum), як зазначено на сторінці Marketplace

### Завантаження та відкриття бази даних

Далі вам потрібно завантажити та відкрити базу даних.

1. Завантажте [файл бази даних з GitHub](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) і збережіть його в папці
1. Відкрийте Visual Studio Code
1. Відкрийте базу даних у розширенні SQLite, натиснувши **Ctl-Shift-P** (або **Cmd-Shift-P** на Mac) і ввівши `SQLite: Open database`
1. Виберіть **Choose database from file** і відкрийте файл **airports.db**, який ви завантажили раніше
1. Після відкриття бази даних (на екрані не буде видно змін), створіть нове вікно запиту, натиснувши **Ctl-Shift-P** (або **Cmd-Shift-P** на Mac) і ввівши `SQLite: New query`

Після відкриття нове вікно запиту можна використовувати для виконання SQL-запитів до бази даних. Ви можете використовувати команду **Ctl-Shift-Q** (або **Cmd-Shift-Q** на Mac) для виконання запитів до бази даних.

> [!NOTE] 
> Для отримання додаткової інформації про розширення SQLite ви можете ознайомитися з [документацією](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum)

## Схема бази даних

Схема бази даних — це її дизайн і структура таблиць. База даних **airports** має дві таблиці: `cities`, яка містить список міст у Великій Британії та Ірландії, і `airports`, яка містить список усіх аеропортів. Оскільки деякі міста можуть мати кілька аеропортів, було створено дві таблиці для зберігання інформації. У цьому завданні ви будете використовувати об'єднання таблиць для відображення інформації про різні міста.

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

## Завдання

Створіть запити для отримання наступної інформації:

1. усі назви міст у таблиці `Cities`
1. усі міста в Ірландії у таблиці `Cities`
1. усі назви аеропортів разом із їх містом і країною
1. усі аеропорти в Лондоні, Великій Британії

## Критерії оцінювання

| Відмінно | Достатньо | Потребує покращення |
| -------- | --------- | ------------------- |

---

**Відмова від відповідальності**:  
Цей документ був перекладений за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ на його рідній мові слід вважати авторитетним джерелом. Для критичної інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникають внаслідок використання цього перекладу.