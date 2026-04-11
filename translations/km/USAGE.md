# Usage Guide

This guide provides examples and common workflows for using the Data Science for Beginners curriculum.

## Table of Contents

- [How to Use This Curriculum](#how-to-use-this-curriculum)
- [Working with Lessons](#working-with-lessons)
- [Working with Jupyter Notebooks](#working-with-jupyter-notebooks)
- [Using the Quiz Application](#using-the-quiz-application)
- [Common Workflows](#common-workflows)
- [Tips for Self-Learners](#tips-for-self-learners)
- [Tips for Teachers](#tips-for-teachers)

## How to Use This Curriculum

This curriculum is designed to be flexible and can be used in multiple ways:

- **Self-paced learning**: Work through lessons independently at your own speed
- **Classroom instruction**: Use as a structured course with guided instruction
- **Study groups**: Learn collaboratively with peers
- **Workshop format**: Intensive short-term learning sessions

## Working with Lessons

Each lesson follows a consistent structure to maximize learning:

### Lesson Structure

1. **Pre-lesson Quiz**: Test your existing knowledge
2. **Sketchnote** (Optional): Visual summary of key concepts
3. **Video** (Optional): Supplemental video content
4. **Written Lesson**: Core concepts and explanations
5. **Jupyter Notebook**: Hands-on coding exercises
6. **Assignment**: Practice what you've learned
7. **Post-lesson Quiz**: Reinforce your understanding

### Example Workflow for a Lesson

```bash
# ១. ទៅកាន់ថតមេរៀន
cd 1-Introduction/01-defining-data-science

# ២. អាន README.md
# បើក README.md នៅក្នុងកម្មវិធីរុករក ឬកម្មវិធីកែសម្រួលរបស់អ្នក

# ៣. ធ្វើការប្រលងមុនមេរៀន
# ចុចលើតំណភ្ជាប់ការប្រលងនៅក្នុង README

# ៤. បើកសៀវភៅកំណត់ត្រា Jupyter (បើមាន)
jupyter notebook

# ៥. បញ្ចប់លំហាត់ក្នុងសៀវភៅកំណត់ត្រា

# ៦. ធ្វើការងារផ្នែកដែលបានផ្ដល់

# ៧. ធ្វើការប្រលងបន្ទាប់ពីមេរៀន
```

## Working with Jupyter Notebooks

### Starting Jupyter

```bash
# បើកប្រព័ន្ធបរិស្ថាននិន្នាការរបស់អ្នក
source venv/bin/activate  # លើ macOS/Linux
# ឬ
venv\Scripts\activate  # លើ Windows

# ចាប់ផ្តើម Jupyter ពីឫសសារមន្ទីរ
jupyter notebook
```

### Running Notebook Cells

1. **Execute a cell**: Press `Shift + Enter` or click the "Run" button
2. **Execute all cells**: Select "Cell" → "Run All" from the menu
3. **Restart kernel**: Select "Kernel" → "Restart" if you encounter issues

### Example: Working with Data in a Notebook

```python
# នាំចូលបណ្ណាល័យដែលត្រូវការ
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ផ្ទុកទិន្នន័យ
df = pd.read_csv('data/sample.csv')

# ស្ទង់មើលទិន្នន័យ
df.head()
df.info()
df.describe()

# បង្កើតការមើលឃើញ
plt.figure(figsize=(10, 6))
plt.plot(df['column_name'])
plt.title('Sample Visualization')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.show()
```

### Saving Your Work

- Jupyter auto-saves periodically
- Manually save: Press `Ctrl + S` (or `Cmd + S` on macOS)
- Your progress is saved in the `.ipynb` file

## Using the Quiz Application

### Running the Quiz App Locally

```bash
# ចូលទៅកាន់ថតកម្មវិធីគ្រាប់សំណួរ
cd quiz-app

# ចាប់ផ្ដើមម៉ាស៊ីនមេអភិវឌ្ឍន៍
npm run serve

# ចូលប្រើនៅ http://localhost:8080
```

### Taking Quizzes

1. Pre-lesson quizzes are linked at the top of each lesson
2. Post-lesson quizzes are linked at the bottom of each lesson
3. Each quiz has 3 questions
4. Quizzes are designed to reinforce learning, not to test exhaustively

### Quiz Numbering

- Quizzes are numbered 0-39 (40 total quizzes)
- Each lesson typically has a pre and post quiz
- Quiz URLs include the quiz number: `https://ff-quizzes.netlify.app/en/ds/quiz/0`

## Common Workflows

### Workflow 1: Complete Beginner Path

```bash
# 1. កំណត់បរិយាកាសរបស់អ្នក (មើល INSTALLATION.md)

# 2. ចាប់ផ្តើមជាមួយមេរៀនទី 1
cd 1-Introduction/01-defining-data-science

# 3. សម្រាប់មេរៀននីមួយៗ:
#    - ធ្វើការប្រលងមុនមេរៀន
#    - អានមាតិការបង្រៀន
#    - ធ្វើការលើសៀវភៅកំណត់ត្រា
#    - បញ្ចប់ការផ្តល់អនុសាសន៍
#    - ធ្វើការប្រលងបន្ទាប់មេរៀន

# 4. ចំណូវតាមរយៈមេរៀនទាំង 20 ដោយលំដាប់លំដោយ
```

### Workflow 2: Topic-Specific Learning

If you're interested in a specific topic:

```bash
# ឧទាហរណ៍៖ ផ្ដោតលើការមើលឃើញទិន្នន័យ
cd 3-Data-Visualization

# សូមស្វែងយល់មេរៀន 9-13៖
# - មេរៀន 9៖ ការមើលឃើញបរិមាណ
# - មេរៀន 10៖ ការមើលឃើញការបែងចែក
# - មេរៀន 11៖ ការមើលឃើញអត្រា
# - មេរៀន 12៖ ការមើលឃើញទំនាក់ទំនង
# - មេរៀន 13៖ ការមើលឃើញមានអត្ថន័យ
```

### Workflow 3: Project-Based Learning

```bash
# ១. ពិនិត្យមើលមេរៀន វដ្ដជីវិតវិទ្យាសាស្ត្រទិន្នន័យ (១៤-១៦)
cd 4-Data-Science-Lifecycle

# ២. ធ្វើការជាមួយឧទាហរណ៍ពិតប្រាកដ (មេរៀន ២០)
cd ../6-Data-Science-In-Wild/20-Real-World-Examples

# ៣. អនុវត្តគំនិតទៅលើគម្រោងផ្ទាល់ខ្លួនរបស់អ្នក
```

### Workflow 4: Cloud-Based Data Science

```bash
# រៀនអំពីវិទ្យាសាស្ត្រទិន្នន័យពពក (មេរៀន ១៧-១៩)
cd 5-Data-Science-In-Cloud

# ១៧: ការណែនាំអំពីវិទ្យាសាស្ត្រទិន្នន័យពពក
# ១៨: ឧបករណ៍ ML កូដទាប
# ១៩: ស្ទូឌីយោ Azure Machine Learning
```

## Tips for Self-Learners

### Stay Organized

```bash
# បង្កើតសៀវភៅកំណត់ហេតុការសិក្សា
mkdir my-learning-journal

# សម្រាប់មេរៀននីមួយៗ បង្កើតកំណត់សម្គាល់
echo "# Lesson 1 Notes" > my-learning-journal/lesson-01-notes.md
```

### Practice Regularly

- Set aside dedicated time each day or week
- Complete at least one lesson per week
- Review previous lessons periodically

### Engage with the Community

- Join the [Discord community](https://aka.ms/ds4beginners/discord)
- Participate in #Data-Science-for-Beginners Channel in Discord [Discord Discussions](https://aka.ms/ds4beginners/discord)
- Share your progress and ask questions

### Build Your Own Projects

After completing lessons, apply concepts to personal projects:

```python
# ឧទាហរណ៍៖ វិភាគទិន្នន័យរបស់អ្នកផ្ទាល់
import pandas as pd

# បញ្ចូលទិន្នន័យរបស់អ្នកផ្ទាល់
my_data = pd.read_csv('my-project/data.csv')

# អនុវត្តបច្ចេកទេសដែលបានរៀន
# - សម្អាតទិន្នន័យ (មេរៀនទី ៨)
# - វិភាគទិន្នន័យស្រាវជ្រាវ (មេរៀនទី ៧)
# - ការបង្ហាញតាមរូបភាព (មេរៀនទី ៩-១៣)
# - ការវិភាគ (មេរៀនទី ១៥)
```

## Tips for Teachers

### Classroom Setup

1. Review [for-teachers.md](for-teachers.md) for detailed guidance
2. Set up a shared environment (GitHub Classroom or Codespaces)
3. Establish a communication channel (Discord, Slack, or Teams)

### Lesson Planning

**Suggested 10-Week Schedule:**

- **Week 1-2**: Introduction (Lessons 1-4)
- **Week 3-4**: Working with Data (Lessons 5-8)
- **Week 5-6**: Data Visualization (Lessons 9-13)
- **Week 7-8**: Data Science Lifecycle (Lessons 14-16)
- **Week 9**: Cloud Data Science (Lessons 17-19)
- **Week 10**: Real-World Applications & Final Projects (Lesson 20)

### Running Docsify for Offline Access

```bash
# បម្រើឯកសារពិពណ៌នាទៅក្នុងមូលដ្ឋានសម្រាប់ការប្រើប្រាស់ថ្នាក់រៀន
docsify serve

# សិស្សអាចចូលប្រើបាននៅ localhost:3000
# មិនចាំបាច់មានអ៊ីនធឺណិតបន្ទាន់ក្រោយពេលបង្កើតដំបូង
```

### Assignment Grading

- Review student notebooks for completed exercises
- Check for understanding through quiz scores
- Evaluate final projects using data science lifecycle principles

### Creating Assignments

```python
# គំរូភារកិច្ចផ្ទាល់ខ្លួនឧទាហរណ៍
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

## Working Offline

### Download Resources

```bash
# អំពីចម្លងគ្រប់ផ្នែកទាំងអស់នៃឃ្លាំងទិន្នន័យ
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# ទាញយកសំណុំនៃទិន្នន័យជាមុន
# សំណុំនៃទិន្នន័យភាគច្រើនត្រូវបានបញ្ចូលក្នុងឃ្លាំងទិន្នន័យ
```

### Run Documentation Locally

```bash
# បម្រុងជាមួយ Docsify
docsify serve

# ចូលប្រើនៅ localhost:3000
```

### Run Quiz App Locally

```bash
cd quiz-app
npm run serve
```

## Accessing Translated Content

Translations are available in 40+ languages:

```bash
# ចូលទៅកាន់មេរៀនបានបកប្រែ
cd translations/fr  # ភាសាបារាំង
cd translations/es  # ភាសាអេស្ប៉ាញ
cd translations/de  # ភាសាអាល្លឺម៉ង់
# ... និងច្រើនទៀត
```

Each translation maintains the same structure as the English version.

## Additional Resources

### Continue Learning

- [Microsoft Learn](https://docs.microsoft.com/learn/) - Additional learning paths
- [Student Hub](https://docs.microsoft.com/learn/student-hub) - Resources for students
- [Azure AI Foundry](https://aka.ms/foundry/forum) - Community forum

### Related Curricula

- [AI for Beginners](https://aka.ms/ai-beginners)
- [ML for Beginners](https://aka.ms/ml-beginners)
- [Web Dev for Beginners](https://aka.ms/webdev-beginners)
- [Generative AI for Beginners](https://aka.ms/genai-beginners)

## Getting Help

- Check [TROUBLESHOOTING.md](TROUBLESHOOTING.md) for common issues
- Search [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
- Join our [Discord](https://aka.ms/ds4beginners/discord)
- Review [CONTRIBUTING.md](CONTRIBUTING.md) to report issues or contribute

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការព្រមាន**៖
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាកម្មបកប្រែដោយ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈពេលដែលយើងខិតខំប្រឹងប្រែងសម្រាប់ភាពត្រឹមត្រូវ សូមយល់ឱ្យបានច្បាស់ថា ការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុស ឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមក្នុងភាសាដើមគួรถูกគេពិចារណាថាជាផ្លូវការនៃព័ត៌មាន។ សម្រាប់ព័ត៌មានសំខាន់ៗ ការបកប្រែដោយអ្នកជំនាញផ្ទាល់ខ្លួនត្រូវបានណែនាំ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសនៃព័ត៌មានដែលបណ្តាលមកពីការប្រើប្រាស់ការបកប្រែនេះឡើយ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->