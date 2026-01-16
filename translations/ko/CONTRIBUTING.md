<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "10f86fb29b5407088445ac803b3d0ed1",
  "translation_date": "2025-10-03T13:37:51+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "ko"
}
-->
# 초보자를 위한 데이터 과학 기여하기

초보자를 위한 데이터 과학 커리큘럼에 관심을 가져주셔서 감사합니다! 커뮤니티의 기여를 환영합니다.

## 목차

- [행동 강령](../..)
- [어떻게 기여할 수 있나요?](../..)
- [시작하기](../..)
- [기여 지침](../..)
- [풀 리퀘스트 프로세스](../..)
- [스타일 지침](../..)
- [기여자 라이선스 계약](../..)

## 행동 강령

이 프로젝트는 [Microsoft 오픈 소스 행동 강령](https://opensource.microsoft.com/codeofconduct/)을 채택했습니다.  
자세한 내용은 [행동 강령 FAQ](https://opensource.microsoft.com/codeofconduct/faq/)를 참조하거나 추가 질문이나 의견이 있는 경우 [opencode@microsoft.com](mailto:opencode@microsoft.com)으로 연락하세요.

## 어떻게 기여할 수 있나요?

### 버그 신고

버그 신고를 작성하기 전에 기존 문제를 확인하여 중복을 피하세요. 버그 신고를 작성할 때 가능한 많은 세부 정보를 포함하세요:

- **명확하고 설명적인 제목 사용**
- **문제를 재현하는 정확한 단계 설명**
- **구체적인 예 제공** (코드 스니펫, 스크린샷)
- **관찰한 동작과 기대했던 동작 설명**
- **환경 세부 정보 포함** (운영 체제, Python 버전, 브라우저)

### 개선 사항 제안

개선 사항 제안을 환영합니다! 개선 사항을 제안할 때:

- **명확하고 설명적인 제목 사용**
- **제안된 개선 사항에 대한 상세한 설명 제공**
- **이 개선 사항이 왜 유용한지 설명**
- **다른 프로젝트에서 유사한 기능이 있다면 목록 작성**

### 문서 기여

문서 개선은 항상 환영합니다:

- **오타 및 문법 오류 수정**
- **설명의 명확성 향상**
- **누락된 문서 추가**
- **오래된 정보 업데이트**
- **예제나 사용 사례 추가**

### 코드 기여

다음과 같은 코드 기여를 환영합니다:

- **새로운 레슨이나 연습 문제**
- **버그 수정**
- **기존 노트북 개선**
- **새로운 데이터셋이나 예제**
- **퀴즈 애플리케이션 개선**

## 시작하기

### 사전 준비

기여하기 전에 다음을 준비하세요:

1. GitHub 계정
2. 시스템에 Git 설치
3. Python 3.7+ 및 Jupyter 설치
4. Node.js 및 npm (퀴즈 앱 기여를 위한)
5. 커리큘럼 구조에 대한 이해

자세한 설치 지침은 [INSTALLATION.md](INSTALLATION.md)를 참조하세요.

### 포크 및 클론

1. GitHub에서 **저장소를 포크**하세요.
2. 로컬에 **포크를 클론**하세요:
   ```bash
   git clone https://github.com/YOUR-USERNAME/Data-Science-For-Beginners.git
   cd Data-Science-For-Beginners
   ```
3. **업스트림 원격 추가**:
   ```bash
   git remote add upstream https://github.com/microsoft/Data-Science-For-Beginners.git
   ```

### 브랜치 생성

작업을 위한 새 브랜치를 생성하세요:

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

브랜치 명명 규칙:
- `feature/` - 새로운 기능 또는 레슨
- `fix/` - 버그 수정
- `docs/` - 문서 변경
- `refactor/` - 코드 리팩토링

## 기여 지침

### 레슨 콘텐츠에 대한 기여

레슨을 기여하거나 기존 레슨을 수정할 때:

1. **기존 구조를 따르세요**:
   - README.md에 레슨 콘텐츠 포함
   - 연습 문제를 포함한 Jupyter 노트북
   - 과제 (해당되는 경우)
   - 사전 및 사후 퀴즈 링크

2. **다음 요소를 포함하세요**:
   - 명확한 학습 목표
   - 단계별 설명
   - 주석이 포함된 코드 예제
   - 연습 문제
   - 추가 자료 링크

3. **접근성을 고려하세요**:
   - 명확하고 간단한 언어 사용
   - 이미지에 대체 텍스트 제공
   - 코드 주석 포함
   - 다양한 학습 스타일을 고려

### Jupyter 노트북에 대한 기여

1. **모든 출력 지우기**:
   ```bash
   jupyter nbconvert --clear-output --inplace notebook.ipynb
   ```

2. **설명이 포함된 마크다운 셀 추가**

3. **일관된 포맷 사용**:
   ```python
   # Import libraries at the top
   import pandas as pd
   import numpy as np
   import matplotlib.pyplot as plt
   
   # Use meaningful variable names
   # Add comments for complex operations
   # Follow PEP 8 style guidelines
   ```

4. **노트북을 완전히 테스트**한 후 제출

### Python 코드에 대한 기여

[PEP 8](https://www.python.org/dev/peps/pep-0008/) 스타일 지침을 따르세요:

```python
# Good practices
import pandas as pd

def calculate_mean(data):
    """Calculate the mean of a dataset.
    
    Args:
        data (list): List of numerical values
        
    Returns:
        float: Mean of the dataset
    """
    return sum(data) / len(data)
```

### 퀴즈 앱 기여

퀴즈 애플리케이션을 수정할 때:

1. **로컬에서 테스트**:
   ```bash
   cd quiz-app
   npm install
   npm run serve
   ```

2. **린터 실행**:
   ```bash
   npm run lint
   ```

3. **성공적으로 빌드**:
   ```bash
   npm run build
   ```

4. **Vue.js 스타일 가이드** 및 기존 패턴 따르기

### 번역 기여

번역을 추가하거나 업데이트할 때:

1. `translations/` 폴더의 구조를 따르세요.
2. 언어 코드를 폴더 이름으로 사용 (예: 프랑스어는 `fr`)
3. 영어 버전과 동일한 파일 구조 유지
4. 퀴즈 링크에 언어 매개변수 추가: `?loc=fr`
5. 모든 링크와 포맷을 테스트

## 풀 리퀘스트 프로세스

### 제출 전

1. **최신 변경 사항으로 브랜치 업데이트**:
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. **변경 사항 테스트**:
   - 수정된 모든 노트북 실행
   - 퀴즈 앱 테스트 (수정된 경우)
   - 모든 링크 확인
   - 철자 및 문법 오류 확인

3. **변경 사항 커밋**:
   ```bash
   git add .
   git commit -m "Brief description of changes"
   ```
   
   명확한 커밋 메시지 작성:
   - 현재 시제 사용 ("Add feature" 대신 "Added feature" 사용하지 않음)
   - 명령형 사용 ("Move cursor to..." 대신 "Moves cursor to..." 사용하지 않음)
   - 첫 줄은 72자 이내로 제한
   - 관련 문제 및 풀 리퀘스트 참조

4. **포크에 푸시**:
   ```bash
   git push origin feature/your-feature-name
   ```

### 풀 리퀘스트 생성

1. [저장소](https://github.com/microsoft/Data-Science-For-Beginners)로 이동
2. "Pull requests" → "New pull request" 클릭
3. "compare across forks" 클릭
4. 포크와 브랜치 선택
5. "Create pull request" 클릭

### PR 제목 형식

다음 형식을 따르는 명확하고 설명적인 제목 사용:

```
[Component] Brief description
```

예시:
- `[Lesson 7] Fix Python notebook import error`
- `[Quiz App] Add German translation`
- `[Docs] Update README with new prerequisites`
- `[Fix] Correct data path in visualization lesson`

### PR 설명

PR 설명에 포함할 내용:

- **무엇**: 어떤 변경을 했는지
- **왜**: 이러한 변경이 왜 필요한지
- **어떻게**: 변경을 어떻게 구현했는지
- **테스트**: 변경 사항을 어떻게 테스트했는지
- **스크린샷**: 시각적 변경 사항이 있다면 스크린샷 포함
- **관련 문제**: 관련 문제 링크 (예: "Fixes #123")

### 리뷰 프로세스

1. **자동화된 검사**가 PR에서 실행됩니다.
2. **유지 관리자가 기여를 검토**합니다.
3. **피드백을 반영**하여 추가 커밋 작성
4. 승인되면 **유지 관리자가 PR을 병합**합니다.

### PR 병합 후

1. 브랜치 삭제:
   ```bash
   git branch -d feature/your-feature-name
   git push origin --delete feature/your-feature-name
   ```

2. 포크 업데이트:
   ```bash
   git checkout main
   git pull upstream main
   git push origin main
   ```

## 스타일 지침

### 마크다운

- 일관된 제목 수준 사용
- 섹션 간 빈 줄 포함
- 언어 지정이 포함된 코드 블록 사용:
  ````markdown
  ```python
  import pandas as pd
  ```
  ````
- 이미지에 대체 텍스트 추가: `![Alt text](../../translated_images/ko/image.4ee84a82b5e4c9e6651b13fd27dcf615e427ec584929f2cef7167aa99151a77a.png)`
- 줄 길이는 적당히 유지 (약 80-100자)

### Python

- PEP 8 스타일 가이드 준수
- 의미 있는 변수 이름 사용
- 함수에 docstring 추가
- 적절한 경우 타입 힌트 포함:
  ```python
  def process_data(df: pd.DataFrame) -> pd.DataFrame:
      """Process the input dataframe."""
      return df
  ```

### JavaScript/Vue.js

- Vue.js 2 스타일 가이드 준수
- 제공된 ESLint 구성 사용
- 모듈화된 재사용 가능한 컴포넌트 작성
- 복잡한 로직에 주석 추가

### 파일 구성

- 관련 파일을 함께 유지
- 설명적인 파일 이름 사용
- 기존 디렉토리 구조 따르기
- 불필요한 파일 커밋 금지 (.DS_Store, .pyc, node_modules 등)

## 기여자 라이선스 계약

이 프로젝트는 기여와 제안을 환영합니다. 대부분의 기여는 기여자 라이선스 계약 (CLA)에 동의해야 하며, 이를 통해 기여자가 기여를 사용할 권리를 가지고 있음을 선언합니다. 자세한 내용은 https://cla.microsoft.com을 참조하세요.

풀 리퀘스트를 제출하면 CLA 봇이 자동으로 CLA 제공 여부를 결정하고 PR에 적절히 표시합니다 (예: 라벨, 댓글). 봇이 제공하는 지침을 따르세요. 이는 CLA를 사용하는 모든 저장소에서 한 번만 수행하면 됩니다.

## 질문이 있나요?

- [Discord 채널 #data-science-for-beginners](https://aka.ms/ds4beginners/discord)를 확인하세요.
- [Discord 커뮤니티](https://aka.ms/ds4beginners/discord)에 참여하세요.
- 기존 [문제](https://github.com/microsoft/Data-Science-For-Beginners/issues) 및 [풀 리퀘스트](https://github.com/microsoft/Data-Science-For-Beginners/pulls)를 검토하세요.

## 감사합니다!

여러분의 기여는 이 커리큘럼을 모두에게 더 나은 것으로 만듭니다. 기여해 주셔서 감사합니다!

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서를 해당 언어로 작성된 상태에서 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.