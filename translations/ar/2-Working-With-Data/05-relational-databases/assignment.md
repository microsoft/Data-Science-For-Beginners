<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2f2d7693f28e4b2675f275e489dc5aac",
  "translation_date": "2025-08-27T08:23:08+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/assignment.md",
  "language_code": "ar"
}
-->
# عرض بيانات المطارات

تم تزويدك بـ [قاعدة بيانات](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) مبنية على [SQLite](https://sqlite.org/index.html) تحتوي على معلومات حول المطارات. يتم عرض المخطط أدناه. ستستخدم [إضافة SQLite](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) في [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) لعرض معلومات حول مطارات مدن مختلفة.

## التعليمات

لبدء المهمة، ستحتاج إلى تنفيذ بعض الخطوات. ستحتاج إلى تثبيت بعض الأدوات وتنزيل قاعدة البيانات النموذجية.

### إعداد النظام الخاص بك

يمكنك استخدام Visual Studio Code وإضافة SQLite للتفاعل مع قاعدة البيانات.

1. انتقل إلى [code.visualstudio.com](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) واتبع التعليمات لتثبيت Visual Studio Code
1. قم بتثبيت [إضافة SQLite](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) كما هو موضح في صفحة Marketplace

### تنزيل وفتح قاعدة البيانات

بعد ذلك، ستقوم بتنزيل وفتح قاعدة البيانات.

1. قم بتنزيل [ملف قاعدة البيانات من GitHub](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) واحفظه في مجلد
1. افتح Visual Studio Code
1. افتح قاعدة البيانات في إضافة SQLite عن طريق اختيار **Ctl-Shift-P** (أو **Cmd-Shift-P** على جهاز Mac) وكتابة `SQLite: Open database`
1. اختر **Choose database from file** وافتح ملف **airports.db** الذي قمت بتنزيله مسبقًا
1. بعد فتح قاعدة البيانات (لن ترى تحديثًا على الشاشة)، قم بإنشاء نافذة استعلام جديدة عن طريق اختيار **Ctl-Shift-P** (أو **Cmd-Shift-P** على جهاز Mac) وكتابة `SQLite: New query`

بمجرد الفتح، يمكن استخدام نافذة الاستعلام الجديدة لتشغيل عبارات SQL على قاعدة البيانات. يمكنك استخدام الأمر **Ctl-Shift-Q** (أو **Cmd-Shift-Q** على جهاز Mac) لتشغيل الاستعلامات على قاعدة البيانات.

> [!NOTE] لمزيد من المعلومات حول إضافة SQLite، يمكنك الرجوع إلى [التوثيق](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum)

## مخطط قاعدة البيانات

مخطط قاعدة البيانات هو تصميمها وهيكلها الجدولي. تحتوي قاعدة بيانات **airports** على جدولين، `cities` الذي يحتوي على قائمة بالمدن في المملكة المتحدة وأيرلندا، و`airports` الذي يحتوي على قائمة بجميع المطارات. نظرًا لأن بعض المدن قد تحتوي على مطارات متعددة، تم إنشاء جدولين لتخزين المعلومات. في هذا التمرين، ستستخدم الربط (joins) لعرض معلومات لمدن مختلفة.

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
1. جميع أسماء المطارات مع مدينتها وبلدها
1. جميع المطارات في لندن، المملكة المتحدة

## معايير التقييم

| متميز       | مقبول       | يحتاج إلى تحسين |
| ----------- | ----------- | --------------- |

---

**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار المستند الأصلي بلغته الأصلية هو المصدر الموثوق. للحصول على معلومات حساسة أو هامة، يُوصى بالاستعانة بترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة تنشأ عن استخدام هذه الترجمة.