<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cc2e18ab65df63e75d3619c4752e9b22",
  "translation_date": "2025-10-03T11:12:23+00:00",
  "source_file": "AGENTS.md",
  "language_code": "bn"
}
-->
# AGENTS.md

## প্রকল্পের সংক্ষিপ্ত বিবরণ

**ডেটা সায়েন্স ফর বিগিনার্স** হলো একটি বিস্তৃত ১০-সপ্তাহের, ২০-লেসনের কারিকুলাম যা মাইক্রোসফট আজুর ক্লাউড অ্যাডভোকেটদের দ্বারা তৈরি। এই রিপোজিটরি একটি শিক্ষামূলক সম্পদ যা প্রকল্প-ভিত্তিক পাঠের মাধ্যমে মৌলিক ডেটা সায়েন্স ধারণাগুলি শেখায়, যার মধ্যে রয়েছে জুপিটার নোটবুক, ইন্টারঅ্যাকটিভ কুইজ এবং হাতে-কলমে অ্যাসাইনমেন্ট।

**মূল প্রযুক্তি:**
- **জুপিটার নোটবুক**: পাইথন ৩ ব্যবহার করে প্রধান শিক্ষার মাধ্যম
- **পাইথন লাইব্রেরি**: pandas, numpy, matplotlib ডেটা বিশ্লেষণ এবং ভিজ্যুয়ালাইজেশনের জন্য
- **Vue.js 2**: কুইজ অ্যাপ্লিকেশন (quiz-app ফোল্ডার)
- **Docsify**: অফলাইন অ্যাক্সেসের জন্য ডকুমেন্টেশন সাইট জেনারেটর
- **Node.js/npm**: জাভাস্ক্রিপ্ট কম্পোনেন্টের প্যাকেজ ম্যানেজমেন্ট
- **Markdown**: সমস্ত পাঠের বিষয়বস্তু এবং ডকুমেন্টেশন

**আর্কিটেকচার:**
- বহু-ভাষার শিক্ষামূলক রিপোজিটরি যা বিস্তৃত অনুবাদ অন্তর্ভুক্ত করে
- পাঠ মডিউলে গঠিত (১-Introduction থেকে ৬-Data-Science-In-Wild পর্যন্ত)
- প্রতিটি পাঠে README, নোটবুক, অ্যাসাইনমেন্ট এবং কুইজ অন্তর্ভুক্ত
- প্রাক-পাঠ এবং পর-পাঠ মূল্যায়নের জন্য স্বতন্ত্র Vue.js কুইজ অ্যাপ্লিকেশন
- GitHub Codespaces এবং VS Code ডেভেলপমেন্ট কন্টেইনার সমর্থন

## সেটআপ কমান্ড

### রিপোজিটরি সেটআপ
```bash
# Clone the repository (if not already cloned)
git clone https://github.com/microsoft/Data-Science-For-Beginners.git
cd Data-Science-For-Beginners
```

### পাইথন এনভায়রনমেন্ট সেটআপ
```bash
# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install common data science libraries (no requirements.txt exists)
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### কুইজ অ্যাপ্লিকেশন সেটআপ
```bash
# Navigate to quiz app
cd quiz-app

# Install dependencies
npm install

# Start development server
npm run serve

# Build for production
npm run build

# Lint and fix files
npm run lint
```

### Docsify ডকুমেন্টেশন সার্ভার
```bash
# Install Docsify globally
npm install -g docsify-cli

# Serve documentation locally
docsify serve

# Documentation will be available at localhost:3000
```

### ভিজ্যুয়ালাইজেশন প্রকল্পের সেটআপ
যেমন meaningful-visualizations (পাঠ ১৩) প্রকল্পের জন্য:
```bash
# Navigate to starter or solution folder
cd 3-Data-Visualization/13-meaningful-visualizations/starter

# Install dependencies
npm install

# Start development server
npm run serve

# Build for production
npm run build

# Lint files
npm run lint
```


## ডেভেলপমেন্ট ওয়ার্কফ্লো

### জুপিটার নোটবুক নিয়ে কাজ করা
1. রিপোজিটরি রুটে জুপিটার চালু করুন: `jupyter notebook`
2. পছন্দের পাঠ ফোল্ডারে যান
3. `.ipynb` ফাইল খুলুন এবং অনুশীলন করুন
4. নোটবুকগুলি স্বয়ংসম্পূর্ণ, যেখানে ব্যাখ্যা এবং কোড সেল অন্তর্ভুক্ত
5. বেশিরভাগ নোটবুক pandas, numpy এবং matplotlib ব্যবহার করে - নিশ্চিত করুন যে সেগুলি ইনস্টল করা আছে

### পাঠের কাঠামো
প্রতিটি পাঠ সাধারণত অন্তর্ভুক্ত করে:
- `README.md` - তত্ত্ব এবং উদাহরণ সহ প্রধান পাঠের বিষয়বস্তু
- `notebook.ipynb` - হাতে-কলমে জুপিটার নোটবুক অনুশীলন
- `assignment.ipynb` বা `assignment.md` - অনুশীলনের জন্য অ্যাসাইনমেন্ট
- `solution/` ফোল্ডার - সমাধানের নোটবুক এবং কোড
- `images/` ফোল্ডার - সহায়ক ভিজ্যুয়াল উপকরণ

### কুইজ অ্যাপ্লিকেশন ডেভেলপমেন্ট
- Vue.js 2 অ্যাপ্লিকেশন যা ডেভেলপমেন্ট চলাকালীন হট-রিলোড সমর্থন করে
- কুইজগুলি `quiz-app/src/assets/translations/` এ সংরক্ষিত
- প্রতিটি ভাষার জন্য আলাদা অনুবাদ ফোল্ডার (en, fr, es, ইত্যাদি)
- কুইজ নম্বর ০ থেকে শুরু হয় এবং ৩৯ পর্যন্ত যায় (মোট ৪০টি কুইজ)

### অনুবাদ যোগ করা
- অনুবাদগুলি রিপোজিটরির রুটে `translations/` ফোল্ডারে যায়
- প্রতিটি ভাষার জন্য ইংরেজি কাঠামোর প্রতিলিপি রাখা হয়
- GitHub Actions এর মাধ্যমে স্বয়ংক্রিয় অনুবাদ (co-op-translator.yml)

## টেস্টিং নির্দেশিকা

### কুইজ অ্যাপ্লিকেশন টেস্টিং
```bash
cd quiz-app

# Run lint checks
npm run lint

# Test build process
npm run build

# Manual testing: Start dev server and verify quiz functionality
npm run serve
```

### নোটবুক টেস্টিং
- নোটবুকের জন্য কোনো স্বয়ংক্রিয় টেস্ট ফ্রেমওয়ার্ক নেই
- ম্যানুয়াল যাচাইকরণ: সমস্ত সেল ক্রমানুসারে চালান এবং নিশ্চিত করুন কোনো ত্রুটি নেই
- ডেটা ফাইল অ্যাক্সেসযোগ্য এবং আউটপুট সঠিকভাবে তৈরি হচ্ছে তা যাচাই করুন
- ভিজ্যুয়ালাইজেশন সঠিকভাবে রেন্ডার হচ্ছে কিনা তা পরীক্ষা করুন

### ডকুমেন্টেশন টেস্টিং
```bash
# Verify Docsify renders correctly
docsify serve

# Check for broken links manually by navigating through content
# Verify all lesson links work in the rendered documentation
```

### কোড কোয়ালিটি চেক
```bash
# Vue.js projects (quiz-app and visualization projects)
cd quiz-app  # or visualization project folder
npm run lint

# Python notebooks - manual verification recommended
# Ensure imports work and cells execute without errors
```


## কোড স্টাইল নির্দেশিকা

### পাইথন (জুপিটার নোটবুক)
- পাইথন কোডের জন্য PEP 8 স্টাইল নির্দেশিকা অনুসরণ করুন
- ডেটা বিশ্লেষণের জন্য স্পষ্ট ভেরিয়েবল নাম ব্যবহার করুন
- কোড সেলের আগে ব্যাখ্যা সহ Markdown সেল যোগ করুন
- কোড সেলগুলো একক ধারণা বা অপারেশনে সীমাবদ্ধ রাখুন
- pandas ডেটা ম্যানিপুলেশনের জন্য এবং matplotlib ভিজ্যুয়ালাইজেশনের জন্য ব্যবহার করুন
- সাধারণ ইমপোর্ট প্যাটার্ন:
  ```python
  import pandas as pd
  import numpy as np
  import matplotlib.pyplot as plt
  ```


### জাভাস্ক্রিপ্ট/Vue.js
- Vue.js 2 স্টাইল গাইড এবং সেরা অনুশীলন অনুসরণ করুন
- `quiz-app/package.json` এ ESLint কনফিগারেশন
- Vue একক-ফাইল কম্পোনেন্ট (.vue ফাইল) ব্যবহার করুন
- কম্পোনেন্ট-ভিত্তিক আর্কিটেকচার বজায় রাখুন
- পরিবর্তন জমা দেওয়ার আগে `npm run lint` চালান

### Markdown ডকুমেন্টেশন
- পরিষ্কার শিরোনামের শ্রেণিবিন্যাস (# ## ### ইত্যাদি) ব্যবহার করুন
- ভাষা নির্দিষ্টকারী সহ কোড ব্লক অন্তর্ভুক্ত করুন
- ছবির জন্য alt টেক্সট যোগ করুন
- সংশ্লিষ্ট পাঠ এবং সম্পদের লিঙ্ক দিন
- পাঠযোগ্যতার জন্য লাইন দৈর্ঘ্য যুক্তিসঙ্গত রাখুন

### ফাইল সংগঠন
- পাঠের বিষয়বস্তু নম্বরযুক্ত ফোল্ডারে (01-defining-data-science, ইত্যাদি)
- `solution/` সাবফোল্ডারে সমাধান সংরক্ষণ
- `translations/` ফোল্ডারে ইংরেজি কাঠামোর প্রতিলিপি
- ডেটা ফাইল `data/` বা পাঠ-নির্দিষ্ট ফোল্ডারে রাখুন

## বিল্ড এবং ডিপ্লয়মেন্ট

### কুইজ অ্যাপ্লিকেশন ডিপ্লয়মেন্ট
```bash
cd quiz-app

# Build production version
npm run build

# Output is in dist/ folder
# Deploy dist/ folder to static hosting (Azure Static Web Apps, Netlify, etc.)
```

### Azure Static Web Apps ডিপ্লয়মেন্ট
কুইজ-অ্যাপ Azure Static Web Apps-এ ডিপ্লয় করা যেতে পারে:
1. Azure Static Web App রিসোর্স তৈরি করুন
2. GitHub রিপোজিটরির সাথে সংযোগ করুন
3. বিল্ড সেটিংস কনফিগার করুন:
   - অ্যাপ লোকেশন: `quiz-app`
   - আউটপুট লোকেশন: `dist`
4. GitHub Actions ওয়ার্কফ্লো পুশ করার সময় স্বয়ংক্রিয়ভাবে ডিপ্লয় করবে

### ডকুমেন্টেশন সাইট
```bash
# Build PDF from Docsify (optional)
npm run convert

# Docsify documentation is served directly from markdown files
# No build step required for deployment
# Deploy repository to static hosting with Docsify
```

### GitHub Codespaces
- রিপোজিটরিতে ডেভ কন্টেইনার কনফিগারেশন অন্তর্ভুক্ত
- Codespaces স্বয়ংক্রিয়ভাবে পাইথন এবং Node.js এনভায়রনমেন্ট সেটআপ করে
- GitHub UI এর মাধ্যমে Codespace-এ রিপোজিটরি খুলুন
- সমস্ত নির্ভরতা স্বয়ংক্রিয়ভাবে ইনস্টল হয়

## পুল রিকোয়েস্ট নির্দেশিকা

### জমা দেওয়ার আগে
```bash
# For Vue.js changes in quiz-app
cd quiz-app
npm run lint
npm run build

# Test changes locally
npm run serve
```

### PR শিরোনামের ফরম্যাট
- পরিষ্কার, বর্ণনামূলক শিরোনাম ব্যবহার করুন
- ফরম্যাট: `[কম্পোনেন্ট] সংক্ষিপ্ত বিবরণ`
- উদাহরণ:
  - `[Lesson 7] Fix Python notebook import error`
  - `[Quiz App] Add German translation`
  - `[Docs] Update README with new prerequisites`

### প্রয়োজনীয় যাচাইকরণ
- নিশ্চিত করুন সমস্ত কোড ত্রুটি ছাড়াই চলে
- নোটবুক সম্পূর্ণরূপে কার্যকর হয় তা যাচাই করুন
- Vue.js অ্যাপ্লিকেশন সফলভাবে বিল্ড হয় তা নিশ্চিত করুন
- ডকুমেন্টেশনের লিঙ্ক কাজ করছে কিনা পরীক্ষা করুন
- কুইজ অ্যাপ্লিকেশন পরিবর্তিত হলে পরীক্ষা করুন
- অনুবাদ কাঠামো সঙ্গতিপূর্ণ কিনা যাচাই করুন

### অবদান নির্দেশিকা
- বিদ্যমান কোড স্টাইল এবং প্যাটার্ন অনুসরণ করুন
- জটিল লজিকের জন্য ব্যাখ্যামূলক মন্তব্য যোগ করুন
- প্রাসঙ্গিক ডকুমেন্টেশন আপডেট করুন
- প্রযোজ্য ক্ষেত্রে বিভিন্ন পাঠ মডিউলে পরিবর্তন পরীক্ষা করুন
- CONTRIBUTING.md ফাইলটি পর্যালোচনা করুন

## অতিরিক্ত নোট

### ব্যবহৃত সাধারণ লাইব্রেরি
- **pandas**: ডেটা ম্যানিপুলেশন এবং বিশ্লেষণ
- **numpy**: সংখ্যাসূচক গণনা
- **matplotlib**: ডেটা ভিজ্যুয়ালাইজেশন এবং প্লটিং
- **seaborn**: পরিসংখ্যানগত ডেটা ভিজ্যুয়ালাইজেশন (কিছু পাঠে)
- **scikit-learn**: মেশিন লার্নিং (উন্নত পাঠে)

### ডেটা ফাইল নিয়ে কাজ করা
- ডেটা ফাইল `data/` ফোল্ডারে বা পাঠ-নির্দিষ্ট ডিরেক্টরিতে অবস্থিত
- বেশিরভাগ নোটবুক আপেক্ষিক পাথের ডেটা ফাইল আশা করে
- CSV ফাইল প্রধান ডেটা ফরম্যাট
- কিছু পাঠে অ-রিলেশনাল ডেটার উদাহরণের জন্য JSON ব্যবহার করা হয়

### বহু-ভাষার সমর্থন
- ৪০+ ভাষায় অনুবাদ GitHub Actions এর মাধ্যমে স্বয়ংক্রিয়
- অনুবাদ ওয়ার্কফ্লো `.github/workflows/co-op-translator.yml` এ
- `translations/` ফোল্ডারে ভাষা কোড সহ অনুবাদ
- কুইজ অনুবাদ `quiz-app/src/assets/translations/` এ

### ডেভেলপমেন্ট এনভায়রনমেন্ট বিকল্প
1. **লোকাল ডেভেলপমেন্ট**: লোকালভাবে পাইথন, জুপিটার, Node.js ইনস্টল করুন
2. **GitHub Codespaces**: ক্লাউড-ভিত্তিক ইনস্ট্যান্ট ডেভেলপমেন্ট এনভায়রনমেন্ট
3. **VS Code Dev Containers**: লোকাল কন্টেইনার-ভিত্তিক ডেভেলপমেন্ট
4. **Binder**: ক্লাউডে নোটবুক চালু করুন (যদি কনফিগার করা থাকে)

### পাঠের বিষয়বস্তু নির্দেশিকা
- প্রতিটি পাঠ স্বতন্ত্র কিন্তু পূর্ববর্তী ধারণার উপর ভিত্তি করে তৈরি
- প্রাক-পাঠ কুইজ পূর্বের জ্ঞান পরীক্ষা করে
- পর-পাঠ কুইজ শেখা জোরদার করে
- অ্যাসাইনমেন্ট হাতে-কলমে অনুশীলন প্রদান করে
- স্কেচনোট ভিজ্যুয়াল সারাংশ প্রদান করে

### সাধারণ সমস্যার সমাধান

**জুপিটার কার্নেল সমস্যা:**
```bash
# Ensure correct kernel is installed
python -m ipykernel install --user --name=datascience
```

**npm ইনস্টল ব্যর্থতা:**
```bash
# Clear npm cache and retry
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
```

**নোটবুকে ইমপোর্ট ত্রুটি:**
- নিশ্চিত করুন সমস্ত প্রয়োজনীয় লাইব্রেরি ইনস্টল করা আছে
- পাইথন সংস্করণ সামঞ্জস্যতা পরীক্ষা করুন (পাইথন ৩.৭+ সুপারিশকৃত)
- নিশ্চিত করুন ভার্চুয়াল এনভায়রনমেন্ট সক্রিয়

**Docsify লোড হচ্ছে না:**
- নিশ্চিত করুন আপনি রিপোজিটরি রুট থেকে সার্ভ করছেন
- নিশ্চিত করুন `index.html` বিদ্যমান
- সঠিক নেটওয়ার্ক অ্যাক্সেস (পোর্ট ৩০০০) নিশ্চিত করুন

### পারফরম্যান্স বিবেচনা
- বড় ডেটাসেট নোটবুকে লোড হতে সময় নিতে পারে
- জটিল প্লটের জন্য ভিজ্যুয়ালাইজেশন রেন্ডারিং ধীর হতে পারে
- Vue.js ডেভ সার্ভার দ্রুত পুনরাবৃত্তির জন্য হট-রিলোড সক্ষম করে
- প্রোডাকশন বিল্ড অপ্টিমাইজড এবং মিনিফাইড

### নিরাপত্তা নোট
- কোনো সংবেদনশীল ডেটা বা শংসাপত্র জমা দেওয়া উচিত নয়
- ক্লাউড পাঠে কোনো API কী-এর জন্য পরিবেশ ভেরিয়েবল ব্যবহার করুন
- Azure-সম্পর্কিত পাঠে Azure অ্যাকাউন্ট শংসাপত্র প্রয়োজন হতে পারে
- নিরাপত্তা প্যাচের জন্য নির্ভরতা আপডেট রাখুন

## অনুবাদে অবদান রাখা
- GitHub Actions এর মাধ্যমে স্বয়ংক্রিয় অনুবাদ পরিচালিত
- অনুবাদের যথার্থতার জন্য ম্যানুয়াল সংশোধন স্বাগত
- বিদ্যমান অনুবাদ ফোল্ডার কাঠামো অনুসরণ করুন
- কুইজ লিঙ্ক আপডেট করুন ভাষার প্যারামিটার অন্তর্ভুক্ত করতে: `?loc=fr`
- অনুবাদিত পাঠ সঠিকভাবে রেন্ডার হচ্ছে কিনা পরীক্ষা করুন

## সংশ্লিষ্ট সম্পদ
- প্রধান কারিকুলাম: https://aka.ms/datascience-beginners
- Microsoft Learn: https://docs.microsoft.com/learn/
- স্টুডেন্ট হাব: https://docs.microsoft.com/learn/student-hub
- আলোচনা ফোরাম: https://github.com/microsoft/Data-Science-For-Beginners/discussions
- অন্যান্য মাইক্রোসফট কারিকুলাম: ML for Beginners, AI for Beginners, Web Dev for Beginners

## প্রকল্প রক্ষণাবেক্ষণ
- বিষয়বস্তু বর্তমান রাখতে নিয়মিত আপডেট
- কমিউনিটি অবদান স্বাগত
- GitHub-এ সমস্যাগুলি ট্র্যাক করা হয়
- কারিকুলাম রক্ষণাবেক্ষণকারীদের দ্বারা PR পর্যালোচনা
- মাসিক বিষয়বস্তু পর্যালোচনা এবং আপডেট

---

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসাধ্য সঠিকতা নিশ্চিত করার চেষ্টা করি, তবে অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। নথিটির মূল ভাষায় থাকা আসল সংস্করণকে প্রামাণিক উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য, পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদ ব্যবহারের ফলে কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যা হলে আমরা তার জন্য দায়বদ্ধ থাকব না।