<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2f2d7693f28e4b2675f275e489dc5aac",
  "translation_date": "2025-08-30T18:14:44+00:00",
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

1. Завантажте [файл бази даних з GitHub](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) і збережіть його в каталозі
1. Відкрийте Visual Studio Code
1. Відкрийте базу даних у розширенні SQLite, натиснувши **Ctl-Shift-P** (або **Cmd-Shift-P** на Mac) і ввівши `SQLite: Open database`
1. Виберіть **Choose database from file** і відкрийте файл **airports.db**, який ви завантажили раніше
1. Після відкриття бази даних (на екрані не буде видно змін), створіть нове вікно запиту, натиснувши **Ctl-Shift-P** (або **Cmd-Shift-P** на Mac) і ввівши `SQLite: New query`

Після відкриття нове вікно запиту можна використовувати для виконання SQL-запитів до бази даних. Ви можете використовувати команду **Ctl-Shift-Q** (або **Cmd-Shift-Q** на Mac) для виконання запитів до бази даних.

> [!NOTE] Для отримання додаткової інформації про розширення SQLite ви можете ознайомитися з [документацією](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum)

## Схема бази даних

Схема бази даних — це її дизайн таблиць та структура. База даних **airports** має дві таблиці: `cities`, яка містить список міст у Великій Британії та Ірландії, і `airports`, яка містить список усіх аеропортів. Оскільки деякі міста можуть мати кілька аеропортів, було створено дві таблиці для зберігання інформації. У цьому завданні ви будете використовувати об'єднання таблиць для відображення інформації про різні міста.

| Міста             |
| ----------------- |
| id (PK, integer)  |
| city (text)       |
| country (text)    |

| Аеропорти                        |
| -------------------------------- |
| id (PK, integer)                 |
| name (text)                      |
| code (text)                      |
| city_id (FK до id у **Cities**)  |

## Завдання

Створіть запити для отримання наступної інформації:

1. усі назви міст у таблиці `Cities`
1. усі міста в Ірландії у таблиці `Cities`
1. усі назви аеропортів разом із їх містом та країною
1. усі аеропорти в Лондоні, Великій Британії

## Критерії оцінювання

| Відмінно | Достатньо | Потребує покращення |
| -------- | --------- | ------------------- |

---

**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, звертаємо вашу увагу, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ мовою оригіналу слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний переклад людиною. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.