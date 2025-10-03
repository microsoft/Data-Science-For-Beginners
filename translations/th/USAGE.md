<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f546349678757508d69ce9e1d2688446",
  "translation_date": "2025-10-03T15:03:15+00:00",
  "source_file": "USAGE.md",
  "language_code": "th"
}
-->
# คู่มือการใช้งาน

คู่มือนี้ให้ตัวอย่างและขั้นตอนการทำงานทั่วไปสำหรับการใช้หลักสูตร Data Science for Beginners

## สารบัญ

- [วิธีการใช้หลักสูตรนี้](../..)
- [การทำงานกับบทเรียน](../..)
- [การทำงานกับ Jupyter Notebooks](../..)
- [การใช้แอปพลิเคชันแบบทดสอบ](../..)
- [ขั้นตอนการทำงานทั่วไป](../..)
- [เคล็ดลับสำหรับผู้เรียนด้วยตนเอง](../..)
- [เคล็ดลับสำหรับครู](../..)

## วิธีการใช้หลักสูตรนี้

หลักสูตรนี้ออกแบบมาให้มีความยืดหยุ่นและสามารถใช้งานได้หลายวิธี:

- **การเรียนรู้ด้วยตนเอง**: ทำบทเรียนด้วยตัวเองตามความเร็วของคุณ
- **การสอนในห้องเรียน**: ใช้เป็นหลักสูตรที่มีการสอนแบบมีโครงสร้าง
- **กลุ่มศึกษา**: เรียนรู้ร่วมกันกับเพื่อน
- **รูปแบบเวิร์กช็อป**: การเรียนรู้แบบเข้มข้นในระยะเวลาสั้น

## การทำงานกับบทเรียน

แต่ละบทเรียนมีโครงสร้างที่สม่ำเสมอเพื่อเพิ่มประสิทธิภาพการเรียนรู้:

### โครงสร้างบทเรียน

1. **แบบทดสอบก่อนบทเรียน**: ทดสอบความรู้ที่มีอยู่
2. **Sketchnote** (ตัวเลือก): สรุปภาพรวมของแนวคิดสำคัญ
3. **วิดีโอ** (ตัวเลือก): เนื้อหาเสริมในรูปแบบวิดีโอ
4. **บทเรียนที่เขียน**: แนวคิดหลักและคำอธิบาย
5. **Jupyter Notebook**: แบบฝึกหัดการเขียนโค้ด
6. **การบ้าน**: ฝึกฝนสิ่งที่คุณเรียนรู้
7. **แบบทดสอบหลังบทเรียน**: เสริมสร้างความเข้าใจ

### ตัวอย่างขั้นตอนการทำงานสำหรับบทเรียน

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

## การทำงานกับ Jupyter Notebooks

### การเริ่มต้น Jupyter

```bash
# Activate your virtual environment
source venv/bin/activate  # On macOS/Linux
# OR
venv\Scripts\activate  # On Windows

# Start Jupyter from the repository root
jupyter notebook
```

### การรันเซลใน Notebook

1. **รันเซล**: กด `Shift + Enter` หรือคลิกปุ่ม "Run"
2. **รันทุกเซล**: เลือก "Cell" → "Run All" จากเมนู
3. **รีสตาร์ทเคอร์เนล**: เลือก "Kernel" → "Restart" หากพบปัญหา

### ตัวอย่าง: การทำงานกับข้อมูลใน Notebook

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

### การบันทึกงานของคุณ

- Jupyter บันทึกอัตโนมัติเป็นระยะ
- บันทึกด้วยตนเอง: กด `Ctrl + S` (หรือ `Cmd + S` บน macOS)
- ความคืบหน้าของคุณจะถูกบันทึกในไฟล์ `.ipynb`

## การใช้แอปพลิเคชันแบบทดสอบ

### การรันแอปแบบทดสอบในเครื่อง

```bash
# Navigate to quiz app directory
cd quiz-app

# Start the development server
npm run serve

# Access at http://localhost:8080
```

### การทำแบบทดสอบ

1. แบบทดสอบก่อนบทเรียนจะลิงก์ไว้ที่ด้านบนของแต่ละบทเรียน
2. แบบทดสอบหลังบทเรียนจะลิงก์ไว้ที่ด้านล่างของแต่ละบทเรียน
3. แต่ละแบบทดสอบมี 3 คำถาม
4. แบบทดสอบออกแบบมาเพื่อเสริมสร้างการเรียนรู้ ไม่ใช่การทดสอบอย่างละเอียด

### การกำหนดหมายเลขแบบทดสอบ

- แบบทดสอบมีหมายเลข 0-39 (รวมทั้งหมด 40 แบบทดสอบ)
- แต่ละบทเรียนมักมีแบบทดสอบก่อนและหลัง
- URL ของแบบทดสอบมีหมายเลขแบบทดสอบ: `https://ff-quizzes.netlify.app/en/ds/quiz/0`

## ขั้นตอนการทำงานทั่วไป

### ขั้นตอนการทำงาน 1: เส้นทางสำหรับผู้เริ่มต้น

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

### ขั้นตอนการทำงาน 2: การเรียนรู้เฉพาะหัวข้อ

หากคุณสนใจหัวข้อเฉพาะ:

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

### ขั้นตอนการทำงาน 3: การเรียนรู้แบบโครงการ

```bash
# 1. Review the Data Science Lifecycle lessons (14-16)
cd 4-Data-Science-Lifecycle

# 2. Work through a real-world example (Lesson 20)
cd ../6-Data-Science-In-Wild/20-Real-World-Examples

# 3. Apply concepts to your own project
```

### ขั้นตอนการทำงาน 4: Data Science บนคลาวด์

```bash
# Learn about cloud data science (Lessons 17-19)
cd 5-Data-Science-In-Cloud

# 17: Introduction to Cloud Data Science
# 18: Low-Code ML Tools
# 19: Azure Machine Learning Studio
```

## เคล็ดลับสำหรับผู้เรียนด้วยตนเอง

### จัดระเบียบตัวเอง

```bash
# Create a learning journal
mkdir my-learning-journal

# For each lesson, create notes
echo "# Lesson 1 Notes" > my-learning-journal/lesson-01-notes.md
```

### ฝึกฝนอย่างสม่ำเสมอ

- กำหนดเวลาที่แน่นอนในแต่ละวันหรือสัปดาห์
- ทำบทเรียนอย่างน้อยหนึ่งบทต่อสัปดาห์
- ทบทวนบทเรียนก่อนหน้าเป็นระยะ

### มีส่วนร่วมกับชุมชน

- เข้าร่วม [ชุมชน Discord](https://aka.ms/ds4beginners/discord)
- มีส่วนร่วมในช่อง #Data-Science-for-Beginners ใน Discord [การสนทนาใน Discord](https://aka.ms/ds4beginners/discord)
- แบ่งปันความคืบหน้าและถามคำถาม

### สร้างโครงการของคุณเอง

หลังจากทำบทเรียนเสร็จแล้ว ให้นำแนวคิดไปใช้กับโครงการส่วนตัว:

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

## เคล็ดลับสำหรับครู

### การตั้งค่าห้องเรียน

1. ทบทวน [for-teachers.md](for-teachers.md) สำหรับคำแนะนำโดยละเอียด
2. ตั้งค่าสภาพแวดล้อมที่ใช้ร่วมกัน (GitHub Classroom หรือ Codespaces)
3. สร้างช่องทางการสื่อสาร (Discord, Slack หรือ Teams)

### การวางแผนบทเรียน

**ตารางเวลาแนะนำ 10 สัปดาห์:**

- **สัปดาห์ที่ 1-2**: บทนำ (บทเรียน 1-4)
- **สัปดาห์ที่ 3-4**: การทำงานกับข้อมูล (บทเรียน 5-8)
- **สัปดาห์ที่ 5-6**: การสร้างภาพข้อมูล (บทเรียน 9-13)
- **สัปดาห์ที่ 7-8**: วงจรชีวิต Data Science (บทเรียน 14-16)
- **สัปดาห์ที่ 9**: Data Science บนคลาวด์ (บทเรียน 17-19)
- **สัปดาห์ที่ 10**: การใช้งานจริงและโครงการสุดท้าย (บทเรียน 20)

### การรัน Docsify สำหรับการเข้าถึงแบบออฟไลน์

```bash
# Serve documentation locally for classroom use
docsify serve

# Students can access at localhost:3000
# No internet required after initial setup
```

### การให้คะแนนการบ้าน

- ทบทวน Notebook ของนักเรียนสำหรับแบบฝึกหัดที่เสร็จสมบูรณ์
- ตรวจสอบความเข้าใจผ่านคะแนนแบบทดสอบ
- ประเมินโครงการสุดท้ายโดยใช้หลักการวงจรชีวิต Data Science

### การสร้างการบ้าน

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

## การทำงานแบบออฟไลน์

### ดาวน์โหลดทรัพยากร

```bash
# Clone the entire repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Download datasets in advance
# Most datasets are included in the repository
```

### รันเอกสารในเครื่อง

```bash
# Serve with Docsify
docsify serve

# Access at localhost:3000
```

### รันแอปแบบทดสอบในเครื่อง

```bash
cd quiz-app
npm run serve
```

## การเข้าถึงเนื้อหาที่แปลแล้ว

มีการแปลเนื้อหาในกว่า 40 ภาษา:

```bash
# Access translated lessons
cd translations/fr  # French
cd translations/es  # Spanish
cd translations/de  # German
# ... and many more
```

การแปลแต่ละภาษามีโครงสร้างเหมือนกับเวอร์ชันภาษาอังกฤษ

## ทรัพยากรเพิ่มเติม

### เรียนรู้ต่อไป

- [Microsoft Learn](https://docs.microsoft.com/learn/) - เส้นทางการเรียนรู้เพิ่มเติม
- [Student Hub](https://docs.microsoft.com/learn/student-hub) - ทรัพยากรสำหรับนักเรียน
- [Azure AI Foundry](https://aka.ms/foundry/forum) - ฟอรัมชุมชน

### หลักสูตรที่เกี่ยวข้อง

- [AI for Beginners](https://aka.ms/ai-beginners)
- [ML for Beginners](https://aka.ms/ml-beginners)
- [Web Dev for Beginners](https://aka.ms/webdev-beginners)
- [Generative AI for Beginners](https://aka.ms/genai-beginners)

## การขอความช่วยเหลือ

- ตรวจสอบ [TROUBLESHOOTING.md](TROUBLESHOOTING.md) สำหรับปัญหาทั่วไป
- ค้นหา [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
- เข้าร่วม [Discord](https://aka.ms/ds4beginners/discord)
- ทบทวน [CONTRIBUTING.md](CONTRIBUTING.md) เพื่อรายงานปัญหาหรือมีส่วนร่วม

---

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้อง แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้บริการแปลภาษามนุษย์ที่เป็นมืออาชีพ เราจะไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดพลาดที่เกิดจากการใช้การแปลนี้