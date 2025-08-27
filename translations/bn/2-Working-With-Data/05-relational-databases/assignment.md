<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2f2d7693f28e4b2675f275e489dc5aac",
  "translation_date": "2025-08-27T08:23:55+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/assignment.md",
  "language_code": "bn"
}
-->
# বিমানবন্দর ডেটা প্রদর্শন

আপনাকে একটি [ডেটাবেস](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) প্রদান করা হয়েছে যা [SQLite](https://sqlite.org/index.html)-এর উপর ভিত্তি করে তৈরি এবং এতে বিমানবন্দর সম্পর্কিত তথ্য রয়েছে। নিচে স্কিমা প্রদর্শিত হয়েছে। আপনি [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum)-এ [SQLite extension](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) ব্যবহার করে বিভিন্ন শহরের বিমানবন্দর সম্পর্কিত তথ্য প্রদর্শন করবেন।

## নির্দেশনা

এই অ্যাসাইনমেন্ট শুরু করতে হলে আপনাকে কয়েকটি ধাপ সম্পন্ন করতে হবে। কিছু টুল ইনস্টল করতে হবে এবং নমুনা ডেটাবেস ডাউনলোড করতে হবে।

### আপনার সিস্টেম সেটআপ করুন

ডেটাবেসের সাথে ইন্টারঅ্যাক্ট করতে Visual Studio Code এবং SQLite extension ব্যবহার করতে পারেন।

1. [code.visualstudio.com](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum)-এ যান এবং Visual Studio Code ইনস্টল করার নির্দেশনা অনুসরণ করুন
1. [SQLite extension](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) ইনস্টল করুন, যা মার্কেটপ্লেস পেজে নির্দেশিত আছে

### ডেটাবেস ডাউনলোড এবং খুলুন

এরপর আপনি ডেটাবেস ডাউনলোড করবেন এবং খুলবেন।

1. [GitHub থেকে ডেটাবেস ফাইল](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) ডাউনলোড করুন এবং একটি ডিরেক্টরিতে সংরক্ষণ করুন
1. Visual Studio Code খুলুন
1. SQLite extension-এ ডেটাবেস খুলুন **Ctl-Shift-P** (অথবা ম্যাক-এ **Cmd-Shift-P**) নির্বাচন করে এবং `SQLite: Open database` টাইপ করে
1. **Choose database from file** নির্বাচন করুন এবং পূর্বে ডাউনলোড করা **airports.db** ফাইলটি খুলুন
1. ডেটাবেস খুলার পরে (স্ক্রিনে কোনো আপডেট দেখা যাবে না), একটি নতুন কোয়েরি উইন্ডো তৈরি করুন **Ctl-Shift-P** (অথবা ম্যাক-এ **Cmd-Shift-P**) নির্বাচন করে এবং `SQLite: New query` টাইপ করে

একবার খুললে, নতুন কোয়েরি উইন্ডোটি ডেটাবেসের বিরুদ্ধে SQL স্টেটমেন্ট চালানোর জন্য ব্যবহার করা যেতে পারে। **Ctl-Shift-Q** (অথবা ম্যাক-এ **Cmd-Shift-Q**) কমান্ড ব্যবহার করে ডেটাবেসের বিরুদ্ধে কোয়েরি চালানো যাবে।

> [!NOTE] SQLite extension সম্পর্কে আরও তথ্যের জন্য, আপনি [ডকুমেন্টেশন](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) পরামর্শ করতে পারেন

## ডেটাবেস স্কিমা

একটি ডেটাবেসের স্কিমা হলো এর টেবিলের ডিজাইন এবং কাঠামো। **airports** ডেটাবেসে দুটি টেবিল রয়েছে, `cities`, যেখানে যুক্তরাজ্য এবং আয়ারল্যান্ডের শহরগুলোর তালিকা রয়েছে, এবং `airports`, যেখানে সমস্ত বিমানবন্দরের তালিকা রয়েছে। কারণ কিছু শহরে একাধিক বিমানবন্দর থাকতে পারে, তথ্য সংরক্ষণের জন্য দুটি টেবিল তৈরি করা হয়েছে। এই অনুশীলনে আপনি বিভিন্ন শহরের তথ্য প্রদর্শনের জন্য জয়েন ব্যবহার করবেন।

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

## অ্যাসাইনমেন্ট

নিম্নলিখিত তথ্য ফেরত দেওয়ার জন্য কোয়েরি তৈরি করুন:

1. `Cities` টেবিলের সমস্ত শহরের নাম
1. `Cities` টেবিলের আয়ারল্যান্ডের সমস্ত শহর
1. শহর এবং দেশের সাথে সমস্ত বিমানবন্দরের নাম
1. লন্ডন, যুক্তরাজ্যের সমস্ত বিমানবন্দর

## মূল্যায়ন

| চমৎকার | পর্যাপ্ত | উন্নতির প্রয়োজন |
| ------- | -------- | ---------------- |

---

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসম্ভব সঠিক অনুবাদের চেষ্টা করি, তবে অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। নথিটির মূল ভাষায় লেখা সংস্করণটিকেই প্রামাণিক উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য, পেশাদার মানব অনুবাদ ব্যবহার করার পরামর্শ দেওয়া হয়। এই অনুবাদ ব্যবহারের ফলে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।  