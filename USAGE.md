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

1. **Execute a cell**: Press `Shift + Enter` or click the "Run" button
2. **Execute all cells**: Select "Cell" → "Run All" from the menu
3. **Restart kernel**: Select "Kernel" → "Restart" if you encounter issues

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

- Jupyter auto-saves periodically
- Manually save: Press `Ctrl + S` (or `Cmd + S` on macOS)
- Your progress is saved in the `.ipynb` file

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

If you're interested in a specific topic:

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
# Serve documentation locally for classroom use
docsify serve

# Students can access at localhost:3000
# No internet required after initial setup
```

### Assignment Grading

- Review student notebooks for completed exercises
- Check for understanding through quiz scores
- Evaluate final projects using data science lifecycle principles

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

Translations are available in 40+ languages:

```bash
# Access translated lessons
cd translations/fr  # French
cd translations/es  # Spanish
cd translations/de  # German
# ... and many more
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
