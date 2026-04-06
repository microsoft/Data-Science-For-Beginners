# បង្ហាញទិន្នន័យអាកាសយានដ្ឋាន

អ្នកត្រូវបានផ្តល់ជូន [មូលដ្ឋានទិន្នន័យ](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) ដែលត្រូវបានបង្កើតលើ [SQLite](https://sqlite.org/index.html) ដែលមានព័ត៌មានអំពីអាកាសយានដ្ឋាន។ សchema ត្រូវបានបង្ហាញខាងក្រោម។ អ្នកនឹងប្រើ [ភាគបន្ថែម SQLite](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) នៅក្នុង [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) ដើម្បីបង្ហាញព័ត៌មានអំពីអាកាសយានដ្ឋាននៃទីក្រុងផ្សេងៗ។

## សេចក្តីណែនាំ

ដើម្បីចាប់ផ្តើមការងារ អ្នកត្រូវធ្វើជំហ៊ានពីរបី។ អ្នកត្រូវតែដំឡើងឧបករណ៍ខ្លះ និងទាញយកមូលដ្ឋានទិន្នន័យគំរូ។

### ដំឡើងប្រព័ន្ធរបស់អ្នក

អ្នកអាចប្រើ Visual Studio Code និងភាគបន្ថែម SQLite ដើម្បីធ្វើប្រតិបត្តិការជាមួយមូលដ្ឋានទិន្នន័យ។

1. ទៅកាន់ [code.visualstudio.com](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) ហើយអនុវត្តន៍តាមការណែនាំដើម្បីដំឡើង Visual Studio Code
1. ដំឡើងភាគបន្ថែម [SQLite extension](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) ដោយតាមការណែនាំនៅលើទំព័រ Marketplace

### ទាញយក និងបើកមូលដ្ឋានទិន្នន័យ

បន្ទាប់មក អ្នកនឹងទាញយក និងបើកមូលដ្ឋានទិន្នន័យ។

1. ទាញយក [ឯកសារមូលដ្ឋានទិន្នន័យពី GitHub](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) ហើយរក្សាទុកវាទៅថតឯកសារ
1. បើក Visual Studio Code
1. បើកមូលដ្ឋានទិន្នន័យនៅក្នុងភាគបន្ថែម SQLite ដោយជ្រើស **Ctl-Shift-P** (ឬ **Cmd-Shift-P** លើ Mac) ហើយវាយ `SQLite: Open database`
1. ជ្រើស **Choose database from file** ហើយបើកឯកសារ **airports.db** ដែលអ្នកបានទាញយកមុននេះ
1. បន្ទាប់ពីបើកមូលដ្ឋានទិន្នន័យ (អ្នកនឹងមិនឃើញការផ្លាស់ប្ដូរនៅលើអេក្រង់ទេ) បង្កើតផ្ទាំងស៊ើបអង្កេតថ្មីដោយជ្រើស **Ctl-Shift-P** (ឬ **Cmd-Shift-P** លើ Mac) ហើយវាយ `SQLite: New query`

ពេលដែលបើករួច ផ្ទាំងស៊ើបអង្កេត ថ្មីអាចប្រើដើម្បីរត់ពាក្យបញ្ជា SQL ទៅលើមូលដ្ឋានទិន្នន័យ។ អ្នកអាចប្រើពាក្យបញ្ជា **Ctl-Shift-Q** (ឬ **Cmd-Shift-Q** លើ Mac) ដើម្បីរត់សំណួរទៅលើមូលដ្ឋានទិន្នន័យ។

> [!NOTE]  
> សម្រាប់ព័ត៌មានបន្ថែមអំពីភាគបន្ថែម SQLite អ្នកអាចពិនិត្យមើល [ឯកសារ](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum)

## សេចក្តីឆ្លងរបស់មូលដ្ឋានទិន្នន័យ

សេចក្តីឆ្លងរបស់មូលដ្ឋានទិន្នន័យគឺជារចនាសម្ព័ន្ធតារាងនិងរចនាបថ។ មូលដ្ឋានទិន្នន័យ **airports** មានតារាងពីរគឺ `cities` ដែលមានបញ្ជីទីក្រុងនៅចក្រភពអង់គ្លេស និងអៀរឡង់ និង `airports` ដែលមានបញ្ជីអាកាសយានដ្ឋានទាំងអស់។ ពីព្រោះមានទីក្រុងខ្លះមានអាកាសយានដ្ឋានច្រើនជាងមួយ តារាងពីរបានត្រូវបង្កើតឡើងដើម្បីរក្សាទុកព័ត៌មាន។ ក្នុងការហាត់នេះ អ្នកនឹងប្រើ joins ដើម្បីបង្ហាញព័ត៌មានសម្រាប់ទីក្រុងផ្សេងៗ។

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

## ការងារ

បង្កើតសំណួរដើម្បីត្រឡប់ព័ត៌មានដូចតទៅ៖

1. ឈ្មោះទីក្រុងទាំងអស់នៅក្នុងតារាង `Cities`
1. ទីក្រុងទាំងអស់នៅក្នុងប្រទេសអៀរឡង់នៅតារាង `Cities`
1. ឈ្មោះអាកាសយានដ្ឋានទាំងអស់ជាមួយទីក្រុង និងប្រទេសរបស់វា
1. អាកាសយានដ្ឋានទាំងអស់នៅទីក្រុងឡុងដ៍ ប្រទេសចក្រភពអង់គ្លេស

## គោលការណ៍វាយតម្លៃ

| ដំណើរការល្អ | គ្រប់គ្រាន់ | ត្រូវកែលម្អ |
| --------- | -------- | ----------------- |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:  
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំខិតខំប្រឹងប្រែងសម្រាប់ភាពត្រឹមត្រូវ កុំភ្លេចថាការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុស ឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមនៅក្នុងភាសាមូលដ្ឋានគួរត្រូវបានគិតថាជាប្រេសកម្មដ៏មានអំណាច។ សម្រាប់ព័ត៌មានសំខាន់ៗ ការបកប្រែដោយមនុស្សជំនាញគឺត្រូវបានសំរាប់។ យើងខ្ញុំមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំនិងការបកប្រើខុសពីការប្រើប្រាស់ការបកប្រែនេះឡើយ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->