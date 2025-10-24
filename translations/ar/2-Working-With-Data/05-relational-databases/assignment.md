<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "25b37acdfb2452917c1aa2e2ca44317a",
  "translation_date": "2025-10-24T09:52:28+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/assignment.md",
  "language_code": "ar"
}
-->
# عرض بيانات المطارات

تم تزويدك بـ [قاعدة بيانات](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) مبنية على [SQLite](https://sqlite.org/index.html) تحتوي على معلومات حول المطارات. يتم عرض المخطط أدناه. ستستخدم [امتداد SQLite](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) في [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) لعرض معلومات حول مطارات المدن المختلفة.

## التعليمات

لبدء المهمة، ستحتاج إلى تنفيذ بعض الخطوات. ستحتاج إلى تثبيت بعض الأدوات وتنزيل قاعدة البيانات النموذجية.

### إعداد النظام الخاص بك

يمكنك استخدام Visual Studio Code وامتداد SQLite للتفاعل مع قاعدة البيانات.

1. انتقل إلى [code.visualstudio.com](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) واتبع التعليمات لتثبيت Visual Studio Code
1. قم بتثبيت [امتداد SQLite](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) كما هو موضح في صفحة السوق

### تنزيل وفتح قاعدة البيانات

بعد ذلك، ستقوم بتنزيل وفتح قاعدة البيانات.

1. قم بتنزيل [ملف قاعدة البيانات من GitHub](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) واحفظه في دليل
1. افتح Visual Studio Code
1. افتح قاعدة البيانات في امتداد SQLite عن طريق تحديد **Ctl-Shift-P** (أو **Cmd-Shift-P** على جهاز Mac) وكتابة `SQLite: Open database`
1. اختر **Choose database from file** وافتح ملف **airports.db** الذي قمت بتنزيله مسبقًا
1. بعد فتح قاعدة البيانات (لن ترى تحديثًا على الشاشة)، قم بإنشاء نافذة استعلام جديدة عن طريق تحديد **Ctl-Shift-P** (أو **Cmd-Shift-P** على جهاز Mac) وكتابة `SQLite: New query`

بمجرد الفتح، يمكن استخدام نافذة الاستعلام الجديدة لتشغيل عبارات SQL ضد قاعدة البيانات. يمكنك استخدام الأمر **Ctl-Shift-Q** (أو **Cmd-Shift-Q** على جهاز Mac) لتشغيل الاستعلامات ضد قاعدة البيانات.

> [!NOTE] 
> لمزيد من المعلومات حول امتداد SQLite، يمكنك الرجوع إلى [التوثيق](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum)

## مخطط قاعدة البيانات

مخطط قاعدة البيانات هو تصميم الجداول وهيكلها. تحتوي قاعدة بيانات **airports** على جدولين، `cities`، الذي يحتوي على قائمة المدن في المملكة المتحدة وأيرلندا، و `airports`، الذي يحتوي على قائمة جميع المطارات. نظرًا لأن بعض المدن قد تحتوي على مطارات متعددة، تم إنشاء جدولين لتخزين المعلومات. في هذا التمرين، ستستخدم الربط لعرض المعلومات للمدن المختلفة.

| المدن            |
| ---------------- |
| id (PK, integer) |
| city (text)      |
| country (text)   |

| المطارات                        |
| -------------------------------- |
| id (PK, integer)                 |
| name (text)                      |
| code (text)                      |
| city_id (FK to id in **Cities**) |

## المهمة

قم بإنشاء استعلامات لإرجاع المعلومات التالية:

1. جميع أسماء المدن في جدول `Cities`
1. جميع المدن في أيرلندا في جدول `Cities`
1. جميع أسماء المطارات مع المدينة والبلد الخاص بها
1. جميع المطارات في لندن، المملكة المتحدة

## التقييم

| متميز | كافٍ | يحتاج إلى تحسين |
| --------- | -------- | ----------------- |

---

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي. للحصول على معلومات حاسمة، يُوصى بالترجمة البشرية الاحترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسير خاطئ ينشأ عن استخدام هذه الترجمة.