<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a6a8a8a209128cbfedcbc076ee21b0",
  "translation_date": "2025-10-03T15:34:13+00:00",
  "source_file": "TROUBLESHOOTING.md",
  "language_code": "ko"
}
-->
# 문제 해결 가이드

이 가이드는 Data Science for Beginners 커리큘럼을 사용하는 동안 발생할 수 있는 일반적인 문제에 대한 해결책을 제공합니다.

## 목차

- [Python 및 Jupyter 문제](../..)
- [패키지 및 종속성 문제](../..)
- [Jupyter Notebook 문제](../..)
- [퀴즈 애플리케이션 문제](../..)
- [Git 및 GitHub 문제](../..)
- [Docsify 문서 문제](../..)
- [데이터 및 파일 문제](../..)
- [성능 문제](../..)
- [추가 도움 받기](../..)

## Python 및 Jupyter 문제

### Python을 찾을 수 없거나 버전이 잘못됨

**문제:** `python: command not found` 또는 잘못된 Python 버전

**해결책:**

```bash
# Check Python version
python --version
python3 --version

# If Python 3 is installed as 'python3', create an alias
# On macOS/Linux, add to ~/.bashrc or ~/.zshrc:
alias python=python3
alias pip=pip3

# Or use python3 explicitly
python3 -m pip install jupyter
```

**Windows 해결책:**
1. [python.org](https://www.python.org/)에서 Python을 다시 설치합니다.
2. 설치 중 "Add Python to PATH"를 선택합니다.
3. 터미널/명령 프롬프트를 다시 시작합니다.

### 가상 환경 활성화 문제

**문제:** 가상 환경이 활성화되지 않음

**해결책:**

**Windows:**
```bash
# If you get execution policy error
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Then activate
venv\Scripts\activate
```

**macOS/Linux:**
```bash
# Ensure the activate script is executable
chmod +x venv/bin/activate

# Then activate
source venv/bin/activate
```

**활성화 확인:**
```bash
# Your prompt should show (venv)
# Check Python location
which python  # Should point to venv
```

### Jupyter 커널 문제

**문제:** "Kernel not found" 또는 "Kernel keeps dying"

**해결책:**

```bash
# Reinstall kernel
python -m ipykernel install --user --name=datascience --display-name="Python (Data Science)"

# Or use the default kernel
python -m ipykernel install --user

# Restart Jupyter
jupyter notebook
```

**문제:** Jupyter에서 잘못된 Python 버전 사용

**해결책:**
```bash
# Install Jupyter in your virtual environment
source venv/bin/activate  # Activate first
pip install jupyter ipykernel

# Register the kernel
python -m ipykernel install --user --name=venv --display-name="Python (venv)"

# In Jupyter, select Kernel -> Change kernel -> Python (venv)
```

## 패키지 및 종속성 문제

### Import 오류

**문제:** `ModuleNotFoundError: No module named 'pandas'` (또는 다른 패키지)

**해결책:**

```bash
# Ensure virtual environment is activated
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Install missing package
pip install pandas

# Install all common packages
pip install jupyter pandas numpy matplotlib seaborn scikit-learn

# Verify installation
python -c "import pandas; print(pandas.__version__)"
```

### Pip 설치 실패

**문제:** `pip install`이 권한 오류로 실패함

**해결책:**

```bash
# Use --user flag
pip install --user package-name

# Or use virtual environment (recommended)
python -m venv venv
source venv/bin/activate
pip install package-name
```

**문제:** `pip install`이 SSL 인증서 오류로 실패함

**해결책:**

```bash
# Update pip first
python -m pip install --upgrade pip

# Try installing with trusted host (temporary workaround)
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org package-name
```

### 패키지 버전 충돌

**문제:** 호환되지 않는 패키지 버전

**해결책:**

```bash
# Create fresh virtual environment
python -m venv venv-new
source venv-new/bin/activate  # or venv-new\Scripts\activate on Windows

# Install packages with specific versions if needed
pip install pandas==1.3.0
pip install numpy==1.21.0

# Or let pip resolve dependencies
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

## Jupyter Notebook 문제

### Jupyter가 시작되지 않음

**문제:** `jupyter notebook` 명령을 찾을 수 없음

**해결책:**

```bash
# Install Jupyter
pip install jupyter

# Or use python -m
python -m jupyter notebook

# Add to PATH if needed (macOS/Linux)
export PATH="$HOME/.local/bin:$PATH"
```

### Notebook이 로드되지 않거나 저장되지 않음

**문제:** "Notebook failed to load" 또는 저장 오류

**해결책:**

1. 파일 권한 확인
```bash
# Make sure you have write permissions
ls -l notebook.ipynb
chmod 644 notebook.ipynb  # If needed
```

2. 파일 손상 여부 확인
```bash
# Try opening in text editor to check JSON structure
# Copy content to new notebook if corrupted
```

3. Jupyter 캐시 지우기
```bash
jupyter notebook --clear-cache
```

### 셀이 실행되지 않음

**문제:** 셀이 "In [*]" 상태로 멈추거나 실행 시간이 너무 오래 걸림

**해결책:**

1. **커널 중단**: "Interrupt" 버튼 클릭 또는 `I, I` 키 누르기
2. **커널 재시작**: Kernel 메뉴 → Restart
3. **코드에서 무한 루프 확인**
4. **출력 지우기**: Cell → All Output → Clear

### 플롯이 표시되지 않음

**문제:** `matplotlib` 플롯이 Notebook에서 표시되지 않음

**해결책:**

```python
# Add magic command at the top of notebook
%matplotlib inline

import matplotlib.pyplot as plt

# Create plot
plt.plot([1, 2, 3, 4])
plt.show()  # Make sure to call show()
```

**대안 (인터랙티브 플롯):**
```python
%matplotlib notebook
# Or
%matplotlib widget
```

## 퀴즈 애플리케이션 문제

### npm install 실패

**문제:** `npm install` 중 오류 발생

**해결책:**

```bash
# Clear npm cache
npm cache clean --force

# Remove node_modules and package-lock.json
rm -rf node_modules package-lock.json

# Reinstall
npm install

# If still failing, try with legacy peer deps
npm install --legacy-peer-deps
```

### 퀴즈 앱이 시작되지 않음

**문제:** `npm run serve` 실패

**해결책:**

```bash
# Check Node.js version
node --version  # Should be 12.x or higher

# Reinstall dependencies
cd quiz-app
rm -rf node_modules package-lock.json
npm install

# Try different port
npm run serve -- --port 8081
```

### 포트가 이미 사용 중임

**문제:** "Port 8080 is already in use"

**해결책:**

```bash
# Find and kill process on port 8080
# macOS/Linux:
lsof -ti:8080 | xargs kill -9

# Windows:
netstat -ano | findstr :8080
taskkill /PID <PID> /F

# Or use a different port
npm run serve -- --port 8081
```

### 퀴즈가 로드되지 않거나 빈 페이지 표시

**문제:** 퀴즈 앱이 로드되지만 빈 페이지 표시

**해결책:**

1. 브라우저 콘솔에서 오류 확인 (F12)
2. 브라우저 캐시 및 쿠키 지우기
3. 다른 브라우저 사용 시도
4. JavaScript가 활성화되어 있는지 확인
5. 광고 차단기가 방해하는지 확인

```bash
# Rebuild the app
npm run build
npm run serve
```

## Git 및 GitHub 문제

### Git이 인식되지 않음

**문제:** `git: command not found`

**해결책:**

**Windows:**
- [git-scm.com](https://git-scm.com/)에서 Git 설치
- 설치 후 터미널 다시 시작

**macOS:**

> **참고:** Homebrew가 설치되어 있지 않은 경우, 먼저 [https://brew.sh/](https://brew.sh/)의 지침을 따라 설치하세요.
```bash
# Install via Homebrew
brew install git

# Or install Xcode Command Line Tools
xcode-select --install
```

**Linux:**
```bash
sudo apt-get install git  # Debian/Ubuntu
sudo dnf install git      # Fedora
```

### 클론 실패

**문제:** `git clone`이 인증 오류로 실패함

**해결책:**

```bash
# Use HTTPS URL
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# If you have 2FA enabled on GitHub, use Personal Access Token
# Create token at: https://github.com/settings/tokens
# Use token as password when prompted
```

### 권한 거부 (publickey)

**문제:** SSH 키 인증 실패

**해결책:**

```bash
# Generate SSH key
ssh-keygen -t ed25519 -C "your_email@example.com"

# Add key to ssh-agent
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# Add public key to GitHub
# Copy key: cat ~/.ssh/id_ed25519.pub
# Add at: https://github.com/settings/keys
```

## Docsify 문서 문제

### Docsify 명령을 찾을 수 없음

**문제:** `docsify: command not found`

**해결책:**

```bash
# Install globally
npm install -g docsify-cli

# If permission error on macOS/Linux
sudo npm install -g docsify-cli

# Verify installation
docsify --version

# If still not found, add npm global path
# Find npm global path
npm config get prefix

# Add to PATH (add to ~/.bashrc or ~/.zshrc)
export PATH="$PATH:/usr/local/bin"
```

### 문서가 로드되지 않음

**문제:** Docsify가 제공되지만 콘텐츠가 로드되지 않음

**해결책:**

```bash
# Ensure you're in the repository root
cd Data-Science-For-Beginners

# Check for index.html
ls index.html

# Serve with specific port
docsify serve --port 3000

# Check browser console for errors (F12)
```

### 이미지가 표시되지 않음

**문제:** 이미지가 깨진 링크 아이콘으로 표시됨

**해결책:**

1. 이미지 경로가 상대 경로인지 확인
2. 이미지 파일이 저장소에 존재하는지 확인
3. 브라우저 캐시 지우기
4. 파일 확장자가 일치하는지 확인 (일부 시스템에서는 대소문자 구분)

## 데이터 및 파일 문제

### 파일을 찾을 수 없음 오류

**문제:** 데이터를 로드할 때 `FileNotFoundError`

**해결책:**

```python
import os

# Check current working directory
print(os.getcwd())

# Use absolute path
data_path = os.path.join(os.getcwd(), 'data', 'filename.csv')
df = pd.read_csv(data_path)

# Or use relative path from notebook location
df = pd.read_csv('../data/filename.csv')

# Verify file exists
print(os.path.exists('data/filename.csv'))
```

### CSV 읽기 오류

**문제:** CSV 파일 읽기 중 오류 발생

**해결책:**

```python
import pandas as pd

# Try different encodings
df = pd.read_csv('file.csv', encoding='utf-8')
# or
df = pd.read_csv('file.csv', encoding='latin-1')
# or
df = pd.read_csv('file.csv', encoding='ISO-8859-1')

# Handle missing values
df = pd.read_csv('file.csv', na_values=['NA', 'N/A', ''])

# Specify delimiter if not comma
df = pd.read_csv('file.csv', delimiter=';')
```

### 대규모 데이터셋으로 인한 메모리 오류

**문제:** 대규모 파일 로드 시 `MemoryError`

**해결책:**

```python
# Read in chunks
chunk_size = 10000
chunks = []
for chunk in pd.read_csv('large_file.csv', chunksize=chunk_size):
    # Process chunk
    chunks.append(chunk)
df = pd.concat(chunks)

# Or read specific columns only
df = pd.read_csv('file.csv', usecols=['col1', 'col2'])

# Use more efficient data types
df = pd.read_csv('file.csv', dtype={'column_name': 'int32'})
```

## 성능 문제

### Notebook 성능 저하

**문제:** Notebook 실행 속도가 매우 느림

**해결책:**

1. **커널 재시작 및 출력 지우기**
   - Kernel → Restart & Clear Output

2. **사용하지 않는 Notebook 닫기**

3. **코드 최적화:**
```python
# Use vectorized operations instead of loops
# Bad:
result = []
for x in data:
    result.append(x * 2)

# Good:
result = data * 2  # NumPy/Pandas vectorization
```

4. **대규모 데이터셋 샘플링:**
```python
# Work with sample during development
df_sample = df.sample(n=1000)  # or df.head(1000)
```

### 브라우저 충돌

**문제:** 브라우저가 충돌하거나 응답하지 않음

**해결책:**

1. 사용하지 않는 탭 닫기
2. 브라우저 캐시 지우기
3. 브라우저 메모리 증가 (Chrome: `chrome://settings/system`)
4. JupyterLab 사용:
```bash
pip install jupyterlab
jupyter lab
```

## 추가 도움 받기

### 도움 요청 전에

1. 이 문제 해결 가이드 확인
2. [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues) 검색
3. [INSTALLATION.md](INSTALLATION.md) 및 [USAGE.md](USAGE.md) 검토
4. 오류 메시지를 온라인에서 검색

### 도움 요청 방법

문제를 생성하거나 도움을 요청할 때 다음을 포함하세요:

1. **운영 체제**: Windows, macOS 또는 Linux (배포판 포함)
2. **Python 버전**: `python --version` 실행
3. **오류 메시지**: 전체 오류 메시지 복사
4. **재현 단계**: 오류 발생 전에 수행한 작업
5. **시도한 해결책**: 이미 시도한 해결책

**예시:**
```
**Operating System:** macOS 12.0
**Python Version:** 3.9.7
**Error Message:** ModuleNotFoundError: No module named 'pandas'
**Steps to Reproduce:**
1. Activated virtual environment
2. Started Jupyter notebook
3. Tried to import pandas

**What I've Tried:**
- Ran pip install pandas
- Restarted Jupyter
```

### 커뮤니티 리소스

- **GitHub Issues**: [문제 생성](https://github.com/microsoft/Data-Science-For-Beginners/issues/new)
- **Discord**: [커뮤니티 참여](https://aka.ms/ds4beginners/discord)
- **Discussions**: [GitHub Discussions](https://github.com/microsoft/Data-Science-For-Beginners/discussions)
- **Microsoft Learn**: [Q&A 포럼](https://docs.microsoft.com/answers/)

### 관련 문서

- [INSTALLATION.md](INSTALLATION.md) - 설치 지침
- [USAGE.md](USAGE.md) - 커리큘럼 사용 방법
- [CONTRIBUTING.md](CONTRIBUTING.md) - 기여 방법
- [README.md](README.md) - 프로젝트 개요

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전을 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.