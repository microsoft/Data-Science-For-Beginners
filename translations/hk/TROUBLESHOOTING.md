<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a6a8a8a209128cbfedcbc076ee21b0",
  "translation_date": "2025-10-03T15:32:40+00:00",
  "source_file": "TROUBLESHOOTING.md",
  "language_code": "hk"
}
-->
# 疑難排解指南

本指南提供了解決在使用《初學者數據科學》課程時可能遇到的常見問題的方法。

## 目錄

- [Python 和 Jupyter 問題](../..)
- [套件和依賴問題](../..)
- [Jupyter Notebook 問題](../..)
- [測驗應用程式問題](../..)
- [Git 和 GitHub 問題](../..)
- [Docsify 文件問題](../..)
- [數據和檔案問題](../..)
- [效能問題](../..)
- [尋求額外幫助](../..)

## Python 和 Jupyter 問題

### 找不到 Python 或版本錯誤

**問題：** `python: command not found` 或 Python 版本錯誤

**解決方法：**

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

**Windows 解決方法：**
1. 從 [python.org](https://www.python.org/) 重新安裝 Python
2. 安裝過程中勾選 "Add Python to PATH"
3. 重啟終端/命令提示符

### 虛擬環境啟動問題

**問題：** 虛擬環境無法啟動

**解決方法：**

**Windows：**
```bash
# If you get execution policy error
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Then activate
venv\Scripts\activate
```

**macOS/Linux：**
```bash
# Ensure the activate script is executable
chmod +x venv/bin/activate

# Then activate
source venv/bin/activate
```

**驗證啟動：**
```bash
# Your prompt should show (venv)
# Check Python location
which python  # Should point to venv
```

### Jupyter 核心問題

**問題：** "Kernel not found" 或 "Kernel keeps dying"

**解決方法：**

```bash
# Reinstall kernel
python -m ipykernel install --user --name=datascience --display-name="Python (Data Science)"

# Or use the default kernel
python -m ipykernel install --user

# Restart Jupyter
jupyter notebook
```

**問題：** Jupyter 中的 Python 版本錯誤

**解決方法：**
```bash
# Install Jupyter in your virtual environment
source venv/bin/activate  # Activate first
pip install jupyter ipykernel

# Register the kernel
python -m ipykernel install --user --name=venv --display-name="Python (venv)"

# In Jupyter, select Kernel -> Change kernel -> Python (venv)
```

## 套件和依賴問題

### 匯入錯誤

**問題：** `ModuleNotFoundError: No module named 'pandas'`（或其他套件）

**解決方法：**

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

### Pip 安裝失敗

**問題：** `pip install` 因權限錯誤失敗

**解決方法：**

```bash
# Use --user flag
pip install --user package-name

# Or use virtual environment (recommended)
python -m venv venv
source venv/bin/activate
pip install package-name
```

**問題：** `pip install` 因 SSL 憑證錯誤失敗

**解決方法：**

```bash
# Update pip first
python -m pip install --upgrade pip

# Try installing with trusted host (temporary workaround)
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org package-name
```

### 套件版本衝突

**問題：** 套件版本不兼容

**解決方法：**

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

## Jupyter Notebook 問題

### Jupyter 無法啟動

**問題：** `jupyter notebook` 命令未找到

**解決方法：**

```bash
# Install Jupyter
pip install jupyter

# Or use python -m
python -m jupyter notebook

# Add to PATH if needed (macOS/Linux)
export PATH="$HOME/.local/bin:$PATH"
```

### Notebook 無法加載或保存

**問題：** "Notebook failed to load" 或保存錯誤

**解決方法：**

1. 檢查檔案權限
```bash
# Make sure you have write permissions
ls -l notebook.ipynb
chmod 644 notebook.ipynb  # If needed
```

2. 檢查檔案是否損壞
```bash
# Try opening in text editor to check JSON structure
# Copy content to new notebook if corrupted
```

3. 清除 Jupyter 快取
```bash
jupyter notebook --clear-cache
```

### Cell 無法執行

**問題：** Cell 停留在 "In [*]" 或執行時間過長

**解決方法：**

1. **中斷核心**：點擊 "Interrupt" 按鈕或按 `I, I`
2. **重啟核心**：Kernel 菜單 → Restart
3. **檢查代碼中的無限循環**
4. **清除輸出**：Cell → All Output → Clear

### 圖表無法顯示

**問題：** `matplotlib` 圖表未在 Notebook 中顯示

**解決方法：**

```python
# Add magic command at the top of notebook
%matplotlib inline

import matplotlib.pyplot as plt

# Create plot
plt.plot([1, 2, 3, 4])
plt.show()  # Make sure to call show()
```

**互動式圖表的替代方法：**
```python
%matplotlib notebook
# Or
%matplotlib widget
```

## 測驗應用程式問題

### npm install 失敗

**問題：** `npm install` 過程中出現錯誤

**解決方法：**

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

### 測驗應用程式無法啟動

**問題：** `npm run serve` 失敗

**解決方法：**

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

### 埠已被佔用

**問題：** "Port 8080 is already in use"

**解決方法：**

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

### 測驗無法加載或顯示空白頁面

**問題：** 測驗應用程式加載但顯示空白頁面

**解決方法：**

1. 檢查瀏覽器控制台中的錯誤（F12）
2. 清除瀏覽器快取和 Cookie
3. 嘗試使用其他瀏覽器
4. 確保 JavaScript 已啟用
5. 檢查是否有廣告攔截器干擾

```bash
# Rebuild the app
npm run build
npm run serve
```

## Git 和 GitHub 問題

### Git 未被識別

**問題：** `git: command not found`

**解決方法：**

**Windows：**
- 從 [git-scm.com](https://git-scm.com/) 安裝 Git
- 安裝後重啟終端

**macOS：**

> **注意：** 如果尚未安裝 Homebrew，請按照 [https://brew.sh/](https://brew.sh/) 的指示進行安裝。
```bash
# Install via Homebrew
brew install git

# Or install Xcode Command Line Tools
xcode-select --install
```

**Linux：**
```bash
sudo apt-get install git  # Debian/Ubuntu
sudo dnf install git      # Fedora
```

### Clone 失敗

**問題：** `git clone` 因身份驗證錯誤失敗

**解決方法：**

```bash
# Use HTTPS URL
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# If you have 2FA enabled on GitHub, use Personal Access Token
# Create token at: https://github.com/settings/tokens
# Use token as password when prompted
```

### 權限被拒絕（publickey）

**問題：** SSH 密鑰身份驗證失敗

**解決方法：**

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

## Docsify 文件問題

### Docsify 命令未找到

**問題：** `docsify: command not found`

**解決方法：**

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

### 文件無法加載

**問題：** Docsify 啟動但內容未加載

**解決方法：**

```bash
# Ensure you're in the repository root
cd Data-Science-For-Beginners

# Check for index.html
ls index.html

# Serve with specific port
docsify serve --port 3000

# Check browser console for errors (F12)
```

### 圖片無法顯示

**問題：** 圖片顯示為斷鏈圖標

**解決方法：**

1. 檢查圖片路徑是否為相對路徑
2. 確保圖片檔案存在於倉庫中
3. 清除瀏覽器快取
4. 驗證檔案擴展名是否匹配（某些系統對大小寫敏感）

## 數據和檔案問題

### 檔案未找到錯誤

**問題：** 加載數據時出現 `FileNotFoundError`

**解決方法：**

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

### CSV 讀取錯誤

**問題：** 讀取 CSV 檔案時出現錯誤

**解決方法：**

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

### 大型數據集的記憶體錯誤

**問題：** 加載大型檔案時出現 `MemoryError`

**解決方法：**

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

## 效能問題

### Notebook 效能緩慢

**問題：** Notebook 運行速度非常慢

**解決方法：**

1. **重啟核心並清除輸出**
   - Kernel → Restart & Clear Output

2. **關閉未使用的 Notebook**

3. **優化代碼：**
```python
# Use vectorized operations instead of loops
# Bad:
result = []
for x in data:
    result.append(x * 2)

# Good:
result = data * 2  # NumPy/Pandas vectorization
```

4. **抽樣大型數據集：**
```python
# Work with sample during development
df_sample = df.sample(n=1000)  # or df.head(1000)
```

### 瀏覽器崩潰

**問題：** 瀏覽器崩潰或無響應

**解決方法：**

1. 關閉未使用的標籤
2. 清除瀏覽器快取
3. 增加瀏覽器記憶體（Chrome：`chrome://settings/system`）
4. 使用 JupyterLab 替代：
```bash
pip install jupyterlab
jupyter lab
```

## 尋求額外幫助

### 在尋求幫助之前

1. 檢查本疑難排解指南
2. 搜索 [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
3. 查看 [INSTALLATION.md](INSTALLATION.md) 和 [USAGE.md](USAGE.md)
4. 嘗試在線搜索錯誤信息

### 如何尋求幫助

在創建問題或尋求幫助時，請提供以下信息：

1. **操作系統**：Windows、macOS 或 Linux（哪個版本）
2. **Python 版本**：運行 `python --version`
3. **錯誤信息**：複製完整的錯誤信息
4. **重現步驟**：描述錯誤發生前的操作
5. **已嘗試的解決方法**：列出已嘗試的解決方法

**範例：**
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

### 社群資源

- **GitHub Issues**：[創建問題](https://github.com/microsoft/Data-Science-For-Beginners/issues/new)
- **Discord**：[加入我們的社群](https://aka.ms/ds4beginners/discord)
- **討論區**：[GitHub Discussions](https://github.com/microsoft/Data-Science-For-Beginners/discussions)
- **Microsoft Learn**：[問答論壇](https://docs.microsoft.com/answers/)

### 相關文件

- [INSTALLATION.md](INSTALLATION.md) - 安裝指南
- [USAGE.md](USAGE.md) - 如何使用課程
- [CONTRIBUTING.md](CONTRIBUTING.md) - 如何貢獻
- [README.md](README.md) - 專案概述

---

**免責聲明**：  
本文件已使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要信息，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋概不負責。