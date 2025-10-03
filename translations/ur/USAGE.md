<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f546349678757508d69ce9e1d2688446",
  "translation_date": "2025-10-03T14:54:00+00:00",
  "source_file": "USAGE.md",
  "language_code": "ur"
}
-->
# استعمال کی رہنمائی

یہ رہنمائی ڈیٹا سائنس فار بیگنرز نصاب کے استعمال کے لیے مثالیں اور عام ورک فلو فراہم کرتی ہے۔

## مواد کی فہرست

- [اس نصاب کو کیسے استعمال کریں](../..)
- [سبق کے ساتھ کام کرنا](../..)
- [جوپیٹر نوٹ بکس کے ساتھ کام کرنا](../..)
- [کوئز ایپلیکیشن کا استعمال](../..)
- [عام ورک فلو](../..)
- [خود سیکھنے والوں کے لیے تجاویز](../..)
- [اساتذہ کے لیے تجاویز](../..)

## اس نصاب کو کیسے استعمال کریں

یہ نصاب لچکدار ہے اور مختلف طریقوں سے استعمال کیا جا سکتا ہے:

- **خود سے سیکھنا**: سبق کو اپنی رفتار سے آزادانہ طور پر مکمل کریں
- **کلاس روم انسٹرکشن**: ہدایت کے ساتھ ایک منظم کورس کے طور پر استعمال کریں
- **مطالعہ گروپس**: ساتھیوں کے ساتھ مل کر سیکھیں
- **ورکشاپ فارمیٹ**: مختصر مدت کے لیے گہرائی سے سیکھنے کے سیشنز

## سبق کے ساتھ کام کرنا

ہر سبق ایک مستقل ساخت کی پیروی کرتا ہے تاکہ سیکھنے کو زیادہ سے زیادہ کیا جا سکے:

### سبق کی ساخت

1. **سبق سے پہلے کا کوئز**: اپنی موجودہ معلومات کا امتحان لیں
2. **اسکیچ نوٹ** (اختیاری): اہم تصورات کا بصری خلاصہ
3. **ویڈیو** (اختیاری): اضافی ویڈیو مواد
4. **تحریری سبق**: بنیادی تصورات اور وضاحتیں
5. **جوپیٹر نوٹ بک**: عملی کوڈنگ مشقیں
6. **اسائنمنٹ**: جو کچھ سیکھا ہے اس پر عمل کریں
7. **سبق کے بعد کا کوئز**: اپنی سمجھ کو مضبوط کریں

### سبق کے لیے مثال ورک فلو

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

## جوپیٹر نوٹ بکس کے ساتھ کام کرنا

### جوپیٹر شروع کرنا

```bash
# Activate your virtual environment
source venv/bin/activate  # On macOS/Linux
# OR
venv\Scripts\activate  # On Windows

# Start Jupyter from the repository root
jupyter notebook
```

### نوٹ بک سیلز چلانا

1. **سیل چلائیں**: `Shift + Enter` دبائیں یا "Run" بٹن پر کلک کریں
2. **تمام سیلز چلائیں**: مینو سے "Cell" → "Run All" منتخب کریں
3. **کرنل ری اسٹارٹ کریں**: اگر مسائل پیش آئیں تو "Kernel" → "Restart" منتخب کریں

### مثال: نوٹ بک میں ڈیٹا کے ساتھ کام کرنا

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

### اپنا کام محفوظ کرنا

- جوپیٹر وقتاً فوقتاً خود بخود محفوظ کرتا ہے
- دستی طور پر محفوظ کریں: `Ctrl + S` دبائیں (یا macOS پر `Cmd + S`)
- آپ کی پیش رفت `.ipynb` فائل میں محفوظ ہوتی ہے

## کوئز ایپلیکیشن کا استعمال

### کوئز ایپ کو مقامی طور پر چلانا

```bash
# Navigate to quiz app directory
cd quiz-app

# Start the development server
npm run serve

# Access at http://localhost:8080
```

### کوئز لینا

1. سبق سے پہلے کے کوئز ہر سبق کے آغاز میں دیے گئے ہیں
2. سبق کے بعد کے کوئز ہر سبق کے آخر میں دیے گئے ہیں
3. ہر کوئز میں 3 سوالات ہوتے ہیں
4. کوئز سیکھنے کو مضبوط کرنے کے لیے بنائے گئے ہیں، نہ کہ مکمل امتحان کے لیے

### کوئز کی نمبرنگ

- کوئز 0-39 تک نمبر دیے گئے ہیں (کل 40 کوئز)
- ہر سبق میں عام طور پر ایک سبق سے پہلے اور بعد کا کوئز ہوتا ہے
- کوئز URLs میں کوئز نمبر شامل ہوتا ہے: `https://ff-quizzes.netlify.app/en/ds/quiz/0`

## عام ورک فلو

### ورک فلو 1: مکمل ابتدائی راستہ

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

### ورک فلو 2: موضوع پر مبنی سیکھنا

اگر آپ کسی خاص موضوع میں دلچسپی رکھتے ہیں:

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

### ورک فلو 3: پروجیکٹ پر مبنی سیکھنا

```bash
# 1. Review the Data Science Lifecycle lessons (14-16)
cd 4-Data-Science-Lifecycle

# 2. Work through a real-world example (Lesson 20)
cd ../6-Data-Science-In-Wild/20-Real-World-Examples

# 3. Apply concepts to your own project
```

### ورک فلو 4: کلاؤڈ پر مبنی ڈیٹا سائنس

```bash
# Learn about cloud data science (Lessons 17-19)
cd 5-Data-Science-In-Cloud

# 17: Introduction to Cloud Data Science
# 18: Low-Code ML Tools
# 19: Azure Machine Learning Studio
```

## خود سیکھنے والوں کے لیے تجاویز

### منظم رہیں

```bash
# Create a learning journal
mkdir my-learning-journal

# For each lesson, create notes
echo "# Lesson 1 Notes" > my-learning-journal/lesson-01-notes.md
```

### باقاعدگی سے مشق کریں

- ہر دن یا ہفتے کے لیے مخصوص وقت مقرر کریں
- کم از کم ایک سبق ہر ہفتے مکمل کریں
- پچھلے سبق کو وقتاً فوقتاً دوبارہ دیکھیں

### کمیونٹی کے ساتھ جڑیں

- [Discord کمیونٹی](https://aka.ms/ds4beginners/discord) میں شامل ہوں
- Discord میں #Data-Science-for-Beginners چینل میں حصہ لیں [Discord Discussions](https://aka.ms/ds4beginners/discord)
- اپنی پیش رفت شیئر کریں اور سوالات پوچھیں

### اپنے پروجیکٹس بنائیں

سبق مکمل کرنے کے بعد، ذاتی پروجیکٹس پر تصورات کا اطلاق کریں:

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

## اساتذہ کے لیے تجاویز

### کلاس روم سیٹ اپ

1. تفصیلی رہنمائی کے لیے [for-teachers.md](for-teachers.md) کا جائزہ لیں
2. ایک مشترکہ ماحول قائم کریں (GitHub Classroom یا Codespaces)
3. ایک مواصلاتی چینل قائم کریں (Discord، Slack، یا Teams)

### سبق کی منصوبہ بندی

**تجویز کردہ 10 ہفتے کا شیڈول:**

- **ہفتہ 1-2**: تعارف (سبق 1-4)
- **ہفتہ 3-4**: ڈیٹا کے ساتھ کام کرنا (سبق 5-8)
- **ہفتہ 5-6**: ڈیٹا ویژولائزیشن (سبق 9-13)
- **ہفتہ 7-8**: ڈیٹا سائنس لائف سائیکل (سبق 14-16)
- **ہفتہ 9**: کلاؤڈ ڈیٹا سائنس (سبق 17-19)
- **ہفتہ 10**: حقیقی دنیا کی ایپلیکیشنز اور حتمی پروجیکٹس (سبق 20)

### آف لائن رسائی کے لیے Docsify چلانا

```bash
# Serve documentation locally for classroom use
docsify serve

# Students can access at localhost:3000
# No internet required after initial setup
```

### اسائنمنٹ گریڈنگ

- طلباء کی نوٹ بکس کا جائزہ لیں تاکہ مکمل مشقیں دیکھ سکیں
- کوئز کے اسکورز کے ذریعے سمجھ کو چیک کریں
- ڈیٹا سائنس لائف سائیکل اصولوں کا استعمال کرتے ہوئے حتمی پروجیکٹس کا جائزہ لیں

### اسائنمنٹ بنانا

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

## آف لائن کام کرنا

### وسائل ڈاؤن لوڈ کریں

```bash
# Clone the entire repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Download datasets in advance
# Most datasets are included in the repository
```

### دستاویزات کو مقامی طور پر چلائیں

```bash
# Serve with Docsify
docsify serve

# Access at localhost:3000
```

### کوئز ایپ کو مقامی طور پر چلائیں

```bash
cd quiz-app
npm run serve
```

## ترجمہ شدہ مواد تک رسائی

ترجمے 40+ زبانوں میں دستیاب ہیں:

```bash
# Access translated lessons
cd translations/fr  # French
cd translations/es  # Spanish
cd translations/de  # German
# ... and many more
```

ہر ترجمہ انگریزی ورژن کی ساخت کو برقرار رکھتا ہے۔

## اضافی وسائل

### سیکھنا جاری رکھیں

- [Microsoft Learn](https://docs.microsoft.com/learn/) - اضافی سیکھنے کے راستے
- [Student Hub](https://docs.microsoft.com/learn/student-hub) - طلباء کے لیے وسائل
- [Azure AI Foundry](https://aka.ms/foundry/forum) - کمیونٹی فورم

### متعلقہ نصاب

- [AI for Beginners](https://aka.ms/ai-beginners)
- [ML for Beginners](https://aka.ms/ml-beginners)
- [Web Dev for Beginners](https://aka.ms/webdev-beginners)
- [Generative AI for Beginners](https://aka.ms/genai-beginners)

## مدد حاصل کرنا

- عام مسائل کے لیے [TROUBLESHOOTING.md](TROUBLESHOOTING.md) چیک کریں
- [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues) تلاش کریں
- ہمارے [Discord](https://aka.ms/ds4beginners/discord) میں شامل ہوں
- مسائل رپورٹ کرنے یا تعاون کرنے کے لیے [CONTRIBUTING.md](CONTRIBUTING.md) کا جائزہ لیں

---

**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا غیر درستیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔