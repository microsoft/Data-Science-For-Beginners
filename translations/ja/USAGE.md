<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f546349678757508d69ce9e1d2688446",
  "translation_date": "2025-10-03T14:57:14+00:00",
  "source_file": "USAGE.md",
  "language_code": "ja"
}
-->
# 使用ガイド

このガイドでは、「初心者のためのデータサイエンス」カリキュラムの使用例と一般的なワークフローを紹介します。

## 目次

- [このカリキュラムの使い方](../..)
- [レッスンの進め方](../..)
- [Jupyter Notebookの使い方](../..)
- [クイズアプリケーションの使用](../..)
- [一般的なワークフロー](../..)
- [自己学習者へのヒント](../..)
- [教師へのヒント](../..)

## このカリキュラムの使い方

このカリキュラムは柔軟に設計されており、以下の方法で利用できます：

- **自己ペース学習**: 自分のペースで独立してレッスンを進める
- **教室での指導**: 指導付きの構造化されたコースとして使用する
- **勉強会**: 仲間と協力して学ぶ
- **ワークショップ形式**: 集中的な短期学習セッション

## レッスンの進め方

各レッスンは学習効果を最大化するために一貫した構造を持っています：

### レッスン構造

1. **事前クイズ**: 既存の知識をテスト
2. **スケッチノート** (オプション): 主要な概念の視覚的な要約
3. **ビデオ** (オプション): 補足的なビデオコンテンツ
4. **書面によるレッスン**: 核心的な概念と説明
5. **Jupyter Notebook**: 実践的なコーディング演習
6. **課題**: 学んだ内容を練習
7. **事後クイズ**: 理解を強化

### レッスンの例ワークフロー

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

## Jupyter Notebookの使い方

### Jupyterの起動

```bash
# Activate your virtual environment
source venv/bin/activate  # On macOS/Linux
# OR
venv\Scripts\activate  # On Windows

# Start Jupyter from the repository root
jupyter notebook
```

### Notebookセルの実行

1. **セルを実行**: `Shift + Enter`を押すか「Run」ボタンをクリック
2. **すべてのセルを実行**: メニューから「Cell」→「Run All」を選択
3. **カーネルの再起動**: 問題が発生した場合は「Kernel」→「Restart」を選択

### 例: Notebookでデータを操作する

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

### 作業内容の保存

- Jupyterは定期的に自動保存します
- 手動保存: `Ctrl + S` (macOSでは`Cmd + S`)を押す
- 進捗は`.ipynb`ファイルに保存されます

## クイズアプリケーションの使用

### クイズアプリをローカルで実行する

```bash
# Navigate to quiz app directory
cd quiz-app

# Start the development server
npm run serve

# Access at http://localhost:8080
```

### クイズの受験

1. レッスンの冒頭に事前クイズへのリンクがあります
2. レッスンの最後に事後クイズへのリンクがあります
3. 各クイズには3つの質問があります
4. クイズは学習を強化するために設計されており、徹底的にテストするものではありません

### クイズの番号付け

- クイズは0～39の番号が付けられています（合計40問）
- 各レッスンには通常、事前クイズと事後クイズがあります
- クイズのURLにはクイズ番号が含まれています: `https://ff-quizzes.netlify.app/en/ds/quiz/0`

## 一般的なワークフロー

### ワークフロー1: 完全初心者向けの道筋

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

### ワークフロー2: 特定のトピックに特化した学習

特定のトピックに興味がある場合：

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

### ワークフロー3: プロジェクトベースの学習

```bash
# 1. Review the Data Science Lifecycle lessons (14-16)
cd 4-Data-Science-Lifecycle

# 2. Work through a real-world example (Lesson 20)
cd ../6-Data-Science-In-Wild/20-Real-World-Examples

# 3. Apply concepts to your own project
```

### ワークフロー4: クラウドベースのデータサイエンス

```bash
# Learn about cloud data science (Lessons 17-19)
cd 5-Data-Science-In-Cloud

# 17: Introduction to Cloud Data Science
# 18: Low-Code ML Tools
# 19: Azure Machine Learning Studio
```

## 自己学習者へのヒント

### 整理整頓を心がける

```bash
# Create a learning journal
mkdir my-learning-journal

# For each lesson, create notes
echo "# Lesson 1 Notes" > my-learning-journal/lesson-01-notes.md
```

### 定期的に練習する

- 毎日または毎週、専用の時間を確保する
- 週に最低1つのレッスンを完了する
- 過去のレッスンを定期的に復習する

### コミュニティに参加する

- [Discordコミュニティ](https://aka.ms/ds4beginners/discord)に参加する
- Discordの#Data-Science-for-Beginnersチャンネルで議論に参加する [Discord Discussions](https://aka.ms/ds4beginners/discord)
- 進捗を共有し、質問をする

### 自分のプロジェクトを作成する

レッスンを完了した後、学んだ概念を個人プロジェクトに応用する：

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

## 教師へのヒント

### 教室の準備

1. 詳細なガイダンスについては[for-teachers.md](for-teachers.md)を確認
2. 共有環境を設定する（GitHub ClassroomやCodespacesなど）
3. コミュニケーションチャネルを確立する（Discord、Slack、またはTeams）

### レッスンプランニング

**推奨10週間スケジュール:**

- **第1～2週**: 導入（レッスン1～4）
- **第3～4週**: データの操作（レッスン5～8）
- **第5～6週**: データの可視化（レッスン9～13）
- **第7～8週**: データサイエンスライフサイクル（レッスン14～16）
- **第9週**: クラウドデータサイエンス（レッスン17～19）
- **第10週**: 実世界の応用と最終プロジェクト（レッスン20）

### Docsifyを使ったオフラインアクセス

```bash
# Serve documentation locally for classroom use
docsify serve

# Students can access at localhost:3000
# No internet required after initial setup
```

### 課題の採点

- 学生のNotebookを確認して演習が完了しているか確認
- クイズのスコアを通じて理解度をチェック
- データサイエンスライフサイクルの原則を使用して最終プロジェクトを評価

### 課題の作成

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

## オフラインでの作業

### リソースのダウンロード

```bash
# Clone the entire repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Download datasets in advance
# Most datasets are included in the repository
```

### ドキュメントをローカルで実行する

```bash
# Serve with Docsify
docsify serve

# Access at localhost:3000
```

### クイズアプリをローカルで実行する

```bash
cd quiz-app
npm run serve
```

## 翻訳されたコンテンツへのアクセス

翻訳は40以上の言語で利用可能です：

```bash
# Access translated lessons
cd translations/fr  # French
cd translations/es  # Spanish
cd translations/de  # German
# ... and many more
```

各翻訳は英語版と同じ構造を維持しています。

## 追加リソース

### 学習を続ける

- [Microsoft Learn](https://docs.microsoft.com/learn/) - 追加の学習パス
- [Student Hub](https://docs.microsoft.com/learn/student-hub) - 学生向けリソース
- [Azure AI Foundry](https://aka.ms/foundry/forum) - コミュニティフォーラム

### 関連カリキュラム

- [AI for Beginners](https://aka.ms/ai-beginners)
- [ML for Beginners](https://aka.ms/ml-beginners)
- [Web Dev for Beginners](https://aka.ms/webdev-beginners)
- [Generative AI for Beginners](https://aka.ms/genai-beginners)

## ヘルプを得る

- 一般的な問題については[TROUBLESHOOTING.md](TROUBLESHOOTING.md)を確認
- [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)を検索
- [Discord](https://aka.ms/ds4beginners/discord)に参加
- 問題の報告や貢献については[CONTRIBUTING.md](CONTRIBUTING.md)を確認

---

**免責事項**:  
この文書は、AI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。元の言語で記載された文書を正式な情報源としてお考えください。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解釈について、当方は一切の責任を負いません。