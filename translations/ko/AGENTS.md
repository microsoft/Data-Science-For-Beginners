<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cc2e18ab65df63e75d3619c4752e9b22",
  "translation_date": "2025-10-03T11:10:09+00:00",
  "source_file": "AGENTS.md",
  "language_code": "ko"
}
-->
# AGENTS.md

## 프로젝트 개요

Data Science for Beginners는 Microsoft Azure Cloud Advocates가 제작한 10주, 20강의 종합 커리큘럼입니다. 이 저장소는 Jupyter 노트북, 인터랙티브 퀴즈, 실습 과제를 포함한 프로젝트 기반 강의를 통해 데이터 과학의 기초 개념을 가르치는 학습 자료입니다.

**주요 기술:**
- **Jupyter 노트북**: Python 3을 사용한 주요 학습 매체
- **Python 라이브러리**: pandas, numpy, matplotlib을 활용한 데이터 분석 및 시각화
- **Vue.js 2**: 퀴즈 애플리케이션 (quiz-app 폴더)
- **Docsify**: 오프라인 접근을 위한 문서 사이트 생성기
- **Node.js/npm**: JavaScript 구성 요소를 위한 패키지 관리
- **Markdown**: 모든 강의 내용 및 문서화

**아키텍처:**
- 다국어 교육용 저장소로 광범위한 번역 제공
- 강의 모듈로 구성 (1-Introduction부터 6-Data-Science-In-Wild까지)
- 각 강의는 README, 노트북, 과제, 퀴즈를 포함
- 독립 실행형 Vue.js 퀴즈 애플리케이션으로 강의 전후 평가 가능
- GitHub Codespaces 및 VS Code 개발 컨테이너 지원

## 설정 명령어

### 저장소 설정
```bash
# Clone the repository (if not already cloned)
git clone https://github.com/microsoft/Data-Science-For-Beginners.git
cd Data-Science-For-Beginners
```

### Python 환경 설정
```bash
# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install common data science libraries (no requirements.txt exists)
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### 퀴즈 애플리케이션 설정
```bash
# Navigate to quiz app
cd quiz-app

# Install dependencies
npm install

# Start development server
npm run serve

# Build for production
npm run build

# Lint and fix files
npm run lint
```

### Docsify 문서 서버
```bash
# Install Docsify globally
npm install -g docsify-cli

# Serve documentation locally
docsify serve

# Documentation will be available at localhost:3000
```

### 시각화 프로젝트 설정
예: meaningful-visualizations (13강):
```bash
# Navigate to starter or solution folder
cd 3-Data-Visualization/13-meaningful-visualizations/starter

# Install dependencies
npm install

# Start development server
npm run serve

# Build for production
npm run build

# Lint files
npm run lint
```


## 개발 워크플로우

### Jupyter 노트북 작업
1. 저장소 루트에서 Jupyter 시작: `jupyter notebook`
2. 원하는 강의 폴더로 이동
3. `.ipynb` 파일 열어 연습 진행
4. 노트북은 설명과 코드 셀이 포함된 독립형 자료
5. 대부분의 노트북은 pandas, numpy, matplotlib을 사용 - 설치 확인 필요

### 강의 구조
각 강의는 일반적으로 다음을 포함합니다:
- `README.md` - 이론 및 예제를 포함한 주요 강의 내용
- `notebook.ipynb` - 실습 Jupyter 노트북 연습
- `assignment.ipynb` 또는 `assignment.md` - 실습 과제
- `solution/` 폴더 - 솔루션 노트북 및 코드
- `images/` 폴더 - 지원 시각 자료

### 퀴즈 애플리케이션 개발
- Vue.js 2 애플리케이션으로 개발 중 핫 리로드 지원
- 퀴즈는 `quiz-app/src/assets/translations/`에 저장
- 각 언어는 자체 번역 폴더를 가짐 (en, fr, es 등)
- 퀴즈 번호는 0부터 시작하여 총 40개

### 번역 추가
- 번역은 저장소 루트의 `translations/` 폴더에 저장
- 각 언어는 영어 구조를 그대로 따름
- GitHub Actions를 통한 자동 번역 (co-op-translator.yml)

## 테스트 지침

### 퀴즈 애플리케이션 테스트
```bash
cd quiz-app

# Run lint checks
npm run lint

# Test build process
npm run build

# Manual testing: Start dev server and verify quiz functionality
npm run serve
```

### 노트북 테스트
- 노트북에 대한 자동화된 테스트 프레임워크는 없음
- 수동 검증: 모든 셀을 순서대로 실행하여 오류 없는지 확인
- 데이터 파일 접근 가능 여부 및 출력 생성 확인
- 시각화가 올바르게 렌더링되는지 확인

### 문서 테스트
```bash
# Verify Docsify renders correctly
docsify serve

# Check for broken links manually by navigating through content
# Verify all lesson links work in the rendered documentation
```

### 코드 품질 검사
```bash
# Vue.js projects (quiz-app and visualization projects)
cd quiz-app  # or visualization project folder
npm run lint

# Python notebooks - manual verification recommended
# Ensure imports work and cells execute without errors
```


## 코드 스타일 지침

### Python (Jupyter 노트북)
- Python 코드에 대해 PEP 8 스타일 지침 준수
- 분석 중인 데이터를 설명하는 명확한 변수명 사용
- 코드 셀 앞에 설명이 포함된 Markdown 셀 추가
- 코드 셀은 단일 개념 또는 작업에 집중
- 데이터 조작에는 pandas, 시각화에는 matplotlib 사용
- 일반적인 import 패턴:
  ```python
  import pandas as pd
  import numpy as np
  import matplotlib.pyplot as plt
  ```


### JavaScript/Vue.js
- Vue.js 2 스타일 가이드 및 모범 사례 준수
- `quiz-app/package.json`에 ESLint 구성
- Vue 단일 파일 구성 요소 (.vue 파일) 사용
- 컴포넌트 기반 아키텍처 유지
- 변경 사항 커밋 전에 `npm run lint` 실행

### Markdown 문서화
- 명확한 제목 계층 구조 사용 (# ## ### 등)
- 언어 지정자를 포함한 코드 블록 추가
- 이미지에 alt 텍스트 추가
- 관련 강의 및 리소스 링크 추가
- 가독성을 위해 적절한 줄 길이 유지

### 파일 구성
- 번호가 매겨진 폴더에 강의 내용 저장 (01-defining-data-science 등)
- 솔루션은 전용 `solution/` 하위 폴더에 저장
- 번역은 영어 구조를 그대로 따르는 `translations/` 폴더에 저장
- 데이터 파일은 `data/` 또는 강의별 폴더에 저장

## 빌드 및 배포

### 퀴즈 애플리케이션 배포
```bash
cd quiz-app

# Build production version
npm run build

# Output is in dist/ folder
# Deploy dist/ folder to static hosting (Azure Static Web Apps, Netlify, etc.)
```

### Azure Static Web Apps 배포
퀴즈 애플리케이션은 Azure Static Web Apps에 배포 가능:
1. Azure Static Web App 리소스 생성
2. GitHub 저장소 연결
3. 빌드 설정 구성:
   - 앱 위치: `quiz-app`
   - 출력 위치: `dist`
4. GitHub Actions 워크플로우가 푸시 시 자동 배포

### 문서 사이트
```bash
# Build PDF from Docsify (optional)
npm run convert

# Docsify documentation is served directly from markdown files
# No build step required for deployment
# Deploy repository to static hosting with Docsify
```

### GitHub Codespaces
- 저장소에 개발 컨테이너 구성 포함
- Codespaces가 Python 및 Node.js 환경 자동 설정
- GitHub UI를 통해 저장소를 Codespace에서 열기
- 모든 종속성이 자동으로 설치됨

## Pull Request 지침

### 제출 전
```bash
# For Vue.js changes in quiz-app
cd quiz-app
npm run lint
npm run build

# Test changes locally
npm run serve
```

### PR 제목 형식
- 명확하고 설명적인 제목 사용
- 형식: `[컴포넌트] 간단한 설명`
- 예시:
  - `[Lesson 7] Fix Python notebook import error`
  - `[Quiz App] Add German translation`
  - `[Docs] Update README with new prerequisites`

### 필수 검사
- 모든 코드가 오류 없이 실행되는지 확인
- 노트북이 완전히 실행되는지 검증
- Vue.js 애플리케이션이 성공적으로 빌드되는지 확인
- 문서 링크가 작동하는지 확인
- 수정된 경우 퀴즈 애플리케이션 테스트
- 번역이 일관된 구조를 유지하는지 확인

### 기여 지침
- 기존 코드 스타일 및 패턴 준수
- 복잡한 로직에 대한 설명 주석 추가
- 관련 문서 업데이트
- 변경 사항이 적용되는 경우 여러 강의 모듈에서 테스트
- CONTRIBUTING.md 파일 검토

## 추가 참고 사항

### 사용된 주요 라이브러리
- **pandas**: 데이터 조작 및 분석
- **numpy**: 수치 계산
- **matplotlib**: 데이터 시각화 및 플로팅
- **seaborn**: 통계적 데이터 시각화 (일부 강의)
- **scikit-learn**: 머신 러닝 (고급 강의)

### 데이터 파일 작업
- 데이터 파일은 `data/` 폴더 또는 강의별 디렉토리에 위치
- 대부분의 노트북은 상대 경로에서 데이터 파일을 기대
- CSV 파일이 주요 데이터 형식
- 일부 강의는 비관계형 데이터 예제를 위해 JSON 사용

### 다국어 지원
- GitHub Actions를 통한 40개 이상의 언어 번역
- 번역 워크플로우는 `.github/workflows/co-op-translator.yml`에 있음
- 번역은 언어 코드가 포함된 `translations/` 폴더에 저장
- 퀴즈 번역은 `quiz-app/src/assets/translations/`에 저장

### 개발 환경 옵션
1. **로컬 개발**: Python, Jupyter, Node.js를 로컬에 설치
2. **GitHub Codespaces**: 클라우드 기반 즉시 개발 환경
3. **VS Code Dev Containers**: 로컬 컨테이너 기반 개발
4. **Binder**: 클라우드에서 노트북 실행 (구성된 경우)

### 강의 내용 지침
- 각 강의는 독립적이지만 이전 개념을 기반으로 구축
- 강의 전 퀴즈는 사전 지식을 테스트
- 강의 후 퀴즈는 학습을 강화
- 과제는 실습 연습 제공
- 스케치노트는 시각적 요약 제공

### 일반적인 문제 해결

**Jupyter 커널 문제:**
```bash
# Ensure correct kernel is installed
python -m ipykernel install --user --name=datascience
```

**npm 설치 실패:**
```bash
# Clear npm cache and retry
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
```

**노트북에서 Import 오류:**
- 필요한 모든 라이브러리가 설치되었는지 확인
- Python 버전 호환성 확인 (Python 3.7+ 권장)
- 가상 환경이 활성화되었는지 확인

**Docsify가 로드되지 않음:**
- 저장소 루트에서 제공 중인지 확인
- `index.html`이 존재하는지 확인
- 적절한 네트워크 접근 확인 (포트 3000)

### 성능 고려 사항
- 대규모 데이터셋은 노트북에서 로드 시간이 걸릴 수 있음
- 복잡한 플롯의 시각화 렌더링이 느릴 수 있음
- Vue.js 개발 서버는 빠른 반복을 위한 핫 리로드 제공
- 프로덕션 빌드는 최적화되고 축소됨

### 보안 참고 사항
- 민감한 데이터나 자격 증명은 커밋하지 말 것
- 클라우드 강의에서 API 키는 환경 변수로 사용
- Azure 관련 강의는 Azure 계정 자격 증명이 필요할 수 있음
- 보안 패치를 위해 종속성을 최신 상태로 유지

## 번역 기여
- GitHub Actions를 통해 자동 번역 관리
- 번역 정확성을 위한 수동 수정 환영
- 기존 번역 폴더 구조 준수
- 퀴즈 링크에 언어 매개변수 추가: `?loc=fr`
- 번역된 강의가 올바르게 렌더링되는지 테스트

## 관련 리소스
- 주요 커리큘럼: https://aka.ms/datascience-beginners
- Microsoft Learn: https://docs.microsoft.com/learn/
- 학생 허브: https://docs.microsoft.com/learn/student-hub
- 토론 포럼: https://github.com/microsoft/Data-Science-For-Beginners/discussions
- 기타 Microsoft 커리큘럼: ML for Beginners, AI for Beginners, Web Dev for Beginners

## 프로젝트 유지 관리
- 콘텐츠를 최신 상태로 유지하기 위한 정기 업데이트
- 커뮤니티 기여 환영
- GitHub에서 문제 추적
- 커리큘럼 유지 관리자가 PR 검토
- 월간 콘텐츠 리뷰 및 업데이트

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전이 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.