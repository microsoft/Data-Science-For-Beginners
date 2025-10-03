<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cc2e18ab65df63e75d3619c4752e9b22",
  "translation_date": "2025-10-03T11:09:03+00:00",
  "source_file": "AGENTS.md",
  "language_code": "ja"
}
-->
# AGENTS.md

## プロジェクト概要

Data Science for Beginnersは、Microsoft Azure Cloud Advocatesによって作成された包括的な10週間、20レッスンのカリキュラムです。このリポジトリは、プロジェクトベースのレッスンを通じて、Jupyterノートブック、インタラクティブなクイズ、実践的な課題を含む基礎的なデータサイエンスの概念を教える学習リソースです。

**主要技術:**
- **Jupyterノートブック**: Python 3を使用した主要な学習媒体
- **Pythonライブラリ**: pandas、numpy、matplotlibを使用したデータ分析と可視化
- **Vue.js 2**: クイズアプリケーション（quiz-appフォルダー）
- **Docsify**: オフラインアクセス用のドキュメントサイト生成ツール
- **Node.js/npm**: JavaScriptコンポーネントのパッケージ管理
- **Markdown**: すべてのレッスン内容とドキュメント

**アーキテクチャ:**
- 多言語対応の教育リポジトリで広範な翻訳を提供
- レッスンモジュール（1-Introductionから6-Data-Science-In-Wildまで）に構造化
- 各レッスンにはREADME、ノートブック、課題、クイズが含まれる
- 独立したVue.jsクイズアプリケーションでレッスン前後の評価を実施
- GitHub CodespacesとVS Code開発コンテナをサポート

## セットアップコマンド

### リポジトリセットアップ
```bash
# Clone the repository (if not already cloned)
git clone https://github.com/microsoft/Data-Science-For-Beginners.git
cd Data-Science-For-Beginners
```

### Python環境セットアップ
```bash
# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install common data science libraries (no requirements.txt exists)
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### クイズアプリケーションセットアップ
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

### Docsifyドキュメントサーバー
```bash
# Install Docsify globally
npm install -g docsify-cli

# Serve documentation locally
docsify serve

# Documentation will be available at localhost:3000
```

### 可視化プロジェクトセットアップ
meaningful-visualizations（レッスン13）のような可視化プロジェクトの場合:
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


## 開発ワークフロー

### Jupyterノートブックの操作
1. リポジトリのルートでJupyterを開始: `jupyter notebook`
2. 希望するレッスンフォルダーに移動
3. `.ipynb`ファイルを開いて演習を進める
4. ノートブックは説明とコードセルを含む自己完結型
5. ほとんどのノートブックはpandas、numpy、matplotlibを使用 - これらがインストールされていることを確認

### レッスン構成
各レッスンには通常以下が含まれます:
- `README.md` - 理論と例を含む主要なレッスン内容
- `notebook.ipynb` - 実践的なJupyterノートブック演習
- `assignment.ipynb`または`assignment.md` - 練習課題
- `solution/`フォルダー - 解答ノートブックとコード
- `images/`フォルダー - 補助的な視覚資料

### クイズアプリケーション開発
- Vue.js 2アプリケーションで開発中にホットリロードを使用
- クイズは`quiz-app/src/assets/translations/`に保存
- 各言語には独自の翻訳フォルダー（en、fr、esなど）がある
- クイズ番号は0から始まり、39まで（合計40クイズ）

### 翻訳の追加
- 翻訳はリポジトリルートの`translations/`フォルダーに配置
- 各言語は英語の構造を完全にミラーリング
- GitHub Actionsによる自動翻訳（co-op-translator.yml）

## テスト手順

### クイズアプリケーションテスト
```bash
cd quiz-app

# Run lint checks
npm run lint

# Test build process
npm run build

# Manual testing: Start dev server and verify quiz functionality
npm run serve
```

### ノートブックテスト
- ノートブックには自動テストフレームワークが存在しない
- 手動検証: すべてのセルを順番に実行してエラーがないことを確認
- データファイルがアクセス可能で出力が正しく生成されることを確認
- 可視化が正しくレンダリングされることを確認

### ドキュメントテスト
```bash
# Verify Docsify renders correctly
docsify serve

# Check for broken links manually by navigating through content
# Verify all lesson links work in the rendered documentation
```

### コード品質チェック
```bash
# Vue.js projects (quiz-app and visualization projects)
cd quiz-app  # or visualization project folder
npm run lint

# Python notebooks - manual verification recommended
# Ensure imports work and cells execute without errors
```


## コードスタイルガイドライン

### Python（Jupyterノートブック）
- PythonコードのPEP 8スタイルガイドラインに従う
- 分析するデータを説明する明確な変数名を使用
- コードセルの前に説明を含むMarkdownセルを追加
- コードセルは単一の概念または操作に集中させる
- データ操作にはpandas、可視化にはmatplotlibを使用
- 一般的なインポートパターン:
  ```python
  import pandas as pd
  import numpy as np
  import matplotlib.pyplot as plt
  ```


### JavaScript/Vue.js
- Vue.js 2のスタイルガイドとベストプラクティスに従う
- ESLint設定は`quiz-app/package.json`に記載
- Vueの単一ファイルコンポーネント（.vueファイル）を使用
- コンポーネントベースのアーキテクチャを維持
- コミット前に`npm run lint`を実行

### Markdownドキュメント
- 明確な見出し階層（# ## ###など）を使用
- 言語指定付きのコードブロックを含める
- 画像には代替テキストを追加
- 関連するレッスンやリソースへのリンクを追加
- 読みやすさのために行の長さを適切に保つ

### ファイル構成
- レッスン内容は番号付きフォルダー（01-defining-data-scienceなど）に配置
- 解答は専用の`solution/`サブフォルダーに配置
- 翻訳は英語の構造をミラーリングして`translations/`フォルダーに配置
- データファイルは`data/`またはレッスン専用フォルダーに保存

## ビルドとデプロイ

### クイズアプリケーションのデプロイ
```bash
cd quiz-app

# Build production version
npm run build

# Output is in dist/ folder
# Deploy dist/ folder to static hosting (Azure Static Web Apps, Netlify, etc.)
```

### Azure Static Web Appsのデプロイ
クイズアプリはAzure Static Web Appsにデプロイ可能:
1. Azure Static Web Appリソースを作成
2. GitHubリポジトリに接続
3. ビルド設定を構成:
   - アプリの場所: `quiz-app`
   - 出力の場所: `dist`
4. GitHub Actionsワークフローがプッシュ時に自動デプロイ

### ドキュメントサイト
```bash
# Build PDF from Docsify (optional)
npm run convert

# Docsify documentation is served directly from markdown files
# No build step required for deployment
# Deploy repository to static hosting with Docsify
```

### GitHub Codespaces
- リポジトリには開発コンテナ構成が含まれる
- CodespacesはPythonとNode.js環境を自動的にセットアップ
- GitHub UIを介してリポジトリをCodespaceで開く
- すべての依存関係が自動的にインストールされる

## プルリクエストガイドライン

### 提出前
```bash
# For Vue.js changes in quiz-app
cd quiz-app
npm run lint
npm run build

# Test changes locally
npm run serve
```

### PRタイトル形式
- 明確で説明的なタイトルを使用
- フォーマット: `[コンポーネント] 簡単な説明`
- 例:
  - `[Lesson 7] Pythonノートブックのインポートエラーを修正`
  - `[Quiz App] ドイツ語翻訳を追加`
  - `[Docs] 新しい前提条件をREADMEに更新`

### 必須チェック
- すべてのコードがエラーなく実行されることを確認
- ノートブックが完全に実行されることを確認
- Vue.jsアプリが正常にビルドされることを確認
- ドキュメントリンクが機能することを確認
- クイズアプリケーションを変更した場合はテスト
- 翻訳が一貫した構造を維持していることを確認

### 貢献ガイドライン
- 既存のコードスタイルとパターンに従う
- 複雑なロジックには説明コメントを追加
- 関連するドキュメントを更新
- 適用可能な場合は異なるレッスンモジュールで変更をテスト
- CONTRIBUTING.mdファイルを確認

## 追加の注意事項

### 使用される一般的なライブラリ
- **pandas**: データ操作と分析
- **numpy**: 数値計算
- **matplotlib**: データの可視化とプロット
- **seaborn**: 統計データの可視化（一部のレッスン）
- **scikit-learn**: 機械学習（高度なレッスン）

### データファイルの操作
- データファイルは`data/`フォルダーまたはレッスン専用ディレクトリに配置
- ほとんどのノートブックはデータファイルを相対パスで期待
- CSVファイルが主なデータ形式
- 一部のレッスンでは非リレーショナルデータ例としてJSONを使用

### 多言語対応
- GitHub Actionsによる40以上の言語翻訳
- 翻訳ワークフローは`.github/workflows/co-op-translator.yml`に記載
- 翻訳は`translations/`フォルダーに言語コード付きで配置
- クイズ翻訳は`quiz-app/src/assets/translations/`に保存

### 開発環境オプション
1. **ローカル開発**: Python、Jupyter、Node.jsをローカルにインストール
2. **GitHub Codespaces**: クラウドベースの即時開発環境
3. **VS Code開発コンテナ**: ローカルコンテナベースの開発
4. **Binder**: クラウドでノートブックを起動（設定されている場合）

### レッスン内容ガイドライン
- 各レッスンは独立しているが、前の概念を基に構築
- レッスン前のクイズで事前知識をテスト
- レッスン後のクイズで学習を強化
- 課題で実践的な練習を提供
- スケッチノートで視覚的な要約を提供

### よくある問題のトラブルシューティング

**Jupyterカーネルの問題:**
```bash
# Ensure correct kernel is installed
python -m ipykernel install --user --name=datascience
```

**npmインストールの失敗:**
```bash
# Clear npm cache and retry
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
```

**ノートブックのインポートエラー:**
- 必要なライブラリがすべてインストールされていることを確認
- Pythonバージョンの互換性を確認（Python 3.7以上推奨）
- 仮想環境が有効化されていることを確認

**Docsifyが読み込まれない:**
- リポジトリルートから提供していることを確認
- `index.html`が存在することを確認
- 適切なネットワークアクセス（ポート3000）を確認

### パフォーマンスに関する注意事項
- 大規模なデータセットはノートブックで読み込むのに時間がかかる場合がある
- 複雑なプロットの可視化レンダリングが遅くなる可能性がある
- Vue.js開発サーバーはホットリロードを有効にして迅速な反復を可能に
- 本番ビルドは最適化され、縮小される

### セキュリティに関する注意事項
- 機密データや資格情報をコミットしない
- クラウドレッスンでのAPIキーは環境変数を使用
- Azure関連のレッスンではAzureアカウント資格情報が必要な場合がある
- セキュリティパッチのために依存関係を最新に保つ

## 翻訳への貢献
- GitHub Actionsによる自動翻訳管理
- 翻訳の正確性向上のための手動修正歓迎
- 既存の翻訳フォルダー構造に従う
- クイズリンクに言語パラメータを追加: `?loc=fr`
- 翻訳されたレッスンが正しくレンダリングされることをテスト

## 関連リソース
- メインカリキュラム: https://aka.ms/datascience-beginners
- Microsoft Learn: https://docs.microsoft.com/learn/
- Student Hub: https://docs.microsoft.com/learn/student-hub
- ディスカッションフォーラム: https://github.com/microsoft/Data-Science-For-Beginners/discussions
- その他のMicrosoftカリキュラム: ML for Beginners, AI for Beginners, Web Dev for Beginners

## プロジェクトの維持管理
- コンテンツを最新に保つための定期的な更新
- コミュニティの貢献を歓迎
- GitHubで問題を追跡
- カリキュラム管理者によるPRレビュー
- 毎月のコンテンツレビューと更新

---

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。元の言語で記載された文書を正式な情報源としてお考えください。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解釈について、当方は一切の責任を負いません。