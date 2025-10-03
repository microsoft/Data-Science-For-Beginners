<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a6a8a8a209128cbfedcbc076ee21b0",
  "translation_date": "2025-10-03T15:33:38+00:00",
  "source_file": "TROUBLESHOOTING.md",
  "language_code": "ja"
}
-->
# トラブルシューティングガイド

このガイドでは、Data Science for Beginners カリキュラムを使用する際に遭遇する可能性のある一般的な問題の解決策を提供します。

## 目次

- [PythonとJupyterの問題](../..)
- [パッケージと依存関係の問題](../..)
- [Jupyter Notebookの問題](../..)
- [クイズアプリケーションの問題](../..)
- [GitとGitHubの問題](../..)
- [Docsifyドキュメントの問題](../..)
- [データとファイルの問題](../..)
- [パフォーマンスの問題](../..)
- [追加のヘルプを得る方法](../..)

## PythonとJupyterの問題

### Pythonが見つからない、またはバージョンが間違っている

**問題:** `python: command not found` またはPythonのバージョンが間違っている

**解決策:**

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

**Windowsでの解決策:**
1. [python.org](https://www.python.org/) からPythonを再インストールする
2. インストール時に「Add Python to PATH」をチェックする
3. ターミナル/コマンドプロンプトを再起動する

### 仮想環境のアクティベーションの問題

**問題:** 仮想環境がアクティベートされない

**解決策:**

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

**アクティベーションの確認:**
```bash
# Your prompt should show (venv)
# Check Python location
which python  # Should point to venv
```

### Jupyterカーネルの問題

**問題:** 「カーネルが見つからない」または「カーネルが頻繁に死ぬ」

**解決策:**

```bash
# Reinstall kernel
python -m ipykernel install --user --name=datascience --display-name="Python (Data Science)"

# Or use the default kernel
python -m ipykernel install --user

# Restart Jupyter
jupyter notebook
```

**問題:** JupyterでPythonのバージョンが間違っている

**解決策:**
```bash
# Install Jupyter in your virtual environment
source venv/bin/activate  # Activate first
pip install jupyter ipykernel

# Register the kernel
python -m ipykernel install --user --name=venv --display-name="Python (venv)"

# In Jupyter, select Kernel -> Change kernel -> Python (venv)
```

## パッケージと依存関係の問題

### インポートエラー

**問題:** `ModuleNotFoundError: No module named 'pandas'`（または他のパッケージ）

**解決策:**

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

### Pipインストールの失敗

**問題:** `pip install` が権限エラーで失敗する

**解決策:**

```bash
# Use --user flag
pip install --user package-name

# Or use virtual environment (recommended)
python -m venv venv
source venv/bin/activate
pip install package-name
```

**問題:** `pip install` がSSL証明書エラーで失敗する

**解決策:**

```bash
# Update pip first
python -m pip install --upgrade pip

# Try installing with trusted host (temporary workaround)
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org package-name
```

### パッケージバージョンの競合

**問題:** パッケージのバージョンが互換性がない

**解決策:**

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

## Jupyter Notebookの問題

### Jupyterが起動しない

**問題:** `jupyter notebook` コマンドが見つからない

**解決策:**

```bash
# Install Jupyter
pip install jupyter

# Or use python -m
python -m jupyter notebook

# Add to PATH if needed (macOS/Linux)
export PATH="$HOME/.local/bin:$PATH"
```

### Notebookが読み込めない、または保存できない

**問題:** 「Notebookの読み込みに失敗」または保存エラー

**解決策:**

1. ファイルの権限を確認する
```bash
# Make sure you have write permissions
ls -l notebook.ipynb
chmod 644 notebook.ipynb  # If needed
```

2. ファイルの破損を確認する
```bash
# Try opening in text editor to check JSON structure
# Copy content to new notebook if corrupted
```

3. Jupyterのキャッシュをクリアする
```bash
jupyter notebook --clear-cache
```

### セルが実行されない

**問題:** セルが「In [*]」のまま止まる、または非常に時間がかかる

**解決策:**

1. **カーネルを中断する**: 「Interrupt」ボタンをクリックするか、`I, I` を押す
2. **カーネルを再起動する**: カーネルメニュー → 再起動
3. **コード内の無限ループを確認する**
4. **出力をクリアする**: セル → 全ての出力 → クリア

### プロットが表示されない

**問題:** `matplotlib` のプロットがNotebookに表示されない

**解決策:**

```python
# Add magic command at the top of notebook
%matplotlib inline

import matplotlib.pyplot as plt

# Create plot
plt.plot([1, 2, 3, 4])
plt.show()  # Make sure to call show()
```

**インタラクティブなプロットの代替案:**
```python
%matplotlib notebook
# Or
%matplotlib widget
```

## クイズアプリケーションの問題

### npm installが失敗する

**問題:** `npm install` 実行時にエラーが発生する

**解決策:**

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

### クイズアプリが起動しない

**問題:** `npm run serve` が失敗する

**解決策:**

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

### ポートが既に使用中

**問題:** 「ポート8080が既に使用中」

**解決策:**

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

### クイズが読み込まれない、または空白のページが表示される

**問題:** クイズアプリは読み込まれるが空白のページが表示される

**解決策:**

1. ブラウザのコンソールでエラーを確認する（F12）
2. ブラウザのキャッシュとクッキーをクリアする
3. 別のブラウザを試す
4. JavaScriptが有効になっていることを確認する
5. 広告ブロッカーが干渉していないか確認する

```bash
# Rebuild the app
npm run build
npm run serve
```

## GitとGitHubの問題

### Gitが認識されない

**問題:** `git: command not found`

**解決策:**

**Windows:**
- [git-scm.com](https://git-scm.com/) からGitをインストールする
- インストール後にターミナルを再起動する

**macOS:**

> **Note:** Homebrewがインストールされていない場合は、[https://brew.sh/](https://brew.sh/) の指示に従って最初にインストールしてください。
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

### クローンが失敗する

**問題:** `git clone` が認証エラーで失敗する

**解決策:**

```bash
# Use HTTPS URL
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# If you have 2FA enabled on GitHub, use Personal Access Token
# Create token at: https://github.com/settings/tokens
# Use token as password when prompted
```

### パーミッション拒否 (publickey)

**問題:** SSHキー認証が失敗する

**解決策:**

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

## Docsifyドキュメントの問題

### Docsifyコマンドが見つからない

**問題:** `docsify: command not found`

**解決策:**

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

### ドキュメントが読み込まれない

**問題:** Docsifyが提供されるがコンテンツが読み込まれない

**解決策:**

```bash
# Ensure you're in the repository root
cd Data-Science-For-Beginners

# Check for index.html
ls index.html

# Serve with specific port
docsify serve --port 3000

# Check browser console for errors (F12)
```

### 画像が表示されない

**問題:** 画像が壊れたリンクアイコンとして表示される

**解決策:**

1. 画像パスが相対パスであることを確認する
2. 画像ファイルがリポジトリ内に存在することを確認する
3. ブラウザのキャッシュをクリアする
4. ファイル拡張子が一致していることを確認する（システムによっては大文字小文字が区別される）

## データとファイルの問題

### ファイルが見つからないエラー

**問題:** データを読み込む際に`FileNotFoundError`が発生する

**解決策:**

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

### CSV読み込みエラー

**問題:** CSVファイルの読み込み時にエラーが発生する

**解決策:**

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

### 大規模データセットでのメモリエラー

**問題:** 大きなファイルを読み込む際に`MemoryError`が発生する

**解決策:**

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

## パフォーマンスの問題

### Notebookのパフォーマンスが遅い

**問題:** Notebookの実行速度が非常に遅い

**解決策:**

1. **カーネルを再起動して出力をクリアする**
   - カーネル → 再起動 & 出力をクリア

2. **使用していないNotebookを閉じる**

3. **コードを最適化する:**
```python
# Use vectorized operations instead of loops
# Bad:
result = []
for x in data:
    result.append(x * 2)

# Good:
result = data * 2  # NumPy/Pandas vectorization
```

4. **大規模データセットをサンプリングする:**
```python
# Work with sample during development
df_sample = df.sample(n=1000)  # or df.head(1000)
```

### ブラウザがクラッシュする

**問題:** ブラウザがクラッシュする、または応答しなくなる

**解決策:**

1. 使用していないタブを閉じる
2. ブラウザのキャッシュをクリアする
3. ブラウザのメモリを増やす（Chrome: `chrome://settings/system`）
4. JupyterLabを使用する:
```bash
pip install jupyterlab
jupyter lab
```

## 追加のヘルプを得る方法

### ヘルプを求める前に

1. このトラブルシューティングガイドを確認する
2. [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues) を検索する
3. [INSTALLATION.md](INSTALLATION.md) と [USAGE.md](USAGE.md) を確認する
4. エラーメッセージをオンラインで検索してみる

### ヘルプを求める方法

問題を報告する際やヘルプを求める際には、以下を含めてください:

1. **オペレーティングシステム**: Windows、macOS、またはLinux（どのディストリビューションか）
2. **Pythonのバージョン**: `python --version` を実行する
3. **エラーメッセージ**: 完全なエラーメッセージをコピーする
4. **再現手順**: エラーが発生する前に行った操作
5. **試したこと**: 既に試した解決策

**例:**
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

### コミュニティリソース

- **GitHub Issues**: [問題を作成する](https://github.com/microsoft/Data-Science-For-Beginners/issues/new)
- **Discord**: [コミュニティに参加する](https://aka.ms/ds4beginners/discord)
- **ディスカッション**: [GitHub Discussions](https://github.com/microsoft/Data-Science-For-Beginners/discussions)
- **Microsoft Learn**: [Q&Aフォーラム](https://docs.microsoft.com/answers/)

### 関連ドキュメント

- [INSTALLATION.md](INSTALLATION.md) - セットアップ手順
- [USAGE.md](USAGE.md) - カリキュラムの使用方法
- [CONTRIBUTING.md](CONTRIBUTING.md) - 貢献方法
- [README.md](README.md) - プロジェクト概要

---

**免責事項**:  
この文書は、AI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。元の言語で記載された文書を正式な情報源としてお考えください。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解釈について、当方は一切の責任を負いません。