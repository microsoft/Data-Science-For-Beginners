<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f546349678757508d69ce9e1d2688446",
  "translation_date": "2025-11-18T18:13:54+00:00",
  "source_file": "USAGE.md",
  "language_code": "pcm"
}
-->
# Usage Guide

Dis guide dey show example and common way wey you fit take use di Data Science for Beginners curriculum.

## Table of Contents

- [How to Use This Curriculum](../..)
- [Working with Lessons](../..)
- [Working with Jupyter Notebooks](../..)
- [Using the Quiz Application](../..)
- [Common Workflows](../..)
- [Tips for Self-Learners](../..)
- [Tips for Teachers](../..)

## How to Use This Curriculum

Dis curriculum dey flexible, you fit use am in different ways:

- **Self-paced learning**: Work through di lessons by yourself for your own time
- **Classroom instruction**: Use am as structured course wey get teacher guidance
- **Study groups**: Learn together with your friends
- **Workshop format**: Short-term intensive learning session

## Working with Lessons

Each lesson get di same structure to help you learn well:

### Lesson Structure

1. **Pre-lesson Quiz**: Test wetin you sabi already
2. **Sketchnote** (Optional): Visual summary of di main ideas
3. **Video** (Optional): Extra video content
4. **Written Lesson**: Main concepts and explanation
5. **Jupyter Notebook**: Hands-on coding exercise
6. **Assignment**: Practice wetin you don learn
7. **Post-lesson Quiz**: Make sure you understand di lesson

### Example Workflow for a Lesson

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

## Working with Jupyter Notebooks

### Starting Jupyter

```bash
# Activate your virtual environment
source venv/bin/activate  # On macOS/Linux
# OR
venv\Scripts\activate  # On Windows

# Start Jupyter from the repository root
jupyter notebook
```

### Running Notebook Cells

1. **Run one cell**: Press `Shift + Enter` or click di "Run" button
2. **Run all cells**: Go "Cell" → "Run All" for di menu
3. **Restart kernel**: Go "Kernel" → "Restart" if problem dey

### Example: Working with Data in a Notebook

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

### Saving Your Work

- Jupyter dey auto-save from time to time
- Save manually: Press `Ctrl + S` (or `Cmd + S` for macOS)
- Your work go dey save inside `.ipynb` file

## Using the Quiz Application

### Running the Quiz App Locally

```bash
# Navigate to quiz app directory
cd quiz-app

# Start the development server
npm run serve

# Access at http://localhost:8080
```

### Taking Quizzes

1. Pre-lesson quizzes dey for di top of each lesson
2. Post-lesson quizzes dey for di bottom of each lesson
3. Each quiz get 3 questions
4. Quizzes dey to help you learn, no be to test you too much

### Quiz Numbering

- Quizzes dey numbered 0-39 (40 quizzes total)
- Each lesson dey usually get pre and post quiz
- Quiz URLs dey include di quiz number: `https://ff-quizzes.netlify.app/en/ds/quiz/0`

## Common Workflows

### Workflow 1: Complete Beginner Path

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

### Workflow 2: Topic-Specific Learning

If you wan focus on one topic:

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

### Workflow 3: Project-Based Learning

```bash
# 1. Review the Data Science Lifecycle lessons (14-16)
cd 4-Data-Science-Lifecycle

# 2. Work through a real-world example (Lesson 20)
cd ../6-Data-Science-In-Wild/20-Real-World-Examples

# 3. Apply concepts to your own project
```

### Workflow 4: Cloud-Based Data Science

```bash
# Learn about cloud data science (Lessons 17-19)
cd 5-Data-Science-In-Cloud

# 17: Introduction to Cloud Data Science
# 18: Low-Code ML Tools
# 19: Azure Machine Learning Studio
```

## Tips for Self-Learners

### Stay Organized

```bash
# Create a learning journal
mkdir my-learning-journal

# For each lesson, create notes
echo "# Lesson 1 Notes" > my-learning-journal/lesson-01-notes.md
```

### Practice Regularly

- Make time every day or week to learn
- Try finish at least one lesson every week
- Go back to review di lessons wey you don do before

### Engage with the Community

- Join di [Discord community](https://aka.ms/ds4beginners/discord)
- Participate for #Data-Science-for-Beginners Channel for Discord [Discord Discussions](https://aka.ms/ds4beginners/discord)
- Share wetin you don learn and ask questions

### Build Your Own Projects

After you don finish di lessons, use wetin you don learn for your own projects:

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

## Tips for Teachers

### Classroom Setup

1. Check [for-teachers.md](for-teachers.md) for detailed guide
2. Set up shared environment (GitHub Classroom or Codespaces)
3. Create communication channel (Discord, Slack, or Teams)

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
# Serve documentation locally for classroom use
docsify serve

# Students can access at localhost:3000
# No internet required after initial setup
```

### Assignment Grading

- Check student notebooks to see di exercises wey dem don complete
- Use quiz scores to check understanding
- Grade final projects based on data science lifecycle principles

### Creating Assignments

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

## Working Offline

### Download Resources

```bash
# Clone the entire repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Download datasets in advance
# Most datasets are included in the repository
```

### Run Documentation Locally

```bash
# Serve with Docsify
docsify serve

# Access at localhost:3000
```

### Run Quiz App Locally

```bash
cd quiz-app
npm run serve
```

## Accessing Translated Content

Translations dey available for more than 40 languages:

```bash
# Access translated lessons
cd translations/fr  # French
cd translations/es  # Spanish
cd translations/de  # German
# ... and many more
```

Each translation dey follow di same structure as di English version.

## Additional Resources

### Continue Learning

- [Microsoft Learn](https://docs.microsoft.com/learn/) - More learning paths
- [Student Hub](https://docs.microsoft.com/learn/student-hub) - Resources for students
- [Azure AI Foundry](https://aka.ms/foundry/forum) - Community forum

### Related Curricula

- [AI for Beginners](https://aka.ms/ai-beginners)
- [ML for Beginners](https://aka.ms/ml-beginners)
- [Web Dev for Beginners](https://aka.ms/webdev-beginners)
- [Generative AI for Beginners](https://aka.ms/genai-beginners)

## Getting Help

- Check [TROUBLESHOOTING.md](TROUBLESHOOTING.md) for common problems
- Search [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
- Join our [Discord](https://aka.ms/ds4beginners/discord)
- Check [CONTRIBUTING.md](CONTRIBUTING.md) to report problems or contribute

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis docu don dey translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even though we dey try make am accurate, abeg sabi say automated translations fit get mistake or no correct well. Di original docu for im native language na di main correct source. For important information, e good make una use professional human translation. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->