<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "25b37acdfb2452917c1aa2e2ca44317a",
  "translation_date": "2025-10-24T09:52:38+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/assignment.md",
  "language_code": "fa"
}
-->
# نمایش داده‌های فرودگاه

یک [پایگاه داده](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) مبتنی بر [SQLite](https://sqlite.org/index.html) که شامل اطلاعاتی درباره فرودگاه‌ها است، در اختیار شما قرار گرفته است. طرح پایگاه داده در زیر نمایش داده شده است. شما از [افزونه SQLite](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) در [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) برای نمایش اطلاعات فرودگاه‌های شهرهای مختلف استفاده خواهید کرد.

## دستورالعمل‌ها

برای شروع این تمرین، باید چند مرحله را انجام دهید. نیاز به نصب ابزارهایی دارید و باید پایگاه داده نمونه را دانلود کنید.

### تنظیم سیستم

می‌توانید از Visual Studio Code و افزونه SQLite برای تعامل با پایگاه داده استفاده کنید.

1. به [code.visualstudio.com](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) بروید و دستورالعمل‌ها را برای نصب Visual Studio Code دنبال کنید.
1. افزونه [SQLite extension](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) را مطابق دستورالعمل‌های صفحه Marketplace نصب کنید.

### دانلود و باز کردن پایگاه داده

در مرحله بعد، پایگاه داده را دانلود و باز کنید.

1. [فایل پایگاه داده را از GitHub دانلود کنید](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) و آن را در یک پوشه ذخیره کنید.
1. Visual Studio Code را باز کنید.
1. پایگاه داده را در افزونه SQLite باز کنید. برای این کار، **Ctl-Shift-P** (یا **Cmd-Shift-P** در مک) را فشار دهید و `SQLite: Open database` را تایپ کنید.
1. گزینه **Choose database from file** را انتخاب کنید و فایل **airports.db** که قبلاً دانلود کرده‌اید را باز کنید.
1. پس از باز کردن پایگاه داده (هیچ به‌روزرسانی روی صفحه نمایش داده نمی‌شود)، یک پنجره جدید برای پرس‌وجو ایجاد کنید. برای این کار، **Ctl-Shift-P** (یا **Cmd-Shift-P** در مک) را فشار دهید و `SQLite: New query` را تایپ کنید.

پس از باز شدن، می‌توانید از پنجره پرس‌وجوی جدید برای اجرای دستورات SQL در پایگاه داده استفاده کنید. برای اجرای پرس‌وجوها در پایگاه داده، می‌توانید از دستور **Ctl-Shift-Q** (یا **Cmd-Shift-Q** در مک) استفاده کنید.

> [!NOTE] 
> برای اطلاعات بیشتر درباره افزونه SQLite، می‌توانید به [مستندات](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) مراجعه کنید.

## طرح پایگاه داده

طرح پایگاه داده طراحی و ساختار جدول‌های آن است. پایگاه داده **airports** شامل دو جدول است: `cities` که لیستی از شهرهای بریتانیا و ایرلند را در بر دارد، و `airports` که لیست تمام فرودگاه‌ها را شامل می‌شود. از آنجا که ممکن است برخی شهرها چندین فرودگاه داشته باشند، دو جدول برای ذخیره اطلاعات ایجاد شده‌اند. در این تمرین از اتصال جداول برای نمایش اطلاعات شهرهای مختلف استفاده خواهید کرد.

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

## تمرین

پرس‌وجوهایی ایجاد کنید که اطلاعات زیر را بازگردانند:

1. تمام نام‌های شهرها در جدول `Cities`
1. تمام شهرهای ایرلند در جدول `Cities`
1. تمام نام‌های فرودگاه‌ها همراه با شهر و کشورشان
1. تمام فرودگاه‌های لندن، بریتانیا

## معیار ارزیابی

| عالی       | کافی       | نیاز به بهبود |
| --------- | --------- | ------------- |

---

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما تلاش می‌کنیم دقت را حفظ کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌ها باشند. سند اصلی به زبان اصلی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئولیتی در قبال سوء تفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.