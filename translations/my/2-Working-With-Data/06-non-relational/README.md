<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "54c5a1c74aecb69d2f9099300a4b7eea",
  "translation_date": "2025-09-05T05:12:07+00:00",
  "source_file": "2-Working-With-Data/06-non-relational/README.md",
  "language_code": "my"
}
-->
# ဒေတာနှင့်အလုပ်လုပ်ခြင်း - မဟုတ်သောဆက်နွယ်မှုရှိသောဒေတာ

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/06-NoSQL.png)|
|:---:|
|NoSQL ဒေတာနှင့်အလုပ်လုပ်ခြင်း - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

## [Pre-Lecture Quiz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/10)

ဒေတာသည် ဆက်နွယ်မှုရှိသောဒေတာဘေ့စ်များတွင်သာမက မဟုတ်သောဆက်နွယ်မှုရှိသောဒေတာများတွင်လည်းရှိနိုင်သည်။ ဒီသင်ခန်းစာမှာ မဟုတ်သောဆက်နွယ်မှုရှိသောဒေတာအကြောင်းကို အခြေခံအချက်များနှင့်အတူ စာရင်းဇယားများနှင့် NoSQL အကြောင်းကိုလေ့လာပါမည်။

## စာရင်းဇယားများ

စာရင်းဇယားများသည် ဒေတာကို သိမ်းဆည်းရန်နှင့် လေ့လာရန်အတွက် လူကြိုက်များသောနည်းလမ်းတစ်ခုဖြစ်ပြီး စတင်ရန်အလုပ်နည်းပါသည်။ ဒီသင်ခန်းစာမှာ စာရင်းဇယား၏ အခြေခံအစိတ်အပိုင်းများ၊ ဖော်မြူလာများနှင့် ဖင်ခရှင်များကိုလေ့လာပါမည်။ ဥပမာများကို Microsoft Excel ဖြင့်ဖော်ပြမည်ဖြစ်ပြီး အခြားစာရင်းဇယားဆော့ဖ်ဝဲများနှင့် နှိုင်းယှဉ်ပါက အများစုမှာ နာမည်နှင့် လုပ်ဆောင်မှုအဆင့်များမှာ တူညီပါသည်။

![Microsoft Excel အလွတ်စာရင်းဇယား](../../../../2-Working-With-Data/06-non-relational/images/parts-of-spreadsheet.png)

စာရင်းဇယားသည် ဖိုင်တစ်ခုဖြစ်ပြီး ကွန်ပျူတာ၊ စက်ပစ္စည်း၊ သို့မဟုတ် cloud-based ဖိုင်စနစ်တွင် ရရှိနိုင်ပါသည်။ ဆော့ဖ်ဝဲကို browser-based ဖြစ်နိုင်သလို ကွန်ပျူတာတွင် install လုပ်ရမည့် application သို့မဟုတ် app အဖြစ် download လုပ်ရနိုင်ပါသည်။ Excel တွင် ဒီဖိုင်များကို **workbooks** ဟုခေါ်ပြီး ဒီသင်ခန်းစာတစ်ခုလုံးတွင် ဒီနာမည်ကို အသုံးပြုပါမည်။

Workbook တစ်ခုတွင် **worksheets** တစ်ခု သို့မဟုတ် အများအပြားပါဝင်ပြီး worksheet တစ်ခုစီကို tabs ဖြင့် label လုပ်ထားသည်။ Worksheet တစ်ခုတွင် **cells** ဟုခေါ်သော စတုရန်းများပါဝင်ပြီး ဒေတာကို ထည့်သွင်းထားသည်။ Cell သည် အတန်းနှင့် ကော်လံတို့၏ intersection ဖြစ်ပြီး ကော်လံများကို အက္ခရာများဖြင့် label လုပ်ထားပြီး အတန်းများကို နံပါတ်များဖြင့် label လုပ်ထားသည်။ စာရင်းဇယားတစ်ချို့တွင် cell တွင်ရှိသော ဒေတာကို ဖော်ပြရန် အတန်းပထမတန်းများတွင် headers ပါဝင်နိုင်သည်။

Excel workbook ၏ အခြေခံအစိတ်အပိုင်းများနှင့်အတူ [Microsoft Templates](https://templates.office.com/) မှ inventory ကို အခြေခံထားသော ဥပမာတစ်ခုကို အသုံးပြု၍ စာရင်းဇယား၏ အပိုင်းများကို လေ့လာပါမည်။

### Inventory ကို စီမံခြင်း

"InventoryExample" ဟုခေါ်သော စာရင်းဇယားဖိုင်သည် inventory အတွင်းရှိ items များကို ဖော်ပြထားသော format စနစ်ဖြင့်ရေးသားထားပြီး worksheets သုံးခုပါဝင်သည်။ Tabs များကို "Inventory List", "Inventory Pick List" နှင့် "Bin Lookup" ဟု label လုပ်ထားသည်။ Inventory List worksheet ၏ အတန်း 4 သည် header ဖြစ်ပြီး header column တွင် cell တစ်ခုစီ၏ value ကို ဖော်ပြထားသည်။

![Microsoft Excel မှ inventory list ၏ formula ကို highlight လုပ်ထားသောပုံ](../../../../2-Working-With-Data/06-non-relational/images/formula-excel.png)

တစ်ခါတစ်ရံ cell တစ်ခုသည် အခြား cell များ၏ value များအပေါ် မူတည်၍ value ကို ဖန်တီးရနိုင်သည်။ Inventory List စာရင်းဇယားသည် inventory အတွင်းရှိ item တစ်ခုစီ၏ cost ကို ထိန်းသိမ်းထားသော်လည်း inventory အတွင်းရှိ အားလုံး၏ value ကို သိရန်လိုအပ်ပါက [**Formulas**](https://support.microsoft.com/en-us/office/overview-of-formulas-34519a4e-1e8d-4f4b-84d4-d642c4f63263) သည် cell data တွင် လုပ်ဆောင်မှုများကို ပြုလုပ်ပြီး ဒီဥပမာတွင် inventory cost ကိုတွက်ရန် အသုံးပြုသည်။ Inventory Value column တွင် formula ကို အသုံးပြု၍ QTY header အောက်ရှိ quantity နှင့် COST header အောက်ရှိ cost ကို များကာ item တစ်ခုစီ၏ value ကိုတွက်ချက်ထားသည်။ Cell ကို double click လုပ်ခြင်း သို့မဟုတ် highlight လုပ်ခြင်းဖြင့် formula ကို ကြည့်နိုင်သည်။ Formula များသည် equals sign ဖြင့်စတင်ပြီး တွက်ချက်မှု သို့မဟုတ် လုပ်ဆောင်မှုကို ဆက်လက်ရေးသားထားသည်။

![Microsoft Excel မှ inventory list ၏ function ကို highlight လုပ်ထားသောပုံ](../../../../2-Working-With-Data/06-non-relational/images/function-excel.png)

Inventory Value ၏ value အားလုံးကို ပေါင်းပြီး total value ကို ရနိုင်သည်။ Cell တစ်ခုစီကို ပေါင်းပြီး တွက်ချက်နိုင်သော်လည်း အလုပ်များသော task ဖြစ်နိုင်သည်။ Excel တွင် [**functions**](https://support.microsoft.com/en-us/office/sum-function-043e1c7d-7726-4e80-8f32-07b23e057f89) ဟုခေါ်သော pre-defined formulas ရှိပြီး cell values တွင် တွက်ချက်မှုများကို ပြုလုပ်နိုင်သည်။ Functions တွင် arguments လိုအပ်ပြီး ဒါတွေက တွက်ချက်မှုများကို ပြုလုပ်ရန်လိုအပ်သော value များဖြစ်သည်။ Functions တွင် argument များစီစဉ်မှုလိုအပ်ပါက အတိအကျစီစဉ်ရမည်။ ဒီဥပမာတွင် SUM function ကို အသုံးပြုပြီး Inventory Value ၏ value များကို argument အဖြစ်အသုံးပြု၍ row 3, column B (B3) တွင် total value ကို ဖော်ပြထားသည်။

## NoSQL

NoSQL သည် မဟုတ်သောဆက်နွယ်မှုရှိသောဒေတာကို သိမ်းဆည်းရန် နည်းလမ်းများကို အုပ်စုဖွဲ့ထားသော term ဖြစ်ပြီး "non-SQL", "non-relational" သို့မဟုတ် "not only SQL" ဟုလည်း အဓိပ္ပါယ်ရနိုင်သည်။ ဒီအမျိုးအစား database systems များကို အမျိုးအစား 4 ခုအဖြစ် အုပ်စုဖွဲ့ထားသည်။

![Key-value data store ၏ ဂရပ်ဖစ်ကိုဖော်ပြထားသောပုံ](../../../../2-Working-With-Data/06-non-relational/images/kv-db.png)
> [Michał Białecki Blog](https://www.michalbialecki.com/2018/03/18/azure-cosmos-db-key-value-database-cloud/) မှရရှိသောအရင်းအမြစ်

[Key-value](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#keyvalue-data-stores) databases တွင် unique keys များနှင့် value များကို pair လုပ်ထားသည်။ ဒီ pair များကို [hash table](https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/tutorial/) ဖြင့် appropriate hashing function ကို အသုံးပြု၍ သိမ်းဆည်းထားသည်။

![Graph data store ၏ ဂရပ်ဖစ်ကိုဖော်ပြထားသောပုံ](../../../../2-Working-With-Data/06-non-relational/images/graph-db.png)
> [Microsoft](https://docs.microsoft.com/en-us/azure/cosmos-db/graph/graph-introduction#graph-database-by-example) မှရရှိသောအရင်းအမြစ်

[Graph](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#graph-data-stores) databases တွင် ဒေတာအတွင်းရှိ ဆက်နွယ်မှုများကို ဖော်ပြထားပြီး nodes နှင့် edges များအဖြစ် ဖော်ပြထားသည်။ Node သည် entity တစ်ခုကို ကိုယ်စားပြုထားပြီး အတန်းသား သို့မဟုတ် ဘဏ်စာရင်းကဲ့သို့ အမှန်တကယ်ရှိသောအရာများကို ကိုယ်စားပြုသည်။ Edge များသည် entity နှစ်ခုအကြားရှိ ဆက်နွယ်မှုကို ကိုယ်စားပြုသည်။ Node နှင့် edge တစ်ခုစီတွင် အပိုဆောင်းအချက်အလက်များကို ဖော်ပြထားသော properties ရှိသည်။

![Columnar data store ၏ ဂရပ်ဖစ်ကိုဖော်ပြထားသောပုံ](../../../../2-Working-With-Data/06-non-relational/images/columnar-db.png)

[Columnar](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#columnar-data-stores) data stores တွင် ဒေတာကို columns နှင့် rows အဖြစ် စီစဉ်ထားပြီး relational data structure ကဲ့သို့ဖြစ်သော်လည်း column တစ်ခုစီကို column family ဟုခေါ်သော အုပ်စုများအဖြစ် ခွဲထားသည်။ Column တစ်ခုအောက်ရှိ ဒေတာအားလုံးသည် ဆက်နွယ်မှုရှိပြီး unit တစ်ခုအဖြစ် retrieve လုပ်နိုင်သည်။

### Azure Cosmos DB ဖြင့် Document Data Stores

[Document](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#document-data-stores) data stores တွင် key-value data store ၏ concept ကို အခြေခံထားပြီး fields နှင့် objects များဖြင့် ဖွဲ့စည်းထားသည်။ ဒီအပိုင်းတွင် Cosmos DB emulator ဖြင့် document databases ကို လေ့လာပါမည်။

Cosmos DB database သည် "Not Only SQL" ဟု အဓိပ္ပါယ်ရပြီး Cosmos DB ၏ document database သည် SQL ကို rely လုပ်၍ ဒေတာကို query လုပ်သည်။ [ယခင်သင်ခန်းစာ](../05-relational-databases/README.md) တွင် SQL ၏ အခြေခံများကို ဖော်ပြထားပြီး ဒီနေရာတွင် document database တွင် query များကို အသုံးပြုနိုင်ပါမည်။ Cosmos DB Emulator ကို အသုံးပြု၍ ကွန်ပျူတာတွင် locally document database တစ်ခုကို ဖန်တီးပြီး လေ့လာနိုင်သည်။ Emulator အကြောင်းကို [ဒီမှာ](https://docs.microsoft.com/en-us/azure/cosmos-db/local-emulator?tabs=ssl-netstd21) ဖတ်ရှုနိုင်သည်။

Document သည် fields နှင့် object values များဖြင့် ဖွဲ့စည်းထားပြီး fields များသည် object value ကို ကိုယ်စားပြုသည်။ အောက်တွင် document ၏ ဥပမာတစ်ခုကို ဖော်ပြထားသည်။

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

ဒီ document ၏ အရေးပါသော fields များမှာ `firstname`, `id`, နှင့် `age` ဖြစ်သည်။ Cosmos DB မှ underscore ဖြင့်စတင်သော fields များကို auto-generate လုပ်ထားသည်။

#### Cosmos DB Emulator ဖြင့် ဒေတာကို လေ့လာခြင်း

Emulator ကို [Windows အတွက် ဒီမှာ](https://aka.ms/cosmosdb-emulator) download လုပ်ပြီး install လုပ်နိုင်သည်။ macOS နှင့် Linux အတွက် Emulator ကို run လုပ်ရန် [ဒီ documentation](https://docs.microsoft.com/en-us/azure/cosmos-db/local-emulator?tabs=ssl-netstd21#run-on-linux-macos) ကို ရည်ညွှန်းပါ။

Emulator သည် browser window တစ်ခုကို ဖွင့်ပြီး Explorer view တွင် documents များကို လေ့လာနိုင်သည်။

![Cosmos DB Emulator ၏ Explorer view](../../../../2-Working-With-Data/06-non-relational/images/cosmosdb-emulator-explorer.png)

လိုက်နာလိုပါက "Start with Sample" ကို click လုပ်ပြီး SampleDB ဟုခေါ်သော sample database ကို ဖန်တီးပါ။ SampleDB ကို arrow ဖြင့် expand လုပ်ပါက `Persons` ဟုခေါ်သော container ကို တွေ့ပါမည်။ Container သည် items များကို collection အဖြစ် သိမ်းဆည်းထားပြီး container အတွင်းရှိ documents များကို ကိုယ်စားပြုသည်။ `Items` အောက်ရှိ individual documents ၄ ခုကို လေ့လာနိုင်သည်။

![Cosmos DB Emulator ၏ sample data ကို လေ့လာခြင်း](../../../../2-Working-With-Data/06-non-relational/images/cosmosdb-emulator-persons.png)

#### Cosmos DB Emulator ဖြင့် Document Data ကို Query လုပ်ခြင်း

New SQL Query button (ဒုတိယ button) ကို click လုပ်ပြီး sample data ကို query လုပ်နိုင်သည်။

`SELECT * FROM c` သည် container အတွင်းရှိ documents အားလုံးကို ပြန်ပေးသည်။ အောက်တွင် where clause ကို ထည့်ပြီး အသက် 40 ထက်ငယ်သောလူများကို ရှာပါ။

`SELECT * FROM c where c.age < 40`

![Cosmos DB Emulator ၏ sample data တွင် SELECT query ကို run လုပ်ခြင်း](../../../../2-Working-With-Data/06-non-relational/images/cosmosdb-emulator-persons-query.png)

Query သည် documents ၂ ခုကို ပြန်ပေးပြီး document တစ်ခုစီ၏ age value သည် 40 ထက်ငယ်သည်။

#### JSON နှင့် Documents

JavaScript Object Notation (JSON) ကို သိရှိထားပါက documents များသည် JSON နှင့် ဆင်တူသည်ကို တွေ့ရပါမည်။ ဒီ directory တွင် `PersonsData.json` ဖိုင်တစ်ခုရှိပြီး ဒေတာများကို Emulator ၏ Persons container တွင် `Upload Item` button ဖြင့် upload လုပ်နိုင်သည်။

အများစုမှာ JSON data ကို return လုပ်သော APIs များသည် document databases တွင် တိုက်ရိုက်သိမ်းဆည်းနိုင်သည်။ အောက်တွင် document တစ်ခုရှိပြီး Microsoft Twitter account မှ tweets ကို Twitter API ဖြင့် retrieve လုပ်ပြီး Cosmos DB တွင် insert လုပ်ထားသည်။

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

ဒီ document ၏ အရေးပါသော fields များမှာ `created_at`, `id`, နှင့် `text` ဖြစ်သည်။

## 🚀 စိန်ခေါ်မှု

`TwitterData.json` ဖိုင်တစ်ခုကို SampleDB database တွင် upload လုပ်နိုင်သည်။ ဒါကို သီးခြား container တွင် ထည့်သွင်းရန် အကြံပြုပါသည်။ ဒီအဆင့်များကို လိုက်နာပါ-

1. အပေါ်ယံညာဘက်ရှိ new container button ကို click လုပ်ပါ
1. ရှိပြီးသား database (SampleDB) ကို ရွေးချယ်ပြီး container id ကို ဖန်တီးပါ
1. Partition key ကို `/id` အဖြစ် သတ်မှတ်ပါ
1. OK ကို click လုပ်ပါ (ဒီ view ၏ အခြားအချက်အလက်များကို လျစ်လျူရှုနိုင်သည်)
1. သင့် container ကို ဖွင့်ပြီး Twitter Data ဖိုင်ကို `Upload Item` button ဖြင့် upload လုပ်ပါ

`text` field တွင် Microsoft ပါဝင်သော documents များကို ရှာရန် select queries အချို့ကို run လုပ်ကြည့်ပါ။ Hint: [LIKE keyword](https://docs.microsoft.com/en-us/azure/cosmos-db/sql/sql-query-keywords#using-like-with-the--wildcard-character) ကို အသုံးပြုပါ။

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ds/)

## ပြန်လည်သုံးသပ်ခြင်းနှင့် ကိုယ်တိုင်လေ့လာခြင်း

- ဒီသင်ခန်းစာတွင် မဖော်ပြထားသော စာရင်းဇယား၏ အပိုဆောင်း format များနှင့် features များရှိသည်။ Microsoft ၏ [Excel အတွက် documentation နှင့် ဗီဒီယိုများ](https://support.microsoft.com/excel) library ကြီးကို လေ့လာပါ။

- မဟုတ်သောဆက်နွယ်မှုရှိသောဒေတာ၏ အမျိုးအစားများ၏ လက္ခဏာများကို ဖော်ပြထားသော architectural documentation ကို [Non-relational Data and NoSQL](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data) တွင် ဖတ်ရှုပါ။

- Cosmos DB သည် cloud-based non-relational database ဖြစ်ပြီး ဒီသင်ခန်းစာတွင်ဖော်ပြထားသော NoSQL အမျိုးအစားများကိုလည်း သိမ်းဆည်းနိုင်သည်။ [Cosmos DB Microsoft Learn Module](https://docs.microsoft.com/en-us/learn/paths/work-with-nosql-data-in-azure-cosmos-db/) တွင် ဒီအမျိုးအစားများအကြောင်းပိုမိုလေ့လာပါ။

## အိမ်စာ

[Soda Profits](assignment.md)

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါရှိနိုင်သည်ကို သတိပြုပါ။ မူရင်းစာရွက်စာတမ်းကို ၎င်း၏ မူရင်းဘာသာစကားဖြင့် အာဏာတရားရှိသော ရင်းမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များမှ ပရော်ဖက်ရှင်နယ် ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအလွတ်များ သို့မဟုတ် အနားယူမှားမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။