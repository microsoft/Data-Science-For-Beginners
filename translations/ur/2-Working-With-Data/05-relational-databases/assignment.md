<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "25b37acdfb2452917c1aa2e2ca44317a",
  "translation_date": "2025-10-24T09:52:48+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/assignment.md",
  "language_code": "ur"
}
-->
# ہوائی اڈے کے ڈیٹا کو دکھانا

آپ کو ایک [ڈیٹا بیس](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) فراہم کیا گیا ہے جو [SQLite](https://sqlite.org/index.html) پر مبنی ہے اور ہوائی اڈوں کے بارے میں معلومات پر مشتمل ہے۔ اس کا اسکیما نیچے دکھایا گیا ہے۔ آپ [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) میں [SQLite extension](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) استعمال کریں گے تاکہ مختلف شہروں کے ہوائی اڈوں کی معلومات دکھا سکیں۔

## ہدایات

اس اسائنمنٹ کو شروع کرنے کے لیے آپ کو چند اقدامات کرنے ہوں گے۔ آپ کو کچھ ٹولز انسٹال کرنے اور نمونہ ڈیٹا بیس ڈاؤنلوڈ کرنے کی ضرورت ہوگی۔

### اپنے سسٹم کو سیٹ اپ کریں

آپ Visual Studio Code اور SQLite extension استعمال کر سکتے ہیں تاکہ ڈیٹا بیس کے ساتھ تعامل کریں۔

1. [code.visualstudio.com](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) پر جائیں اور Visual Studio Code انسٹال کرنے کے لیے ہدایات پر عمل کریں
1. [SQLite extension](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) کو انسٹال کریں جیسا کہ Marketplace صفحے پر بتایا گیا ہے

### ڈیٹا بیس ڈاؤنلوڈ کریں اور کھولیں

اگلے مرحلے میں آپ ڈیٹا بیس ڈاؤنلوڈ کریں گے اور اسے کھولیں گے۔

1. [GitHub سے ڈیٹا بیس فائل](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) ڈاؤنلوڈ کریں اور اسے کسی ڈائریکٹری میں محفوظ کریں
1. Visual Studio Code کھولیں
1. SQLite extension میں ڈیٹا بیس کھولنے کے لیے **Ctl-Shift-P** (یا میک پر **Cmd-Shift-P**) دبائیں اور `SQLite: Open database` ٹائپ کریں
1. **Choose database from file** منتخب کریں اور وہ **airports.db** فائل کھولیں جو آپ نے پہلے ڈاؤنلوڈ کی تھی
1. ڈیٹا بیس کھولنے کے بعد (آپ کو اسکرین پر کوئی اپڈیٹ نظر نہیں آئے گی)، ایک نیا کوئری ونڈو بنانے کے لیے **Ctl-Shift-P** (یا میک پر **Cmd-Shift-P**) دبائیں اور `SQLite: New query` ٹائپ کریں

ایک بار کھلنے کے بعد، نیا کوئری ونڈو ڈیٹا بیس کے خلاف SQL statements چلانے کے لیے استعمال کیا جا سکتا ہے۔ آپ **Ctl-Shift-Q** (یا میک پر **Cmd-Shift-Q**) کمانڈ استعمال کر سکتے ہیں تاکہ ڈیٹا بیس کے خلاف کوئریز چلائیں۔

> [!NOTE] 
> SQLite extension کے بارے میں مزید معلومات کے لیے، آپ [دستاویزات](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) دیکھ سکتے ہیں

## ڈیٹا بیس اسکیما

ڈیٹا بیس کا اسکیما اس کی ٹیبل ڈیزائن اور ساخت ہے۔ **airports** ڈیٹا بیس میں دو ٹیبلز ہیں، `cities`، جو کہ برطانیہ اور آئرلینڈ کے شہروں کی فہرست پر مشتمل ہے، اور `airports`، جو کہ تمام ہوائی اڈوں کی فہرست پر مشتمل ہے۔ چونکہ کچھ شہروں میں متعدد ہوائی اڈے ہو سکتے ہیں، اس معلومات کو محفوظ کرنے کے لیے دو ٹیبلز بنائی گئیں۔ اس مشق میں آپ مختلف شہروں کی معلومات دکھانے کے لیے جوائنز استعمال کریں گے۔

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

## اسائنمنٹ

ایسی کوئریز بنائیں جو درج ذیل معلومات واپس کریں:

1. `Cities` ٹیبل میں تمام شہروں کے نام
1. `Cities` ٹیبل میں آئرلینڈ کے تمام شہر
1. تمام ہوائی اڈوں کے نام ان کے شہر اور ملک کے ساتھ
1. لندن، برطانیہ کے تمام ہوائی اڈے

## روبریک

| مثالی | مناسب | بہتری کی ضرورت |
| --------- | -------- | ----------------- |

---

**اعلانِ لاتعلقی**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا غیر درستیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے لیے ہم ذمہ دار نہیں ہیں۔