<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2f2d7693f28e4b2675f275e489dc5aac",
  "translation_date": "2025-08-24T20:56:26+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/assignment.md",
  "language_code": "fa"
}
-->
# نمایش داده‌های فرودگاه

یک [پایگاه داده](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) مبتنی بر [SQLite](https://sqlite.org/index.html) که شامل اطلاعاتی درباره فرودگاه‌ها است، در اختیار شما قرار گرفته است. طرح پایگاه داده در زیر نمایش داده شده است. شما از [افزونه SQLite](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) در [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) برای نمایش اطلاعات فرودگاه‌های شهرهای مختلف استفاده خواهید کرد.

## دستورالعمل‌ها

برای شروع این تمرین، باید چند مرحله را انجام دهید. لازم است ابزارهایی نصب کنید و پایگاه داده نمونه را دانلود کنید.

### تنظیم سیستم

شما می‌توانید از Visual Studio Code و افزونه SQLite برای تعامل با پایگاه داده استفاده کنید.

1. به [code.visualstudio.com](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) بروید و دستورالعمل‌ها را برای نصب Visual Studio Code دنبال کنید.
1. افزونه [SQLite extension](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) را طبق دستورالعمل‌های صفحه Marketplace نصب کنید.

### دانلود و باز کردن پایگاه داده

در مرحله بعد، پایگاه داده را دانلود و باز کنید.

1. فایل [پایگاه داده از GitHub](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) را دانلود کرده و در یک پوشه ذخیره کنید.
1. Visual Studio Code را باز کنید.
1. پایگاه داده را در افزونه SQLite باز کنید. برای این کار، **Ctl-Shift-P** (یا **Cmd-Shift-P** در مک) را فشار دهید و عبارت `SQLite: Open database` را تایپ کنید.
1. گزینه **Choose database from file** را انتخاب کرده و فایل **airports.db** که قبلاً دانلود کرده‌اید را باز کنید.
1. پس از باز کردن پایگاه داده (هیچ تغییری روی صفحه مشاهده نخواهید کرد)، یک پنجره جدید برای نوشتن کوئری ایجاد کنید. برای این کار، **Ctl-Shift-P** (یا **Cmd-Shift-P** در مک) را فشار دهید و عبارت `SQLite: New query` را تایپ کنید.

پس از باز شدن پنجره جدید، می‌توانید دستورات SQL را روی پایگاه داده اجرا کنید. برای اجرای کوئری‌ها، از دستور **Ctl-Shift-Q** (یا **Cmd-Shift-Q** در مک) استفاده کنید.

> [!NOTE] برای اطلاعات بیشتر درباره افزونه SQLite، می‌توانید به [مستندات](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) مراجعه کنید.

## طرح پایگاه داده

طرح پایگاه داده، طراحی و ساختار جدول‌های آن است. پایگاه داده **airports** شامل دو جدول است: `cities` که لیستی از شهرهای بریتانیا و ایرلند را در بر دارد، و `airports` که لیستی از تمام فرودگاه‌ها را شامل می‌شود. از آنجا که برخی شهرها ممکن است چندین فرودگاه داشته باشند، دو جدول برای ذخیره اطلاعات ایجاد شده‌اند. در این تمرین، شما از اتصال جداول برای نمایش اطلاعات شهرهای مختلف استفاده خواهید کرد.

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

کوئری‌هایی ایجاد کنید که اطلاعات زیر را بازگردانند:

1. تمام نام‌های شهرها در جدول `Cities`
1. تمام شهرهای ایرلند در جدول `Cities`
1. تمام نام‌های فرودگاه‌ها همراه با شهر و کشورشان
1. تمام فرودگاه‌های لندن، بریتانیا

## معیار ارزیابی

| عالی       | قابل قبول | نیاز به بهبود |
| --------- | -------- | ------------- |

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما تلاش می‌کنیم دقت را حفظ کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان اصلی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما هیچ مسئولیتی در قبال سوءتفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.