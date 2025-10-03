<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f546349678757508d69ce9e1d2688446",
  "translation_date": "2025-10-03T14:58:16+00:00",
  "source_file": "USAGE.md",
  "language_code": "bn"
}
-->
# ব্যবহার নির্দেশিকা

এই নির্দেশিকাটি ডেটা সায়েন্স ফর বিগিনার্স কারিকুলাম ব্যবহারের উদাহরণ এবং সাধারণ কর্মপ্রবাহ প্রদান করে।

## সূচিপত্র

- [এই কারিকুলাম কীভাবে ব্যবহার করবেন](../..)
- [পাঠের সাথে কাজ করা](../..)
- [জুপিটার নোটবুকের সাথে কাজ করা](../..)
- [কুইজ অ্যাপ্লিকেশন ব্যবহার করা](../..)
- [সাধারণ কর্মপ্রবাহ](../..)
- [স্ব-শিক্ষার্থীদের জন্য টিপস](../..)
- [শিক্ষকদের জন্য টিপস](../..)

## এই কারিকুলাম কীভাবে ব্যবহার করবেন

এই কারিকুলামটি নমনীয়ভাবে ডিজাইন করা হয়েছে এবং বিভিন্ন উপায়ে ব্যবহার করা যেতে পারে:

- **স্ব-গতির শিক্ষা**: নিজের গতিতে স্বাধীনভাবে পাঠগুলি সম্পন্ন করুন
- **শ্রেণীকক্ষের নির্দেশনা**: গাইডেড নির্দেশনার সাথে একটি কাঠামোগত কোর্স হিসাবে ব্যবহার করুন
- **স্টাডি গ্রুপ**: সহপাঠীদের সাথে সহযোগিতামূলকভাবে শিখুন
- **ওয়ার্কশপ ফরম্যাট**: স্বল্পমেয়াদী নিবিড় শিক্ষার সেশন

## পাঠের সাথে কাজ করা

প্রতিটি পাঠ একটি ধারাবাহিক কাঠামো অনুসরণ করে যাতে শেখার সর্বাধিক সুবিধা হয়:

### পাঠের কাঠামো

1. **পূর্ব-পাঠ কুইজ**: আপনার বিদ্যমান জ্ঞান পরীক্ষা করুন
2. **স্কেচনোট** (ঐচ্ছিক): মূল ধারণার ভিজ্যুয়াল সারাংশ
3. **ভিডিও** (ঐচ্ছিক): সম্পূরক ভিডিও সামগ্রী
4. **লিখিত পাঠ**: মূল ধারণা এবং ব্যাখ্যা
5. **জুপিটার নোটবুক**: হাতে-কলমে কোডিং অনুশীলন
6. **অ্যাসাইনমেন্ট**: আপনি যা শিখেছেন তা অনুশীলন করুন
7. **পোস্ট-পাঠ কুইজ**: আপনার বোঝাপড়া শক্তিশালী করুন

### একটি পাঠের উদাহরণ কর্মপ্রবাহ

```bash
# 1. Navigate to the lesson directory
cd 1-Introduction/01-defining-data-science

# 2. Read the README.md
# Open README.md in your browser or editor

# 3. Take the pre-lesson quiz
# Click the quiz link in the README

# 4. Open the Jupyter notebook (if available)
jupyter notebook

# 5. Complete the exercises in the notebook

# 6. Work on the assignment

# 7. Take the post-lesson quiz
```

## জুপিটার নোটবুকের সাথে কাজ করা

### জুপিটার শুরু করা

```bash
# Activate your virtual environment
source venv/bin/activate  # On macOS/Linux
# OR
venv\Scripts\activate  # On Windows

# Start Jupyter from the repository root
jupyter notebook
```

### নোটবুক সেলের কার্যকরী করা

1. **একটি সেল কার্যকর করুন**: `Shift + Enter` চাপুন বা "Run" বোতামে ক্লিক করুন
2. **সব সেল কার্যকর করুন**: মেনু থেকে "Cell" → "Run All" নির্বাচন করুন
3. **কর্ণেল পুনরায় শুরু করুন**: সমস্যা হলে "Kernel" → "Restart" নির্বাচন করুন

### উদাহরণ: নোটবুকে ডেটার সাথে কাজ করা

```python
# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load a dataset
df = pd.read_csv('data/sample.csv')

# Explore the data
df.head()
df.info()
df.describe()

# Create a visualization
plt.figure(figsize=(10, 6))
plt.plot(df['column_name'])
plt.title('Sample Visualization')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.show()
```

### আপনার কাজ সংরক্ষণ করা

- জুপিটার সময়ে সময়ে স্বয়ংক্রিয়ভাবে সংরক্ষণ করে
- ম্যানুয়ালি সংরক্ষণ করুন: `Ctrl + S` (বা macOS-এ `Cmd + S`) চাপুন
- আপনার অগ্রগতি `.ipynb` ফাইলে সংরক্ষিত হয়

## কুইজ অ্যাপ্লিকেশন ব্যবহার করা

### স্থানীয়ভাবে কুইজ অ্যাপ চালানো

```bash
# Navigate to quiz app directory
cd quiz-app

# Start the development server
npm run serve

# Access at http://localhost:8080
```

### কুইজ নেওয়া

1. পূর্ব-পাঠ কুইজগুলি প্রতিটি পাঠের শীর্ষে লিঙ্ক করা থাকে
2. পোস্ট-পাঠ কুইজগুলি প্রতিটি পাঠের শেষে লিঙ্ক করা থাকে
3. প্রতিটি কুইজে ৩টি প্রশ্ন থাকে
4. কুইজগুলি শেখার শক্তিশালীকরণের জন্য ডিজাইন করা হয়েছে, সম্পূর্ণ পরীক্ষা করার জন্য নয়

### কুইজ নম্বরিং

- কুইজগুলি ০-৩৯ নম্বরযুক্ত (মোট ৪০টি কুইজ)
- প্রতিটি পাঠে সাধারণত একটি পূর্ব এবং একটি পোস্ট কুইজ থাকে
- কুইজ URL-এ কুইজ নম্বর অন্তর্ভুক্ত থাকে: `https://ff-quizzes.netlify.app/en/ds/quiz/0`

## সাধারণ কর্মপ্রবাহ

### কর্মপ্রবাহ ১: সম্পূর্ণ বিগিনার পথ

```bash
# 1. Set up your environment (see INSTALLATION.md)

# 2. Start with Lesson 1
cd 1-Introduction/01-defining-data-science

# 3. For each lesson:
#    - Take pre-lesson quiz
#    - Read the lesson content
#    - Work through the notebook
#    - Complete the assignment
#    - Take post-lesson quiz

# 4. Progress through all 20 lessons sequentially
```

### কর্মপ্রবাহ ২: বিষয়-নির্দিষ্ট শিক্ষা

যদি আপনি একটি নির্দিষ্ট বিষয়ে আগ্রহী হন:

```bash
# Example: Focus on Data Visualization
cd 3-Data-Visualization

# Explore lessons 9-13:
# - Lesson 9: Visualizing Quantities
# - Lesson 10: Visualizing Distributions
# - Lesson 11: Visualizing Proportions
# - Lesson 12: Visualizing Relationships
# - Lesson 13: Meaningful Visualizations
```

### কর্মপ্রবাহ ৩: প্রকল্প-ভিত্তিক শিক্ষা

```bash
# 1. Review the Data Science Lifecycle lessons (14-16)
cd 4-Data-Science-Lifecycle

# 2. Work through a real-world example (Lesson 20)
cd ../6-Data-Science-In-Wild/20-Real-World-Examples

# 3. Apply concepts to your own project
```

### কর্মপ্রবাহ ৪: ক্লাউড-ভিত্তিক ডেটা সায়েন্স

```bash
# Learn about cloud data science (Lessons 17-19)
cd 5-Data-Science-In-Cloud

# 17: Introduction to Cloud Data Science
# 18: Low-Code ML Tools
# 19: Azure Machine Learning Studio
```

## স্ব-শিক্ষার্থীদের জন্য টিপস

### সংগঠিত থাকুন

```bash
# Create a learning journal
mkdir my-learning-journal

# For each lesson, create notes
echo "# Lesson 1 Notes" > my-learning-journal/lesson-01-notes.md
```

### নিয়মিত অনুশীলন করুন

- প্রতিদিন বা প্রতি সপ্তাহে নির্ধারিত সময় বরাদ্দ করুন
- প্রতি সপ্তাহে অন্তত একটি পাঠ সম্পন্ন করুন
- পূর্ববর্তী পাঠগুলি সময়ে সময়ে পুনরায় দেখুন

### সম্প্রদায়ের সাথে যুক্ত হন

- [Discord কমিউনিটি](https://aka.ms/ds4beginners/discord)-এ যোগ দিন
- Discord-এ #Data-Science-for-Beginners চ্যানেলে অংশগ্রহণ করুন [Discord Discussions](https://aka.ms/ds4beginners/discord)
- আপনার অগ্রগতি শেয়ার করুন এবং প্রশ্ন করুন

### নিজের প্রকল্প তৈরি করুন

পাঠগুলি সম্পন্ন করার পরে, ব্যক্তিগত প্রকল্পে ধারণাগুলি প্রয়োগ করুন:

```python
# Example: Analyze your own dataset
import pandas as pd

# Load your own data
my_data = pd.read_csv('my-project/data.csv')

# Apply techniques learned
# - Data cleaning (Lesson 8)
# - Exploratory data analysis (Lesson 7)
# - Visualization (Lessons 9-13)
# - Analysis (Lesson 15)
```

## শিক্ষকদের জন্য টিপস

### শ্রেণীকক্ষ সেটআপ

1. বিস্তারিত নির্দেশনার জন্য [for-teachers.md](for-teachers.md) পর্যালোচনা করুন
2. একটি শেয়ারড পরিবেশ সেট আপ করুন (GitHub Classroom বা Codespaces)
3. একটি যোগাযোগ চ্যানেল স্থাপন করুন (Discord, Slack, বা Teams)

### পাঠ পরিকল্পনা

**প্রস্তাবিত ১০-সপ্তাহের সময়সূচি:**

- **সপ্তাহ ১-২**: পরিচিতি (পাঠ ১-৪)
- **সপ্তাহ ৩-৪**: ডেটার সাথে কাজ করা (পাঠ ৫-৮)
- **সপ্তাহ ৫-৬**: ডেটা ভিজ্যুয়ালাইজেশন (পাঠ ৯-১৩)
- **সপ্তাহ ৭-৮**: ডেটা সায়েন্স লাইফসাইকেল (পাঠ ১৪-১৬)
- **সপ্তাহ ৯**: ক্লাউড ডেটা সায়েন্স (পাঠ ১৭-১৯)
- **সপ্তাহ ১০**: বাস্তব জীবনের প্রয়োগ এবং চূড়ান্ত প্রকল্প (পাঠ ২০)

### অফলাইনে অ্যাক্সেসের জন্য Docsify চালানো

```bash
# Serve documentation locally for classroom use
docsify serve

# Students can access at localhost:3000
# No internet required after initial setup
```

### অ্যাসাইনমেন্ট গ্রেডিং

- শিক্ষার্থীদের নোটবুক পর্যালোচনা করুন যাতে সম্পন্ন অনুশীলনগুলি থাকে
- কুইজ স্কোরের মাধ্যমে বোঝাপড়া পরীক্ষা করুন
- ডেটা সায়েন্স লাইফসাইকেল নীতিগুলি ব্যবহার করে চূড়ান্ত প্রকল্প মূল্যায়ন করুন

### অ্যাসাইনমেন্ট তৈরি করা

```python
# Example custom assignment template
"""
Assignment: [Topic]

Objective: [Learning goal]

Dataset: [Provide or have students find one]

Tasks:
1. Load and explore the dataset
2. Clean and prepare the data
3. Create at least 3 visualizations
4. Perform analysis
5. Communicate findings

Deliverables:
- Jupyter notebook with code and explanations
- Written summary of findings
"""
```

## অফলাইনে কাজ করা

### রিসোর্স ডাউনলোড করুন

```bash
# Clone the entire repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Download datasets in advance
# Most datasets are included in the repository
```

### স্থানীয়ভাবে ডকুমেন্টেশন চালান

```bash
# Serve with Docsify
docsify serve

# Access at localhost:3000
```

### স্থানীয়ভাবে কুইজ অ্যাপ চালান

```bash
cd quiz-app
npm run serve
```

## অনুবাদিত বিষয়বস্তু অ্যাক্সেস করা

অনুবাদগুলি ৪০+ ভাষায় উপলব্ধ:

```bash
# Access translated lessons
cd translations/fr  # French
cd translations/es  # Spanish
cd translations/de  # German
# ... and many more
```

প্রতিটি অনুবাদ ইংরেজি সংস্করণের মতো একই কাঠামো বজায় রাখে।

## অতিরিক্ত রিসোর্স

### শেখা চালিয়ে যান

- [Microsoft Learn](https://docs.microsoft.com/learn/) - অতিরিক্ত শেখার পথ
- [Student Hub](https://docs.microsoft.com/learn/student-hub) - শিক্ষার্থীদের জন্য রিসোর্স
- [Azure AI Foundry](https://aka.ms/foundry/forum) - কমিউনিটি ফোরাম

### সম্পর্কিত কারিকুলাম

- [AI for Beginners](https://aka.ms/ai-beginners)
- [ML for Beginners](https://aka.ms/ml-beginners)
- [Web Dev for Beginners](https://aka.ms/webdev-beginners)
- [Generative AI for Beginners](https://aka.ms/genai-beginners)

## সাহায্য পাওয়া

- সাধারণ সমস্যার জন্য [TROUBLESHOOTING.md](TROUBLESHOOTING.md) পরীক্ষা করুন
- [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues) অনুসন্ধান করুন
- আমাদের [Discord](https://aka.ms/ds4beginners/discord)-এ যোগ দিন
- সমস্যা রিপোর্ট করতে বা অবদান রাখতে [CONTRIBUTING.md](CONTRIBUTING.md) পর্যালোচনা করুন

---

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসাধ্য সঠিকতার জন্য চেষ্টা করি, তবে অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল ভাষায় থাকা নথিটিকে প্রামাণিক উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য, পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদ ব্যবহারের ফলে কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যা হলে আমরা দায়বদ্ধ থাকব না।