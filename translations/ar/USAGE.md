<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f546349678757508d69ce9e1d2688446",
  "translation_date": "2025-10-03T14:53:12+00:00",
  "source_file": "USAGE.md",
  "language_code": "ar"
}
-->
# دليل الاستخدام

يوفر هذا الدليل أمثلة ومسارات عمل شائعة لاستخدام منهج "علم البيانات للمبتدئين".

## جدول المحتويات

- [كيفية استخدام هذا المنهج](../..)
- [العمل مع الدروس](../..)
- [العمل مع دفاتر Jupyter](../..)
- [استخدام تطبيق الاختبارات](../..)
- [مسارات العمل الشائعة](../..)
- [نصائح للمتعلمين ذاتيًا](../..)
- [نصائح للمعلمين](../..)

## كيفية استخدام هذا المنهج

تم تصميم هذا المنهج ليكون مرنًا ويمكن استخدامه بطرق متعددة:

- **التعلم الذاتي**: العمل على الدروس بشكل مستقل وبالسرعة التي تناسبك.
- **التدريس في الفصل الدراسي**: استخدامه كدورة منظمة مع تعليم موجه.
- **مجموعات الدراسة**: التعلم بشكل تعاوني مع الأقران.
- **ورش العمل**: جلسات تعليم مكثفة قصيرة المدى.

## العمل مع الدروس

كل درس يتبع هيكلًا ثابتًا لتعظيم الفائدة التعليمية:

### هيكل الدرس

1. **اختبار ما قبل الدرس**: اختبار معرفتك الحالية.
2. **رسم تخطيطي** (اختياري): ملخص بصري للمفاهيم الرئيسية.
3. **فيديو** (اختياري): محتوى فيديو إضافي.
4. **الدرس المكتوب**: المفاهيم الأساسية والتفسيرات.
5. **دفتر Jupyter**: تمارين عملية للبرمجة.
6. **التكليف**: ممارسة ما تعلمته.
7. **اختبار ما بعد الدرس**: تعزيز فهمك.

### مثال على مسار عمل للدرس

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

## العمل مع دفاتر Jupyter

### بدء تشغيل Jupyter

```bash
# Activate your virtual environment
source venv/bin/activate  # On macOS/Linux
# OR
venv\Scripts\activate  # On Windows

# Start Jupyter from the repository root
jupyter notebook
```

### تشغيل خلايا الدفتر

1. **تشغيل خلية**: اضغط على `Shift + Enter` أو انقر على زر "Run".
2. **تشغيل جميع الخلايا**: اختر "Cell" → "Run All" من القائمة.
3. **إعادة تشغيل النواة**: اختر "Kernel" → "Restart" إذا واجهت مشاكل.

### مثال: العمل مع البيانات في دفتر

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

### حفظ عملك

- يقوم Jupyter بالحفظ التلقائي بشكل دوري.
- الحفظ يدويًا: اضغط على `Ctrl + S` (أو `Cmd + S` على macOS).
- يتم حفظ تقدمك في ملف `.ipynb`.

## استخدام تطبيق الاختبارات

### تشغيل تطبيق الاختبارات محليًا

```bash
# Navigate to quiz app directory
cd quiz-app

# Start the development server
npm run serve

# Access at http://localhost:8080
```

### إجراء الاختبارات

1. يتم ربط اختبارات ما قبل الدرس في بداية كل درس.
2. يتم ربط اختبارات ما بعد الدرس في نهاية كل درس.
3. يحتوي كل اختبار على 3 أسئلة.
4. تم تصميم الاختبارات لتعزيز التعلم وليس للاختبار الشامل.

### ترقيم الاختبارات

- يتم ترقيم الاختبارات من 0 إلى 39 (إجمالي 40 اختبارًا).
- يحتوي كل درس عادةً على اختبار ما قبل وما بعد.
- تتضمن روابط الاختبارات رقم الاختبار: `https://ff-quizzes.netlify.app/en/ds/quiz/0`

## مسارات العمل الشائعة

### المسار 1: طريق المبتدئين بالكامل

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

### المسار 2: التعلم حسب الموضوع

إذا كنت مهتمًا بموضوع معين:

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

### المسار 3: التعلم القائم على المشاريع

```bash
# 1. Review the Data Science Lifecycle lessons (14-16)
cd 4-Data-Science-Lifecycle

# 2. Work through a real-world example (Lesson 20)
cd ../6-Data-Science-In-Wild/20-Real-World-Examples

# 3. Apply concepts to your own project
```

### المسار 4: علم البيانات القائم على السحابة

```bash
# Learn about cloud data science (Lessons 17-19)
cd 5-Data-Science-In-Cloud

# 17: Introduction to Cloud Data Science
# 18: Low-Code ML Tools
# 19: Azure Machine Learning Studio
```

## نصائح للمتعلمين ذاتيًا

### التنظيم

```bash
# Create a learning journal
mkdir my-learning-journal

# For each lesson, create notes
echo "# Lesson 1 Notes" > my-learning-journal/lesson-01-notes.md
```

### الممارسة بانتظام

- خصص وقتًا محددًا يوميًا أو أسبوعيًا.
- أكمل درسًا واحدًا على الأقل أسبوعيًا.
- راجع الدروس السابقة بشكل دوري.

### التفاعل مع المجتمع

- انضم إلى [مجتمع Discord](https://aka.ms/ds4beginners/discord).
- شارك في قناة #Data-Science-for-Beginners في Discord [مناقشات Discord](https://aka.ms/ds4beginners/discord).
- شارك تقدمك واطرح الأسئلة.

### بناء مشاريعك الخاصة

بعد إكمال الدروس، قم بتطبيق المفاهيم على مشاريع شخصية:

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

## نصائح للمعلمين

### إعداد الفصل الدراسي

1. راجع [for-teachers.md](for-teachers.md) للحصول على إرشادات مفصلة.
2. قم بإعداد بيئة مشتركة (GitHub Classroom أو Codespaces).
3. أنشئ قناة اتصال (Discord، Slack، أو Teams).

### تخطيط الدروس

**الجدول المقترح لمدة 10 أسابيع:**

- **الأسبوع 1-2**: المقدمة (الدروس 1-4).
- **الأسبوع 3-4**: العمل مع البيانات (الدروس 5-8).
- **الأسبوع 5-6**: تصور البيانات (الدروس 9-13).
- **الأسبوع 7-8**: دورة حياة علم البيانات (الدروس 14-16).
- **الأسبوع 9**: علم البيانات السحابي (الدروس 17-19).
- **الأسبوع 10**: التطبيقات الواقعية والمشاريع النهائية (الدرس 20).

### تشغيل Docsify للوصول دون اتصال

```bash
# Serve documentation locally for classroom use
docsify serve

# Students can access at localhost:3000
# No internet required after initial setup
```

### تقييم التكليفات

- مراجعة دفاتر الطلاب للتحقق من التمارين المكتملة.
- التحقق من الفهم من خلال درجات الاختبارات.
- تقييم المشاريع النهائية باستخدام مبادئ دورة حياة علم البيانات.

### إنشاء التكليفات

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

## العمل دون اتصال

### تنزيل الموارد

```bash
# Clone the entire repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Download datasets in advance
# Most datasets are included in the repository
```

### تشغيل الوثائق محليًا

```bash
# Serve with Docsify
docsify serve

# Access at localhost:3000
```

### تشغيل تطبيق الاختبارات محليًا

```bash
cd quiz-app
npm run serve
```

## الوصول إلى المحتوى المترجم

تتوفر الترجمات بأكثر من 40 لغة:

```bash
# Access translated lessons
cd translations/fr  # French
cd translations/es  # Spanish
cd translations/de  # German
# ... and many more
```

تحافظ كل ترجمة على نفس هيكل النسخة الإنجليزية.

## موارد إضافية

### مواصلة التعلم

- [Microsoft Learn](https://docs.microsoft.com/learn/) - مسارات تعلم إضافية.
- [Student Hub](https://docs.microsoft.com/learn/student-hub) - موارد للطلاب.
- [Azure AI Foundry](https://aka.ms/foundry/forum) - منتدى المجتمع.

### المناهج ذات الصلة

- [الذكاء الاصطناعي للمبتدئين](https://aka.ms/ai-beginners).
- [تعلم الآلة للمبتدئين](https://aka.ms/ml-beginners).
- [تطوير الويب للمبتدئين](https://aka.ms/webdev-beginners).
- [الذكاء الاصطناعي التوليدي للمبتدئين](https://aka.ms/genai-beginners).

## الحصول على المساعدة

- تحقق من [TROUBLESHOOTING.md](TROUBLESHOOTING.md) للمشاكل الشائعة.
- ابحث في [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues).
- انضم إلى [Discord](https://aka.ms/ds4beginners/discord).
- راجع [CONTRIBUTING.md](CONTRIBUTING.md) للإبلاغ عن المشاكل أو المساهمة.

---

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي. للحصول على معلومات حاسمة، يُوصى بالترجمة البشرية الاحترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة ناتجة عن استخدام هذه الترجمة.