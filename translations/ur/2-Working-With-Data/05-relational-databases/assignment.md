<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2f2d7693f28e4b2675f275e489dc5aac",
  "translation_date": "2025-08-27T08:23:25+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/assignment.md",
  "language_code": "ur"
}
-->
# ہوائی اڈوں کے ڈیٹا کو ظاہر کرنا

آپ کو ایک [ڈیٹا بیس](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) فراہم کیا گیا ہے جو [SQLite](https://sqlite.org/index.html) پر مبنی ہے اور اس میں ہوائی اڈوں کی معلومات شامل ہیں۔ اس کا اسکیما نیچے دکھایا گیا ہے۔ آپ [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) میں [SQLite extension](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) کا استعمال کرتے ہوئے مختلف شہروں کے ہوائی اڈوں کی معلومات ظاہر کریں گے۔

## ہدایات

اس اسائنمنٹ کو شروع کرنے کے لیے، آپ کو چند اقدامات کرنے ہوں گے۔ آپ کو کچھ ٹولز انسٹال کرنے اور نمونہ ڈیٹا بیس ڈاؤن لوڈ کرنے کی ضرورت ہوگی۔

### اپنے سسٹم کو سیٹ اپ کریں

آپ Visual Studio Code اور SQLite extension کا استعمال کرتے ہوئے ڈیٹا بیس کے ساتھ تعامل کر سکتے ہیں۔

1. [code.visualstudio.com](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) پر جائیں اور Visual Studio Code انسٹال کرنے کے لیے ہدایات پر عمل کریں۔
1. [SQLite extension](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) کو انسٹال کریں جیسا کہ مارکیٹ پلیس صفحے پر ہدایت دی گئی ہے۔

### ڈیٹا بیس ڈاؤن لوڈ کریں اور کھولیں

اب آپ ڈیٹا بیس کو ڈاؤن لوڈ کریں گے اور کھولیں گے۔

1. [GitHub سے ڈیٹا بیس فائل](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) ڈاؤن لوڈ کریں اور اسے کسی ڈائریکٹری میں محفوظ کریں۔
1. Visual Studio Code کھولیں۔
1. SQLite extension میں ڈیٹا بیس کھولنے کے لیے **Ctl-Shift-P** (یا میک پر **Cmd-Shift-P**) دبائیں اور `SQLite: Open database` ٹائپ کریں۔
1. **Choose database from file** منتخب کریں اور وہ **airports.db** فائل کھولیں جو آپ نے پہلے ڈاؤن لوڈ کی تھی۔
1. ڈیٹا بیس کھولنے کے بعد (آپ کو اسکرین پر کوئی اپ ڈیٹ نظر نہیں آئے گا)، ایک نیا کوئری ونڈو بنانے کے لیے **Ctl-Shift-P** (یا میک پر **Cmd-Shift-P**) دبائیں اور `SQLite: New query` ٹائپ کریں۔

ایک بار کھلنے کے بعد، نیا کوئری ونڈو ڈیٹا بیس کے خلاف SQL اسٹیٹمنٹس چلانے کے لیے استعمال کیا جا سکتا ہے۔ آپ **Ctl-Shift-Q** (یا میک پر **Cmd-Shift-Q**) کمانڈ کا استعمال کرتے ہوئے ڈیٹا بیس کے خلاف کوئریز چلا سکتے ہیں۔

> [!NOTE] SQLite extension کے بارے میں مزید معلومات کے لیے، آپ [دستاویزات](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) کا حوالہ دے سکتے ہیں۔

## ڈیٹا بیس اسکیما

ڈیٹا بیس کا اسکیما اس کی ٹیبل ڈیزائن اور ساخت ہے۔ **airports** ڈیٹا بیس میں دو ٹیبلز ہیں، `cities`، جس میں برطانیہ اور آئرلینڈ کے شہروں کی فہرست شامل ہے، اور `airports`، جس میں تمام ہوائی اڈوں کی فہرست شامل ہے۔ چونکہ کچھ شہروں میں ایک سے زیادہ ہوائی اڈے ہو سکتے ہیں، اس معلومات کو محفوظ کرنے کے لیے دو ٹیبلز بنائی گئیں۔ اس مشق میں آپ مختلف شہروں کے لیے معلومات ظاہر کرنے کے لیے جوائنز کا استعمال کریں گے۔

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

| مثالی       | مناسب       | بہتری کی ضرورت |
| ----------- | ----------- | --------------- |

---

**ڈس کلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے پوری کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستگی ہو سکتی ہیں۔ اصل دستاویز، جو اس کی اصل زبان میں ہے، کو مستند ماخذ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے لیے ہم ذمہ دار نہیں ہیں۔