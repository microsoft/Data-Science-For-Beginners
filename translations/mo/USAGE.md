<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f546349678757508d69ce9e1d2688446",
  "translation_date": "2025-10-03T14:55:02+00:00",
  "source_file": "USAGE.md",
  "language_code": "mo"
}
-->
# 使用指南

本指南提供了使用「初學者的數據科學」課程的範例和常見工作流程。

## 目錄

- [如何使用此課程](../..)
- [使用課程](../..)
- [使用 Jupyter Notebook](../..)
- [使用測驗應用程式](../..)
- [常見工作流程](../..)
- [自學者的提示](../..)
- [教師的提示](../..)

## 如何使用此課程

此課程設計靈活，可用於多種方式：

- **自學**：按照自己的速度獨立完成課程
- **課堂教學**：作為結構化課程進行指導教學
- **學習小組**：與同伴合作學習
- **工作坊形式**：密集的短期學習課程

## 使用課程

每節課遵循一致的結構以最大化學習效果：

### 課程結構

1. **課前測驗**：測試現有知識
2. **手繪筆記**（可選）：關鍵概念的視覺摘要
3. **影片**（可選）：補充的影片內容
4. **書面課程**：核心概念和解釋
5. **Jupyter Notebook**：動手編碼練習
6. **作業**：練習所學內容
7. **課後測驗**：加強理解

### 課程範例工作流程

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

## 使用 Jupyter Notebook

### 啟動 Jupyter

```bash
# Activate your virtual environment
source venv/bin/activate  # On macOS/Linux
# OR
venv\Scripts\activate  # On Windows

# Start Jupyter from the repository root
jupyter notebook
```

### 執行 Notebook 的單元格

1. **執行單元格**：按 `Shift + Enter` 或點擊「執行」按鈕
2. **執行所有單元格**：選擇「Cell」→「Run All」選項
3. **重啟核心**：如果遇到問題，選擇「Kernel」→「Restart」

### 範例：在 Notebook 中處理數據

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

- Jupyter 會定期自動保存
- 手動保存：按 `Ctrl + S`（macOS 上為 `Cmd + S`）
- 您的進度會保存到 `.ipynb` 文件中

## 使用測驗應用程式

### 本地運行測驗應用程式

```bash
# Navigate to quiz app directory
cd quiz-app

# Start the development server
npm run serve

# Access at http://localhost:8080
```

### 進行測驗

1. 課前測驗位於每節課的頂部
2. 課後測驗位於每節課的底部
3. 每個測驗包含 3 個問題
4. 測驗旨在加強學習，而非全面測試

### 測驗編號

- 測驗編號為 0-39（共 40 個測驗）
- 每節課通常有課前和課後測驗
- 測驗 URL 包含測驗編號：`https://ff-quizzes.netlify.app/en/ds/quiz/0`

## 常見工作流程

### 工作流程 1：完全初學者路徑

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

### 工作流程 2：特定主題學習

如果您對某個特定主題感興趣：

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

### 工作流程 3：基於項目的學習

```bash
# 1. Review the Data Science Lifecycle lessons (14-16)
cd 4-Data-Science-Lifecycle

# 2. Work through a real-world example (Lesson 20)
cd ../6-Data-Science-In-Wild/20-Real-World-Examples

# 3. Apply concepts to your own project
```

### 工作流程 4：基於雲端的數據科學

```bash
# Learn about cloud data science (Lessons 17-19)
cd 5-Data-Science-In-Cloud

# 17: Introduction to Cloud Data Science
# 18: Low-Code ML Tools
# 19: Azure Machine Learning Studio
```

## 自學者的提示

### 保持有條理

```bash
# Create a learning journal
mkdir my-learning-journal

# For each lesson, create notes
echo "# Lesson 1 Notes" > my-learning-journal/lesson-01-notes.md
```

### 定期練習

- 每天或每週安排固定的學習時間
- 每週至少完成一節課
- 定期回顧之前的課程

### 與社群互動

- 加入 [Discord 社群](https://aka.ms/ds4beginners/discord)
- 參與 Discord 的 #Data-Science-for-Beginners 頻道 [Discord 討論](https://aka.ms/ds4beginners/discord)
- 分享您的進度並提出問題

### 建立自己的項目

完成課程後，將概念應用於個人項目：

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

## 教師的提示

### 課堂設置

1. 查看 [for-teachers.md](for-teachers.md) 以獲取詳細指導
2. 設置共享環境（GitHub Classroom 或 Codespaces）
3. 建立溝通渠道（Discord、Slack 或 Teams）

### 課程規劃

**建議的 10 週計劃：**

- **第 1-2 週**：介紹（課程 1-4）
- **第 3-4 週**：數據處理（課程 5-8）
- **第 5-6 週**：數據可視化（課程 9-13）
- **第 7-8 週**：數據科學生命周期（課程 14-16）
- **第 9 週**：雲端數據科學（課程 17-19）
- **第 10 週**：實際應用與最終項目（課程 20）

### 運行 Docsify 以離線訪問

```bash
# Serve documentation locally for classroom use
docsify serve

# Students can access at localhost:3000
# No internet required after initial setup
```

### 作業評分

- 查看學生 Notebook 中完成的練習
- 通過測驗分數檢查理解程度
- 使用數據科學生命周期原則評估最終項目

### 創建作業

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

## 離線使用

### 下載資源

```bash
# Clone the entire repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Download datasets in advance
# Most datasets are included in the repository
```

### 本地運行文檔

```bash
# Serve with Docsify
docsify serve

# Access at localhost:3000
```

### 本地運行測驗應用程式

```bash
cd quiz-app
npm run serve
```

## 訪問翻譯內容

翻譯版本提供超過 40 種語言：

```bash
# Access translated lessons
cd translations/fr  # French
cd translations/es  # Spanish
cd translations/de  # German
# ... and many more
```

每個翻譯版本的結構與英文版保持一致。

## 其他資源

### 繼續學習

- [Microsoft Learn](https://docs.microsoft.com/learn/) - 額外的學習路徑
- [Student Hub](https://docs.microsoft.com/learn/student-hub) - 學生資源
- [Azure AI Foundry](https://aka.ms/foundry/forum) - 社群論壇

### 相關課程

- [AI for Beginners](https://aka.ms/ai-beginners)
- [ML for Beginners](https://aka.ms/ml-beginners)
- [Web Dev for Beginners](https://aka.ms/webdev-beginners)
- [Generative AI for Beginners](https://aka.ms/genai-beginners)

## 獲取幫助

- 查看 [TROUBLESHOOTING.md](TROUBLESHOOTING.md) 以解決常見問題
- 搜索 [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
- 加入我們的 [Discord](https://aka.ms/ds4beginners/discord)
- 查看 [CONTRIBUTING.md](CONTRIBUTING.md) 以報告問題或貢獻內容

---

**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們努力確保翻譯的準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於關鍵信息，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤釋不承擔責任。