<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a64d8afa22ffcc2016bb239188d6acb1",
  "translation_date": "2025-10-03T15:16:31+00:00",
  "source_file": "INSTALLATION.md",
  "language_code": "hk"
}
-->
# 安裝指南

本指南將幫助您設置環境，以使用《初學者數據科學課程》。

## 目錄

- [先決條件](../..)
- [快速開始選項](../..)
- [本地安裝](../..)
- [驗證您的安裝](../..)

## 先決條件

在開始之前，您應該具備以下條件：

- 基本的命令行/終端操作知識
- 一個 GitHub 帳戶（免費）
- 穩定的網絡連接以完成初始設置

## 快速開始選項

### 選項 1：GitHub Codespaces（推薦給初學者）

最簡單的開始方式是使用 GitHub Codespaces，它提供了一個完整的開發環境，直接在瀏覽器中使用。

1. 前往 [倉庫](https://github.com/microsoft/Data-Science-For-Beginners)
2. 點擊 **Code** 下拉菜單
3. 選擇 **Codespaces** 標籤
4. 點擊 **Create codespace on main**
5. 等待環境初始化（2-3 分鐘）

您的環境現在已準備好，所有依賴項都已預先安裝！

### 選項 2：本地開發

如果您希望在自己的電腦上工作，請按照以下詳細說明進行操作。

## 本地安裝

### 步驟 1：安裝 Git

Git 是用於克隆倉庫和跟蹤更改的必要工具。

**Windows:**
- 從 [git-scm.com](https://git-scm.com/download/win) 下載
- 使用默認設置運行安裝程序

**macOS:**
- 使用 Homebrew 安裝：`brew install git`
- 或從 [git-scm.com](https://git-scm.com/download/mac) 下載

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

### 步驟 2：克隆倉庫

```bash
# Clone the repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Navigate to the directory
cd Data-Science-For-Beginners
```

### 步驟 3：安裝 Python 和 Jupyter

數據科學課程需要 Python 3.7 或更高版本。

**Windows:**
1. 從 [python.org](https://www.python.org/downloads/) 下載 Python
2. 安裝過程中勾選 "Add Python to PATH"
3. 驗證安裝：
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

### 步驟 4：設置 Python 環境

建議使用虛擬環境來隔離依賴項。

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### 步驟 5：安裝 Python 套件

安裝所需的數據科學庫：

```bash
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### 步驟 6：安裝 Node.js 和 npm（用於測驗應用）

測驗應用需要 Node.js 和 npm。

**Windows/macOS:**
- 從 [nodejs.org](https://nodejs.org/) 下載（推薦 LTS 版本）
- 運行安裝程序

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

### 步驟 7：安裝測驗應用依賴項

```bash
# Navigate to quiz app directory
cd quiz-app

# Install dependencies
npm install

# Return to root directory
cd ..
```

### 步驟 8：安裝 Docsify（可選）

用於離線訪問文檔：

```bash
npm install -g docsify-cli
```

## 驗證您的安裝

### 測試 Python 和 Jupyter

```bash
# Activate your virtual environment if not already activated
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Start Jupyter Notebook
jupyter notebook
```

您的瀏覽器應打開 Jupyter 界面。您現在可以導航到任何課程的 `.ipynb` 文件。

### 測試測驗應用

```bash
# Navigate to quiz app
cd quiz-app

# Start development server
npm run serve
```

測驗應用應可在 `http://localhost:8080`（如果 8080 端口被佔用，則使用其他端口）訪問。

### 測試文檔服務器

```bash
# From the root directory of the repository
docsify serve
```

文檔應可在 `http://localhost:3000` 訪問。

## 使用 VS Code Dev Containers

如果您已安裝 Docker，可以使用 VS Code Dev Containers：

1. 安裝 [Docker Desktop](https://www.docker.com/products/docker-desktop)
2. 安裝 [Visual Studio Code](https://code.visualstudio.com/)
3. 安裝 [Remote - Containers 擴展](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
4. 在 VS Code 中打開倉庫
5. 按 `F1` 並選擇 "Remote-Containers: Reopen in Container"
6. 等待容器構建（僅首次需要）

## 下一步

- 探索 [README.md](README.md) 以了解課程概覽
- 閱讀 [USAGE.md](USAGE.md) 以了解常見工作流程和示例
- 如果遇到問題，查看 [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
- 如果您想貢獻，請查看 [CONTRIBUTING.md](CONTRIBUTING.md)

## 獲取幫助

如果您遇到問題：

1. 查看 [TROUBLESHOOTING.md](TROUBLESHOOTING.md) 指南
2. 搜索現有的 [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
3. 加入我們的 [Discord 社群](https://aka.ms/ds4beginners/discord)
4. 創建一個新問題，並詳細描述您的問題

---

**免責聲明**：  
本文件已使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。原始語言的文件應被視為權威來源。對於關鍵信息，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋概不負責。