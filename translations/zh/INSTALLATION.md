<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a64d8afa22ffcc2016bb239188d6acb1",
  "translation_date": "2025-10-03T15:15:57+00:00",
  "source_file": "INSTALLATION.md",
  "language_code": "zh"
}
-->
# 安装指南

本指南将帮助您设置环境，以使用《数据科学入门》课程。

## 目录

- [先决条件](../..)
- [快速开始选项](../..)
- [本地安装](../..)
- [验证安装](../..)

## 先决条件

在开始之前，您需要具备以下条件：

- 基本的命令行/终端操作知识
- 一个 GitHub 账户（免费）
- 稳定的互联网连接以完成初始设置

## 快速开始选项

### 选项 1：GitHub Codespaces（推荐初学者使用）

最简单的开始方式是使用 GitHub Codespaces，它提供了一个完整的开发环境，直接在浏览器中运行。

1. 访问 [仓库](https://github.com/microsoft/Data-Science-For-Beginners)
2. 点击 **Code** 下拉菜单
3. 选择 **Codespaces** 标签
4. 点击 **Create codespace on main**
5. 等待环境初始化（2-3分钟）

您的环境现在已经准备好，所有依赖项都已预安装！

### 选项 2：本地开发

如果您希望在自己的电脑上工作，请按照以下详细说明操作。

## 本地安装

### 步骤 1：安装 Git

Git 是用于克隆仓库和跟踪更改的必要工具。

**Windows:**
- 从 [git-scm.com](https://git-scm.com/download/win) 下载
- 使用默认设置运行安装程序

**macOS:**
- 使用 Homebrew 安装：`brew install git`
- 或从 [git-scm.com](https://git-scm.com/download/mac) 下载

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

### 步骤 2：克隆仓库

```bash
# Clone the repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Navigate to the directory
cd Data-Science-For-Beginners
```

### 步骤 3：安装 Python 和 Jupyter

数据科学课程需要 Python 3.7 或更高版本。

**Windows:**
1. 从 [python.org](https://www.python.org/downloads/) 下载 Python
2. 安装时勾选“Add Python to PATH”
3. 验证安装：
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

### 步骤 4：设置 Python 环境

建议使用虚拟环境来隔离依赖项。

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### 步骤 5：安装 Python 包

安装所需的数据科学库：

```bash
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### 步骤 6：安装 Node.js 和 npm（用于测验应用）

测验应用需要 Node.js 和 npm。

**Windows/macOS:**
- 从 [nodejs.org](https://nodejs.org/) 下载（推荐 LTS 版本）
- 运行安装程序

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

### 步骤 7：安装测验应用依赖项

```bash
# Navigate to quiz app directory
cd quiz-app

# Install dependencies
npm install

# Return to root directory
cd ..
```

### 步骤 8：安装 Docsify（可选）

用于离线访问文档：

```bash
npm install -g docsify-cli
```

## 验证安装

### 测试 Python 和 Jupyter

```bash
# Activate your virtual environment if not already activated
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Start Jupyter Notebook
jupyter notebook
```

您的浏览器应该会打开 Jupyter 界面。您现在可以导航到任何课程的 `.ipynb` 文件。

### 测试测验应用

```bash
# Navigate to quiz app
cd quiz-app

# Start development server
npm run serve
```

测验应用应该可以通过 `http://localhost:8080`（如果 8080 端口被占用，则使用其他端口）访问。

### 测试文档服务器

```bash
# From the root directory of the repository
docsify serve
```

文档应该可以通过 `http://localhost:3000` 访问。

## 使用 VS Code Dev Containers

如果您安装了 Docker，可以使用 VS Code Dev Containers：

1. 安装 [Docker Desktop](https://www.docker.com/products/docker-desktop)
2. 安装 [Visual Studio Code](https://code.visualstudio.com/)
3. 安装 [Remote - Containers 扩展](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
4. 在 VS Code 中打开仓库
5. 按 `F1` 并选择“Remote-Containers: Reopen in Container”
6. 等待容器构建（仅首次需要）

## 下一步

- 查看 [README.md](README.md) 了解课程概览
- 阅读 [USAGE.md](USAGE.md) 了解常见工作流程和示例
- 如果遇到问题，请查看 [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
- 如果您想贡献，请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)

## 获取帮助

如果您遇到问题：

1. 查看 [TROUBLESHOOTING.md](TROUBLESHOOTING.md) 指南
2. 搜索现有的 [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
3. 加入我们的 [Discord 社区](https://aka.ms/ds4beginners/discord)
4. 创建一个新问题，并详细描述您的问题

---

**免责声明**：  
本文档使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于关键信息，建议使用专业人工翻译。我们对因使用此翻译而产生的任何误解或误读不承担责任。