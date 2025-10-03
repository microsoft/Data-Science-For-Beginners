<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f546349678757508d69ce9e1d2688446",
  "translation_date": "2025-10-03T14:53:38+00:00",
  "source_file": "USAGE.md",
  "language_code": "fa"
}
-->
# راهنمای استفاده

این راهنما مثال‌ها و جریان‌های کاری رایج برای استفاده از برنامه درسی «علم داده برای مبتدیان» را ارائه می‌دهد.

## فهرست مطالب

- [چگونه از این برنامه درسی استفاده کنیم](../..)
- [کار با درس‌ها](../..)
- [کار با دفترچه‌های Jupyter](../..)
- [استفاده از برنامه آزمون](../..)
- [جریان‌های کاری رایج](../..)
- [نکات برای یادگیرندگان مستقل](../..)
- [نکات برای معلمان](../..)

## چگونه از این برنامه درسی استفاده کنیم

این برنامه درسی به گونه‌ای طراحی شده است که انعطاف‌پذیر باشد و می‌توان از آن به روش‌های مختلف استفاده کرد:

- **یادگیری خودمحور**: درس‌ها را به صورت مستقل و با سرعت خودتان پیش ببرید
- **آموزش در کلاس درس**: استفاده به عنوان یک دوره ساختاریافته با آموزش هدایت‌شده
- **گروه‌های مطالعه**: یادگیری به صورت گروهی با همتایان
- **فرمت کارگاه**: جلسات یادگیری کوتاه‌مدت و فشرده

## کار با درس‌ها

هر درس دارای ساختاری ثابت است تا یادگیری را به حداکثر برساند:

### ساختار درس

1. **آزمون پیش از درس**: دانش موجود خود را آزمایش کنید
2. **Sketchnote** (اختیاری): خلاصه تصویری از مفاهیم کلیدی
3. **ویدیو** (اختیاری): محتوای ویدیویی مکمل
4. **درس نوشتاری**: مفاهیم اصلی و توضیحات
5. **دفترچه Jupyter**: تمرین‌های کدنویسی عملی
6. **تکلیف**: تمرین آنچه آموخته‌اید
7. **آزمون پس از درس**: درک خود را تقویت کنید

### جریان کاری نمونه برای یک درس

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

## کار با دفترچه‌های Jupyter

### شروع Jupyter

```bash
# Activate your virtual environment
source venv/bin/activate  # On macOS/Linux
# OR
venv\Scripts\activate  # On Windows

# Start Jupyter from the repository root
jupyter notebook
```

### اجرای سلول‌های دفترچه

1. **اجرای یک سلول**: کلیدهای `Shift + Enter` را فشار دهید یا روی دکمه "Run" کلیک کنید
2. **اجرای همه سلول‌ها**: از منو گزینه "Cell" → "Run All" را انتخاب کنید
3. **راه‌اندازی مجدد کرنل**: اگر با مشکلی مواجه شدید، گزینه "Kernel" → "Restart" را انتخاب کنید

### مثال: کار با داده‌ها در یک دفترچه

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

### ذخیره کار شما

- Jupyter به صورت دوره‌ای به طور خودکار ذخیره می‌کند
- ذخیره دستی: کلیدهای `Ctrl + S` (یا `Cmd + S` در macOS) را فشار دهید
- پیشرفت شما در فایل `.ipynb` ذخیره می‌شود

## استفاده از برنامه آزمون

### اجرای برنامه آزمون به صورت محلی

```bash
# Navigate to quiz app directory
cd quiz-app

# Start the development server
npm run serve

# Access at http://localhost:8080
```

### انجام آزمون‌ها

1. آزمون‌های پیش از درس در بالای هر درس لینک شده‌اند
2. آزمون‌های پس از درس در پایین هر درس لینک شده‌اند
3. هر آزمون شامل 3 سؤال است
4. آزمون‌ها برای تقویت یادگیری طراحی شده‌اند، نه برای ارزیابی جامع

### شماره‌گذاری آزمون‌ها

- آزمون‌ها از 0 تا 39 شماره‌گذاری شده‌اند (در مجموع 40 آزمون)
- هر درس معمولاً یک آزمون پیش و پس دارد
- URL‌های آزمون شامل شماره آزمون هستند: `https://ff-quizzes.netlify.app/en/ds/quiz/0`

## جریان‌های کاری رایج

### جریان کاری 1: مسیر مبتدی کامل

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

### جریان کاری 2: یادگیری موضوعی

اگر به یک موضوع خاص علاقه‌مند هستید:

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

### جریان کاری 3: یادگیری مبتنی بر پروژه

```bash
# 1. Review the Data Science Lifecycle lessons (14-16)
cd 4-Data-Science-Lifecycle

# 2. Work through a real-world example (Lesson 20)
cd ../6-Data-Science-In-Wild/20-Real-World-Examples

# 3. Apply concepts to your own project
```

### جریان کاری 4: علم داده مبتنی بر ابر

```bash
# Learn about cloud data science (Lessons 17-19)
cd 5-Data-Science-In-Cloud

# 17: Introduction to Cloud Data Science
# 18: Low-Code ML Tools
# 19: Azure Machine Learning Studio
```

## نکات برای یادگیرندگان مستقل

### سازماندهی بمانید

```bash
# Create a learning journal
mkdir my-learning-journal

# For each lesson, create notes
echo "# Lesson 1 Notes" > my-learning-journal/lesson-01-notes.md
```

### تمرین منظم

- هر روز یا هفته زمان مشخصی را اختصاص دهید
- حداقل یک درس در هفته را کامل کنید
- درس‌های قبلی را به صورت دوره‌ای مرور کنید

### تعامل با جامعه

- به [جامعه Discord](https://aka.ms/ds4beginners/discord) بپیوندید
- در کانال #Data-Science-for-Beginners در Discord شرکت کنید [بحث‌های Discord](https://aka.ms/ds4beginners/discord)
- پیشرفت خود را به اشتراک بگذارید و سوالات خود را مطرح کنید

### پروژه‌های خود را بسازید

پس از تکمیل درس‌ها، مفاهیم را در پروژه‌های شخصی اعمال کنید:

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

## نکات برای معلمان

### تنظیم کلاس درس

1. [for-teachers.md](for-teachers.md) را برای راهنمایی دقیق مرور کنید
2. یک محیط مشترک (GitHub Classroom یا Codespaces) راه‌اندازی کنید
3. یک کانال ارتباطی (Discord، Slack یا Teams) ایجاد کنید

### برنامه‌ریزی درس‌ها

**برنامه پیشنهادی 10 هفته‌ای:**

- **هفته 1-2**: مقدمه (درس‌های 1-4)
- **هفته 3-4**: کار با داده‌ها (درس‌های 5-8)
- **هفته 5-6**: مصورسازی داده‌ها (درس‌های 9-13)
- **هفته 7-8**: چرخه عمر علم داده (درس‌های 14-16)
- **هفته 9**: علم داده ابری (درس‌های 17-19)
- **هفته 10**: کاربردهای واقعی و پروژه‌های نهایی (درس 20)

### اجرای Docsify برای دسترسی آفلاین

```bash
# Serve documentation locally for classroom use
docsify serve

# Students can access at localhost:3000
# No internet required after initial setup
```

### ارزیابی تکالیف

- دفترچه‌های دانش‌آموزان را برای تمرین‌های کامل شده مرور کنید
- درک را از طریق نمرات آزمون بررسی کنید
- پروژه‌های نهایی را با استفاده از اصول چرخه عمر علم داده ارزیابی کنید

### ایجاد تکالیف

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

## کار به صورت آفلاین

### دانلود منابع

```bash
# Clone the entire repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Download datasets in advance
# Most datasets are included in the repository
```

### اجرای مستندات به صورت محلی

```bash
# Serve with Docsify
docsify serve

# Access at localhost:3000
```

### اجرای برنامه آزمون به صورت محلی

```bash
cd quiz-app
npm run serve
```

## دسترسی به محتوای ترجمه شده

ترجمه‌ها در بیش از 40 زبان موجود هستند:

```bash
# Access translated lessons
cd translations/fr  # French
cd translations/es  # Spanish
cd translations/de  # German
# ... and many more
```

هر ترجمه همان ساختار نسخه انگلیسی را حفظ می‌کند.

## منابع اضافی

### ادامه یادگیری

- [Microsoft Learn](https://docs.microsoft.com/learn/) - مسیرهای یادگیری اضافی
- [Student Hub](https://docs.microsoft.com/learn/student-hub) - منابع برای دانش‌آموزان
- [Azure AI Foundry](https://aka.ms/foundry/forum) - انجمن جامعه

### برنامه‌های درسی مرتبط

- [AI برای مبتدیان](https://aka.ms/ai-beginners)
- [ML برای مبتدیان](https://aka.ms/ml-beginners)
- [توسعه وب برای مبتدیان](https://aka.ms/webdev-beginners)
- [هوش مصنوعی مولد برای مبتدیان](https://aka.ms/genai-beginners)

## دریافت کمک

- [TROUBLESHOOTING.md](TROUBLESHOOTING.md) را برای مشکلات رایج بررسی کنید
- [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues) را جستجو کنید
- به [Discord](https://aka.ms/ds4beginners/discord) ما بپیوندید
- [CONTRIBUTING.md](CONTRIBUTING.md) را مرور کنید تا مشکلات را گزارش دهید یا مشارکت کنید

---

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما تلاش می‌کنیم دقت را حفظ کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌ها باشند. سند اصلی به زبان اصلی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس، توصیه می‌شود از ترجمه انسانی حرفه‌ای استفاده کنید. ما مسئولیتی در قبال سوء تفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.