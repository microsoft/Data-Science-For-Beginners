<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2f2d7693f28e4b2675f275e489dc5aac",
  "translation_date": "2025-08-30T18:14:59+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/assignment.md",
  "language_code": "my"
}
-->
# လေဆိပ်ဆိုင်ရာ ဒေတာကို ပြသခြင်း

သင့်အား [SQLite](https://sqlite.org/index.html) အခြေခံပြီး တည်ဆောက်ထားသော [ဒေတာဘေစ်စ်](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) တစ်ခုကို ပေးထားပြီး၊ လေဆိပ်ဆိုင်ရာ အချက်အလက်များ ပါဝင်သည်။ Schema ကို အောက်တွင် ပြထားသည်။ သင်သည် [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) တွင် [SQLite extension](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) ကို အသုံးပြု၍ မြို့များ၏ လေဆိပ်ဆိုင်ရာ အချက်အလက်များကို ပြသမည်ဖြစ်သည်။

## လုပ်ဆောင်ရန်ညွှန်ကြားချက်များ

ဤအလုပ်ကို စတင်လုပ်ဆောင်ရန် သင်သည် အဆင့်အတန်းအချို့ကို လုပ်ဆောင်ရန် လိုအပ်ပါမည်။ အချို့သော tools များကို ထည့်သွင်းပြီး နမူနာ ဒေတာဘေစ်စ်ကို ဒေါင်းလုဒ်လုပ်ရန် လိုအပ်ပါမည်။

### သင့်စနစ်ကို ပြင်ဆင်ပါ

Visual Studio Code နှင့် SQLite extension ကို အသုံးပြု၍ ဒေတာဘေစ်စ်နှင့် အပြန်အလှန် ဆက်သွယ်နိုင်ပါသည်။

1. [code.visualstudio.com](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) သို့ သွားပြီး Visual Studio Code ကို ထည့်သွင်းရန် ညွှန်ကြားချက်များကို လိုက်နာပါ
1. [SQLite extension](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) ကို Marketplace စာမျက်နှာတွင် ရှိသော ညွှန်ကြားချက်များအတိုင်း ထည့်သွင်းပါ

### ဒေတာဘေစ်စ်ကို ဒေါင်းလုဒ်လုပ်ပြီး ဖွင့်ပါ

နောက်တစ်ဆင့်တွင် ဒေတာဘေစ်စ်ကို ဒေါင်းလုဒ်လုပ်ပြီး ဖွင့်ပါ။

1. [GitHub မှ ဒေတာဘေစ်စ်ဖိုင်](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) ကို ဒေါင်းလုဒ်လုပ်ပြီး ဖိုင်ကို တစ်ခုခုသော ဒါရိုက်ထရီတွင် သိမ်းဆည်းပါ
1. Visual Studio Code ကို ဖွင့်ပါ
1. **Ctl-Shift-P** (Mac တွင် **Cmd-Shift-P**) ကို ရိုက်နှိပ်ပြီး `SQLite: Open database` ဟု ရိုက်ပါ၊ ထို့နောက် SQLite extension တွင် ဒေတာဘေစ်စ်ကို ဖွင့်ပါ
1. **Choose database from file** ကို ရွေးပြီး သင် ဒေါင်းလုဒ်လုပ်ထားသော **airports.db** ဖိုင်ကို ဖွင့်ပါ
1. ဒေတာဘေစ်စ်ကို ဖွင့်ပြီးနောက် (Screen တွင် update များ မမြင်ရပါ) **Ctl-Shift-P** (Mac တွင် **Cmd-Shift-P**) ကို ရိုက်နှိပ်ပြီး `SQLite: New query` ဟု ရိုက်ပါ

ဖွင့်ပြီးနောက် query window အသစ်ကို SQL statements များကို ဒေတာဘေစ်စ်တွင် run လုပ်ရန် အသုံးပြုနိုင်ပါသည်။ **Ctl-Shift-Q** (Mac တွင် **Cmd-Shift-Q**) ကို အသုံးပြု၍ query များကို run လုပ်နိုင်ပါသည်။

> [!NOTE] SQLite extension အကြောင်း ပိုမိုသိရှိလိုပါက [documentation](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) ကို ကြည့်ရှုနိုင်ပါသည်။

## ဒေတာဘေစ်စ် Schema

ဒေတာဘေစ်စ်၏ schema သည် table design နှင့် structure ဖြစ်သည်။ **airports** ဒေတာဘေစ်စ်တွင် `cities` နှင့် `airports` ဟုခေါ်သော table နှစ်ခု ပါဝင်သည်။ `cities` တွင် United Kingdom နှင့် Ireland ရှိ မြို့များ၏ စာရင်းပါဝင်ပြီး၊ `airports` တွင် လေဆိပ်များ၏ စာရင်းပါဝင်သည်။ အချို့သော မြို့များတွင် လေဆိပ်များစွာ ရှိနိုင်သောကြောင့် အချက်အလက်များကို သိမ်းဆည်းရန် table နှစ်ခုကို ဖန်တီးထားသည်။ ဤလေ့ကျင့်ခန်းတွင် သင်သည် joins ကို အသုံးပြု၍ မြို့များအတွက် အချက်အလက်များကို ပြသမည်ဖြစ်သည်။

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

## လုပ်ငန်းတာဝန်

အောက်ပါ အချက်အလက်များကို ပြန်ပေးရန် query များကို ဖန်တီးပါ-

1. `Cities` table တွင် မြို့အမည်အားလုံး
1. `Cities` table တွင် Ireland ရှိ မြို့များအားလုံး
1. လေဆိပ်အမည်များအားလုံး၊ ၎င်းတို့၏ မြို့နှင့် နိုင်ငံ
1. London, United Kingdom ရှိ လေဆိပ်များအားလုံး

## အဆင့်သတ်မှတ်ချက်

| ထူးချွန် | လုံလောက် | တိုးတက်ရန်လိုအပ် |
| --------- | -------- | ---------------- |

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါရှိနိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာရှိသော ရင်းမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များမှ ပရော်ဖက်ရှင်နယ် ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအလွဲအမှားများ သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။