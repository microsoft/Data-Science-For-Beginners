<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f546349678757508d69ce9e1d2688446",
  "translation_date": "2025-10-03T14:54:44+00:00",
  "source_file": "USAGE.md",
  "language_code": "zh"
}
-->
# 使用指南

本指南提供了使用《数据科学入门》课程的示例和常见工作流程。

## 目录

- [如何使用本课程](../..)
- [学习课程内容](../..)
- [使用 Jupyter Notebooks](../..)
- [使用测验应用程序](../..)
- [常见工作流程](../..)
- [自学者提示](../..)
- [教师提示](../..)

## 如何使用本课程

本课程设计灵活，可通过多种方式使用：

- **自学**：根据自己的节奏独立完成课程
- **课堂教学**：作为结构化课程进行指导教学
- **学习小组**：与同伴协作学习
- **工作坊形式**：短期强化学习

## 学习课程内容

每节课遵循一致的结构，以最大化学习效果：

### 课程结构

1. **课前测验**：测试现有知识
2. **手绘笔记**（可选）：关键概念的视觉总结
3. **视频**（可选）：补充视频内容
4. **书面课程**：核心概念和解释
5. **Jupyter Notebook**：动手编码练习
6. **作业**：练习所学内容
7. **课后测验**：巩固理解

### 课程学习示例流程

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

## 使用 Jupyter Notebooks

### 启动 Jupyter

```bash
# Activate your virtual environment
source venv/bin/activate  # On macOS/Linux
# OR
venv\Scripts\activate  # On Windows

# Start Jupyter from the repository root
jupyter notebook
```

### 运行 Notebook 单元格

1. **执行单元格**：按 `Shift + Enter` 或点击“运行”按钮
2. **运行所有单元格**：从菜单中选择“Cell” → “Run All”
3. **重启内核**：如果遇到问题，选择“Kernel” → “Restart”

### 示例：在 Notebook 中处理数据

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

### 保存您的工作

- Jupyter 会定期自动保存
- 手动保存：按 `Ctrl + S`（macOS 上为 `Cmd + S`）
- 您的进度保存在 `.ipynb` 文件中

## 使用测验应用程序

### 本地运行测验应用程序

```bash
# Navigate to quiz app directory
cd quiz-app

# Start the development server
npm run serve

# Access at http://localhost:8080
```

### 参加测验

1. 课前测验链接位于每节课顶部
2. 课后测验链接位于每节课底部
3. 每个测验包含 3 个问题
4. 测验旨在巩固学习，而非全面测试

### 测验编号

- 测验编号为 0-39（共 40 个测验）
- 每节课通常有课前和课后测验
- 测验 URL 包含测验编号：`https://ff-quizzes.netlify.app/en/ds/quiz/0`

## 常见工作流程

### 工作流程 1：完全初学者路径

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

### 工作流程 2：特定主题学习

如果您对某个特定主题感兴趣：

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

### 工作流程 3：基于项目的学习

```bash
# 1. Review the Data Science Lifecycle lessons (14-16)
cd 4-Data-Science-Lifecycle

# 2. Work through a real-world example (Lesson 20)
cd ../6-Data-Science-In-Wild/20-Real-World-Examples

# 3. Apply concepts to your own project
```

### 工作流程 4：基于云的数据科学

```bash
# Learn about cloud data science (Lessons 17-19)
cd 5-Data-Science-In-Cloud

# 17: Introduction to Cloud Data Science
# 18: Low-Code ML Tools
# 19: Azure Machine Learning Studio
```

## 自学者提示

### 保持条理

```bash
# Create a learning journal
mkdir my-learning-journal

# For each lesson, create notes
echo "# Lesson 1 Notes" > my-learning-journal/lesson-01-notes.md
```

### 定期练习

- 每天或每周安排固定时间学习
- 每周至少完成一节课
- 定期复习之前的课程

### 参与社区

- 加入 [Discord 社区](https://aka.ms/ds4beginners/discord)
- 参与 Discord 中的 #Data-Science-for-Beginners 频道 [Discord Discussions](https://aka.ms/ds4beginners/discord)
- 分享您的学习进度并提出问题

### 创建自己的项目

完成课程后，将概念应用到个人项目中：

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

## 教师提示

### 课堂设置

1. 查看 [for-teachers.md](for-teachers.md) 获取详细指导
2. 设置共享环境（GitHub Classroom 或 Codespaces）
3. 建立沟通渠道（Discord、Slack 或 Teams）

### 课程计划

**建议的 10 周课程安排：**

- **第 1-2 周**：介绍（第 1-4 课）
- **第 3-4 周**：数据处理（第 5-8 课）
- **第 5-6 周**：数据可视化（第 9-13 课）
- **第 7-8 周**：数据科学生命周期（第 14-16 课）
- **第 9 周**：云数据科学（第 17-19 课）
- **第 10 周**：实际应用与最终项目（第 20 课）

### 运行 Docsify 以离线访问

```bash
# Serve documentation locally for classroom use
docsify serve

# Students can access at localhost:3000
# No internet required after initial setup
```

### 作业评分

- 检查学生的 Notebook 是否完成练习
- 通过测验分数检查理解情况
- 使用数据科学生命周期原则评估最终项目

### 创建作业

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

## 离线使用

### 下载资源

```bash
# Clone the entire repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Download datasets in advance
# Most datasets are included in the repository
```

### 本地运行文档

```bash
# Serve with Docsify
docsify serve

# Access at localhost:3000
```

### 本地运行测验应用程序

```bash
cd quiz-app
npm run serve
```

## 访问翻译内容

翻译版本支持 40 多种语言：

```bash
# Access translated lessons
cd translations/fr  # French
cd translations/es  # Spanish
cd translations/de  # German
# ... and many more
```

每种翻译版本的结构与英文版保持一致。

## 其他资源

### 继续学习

- [Microsoft Learn](https://docs.microsoft.com/learn/) - 更多学习路径
- [Student Hub](https://docs.microsoft.com/learn/student-hub) - 学生资源
- [Azure AI Foundry](https://aka.ms/foundry/forum) - 社区论坛

### 相关课程

- [AI 入门](https://aka.ms/ai-beginners)
- [ML 入门](https://aka.ms/ml-beginners)
- [Web 开发入门](https://aka.ms/webdev-beginners)
- [生成式 AI 入门](https://aka.ms/genai-beginners)

## 获取帮助

- 查看 [TROUBLESHOOTING.md](TROUBLESHOOTING.md) 了解常见问题
- 搜索 [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
- 加入我们的 [Discord](https://aka.ms/ds4beginners/discord)
- 查看 [CONTRIBUTING.md](CONTRIBUTING.md) 以报告问题或贡献内容

---

**免责声明**：  
本文档使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于关键信息，建议使用专业人工翻译。我们不对因使用此翻译而产生的任何误解或误读承担责任。