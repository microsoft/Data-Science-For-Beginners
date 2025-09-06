<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c182e87f9f80be7e7cdffc7b40bbfccf",
  "translation_date": "2025-09-05T20:10:21+00:00",
  "source_file": "2-Working-With-Data/06-non-relational/README.md",
  "language_code": "my"
}
-->
# ဒေတာနှင့်အလုပ်လုပ်ခြင်း - မဟုတ်သောဆက်နွယ်မှုရှိသော ဒေတာ

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/06-NoSQL.png)|
|:---:|
|NoSQL ဒေတာနှင့်အလုပ်လုပ်ခြင်း - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

## [Pre-Lecture Quiz](https://ff-quizzes.netlify.app/en/ds/quiz/10)

ဒေတာသည် ဆက်နွယ်မှုရှိသော ဒေတာဘေ့စ်များတွင်သာ ကန့်သတ်ထားခြင်းမရှိပါ။ ဒီသင်ခန်းစာမှာ မဟုတ်သောဆက်နွယ်မှုရှိသော ဒေတာကို အဓိကထားပြီး စာရင်းဇယားနှင့် NoSQL အခြေခံများကို လေ့လာပါမည်။

## စာရင်းဇယားများ

စာရင်းဇယားများသည် ဒေတာကို သိမ်းဆည်းရန်နှင့် ရှာဖွေရန် လူကြိုက်များသောနည်းလမ်းတစ်ခုဖြစ်ပြီး စတင်ရန်အလုပ်နည်းပါသည်။ ဒီသင်ခန်းစာမှာ စာရင်းဇယား၏ အခြေခံအစိတ်အပိုင်းများ၊ ဖော်မြူလာများနှင့် ဖင်ခွန်းများကို လေ့လာပါမည်။ ဥပမာများကို Microsoft Excel ဖြင့် ဖော်ပြမည်ဖြစ်ပြီး အခြားစာရင်းဇယားဆော့ဖ်ဝဲများနှင့် နှိုင်းယှဉ်ပါက အစိတ်အပိုင်းများနှင့် ခေါင်းစဉ်များသည် နာမည်နှင့် လုပ်ဆောင်မှုအဆင့်များမှာ ဆင်တူပါမည်။

![An empty Microsoft Excel workbook with two worksheets](../../../../2-Working-With-Data/06-non-relational/images/parts-of-spreadsheet.png)

စာရင်းဇယားသည် ဖိုင်တစ်ခုဖြစ်ပြီး ကွန်ပျူတာ၊ စက်ပစ္စည်း၊ သို့မဟုတ် cloud-based ဖိုင်စနစ်၏ ဖိုင်စနစ်တွင် ဝင်ရောက်နိုင်ပါသည်။ ဆော့ဖ်ဝဲကို browser-based ဖြစ်နိုင်သလို ကွန်ပျူတာတွင် ထည့်သွင်းရမည့် application သို့မဟုတ် app အဖြစ် ဒေါင်းလုဒ်လုပ်ရမည်ဖြစ်နိုင်သည်။ Excel တွင် ဒီဖိုင်များကို **workbooks** ဟုလည်း သတ်မှတ်ထားပြီး ဒီသင်ခန်းစာတစ်ခုလုံးတွင် ဒီနာမည်ကို အသုံးပြုပါမည်။

Workbook တစ်ခုတွင် **worksheets** တစ်ခု သို့မဟုတ် အများအပြားပါဝင်ပြီး worksheet တစ်ခုစီကို tabs ဖြင့် အမည်ပေးထားသည်။ Worksheet အတွင်းတွင် **cells** ဟုခေါ်သော စတုရန်းများရှိပြီး ဒေတာကို ထည့်သွင်းထားသည်။ Cell သည် row နှင့် column တစ်ခု၏ ချိတ်ဆက်မှုဖြစ်ပြီး column များကို အက္ခရာများဖြင့် အမည်ပေးထားပြီး row များကို ကိန်းဂဏန်းများဖြင့် အမည်ပေးထားသည်။ စာရင်းဇယားတစ်ချို့တွင် cell အတွင်းရှိ ဒေတာကို ဖော်ပြရန် ပထမဆုံး row များတွင် headers ပါဝင်နိုင်သည်။

Excel workbook ၏ အခြေခံအစိတ်အပိုင်းများနှင့်အတူ [Microsoft Templates](https://templates.office.com/) မှ inventory ကို အခြေခံထားသော ဥပမာတစ်ခုကို အသုံးပြု၍ စာရင်းဇယား၏ အပိုင်းများကို ဆက်လက်လေ့လာပါမည်။

### Inventory ကို စီမံခြင်း

"InventoryExample" ဟုခေါ်သော စာရင်းဇယားဖိုင်သည် inventory အတွင်းရှိ items များကို ဖော်ပြထားသော format စာရင်းဇယားဖြစ်ပြီး "Inventory List", "Inventory Pick List" နှင့် "Bin Lookup" ဟုခေါ်သော tabs များပါဝင်သော worksheets သုံးခုပါဝင်သည်။ Inventory List worksheet ၏ Row 4 သည် header ဖြစ်ပြီး header column အတွင်းရှိ cell တစ်ခုစီ၏ အဖွဲ့အစည်းကို ဖော်ပြသည်။

![A highlighted formula from an example inventory list in Microsoft Excel](../../../../2-Working-With-Data/06-non-relational/images/formula-excel.png)

တစ်ခါတစ်ရံ cell တစ်ခုသည် ၎င်း၏တန်ဖိုးကို ဖော်ဆောင်ရန် အခြား cell များ၏ တန်ဖိုးများကို အခြေခံထားသည်။ Inventory List စာရင်းဇယားသည် inventory အတွင်းရှိ item တစ်ခုစီ၏ ကုန်ကျစရိတ်ကို ထိန်းသိမ်းထားသော်လည်း inventory အတွင်းရှိ အားလုံး၏တန်ဖိုးကို သိရန်လိုအပ်ပါက [**Formulas**](https://support.microsoft.com/en-us/office/overview-of-formulas-34519a4e-1e8d-4f4b-84d4-d642c4f63263) သည် cell data တွင် လုပ်ဆောင်မှုများကို ဆောင်ရွက်ပြီး ဤဥပမာတွင် inventory ၏တန်ဖိုးကိုတွက်ရန် အသုံးပြုသည်။ ဤစာရင်းဇယားသည် Inventory Value column တွင် formula ကို အသုံးပြု၍ QTY header အောက်ရှိ အရေအတွက်နှင့် COST header အောက်ရှိ ကုန်ကျစရိတ်ကို များပြားစေခြင်းဖြင့် item တစ်ခုစီ၏တန်ဖိုးကိုတွက်ချက်သည်။ Cell ကို double click လုပ်ခြင်း သို့မဟုတ် highlight လုပ်ခြင်းဖြင့် formula ကို ကြည့်နိုင်သည်။ Formula များသည် အမှန်ခြင်းဖြင့် စတင်ပြီး calculation သို့မဟုတ် operation ကို ဆက်လက်လုပ်ဆောင်သည်။

![A highlighted function from an example inventory list in Microsoft Excel](../../../../2-Working-With-Data/06-non-relational/images/function-excel.png)

Inventory Value ၏တန်ဖိုးအားလုံးကို ပေါင်းပြီး ၎င်း၏စုစုပေါင်းတန်ဖိုးကို ရရှိရန် အခြား formula ကို အသုံးပြုနိုင်သည်။ ဤကို cell တစ်ခုစီကို ပေါင်းပြီး စုစုပေါင်းကို ရရှိရန်တွက်ချက်နိုင်သော်လည်း ၎င်းသည် အလုပ်များသောအလုပ်ဖြစ်နိုင်သည်။ Excel တွင် [**functions**](https://support.microsoft.com/en-us/office/sum-function-043e1c7d-7726-4e80-8f32-07b23e057f89) သို့မဟုတ် cell values တွင် calculation များကို ဆောင်ရွက်ရန် အကြိုသတ်မှတ်ထားသော formula များရှိသည်။ Functions တွင် arguments လိုအပ်ပြီး calculation များကို ဆောင်ရွက်ရန်လိုအပ်သောတန်ဖိုးများဖြစ်သည်။ Functions တွင် arguments အများအပြားလိုအပ်ပါက ၎င်းတို့ကို အတိအကျအစီအစဉ်ဖြင့် ရေးရန်လိုအပ်ပြီး function သည် တန်ဖိုးမှန်ကန်စွာတွက်ချက်မည်မဟုတ်ပါ။ ဤဥပမာတွင် SUM function ကို အသုံးပြုပြီး Inventory Value ၏တန်ဖိုးများကို argument အဖြစ်အသုံးပြု၍ row 3, column B (B3 ဟုလည်းခေါ်သည်) အောက်တွင် ဖော်ပြထားသောစုစုပေါင်းကို ရရှိသည်။

## NoSQL

NoSQL သည် မဟုတ်သောဆက်နွယ်မှုရှိသော ဒေတာကို သိမ်းဆည်းရန် နည်းလမ်းများကို အုပ်စုဖွဲ့ထားသော စကားလုံးဖြစ်ပြီး "non-SQL", "non-relational" သို့မဟုတ် "not only SQL" ဟု အဓိပ္ပါယ်ဖွင့်ဆိုနိုင်သည်။ ဒီအမျိုးအစား database စနစ်များကို အမျိုးအစား ၄ မျိုးအဖြစ် အုပ်စုဖွဲ့နိုင်သည်။

![Graphical representation of a key-value data store showing 4 unique numerical keys that are associated with 4 various values](../../../../2-Working-With-Data/06-non-relational/images/kv-db.png)
> Source from [Michał Białecki Blog](https://www.michalbialecki.com/2018/03/18/azure-cosmos-db-key-value-database-cloud/)

[Key-value](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#keyvalue-data-stores) databases တွင် unique keys များနှင့် value တစ်ခုနှင့်ချိတ်ဆက်ထားသော unique identifier များကို pair လုပ်ထားသည်။ ဤ pairs များကို [hash table](https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/tutorial/) နှင့် သင့်လျော်သော hashing function ကို အသုံးပြု၍ သိမ်းဆည်းထားသည်။

![Graphical representation of a graph data store showing the relationships between people, their interests and locations](../../../../2-Working-With-Data/06-non-relational/images/graph-db.png)
> Source from [Microsoft](https://docs.microsoft.com/en-us/azure/cosmos-db/graph/graph-introduction#graph-database-by-example)

[Graph](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#graph-data-stores) databases တွင် ဒေတာအတွင်းရှိ ဆက်နွယ်မှုများကို ဖော်ပြပြီး nodes နှင့် edges များ၏စုစုပေါင်းအဖြစ် ဖော်ပြထားသည်။ Node သည် entity တစ်ခုကို ကိုယ်စားပြုပြီး ၎င်းသည် ကျောင်းသား သို့မဟုတ် ဘဏ်စာရင်းကဲ့သို့ အမှန်တကယ်ရှိသောအရာတစ်ခုဖြစ်သည်။ Edge များသည် entity နှစ်ခုအကြားရှိ ဆက်နွယ်မှုကို ကိုယ်စားပြုသည်။ Node နှင့် edge တစ်ခုစီတွင် node နှင့် edge တစ်ခုစီအကြောင်းအရာကို ပိုမိုသိရှိစေရန် properties များပါဝင်သည်။

![Graphical representation of a columnar data store showing a customer database with two column families named Identity and Contact Info](../../../../2-Working-With-Data/06-non-relational/images/columnar-db.png)

[Columnar](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#columnar-data-stores) data stores တွင် ဒေတာကို columns နှင့် rows အဖြစ် စီစဉ်ထားပြီး relational data structure ကဲ့သို့ဖြစ်သော်လည်း column တစ်ခုစီကို column family ဟုခေါ်သော အုပ်စုများအဖြစ် ခွဲထားပြီး column တစ်ခုအောက်ရှိ ဒေတာအားလုံးသည် ဆက်နွယ်မှုရှိပြီး unit တစ်ခုအဖြစ် retrieve လုပ်နိုင်သည်။

### Azure Cosmos DB နှင့် Document Data Stores

[Document](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#document-data-stores) data stores တွင် key-value data store ၏အယူအဆကို အခြေခံထားပြီး fields နှင့် objects များ၏ စုစုပေါင်းဖြစ်သည်။ ဒီအပိုင်းတွင် Cosmos DB emulator ဖြင့် document databases များကို လေ့လာပါမည်။

Cosmos DB database သည် "Not Only SQL" ဟု အဓိပ္ပါယ်ဖွင့်ဆိုနိုင်ပြီး Cosmos DB ၏ document database သည် SQL ကို အခြေခံထား၍ ဒေတာကို query လုပ်သည်။ [ယခင်သင်ခန်းစာ](../05-relational-databases/README.md) တွင် SQL ၏ အခြေခံများကို ဖော်ပြထားပြီး ဒီနေရာတွင် document database တွင် query များကို အသုံးပြုနိုင်ပါမည်။ Cosmos DB Emulator ကို အသုံးပြု၍ ကွန်ပျူတာတွင် locally document database တစ်ခုကို ဖန်တီးပြီး လေ့လာနိုင်ပါသည်။ Emulator အကြောင်းကို [ဒီနေရာ](https://docs.microsoft.com/en-us/azure/cosmos-db/local-emulator?tabs=ssl-netstd21) တွင် ပိုမိုလေ့လာနိုင်ပါသည်။

Document တစ်ခုသည် fields နှင့် object values များ၏ စုစုပေါင်းဖြစ်ပြီး fields များသည် object value ကို ကိုယ်စားပြုသည်။ အောက်တွင် document ၏ ဥပမာတစ်ခုကို ဖော်ပြထားသည်။

```json
{
    "firstname": "Eva",
    "age": 44,
    "id": "8c74a315-aebf-4a16-bb38-2430a9896ce5",
    "_rid": "bHwDAPQz8s0BAAAAAAAAAA==",
    "_self": "dbs/bHwDAA==/colls/bHwDAPQz8s0=/docs/bHwDAPQz8s0BAAAAAAAAAA==/",
    "_etag": "\"00000000-0000-0000-9f95-010a691e01d7\"",
    "_attachments": "attachments/",
    "_ts": 1630544034
}
```

ဤ document ၏ အဓိက fields များမှာ `firstname`, `id`, နှင့် `age` ဖြစ်သည်။ Cosmos DB မှ ထုတ်လုပ်ထားသော underscores ပါဝင်သော fields များကိုလည်း တွေ့နိုင်သည်။

#### Cosmos DB Emulator ဖြင့် ဒေတာကို လေ့လာခြင်း

Windows အတွက် emulator ကို [ဒီနေရာ](https://aka.ms/cosmosdb-emulator) မှာ ဒေါင်းလုဒ်လုပ်ပြီး ထည့်သွင်းနိုင်သည်။ macOS နှင့် Linux အတွက် Emulator ကို run လုပ်ရန် [ဒီ documentation](https://docs.microsoft.com/en-us/azure/cosmos-db/local-emulator?tabs=ssl-netstd21#run-on-linux-macos) ကို ရည်ညွှန်းပါ။

Emulator သည် browser window တစ်ခုကို ဖွင့်ပြီး Explorer view တွင် documents များကို လေ့လာနိုင်သည်။

![The Explorer view of the Cosmos DB Emulator](../../../../2-Working-With-Data/06-non-relational/images/cosmosdb-emulator-explorer.png)

သင်လိုက်နာနေပါက "Start with Sample" ကို click လုပ်ပြီး SampleDB ဟုခေါ်သော sample database ကို ဖန်တီးပါ။ Sample DB ကို arrow ဖြင့် expand လုပ်ပါက `Persons` ဟုခေါ်သော container တစ်ခုကို တွေ့နိုင်ပါမည်။ Container သည် items များ၏ စုစုပေါင်းကို ထိန်းသိမ်းထားပြီး ၎င်းသည် container အတွင်းရှိ documents များဖြစ်သည်။ `Items` အောက်ရှိ individual documents လေးခုကို လေ့လာနိုင်ပါသည်။

![Exploring sample data in the Cosmos DB Emulator](../../../../2-Working-With-Data/06-non-relational/images/cosmosdb-emulator-persons.png)

#### Cosmos DB Emulator ဖြင့် Document Data ကို Query လုပ်ခြင်း

New SQL Query button (ဘယ်ဘက်မှ ဒုတိယ button) ကို click လုပ်ပြီး sample data ကို query လုပ်နိုင်ပါသည်။

`SELECT * FROM c` သည် container အတွင်းရှိ documents အားလုံးကို ပြန်ပေးသည်။ အောက်တွင် where clause ကို ထည့်ပြီး အသက် 40 ထက်ငယ်သောလူများကို ရှာဖွေပါ။

`SELECT * FROM c where c.age < 40`

![Running a SELECT query on sample data in the Cosmos DB Emulator to find documents that have an age field value that is less than 40](../../../../2-Working-With-Data/06-non-relational/images/cosmosdb-emulator-persons-query.png)

Query သည် documents နှစ်ခုကို ပြန်ပေးပြီး document တစ်ခုစီ၏ အသက်တန်ဖိုးသည် 40 ထက်ငယ်သည်ကို တွေ့နိုင်သည်။

#### JSON နှင့် Documents

သင် JavaScript Object Notation (JSON) ကို သိရှိထားပါက documents များသည် JSON နှင့် ဆင်တူသည်ကို တွေ့နိုင်ပါသည်။ ဒီ directory တွင် `PersonsData.json` ဖိုင်တစ်ခုရှိပြီး ဒေတာများကို Emulator ၏ Persons container တွင် `Upload Item` button ဖြင့် upload လုပ်နိုင်ပါသည်။

အများအားဖြင့် JSON ဒေတာကို ပြန်ပေးသော APIs များသည် document databases တွင် တိုက်ရိုက်လွှဲပြောင်းပြီး သိမ်းဆည်းနိုင်သည်။ အောက်တွင် document တစ်ခုကို ဖော်ပြထားပြီး ၎င်းသည် Microsoft Twitter account မှ tweets ကို Twitter API ကို အသုံးပြု၍ ရယူပြီး Cosmos DB တွင် ထည့်သွင်းထားသည်။

```json
{
    "created_at": "2021-08-31T19:03:01.000Z",
    "id": "1432780985872142341",
    "text": "Blank slate. Like this tweet if you’ve ever painted in Microsoft Paint before. https://t.co/cFeEs8eOPK",
    "_rid": "dhAmAIUsA4oHAAAAAAAAAA==",
    "_self": "dbs/dhAmAA==/colls/dhAmAIUsA4o=/docs/dhAmAIUsA4oHAAAAAAAAAA==/",
    "_etag": "\"00000000-0000-0000-9f84-a0958ad901d7\"",
    "_attachments": "attachments/",
    "_ts": 1630537000
```

ဤ document ၏ အဓိက fields များမှာ `created_at`, `id`, နှင့် `text` ဖြစ်သည်။

## 🚀 စိန်ခေါ်မှု

`TwitterData.json` ဖိုင်တစ်ခုကို SampleDB database တွင် upload လုပ်နိုင်ပါသည်။ ၎င်းကို သီးခြား container တွင် ထည့်သွင်းရန် အကြံပြုပါသည်။ ၎င်းကို လုပ်ဆောင်ရန်:

1. အပေါ်ယံညာဘက်ရှိ new container button ကို click လုပ်ပါ
1. ရှိပြီးသား database (SampleDB) ကို ရွေးချယ်ပြီး container id ကို ဖန်တီးပါ
1. Partition key ကို `/id` အဖြစ် သတ်မှတ်ပါ
1. OK ကို click လုပ်ပါ (ဤ view အတွင်းရှိ အခြားအချက်အလက်များကို မထည့်သွင်းလည်းရသည်၊ ဒါဟာ သင့်စက်တွင် locally run လုပ်နေသော dataset သေးငယ်တစ်ခုဖြစ်သည်)
1. သင့် container အသစ်ကို ဖွင့်ပြီး Twitter Data ဖိုင်ကို `Upload Item` button ဖြင့် upload လုပ်ပါ

Text field အတွင်း Microsoft ပါဝင်သော documents များကို ရှာဖွေရန် select queries အချို့ကို run လုပ်ကြည့်ပါ။ Hint: [LIKE keyword](https://docs.microsoft.com/en-us/azure/cosmos-db/sql/sql-query-keywords#using-like-with-the--wildcard-character) ကို အသုံးပြုရန် ကြိုးစားပါ။

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ds/quiz/11)

## ပြန်လည်သုံးသပ်ခြင်းနှင့် ကိုယ်တိုင်လေ့လာခြင်း

- ဒီသင်ခန်းစာမှာ မဖော်ပြထားသော အပို formatting နှင့် features များကို စာရင်းဇယားတွင် ထည့်သွင်းထားသည်။ Microsoft ၏ [Excel အတွက် documentation နှင့် ဗီဒီယိုများ](https://support.microsoft.com/excel) library ကြီးတစ်ခုရှိပြီး ပိုမိုလေ့လာလိုပါက ကြည့်ရှုနိုင်ပါသည်။

- မဟုတ်သောဆက်နွယ်မှုရှိသော ဒေတာ၏ အမျိုးအစားများ၏ လက္ခဏာများကို ဖော်ပြထားသော ဒီ architectural documentation ကို ကြည့်ရှုပါ: [Non-relational Data and NoSQL](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data)

- Cosmos DB သည် cloud-based non-rel

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းစာရွက်စာတမ်းကို ၎င်း၏ မူရင်းဘာသာစကားဖြင့် အာဏာတရားရှိသော အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူက ဘာသာပြန်မှု ဝန်ဆောင်မှုကို အသုံးပြုရန် အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအလွတ်များ သို့မဟုတ် အနားယူမှုမှားများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။