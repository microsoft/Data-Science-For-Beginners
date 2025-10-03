<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a64d8afa22ffcc2016bb239188d6acb1",
  "translation_date": "2025-10-03T15:17:24+00:00",
  "source_file": "INSTALLATION.md",
  "language_code": "ko"
}
-->
# 설치 가이드

이 가이드는 초보자를 위한 데이터 과학 커리큘럼을 작업할 수 있도록 환경을 설정하는 방법을 안내합니다.

## 목차

- [사전 준비](../..)
- [빠른 시작 옵션](../..)
- [로컬 설치](../..)
- [설치 확인](../..)

## 사전 준비

시작하기 전에 다음을 준비하세요:

- 명령줄/터미널에 대한 기본적인 이해
- GitHub 계정 (무료)
- 초기 설정을 위한 안정적인 인터넷 연결

## 빠른 시작 옵션

### 옵션 1: GitHub Codespaces (초보자에게 추천)

가장 간단한 시작 방법은 GitHub Codespaces를 사용하는 것입니다. 브라우저에서 완전한 개발 환경을 제공합니다.

1. [저장소](https://github.com/microsoft/Data-Science-For-Beginners)로 이동합니다.
2. **Code** 드롭다운 메뉴를 클릭합니다.
3. **Codespaces** 탭을 선택합니다.
4. **Create codespace on main**을 클릭합니다.
5. 환경이 초기화될 때까지 기다립니다 (2-3분 소요).

이제 모든 종속성이 사전 설치된 상태로 환경이 준비되었습니다!

### 옵션 2: 로컬 개발

자신의 컴퓨터에서 작업하려면 아래의 자세한 지침을 따르세요.

## 로컬 설치

### 1단계: Git 설치

Git은 저장소를 클론하고 변경 사항을 추적하는 데 필요합니다.

**Windows:**
- [git-scm.com](https://git-scm.com/download/win)에서 다운로드합니다.
- 기본 설정으로 설치 프로그램을 실행합니다.

**macOS:**
- Homebrew를 통해 설치: `brew install git`
- 또는 [git-scm.com](https://git-scm.com/download/mac)에서 다운로드합니다.

**Linux:**
```bash
# Debian/Ubuntu
sudo apt-get update
sudo apt-get install git

# Fedora
sudo dnf install git

# Arch
sudo pacman -S git
```

### 2단계: 저장소 클론

```bash
# Clone the repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Navigate to the directory
cd Data-Science-For-Beginners
```

### 3단계: Python 및 Jupyter 설치

데이터 과학 수업에는 Python 3.7 이상이 필요합니다.

**Windows:**
1. [python.org](https://www.python.org/downloads/)에서 Python을 다운로드합니다.
2. 설치 중 "Add Python to PATH"를 체크합니다.
3. 설치 확인:
```bash
python --version
```

**macOS:**
```bash
# Using Homebrew
brew install python3

# Verify installation
python3 --version
```

**Linux:**
```bash
# Most Linux distributions come with Python pre-installed
python3 --version

# If not installed:
# Debian/Ubuntu
sudo apt-get install python3 python3-pip

# Fedora
sudo dnf install python3 python3-pip
```

### 4단계: Python 환경 설정

종속성을 격리하기 위해 가상 환경을 사용하는 것이 좋습니다.

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### 5단계: Python 패키지 설치

필요한 데이터 과학 라이브러리를 설치합니다:

```bash
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### 6단계: Node.js 및 npm 설치 (퀴즈 앱용)

퀴즈 애플리케이션에는 Node.js와 npm이 필요합니다.

**Windows/macOS:**
- [nodejs.org](https://nodejs.org/)에서 다운로드 (LTS 버전 추천)
- 설치 프로그램 실행

**Linux:**
```bash
# Debian/Ubuntu
# WARNING: Piping scripts from the internet directly into bash can be a security risk.
# It is recommended to review the script before running it:
#   curl -fsSL https://deb.nodesource.com/setup_lts.x -o setup_lts.x
#   less setup_lts.x
# Then run:
#   sudo -E bash setup_lts.x
#
# Alternatively, you can use the one-liner below at your own risk:
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt-get install -y nodejs

# Fedora
sudo dnf install nodejs

# Verify installation
node --version
npm --version
```

### 7단계: 퀴즈 앱 종속성 설치

```bash
# Navigate to quiz app directory
cd quiz-app

# Install dependencies
npm install

# Return to root directory
cd ..
```

### 8단계: Docsify 설치 (선택 사항)

문서를 오프라인으로 액세스하려면:

```bash
npm install -g docsify-cli
```

## 설치 확인

### Python 및 Jupyter 테스트

```bash
# Activate your virtual environment if not already activated
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Start Jupyter Notebook
jupyter notebook
```

브라우저가 열리며 Jupyter 인터페이스가 표시됩니다. 이제 각 수업의 `.ipynb` 파일로 이동할 수 있습니다.

### 퀴즈 애플리케이션 테스트

```bash
# Navigate to quiz app
cd quiz-app

# Start development server
npm run serve
```

퀴즈 앱은 `http://localhost:8080` (또는 8080 포트가 사용 중일 경우 다른 포트)에서 사용할 수 있습니다.

### 문서 서버 테스트

```bash
# From the root directory of the repository
docsify serve
```

문서는 `http://localhost:3000`에서 사용할 수 있습니다.

## VS Code Dev Containers 사용

Docker가 설치되어 있다면 VS Code Dev Containers를 사용할 수 있습니다:

1. [Docker Desktop](https://www.docker.com/products/docker-desktop)을 설치합니다.
2. [Visual Studio Code](https://code.visualstudio.com/)를 설치합니다.
3. [Remote - Containers 확장](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)을 설치합니다.
4. VS Code에서 저장소를 엽니다.
5. `F1`을 누르고 "Remote-Containers: Reopen in Container"를 선택합니다.
6. 컨테이너가 빌드될 때까지 기다립니다 (최초 실행 시만).

## 다음 단계

- 커리큘럼 개요는 [README.md](README.md)를 확인하세요.
- 일반적인 워크플로와 예제는 [USAGE.md](USAGE.md)를 읽어보세요.
- 문제가 발생하면 [TROUBLESHOOTING.md](TROUBLESHOOTING.md)를 확인하세요.
- 기여를 원한다면 [CONTRIBUTING.md](CONTRIBUTING.md)를 검토하세요.

## 도움 받기

문제가 발생하면:

1. [TROUBLESHOOTING.md](TROUBLESHOOTING.md) 가이드를 확인하세요.
2. 기존 [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)를 검색하세요.
3. [Discord 커뮤니티](https://aka.ms/ds4beginners/discord)에 참여하세요.
4. 문제에 대한 자세한 정보를 포함하여 새 이슈를 생성하세요.

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전을 신뢰할 수 있는 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.