<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a6a8a8a209128cbfedcbc076ee21b0",
  "translation_date": "2025-10-03T15:31:56+00:00",
  "source_file": "TROUBLESHOOTING.md",
  "language_code": "zh"
}
-->
# 故障排查指南

本指南提供了解决使用《数据科学入门》课程时可能遇到的常见问题的方法。

## 目录

- [Python 和 Jupyter 问题](../..)
- [包和依赖问题](../..)
- [Jupyter Notebook 问题](../..)
- [测验应用问题](../..)
- [Git 和 GitHub 问题](../..)
- [Docsify 文档问题](../..)
- [数据和文件问题](../..)
- [性能问题](../..)
- [获取额外帮助](../..)

## Python 和 Jupyter 问题

### 找不到 Python 或版本错误

**问题：** `python: command not found` 或 Python 版本错误

**解决方法：**

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

**Windows 解决方法：**
1. 从 [python.org](https://www.python.org/) 重新安装 Python
2. 安装时勾选“Add Python to PATH”
3. 重启终端/命令提示符

### 虚拟环境激活问题

**问题：** 虚拟环境无法激活

**解决方法：**

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

**验证激活：**
```bash
# Your prompt should show (venv)
# Check Python location
which python  # Should point to venv
```

### Jupyter 内核问题

**问题：** “找不到内核”或“内核不断崩溃”

**解决方法：**

```bash
# Reinstall kernel
python -m ipykernel install --user --name=datascience --display-name="Python (Data Science)"

# Or use the default kernel
python -m ipykernel install --user

# Restart Jupyter
jupyter notebook
```

**问题：** Jupyter 中的 Python 版本错误

**解决方法：**
```bash
# Install Jupyter in your virtual environment
source venv/bin/activate  # Activate first
pip install jupyter ipykernel

# Register the kernel
python -m ipykernel install --user --name=venv --display-name="Python (venv)"

# In Jupyter, select Kernel -> Change kernel -> Python (venv)
```

## 包和依赖问题

### 导入错误

**问题：** `ModuleNotFoundError: No module named 'pandas'`（或其他包）

**解决方法：**

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

### Pip 安装失败

**问题：** `pip install` 因权限错误失败

**解决方法：**

```bash
# Use --user flag
pip install --user package-name

# Or use virtual environment (recommended)
python -m venv venv
source venv/bin/activate
pip install package-name
```

**问题：** `pip install` 因 SSL 证书错误失败

**解决方法：**

```bash
# Update pip first
python -m pip install --upgrade pip

# Try installing with trusted host (temporary workaround)
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org package-name
```

### 包版本冲突

**问题：** 包版本不兼容

**解决方法：**

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

## Jupyter Notebook 问题

### Jupyter 无法启动

**问题：** `jupyter notebook` 命令未找到

**解决方法：**

```bash
# Install Jupyter
pip install jupyter

# Or use python -m
python -m jupyter notebook

# Add to PATH if needed (macOS/Linux)
export PATH="$HOME/.local/bin:$PATH"
```

### Notebook 无法加载或保存

**问题：** “Notebook 加载失败”或保存错误

**解决方法：**

1. 检查文件权限
```bash
# Make sure you have write permissions
ls -l notebook.ipynb
chmod 644 notebook.ipynb  # If needed
```

2. 检查文件是否损坏
```bash
# Try opening in text editor to check JSON structure
# Copy content to new notebook if corrupted
```

3. 清除 Jupyter 缓存
```bash
jupyter notebook --clear-cache
```

### 单元格无法执行

**问题：** 单元格卡在“In [*]”或执行时间过长

**解决方法：**

1. **中断内核：** 点击“Interrupt”按钮或按 `I, I`
2. **重启内核：** 内核菜单 → 重启
3. **检查代码中的无限循环**
4. **清除输出：** 单元格 → 所有输出 → 清除

### 图表不显示

**问题：** `matplotlib` 图表未在 Notebook 中显示

**解决方法：**

```python
# Add magic command at the top of notebook
%matplotlib inline

import matplotlib.pyplot as plt

# Create plot
plt.plot([1, 2, 3, 4])
plt.show()  # Make sure to call show()
```

**交互式图表的替代方法：**
```python
%matplotlib notebook
# Or
%matplotlib widget
```

## 测验应用问题

### npm install 失败

**问题：** `npm install` 期间出现错误

**解决方法：**

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

### 测验应用无法启动

**问题：** `npm run serve` 失败

**解决方法：**

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

### 端口已被占用

**问题：** “端口 8080 已被占用”

**解决方法：**

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

### 测验无法加载或显示空白页面

**问题：** 测验应用加载但显示空白页面

**解决方法：**

1. 检查浏览器控制台中的错误（按 F12）
2. 清除浏览器缓存和 Cookie
3. 尝试使用其他浏览器
4. 确保启用了 JavaScript
5. 检查是否有广告拦截器干扰

```bash
# Rebuild the app
npm run build
npm run serve
```

## Git 和 GitHub 问题

### Git 未识别

**问题：** `git: command not found`

**解决方法：**

**Windows：**
- 从 [git-scm.com](https://git-scm.com/) 安装 Git
- 安装后重启终端

**macOS：**

> **注意：** 如果尚未安装 Homebrew，请先按照 [https://brew.sh/](https://brew.sh/) 的说明进行安装。
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

### 克隆失败

**问题：** `git clone` 因身份验证错误失败

**解决方法：**

```bash
# Use HTTPS URL
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# If you have 2FA enabled on GitHub, use Personal Access Token
# Create token at: https://github.com/settings/tokens
# Use token as password when prompted
```

### 权限被拒绝（publickey）

**问题：** SSH 密钥认证失败

**解决方法：**

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

## Docsify 文档问题

### Docsify 命令未找到

**问题：** `docsify: command not found`

**解决方法：**

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

### 文档无法加载

**问题：** Docsify 服务启动但内容未加载

**解决方法：**

```bash
# Ensure you're in the repository root
cd Data-Science-For-Beginners

# Check for index.html
ls index.html

# Serve with specific port
docsify serve --port 3000

# Check browser console for errors (F12)
```

### 图片无法显示

**问题：** 图片显示为断链图标

**解决方法：**

1. 检查图片路径是否为相对路径
2. 确保图片文件存在于仓库中
3. 清除浏览器缓存
4. 验证文件扩展名是否匹配（某些系统对大小写敏感）

## 数据和文件问题

### 文件未找到错误

**问题：** 加载数据时出现 `FileNotFoundError`

**解决方法：**

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

### CSV 读取错误

**问题：** 读取 CSV 文件时出现错误

**解决方法：**

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

### 大数据集导致内存错误

**问题：** 加载大文件时出现 `MemoryError`

**解决方法：**

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

## 性能问题

### Notebook 性能缓慢

**问题：** Notebook 运行速度非常慢

**解决方法：**

1. **重启内核并清除输出**
   - 内核 → 重启并清除输出

2. **关闭未使用的 Notebook**

3. **优化代码：**
```python
# Use vectorized operations instead of loops
# Bad:
result = []
for x in data:
    result.append(x * 2)

# Good:
result = data * 2  # NumPy/Pandas vectorization
```

4. **对大数据集进行采样：**
```python
# Work with sample during development
df_sample = df.sample(n=1000)  # or df.head(1000)
```

### 浏览器崩溃

**问题：** 浏览器崩溃或无响应

**解决方法：**

1. 关闭未使用的标签页
2. 清除浏览器缓存
3. 增加浏览器内存（Chrome：`chrome://settings/system`）
4. 使用 JupyterLab 替代：
```bash
pip install jupyterlab
jupyter lab
```

## 获取额外帮助

### 在寻求帮助之前

1. 查看本故障排查指南
2. 搜索 [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
3. 查看 [INSTALLATION.md](INSTALLATION.md) 和 [USAGE.md](USAGE.md)
4. 尝试在线搜索错误信息

### 如何寻求帮助

在创建问题或寻求帮助时，请提供以下信息：

1. **操作系统：** Windows、macOS 或 Linux（具体发行版）
2. **Python 版本：** 运行 `python --version`
3. **错误信息：** 复制完整的错误信息
4. **复现步骤：** 错误发生前的操作
5. **已尝试的解决方法：** 你已经尝试过的解决方案

**示例：**
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

### 社区资源

- **GitHub Issues：** [创建问题](https://github.com/microsoft/Data-Science-For-Beginners/issues/new)
- **Discord：** [加入我们的社区](https://aka.ms/ds4beginners/discord)
- **讨论区：** [GitHub Discussions](https://github.com/microsoft/Data-Science-For-Beginners/discussions)
- **Microsoft Learn：** [问答论坛](https://docs.microsoft.com/answers/)

### 相关文档

- [INSTALLATION.md](INSTALLATION.md) - 安装说明
- [USAGE.md](USAGE.md) - 如何使用课程
- [CONTRIBUTING.md](CONTRIBUTING.md) - 如何贡献
- [README.md](README.md) - 项目概述

---

**免责声明**：  
本文档使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于关键信息，建议使用专业人工翻译。我们对因使用此翻译而产生的任何误解或误读不承担责任。