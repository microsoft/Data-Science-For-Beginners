<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a64d8afa22ffcc2016bb239188d6acb1",
  "translation_date": "2025-10-03T15:17:06+00:00",
  "source_file": "INSTALLATION.md",
  "language_code": "ja"
}
-->
# インストールガイド

このガイドでは、Data Science for Beginners カリキュラムを使用するための環境設定方法を説明します。

## 目次

- [前提条件](../..)
- [クイックスタートオプション](../..)
- [ローカルインストール](../..)
- [インストールの確認](../..)

## 前提条件

始める前に以下を準備してください：

- コマンドライン/ターミナルの基本的な操作に慣れていること
- GitHubアカウント（無料）
- 初期設定のための安定したインターネット接続

## クイックスタートオプション

### オプション1: GitHub Codespaces（初心者におすすめ）

最も簡単に始められる方法は、ブラウザ上で完全な開発環境を提供するGitHub Codespacesを利用することです。

1. [リポジトリ](https://github.com/microsoft/Data-Science-For-Beginners)に移動します
2. **Code** ドロップダウンメニューをクリックします
3. **Codespaces** タブを選択します
4. **Create codespace on main** をクリックします
5. 環境が初期化されるまで待ちます（2～3分）

これで、すべての依存関係が事前にインストールされた状態で環境が準備完了です！

### オプション2: ローカル開発

自分のコンピュータで作業する場合は、以下の詳細な手順に従ってください。

## ローカルインストール

### ステップ1: Gitのインストール

Gitはリポジトリをクローンし、変更を追跡するために必要です。

**Windows:**
- [git-scm.com](https://git-scm.com/download/win) からダウンロード
- インストーラーをデフォルト設定で実行

**macOS:**
- Homebrewを使用してインストール: `brew install git`
- または [git-scm.com](https://git-scm.com/download/mac) からダウンロード

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

### ステップ2: リポジトリのクローン

```bash
# Clone the repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Navigate to the directory
cd Data-Science-For-Beginners
```

### ステップ3: PythonとJupyterのインストール

データサイエンスのレッスンにはPython 3.7以上が必要です。

**Windows:**
1. [python.org](https://www.python.org/downloads/) からPythonをダウンロード
2. インストール時に「Add Python to PATH」をチェック
3. インストールを確認：
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

### ステップ4: Python環境のセットアップ

依存関係を分離するために仮想環境を使用することを推奨します。

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### ステップ5: Pythonパッケージのインストール

必要なデータサイエンスライブラリをインストールします：

```bash
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### ステップ6: Node.jsとnpmのインストール（クイズアプリ用）

クイズアプリケーションにはNode.jsとnpmが必要です。

**Windows/macOS:**
- [nodejs.org](https://nodejs.org/) からダウンロード（LTSバージョン推奨）
- インストーラーを実行

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

### ステップ7: クイズアプリの依存関係をインストール

```bash
# Navigate to quiz app directory
cd quiz-app

# Install dependencies
npm install

# Return to root directory
cd ..
```

### ステップ8: Docsifyのインストール（オプション）

ドキュメントをオフラインで利用するために：

```bash
npm install -g docsify-cli
```

## インストールの確認

### PythonとJupyterのテスト

```bash
# Activate your virtual environment if not already activated
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Start Jupyter Notebook
jupyter notebook
```

ブラウザが開き、Jupyterインターフェイスが表示されます。任意のレッスンの`.ipynb`ファイルに移動できます。

### クイズアプリケーションのテスト

```bash
# Navigate to quiz app
cd quiz-app

# Start development server
npm run serve
```

クイズアプリは`http://localhost:8080`（8080ポートが使用中の場合は別のポート）で利用可能です。

### ドキュメントサーバーのテスト

```bash
# From the root directory of the repository
docsify serve
```

ドキュメントは`http://localhost:3000`で利用可能です。

## VS Code Dev Containersの使用

Dockerがインストールされている場合、VS Code Dev Containersを使用できます：

1. [Docker Desktop](https://www.docker.com/products/docker-desktop) をインストール
2. [Visual Studio Code](https://code.visualstudio.com/) をインストール
3. [Remote - Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) をインストール
4. VS Codeでリポジトリを開く
5. `F1`を押して「Remote-Containers: Reopen in Container」を選択
6. コンテナのビルドを待つ（初回のみ）

## 次のステップ

- カリキュラムの概要については [README.md](README.md) を参照
- 一般的なワークフローや例については [USAGE.md](USAGE.md) を読む
- 問題が発生した場合は [TROUBLESHOOTING.md](TROUBLESHOOTING.md) を確認
- 貢献したい場合は [CONTRIBUTING.md](CONTRIBUTING.md) をレビュー

## ヘルプを得る

問題が発生した場合：

1. [TROUBLESHOOTING.md](TROUBLESHOOTING.md) ガイドを確認
2. 既存の [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues) を検索
3. [Discordコミュニティ](https://aka.ms/ds4beginners/discord) に参加
4. 問題の詳細情報を記載して新しいIssueを作成

---

**免責事項**:  
この文書は、AI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知ください。元の言語で記載された文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解釈について、当方は一切の責任を負いません。