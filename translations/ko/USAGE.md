<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f546349678757508d69ce9e1d2688446",
  "translation_date": "2025-10-03T14:57:29+00:00",
  "source_file": "USAGE.md",
  "language_code": "ko"
}
-->
# 사용 가이드

이 가이드는 초보자를 위한 데이터 과학 커리큘럼을 사용하는 예제와 일반적인 워크플로를 제공합니다.

## 목차

- [이 커리큘럼을 사용하는 방법](../..)
- [레슨 활용하기](../..)
- [주피터 노트북 활용하기](../..)
- [퀴즈 애플리케이션 사용하기](../..)
- [일반적인 워크플로](../..)
- [자기주도 학습자를 위한 팁](../..)
- [교사를 위한 팁](../..)

## 이 커리큘럼을 사용하는 방법

이 커리큘럼은 유연하게 설계되어 다양한 방식으로 사용할 수 있습니다:

- **자기주도 학습**: 자신의 속도에 맞춰 독립적으로 레슨을 진행
- **교실 수업**: 구조화된 강의와 함께 사용하는 코스
- **스터디 그룹**: 동료들과 협력하여 학습
- **워크숍 형식**: 집중적인 단기 학습 세션

## 레슨 활용하기

각 레슨은 학습 효과를 극대화하기 위해 일관된 구조를 따릅니다:

### 레슨 구조

1. **사전 퀴즈**: 기존 지식을 테스트
2. **스케치노트** (선택 사항): 주요 개념의 시각적 요약
3. **비디오** (선택 사항): 보충 비디오 콘텐츠
4. **작성된 레슨**: 핵심 개념과 설명
5. **주피터 노트북**: 실습 코딩 연습
6. **과제**: 배운 내용을 연습
7. **사후 퀴즈**: 이해도를 강화

### 레슨 예제 워크플로

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

## 주피터 노트북 활용하기

### 주피터 시작하기

```bash
# Activate your virtual environment
source venv/bin/activate  # On macOS/Linux
# OR
venv\Scripts\activate  # On Windows

# Start Jupyter from the repository root
jupyter notebook
```

### 노트북 셀 실행하기

1. **셀 실행**: `Shift + Enter`를 누르거나 "실행" 버튼 클릭
2. **모든 셀 실행**: 메뉴에서 "Cell" → "Run All" 선택
3. **커널 재시작**: 문제가 발생하면 "Kernel" → "Restart" 선택

### 예제: 노트북에서 데이터 작업하기

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

### 작업 저장하기

- 주피터는 주기적으로 자동 저장됩니다
- 수동 저장: `Ctrl + S` (macOS에서는 `Cmd + S`) 누르기
- 진행 상황은 `.ipynb` 파일에 저장됩니다

## 퀴즈 애플리케이션 사용하기

### 로컬에서 퀴즈 앱 실행하기

```bash
# Navigate to quiz app directory
cd quiz-app

# Start the development server
npm run serve

# Access at http://localhost:8080
```

### 퀴즈 풀기

1. 사전 퀴즈는 각 레슨 상단에 링크로 제공됩니다
2. 사후 퀴즈는 각 레슨 하단에 링크로 제공됩니다
3. 각 퀴즈는 3개의 질문으로 구성됩니다
4. 퀴즈는 학습을 강화하기 위한 것이며, 철저한 테스트를 위한 것은 아닙니다

### 퀴즈 번호 체계

- 퀴즈는 0-39번으로 번호가 매겨져 있습니다 (총 40개 퀴즈)
- 각 레슨에는 일반적으로 사전 및 사후 퀴즈가 포함됩니다
- 퀴즈 URL에는 퀴즈 번호가 포함됩니다: `https://ff-quizzes.netlify.app/en/ds/quiz/0`

## 일반적인 워크플로

### 워크플로 1: 완전 초보자 경로

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

### 워크플로 2: 특정 주제 학습

특정 주제에 관심이 있다면:

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

### 워크플로 3: 프로젝트 기반 학습

```bash
# 1. Review the Data Science Lifecycle lessons (14-16)
cd 4-Data-Science-Lifecycle

# 2. Work through a real-world example (Lesson 20)
cd ../6-Data-Science-In-Wild/20-Real-World-Examples

# 3. Apply concepts to your own project
```

### 워크플로 4: 클라우드 기반 데이터 과학

```bash
# Learn about cloud data science (Lessons 17-19)
cd 5-Data-Science-In-Cloud

# 17: Introduction to Cloud Data Science
# 18: Low-Code ML Tools
# 19: Azure Machine Learning Studio
```

## 자기주도 학습자를 위한 팁

### 체계적으로 학습하기

```bash
# Create a learning journal
mkdir my-learning-journal

# For each lesson, create notes
echo "# Lesson 1 Notes" > my-learning-journal/lesson-01-notes.md
```

### 규칙적으로 연습하기

- 매일 또는 매주 전용 시간을 확보하세요
- 최소한 주당 한 개의 레슨을 완료하세요
- 이전 레슨을 주기적으로 복습하세요

### 커뮤니티와 소통하기

- [Discord 커뮤니티](https://aka.ms/ds4beginners/discord)에 참여하세요
- Discord의 #Data-Science-for-Beginners 채널에서 토론에 참여하세요 [Discord Discussions](https://aka.ms/ds4beginners/discord)
- 진행 상황을 공유하고 질문하세요

### 자신만의 프로젝트 만들기

레슨을 완료한 후, 개인 프로젝트에 개념을 적용하세요:

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

## 교사를 위한 팁

### 교실 환경 설정

1. [for-teachers.md](for-teachers.md)를 검토하여 자세한 지침 확인
2. 공유 환경 설정 (GitHub Classroom 또는 Codespaces)
3. 커뮤니케이션 채널 설정 (Discord, Slack, 또는 Teams)

### 레슨 계획

**10주 추천 일정:**

- **1-2주차**: 소개 (레슨 1-4)
- **3-4주차**: 데이터 작업 (레슨 5-8)
- **5-6주차**: 데이터 시각화 (레슨 9-13)
- **7-8주차**: 데이터 과학 라이프사이클 (레슨 14-16)
- **9주차**: 클라우드 데이터 과학 (레슨 17-19)
- **10주차**: 실제 응용 및 최종 프로젝트 (레슨 20)

### 오프라인 액세스를 위한 Docsify 실행

```bash
# Serve documentation locally for classroom use
docsify serve

# Students can access at localhost:3000
# No internet required after initial setup
```

### 과제 채점

- 학생 노트북을 검토하여 완료된 연습 확인
- 퀴즈 점수를 통해 이해도 확인
- 데이터 과학 라이프사이클 원칙을 사용하여 최종 프로젝트 평가

### 과제 만들기

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

## 오프라인 작업

### 리소스 다운로드

```bash
# Clone the entire repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Download datasets in advance
# Most datasets are included in the repository
```

### 로컬에서 문서 실행

```bash
# Serve with Docsify
docsify serve

# Access at localhost:3000
```

### 로컬에서 퀴즈 앱 실행

```bash
cd quiz-app
npm run serve
```

## 번역된 콘텐츠 액세스

번역은 40개 이상의 언어로 제공됩니다:

```bash
# Access translated lessons
cd translations/fr  # French
cd translations/es  # Spanish
cd translations/de  # German
# ... and many more
```

각 번역은 영어 버전과 동일한 구조를 유지합니다.

## 추가 리소스

### 학습 계속하기

- [Microsoft Learn](https://docs.microsoft.com/learn/) - 추가 학습 경로
- [Student Hub](https://docs.microsoft.com/learn/student-hub) - 학생을 위한 리소스
- [Azure AI Foundry](https://aka.ms/foundry/forum) - 커뮤니티 포럼

### 관련 커리큘럼

- [AI for Beginners](https://aka.ms/ai-beginners)
- [ML for Beginners](https://aka.ms/ml-beginners)
- [Web Dev for Beginners](https://aka.ms/webdev-beginners)
- [Generative AI for Beginners](https://aka.ms/genai-beginners)

## 도움 받기

- [TROUBLESHOOTING.md](TROUBLESHOOTING.md)에서 일반적인 문제 확인
- [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues) 검색
- [Discord](https://aka.ms/ds4beginners/discord)에 참여
- [CONTRIBUTING.md](CONTRIBUTING.md)를 검토하여 문제를 보고하거나 기여하세요

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전을 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.